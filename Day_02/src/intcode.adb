with Ada.Text_IO; use Ada.Text_IO;
with Array_Stuff; use Array_Stuff;

package body Intcode is

   function Initialise_Program(program_data: Int_Arr; 
                                noun, verb: Integer) return Int_Arr is
      initialised_data: Int_Arr:= program_data;
   begin
      initialised_data(program_data'First + 1) := noun;
      initialised_data(program_data'First + 2) := verb;
      
      return initialised_data;
   end Initialise_Program;
   
   
   function Run_Operation(program_data: in out Int_Arr;
                          index: in out Natural) return Boolean is
      code : Opcode:=Opcode'Enum_Val(program_data(index));
   begin
      case code is
         when add =>
            program_data(program_data(index+3) + program_data'First) :=
              program_data(program_data(index+1) + program_data'First)
                + program_data(program_data(index+2) + program_data'First);
            index:= index + 4;
            return True;
         when multiply =>
            program_data(program_data(index+3) + program_data'First) :=
              program_data(program_data(index+1) + program_data'First)
                * program_data(program_data(index+2) + program_data'First);
            index:= index + 4;
            return True;
         when halt =>
            index:= index + 1;
            return False;
      end case;
   end Run_Operation;
   
   
   function Run_Program(program_data: in out Int_Arr) return Integer is
      should_continue : Boolean:= True;
      index : Natural:= program_data'First;
   begin
      while should_continue and index <= program_data'Last loop
         should_continue := Run_Operation(program_data, index);
      end loop;
      return program_data(program_data'First);
   end Run_Program;

end Intcode;
