using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace projeto_wagner_3_bi
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

        //Valor da compra
        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        //qntd parcelas
        private void textBox2_TextChanged(object sender, EventArgs e)
        {

        }

        //efetuar a compra
        DateTime data = DateTime.Now;
        double ValorCompra = 0;
        int NmrParcelas = 0;
        double ValorXParcela = 0;
        int dia = 0;
        int parcelaSerPaga = 0;
        int parcelaPaga = 0;
        double ValorCompraFaltando = 0;
        private void button1_Click(object sender, EventArgs e)
        {
            textBox3.Text = "";
            parcelaSerPaga = 0;
            parcelaPaga = 0;
            ValorCompraFaltando = 0;

            data = DateTime.Now;
            ValorCompra = double.Parse(textBox1.Text);
            NmrParcelas = int.Parse(textBox2.Text);
            ValorXParcela = ValorCompra / NmrParcelas;

            //data.ToString("dd/MM/yyyy");

            //mostra na textbox3 o valor de cada parcela e a data de vencimento dela
            for (int x=0; x<NmrParcelas; x++)
            {
                for (int y = 1; y <= 31; y++)
                { 
                    data = data.AddDays(1);
                    dia = (int)data.DayOfWeek;
                    if (dia > 5 || dia == 0)
                    {
                        data = data.AddDays(2);
                    }
                }
                
                dia = (int)data.DayOfWeek;
                DayOfWeek DiaSemana = data.DayOfWeek;
                textBox3.AppendText("Parcela " + (x+1).ToString() +": R$"+ System.Math.Round(ValorXParcela, 2) + " " + data.ToString("dd/MM/yyyy") +" "+ DiaSemana.ToString() +" "+ dia.ToString() + Environment.NewLine);
            }
        }

        //Lista com as datas de cada parcelas e seus respectivos valores
        private void textBox3_TextChanged(object sender, EventArgs e)
        {

        }

        //botão para enviar a data do pagamento da parcela atual
         private void button2_Click(object sender, EventArgs e)
         {
            data = DateTime.Now;
            textBox3.Text = "";
            int compareParcela = 0;
            int dia = int.Parse(textBox4.Text);
            int mes = int.Parse(textBox6.Text);
            int ano = int.Parse(textBox5.Text);
            parcelaSerPaga = int.Parse(textBox7.Text);
            
            DateTime DataParcela = new DateTime(ano, mes, dia);


            ValorCompra = double.Parse(textBox1.Text);
            NmrParcelas = int.Parse(textBox2.Text);
            ValorXParcela = ValorCompra / NmrParcelas;
            ValorCompraFaltando = ValorCompra;

            if (parcelaPaga < NmrParcelas-1 )
            {
                if (parcelaSerPaga > parcelaPaga+1)
                {   
                    //mostra na textbox3 o valor de cada parcela e a data de vencimento dela
                    for (int x = parcelaPaga; x < NmrParcelas; x++)
                    {
                        for (int y = 1; y <= 31; y++)
                        {
                            data = data.AddDays(1);
                            dia = (int)data.DayOfWeek;
                            if (dia > 5 || dia == 0)
                            {
                                data = data.AddDays(2);
                            }
                        }

                        dia = (int)data.DayOfWeek;
                        DayOfWeek DiaSemana = data.DayOfWeek;
                        textBox3.AppendText("Parcela " + (x + 1).ToString() + ": R$" + System.Math.Round(ValorXParcela, 2) + " " + data.ToString("dd/MM/yyyy") + " " + DiaSemana.ToString() + " " + dia.ToString() + Environment.NewLine);
                    }
                    label4.Text = "Deve-se pagar outras parcelas antes!" + Environment.NewLine +"Valor restante a ser pago: R$" + (ValorCompraFaltando - (ValorXParcela * parcelaPaga));
                }
                else if(parcelaSerPaga-1 == parcelaPaga)
                {
                    parcelaPaga = parcelaPaga + 1;
                    //mostra na textbox3 o valor de cada parcela e a data de vencimento dela
                        for (int x = parcelaPaga; x < NmrParcelas; x++)
                        {
                                for (int y = 1; y <= 31; y++)
                                {
                                    data = data.AddDays(1);
                                    dia = (int)data.DayOfWeek;
                                    if (dia > 5 || dia == 0)
                                    {
                                        data = data.AddDays(2);
                                    }
                                }
                            dia = (int)data.DayOfWeek;
                            DayOfWeek DiaSemana = data.DayOfWeek;
                            textBox3.AppendText("Parcela " + (x + 1).ToString() + ": R$" + System.Math.Round(ValorXParcela, 2) + " " + data.ToString("dd/MM/yyyy") + " " + DiaSemana.ToString() + " " + dia.ToString() + Environment.NewLine);
                        }
                        ValorCompraFaltando -= (ValorXParcela * parcelaPaga);
                        label4.Text = "Parcela paga!" + Environment.NewLine + "Valor restante a ser pago: R$" + ValorCompraFaltando;
                    
                }
                else
                {
                    //mostra na textbox3 o valor de cada parcela e a data de vencimento dela
                    for (int x = parcelaPaga; x < NmrParcelas; x++)
                    {
                        for (int y = 1; y <= 31; y++)
                        {
                            data = data.AddDays(1);
                            dia = (int)data.DayOfWeek;
                            if (dia > 5 || dia == 0)
                            {
                                data = data.AddDays(2);
                            }
                        }

                        dia = (int)data.DayOfWeek;
                        DayOfWeek DiaSemana = data.DayOfWeek;
                        textBox3.AppendText("Parcela " + (x + 1).ToString() + ": R$" + System.Math.Round(ValorXParcela, 2) + " " + data.ToString("dd/MM/yyyy") + " " + DiaSemana.ToString() + " " + dia.ToString() + Environment.NewLine);
                    }
                    label4.Text = "Parcela já foi paga!" + Environment.NewLine + "Valor restante a ser pago: R$" + (ValorCompraFaltando - (ValorXParcela * parcelaPaga));
                }
            }
            else
            {
                textBox3.Text = "Compra fechada!";
                label4.Text = "Valor completamente pago.";
            }
              
         }

        //Dia
        private void textBox4_TextChanged(object sender, EventArgs e)
        {

        }
        
        //Mes
        private void textBox6_TextChanged(object sender, EventArgs e)
        {

        }

        //Ano
        private void textBox5_TextChanged(object sender, EventArgs e)
        {

        }

        //valor restante a ser pago
        private void label4_Click(object sender, EventArgs e)
        {

        }

        //numero parcela a ser paga
        private void textBox7_TextChanged(object sender, EventArgs e)
        {

        }
    }
}
