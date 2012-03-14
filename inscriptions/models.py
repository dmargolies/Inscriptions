from django.db import models
class Trade(models.Model):
    trade_name = models.CharField(max_length = 200)
    comment = models.TextField(null=True, blank=True) #in case she needs more space than 200
    def __unicode__(self):
        return self.trade_name
class Deity(models.Model):
    deity_name = models.CharField(max_length=200)
    comment = models.TextField(null=True, blank=True)
    def __unicode__(self):
        return self.deity_name
class AssociativeUnit(models.Model):
    unit_name = models.CharField(max_length=200)
    comment = models.TextField(null=True, blank=True)
    def __unicode__(self):
        return self.unit_name        
class ImperialHouse(models.Model):
    house_name = models.CharField(max_length=200)
    comment = models.TextField(null=True, blank=True)
    def __unicode__(self):
        return self.house_name
        
class Person(models.Model):
    name = models.CharField(max_length = 200)
    praenomen = models.CharField(max_length = 200, null=True, blank=True)
    nomen = models.CharField(max_length = 200, null=True, blank=True)
    cognoment = models.CharField(max_length = 200, null=True, blank=True) 
    supernomen = models.CharField(max_length = 200, null=True, blank=True)
    filiation = models.CharField(max_length = 200, null=True, blank=True)
    tribus = models.CharField(max_length = 200, null=True, blank=True)
    origo = models.CharField(max_length = 200, null=True, blank=True)
    other = models.CharField(max_length = 200, null=True, blank=True) #maybe textfield?
    gender = models.CharField(max_length = 20, null=True, blank=True) #could also use a list like in tut(m/f)
    relations = models.CharField(max_length = 20, null=True, blank=True)
    status = models.CharField(max_length = 20, null=True, blank=True)
    official_positions = models.CharField(max_length = 200, null=True, blank=True)
    occupation = models.CharField(max_length = 200, null=True, blank=True)
    lifetime_years = models.CharField(max_length = 20, null=True, blank=True) #will this be an integer 
    lifetime_months = models.IntegerField(null=True, blank=True)
    lifetime_days = models.IntegerField(null=True, blank=True)
    lifetime_hours = models.IntegerField(null=True, blank=True)
    def __unicode__(self):
        return self.name

class Inscription(models.Model):
    hd_number = models.CharField(max_length = 10, null=True, blank=True) #could just be 8, **make unique**
    tm_number = models.CharField(max_length = 10, null=True, blank=True) #did not actually find any tm numbers(?)
    province  = models.CharField(max_length = 200, null=True, blank=True)
    modern_country = models.CharField(max_length = 200, null=True, blank=True) #too big?
    find_spot_ancient_name = models.CharField(max_length = 200, null=True, blank=True)
    find_spot_modern_name = models.CharField(max_length = 200, null=True, blank=True)
    region = models.CharField(max_length = 200, null=True, blank=True)
    year_of_find = models.IntegerField(null=True, blank=True)
    find_spot = models.CharField(max_length = 200, null=True, blank=True)
    present_location = models.CharField(max_length = 200, null=True, blank=True)
    state_of_preservation = models.CharField(max_length = 200, null=True, blank=True)
    decoration = models.CharField(max_length = 200, null=True, blank=True)
    inscription_type = models.CharField(max_length = 200, null=True, blank=True)
    inscription_bearer = models.CharField(max_length = 200, null=True, blank=True)
    field = models.CharField(max_length = 200, null=True, blank=True)
    material = models.CharField(max_length = 200, null=True, blank=True)
    height = models.DecimalField(max_digits = 7, decimal_places = 2, null=True, blank=True)
    width = models.DecimalField(max_digits = 7, decimal_places = 2, null=True, blank=True)
    depth = models.DecimalField(max_digits = 7, decimal_places = 2, null=True, blank=True)
    height_i_field = models.DecimalField(max_digits = 7, decimal_places = 2, null=True, blank=True)
    width_i_field = models.DecimalField(max_digits = 7, decimal_places = 2, null=True, blank=True)
    letters_size = models.CharField(max_length = 200, null=True, blank=True)
    ligature = models.CharField(max_length = 200, null=True, blank=True)
    meter = models.CharField(max_length = 200, null=True, blank=True)
    language = models.CharField(max_length = 200, null=True, blank=True)
    date_day = models.CharField(max_length = 20, null=True, blank=True) #integer?
    date_month = models.CharField(max_length = 20, null=True, blank=True) #integer?
    date_year = models.CharField(max_length = 40, null=True, blank=True) #not ever sure what the german means
    date_specific = models.CharField(max_length = 40, null=True, blank=True) #english is y/n, german is longer words, w/ opposite meaning?
    sel_history = models.CharField(max_length = 200, null=True, blank=True) #should this be a text field, legal was mispelled leagal
    religion = models.CharField(max_length = 200, null=True, blank=True)
    communal_groups = models.CharField(max_length = 200, null=True, blank=True)
    geography = models.CharField(max_length = 200, null=True, blank=True)
    political_communities = models.CharField(max_length = 200, null=True, blank=True) 
    military = models.CharField(max_length = 200, null=True, blank=True)
    status_EDH_version = models.CharField(max_length = 200, null=True, blank=True)
    responsible_individual = models.CharField(max_length = 200, null=True, blank=True)
    last_update = models.DateField(null=True, blank=True)
    palaeography_longa = models.CharField(max_length = 200, null=True, blank=True)
    palaeography_apica_ornata = models.CharField(max_length = 200, null=True, blank=True)
    palaeography_parva = models.CharField(max_length = 200, null=True, blank=True)
    palaeography_inserta = models.CharField(max_length = 200, null=True, blank=True)
    writing_type = models.CharField(max_length = 200, null=True, blank=True)
    punctuation = models.CharField(max_length = 200, null=True, blank=True) 
    literature = models.TextField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    connections = models.TextField(null=True, blank=True)
    
    #persons
    persons = models.ManyToManyField(Person, null=True, blank=True)
    
    #a,b-text just fields
    a_text = models.TextField(null=True, blank=True)
    b_text = models.TextField(null=True, blank=True)
    
    #alphabetical list of words -- why bother making this a list??
    words = models.TextField(null=True, blank=True)
    
    #other many-many fields
    trades = models.ManyToManyField(Trade, null=True, blank=True)
    deities = models.ManyToManyField(Deity, null=True, blank=True)
    associativeUnits = models.ManyToManyField(AssociativeUnit, null=True, blank=True)
    imperialHouses = models.ManyToManyField(ImperialHouse, null=True, blank=True)
    
    #additional fields
    translation = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.hd_number + " " + self.inscription_type
