def samitleri_al(cumle):
    saitler = {"a", "0", "u", "ü", "ö", "i", "ı", "e", "ə"}
    print("Samitler: ",{herf for herf in cumle if herf.lower() not in saitler and herf.isalpha()})