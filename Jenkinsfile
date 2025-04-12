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
                sh 'python3 -m pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 -m unittest tests/test_app.py'
            }
        }
        stage('Run') {
            steps {
                sh 'python3 app.py'
            }
        }
    }
} 