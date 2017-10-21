a = 5; b = -13; c = 11;
        
        final long startTimer = System.nanoTime();
        function = ( (((a-5)*(a+9) + a*b*c)%513)*Math.log(32) )*Math.PI/( Math.log(32)*Math.PI );
        final double temp = rand.nextDouble()*rand.nextInt(Integer.MAX_VALUE);
        System.out.println(temp+ ", TEXT: "+Math.pow(Math.log(32), temp));
        function = ( (((a-5)*(a+9) + a*b*c)%513)*Math.pow(Math.log(32), temp) )/( Math.pow(Math.log(32),temp) );
        double abc = (a*b*c)%513;


final long  endTimer = System.nanoTime();
        final double timeTook = (endTimer - startTimer)/Math.pow(10, 9);
        System.out.println("Time: "+timeTook+"\nShould be: "+abc+"\nIs: "+function);