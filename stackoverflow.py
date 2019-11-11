from google.cloud import bigquery

def get_client_dataset():
	client = bigquery.Client()
	ref = client.dataset('stackoverflow', project='bigquery-public-data')
	dataset = client.get_dataset(ref)
	return client, dataset

def add_rows(client, dataset, table_name, rows):
	table = client.get_table(dataset.table(table_name))
	for r in client.list_rows(table):
		rows.append(r)

if __name__ == '__main__':
	main()
