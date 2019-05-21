# Build script example

Run the following command to see the output of the python scripts:

    python template.py

Which will show:

    resources:
    - name: vm
      properties:
        machineType: zones/us-east-2/machineTypes/n1-ultramem-40
        zone: us-east-2
      type: compute.v1.instance

Now, change (or delete) the values displayed in `config/env.py`, which are set as overrides from `config/generic.py`.

To see the result of the changes, run:

    python template.py

Which will now show:

    resources:
    - name: vm
      properties:
        machineType: zones/us-east-1/machineTypes/n1-standard-4
        zone: us-east-1
      type: compute.v1.instance

Here we can see the default `config/generic.py` configuration being used, since no matches were found for the environment-specific values.

