package com.riti.web_backend.data.transformer.mapper;

import com.riti.web_backend.data.entity.DiseaseDto;

import org.springframework.jdbc.core.RowMapper;
import java.sql.ResultSet;
import java.sql.SQLException;

public class DiseaseRowMapper implements RowMapper<DiseaseDto> {
    public DiseaseDto mapRow(ResultSet rs, int rowNum) throws SQLException{
        DiseaseDto diseaseDto = new DiseaseDto();
        diseaseDto.setDiseaseName(rs.getString("DISEASE"));
//        diseaseDto.setDescription(rs.getInt("Description"));
        diseaseDto.setSymptom_1(rs.getInt("Symptom_1"));
        diseaseDto.setSymptom_2(rs.getInt("Symptom_2"));
        diseaseDto.setSymptom_3(rs.getInt("Symptom_3"));
        diseaseDto.setSymptom_4(rs.getInt("Symptom_4"));
        diseaseDto.setSymptom_5(rs.getInt("Symptom_5"));
        diseaseDto.setSymptom_6(rs.getInt("Symptom_6"));
        diseaseDto.setSymptom_7(rs.getInt("Symptom_7"));
        diseaseDto.setSymptom_8(rs.getInt("Symptom_8"));
        diseaseDto.setSymptom_9(rs.getInt("Symptom_9"));
        diseaseDto.setSymptom_10(rs.getInt("Symptom_10"));
        diseaseDto.setSymptom_11(rs.getInt("Symptom_11"));
        diseaseDto.setSymptom_12(rs.getInt("Symptom_12"));
        diseaseDto.setSymptom_13(rs.getInt("Symptom_13"));
        diseaseDto.setSymptom_14(rs.getInt("Symptom_14"));
        diseaseDto.setSymptom_15(rs.getInt("Symptom_15"));
        diseaseDto.setSymptom_16(rs.getInt("Symptom_16"));
        diseaseDto.setSymptom_17(rs.getInt("Symptom_17"));

        return diseaseDto;
    }
}
