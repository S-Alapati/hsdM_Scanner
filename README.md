## hsdM BLAST Scanner

### Overview
This tool scans genome assembly FASTA files to detect **hsdM gene sequences** using **BLASTN**. A pre-built BLAST database (`hsdM_db`) is provided for faster searches.

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
wget ftp://ftp.neb.com/pub/rebase/hsdM.txt -O hsdM_sequences.txt
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

#### **LICENSE (MIT License)**
```
MIT License

Copyright (c) 2025 Susanth & Karolin Hijazi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

[...] (full MIT license text)
```

#### **requirements.txt**
```
biopython
pandas
```

### Contributing
Pull requests are welcome!

### License
MIT License © 2025 Susanth & Karolin Hijazi
