pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/TheDanz/Seminar_Lab4'
            }
        }
        
        stage('Setup Python Environment') {
            steps {
                script {
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Run Unit Tests') {
            steps {
                script {
                    sh 'python3 -m unittest tests.py'
                }
            }
        }
    }
}