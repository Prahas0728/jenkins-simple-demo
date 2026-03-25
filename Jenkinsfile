pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                // This URL must NOT be empty
                git url: 'https://github.com/Prahas0728/jenkins-simple-demo.git',
                    branch: 'main'
            }
        }

        stage('Run Script') {
            steps {
                // Note: This will fail if 'script.sh' is missing from your repo
                sh 'chmod +x script.sh'
                sh './script.sh'
            }
        }

        stage('Run Python Script') {
            steps {
                sh 'python3 --version'
                // Note: This will fail if 'python.py' is missing from your repo
                sh 'python3 python.py'
            }
        }
    }
}
