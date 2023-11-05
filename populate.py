from main import Doctor, Patient, Nurse, Session, Ward, engine
import datetime 
import click
import re
from sqlalchemy import inspect


def verify_email(email):
    pattern = "^[a-z A-Z 0-9]+@[a-z A-Z]+\.[a-z A-Z]{2,3}$"
    if re.search(pattern, email):
        return email
    else:
        print("Email is not valid")

@click.command()
@click.option('--name', prompt = 'Name', help ='Name of the doctor')
@click.option('--specialization', prompt = 'specialization', help = 'Doctor Specialization')
@click.option('--email', prompt = 'Email', help = 'Enter the email of the doctor')

def add_to_doctors(name, specialization, email):
    sess = Session()

    new_entry = Doctor(name = name, specialization = specialization, email= verify_email(email))
    sess.add(new_entry)
    

    click.echo(f'Data added: {name} {specialization}')

    sess.commit()
    sess.close()


NURSES_SHIFTS = ['Day', 'NIght']

@click.command()
@click.option('--name', prompt = 'Name', help = 'Name of the nurse')
@click.option('--shift', prompt = 'Shift', type=click.Choice(NURSES_SHIFTS), help = 'Nurse shift')

def add_to_nurses(name, shift):
    
    sess = Session()

    new_entry = Nurse(name = name, shift = shift)
    sess.add(new_entry)

    click.echo(f'Data added: Name: {name}, Shift: {shift}')

    sess.commit()
    sess.close()



def format_date():
    arrival_time = datetime.datetime.now()
    formatted_time = arrival_time.strftime('%y/%m/%d %H:%M')
    return formatted_time

@click.command()
@click.option('--name', prompt = 'Name')
@click.option('--assigned_doctor', prompt = 'Assigned Doctor')
@click.option('--arrival_time')
@click.option('--ward', prompt ='Ward')

def add_to_patients(name, arrival_time, assigned_doctor, ward):
    sess = Session()

    new_entry = Patient(name = name, arrival_time = format_date(), assigned_doctor = assigned_doctor, ward = ward)
    sess.add(new_entry)

    click.echo(f'Data added: Name: {name}, Assigned Doctor: {assigned_doctor}, Ward: {ward}')

    sess.commit()
    sess.close()

@click.command()
@click.option('--name', prompt = 'Name')

def add_to_wards(name):
    sess = Session()

    new_entry = Ward(name = name)
    sess.add(new_entry)

    click.echo(f'Name: {name}')

    sess.commit()
    sess.close()

#VIEWING DATA ADDED IN TABLES
@click.command()
@click.option('--table', prompt = 'Table Name', help='Name of the table to view data')


def view_data(table):
    sess = Session()

    table_mapping = {
        'doctors': Doctor,
        'nurses': Nurse,
        'patients':Patient,
        'wards': Ward
    }

    if table not in table_mapping:
        click.echo(f'Table {table} not found')

    else:
        target_table = table_mapping[table]

        query = sess.query(target_table).all()

        if query:
            click.echo(f'Data in Table {table}')

            for item in query:
                click.echo(item)

        else:
            click.echo(f'No data found in {table}')

        



#DELETING DATA FROM TABLE doctors

@click.command()
@click.option('--table', prompt ='Table Name', help='Name of the table to delete data from')
@click.option('--id', prompt='Data ID', type= int, help='ID of the data to delete')

def delete(table, id):
    sess = Session()
    
    table_mapping = {
        'doctors': Doctor,
        'nurses': Nurse,
        'patients':Patient,
        'wards': Ward
        }

    if table not in table_mapping:
        click.echo(f'Table {table} not found')

    else:
        target_table = table_mapping[table]

        query = sess.query(target_table).filter(target_table.id == id).first()
    
        if query:
            sess.delete(query)
            sess.commit()
            click.echo(f'Data in {table} with ID {id} deleted')

        else:
            click.echo(f'Data in {table} with ID {id} not found')




@click.group()

def cli():
    pass
    

cli.add_command(add_to_doctors)
cli.add_command(add_to_nurses)
cli.add_command(add_to_patients)
cli.add_command(add_to_wards)
cli.add_command(delete)
cli.add_command(view_data)


if __name__ == '__main__':
    cli()
