package com.riti.web_backend.service;

import jakarta.annotation.PostConstruct;
import org.springframework.stereotype.Service;

import java.util.*;

@Service
public class CacheManager {
    private List<String> symptoms;
    private Map<Double, String> diseaseMap;

    public List<String> getSymptoms(){
        return symptoms;
    }

    public Map<Double, String> getDiseases(){
        return diseaseMap;
    }

    @PostConstruct
    public void initCacheSymptoms() {
            symptoms = new ArrayList<>();
            symptoms.add("red_sore_around_nose");
            symptoms.add("fatigue");
            symptoms.add("skin_peeling");
            symptoms.add("chills");
            symptoms.add("itching");
            symptoms.add("visual_disturbances");
            symptoms.add("dehydration");
            symptoms.add("phlegm");
            symptoms.add("vomiting");
            symptoms.add("constipation");
            symptoms.add("swelling_joints");
            symptoms.add("family_history");
            symptoms.add("dizziness");
            symptoms.add("blackheads");
            symptoms.add("pain_during_bowel_movements");
            symptoms.add("lack_of_concentration");
            symptoms.add("slurred_speech");
            symptoms.add("skin_rash");
            symptoms.add("palpitations");
            symptoms.add("bruising");
            symptoms.add("coma");
            symptoms.add("toxic_look_(typhos)");
            symptoms.add("hip_joint_pain");
            symptoms.add("mood_swings");
            symptoms.add("drying_and_tingling_lips");
            symptoms.add("mucoid_sputum");
            symptoms.add("small_dents_in_nails");
            symptoms.add("weight_gain");
            symptoms.add("fast_heart_rate");
            symptoms.add("stomach_pain");
            symptoms.add("irregular_sugar_level");
            symptoms.add("muscle_pain");
            symptoms.add("enlarged_thyroid");
            symptoms.add("runny_nose");
            symptoms.add("weight_loss");
            symptoms.add("loss_of_smell");
            symptoms.add("swelling_of_stomach");
            symptoms.add("movement_stiffness");
            symptoms.add("high_fever");
            symptoms.add("swelled_lymph_nodes");
            symptoms.add("yellowish_skin");
            symptoms.add("excessive_hunger");
            symptoms.add("continuous_feel_of_urine");
            symptoms.add("silver_like_dusting");
            symptoms.add("internal_itching");
            symptoms.add("increased_appetite");
            symptoms.add("bloody_stool");
            symptoms.add("swollen_extremeties");
            symptoms.add("yellowing_of_eyes");
            symptoms.add("sinus_pressure");
            symptoms.add("distention_of_abdomen");
            symptoms.add("nodal_skin_eruptions");
            symptoms.add("ulcers_on_tongue");
            symptoms.add("throat_irritation");
            symptoms.add("blood_in_sputum");
            symptoms.add("redness_of_eyes");
            symptoms.add("breathlessness");
            symptoms.add("receiving_blood_transfusion");
            symptoms.add("red_spots_over_body");
            symptoms.add("congestion");
            symptoms.add("irritation_in_anus");
            symptoms.add("cramps");
            symptoms.add("sunken_eyes");
            symptoms.add("malaise");
            symptoms.add("swollen_blood_vessels");
            symptoms.add("abdominal_pain");
            symptoms.add("chest_pain");
            symptoms.add("muscle_weakness");
            symptoms.add("cough");
            symptoms.add("loss_of_appetite");
            symptoms.add("prominent_veins_on_calf");
            symptoms.add("swollen_legs");
            symptoms.add("unsteadiness");
            symptoms.add("spinning_movements");
            symptoms.add("continuous_sneezing");
            symptoms.add("obesity");
            symptoms.add("rusty_sputum");
            symptoms.add("burning_micturition");
            symptoms.add("irritability");
            symptoms.add("blurred_and_distorted_vision");
            symptoms.add("loss_of_balance");
            symptoms.add("puffy_face_and_eyes");
            symptoms.add("restlessness");
            symptoms.add("knee_pain");
            symptoms.add("nausea");
            symptoms.add("anxiety");
            symptoms.add("mild_fever");
            symptoms.add("brittle_nails");
            symptoms.add("watering_from_eyes");
            symptoms.add("muscle_wasting");
            symptoms.add("belly_pain");
            symptoms.add("receiving_unsterile_injections");
            symptoms.add("lethargy");
            symptoms.add("back_pain");
            symptoms.add("polyuria");
            symptoms.add("fluid_overload");
            symptoms.add("stiff_neck");
            symptoms.add("blister");
            symptoms.add("passage_of_gases");
            symptoms.add("indigestion");
            symptoms.add("cold_hands_and_feets");
            symptoms.add("pain_in_anal_region");
            symptoms.add("painful_walking");
            symptoms.add("patches_in_throat");
            symptoms.add("diarrhoea");
            symptoms.add("stomach_bleeding");
            symptoms.add("scurring");
            symptoms.add("bladder_discomfort");
            symptoms.add("inflammatory_nails");
            symptoms.add("spotting_urination");
            symptoms.add("weakness_in_limbs");
            symptoms.add("joint_pain");
            symptoms.add("shivering");
            symptoms.add("altered_sensorium");
            symptoms.add("extra_marital_contacts");
            symptoms.add("pus_filled_pimples");
            symptoms.add("history_of_alcohol_consumption");
            symptoms.add("yellow_urine");
            symptoms.add("acidity");
            symptoms.add("abnormal_menstruation");
            symptoms.add("foul_smell_of_urine");
            symptoms.add("acute_liver_failure");
            symptoms.add("dischromic_patches");
            symptoms.add("neck_pain");
            symptoms.add("pain_behind_the_eyes");
            symptoms.add("headache");
            symptoms.add("depression");
            symptoms.add("weakness_of_one_body_side");
            symptoms.add("dark_urine");
            symptoms.add("sweating");
            symptoms.add("yellow_crust_ooze");
        }
        @PostConstruct
        public void initDisease(){
            diseaseMap = new HashMap<Double, String>();
            diseaseMap.put(0.0,"Fungal infection");
            diseaseMap.put(1.0,"Allergy");
            diseaseMap.put(2.0,"GERD");
            diseaseMap.put(3.0,"Chronic cholestasis");
            diseaseMap.put(4.0,"Drug Reaction");
            diseaseMap.put(5.0,"Peptic ulcer diseae");
            diseaseMap.put(6.0,"AIDS");
            diseaseMap.put(7.0,"Diabetes");
            diseaseMap.put(8.0,"Gastroenteritis");
            diseaseMap.put(9.0,"Bronchial Asthma");
            diseaseMap.put(10.0,"Hypertension");
            diseaseMap.put(11.0,"Migraine");
            diseaseMap.put(12.0,"Cervical spondylosis");
            diseaseMap.put(13.0,"Paralysis (brain hemorrhage)");
            diseaseMap.put(14.0,"Jaundice");
            diseaseMap.put(15.0,"Malaria");
            diseaseMap.put(16.0,"Chicken pox");
            diseaseMap.put(17.0,"Dengue");
            diseaseMap.put(18.0,"Typhoid");
            diseaseMap.put(19.0,"hepatitis A");
            diseaseMap.put(20.0,"Hepatitis B");
            diseaseMap.put(21.0,"Hepatitis C");
            diseaseMap.put(22.0,"Hepatitis D");
            diseaseMap.put(23.0,"Hepatitis E");
            diseaseMap.put(24.0,"Alcoholic hepatitis");
            diseaseMap.put(25.0,"Tuberculosis");
            diseaseMap.put(26.0,"Common Cold");
            diseaseMap.put(27.0,"Pneumonia");
            diseaseMap.put(28.0,"Dimorphic hemmorhoids(piles)");
            diseaseMap.put(29.0,"Heart attack");
            diseaseMap.put(30.0,"Varicose veins");
            diseaseMap.put(31.0,"Hypothyroidism");
            diseaseMap.put(32.0,"Hyperthyroidism");
            diseaseMap.put(33.0,"Hypoglycemia");
            diseaseMap.put(34.0,"Osteoarthristis");
            diseaseMap.put(35.0,"Arthritis");
            diseaseMap.put(36.0,"(vertigo) Paroymsal  Positional Vertigo");
            diseaseMap.put(37.0,"Acne");
            diseaseMap.put(38.0,"Urinary tract infection");
            diseaseMap.put(39.0,"Psoriasis");
            diseaseMap.put(40.0,"Impetigo");
        }

    }

//    public Map<Double, String> getDiseaseMap() {
//
//    }
//    public String getDiseaseName(double id){
//        Map<Double, String> diseaseMap = getDiseaseMap();
//        return diseaseMap.getOrDefault(id, "Unknown Disease");
//    }


