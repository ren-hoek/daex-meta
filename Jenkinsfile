node {
    stage('Cloning Git') {
        git credentialsId: 'gitlab', url: 'http://gitlab/gavin/daex-meta.git'
    }

    stage('Build Redis Stack') {
        dir('stacks/redis') {
            redis = docker.image("redis").pull()
            sh 'docker tag redis docker.service:5000/redis'
            docker.build('docker.service:5000/daex-meta/rqdash')
        }
    }
    
    stage('Build Portainer Stack') {
        dir('stacks/portainer') {
            portainer = docker.image("portainer/portainer").pull()
            sh 'docker tag portainer/portainer docker.service:5000/portainer/portainer'
            agent = docker.image("portainer/agent").pull()
            sh 'docker tag portainer/agent docker.service:5000/portainer/agent'
        }
    }
    
    stage('Build Mongo Stack') {
        dir('stacks/portainer') {
            mongo = docker.image("mongo").pull()
            sh 'docker tag mongo docker.service:5000/mongo'
            express = docker.image("mongo-express").pull()
            sh 'docker tag mongo-express docker.service:5000/mongo-express'
        }
    }

    stage('Build Daex: dedgbase') {
        dir('stacks/daex/dedgbase') {
             docker.build('docker.service:5000/daex-meta/dedgbase')
       }
    }

    stage('Build Daex: jupyterhub') {
        dir('stacks/daex/jupyterhub') {
             docker.build('docker.service:5000/daex-meta/jupyterhub')
       }
    }

    stage('Build Daex: rbase') {
        dir('stacks/daex/rbase') {
             docker.build('docker.service:5000/daex-meta/rbase')
       }
    }
    
    stage('Build Daex: rstudio') {
        dir('stacks/daex/rstudio') {
             docker.build('docker.service:5000/daex-meta/rstudio')
       }
    }

    stage('Build Daex: shiny') {
        dir('stacks/daex/shiny') {
             docker.build('docker.service:5000/daex-meta/shiny')
       }
    }

    stage('Push Images to Registry') {
	docker.image('docker.service:5000/redis').push()
        docker.image('docker.service:5000/portainer/portainer').push()
        docker.image('docker.service:5000/portainer/agent').push()
        docker.image('docker.service:5000/mongo').push() 
        docker.image('docker.service:5000/mongo-express').push() 
        docker.image('docker.service:5000/daex-meta/rqdash').push()
        docker.image('docker.service:5000/daex-meta/dedgbase').push()
        docker.image('docker.service:5000/daex-meta/jupyterhub').push()
        docker.image('docker.service:5000/daex-meta/rbase').push()
        docker.image('docker.service:5000/daex-meta/rstudio').push()
        docker.image('docker.service:5000/daex-meta/shiny').push()
    }   

    stage('Deploy daex-meta') {
        
        dir('stacks/redis') {
            sh 'docker stack deploy -c docker-compose.yml redis'
        }
        
        dir('stacks/portainer') {
            sh 'docker stack deploy -c docker-compose.yml portainer'
        }
        
        dir('stacks/mongo') {
            sh 'docker stack deploy -c docker-compose.yml mongo'
        }
        
        dir('stacks/daex') {
            sh 'docker stack deploy -c docker-compose.yml daex'
        }

        dir('stacks/nginx/html') {
            sh '''
            docker run -v nginx_html:/data --name helper centos true 
            docker cp . helper:/data
            docker rm helper
            '''
        }

        dir('stacks/nginx/conf') {
            sh '''
            docker run -v nginx_conf:/data --name helper centos true 
            docker cp . helper:/data
            docker rm helper
            '''
        }

        dir('stacks/nginx') {
            sh 'docker service update --force nginx_nginx'
        }        
    }
}
