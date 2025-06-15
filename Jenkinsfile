pipeline {
    agent any

    stages {
        stage('Clonar repositorio') {
            steps {
                echo 'Clonando repositorio...'
                checkout scm
            }
        }

        stage('Verificar cambios') {
            steps {
                bat 'git fetch'
                script {
                    def cambios = bat(script: "git diff --name-only origin/main", returnStdout: true).trim()
                    if (cambios) {
                        echo "⚠ Se detectaron cambios respecto a origin/main:"
                        echo cambios
                    } else {
                        echo "✅ No hay cambios respecto a origin/main."
                    }
                }
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
