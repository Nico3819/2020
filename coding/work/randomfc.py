import random
def goalkeeper():
  goalkeepers = ('vega','kepa','allison','howard','ter stegen','de gea','ederson','courtois','lloris') 
  print ('\t\t\t\t\t\t%s' % (random.choice(goalkeepers)))

goalkeeper()

def defender():
  defenders = ('trent','robertson','david luiz','van dijk','sokratis','thompson','jungwurth','ramos','pique','marcelo','alba','phil jones','smalling','azpuliceta','thiago silva','varane','umtti')
  print('\n\n\n\n\n\n\n\n\n%s\t\t\t%s\t\t\t%s\t\t%s' % (random.choice(defenders),random.choice(defenders),random.choice(defenders),random.choice(defenders)))

defender()

def midfielder():
  midfielders = ('kante','lampard','modric','yueill','de breyune','jorginho','pogba','buesquets','modric','rakatic','judson','david silva','kovacic','muller','kroos')
  print('\n\n\n\n\n\n\n\n\t\t%s\t\t\t\t%s\t\t\t\t%s' % (random.choice(midfielders),random.choice(midfielders),random.choice(midfielders)))

midfielder()

def forward():
  forwards = ('messi','ronaldo','neymar','mbappe','aguero','mane','salah','suarez','wondolowski','morata','lewandowski','greizmann','pulisic','aubamayang','sterling','zlatan','vako','bale','hazard','benzema')
  print('\n\n\n\n\n\n\n\t\t%s\t\t\t\t%s\t\t\t\t%s\t\n\n' % (random.choice(forwards),random.choice(forwards),random.choice(forwards)))

forward()
