/* *******************************************************************
* Colegio Técnico Antônio Teixeira Fernandes (Univap)
* Curso Técnico em Informática - Data de Entrega: 15/06/2022
* Autores do Projeto: Rafael Giordano Matesco
* Turma: 2H
* Atividade Proposta em aula
* Observação: <colocar se houver>
* 
* Form1.cs
* ************************************************************/

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace atividade_8
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {
        }

        private void button1_Click(object sender, EventArgs e)
        {

            double area = double.Parse(textBox1.Text);
            double raio = area / Math.PI;
            raio = Math.Sqrt(raio);
            raio = Math.Round(raio);

            double numProximo = 0;
            double numAnterior;
            int numeroAnterior = 0;
            int numeroAtual = 1;
            int fibonacci;
            int m1=0; 
            int n1=0; 
            int m2=0; 
            for (int i = 0; i < 1000; i++)
            {
                fibonacci = numeroAnterior + numeroAtual;
                Console.WriteLine(fibonacci);
                numeroAnterior = numeroAtual;
                numeroAtual = fibonacci;
                numAnterior = raio - numeroAtual;
                if(numAnterior > numProximo)
                {
                    m1 = numeroAnterior;
                }else if(numAnterior < numProximo)
                {
                    m2 = numeroAnterior*-1;
                    n1 = 1;
                }

                if(n1 == 1)
                {
                    if (m1 > m2)
                    {
                        label1.Text = "Número fibonnacci mais próximo do raio " + raio.ToString() + ":" + numeroAtual.ToString();
                        break;
                    }else if (m2 > m1)
                    {
                        label1.Text = "Número fibonnacci mais próximo do raio " + raio.ToString() + ":" + numeroAtual.ToString();
                        break;
                    }
                }

                


            }


        }

    }
}
