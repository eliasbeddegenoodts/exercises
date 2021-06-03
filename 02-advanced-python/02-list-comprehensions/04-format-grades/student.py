def format_grades(grades):
    def avg(ns):
        return round(sum(ns) / len(ns))

    return "\n".join( f'''{name}: {avg(gradeOfStudent)}''' for name, gradeOfStudent in grades.items() )
    
    