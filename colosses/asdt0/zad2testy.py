import random
from typing import List, Tuple


class Node:
    def __init__(self, left=None, leftval=0, right=None, rightval=0):
        self.left = left  # lewe podrzewo
        self.leftval = leftval  # wartość krawędzi do lewego poddrzewa jeśli istnieje
        self.right = right  # prawe poddrzewo
        self.rightval = rightval  # wartość krawędzi do prawego poddrzewa jeśli istnieje
        self.X = None  # miejsce na dodatkowe dane

    def __str__(self):
        return self._mkstr(level=0)

    def _mkstr(self, level=0):
        if self.left == None and self.right == None:
            return "Node()"
        prefix = "\t" * (level + 1)
        return f"""Node(leftval={self.leftval}, rightval={self.rightval},
{prefix}left={self.left._mkstr(level=level + 1) if self.left else None},
{prefix}right={self.right._mkstr(level=level + 1) if self.right else None})"""


def make_tree_1():
    A = Node()
    B = Node()
    C = Node()
    D = Node()
    E = Node()
    F = Node()
    G = Node()
    A.left = B
    A.right = E
    B.left = D
    B.right = C
    C.left = F
    C.right = G
    A.leftval = 1
    A.rightval = 5
    B.leftval = 6
    B.rightval = 2
    C.leftval = 8
    C.rightval = 10
    return A, 3, 20


def make_tree_2():
    T = Node(
        right=Node(),
        rightval=2
    )
    return T, 1, 2


def make_tree_3():
    T = Node(leftval=517, rightval=143,
             left=Node(leftval=598, rightval=914,
                       left=Node(leftval=0, rightval=941,
                                 left=None,
                                 right=Node(leftval=415, rightval=0,
                                            left=Node(),
                                            right=None)),
                       right=Node(leftval=367, rightval=0,
                                  left=Node(),
                                  right=None)),
             right=Node())
    return T, 1, 941


def make_tree_4():
    max_edge = 100
    T = Node(leftval=1, rightval=2,
             left=Node(leftval=3, rightval=4,
                       left=Node(leftval=0, rightval=max_edge,
                                 left=None,
                                 right=Node()
                                 # right=Node(leftval=5, rightval=0,
                                 #            left=Node(),
                                 #            right=None)
                                 ),
                       right=Node(leftval=6, rightval=0,
                                  left=Node(),
                                  right=None)),
             right=Node())
    return T, 1, max_edge


def make_tree_5():
    max_edge = 100
    T = Node(leftval=1, rightval=2,
             left=Node(leftval=3, rightval=4,
                       left=Node(leftval=0, rightval=max_edge,
                                 left=None,
                                 right=Node()),
                       right=None),
             right=Node())
    return T, 1, max_edge


def make_tree_6():
    max_edge = 100
    T = Node(leftval=3, rightval=4,
             left=Node(leftval=0, rightval=max_edge,
                       left=None,
                       right=Node()),
             right=None)
    return T, 1, max_edge


def make_tree_7():
    max_edge = 100
    T = Node(leftval=3, rightval=4,
             left=Node(leftval=0, rightval=max_edge,
                       left=None,
                       right=Node()),
             right=None)
    return T, 2, max_edge + 3


def make_tree_8():
    T = Node(leftval=185, rightval=63,
             left=Node(leftval=189, rightval=0,
                       left=Node(leftval=248, rightval=298,
                                 left=Node(leftval=804, rightval=685,
                                           left=Node(),
                                           right=Node(leftval=728, rightval=845,
                                                      left=Node(leftval=210, rightval=0,
                                                                left=Node(leftval=656, rightval=935,
                                                                          left=Node(leftval=98, rightval=634,
                                                                                    left=Node(leftval=598, rightval=0,
                                                                                              left=Node(),
                                                                                              right=None),
                                                                                    right=Node(leftval=0, rightval=774,
                                                                                               left=None,
                                                                                               right=Node(leftval=0,
                                                                                                          rightval=144,
                                                                                                          left=None,
                                                                                                          right=Node()))),
                                                                          right=Node(leftval=324, rightval=626,
                                                                                     left=Node(leftval=871,
                                                                                               rightval=701,
                                                                                               left=Node(),
                                                                                               right=Node(leftval=0,
                                                                                                          rightval=921,
                                                                                                          left=None,
                                                                                                          right=Node())),
                                                                                     right=Node(leftval=363,
                                                                                                rightval=445,
                                                                                                left=Node(),
                                                                                                right=Node()))),
                                                                right=None),
                                                      right=Node(leftval=861, rightval=409,
                                                                 left=Node(leftval=562, rightval=0,
                                                                           left=Node(leftval=825, rightval=941,
                                                                                     left=Node(),
                                                                                     right=Node()),
                                                                           right=None),
                                                                 right=Node(leftval=0, rightval=737,
                                                                            left=None,
                                                                            right=Node())))),
                                 right=Node(leftval=590, rightval=0,
                                            left=Node(leftval=0, rightval=325,
                                                      left=None,
                                                      right=Node(leftval=818, rightval=395,
                                                                 left=Node(leftval=987, rightval=819,
                                                                           left=Node(leftval=561, rightval=341,
                                                                                     left=Node(leftval=228,
                                                                                               rightval=245,
                                                                                               left=Node(),
                                                                                               right=Node(leftval=582,
                                                                                                          rightval=0,
                                                                                                          left=Node(
                                                                                                              leftval=0,
                                                                                                              rightval=940,
                                                                                                              left=None,
                                                                                                              right=Node()),
                                                                                                          right=None)),
                                                                                     right=Node(leftval=128, rightval=0,
                                                                                                left=Node(leftval=299,
                                                                                                          rightval=724,
                                                                                                          left=Node(),
                                                                                                          right=Node(
                                                                                                              leftval=0,
                                                                                                              rightval=565,
                                                                                                              left=None,
                                                                                                              right=Node(
                                                                                                                  leftval=0,
                                                                                                                  rightval=309,
                                                                                                                  left=None,
                                                                                                                  right=Node(
                                                                                                                      leftval=112,
                                                                                                                      rightval=0,
                                                                                                                      left=Node(),
                                                                                                                      right=None)))),
                                                                                                right=None)),
                                                                           right=Node()),
                                                                 right=Node(leftval=611, rightval=0,
                                                                            left=Node(leftval=94, rightval=0,
                                                                                      left=Node(),
                                                                                      right=None),
                                                                            right=None))),
                                            right=None)),
                       right=None),
             right=Node(leftval=359, rightval=447,
                        left=Node(leftval=604, rightval=846,
                                  left=Node(leftval=0, rightval=488,
                                            left=None,
                                            right=Node()),
                                  right=Node(leftval=917, rightval=696,
                                             left=Node(),
                                             right=Node(leftval=870, rightval=221,
                                                        left=Node(leftval=538, rightval=283,
                                                                  left=Node(),
                                                                  right=Node(leftval=0, rightval=723,
                                                                             left=None,
                                                                             right=Node(leftval=0, rightval=858,
                                                                                        left=None,
                                                                                        right=Node()))),
                                                        right=Node()))),
                        right=Node(leftval=663, rightval=309,
                                   left=Node(leftval=119, rightval=38,
                                             left=Node(leftval=588, rightval=650,
                                                       left=Node(leftval=750, rightval=0,
                                                                 left=Node(leftval=249, rightval=17,
                                                                           left=Node(leftval=628, rightval=0,
                                                                                     left=Node(leftval=333, rightval=0,
                                                                                               left=Node(),
                                                                                               right=None),
                                                                                     right=None),
                                                                           right=Node(leftval=0, rightval=195,
                                                                                      left=None,
                                                                                      right=Node(leftval=866,
                                                                                                 rightval=0,
                                                                                                 left=Node(),
                                                                                                 right=None))),
                                                                 right=None),
                                                       right=Node(leftval=47, rightval=837,
                                                                  left=Node(leftval=0, rightval=341,
                                                                            left=None,
                                                                            right=Node(leftval=175, rightval=0,
                                                                                       left=Node(leftval=0,
                                                                                                 rightval=814,
                                                                                                 left=None,
                                                                                                 right=Node()),
                                                                                       right=None)),
                                                                  right=Node(leftval=225, rightval=0,
                                                                             left=Node(leftval=0, rightval=715,
                                                                                       left=None,
                                                                                       right=Node(leftval=0,
                                                                                                  rightval=876,
                                                                                                  left=None,
                                                                                                  right=Node())),
                                                                             right=None))),
                                             right=Node(leftval=380, rightval=854,
                                                        left=Node(leftval=0, rightval=590,
                                                                  left=None,
                                                                  right=Node(leftval=0, rightval=851,
                                                                             left=None,
                                                                             right=Node(leftval=0, rightval=621,
                                                                                        left=None,
                                                                                        right=Node()))),
                                                        right=Node(leftval=0, rightval=94,
                                                                   left=None,
                                                                   right=Node()))),
                                   right=Node(leftval=74, rightval=0,
                                              left=Node(leftval=0, rightval=227,
                                                        left=None,
                                                        right=Node(leftval=267, rightval=72,
                                                                   left=Node(leftval=0, rightval=745,
                                                                             left=None,
                                                                             right=Node(leftval=0, rightval=216,
                                                                                        left=None,
                                                                                        right=Node())),
                                                                   right=Node(leftval=0, rightval=856,
                                                                              left=None,
                                                                              right=Node(leftval=104, rightval=0,
                                                                                         left=Node(leftval=0,
                                                                                                   rightval=636,
                                                                                                   left=None,
                                                                                                   right=Node()),
                                                                                         right=None)))),
                                              right=None))))
    return T, 99, 50225


