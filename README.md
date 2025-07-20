# ICT Inventory Management System

A Django-based inventory management system for tracking ICT equipment and maintenance.

## Features

- Equipment Management:
  - Add, edit, and delete equipment
  - Track equipment details (serial numbers, asset tags, categories)
  - Assign equipment to users
  - Track purchase prices and warranty information

- Maintenance Tracking:
  - Record maintenance activities
  - Track maintenance costs
  - Record maintenance descriptions
  - Track who performed maintenance

- Repair Management:
  - Track repair activities
  - Record repair descriptions and costs
  - Track completion status
  - Record who performed repairs

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd inventory_prj
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Make and apply migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser (optional):
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

## Project Structure

```
inventory_prj/
├── inventory/           # Main application
│   ├── migrations/     # Database migrations
│   ├── static/         # Static files
│   ├── templates/      # HTML templates
│   └── __init__.py
├── manage.py
└── requirements.txt
```

## Database Models

- Equipment: Tracks ICT equipment details
- MaintenanceRecord: Tracks maintenance activities
- RepairRecord: Tracks repair activities

## Requirements

- Python 3.8+
- Django 5.2.4
- Other dependencies listed in requirements.txt

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License
