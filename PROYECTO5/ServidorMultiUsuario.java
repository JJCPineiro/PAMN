import java.net.*;
import java.io.*;

public class ServidorMultiUsuario{
	public static final Proceso arreglo[] = new Proceso[3];
	
	public static void main(String args[]) throws IOException, UnknownHostException{

		Socket cliente;
		ServerSocket servidor;

		servidor = new ServerSocket(8080);
		System.out.println("...Servidor encendido...");
		int i = 0;
		while(i<3){

			cliente = servidor.accept();
			(arreglo[i] = new Proceso(cliente, arreglo)).start();
			System.out.println("--> Nuevo usuario conectado");
			i++;
		}
		System.out.println("...Servidor apagado...");

	}

}
