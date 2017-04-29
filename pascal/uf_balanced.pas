program uf;

function find(var parents : array of int64;
                  node    : int64): int64;
begin
   while node <> parents[node] do
      node := parents[node];
   find := node
end;

procedure union(var parents : array of int64;
                var size    : array of int64;
                    a       : int64;
                    b       : int64);
var
   root_a : int64;
   root_b : int64;
begin
   root_a := find(parents, a);
   root_b := find(parents, b);
   if root_a <> root_b then
      if size[root_a] < size[root_b] then begin
         parents[root_a] := root_b;
         size[root_b] := size[root_b] + size[root_a]
      end else begin
         parents[root_b] := root_a;
         size[root_a] := size[root_a] + size[root_b]
      end
end;

var
   V       : int64; { number of vertices }
   E       : int64; { number of edges }
   Q       : int64; { number of queries }
   parents : array of int64;
   size    : array of int64; { size of tree containing i }
   a, b    : int64; { two lambda nodes }
   i       : int64;

begin
   {
   Read the number of vertices and initialize
   the adjacency list (i.e., set all the neighbors
   to the empty list.
   }
   read(V);
   setlength(parents, V);
   setlength(size, V);
   for i := 0 to V - 1 do begin
      parents[i] := i;
      size[i] := i
   end;

   {
   Read the number of edges and update the adj array.
   }
   read(E);
   for i := 1 to E do begin
      read(a, b);
      union(parents, size, a, b);
   end;


   read(Q);
   for i := 1 to Q do begin
      read(a);
      read(b);
      if find(parents, a) = find(parents, b) then
         writeln('yes')
      else
         writeln('no')
   end
end.
