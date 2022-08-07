import requests
import pandas as pd

class lista_cep:

    def __init__(self) -> None:
        self._url = "https://cep.awesomeapi.com.br/json/"
        self._dados = {
            'Nome': ['Vitor', 'Justin', 'Kanye'],
            'Id': [1, 2, 3],
            'CEP': ['01002020', '01451000', '04786071']
        }

    def data(self):
        return pd.DataFrame(data=self._dados)
    
    def empty_data(self):
        return pd.DataFrame()

    def fill_empty_data(self):
        df = self.data()
        df_vazio = self.empty_data()

        for row in df.itertuples():
            rqst = requests.get(f'{self._url}{row.CEP}').json()
            rqst_df = pd.json_normalize(rqst)

            df_vazio = df_vazio.append(rqst_df)

        return df_vazio

    def merge_data(self):
        df = self.data()
        df_vazio = self.fill_empty_data()

        df_final = df.merge(
            df_vazio[df_vazio.columns[1:]],
            how='left',
            left_on='CEP',
            right_on=df_vazio['cep'],
        )

        return df_final.head()

if __name__ == "__main__":
    print(lista_cep().merge_data())