import os
import subprocess
import pandas as pd
from Bio import SeqIO
import logging

def setup_logging():
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

def convert_txt_to_fasta(txt_file, fasta_file):
    """Converts a TXT file with sequences into a FASTA file."""
    with open(txt_file, "r") as infile, open(fasta_file, "w") as outfile:
        for i, line in enumerate(infile):
            outfile.write(f">hsdM_gene_{i+1}\n{line.strip()}\n")

def make_blast_db(fasta_file, db_name="assembly_db"):
    """Creates a BLAST database from the given FASTA file."""
    cmd = f"makeblastdb -in {fasta_file} -dbtype nucl -out {db_name}"
    subprocess.run(cmd, shell=True, check=True)
    return db_name

def run_blast(query_file, db_name, output_file="blast_results.txt", num_threads=4):
    """Runs BLASTN to search for hsdM sequences in the assembly with multi-threading."""
    cmd = f"blastn -query {query_file} -db {db_name} -out {output_file} -outfmt '6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore' -num_threads {num_threads}"
    subprocess.run(cmd, shell=True, check=True)
    return output_file

def filter_and_save_results(blast_output, min_identity=90.0, min_coverage=80.0, csv_output="filtered_results.csv"):
    """Filters BLAST results by identity and coverage, then saves to CSV."""
    col_names = ["qseqid", "sseqid", "pident", "length", "mismatch", "gapopen", "qstart", "qend", "sstart", "send", "evalue", "bitscore"]
    df = pd.read_csv(blast_output, sep="\t", names=col_names)
    
    # Calculate query coverage
    df["query_length"] = df["qend"] - df["qstart"] + 1
    df["coverage"] = (df["query_length"] / df["length"]) * 100
    
    # Filter based on identity and coverage
    df_filtered = df[(df["pident"] >= min_identity) & (df["coverage"] >= min_coverage)]
    
    if df_filtered.empty:
        logging.info("No significant matches found based on filtering criteria.")
    else:
        logging.info(f"✅ BLAST search completed! Found {len(df_filtered)} matching sequences.")
        logging.info("📊 Top 5 Matches:")
        top_hits = df_filtered.sort_values(by=['pident', 'coverage'], ascending=[False, False]).head(5)
        for i, row in top_hits.iterrows():
            logging.info(f"  {i+1}. Query: {row['qseqid']} | Match: {row['sseqid']} | Identity: {row['pident']}% | Coverage: {row['coverage']}%")
    
    # Save to CSV
    df_filtered.to_csv(csv_output, index=False)
    logging.info(f"📁 Full results saved to: {csv_output}")

def scan_hsdM_in_assembly(assembly_fasta, hsdM_input):
    """Scans an assembly FASTA file for hsdM sequences."""
    setup_logging()
    hsdM_fasta = "hsdM.fasta"
    
    if hsdM_input.endswith(".txt"):
        logging.info("Converting TXT to FASTA...")
        convert_txt_to_fasta(hsdM_input, hsdM_fasta)
    else:
        hsdM_fasta = hsdM_input
    
    logging.info("Creating BLAST database...")
    db_name = make_blast_db(assembly_fasta)
    logging.info("Running BLAST search...")
    output_file = run_blast(hsdM_fasta, db_name)
    
    logging.info("Filtering and saving results...")
    filter_and_save_results(output_file)
    
if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Scan an assembly FASTA file for hsdM sequences.")
    parser.add_argument("assembly", help="Path to the assembly FASTA file")
    parser.add_argument("hsdM", help="Path to the hsdM gene sequences FASTA or TXT file")
    parser.add_argument("--threads", type=int, default=4, help="Number of BLAST threads (default: 4)")
    parser.add_argument("--min_identity", type=float, default=90.0, help="Minimum identity percentage (default: 90.0)")
    parser.add_argument("--min_coverage", type=float, default=80.0, help="Minimum query coverage percentage (default: 80.0)")
    args = parser.parse_args()
    
    scan_hsdM_in_assembly(args.assembly, args.hsdM)
