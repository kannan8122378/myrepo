pipeline{
    agent any
    
    tools{
        maven 'Maven'
    stages{
        stage(Build stage){
            steps{
                bat 'mvn -v' 
                bat 'mvn clean install'
            }
        }
    }
}
