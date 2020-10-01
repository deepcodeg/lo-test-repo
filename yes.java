public class C {
    public synchronized int read() throws IOException {
      final byte[] b = new byte[1];
      if (doRead(b, 0, 1) == -1) {
        return -1;
      }
      return b[0];
    }
}
