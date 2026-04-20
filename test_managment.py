import pytest
import datetime
from employee import Employee
from relations_manager import RelationsManager
from employee_manager import EmployeeManager

#  ADAT ELLENŐRZŐ TESZTEK

def test_1_john_doe_adatai():
    rm = RelationsManager()
    john = None
    for e in rm.get_all_employees():
        if e.id == 1: john = e
    assert john.first_name == "John"
    assert john.last_name == "Doe"
    assert john.birth_date == datetime.date(1970, 1, 31)

def test_2_myrta_torkelson_fizetese():
    rm = RelationsManager()
    myrta = None
    for e in rm.get_all_employees():
        if e.id == 2: myrta = e

    assert myrta.base_salary == 1000

def test_3_gretchen_watford_adatai():
    rm = RelationsManager()
    gretchen = None
    for e in rm.get_all_employees():
        if e.id == 4: gretchen = e
    assert gretchen.first_name == "Gretchen"
    assert gretchen.last_name == "Watford"

#  VEZETŐI ÉS CSAPAT TESZTEK

def test_4_john_doe_vezeto_e():
    rm = RelationsManager()
    john = None
    for e in rm.get_all_employees():
        if e.id == 1: john = e
    assert rm.is_leader(john) == True

def test_5_scotty_bomba_nem_vezeto():
    rm = RelationsManager()
    scotty = None
    for e in rm.get_all_employees():
        if e.id == 6: scotty = e
    assert rm.is_leader(scotty) == False

def test_6_john_doe_csapat_merete():
    rm = RelationsManager()
    john = None
    for e in rm.get_all_employees():
        if e.id == 1: john = e
    csapat = rm.get_team_members(john)
    assert len(csapat) == 2

def test_7_gretchen_csapat_tagjai():
    rm = RelationsManager()
    gretchen = None
    for e in rm.get_all_employees():
        if e.id == 4: gretchen = e
    csapat = rm.get_team_members(gretchen)
    assert 5 in csapat
    assert 6 in csapat

# --- BÉRSZÁMÍTÁSI TESZTEK ---

def test_8_sima_dolgozo_fizetes_szamitas():
    rm = RelationsManager()
    em = EmployeeManager(rm)

    teszt_e = Employee(id=99, first_name="Teszt", last_name="Elek",
                      base_salary=1000, birth_date=datetime.date(1980,1,1),
                      hire_date=datetime.date(2010, 1, 1))
    eredmeny = em.calculate_salary(teszt_e)
    evek = datetime.date.today().year - 2010
    assert eredmeny == 1000 + (evek * 100)

def test_9_vezeto_bonusz_szamitas():
    rm = RelationsManager()
    em = EmployeeManager(rm)
    john = None
    for e in rm.get_all_employees():
        if e.id == 1: john = e
    eredmeny = em.calculate_salary(john)
    evek = datetime.date.today().year - 1990
    elvart = 3000 + (evek * 100) + (2 * 200)
    assert eredmeny == elvart

# NEGATÍV ÉS LOGIKAI TESZTEK

def test_10_nem_letezo_dolgozo_keresese():
    rm = RelationsManager()
    szellem = None
    for e in rm.get_all_employees():
        if e.first_name == "Batman":
            szellem = e
    assert szellem is None

def test_11_ures_csapat_ha_nem_vezeto():
    rm = RelationsManager()
    myrta = None
    for e in rm.get_all_employees():
        if e.id == 2: myrta = e
    eredmeny = rm.get_team_members(myrta)
    assert eredmeny is None