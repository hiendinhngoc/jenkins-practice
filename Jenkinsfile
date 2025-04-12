pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/hiendinhngoc/jenkins-practice.git'
            }
        }
        stage('Setup') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'python -m unittest tests/test_app.py'
            }
        }
        stage('Run') {
            steps {
                sh 'python app.py'
            }
        }
    }
} 