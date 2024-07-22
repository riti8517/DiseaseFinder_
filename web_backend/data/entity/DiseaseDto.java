package com.riti.symptomFinder.data.entity;

public class DiseaseDto {

    private String Disease;
    private String Description;
    private String Symptom_1;
    private String Symptom_2;
    private String Symptom_3;

    public DiseaseDto() {
    }

    public String getDescription() {
        return Description;
    }

    public void setDescription(String description) {
        Description = description;
    }

    public String getDiseaseName() {
        return Disease;
    }

    public void setDiseaseName(String Disease) {
        this.Disease = Disease;
    }

    public String getSymptom_1() {
        return Symptom_1;
    }

    public void setSymptom_1(String symptom_1) {
        Symptom_1 = symptom_1;
    }

    public String getSymptom_2() {
        return Symptom_2;
    }

    public void setSymptom_2(String symptom_2) {
        Symptom_2 = symptom_2;
    }

    public String getSymptom_3() {
        return Symptom_3;
    }

    public void setSymptom_3(String symptom_3) {
        Symptom_3 = symptom_3;
    }

    @Override
    public String toString() {
        return "Disease{" +
                "disease='" + Disease + '\'' +
                ", Symptom_1='" + Symptom_1 + '\'' +
                ", Symptom_2='" + Symptom_2 + '\'' +
                ", Symptom_3='" + Symptom_3 + '\'' +
                '}';
    }
}
