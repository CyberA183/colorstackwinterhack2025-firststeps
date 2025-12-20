# Table Queries
CREATE_OPPORTUNITY = """CREATE TABLE IF NOT EXISTS Opportunity (
    OpportunityID SERIAL PRIMARY KEY,
    Title TEXT NOT NULL,
    Description TEXT,
    Location TEXT,
    OrganizationID INTEGER,
    Website TEXT NOT NULL,
    Deadline TIMESTAMP NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    OpportunityType INTEGER NOT NULL,
    CreatedByUserID INTEGER,
    
    FOREIGN KEY (OrganizationID) REFERENCES Organization(OrganizationID),
    FOREIGN KEY (OpportunityType) REFERENCES OpportunityType(TypeID),
    FOREIGN KEY (CreatedByUserID) REFERENCES User(UserID));
    """
CREATE_OPPORTUNITY_DATE = """CREATE TABLE IF NOT EXISTS OpportunityDate (
    DateID SERIAL PRIMARY KEY,
    StartDate TIMESTAMP NOT NULL,
    EndDate TIMESTAMP NOT NULL,
    OpportunityID INTEGER NOT NULL,
    
    FOREIGN KEY (OpportunityID) REFERENCES Opportunity(OpportunityID));
    """
CREATE_OPPORTUNITY_TYPE = """CREATE TABLE IF NOT EXISTS OpportunityType (
    TypeID SERIAL PRIMARY KEY,
    TypeName TEXT NOT NULL);
    """

CREATE_TAG = """CREATE TABLE IF NOT EXISTS Tag (
    TagID SERIAL PRIMARY KEY,
    TagName TEXT NOT NULL);
    """
CREATE_OPPORTUNITY_TAG = """CREATE TABLE IF NOT EXISTS OpportunityTag (
    (OpportunityID, TagID) PRIMARY KEY,
    OpportunityID INTEGER NOT NULL,
    TagID INTEGER NOT NULL,
    
    FOREIGN KEY (OpportunityID) REFERENCES Opportunity(OpportunityID),
    FOREIGN KEY (TagID) REFERENCES Tag(TagID));
    """

CREATE_INTEREST = """CREATE TABLE IF NOT EXISTS Interest (
    InterestID SERIAL PRIMARY KEY,
    InterestName TEXT NOT NULL);
    """
CREATE_OPPORTUNITY_INTEREST = """CREATE TABLE IF NOT EXISTS OpportunityInterest (
    (OpportunityID, InterestID) PRIMARY KEY,
    InterestID INTEGER NOT NULL,
    OpportunityID INTEGER NOT NULL,
    
    FOREIGN KEY (InterestID) REFERENCES Interest(InterestID),
    FOREIGN KEY (OpportunityID) REFERENCES Opportunity(OpportunityID));
    """

CREATE_GRADE = """CREATE TABLE IF NOT EXISTS Grade (
    GradeID SERIAL PRIMARY KEY,
    GradeName TEXT NOT NULL);
    """
CREATE_OPPORTUNITY_GRADE = """CREATE TABLE IF NOT EXISTS OpportunityGrade (
    (OpportunityID, GradeID) PRIMARY KEY,
    GradeID INTEGER NOT NULL,
    OpportunityID INTEGER NOT NULL,
    
    FOREIGN KEY (GradeID) REFERENCES Grade(GradeID),
    FOREIGN KEY (OpportunityID) REFERENCES Opportunity(OpportunityID));
    """

CREATE_DEMOGRAPHIC = """CREATE TABLE IF NOT EXISTS Demographic (
    DemographicID SERIAL PRIMARY KEY,
    DemographicName TEXT NOT NULL);
    """
CREATE_OPPORTUNITY_DEMOGRAPHIC = """CREATE TABLE IF NOT EXISTS OpportunityDemographic (
    (OpportunityID, DemographicID) PRIMARY KEY,
    DemographicID INTEGER NOT NULL,
    OpportunityID INTEGER NOT NULL,
    
    FOREIGN KEY (DemographicID) REFERENCES Demographic(DemographicID),
    FOREIGN KEY (OpportunityID) REFERENCES Opportunity(OpportunityID));
    """

CREATE_LIST = """CREATE TABLE IF NOT EXISTS List (
    ListID SERIAL PRIMARY KEY,
    ListName TEXT NOT NULL,
    ListDescription TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CreatedByUserID INTEGER NOT NULL,
    
    FOREIGN KEY (CreatedByUserID) REFERENCES User(UserID));
    """
CREATE_OPPORTUNITY_LIST = """CREATE TABLE IF NOT EXISTS OpportunityList (
    (OpportunityID, ListID) PRIMARY KEY,
    ListID INTEGER NOT NULL,
    OpportunityID INTEGER NOT NULL,
    
    FOREIGN KEY (ListID) REFERENCES List(ListID),
    FOREIGN KEY (OpportunityID) REFERENCES Opportunity(OpportunityID));
    """

CREATE_USER = """CREATE TABLE IF NOT EXISTS User (
    UserID SERIAL PRIMARY KEY,
    UserName TEXT NOT NULL,
    DateOfBirth DATE NOT NULL,
    DemographicID INTEGER,
    UserType INTEGER NOT NULL,
    
    FOREIGN KEY (DemographicID) REFERENCES Demographic(DemographicID),
    FOREIGN KEY (UserType) REFERENCES User(UserType));
    """
CREATE_USER_TYPE = """CREATE TABLE IF NOT EXISTS UserType (
    UserTyeID SERIAL PRIMARY KEY,
    TypeName TEXT NOT NULL);"""

CREATE_ORGANIZATION = """CREATE TABLE IF NOT EXISTS Organization (
    OrganizationID SERIAL PRIMARY KEY,
    OrganizationName TEXT NOT NULL,
    HeadquarterLocation TEXT NOT NULL,
    Website TEXT NOT NULL);
    """
CREATE_ORGANIZATION_TAG = """CREATE TABLE IF NOT EXISTS OrganizationTag (
    (OrganizationID, TagID) PRIMARY KEY,
    OrganizationID INTEGER NOT NULL,
    TagID INTEGER NOT NULL,
    
    FOREIGN KEY (TagID) REFERENCES Tag(TagID),
    FOREIGN KEY (OrganizationID) REFERENCES Organization(OrganizationID));
    """
CREATE_ORGANIZATION_DEMOGRAPHIC = """CREATE TABLE IF NOT EXISTS OrganizationDemographic (
    (OrganizationID, DemographicID) PRIMARY KEY,
    OrganizationID INTEGER NOT NULL,
    DemographicID INTEGER NOT NULL,
    
    FOREIGN KEY (OrganizationID) REFERENCES Organization(OrganizationID),
    FOREIGN KEY (DemographicID) REFERENCES Demographic(DemographicID));
    """

