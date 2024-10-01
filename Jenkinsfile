pipeline {
    agent any  // Запускаем на любом доступном агенте Jenkins

    stages {
        stage('Checkout') { 
            steps {
                // Извлечение кода из репозитория GitHub
                git url: 'https://github.com/TheDanz/Seminar_Lab4'
            }
        }

        stage('Setup Python Environment') {
            steps {
                // Устанавливаем Python и виртуальную среду
                sh '''
                # Проверяем и устанавливаем pyenv для управления версиями Python (если требуется)
                if ! command -v pyenv &> /dev/null
                then
                    curl https://pyenv.run | bash
                    export PATH="/root/.pyenv/bin:$PATH"
                    eval "$(pyenv init --path)"
                    eval "$(pyenv virtualenv-init -)"
                fi

                # Установка необходимой версии Python
                pyenv install -s 3.8.0
                pyenv global 3.8.0
                
                # Создаем и активируем виртуальную среду
                python -m venv venv
                source venv/bin/activate
                
                # Устанавливаем зависимости из requirements.txt
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                // Запускаем модульные тесты
                sh '''
                source venv/bin/activate
                python -m unittest tests.py
                '''
            }
        }
    }

    post {
        always {
            // Удаляем виртуальную среду после завершения работы пайплайна
            sh 'rm -rf venv'
        }
        success {
            echo 'Pipeline завершен успешно!'
        }
        failure {
            echo 'Pipeline завершился с ошибкой.'
        }
    }
}