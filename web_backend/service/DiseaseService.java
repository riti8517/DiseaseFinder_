package com.riti.web_backend.service;
import com.riti.web_backend.data.entity.DiseaseDto;
import com.riti.web_backend.data.repository.JdbcDiseaseRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class DiseaseService {
    @Autowired
    private JdbcDiseaseRepository diseaseRepository;

    public DiseaseService(JdbcDiseaseRepository diseaseRepository) {
        this.diseaseRepository = diseaseRepository;
    }
    public List<DiseaseDto> getDiseaseDetails(String diseaseName){
       // return diseaseRepository.getDescriptionByDisease(diseaseName);
        return diseaseRepository.getAllSymptoms();
    }

//    public UserRequestDto getDiseaseDtoById(String id) {
//    }
}