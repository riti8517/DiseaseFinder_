package com.riti.web_backend;

import com.riti.web_backend.data.repository.JdbcDiseaseRepository;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class SymptomFinderApp {

	//@Autowired
	JdbcDiseaseRepository diseaseRepository;

	public static void main(String[] args) {

		SpringApplication.run(SymptomFinderApp.class, args);
	}

}
