import random
import numpy as np



def gen_rand_dna(length=None):
    d = ("A","T","G","C")
    if not length:
        length = 16
    res = "".join([random.choice(d) for i in range(length)])
    return res


def gen_V_segment(length=None):
    """у человека - примерно 45 штук по 280-320 бп"""

    if not length:
        length = random.randint(280, 320)
    else:
        length = random.randint(length-int(length*0.9), length-int(length*0.9))
    print(f"gen_V_segment: length={length}")
    return gen_rand_dna(length)


def gen_D_segment(length=None):
    """у человека - примерно 23 штук по 10-37 бп"""

    if not length:
        length = random.randint(10, 37)
    print(f"gen_D_segment: length={length}")
    return gen_rand_dna(length)

def gen_J_segment(length=None):
    """у человека - примерно 6 штук по 40-60 бп"""

    if not length:
        length = random.randint(40, 60)
    print(f"gen_J_segment: length={length}")
    return gen_rand_dna(length)

# Игрушечные сегменты (длины приближены к реальным)
V_segments = [
    "ATGGAGTCTGGGGGAGGCTTGGTACAGCCTGG",
    "ATGGACTGGACCTGGAGGATCCTGGG",
    "ATGAACTGGGTCCGAGGGTCTC"
]



D_segments = [
    "GGGACAGGG",
    "GATCTGGT",
    "GGGTT"
]

J_segments = [
    "TTACTACTACTAC",
    "TTACGGTAGTAG",
    "TACTACTGG"
]

# Веса (НЕравномерность использования)
V_weights = [0.5, 0.3, 0.2]
D_weights = [0.6, 0.3, 0.1]
J_weights = [0.5, 0.3, 0.2]



def chew(seq, max_chew=10):
    """Экзонуклеазная обрезка"""
    chew_left = random.randint(0, min(max_chew, len(seq)//3))
    chew_right = random.randint(0, min(max_chew, len(seq)//3))
    return seq[chew_left:len(seq)-chew_right]

def add_P():
    """P-нуклеотиды (палиндромы, редко)"""
    if random.random() < 0.3:
        k = random.randint(1, 3)
        bases = random.choices("ACGT", k=k)
        return "".join(bases + bases[::-1])
    return ""

def add_N():
    """N-нуклеотиды (TdT, GC bias)"""
    length = np.random.geometric(p=0.2) - 1  # 0–~20
    bases = random.choices(
        ["G", "C", "A", "T"],
        weights=[0.35, 0.35, 0.15, 0.15],
        k=length
    )
    return "".join(bases)




def generate_vdj():
    V = random.choices(V_segments, weights=V_weights)[0]
    D = random.choices(D_segments, weights=D_weights)[0]
    J = random.choices(J_segments, weights=J_weights)[0]

    V = chew(V)
    D = chew(D)
    J = chew(J)

    vd = V + add_P() + add_N() + D
    dj = add_P() + add_N() + J

    return vd + dj


def generate_vdj_v2():
    """generate V D J fragments instead of mocks"""
    V_segments = [gen_V_segment() for i in range(3)]
    D_segments = [gen_D_segment() for i in range(3)]
    J_segments = [gen_J_segment() for i in range(3)]
    V = random.choices(V_segments, weights=V_weights)[0]
    D = random.choices(D_segments, weights=D_weights)[0]
    J = random.choices(J_segments, weights=J_weights)[0]

    V = chew(V)
    D = chew(D)
    J = chew(J)

    vd = V + add_P() + add_N() + D
    dj = add_P() + add_N() + J

    return vd + dj



if __name__ == "__main__":
    print("testing generate_vdj:")
    repertoire = [generate_vdj() for _ in range(10)]

    for seq in repertoire:
        print(len(seq), seq)

    print("#"*50 + "\n\n")
    print("testing generate_vdj_v2:")
    repertoire = [generate_vdj_v2() for _ in range(10)]

    for seq in repertoire:
        print(len(seq), seq)
