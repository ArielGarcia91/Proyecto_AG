import typing

# --- CONSTANTS & CONFIGURATION ---

LEVELS = ["Educación Inicial", "Educación Primaria", "Educación Secundaria"]

MODALITIES = [
    "Preescolar comunitario", "preescolar formal", 
    "primaria multigrado", "primaria regular", 
    "Secundaria Regular", "Secundaria a Distancia en el campo", 
    "Secundaria de Jóvenes y Adultos"
]

SHIFTS = ["Matutino", "Vespertino", "Sabatino"]

# Allowed Grades mapping per Level
LEVEL_GRADES = {
    "Educación Inicial": ["I Nivel", "II nivel", "III nivel"],
    "Educación Primaria": ["primero", "segundo", "tercero", "cuarto", "quinto", "sexto"],
    "Educación Secundaria": ["séptimo", "octavo", "noveno", "decimo", "undécimo"]
}

# Grading Scales per Level
GRADING_SCALES = {
    "Educación Inicial": {"AA", "AP", "NE"},
    "Educación Primaria": {"AA", "AS", "AF", "AI"},
    "Educación Secundaria": None  # Numeric scale (typically 0-100) or customized scale can be defined here
}

# Subjects mapped per Level
LEVEL_SUBJECTS = {
    "Educación Inicial": [],  # Usually evaluation is global or generic criteria
    "Educación Primaria": [
        "LENGUA Y LITERATURA", "MATEMÁTICA", "ESTUDIOS SOCIALES", 
        "CIENCIAS NATURALES", "APRENDER EMPRENDER Y PROSPERAR", 
        "DERECHO Y DIGNIDAD DE LAS MUJERES", "CRECIENDO EN VALORES", 
        "TALLERES DE ARTE Y CULTURA", "EDUCACIÓN FÍSICA Y PRÁCTICA DEPORTIVA", 
        "INGLÉS", "CONOCIENDO MI MUNDO"
    ],
    "Educación Secundaria": [
        "LENGUA Y LITERATURA", "MATEMÁTICA", "CIENCIAS SOCIALES", 
        "CIENCIAS NATURALES", "APRENDER EMPRENDER Y PROSPERAR", 
        "DERECHO Y DIGNIDAD DE LAS MUJERES", "CRECIENDO EN VALORES", 
        "TALLERES DE ARTE Y CULTURA", "EDUCACIÓN FÍSICA Y PRÁCTICA DEPORTIVA", 
        "INGLÉS", "FISICA", "QUIMICA", "BIOLOGÍA", "SOCIOLOGÍA", 
        "FILOSOFIA", "VOCACIÓN PRODUCTIVA"
    ]
}

GRADING_PERIODS = ["I corte", "II corte", "III corte", "IV corte", "Final"]

# --- DATA MODEL & CLASSES ---

class Teacher:
    def __init__(self, teacher_id: str, name: str):
        self.teacher_id = teacher_id
        self.name = name
        # A teacher can be assigned to one or multiple grade levels
        self.assigned_grades: typing.List[str] = []

    def assign_grade(self, grade: str):
        self.assigned_grades.append(grade)


class Student:
    def __init__(self, first_names: str, last_names: str, grade: str, personal_code: typing.Optional[str] = None):
        self.first_names = first_names
        self.last_names = last_names
        self.personal_code = personal_code
        self.grade = grade
        # Storage for keeping student's grades
        # Relationship structure: { subject: { period: score_or_grade } }
        self.academic_record: typing.Dict[str, typing.Dict[str, typing.Union[str, float]]] = {}

    def initialize_subject_records(self, subjects: typing.List[str]):
        """Pre-populates the 5 standard grading periods for given subjects"""
        for subject in subjects:
            self.academic_record[subject] = {period: None for period in GRADING_PERIODS}


