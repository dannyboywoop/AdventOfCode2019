with Ada.Strings.Unbounded;
use Ada.Strings.Unbounded;

package Array_Stuff is

   type Int_Arr is array (Natural range <>) of Integer;
   type Str_Arr is array (Natural range <>) of Unbounded_String;
   function Str_To_Int_Array(strings: Str_Arr) return Int_Arr;
   
   generic
      type T is private;
      with function Transform(X: T) return T;
      type T_Arr is array (Natural range <>) of T;
   function Apply_To_Elements(input: T_Arr) return T_Arr;
   
   generic
      type T is private;
      type T_Arr is array (Natural range <>) of T;
      with function "+" (X, Y: T) return T is <>;
   function Sum_Elements(input: T_Arr; zero: T) return T;

end Array_Stuff;
