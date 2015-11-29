#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print itl
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def BuildTheList(year,dict_name_rank):
  List_ = [year]
  sort_list_dict_name_rank_keys = sorted(dict_name_rank.keys())
  for each in sort_list_dict_name_rank_keys:
    List_.append(each+' '+dict_name_rank[each])
  return List_

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  dict_name_rank = {}
  year = ''
  f = open(filename,'rU')
  i = 0
  for line in f:
    i += 1
    # print i
    # print 'chec one: '+line
    match = re.search(r'<\w*\s\w*=.\w*.?>Popularity in (\d+)<.\w\d?>',line)
    if match:
      year = match.group(1)
      # print match.group()
      # print match.group(1)+', ',
      # break

    # print 'check two: '+line

    match_name_rank = re.search(r'<\w+\s\w*..\w+.?><td>(\d+)</td><td>(\w+)<\/td><td>(\w+)</td>',line)
    if match_name_rank:
      # print 'step three'
      dict_name_rank[str(match_name_rank.group(3))] = str(match_name_rank.group(1))
      dict_name_rank[str(match_name_rank.group(2))] = str(match_name_rank.group(1))
      # print match_name_rank.group(3)+' '+match_name_rank.group(1)+', ',

  f.close()
  # print dict_name_rank
  return BuildTheList(year,dict_name_rank)


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  if summary and args[0]:
    print 'step one'
    print extract_names(args[0])
  
if __name__ == '__main__':
  main()
