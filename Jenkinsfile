pipeline {
  agent {
    docker { image 'python:3.6.5-alpine' }
  }
  stages {
    stage('Prepare environment') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('Run unit tests') {
      steps {
        sh 'pytest -v tests/'
      }
    }
  }
}