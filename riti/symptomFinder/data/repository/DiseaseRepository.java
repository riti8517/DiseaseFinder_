package com.riti.symptomFinder.data.repository;

import com.riti.symptomFinder.data.entity.DiseaseDto;

import java.util.Optional;

public interface DiseaseRepository {
   DiseaseDto getDescriptionByDisease(String diseaseName);

}
