pipeline {
    agent {label "mainnode"}
    options {
        buildDiscarder logRotator(artifactDaysToKeepStr: '', artifactNumToKeepStr: '5', daysToKeepStr: '', numToKeepStr:'5')
        disableConcurrentBuilds()
    }
    stages {
        stage('pip installs'){
            steps {
                sh 'pip3 install flask'
                sh 'python3 print("aa")'
            }
        }
    }
}
