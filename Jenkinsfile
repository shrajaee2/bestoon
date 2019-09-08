pipeline {
  agent {
    docker {
      image 'python'
      args '-p 8080:8080'
    }

  }
  stages {
    stage('pre-build') {
      agent any
      steps {
        echo 'First Step'
        git(url: 'https://github.com/shrajaee2/bestoon.git', branch: 'master')
        echo 'end of step one'
      }
    }
    stage('Fetching Docker...') {
      agent {
        docker {
          image 'python'
        }

      }
      steps {
        sh 'echo "Fetching Python Docker"'
      }
    }
  }
}