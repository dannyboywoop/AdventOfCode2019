with Ada.Text_IO, File_IO, Array_Stuff, Rocket_Maths;
use Ada.Text_IO, File_IO, Array_Stuff, Rocket_Maths;

procedure Main is
   strings : Str_Arr:=Read_File;
   masses : Int_Arr:=Str_To_Int_Array(strings);
begin
   Put_Line(Get_Required_Fuel(masses, True)'Image);
end Main;
