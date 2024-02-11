pipeline {
    agent {label "mainnode"}
    options {
        buildDiscarder logRotator(artifactDaysToKeepStr: '', artifactNumToKeepStr: '5', daysToKeepStr: '', numToKeepStr:'5')
        disableConcurrentBuilds()
    }
    stages {
        stage("version"){
            steps{
                sh 'sudo apt install python3 -y'
            }
        }
        stage('hello'){
            steps {
                sh 'nohup python3 simpleServer.py'
            }
        }
    }
}
