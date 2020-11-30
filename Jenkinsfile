pipeline {
  agent { docker { 
  			label 'windows'
  			image 'python:3' 
  			} }
  stages {
    stage('build') {
      steps {
        sh 'python test.py'
      }
    }
  }
}