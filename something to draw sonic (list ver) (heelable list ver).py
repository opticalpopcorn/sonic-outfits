import random

input_that_restarts = ''
perma_chara = ''
perma_outfit = ''
chara_list = ['amy',
              'antoine',
              'blaze',
              'bunnie',
              'cassia',
              'chaos',
              'classic sonic',
              'clove',
              'cream',
              'eclipse',
              'espio',
              'gadget',
              'geoffery',
              'gold',
              'honey',
              'infinite',
              'jet',
              'knuckles',
              'lisbon',
              'manic',
              'metal',
              'mighty',
              'nicole',
              'paris',
              'peaches',
              'ray',
              'rouge',
              'sally',
              'scourge',
              'shadow',
              'silver',
              'sonia',
              'sonic',
              'sticks',
              'tails',
              'wave',
              ]

while input_that_restarts != "quit":
    
    top_style = ''
    top_color = ''
    top_pattern = ''
    top_logo = ''
    top_type_cas = ''
    top_type_form = ''
    top_type_dress = ''
    top_type_spe = ''
    jacket_logo = '' 
    jacket_color = ''
    jacket_pattern = ''
    jacket_type_cas = ''
    jacket_type_form = ''
    jacket_type_dress = ''
    bottom_type_cas = ''
    bottom_type_form = '' 
    skirt_length = ''
    skirt_fold = ''
    bottom_pattern = ''
    bottom_color = ''
    shoe_type_cas = ''
    shoe_type_form = ''
    shoe_type_spe = ''
    shoe_color = ''
    heel_type = ''


    #choose the character from the character list defined before starting-------------------------------------------------------------------
    chara = random.choice(chara_list)

