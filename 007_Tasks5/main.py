import pandas as pd
import random as rand


def task1() -> None:
    row_count = 5
    column_count = 10
    population = [x / 100000. for x in range(0, 100000)]
    dataframe = pd.DataFrame([rand.choices(population, k=column_count) for _ in range(row_count)])
    means = dataframe.where(cond=lambda x: x > 0.3, axis='rows').mean()
    print(means)


task1()
