ENCYCLOPEDIAS_FOLDER = "encyclopedias/"
PAGE_NUMBER_STRING = "page_number="
INDEX_STRING = "index="
BASE_URL = "https://runeberg.org/nf"
# base_url = "http://runeberg.org/download.pl?mode=ocrtext&work=nf"
INF = 10**9
MAX_ENTRY_LENGTH = 200
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖÜ"

#the ranges for the urls, they have a slightly weird format

edition1_url_range = {
    'a': "abcdefghijklmnopqr",
}

edition2_url_range = {
    'b': "abcdefghijklmnopqrst",
    'c': "abcdefghijklmn",
}

#the start and end pages for each volume
edition1_volume_start_end = {
    "aa": (9, 1579),
    "ab": (9, 800),
    "ac": (7, 798),
    "ad": (7, 797),
    "ae": (7, 798),
    "af": (5, 795),
    "ag": (7, 798),
    "ah": (5, 799),
    "ai": (7, 798),
    "aj": (7, 798),
    "ak": (7, 798),
    "al": (7, 798),
    "am": (7, 798),
    "an": (7, 798),
    "ao": (7, 798),
    "ap": (7, 826),
    "aq": (5, 804),
    "ar": (3, 403),
}

#the pages where the lookup letter changes
edition1_volume_letters = {
    "aa": [(["A"], 1383), (["B"], INF)],
    "ab": [(["B"], 751), (["C"], INF)], 
    "ac": [(["C"], 369), (["D"], INF)],
    "ad": [(["D"], 58), (["E"], 464), (["F"], INF)],
    "ae": [(["F"], 380), (["G"], INF)],
    "af": [(["G"], 220), (["H"], INF)],
    "ag": [(["H"], 196), (["I"], 489), (["J"], 778), (["K"], INF)],
    "ah": [(["K"], INF)], 
    "ai": [(["K"], 232), (["L"], INF)], 
    "aj": [(["L"], 255), (["M"], INF)],
    "ak": [(["M"], 380), (["N"], INF)],
    "al": [(["N"], 30), (["O"], 277), (["P"], INF)],
    "am": [(["P"], 262), (["Q"], 306), (["R"], INF)],
    "an": [(["R"], 147), (["S"], INF)],
    "ao": [(["S"], 641), (["T"], INF)],
    "ap": [(["T"], 625), (["U", "Ü"], INF)], #special case for Ü
    "aq": [(["V", "W"], INF)], #special case with W
    "ar": [(["V", "W"], 35), (["X"], 42), (["Y"], 78), (["Z"], 178), (["Å"], 243), (["Ä"], 277), (["Ö"], INF)] #special case with W
}

#the start and end pages for each volume
edition2_volume_start_end = {
    "ba": (13, 824),
    "bb": (13, 798),
    "bc": (17, 808),
    "bd": (17, 814),
    "be": (17, 800),
    "bf": (17, 814),
    "bg": (17, 802),
    "bh": (17, 806),
    "bi": (17, 782),
    "bj": (17, 804),
    "bk": (17, 784),
    "bl": (17, 816),
    "bm": (17, 784),
    "bn": (17, 784),
    "bo": (17, 788),
    "bp": (17, 812),
    "bq": (17, 785),
    "br": (17, 779),
    "bs": (17, 820),
    "bt": (17, 796),
    "ca": (17, 812),
    "cb": (17, 778),
    "cc": (17, 817),
    "cd": (17, 784),
    "ce": (17, 794),
    "cf": (17, 820),
    "cg": (17, 806),
    "ch": (17, 688),
    "ci": (17, 458),
    "cj": (17, 719),
    "ck": (17, 688),
    "cl": (17, 686),
    "cm": (17, 685),
    "cn": (17, 180),
}

#the pages where the lookup letter changes
edition2_volume_letters = {
    "ba": [(["A"], INF)],
    "bb": [(["A"], 310), (["B"], INF)],
    "bc": [(["B"], INF)],
    "bd": [(["B"], 519), (["C"], INF)],
    "be": [(["C"], 558), (["D"], INF)],
    "bf": [(["D"], 678), (["E"], INF)],
    "bg": [(["E"], 651), (["F"], INF)],
    "bh": [(["F"], INF)],
    "bi": [(["F"], 281), (["G"], INF)],
    "bj": [(["G"], 506), (["H"], INF)],
    "bk": [(["H"], INF)],
    "bl": [(["H"], 180), (["I"], 611), (["J"], INF)],
    "bm": [(["J"], 275), (["K"], INF)],
    "bn": [(["K"], INF)],
    "bo": [(["K"], 385), (["L"], INF)],
    "bp": [(["L"],  INF)],
    "bq": [(["L"], 180), (["M"], INF)],
    "br": [(["M"], INF)],
    "bs": [(["M"], 213), (["N"], INF)],
    "bt": [(["N"], 213), (["O"], 641), (["P"], INF)],
    "ca": [(["P"], INF)],
    "cb": [(["P"], 385), (["Q"], 418), (["R"], INF)],
    "cc": [(["R"], INF)],
    "cd": [(["R"], 136), (["S"], INF)],
    "ce": [(["S"], INF)],
    "cf": [(["S"], INF)],
    "cg": [(["S"], INF)],
    "ch": [(["S"], 138), (["T"], INF)],
    "ci": [(["T"], INF)],
    "cj": [(["T"], 441), (["U"], INF)],
    "ck": [(["U"], 116), (["V"], INF)],
    "cl": [(["V", "W"], INF)], #Special case with W
    "cm": [(["V", "W"], 281), (["X"], 291), (["Y"], 357), (["Z"], 488), (["Å"], 619), (["Ä"], INF)], #special case with W?
    "cn": [(["Ö"], INF)]
}

edition1_volumes = edition1_volume_start_end.keys()
edition2_volumes = edition2_volume_start_end.keys()

edition1_first_letter_list = ['a']
edition2_first_letter_list = ['b', 'c']

#folder to save the .txt files in
folder_edition1 = ENCYCLOPEDIAS_FOLDER + "first/"
folder_edition2 = ENCYCLOPEDIAS_FOLDER + "second/"

folder_evaluations = "evaluations/"

def clean_html_markup(s: str, html_entities: list) -> str:
    res = s
    for pair in html_entities:
        res = res.replace(pair[0], pair[1])
    return res
