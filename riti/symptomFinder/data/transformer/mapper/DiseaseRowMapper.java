package com.riti.symptomFinder.data.transformer.mapper;

import com.riti.symptomFinder.data.entity.DiseaseDto;

import org.springframework.jdbc.core.RowMapper;
import java.sql.ResultSet;
import java.sql.SQLException;

public class DiseaseRowMapper implements RowMapper<DiseaseDto> {
    public DiseaseDto mapRow(ResultSet rs, int rowNum) throws SQLException{
        DiseaseDto diseaseDto = new DiseaseDto();
        diseaseDto.setDiseaseName(rs.getString("DISEASE"));
        diseaseDto.setDescription(rs.getString("Description"));
//        diseaseDto.setSymptom_1(rs.getString("SYMPTOM_1"));
//        diseaseDto.setSymptom_2(rs.getString("SYMPTOM_2"));
//        diseaseDto.setSymptom_3(rs.getString("SYMPTOM_3"));
        return diseaseDto;
    }
}
