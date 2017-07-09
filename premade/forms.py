from django import forms 

STRAT_CHOICES = [("PT", "Pairs Trade"), ("MA", "Moving Average")]

class StrategyForm(forms.Form):
	
	strategy = forms.ChoiceField(label="Strategy",choices=STRAT_CHOICES)