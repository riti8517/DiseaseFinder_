package com.riti.web_backend.data.entity;

public class DiseaseDto extends SymptomDto{

    private String Disease;
    public DiseaseDto() {
    }

    public String getDiseaseName() {
        return Disease;
    }

    public void setDiseaseName(String Disease) {
        this.Disease = Disease;
    }

    public String getDisease() {
        return Disease;
    }

    public void setDisease(String disease) {
        Disease = disease;
    }

    @Override
    public String toString() {
        return "Disease{" +
                "disease='" + Disease + '\'' +
                '}';
    }
}
