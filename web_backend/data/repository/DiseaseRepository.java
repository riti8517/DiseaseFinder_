package com.riti.web_backend.data.repository;

import com.riti.web_backend.data.entity.DiseaseDto;

public interface DiseaseRepository {
   DiseaseDto getDescriptionByDisease(String diseaseName);
}
