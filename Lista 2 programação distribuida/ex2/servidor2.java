package ex2;
import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Scanner;

public class servidor2 extends Thread {
	private Socket concurrentSocket;

	public servidor2(Socket clientSocket) {
		this.concurrentSocket = clientSocket;
	}

	public static void main(String[] args) {
		try {
			try (ServerSocket serverSocket = new ServerSocket(15000)) {
                System.out.println("Aguardando Cliente");
                while (true){
                	Socket clientSocket = serverSocket.accept();
                	System.out.println("Cliente conectado:"+clientSocket);
                	servidor2 client = new servidor2(clientSocket);
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
                PrintWriter out = new PrintWriter(outputStream, true);

                String Nome = scanner.nextLine();
                String Sexo = scanner.nextLine();
                String Idade = scanner.nextLine();
                String maioridade = " menor de idade";
                
                if(Sexo.equals("masculino")){
                	if(Integer.parseInt(Idade) >= 18){
                		maioridade = " maior de idade";
                	}
                }
				else
					if(Sexo.equals("feminino")){
                		if(Integer.parseInt(Idade) >= 21){
                			maioridade = " maior de idade";
                		}
                	}
                
                out.println("A pessoa: "+Nome+maioridade);
            } 
			catch (NumberFormatException e) {
                e.printStackTrace();
            }
		} catch (IOException i){

        }
	}
}