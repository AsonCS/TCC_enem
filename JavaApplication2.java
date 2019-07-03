/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package javaapplication2;

import java.io.DataOutputStream;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.ConnectException;
import java.net.Socket;
import java.net.UnknownHostException;

public class JavaApplication2{
    
    public static void main(String[] args) {
        PrintService printService = new PrintService("127.0.0.1", 8888);
        printService.sendTPrinter("");
    }
    
}

class PrintService {
    private static final String SUCCESSFULLY_SENT = "Successfully sent to printer";
    public static final int BUFFER_SIZE = 3000;
    private final String ipAddress;
    private static final String TAG = "PrintServiceTask - ";
    private final int portNumber;

    public PrintService(String ipAddress, int portNumber){
        this.ipAddress = ipAddress;
        this.portNumber = portNumber;
    }

    public String sendTPrinter(String htmlString) {
        DataOutputStream outToServer = null;
        Socket clientSocket;
        String result;
        try {
            //StringBuffer bufferr = new StringBuffer("jhdjdshfkjhdkjsdhfkjshdfkjhsdjkfhjksdhfkjshd");
            clientSocket = new Socket(ipAddress, portNumber);
            outToServer = new DataOutputStream(clientSocket.getOutputStream());
            byte[] buffer = {'a','b','a','b','a','b','a','b','a','b','a','b','a','b','a','b','a','b','a','b','a','b','a','b'};
            outToServer.write(buffer);
            outToServer.flush();
            result = SUCCESSFULLY_SENT;
        } catch (ConnectException connectException){
            System.err.println(TAG + connectException.toString());
            result = connectException.toString();
        } catch (UnknownHostException unknownHostException) {
            System.err.println(TAG + unknownHostException.toString());
            result = unknownHostException.toString();
        } catch (IOException ioException) {
            System.err.println(TAG + ioException.toString());
            result = ioException.toString();
        } finally{
            try {
               if (outToServer!=null){
                    outToServer.close();
               }
            }catch (IOException ioException){
                result = ioException.toString();
            }
        }
        return result;
    }
}
