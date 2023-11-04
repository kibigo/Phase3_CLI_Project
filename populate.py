from main import Doctor, Patient, Nurse, Session, Ward
import datetime 
import click

@click.command()
@click.option('--name', prompt = 'Name', help ='Name of the doctor')
@click.option('--specialization', prompt = 'specialization', help = 'Doctor Specialization')

def add_to_doctors(name, specialization):
    sess = Session()

    new_entry = Doctor(name = name, specialization = specialization)
    sess.add(new_entry)
    

    click.echo(f'Data added: {name} {specialization}')

    sess.commit()
    sess.close()



@click.command()
@click.option('--name', prompt = 'Name', help = 'Name of the nurse')
@click.option('--shift', prompt = 'Shift', help = 'Nurse shift')

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
@click.option('--disease', prompt = 'Disease')
@click.option('--assigned_doctor', prompt = 'Assigned Doctor')
@click.option('--arrival_time')

def add_data_to_patients(name, arrival_time, disease, assigned_doctor):
    sess = Session()

    new_entry = Patient(name = name, arrival_time = format_date(), disease = disease, assigned_doctor = assigned_doctor)
    sess.add(new_entry)

    click.echo(f'Data added: Name: {name}, Disease: {disease}, Assigned Doctor: {assigned_doctor}')

    sess.commit()
    sess.close()

@click.command()
@click.option('--patient_id', prompt = 'Patient_id')
@click.option('--doctor_id', prompt = 'Doctor_id')
@click.option('--nurse_id', prompt = 'Nurse_id')

def add_data_to_wards(patient_id, doctor_id, nurse_id):
    sess = Session()

    new_entry = Ward(patient_id = patient_id, doctor_id=doctor_id, nurse_id = nurse_id)
    sess.add(new_entry)

    click.echo(f'Patient_id: {patient_id}, Doctor_id: {doctor_id}, Nurse_id: {nurse_id}')

    sess.commit()
    sess.close()

@click.group()

def cli():
    pass
    

cli.add_command(add_data_to_doctors)
cli.add_command(add_data_to_nurses)
cli.add_command(add_data_to_patients)
cli.add_command(add_data_to_wards)

if __name__ == '__main__':
    cli()
