A scirpt for helping to automate nmap usage.

Instal:
 1. Click on the script in your browser and download the raw code locally.
  
 2. Create a bin fodler in your home directory if there isn't one with mkdir.
  
 3. cp the script to the bin folder.
  
 4. Run chmod +x nmap_script to make it executable.
   
 5. mv nmap-script.py nmap_script, Linux doesn't need file extensions, and it makes it easier to typoe in the terminal.
  
 6. Need to add a line to PATH using your terminals config file in your home directory.
    
    For bash: nano .bashrc #Most normal distros terminals use this file
    
    For zsh: nano .zshrc #On Kali this is what you will need to edit
    
 7. Go to the end of the file. In nano press Ctrl+end.
  
 8. Hit enter, then on the new line enter:
  
    export PATH=~/bin:$PATH

 9. In nano press Ctrl+s, then y to save and exit.
  
 10. You will need to exit the terminal and open a new one for the changes to take effect.
