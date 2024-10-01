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
                script {
                    sh 'python3 -m unittest tests.py'
                }
            }
        }

        stage('Run Unit Tests') {
            steps {
                script {
                    sh 'pwd'
                }
            }
        }
    }
}