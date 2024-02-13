# Tucil1_13522148 - Cyberpunk 2077 Breach Protocol Solver
This repository is an archive of files for Tugas Kecil 1 IF2211 Strategi Algoritma.

## Table of Contents
  - [Table of Contents](#table-of-contents)
  - [General Information](#general-information)
  - [Contributor](#contributor)
  - [Technologies Used](#technologies-used)
  - [Structure](#structure)
  - [How to Use](#how-to-use)
    - [Installation](#installation)
    - [Program Execution](#program-execution)

## General Information
This program is designed to solve the Breach Protocol mini-game found in Cyberpunk 2077. Breach Protocol is a hacking mini-game where the player needs to input a sequence of codes within a grid-based interface to gain rewards. The approach employed in solving this task is the brute force method, which entails systematically exploring all potential paths through the code matrix. By exhaustively exploring each combination of codes, the program calculates the rewards obtained by comparing the buffer contents with the required sequence. This comprehensive analysis enables the determination of the most effective path to successfully complete the Breach Protocol mini-game.

## Contributor
13522148 Auralea Alvinia Syaikha

## Technologies Used
- Python

## Structure

```
├── README.md
├── bin
│   └── read.txt
│
├── doc
│   └── Tucil1_K3_13522148_Auralea Alvinia Syaikha.pdf
│
├── src
│   ├── main.py
│   ├── matrix.py
│   ├── readCLI.py
│   ├── readFile.py
│   ├── recursive.py
│   ├── sequence.py
│   └── tokenin.py
│ 
└── test
    ├── sol1.txt
    ├── sol2.txt
    ├── sol3.txt
    ├── sol4.txt
    ├── sol5.txt
    ├── sol6.txt
    ├── test.txt
    ├── test1.txt
    └── test2.txt
    
```

---

## How to Use

### Installation
- Download and install [Python](https://www.python.org/downloads/)
- Download all folder and files on this repository or simply clone this repo!

### Program Execution
    git clone https://github.com/auraleaas/Tucil1_13522148
    cd Tucil1_13522148
    cd src
    python main.py
