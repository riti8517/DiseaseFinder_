package com.riti.web_backend.api.controller;

import com.riti.web_backend.data.entity.DiseaseDto;
import com.riti.web_backend.response.ResponseHandler;
import com.riti.web_backend.service.DiseaseService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.*;

import java.util.Optional;

@RestController
@RequestMapping("/")
public class SearchController {

    @Autowired
    DiseaseService service;

    @GetMapping("/{Disease}")
    public ResponseEntity<Object> search(@PathVariable(name = "Disease") String diseaseName){
        return ResponseHandler.responseBuilder("Request", HttpStatus.OK, service.getDiseaseDetails(diseaseName));

    }
}
