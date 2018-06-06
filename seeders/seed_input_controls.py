from api.models.input_control import InputControl
import uuid


def seed_inputs_controls():
    """Seed Input controls to the database"""
    
    field_controls = ['text', 'text area', 'file', 'radio', 'checkbox']

    for field in field_controls:
        input_control = InputControl(id=str(uuid.uuid4()), name=field)
        input_control.save()