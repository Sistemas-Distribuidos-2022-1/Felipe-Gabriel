package ex3;
import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Scanner;

public class servidor3 extends Thread {
	private Socket concurrentSocket;

	public servidor3(Socket clientSocket) {
		this.concurrentSocket = clientSocket;
	}

	public static void main(String[] args) {
		try {
			try (ServerSocket serverSocket = new ServerSocket(15000)) {
                System.out.println("Aguardando Cliente");
                while (true){
                	Socket clientSocket = serverSocket.accept();
                	System.out.println("Cliente conectado:"+clientSocket);
                	servidor3 client = new servidor3(clientSocket);
                	client.start();
                }
            }
		} 
        catch (IOException i){
            
        }
	}

	public void run(){
		try {
			InputStream inputStream = concurrentSocket.getInputStream();
			try (Scanner scanner = new Scanner(inputStream)) {
                OutputStream outputStream = concurrentSocket.getOutputStream();
                PrintWriter out = new PrintWriter(outputStream, true);

                String snota1 = scanner.nextLine();
                String snota2 = scanner.nextLine();
                String snota3 = scanner.nextLine();
                String foi_aprovado = "Reprovado";
                int nota1 = Integer.parseInt(snota1);
                int nota2 = Integer.parseInt(snota2);
                int nota3 = Integer.parseInt(snota3);
                float media1 = (nota1+nota2)/2;
                float media2 = (media1+nota3)/2;

                if(media1 >= 7){
                	foi_aprovado ="Aprovado";
                }
                else
                    if(media1 >= 3 & media2 >= 5 ){
                	    foi_aprovado ="Aprovado";
                }
                
                out.println(foi_aprovado);
            } 
            catch (NumberFormatException e) {
             
                e.printStackTrace();
            }
		} 
        catch (IOException i){

        }
	}

}