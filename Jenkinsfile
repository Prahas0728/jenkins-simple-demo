pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                // Pulls your code from GitHub
                git url: 'https://github.com/Prahas0728/jenkins-simple-demo.git', 
                    branch: 'main'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Builds the image using the Dockerfile in your repo
                    sh 'docker build -t my-python-app:latest .'
                }
            }
        }

        stage('Deploy Container') {
            steps {
                script {
                    // 1. Stop and remove the old container if it exists (to avoid port conflicts)
                    sh 'docker stop my-running-app || true'
                    sh 'docker rm my-running-app || true'
                    
                    // 2. Run the new container on port 5000
                    sh 'docker run -d -p 5000:5000 --name my-running-app my-python-app:latest'
                }
            }
        }
    }
    
    post {
        success {
            echo 'Deployment successful! Access your app at http://localhost:5000'
        }
        failure {
            echo 'Pipeline failed. Check the console output for errors.'
        }
    }
}
