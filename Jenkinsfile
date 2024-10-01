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
                    sh 'date'
                }
            }
        }

        stage('Run Unit Tests') {
            steps {
                script {
                    sh 'date'
                }
            }
        }
    }
}