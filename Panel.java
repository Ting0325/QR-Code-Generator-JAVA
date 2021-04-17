import java.awt.Color;
import java.awt.Graphics;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;

import javax.swing.JPanel;

public class Panel extends JPanel{
	int[][] pattern;
	final int SIZE = 500;
	final int MARGIN = 10;
	Panel(){
		this.setBackground(Color.white);
		this.addMouseListener(new MouseAdapter() {
			public void mouseClicked(MouseEvent e) {

				System.out.println(e.getX()+" "+e.getY());
				
			}
		});
	}
	

	public void paintComponent(Graphics g) {
		super.paintComponent(g);
		if(pattern != null){
			int pixelSize = SIZE/pattern.length;
			System.out.println(pixelSize);
			//paint pattern
			for(int i = 0; i < pattern.length;i ++) {
				for(int j = 0; j < pattern[i].length;j++) {
					if(pattern[i][j] == 1)
						g.fillRect(MARGIN+(j*pixelSize), MARGIN+(i*pixelSize),pixelSize, pixelSize);
				}
			}
		}

		
			
	}


	
}