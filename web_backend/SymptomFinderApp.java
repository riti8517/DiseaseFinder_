package com.riti.web_backend;

import com.riti.web_backend.data.repository.JdbcDiseaseRepository;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import java.io.IOException;
import java.net.URISyntaxException;

@SpringBootApplication
public class SymptomFinderApp {

	//@Autowired
	JdbcDiseaseRepository diseaseRepository;


	public static void main(String[] args) throws URISyntaxException, IOException, InterruptedException {
//		SymptomDto symptomDto = new SymptomDto();
//		symptomDto.setSymptom_1(0);
//		symptomDto.setSymptom_2(0);
//		symptomDto.setSymptom_3(0);
//		symptomDto.setSymptom_4(0);
//		symptomDto.setSymptom_5(0);
//		symptomDto.setSymptom_6(0);
//		symptomDto.setSymptom_7(0);
//		symptomDto.setSymptom_8(0);
//		symptomDto.setSymptom_9(0);
//		symptomDto.setSymptom_10(0);
//		symptomDto.setSymptom_11(0);
//		symptomDto.setSymptom_12(0);
//		symptomDto.setSymptom_13(0);
//		symptomDto.setSymptom_14(0);
//		symptomDto.setSymptom_15(0);
//		symptomDto.setSymptom_16(0);
//		symptomDto.setSymptom_17(0);
//		symptomDto.setSymptom_18(0);
//		symptomDto.setSymptom_19(0);
//		symptomDto.setSymptom_20(0);
//		symptomDto.setSymptom_21(0);
//		symptomDto.setSymptom_22(0);
//		symptomDto.setSymptom_23(0);
//		symptomDto.setSymptom_24(0);
//		symptomDto.setSymptom_25(0);
//		symptomDto.setSymptom_26(0);
//		symptomDto.setSymptom_27(0);
//		symptomDto.setSymptom_28(0);
//		symptomDto.setSymptom_29(0);
//		symptomDto.setSymptom_30(0);
//		symptomDto.setSymptom_31(0);
//		symptomDto.setSymptom_32(0);
//		symptomDto.setSymptom_33(0);
//		symptomDto.setSymptom_34(0);
//		symptomDto.setSymptom_35(0);
//		symptomDto.setSymptom_36(0);
//		symptomDto.setSymptom_37(0);
//		symptomDto.setSymptom_38(0);
//		symptomDto.setSymptom_39(0);
//		symptomDto.setSymptom_40(0);
//		symptomDto.setSymptom_41(0);
//		symptomDto.setSymptom_42(0);
//		symptomDto.setSymptom_43(0);
//		symptomDto.setSymptom_44(0);
//		symptomDto.setSymptom_45(0);
//		symptomDto.setSymptom_46(0);
//		symptomDto.setSymptom_47(0);
//		symptomDto.setSymptom_48(0);
//		symptomDto.setSymptom_49(1);
//		symptomDto.setSymptom_50(1);
//		symptomDto.setSymptom_51(0);
//		symptomDto.setSymptom_52(0);
//		symptomDto.setSymptom_53(0);
//		symptomDto.setSymptom_54(1);
//		symptomDto.setSymptom_55(1);
//		symptomDto.setSymptom_56(0);
//		symptomDto.setSymptom_57(0);
//		symptomDto.setSymptom_58(0);
//		symptomDto.setSymptom_59(0);
//		symptomDto.setSymptom_60(0);
//		symptomDto.setSymptom_61(0);
//		symptomDto.setSymptom_62(0);
//		symptomDto.setSymptom_63(0);
//		symptomDto.setSymptom_64(0);
//		symptomDto.setSymptom_65(0);
//		symptomDto.setSymptom_66(0);
//		symptomDto.setSymptom_67(0);
//		symptomDto.setSymptom_68(0);
//		symptomDto.setSymptom_69(0);
//		symptomDto.setSymptom_70(0);
//		symptomDto.setSymptom_71(0);
//		symptomDto.setSymptom_72(0);
//		symptomDto.setSymptom_73(0);
//		symptomDto.setSymptom_74(0);
//		symptomDto.setSymptom_75(0);
//		symptomDto.setSymptom_76(0);
//		symptomDto.setSymptom_77(0);
//		symptomDto.setSymptom_78(0);
//		symptomDto.setSymptom_79(0);
//		symptomDto.setSymptom_80(0);
//		symptomDto.setSymptom_81(0);
//		symptomDto.setSymptom_82(0);
//		symptomDto.setSymptom_83(0);
//		symptomDto.setSymptom_84(0);
//		symptomDto.setSymptom_85(0);
//		symptomDto.setSymptom_86(0);
//		symptomDto.setSymptom_87(0);
//		symptomDto.setSymptom_88(0);
//		symptomDto.setSymptom_89(0);
//		symptomDto.setSymptom_90(0);
//		symptomDto.setSymptom_91(0);
//		symptomDto.setSymptom_92(0);
//		symptomDto.setSymptom_93(0);
//		symptomDto.setSymptom_94(0);
//		symptomDto.setSymptom_95(0);
//		symptomDto.setSymptom_96(0);
//		symptomDto.setSymptom_97(0);
//		symptomDto.setSymptom_98(0);
//		symptomDto.setSymptom_99(0);
//		symptomDto.setSymptom_100(0);
//		symptomDto.setSymptom_101(0);
//		symptomDto.setSymptom_102(0);
//		symptomDto.setSymptom_103(0);
//		symptomDto.setSymptom_104(0);
//		symptomDto.setSymptom_105(0);
//		symptomDto.setSymptom_106(0);
//		symptomDto.setSymptom_107(0);
//		symptomDto.setSymptom_108(0);
//		symptomDto.setSymptom_109(0);
//		symptomDto.setSymptom_110(0);
//		symptomDto.setSymptom_111(0);
//		symptomDto.setSymptom_112(0);
//		symptomDto.setSymptom_113(0);
//		symptomDto.setSymptom_114(0);
//		symptomDto.setSymptom_115(0);
//		symptomDto.setSymptom_116(0);
//		symptomDto.setSymptom_117(0);
//		symptomDto.setSymptom_118(0);
//		symptomDto.setSymptom_119(0);
//		symptomDto.setSymptom_120(0);
//		symptomDto.setSymptom_121(0);
//		symptomDto.setSymptom_122(0);
//		symptomDto.setSymptom_123(0);
//		symptomDto.setSymptom_124(0);
//		symptomDto.setSymptom_125(0);
//		symptomDto.setSymptom_126(0);
//		symptomDto.setSymptom_127(0);
//		symptomDto.setSymptom_128(0);
//		symptomDto.setSymptom_129(0);
//		symptomDto.setSymptom_130(0);
//		symptomDto.setSymptom_131(0);
//		System.out.println("Symptom Values: " + symptomDto);
//
//		HttpRequest getRequest = HttpRequest.newBuilder()
//				.uri(new URI("http://127.0.0.1:8080/predict?data="+symptomDto))
//				.GET() // Sending the values string as request body
//				.build();
//		HttpClient httpClient = HttpClient.newHttpClient();
//		HttpResponse<String> getResponse = httpClient.send(getRequest, HttpResponse.BodyHandlers.ofString());
//		System.out.println("Response Body: " + getResponse.body());
//		System.out.println("Response Code: " + getResponse.statusCode());
//		JsonElement jsonElement = JsonParser.parseString(getResponse.body());
//		JsonArray predictionArray = jsonElement.getAsJsonObject().getAsJsonArray("prediction");
//		double id = predictionArray.get(0).getAsDouble();
//		System.out.println(id);
//		String disease =  findDisease(id);
//		System.out.println(disease);
		SpringApplication.run(SymptomFinderApp.class, args);
	}


}

