pipeline{
    agent { label 'docker' }

    environment{
        dockerHub = "42b681e3-a3cc-4816-9f2a-1cfe57921f48"
        registry  = "surenbaboyan/webpytest"
    }
    
    stages{
        stage('Checkout code from git'){
            steps{
                git 'https://github.com/surenbaboyan/JenkinsCICD.git'
            }
        }
        stage('Build docker image'){
            steps{
                script{
                    dockerImage = docker.build registry + ":$BUILD_NUMER"
                }

            }
        }
        stage('Push imge to dockerHub'){
            steps{
                script{
                    docker.withRegistry('',dockerHub){
                        dockerImage.push()
                    }
                }

            }
        }
    }
}