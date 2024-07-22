package com.riti.symptomFinder.service;
import com.riti.symptomFinder.data.entity.DiseaseDto;
import com.riti.symptomFinder.data.repository.JdbcDiseaseRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.Optional;

@Service
public class DiseaseService {
    @Autowired
    private JdbcDiseaseRepository diseaseRepository;

    public DiseaseService(JdbcDiseaseRepository diseaseRepository) {
        this.diseaseRepository = diseaseRepository;
    }
    public DiseaseDto getDiseaseDetails(String diseaseName){
        return diseaseRepository.getDescriptionByDisease(diseaseName);
    }

//    public UserRequestDto getDiseaseDtoById(String id) {
//    }
}