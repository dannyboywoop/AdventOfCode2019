with Ada.Text_IO, Array_Stuff;
use Ada.Text_IO, Array_Stuff;

package File_IO is
   function Count_Lines(file: in out File_Type) return Integer;
   function Read_File(filename: String:="input.txt") return Str_Arr;
end File_IO;
