def create_classes(db):
    class Loan(db.Model):
        __tablename__ = 'loanData'

        id = db.Column(db.Integer, primary_key=True)
        member_id = db.Column(db.Integer(64))
        loan_amnt = db.Column(db.db.Integer(64))
        funded_amnt = db.Column(db.db.Integer(64))
        term_yrs = db.Column(db.db.Integer(64))
        int_rate = db.Column(db.Float(64))
        grade = db.Column(db.Object)
        sub_grade = db.Column(db.Object)
        emp_length = db.Column(db.Object)
        home_ownership = db.Column(db.Object)
        annual_inc = db.Column(db.Float(64))
        issue_d = db.Column(db.Object)
        loan_status = db.Column(db.Object)
        desc = db.Column(db.Object)
        purpose = db.Column(db.Object)
        addr_state = db.Column(db.Object)
        dti = db.Column(db.Float(64))
        recoveries = db.Column(db.Float(64))
        last_pymnt_d = db.Column(db.Object)
        last_pymnt_amnt = db.Column(db.Float(64))
        application_type = db.Column(db.Object)
        tot_cur_bal = db.Column(db.Float(64))

        def __repr__(self):
            return '<Loan %r>' % (self.id)
    return Loan
