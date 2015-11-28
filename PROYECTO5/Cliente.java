import java.io.*;
import java.net.*;

public class Cliente{
	static String [] cliente = {"German", "Alberto", "Josue"};
	static String [] pass = {"12345", "54321", "34567"};

	public static void main (String[] args) throws IOException{
		String user="";
		String password="";
		int i;

		InputStreamReader isr = new InputStreamReader(System.in);
		BufferedReader br = new BufferedReader(isr);

		//Relación servidor

		Socket socket = new Socket("localhost", 8080);
		PrintWriter out = new PrintWriter(socket.getOutputStream());
		InputStreamReader in = new InputStreamReader(socket.getInputStream());
		BufferedReader bf = new BufferedReader(in);

		do{
			System.out.print("\nIngrese su usuario: ");
			user = br.readLine();
			if(cliente[0].equals(user)){
				System.out.println("\n\tHola " + user);
				System.out.print("\nIngresa tu password: ");
				do{
					password = br.readLine();
					if(pass[0].equals(password)){
					System.out.println("\n\tBienvenido " + user + " has ingresado correctamente\n");
					}
					else{
						System.out.println("***Password incorrecta***");
						System.out.print("\nIntenta de nuevo:  ");
					}

				}while(password != pass[0]);
			}
			else {
				System.out.println("\n" + user + " no esta registrado\n");
				
			}
		}while(user != "German");
		
	}
}
