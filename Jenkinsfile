pipeline {
    agent {label "mainnode"}
    options {
        buildDiscarder logRotator(artifactDaysToKeepStr: '', artifactNumToKeepStr: '5', daysToKeepStr: '', numToKeepStr:'5')
        disableConcurrentBuilds()
    }
    stages {
        stage('hello'){
            steps {
                if((sh 'python print("test")') == ''){
                    echo "clean"
                }
            }
        }
    }
}