package body Passwords is 
   
   function Always_Increasing(password: Integer) return Boolean is
      str_password: String:= Integer'Image(password);
      prev_digit: Character:='0';
      digit: Character;
   begin
      for i in str_password'First+1..str_password'Last loop
         digit:= str_password(i);
         if digit < prev_digit then
            return False;
         end if;
         prev_digit:= digit;
      end loop;
      return True;
   end Always_Increasing;
   
   function Repeated_Digit(password: Integer) return Boolean is
      str_password: String:= Integer'Image(password);
      prev_digit: Character:='-';
      digit: Character;
   begin
      for i in str_password'First+1..str_password'Last loop
         digit:= str_password(i);
         if digit = prev_digit then
            return True;
         end if;
         prev_digit:= digit;
      end loop;
      return False;
   end Repeated_Digit;
   
   function Double_Digit(password: Integer) return Boolean is
      str_password: String:= Integer'Image(password);
      prev_digit: Character:='-';
      digit: Character;
      count: Integer:= 0;
   begin
      for i in str_password'First+1..str_password'Last loop
         digit:= str_password(i);
         if digit = prev_digit then
            count:= count+1;
         elsif count = 2 then
            return True;
         else
            count:= 1;
         end if;
         prev_digit:= digit;
      end loop;
      if count = 2 then
         return True;
      end if;
      return False;
   end Double_Digit;
   
   function Meets_Star_One_Criteria(password: Integer) return Boolean is 
   begin
      return Always_Increasing(password) and Repeated_Digit(password);
   end Meets_Star_One_Criteria;
   
   function Meets_Star_Two_Criteria(password: Integer) return Boolean is 
   begin
      return Always_Increasing(password) and Double_Digit(password);
   end Meets_Star_Two_Criteria;
   
   function Count_Valid_Passwords(start, stop: Integer;
                                  criteria: Criteria_Function) return Integer is
      count: Integer:=0;
   begin
      for i in start..stop loop
         if criteria(i) then
            count := count + 1;
         end if;
      end loop;
      return count;
   end Count_Valid_Passwords;

end Passwords;
