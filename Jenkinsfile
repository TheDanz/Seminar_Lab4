 pipeline {
       agent any

       stages {
           stage('Checkout') {
               steps {
                   checkout scm
               }
           }
           stage('Setup Python Environment') {
               steps {
                   sh '''
                   python3 -m venv venv
                   . venv/bin/activate
                   pip install -r requirements.txt
                   '''
               }
           }
           stage('Run Unit Tests') {
               steps {
                   sh '''
                   . venv/bin/activate
                   python3 -m unittest test.py
                   '''
               }
           }
       }
   }
