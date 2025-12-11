'''
Plot Data. This program takes in a file and through class CreatingGraph, it build graph with the corresponding data which is found in the file. Alisa Dzhoha. 12/11/2025
'''

from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime



class CreatingGraph():
  '''
  This class takes in file and based on the data creates graph
  '''
   
  def __init__(self, file):
    '''
    Constuctor method
    '''
    self.file = file
    self.dates = []
    self.oh = []

  def read_data(self):
    '''
    This method reads file and formats data which will be shown on the graph
    '''
    path = self.file
    lines = path.read_text(encoding='utf-8').splitlines()
    reader = csv.reader(lines)
    header_row = next(reader)

    for index, col_title in enumerate(header_row):
        print(index, col_title)

    for row in reader:
      remWhiteSpace_date = row[0].strip()
      remWhiteSpace_oh = row[1].strip()
      date = datetime.strptime(remWhiteSpace_date, '%Y-%m-%d')
      oh =  float(remWhiteSpace_oh)
      self.dates.append(date)
      self.oh.append(oh)
        


  def plot_graph(self, xlabel, ylabel, title):
    '''
    This method takes formatted data and passed parameters to build the graph
    '''

    plt.plot(self.dates, self.oh)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()


if __name__ == "__main__":
    graph = CreatingGraph(Path("OHUR.csv"))
    graph.read_data()
    graph.plot_graph(xlabel='Date', ylabel='Unemp Rate', title = 'Ohio Unemployment(by Month): 1976 - 2022')