#TOPS
    #choose type of top; eg t-shirt, blouse, etc., includes dress-------------------------------------------------------------------
    top_type_cas_list = [' t-shirt',
                         ' t-shirt',
                         ' tank top',
                         ' tank top',
                         ' long-sleeve t-shirt',
                         ' tube top',]
    top_type_form_list = [' long-sleeved blouse',
                          ' short-sleeved blouse',
                          ' dress shirt',]
    top_type_dress_list = [' dress',]
    top_type_spe_list = [' swimsuit',
                         ' nightshirt',
                         ' bathrobe',
                         ' romper',
                         ' jumpsuit',]
    
    rand_int = random.randint(1,11)
    if rand_int in range(1,5):
        top_type_cas = random.choice(top_type_cas_list)
    elif rand_int in range(5,8):
        top_type_form = random.choice(top_type_form_list)
    elif rand_int == 8:
        top_type_dress = random.choice(top_type_dress_list)
    else:
        top_type_spe = random.choice(top_type_spe_list)

    #choose style of top. dependent on the type of top.-------------------------------------------------------------------
    if top_type_cas != '':                      #styles for casual tops
        style_list = [' muted',
                      ' pastel',
                      ' vibrant',
                      ' dark',
                      ' button-up',
                      ' loose-fitting',
                      ' form-fitting',]
    elif top_type_form != '':                   #styles for formal tops
        style_list = [' muted',
                      ' pastel',
                      ' dark',
                      ' chic',
                      ' silk',
                      ' lacy',
                      ' button-up',
                      ' ruffled',
                      ' loose-fitting',
                      ' form-fitting',]
    elif top_type_dress != '':                  #styles for dresses
        style_list = [' muted',
                      ' pastel',
                      ' vibrant',
                      ' dark',
                      ' chic',
                      ' cute',
                      ' knit',
                      ' silk',
                      ' lacy',
                      ' button-up',
                      ' ruffled',
                      ' loose-fitting',
                      ' form-fitting',]
    else:                                       #individual styles for special top types that can't be consolidated
        if top_type_spe == ' swimsuit':
            style_list = [' muted',
                          ' pastel',
                          ' vibrant',
                          ' dark',
                          ' chic',
                          ' cute',
                          ' ruffled',]
        elif top_type_spe == ' nightshirt':
            style_list = [' muted',
                          ' pastel',
                          ' vibrant',
                          ' dark',
                          ' cute',
                          ' silk',
                          ' lacy',
                          ' button-up',
                          ' ruffled',
                          ' loose-fitting']
        elif top_type_spe == ' bathrobe':
            style_list = [' muted',
                          ' pastel',
                          ' vibrant',
                          ' dark',
                          ' cute',
                          ' plush-lined',
                          ' silk',
                          ' lacy',
                          ' button-up',
                          ' zip-up',
                          ' loose-fitting']
        else:   #(romper/jumpsuit)
            style_list = [' muted',
                          ' pastel',
                          ' vibrant',
                          ' dark',
                          ' chic',
                          ' cute',
                          ' silk',
                          ' lacy',
                          ' button-up',
                          ' ruffled',
                          ' loose-fitting',
                          ' form-fitting',]
    top_style = random.choice(style_list)
            
    #top color-------------------------------------------------------------------
    color_list = [    ' red',
                      ' red',
                      ' orange',
                      ' yellow',
                      ' green',
                      ' blue',
                      ' violet',
                      ' pink',
                      ' white',
                      ' white',
                      ' white',
                      ' black',
                      ' black',
                      ' black',
                      ' brown',
                      ' gray',]
    if random.randint(1,24) == 24:                       #1/24 chance to change top color to rainbow
        top_color = ' rainbow'
    else:
        top_color = random.choice(color_list)     

    #top pattern-------------------------------------------------------------------
    if (random.randint(1,2) == 1) and (top_type_form == ''):
        top_pattern_list = [' striped',  
                            ' striped',  
                            ' striped',  
                            ' polka-dot',       
                            ' floral',                
                            ' zentangle',      
                            ' checkerboard',
                            ' grid-patterned',
                            ' star-patterned',
                            ' tie-dye']
        top_pattern = random.choice(top_pattern_list)
    else:
        top_pattern = ''

    #top emblazoned with...-------------------------------------------------------------------
    if random.randint(1,10) in range (1,7):
        if (top_type_form == '') and (top_type_dress == '') and (top_pattern != ' zentangle'):          #nested "if/elses" for legibility
            top_logo_list = [' the adidas logo',
                             ' the nike logo',
                             ' the sonic logo',
                             ' the sega logo',
                             ' a phantom ruby decal',
                             ' a cluster of flowers',
                             ' a swearword',
                             ' the words "keep calm and carry on"',
                             ' stars',
                             ' a set of orange slices',
                             ' some bees',
                             ' the moon',
                             ' an autumn leaf',
                             ' a famous quote',
                             ' a skull',
                             ' a panda',
                             ' a crow',
                             ' a rainbow']
                             
            top_logo = random.choice(top_logo_list)
        else:
            top_logo = ''
    else:
        top_logo = ''

    #assign sleeves to dress-------------------------------------------------------------------
    if (top_type_dress != ''):
        dress_sleeve_length_list = [' sleeveless',
                                    ' short-sleeved',
                                    ' elbow-length-sleeved',
                                    ' long-sleeved',]
        dress_sleeve_length = random.choice(dress_sleeve_length_list)
    else:
        dress_sleeve_length = ''

