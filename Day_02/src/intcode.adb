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
   
   function Find_Start_Vals(program_data: Int_Arr; 
                            desired_result: Integer) return Integer is
      data: Int_Arr(program_data'Range);
   begin
      for i in 0..99 loop
         for j in 0..99 loop
            data := Initialise_Program(program_data, i, j);
            if Run_Program(data) = desired_result then
               return 100*i + j;
            end if;
         end loop;
      end loop;
      return -1;
   end Find_Start_Vals;

end Intcode;
