from miidl import MData

md = MData()
md.read('CRC.txt')
md.qc(obs=0.25)
# In this case, normalization and imputation are not applied
# md.normalize(method='none')
# md.impute(method='none')
md.reshape()
md.buildmodel(epochs=50)
md.explain(target='CRC')
md.save()# Save data
