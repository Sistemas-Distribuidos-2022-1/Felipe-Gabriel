package ex5;
import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Scanner;

public class servidor5 extends Thread {
	private Socket concurrentSocket;

	public servidor5(Socket clientSocket) {
		this.concurrentSocket = clientSocket;
	}

	public static void main(String[] args) {
		try {
			try (ServerSocket serverSocket = new ServerSocket(7890)) {
                System.out.println("Aguardando Cliente");
                while (true){
                	Socket clientSocket = serverSocket.accept();
                	System.out.println("Cliente conectado:"+clientSocket);
                	servidor5 client = new servidor5(clientSocket);
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

                String idaderecebida = scanner.nextLine();
                String categoria;
                int idade = Integer.parseInt(idaderecebida);
                if(idade >= 18){
                	categoria = "Adulto";
                }
                else
                    if(idade >= 14){
                	    categoria = "Juvenil B";
                }
                else 
                    if(idade >= 11){
                	    categoria = "Juvenil A";
                }
                else
                    if(idade >= 8){
                	    categoria = "Infantil B";
                }
                else 
                    if(idade >= 5){
                	    categoria = "Infantil A";
                }
                    else{
                	    categoria = "Não existe";
                }
                
                out.println(categoria);
            } 
            catch (NumberFormatException e) {
                
                e.printStackTrace();
            }
		} 
        catch (IOException i){

        }
	}
}