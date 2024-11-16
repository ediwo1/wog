
pipeline {
    agent {label 'linux'}
    stages {
        stage('Checkout') {
            steps {
                sh """
                    # [ -d wog ] && rm -rf wog
                    git clone https://github.com/ediwo1/wog.git
                    cd wog && git checkout wog-level4
                """
            }
        }

        stage('Build docker image') {
            steps{
                echo "Building docker image..."
                sh """
                    cd wog/website
                    docker compose build
                """
            }
        }

        stage('Run Flask App') {
            steps{
                sh """
                    cd wog/website
                    docker compose up -d
                    sleep 10s
                """
            }
        }

        stage('Run Test') {
            steps{
                sh """
                    cd wog/tests
                    python3 e2e.py
                """
            }
        }

        stage('Push docker image to repository') {
            steps{

                withCredentials([usernamePassword(credentialsId: 'docker-hub-login', passwordVariable: 'PASSWORD', usernameVariable: 'USERNAME')]) {
                    sh """
                        docker login -u $USERNAME -p $PASSWORD
                        cd wog/website
                        docker compose push
                    """
                }
            }
        }
    }
    post {
        always {
            sh """
                cd wog/website
                docker compose down
            """
            cleanWs()
        }
    }
}