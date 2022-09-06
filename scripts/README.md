# Building dataset

Requirements:

- Python3

To build the dataset, download the JSON file from the UN Comtrade data extraction API. Then execute the conversion script as follows.

```bash
`scripts/convert.py -i <input filename> -o <output filename>`

# for example:
# scripts/convert.py -i classificationH6.json -o hs2022.csv
```
