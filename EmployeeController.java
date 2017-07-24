package com.journaldev.spring.controller;

import java.util.ArrayList;
import java.util.Date;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Set;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;

import com.journaldev.spring.model.Employee;

/**
 * Handles requests for the Employee service.
 */
@Controller
public class EmployeeController {
	
	private static final Logger logger = LoggerFactory.getLogger(EmployeeController.class);
	
	//Map to store employees, ideally we should use database
	Map<Integer, Employee> empData = new HashMap<Integer, Employee>();
	Map<String, Object> empData1 = new HashMap<String, Object>();
	
String dp_loanStat ="nt001000        loan                                                                                    lm001000    795782566M987     0SRI NIKHIL PHALGHU            201507292016110810000000000000000000000000013470020170324000000000000000000000001000000000000000000000000000000001 O00000000000000000000 149000000000000 000000000000010000000100000000                                           00000000673500201609201703P000000128000  201";   
	
    String Policy_no = "795782566987    ";//reference info
    String self_code = "CBK1";//source brn code
    String remote_code = "X095";//remote brn code==DC Code
    String priority = "1";
    String prg_name = "portlonq";
    String prg_input_param = "QY  ";
    String auth_send = "    ";
    String auth_rec = "    ";
    //buffer length changed
    String buf_len = "0450";
    String req_code = "1";
    String res_code = "     ";
    String encrp_ind = "N";
    String timestamp = "2017030810593405";
    String trans_no = "00000000";
    String tib_res_code = "06";
    String future_use = "Y   ";
    String remote_server_code = "987 ";//branch Code
    String remote_server_sub_code = "    ";
    String remote_future_use = "   ";
    String prog_group = "  ";
    String DataPart=dp_loanStat;
	

	
	@RequestMapping(value = EmpRestURIConstants.DUMMY_EMP1, method = RequestMethod.GET)
	public @ResponseBody  List<String> getDummyEmployee1() {
		logger.info("Start getDummyEmployee");
		

	    empData1.put("SOURCEBRANCHCODE", self_code);
	    empData1.put("REMOTEBRANCHCODE", remote_code);
	    empData1.put("PRIORITYLEVEL", priority);
	    empData1.put("PROGRAMNAME", prg_name);
	    empData1.put("PROGRAMINPUTPARAM", prg_input_param);
	    empData1.put("AUTHORIZATIONSENDER", auth_send);
	    empData1.put("AUTHORIZATIONRECEIVER", auth_rec);
	    empData1.put("BUFFERLENGTH", buf_len);
	    empData1.put("REQUESTCODE", req_code);
	    empData1.put("RESPONSECODE", res_code);
	    empData1.put("ENCRYPTIONINDICATOR", encrp_ind);
	    empData1.put("TIMESTAMP", timestamp);
	    empData1.put("TRANSNO", trans_no);
	    empData1.put("REFERENCENO", Policy_no);
	    empData1.put("TIBCORESCODE", tib_res_code);
	    empData1.put("FUTUREUSE", future_use);
	    empData1.put("REMOTESERVERCODE", remote_server_code);
	    empData1.put("REMOTESERVERSUBCODE", remote_server_sub_code);
	    empData1.put("REMOTEFUTUREUSE", remote_future_use);
	    empData1.put("PROGRAMGROUP", prog_group);
	    empData1.put("DATAPART", DataPart);
	    
	   
	   
	    List<String> emps1 = new ArrayList<String>();
	    
	    for (Entry<String, Object> entry : empData1.entrySet())
	    {
        emps1.add(entry.getValue().toString());
	  
		}

    
		return emps1;
	}

}
