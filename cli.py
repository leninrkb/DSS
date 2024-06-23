import click

@click.group()
def dss():
    pass

@dss.command()
@click.option('--criteria', default='1234', help='sort criteria')      
def sort(criteria:str):
    for c in criteria:
        print(c)






