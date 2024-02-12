pipeline {
    agent {label "mainnode"}
    options {
        buildDiscarder logRotator(artifactDaysToKeepStr: '', artifactNumToKeepStr: '5', daysToKeepStr: '', numToKeepStr:'5')
        disableConcurrentBuilds()
    }
    stages {
        stage("version"){
            steps{
                sh 'sudo docker build -t simpleserver:latest .'
            }
        }
        stage('hello'){
            steps {
                sh 'sudo docker run -d -p 8001:8001 simpleserver:latest'
            }
        }
        stage('check_working'){
            steps {
                script{
                    def  a = sh (
                        script: 'curl http://localhost:8001/hello/daniel',
                        returnStdout: true
                    ).trim()
                }
                echo "Build full flag: ${a}"
            }
        }
    }
}
