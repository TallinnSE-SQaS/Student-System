import os
from typing import Dict

environments = {
    'prod': {
        'db_name': 'student-system.db'
    },
    'dev': {
        'db_name': 'student-system.dev.db'
    },
    'test': {
        'db_name': 'student-system.test.db'
    },
}


def get_environment() -> Dict[str, str]:
    return environments[os.getenv('ENV', 'dev')]
