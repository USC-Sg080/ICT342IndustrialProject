import dataset
import dataset

client = dataset.api_client()
project = client.get_project(dataset.default_project_key())
project_variables = dataset.get_custom_variables()
csv_dataset_name = 'NEW_DATASET_NAME'


	csv_dataset = project.get_dataset(csv_dataset_name)
	csv_dataset.clear()
except:
	
	params = {'Dataset': 'DATASET', 'CLIN DSET NAME', 'CLIN DSET DESCR',
                  'PK','PATIENT','DOB','WEIGHT','HEIGHT','COMMENT','PK.ORIGIN'

        format_params = {'separator': '\t', 'style': 'unix', 'compress': ''}

	csv_dataset = project.create_dataset(csv_dataset_name, type='Filesystem',
        params=params,
        formatType='csv', formatParams=format_params)

	
	ds_def = csv_dataset.get_definition()
	ds_def['managed'] = True
	csv_dataset.set_definition(ds_def)


csv_dataset.set_schema({'columns': csv_dku_schema_columns})


csv_dataset.clear()
csv_dataset.delete()
