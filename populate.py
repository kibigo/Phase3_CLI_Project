from main import Doctor, Patient, Nurse, Session, Ward, connector_table, engine
import datetime 
import click
import re


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

@click.command()
@click.option('--patient_id', prompt = 'Patient_id', help='Enter the patient id')
@click.option('--ward_id', prompt = 'Ward_id', help = 'Enter the ward where the patient is located')

def add_to_location(patient_id, ward_id):
    sess = Session()
    new_entry = connector_table.insert().values(patient_id=patient_id,ward_id=ward_id)
    
    conn = engine.connect()
    conn.execute(new_entry)

    click.echo('Added')

    sess.commit()
    sess.close()

#DELETING DATA FROM TABLE doctors

@click.command()
def delete_doctor():
    sess = Session()

    query = sess.query(Doctor).filter(Doctor.id == 2).first()
    
    if query:
        sess.delete(query)
        sess.commit()
        click.echo('Doctor deleted')

    else:
        click.echo('Doctor not found')

#Deleting an entire table



@click.group()

def cli():
    pass
    

cli.add_command(add_to_doctors)
cli.add_command(add_to_nurses)
cli.add_command(add_to_patients)
cli.add_command(add_to_wards)
cli.add_command(delete_doctor)
cli.add_command(add_to_location)

if __name__ == '__main__':
    cli()
