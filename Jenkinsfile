pipeline {
    agent {label "mainnode"}
    options {
        buildDiscarder logRotator(artifactDaysToKeepStr: '', artifactNumToKeepStr: '5', daysToKeepStr: '', numToKeepStr:'5')
        disableConcurrentBuilds()
    }
    stages {
        stage("version"){
            steps{
                sh 'docker build -t simpleserver:latest .'
            }
        }
        stage('hello'){
            steps {
                sh 'docker run -d -p 8001:8001 --name server1 simpleserver:latest'
            }
        }
        stage('check_working'){
            steps {
                script{
                    def  DATA_RETURNS = sh (
                        script: 'curl http://localhost:8001/hello/daniel',
                        returnStdout: true
                    ).trim()
                }
                echo "ABuild full flag: ${DATA_RETURNS}"
            }
        }
    }
}
