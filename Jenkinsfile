pipeline {
environment {
    registry = "lozog95/pass_gen_service"
    registryCredential = 'dockerhub'
  }
    agent none
    stages {
        stage("path"){
            steps {
                sh 'source /Users/lozog/.zshenv'
            }
        }
        stage("Init and test") {
            environment {
                PATH = "$PATH:/usr/local/bin"
            }
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
        environment {
                PATH = "$PATH:/usr/local/bin"
            }
            agent none
            stages {
                stage('Build and deploy image') {
                    steps{
                script {
          dockerImage = docker.build registry + ":$BUILD_NUMBER"
          docker.withRegistry( '', registryCredential ) {
            dockerImage.push()
          }
        }
        sh "kubectl set image deployment/password-service password-service=lozog95/pass-gen-service:${BUILD_NUMBER}"
      }
    }
            }
        }
    }
}


