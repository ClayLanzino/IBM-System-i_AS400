///////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
// AS400JConecction example.
// Purpose: This script is designed to illustrate how to use a connection to an IBM System i - AS / 400 Server,
// using the connection and login methods with Java. Additionally it connects to a Database via SQL statements.
// Note: Where xx is the Server IP address.
//
///////////////////////////////////////////////////////////////////////////////////////////////////////////////

import com.ibm.as400.access.AS400JDBCDriver; 
import java.sql.*;

public class AS400JConecction {
  public static void main(String[] args) {

     try {
        System.out.println("Trying to connect...");
        String DRIVER = "com.ibm.as400.access.AS400JDBCDriver";
        String URL = "jdbc:as400://12.34.567.89";
        Class.forName(DRIVER);
        Connection conn = DriverManager.getConnection(URL,"CLAGUT", "CLAGUT");
        Statement stmt = conn.createStatement();
        ResultSet rs = stmt.executeQuery("select employee_code, employee_name, monthly_salary from spiobjuser.nmpp960");
        System.out.println("Connected with " + conn);
        System.out.println("employee_code, employee_name, monthly_salary");
        while(rs.next()) {
            System.out.println(rs.getString("employee_code")+" "+rs.getString("employee_name")+" "+rs.getInt("monthly_salary"));
       }
       conn.close();
       System.exit(0);
    }
    catch(Exception e) {
       System.out.println(e);
    }
  }
 }

