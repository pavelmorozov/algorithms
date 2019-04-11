package testDome;

import java.io.StringReader;
import java.util.Collection;
import java.util.HashSet;
import java.util.Set;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;

import org.w3c.dom.Document;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;
import org.xml.sax.InputSource;

public class Folders {
    public static Collection<String> folderNames2of3TestsPassed(String xml, char startingLetter) throws Exception {
    	Set<String> tags = new HashSet<String>();
    	
    	//? - non greedy to not match all the chars until last occurence
    	Pattern regex = Pattern.compile("<folder\\s*name=\"(.*?)\".*?>");
    	Matcher matcher = regex.matcher(xml);
    	
    	while (matcher.find()) {
    		String name = matcher.group(1);
    		if (name.charAt(0)==startingLetter) {
    			tags.add(name);
    		}
    		
        }
    	
    	return tags;
    }
    
    public static Collection<String> folderNames(String xml, char startingLetter) throws Exception {
    	Set<String> tagNames = new HashSet<String>();
        DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
        DocumentBuilder builder = factory.newDocumentBuilder();
        //Document document = builder.parse(xml);
        Document document = builder.parse(new InputSource(new StringReader(xml)));
        NodeList folders = document.getElementsByTagName("folder");
        for (int i = 0; i < folders.getLength(); i++) {
        	Node node = folders.item(i);
        	String name = node.getAttributes().getNamedItem("name").getNodeValue();
    		if (name.charAt(0)==startingLetter) {
    			tagNames.add(name);
    		}
        }
        return tagNames;
    }
    
    
    public static void main(String[] args) throws Exception {
        String xml =
                "<?xml version=\"1.0\" encoding=\"UTF-8\"?>" +
                "<folder name=\"c\">" +
                    "<folder name=\"program files\">" +
                        "<folder name=\"uninstall information\" />" +
                    "</folder>" +
                    "<folder name=\"users\" />" +
                "</folder>";

        Collection<String> names = folderNames(xml, 'u');
        for(String name: names)
            System.out.println(name);
    }
}
