pipeline {
    agent any
    stages {
        stage('Pytest') {
            steps {
                echo 'Executing pytest unittest'
                sh 'ls'
                sh 'source venv/bin/activate'
                sh 'pip3 install -r requirements.txt --user'
                sh 'python3 -m pytest'
            }
        }
        stage('Behave') {
            steps {
                sh 'echo Executing feature tests'
                sh 'python3 -m behave -f allure_behave.formatter:AllureFormatter -o allure_results tests/features'
            }
        }
    }
    post {
        always {
            mail to:'jas.rajabov@gmail.com', subject:"${currentBuild.fullDisplayName}", body: "Build "
        }
    }
}