package com.riti.symptomFinder.api.controller;

import com.riti.symptomFinder.data.entity.DiseaseDto;
import com.riti.symptomFinder.service.DiseaseService;
import org.springframework.web.bind.annotation.*;

import java.util.Optional;

@RestController
@RequestMapping("/disease")
public class SearchController {

    private DiseaseService service;

    public SearchController(DiseaseService service){
        this.service= service;
    }

    @GetMapping("/{Disease}")
    public DiseaseDto search(@PathVariable(name = "Disease") String diseaseName){
        return service.getDiseaseDetails(diseaseName);

    }
}