def make_tree_9_999_too_big():
    T = Node(leftval=-231, rightval=-826,
             left=Node(leftval=338, rightval=837,
                       left=Node(leftval=-146, rightval=970,
                                 left=Node(leftval=-390, rightval=304,
                                           left=Node(leftval=139, rightval=62,
                                                     left=Node(leftval=90, rightval=444,
                                                               left=Node(leftval=826, rightval=0,
                                                                         left=Node(leftval=-267, rightval=194,
                                                                                   left=Node(),
                                                                                   right=Node()),
                                                                         right=None),
                                                               right=Node(leftval=-487, rightval=863,
                                                                          left=Node(),
                                                                          right=Node(leftval=266, rightval=637,
                                                                                     left=Node(),
                                                                                     right=Node()))),
                                                     right=Node(leftval=-800, rightval=-194,
                                                                left=Node(leftval=-475, rightval=-727,
                                                                          left=Node(leftval=-406, rightval=-624,
                                                                                    left=Node(leftval=-609,
                                                                                              rightval=878,
                                                                                              left=Node(leftval=146,
                                                                                                        rightval=0,
                                                                                                        left=Node(
                                                                                                            leftval=0,
                                                                                                            rightval=-34,
                                                                                                            left=None,
                                                                                                            right=Node()),
                                                                                                        right=None),
                                                                                              right=Node(leftval=782,
                                                                                                         rightval=-872,
                                                                                                         left=Node(),
                                                                                                         right=Node(
                                                                                                             leftval=-334,
                                                                                                             rightval=441,
                                                                                                             left=Node(
                                                                                                                 leftval=123,
                                                                                                                 rightval=875,
                                                                                                                 left=Node(
                                                                                                                     leftval=0,
                                                                                                                     rightval=-94,
                                                                                                                     left=None,
                                                                                                                     right=Node()),
                                                                                                                 right=Node(
                                                                                                                     leftval=881,
                                                                                                                     rightval=0,
                                                                                                                     left=Node(
                                                                                                                         leftval=648,
                                                                                                                         rightval=0,
                                                                                                                         left=Node(),
                                                                                                                         right=None),
                                                                                                                     right=None)),
                                                                                                             right=Node(
                                                                                                                 leftval=0,
                                                                                                                 rightval=495,
                                                                                                                 left=None,
                                                                                                                 right=Node(
                                                                                                                     leftval=0,
                                                                                                                     rightval=-501,
                                                                                                                     left=None,
                                                                                                                     right=Node(
                                                                                                                         leftval=-318,
                                                                                                                         rightval=0,
                                                                                                                         left=Node(
                                                                                                                             leftval=776,
                                                                                                                             rightval=0,
                                                                                                                             left=Node(
                                                                                                                                 leftval=0,
                                                                                                                                 rightval=695,
                                                                                                                                 left=None,
                                                                                                                                 right=Node()),
                                                                                                                             right=None),
                                                                                                                         right=None)))))),
                                                                                    right=Node(leftval=178,
                                                                                               rightval=-505,
                                                                                               left=Node(leftval=-777,
                                                                                                         rightval=-383,
                                                                                                         left=Node(),
                                                                                                         right=Node(
                                                                                                             leftval=2,
                                                                                                             rightval=0,
                                                                                                             left=Node(
                                                                                                                 leftval=910,
                                                                                                                 rightval=0,
                                                                                                                 left=Node(
                                                                                                                     leftval=0,
                                                                                                                     rightval=40,
                                                                                                                     left=None,
                                                                                                                     right=Node(
                                                                                                                         leftval=0,
                                                                                                                         rightval=792,
                                                                                                                         left=None,
                                                                                                                         right=Node())),
                                                                                                                 right=None),
                                                                                                             right=None)),
                                                                                               right=Node(leftval=-351,
                                                                                                          rightval=0,
                                                                                                          left=Node(
                                                                                                              leftval=634,
                                                                                                              rightval=-212,
                                                                                                              left=Node(
                                                                                                                  leftval=0,
                                                                                                                  rightval=235,
                                                                                                                  left=None,
                                                                                                                  right=Node(
                                                                                                                      leftval=637,
                                                                                                                      rightval=0,
                                                                                                                      left=Node(
                                                                                                                          leftval=973,
                                                                                                                          rightval=0,
                                                                                                                          left=Node(),
                                                                                                                          right=None),
                                                                                                                      right=None)),
                                                                                                              right=Node(
                                                                                                                  leftval=221,
                                                                                                                  rightval=0,
                                                                                                                  left=Node(
                                                                                                                      leftval=-813,
                                                                                                                      rightval=0,
                                                                                                                      left=Node(),
                                                                                                                      right=None),
                                                                                                                  right=None)),
                                                                                                          right=None))),
                                                                          right=Node(leftval=-763, rightval=764,
                                                                                     left=Node(leftval=-794,
                                                                                               rightval=603,
                                                                                               left=Node(leftval=0,
                                                                                                         rightval=891,
                                                                                                         left=None,
                                                                                                         right=Node(
                                                                                                             leftval=795,
                                                                                                             rightval=-694,
                                                                                                             left=Node(
                                                                                                                 leftval=-817,
                                                                                                                 rightval=0,
                                                                                                                 left=Node(),
                                                                                                                 right=None),
                                                                                                             right=Node())),
                                                                                               right=Node(leftval=670,
                                                                                                          rightval=-873,
                                                                                                          left=Node(),
                                                                                                          right=Node(
                                                                                                              leftval=-319,
                                                                                                              rightval=-128,
                                                                                                              left=Node(
                                                                                                                  leftval=-445,
                                                                                                                  rightval=0,
                                                                                                                  left=Node(
                                                                                                                      leftval=-967,
                                                                                                                      rightval=498,
                                                                                                                      left=Node(
                                                                                                                          leftval=-764,
                                                                                                                          rightval=-4,
                                                                                                                          left=Node(
                                                                                                                              leftval=8,
                                                                                                                              rightval=352,
                                                                                                                              left=Node(),
                                                                                                                              right=Node(
                                                                                                                                  leftval=-78,
                                                                                                                                  rightval=0,
                                                                                                                                  left=Node(),
                                                                                                                                  right=None)),
                                                                                                                          right=Node(
                                                                                                                              leftval=254,
                                                                                                                              rightval=0,
                                                                                                                              left=Node(
                                                                                                                                  leftval=-336,
                                                                                                                                  rightval=0,
                                                                                                                                  left=Node(),
                                                                                                                                  right=None),
                                                                                                                              right=None)),
                                                                                                                      right=Node(
                                                                                                                          leftval=-503,
                                                                                                                          rightval=0,
                                                                                                                          left=Node(),
                                                                                                                          right=None)),
                                                                                                                  right=None),
                                                                                                              right=Node(
                                                                                                                  leftval=0,
                                                                                                                  rightval=-651,
                                                                                                                  left=None,
                                                                                                                  right=Node(
                                                                                                                      leftval=0,
                                                                                                                      rightval=627,
                                                                                                                      left=None,
                                                                                                                      right=Node()))))),
                                                                                     right=Node(leftval=638,
                                                                                                rightval=622,
                                                                                                left=Node(leftval=324,
                                                                                                          rightval=-384,
                                                                                                          left=Node(
                                                                                                              leftval=0,
                                                                                                              rightval=-242,
                                                                                                              left=None,
                                                                                                              right=Node(
                                                                                                                  leftval=-199,
                                                                                                                  rightval=-813,
                                                                                                                  left=Node(
                                                                                                                      leftval=0,
                                                                                                                      rightval=179,
                                                                                                                      left=None,
                                                                                                                      right=Node(
                                                                                                                          leftval=0,
                                                                                                                          rightval=700,
                                                                                                                          left=None,
                                                                                                                          right=Node(
                                                                                                                              leftval=0,
                                                                                                                              rightval=241,
                                                                                                                              left=None,
                                                                                                                              right=Node()))),
                                                                                                                  right=Node())),
                                                                                                          right=Node(
                                                                                                              leftval=-548,
                                                                                                              rightval=-853,
                                                                                                              left=Node(),
                                                                                                              right=Node(
                                                                                                                  leftval=0,
                                                                                                                  rightval=-857,
                                                                                                                  left=None,
                                                                                                                  right=Node(
                                                                                                                      leftval=711,
                                                                                                                      rightval=-468,
                                                                                                                      left=Node(),
                                                                                                                      right=Node(
                                                                                                                          leftval=0,
                                                                                                                          rightval=-793,
                                                                                                                          left=None,
                                                                                                                          right=Node(
                                                                                                                              leftval=270,
                                                                                                                              rightval=0,
                                                                                                                              left=Node(
                                                                                                                                  leftval=0,
                                                                                                                                  rightval=-129,
                                                                                                                                  left=None,
                                                                                                                                  right=Node(
                                                                                                                                      leftval=0,
                                                                                                                                      rightval=114,
                                                                                                                                      left=None,
                                                                                                                                      right=Node())),
                                                                                                                              right=None)))))),
                                                                                                right=Node(leftval=871,
                                                                                                           rightval=-73,
                                                                                                           left=Node(
                                                                                                               leftval=452,
                                                                                                               rightval=-905,
                                                                                                               left=Node(
                                                                                                                   leftval=560,
                                                                                                                   rightval=952,
                                                                                                                   left=Node(
                                                                                                                       leftval=0,
                                                                                                                       rightval=852,
                                                                                                                       left=None,
                                                                                                                       right=Node(
                                                                                                                           leftval=-266,
                                                                                                                           rightval=0,
                                                                                                                           left=Node(
                                                                                                                               leftval=0,
                                                                                                                               rightval=-468,
                                                                                                                               left=None,
                                                                                                                               right=Node(
                                                                                                                                   leftval=0,
                                                                                                                                   rightval=-592,
                                                                                                                                   left=None,
                                                                                                                                   right=Node())),
                                                                                                                           right=None)),
                                                                                                                   right=Node(
                                                                                                                       leftval=-724,
                                                                                                                       rightval=-509,
                                                                                                                       left=Node(
                                                                                                                           leftval=-686,
                                                                                                                           rightval=148,
                                                                                                                           left=Node(
                                                                                                                               leftval=-205,
                                                                                                                               rightval=715,
                                                                                                                               left=Node(
                                                                                                                                   leftval=-973,
                                                                                                                                   rightval=-35,
                                                                                                                                   left=Node(
                                                                                                                                       leftval=0,
                                                                                                                                       rightval=615,
                                                                                                                                       left=None,
                                                                                                                                       right=Node()),
                                                                                                                                   right=Node(
                                                                                                                                       leftval=-642,
                                                                                                                                       rightval=0,
                                                                                                                                       left=Node(
                                                                                                                                           leftval=-95,
                                                                                                                                           rightval=363,
                                                                                                                                           left=Node(),
                                                                                                                                           right=Node(
                                                                                                                                               leftval=222,
                                                                                                                                               rightval=887,
                                                                                                                                               left=Node(),
                                                                                                                                               right=Node())),
                                                                                                                                       right=None)),
                                                                                                                               right=Node(
                                                                                                                                   leftval=-269,
                                                                                                                                   rightval=0,
                                                                                                                                   left=Node(
                                                                                                                                       leftval=329,
                                                                                                                                       rightval=0,
                                                                                                                                       left=Node(),
                                                                                                                                       right=None),
                                                                                                                                   right=None)),
                                                                                                                           right=Node()),
                                                                                                                       right=Node(
                                                                                                                           leftval=0,
                                                                                                                           rightval=-425,
                                                                                                                           left=None,
                                                                                                                           right=Node(
                                                                                                                               leftval=114,
                                                                                                                               rightval=0,
                                                                                                                               left=Node(
                                                                                                                                   leftval=-907,
                                                                                                                                   rightval=0,
                                                                                                                                   left=Node(
                                                                                                                                       leftval=0,
                                                                                                                                       rightval=513,
                                                                                                                                       left=None,
                                                                                                                                       right=Node()),
                                                                                                                                   right=None),
                                                                                                                               right=None)))),
                                                                                                               right=Node(
                                                                                                                   leftval=356,
                                                                                                                   rightval=0,
                                                                                                                   left=Node(
                                                                                                                       leftval=-144,
                                                                                                                       rightval=581,
                                                                                                                       left=Node(
                                                                                                                           leftval=-152,
                                                                                                                           rightval=0,
                                                                                                                           left=Node(
                                                                                                                               leftval=-206,
                                                                                                                               rightval=532,
                                                                                                                               left=Node(
                                                                                                                                   leftval=465,
                                                                                                                                   rightval=0,
                                                                                                                                   left=Node(),
                                                                                                                                   right=None),
                                                                                                                               right=Node()),
                                                                                                                           right=None),
                                                                                                                       right=Node(
                                                                                                                           leftval=437,
                                                                                                                           rightval=162,
                                                                                                                           left=Node(),
                                                                                                                           right=Node(
                                                                                                                               leftval=-177,
                                                                                                                               rightval=785,
                                                                                                                               left=Node(
                                                                                                                                   leftval=305,
                                                                                                                                   rightval=-83,
                                                                                                                                   left=Node(),
                                                                                                                                   right=Node(
                                                                                                                                       leftval=0,
                                                                                                                                       rightval=-544,
                                                                                                                                       left=None,
                                                                                                                                       right=Node())),
                                                                                                                               right=Node(
                                                                                                                                   leftval=-936,
                                                                                                                                   rightval=0,
                                                                                                                                   left=Node(),
                                                                                                                                   right=None)))),
                                                                                                                   right=None)),
                                                                                                           right=Node(
                                                                                                               leftval=-956,
                                                                                                               rightval=-438,
                                                                                                               left=Node(
                                                                                                                   leftval=859,
                                                                                                                   rightval=149,
                                                                                                                   left=Node(
                                                                                                                       leftval=0,
                                                                                                                       rightval=80,
                                                                                                                       left=None,
                                                                                                                       right=Node(
                                                                                                                           leftval=-86,
                                                                                                                           rightval=0,
                                                                                                                           left=Node(),
                                                                                                                           right=None)),
                                                                                                                   right=Node()),
                                                                                                               right=Node(
                                                                                                                   leftval=285,
                                                                                                                   rightval=-834,
                                                                                                                   left=Node(
                                                                                                                       leftval=0,
                                                                                                                       rightval=889,
                                                                                                                       left=None,
                                                                                                                       right=Node(
                                                                                                                           leftval=-26,
                                                                                                                           rightval=748,
                                                                                                                           left=Node(),
                                                                                                                           right=Node(
                                                                                                                               leftval=-627,
                                                                                                                               rightval=-795,
                                                                                                                               left=Node(
                                                                                                                                   leftval=469,
                                                                                                                                   rightval=545,
                                                                                                                                   left=Node(
                                                                                                                                       leftval=296,
                                                                                                                                       rightval=0,
                                                                                                                                       left=Node(
                                                                                                                                           leftval=0,
                                                                                                                                           rightval=972,
                                                                                                                                           left=None,
                                                                                                                                           right=Node(
                                                                                                                                               leftval=123,
                                                                                                                                               rightval=0,
                                                                                                                                               left=Node(),
                                                                                                                                               right=None)),
                                                                                                                                       right=None),
                                                                                                                                   right=Node(
                                                                                                                                       leftval=0,
                                                                                                                                       rightval=-971,
                                                                                                                                       left=None,
                                                                                                                                       right=Node(
                                                                                                                                           leftval=-994,
                                                                                                                                           rightval=-563,
                                                                                                                                           left=Node(),
                                                                                                                                           right=Node(
                                                                                                                                               leftval=-353,
                                                                                                                                               rightval=0,
                                                                                                                                               left=Node(),
                                                                                                                                               right=None)))),
                                                                                                                               right=Node(
                                                                                                                                   leftval=0,
                                                                                                                                   rightval=410,
                                                                                                                                   left=None,
                                                                                                                                   right=Node(
                                                                                                                                       leftval=0,
                                                                                                                                       rightval=-427,
                                                                                                                                       left=None,
                                                                                                                                       right=Node(
                                                                                                                                           leftval=0,
                                                                                                                                           rightval=-381,
                                                                                                                                           left=None,
                                                                                                                                           right=Node(
                                                                                                                                               leftval=0,
                                                                                                                                               rightval=789,
                                                                                                                                               left=None,
                                                                                                                                               right=Node()))))))),
                                                                                                                   right=Node())))))),
                                                                right=Node(leftval=-212, rightval=-984,
                                                                           left=Node(leftval=504, rightval=407,
                                                                                     left=Node(leftval=-778,
                                                                                               rightval=-797,
                                                                                               left=Node(leftval=-694,
                                                                                                         rightval=194,
                                                                                                         left=Node(
                                                                                                             leftval=0,
                                                                                                             rightval=-917,
                                                                                                             left=None,
                                                                                                             right=Node(
                                                                                                                 leftval=-914,
                                                                                                                 rightval=0,
                                                                                                                 left=Node(),
                                                                                                                 right=None)),
                                                                                                         right=Node(
                                                                                                             leftval=-448,
                                                                                                             rightval=-665,
                                                                                                             left=Node(
                                                                                                                 leftval=-61,
                                                                                                                 rightval=0,
                                                                                                                 left=Node(
                                                                                                                     leftval=319,
                                                                                                                     rightval=848,
                                                                                                                     left=Node(
                                                                                                                         leftval=921,
                                                                                                                         rightval=0,
                                                                                                                         left=Node(),
                                                                                                                         right=None),
                                                                                                                     right=Node(
                                                                                                                         leftval=0,
                                                                                                                         rightval=458,
                                                                                                                         left=None,
                                                                                                                         right=Node())),
                                                                                                                 right=None),
                                                                                                             right=Node(
                                                                                                                 leftval=-916,
                                                                                                                 rightval=0,
                                                                                                                 left=Node(
                                                                                                                     leftval=270,
                                                                                                                     rightval=-927,
                                                                                                                     left=Node(
                                                                                                                         leftval=-445,
                                                                                                                         rightval=-318,
                                                                                                                         left=Node(
                                                                                                                             leftval=0,
                                                                                                                             rightval=-231,
                                                                                                                             left=None,
                                                                                                                             right=Node()),
                                                                                                                         right=Node(
                                                                                                                             leftval=-691,
                                                                                                                             rightval=0,
                                                                                                                             left=Node(
                                                                                                                                 leftval=-717,
                                                                                                                                 rightval=0,
                                                                                                                                 left=Node(),
                                                                                                                                 right=None),
                                                                                                                             right=None)),
                                                                                                                     right=Node(
                                                                                                                         leftval=-308,
                                                                                                                         rightval=596,
                                                                                                                         left=Node(),
                                                                                                                         right=Node())),
                                                                                                                 right=None))),
                                                                                               right=Node(leftval=-388,
                                                                                                          rightval=-151,
                                                                                                          left=Node(
                                                                                                              leftval=-21,
                                                                                                              rightval=496,
                                                                                                              left=Node(
                                                                                                                  leftval=-400,
                                                                                                                  rightval=0,
                                                                                                                  left=Node(),
                                                                                                                  right=None),
                                                                                                              right=Node()),
                                                                                                          right=Node(
                                                                                                              leftval=711,
                                                                                                              rightval=-328,
                                                                                                              left=Node(),
                                                                                                              right=Node(
                                                                                                                  leftval=-381,
                                                                                                                  rightval=-175,
                                                                                                                  left=Node(),
                                                                                                                  right=Node())))),
                                                                                     right=Node(leftval=-382,
                                                                                                rightval=-314,
                                                                                                left=Node(leftval=-763,
                                                                                                          rightval=0,
                                                                                                          left=Node(
                                                                                                              leftval=-746,
                                                                                                              rightval=-19,
                                                                                                              left=Node(),
                                                                                                              right=Node()),
                                                                                                          right=None),
                                                                                                right=Node(leftval=-923,
                                                                                                           rightval=0,
                                                                                                           left=Node(),
                                                                                                           right=None))),
                                                                           right=Node(leftval=-548, rightval=-875,
                                                                                      left=Node(),
                                                                                      right=Node(leftval=535,
                                                                                                 rightval=0,
                                                                                                 left=Node(leftval=-595,
                                                                                                           rightval=0,
                                                                                                           left=Node(
                                                                                                               leftval=-827,
                                                                                                               rightval=0,
                                                                                                               left=Node(
                                                                                                                   leftval=0,
                                                                                                                   rightval=654,
                                                                                                                   left=None,
                                                                                                                   right=Node()),
                                                                                                               right=None),
                                                                                                           right=None),
                                                                                                 right=None))))),
                                           right=Node(leftval=210, rightval=-136,
                                                      left=Node(leftval=928, rightval=-927,
                                                                left=Node(leftval=620, rightval=991,
                                                                          left=Node(leftval=971, rightval=529,
                                                                                    left=Node(leftval=67, rightval=14,
                                                                                              left=Node(leftval=-62,
                                                                                                        rightval=-226,
                                                                                                        left=Node(
                                                                                                            leftval=-266,
                                                                                                            rightval=-765,
                                                                                                            left=Node(
                                                                                                                leftval=0,
                                                                                                                rightval=198,
                                                                                                                left=None,
                                                                                                                right=Node(
                                                                                                                    leftval=-466,
                                                                                                                    rightval=0,
                                                                                                                    left=Node(),
                                                                                                                    right=None)),
                                                                                                            right=Node(
                                                                                                                leftval=0,
                                                                                                                rightval=-607,
                                                                                                                left=None,
                                                                                                                right=Node())),
                                                                                                        right=Node(
                                                                                                            leftval=-786,
                                                                                                            rightval=-595,
                                                                                                            left=Node(),
                                                                                                            right=Node(
                                                                                                                leftval=-701,
                                                                                                                rightval=0,
                                                                                                                left=Node(
                                                                                                                    leftval=276,
                                                                                                                    rightval=0,
                                                                                                                    left=Node(
                                                                                                                        leftval=-558,
                                                                                                                        rightval=0,
                                                                                                                        left=Node(
                                                                                                                            leftval=633,
                                                                                                                            rightval=0,
                                                                                                                            left=Node(
                                                                                                                                leftval=-914,
                                                                                                                                rightval=941,
                                                                                                                                left=Node(),
                                                                                                                                right=Node(
                                                                                                                                    leftval=-576,
                                                                                                                                    rightval=312,
                                                                                                                                    left=Node(),
                                                                                                                                    right=Node())),
                                                                                                                            right=None),
                                                                                                                        right=None),
                                                                                                                    right=None),
                                                                                                                right=None))),
                                                                                              right=Node(leftval=-134,
                                                                                                         rightval=797,
                                                                                                         left=Node(
                                                                                                             leftval=0,
                                                                                                             rightval=221,
                                                                                                             left=None,
                                                                                                             right=Node()),
                                                                                                         right=Node(
                                                                                                             leftval=307,
                                                                                                             rightval=392,
                                                                                                             left=Node(),
                                                                                                             right=Node()))),
                                                                                    right=Node(leftval=-304,
                                                                                               rightval=445,
                                                                                               left=Node(leftval=300,
                                                                                                         rightval=0,
                                                                                                         left=Node(),
                                                                                                         right=None),
                                                                                               right=Node(leftval=0,
                                                                                                          rightval=-981,
                                                                                                          left=None,
                                                                                                          right=Node()))),
                                                                          right=Node(leftval=-13, rightval=731,
                                                                                     left=Node(leftval=-917,
                                                                                               rightval=-385,
                                                                                               left=Node(leftval=0,
                                                                                                         rightval=446,
                                                                                                         left=None,
                                                                                                         right=Node(
                                                                                                             leftval=-398,
                                                                                                             rightval=470,
                                                                                                             left=Node(),
                                                                                                             right=Node(
                                                                                                                 leftval=0,
                                                                                                                 rightval=193,
                                                                                                                 left=None,
                                                                                                                 right=Node()))),
                                                                                               right=Node(leftval=-733,
                                                                                                          rightval=0,
                                                                                                          left=Node(
                                                                                                              leftval=0,
                                                                                                              rightval=-540,
                                                                                                              left=None,
                                                                                                              right=Node(
                                                                                                                  leftval=0,
                                                                                                                  rightval=-865,
                                                                                                                  left=None,
                                                                                                                  right=Node())),
                                                                                                          right=None)),
                                                                                     right=Node(leftval=0, rightval=991,
                                                                                                left=None,
                                                                                                right=Node(leftval=691,
                                                                                                           rightval=0,
                                                                                                           left=Node(
                                                                                                               leftval=225,
                                                                                                               rightval=-145,
                                                                                                               left=Node(
                                                                                                                   leftval=626,
                                                                                                                   rightval=648,
                                                                                                                   left=Node(
                                                                                                                       leftval=0,
                                                                                                                       rightval=779,
                                                                                                                       left=None,
                                                                                                                       right=Node()),
                                                                                                                   right=Node(
                                                                                                                       leftval=389,
                                                                                                                       rightval=0,
                                                                                                                       left=Node(
                                                                                                                           leftval=175,
                                                                                                                           rightval=-815,
                                                                                                                           left=Node(),
                                                                                                                           right=Node()),
                                                                                                                       right=None)),
                                                                                                               right=Node(
                                                                                                                   leftval=0,
                                                                                                                   rightval=845,
                                                                                                                   left=None,
                                                                                                                   right=Node(
                                                                                                                       leftval=96,
                                                                                                                       rightval=0,
                                                                                                                       left=Node(
                                                                                                                           leftval=-407,
                                                                                                                           rightval=0,
                                                                                                                           left=Node(),
                                                                                                                           right=None),
                                                                                                                       right=None))),
                                                                                                           right=None)))),
                                                                right=Node(leftval=-316, rightval=-887,
                                                                           left=Node(leftval=-665, rightval=312,
                                                                                     left=Node(leftval=582,
                                                                                               rightval=-165,
                                                                                               left=Node(leftval=0,
                                                                                                         rightval=38,
                                                                                                         left=None,
                                                                                                         right=Node(
                                                                                                             leftval=0,
                                                                                                             rightval=-381,
                                                                                                             left=None,
                                                                                                             right=Node())),
                                                                                               right=Node(leftval=-380,
                                                                                                          rightval=0,
                                                                                                          left=Node(
                                                                                                              leftval=931,
                                                                                                              rightval=689,
                                                                                                              left=Node(
                                                                                                                  leftval=10,
                                                                                                                  rightval=0,
                                                                                                                  left=Node(),
                                                                                                                  right=None),
                                                                                                              right=Node()),
                                                                                                          right=None)),
                                                                                     right=Node(leftval=-873,
                                                                                                rightval=0,
                                                                                                left=Node(),
                                                                                                right=None)),
                                                                           right=Node(leftval=0, rightval=699,
                                                                                      left=None,
                                                                                      right=Node(leftval=0,
                                                                                                 rightval=493,
                                                                                                 left=None,
                                                                                                 right=Node())))),
                                                      right=Node(leftval=897, rightval=-709,
                                                                 left=Node(leftval=995, rightval=-528,
                                                                           left=Node(leftval=-399, rightval=877,
                                                                                     left=Node(leftval=-158, rightval=0,
                                                                                               left=Node(leftval=-278,
                                                                                                         rightval=0,
                                                                                                         left=Node(
                                                                                                             leftval=0,
                                                                                                             rightval=659,
                                                                                                             left=None,
                                                                                                             right=Node()),
                                                                                                         right=None),
                                                                                               right=None),
                                                                                     right=Node(leftval=-207,
                                                                                                rightval=637,
                                                                                                left=Node(),
                                                                                                right=Node(leftval=962,
                                                                                                           rightval=867,
                                                                                                           left=Node(
                                                                                                               leftval=-877,
                                                                                                               rightval=249,
                                                                                                               left=Node(
                                                                                                                   leftval=0,
                                                                                                                   rightval=433,
                                                                                                                   left=None,
                                                                                                                   right=Node(
                                                                                                                       leftval=0,
                                                                                                                       rightval=-785,
                                                                                                                       left=None,
                                                                                                                       right=Node(
                                                                                                                           leftval=290,
                                                                                                                           rightval=-337,
                                                                                                                           left=Node(
                                                                                                                               leftval=0,
                                                                                                                               rightval=264,
                                                                                                                               left=None,
                                                                                                                               right=Node(
                                                                                                                                   leftval=0,
                                                                                                                                   rightval=225,
                                                                                                                                   left=None,
                                                                                                                                   right=Node())),
                                                                                                                           right=Node()))),
                                                                                                               right=Node(
                                                                                                                   leftval=-773,
                                                                                                                   rightval=804,
                                                                                                                   left=Node(
                                                                                                                       leftval=0,
                                                                                                                       rightval=604,
                                                                                                                       left=None,
                                                                                                                       right=Node()),
                                                                                                                   right=Node())),
                                                                                                           right=Node(
                                                                                                               leftval=-740,
                                                                                                               rightval=0,
                                                                                                               left=Node(
                                                                                                                   leftval=614,
                                                                                                                   rightval=739,
                                                                                                                   left=Node(
                                                                                                                       leftval=397,
                                                                                                                       rightval=0,
                                                                                                                       left=Node(
                                                                                                                           leftval=985,
                                                                                                                           rightval=0,
                                                                                                                           left=Node(),
                                                                                                                           right=None),
                                                                                                                       right=None),
                                                                                                                   right=Node()),
                                                                                                               right=None)))),
                                                                           right=Node(leftval=-980, rightval=700,
                                                                                      left=Node(leftval=294,
                                                                                                rightval=-846,
                                                                                                left=Node(leftval=549,
                                                                                                          rightval=-610,
                                                                                                          left=Node(),
                                                                                                          right=Node(
                                                                                                              leftval=-240,
                                                                                                              rightval=0,
                                                                                                              left=Node(),
                                                                                                              right=None)),
                                                                                                right=Node(leftval=617,
                                                                                                           rightval=0,
                                                                                                           left=Node(),
                                                                                                           right=None)),
                                                                                      right=Node(leftval=-288,
                                                                                                 rightval=-636,
                                                                                                 left=Node(),
                                                                                                 right=Node(
                                                                                                     leftval=-940,
                                                                                                     rightval=-293,
                                                                                                     left=Node(
                                                                                                         leftval=-938,
                                                                                                         rightval=620,
                                                                                                         left=Node(
                                                                                                             leftval=0,
                                                                                                             rightval=678,
                                                                                                             left=None,
                                                                                                             right=Node(
                                                                                                                 leftval=589,
                                                                                                                 rightval=0,
                                                                                                                 left=Node(
                                                                                                                     leftval=0,
                                                                                                                     rightval=-809,
                                                                                                                     left=None,
                                                                                                                     right=Node()),
                                                                                                                 right=None)),
                                                                                                         right=Node(
                                                                                                             leftval=503,
                                                                                                             rightval=954,
                                                                                                             left=Node(
                                                                                                                 leftval=-150,
                                                                                                                 rightval=584,
                                                                                                                 left=Node(
                                                                                                                     leftval=-149,
                                                                                                                     rightval=-872,
                                                                                                                     left=Node(
                                                                                                                         leftval=890,
                                                                                                                         rightval=-828,
                                                                                                                         left=Node(
                                                                                                                             leftval=0,
                                                                                                                             rightval=-128,
                                                                                                                             left=None,
                                                                                                                             right=Node()),
                                                                                                                         right=Node()),
                                                                                                                     right=Node()),
                                                                                                                 right=Node()),
                                                                                                             right=Node())),
                                                                                                     right=Node(
                                                                                                         leftval=416,
                                                                                                         rightval=0,
                                                                                                         left=Node(
                                                                                                             leftval=-752,
                                                                                                             rightval=-265,
                                                                                                             left=Node(
                                                                                                                 leftval=882,
                                                                                                                 rightval=0,
                                                                                                                 left=Node(
                                                                                                                     leftval=17,
                                                                                                                     rightval=0,
                                                                                                                     left=Node(),
                                                                                                                     right=None),
                                                                                                                 right=None),
                                                                                                             right=Node(
                                                                                                                 leftval=-279,
                                                                                                                 rightval=-856,
                                                                                                                 left=Node(),
                                                                                                                 right=Node())),
                                                                                                         right=None))))),
                                                                 right=Node(leftval=-147, rightval=517,
                                                                            left=Node(leftval=936, rightval=-744,
                                                                                      left=Node(leftval=0,
                                                                                                rightval=-994,
                                                                                                left=None,
                                                                                                right=Node()),
                                                                                      right=Node(leftval=838,
                                                                                                 rightval=-700,
                                                                                                 left=Node(leftval=-710,
                                                                                                           rightval=0,
                                                                                                           left=Node(
                                                                                                               leftval=0,
                                                                                                               rightval=759,
                                                                                                               left=None,
                                                                                                               right=Node(
                                                                                                                   leftval=0,
                                                                                                                   rightval=-524,
                                                                                                                   left=None,
                                                                                                                   right=Node(
                                                                                                                       leftval=910,
                                                                                                                       rightval=238,
                                                                                                                       left=Node(),
                                                                                                                       right=Node()))),
                                                                                                           right=None),
                                                                                                 right=Node(
                                                                                                     leftval=-680,
                                                                                                     rightval=-229,
                                                                                                     left=Node(
                                                                                                         leftval=-24,
                                                                                                         rightval=0,
                                                                                                         left=Node(),
                                                                                                         right=None),
                                                                                                     right=Node(
                                                                                                         leftval=189,
                                                                                                         rightval=-370,
                                                                                                         left=Node(
                                                                                                             leftval=-31,
                                                                                                             rightval=967,
                                                                                                             left=Node(
                                                                                                                 leftval=0,
                                                                                                                 rightval=979,
                                                                                                                 left=None,
                                                                                                                 right=Node()),
                                                                                                             right=Node(
                                                                                                                 leftval=0,
                                                                                                                 rightval=-314,
                                                                                                                 left=None,
                                                                                                                 right=Node())),
                                                                                                         right=Node(
                                                                                                             leftval=-790,
                                                                                                             rightval=92,
                                                                                                             left=Node(
                                                                                                                 leftval=-624,
                                                                                                                 rightval=0,
                                                                                                                 left=Node(),
                                                                                                                 right=None),
                                                                                                             right=Node()))))),
                                                                            right=Node(leftval=-387, rightval=127,
                                                                                       left=Node(leftval=545,
                                                                                                 rightval=-624,
                                                                                                 left=Node(),
                                                                                                 right=Node()),
                                                                                       right=Node(leftval=-730,
                                                                                                  rightval=-140,
                                                                                                  left=Node(leftval=358,
                                                                                                            rightval=0,
                                                                                                            left=Node(),
                                                                                                            right=None),
                                                                                                  right=Node(leftval=0,
                                                                                                             rightval=-851,
                                                                                                             left=None,
                                                                                                             right=Node(
                                                                                                                 leftval=0,
                                                                                                                 rightval=438,
                                                                                                                 left=None,
                                                                                                                 right=Node(
                                                                                                                     leftval=0,
                                                                                                                     rightval=-841,
                                                                                                                     left=None,
                                                                                                                     right=Node()))))))))),
                                 right=Node(leftval=-164, rightval=-983,
                                            left=Node(leftval=0, rightval=-90,
                                                      left=None,
                                                      right=Node()),
                                            right=Node(leftval=-230, rightval=0,
                                                       left=Node(),
                                                       right=None))),
                       right=Node(leftval=261, rightval=414,
                                  left=Node(leftval=-105, rightval=805,
                                            left=Node(leftval=963, rightval=-631,
                                                      left=Node(leftval=57, rightval=363,
                                                                left=Node(leftval=19, rightval=556,
                                                                          left=Node(leftval=-72, rightval=-303,
                                                                                    left=Node(leftval=143, rightval=0,
                                                                                              left=Node(leftval=0,
                                                                                                        rightval=-771,
                                                                                                        left=None,
                                                                                                        right=Node(
                                                                                                            leftval=0,
                                                                                                            rightval=-433,
                                                                                                            left=None,
                                                                                                            right=Node())),
                                                                                              right=None),
                                                                                    right=Node(leftval=-493,
                                                                                               rightval=965,
                                                                                               left=Node(leftval=-137,
                                                                                                         rightval=-116,
                                                                                                         left=Node(),
                                                                                                         right=Node(
                                                                                                             leftval=572,
                                                                                                             rightval=0,
                                                                                                             left=Node(),
                                                                                                             right=None)),
                                                                                               right=Node())),
                                                                          right=Node(leftval=-811, rightval=388,
                                                                                     left=Node(leftval=-54,
                                                                                               rightval=-985,
                                                                                               left=Node(leftval=293,
                                                                                                         rightval=0,
                                                                                                         left=Node(),
                                                                                                         right=None),
                                                                                               right=Node(leftval=0,
                                                                                                          rightval=267,
                                                                                                          left=None,
                                                                                                          right=Node(
                                                                                                              leftval=-81,
                                                                                                              rightval=0,
                                                                                                              left=Node(
                                                                                                                  leftval=0,
                                                                                                                  rightval=431,
                                                                                                                  left=None,
                                                                                                                  right=Node(
                                                                                                                      leftval=700,
                                                                                                                      rightval=0,
                                                                                                                      left=Node(),
                                                                                                                      right=None)),
                                                                                                              right=None))),
                                                                                     right=Node(leftval=538,
                                                                                                rightval=-35,
                                                                                                left=Node(),
                                                                                                right=Node(leftval=0,
                                                                                                           rightval=446,
                                                                                                           left=None,
                                                                                                           right=Node(
                                                                                                               leftval=-132,
                                                                                                               rightval=0,
                                                                                                               left=Node(),
                                                                                                               right=None))))),
                                                                right=Node(leftval=294, rightval=427,
                                                                           left=Node(leftval=210, rightval=-42,
                                                                                     left=Node(leftval=763,
                                                                                               rightval=-407,
                                                                                               left=Node(leftval=-463,
                                                                                                         rightval=-375,
                                                                                                         left=Node(
                                                                                                             leftval=0,
                                                                                                             rightval=-185,
                                                                                                             left=None,
                                                                                                             right=Node(
                                                                                                                 leftval=0,
                                                                                                                 rightval=-475,
                                                                                                                 left=None,
                                                                                                                 right=Node(
                                                                                                                     leftval=-1000,
                                                                                                                     rightval=0,
                                                                                                                     left=Node(),
                                                                                                                     right=None))),
                                                                                                         right=Node(
                                                                                                             leftval=-856,
                                                                                                             rightval=622,
                                                                                                             left=Node(
                                                                                                                 leftval=784,
                                                                                                                 rightval=0,
                                                                                                                 left=Node(
                                                                                                                     leftval=-276,
                                                                                                                     rightval=-420,
                                                                                                                     left=Node(),
                                                                                                                     right=Node()),
                                                                                                                 right=None),
                                                                                                             right=Node(
                                                                                                                 leftval=0,
                                                                                                                 rightval=-928,
                                                                                                                 left=None,
                                                                                                                 right=Node()))),
                                                                                               right=Node(leftval=-861,
                                                                                                          rightval=-151,
                                                                                                          left=Node(
                                                                                                              leftval=0,
                                                                                                              rightval=824,
                                                                                                              left=None,
                                                                                                              right=Node()),
                                                                                                          right=Node())),
                                                                                     right=Node(leftval=-219,
                                                                                                rightval=-179,
                                                                                                left=Node(leftval=299,
                                                                                                          rightval=113,
                                                                                                          left=Node(),
                                                                                                          right=Node(
                                                                                                              leftval=0,
                                                                                                              rightval=957,
                                                                                                              left=None,
                                                                                                              right=Node())),
                                                                                                right=Node(leftval=427,
                                                                                                           rightval=-754,
                                                                                                           left=Node(
                                                                                                               leftval=-239,
                                                                                                               rightval=0,
                                                                                                               left=Node(
                                                                                                                   leftval=-95,
                                                                                                                   rightval=0,
                                                                                                                   left=Node(),
                                                                                                                   right=None),
                                                                                                               right=None),
                                                                                                           right=Node(
                                                                                                               leftval=0,
                                                                                                               rightval=-748,
                                                                                                               left=None,
                                                                                                               right=Node())))),
                                                                           right=Node(leftval=-62, rightval=-890,
                                                                                      left=Node(leftval=-877,
                                                                                                rightval=-91,
                                                                                                left=Node(leftval=1,
                                                                                                          rightval=422,
                                                                                                          left=Node(
                                                                                                              leftval=-554,
                                                                                                              rightval=0,
                                                                                                              left=Node(),
                                                                                                              right=None),
                                                                                                          right=Node()),
                                                                                                right=Node(leftval=962,
                                                                                                           rightval=0,
                                                                                                           left=Node(
                                                                                                               leftval=335,
                                                                                                               rightval=0,
                                                                                                               left=Node(),
                                                                                                               right=None),
                                                                                                           right=None)),
                                                                                      right=Node(leftval=-277,
                                                                                                 rightval=-158,
                                                                                                 left=Node(leftval=-656,
                                                                                                           rightval=-323,
                                                                                                           left=Node(
                                                                                                               leftval=-200,
                                                                                                               rightval=0,
                                                                                                               left=Node(
                                                                                                                   leftval=0,
                                                                                                                   rightval=-35,
                                                                                                                   left=None,
                                                                                                                   right=Node(
                                                                                                                       leftval=0,
                                                                                                                       rightval=-273,
                                                                                                                       left=None,
                                                                                                                       right=Node())),
                                                                                                               right=None),
                                                                                                           right=Node(
                                                                                                               leftval=0,
                                                                                                               rightval=-214,
                                                                                                               left=None,
                                                                                                               right=Node(
                                                                                                                   leftval=467,
                                                                                                                   rightval=-324,
                                                                                                                   left=Node(
                                                                                                                       leftval=432,
                                                                                                                       rightval=-401,
                                                                                                                       left=Node(),
                                                                                                                       right=Node(
                                                                                                                           leftval=311,
                                                                                                                           rightval=0,
                                                                                                                           left=Node(
                                                                                                                               leftval=-447,
                                                                                                                               rightval=788,
                                                                                                                               left=Node(
                                                                                                                                   leftval=0,
                                                                                                                                   rightval=271,
                                                                                                                                   left=None,
                                                                                                                                   right=Node(
                                                                                                                                       leftval=-763,
                                                                                                                                       rightval=0,
                                                                                                                                       left=Node(),
                                                                                                                                       right=None)),
                                                                                                                               right=Node()),
                                                                                                                           right=None)),
                                                                                                                   right=Node(
                                                                                                                       leftval=-112,
                                                                                                                       rightval=-57,
                                                                                                                       left=Node(),
                                                                                                                       right=Node(
                                                                                                                           leftval=-785,
                                                                                                                           rightval=0,
                                                                                                                           left=Node(),
                                                                                                                           right=None))))),
                                                                                                 right=Node(leftval=797,
                                                                                                            rightval=808,
                                                                                                            left=Node(
                                                                                                                leftval=-582,
                                                                                                                rightval=201,
                                                                                                                left=Node(
                                                                                                                    leftval=-550,
                                                                                                                    rightval=629,
                                                                                                                    left=Node(
                                                                                                                        leftval=-285,
                                                                                                                        rightval=616,
                                                                                                                        left=Node(),
                                                                                                                        right=Node(
                                                                                                                            leftval=-618,
                                                                                                                            rightval=-91,
                                                                                                                            left=Node(),
                                                                                                                            right=Node(
                                                                                                                                leftval=0,
                                                                                                                                rightval=864,
                                                                                                                                left=None,
                                                                                                                                right=Node()))),
                                                                                                                    right=Node(
                                                                                                                        leftval=-203,
                                                                                                                        rightval=494,
                                                                                                                        left=Node(),
                                                                                                                        right=Node())),
                                                                                                                right=Node(
                                                                                                                    leftval=0,
                                                                                                                    rightval=925,
                                                                                                                    left=None,
                                                                                                                    right=Node())),
                                                                                                            right=Node(
                                                                                                                leftval=579,
                                                                                                                rightval=0,
                                                                                                                left=Node(
                                                                                                                    leftval=0,
                                                                                                                    rightval=-418,
                                                                                                                    left=None,
                                                                                                                    right=Node(
                                                                                                                        leftval=48,
                                                                                                                        rightval=539,
                                                                                                                        left=Node(
                                                                                                                            leftval=0,
                                                                                                                            rightval=-523,
                                                                                                                            left=None,
                                                                                                                            right=Node(
                                                                                                                                leftval=387,
                                                                                                                                rightval=-645,
                                                                                                                                left=Node(),
                                                                                                                                right=Node(
                                                                                                                                    leftval=0,
                                                                                                                                    rightval=306,
                                                                                                                                    left=None,
                                                                                                                                    right=Node(
                                                                                                                                        leftval=521,
                                                                                                                                        rightval=0,
                                                                                                                                        left=Node(),
                                                                                                                                        right=None)))),
                                                                                                                        right=Node(
                                                                                                                            leftval=779,
                                                                                                                            rightval=0,
                                                                                                                            left=Node(
                                                                                                                                leftval=443,
                                                                                                                                rightval=0,
                                                                                                                                left=Node(),
                                                                                                                                right=None),
                                                                                                                            right=None))),
                                                                                                                right=None)))))),
                                                      right=Node(leftval=-193, rightval=-920,
                                                                 left=Node(leftval=-57, rightval=-99,
                                                                           left=Node(leftval=130, rightval=-852,
                                                                                     left=Node(leftval=377,
                                                                                               rightval=493,
                                                                                               left=Node(leftval=-67,
                                                                                                         rightval=829,
                                                                                                         left=Node(
                                                                                                             leftval=-305,
                                                                                                             rightval=245,
                                                                                                             left=Node(
                                                                                                                 leftval=-407,
                                                                                                                 rightval=340,
                                                                                                                 left=Node(
                                                                                                                     leftval=-310,
                                                                                                                     rightval=0,
                                                                                                                     left=Node(),
                                                                                                                     right=None),
                                                                                                                 right=Node(
                                                                                                                     leftval=-284,
                                                                                                                     rightval=-993,
                                                                                                                     left=Node(
                                                                                                                         leftval=0,
                                                                                                                         rightval=-893,
                                                                                                                         left=None,
                                                                                                                         right=Node()),
                                                                                                                     right=Node())),
                                                                                                             right=Node(
                                                                                                                 leftval=0,
                                                                                                                 rightval=-606,
                                                                                                                 left=None,
                                                                                                                 right=Node(
                                                                                                                     leftval=-548,
                                                                                                                     rightval=-71,
                                                                                                                     left=Node(),
                                                                                                                     right=Node(
                                                                                                                         leftval=142,
                                                                                                                         rightval=887,
                                                                                                                         left=Node(),
                                                                                                                         right=Node())))),
                                                                                                         right=Node(
                                                                                                             leftval=0,
                                                                                                             rightval=97,
                                                                                                             left=None,
                                                                                                             right=Node(
                                                                                                                 leftval=0,
                                                                                                                 rightval=-339,
                                                                                                                 left=None,
                                                                                                                 right=Node()))),
                                                                                               right=Node(leftval=-588,
                                                                                                          rightval=-486,
                                                                                                          left=Node(
                                                                                                              leftval=781,
                                                                                                              rightval=74,
                                                                                                              left=Node(
                                                                                                                  leftval=0,
                                                                                                                  rightval=-611,
                                                                                                                  left=None,
                                                                                                                  right=Node()),
                                                                                                              right=Node(
                                                                                                                  leftval=-571,
                                                                                                                  rightval=0,
                                                                                                                  left=Node(),
                                                                                                                  right=None)),
                                                                                                          right=Node(
                                                                                                              leftval=714,
                                                                                                              rightval=0,
                                                                                                              left=Node(),
                                                                                                              right=None))),
                                                                                     right=Node(leftval=-374,
                                                                                                rightval=913,
                                                                                                left=Node(leftval=459,
                                                                                                          rightval=-509,
                                                                                                          left=Node(
                                                                                                              leftval=-479,
                                                                                                              rightval=0,
                                                                                                              left=Node(),
                                                                                                              right=None),
                                                                                                          right=Node(
                                                                                                              leftval=785,
                                                                                                              rightval=0,
                                                                                                              left=Node(),
                                                                                                              right=None)),
                                                                                                right=Node())),
                                                                           right=Node(leftval=0, rightval=10,
                                                                                      left=None,
                                                                                      right=Node(leftval=-156,
                                                                                                 rightval=0,
                                                                                                 left=Node(leftval=878,
                                                                                                           rightval=656,
                                                                                                           left=Node(),
                                                                                                           right=Node()),
                                                                                                 right=None))),
                                                                 right=Node(leftval=815, rightval=698,
                                                                            left=Node(),
                                                                            right=Node(leftval=0, rightval=545,
                                                                                       left=None,
                                                                                       right=Node(leftval=-126,
                                                                                                  rightval=144,
                                                                                                  left=Node(),
                                                                                                  right=Node(
                                                                                                      leftval=-843,
                                                                                                      rightval=675,
                                                                                                      left=Node(),
                                                                                                      right=Node(
                                                                                                          leftval=0,
                                                                                                          rightval=254,
                                                                                                          left=None,
                                                                                                          right=Node()))))))),
                                            right=Node(leftval=-444, rightval=-483,
                                                       left=Node(leftval=-403, rightval=-214,
                                                                 left=Node(leftval=-650, rightval=-719,
                                                                           left=Node(leftval=-96, rightval=52,
                                                                                     left=Node(),
                                                                                     right=Node(leftval=-393,
                                                                                                rightval=592,
                                                                                                left=Node(leftval=-781,
                                                                                                          rightval=0,
                                                                                                          left=Node(),
                                                                                                          right=None),
                                                                                                right=Node(leftval=456,
                                                                                                           rightval=0,
                                                                                                           left=Node(),
                                                                                                           right=None))),
                                                                           right=Node(leftval=-413, rightval=192,
                                                                                      left=Node(leftval=-371,
                                                                                                rightval=381,
                                                                                                left=Node(leftval=509,
                                                                                                          rightval=156,
                                                                                                          left=Node(
                                                                                                              leftval=507,
                                                                                                              rightval=350,
                                                                                                              left=Node(
                                                                                                                  leftval=-647,
                                                                                                                  rightval=500,
                                                                                                                  left=Node(
                                                                                                                      leftval=0,
                                                                                                                      rightval=-757,
                                                                                                                      left=None,
                                                                                                                      right=Node()),
                                                                                                                  right=Node()),
                                                                                                              right=Node(
                                                                                                                  leftval=-418,
                                                                                                                  rightval=801,
                                                                                                                  left=Node(),
                                                                                                                  right=Node())),
                                                                                                          right=Node(
                                                                                                              leftval=0,
                                                                                                              rightval=988,
                                                                                                              left=None,
                                                                                                              right=Node(
                                                                                                                  leftval=-758,
                                                                                                                  rightval=0,
                                                                                                                  left=Node(
                                                                                                                      leftval=0,
                                                                                                                      rightval=-442,
                                                                                                                      left=None,
                                                                                                                      right=Node(
                                                                                                                          leftval=0,
                                                                                                                          rightval=321,
                                                                                                                          left=None,
                                                                                                                          right=Node())),
                                                                                                                  right=None))),
                                                                                                right=Node(leftval=-868,
                                                                                                           rightval=61,
                                                                                                           left=Node(
                                                                                                               leftval=0,
                                                                                                               rightval=-547,
                                                                                                               left=None,
                                                                                                               right=Node()),
                                                                                                           right=Node())),
                                                                                      right=Node(leftval=287,
                                                                                                 rightval=-17,
                                                                                                 left=Node(),
                                                                                                 right=Node()))),
                                                                 right=Node(leftval=-352, rightval=608,
                                                                            left=Node(leftval=0, rightval=-16,
                                                                                      left=None,
                                                                                      right=Node(leftval=952,
                                                                                                 rightval=510,
                                                                                                 left=Node(leftval=220,
                                                                                                           rightval=0,
                                                                                                           left=Node(
                                                                                                               leftval=-947,
                                                                                                               rightval=78,
                                                                                                               left=Node(
                                                                                                                   leftval=671,
                                                                                                                   rightval=-522,
                                                                                                                   left=Node(
                                                                                                                       leftval=-844,
                                                                                                                       rightval=0,
                                                                                                                       left=Node(
                                                                                                                           leftval=0,
                                                                                                                           rightval=45,
                                                                                                                           left=None,
                                                                                                                           right=Node(
                                                                                                                               leftval=0,
                                                                                                                               rightval=-638,
                                                                                                                               left=None,
                                                                                                                               right=Node(
                                                                                                                                   leftval=998,
                                                                                                                                   rightval=0,
                                                                                                                                   left=Node(),
                                                                                                                                   right=None))),
                                                                                                                       right=None),
                                                                                                                   right=Node(
                                                                                                                       leftval=500,
                                                                                                                       rightval=-730,
                                                                                                                       left=Node(),
                                                                                                                       right=Node(
                                                                                                                           leftval=-519,
                                                                                                                           rightval=0,
                                                                                                                           left=Node(),
                                                                                                                           right=None))),
                                                                                                               right=Node(
                                                                                                                   leftval=261,
                                                                                                                   rightval=707,
                                                                                                                   left=Node(
                                                                                                                       leftval=844,
                                                                                                                       rightval=879,
                                                                                                                       left=Node(),
                                                                                                                       right=Node()),
                                                                                                                   right=Node())),
                                                                                                           right=None),
                                                                                                 right=Node(leftval=13,
                                                                                                            rightval=657,
                                                                                                            left=Node(
                                                                                                                leftval=-368,
                                                                                                                rightval=0,
                                                                                                                left=Node(),
                                                                                                                right=None),
                                                                                                            right=Node(
                                                                                                                leftval=0,
                                                                                                                rightval=800,
                                                                                                                left=None,
                                                                                                                right=Node(
                                                                                                                    leftval=0,
                                                                                                                    rightval=353,
                                                                                                                    left=None,
                                                                                                                    right=Node()))))),
                                                                            right=Node(leftval=682, rightval=0,
                                                                                       left=Node(leftval=440,
                                                                                                 rightval=-609,
                                                                                                 left=Node(leftval=0,
                                                                                                           rightval=-719,
                                                                                                           left=None,
                                                                                                           right=Node()),
                                                                                                 right=Node()),
                                                                                       right=None))),
                                                       right=Node(leftval=-192, rightval=925,
                                                                  left=Node(leftval=-506, rightval=-908,
                                                                            left=Node(leftval=0, rightval=767,
                                                                                      left=None,
                                                                                      right=Node(leftval=-298,
                                                                                                 rightval=0,
                                                                                                 left=Node(),
                                                                                                 right=None)),
                                                                            right=Node(leftval=-875, rightval=-950,
                                                                                       left=Node(leftval=499,
                                                                                                 rightval=291,
                                                                                                 left=Node(leftval=174,
                                                                                                           rightval=104,
                                                                                                           left=Node(),
                                                                                                           right=Node(
                                                                                                               leftval=-966,
                                                                                                               rightval=-271,
                                                                                                               left=Node(),
                                                                                                               right=Node())),
                                                                                                 right=Node()),
                                                                                       right=Node(leftval=0,
                                                                                                  rightval=285,
                                                                                                  left=None,
                                                                                                  right=Node(leftval=5,
                                                                                                             rightval=0,
                                                                                                             left=Node(),
                                                                                                             right=None)))),
                                                                  right=Node(leftval=-127, rightval=299,
                                                                             left=Node(),
                                                                             right=Node(leftval=-867, rightval=900,
                                                                                        left=Node(leftval=659,
                                                                                                  rightval=443,
                                                                                                  left=Node(leftval=357,
                                                                                                            rightval=594,
                                                                                                            left=Node(
                                                                                                                leftval=-668,
                                                                                                                rightval=506,
                                                                                                                left=Node(
                                                                                                                    leftval=0,
                                                                                                                    rightval=-557,
                                                                                                                    left=None,
                                                                                                                    right=Node(
                                                                                                                        leftval=827,
                                                                                                                        rightval=888,
                                                                                                                        left=Node(),
                                                                                                                        right=Node())),
                                                                                                                right=Node(
                                                                                                                    leftval=39,
                                                                                                                    rightval=-272,
                                                                                                                    left=Node(
                                                                                                                        leftval=-483,
                                                                                                                        rightval=-304,
                                                                                                                        left=Node(
                                                                                                                            leftval=355,
                                                                                                                            rightval=52,
                                                                                                                            left=Node(
                                                                                                                                leftval=-638,
                                                                                                                                rightval=0,
                                                                                                                                left=Node(),
                                                                                                                                right=None),
                                                                                                                            right=Node(
                                                                                                                                leftval=273,
                                                                                                                                rightval=779,
                                                                                                                                left=Node(
                                                                                                                                    leftval=554,
                                                                                                                                    rightval=-915,
                                                                                                                                    left=Node(
                                                                                                                                        leftval=824,
                                                                                                                                        rightval=-460,
                                                                                                                                        left=Node(),
                                                                                                                                        right=Node()),
                                                                                                                                    right=Node()),
                                                                                                                                right=Node(
                                                                                                                                    leftval=0,
                                                                                                                                    rightval=-717,
                                                                                                                                    left=None,
                                                                                                                                    right=Node(
                                                                                                                                        leftval=-994,
                                                                                                                                        rightval=25,
                                                                                                                                        left=Node(),
                                                                                                                                        right=Node())))),
                                                                                                                        right=Node(
                                                                                                                            leftval=-918,
                                                                                                                            rightval=0,
                                                                                                                            left=Node(
                                                                                                                                leftval=259,
                                                                                                                                rightval=232,
                                                                                                                                left=Node(
                                                                                                                                    leftval=-64,
                                                                                                                                    rightval=454,
                                                                                                                                    left=Node(
                                                                                                                                        leftval=0,
                                                                                                                                        rightval=-514,
                                                                                                                                        left=None,
                                                                                                                                        right=Node()),
                                                                                                                                    right=Node(
                                                                                                                                        leftval=270,
                                                                                                                                        rightval=287,
                                                                                                                                        left=Node(
                                                                                                                                            leftval=0,
                                                                                                                                            rightval=959,
                                                                                                                                            left=None,
                                                                                                                                            right=Node()),
                                                                                                                                        right=Node(
                                                                                                                                            leftval=224,
                                                                                                                                            rightval=-788,
                                                                                                                                            left=Node(),
                                                                                                                                            right=Node(
                                                                                                                                                leftval=770,
                                                                                                                                                rightval=0,
                                                                                                                                                left=Node(
                                                                                                                                                    leftval=0,
                                                                                                                                                    rightval=899,
                                                                                                                                                    left=None,
                                                                                                                                                    right=Node()),
                                                                                                                                                right=None)))),
                                                                                                                                right=Node()),
                                                                                                                            right=None)),
                                                                                                                    right=Node(
                                                                                                                        leftval=-517,
                                                                                                                        rightval=0,
                                                                                                                        left=Node(
                                                                                                                            leftval=-62,
                                                                                                                            rightval=0,
                                                                                                                            left=Node(
                                                                                                                                leftval=375,
                                                                                                                                rightval=-692,
                                                                                                                                left=Node(
                                                                                                                                    leftval=0,
                                                                                                                                    rightval=-267,
                                                                                                                                    left=None,
                                                                                                                                    right=Node(
                                                                                                                                        leftval=0,
                                                                                                                                        rightval=-817,
                                                                                                                                        left=None,
                                                                                                                                        right=Node())),
                                                                                                                                right=Node()),
                                                                                                                            right=None),
                                                                                                                        right=None))),
                                                                                                            right=Node(
                                                                                                                leftval=360,
                                                                                                                rightval=676,
                                                                                                                left=Node(
                                                                                                                    leftval=733,
                                                                                                                    rightval=530,
                                                                                                                    left=Node(
                                                                                                                        leftval=-174,
                                                                                                                        rightval=-291,
                                                                                                                        left=Node(
                                                                                                                            leftval=-410,
                                                                                                                            rightval=0,
                                                                                                                            left=Node(
                                                                                                                                leftval=86,
                                                                                                                                rightval=844,
                                                                                                                                left=Node(),
                                                                                                                                right=Node()),
                                                                                                                            right=None),
                                                                                                                        right=Node(
                                                                                                                            leftval=-755,
                                                                                                                            rightval=0,
                                                                                                                            left=Node(
                                                                                                                                leftval=477,
                                                                                                                                rightval=0,
                                                                                                                                left=Node(
                                                                                                                                    leftval=0,
                                                                                                                                    rightval=-191,
                                                                                                                                    left=None,
                                                                                                                                    right=Node(
                                                                                                                                        leftval=-67,
                                                                                                                                        rightval=0,
                                                                                                                                        left=Node(),
                                                                                                                                        right=None)),
                                                                                                                                right=None),
                                                                                                                            right=None)),
                                                                                                                    right=Node(
                                                                                                                        leftval=-687,
                                                                                                                        rightval=-323,
                                                                                                                        left=Node(
                                                                                                                            leftval=0,
                                                                                                                            rightval=-210,
                                                                                                                            left=None,
                                                                                                                            right=Node(
                                                                                                                                leftval=0,
                                                                                                                                rightval=-304,
                                                                                                                                left=None,
                                                                                                                                right=Node(
                                                                                                                                    leftval=83,
                                                                                                                                    rightval=57,
                                                                                                                                    left=Node(
                                                                                                                                        leftval=0,
                                                                                                                                        rightval=394,
                                                                                                                                        left=None,
                                                                                                                                        right=Node()),
                                                                                                                                    right=Node(
                                                                                                                                        leftval=561,
                                                                                                                                        rightval=0,
                                                                                                                                        left=Node(),
                                                                                                                                        right=None)))),
                                                                                                                        right=Node(
                                                                                                                            leftval=777,
                                                                                                                            rightval=842,
                                                                                                                            left=Node(
                                                                                                                                leftval=0,
                                                                                                                                rightval=159,
                                                                                                                                left=None,
                                                                                                                                right=Node()),
                                                                                                                            right=Node(
                                                                                                                                leftval=-668,
                                                                                                                                rightval=876,
                                                                                                                                left=Node(),
                                                                                                                                right=Node())))),
                                                                                                                right=Node(
                                                                                                                    leftval=863,
                                                                                                                    rightval=938,
                                                                                                                    left=Node(
                                                                                                                        leftval=0,
                                                                                                                        rightval=942,
                                                                                                                        left=None,
                                                                                                                        right=Node(
                                                                                                                            leftval=903,
                                                                                                                            rightval=-981,
                                                                                                                            left=Node(
                                                                                                                                leftval=0,
                                                                                                                                rightval=-911,
                                                                                                                                left=None,
                                                                                                                                right=Node(
                                                                                                                                    leftval=-712,
                                                                                                                                    rightval=164,
                                                                                                                                    left=Node(
                                                                                                                                        leftval=-404,
                                                                                                                                        rightval=0,
                                                                                                                                        left=Node(),
                                                                                                                                        right=None),
                                                                                                                                    right=Node(
                                                                                                                                        leftval=-998,
                                                                                                                                        rightval=614,
                                                                                                                                        left=Node(
                                                                                                                                            leftval=603,
                                                                                                                                            rightval=0,
                                                                                                                                            left=Node(),
                                                                                                                                            right=None),
                                                                                                                                        right=Node(
                                                                                                                                            leftval=-652,
                                                                                                                                            rightval=0,
                                                                                                                                            left=Node(),
                                                                                                                                            right=None)))),
                                                                                                                            right=Node(
                                                                                                                                leftval=-301,
                                                                                                                                rightval=0,
                                                                                                                                left=Node(),
                                                                                                                                right=None))),
                                                                                                                    right=Node()))),
                                                                                                  right=Node(
                                                                                                      leftval=832,
                                                                                                      rightval=652,
                                                                                                      left=Node(
                                                                                                          leftval=445,
                                                                                                          rightval=602,
                                                                                                          left=Node(
                                                                                                              leftval=0,
                                                                                                              rightval=187,
                                                                                                              left=None,
                                                                                                              right=Node(
                                                                                                                  leftval=-678,
                                                                                                                  rightval=0,
                                                                                                                  left=Node(
                                                                                                                      leftval=309,
                                                                                                                      rightval=0,
                                                                                                                      left=Node(
                                                                                                                          leftval=-871,
                                                                                                                          rightval=349,
                                                                                                                          left=Node(),
                                                                                                                          right=Node()),
                                                                                                                      right=None),
                                                                                                                  right=None)),
                                                                                                          right=Node(
                                                                                                              leftval=-300,
                                                                                                              rightval=-611,
                                                                                                              left=Node(),
                                                                                                              right=Node(
                                                                                                                  leftval=-349,
                                                                                                                  rightval=0,
                                                                                                                  left=Node(
                                                                                                                      leftval=79,
                                                                                                                      rightval=135,
                                                                                                                      left=Node(
                                                                                                                          leftval=-973,
                                                                                                                          rightval=-123,
                                                                                                                          left=Node(),
                                                                                                                          right=Node()),
                                                                                                                      right=Node(
                                                                                                                          leftval=101,
                                                                                                                          rightval=0,
                                                                                                                          left=Node(),
                                                                                                                          right=None)),
                                                                                                                  right=None))),
                                                                                                      right=Node(
                                                                                                          leftval=768,
                                                                                                          rightval=42,
                                                                                                          left=Node(
                                                                                                              leftval=505,
                                                                                                              rightval=0,
                                                                                                              left=Node(
                                                                                                                  leftval=-961,
                                                                                                                  rightval=496,
                                                                                                                  left=Node(
                                                                                                                      leftval=0,
                                                                                                                      rightval=606,
                                                                                                                      left=None,
                                                                                                                      right=Node()),
                                                                                                                  right=Node(
                                                                                                                      leftval=433,
                                                                                                                      rightval=17,
                                                                                                                      left=Node(
                                                                                                                          leftval=927,
                                                                                                                          rightval=-676,
                                                                                                                          left=Node(
                                                                                                                              leftval=150,
                                                                                                                              rightval=0,
                                                                                                                              left=Node(),
                                                                                                                              right=None),
                                                                                                                          right=Node(
                                                                                                                              leftval=-259,
                                                                                                                              rightval=83,
                                                                                                                              left=Node(),
                                                                                                                              right=Node())),
                                                                                                                      right=Node(
                                                                                                                          leftval=0,
                                                                                                                          rightval=285,
                                                                                                                          left=None,
                                                                                                                          right=Node()))),
                                                                                                              right=None),
                                                                                                          right=Node(
                                                                                                              leftval=461,
                                                                                                              rightval=-80,
                                                                                                              left=Node(),
                                                                                                              right=Node(
                                                                                                                  leftval=-516,
                                                                                                                  rightval=523,
                                                                                                                  left=Node(
                                                                                                                      leftval=0,
                                                                                                                      rightval=-841,
                                                                                                                      left=None,
                                                                                                                      right=Node()),
                                                                                                                  right=Node()))))),
                                                                                        right=Node(leftval=0,
                                                                                                   rightval=891,
                                                                                                   left=None,
                                                                                                   right=Node(leftval=0,
                                                                                                              rightval=-98,
                                                                                                              left=None,
                                                                                                              right=Node()))))))),
                                  right=Node(leftval=-638, rightval=-174,
                                             left=Node(leftval=-588, rightval=638,
                                                       left=Node(leftval=524, rightval=428,
                                                                 left=Node(leftval=-774, rightval=375,
                                                                           left=Node(leftval=8, rightval=0,
                                                                                     left=Node(),
                                                                                     right=None),
                                                                           right=Node(leftval=0, rightval=469,
                                                                                      left=None,
                                                                                      right=Node(leftval=-858,
                                                                                                 rightval=-610,
                                                                                                 left=Node(leftval=-741,
                                                                                                           rightval=155,
                                                                                                           left=Node(
                                                                                                               leftval=588,
                                                                                                               rightval=301,
                                                                                                               left=Node(),
                                                                                                               right=Node()),
                                                                                                           right=Node(
                                                                                                               leftval=164,
                                                                                                               rightval=0,
                                                                                                               left=Node(
                                                                                                                   leftval=699,
                                                                                                                   rightval=0,
                                                                                                                   left=Node(
                                                                                                                       leftval=0,
                                                                                                                       rightval=-274,
                                                                                                                       left=None,
                                                                                                                       right=Node()),
                                                                                                                   right=None),
                                                                                                               right=None)),
                                                                                                 right=Node(
                                                                                                     leftval=-261,
                                                                                                     rightval=-991,
                                                                                                     left=Node(
                                                                                                         leftval=-834,
                                                                                                         rightval=159,
                                                                                                         left=Node(
                                                                                                             leftval=-185,
                                                                                                             rightval=0,
                                                                                                             left=Node(),
                                                                                                             right=None),
                                                                                                         right=Node(
                                                                                                             leftval=-915,
                                                                                                             rightval=0,
                                                                                                             left=Node(),
                                                                                                             right=None)),
                                                                                                     right=Node())))),
                                                                 right=Node(leftval=415, rightval=0,
                                                                            left=Node(leftval=686, rightval=136,
                                                                                      left=Node(leftval=0, rightval=64,
                                                                                                left=None,
                                                                                                right=Node(leftval=494,
                                                                                                           rightval=687,
                                                                                                           left=Node(
                                                                                                               leftval=0,
                                                                                                               rightval=-709,
                                                                                                               left=None,
                                                                                                               right=Node(
                                                                                                                   leftval=-168,
                                                                                                                   rightval=373,
                                                                                                                   left=Node(
                                                                                                                       leftval=566,
                                                                                                                       rightval=0,
                                                                                                                       left=Node(),
                                                                                                                       right=None),
                                                                                                                   right=Node())),
                                                                                                           right=Node(
                                                                                                               leftval=481,
                                                                                                               rightval=-905,
                                                                                                               left=Node(
                                                                                                                   leftval=47,
                                                                                                                   rightval=0,
                                                                                                                   left=Node(),
                                                                                                                   right=None),
                                                                                                               right=Node(
                                                                                                                   leftval=0,
                                                                                                                   rightval=564,
                                                                                                                   left=None,
                                                                                                                   right=Node(
                                                                                                                       leftval=314,
                                                                                                                       rightval=466,
                                                                                                                       left=Node(),
                                                                                                                       right=Node(
                                                                                                                           leftval=0,
                                                                                                                           rightval=444,
                                                                                                                           left=None,
                                                                                                                           right=Node())))))),
                                                                                      right=Node()),
                                                                            right=None)),
                                                       right=Node(leftval=665, rightval=-457,
                                                                  left=Node(leftval=0, rightval=146,
                                                                            left=None,
                                                                            right=Node(leftval=-835, rightval=0,
                                                                                       left=Node(),
                                                                                       right=None)),
                                                                  right=Node())),
                                             right=Node(leftval=-282, rightval=-957,
                                                        left=Node(leftval=138, rightval=-883,
                                                                  left=Node(leftval=251, rightval=-512,
                                                                            left=Node(leftval=131, rightval=-688,
                                                                                      left=Node(leftval=549, rightval=0,
                                                                                                left=Node(),
                                                                                                right=None),
                                                                                      right=Node()),
                                                                            right=Node(leftval=0, rightval=-65,
                                                                                       left=None,
                                                                                       right=Node(leftval=327,
                                                                                                  rightval=620,
                                                                                                  left=Node(),
                                                                                                  right=Node(
                                                                                                      leftval=-605,
                                                                                                      rightval=0,
                                                                                                      left=Node(),
                                                                                                      right=None)))),
                                                                  right=Node(leftval=-25, rightval=580,
                                                                             left=Node(leftval=341, rightval=0,
                                                                                       left=Node(leftval=0,
                                                                                                 rightval=869,
                                                                                                 left=None,
                                                                                                 right=Node()),
                                                                                       right=None),
                                                                             right=Node())),
                                                        right=Node(leftval=-748, rightval=-947,
                                                                   left=Node(leftval=167, rightval=0,
                                                                             left=Node(leftval=244, rightval=-279,
                                                                                       left=Node(leftval=0,
                                                                                                 rightval=-788,
                                                                                                 left=None,
                                                                                                 right=Node()),
                                                                                       right=Node()),
                                                                             right=None),
                                                                   right=Node(leftval=-268, rightval=-803,
                                                                              left=Node(leftval=229, rightval=571,
                                                                                        left=Node(leftval=-627,
                                                                                                  rightval=502,
                                                                                                  left=Node(
                                                                                                      leftval=-352,
                                                                                                      rightval=0,
                                                                                                      left=Node(
                                                                                                          leftval=-722,
                                                                                                          rightval=0,
                                                                                                          left=Node(),
                                                                                                          right=None),
                                                                                                      right=None),
                                                                                                  right=Node()),
                                                                                        right=Node(leftval=867,
                                                                                                   rightval=-894,
                                                                                                   left=Node(leftval=0,
                                                                                                             rightval=814,
                                                                                                             left=None,
                                                                                                             right=Node()),
                                                                                                   right=Node(
                                                                                                       leftval=-203,
                                                                                                       rightval=0,
                                                                                                       left=Node(
                                                                                                           leftval=-363,
                                                                                                           rightval=631,
                                                                                                           left=Node(),
                                                                                                           right=Node(
                                                                                                               leftval=431,
                                                                                                               rightval=0,
                                                                                                               left=Node(),
                                                                                                               right=None)),
                                                                                                       right=None))),
                                                                              right=Node(leftval=-869, rightval=0,
                                                                                         left=Node(leftval=944,
                                                                                                   rightval=-207,
                                                                                                   left=Node(
                                                                                                       leftval=-164,
                                                                                                       rightval=0,
                                                                                                       left=Node(),
                                                                                                       right=None),
                                                                                                   right=Node(leftval=0,
                                                                                                              rightval=-610,
                                                                                                              left=None,
                                                                                                              right=Node(
                                                                                                                  leftval=643,
                                                                                                                  rightval=-460,
                                                                                                                  left=Node(
                                                                                                                      leftval=152,
                                                                                                                      rightval=738,
                                                                                                                      left=Node(),
                                                                                                                      right=Node()),
                                                                                                                  right=Node(
                                                                                                                      leftval=-938,
                                                                                                                      rightval=-71,
                                                                                                                      left=Node(),
                                                                                                                      right=Node())))),
                                                                                         right=None))))))),
             right=Node(leftval=258, rightval=-655,
                        left=Node(leftval=-25, rightval=-836,
                                  left=Node(),
                                  right=Node()),
                        right=Node(leftval=410, rightval=498,
                                   left=Node(leftval=122, rightval=425,
                                             left=Node(leftval=-685, rightval=861,
                                                       left=Node(leftval=-35, rightval=982,
                                                                 left=Node(leftval=0, rightval=713,
                                                                           left=None,
                                                                           right=Node()),
                                                                 right=Node(leftval=0, rightval=-799,
                                                                            left=None,
                                                                            right=Node(leftval=956, rightval=0,
                                                                                       left=Node(),
                                                                                       right=None))),
                                                       right=Node()),
                                             right=Node(leftval=-679, rightval=934,
                                                        left=Node(leftval=0, rightval=-229,
                                                                  left=None,
                                                                  right=Node()),
                                                        right=Node())),
                                   right=Node(leftval=-773, rightval=-454,
                                              left=Node(leftval=-973, rightval=-668,
                                                        left=Node(leftval=-11, rightval=963,
                                                                  left=Node(),
                                                                  right=Node(leftval=-952, rightval=0,
                                                                             left=Node(leftval=0, rightval=936,
                                                                                       left=None,
                                                                                       right=Node()),
                                                                             right=None)),
                                                        right=Node(leftval=156, rightval=578,
                                                                   left=Node(leftval=157, rightval=-718,
                                                                             left=Node(leftval=0, rightval=-538,
                                                                                       left=None,
                                                                                       right=Node(leftval=-513,
                                                                                                  rightval=-279,
                                                                                                  left=Node(),
                                                                                                  right=Node(
                                                                                                      leftval=978,
                                                                                                      rightval=0,
                                                                                                      left=Node(
                                                                                                          leftval=-652,
                                                                                                          rightval=0,
                                                                                                          left=Node(),
                                                                                                          right=None),
                                                                                                      right=None))),
                                                                             right=Node(leftval=0, rightval=795,
                                                                                        left=None,
                                                                                        right=Node(leftval=-256,
                                                                                                   rightval=0,
                                                                                                   left=Node(),
                                                                                                   right=None))),
                                                                   right=Node())),
                                              right=Node(leftval=235, rightval=51,
                                                         left=Node(leftval=0, rightval=9,
                                                                   left=None,
                                                                   right=Node(leftval=-723, rightval=677,
                                                                              left=Node(leftval=287, rightval=-268,
                                                                                        left=Node(leftval=-675,
                                                                                                  rightval=208,
                                                                                                  left=Node(
                                                                                                      leftval=-107,
                                                                                                      rightval=163,
                                                                                                      left=Node(
                                                                                                          leftval=0,
                                                                                                          rightval=687,
                                                                                                          left=None,
                                                                                                          right=Node()),
                                                                                                      right=Node(
                                                                                                          leftval=-946,
                                                                                                          rightval=-143,
                                                                                                          left=Node(
                                                                                                              leftval=594,
                                                                                                              rightval=0,
                                                                                                              left=Node(
                                                                                                                  leftval=0,
                                                                                                                  rightval=-698,
                                                                                                                  left=None,
                                                                                                                  right=Node(
                                                                                                                      leftval=0,
                                                                                                                      rightval=252,
                                                                                                                      left=None,
                                                                                                                      right=Node(
                                                                                                                          leftval=0,
                                                                                                                          rightval=173,
                                                                                                                          left=None,
                                                                                                                          right=Node()))),
                                                                                                              right=None),
                                                                                                          right=Node(
                                                                                                              leftval=0,
                                                                                                              rightval=613,
                                                                                                              left=None,
                                                                                                              right=Node()))),
                                                                                                  right=Node(
                                                                                                      leftval=-29,
                                                                                                      rightval=-159,
                                                                                                      left=Node(
                                                                                                          leftval=251,
                                                                                                          rightval=-342,
                                                                                                          left=Node(
                                                                                                              leftval=978,
                                                                                                              rightval=-803,
                                                                                                              left=Node(),
                                                                                                              right=Node(
                                                                                                                  leftval=-282,
                                                                                                                  rightval=0,
                                                                                                                  left=Node(
                                                                                                                      leftval=159,
                                                                                                                      rightval=348,
                                                                                                                      left=Node(),
                                                                                                                      right=Node(
                                                                                                                          leftval=0,
                                                                                                                          rightval=-165,
                                                                                                                          left=None,
                                                                                                                          right=Node())),
                                                                                                                  right=None)),
                                                                                                          right=Node(
                                                                                                              leftval=-435,
                                                                                                              rightval=-918,
                                                                                                              left=Node(
                                                                                                                  leftval=-15,
                                                                                                                  rightval=-187,
                                                                                                                  left=Node(
                                                                                                                      leftval=0,
                                                                                                                      rightval=876,
                                                                                                                      left=None,
                                                                                                                      right=Node(
                                                                                                                          leftval=-540,
                                                                                                                          rightval=0,
                                                                                                                          left=Node(),
                                                                                                                          right=None)),
                                                                                                                  right=Node(
                                                                                                                      leftval=321,
                                                                                                                      rightval=0,
                                                                                                                      left=Node(),
                                                                                                                      right=None)),
                                                                                                              right=Node(
                                                                                                                  leftval=795,
                                                                                                                  rightval=-515,
                                                                                                                  left=Node(
                                                                                                                      leftval=0,
                                                                                                                      rightval=237,
                                                                                                                      left=None,
                                                                                                                      right=Node(
                                                                                                                          leftval=110,
                                                                                                                          rightval=-956,
                                                                                                                          left=Node(),
                                                                                                                          right=Node())),
                                                                                                                  right=Node()))),
                                                                                                      right=Node(
                                                                                                          leftval=-653,
                                                                                                          rightval=-303,
                                                                                                          left=Node(
                                                                                                              leftval=999,
                                                                                                              rightval=0,
                                                                                                              left=Node(
                                                                                                                  leftval=0,
                                                                                                                  rightval=782,
                                                                                                                  left=None,
                                                                                                                  right=Node(
                                                                                                                      leftval=0,
                                                                                                                      rightval=497,
                                                                                                                      left=None,
                                                                                                                      right=Node(
                                                                                                                          leftval=0,
                                                                                                                          rightval=-138,
                                                                                                                          left=None,
                                                                                                                          right=Node(
                                                                                                                              leftval=572,
                                                                                                                              rightval=0,
                                                                                                                              left=Node(),
                                                                                                                              right=None)))),
                                                                                                              right=None),
                                                                                                          right=Node(
                                                                                                              leftval=-670,
                                                                                                              rightval=0,
                                                                                                              left=Node(
                                                                                                                  leftval=237,
                                                                                                                  rightval=-54,
                                                                                                                  left=Node(),
                                                                                                                  right=Node()),
                                                                                                              right=None)))),
                                                                                        right=Node(leftval=-293,
                                                                                                   rightval=-708,
                                                                                                   left=Node(),
                                                                                                   right=Node())),
                                                                              right=Node(leftval=-940, rightval=75,
                                                                                         left=Node(leftval=-119,
                                                                                                   rightval=181,
                                                                                                   left=Node(
                                                                                                       leftval=490,
                                                                                                       rightval=-574,
                                                                                                       left=Node(
                                                                                                           leftval=0,
                                                                                                           rightval=-449,
                                                                                                           left=None,
                                                                                                           right=Node(
                                                                                                               leftval=397,
                                                                                                               rightval=-160,
                                                                                                               left=Node(),
                                                                                                               right=Node(
                                                                                                                   leftval=-117,
                                                                                                                   rightval=-929,
                                                                                                                   left=Node(),
                                                                                                                   right=Node(
                                                                                                                       leftval=-404,
                                                                                                                       rightval=129,
                                                                                                                       left=Node(),
                                                                                                                       right=Node())))),
                                                                                                       right=Node()),
                                                                                                   right=Node(
                                                                                                       leftval=-661,
                                                                                                       rightval=-937,
                                                                                                       left=Node(
                                                                                                           leftval=0,
                                                                                                           rightval=-775,
                                                                                                           left=None,
                                                                                                           right=Node()),
                                                                                                       right=Node())),
                                                                                         right=Node(leftval=-664,
                                                                                                    rightval=-533,
                                                                                                    left=Node(
                                                                                                        leftval=592,
                                                                                                        rightval=-129,
                                                                                                        left=Node(),
                                                                                                        right=Node()),
                                                                                                    right=Node(
                                                                                                        leftval=-576,
                                                                                                        rightval=0,
                                                                                                        left=Node(
                                                                                                            leftval=0,
                                                                                                            rightval=-687,
                                                                                                            left=None,
                                                                                                            right=Node()),
                                                                                                        right=None))))),
                                                         right=Node(leftval=220, rightval=319,
                                                                    left=Node(leftval=803, rightval=873,
                                                                              left=Node(leftval=137, rightval=-375,
                                                                                        left=Node(leftval=841,
                                                                                                  rightval=-676,
                                                                                                  left=Node(leftval=0,
                                                                                                            rightval=583,
                                                                                                            left=None,
                                                                                                            right=Node()),
                                                                                                  right=Node()),
                                                                                        right=Node(leftval=515,
                                                                                                   rightval=523,
                                                                                                   left=Node(
                                                                                                       leftval=868,
                                                                                                       rightval=0,
                                                                                                       left=Node(),
                                                                                                       right=None),
                                                                                                   right=Node())),
                                                                              right=Node()),
                                                                    right=Node(leftval=429, rightval=-581,
                                                                               left=Node(leftval=399, rightval=993,
                                                                                         left=Node(leftval=47,
                                                                                                   rightval=0,
                                                                                                   left=Node(),
                                                                                                   right=None),
                                                                                         right=Node(leftval=664,
                                                                                                    rightval=-800,
                                                                                                    left=Node(),
                                                                                                    right=Node())),
                                                                               right=Node(leftval=595, rightval=325,
                                                                                          left=Node(),
                                                                                          right=Node(leftval=0,
                                                                                                     rightval=427,
                                                                                                     left=None,
                                                                                                     right=Node())))))))))

    return T, 999, -4037


