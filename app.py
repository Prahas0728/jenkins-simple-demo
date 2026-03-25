pipeline {
    agent any
    
    environment {
        DOCKER_HUB_USER = 'prahas01' 
        REPO_NAME = 'jenkins-simple-demo'
        IMAGE_TAG = "${DOCKER_HUB_USER}/${REPO_NAME}:latest"
    }

    stages {
        stage('Clone') {
            steps {
                git url: 'https://github.com/Prahas0728/jenkins-simple-demo.git', branch: 'main'
            }
        }

        stage('Check Files') {
            steps {
                sh 'chmod +x script.sh'
                sh './script.sh'
                sh 'python3 python.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                // Uses the tag that worked in your terminal
                sh "docker build -t ${IMAGE_TAG} ."
            }
        }

        stage('Push to Docker Hub') {
            steps {
                // IMPORTANT: Ensure 'docker-hub-creds' ID exists in Jenkins
                // and contains your NEW Access Token as the password
                withCredentials([usernamePassword(credentialsId: 'docker-hub-creds', 
                                 usernameVariable: 'USER', 
                                 passwordVariable: 'PASS')]) {
                    sh "echo ${PASS} | docker login -u ${USER} --password-stdin"
                    sh "docker push ${IMAGE_TAG}"
                }
            }
        }

        stage('Deploy Local Container') {
            steps {
                // This runs the app on your Jenkins machine so you can see it
                sh "docker stop my-running-app || true"
                sh "docker rm my-running-app || true"
                sh "docker run -d -p 5000:5000 --name my-running-app ${IMAGE_TAG}"
            }
        }
    }
}
