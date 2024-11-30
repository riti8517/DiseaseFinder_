package com.riti.web_backend.data.repository;

import com.riti.web_backend.data.entity.DiseaseDto;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Repository;

import java.sql.*;

@Repository
public class JdbcDiseaseRepository implements DiseaseRepository {
    @Autowired
    private JdbcTemplate jdbcTemplate;
    private final String SQL_FIND_DISEASE = "select * from symptoms where Disease";
    Connection connection;

    public JdbcDiseaseRepository() {
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            String url = "jdbc:mysql://localhost:3306/diseaseFinder";
            String user = "abstract-programmer";
            String password = "example-password";
            connection = DriverManager.getConnection(url, user, password);
        } catch (Exception e) {
            System.out.println(e);
        }
    }

    @Override
    public DiseaseDto getDescriptionByDisease(String diseaseName) {
        return null;
    }

//    public DiseaseDto getDescriptionByDisease(String diseaseName) {
//        return jdbcTemplate.queryForObject(SQL_FIND_DISEASE, new Object[]{diseaseName}, new DiseaseRowMapper());
//    }

//    public List<DiseaseDto> getAllSymptoms() {
//        return jdbcTemplate.query("select * from symptoms", new RowMapper<DiseaseDto>() {
//            @Override
//            public DiseaseDto mapRow(ResultSet rs, int rowNum) throws SQLException {
//                DiseaseDto diseaseDto = new DiseaseDto();
//                diseaseDto.setDiseaseName(rs.getString("Disease"));
//                diseaseDto.setSymptom_1(rs.getInt("Symptom_1"));
//                diseaseDto.setSymptom_2(rs.getInt("Symptom_2"));
//                diseaseDto.setSymptom_3(rs.getInt("Symptom_3"));
//                diseaseDto.setSymptom_4(rs.getInt("Symptom_4"));
//                diseaseDto.setSymptom_5(rs.getInt("Symptom_5"));
//                diseaseDto.setSymptom_6(rs.getInt("Symptom_6"));
//                diseaseDto.setSymptom_7(rs.getInt("Symptom_7"));
//                diseaseDto.setSymptom_8(rs.getInt("Symptom_8"));
//                diseaseDto.setSymptom_9(rs.getInt("Symptom_9"));
//                diseaseDto.setSymptom_10(rs.getInt("Symptom_10"));
//                diseaseDto.setSymptom_11(rs.getInt("Symptom_11"));
//                diseaseDto.setSymptom_12(rs.getInt("Symptom_12"));
//                diseaseDto.setSymptom_13(rs.getInt("Symptom_13"));
//                diseaseDto.setSymptom_14(rs.getInt("Symptom_14"));
//                diseaseDto.setSymptom_15(rs.getInt("Symptom_15"));
//                diseaseDto.setSymptom_16(rs.getInt("Symptom_16"));
//                diseaseDto.setSymptom_17(rs.getInt("Symptom_17"));
//                return diseaseDto;
//            }
//        });

   // }
}

