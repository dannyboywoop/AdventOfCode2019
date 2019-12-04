with Ada.Strings.Unbounded, Array_Stuff;
use Ada.strings.Unbounded, Array_Stuff;

package String_Stuff is

   function Split(input: Unbounded_String; delim: String) return Str_Arr;

end String_Stuff;
