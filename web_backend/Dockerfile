# Use an official OpenJDK runtime as a parent image
FROM openjdk:17-alpine

# set shell to bash
# source: https://stackoverflow.com/a/40944512/3128926
RUN apk update && apk add bash

# Set the working directory to /app
WORKDIR /app

# Copy the fat jar into the container at /app
COPY ../target/docker-java-app-symptomfinder.jar /app

# Make port 8080 available to the world outside this container
EXPOSE 8083

# Run jar file when the container launches
CMD ["java", "-jar", "docker-java-app-symptomfinder.jar"]
