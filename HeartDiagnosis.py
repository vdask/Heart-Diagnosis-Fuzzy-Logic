from RuleBase.Age import *
from RuleBase.BloodPressure import *
from RuleBase.Cholesterol import *
from RuleBase.BloodSugar import *
from RuleBase.LoweDensityLipoprotein import *
from RuleBase.HighDensityLipoprotein import *
from RuleBase.RiskRule import *
from Risk import Risk
class HeartDiagnosis:
    def __init__(self):
        print("\t\tWelcome In Fuzzy Logic Hospital ❤❤")
        print("Enter health data for Heart Disease Risk Calculation with Fuzzy Logic")

        self.userAge            = getInformationUser("Enter Age: ")
        self.userBloodPressure  = getInformationUser("Enter Blood Pressure:  ")
        self.userCholesterol    = getInformationUser("Enter Cholesterol:  ")
        self.userBloodSugar     = getInformationUser("Enter Blood Sugar:  ")
        self.userLDL            = getInformationUser("Enter Lowe Density Lipoprotein:  ")
        self.userHDL            = getInformationUser("Enter High Density Lipoprotein:  ")

        print("Thanks, Pleas Wait To Calculate Result 😊")

    def heartDiagnosis(self):
        ageRule = Age()
        ageRule.trapezoidalMembership()
        ageRule.draw()
        # Fuzzification
        ageRule.membershipDegrees(self.userAge)

        bloodRule = BloodPressure()
        bloodRule.trapezoidalMembership()
        bloodRule.draw()
        # Fuzzification
        bloodRule.membershipDegrees(self.userBloodPressure)

        cholesterolRule = Cholesterol()
        cholesterolRule.trapezoidalMembership()
        cholesterolRule.draw()
        # Fuzzification
        cholesterolRule.membershipDegrees(self.userCholesterol)

        bloodSugarRule = BloodSugar()
        bloodSugarRule.triangularMembership()
        bloodSugarRule.draw()
        # Fuzzification
        bloodSugarRule.membershipDegrees(self.userBloodSugar)

        ldlRule = LoweDensityLipoprotein()
        ldlRule.triangularMembership()
        ldlRule.draw()
        # Fuzzification
        ldlRule.membershipDegrees(self.userLDL)


        hdlRule = HighDensityLipoprotein()
        hdlRule.triangularMembership()
        hdlRule.draw()
        # Fuzzification
        hdlRule.membershipDegrees(self.userHDL)

        riskRule = RiskRule()
        riskRule.trapezoidalMembership()
        riskRule.draw()


        riskValues = Risk(ageRule=ageRule,
                          bloodRule=bloodRule,
                          cholesterolRule=cholesterolRule,
                          bloodSugarRule=bloodSugarRule,
                          ldlRule=ldlRule,
                          hdlRule=hdlRule,
                          riskRule=riskRule)

        # combining the fuzzified inputs according to the fuzzy rules to establish a rule strength
        riskValues.inferenceSystems()

        # cloudy inference engine using rules
        riskValues.cloudyInferenceEngine()

        risk0 = zeros_like(risk)

        fig, ax0 = plt.subplots()
        ax0.fill_between(risk, risk0, riskValues.uninfected, facecolor='r', alpha=0.7)
        ax0.plot(risk, riskRule.riskNot, 'r', linestyle='--')
        ax0.fill_between(risk, risk0, riskValues.little, facecolor='g', alpha=0.7)
        ax0.plot(risk, riskRule.riskLittle, 'g', linestyle='--')
        ax0.fill_between(risk, risk0, riskValues.mid, facecolor='b', alpha=0.7)
        ax0.plot(risk, riskRule.riskMid, 'b', linestyle='--')
        ax0.fill_between(risk, risk0, riskValues.high, facecolor='y', alpha=0.7)
        ax0.plot(risk, riskRule.riskHigh, 'y', linestyle='--')
        ax0.fill_between(risk, risk0, riskValues.veryHigh, facecolor='m', alpha=0.7)
        ax0.plot(risk, riskRule.riskVeryHigh, 'm', linestyle='--')
        ax0.set_title('Out of the Risk')

        plt.tight_layout()

        # Defuzzification
        crispValue  = fmax(fmax(fmax(fmax(riskValues.uninfected, riskValues.little), riskValues.mid), riskValues.high), riskValues.veryHigh)

        defuzzified = fuzz.defuzz(risk, crispValue, "mom") # mean of maximum

        result = fuzz.interp_membership(risk, crispValue, defuzzified)

        print(f"\n\tCoroner Heart Diagnosis: {defuzzified}")



        fig, ax0 = plt.subplots()

        ax0.plot(risk, riskRule.riskNot, 'r', linewidth=0.5, linestyle="--")
        ax0.plot(risk, riskRule.riskLittle, 'g', linewidth=0.5, linestyle="--")
        ax0.plot(risk, riskRule.riskLittle, 'b', linewidth=0.5, linestyle="--")
        ax0.plot(risk, riskRule.riskHigh, 'y', linewidth=0.5, linestyle="--")
        ax0.plot(risk, riskRule.riskVeryHigh, 'm', linewidth=0.5, linestyle="--")

        ax0.fill_between(risk, risk0, crispValue, facecolor="Orange", alpha=0.7)
        ax0.plot([defuzzified, defuzzified], [0, result], 'k', linewidth=1.5, alpha=0.9)
        ax0.set_title("Mean of Maximum Defuzzification")

        plt.tight_layout()