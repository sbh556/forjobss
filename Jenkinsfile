pipeline {
    agent {
        docker{
            image 'python:3'
            lable 'mainnode'
        }
    }
    options {
        buildDiscarder logRotator(artifactDaysToKeepStr: '', artifactNumToKeepStr: '5', daysToKeepStr: '', numToKeepStr:'5')
        disableConcurrentBuilds()
    }
    stages {
        stage("version"){
            steps{
                sh 'python3 --version'
            }
        }
        stage('hello'){
            steps {
                sh 'python3 print("aa")'
            }
        }
    }
}