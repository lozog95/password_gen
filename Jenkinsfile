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
    stage('Building image') {
      steps{
        script {
          dockerImage = docker.build registry + ":latest"
        }
      }
    }
    stage('Deploy Image') {
      steps{
        script {
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