# Cybersecurity Scripts

A simple automation with python to analyze log activities in your system 

## Table of Contents

- [About](#about)
- [Installation](#installation)
- [Usage](#usage)


## About

The `simple_log_analysis.py` script is a simple Python tool designed for automating the analysis of log files in a Linux environment. It can help you analyze log files and gather insights from them, specifically tailored for Apache web server access logs.

Key features and objectives of the script include:

- Parsing Apache access log files to extract relevant information.
- Analyzing the log data to provide essential statistics, such as the total number of requests and HTTP status codes.
- Easy customization for different log file formats and analysis requirements.

Whether you want to monitor the health of your web server, identify security issues, or troubleshoot problems, this script offers a foundation for log file analysis. It is designed to be a starting point that you can adapt and extend to fit your specific needs.



### Installation 


1. Clone the repository 

    git clone `git@github.com:rodrigocolozio/cybersecurity-.git`

2. Change to the repository's directory 

    cd your_directory

3. Make the script executable
    sudo chmod +x simple_log_analisis.py


### Usage 

Once inside the respective directory

1. Run the project
    python3 simple_log_analysis.py /your/log/path/goes/here





