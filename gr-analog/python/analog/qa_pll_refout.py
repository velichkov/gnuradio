#!/usr/bin/env python
#
# Copyright 2004,2010,2012,2013 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
#

from __future__ import division

import math

from gnuradio import gr, gr_unittest, analog, blocks

class test_pll_refout(gr_unittest.TestCase):

    def setUp(self):
        self.tb = gr.top_block()

    def tearDown(self):
        self.tb = None

    def test_pll_refout(self):
        expected_result = ((1+0j),
                            (1+6.408735764296125e-10j),
                            (0.9999844431877136+0.005577784031629562j),
                            (0.9998642802238464+0.016474783420562744j),
                            (0.9994739890098572+0.032431427389383316j),
                            (0.9985847473144531+0.05318402871489525j),
                            (0.996917188167572+0.07846084982156754j),
                            (0.9941533207893372+0.10797744989395142j),
                            (0.9899479150772095+0.14143235981464386j),
                            (0.9839394092559814+0.1785029172897339j),
                            (0.9757603406906128+0.2188417762517929j),
                            (0.9650475978851318+0.26207470893859863j),
                            (0.9514514803886414+0.30779871344566345j),
                            (0.9346449971199036+0.35558223724365234j),
                            (0.9143316149711609+0.40496626496315j),
                            (0.8902531862258911+0.4554659426212311j),
                            (0.8621962666511536+0.5065743923187256j),
                            (0.8299974799156189+0.5577671527862549j),
                            (0.7935484647750854+0.6085070967674255j),
                            (0.7527987360954285+0.6582507491111755j),
                            (0.7077582478523254+0.7064547538757324j),
                            (0.6584978699684143+0.7525825500488281j),
                            (0.6051493883132935+0.7961119413375854j),
                            (0.547903835773468+0.8365413546562195j),
                            (0.48700881004333496+0.8733970522880554j),
                            (0.42276495695114136+0.90623939037323j),
                            (0.35552138090133667+0.9346681237220764j),
                            (0.2856702208518982+0.9583280086517334j),
                            (0.21364101767539978+0.976912260055542j),
                            (0.13989387452602386+0.9901664853096008j),
                            (0.06491273641586304+0.9978909492492676j),
                            (-0.01080091018229723+0.9999416470527649j),
                            (-0.08673560619354248+0.9962313771247864j),
                            (-0.16237612068653107+0.9867289662361145j),
                            (-0.23721040785312653+0.9714583158493042j),
                            (-0.3107353150844574+0.95049649477005j),
                            (-0.3824624717235565+0.9239710569381714j),
                            (-0.45192304253578186+0.892056941986084j),
                            (-0.5186731219291687+0.8549726009368896j),
                            (-0.5822963714599609+0.812976598739624j),
                            (-0.6424083709716797+0.7663624882698059j),
                            (-0.6986585855484009+0.7154552340507507j),
                            (-0.7507330775260925+0.6606056690216064j),
                            (-0.7983550429344177+0.6021870970726013j),
                            (-0.841286301612854+0.5405898094177246j),
                            (-0.879327654838562+0.47621726989746094j),
                            (-0.912318229675293+0.4094819128513336j),
                            (-0.9401354789733887+0.340800940990448j),
                            (-0.9626938104629517+0.27059316635131836j),
                            (-0.979943573474884+0.1992751508951187j),
                            (-0.9918696284294128+0.12725839018821716j),
                            (-0.9984893202781677+0.054946307092905045j),
                            (-0.9998509287834167-0.017267409712076187j),
                            (-0.9960314631462097-0.08900183439254761j),
                            (-0.9871346950531006-0.1598907858133316j),
                            (-0.9732890129089355-0.2295832633972168j),
                            (-0.9546451568603516-0.29774588346481323j),
                            (-0.9313743710517883-0.3640628457069397j),
                            (-0.9036663174629211-0.42823725938796997j),
                            (-0.8717266321182251-0.48999255895614624j),
                            (-0.8357754945755005-0.5490713119506836j),
                            (-0.7960456013679504-0.6052366495132446j),
                            (-0.7527803182601929-0.658271849155426j),
                            (-0.706232488155365-0.7079799771308899j),
                            (-0.6566619873046875-0.7541850209236145j),
                            (-0.6043350696563721-0.7967302799224854j),
                            (-0.5495226979255676-0.8354787826538086j),
                            (-0.4924990236759186-0.8703129887580872j),
                            (-0.4335414469242096-0.9011335968971252j),
                            (-0.3729270100593567-0.927860677242279j),
                            (-0.3109343349933624-0.9504314064979553j),
                            (-0.2478405237197876-0.9688008427619934j),
                            (-0.18392162024974823-0.9829409122467041j),
                            (-0.11945075541734695-0.9928401112556458j),
                            (-0.05469784513115883-0.9985029697418213j),
                            (0.010069688782095909-0.9999492764472961j),
                            (0.07459097355604172-0.9972141981124878j),
                            (0.13860897719860077-0.9903472065925598j),
                            (0.2018725872039795-0.979411780834198j),
                            (0.2641367018222809-0.964485228061676j),
                            (0.32516375184059143-0.9456577301025391j),
                            (0.3847236633300781-0.9230318069458008j),
                            (0.44259318709373474-0.8967224955558777j),
                            (0.49855801463127136-0.8668563365936279j),
                            (0.5524120926856995-0.8335711359977722j),
                            (0.6039596796035767-0.7970148921012878j),
                            (0.6530137062072754-0.7573460936546326j),
                            (0.6993972063064575-0.7147331833839417j),
                            (0.7429447770118713-0.6693527102470398j),
                            (0.7835012078285217-0.6213902235031128j),
                            (0.8209227919578552-0.5710391998291016j),
                            (0.8550769090652466-0.5185011625289917j),
                            (0.8858439326286316-0.46398329734802246j),
                            (0.9131162166595459-0.4076994061470032j),
                            (0.936798632144928-0.3498689830303192j),
                            (0.956809401512146-0.2907160222530365j),
                            (0.9730796813964844-0.23046888411045074j),
                            (0.9855544567108154-0.16935895383358002j),
                            (0.9941920042037964-0.10762103646993637j),
                            (0.9989647269248962-0.045491550117731094j)) 

        sampling_freq = 10e3
        freq = sampling_freq / 100

        loop_bw = math.pi / 100.0
        maxf = 1
        minf = -1

        src = analog.sig_source_c(sampling_freq, analog.GR_COS_WAVE, freq, 1.0)
        pll = analog.pll_refout_cc(loop_bw, maxf, minf)
        head = blocks.head(gr.sizeof_gr_complex, int (freq))
        dst = blocks.vector_sink_c()

        self.tb.connect(src, pll, head)
        self.tb.connect(head, dst)

        self.tb.run()
        dst_data = dst.data()
        self.assertComplexTuplesAlmostEqual(expected_result, dst_data, 4)

if __name__ == '__main__':
    gr_unittest.run(test_pll_refout)
