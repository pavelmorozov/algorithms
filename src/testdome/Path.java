package testDome;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Path {
    private String path;

    public Path(String path) {
        this.path = path;
    }

    public String getPath() {
        return path;
    }

    private List<String> getChunks (String source) {
        List<String> chunks = Arrays.stream(source.split("/")).
        		filter(s -> {
        			if (s.isEmpty()) return false;
        			return true;
        		}).
        		map(s -> s).
        		collect(Collectors.toList());
    	return chunks;
    }
    
    public void cd(String newPath) {
        //String[] folders = path.split("/");
        List<String> folders = getChunks(path);
        List<String> newFolders = getChunks(newPath);
        
        for (String s : newFolders) {
        	if (s.equals("..")) 
        		folders.remove(folders.size()-1); 
        	else folders.add(s);
        }
        
        StringBuilder sb = new StringBuilder(); 
        //sb.append("/");
        folders.forEach(f -> {
        	sb.append("/");
        	sb.append(f);
        });
        
        if (folders.isEmpty()) sb.append("/");
        
        path = sb.toString();
    }

    public static void main(String[] args) {
        Path path = new Path("/a/b/c/d");
        path.cd("../x");
        System.out.println(path.getPath());
    }
}