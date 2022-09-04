#!/usr/bin/env python3

import argparse, json

def section_for(hscode):
  chapter = int(hscode[:2])
  if chapter <= 5:
    return "I"
  elif chapter <= 14:
    return "II"
  elif chapter == 15:
    return "III"
  elif chapter <= 24:
    return "IV"
  elif chapter <= 27:
    return "V"
  elif chapter <= 38:
    return "VI"
  elif chapter <= 40:
    return "VII"
  elif chapter <= 43:
    return "VIII"
  elif chapter <= 46:
    return "IX"
  elif chapter <= 49:
    return "X"
  elif chapter <= 63:
    return "XI"
  elif chapter <= 67:
    return "XII"
  elif chapter <= 70:
    return "XIII"
  elif chapter == 71:
    return "XIV"
  elif chapter <= 83:
    return "XV"
  elif chapter <= 85:
    return "XVI"
  elif chapter <= 89:
    return "XVII"
  elif chapter <= 92:
    return "XVIII"
  elif chapter == 93:
    return "XIX"
  elif chapter <= 96:
    return "XX"
  elif chapter == 97:
    return "XXI"
  else:
    return "TOTAL"

def convert(input_filename, output_filename):
  input = open(input_filename, "r")
  data = json.loads(input.read())

  output = open(output_filename, "w")

  output.write("section,hscode,description,parent,level\n")

  for i in data["results"]:
    hscode = i["id"]
    if not hscode.isnumeric() or hscode == "TOTAL":
      continue

    description = i["text"].split(" - ")[-1]
    if "," in description:
      description = '"' + description + '"'

    section = section_for(hscode)

    parent = i["parent"]

    level = len(hscode)

    output.write(f"{section},{hscode},{description},{parent},{level}\n")

  input.close()
  output.close()

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Convert UN Comtrade HS Code data")
  parser.add_argument("-i", "--input", required=True)
  parser.add_argument("-o", "--output", required=True)
  args = parser.parse_args()

  convert(args.input, args.output)