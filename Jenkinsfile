pipeline {
    agent any
    stages {
        stage('Pytest') {
            steps {
                echo 'Executing pytest unittest'
                sh 'ls'
                sh 'source venv/bin/activate'
                sh 'pip3 install -r requirements.txt --user'
            }
        }
    }
    post {
        always {
            echo 'This is post message'
        }
    }
}