## hsdM BLAST Scanner

### Overview
This tool scans genome assembly FASTA files to detect **hsdM gene sequences** using **BLASTN**. A pre-built BLAST database (`hsdM_db`) created using the hsdM gene sequences extracted from the Restriction Enzyme dataBASE (Roberts, R.J., Vincze, T., Posfai, J., Macelis, D. REBASE: a database for DNA restriction and modification: enzymes, genes and genomes. Nucleic Acids Res. 51: D629-D630 (2023). doi: 10.1093/nar/gkac975) is provided for faster searches on entire genome irrespective of its size!

### Description
The hsdM BLAST Scanner is a powerful tool designed to help researchers detect hsdM gene sequences in genome assembly FASTA files. By leveraging the BLASTN algorithm, this tool compares the input genomes against a pre-built BLAST database of hsdM gene sequences for efficient and accurate sequence identification.

Ideal for genomic studies focused on the hsdM gene in prokaryotic genomes, the scanner supports multi-threading for fast searches on large datasets and provides customizable filters for sequence identity and coverage. Output is generated both as console reports for top matches and detailed results stored in a CSV file for further analysis.

This tool is essential for anyone working on hsdM gene detection and provides an easy-to-use, reliable solution for integrating genomic data analysis into research workflows.

### Installation
#### Prerequisites:
- Python (≥3.7)
- [BLAST+](https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/)
- Biopython & Pandas:  
  ```bash
  pip install biopython pandas
  ```

### Downloading hsdM Data
To obtain the latest **hsdM gene sequences** from REBASE FTP, use:
```bash
wget ftp://ftp.neb.com/pub/rebase/All_Type_I_M_subunit_genes_DNA.txt -O hsdM_sequences.txt
```
### BLAST Database Files
This project requires the following BLAST database files for usage with blastn or blastdbcmd.

```
hsdM_db.nsq.gz → Contains nucleotide sequence data (Please extrcat before utilising)
hsdM_db.nhr → Contains BLAST database index
hsdM_db.nin → Contains BLAST index file
```


### Usage

#### **Command Line Usage**
```bash
python scan_hsdM.py assembly.fasta --blastdb hsdM_db --threads 8 --min_identity 95 --min_coverage 85
```

#### **As a Python Module**
```python
from scan_hsdM import scan_hsdM_in_assembly
scan_hsdM_in_assembly("assembly.fasta", blastdb="hsdM_db")
```

### Output
- Top matches are printed
- Full results saved in `filtered_results.csv`

### Files
#### **.gitignore**
```
# Ignore BLAST database files
*.nhr
*.nin
*.nsq
*.log
*.csv
```

#### **requirements.txt**
```
biopython
pandas
```

### Contributing
Pull requests are welcome!

### License
This project is licensed under the MIT License. See the LICENSE file for details. MIT License © 2025 Susanth Alapati (Clinical Research Fellow) & Karolin Hijazi (Primary Investigator) at University of Aberdeen.
