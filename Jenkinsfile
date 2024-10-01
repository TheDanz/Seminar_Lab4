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
                    sh "echo $(pwd)"
                }
            }
        }

        stage('Run Unit Tests') {
            steps {
                script {
                    sh "echo $(pwd)"
                }
            }
        }
    }
}