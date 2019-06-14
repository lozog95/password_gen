pipeline {
  environment {
    registry = "lozog95/pass_gen_service"
    registryCredential = 'dockerhub'
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
    stage('Build and deploy image') {
    agent {
      docker {
        image 'docker:latest'
        args '-u root:root'
     }
  }
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
  post {
        always {
            junit '*.xml'
        }
    }
}