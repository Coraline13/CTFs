import java.rmi.Remote;
import java.rmi.RemoteException;

public interface FlagInterface extends Remote {
    String printFlag() throws RemoteException;
}
