import javax.jws.WebMethod;
import javax.jws.WebService;
import javax.jws.soap.SOAPBinding;

@WebService
@SOAPBinding(style = SOAPBinding.Style.RPC)
public interface MeuServico {
    @WebMethod
    String metodoUm(String parametro);

    @WebMethod
    int metodoDois(int parametro);

    @WebMethod
    void metodoTres(String parametroUm, int parametroDois);

    @WebMethod
    double metodoQuatro(double parametroUm, double parametroDois);
}
@WebService(endpointInterface = "MeuServico")
public class MeuServicoImpl implements MeuServico {
    public String metodoUm(String parametro) {
        return "Olá, " + parametro + "!";
    }

    public int metodoDois(int parametro) {
        return parametro * 2;
    }

    public void metodoTres(String parametroUm, int parametroDois) {
        System.out.println("O parâmetro um é " + parametroUm + " e o parâmetro dois é " + parametroDois);
    }

    public double metodoQuatro(double parametroUm, double parametroDois) {
        return parametroUm + parametroDois;
    }
}
import javax.xml.ws.Endpoint;

public class ServidorSOAP {
    public static void main(String[] args) {
        String url = "http://localhost:8080/meuservico";
        Endpoint.publish(url, new MeuServicoImpl());
        System.out.println("Serviço publicado em " + url);
    }
}
