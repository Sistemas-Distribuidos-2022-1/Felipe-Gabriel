package ex6;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Scanner;

public class servidor6 extends Thread {
	private Socket concurrentSocket;

	public servidor6(Socket clientSocket) {
		this.concurrentSocket = clientSocket;
	}

	public static void main(String[] args) {
		try {
			try (ServerSocket serverSocket = new ServerSocket(1010)) {
                System.out.println("Aguardando Cliente");
                while (true){
                	Socket clientSocket = serverSocket.accept();
                	System.out.println("Cliente conectado:"+clientSocket);
                	servidor6 client = new servidor6(clientSocket);
                	client.start();
                }
            }
		} 
        catch (IOException i){}
	}

	public void run(){
		try {
			InputStream inputStream = concurrentSocket.getInputStream();
			try (Scanner scanner = new Scanner(inputStream)) {
                OutputStream outputStream = concurrentSocket.getOutputStream();
                PrintWriter out = new PrintWriter(outputStream, true);

                String nome = scanner.nextLine();
                String nivel = scanner.nextLine();
                String salario = scanner.nextLine();
                String nmrdependents = scanner.nextLine();
                float salariobruto = Float.parseFloat(salario);
                int dependentes = Integer.parseInt(nmrdependents);

                
                if(nivel.equals("A")){
                	if(dependentes != 0){
                		salariobruto *= 0.92;
                	}
                    else{
                		salariobruto *= 0.97;
                	}
                }
                else
                     if(nivel.equals("B")){
                	    if(dependentes != 0){
                		    salariobruto *= 0.90;
                	}
                    else{
                		salariobruto *= 0.95;
                	}
                }else
                     if(nivel.equals("C")){
                	    if(dependentes != 0){
                		    salariobruto *= 0.85;
                	}
                    else{
                		salariobruto *= 0.92;
                	}
                }
                else  
                    if(nivel.equals("D")){
                	    if(dependentes != 0){
                    		salariobruto *= 0.83;
                	}
                    else{
                		salariobruto *= 0.90;
                	}
                }
                else{
                	out.println("Categoria invalida");
                }
                
                out.println("Funcionario: "+nome+" Nivel: '"+nivel+"' Salario liquido:R$ "+salariobruto);
            } 
            catch (NumberFormatException e) {
               
                e.printStackTrace();
            }
		} 
        catch (IOException i){}
	}
}