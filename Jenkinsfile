pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git url: '',
                    branch: 'main'
            }
        }

        stage('Run Script') {
            steps {
                sh 'chmod +x script.sh'
                sh './script.sh'
            }
        }
    }
}


pipeline {
    agent any

     stages {

        stage('Clone') {
            steps {
                git url: 'https://github.com/Prahas0728/jenkins-simple-demo.git',
                    branch: 'main'
            }
        }

        stage('Run Python Script') {
            steps {
                sh 'python3 --version'
                sh 'python3 python.py'
            }
        }

    }
}
