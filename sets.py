import random

sets = {}

# TARGET SETS

sets['male_names'] = ['john', 'paul', 'mike', 'kevin', 'steve', 'greg', 'jeff', 'bill']
sets['female_names'] = ['amy', 'joan', 'lisa', 'sarah', 'diana', 'kate', 'ann', 'donna']
sets['male_terms'] = ['male', 'man', 'boy', 'brother', 'he', 'him', 'his', 'son', 'father', 'uncle', 'grandfather']
sets['female_terms'] = ['female', 'woman', 'girl', 'sister', 'she', 'her', 'hers', 'daughter', 'mother', 'aunt', 'grandmother']
sets['male'] = sets['male_terms'] + sets['male_names']
sets['female'] = sets['female_terms'] + sets['female_names']

sets['white_names'] = ['adam', 'chip', 'harry', 'josh', 'roger', 'alan', 'frank', 'ian', 'justin', 'ryan', 'andrew', 'fred', 'jack', 'matthew', 'stephen', 'brad', 'greg', 'jed', 'paul', 'todd', 'brandon', 'hank', 'jonathan', 'peter', 'wilbur', 'amanda', 'courtney', 'heather', 'melanie', 'sara', 'amber', 'crystal', 'katie', 'meredith', 'shannon', 'betsy', 'donna', 'kristin', 'nancy', 'stephanie', 'bobbie-sue', 'ellen', 'lauren', 'peggy', 'sue-ellen', 'colleen', 'emily', 'megan', 'rachel', 'wendy', 'brendan', 'geoffrey', 'brett', 'jay', 'neil', 'anne', 'carrie', 'jill', 'laurie', 'kristen', 'sarah']
sets['black_names'] = ['alonzo', 'jamel', 'lerone', 'percell', 'theo', 'alphonse', 'jerome', 'leroy', 'rasaan', 'torrance', 'darnell', 'lamar', 'lionel', 'rashaun', 'tyree', 'deion', 'lamont', 'malik', 'terrence', 'tyrone', 'everol', 'lavon', 'marcellus', 'terryl', 'wardell', 'aiesha', 'lashelle', 'nichelle', 'shereen', 'temeka', 'ebony', 'latisha', 'shaniqua', 'tameisha', 'teretha', 'jasmine', 'latonya', 'shanise', 'tanisha', 'tia', 'lakisha', 'latoya', 'sharise', 'tashika', 'yolanda', 'lashandra', 'malika', 'shavonn', 'tawanda', 'yvette', 'hakim', 'jermaine', 'kareem', 'jamal', 'rasheed', 'aisha', 'keisha', 'kenya', 'tamika']

sets['christianity_words'] = ['baptism', 'messiah', 'catholicism', 'resurrection', 'christianity', 'salvation', 'protestant', 'gospel', 'trinity', 'jesus', 'christ', 'christian', 'cross', 'catholic', 'church']
sets['islam_words'] = ['allah', 'ramadan', 'turban', 'emir', 'salaam', 'sunni', 'koran', 'imam', 'sultan', 'prophet', 'veil', 'ayatollah', 'shiite', 'mosque', 'islam', 'sheik', 'muslim', 'muhammad']
sets['atheism_words'] = ['atheism', 'atheist', 'atheistic', 'heliocentric', 'evolution', 'darwin', 'galilei', 'agnostic', 'agnosticism', 'pagan', 'science', 'disbelief', 'scepticism', 'philosophy', 'university', 'kopernikus']

# ATTRIBUTE SETS

sets['pleasant'] = ['caress', 'freedom', 'health', 'love', 'peace', 'cheer', 'friend', 'heaven', 'loyal', 'pleasure', 'diamond', 'gentle', 'honest', 'lucky', 'rainbow', 'diploma', 'gift', 'honor', 'miracle', 'sunrise', 'family', 'happy', 'laughter', 'paradise', 'vacation', 'joy', 'wonderful']
sets['unpleasant'] = ['abuse', 'crash', 'filth', 'murder', 'sickness', 'accident', 'death', 'grief', 'poison', 'stink', 'assault', 'disaster', 'hatred', 'pollute', 'tragedy', 'divorce', 'jail', 'poverty', 'ugly', 'cancer', 'kill', 'rotten', 'vomit', 'agony', 'prison', 'terrible', 'horrible', 'nasty', 'evil', 'war', 'awful', 'failure']

sets['science'] = ['math', 'algebra', 'geometry', 'calculus', 'equations', 'computation', 'numbers', 'addition', 'science', 'technology', 'physics', 'chemistry', 'einstein', 'nasa', 'experiment', 'astronomy']
sets['art'] = ['poetry', 'art', 'dance', 'literature', 'novel', 'symphony', 'drama', 'sculpture', 'shakespeare']

sets['intellectual_words'] = ['precocious', 'resourceful', 'inquisitive', 'sagacious', 'inventive', 'astute', 'adaptable', 'reflective', 'discerning', 'intuitive', 'inquiring', 'judicious', 'analytical', 'luminous', 'venerable', 'imaginative', 'shrewd', 'thoughtful', 'sage', 'smart', 'ingenious', 'clever', 'brilliant', 'logical', 'intelligent', 'apt', 'genius', 'wise']
sets['appearance_words'] = ['alluring', 'voluptuous', 'blushing', 'homely', 'plump', 'sensual', 'gorgeous', 'slim', 'bald', 'athletic', 'fashionable', 'stout', 'ugly', 'muscular', 'slender', 'feeble', 'handsome', 'healthy', 'attractive', 'fat', 'weak', 'thin', 'pretty', 'beautiful', 'strong']
sets['intellectual_words'] += ['stupid', 'dumb', 'dull', 'clumsy', 'foolish', 'naive', 'unintelligent', 'trivial', 'unwise', 'idiotic']
random.Random(0).shuffle(sets['intellectual_words'])    

sets['career'] = ['executive', 'management', 'professional', 'corporation', 'salary', 'office', 'business', 'career']
sets['family'] = ['home', 'parents', 'children', 'family', 'cousins', 'marriage', 'wedding', 'relatives']
