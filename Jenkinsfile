pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building the project...'
                sh 'mvn clean install'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'mvn test'
            }
        }
         stage('Install JDK') {
            steps {
                echo 'Install JDK'
                sh '''sudo apt-get update -y sudo apt-get install -y openjdk-17-jdk java -version'''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying the application...'
                // Add deployment commands here
            }
        }
    }
}
