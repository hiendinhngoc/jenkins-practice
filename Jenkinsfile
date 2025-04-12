pipeline {
    agent { dockerfile true } // Use a Dockerfile to build the agent

    stages {
        stage('Checkout') {
            steps {
                git 'git@github.com:hiendinhngoc/jenkins-practice.git'
            }
        }
        stage('Build') {
            steps {
                sh 'docker build -t flask-app:latest .'
            }
        }
        stage('Test') {
            steps {
                sh 'python -m unittest tests/test_app.py'
            }
        }
        stage('Deploy') {
            steps {
                sh 'echo "Deploying the application..."'
                sh 'docker run -d -p 5000:5000 flask-app:latest'
            }
        }
    }
} 