type t =
  | String(string)
  | Int(int)
  | List(list(string));

let toString =
  fun
  | String(s) => s
  | Int(i) => Int.toString(i)
  | List(items) => items->List.toArray->Js.Array2.joinWith("");
