pipeline{
    agent any
    
    tools{
        maven 'Maven'
    stages{
        stage(Build stage){
            steps{
                sh 'mvn -v' 
                sh 'mvn clean install'
            }
        }
    }
}
