# Software Graph Analytics Workshop

This repository contains material for my Software Analytics workshop  @ Software Architecture Summit 2024 in Munich.

## Slides

You can download the slides here: [Download](https://nextcloud.innoq.io/index.php/s/c9SLsMy7x6as4MN/download)

## Online data analysis platform
To play around with the content online, please press the button: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/feststelltaste/sas2024/HEAD?urlpath=%2Fnotebooks%2F)

### Alternatively: choose your online server

* https://ovh2.mybinder.org/
* https://notebooks.gesis.org/binder/ (rather lame)

You need to place the URL of this repository into the field "GitHub repository name or URL" and press the "launch" button. After launching, you need to change the url part `lab` to `notebooks`.

## Local installation

Please use a local installation if you want to access the Neo4j database and/or want to play around with your own data.

### Prerequisites
- Linux-based operating system, MacOS or Windows Subsystem for Linux (wsl)
- Java 8+ JDK installation (https://openjdk.org/install/) for running a local Neo4j graph database installation
- Anaconda (or similar) Python-based data analysis platform (https://www.anaconda.com/products/distribution)

### Next steps
- Check out this repository (`git clone https://github.com/feststelltaste/sas2024`)
- Install all the needed dependencies for your Python environment (see `requirements.txt`) with pip -r `requirements.txt`
- Execute the bash script `postBuild` (`sh ./postBuild`), which will download and configure a local Neo4j installation
- Execute the bash script `start` (sh ./start) to start the local Neo4j server
- Start Jupyter notebook in the repository directory (with `jupyter notebook`)
- Open up a browser with the shown URL from the Jupyter notebook server
- Have fun!

### Stopping Neo4j
- Execute the bash script `stop` (`sh ./stop`)

## Further information

For more information, visit [https://softwareanalytics.de/](https://softwareanalytics.de/)!

## Feedback? Problems?

Feel free to reach out via new issues or contact Markus via LinkedIn (https://www.linkedin.com/in/markus-harrer/).
