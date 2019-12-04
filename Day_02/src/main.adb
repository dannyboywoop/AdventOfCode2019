with File_IO; use File_IO;
with Ada.Text_IO; use Ada.Text_IO;
with Array_Stuff; use Array_Stuff;
with Ada.Strings.Unbounded; use Ada.Strings.Unbounded;
with String_Stuff; use String_Stuff;
with Intcode; use Intcode;

procedure Main is
   input: Unbounded_String:=Read_File("input.txt")(1);
   strings: Str_Arr:=Split(input, ",");
   program_data: Int_Arr:=Str_To_Int_Array(strings);
   star_one_data: Int_Arr:=Initialise_Program(program_data, 12, 2);
   star_one, star_two: Integer;
begin
   star_one:= Run_Program(star_one_data);
   Put_Line("Star one: "&Integer'Image(star_one));

   star_two:= Find_Start_Vals(program_data, 19690720);
   Put_Line("Star two: "&Integer'Image(star_two));
end Main;
