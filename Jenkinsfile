pipeline {
    agent any
    stages {
        stage('Pytest') {
            steps {
                echo 'Executing pytest unittest'
                sh 'pip install -r requirements.txt'
            }
        }
    }
    post {
        always {
            echo 'This is post message'
        }
    }
}