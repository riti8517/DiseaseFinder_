package com.riti.web_backend.service;
import com.riti.web_backend.data.entity.DiseaseDto;
import com.riti.web_backend.data.repository.JdbcDiseaseRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@Service
public class DiseaseService {
    @Autowired
    private JdbcDiseaseRepository diseaseRepository;

    @Autowired
    private com.riti.web_backend.service.CacheManager cacheManager;


    public DiseaseDto getDiseaseDetails(String diseaseName){
        return diseaseRepository.getDescriptionByDisease(diseaseName);
     //   return diseaseRepository.getAllSymptoms();
    }

    public List<String> getAllSymptoms(){
        List<String> symptoms = cacheManager.getSymptoms();
        List<String> updatedSymptoms = new ArrayList<>();
        for (String symptom : symptoms) {
            updatedSymptoms.add(symptom.replace("_", " "));
        }
        return updatedSymptoms;
    }
    public String getDiseaseName(double id) {
        return cacheManager.getDiseases().get(id);
    }
}