pipeline {
    agent {label "Built-In Node"}
    options {
        buildDiscarder logRotator(artifactDaysToKeepStr: '', artifactNumToKeepStr: '5', daysToKeepStr: '', numToKeepStr:'5')
        disableConcurrentBuilds()
    }
    stages {
        stage('hello'){
            steps {
                echo "hello"
            }
        }
    }
}