pipeline {
    agent {label "mainnode"}
    options {
        buildDiscarder logRotator(artifactDaysToKeepStr: '', artifactNumToKeepStr: '5', daysToKeepStr: '', numToKeepStr:'5')
        disableConcurrentBuilds()
    }
    stages {
        stage('modules'){
            steps{
                sh 'pip3 install flask'
            }
        }
        stage('hello'){
            steps {
                sh 'python3 print("aa")'
            }
        }
    }
}
