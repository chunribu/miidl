import captum.attr
# IntegratedGradients, Saliency, DeepLift, DeepLiftShap, InputXGradient, GuidedBackprop, GuidedGradCam, Deconvolution, FeaturePermutation, KernelShap, LRP

def explain(model, input, method='IntegratedGradients', target=2):
    interp = getattr(captum.attr, method)(model)
    attribution = interp.attribute(input, target)
    return attribution