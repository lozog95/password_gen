pipeline {
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