def make_tree_10_199():
    T = Node(leftval=-381, rightval=-175,
             left=Node(leftval=432, rightval=0,
                       left=Node(leftval=221, rightval=-794,
                                 left=Node(leftval=-694, rightval=891,
                                           left=Node(leftval=-171, rightval=0,
                                                     left=Node(),
                                                     right=None),
                                           right=Node(leftval=-734, rightval=795,
                                                      left=Node(leftval=-467, rightval=-873,
                                                                left=Node(leftval=-582, rightval=979,
                                                                          left=Node(leftval=637, rightval=0,
                                                                                    left=Node(leftval=-806,
                                                                                              rightval=266,
                                                                                              left=Node(),
                                                                                              right=Node(leftval=547,
                                                                                                         rightval=0,
                                                                                                         left=Node(),
                                                                                                         right=None)),
                                                                                    right=None),
                                                                          right=Node(leftval=311, rightval=869,
                                                                                     left=Node(leftval=741,
                                                                                               rightval=400,
                                                                                               left=Node(),
                                                                                               right=Node(leftval=0,
                                                                                                          rightval=840,
                                                                                                          left=None,
                                                                                                          right=Node())),
                                                                                     right=Node(leftval=-353,
                                                                                                rightval=251,
                                                                                                left=Node(leftval=-276,
                                                                                                          rightval=0,
                                                                                                          left=Node(),
                                                                                                          right=None),
                                                                                                right=Node()))),
                                                                right=Node(leftval=67, rightval=0,
                                                                           left=Node(leftval=772, rightval=0,
                                                                                     left=Node(),
                                                                                     right=None),
                                                                           right=None)),
                                                      right=Node(leftval=390, rightval=551,
                                                                 left=Node(leftval=-406, rightval=-624,
                                                                           left=Node(leftval=0, rightval=447,
                                                                                     left=None,
                                                                                     right=Node(leftval=128,
                                                                                                rightval=-404,
                                                                                                left=Node(leftval=253,
                                                                                                          rightval=0,
                                                                                                          left=Node(),
                                                                                                          right=None),
                                                                                                right=Node(leftval=-777,
                                                                                                           rightval=-383,
                                                                                                           left=Node(
                                                                                                               leftval=644,
                                                                                                               rightval=0,
                                                                                                               left=Node(
                                                                                                                   leftval=981,
                                                                                                                   rightval=-709,
                                                                                                                   left=Node(
                                                                                                                       leftval=0,
                                                                                                                       rightval=441,
                                                                                                                       left=None,
                                                                                                                       right=Node()),
                                                                                                                   right=Node(
                                                                                                                       leftval=0,
                                                                                                                       rightval=645,
                                                                                                                       left=None,
                                                                                                                       right=Node(
                                                                                                                           leftval=0,
                                                                                                                           rightval=-512,
                                                                                                                           left=None,
                                                                                                                           right=Node()))),
                                                                                                               right=None),
                                                                                                           right=Node(
                                                                                                               leftval=2,
                                                                                                               rightval=0,
                                                                                                               left=Node(
                                                                                                                   leftval=910,
                                                                                                                   rightval=0,
                                                                                                                   left=Node(
                                                                                                                       leftval=0,
                                                                                                                       rightval=40,
                                                                                                                       left=None,
                                                                                                                       right=Node(
                                                                                                                           leftval=0,
                                                                                                                           rightval=792,
                                                                                                                           left=None,
                                                                                                                           right=Node())),
                                                                                                                   right=None),
                                                                                                               right=None)))),
                                                                           right=Node(leftval=0, rightval=-505,
                                                                                      left=None,
                                                                                      right=Node(leftval=-351,
                                                                                                 rightval=178,
                                                                                                 left=Node(leftval=221,
                                                                                                           rightval=634,
                                                                                                           left=Node(
                                                                                                               leftval=0,
                                                                                                               rightval=-89,
                                                                                                               left=None,
                                                                                                               right=Node()),
                                                                                                           right=Node()),
                                                                                                 right=Node()))),
                                                                 right=Node(leftval=-859, rightval=-817,
                                                                            left=Node(),
                                                                            right=Node(leftval=0, rightval=-25,
                                                                                       left=None,
                                                                                       right=Node()))))),
                                 right=Node(leftval=-44, rightval=-920,
                                            left=Node(leftval=0, rightval=715,
                                                      left=None,
                                                      right=Node()),
                                            right=Node(leftval=-875, rightval=31,
                                                       left=Node(leftval=-954, rightval=114,
                                                                 left=Node(leftval=-701, rightval=0,
                                                                           left=Node(leftval=-794, rightval=603,
                                                                                     left=Node(leftval=-4, rightval=0,
                                                                                               left=Node(leftval=254,
                                                                                                         rightval=-764,
                                                                                                         left=Node(),
                                                                                                         right=Node(
                                                                                                             leftval=-832,
                                                                                                             rightval=-336,
                                                                                                             left=Node(
                                                                                                                 leftval=352,
                                                                                                                 rightval=0,
                                                                                                                 left=Node(),
                                                                                                                 right=None),
                                                                                                             right=Node())),
                                                                                               right=None),
                                                                                     right=Node(leftval=670,
                                                                                                rightval=-873,
                                                                                                left=Node(leftval=-239,
                                                                                                          rightval=627,
                                                                                                          left=Node(),
                                                                                                          right=Node(
                                                                                                              leftval=0,
                                                                                                              rightval=-549,
                                                                                                              left=None,
                                                                                                              right=Node(
                                                                                                                  leftval=444,
                                                                                                                  rightval=0,
                                                                                                                  left=Node(),
                                                                                                                  right=None))),
                                                                                                right=Node(leftval=0,
                                                                                                           rightval=-128,
                                                                                                           left=None,
                                                                                                           right=Node()))),
                                                                           right=None),
                                                                 right=Node(leftval=918, rightval=391,
                                                                            left=Node(leftval=-569, rightval=489,
                                                                                      left=Node(leftval=470,
                                                                                                rightval=-747,
                                                                                                left=Node(leftval=0,
                                                                                                          rightval=300,
                                                                                                          left=None,
                                                                                                          right=Node(
                                                                                                              leftval=0,
                                                                                                              rightval=-746,
                                                                                                              left=None,
                                                                                                              right=Node())),
                                                                                                right=Node(leftval=987,
                                                                                                           rightval=-622,
                                                                                                           left=Node(),
                                                                                                           right=Node(
                                                                                                               leftval=-602,
                                                                                                               rightval=968,
                                                                                                               left=Node(
                                                                                                                   leftval=0,
                                                                                                                   rightval=240,
                                                                                                                   left=None,
                                                                                                                   right=Node(
                                                                                                                       leftval=-926,
                                                                                                                       rightval=0,
                                                                                                                       left=Node(),
                                                                                                                       right=None)),
                                                                                                               right=Node()))),
                                                                                      right=Node()),
                                                                            right=Node())),
                                                       right=Node(leftval=-107, rightval=-631,
                                                                  left=Node(leftval=-548, rightval=0,
                                                                            left=Node(leftval=0, rightval=-857,
                                                                                      left=None,
                                                                                      right=Node()),
                                                                            right=None),
                                                                  right=Node(leftval=0, rightval=-283,
                                                                             left=None,
                                                                             right=Node()))))),
                       right=None),
             right=Node(leftval=492, rightval=-855,
                        left=Node(leftval=-44, rightval=-898,
                                  left=Node(leftval=-35, rightval=395,
                                            left=Node(leftval=979, rightval=571,
                                                      left=Node(leftval=428, rightval=0,
                                                                left=Node(),
                                                                right=None),
                                                      right=Node()),
                                            right=Node(leftval=0, rightval=-973,
                                                       left=None,
                                                       right=Node(leftval=-642, rightval=0,
                                                                  left=Node(leftval=-95, rightval=363,
                                                                            left=Node(),
                                                                            right=Node(leftval=222, rightval=887,
                                                                                       left=Node(),
                                                                                       right=Node())),
                                                                  right=None))),
                                  right=Node(leftval=-361, rightval=715,
                                             left=Node(leftval=-936, rightval=-177,
                                                       left=Node(leftval=-997, rightval=217,
                                                                 left=Node(leftval=697, rightval=332,
                                                                           left=Node(leftval=-724, rightval=-509,
                                                                                     left=Node(leftval=-63,
                                                                                               rightval=518,
                                                                                               left=Node(leftval=414,
                                                                                                         rightval=0,
                                                                                                         left=Node(
                                                                                                             leftval=148,
                                                                                                             rightval=0,
                                                                                                             left=Node(),
                                                                                                             right=None),
                                                                                                         right=None),
                                                                                               right=Node()),
                                                                                     right=Node(leftval=0,
                                                                                                rightval=-425,
                                                                                                left=None,
                                                                                                right=Node(leftval=114,
                                                                                                           rightval=0,
                                                                                                           left=Node(),
                                                                                                           right=None))),
                                                                           right=Node(leftval=532, rightval=-152,
                                                                                      left=Node(leftval=208,
                                                                                                rightval=939,
                                                                                                left=Node(),
                                                                                                right=Node()),
                                                                                      right=Node(leftval=0,
                                                                                                 rightval=-206,
                                                                                                 left=None,
                                                                                                 right=Node()))),
                                                                 right=Node()),
                                                       right=Node(leftval=791, rightval=-152,
                                                                  left=Node(),
                                                                  right=Node(leftval=379, rightval=163,
                                                                             left=Node(),
                                                                             right=Node(leftval=0, rightval=792,
                                                                                        left=None,
                                                                                        right=Node(leftval=454,
                                                                                                   rightval=0,
                                                                                                   left=Node(),
                                                                                                   right=None))))),
                                             right=Node(leftval=-333, rightval=0,
                                                        left=Node(leftval=-921, rightval=12,
                                                                  left=Node(leftval=812, rightval=0,
                                                                            left=Node(leftval=0, rightval=80,
                                                                                      left=None,
                                                                                      right=Node(leftval=-678,
                                                                                                 rightval=-86,
                                                                                                 left=Node(),
                                                                                                 right=Node(leftval=0,
                                                                                                            rightval=436,
                                                                                                            left=None,
                                                                                                            right=Node()))),
                                                                            right=None),
                                                                  right=Node(leftval=810, rightval=0,
                                                                             left=Node(),
                                                                             right=None)),
                                                        right=None))),
                        right=Node(leftval=755, rightval=71,
                                   left=Node(leftval=394, rightval=-469,
                                             left=Node(leftval=-353, rightval=-994,
                                                       left=Node(leftval=0, rightval=389,
                                                                 left=None,
                                                                 right=Node(leftval=944, rightval=0,
                                                                            left=Node(leftval=0, rightval=-178,
                                                                                      left=None,
                                                                                      right=Node()),
                                                                            right=None)),
                                                       right=Node()),
                                             right=Node(leftval=-917, rightval=-579,
                                                        left=Node(leftval=0, rightval=-627,
                                                                  left=None,
                                                                  right=Node(leftval=0, rightval=410,
                                                                             left=None,
                                                                             right=Node(leftval=0, rightval=-427,
                                                                                        left=None,
                                                                                        right=Node(leftval=0,
                                                                                                   rightval=-381,
                                                                                                   left=None,
                                                                                                   right=Node(leftval=0,
                                                                                                              rightval=789,
                                                                                                              left=None,
                                                                                                              right=Node()))))),
                                                        right=Node(leftval=-962, rightval=-914,
                                                                   left=Node(),
                                                                   right=Node(leftval=-430, rightval=743,
                                                                              left=Node(leftval=66, rightval=0,
                                                                                        left=Node(leftval=0,
                                                                                                  rightval=338,
                                                                                                  left=None,
                                                                                                  right=Node(leftval=0,
                                                                                                             rightval=-727,
                                                                                                             left=None,
                                                                                                             right=Node(
                                                                                                                 leftval=764,
                                                                                                                 rightval=-475,
                                                                                                                 left=Node(),
                                                                                                                 right=Node()))),
                                                                                        right=None),
                                                                              right=Node(leftval=-684, rightval=0,
                                                                                         left=Node(leftval=785,
                                                                                                   rightval=0,
                                                                                                   left=Node(),
                                                                                                   right=None),
                                                                                         right=None))))),
                                   right=Node(leftval=-370, rightval=-633,
                                              left=Node(leftval=-408, rightval=-261,
                                                        left=Node(leftval=-445, rightval=-318,
                                                                  left=Node(leftval=784, rightval=0,
                                                                            left=Node(leftval=0, rightval=-238,
                                                                                      left=None,
                                                                                      right=Node(leftval=-109,
                                                                                                 rightval=0,
                                                                                                 left=Node(leftval=311,
                                                                                                           rightval=0,
                                                                                                           left=Node(),
                                                                                                           right=None),
                                                                                                 right=None)),
                                                                            right=None),
                                                                  right=Node(leftval=-717, rightval=-691,
                                                                             left=Node(),
                                                                             right=Node(leftval=-982, rightval=0,
                                                                                        left=Node(),
                                                                                        right=None))),
                                                        right=Node(leftval=-694, rightval=194,
                                                                   left=Node(leftval=-308, rightval=0,
                                                                             left=Node(),
                                                                             right=None),
                                                                   right=Node(leftval=-665, rightval=0,
                                                                              left=Node(leftval=0, rightval=-448,
                                                                                        left=None,
                                                                                        right=Node()),
                                                                              right=None))),
                                              right=Node(leftval=912, rightval=-902,
                                                         left=Node(leftval=-21, rightval=0,
                                                                   left=Node(leftval=0, rightval=-765,
                                                                             left=None,
                                                                             right=Node()),
                                                                   right=None),
                                                         right=Node())))))
    return T, 199, -8374


