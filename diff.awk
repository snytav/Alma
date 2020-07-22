{
   if(NR == 1)
   {
      fn1 = FILENAME
      fn2 = fn1
      NF1 = NF
      flag = 1
   }
   if(fn2 != FILENAME)
   {
      NR1 = NR-1
      print(NR1)
      #lag = 0
      fn2 = FILENAME
   }
         
   for(i=1;i <= NF;i++)
   {
      a[NR,i]=$i
      print(a[NR,i],i,NR)
   }
}
END{
    
   if((NR1*2 != NR) || (NF1 != NF))
   {
      print(fn1,fn2,NF1,NF,NR1,NR)
      print("different size files !!!!")
      exit
   }
   diff = 0.0
   for(j = 1;j <= NF;j++)
   {
       for(i = 1;i <= NR/2;i++)
       {
           t = a[i,j] - a[i+NR/2,j]
           if(t < 0) t = -t

           printf("i %10d j %d %25.15e %25.15e %e\n",i,NR,a[i,j],a[i+NR/2,j],t)

           if (t > diff)
           {
              diff = t
              e_j  = j
              e_i  = i
              printf("%10d %25.15e %25.15e %e\n",i,a[i,j],a[i+NR/2,j],t)
           }
       }
   }

   printf("%e row %d col %d %e %e \n",diff,e_i,e_j,a[e_i,e_j],a[e_i+NR/2,e_j]) 
   
}
