using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

namespace Rextester
{
    public class Program
    {
        public static void Main(string[] args)
        {   int x = 2, y = 1,  z= 1, a=0;  
            List<int> recursion = new List<int>{1,1,2};
            List<int> Fibo_even = new List<int>{};
            while (x < 4000000 ){x = recursion[1+a]+recursion[a];
                                 y = recursion[2+a];
                                 z = recursion[1+a];
                                recursion.Add(y+z);
                                 if (x % 2== 0)
                                 {Fibo_even.Add(x);}
                                 a++;                              
                }
          Console.WriteLine(Fibo_even.Sum());
    }
}
}
