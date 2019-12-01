with Array_Stuff;
use Array_Stuff;

package body Rocket_Maths is

   
   function Calculate_Fuel_Cost(mass: Integer) return Integer is
   begin
      return mass/3 - 2;
   end Calculate_Fuel_Cost;

   
   function Get_Required_Fuel(masses: Int_Arr) return Integer is
      function Get_Each_Fuel_Cost is new Apply_To_Elements(T => Integer,
                                                           T_Arr => Int_Arr,
                                                           Transform => Calculate_Fuel_Cost);
      function Sum_Ints is new Sum_Elements(T => Integer,
                                            T_Arr => Int_Arr);
      fuel_needed :Int_Arr(masses'Range);
   begin
      fuel_needed:=Get_Each_Fuel_Cost(masses);
      return Sum_Ints(fuel_needed, 0);
   end Get_Required_Fuel;

end Rocket_Maths;
