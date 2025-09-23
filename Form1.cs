using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Reflection.Emit;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using textfile_generator.Properties;

namespace textfile_generator
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string fcontent = file_content.Text;
            string fname =file_name.Text;

            File.WriteAllText(fname + ".txt", fcontent);  // Create a file and write the content of writeText to it

        }

        private void file_content_TextChanged(object sender, EventArgs e)
        {

        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void fish_Click(object sender, EventArgs e)
        {
            
        }

        private void normal_Click(object sender, EventArgs e)
        {

        }
    }
}
