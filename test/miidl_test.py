from miidl import MData


md = MData()
md.read('FILE', role='all')
md.qc()
md.normalize()
md.impute()
md.reshape()
md.buildmodel()
md.explain()

# Save data
md.save()
