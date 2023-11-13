
# Jardeen : test automation

This repository houses a collection of automation scripts dedicated to test cases for the evolving application, Jardeen. 



## Demo

![gif_projet_4_demo](https://github.com/eql63/jardeen/assets/150632054/851dee1e-fe87-44fa-8859-179b32d1f48e)



## How to use it

Requirements : 
- Python >= 3.10
- Have followed the procedure for installing and launching the Jardeen application on http://localhost:8080/index.xhtml

### First step:
Clone this repo with Git or download manually the ZIP file.

```bash
  git clone https://github.com/eql63/jardeen.git
```
### Second step: 
Install requirements :
```bash
  pip install -r requirements.txt
```
Note: use virtual environments such as VENV

### Third étape : test case execution
Automated test cases use the same names as on Squash. For example, if you want to run the ADP-01 test case present on Squash, you need to enter the following command:
```bash
  python adp-01.py
```

In this POC, only 3 test cases were automated:
- adp-01
- adp-02
- adp-03
