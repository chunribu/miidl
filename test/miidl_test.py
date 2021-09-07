import miidl

# Sequential style
data = miidl.read('FILE')
data = miidl.qc(data)
data = miidl.normalize(data)
data = miidl.impute(data)
data = miidl.reshape(data)
data = miidl.buildmodel(data)
data = miidl.explain()
data = miidl.buildnet(data)

# Chain style
data = miidl.read().qc().normalize().impute().reshape().buildmodel().explain().buildnet()

# Save data
data.save()

