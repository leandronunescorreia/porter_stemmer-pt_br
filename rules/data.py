plural_rules = [
        ("ns", 1, "m"),
        ("ões", 3, "ão"),
        ("ões", 2, "ão"),## personal addition
        ("ães", 1, "ão"),
        ("ais", 1, "al"),
        ("éis", 2, "el"),
        ("eis", 2, "el"),
        ("eis", 1, "ei"),## personal addition
        ("óis", 2, "ol"),
        ("is", 2, "il"),
        ("les", 3, "l"),
        ("res", 2, "r"),
        ("s", 2, ""),
    ]

feminine_rules = [
        ("ona",     3, "ão"),
        ("ora",     3, "or"),
        ("na",      4, "no"),
        ("da",      2, "do"),## personal addition
        ("ca",      2, "co"),## personal addition
        ("va",      2, "vo"),## personal addition
        ("inha",    3, "inho"),
        ("esa",     3, "ês"),
        ("osa",     3, "oso"),
        ("iaca",    3, "iaco"),
        ("ica",     3, "ico"),
        ("ada",     2, "ado"),
        ("ida",     3, "ido"),
        ("ída",     3, "ido"),
        ("ima",     3, "imo"),
        ("iva",     3, "ivo"),
        ("iera",    2, "eiro"),
        ("ã",       2, "ão"),
        ("ia",      5, "io"),## personal addition
        ("ista",    5, "ista"),## personal addition
        ("eira",    5, "eiro"),## personal addition
        ("riz",    2, "or"),## personal addition
        ("oa",    2, "ão"),## personal addition
    ]


augmentative_rules = [
    ('díssimo', 5, ''),
    ('abilíssimo',5, ''),
    ('íssimo', 4, ''),
    ('issimo', 3, ''),
    ('ésimo',  3, ''),
    ('érrimo', 4, ''),
    ('zinho', 2, ''),
    ('quinho', 4, 'co'),
    ('uinho', 4, ''),
    ('adinho', 3, ''),
    ('inho', 3, ''),
    ('alhão', 4, ''),
    ('uça',  4, ''),
    ('aço',  4, ''),
    ('aça',  4, ''),
    ('adão', 4, 'cidadão'),
    ('idão', 4, ''),
    ('ázio', 3, ''),
    ('arraz',4, ''),
    ('zarrão', 3, ''),
    ('arrão', 4, ''),
    ('arra', 3, ''),
    ('zão', 2, ''),
    ('ão', 3, ''),
    ("acho", 2, 'o')
]



nominative_rules = [
        ("encialista", 4, ""),
        ("alista", 5, ""),
        ("agem", 3, ""),
        ("iamento", 4, ""),
        ("amento", 3, ""),
        ("imento", 3, ""),
        ("mento", 6, ""),
        ("alizado", 4, ""),
        ("atizado", 4, ""),
        ("tizado", 4, ""),
        ("izado", 5, ""),
        ("ativo", 4, ""),
        ("tivo", 4, ""),
        ("ivo", 4, ""),
        ("ado", 2, ""),
        ("ido", 3, ""),
        ("ador", 3, ""),
        ("edor", 3, ""),
        ("idor", 4, ""),
        ("dor", 4, ""),
        ("sor", 4, ""),
        ("atoria", 5, ""),
        ("oria", 4, ""),
        ("tor", 4, ""),
        ("or", 2, ""),
        ("abilidade", 5, ""), 
        ("idade", 5, ""), 
        ("icionista", 4, ""),
        ("cionista", 5, ""),
        ("ionista", 5, ""),
        ("ionar", 5, ""),
        ("ional", 4, ""),
        ("ência", 3, ""),
        ("ância", 4, ""),
        ("edouro", 3, ""),
        ("queiro", 3, ""),
        ("adeiro", 4, ""),
        ("eiro", 3, ""),
        ("uoso", 3, ""),
        ("oso", 3, ""), 
        ("alizaç", 5, ""),
        ("atizaç", 5, ""),
        ("tizaç", 5, ""),
        # ("ização", 6, ""),
        ("ção", 6, ""),
        ("aç", 3, ""),
        ("iç", 3, ""),
        ("ário", 3, ""),
        ("atório", 3, ""),
        ("rio", 5, ""),
        ("ério", 6, ""),
        ("ês", 4, ""),
        ("eza", 3, ""),
        ("ez", 4, ""),
        ("esco", 4, ""),
        ("ante", 2, ""), 
        ("ástico", 4, ""),
        ("alístico", 3, ""),
        ("áutico", 4, ""),
        ("êutico", 4, ""),
        ("tico", 3, ""),
        ("ade", 4, ""),
        ("ável", 2, "")
]

