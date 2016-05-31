# -*- coding: utf-8 -*-

# define function to change conditions
def setupConditions(model, medium='ypd', aeration='aerobic'):
    """
    # This function sets up the medium and aeration conditions for the model
    # Inputs: model - model of organism's metabolism
    #         medium - either 'ypd' or 'minimal'
    #         aeration - either 'aerobic' or 'anaerobic' 
    """
    R1 = model.reactions[1192] # oxygen uptake
    R2 = model.reactions[1196] # amonium uptake
    R3 = model.reactions[1176] # sulphate uptake
    R4 = model.reactions[1189] # phasphate uptake
    R5 = model.reactions[1260] # glucose uptake
    
    R6 = model.reactions[1223] # L-alanine uptake
    R7 = model.reactions[1222] # L-arginine uptake
    R8 = model.reactions[1220] # L-aspartate uptake
    R9 = model.reactions[1219] # L-cysteine uptake
    R10 = model.reactions[1217] # L-glutamate uptake
    R11 = model.reactions[1229] # glycine uptake
    R12 = model.reactions[1215] # L-histidine uptake
    R13 = model.reactions[1214] # L-isoleucine uptake
    R14 = model.reactions[1213] # L-leucine uptake
    R15 = model.reactions[1212] # lysine uptake
    R16 = model.reactions[1211] # methionine uptake
    R17 = model.reactions[1209] # L-phenylalanine uptake
    R18 = model.reactions[1208] # L-proline uptake
    R19 = model.reactions[1207] # L-serine uptake
    R20 = model.reactions[1206] # L-threonine  uptake
    R21 = model.reactions[1205] # L-tryptophan uptake
    R22 = model.reactions[1204] # L-tyrosine uptake
    R23 = model.reactions[1203] # L-valine uptake
    
    R24 = model.reactions[1187] # potassium uptake
    R25 = model.reactions[1182] # sodium uptake
    R26 = model.reactions[1256] # biotin uptake
    R27 = model.reactions[1255] # chlorine uptake
    R28 = model.reactions[1185] # raboflavin uptake
    R29 = model.reactions[1175] # thiamine uptake
    R30 = model.reactions[1198] # myo-inositol uptake
    R31 = model.reactions[1174] # thymidine uptake
    R32 = model.reactions[1271] # (R)-panthotenate uptake
    R33 = model.reactions[1172] # uracyl uptake
    
    R34 = model.reactions[1236] # ergosterol uptake
    R35 = model.reactions[1168] # zymosterol uptake
    
    
    # set up medium conditions    
    R1.upper_bound = 6.3
    R2.upper_bound = 1000
    R3.upper_bound = 1000
    R4.upper_bound = 1000
    R5.upper_bound = 22.6
    
    
    # Set specific medium conditions
    if medium == 'ypd':
        R6.upper_bound = 0.519
        R7.upper_bound = 0.193
        R8.upper_bound = 0.274
        R9.upper_bound = 0.0192
        R10.upper_bound = 0.479
        R11.upper_bound = 0.934
        R12.upper_bound = 0.31
        R13.upper_bound = 0.0952
        R14.upper_bound = 1.66
        R15.upper_bound = 0.167
        R16.upper_bound = 0.0468
        R17.upper_bound = 0.0758
        R18.upper_bound = 0.357
        R19.upper_bound = 0.166
        R20.upper_bound = 0.112
        R21.upper_bound = 0.0207
        R22.upper_bound = 0.0279
        R23.upper_bound = 0.148
        
        R24.upper_bound = 1000
        R25.upper_bound = 1000
        R26.upper_bound = 1000
        R27.upper_bound = 1000
        R28.upper_bound = 1000
        R29.upper_bound = 1000
        R30.upper_bound = 1000
        R31.upper_bound = 1000
        R32.upper_bound = 1000
        R33.upper_bound = 1000
        
    else: #medium == 'minimal'
        R6.upper_bound = 0
        R7.upper_bound = 0
        R8.upper_bound = 0
        R9.upper_bound = 0
        R10.upper_bound = 0
        R11.upper_bound = 0
        R12.upper_bound = 0
        R13.upper_bound = 0
        R14.upper_bound = 1
        R15.upper_bound = 0
        R16.upper_bound = 0
        R17.upper_bound = 0
        R18.upper_bound = 0
        R19.upper_bound = 0
        R20.upper_bound = 0
        R21.upper_bound = 0
        R22.upper_bound = 0
        R23.upper_bound = 0
        
        R24.upper_bound = 1000
        R25.upper_bound = 1000
        R26.upper_bound = 1000
        R27.upper_bound = 1000
        R30.upper_bound = 1000
        R32.upper_bound = 1000
        R33.upper_bound = 1000

    
    # set aeration conditions and in case of anaerobiosis, supplement the medium adequately for growth
    if aeration == 'anaerobic':    
        R1.upper_bound = 0
        R34.upper_bound = 1000
        R35.upper_bound = 1000
        
    return model