class Group:
    """Represents a specific classroom cohort offering a level, modality, shift, and grade."""
    def __init__(self, level: str, modality: str, shift: str, grade: str):
        # Validation constraints
        if level not in LEVELS:
            raise ValueError(f"Invalid level: {level}")
        if modality not in MODALITIES:
            raise ValueError(f"Invalid modality: {modality}")
        if shift not in SHIFTS:
            raise ValueError(f"Invalid shift: {shift}")
        if grade not in LEVEL_GRADES[level]:
            raise ValueError(f"Grade '{grade}' is not valid for level '{level}'")

        self.level = level
        self.modality = modality
        self.shift = shift
        self.grade = grade
        self.students: typing.List[Student] = []
        self.teachers: typing.List[Teacher] = []

    def add_student(self, student: Student):
        student.initialize_subject_records(LEVEL_SUBJECTS.get(self.level, []))
        self.students.append(student)

    def assign_teacher(self, teacher: Teacher):
        if self.grade not in teacher.assigned_grades:
            teacher.assign_grade(self.grade)
        self.teachers.append(teacher)


class EducationalCenter:
    def __init__(self, unique_code: str, standard_code: str, name: str):
        self.unique_code = unique_code
        self.standard_code = standard_code
        self.name = name
        self.groups: typing.List[Group] = []

    def create_group(self, level: str, modality: str, shift: str, grade: str) -> Group:
        new_group = Group(level, modality, shift, grade)
        self.groups.append(new_group)
        return new_group


class AcademicPerformanceSystem:
    """Orchestrator for managing the academic centers and enforcing performance validations."""
    def __init__(self):
        self.centers: typing.Dict[str, EducationalCenter] = {}

    def register_center(self, unique_code: str, standard_code: str, name: str) -> EducationalCenter:
        if unique_code in self.centers:
            raise ValueError("Educational Center with this unique code already exists.")
        center = EducationalCenter(unique_code, standard_code, name)
        self.centers[unique_code] = center
        return center

    def enroll_student_to_group(self, center_code: str, group: Group, student: Student):
        if center_code not in self.centers:
            raise ValueError("Educational Center not found.")
        group.add_student(student)

    def register_grade(self, student: Student, level: str, subject: str, period: str, grade_value: typing.Union[str, float]):
        """Enforces evaluation and grading schema validation constraints before committing records."""
        # Ensure subject belongs to level
        valid_subjects = LEVEL_SUBJECTS.get(level, [])
        if subject not in valid_subjects:
            raise ValueError(f"Subject '{subject}' is not offered in educational level '{level}'")

        # Ensure correct period validation
        if period not in GRADING_PERIODS:
            raise ValueError(f"Invalid grading period: '{period}'. Must be one of {GRADING_PERIODS}")

        # Validate grading scale constraints
        scale = GRADING_SCALES.get(level)
        if scale is not None:
            # Categorical validation (e.g., Inicial & Primaria scales)
            if grade_value not in scale:
                raise ValueError(f"Grade '{grade_value}' is invalid for scale of '{level}'. Expected {scale}")
        else:
            # Numeric grade verification (Secondary defaults to 0-100)
            if not isinstance(grade_value, (int, float)) or not (0 <= grade_value <= 100):
                raise ValueError(f"Grade value '{grade_value}' must be a numeric score between 0 and 100 for '{level}'")

        # Register score if validations pass
        if subject not in student.academic_record:
            student.academic_record[subject] = {}
        student.academic_record[subject][period] = grade_value

# --- USAGE EXAMPLE (PSEUDOCODE EXECUTION) ---
if __name__ == "__main__":
    # 1. Initialize System
    system = AcademicPerformanceSystem()
    
    # 2. Add Center
    center = system.register_center("C001", "ST-9923", "Instituto Tecnológico Central")
    
    # 3. Establish Class Groups
    primary_group = center.create_group(
        level="Educación Primaria", 
        modality="primaria regular", 
        shift="Matutino", 
        grade="tercero"
    )
    
    # 4. Enroll Students
    student1 = Student("Carlos", "Gomez", grade="tercero", personal_code="STUD8812")
    system.enroll_student_to_group("C001", primary_group, student1)
    
    # 5. Register validated grade cards (e.g., Primary allows AP, AA, AS, AI)
    try:
        system.register_grade(
            student=student1, 
            level="Educación Primaria", 
            subject="MATEMÁTICA", 
            period="I corte", 
            grade_value="AA"
        )
        print("Successfully saved grade!")
    except ValueError as e:
        print(f"Validation Error: {e}")