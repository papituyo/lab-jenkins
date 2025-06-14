pipeline {
    agent any
    stages {
        stage('Clonar repositorio') {
            steps {
                echo 'Clonando repositorio...'
            }
        }
        stage('Construir') {
            steps {
                echo 'Construyendo el proyecto...'
            }
        }
        stage('Pruebas') {
            steps {
                echo 'Ejecutando pruebas...'
            }
        }
        stage('Despliegue') {
            steps {
                echo 'Desplegando en entorno de pruebas...'
            }
        }
    }
}
