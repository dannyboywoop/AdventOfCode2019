with Array_Stuff;
use Array_Stuff;

package Intcode is
   
   function Run_Program(program_data: in out Int_Arr) return Integer;
   
   
   function Initialise_Program(program_data: Int_Arr; 
                                noun, verb: Integer) return Int_Arr;
private

   function Run_Operation(program_data: in out Int_Arr;
                          index: in out Natural) return Boolean;
   
   type Opcode is (add, multiply, halt);
   
   for Opcode use
     (add => 1,
      multiply => 2,
      halt => 99
     );

end Intcode;
