package com.riti.web_backend.data.repository;

import com.riti.web_backend.data.entity.DiseaseDto;

import java.util.List;
import java.util.Optional;

public interface DiseaseRepository {
   //DiseaseDto getDescriptionByDisease(String diseaseName);
  List<DiseaseDto> getAllSymptoms();

}
