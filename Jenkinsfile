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
                   date
                   '''
               }
           }
           stage('Run Unit Tests') {
               steps {
                   sh '''
                   date
                   '''
               }
           }
       }
   }
