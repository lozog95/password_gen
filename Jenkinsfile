pipeline {
environment {
    registry = "lozog95/pass_gen_service"
    registryCredential = 'dockerhub'
  }
    agent none
    stages {
        stage("Init and test") {
            agent {
              docker {
              image 'python:3.6.5-alpine'
              args '-u root:root'
              }
            }
            stages {
               stage('Prepare environment') {
                 steps {
                   sh 'pip install -r requirements.txt'
                 }
               }
               stage('Run unit tests') {
                 steps {
                   sh 'python -m pytest --junitxml=tests.xml -v tests/'
                 }
               }
            }
            post {
              always {
                junit '*.xml'
              }
            }
        }
        stage("Build and deploy"){
            agent none
            stages {
                stage('Build and deploy image') {
                    steps{
                script {
          dockerImage = docker.build registry + ":latest"
          docker.withRegistry( '', registryCredential ) {
            dockerImage.push()
          }
        }
      }
    }
            }
        }
    }
}