#JACKETS
    #jacket type-------------------------------------------------------------------
    if random.randint(1,10) in range(1,8):     
        if top_type_cas != '':                   #casual jacket types         
            jacket_type_list = [' jacket',
                                ' parka',
                                ' poncho',
                                ' pullover hoodie',
                                ' sweater',
                                ' sweatshirt',
                                ' varsity jacket',
                                ' zip-up hoodie',
                                ' jacket tied around their waist']
            jacket_type_cas = random.choice(jacket_type_list)
            
        elif top_type_form != '':                #formal jacket types
            if random.randint(1,3) == 1:
                jacket_type_list = [' jacket',
                                    ' parka',
                                    ' poncho',
                                    ' pullover hoodie',
                                    ' sweater',
                                    ' sweatshirt',
                                    ' zip-up hoodie']
                jacket_type_cas = random.choice(jacket_type_list)
            else:
                jacket_type_list = [' suit jacket',
                                    ' double-breasted jacket',
                                    ' sweater',
                                    ' sweater vest',]
                jacket_type_form = random.choice(jacket_type_list)
                
        elif top_type_dress != '':               #jackets worn with dresses
            if random.randint(1,10) in range (1,8):
                jacket_type_list =[' jacket',
                                   ' parka',
                                   ' poncho',
                                   ' varsity jacket',
                                   ' zip-up hoodie']
                jacket_type_dress = random.choice(jacket_type_list)
            else:
                jacket_type_dress = ''

        else:                                    #special top type jacket; always none
            jacket_type_cas = ''
            jacket_type_form = ''
            jacket_type_dress = ''
            
    else:                                        #no jacket
        jacket_type_cas = ''
        jacket_type_form = ''
        jacket_type_dress = ''

    #jacket style-------------------------------------------------------------------
    if random.randint(1,8) in range(1,8):
        if jacket_type_cas != '':                   #styles for casual jackets
            jacket_style_list = [' muted',
                                ' pastel',
                                ' vibrant',
                                ' dark',
                                ' cute',
                                ' loose-fitting',
                                ' form-fitting',]
            jacket_style = random.choice(jacket_style_list)
        else:                                       #styles for dress/formal jackets
            jacket_style_list = [' muted',
                                     ' dark',
                                     ' chic',
                                     ' button-up',
                                     ' loose-fitting',
                                     ' form-fitting',]
            jacket_style = random.choice(jacket_style_list)
    else:                                           #styles for no jacket; always blank
        jacket_style = ''
        
    #jacket color-------------------------------------------------------------------
    if jacket_type_cas != '' or jacket_type_dress != '':
        if random.randint(1,15) in range(1,15):                 #gives a 1/15 chance of not defining a jacket color even when a jacket is present; helps prevent over-cluttering with adjectives
            jacket_color = random.choice(color_list)            #casual and dress jackets use the default colors...
        else:
            jacket_color = ''
    elif  jacket_type_form != '':
        jacket_color_form_list = [' blue',
                                  ' black',
                                  ' white',
                                  ' gray',
                                  ' brown']
        jacket_color = random.choice(jacket_color_form_list)    #...while formal jackets have special muted colors
    else:
        jacket_color = ''
        
    #jacket pattern-------------------------------------------------------------------
    if random.randint(1,20) in range (1,11):
        if top_pattern == '':                               #prevents jacket pattern from clashing with top pattern. ...*
            
            if jacket_type_cas != '' or jacket_type_dress != '':
                jacket_pattern_list = [' striped',
                                       ' striped',
                                       ' striped',
                                       ' polka-dot',
                                       ' plaid',
                                       ' floral',
                                       ' zentangle',
                                       ' checkerboard',
                                       ' grid-patterned',
                                       ' star-patterned',
                                       ' tie-dye']
                jacket_pattern = random.choice(jacket_pattern_list)
            elif jacket_type_form != '':                    #formal jackets can only be striped or non-patterned
                if random.randint(1,3) == 1:
                    jacket_pattern = ' striped'
            else:                                           #if no jacket is present, the jacket pattern is blank
                jacket_pattern == ''
                
        else:                                               #*prevents jacket pattern from clashing with top pattern. ...
            if random.randint(1,3) == 1:                         #...the jacket pattern is either set to the pattern of the top (1/3 chance)...
                jacket_pattern == top_pattern
            else:
                jacket_pattern = ''                              #...or to no pattern (2/3 chance)
    else:
        jacket_pattern = ''

    #jacket emblazoned with...-------------------------------------------------------------------
    if top_logo == '' and jacket_type_cas != '':            #logos can only be present on casual jackets
        if random.randint(1,3) == 1:
            jacket_logo_list = [' the adidas logo',
                             ' the nike logo',
                             ' the sonic logo',
                             ' the sega logo',
                             ' a phantom ruby decal',
                             ' a cluster of flowers',
                             ' a swearword',
                             ' the words "keep calm and carry on"',
                             ' stars',
                             ' a set of orange slices',
                             ' some bees',
                             ' the moon',
                             ' an autumn leaf',
                             ' a famous quote',
                             ' a skull',
                             ' a panda',
                             ' a crow',
                             ' a rainbow']
            jacket_logo = random.choice(jacket_logo_list)
        else:
            jacket_logo = ''
    else:
        jacket_logo = ''

