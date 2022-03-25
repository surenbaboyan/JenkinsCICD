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
                    dockerImage = docker.build registry + ":$BUILD_NUMBER"
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
        stage('Deploy to Dev environment'){
            steps{
                sh 'docker run -p 9090:80 -d $registry:$BUILD_NUMBER'
            }
        }
        stage('Deploy to Prod'){
            steps{
                input 'Go to Prod'
            }
        }
        stage('Deploy to Prod environment'){
            agent { label 'prod' }           
            steps{
                sh 'docker run -p 9090:80 -d $registry:$BUILD_NUMBER'
            }
        }
    }
}