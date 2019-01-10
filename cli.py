from bot import on_enter_state, on_input

state = 'NO QUERY'
context = None

while state != 'END':
  output = on_enter_state(state, context)
  if output:
    print(output)

  user_input = input('> ')
  state, context, output = on_input(state, user_input, context)
  if output:
    print(output)