def make_tree_gen_1():
    """
    k = 1
    solution value = max edge
    """
    random.seed(0, version=2)
    size = 8
    # minval = -1000
    minval = 1
    maxval = 1000

    max_edge = minval - 1

    def gen_subtree(size: int):
        nonlocal max_edge

        if size == 0:
            return None
        left_size = random.randint(0, size - 1)
        right_size = size - 1 - left_size
        l = gen_subtree(left_size)
        r = gen_subtree(right_size)
        lval = random.randint(minval, maxval) if l is not None else 0
        rval = random.randint(minval, maxval) if r is not None else 0
        max_edge = max(max_edge, lval, rval)
        return Node(
            right=r,
            rightval=rval,
            left=l,
            leftval=lval
        )

    T = gen_subtree(size=size)
    # print(f"Generated a tree with a max edge: {max_edge}")
    # print(T)
    return T, 1, max_edge


def make_tree_gen_2():
    """
    k = number of edges
    solution value = sum of all edges
    """
    random.seed(0, version=2)
    size = 200
    minval = -1000
    maxval = 1000

    sum_edge = 0
    edge_count = 0

    def gen_subtree(size: int):
        nonlocal sum_edge
        nonlocal edge_count

        if size == 0:
            return None
        left_size = random.randint(0, size - 1)
        right_size = size - 1 - left_size
        l = gen_subtree(left_size)
        r = gen_subtree(right_size)
        lval = random.randint(minval, maxval) if l is not None else 0
        rval = random.randint(minval, maxval) if r is not None else 0
        if l is not None:
            edge_count += 1
        if r is not None:
            edge_count += 1
        sum_edge = sum_edge + lval + rval
        return Node(
            right=r,
            rightval=rval,
            left=l,
            leftval=lval
        )

    T = gen_subtree(size=size)
    # print(f"Generated a tree with a max edge: {sum_edge}")
    print(T)
    return T, edge_count, sum_edge


tests: List[Tuple[Node, int, int]] = [
    #   (None, 0, 0),
    # (None, 1, None),
    make_tree_1(),
    make_tree_2(),
    make_tree_3(),
    make_tree_4(),
    make_tree_5(),
    make_tree_6(),
    make_tree_7(),
    make_tree_8(),
    make_tree_10_199(),
    #    make_tree_9_999_too_big(),
    #    make_tree_10_199(),
    # make_tree_gen_1(),
    # make_tree_gen_2(),
]


def runtests(f):
    problems_count = 0
    for i, test in enumerate(tests):
        print("---------------------")
        print(f"Test {i + 1}")
        T, k, expected = test

        actual = f(T, k)
        if actual == expected:
            print(f"OK, k: {k}, suma: {actual}")
        else:
            problems_count += 1
            print(f"Problemy! k={k}, Oczekiwane: {expected} != uzyskane: {actual}")

    print("---------------")
    if problems_count > 0:
        print(f"PROBLEMY!! Jest ich {problems_count}")
    else:
        print("Wszystko OK")
