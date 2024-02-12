pipeline {
    agent {label "mainnode"}
    options {
        buildDiscarder logRotator(artifactDaysToKeepStr: '', artifactNumToKeepStr: '5', daysToKeepStr: '', numToKeepStr:'5')
        disableConcurrentBuilds()
    }
    stages {
        stage("check syntax"){
            steps{
                script{
                    def syntaxError
                    syntaxError = sh (
                        script:'python3 -m py_compile simpleServer.py',
                        returnStdout: true
                    )
                    if(syntaxError?.trim())
                    {
                        currentBuild.result = 'ABORTED'
                        error('Syntax Error')
                        echo ('Syntax error: ${syntaxError}')
                    }
                }
            }
        }
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
                        script: 'curl http://localhost:8001/hello/daniel',
                        returnStdout: true
                    ).trim()
                    if (a == 'hello daniel'){
                        currentBuild.result = 'SUCCESS'
                    }else{
                        currentBuild.result = 'FAILURE'
                        echo 'Output doesnt match input'
                    }
                    sh 'sudo docker stop $(sudo docker ps -a -q)'
                    sh 'sudo docker rm $(sudo docker ps -a -q)'
                }
            }
        }
    }
}
