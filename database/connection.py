from contextlib import contextmanager
import queries as q

@contextmanager
def get_cursor(connection):
    with connection:
        with connection.cursor() as cursor:
            yield cursor

def create_tables(connection):
    with get_cursor(connection) as cursor:
        cursor.execute(q.CREATE_ORGANIZATION)
        cursor.execute(q.CREATE_ORGANIZATION_TAG)
        cursor.execute(q.CREATE_ORGANIZATION_DEMOGRAPHIC)
        cursor.execute(q.CREATE_OPPORTUNITY)
        cursor.execute(q.CREATE_OPPORTUNITY_TYPE)
        cursor.execute(q.CREATE_OPPORTUNITY_DATE)
        cursor.execute(q.CREATE_USER)
        cursor.execute(q.CREATE_USER_TYPE)
        cursor.execute(q.CREATE_TAG)
        cursor.execute(q.CREATE_OPPORTUNITY_TAG)
        cursor.execute(q.CREATE_INTEREST)
        cursor.execute(q.CREATE_OPPORTUNITY_INTEREST)
        cursor.execute(q.CREATE_GRADE)
        cursor.execute(q.CREATE_OPPORTUNITY_GRADE)
        cursor.execute(q.CREATE_DEMOGRAPHIC)
        cursor.execute(q.CREATE_OPPORTUNITY_DEMOGRAPHIC)
        cursor.execute(q.CREATE_LIST)
        cursor.execute(q.CREATE_OPPORTUNITY_LIST)