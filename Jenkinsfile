pipeline{
    agent { label 'docker' }

    environment{
        imageName = "webpytest"
        dockerHub = "42b681e3-a3cc-4816-9f2a-1cfe57921f48"
    }
    
    stages{
        stage('Checkout code from git'){
            steps{
                git 'https://github.com/surenbaboyan/JenkinsCICD.git'
            }
        }
    }
    stages{
        stage('Build docker image'){
            steps{
                script{
                    dockerImage = docker.build imageName
                }

            }
        }
    }
    stages{
        stage('Push imge to dockerHub'){
            steps{
                script{
                    docker.withRegistry(registry,dockerHub){
                        dockerImage.push("$BUILD_NUMBER")
                        dockerImage.push("latest")
                    }
                }

            }
        }
    }
}