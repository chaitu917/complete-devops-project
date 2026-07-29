pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking project files...'
                sh 'pwd'
                sh 'ls -la'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh 'docker-compose build'
            }
        }

        stage('Deploy Application') {
            steps {
                echo 'Stopping old application...'
                sh 'docker-compose down || true'

                echo 'Starting new application...'
                sh 'docker-compose up -d --build'

                echo 'Checking running containers...'
                sh 'docker-compose ps'
            }
        }

        stage('Health Check') {
            steps {
                echo 'Checking application health...'
                sh 'sleep 5'
                sh 'curl -f http://localhost:5001/health'
            }
        }
    }

    post {
        success {
            echo 'CI/CD Pipeline completed successfully!'
        }

        failure {
            echo 'CI/CD Pipeline failed!'
        }
    }
}



