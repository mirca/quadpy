# -*- coding: utf-8 -*-
#
from .helpers import _s4, _s31, _s22, _s211

from ..helpers import untangle


class Keast(object):
    '''
    P. Keast,
    Moderate degree tetrahedral quadrature formulas,
    CMAME 55: 339-348
    1986,
    <http://dx.doi.org/10.1016/0045-7825(86)90059-9>.

    Abstract:
    Quadrature formulas of degrees 4 to 8 for numerical integration over the
    tetrahedron are constructed. The formulas are fully symmetric with respect
    to the tetrahedron, and in some cases are the minimum point rules with this
    symmetry.

    https://people.sc.fsu.edu/~jburkardt/datasets/quadrature_rules_tet/quadrature_rules_tet.html
    '''
    def __init__(self, index):
        if index == 0:
            # Does not appear in Keast's article.
            self.degree = 1
            data = [
                (1.0, _s4())
                ]
        elif index == 1:
            # Does not appear in Keast's article.
            self.degree = 2
            data = [
                (0.25, _s31(0.1381966011250105))
                ]
        elif index == 2:
            # Does not appear in Keast's article.
            data = [
                (-0.8, _s4()),
                (0.45, _s31(1.0/6.0)),
                ]
            self.degree = 3
        elif index == 3:
            # Does not appear in Keast's article.
            self.degree = 3
            data = [
                (0.2177650698804054, _s31(0.1438564719343852)),
                (0.0214899534130631, _s22(0.5)),
                ]
        elif index == 4:
            self.degree = 4
            data = [
                (-148.0/1875.0, _s4()),
                (+343.0/7500.0, _s31(1.0/14.0)),
                (+56.0/375.0, _s22(0.3994035761667992)),
                ]
        elif index == 5:
            self.degree = 4
            data = [
                (2.0/105.0, _s22(0.5)),
                (0.0885898247429807, _s31(0.1005267652252045)),
                (0.1328387466855907, _s31(0.3143728734931922)),
                ]
        elif index == 6:
            self.degree = 5
            data = [
                (6544.0 / 36015.0, _s4()),
                (81.0 / 2240.0, _s31(1.0/3.0)),
                (161051.0 / 2304960.0, _s31(1.0/11.0)),
                (338.0 / 5145.0, _s22(0.0665501535736643)),
                ]
        elif index == 7:
            self.degree = 6
            data = [
                (0.0399227502581679, _s31(0.2146028712591517)),
                (0.0100772110553207, _s31(0.0406739585346113)),
                (0.0553571815436544, _s31(0.3223378901422757)),
                (27.0/560.0, _s211(0.0636610018750175, 0.2696723314583159)),
                ]
        elif index == 8:
            self.degree = 7
            data = [
                (+0.1095853407966528, _s4()),
                (+0.0635996491464850, _s31(0.0782131923303186)),
                (-0.3751064406859797, _s31(0.1218432166639044)),
                (+0.0293485515784412, _s31(0.3325391644464206)),
                (+0.0058201058201058, _s22(0.5)),
                (+0.1653439153439105, _s211(0.1, 0.2)),
                ]
        elif index == 9:
            self.degree = 8
            data = [
                (-0.2359620398477557, _s4()),
                (+0.0244878963560562, _s31(0.1274709365666390)),
                (+0.0039485206398261, _s31(0.0320788303926323)),
                (+0.0263055529507371, _s22(0.0497770956432810)),
                (+0.0829803830550589, _s22(0.1837304473985499)),
                (+0.0254426245481023, _s211(0.2319010893971509, 0.5132800333608811)),
                (+0.0134324384376852, _s211(0.0379700484718286, 0.1937464752488044)),
                ]
        else:
            assert index == 10
            self.degree = 8
            # In Keast's article, the first weight is incorrectly given with a
            # positive sign.
            data = [
                (-0.393270066412926145e-01, _s4()),
                (+0.408131605934270525e-02, _s31(0.127470936566639015e-00)),
                (+0.658086773304341943e-03, _s31(0.320788303926322960e-01)),
                (+0.438425882512284693e-02, _s22(0.497770956432810185e-01)),
                (+0.138300638425098166e-01, _s22(0.183730447398549945e-00)),
                (+0.424043742468372453e-02, _s211(0.231901089397150906e-00, 0.229177878448171174e-01)),
                (+0.223873973961420164e-02, _s211(0.379700484718286102e-01, 0.730313427807538396e-00)),
                ]

        self.bary, self.weights = untangle(data)
        if index == 10:
            self.weights *= 6
        self.points = self.bary[:, 1:]
        return
