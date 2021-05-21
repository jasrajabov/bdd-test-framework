pipeline {
    agent any
    triggers {
    //runs every 15 min between 1-2 pm every weekend
        cron('H/15 13-14 * * 6-7')
    }
    stages {
        stage('Tests') {
            parallel {
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
        }
    }
    post {
        always {
            emailext body: 'BUILD STATS: $DEFAULT_CONTENT',
            subject: '$DEFAULT_SUBJECT',
            to: 'razhabov@yahoo.com'
        }
    }
}