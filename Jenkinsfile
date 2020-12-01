pipeline {
  agent { docker { image 'python:3' } }
  stages {
    stage('build') {
      steps {
      	sh """
      	pip install numpy 
        python -m test.py
        """
      }
    }
  }
}