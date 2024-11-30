package com.riti.web_backend.api.controller;

import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import com.riti.web_backend.response.ResponseHandler;
import com.riti.web_backend.service.DiseaseService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

@RestController
@RequestMapping("/")
public class SearchController {

    @Autowired
    DiseaseService service;

    @GetMapping("/")
    public ResponseEntity<Object> getHello(){
        return ResponseHandler.responseBuilder("Request", HttpStatus.OK, "hello from Titi");
    }

    @GetMapping("/{Disease}")
    public ResponseEntity<Object> getDiseaseDescription(@PathVariable(name = "Disease") String diseaseName){
        return ResponseHandler.responseBuilder("Request", HttpStatus.OK, service.getDiseaseDetails(diseaseName));

    }

    @GetMapping("/predictDisease")
    @ResponseBody
    public ResponseEntity<Object> predictDisease(@RequestParam("symptoms") List<String> sympList) throws URISyntaxException, IOException, InterruptedException {

        ArrayList<String> binaryList = new ArrayList<>(Collections.nCopies(service.getAllSymptoms().size(), "0"));
        for (String symptom : sympList) {
            if (service.getAllSymptoms().contains(symptom)) {
                int index = service.getAllSymptoms().indexOf(symptom);
                binaryList.set(index, "1");
            }
        }

        String stringSymptoms = String.join(",", binaryList);
        HttpRequest getRequest = HttpRequest.newBuilder()
                .uri(new URI("http://127.0.0.1:8000/predict?data=" + stringSymptoms))
                .GET()
                .build();

        HttpClient httpClient = HttpClient.newHttpClient();
        HttpResponse<String> getResponse = httpClient.send(getRequest, HttpResponse.BodyHandlers.ofString());
        String responseBody = getResponse.body();
        if (responseBody.startsWith("{")) {
            JsonElement jsonElement = JsonParser.parseString(responseBody);
            JsonArray predictionArray = jsonElement.getAsJsonObject().getAsJsonArray("prediction");
            double id = predictionArray.get(0).getAsDouble();
            String diseaseName = service.getDiseaseName(id);
            return ResponseHandler.responseBuilder("Disease Prediction", HttpStatus.OK, diseaseName);
        } else {
            return ResponseHandler.responseBuilder("Disease Prediction", HttpStatus.OK, responseBody);
        }
    }
//    @GetMapping("/predictDisease")
//    @ResponseBody
//    public String predictDisease(@RequestParam("symptoms") List<String> sympList) throws URISyntaxException, IOException, InterruptedException {
//
//        ArrayList<String> binaryList = new ArrayList<>(Collections.nCopies(service.getAllSymptoms().size(), "0"));
//        for (String symptom : sympList) {
//            if (service.getAllSymptoms().contains(symptom)) {
//                int index = service.getAllSymptoms().indexOf(symptom);
//                binaryList.set(index, "1");
//            }
//        }
//
//        String stringSymptoms = String.join(",", binaryList);
//        HttpRequest getRequest = HttpRequest.newBuilder()
//				.uri(new URI("http://127.0.0.1:8000/predict?data="+stringSymptoms))
//				.GET() // Sending the values string as request body
//				.build();
//		HttpClient httpClient = HttpClient.newHttpClient();
//		HttpResponse<String> getResponse = httpClient.send((java.net.http.HttpRequest) getRequest, HttpResponse.BodyHandlers.ofString());
//		System.out.println("Response Body: " + getResponse.body());
//		System.out.println("Response Code: " + getResponse.statusCode());
//		JsonElement jsonElement = JsonParser.parseString(getResponse.body());
//		JsonArray predictionArray = jsonElement.getAsJsonObject().getAsJsonArray("prediction");
//		double id = predictionArray.get(0).getAsDouble();
//        return service.getDiseaseName(id);
//    }
    @GetMapping("/symptoms")
    @ResponseBody
    public ResponseEntity<String> getAllSymptoms() {
        List<String> symptoms = service.getAllSymptoms();
        JsonArray jsonArray = new JsonArray();
        for (String symptom : symptoms) {
            JsonObject jsonObject = new JsonObject();
            jsonObject.addProperty("symptom", symptom);
            jsonArray.add(jsonObject);
        }

        return new ResponseEntity<>(jsonArray.toString(), HttpStatus.OK);
    }
//    @GetMapping("/symptoms")
//    @ResponseBody
//    public ResponseEntity<List<String>> getAllSymptoms() {
//        List<String> symptoms = service.getAllSymptoms();
//        return new ResponseEntity<>(symptoms, HttpStatus.OK);
//    }
}
