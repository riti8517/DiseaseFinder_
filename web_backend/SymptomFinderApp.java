package com.riti.symptomFinder;

import com.riti.symptomFinder.data.repository.JdbcDiseaseRepository;
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
