/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package robotbuilder.data.properties;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import javax.swing.JComboBox;
import javax.swing.JFileChooser;
import javax.swing.filechooser.FileNameExtensionFilter;
import robotbuilder.data.RobotComponent;
import sun.java2d.loops.ProcessPath;

/**
 *
 * @author Alex Henning
 */
public class FileProperty extends Property {
    protected String value, extension;
    protected boolean folder;
    protected JFileChooser chooser;
    
    public FileProperty() {}
    
    public FileProperty(String name, Object defaultValue, String[] validators, RobotComponent component,
            String value, String extension, boolean folder) {
        super(name, defaultValue, validators, component);
        this.value = value;
        this.extension = extension;
        this.folder = folder;
    }

    @Override
    public Property copy() {
        return new FileProperty(name, defaultValue, validators, component, value, extension, folder);
    }

    @Override
    public Object getValue() {
        return (value != null) ? value : defaultValue;
    }
    
    @Override
    public Object getDisplayValue() {
        if (chooser == null) {
            chooser = new JFileChooser(component.getRobotTree().getFilePath());
            if (folder) {
                chooser.setFileSelectionMode(JFileChooser.DIRECTORIES_ONLY);
            } else {
                chooser.setFileSelectionMode(JFileChooser.FILES_ONLY);
                chooser.setFileFilter(new FileNameExtensionFilter(extension+" file", extension));
            }
            chooser.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent ae) {
                    System.out.println(ae.getActionCommand());
                    if (ae.getActionCommand().equals("ApproveSelection")){
                        setValue(chooser.getSelectedFile().getPath());
                    }
                }
            });
        }
        update();
        return chooser;
    }

    @Override
    public void setValue(Object value) {
        if (extension != null && value != null
                && !((String) value).endsWith("."+extension)) {
            value = ((String) value)+"."+extension;
        }
        System.out.println(name+" => "+value);
        super.setValue(value);
        this.value = (String) value;
    }

    public String getExtension() {
        return extension;
    }
    public void setExtension(String extension) {
        this.extension = extension;
    }

    public boolean getFolder() {
        return folder;
    }
    public void setFolder(boolean folder) {
        this.folder = folder;
    }
    
    @Override
    public void update() {
        super.update();
        if (chooser != null && !getValue().equals("")) {
            chooser.setSelectedFile(new File(getValue().toString()));
            value = chooser.getSelectedFile().toString();
        }
    }
    
}
