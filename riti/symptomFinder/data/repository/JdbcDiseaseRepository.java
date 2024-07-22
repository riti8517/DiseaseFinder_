package com.riti.symptomFinder.data.repository;

import com.riti.symptomFinder.data.entity.DiseaseDto;
import com.riti.symptomFinder.data.transformer.mapper.DiseaseRowMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Repository;

import java.sql.*;
import java.util.Optional;

@Repository
public class JdbcDiseaseRepository implements DiseaseRepository  {
    @Autowired
    private JdbcTemplate jdbcTemplate;
    private final String SQL_FIND_DISEASE = "select * from symptom_description where Disease = ?";
    Connection connection;

    public JdbcDiseaseRepository() {
        System.out.println("helloooo");
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            String url = "jdbc:mysql://localhost:3306/diseases";
            String user = "root";
            String password = "riti2006";
            connection = DriverManager.getConnection(url, user, password);
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
    public DiseaseDto getDescriptionByDisease(String diseaseName){
        return jdbcTemplate.queryForObject(SQL_FIND_DISEASE, new Object[] { diseaseName }, new DiseaseRowMapper());
    }
}

