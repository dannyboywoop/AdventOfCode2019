with Passwords; use Passwords;
with Ada.Text_IO; use Ada.Text_IO;

procedure Main is
   star_one: Integer;
   start: Integer:=172851;
   stop: Integer:=675869;
begin
   star_one := Count_Valid_Passwords(start, stop,
                                     Meets_Star_One_Criteria'Access);
   Put_Line("Star one: "&star_one'Image);
end Main;
