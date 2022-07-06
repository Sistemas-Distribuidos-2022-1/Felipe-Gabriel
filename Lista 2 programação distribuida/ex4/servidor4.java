package ex4;
import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Scanner;

public class servidor4 extends Thread {
	private Socket concurrentSocket;

	public servidor4(Socket clientSocket) {
		this.concurrentSocket = clientSocket;
	}

	public static void main(String[] args) {
		try {
			try (ServerSocket serverSocket = new ServerSocket(15000)) {
                System.out.println("Aguardando Cliente");
                while (true){
                	Socket clientSocket = serverSocket.accept();
                	System.out.println("Cliente conectado:"+clientSocket);
                	servidor4 client = new servidor4(clientSocket);
                	client.start();
                }
            }
		} catch (IOException i){

        }
	}

	public void run(){
		try {
			InputStream inputStream = concurrentSocket.getInputStream();
			try (Scanner scanner = new Scanner(inputStream)) {
                OutputStream outputStream = concurrentSocket.getOutputStream();
                PrintWriter out =new PrintWriter(outputStream, true);

                String alturaEntrada = scanner.nextLine();
                String sex = scanner.nextLine();
                
                float peso;
                float altura = Float.parseFloat(alturaEntrada);
                String pesoideal;

                if(sex.equals("masculino")){
                	peso = (float) ((altura * 72.7) - 58);
                	pesoideal = Float.toString(peso);
                }
                else 
                    if(sex.equals("feminino")){
                	    peso = (float) ((altura * 62.1) - 44.7);
                	    pesoideal = Float.toString(peso);
                }
                else{
                	pesoideal = ("Sexo não identificado");
                }
                
                out.println(pesoideal);
            } 
            catch (NumberFormatException e) {
               
                e.printStackTrace();
            }
		} catch (IOException i){

        }
	}

}