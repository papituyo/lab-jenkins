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
                script {
                    def cambios = sh(script: "git diff --name-only $GIT_PREVIOUS_COMMIT $GIT_COMMIT", returnStdout: true).trim()
                    if (cambios) {
                        echo "⚠ Se detectaron cambios en los siguientes archivos:"
                        echo cambios
                    } else {
                        echo "✅ No hay cambios desde la última ejecución."
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
