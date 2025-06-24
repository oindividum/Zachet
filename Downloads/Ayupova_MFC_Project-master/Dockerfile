# Используем официальный образ с JDK 17
FROM eclipse-temurin:17-jdk

# Создаём рабочую директорию в контейнере
WORKDIR /app

# Копируем всё из текущей директории проекта
COPY . .

# Собираем проект через встроенный Maven Wrapper
RUN ./mvnw clean package -DskipTests

# Открываем порт 8080 (Spring Boot)
EXPOSE 8080

# Указываем, как запускать приложение
CMD ["java", "-jar", "target/popitka2-0.0.1-SNAPSHOT.jar"]
