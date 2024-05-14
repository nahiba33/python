def samitleri_al(cumle):
    saitler = ["a", "0", "u", "ü", "ö", "i", "ı", "e", "ə"]
    samitler = set()
    return {herf for herf in cumle if herf.lower() not in saitler and herf.isalpha() and herf.lower() not in samitler}