#BOTTOMS
    #bottom type-------------------------------------------------------------------
    if random.randint(1,2) == 1:
        if (top_type_spe == '') and (top_type_dress == ''):     #if they're not already wearing a top that doesn't need pants (eg dress, romper, swimsuit)...
            if top_type_form != '':                                 #...and if the top type is formal, choose...
                if random.randint(1,5) == 1:                            #...maybe casual bottoms (1/5 chance)...                              
                    bottom_type_list = [' skirt',
                                        ' pair of leggings',
                                        ' pair of jeans',
                                        ' pair of skinny jeans',]
                    bottom_type_form = random.choice(bottom_type_list)
                else:
                    bottom_type_list = [' skirt',                       #...but usually formal bottoms (4/5 chance)
                                        ' pair of slacks']
                    bottom_type_form = random.choice(bottom_type_list)
            else:                                                   #if the top is casual(?), choose casual bottoms
                bottom_type_list = [' skirt',
                                    ' pair of shorts',
                                    ' pair of overalls',
                                    ' pair of sweatpants',
                                    ' pair of leggings',
                                    ' pair of jeans',
                                    ' pair of skinny jeans',]
                bottom_type_cas = random.choice(bottom_type_list)
        else:
            bottom_type_cas = ''
            bottom_type_form = ''
    else:
        bottom_type_cas = ''
        bottom_type_form = ''
        
    #assign length to dress/skirt-------------------------------------------------------------------
    if (top_type_dress != '') or (bottom_type_cas == ' skirt') or (bottom_type_form == ' skirt'):
        skirt_length_list = [' short',
                             ' mid-thigh length',
                             ' knee-length',
                             ' midi-length',
                             ' ankle-length',
                             ' maxi-length']
        skirt_length = random.choice(skirt_length_list)
    else:
        skirt_length = ''

    #assign fold style to dress/skirt-------------------------------------------------------------------
    if (top_type_dress != '') or (bottom_type_cas == ' skirt') or (bottom_type_form == ' skirt'):
        if random.randint(1,2) == 1:                            #1/2 chance of a skirt having a fold (or another extra feature in the fabric)
            skirt_fold_list = [' slitted',
                               ' tiered',
                               ' yoke-waist',
                               ' knife-pleated',
                               ' box-pleated',
                               ' accordion']
            skirt_fold = random.choice(skirt_fold_list)
        else:
            skirt_fold = ''
    else:
        skirt_fold = ''

    #bottom color-------------------------------------------------------------------
    if bottom_type_cas != '' or bottom_type_form != '':
        if bottom_type_cas == ' pair of jeans' or ' pair of skinny jeans':      
            jeans_color_list = [' blue',
                                ' black',
                                ' white',
                                ' gray',]
            bottom_color = random.choice(jeans_color_list)                      #if the bottom type is jeans, stick to these non-ugly jeans colors^^...
        else:
            bottom_color = random.choice(color_list)                            #...otherwise, use the generic color list defined in the "tops" section
    else:
        bottom_color = ''

    #bottom pattern-----------------------------------------------------------------
    if bottom_type_cas != '':
        if random.randint(1,4) == 1:
            bottom_pattern_list = [' striped',
                                   ' polka-dot',
                                   ' floral',
                                   ' zentangle',
                                   ' checkerboard',
                                   ' grid-patterned',
                                   ' star-patterned']
            bottom_pattern = random.choice(bottom_pattern_list)
        else:
            bottom_pattern = ''
    else:
        bottom_pattern = ''

