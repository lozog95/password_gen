pipeline {
environment {
    registry = "lozog95/pass_gen_service"
    registryCredential = 'dockerhub'
  }
    agent any
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
            agent any
            steps{
                script {
                    dockerImage = docker.build registry + ":$BUILD_NUMBER"
                    docker.withRegistry( '', registryCredential ) {
                        dockerImage.push()
                    }
                }
                sh "docker service update --image lozog95/pass_gen_service:${BUILD_NUMBER} password-service"

            }
        }


    }
}


