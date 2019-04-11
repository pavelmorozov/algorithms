package testDome;

import java.util.HashSet;
import java.util.Set;

public class Song {
    private String name;
    private Song nextSong;
    
    public Song(String name) {
        this.name = name;
    }

    public void setNextSong(Song nextSong) {
        this.nextSong = nextSong;
    }

    public boolean isRepeatingPlaylist() {
    	Set<Song> processedSongs = new HashSet<Song>();
    	Song currentSong = this;
    	while (currentSong!=null) {
    		if (processedSongs.contains(currentSong)) return true;
    		processedSongs.add(currentSong);
    		currentSong = currentSong.nextSong;
    	}
    	return false;
    }

    public static void main(String[] args) {
        Song first = new Song("Hello");
        Song second = new Song("Eye of the tiger");
        Song third = new Song("third");

        first.setNextSong(second);
        second.setNextSong(third);
        third.setNextSong(first);

        System.out.println(first.isRepeatingPlaylist());
        System.out.println(second.isRepeatingPlaylist());
    }
}