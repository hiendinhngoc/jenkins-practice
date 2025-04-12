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
                sh '''
                    # Debug network information
                    echo "=== Network Information ==="
                    ip addr
                    netstat -tulpn
                    
                    # Run Flask with explicit host binding
                    FLASK_APP=app.py FLASK_ENV=development flask run --host=0.0.0.0 > flask.log 2>&1 &
                    echo $! > flask.pid
                    sleep 5
                    
                    # Show Flask logs
                    echo "=== Flask Logs ==="
                    cat flask.log
                    
                    # Test connection
                    echo "=== Testing Connection ==="
                    curl -v http://localhost:5000 || true
                    curl -v http://127.0.0.1:5000 || true
                '''
            }
        }
    }
    post {
        always {
            sh '''
                if [ -f flask.pid ]; then
                    kill $(cat flask.pid) || true
                    rm flask.pid
                fi
            '''
        }
    }
} 