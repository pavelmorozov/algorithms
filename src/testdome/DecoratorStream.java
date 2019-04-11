package testDome;

import java.io.BufferedReader;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;

public class DecoratorStream extends OutputStream {

	private boolean firstFlag = true;

	private OutputStream stream;
	private String prefix;

	public DecoratorStream(OutputStream stream, String prefix) {
		super();
		this.stream = stream;
		this.prefix = prefix;
	}

	@Override
	public void write(int b) throws IOException {
		byte[] result = new byte[1];
		result[0] = (byte) (b);
		stream.write(result, 0, 1);
	}

	@Override
    public void write(byte[] b, int off, int len) throws IOException {
    	byte[] lineBytes = null;
    	if (firstFlag) {
        	String s = (new String(prefix.getBytes("UTF-8"), "UTF-8")) + (new String(b, "UTF-8"));
        	lineBytes = s.getBytes("UTF-8");
        	firstFlag=false;
    	}else {
    		lineBytes = b;
    	}
    	
        for (int i = 0 ; i < lineBytes.length ; i++) {
            write(lineBytes[off + i]);
        }
    }

	@Override
	public void write(byte[] b) throws IOException {
		write(b, 0, b.length);
	}

	public static void main(String[] args) throws IOException {
		byte[] message = new byte[] { 0x48, 0x65, 0x6c, 0x6c, 0x6f, 0x2c, 0x20, 0x77, 0x6f, 0x72, 0x6c, 0x64, 0x21 };
		try (ByteArrayOutputStream baos = new ByteArrayOutputStream()) {
			DecoratorStream decoratorStream = new DecoratorStream(baos, "大 Украина First line: ");
			decoratorStream.write(message);

			try (BufferedReader reader = new BufferedReader(
					new InputStreamReader(new ByteArrayInputStream(baos.toByteArray()), "UTF-8"))) {
				System.out.println(reader.readLine()); // should print "First line: Hello, world!"
			}
		}
	}
}