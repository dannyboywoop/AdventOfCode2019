with Ada.Command_Line, Ada.Text_IO, Ada.Strings.Unbounded, Array_Stuff;
use Ada.Command_Line, Ada.Text_IO, Ada.Strings.Unbounded, Array_Stuff;

package body File_IO is

   
   function Count_Lines(file: in out File_Type) return Integer is
      New_Lines : Integer := 0;
   begin
      --Skip through the file one line at a time
      while not Ada.Text_IO.End_Of_File(file) loop
         Skip_Line(file);
         New_Lines := New_Lines + 1;
      end loop;
      Reset(file);
      return New_Lines;
   end Count_Lines;
   
   
   function Read_File(filename: String:="input.txt") return Str_Arr is
      input : File_Type;
   begin
      --Attempt to open the file
      begin
         Open (File => input,
               Mode => In_File,
               Name => filename);
      exception
         when others =>
            Put_Line (Standard_Error,
                      "Can not open the file '" & filename & "'!");
            Set_Exit_Status (Failure);
      end;
      
      --Read lines into string array
      declare
         strings : Str_Arr(1..Count_Lines(input));
         i : integer:=1;
      begin
         while not End_Of_File (input) loop
            strings(i):=To_Unbounded_String(Get_Line(input));
            i := i+1;
         end loop;
         return strings;
      end;
           
   end Read_File; 

end File_IO;
