with Array_Stuff;
use Array_Stuff;

package Rocket_Maths is
   
   function Calculate_Fuel_Cost(mass: Integer) return Integer;
   function Calculate_Recursive_Fuel_Cost(mass: Integer) return Integer;
   function Get_Required_Fuel(masses: Int_Arr; recursive: Boolean) return Integer;

end Rocket_Maths;
