package com.riti.web_backend.data.transformer.mapper;

import com.riti.web_backend.data.entity.DiseaseDto;

import org.springframework.jdbc.core.RowMapper;
import java.sql.ResultSet;
import java.sql.SQLException;

public class DiseaseRowMapper implements RowMapper<DiseaseDto> {
    public DiseaseDto mapRow(ResultSet rs, int rowNum) throws SQLException{
        DiseaseDto diseaseDto = new DiseaseDto();
        diseaseDto.setDiseaseName(rs.getString("DISEASE"));
//        diseaseDto.setDescription(rs.getString("Description"));
        diseaseDto.setSymptom_1(rs.getString("Symptom_1"));
        diseaseDto.setSymptom_2(rs.getString("Symptom_2"));
        diseaseDto.setSymptom_3(rs.getString("Symptom_3"));
        diseaseDto.setSymptom_4(rs.getString("Symptom_4"));
        diseaseDto.setSymptom_5(rs.getString("Symptom_5"));
        diseaseDto.setSymptom_6(rs.getString("Symptom_6"));
        diseaseDto.setSymptom_7(rs.getString("Symptom_7"));
        diseaseDto.setSymptom_8(rs.getString("Symptom_8"));
        diseaseDto.setSymptom_9(rs.getString("Symptom_9"));
        diseaseDto.setSymptom_10(rs.getString("Symptom_10"));
        diseaseDto.setSymptom_11(rs.getString("Symptom_11"));
        diseaseDto.setSymptom_12(rs.getString("Symptom_12"));
        diseaseDto.setSymptom_13(rs.getString("Symptom_13"));
        diseaseDto.setSymptom_14(rs.getString("Symptom_14"));
        diseaseDto.setSymptom_15(rs.getString("Symptom_15"));
        diseaseDto.setSymptom_16(rs.getString("Symptom_16"));
        diseaseDto.setSymptom_17(rs.getString("Symptom_17"));

        return diseaseDto;
    }
}
