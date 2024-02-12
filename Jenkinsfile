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
                    def  a 
                    a = sh (
                        script: 'curl http://localhost:8001/hello/amit',
                        returnStdout: true
                    ).trim()
                    if (a == 'hello daniel'){
                        currentBuild.result = 'SUCCESS'
                    }else{
                        currentBuild.result = 'FAILURE'
                    }
                    sh 'docker stop $(docker ps -a -q)'
                    sh 'docker rm $(docker ps -a -q)'
                }
            }
        }
    }
}
