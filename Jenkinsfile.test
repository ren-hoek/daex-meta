node {

    stage('Cloning Git') {
        git url: 'http://gitlab/daex/daex-meta.git'
    }
    stage('Build Redis Stack') {
        dir('stacks/redis') {
            sh 'ls'
        }
    }
}
