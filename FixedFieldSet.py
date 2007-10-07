
class FixedField:
    def __init__(self, name=None, start=0, end=0, type=str):
        self.name = name
        self.start = start
        self.end = end
        self.type = type
        self.sum = 0
        self.avg = 0
        self.min = 0
        self.max = 0
        self.count = 0
        
    
class RecordParser:
    fields = []
    parsed_records = []
    
    def __init__(self, fields=[]):
        self.fields = fields
        
    def parse(self, records):
        for record in records:
            parsed_record = {}
            
            for field in self.fields:
                value = field.type(record[field.start:field.end].strip())
                parsed_record[field.name] = value
                
                field.count += 1
                if isinstance(value, int) or isinstance(value, long) or isinstance(value, float):
                    field.sum += value
                    if value > field.max: field.max = value
                    if field.count == 1 or value < field.min: field.min = value
                      
            self.parsed_records.append(parsed_record)
        
        parsed = True
        #print self.parsed_records

    def show_stats(self):
        for field in self.fields:
            if field.count > 0:
                field.avg = field.sum/field.count
            
            print '<%s> count:%d sum:%d avg:%d min:%d max:%d' % (field.name, field.count, field.sum, field.avg, field.min, field.max)

 
if __name__ == '__main__':
    records = ['050070200707019999', '050070200708020050', '050072200710070375']
    fields = [FixedField('insurer_id', 0, 6, str), 
              FixedField('date', 6, 14, str),
              FixedField('contract_amt', 14, 18, int), 
              ]  
    
    rp = RecordParser(fields)
    rp.parse(records)
    rp.show_stats()
    
    

    