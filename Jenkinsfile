pipeline {
    agent { docker { image 'python:3.11.2' } }
    options {
        buildDiscarder logRotator(artifactDaysToKeepStr: '', artifactNumToKeepStr: '5', daysToKeepStr: '', numToKeepStr:'5')
        disableConcurrentBuilds()
    }
    stages {
        stage('pip installs'){
            steps {
                sh 'pip3 install flash'
                sh 'python3 print("aa")'
            }
        }
    }
}
