with Array_Stuff; use Array_Stuff;

package Passwords is
 
   type Criteria_Function is access function(password: Integer) return Boolean;
   function Meets_Star_One_Criteria(password: Integer) return Boolean;
   
   function Count_Valid_Passwords(start, stop: Integer;
                                  criteria: Criteria_Function) return Integer;
   
private
   function Always_Increasing(password: Integer) return Boolean;
   function Repeated_Digit(password: Integer) return Boolean;
   

end Passwords;