#SHOES
    #shoe type------------------------------------------------------------------------
    if random.randint(1,10) in range(1,6):
        if top_type_form != '':                         #if the top type is formal
            shoe_type_form_list = [' oxfords',
                                   ' loafers',
                                   ' pumps']
            shoe_type_form = random.choice(shoe_type_form_list) 
        elif (top_type_cas != '') or (top_type_dress != '') or (top_type_spe == ' jumpsuit') or (top_type_spe == ' romper'):      #if the top is casual, a dress, or is a romper or jumpsuit
            shoe_type_cas_list = [' combat boots',
                                  ' ankle boots',
                                  ' thigh-high boots',
                                  ' knee-high boots',
                                  ' sneakers',
                                  ' converse',
                                  ' sandals',
                                  ' loafers',
                                  ' pumps',
                                  ' flip-flops']
            shoe_type_cas = random.choice(shoe_type_cas_list)
        elif top_type_spe == ' swimsuit':
            shoe_type_spe_list = [' flip-flops',
                                  '',
                                  '']
            shoe_type_spe = random.choice(shoe_type_spe_list)
        else:
            shoe_type_spe_list = [' slippers',
                                  '',
                                  '']
            shoe_type_spe = random.choice(shoe_type_spe_list)
    else:
        shoe_type_cas = ''
        shoe_type_form = ''
        shoe_type_spe = ''

    #shoe heel------------------------------------------------------------------------
    heel_type = ''
    if shoe_type_cas in (' ankle boots', ' thigh-high boots', ' knee-high boots', ' pumps'):
        heel_type_list = [' with stiletto heels',
                          ' with block heels',
                          ' with wedge heels',
                          '']
        heel_type = random.choice(heel_type_list)
    elif (shoe_type_form == ' pumps'):
        heel_type_list = [' with stiletto heels',
                          ' with block heels',
                          ' with wedge heels',
                          '']            
        heel_type = random.choice(heel_type_list)            
    else:
        heel_type = ''
        

    #shoe color------------------------------------------------------------------------
    if shoe_type_cas != '':
        shoe_color = random.choice(color_list)
    elif shoe_type_form != '':
        shoe_color_form_list = [' white',
                                ' gray',
                                ' black',
                                ' brown']
        shoe_color = random.choice(shoe_color_form_list)
    else:
        shoe_color = ''



        



        
    if perma_chara != '':
        chara = perma_chara
    if perma_outfit == 'true':
        top_style = perma_top_style
        top_color = perma_top_color
        top_pattern = perma_top_pattern
        top_logo = perma_top_logo
        top_type_cas = perma_top_type_cas
        top_type_form = perma_top_type_form
        top_type_dress = perma_top_type_dress
        top_type_spe = perma_top_type_spe
        dress_sleeve_length = perma_dress_sleeve_length
        jacket_logo = perma_jacket_logo 
        jacket_color = perma_jacket_color
        jacket_pattern = perma_jacket_pattern
        jacket_style = perma_jacket_style
        jacket_type_cas = perma_jacket_type_cas
        jacket_type_form = perma_jacket_type_form
        jacket_type_dress = perma_jacket_type_dress
        bottom_type_cas = perma_bottom_type_cas
        bottom_type_form = perma_bottom_type_form 
        skirt_length = perma_skirt_length
        skirt_fold = perma_skirt_fold
        bottom_pattern = perma_bottom_pattern
        bottom_color = perma_bottom_color
        shoe_type_cas = perma_shoe_type_cas
        shoe_type_form = perma_shoe_type_form
        shoe_type_spe = perma_shoe_type_spe
        shoe_color = perma_shoe_color
        heel_type = perma_heel_type
        



    
    print('''---------

here is your prompt:''')
    
    print('draw this:')

    #prints the shirt/dress
    if top_type_dress == '':
        print(chara+' wearing a'+top_style+top_color+top_pattern+top_type_cas+top_type_form+top_type_spe+'.')
    else:
        print(chara+' wearing a'+dress_sleeve_length+top_style+top_color+top_pattern+top_type_dress+' with a'+skirt_fold+skirt_length+' skirt.')            

    #prints the jacket
    if jacket_type_cas != '' or jacket_type_form != '':
        print('with it they are wearing a'+jacket_style+jacket_color+jacket_pattern+jacket_type_cas+jacket_type_form+jacket_type_dress+'.')
    else:
        pass

    #prints the decoration on the shirt/dress
    if top_logo != '':
        print('the'+top_type_cas+top_type_form+top_type_dress+top_type_spe+' has'+top_logo,'on it.')
    else:
        pass

    #prints the decoration on the jacket
    if ((jacket_type_cas != '') or (jacket_type_form != '') or (jacket_type_dress != '')) and (jacket_logo != ''):
        print('the'+jacket_type_cas+jacket_type_form+jacket_type_dress+' has'+jacket_logo+' on it.')
    else:
        pass

    #prints the skirt
    if (bottom_type_cas != '') or (bottom_type_form != ''):
        print('they are wearing a'+skirt_fold+skirt_length+bottom_color+bottom_pattern+bottom_type_cas+bottom_type_form+'.')

    #prints the shoes
    if (shoe_type_cas != '') or (shoe_type_form != '') or (shoe_type_spe != ''):
        print('they are wearing'+shoe_color+shoe_type_cas+shoe_type_form+shoe_type_spe+heel_type+'.')


        
    input_that_restarts = input('''
press enter for another prompt. type help for a list of commands. ''')

    if input_that_restarts == 'help':
        print('''
---------HELP MENU---------

>type "lock chara" to custom-set a character and keep
    it set until the "unlock chara" command is used.
    you choose which character to set.
    
>type "unlock chara" to unset the permanent character.

>type "lock outfit" to keep the last outfit that was
    generated. the outfit stays locked until the
    "unlock outfit" command is used.
    
>type "unlock outfit" to unset the locked outfit.

>type "quit" to quit.

press enter for another prompt. ''')
        input_that_restarts = input()
    if input_that_restarts == 'lock chara':
        perma_chara = input('type the character you wish to set and press enter twice.')
        input_that_restarts = input()
    if input_that_restarts == 'unlock chara':
        perma_chara = ''
        input_that_restarts = input()
    if input_that_restarts == 'lock outfit':
        perma_outfit = 'true'
        perma_top_style = top_style
        perma_top_color = top_color
        perma_top_pattern = top_pattern
        perma_top_logo = top_logo
        perma_top_type_cas = top_type_cas
        perma_top_type_form = top_type_form
        perma_top_type_dress = top_type_dress
        perma_top_type_spe = top_type_spe
        perma_dress_sleeve_length = dress_sleeve_length
        perma_jacket_logo  = jacket_logo
        perma_jacket_color = jacket_color
        perma_jacket_pattern = jacket_pattern
        perma_jacket_style = jacket_style
        perma_jacket_type_cas = jacket_type_cas
        perma_jacket_type_form = jacket_type_form
        perma_jacket_type_dress = jacket_type_dress
        perma_bottom_type_cas = bottom_type_cas
        perma_bottom_type_form = bottom_type_form            
        perma_skirt_length = skirt_length
        perma_skirt_fold = skirt_fold
        perma_bottom_pattern = bottom_pattern
        perma_bottom_color = bottom_color
        perma_shoe_type_cas = shoe_type_cas
        perma_shoe_type_form = shoe_type_form
        perma_shoe_type_spe = shoe_type_spe
        perma_shoe_color = shoe_color
        perma_heel_type = heel_type
        input_that_restarts = input()
    if input_that_restarts == 'unlock outfit':
        perma_outfit = ''
        input_that_restarts = input()

