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

        stage('Ansible Deployment') {
            steps {
                echo 'Deploying application using Ansible...'
                sh '''
                    ansible-playbook \
                    -i ansible/inventory \
                    ansible/deploy.yml
                '''
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
