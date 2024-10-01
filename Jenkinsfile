pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Install Python 3 and pip') {
            steps {
                script {
                    sh '''
                        sudo apt-get update
                        sudo apt-get install -y python3
                        sudo apt-get install -y python3-pip
                    '''
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