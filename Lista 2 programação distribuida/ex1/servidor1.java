package ex1;
import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Scanner;

public class servidor1 extends Thread {
	private Socket concurrentSocket;

	public servidor1(Socket clientSocket) {
		this.concurrentSocket = clientSocket;
	}


	public static void main(String[] args) {
		try {
			try (ServerSocket serverSocket = new ServerSocket(15000)) {
				System.out.println("Aguardando Cliente");
				while (true){
					Socket clientSocket = serverSocket.accept();
					System.out.println("Cliente conectado:"+clientSocket);
					servidor1 client = new servidor1(clientSocket);
					client.start();
				}
			}
		} catch (IOException i){
	}
}
/*--------------------------------------------------------------------------*/
	/*recebe os dados do programa cliente */
    public void run(){
		try {
			InputStream inputStream = concurrentSocket.getInputStream();
			try (Scanner scanner = new Scanner(inputStream)) {
				OutputStream outputStream = concurrentSocket.getOutputStream();
				PrintWriter out = new PrintWriter(outputStream, true);

				String Nome = scanner.nextLine();
				String Cargo = scanner.nextLine();
				String Salario = scanner.nextLine();
				float reajusteSalarial;
				
				/*calcula os reajustes salariais */
				if(Cargo.equals("operador")){
					float salarioAntigo = Float.parseFloat(Salario);
					reajusteSalarial = (float) (salarioAntigo*1.2);
				}
				if(Cargo.equals("Operador")){
					float salarioAntigo = Float.parseFloat(Salario);
					reajusteSalarial = (float) (salarioAntigo*1.2);
				}
				else
				     if(Cargo.equals("programador")){
					    float salarioAntigo = Float.parseFloat(Salario);
					    reajusteSalarial = (float) (salarioAntigo * 1.18);
				}
					if(Cargo.equals("Programador")){
						float salarioAntigo = Float.parseFloat(Salario);
						reajusteSalarial = (float) (salarioAntigo * 1.18);
					}
				else{
					float salarioAntigo = Float.parseFloat(Salario);
					reajusteSalarial = (float) (salarioAntigo * 1.0);
				}
				
				out.println("Nome: "+Nome+". Salario ajustado: R$"+Float.toString(reajusteSalarial));
			} catch (NumberFormatException e) {
			
				e.printStackTrace();
			}
		} 
        catch (IOException i){}
	}
}