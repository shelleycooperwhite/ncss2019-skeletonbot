import re
import random

TUTORS = ['Tim', 'Nicky', 'Kenni', 'Ben', 'Smerity']


# ---
# REGISTER THE STATES
# Connects our states (eg. 'LOCKED OUT') with our functions (eg. locked_out_on_enter_state)
# ---

# What to do when we enter a state
def on_enter_state(state, context):
  if state == 'NO QUERY':
    return no_query_on_enter_state(context)
  elif state == 'LOCKED OUT':
    return locked_out_on_enter_state(context)
  elif state == 'LOCKED OUT LOCATION':
    return locked_out_location_on_enter_state(context)
  # More states here
  # elif state == ...

# What to do when we receive input while in a state
def on_input(state, user_input, context):
  # First up, if they're trying to quit, then quit.
  if user_input == 'quit':
    return 'END', {}, 'Bye!'

  # Otherwise, check the state.
  if state == 'NO QUERY':
    return no_query_on_input(user_input, context)
  elif state == 'LOCKED OUT':
    return locked_out_on_input(user_input, context)
  elif state == 'LOCKED OUT LOCATION':
    return locked_out_location_on_input(user_input, context)
  # More states here
  # elif state == ...


# ---
# START STATE
# The big start state that knows where to send the user.
# ---

def no_query_on_enter_state(context):
  return 'I am Lockout helper bot. How can I help you?'

def no_query_on_input(user_input, context):
  # Check where they're locked out.
  match = re.match('I am locked out( in (?P<location>.*))?', user_input)
  if match:
    location = match.group('location')
    # If we got a location, go to the locked out + location state.
    if location:
      return 'LOCKED OUT LOCATION', {'location': location}, None
    # If no location, go to the locked out state.
    else:
      return 'LOCKED OUT', {}, None

  # If we didn't match any regex, go back to this start state and try again.
  else:
    return 'NO QUERY', {}, 'Sorry, I don\'t understand!'


# ---
# OTHER STATES
# ---

# TODO: Replace these states with your project's cool states

# LOCKED OUT state
def locked_out_on_enter_state(context):
  return 'Where are you locked out?'

def locked_out_on_input(user_input, context):
  # Store the full response text as the location.
  location = user_input
  return 'LOCKED OUT LOCATION', {'location': location}, None


# LOCKED OUT LOCATION state
def locked_out_location_on_enter_state(context):
  location = context['location']
  tutor = random.choice(TUTORS)
  return f'{tutor} will be at {location} right away!'

def locked_out_location_on_input(user_input, context):
  return 'END', {}, 'Bye!'


# --- More states go here! --- #
