pipeline {
    agent {label "mainnode"}
    options {
        buildDiscarder logRotator(artifactDaysToKeepStr: '', artifactNumToKeepStr: '5', daysToKeepStr: '', numToKeepStr:'5')
        disableConcurrentBuilds()
    }
    stages {
        stage('hello'){
            steps {
                if((python -m py_compile main.py) == ''){
                    echo "clean"
                }
            }
        }
    }
}