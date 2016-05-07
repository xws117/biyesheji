package show ;


import javax.swing.*;
import javax.swing.border.Border;

import java.awt.*;
import java.awt.event.*;  
import java.sql.ResultSet;  
import java.sql.SQLException; 

public class coon {
	public static void main(String args[]){
		new BoxWindow();
	}
}
class BoxWindow extends JFrame implements ActionListener{
	JButton but,imgbut,haha;
	JTextArea txt;
	JTextArea search;
	Icon  img;  
	JScrollPane p;
	JPanel p1;
	JTextField p2;
	Box basebox,boxv1,boxv2,boxv3,up;
	//JLabel imagelabel;
	BoxWindow(){
		img = new ImageIcon("b.png");
		but = new JButton(img);
		imgbut = new JButton("Search");
		imgbut.addActionListener(this);
		p2 = new JTextField(5);
		p2.setText("Please Input the Protein ID");
		up = Box.createHorizontalBox();
		
		up.add(but);
		up.add(p2);
		up.add(imgbut);
		//up.setLayout(new FlowLayout());
		//up.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
		//--------------------------------上边的窗口---------------------
	    haha = new JButton("qunimeide");
	    txt =new JTextArea();
		boxv1 = Box.createHorizontalBox();
		//boxv1.add(haha);
		boxv1.add(new JScrollPane(txt));
		
		
		//--------------------------------中间的窗口----------------------
		
		boxv2 = Box.createHorizontalBox();
		boxv2.add(new JButton("copyright@2016                                                                         Powered By XiaWeishang"));
		
		
		
		//================================下面的窗口=======================
		
		add(BorderLayout.NORTH,up);
		add(BorderLayout.CENTER,boxv1);
		add(BorderLayout.SOUTH,boxv2);
		validate();
		setVisible(true);
		setBounds(100,10,500,500);
		setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
	}


	@Override
	public void actionPerformed(ActionEvent e) {

		
		//----------------------------------连接数据库----------------------------------------
		String sql = "select * from pro where name = 'sp|A0AVI4|TM129_HUMAN' ";//SQL语句  
	    DBHelper  db1 = new DBHelper(sql);//创建DBHelper对象  
	    String get = p2.getText();
	    System.out.println(get);
	    p2.setText("done");
	  
	    try {  
	    	 ResultSet ret = db1.pst.executeQuery();//执行语句，得到结果集  
	         while (ret.next()) {  
	             String uid = ret.getString(1);  
	             String ufname = ret.getString(2);  
	             String ulname = ret.getString(3);  
	             String udate = ret.getString(4);  
	             System.out.println(uid + "\t" + ufname + "\t" + ulname + "\t" + udate );  
	         }//显示数据  
	         ret.close();  
	         db1.close();//关闭连接  
	        } catch (SQLException error) {  
	            error.printStackTrace();  
	        }  
	}}
