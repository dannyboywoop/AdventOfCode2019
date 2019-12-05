with Array_Stuff;
use Array_Stuff;

package body Rocket_Maths is

   function Calculate_Fuel_Cost(mass: Integer) return Integer is
   begin
      return mass/3 - 2;
   end Calculate_Fuel_Cost;  
   
   
   function Calculate_Recursive_Fuel_Cost(mass: Integer) return Integer is
      fuel: Integer:= Calculate_Fuel_Cost(mass);
   begin
      if fuel < 0 then
         return 0;
      else
         return fuel + Calculate_Recursive_Fuel_Cost(fuel);
      end if;
   end Calculate_Recursive_Fuel_Cost;
   
   
   function Get_Required_Fuel(masses: Int_Arr; recursive:Boolean) return Integer is
      function Get_Each_Fuel_Cost is new Transform_Elements(T => Integer,
                                                           T_Arr => Int_Arr,
                                                           Transform => Calculate_Fuel_Cost);
         
      function Get_Each_Fuel_Cost_Recursive is new Transform_Elements(T => Integer,
                                                                     T_Arr => Int_Arr,
                                                                     Transform => Calculate_Recursive_Fuel_Cost);
      function Sum_Ints is new Sum_Elements(T => Integer,
                                            T_Arr => Int_Arr);
      fuel_needed :Int_Arr(masses'Range);
   begin
      if recursive then
         fuel_needed:=Get_Each_Fuel_Cost_Recursive(masses);
      else
         fuel_needed:=Get_Each_Fuel_Cost(masses);
      end if;
      return Sum_Ints(fuel_needed, 0);
   end Get_Required_Fuel;

end Rocket_Maths;
