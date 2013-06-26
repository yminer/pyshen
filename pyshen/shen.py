"""
The License
-----------
The user is free to produce commercial applications with the software, to
distribute these applications in source or binary form, and to charge monies
for them as he sees fit and in concordance with the laws of the land subject
to the following license.

1. The license applies to all the software and all derived software and must
   appear on such.

2. It is illegal to distribute the software without this license attached to
   it and use of the software implies agreement with the license as such. It
   is illegal for anyone who is not the copyright holder to tamper with or
   change the license.

3. Neither the names of Lambda Associates or the copyright holder may be used
   to endorse or promote products built using the software without specific
   prior written permission from the copyright holder.

4. That possession of this license does not confer on the copyright holder any
   special contractual obligation towards the user. That in no event shall the
   copyright holder be liable for any direct, indirect, incidental, special,
   exemplary or consequential damages (including but not limited to
   procurement of substitute goods or services, loss of use, data, or profits;
   or business interruption), however caused and on any theory of liability,
   whether in contract, strict liability or tort (including negligence)
   arising in any way out of the use of the software, even if advised of the
   possibility of such damage.

5. It is permitted for the user to change the software, for the purpose of
   improving performance, correcting an error, or porting to a new platform,
   and distribute the modified version of Shen (hereafter the modified
   version) provided the resulting program conforms in all respects to the
   Shen standard and is issued under that title. The user must make it clear
   with his distribution that he/she is the author of the changes and what
   these changes are and why.

6. Derived versions of this software in whatever form are subject to the same
   restrictions. In particular it is not permitted to make derived copies of
   this software which do not conform to the Shen standard or appear under a
   different title.

7. It is permitted to distribute versions of Shen which incorporate libraries,
   graphics or other facilities which are not part of the Shen standard.

For an explication of this license see
[http://www.lambdassociates.org/News/june11/license.htm] which explains this
license in full.
"""


import sys
from pyshen import *

class SymDic:
    symdic_XVx47Y = Sym('XV/Y')
    symdic_shen_x60sidex45conditionsx62 = Sym('shen.<side-conditions>')
    symdic_shen_line = Sym('shen.line')
    symdic_shen_free_variable_check = Sym('shen.free_variable_check')
    symdic_kl_findall = Sym('findall')
    symdic_V1369 = Sym('V1369')
    symdic_Parse_shen_x60st_input1x62 = Sym('Parse_shen.<st_input1>')
    symdic_shen_linearise_help = Sym('shen.linearise_help')
    symdic_V1364 = Sym('V1364')
    symdic_V2601 = Sym('V2601')
    symdic_Cases = Sym('Cases')
    symdic_Typecheck = Sym('Typecheck')
    symdic_CCRules = Sym('CCRules')
    symdic_shen_ue = Sym('shen.ue')
    symdic_kl_consx63 = Sym('cons?')
    symdic_kl_vector = Sym('vector')
    symdic_shen_x60whitespacesx62 = Sym('shen.<whitespaces>')
    symdic_shen_x60numx62 = Sym('shen.<num>')
    symdic_shen_condx45form = Sym('shen.cond-form')
    symdic_shen_mod = Sym('shen.mod')
    symdic_V819 = Sym('V819')
    symdic_V818 = Sym('V818')
    symdic_shen_tcx45rules = Sym('shen.tc-rules')
    symdic_V811 = Sym('V811')
    symdic_kl_x43 = Sym('+')
    symdic_V812 = Sym('V812')
    symdic_V817 = Sym('V817')
    symdic_V1185 = Sym('V1185')
    symdic_V1184 = Sym('V1184')
    symdic_shen_update_history = Sym('shen.update_history')
    symdic_V1181 = Sym('V1181')
    symdic_V1180 = Sym('V1180')
    symdic_V1183 = Sym('V1183')
    symdic_V1182 = Sym('V1182')
    symdic_V780 = Sym('V780')
    symdic_V783 = Sym('V783')
    symdic_V785 = Sym('V785')
    symdic_V784 = Sym('V784')
    symdic_V787 = Sym('V787')
    symdic_V786 = Sym('V786')
    symdic_V788 = Sym('V788')
    symdic_shen_add_test = Sym('shen.add_test')
    symdic_kl_specialise = Sym('specialise')
    symdic_shen_letx45macro = Sym('shen.let-macro')
    symdic_V2877 = Sym('V2877')
    symdic_kl_x38x38 = Sym('&&')
    symdic_Curry = Sym('Curry')
    symdic_kl_tlstr = Sym('tlstr')
    symdic_shen_prologx45macro = Sym('shen.prolog-macro')
    symdic_Shen = Sym('Shen')
    symdic_shen_singleunderlinex63 = Sym('shen.singleunderline?')
    symdic_V1988 = Sym('V1988')
    symdic_V1985 = Sym('V1985')
    symdic_V1984 = Sym('V1984')
    symdic_V1987 = Sym('V1987')
    symdic_V1986 = Sym('V1986')
    symdic_V1980 = Sym('V1980')
    symdic_V1983 = Sym('V1983')
    symdic_V1133 = Sym('V1133')
    symdic_Group = Sym('Group')
    symdic_shen_x60commentx62 = Sym('shen.<comment>')
    symdic_V2852 = Sym('V2852')
    symdic_V2853 = Sym('V2853')
    symdic_shen_pvarx63 = Sym('shen.pvar?')
    symdic_V2851 = Sym('V2851')
    symdic_V2856 = Sym('V2856')
    symdic_V2857 = Sym('V2857')
    symdic_V2854 = Sym('V2854')
    symdic_V2855 = Sym('V2855')
    symdic_V2858 = Sym('V2858')
    symdic_V2859 = Sym('V2859')
    symdic_kl_unit = Sym('unit')
    symdic_V960 = Sym('V960')
    symdic_V2520 = Sym('V2520')
    symdic_V2521 = Sym('V2521')
    symdic_V965 = Sym('V965')
    symdic_V2527 = Sym('V2527')
    symdic_shen_complexity_head = Sym('shen.complexity_head')
    symdic_V2528 = Sym('V2528')
    symdic_shen_x42signedfuncsx42 = Sym('shen.*signedfuncs*')
    symdic_kl_tail = Sym('tail')
    symdic_Xx38x38 = Sym('X&&')
    symdic_V3039 = Sym('V3039')
    symdic_V3038 = Sym('V3038')
    symdic_kl_call = Sym('call')
    symdic_V3033 = Sym('V3033')
    symdic_V3032 = Sym('V3032')
    symdic_V3031 = Sym('V3031')
    symdic_V3030 = Sym('V3030')
    symdic_kl_type = Sym('type')
    symdic_V3036 = Sym('V3036')
    symdic_V3035 = Sym('V3035')
    symdic_V3034 = Sym('V3034')
    symdic_shen_getx45syntaxx43semantics = Sym('shen.get-syntax+semantics')
    symdic_V1763 = Sym('V1763')
    symdic_V1762 = Sym('V1762')
    symdic_V1765 = Sym('V1765')
    symdic_V1764 = Sym('V1764')
    symdic_V1767 = Sym('V1767')
    symdic_V1766 = Sym('V1766')
    symdic_V1769 = Sym('V1769')
    symdic_V1768 = Sym('V1768')
    symdic_shen_rememberx45datatype = Sym('shen.remember-datatype')
    symdic_Rule = Sym('Rule')
    symdic_V2517 = Sym('V2517')
    symdic_NewLineread = Sym('NewLineread')
    symdic_V = Sym('V')
    symdic_shen_internx45type = Sym('shen.intern-type')
    symdic_shen_explodex45h = Sym('shen.explode-h')
    symdic_shen_cc_body = Sym('shen.cc_body')
    symdic_V2298 = Sym('V2298')
    symdic_V2299 = Sym('V2299')
    symdic_V2292 = Sym('V2292')
    symdic_V2293 = Sym('V2293')
    symdic_V2294 = Sym('V2294')
    symdic_V2295 = Sym('V2295')
    symdic_V2296 = Sym('V2296')
    symdic_V2988 = Sym('V2988')
    symdic_V2989 = Sym('V2989')
    symdic_V2459 = Sym('V2459')
    symdic_V2984 = Sym('V2984')
    symdic_V2985 = Sym('V2985')
    symdic_V2986 = Sym('V2986')
    symdic_V2987 = Sym('V2987')
    symdic_V2980 = Sym('V2980')
    symdic_V2981 = Sym('V2981')
    symdic_V2982 = Sym('V2982')
    symdic_V2983 = Sym('V2983')
    symdic_V2276 = Sym('V2276')
    symdic_V2277 = Sym('V2277')
    symdic_V2274 = Sym('V2274')
    symdic_V2275 = Sym('V2275')
    symdic_shen_aritycheck = Sym('shen.aritycheck')
    symdic_shen_single = Sym('shen.single')
    symdic_V2515 = Sym('V2515')
    symdic_V2278 = Sym('V2278')
    symdic_V2279 = Sym('V2279')
    symdic_Abs = Sym('Abs')
    symdic_shen_readx45error = Sym('shen.read-error')
    symdic_shen_unbindv = Sym('shen.unbindv')
    symdic_V2185 = Sym('V2185')
    symdic_V2186 = Sym('V2186')
    symdic_V2187 = Sym('V2187')
    symdic_V2180 = Sym('V2180')
    symdic_V2874 = Sym('V2874')
    symdic_V2514 = Sym('V2514')
    symdic_V2188 = Sym('V2188')
    symdic_V2189 = Sym('V2189')
    symdic_V2875 = Sym('V2875')
    symdic_V2678 = Sym('V2678')
    symdic_V2679 = Sym('V2679')
    symdic_V2876 = Sym('V2876')
    symdic_Atom = Sym('Atom')
    symdic_V2672 = Sym('V2672')
    symdic_V2673 = Sym('V2673')
    symdic_V2670 = Sym('V2670')
    symdic_V694 = Sym('V694')
    symdic_V2676 = Sym('V2676')
    symdic_V2677 = Sym('V2677')
    symdic_V2674 = Sym('V2674')
    symdic_V2675 = Sym('V2675')
    symdic_A = Sym('A')
    symdic_V2509 = Sym('V2509')
    symdic_shen_x42varcounterx42 = Sym('shen.*varcounter*')
    symdic_shen_constructx45basex45searchx45clause = Sym('shen.construct-base-search-clause')
    symdic_shen_x60typex62 = Sym('shen.<type>')
    symdic_V2410 = Sym('V2410')
    symdic_V2512 = Sym('V2512')
    symdic_kl_datatype = Sym('datatype')
    symdic_V1500 = Sym('V1500')
    symdic_kl_readx45byte = Sym('read-byte')
    symdic_V1263 = Sym('V1263')
    symdic_V1505 = Sym('V1505')
    symdic_V808 = Sym('V808')
    symdic_V2073 = Sym('V2073')
    symdic_V2078 = Sym('V2078')
    symdic_shen_prologx45failure = Sym('shen.prolog-failure')
    symdic_V2502 = Sym('V2502')
    symdic_V2503 = Sym('V2503')
    symdic_V2511 = Sym('V2511')
    symdic_VectorElement = Sym('VectorElement')
    symdic_V2821 = Sym('V2821')
    symdic_V2504 = Sym('V2504')
    symdic_shen_x60commax62 = Sym('shen.<comma>')
    symdic_kl_synonyms = Sym('synonyms')
    symdic_shen_uex63 = Sym('shen.ue?')
    symdic_V1217 = Sym('V1217')
    symdic_V1216 = Sym('V1216')
    symdic_kl_fix = Sym('fix')
    symdic_V1219 = Sym('V1219')
    symdic_Eval = Sym('Eval')
    symdic_CodePoint = Sym('CodePoint')
    symdic_shen_vectorx45x62str = Sym('shen.vector->str')
    symdic_Yx45orx45N = Sym('Y-or-N')
    symdic_V1178 = Sym('V1178')
    symdic_V1179 = Sym('V1179')
    symdic_shen_ues = Sym('shen.ues')
    symdic_shen_rightx45rule = Sym('shen.right-rule')
    symdic_V1172 = Sym('V1172')
    symdic_V1173 = Sym('V1173')
    symdic_V1174 = Sym('V1174')
    symdic_V1175 = Sym('V1175')
    symdic_V1177 = Sym('V1177')
    symdic_shen_initialise_environment = Sym('shen.initialise_environment')
    symdic_V1379 = Sym('V1379')
    symdic_V1374 = Sym('V1374')
    symdic_kl_explode = Sym('explode')
    symdic_V885 = Sym('V885')
    symdic_Check = Sym('Check')
    symdic_NewHyp = Sym('NewHyp')
    symdic_V2489 = Sym('V2489')
    symdic_shen_clausesx45tox45shen = Sym('shen.clauses-to-shen')
    symdic_shen_mkx45pvar = Sym('shen.mk-pvar')
    symdic_V1665 = Sym('V1665')
    symdic_shen_x60patternsx62 = Sym('shen.<patterns>')
    symdic_Type = Sym('Type')
    symdic_shen_tx42x45def = Sym('shen.t*-def')
    symdic_shen_iterx45list = Sym('shen.iter-list')
    symdic_shen_x60rrbx62 = Sym('shen.<rrb>')
    symdic_shen_curryx45type = Sym('shen.curry-type')
    symdic_V1746 = Sym('V1746')
    symdic_shen_thx42 = Sym('shen.th*')
    symdic_V1744 = Sym('V1744')
    symdic_shen_compose = Sym('shen.compose')
    symdic_shen_packagex45macro = Sym('shen.package-macro')
    symdic_V1742 = Sym('V1742')
    symdic_kl_nth = Sym('nth')
    symdic_W = Sym('W')
    symdic_Parse_shen_x60predigitsx62 = Sym('Parse_shen.<predigits>')
    symdic_V2486 = Sym('V2486')
    symdic_Tm2483 = Sym('Tm2483')
    symdic_shen_datatypex45error = Sym('shen.datatype-error')
    symdic_shen_memo = Sym('shen.memo')
    symdic_kl_readx45filex45asx45bytelist = Sym('read-file-as-bytelist')
    symdic_shen_stack = Sym('shen.stack')
    symdic_V734 = Sym('V734')
    symdic_V778 = Sym('V778')
    symdic_kl_x62x61 = Sym('>=')
    symdic_kl_x62x62 = Sym('>>')
    symdic_V775 = Sym('V775')
    symdic_V776 = Sym('V776')
    symdic_V777 = Sym('V777')
    symdic_V882 = Sym('V882')
    symdic_shen_lzyx61 = Sym('shen.lzy=')
    symdic_shen_prologx45error = Sym('shen.prolog-error')
    symdic_shen_x60st_input2x62 = Sym('shen.<st_input2>')
    symdic_shen_yaccx45x62shen = Sym('shen.yacc->shen')
    symdic_shen_variantx63 = Sym('shen.variant?')
    symdic_shen_x60lcurlyx62 = Sym('shen.<lcurly>')
    symdic_shen_parameters = Sym('shen.parameters')
    symdic_V1998 = Sym('V1998')
    symdic_V1997 = Sym('V1997')
    symdic_B = Sym('B')
    symdic_Parse_shen_x60signaturex45helpx62 = Sym('Parse_shen.<signature-help>')
    symdic_kl_x42implementationx42 = Sym('*implementation*')
    symdic_shen_factorx45cn = Sym('shen.factor-cn')
    symdic_V688 = Sym('V688')
    symdic_V689 = Sym('V689')
    symdic_shen_tuplex45up = Sym('shen.tuple-up')
    symdic_V2809 = Sym('V2809')
    symdic_V682 = Sym('V682')
    symdic_V687 = Sym('V687')
    symdic_V3024 = Sym('V3024')
    symdic_V3025 = Sym('V3025')
    symdic_V3026 = Sym('V3026')
    symdic_Code = Sym('Code')
    symdic_V3020 = Sym('V3020')
    symdic_V3021 = Sym('V3021')
    symdic_V2519 = Sym('V2519')
    symdic_V2518 = Sym('V2518')
    symdic_V994 = Sym('V994')
    symdic_V995 = Sym('V995')
    symdic_V996 = Sym('V996')
    symdic_V997 = Sym('V997')
    symdic_V2513 = Sym('V2513')
    symdic_V991 = Sym('V991')
    symdic_V992 = Sym('V992')
    symdic_V993 = Sym('V993')
    symdic_shen_aritycheckx45action = Sym('shen.aritycheck-action')
    symdic_V2377 = Sym('V2377')
    symdic_shen_aum_to_shen = Sym('shen.aum_to_shen')
    symdic_V2376 = Sym('V2376')
    symdic_V2375 = Sym('V2375')
    symdic_shen_x60rcurlyx62 = Sym('shen.<rcurly>')
    symdic_V1772 = Sym('V1772')
    symdic_shen_percent = Sym('shen.percent')
    symdic_V1770 = Sym('V1770')
    symdic_V1771 = Sym('V1771')
    symdic_V1777 = Sym('V1777')
    symdic_V2373 = Sym('V2373')
    symdic_V1778 = Sym('V1778')
    symdic_V1779 = Sym('V1779')
    symdic_shen_typecheckx45andx45evaluate = Sym('shen.typecheck-and-evaluate')
    symdic_shen_stringx45x62bytes = Sym('shen.string->bytes')
    symdic_AfterCodePoint = Sym('AfterCodePoint')
    symdic_YaccParse = Sym('YaccParse')
    symdic_kl_x45 = Sym('-')
    symdic_V2469 = Sym('V2469')
    symdic_shen_initialisex45prolog = Sym('shen.initialise-prolog')
    symdic_shen_deref = Sym('shen.deref')
    symdic_V2462 = Sym('V2462')
    symdic_V2461 = Sym('V2461')
    symdic_V2460 = Sym('V2460')
    symdic_V2467 = Sym('V2467')
    symdic_V2466 = Sym('V2466')
    symdic_V2465 = Sym('V2465')
    symdic_V2464 = Sym('V2464')
    symdic_shen_occursx63 = Sym('shen.occurs?')
    symdic_V2242 = Sym('V2242')
    symdic_V2241 = Sym('V2241')
    symdic_V2240 = Sym('V2240')
    symdic_shen_x60timesx62 = Sym('shen.<times>')
    symdic_Qv = Sym('Qv')
    symdic_kl_lineread = Sym('lineread')
    symdic_V2647 = Sym('V2647')
    symdic_shen_prefixx63 = Sym('shen.prefix?')
    symdic_V2645 = Sym('V2645')
    symdic_V2644 = Sym('V2644')
    symdic_V2643 = Sym('V2643')
    symdic_V2642 = Sym('V2642')
    symdic_V2641 = Sym('V2641')
    symdic_V2640 = Sym('V2640')
    symdic_Bound = Sym('Bound')
    symdic_V2649 = Sym('V2649')
    symdic_V2648 = Sym('V2648')
    symdic_shen_reduce_help = Sym('shen.reduce_help')
    symdic_R = Sym('R')
    symdic_V2881 = Sym('V2881')
    symdic_V2880 = Sym('V2880')
    symdic_shen_source = Sym('shen.source')
    symdic_V2745 = Sym('V2745')
    symdic_V2889 = Sym('V2889')
    symdic_shen_functionx45abstractionx45help = Sym('shen.function-abstraction-help')
    symdic_V2395 = Sym('V2395')
    symdic_kl_x42propertyx45vectorx42 = Sym('*property-vector*')
    symdic_shen_split_cc_rule = Sym('shen.split_cc_rule')
    symdic_V2394 = Sym('V2394')
    symdic_ZeroStamp = Sym('ZeroStamp')
    symdic_kl_macroexpand = Sym('macroexpand')
    symdic_Parse_Y = Sym('Parse_Y')
    symdic_Parse_X = Sym('Parse_X')
    symdic_shen_continuation_call = Sym('shen.continuation_call')
    symdic_shen_udefsx42 = Sym('shen.udefs*')
    symdic_shen_rightx45x62left = Sym('shen.right->left')
    symdic_V1519 = Sym('V1519')
    symdic_V2393 = Sym('V2393')
    symdic_V1510 = Sym('V1510')
    symdic_V1511 = Sym('V1511')
    symdic_Free = Sym('Free')
    symdic_V1515 = Sym('V1515')
    symdic_kl_x42versionx42 = Sym('*version*')
    symdic_V1186 = Sym('V1186')
    symdic_V2089 = Sym('V2089')
    symdic_V2088 = Sym('V2088')
    symdic_V2743 = Sym('V2743')
    symdic_V2085 = Sym('V2085')
    symdic_kl_hdstr = Sym('hdstr')
    symdic_V2087 = Sym('V2087')
    symdic_V2086 = Sym('V2086')
    symdic_shen_tx42x45defcc = Sym('shen.t*-defcc')
    symdic_V2083 = Sym('V2083')
    symdic_kl_do = Sym('do')
    symdic_shen_fail_if = Sym('shen.fail_if')
    symdic_kl_emptyx63 = Sym('empty?')
    symdic_shen_tests = Sym('shen.tests')
    symdic_X = Sym('X')
    symdic_V2951 = Sym('V2951')
    symdic_V1206 = Sym('V1206')
    symdic_shen_nonx45empty = Sym('shen.non-empty')
    symdic_V1204 = Sym('V1204')
    symdic_V1205 = Sym('V1205')
    symdic_V1203 = Sym('V1203')
    symdic_shen_recordx45source = Sym('shen.record-source')
    symdic_shen_firstx45rule = Sym('shen.first-rule')
    symdic_Parse_shen_x60whitespacex62 = Sym('Parse_shen.<whitespace>')
    symdic_kl_fail = Sym('fail')
    symdic_shen_storex45arity = Sym('shen.store-arity')
    symdic_KL = Sym('KL')
    symdic_shen_insert = Sym('shen.insert')
    symdic_V1349 = Sym('V1349')
    symdic_V1910 = Sym('V1910')
    symdic_V1344 = Sym('V1344')
    symdic_shen_x60anymultix62 = Sym('shen.<anymulti>')
    symdic_shen_linearise = Sym('shen.linearise')
    symdic_V2650 = Sym('V2650')
    symdic_C = Sym('C')
    symdic_shen_flatten = Sym('shen.flatten')
    symdic_shen_outputx45macro = Sym('shen.output-macro')
    symdic_Counter = Sym('Counter')
    symdic_V2625 = Sym('V2625')
    symdic_Infs = Sym('Infs')
    symdic_shen_shen = Sym('shen.shen')
    symdic_kl_protect = Sym('protect')
    symdic_shen_reduce = Sym('shen.reduce')
    symdic_V2659 = Sym('V2659')
    symdic_shen_alphanumsx63 = Sym('shen.alphanums?')
    symdic_shen_mult_subst = Sym('shen.mult_subst')
    symdic_shen_errorx45macro = Sym('shen.error-macro')
    symdic_shen_tx42x45action = Sym('shen.t*-action')
    symdic_kl_makex45string = Sym('make-string')
    symdic_shen_lzyx61x61 = Sym('shen.lzy==')
    symdic_shen_x42historyx42 = Sym('shen.*history*')
    symdic_kl_loaded = Sym('loaded')
    symdic_shen_space = Sym('shen.space')
    symdic_kl_union = Sym('union')
    symdic_Parse_shen_x60exprx62 = Sym('Parse_shen.<expr>')
    symdic_V1835 = Sym('V1835')
    symdic_V1834 = Sym('V1834')
    symdic_V1837 = Sym('V1837')
    symdic_V1836 = Sym('V1836')
    symdic_V1831 = Sym('V1831')
    symdic_V1830 = Sym('V1830')
    symdic_shen_call_the_continuation = Sym('shen.call_the_continuation')
    symdic_V1832 = Sym('V1832')
    symdic_V766 = Sym('V766')
    symdic_V1839 = Sym('V1839')
    symdic_V1838 = Sym('V1838')
    symdic_V761 = Sym('V761')
    symdic_V760 = Sym('V760')
    symdic_V2710 = Sym('V2710')
    symdic_shen_x42occursx42 = Sym('shen.*occurs*')
    symdic_kl_exception = Sym('exception')
    symdic_shen_readx45charx45h = Sym('shen.read-char-h')
    symdic_shen_post = Sym('shen.post')
    symdic_shen_x60rulesx62 = Sym('shen.<rules>')
    symdic_V2620 = Sym('V2620')
    symdic_Other = Sym('Other')
    symdic_V2717 = Sym('V2717')
    symdic_Cs = Sym('Cs')
    symdic_shen_expt = Sym('shen.expt')
    symdic_kl_cons = Sym('cons')
    symdic_shen_toplineread_loop = Sym('shen.toplineread_loop')
    symdic_kl_is = Sym('is')
    symdic_ShenDef = Sym('ShenDef')
    symdic_Write = Sym('Write')
    symdic_V698 = Sym('V698')
    symdic_kl_cond = Sym('cond')
    symdic_kl_in = Sym('in')
    symdic_V693 = Sym('V693')
    symdic_V692 = Sym('V692')
    symdic_V2873 = Sym('V2873')
    symdic_V697 = Sym('V697')
    symdic_V696 = Sym('V696')
    symdic_V695 = Sym('V695')
    symdic_kl_if = Sym('if')
    symdic_V2508 = Sym('V2508')
    symdic_shen_list_streamx63 = Sym('shen.list_stream?')
    symdic_Abstraction = Sym('Abstraction')
    symdic_shen_pausex45forx45user = Sym('shen.pause-for-user')
    symdic_shen_extractx45pvars = Sym('shen.extract-pvars')
    symdic_format = Sym('format')
    symdic_V983 = Sym('V983')
    symdic_V2505 = Sym('V2505')
    symdic_V2506 = Sym('V2506')
    symdic_V2507 = Sym('V2507')
    symdic_V2535 = Sym('V2535')
    symdic_shen_maxseq = Sym('shen.maxseq')
    symdic_Parse_shen_x60strcontentsx62 = Sym('Parse_shen.<strcontents>')
    symdic_shen_x60returnx62 = Sym('shen.<return>')
    symdic_V1749 = Sym('V1749')
    symdic_V1748 = Sym('V1748')
    symdic_V1747 = Sym('V1747')
    symdic_shen_sx45prolog_clause = Sym('shen.s-prolog_clause')
    symdic_V1745 = Sym('V1745')
    symdic_shen_product = Sym('shen.product')
    symdic_V1743 = Sym('V1743')
    symdic_shen_insert_deref = Sym('shen.insert_deref')
    symdic_V1741 = Sym('V1741')
    symdic_V1740 = Sym('V1740')
    symdic_shen_x60digitsx62 = Sym('shen.<digits>')
    symdic_Y = Sym('Y')
    symdic_Parse_shen_x60singlelinex62 = Sym('Parse_shen.<singleline>')
    symdic_V867 = Sym('V867')
    symdic_V2470 = Sym('V2470')
    symdic_V2471 = Sym('V2471')
    symdic_V2472 = Sym('V2472')
    symdic_V2473 = Sym('V2473')
    symdic_V860 = Sym('V860')
    symdic_V2408 = Sym('V2408')
    symdic_Table = Sym('Table')
    symdic_shen_rulex45x62hornx45clause = Sym('shen.rule->horn-clause')
    symdic_V2254 = Sym('V2254')
    symdic_V2255 = Sym('V2255')
    symdic_V2256 = Sym('V2256')
    symdic_shen_be = Sym('shen.be')
    symdic_kl_defcc = Sym('defcc')
    symdic_shen_syntaxx45check = Sym('shen.syntax-check')
    symdic_V1699 = Sym('V1699')
    symdic_V1698 = Sym('V1698')
    symdic_V2652 = Sym('V2652')
    symdic_V2653 = Sym('V2653')
    symdic_V2654 = Sym('V2654')
    symdic_V2655 = Sym('V2655')
    symdic_V2656 = Sym('V2656')
    symdic_V2657 = Sym('V2657')
    symdic_V2658 = Sym('V2658')
    symdic_V1690 = Sym('V1690')
    symdic_shen_intprolog = Sym('shen.intprolog')
    symdic_V1695 = Sym('V1695')
    symdic_V1697 = Sym('V1697')
    symdic_V1696 = Sym('V1696')
    symdic_V2896 = Sym('V2896')
    symdic_V2897 = Sym('V2897')
    symdic_V2894 = Sym('V2894')
    symdic_V2895 = Sym('V2895')
    symdic_V2892 = Sym('V2892')
    symdic_V2893 = Sym('V2893')
    symdic_V2890 = Sym('V2890')
    symdic_V2891 = Sym('V2891')
    symdic_V2898 = Sym('V2898')
    symdic_V2899 = Sym('V2899')
    symdic_shen_tlvx45help = Sym('shen.tlv-help')
    symdic_D = Sym('D')
    symdic_V2757 = Sym('V2757')
    symdic_Parse_shen_x60patternsx62 = Sym('Parse_shen.<patterns>')
    symdic_V1523 = Sym('V1523')
    symdic_V1522 = Sym('V1522')
    symdic_shen_result = Sym('shen.result')
    symdic_Countx431 = Sym('Count+1')
    symdic_V1528 = Sym('V1528')
    symdic_V2850 = Sym('V2850')
    symdic_shen_errormaxinfs = Sym('shen.errormaxinfs')
    symdic_shen_findx45pastx45inputs = Sym('shen.find-past-inputs')
    symdic_shen_x60rulex62 = Sym('shen.<rule>')
    symdic_V2098 = Sym('V2098')
    symdic_V2099 = Sym('V2099')
    symdic_V2092 = Sym('V2092')
    symdic_V2093 = Sym('V2093')
    symdic_V2090 = Sym('V2090')
    symdic_kl_tuplex63 = Sym('tuple?')
    symdic_Parse_shen_x60postdigitsx62 = Sym('Parse_shen.<postdigits>')
    symdic_V1912 = Sym('V1912')
    symdic_shen_absx45macro = Sym('shen.abs-macro')
    symdic_shen_cf_help = Sym('shen.cf_help')
    symdic_kl_intern = Sym('intern')
    symdic_AUM_instruction = Sym('AUM_instruction')
    symdic_V1239 = Sym('V1239')
    symdic_shen_x42callx42 = Sym('shen.*call*')
    symdic_kl_x47 = Sym('/')
    symdic_kl_defprolog = Sym('defprolog')
    symdic_V2621 = Sym('V2621')
    symdic_shen_loop = Sym('shen.loop')
    symdic_V2623 = Sym('V2623')
    symdic_Parse_ = Sym('Parse_')
    symdic_V2622 = Sym('V2622')
    symdic_kl_absvector = Sym('absvector')
    symdic_shen_prbytes = Sym('shen.prbytes')
    symdic_V1354 = Sym('V1354')
    symdic_shen_x60termx42x62 = Sym('shen.<term*>')
    symdic_V2526 = Sym('V2526')
    symdic_V1359 = Sym('V1359')
    symdic_V2752 = Sym('V2752')
    symdic_V2525 = Sym('V2525')
    symdic_shen_default_semantics = Sym('shen.default_semantics')
    symdic_kl_unprofile = Sym('unprofile')
    symdic_shen_x60literalx42x62 = Sym('shen.<literal*>')
    symdic_V2091 = Sym('V2091')
    symdic_shen_typextable = Sym('shen.typextable')
    symdic_CCBody = Sym('CCBody')
    symdic_V2529 = Sym('V2529')
    symdic_Parse_shen_x60headx42x62 = Sym('Parse_shen.<head*>')
    symdic_shen_putx45profile = Sym('shen.put-profile')
    symdic_shen_readx45filex45asx45bytelistx45help = Sym('shen.read-file-as-bytelist-help')
    symdic_shen_funexstring = Sym('shen.funexstring')
    symdic_shen_abstract_rule = Sym('shen.abstract_rule')
    symdic_Parse_shen_x60strcx62 = Sym('Parse_shen.<strc>')
    symdic_shen_rulex45x62hornx45clausex45head = Sym('shen.rule->horn-clause-head')
    symdic_kl_head = Sym('head')
    symdic_kl_evalx45kl = Sym('eval-kl')
    symdic_Assume = Sym('Assume')
    symdic_shen_listx45x62str = Sym('shen.list->str')
    symdic_shen_insertx45trackingx45code = Sym('shen.insert-tracking-code')
    symdic_shen_pop = Sym('shen.pop')
    symdic_Z = Sym('Z')
    symdic_shen_x60actionx62 = Sym('shen.<action>')
    symdic_Parse_shen_x60backslashx62 = Sym('Parse_shen.<backslash>')
    symdic_Application = Sym('Application')
    symdic_shen_resizex45vector = Sym('shen.resize-vector')
    symdic_shen_modex45ify = Sym('shen.mode-ify')
    symdic_V1824 = Sym('V1824')
    symdic_V1826 = Sym('V1826')
    symdic_V1827 = Sym('V1827')
    symdic_shen_procedure_name = Sym('shen.procedure_name')
    symdic_V759 = Sym('V759')
    symdic_V1822 = Sym('V1822')
    symdic_V1823 = Sym('V1823')
    symdic_V1820 = Sym('V1820')
    symdic_V1821 = Sym('V1821')
    symdic_V752 = Sym('V752')
    symdic_ListofExceptions = Sym('ListofExceptions')
    symdic_shen_x42teststackx42 = Sym('shen.*teststack*')
    symdic_V751 = Sym('V751')
    symdic_V756 = Sym('V756')
    symdic_V757 = Sym('V757')
    symdic_V1828 = Sym('V1828')
    symdic_V1829 = Sym('V1829')
    symdic_Parse_shen_x60rsbx62 = Sym('Parse_shen.<rsb>')
    symdic_Sig = Sym('Sig')
    symdic_shen_constructx45context = Sym('shen.construct-context')
    symdic_kl_nl = Sym('nl')
    symdic_shen_x60anysinglex62 = Sym('shen.<anysingle>')
    symdic_kl_when = Sym('when')
    symdic_shen_semanticsx45check = Sym('shen.semantics-check')
    symdic_shen_x60endx42x62 = Sym('shen.<end*>')
    symdic_shen_ebr = Sym('shen.ebr')
    symdic_E = Sym('E')
    symdic_shen_x60lrbx62 = Sym('shen.<lrb>')
    symdic_shen_prologx45x62shen = Sym('shen.prolog->shen')
    symdic_Parse_shen_x60simple_patternx62 = Sym('Parse_shen.<simple_pattern>')
    symdic_kl_spy = Sym('spy')
    symdic_shen_lengthx45h = Sym('shen.length-h')
    symdic_V3043 = Sym('V3043')
    symdic_V3040 = Sym('V3040')
    symdic_V3041 = Sym('V3041')
    symdic_kl_x60x45address = Sym('<-address')
    symdic_Reduce = Sym('Reduce')
    symdic_V2790 = Sym('V2790')
    symdic_kl_fst = Sym('fst')
    symdic_kl_time = Sym('time')
    symdic_TypeTable = Sym('TypeTable')
    symdic_kl_x58x45 = Sym(':-')
    symdic_kl_mapcan = Sym('mapcan')
    symdic_V1750 = Sym('V1750')
    symdic_V1751 = Sym('V1751')
    symdic_V1752 = Sym('V1752')
    symdic_shen_variancyx45test = Sym('shen.variancy-test')
    symdic_V1757 = Sym('V1757')
    symdic_V2791 = Sym('V2791')
    symdic_kl_x42macrosx42 = Sym('*macros*')
    symdic_V2793 = Sym('V2793')
    symdic_V2792 = Sym('V2792')
    symdic_shen_explicit_modes = Sym('shen.explicit_modes')
    symdic_Len = Sym('Len')
    symdic_V2797 = Sym('V2797')
    symdic_V2796 = Sym('V2796')
    symdic_V2799 = Sym('V2799')
    symdic_V2798 = Sym('V2798')
    symdic_V2407 = Sym('V2407')
    symdic_shen_tx42x45hyps = Sym('shen.t*-hyps')
    symdic_V2409 = Sym('V2409')
    symdic_shen_x60defprologx62 = Sym('shen.<defprolog>')
    symdic_Standard = Sym('Standard')
    symdic_Parse_x60x33x62 = Sym('Parse_<!>')
    symdic_shen_lzyx61x33 = Sym('shen.lzy=!')
    symdic_shen_yacc = Sym('shen.yacc')
    symdic_V2439 = Sym('V2439')
    symdic_shen_prettyx45type = Sym('shen.pretty-type')
    symdic_V2229 = Sym('V2229')
    symdic_kl_string = Sym('string')
    symdic_shen_removetype = Sym('shen.removetype')
    symdic_shen_procx45inputx43 = Sym('shen.proc-input+')
    symdic_V2220 = Sym('V2220')
    symdic_V2223 = Sym('V2223')
    symdic_V2222 = Sym('V2222')
    symdic_V2225 = Sym('V2225')
    symdic_V2224 = Sym('V2224')
    symdic_shen_x45nullx45 = Sym('shen.-null-')
    symdic_shen_doubleunderlinex63 = Sym('shen.doubleunderline?')
    symdic_Declare = Sym('Declare')
    symdic_shen_uppercasex63 = Sym('shen.uppercase?')
    symdic_Clause = Sym('Clause')
    symdic_V1680 = Sym('V1680')
    symdic_kl_gensym = Sym('gensym')
    symdic_V1685 = Sym('V1685')
    symdic_Tag = Sym('Tag')
    symdic_V2318 = Sym('V2318')
    symdic_shen_renamex45semantics = Sym('shen.rename-semantics')
    symdic_V2317 = Sym('V2317')
    symdic_V2310 = Sym('V2310')
    symdic_V2135 = Sym('V2135')
    symdic_V2134 = Sym('V2134')
    symdic_V2137 = Sym('V2137')
    symdic_V2136 = Sym('V2136')
    symdic_V2131 = Sym('V2131')
    symdic_V2130 = Sym('V2130')
    symdic_V2133 = Sym('V2133')
    symdic_V2132 = Sym('V2132')
    symdic_V2139 = Sym('V2139')
    symdic_V2138 = Sym('V2138')
    symdic_V2646 = Sym('V2646')
    symdic_AtomType = Sym('AtomType')
    symdic_V1538 = Sym('V1538')
    symdic_kl_run = Sym('run')
    symdic_V2597 = Sym('V2597')
    symdic_kl_vectorx63 = Sym('vector?')
    symdic_shen_x60barx62 = Sym('shen.<bar>')
    symdic_shen_nextline = Sym('shen.nextline')
    symdic_shen_synonymsx45help = Sym('shen.synonyms-help')
    symdic_shen_shx63 = Sym('shen.sh?')
    symdic_V2591 = Sym('V2591')
    symdic_kl_trapx45error = Sym('trap-error')
    symdic_shen_x60strx62 = Sym('shen.<str>')
    symdic_shen_cl = Sym('shen.cl')
    symdic_V2454 = Sym('V2454')
    symdic_V2455 = Sym('V2455')
    symdic_shen_clause_form = Sym('shen.clause_form')
    symdic_shen_bytex45x62digit = Sym('shen.byte->digit')
    symdic_V2452 = Sym('V2452')
    symdic_V1220 = Sym('V1220')
    symdic_V1221 = Sym('V1221')
    symdic_V1222 = Sym('V1222')
    symdic_Freeze = Sym('Freeze')
    symdic_Parse_shen_x60premisesx62 = Sym('Parse_shen.<premises>')
    symdic_Jnk = Sym('Jnk')
    symdic_shen_spaces = Sym('shen.spaces')
    symdic_shen_rcons_form = Sym('shen.rcons_form')
    symdic_shen_prhush = Sym('shen.prhush')
    symdic_V1323 = Sym('V1323')
    symdic_V1324 = Sym('V1324')
    symdic_V1329 = Sym('V1329')
    symdic_Parse_shen_x60formulaex62 = Sym('Parse_shen.<formulae>')
    symdic_shen_x60strcontentsx62 = Sym('shen.<strcontents>')
    symdic_kl_x42portx42 = Sym('*port*')
    symdic_shen_make_mu_application = Sym('shen.make_mu_application')
    symdic_CondExpression = Sym('CondExpression')
    symdic_Lineread = Sym('Lineread')
    symdic_V2549 = Sym('V2549')
    symdic_Parse_shen_x60bodyx42x62 = Sym('Parse_shen.<body*>')
    symdic_F = Sym('F')
    symdic_Default = Sym('Default')
    symdic_shen_x60singleunderlinex62 = Sym('shen.<singleunderline>')
    symdic_shen_callx45help = Sym('shen.call-help')
    symdic_Time = Sym('Time')
    symdic_kl_cases = Sym('cases')
    symdic_V1035 = Sym('V1035')
    symdic_V1034 = Sym('V1034')
    symdic_V1036 = Sym('V1036')
    symdic_V1033 = Sym('V1033')
    symdic_shen_atomx45type = Sym('shen.atom-type')
    symdic_shen_x60semicolonx45symbolx62 = Sym('shen.<semicolon-symbol>')
    symdic_Parse_shen_x60lsbx62 = Sym('Parse_shen.<lsb>')
    symdic_kl_stream = Sym('stream')
    symdic_kl_abort = Sym('abort')
    symdic_kl_inputx43 = Sym('input+')
    symdic_Terms = Sym('Terms')
    symdic_shen_trackedx63 = Sym('shen.tracked?')
    symdic_kl_get = Sym('get')
    symdic_shen_lispx45or = Sym('shen.lisp-or')
    symdic_shen_removex45synonyms = Sym('shen.remove-synonyms')
    symdic_H = Sym('H')
    symdic_Datatypes = Sym('Datatypes')
    symdic_shen_aum = Sym('shen.aum')
    symdic_V1813 = Sym('V1813')
    symdic_V1812 = Sym('V1812')
    symdic_kl_snd = Sym('snd')
    symdic_V1810 = Sym('V1810')
    symdic_V1817 = Sym('V1817')
    symdic_V1816 = Sym('V1816')
    symdic_V1814 = Sym('V1814')
    symdic_V2817 = Sym('V2817')
    symdic_V1819 = Sym('V1819')
    symdic_V1818 = Sym('V1818')
    symdic_V2948 = Sym('V2948')
    symdic_shen_sysfuncx63 = Sym('shen.sysfunc?')
    symdic_Parsed = Sym('Parsed')
    symdic_ContextOut_1957 = Sym('ContextOut_1957')
    symdic_shen_copyx45vector = Sym('shen.copy-vector')
    symdic_V2904 = Sym('V2904')
    symdic_shen_compile_to_lambdax43 = Sym('shen.compile_to_lambda+')
    symdic_Direction = Sym('Direction')
    symdic_V2772 = Sym('V2772')
    symdic_Rules = Sym('Rules')
    symdic_V745 = Sym('V745')
    symdic_V744 = Sym('V744')
    symdic_Parse_shen_x60atomx62 = Sym('Parse_shen.<atom>')
    symdic_V743 = Sym('V743')
    symdic_shen_decimalise = Sym('shen.decimalise')
    symdic_NewHistory = Sym('NewHistory')
    symdic_V2667 = Sym('V2667')
    symdic_V2906 = Sym('V2906')
    symdic_shen_skip = Sym('shen.skip')
    symdic_shen_tcx45rule = Sym('shen.tc-rule')
    symdic_ProcessN = Sym('ProcessN')
    symdic_V2782 = Sym('V2782')
    symdic_V2783 = Sym('V2783')
    symdic_V2780 = Sym('V2780')
    symdic_V2781 = Sym('V2781')
    symdic_V2786 = Sym('V2786')
    symdic_V2787 = Sym('V2787')
    symdic_V2784 = Sym('V2784')
    symdic_V2785 = Sym('V2785')
    symdic_kl_not = Sym('not')
    symdic_V2788 = Sym('V2788')
    symdic_V2789 = Sym('V2789')
    symdic_V2412 = Sym('V2412')
    symdic_V2413 = Sym('V2413')
    symdic_shen_getx45type = Sym('shen.get-type')
    symdic_V2671 = Sym('V2671')
    symdic_V2416 = Sym('V2416')
    symdic_shen_x42infsx42 = Sym('shen.*infs*')
    symdic_V2414 = Sym('V2414')
    symdic_V2415 = Sym('V2415')
    symdic_shen_failx33 = Sym('shen.fail!')
    symdic_Parse_shen_x60typex62 = Sym('Parse_shen.<type>')
    symdic_shen_demodx45atom = Sym('shen.demod-atom')
    symdic_Abstractions = Sym('Abstractions')
    symdic_V2232 = Sym('V2232')
    symdic_V2233 = Sym('V2233')
    symdic_V2230 = Sym('V2230')
    symdic_V2231 = Sym('V2231')
    symdic_V2234 = Sym('V2234')
    symdic_PremissLiterals = Sym('PremissLiterals')
    symdic_shen_x60rsbx62 = Sym('shen.<rsb>')
    symdic_kl_vectorx45x62 = Sym('vector->')
    symdic_V886 = Sym('V886')
    symdic_shen_application_build = Sym('shen.application_build')
    symdic_V2453 = Sym('V2453')
    symdic_V887 = Sym('V887')
    symdic_shen_x60st_inputx62 = Sym('shen.<st_input>')
    symdic_Parse_shen_x60commax45symbolx62 = Sym('Parse_shen.<comma-symbol>')
    symdic_V2308 = Sym('V2308')
    symdic_V2309 = Sym('V2309')
    symdic_V2306 = Sym('V2306')
    symdic_V2307 = Sym('V2307')
    symdic_V2304 = Sym('V2304')
    symdic_V2305 = Sym('V2305')
    symdic_shen_x42gensymx42 = Sym('shen.*gensym*')
    symdic_V2126 = Sym('V2126')
    symdic_V2127 = Sym('V2127')
    symdic_V2122 = Sym('V2122')
    symdic_V2123 = Sym('V2123')
    symdic_G = Sym('G')
    symdic_kl_boundx63 = Sym('bound?')
    symdic_V2128 = Sym('V2128')
    symdic_V2129 = Sym('V2129')
    symdic_Record = Sym('Record')
    symdic_V2493 = Sym('V2493')
    symdic_shen_newline = Sym('shen.newline')
    symdic_V1783 = Sym('V1783')
    symdic_V1782 = Sym('V1782')
    symdic_V1781 = Sym('V1781')
    symdic_V1780 = Sym('V1780')
    symdic_V1787 = Sym('V1787')
    symdic_V1786 = Sym('V1786')
    symdic_V1785 = Sym('V1785')
    symdic_V1784 = Sym('V1784')
    symdic_shen_x60clausex42x62 = Sym('shen.<clause*>')
    symdic_Macroexpand = Sym('Macroexpand')
    symdic_V2628 = Sym('V2628')
    symdic_kl_lambda = Sym('lambda')
    symdic_shen_else = Sym('shen.else')
    symdic_shen_readx45evaluatex45print = Sym('shen.read-evaluate-print')
    symdic_kl_readx45file = Sym('read-file')
    symdic_Start = Sym('Start')
    symdic_V1125 = Sym('V1125')
    symdic_shen_syntax = Sym('shen.syntax')
    symdic_shen_callx45rest = Sym('shen.call-rest')
    symdic_kl_open = Sym('open')
    symdic_X2369 = Sym('X2369')
    symdic_Arity = Sym('Arity')
    symdic_kl_thaw = Sym('thaw')
    symdic_kl_variablex63 = Sym('variable?')
    symdic_kl_arity = Sym('arity')
    symdic_V3029 = Sym('V3029')
    symdic_V1334 = Sym('V1334')
    symdic_READx45CHAR = Sym('READ-CHAR')
    symdic_kl_lazy = Sym('lazy')
    symdic_V1339 = Sym('V1339')
    symdic_History = Sym('History')
    symdic_optimise = Sym('optimise')
    symdic_shen_shenx45syntaxx45error = Sym('shen.shen-syntax-error')
    symdic_shen_recursive_cons_form = Sym('shen.recursive_cons_form')
    symdic_kl_and = Sym('and')
    symdic_kl_cn = Sym('cn')
    symdic_Parse_shen_x60equalx62 = Sym('Parse_shen.<equal>')
    symdic_V3037 = Sym('V3037')
    symdic_Parse_shen_x60digitsx62 = Sym('Parse_shen.<digits>')
    symdic_shen_chwild = Sym('shen.chwild')
    symdic_shen_retrievex45fromx45historyx45ifx45needed = Sym('shen.retrieve-from-history-if-needed')
    symdic_Parse_shen_x60returnx62 = Sym('Parse_shen.<return>')
    symdic_shen_x43vectorx63 = Sym('shen.+vector?')
    symdic_V1020 = Sym('V1020')
    symdic_V2463 = Sym('V2463')
    symdic_shen_copyfromvector = Sym('shen.copyfromvector')
    symdic_shen_evalx45cons = Sym('shen.eval-cons')
    symdic_kl_destroy = Sym('destroy')
    symdic_Ds = Sym('Ds')
    symdic_shen_outputx45track = Sym('shen.output-track')
    symdic_V2545 = Sym('V2545')
    symdic_kl_track = Sym('track')
    symdic_V2547 = Sym('V2547')
    symdic_V2084 = Sym('V2084')
    symdic_shen_hdtl = Sym('shen.hdtl')
    symdic_V2543 = Sym('V2543')
    symdic_kl_x42maximumx45printx45sequencex45sizex42 = Sym('*maximum-print-sequence-size*')
    symdic_Strip = Sym('Strip')
    symdic_shen_encodex45choices = Sym('shen.encode-choices')
    symdic_V1808 = Sym('V1808')
    symdic_V1809 = Sym('V1809')
    symdic_Parse_shen_x60termx42x62 = Sym('Parse_shen.<term*>')
    symdic_V1804 = Sym('V1804')
    symdic_V1805 = Sym('V1805')
    symdic_V1806 = Sym('V1806')
    symdic_V1807 = Sym('V1807')
    symdic_V1800 = Sym('V1800')
    symdic_V1801 = Sym('V1801')
    symdic_V1802 = Sym('V1802')
    symdic_V1803 = Sym('V1803')
    symdic_kl_x42portersx42 = Sym('*porters*')
    symdic_Test = Sym('Test')
    symdic_shen_catchkill = Sym('shen.catchkill')
    symdic_Parse_shen_x60rcurlyx62 = Sym('Parse_shen.<rcurly>')
    symdic_shen_typedfx63 = Sym('shen.typedf?')
    symdic_Parse_shen_x60rulesx62 = Sym('Parse_shen.<rules>')
    symdic_V3019 = Sym('V3019')
    symdic_Byte = Sym('Byte')
    symdic_V3018 = Sym('V3018')
    symdic_Parse_shen_x60colonx62 = Sym('Parse_shen.<colon>')
    symdic_kl_includex45allx45but = Sym('include-all-but')
    symdic_V644 = Sym('V644')
    symdic_V645 = Sym('V645')
    symdic_V646 = Sym('V646')
    symdic_MacroAdd = Sym('MacroAdd')
    symdic_Parse_shen_x60numx62 = Sym('Parse_shen.<num>')
    symdic_V2488 = Sym('V2488')
    symdic_V3014 = Sym('V3014')
    symdic_shen_packagex45contents = Sym('shen.package-contents')
    symdic_Parse_shen_x60semicolonx62 = Sym('Parse_shen.<semicolon>')
    symdic_shen_x60dbqx62 = Sym('shen.<dbq>')
    symdic_shen_check_stream = Sym('shen.check_stream')
    symdic_V730 = Sym('V730')
    symdic_V731 = Sym('V731')
    symdic_V884 = Sym('V884')
    symdic_V733 = Sym('V733')
    symdic_shen_precludex45h = Sym('shen.preclude-h')
    symdic_V883 = Sym('V883')
    symdic_V880 = Sym('V880')
    symdic_V881 = Sym('V881')
    symdic_V3012 = Sym('V3012')
    symdic_kl_where = Sym('where')
    symdic_Tms = Sym('Tms')
    symdic_shen_intprologx45help = Sym('shen.intprolog-help')
    symdic_V2937 = Sym('V2937')
    symdic_V2936 = Sym('V2936')
    symdic_V2931 = Sym('V2931')
    symdic_V2930 = Sym('V2930')
    symdic_shen_valvector = Sym('shen.valvector')
    symdic_shen_x60whitespacex62 = Sym('shen.<whitespace>')
    symdic_shen_x42alphabetx42 = Sym('shen.*alphabet*')
    symdic_Finish = Sym('Finish')
    symdic_shen_x64vx45help = Sym('shen.@v-help')
    symdic_V2689 = Sym('V2689')
    symdic_V2683 = Sym('V2683')
    symdic_V2682 = Sym('V2682')
    symdic_V2681 = Sym('V2681')
    symdic_V2680 = Sym('V2680')
    symdic_S = Sym('S')
    symdic_V2684 = Sym('V2684')
    symdic_shen_constructx45sidex45literals = Sym('shen.construct-side-literals')
    symdic_V2330 = Sym('V2330')
    symdic_V2113 = Sym('V2113')
    symdic_V2112 = Sym('V2112')
    symdic_AllExceptions = Sym('AllExceptions')
    symdic_V2110 = Sym('V2110')
    symdic_shen_trimx45gubbins = Sym('shen.trim-gubbins')
    symdic_NewAction = Sym('NewAction')
    symdic_V2552 = Sym('V2552')
    symdic_shen_x60signaturex45helpx62 = Sym('shen.<signature-help>')
    symdic_kl_pos = Sym('pos')
    symdic_Parse_Case = Sym('Parse_Case')
    symdic_shen_x42trackingx42 = Sym('shen.*tracking*')
    symdic_V1825 = Sym('V1825')
    symdic_V1798 = Sym('V1798')
    symdic_V1799 = Sym('V1799')
    symdic_V1794 = Sym('V1794')
    symdic_Parse_shen_x60clausex42x62 = Sym('Parse_shen.<clause*>')
    symdic_V2207 = Sym('V2207')
    symdic_V2754 = Sym('V2754')
    symdic_Parse_shen_x60alphax62 = Sym('Parse_shen.<alpha>')
    symdic_V2756 = Sym('V2756')
    symdic_V2751 = Sym('V2751')
    symdic_V2202 = Sym('V2202')
    symdic_V2753 = Sym('V2753')
    symdic_Assumptions_1957 = Sym('Assumptions_1957')
    symdic_V2759 = Sym('V2759')
    symdic_V2758 = Sym('V2758')
    symdic_V2209 = Sym('V2209')
    symdic_V2208 = Sym('V2208')
    symdic_kl_occursx45check = Sym('occurs-check')
    symdic_V754 = Sym('V754')
    symdic_shen_strx45x62str = Sym('shen.str->str')
    symdic_Action = Sym('Action')
    symdic_V2724 = Sym('V2724')
    symdic_V755 = Sym('V755')
    symdic_V2725 = Sym('V2725')
    symdic_shen_constructx45searchx45clause = Sym('shen.construct-search-clause')
    symdic_kl_hdv = Sym('hdv')
    symdic_V1248 = Sym('V1248')
    symdic_shen_sx45prolog_literal = Sym('shen.s-prolog_literal')
    symdic_NewContinuation = Sym('NewContinuation')
    symdic_shen_procx45nl = Sym('shen.proc-nl')
    symdic_V1240 = Sym('V1240')
    symdic_V1241 = Sym('V1241')
    symdic_V1246 = Sym('V1246')
    symdic_V1247 = Sym('V1247')
    symdic_shen_x60pattern1x62 = Sym('shen.<pattern1>')
    symdic_V1245 = Sym('V1245')
    symdic_kl_compile = Sym('compile')
    symdic_Other2440 = Sym('Other2440')
    symdic_SynHyps = Sym('SynHyps')
    symdic_shen_variablex45match = Sym('shen.variable-match')
    symdic_shen_decons = Sym('shen.decons')
    symdic_shen_x60sigx43restx62 = Sym('shen.<sig+rest>')
    symdic_shen_toplineread = Sym('shen.toplineread')
    symdic_shen_ephemeral_variablex63 = Sym('shen.ephemeral_variable?')
    symdic_V1309 = Sym('V1309')
    symdic_V1307 = Sym('V1307')
    symdic_kl_return = Sym('return')
    symdic_V1305 = Sym('V1305')
    symdic_V1304 = Sym('V1304')
    symdic_V1303 = Sym('V1303')
    symdic_Profile = Sym('Profile')
    symdic_kl_verified = Sym('verified')
    symdic_shen_x60datatypex45rulex62 = Sym('shen.<datatype-rule>')
    symdic_shen_tuple = Sym('shen.tuple')
    symdic_shen_prompt = Sym('shen.prompt')
    symdic_shen_showx45p = Sym('shen.show-p')
    symdic_I = Sym('I')
    symdic_shen_makex45stringx45macro = Sym('shen.make-string-macro')
    symdic_shen_x60equalx62 = Sym('shen.<equal>')
    symdic_shen_prologx45aritycheck = Sym('shen.prolog-aritycheck')
    symdic_V1019 = Sym('V1019')
    symdic_V1018 = Sym('V1018')
    symdic_shen_mkstrx45l = Sym('shen.mkstr-l')
    symdic_shen_of = Sym('shen.of')
    symdic_shen_ok = Sym('shen.ok')
    symdic_Parse_shen_x60singleunderlinex62 = Sym('Parse_shen.<singleunderline>')
    symdic_shen_sndx45orx45fail = Sym('shen.snd-or-fail')
    symdic_V2111 = Sym('V2111')
    symdic_kill = Sym('kill')
    symdic_shen_compile_to_kl = Sym('shen.compile_to_kl')
    symdic_shen_x42processx45counterx42 = Sym('shen.*process-counter*')
    symdic_shen_x60predigitsx62 = Sym('shen.<predigits>')
    symdic_Linear = Sym('Linear')
    symdic_Parse_shen_x60literalx42x62 = Sym('Parse_shen.<literal*>')
    symdic_Applications = Sym('Applications')
    symdic_Change = Sym('Change')
    symdic_shen_digitsx45x62integers = Sym('shen.digits->integers')
    symdic_kl_read = Sym('read')
    symdic_V1870 = Sym('V1870')
    symdic_kl_maxinferences = Sym('maxinferences')
    symdic_V1877 = Sym('V1877')
    symdic_V1876 = Sym('V1876')
    symdic_IncrementProcessCounter = Sym('IncrementProcessCounter')
    symdic_shen_timerx45macro = Sym('shen.timer-macro')
    symdic_shen_x60log10x62 = Sym('shen.<log10>')
    symdic_V2055 = Sym('V2055')
    symdic_Parse_shen_x60patternx62 = Sym('Parse_shen.<pattern>')
    symdic_External = Sym('External')
    symdic_shen_x42tcx42 = Sym('shen.*tc*')
    symdic_shen_deconsx45string = Sym('shen.decons-string')
    symdic_kl_output = Sym('output')
    symdic_shen_x60strcx62 = Sym('shen.<strc>')
    symdic_Context1_1957 = Sym('Context1_1957')
    symdic_shen_x42optimisex42 = Sym('shen.*optimise*')
    symdic_V1901 = Sym('V1901')
    symdic_V1900 = Sym('V1900')
    symdic_V656 = Sym('V656')
    symdic_V1909 = Sym('V1909')
    symdic_V1908 = Sym('V1908')
    symdic_V651 = Sym('V651')
    symdic_shen_x60signaturex62 = Sym('shen.<signature>')
    symdic_shen_insertx45h = Sym('shen.insert-h')
    symdic_CompileProfile = Sym('CompileProfile')
    symdic_shen_insertx45l = Sym('shen.insert-l')
    symdic_V891 = Sym('V891')
    symdic_V890 = Sym('V890')
    symdic_V893 = Sym('V893')
    symdic_V720 = Sym('V720')
    symdic_V895 = Sym('V895')
    symdic_V894 = Sym('V894')
    symdic_V897 = Sym('V897')
    symdic_V896 = Sym('V896')
    symdic_V899 = Sym('V899')
    symdic_V898 = Sym('V898')
    symdic_V729 = Sym('V729')
    symdic_shen_findallhelp = Sym('shen.findallhelp')
    symdic_shen_condx45expression = Sym('shen.cond-expression')
    symdic_Parse_shen_x60symx62 = Sym('Parse_shen.<sym>')
    symdic_Parse_shen_x60semicolonx45symbolx62 = Sym('Parse_shen.<semicolon-symbol>')
    symdic_shen_typecheckx45andx45load = Sym('shen.typecheck-and-load')
    symdic_kl__ = Sym('_')
    symdic_V2438 = Sym('V2438')
    symdic_shen_cslx45help = Sym('shen.csl-help')
    symdic_kl_package = Sym('package')
    symdic_shen_double = Sym('shen.double')
    symdic_V2925 = Sym('V2925')
    symdic_V2922 = Sym('V2922')
    symdic_V2923 = Sym('V2923')
    symdic_V2920 = Sym('V2920')
    symdic_V2921 = Sym('V2921')
    symdic_shen_x60datatypex45rulesx62 = Sym('shen.<datatype-rules>')
    symdic_Message = Sym('Message')
    symdic_shen_trackx45function = Sym('shen.track-function')
    symdic_kl_or = Sym('or')
    symdic_shen_x60multilinex62 = Sym('shen.<multiline>')
    symdic_shen_walk = Sym('shen.walk')
    symdic_V2964 = Sym('V2964')
    symdic_V1495 = Sym('V1495')
    symdic_V1490 = Sym('V1490')
    symdic_V2694 = Sym('V2694')
    symdic_V2695 = Sym('V2695')
    symdic_V2696 = Sym('V2696')
    symdic_V2697 = Sym('V2697')
    symdic_V2690 = Sym('V2690')
    symdic_V1658 = Sym('V1658')
    symdic_V2692 = Sym('V2692')
    symdic_V2693 = Sym('V2693')
    symdic_Ns = Sym('Ns')
    symdic_V2698 = Sym('V2698')
    symdic_V2699 = Sym('V2699')
    symdic_V1653 = Sym('V1653')
    symdic_V2755 = Sym('V2755')
    symdic_V2329 = Sym('V2329')
    symdic_Parse_shen_x60minusx62 = Sym('Parse_shen.<minus>')
    symdic_shen_sum = Sym('shen.sum')
    symdic_shen_tab = Sym('shen.tab')
    symdic_V2750 = Sym('V2750')
    symdic_V3042 = Sym('V3042')
    symdic_V2108 = Sym('V2108')
    symdic_V2109 = Sym('V2109')
    symdic_V2104 = Sym('V2104')
    symdic_V2105 = Sym('V2105')
    symdic_V2106 = Sym('V2106')
    symdic_J = Sym('J')
    symdic_V2100 = Sym('V2100')
    symdic_V2101 = Sym('V2101')
    symdic_V2102 = Sym('V2102')
    symdic_V2103 = Sym('V2103')
    symdic_Error = Sym('Error')
    symdic_shen_catchx45cut = Sym('shen.catch-cut')
    symdic_shen_x60exprx62 = Sym('shen.<expr>')
    symdic_shen_cc_help = Sym('shen.cc_help')
    symdic_V2210 = Sym('V2210')
    symdic_V2211 = Sym('V2211')
    symdic_V2212 = Sym('V2212')
    symdic_shen_modh = Sym('shen.modh')
    symdic_V2214 = Sym('V2214')
    symdic_V2215 = Sym('V2215')
    symdic_V2216 = Sym('V2216')
    symdic_V2741 = Sym('V2741')
    symdic_shen_stripx45protect = Sym('shen.strip-protect')
    symdic_Close = Sym('Close')
    symdic_kl_define = Sym('define')
    symdic_V2748 = Sym('V2748')
    symdic_V2749 = Sym('V2749')
    symdic_shen_tx42x45rule = Sym('shen.t*-rule')
    symdic_shen_x60pattern2x62 = Sym('shen.<pattern2>')
    symdic_kl_file = Sym('file')
    symdic_shen_afterx45codepoint = Sym('shen.after-codepoint')
    symdic_shen_x60variablex63x62 = Sym('shen.<variable?>')
    symdic_shen_linearisex45clause = Sym('shen.linearise-clause')
    symdic_V1279 = Sym('V1279')
    symdic_V1278 = Sym('V1278')
    symdic_V1475 = Sym('V1475')
    symdic_V1470 = Sym('V1470')
    symdic_Direction2685 = Sym('Direction2685')
    symdic_shen_inputx45track = Sym('shen.input-track')
    symdic_shen_stripx45pathname = Sym('shen.strip-pathname')
    symdic_SearchLiterals = Sym('SearchLiterals')
    symdic_kl_stringx63 = Sym('string?')
    symdic_Parse_shen_x60formulax62 = Sym('Parse_shen.<formula>')
    symdic_shen_toplevel = Sym('shen.toplevel')
    symdic_kl_absvectorx63 = Sym('absvector?')
    symdic_x60x33x62 = Sym('<!>')
    symdic_shen_continuation = Sym('shen.continuation')
    symdic_kl_symbol = Sym('symbol')
    symdic_NewVector = Sym('NewVector')
    symdic_V1318 = Sym('V1318')
    symdic_V1310 = Sym('V1310')
    symdic_V1311 = Sym('V1311')
    symdic_kl_concat = Sym('concat')
    symdic_shen_x60formulax62 = Sym('shen.<formula>')
    symdic_shen_readx45char = Sym('shen.read-char')
    symdic_V2213 = Sym('V2213')
    symdic_NewPremises = Sym('NewPremises')
    symdic_kl_external = Sym('external')
    symdic_V1106 = Sym('V1106')
    symdic_Val = Sym('Val')
    symdic_shen_tx42x45rules = Sym('shen.t*-rules')
    symdic_V1000 = Sym('V1000')
    symdic_V1001 = Sym('V1001')
    symdic_shen_linearise_X = Sym('shen.linearise_X')
    symdic_Var = Sym('Var')
    symdic_shen_x60premisesx62 = Sym('shen.<premises>')
    symdic_kl_tl = Sym('tl')
    symdic_shen_semantics = Sym('shen.semantics')
    symdic_shen_hat = Sym('shen.hat')
    symdic_shen_x60alphanumx62 = Sym('shen.<alphanum>')
    symdic_kl_tc = Sym('tc')
    symdic_shen_printx45pastx45inputs = Sym('shen.print-past-inputs')
    symdic_x42stoutputx42 = Sym('*stoutput*')
    symdic_V2491 = Sym('V2491')
    symdic_Bytes = Sym('Bytes')
    symdic_shen_rulex45x62hornx45clausex45body = Sym('shen.rule->horn-clause-body')
    symdic_A2402 = Sym('A2402')
    symdic_V2494 = Sym('V2494')
    symdic_kl_difference = Sym('difference')
    symdic_kl_readx45filex45asx45string = Sym('read-file-as-string')
    symdic_shen_x60plusx62 = Sym('shen.<plus>')
    symdic_shen_fixx45help = Sym('shen.fix-help')
    symdic_shen_measurex38return = Sym('shen.measure&return')
    symdic_kl_x58x61 = Sym(':=')
    symdic_kl_list = Sym('list')
    symdic_Rest = Sym('Rest')
    symdic_FileName = Sym('FileName')
    symdic_V1242 = Sym('V1242')
    symdic_MuApplication = Sym('MuApplication')
    symdic_V2795 = Sym('V2795')
    symdic_kl_x45x62 = Sym('->')
    symdic_V2794 = Sym('V2794')
    symdic_V1869 = Sym('V1869')
    symdic_shen_loadx45help = Sym('shen.load-help')
    symdic_RemoveSynonyms = Sym('RemoveSynonyms')
    symdic_shen_constructx45premissx45literal = Sym('shen.construct-premiss-literal')
    symdic_kl_prologx63 = Sym('prolog?')
    symdic_V1244 = Sym('V1244')
    symdic_kl_x42stinputx42 = Sym('*stinput*')
    symdic_shen_x60backslashx62 = Sym('shen.<backslash>')
    symdic_shen_find = Sym('shen.find')
    symdic_kl_x64s = Sym('@s')
    symdic_kl_x64p = Sym('@p')
    symdic_kl_version = Sym('version')
    symdic_kl_x64v = Sym('@v')
    symdic_shen_legitimatex45termx63 = Sym('shen.legitimate-term?')
    symdic_shen_em_help = Sym('shen.em_help')
    symdic_kl_undefmacro = Sym('undefmacro')
    symdic_V1914 = Sym('V1914')
    symdic_V1915 = Sym('V1915')
    symdic_kl_hash = Sym('hash')
    symdic_V1913 = Sym('V1913')
    symdic_shen_sx45prolog = Sym('shen.s-prolog')
    symdic_shen_x42datatypesx42 = Sym('shen.*datatypes*')
    symdic_V662 = Sym('V662')
    symdic_K = Sym('K')
    symdic_V661 = Sym('V661')
    symdic_V667 = Sym('V667')
    symdic_V1918 = Sym('V1918')
    symdic_V1919 = Sym('V1919')
    symdic_kl_x60x45vector = Sym('<-vector')
    symdic_shen_toplevel_evaluate = Sym('shen.toplevel_evaluate')
    symdic_V2446 = Sym('V2446')
    symdic_Zx45Y = Sym('Z-Y')
    symdic_V868 = Sym('V868')
    symdic_V869 = Sym('V869')
    symdic_V718 = Sym('V718')
    symdic_V719 = Sym('V719')
    symdic_V716 = Sym('V716')
    symdic_V717 = Sym('V717')
    symdic_V714 = Sym('V714')
    symdic_V715 = Sym('V715')
    symdic_V712 = Sym('V712')
    symdic_V713 = Sym('V713')
    symdic_shen_group_clauses = Sym('shen.group_clauses')
    symdic_Parse_shen_x60namex62 = Sym('Parse_shen.<name>')
    symdic_Parse_shen_x60numberx62 = Sym('Parse_shen.<number>')
    symdic_V2367 = Sym('V2367')
    symdic_V2919 = Sym('V2919')
    symdic_V2918 = Sym('V2918')
    symdic_V2913 = Sym('V2913')
    symdic_V2912 = Sym('V2912')
    symdic_V2911 = Sym('V2911')
    symdic_V2910 = Sym('V2910')
    symdic_V2917 = Sym('V2917')
    symdic_V2916 = Sym('V2916')
    symdic_V2915 = Sym('V2915')
    symdic_V2914 = Sym('V2914')
    symdic_shen_pvar = Sym('shen.pvar')
    symdic_V1480 = Sym('V1480')
    symdic_shen_x42spyx42 = Sym('shen.*spy*')
    symdic_V1485 = Sym('V1485')
    symdic_Parse_shen_x60clausesx42x62 = Sym('Parse_shen.<clauses*>')
    symdic_V1648 = Sym('V1648')
    symdic_V924 = Sym('V924')
    symdic_V1642 = Sym('V1642')
    symdic_V1643 = Sym('V1643')
    symdic_shen_doublex45x62singles = Sym('shen.double->singles')
    symdic_V2352 = Sym('V2352')
    symdic_V2357 = Sym('V2357')
    symdic_NewHyps = Sym('NewHyps')
    symdic_V2359 = Sym('V2359')
    symdic_V2358 = Sym('V2358')
    symdic_X2401 = Sym('X2401')
    symdic_V914 = Sym('V914')
    symdic_V915 = Sym('V915')
    symdic_V2595 = Sym('V2595')
    symdic_V2594 = Sym('V2594')
    symdic_V2593 = Sym('V2593')
    symdic_V2592 = Sym('V2592')
    symdic_Parse_shen_x60rrbx62 = Sym('Parse_shen.<rrb>')
    symdic_V2590 = Sym('V2590')
    symdic_Fx38x38 = Sym('F&&')
    symdic_V2171 = Sym('V2171')
    symdic_V2170 = Sym('V2170')
    symdic_shen_showx45assumptions = Sym('shen.show-assumptions')
    symdic_V1306 = Sym('V1306')
    symdic_kl_x33 = Sym('!')
    symdic_shen_unwindx45types = Sym('shen.unwind-types')
    symdic_V2380 = Sym('V2380')
    symdic_shen_extract_vars = Sym('shen.extract_vars')
    symdic_V2773 = Sym('V2773')
    symdic_V2221 = Sym('V2221')
    symdic_V2771 = Sym('V2771')
    symdic_V2770 = Sym('V2770')
    symdic_V2777 = Sym('V2777')
    symdic_V2776 = Sym('V2776')
    symdic_V2775 = Sym('V2775')
    symdic_V2774 = Sym('V2774')
    symdic_V2779 = Sym('V2779')
    symdic_V2778 = Sym('V2778')
    symdic_V2007 = Sym('V2007')
    symdic_V2006 = Sym('V2006')
    symdic_Parse_shen_x60multilinex62 = Sym('Parse_shen.<multiline>')
    symdic_Parse_shen_x60predicatex42x62 = Sym('Parse_shen.<predicate*>')
    symdic_V2009 = Sym('V2009')
    symdic_V2008 = Sym('V2008')
    symdic_Parse_shen_x60guardx62 = Sym('Parse_shen.<guard>')
    symdic_V1264 = Sym('V1264')
    symdic_V1265 = Sym('V1265')
    symdic_kl_numberx63 = Sym('number?')
    symdic_V2226 = Sym('V2226')
    symdic_shen_putx47getx45macro = Sym('shen.put/get-macro')
    symdic_V1465 = Sym('V1465')
    symdic_V1460 = Sym('V1460')
    symdic_Variables = Sym('Variables')
    symdic_shen_remove_modes = Sym('shen.remove_modes')
    symdic_shen_getx45rules = Sym('shen.get-rules')
    symdic_V2651 = Sym('V2651')
    symdic_V779 = Sym('V779')
    symdic_kl_systemf = Sym('systemf')
    symdic_kl_writex45tox45file = Sym('write-to-file')
    symdic_Hash = Sym('Hash')
    symdic_shen_dhx63 = Sym('shen.dh?')
    symdic_shen_syntaxx45hyps = Sym('shen.syntax-hyps')
    symdic_shen_magless = Sym('shen.magless')
    symdic_Parse_x60ex62 = Sym('Parse_<e>')
    symdic_shen_pre = Sym('shen.pre')
    symdic_Err = Sym('Err')
    symdic_L = Sym('L')
    symdic_kl_number = Sym('number')
    symdic_V1071 = Sym('V1071')
    symdic_V1070 = Sym('V1070')
    symdic_V1073 = Sym('V1073')
    symdic_V1075 = Sym('V1075')
    symdic_V1074 = Sym('V1074')
    symdic_V1076 = Sym('V1076')
    symdic_Parse_shen_x60Ex62 = Sym('Parse_shen.<E>')
    symdic_kl_fwhen = Sym('fwhen')
    symdic_shen_recursivelyx45print = Sym('shen.recursively-print')
    symdic_shen_void = Sym('shen.void')
    symdic_shen_mu = Sym('shen.mu')
    symdic_shen_functionx45abstraction = Sym('shen.function-abstraction')
    symdic_shen_x42maxinferencesx42 = Sym('shen.*maxinferences*')
    symdic_FType = Sym('FType')
    symdic_shen_remember = Sym('shen.remember')
    symdic_Parse_shen_x60alphanumsx62 = Sym('Parse_shen.<alphanums>')
    symdic_shen_elimx45def = Sym('shen.elim-def')
    symdic_BigVector = Sym('BigVector')
    symdic_V2587 = Sym('V2587')
    symdic_TypedCondExpression = Sym('TypedCondExpression')
    symdic_V1109 = Sym('V1109')
    symdic_V1108 = Sym('V1108')
    symdic_V1105 = Sym('V1105')
    symdic_V1104 = Sym('V1104')
    symdic_V1107 = Sym('V1107')
    symdic_shen_codex45point = Sym('shen.code-point')
    symdic_V1101 = Sym('V1101')
    symdic_V1100 = Sym('V1100')
    symdic_V1103 = Sym('V1103')
    symdic_V1102 = Sym('V1102')
    symdic_Parse_shen_x60pattern1x62 = Sym('Parse_shen.<pattern1>')
    symdic_kl_print = Sym('print')
    symdic_shen_dereferencing = Sym('shen.dereferencing')
    symdic_kl_put = Sym('put')
    symdic_V866 = Sym('V866')
    symdic_V2701 = Sym('V2701')
    symdic_shen_cons_form = Sym('shen.cons_form')
    symdic_V2706 = Sym('V2706')
    symdic_shen_x42installingx45klx42 = Sym('shen.*installing-kl*')
    symdic_shen_integerx45testx63 = Sym('shen.integer-test?')
    symdic_V1921 = Sym('V1921')
    symdic_V1920 = Sym('V1920')
    symdic_V1927 = Sym('V1927')
    symdic_V1926 = Sym('V1926')
    symdic_V1925 = Sym('V1925')
    symdic_V1924 = Sym('V1924')
    symdic_V1929 = Sym('V1929')
    symdic_V1928 = Sym('V1928')
    symdic_shen_mapx45h = Sym('shen.map-h')
    symdic_shen_yacc_cases = Sym('shen.yacc_cases')
    symdic_shen_catchpoint = Sym('shen.catchpoint')
    symdic_shen_lazyderef = Sym('shen.lazyderef')
    symdic_V709 = Sym('V709')
    symdic_V708 = Sym('V708')
    symdic_shen_leftx45round = Sym('shen.left-round')
    symdic_V1855 = Sym('V1855')
    symdic_V1857 = Sym('V1857')
    symdic_V1856 = Sym('V1856')
    symdic_shen_alphax63 = Sym('shen.alpha?')
    symdic_V1854 = Sym('V1854')
    symdic_V1853 = Sym('V1853')
    symdic_V1852 = Sym('V1852')
    symdic_V1851 = Sym('V1851')
    symdic_V1850 = Sym('V1850')
    symdic_V877 = Sym('V877')
    symdic_V876 = Sym('V876')
    symdic_V875 = Sym('V875')
    symdic_V874 = Sym('V874')
    symdic_shen_credits = Sym('shen.credits')
    symdic_V1795 = Sym('V1795')
    symdic_V1859 = Sym('V1859')
    symdic_V1858 = Sym('V1858')
    symdic_V879 = Sym('V879')
    symdic_V878 = Sym('V878')
    symdic_shen_x60minusx62 = Sym('shen.<minus>')
    symdic_V2905 = Sym('V2905')
    symdic_shen_incinfs = Sym('shen.incinfs')
    symdic_V2907 = Sym('V2907')
    symdic_V2900 = Sym('V2900')
    symdic_V2901 = Sym('V2901')
    symdic_V2902 = Sym('V2902')
    symdic_V2903 = Sym('V2903')
    symdic_V2908 = Sym('V2908')
    symdic_V2909 = Sym('V2909')
    symdic_Parse_shen_x60anymultix62 = Sym('Parse_shen.<anymulti>')
    symdic_V873 = Sym('V873')
    symdic_Parse_shen_x60anysinglex62 = Sym('Parse_shen.<anysingle>')
    symdic_V872 = Sym('V872')
    symdic_shen_externalx45symbols = Sym('shen.external-symbols')
    symdic_V1533 = Sym('V1533')
    symdic_V871 = Sym('V871')
    symdic_kl_str = Sym('str')
    symdic_V672 = Sym('V672')
    symdic_V870 = Sym('V870')
    symdic_kl_declare = Sym('declare')
    symdic_shen_tx42x45pattern = Sym('shen.t*-pattern')
    symdic_V2510 = Sym('V2510')
    symdic_shen_variable = Sym('shen.variable')
    symdic_shen_nlx45macro = Sym('shen.nl-macro')
    symdic_V1670 = Sym('V1670')
    symdic_V1675 = Sym('V1675')
    symdic_V2342 = Sym('V2342')
    symdic_V2343 = Sym('V2343')
    symdic_V2340 = Sym('V2340')
    symdic_V2341 = Sym('V2341')
    symdic_V2346 = Sym('V2346')
    symdic_V2347 = Sym('V2347')
    symdic_V2344 = Sym('V2344')
    symdic_V2345 = Sym('V2345')
    symdic_shen_mkstrx45r = Sym('shen.mkstr-r')
    symdic_shen_listx63 = Sym('shen.list?')
    symdic_V907 = Sym('V907')
    symdic_V2581 = Sym('V2581')
    symdic_V2582 = Sym('V2582')
    symdic_V2583 = Sym('V2583')
    symdic_V2584 = Sym('V2584')
    symdic_V902 = Sym('V902')
    symdic_V901 = Sym('V901')
    symdic_V900 = Sym('V900')
    symdic_V2588 = Sym('V2588')
    symdic_V2589 = Sym('V2589')
    symdic_Xx43NewVector = Sym('X+NewVector')
    symdic_V2168 = Sym('V2168')
    symdic_V2169 = Sym('V2169')
    symdic_V1589 = Sym('V1589')
    symdic_V1588 = Sym('V1588')
    symdic_V2160 = Sym('V2160')
    symdic_V2166 = Sym('V2166')
    symdic_V2167 = Sym('V2167')
    symdic_V2165 = Sym('V2165')
    symdic_shen_prolog_constantx63 = Sym('shen.prolog_constant?')
    symdic_kl_assoc = Sym('assoc')
    symdic_shen_printx45vectorx63 = Sym('shen.print-vector?')
    symdic_Parse_shen_x60stopx62 = Sym('Parse_shen.<stop>')
    symdic_Patterns = Sym('Patterns')
    symdic_Parse_shen_x60alphanumx62 = Sym('Parse_shen.<alphanum>')
    symdic_V2768 = Sym('V2768')
    symdic_V2769 = Sym('V2769')
    symdic_V2764 = Sym('V2764')
    symdic_V2765 = Sym('V2765')
    symdic_V2766 = Sym('V2766')
    symdic_V2767 = Sym('V2767')
    symdic_V2760 = Sym('V2760')
    symdic_V2761 = Sym('V2761')
    symdic_V2762 = Sym('V2762')
    symdic_V2763 = Sym('V2763')
    symdic_V2016 = Sym('V2016')
    symdic_V2015 = Sym('V2015')
    symdic_V2010 = Sym('V2010')
    symdic_V2011 = Sym('V2011')
    symdic_V2019 = Sym('V2019')
    symdic_shen_outx45ofx45bounds = Sym('shen.out-of-bounds')
    symdic_V1298 = Sym('V1298')
    symdic_V1295 = Sym('V1295')
    symdic_V1297 = Sym('V1297')
    symdic_V1296 = Sym('V1296')
    symdic_V1291 = Sym('V1291')
    symdic_V1290 = Sym('V1290')
    symdic_shen_compile_to_machine_code = Sym('shen.compile_to_machine_code')
    symdic_V1450 = Sym('V1450')
    symdic_V1455 = Sym('V1455')
    symdic_V2637 = Sym('V2637')
    symdic_V2860 = Sym('V2860')
    symdic_shen_x42catchx42 = Sym('shen.*catch*')
    symdic_NewTable = Sym('NewTable')
    symdic_V3027 = Sym('V3027')
    symdic_V2149 = Sym('V2149')
    symdic_shen_insertx45predicate = Sym('shen.insert-predicate')
    symdic_kl_x59 = Sym(';')
    symdic_V3022 = Sym('V3022')
    symdic_kl_enablex45typex45theory = Sym('enable-type-theory')
    symdic_Lambdax43 = Sym('Lambda+')
    symdic_V3023 = Sym('V3023')
    symdic_kl_remove = Sym('remove')
    symdic_Parse_shen_x60barx62 = Sym('Parse_shen.<bar>')
    symdic_V2516 = Sym('V2516')
    symdic_shen_constructx45searchx45literals = Sym('shen.construct-search-literals')
    symdic_V2390 = Sym('V2390')
    symdic_kl_set = Sym('set')
    symdic_V3028 = Sym('V3028')
    symdic_shen_x60sigx43rulesx62 = Sym('shen.<sig+rules>')
    symdic_V1062 = Sym('V1062')
    symdic_V1063 = Sym('V1063')
    symdic_V1060 = Sym('V1060')
    symdic_V1061 = Sym('V1061')
    symdic_V1066 = Sym('V1066')
    symdic_shen_checkx45byte = Sym('shen.check-byte')
    symdic_V1064 = Sym('V1064')
    symdic_V1065 = Sym('V1065')
    symdic_kl_close = Sym('close')
    symdic_V1069 = Sym('V1069')
    symdic_shen_checkx45defccx45rule = Sym('shen.check-defcc-rule')
    symdic_Parse_shen_x60timesx62 = Sym('Parse_shen.<times>')
    symdic_V677 = Sym('V677')
    symdic_Parse_shen_x60pattern2x62 = Sym('Parse_shen.<pattern2>')
    symdic_kl_barx33 = Sym('bar!')
    symdic_shen_thisx45symbolx45isx45unbound = Sym('shen.this-symbol-is-unbound')
    symdic_shen_x60digitx62 = Sym('shen.<digit>')
    symdic_kl_reverse = Sym('reverse')
    symdic_V1116 = Sym('V1116')
    symdic_kl_errorx45tox45string = Sym('error-to-string')
    symdic_V1114 = Sym('V1114')
    symdic_V1115 = Sym('V1115')
    symdic_V1113 = Sym('V1113')
    symdic_V1110 = Sym('V1110')
    symdic_shen_x42prologvectorsx42 = Sym('shen.*prologvectors*')
    symdic_kl_load = Sym('load')
    symdic_shen_mu_reduction = Sym('shen.mu_reduction')
    symdic_kl_pr = Sym('pr')
    symdic_kl_ps = Sym('ps')
    symdic_shen_demodulate = Sym('shen.demodulate')
    symdic_shen_packagedx63 = Sym('shen.packaged?')
    symdic_shen_removex45h = Sym('shen.remove-h')
    symdic_shen_addx45macro = Sym('shen.add-macro')
    symdic_V1935 = Sym('V1935')
    symdic_V1936 = Sym('V1936')
    symdic_V1937 = Sym('V1937')
    symdic_V1930 = Sym('V1930')
    symdic_V1931 = Sym('V1931')
    symdic_V1932 = Sym('V1932')
    symdic_N = Sym('N')
    symdic_Parse_shen_x60signaturex62 = Sym('Parse_shen.<signature>')
    symdic_shen_app = Sym('shen.app')
    symdic_V1087 = Sym('V1087')
    symdic_kl_unify = Sym('unify')
    symdic_Stream = Sym('Stream')
    symdic_shen_x60conclusionx62 = Sym('shen.<conclusion>')
    symdic_shen_alphanumx63 = Sym('shen.alphanum?')
    symdic_V1840 = Sym('V1840')
    symdic_V1841 = Sym('V1841')
    symdic_V1842 = Sym('V1842')
    symdic_V1843 = Sym('V1843')
    symdic_V1844 = Sym('V1844')
    symdic_V1845 = Sym('V1845')
    symdic_V1846 = Sym('V1846')
    symdic_V1847 = Sym('V1847')
    symdic_V1848 = Sym('V1848')
    symdic_V846 = Sym('V846')
    symdic_V847 = Sym('V847')
    symdic_Nx2 = Sym('Nx2')
    symdic_V2392 = Sym('V2392')
    symdic_kl_x60x61 = Sym('<=')
    symdic_shen_constructx45recursivex45searchx45clause = Sym('shen.construct-recursive-search-clause')
    symdic_V2971 = Sym('V2971')
    symdic_V2970 = Sym('V2970')
    symdic_V2973 = Sym('V2973')
    symdic_V2972 = Sym('V2972')
    symdic_V2975 = Sym('V2975')
    symdic_V2974 = Sym('V2974')
    symdic_V2977 = Sym('V2977')
    symdic_V2976 = Sym('V2976')
    symdic_V2979 = Sym('V2979')
    symdic_V2978 = Sym('V2978')
    symdic_kl_x60x45 = Sym('<-')
    symdic_kl_null = Sym('null')
    symdic_shen_x42specialx42 = Sym('shen.*special*')
    symdic_V607 = Sym('V607')
    symdic_V608 = Sym('V608')
    symdic_V609 = Sym('V609')
    symdic_V1664 = Sym('V1664')
    symdic_shen_jump_stream = Sym('shen.jump_stream')
    symdic_V1663 = Sym('V1663')
    symdic_readx43 = Sym('read+')
    symdic_V2487 = Sym('V2487')
    symdic_V2596 = Sym('V2596')
    symdic_Item = Sym('Item')
    symdic_Fst = Sym('Fst')
    symdic_Parse_shen_x60endx42x62 = Sym('Parse_shen.<end*>')
    symdic_V2808 = Sym('V2808')
    symdic_V2379 = Sym('V2379')
    symdic_V2378 = Sym('V2378')
    symdic_V2805 = Sym('V2805')
    symdic_V2804 = Sym('V2804')
    symdic_V2807 = Sym('V2807')
    symdic_V2806 = Sym('V2806')
    symdic_V2801 = Sym('V2801')
    symdic_V2800 = Sym('V2800')
    symdic_V2803 = Sym('V2803')
    symdic_V2802 = Sym('V2802')
    symdic_V2579 = Sym('V2579')
    symdic_V2578 = Sym('V2578')
    symdic_V934 = Sym('V934')
    symdic_shen_x64sx45macro = Sym('shen.@s-macro')
    symdic_V2574 = Sym('V2574')
    symdic_V939 = Sym('V939')
    symdic_V2573 = Sym('V2573')
    symdic_V2572 = Sym('V2572')
    symdic_V1592 = Sym('V1592')
    symdic_V1593 = Sym('V1593')
    symdic_V2397 = Sym('V2397')
    symdic_V2396 = Sym('V2396')
    symdic_V2391 = Sym('V2391')
    symdic_shen_linereadx45loop = Sym('shen.lineread-loop')
    symdic_V1594 = Sym('V1594')
    symdic_V1595 = Sym('V1595')
    symdic_shen_newcontinuation = Sym('shen.newcontinuation')
    symdic_ValidTypes = Sym('ValidTypes')
    symdic_V2399 = Sym('V2399')
    symdic_V2398 = Sym('V2398')
    symdic_shen_compilex45macro = Sym('shen.compile-macro')
    symdic_V2580 = Sym('V2580')
    symdic_kl_cut = Sym('cut')
    symdic_kl_x36 = Sym('$')
    symdic_EncodeChoices = Sym('EncodeChoices')
    symdic_V2719 = Sym('V2719')
    symdic_V2718 = Sym('V2718')
    symdic_V2468 = Sym('V2468')
    symdic_V2711 = Sym('V2711')
    symdic_kl_input = Sym('input')
    symdic_V2713 = Sym('V2713')
    symdic_V2712 = Sym('V2712')
    symdic_V2715 = Sym('V2715')
    symdic_V2714 = Sym('V2714')
    symdic_shen_rfasx45h = Sym('shen.rfas-h')
    symdic_V2716 = Sym('V2716')
    symdic_V2023 = Sym('V2023')
    symdic_V2022 = Sym('V2022')
    symdic_V2021 = Sym('V2021')
    symdic_V2020 = Sym('V2020')
    symdic_V2027 = Sym('V2027')
    symdic_V2026 = Sym('V2026')
    symdic_V2025 = Sym('V2025')
    symdic_V2024 = Sym('V2024')
    symdic_shen_head_abstraction = Sym('shen.head_abstraction')
    symdic_V2028 = Sym('V2028')
    symdic_Ob = Sym('Ob')
    symdic_shen_x43stringx63 = Sym('shen.+string?')
    symdic_V1288 = Sym('V1288')
    symdic_V1289 = Sym('V1289')
    symdic_V1286 = Sym('V1286')
    symdic_V1287 = Sym('V1287')
    symdic_V1284 = Sym('V1284')
    symdic_V1285 = Sym('V1285')
    symdic_shen_rename = Sym('shen.rename')
    symdic_V1283 = Sym('V1283')
    symdic_V1280 = Sym('V1280')
    symdic_V1281 = Sym('V1281')
    symdic_shen_compile_prolog_procedure = Sym('shen.compile_prolog_procedure')
    symdic_V1445 = Sym('V1445')
    symdic_V1440 = Sym('V1440')
    symdic_PastPrint = Sym('PastPrint')
    symdic_V2624 = Sym('V2624')
    symdic_V2627 = Sym('V2627')
    symdic_V2626 = Sym('V2626')
    symdic_V2153 = Sym('V2153')
    symdic_V2152 = Sym('V2152')
    symdic_V2151 = Sym('V2151')
    symdic_V2150 = Sym('V2150')
    symdic_V2629 = Sym('V2629')
    symdic_Find = Sym('Find')
    symdic_V2243 = Sym('V2243')
    symdic_shen_leftx45rule = Sym('shen.left-rule')
    symdic_V805 = Sym('V805')
    symdic_Pattern = Sym('Pattern')
    symdic_shen_iterx45vector = Sym('shen.iter-vector')
    symdic_V1583 = Sym('V1583')
    symdic_Input = Sym('Input')
    symdic_Parse_shen_x60lrbx62 = Sym('Parse_shen.<lrb>')
    symdic_shen_x60x45sem = Sym('shen.<-sem')
    symdic_String = Sym('String')
    symdic_shen_collect = Sym('shen.collect')
    symdic_VBody = Sym('VBody')
    symdic_kl_integerx63 = Sym('integer?')
    symdic_Throwcontrol = Sym('Throwcontrol')
    symdic_shen_typecheck = Sym('shen.typecheck')
    symdic_ResizeVectorIfNeeded = Sym('ResizeVectorIfNeeded')
    symdic_M = Sym('M')
    symdic_O = Sym('O')
    symdic_SearchClauses = Sym('SearchClauses')
    symdic_shen_bindv = Sym('shen.bindv')
    symdic_kl_step = Sym('step')
    symdic_V1055 = Sym('V1055')
    symdic_V1054 = Sym('V1054')
    symdic_V1053 = Sym('V1053')
    symdic_V1052 = Sym('V1052')
    symdic_V1051 = Sym('V1051')
    symdic_V1050 = Sym('V1050')
    symdic_Parse_shen_x60datatypex45rulex62 = Sym('Parse_shen.<datatype-rule>')
    symdic_Parse_Byte = Sym('Parse_Byte')
    symdic_Parse_shen_x60actionx62 = Sym('Parse_shen.<action>')
    symdic_Literal = Sym('Literal')
    symdic_shen_grammar_symbolx63 = Sym('shen.grammar_symbol?')
    symdic_V1129 = Sym('V1129')
    symdic_V1128 = Sym('V1128')
    symdic_Parameters = Sym('Parameters')
    symdic_kl_unspecialise = Sym('unspecialise')
    symdic_V1123 = Sym('V1123')
    symdic_V1122 = Sym('V1122')
    symdic_V1121 = Sym('V1121')
    symdic_V1120 = Sym('V1120')
    symdic_V1127 = Sym('V1127')
    symdic_V1126 = Sym('V1126')
    symdic_Context_1957 = Sym('Context_1957')
    symdic_shen_digitx63 = Sym('shen.digit?')
    symdic_kl_subst = Sym('subst')
    symdic_shen_tmsx45x62hyp = Sym('shen.tms->hyp')
    symdic_shen_abstraction_build = Sym('shen.abstraction_build')
    symdic_Predicates = Sym('Predicates')
    symdic_kl_x58 = Sym(':')
    symdic_Parse_shen_x60premisex62 = Sym('Parse_shen.<premise>')
    symdic_kl_defmacro = Sym('defmacro')
    symdic_shen_x60numberx62 = Sym('shen.<number>')
    symdic_shen_x60commax45symbolx62 = Sym('shen.<comma-symbol>')
    symdic_shen_show = Sym('shen.show')
    symdic_Load = Sym('Load')
    symdic_Keyx63 = Sym('Key?')
    symdic_shen_aah = Sym('shen.aah')
    symdic_Parse_shen_x60st_inputx62 = Sym('Parse_shen.<st_input>')
    symdic_shen_nestx45disjunct = Sym('shen.nest-disjunct')
    symdic_kl_precludex45allx45but = Sym('preclude-all-but')
    symdic_shen_pair = Sym('shen.pair')
    symdic_shen_argx45x62str = Sym('shen.arg->str')
    symdic_shen_cutpoint = Sym('shen.cutpoint')
    symdic_NewPatts = Sym('NewPatts')
    symdic_shen_assumetype = Sym('shen.assumetype')
    symdic_Tr = Sym('Tr')
    symdic_V1944 = Sym('V1944')
    symdic_kl_x60ex62 = Sym('<e>')
    symdic_kl_elementx63 = Sym('element?')
    symdic_kl_stringx45x62n = Sym('string->n')
    symdic_Tm = Sym('Tm')
    symdic_shen_leavex33 = Sym('shen.leave!')
    symdic_shen_jump_streamx63 = Sym('shen.jump_stream?')
    symdic_V854 = Sym('V854')
    symdic_Snd = Sym('Snd')
    symdic_V853 = Sym('V853')
    symdic_V852 = Sym('V852')
    symdic_shen_sigf = Sym('shen.sigf')
    symdic_V859 = Sym('V859')
    symdic_shen_x60semicolonx62 = Sym('shen.<semicolon>')
    symdic_shen_startx45newx45prologx45process = Sym('shen.start-new-prolog-process')
    symdic_V2886 = Sym('V2886')
    symdic_shen_shenx45x62kl = Sym('shen.shen->kl')
    symdic_shen_x42maxcomplexityx42 = Sym('shen.*maxcomplexity*')
    symdic_Continuation = Sym('Continuation')
    symdic_Case = Sym('Case')
    symdic_shen_prologx45form = Sym('shen.prolog-form')
    symdic_V2962 = Sym('V2962')
    symdic_V2963 = Sym('V2963')
    symdic_V2960 = Sym('V2960')
    symdic_V2961 = Sym('V2961')
    symdic_V2966 = Sym('V2966')
    symdic_V2967 = Sym('V2967')
    symdic_kl_eval = Sym('eval')
    symdic_V2965 = Sym('V2965')
    symdic_V2968 = Sym('V2968')
    symdic_V2969 = Sym('V2969')
    symdic_V1134 = Sym('V1134')
    symdic_V610 = Sym('V610')
    symdic_V615 = Sym('V615')
    symdic_V1612 = Sym('V1612')
    symdic_V1617 = Sym('V1617')
    symdic_V2492 = Sym('V2492')
    symdic_Parse_shen_x60log10x62 = Sym('Parse_shen.<log10>')
    symdic_V2490 = Sym('V2490')
    symdic_kl_booleanx63 = Sym('boolean?')
    symdic_V2496 = Sym('V2496')
    symdic_shen_truncate = Sym('shen.truncate')
    symdic_V2495 = Sym('V2495')
    symdic_shen_sysx45error = Sym('shen.sys-error')
    symdic_kl_inferences = Sym('inferences')
    symdic_V2368 = Sym('V2368')
    symdic_IncVar = Sym('IncVar')
    symdic_V2818 = Sym('V2818')
    symdic_V2819 = Sym('V2819')
    symdic_shen_m_prolog_to_sx45prolog_predicate = Sym('shen.m_prolog_to_s-prolog_predicate')
    symdic_V2814 = Sym('V2814')
    symdic_V2813 = Sym('V2813')
    symdic_V2366 = Sym('V2366')
    symdic_Parse_shen_x60rulex62 = Sym('Parse_shen.<rule>')
    symdic_V892 = Sym('V892')
    symdic_V929 = Sym('V929')
    symdic_kl_adjoin = Sym('adjoin')
    symdic_V2568 = Sym('V2568')
    symdic_Parse_shen_x60dbqx62 = Sym('Parse_shen.<dbq>')
    symdic_kl_include = Sym('include')
    symdic_V921 = Sym('V921')
    symdic_V920 = Sym('V920')
    symdic_V923 = Sym('V923')
    symdic_V922 = Sym('V922')
    symdic_V2386 = Sym('V2386')
    symdic_V2387 = Sym('V2387')
    symdic_V2384 = Sym('V2384')
    symdic_V2385 = Sym('V2385')
    symdic_V2382 = Sym('V2382')
    symdic_V2383 = Sym('V2383')
    symdic_shen_x60formulaex62 = Sym('shen.<formulae>')
    symdic_V2381 = Sym('V2381')
    symdic_DecArity = Sym('DecArity')
    symdic_V2388 = Sym('V2388')
    symdic_V2389 = Sym('V2389')
    symdic_P = Sym('P')
    symdic_Parse_shen_x60lcurlyx62 = Sym('Parse_shen.<lcurly>')
    symdic_V1725 = Sym('V1725')
    symdic_V1724 = Sym('V1724')
    symdic_V1726 = Sym('V1726')
    symdic_V1721 = Sym('V1721')
    symdic_V1720 = Sym('V1720')
    symdic_V1723 = Sym('V1723')
    symdic_V1722 = Sym('V1722')
    symdic_V2708 = Sym('V2708')
    symdic_V2709 = Sym('V2709')
    symdic_shen_complexity = Sym('shen.complexity')
    symdic_V2702 = Sym('V2702')
    symdic_V2703 = Sym('V2703')
    symdic_V2700 = Sym('V2700')
    symdic_shen_recursive_descent = Sym('shen.recursive_descent')
    symdic_shen_assocx45macro = Sym('shen.assoc-macro')
    symdic_V2707 = Sym('V2707')
    symdic_V2704 = Sym('V2704')
    symdic_V2705 = Sym('V2705')
    symdic_V2038 = Sym('V2038')
    symdic_V2037 = Sym('V2037')
    symdic_shen_typetable = Sym('shen.typetable')
    symdic_kl_append = Sym('append')
    symdic_V1439 = Sym('V1439')
    symdic_V1434 = Sym('V1434')
    symdic_V2636 = Sym('V2636')
    symdic_shen_x60alphanumsx62 = Sym('shen.<alphanums>')
    symdic_V2634 = Sym('V2634')
    symdic_V2635 = Sym('V2635')
    symdic_V2632 = Sym('V2632')
    symdic_V2633 = Sym('V2633')
    symdic_V2630 = Sym('V2630')
    symdic_V2631 = Sym('V2631')
    symdic_V2148 = Sym('V2148')
    symdic_shen_errx45condition = Sym('shen.err-condition')
    symdic_Line = Sym('Line')
    symdic_V1292 = Sym('V1292')
    symdic_V2638 = Sym('V2638')
    symdic_V2639 = Sym('V2639')
    symdic_shen_tx42x45defhh = Sym('shen.t*-defhh')
    symdic_shen_x60headx42x62 = Sym('shen.<head*>')
    symdic_V1518 = Sym('V1518')
    symdic_kl_let = Sym('let')
    symdic_shen_list_stream = Sym('shen.list_stream')
    symdic_V1543 = Sym('V1543')
    symdic_shen_x43vector = Sym('shen.+vector')
    symdic_shen_processx45datatype = Sym('shen.process-datatype')
    symdic_shen_pushnew = Sym('shen.pushnew')
    symdic_V1548 = Sym('V1548')
    symdic_NewConclusion = Sym('NewConclusion')
    symdic_kl_x123 = Sym('{')
    symdic_shen_casex45form = Sym('shen.case-form')
    symdic_kl_simplex45error = Sym('simple-error')
    symdic_shen_makex45key = Sym('shen.make-key')
    symdic_shen_free_variable_warnings = Sym('shen.free_variable_warnings')
    symdic_V1049 = Sym('V1049')
    symdic_kl_boolean = Sym('boolean')
    symdic_V1514 = Sym('V1514')
    symdic_V1041 = Sym('V1041')
    symdic_V1042 = Sym('V1042')
    symdic_V1044 = Sym('V1044')
    symdic_V1045 = Sym('V1045')
    symdic_V1046 = Sym('V1046')
    symdic_kl_x60x45x45 = Sym('<--')
    symdic_Parse_shen_x60datatypex45rulesx62 = Sym('Parse_shen.<datatype-rules>')
    symdic_kl_nx45x62string = Sym('n->string')
    symdic_V2531 = Sym('V2531')
    symdic_Parse_shen_x60whitespacesx62 = Sym('Parse_shen.<whitespaces>')
    symdic_V2530 = Sym('V2530')
    symdic_V2533 = Sym('V2533')
    symdic_kl_stinput = Sym('stinput')
    symdic_V1135 = Sym('V1135')
    symdic_V1136 = Sym('V1136')
    symdic_V1137 = Sym('V1137')
    symdic_V1130 = Sym('V1130')
    symdic_V1131 = Sym('V1131')
    symdic_V1132 = Sym('V1132')
    symdic_shen_embedx45and = Sym('shen.embed-and')
    symdic_shen_intprologx45helpx45help = Sym('shen.intprolog-help-help')
    symdic_shen_split_cc_rules = Sym('shen.split_cc_rules')
    symdic_V2534 = Sym('V2534')
    symdic_V2537 = Sym('V2537')
    symdic_V2536 = Sym('V2536')
    symdic_Parse_shen_x60st_input2x62 = Sym('Parse_shen.<st_input2>')
    symdic_Syntax = Sym('Syntax')
    symdic_shen_uex45hx63 = Sym('shen.ue-h?')
    symdic_Fx42 = Sym('F*')
    symdic_V2924 = Sym('V2924')
    symdic_shen_profilex45help = Sym('shen.profile-help')
    symdic_V2434 = Sym('V2434')
    symdic_V2435 = Sym('V2435')
    symdic_shen_then = Sym('shen.then')
    symdic_V2436 = Sym('V2436')
    symdic_V2437 = Sym('V2437')
    symdic_Variancy = Sym('Variancy')
    symdic_shen_atomx45x62str = Sym('shen.atom->str')
    symdic_kl_x42homex45directoryx42 = Sym('*home-directory*')
    symdic_shen_rulesx45x62hornx45clauses = Sym('shen.rules->horn-clauses')
    symdic_shen_profilex45func = Sym('shen.profile-func')
    symdic_kl_profile = Sym('profile')
    symdic_shen_nextx4550 = Sym('shen.next-50')
    symdic_V1958 = Sym('V1958')
    symdic_V1959 = Sym('V1959')
    symdic_V1952 = Sym('V1952')
    symdic_V1951 = Sym('V1951')
    symdic_V1956 = Sym('V1956')
    symdic_V1957 = Sym('V1957')
    symdic_V1955 = Sym('V1955')
    symdic_Q = Sym('Q')
    symdic_Value = Sym('Value')
    symdic_Parse_shen_x60variablex63x62 = Sym('Parse_shen.<variable?>')
    symdic_V820 = Sym('V820')
    symdic_V821 = Sym('V821')
    symdic_V822 = Sym('V822')
    symdic_V823 = Sym('V823')
    symdic_V824 = Sym('V824')
    symdic_V825 = Sym('V825')
    symdic_V826 = Sym('V826')
    symdic_V827 = Sym('V827')
    symdic_V828 = Sym('V828')
    symdic_kl_bind = Sym('bind')
    symdic_Results = Sym('Results')
    symdic_kl_readx45fromx45string = Sym('read-from-string')
    symdic_shen_analysex45variablex63 = Sym('shen.analyse-variable?')
    symdic_shen_x42synonymsx42 = Sym('shen.*synonyms*')
    symdic_shen_x60symx62 = Sym('shen.<sym>')
    symdic_shen_maxinfexceededx63 = Sym('shen.maxinfexceeded?')
    symdic_V2959 = Sym('V2959')
    symdic_shen_reverse_help = Sym('shen.reverse_help')
    symdic_V2957 = Sym('V2957')
    symdic_shen_x60bytex62 = Sym('shen.<byte>')
    symdic_V2955 = Sym('V2955')
    symdic_V2954 = Sym('V2954')
    symdic_V2953 = Sym('V2953')
    symdic_V2952 = Sym('V2952')
    symdic_shen_x60simple_patternx62 = Sym('shen.<simple_pattern>')
    symdic_V2950 = Sym('V2950')
    symdic_kl_failx45if = Sym('fail-if')
    symdic_V629 = Sym('V629')
    symdic_V626 = Sym('V626')
    symdic_kl_x60 = Sym('<')
    symdic_V620 = Sym('V620')
    symdic_V621 = Sym('V621')
    symdic_kl_unifyx33 = Sym('unify!')
    symdic_V1607 = Sym('V1607')
    symdic_V1604 = Sym('V1604')
    symdic_V1605 = Sym('V1605')
    symdic_shen_getx45profile = Sym('shen.get-profile')
    symdic_shen_optimise = Sym('shen.optimise')
    symdic_Out_1957 = Sym('Out_1957')
    symdic_Parse_shen_x60sidex45conditionsx62 = Sym('Parse_shen.<side-conditions>')
    symdic_kl_symbolx63 = Sym('symbol?')
    symdic_V2829 = Sym('V2829')
    symdic_V2828 = Sym('V2828')
    symdic_V2823 = Sym('V2823')
    symdic_V2822 = Sym('V2822')
    symdic_shen_r = Sym('shen.r')
    symdic_shen_s = Sym('shen.s')
    symdic_V2827 = Sym('V2827')
    symdic_V2826 = Sym('V2826')
    symdic_shen_x60atomx62 = Sym('shen.<atom>')
    symdic_V2824 = Sym('V2824')
    symdic_shen_removex45bar = Sym('shen.remove-bar')
    symdic_kl_mode = Sym('mode')
    symdic_V2553 = Sym('V2553')
    symdic_shen_a = Sym('shen.a')
    symdic_V2551 = Sym('V2551')
    symdic_V2550 = Sym('V2550')
    symdic_V954 = Sym('V954')
    symdic_V955 = Sym('V955')
    symdic_V758 = Sym('V758')
    symdic_V2691 = Sym('V2691')
    symdic_kl_map = Sym('map')
    symdic_shen_compressx4550 = Sym('shen.compress-50')
    symdic_V1811 = Sym('V1811')
    symdic_Next = Sym('Next')
    symdic_V1738 = Sym('V1738')
    symdic_V1739 = Sym('V1739')
    symdic_Print = Sym('Print')
    symdic_V1737 = Sym('V1737')
    symdic_V1734 = Sym('V1734')
    symdic_shen_assignx45types = Sym('shen.assign-types')
    symdic_V1733 = Sym('V1733')
    symdic_V1731 = Sym('V1731')
    symdic_kl_yx45orx45nx63 = Sym('y-or-n?')
    symdic_V2736 = Sym('V2736')
    symdic_V2735 = Sym('V2735')
    symdic_shen_x60singlelinex62 = Sym('shen.<singleline>')
    symdic_kl_stringx45x62symbol = Sym('string->symbol')
    symdic_V2732 = Sym('V2732')
    symdic_V2731 = Sym('V2731')
    symdic_V2730 = Sym('V2730')
    symdic_shen_initialise_arity_table = Sym('shen.initialise_arity_table')
    symdic_V2739 = Sym('V2739')
    symdic_V2738 = Sym('V2738')
    symdic_shen_list_variables = Sym('shen.list_variables')
    symdic_V2045 = Sym('V2045')
    symdic_V2044 = Sym('V2044')
    symdic_Parse_shen_x60commax62 = Sym('Parse_shen.<comma>')
    symdic_VTerms = Sym('VTerms')
    symdic_V1429 = Sym('V1429')
    symdic_YaccCases = Sym('YaccCases')
    symdic_shen_demodh = Sym('shen.demodh')
    symdic_V1424 = Sym('V1424')
    symdic_V2603 = Sym('V2603')
    symdic_V2602 = Sym('V2602')
    symdic_kl_length = Sym('length')
    symdic_V2600 = Sym('V2600')
    symdic_V2607 = Sym('V2607')
    symdic_V2606 = Sym('V2606')
    symdic_V2605 = Sym('V2605')
    symdic_V2604 = Sym('V2604')
    symdic_shen_choicepointx33 = Sym('shen.choicepoint!')
    symdic_V2609 = Sym('V2609')
    symdic_V2608 = Sym('V2608')
    symdic_CatchKill = Sym('CatchKill')
    symdic_kl_occurrences = Sym('occurrences')
    symdic_shen_x42shenx45typex45theoryx45enabledx63x42 = Sym('shen.*shen-type-theory-enabled?*')
    symdic_Parse_shen_x60conclusionx62 = Sym('Parse_shen.<conclusion>')
    symdic_V1553 = Sym('V1553')
    symdic_V2992 = Sym('V2992')
    symdic_Symbol = Sym('Symbol')
    symdic_shen_succeedsx63 = Sym('shen.succeeds?')
    symdic_V1558 = Sym('V1558')
    symdic_shen_datatypex45macro = Sym('shen.datatype-macro')
    symdic_V2449 = Sym('V2449')
    symdic_shen_resizeprocessvector = Sym('shen.resizeprocessvector')
    symdic_V2448 = Sym('V2448')
    symdic_shen_multiplex45set = Sym('shen.multiple-set')
    symdic_x42hushx42 = Sym('*hush*')
    symdic_shen_x60st_input1x62 = Sym('shen.<st_input1>')
    symdic_kl_getx45time = Sym('get-time')
    symdic_shen_x60clausesx42x62 = Sym('shen.<clauses*>')
    symdic_Absx45N = Sym('Abs-N')
    symdic_V2447 = Sym('V2447')
    symdic_kl_x61x61x62 = Sym('==>')
    symdic_shen_insert_modes = Sym('shen.insert_modes')
    symdic_Bx38x38 = Sym('B&&')
    symdic_shen_analysex45kill = Sym('shen.analyse-kill')
    symdic_shen_the = Sym('shen.the')
    symdic_V829 = Sym('V829')
    symdic_kl_function = Sym('function')
    symdic_V2264 = Sym('V2264')
    symdic_CompileG = Sym('CompileG')
    symdic_shen_synonymsx45macro = Sym('shen.synonyms-macro')
    symdic_shen_controlx45chars = Sym('shen.control-chars')
    symdic_V1143 = Sym('V1143')
    symdic_V1142 = Sym('V1142')
    symdic_shen_by_hypothesis = Sym('shen.by_hypothesis')
    symdic_V1144 = Sym('V1144')
    symdic_V1149 = Sym('V1149')
    symdic_shen_specialx63 = Sym('shen.special?')
    symdic_V1384 = Sym('V1384')
    symdic_shen_mkstr = Sym('shen.mkstr')
    symdic_V1389 = Sym('V1389')
    symdic_shen_curry = Sym('shen.curry')
    symdic_shen_insertx45prologx45variables = Sym('shen.insert-prolog-variables')
    symdic_kl_x61 = Sym('=')
    symdic_Parse_shen_x60digitx62 = Sym('Parse_shen.<digit>')
    symdic_V2107 = Sym('V2107')
    symdic_kl_hd = Sym('hd')
    symdic_shen_includex45h = Sym('shen.include-h')
    symdic_AUM_instructions = Sym('AUM_instructions')
    symdic_Parse_shen_x60sidex45conditionx62 = Sym('Parse_shen.<side-condition>')
    symdic_V1097 = Sym('V1097')
    symdic_shen_defprologx45macro = Sym('shen.defprolog-macro')
    symdic_V1099 = Sym('V1099')
    symdic_V1098 = Sym('V1098')
    symdic_kl_x125 = Sym('}')
    symdic_shen_casesx45macro = Sym('shen.cases-macro')
    symdic_FORMAT = Sym('FORMAT')
    symdic_V1154 = Sym('V1154')
    symdic_shen_aritycheckx45name = Sym('shen.aritycheck-name')
    symdic_V2661 = Sym('V2661')
    symdic_shen_fillvector = Sym('shen.fillvector')
    symdic_V837 = Sym('V837')
    symdic_V836 = Sym('V836')
    symdic_V835 = Sym('V835')
    symdic_V834 = Sym('V834')
    symdic_V2660 = Sym('V2660')
    symdic_V1899 = Sym('V1899')
    symdic_Assumption_1957 = Sym('Assumption_1957')
    symdic_V1893 = Sym('V1893')
    symdic_V1892 = Sym('V1892')
    symdic_kl_x61x61 = Sym('==')
    symdic_Initialise = Sym('Initialise')
    symdic_V2663 = Sym('V2663')
    symdic_shen_x60namex62 = Sym('shen.<name>')
    symdic_V2949 = Sym('V2949')
    symdic_kl_x61x33 = Sym('=!')
    symdic_V2944 = Sym('V2944')
    symdic_V2945 = Sym('V2945')
    symdic_V2946 = Sym('V2946')
    symdic_V2947 = Sym('V2947')
    symdic_kl_addressx45x62 = Sym('address->')
    symdic_shen_x60sidex45conditionx62 = Sym('shen.<side-condition>')
    symdic_shen_placeholder = Sym('shen.placeholder')
    symdic_V2662 = Sym('V2662')
    symdic_V639 = Sym('V639')
    symdic_V1963 = Sym('V1963')
    symdic_V1962 = Sym('V1962')
    symdic_V1961 = Sym('V1961')
    symdic_V1960 = Sym('V1960')
    symdic_CurrExceptions = Sym('CurrExceptions')
    symdic_V634 = Sym('V634')
    symdic_V1637 = Sym('V1637')
    symdic_V2958 = Sym('V2958')
    symdic_V1632 = Sym('V1632')
    symdic_shen_recordx45exceptions = Sym('shen.record-exceptions')
    symdic_kl_freeze = Sym('freeze')
    symdic_Source = Sym('Source')
    symdic_V2836 = Sym('V2836')
    symdic_V2830 = Sym('V2830')
    symdic_V2831 = Sym('V2831')
    symdic_V2956 = Sym('V2956')
    symdic_shen_evalx45withoutx45macros = Sym('shen.eval-without-macros')
    symdic_shen_x60colonx62 = Sym('shen.<colon>')
    symdic_V2544 = Sym('V2544')
    symdic_V2746 = Sym('V2746')
    symdic_V2546 = Sym('V2546')
    symdic_kl_error = Sym('error')
    symdic_V2747 = Sym('V2747')
    symdic_V2548 = Sym('V2548')
    symdic_V2744 = Sym('V2744')
    symdic_V949 = Sym('V949')
    symdic_Parse_shen_x60nonx45returnx62 = Sym('Parse_shen.<non-return>')
    symdic_shen_x60patternx62 = Sym('shen.<pattern>')
    symdic_FilterDatatypes = Sym('FilterDatatypes')
    symdic_shen_tx42x45defh = Sym('shen.t*-defh')
    symdic_V3015 = Sym('V3015')
    symdic_V2742 = Sym('V2742')
    symdic_V3017 = Sym('V3017')
    symdic_V3016 = Sym('V3016')
    symdic_V3011 = Sym('V3011')
    symdic_V3010 = Sym('V3010')
    symdic_V3013 = Sym('V3013')
    symdic_V944 = Sym('V944')
    symdic_V2740 = Sym('V2740')
    symdic_shen_functionx45macro = Sym('shen.function-macro')
    symdic_Parse_shen_x60commentx62 = Sym('Parse_shen.<comment>')
    symdic_V1709 = Sym('V1709')
    symdic_Vector = Sym('Vector')
    symdic_V2219 = Sym('V2219')
    symdic_V1701 = Sym('V1701')
    symdic_V1700 = Sym('V1700')
    symdic_V1706 = Sym('V1706')
    symdic_V2720 = Sym('V2720')
    symdic_V2721 = Sym('V2721')
    symdic_V2722 = Sym('V2722')
    symdic_V2723 = Sym('V2723')
    symdic_shen_newpv = Sym('shen.newpv')
    symdic_kl_tlv = Sym('tlv')
    symdic_V2726 = Sym('V2726')
    symdic_V2727 = Sym('V2727')
    symdic_V2728 = Sym('V2728')
    symdic_V2729 = Sym('V2729')
    symdic_shen_x42stepx42 = Sym('shen.*step*')
    symdic_Result = Sym('Result')
    symdic_shen_insertx45prologx45variablesx45help = Sym('shen.insert-prolog-variables-help')
    symdic_V2666 = Sym('V2666')
    symdic_Parse_shen_x60plusx62 = Sym('Parse_shen.<plus>')
    symdic_V2052 = Sym('V2052')
    symdic_V2053 = Sym('V2053')
    symdic_V2050 = Sym('V2050')
    symdic_V2051 = Sym('V2051')
    symdic_V2056 = Sym('V2056')
    symdic_shen_x60guardx62 = Sym('shen.<guard>')
    symdic_V2054 = Sym('V2054')
    symdic_kl_cd = Sym('cd')
    symdic_V1414 = Sym('V1414')
    symdic_V1419 = Sym('V1419')
    symdic_V2532 = Sym('V2532')
    symdic_V2618 = Sym('V2618')
    symdic_V2619 = Sym('V2619')
    symdic_kl_stoutput = Sym('stoutput')
    symdic_V2614 = Sym('V2614')
    symdic_V2615 = Sym('V2615')
    symdic_shen_x60definex62 = Sym('shen.<define>')
    symdic_V2617 = Sym('V2617')
    symdic_V2610 = Sym('V2610')
    symdic_V2611 = Sym('V2611')
    symdic_V2612 = Sym('V2612')
    symdic_kl_x62 = Sym('>')
    symdic_shen_f_error = Sym('shen.f_error')
    symdic_kl_untrack = Sym('untrack')
    symdic_PackageNameDot = Sym('PackageNameDot')
    symdic_V753 = Sym('V753')
    symdic_V1563 = Sym('V1563')
    symdic_V1568 = Sym('V1568')
    symdic_shen_x60alphax62 = Sym('shen.<alpha>')
    symdic_kl_value = Sym('value')
    symdic_Restx38x38 = Sym('Rest&&')
    symdic_Semantics = Sym('Semantics')
    symdic_shen_x42readerx45macrosx42 = Sym('shen.*reader-macros*')
    symdic_shen_typex45signaturex45ofx45 = Sym('shen.type-signature-of-')
    symdic_TypeF = Sym('TypeF')
    symdic_Pastprint = Sym('Pastprint')
    symdic_shen_tx42 = Sym('shen.t*')
    symdic_V1606 = Sym('V1606')
    symdic_shen_x42systemx42 = Sym('shen.*system*')
    symdic_Semanticsx42 = Sym('Semantics*')
    symdic_shen_copyx45vectorx45stagex451 = Sym('shen.copy-vector-stage-1')
    symdic_shen_abs = Sym('shen.abs')
    symdic_shen_copyx45vectorx45stagex452 = Sym('shen.copy-vector-stage-2')
    symdic_kl_defun = Sym('defun')
    symdic_shen_x60postdigitsx62 = Sym('shen.<postdigits>')
    symdic_V1152 = Sym('V1152')
    symdic_V1153 = Sym('V1153')
    symdic_V1150 = Sym('V1150')
    symdic_V1151 = Sym('V1151')
    symdic_shen_to = Sym('shen.to')
    symdic_V1155 = Sym('V1155')
    symdic_shen_x60lsbx62 = Sym('shen.<lsb>')
    symdic_kl_x42languagex42 = Sym('*language*')
    symdic_kl_x47_ = Sym('/.')
    symdic_shen_insert_lazyderef = Sym('shen.insert_lazyderef')
    symdic_V1394 = Sym('V1394')
    symdic_V1395 = Sym('V1395')
    symdic_V1398 = Sym('V1398')
    symdic_shen_terminalx63 = Sym('shen.terminal?')
    symdic_shen_exclamation = Sym('shen.exclamation')
    symdic_shen_carriagex45return = Sym('shen.carriage-return')
    symdic_shen_plugx45wildcards = Sym('shen.plug-wildcards')
    symdic_Else = Sym('Else')
    symdic_shen_remtype = Sym('shen.remtype')
    symdic_shen_variables = Sym('shen.variables')
    symdic_Bytelist = Sym('Bytelist')
    symdic_NewDatatypes = Sym('NewDatatypes')
    symdic_V1088 = Sym('V1088')
    symdic_V1084 = Sym('V1084')
    symdic_V1085 = Sym('V1085')
    symdic_V1086 = Sym('V1086')
    symdic_shen_x60stopx62 = Sym('shen.<stop>')
    symdic_V1083 = Sym('V1083')
    symdic_kl_identical = Sym('identical')
    symdic_kl_tcx63 = Sym('tc?')
    symdic_shen_typex45theoryx45enabledx63 = Sym('shen.type-theory-enabled?')
    symdic_shen_base = Sym('shen.base')
    symdic_shen_failedx33 = Sym('shen.failed!')
    symdic_Hyp = Sym('Hyp')
    symdic_V2411 = Sym('V2411')
    symdic_Limit = Sym('Limit')
    symdic_T = Sym('T')
    symdic_kl_intersection = Sym('intersection')
    symdic_V2417 = Sym('V2417')
    symdic_V1880 = Sym('V1880')
    symdic_V1881 = Sym('V1881')
    symdic_V1882 = Sym('V1882')
    symdic_V1883 = Sym('V1883')
    symdic_V804 = Sym('V804')
    symdic_shen_sequent = Sym('shen.sequent')
    symdic_V802 = Sym('V802')
    symdic_V803 = Sym('V803')
    symdic_shen_x60nonx45returnx62 = Sym('shen.<non-return>')
    symdic_kl_preclude = Sym('preclude')
    symdic_V797 = Sym('V797')
    symdic_V2820 = Sym('V2820')
    symdic_shen_symbolx45codex63 = Sym('shen.symbol-code?')
    symdic_V798 = Sym('V798')
    symdic_V799 = Sym('V799')
    symdic_shen_x42extraspecialx42 = Sym('shen.*extraspecial*')
    symdic_V2825 = Sym('V2825')
    symdic_Parse_shen_x60strx62 = Sym('Parse_shen.<str>')
    symdic_shen_x60premisex62 = Sym('shen.<premise>')
    symdic_shen_x60Ex62 = Sym('shen.<E>')
    symdic_shen_same_predicatex63 = Sym('shen.same_predicate?')
    symdic_V1972 = Sym('V1972')
    symdic_V1973 = Sym('V1973')
    symdic_V1974 = Sym('V1974')
    symdic_V1976 = Sym('V1976')
    symdic_V1977 = Sym('V1977')
    symdic_V1978 = Sym('V1978')
    symdic_V1979 = Sym('V1979')
    symdic_V2616 = Sym('V2616')
    symdic_shen_constructorx45error = Sym('shen.constructor-error')
    symdic_V1622 = Sym('V1622')
    symdic_shen_posintx63 = Sym('shen.posint?')
    symdic_V1627 = Sym('V1627')
    symdic_V2845 = Sym('V2845')
    symdic_shen_x60doubleunderlinex62 = Sym('shen.<doubleunderline>')
    symdic_V2847 = Sym('V2847')
    symdic_V2846 = Sym('V2846')
    symdic_V2849 = Sym('V2849')
    symdic_V2848 = Sym('V2848')
    symdic_V976 = Sym('V976')
    symdic_V977 = Sym('V977')
    symdic_V974 = Sym('V974')
    symdic_V975 = Sym('V975')
    symdic_V972 = Sym('V972')
    symdic_V973 = Sym('V973')
    symdic_V970 = Sym('V970')
    symdic_V971 = Sym('V971')
    symdic_ListAx38x38 = Sym('ListA&&')
    symdic_V978 = Sym('V978')
    symdic_Zero = Sym('Zero')
    symdic_shen_f = Sym('shen.f')
    symdic_V3008 = Sym('V3008')
    symdic_V3009 = Sym('V3009')
    symdic_V3006 = Sym('V3006')
    symdic_V3007 = Sym('V3007')
    symdic_V3004 = Sym('V3004')
    symdic_V3005 = Sym('V3005')
    symdic_V3002 = Sym('V3002')
    symdic_V3003 = Sym('V3003')
    symdic_V3000 = Sym('V3000')
    symdic_V3001 = Sym('V3001')
    symdic_V1710 = Sym('V1710')
    symdic_V1711 = Sym('V1711')
    symdic_V1712 = Sym('V1712')
    symdic_V1713 = Sym('V1713')
    symdic_V1718 = Sym('V1718')
    symdic_V1719 = Sym('V1719')
    symdic_shen_x42alldatatypesx42 = Sym('shen.*alldatatypes*')
    symdic_In_1957 = Sym('In_1957')
    symdic_Entry = Sym('Entry')
    symdic_shen_constructx45searchx45clauses = Sym('shen.construct-search-clauses')
    symdic_kl_x42 = Sym('*')
    symdic_V2282 = Sym('V2282')
    symdic_V2281 = Sym('V2281')
    symdic_V2280 = Sym('V2280')
    symdic_V2993 = Sym('V2993')
    symdic_shen_extract_free_vars = Sym('shen.extract_free_vars')
    symdic_V2991 = Sym('V2991')
    symdic_V2990 = Sym('V2990')
    symdic_V2997 = Sym('V2997')
    symdic_V2996 = Sym('V2996')
    symdic_V2995 = Sym('V2995')
    symdic_V2994 = Sym('V2994')
    symdic_V2445 = Sym('V2445')
    symdic_V2999 = Sym('V2999')
    symdic_V2998 = Sym('V2998')
    symdic_shen_numbytex63 = Sym('shen.numbyte?')
    symdic_V2374 = Sym('V2374')
    symdic_V2265 = Sym('V2265')
    symdic_shen_analysex45symbolx63 = Sym('shen.analyse-symbol?')
    symdic_V2267 = Sym('V2267')
    symdic_V2266 = Sym('V2266')
    symdic_V2261 = Sym('V2261')
    symdic_V2263 = Sym('V2263')
    symdic_V2262 = Sym('V2262')
    symdic_shen_x60predicatex42x62 = Sym('shen.<predicate*>')
    symdic_V2613 = Sym('V2613')
    symdic_V1403 = Sym('V1403')
    symdic_V1404 = Sym('V1404')
    symdic_V1409 = Sym('V1409')
    symdic_X2441 = Sym('X2441')
    symdic_Def = Sym('Def')
    symdic_XTerms = Sym('XTerms')
    symdic_V2669 = Sym('V2669')
    symdic_V2668 = Sym('V2668')
    symdic_kl_limit = Sym('limit')
    symdic_V2193 = Sym('V2193')
    symdic_V2192 = Sym('V2192')
    symdic_V2191 = Sym('V2191')
    symdic_V2190 = Sym('V2190')
    symdic_V2665 = Sym('V2665')
    symdic_V2664 = Sym('V2664')
    symdic_V2195 = Sym('V2195')
    symdic_V2194 = Sym('V2194')
    symdic_V1282 = Sym('V1282')
    symdic_kl_x45x45x62 = Sym('-->')
    symdic_shen_packageh = Sym('shen.packageh')
    symdic_shen_terprix45orx45readx45char = Sym('shen.terpri-or-read-char')
    symdic_SideLiterals = Sym('SideLiterals')
    symdic_shen_extraspecialx63 = Sym('shen.extraspecial?')
    symdic_Restx38 = Sym('Rest&')
    symdic_Parse_shen_x60doubleunderlinex62 = Sym('Parse_shen.<doubleunderline>')
    symdic_V1578 = Sym('V1578')
    symdic_V1833 = Sym('V1833')
    symdic_shen_changex45pointerx45value = Sym('shen.change-pointer-value')
    symdic_V1732 = Sym('V1732')
    symdic_V1573 = Sym('V1573')
    symdic_V2067 = Sym('V2067')
    symdic_V2066 = Sym('V2066')
    symdic_V2065 = Sym('V2065')
    symdic_V2064 = Sym('V2064')
    symdic_V2063 = Sym('V2063')
    symdic_V2062 = Sym('V2062')
    symdic_V2061 = Sym('V2061')
    symdic_kl_out = Sym('out')
    symdic_V2068 = Sym('V2068')
    symdic_V2737 = Sym('V2737')
    symdic_kl_profilex45results = Sym('profile-results')
    symdic_V2734 = Sym('V2734')
    symdic_U = Sym('U')
    symdic_Context = Sym('Context')
    symdic_V2733 = Sym('V2733')
    symdic_shen_x60bodyx42x62 = Sym('shen.<body*>')
    symdic_shen_fboundx63 = Sym('shen.fbound?')
    symdic_shen_multiples = Sym('shen.multiples')
symdic = SymDic()
FUNCTIONS.update({'or': shen_or, 'and': shen_and})
VARS.update({'*language*': 'Python', '*implementation*': 'pyshen', '*release*': '', '*port*': '0.136', '*porters*': 'Matthieu Lagacherie and Yannick Drant', '*home-directory*': '~/', '*stinput*': shen_stdin(), '*stoutput*': shen_stdout(), '*version*': 'version 12'})


#============================== toplevel.kl==============================



@tail_recursion
def shen_shen():
    global symdic
    return [tco_apply(shen_credits, []), tail_call(shen_loop, [])][(-1)]
shen_add_fun('shen.shen', shen_shen, 0)

@tail_recursion
def shen_loop():
    global symdic
    return [tco_apply(shen_initialise_environment, []), [tco_apply(shen_prompt, []), [shen_try_except((lambda : tco_apply(shen_readx45evaluatex45print, [])), (lambda KL_ARG_E_0: shen_pr(KL_ARG_E_0.message, tco_apply(kl_stoutput, [])))), tail_call(shen_loop, [])][(-1)]][(-1)]][(-1)]
shen_add_fun('shen.loop', shen_loop, 0)

@tail_recursion
def kl_version(KL_ARG_V2280_1):
    global symdic
    return shen_set(symdic.symdic_kl_x42versionx42, KL_ARG_V2280_1)
shen_add_fun('version', kl_version, 1)
tail_call(kl_version, ['version 12'])

@tail_recursion
def shen_credits():
    global symdic
    return [tco_apply(shen_prhush, ['\r\nShen 2010, copyright (C) 2010 Mark Tarver\r\n', tco_apply(kl_stoutput, [])]), [tco_apply(shen_prhush, ['released under the Shen license\r\n', tco_apply(kl_stoutput, [])]), [tco_apply(shen_prhush, [('www.shenlanguage.org, ' + tco_apply(shen_app, [shen_get(symdic.symdic_kl_x42versionx42), '\r\n', symdic.symdic_shen_a])), tco_apply(kl_stoutput, [])]), [tco_apply(shen_prhush, [('running under ' + tco_apply(shen_app, [shen_get(symdic.symdic_kl_x42languagex42), (', implementation: ' + tco_apply(shen_app, [shen_get(symdic.symdic_kl_x42implementationx42), '', symdic.symdic_shen_a])), symdic.symdic_shen_a])), tco_apply(kl_stoutput, [])]), tail_call(shen_prhush, [('\r\nport ' + tco_apply(shen_app, [shen_get(symdic.symdic_kl_x42portx42), (' ported by ' + tco_apply(shen_app, [shen_get(symdic.symdic_kl_x42portersx42), '\r\n', symdic.symdic_shen_a])), symdic.symdic_shen_a])), tco_apply(kl_stoutput, [])])][(-1)]][(-1)]][(-1)]][(-1)]
shen_add_fun('shen.credits', shen_credits, 0)

@tail_recursion
def shen_initialise_environment():
    global symdic
    return tail_call(shen_multiplex45set, [[symdic.symdic_shen_x42callx42, [0, [symdic.symdic_shen_x42infsx42, [0, [symdic.symdic_shen_x42processx45counterx42, [0, [symdic.symdic_shen_x42catchx42, [0, []]]]]]]]]])
shen_add_fun('shen.initialise_environment', shen_initialise_environment, 0)

@tail_recursion
def shen_multiplex45set(KL_ARG_V2281_2):
    global symdic
    return ([] if ([] == KL_ARG_V2281_2) else ([shen_set(KL_ARG_V2281_2[0], KL_ARG_V2281_2[1][0]), tail_call(shen_multiplex45set, [KL_ARG_V2281_2[1][1]])][(-1)] if (shen_consp(KL_ARG_V2281_2[1]) if shen_consp(KL_ARG_V2281_2) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_multiplex45set]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.multiple-set', shen_multiplex45set, 1)

@tail_recursion
def kl_destroy(KL_ARG_V2282_3):
    global symdic
    return apply(kl_declare, [KL_ARG_V2282_3, []])
shen_add_fun('destroy', kl_destroy, 1)
shen_set(symdic.symdic_shen_x42historyx42, [])

@tail_recursion
def shen_readx45evaluatex45print():

    class KL_Context:
        KL_LOC_Lineread_4 = None
        KL_LOC_History_5 = None
        KL_LOC_NewLineread_6 = None
        KL_LOC_NewHistory_7 = None
        KL_LOC_Parsed_8 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Lineread_4', tco_apply(shen_toplineread, [])), [setattr(KL_CTX, 'KL_LOC_History_5', shen_get(symdic.symdic_shen_x42historyx42)), [setattr(KL_CTX, 'KL_LOC_NewLineread_6', tco_apply(shen_retrievex45fromx45historyx45ifx45needed, [KL_CTX.KL_LOC_Lineread_4, KL_CTX.KL_LOC_History_5])), [setattr(KL_CTX, 'KL_LOC_NewHistory_7', tco_apply(shen_update_history, [KL_CTX.KL_LOC_NewLineread_6, KL_CTX.KL_LOC_History_5])), [setattr(KL_CTX, 'KL_LOC_Parsed_8', tco_apply(kl_fst, [KL_CTX.KL_LOC_NewLineread_6])), tail_call(shen_toplevel, [KL_CTX.KL_LOC_Parsed_8])][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]
shen_add_fun('shen.read-evaluate-print', shen_readx45evaluatex45print, 0)

@tail_recursion
def shen_retrievex45fromx45historyx45ifx45needed(KL_ARG_V2292_9, KL_ARG_V2293_10):

    class KL_Context:
        KL_LOC_PastPrint_11 = None
        KL_LOC_Keyx63_12 = None
        KL_LOC_Find_13 = None
        KL_LOC_PastPrint_14 = None
        KL_LOC_Keyx63_16 = None
        KL_LOC_Pastprint_17 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_PastPrint_11', tco_apply(shen_prbytes, [tco_apply(kl_snd, [KL_ARG_V2293_10[0]])])), KL_ARG_V2293_10[0]][(-1)] if (((((((tco_apply(kl_snd, [KL_ARG_V2292_9])[1][0] == tco_apply(shen_exclamation, [])) if (tco_apply(kl_snd, [KL_ARG_V2292_9])[0] == tco_apply(shen_exclamation, [])) else False) if shen_consp(KL_ARG_V2293_10) else False) if ([] == tco_apply(kl_snd, [KL_ARG_V2292_9])[1][1]) else False) if shen_consp(tco_apply(kl_snd, [KL_ARG_V2292_9])[1]) else False) if shen_consp(tco_apply(kl_snd, [KL_ARG_V2292_9])) else False) if tco_apply(kl_tuplex63, [KL_ARG_V2292_9]) else False) else ([setattr(KL_CTX, 'KL_LOC_Keyx63_12', tco_apply(shen_makex45key, [tco_apply(kl_snd, [KL_ARG_V2292_9])[1], KL_ARG_V2293_10])), [setattr(KL_CTX, 'KL_LOC_Find_13', tco_apply(kl_head, [tco_apply(shen_findx45pastx45inputs, [KL_CTX.KL_LOC_Keyx63_12, KL_ARG_V2293_10])])), [setattr(KL_CTX, 'KL_LOC_PastPrint_14', tco_apply(shen_prbytes, [tco_apply(kl_snd, [KL_CTX.KL_LOC_Find_13])])), KL_CTX.KL_LOC_Find_13][(-1)]][(-1)]][(-1)] if (((tco_apply(kl_snd, [KL_ARG_V2292_9])[0] == tco_apply(shen_exclamation, [])) if shen_consp(tco_apply(kl_snd, [KL_ARG_V2292_9])) else False) if tco_apply(kl_tuplex63, [KL_ARG_V2292_9]) else False) else ([tco_apply(shen_printx45pastx45inputs, [(lambda KL_ARG_X_15: True), tco_apply(kl_reverse, [KL_ARG_V2293_10]), 0]), tail_call(kl_abort, [])][(-1)] if ((((tco_apply(kl_snd, [KL_ARG_V2292_9])[0] == tco_apply(shen_percent, [])) if ([] == tco_apply(kl_snd, [KL_ARG_V2292_9])[1]) else False) if shen_consp(tco_apply(kl_snd, [KL_ARG_V2292_9])) else False) if tco_apply(kl_tuplex63, [KL_ARG_V2292_9]) else False) else ([setattr(KL_CTX, 'KL_LOC_Keyx63_16', tco_apply(shen_makex45key, [tco_apply(kl_snd, [KL_ARG_V2292_9])[1], KL_ARG_V2293_10])), [setattr(KL_CTX, 'KL_LOC_Pastprint_17', tco_apply(shen_printx45pastx45inputs, [KL_CTX.KL_LOC_Keyx63_16, tco_apply(kl_reverse, [KL_ARG_V2293_10]), 0])), tail_call(kl_abort, [])][(-1)]][(-1)] if (((tco_apply(kl_snd, [KL_ARG_V2292_9])[0] == tco_apply(shen_percent, [])) if shen_consp(tco_apply(kl_snd, [KL_ARG_V2292_9])) else False) if tco_apply(kl_tuplex63, [KL_ARG_V2292_9]) else False) else (KL_ARG_V2292_9 if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.retrieve-from-history-if-needed', shen_retrievex45fromx45historyx45ifx45needed, 2)

@tail_recursion
def shen_percent():
    global symdic
    return 37
shen_add_fun('shen.percent', shen_percent, 0)

@tail_recursion
def shen_exclamation():
    global symdic
    return 33
shen_add_fun('shen.exclamation', shen_exclamation, 0)

@tail_recursion
def shen_prbytes(KL_ARG_V2294_18):
    global symdic
    return [tco_apply(kl_map, [(lambda KL_ARG_Byte_19: shen_pr(chr(KL_ARG_Byte_19), tco_apply(kl_stoutput, []))), KL_ARG_V2294_18]), tail_call(kl_nl, [1])][(-1)]
shen_add_fun('shen.prbytes', shen_prbytes, 1)

@tail_recursion
def shen_update_history(KL_ARG_V2295_20, KL_ARG_V2296_21):
    global symdic
    return shen_set(symdic.symdic_shen_x42historyx42, [KL_ARG_V2295_20, KL_ARG_V2296_21])
shen_add_fun('shen.update_history', shen_update_history, 2)

@tail_recursion
def shen_toplineread():
    global symdic
    return tail_call(shen_toplineread_loop, [shen_read_byte(tco_apply(kl_stinput, [])), []])
shen_add_fun('shen.toplineread', shen_toplineread, 0)

@tail_recursion
def shen_toplineread_loop(KL_ARG_V2298_22, KL_ARG_V2299_23):

    class KL_Context:
        KL_LOC_Line_24 = None
    KL_CTX = KL_Context()
    global symdic
    return (shen_simple_error('line read aborted') if (KL_ARG_V2298_22 == tco_apply(shen_hat, [])) else ([setattr(KL_CTX, 'KL_LOC_Line_24', tco_apply(kl_compile, [symdic.symdic_shen_x60st_inputx62, KL_ARG_V2299_23, (lambda KL_ARG_E_25: symdic.symdic_shen_nextline)])), (tail_call(shen_toplineread_loop, [shen_read_byte(tco_apply(kl_stinput, [])), tco_apply(kl_append, [KL_ARG_V2299_23, [KL_ARG_V2298_22, []]])]) if (True if (KL_CTX.KL_LOC_Line_24 == symdic.symdic_shen_nextline) else tco_apply(kl_emptyx63, [KL_CTX.KL_LOC_Line_24])) else tail_call(kl_x64p, [KL_CTX.KL_LOC_Line_24, KL_ARG_V2299_23]))][(-1)] if tco_apply(kl_elementx63, [KL_ARG_V2298_22, [tco_apply(shen_newline, []), [tco_apply(shen_carriagex45return, []), []]]]) else (tail_call(shen_toplineread_loop, [shen_read_byte(tco_apply(kl_stinput, [])), tco_apply(kl_append, [KL_ARG_V2299_23, [KL_ARG_V2298_22, []]])]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.toplineread_loop', shen_toplineread_loop, 2)

@tail_recursion
def shen_hat():
    global symdic
    return 94
shen_add_fun('shen.hat', shen_hat, 0)

@tail_recursion
def shen_newline():
    global symdic
    return 10
shen_add_fun('shen.newline', shen_newline, 0)

@tail_recursion
def shen_carriagex45return():
    global symdic
    return 13
shen_add_fun('shen.carriage-return', shen_carriagex45return, 0)

@tail_recursion
def kl_tc(KL_ARG_V2304_26):
    global symdic
    return (shen_set(symdic.symdic_shen_x42tcx42, True) if (symdic.symdic_kl_x43 == KL_ARG_V2304_26) else (shen_set(symdic.symdic_shen_x42tcx42, False) if (symdic.symdic_kl_x45 == KL_ARG_V2304_26) else (shen_simple_error('tc expects a + or -') if True else shen_simple_error('condition failure'))))
shen_add_fun('tc', kl_tc, 1)

@tail_recursion
def shen_prompt():
    global symdic
    return (tail_call(shen_prhush, [('\r\n\r\n(' + tco_apply(shen_app, [tco_apply(kl_length, [shen_get(symdic.symdic_shen_x42historyx42)]), '+) ', symdic.symdic_shen_a])), tco_apply(kl_stoutput, [])]) if shen_get(symdic.symdic_shen_x42tcx42) else tail_call(shen_prhush, [('\r\n\r\n(' + tco_apply(shen_app, [tco_apply(kl_length, [shen_get(symdic.symdic_shen_x42historyx42)]), '-) ', symdic.symdic_shen_a])), tco_apply(kl_stoutput, [])]))
shen_add_fun('shen.prompt', shen_prompt, 0)

@tail_recursion
def shen_toplevel(KL_ARG_V2305_27):
    global symdic
    return tail_call(shen_toplevel_evaluate, [KL_ARG_V2305_27, shen_get(symdic.symdic_shen_x42tcx42)])
shen_add_fun('shen.toplevel', shen_toplevel, 1)

@tail_recursion
def shen_findx45pastx45inputs(KL_ARG_V2306_28, KL_ARG_V2307_29):

    class KL_Context:
        KL_LOC_F_30 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_F_30', tco_apply(shen_find, [KL_ARG_V2306_28, KL_ARG_V2307_29])), (shen_simple_error('input not found\r\n') if tco_apply(kl_emptyx63, [KL_CTX.KL_LOC_F_30]) else KL_CTX.KL_LOC_F_30)][(-1)]
shen_add_fun('shen.find-past-inputs', shen_findx45pastx45inputs, 2)

@tail_recursion
def shen_makex45key(KL_ARG_V2308_31, KL_ARG_V2309_32):

    class KL_Context:
        KL_LOC_Atom_33 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Atom_33', tco_apply(kl_compile, [symdic.symdic_shen_x60st_inputx62, KL_ARG_V2308_31, (lambda KL_ARG_E_34: (shen_simple_error(('parse error here: ' + tco_apply(shen_app, [KL_ARG_E_34, '\r\n', symdic.symdic_shen_s]))) if shen_consp(KL_ARG_E_34) else shen_simple_error('parse error\r\n')))])[0]), ((lambda KL_ARG_X_35: (KL_ARG_X_35 == tco_apply(kl_nth, [(KL_CTX.KL_LOC_Atom_33 + 1), tco_apply(kl_reverse, [KL_ARG_V2309_32])]))) if tco_apply(kl_integerx63, [KL_CTX.KL_LOC_Atom_33]) else (lambda KL_ARG_X_36: tail_call(shen_prefixx63, [KL_ARG_V2308_31, tco_apply(shen_trimx45gubbins, [tco_apply(kl_snd, [KL_ARG_X_36])])])))][(-1)]
shen_add_fun('shen.make-key', shen_makex45key, 2)

@tail_recursion
def shen_trimx45gubbins(KL_ARG_V2310_37):
    global symdic
    return (tail_call(shen_trimx45gubbins, [KL_ARG_V2310_37[1]]) if ((KL_ARG_V2310_37[0] == tco_apply(shen_space, [])) if shen_consp(KL_ARG_V2310_37) else False) else (tail_call(shen_trimx45gubbins, [KL_ARG_V2310_37[1]]) if ((KL_ARG_V2310_37[0] == tco_apply(shen_newline, [])) if shen_consp(KL_ARG_V2310_37) else False) else (tail_call(shen_trimx45gubbins, [KL_ARG_V2310_37[1]]) if ((KL_ARG_V2310_37[0] == tco_apply(shen_carriagex45return, [])) if shen_consp(KL_ARG_V2310_37) else False) else (tail_call(shen_trimx45gubbins, [KL_ARG_V2310_37[1]]) if ((KL_ARG_V2310_37[0] == tco_apply(shen_tab, [])) if shen_consp(KL_ARG_V2310_37) else False) else (tail_call(shen_trimx45gubbins, [KL_ARG_V2310_37[1]]) if ((KL_ARG_V2310_37[0] == tco_apply(shen_leftx45round, [])) if shen_consp(KL_ARG_V2310_37) else False) else (KL_ARG_V2310_37 if True else shen_simple_error('condition failure')))))))
shen_add_fun('shen.trim-gubbins', shen_trimx45gubbins, 1)

@tail_recursion
def shen_space():
    global symdic
    return 32
shen_add_fun('shen.space', shen_space, 0)

@tail_recursion
def shen_tab():
    global symdic
    return 9
shen_add_fun('shen.tab', shen_tab, 0)

@tail_recursion
def shen_leftx45round():
    global symdic
    return 40
shen_add_fun('shen.left-round', shen_leftx45round, 0)

@tail_recursion
def shen_find(KL_ARG_V2317_38, KL_ARG_V2318_39):
    global symdic
    return ([] if ([] == KL_ARG_V2318_39) else ([KL_ARG_V2318_39[0], tco_apply(shen_find, [KL_ARG_V2317_38, KL_ARG_V2318_39[1]])] if (shen_apply(KL_ARG_V2317_38, [KL_ARG_V2318_39[0]]) if shen_consp(KL_ARG_V2318_39) else False) else (tail_call(shen_find, [KL_ARG_V2317_38, KL_ARG_V2318_39[1]]) if shen_consp(KL_ARG_V2318_39) else (tail_call(shen_sysx45error, [symdic.symdic_shen_find]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.find', shen_find, 2)

@tail_recursion
def shen_prefixx63(KL_ARG_V2329_40, KL_ARG_V2330_41):
    global symdic
    return (True if ([] == KL_ARG_V2329_40) else (tail_call(shen_prefixx63, [KL_ARG_V2329_40[1], KL_ARG_V2330_41[1]]) if (((KL_ARG_V2330_41[0] == KL_ARG_V2329_40[0]) if shen_consp(KL_ARG_V2330_41) else False) if shen_consp(KL_ARG_V2329_40) else False) else (False if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.prefix?', shen_prefixx63, 2)

@tail_recursion
def shen_printx45pastx45inputs(KL_ARG_V2340_42, KL_ARG_V2341_43, KL_ARG_V2342_44):
    global symdic
    return (symdic.symdic_kl__ if ([] == KL_ARG_V2341_43) else (tail_call(shen_printx45pastx45inputs, [KL_ARG_V2340_42, KL_ARG_V2341_43[1], (KL_ARG_V2342_44 + 1)]) if ((not shen_apply(KL_ARG_V2340_42, [KL_ARG_V2341_43[0]])) if shen_consp(KL_ARG_V2341_43) else False) else ([tco_apply(shen_prhush, [tco_apply(shen_app, [KL_ARG_V2342_44, '. ', symdic.symdic_shen_a]), tco_apply(kl_stoutput, [])]), [tco_apply(shen_prbytes, [tco_apply(kl_snd, [KL_ARG_V2341_43[0]])]), tail_call(shen_printx45pastx45inputs, [KL_ARG_V2340_42, KL_ARG_V2341_43[1], (KL_ARG_V2342_44 + 1)])][(-1)]][(-1)] if (tco_apply(kl_tuplex63, [KL_ARG_V2341_43[0]]) if shen_consp(KL_ARG_V2341_43) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_printx45pastx45inputs]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.print-past-inputs', shen_printx45pastx45inputs, 3)

@tail_recursion
def shen_toplevel_evaluate(KL_ARG_V2343_45, KL_ARG_V2344_46):

    class KL_Context:
        KL_LOC_Eval_47 = None
    KL_CTX = KL_Context()
    global symdic
    return (tail_call(shen_typecheckx45andx45evaluate, [KL_ARG_V2343_45[0], KL_ARG_V2343_45[1][1][0]]) if ((((((True == KL_ARG_V2344_46) if ([] == KL_ARG_V2343_45[1][1][1]) else False) if shen_consp(KL_ARG_V2343_45[1][1]) else False) if (symdic.symdic_kl_x58 == KL_ARG_V2343_45[1][0]) else False) if shen_consp(KL_ARG_V2343_45[1]) else False) if shen_consp(KL_ARG_V2343_45) else False) else ([tco_apply(shen_toplevel_evaluate, [[KL_ARG_V2343_45[0], []], KL_ARG_V2344_46]), [tco_apply(kl_nl, [1]), tail_call(shen_toplevel_evaluate, [KL_ARG_V2343_45[1], KL_ARG_V2344_46])][(-1)]][(-1)] if (shen_consp(KL_ARG_V2343_45[1]) if shen_consp(KL_ARG_V2343_45) else False) else (tail_call(shen_typecheckx45andx45evaluate, [KL_ARG_V2343_45[0], tco_apply(kl_gensym, [symdic.symdic_A])]) if (((True == KL_ARG_V2344_46) if ([] == KL_ARG_V2343_45[1]) else False) if shen_consp(KL_ARG_V2343_45) else False) else ([setattr(KL_CTX, 'KL_LOC_Eval_47', tco_apply(shen_evalx45withoutx45macros, [KL_ARG_V2343_45[0]])), tail_call(kl_print, [KL_CTX.KL_LOC_Eval_47])][(-1)] if (((False == KL_ARG_V2344_46) if ([] == KL_ARG_V2343_45[1]) else False) if shen_consp(KL_ARG_V2343_45) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_toplevel_evaluate]) if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.toplevel_evaluate', shen_toplevel_evaluate, 2)

@tail_recursion
def shen_typecheckx45andx45evaluate(KL_ARG_V2345_48, KL_ARG_V2346_49):

    class KL_Context:
        KL_LOC_Typecheck_50 = None
        KL_LOC_Eval_51 = None
        KL_LOC_Type_52 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Typecheck_50', tco_apply(shen_typecheck, [KL_ARG_V2345_48, KL_ARG_V2346_49])), (shen_simple_error('type error\r\n') if (KL_CTX.KL_LOC_Typecheck_50 == False) else [setattr(KL_CTX, 'KL_LOC_Eval_51', tco_apply(shen_evalx45withoutx45macros, [KL_ARG_V2345_48])), [setattr(KL_CTX, 'KL_LOC_Type_52', tco_apply(shen_prettyx45type, [KL_CTX.KL_LOC_Typecheck_50])), tail_call(shen_prhush, [tco_apply(shen_app, [KL_CTX.KL_LOC_Eval_51, (' : ' + tco_apply(shen_app, [KL_CTX.KL_LOC_Type_52, '', symdic.symdic_shen_r])), symdic.symdic_shen_s]), tco_apply(kl_stoutput, [])])][(-1)]][(-1)])][(-1)]
shen_add_fun('shen.typecheck-and-evaluate', shen_typecheckx45andx45evaluate, 2)

@tail_recursion
def shen_prettyx45type(KL_ARG_V2347_53):
    global symdic
    return tail_call(shen_mult_subst, [shen_get(symdic.symdic_shen_x42alphabetx42), tco_apply(shen_extractx45pvars, [KL_ARG_V2347_53]), KL_ARG_V2347_53])
shen_add_fun('shen.pretty-type', shen_prettyx45type, 1)

@tail_recursion
def shen_extractx45pvars(KL_ARG_V2352_54):
    global symdic
    return ([KL_ARG_V2352_54, []] if tco_apply(shen_pvarx63, [KL_ARG_V2352_54]) else (tail_call(kl_union, [tco_apply(shen_extractx45pvars, [KL_ARG_V2352_54[0]]), tco_apply(shen_extractx45pvars, [KL_ARG_V2352_54[1]])]) if shen_consp(KL_ARG_V2352_54) else ([] if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.extract-pvars', shen_extractx45pvars, 1)

@tail_recursion
def shen_mult_subst(KL_ARG_V2357_55, KL_ARG_V2358_56, KL_ARG_V2359_57):
    global symdic
    return (KL_ARG_V2359_57 if ([] == KL_ARG_V2357_55) else (KL_ARG_V2359_57 if ([] == KL_ARG_V2358_56) else (tail_call(shen_mult_subst, [KL_ARG_V2357_55[1], KL_ARG_V2358_56[1], tco_apply(kl_subst, [KL_ARG_V2357_55[0], KL_ARG_V2358_56[0], KL_ARG_V2359_57])]) if (shen_consp(KL_ARG_V2358_56) if shen_consp(KL_ARG_V2357_55) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_mult_subst]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.mult_subst', shen_mult_subst, 3)


#============================== core.kl==============================



@tail_recursion
def shen_shenx45x62kl(KL_ARG_V607_58, KL_ARG_V608_59):
    global symdic
    return tail_call(kl_compile, [symdic.symdic_shen_x60definex62, [KL_ARG_V607_58, KL_ARG_V608_59], (lambda KL_ARG_X_60: tail_call(shen_shenx45syntaxx45error, [KL_ARG_V607_58, KL_ARG_X_60]))])
shen_add_fun('shen.shen->kl', shen_shenx45x62kl, 2)

@tail_recursion
def shen_shenx45syntaxx45error(KL_ARG_V609_61, KL_ARG_V610_62):
    global symdic
    return shen_simple_error(('syntax error in ' + tco_apply(shen_app, [KL_ARG_V609_61, (' here:\r\n\r\n ' + tco_apply(shen_app, [tco_apply(shen_nextx4550, [50, KL_ARG_V610_62]), '\r\n', symdic.symdic_shen_a])), symdic.symdic_shen_a])))
shen_add_fun('shen.shen-syntax-error', shen_shenx45syntaxx45error, 2)

@tail_recursion
def shen_x60definex62(KL_ARG_V615_63):

    class KL_Context:
        KL_LOC_Result_64 = None
        KL_LOC_Parse_shen_x60namex62_65 = None
        KL_LOC_Parse_shen_x60signaturex62_66 = None
        KL_LOC_Parse_shen_x60rulesx62_67 = None
        KL_LOC_Result_68 = None
        KL_LOC_Parse_shen_x60namex62_69 = None
        KL_LOC_Parse_shen_x60rulesx62_70 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_64', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60namex62_65', tco_apply(shen_x60namex62, [KL_ARG_V615_63])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60signaturex62_66', tco_apply(shen_x60signaturex62, [KL_CTX.KL_LOC_Parse_shen_x60namex62_65])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60rulesx62_67', tco_apply(shen_x60rulesx62, [KL_CTX.KL_LOC_Parse_shen_x60signaturex62_66])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60rulesx62_67[0], tco_apply(shen_compile_to_machine_code, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60namex62_65]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60rulesx62_67])])]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60rulesx62_67)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60signaturex62_66)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60namex62_65)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_68', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60namex62_69', tco_apply(shen_x60namex62, [KL_ARG_V615_63])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60rulesx62_70', tco_apply(shen_x60rulesx62, [KL_CTX.KL_LOC_Parse_shen_x60namex62_69])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60rulesx62_70[0], tco_apply(shen_compile_to_machine_code, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60namex62_69]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60rulesx62_70])])]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60rulesx62_70)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60namex62_69)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_68 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_68)][(-1)] if (KL_CTX.KL_LOC_Result_64 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_64)][(-1)]
shen_add_fun('shen.<define>', shen_x60definex62, 1)

@tail_recursion
def shen_x60namex62(KL_ARG_V620_71):

    class KL_Context:
        KL_LOC_Result_72 = None
        KL_LOC_Parse_X_73 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_72', ([setattr(KL_CTX, 'KL_LOC_Parse_X_73', KL_ARG_V620_71[0][0]), tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V620_71[0][1], tco_apply(shen_hdtl, [KL_ARG_V620_71])])[0], (KL_CTX.KL_LOC_Parse_X_73 if ((not tco_apply(shen_sysfuncx63, [KL_CTX.KL_LOC_Parse_X_73])) if tco_apply(kl_symbolx63, [KL_CTX.KL_LOC_Parse_X_73]) else False) else shen_simple_error(tco_apply(shen_app, [KL_CTX.KL_LOC_Parse_X_73, ' is not a legitimate function name.\r\n', symdic.symdic_shen_a])))])][(-1)] if shen_consp(KL_ARG_V620_71[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_72 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_72)][(-1)]
shen_add_fun('shen.<name>', shen_x60namex62, 1)

@tail_recursion
def shen_sysfuncx63(KL_ARG_V621_74):
    global symdic
    return tail_call(kl_elementx63, [KL_ARG_V621_74, tco_apply(kl_get, [shen_intern('shen'), symdic.symdic_shen_externalx45symbols, shen_get(symdic.symdic_kl_x42propertyx45vectorx42)])])
shen_add_fun('shen.sysfunc?', shen_sysfuncx63, 1)

@tail_recursion
def shen_x60signaturex62(KL_ARG_V626_75):

    class KL_Context:
        KL_LOC_Result_76 = None
        KL_LOC_Parse_shen_x60signaturex45helpx62_77 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_76', ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60signaturex45helpx62_77', tco_apply(shen_x60signaturex45helpx62, [tco_apply(shen_pair, [KL_ARG_V626_75[0][1], tco_apply(shen_hdtl, [KL_ARG_V626_75])])])), ((tco_apply(shen_pair, [tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60signaturex45helpx62_77[0][1], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60signaturex45helpx62_77])])[0], tco_apply(shen_demodulate, [tco_apply(shen_curryx45type, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60signaturex45helpx62_77])])])]) if ((symdic.symdic_kl_x125 == KL_CTX.KL_LOC_Parse_shen_x60signaturex45helpx62_77[0][0]) if shen_consp(KL_CTX.KL_LOC_Parse_shen_x60signaturex45helpx62_77[0]) else False) else tco_apply(kl_fail, [])) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60signaturex45helpx62_77)) else tco_apply(kl_fail, []))][(-1)] if ((symdic.symdic_kl_x123 == KL_ARG_V626_75[0][0]) if shen_consp(KL_ARG_V626_75[0]) else False) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_76 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_76)][(-1)]
shen_add_fun('shen.<signature>', shen_x60signaturex62, 1)

@tail_recursion
def shen_curryx45type(KL_ARG_V629_78):
    global symdic
    return (tail_call(shen_curryx45type, [[KL_ARG_V629_78[0], [symdic.symdic_kl_x45x45x62, [KL_ARG_V629_78[1][1], []]]]]) if ((((((symdic.symdic_kl_x45x45x62 == KL_ARG_V629_78[1][1][1][0]) if shen_consp(KL_ARG_V629_78[1][1][1]) else False) if shen_consp(KL_ARG_V629_78[1][1]) else False) if (symdic.symdic_kl_x45x45x62 == KL_ARG_V629_78[1][0]) else False) if shen_consp(KL_ARG_V629_78[1]) else False) if shen_consp(KL_ARG_V629_78) else False) else ([symdic.symdic_kl_list, [tco_apply(shen_curryx45type, [KL_ARG_V629_78[1][0]]), []]] if ((((([] == KL_ARG_V629_78[1][1][1]) if shen_consp(KL_ARG_V629_78[1][1]) else False) if shen_consp(KL_ARG_V629_78[1]) else False) if (symdic.symdic_kl_cons == KL_ARG_V629_78[0]) else False) if shen_consp(KL_ARG_V629_78) else False) else (tail_call(shen_curryx45type, [[KL_ARG_V629_78[0], [symdic.symdic_kl_x42, [KL_ARG_V629_78[1][1], []]]]]) if ((((((symdic.symdic_kl_x42 == KL_ARG_V629_78[1][1][1][0]) if shen_consp(KL_ARG_V629_78[1][1][1]) else False) if shen_consp(KL_ARG_V629_78[1][1]) else False) if (symdic.symdic_kl_x42 == KL_ARG_V629_78[1][0]) else False) if shen_consp(KL_ARG_V629_78[1]) else False) if shen_consp(KL_ARG_V629_78) else False) else (tail_call(kl_map, [symdic.symdic_shen_curryx45type, KL_ARG_V629_78]) if shen_consp(KL_ARG_V629_78) else (KL_ARG_V629_78 if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.curry-type', shen_curryx45type, 1)

@tail_recursion
def shen_x60signaturex45helpx62(KL_ARG_V634_79):

    class KL_Context:
        KL_LOC_Result_80 = None
        KL_LOC_Parse_X_81 = None
        KL_LOC_Parse_shen_x60signaturex45helpx62_82 = None
        KL_LOC_Result_83 = None
        KL_LOC_Parse_x60ex62_84 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_80', ([setattr(KL_CTX, 'KL_LOC_Parse_X_81', KL_ARG_V634_79[0][0]), [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60signaturex45helpx62_82', tco_apply(shen_x60signaturex45helpx62, [tco_apply(shen_pair, [KL_ARG_V634_79[0][1], tco_apply(shen_hdtl, [KL_ARG_V634_79])])])), ((tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60signaturex45helpx62_82[0], [KL_CTX.KL_LOC_Parse_X_81, tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60signaturex45helpx62_82])]]) if (not tco_apply(kl_elementx63, [KL_CTX.KL_LOC_Parse_X_81, [symdic.symdic_kl_x123, [symdic.symdic_kl_x125, []]]])) else tco_apply(kl_fail, [])) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60signaturex45helpx62_82)) else tco_apply(kl_fail, []))][(-1)]][(-1)] if shen_consp(KL_ARG_V634_79[0]) else tco_apply(kl_fail, []))), ([setattr(KL_CTX, 'KL_LOC_Result_83', [setattr(KL_CTX, 'KL_LOC_Parse_x60ex62_84', tco_apply(kl_x60ex62, [KL_ARG_V634_79])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_x60ex62_84[0], []]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_x60ex62_84)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_83 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_83)][(-1)] if (KL_CTX.KL_LOC_Result_80 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_80)][(-1)]
shen_add_fun('shen.<signature-help>', shen_x60signaturex45helpx62, 1)

@tail_recursion
def shen_x60rulesx62(KL_ARG_V639_85):

    class KL_Context:
        KL_LOC_Result_86 = None
        KL_LOC_Parse_shen_x60rulex62_87 = None
        KL_LOC_Parse_shen_x60rulesx62_88 = None
        KL_LOC_Result_89 = None
        KL_LOC_Parse_shen_x60rulex62_90 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_86', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60rulex62_87', tco_apply(shen_x60rulex62, [KL_ARG_V639_85])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60rulesx62_88', tco_apply(shen_x60rulesx62, [KL_CTX.KL_LOC_Parse_shen_x60rulex62_87])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60rulesx62_88[0], [tco_apply(shen_linearise, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60rulex62_87])]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60rulesx62_88])]]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60rulesx62_88)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60rulex62_87)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_89', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60rulex62_90', tco_apply(shen_x60rulex62, [KL_ARG_V639_85])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60rulex62_90[0], [tco_apply(shen_linearise, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60rulex62_90])]), []]]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60rulex62_90)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_89 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_89)][(-1)] if (KL_CTX.KL_LOC_Result_86 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_86)][(-1)]
shen_add_fun('shen.<rules>', shen_x60rulesx62, 1)

@tail_recursion
def shen_x60rulex62(KL_ARG_V644_91):

    class KL_Context:
        KL_LOC_Result_92 = None
        KL_LOC_Parse_shen_x60patternsx62_93 = None
        KL_LOC_Parse_shen_x60actionx62_94 = None
        KL_LOC_Parse_shen_x60guardx62_95 = None
        KL_LOC_Result_96 = None
        KL_LOC_Parse_shen_x60patternsx62_97 = None
        KL_LOC_Parse_shen_x60actionx62_98 = None
        KL_LOC_Result_99 = None
        KL_LOC_Parse_shen_x60patternsx62_100 = None
        KL_LOC_Parse_shen_x60actionx62_101 = None
        KL_LOC_Parse_shen_x60guardx62_102 = None
        KL_LOC_Result_103 = None
        KL_LOC_Parse_shen_x60patternsx62_104 = None
        KL_LOC_Parse_shen_x60actionx62_105 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_92', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60patternsx62_93', tco_apply(shen_x60patternsx62, [KL_ARG_V644_91])), (([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60actionx62_94', tco_apply(shen_x60actionx62, [tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_93[0][1], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_93])])])), (([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60guardx62_95', tco_apply(shen_x60guardx62, [tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60actionx62_94[0][1], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60actionx62_94])])])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60guardx62_95[0], [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_93]), [[symdic.symdic_kl_where, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60guardx62_95]), [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60actionx62_94]), []]]], []]]]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60guardx62_95)) else tco_apply(kl_fail, []))][(-1)] if ((symdic.symdic_kl_where == KL_CTX.KL_LOC_Parse_shen_x60actionx62_94[0][0]) if shen_consp(KL_CTX.KL_LOC_Parse_shen_x60actionx62_94[0]) else False) else tco_apply(kl_fail, [])) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60actionx62_94)) else tco_apply(kl_fail, []))][(-1)] if ((symdic.symdic_kl_x45x62 == KL_CTX.KL_LOC_Parse_shen_x60patternsx62_93[0][0]) if shen_consp(KL_CTX.KL_LOC_Parse_shen_x60patternsx62_93[0]) else False) else tco_apply(kl_fail, [])) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60patternsx62_93)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_96', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60patternsx62_97', tco_apply(shen_x60patternsx62, [KL_ARG_V644_91])), (([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60actionx62_98', tco_apply(shen_x60actionx62, [tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_97[0][1], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_97])])])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60actionx62_98[0], [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_97]), [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60actionx62_98]), []]]]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60actionx62_98)) else tco_apply(kl_fail, []))][(-1)] if ((symdic.symdic_kl_x45x62 == KL_CTX.KL_LOC_Parse_shen_x60patternsx62_97[0][0]) if shen_consp(KL_CTX.KL_LOC_Parse_shen_x60patternsx62_97[0]) else False) else tco_apply(kl_fail, [])) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60patternsx62_97)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_99', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60patternsx62_100', tco_apply(shen_x60patternsx62, [KL_ARG_V644_91])), (([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60actionx62_101', tco_apply(shen_x60actionx62, [tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_100[0][1], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_100])])])), (([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60guardx62_102', tco_apply(shen_x60guardx62, [tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60actionx62_101[0][1], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60actionx62_101])])])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60guardx62_102[0], [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_100]), [[symdic.symdic_kl_where, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60guardx62_102]), [[symdic.symdic_shen_choicepointx33, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60actionx62_101]), []]], []]]], []]]]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60guardx62_102)) else tco_apply(kl_fail, []))][(-1)] if ((symdic.symdic_kl_where == KL_CTX.KL_LOC_Parse_shen_x60actionx62_101[0][0]) if shen_consp(KL_CTX.KL_LOC_Parse_shen_x60actionx62_101[0]) else False) else tco_apply(kl_fail, [])) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60actionx62_101)) else tco_apply(kl_fail, []))][(-1)] if ((symdic.symdic_kl_x60x45 == KL_CTX.KL_LOC_Parse_shen_x60patternsx62_100[0][0]) if shen_consp(KL_CTX.KL_LOC_Parse_shen_x60patternsx62_100[0]) else False) else tco_apply(kl_fail, [])) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60patternsx62_100)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_103', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60patternsx62_104', tco_apply(shen_x60patternsx62, [KL_ARG_V644_91])), (([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60actionx62_105', tco_apply(shen_x60actionx62, [tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_104[0][1], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_104])])])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60actionx62_105[0], [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_104]), [[symdic.symdic_shen_choicepointx33, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60actionx62_105]), []]], []]]]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60actionx62_105)) else tco_apply(kl_fail, []))][(-1)] if ((symdic.symdic_kl_x60x45 == KL_CTX.KL_LOC_Parse_shen_x60patternsx62_104[0][0]) if shen_consp(KL_CTX.KL_LOC_Parse_shen_x60patternsx62_104[0]) else False) else tco_apply(kl_fail, [])) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60patternsx62_104)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_103 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_103)][(-1)] if (KL_CTX.KL_LOC_Result_99 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_99)][(-1)] if (KL_CTX.KL_LOC_Result_96 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_96)][(-1)] if (KL_CTX.KL_LOC_Result_92 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_92)][(-1)]
shen_add_fun('shen.<rule>', shen_x60rulex62, 1)

@tail_recursion
def shen_fail_if(KL_ARG_V645_106, KL_ARG_V646_107):
    global symdic
    return (tail_call(kl_fail, []) if shen_apply(KL_ARG_V645_106, [KL_ARG_V646_107]) else KL_ARG_V646_107)
shen_add_fun('shen.fail_if', shen_fail_if, 2)

@tail_recursion
def shen_succeedsx63(KL_ARG_V651_108):
    global symdic
    return (False if (KL_ARG_V651_108 == tco_apply(kl_fail, [])) else (True if True else shen_simple_error('condition failure')))
shen_add_fun('shen.succeeds?', shen_succeedsx63, 1)

@tail_recursion
def shen_x60patternsx62(KL_ARG_V656_109):

    class KL_Context:
        KL_LOC_Result_110 = None
        KL_LOC_Parse_shen_x60patternx62_111 = None
        KL_LOC_Parse_shen_x60patternsx62_112 = None
        KL_LOC_Result_113 = None
        KL_LOC_Parse_x60ex62_114 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_110', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60patternx62_111', tco_apply(shen_x60patternx62, [KL_ARG_V656_109])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60patternsx62_112', tco_apply(shen_x60patternsx62, [KL_CTX.KL_LOC_Parse_shen_x60patternx62_111])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_112[0], [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternx62_111]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_112])]]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60patternsx62_112)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60patternx62_111)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_113', [setattr(KL_CTX, 'KL_LOC_Parse_x60ex62_114', tco_apply(kl_x60ex62, [KL_ARG_V656_109])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_x60ex62_114[0], []]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_x60ex62_114)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_113 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_113)][(-1)] if (KL_CTX.KL_LOC_Result_110 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_110)][(-1)]
shen_add_fun('shen.<patterns>', shen_x60patternsx62, 1)

@tail_recursion
def shen_x60patternx62(KL_ARG_V661_115):

    class KL_Context:
        KL_LOC_Result_116 = None
        KL_LOC_Parse_shen_x60pattern1x62_117 = None
        KL_LOC_Parse_shen_x60pattern2x62_118 = None
        KL_LOC_Result_119 = None
        KL_LOC_Parse_shen_x60pattern1x62_120 = None
        KL_LOC_Parse_shen_x60pattern2x62_121 = None
        KL_LOC_Result_122 = None
        KL_LOC_Parse_shen_x60pattern1x62_123 = None
        KL_LOC_Parse_shen_x60pattern2x62_124 = None
        KL_LOC_Result_125 = None
        KL_LOC_Parse_shen_x60pattern1x62_126 = None
        KL_LOC_Parse_shen_x60pattern2x62_127 = None
        KL_LOC_Result_128 = None
        KL_LOC_Result_129 = None
        KL_LOC_Parse_X_130 = None
        KL_LOC_Result_131 = None
        KL_LOC_Parse_shen_x60simple_patternx62_132 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_116', (tco_apply(shen_sndx45orx45fail, [([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60pattern1x62_117', tco_apply(shen_x60pattern1x62, [tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V661_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V661_115])])[0][1], tco_apply(shen_hdtl, [tco_apply(shen_pair, [KL_ARG_V661_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V661_115])])])])])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60pattern2x62_118', tco_apply(shen_x60pattern2x62, [KL_CTX.KL_LOC_Parse_shen_x60pattern1x62_117])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60pattern2x62_118[0], tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V661_115[0][1], tco_apply(shen_hdtl, [KL_ARG_V661_115])])[0], [symdic.symdic_kl_x64p, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60pattern1x62_117]), [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60pattern2x62_118]), []]]]])]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60pattern2x62_118)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60pattern1x62_117)) else tco_apply(kl_fail, []))][(-1)] if ((symdic.symdic_kl_x64p == tco_apply(shen_pair, [KL_ARG_V661_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V661_115])])[0][0]) if shen_consp(tco_apply(shen_pair, [KL_ARG_V661_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V661_115])])[0]) else False) else tco_apply(kl_fail, []))]) if (shen_consp(KL_ARG_V661_115[0][0]) if shen_consp(KL_ARG_V661_115[0]) else False) else tco_apply(kl_fail, []))), ([setattr(KL_CTX, 'KL_LOC_Result_119', (tco_apply(shen_sndx45orx45fail, [([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60pattern1x62_120', tco_apply(shen_x60pattern1x62, [tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V661_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V661_115])])[0][1], tco_apply(shen_hdtl, [tco_apply(shen_pair, [KL_ARG_V661_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V661_115])])])])])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60pattern2x62_121', tco_apply(shen_x60pattern2x62, [KL_CTX.KL_LOC_Parse_shen_x60pattern1x62_120])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60pattern2x62_121[0], tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V661_115[0][1], tco_apply(shen_hdtl, [KL_ARG_V661_115])])[0], [symdic.symdic_kl_cons, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60pattern1x62_120]), [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60pattern2x62_121]), []]]]])]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60pattern2x62_121)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60pattern1x62_120)) else tco_apply(kl_fail, []))][(-1)] if ((symdic.symdic_kl_cons == tco_apply(shen_pair, [KL_ARG_V661_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V661_115])])[0][0]) if shen_consp(tco_apply(shen_pair, [KL_ARG_V661_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V661_115])])[0]) else False) else tco_apply(kl_fail, []))]) if (shen_consp(KL_ARG_V661_115[0][0]) if shen_consp(KL_ARG_V661_115[0]) else False) else tco_apply(kl_fail, []))), ([setattr(KL_CTX, 'KL_LOC_Result_122', (tco_apply(shen_sndx45orx45fail, [([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60pattern1x62_123', tco_apply(shen_x60pattern1x62, [tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V661_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V661_115])])[0][1], tco_apply(shen_hdtl, [tco_apply(shen_pair, [KL_ARG_V661_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V661_115])])])])])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60pattern2x62_124', tco_apply(shen_x60pattern2x62, [KL_CTX.KL_LOC_Parse_shen_x60pattern1x62_123])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60pattern2x62_124[0], tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V661_115[0][1], tco_apply(shen_hdtl, [KL_ARG_V661_115])])[0], [symdic.symdic_kl_x64v, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60pattern1x62_123]), [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60pattern2x62_124]), []]]]])]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60pattern2x62_124)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60pattern1x62_123)) else tco_apply(kl_fail, []))][(-1)] if ((symdic.symdic_kl_x64v == tco_apply(shen_pair, [KL_ARG_V661_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V661_115])])[0][0]) if shen_consp(tco_apply(shen_pair, [KL_ARG_V661_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V661_115])])[0]) else False) else tco_apply(kl_fail, []))]) if (shen_consp(KL_ARG_V661_115[0][0]) if shen_consp(KL_ARG_V661_115[0]) else False) else tco_apply(kl_fail, []))), ([setattr(KL_CTX, 'KL_LOC_Result_125', (tco_apply(shen_sndx45orx45fail, [([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60pattern1x62_126', tco_apply(shen_x60pattern1x62, [tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V661_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V661_115])])[0][1], tco_apply(shen_hdtl, [tco_apply(shen_pair, [KL_ARG_V661_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V661_115])])])])])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60pattern2x62_127', tco_apply(shen_x60pattern2x62, [KL_CTX.KL_LOC_Parse_shen_x60pattern1x62_126])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60pattern2x62_127[0], tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V661_115[0][1], tco_apply(shen_hdtl, [KL_ARG_V661_115])])[0], [symdic.symdic_kl_x64s, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60pattern1x62_126]), [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60pattern2x62_127]), []]]]])]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60pattern2x62_127)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60pattern1x62_126)) else tco_apply(kl_fail, []))][(-1)] if ((symdic.symdic_kl_x64s == tco_apply(shen_pair, [KL_ARG_V661_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V661_115])])[0][0]) if shen_consp(tco_apply(shen_pair, [KL_ARG_V661_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V661_115])])[0]) else False) else tco_apply(kl_fail, []))]) if (shen_consp(KL_ARG_V661_115[0][0]) if shen_consp(KL_ARG_V661_115[0]) else False) else tco_apply(kl_fail, []))), ([setattr(KL_CTX, 'KL_LOC_Result_128', (tco_apply(shen_sndx45orx45fail, [((tco_apply(shen_pair, [tco_apply(shen_pair, [tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V661_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V661_115])])[0][1], tco_apply(shen_hdtl, [tco_apply(shen_pair, [KL_ARG_V661_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V661_115])])])])[0][1], tco_apply(shen_hdtl, [tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V661_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V661_115])])[0][1], tco_apply(shen_hdtl, [tco_apply(shen_pair, [KL_ARG_V661_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V661_115])])])])])])[0], tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V661_115[0][1], tco_apply(shen_hdtl, [KL_ARG_V661_115])])[0], [symdic.symdic_kl_vector, [0, []]]])]) if ((0 == tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V661_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V661_115])])[0][1], tco_apply(shen_hdtl, [tco_apply(shen_pair, [KL_ARG_V661_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V661_115])])])])[0][0]) if shen_consp(tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V661_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V661_115])])[0][1], tco_apply(shen_hdtl, [tco_apply(shen_pair, [KL_ARG_V661_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V661_115])])])])[0]) else False) else tco_apply(kl_fail, [])) if ((symdic.symdic_kl_vector == tco_apply(shen_pair, [KL_ARG_V661_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V661_115])])[0][0]) if shen_consp(tco_apply(shen_pair, [KL_ARG_V661_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V661_115])])[0]) else False) else tco_apply(kl_fail, []))]) if (shen_consp(KL_ARG_V661_115[0][0]) if shen_consp(KL_ARG_V661_115[0]) else False) else tco_apply(kl_fail, []))), ([setattr(KL_CTX, 'KL_LOC_Result_129', ([setattr(KL_CTX, 'KL_LOC_Parse_X_130', KL_ARG_V661_115[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V661_115[0][1], tco_apply(shen_hdtl, [KL_ARG_V661_115])])[0], tco_apply(shen_constructorx45error, [KL_CTX.KL_LOC_Parse_X_130])]) if shen_consp(KL_CTX.KL_LOC_Parse_X_130) else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V661_115[0]) else tco_apply(kl_fail, []))), ([setattr(KL_CTX, 'KL_LOC_Result_131', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60simple_patternx62_132', tco_apply(shen_x60simple_patternx62, [KL_ARG_V661_115])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60simple_patternx62_132[0], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60simple_patternx62_132])]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60simple_patternx62_132)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_131 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_131)][(-1)] if (KL_CTX.KL_LOC_Result_129 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_129)][(-1)] if (KL_CTX.KL_LOC_Result_128 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_128)][(-1)] if (KL_CTX.KL_LOC_Result_125 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_125)][(-1)] if (KL_CTX.KL_LOC_Result_122 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_122)][(-1)] if (KL_CTX.KL_LOC_Result_119 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_119)][(-1)] if (KL_CTX.KL_LOC_Result_116 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_116)][(-1)]
shen_add_fun('shen.<pattern>', shen_x60patternx62, 1)

@tail_recursion
def shen_constructorx45error(KL_ARG_V662_133):
    global symdic
    return shen_simple_error(tco_apply(shen_app, [KL_ARG_V662_133, ' is not a legitimate constructor\r\n', symdic.symdic_shen_a]))
shen_add_fun('shen.constructor-error', shen_constructorx45error, 1)

@tail_recursion
def shen_x60simple_patternx62(KL_ARG_V667_134):

    class KL_Context:
        KL_LOC_Result_135 = None
        KL_LOC_Parse_X_136 = None
        KL_LOC_Result_137 = None
        KL_LOC_Parse_X_138 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_135', ([setattr(KL_CTX, 'KL_LOC_Parse_X_136', KL_ARG_V667_134[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V667_134[0][1], tco_apply(shen_hdtl, [KL_ARG_V667_134])])[0], tco_apply(kl_gensym, [symdic.symdic_Parse_Y])]) if (KL_CTX.KL_LOC_Parse_X_136 == symdic.symdic_kl__) else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V667_134[0]) else tco_apply(kl_fail, []))), ([setattr(KL_CTX, 'KL_LOC_Result_137', ([setattr(KL_CTX, 'KL_LOC_Parse_X_138', KL_ARG_V667_134[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V667_134[0][1], tco_apply(shen_hdtl, [KL_ARG_V667_134])])[0], KL_CTX.KL_LOC_Parse_X_138]) if (not tco_apply(kl_elementx63, [KL_CTX.KL_LOC_Parse_X_138, [symdic.symdic_kl_x45x62, [symdic.symdic_kl_x60x45, []]]])) else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V667_134[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_137 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_137)][(-1)] if (KL_CTX.KL_LOC_Result_135 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_135)][(-1)]
shen_add_fun('shen.<simple_pattern>', shen_x60simple_patternx62, 1)

@tail_recursion
def shen_x60pattern1x62(KL_ARG_V672_139):

    class KL_Context:
        KL_LOC_Result_140 = None
        KL_LOC_Parse_shen_x60patternx62_141 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_140', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60patternx62_141', tco_apply(shen_x60patternx62, [KL_ARG_V672_139])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60patternx62_141[0], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternx62_141])]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60patternx62_141)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_140 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_140)][(-1)]
shen_add_fun('shen.<pattern1>', shen_x60pattern1x62, 1)

@tail_recursion
def shen_x60pattern2x62(KL_ARG_V677_142):

    class KL_Context:
        KL_LOC_Result_143 = None
        KL_LOC_Parse_shen_x60patternx62_144 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_143', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60patternx62_144', tco_apply(shen_x60patternx62, [KL_ARG_V677_142])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60patternx62_144[0], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternx62_144])]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60patternx62_144)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_143 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_143)][(-1)]
shen_add_fun('shen.<pattern2>', shen_x60pattern2x62, 1)

@tail_recursion
def shen_x60actionx62(KL_ARG_V682_145):

    class KL_Context:
        KL_LOC_Result_146 = None
        KL_LOC_Parse_X_147 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_146', ([setattr(KL_CTX, 'KL_LOC_Parse_X_147', KL_ARG_V682_145[0][0]), tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V682_145[0][1], tco_apply(shen_hdtl, [KL_ARG_V682_145])])[0], KL_CTX.KL_LOC_Parse_X_147])][(-1)] if shen_consp(KL_ARG_V682_145[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_146 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_146)][(-1)]
shen_add_fun('shen.<action>', shen_x60actionx62, 1)

@tail_recursion
def shen_x60guardx62(KL_ARG_V687_148):

    class KL_Context:
        KL_LOC_Result_149 = None
        KL_LOC_Parse_X_150 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_149', ([setattr(KL_CTX, 'KL_LOC_Parse_X_150', KL_ARG_V687_148[0][0]), tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V687_148[0][1], tco_apply(shen_hdtl, [KL_ARG_V687_148])])[0], KL_CTX.KL_LOC_Parse_X_150])][(-1)] if shen_consp(KL_ARG_V687_148[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_149 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_149)][(-1)]
shen_add_fun('shen.<guard>', shen_x60guardx62, 1)

@tail_recursion
def shen_compile_to_machine_code(KL_ARG_V688_151, KL_ARG_V689_152):

    class KL_Context:
        KL_LOC_Lambdax43_153 = None
        KL_LOC_KL_154 = None
        KL_LOC_Record_155 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Lambdax43_153', tco_apply(shen_compile_to_lambdax43, [KL_ARG_V688_151, KL_ARG_V689_152])), [setattr(KL_CTX, 'KL_LOC_KL_154', tco_apply(shen_compile_to_kl, [KL_ARG_V688_151, KL_CTX.KL_LOC_Lambdax43_153])), [setattr(KL_CTX, 'KL_LOC_Record_155', tco_apply(shen_recordx45source, [KL_ARG_V688_151, KL_CTX.KL_LOC_KL_154])), KL_CTX.KL_LOC_KL_154][(-1)]][(-1)]][(-1)]
shen_add_fun('shen.compile_to_machine_code', shen_compile_to_machine_code, 2)

@tail_recursion
def shen_recordx45source(KL_ARG_V692_156, KL_ARG_V693_157):
    global symdic
    return (symdic.symdic_shen_skip if shen_get(symdic.symdic_shen_x42installingx45klx42) else (tail_call(kl_put, [KL_ARG_V692_156, symdic.symdic_shen_source, KL_ARG_V693_157, shen_get(symdic.symdic_kl_x42propertyx45vectorx42)]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.record-source', shen_recordx45source, 2)

@tail_recursion
def shen_compile_to_lambdax43(KL_ARG_V694_158, KL_ARG_V695_159):

    class KL_Context:
        KL_LOC_Arity_160 = None
        KL_LOC_Free_161 = None
        KL_LOC_Variables_163 = None
        KL_LOC_Strip_164 = None
        KL_LOC_Abstractions_165 = None
        KL_LOC_Applications_166 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Arity_160', tco_apply(shen_aritycheck, [KL_ARG_V694_158, KL_ARG_V695_159])), [setattr(KL_CTX, 'KL_LOC_Free_161', tco_apply(kl_map, [(lambda KL_ARG_Rule_162: tail_call(shen_free_variable_check, [KL_ARG_V694_158, KL_ARG_Rule_162])), KL_ARG_V695_159])), [setattr(KL_CTX, 'KL_LOC_Variables_163', tco_apply(shen_parameters, [KL_CTX.KL_LOC_Arity_160])), [setattr(KL_CTX, 'KL_LOC_Strip_164', tco_apply(kl_map, [symdic.symdic_shen_stripx45protect, KL_ARG_V695_159])), [setattr(KL_CTX, 'KL_LOC_Abstractions_165', tco_apply(kl_map, [symdic.symdic_shen_abstract_rule, KL_CTX.KL_LOC_Strip_164])), [setattr(KL_CTX, 'KL_LOC_Applications_166', tco_apply(kl_map, [(lambda KL_ARG_X_167: tail_call(shen_application_build, [KL_CTX.KL_LOC_Variables_163, KL_ARG_X_167])), KL_CTX.KL_LOC_Abstractions_165])), [KL_CTX.KL_LOC_Variables_163, [KL_CTX.KL_LOC_Applications_166, []]]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]
shen_add_fun('shen.compile_to_lambda+', shen_compile_to_lambdax43, 2)

@tail_recursion
def shen_free_variable_check(KL_ARG_V696_168, KL_ARG_V697_169):

    class KL_Context:
        KL_LOC_Bound_170 = None
        KL_LOC_Free_171 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_Bound_170', tco_apply(shen_extract_vars, [KL_ARG_V697_169[0]])), [setattr(KL_CTX, 'KL_LOC_Free_171', tco_apply(shen_extract_free_vars, [KL_CTX.KL_LOC_Bound_170, KL_ARG_V697_169[1][0]])), tail_call(shen_free_variable_warnings, [KL_ARG_V696_168, KL_CTX.KL_LOC_Free_171])][(-1)]][(-1)] if ((([] == KL_ARG_V697_169[1][1]) if shen_consp(KL_ARG_V697_169[1]) else False) if shen_consp(KL_ARG_V697_169) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_free_variable_check]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.free_variable_check', shen_free_variable_check, 2)

@tail_recursion
def shen_extract_vars(KL_ARG_V698_172):
    global symdic
    return ([KL_ARG_V698_172, []] if tco_apply(kl_variablex63, [KL_ARG_V698_172]) else (tail_call(kl_union, [tco_apply(shen_extract_vars, [KL_ARG_V698_172[0]]), tco_apply(shen_extract_vars, [KL_ARG_V698_172[1]])]) if shen_consp(KL_ARG_V698_172) else ([] if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.extract_vars', shen_extract_vars, 1)

@tail_recursion
def shen_extract_free_vars(KL_ARG_V708_173, KL_ARG_V709_174):
    global symdic
    return ([] if ((((KL_ARG_V709_174[0] == symdic.symdic_kl_protect) if ([] == KL_ARG_V709_174[1][1]) else False) if shen_consp(KL_ARG_V709_174[1]) else False) if shen_consp(KL_ARG_V709_174) else False) else ([KL_ARG_V709_174, []] if ((not tco_apply(kl_elementx63, [KL_ARG_V709_174, KL_ARG_V708_173])) if tco_apply(kl_variablex63, [KL_ARG_V709_174]) else False) else (tail_call(shen_extract_free_vars, [[KL_ARG_V709_174[1][0], KL_ARG_V708_173], KL_ARG_V709_174[1][1][0]]) if ((((([] == KL_ARG_V709_174[1][1][1]) if shen_consp(KL_ARG_V709_174[1][1]) else False) if shen_consp(KL_ARG_V709_174[1]) else False) if (symdic.symdic_kl_lambda == KL_ARG_V709_174[0]) else False) if shen_consp(KL_ARG_V709_174) else False) else (tail_call(kl_union, [tco_apply(shen_extract_free_vars, [KL_ARG_V708_173, KL_ARG_V709_174[1][1][0]]), tco_apply(shen_extract_free_vars, [[KL_ARG_V709_174[1][0], KL_ARG_V708_173], KL_ARG_V709_174[1][1][1][0]])]) if (((((([] == KL_ARG_V709_174[1][1][1][1]) if shen_consp(KL_ARG_V709_174[1][1][1]) else False) if shen_consp(KL_ARG_V709_174[1][1]) else False) if shen_consp(KL_ARG_V709_174[1]) else False) if (symdic.symdic_kl_let == KL_ARG_V709_174[0]) else False) if shen_consp(KL_ARG_V709_174) else False) else (tail_call(kl_union, [tco_apply(shen_extract_free_vars, [KL_ARG_V708_173, KL_ARG_V709_174[0]]), tco_apply(shen_extract_free_vars, [KL_ARG_V708_173, KL_ARG_V709_174[1]])]) if shen_consp(KL_ARG_V709_174) else ([] if True else shen_simple_error('condition failure')))))))
shen_add_fun('shen.extract_free_vars', shen_extract_free_vars, 2)

@tail_recursion
def shen_free_variable_warnings(KL_ARG_V712_175, KL_ARG_V713_176):
    global symdic
    return (symdic.symdic_kl__ if ([] == KL_ARG_V713_176) else (shen_simple_error(('error: the following variables are free in ' + tco_apply(shen_app, [KL_ARG_V712_175, (': ' + tco_apply(shen_app, [tco_apply(shen_list_variables, [KL_ARG_V713_176]), '', symdic.symdic_shen_a])), symdic.symdic_shen_a]))) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.free_variable_warnings', shen_free_variable_warnings, 2)

@tail_recursion
def shen_list_variables(KL_ARG_V714_177):
    global symdic
    return ((str(KL_ARG_V714_177[0]) + '.') if (([] == KL_ARG_V714_177[1]) if shen_consp(KL_ARG_V714_177) else False) else ((str(KL_ARG_V714_177[0]) + (', ' + tco_apply(shen_list_variables, [KL_ARG_V714_177[1]]))) if shen_consp(KL_ARG_V714_177) else (tail_call(shen_sysx45error, [symdic.symdic_shen_list_variables]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.list_variables', shen_list_variables, 1)

@tail_recursion
def shen_stripx45protect(KL_ARG_V715_178):
    global symdic
    return (KL_ARG_V715_178[1][0] if ((((KL_ARG_V715_178[0] == symdic.symdic_kl_protect) if ([] == KL_ARG_V715_178[1][1]) else False) if shen_consp(KL_ARG_V715_178[1]) else False) if shen_consp(KL_ARG_V715_178) else False) else ([tco_apply(shen_stripx45protect, [KL_ARG_V715_178[0]]), tco_apply(shen_stripx45protect, [KL_ARG_V715_178[1]])] if shen_consp(KL_ARG_V715_178) else (KL_ARG_V715_178 if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.strip-protect', shen_stripx45protect, 1)

@tail_recursion
def shen_linearise(KL_ARG_V716_179):
    global symdic
    return (tail_call(shen_linearise_help, [tco_apply(shen_flatten, [KL_ARG_V716_179[0]]), KL_ARG_V716_179[0], KL_ARG_V716_179[1][0]]) if ((([] == KL_ARG_V716_179[1][1]) if shen_consp(KL_ARG_V716_179[1]) else False) if shen_consp(KL_ARG_V716_179) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_linearise]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.linearise', shen_linearise, 1)

@tail_recursion
def shen_flatten(KL_ARG_V717_180):
    global symdic
    return ([] if ([] == KL_ARG_V717_180) else (tail_call(kl_append, [tco_apply(shen_flatten, [KL_ARG_V717_180[0]]), tco_apply(shen_flatten, [KL_ARG_V717_180[1]])]) if shen_consp(KL_ARG_V717_180) else ([KL_ARG_V717_180, []] if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.flatten', shen_flatten, 1)

@tail_recursion
def shen_linearise_help(KL_ARG_V718_181, KL_ARG_V719_182, KL_ARG_V720_183):

    class KL_Context:
        KL_LOC_Var_184 = None
        KL_LOC_NewAction_185 = None
        KL_LOC_NewPatts_186 = None
    KL_CTX = KL_Context()
    global symdic
    return ([KL_ARG_V719_182, [KL_ARG_V720_183, []]] if ([] == KL_ARG_V718_181) else (([setattr(KL_CTX, 'KL_LOC_Var_184', tco_apply(kl_gensym, [KL_ARG_V718_181[0]])), [setattr(KL_CTX, 'KL_LOC_NewAction_185', [symdic.symdic_kl_where, [[symdic.symdic_kl_x61, [KL_ARG_V718_181[0], [KL_CTX.KL_LOC_Var_184, []]]], [KL_ARG_V720_183, []]]]), [setattr(KL_CTX, 'KL_LOC_NewPatts_186', tco_apply(shen_linearise_X, [KL_ARG_V718_181[0], KL_CTX.KL_LOC_Var_184, KL_ARG_V719_182])), tail_call(shen_linearise_help, [KL_ARG_V718_181[1], KL_CTX.KL_LOC_NewPatts_186, KL_CTX.KL_LOC_NewAction_185])][(-1)]][(-1)]][(-1)] if (tco_apply(kl_elementx63, [KL_ARG_V718_181[0], KL_ARG_V718_181[1]]) if tco_apply(kl_variablex63, [KL_ARG_V718_181[0]]) else False) else tail_call(shen_linearise_help, [KL_ARG_V718_181[1], KL_ARG_V719_182, KL_ARG_V720_183])) if shen_consp(KL_ARG_V718_181) else (tail_call(shen_sysx45error, [symdic.symdic_shen_linearise_help]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.linearise_help', shen_linearise_help, 3)

@tail_recursion
def shen_linearise_X(KL_ARG_V729_187, KL_ARG_V730_188, KL_ARG_V731_189):

    class KL_Context:
        KL_LOC_L_190 = None
    KL_CTX = KL_Context()
    global symdic
    return (KL_ARG_V730_188 if (KL_ARG_V731_189 == KL_ARG_V729_187) else ([setattr(KL_CTX, 'KL_LOC_L_190', tco_apply(shen_linearise_X, [KL_ARG_V729_187, KL_ARG_V730_188, KL_ARG_V731_189[0]])), ([KL_ARG_V731_189[0], tco_apply(shen_linearise_X, [KL_ARG_V729_187, KL_ARG_V730_188, KL_ARG_V731_189[1]])] if (KL_CTX.KL_LOC_L_190 == KL_ARG_V731_189[0]) else [KL_CTX.KL_LOC_L_190, KL_ARG_V731_189[1]])][(-1)] if shen_consp(KL_ARG_V731_189) else (KL_ARG_V731_189 if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.linearise_X', shen_linearise_X, 3)

@tail_recursion
def shen_aritycheck(KL_ARG_V733_191, KL_ARG_V734_192):
    global symdic
    return ([tco_apply(shen_aritycheckx45action, [KL_ARG_V734_192[0][1][0]]), tail_call(shen_aritycheckx45name, [KL_ARG_V733_191, tco_apply(kl_arity, [KL_ARG_V733_191]), tco_apply(kl_length, [KL_ARG_V734_192[0][0]])])][(-1)] if ((((([] == KL_ARG_V734_192[1]) if ([] == KL_ARG_V734_192[0][1][1]) else False) if shen_consp(KL_ARG_V734_192[0][1]) else False) if shen_consp(KL_ARG_V734_192[0]) else False) if shen_consp(KL_ARG_V734_192) else False) else (([tco_apply(shen_aritycheckx45action, [KL_ARG_V734_192[0][1][0]]), tail_call(shen_aritycheck, [KL_ARG_V733_191, KL_ARG_V734_192[1]])][(-1)] if (tco_apply(kl_length, [KL_ARG_V734_192[0][0]]) == tco_apply(kl_length, [KL_ARG_V734_192[1][0][0]])) else shen_simple_error(('arity error in ' + tco_apply(shen_app, [KL_ARG_V733_191, '\r\n', symdic.symdic_shen_a])))) if (((((((([] == KL_ARG_V734_192[1][0][1][1]) if shen_consp(KL_ARG_V734_192[1][0][1]) else False) if shen_consp(KL_ARG_V734_192[1][0]) else False) if shen_consp(KL_ARG_V734_192[1]) else False) if ([] == KL_ARG_V734_192[0][1][1]) else False) if shen_consp(KL_ARG_V734_192[0][1]) else False) if shen_consp(KL_ARG_V734_192[0]) else False) if shen_consp(KL_ARG_V734_192) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_aritycheck]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.aritycheck', shen_aritycheck, 2)

@tail_recursion
def shen_aritycheckx45name(KL_ARG_V743_193, KL_ARG_V744_194, KL_ARG_V745_195):
    global symdic
    return (KL_ARG_V745_195 if ((-1) == KL_ARG_V744_194) else (KL_ARG_V745_195 if (KL_ARG_V745_195 == KL_ARG_V744_194) else ([tco_apply(shen_prhush, [('\r\nwarning: changing the arity of ' + tco_apply(shen_app, [KL_ARG_V743_193, ' can cause errors.\r\n', symdic.symdic_shen_a])), tco_apply(kl_stoutput, [])]), KL_ARG_V745_195][(-1)] if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.aritycheck-name', shen_aritycheckx45name, 3)

@tail_recursion
def shen_aritycheckx45action(KL_ARG_V751_196):
    global symdic
    return ([tco_apply(shen_aah, [KL_ARG_V751_196[0], KL_ARG_V751_196[1]]), tail_call(kl_map, [symdic.symdic_shen_aritycheckx45action, KL_ARG_V751_196])][(-1)] if shen_consp(KL_ARG_V751_196) else (symdic.symdic_shen_skip if True else shen_simple_error('condition failure')))
shen_add_fun('shen.aritycheck-action', shen_aritycheckx45action, 1)

@tail_recursion
def shen_aah(KL_ARG_V752_197, KL_ARG_V753_198):

    class KL_Context:
        KL_LOC_Arity_199 = None
        KL_LOC_Len_200 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Arity_199', tco_apply(kl_arity, [KL_ARG_V752_197])), [setattr(KL_CTX, 'KL_LOC_Len_200', tco_apply(kl_length, [KL_ARG_V753_198])), (tail_call(shen_prhush, [('warning: ' + tco_apply(shen_app, [KL_ARG_V752_197, (' might not like ' + tco_apply(shen_app, [KL_CTX.KL_LOC_Len_200, (' argument' + tco_apply(shen_app, [('s' if (KL_CTX.KL_LOC_Len_200 > 1) else ''), '.\r\n', symdic.symdic_shen_a])), symdic.symdic_shen_a])), symdic.symdic_shen_a])), tco_apply(kl_stoutput, [])]) if ((KL_CTX.KL_LOC_Len_200 > KL_CTX.KL_LOC_Arity_199) if (KL_CTX.KL_LOC_Arity_199 > (-1)) else False) else symdic.symdic_shen_skip)][(-1)]][(-1)]
shen_add_fun('shen.aah', shen_aah, 2)

@tail_recursion
def shen_abstract_rule(KL_ARG_V754_201):
    global symdic
    return (tail_call(shen_abstraction_build, [KL_ARG_V754_201[0], KL_ARG_V754_201[1][0]]) if ((([] == KL_ARG_V754_201[1][1]) if shen_consp(KL_ARG_V754_201[1]) else False) if shen_consp(KL_ARG_V754_201) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_abstract_rule]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.abstract_rule', shen_abstract_rule, 1)

@tail_recursion
def shen_abstraction_build(KL_ARG_V755_202, KL_ARG_V756_203):
    global symdic
    return (KL_ARG_V756_203 if ([] == KL_ARG_V755_202) else ([symdic.symdic_kl_x47_, [KL_ARG_V755_202[0], [tco_apply(shen_abstraction_build, [KL_ARG_V755_202[1], KL_ARG_V756_203]), []]]] if shen_consp(KL_ARG_V755_202) else (tail_call(shen_sysx45error, [symdic.symdic_shen_abstraction_build]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.abstraction_build', shen_abstraction_build, 2)

@tail_recursion
def shen_parameters(KL_ARG_V757_204):
    global symdic
    return ([] if (0 == KL_ARG_V757_204) else ([tco_apply(kl_gensym, [symdic.symdic_V]), tco_apply(shen_parameters, [(KL_ARG_V757_204 - 1)])] if True else shen_simple_error('condition failure')))
shen_add_fun('shen.parameters', shen_parameters, 1)

@tail_recursion
def shen_application_build(KL_ARG_V758_205, KL_ARG_V759_206):
    global symdic
    return (KL_ARG_V759_206 if ([] == KL_ARG_V758_205) else (tail_call(shen_application_build, [KL_ARG_V758_205[1], [KL_ARG_V759_206, [KL_ARG_V758_205[0], []]]]) if shen_consp(KL_ARG_V758_205) else (tail_call(shen_sysx45error, [symdic.symdic_shen_application_build]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.application_build', shen_application_build, 2)

@tail_recursion
def shen_compile_to_kl(KL_ARG_V760_207, KL_ARG_V761_208):

    class KL_Context:
        KL_LOC_Arity_209 = None
        KL_LOC_Reduce_210 = None
        KL_LOC_CondExpression_211 = None
        KL_LOC_TypeTable_212 = None
        KL_LOC_TypedCondExpression_213 = None
        KL_LOC_KL_214 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_Arity_209', tco_apply(shen_storex45arity, [KL_ARG_V760_207, tco_apply(kl_length, [KL_ARG_V761_208[0]])])), [setattr(KL_CTX, 'KL_LOC_Reduce_210', tco_apply(kl_map, [symdic.symdic_shen_reduce, KL_ARG_V761_208[1][0]])), [setattr(KL_CTX, 'KL_LOC_CondExpression_211', tco_apply(shen_condx45expression, [KL_ARG_V760_207, KL_ARG_V761_208[0], KL_CTX.KL_LOC_Reduce_210])), [setattr(KL_CTX, 'KL_LOC_TypeTable_212', (tco_apply(shen_typextable, [tco_apply(shen_getx45type, [KL_ARG_V760_207]), KL_ARG_V761_208[0]]) if shen_get(symdic.symdic_shen_x42optimisex42) else symdic.symdic_shen_skip)), [setattr(KL_CTX, 'KL_LOC_TypedCondExpression_213', (tco_apply(shen_assignx45types, [KL_ARG_V761_208[0], KL_CTX.KL_LOC_TypeTable_212, KL_CTX.KL_LOC_CondExpression_211]) if shen_get(symdic.symdic_shen_x42optimisex42) else KL_CTX.KL_LOC_CondExpression_211)), [setattr(KL_CTX, 'KL_LOC_KL_214', [symdic.symdic_kl_defun, [KL_ARG_V760_207, [KL_ARG_V761_208[0], [KL_CTX.KL_LOC_TypedCondExpression_213, []]]]]), KL_CTX.KL_LOC_KL_214][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)] if ((([] == KL_ARG_V761_208[1][1]) if shen_consp(KL_ARG_V761_208[1]) else False) if shen_consp(KL_ARG_V761_208) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_compile_to_kl]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.compile_to_kl', shen_compile_to_kl, 2)

@tail_recursion
def shen_getx45type(KL_ARG_V766_215):

    class KL_Context:
        KL_LOC_FType_216 = None
    KL_CTX = KL_Context()
    global symdic
    return (symdic.symdic_shen_skip if shen_consp(KL_ARG_V766_215) else ([setattr(KL_CTX, 'KL_LOC_FType_216', tco_apply(kl_assoc, [KL_ARG_V766_215, shen_get(symdic.symdic_shen_x42signedfuncsx42)])), (symdic.symdic_shen_skip if tco_apply(kl_emptyx63, [KL_CTX.KL_LOC_FType_216]) else KL_CTX.KL_LOC_FType_216[1])][(-1)] if True else shen_simple_error('condition failure')))
shen_add_fun('shen.get-type', shen_getx45type, 1)

@tail_recursion
def shen_typextable(KL_ARG_V775_217, KL_ARG_V776_218):
    global symdic
    return ((tail_call(shen_typextable, [KL_ARG_V775_217[1][1][0], KL_ARG_V776_218[1]]) if tco_apply(kl_variablex63, [KL_ARG_V775_217[0]]) else [[KL_ARG_V776_218[0], KL_ARG_V775_217[0]], tco_apply(shen_typextable, [KL_ARG_V775_217[1][1][0], KL_ARG_V776_218[1]])]) if (((((shen_consp(KL_ARG_V776_218) if ([] == KL_ARG_V775_217[1][1][1]) else False) if shen_consp(KL_ARG_V775_217[1][1]) else False) if (symdic.symdic_kl_x45x45x62 == KL_ARG_V775_217[1][0]) else False) if shen_consp(KL_ARG_V775_217[1]) else False) if shen_consp(KL_ARG_V775_217) else False) else ([] if True else shen_simple_error('condition failure')))
shen_add_fun('shen.typextable', shen_typextable, 2)

@tail_recursion
def shen_assignx45types(KL_ARG_V777_219, KL_ARG_V778_220, KL_ARG_V779_221):

    class KL_Context:
        KL_LOC_NewTable_223 = None
        KL_LOC_AtomType_225 = None
    KL_CTX = KL_Context()
    global symdic
    return ([symdic.symdic_kl_let, [KL_ARG_V779_221[1][0], [tco_apply(shen_assignx45types, [KL_ARG_V777_219, KL_ARG_V778_220, KL_ARG_V779_221[1][1][0]]), [tco_apply(shen_assignx45types, [[KL_ARG_V779_221[1][0], KL_ARG_V777_219], KL_ARG_V778_220, KL_ARG_V779_221[1][1][1][0]]), []]]]] if (((((([] == KL_ARG_V779_221[1][1][1][1]) if shen_consp(KL_ARG_V779_221[1][1][1]) else False) if shen_consp(KL_ARG_V779_221[1][1]) else False) if shen_consp(KL_ARG_V779_221[1]) else False) if (symdic.symdic_kl_let == KL_ARG_V779_221[0]) else False) if shen_consp(KL_ARG_V779_221) else False) else ([symdic.symdic_kl_lambda, [KL_ARG_V779_221[1][0], [tco_apply(shen_assignx45types, [[KL_ARG_V779_221[1][0], KL_ARG_V777_219], KL_ARG_V778_220, KL_ARG_V779_221[1][1][0]]), []]]] if ((((([] == KL_ARG_V779_221[1][1][1]) if shen_consp(KL_ARG_V779_221[1][1]) else False) if shen_consp(KL_ARG_V779_221[1]) else False) if (symdic.symdic_kl_lambda == KL_ARG_V779_221[0]) else False) if shen_consp(KL_ARG_V779_221) else False) else ([symdic.symdic_kl_cond, tco_apply(kl_map, [(lambda KL_ARG_Y_222: [tco_apply(shen_assignx45types, [KL_ARG_V777_219, KL_ARG_V778_220, KL_ARG_Y_222[0]]), [tco_apply(shen_assignx45types, [KL_ARG_V777_219, KL_ARG_V778_220, KL_ARG_Y_222[1][0]]), []]]), KL_ARG_V779_221[1]])] if ((symdic.symdic_kl_cond == KL_ARG_V779_221[0]) if shen_consp(KL_ARG_V779_221) else False) else ([setattr(KL_CTX, 'KL_LOC_NewTable_223', tco_apply(shen_typextable, [tco_apply(shen_getx45type, [KL_ARG_V779_221[0]]), KL_ARG_V779_221[1]])), [KL_ARG_V779_221[0], tco_apply(kl_map, [(lambda KL_ARG_Y_224: tail_call(shen_assignx45types, [KL_ARG_V777_219, tco_apply(kl_append, [KL_ARG_V778_220, KL_CTX.KL_LOC_NewTable_223]), KL_ARG_Y_224])), KL_ARG_V779_221[1]])]][(-1)] if shen_consp(KL_ARG_V779_221) else ([setattr(KL_CTX, 'KL_LOC_AtomType_225', tco_apply(kl_assoc, [KL_ARG_V779_221, KL_ARG_V778_220])), ([symdic.symdic_kl_type, [KL_ARG_V779_221, [KL_CTX.KL_LOC_AtomType_225[1], []]]] if shen_consp(KL_CTX.KL_LOC_AtomType_225) else (KL_ARG_V779_221 if tco_apply(kl_elementx63, [KL_ARG_V779_221, KL_ARG_V777_219]) else tail_call(shen_atomx45type, [KL_ARG_V779_221])))][(-1)] if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.assign-types', shen_assignx45types, 3)

@tail_recursion
def shen_atomx45type(KL_ARG_V780_226):
    global symdic
    return ([symdic.symdic_kl_type, [KL_ARG_V780_226, [symdic.symdic_kl_string, []]]] if isinstance(KL_ARG_V780_226, str) else ([symdic.symdic_kl_type, [KL_ARG_V780_226, [symdic.symdic_kl_number, []]]] if isinstance(KL_ARG_V780_226, numbers.Number) else ([symdic.symdic_kl_type, [KL_ARG_V780_226, [symdic.symdic_kl_boolean, []]]] if tco_apply(kl_booleanx63, [KL_ARG_V780_226]) else ([symdic.symdic_kl_type, [KL_ARG_V780_226, [symdic.symdic_kl_symbol, []]]] if tco_apply(kl_symbolx63, [KL_ARG_V780_226]) else KL_ARG_V780_226))))
shen_add_fun('shen.atom-type', shen_atomx45type, 1)

@tail_recursion
def shen_storex45arity(KL_ARG_V783_227, KL_ARG_V784_228):
    global symdic
    return (symdic.symdic_shen_skip if shen_get(symdic.symdic_shen_x42installingx45klx42) else (tail_call(kl_put, [KL_ARG_V783_227, symdic.symdic_kl_arity, KL_ARG_V784_228, shen_get(symdic.symdic_kl_x42propertyx45vectorx42)]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.store-arity', shen_storex45arity, 2)

@tail_recursion
def shen_reduce(KL_ARG_V785_229):

    class KL_Context:
        KL_LOC_Result_230 = None
    KL_CTX = KL_Context()
    global symdic
    return [shen_set(symdic.symdic_shen_x42teststackx42, []), [setattr(KL_CTX, 'KL_LOC_Result_230', tco_apply(shen_reduce_help, [KL_ARG_V785_229])), [[symdic.symdic_kl_x58, [symdic.symdic_shen_tests, tco_apply(kl_reverse, [shen_get(symdic.symdic_shen_x42teststackx42)])]], [KL_CTX.KL_LOC_Result_230, []]]][(-1)]][(-1)]
shen_add_fun('shen.reduce', shen_reduce, 1)

@tail_recursion
def shen_reduce_help(KL_ARG_V786_231):

    class KL_Context:
        KL_LOC_Abstraction_232 = None
        KL_LOC_Application_233 = None
        KL_LOC_Abstraction_234 = None
        KL_LOC_Application_235 = None
        KL_LOC_Abstraction_236 = None
        KL_LOC_Application_237 = None
        KL_LOC_Abstraction_238 = None
        KL_LOC_Application_239 = None
        KL_LOC_Z_240 = None
    KL_CTX = KL_Context()
    global symdic
    return ([tco_apply(shen_add_test, [[symdic.symdic_kl_consx63, KL_ARG_V786_231[1]]]), [setattr(KL_CTX, 'KL_LOC_Abstraction_232', [symdic.symdic_kl_x47_, [KL_ARG_V786_231[0][1][0][1][0], [[symdic.symdic_kl_x47_, [KL_ARG_V786_231[0][1][0][1][1][0], [tco_apply(shen_ebr, [KL_ARG_V786_231[1][0], KL_ARG_V786_231[0][1][0], KL_ARG_V786_231[0][1][1][0]]), []]]], []]]]), [setattr(KL_CTX, 'KL_LOC_Application_233', [[KL_CTX.KL_LOC_Abstraction_232, [[symdic.symdic_kl_hd, KL_ARG_V786_231[1]], []]], [[symdic.symdic_kl_tl, KL_ARG_V786_231[1]], []]]), tail_call(shen_reduce_help, [KL_CTX.KL_LOC_Application_233])][(-1)]][(-1)]][(-1)] if ((((((((((((([] == KL_ARG_V786_231[1][1]) if shen_consp(KL_ARG_V786_231[1]) else False) if ([] == KL_ARG_V786_231[0][1][1][1]) else False) if shen_consp(KL_ARG_V786_231[0][1][1]) else False) if ([] == KL_ARG_V786_231[0][1][0][1][1][1]) else False) if shen_consp(KL_ARG_V786_231[0][1][0][1][1]) else False) if shen_consp(KL_ARG_V786_231[0][1][0][1]) else False) if (symdic.symdic_kl_cons == KL_ARG_V786_231[0][1][0][0]) else False) if shen_consp(KL_ARG_V786_231[0][1][0]) else False) if shen_consp(KL_ARG_V786_231[0][1]) else False) if (symdic.symdic_kl_x47_ == KL_ARG_V786_231[0][0]) else False) if shen_consp(KL_ARG_V786_231[0]) else False) if shen_consp(KL_ARG_V786_231) else False) else ([tco_apply(shen_add_test, [[symdic.symdic_kl_tuplex63, KL_ARG_V786_231[1]]]), [setattr(KL_CTX, 'KL_LOC_Abstraction_234', [symdic.symdic_kl_x47_, [KL_ARG_V786_231[0][1][0][1][0], [[symdic.symdic_kl_x47_, [KL_ARG_V786_231[0][1][0][1][1][0], [tco_apply(shen_ebr, [KL_ARG_V786_231[1][0], KL_ARG_V786_231[0][1][0], KL_ARG_V786_231[0][1][1][0]]), []]]], []]]]), [setattr(KL_CTX, 'KL_LOC_Application_235', [[KL_CTX.KL_LOC_Abstraction_234, [[symdic.symdic_kl_fst, KL_ARG_V786_231[1]], []]], [[symdic.symdic_kl_snd, KL_ARG_V786_231[1]], []]]), tail_call(shen_reduce_help, [KL_CTX.KL_LOC_Application_235])][(-1)]][(-1)]][(-1)] if ((((((((((((([] == KL_ARG_V786_231[1][1]) if shen_consp(KL_ARG_V786_231[1]) else False) if ([] == KL_ARG_V786_231[0][1][1][1]) else False) if shen_consp(KL_ARG_V786_231[0][1][1]) else False) if ([] == KL_ARG_V786_231[0][1][0][1][1][1]) else False) if shen_consp(KL_ARG_V786_231[0][1][0][1][1]) else False) if shen_consp(KL_ARG_V786_231[0][1][0][1]) else False) if (symdic.symdic_kl_x64p == KL_ARG_V786_231[0][1][0][0]) else False) if shen_consp(KL_ARG_V786_231[0][1][0]) else False) if shen_consp(KL_ARG_V786_231[0][1]) else False) if (symdic.symdic_kl_x47_ == KL_ARG_V786_231[0][0]) else False) if shen_consp(KL_ARG_V786_231[0]) else False) if shen_consp(KL_ARG_V786_231) else False) else ([tco_apply(shen_add_test, [[symdic.symdic_shen_x43vectorx63, KL_ARG_V786_231[1]]]), [setattr(KL_CTX, 'KL_LOC_Abstraction_236', [symdic.symdic_kl_x47_, [KL_ARG_V786_231[0][1][0][1][0], [[symdic.symdic_kl_x47_, [KL_ARG_V786_231[0][1][0][1][1][0], [tco_apply(shen_ebr, [KL_ARG_V786_231[1][0], KL_ARG_V786_231[0][1][0], KL_ARG_V786_231[0][1][1][0]]), []]]], []]]]), [setattr(KL_CTX, 'KL_LOC_Application_237', [[KL_CTX.KL_LOC_Abstraction_236, [[symdic.symdic_kl_hdv, KL_ARG_V786_231[1]], []]], [[symdic.symdic_kl_tlv, KL_ARG_V786_231[1]], []]]), tail_call(shen_reduce_help, [KL_CTX.KL_LOC_Application_237])][(-1)]][(-1)]][(-1)] if ((((((((((((([] == KL_ARG_V786_231[1][1]) if shen_consp(KL_ARG_V786_231[1]) else False) if ([] == KL_ARG_V786_231[0][1][1][1]) else False) if shen_consp(KL_ARG_V786_231[0][1][1]) else False) if ([] == KL_ARG_V786_231[0][1][0][1][1][1]) else False) if shen_consp(KL_ARG_V786_231[0][1][0][1][1]) else False) if shen_consp(KL_ARG_V786_231[0][1][0][1]) else False) if (symdic.symdic_kl_x64v == KL_ARG_V786_231[0][1][0][0]) else False) if shen_consp(KL_ARG_V786_231[0][1][0]) else False) if shen_consp(KL_ARG_V786_231[0][1]) else False) if (symdic.symdic_kl_x47_ == KL_ARG_V786_231[0][0]) else False) if shen_consp(KL_ARG_V786_231[0]) else False) if shen_consp(KL_ARG_V786_231) else False) else ([tco_apply(shen_add_test, [[symdic.symdic_shen_x43stringx63, KL_ARG_V786_231[1]]]), [setattr(KL_CTX, 'KL_LOC_Abstraction_238', [symdic.symdic_kl_x47_, [KL_ARG_V786_231[0][1][0][1][0], [[symdic.symdic_kl_x47_, [KL_ARG_V786_231[0][1][0][1][1][0], [tco_apply(shen_ebr, [KL_ARG_V786_231[1][0], KL_ARG_V786_231[0][1][0], KL_ARG_V786_231[0][1][1][0]]), []]]], []]]]), [setattr(KL_CTX, 'KL_LOC_Application_239', [[KL_CTX.KL_LOC_Abstraction_238, [[symdic.symdic_kl_pos, [KL_ARG_V786_231[1][0], [0, []]]], []]], [[symdic.symdic_kl_tlstr, KL_ARG_V786_231[1]], []]]), tail_call(shen_reduce_help, [KL_CTX.KL_LOC_Application_239])][(-1)]][(-1)]][(-1)] if ((((((((((((([] == KL_ARG_V786_231[1][1]) if shen_consp(KL_ARG_V786_231[1]) else False) if ([] == KL_ARG_V786_231[0][1][1][1]) else False) if shen_consp(KL_ARG_V786_231[0][1][1]) else False) if ([] == KL_ARG_V786_231[0][1][0][1][1][1]) else False) if shen_consp(KL_ARG_V786_231[0][1][0][1][1]) else False) if shen_consp(KL_ARG_V786_231[0][1][0][1]) else False) if (symdic.symdic_kl_x64s == KL_ARG_V786_231[0][1][0][0]) else False) if shen_consp(KL_ARG_V786_231[0][1][0]) else False) if shen_consp(KL_ARG_V786_231[0][1]) else False) if (symdic.symdic_kl_x47_ == KL_ARG_V786_231[0][0]) else False) if shen_consp(KL_ARG_V786_231[0]) else False) if shen_consp(KL_ARG_V786_231) else False) else ([tco_apply(shen_add_test, [[symdic.symdic_kl_x61, [KL_ARG_V786_231[0][1][0], KL_ARG_V786_231[1]]]]), tail_call(shen_reduce_help, [KL_ARG_V786_231[0][1][1][0]])][(-1)] if (((((((((not tco_apply(kl_variablex63, [KL_ARG_V786_231[0][1][0]])) if ([] == KL_ARG_V786_231[1][1]) else False) if shen_consp(KL_ARG_V786_231[1]) else False) if ([] == KL_ARG_V786_231[0][1][1][1]) else False) if shen_consp(KL_ARG_V786_231[0][1][1]) else False) if shen_consp(KL_ARG_V786_231[0][1]) else False) if (symdic.symdic_kl_x47_ == KL_ARG_V786_231[0][0]) else False) if shen_consp(KL_ARG_V786_231[0]) else False) if shen_consp(KL_ARG_V786_231) else False) else (tail_call(shen_reduce_help, [tco_apply(shen_ebr, [KL_ARG_V786_231[1][0], KL_ARG_V786_231[0][1][0], KL_ARG_V786_231[0][1][1][0]])]) if (((((((([] == KL_ARG_V786_231[1][1]) if shen_consp(KL_ARG_V786_231[1]) else False) if ([] == KL_ARG_V786_231[0][1][1][1]) else False) if shen_consp(KL_ARG_V786_231[0][1][1]) else False) if shen_consp(KL_ARG_V786_231[0][1]) else False) if (symdic.symdic_kl_x47_ == KL_ARG_V786_231[0][0]) else False) if shen_consp(KL_ARG_V786_231[0]) else False) if shen_consp(KL_ARG_V786_231) else False) else ([tco_apply(shen_add_test, [KL_ARG_V786_231[1][0]]), tail_call(shen_reduce_help, [KL_ARG_V786_231[1][1][0]])][(-1)] if ((((([] == KL_ARG_V786_231[1][1][1]) if shen_consp(KL_ARG_V786_231[1][1]) else False) if shen_consp(KL_ARG_V786_231[1]) else False) if (symdic.symdic_kl_where == KL_ARG_V786_231[0]) else False) if shen_consp(KL_ARG_V786_231) else False) else ([setattr(KL_CTX, 'KL_LOC_Z_240', tco_apply(shen_reduce_help, [KL_ARG_V786_231[0]])), (KL_ARG_V786_231 if (KL_ARG_V786_231[0] == KL_CTX.KL_LOC_Z_240) else tail_call(shen_reduce_help, [[KL_CTX.KL_LOC_Z_240, KL_ARG_V786_231[1]]]))][(-1)] if ((([] == KL_ARG_V786_231[1][1]) if shen_consp(KL_ARG_V786_231[1]) else False) if shen_consp(KL_ARG_V786_231) else False) else (KL_ARG_V786_231 if True else shen_simple_error('condition failure'))))))))))
shen_add_fun('shen.reduce_help', shen_reduce_help, 1)

@tail_recursion
def shen_x43stringx63(KL_ARG_V787_241):
    global symdic
    return (False if ('' == KL_ARG_V787_241) else (isinstance(KL_ARG_V787_241, str) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.+string?', shen_x43stringx63, 1)

@tail_recursion
def shen_x43vector(KL_ARG_V788_242):
    global symdic
    return (False if (KL_ARG_V788_242 == tco_apply(kl_vector, [0])) else (tail_call(kl_vectorx63, [KL_ARG_V788_242]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.+vector', shen_x43vector, 1)

@tail_recursion
def shen_ebr(KL_ARG_V797_243, KL_ARG_V798_244, KL_ARG_V799_245):
    global symdic
    return (KL_ARG_V797_243 if (KL_ARG_V799_245 == KL_ARG_V798_244) else (KL_ARG_V799_245 if ((((((tco_apply(kl_occurrences, [KL_ARG_V798_244, KL_ARG_V799_245[1][0]]) > 0) if ([] == KL_ARG_V799_245[1][1][1]) else False) if shen_consp(KL_ARG_V799_245[1][1]) else False) if shen_consp(KL_ARG_V799_245[1]) else False) if (symdic.symdic_kl_x47_ == KL_ARG_V799_245[0]) else False) if shen_consp(KL_ARG_V799_245) else False) else ([symdic.symdic_kl_let, [KL_ARG_V799_245[1][0], [tco_apply(shen_ebr, [KL_ARG_V797_243, KL_ARG_V799_245[1][0], KL_ARG_V799_245[1][1][0]]), KL_ARG_V799_245[1][1][1]]]] if (((((((KL_ARG_V799_245[1][0] == KL_ARG_V798_244) if ([] == KL_ARG_V799_245[1][1][1][1]) else False) if shen_consp(KL_ARG_V799_245[1][1][1]) else False) if shen_consp(KL_ARG_V799_245[1][1]) else False) if shen_consp(KL_ARG_V799_245[1]) else False) if (symdic.symdic_kl_let == KL_ARG_V799_245[0]) else False) if shen_consp(KL_ARG_V799_245) else False) else ([tco_apply(shen_ebr, [KL_ARG_V797_243, KL_ARG_V798_244, KL_ARG_V799_245[0]]), tco_apply(shen_ebr, [KL_ARG_V797_243, KL_ARG_V798_244, KL_ARG_V799_245[1]])] if shen_consp(KL_ARG_V799_245) else (KL_ARG_V799_245 if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.ebr', shen_ebr, 3)

@tail_recursion
def shen_add_test(KL_ARG_V802_246):
    global symdic
    return shen_set(symdic.symdic_shen_x42teststackx42, [KL_ARG_V802_246, shen_get(symdic.symdic_shen_x42teststackx42)])
shen_add_fun('shen.add_test', shen_add_test, 1)

@tail_recursion
def shen_condx45expression(KL_ARG_V803_247, KL_ARG_V804_248, KL_ARG_V805_249):

    class KL_Context:
        KL_LOC_Err_250 = None
        KL_LOC_Cases_251 = None
        KL_LOC_EncodeChoices_252 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Err_250', tco_apply(shen_errx45condition, [KL_ARG_V803_247])), [setattr(KL_CTX, 'KL_LOC_Cases_251', tco_apply(shen_casex45form, [KL_ARG_V805_249, KL_CTX.KL_LOC_Err_250])), [setattr(KL_CTX, 'KL_LOC_EncodeChoices_252', tco_apply(shen_encodex45choices, [KL_CTX.KL_LOC_Cases_251, KL_ARG_V803_247])), tail_call(shen_condx45form, [KL_CTX.KL_LOC_EncodeChoices_252])][(-1)]][(-1)]][(-1)]
shen_add_fun('shen.cond-expression', shen_condx45expression, 3)

@tail_recursion
def shen_condx45form(KL_ARG_V808_253):
    global symdic
    return (KL_ARG_V808_253[0][1][0] if ((((([] == KL_ARG_V808_253[0][1][1]) if shen_consp(KL_ARG_V808_253[0][1]) else False) if (True == KL_ARG_V808_253[0][0]) else False) if shen_consp(KL_ARG_V808_253[0]) else False) if shen_consp(KL_ARG_V808_253) else False) else ([symdic.symdic_kl_cond, KL_ARG_V808_253] if True else shen_simple_error('condition failure')))
shen_add_fun('shen.cond-form', shen_condx45form, 1)

@tail_recursion
def shen_encodex45choices(KL_ARG_V811_254, KL_ARG_V812_255):
    global symdic
    return ([] if ([] == KL_ARG_V811_254) else ([[True, [[symdic.symdic_kl_let, [symdic.symdic_Result, [KL_ARG_V811_254[0][1][0][1][0], [[symdic.symdic_kl_if, [[symdic.symdic_kl_x61, [symdic.symdic_Result, [[symdic.symdic_kl_fail, []], []]]], [([symdic.symdic_shen_sysx45error, [KL_ARG_V812_255, []]] if shen_get(symdic.symdic_shen_x42installingx45klx42) else [symdic.symdic_shen_f_error, [KL_ARG_V812_255, []]]), [symdic.symdic_Result, []]]]], []]]]], []]], []] if (((((((((([] == KL_ARG_V811_254[1]) if ([] == KL_ARG_V811_254[0][1][1]) else False) if ([] == KL_ARG_V811_254[0][1][0][1][1]) else False) if shen_consp(KL_ARG_V811_254[0][1][0][1]) else False) if (symdic.symdic_shen_choicepointx33 == KL_ARG_V811_254[0][1][0][0]) else False) if shen_consp(KL_ARG_V811_254[0][1][0]) else False) if shen_consp(KL_ARG_V811_254[0][1]) else False) if (True == KL_ARG_V811_254[0][0]) else False) if shen_consp(KL_ARG_V811_254[0]) else False) if shen_consp(KL_ARG_V811_254) else False) else ([[True, [[symdic.symdic_kl_let, [symdic.symdic_Result, [KL_ARG_V811_254[0][1][0][1][0], [[symdic.symdic_kl_if, [[symdic.symdic_kl_x61, [symdic.symdic_Result, [[symdic.symdic_kl_fail, []], []]]], [tco_apply(shen_condx45form, [tco_apply(shen_encodex45choices, [KL_ARG_V811_254[1], KL_ARG_V812_255])]), [symdic.symdic_Result, []]]]], []]]]], []]], []] if ((((((((([] == KL_ARG_V811_254[0][1][1]) if ([] == KL_ARG_V811_254[0][1][0][1][1]) else False) if shen_consp(KL_ARG_V811_254[0][1][0][1]) else False) if (symdic.symdic_shen_choicepointx33 == KL_ARG_V811_254[0][1][0][0]) else False) if shen_consp(KL_ARG_V811_254[0][1][0]) else False) if shen_consp(KL_ARG_V811_254[0][1]) else False) if (True == KL_ARG_V811_254[0][0]) else False) if shen_consp(KL_ARG_V811_254[0]) else False) if shen_consp(KL_ARG_V811_254) else False) else ([[True, [[symdic.symdic_kl_let, [symdic.symdic_Freeze, [[symdic.symdic_kl_freeze, [tco_apply(shen_condx45form, [tco_apply(shen_encodex45choices, [KL_ARG_V811_254[1], KL_ARG_V812_255])]), []]], [[symdic.symdic_kl_if, [KL_ARG_V811_254[0][0], [[symdic.symdic_kl_let, [symdic.symdic_Result, [KL_ARG_V811_254[0][1][0][1][0], [[symdic.symdic_kl_if, [[symdic.symdic_kl_x61, [symdic.symdic_Result, [[symdic.symdic_kl_fail, []], []]]], [[symdic.symdic_kl_thaw, [symdic.symdic_Freeze, []]], [symdic.symdic_Result, []]]]], []]]]], [[symdic.symdic_kl_thaw, [symdic.symdic_Freeze, []]], []]]]], []]]]], []]], []] if (((((((([] == KL_ARG_V811_254[0][1][1]) if ([] == KL_ARG_V811_254[0][1][0][1][1]) else False) if shen_consp(KL_ARG_V811_254[0][1][0][1]) else False) if (symdic.symdic_shen_choicepointx33 == KL_ARG_V811_254[0][1][0][0]) else False) if shen_consp(KL_ARG_V811_254[0][1][0]) else False) if shen_consp(KL_ARG_V811_254[0][1]) else False) if shen_consp(KL_ARG_V811_254[0]) else False) if shen_consp(KL_ARG_V811_254) else False) else ([KL_ARG_V811_254[0], tco_apply(shen_encodex45choices, [KL_ARG_V811_254[1], KL_ARG_V812_255])] if (((([] == KL_ARG_V811_254[0][1][1]) if shen_consp(KL_ARG_V811_254[0][1]) else False) if shen_consp(KL_ARG_V811_254[0]) else False) if shen_consp(KL_ARG_V811_254) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_encodex45choices]) if True else shen_simple_error('condition failure')))))))
shen_add_fun('shen.encode-choices', shen_encodex45choices, 2)

@tail_recursion
def shen_casex45form(KL_ARG_V817_256, KL_ARG_V818_257):
    global symdic
    return ([KL_ARG_V818_257, []] if ([] == KL_ARG_V817_256) else ([[True, KL_ARG_V817_256[0][1]], tco_apply(shen_casex45form, [KL_ARG_V817_256[1], KL_ARG_V818_257])] if ((((((((((((([] == KL_ARG_V817_256[0][1][1]) if ([] == KL_ARG_V817_256[0][1][0][1][1]) else False) if shen_consp(KL_ARG_V817_256[0][1][0][1]) else False) if (symdic.symdic_shen_choicepointx33 == KL_ARG_V817_256[0][1][0][0]) else False) if shen_consp(KL_ARG_V817_256[0][1][0]) else False) if shen_consp(KL_ARG_V817_256[0][1]) else False) if ([] == KL_ARG_V817_256[0][0][1][1]) else False) if (symdic.symdic_shen_tests == KL_ARG_V817_256[0][0][1][0]) else False) if shen_consp(KL_ARG_V817_256[0][0][1]) else False) if (symdic.symdic_kl_x58 == KL_ARG_V817_256[0][0][0]) else False) if shen_consp(KL_ARG_V817_256[0][0]) else False) if shen_consp(KL_ARG_V817_256[0]) else False) if shen_consp(KL_ARG_V817_256) else False) else ([[True, KL_ARG_V817_256[0][1]], []] if ((((((((([] == KL_ARG_V817_256[0][1][1]) if shen_consp(KL_ARG_V817_256[0][1]) else False) if ([] == KL_ARG_V817_256[0][0][1][1]) else False) if (symdic.symdic_shen_tests == KL_ARG_V817_256[0][0][1][0]) else False) if shen_consp(KL_ARG_V817_256[0][0][1]) else False) if (symdic.symdic_kl_x58 == KL_ARG_V817_256[0][0][0]) else False) if shen_consp(KL_ARG_V817_256[0][0]) else False) if shen_consp(KL_ARG_V817_256[0]) else False) if shen_consp(KL_ARG_V817_256) else False) else ([[tco_apply(shen_embedx45and, [KL_ARG_V817_256[0][0][1][1]]), KL_ARG_V817_256[0][1]], tco_apply(shen_casex45form, [KL_ARG_V817_256[1], KL_ARG_V818_257])] if (((((((([] == KL_ARG_V817_256[0][1][1]) if shen_consp(KL_ARG_V817_256[0][1]) else False) if (symdic.symdic_shen_tests == KL_ARG_V817_256[0][0][1][0]) else False) if shen_consp(KL_ARG_V817_256[0][0][1]) else False) if (symdic.symdic_kl_x58 == KL_ARG_V817_256[0][0][0]) else False) if shen_consp(KL_ARG_V817_256[0][0]) else False) if shen_consp(KL_ARG_V817_256[0]) else False) if shen_consp(KL_ARG_V817_256) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_casex45form]) if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.case-form', shen_casex45form, 2)

@tail_recursion
def shen_embedx45and(KL_ARG_V819_258):
    global symdic
    return (KL_ARG_V819_258[0] if (([] == KL_ARG_V819_258[1]) if shen_consp(KL_ARG_V819_258) else False) else ([symdic.symdic_kl_and, [KL_ARG_V819_258[0], [tco_apply(shen_embedx45and, [KL_ARG_V819_258[1]]), []]]] if shen_consp(KL_ARG_V819_258) else (tail_call(shen_sysx45error, [symdic.symdic_shen_embedx45and]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.embed-and', shen_embedx45and, 1)

@tail_recursion
def shen_errx45condition(KL_ARG_V820_259):
    global symdic
    return [True, [[symdic.symdic_shen_f_error, [KL_ARG_V820_259, []]], []]]
shen_add_fun('shen.err-condition', shen_errx45condition, 1)

@tail_recursion
def shen_sysx45error(KL_ARG_V821_260):
    global symdic
    return shen_simple_error(('system function ' + tco_apply(shen_app, [KL_ARG_V821_260, ': unexpected argument\r\n', symdic.symdic_shen_a])))
shen_add_fun('shen.sys-error', shen_sysx45error, 1)


#============================== sys.kl==============================



@tail_recursion
def kl_thaw(KL_ARG_V1782_261):
    global symdic
    return shen_apply(KL_ARG_V1782_261, [])
shen_add_fun('thaw', kl_thaw, 1)

@tail_recursion
def kl_eval(KL_ARG_V1783_262):

    class KL_Context:
        KL_LOC_Macroexpand_263 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Macroexpand_263', tco_apply(shen_walk, [(lambda KL_ARG_V1780_264: tail_call(kl_macroexpand, [KL_ARG_V1780_264])), KL_ARG_V1783_262])), (tail_call(kl_map, [symdic.symdic_shen_evalx45withoutx45macros, tco_apply(shen_packagex45contents, [KL_CTX.KL_LOC_Macroexpand_263])]) if tco_apply(shen_packagedx63, [KL_CTX.KL_LOC_Macroexpand_263]) else tail_call(shen_evalx45withoutx45macros, [KL_CTX.KL_LOC_Macroexpand_263]))][(-1)]
shen_add_fun('eval', kl_eval, 1)

@tail_recursion
def shen_evalx45withoutx45macros(KL_ARG_V1784_265):
    global symdic
    return shen_eval_kl(tco_apply(shen_elimx45def, [tco_apply(shen_procx45inputx43, [KL_ARG_V1784_265])]))
shen_add_fun('shen.eval-without-macros', shen_evalx45withoutx45macros, 1)

@tail_recursion
def shen_procx45inputx43(KL_ARG_V1785_266):
    global symdic
    return ([symdic.symdic_kl_inputx43, [KL_ARG_V1785_266[1][0], [tco_apply(shen_rcons_form, [KL_ARG_V1785_266[1][1][0]]), []]]] if ((((([] == KL_ARG_V1785_266[1][1][1]) if shen_consp(KL_ARG_V1785_266[1][1]) else False) if shen_consp(KL_ARG_V1785_266[1]) else False) if (symdic.symdic_kl_inputx43 == KL_ARG_V1785_266[0]) else False) if shen_consp(KL_ARG_V1785_266) else False) else ([symdic.symdic_readx43, [KL_ARG_V1785_266[1][0], [tco_apply(shen_rcons_form, [KL_ARG_V1785_266[1][1][0]]), []]]] if ((((([] == KL_ARG_V1785_266[1][1][1]) if shen_consp(KL_ARG_V1785_266[1][1]) else False) if shen_consp(KL_ARG_V1785_266[1]) else False) if (symdic.symdic_readx43 == KL_ARG_V1785_266[0]) else False) if shen_consp(KL_ARG_V1785_266) else False) else (tail_call(kl_map, [symdic.symdic_shen_procx45inputx43, KL_ARG_V1785_266]) if shen_consp(KL_ARG_V1785_266) else (KL_ARG_V1785_266 if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.proc-input+', shen_procx45inputx43, 1)

@tail_recursion
def shen_elimx45def(KL_ARG_V1786_267):

    class KL_Context:
        KL_LOC_Default_268 = None
        KL_LOC_Def_269 = None
        KL_LOC_MacroAdd_270 = None
    KL_CTX = KL_Context()
    global symdic
    return (tail_call(shen_shenx45x62kl, [KL_ARG_V1786_267[1][0], KL_ARG_V1786_267[1][1]]) if ((shen_consp(KL_ARG_V1786_267[1]) if (symdic.symdic_kl_define == KL_ARG_V1786_267[0]) else False) if shen_consp(KL_ARG_V1786_267) else False) else ([setattr(KL_CTX, 'KL_LOC_Default_268', [symdic.symdic_X, [symdic.symdic_kl_x45x62, [symdic.symdic_X, []]]]), [setattr(KL_CTX, 'KL_LOC_Def_269', tco_apply(shen_elimx45def, [[symdic.symdic_kl_define, [KL_ARG_V1786_267[1][0], tco_apply(kl_append, [KL_ARG_V1786_267[1][1], KL_CTX.KL_LOC_Default_268])]]])), [setattr(KL_CTX, 'KL_LOC_MacroAdd_270', tco_apply(shen_addx45macro, [KL_ARG_V1786_267[1][0]])), KL_CTX.KL_LOC_Def_269][(-1)]][(-1)]][(-1)] if ((shen_consp(KL_ARG_V1786_267[1]) if (symdic.symdic_kl_defmacro == KL_ARG_V1786_267[0]) else False) if shen_consp(KL_ARG_V1786_267) else False) else (tail_call(shen_elimx45def, [tco_apply(shen_yacc, [KL_ARG_V1786_267])]) if ((shen_consp(KL_ARG_V1786_267[1]) if (symdic.symdic_kl_defcc == KL_ARG_V1786_267[0]) else False) if shen_consp(KL_ARG_V1786_267) else False) else (tail_call(kl_map, [symdic.symdic_shen_elimx45def, KL_ARG_V1786_267]) if shen_consp(KL_ARG_V1786_267) else (KL_ARG_V1786_267 if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.elim-def', shen_elimx45def, 1)

@tail_recursion
def shen_addx45macro(KL_ARG_V1787_271):
    global symdic
    return shen_set(symdic.symdic_kl_x42macrosx42, tco_apply(kl_adjoin, [KL_ARG_V1787_271, shen_get(symdic.symdic_kl_x42macrosx42)]))
shen_add_fun('shen.add-macro', shen_addx45macro, 1)

@tail_recursion
def shen_packagedx63(KL_ARG_V1794_272):
    global symdic
    return (True if (((shen_consp(KL_ARG_V1794_272[1][1]) if shen_consp(KL_ARG_V1794_272[1]) else False) if (symdic.symdic_kl_package == KL_ARG_V1794_272[0]) else False) if shen_consp(KL_ARG_V1794_272) else False) else (False if True else shen_simple_error('condition failure')))
shen_add_fun('shen.packaged?', shen_packagedx63, 1)

@tail_recursion
def kl_external(KL_ARG_V1795_273):
    global symdic
    return shen_try_except((lambda : tco_apply(kl_get, [KL_ARG_V1795_273, symdic.symdic_shen_externalx45symbols, shen_get(symdic.symdic_kl_x42propertyx45vectorx42)])), (lambda KL_ARG_E_274: shen_simple_error(('package ' + tco_apply(shen_app, [KL_ARG_V1795_273, ' has not been used.\r\n', symdic.symdic_shen_a])))))
shen_add_fun('external', kl_external, 1)

@tail_recursion
def shen_packagex45contents(KL_ARG_V1798_275):
    global symdic
    return (KL_ARG_V1798_275[1][1][1] if ((((shen_consp(KL_ARG_V1798_275[1][1]) if (symdic.symdic_kl_null == KL_ARG_V1798_275[1][0]) else False) if shen_consp(KL_ARG_V1798_275[1]) else False) if (symdic.symdic_kl_package == KL_ARG_V1798_275[0]) else False) if shen_consp(KL_ARG_V1798_275) else False) else (tail_call(shen_packageh, [KL_ARG_V1798_275[1][0], KL_ARG_V1798_275[1][1][0], KL_ARG_V1798_275[1][1][1]]) if (((shen_consp(KL_ARG_V1798_275[1][1]) if shen_consp(KL_ARG_V1798_275[1]) else False) if (symdic.symdic_kl_package == KL_ARG_V1798_275[0]) else False) if shen_consp(KL_ARG_V1798_275) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_packagex45contents]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.package-contents', shen_packagex45contents, 1)

@tail_recursion
def shen_walk(KL_ARG_V1799_276, KL_ARG_V1800_277):
    global symdic
    return (shen_apply(KL_ARG_V1799_276, [tco_apply(kl_map, [(lambda KL_ARG_Z_278: tail_call(shen_walk, [KL_ARG_V1799_276, KL_ARG_Z_278])), KL_ARG_V1800_277])]) if shen_consp(KL_ARG_V1800_277) else (shen_apply(KL_ARG_V1799_276, [KL_ARG_V1800_277]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.walk', shen_walk, 2)

@tail_recursion
def kl_compile(KL_ARG_V1801_279, KL_ARG_V1802_280, KL_ARG_V1803_281):

    class KL_Context:
        KL_LOC_O_282 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_O_282', shen_apply(KL_ARG_V1801_279, [[KL_ARG_V1802_280, [[], []]]])), (shen_apply(KL_ARG_V1803_281, [KL_CTX.KL_LOC_O_282]) if (True if (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_O_282) else (not tco_apply(kl_emptyx63, [KL_CTX.KL_LOC_O_282[0]]))) else tail_call(shen_hdtl, [KL_CTX.KL_LOC_O_282]))][(-1)]
shen_add_fun('compile', kl_compile, 3)

@tail_recursion
def kl_failx45if(KL_ARG_V1804_283, KL_ARG_V1805_284):
    global symdic
    return (tail_call(kl_fail, []) if shen_apply(KL_ARG_V1804_283, [KL_ARG_V1805_284]) else KL_ARG_V1805_284)
shen_add_fun('fail-if', kl_failx45if, 2)

@tail_recursion
def kl_x64s(KL_ARG_V1806_285, KL_ARG_V1807_286):
    global symdic
    return (KL_ARG_V1806_285 + KL_ARG_V1807_286)
shen_add_fun('@s', kl_x64s, 2)

@tail_recursion
def kl_tcx63():
    global symdic
    return shen_get(symdic.symdic_shen_x42tcx42)
shen_add_fun('tc?', kl_tcx63, 0)

@tail_recursion
def kl_ps(KL_ARG_V1808_287):
    global symdic
    return shen_try_except((lambda : tco_apply(kl_get, [KL_ARG_V1808_287, symdic.symdic_shen_source, shen_get(symdic.symdic_kl_x42propertyx45vectorx42)])), (lambda KL_ARG_E_288: shen_simple_error(tco_apply(shen_app, [KL_ARG_V1808_287, ' not found.\r\n', symdic.symdic_shen_a]))))
shen_add_fun('ps', kl_ps, 1)

@tail_recursion
def kl_stinput():
    global symdic
    return shen_get(symdic.symdic_kl_x42stinputx42)
shen_add_fun('stinput', kl_stinput, 0)

@tail_recursion
def shen_x43vectorx63(KL_ARG_V1809_289):
    global symdic
    return ((shen_absvector_get(KL_ARG_V1809_289, 0) > 0) if shen_absvectorp(KL_ARG_V1809_289) else False)
shen_add_fun('shen.+vector?', shen_x43vectorx63, 1)

@tail_recursion
def kl_vector(KL_ARG_V1810_290):

    class KL_Context:
        KL_LOC_Vector_291 = None
        KL_LOC_ZeroStamp_292 = None
        KL_LOC_Standard_293 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Vector_291', shen_absvector((KL_ARG_V1810_290 + 1))), [setattr(KL_CTX, 'KL_LOC_ZeroStamp_292', shen_absvector_set(KL_CTX.KL_LOC_Vector_291, 0, KL_ARG_V1810_290)), [setattr(KL_CTX, 'KL_LOC_Standard_293', (KL_CTX.KL_LOC_ZeroStamp_292 if (KL_ARG_V1810_290 == 0) else tco_apply(shen_fillvector, [KL_CTX.KL_LOC_ZeroStamp_292, 1, KL_ARG_V1810_290, tco_apply(kl_fail, [])]))), KL_CTX.KL_LOC_Standard_293][(-1)]][(-1)]][(-1)]
shen_add_fun('vector', kl_vector, 1)

@tail_recursion
def shen_fillvector(KL_ARG_V1811_294, KL_ARG_V1812_295, KL_ARG_V1813_296, KL_ARG_V1814_297):
    global symdic
    return (shen_absvector_set(KL_ARG_V1811_294, KL_ARG_V1813_296, KL_ARG_V1814_297) if (KL_ARG_V1813_296 == KL_ARG_V1812_295) else (tail_call(shen_fillvector, [shen_absvector_set(KL_ARG_V1811_294, KL_ARG_V1812_295, KL_ARG_V1814_297), (1 + KL_ARG_V1812_295), KL_ARG_V1813_296, KL_ARG_V1814_297]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.fillvector', shen_fillvector, 4)

@tail_recursion
def kl_vectorx63(KL_ARG_V1816_298):
    global symdic
    return (shen_try_except((lambda : (shen_absvector_get(KL_ARG_V1816_298, 0) >= 0)), (lambda KL_ARG_E_299: False)) if shen_absvectorp(KL_ARG_V1816_298) else False)
shen_add_fun('vector?', kl_vectorx63, 1)

@tail_recursion
def kl_vectorx45x62(KL_ARG_V1817_300, KL_ARG_V1818_301, KL_ARG_V1819_302):
    global symdic
    return (shen_simple_error('cannot access 0th element of a vector\r\n') if (KL_ARG_V1818_301 == 0) else shen_absvector_set(KL_ARG_V1817_300, KL_ARG_V1818_301, KL_ARG_V1819_302))
shen_add_fun('vector->', kl_vectorx45x62, 3)

@tail_recursion
def kl_x60x45vector(KL_ARG_V1820_303, KL_ARG_V1821_304):

    class KL_Context:
        KL_LOC_VectorElement_305 = None
    KL_CTX = KL_Context()
    global symdic
    return (shen_simple_error('cannot access 0th element of a vector\r\n') if (KL_ARG_V1821_304 == 0) else [setattr(KL_CTX, 'KL_LOC_VectorElement_305', shen_absvector_get(KL_ARG_V1820_303, KL_ARG_V1821_304)), (shen_simple_error('vector element not found\r\n') if (KL_CTX.KL_LOC_VectorElement_305 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_VectorElement_305)][(-1)])
shen_add_fun('<-vector', kl_x60x45vector, 2)

@tail_recursion
def shen_posintx63(KL_ARG_V1822_306):
    global symdic
    return ((KL_ARG_V1822_306 >= 0) if tco_apply(kl_integerx63, [KL_ARG_V1822_306]) else False)
shen_add_fun('shen.posint?', shen_posintx63, 1)

@tail_recursion
def kl_limit(KL_ARG_V1823_307):
    global symdic
    return shen_absvector_get(KL_ARG_V1823_307, 0)
shen_add_fun('limit', kl_limit, 1)

@tail_recursion
def kl_symbolx63(KL_ARG_V1824_308):

    class KL_Context:
        KL_LOC_String_309 = None
    KL_CTX = KL_Context()
    global symdic
    return (False if (True if tco_apply(kl_booleanx63, [KL_ARG_V1824_308]) else (True if isinstance(KL_ARG_V1824_308, numbers.Number) else isinstance(KL_ARG_V1824_308, str))) else (shen_try_except((lambda : [setattr(KL_CTX, 'KL_LOC_String_309', str(KL_ARG_V1824_308)), tco_apply(shen_analysex45symbolx63, [KL_CTX.KL_LOC_String_309])][(-1)]), (lambda KL_ARG_E_310: False)) if True else shen_simple_error('condition failure')))
shen_add_fun('symbol?', kl_symbolx63, 1)

@tail_recursion
def shen_analysex45symbolx63(KL_ARG_V1825_311):
    global symdic
    return ((tail_call(shen_alphanumsx63, [KL_ARG_V1825_311[1:]]) if tco_apply(shen_alphax63, [KL_ARG_V1825_311[0]]) else False) if tco_apply(shen_x43stringx63, [KL_ARG_V1825_311]) else (tail_call(shen_sysx45error, [symdic.symdic_shen_analysex45symbolx63]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.analyse-symbol?', shen_analysex45symbolx63, 1)

@tail_recursion
def shen_alphax63(KL_ARG_V1826_312):
    global symdic
    return tail_call(kl_elementx63, [KL_ARG_V1826_312, ['A', ['B', ['C', ['D', ['E', ['F', ['G', ['H', ['I', ['J', ['K', ['L', ['M', ['N', ['O', ['P', ['Q', ['R', ['S', ['T', ['U', ['V', ['W', ['X', ['Y', ['Z', ['a', ['b', ['c', ['d', ['e', ['f', ['g', ['h', ['i', ['j', ['k', ['l', ['m', ['n', ['o', ['p', ['q', ['r', ['s', ['t', ['u', ['v', ['w', ['x', ['y', ['z', ['=', ['*', ['/', ['+', ['-', ['_', ['?', ['$', ['!', ['@', ['~', ['>', ['<', ['&', ['%', ['{', ['}', [':', [';', ['`', ['#', ["'", ['.', []]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]])
shen_add_fun('shen.alpha?', shen_alphax63, 1)

@tail_recursion
def shen_alphanumsx63(KL_ARG_V1827_313):
    global symdic
    return (True if ('' == KL_ARG_V1827_313) else ((tail_call(shen_alphanumsx63, [KL_ARG_V1827_313[1:]]) if tco_apply(shen_alphanumx63, [KL_ARG_V1827_313[0]]) else False) if tco_apply(shen_x43stringx63, [KL_ARG_V1827_313]) else (tail_call(shen_sysx45error, [symdic.symdic_shen_alphanumsx63]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.alphanums?', shen_alphanumsx63, 1)

@tail_recursion
def shen_alphanumx63(KL_ARG_V1828_314):
    global symdic
    return (True if tco_apply(shen_alphax63, [KL_ARG_V1828_314]) else tail_call(shen_digitx63, [KL_ARG_V1828_314]))
shen_add_fun('shen.alphanum?', shen_alphanumx63, 1)

@tail_recursion
def shen_digitx63(KL_ARG_V1829_315):
    global symdic
    return tail_call(kl_elementx63, [KL_ARG_V1829_315, ['1', ['2', ['3', ['4', ['5', ['6', ['7', ['8', ['9', ['0', []]]]]]]]]]]])
shen_add_fun('shen.digit?', shen_digitx63, 1)

@tail_recursion
def kl_variablex63(KL_ARG_V1830_316):

    class KL_Context:
        KL_LOC_String_317 = None
    KL_CTX = KL_Context()
    global symdic
    return (False if (True if tco_apply(kl_booleanx63, [KL_ARG_V1830_316]) else (True if isinstance(KL_ARG_V1830_316, numbers.Number) else isinstance(KL_ARG_V1830_316, str))) else (shen_try_except((lambda : [setattr(KL_CTX, 'KL_LOC_String_317', str(KL_ARG_V1830_316)), tco_apply(shen_analysex45variablex63, [KL_CTX.KL_LOC_String_317])][(-1)]), (lambda KL_ARG_E_318: False)) if True else shen_simple_error('condition failure')))
shen_add_fun('variable?', kl_variablex63, 1)

@tail_recursion
def shen_analysex45variablex63(KL_ARG_V1831_319):
    global symdic
    return ((tail_call(shen_alphanumsx63, [KL_ARG_V1831_319[1:]]) if tco_apply(shen_uppercasex63, [KL_ARG_V1831_319[0]]) else False) if tco_apply(shen_x43stringx63, [KL_ARG_V1831_319]) else (tail_call(shen_sysx45error, [symdic.symdic_shen_analysex45variablex63]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.analyse-variable?', shen_analysex45variablex63, 1)

@tail_recursion
def shen_uppercasex63(KL_ARG_V1832_320):
    global symdic
    return tail_call(kl_elementx63, [KL_ARG_V1832_320, ['A', ['B', ['C', ['D', ['E', ['F', ['G', ['H', ['I', ['J', ['K', ['L', ['M', ['N', ['O', ['P', ['Q', ['R', ['S', ['T', ['U', ['V', ['W', ['X', ['Y', ['Z', []]]]]]]]]]]]]]]]]]]]]]]]]]]])
shen_add_fun('shen.uppercase?', shen_uppercasex63, 1)

@tail_recursion
def kl_gensym(KL_ARG_V1833_321):
    global symdic
    return tail_call(kl_concat, [KL_ARG_V1833_321, shen_set(symdic.symdic_shen_x42gensymx42, (1 + shen_get(symdic.symdic_shen_x42gensymx42)))])
shen_add_fun('gensym', kl_gensym, 1)

@tail_recursion
def kl_concat(KL_ARG_V1834_322, KL_ARG_V1835_323):
    global symdic
    return shen_intern((str(KL_ARG_V1834_322) + str(KL_ARG_V1835_323)))
shen_add_fun('concat', kl_concat, 2)

@tail_recursion
def kl_x64p(KL_ARG_V1836_324, KL_ARG_V1837_325):

    class KL_Context:
        KL_LOC_Vector_326 = None
        KL_LOC_Tag_327 = None
        KL_LOC_Fst_328 = None
        KL_LOC_Snd_329 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Vector_326', shen_absvector(3)), [setattr(KL_CTX, 'KL_LOC_Tag_327', shen_absvector_set(KL_CTX.KL_LOC_Vector_326, 0, symdic.symdic_shen_tuple)), [setattr(KL_CTX, 'KL_LOC_Fst_328', shen_absvector_set(KL_CTX.KL_LOC_Vector_326, 1, KL_ARG_V1836_324)), [setattr(KL_CTX, 'KL_LOC_Snd_329', shen_absvector_set(KL_CTX.KL_LOC_Vector_326, 2, KL_ARG_V1837_325)), KL_CTX.KL_LOC_Vector_326][(-1)]][(-1)]][(-1)]][(-1)]
shen_add_fun('@p', kl_x64p, 2)

@tail_recursion
def kl_fst(KL_ARG_V1838_330):
    global symdic
    return shen_absvector_get(KL_ARG_V1838_330, 1)
shen_add_fun('fst', kl_fst, 1)

@tail_recursion
def kl_snd(KL_ARG_V1839_331):
    global symdic
    return shen_absvector_get(KL_ARG_V1839_331, 2)
shen_add_fun('snd', kl_snd, 1)

@tail_recursion
def kl_tuplex63(KL_ARG_V1840_332):
    global symdic
    return shen_try_except((lambda : ((symdic.symdic_shen_tuple == shen_absvector_get(KL_ARG_V1840_332, 0)) if shen_absvectorp(KL_ARG_V1840_332) else False)), (lambda KL_ARG_E_333: False))
shen_add_fun('tuple?', kl_tuplex63, 1)

@tail_recursion
def kl_append(KL_ARG_V1841_334, KL_ARG_V1842_335):
    global symdic
    return (KL_ARG_V1842_335 if ([] == KL_ARG_V1841_334) else ([KL_ARG_V1841_334[0], tco_apply(kl_append, [KL_ARG_V1841_334[1], KL_ARG_V1842_335])] if shen_consp(KL_ARG_V1841_334) else (tail_call(shen_sysx45error, [symdic.symdic_kl_append]) if True else shen_simple_error('condition failure'))))
shen_add_fun('append', kl_append, 2)

@tail_recursion
def kl_x64v(KL_ARG_V1843_336, KL_ARG_V1844_337):

    class KL_Context:
        KL_LOC_Limit_338 = None
        KL_LOC_NewVector_339 = None
        KL_LOC_Xx43NewVector_340 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Limit_338', tco_apply(kl_limit, [KL_ARG_V1844_337])), [setattr(KL_CTX, 'KL_LOC_NewVector_339', tco_apply(kl_vector, [(KL_CTX.KL_LOC_Limit_338 + 1)])), [setattr(KL_CTX, 'KL_LOC_Xx43NewVector_340', tco_apply(kl_vectorx45x62, [KL_CTX.KL_LOC_NewVector_339, 1, KL_ARG_V1843_336])), (KL_CTX.KL_LOC_Xx43NewVector_340 if (KL_CTX.KL_LOC_Limit_338 == 0) else tail_call(shen_x64vx45help, [KL_ARG_V1844_337, 1, KL_CTX.KL_LOC_Limit_338, KL_CTX.KL_LOC_Xx43NewVector_340]))][(-1)]][(-1)]][(-1)]
shen_add_fun('@v', kl_x64v, 2)

@tail_recursion
def shen_x64vx45help(KL_ARG_V1845_341, KL_ARG_V1846_342, KL_ARG_V1847_343, KL_ARG_V1848_344):
    global symdic
    return (tail_call(shen_copyfromvector, [KL_ARG_V1845_341, KL_ARG_V1848_344, KL_ARG_V1847_343, (KL_ARG_V1847_343 + 1)]) if (KL_ARG_V1847_343 == KL_ARG_V1846_342) else (tail_call(shen_x64vx45help, [KL_ARG_V1845_341, (KL_ARG_V1846_342 + 1), KL_ARG_V1847_343, tco_apply(shen_copyfromvector, [KL_ARG_V1845_341, KL_ARG_V1848_344, KL_ARG_V1846_342, (KL_ARG_V1846_342 + 1)])]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.@v-help', shen_x64vx45help, 4)

@tail_recursion
def shen_copyfromvector(KL_ARG_V1850_345, KL_ARG_V1851_346, KL_ARG_V1852_347, KL_ARG_V1853_348):
    global symdic
    return shen_try_except((lambda : tco_apply(kl_vectorx45x62, [KL_ARG_V1851_346, KL_ARG_V1853_348, tco_apply(kl_x60x45vector, [KL_ARG_V1850_345, KL_ARG_V1852_347])])), (lambda KL_ARG_E_349: KL_ARG_V1851_346))
shen_add_fun('shen.copyfromvector', shen_copyfromvector, 4)

@tail_recursion
def kl_hdv(KL_ARG_V1854_350):
    global symdic
    return shen_try_except((lambda : tco_apply(kl_x60x45vector, [KL_ARG_V1854_350, 1])), (lambda KL_ARG_E_351: shen_simple_error(('hdv needs a non-empty vector as an argument; not ' + tco_apply(shen_app, [KL_ARG_V1854_350, '\r\n', symdic.symdic_shen_s])))))
shen_add_fun('hdv', kl_hdv, 1)

@tail_recursion
def kl_tlv(KL_ARG_V1855_352):

    class KL_Context:
        KL_LOC_Limit_353 = None
        KL_LOC_NewVector_354 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Limit_353', tco_apply(kl_limit, [KL_ARG_V1855_352])), (shen_simple_error('cannot take the tail of the empty vector\r\n') if (KL_CTX.KL_LOC_Limit_353 == 0) else (tail_call(kl_vector, [0]) if (KL_CTX.KL_LOC_Limit_353 == 1) else [setattr(KL_CTX, 'KL_LOC_NewVector_354', tco_apply(kl_vector, [(KL_CTX.KL_LOC_Limit_353 - 1)])), tail_call(shen_tlvx45help, [KL_ARG_V1855_352, 2, KL_CTX.KL_LOC_Limit_353, tco_apply(kl_vector, [(KL_CTX.KL_LOC_Limit_353 - 1)])])][(-1)]))][(-1)]
shen_add_fun('tlv', kl_tlv, 1)

@tail_recursion
def shen_tlvx45help(KL_ARG_V1856_355, KL_ARG_V1857_356, KL_ARG_V1858_357, KL_ARG_V1859_358):
    global symdic
    return (tail_call(shen_copyfromvector, [KL_ARG_V1856_355, KL_ARG_V1859_358, KL_ARG_V1858_357, (KL_ARG_V1858_357 - 1)]) if (KL_ARG_V1858_357 == KL_ARG_V1857_356) else (tail_call(shen_tlvx45help, [KL_ARG_V1856_355, (KL_ARG_V1857_356 + 1), KL_ARG_V1858_357, tco_apply(shen_copyfromvector, [KL_ARG_V1856_355, KL_ARG_V1859_358, KL_ARG_V1857_356, (KL_ARG_V1857_356 - 1)])]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.tlv-help', shen_tlvx45help, 4)

@tail_recursion
def kl_assoc(KL_ARG_V1869_359, KL_ARG_V1870_360):
    global symdic
    return ([] if ([] == KL_ARG_V1870_360) else (KL_ARG_V1870_360[0] if (((KL_ARG_V1870_360[0][0] == KL_ARG_V1869_359) if shen_consp(KL_ARG_V1870_360[0]) else False) if shen_consp(KL_ARG_V1870_360) else False) else (tail_call(kl_assoc, [KL_ARG_V1869_359, KL_ARG_V1870_360[1]]) if shen_consp(KL_ARG_V1870_360) else (tail_call(shen_sysx45error, [symdic.symdic_kl_assoc]) if True else shen_simple_error('condition failure')))))
shen_add_fun('assoc', kl_assoc, 2)

@tail_recursion
def kl_booleanx63(KL_ARG_V1876_361):
    global symdic
    return (True if (True == KL_ARG_V1876_361) else (True if (False == KL_ARG_V1876_361) else (False if True else shen_simple_error('condition failure'))))
shen_add_fun('boolean?', kl_booleanx63, 1)

@tail_recursion
def kl_nl(KL_ARG_V1877_362):
    global symdic
    return (0 if (0 == KL_ARG_V1877_362) else ([tco_apply(shen_prhush, ['\r\n', tco_apply(kl_stoutput, [])]), tail_call(kl_nl, [(KL_ARG_V1877_362 - 1)])][(-1)] if True else shen_simple_error('condition failure')))
shen_add_fun('nl', kl_nl, 1)

@tail_recursion
def kl_difference(KL_ARG_V1880_363, KL_ARG_V1881_364):
    global symdic
    return ([] if ([] == KL_ARG_V1880_363) else ((tail_call(kl_difference, [KL_ARG_V1880_363[1], KL_ARG_V1881_364]) if tco_apply(kl_elementx63, [KL_ARG_V1880_363[0], KL_ARG_V1881_364]) else [KL_ARG_V1880_363[0], tco_apply(kl_difference, [KL_ARG_V1880_363[1], KL_ARG_V1881_364])]) if shen_consp(KL_ARG_V1880_363) else (tail_call(shen_sysx45error, [symdic.symdic_kl_difference]) if True else shen_simple_error('condition failure'))))
shen_add_fun('difference', kl_difference, 2)

@tail_recursion
def kl_do(KL_ARG_V1882_365, KL_ARG_V1883_366):
    global symdic
    return KL_ARG_V1883_366
shen_add_fun('do', kl_do, 2)

@tail_recursion
def kl_elementx63(KL_ARG_V1892_367, KL_ARG_V1893_368):
    global symdic
    return (False if ([] == KL_ARG_V1893_368) else (True if ((KL_ARG_V1893_368[0] == KL_ARG_V1892_367) if shen_consp(KL_ARG_V1893_368) else False) else (tail_call(kl_elementx63, [KL_ARG_V1892_367, KL_ARG_V1893_368[1]]) if shen_consp(KL_ARG_V1893_368) else (tail_call(shen_sysx45error, [symdic.symdic_kl_elementx63]) if True else shen_simple_error('condition failure')))))
shen_add_fun('element?', kl_elementx63, 2)

@tail_recursion
def kl_emptyx63(KL_ARG_V1899_369):
    global symdic
    return (True if ([] == KL_ARG_V1899_369) else (False if True else shen_simple_error('condition failure')))
shen_add_fun('empty?', kl_emptyx63, 1)

@tail_recursion
def kl_fix(KL_ARG_V1900_370, KL_ARG_V1901_371):
    global symdic
    return tail_call(shen_fixx45help, [KL_ARG_V1900_370, KL_ARG_V1901_371, shen_apply(KL_ARG_V1900_370, [KL_ARG_V1901_371])])
shen_add_fun('fix', kl_fix, 2)

@tail_recursion
def shen_fixx45help(KL_ARG_V1908_372, KL_ARG_V1909_373, KL_ARG_V1910_374):
    global symdic
    return (KL_ARG_V1910_374 if (KL_ARG_V1910_374 == KL_ARG_V1909_373) else (tail_call(shen_fixx45help, [KL_ARG_V1908_372, KL_ARG_V1910_374, shen_apply(KL_ARG_V1908_372, [KL_ARG_V1910_374])]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.fix-help', shen_fixx45help, 3)

@tail_recursion
def kl_put(KL_ARG_V1912_375, KL_ARG_V1913_376, KL_ARG_V1914_377, KL_ARG_V1915_378):

    class KL_Context:
        KL_LOC_N_379 = None
        KL_LOC_Entry_380 = None
        KL_LOC_Change_382 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_N_379', tco_apply(kl_hash, [KL_ARG_V1912_375, tco_apply(kl_limit, [KL_ARG_V1915_378])])), [setattr(KL_CTX, 'KL_LOC_Entry_380', shen_try_except((lambda : tco_apply(kl_x60x45vector, [KL_ARG_V1915_378, KL_CTX.KL_LOC_N_379])), (lambda KL_ARG_E_381: []))), [setattr(KL_CTX, 'KL_LOC_Change_382', tco_apply(kl_vectorx45x62, [KL_ARG_V1915_378, KL_CTX.KL_LOC_N_379, tco_apply(shen_changex45pointerx45value, [KL_ARG_V1912_375, KL_ARG_V1913_376, KL_ARG_V1914_377, KL_CTX.KL_LOC_Entry_380])])), KL_ARG_V1914_377][(-1)]][(-1)]][(-1)]
shen_add_fun('put', kl_put, 4)

@tail_recursion
def shen_changex45pointerx45value(KL_ARG_V1918_383, KL_ARG_V1919_384, KL_ARG_V1920_385, KL_ARG_V1921_386):
    global symdic
    return ([[[KL_ARG_V1918_383, [KL_ARG_V1919_384, []]], KL_ARG_V1920_385], []] if ([] == KL_ARG_V1921_386) else ([[KL_ARG_V1921_386[0][0], KL_ARG_V1920_385], KL_ARG_V1921_386[1]] if (((((((KL_ARG_V1921_386[0][0][0] == KL_ARG_V1918_383) if (KL_ARG_V1921_386[0][0][1][0] == KL_ARG_V1919_384) else False) if ([] == KL_ARG_V1921_386[0][0][1][1]) else False) if shen_consp(KL_ARG_V1921_386[0][0][1]) else False) if shen_consp(KL_ARG_V1921_386[0][0]) else False) if shen_consp(KL_ARG_V1921_386[0]) else False) if shen_consp(KL_ARG_V1921_386) else False) else ([KL_ARG_V1921_386[0], tco_apply(shen_changex45pointerx45value, [KL_ARG_V1918_383, KL_ARG_V1919_384, KL_ARG_V1920_385, KL_ARG_V1921_386[1]])] if shen_consp(KL_ARG_V1921_386) else (tail_call(shen_sysx45error, [symdic.symdic_shen_changex45pointerx45value]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.change-pointer-value', shen_changex45pointerx45value, 4)

@tail_recursion
def kl_get(KL_ARG_V1924_387, KL_ARG_V1925_388, KL_ARG_V1926_389):

    class KL_Context:
        KL_LOC_N_390 = None
        KL_LOC_Entry_391 = None
        KL_LOC_Result_393 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_N_390', tco_apply(kl_hash, [KL_ARG_V1924_387, tco_apply(kl_limit, [KL_ARG_V1926_389])])), [setattr(KL_CTX, 'KL_LOC_Entry_391', shen_try_except((lambda : tco_apply(kl_x60x45vector, [KL_ARG_V1926_389, KL_CTX.KL_LOC_N_390])), (lambda KL_ARG_E_392: shen_simple_error('pointer not found\r\n')))), [setattr(KL_CTX, 'KL_LOC_Result_393', tco_apply(kl_assoc, [[KL_ARG_V1924_387, [KL_ARG_V1925_388, []]], KL_CTX.KL_LOC_Entry_391])), (shen_simple_error('value not found\r\n') if tco_apply(kl_emptyx63, [KL_CTX.KL_LOC_Result_393]) else KL_CTX.KL_LOC_Result_393[1])][(-1)]][(-1)]][(-1)]
shen_add_fun('get', kl_get, 3)

@tail_recursion
def kl_hash(KL_ARG_V1927_394, KL_ARG_V1928_395):

    class KL_Context:
        KL_LOC_Hash_396 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Hash_396', tco_apply(shen_mod, [tco_apply(shen_sum, [tco_apply(kl_map, [(lambda KL_ARG_V1781_397: ord(KL_ARG_V1781_397)), tco_apply(kl_explode, [KL_ARG_V1927_394])])]), KL_ARG_V1928_395])), (1 if (0 == KL_CTX.KL_LOC_Hash_396) else KL_CTX.KL_LOC_Hash_396)][(-1)]
shen_add_fun('hash', kl_hash, 2)

@tail_recursion
def shen_mod(KL_ARG_V1929_398, KL_ARG_V1930_399):
    global symdic
    return tail_call(shen_modh, [KL_ARG_V1929_398, tco_apply(shen_multiples, [KL_ARG_V1929_398, [KL_ARG_V1930_399, []]])])
shen_add_fun('shen.mod', shen_mod, 2)

@tail_recursion
def shen_multiples(KL_ARG_V1931_400, KL_ARG_V1932_401):
    global symdic
    return (KL_ARG_V1932_401[1] if ((KL_ARG_V1932_401[0] > KL_ARG_V1931_400) if shen_consp(KL_ARG_V1932_401) else False) else (tail_call(shen_multiples, [KL_ARG_V1931_400, [(2 * KL_ARG_V1932_401[0]), KL_ARG_V1932_401]]) if shen_consp(KL_ARG_V1932_401) else (tail_call(shen_sysx45error, [symdic.symdic_shen_multiples]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.multiples', shen_multiples, 2)

@tail_recursion
def shen_modh(KL_ARG_V1935_402, KL_ARG_V1936_403):
    global symdic
    return (0 if (0 == KL_ARG_V1935_402) else (KL_ARG_V1935_402 if ([] == KL_ARG_V1936_403) else ((KL_ARG_V1935_402 if tco_apply(kl_emptyx63, [KL_ARG_V1936_403[1]]) else tail_call(shen_modh, [KL_ARG_V1935_402, KL_ARG_V1936_403[1]])) if ((KL_ARG_V1936_403[0] > KL_ARG_V1935_402) if shen_consp(KL_ARG_V1936_403) else False) else (tail_call(shen_modh, [(KL_ARG_V1935_402 - KL_ARG_V1936_403[0]), KL_ARG_V1936_403]) if shen_consp(KL_ARG_V1936_403) else (tail_call(shen_sysx45error, [symdic.symdic_shen_modh]) if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.modh', shen_modh, 2)

@tail_recursion
def shen_sum(KL_ARG_V1937_404):
    global symdic
    return (0 if ([] == KL_ARG_V1937_404) else ((KL_ARG_V1937_404[0] + tco_apply(shen_sum, [KL_ARG_V1937_404[1]])) if shen_consp(KL_ARG_V1937_404) else (tail_call(shen_sysx45error, [symdic.symdic_shen_sum]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.sum', shen_sum, 1)

@tail_recursion
def kl_head(KL_ARG_V1944_405):
    global symdic
    return (KL_ARG_V1944_405[0] if shen_consp(KL_ARG_V1944_405) else (shen_simple_error('head expects a non-empty list') if True else shen_simple_error('condition failure')))
shen_add_fun('head', kl_head, 1)

@tail_recursion
def kl_tail(KL_ARG_V1951_406):
    global symdic
    return (KL_ARG_V1951_406[1] if shen_consp(KL_ARG_V1951_406) else (shen_simple_error('tail expects a non-empty list') if True else shen_simple_error('condition failure')))
shen_add_fun('tail', kl_tail, 1)

@tail_recursion
def kl_hdstr(KL_ARG_V1952_407):
    global symdic
    return KL_ARG_V1952_407[0]
shen_add_fun('hdstr', kl_hdstr, 1)

@tail_recursion
def kl_intersection(KL_ARG_V1955_408, KL_ARG_V1956_409):
    global symdic
    return ([] if ([] == KL_ARG_V1955_408) else (([KL_ARG_V1955_408[0], tco_apply(kl_intersection, [KL_ARG_V1955_408[1], KL_ARG_V1956_409])] if tco_apply(kl_elementx63, [KL_ARG_V1955_408[0], KL_ARG_V1956_409]) else tail_call(kl_intersection, [KL_ARG_V1955_408[1], KL_ARG_V1956_409])) if shen_consp(KL_ARG_V1955_408) else (tail_call(shen_sysx45error, [symdic.symdic_kl_intersection]) if True else shen_simple_error('condition failure'))))
shen_add_fun('intersection', kl_intersection, 2)

@tail_recursion
def kl_reverse(KL_ARG_V1957_410):
    global symdic
    return tail_call(shen_reverse_help, [KL_ARG_V1957_410, []])
shen_add_fun('reverse', kl_reverse, 1)

@tail_recursion
def shen_reverse_help(KL_ARG_V1958_411, KL_ARG_V1959_412):
    global symdic
    return (KL_ARG_V1959_412 if ([] == KL_ARG_V1958_411) else (tail_call(shen_reverse_help, [KL_ARG_V1958_411[1], [KL_ARG_V1958_411[0], KL_ARG_V1959_412]]) if shen_consp(KL_ARG_V1958_411) else (tail_call(shen_sysx45error, [symdic.symdic_shen_reverse_help]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.reverse_help', shen_reverse_help, 2)

@tail_recursion
def kl_union(KL_ARG_V1960_413, KL_ARG_V1961_414):
    global symdic
    return (KL_ARG_V1961_414 if ([] == KL_ARG_V1960_413) else ((tail_call(kl_union, [KL_ARG_V1960_413[1], KL_ARG_V1961_414]) if tco_apply(kl_elementx63, [KL_ARG_V1960_413[0], KL_ARG_V1961_414]) else [KL_ARG_V1960_413[0], tco_apply(kl_union, [KL_ARG_V1960_413[1], KL_ARG_V1961_414])]) if shen_consp(KL_ARG_V1960_413) else (tail_call(shen_sysx45error, [symdic.symdic_kl_union]) if True else shen_simple_error('condition failure'))))
shen_add_fun('union', kl_union, 2)

@tail_recursion
def kl_yx45orx45nx63(KL_ARG_V1962_415):

    class KL_Context:
        KL_LOC_Message_416 = None
        KL_LOC_Yx45orx45N_417 = None
        KL_LOC_Input_418 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Message_416', tco_apply(shen_prhush, [tco_apply(shen_procx45nl, [KL_ARG_V1962_415]), tco_apply(kl_stoutput, [])])), [setattr(KL_CTX, 'KL_LOC_Yx45orx45N_417', tco_apply(shen_prhush, [' (y/n) ', tco_apply(kl_stoutput, [])])), [setattr(KL_CTX, 'KL_LOC_Input_418', tco_apply(shen_app, [tco_apply(kl_input, []), '', symdic.symdic_shen_s])), (True if ('y' == KL_CTX.KL_LOC_Input_418) else (False if ('n' == KL_CTX.KL_LOC_Input_418) else [tco_apply(shen_prhush, ['please answer y or n\r\n', tco_apply(kl_stoutput, [])]), tail_call(kl_yx45orx45nx63, [KL_ARG_V1962_415])][(-1)]))][(-1)]][(-1)]][(-1)]
shen_add_fun('y-or-n?', kl_yx45orx45nx63, 1)

@tail_recursion
def kl_not(KL_ARG_V1963_419):
    global symdic
    return (False if KL_ARG_V1963_419 else True)
shen_add_fun('not', kl_not, 1)

@tail_recursion
def kl_subst(KL_ARG_V1972_420, KL_ARG_V1973_421, KL_ARG_V1974_422):
    global symdic
    return (KL_ARG_V1972_420 if (KL_ARG_V1974_422 == KL_ARG_V1973_421) else ([tco_apply(kl_subst, [KL_ARG_V1972_420, KL_ARG_V1973_421, KL_ARG_V1974_422[0]]), tco_apply(kl_subst, [KL_ARG_V1972_420, KL_ARG_V1973_421, KL_ARG_V1974_422[1]])] if shen_consp(KL_ARG_V1974_422) else (KL_ARG_V1974_422 if True else shen_simple_error('condition failure'))))
shen_add_fun('subst', kl_subst, 3)

@tail_recursion
def kl_explode(KL_ARG_V1976_423):
    global symdic
    return tail_call(shen_explodex45h, [tco_apply(shen_app, [KL_ARG_V1976_423, '', symdic.symdic_shen_a])])
shen_add_fun('explode', kl_explode, 1)

@tail_recursion
def shen_explodex45h(KL_ARG_V1977_424):
    global symdic
    return ([] if ('' == KL_ARG_V1977_424) else ([KL_ARG_V1977_424[0], tco_apply(shen_explodex45h, [KL_ARG_V1977_424[1:]])] if tco_apply(shen_x43stringx63, [KL_ARG_V1977_424]) else (tail_call(shen_sysx45error, [symdic.symdic_shen_explodex45h]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.explode-h', shen_explodex45h, 1)

@tail_recursion
def kl_cd(KL_ARG_V1978_425):
    global symdic
    return shen_set(symdic.symdic_kl_x42homex45directoryx42, ('' if (KL_ARG_V1978_425 == '') else tco_apply(shen_app, [KL_ARG_V1978_425, '/', symdic.symdic_shen_a])))
shen_add_fun('cd', kl_cd, 1)

@tail_recursion
def kl_map(KL_ARG_V1979_426, KL_ARG_V1980_427):
    global symdic
    return tail_call(shen_mapx45h, [KL_ARG_V1979_426, KL_ARG_V1980_427, []])
shen_add_fun('map', kl_map, 2)

@tail_recursion
def shen_mapx45h(KL_ARG_V1983_428, KL_ARG_V1984_429, KL_ARG_V1985_430):
    global symdic
    return (tail_call(kl_reverse, [KL_ARG_V1985_430]) if ([] == KL_ARG_V1984_429) else (tail_call(shen_mapx45h, [KL_ARG_V1983_428, KL_ARG_V1984_429[1], [shen_apply(KL_ARG_V1983_428, [KL_ARG_V1984_429[0]]), KL_ARG_V1985_430]]) if shen_consp(KL_ARG_V1984_429) else (tail_call(shen_sysx45error, [symdic.symdic_shen_mapx45h]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.map-h', shen_mapx45h, 3)

@tail_recursion
def kl_length(KL_ARG_V1986_431):
    global symdic
    return tail_call(shen_lengthx45h, [KL_ARG_V1986_431, 0])
shen_add_fun('length', kl_length, 1)

@tail_recursion
def shen_lengthx45h(KL_ARG_V1987_432, KL_ARG_V1988_433):
    global symdic
    return (KL_ARG_V1988_433 if ([] == KL_ARG_V1987_432) else (tail_call(shen_lengthx45h, [KL_ARG_V1987_432[1], (KL_ARG_V1988_433 + 1)]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.length-h', shen_lengthx45h, 2)

@tail_recursion
def kl_occurrences(KL_ARG_V1997_434, KL_ARG_V1998_435):
    global symdic
    return (1 if (KL_ARG_V1998_435 == KL_ARG_V1997_434) else ((tco_apply(kl_occurrences, [KL_ARG_V1997_434, KL_ARG_V1998_435[0]]) + tco_apply(kl_occurrences, [KL_ARG_V1997_434, KL_ARG_V1998_435[1]])) if shen_consp(KL_ARG_V1998_435) else (0 if True else shen_simple_error('condition failure'))))
shen_add_fun('occurrences', kl_occurrences, 2)

@tail_recursion
def kl_nth(KL_ARG_V2006_436, KL_ARG_V2007_437):
    global symdic
    return (KL_ARG_V2007_437[0] if (shen_consp(KL_ARG_V2007_437) if (1 == KL_ARG_V2006_436) else False) else (tail_call(kl_nth, [(KL_ARG_V2006_436 - 1), KL_ARG_V2007_437[1]]) if shen_consp(KL_ARG_V2007_437) else (tail_call(shen_sysx45error, [symdic.symdic_kl_nth]) if True else shen_simple_error('condition failure'))))
shen_add_fun('nth', kl_nth, 2)

@tail_recursion
def kl_integerx63(KL_ARG_V2008_438):

    class KL_Context:
        KL_LOC_Abs_439 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_Abs_439', tco_apply(shen_abs, [KL_ARG_V2008_438])), tail_call(shen_integerx45testx63, [KL_CTX.KL_LOC_Abs_439, tco_apply(shen_magless, [KL_CTX.KL_LOC_Abs_439, 1])])][(-1)] if isinstance(KL_ARG_V2008_438, numbers.Number) else False)
shen_add_fun('integer?', kl_integerx63, 1)

@tail_recursion
def shen_abs(KL_ARG_V2009_440):
    global symdic
    return (KL_ARG_V2009_440 if (KL_ARG_V2009_440 > 0) else (0 - KL_ARG_V2009_440))
shen_add_fun('shen.abs', shen_abs, 1)

@tail_recursion
def shen_magless(KL_ARG_V2010_441, KL_ARG_V2011_442):

    class KL_Context:
        KL_LOC_Nx2_443 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Nx2_443', (KL_ARG_V2011_442 * 2)), (KL_ARG_V2011_442 if (KL_CTX.KL_LOC_Nx2_443 > KL_ARG_V2010_441) else tail_call(shen_magless, [KL_ARG_V2010_441, KL_CTX.KL_LOC_Nx2_443]))][(-1)]
shen_add_fun('shen.magless', shen_magless, 2)

@tail_recursion
def shen_integerx45testx63(KL_ARG_V2015_444, KL_ARG_V2016_445):

    class KL_Context:
        KL_LOC_Absx45N_446 = None
    KL_CTX = KL_Context()
    global symdic
    return (True if (0 == KL_ARG_V2015_444) else (False if (1 > KL_ARG_V2015_444) else ([setattr(KL_CTX, 'KL_LOC_Absx45N_446', (KL_ARG_V2015_444 - KL_ARG_V2016_445)), (tail_call(kl_integerx63, [KL_ARG_V2015_444]) if (0 > KL_CTX.KL_LOC_Absx45N_446) else tail_call(shen_integerx45testx63, [KL_CTX.KL_LOC_Absx45N_446, KL_ARG_V2016_445]))][(-1)] if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.integer-test?', shen_integerx45testx63, 2)

@tail_recursion
def kl_mapcan(KL_ARG_V2019_447, KL_ARG_V2020_448):
    global symdic
    return ([] if ([] == KL_ARG_V2020_448) else (tail_call(kl_append, [shen_apply(KL_ARG_V2019_447, [KL_ARG_V2020_448[0]]), tco_apply(kl_mapcan, [KL_ARG_V2019_447, KL_ARG_V2020_448[1]])]) if shen_consp(KL_ARG_V2020_448) else (tail_call(shen_sysx45error, [symdic.symdic_kl_mapcan]) if True else shen_simple_error('condition failure'))))
shen_add_fun('mapcan', kl_mapcan, 2)

@tail_recursion
def kl_readx45filex45asx45bytelist(KL_ARG_V2021_449):

    class KL_Context:
        KL_LOC_Stream_450 = None
        KL_LOC_Byte_451 = None
        KL_LOC_Bytes_452 = None
        KL_LOC_Close_453 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Stream_450', shen_open(symdic.symdic_kl_file, KL_ARG_V2021_449, symdic.symdic_kl_in)), [setattr(KL_CTX, 'KL_LOC_Byte_451', shen_read_byte(KL_CTX.KL_LOC_Stream_450)), [setattr(KL_CTX, 'KL_LOC_Bytes_452', tco_apply(shen_readx45filex45asx45bytelistx45help, [KL_CTX.KL_LOC_Stream_450, KL_CTX.KL_LOC_Byte_451, []])), [setattr(KL_CTX, 'KL_LOC_Close_453', shen_close(KL_CTX.KL_LOC_Stream_450)), tail_call(kl_reverse, [KL_CTX.KL_LOC_Bytes_452])][(-1)]][(-1)]][(-1)]][(-1)]
shen_add_fun('read-file-as-bytelist', kl_readx45filex45asx45bytelist, 1)

@tail_recursion
def shen_readx45filex45asx45bytelistx45help(KL_ARG_V2022_454, KL_ARG_V2023_455, KL_ARG_V2024_456):
    global symdic
    return (KL_ARG_V2024_456 if ((-1) == KL_ARG_V2023_455) else (tail_call(shen_readx45filex45asx45bytelistx45help, [KL_ARG_V2022_454, shen_read_byte(KL_ARG_V2022_454), [KL_ARG_V2023_455, KL_ARG_V2024_456]]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.read-file-as-bytelist-help', shen_readx45filex45asx45bytelistx45help, 3)

@tail_recursion
def kl_readx45filex45asx45string(KL_ARG_V2025_457):

    class KL_Context:
        KL_LOC_Stream_458 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Stream_458', shen_open(symdic.symdic_kl_file, KL_ARG_V2025_457, symdic.symdic_kl_in)), tail_call(shen_rfasx45h, [KL_CTX.KL_LOC_Stream_458, shen_read_byte(KL_CTX.KL_LOC_Stream_458), ''])][(-1)]
shen_add_fun('read-file-as-string', kl_readx45filex45asx45string, 1)

@tail_recursion
def shen_rfasx45h(KL_ARG_V2026_459, KL_ARG_V2027_460, KL_ARG_V2028_461):
    global symdic
    return ([shen_close(KL_ARG_V2026_459), KL_ARG_V2028_461][(-1)] if ((-1) == KL_ARG_V2027_460) else (tail_call(shen_rfasx45h, [KL_ARG_V2026_459, shen_read_byte(KL_ARG_V2026_459), (KL_ARG_V2028_461 + chr(KL_ARG_V2027_460))]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.rfas-h', shen_rfasx45h, 3)

@tail_recursion
def kl_x61x61(KL_ARG_V2037_462, KL_ARG_V2038_463):
    global symdic
    return (True if (KL_ARG_V2038_463 == KL_ARG_V2037_462) else (False if True else shen_simple_error('condition failure')))
shen_add_fun('==', kl_x61x61, 2)

@tail_recursion
def kl_abort():
    global symdic
    return shen_simple_error('')
shen_add_fun('abort', kl_abort, 0)

@tail_recursion
def kl_read():
    global symdic
    return tco_apply(kl_lineread, [])[0]
shen_add_fun('read', kl_read, 0)

@tail_recursion
def kl_input():
    global symdic
    return tail_call(kl_eval, [tco_apply(kl_read, [])])
shen_add_fun('input', kl_input, 0)

@tail_recursion
def kl_inputx43(KL_ARG_V2044_464, KL_ARG_V2045_465):

    class KL_Context:
        KL_LOC_Input_466 = None
        KL_LOC_Check_467 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Input_466', tco_apply(kl_read, [])), [setattr(KL_CTX, 'KL_LOC_Check_467', tco_apply(shen_typecheck, [KL_CTX.KL_LOC_Input_466, KL_ARG_V2045_465])), ([tco_apply(shen_prhush, [('input is not of type ' + tco_apply(shen_app, [KL_ARG_V2045_465, ': please re-enter ', symdic.symdic_shen_r])), tco_apply(kl_stoutput, [])]), tail_call(kl_inputx43, [symdic.symdic_kl_x58, KL_ARG_V2045_465])][(-1)] if (False == KL_CTX.KL_LOC_Check_467) else tail_call(kl_eval, [KL_CTX.KL_LOC_Input_466]))][(-1)]][(-1)]
shen_add_fun('input+', kl_inputx43, 2)

@tail_recursion
def readx43(KL_ARG_V2050_468, KL_ARG_V2051_469):

    class KL_Context:
        KL_LOC_Input_470 = None
        KL_LOC_Check_471 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Input_470', tco_apply(kl_read, [])), [setattr(KL_CTX, 'KL_LOC_Check_471', tco_apply(shen_typecheck, [tco_apply(shen_rcons_form, [KL_CTX.KL_LOC_Input_470]), KL_ARG_V2051_469])), ([tco_apply(shen_prhush, [('input is not of type ' + tco_apply(shen_app, [KL_ARG_V2051_469, ': please re-enter ', symdic.symdic_shen_r])), tco_apply(kl_stoutput, [])]), tail_call(readx43, [symdic.symdic_kl_x58, KL_ARG_V2051_469])][(-1)] if (False == KL_CTX.KL_LOC_Check_471) else KL_CTX.KL_LOC_Input_470)][(-1)]][(-1)]
shen_add_fun('read+', readx43, 2)

@tail_recursion
def kl_boundx63(KL_ARG_V2052_472):

    class KL_Context:
        KL_LOC_Val_473 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_Val_473', shen_try_except((lambda : shen_get(KL_ARG_V2052_472)), (lambda KL_ARG_E_474: symdic.symdic_shen_thisx45symbolx45isx45unbound))), (False if (KL_CTX.KL_LOC_Val_473 == symdic.symdic_shen_thisx45symbolx45isx45unbound) else True)][(-1)] if tco_apply(kl_symbolx63, [KL_ARG_V2052_472]) else False)
shen_add_fun('bound?', kl_boundx63, 1)

@tail_recursion
def shen_stringx45x62bytes(KL_ARG_V2053_475):
    global symdic
    return ([] if ('' == KL_ARG_V2053_475) else ([ord(KL_ARG_V2053_475[0]), tco_apply(shen_stringx45x62bytes, [KL_ARG_V2053_475[1:]])] if True else shen_simple_error('condition failure')))
shen_add_fun('shen.string->bytes', shen_stringx45x62bytes, 1)

@tail_recursion
def kl_maxinferences(KL_ARG_V2054_476):
    global symdic
    return shen_set(symdic.symdic_shen_x42maxinferencesx42, KL_ARG_V2054_476)
shen_add_fun('maxinferences', kl_maxinferences, 1)

@tail_recursion
def kl_inferences():
    global symdic
    return shen_get(symdic.symdic_shen_x42infsx42)
shen_add_fun('inferences', kl_inferences, 0)

@tail_recursion
def kl_protect(KL_ARG_V2055_477):
    global symdic
    return KL_ARG_V2055_477
shen_add_fun('protect', kl_protect, 1)

@tail_recursion
def kl_stoutput():
    global symdic
    return shen_get(symdic.symdic_x42stoutputx42)
shen_add_fun('stoutput', kl_stoutput, 0)

@tail_recursion
def kl_stringx45x62symbol(KL_ARG_V2056_478):

    class KL_Context:
        KL_LOC_Symbol_479 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Symbol_479', shen_intern(KL_ARG_V2056_478)), (KL_CTX.KL_LOC_Symbol_479 if tco_apply(kl_symbolx63, [KL_CTX.KL_LOC_Symbol_479]) else shen_simple_error(('cannot intern ' + tco_apply(shen_app, [KL_ARG_V2056_478, ' to a symbol', symdic.symdic_shen_s]))))][(-1)]
shen_add_fun('string->symbol', kl_stringx45x62symbol, 1)

@tail_recursion
def shen_optimise(KL_ARG_V2061_480):
    global symdic
    return (shen_set(symdic.symdic_shen_x42optimisex42, True) if (symdic.symdic_kl_x43 == KL_ARG_V2061_480) else (shen_set(symdic.symdic_shen_x42optimisex42, False) if (symdic.symdic_kl_x45 == KL_ARG_V2061_480) else (shen_simple_error('optimise expects a + or a -.\r\n') if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.optimise', shen_optimise, 1)


#============================== sequent.kl==============================



@tail_recursion
def shen_datatypex45error(KL_ARG_V1612_481):
    global symdic
    return (shen_simple_error(('datatype syntax error here:\r\n\r\n ' + tco_apply(shen_app, [tco_apply(shen_nextx4550, [50, KL_ARG_V1612_481[0]]), '\r\n', symdic.symdic_shen_a]))) if ((([] == KL_ARG_V1612_481[1][1]) if shen_consp(KL_ARG_V1612_481[1]) else False) if shen_consp(KL_ARG_V1612_481) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_datatypex45error]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.datatype-error', shen_datatypex45error, 1)

@tail_recursion
def shen_x60datatypex45rulesx62(KL_ARG_V1617_482):

    class KL_Context:
        KL_LOC_Result_483 = None
        KL_LOC_Parse_shen_x60datatypex45rulex62_484 = None
        KL_LOC_Parse_shen_x60datatypex45rulesx62_485 = None
        KL_LOC_Result_486 = None
        KL_LOC_Parse_x60ex62_487 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_483', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60datatypex45rulex62_484', tco_apply(shen_x60datatypex45rulex62, [KL_ARG_V1617_482])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60datatypex45rulesx62_485', tco_apply(shen_x60datatypex45rulesx62, [KL_CTX.KL_LOC_Parse_shen_x60datatypex45rulex62_484])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60datatypex45rulesx62_485[0], [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60datatypex45rulex62_484]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60datatypex45rulesx62_485])]]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60datatypex45rulesx62_485)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60datatypex45rulex62_484)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_486', [setattr(KL_CTX, 'KL_LOC_Parse_x60ex62_487', tco_apply(kl_x60ex62, [KL_ARG_V1617_482])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_x60ex62_487[0], []]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_x60ex62_487)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_486 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_486)][(-1)] if (KL_CTX.KL_LOC_Result_483 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_483)][(-1)]
shen_add_fun('shen.<datatype-rules>', shen_x60datatypex45rulesx62, 1)

@tail_recursion
def shen_x60datatypex45rulex62(KL_ARG_V1622_488):

    class KL_Context:
        KL_LOC_Result_489 = None
        KL_LOC_Parse_shen_x60sidex45conditionsx62_490 = None
        KL_LOC_Parse_shen_x60premisesx62_491 = None
        KL_LOC_Parse_shen_x60singleunderlinex62_492 = None
        KL_LOC_Parse_shen_x60conclusionx62_493 = None
        KL_LOC_Result_494 = None
        KL_LOC_Parse_shen_x60sidex45conditionsx62_495 = None
        KL_LOC_Parse_shen_x60premisesx62_496 = None
        KL_LOC_Parse_shen_x60doubleunderlinex62_497 = None
        KL_LOC_Parse_shen_x60conclusionx62_498 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_489', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60sidex45conditionsx62_490', tco_apply(shen_x60sidex45conditionsx62, [KL_ARG_V1622_488])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60premisesx62_491', tco_apply(shen_x60premisesx62, [KL_CTX.KL_LOC_Parse_shen_x60sidex45conditionsx62_490])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60singleunderlinex62_492', tco_apply(shen_x60singleunderlinex62, [KL_CTX.KL_LOC_Parse_shen_x60premisesx62_491])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60conclusionx62_493', tco_apply(shen_x60conclusionx62, [KL_CTX.KL_LOC_Parse_shen_x60singleunderlinex62_492])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60conclusionx62_493[0], tco_apply(shen_sequent, [symdic.symdic_shen_single, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60sidex45conditionsx62_490]), [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60premisesx62_491]), [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60conclusionx62_493]), []]]]])]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60conclusionx62_493)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60singleunderlinex62_492)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60premisesx62_491)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60sidex45conditionsx62_490)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_494', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60sidex45conditionsx62_495', tco_apply(shen_x60sidex45conditionsx62, [KL_ARG_V1622_488])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60premisesx62_496', tco_apply(shen_x60premisesx62, [KL_CTX.KL_LOC_Parse_shen_x60sidex45conditionsx62_495])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60doubleunderlinex62_497', tco_apply(shen_x60doubleunderlinex62, [KL_CTX.KL_LOC_Parse_shen_x60premisesx62_496])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60conclusionx62_498', tco_apply(shen_x60conclusionx62, [KL_CTX.KL_LOC_Parse_shen_x60doubleunderlinex62_497])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60conclusionx62_498[0], tco_apply(shen_sequent, [symdic.symdic_shen_double, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60sidex45conditionsx62_495]), [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60premisesx62_496]), [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60conclusionx62_498]), []]]]])]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60conclusionx62_498)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60doubleunderlinex62_497)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60premisesx62_496)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60sidex45conditionsx62_495)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_494 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_494)][(-1)] if (KL_CTX.KL_LOC_Result_489 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_489)][(-1)]
shen_add_fun('shen.<datatype-rule>', shen_x60datatypex45rulex62, 1)

@tail_recursion
def shen_x60sidex45conditionsx62(KL_ARG_V1627_499):

    class KL_Context:
        KL_LOC_Result_500 = None
        KL_LOC_Parse_shen_x60sidex45conditionx62_501 = None
        KL_LOC_Parse_shen_x60sidex45conditionsx62_502 = None
        KL_LOC_Result_503 = None
        KL_LOC_Parse_x60ex62_504 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_500', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60sidex45conditionx62_501', tco_apply(shen_x60sidex45conditionx62, [KL_ARG_V1627_499])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60sidex45conditionsx62_502', tco_apply(shen_x60sidex45conditionsx62, [KL_CTX.KL_LOC_Parse_shen_x60sidex45conditionx62_501])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60sidex45conditionsx62_502[0], [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60sidex45conditionx62_501]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60sidex45conditionsx62_502])]]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60sidex45conditionsx62_502)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60sidex45conditionx62_501)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_503', [setattr(KL_CTX, 'KL_LOC_Parse_x60ex62_504', tco_apply(kl_x60ex62, [KL_ARG_V1627_499])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_x60ex62_504[0], []]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_x60ex62_504)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_503 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_503)][(-1)] if (KL_CTX.KL_LOC_Result_500 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_500)][(-1)]
shen_add_fun('shen.<side-conditions>', shen_x60sidex45conditionsx62, 1)

@tail_recursion
def shen_x60sidex45conditionx62(KL_ARG_V1632_505):

    class KL_Context:
        KL_LOC_Result_506 = None
        KL_LOC_Parse_shen_x60exprx62_507 = None
        KL_LOC_Result_508 = None
        KL_LOC_Parse_shen_x60variablex63x62_509 = None
        KL_LOC_Parse_shen_x60exprx62_510 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_506', ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60exprx62_507', tco_apply(shen_x60exprx62, [tco_apply(shen_pair, [KL_ARG_V1632_505[0][1], tco_apply(shen_hdtl, [KL_ARG_V1632_505])])])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60exprx62_507[0], [symdic.symdic_kl_if, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60exprx62_507]), []]]]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60exprx62_507)) else tco_apply(kl_fail, []))][(-1)] if ((symdic.symdic_kl_if == KL_ARG_V1632_505[0][0]) if shen_consp(KL_ARG_V1632_505[0]) else False) else tco_apply(kl_fail, []))), ([setattr(KL_CTX, 'KL_LOC_Result_508', ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60variablex63x62_509', tco_apply(shen_x60variablex63x62, [tco_apply(shen_pair, [KL_ARG_V1632_505[0][1], tco_apply(shen_hdtl, [KL_ARG_V1632_505])])])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60exprx62_510', tco_apply(shen_x60exprx62, [KL_CTX.KL_LOC_Parse_shen_x60variablex63x62_509])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60exprx62_510[0], [symdic.symdic_kl_let, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60variablex63x62_509]), [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60exprx62_510]), []]]]]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60exprx62_510)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60variablex63x62_509)) else tco_apply(kl_fail, []))][(-1)] if ((symdic.symdic_kl_let == KL_ARG_V1632_505[0][0]) if shen_consp(KL_ARG_V1632_505[0]) else False) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_508 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_508)][(-1)] if (KL_CTX.KL_LOC_Result_506 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_506)][(-1)]
shen_add_fun('shen.<side-condition>', shen_x60sidex45conditionx62, 1)

@tail_recursion
def shen_x60variablex63x62(KL_ARG_V1637_511):

    class KL_Context:
        KL_LOC_Result_512 = None
        KL_LOC_Parse_X_513 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_512', ([setattr(KL_CTX, 'KL_LOC_Parse_X_513', KL_ARG_V1637_511[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1637_511[0][1], tco_apply(shen_hdtl, [KL_ARG_V1637_511])])[0], KL_CTX.KL_LOC_Parse_X_513]) if tco_apply(kl_variablex63, [KL_CTX.KL_LOC_Parse_X_513]) else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V1637_511[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_512 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_512)][(-1)]
shen_add_fun('shen.<variable?>', shen_x60variablex63x62, 1)

@tail_recursion
def shen_x60exprx62(KL_ARG_V1642_514):

    class KL_Context:
        KL_LOC_Result_515 = None
        KL_LOC_Parse_X_516 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_515', ([setattr(KL_CTX, 'KL_LOC_Parse_X_516', KL_ARG_V1642_514[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1642_514[0][1], tco_apply(shen_hdtl, [KL_ARG_V1642_514])])[0], tco_apply(shen_removex45bar, [KL_CTX.KL_LOC_Parse_X_516])]) if (not (True if tco_apply(kl_elementx63, [KL_CTX.KL_LOC_Parse_X_516, [symdic.symdic_kl_x62x62, [symdic.symdic_kl_x59, []]]]) else (True if tco_apply(shen_singleunderlinex63, [KL_CTX.KL_LOC_Parse_X_516]) else tco_apply(shen_doubleunderlinex63, [KL_CTX.KL_LOC_Parse_X_516])))) else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V1642_514[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_515 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_515)][(-1)]
shen_add_fun('shen.<expr>', shen_x60exprx62, 1)

@tail_recursion
def shen_removex45bar(KL_ARG_V1643_517):
    global symdic
    return ([KL_ARG_V1643_517[0], KL_ARG_V1643_517[1][1][0]] if (((((KL_ARG_V1643_517[1][0] == symdic.symdic_kl_barx33) if ([] == KL_ARG_V1643_517[1][1][1]) else False) if shen_consp(KL_ARG_V1643_517[1][1]) else False) if shen_consp(KL_ARG_V1643_517[1]) else False) if shen_consp(KL_ARG_V1643_517) else False) else ([tco_apply(shen_removex45bar, [KL_ARG_V1643_517[0]]), tco_apply(shen_removex45bar, [KL_ARG_V1643_517[1]])] if shen_consp(KL_ARG_V1643_517) else (KL_ARG_V1643_517 if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.remove-bar', shen_removex45bar, 1)

@tail_recursion
def shen_x60premisesx62(KL_ARG_V1648_518):

    class KL_Context:
        KL_LOC_Result_519 = None
        KL_LOC_Parse_shen_x60premisex62_520 = None
        KL_LOC_Parse_shen_x60semicolonx45symbolx62_521 = None
        KL_LOC_Parse_shen_x60premisesx62_522 = None
        KL_LOC_Result_523 = None
        KL_LOC_Parse_x60ex62_524 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_519', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60premisex62_520', tco_apply(shen_x60premisex62, [KL_ARG_V1648_518])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60semicolonx45symbolx62_521', tco_apply(shen_x60semicolonx45symbolx62, [KL_CTX.KL_LOC_Parse_shen_x60premisex62_520])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60premisesx62_522', tco_apply(shen_x60premisesx62, [KL_CTX.KL_LOC_Parse_shen_x60semicolonx45symbolx62_521])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60premisesx62_522[0], [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60premisex62_520]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60premisesx62_522])]]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60premisesx62_522)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60semicolonx45symbolx62_521)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60premisex62_520)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_523', [setattr(KL_CTX, 'KL_LOC_Parse_x60ex62_524', tco_apply(kl_x60ex62, [KL_ARG_V1648_518])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_x60ex62_524[0], []]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_x60ex62_524)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_523 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_523)][(-1)] if (KL_CTX.KL_LOC_Result_519 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_519)][(-1)]
shen_add_fun('shen.<premises>', shen_x60premisesx62, 1)

@tail_recursion
def shen_x60semicolonx45symbolx62(KL_ARG_V1653_525):

    class KL_Context:
        KL_LOC_Result_526 = None
        KL_LOC_Parse_X_527 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_526', ([setattr(KL_CTX, 'KL_LOC_Parse_X_527', KL_ARG_V1653_525[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1653_525[0][1], tco_apply(shen_hdtl, [KL_ARG_V1653_525])])[0], symdic.symdic_shen_skip]) if (KL_CTX.KL_LOC_Parse_X_527 == symdic.symdic_kl_x59) else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V1653_525[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_526 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_526)][(-1)]
shen_add_fun('shen.<semicolon-symbol>', shen_x60semicolonx45symbolx62, 1)

@tail_recursion
def shen_x60premisex62(KL_ARG_V1658_528):

    class KL_Context:
        KL_LOC_Result_529 = None
        KL_LOC_Result_530 = None
        KL_LOC_Parse_shen_x60formulaex62_531 = None
        KL_LOC_Parse_shen_x60formulax62_532 = None
        KL_LOC_Result_533 = None
        KL_LOC_Parse_shen_x60formulax62_534 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_529', (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1658_528[0][1], tco_apply(shen_hdtl, [KL_ARG_V1658_528])])[0], symdic.symdic_kl_x33]) if ((symdic.symdic_kl_x33 == KL_ARG_V1658_528[0][0]) if shen_consp(KL_ARG_V1658_528[0]) else False) else tco_apply(kl_fail, []))), ([setattr(KL_CTX, 'KL_LOC_Result_530', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60formulaex62_531', tco_apply(shen_x60formulaex62, [KL_ARG_V1658_528])), (([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60formulax62_532', tco_apply(shen_x60formulax62, [tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60formulaex62_531[0][1], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60formulaex62_531])])])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60formulax62_532[0], tco_apply(shen_sequent, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60formulaex62_531]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60formulax62_532])])]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60formulax62_532)) else tco_apply(kl_fail, []))][(-1)] if ((symdic.symdic_kl_x62x62 == KL_CTX.KL_LOC_Parse_shen_x60formulaex62_531[0][0]) if shen_consp(KL_CTX.KL_LOC_Parse_shen_x60formulaex62_531[0]) else False) else tco_apply(kl_fail, [])) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60formulaex62_531)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_533', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60formulax62_534', tco_apply(shen_x60formulax62, [KL_ARG_V1658_528])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60formulax62_534[0], tco_apply(shen_sequent, [[], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60formulax62_534])])]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60formulax62_534)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_533 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_533)][(-1)] if (KL_CTX.KL_LOC_Result_530 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_530)][(-1)] if (KL_CTX.KL_LOC_Result_529 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_529)][(-1)]
shen_add_fun('shen.<premise>', shen_x60premisex62, 1)

@tail_recursion
def shen_x60conclusionx62(KL_ARG_V1663_535):

    class KL_Context:
        KL_LOC_Result_536 = None
        KL_LOC_Parse_shen_x60formulaex62_537 = None
        KL_LOC_Parse_shen_x60formulax62_538 = None
        KL_LOC_Parse_shen_x60semicolonx45symbolx62_539 = None
        KL_LOC_Result_540 = None
        KL_LOC_Parse_shen_x60formulax62_541 = None
        KL_LOC_Parse_shen_x60semicolonx45symbolx62_542 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_536', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60formulaex62_537', tco_apply(shen_x60formulaex62, [KL_ARG_V1663_535])), (([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60formulax62_538', tco_apply(shen_x60formulax62, [tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60formulaex62_537[0][1], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60formulaex62_537])])])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60semicolonx45symbolx62_539', tco_apply(shen_x60semicolonx45symbolx62, [KL_CTX.KL_LOC_Parse_shen_x60formulax62_538])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60semicolonx45symbolx62_539[0], tco_apply(shen_sequent, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60formulaex62_537]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60formulax62_538])])]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60semicolonx45symbolx62_539)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60formulax62_538)) else tco_apply(kl_fail, []))][(-1)] if ((symdic.symdic_kl_x62x62 == KL_CTX.KL_LOC_Parse_shen_x60formulaex62_537[0][0]) if shen_consp(KL_CTX.KL_LOC_Parse_shen_x60formulaex62_537[0]) else False) else tco_apply(kl_fail, [])) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60formulaex62_537)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_540', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60formulax62_541', tco_apply(shen_x60formulax62, [KL_ARG_V1663_535])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60semicolonx45symbolx62_542', tco_apply(shen_x60semicolonx45symbolx62, [KL_CTX.KL_LOC_Parse_shen_x60formulax62_541])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60semicolonx45symbolx62_542[0], tco_apply(shen_sequent, [[], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60formulax62_541])])]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60semicolonx45symbolx62_542)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60formulax62_541)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_540 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_540)][(-1)] if (KL_CTX.KL_LOC_Result_536 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_536)][(-1)]
shen_add_fun('shen.<conclusion>', shen_x60conclusionx62, 1)

@tail_recursion
def shen_sequent(KL_ARG_V1664_543, KL_ARG_V1665_544):
    global symdic
    return tail_call(kl_x64p, [KL_ARG_V1664_543, KL_ARG_V1665_544])
shen_add_fun('shen.sequent', shen_sequent, 2)

@tail_recursion
def shen_x60formulaex62(KL_ARG_V1670_545):

    class KL_Context:
        KL_LOC_Result_546 = None
        KL_LOC_Parse_shen_x60formulax62_547 = None
        KL_LOC_Parse_shen_x60commax45symbolx62_548 = None
        KL_LOC_Parse_shen_x60formulaex62_549 = None
        KL_LOC_Result_550 = None
        KL_LOC_Parse_shen_x60formulax62_551 = None
        KL_LOC_Result_552 = None
        KL_LOC_Parse_x60ex62_553 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_546', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60formulax62_547', tco_apply(shen_x60formulax62, [KL_ARG_V1670_545])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60commax45symbolx62_548', tco_apply(shen_x60commax45symbolx62, [KL_CTX.KL_LOC_Parse_shen_x60formulax62_547])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60formulaex62_549', tco_apply(shen_x60formulaex62, [KL_CTX.KL_LOC_Parse_shen_x60commax45symbolx62_548])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60formulaex62_549[0], [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60formulax62_547]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60formulaex62_549])]]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60formulaex62_549)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60commax45symbolx62_548)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60formulax62_547)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_550', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60formulax62_551', tco_apply(shen_x60formulax62, [KL_ARG_V1670_545])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60formulax62_551[0], [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60formulax62_551]), []]]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60formulax62_551)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_552', [setattr(KL_CTX, 'KL_LOC_Parse_x60ex62_553', tco_apply(kl_x60ex62, [KL_ARG_V1670_545])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_x60ex62_553[0], []]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_x60ex62_553)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_552 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_552)][(-1)] if (KL_CTX.KL_LOC_Result_550 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_550)][(-1)] if (KL_CTX.KL_LOC_Result_546 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_546)][(-1)]
shen_add_fun('shen.<formulae>', shen_x60formulaex62, 1)

@tail_recursion
def shen_x60commax45symbolx62(KL_ARG_V1675_554):

    class KL_Context:
        KL_LOC_Result_555 = None
        KL_LOC_Parse_X_556 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_555', ([setattr(KL_CTX, 'KL_LOC_Parse_X_556', KL_ARG_V1675_554[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1675_554[0][1], tco_apply(shen_hdtl, [KL_ARG_V1675_554])])[0], symdic.symdic_shen_skip]) if (KL_CTX.KL_LOC_Parse_X_556 == shen_intern(',')) else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V1675_554[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_555 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_555)][(-1)]
shen_add_fun('shen.<comma-symbol>', shen_x60commax45symbolx62, 1)

@tail_recursion
def shen_x60formulax62(KL_ARG_V1680_557):

    class KL_Context:
        KL_LOC_Result_558 = None
        KL_LOC_Parse_shen_x60exprx62_559 = None
        KL_LOC_Parse_shen_x60typex62_560 = None
        KL_LOC_Result_561 = None
        KL_LOC_Parse_shen_x60exprx62_562 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_558', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60exprx62_559', tco_apply(shen_x60exprx62, [KL_ARG_V1680_557])), (([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60typex62_560', tco_apply(shen_x60typex62, [tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60exprx62_559[0][1], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60exprx62_559])])])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60typex62_560[0], [tco_apply(shen_curry, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60exprx62_559])]), [symdic.symdic_kl_x58, [tco_apply(shen_demodulate, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60typex62_560])]), []]]]]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60typex62_560)) else tco_apply(kl_fail, []))][(-1)] if ((symdic.symdic_kl_x58 == KL_CTX.KL_LOC_Parse_shen_x60exprx62_559[0][0]) if shen_consp(KL_CTX.KL_LOC_Parse_shen_x60exprx62_559[0]) else False) else tco_apply(kl_fail, [])) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60exprx62_559)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_561', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60exprx62_562', tco_apply(shen_x60exprx62, [KL_ARG_V1680_557])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60exprx62_562[0], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60exprx62_562])]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60exprx62_562)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_561 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_561)][(-1)] if (KL_CTX.KL_LOC_Result_558 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_558)][(-1)]
shen_add_fun('shen.<formula>', shen_x60formulax62, 1)

@tail_recursion
def shen_x60typex62(KL_ARG_V1685_563):

    class KL_Context:
        KL_LOC_Result_564 = None
        KL_LOC_Parse_shen_x60exprx62_565 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_564', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60exprx62_565', tco_apply(shen_x60exprx62, [KL_ARG_V1685_563])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60exprx62_565[0], tco_apply(shen_curryx45type, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60exprx62_565])])]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60exprx62_565)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_564 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_564)][(-1)]
shen_add_fun('shen.<type>', shen_x60typex62, 1)

@tail_recursion
def shen_x60doubleunderlinex62(KL_ARG_V1690_566):

    class KL_Context:
        KL_LOC_Result_567 = None
        KL_LOC_Parse_X_568 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_567', ([setattr(KL_CTX, 'KL_LOC_Parse_X_568', KL_ARG_V1690_566[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1690_566[0][1], tco_apply(shen_hdtl, [KL_ARG_V1690_566])])[0], KL_CTX.KL_LOC_Parse_X_568]) if tco_apply(shen_doubleunderlinex63, [KL_CTX.KL_LOC_Parse_X_568]) else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V1690_566[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_567 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_567)][(-1)]
shen_add_fun('shen.<doubleunderline>', shen_x60doubleunderlinex62, 1)

@tail_recursion
def shen_x60singleunderlinex62(KL_ARG_V1695_569):

    class KL_Context:
        KL_LOC_Result_570 = None
        KL_LOC_Parse_X_571 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_570', ([setattr(KL_CTX, 'KL_LOC_Parse_X_571', KL_ARG_V1695_569[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1695_569[0][1], tco_apply(shen_hdtl, [KL_ARG_V1695_569])])[0], KL_CTX.KL_LOC_Parse_X_571]) if tco_apply(shen_singleunderlinex63, [KL_CTX.KL_LOC_Parse_X_571]) else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V1695_569[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_570 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_570)][(-1)]
shen_add_fun('shen.<singleunderline>', shen_x60singleunderlinex62, 1)

@tail_recursion
def shen_singleunderlinex63(KL_ARG_V1696_572):
    global symdic
    return (tail_call(shen_shx63, [str(KL_ARG_V1696_572)]) if tco_apply(kl_symbolx63, [KL_ARG_V1696_572]) else False)
shen_add_fun('shen.singleunderline?', shen_singleunderlinex63, 1)

@tail_recursion
def shen_shx63(KL_ARG_V1697_573):
    global symdic
    return (True if ('_' == KL_ARG_V1697_573) else ((tail_call(shen_shx63, [KL_ARG_V1697_573[1:]]) if (KL_ARG_V1697_573[0] == '_') else False) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.sh?', shen_shx63, 1)

@tail_recursion
def shen_doubleunderlinex63(KL_ARG_V1698_574):
    global symdic
    return (tail_call(shen_dhx63, [str(KL_ARG_V1698_574)]) if tco_apply(kl_symbolx63, [KL_ARG_V1698_574]) else False)
shen_add_fun('shen.doubleunderline?', shen_doubleunderlinex63, 1)

@tail_recursion
def shen_dhx63(KL_ARG_V1699_575):
    global symdic
    return (True if ('=' == KL_ARG_V1699_575) else ((tail_call(shen_dhx63, [KL_ARG_V1699_575[1:]]) if (KL_ARG_V1699_575[0] == '=') else False) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.dh?', shen_dhx63, 1)

@tail_recursion
def shen_processx45datatype(KL_ARG_V1700_576, KL_ARG_V1701_577):
    global symdic
    return tail_call(shen_rememberx45datatype, [tco_apply(shen_sx45prolog, [tco_apply(shen_rulesx45x62hornx45clauses, [KL_ARG_V1700_576, KL_ARG_V1701_577])])])
shen_add_fun('shen.process-datatype', shen_processx45datatype, 2)

@tail_recursion
def shen_rememberx45datatype(KL_ARG_V1706_578):
    global symdic
    return ([shen_set(symdic.symdic_shen_x42datatypesx42, tco_apply(kl_adjoin, [KL_ARG_V1706_578[0], shen_get(symdic.symdic_shen_x42datatypesx42)])), [shen_set(symdic.symdic_shen_x42alldatatypesx42, tco_apply(kl_adjoin, [KL_ARG_V1706_578[0], shen_get(symdic.symdic_shen_x42alldatatypesx42)])), KL_ARG_V1706_578[0]][(-1)]][(-1)] if shen_consp(KL_ARG_V1706_578) else (tail_call(shen_sysx45error, [symdic.symdic_shen_rememberx45datatype]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.remember-datatype', shen_rememberx45datatype, 1)

@tail_recursion
def shen_rulesx45x62hornx45clauses(KL_ARG_V1709_579, KL_ARG_V1710_580):
    global symdic
    return ([] if ([] == KL_ARG_V1710_580) else ([tco_apply(shen_rulex45x62hornx45clause, [KL_ARG_V1709_579, tco_apply(kl_snd, [KL_ARG_V1710_580[0]])]), tco_apply(shen_rulesx45x62hornx45clauses, [KL_ARG_V1709_579, KL_ARG_V1710_580[1]])] if (((symdic.symdic_shen_single == tco_apply(kl_fst, [KL_ARG_V1710_580[0]])) if tco_apply(kl_tuplex63, [KL_ARG_V1710_580[0]]) else False) if shen_consp(KL_ARG_V1710_580) else False) else (tail_call(shen_rulesx45x62hornx45clauses, [KL_ARG_V1709_579, tco_apply(kl_append, [tco_apply(shen_doublex45x62singles, [tco_apply(kl_snd, [KL_ARG_V1710_580[0]])]), KL_ARG_V1710_580[1]])]) if (((symdic.symdic_shen_double == tco_apply(kl_fst, [KL_ARG_V1710_580[0]])) if tco_apply(kl_tuplex63, [KL_ARG_V1710_580[0]]) else False) if shen_consp(KL_ARG_V1710_580) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_rulesx45x62hornx45clauses]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.rules->horn-clauses', shen_rulesx45x62hornx45clauses, 2)

@tail_recursion
def shen_doublex45x62singles(KL_ARG_V1711_581):
    global symdic
    return [tco_apply(shen_rightx45rule, [KL_ARG_V1711_581]), [tco_apply(shen_leftx45rule, [KL_ARG_V1711_581]), []]]
shen_add_fun('shen.double->singles', shen_doublex45x62singles, 1)

@tail_recursion
def shen_rightx45rule(KL_ARG_V1712_582):
    global symdic
    return tail_call(kl_x64p, [symdic.symdic_shen_single, KL_ARG_V1712_582])
shen_add_fun('shen.right-rule', shen_rightx45rule, 1)

@tail_recursion
def shen_leftx45rule(KL_ARG_V1713_583):

    class KL_Context:
        KL_LOC_Q_584 = None
        KL_LOC_NewConclusion_585 = None
        KL_LOC_NewPremises_586 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_Q_584', tco_apply(kl_gensym, [symdic.symdic_Qv])), [setattr(KL_CTX, 'KL_LOC_NewConclusion_585', tco_apply(kl_x64p, [[tco_apply(kl_snd, [KL_ARG_V1713_583[1][1][0]]), []], KL_CTX.KL_LOC_Q_584])), [setattr(KL_CTX, 'KL_LOC_NewPremises_586', [tco_apply(kl_x64p, [tco_apply(kl_map, [symdic.symdic_shen_rightx45x62left, KL_ARG_V1713_583[1][0]]), KL_CTX.KL_LOC_Q_584]), []]), tail_call(kl_x64p, [symdic.symdic_shen_single, [KL_ARG_V1713_583[0], [KL_CTX.KL_LOC_NewPremises_586, [KL_CTX.KL_LOC_NewConclusion_585, []]]]])][(-1)]][(-1)]][(-1)] if (((((([] == KL_ARG_V1713_583[1][1][1]) if ([] == tco_apply(kl_fst, [KL_ARG_V1713_583[1][1][0]])) else False) if tco_apply(kl_tuplex63, [KL_ARG_V1713_583[1][1][0]]) else False) if shen_consp(KL_ARG_V1713_583[1][1]) else False) if shen_consp(KL_ARG_V1713_583[1]) else False) if shen_consp(KL_ARG_V1713_583) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_leftx45rule]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.left-rule', shen_leftx45rule, 1)

@tail_recursion
def shen_rightx45x62left(KL_ARG_V1718_587):
    global symdic
    return (tail_call(kl_snd, [KL_ARG_V1718_587]) if (([] == tco_apply(kl_fst, [KL_ARG_V1718_587])) if tco_apply(kl_tuplex63, [KL_ARG_V1718_587]) else False) else (shen_simple_error('syntax error with ==========\r\n') if True else shen_simple_error('condition failure')))
shen_add_fun('shen.right->left', shen_rightx45x62left, 1)

@tail_recursion
def shen_rulex45x62hornx45clause(KL_ARG_V1719_588, KL_ARG_V1720_589):
    global symdic
    return ([tco_apply(shen_rulex45x62hornx45clausex45head, [KL_ARG_V1719_588, tco_apply(kl_snd, [KL_ARG_V1720_589[1][1][0]])]), [symdic.symdic_kl_x58x45, [tco_apply(shen_rulex45x62hornx45clausex45body, [KL_ARG_V1720_589[0], KL_ARG_V1720_589[1][0], tco_apply(kl_fst, [KL_ARG_V1720_589[1][1][0]])]), []]]] if ((((([] == KL_ARG_V1720_589[1][1][1]) if tco_apply(kl_tuplex63, [KL_ARG_V1720_589[1][1][0]]) else False) if shen_consp(KL_ARG_V1720_589[1][1]) else False) if shen_consp(KL_ARG_V1720_589[1]) else False) if shen_consp(KL_ARG_V1720_589) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_rulex45x62hornx45clause]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.rule->horn-clause', shen_rulex45x62hornx45clause, 2)

@tail_recursion
def shen_rulex45x62hornx45clausex45head(KL_ARG_V1721_590, KL_ARG_V1722_591):
    global symdic
    return [KL_ARG_V1721_590, [tco_apply(shen_modex45ify, [KL_ARG_V1722_591]), [symdic.symdic_Context_1957, []]]]
shen_add_fun('shen.rule->horn-clause-head', shen_rulex45x62hornx45clausex45head, 2)

@tail_recursion
def shen_modex45ify(KL_ARG_V1723_592):
    global symdic
    return ([symdic.symdic_kl_mode, [[KL_ARG_V1723_592[0], [symdic.symdic_kl_x58, [[symdic.symdic_kl_mode, [KL_ARG_V1723_592[1][1][0], [symdic.symdic_kl_x43, []]]], []]]], [symdic.symdic_kl_x45, []]]] if ((((([] == KL_ARG_V1723_592[1][1][1]) if shen_consp(KL_ARG_V1723_592[1][1]) else False) if (symdic.symdic_kl_x58 == KL_ARG_V1723_592[1][0]) else False) if shen_consp(KL_ARG_V1723_592[1]) else False) if shen_consp(KL_ARG_V1723_592) else False) else (KL_ARG_V1723_592 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.mode-ify', shen_modex45ify, 1)

@tail_recursion
def shen_rulex45x62hornx45clausex45body(KL_ARG_V1724_593, KL_ARG_V1725_594, KL_ARG_V1726_595):

    class KL_Context:
        KL_LOC_Variables_596 = None
        KL_LOC_Predicates_597 = None
        KL_LOC_SearchLiterals_599 = None
        KL_LOC_SearchClauses_600 = None
        KL_LOC_SideLiterals_601 = None
        KL_LOC_PremissLiterals_602 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Variables_596', tco_apply(kl_map, [symdic.symdic_shen_extract_vars, KL_ARG_V1726_595])), [setattr(KL_CTX, 'KL_LOC_Predicates_597', tco_apply(kl_map, [(lambda KL_ARG_X_598: tail_call(kl_gensym, [symdic.symdic_shen_cl])), KL_ARG_V1726_595])), [setattr(KL_CTX, 'KL_LOC_SearchLiterals_599', tco_apply(shen_constructx45searchx45literals, [KL_CTX.KL_LOC_Predicates_597, KL_CTX.KL_LOC_Variables_596, symdic.symdic_Context_1957, symdic.symdic_Context1_1957])), [setattr(KL_CTX, 'KL_LOC_SearchClauses_600', tco_apply(shen_constructx45searchx45clauses, [KL_CTX.KL_LOC_Predicates_597, KL_ARG_V1726_595, KL_CTX.KL_LOC_Variables_596])), [setattr(KL_CTX, 'KL_LOC_SideLiterals_601', tco_apply(shen_constructx45sidex45literals, [KL_ARG_V1724_593])), [setattr(KL_CTX, 'KL_LOC_PremissLiterals_602', tco_apply(kl_map, [(lambda KL_ARG_X_603: tail_call(shen_constructx45premissx45literal, [KL_ARG_X_603, tco_apply(kl_emptyx63, [KL_ARG_V1726_595])])), KL_ARG_V1725_594])), tail_call(kl_append, [KL_CTX.KL_LOC_SearchLiterals_599, tco_apply(kl_append, [KL_CTX.KL_LOC_SideLiterals_601, KL_CTX.KL_LOC_PremissLiterals_602])])][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]
shen_add_fun('shen.rule->horn-clause-body', shen_rulex45x62hornx45clausex45body, 3)

@tail_recursion
def shen_constructx45searchx45literals(KL_ARG_V1731_604, KL_ARG_V1732_605, KL_ARG_V1733_606, KL_ARG_V1734_607):
    global symdic
    return ([] if (([] == KL_ARG_V1732_605) if ([] == KL_ARG_V1731_604) else False) else (tail_call(shen_cslx45help, [KL_ARG_V1731_604, KL_ARG_V1732_605, KL_ARG_V1733_606, KL_ARG_V1734_607]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.construct-search-literals', shen_constructx45searchx45literals, 4)

@tail_recursion
def shen_cslx45help(KL_ARG_V1737_608, KL_ARG_V1738_609, KL_ARG_V1739_610, KL_ARG_V1740_611):
    global symdic
    return ([[symdic.symdic_kl_bind, [symdic.symdic_ContextOut_1957, [KL_ARG_V1739_610, []]]], []] if (([] == KL_ARG_V1738_609) if ([] == KL_ARG_V1737_608) else False) else ([[KL_ARG_V1737_608[0], [KL_ARG_V1739_610, [KL_ARG_V1740_611, KL_ARG_V1738_609[0]]]], tco_apply(shen_cslx45help, [KL_ARG_V1737_608[1], KL_ARG_V1738_609[1], KL_ARG_V1740_611, tco_apply(kl_gensym, [symdic.symdic_Context])])] if (shen_consp(KL_ARG_V1738_609) if shen_consp(KL_ARG_V1737_608) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_cslx45help]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.csl-help', shen_cslx45help, 4)

@tail_recursion
def shen_constructx45searchx45clauses(KL_ARG_V1741_612, KL_ARG_V1742_613, KL_ARG_V1743_614):
    global symdic
    return (symdic.symdic_shen_skip if ((([] == KL_ARG_V1743_614) if ([] == KL_ARG_V1742_613) else False) if ([] == KL_ARG_V1741_612) else False) else ([tco_apply(shen_constructx45searchx45clause, [KL_ARG_V1741_612[0], KL_ARG_V1742_613[0], KL_ARG_V1743_614[0]]), tail_call(shen_constructx45searchx45clauses, [KL_ARG_V1741_612[1], KL_ARG_V1742_613[1], KL_ARG_V1743_614[1]])][(-1)] if ((shen_consp(KL_ARG_V1743_614) if shen_consp(KL_ARG_V1742_613) else False) if shen_consp(KL_ARG_V1741_612) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_constructx45searchx45clauses]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.construct-search-clauses', shen_constructx45searchx45clauses, 3)

@tail_recursion
def shen_constructx45searchx45clause(KL_ARG_V1744_615, KL_ARG_V1745_616, KL_ARG_V1746_617):
    global symdic
    return tail_call(shen_sx45prolog, [[tco_apply(shen_constructx45basex45searchx45clause, [KL_ARG_V1744_615, KL_ARG_V1745_616, KL_ARG_V1746_617]), [tco_apply(shen_constructx45recursivex45searchx45clause, [KL_ARG_V1744_615, KL_ARG_V1745_616, KL_ARG_V1746_617]), []]]])
shen_add_fun('shen.construct-search-clause', shen_constructx45searchx45clause, 3)

@tail_recursion
def shen_constructx45basex45searchx45clause(KL_ARG_V1747_618, KL_ARG_V1748_619, KL_ARG_V1749_620):
    global symdic
    return [[KL_ARG_V1747_618, [[tco_apply(shen_modex45ify, [KL_ARG_V1748_619]), symdic.symdic_In_1957], [symdic.symdic_In_1957, KL_ARG_V1749_620]]], [symdic.symdic_kl_x58x45, [[], []]]]
shen_add_fun('shen.construct-base-search-clause', shen_constructx45basex45searchx45clause, 3)

@tail_recursion
def shen_constructx45recursivex45searchx45clause(KL_ARG_V1750_621, KL_ARG_V1751_622, KL_ARG_V1752_623):
    global symdic
    return [[KL_ARG_V1750_621, [[symdic.symdic_Assumption_1957, symdic.symdic_Assumptions_1957], [[symdic.symdic_Assumption_1957, symdic.symdic_Out_1957], KL_ARG_V1752_623]]], [symdic.symdic_kl_x58x45, [[[KL_ARG_V1750_621, [symdic.symdic_Assumptions_1957, [symdic.symdic_Out_1957, KL_ARG_V1752_623]]], []], []]]]
shen_add_fun('shen.construct-recursive-search-clause', shen_constructx45recursivex45searchx45clause, 3)

@tail_recursion
def shen_constructx45sidex45literals(KL_ARG_V1757_624):
    global symdic
    return ([] if ([] == KL_ARG_V1757_624) else ([[symdic.symdic_kl_when, KL_ARG_V1757_624[0][1]], tco_apply(shen_constructx45sidex45literals, [KL_ARG_V1757_624[1]])] if ((((([] == KL_ARG_V1757_624[0][1][1]) if shen_consp(KL_ARG_V1757_624[0][1]) else False) if (symdic.symdic_kl_if == KL_ARG_V1757_624[0][0]) else False) if shen_consp(KL_ARG_V1757_624[0]) else False) if shen_consp(KL_ARG_V1757_624) else False) else ([[symdic.symdic_kl_is, KL_ARG_V1757_624[0][1]], tco_apply(shen_constructx45sidex45literals, [KL_ARG_V1757_624[1]])] if (((((([] == KL_ARG_V1757_624[0][1][1][1]) if shen_consp(KL_ARG_V1757_624[0][1][1]) else False) if shen_consp(KL_ARG_V1757_624[0][1]) else False) if (symdic.symdic_kl_let == KL_ARG_V1757_624[0][0]) else False) if shen_consp(KL_ARG_V1757_624[0]) else False) if shen_consp(KL_ARG_V1757_624) else False) else (tail_call(shen_constructx45sidex45literals, [KL_ARG_V1757_624[1]]) if shen_consp(KL_ARG_V1757_624) else (tail_call(shen_sysx45error, [symdic.symdic_shen_constructx45sidex45literals]) if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.construct-side-literals', shen_constructx45sidex45literals, 1)

@tail_recursion
def shen_constructx45premissx45literal(KL_ARG_V1762_625, KL_ARG_V1763_626):
    global symdic
    return ([symdic.symdic_shen_tx42, [tco_apply(shen_recursive_cons_form, [tco_apply(kl_snd, [KL_ARG_V1762_625])]), [tco_apply(shen_constructx45context, [KL_ARG_V1763_626, tco_apply(kl_fst, [KL_ARG_V1762_625])]), []]]] if tco_apply(kl_tuplex63, [KL_ARG_V1762_625]) else ([symdic.symdic_kl_cut, [symdic.symdic_Throwcontrol, []]] if (symdic.symdic_kl_x33 == KL_ARG_V1762_625) else (tail_call(shen_sysx45error, [symdic.symdic_shen_constructx45premissx45literal]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.construct-premiss-literal', shen_constructx45premissx45literal, 2)

@tail_recursion
def shen_constructx45context(KL_ARG_V1764_627, KL_ARG_V1765_628):
    global symdic
    return (symdic.symdic_Context_1957 if (([] == KL_ARG_V1765_628) if (True == KL_ARG_V1764_627) else False) else (symdic.symdic_ContextOut_1957 if (([] == KL_ARG_V1765_628) if (False == KL_ARG_V1764_627) else False) else ([symdic.symdic_kl_cons, [tco_apply(shen_recursive_cons_form, [KL_ARG_V1765_628[0]]), [tco_apply(shen_constructx45context, [KL_ARG_V1764_627, KL_ARG_V1765_628[1]]), []]]] if shen_consp(KL_ARG_V1765_628) else (tail_call(shen_sysx45error, [symdic.symdic_shen_constructx45context]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.construct-context', shen_constructx45context, 2)

@tail_recursion
def shen_recursive_cons_form(KL_ARG_V1766_629):
    global symdic
    return ([symdic.symdic_kl_cons, [tco_apply(shen_recursive_cons_form, [KL_ARG_V1766_629[0]]), [tco_apply(shen_recursive_cons_form, [KL_ARG_V1766_629[1]]), []]]] if shen_consp(KL_ARG_V1766_629) else (KL_ARG_V1766_629 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.recursive_cons_form', shen_recursive_cons_form, 1)

@tail_recursion
def kl_preclude(KL_ARG_V1767_630):
    global symdic
    return tail_call(shen_precludex45h, [tco_apply(kl_map, [symdic.symdic_shen_internx45type, KL_ARG_V1767_630])])
shen_add_fun('preclude', kl_preclude, 1)

@tail_recursion
def shen_precludex45h(KL_ARG_V1768_631):

    class KL_Context:
        KL_LOC_FilterDatatypes_632 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_FilterDatatypes_632', shen_set(symdic.symdic_shen_x42datatypesx42, tco_apply(kl_difference, [shen_get(symdic.symdic_shen_x42datatypesx42), KL_ARG_V1768_631]))), shen_get(symdic.symdic_shen_x42datatypesx42)][(-1)]
shen_add_fun('shen.preclude-h', shen_precludex45h, 1)

@tail_recursion
def kl_include(KL_ARG_V1769_633):
    global symdic
    return tail_call(shen_includex45h, [tco_apply(kl_map, [symdic.symdic_shen_internx45type, KL_ARG_V1769_633])])
shen_add_fun('include', kl_include, 1)

@tail_recursion
def shen_includex45h(KL_ARG_V1770_634):

    class KL_Context:
        KL_LOC_ValidTypes_635 = None
        KL_LOC_NewDatatypes_636 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_ValidTypes_635', tco_apply(kl_intersection, [KL_ARG_V1770_634, shen_get(symdic.symdic_shen_x42alldatatypesx42)])), [setattr(KL_CTX, 'KL_LOC_NewDatatypes_636', shen_set(symdic.symdic_shen_x42datatypesx42, tco_apply(kl_union, [KL_CTX.KL_LOC_ValidTypes_635, shen_get(symdic.symdic_shen_x42datatypesx42)]))), shen_get(symdic.symdic_shen_x42datatypesx42)][(-1)]][(-1)]
shen_add_fun('shen.include-h', shen_includex45h, 1)

@tail_recursion
def kl_precludex45allx45but(KL_ARG_V1771_637):
    global symdic
    return tail_call(shen_precludex45h, [tco_apply(kl_difference, [shen_get(symdic.symdic_shen_x42alldatatypesx42), tco_apply(kl_map, [symdic.symdic_shen_internx45type, KL_ARG_V1771_637])])])
shen_add_fun('preclude-all-but', kl_precludex45allx45but, 1)

@tail_recursion
def kl_includex45allx45but(KL_ARG_V1772_638):
    global symdic
    return tail_call(shen_includex45h, [tco_apply(kl_difference, [shen_get(symdic.symdic_shen_x42alldatatypesx42), tco_apply(kl_map, [symdic.symdic_shen_internx45type, KL_ARG_V1772_638])])])
shen_add_fun('include-all-but', kl_includex45allx45but, 1)

@tail_recursion
def shen_synonymsx45help(KL_ARG_V1777_639):
    global symdic
    return (symdic.symdic_kl_synonyms if ([] == KL_ARG_V1777_639) else ([tco_apply(shen_pushnew, [[KL_ARG_V1777_639[0], tco_apply(shen_curryx45type, [KL_ARG_V1777_639[1][0]])], symdic.symdic_shen_x42synonymsx42]), tail_call(shen_synonymsx45help, [KL_ARG_V1777_639[1][1]])][(-1)] if (shen_consp(KL_ARG_V1777_639[1]) if shen_consp(KL_ARG_V1777_639) else False) else (shen_simple_error(('odd number of synonyms\r\n' + '')) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.synonyms-help', shen_synonymsx45help, 1)

@tail_recursion
def shen_pushnew(KL_ARG_V1778_640, KL_ARG_V1779_641):
    global symdic
    return (shen_get(KL_ARG_V1779_641) if tco_apply(kl_elementx63, [KL_ARG_V1778_640, shen_get(KL_ARG_V1779_641)]) else shen_set(KL_ARG_V1779_641, [KL_ARG_V1778_640, shen_get(KL_ARG_V1779_641)]))
shen_add_fun('shen.pushnew', shen_pushnew, 2)


#============================== yacc.kl==============================



@tail_recursion
def shen_yacc(KL_ARG_V2126_642):
    global symdic
    return (tail_call(shen_yacc, [[symdic.symdic_kl_defcc, [KL_ARG_V2126_642[1][0], KL_ARG_V2126_642[1][1][1][1][1][1][1]]]]) if (((((((((((symdic.symdic_kl_x125 == KL_ARG_V2126_642[1][1][1][1][1][1][0]) if shen_consp(KL_ARG_V2126_642[1][1][1][1][1][1]) else False) if shen_consp(KL_ARG_V2126_642[1][1][1][1][1]) else False) if (symdic.symdic_kl_x61x61x62 == KL_ARG_V2126_642[1][1][1][1][0]) else False) if shen_consp(KL_ARG_V2126_642[1][1][1][1]) else False) if shen_consp(KL_ARG_V2126_642[1][1][1]) else False) if (symdic.symdic_kl_x123 == KL_ARG_V2126_642[1][1][0]) else False) if shen_consp(KL_ARG_V2126_642[1][1]) else False) if shen_consp(KL_ARG_V2126_642[1]) else False) if (symdic.symdic_kl_defcc == KL_ARG_V2126_642[0]) else False) if shen_consp(KL_ARG_V2126_642) else False) else (tail_call(shen_yaccx45x62shen, [KL_ARG_V2126_642[1][0], KL_ARG_V2126_642[1][1]]) if ((shen_consp(KL_ARG_V2126_642[1]) if (symdic.symdic_kl_defcc == KL_ARG_V2126_642[0]) else False) if shen_consp(KL_ARG_V2126_642) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_yacc]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.yacc', shen_yacc, 1)

@tail_recursion
def shen_yaccx45x62shen(KL_ARG_V2127_643, KL_ARG_V2128_644):

    class KL_Context:
        KL_LOC_CCRules_645 = None
        KL_LOC_CCBody_646 = None
        KL_LOC_YaccCases_647 = None
        KL_LOC_CatchKill_648 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_CCRules_645', tco_apply(shen_split_cc_rules, [KL_ARG_V2128_644, []])), [setattr(KL_CTX, 'KL_LOC_CCBody_646', tco_apply(kl_map, [symdic.symdic_shen_cc_body, KL_CTX.KL_LOC_CCRules_645])), [setattr(KL_CTX, 'KL_LOC_YaccCases_647', tco_apply(shen_yacc_cases, [KL_CTX.KL_LOC_CCBody_646])), [setattr(KL_CTX, 'KL_LOC_CatchKill_648', tco_apply(shen_catchkill, [KL_CTX.KL_LOC_YaccCases_647])), [symdic.symdic_kl_define, [KL_ARG_V2127_643, [symdic.symdic_Stream, [symdic.symdic_kl_x45x62, [KL_CTX.KL_LOC_CatchKill_648, []]]]]]][(-1)]][(-1)]][(-1)]][(-1)]
shen_add_fun('shen.yacc->shen', shen_yaccx45x62shen, 2)

@tail_recursion
def shen_split_cc_rules(KL_ARG_V2129_649, KL_ARG_V2130_650):
    global symdic
    return ([] if (([] == KL_ARG_V2130_650) if ([] == KL_ARG_V2129_649) else False) else ([tco_apply(shen_split_cc_rule, [tco_apply(kl_reverse, [KL_ARG_V2130_650]), []]), []] if ([] == KL_ARG_V2129_649) else ([tco_apply(shen_split_cc_rule, [tco_apply(kl_reverse, [KL_ARG_V2130_650]), []]), tco_apply(shen_split_cc_rules, [KL_ARG_V2129_649[1], []])] if ((symdic.symdic_kl_x59 == KL_ARG_V2129_649[0]) if shen_consp(KL_ARG_V2129_649) else False) else (tail_call(shen_split_cc_rules, [KL_ARG_V2129_649[1], [KL_ARG_V2129_649[0], KL_ARG_V2130_650]]) if shen_consp(KL_ARG_V2129_649) else (tail_call(shen_sysx45error, [symdic.symdic_shen_split_cc_rules]) if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.split_cc_rules', shen_split_cc_rules, 2)

@tail_recursion
def shen_split_cc_rule(KL_ARG_V2131_651, KL_ARG_V2132_652):
    global symdic
    return ([tco_apply(kl_reverse, [KL_ARG_V2132_652]), KL_ARG_V2131_651[1]] if (((([] == KL_ARG_V2131_651[1][1]) if shen_consp(KL_ARG_V2131_651[1]) else False) if (symdic.symdic_kl_x58x61 == KL_ARG_V2131_651[0]) else False) if shen_consp(KL_ARG_V2131_651) else False) else ([tco_apply(kl_reverse, [KL_ARG_V2132_652]), [[symdic.symdic_kl_where, [KL_ARG_V2131_651[1][1][1][0], [KL_ARG_V2131_651[1][0], []]]], []]] if ((((((([] == KL_ARG_V2131_651[1][1][1][1]) if shen_consp(KL_ARG_V2131_651[1][1][1]) else False) if (symdic.symdic_kl_where == KL_ARG_V2131_651[1][1][0]) else False) if shen_consp(KL_ARG_V2131_651[1][1]) else False) if shen_consp(KL_ARG_V2131_651[1]) else False) if (symdic.symdic_kl_x58x61 == KL_ARG_V2131_651[0]) else False) if shen_consp(KL_ARG_V2131_651) else False) else ([tco_apply(shen_prhush, ['warning: ', tco_apply(kl_stoutput, [])]), [tco_apply(kl_map, [(lambda KL_ARG_X_653: tail_call(shen_prhush, [tco_apply(shen_app, [KL_ARG_X_653, ' ', symdic.symdic_shen_a]), tco_apply(kl_stoutput, [])])), tco_apply(kl_reverse, [KL_ARG_V2132_652])]), [tco_apply(shen_prhush, ['has no semantics.\r\n', tco_apply(kl_stoutput, [])]), tail_call(shen_split_cc_rule, [[symdic.symdic_kl_x58x61, [tco_apply(shen_default_semantics, [tco_apply(kl_reverse, [KL_ARG_V2132_652])]), []]], KL_ARG_V2132_652])][(-1)]][(-1)]][(-1)] if ([] == KL_ARG_V2131_651) else (tail_call(shen_split_cc_rule, [KL_ARG_V2131_651[1], [KL_ARG_V2131_651[0], KL_ARG_V2132_652]]) if shen_consp(KL_ARG_V2131_651) else (tail_call(shen_sysx45error, [symdic.symdic_shen_split_cc_rule]) if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.split_cc_rule', shen_split_cc_rule, 2)

@tail_recursion
def shen_default_semantics(KL_ARG_V2133_654):
    global symdic
    return ([] if ([] == KL_ARG_V2133_654) else ([symdic.symdic_kl_append, [KL_ARG_V2133_654[0], [tco_apply(shen_default_semantics, [KL_ARG_V2133_654[1]]), []]]] if (tco_apply(shen_grammar_symbolx63, [KL_ARG_V2133_654[0]]) if shen_consp(KL_ARG_V2133_654) else False) else ([symdic.symdic_kl_cons, [KL_ARG_V2133_654[0], [tco_apply(shen_default_semantics, [KL_ARG_V2133_654[1]]), []]]] if shen_consp(KL_ARG_V2133_654) else (tail_call(shen_sysx45error, [symdic.symdic_shen_default_semantics]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.default_semantics', shen_default_semantics, 1)

@tail_recursion
def shen_grammar_symbolx63(KL_ARG_V2134_655):

    class KL_Context:
        KL_LOC_Cs_656 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_Cs_656', tco_apply(shen_stripx45pathname, [tco_apply(kl_explode, [KL_ARG_V2134_655])])), ((tco_apply(kl_reverse, [KL_CTX.KL_LOC_Cs_656])[0] == '>') if (KL_CTX.KL_LOC_Cs_656[0] == '<') else False)][(-1)] if tco_apply(kl_symbolx63, [KL_ARG_V2134_655]) else False)
shen_add_fun('shen.grammar_symbol?', shen_grammar_symbolx63, 1)

@tail_recursion
def shen_yacc_cases(KL_ARG_V2135_657):

    class KL_Context:
        KL_LOC_P_658 = None
    KL_CTX = KL_Context()
    global symdic
    return (KL_ARG_V2135_657[0] if (([] == KL_ARG_V2135_657[1]) if shen_consp(KL_ARG_V2135_657) else False) else ([setattr(KL_CTX, 'KL_LOC_P_658', symdic.symdic_YaccParse), [symdic.symdic_kl_let, [KL_CTX.KL_LOC_P_658, [KL_ARG_V2135_657[0], [[symdic.symdic_kl_if, [[symdic.symdic_kl_x61, [KL_CTX.KL_LOC_P_658, [[symdic.symdic_kl_fail, []], []]]], [tco_apply(shen_yacc_cases, [KL_ARG_V2135_657[1]]), [KL_CTX.KL_LOC_P_658, []]]]], []]]]]][(-1)] if shen_consp(KL_ARG_V2135_657) else (tail_call(shen_sysx45error, [symdic.symdic_shen_yacc_cases]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.yacc_cases', shen_yacc_cases, 1)

@tail_recursion
def shen_cc_body(KL_ARG_V2136_659):
    global symdic
    return (tail_call(shen_syntax, [KL_ARG_V2136_659[0], symdic.symdic_Stream, KL_ARG_V2136_659[1][0]]) if ((([] == KL_ARG_V2136_659[1][1]) if shen_consp(KL_ARG_V2136_659[1]) else False) if shen_consp(KL_ARG_V2136_659) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_cc_body]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.cc_body', shen_cc_body, 1)

@tail_recursion
def shen_syntax(KL_ARG_V2137_660, KL_ARG_V2138_661, KL_ARG_V2139_662):
    global symdic
    return ([symdic.symdic_kl_if, [tco_apply(shen_semantics, [KL_ARG_V2139_662[1][0]]), [[symdic.symdic_shen_pair, [[symdic.symdic_kl_hd, [KL_ARG_V2138_661, []]], [tco_apply(shen_semantics, [KL_ARG_V2139_662[1][1][0]]), []]]], [[symdic.symdic_kl_fail, []], []]]]] if (((((([] == KL_ARG_V2139_662[1][1][1]) if shen_consp(KL_ARG_V2139_662[1][1]) else False) if shen_consp(KL_ARG_V2139_662[1]) else False) if (symdic.symdic_kl_where == KL_ARG_V2139_662[0]) else False) if shen_consp(KL_ARG_V2139_662) else False) if ([] == KL_ARG_V2137_660) else False) else ([symdic.symdic_shen_pair, [[symdic.symdic_kl_hd, [KL_ARG_V2138_661, []]], [tco_apply(shen_semantics, [KL_ARG_V2139_662]), []]]] if ([] == KL_ARG_V2137_660) else ((tail_call(shen_recursive_descent, [KL_ARG_V2137_660, KL_ARG_V2138_661, KL_ARG_V2139_662]) if tco_apply(shen_grammar_symbolx63, [KL_ARG_V2137_660[0]]) else (tail_call(shen_variablex45match, [KL_ARG_V2137_660, KL_ARG_V2138_661, KL_ARG_V2139_662]) if tco_apply(kl_variablex63, [KL_ARG_V2137_660[0]]) else (tail_call(shen_jump_stream, [KL_ARG_V2137_660, KL_ARG_V2138_661, KL_ARG_V2139_662]) if tco_apply(shen_jump_streamx63, [KL_ARG_V2137_660[0]]) else (tail_call(shen_check_stream, [KL_ARG_V2137_660, KL_ARG_V2138_661, KL_ARG_V2139_662]) if tco_apply(shen_terminalx63, [KL_ARG_V2137_660[0]]) else (tail_call(shen_list_stream, [tco_apply(shen_decons, [KL_ARG_V2137_660[0]]), KL_ARG_V2137_660[1], KL_ARG_V2138_661, KL_ARG_V2139_662]) if tco_apply(shen_list_streamx63, [KL_ARG_V2137_660[0]]) else shen_simple_error(tco_apply(shen_app, [KL_ARG_V2137_660[0], ' is not legal syntax\r\n', symdic.symdic_shen_a]))))))) if shen_consp(KL_ARG_V2137_660) else (tail_call(shen_sysx45error, [symdic.symdic_shen_syntax]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.syntax', shen_syntax, 3)

@tail_recursion
def shen_list_streamx63(KL_ARG_V2148_663):
    global symdic
    return (True if shen_consp(KL_ARG_V2148_663) else (False if True else shen_simple_error('condition failure')))
shen_add_fun('shen.list_stream?', shen_list_streamx63, 1)

@tail_recursion
def shen_decons(KL_ARG_V2149_664):
    global symdic
    return ([KL_ARG_V2149_664[1][0], tco_apply(shen_decons, [KL_ARG_V2149_664[1][1][0]])] if ((((([] == KL_ARG_V2149_664[1][1][1]) if shen_consp(KL_ARG_V2149_664[1][1]) else False) if shen_consp(KL_ARG_V2149_664[1]) else False) if (symdic.symdic_kl_cons == KL_ARG_V2149_664[0]) else False) if shen_consp(KL_ARG_V2149_664) else False) else (KL_ARG_V2149_664 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.decons', shen_decons, 1)

@tail_recursion
def shen_list_stream(KL_ARG_V2150_665, KL_ARG_V2151_666, KL_ARG_V2152_667, KL_ARG_V2153_668):

    class KL_Context:
        KL_LOC_Test_669 = None
        KL_LOC_Action_670 = None
        KL_LOC_Else_671 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Test_669', [symdic.symdic_kl_and, [[symdic.symdic_kl_consx63, [[symdic.symdic_kl_hd, [KL_ARG_V2152_667, []]], []]], [[symdic.symdic_kl_consx63, [[symdic.symdic_kl_hd, [[symdic.symdic_kl_hd, [KL_ARG_V2152_667, []]], []]], []]], []]]]), [setattr(KL_CTX, 'KL_LOC_Action_670', [symdic.symdic_shen_sndx45orx45fail, [tco_apply(shen_syntax, [KL_ARG_V2150_665, [symdic.symdic_shen_pair, [[symdic.symdic_kl_hd, [[symdic.symdic_kl_hd, [KL_ARG_V2152_667, []]], []]], [[symdic.symdic_shen_hdtl, [KL_ARG_V2152_667, []]], []]]], [symdic.symdic_shen_leavex33, [tco_apply(shen_syntax, [KL_ARG_V2151_666, [symdic.symdic_shen_pair, [[symdic.symdic_kl_tl, [[symdic.symdic_kl_hd, [KL_ARG_V2152_667, []]], []]], [[symdic.symdic_shen_hdtl, [KL_ARG_V2152_667, []]], []]]], KL_ARG_V2153_668]), []]]]), []]]), [setattr(KL_CTX, 'KL_LOC_Else_671', [symdic.symdic_kl_fail, []]), [symdic.symdic_kl_if, [KL_CTX.KL_LOC_Test_669, [KL_CTX.KL_LOC_Action_670, [KL_CTX.KL_LOC_Else_671, []]]]]][(-1)]][(-1)]][(-1)]
shen_add_fun('shen.list_stream', shen_list_stream, 4)

@tail_recursion
def shen_sndx45orx45fail(KL_ARG_V2160_672):
    global symdic
    return (KL_ARG_V2160_672[1][0] if ((([] == KL_ARG_V2160_672[1][1]) if shen_consp(KL_ARG_V2160_672[1]) else False) if shen_consp(KL_ARG_V2160_672) else False) else (tail_call(kl_fail, []) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.snd-or-fail', shen_sndx45orx45fail, 1)

@tail_recursion
def shen_stripx45pathname(KL_ARG_V2165_673):
    global symdic
    return (KL_ARG_V2165_673 if (not tco_apply(kl_elementx63, ['.', KL_ARG_V2165_673])) else (tail_call(shen_stripx45pathname, [KL_ARG_V2165_673[1]]) if shen_consp(KL_ARG_V2165_673) else (tail_call(shen_sysx45error, [symdic.symdic_shen_stripx45pathname]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.strip-pathname', shen_stripx45pathname, 1)

@tail_recursion
def shen_recursive_descent(KL_ARG_V2166_674, KL_ARG_V2167_675, KL_ARG_V2168_676):

    class KL_Context:
        KL_LOC_Test_677 = None
        KL_LOC_Action_678 = None
        KL_LOC_Else_679 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_Test_677', [KL_ARG_V2166_674[0], [KL_ARG_V2167_675, []]]), [setattr(KL_CTX, 'KL_LOC_Action_678', tco_apply(shen_syntax, [KL_ARG_V2166_674[1], tco_apply(kl_concat, [symdic.symdic_Parse_, KL_ARG_V2166_674[0]]), KL_ARG_V2168_676])), [setattr(KL_CTX, 'KL_LOC_Else_679', [symdic.symdic_kl_fail, []]), [symdic.symdic_kl_let, [tco_apply(kl_concat, [symdic.symdic_Parse_, KL_ARG_V2166_674[0]]), [KL_CTX.KL_LOC_Test_677, [[symdic.symdic_kl_if, [[symdic.symdic_kl_not, [[symdic.symdic_kl_x61, [[symdic.symdic_kl_fail, []], [tco_apply(kl_concat, [symdic.symdic_Parse_, KL_ARG_V2166_674[0]]), []]]], []]], [KL_CTX.KL_LOC_Action_678, [KL_CTX.KL_LOC_Else_679, []]]]], []]]]]][(-1)]][(-1)]][(-1)] if shen_consp(KL_ARG_V2166_674) else (tail_call(shen_sysx45error, [symdic.symdic_shen_recursive_descent]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.recursive_descent', shen_recursive_descent, 3)

@tail_recursion
def shen_variablex45match(KL_ARG_V2169_680, KL_ARG_V2170_681, KL_ARG_V2171_682):

    class KL_Context:
        KL_LOC_Test_683 = None
        KL_LOC_Action_684 = None
        KL_LOC_Else_685 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_Test_683', [symdic.symdic_kl_consx63, [[symdic.symdic_kl_hd, [KL_ARG_V2170_681, []]], []]]), [setattr(KL_CTX, 'KL_LOC_Action_684', [symdic.symdic_kl_let, [tco_apply(kl_concat, [symdic.symdic_Parse_, KL_ARG_V2169_680[0]]), [[symdic.symdic_kl_hd, [[symdic.symdic_kl_hd, [KL_ARG_V2170_681, []]], []]], [tco_apply(shen_syntax, [KL_ARG_V2169_680[1], [symdic.symdic_shen_pair, [[symdic.symdic_kl_tl, [[symdic.symdic_kl_hd, [KL_ARG_V2170_681, []]], []]], [[symdic.symdic_shen_hdtl, [KL_ARG_V2170_681, []]], []]]], KL_ARG_V2171_682]), []]]]]), [setattr(KL_CTX, 'KL_LOC_Else_685', [symdic.symdic_kl_fail, []]), [symdic.symdic_kl_if, [KL_CTX.KL_LOC_Test_683, [KL_CTX.KL_LOC_Action_684, [KL_CTX.KL_LOC_Else_685, []]]]]][(-1)]][(-1)]][(-1)] if shen_consp(KL_ARG_V2169_680) else (tail_call(shen_sysx45error, [symdic.symdic_shen_variablex45match]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.variable-match', shen_variablex45match, 3)

@tail_recursion
def shen_terminalx63(KL_ARG_V2180_686):
    global symdic
    return (False if shen_consp(KL_ARG_V2180_686) else (False if tco_apply(kl_variablex63, [KL_ARG_V2180_686]) else (True if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.terminal?', shen_terminalx63, 1)

@tail_recursion
def shen_jump_streamx63(KL_ARG_V2185_687):
    global symdic
    return (True if (KL_ARG_V2185_687 == symdic.symdic_kl__) else (False if True else shen_simple_error('condition failure')))
shen_add_fun('shen.jump_stream?', shen_jump_streamx63, 1)

@tail_recursion
def shen_check_stream(KL_ARG_V2186_688, KL_ARG_V2187_689, KL_ARG_V2188_690):

    class KL_Context:
        KL_LOC_Test_691 = None
        KL_LOC_Action_692 = None
        KL_LOC_Else_693 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_Test_691', [symdic.symdic_kl_and, [[symdic.symdic_kl_consx63, [[symdic.symdic_kl_hd, [KL_ARG_V2187_689, []]], []]], [[symdic.symdic_kl_x61, [KL_ARG_V2186_688[0], [[symdic.symdic_kl_hd, [[symdic.symdic_kl_hd, [KL_ARG_V2187_689, []]], []]], []]]], []]]]), [setattr(KL_CTX, 'KL_LOC_Action_692', tco_apply(shen_syntax, [KL_ARG_V2186_688[1], [symdic.symdic_shen_pair, [[symdic.symdic_kl_tl, [[symdic.symdic_kl_hd, [KL_ARG_V2187_689, []]], []]], [[symdic.symdic_shen_hdtl, [KL_ARG_V2187_689, []]], []]]], KL_ARG_V2188_690])), [setattr(KL_CTX, 'KL_LOC_Else_693', [symdic.symdic_kl_fail, []]), [symdic.symdic_kl_if, [KL_CTX.KL_LOC_Test_691, [KL_CTX.KL_LOC_Action_692, [KL_CTX.KL_LOC_Else_693, []]]]]][(-1)]][(-1)]][(-1)] if shen_consp(KL_ARG_V2186_688) else (tail_call(shen_sysx45error, [symdic.symdic_shen_check_stream]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.check_stream', shen_check_stream, 3)

@tail_recursion
def shen_jump_stream(KL_ARG_V2189_694, KL_ARG_V2190_695, KL_ARG_V2191_696):

    class KL_Context:
        KL_LOC_Test_697 = None
        KL_LOC_Action_698 = None
        KL_LOC_Else_699 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_Test_697', [symdic.symdic_kl_consx63, [[symdic.symdic_kl_hd, [KL_ARG_V2190_695, []]], []]]), [setattr(KL_CTX, 'KL_LOC_Action_698', tco_apply(shen_syntax, [KL_ARG_V2189_694[1], [symdic.symdic_shen_pair, [[symdic.symdic_kl_tl, [[symdic.symdic_kl_hd, [KL_ARG_V2190_695, []]], []]], [[symdic.symdic_shen_hdtl, [KL_ARG_V2190_695, []]], []]]], KL_ARG_V2191_696])), [setattr(KL_CTX, 'KL_LOC_Else_699', [symdic.symdic_kl_fail, []]), [symdic.symdic_kl_if, [KL_CTX.KL_LOC_Test_697, [KL_CTX.KL_LOC_Action_698, [KL_CTX.KL_LOC_Else_699, []]]]]][(-1)]][(-1)]][(-1)] if shen_consp(KL_ARG_V2189_694) else (tail_call(shen_sysx45error, [symdic.symdic_shen_jump_stream]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.jump_stream', shen_jump_stream, 3)

@tail_recursion
def shen_semantics(KL_ARG_V2192_700):
    global symdic
    return (KL_ARG_V2192_700[1][0] if (((([] == KL_ARG_V2192_700[1][1]) if shen_consp(KL_ARG_V2192_700[1]) else False) if (symdic.symdic_shen_leavex33 == KL_ARG_V2192_700[0]) else False) if shen_consp(KL_ARG_V2192_700) else False) else ([] if ([] == KL_ARG_V2192_700) else ([symdic.symdic_shen_hdtl, [tco_apply(kl_concat, [symdic.symdic_Parse_, KL_ARG_V2192_700]), []]] if tco_apply(shen_grammar_symbolx63, [KL_ARG_V2192_700]) else (tail_call(kl_concat, [symdic.symdic_Parse_, KL_ARG_V2192_700]) if tco_apply(kl_variablex63, [KL_ARG_V2192_700]) else (tail_call(kl_map, [symdic.symdic_shen_semantics, KL_ARG_V2192_700]) if shen_consp(KL_ARG_V2192_700) else (KL_ARG_V2192_700 if True else shen_simple_error('condition failure')))))))
shen_add_fun('shen.semantics', shen_semantics, 1)

@tail_recursion
def kl_fail():
    global symdic
    return symdic.symdic_shen_failx33
shen_add_fun('fail', kl_fail, 0)

@tail_recursion
def shen_pair(KL_ARG_V2193_701, KL_ARG_V2194_702):
    global symdic
    return [KL_ARG_V2193_701, [KL_ARG_V2194_702, []]]
shen_add_fun('shen.pair', shen_pair, 2)

@tail_recursion
def shen_hdtl(KL_ARG_V2195_703):
    global symdic
    return KL_ARG_V2195_703[1][0]
shen_add_fun('shen.hdtl', shen_hdtl, 1)

@tail_recursion
def x60x33x62(KL_ARG_V2202_704):
    global symdic
    return ([[], [KL_ARG_V2202_704[0], []]] if ((([] == KL_ARG_V2202_704[1][1]) if shen_consp(KL_ARG_V2202_704[1]) else False) if shen_consp(KL_ARG_V2202_704) else False) else (tail_call(kl_fail, []) if True else shen_simple_error('condition failure')))
shen_add_fun('<!>', x60x33x62, 1)

@tail_recursion
def kl_x60ex62(KL_ARG_V2207_705):
    global symdic
    return ([KL_ARG_V2207_705[0], [[], []]] if ((([] == KL_ARG_V2207_705[1][1]) if shen_consp(KL_ARG_V2207_705[1]) else False) if shen_consp(KL_ARG_V2207_705) else False) else (tail_call(shen_sysx45error, [symdic.symdic_kl_x60ex62]) if True else shen_simple_error('condition failure')))
shen_add_fun('<e>', kl_x60ex62, 1)

@tail_recursion
def shen_catchkill(KL_ARG_V2208_706):
    global symdic
    return [symdic.symdic_kl_trapx45error, [KL_ARG_V2208_706, [[symdic.symdic_kl_lambda, [symdic.symdic_E, [[symdic.symdic_shen_analysex45kill, [symdic.symdic_E, []]], []]]], []]]]
shen_add_fun('shen.catchkill', shen_catchkill, 1)

@tail_recursion
def shen_analysex45kill(KL_ARG_V2209_707):

    class KL_Context:
        KL_LOC_String_708 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_String_708', KL_ARG_V2209_707.message), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_String_708 == 'Shen YACC kill') else shen_simple_error(KL_CTX.KL_LOC_String_708))][(-1)]
shen_add_fun('shen.analyse-kill', shen_analysex45kill, 1)

@tail_recursion
def kill():
    global symdic
    return shen_simple_error('Shen YACC kill')
shen_add_fun('kill', kill, 0)


#============================== reader.kl==============================



@tail_recursion
def kl_lineread():
    global symdic
    return tail_call(shen_linereadx45loop, [shen_read_byte(tco_apply(kl_stinput, [])), []])
shen_add_fun('lineread', kl_lineread, 0)

@tail_recursion
def shen_linereadx45loop(KL_ARG_V1309_709, KL_ARG_V1310_710):

    class KL_Context:
        KL_LOC_Line_711 = None
    KL_CTX = KL_Context()
    global symdic
    return (shen_simple_error('line read aborted') if (KL_ARG_V1309_709 == tco_apply(shen_hat, [])) else ([setattr(KL_CTX, 'KL_LOC_Line_711', tco_apply(kl_compile, [symdic.symdic_shen_x60st_inputx62, KL_ARG_V1310_710, (lambda KL_ARG_E_712: symdic.symdic_shen_nextline)])), (tail_call(shen_linereadx45loop, [shen_read_byte(tco_apply(kl_stinput, [])), tco_apply(kl_append, [KL_ARG_V1310_710, [KL_ARG_V1309_709, []]])]) if (True if (KL_CTX.KL_LOC_Line_711 == symdic.symdic_shen_nextline) else tco_apply(kl_emptyx63, [KL_CTX.KL_LOC_Line_711])) else KL_CTX.KL_LOC_Line_711)][(-1)] if tco_apply(kl_elementx63, [KL_ARG_V1309_709, [tco_apply(shen_newline, []), [tco_apply(shen_carriagex45return, []), []]]]) else (tail_call(shen_linereadx45loop, [shen_read_byte(tco_apply(kl_stinput, [])), tco_apply(kl_append, [KL_ARG_V1310_710, [KL_ARG_V1309_709, []]])]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.lineread-loop', shen_linereadx45loop, 2)

@tail_recursion
def kl_readx45file(KL_ARG_V1311_713):

    class KL_Context:
        KL_LOC_Bytelist_714 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Bytelist_714', tco_apply(kl_readx45filex45asx45bytelist, [KL_ARG_V1311_713])), tail_call(kl_compile, [symdic.symdic_shen_x60st_inputx62, KL_CTX.KL_LOC_Bytelist_714, symdic.symdic_shen_readx45error])][(-1)]
shen_add_fun('read-file', kl_readx45file, 1)

@tail_recursion
def shen_readx45error(KL_ARG_V1318_715):
    global symdic
    return (shen_simple_error(('read error here:\r\n\r\n ' + tco_apply(shen_app, [tco_apply(shen_compressx4550, [50, KL_ARG_V1318_715[0]]), '\r\n', symdic.symdic_shen_a]))) if (((([] == KL_ARG_V1318_715[1][1]) if shen_consp(KL_ARG_V1318_715[1]) else False) if shen_consp(KL_ARG_V1318_715[0]) else False) if shen_consp(KL_ARG_V1318_715) else False) else (shen_simple_error('read error\r\n') if True else shen_simple_error('condition failure')))
shen_add_fun('shen.read-error', shen_readx45error, 1)

@tail_recursion
def shen_compressx4550(KL_ARG_V1323_716, KL_ARG_V1324_717):
    global symdic
    return ('' if ([] == KL_ARG_V1324_717) else ('' if (0 == KL_ARG_V1323_716) else ((chr(KL_ARG_V1324_717[0]) + tco_apply(shen_compressx4550, [(KL_ARG_V1323_716 - 1), KL_ARG_V1324_717[1]])) if shen_consp(KL_ARG_V1324_717) else (tail_call(shen_sysx45error, [symdic.symdic_shen_compressx4550]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.compress-50', shen_compressx4550, 2)

@tail_recursion
def shen_x60st_inputx62(KL_ARG_V1329_718):

    class KL_Context:
        KL_LOC_Result_719 = None
        KL_LOC_Parse_shen_x60lsbx62_720 = None
        KL_LOC_Parse_shen_x60st_input1x62_721 = None
        KL_LOC_Parse_shen_x60rsbx62_722 = None
        KL_LOC_Parse_shen_x60st_input2x62_723 = None
        KL_LOC_Result_724 = None
        KL_LOC_Parse_shen_x60lrbx62_725 = None
        KL_LOC_Parse_shen_x60st_input1x62_726 = None
        KL_LOC_Parse_shen_x60rrbx62_727 = None
        KL_LOC_Parse_shen_x60st_input2x62_728 = None
        KL_LOC_Result_729 = None
        KL_LOC_Parse_shen_x60lcurlyx62_730 = None
        KL_LOC_Parse_shen_x60st_inputx62_731 = None
        KL_LOC_Result_732 = None
        KL_LOC_Parse_shen_x60rcurlyx62_733 = None
        KL_LOC_Parse_shen_x60st_inputx62_734 = None
        KL_LOC_Result_735 = None
        KL_LOC_Parse_shen_x60barx62_736 = None
        KL_LOC_Parse_shen_x60st_inputx62_737 = None
        KL_LOC_Result_738 = None
        KL_LOC_Parse_shen_x60semicolonx62_739 = None
        KL_LOC_Parse_shen_x60st_inputx62_740 = None
        KL_LOC_Result_741 = None
        KL_LOC_Parse_shen_x60colonx62_742 = None
        KL_LOC_Parse_shen_x60equalx62_743 = None
        KL_LOC_Parse_shen_x60st_inputx62_744 = None
        KL_LOC_Result_745 = None
        KL_LOC_Parse_shen_x60colonx62_746 = None
        KL_LOC_Parse_shen_x60minusx62_747 = None
        KL_LOC_Parse_shen_x60st_inputx62_748 = None
        KL_LOC_Result_749 = None
        KL_LOC_Parse_shen_x60colonx62_750 = None
        KL_LOC_Parse_shen_x60st_inputx62_751 = None
        KL_LOC_Result_752 = None
        KL_LOC_Parse_shen_x60commax62_753 = None
        KL_LOC_Parse_shen_x60st_inputx62_754 = None
        KL_LOC_Result_755 = None
        KL_LOC_Parse_shen_x60commentx62_756 = None
        KL_LOC_Parse_shen_x60st_inputx62_757 = None
        KL_LOC_Result_758 = None
        KL_LOC_Parse_shen_x60atomx62_759 = None
        KL_LOC_Parse_shen_x60st_inputx62_760 = None
        KL_LOC_Result_761 = None
        KL_LOC_Parse_shen_x60whitespacesx62_762 = None
        KL_LOC_Parse_shen_x60st_inputx62_763 = None
        KL_LOC_Result_764 = None
        KL_LOC_Parse_x60ex62_765 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_719', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60lsbx62_720', tco_apply(shen_x60lsbx62, [KL_ARG_V1329_718])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_input1x62_721', tco_apply(shen_x60st_input1x62, [KL_CTX.KL_LOC_Parse_shen_x60lsbx62_720])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60rsbx62_722', tco_apply(shen_x60rsbx62, [KL_CTX.KL_LOC_Parse_shen_x60st_input1x62_721])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_input2x62_723', tco_apply(shen_x60st_input2x62, [KL_CTX.KL_LOC_Parse_shen_x60rsbx62_722])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60st_input2x62_723[0], [tco_apply(kl_macroexpand, [tco_apply(shen_cons_form, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_input1x62_721])])]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_input2x62_723])]]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60st_input2x62_723)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60rsbx62_722)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60st_input1x62_721)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60lsbx62_720)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_724', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60lrbx62_725', tco_apply(shen_x60lrbx62, [KL_ARG_V1329_718])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_input1x62_726', tco_apply(shen_x60st_input1x62, [KL_CTX.KL_LOC_Parse_shen_x60lrbx62_725])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60rrbx62_727', tco_apply(shen_x60rrbx62, [KL_CTX.KL_LOC_Parse_shen_x60st_input1x62_726])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_input2x62_728', tco_apply(shen_x60st_input2x62, [KL_CTX.KL_LOC_Parse_shen_x60rrbx62_727])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60st_input2x62_728[0], tco_apply(shen_packagex45macro, [tco_apply(kl_macroexpand, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_input1x62_726])]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_input2x62_728])])]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60st_input2x62_728)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60rrbx62_727)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60st_input1x62_726)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60lrbx62_725)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_729', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60lcurlyx62_730', tco_apply(shen_x60lcurlyx62, [KL_ARG_V1329_718])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_inputx62_731', tco_apply(shen_x60st_inputx62, [KL_CTX.KL_LOC_Parse_shen_x60lcurlyx62_730])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_731[0], [symdic.symdic_kl_x123, tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_731])]]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_731)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60lcurlyx62_730)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_732', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60rcurlyx62_733', tco_apply(shen_x60rcurlyx62, [KL_ARG_V1329_718])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_inputx62_734', tco_apply(shen_x60st_inputx62, [KL_CTX.KL_LOC_Parse_shen_x60rcurlyx62_733])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_734[0], [symdic.symdic_kl_x125, tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_734])]]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_734)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60rcurlyx62_733)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_735', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60barx62_736', tco_apply(shen_x60barx62, [KL_ARG_V1329_718])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_inputx62_737', tco_apply(shen_x60st_inputx62, [KL_CTX.KL_LOC_Parse_shen_x60barx62_736])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_737[0], [symdic.symdic_kl_barx33, tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_737])]]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_737)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60barx62_736)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_738', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60semicolonx62_739', tco_apply(shen_x60semicolonx62, [KL_ARG_V1329_718])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_inputx62_740', tco_apply(shen_x60st_inputx62, [KL_CTX.KL_LOC_Parse_shen_x60semicolonx62_739])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_740[0], [symdic.symdic_kl_x59, tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_740])]]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_740)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60semicolonx62_739)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_741', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60colonx62_742', tco_apply(shen_x60colonx62, [KL_ARG_V1329_718])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60equalx62_743', tco_apply(shen_x60equalx62, [KL_CTX.KL_LOC_Parse_shen_x60colonx62_742])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_inputx62_744', tco_apply(shen_x60st_inputx62, [KL_CTX.KL_LOC_Parse_shen_x60equalx62_743])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_744[0], [symdic.symdic_kl_x58x61, tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_744])]]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_744)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60equalx62_743)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60colonx62_742)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_745', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60colonx62_746', tco_apply(shen_x60colonx62, [KL_ARG_V1329_718])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60minusx62_747', tco_apply(shen_x60minusx62, [KL_CTX.KL_LOC_Parse_shen_x60colonx62_746])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_inputx62_748', tco_apply(shen_x60st_inputx62, [KL_CTX.KL_LOC_Parse_shen_x60minusx62_747])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_748[0], [symdic.symdic_kl_x58x45, tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_748])]]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_748)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60minusx62_747)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60colonx62_746)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_749', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60colonx62_750', tco_apply(shen_x60colonx62, [KL_ARG_V1329_718])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_inputx62_751', tco_apply(shen_x60st_inputx62, [KL_CTX.KL_LOC_Parse_shen_x60colonx62_750])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_751[0], [symdic.symdic_kl_x58, tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_751])]]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_751)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60colonx62_750)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_752', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60commax62_753', tco_apply(shen_x60commax62, [KL_ARG_V1329_718])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_inputx62_754', tco_apply(shen_x60st_inputx62, [KL_CTX.KL_LOC_Parse_shen_x60commax62_753])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_754[0], [shen_intern(','), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_754])]]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_754)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60commax62_753)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_755', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60commentx62_756', tco_apply(shen_x60commentx62, [KL_ARG_V1329_718])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_inputx62_757', tco_apply(shen_x60st_inputx62, [KL_CTX.KL_LOC_Parse_shen_x60commentx62_756])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_757[0], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_757])]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_757)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60commentx62_756)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_758', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60atomx62_759', tco_apply(shen_x60atomx62, [KL_ARG_V1329_718])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_inputx62_760', tco_apply(shen_x60st_inputx62, [KL_CTX.KL_LOC_Parse_shen_x60atomx62_759])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_760[0], [tco_apply(kl_macroexpand, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60atomx62_759])]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_760])]]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_760)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60atomx62_759)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_761', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60whitespacesx62_762', tco_apply(shen_x60whitespacesx62, [KL_ARG_V1329_718])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_inputx62_763', tco_apply(shen_x60st_inputx62, [KL_CTX.KL_LOC_Parse_shen_x60whitespacesx62_762])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_763[0], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_763])]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_763)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60whitespacesx62_762)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_764', [setattr(KL_CTX, 'KL_LOC_Parse_x60ex62_765', tco_apply(kl_x60ex62, [KL_ARG_V1329_718])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_x60ex62_765[0], []]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_x60ex62_765)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_764 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_764)][(-1)] if (KL_CTX.KL_LOC_Result_761 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_761)][(-1)] if (KL_CTX.KL_LOC_Result_758 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_758)][(-1)] if (KL_CTX.KL_LOC_Result_755 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_755)][(-1)] if (KL_CTX.KL_LOC_Result_752 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_752)][(-1)] if (KL_CTX.KL_LOC_Result_749 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_749)][(-1)] if (KL_CTX.KL_LOC_Result_745 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_745)][(-1)] if (KL_CTX.KL_LOC_Result_741 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_741)][(-1)] if (KL_CTX.KL_LOC_Result_738 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_738)][(-1)] if (KL_CTX.KL_LOC_Result_735 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_735)][(-1)] if (KL_CTX.KL_LOC_Result_732 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_732)][(-1)] if (KL_CTX.KL_LOC_Result_729 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_729)][(-1)] if (KL_CTX.KL_LOC_Result_724 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_724)][(-1)] if (KL_CTX.KL_LOC_Result_719 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_719)][(-1)]
shen_add_fun('shen.<st_input>', shen_x60st_inputx62, 1)

@tail_recursion
def shen_x60lsbx62(KL_ARG_V1334_766):

    class KL_Context:
        KL_LOC_Result_767 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_767', (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1334_766[0][1], tco_apply(shen_hdtl, [KL_ARG_V1334_766])])[0], symdic.symdic_shen_skip]) if ((91 == KL_ARG_V1334_766[0][0]) if shen_consp(KL_ARG_V1334_766[0]) else False) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_767 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_767)][(-1)]
shen_add_fun('shen.<lsb>', shen_x60lsbx62, 1)

@tail_recursion
def shen_x60rsbx62(KL_ARG_V1339_768):

    class KL_Context:
        KL_LOC_Result_769 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_769', (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1339_768[0][1], tco_apply(shen_hdtl, [KL_ARG_V1339_768])])[0], symdic.symdic_shen_skip]) if ((93 == KL_ARG_V1339_768[0][0]) if shen_consp(KL_ARG_V1339_768[0]) else False) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_769 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_769)][(-1)]
shen_add_fun('shen.<rsb>', shen_x60rsbx62, 1)

@tail_recursion
def shen_x60lcurlyx62(KL_ARG_V1344_770):

    class KL_Context:
        KL_LOC_Result_771 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_771', (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1344_770[0][1], tco_apply(shen_hdtl, [KL_ARG_V1344_770])])[0], symdic.symdic_shen_skip]) if ((123 == KL_ARG_V1344_770[0][0]) if shen_consp(KL_ARG_V1344_770[0]) else False) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_771 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_771)][(-1)]
shen_add_fun('shen.<lcurly>', shen_x60lcurlyx62, 1)

@tail_recursion
def shen_x60rcurlyx62(KL_ARG_V1349_772):

    class KL_Context:
        KL_LOC_Result_773 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_773', (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1349_772[0][1], tco_apply(shen_hdtl, [KL_ARG_V1349_772])])[0], symdic.symdic_shen_skip]) if ((125 == KL_ARG_V1349_772[0][0]) if shen_consp(KL_ARG_V1349_772[0]) else False) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_773 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_773)][(-1)]
shen_add_fun('shen.<rcurly>', shen_x60rcurlyx62, 1)

@tail_recursion
def shen_x60barx62(KL_ARG_V1354_774):

    class KL_Context:
        KL_LOC_Result_775 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_775', (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1354_774[0][1], tco_apply(shen_hdtl, [KL_ARG_V1354_774])])[0], symdic.symdic_shen_skip]) if ((124 == KL_ARG_V1354_774[0][0]) if shen_consp(KL_ARG_V1354_774[0]) else False) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_775 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_775)][(-1)]
shen_add_fun('shen.<bar>', shen_x60barx62, 1)

@tail_recursion
def shen_x60semicolonx62(KL_ARG_V1359_776):

    class KL_Context:
        KL_LOC_Result_777 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_777', (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1359_776[0][1], tco_apply(shen_hdtl, [KL_ARG_V1359_776])])[0], symdic.symdic_shen_skip]) if ((59 == KL_ARG_V1359_776[0][0]) if shen_consp(KL_ARG_V1359_776[0]) else False) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_777 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_777)][(-1)]
shen_add_fun('shen.<semicolon>', shen_x60semicolonx62, 1)

@tail_recursion
def shen_x60colonx62(KL_ARG_V1364_778):

    class KL_Context:
        KL_LOC_Result_779 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_779', (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1364_778[0][1], tco_apply(shen_hdtl, [KL_ARG_V1364_778])])[0], symdic.symdic_shen_skip]) if ((58 == KL_ARG_V1364_778[0][0]) if shen_consp(KL_ARG_V1364_778[0]) else False) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_779 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_779)][(-1)]
shen_add_fun('shen.<colon>', shen_x60colonx62, 1)

@tail_recursion
def shen_x60commax62(KL_ARG_V1369_780):

    class KL_Context:
        KL_LOC_Result_781 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_781', (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1369_780[0][1], tco_apply(shen_hdtl, [KL_ARG_V1369_780])])[0], symdic.symdic_shen_skip]) if ((44 == KL_ARG_V1369_780[0][0]) if shen_consp(KL_ARG_V1369_780[0]) else False) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_781 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_781)][(-1)]
shen_add_fun('shen.<comma>', shen_x60commax62, 1)

@tail_recursion
def shen_x60equalx62(KL_ARG_V1374_782):

    class KL_Context:
        KL_LOC_Result_783 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_783', (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1374_782[0][1], tco_apply(shen_hdtl, [KL_ARG_V1374_782])])[0], symdic.symdic_shen_skip]) if ((61 == KL_ARG_V1374_782[0][0]) if shen_consp(KL_ARG_V1374_782[0]) else False) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_783 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_783)][(-1)]
shen_add_fun('shen.<equal>', shen_x60equalx62, 1)

@tail_recursion
def shen_x60minusx62(KL_ARG_V1379_784):

    class KL_Context:
        KL_LOC_Result_785 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_785', (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1379_784[0][1], tco_apply(shen_hdtl, [KL_ARG_V1379_784])])[0], symdic.symdic_shen_skip]) if ((45 == KL_ARG_V1379_784[0][0]) if shen_consp(KL_ARG_V1379_784[0]) else False) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_785 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_785)][(-1)]
shen_add_fun('shen.<minus>', shen_x60minusx62, 1)

@tail_recursion
def shen_x60lrbx62(KL_ARG_V1384_786):

    class KL_Context:
        KL_LOC_Result_787 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_787', (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1384_786[0][1], tco_apply(shen_hdtl, [KL_ARG_V1384_786])])[0], symdic.symdic_shen_skip]) if ((40 == KL_ARG_V1384_786[0][0]) if shen_consp(KL_ARG_V1384_786[0]) else False) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_787 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_787)][(-1)]
shen_add_fun('shen.<lrb>', shen_x60lrbx62, 1)

@tail_recursion
def shen_x60rrbx62(KL_ARG_V1389_788):

    class KL_Context:
        KL_LOC_Result_789 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_789', (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1389_788[0][1], tco_apply(shen_hdtl, [KL_ARG_V1389_788])])[0], symdic.symdic_shen_skip]) if ((41 == KL_ARG_V1389_788[0][0]) if shen_consp(KL_ARG_V1389_788[0]) else False) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_789 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_789)][(-1)]
shen_add_fun('shen.<rrb>', shen_x60rrbx62, 1)

@tail_recursion
def shen_x60atomx62(KL_ARG_V1394_790):

    class KL_Context:
        KL_LOC_Result_791 = None
        KL_LOC_Parse_shen_x60strx62_792 = None
        KL_LOC_Result_793 = None
        KL_LOC_Parse_shen_x60numberx62_794 = None
        KL_LOC_Result_795 = None
        KL_LOC_Parse_shen_x60symx62_796 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_791', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60strx62_792', tco_apply(shen_x60strx62, [KL_ARG_V1394_790])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60strx62_792[0], tco_apply(shen_controlx45chars, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60strx62_792])])]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60strx62_792)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_793', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60numberx62_794', tco_apply(shen_x60numberx62, [KL_ARG_V1394_790])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60numberx62_794[0], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60numberx62_794])]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60numberx62_794)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_795', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60symx62_796', tco_apply(shen_x60symx62, [KL_ARG_V1394_790])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60symx62_796[0], ([symdic.symdic_kl_vector, [0, []]] if (tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60symx62_796]) == '<>') else shen_intern(tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60symx62_796])))]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60symx62_796)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_795 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_795)][(-1)] if (KL_CTX.KL_LOC_Result_793 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_793)][(-1)] if (KL_CTX.KL_LOC_Result_791 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_791)][(-1)]
shen_add_fun('shen.<atom>', shen_x60atomx62, 1)

@tail_recursion
def shen_controlx45chars(KL_ARG_V1395_797):

    class KL_Context:
        KL_LOC_CodePoint_798 = None
        KL_LOC_AfterCodePoint_799 = None
    KL_CTX = KL_Context()
    global symdic
    return ('' if ([] == KL_ARG_V1395_797) else ([setattr(KL_CTX, 'KL_LOC_CodePoint_798', tco_apply(shen_codex45point, [KL_ARG_V1395_797[1][1]])), [setattr(KL_CTX, 'KL_LOC_AfterCodePoint_799', tco_apply(shen_afterx45codepoint, [KL_ARG_V1395_797[1][1]])), tail_call(kl_x64s, [chr(tco_apply(shen_decimalise, [KL_CTX.KL_LOC_CodePoint_798])), tco_apply(shen_controlx45chars, [KL_CTX.KL_LOC_AfterCodePoint_799])])][(-1)]][(-1)] if (((('#' == KL_ARG_V1395_797[1][0]) if shen_consp(KL_ARG_V1395_797[1]) else False) if ('c' == KL_ARG_V1395_797[0]) else False) if shen_consp(KL_ARG_V1395_797) else False) else (tail_call(kl_x64s, [KL_ARG_V1395_797[0], tco_apply(shen_controlx45chars, [KL_ARG_V1395_797[1]])]) if shen_consp(KL_ARG_V1395_797) else (tail_call(shen_sysx45error, [symdic.symdic_shen_controlx45chars]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.control-chars', shen_controlx45chars, 1)

@tail_recursion
def shen_codex45point(KL_ARG_V1398_800):
    global symdic
    return ('' if ((';' == KL_ARG_V1398_800[0]) if shen_consp(KL_ARG_V1398_800) else False) else ([KL_ARG_V1398_800[0], tco_apply(shen_codex45point, [KL_ARG_V1398_800[1]])] if (tco_apply(kl_elementx63, [KL_ARG_V1398_800[0], ['0', ['1', ['2', ['3', ['4', ['5', ['6', ['7', ['8', ['9', ['0', []]]]]]]]]]]]]) if shen_consp(KL_ARG_V1398_800) else False) else (shen_simple_error(('code point parse error ' + tco_apply(shen_app, [KL_ARG_V1398_800, '\r\n', symdic.symdic_shen_a]))) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.code-point', shen_codex45point, 1)

@tail_recursion
def shen_afterx45codepoint(KL_ARG_V1403_801):
    global symdic
    return ([] if ([] == KL_ARG_V1403_801) else (KL_ARG_V1403_801[1] if ((';' == KL_ARG_V1403_801[0]) if shen_consp(KL_ARG_V1403_801) else False) else (tail_call(shen_afterx45codepoint, [KL_ARG_V1403_801[1]]) if shen_consp(KL_ARG_V1403_801) else (tail_call(shen_sysx45error, [symdic.symdic_shen_afterx45codepoint]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.after-codepoint', shen_afterx45codepoint, 1)

@tail_recursion
def shen_decimalise(KL_ARG_V1404_802):
    global symdic
    return tail_call(shen_pre, [tco_apply(kl_reverse, [tco_apply(shen_digitsx45x62integers, [KL_ARG_V1404_802])]), 0])
shen_add_fun('shen.decimalise', shen_decimalise, 1)

@tail_recursion
def shen_digitsx45x62integers(KL_ARG_V1409_803):
    global symdic
    return ([0, tco_apply(shen_digitsx45x62integers, [KL_ARG_V1409_803[1]])] if (('0' == KL_ARG_V1409_803[0]) if shen_consp(KL_ARG_V1409_803) else False) else ([1, tco_apply(shen_digitsx45x62integers, [KL_ARG_V1409_803[1]])] if (('1' == KL_ARG_V1409_803[0]) if shen_consp(KL_ARG_V1409_803) else False) else ([2, tco_apply(shen_digitsx45x62integers, [KL_ARG_V1409_803[1]])] if (('2' == KL_ARG_V1409_803[0]) if shen_consp(KL_ARG_V1409_803) else False) else ([3, tco_apply(shen_digitsx45x62integers, [KL_ARG_V1409_803[1]])] if (('3' == KL_ARG_V1409_803[0]) if shen_consp(KL_ARG_V1409_803) else False) else ([4, tco_apply(shen_digitsx45x62integers, [KL_ARG_V1409_803[1]])] if (('4' == KL_ARG_V1409_803[0]) if shen_consp(KL_ARG_V1409_803) else False) else ([5, tco_apply(shen_digitsx45x62integers, [KL_ARG_V1409_803[1]])] if (('5' == KL_ARG_V1409_803[0]) if shen_consp(KL_ARG_V1409_803) else False) else ([6, tco_apply(shen_digitsx45x62integers, [KL_ARG_V1409_803[1]])] if (('6' == KL_ARG_V1409_803[0]) if shen_consp(KL_ARG_V1409_803) else False) else ([7, tco_apply(shen_digitsx45x62integers, [KL_ARG_V1409_803[1]])] if (('7' == KL_ARG_V1409_803[0]) if shen_consp(KL_ARG_V1409_803) else False) else ([8, tco_apply(shen_digitsx45x62integers, [KL_ARG_V1409_803[1]])] if (('8' == KL_ARG_V1409_803[0]) if shen_consp(KL_ARG_V1409_803) else False) else ([9, tco_apply(shen_digitsx45x62integers, [KL_ARG_V1409_803[1]])] if (('9' == KL_ARG_V1409_803[0]) if shen_consp(KL_ARG_V1409_803) else False) else ([] if True else shen_simple_error('condition failure'))))))))))))
shen_add_fun('shen.digits->integers', shen_digitsx45x62integers, 1)

@tail_recursion
def shen_x60symx62(KL_ARG_V1414_804):

    class KL_Context:
        KL_LOC_Result_805 = None
        KL_LOC_Parse_shen_x60alphax62_806 = None
        KL_LOC_Parse_shen_x60alphanumsx62_807 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_805', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60alphax62_806', tco_apply(shen_x60alphax62, [KL_ARG_V1414_804])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60alphanumsx62_807', tco_apply(shen_x60alphanumsx62, [KL_CTX.KL_LOC_Parse_shen_x60alphax62_806])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60alphanumsx62_807[0], tco_apply(kl_x64s, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60alphax62_806]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60alphanumsx62_807])])]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60alphanumsx62_807)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60alphax62_806)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_805 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_805)][(-1)]
shen_add_fun('shen.<sym>', shen_x60symx62, 1)

@tail_recursion
def shen_x60alphanumsx62(KL_ARG_V1419_808):

    class KL_Context:
        KL_LOC_Result_809 = None
        KL_LOC_Parse_shen_x60alphanumx62_810 = None
        KL_LOC_Parse_shen_x60alphanumsx62_811 = None
        KL_LOC_Result_812 = None
        KL_LOC_Parse_x60ex62_813 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_809', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60alphanumx62_810', tco_apply(shen_x60alphanumx62, [KL_ARG_V1419_808])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60alphanumsx62_811', tco_apply(shen_x60alphanumsx62, [KL_CTX.KL_LOC_Parse_shen_x60alphanumx62_810])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60alphanumsx62_811[0], tco_apply(kl_x64s, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60alphanumx62_810]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60alphanumsx62_811])])]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60alphanumsx62_811)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60alphanumx62_810)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_812', [setattr(KL_CTX, 'KL_LOC_Parse_x60ex62_813', tco_apply(kl_x60ex62, [KL_ARG_V1419_808])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_x60ex62_813[0], '']) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_x60ex62_813)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_812 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_812)][(-1)] if (KL_CTX.KL_LOC_Result_809 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_809)][(-1)]
shen_add_fun('shen.<alphanums>', shen_x60alphanumsx62, 1)

@tail_recursion
def shen_x60alphanumx62(KL_ARG_V1424_814):

    class KL_Context:
        KL_LOC_Result_815 = None
        KL_LOC_Parse_shen_x60alphax62_816 = None
        KL_LOC_Result_817 = None
        KL_LOC_Parse_shen_x60numx62_818 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_815', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60alphax62_816', tco_apply(shen_x60alphax62, [KL_ARG_V1424_814])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60alphax62_816[0], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60alphax62_816])]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60alphax62_816)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_817', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60numx62_818', tco_apply(shen_x60numx62, [KL_ARG_V1424_814])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60numx62_818[0], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60numx62_818])]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60numx62_818)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_817 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_817)][(-1)] if (KL_CTX.KL_LOC_Result_815 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_815)][(-1)]
shen_add_fun('shen.<alphanum>', shen_x60alphanumx62, 1)

@tail_recursion
def shen_x60numx62(KL_ARG_V1429_819):

    class KL_Context:
        KL_LOC_Result_820 = None
        KL_LOC_Parse_Byte_821 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_820', ([setattr(KL_CTX, 'KL_LOC_Parse_Byte_821', KL_ARG_V1429_819[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1429_819[0][1], tco_apply(shen_hdtl, [KL_ARG_V1429_819])])[0], chr(KL_CTX.KL_LOC_Parse_Byte_821)]) if tco_apply(shen_numbytex63, [KL_CTX.KL_LOC_Parse_Byte_821]) else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V1429_819[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_820 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_820)][(-1)]
shen_add_fun('shen.<num>', shen_x60numx62, 1)

@tail_recursion
def shen_numbytex63(KL_ARG_V1434_822):
    global symdic
    return (True if (48 == KL_ARG_V1434_822) else (True if (49 == KL_ARG_V1434_822) else (True if (50 == KL_ARG_V1434_822) else (True if (51 == KL_ARG_V1434_822) else (True if (52 == KL_ARG_V1434_822) else (True if (53 == KL_ARG_V1434_822) else (True if (54 == KL_ARG_V1434_822) else (True if (55 == KL_ARG_V1434_822) else (True if (56 == KL_ARG_V1434_822) else (True if (57 == KL_ARG_V1434_822) else (False if True else shen_simple_error('condition failure'))))))))))))
shen_add_fun('shen.numbyte?', shen_numbytex63, 1)

@tail_recursion
def shen_x60alphax62(KL_ARG_V1439_823):

    class KL_Context:
        KL_LOC_Result_824 = None
        KL_LOC_Parse_Byte_825 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_824', ([setattr(KL_CTX, 'KL_LOC_Parse_Byte_825', KL_ARG_V1439_823[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1439_823[0][1], tco_apply(shen_hdtl, [KL_ARG_V1439_823])])[0], chr(KL_CTX.KL_LOC_Parse_Byte_825)]) if tco_apply(shen_symbolx45codex63, [KL_CTX.KL_LOC_Parse_Byte_825]) else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V1439_823[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_824 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_824)][(-1)]
shen_add_fun('shen.<alpha>', shen_x60alphax62, 1)

@tail_recursion
def shen_symbolx45codex63(KL_ARG_V1440_826):
    global symdic
    return (True if (KL_ARG_V1440_826 == 126) else (True if ((KL_ARG_V1440_826 < 123) if (KL_ARG_V1440_826 > 94) else False) else (True if ((KL_ARG_V1440_826 < 91) if (KL_ARG_V1440_826 > 59) else False) else (True if (((not (KL_ARG_V1440_826 == 44)) if (KL_ARG_V1440_826 < 58) else False) if (KL_ARG_V1440_826 > 41) else False) else (True if ((KL_ARG_V1440_826 < 40) if (KL_ARG_V1440_826 > 34) else False) else (KL_ARG_V1440_826 == 33))))))
shen_add_fun('shen.symbol-code?', shen_symbolx45codex63, 1)

@tail_recursion
def shen_x60strx62(KL_ARG_V1445_827):

    class KL_Context:
        KL_LOC_Result_828 = None
        KL_LOC_Parse_shen_x60dbqx62_829 = None
        KL_LOC_Parse_shen_x60strcontentsx62_830 = None
        KL_LOC_Parse_shen_x60dbqx62_831 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_828', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60dbqx62_829', tco_apply(shen_x60dbqx62, [KL_ARG_V1445_827])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60strcontentsx62_830', tco_apply(shen_x60strcontentsx62, [KL_CTX.KL_LOC_Parse_shen_x60dbqx62_829])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60dbqx62_831', tco_apply(shen_x60dbqx62, [KL_CTX.KL_LOC_Parse_shen_x60strcontentsx62_830])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60dbqx62_831[0], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60strcontentsx62_830])]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60dbqx62_831)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60strcontentsx62_830)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60dbqx62_829)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_828 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_828)][(-1)]
shen_add_fun('shen.<str>', shen_x60strx62, 1)

@tail_recursion
def shen_x60dbqx62(KL_ARG_V1450_832):

    class KL_Context:
        KL_LOC_Result_833 = None
        KL_LOC_Parse_Byte_834 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_833', ([setattr(KL_CTX, 'KL_LOC_Parse_Byte_834', KL_ARG_V1450_832[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1450_832[0][1], tco_apply(shen_hdtl, [KL_ARG_V1450_832])])[0], KL_CTX.KL_LOC_Parse_Byte_834]) if (KL_CTX.KL_LOC_Parse_Byte_834 == 34) else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V1450_832[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_833 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_833)][(-1)]
shen_add_fun('shen.<dbq>', shen_x60dbqx62, 1)

@tail_recursion
def shen_x60strcontentsx62(KL_ARG_V1455_835):

    class KL_Context:
        KL_LOC_Result_836 = None
        KL_LOC_Parse_shen_x60strcx62_837 = None
        KL_LOC_Parse_shen_x60strcontentsx62_838 = None
        KL_LOC_Result_839 = None
        KL_LOC_Parse_x60ex62_840 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_836', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60strcx62_837', tco_apply(shen_x60strcx62, [KL_ARG_V1455_835])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60strcontentsx62_838', tco_apply(shen_x60strcontentsx62, [KL_CTX.KL_LOC_Parse_shen_x60strcx62_837])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60strcontentsx62_838[0], [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60strcx62_837]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60strcontentsx62_838])]]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60strcontentsx62_838)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60strcx62_837)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_839', [setattr(KL_CTX, 'KL_LOC_Parse_x60ex62_840', tco_apply(kl_x60ex62, [KL_ARG_V1455_835])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_x60ex62_840[0], []]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_x60ex62_840)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_839 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_839)][(-1)] if (KL_CTX.KL_LOC_Result_836 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_836)][(-1)]
shen_add_fun('shen.<strcontents>', shen_x60strcontentsx62, 1)

@tail_recursion
def shen_x60bytex62(KL_ARG_V1460_841):

    class KL_Context:
        KL_LOC_Result_842 = None
        KL_LOC_Parse_Byte_843 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_842', ([setattr(KL_CTX, 'KL_LOC_Parse_Byte_843', KL_ARG_V1460_841[0][0]), tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1460_841[0][1], tco_apply(shen_hdtl, [KL_ARG_V1460_841])])[0], chr(KL_CTX.KL_LOC_Parse_Byte_843)])][(-1)] if shen_consp(KL_ARG_V1460_841[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_842 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_842)][(-1)]
shen_add_fun('shen.<byte>', shen_x60bytex62, 1)

@tail_recursion
def shen_x60strcx62(KL_ARG_V1465_844):

    class KL_Context:
        KL_LOC_Result_845 = None
        KL_LOC_Parse_Byte_846 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_845', ([setattr(KL_CTX, 'KL_LOC_Parse_Byte_846', KL_ARG_V1465_844[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1465_844[0][1], tco_apply(shen_hdtl, [KL_ARG_V1465_844])])[0], chr(KL_CTX.KL_LOC_Parse_Byte_846)]) if (not (KL_CTX.KL_LOC_Parse_Byte_846 == 34)) else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V1465_844[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_845 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_845)][(-1)]
shen_add_fun('shen.<strc>', shen_x60strcx62, 1)

@tail_recursion
def shen_x60numberx62(KL_ARG_V1470_847):

    class KL_Context:
        KL_LOC_Result_848 = None
        KL_LOC_Parse_shen_x60minusx62_849 = None
        KL_LOC_Parse_shen_x60numberx62_850 = None
        KL_LOC_Result_851 = None
        KL_LOC_Parse_shen_x60plusx62_852 = None
        KL_LOC_Parse_shen_x60numberx62_853 = None
        KL_LOC_Result_854 = None
        KL_LOC_Parse_shen_x60predigitsx62_855 = None
        KL_LOC_Parse_shen_x60stopx62_856 = None
        KL_LOC_Parse_shen_x60postdigitsx62_857 = None
        KL_LOC_Parse_shen_x60Ex62_858 = None
        KL_LOC_Parse_shen_x60log10x62_859 = None
        KL_LOC_Result_860 = None
        KL_LOC_Parse_shen_x60digitsx62_861 = None
        KL_LOC_Parse_shen_x60Ex62_862 = None
        KL_LOC_Parse_shen_x60log10x62_863 = None
        KL_LOC_Result_864 = None
        KL_LOC_Parse_shen_x60predigitsx62_865 = None
        KL_LOC_Parse_shen_x60stopx62_866 = None
        KL_LOC_Parse_shen_x60postdigitsx62_867 = None
        KL_LOC_Result_868 = None
        KL_LOC_Parse_shen_x60digitsx62_869 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_848', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60minusx62_849', tco_apply(shen_x60minusx62, [KL_ARG_V1470_847])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60numberx62_850', tco_apply(shen_x60numberx62, [KL_CTX.KL_LOC_Parse_shen_x60minusx62_849])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60numberx62_850[0], (0 - tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60numberx62_850]))]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60numberx62_850)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60minusx62_849)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_851', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60plusx62_852', tco_apply(shen_x60plusx62, [KL_ARG_V1470_847])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60numberx62_853', tco_apply(shen_x60numberx62, [KL_CTX.KL_LOC_Parse_shen_x60plusx62_852])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60numberx62_853[0], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60numberx62_853])]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60numberx62_853)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60plusx62_852)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_854', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60predigitsx62_855', tco_apply(shen_x60predigitsx62, [KL_ARG_V1470_847])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60stopx62_856', tco_apply(shen_x60stopx62, [KL_CTX.KL_LOC_Parse_shen_x60predigitsx62_855])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60postdigitsx62_857', tco_apply(shen_x60postdigitsx62, [KL_CTX.KL_LOC_Parse_shen_x60stopx62_856])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60Ex62_858', tco_apply(shen_x60Ex62, [KL_CTX.KL_LOC_Parse_shen_x60postdigitsx62_857])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60log10x62_859', tco_apply(shen_x60log10x62, [KL_CTX.KL_LOC_Parse_shen_x60Ex62_858])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60log10x62_859[0], (tco_apply(shen_expt, [10, tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60log10x62_859])]) * (tco_apply(shen_pre, [tco_apply(kl_reverse, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60predigitsx62_855])]), 0]) + tco_apply(shen_post, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60postdigitsx62_857]), 1])))]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60log10x62_859)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60Ex62_858)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60postdigitsx62_857)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60stopx62_856)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60predigitsx62_855)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_860', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60digitsx62_861', tco_apply(shen_x60digitsx62, [KL_ARG_V1470_847])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60Ex62_862', tco_apply(shen_x60Ex62, [KL_CTX.KL_LOC_Parse_shen_x60digitsx62_861])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60log10x62_863', tco_apply(shen_x60log10x62, [KL_CTX.KL_LOC_Parse_shen_x60Ex62_862])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60log10x62_863[0], (tco_apply(shen_expt, [10, tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60log10x62_863])]) * tco_apply(shen_pre, [tco_apply(kl_reverse, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60digitsx62_861])]), 0]))]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60log10x62_863)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60Ex62_862)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60digitsx62_861)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_864', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60predigitsx62_865', tco_apply(shen_x60predigitsx62, [KL_ARG_V1470_847])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60stopx62_866', tco_apply(shen_x60stopx62, [KL_CTX.KL_LOC_Parse_shen_x60predigitsx62_865])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60postdigitsx62_867', tco_apply(shen_x60postdigitsx62, [KL_CTX.KL_LOC_Parse_shen_x60stopx62_866])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60postdigitsx62_867[0], (tco_apply(shen_pre, [tco_apply(kl_reverse, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60predigitsx62_865])]), 0]) + tco_apply(shen_post, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60postdigitsx62_867]), 1]))]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60postdigitsx62_867)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60stopx62_866)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60predigitsx62_865)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_868', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60digitsx62_869', tco_apply(shen_x60digitsx62, [KL_ARG_V1470_847])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60digitsx62_869[0], tco_apply(shen_pre, [tco_apply(kl_reverse, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60digitsx62_869])]), 0])]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60digitsx62_869)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_868 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_868)][(-1)] if (KL_CTX.KL_LOC_Result_864 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_864)][(-1)] if (KL_CTX.KL_LOC_Result_860 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_860)][(-1)] if (KL_CTX.KL_LOC_Result_854 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_854)][(-1)] if (KL_CTX.KL_LOC_Result_851 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_851)][(-1)] if (KL_CTX.KL_LOC_Result_848 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_848)][(-1)]
shen_add_fun('shen.<number>', shen_x60numberx62, 1)

@tail_recursion
def shen_x60Ex62(KL_ARG_V1475_870):

    class KL_Context:
        KL_LOC_Result_871 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_871', (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1475_870[0][1], tco_apply(shen_hdtl, [KL_ARG_V1475_870])])[0], symdic.symdic_shen_skip]) if ((101 == KL_ARG_V1475_870[0][0]) if shen_consp(KL_ARG_V1475_870[0]) else False) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_871 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_871)][(-1)]
shen_add_fun('shen.<E>', shen_x60Ex62, 1)

@tail_recursion
def shen_x60log10x62(KL_ARG_V1480_872):

    class KL_Context:
        KL_LOC_Result_873 = None
        KL_LOC_Parse_shen_x60minusx62_874 = None
        KL_LOC_Parse_shen_x60digitsx62_875 = None
        KL_LOC_Result_876 = None
        KL_LOC_Parse_shen_x60digitsx62_877 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_873', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60minusx62_874', tco_apply(shen_x60minusx62, [KL_ARG_V1480_872])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60digitsx62_875', tco_apply(shen_x60digitsx62, [KL_CTX.KL_LOC_Parse_shen_x60minusx62_874])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60digitsx62_875[0], (0 - tco_apply(shen_pre, [tco_apply(kl_reverse, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60digitsx62_875])]), 0]))]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60digitsx62_875)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60minusx62_874)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_876', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60digitsx62_877', tco_apply(shen_x60digitsx62, [KL_ARG_V1480_872])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60digitsx62_877[0], tco_apply(shen_pre, [tco_apply(kl_reverse, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60digitsx62_877])]), 0])]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60digitsx62_877)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_876 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_876)][(-1)] if (KL_CTX.KL_LOC_Result_873 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_873)][(-1)]
shen_add_fun('shen.<log10>', shen_x60log10x62, 1)

@tail_recursion
def shen_x60plusx62(KL_ARG_V1485_878):

    class KL_Context:
        KL_LOC_Result_879 = None
        KL_LOC_Parse_Byte_880 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_879', ([setattr(KL_CTX, 'KL_LOC_Parse_Byte_880', KL_ARG_V1485_878[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1485_878[0][1], tco_apply(shen_hdtl, [KL_ARG_V1485_878])])[0], KL_CTX.KL_LOC_Parse_Byte_880]) if (KL_CTX.KL_LOC_Parse_Byte_880 == 43) else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V1485_878[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_879 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_879)][(-1)]
shen_add_fun('shen.<plus>', shen_x60plusx62, 1)

@tail_recursion
def shen_x60stopx62(KL_ARG_V1490_881):

    class KL_Context:
        KL_LOC_Result_882 = None
        KL_LOC_Parse_Byte_883 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_882', ([setattr(KL_CTX, 'KL_LOC_Parse_Byte_883', KL_ARG_V1490_881[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1490_881[0][1], tco_apply(shen_hdtl, [KL_ARG_V1490_881])])[0], KL_CTX.KL_LOC_Parse_Byte_883]) if (KL_CTX.KL_LOC_Parse_Byte_883 == 46) else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V1490_881[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_882 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_882)][(-1)]
shen_add_fun('shen.<stop>', shen_x60stopx62, 1)

@tail_recursion
def shen_x60predigitsx62(KL_ARG_V1495_884):

    class KL_Context:
        KL_LOC_Result_885 = None
        KL_LOC_Parse_shen_x60digitsx62_886 = None
        KL_LOC_Result_887 = None
        KL_LOC_Parse_x60ex62_888 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_885', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60digitsx62_886', tco_apply(shen_x60digitsx62, [KL_ARG_V1495_884])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60digitsx62_886[0], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60digitsx62_886])]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60digitsx62_886)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_887', [setattr(KL_CTX, 'KL_LOC_Parse_x60ex62_888', tco_apply(kl_x60ex62, [KL_ARG_V1495_884])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_x60ex62_888[0], []]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_x60ex62_888)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_887 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_887)][(-1)] if (KL_CTX.KL_LOC_Result_885 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_885)][(-1)]
shen_add_fun('shen.<predigits>', shen_x60predigitsx62, 1)

@tail_recursion
def shen_x60postdigitsx62(KL_ARG_V1500_889):

    class KL_Context:
        KL_LOC_Result_890 = None
        KL_LOC_Parse_shen_x60digitsx62_891 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_890', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60digitsx62_891', tco_apply(shen_x60digitsx62, [KL_ARG_V1500_889])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60digitsx62_891[0], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60digitsx62_891])]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60digitsx62_891)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_890 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_890)][(-1)]
shen_add_fun('shen.<postdigits>', shen_x60postdigitsx62, 1)

@tail_recursion
def shen_x60digitsx62(KL_ARG_V1505_892):

    class KL_Context:
        KL_LOC_Result_893 = None
        KL_LOC_Parse_shen_x60digitx62_894 = None
        KL_LOC_Parse_shen_x60digitsx62_895 = None
        KL_LOC_Result_896 = None
        KL_LOC_Parse_shen_x60digitx62_897 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_893', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60digitx62_894', tco_apply(shen_x60digitx62, [KL_ARG_V1505_892])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60digitsx62_895', tco_apply(shen_x60digitsx62, [KL_CTX.KL_LOC_Parse_shen_x60digitx62_894])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60digitsx62_895[0], [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60digitx62_894]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60digitsx62_895])]]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60digitsx62_895)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60digitx62_894)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_896', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60digitx62_897', tco_apply(shen_x60digitx62, [KL_ARG_V1505_892])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60digitx62_897[0], [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60digitx62_897]), []]]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60digitx62_897)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_896 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_896)][(-1)] if (KL_CTX.KL_LOC_Result_893 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_893)][(-1)]
shen_add_fun('shen.<digits>', shen_x60digitsx62, 1)

@tail_recursion
def shen_x60digitx62(KL_ARG_V1510_898):

    class KL_Context:
        KL_LOC_Result_899 = None
        KL_LOC_Parse_X_900 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_899', ([setattr(KL_CTX, 'KL_LOC_Parse_X_900', KL_ARG_V1510_898[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1510_898[0][1], tco_apply(shen_hdtl, [KL_ARG_V1510_898])])[0], tco_apply(shen_bytex45x62digit, [KL_CTX.KL_LOC_Parse_X_900])]) if tco_apply(shen_numbytex63, [KL_CTX.KL_LOC_Parse_X_900]) else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V1510_898[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_899 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_899)][(-1)]
shen_add_fun('shen.<digit>', shen_x60digitx62, 1)

@tail_recursion
def shen_bytex45x62digit(KL_ARG_V1511_901):
    global symdic
    return (0 if (48 == KL_ARG_V1511_901) else (1 if (49 == KL_ARG_V1511_901) else (2 if (50 == KL_ARG_V1511_901) else (3 if (51 == KL_ARG_V1511_901) else (4 if (52 == KL_ARG_V1511_901) else (5 if (53 == KL_ARG_V1511_901) else (6 if (54 == KL_ARG_V1511_901) else (7 if (55 == KL_ARG_V1511_901) else (8 if (56 == KL_ARG_V1511_901) else (9 if (57 == KL_ARG_V1511_901) else (tail_call(shen_sysx45error, [symdic.symdic_shen_bytex45x62digit]) if True else shen_simple_error('condition failure'))))))))))))
shen_add_fun('shen.byte->digit', shen_bytex45x62digit, 1)

@tail_recursion
def shen_pre(KL_ARG_V1514_902, KL_ARG_V1515_903):
    global symdic
    return (0 if ([] == KL_ARG_V1514_902) else (((tco_apply(shen_expt, [10, KL_ARG_V1515_903]) * KL_ARG_V1514_902[0]) + tco_apply(shen_pre, [KL_ARG_V1514_902[1], (KL_ARG_V1515_903 + 1)])) if shen_consp(KL_ARG_V1514_902) else (tail_call(shen_sysx45error, [symdic.symdic_shen_pre]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.pre', shen_pre, 2)

@tail_recursion
def shen_post(KL_ARG_V1518_904, KL_ARG_V1519_905):
    global symdic
    return (0 if ([] == KL_ARG_V1518_904) else (((tco_apply(shen_expt, [10, (0 - KL_ARG_V1519_905)]) * KL_ARG_V1518_904[0]) + tco_apply(shen_post, [KL_ARG_V1518_904[1], (KL_ARG_V1519_905 + 1)])) if shen_consp(KL_ARG_V1518_904) else (tail_call(shen_sysx45error, [symdic.symdic_shen_post]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.post', shen_post, 2)

@tail_recursion
def shen_expt(KL_ARG_V1522_906, KL_ARG_V1523_907):
    global symdic
    return (1 if (0 == KL_ARG_V1523_907) else ((KL_ARG_V1522_906 * tco_apply(shen_expt, [KL_ARG_V1522_906, (KL_ARG_V1523_907 - 1)])) if (KL_ARG_V1523_907 > 0) else ((1 * (tco_apply(shen_expt, [KL_ARG_V1522_906, (KL_ARG_V1523_907 + 1)]) / KL_ARG_V1522_906)) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.expt', shen_expt, 2)

@tail_recursion
def shen_x60st_input1x62(KL_ARG_V1528_908):

    class KL_Context:
        KL_LOC_Result_909 = None
        KL_LOC_Parse_shen_x60st_inputx62_910 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_909', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_inputx62_910', tco_apply(shen_x60st_inputx62, [KL_ARG_V1528_908])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_910[0], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_910])]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_910)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_909 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_909)][(-1)]
shen_add_fun('shen.<st_input1>', shen_x60st_input1x62, 1)

@tail_recursion
def shen_x60st_input2x62(KL_ARG_V1533_911):

    class KL_Context:
        KL_LOC_Result_912 = None
        KL_LOC_Parse_shen_x60st_inputx62_913 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_912', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_inputx62_913', tco_apply(shen_x60st_inputx62, [KL_ARG_V1533_911])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_913[0], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_913])]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_913)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_912 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_912)][(-1)]
shen_add_fun('shen.<st_input2>', shen_x60st_input2x62, 1)

@tail_recursion
def shen_x60commentx62(KL_ARG_V1538_914):

    class KL_Context:
        KL_LOC_Result_915 = None
        KL_LOC_Parse_shen_x60singlelinex62_916 = None
        KL_LOC_Result_917 = None
        KL_LOC_Parse_shen_x60multilinex62_918 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_915', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60singlelinex62_916', tco_apply(shen_x60singlelinex62, [KL_ARG_V1538_914])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60singlelinex62_916[0], symdic.symdic_shen_skip]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60singlelinex62_916)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_917', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60multilinex62_918', tco_apply(shen_x60multilinex62, [KL_ARG_V1538_914])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60multilinex62_918[0], symdic.symdic_shen_skip]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60multilinex62_918)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_917 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_917)][(-1)] if (KL_CTX.KL_LOC_Result_915 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_915)][(-1)]
shen_add_fun('shen.<comment>', shen_x60commentx62, 1)

@tail_recursion
def shen_x60singlelinex62(KL_ARG_V1543_919):

    class KL_Context:
        KL_LOC_Result_920 = None
        KL_LOC_Parse_shen_x60backslashx62_921 = None
        KL_LOC_Parse_shen_x60backslashx62_922 = None
        KL_LOC_Parse_shen_x60anysinglex62_923 = None
        KL_LOC_Parse_shen_x60returnx62_924 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_920', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60backslashx62_921', tco_apply(shen_x60backslashx62, [KL_ARG_V1543_919])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60backslashx62_922', tco_apply(shen_x60backslashx62, [KL_CTX.KL_LOC_Parse_shen_x60backslashx62_921])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60anysinglex62_923', tco_apply(shen_x60anysinglex62, [KL_CTX.KL_LOC_Parse_shen_x60backslashx62_922])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60returnx62_924', tco_apply(shen_x60returnx62, [KL_CTX.KL_LOC_Parse_shen_x60anysinglex62_923])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60returnx62_924[0], symdic.symdic_shen_skip]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60returnx62_924)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60anysinglex62_923)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60backslashx62_922)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60backslashx62_921)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_920 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_920)][(-1)]
shen_add_fun('shen.<singleline>', shen_x60singlelinex62, 1)

@tail_recursion
def shen_x60backslashx62(KL_ARG_V1548_925):

    class KL_Context:
        KL_LOC_Result_926 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_926', (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1548_925[0][1], tco_apply(shen_hdtl, [KL_ARG_V1548_925])])[0], symdic.symdic_shen_skip]) if ((92 == KL_ARG_V1548_925[0][0]) if shen_consp(KL_ARG_V1548_925[0]) else False) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_926 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_926)][(-1)]
shen_add_fun('shen.<backslash>', shen_x60backslashx62, 1)

@tail_recursion
def shen_x60anysinglex62(KL_ARG_V1553_927):

    class KL_Context:
        KL_LOC_Result_928 = None
        KL_LOC_Parse_shen_x60nonx45returnx62_929 = None
        KL_LOC_Parse_shen_x60anysinglex62_930 = None
        KL_LOC_Result_931 = None
        KL_LOC_Parse_x60ex62_932 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_928', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60nonx45returnx62_929', tco_apply(shen_x60nonx45returnx62, [KL_ARG_V1553_927])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60anysinglex62_930', tco_apply(shen_x60anysinglex62, [KL_CTX.KL_LOC_Parse_shen_x60nonx45returnx62_929])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60anysinglex62_930[0], symdic.symdic_shen_skip]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60anysinglex62_930)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60nonx45returnx62_929)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_931', [setattr(KL_CTX, 'KL_LOC_Parse_x60ex62_932', tco_apply(kl_x60ex62, [KL_ARG_V1553_927])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_x60ex62_932[0], symdic.symdic_shen_skip]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_x60ex62_932)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_931 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_931)][(-1)] if (KL_CTX.KL_LOC_Result_928 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_928)][(-1)]
shen_add_fun('shen.<anysingle>', shen_x60anysinglex62, 1)

@tail_recursion
def shen_x60nonx45returnx62(KL_ARG_V1558_933):

    class KL_Context:
        KL_LOC_Result_934 = None
        KL_LOC_Parse_X_935 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_934', ([setattr(KL_CTX, 'KL_LOC_Parse_X_935', KL_ARG_V1558_933[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1558_933[0][1], tco_apply(shen_hdtl, [KL_ARG_V1558_933])])[0], symdic.symdic_shen_skip]) if (not tco_apply(kl_elementx63, [KL_CTX.KL_LOC_Parse_X_935, [10, [13, []]]])) else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V1558_933[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_934 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_934)][(-1)]
shen_add_fun('shen.<non-return>', shen_x60nonx45returnx62, 1)

@tail_recursion
def shen_x60returnx62(KL_ARG_V1563_936):

    class KL_Context:
        KL_LOC_Result_937 = None
        KL_LOC_Parse_X_938 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_937', ([setattr(KL_CTX, 'KL_LOC_Parse_X_938', KL_ARG_V1563_936[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1563_936[0][1], tco_apply(shen_hdtl, [KL_ARG_V1563_936])])[0], symdic.symdic_shen_skip]) if tco_apply(kl_elementx63, [KL_CTX.KL_LOC_Parse_X_938, [10, [13, []]]]) else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V1563_936[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_937 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_937)][(-1)]
shen_add_fun('shen.<return>', shen_x60returnx62, 1)

@tail_recursion
def shen_x60multilinex62(KL_ARG_V1568_939):

    class KL_Context:
        KL_LOC_Result_940 = None
        KL_LOC_Parse_shen_x60backslashx62_941 = None
        KL_LOC_Parse_shen_x60timesx62_942 = None
        KL_LOC_Parse_shen_x60anymultix62_943 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_940', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60backslashx62_941', tco_apply(shen_x60backslashx62, [KL_ARG_V1568_939])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60timesx62_942', tco_apply(shen_x60timesx62, [KL_CTX.KL_LOC_Parse_shen_x60backslashx62_941])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60anymultix62_943', tco_apply(shen_x60anymultix62, [KL_CTX.KL_LOC_Parse_shen_x60timesx62_942])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60anymultix62_943[0], symdic.symdic_shen_skip]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60anymultix62_943)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60timesx62_942)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60backslashx62_941)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_940 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_940)][(-1)]
shen_add_fun('shen.<multiline>', shen_x60multilinex62, 1)

@tail_recursion
def shen_x60timesx62(KL_ARG_V1573_944):

    class KL_Context:
        KL_LOC_Result_945 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_945', (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1573_944[0][1], tco_apply(shen_hdtl, [KL_ARG_V1573_944])])[0], symdic.symdic_shen_skip]) if ((42 == KL_ARG_V1573_944[0][0]) if shen_consp(KL_ARG_V1573_944[0]) else False) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_945 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_945)][(-1)]
shen_add_fun('shen.<times>', shen_x60timesx62, 1)

@tail_recursion
def shen_x60anymultix62(KL_ARG_V1578_946):

    class KL_Context:
        KL_LOC_Result_947 = None
        KL_LOC_Parse_shen_x60commentx62_948 = None
        KL_LOC_Parse_shen_x60anymultix62_949 = None
        KL_LOC_Result_950 = None
        KL_LOC_Parse_shen_x60timesx62_951 = None
        KL_LOC_Parse_shen_x60backslashx62_952 = None
        KL_LOC_Result_953 = None
        KL_LOC_Parse_X_954 = None
        KL_LOC_Parse_shen_x60anymultix62_955 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_947', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60commentx62_948', tco_apply(shen_x60commentx62, [KL_ARG_V1578_946])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60anymultix62_949', tco_apply(shen_x60anymultix62, [KL_CTX.KL_LOC_Parse_shen_x60commentx62_948])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60anymultix62_949[0], symdic.symdic_shen_skip]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60anymultix62_949)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60commentx62_948)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_950', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60timesx62_951', tco_apply(shen_x60timesx62, [KL_ARG_V1578_946])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60backslashx62_952', tco_apply(shen_x60backslashx62, [KL_CTX.KL_LOC_Parse_shen_x60timesx62_951])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60backslashx62_952[0], symdic.symdic_shen_skip]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60backslashx62_952)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60timesx62_951)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_953', ([setattr(KL_CTX, 'KL_LOC_Parse_X_954', KL_ARG_V1578_946[0][0]), [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60anymultix62_955', tco_apply(shen_x60anymultix62, [tco_apply(shen_pair, [KL_ARG_V1578_946[0][1], tco_apply(shen_hdtl, [KL_ARG_V1578_946])])])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60anymultix62_955[0], symdic.symdic_shen_skip]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60anymultix62_955)) else tco_apply(kl_fail, []))][(-1)]][(-1)] if shen_consp(KL_ARG_V1578_946[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_953 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_953)][(-1)] if (KL_CTX.KL_LOC_Result_950 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_950)][(-1)] if (KL_CTX.KL_LOC_Result_947 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_947)][(-1)]
shen_add_fun('shen.<anymulti>', shen_x60anymultix62, 1)

@tail_recursion
def shen_x60whitespacesx62(KL_ARG_V1583_956):

    class KL_Context:
        KL_LOC_Result_957 = None
        KL_LOC_Parse_shen_x60whitespacex62_958 = None
        KL_LOC_Parse_shen_x60whitespacesx62_959 = None
        KL_LOC_Result_960 = None
        KL_LOC_Parse_shen_x60whitespacex62_961 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_957', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60whitespacex62_958', tco_apply(shen_x60whitespacex62, [KL_ARG_V1583_956])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60whitespacesx62_959', tco_apply(shen_x60whitespacesx62, [KL_CTX.KL_LOC_Parse_shen_x60whitespacex62_958])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60whitespacesx62_959[0], symdic.symdic_shen_skip]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60whitespacesx62_959)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60whitespacex62_958)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_960', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60whitespacex62_961', tco_apply(shen_x60whitespacex62, [KL_ARG_V1583_956])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60whitespacex62_961[0], symdic.symdic_shen_skip]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60whitespacex62_961)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_960 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_960)][(-1)] if (KL_CTX.KL_LOC_Result_957 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_957)][(-1)]
shen_add_fun('shen.<whitespaces>', shen_x60whitespacesx62, 1)

@tail_recursion
def shen_x60whitespacex62(KL_ARG_V1588_962):

    class KL_Context:
        KL_LOC_Result_963 = None
        KL_LOC_Parse_X_964 = None
        KL_LOC_Parse_Case_965 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_963', ([setattr(KL_CTX, 'KL_LOC_Parse_X_964', KL_ARG_V1588_962[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1588_962[0][1], tco_apply(shen_hdtl, [KL_ARG_V1588_962])])[0], symdic.symdic_shen_skip]) if [setattr(KL_CTX, 'KL_LOC_Parse_Case_965', KL_CTX.KL_LOC_Parse_X_964), (True if (KL_CTX.KL_LOC_Parse_Case_965 == 32) else (True if (KL_CTX.KL_LOC_Parse_Case_965 == 13) else (True if (KL_CTX.KL_LOC_Parse_Case_965 == 10) else (KL_CTX.KL_LOC_Parse_Case_965 == 9))))][(-1)] else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V1588_962[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_963 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_963)][(-1)]
shen_add_fun('shen.<whitespace>', shen_x60whitespacex62, 1)

@tail_recursion
def shen_cons_form(KL_ARG_V1589_966):
    global symdic
    return ([] if ([] == KL_ARG_V1589_966) else ([symdic.symdic_kl_cons, [KL_ARG_V1589_966[0], KL_ARG_V1589_966[1][1]]] if (((((KL_ARG_V1589_966[1][0] == symdic.symdic_kl_barx33) if ([] == KL_ARG_V1589_966[1][1][1]) else False) if shen_consp(KL_ARG_V1589_966[1][1]) else False) if shen_consp(KL_ARG_V1589_966[1]) else False) if shen_consp(KL_ARG_V1589_966) else False) else ([symdic.symdic_kl_cons, [KL_ARG_V1589_966[0], [tco_apply(shen_cons_form, [KL_ARG_V1589_966[1]]), []]]] if shen_consp(KL_ARG_V1589_966) else (tail_call(shen_sysx45error, [symdic.symdic_shen_cons_form]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.cons_form', shen_cons_form, 1)

@tail_recursion
def shen_packagex45macro(KL_ARG_V1592_967, KL_ARG_V1593_968):

    class KL_Context:
        KL_LOC_ListofExceptions_969 = None
        KL_LOC_Record_970 = None
        KL_LOC_PackageNameDot_971 = None
    KL_CTX = KL_Context()
    global symdic
    return (tail_call(kl_append, [tco_apply(kl_explode, [KL_ARG_V1592_967[1][0]]), KL_ARG_V1593_968]) if (((([] == KL_ARG_V1592_967[1][1]) if shen_consp(KL_ARG_V1592_967[1]) else False) if (symdic.symdic_kl_x36 == KL_ARG_V1592_967[0]) else False) if shen_consp(KL_ARG_V1592_967) else False) else (tail_call(kl_append, [KL_ARG_V1592_967[1][1][1], KL_ARG_V1593_968]) if ((((shen_consp(KL_ARG_V1592_967[1][1]) if (symdic.symdic_kl_null == KL_ARG_V1592_967[1][0]) else False) if shen_consp(KL_ARG_V1592_967[1]) else False) if (symdic.symdic_kl_package == KL_ARG_V1592_967[0]) else False) if shen_consp(KL_ARG_V1592_967) else False) else ([setattr(KL_CTX, 'KL_LOC_ListofExceptions_969', tco_apply(shen_evalx45withoutx45macros, [KL_ARG_V1592_967[1][1][0]])), [setattr(KL_CTX, 'KL_LOC_Record_970', tco_apply(shen_recordx45exceptions, [KL_CTX.KL_LOC_ListofExceptions_969, KL_ARG_V1592_967[1][0]])), [setattr(KL_CTX, 'KL_LOC_PackageNameDot_971', shen_intern((str(KL_ARG_V1592_967[1][0]) + '.'))), tail_call(kl_append, [tco_apply(shen_packageh, [KL_CTX.KL_LOC_PackageNameDot_971, KL_CTX.KL_LOC_ListofExceptions_969, KL_ARG_V1592_967[1][1][1]]), KL_ARG_V1593_968])][(-1)]][(-1)]][(-1)] if (((shen_consp(KL_ARG_V1592_967[1][1]) if shen_consp(KL_ARG_V1592_967[1]) else False) if (symdic.symdic_kl_package == KL_ARG_V1592_967[0]) else False) if shen_consp(KL_ARG_V1592_967) else False) else ([KL_ARG_V1592_967, KL_ARG_V1593_968] if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.package-macro', shen_packagex45macro, 2)

@tail_recursion
def shen_recordx45exceptions(KL_ARG_V1594_972, KL_ARG_V1595_973):

    class KL_Context:
        KL_LOC_CurrExceptions_974 = None
        KL_LOC_AllExceptions_976 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_CurrExceptions_974', shen_try_except((lambda : tco_apply(kl_get, [KL_ARG_V1595_973, symdic.symdic_shen_externalx45symbols, shen_get(symdic.symdic_kl_x42propertyx45vectorx42)])), (lambda KL_ARG_E_975: []))), [setattr(KL_CTX, 'KL_LOC_AllExceptions_976', tco_apply(kl_union, [KL_ARG_V1594_972, KL_CTX.KL_LOC_CurrExceptions_974])), tail_call(kl_put, [KL_ARG_V1595_973, symdic.symdic_shen_externalx45symbols, KL_CTX.KL_LOC_AllExceptions_976, shen_get(symdic.symdic_kl_x42propertyx45vectorx42)])][(-1)]][(-1)]
shen_add_fun('shen.record-exceptions', shen_recordx45exceptions, 2)

@tail_recursion
def shen_packageh(KL_ARG_V1604_977, KL_ARG_V1605_978, KL_ARG_V1606_979):
    global symdic
    return ([tco_apply(shen_packageh, [KL_ARG_V1604_977, KL_ARG_V1605_978, KL_ARG_V1606_979[0]]), tco_apply(shen_packageh, [KL_ARG_V1604_977, KL_ARG_V1605_978, KL_ARG_V1606_979[1]])] if shen_consp(KL_ARG_V1606_979) else (KL_ARG_V1606_979 if (True if tco_apply(shen_sysfuncx63, [KL_ARG_V1606_979]) else (True if tco_apply(kl_variablex63, [KL_ARG_V1606_979]) else (True if tco_apply(kl_elementx63, [KL_ARG_V1606_979, KL_ARG_V1605_978]) else (True if tco_apply(shen_doubleunderlinex63, [KL_ARG_V1606_979]) else tco_apply(shen_singleunderlinex63, [KL_ARG_V1606_979]))))) else (tail_call(kl_concat, [KL_ARG_V1604_977, KL_ARG_V1606_979]) if ((not tco_apply(shen_prefixx63, [['s', ['h', ['e', ['n', ['.', []]]]]], tco_apply(kl_explode, [KL_ARG_V1606_979])])) if tco_apply(kl_symbolx63, [KL_ARG_V1606_979]) else False) else (KL_ARG_V1606_979 if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.packageh', shen_packageh, 3)

@tail_recursion
def kl_readx45fromx45string(KL_ARG_V1607_980):

    class KL_Context:
        KL_LOC_Ns_981 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Ns_981', tco_apply(kl_map, [(lambda KL_ARG_V1307_982: ord(KL_ARG_V1307_982)), tco_apply(kl_explode, [KL_ARG_V1607_980])])), tail_call(kl_compile, [symdic.symdic_shen_x60st_inputx62, KL_CTX.KL_LOC_Ns_981, symdic.symdic_shen_readx45error])][(-1)]
shen_add_fun('read-from-string', kl_readx45fromx45string, 1)


#============================== prolog.kl==============================



@tail_recursion
def shen_x60defprologx62(KL_ARG_V907_983):

    class KL_Context:
        KL_LOC_Result_984 = None
        KL_LOC_Parse_shen_x60predicatex42x62_985 = None
        KL_LOC_Parse_shen_x60clausesx42x62_986 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_984', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60predicatex42x62_985', tco_apply(shen_x60predicatex42x62, [KL_ARG_V907_983])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60clausesx42x62_986', tco_apply(shen_x60clausesx42x62, [KL_CTX.KL_LOC_Parse_shen_x60predicatex42x62_985])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60clausesx42x62_986[0], tco_apply(shen_prologx45x62shen, [tco_apply(kl_map, [(lambda KL_ARG_Parse_X_987: tail_call(shen_insertx45predicate, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60predicatex42x62_985]), KL_ARG_Parse_X_987])), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60clausesx42x62_986])])])[0]]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60clausesx42x62_986)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60predicatex42x62_985)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_984 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_984)][(-1)]
shen_add_fun('shen.<defprolog>', shen_x60defprologx62, 1)

@tail_recursion
def shen_prologx45error(KL_ARG_V914_988, KL_ARG_V915_989):
    global symdic
    return (shen_simple_error(('prolog syntax error in ' + tco_apply(shen_app, [KL_ARG_V914_988, (' here:\r\n\r\n ' + tco_apply(shen_app, [tco_apply(shen_nextx4550, [50, KL_ARG_V915_989[0]]), '\r\n', symdic.symdic_shen_a])), symdic.symdic_shen_a]))) if ((([] == KL_ARG_V915_989[1][1]) if shen_consp(KL_ARG_V915_989[1]) else False) if shen_consp(KL_ARG_V915_989) else False) else (shen_simple_error(('prolog syntax error in ' + tco_apply(shen_app, [KL_ARG_V914_988, '\r\n', symdic.symdic_shen_a]))) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.prolog-error', shen_prologx45error, 2)

@tail_recursion
def shen_nextx4550(KL_ARG_V920_990, KL_ARG_V921_991):
    global symdic
    return ('' if ([] == KL_ARG_V921_991) else ('' if (0 == KL_ARG_V920_990) else ((tco_apply(shen_deconsx45string, [KL_ARG_V921_991[0]]) + tco_apply(shen_nextx4550, [(KL_ARG_V920_990 - 1), KL_ARG_V921_991[1]])) if shen_consp(KL_ARG_V921_991) else (tail_call(shen_sysx45error, [symdic.symdic_shen_nextx4550]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.next-50', shen_nextx4550, 2)

@tail_recursion
def shen_deconsx45string(KL_ARG_V922_992):
    global symdic
    return (tail_call(shen_app, [tco_apply(shen_evalx45cons, [KL_ARG_V922_992]), ' ', symdic.symdic_shen_s]) if ((((([] == KL_ARG_V922_992[1][1][1]) if shen_consp(KL_ARG_V922_992[1][1]) else False) if shen_consp(KL_ARG_V922_992[1]) else False) if (symdic.symdic_kl_cons == KL_ARG_V922_992[0]) else False) if shen_consp(KL_ARG_V922_992) else False) else (tail_call(shen_app, [KL_ARG_V922_992, ' ', symdic.symdic_shen_r]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.decons-string', shen_deconsx45string, 1)

@tail_recursion
def shen_insertx45predicate(KL_ARG_V923_993, KL_ARG_V924_994):
    global symdic
    return ([[KL_ARG_V923_993, KL_ARG_V924_994[0]], [symdic.symdic_kl_x58x45, KL_ARG_V924_994[1]]] if ((([] == KL_ARG_V924_994[1][1]) if shen_consp(KL_ARG_V924_994[1]) else False) if shen_consp(KL_ARG_V924_994) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_insertx45predicate]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.insert-predicate', shen_insertx45predicate, 2)

@tail_recursion
def shen_x60predicatex42x62(KL_ARG_V929_995):

    class KL_Context:
        KL_LOC_Result_996 = None
        KL_LOC_Parse_X_997 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_996', ([setattr(KL_CTX, 'KL_LOC_Parse_X_997', KL_ARG_V929_995[0][0]), tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V929_995[0][1], tco_apply(shen_hdtl, [KL_ARG_V929_995])])[0], KL_CTX.KL_LOC_Parse_X_997])][(-1)] if shen_consp(KL_ARG_V929_995[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_996 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_996)][(-1)]
shen_add_fun('shen.<predicate*>', shen_x60predicatex42x62, 1)

@tail_recursion
def shen_x60clausesx42x62(KL_ARG_V934_998):

    class KL_Context:
        KL_LOC_Result_999 = None
        KL_LOC_Parse_shen_x60clausex42x62_1000 = None
        KL_LOC_Parse_shen_x60clausesx42x62_1001 = None
        KL_LOC_Result_1002 = None
        KL_LOC_Parse_x60ex62_1003 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_999', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60clausex42x62_1000', tco_apply(shen_x60clausex42x62, [KL_ARG_V934_998])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60clausesx42x62_1001', tco_apply(shen_x60clausesx42x62, [KL_CTX.KL_LOC_Parse_shen_x60clausex42x62_1000])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60clausesx42x62_1001[0], [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60clausex42x62_1000]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60clausesx42x62_1001])]]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60clausesx42x62_1001)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60clausex42x62_1000)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_1002', [setattr(KL_CTX, 'KL_LOC_Parse_x60ex62_1003', tco_apply(kl_x60ex62, [KL_ARG_V934_998])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_x60ex62_1003[0], tco_apply(kl_append, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_x60ex62_1003]), []])]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_x60ex62_1003)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_1002 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_1002)][(-1)] if (KL_CTX.KL_LOC_Result_999 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_999)][(-1)]
shen_add_fun('shen.<clauses*>', shen_x60clausesx42x62, 1)

@tail_recursion
def shen_x60clausex42x62(KL_ARG_V939_1004):

    class KL_Context:
        KL_LOC_Result_1005 = None
        KL_LOC_Parse_shen_x60headx42x62_1006 = None
        KL_LOC_Parse_shen_x60bodyx42x62_1007 = None
        KL_LOC_Parse_shen_x60endx42x62_1008 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_1005', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60headx42x62_1006', tco_apply(shen_x60headx42x62, [KL_ARG_V939_1004])), (([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60bodyx42x62_1007', tco_apply(shen_x60bodyx42x62, [tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60headx42x62_1006[0][1], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60headx42x62_1006])])])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60endx42x62_1008', tco_apply(shen_x60endx42x62, [KL_CTX.KL_LOC_Parse_shen_x60bodyx42x62_1007])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60endx42x62_1008[0], [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60headx42x62_1006]), [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60bodyx42x62_1007]), []]]]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60endx42x62_1008)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60bodyx42x62_1007)) else tco_apply(kl_fail, []))][(-1)] if ((symdic.symdic_kl_x60x45x45 == KL_CTX.KL_LOC_Parse_shen_x60headx42x62_1006[0][0]) if shen_consp(KL_CTX.KL_LOC_Parse_shen_x60headx42x62_1006[0]) else False) else tco_apply(kl_fail, [])) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60headx42x62_1006)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_1005 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_1005)][(-1)]
shen_add_fun('shen.<clause*>', shen_x60clausex42x62, 1)

@tail_recursion
def shen_x60headx42x62(KL_ARG_V944_1009):

    class KL_Context:
        KL_LOC_Result_1010 = None
        KL_LOC_Parse_shen_x60termx42x62_1011 = None
        KL_LOC_Parse_shen_x60headx42x62_1012 = None
        KL_LOC_Result_1013 = None
        KL_LOC_Parse_x60ex62_1014 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_1010', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60termx42x62_1011', tco_apply(shen_x60termx42x62, [KL_ARG_V944_1009])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60headx42x62_1012', tco_apply(shen_x60headx42x62, [KL_CTX.KL_LOC_Parse_shen_x60termx42x62_1011])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60headx42x62_1012[0], [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60termx42x62_1011]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60headx42x62_1012])]]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60headx42x62_1012)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60termx42x62_1011)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_1013', [setattr(KL_CTX, 'KL_LOC_Parse_x60ex62_1014', tco_apply(kl_x60ex62, [KL_ARG_V944_1009])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_x60ex62_1014[0], tco_apply(kl_append, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_x60ex62_1014]), []])]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_x60ex62_1014)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_1013 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_1013)][(-1)] if (KL_CTX.KL_LOC_Result_1010 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_1010)][(-1)]
shen_add_fun('shen.<head*>', shen_x60headx42x62, 1)

@tail_recursion
def shen_x60termx42x62(KL_ARG_V949_1015):

    class KL_Context:
        KL_LOC_Result_1016 = None
        KL_LOC_Parse_X_1017 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_1016', ([setattr(KL_CTX, 'KL_LOC_Parse_X_1017', KL_ARG_V949_1015[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V949_1015[0][1], tco_apply(shen_hdtl, [KL_ARG_V949_1015])])[0], tco_apply(shen_evalx45cons, [KL_CTX.KL_LOC_Parse_X_1017])]) if (tco_apply(shen_legitimatex45termx63, [KL_CTX.KL_LOC_Parse_X_1017]) if (not (symdic.symdic_kl_x60x45x45 == KL_CTX.KL_LOC_Parse_X_1017)) else False) else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V949_1015[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_1016 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_1016)][(-1)]
shen_add_fun('shen.<term*>', shen_x60termx42x62, 1)

@tail_recursion
def shen_legitimatex45termx63(KL_ARG_V954_1018):
    global symdic
    return ((tail_call(shen_legitimatex45termx63, [KL_ARG_V954_1018[1][1][0]]) if tco_apply(shen_legitimatex45termx63, [KL_ARG_V954_1018[1][0]]) else False) if ((((([] == KL_ARG_V954_1018[1][1][1]) if shen_consp(KL_ARG_V954_1018[1][1]) else False) if shen_consp(KL_ARG_V954_1018[1]) else False) if (symdic.symdic_kl_cons == KL_ARG_V954_1018[0]) else False) if shen_consp(KL_ARG_V954_1018) else False) else (tail_call(shen_legitimatex45termx63, [KL_ARG_V954_1018[1][0]]) if (((((([] == KL_ARG_V954_1018[1][1][1]) if (symdic.symdic_kl_x43 == KL_ARG_V954_1018[1][1][0]) else False) if shen_consp(KL_ARG_V954_1018[1][1]) else False) if shen_consp(KL_ARG_V954_1018[1]) else False) if (symdic.symdic_kl_mode == KL_ARG_V954_1018[0]) else False) if shen_consp(KL_ARG_V954_1018) else False) else (tail_call(shen_legitimatex45termx63, [KL_ARG_V954_1018[1][0]]) if (((((([] == KL_ARG_V954_1018[1][1][1]) if (symdic.symdic_kl_x45 == KL_ARG_V954_1018[1][1][0]) else False) if shen_consp(KL_ARG_V954_1018[1][1]) else False) if shen_consp(KL_ARG_V954_1018[1]) else False) if (symdic.symdic_kl_mode == KL_ARG_V954_1018[0]) else False) if shen_consp(KL_ARG_V954_1018) else False) else (False if shen_consp(KL_ARG_V954_1018) else (True if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.legitimate-term?', shen_legitimatex45termx63, 1)

@tail_recursion
def shen_evalx45cons(KL_ARG_V955_1019):
    global symdic
    return ([tco_apply(shen_evalx45cons, [KL_ARG_V955_1019[1][0]]), tco_apply(shen_evalx45cons, [KL_ARG_V955_1019[1][1][0]])] if ((((([] == KL_ARG_V955_1019[1][1][1]) if shen_consp(KL_ARG_V955_1019[1][1]) else False) if shen_consp(KL_ARG_V955_1019[1]) else False) if (symdic.symdic_kl_cons == KL_ARG_V955_1019[0]) else False) if shen_consp(KL_ARG_V955_1019) else False) else ([symdic.symdic_kl_mode, [tco_apply(shen_evalx45cons, [KL_ARG_V955_1019[1][0]]), KL_ARG_V955_1019[1][1]]] if ((((([] == KL_ARG_V955_1019[1][1][1]) if shen_consp(KL_ARG_V955_1019[1][1]) else False) if shen_consp(KL_ARG_V955_1019[1]) else False) if (symdic.symdic_kl_mode == KL_ARG_V955_1019[0]) else False) if shen_consp(KL_ARG_V955_1019) else False) else (KL_ARG_V955_1019 if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.eval-cons', shen_evalx45cons, 1)

@tail_recursion
def shen_x60bodyx42x62(KL_ARG_V960_1020):

    class KL_Context:
        KL_LOC_Result_1021 = None
        KL_LOC_Parse_shen_x60literalx42x62_1022 = None
        KL_LOC_Parse_shen_x60bodyx42x62_1023 = None
        KL_LOC_Result_1024 = None
        KL_LOC_Parse_x60ex62_1025 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_1021', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60literalx42x62_1022', tco_apply(shen_x60literalx42x62, [KL_ARG_V960_1020])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60bodyx42x62_1023', tco_apply(shen_x60bodyx42x62, [KL_CTX.KL_LOC_Parse_shen_x60literalx42x62_1022])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60bodyx42x62_1023[0], [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60literalx42x62_1022]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60bodyx42x62_1023])]]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60bodyx42x62_1023)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60literalx42x62_1022)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_1024', [setattr(KL_CTX, 'KL_LOC_Parse_x60ex62_1025', tco_apply(kl_x60ex62, [KL_ARG_V960_1020])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_x60ex62_1025[0], tco_apply(kl_append, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_x60ex62_1025]), []])]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_x60ex62_1025)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_1024 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_1024)][(-1)] if (KL_CTX.KL_LOC_Result_1021 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_1021)][(-1)]
shen_add_fun('shen.<body*>', shen_x60bodyx42x62, 1)

@tail_recursion
def shen_x60literalx42x62(KL_ARG_V965_1026):

    class KL_Context:
        KL_LOC_Result_1027 = None
        KL_LOC_Result_1028 = None
        KL_LOC_Parse_X_1029 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_1027', (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V965_1026[0][1], tco_apply(shen_hdtl, [KL_ARG_V965_1026])])[0], [symdic.symdic_kl_cut, [shen_intern('Throwcontrol'), []]]]) if ((symdic.symdic_kl_x33 == KL_ARG_V965_1026[0][0]) if shen_consp(KL_ARG_V965_1026[0]) else False) else tco_apply(kl_fail, []))), ([setattr(KL_CTX, 'KL_LOC_Result_1028', ([setattr(KL_CTX, 'KL_LOC_Parse_X_1029', KL_ARG_V965_1026[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V965_1026[0][1], tco_apply(shen_hdtl, [KL_ARG_V965_1026])])[0], KL_CTX.KL_LOC_Parse_X_1029]) if shen_consp(KL_CTX.KL_LOC_Parse_X_1029) else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V965_1026[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_1028 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_1028)][(-1)] if (KL_CTX.KL_LOC_Result_1027 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_1027)][(-1)]
shen_add_fun('shen.<literal*>', shen_x60literalx42x62, 1)

@tail_recursion
def shen_x60endx42x62(KL_ARG_V970_1030):

    class KL_Context:
        KL_LOC_Result_1031 = None
        KL_LOC_Parse_X_1032 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_1031', ([setattr(KL_CTX, 'KL_LOC_Parse_X_1032', KL_ARG_V970_1030[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V970_1030[0][1], tco_apply(shen_hdtl, [KL_ARG_V970_1030])])[0], KL_CTX.KL_LOC_Parse_X_1032]) if (KL_CTX.KL_LOC_Parse_X_1032 == symdic.symdic_kl_x59) else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V970_1030[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_1031 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_1031)][(-1)]
shen_add_fun('shen.<end*>', shen_x60endx42x62, 1)

@tail_recursion
def kl_cut(KL_ARG_V971_1033, KL_ARG_V972_1034, KL_ARG_V973_1035):

    class KL_Context:
        KL_LOC_Result_1036 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_1036', tco_apply(kl_thaw, [KL_ARG_V973_1035])), (KL_ARG_V971_1033 if (KL_CTX.KL_LOC_Result_1036 == False) else KL_CTX.KL_LOC_Result_1036)][(-1)]
shen_add_fun('cut', kl_cut, 3)

@tail_recursion
def shen_insert_modes(KL_ARG_V974_1037):
    global symdic
    return (KL_ARG_V974_1037 if ((((([] == KL_ARG_V974_1037[1][1][1]) if shen_consp(KL_ARG_V974_1037[1][1]) else False) if shen_consp(KL_ARG_V974_1037[1]) else False) if (symdic.symdic_kl_mode == KL_ARG_V974_1037[0]) else False) if shen_consp(KL_ARG_V974_1037) else False) else ([] if ([] == KL_ARG_V974_1037) else ([[symdic.symdic_kl_mode, [KL_ARG_V974_1037[0], [symdic.symdic_kl_x43, []]]], [symdic.symdic_kl_mode, [tco_apply(shen_insert_modes, [KL_ARG_V974_1037[1]]), [symdic.symdic_kl_x45, []]]]] if shen_consp(KL_ARG_V974_1037) else (KL_ARG_V974_1037 if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.insert_modes', shen_insert_modes, 1)

@tail_recursion
def shen_sx45prolog(KL_ARG_V975_1038):
    global symdic
    return tail_call(kl_map, [(lambda KL_ARG_V901_1039: tail_call(kl_eval, [KL_ARG_V901_1039])), tco_apply(shen_prologx45x62shen, [KL_ARG_V975_1038])])
shen_add_fun('shen.s-prolog', shen_sx45prolog, 1)

@tail_recursion
def shen_prologx45x62shen(KL_ARG_V976_1040):
    global symdic
    return tail_call(kl_map, [symdic.symdic_shen_compile_prolog_procedure, tco_apply(shen_group_clauses, [tco_apply(kl_map, [symdic.symdic_shen_sx45prolog_clause, tco_apply(kl_mapcan, [symdic.symdic_shen_head_abstraction, KL_ARG_V976_1040])])])])
shen_add_fun('shen.prolog->shen', shen_prologx45x62shen, 1)

@tail_recursion
def shen_sx45prolog_clause(KL_ARG_V977_1041):
    global symdic
    return ([KL_ARG_V977_1041[0], [symdic.symdic_kl_x58x45, [tco_apply(kl_map, [symdic.symdic_shen_sx45prolog_literal, KL_ARG_V977_1041[1][1][0]]), []]]] if ((((([] == KL_ARG_V977_1041[1][1][1]) if shen_consp(KL_ARG_V977_1041[1][1]) else False) if (symdic.symdic_kl_x58x45 == KL_ARG_V977_1041[1][0]) else False) if shen_consp(KL_ARG_V977_1041[1]) else False) if shen_consp(KL_ARG_V977_1041) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_sx45prolog_clause]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.s-prolog_clause', shen_sx45prolog_clause, 1)

@tail_recursion
def shen_head_abstraction(KL_ARG_V978_1042):

    class KL_Context:
        KL_LOC_Terms_1043 = None
        KL_LOC_XTerms_1045 = None
        KL_LOC_Literal_1046 = None
        KL_LOC_Clause_1047 = None
    KL_CTX = KL_Context()
    global symdic
    return ([KL_ARG_V978_1042, []] if ((((((tco_apply(shen_complexity_head, [KL_ARG_V978_1042[0]]) < shen_get(symdic.symdic_shen_x42maxcomplexityx42)) if ([] == KL_ARG_V978_1042[1][1][1]) else False) if shen_consp(KL_ARG_V978_1042[1][1]) else False) if (symdic.symdic_kl_x58x45 == KL_ARG_V978_1042[1][0]) else False) if shen_consp(KL_ARG_V978_1042[1]) else False) if shen_consp(KL_ARG_V978_1042) else False) else ([setattr(KL_CTX, 'KL_LOC_Terms_1043', tco_apply(kl_map, [(lambda KL_ARG_Y_1044: tail_call(kl_gensym, [symdic.symdic_V])), KL_ARG_V978_1042[0][1]])), [setattr(KL_CTX, 'KL_LOC_XTerms_1045', tco_apply(shen_rcons_form, [tco_apply(shen_remove_modes, [KL_ARG_V978_1042[0][1]])])), [setattr(KL_CTX, 'KL_LOC_Literal_1046', [symdic.symdic_kl_unify, [tco_apply(shen_cons_form, [KL_CTX.KL_LOC_Terms_1043]), [KL_CTX.KL_LOC_XTerms_1045, []]]]), [setattr(KL_CTX, 'KL_LOC_Clause_1047', [[KL_ARG_V978_1042[0][0], KL_CTX.KL_LOC_Terms_1043], [symdic.symdic_kl_x58x45, [[KL_CTX.KL_LOC_Literal_1046, KL_ARG_V978_1042[1][1][0]], []]]]), [KL_CTX.KL_LOC_Clause_1047, []]][(-1)]][(-1)]][(-1)]][(-1)] if (((((([] == KL_ARG_V978_1042[1][1][1]) if shen_consp(KL_ARG_V978_1042[1][1]) else False) if (symdic.symdic_kl_x58x45 == KL_ARG_V978_1042[1][0]) else False) if shen_consp(KL_ARG_V978_1042[1]) else False) if shen_consp(KL_ARG_V978_1042[0]) else False) if shen_consp(KL_ARG_V978_1042) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_head_abstraction]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.head_abstraction', shen_head_abstraction, 1)

@tail_recursion
def shen_complexity_head(KL_ARG_V983_1048):
    global symdic
    return (tail_call(shen_product, [tco_apply(kl_map, [symdic.symdic_shen_complexity, KL_ARG_V983_1048[1]])]) if shen_consp(KL_ARG_V983_1048) else (tail_call(shen_sysx45error, [symdic.symdic_shen_complexity_head]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.complexity_head', shen_complexity_head, 1)

@tail_recursion
def shen_complexity(KL_ARG_V991_1049):
    global symdic
    return (tail_call(shen_complexity, [KL_ARG_V991_1049[1][0]]) if (((((((((([] == KL_ARG_V991_1049[1][1][1]) if shen_consp(KL_ARG_V991_1049[1][1]) else False) if ([] == KL_ARG_V991_1049[1][0][1][1][1]) else False) if shen_consp(KL_ARG_V991_1049[1][0][1][1]) else False) if shen_consp(KL_ARG_V991_1049[1][0][1]) else False) if (symdic.symdic_kl_mode == KL_ARG_V991_1049[1][0][0]) else False) if shen_consp(KL_ARG_V991_1049[1][0]) else False) if shen_consp(KL_ARG_V991_1049[1]) else False) if (symdic.symdic_kl_mode == KL_ARG_V991_1049[0]) else False) if shen_consp(KL_ARG_V991_1049) else False) else ((2 * (tco_apply(shen_complexity, [[symdic.symdic_kl_mode, [KL_ARG_V991_1049[1][0][0], KL_ARG_V991_1049[1][1]]]]) * tco_apply(shen_complexity, [[symdic.symdic_kl_mode, [KL_ARG_V991_1049[1][0][1], KL_ARG_V991_1049[1][1]]]]))) if ((((((([] == KL_ARG_V991_1049[1][1][1]) if (symdic.symdic_kl_x43 == KL_ARG_V991_1049[1][1][0]) else False) if shen_consp(KL_ARG_V991_1049[1][1]) else False) if shen_consp(KL_ARG_V991_1049[1][0]) else False) if shen_consp(KL_ARG_V991_1049[1]) else False) if (symdic.symdic_kl_mode == KL_ARG_V991_1049[0]) else False) if shen_consp(KL_ARG_V991_1049) else False) else ((tco_apply(shen_complexity, [[symdic.symdic_kl_mode, [KL_ARG_V991_1049[1][0][0], KL_ARG_V991_1049[1][1]]]]) * tco_apply(shen_complexity, [[symdic.symdic_kl_mode, [KL_ARG_V991_1049[1][0][1], KL_ARG_V991_1049[1][1]]]])) if ((((((([] == KL_ARG_V991_1049[1][1][1]) if (symdic.symdic_kl_x45 == KL_ARG_V991_1049[1][1][0]) else False) if shen_consp(KL_ARG_V991_1049[1][1]) else False) if shen_consp(KL_ARG_V991_1049[1][0]) else False) if shen_consp(KL_ARG_V991_1049[1]) else False) if (symdic.symdic_kl_mode == KL_ARG_V991_1049[0]) else False) if shen_consp(KL_ARG_V991_1049) else False) else (1 if (((((tco_apply(kl_variablex63, [KL_ARG_V991_1049[1][0]]) if ([] == KL_ARG_V991_1049[1][1][1]) else False) if shen_consp(KL_ARG_V991_1049[1][1]) else False) if shen_consp(KL_ARG_V991_1049[1]) else False) if (symdic.symdic_kl_mode == KL_ARG_V991_1049[0]) else False) if shen_consp(KL_ARG_V991_1049) else False) else (2 if (((((([] == KL_ARG_V991_1049[1][1][1]) if (symdic.symdic_kl_x43 == KL_ARG_V991_1049[1][1][0]) else False) if shen_consp(KL_ARG_V991_1049[1][1]) else False) if shen_consp(KL_ARG_V991_1049[1]) else False) if (symdic.symdic_kl_mode == KL_ARG_V991_1049[0]) else False) if shen_consp(KL_ARG_V991_1049) else False) else (1 if (((((([] == KL_ARG_V991_1049[1][1][1]) if (symdic.symdic_kl_x45 == KL_ARG_V991_1049[1][1][0]) else False) if shen_consp(KL_ARG_V991_1049[1][1]) else False) if shen_consp(KL_ARG_V991_1049[1]) else False) if (symdic.symdic_kl_mode == KL_ARG_V991_1049[0]) else False) if shen_consp(KL_ARG_V991_1049) else False) else (tail_call(shen_complexity, [[symdic.symdic_kl_mode, [KL_ARG_V991_1049, [symdic.symdic_kl_x43, []]]]]) if True else shen_simple_error('condition failure'))))))))
shen_add_fun('shen.complexity', shen_complexity, 1)

@tail_recursion
def shen_product(KL_ARG_V992_1050):
    global symdic
    return (1 if ([] == KL_ARG_V992_1050) else ((KL_ARG_V992_1050[0] * tco_apply(shen_product, [KL_ARG_V992_1050[1]])) if shen_consp(KL_ARG_V992_1050) else (tail_call(shen_sysx45error, [symdic.symdic_shen_product]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.product', shen_product, 1)

@tail_recursion
def shen_sx45prolog_literal(KL_ARG_V993_1051):
    global symdic
    return ([symdic.symdic_kl_bind, [KL_ARG_V993_1051[1][0], [tco_apply(shen_insert_deref, [KL_ARG_V993_1051[1][1][0]]), []]]] if ((((([] == KL_ARG_V993_1051[1][1][1]) if shen_consp(KL_ARG_V993_1051[1][1]) else False) if shen_consp(KL_ARG_V993_1051[1]) else False) if (symdic.symdic_kl_is == KL_ARG_V993_1051[0]) else False) if shen_consp(KL_ARG_V993_1051) else False) else ([symdic.symdic_kl_fwhen, [tco_apply(shen_insert_deref, [KL_ARG_V993_1051[1][0]]), []]] if (((([] == KL_ARG_V993_1051[1][1]) if shen_consp(KL_ARG_V993_1051[1]) else False) if (symdic.symdic_kl_when == KL_ARG_V993_1051[0]) else False) if shen_consp(KL_ARG_V993_1051) else False) else ([symdic.symdic_kl_bind, [KL_ARG_V993_1051[1][0], [tco_apply(shen_insert_lazyderef, [KL_ARG_V993_1051[1][1][0]]), []]]] if ((((([] == KL_ARG_V993_1051[1][1][1]) if shen_consp(KL_ARG_V993_1051[1][1]) else False) if shen_consp(KL_ARG_V993_1051[1]) else False) if (symdic.symdic_kl_bind == KL_ARG_V993_1051[0]) else False) if shen_consp(KL_ARG_V993_1051) else False) else ([symdic.symdic_kl_fwhen, [tco_apply(shen_insert_lazyderef, [KL_ARG_V993_1051[1][0]]), []]] if (((([] == KL_ARG_V993_1051[1][1]) if shen_consp(KL_ARG_V993_1051[1]) else False) if (symdic.symdic_kl_fwhen == KL_ARG_V993_1051[0]) else False) if shen_consp(KL_ARG_V993_1051) else False) else ([tco_apply(shen_m_prolog_to_sx45prolog_predicate, [KL_ARG_V993_1051[0]]), KL_ARG_V993_1051[1]] if shen_consp(KL_ARG_V993_1051) else (tail_call(shen_sysx45error, [symdic.symdic_shen_sx45prolog_literal]) if True else shen_simple_error('condition failure')))))))
shen_add_fun('shen.s-prolog_literal', shen_sx45prolog_literal, 1)

@tail_recursion
def shen_insert_deref(KL_ARG_V994_1052):
    global symdic
    return ([symdic.symdic_shen_deref, [KL_ARG_V994_1052, [symdic.symdic_ProcessN, []]]] if tco_apply(kl_variablex63, [KL_ARG_V994_1052]) else ([tco_apply(shen_insert_deref, [KL_ARG_V994_1052[0]]), tco_apply(shen_insert_deref, [KL_ARG_V994_1052[1]])] if shen_consp(KL_ARG_V994_1052) else (KL_ARG_V994_1052 if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.insert_deref', shen_insert_deref, 1)

@tail_recursion
def shen_insert_lazyderef(KL_ARG_V995_1053):
    global symdic
    return ([symdic.symdic_shen_lazyderef, [KL_ARG_V995_1053, [symdic.symdic_ProcessN, []]]] if tco_apply(kl_variablex63, [KL_ARG_V995_1053]) else ([tco_apply(shen_insert_lazyderef, [KL_ARG_V995_1053[0]]), tco_apply(shen_insert_lazyderef, [KL_ARG_V995_1053[1]])] if shen_consp(KL_ARG_V995_1053) else (KL_ARG_V995_1053 if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.insert_lazyderef', shen_insert_lazyderef, 1)

@tail_recursion
def shen_m_prolog_to_sx45prolog_predicate(KL_ARG_V996_1054):
    global symdic
    return (symdic.symdic_kl_unify if (symdic.symdic_kl_x61 == KL_ARG_V996_1054) else (symdic.symdic_kl_unifyx33 if (symdic.symdic_kl_x61x33 == KL_ARG_V996_1054) else (symdic.symdic_kl_identical if (symdic.symdic_kl_x61x61 == KL_ARG_V996_1054) else (KL_ARG_V996_1054 if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.m_prolog_to_s-prolog_predicate', shen_m_prolog_to_sx45prolog_predicate, 1)

@tail_recursion
def shen_group_clauses(KL_ARG_V997_1055):

    class KL_Context:
        KL_LOC_Group_1056 = None
        KL_LOC_Rest_1058 = None
    KL_CTX = KL_Context()
    global symdic
    return ([] if ([] == KL_ARG_V997_1055) else ([setattr(KL_CTX, 'KL_LOC_Group_1056', tco_apply(shen_collect, [(lambda KL_ARG_X_1057: tail_call(shen_same_predicatex63, [KL_ARG_V997_1055[0], KL_ARG_X_1057])), KL_ARG_V997_1055])), [setattr(KL_CTX, 'KL_LOC_Rest_1058', tco_apply(kl_difference, [KL_ARG_V997_1055, KL_CTX.KL_LOC_Group_1056])), [KL_CTX.KL_LOC_Group_1056, tco_apply(shen_group_clauses, [KL_CTX.KL_LOC_Rest_1058])]][(-1)]][(-1)] if shen_consp(KL_ARG_V997_1055) else (tail_call(shen_sysx45error, [symdic.symdic_shen_group_clauses]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.group_clauses', shen_group_clauses, 1)

@tail_recursion
def shen_collect(KL_ARG_V1000_1059, KL_ARG_V1001_1060):
    global symdic
    return ([] if ([] == KL_ARG_V1001_1060) else (([KL_ARG_V1001_1060[0], tco_apply(shen_collect, [KL_ARG_V1000_1059, KL_ARG_V1001_1060[1]])] if shen_apply(KL_ARG_V1000_1059, [KL_ARG_V1001_1060[0]]) else tail_call(shen_collect, [KL_ARG_V1000_1059, KL_ARG_V1001_1060[1]])) if shen_consp(KL_ARG_V1001_1060) else (tail_call(shen_sysx45error, [symdic.symdic_shen_collect]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.collect', shen_collect, 2)

@tail_recursion
def shen_same_predicatex63(KL_ARG_V1018_1061, KL_ARG_V1019_1062):
    global symdic
    return ((KL_ARG_V1018_1061[0][0] == KL_ARG_V1019_1062[0][0]) if (((shen_consp(KL_ARG_V1019_1062[0]) if shen_consp(KL_ARG_V1019_1062) else False) if shen_consp(KL_ARG_V1018_1061[0]) else False) if shen_consp(KL_ARG_V1018_1061) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_same_predicatex63]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.same_predicate?', shen_same_predicatex63, 2)

@tail_recursion
def shen_compile_prolog_procedure(KL_ARG_V1020_1063):

    class KL_Context:
        KL_LOC_F_1064 = None
        KL_LOC_Shen_1065 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_F_1064', tco_apply(shen_procedure_name, [KL_ARG_V1020_1063])), [setattr(KL_CTX, 'KL_LOC_Shen_1065', tco_apply(shen_clausesx45tox45shen, [KL_CTX.KL_LOC_F_1064, KL_ARG_V1020_1063])), KL_CTX.KL_LOC_Shen_1065][(-1)]][(-1)]
shen_add_fun('shen.compile_prolog_procedure', shen_compile_prolog_procedure, 1)

@tail_recursion
def shen_procedure_name(KL_ARG_V1033_1066):
    global symdic
    return (KL_ARG_V1033_1066[0][0][0] if ((shen_consp(KL_ARG_V1033_1066[0][0]) if shen_consp(KL_ARG_V1033_1066[0]) else False) if shen_consp(KL_ARG_V1033_1066) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_procedure_name]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.procedure_name', shen_procedure_name, 1)

@tail_recursion
def shen_clausesx45tox45shen(KL_ARG_V1034_1067, KL_ARG_V1035_1068):

    class KL_Context:
        KL_LOC_Linear_1069 = None
        KL_LOC_Arity_1070 = None
        KL_LOC_Parameters_1072 = None
        KL_LOC_AUM_instructions_1073 = None
        KL_LOC_Code_1075 = None
        KL_LOC_ShenDef_1076 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Linear_1069', tco_apply(kl_map, [symdic.symdic_shen_linearisex45clause, KL_ARG_V1035_1068])), [setattr(KL_CTX, 'KL_LOC_Arity_1070', tco_apply(shen_prologx45aritycheck, [KL_ARG_V1034_1067, tco_apply(kl_map, [(lambda KL_ARG_V902_1071: tail_call(kl_head, [KL_ARG_V902_1071])), KL_ARG_V1035_1068])])), [setattr(KL_CTX, 'KL_LOC_Parameters_1072', tco_apply(shen_parameters, [KL_CTX.KL_LOC_Arity_1070])), [setattr(KL_CTX, 'KL_LOC_AUM_instructions_1073', tco_apply(kl_map, [(lambda KL_ARG_X_1074: tail_call(shen_aum, [KL_ARG_X_1074, KL_CTX.KL_LOC_Parameters_1072])), KL_CTX.KL_LOC_Linear_1069])), [setattr(KL_CTX, 'KL_LOC_Code_1075', tco_apply(shen_catchx45cut, [tco_apply(shen_nestx45disjunct, [tco_apply(kl_map, [symdic.symdic_shen_aum_to_shen, KL_CTX.KL_LOC_AUM_instructions_1073])])])), [setattr(KL_CTX, 'KL_LOC_ShenDef_1076', [symdic.symdic_kl_define, [KL_ARG_V1034_1067, tco_apply(kl_append, [KL_CTX.KL_LOC_Parameters_1072, tco_apply(kl_append, [[symdic.symdic_ProcessN, [symdic.symdic_Continuation, []]], [symdic.symdic_kl_x45x62, [KL_CTX.KL_LOC_Code_1075, []]]])])]]), KL_CTX.KL_LOC_ShenDef_1076][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]
shen_add_fun('shen.clauses-to-shen', shen_clausesx45tox45shen, 2)

@tail_recursion
def shen_catchx45cut(KL_ARG_V1036_1077):
    global symdic
    return (KL_ARG_V1036_1077 if (not tco_apply(shen_occursx63, [symdic.symdic_kl_cut, KL_ARG_V1036_1077])) else ([symdic.symdic_kl_let, [symdic.symdic_Throwcontrol, [[symdic.symdic_shen_catchpoint, []], [[symdic.symdic_shen_cutpoint, [symdic.symdic_Throwcontrol, [KL_ARG_V1036_1077, []]]], []]]]] if True else shen_simple_error('condition failure')))
shen_add_fun('shen.catch-cut', shen_catchx45cut, 1)

@tail_recursion
def shen_catchpoint():
    global symdic
    return shen_set(symdic.symdic_shen_x42catchx42, (1 + shen_get(symdic.symdic_shen_x42catchx42)))
shen_add_fun('shen.catchpoint', shen_catchpoint, 0)

@tail_recursion
def shen_cutpoint(KL_ARG_V1041_1078, KL_ARG_V1042_1079):
    global symdic
    return (False if (KL_ARG_V1042_1079 == KL_ARG_V1041_1078) else (KL_ARG_V1042_1079 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.cutpoint', shen_cutpoint, 2)

@tail_recursion
def shen_nestx45disjunct(KL_ARG_V1044_1080):
    global symdic
    return (KL_ARG_V1044_1080[0] if (([] == KL_ARG_V1044_1080[1]) if shen_consp(KL_ARG_V1044_1080) else False) else (tail_call(shen_lispx45or, [KL_ARG_V1044_1080[0], tco_apply(shen_nestx45disjunct, [KL_ARG_V1044_1080[1]])]) if shen_consp(KL_ARG_V1044_1080) else (tail_call(shen_sysx45error, [symdic.symdic_shen_nestx45disjunct]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.nest-disjunct', shen_nestx45disjunct, 1)

@tail_recursion
def shen_lispx45or(KL_ARG_V1045_1081, KL_ARG_V1046_1082):
    global symdic
    return [symdic.symdic_kl_let, [symdic.symdic_Case, [KL_ARG_V1045_1081, [[symdic.symdic_kl_if, [[symdic.symdic_kl_x61, [symdic.symdic_Case, [False, []]]], [KL_ARG_V1046_1082, [symdic.symdic_Case, []]]]], []]]]]
shen_add_fun('shen.lisp-or', shen_lispx45or, 2)

@tail_recursion
def shen_prologx45aritycheck(KL_ARG_V1049_1083, KL_ARG_V1050_1084):
    global symdic
    return ((tco_apply(kl_length, [KL_ARG_V1050_1084[0]]) - 1) if (([] == KL_ARG_V1050_1084[1]) if shen_consp(KL_ARG_V1050_1084) else False) else ((tail_call(shen_prologx45aritycheck, [KL_ARG_V1049_1083, KL_ARG_V1050_1084[1]]) if (tco_apply(kl_length, [KL_ARG_V1050_1084[0]]) == tco_apply(kl_length, [KL_ARG_V1050_1084[1][0]])) else shen_simple_error(('arity error in prolog procedure ' + tco_apply(shen_app, [[KL_ARG_V1049_1083, []], '\r\n', symdic.symdic_shen_a])))) if (shen_consp(KL_ARG_V1050_1084[1]) if shen_consp(KL_ARG_V1050_1084) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_prologx45aritycheck]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.prolog-aritycheck', shen_prologx45aritycheck, 2)

@tail_recursion
def shen_linearisex45clause(KL_ARG_V1051_1085):

    class KL_Context:
        KL_LOC_Linear_1086 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_Linear_1086', tco_apply(shen_linearise, [[KL_ARG_V1051_1085[0], KL_ARG_V1051_1085[1][1]]])), tail_call(shen_clause_form, [KL_CTX.KL_LOC_Linear_1086])][(-1)] if ((((([] == KL_ARG_V1051_1085[1][1][1]) if shen_consp(KL_ARG_V1051_1085[1][1]) else False) if (symdic.symdic_kl_x58x45 == KL_ARG_V1051_1085[1][0]) else False) if shen_consp(KL_ARG_V1051_1085[1]) else False) if shen_consp(KL_ARG_V1051_1085) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_linearisex45clause]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.linearise-clause', shen_linearisex45clause, 1)

@tail_recursion
def shen_clause_form(KL_ARG_V1052_1087):
    global symdic
    return ([tco_apply(shen_explicit_modes, [KL_ARG_V1052_1087[0]]), [symdic.symdic_kl_x58x45, [tco_apply(shen_cf_help, [KL_ARG_V1052_1087[1][0]]), []]]] if ((([] == KL_ARG_V1052_1087[1][1]) if shen_consp(KL_ARG_V1052_1087[1]) else False) if shen_consp(KL_ARG_V1052_1087) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_clause_form]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.clause_form', shen_clause_form, 1)

@tail_recursion
def shen_explicit_modes(KL_ARG_V1053_1088):
    global symdic
    return ([KL_ARG_V1053_1088[0], tco_apply(kl_map, [symdic.symdic_shen_em_help, KL_ARG_V1053_1088[1]])] if shen_consp(KL_ARG_V1053_1088) else (tail_call(shen_sysx45error, [symdic.symdic_shen_explicit_modes]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.explicit_modes', shen_explicit_modes, 1)

@tail_recursion
def shen_em_help(KL_ARG_V1054_1089):
    global symdic
    return (KL_ARG_V1054_1089 if ((((([] == KL_ARG_V1054_1089[1][1][1]) if shen_consp(KL_ARG_V1054_1089[1][1]) else False) if shen_consp(KL_ARG_V1054_1089[1]) else False) if (symdic.symdic_kl_mode == KL_ARG_V1054_1089[0]) else False) if shen_consp(KL_ARG_V1054_1089) else False) else ([symdic.symdic_kl_mode, [KL_ARG_V1054_1089, [symdic.symdic_kl_x43, []]]] if True else shen_simple_error('condition failure')))
shen_add_fun('shen.em_help', shen_em_help, 1)

@tail_recursion
def shen_cf_help(KL_ARG_V1055_1090):
    global symdic
    return ([[(symdic.symdic_kl_unifyx33 if shen_get(symdic.symdic_shen_x42occursx42) else symdic.symdic_kl_unify), KL_ARG_V1055_1090[1][0][1]], tco_apply(shen_cf_help, [KL_ARG_V1055_1090[1][1][0]])] if (((((((((([] == KL_ARG_V1055_1090[1][1][1]) if shen_consp(KL_ARG_V1055_1090[1][1]) else False) if ([] == KL_ARG_V1055_1090[1][0][1][1][1]) else False) if shen_consp(KL_ARG_V1055_1090[1][0][1][1]) else False) if shen_consp(KL_ARG_V1055_1090[1][0][1]) else False) if (symdic.symdic_kl_x61 == KL_ARG_V1055_1090[1][0][0]) else False) if shen_consp(KL_ARG_V1055_1090[1][0]) else False) if shen_consp(KL_ARG_V1055_1090[1]) else False) if (symdic.symdic_kl_where == KL_ARG_V1055_1090[0]) else False) if shen_consp(KL_ARG_V1055_1090) else False) else (KL_ARG_V1055_1090 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.cf_help', shen_cf_help, 1)

@tail_recursion
def kl_occursx45check(KL_ARG_V1060_1091):
    global symdic
    return (shen_set(symdic.symdic_shen_x42occursx42, True) if (symdic.symdic_kl_x43 == KL_ARG_V1060_1091) else (shen_set(symdic.symdic_shen_x42occursx42, False) if (symdic.symdic_kl_x45 == KL_ARG_V1060_1091) else (shen_simple_error('occurs-check expects + or -\r\n') if True else shen_simple_error('condition failure'))))
shen_add_fun('occurs-check', kl_occursx45check, 1)

@tail_recursion
def shen_aum(KL_ARG_V1061_1092, KL_ARG_V1062_1093):

    class KL_Context:
        KL_LOC_MuApplication_1094 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_MuApplication_1094', tco_apply(shen_make_mu_application, [[symdic.symdic_shen_mu, [KL_ARG_V1061_1092[0][1], [tco_apply(shen_continuation_call, [KL_ARG_V1061_1092[0][1], KL_ARG_V1061_1092[1][1][0]]), []]]], KL_ARG_V1062_1093])), tail_call(shen_mu_reduction, [KL_CTX.KL_LOC_MuApplication_1094, symdic.symdic_kl_x43])][(-1)] if (((((([] == KL_ARG_V1061_1092[1][1][1]) if shen_consp(KL_ARG_V1061_1092[1][1]) else False) if (symdic.symdic_kl_x58x45 == KL_ARG_V1061_1092[1][0]) else False) if shen_consp(KL_ARG_V1061_1092[1]) else False) if shen_consp(KL_ARG_V1061_1092[0]) else False) if shen_consp(KL_ARG_V1061_1092) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_aum]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.aum', shen_aum, 2)

@tail_recursion
def shen_continuation_call(KL_ARG_V1063_1095, KL_ARG_V1064_1096):

    class KL_Context:
        KL_LOC_VTerms_1097 = None
        KL_LOC_VBody_1098 = None
        KL_LOC_Free_1099 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_VTerms_1097', [symdic.symdic_ProcessN, tco_apply(shen_extract_vars, [KL_ARG_V1063_1095])]), [setattr(KL_CTX, 'KL_LOC_VBody_1098', tco_apply(shen_extract_vars, [KL_ARG_V1064_1096])), [setattr(KL_CTX, 'KL_LOC_Free_1099', tco_apply(kl_remove, [symdic.symdic_Throwcontrol, tco_apply(kl_difference, [KL_CTX.KL_LOC_VBody_1098, KL_CTX.KL_LOC_VTerms_1097])])), tail_call(shen_cc_help, [KL_CTX.KL_LOC_Free_1099, KL_ARG_V1064_1096])][(-1)]][(-1)]][(-1)]
shen_add_fun('shen.continuation_call', shen_continuation_call, 2)

@tail_recursion
def kl_remove(KL_ARG_V1065_1100, KL_ARG_V1066_1101):
    global symdic
    return tail_call(shen_removex45h, [KL_ARG_V1065_1100, KL_ARG_V1066_1101, []])
shen_add_fun('remove', kl_remove, 2)

@tail_recursion
def shen_removex45h(KL_ARG_V1069_1102, KL_ARG_V1070_1103, KL_ARG_V1071_1104):
    global symdic
    return (tail_call(kl_reverse, [KL_ARG_V1071_1104]) if ([] == KL_ARG_V1070_1103) else (tail_call(shen_removex45h, [KL_ARG_V1070_1103[0], KL_ARG_V1070_1103[1], KL_ARG_V1071_1104]) if ((KL_ARG_V1070_1103[0] == KL_ARG_V1069_1102) if shen_consp(KL_ARG_V1070_1103) else False) else (tail_call(shen_removex45h, [KL_ARG_V1069_1102, KL_ARG_V1070_1103[1], [KL_ARG_V1070_1103[0], KL_ARG_V1071_1104]]) if shen_consp(KL_ARG_V1070_1103) else (tail_call(shen_sysx45error, [symdic.symdic_shen_removex45h]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.remove-h', shen_removex45h, 3)

@tail_recursion
def shen_cc_help(KL_ARG_V1073_1105, KL_ARG_V1074_1106):
    global symdic
    return ([symdic.symdic_shen_pop, [symdic.symdic_shen_the, [symdic.symdic_shen_stack, []]]] if (([] == KL_ARG_V1074_1106) if ([] == KL_ARG_V1073_1105) else False) else ([symdic.symdic_shen_rename, [symdic.symdic_shen_the, [symdic.symdic_shen_variables, [symdic.symdic_kl_in, [KL_ARG_V1073_1105, [symdic.symdic_kl_and, [symdic.symdic_shen_then, [[symdic.symdic_shen_pop, [symdic.symdic_shen_the, [symdic.symdic_shen_stack, []]]], []]]]]]]]] if ([] == KL_ARG_V1074_1106) else ([symdic.symdic_kl_call, [symdic.symdic_shen_the, [symdic.symdic_shen_continuation, [KL_ARG_V1074_1106, []]]]] if ([] == KL_ARG_V1073_1105) else ([symdic.symdic_shen_rename, [symdic.symdic_shen_the, [symdic.symdic_shen_variables, [symdic.symdic_kl_in, [KL_ARG_V1073_1105, [symdic.symdic_kl_and, [symdic.symdic_shen_then, [[symdic.symdic_kl_call, [symdic.symdic_shen_the, [symdic.symdic_shen_continuation, [KL_ARG_V1074_1106, []]]]], []]]]]]]]] if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.cc_help', shen_cc_help, 2)

@tail_recursion
def shen_make_mu_application(KL_ARG_V1075_1107, KL_ARG_V1076_1108):
    global symdic
    return (KL_ARG_V1075_1107[1][1][0] if ((((((([] == KL_ARG_V1076_1108) if ([] == KL_ARG_V1075_1107[1][1][1]) else False) if shen_consp(KL_ARG_V1075_1107[1][1]) else False) if ([] == KL_ARG_V1075_1107[1][0]) else False) if shen_consp(KL_ARG_V1075_1107[1]) else False) if (symdic.symdic_shen_mu == KL_ARG_V1075_1107[0]) else False) if shen_consp(KL_ARG_V1075_1107) else False) else ([[symdic.symdic_shen_mu, [KL_ARG_V1075_1107[1][0][0], [tco_apply(shen_make_mu_application, [[symdic.symdic_shen_mu, [KL_ARG_V1075_1107[1][0][1], KL_ARG_V1075_1107[1][1]]], KL_ARG_V1076_1108[1]]), []]]], [KL_ARG_V1076_1108[0], []]] if ((((((shen_consp(KL_ARG_V1076_1108) if ([] == KL_ARG_V1075_1107[1][1][1]) else False) if shen_consp(KL_ARG_V1075_1107[1][1]) else False) if shen_consp(KL_ARG_V1075_1107[1][0]) else False) if shen_consp(KL_ARG_V1075_1107[1]) else False) if (symdic.symdic_shen_mu == KL_ARG_V1075_1107[0]) else False) if shen_consp(KL_ARG_V1075_1107) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_make_mu_application]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.make_mu_application', shen_make_mu_application, 2)

@tail_recursion
def shen_mu_reduction(KL_ARG_V1083_1109, KL_ARG_V1084_1110):

    class KL_Context:
        KL_LOC_Z_1111 = None
        KL_LOC_Z_1112 = None
        KL_LOC_Z_1113 = None
        KL_LOC_Z_1114 = None
    KL_CTX = KL_Context()
    global symdic
    return (tail_call(shen_mu_reduction, [[[symdic.symdic_shen_mu, [KL_ARG_V1083_1109[0][1][0][1][0], KL_ARG_V1083_1109[0][1][1]]], KL_ARG_V1083_1109[1]], KL_ARG_V1083_1109[0][1][0][1][1][0]]) if ((((((((((((([] == KL_ARG_V1083_1109[1][1]) if shen_consp(KL_ARG_V1083_1109[1]) else False) if ([] == KL_ARG_V1083_1109[0][1][1][1]) else False) if shen_consp(KL_ARG_V1083_1109[0][1][1]) else False) if ([] == KL_ARG_V1083_1109[0][1][0][1][1][1]) else False) if shen_consp(KL_ARG_V1083_1109[0][1][0][1][1]) else False) if shen_consp(KL_ARG_V1083_1109[0][1][0][1]) else False) if (symdic.symdic_kl_mode == KL_ARG_V1083_1109[0][1][0][0]) else False) if shen_consp(KL_ARG_V1083_1109[0][1][0]) else False) if shen_consp(KL_ARG_V1083_1109[0][1]) else False) if (symdic.symdic_shen_mu == KL_ARG_V1083_1109[0][0]) else False) if shen_consp(KL_ARG_V1083_1109[0]) else False) if shen_consp(KL_ARG_V1083_1109) else False) else (tail_call(shen_mu_reduction, [KL_ARG_V1083_1109[0][1][1][0], KL_ARG_V1084_1110]) if (((((((((symdic.symdic_kl__ == KL_ARG_V1083_1109[0][1][0]) if ([] == KL_ARG_V1083_1109[1][1]) else False) if shen_consp(KL_ARG_V1083_1109[1]) else False) if ([] == KL_ARG_V1083_1109[0][1][1][1]) else False) if shen_consp(KL_ARG_V1083_1109[0][1][1]) else False) if shen_consp(KL_ARG_V1083_1109[0][1]) else False) if (symdic.symdic_shen_mu == KL_ARG_V1083_1109[0][0]) else False) if shen_consp(KL_ARG_V1083_1109[0]) else False) if shen_consp(KL_ARG_V1083_1109) else False) else (tail_call(kl_subst, [KL_ARG_V1083_1109[1][0], KL_ARG_V1083_1109[0][1][0], tco_apply(shen_mu_reduction, [KL_ARG_V1083_1109[0][1][1][0], KL_ARG_V1084_1110])]) if ((((((((tco_apply(shen_ephemeral_variablex63, [KL_ARG_V1083_1109[0][1][0], KL_ARG_V1083_1109[1][0]]) if ([] == KL_ARG_V1083_1109[1][1]) else False) if shen_consp(KL_ARG_V1083_1109[1]) else False) if ([] == KL_ARG_V1083_1109[0][1][1][1]) else False) if shen_consp(KL_ARG_V1083_1109[0][1][1]) else False) if shen_consp(KL_ARG_V1083_1109[0][1]) else False) if (symdic.symdic_shen_mu == KL_ARG_V1083_1109[0][0]) else False) if shen_consp(KL_ARG_V1083_1109[0]) else False) if shen_consp(KL_ARG_V1083_1109) else False) else ([symdic.symdic_kl_let, [KL_ARG_V1083_1109[0][1][0], [symdic.symdic_shen_be, [KL_ARG_V1083_1109[1][0], [symdic.symdic_kl_in, [tco_apply(shen_mu_reduction, [KL_ARG_V1083_1109[0][1][1][0], KL_ARG_V1084_1110]), []]]]]]] if ((((((((tco_apply(kl_variablex63, [KL_ARG_V1083_1109[0][1][0]]) if ([] == KL_ARG_V1083_1109[1][1]) else False) if shen_consp(KL_ARG_V1083_1109[1]) else False) if ([] == KL_ARG_V1083_1109[0][1][1][1]) else False) if shen_consp(KL_ARG_V1083_1109[0][1][1]) else False) if shen_consp(KL_ARG_V1083_1109[0][1]) else False) if (symdic.symdic_shen_mu == KL_ARG_V1083_1109[0][0]) else False) if shen_consp(KL_ARG_V1083_1109[0]) else False) if shen_consp(KL_ARG_V1083_1109) else False) else ([setattr(KL_CTX, 'KL_LOC_Z_1111', tco_apply(kl_gensym, [symdic.symdic_V])), [symdic.symdic_kl_let, [KL_CTX.KL_LOC_Z_1111, [symdic.symdic_shen_be, [[symdic.symdic_shen_the, [symdic.symdic_shen_result, [symdic.symdic_shen_of, [symdic.symdic_shen_dereferencing, KL_ARG_V1083_1109[1]]]]], [symdic.symdic_kl_in, [[symdic.symdic_kl_if, [[KL_CTX.KL_LOC_Z_1111, [symdic.symdic_kl_is, [symdic.symdic_kl_identical, [symdic.symdic_shen_to, [KL_ARG_V1083_1109[0][1][0], []]]]]], [symdic.symdic_shen_then, [tco_apply(shen_mu_reduction, [KL_ARG_V1083_1109[0][1][1][0], symdic.symdic_kl_x45]), [symdic.symdic_shen_else, [symdic.symdic_shen_failedx33, []]]]]]], []]]]]]]][(-1)] if (((((((((tco_apply(shen_prolog_constantx63, [KL_ARG_V1083_1109[0][1][0]]) if (symdic.symdic_kl_x45 == KL_ARG_V1084_1110) else False) if ([] == KL_ARG_V1083_1109[1][1]) else False) if shen_consp(KL_ARG_V1083_1109[1]) else False) if ([] == KL_ARG_V1083_1109[0][1][1][1]) else False) if shen_consp(KL_ARG_V1083_1109[0][1][1]) else False) if shen_consp(KL_ARG_V1083_1109[0][1]) else False) if (symdic.symdic_shen_mu == KL_ARG_V1083_1109[0][0]) else False) if shen_consp(KL_ARG_V1083_1109[0]) else False) if shen_consp(KL_ARG_V1083_1109) else False) else ([setattr(KL_CTX, 'KL_LOC_Z_1112', tco_apply(kl_gensym, [symdic.symdic_V])), [symdic.symdic_kl_let, [KL_CTX.KL_LOC_Z_1112, [symdic.symdic_shen_be, [[symdic.symdic_shen_the, [symdic.symdic_shen_result, [symdic.symdic_shen_of, [symdic.symdic_shen_dereferencing, KL_ARG_V1083_1109[1]]]]], [symdic.symdic_kl_in, [[symdic.symdic_kl_if, [[KL_CTX.KL_LOC_Z_1112, [symdic.symdic_kl_is, [symdic.symdic_kl_identical, [symdic.symdic_shen_to, [KL_ARG_V1083_1109[0][1][0], []]]]]], [symdic.symdic_shen_then, [tco_apply(shen_mu_reduction, [KL_ARG_V1083_1109[0][1][1][0], symdic.symdic_kl_x43]), [symdic.symdic_shen_else, [[symdic.symdic_kl_if, [[KL_CTX.KL_LOC_Z_1112, [symdic.symdic_kl_is, [symdic.symdic_shen_a, [symdic.symdic_shen_variable, []]]]], [symdic.symdic_shen_then, [[symdic.symdic_kl_bind, [KL_CTX.KL_LOC_Z_1112, [symdic.symdic_shen_to, [KL_ARG_V1083_1109[0][1][0], [symdic.symdic_kl_in, [tco_apply(shen_mu_reduction, [KL_ARG_V1083_1109[0][1][1][0], symdic.symdic_kl_x43]), []]]]]]], [symdic.symdic_shen_else, [symdic.symdic_shen_failedx33, []]]]]]], []]]]]]], []]]]]]]][(-1)] if (((((((((tco_apply(shen_prolog_constantx63, [KL_ARG_V1083_1109[0][1][0]]) if (symdic.symdic_kl_x43 == KL_ARG_V1084_1110) else False) if ([] == KL_ARG_V1083_1109[1][1]) else False) if shen_consp(KL_ARG_V1083_1109[1]) else False) if ([] == KL_ARG_V1083_1109[0][1][1][1]) else False) if shen_consp(KL_ARG_V1083_1109[0][1][1]) else False) if shen_consp(KL_ARG_V1083_1109[0][1]) else False) if (symdic.symdic_shen_mu == KL_ARG_V1083_1109[0][0]) else False) if shen_consp(KL_ARG_V1083_1109[0]) else False) if shen_consp(KL_ARG_V1083_1109) else False) else ([setattr(KL_CTX, 'KL_LOC_Z_1113', tco_apply(kl_gensym, [symdic.symdic_V])), [symdic.symdic_kl_let, [KL_CTX.KL_LOC_Z_1113, [symdic.symdic_shen_be, [[symdic.symdic_shen_the, [symdic.symdic_shen_result, [symdic.symdic_shen_of, [symdic.symdic_shen_dereferencing, KL_ARG_V1083_1109[1]]]]], [symdic.symdic_kl_in, [[symdic.symdic_kl_if, [[KL_CTX.KL_LOC_Z_1113, [symdic.symdic_kl_is, [symdic.symdic_shen_a, [symdic.symdic_shen_nonx45empty, [symdic.symdic_kl_list, []]]]]], [symdic.symdic_shen_then, [tco_apply(shen_mu_reduction, [[[symdic.symdic_shen_mu, [KL_ARG_V1083_1109[0][1][0][0], [[[symdic.symdic_shen_mu, [KL_ARG_V1083_1109[0][1][0][1], KL_ARG_V1083_1109[0][1][1]]], [[symdic.symdic_shen_the, [symdic.symdic_kl_tail, [symdic.symdic_shen_of, [KL_CTX.KL_LOC_Z_1113, []]]]], []]], []]]], [[symdic.symdic_shen_the, [symdic.symdic_kl_head, [symdic.symdic_shen_of, [KL_CTX.KL_LOC_Z_1113, []]]]], []]], symdic.symdic_kl_x45]), [symdic.symdic_shen_else, [symdic.symdic_shen_failedx33, []]]]]]], []]]]]]]][(-1)] if ((((((((((symdic.symdic_kl_x45 == KL_ARG_V1084_1110) if ([] == KL_ARG_V1083_1109[1][1]) else False) if shen_consp(KL_ARG_V1083_1109[1]) else False) if ([] == KL_ARG_V1083_1109[0][1][1][1]) else False) if shen_consp(KL_ARG_V1083_1109[0][1][1]) else False) if shen_consp(KL_ARG_V1083_1109[0][1][0]) else False) if shen_consp(KL_ARG_V1083_1109[0][1]) else False) if (symdic.symdic_shen_mu == KL_ARG_V1083_1109[0][0]) else False) if shen_consp(KL_ARG_V1083_1109[0]) else False) if shen_consp(KL_ARG_V1083_1109) else False) else ([setattr(KL_CTX, 'KL_LOC_Z_1114', tco_apply(kl_gensym, [symdic.symdic_V])), [symdic.symdic_kl_let, [KL_CTX.KL_LOC_Z_1114, [symdic.symdic_shen_be, [[symdic.symdic_shen_the, [symdic.symdic_shen_result, [symdic.symdic_shen_of, [symdic.symdic_shen_dereferencing, KL_ARG_V1083_1109[1]]]]], [symdic.symdic_kl_in, [[symdic.symdic_kl_if, [[KL_CTX.KL_LOC_Z_1114, [symdic.symdic_kl_is, [symdic.symdic_shen_a, [symdic.symdic_shen_nonx45empty, [symdic.symdic_kl_list, []]]]]], [symdic.symdic_shen_then, [tco_apply(shen_mu_reduction, [[[symdic.symdic_shen_mu, [KL_ARG_V1083_1109[0][1][0][0], [[[symdic.symdic_shen_mu, [KL_ARG_V1083_1109[0][1][0][1], KL_ARG_V1083_1109[0][1][1]]], [[symdic.symdic_shen_the, [symdic.symdic_kl_tail, [symdic.symdic_shen_of, [KL_CTX.KL_LOC_Z_1114, []]]]], []]], []]]], [[symdic.symdic_shen_the, [symdic.symdic_kl_head, [symdic.symdic_shen_of, [KL_CTX.KL_LOC_Z_1114, []]]]], []]], symdic.symdic_kl_x43]), [symdic.symdic_shen_else, [[symdic.symdic_kl_if, [[KL_CTX.KL_LOC_Z_1114, [symdic.symdic_kl_is, [symdic.symdic_shen_a, [symdic.symdic_shen_variable, []]]]], [symdic.symdic_shen_then, [[symdic.symdic_shen_rename, [symdic.symdic_shen_the, [symdic.symdic_shen_variables, [symdic.symdic_kl_in, [tco_apply(shen_extract_vars, [KL_ARG_V1083_1109[0][1][0]]), [symdic.symdic_kl_and, [symdic.symdic_shen_then, [[symdic.symdic_kl_bind, [KL_CTX.KL_LOC_Z_1114, [symdic.symdic_shen_to, [tco_apply(shen_rcons_form, [tco_apply(shen_remove_modes, [KL_ARG_V1083_1109[0][1][0]])]), [symdic.symdic_kl_in, [tco_apply(shen_mu_reduction, [KL_ARG_V1083_1109[0][1][1][0], symdic.symdic_kl_x43]), []]]]]]], []]]]]]]]], [symdic.symdic_shen_else, [symdic.symdic_shen_failedx33, []]]]]]], []]]]]]], []]]]]]]][(-1)] if ((((((((((symdic.symdic_kl_x43 == KL_ARG_V1084_1110) if ([] == KL_ARG_V1083_1109[1][1]) else False) if shen_consp(KL_ARG_V1083_1109[1]) else False) if ([] == KL_ARG_V1083_1109[0][1][1][1]) else False) if shen_consp(KL_ARG_V1083_1109[0][1][1]) else False) if shen_consp(KL_ARG_V1083_1109[0][1][0]) else False) if shen_consp(KL_ARG_V1083_1109[0][1]) else False) if (symdic.symdic_shen_mu == KL_ARG_V1083_1109[0][0]) else False) if shen_consp(KL_ARG_V1083_1109[0]) else False) if shen_consp(KL_ARG_V1083_1109) else False) else (KL_ARG_V1083_1109 if True else shen_simple_error('condition failure'))))))))))
shen_add_fun('shen.mu_reduction', shen_mu_reduction, 2)

@tail_recursion
def shen_rcons_form(KL_ARG_V1085_1115):
    global symdic
    return ([symdic.symdic_kl_cons, [tco_apply(shen_rcons_form, [KL_ARG_V1085_1115[0]]), [tco_apply(shen_rcons_form, [KL_ARG_V1085_1115[1]]), []]]] if shen_consp(KL_ARG_V1085_1115) else (KL_ARG_V1085_1115 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.rcons_form', shen_rcons_form, 1)

@tail_recursion
def shen_remove_modes(KL_ARG_V1086_1116):
    global symdic
    return (tail_call(shen_remove_modes, [KL_ARG_V1086_1116[1][0]]) if (((((([] == KL_ARG_V1086_1116[1][1][1]) if (symdic.symdic_kl_x43 == KL_ARG_V1086_1116[1][1][0]) else False) if shen_consp(KL_ARG_V1086_1116[1][1]) else False) if shen_consp(KL_ARG_V1086_1116[1]) else False) if (symdic.symdic_kl_mode == KL_ARG_V1086_1116[0]) else False) if shen_consp(KL_ARG_V1086_1116) else False) else (tail_call(shen_remove_modes, [KL_ARG_V1086_1116[1][0]]) if (((((([] == KL_ARG_V1086_1116[1][1][1]) if (symdic.symdic_kl_x45 == KL_ARG_V1086_1116[1][1][0]) else False) if shen_consp(KL_ARG_V1086_1116[1][1]) else False) if shen_consp(KL_ARG_V1086_1116[1]) else False) if (symdic.symdic_kl_mode == KL_ARG_V1086_1116[0]) else False) if shen_consp(KL_ARG_V1086_1116) else False) else ([tco_apply(shen_remove_modes, [KL_ARG_V1086_1116[0]]), tco_apply(shen_remove_modes, [KL_ARG_V1086_1116[1]])] if shen_consp(KL_ARG_V1086_1116) else (KL_ARG_V1086_1116 if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.remove_modes', shen_remove_modes, 1)

@tail_recursion
def shen_ephemeral_variablex63(KL_ARG_V1087_1117, KL_ARG_V1088_1118):
    global symdic
    return (tail_call(kl_variablex63, [KL_ARG_V1088_1118]) if tco_apply(kl_variablex63, [KL_ARG_V1087_1117]) else False)
shen_add_fun('shen.ephemeral_variable?', shen_ephemeral_variablex63, 2)

@tail_recursion
def shen_prolog_constantx63(KL_ARG_V1097_1119):
    global symdic
    return (False if shen_consp(KL_ARG_V1097_1119) else (True if True else shen_simple_error('condition failure')))
shen_add_fun('shen.prolog_constant?', shen_prolog_constantx63, 1)

@tail_recursion
def shen_aum_to_shen(KL_ARG_V1098_1120):
    global symdic
    return ([symdic.symdic_kl_let, [KL_ARG_V1098_1120[1][0], [tco_apply(shen_aum_to_shen, [KL_ARG_V1098_1120[1][1][1][0]]), [tco_apply(shen_aum_to_shen, [KL_ARG_V1098_1120[1][1][1][1][1][0]]), []]]]] if (((((((((([] == KL_ARG_V1098_1120[1][1][1][1][1][1]) if shen_consp(KL_ARG_V1098_1120[1][1][1][1][1]) else False) if (symdic.symdic_kl_in == KL_ARG_V1098_1120[1][1][1][1][0]) else False) if shen_consp(KL_ARG_V1098_1120[1][1][1][1]) else False) if shen_consp(KL_ARG_V1098_1120[1][1][1]) else False) if (symdic.symdic_shen_be == KL_ARG_V1098_1120[1][1][0]) else False) if shen_consp(KL_ARG_V1098_1120[1][1]) else False) if shen_consp(KL_ARG_V1098_1120[1]) else False) if (symdic.symdic_kl_let == KL_ARG_V1098_1120[0]) else False) if shen_consp(KL_ARG_V1098_1120) else False) else ([symdic.symdic_shen_lazyderef, [tco_apply(shen_aum_to_shen, [KL_ARG_V1098_1120[1][1][1][1][0]]), [symdic.symdic_ProcessN, []]]] if (((((((((([] == KL_ARG_V1098_1120[1][1][1][1][1]) if shen_consp(KL_ARG_V1098_1120[1][1][1][1]) else False) if (symdic.symdic_shen_dereferencing == KL_ARG_V1098_1120[1][1][1][0]) else False) if shen_consp(KL_ARG_V1098_1120[1][1][1]) else False) if (symdic.symdic_shen_of == KL_ARG_V1098_1120[1][1][0]) else False) if shen_consp(KL_ARG_V1098_1120[1][1]) else False) if (symdic.symdic_shen_result == KL_ARG_V1098_1120[1][0]) else False) if shen_consp(KL_ARG_V1098_1120[1]) else False) if (symdic.symdic_shen_the == KL_ARG_V1098_1120[0]) else False) if shen_consp(KL_ARG_V1098_1120) else False) else ([symdic.symdic_kl_if, [tco_apply(shen_aum_to_shen, [KL_ARG_V1098_1120[1][0]]), [tco_apply(shen_aum_to_shen, [KL_ARG_V1098_1120[1][1][1][0]]), [tco_apply(shen_aum_to_shen, [KL_ARG_V1098_1120[1][1][1][1][1][0]]), []]]]] if (((((((((([] == KL_ARG_V1098_1120[1][1][1][1][1][1]) if shen_consp(KL_ARG_V1098_1120[1][1][1][1][1]) else False) if (symdic.symdic_shen_else == KL_ARG_V1098_1120[1][1][1][1][0]) else False) if shen_consp(KL_ARG_V1098_1120[1][1][1][1]) else False) if shen_consp(KL_ARG_V1098_1120[1][1][1]) else False) if (symdic.symdic_shen_then == KL_ARG_V1098_1120[1][1][0]) else False) if shen_consp(KL_ARG_V1098_1120[1][1]) else False) if shen_consp(KL_ARG_V1098_1120[1]) else False) if (symdic.symdic_kl_if == KL_ARG_V1098_1120[0]) else False) if shen_consp(KL_ARG_V1098_1120) else False) else ([symdic.symdic_shen_pvarx63, [KL_ARG_V1098_1120[0], []]] if (((((((([] == KL_ARG_V1098_1120[1][1][1][1]) if (symdic.symdic_shen_variable == KL_ARG_V1098_1120[1][1][1][0]) else False) if shen_consp(KL_ARG_V1098_1120[1][1][1]) else False) if (symdic.symdic_shen_a == KL_ARG_V1098_1120[1][1][0]) else False) if shen_consp(KL_ARG_V1098_1120[1][1]) else False) if (symdic.symdic_kl_is == KL_ARG_V1098_1120[1][0]) else False) if shen_consp(KL_ARG_V1098_1120[1]) else False) if shen_consp(KL_ARG_V1098_1120) else False) else ([symdic.symdic_kl_consx63, [KL_ARG_V1098_1120[0], []]] if (((((((((([] == KL_ARG_V1098_1120[1][1][1][1][1]) if (symdic.symdic_kl_list == KL_ARG_V1098_1120[1][1][1][1][0]) else False) if shen_consp(KL_ARG_V1098_1120[1][1][1][1]) else False) if (symdic.symdic_shen_nonx45empty == KL_ARG_V1098_1120[1][1][1][0]) else False) if shen_consp(KL_ARG_V1098_1120[1][1][1]) else False) if (symdic.symdic_shen_a == KL_ARG_V1098_1120[1][1][0]) else False) if shen_consp(KL_ARG_V1098_1120[1][1]) else False) if (symdic.symdic_kl_is == KL_ARG_V1098_1120[1][0]) else False) if shen_consp(KL_ARG_V1098_1120[1]) else False) if shen_consp(KL_ARG_V1098_1120) else False) else (tail_call(shen_aum_to_shen, [KL_ARG_V1098_1120[1][1][1][1][1][1][1][0]]) if (((((((((((((((([] == KL_ARG_V1098_1120[1][1][1][1][1][1][1][1]) if shen_consp(KL_ARG_V1098_1120[1][1][1][1][1][1][1]) else False) if (symdic.symdic_shen_then == KL_ARG_V1098_1120[1][1][1][1][1][1][0]) else False) if shen_consp(KL_ARG_V1098_1120[1][1][1][1][1][1]) else False) if (symdic.symdic_kl_and == KL_ARG_V1098_1120[1][1][1][1][1][0]) else False) if shen_consp(KL_ARG_V1098_1120[1][1][1][1][1]) else False) if ([] == KL_ARG_V1098_1120[1][1][1][1][0]) else False) if shen_consp(KL_ARG_V1098_1120[1][1][1][1]) else False) if (symdic.symdic_kl_in == KL_ARG_V1098_1120[1][1][1][0]) else False) if shen_consp(KL_ARG_V1098_1120[1][1][1]) else False) if (symdic.symdic_shen_variables == KL_ARG_V1098_1120[1][1][0]) else False) if shen_consp(KL_ARG_V1098_1120[1][1]) else False) if (symdic.symdic_shen_the == KL_ARG_V1098_1120[1][0]) else False) if shen_consp(KL_ARG_V1098_1120[1]) else False) if (symdic.symdic_shen_rename == KL_ARG_V1098_1120[0]) else False) if shen_consp(KL_ARG_V1098_1120) else False) else ([symdic.symdic_kl_let, [KL_ARG_V1098_1120[1][1][1][1][0][0], [[symdic.symdic_shen_newpv, [symdic.symdic_ProcessN, []]], [tco_apply(shen_aum_to_shen, [[symdic.symdic_shen_rename, [symdic.symdic_shen_the, [symdic.symdic_shen_variables, [symdic.symdic_kl_in, [KL_ARG_V1098_1120[1][1][1][1][0][1], KL_ARG_V1098_1120[1][1][1][1][1]]]]]]]), []]]]] if (((((((((((((((([] == KL_ARG_V1098_1120[1][1][1][1][1][1][1][1]) if shen_consp(KL_ARG_V1098_1120[1][1][1][1][1][1][1]) else False) if (symdic.symdic_shen_then == KL_ARG_V1098_1120[1][1][1][1][1][1][0]) else False) if shen_consp(KL_ARG_V1098_1120[1][1][1][1][1][1]) else False) if (symdic.symdic_kl_and == KL_ARG_V1098_1120[1][1][1][1][1][0]) else False) if shen_consp(KL_ARG_V1098_1120[1][1][1][1][1]) else False) if shen_consp(KL_ARG_V1098_1120[1][1][1][1][0]) else False) if shen_consp(KL_ARG_V1098_1120[1][1][1][1]) else False) if (symdic.symdic_kl_in == KL_ARG_V1098_1120[1][1][1][0]) else False) if shen_consp(KL_ARG_V1098_1120[1][1][1]) else False) if (symdic.symdic_shen_variables == KL_ARG_V1098_1120[1][1][0]) else False) if shen_consp(KL_ARG_V1098_1120[1][1]) else False) if (symdic.symdic_shen_the == KL_ARG_V1098_1120[1][0]) else False) if shen_consp(KL_ARG_V1098_1120[1]) else False) if (symdic.symdic_shen_rename == KL_ARG_V1098_1120[0]) else False) if shen_consp(KL_ARG_V1098_1120) else False) else ([symdic.symdic_kl_do, [[symdic.symdic_shen_bindv, [KL_ARG_V1098_1120[1][0], [tco_apply(shen_chwild, [KL_ARG_V1098_1120[1][1][1][0]]), [symdic.symdic_ProcessN, []]]]], [[symdic.symdic_kl_let, [symdic.symdic_Result, [tco_apply(shen_aum_to_shen, [KL_ARG_V1098_1120[1][1][1][1][1][0]]), [[symdic.symdic_kl_do, [[symdic.symdic_shen_unbindv, [KL_ARG_V1098_1120[1][0], [symdic.symdic_ProcessN, []]]], [symdic.symdic_Result, []]]], []]]]], []]]] if (((((((((([] == KL_ARG_V1098_1120[1][1][1][1][1][1]) if shen_consp(KL_ARG_V1098_1120[1][1][1][1][1]) else False) if (symdic.symdic_kl_in == KL_ARG_V1098_1120[1][1][1][1][0]) else False) if shen_consp(KL_ARG_V1098_1120[1][1][1][1]) else False) if shen_consp(KL_ARG_V1098_1120[1][1][1]) else False) if (symdic.symdic_shen_to == KL_ARG_V1098_1120[1][1][0]) else False) if shen_consp(KL_ARG_V1098_1120[1][1]) else False) if shen_consp(KL_ARG_V1098_1120[1]) else False) if (symdic.symdic_kl_bind == KL_ARG_V1098_1120[0]) else False) if shen_consp(KL_ARG_V1098_1120) else False) else ([symdic.symdic_kl_x61, [KL_ARG_V1098_1120[1][1][1][1][0], [KL_ARG_V1098_1120[0], []]]] if ((((((((([] == KL_ARG_V1098_1120[1][1][1][1][1]) if shen_consp(KL_ARG_V1098_1120[1][1][1][1]) else False) if (symdic.symdic_shen_to == KL_ARG_V1098_1120[1][1][1][0]) else False) if shen_consp(KL_ARG_V1098_1120[1][1][1]) else False) if (symdic.symdic_kl_identical == KL_ARG_V1098_1120[1][1][0]) else False) if shen_consp(KL_ARG_V1098_1120[1][1]) else False) if (symdic.symdic_kl_is == KL_ARG_V1098_1120[1][0]) else False) if shen_consp(KL_ARG_V1098_1120[1]) else False) if shen_consp(KL_ARG_V1098_1120) else False) else (False if (symdic.symdic_shen_failedx33 == KL_ARG_V1098_1120) else ([symdic.symdic_kl_hd, KL_ARG_V1098_1120[1][1][1]] if (((((((([] == KL_ARG_V1098_1120[1][1][1][1]) if shen_consp(KL_ARG_V1098_1120[1][1][1]) else False) if (symdic.symdic_shen_of == KL_ARG_V1098_1120[1][1][0]) else False) if shen_consp(KL_ARG_V1098_1120[1][1]) else False) if (symdic.symdic_kl_head == KL_ARG_V1098_1120[1][0]) else False) if shen_consp(KL_ARG_V1098_1120[1]) else False) if (symdic.symdic_shen_the == KL_ARG_V1098_1120[0]) else False) if shen_consp(KL_ARG_V1098_1120) else False) else ([symdic.symdic_kl_tl, KL_ARG_V1098_1120[1][1][1]] if (((((((([] == KL_ARG_V1098_1120[1][1][1][1]) if shen_consp(KL_ARG_V1098_1120[1][1][1]) else False) if (symdic.symdic_shen_of == KL_ARG_V1098_1120[1][1][0]) else False) if shen_consp(KL_ARG_V1098_1120[1][1]) else False) if (symdic.symdic_kl_tail == KL_ARG_V1098_1120[1][0]) else False) if shen_consp(KL_ARG_V1098_1120[1]) else False) if (symdic.symdic_shen_the == KL_ARG_V1098_1120[0]) else False) if shen_consp(KL_ARG_V1098_1120) else False) else ([symdic.symdic_kl_do, [[symdic.symdic_shen_incinfs, []], [[symdic.symdic_kl_thaw, [symdic.symdic_Continuation, []]], []]]] if ((((((([] == KL_ARG_V1098_1120[1][1][1]) if (symdic.symdic_shen_stack == KL_ARG_V1098_1120[1][1][0]) else False) if shen_consp(KL_ARG_V1098_1120[1][1]) else False) if (symdic.symdic_shen_the == KL_ARG_V1098_1120[1][0]) else False) if shen_consp(KL_ARG_V1098_1120[1]) else False) if (symdic.symdic_shen_pop == KL_ARG_V1098_1120[0]) else False) if shen_consp(KL_ARG_V1098_1120) else False) else ([symdic.symdic_kl_do, [[symdic.symdic_shen_incinfs, []], [tco_apply(shen_call_the_continuation, [tco_apply(shen_chwild, [KL_ARG_V1098_1120[1][1][1][0]]), symdic.symdic_ProcessN, symdic.symdic_Continuation]), []]]] if (((((((([] == KL_ARG_V1098_1120[1][1][1][1]) if shen_consp(KL_ARG_V1098_1120[1][1][1]) else False) if (symdic.symdic_shen_continuation == KL_ARG_V1098_1120[1][1][0]) else False) if shen_consp(KL_ARG_V1098_1120[1][1]) else False) if (symdic.symdic_shen_the == KL_ARG_V1098_1120[1][0]) else False) if shen_consp(KL_ARG_V1098_1120[1]) else False) if (symdic.symdic_kl_call == KL_ARG_V1098_1120[0]) else False) if shen_consp(KL_ARG_V1098_1120) else False) else (KL_ARG_V1098_1120 if True else shen_simple_error('condition failure'))))))))))))))))
shen_add_fun('shen.aum_to_shen', shen_aum_to_shen, 1)

@tail_recursion
def shen_chwild(KL_ARG_V1099_1121):
    global symdic
    return ([symdic.symdic_shen_newpv, [symdic.symdic_ProcessN, []]] if (KL_ARG_V1099_1121 == symdic.symdic_kl__) else (tail_call(kl_map, [symdic.symdic_shen_chwild, KL_ARG_V1099_1121]) if shen_consp(KL_ARG_V1099_1121) else (KL_ARG_V1099_1121 if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.chwild', shen_chwild, 1)

@tail_recursion
def shen_newpv(KL_ARG_V1100_1122):

    class KL_Context:
        KL_LOC_Countx431_1123 = None
        KL_LOC_IncVar_1124 = None
        KL_LOC_Vector_1125 = None
        KL_LOC_ResizeVectorIfNeeded_1126 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Countx431_1123', (shen_absvector_get(shen_get(symdic.symdic_shen_x42varcounterx42), KL_ARG_V1100_1122) + 1)), [setattr(KL_CTX, 'KL_LOC_IncVar_1124', shen_absvector_set(shen_get(symdic.symdic_shen_x42varcounterx42), KL_ARG_V1100_1122, KL_CTX.KL_LOC_Countx431_1123)), [setattr(KL_CTX, 'KL_LOC_Vector_1125', shen_absvector_get(shen_get(symdic.symdic_shen_x42prologvectorsx42), KL_ARG_V1100_1122)), [setattr(KL_CTX, 'KL_LOC_ResizeVectorIfNeeded_1126', (tco_apply(shen_resizeprocessvector, [KL_ARG_V1100_1122, KL_CTX.KL_LOC_Countx431_1123]) if (KL_CTX.KL_LOC_Countx431_1123 == tco_apply(kl_limit, [KL_CTX.KL_LOC_Vector_1125])) else symdic.symdic_shen_skip)), tail_call(shen_mkx45pvar, [KL_CTX.KL_LOC_Countx431_1123])][(-1)]][(-1)]][(-1)]][(-1)]
shen_add_fun('shen.newpv', shen_newpv, 1)

@tail_recursion
def shen_resizeprocessvector(KL_ARG_V1101_1127, KL_ARG_V1102_1128):

    class KL_Context:
        KL_LOC_Vector_1129 = None
        KL_LOC_BigVector_1130 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Vector_1129', shen_absvector_get(shen_get(symdic.symdic_shen_x42prologvectorsx42), KL_ARG_V1101_1127)), [setattr(KL_CTX, 'KL_LOC_BigVector_1130', tco_apply(shen_resizex45vector, [KL_CTX.KL_LOC_Vector_1129, (KL_ARG_V1102_1128 + KL_ARG_V1102_1128), symdic.symdic_shen_x45nullx45])), shen_absvector_set(shen_get(symdic.symdic_shen_x42prologvectorsx42), KL_ARG_V1101_1127, KL_CTX.KL_LOC_BigVector_1130)][(-1)]][(-1)]
shen_add_fun('shen.resizeprocessvector', shen_resizeprocessvector, 2)

@tail_recursion
def shen_resizex45vector(KL_ARG_V1103_1131, KL_ARG_V1104_1132, KL_ARG_V1105_1133):

    class KL_Context:
        KL_LOC_BigVector_1134 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_BigVector_1134', shen_absvector_set(shen_absvector((1 + KL_ARG_V1104_1132)), 0, KL_ARG_V1104_1132)), tail_call(shen_copyx45vector, [KL_ARG_V1103_1131, KL_CTX.KL_LOC_BigVector_1134, tco_apply(kl_limit, [KL_ARG_V1103_1131]), KL_ARG_V1104_1132, KL_ARG_V1105_1133])][(-1)]
shen_add_fun('shen.resize-vector', shen_resizex45vector, 3)

@tail_recursion
def shen_copyx45vector(KL_ARG_V1106_1135, KL_ARG_V1107_1136, KL_ARG_V1108_1137, KL_ARG_V1109_1138, KL_ARG_V1110_1139):
    global symdic
    return tail_call(shen_copyx45vectorx45stagex452, [(1 + KL_ARG_V1108_1137), (KL_ARG_V1109_1138 + 1), KL_ARG_V1110_1139, tco_apply(shen_copyx45vectorx45stagex451, [1, KL_ARG_V1106_1135, KL_ARG_V1107_1136, (1 + KL_ARG_V1108_1137)])])
shen_add_fun('shen.copy-vector', shen_copyx45vector, 5)

@tail_recursion
def shen_copyx45vectorx45stagex451(KL_ARG_V1113_1140, KL_ARG_V1114_1141, KL_ARG_V1115_1142, KL_ARG_V1116_1143):
    global symdic
    return (KL_ARG_V1115_1142 if (KL_ARG_V1116_1143 == KL_ARG_V1113_1140) else (tail_call(shen_copyx45vectorx45stagex451, [(1 + KL_ARG_V1113_1140), KL_ARG_V1114_1141, shen_absvector_set(KL_ARG_V1115_1142, KL_ARG_V1113_1140, shen_absvector_get(KL_ARG_V1114_1141, KL_ARG_V1113_1140)), KL_ARG_V1116_1143]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.copy-vector-stage-1', shen_copyx45vectorx45stagex451, 4)

@tail_recursion
def shen_copyx45vectorx45stagex452(KL_ARG_V1120_1144, KL_ARG_V1121_1145, KL_ARG_V1122_1146, KL_ARG_V1123_1147):
    global symdic
    return (KL_ARG_V1123_1147 if (KL_ARG_V1121_1145 == KL_ARG_V1120_1144) else (tail_call(shen_copyx45vectorx45stagex452, [(KL_ARG_V1120_1144 + 1), KL_ARG_V1121_1145, KL_ARG_V1122_1146, shen_absvector_set(KL_ARG_V1123_1147, KL_ARG_V1120_1144, KL_ARG_V1122_1146)]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.copy-vector-stage-2', shen_copyx45vectorx45stagex452, 4)

@tail_recursion
def shen_mkx45pvar(KL_ARG_V1125_1148):
    global symdic
    return shen_absvector_set(shen_absvector_set(shen_absvector(2), 0, symdic.symdic_shen_pvar), 1, KL_ARG_V1125_1148)
shen_add_fun('shen.mk-pvar', shen_mkx45pvar, 1)

@tail_recursion
def shen_pvarx63(KL_ARG_V1126_1149):
    global symdic
    return ((shen_absvector_get(KL_ARG_V1126_1149, 0) == symdic.symdic_shen_pvar) if shen_absvectorp(KL_ARG_V1126_1149) else False)
shen_add_fun('shen.pvar?', shen_pvarx63, 1)

@tail_recursion
def shen_bindv(KL_ARG_V1127_1150, KL_ARG_V1128_1151, KL_ARG_V1129_1152):

    class KL_Context:
        KL_LOC_Vector_1153 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Vector_1153', shen_absvector_get(shen_get(symdic.symdic_shen_x42prologvectorsx42), KL_ARG_V1129_1152)), shen_absvector_set(KL_CTX.KL_LOC_Vector_1153, shen_absvector_get(KL_ARG_V1127_1150, 1), KL_ARG_V1128_1151)][(-1)]
shen_add_fun('shen.bindv', shen_bindv, 3)

@tail_recursion
def shen_unbindv(KL_ARG_V1130_1154, KL_ARG_V1131_1155):

    class KL_Context:
        KL_LOC_Vector_1156 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Vector_1156', shen_absvector_get(shen_get(symdic.symdic_shen_x42prologvectorsx42), KL_ARG_V1131_1155)), shen_absvector_set(KL_CTX.KL_LOC_Vector_1156, shen_absvector_get(KL_ARG_V1130_1154, 1), symdic.symdic_shen_x45nullx45)][(-1)]
shen_add_fun('shen.unbindv', shen_unbindv, 2)

@tail_recursion
def shen_incinfs():
    global symdic
    return shen_set(symdic.symdic_shen_x42infsx42, (1 + shen_get(symdic.symdic_shen_x42infsx42)))
shen_add_fun('shen.incinfs', shen_incinfs, 0)

@tail_recursion
def shen_call_the_continuation(KL_ARG_V1132_1157, KL_ARG_V1133_1158, KL_ARG_V1134_1159):

    class KL_Context:
        KL_LOC_NewContinuation_1160 = None
    KL_CTX = KL_Context()
    global symdic
    return ([KL_ARG_V1132_1157[0][0], tco_apply(kl_append, [KL_ARG_V1132_1157[0][1], [KL_ARG_V1133_1158, [KL_ARG_V1134_1159, []]]])] if ((([] == KL_ARG_V1132_1157[1]) if shen_consp(KL_ARG_V1132_1157[0]) else False) if shen_consp(KL_ARG_V1132_1157) else False) else ([setattr(KL_CTX, 'KL_LOC_NewContinuation_1160', tco_apply(shen_newcontinuation, [KL_ARG_V1132_1157[1], KL_ARG_V1133_1158, KL_ARG_V1134_1159])), [KL_ARG_V1132_1157[0][0], tco_apply(kl_append, [KL_ARG_V1132_1157[0][1], [KL_ARG_V1133_1158, [KL_CTX.KL_LOC_NewContinuation_1160, []]]])]][(-1)] if (shen_consp(KL_ARG_V1132_1157[0]) if shen_consp(KL_ARG_V1132_1157) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_call_the_continuation]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.call_the_continuation', shen_call_the_continuation, 3)

@tail_recursion
def shen_newcontinuation(KL_ARG_V1135_1161, KL_ARG_V1136_1162, KL_ARG_V1137_1163):
    global symdic
    return (KL_ARG_V1137_1163 if ([] == KL_ARG_V1135_1161) else ([symdic.symdic_kl_freeze, [[KL_ARG_V1135_1161[0][0], tco_apply(kl_append, [KL_ARG_V1135_1161[0][1], [KL_ARG_V1136_1162, [tco_apply(shen_newcontinuation, [KL_ARG_V1135_1161[1], KL_ARG_V1136_1162, KL_ARG_V1137_1163]), []]]])], []]] if (shen_consp(KL_ARG_V1135_1161[0]) if shen_consp(KL_ARG_V1135_1161) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_newcontinuation]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.newcontinuation', shen_newcontinuation, 3)

@tail_recursion
def kl_return(KL_ARG_V1142_1164, KL_ARG_V1143_1165, KL_ARG_V1144_1166):
    global symdic
    return tail_call(shen_deref, [KL_ARG_V1142_1164, KL_ARG_V1143_1165])
shen_add_fun('return', kl_return, 3)

@tail_recursion
def shen_measurex38return(KL_ARG_V1149_1167, KL_ARG_V1150_1168, KL_ARG_V1151_1169):
    global symdic
    return [tco_apply(shen_prhush, [tco_apply(shen_app, [shen_get(symdic.symdic_shen_x42infsx42), ' inferences\r\n', symdic.symdic_shen_a]), tco_apply(kl_stoutput, [])]), tail_call(shen_deref, [KL_ARG_V1149_1167, KL_ARG_V1150_1168])][(-1)]
shen_add_fun('shen.measure&return', shen_measurex38return, 3)

@tail_recursion
def kl_unify(KL_ARG_V1152_1170, KL_ARG_V1153_1171, KL_ARG_V1154_1172, KL_ARG_V1155_1173):
    global symdic
    return tail_call(shen_lzyx61, [tco_apply(shen_lazyderef, [KL_ARG_V1152_1170, KL_ARG_V1154_1172]), tco_apply(shen_lazyderef, [KL_ARG_V1153_1171, KL_ARG_V1154_1172]), KL_ARG_V1154_1172, KL_ARG_V1155_1173])
shen_add_fun('unify', kl_unify, 4)

@tail_recursion
def shen_lzyx61(KL_ARG_V1172_1174, KL_ARG_V1173_1175, KL_ARG_V1174_1176, KL_ARG_V1175_1177):
    global symdic
    return (tail_call(kl_thaw, [KL_ARG_V1175_1177]) if (KL_ARG_V1173_1175 == KL_ARG_V1172_1174) else (tail_call(kl_bind, [KL_ARG_V1172_1174, KL_ARG_V1173_1175, KL_ARG_V1174_1176, KL_ARG_V1175_1177]) if tco_apply(shen_pvarx63, [KL_ARG_V1172_1174]) else (tail_call(kl_bind, [KL_ARG_V1173_1175, KL_ARG_V1172_1174, KL_ARG_V1174_1176, KL_ARG_V1175_1177]) if tco_apply(shen_pvarx63, [KL_ARG_V1173_1175]) else (tail_call(shen_lzyx61, [tco_apply(shen_lazyderef, [KL_ARG_V1172_1174[0], KL_ARG_V1174_1176]), tco_apply(shen_lazyderef, [KL_ARG_V1173_1175[0], KL_ARG_V1174_1176]), KL_ARG_V1174_1176, (lambda : tail_call(shen_lzyx61, [tco_apply(shen_lazyderef, [KL_ARG_V1172_1174[1], KL_ARG_V1174_1176]), tco_apply(shen_lazyderef, [KL_ARG_V1173_1175[1], KL_ARG_V1174_1176]), KL_ARG_V1174_1176, KL_ARG_V1175_1177]))]) if (shen_consp(KL_ARG_V1173_1175) if shen_consp(KL_ARG_V1172_1174) else False) else (False if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.lzy=', shen_lzyx61, 4)

@tail_recursion
def shen_deref(KL_ARG_V1177_1178, KL_ARG_V1178_1179):

    class KL_Context:
        KL_LOC_Value_1180 = None
    KL_CTX = KL_Context()
    global symdic
    return ([tco_apply(shen_deref, [KL_ARG_V1177_1178[0], KL_ARG_V1178_1179]), tco_apply(shen_deref, [KL_ARG_V1177_1178[1], KL_ARG_V1178_1179])] if shen_consp(KL_ARG_V1177_1178) else (([setattr(KL_CTX, 'KL_LOC_Value_1180', tco_apply(shen_valvector, [KL_ARG_V1177_1178, KL_ARG_V1178_1179])), (KL_ARG_V1177_1178 if (KL_CTX.KL_LOC_Value_1180 == symdic.symdic_shen_x45nullx45) else tail_call(shen_deref, [KL_CTX.KL_LOC_Value_1180, KL_ARG_V1178_1179]))][(-1)] if tco_apply(shen_pvarx63, [KL_ARG_V1177_1178]) else KL_ARG_V1177_1178) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.deref', shen_deref, 2)

@tail_recursion
def shen_lazyderef(KL_ARG_V1179_1181, KL_ARG_V1180_1182):

    class KL_Context:
        KL_LOC_Value_1183 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_Value_1183', tco_apply(shen_valvector, [KL_ARG_V1179_1181, KL_ARG_V1180_1182])), (KL_ARG_V1179_1181 if (KL_CTX.KL_LOC_Value_1183 == symdic.symdic_shen_x45nullx45) else tail_call(shen_lazyderef, [KL_CTX.KL_LOC_Value_1183, KL_ARG_V1180_1182]))][(-1)] if tco_apply(shen_pvarx63, [KL_ARG_V1179_1181]) else KL_ARG_V1179_1181)
shen_add_fun('shen.lazyderef', shen_lazyderef, 2)

@tail_recursion
def shen_valvector(KL_ARG_V1181_1184, KL_ARG_V1182_1185):
    global symdic
    return shen_absvector_get(shen_absvector_get(shen_get(symdic.symdic_shen_x42prologvectorsx42), KL_ARG_V1182_1185), shen_absvector_get(KL_ARG_V1181_1184, 1))
shen_add_fun('shen.valvector', shen_valvector, 2)

@tail_recursion
def kl_unifyx33(KL_ARG_V1183_1186, KL_ARG_V1184_1187, KL_ARG_V1185_1188, KL_ARG_V1186_1189):
    global symdic
    return tail_call(shen_lzyx61x33, [tco_apply(shen_lazyderef, [KL_ARG_V1183_1186, KL_ARG_V1185_1188]), tco_apply(shen_lazyderef, [KL_ARG_V1184_1187, KL_ARG_V1185_1188]), KL_ARG_V1185_1188, KL_ARG_V1186_1189])
shen_add_fun('unify!', kl_unifyx33, 4)

@tail_recursion
def shen_lzyx61x33(KL_ARG_V1203_1190, KL_ARG_V1204_1191, KL_ARG_V1205_1192, KL_ARG_V1206_1193):
    global symdic
    return (tail_call(kl_thaw, [KL_ARG_V1206_1193]) if (KL_ARG_V1204_1191 == KL_ARG_V1203_1190) else (tail_call(kl_bind, [KL_ARG_V1203_1190, KL_ARG_V1204_1191, KL_ARG_V1205_1192, KL_ARG_V1206_1193]) if ((not tco_apply(shen_occursx63, [KL_ARG_V1203_1190, tco_apply(shen_deref, [KL_ARG_V1204_1191, KL_ARG_V1205_1192])])) if tco_apply(shen_pvarx63, [KL_ARG_V1203_1190]) else False) else (tail_call(kl_bind, [KL_ARG_V1204_1191, KL_ARG_V1203_1190, KL_ARG_V1205_1192, KL_ARG_V1206_1193]) if ((not tco_apply(shen_occursx63, [KL_ARG_V1204_1191, tco_apply(shen_deref, [KL_ARG_V1203_1190, KL_ARG_V1205_1192])])) if tco_apply(shen_pvarx63, [KL_ARG_V1204_1191]) else False) else (tail_call(shen_lzyx61x33, [tco_apply(shen_lazyderef, [KL_ARG_V1203_1190[0], KL_ARG_V1205_1192]), tco_apply(shen_lazyderef, [KL_ARG_V1204_1191[0], KL_ARG_V1205_1192]), KL_ARG_V1205_1192, (lambda : tail_call(shen_lzyx61x33, [tco_apply(shen_lazyderef, [KL_ARG_V1203_1190[1], KL_ARG_V1205_1192]), tco_apply(shen_lazyderef, [KL_ARG_V1204_1191[1], KL_ARG_V1205_1192]), KL_ARG_V1205_1192, KL_ARG_V1206_1193]))]) if (shen_consp(KL_ARG_V1204_1191) if shen_consp(KL_ARG_V1203_1190) else False) else (False if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.lzy=!', shen_lzyx61x33, 4)

@tail_recursion
def shen_occursx63(KL_ARG_V1216_1194, KL_ARG_V1217_1195):
    global symdic
    return (True if (KL_ARG_V1217_1195 == KL_ARG_V1216_1194) else ((True if tco_apply(shen_occursx63, [KL_ARG_V1216_1194, KL_ARG_V1217_1195[0]]) else tail_call(shen_occursx63, [KL_ARG_V1216_1194, KL_ARG_V1217_1195[1]])) if shen_consp(KL_ARG_V1217_1195) else (False if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.occurs?', shen_occursx63, 2)

@tail_recursion
def kl_identical(KL_ARG_V1219_1196, KL_ARG_V1220_1197, KL_ARG_V1221_1198, KL_ARG_V1222_1199):
    global symdic
    return tail_call(shen_lzyx61x61, [tco_apply(shen_lazyderef, [KL_ARG_V1219_1196, KL_ARG_V1221_1198]), tco_apply(shen_lazyderef, [KL_ARG_V1220_1197, KL_ARG_V1221_1198]), KL_ARG_V1221_1198, KL_ARG_V1222_1199])
shen_add_fun('identical', kl_identical, 4)

@tail_recursion
def shen_lzyx61x61(KL_ARG_V1239_1200, KL_ARG_V1240_1201, KL_ARG_V1241_1202, KL_ARG_V1242_1203):
    global symdic
    return (tail_call(kl_thaw, [KL_ARG_V1242_1203]) if (KL_ARG_V1240_1201 == KL_ARG_V1239_1200) else (tail_call(shen_lzyx61x61, [tco_apply(shen_lazyderef, [KL_ARG_V1239_1200[0], KL_ARG_V1241_1202]), tco_apply(shen_lazyderef, [KL_ARG_V1240_1201[0], KL_ARG_V1241_1202]), KL_ARG_V1241_1202, (lambda : tail_call(shen_lzyx61x61, [KL_ARG_V1239_1200[1], KL_ARG_V1240_1201[1], KL_ARG_V1241_1202, KL_ARG_V1242_1203]))]) if (shen_consp(KL_ARG_V1240_1201) if shen_consp(KL_ARG_V1239_1200) else False) else (False if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.lzy==', shen_lzyx61x61, 4)

@tail_recursion
def shen_pvar(KL_ARG_V1244_1204):
    global symdic
    return ('Var' + tco_apply(shen_app, [shen_absvector_get(KL_ARG_V1244_1204, 1), '', symdic.symdic_shen_a]))
shen_add_fun('shen.pvar', shen_pvar, 1)

@tail_recursion
def kl_bind(KL_ARG_V1245_1205, KL_ARG_V1246_1206, KL_ARG_V1247_1207, KL_ARG_V1248_1208):

    class KL_Context:
        KL_LOC_Result_1209 = None
    KL_CTX = KL_Context()
    global symdic
    return [tco_apply(shen_bindv, [KL_ARG_V1245_1205, KL_ARG_V1246_1206, KL_ARG_V1247_1207]), [setattr(KL_CTX, 'KL_LOC_Result_1209', tco_apply(kl_thaw, [KL_ARG_V1248_1208])), [tco_apply(shen_unbindv, [KL_ARG_V1245_1205, KL_ARG_V1247_1207]), KL_CTX.KL_LOC_Result_1209][(-1)]][(-1)]][(-1)]
shen_add_fun('bind', kl_bind, 4)

@tail_recursion
def kl_fwhen(KL_ARG_V1263_1210, KL_ARG_V1264_1211, KL_ARG_V1265_1212):
    global symdic
    return (tail_call(kl_thaw, [KL_ARG_V1265_1212]) if (True == KL_ARG_V1263_1210) else (False if (False == KL_ARG_V1263_1210) else (shen_simple_error(('fwhen expects a boolean: not ' + tco_apply(shen_app, [KL_ARG_V1263_1210, '%', symdic.symdic_shen_s]))) if True else shen_simple_error('condition failure'))))
shen_add_fun('fwhen', kl_fwhen, 3)

@tail_recursion
def kl_call(KL_ARG_V1278_1213, KL_ARG_V1279_1214, KL_ARG_V1280_1215):
    global symdic
    return (tail_call(shen_callx45help, [tco_apply(shen_m_prolog_to_sx45prolog_predicate, [tco_apply(shen_lazyderef, [KL_ARG_V1278_1213[0], KL_ARG_V1279_1214])]), KL_ARG_V1278_1213[1], KL_ARG_V1279_1214, KL_ARG_V1280_1215]) if shen_consp(KL_ARG_V1278_1213) else (False if True else shen_simple_error('condition failure')))
shen_add_fun('call', kl_call, 3)

@tail_recursion
def shen_callx45help(KL_ARG_V1281_1216, KL_ARG_V1282_1217, KL_ARG_V1283_1218, KL_ARG_V1284_1219):
    global symdic
    return (shen_apply(KL_ARG_V1281_1216, [KL_ARG_V1283_1218, KL_ARG_V1284_1219]) if ([] == KL_ARG_V1282_1217) else (tail_call(shen_callx45help, [shen_apply(KL_ARG_V1281_1216, [KL_ARG_V1282_1217[0]]), KL_ARG_V1282_1217[1], KL_ARG_V1283_1218, KL_ARG_V1284_1219]) if shen_consp(KL_ARG_V1282_1217) else (tail_call(shen_sysx45error, [symdic.symdic_shen_callx45help]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.call-help', shen_callx45help, 4)

@tail_recursion
def shen_intprolog(KL_ARG_V1285_1220):

    class KL_Context:
        KL_LOC_ProcessN_1221 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_ProcessN_1221', tco_apply(shen_startx45newx45prologx45process, [])), tail_call(shen_intprologx45help, [KL_ARG_V1285_1220[0][0], tco_apply(shen_insertx45prologx45variables, [[KL_ARG_V1285_1220[0][1], [KL_ARG_V1285_1220[1], []]], KL_CTX.KL_LOC_ProcessN_1221]), KL_CTX.KL_LOC_ProcessN_1221])][(-1)] if (shen_consp(KL_ARG_V1285_1220[0]) if shen_consp(KL_ARG_V1285_1220) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_intprolog]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.intprolog', shen_intprolog, 1)

@tail_recursion
def shen_intprologx45help(KL_ARG_V1286_1222, KL_ARG_V1287_1223, KL_ARG_V1288_1224):
    global symdic
    return (tail_call(shen_intprologx45helpx45help, [KL_ARG_V1286_1222, KL_ARG_V1287_1223[0], KL_ARG_V1287_1223[1][0], KL_ARG_V1288_1224]) if ((([] == KL_ARG_V1287_1223[1][1]) if shen_consp(KL_ARG_V1287_1223[1]) else False) if shen_consp(KL_ARG_V1287_1223) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_intprologx45help]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.intprolog-help', shen_intprologx45help, 3)

@tail_recursion
def shen_intprologx45helpx45help(KL_ARG_V1289_1225, KL_ARG_V1290_1226, KL_ARG_V1291_1227, KL_ARG_V1292_1228):
    global symdic
    return (shen_apply(KL_ARG_V1289_1225, [KL_ARG_V1292_1228, (lambda : tail_call(shen_callx45rest, [KL_ARG_V1291_1227, KL_ARG_V1292_1228]))]) if ([] == KL_ARG_V1290_1226) else (tail_call(shen_intprologx45helpx45help, [shen_apply(KL_ARG_V1289_1225, [KL_ARG_V1290_1226[0]]), KL_ARG_V1290_1226[1], KL_ARG_V1291_1227, KL_ARG_V1292_1228]) if shen_consp(KL_ARG_V1290_1226) else (tail_call(shen_sysx45error, [symdic.symdic_shen_intprologx45helpx45help]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.intprolog-help-help', shen_intprologx45helpx45help, 4)

@tail_recursion
def shen_callx45rest(KL_ARG_V1295_1229, KL_ARG_V1296_1230):
    global symdic
    return (True if ([] == KL_ARG_V1295_1229) else (tail_call(shen_callx45rest, [[[tco_apply(KL_ARG_V1295_1229[0][0], [KL_ARG_V1295_1229[0][1][0]]), KL_ARG_V1295_1229[0][1][1]], KL_ARG_V1295_1229[1]], KL_ARG_V1296_1230]) if ((shen_consp(KL_ARG_V1295_1229[0][1]) if shen_consp(KL_ARG_V1295_1229[0]) else False) if shen_consp(KL_ARG_V1295_1229) else False) else (tail_call(KL_ARG_V1295_1229[0][0], [KL_ARG_V1296_1230, (lambda : tail_call(shen_callx45rest, [KL_ARG_V1295_1229[1], KL_ARG_V1296_1230]))]) if ((([] == KL_ARG_V1295_1229[0][1]) if shen_consp(KL_ARG_V1295_1229[0]) else False) if shen_consp(KL_ARG_V1295_1229) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_callx45rest]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.call-rest', shen_callx45rest, 2)

@tail_recursion
def shen_startx45newx45prologx45process():

    class KL_Context:
        KL_LOC_IncrementProcessCounter_1231 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_IncrementProcessCounter_1231', shen_set(symdic.symdic_shen_x42processx45counterx42, (1 + shen_get(symdic.symdic_shen_x42processx45counterx42)))), tail_call(shen_initialisex45prolog, [KL_CTX.KL_LOC_IncrementProcessCounter_1231])][(-1)]
shen_add_fun('shen.start-new-prolog-process', shen_startx45newx45prologx45process, 0)

@tail_recursion
def shen_insertx45prologx45variables(KL_ARG_V1297_1232, KL_ARG_V1298_1233):
    global symdic
    return tail_call(shen_insertx45prologx45variablesx45help, [KL_ARG_V1297_1232, tco_apply(shen_flatten, [KL_ARG_V1297_1232]), KL_ARG_V1298_1233])
shen_add_fun('shen.insert-prolog-variables', shen_insertx45prologx45variables, 2)

@tail_recursion
def shen_insertx45prologx45variablesx45help(KL_ARG_V1303_1234, KL_ARG_V1304_1235, KL_ARG_V1305_1236):

    class KL_Context:
        KL_LOC_V_1237 = None
        KL_LOC_XVx47Y_1238 = None
        KL_LOC_Zx45Y_1239 = None
    KL_CTX = KL_Context()
    global symdic
    return (KL_ARG_V1303_1234 if ([] == KL_ARG_V1304_1235) else ([setattr(KL_CTX, 'KL_LOC_V_1237', tco_apply(shen_newpv, [KL_ARG_V1305_1236])), [setattr(KL_CTX, 'KL_LOC_XVx47Y_1238', tco_apply(kl_subst, [KL_CTX.KL_LOC_V_1237, KL_ARG_V1304_1235[0], KL_ARG_V1303_1234])), [setattr(KL_CTX, 'KL_LOC_Zx45Y_1239', tco_apply(kl_remove, [KL_ARG_V1304_1235[0], KL_ARG_V1304_1235[1]])), tail_call(shen_insertx45prologx45variablesx45help, [KL_CTX.KL_LOC_XVx47Y_1238, KL_CTX.KL_LOC_Zx45Y_1239, KL_ARG_V1305_1236])][(-1)]][(-1)]][(-1)] if (tco_apply(kl_variablex63, [KL_ARG_V1304_1235[0]]) if shen_consp(KL_ARG_V1304_1235) else False) else (tail_call(shen_insertx45prologx45variablesx45help, [KL_ARG_V1303_1234, KL_ARG_V1304_1235[1], KL_ARG_V1305_1236]) if shen_consp(KL_ARG_V1304_1235) else (tail_call(shen_sysx45error, [symdic.symdic_shen_insertx45prologx45variablesx45help]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.insert-prolog-variables-help', shen_insertx45prologx45variablesx45help, 3)

@tail_recursion
def shen_initialisex45prolog(KL_ARG_V1306_1240):

    class KL_Context:
        KL_LOC_Vector_1241 = None
        KL_LOC_Counter_1242 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Vector_1241', shen_absvector_set(shen_get(symdic.symdic_shen_x42prologvectorsx42), KL_ARG_V1306_1240, tco_apply(shen_fillvector, [tco_apply(kl_vector, [10]), 1, 10, symdic.symdic_shen_x45nullx45]))), [setattr(KL_CTX, 'KL_LOC_Counter_1242', shen_absvector_set(shen_get(symdic.symdic_shen_x42varcounterx42), KL_ARG_V1306_1240, 1)), KL_ARG_V1306_1240][(-1)]][(-1)]
shen_add_fun('shen.initialise-prolog', shen_initialisex45prolog, 1)


#============================== track.kl==============================



@tail_recursion
def shen_f_error(KL_ARG_V2062_1243):
    global symdic
    return [tco_apply(shen_prhush, [('partial function ' + tco_apply(shen_app, [KL_ARG_V2062_1243, ';\r\n', symdic.symdic_shen_a])), tco_apply(kl_stoutput, [])]), [(tco_apply(shen_trackx45function, [tco_apply(kl_ps, [KL_ARG_V2062_1243])]) if (tco_apply(kl_yx45orx45nx63, [('track ' + tco_apply(shen_app, [KL_ARG_V2062_1243, '? ', symdic.symdic_shen_a]))]) if (not tco_apply(shen_trackedx63, [KL_ARG_V2062_1243])) else False) else symdic.symdic_shen_ok), shen_simple_error('aborted')][(-1)]][(-1)]
shen_add_fun('shen.f_error', shen_f_error, 1)

@tail_recursion
def shen_trackedx63(KL_ARG_V2063_1244):
    global symdic
    return tail_call(kl_elementx63, [KL_ARG_V2063_1244, shen_get(symdic.symdic_shen_x42trackingx42)])
shen_add_fun('shen.tracked?', shen_trackedx63, 1)

@tail_recursion
def kl_track(KL_ARG_V2064_1245):

    class KL_Context:
        KL_LOC_Source_1246 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Source_1246', tco_apply(kl_ps, [KL_ARG_V2064_1245])), tail_call(shen_trackx45function, [KL_CTX.KL_LOC_Source_1246])][(-1)]
shen_add_fun('track', kl_track, 1)

@tail_recursion
def shen_trackx45function(KL_ARG_V2065_1247):

    class KL_Context:
        KL_LOC_KL_1248 = None
        KL_LOC_Ob_1249 = None
        KL_LOC_Tr_1250 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_KL_1248', [symdic.symdic_kl_defun, [KL_ARG_V2065_1247[1][0], [KL_ARG_V2065_1247[1][1][0], [tco_apply(shen_insertx45trackingx45code, [KL_ARG_V2065_1247[1][0], KL_ARG_V2065_1247[1][1][0], KL_ARG_V2065_1247[1][1][1][0]]), []]]]]), [setattr(KL_CTX, 'KL_LOC_Ob_1249', tco_apply(kl_eval, [KL_CTX.KL_LOC_KL_1248])), [setattr(KL_CTX, 'KL_LOC_Tr_1250', shen_set(symdic.symdic_shen_x42trackingx42, [KL_CTX.KL_LOC_Ob_1249, shen_get(symdic.symdic_shen_x42trackingx42)])), KL_CTX.KL_LOC_Ob_1249][(-1)]][(-1)]][(-1)] if (((((([] == KL_ARG_V2065_1247[1][1][1][1]) if shen_consp(KL_ARG_V2065_1247[1][1][1]) else False) if shen_consp(KL_ARG_V2065_1247[1][1]) else False) if shen_consp(KL_ARG_V2065_1247[1]) else False) if (symdic.symdic_kl_defun == KL_ARG_V2065_1247[0]) else False) if shen_consp(KL_ARG_V2065_1247) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_trackx45function]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.track-function', shen_trackx45function, 1)

@tail_recursion
def shen_insertx45trackingx45code(KL_ARG_V2066_1251, KL_ARG_V2067_1252, KL_ARG_V2068_1253):
    global symdic
    return [symdic.symdic_kl_do, [[symdic.symdic_kl_set, [symdic.symdic_shen_x42callx42, [[symdic.symdic_kl_x43, [[symdic.symdic_kl_value, [symdic.symdic_shen_x42callx42, []]], [1, []]]], []]]], [[symdic.symdic_kl_do, [[symdic.symdic_shen_inputx45track, [[symdic.symdic_kl_value, [symdic.symdic_shen_x42callx42, []]], [KL_ARG_V2066_1251, [tco_apply(shen_cons_form, [KL_ARG_V2067_1252]), []]]]], [[symdic.symdic_kl_do, [[symdic.symdic_shen_terprix45orx45readx45char, []], [[symdic.symdic_kl_let, [symdic.symdic_Result, [KL_ARG_V2068_1253, [[symdic.symdic_kl_do, [[symdic.symdic_shen_outputx45track, [[symdic.symdic_kl_value, [symdic.symdic_shen_x42callx42, []]], [KL_ARG_V2066_1251, [symdic.symdic_Result, []]]]], [[symdic.symdic_kl_do, [[symdic.symdic_kl_set, [symdic.symdic_shen_x42callx42, [[symdic.symdic_kl_x45, [[symdic.symdic_kl_value, [symdic.symdic_shen_x42callx42, []]], [1, []]]], []]]], [[symdic.symdic_kl_do, [[symdic.symdic_shen_terprix45orx45readx45char, []], [symdic.symdic_Result, []]]], []]]], []]]], []]]]], []]]], []]]], []]]]
shen_add_fun('shen.insert-tracking-code', shen_insertx45trackingx45code, 3)
shen_set(symdic.symdic_shen_x42stepx42, False)

@tail_recursion
def kl_step(KL_ARG_V2073_1254):
    global symdic
    return (shen_set(symdic.symdic_shen_x42stepx42, True) if (symdic.symdic_kl_x43 == KL_ARG_V2073_1254) else (shen_set(symdic.symdic_shen_x42stepx42, False) if (symdic.symdic_kl_x45 == KL_ARG_V2073_1254) else (shen_simple_error('step expects a + or a -.\r\n') if True else shen_simple_error('condition failure'))))
shen_add_fun('step', kl_step, 1)

@tail_recursion
def kl_spy(KL_ARG_V2078_1255):
    global symdic
    return (shen_set(symdic.symdic_shen_x42spyx42, True) if (symdic.symdic_kl_x43 == KL_ARG_V2078_1255) else (shen_set(symdic.symdic_shen_x42spyx42, False) if (symdic.symdic_kl_x45 == KL_ARG_V2078_1255) else (shen_simple_error('spy expects a + or a -.\r\n') if True else shen_simple_error('condition failure'))))
shen_add_fun('spy', kl_spy, 1)

@tail_recursion
def shen_terprix45orx45readx45char():
    global symdic
    return (tail_call(shen_checkx45byte, [shen_read_byte(shen_get(symdic.symdic_kl_x42stinputx42))]) if shen_get(symdic.symdic_shen_x42stepx42) else tail_call(kl_nl, [1]))
shen_add_fun('shen.terpri-or-read-char', shen_terprix45orx45readx45char, 0)

@tail_recursion
def shen_checkx45byte(KL_ARG_V2083_1256):
    global symdic
    return (shen_simple_error('aborted') if (KL_ARG_V2083_1256 == tco_apply(shen_hat, [])) else (True if True else shen_simple_error('condition failure')))
shen_add_fun('shen.check-byte', shen_checkx45byte, 1)

@tail_recursion
def shen_inputx45track(KL_ARG_V2084_1257, KL_ARG_V2085_1258, KL_ARG_V2086_1259):
    global symdic
    return [tco_apply(shen_prhush, [('\r\n' + tco_apply(shen_app, [tco_apply(shen_spaces, [KL_ARG_V2084_1257]), ('<' + tco_apply(shen_app, [KL_ARG_V2084_1257, ('> Inputs to ' + tco_apply(shen_app, [KL_ARG_V2085_1258, (' \r\n' + tco_apply(shen_app, [tco_apply(shen_spaces, [KL_ARG_V2084_1257]), '', symdic.symdic_shen_a])), symdic.symdic_shen_a])), symdic.symdic_shen_a])), symdic.symdic_shen_a])), tco_apply(kl_stoutput, [])]), tail_call(shen_recursivelyx45print, [KL_ARG_V2086_1259])][(-1)]
shen_add_fun('shen.input-track', shen_inputx45track, 3)

@tail_recursion
def shen_recursivelyx45print(KL_ARG_V2087_1260):
    global symdic
    return (tail_call(shen_prhush, [' ==>', tco_apply(kl_stoutput, [])]) if ([] == KL_ARG_V2087_1260) else ([tco_apply(kl_print, [KL_ARG_V2087_1260[0]]), [tco_apply(shen_prhush, [', ', tco_apply(kl_stoutput, [])]), tail_call(shen_recursivelyx45print, [KL_ARG_V2087_1260[1]])][(-1)]][(-1)] if shen_consp(KL_ARG_V2087_1260) else (tail_call(shen_sysx45error, [symdic.symdic_shen_recursivelyx45print]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.recursively-print', shen_recursivelyx45print, 1)

@tail_recursion
def shen_spaces(KL_ARG_V2088_1261):
    global symdic
    return ('' if (0 == KL_ARG_V2088_1261) else ((' ' + tco_apply(shen_spaces, [(KL_ARG_V2088_1261 - 1)])) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.spaces', shen_spaces, 1)

@tail_recursion
def shen_outputx45track(KL_ARG_V2089_1262, KL_ARG_V2090_1263, KL_ARG_V2091_1264):
    global symdic
    return tail_call(shen_prhush, [('\r\n' + tco_apply(shen_app, [tco_apply(shen_spaces, [KL_ARG_V2089_1262]), ('<' + tco_apply(shen_app, [KL_ARG_V2089_1262, ('> Output from ' + tco_apply(shen_app, [KL_ARG_V2090_1263, (' \r\n' + tco_apply(shen_app, [tco_apply(shen_spaces, [KL_ARG_V2089_1262]), ('==> ' + tco_apply(shen_app, [KL_ARG_V2091_1264, '', symdic.symdic_shen_s])), symdic.symdic_shen_a])), symdic.symdic_shen_a])), symdic.symdic_shen_a])), symdic.symdic_shen_a])), tco_apply(kl_stoutput, [])])
shen_add_fun('shen.output-track', shen_outputx45track, 3)

@tail_recursion
def kl_untrack(KL_ARG_V2092_1265):
    global symdic
    return tail_call(kl_eval, [tco_apply(kl_ps, [KL_ARG_V2092_1265])])
shen_add_fun('untrack', kl_untrack, 1)

@tail_recursion
def kl_profile(KL_ARG_V2093_1266):
    global symdic
    return tail_call(shen_profilex45help, [tco_apply(kl_ps, [KL_ARG_V2093_1266])])
shen_add_fun('profile', kl_profile, 1)

@tail_recursion
def shen_profilex45help(KL_ARG_V2098_1267):

    class KL_Context:
        KL_LOC_G_1268 = None
        KL_LOC_Profile_1269 = None
        KL_LOC_Def_1270 = None
        KL_LOC_CompileProfile_1271 = None
        KL_LOC_CompileG_1272 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_G_1268', tco_apply(kl_gensym, [symdic.symdic_shen_f])), [setattr(KL_CTX, 'KL_LOC_Profile_1269', [symdic.symdic_kl_defun, [KL_ARG_V2098_1267[1][0], [KL_ARG_V2098_1267[1][1][0], [tco_apply(shen_profilex45func, [KL_ARG_V2098_1267[1][0], KL_ARG_V2098_1267[1][1][0], [KL_CTX.KL_LOC_G_1268, KL_ARG_V2098_1267[1][1][0]]]), []]]]]), [setattr(KL_CTX, 'KL_LOC_Def_1270', [symdic.symdic_kl_defun, [KL_CTX.KL_LOC_G_1268, [KL_ARG_V2098_1267[1][1][0], [tco_apply(kl_subst, [KL_CTX.KL_LOC_G_1268, KL_ARG_V2098_1267[1][0], KL_ARG_V2098_1267[1][1][1][0]]), []]]]]), [setattr(KL_CTX, 'KL_LOC_CompileProfile_1271', tco_apply(shen_evalx45withoutx45macros, [KL_CTX.KL_LOC_Profile_1269])), [setattr(KL_CTX, 'KL_LOC_CompileG_1272', tco_apply(shen_evalx45withoutx45macros, [KL_CTX.KL_LOC_Def_1270])), KL_ARG_V2098_1267[1][0]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)] if (((((([] == KL_ARG_V2098_1267[1][1][1][1]) if shen_consp(KL_ARG_V2098_1267[1][1][1]) else False) if shen_consp(KL_ARG_V2098_1267[1][1]) else False) if shen_consp(KL_ARG_V2098_1267[1]) else False) if (symdic.symdic_kl_defun == KL_ARG_V2098_1267[0]) else False) if shen_consp(KL_ARG_V2098_1267) else False) else (shen_simple_error('Cannot profile.\r\n') if True else shen_simple_error('condition failure')))
shen_add_fun('shen.profile-help', shen_profilex45help, 1)

@tail_recursion
def kl_unprofile(KL_ARG_V2099_1273):
    global symdic
    return tail_call(kl_untrack, [KL_ARG_V2099_1273])
shen_add_fun('unprofile', kl_unprofile, 1)

@tail_recursion
def shen_profilex45func(KL_ARG_V2100_1274, KL_ARG_V2101_1275, KL_ARG_V2102_1276):
    global symdic
    return [symdic.symdic_kl_let, [symdic.symdic_Start, [[symdic.symdic_kl_getx45time, [symdic.symdic_kl_run, []]], [[symdic.symdic_kl_let, [symdic.symdic_Result, [KL_ARG_V2102_1276, [[symdic.symdic_kl_let, [symdic.symdic_Finish, [[symdic.symdic_kl_x45, [[symdic.symdic_kl_getx45time, [symdic.symdic_kl_run, []]], [symdic.symdic_Start, []]]], [[symdic.symdic_kl_let, [symdic.symdic_Record, [[symdic.symdic_shen_putx45profile, [KL_ARG_V2100_1274, [[symdic.symdic_kl_x43, [[symdic.symdic_shen_getx45profile, [KL_ARG_V2100_1274, []]], [symdic.symdic_Finish, []]]], []]]], [symdic.symdic_Result, []]]]], []]]]], []]]]], []]]]]
shen_add_fun('shen.profile-func', shen_profilex45func, 3)

@tail_recursion
def kl_profilex45results(KL_ARG_V2103_1277):

    class KL_Context:
        KL_LOC_Results_1278 = None
        KL_LOC_Initialise_1279 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Results_1278', tco_apply(shen_getx45profile, [KL_ARG_V2103_1277])), [setattr(KL_CTX, 'KL_LOC_Initialise_1279', tco_apply(shen_putx45profile, [KL_ARG_V2103_1277, 0])), tail_call(kl_x64p, [KL_ARG_V2103_1277, KL_CTX.KL_LOC_Results_1278])][(-1)]][(-1)]
shen_add_fun('profile-results', kl_profilex45results, 1)

@tail_recursion
def shen_getx45profile(KL_ARG_V2104_1280):
    global symdic
    return shen_try_except((lambda : tco_apply(kl_get, [KL_ARG_V2104_1280, symdic.symdic_kl_profile, shen_get(symdic.symdic_kl_x42propertyx45vectorx42)])), (lambda KL_ARG_E_1281: 0))
shen_add_fun('shen.get-profile', shen_getx45profile, 1)

@tail_recursion
def shen_putx45profile(KL_ARG_V2105_1282, KL_ARG_V2106_1283):
    global symdic
    return tail_call(kl_put, [KL_ARG_V2105_1282, symdic.symdic_kl_profile, KL_ARG_V2106_1283, shen_get(symdic.symdic_kl_x42propertyx45vectorx42)])
shen_add_fun('shen.put-profile', shen_putx45profile, 2)


#============================== load.kl==============================



@tail_recursion
def kl_load(KL_ARG_V829_1284):

    class KL_Context:
        KL_LOC_Load_1285 = None
        KL_LOC_Start_1286 = None
        KL_LOC_Result_1287 = None
        KL_LOC_Finish_1288 = None
        KL_LOC_Time_1289 = None
        KL_LOC_Message_1290 = None
        KL_LOC_Infs_1291 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Load_1285', [setattr(KL_CTX, 'KL_LOC_Start_1286', shen_get_time(symdic.symdic_kl_run)), [setattr(KL_CTX, 'KL_LOC_Result_1287', tco_apply(shen_loadx45help, [shen_get(symdic.symdic_shen_x42tcx42), tco_apply(kl_readx45file, [KL_ARG_V829_1284])])), [setattr(KL_CTX, 'KL_LOC_Finish_1288', shen_get_time(symdic.symdic_kl_run)), [setattr(KL_CTX, 'KL_LOC_Time_1289', (KL_CTX.KL_LOC_Finish_1288 - KL_CTX.KL_LOC_Start_1286)), [setattr(KL_CTX, 'KL_LOC_Message_1290', tco_apply(shen_prhush, [('\r\nrun time: ' + (str(KL_CTX.KL_LOC_Time_1289) + ' secs\r\n')), tco_apply(kl_stoutput, [])])), KL_CTX.KL_LOC_Result_1287][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]), [setattr(KL_CTX, 'KL_LOC_Infs_1291', (tco_apply(shen_prhush, [('\r\ntypechecked in ' + tco_apply(shen_app, [tco_apply(kl_inferences, []), ' inferences\r\n', symdic.symdic_shen_a])), tco_apply(kl_stoutput, [])]) if shen_get(symdic.symdic_shen_x42tcx42) else symdic.symdic_shen_skip)), symdic.symdic_kl_loaded][(-1)]][(-1)]
shen_add_fun('load', kl_load, 1)

@tail_recursion
def shen_loadx45help(KL_ARG_V834_1292, KL_ARG_V835_1293):

    class KL_Context:
        KL_LOC_RemoveSynonyms_1295 = None
        KL_LOC_Table_1296 = None
        KL_LOC_Assume_1297 = None
    KL_CTX = KL_Context()
    global symdic
    return (tail_call(kl_map, [(lambda KL_ARG_X_1294: tail_call(shen_prhush, [tco_apply(shen_app, [tco_apply(shen_evalx45withoutx45macros, [KL_ARG_X_1294]), '\r\n', symdic.symdic_shen_s]), tco_apply(kl_stoutput, [])])), KL_ARG_V835_1293]) if (False == KL_ARG_V834_1292) else ([setattr(KL_CTX, 'KL_LOC_RemoveSynonyms_1295', tco_apply(kl_mapcan, [symdic.symdic_shen_removex45synonyms, KL_ARG_V835_1293])), [setattr(KL_CTX, 'KL_LOC_Table_1296', tco_apply(kl_mapcan, [symdic.symdic_shen_typetable, KL_CTX.KL_LOC_RemoveSynonyms_1295])), [setattr(KL_CTX, 'KL_LOC_Assume_1297', tco_apply(kl_map, [symdic.symdic_shen_assumetype, KL_CTX.KL_LOC_Table_1296])), shen_try_except((lambda : tco_apply(kl_map, [symdic.symdic_shen_typecheckx45andx45load, KL_CTX.KL_LOC_RemoveSynonyms_1295])), (lambda KL_ARG_E_1298: tail_call(shen_unwindx45types, [KL_ARG_E_1298, KL_CTX.KL_LOC_Table_1296])))][(-1)]][(-1)]][(-1)] if True else shen_simple_error('condition failure')))
shen_add_fun('shen.load-help', shen_loadx45help, 2)

@tail_recursion
def shen_removex45synonyms(KL_ARG_V836_1299):
    global symdic
    return ([tco_apply(kl_eval, [KL_ARG_V836_1299]), []][(-1)] if ((symdic.symdic_shen_synonymsx45help == KL_ARG_V836_1299[0]) if shen_consp(KL_ARG_V836_1299) else False) else ([KL_ARG_V836_1299, []] if True else shen_simple_error('condition failure')))
shen_add_fun('shen.remove-synonyms', shen_removex45synonyms, 1)

@tail_recursion
def shen_typecheckx45andx45load(KL_ARG_V837_1300):
    global symdic
    return [tco_apply(kl_nl, [1]), tail_call(shen_typecheckx45andx45evaluate, [KL_ARG_V837_1300, tco_apply(kl_gensym, [symdic.symdic_A])])][(-1)]
shen_add_fun('shen.typecheck-and-load', shen_typecheckx45andx45load, 1)

@tail_recursion
def shen_typetable(KL_ARG_V846_1301):

    class KL_Context:
        KL_LOC_Sig_1302 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_Sig_1302', tco_apply(kl_compile, [symdic.symdic_shen_x60sigx43restx62, KL_ARG_V846_1301[1][1], []])), (shen_simple_error(tco_apply(shen_app, [KL_ARG_V846_1301[1][0], ' lacks a proper signature.\r\n', symdic.symdic_shen_a])) if (KL_CTX.KL_LOC_Sig_1302 == tco_apply(kl_fail, [])) else [[KL_ARG_V846_1301[1][0], KL_CTX.KL_LOC_Sig_1302], []])][(-1)] if ((shen_consp(KL_ARG_V846_1301[1]) if (symdic.symdic_kl_define == KL_ARG_V846_1301[0]) else False) if shen_consp(KL_ARG_V846_1301) else False) else ([[KL_ARG_V846_1301[1][0], [KL_ARG_V846_1301[1][1][1][0], [symdic.symdic_kl_x61x61x62, [KL_ARG_V846_1301[1][1][1][1][1][0], []]]]], []] if (((((((((((((((symdic.symdic_kl_x125 == KL_ARG_V846_1301[1][1][1][1][1][1][0]) if shen_consp(KL_ARG_V846_1301[1][1][1][1][1][1]) else False) if shen_consp(KL_ARG_V846_1301[1][1][1][1][1]) else False) if (symdic.symdic_kl_x61x61x62 == KL_ARG_V846_1301[1][1][1][1][0]) else False) if shen_consp(KL_ARG_V846_1301[1][1][1][1]) else False) if ([] == KL_ARG_V846_1301[1][1][1][0][1][1]) else False) if shen_consp(KL_ARG_V846_1301[1][1][1][0][1]) else False) if (symdic.symdic_kl_list == KL_ARG_V846_1301[1][1][1][0][0]) else False) if shen_consp(KL_ARG_V846_1301[1][1][1][0]) else False) if shen_consp(KL_ARG_V846_1301[1][1][1]) else False) if (symdic.symdic_kl_x123 == KL_ARG_V846_1301[1][1][0]) else False) if shen_consp(KL_ARG_V846_1301[1][1]) else False) if shen_consp(KL_ARG_V846_1301[1]) else False) if (symdic.symdic_kl_defcc == KL_ARG_V846_1301[0]) else False) if shen_consp(KL_ARG_V846_1301) else False) else (shen_simple_error(tco_apply(shen_app, [KL_ARG_V846_1301[1][0], ' lacks a proper signature.\r\n', symdic.symdic_shen_a])) if ((shen_consp(KL_ARG_V846_1301[1]) if (symdic.symdic_kl_defcc == KL_ARG_V846_1301[0]) else False) if shen_consp(KL_ARG_V846_1301) else False) else ([] if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.typetable', shen_typetable, 1)

@tail_recursion
def shen_assumetype(KL_ARG_V847_1303):
    global symdic
    return (apply(kl_declare, [KL_ARG_V847_1303[0], KL_ARG_V847_1303[1]]) if shen_consp(KL_ARG_V847_1303) else (tail_call(shen_sysx45error, [symdic.symdic_shen_assumetype]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.assumetype', shen_assumetype, 1)

@tail_recursion
def shen_unwindx45types(KL_ARG_V852_1304, KL_ARG_V853_1305):
    global symdic
    return (shen_simple_error(KL_ARG_V852_1304.message) if ([] == KL_ARG_V853_1305) else ([tco_apply(shen_remtype, [KL_ARG_V853_1305[0][0]]), tail_call(shen_unwindx45types, [KL_ARG_V852_1304, KL_ARG_V853_1305[1]])][(-1)] if (shen_consp(KL_ARG_V853_1305[0]) if shen_consp(KL_ARG_V853_1305) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_unwindx45types]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.unwind-types', shen_unwindx45types, 2)

@tail_recursion
def shen_remtype(KL_ARG_V854_1306):
    global symdic
    return shen_set(symdic.symdic_shen_x42signedfuncsx42, tco_apply(shen_removetype, [KL_ARG_V854_1306, shen_get(symdic.symdic_shen_x42signedfuncsx42)]))
shen_add_fun('shen.remtype', shen_remtype, 1)

@tail_recursion
def shen_removetype(KL_ARG_V859_1307, KL_ARG_V860_1308):
    global symdic
    return ([] if ([] == KL_ARG_V860_1308) else (tail_call(shen_removetype, [KL_ARG_V860_1308[0][0], KL_ARG_V860_1308[1]]) if (((KL_ARG_V860_1308[0][0] == KL_ARG_V859_1307) if shen_consp(KL_ARG_V860_1308[0]) else False) if shen_consp(KL_ARG_V860_1308) else False) else ([KL_ARG_V860_1308[0], tco_apply(shen_removetype, [KL_ARG_V859_1307, KL_ARG_V860_1308[1]])] if shen_consp(KL_ARG_V860_1308) else (tail_call(shen_sysx45error, [symdic.symdic_shen_removetype]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.removetype', shen_removetype, 2)

@tail_recursion
def shen_x60sigx43restx62(KL_ARG_V866_1309):

    class KL_Context:
        KL_LOC_Result_1310 = None
        KL_LOC_Parse_shen_x60signaturex62_1311 = None
        KL_LOC_Parse_x60x33x62_1312 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_1310', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60signaturex62_1311', tco_apply(shen_x60signaturex62, [KL_ARG_V866_1309])), ([setattr(KL_CTX, 'KL_LOC_Parse_x60x33x62_1312', tco_apply(x60x33x62, [KL_CTX.KL_LOC_Parse_shen_x60signaturex62_1311])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_x60x33x62_1312[0], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60signaturex62_1311])]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_x60x33x62_1312)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60signaturex62_1311)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_1310 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_1310)][(-1)]
shen_add_fun('shen.<sig+rest>', shen_x60sigx43restx62, 1)

@tail_recursion
def kl_writex45tox45file(KL_ARG_V867_1313, KL_ARG_V868_1314):

    class KL_Context:
        KL_LOC_Stream_1315 = None
        KL_LOC_String_1316 = None
        KL_LOC_Write_1317 = None
        KL_LOC_Close_1318 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Stream_1315', shen_open(symdic.symdic_kl_file, KL_ARG_V867_1313, symdic.symdic_kl_out)), [setattr(KL_CTX, 'KL_LOC_String_1316', (tco_apply(shen_app, [KL_ARG_V868_1314, '\r\n\r\n', symdic.symdic_shen_a]) if isinstance(KL_ARG_V868_1314, str) else tco_apply(shen_app, [KL_ARG_V868_1314, '\r\n\r\n', symdic.symdic_shen_s]))), [setattr(KL_CTX, 'KL_LOC_Write_1317', shen_pr(KL_CTX.KL_LOC_String_1316, KL_CTX.KL_LOC_Stream_1315)), [setattr(KL_CTX, 'KL_LOC_Close_1318', shen_close(KL_CTX.KL_LOC_Stream_1315)), KL_ARG_V868_1314][(-1)]][(-1)]][(-1)]][(-1)]
shen_add_fun('write-to-file', kl_writex45tox45file, 2)


#============================== writer.kl==============================



@tail_recursion
def kl_print(KL_ARG_V2210_1319):

    class KL_Context:
        KL_LOC_String_1320 = None
        KL_LOC_Print_1321 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_String_1320', tco_apply(shen_insert, [KL_ARG_V2210_1319, '~S'])), [setattr(KL_CTX, 'KL_LOC_Print_1321', tco_apply(shen_prhush, [KL_CTX.KL_LOC_String_1320, tco_apply(kl_stoutput, [])])), KL_ARG_V2210_1319][(-1)]][(-1)]
shen_add_fun('print', kl_print, 1)

@tail_recursion
def shen_prhush(KL_ARG_V2211_1322, KL_ARG_V2212_1323):
    global symdic
    return (KL_ARG_V2211_1322 if shen_get(symdic.symdic_x42hushx42) else shen_pr(KL_ARG_V2211_1322, KL_ARG_V2212_1323))
shen_add_fun('shen.prhush', shen_prhush, 2)

@tail_recursion
def shen_mkstr(KL_ARG_V2213_1324, KL_ARG_V2214_1325):
    global symdic
    return (tail_call(shen_mkstrx45l, [tco_apply(shen_procx45nl, [KL_ARG_V2213_1324]), KL_ARG_V2214_1325]) if isinstance(KL_ARG_V2213_1324, str) else (tail_call(shen_mkstrx45r, [[symdic.symdic_shen_procx45nl, [KL_ARG_V2213_1324, []]], KL_ARG_V2214_1325]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.mkstr', shen_mkstr, 2)

@tail_recursion
def shen_mkstrx45l(KL_ARG_V2215_1326, KL_ARG_V2216_1327):
    global symdic
    return (KL_ARG_V2215_1326 if ([] == KL_ARG_V2216_1327) else (tail_call(shen_mkstrx45l, [tco_apply(shen_insertx45l, [KL_ARG_V2216_1327[0], KL_ARG_V2215_1326]), KL_ARG_V2216_1327[1]]) if shen_consp(KL_ARG_V2216_1327) else (tail_call(shen_sysx45error, [symdic.symdic_shen_mkstrx45l]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.mkstr-l', shen_mkstrx45l, 2)

@tail_recursion
def shen_insertx45l(KL_ARG_V2219_1328, KL_ARG_V2220_1329):
    global symdic
    return ('' if ('' == KL_ARG_V2220_1329) else ([symdic.symdic_shen_app, [KL_ARG_V2219_1328, [KL_ARG_V2220_1329[1:][1:], [symdic.symdic_shen_a, []]]]] if (((('A' == KL_ARG_V2220_1329[1:][0]) if tco_apply(shen_x43stringx63, [KL_ARG_V2220_1329[1:]]) else False) if ('~' == KL_ARG_V2220_1329[0]) else False) if tco_apply(shen_x43stringx63, [KL_ARG_V2220_1329]) else False) else ([symdic.symdic_shen_app, [KL_ARG_V2219_1328, [KL_ARG_V2220_1329[1:][1:], [symdic.symdic_shen_r, []]]]] if (((('R' == KL_ARG_V2220_1329[1:][0]) if tco_apply(shen_x43stringx63, [KL_ARG_V2220_1329[1:]]) else False) if ('~' == KL_ARG_V2220_1329[0]) else False) if tco_apply(shen_x43stringx63, [KL_ARG_V2220_1329]) else False) else ([symdic.symdic_shen_app, [KL_ARG_V2219_1328, [KL_ARG_V2220_1329[1:][1:], [symdic.symdic_shen_s, []]]]] if (((('S' == KL_ARG_V2220_1329[1:][0]) if tco_apply(shen_x43stringx63, [KL_ARG_V2220_1329[1:]]) else False) if ('~' == KL_ARG_V2220_1329[0]) else False) if tco_apply(shen_x43stringx63, [KL_ARG_V2220_1329]) else False) else (tail_call(shen_factorx45cn, [[symdic.symdic_kl_cn, [KL_ARG_V2220_1329[0], [tco_apply(shen_insertx45l, [KL_ARG_V2219_1328, KL_ARG_V2220_1329[1:]]), []]]]]) if tco_apply(shen_x43stringx63, [KL_ARG_V2220_1329]) else ([symdic.symdic_kl_cn, [KL_ARG_V2220_1329[1][0], [tco_apply(shen_insertx45l, [KL_ARG_V2219_1328, KL_ARG_V2220_1329[1][1][0]]), []]]] if ((((([] == KL_ARG_V2220_1329[1][1][1]) if shen_consp(KL_ARG_V2220_1329[1][1]) else False) if shen_consp(KL_ARG_V2220_1329[1]) else False) if (symdic.symdic_kl_cn == KL_ARG_V2220_1329[0]) else False) if shen_consp(KL_ARG_V2220_1329) else False) else ([symdic.symdic_shen_app, [KL_ARG_V2220_1329[1][0], [tco_apply(shen_insertx45l, [KL_ARG_V2219_1328, KL_ARG_V2220_1329[1][1][0]]), KL_ARG_V2220_1329[1][1][1]]]] if (((((([] == KL_ARG_V2220_1329[1][1][1][1]) if shen_consp(KL_ARG_V2220_1329[1][1][1]) else False) if shen_consp(KL_ARG_V2220_1329[1][1]) else False) if shen_consp(KL_ARG_V2220_1329[1]) else False) if (symdic.symdic_shen_app == KL_ARG_V2220_1329[0]) else False) if shen_consp(KL_ARG_V2220_1329) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_insertx45l]) if True else shen_simple_error('condition failure')))))))))
shen_add_fun('shen.insert-l', shen_insertx45l, 2)

@tail_recursion
def shen_factorx45cn(KL_ARG_V2221_1330):
    global symdic
    return ([symdic.symdic_kl_cn, [(KL_ARG_V2221_1330[1][0] + KL_ARG_V2221_1330[1][1][0][1][0]), KL_ARG_V2221_1330[1][1][0][1][1]]] if (((((((((((isinstance(KL_ARG_V2221_1330[1][1][0][1][0], str) if isinstance(KL_ARG_V2221_1330[1][0], str) else False) if ([] == KL_ARG_V2221_1330[1][1][1]) else False) if ([] == KL_ARG_V2221_1330[1][1][0][1][1][1]) else False) if shen_consp(KL_ARG_V2221_1330[1][1][0][1][1]) else False) if shen_consp(KL_ARG_V2221_1330[1][1][0][1]) else False) if (symdic.symdic_kl_cn == KL_ARG_V2221_1330[1][1][0][0]) else False) if shen_consp(KL_ARG_V2221_1330[1][1][0]) else False) if shen_consp(KL_ARG_V2221_1330[1][1]) else False) if shen_consp(KL_ARG_V2221_1330[1]) else False) if (symdic.symdic_kl_cn == KL_ARG_V2221_1330[0]) else False) if shen_consp(KL_ARG_V2221_1330) else False) else (KL_ARG_V2221_1330 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.factor-cn', shen_factorx45cn, 1)

@tail_recursion
def shen_procx45nl(KL_ARG_V2222_1331):
    global symdic
    return ('' if ('' == KL_ARG_V2222_1331) else ((chr(10) + tco_apply(shen_procx45nl, [KL_ARG_V2222_1331[1:][1:]])) if (((('%' == KL_ARG_V2222_1331[1:][0]) if tco_apply(shen_x43stringx63, [KL_ARG_V2222_1331[1:]]) else False) if ('~' == KL_ARG_V2222_1331[0]) else False) if tco_apply(shen_x43stringx63, [KL_ARG_V2222_1331]) else False) else ((KL_ARG_V2222_1331[0] + tco_apply(shen_procx45nl, [KL_ARG_V2222_1331[1:]])) if tco_apply(shen_x43stringx63, [KL_ARG_V2222_1331]) else (tail_call(shen_sysx45error, [symdic.symdic_shen_procx45nl]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.proc-nl', shen_procx45nl, 1)

@tail_recursion
def shen_mkstrx45r(KL_ARG_V2223_1332, KL_ARG_V2224_1333):
    global symdic
    return (KL_ARG_V2223_1332 if ([] == KL_ARG_V2224_1333) else (tail_call(shen_mkstrx45r, [[symdic.symdic_shen_insert, [KL_ARG_V2224_1333[0], [KL_ARG_V2223_1332, []]]], KL_ARG_V2224_1333[1]]) if shen_consp(KL_ARG_V2224_1333) else (tail_call(shen_sysx45error, [symdic.symdic_shen_mkstrx45r]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.mkstr-r', shen_mkstrx45r, 2)

@tail_recursion
def shen_insert(KL_ARG_V2225_1334, KL_ARG_V2226_1335):
    global symdic
    return tail_call(shen_insertx45h, [KL_ARG_V2225_1334, KL_ARG_V2226_1335, ''])
shen_add_fun('shen.insert', shen_insert, 2)

@tail_recursion
def shen_insertx45h(KL_ARG_V2229_1336, KL_ARG_V2230_1337, KL_ARG_V2231_1338):
    global symdic
    return (KL_ARG_V2231_1338 if ('' == KL_ARG_V2230_1337) else ((KL_ARG_V2231_1338 + tco_apply(shen_app, [KL_ARG_V2229_1336, KL_ARG_V2230_1337[1:][1:], symdic.symdic_shen_a])) if (((('A' == KL_ARG_V2230_1337[1:][0]) if tco_apply(shen_x43stringx63, [KL_ARG_V2230_1337[1:]]) else False) if ('~' == KL_ARG_V2230_1337[0]) else False) if tco_apply(shen_x43stringx63, [KL_ARG_V2230_1337]) else False) else ((KL_ARG_V2231_1338 + tco_apply(shen_app, [KL_ARG_V2229_1336, KL_ARG_V2230_1337[1:][1:], symdic.symdic_shen_r])) if (((('R' == KL_ARG_V2230_1337[1:][0]) if tco_apply(shen_x43stringx63, [KL_ARG_V2230_1337[1:]]) else False) if ('~' == KL_ARG_V2230_1337[0]) else False) if tco_apply(shen_x43stringx63, [KL_ARG_V2230_1337]) else False) else ((KL_ARG_V2231_1338 + tco_apply(shen_app, [KL_ARG_V2229_1336, KL_ARG_V2230_1337[1:][1:], symdic.symdic_shen_s])) if (((('S' == KL_ARG_V2230_1337[1:][0]) if tco_apply(shen_x43stringx63, [KL_ARG_V2230_1337[1:]]) else False) if ('~' == KL_ARG_V2230_1337[0]) else False) if tco_apply(shen_x43stringx63, [KL_ARG_V2230_1337]) else False) else (tail_call(shen_insertx45h, [KL_ARG_V2229_1336, KL_ARG_V2230_1337[1:], (KL_ARG_V2231_1338 + KL_ARG_V2230_1337[0])]) if tco_apply(shen_x43stringx63, [KL_ARG_V2230_1337]) else (tail_call(shen_sysx45error, [symdic.symdic_shen_insertx45h]) if True else shen_simple_error('condition failure')))))))
shen_add_fun('shen.insert-h', shen_insertx45h, 3)

@tail_recursion
def shen_app(KL_ARG_V2232_1339, KL_ARG_V2233_1340, KL_ARG_V2234_1341):
    global symdic
    return (tco_apply(shen_argx45x62str, [KL_ARG_V2232_1339, KL_ARG_V2234_1341]) + KL_ARG_V2233_1340)
shen_add_fun('shen.app', shen_app, 3)

@tail_recursion
def shen_argx45x62str(KL_ARG_V2240_1342, KL_ARG_V2241_1343):
    global symdic
    return ('...' if (KL_ARG_V2240_1342 == tco_apply(kl_fail, [])) else (tail_call(shen_listx45x62str, [KL_ARG_V2240_1342, KL_ARG_V2241_1343]) if tco_apply(shen_listx63, [KL_ARG_V2240_1342]) else (tail_call(shen_strx45x62str, [KL_ARG_V2240_1342, KL_ARG_V2241_1343]) if isinstance(KL_ARG_V2240_1342, str) else (tail_call(shen_vectorx45x62str, [KL_ARG_V2240_1342, KL_ARG_V2241_1343]) if shen_absvectorp(KL_ARG_V2240_1342) else (tail_call(shen_atomx45x62str, [KL_ARG_V2240_1342]) if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.arg->str', shen_argx45x62str, 2)

@tail_recursion
def shen_listx45x62str(KL_ARG_V2242_1344, KL_ARG_V2243_1345):
    global symdic
    return (tail_call(kl_x64s, ['(', tco_apply(kl_x64s, [tco_apply(shen_iterx45list, [KL_ARG_V2242_1344, symdic.symdic_shen_r, tco_apply(shen_maxseq, [])]), ')'])]) if (symdic.symdic_shen_r == KL_ARG_V2243_1345) else (tail_call(kl_x64s, ['[', tco_apply(kl_x64s, [tco_apply(shen_iterx45list, [KL_ARG_V2242_1344, KL_ARG_V2243_1345, tco_apply(shen_maxseq, [])]), ']'])]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.list->str', shen_listx45x62str, 2)

@tail_recursion
def shen_maxseq():
    global symdic
    return shen_get(symdic.symdic_kl_x42maximumx45printx45sequencex45sizex42)
shen_add_fun('shen.maxseq', shen_maxseq, 0)

@tail_recursion
def shen_iterx45list(KL_ARG_V2254_1346, KL_ARG_V2255_1347, KL_ARG_V2256_1348):
    global symdic
    return ('' if ([] == KL_ARG_V2254_1346) else ('... etc' if (0 == KL_ARG_V2256_1348) else (tail_call(shen_argx45x62str, [KL_ARG_V2254_1346[0], KL_ARG_V2255_1347]) if (([] == KL_ARG_V2254_1346[1]) if shen_consp(KL_ARG_V2254_1346) else False) else (tail_call(kl_x64s, [tco_apply(shen_argx45x62str, [KL_ARG_V2254_1346[0], KL_ARG_V2255_1347]), tco_apply(kl_x64s, [' ', tco_apply(shen_iterx45list, [KL_ARG_V2254_1346[1], KL_ARG_V2255_1347, (KL_ARG_V2256_1348 - 1)])])]) if shen_consp(KL_ARG_V2254_1346) else (tail_call(kl_x64s, ['|', tco_apply(kl_x64s, [' ', tco_apply(shen_argx45x62str, [KL_ARG_V2254_1346, KL_ARG_V2255_1347])])]) if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.iter-list', shen_iterx45list, 3)

@tail_recursion
def shen_strx45x62str(KL_ARG_V2261_1349, KL_ARG_V2262_1350):
    global symdic
    return (KL_ARG_V2261_1349 if (symdic.symdic_shen_a == KL_ARG_V2262_1350) else (tail_call(kl_x64s, [chr(34), tco_apply(kl_x64s, [KL_ARG_V2261_1349, chr(34)])]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.str->str', shen_strx45x62str, 2)

@tail_recursion
def shen_vectorx45x62str(KL_ARG_V2263_1351, KL_ARG_V2264_1352):
    global symdic
    return (tail_call(shen_absvector_get(KL_ARG_V2263_1351, 0), [KL_ARG_V2263_1351]) if tco_apply(shen_printx45vectorx63, [KL_ARG_V2263_1351]) else (tail_call(kl_x64s, ['<', tco_apply(kl_x64s, [tco_apply(shen_iterx45vector, [KL_ARG_V2263_1351, 1, KL_ARG_V2264_1352, tco_apply(shen_maxseq, [])]), '>'])]) if tco_apply(kl_vectorx63, [KL_ARG_V2263_1351]) else tail_call(kl_x64s, ['<', tco_apply(kl_x64s, ['<', tco_apply(kl_x64s, [tco_apply(shen_iterx45vector, [KL_ARG_V2263_1351, 0, KL_ARG_V2264_1352, tco_apply(shen_maxseq, [])]), '>>'])])])))
shen_add_fun('shen.vector->str', shen_vectorx45x62str, 2)

@tail_recursion
def shen_printx45vectorx63(KL_ARG_V2265_1353):

    class KL_Context:
        KL_LOC_Zero_1354 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Zero_1354', shen_absvector_get(KL_ARG_V2265_1353, 0)), (True if (KL_CTX.KL_LOC_Zero_1354 == symdic.symdic_shen_tuple) else (True if (KL_CTX.KL_LOC_Zero_1354 == symdic.symdic_shen_pvar) else (tail_call(shen_fboundx63, [KL_CTX.KL_LOC_Zero_1354]) if (not isinstance(KL_CTX.KL_LOC_Zero_1354, numbers.Number)) else False)))][(-1)]
shen_add_fun('shen.print-vector?', shen_printx45vectorx63, 1)

@tail_recursion
def shen_fboundx63(KL_ARG_V2266_1355):
    global symdic
    return shen_try_except((lambda : [tco_apply(kl_ps, [KL_ARG_V2266_1355]), True][(-1)]), (lambda KL_ARG_E_1356: False))
shen_add_fun('shen.fbound?', shen_fboundx63, 1)

@tail_recursion
def shen_tuple(KL_ARG_V2267_1357):
    global symdic
    return ('(@p ' + tco_apply(shen_app, [shen_absvector_get(KL_ARG_V2267_1357, 1), (' ' + tco_apply(shen_app, [shen_absvector_get(KL_ARG_V2267_1357, 2), ')', symdic.symdic_shen_s])), symdic.symdic_shen_s]))
shen_add_fun('shen.tuple', shen_tuple, 1)

@tail_recursion
def shen_iterx45vector(KL_ARG_V2274_1358, KL_ARG_V2275_1359, KL_ARG_V2276_1360, KL_ARG_V2277_1361):

    class KL_Context:
        KL_LOC_Item_1362 = None
        KL_LOC_Next_1364 = None
    KL_CTX = KL_Context()
    global symdic
    return ('... etc' if (0 == KL_ARG_V2277_1361) else ([setattr(KL_CTX, 'KL_LOC_Item_1362', shen_try_except((lambda : shen_absvector_get(KL_ARG_V2274_1358, KL_ARG_V2275_1359)), (lambda KL_ARG_E_1363: symdic.symdic_shen_outx45ofx45bounds))), [setattr(KL_CTX, 'KL_LOC_Next_1364', shen_try_except((lambda : shen_absvector_get(KL_ARG_V2274_1358, (KL_ARG_V2275_1359 + 1))), (lambda KL_ARG_E_1365: symdic.symdic_shen_outx45ofx45bounds))), ('' if (KL_CTX.KL_LOC_Item_1362 == symdic.symdic_shen_outx45ofx45bounds) else (tail_call(shen_argx45x62str, [KL_CTX.KL_LOC_Item_1362, KL_ARG_V2276_1360]) if (KL_CTX.KL_LOC_Next_1364 == symdic.symdic_shen_outx45ofx45bounds) else tail_call(kl_x64s, [tco_apply(shen_argx45x62str, [KL_CTX.KL_LOC_Item_1362, KL_ARG_V2276_1360]), tco_apply(kl_x64s, [' ', tco_apply(shen_iterx45vector, [KL_ARG_V2274_1358, (KL_ARG_V2275_1359 + 1), KL_ARG_V2276_1360, (KL_ARG_V2277_1361 - 1)])])])))][(-1)]][(-1)] if True else shen_simple_error('condition failure')))
shen_add_fun('shen.iter-vector', shen_iterx45vector, 4)

@tail_recursion
def shen_atomx45x62str(KL_ARG_V2278_1366):
    global symdic
    return shen_try_except((lambda : str(KL_ARG_V2278_1366)), (lambda KL_ARG_E_1367: tail_call(shen_funexstring, [])))
shen_add_fun('shen.atom->str', shen_atomx45x62str, 1)

@tail_recursion
def shen_funexstring():
    global symdic
    return tail_call(kl_x64s, ['\x10', tco_apply(kl_x64s, ['f', tco_apply(kl_x64s, ['u', tco_apply(kl_x64s, ['n', tco_apply(kl_x64s, ['e', tco_apply(kl_x64s, [tco_apply(shen_argx45x62str, [tco_apply(kl_gensym, [shen_intern('x')]), symdic.symdic_shen_a]), '\x11'])])])])])])
shen_add_fun('shen.funexstring', shen_funexstring, 0)

@tail_recursion
def shen_listx63(KL_ARG_V2279_1368):
    global symdic
    return (True if tco_apply(kl_emptyx63, [KL_ARG_V2279_1368]) else shen_consp(KL_ARG_V2279_1368))
shen_add_fun('shen.list?', shen_listx63, 1)


#============================== macros.kl==============================



@tail_recursion
def kl_macroexpand(KL_ARG_V870_1369):

    class KL_Context:
        KL_LOC_Y_1370 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Y_1370', tco_apply(shen_compose, [shen_get(symdic.symdic_kl_x42macrosx42), KL_ARG_V870_1369])), (KL_ARG_V870_1369 if (KL_ARG_V870_1369 == KL_CTX.KL_LOC_Y_1370) else tail_call(shen_walk, [(lambda KL_ARG_V869_1371: tail_call(kl_macroexpand, [KL_ARG_V869_1371])), KL_CTX.KL_LOC_Y_1370]))][(-1)]
shen_add_fun('macroexpand', kl_macroexpand, 1)
shen_set(symdic.symdic_kl_x42macrosx42, [symdic.symdic_shen_timerx45macro, [symdic.symdic_shen_casesx45macro, [symdic.symdic_shen_absx45macro, [symdic.symdic_shen_putx47getx45macro, [symdic.symdic_shen_compilex45macro, [symdic.symdic_shen_datatypex45macro, [symdic.symdic_shen_letx45macro, [symdic.symdic_shen_assocx45macro, [symdic.symdic_shen_makex45stringx45macro, [symdic.symdic_shen_outputx45macro, [symdic.symdic_shen_errorx45macro, [symdic.symdic_shen_prologx45macro, [symdic.symdic_shen_synonymsx45macro, [symdic.symdic_shen_nlx45macro, [symdic.symdic_shen_x64sx45macro, [symdic.symdic_shen_defprologx45macro, [symdic.symdic_shen_functionx45macro, []]]]]]]]]]]]]]]]]])

@tail_recursion
def shen_errorx45macro(KL_ARG_V871_1372):
    global symdic
    return ([symdic.symdic_kl_simplex45error, [tco_apply(shen_mkstr, [KL_ARG_V871_1372[1][0], KL_ARG_V871_1372[1][1]]), []]] if ((shen_consp(KL_ARG_V871_1372[1]) if (symdic.symdic_kl_error == KL_ARG_V871_1372[0]) else False) if shen_consp(KL_ARG_V871_1372) else False) else (KL_ARG_V871_1372 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.error-macro', shen_errorx45macro, 1)

@tail_recursion
def shen_outputx45macro(KL_ARG_V872_1373):
    global symdic
    return ([symdic.symdic_shen_prhush, [tco_apply(shen_mkstr, [KL_ARG_V872_1373[1][0], KL_ARG_V872_1373[1][1]]), [[symdic.symdic_kl_stoutput, []], []]]] if ((shen_consp(KL_ARG_V872_1373[1]) if (symdic.symdic_kl_output == KL_ARG_V872_1373[0]) else False) if shen_consp(KL_ARG_V872_1373) else False) else (KL_ARG_V872_1373 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.output-macro', shen_outputx45macro, 1)

@tail_recursion
def shen_makex45stringx45macro(KL_ARG_V873_1374):
    global symdic
    return (tail_call(shen_mkstr, [KL_ARG_V873_1374[1][0], KL_ARG_V873_1374[1][1]]) if ((shen_consp(KL_ARG_V873_1374[1]) if (symdic.symdic_kl_makex45string == KL_ARG_V873_1374[0]) else False) if shen_consp(KL_ARG_V873_1374) else False) else (KL_ARG_V873_1374 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.make-string-macro', shen_makex45stringx45macro, 1)

@tail_recursion
def shen_compose(KL_ARG_V874_1375, KL_ARG_V875_1376):
    global symdic
    return (KL_ARG_V875_1376 if ([] == KL_ARG_V874_1375) else (tail_call(shen_compose, [KL_ARG_V874_1375[1], tco_apply(KL_ARG_V874_1375[0], [KL_ARG_V875_1376])]) if shen_consp(KL_ARG_V874_1375) else (tail_call(shen_sysx45error, [symdic.symdic_shen_compose]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.compose', shen_compose, 2)

@tail_recursion
def shen_compilex45macro(KL_ARG_V876_1377):
    global symdic
    return ([symdic.symdic_kl_compile, [KL_ARG_V876_1377[1][0], [KL_ARG_V876_1377[1][1][0], [[symdic.symdic_kl_lambda, [symdic.symdic_E, [[symdic.symdic_kl_if, [[symdic.symdic_kl_consx63, [symdic.symdic_E, []]], [[symdic.symdic_kl_error, ['parse error here: ~S~%', [symdic.symdic_E, []]]], [[symdic.symdic_kl_error, ['parse error~%', []]], []]]]], []]]], []]]]] if ((((([] == KL_ARG_V876_1377[1][1][1]) if shen_consp(KL_ARG_V876_1377[1][1]) else False) if shen_consp(KL_ARG_V876_1377[1]) else False) if (symdic.symdic_kl_compile == KL_ARG_V876_1377[0]) else False) if shen_consp(KL_ARG_V876_1377) else False) else (KL_ARG_V876_1377 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.compile-macro', shen_compilex45macro, 1)

@tail_recursion
def shen_prologx45macro(KL_ARG_V877_1378):
    global symdic
    return ([symdic.symdic_shen_intprolog, [tco_apply(shen_prologx45form, [KL_ARG_V877_1378[1]]), []]] if ((symdic.symdic_kl_prologx63 == KL_ARG_V877_1378[0]) if shen_consp(KL_ARG_V877_1378) else False) else (KL_ARG_V877_1378 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.prolog-macro', shen_prologx45macro, 1)

@tail_recursion
def shen_defprologx45macro(KL_ARG_V878_1379):
    global symdic
    return (tail_call(kl_compile, [symdic.symdic_shen_x60defprologx62, KL_ARG_V878_1379[1], (lambda KL_ARG_Y_1380: tail_call(shen_prologx45error, [KL_ARG_V878_1379[1][0], KL_ARG_Y_1380]))]) if ((shen_consp(KL_ARG_V878_1379[1]) if (symdic.symdic_kl_defprolog == KL_ARG_V878_1379[0]) else False) if shen_consp(KL_ARG_V878_1379) else False) else (KL_ARG_V878_1379 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.defprolog-macro', shen_defprologx45macro, 1)

@tail_recursion
def shen_prologx45form(KL_ARG_V879_1381):
    global symdic
    return tail_call(shen_cons_form, [tco_apply(kl_map, [symdic.symdic_shen_cons_form, KL_ARG_V879_1381])])
shen_add_fun('shen.prolog-form', shen_prologx45form, 1)

@tail_recursion
def shen_datatypex45macro(KL_ARG_V880_1382):
    global symdic
    return ([symdic.symdic_shen_processx45datatype, [tco_apply(shen_internx45type, [KL_ARG_V880_1382[1][0]]), [[symdic.symdic_kl_compile, [[symdic.symdic_kl_function, [symdic.symdic_shen_x60datatypex45rulesx62, []]], [tco_apply(shen_rcons_form, [KL_ARG_V880_1382[1][1]]), [[symdic.symdic_kl_function, [symdic.symdic_shen_datatypex45error, []]], []]]]], []]]] if ((shen_consp(KL_ARG_V880_1382[1]) if (symdic.symdic_kl_datatype == KL_ARG_V880_1382[0]) else False) if shen_consp(KL_ARG_V880_1382) else False) else (KL_ARG_V880_1382 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.datatype-macro', shen_datatypex45macro, 1)

@tail_recursion
def shen_internx45type(KL_ARG_V881_1383):
    global symdic
    return shen_intern(('type#' + str(KL_ARG_V881_1383)))
shen_add_fun('shen.intern-type', shen_internx45type, 1)

@tail_recursion
def shen_x64sx45macro(KL_ARG_V882_1384):

    class KL_Context:
        KL_LOC_E_1385 = None
    KL_CTX = KL_Context()
    global symdic
    return ([symdic.symdic_kl_x64s, [KL_ARG_V882_1384[1][0], [tco_apply(shen_x64sx45macro, [[symdic.symdic_kl_x64s, KL_ARG_V882_1384[1][1]]]), []]]] if ((((shen_consp(KL_ARG_V882_1384[1][1][1]) if shen_consp(KL_ARG_V882_1384[1][1]) else False) if shen_consp(KL_ARG_V882_1384[1]) else False) if (symdic.symdic_kl_x64s == KL_ARG_V882_1384[0]) else False) if shen_consp(KL_ARG_V882_1384) else False) else ([setattr(KL_CTX, 'KL_LOC_E_1385', tco_apply(kl_explode, [KL_ARG_V882_1384[1][0]])), (tail_call(shen_x64sx45macro, [[symdic.symdic_kl_x64s, tco_apply(kl_append, [KL_CTX.KL_LOC_E_1385, KL_ARG_V882_1384[1][1]])]]) if (tco_apply(kl_length, [KL_CTX.KL_LOC_E_1385]) > 1) else KL_ARG_V882_1384)][(-1)] if (((((isinstance(KL_ARG_V882_1384[1][0], str) if ([] == KL_ARG_V882_1384[1][1][1]) else False) if shen_consp(KL_ARG_V882_1384[1][1]) else False) if shen_consp(KL_ARG_V882_1384[1]) else False) if (symdic.symdic_kl_x64s == KL_ARG_V882_1384[0]) else False) if shen_consp(KL_ARG_V882_1384) else False) else (KL_ARG_V882_1384 if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.@s-macro', shen_x64sx45macro, 1)

@tail_recursion
def shen_synonymsx45macro(KL_ARG_V883_1386):
    global symdic
    return ([symdic.symdic_shen_synonymsx45help, [tco_apply(shen_rcons_form, [KL_ARG_V883_1386[1]]), []]] if ((symdic.symdic_kl_synonyms == KL_ARG_V883_1386[0]) if shen_consp(KL_ARG_V883_1386) else False) else (KL_ARG_V883_1386 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.synonyms-macro', shen_synonymsx45macro, 1)

@tail_recursion
def shen_nlx45macro(KL_ARG_V884_1387):
    global symdic
    return ([symdic.symdic_kl_nl, [1, []]] if ((([] == KL_ARG_V884_1387[1]) if (symdic.symdic_kl_nl == KL_ARG_V884_1387[0]) else False) if shen_consp(KL_ARG_V884_1387) else False) else (KL_ARG_V884_1387 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.nl-macro', shen_nlx45macro, 1)

@tail_recursion
def shen_assocx45macro(KL_ARG_V885_1388):
    global symdic
    return ([KL_ARG_V885_1388[0], [KL_ARG_V885_1388[1][0], [tco_apply(shen_assocx45macro, [[KL_ARG_V885_1388[0], KL_ARG_V885_1388[1][1]]]), []]]] if ((((tco_apply(kl_elementx63, [KL_ARG_V885_1388[0], [symdic.symdic_kl_x64p, [symdic.symdic_kl_x64v, [symdic.symdic_kl_append, [symdic.symdic_kl_and, [symdic.symdic_kl_or, [symdic.symdic_kl_x43, [symdic.symdic_kl_x42, [symdic.symdic_kl_do, []]]]]]]]]]) if shen_consp(KL_ARG_V885_1388[1][1][1]) else False) if shen_consp(KL_ARG_V885_1388[1][1]) else False) if shen_consp(KL_ARG_V885_1388[1]) else False) if shen_consp(KL_ARG_V885_1388) else False) else (KL_ARG_V885_1388 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.assoc-macro', shen_assocx45macro, 1)

@tail_recursion
def shen_letx45macro(KL_ARG_V886_1389):
    global symdic
    return ([symdic.symdic_kl_let, [KL_ARG_V886_1389[1][0], [KL_ARG_V886_1389[1][1][0], [tco_apply(shen_letx45macro, [[symdic.symdic_kl_let, KL_ARG_V886_1389[1][1][1]]]), []]]]] if (((((shen_consp(KL_ARG_V886_1389[1][1][1][1]) if shen_consp(KL_ARG_V886_1389[1][1][1]) else False) if shen_consp(KL_ARG_V886_1389[1][1]) else False) if shen_consp(KL_ARG_V886_1389[1]) else False) if (symdic.symdic_kl_let == KL_ARG_V886_1389[0]) else False) if shen_consp(KL_ARG_V886_1389) else False) else (KL_ARG_V886_1389 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.let-macro', shen_letx45macro, 1)

@tail_recursion
def shen_absx45macro(KL_ARG_V887_1390):
    global symdic
    return ([symdic.symdic_kl_lambda, [KL_ARG_V887_1390[1][0], [tco_apply(shen_absx45macro, [[symdic.symdic_kl_x47_, KL_ARG_V887_1390[1][1]]]), []]]] if ((((shen_consp(KL_ARG_V887_1390[1][1][1]) if shen_consp(KL_ARG_V887_1390[1][1]) else False) if shen_consp(KL_ARG_V887_1390[1]) else False) if (symdic.symdic_kl_x47_ == KL_ARG_V887_1390[0]) else False) if shen_consp(KL_ARG_V887_1390) else False) else ([symdic.symdic_kl_lambda, KL_ARG_V887_1390[1]] if ((((([] == KL_ARG_V887_1390[1][1][1]) if shen_consp(KL_ARG_V887_1390[1][1]) else False) if shen_consp(KL_ARG_V887_1390[1]) else False) if (symdic.symdic_kl_x47_ == KL_ARG_V887_1390[0]) else False) if shen_consp(KL_ARG_V887_1390) else False) else (KL_ARG_V887_1390 if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.abs-macro', shen_absx45macro, 1)

@tail_recursion
def shen_casesx45macro(KL_ARG_V890_1391):
    global symdic
    return (KL_ARG_V890_1391[1][1][0] if ((((shen_consp(KL_ARG_V890_1391[1][1]) if (True == KL_ARG_V890_1391[1][0]) else False) if shen_consp(KL_ARG_V890_1391[1]) else False) if (symdic.symdic_kl_cases == KL_ARG_V890_1391[0]) else False) if shen_consp(KL_ARG_V890_1391) else False) else ([symdic.symdic_kl_if, [KL_ARG_V890_1391[1][0], [KL_ARG_V890_1391[1][1][0], [[symdic.symdic_kl_simplex45error, ['error: cases exhausted', []]], []]]]] if ((((([] == KL_ARG_V890_1391[1][1][1]) if shen_consp(KL_ARG_V890_1391[1][1]) else False) if shen_consp(KL_ARG_V890_1391[1]) else False) if (symdic.symdic_kl_cases == KL_ARG_V890_1391[0]) else False) if shen_consp(KL_ARG_V890_1391) else False) else ([symdic.symdic_kl_if, [KL_ARG_V890_1391[1][0], [KL_ARG_V890_1391[1][1][0], [tco_apply(shen_casesx45macro, [[symdic.symdic_kl_cases, KL_ARG_V890_1391[1][1][1]]]), []]]]] if (((shen_consp(KL_ARG_V890_1391[1][1]) if shen_consp(KL_ARG_V890_1391[1]) else False) if (symdic.symdic_kl_cases == KL_ARG_V890_1391[0]) else False) if shen_consp(KL_ARG_V890_1391) else False) else (shen_simple_error('error: odd number of case elements\r\n') if (((([] == KL_ARG_V890_1391[1][1]) if shen_consp(KL_ARG_V890_1391[1]) else False) if (symdic.symdic_kl_cases == KL_ARG_V890_1391[0]) else False) if shen_consp(KL_ARG_V890_1391) else False) else (KL_ARG_V890_1391 if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.cases-macro', shen_casesx45macro, 1)

@tail_recursion
def shen_timerx45macro(KL_ARG_V891_1392):
    global symdic
    return (tail_call(shen_letx45macro, [[symdic.symdic_kl_let, [symdic.symdic_Start, [[symdic.symdic_kl_getx45time, [symdic.symdic_kl_run, []]], [symdic.symdic_Result, [KL_ARG_V891_1392[1][0], [symdic.symdic_Finish, [[symdic.symdic_kl_getx45time, [symdic.symdic_kl_run, []]], [symdic.symdic_Time, [[symdic.symdic_kl_x45, [symdic.symdic_Finish, [symdic.symdic_Start, []]]], [symdic.symdic_Message, [[symdic.symdic_shen_prhush, [[symdic.symdic_kl_cn, ['\r\nrun time: ', [[symdic.symdic_kl_cn, [[symdic.symdic_kl_str, [symdic.symdic_Time, []]], [' secs\r\n', []]]], []]]], [[symdic.symdic_kl_stoutput, []], []]]], [symdic.symdic_Result, []]]]]]]]]]]]]]) if (((([] == KL_ARG_V891_1392[1][1]) if shen_consp(KL_ARG_V891_1392[1]) else False) if (symdic.symdic_kl_time == KL_ARG_V891_1392[0]) else False) if shen_consp(KL_ARG_V891_1392) else False) else (KL_ARG_V891_1392 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.timer-macro', shen_timerx45macro, 1)

@tail_recursion
def shen_tuplex45up(KL_ARG_V892_1393):
    global symdic
    return ([symdic.symdic_kl_x64p, [KL_ARG_V892_1393[0], [tco_apply(shen_tuplex45up, [KL_ARG_V892_1393[1]]), []]]] if shen_consp(KL_ARG_V892_1393) else (KL_ARG_V892_1393 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.tuple-up', shen_tuplex45up, 1)

@tail_recursion
def shen_putx47getx45macro(KL_ARG_V893_1394):
    global symdic
    return ([symdic.symdic_kl_put, [KL_ARG_V893_1394[1][0], [KL_ARG_V893_1394[1][1][0], [KL_ARG_V893_1394[1][1][1][0], [[symdic.symdic_kl_value, [symdic.symdic_kl_x42propertyx45vectorx42, []]], []]]]]] if (((((([] == KL_ARG_V893_1394[1][1][1][1]) if shen_consp(KL_ARG_V893_1394[1][1][1]) else False) if shen_consp(KL_ARG_V893_1394[1][1]) else False) if shen_consp(KL_ARG_V893_1394[1]) else False) if (symdic.symdic_kl_put == KL_ARG_V893_1394[0]) else False) if shen_consp(KL_ARG_V893_1394) else False) else ([symdic.symdic_kl_get, [KL_ARG_V893_1394[1][0], [KL_ARG_V893_1394[1][1][0], [[symdic.symdic_kl_value, [symdic.symdic_kl_x42propertyx45vectorx42, []]], []]]]] if ((((([] == KL_ARG_V893_1394[1][1][1]) if shen_consp(KL_ARG_V893_1394[1][1]) else False) if shen_consp(KL_ARG_V893_1394[1]) else False) if (symdic.symdic_kl_get == KL_ARG_V893_1394[0]) else False) if shen_consp(KL_ARG_V893_1394) else False) else (KL_ARG_V893_1394 if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.put/get-macro', shen_putx47getx45macro, 1)

@tail_recursion
def shen_functionx45macro(KL_ARG_V894_1395):
    global symdic
    return (tail_call(shen_functionx45abstraction, [KL_ARG_V894_1395[1][0], tco_apply(kl_arity, [KL_ARG_V894_1395[1][0]])]) if (((([] == KL_ARG_V894_1395[1][1]) if shen_consp(KL_ARG_V894_1395[1]) else False) if (symdic.symdic_kl_function == KL_ARG_V894_1395[0]) else False) if shen_consp(KL_ARG_V894_1395) else False) else (KL_ARG_V894_1395 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.function-macro', shen_functionx45macro, 1)

@tail_recursion
def shen_functionx45abstraction(KL_ARG_V895_1396, KL_ARG_V896_1397):
    global symdic
    return ([symdic.symdic_kl_freeze, [KL_ARG_V895_1396, []]] if (0 == KL_ARG_V896_1397) else (KL_ARG_V895_1396 if ((-1) == KL_ARG_V896_1397) else (tail_call(shen_functionx45abstractionx45help, [KL_ARG_V895_1396, KL_ARG_V896_1397, []]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.function-abstraction', shen_functionx45abstraction, 2)

@tail_recursion
def shen_functionx45abstractionx45help(KL_ARG_V897_1398, KL_ARG_V898_1399, KL_ARG_V899_1400):

    class KL_Context:
        KL_LOC_X_1401 = None
    KL_CTX = KL_Context()
    global symdic
    return ([KL_ARG_V897_1398, KL_ARG_V899_1400] if (0 == KL_ARG_V898_1399) else ([setattr(KL_CTX, 'KL_LOC_X_1401', tco_apply(kl_gensym, [symdic.symdic_V])), [symdic.symdic_kl_x47_, [KL_CTX.KL_LOC_X_1401, [tco_apply(shen_functionx45abstractionx45help, [KL_ARG_V897_1398, (KL_ARG_V898_1399 - 1), tco_apply(kl_append, [KL_ARG_V899_1400, [KL_CTX.KL_LOC_X_1401, []]])]), []]]]][(-1)] if True else shen_simple_error('condition failure')))
shen_add_fun('shen.function-abstraction-help', shen_functionx45abstractionx45help, 3)

@tail_recursion
def kl_undefmacro(KL_ARG_V900_1402):
    global symdic
    return [shen_set(symdic.symdic_kl_x42macrosx42, tco_apply(kl_remove, [KL_ARG_V900_1402, shen_get(symdic.symdic_kl_x42macrosx42)])), KL_ARG_V900_1402][(-1)]
shen_add_fun('undefmacro', kl_undefmacro, 1)


#============================== declarations.kl==============================


shen_set(symdic.symdic_shen_x42installingx45klx42, False)
shen_set(symdic.symdic_shen_x42historyx42, [])
shen_set(symdic.symdic_shen_x42tcx42, False)
shen_set(symdic.symdic_kl_x42propertyx45vectorx42, tco_apply(kl_vector, [20000]))
shen_set(symdic.symdic_shen_x42processx45counterx42, 0)
shen_set(symdic.symdic_shen_x42varcounterx42, tco_apply(kl_vector, [1000]))
shen_set(symdic.symdic_shen_x42prologvectorsx42, tco_apply(kl_vector, [1000]))
shen_set(symdic.symdic_shen_x42readerx45macrosx42, [])
shen_set(symdic.symdic_kl_x42homex45directoryx42, [])
shen_set(symdic.symdic_shen_x42gensymx42, 0)
shen_set(symdic.symdic_shen_x42trackingx42, [])
shen_set(symdic.symdic_kl_x42homex45directoryx42, '')
shen_set(symdic.symdic_shen_x42alphabetx42, [symdic.symdic_A, [symdic.symdic_B, [symdic.symdic_C, [symdic.symdic_D, [symdic.symdic_E, [symdic.symdic_F, [symdic.symdic_G, [symdic.symdic_H, [symdic.symdic_I, [symdic.symdic_J, [symdic.symdic_K, [symdic.symdic_L, [symdic.symdic_M, [symdic.symdic_N, [symdic.symdic_O, [symdic.symdic_P, [symdic.symdic_Q, [symdic.symdic_R, [symdic.symdic_S, [symdic.symdic_T, [symdic.symdic_U, [symdic.symdic_V, [symdic.symdic_W, [symdic.symdic_X, [symdic.symdic_Y, [symdic.symdic_Z, []]]]]]]]]]]]]]]]]]]]]]]]]]])
shen_set(symdic.symdic_shen_x42specialx42, [symdic.symdic_kl_x64p, [symdic.symdic_kl_x64s, [symdic.symdic_kl_x64v, [symdic.symdic_kl_cons, [symdic.symdic_kl_lambda, [symdic.symdic_kl_let, [symdic.symdic_kl_type, [symdic.symdic_kl_where, [symdic.symdic_kl_set, [symdic.symdic_kl_open, []]]]]]]]]]])
shen_set(symdic.symdic_shen_x42extraspecialx42, [symdic.symdic_kl_define, [symdic.symdic_shen_processx45datatype, [symdic.symdic_kl_inputx43, [symdic.symdic_kl_defcc, [symdic.symdic_readx43, [symdic.symdic_kl_defmacro, []]]]]]])
shen_set(symdic.symdic_shen_x42spyx42, False)
shen_set(symdic.symdic_shen_x42datatypesx42, [])
shen_set(symdic.symdic_shen_x42alldatatypesx42, [])
shen_set(symdic.symdic_shen_x42shenx45typex45theoryx45enabledx63x42, True)
shen_set(symdic.symdic_shen_x42synonymsx42, [])
shen_set(symdic.symdic_shen_x42systemx42, [])
shen_set(symdic.symdic_shen_x42signedfuncsx42, [])
shen_set(symdic.symdic_shen_x42maxcomplexityx42, 128)
shen_set(symdic.symdic_shen_x42occursx42, True)
shen_set(symdic.symdic_shen_x42maxinferencesx42, 1000000)
shen_set(symdic.symdic_kl_x42maximumx45printx45sequencex45sizex42, 20)
shen_set(symdic.symdic_shen_x42catchx42, 0)
shen_set(symdic.symdic_shen_x42callx42, 0)
shen_set(symdic.symdic_shen_x42infsx42, 0)
shen_set(symdic.symdic_x42hushx42, False)
shen_set(symdic.symdic_shen_x42optimisex42, False)

@tail_recursion
def shen_initialise_arity_table(KL_ARG_V822_1403):

    class KL_Context:
        KL_LOC_DecArity_1404 = None
    KL_CTX = KL_Context()
    global symdic
    return ([] if ([] == KL_ARG_V822_1403) else ([setattr(KL_CTX, 'KL_LOC_DecArity_1404', tco_apply(kl_put, [KL_ARG_V822_1403[0], symdic.symdic_kl_arity, KL_ARG_V822_1403[1][0], shen_get(symdic.symdic_kl_x42propertyx45vectorx42)])), tail_call(shen_initialise_arity_table, [KL_ARG_V822_1403[1][1]])][(-1)] if (shen_consp(KL_ARG_V822_1403[1]) if shen_consp(KL_ARG_V822_1403) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_initialise_arity_table]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.initialise_arity_table', shen_initialise_arity_table, 1)

@tail_recursion
def kl_arity(KL_ARG_V823_1405):
    global symdic
    return shen_try_except((lambda : tco_apply(kl_get, [KL_ARG_V823_1405, symdic.symdic_kl_arity, shen_get(symdic.symdic_kl_x42propertyx45vectorx42)])), (lambda KL_ARG_E_1406: (-1)))
shen_add_fun('arity', kl_arity, 1)

@tail_recursion
def kl_systemf(KL_ARG_V824_1407):

    class KL_Context:
        KL_LOC_Shen_1408 = None
        KL_LOC_External_1409 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Shen_1408', shen_intern('shen')), [setattr(KL_CTX, 'KL_LOC_External_1409', tco_apply(kl_get, [KL_CTX.KL_LOC_Shen_1408, symdic.symdic_shen_externalx45symbols, shen_get(symdic.symdic_kl_x42propertyx45vectorx42)])), tail_call(kl_put, [KL_CTX.KL_LOC_Shen_1408, symdic.symdic_shen_externalx45symbols, tco_apply(kl_adjoin, [KL_ARG_V824_1407, KL_CTX.KL_LOC_External_1409]), shen_get(symdic.symdic_kl_x42propertyx45vectorx42)])][(-1)]][(-1)]
shen_add_fun('systemf', kl_systemf, 1)

@tail_recursion
def kl_adjoin(KL_ARG_V825_1410, KL_ARG_V826_1411):
    global symdic
    return (KL_ARG_V826_1411 if tco_apply(kl_elementx63, [KL_ARG_V825_1410, KL_ARG_V826_1411]) else [KL_ARG_V825_1410, KL_ARG_V826_1411])
shen_add_fun('adjoin', kl_adjoin, 2)

@tail_recursion
def kl_specialise(KL_ARG_V827_1412):
    global symdic
    return [shen_set(symdic.symdic_shen_x42specialx42, [KL_ARG_V827_1412, shen_get(symdic.symdic_shen_x42specialx42)]), KL_ARG_V827_1412][(-1)]
shen_add_fun('specialise', kl_specialise, 1)

@tail_recursion
def kl_unspecialise(KL_ARG_V828_1413):
    global symdic
    return [shen_set(symdic.symdic_shen_x42specialx42, tco_apply(kl_remove, [KL_ARG_V828_1413, shen_get(symdic.symdic_shen_x42specialx42)])), KL_ARG_V828_1413][(-1)]
shen_add_fun('unspecialise', kl_unspecialise, 1)


#============================== types.kl==============================



@tail_recursion
def kl_declare(KL_ARG_V2107_1414, KL_ARG_V2108_1415):

    class KL_Context:
        KL_LOC_Record_1416 = None
        KL_LOC_Variancy_1417 = None
        KL_LOC_Type_1419 = None
        KL_LOC_Fx42_1420 = None
        KL_LOC_Parameters_1421 = None
        KL_LOC_Clause_1422 = None
        KL_LOC_AUM_instruction_1423 = None
        KL_LOC_Code_1424 = None
        KL_LOC_ShenDef_1425 = None
        KL_LOC_Eval_1426 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Record_1416', shen_set(symdic.symdic_shen_x42signedfuncsx42, [[KL_ARG_V2107_1414, KL_ARG_V2108_1415], shen_get(symdic.symdic_shen_x42signedfuncsx42)])), [setattr(KL_CTX, 'KL_LOC_Variancy_1417', shen_try_except((lambda : tco_apply(shen_variancyx45test, [KL_ARG_V2107_1414, KL_ARG_V2108_1415])), (lambda KL_ARG_E_1418: symdic.symdic_shen_skip))), [setattr(KL_CTX, 'KL_LOC_Type_1419', tco_apply(shen_rcons_form, [tco_apply(shen_demodulate, [KL_ARG_V2108_1415])])), [setattr(KL_CTX, 'KL_LOC_Fx42_1420', tco_apply(kl_concat, [symdic.symdic_shen_typex45signaturex45ofx45, KL_ARG_V2107_1414])), [setattr(KL_CTX, 'KL_LOC_Parameters_1421', tco_apply(shen_parameters, [1])), [setattr(KL_CTX, 'KL_LOC_Clause_1422', [[KL_CTX.KL_LOC_Fx42_1420, [symdic.symdic_X, []]], [symdic.symdic_kl_x58x45, [[[symdic.symdic_kl_unifyx33, [symdic.symdic_X, [KL_CTX.KL_LOC_Type_1419, []]]], []], []]]]), [setattr(KL_CTX, 'KL_LOC_AUM_instruction_1423', tco_apply(shen_aum, [KL_CTX.KL_LOC_Clause_1422, KL_CTX.KL_LOC_Parameters_1421])), [setattr(KL_CTX, 'KL_LOC_Code_1424', tco_apply(shen_aum_to_shen, [KL_CTX.KL_LOC_AUM_instruction_1423])), [setattr(KL_CTX, 'KL_LOC_ShenDef_1425', [symdic.symdic_kl_define, [KL_CTX.KL_LOC_Fx42_1420, tco_apply(kl_append, [KL_CTX.KL_LOC_Parameters_1421, tco_apply(kl_append, [[symdic.symdic_ProcessN, [symdic.symdic_Continuation, []]], [symdic.symdic_kl_x45x62, [KL_CTX.KL_LOC_Code_1424, []]]])])]]), [setattr(KL_CTX, 'KL_LOC_Eval_1426', tco_apply(shen_evalx45withoutx45macros, [KL_CTX.KL_LOC_ShenDef_1425])), KL_ARG_V2107_1414][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]
shen_add_fun('declare', kl_declare, 2)

@tail_recursion
def shen_demodulate(KL_ARG_V2109_1427):
    global symdic
    return tail_call(kl_fix, [symdic.symdic_shen_demodh, KL_ARG_V2109_1427])
shen_add_fun('shen.demodulate', shen_demodulate, 1)

@tail_recursion
def shen_demodh(KL_ARG_V2110_1428):
    global symdic
    return (tail_call(kl_map, [symdic.symdic_shen_demodh, KL_ARG_V2110_1428]) if shen_consp(KL_ARG_V2110_1428) else (tail_call(shen_demodx45atom, [KL_ARG_V2110_1428]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.demodh', shen_demodh, 1)

@tail_recursion
def shen_demodx45atom(KL_ARG_V2111_1429):

    class KL_Context:
        KL_LOC_Val_1430 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Val_1430', tco_apply(kl_assoc, [KL_ARG_V2111_1429, shen_get(symdic.symdic_shen_x42synonymsx42)])), (KL_ARG_V2111_1429 if tco_apply(kl_emptyx63, [KL_CTX.KL_LOC_Val_1430]) else KL_CTX.KL_LOC_Val_1430[1])][(-1)]
shen_add_fun('shen.demod-atom', shen_demodx45atom, 1)

@tail_recursion
def shen_variancyx45test(KL_ARG_V2112_1431, KL_ARG_V2113_1432):

    class KL_Context:
        KL_LOC_TypeF_1433 = None
        KL_LOC_Check_1434 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_TypeF_1433', tco_apply(shen_typecheck, [KL_ARG_V2112_1431, symdic.symdic_B])), [setattr(KL_CTX, 'KL_LOC_Check_1434', (symdic.symdic_shen_skip if (symdic.symdic_kl_symbol == KL_CTX.KL_LOC_TypeF_1433) else (symdic.symdic_shen_skip if tco_apply(shen_variantx63, [KL_CTX.KL_LOC_TypeF_1433, KL_ARG_V2113_1432]) else tco_apply(shen_prhush, [('warning: changing the type of ' + tco_apply(shen_app, [KL_ARG_V2112_1431, ' may create errors\r\n', symdic.symdic_shen_a])), tco_apply(kl_stoutput, [])])))), symdic.symdic_shen_skip][(-1)]][(-1)]
shen_add_fun('shen.variancy-test', shen_variancyx45test, 2)

@tail_recursion
def shen_variantx63(KL_ARG_V2122_1435, KL_ARG_V2123_1436):
    global symdic
    return (True if (KL_ARG_V2123_1436 == KL_ARG_V2122_1435) else (tail_call(shen_variantx63, [KL_ARG_V2122_1435[1], KL_ARG_V2123_1436[1]]) if (((KL_ARG_V2123_1436[0] == KL_ARG_V2122_1435[0]) if shen_consp(KL_ARG_V2123_1436) else False) if shen_consp(KL_ARG_V2122_1435) else False) else (tail_call(shen_variantx63, [tco_apply(kl_subst, [symdic.symdic_shen_a, KL_ARG_V2122_1435[0], KL_ARG_V2122_1435[1]]), tco_apply(kl_subst, [symdic.symdic_shen_a, KL_ARG_V2123_1436[0], KL_ARG_V2123_1436[1]])]) if (((tco_apply(kl_variablex63, [KL_ARG_V2123_1436[0]]) if tco_apply(shen_pvarx63, [KL_ARG_V2122_1435[0]]) else False) if shen_consp(KL_ARG_V2123_1436) else False) if shen_consp(KL_ARG_V2122_1435) else False) else (tail_call(shen_variantx63, [tco_apply(kl_append, [KL_ARG_V2122_1435[0], KL_ARG_V2122_1435[1]]), tco_apply(kl_append, [KL_ARG_V2123_1436[0], KL_ARG_V2123_1436[1]])]) if (((shen_consp(KL_ARG_V2123_1436[0]) if shen_consp(KL_ARG_V2123_1436) else False) if shen_consp(KL_ARG_V2122_1435[0]) else False) if shen_consp(KL_ARG_V2122_1435) else False) else (False if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.variant?', shen_variantx63, 2)


#============================== t-star.kl==============================



@tail_recursion
def shen_typecheck(KL_ARG_V2823_1437, KL_ARG_V2824_1438):

    class KL_Context:
        KL_LOC_Curry_1439 = None
        KL_LOC_ProcessN_1440 = None
        KL_LOC_Type_1441 = None
        KL_LOC_Continuation_1442 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Curry_1439', tco_apply(shen_curry, [KL_ARG_V2823_1437])), [setattr(KL_CTX, 'KL_LOC_ProcessN_1440', tco_apply(shen_startx45newx45prologx45process, [])), [setattr(KL_CTX, 'KL_LOC_Type_1441', tco_apply(shen_insertx45prologx45variables, [tco_apply(shen_demodulate, [tco_apply(shen_curryx45type, [KL_ARG_V2824_1438])]), KL_CTX.KL_LOC_ProcessN_1440])), [setattr(KL_CTX, 'KL_LOC_Continuation_1442', (lambda : tail_call(kl_return, [KL_CTX.KL_LOC_Type_1441, KL_CTX.KL_LOC_ProcessN_1440, symdic.symdic_shen_void]))), tail_call(shen_tx42, [[KL_CTX.KL_LOC_Curry_1439, [symdic.symdic_kl_x58, [KL_CTX.KL_LOC_Type_1441, []]]], [], KL_CTX.KL_LOC_ProcessN_1440, KL_CTX.KL_LOC_Continuation_1442])][(-1)]][(-1)]][(-1)]][(-1)]
shen_add_fun('shen.typecheck', shen_typecheck, 2)

@tail_recursion
def shen_curry(KL_ARG_V2825_1443):
    global symdic
    return ([KL_ARG_V2825_1443[0], tco_apply(kl_map, [symdic.symdic_shen_curry, KL_ARG_V2825_1443[1]])] if (tco_apply(shen_specialx63, [KL_ARG_V2825_1443[0]]) if shen_consp(KL_ARG_V2825_1443) else False) else (KL_ARG_V2825_1443 if ((tco_apply(shen_extraspecialx63, [KL_ARG_V2825_1443[0]]) if shen_consp(KL_ARG_V2825_1443[1]) else False) if shen_consp(KL_ARG_V2825_1443) else False) else (tail_call(shen_curry, [[[KL_ARG_V2825_1443[0], [KL_ARG_V2825_1443[1][0], []]], KL_ARG_V2825_1443[1][1]]]) if ((shen_consp(KL_ARG_V2825_1443[1][1]) if shen_consp(KL_ARG_V2825_1443[1]) else False) if shen_consp(KL_ARG_V2825_1443) else False) else ([tco_apply(shen_curry, [KL_ARG_V2825_1443[0]]), [tco_apply(shen_curry, [KL_ARG_V2825_1443[1][0]]), []]] if ((([] == KL_ARG_V2825_1443[1][1]) if shen_consp(KL_ARG_V2825_1443[1]) else False) if shen_consp(KL_ARG_V2825_1443) else False) else (KL_ARG_V2825_1443 if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.curry', shen_curry, 1)

@tail_recursion
def shen_specialx63(KL_ARG_V2826_1444):
    global symdic
    return tail_call(kl_elementx63, [KL_ARG_V2826_1444, shen_get(symdic.symdic_shen_x42specialx42)])
shen_add_fun('shen.special?', shen_specialx63, 1)

@tail_recursion
def shen_extraspecialx63(KL_ARG_V2827_1445):
    global symdic
    return tail_call(kl_elementx63, [KL_ARG_V2827_1445, shen_get(symdic.symdic_shen_x42extraspecialx42)])
shen_add_fun('shen.extraspecial?', shen_extraspecialx63, 1)

@tail_recursion
def shen_tx42(KL_ARG_V2828_1446, KL_ARG_V2829_1447, KL_ARG_V2830_1448, KL_ARG_V2831_1449):

    class KL_Context:
        KL_LOC_Throwcontrol_1450 = None
        KL_LOC_Case_1451 = None
        KL_LOC_Error_1452 = None
        KL_LOC_Case_1453 = None
        KL_LOC_V2817_1454 = None
        KL_LOC_Case_1455 = None
        KL_LOC_V2818_1456 = None
        KL_LOC_X_1457 = None
        KL_LOC_V2819_1458 = None
        KL_LOC_V2820_1459 = None
        KL_LOC_V2821_1460 = None
        KL_LOC_A_1461 = None
        KL_LOC_V2822_1462 = None
        KL_LOC_Datatypes_1463 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Throwcontrol_1450', tco_apply(shen_catchpoint, [])), tail_call(shen_cutpoint, [KL_CTX.KL_LOC_Throwcontrol_1450, [setattr(KL_CTX, 'KL_LOC_Case_1451', [setattr(KL_CTX, 'KL_LOC_Error_1452', tco_apply(shen_newpv, [KL_ARG_V2830_1448])), [tco_apply(shen_incinfs, []), tco_apply(kl_fwhen, [tco_apply(shen_maxinfexceededx63, []), KL_ARG_V2830_1448, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Error_1452, tco_apply(shen_errormaxinfs, []), KL_ARG_V2830_1448, KL_ARG_V2831_1449]))])][(-1)]][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1453', [setattr(KL_CTX, 'KL_LOC_V2817_1454', tco_apply(shen_lazyderef, [KL_ARG_V2828_1446, KL_ARG_V2830_1448])), ([tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1450, KL_ARG_V2830_1448, (lambda : tail_call(shen_prologx45failure, [KL_ARG_V2830_1448, KL_ARG_V2831_1449]))])][(-1)] if (symdic.symdic_kl_fail == KL_CTX.KL_LOC_V2817_1454) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1455', [setattr(KL_CTX, 'KL_LOC_V2818_1456', tco_apply(shen_lazyderef, [KL_ARG_V2828_1446, KL_ARG_V2830_1448])), ([setattr(KL_CTX, 'KL_LOC_X_1457', KL_CTX.KL_LOC_V2818_1456[0]), [setattr(KL_CTX, 'KL_LOC_V2819_1458', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2818_1456[1], KL_ARG_V2830_1448])), ([setattr(KL_CTX, 'KL_LOC_V2820_1459', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2819_1458[0], KL_ARG_V2830_1448])), ([setattr(KL_CTX, 'KL_LOC_V2821_1460', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2819_1458[1], KL_ARG_V2830_1448])), ([setattr(KL_CTX, 'KL_LOC_A_1461', KL_CTX.KL_LOC_V2821_1460[0]), [setattr(KL_CTX, 'KL_LOC_V2822_1462', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2821_1460[1], KL_ARG_V2830_1448])), ([tco_apply(shen_incinfs, []), tco_apply(kl_fwhen, [tco_apply(shen_typex45theoryx45enabledx63, []), KL_ARG_V2830_1448, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1450, KL_ARG_V2830_1448, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_X_1457, KL_CTX.KL_LOC_A_1461, KL_ARG_V2829_1447, KL_ARG_V2830_1448, KL_ARG_V2831_1449]))]))])][(-1)] if ([] == KL_CTX.KL_LOC_V2822_1462) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2821_1460) else False)][(-1)] if (symdic.symdic_kl_x58 == KL_CTX.KL_LOC_V2820_1459) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2819_1458) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2818_1456) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Datatypes_1463', tco_apply(shen_newpv, [KL_ARG_V2830_1448])), [tco_apply(shen_incinfs, []), tco_apply(shen_show, [KL_ARG_V2828_1446, KL_ARG_V2829_1447, KL_ARG_V2830_1448, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Datatypes_1463, shen_get(symdic.symdic_shen_x42datatypesx42), KL_ARG_V2830_1448, (lambda : tail_call(shen_udefsx42, [KL_ARG_V2828_1446, KL_ARG_V2829_1447, KL_CTX.KL_LOC_Datatypes_1463, KL_ARG_V2830_1448, KL_ARG_V2831_1449]))]))])][(-1)]][(-1)] if (KL_CTX.KL_LOC_Case_1455 == False) else KL_CTX.KL_LOC_Case_1455)][(-1)] if (KL_CTX.KL_LOC_Case_1453 == False) else KL_CTX.KL_LOC_Case_1453)][(-1)] if (KL_CTX.KL_LOC_Case_1451 == False) else KL_CTX.KL_LOC_Case_1451)][(-1)]])][(-1)]
shen_add_fun('shen.t*', shen_tx42, 4)

@tail_recursion
def shen_typex45theoryx45enabledx63():
    global symdic
    return shen_get(symdic.symdic_shen_x42shenx45typex45theoryx45enabledx63x42)
shen_add_fun('shen.type-theory-enabled?', shen_typex45theoryx45enabledx63, 0)

@tail_recursion
def kl_enablex45typex45theory(KL_ARG_V2836_1464):
    global symdic
    return (shen_set(symdic.symdic_shen_x42shenx45typex45theoryx45enabledx63x42, True) if (symdic.symdic_kl_x43 == KL_ARG_V2836_1464) else (shen_set(symdic.symdic_shen_x42shenx45typex45theoryx45enabledx63x42, False) if (symdic.symdic_kl_x45 == KL_ARG_V2836_1464) else (shen_simple_error('enable-type-theory expects a + or a -\r\n') if True else shen_simple_error('condition failure'))))
shen_add_fun('enable-type-theory', kl_enablex45typex45theory, 1)

@tail_recursion
def shen_prologx45failure(KL_ARG_V2845_1465, KL_ARG_V2846_1466):
    global symdic
    return False
shen_add_fun('shen.prolog-failure', shen_prologx45failure, 2)

@tail_recursion
def shen_maxinfexceededx63():
    global symdic
    return (tco_apply(kl_inferences, []) > shen_get(symdic.symdic_shen_x42maxinferencesx42))
shen_add_fun('shen.maxinfexceeded?', shen_maxinfexceededx63, 0)

@tail_recursion
def shen_errormaxinfs():
    global symdic
    return shen_simple_error('maximum inferences exceeded~%')
shen_add_fun('shen.errormaxinfs', shen_errormaxinfs, 0)

@tail_recursion
def shen_udefsx42(KL_ARG_V2847_1467, KL_ARG_V2848_1468, KL_ARG_V2849_1469, KL_ARG_V2850_1470, KL_ARG_V2851_1471):

    class KL_Context:
        KL_LOC_Case_1472 = None
        KL_LOC_V2813_1473 = None
        KL_LOC_D_1474 = None
        KL_LOC_V2814_1475 = None
        KL_LOC_Ds_1476 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Case_1472', [setattr(KL_CTX, 'KL_LOC_V2813_1473', tco_apply(shen_lazyderef, [KL_ARG_V2849_1469, KL_ARG_V2850_1470])), ([setattr(KL_CTX, 'KL_LOC_D_1474', KL_CTX.KL_LOC_V2813_1473[0]), [tco_apply(shen_incinfs, []), tco_apply(kl_call, [[KL_CTX.KL_LOC_D_1474, [KL_ARG_V2847_1467, [KL_ARG_V2848_1468, []]]], KL_ARG_V2850_1470, KL_ARG_V2851_1471])][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2813_1473) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_V2814_1475', tco_apply(shen_lazyderef, [KL_ARG_V2849_1469, KL_ARG_V2850_1470])), ([setattr(KL_CTX, 'KL_LOC_Ds_1476', KL_CTX.KL_LOC_V2814_1475[1]), [tco_apply(shen_incinfs, []), tail_call(shen_udefsx42, [KL_ARG_V2847_1467, KL_ARG_V2848_1468, KL_CTX.KL_LOC_Ds_1476, KL_ARG_V2850_1470, KL_ARG_V2851_1471])][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2814_1475) else False)][(-1)] if (KL_CTX.KL_LOC_Case_1472 == False) else KL_CTX.KL_LOC_Case_1472)][(-1)]
shen_add_fun('shen.udefs*', shen_udefsx42, 5)

@tail_recursion
def shen_thx42(KL_ARG_V2852_1477, KL_ARG_V2853_1478, KL_ARG_V2854_1479, KL_ARG_V2855_1480, KL_ARG_V2856_1481):

    class KL_Context:
        KL_LOC_Throwcontrol_1482 = None
        KL_LOC_Case_1483 = None
        KL_LOC_Case_1484 = None
        KL_LOC_F_1485 = None
        KL_LOC_Case_1486 = None
        KL_LOC_Case_1487 = None
        KL_LOC_Case_1488 = None
        KL_LOC_V2689_1489 = None
        KL_LOC_F_1490 = None
        KL_LOC_V2690_1491 = None
        KL_LOC_Case_1492 = None
        KL_LOC_V2691_1493 = None
        KL_LOC_F_1494 = None
        KL_LOC_V2692_1495 = None
        KL_LOC_X_1496 = None
        KL_LOC_V2693_1497 = None
        KL_LOC_B_1498 = None
        KL_LOC_Case_1499 = None
        KL_LOC_V2694_1500 = None
        KL_LOC_V2695_1501 = None
        KL_LOC_V2696_1502 = None
        KL_LOC_X_1503 = None
        KL_LOC_V2697_1504 = None
        KL_LOC_Y_1505 = None
        KL_LOC_V2698_1506 = None
        KL_LOC_V2699_1507 = None
        KL_LOC_V2700_1508 = None
        KL_LOC_V2701_1509 = None
        KL_LOC_A_1510 = None
        KL_LOC_V2702_1511 = None
        KL_LOC_Result_1512 = None
        KL_LOC_A_1513 = None
        KL_LOC_Result_1514 = None
        KL_LOC_Result_1515 = None
        KL_LOC_V2703_1516 = None
        KL_LOC_A_1517 = None
        KL_LOC_V2704_1518 = None
        KL_LOC_Result_1519 = None
        KL_LOC_A_1520 = None
        KL_LOC_Result_1521 = None
        KL_LOC_A_1522 = None
        KL_LOC_Result_1523 = None
        KL_LOC_Case_1524 = None
        KL_LOC_V2705_1525 = None
        KL_LOC_V2706_1526 = None
        KL_LOC_V2707_1527 = None
        KL_LOC_X_1528 = None
        KL_LOC_V2708_1529 = None
        KL_LOC_Y_1530 = None
        KL_LOC_V2709_1531 = None
        KL_LOC_V2710_1532 = None
        KL_LOC_A_1533 = None
        KL_LOC_V2711_1534 = None
        KL_LOC_V2712_1535 = None
        KL_LOC_V2713_1536 = None
        KL_LOC_B_1537 = None
        KL_LOC_V2714_1538 = None
        KL_LOC_Result_1539 = None
        KL_LOC_B_1540 = None
        KL_LOC_Result_1541 = None
        KL_LOC_Result_1542 = None
        KL_LOC_V2715_1543 = None
        KL_LOC_B_1544 = None
        KL_LOC_V2716_1545 = None
        KL_LOC_Result_1546 = None
        KL_LOC_B_1547 = None
        KL_LOC_Result_1548 = None
        KL_LOC_B_1549 = None
        KL_LOC_Result_1550 = None
        KL_LOC_A_1551 = None
        KL_LOC_B_1552 = None
        KL_LOC_Result_1553 = None
        KL_LOC_Case_1554 = None
        KL_LOC_V2717_1555 = None
        KL_LOC_V2718_1556 = None
        KL_LOC_V2719_1557 = None
        KL_LOC_X_1558 = None
        KL_LOC_V2720_1559 = None
        KL_LOC_Y_1560 = None
        KL_LOC_V2721_1561 = None
        KL_LOC_V2722_1562 = None
        KL_LOC_V2723_1563 = None
        KL_LOC_V2724_1564 = None
        KL_LOC_A_1565 = None
        KL_LOC_V2725_1566 = None
        KL_LOC_Result_1567 = None
        KL_LOC_A_1568 = None
        KL_LOC_Result_1569 = None
        KL_LOC_Result_1570 = None
        KL_LOC_V2726_1571 = None
        KL_LOC_A_1572 = None
        KL_LOC_V2727_1573 = None
        KL_LOC_Result_1574 = None
        KL_LOC_A_1575 = None
        KL_LOC_Result_1576 = None
        KL_LOC_A_1577 = None
        KL_LOC_Result_1578 = None
        KL_LOC_Case_1579 = None
        KL_LOC_V2728_1580 = None
        KL_LOC_V2729_1581 = None
        KL_LOC_V2730_1582 = None
        KL_LOC_X_1583 = None
        KL_LOC_V2731_1584 = None
        KL_LOC_Y_1585 = None
        KL_LOC_V2732_1586 = None
        KL_LOC_V2733_1587 = None
        KL_LOC_Result_1588 = None
        KL_LOC_Case_1589 = None
        KL_LOC_V2734_1590 = None
        KL_LOC_V2735_1591 = None
        KL_LOC_V2736_1592 = None
        KL_LOC_X_1593 = None
        KL_LOC_V2737_1594 = None
        KL_LOC_Y_1595 = None
        KL_LOC_V2738_1596 = None
        KL_LOC_V2739_1597 = None
        KL_LOC_A_1598 = None
        KL_LOC_V2740_1599 = None
        KL_LOC_V2741_1600 = None
        KL_LOC_V2742_1601 = None
        KL_LOC_B_1602 = None
        KL_LOC_V2743_1603 = None
        KL_LOC_Z_1604 = None
        KL_LOC_Xx38x38_1605 = None
        KL_LOC_Result_1606 = None
        KL_LOC_Z_1607 = None
        KL_LOC_Xx38x38_1608 = None
        KL_LOC_B_1609 = None
        KL_LOC_Result_1610 = None
        KL_LOC_Z_1611 = None
        KL_LOC_Xx38x38_1612 = None
        KL_LOC_Result_1613 = None
        KL_LOC_V2744_1614 = None
        KL_LOC_B_1615 = None
        KL_LOC_V2745_1616 = None
        KL_LOC_Z_1617 = None
        KL_LOC_Xx38x38_1618 = None
        KL_LOC_Result_1619 = None
        KL_LOC_Z_1620 = None
        KL_LOC_Xx38x38_1621 = None
        KL_LOC_B_1622 = None
        KL_LOC_Result_1623 = None
        KL_LOC_Z_1624 = None
        KL_LOC_Xx38x38_1625 = None
        KL_LOC_B_1626 = None
        KL_LOC_Result_1627 = None
        KL_LOC_Z_1628 = None
        KL_LOC_Xx38x38_1629 = None
        KL_LOC_A_1630 = None
        KL_LOC_B_1631 = None
        KL_LOC_Result_1632 = None
        KL_LOC_Z_1633 = None
        KL_LOC_Xx38x38_1634 = None
        KL_LOC_Case_1635 = None
        KL_LOC_V2746_1636 = None
        KL_LOC_V2747_1637 = None
        KL_LOC_V2748_1638 = None
        KL_LOC_X_1639 = None
        KL_LOC_V2749_1640 = None
        KL_LOC_Y_1641 = None
        KL_LOC_V2750_1642 = None
        KL_LOC_Z_1643 = None
        KL_LOC_V2751_1644 = None
        KL_LOC_W_1645 = None
        KL_LOC_Xx38x38_1646 = None
        KL_LOC_B_1647 = None
        KL_LOC_Case_1648 = None
        KL_LOC_V2752_1649 = None
        KL_LOC_V2753_1650 = None
        KL_LOC_V2754_1651 = None
        KL_LOC_V2755_1652 = None
        KL_LOC_V2756_1653 = None
        KL_LOC_FileName_1654 = None
        KL_LOC_V2757_1655 = None
        KL_LOC_Direction2685_1656 = None
        KL_LOC_V2758_1657 = None
        KL_LOC_V2759_1658 = None
        KL_LOC_V2760_1659 = None
        KL_LOC_V2761_1660 = None
        KL_LOC_Direction_1661 = None
        KL_LOC_V2762_1662 = None
        KL_LOC_Result_1663 = None
        KL_LOC_Direction_1664 = None
        KL_LOC_Result_1665 = None
        KL_LOC_Result_1666 = None
        KL_LOC_V2763_1667 = None
        KL_LOC_Direction_1668 = None
        KL_LOC_V2764_1669 = None
        KL_LOC_Result_1670 = None
        KL_LOC_Direction_1671 = None
        KL_LOC_Result_1672 = None
        KL_LOC_Direction_1673 = None
        KL_LOC_Result_1674 = None
        KL_LOC_Case_1675 = None
        KL_LOC_V2765_1676 = None
        KL_LOC_V2766_1677 = None
        KL_LOC_V2767_1678 = None
        KL_LOC_X_1679 = None
        KL_LOC_V2768_1680 = None
        KL_LOC_A_1681 = None
        KL_LOC_V2769_1682 = None
        KL_LOC_Case_1683 = None
        KL_LOC_V2770_1684 = None
        KL_LOC_V2771_1685 = None
        KL_LOC_V2772_1686 = None
        KL_LOC_V2773_1687 = None
        KL_LOC_V2774_1688 = None
        KL_LOC_A_1689 = None
        KL_LOC_V2775_1690 = None
        KL_LOC_C_1691 = None
        KL_LOC_Case_1692 = None
        KL_LOC_V2776_1693 = None
        KL_LOC_V2777_1694 = None
        KL_LOC_V2778_1695 = None
        KL_LOC_V2779_1696 = None
        KL_LOC_V2780_1697 = None
        KL_LOC_A_1698 = None
        KL_LOC_V2781_1699 = None
        KL_LOC_C_1700 = None
        KL_LOC_Case_1701 = None
        KL_LOC_V2782_1702 = None
        KL_LOC_V2783_1703 = None
        KL_LOC_V2784_1704 = None
        KL_LOC_Var_1705 = None
        KL_LOC_V2785_1706 = None
        KL_LOC_Val_1707 = None
        KL_LOC_V2786_1708 = None
        KL_LOC_Case_1709 = None
        KL_LOC_V2787_1710 = None
        KL_LOC_V2788_1711 = None
        KL_LOC_V2789_1712 = None
        KL_LOC_F_1713 = None
        KL_LOC_V2790_1714 = None
        KL_LOC_A_1715 = None
        KL_LOC_Fx38x38_1716 = None
        KL_LOC_B_1717 = None
        KL_LOC_Case_1718 = None
        KL_LOC_V2791_1719 = None
        KL_LOC_V2792_1720 = None
        KL_LOC_V2793_1721 = None
        KL_LOC_V2794_1722 = None
        KL_LOC_Result_1723 = None
        KL_LOC_Case_1724 = None
        KL_LOC_NewHyp_1725 = None
        KL_LOC_Case_1726 = None
        KL_LOC_V2795_1727 = None
        KL_LOC_V2796_1728 = None
        KL_LOC_V2797_1729 = None
        KL_LOC_F_1730 = None
        KL_LOC_X_1731 = None
        KL_LOC_Case_1732 = None
        KL_LOC_V2798_1733 = None
        KL_LOC_V2799_1734 = None
        KL_LOC_V2800_1735 = None
        KL_LOC_F_1736 = None
        KL_LOC_X_1737 = None
        KL_LOC_Case_1738 = None
        KL_LOC_V2801_1739 = None
        KL_LOC_V2802_1740 = None
        KL_LOC_V2803_1741 = None
        KL_LOC_Result_1742 = None
        KL_LOC_Case_1743 = None
        KL_LOC_V2804_1744 = None
        KL_LOC_V2805_1745 = None
        KL_LOC_V2806_1746 = None
        KL_LOC_Result_1747 = None
        KL_LOC_Case_1748 = None
        KL_LOC_V2807_1749 = None
        KL_LOC_V2808_1750 = None
        KL_LOC_V2809_1751 = None
        KL_LOC_Result_1752 = None
        KL_LOC_Datatypes_1753 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Throwcontrol_1482', tco_apply(shen_catchpoint, [])), tail_call(shen_cutpoint, [KL_CTX.KL_LOC_Throwcontrol_1482, [setattr(KL_CTX, 'KL_LOC_Case_1483', [tco_apply(shen_incinfs, []), tco_apply(shen_show, [[KL_ARG_V2852_1477, [symdic.symdic_kl_x58, [KL_ARG_V2853_1478, []]]], KL_ARG_V2854_1479, KL_ARG_V2855_1480, (lambda : tail_call(kl_fwhen, [False, KL_ARG_V2855_1480, KL_ARG_V2856_1481]))])][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1484', [setattr(KL_CTX, 'KL_LOC_F_1485', tco_apply(shen_newpv, [KL_ARG_V2855_1480])), [tco_apply(shen_incinfs, []), tco_apply(kl_fwhen, [tco_apply(shen_typedfx63, [tco_apply(shen_lazyderef, [KL_ARG_V2852_1477, KL_ARG_V2855_1480])]), KL_ARG_V2855_1480, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_F_1485, tco_apply(shen_sigf, [tco_apply(shen_lazyderef, [KL_ARG_V2852_1477, KL_ARG_V2855_1480])]), KL_ARG_V2855_1480, (lambda : tail_call(kl_call, [[KL_CTX.KL_LOC_F_1485, [KL_ARG_V2853_1478, []]], KL_ARG_V2855_1480, KL_ARG_V2856_1481]))]))])][(-1)]][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1486', [tco_apply(shen_incinfs, []), tco_apply(shen_base, [KL_ARG_V2852_1477, KL_ARG_V2853_1478, KL_ARG_V2855_1480, KL_ARG_V2856_1481])][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1487', [tco_apply(shen_incinfs, []), tco_apply(shen_by_hypothesis, [KL_ARG_V2852_1477, KL_ARG_V2853_1478, KL_ARG_V2854_1479, KL_ARG_V2855_1480, KL_ARG_V2856_1481])][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1488', [setattr(KL_CTX, 'KL_LOC_V2689_1489', tco_apply(shen_lazyderef, [KL_ARG_V2852_1477, KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_F_1490', KL_CTX.KL_LOC_V2689_1489[0]), [setattr(KL_CTX, 'KL_LOC_V2690_1491', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2689_1489[1], KL_ARG_V2855_1480])), ([tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_F_1490, [symdic.symdic_kl_x45x45x62, [KL_ARG_V2853_1478, []]], KL_ARG_V2854_1479, KL_ARG_V2855_1480, KL_ARG_V2856_1481])][(-1)] if ([] == KL_CTX.KL_LOC_V2690_1491) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2689_1489) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1492', [setattr(KL_CTX, 'KL_LOC_V2691_1493', tco_apply(shen_lazyderef, [KL_ARG_V2852_1477, KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_F_1494', KL_CTX.KL_LOC_V2691_1493[0]), [setattr(KL_CTX, 'KL_LOC_V2692_1495', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2691_1493[1], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_X_1496', KL_CTX.KL_LOC_V2692_1495[0]), [setattr(KL_CTX, 'KL_LOC_V2693_1497', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2692_1495[1], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_B_1498', tco_apply(shen_newpv, [KL_ARG_V2855_1480])), [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_F_1494, [KL_CTX.KL_LOC_B_1498, [symdic.symdic_kl_x45x45x62, [KL_ARG_V2853_1478, []]]], KL_ARG_V2854_1479, KL_ARG_V2855_1480, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_X_1496, KL_CTX.KL_LOC_B_1498, KL_ARG_V2854_1479, KL_ARG_V2855_1480, KL_ARG_V2856_1481]))])][(-1)]][(-1)] if ([] == KL_CTX.KL_LOC_V2693_1497) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2692_1495) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2691_1493) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1499', [setattr(KL_CTX, 'KL_LOC_V2694_1500', tco_apply(shen_lazyderef, [KL_ARG_V2852_1477, KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_V2695_1501', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2694_1500[0], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_V2696_1502', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2694_1500[1], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_X_1503', KL_CTX.KL_LOC_V2696_1502[0]), [setattr(KL_CTX, 'KL_LOC_V2697_1504', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2696_1502[1], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_Y_1505', KL_CTX.KL_LOC_V2697_1504[0]), [setattr(KL_CTX, 'KL_LOC_V2698_1506', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2697_1504[1], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_V2699_1507', tco_apply(shen_lazyderef, [KL_ARG_V2853_1478, KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_V2700_1508', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2699_1507[0], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_V2701_1509', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2699_1507[1], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_A_1510', KL_CTX.KL_LOC_V2701_1509[0]), [setattr(KL_CTX, 'KL_LOC_V2702_1511', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2701_1509[1], KL_ARG_V2855_1480])), ([tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1503, KL_CTX.KL_LOC_A_1510, KL_ARG_V2854_1479, KL_ARG_V2855_1480, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1505, [symdic.symdic_kl_list, [KL_CTX.KL_LOC_A_1510, []]], KL_ARG_V2854_1479, KL_ARG_V2855_1480, KL_ARG_V2856_1481]))])][(-1)] if ([] == KL_CTX.KL_LOC_V2702_1511) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2702_1511, [], KL_ARG_V2855_1480]), [setattr(KL_CTX, 'KL_LOC_Result_1512', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1503, KL_CTX.KL_LOC_A_1510, KL_ARG_V2854_1479, KL_ARG_V2855_1480, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1505, [symdic.symdic_kl_list, [KL_CTX.KL_LOC_A_1510, []]], KL_ARG_V2854_1479, KL_ARG_V2855_1480, KL_ARG_V2856_1481]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2702_1511, KL_ARG_V2855_1480]), KL_CTX.KL_LOC_Result_1512][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2702_1511]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2701_1509) else ([setattr(KL_CTX, 'KL_LOC_A_1513', tco_apply(shen_newpv, [KL_ARG_V2855_1480])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2701_1509, [KL_CTX.KL_LOC_A_1513, []], KL_ARG_V2855_1480]), [setattr(KL_CTX, 'KL_LOC_Result_1514', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1503, KL_CTX.KL_LOC_A_1513, KL_ARG_V2854_1479, KL_ARG_V2855_1480, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1505, [symdic.symdic_kl_list, [KL_CTX.KL_LOC_A_1513, []]], KL_ARG_V2854_1479, KL_ARG_V2855_1480, KL_ARG_V2856_1481]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2701_1509, KL_ARG_V2855_1480]), KL_CTX.KL_LOC_Result_1514][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2701_1509]) else False))][(-1)] if (symdic.symdic_kl_list == KL_CTX.KL_LOC_V2700_1508) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2700_1508, symdic.symdic_kl_list, KL_ARG_V2855_1480]), [setattr(KL_CTX, 'KL_LOC_Result_1515', [setattr(KL_CTX, 'KL_LOC_V2703_1516', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2699_1507[1], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_A_1517', KL_CTX.KL_LOC_V2703_1516[0]), [setattr(KL_CTX, 'KL_LOC_V2704_1518', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2703_1516[1], KL_ARG_V2855_1480])), ([tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1503, KL_CTX.KL_LOC_A_1517, KL_ARG_V2854_1479, KL_ARG_V2855_1480, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1505, [symdic.symdic_kl_list, [KL_CTX.KL_LOC_A_1517, []]], KL_ARG_V2854_1479, KL_ARG_V2855_1480, KL_ARG_V2856_1481]))])][(-1)] if ([] == KL_CTX.KL_LOC_V2704_1518) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2704_1518, [], KL_ARG_V2855_1480]), [setattr(KL_CTX, 'KL_LOC_Result_1519', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1503, KL_CTX.KL_LOC_A_1517, KL_ARG_V2854_1479, KL_ARG_V2855_1480, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1505, [symdic.symdic_kl_list, [KL_CTX.KL_LOC_A_1517, []]], KL_ARG_V2854_1479, KL_ARG_V2855_1480, KL_ARG_V2856_1481]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2704_1518, KL_ARG_V2855_1480]), KL_CTX.KL_LOC_Result_1519][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2704_1518]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2703_1516) else ([setattr(KL_CTX, 'KL_LOC_A_1520', tco_apply(shen_newpv, [KL_ARG_V2855_1480])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2703_1516, [KL_CTX.KL_LOC_A_1520, []], KL_ARG_V2855_1480]), [setattr(KL_CTX, 'KL_LOC_Result_1521', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1503, KL_CTX.KL_LOC_A_1520, KL_ARG_V2854_1479, KL_ARG_V2855_1480, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1505, [symdic.symdic_kl_list, [KL_CTX.KL_LOC_A_1520, []]], KL_ARG_V2854_1479, KL_ARG_V2855_1480, KL_ARG_V2856_1481]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2703_1516, KL_ARG_V2855_1480]), KL_CTX.KL_LOC_Result_1521][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2703_1516]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2700_1508, KL_ARG_V2855_1480]), KL_CTX.KL_LOC_Result_1515][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2700_1508]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2699_1507) else ([setattr(KL_CTX, 'KL_LOC_A_1522', tco_apply(shen_newpv, [KL_ARG_V2855_1480])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2699_1507, [symdic.symdic_kl_list, [KL_CTX.KL_LOC_A_1522, []]], KL_ARG_V2855_1480]), [setattr(KL_CTX, 'KL_LOC_Result_1523', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1503, KL_CTX.KL_LOC_A_1522, KL_ARG_V2854_1479, KL_ARG_V2855_1480, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1505, [symdic.symdic_kl_list, [KL_CTX.KL_LOC_A_1522, []]], KL_ARG_V2854_1479, KL_ARG_V2855_1480, KL_ARG_V2856_1481]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2699_1507, KL_ARG_V2855_1480]), KL_CTX.KL_LOC_Result_1523][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2699_1507]) else False))][(-1)] if ([] == KL_CTX.KL_LOC_V2698_1506) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2697_1504) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2696_1502) else False)][(-1)] if (symdic.symdic_kl_cons == KL_CTX.KL_LOC_V2695_1501) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2694_1500) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1524', [setattr(KL_CTX, 'KL_LOC_V2705_1525', tco_apply(shen_lazyderef, [KL_ARG_V2852_1477, KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_V2706_1526', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2705_1525[0], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_V2707_1527', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2705_1525[1], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_X_1528', KL_CTX.KL_LOC_V2707_1527[0]), [setattr(KL_CTX, 'KL_LOC_V2708_1529', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2707_1527[1], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_Y_1530', KL_CTX.KL_LOC_V2708_1529[0]), [setattr(KL_CTX, 'KL_LOC_V2709_1531', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2708_1529[1], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_V2710_1532', tco_apply(shen_lazyderef, [KL_ARG_V2853_1478, KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_A_1533', KL_CTX.KL_LOC_V2710_1532[0]), [setattr(KL_CTX, 'KL_LOC_V2711_1534', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2710_1532[1], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_V2712_1535', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2711_1534[0], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_V2713_1536', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2711_1534[1], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_B_1537', KL_CTX.KL_LOC_V2713_1536[0]), [setattr(KL_CTX, 'KL_LOC_V2714_1538', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2713_1536[1], KL_ARG_V2855_1480])), ([tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1528, KL_CTX.KL_LOC_A_1533, KL_ARG_V2854_1479, KL_ARG_V2855_1480, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1530, KL_CTX.KL_LOC_B_1537, KL_ARG_V2854_1479, KL_ARG_V2855_1480, KL_ARG_V2856_1481]))])][(-1)] if ([] == KL_CTX.KL_LOC_V2714_1538) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2714_1538, [], KL_ARG_V2855_1480]), [setattr(KL_CTX, 'KL_LOC_Result_1539', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1528, KL_CTX.KL_LOC_A_1533, KL_ARG_V2854_1479, KL_ARG_V2855_1480, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1530, KL_CTX.KL_LOC_B_1537, KL_ARG_V2854_1479, KL_ARG_V2855_1480, KL_ARG_V2856_1481]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2714_1538, KL_ARG_V2855_1480]), KL_CTX.KL_LOC_Result_1539][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2714_1538]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2713_1536) else ([setattr(KL_CTX, 'KL_LOC_B_1540', tco_apply(shen_newpv, [KL_ARG_V2855_1480])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2713_1536, [KL_CTX.KL_LOC_B_1540, []], KL_ARG_V2855_1480]), [setattr(KL_CTX, 'KL_LOC_Result_1541', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1528, KL_CTX.KL_LOC_A_1533, KL_ARG_V2854_1479, KL_ARG_V2855_1480, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1530, KL_CTX.KL_LOC_B_1540, KL_ARG_V2854_1479, KL_ARG_V2855_1480, KL_ARG_V2856_1481]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2713_1536, KL_ARG_V2855_1480]), KL_CTX.KL_LOC_Result_1541][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2713_1536]) else False))][(-1)] if (symdic.symdic_kl_x42 == KL_CTX.KL_LOC_V2712_1535) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2712_1535, symdic.symdic_kl_x42, KL_ARG_V2855_1480]), [setattr(KL_CTX, 'KL_LOC_Result_1542', [setattr(KL_CTX, 'KL_LOC_V2715_1543', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2711_1534[1], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_B_1544', KL_CTX.KL_LOC_V2715_1543[0]), [setattr(KL_CTX, 'KL_LOC_V2716_1545', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2715_1543[1], KL_ARG_V2855_1480])), ([tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1528, KL_CTX.KL_LOC_A_1533, KL_ARG_V2854_1479, KL_ARG_V2855_1480, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1530, KL_CTX.KL_LOC_B_1544, KL_ARG_V2854_1479, KL_ARG_V2855_1480, KL_ARG_V2856_1481]))])][(-1)] if ([] == KL_CTX.KL_LOC_V2716_1545) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2716_1545, [], KL_ARG_V2855_1480]), [setattr(KL_CTX, 'KL_LOC_Result_1546', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1528, KL_CTX.KL_LOC_A_1533, KL_ARG_V2854_1479, KL_ARG_V2855_1480, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1530, KL_CTX.KL_LOC_B_1544, KL_ARG_V2854_1479, KL_ARG_V2855_1480, KL_ARG_V2856_1481]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2716_1545, KL_ARG_V2855_1480]), KL_CTX.KL_LOC_Result_1546][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2716_1545]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2715_1543) else ([setattr(KL_CTX, 'KL_LOC_B_1547', tco_apply(shen_newpv, [KL_ARG_V2855_1480])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2715_1543, [KL_CTX.KL_LOC_B_1547, []], KL_ARG_V2855_1480]), [setattr(KL_CTX, 'KL_LOC_Result_1548', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1528, KL_CTX.KL_LOC_A_1533, KL_ARG_V2854_1479, KL_ARG_V2855_1480, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1530, KL_CTX.KL_LOC_B_1547, KL_ARG_V2854_1479, KL_ARG_V2855_1480, KL_ARG_V2856_1481]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2715_1543, KL_ARG_V2855_1480]), KL_CTX.KL_LOC_Result_1548][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2715_1543]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2712_1535, KL_ARG_V2855_1480]), KL_CTX.KL_LOC_Result_1542][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2712_1535]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2711_1534) else ([setattr(KL_CTX, 'KL_LOC_B_1549', tco_apply(shen_newpv, [KL_ARG_V2855_1480])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2711_1534, [symdic.symdic_kl_x42, [KL_CTX.KL_LOC_B_1549, []]], KL_ARG_V2855_1480]), [setattr(KL_CTX, 'KL_LOC_Result_1550', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1528, KL_CTX.KL_LOC_A_1533, KL_ARG_V2854_1479, KL_ARG_V2855_1480, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1530, KL_CTX.KL_LOC_B_1549, KL_ARG_V2854_1479, KL_ARG_V2855_1480, KL_ARG_V2856_1481]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2711_1534, KL_ARG_V2855_1480]), KL_CTX.KL_LOC_Result_1550][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2711_1534]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2710_1532) else ([setattr(KL_CTX, 'KL_LOC_A_1551', tco_apply(shen_newpv, [KL_ARG_V2855_1480])), [setattr(KL_CTX, 'KL_LOC_B_1552', tco_apply(shen_newpv, [KL_ARG_V2855_1480])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2710_1532, [KL_CTX.KL_LOC_A_1551, [symdic.symdic_kl_x42, [KL_CTX.KL_LOC_B_1552, []]]], KL_ARG_V2855_1480]), [setattr(KL_CTX, 'KL_LOC_Result_1553', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1528, KL_CTX.KL_LOC_A_1551, KL_ARG_V2854_1479, KL_ARG_V2855_1480, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1530, KL_CTX.KL_LOC_B_1552, KL_ARG_V2854_1479, KL_ARG_V2855_1480, KL_ARG_V2856_1481]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2710_1532, KL_ARG_V2855_1480]), KL_CTX.KL_LOC_Result_1553][(-1)]][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2710_1532]) else False))][(-1)] if ([] == KL_CTX.KL_LOC_V2709_1531) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2708_1529) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2707_1527) else False)][(-1)] if (symdic.symdic_kl_x64p == KL_CTX.KL_LOC_V2706_1526) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2705_1525) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1554', [setattr(KL_CTX, 'KL_LOC_V2717_1555', tco_apply(shen_lazyderef, [KL_ARG_V2852_1477, KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_V2718_1556', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2717_1555[0], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_V2719_1557', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2717_1555[1], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_X_1558', KL_CTX.KL_LOC_V2719_1557[0]), [setattr(KL_CTX, 'KL_LOC_V2720_1559', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2719_1557[1], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_Y_1560', KL_CTX.KL_LOC_V2720_1559[0]), [setattr(KL_CTX, 'KL_LOC_V2721_1561', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2720_1559[1], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_V2722_1562', tco_apply(shen_lazyderef, [KL_ARG_V2853_1478, KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_V2723_1563', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2722_1562[0], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_V2724_1564', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2722_1562[1], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_A_1565', KL_CTX.KL_LOC_V2724_1564[0]), [setattr(KL_CTX, 'KL_LOC_V2725_1566', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2724_1564[1], KL_ARG_V2855_1480])), ([tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1558, KL_CTX.KL_LOC_A_1565, KL_ARG_V2854_1479, KL_ARG_V2855_1480, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1560, [symdic.symdic_kl_vector, [KL_CTX.KL_LOC_A_1565, []]], KL_ARG_V2854_1479, KL_ARG_V2855_1480, KL_ARG_V2856_1481]))])][(-1)] if ([] == KL_CTX.KL_LOC_V2725_1566) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2725_1566, [], KL_ARG_V2855_1480]), [setattr(KL_CTX, 'KL_LOC_Result_1567', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1558, KL_CTX.KL_LOC_A_1565, KL_ARG_V2854_1479, KL_ARG_V2855_1480, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1560, [symdic.symdic_kl_vector, [KL_CTX.KL_LOC_A_1565, []]], KL_ARG_V2854_1479, KL_ARG_V2855_1480, KL_ARG_V2856_1481]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2725_1566, KL_ARG_V2855_1480]), KL_CTX.KL_LOC_Result_1567][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2725_1566]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2724_1564) else ([setattr(KL_CTX, 'KL_LOC_A_1568', tco_apply(shen_newpv, [KL_ARG_V2855_1480])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2724_1564, [KL_CTX.KL_LOC_A_1568, []], KL_ARG_V2855_1480]), [setattr(KL_CTX, 'KL_LOC_Result_1569', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1558, KL_CTX.KL_LOC_A_1568, KL_ARG_V2854_1479, KL_ARG_V2855_1480, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1560, [symdic.symdic_kl_vector, [KL_CTX.KL_LOC_A_1568, []]], KL_ARG_V2854_1479, KL_ARG_V2855_1480, KL_ARG_V2856_1481]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2724_1564, KL_ARG_V2855_1480]), KL_CTX.KL_LOC_Result_1569][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2724_1564]) else False))][(-1)] if (symdic.symdic_kl_vector == KL_CTX.KL_LOC_V2723_1563) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2723_1563, symdic.symdic_kl_vector, KL_ARG_V2855_1480]), [setattr(KL_CTX, 'KL_LOC_Result_1570', [setattr(KL_CTX, 'KL_LOC_V2726_1571', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2722_1562[1], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_A_1572', KL_CTX.KL_LOC_V2726_1571[0]), [setattr(KL_CTX, 'KL_LOC_V2727_1573', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2726_1571[1], KL_ARG_V2855_1480])), ([tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1558, KL_CTX.KL_LOC_A_1572, KL_ARG_V2854_1479, KL_ARG_V2855_1480, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1560, [symdic.symdic_kl_vector, [KL_CTX.KL_LOC_A_1572, []]], KL_ARG_V2854_1479, KL_ARG_V2855_1480, KL_ARG_V2856_1481]))])][(-1)] if ([] == KL_CTX.KL_LOC_V2727_1573) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2727_1573, [], KL_ARG_V2855_1480]), [setattr(KL_CTX, 'KL_LOC_Result_1574', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1558, KL_CTX.KL_LOC_A_1572, KL_ARG_V2854_1479, KL_ARG_V2855_1480, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1560, [symdic.symdic_kl_vector, [KL_CTX.KL_LOC_A_1572, []]], KL_ARG_V2854_1479, KL_ARG_V2855_1480, KL_ARG_V2856_1481]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2727_1573, KL_ARG_V2855_1480]), KL_CTX.KL_LOC_Result_1574][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2727_1573]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2726_1571) else ([setattr(KL_CTX, 'KL_LOC_A_1575', tco_apply(shen_newpv, [KL_ARG_V2855_1480])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2726_1571, [KL_CTX.KL_LOC_A_1575, []], KL_ARG_V2855_1480]), [setattr(KL_CTX, 'KL_LOC_Result_1576', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1558, KL_CTX.KL_LOC_A_1575, KL_ARG_V2854_1479, KL_ARG_V2855_1480, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1560, [symdic.symdic_kl_vector, [KL_CTX.KL_LOC_A_1575, []]], KL_ARG_V2854_1479, KL_ARG_V2855_1480, KL_ARG_V2856_1481]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2726_1571, KL_ARG_V2855_1480]), KL_CTX.KL_LOC_Result_1576][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2726_1571]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2723_1563, KL_ARG_V2855_1480]), KL_CTX.KL_LOC_Result_1570][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2723_1563]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2722_1562) else ([setattr(KL_CTX, 'KL_LOC_A_1577', tco_apply(shen_newpv, [KL_ARG_V2855_1480])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2722_1562, [symdic.symdic_kl_vector, [KL_CTX.KL_LOC_A_1577, []]], KL_ARG_V2855_1480]), [setattr(KL_CTX, 'KL_LOC_Result_1578', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1558, KL_CTX.KL_LOC_A_1577, KL_ARG_V2854_1479, KL_ARG_V2855_1480, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1560, [symdic.symdic_kl_vector, [KL_CTX.KL_LOC_A_1577, []]], KL_ARG_V2854_1479, KL_ARG_V2855_1480, KL_ARG_V2856_1481]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2722_1562, KL_ARG_V2855_1480]), KL_CTX.KL_LOC_Result_1578][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2722_1562]) else False))][(-1)] if ([] == KL_CTX.KL_LOC_V2721_1561) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2720_1559) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2719_1557) else False)][(-1)] if (symdic.symdic_kl_x64v == KL_CTX.KL_LOC_V2718_1556) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2717_1555) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1579', [setattr(KL_CTX, 'KL_LOC_V2728_1580', tco_apply(shen_lazyderef, [KL_ARG_V2852_1477, KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_V2729_1581', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2728_1580[0], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_V2730_1582', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2728_1580[1], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_X_1583', KL_CTX.KL_LOC_V2730_1582[0]), [setattr(KL_CTX, 'KL_LOC_V2731_1584', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2730_1582[1], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_Y_1585', KL_CTX.KL_LOC_V2731_1584[0]), [setattr(KL_CTX, 'KL_LOC_V2732_1586', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2731_1584[1], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_V2733_1587', tco_apply(shen_lazyderef, [KL_ARG_V2853_1478, KL_ARG_V2855_1480])), ([tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1583, symdic.symdic_kl_string, KL_ARG_V2854_1479, KL_ARG_V2855_1480, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1585, symdic.symdic_kl_string, KL_ARG_V2854_1479, KL_ARG_V2855_1480, KL_ARG_V2856_1481]))])][(-1)] if (symdic.symdic_kl_string == KL_CTX.KL_LOC_V2733_1587) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2733_1587, symdic.symdic_kl_string, KL_ARG_V2855_1480]), [setattr(KL_CTX, 'KL_LOC_Result_1588', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1583, symdic.symdic_kl_string, KL_ARG_V2854_1479, KL_ARG_V2855_1480, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1585, symdic.symdic_kl_string, KL_ARG_V2854_1479, KL_ARG_V2855_1480, KL_ARG_V2856_1481]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2733_1587, KL_ARG_V2855_1480]), KL_CTX.KL_LOC_Result_1588][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2733_1587]) else False))][(-1)] if ([] == KL_CTX.KL_LOC_V2732_1586) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2731_1584) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2730_1582) else False)][(-1)] if (symdic.symdic_kl_x64s == KL_CTX.KL_LOC_V2729_1581) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2728_1580) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1589', [setattr(KL_CTX, 'KL_LOC_V2734_1590', tco_apply(shen_lazyderef, [KL_ARG_V2852_1477, KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_V2735_1591', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2734_1590[0], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_V2736_1592', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2734_1590[1], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_X_1593', KL_CTX.KL_LOC_V2736_1592[0]), [setattr(KL_CTX, 'KL_LOC_V2737_1594', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2736_1592[1], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_Y_1595', KL_CTX.KL_LOC_V2737_1594[0]), [setattr(KL_CTX, 'KL_LOC_V2738_1596', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2737_1594[1], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_V2739_1597', tco_apply(shen_lazyderef, [KL_ARG_V2853_1478, KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_A_1598', KL_CTX.KL_LOC_V2739_1597[0]), [setattr(KL_CTX, 'KL_LOC_V2740_1599', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2739_1597[1], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_V2741_1600', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2740_1599[0], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_V2742_1601', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2740_1599[1], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_B_1602', KL_CTX.KL_LOC_V2742_1601[0]), [setattr(KL_CTX, 'KL_LOC_V2743_1603', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2742_1601[1], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_Z_1604', tco_apply(shen_newpv, [KL_ARG_V2855_1480])), [setattr(KL_CTX, 'KL_LOC_Xx38x38_1605', tco_apply(shen_newpv, [KL_ARG_V2855_1480])), [tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1482, KL_ARG_V2855_1480, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Xx38x38_1605, tco_apply(shen_placeholder, []), KL_ARG_V2855_1480, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Z_1604, tco_apply(shen_ebr, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Xx38x38_1605, KL_ARG_V2855_1480]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1593, KL_ARG_V2855_1480]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1595, KL_ARG_V2855_1480])]), KL_ARG_V2855_1480, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Z_1604, KL_CTX.KL_LOC_B_1602, [[KL_CTX.KL_LOC_Xx38x38_1605, [symdic.symdic_kl_x58, [KL_CTX.KL_LOC_A_1598, []]]], KL_ARG_V2854_1479], KL_ARG_V2855_1480, KL_ARG_V2856_1481]))]))]))])][(-1)]][(-1)]][(-1)] if ([] == KL_CTX.KL_LOC_V2743_1603) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2743_1603, [], KL_ARG_V2855_1480]), [setattr(KL_CTX, 'KL_LOC_Result_1606', [setattr(KL_CTX, 'KL_LOC_Z_1607', tco_apply(shen_newpv, [KL_ARG_V2855_1480])), [setattr(KL_CTX, 'KL_LOC_Xx38x38_1608', tco_apply(shen_newpv, [KL_ARG_V2855_1480])), [tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1482, KL_ARG_V2855_1480, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Xx38x38_1608, tco_apply(shen_placeholder, []), KL_ARG_V2855_1480, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Z_1607, tco_apply(shen_ebr, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Xx38x38_1608, KL_ARG_V2855_1480]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1593, KL_ARG_V2855_1480]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1595, KL_ARG_V2855_1480])]), KL_ARG_V2855_1480, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Z_1607, KL_CTX.KL_LOC_B_1602, [[KL_CTX.KL_LOC_Xx38x38_1608, [symdic.symdic_kl_x58, [KL_CTX.KL_LOC_A_1598, []]]], KL_ARG_V2854_1479], KL_ARG_V2855_1480, KL_ARG_V2856_1481]))]))]))])][(-1)]][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2743_1603, KL_ARG_V2855_1480]), KL_CTX.KL_LOC_Result_1606][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2743_1603]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2742_1601) else ([setattr(KL_CTX, 'KL_LOC_B_1609', tco_apply(shen_newpv, [KL_ARG_V2855_1480])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2742_1601, [KL_CTX.KL_LOC_B_1609, []], KL_ARG_V2855_1480]), [setattr(KL_CTX, 'KL_LOC_Result_1610', [setattr(KL_CTX, 'KL_LOC_Z_1611', tco_apply(shen_newpv, [KL_ARG_V2855_1480])), [setattr(KL_CTX, 'KL_LOC_Xx38x38_1612', tco_apply(shen_newpv, [KL_ARG_V2855_1480])), [tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1482, KL_ARG_V2855_1480, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Xx38x38_1612, tco_apply(shen_placeholder, []), KL_ARG_V2855_1480, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Z_1611, tco_apply(shen_ebr, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Xx38x38_1612, KL_ARG_V2855_1480]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1593, KL_ARG_V2855_1480]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1595, KL_ARG_V2855_1480])]), KL_ARG_V2855_1480, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Z_1611, KL_CTX.KL_LOC_B_1609, [[KL_CTX.KL_LOC_Xx38x38_1612, [symdic.symdic_kl_x58, [KL_CTX.KL_LOC_A_1598, []]]], KL_ARG_V2854_1479], KL_ARG_V2855_1480, KL_ARG_V2856_1481]))]))]))])][(-1)]][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2742_1601, KL_ARG_V2855_1480]), KL_CTX.KL_LOC_Result_1610][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2742_1601]) else False))][(-1)] if (symdic.symdic_kl_x45x45x62 == KL_CTX.KL_LOC_V2741_1600) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2741_1600, symdic.symdic_kl_x45x45x62, KL_ARG_V2855_1480]), [setattr(KL_CTX, 'KL_LOC_Result_1613', [setattr(KL_CTX, 'KL_LOC_V2744_1614', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2740_1599[1], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_B_1615', KL_CTX.KL_LOC_V2744_1614[0]), [setattr(KL_CTX, 'KL_LOC_V2745_1616', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2744_1614[1], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_Z_1617', tco_apply(shen_newpv, [KL_ARG_V2855_1480])), [setattr(KL_CTX, 'KL_LOC_Xx38x38_1618', tco_apply(shen_newpv, [KL_ARG_V2855_1480])), [tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1482, KL_ARG_V2855_1480, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Xx38x38_1618, tco_apply(shen_placeholder, []), KL_ARG_V2855_1480, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Z_1617, tco_apply(shen_ebr, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Xx38x38_1618, KL_ARG_V2855_1480]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1593, KL_ARG_V2855_1480]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1595, KL_ARG_V2855_1480])]), KL_ARG_V2855_1480, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Z_1617, KL_CTX.KL_LOC_B_1615, [[KL_CTX.KL_LOC_Xx38x38_1618, [symdic.symdic_kl_x58, [KL_CTX.KL_LOC_A_1598, []]]], KL_ARG_V2854_1479], KL_ARG_V2855_1480, KL_ARG_V2856_1481]))]))]))])][(-1)]][(-1)]][(-1)] if ([] == KL_CTX.KL_LOC_V2745_1616) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2745_1616, [], KL_ARG_V2855_1480]), [setattr(KL_CTX, 'KL_LOC_Result_1619', [setattr(KL_CTX, 'KL_LOC_Z_1620', tco_apply(shen_newpv, [KL_ARG_V2855_1480])), [setattr(KL_CTX, 'KL_LOC_Xx38x38_1621', tco_apply(shen_newpv, [KL_ARG_V2855_1480])), [tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1482, KL_ARG_V2855_1480, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Xx38x38_1621, tco_apply(shen_placeholder, []), KL_ARG_V2855_1480, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Z_1620, tco_apply(shen_ebr, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Xx38x38_1621, KL_ARG_V2855_1480]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1593, KL_ARG_V2855_1480]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1595, KL_ARG_V2855_1480])]), KL_ARG_V2855_1480, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Z_1620, KL_CTX.KL_LOC_B_1615, [[KL_CTX.KL_LOC_Xx38x38_1621, [symdic.symdic_kl_x58, [KL_CTX.KL_LOC_A_1598, []]]], KL_ARG_V2854_1479], KL_ARG_V2855_1480, KL_ARG_V2856_1481]))]))]))])][(-1)]][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2745_1616, KL_ARG_V2855_1480]), KL_CTX.KL_LOC_Result_1619][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2745_1616]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2744_1614) else ([setattr(KL_CTX, 'KL_LOC_B_1622', tco_apply(shen_newpv, [KL_ARG_V2855_1480])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2744_1614, [KL_CTX.KL_LOC_B_1622, []], KL_ARG_V2855_1480]), [setattr(KL_CTX, 'KL_LOC_Result_1623', [setattr(KL_CTX, 'KL_LOC_Z_1624', tco_apply(shen_newpv, [KL_ARG_V2855_1480])), [setattr(KL_CTX, 'KL_LOC_Xx38x38_1625', tco_apply(shen_newpv, [KL_ARG_V2855_1480])), [tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1482, KL_ARG_V2855_1480, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Xx38x38_1625, tco_apply(shen_placeholder, []), KL_ARG_V2855_1480, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Z_1624, tco_apply(shen_ebr, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Xx38x38_1625, KL_ARG_V2855_1480]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1593, KL_ARG_V2855_1480]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1595, KL_ARG_V2855_1480])]), KL_ARG_V2855_1480, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Z_1624, KL_CTX.KL_LOC_B_1622, [[KL_CTX.KL_LOC_Xx38x38_1625, [symdic.symdic_kl_x58, [KL_CTX.KL_LOC_A_1598, []]]], KL_ARG_V2854_1479], KL_ARG_V2855_1480, KL_ARG_V2856_1481]))]))]))])][(-1)]][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2744_1614, KL_ARG_V2855_1480]), KL_CTX.KL_LOC_Result_1623][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2744_1614]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2741_1600, KL_ARG_V2855_1480]), KL_CTX.KL_LOC_Result_1613][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2741_1600]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2740_1599) else ([setattr(KL_CTX, 'KL_LOC_B_1626', tco_apply(shen_newpv, [KL_ARG_V2855_1480])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2740_1599, [symdic.symdic_kl_x45x45x62, [KL_CTX.KL_LOC_B_1626, []]], KL_ARG_V2855_1480]), [setattr(KL_CTX, 'KL_LOC_Result_1627', [setattr(KL_CTX, 'KL_LOC_Z_1628', tco_apply(shen_newpv, [KL_ARG_V2855_1480])), [setattr(KL_CTX, 'KL_LOC_Xx38x38_1629', tco_apply(shen_newpv, [KL_ARG_V2855_1480])), [tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1482, KL_ARG_V2855_1480, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Xx38x38_1629, tco_apply(shen_placeholder, []), KL_ARG_V2855_1480, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Z_1628, tco_apply(shen_ebr, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Xx38x38_1629, KL_ARG_V2855_1480]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1593, KL_ARG_V2855_1480]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1595, KL_ARG_V2855_1480])]), KL_ARG_V2855_1480, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Z_1628, KL_CTX.KL_LOC_B_1626, [[KL_CTX.KL_LOC_Xx38x38_1629, [symdic.symdic_kl_x58, [KL_CTX.KL_LOC_A_1598, []]]], KL_ARG_V2854_1479], KL_ARG_V2855_1480, KL_ARG_V2856_1481]))]))]))])][(-1)]][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2740_1599, KL_ARG_V2855_1480]), KL_CTX.KL_LOC_Result_1627][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2740_1599]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2739_1597) else ([setattr(KL_CTX, 'KL_LOC_A_1630', tco_apply(shen_newpv, [KL_ARG_V2855_1480])), [setattr(KL_CTX, 'KL_LOC_B_1631', tco_apply(shen_newpv, [KL_ARG_V2855_1480])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2739_1597, [KL_CTX.KL_LOC_A_1630, [symdic.symdic_kl_x45x45x62, [KL_CTX.KL_LOC_B_1631, []]]], KL_ARG_V2855_1480]), [setattr(KL_CTX, 'KL_LOC_Result_1632', [setattr(KL_CTX, 'KL_LOC_Z_1633', tco_apply(shen_newpv, [KL_ARG_V2855_1480])), [setattr(KL_CTX, 'KL_LOC_Xx38x38_1634', tco_apply(shen_newpv, [KL_ARG_V2855_1480])), [tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1482, KL_ARG_V2855_1480, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Xx38x38_1634, tco_apply(shen_placeholder, []), KL_ARG_V2855_1480, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Z_1633, tco_apply(shen_ebr, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Xx38x38_1634, KL_ARG_V2855_1480]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1593, KL_ARG_V2855_1480]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1595, KL_ARG_V2855_1480])]), KL_ARG_V2855_1480, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Z_1633, KL_CTX.KL_LOC_B_1631, [[KL_CTX.KL_LOC_Xx38x38_1634, [symdic.symdic_kl_x58, [KL_CTX.KL_LOC_A_1630, []]]], KL_ARG_V2854_1479], KL_ARG_V2855_1480, KL_ARG_V2856_1481]))]))]))])][(-1)]][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2739_1597, KL_ARG_V2855_1480]), KL_CTX.KL_LOC_Result_1632][(-1)]][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2739_1597]) else False))][(-1)] if ([] == KL_CTX.KL_LOC_V2738_1596) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2737_1594) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2736_1592) else False)][(-1)] if (symdic.symdic_kl_lambda == KL_CTX.KL_LOC_V2735_1591) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2734_1590) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1635', [setattr(KL_CTX, 'KL_LOC_V2746_1636', tco_apply(shen_lazyderef, [KL_ARG_V2852_1477, KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_V2747_1637', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2746_1636[0], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_V2748_1638', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2746_1636[1], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_X_1639', KL_CTX.KL_LOC_V2748_1638[0]), [setattr(KL_CTX, 'KL_LOC_V2749_1640', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2748_1638[1], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_Y_1641', KL_CTX.KL_LOC_V2749_1640[0]), [setattr(KL_CTX, 'KL_LOC_V2750_1642', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2749_1640[1], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_Z_1643', KL_CTX.KL_LOC_V2750_1642[0]), [setattr(KL_CTX, 'KL_LOC_V2751_1644', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2750_1642[1], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_W_1645', tco_apply(shen_newpv, [KL_ARG_V2855_1480])), [setattr(KL_CTX, 'KL_LOC_Xx38x38_1646', tco_apply(shen_newpv, [KL_ARG_V2855_1480])), [setattr(KL_CTX, 'KL_LOC_B_1647', tco_apply(shen_newpv, [KL_ARG_V2855_1480])), [tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1482, KL_ARG_V2855_1480, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1641, KL_CTX.KL_LOC_B_1647, KL_ARG_V2854_1479, KL_ARG_V2855_1480, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Xx38x38_1646, tco_apply(shen_placeholder, []), KL_ARG_V2855_1480, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_W_1645, tco_apply(shen_ebr, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Xx38x38_1646, KL_ARG_V2855_1480]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1639, KL_ARG_V2855_1480]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Z_1643, KL_ARG_V2855_1480])]), KL_ARG_V2855_1480, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_W_1645, KL_ARG_V2853_1478, [[KL_CTX.KL_LOC_Xx38x38_1646, [symdic.symdic_kl_x58, [KL_CTX.KL_LOC_B_1647, []]]], KL_ARG_V2854_1479], KL_ARG_V2855_1480, KL_ARG_V2856_1481]))]))]))]))])][(-1)]][(-1)]][(-1)]][(-1)] if ([] == KL_CTX.KL_LOC_V2751_1644) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2750_1642) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2749_1640) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2748_1638) else False)][(-1)] if (symdic.symdic_kl_let == KL_CTX.KL_LOC_V2747_1637) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2746_1636) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1648', [setattr(KL_CTX, 'KL_LOC_V2752_1649', tco_apply(shen_lazyderef, [KL_ARG_V2852_1477, KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_V2753_1650', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2752_1649[0], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_V2754_1651', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2752_1649[1], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_V2755_1652', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2754_1651[0], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_V2756_1653', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2754_1651[1], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_FileName_1654', KL_CTX.KL_LOC_V2756_1653[0]), [setattr(KL_CTX, 'KL_LOC_V2757_1655', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2756_1653[1], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_Direction2685_1656', KL_CTX.KL_LOC_V2757_1655[0]), [setattr(KL_CTX, 'KL_LOC_V2758_1657', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2757_1655[1], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_V2759_1658', tco_apply(shen_lazyderef, [KL_ARG_V2853_1478, KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_V2760_1659', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2759_1658[0], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_V2761_1660', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2759_1658[1], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_Direction_1661', KL_CTX.KL_LOC_V2761_1660[0]), [setattr(KL_CTX, 'KL_LOC_V2762_1662', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2761_1660[1], KL_ARG_V2855_1480])), ([tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_Direction_1661, KL_CTX.KL_LOC_Direction2685_1656, KL_ARG_V2855_1480, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1482, KL_ARG_V2855_1480, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_FileName_1654, symdic.symdic_kl_string, KL_ARG_V2854_1479, KL_ARG_V2855_1480, KL_ARG_V2856_1481]))]))])][(-1)] if ([] == KL_CTX.KL_LOC_V2762_1662) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2762_1662, [], KL_ARG_V2855_1480]), [setattr(KL_CTX, 'KL_LOC_Result_1663', [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_Direction_1661, KL_CTX.KL_LOC_Direction2685_1656, KL_ARG_V2855_1480, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1482, KL_ARG_V2855_1480, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_FileName_1654, symdic.symdic_kl_string, KL_ARG_V2854_1479, KL_ARG_V2855_1480, KL_ARG_V2856_1481]))]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2762_1662, KL_ARG_V2855_1480]), KL_CTX.KL_LOC_Result_1663][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2762_1662]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2761_1660) else ([setattr(KL_CTX, 'KL_LOC_Direction_1664', tco_apply(shen_newpv, [KL_ARG_V2855_1480])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2761_1660, [KL_CTX.KL_LOC_Direction_1664, []], KL_ARG_V2855_1480]), [setattr(KL_CTX, 'KL_LOC_Result_1665', [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_Direction_1664, KL_CTX.KL_LOC_Direction2685_1656, KL_ARG_V2855_1480, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1482, KL_ARG_V2855_1480, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_FileName_1654, symdic.symdic_kl_string, KL_ARG_V2854_1479, KL_ARG_V2855_1480, KL_ARG_V2856_1481]))]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2761_1660, KL_ARG_V2855_1480]), KL_CTX.KL_LOC_Result_1665][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2761_1660]) else False))][(-1)] if (symdic.symdic_kl_stream == KL_CTX.KL_LOC_V2760_1659) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2760_1659, symdic.symdic_kl_stream, KL_ARG_V2855_1480]), [setattr(KL_CTX, 'KL_LOC_Result_1666', [setattr(KL_CTX, 'KL_LOC_V2763_1667', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2759_1658[1], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_Direction_1668', KL_CTX.KL_LOC_V2763_1667[0]), [setattr(KL_CTX, 'KL_LOC_V2764_1669', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2763_1667[1], KL_ARG_V2855_1480])), ([tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_Direction_1668, KL_CTX.KL_LOC_Direction2685_1656, KL_ARG_V2855_1480, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1482, KL_ARG_V2855_1480, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_FileName_1654, symdic.symdic_kl_string, KL_ARG_V2854_1479, KL_ARG_V2855_1480, KL_ARG_V2856_1481]))]))])][(-1)] if ([] == KL_CTX.KL_LOC_V2764_1669) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2764_1669, [], KL_ARG_V2855_1480]), [setattr(KL_CTX, 'KL_LOC_Result_1670', [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_Direction_1668, KL_CTX.KL_LOC_Direction2685_1656, KL_ARG_V2855_1480, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1482, KL_ARG_V2855_1480, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_FileName_1654, symdic.symdic_kl_string, KL_ARG_V2854_1479, KL_ARG_V2855_1480, KL_ARG_V2856_1481]))]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2764_1669, KL_ARG_V2855_1480]), KL_CTX.KL_LOC_Result_1670][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2764_1669]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2763_1667) else ([setattr(KL_CTX, 'KL_LOC_Direction_1671', tco_apply(shen_newpv, [KL_ARG_V2855_1480])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2763_1667, [KL_CTX.KL_LOC_Direction_1671, []], KL_ARG_V2855_1480]), [setattr(KL_CTX, 'KL_LOC_Result_1672', [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_Direction_1671, KL_CTX.KL_LOC_Direction2685_1656, KL_ARG_V2855_1480, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1482, KL_ARG_V2855_1480, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_FileName_1654, symdic.symdic_kl_string, KL_ARG_V2854_1479, KL_ARG_V2855_1480, KL_ARG_V2856_1481]))]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2763_1667, KL_ARG_V2855_1480]), KL_CTX.KL_LOC_Result_1672][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2763_1667]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2760_1659, KL_ARG_V2855_1480]), KL_CTX.KL_LOC_Result_1666][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2760_1659]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2759_1658) else ([setattr(KL_CTX, 'KL_LOC_Direction_1673', tco_apply(shen_newpv, [KL_ARG_V2855_1480])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2759_1658, [symdic.symdic_kl_stream, [KL_CTX.KL_LOC_Direction_1673, []]], KL_ARG_V2855_1480]), [setattr(KL_CTX, 'KL_LOC_Result_1674', [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_Direction_1673, KL_CTX.KL_LOC_Direction2685_1656, KL_ARG_V2855_1480, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1482, KL_ARG_V2855_1480, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_FileName_1654, symdic.symdic_kl_string, KL_ARG_V2854_1479, KL_ARG_V2855_1480, KL_ARG_V2856_1481]))]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2759_1658, KL_ARG_V2855_1480]), KL_CTX.KL_LOC_Result_1674][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2759_1658]) else False))][(-1)] if ([] == KL_CTX.KL_LOC_V2758_1657) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2757_1655) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2756_1653) else False)][(-1)] if (symdic.symdic_kl_file == KL_CTX.KL_LOC_V2755_1652) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2754_1651) else False)][(-1)] if (symdic.symdic_kl_open == KL_CTX.KL_LOC_V2753_1650) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2752_1649) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1675', [setattr(KL_CTX, 'KL_LOC_V2765_1676', tco_apply(shen_lazyderef, [KL_ARG_V2852_1477, KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_V2766_1677', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2765_1676[0], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_V2767_1678', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2765_1676[1], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_X_1679', KL_CTX.KL_LOC_V2767_1678[0]), [setattr(KL_CTX, 'KL_LOC_V2768_1680', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2767_1678[1], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_A_1681', KL_CTX.KL_LOC_V2768_1680[0]), [setattr(KL_CTX, 'KL_LOC_V2769_1682', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2768_1680[1], KL_ARG_V2855_1480])), ([tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1482, KL_ARG_V2855_1480, (lambda : tail_call(kl_unify, [KL_CTX.KL_LOC_A_1681, KL_ARG_V2853_1478, KL_ARG_V2855_1480, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_X_1679, KL_CTX.KL_LOC_A_1681, KL_ARG_V2854_1479, KL_ARG_V2855_1480, KL_ARG_V2856_1481]))]))])][(-1)] if ([] == KL_CTX.KL_LOC_V2769_1682) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2768_1680) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2767_1678) else False)][(-1)] if (symdic.symdic_kl_type == KL_CTX.KL_LOC_V2766_1677) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2765_1676) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1683', [setattr(KL_CTX, 'KL_LOC_V2770_1684', tco_apply(shen_lazyderef, [KL_ARG_V2852_1477, KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_V2771_1685', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2770_1684[0], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_V2772_1686', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2770_1684[1], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_V2773_1687', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2772_1686[0], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_V2774_1688', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2772_1686[1], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_A_1689', KL_CTX.KL_LOC_V2774_1688[0]), [setattr(KL_CTX, 'KL_LOC_V2775_1690', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2774_1688[1], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_C_1691', tco_apply(shen_newpv, [KL_ARG_V2855_1480])), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_CTX.KL_LOC_C_1691, tco_apply(shen_demodulate, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1689, KL_ARG_V2855_1480])]), KL_ARG_V2855_1480, (lambda : tail_call(kl_unify, [KL_ARG_V2853_1478, KL_CTX.KL_LOC_C_1691, KL_ARG_V2855_1480, KL_ARG_V2856_1481]))])][(-1)]][(-1)] if ([] == KL_CTX.KL_LOC_V2775_1690) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2774_1688) else False)][(-1)] if (symdic.symdic_kl_x58 == KL_CTX.KL_LOC_V2773_1687) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2772_1686) else False)][(-1)] if (symdic.symdic_kl_inputx43 == KL_CTX.KL_LOC_V2771_1685) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2770_1684) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1692', [setattr(KL_CTX, 'KL_LOC_V2776_1693', tco_apply(shen_lazyderef, [KL_ARG_V2852_1477, KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_V2777_1694', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2776_1693[0], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_V2778_1695', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2776_1693[1], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_V2779_1696', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2778_1695[0], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_V2780_1697', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2778_1695[1], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_A_1698', KL_CTX.KL_LOC_V2780_1697[0]), [setattr(KL_CTX, 'KL_LOC_V2781_1699', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2780_1697[1], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_C_1700', tco_apply(shen_newpv, [KL_ARG_V2855_1480])), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_CTX.KL_LOC_C_1700, tco_apply(shen_demodulate, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1698, KL_ARG_V2855_1480])]), KL_ARG_V2855_1480, (lambda : tail_call(kl_unify, [KL_ARG_V2853_1478, KL_CTX.KL_LOC_C_1700, KL_ARG_V2855_1480, KL_ARG_V2856_1481]))])][(-1)]][(-1)] if ([] == KL_CTX.KL_LOC_V2781_1699) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2780_1697) else False)][(-1)] if (symdic.symdic_kl_x58 == KL_CTX.KL_LOC_V2779_1696) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2778_1695) else False)][(-1)] if (symdic.symdic_readx43 == KL_CTX.KL_LOC_V2777_1694) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2776_1693) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1701', [setattr(KL_CTX, 'KL_LOC_V2782_1702', tco_apply(shen_lazyderef, [KL_ARG_V2852_1477, KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_V2783_1703', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2782_1702[0], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_V2784_1704', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2782_1702[1], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_Var_1705', KL_CTX.KL_LOC_V2784_1704[0]), [setattr(KL_CTX, 'KL_LOC_V2785_1706', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2784_1704[1], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_Val_1707', KL_CTX.KL_LOC_V2785_1706[0]), [setattr(KL_CTX, 'KL_LOC_V2786_1708', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2785_1706[1], KL_ARG_V2855_1480])), ([tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1482, KL_ARG_V2855_1480, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Var_1705, symdic.symdic_kl_symbol, KL_ARG_V2854_1479, KL_ARG_V2855_1480, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1482, KL_ARG_V2855_1480, (lambda : tail_call(shen_thx42, [[symdic.symdic_kl_value, [KL_CTX.KL_LOC_Var_1705, []]], KL_ARG_V2853_1478, KL_ARG_V2854_1479, KL_ARG_V2855_1480, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Val_1707, KL_ARG_V2853_1478, KL_ARG_V2854_1479, KL_ARG_V2855_1480, KL_ARG_V2856_1481]))]))]))]))])][(-1)] if ([] == KL_CTX.KL_LOC_V2786_1708) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2785_1706) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2784_1704) else False)][(-1)] if (symdic.symdic_kl_set == KL_CTX.KL_LOC_V2783_1703) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2782_1702) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1709', [setattr(KL_CTX, 'KL_LOC_V2787_1710', tco_apply(shen_lazyderef, [KL_ARG_V2852_1477, KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_V2788_1711', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2787_1710[0], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_V2789_1712', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2787_1710[1], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_F_1713', KL_CTX.KL_LOC_V2789_1712[0]), [setattr(KL_CTX, 'KL_LOC_V2790_1714', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2789_1712[1], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_A_1715', tco_apply(shen_newpv, [KL_ARG_V2855_1480])), [setattr(KL_CTX, 'KL_LOC_Fx38x38_1716', tco_apply(shen_newpv, [KL_ARG_V2855_1480])), [setattr(KL_CTX, 'KL_LOC_B_1717', tco_apply(shen_newpv, [KL_ARG_V2855_1480])), [tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1482, KL_ARG_V2855_1480, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_F_1713, [KL_CTX.KL_LOC_A_1715, [symdic.symdic_kl_x61x61x62, [KL_CTX.KL_LOC_B_1717, []]]], KL_ARG_V2854_1479, KL_ARG_V2855_1480, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1482, KL_ARG_V2855_1480, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Fx38x38_1716, tco_apply(kl_concat, [symdic.symdic_kl_x38x38, tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_F_1713, KL_ARG_V2855_1480])]), KL_ARG_V2855_1480, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1482, KL_ARG_V2855_1480, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Fx38x38_1716, KL_ARG_V2853_1478, [[KL_CTX.KL_LOC_Fx38x38_1716, [symdic.symdic_kl_x58, [KL_CTX.KL_LOC_B_1717, []]]], KL_ARG_V2854_1479], KL_ARG_V2855_1480, KL_ARG_V2856_1481]))]))]))]))]))])][(-1)]][(-1)]][(-1)]][(-1)] if ([] == KL_CTX.KL_LOC_V2790_1714) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2789_1712) else False)][(-1)] if (symdic.symdic_shen_x60x45sem == KL_CTX.KL_LOC_V2788_1711) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2787_1710) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1718', [setattr(KL_CTX, 'KL_LOC_V2791_1719', tco_apply(shen_lazyderef, [KL_ARG_V2852_1477, KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_V2792_1720', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2791_1719[0], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_V2793_1721', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2791_1719[1], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_V2794_1722', tco_apply(shen_lazyderef, [KL_ARG_V2853_1478, KL_ARG_V2855_1480])), ([tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V2856_1481])][(-1)] if (symdic.symdic_kl_symbol == KL_CTX.KL_LOC_V2794_1722) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2794_1722, symdic.symdic_kl_symbol, KL_ARG_V2855_1480]), [setattr(KL_CTX, 'KL_LOC_Result_1723', [tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V2856_1481])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2794_1722, KL_ARG_V2855_1480]), KL_CTX.KL_LOC_Result_1723][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2794_1722]) else False))][(-1)] if ([] == KL_CTX.KL_LOC_V2793_1721) else False)][(-1)] if (symdic.symdic_kl_fail == KL_CTX.KL_LOC_V2792_1720) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2791_1719) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1724', [setattr(KL_CTX, 'KL_LOC_NewHyp_1725', tco_apply(shen_newpv, [KL_ARG_V2855_1480])), [tco_apply(shen_incinfs, []), tco_apply(shen_tx42x45hyps, [KL_ARG_V2854_1479, KL_CTX.KL_LOC_NewHyp_1725, KL_ARG_V2855_1480, (lambda : tail_call(shen_thx42, [KL_ARG_V2852_1477, KL_ARG_V2853_1478, KL_CTX.KL_LOC_NewHyp_1725, KL_ARG_V2855_1480, KL_ARG_V2856_1481]))])][(-1)]][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1726', [setattr(KL_CTX, 'KL_LOC_V2795_1727', tco_apply(shen_lazyderef, [KL_ARG_V2852_1477, KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_V2796_1728', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2795_1727[0], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_V2797_1729', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2795_1727[1], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_F_1730', KL_CTX.KL_LOC_V2797_1729[0]), [setattr(KL_CTX, 'KL_LOC_X_1731', KL_CTX.KL_LOC_V2797_1729[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1482, KL_ARG_V2855_1480, (lambda : tail_call(shen_tx42x45def, [[symdic.symdic_kl_define, [KL_CTX.KL_LOC_F_1730, KL_CTX.KL_LOC_X_1731]], KL_ARG_V2853_1478, KL_ARG_V2854_1479, KL_ARG_V2855_1480, KL_ARG_V2856_1481]))])][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2797_1729) else False)][(-1)] if (symdic.symdic_kl_define == KL_CTX.KL_LOC_V2796_1728) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2795_1727) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1732', [setattr(KL_CTX, 'KL_LOC_V2798_1733', tco_apply(shen_lazyderef, [KL_ARG_V2852_1477, KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_V2799_1734', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2798_1733[0], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_V2800_1735', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2798_1733[1], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_F_1736', KL_CTX.KL_LOC_V2800_1735[0]), [setattr(KL_CTX, 'KL_LOC_X_1737', KL_CTX.KL_LOC_V2800_1735[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1482, KL_ARG_V2855_1480, (lambda : tail_call(shen_tx42x45defcc, [[symdic.symdic_kl_defcc, [KL_CTX.KL_LOC_F_1736, KL_CTX.KL_LOC_X_1737]], KL_ARG_V2853_1478, KL_ARG_V2854_1479, KL_ARG_V2855_1480, KL_ARG_V2856_1481]))])][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2800_1735) else False)][(-1)] if (symdic.symdic_kl_defcc == KL_CTX.KL_LOC_V2799_1734) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2798_1733) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1738', [setattr(KL_CTX, 'KL_LOC_V2801_1739', tco_apply(shen_lazyderef, [KL_ARG_V2852_1477, KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_V2802_1740', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2801_1739[0], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_V2803_1741', tco_apply(shen_lazyderef, [KL_ARG_V2853_1478, KL_ARG_V2855_1480])), ([tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1482, KL_ARG_V2855_1480, KL_ARG_V2856_1481])][(-1)] if (symdic.symdic_kl_unit == KL_CTX.KL_LOC_V2803_1741) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2803_1741, symdic.symdic_kl_unit, KL_ARG_V2855_1480]), [setattr(KL_CTX, 'KL_LOC_Result_1742', [tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1482, KL_ARG_V2855_1480, KL_ARG_V2856_1481])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2803_1741, KL_ARG_V2855_1480]), KL_CTX.KL_LOC_Result_1742][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2803_1741]) else False))][(-1)] if (symdic.symdic_kl_defmacro == KL_CTX.KL_LOC_V2802_1740) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2801_1739) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1743', [setattr(KL_CTX, 'KL_LOC_V2804_1744', tco_apply(shen_lazyderef, [KL_ARG_V2852_1477, KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_V2805_1745', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2804_1744[0], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_V2806_1746', tco_apply(shen_lazyderef, [KL_ARG_V2853_1478, KL_ARG_V2855_1480])), ([tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V2856_1481])][(-1)] if (symdic.symdic_kl_symbol == KL_CTX.KL_LOC_V2806_1746) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2806_1746, symdic.symdic_kl_symbol, KL_ARG_V2855_1480]), [setattr(KL_CTX, 'KL_LOC_Result_1747', [tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V2856_1481])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2806_1746, KL_ARG_V2855_1480]), KL_CTX.KL_LOC_Result_1747][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2806_1746]) else False))][(-1)] if (symdic.symdic_shen_processx45datatype == KL_CTX.KL_LOC_V2805_1745) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2804_1744) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1748', [setattr(KL_CTX, 'KL_LOC_V2807_1749', tco_apply(shen_lazyderef, [KL_ARG_V2852_1477, KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_V2808_1750', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2807_1749[0], KL_ARG_V2855_1480])), ([setattr(KL_CTX, 'KL_LOC_V2809_1751', tco_apply(shen_lazyderef, [KL_ARG_V2853_1478, KL_ARG_V2855_1480])), ([tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V2856_1481])][(-1)] if (symdic.symdic_kl_symbol == KL_CTX.KL_LOC_V2809_1751) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2809_1751, symdic.symdic_kl_symbol, KL_ARG_V2855_1480]), [setattr(KL_CTX, 'KL_LOC_Result_1752', [tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V2856_1481])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2809_1751, KL_ARG_V2855_1480]), KL_CTX.KL_LOC_Result_1752][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2809_1751]) else False))][(-1)] if (symdic.symdic_shen_synonymsx45help == KL_CTX.KL_LOC_V2808_1750) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2807_1749) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Datatypes_1753', tco_apply(shen_newpv, [KL_ARG_V2855_1480])), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_CTX.KL_LOC_Datatypes_1753, shen_get(symdic.symdic_shen_x42datatypesx42), KL_ARG_V2855_1480, (lambda : tail_call(shen_udefsx42, [[KL_ARG_V2852_1477, [symdic.symdic_kl_x58, [KL_ARG_V2853_1478, []]]], KL_ARG_V2854_1479, KL_CTX.KL_LOC_Datatypes_1753, KL_ARG_V2855_1480, KL_ARG_V2856_1481]))])][(-1)]][(-1)] if (KL_CTX.KL_LOC_Case_1748 == False) else KL_CTX.KL_LOC_Case_1748)][(-1)] if (KL_CTX.KL_LOC_Case_1743 == False) else KL_CTX.KL_LOC_Case_1743)][(-1)] if (KL_CTX.KL_LOC_Case_1738 == False) else KL_CTX.KL_LOC_Case_1738)][(-1)] if (KL_CTX.KL_LOC_Case_1732 == False) else KL_CTX.KL_LOC_Case_1732)][(-1)] if (KL_CTX.KL_LOC_Case_1726 == False) else KL_CTX.KL_LOC_Case_1726)][(-1)] if (KL_CTX.KL_LOC_Case_1724 == False) else KL_CTX.KL_LOC_Case_1724)][(-1)] if (KL_CTX.KL_LOC_Case_1718 == False) else KL_CTX.KL_LOC_Case_1718)][(-1)] if (KL_CTX.KL_LOC_Case_1709 == False) else KL_CTX.KL_LOC_Case_1709)][(-1)] if (KL_CTX.KL_LOC_Case_1701 == False) else KL_CTX.KL_LOC_Case_1701)][(-1)] if (KL_CTX.KL_LOC_Case_1692 == False) else KL_CTX.KL_LOC_Case_1692)][(-1)] if (KL_CTX.KL_LOC_Case_1683 == False) else KL_CTX.KL_LOC_Case_1683)][(-1)] if (KL_CTX.KL_LOC_Case_1675 == False) else KL_CTX.KL_LOC_Case_1675)][(-1)] if (KL_CTX.KL_LOC_Case_1648 == False) else KL_CTX.KL_LOC_Case_1648)][(-1)] if (KL_CTX.KL_LOC_Case_1635 == False) else KL_CTX.KL_LOC_Case_1635)][(-1)] if (KL_CTX.KL_LOC_Case_1589 == False) else KL_CTX.KL_LOC_Case_1589)][(-1)] if (KL_CTX.KL_LOC_Case_1579 == False) else KL_CTX.KL_LOC_Case_1579)][(-1)] if (KL_CTX.KL_LOC_Case_1554 == False) else KL_CTX.KL_LOC_Case_1554)][(-1)] if (KL_CTX.KL_LOC_Case_1524 == False) else KL_CTX.KL_LOC_Case_1524)][(-1)] if (KL_CTX.KL_LOC_Case_1499 == False) else KL_CTX.KL_LOC_Case_1499)][(-1)] if (KL_CTX.KL_LOC_Case_1492 == False) else KL_CTX.KL_LOC_Case_1492)][(-1)] if (KL_CTX.KL_LOC_Case_1488 == False) else KL_CTX.KL_LOC_Case_1488)][(-1)] if (KL_CTX.KL_LOC_Case_1487 == False) else KL_CTX.KL_LOC_Case_1487)][(-1)] if (KL_CTX.KL_LOC_Case_1486 == False) else KL_CTX.KL_LOC_Case_1486)][(-1)] if (KL_CTX.KL_LOC_Case_1484 == False) else KL_CTX.KL_LOC_Case_1484)][(-1)] if (KL_CTX.KL_LOC_Case_1483 == False) else KL_CTX.KL_LOC_Case_1483)][(-1)]])][(-1)]
shen_add_fun('shen.th*', shen_thx42, 5)

@tail_recursion
def shen_tx42x45hyps(KL_ARG_V2857_1754, KL_ARG_V2858_1755, KL_ARG_V2859_1756, KL_ARG_V2860_1757):

    class KL_Context:
        KL_LOC_Case_1758 = None
        KL_LOC_V2600_1759 = None
        KL_LOC_V2601_1760 = None
        KL_LOC_V2602_1761 = None
        KL_LOC_V2603_1762 = None
        KL_LOC_V2604_1763 = None
        KL_LOC_X_1764 = None
        KL_LOC_V2605_1765 = None
        KL_LOC_Y_1766 = None
        KL_LOC_V2606_1767 = None
        KL_LOC_V2607_1768 = None
        KL_LOC_V2608_1769 = None
        KL_LOC_V2609_1770 = None
        KL_LOC_V2610_1771 = None
        KL_LOC_V2611_1772 = None
        KL_LOC_V2612_1773 = None
        KL_LOC_A_1774 = None
        KL_LOC_V2613_1775 = None
        KL_LOC_V2614_1776 = None
        KL_LOC_Hyp_1777 = None
        KL_LOC_Result_1778 = None
        KL_LOC_Hyp_1779 = None
        KL_LOC_Result_1780 = None
        KL_LOC_V2615_1781 = None
        KL_LOC_Hyp_1782 = None
        KL_LOC_Result_1783 = None
        KL_LOC_Hyp_1784 = None
        KL_LOC_A_1785 = None
        KL_LOC_Result_1786 = None
        KL_LOC_V2616_1787 = None
        KL_LOC_Hyp_1788 = None
        KL_LOC_Result_1789 = None
        KL_LOC_Hyp_1790 = None
        KL_LOC_Result_1791 = None
        KL_LOC_V2617_1792 = None
        KL_LOC_A_1793 = None
        KL_LOC_V2618_1794 = None
        KL_LOC_V2619_1795 = None
        KL_LOC_Hyp_1796 = None
        KL_LOC_Result_1797 = None
        KL_LOC_Hyp_1798 = None
        KL_LOC_Result_1799 = None
        KL_LOC_V2620_1800 = None
        KL_LOC_Hyp_1801 = None
        KL_LOC_Result_1802 = None
        KL_LOC_Hyp_1803 = None
        KL_LOC_A_1804 = None
        KL_LOC_Result_1805 = None
        KL_LOC_V2621_1806 = None
        KL_LOC_Hyp_1807 = None
        KL_LOC_Result_1808 = None
        KL_LOC_Hyp_1809 = None
        KL_LOC_A_1810 = None
        KL_LOC_Result_1811 = None
        KL_LOC_V2622_1812 = None
        KL_LOC_Hyp_1813 = None
        KL_LOC_Result_1814 = None
        KL_LOC_Hyp_1815 = None
        KL_LOC_Case_1816 = None
        KL_LOC_V2623_1817 = None
        KL_LOC_V2624_1818 = None
        KL_LOC_V2625_1819 = None
        KL_LOC_V2626_1820 = None
        KL_LOC_V2627_1821 = None
        KL_LOC_X_1822 = None
        KL_LOC_V2628_1823 = None
        KL_LOC_Y_1824 = None
        KL_LOC_V2629_1825 = None
        KL_LOC_V2630_1826 = None
        KL_LOC_V2631_1827 = None
        KL_LOC_V2632_1828 = None
        KL_LOC_V2633_1829 = None
        KL_LOC_A_1830 = None
        KL_LOC_V2634_1831 = None
        KL_LOC_V2635_1832 = None
        KL_LOC_V2636_1833 = None
        KL_LOC_B_1834 = None
        KL_LOC_V2637_1835 = None
        KL_LOC_V2638_1836 = None
        KL_LOC_Hyp_1837 = None
        KL_LOC_Result_1838 = None
        KL_LOC_Hyp_1839 = None
        KL_LOC_Result_1840 = None
        KL_LOC_V2639_1841 = None
        KL_LOC_Hyp_1842 = None
        KL_LOC_Result_1843 = None
        KL_LOC_Hyp_1844 = None
        KL_LOC_B_1845 = None
        KL_LOC_Result_1846 = None
        KL_LOC_V2640_1847 = None
        KL_LOC_Hyp_1848 = None
        KL_LOC_Result_1849 = None
        KL_LOC_Hyp_1850 = None
        KL_LOC_Result_1851 = None
        KL_LOC_V2641_1852 = None
        KL_LOC_B_1853 = None
        KL_LOC_V2642_1854 = None
        KL_LOC_V2643_1855 = None
        KL_LOC_Hyp_1856 = None
        KL_LOC_Result_1857 = None
        KL_LOC_Hyp_1858 = None
        KL_LOC_Result_1859 = None
        KL_LOC_V2644_1860 = None
        KL_LOC_Hyp_1861 = None
        KL_LOC_Result_1862 = None
        KL_LOC_Hyp_1863 = None
        KL_LOC_B_1864 = None
        KL_LOC_Result_1865 = None
        KL_LOC_V2645_1866 = None
        KL_LOC_Hyp_1867 = None
        KL_LOC_Result_1868 = None
        KL_LOC_Hyp_1869 = None
        KL_LOC_B_1870 = None
        KL_LOC_Result_1871 = None
        KL_LOC_V2646_1872 = None
        KL_LOC_Hyp_1873 = None
        KL_LOC_Result_1874 = None
        KL_LOC_Hyp_1875 = None
        KL_LOC_A_1876 = None
        KL_LOC_B_1877 = None
        KL_LOC_Result_1878 = None
        KL_LOC_V2647_1879 = None
        KL_LOC_Hyp_1880 = None
        KL_LOC_Result_1881 = None
        KL_LOC_Hyp_1882 = None
        KL_LOC_Case_1883 = None
        KL_LOC_V2648_1884 = None
        KL_LOC_V2649_1885 = None
        KL_LOC_V2650_1886 = None
        KL_LOC_V2651_1887 = None
        KL_LOC_V2652_1888 = None
        KL_LOC_X_1889 = None
        KL_LOC_V2653_1890 = None
        KL_LOC_Y_1891 = None
        KL_LOC_V2654_1892 = None
        KL_LOC_V2655_1893 = None
        KL_LOC_V2656_1894 = None
        KL_LOC_V2657_1895 = None
        KL_LOC_V2658_1896 = None
        KL_LOC_V2659_1897 = None
        KL_LOC_V2660_1898 = None
        KL_LOC_A_1899 = None
        KL_LOC_V2661_1900 = None
        KL_LOC_V2662_1901 = None
        KL_LOC_Hyp_1902 = None
        KL_LOC_Result_1903 = None
        KL_LOC_Hyp_1904 = None
        KL_LOC_Result_1905 = None
        KL_LOC_V2663_1906 = None
        KL_LOC_Hyp_1907 = None
        KL_LOC_Result_1908 = None
        KL_LOC_Hyp_1909 = None
        KL_LOC_A_1910 = None
        KL_LOC_Result_1911 = None
        KL_LOC_V2664_1912 = None
        KL_LOC_Hyp_1913 = None
        KL_LOC_Result_1914 = None
        KL_LOC_Hyp_1915 = None
        KL_LOC_Result_1916 = None
        KL_LOC_V2665_1917 = None
        KL_LOC_A_1918 = None
        KL_LOC_V2666_1919 = None
        KL_LOC_V2667_1920 = None
        KL_LOC_Hyp_1921 = None
        KL_LOC_Result_1922 = None
        KL_LOC_Hyp_1923 = None
        KL_LOC_Result_1924 = None
        KL_LOC_V2668_1925 = None
        KL_LOC_Hyp_1926 = None
        KL_LOC_Result_1927 = None
        KL_LOC_Hyp_1928 = None
        KL_LOC_A_1929 = None
        KL_LOC_Result_1930 = None
        KL_LOC_V2669_1931 = None
        KL_LOC_Hyp_1932 = None
        KL_LOC_Result_1933 = None
        KL_LOC_Hyp_1934 = None
        KL_LOC_A_1935 = None
        KL_LOC_Result_1936 = None
        KL_LOC_V2670_1937 = None
        KL_LOC_Hyp_1938 = None
        KL_LOC_Result_1939 = None
        KL_LOC_Hyp_1940 = None
        KL_LOC_Case_1941 = None
        KL_LOC_V2671_1942 = None
        KL_LOC_V2672_1943 = None
        KL_LOC_V2673_1944 = None
        KL_LOC_V2674_1945 = None
        KL_LOC_V2675_1946 = None
        KL_LOC_X_1947 = None
        KL_LOC_V2676_1948 = None
        KL_LOC_Y_1949 = None
        KL_LOC_V2677_1950 = None
        KL_LOC_V2678_1951 = None
        KL_LOC_V2679_1952 = None
        KL_LOC_V2680_1953 = None
        KL_LOC_V2681_1954 = None
        KL_LOC_V2682_1955 = None
        KL_LOC_Hyp_1956 = None
        KL_LOC_Result_1957 = None
        KL_LOC_Hyp_1958 = None
        KL_LOC_Result_1959 = None
        KL_LOC_V2683_1960 = None
        KL_LOC_Hyp_1961 = None
        KL_LOC_Result_1962 = None
        KL_LOC_Hyp_1963 = None
        KL_LOC_V2684_1964 = None
        KL_LOC_X_1965 = None
        KL_LOC_Hyp_1966 = None
        KL_LOC_NewHyps_1967 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Case_1758', [setattr(KL_CTX, 'KL_LOC_V2600_1759', tco_apply(shen_lazyderef, [KL_ARG_V2857_1754, KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_V2601_1760', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2600_1759[0], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_V2602_1761', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2601_1760[0], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_V2603_1762', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2602_1761[0], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_V2604_1763', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2602_1761[1], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_X_1764', KL_CTX.KL_LOC_V2604_1763[0]), [setattr(KL_CTX, 'KL_LOC_V2605_1765', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2604_1763[1], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_Y_1766', KL_CTX.KL_LOC_V2605_1765[0]), [setattr(KL_CTX, 'KL_LOC_V2606_1767', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2605_1765[1], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_V2607_1768', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2601_1760[1], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_V2608_1769', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2607_1768[0], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_V2609_1770', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2607_1768[1], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_V2610_1771', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2609_1770[0], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_V2611_1772', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2610_1771[0], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_V2612_1773', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2610_1771[1], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_A_1774', KL_CTX.KL_LOC_V2612_1773[0]), [setattr(KL_CTX, 'KL_LOC_V2613_1775', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2612_1773[1], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_V2614_1776', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2609_1770[1], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1777', KL_CTX.KL_LOC_V2600_1759[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2858_1755, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1764, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1774, KL_ARG_V2859_1756]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1766, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_list, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1774, KL_ARG_V2859_1756]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1777, KL_ARG_V2859_1756])]], KL_ARG_V2859_1756, KL_ARG_V2860_1757])][(-1)]][(-1)] if ([] == KL_CTX.KL_LOC_V2614_1776) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2614_1776, [], KL_ARG_V2859_1756]), [setattr(KL_CTX, 'KL_LOC_Result_1778', [setattr(KL_CTX, 'KL_LOC_Hyp_1779', KL_CTX.KL_LOC_V2600_1759[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2858_1755, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1764, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1774, KL_ARG_V2859_1756]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1766, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_list, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1774, KL_ARG_V2859_1756]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1779, KL_ARG_V2859_1756])]], KL_ARG_V2859_1756, KL_ARG_V2860_1757])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2614_1776, KL_ARG_V2859_1756]), KL_CTX.KL_LOC_Result_1778][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2614_1776]) else False))][(-1)] if ([] == KL_CTX.KL_LOC_V2613_1775) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2613_1775, [], KL_ARG_V2859_1756]), [setattr(KL_CTX, 'KL_LOC_Result_1780', [setattr(KL_CTX, 'KL_LOC_V2615_1781', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2609_1770[1], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1782', KL_CTX.KL_LOC_V2600_1759[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2858_1755, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1764, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1774, KL_ARG_V2859_1756]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1766, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_list, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1774, KL_ARG_V2859_1756]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1782, KL_ARG_V2859_1756])]], KL_ARG_V2859_1756, KL_ARG_V2860_1757])][(-1)]][(-1)] if ([] == KL_CTX.KL_LOC_V2615_1781) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2615_1781, [], KL_ARG_V2859_1756]), [setattr(KL_CTX, 'KL_LOC_Result_1783', [setattr(KL_CTX, 'KL_LOC_Hyp_1784', KL_CTX.KL_LOC_V2600_1759[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2858_1755, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1764, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1774, KL_ARG_V2859_1756]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1766, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_list, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1774, KL_ARG_V2859_1756]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1784, KL_ARG_V2859_1756])]], KL_ARG_V2859_1756, KL_ARG_V2860_1757])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2615_1781, KL_ARG_V2859_1756]), KL_CTX.KL_LOC_Result_1783][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2615_1781]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2613_1775, KL_ARG_V2859_1756]), KL_CTX.KL_LOC_Result_1780][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2613_1775]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2612_1773) else ([setattr(KL_CTX, 'KL_LOC_A_1785', tco_apply(shen_newpv, [KL_ARG_V2859_1756])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2612_1773, [KL_CTX.KL_LOC_A_1785, []], KL_ARG_V2859_1756]), [setattr(KL_CTX, 'KL_LOC_Result_1786', [setattr(KL_CTX, 'KL_LOC_V2616_1787', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2609_1770[1], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1788', KL_CTX.KL_LOC_V2600_1759[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2858_1755, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1764, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1785, KL_ARG_V2859_1756]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1766, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_list, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1785, KL_ARG_V2859_1756]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1788, KL_ARG_V2859_1756])]], KL_ARG_V2859_1756, KL_ARG_V2860_1757])][(-1)]][(-1)] if ([] == KL_CTX.KL_LOC_V2616_1787) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2616_1787, [], KL_ARG_V2859_1756]), [setattr(KL_CTX, 'KL_LOC_Result_1789', [setattr(KL_CTX, 'KL_LOC_Hyp_1790', KL_CTX.KL_LOC_V2600_1759[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2858_1755, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1764, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1785, KL_ARG_V2859_1756]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1766, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_list, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1785, KL_ARG_V2859_1756]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1790, KL_ARG_V2859_1756])]], KL_ARG_V2859_1756, KL_ARG_V2860_1757])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2616_1787, KL_ARG_V2859_1756]), KL_CTX.KL_LOC_Result_1789][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2616_1787]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2612_1773, KL_ARG_V2859_1756]), KL_CTX.KL_LOC_Result_1786][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2612_1773]) else False))][(-1)] if (symdic.symdic_kl_list == KL_CTX.KL_LOC_V2611_1772) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2611_1772, symdic.symdic_kl_list, KL_ARG_V2859_1756]), [setattr(KL_CTX, 'KL_LOC_Result_1791', [setattr(KL_CTX, 'KL_LOC_V2617_1792', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2610_1771[1], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_A_1793', KL_CTX.KL_LOC_V2617_1792[0]), [setattr(KL_CTX, 'KL_LOC_V2618_1794', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2617_1792[1], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_V2619_1795', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2609_1770[1], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1796', KL_CTX.KL_LOC_V2600_1759[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2858_1755, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1764, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1793, KL_ARG_V2859_1756]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1766, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_list, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1793, KL_ARG_V2859_1756]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1796, KL_ARG_V2859_1756])]], KL_ARG_V2859_1756, KL_ARG_V2860_1757])][(-1)]][(-1)] if ([] == KL_CTX.KL_LOC_V2619_1795) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2619_1795, [], KL_ARG_V2859_1756]), [setattr(KL_CTX, 'KL_LOC_Result_1797', [setattr(KL_CTX, 'KL_LOC_Hyp_1798', KL_CTX.KL_LOC_V2600_1759[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2858_1755, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1764, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1793, KL_ARG_V2859_1756]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1766, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_list, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1793, KL_ARG_V2859_1756]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1798, KL_ARG_V2859_1756])]], KL_ARG_V2859_1756, KL_ARG_V2860_1757])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2619_1795, KL_ARG_V2859_1756]), KL_CTX.KL_LOC_Result_1797][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2619_1795]) else False))][(-1)] if ([] == KL_CTX.KL_LOC_V2618_1794) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2618_1794, [], KL_ARG_V2859_1756]), [setattr(KL_CTX, 'KL_LOC_Result_1799', [setattr(KL_CTX, 'KL_LOC_V2620_1800', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2609_1770[1], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1801', KL_CTX.KL_LOC_V2600_1759[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2858_1755, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1764, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1793, KL_ARG_V2859_1756]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1766, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_list, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1793, KL_ARG_V2859_1756]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1801, KL_ARG_V2859_1756])]], KL_ARG_V2859_1756, KL_ARG_V2860_1757])][(-1)]][(-1)] if ([] == KL_CTX.KL_LOC_V2620_1800) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2620_1800, [], KL_ARG_V2859_1756]), [setattr(KL_CTX, 'KL_LOC_Result_1802', [setattr(KL_CTX, 'KL_LOC_Hyp_1803', KL_CTX.KL_LOC_V2600_1759[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2858_1755, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1764, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1793, KL_ARG_V2859_1756]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1766, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_list, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1793, KL_ARG_V2859_1756]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1803, KL_ARG_V2859_1756])]], KL_ARG_V2859_1756, KL_ARG_V2860_1757])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2620_1800, KL_ARG_V2859_1756]), KL_CTX.KL_LOC_Result_1802][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2620_1800]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2618_1794, KL_ARG_V2859_1756]), KL_CTX.KL_LOC_Result_1799][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2618_1794]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2617_1792) else ([setattr(KL_CTX, 'KL_LOC_A_1804', tco_apply(shen_newpv, [KL_ARG_V2859_1756])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2617_1792, [KL_CTX.KL_LOC_A_1804, []], KL_ARG_V2859_1756]), [setattr(KL_CTX, 'KL_LOC_Result_1805', [setattr(KL_CTX, 'KL_LOC_V2621_1806', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2609_1770[1], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1807', KL_CTX.KL_LOC_V2600_1759[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2858_1755, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1764, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1804, KL_ARG_V2859_1756]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1766, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_list, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1804, KL_ARG_V2859_1756]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1807, KL_ARG_V2859_1756])]], KL_ARG_V2859_1756, KL_ARG_V2860_1757])][(-1)]][(-1)] if ([] == KL_CTX.KL_LOC_V2621_1806) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2621_1806, [], KL_ARG_V2859_1756]), [setattr(KL_CTX, 'KL_LOC_Result_1808', [setattr(KL_CTX, 'KL_LOC_Hyp_1809', KL_CTX.KL_LOC_V2600_1759[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2858_1755, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1764, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1804, KL_ARG_V2859_1756]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1766, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_list, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1804, KL_ARG_V2859_1756]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1809, KL_ARG_V2859_1756])]], KL_ARG_V2859_1756, KL_ARG_V2860_1757])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2621_1806, KL_ARG_V2859_1756]), KL_CTX.KL_LOC_Result_1808][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2621_1806]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2617_1792, KL_ARG_V2859_1756]), KL_CTX.KL_LOC_Result_1805][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2617_1792]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2611_1772, KL_ARG_V2859_1756]), KL_CTX.KL_LOC_Result_1791][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2611_1772]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2610_1771) else ([setattr(KL_CTX, 'KL_LOC_A_1810', tco_apply(shen_newpv, [KL_ARG_V2859_1756])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2610_1771, [symdic.symdic_kl_list, [KL_CTX.KL_LOC_A_1810, []]], KL_ARG_V2859_1756]), [setattr(KL_CTX, 'KL_LOC_Result_1811', [setattr(KL_CTX, 'KL_LOC_V2622_1812', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2609_1770[1], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1813', KL_CTX.KL_LOC_V2600_1759[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2858_1755, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1764, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1810, KL_ARG_V2859_1756]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1766, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_list, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1810, KL_ARG_V2859_1756]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1813, KL_ARG_V2859_1756])]], KL_ARG_V2859_1756, KL_ARG_V2860_1757])][(-1)]][(-1)] if ([] == KL_CTX.KL_LOC_V2622_1812) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2622_1812, [], KL_ARG_V2859_1756]), [setattr(KL_CTX, 'KL_LOC_Result_1814', [setattr(KL_CTX, 'KL_LOC_Hyp_1815', KL_CTX.KL_LOC_V2600_1759[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2858_1755, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1764, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1810, KL_ARG_V2859_1756]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1766, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_list, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1810, KL_ARG_V2859_1756]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1815, KL_ARG_V2859_1756])]], KL_ARG_V2859_1756, KL_ARG_V2860_1757])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2622_1812, KL_ARG_V2859_1756]), KL_CTX.KL_LOC_Result_1814][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2622_1812]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2610_1771, KL_ARG_V2859_1756]), KL_CTX.KL_LOC_Result_1811][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2610_1771]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2609_1770) else False)][(-1)] if (symdic.symdic_kl_x58 == KL_CTX.KL_LOC_V2608_1769) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2607_1768) else False)][(-1)] if ([] == KL_CTX.KL_LOC_V2606_1767) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2605_1765) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2604_1763) else False)][(-1)] if (symdic.symdic_kl_cons == KL_CTX.KL_LOC_V2603_1762) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2602_1761) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2601_1760) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2600_1759) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1816', [setattr(KL_CTX, 'KL_LOC_V2623_1817', tco_apply(shen_lazyderef, [KL_ARG_V2857_1754, KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_V2624_1818', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2623_1817[0], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_V2625_1819', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2624_1818[0], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_V2626_1820', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2625_1819[0], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_V2627_1821', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2625_1819[1], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_X_1822', KL_CTX.KL_LOC_V2627_1821[0]), [setattr(KL_CTX, 'KL_LOC_V2628_1823', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2627_1821[1], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_Y_1824', KL_CTX.KL_LOC_V2628_1823[0]), [setattr(KL_CTX, 'KL_LOC_V2629_1825', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2628_1823[1], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_V2630_1826', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2624_1818[1], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_V2631_1827', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2630_1826[0], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_V2632_1828', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2630_1826[1], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_V2633_1829', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2632_1828[0], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_A_1830', KL_CTX.KL_LOC_V2633_1829[0]), [setattr(KL_CTX, 'KL_LOC_V2634_1831', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2633_1829[1], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_V2635_1832', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2634_1831[0], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_V2636_1833', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2634_1831[1], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_B_1834', KL_CTX.KL_LOC_V2636_1833[0]), [setattr(KL_CTX, 'KL_LOC_V2637_1835', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2636_1833[1], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_V2638_1836', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2632_1828[1], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1837', KL_CTX.KL_LOC_V2623_1817[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2858_1755, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1822, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1830, KL_ARG_V2859_1756]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1824, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_1834, KL_ARG_V2859_1756]), []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1837, KL_ARG_V2859_1756])]], KL_ARG_V2859_1756, KL_ARG_V2860_1757])][(-1)]][(-1)] if ([] == KL_CTX.KL_LOC_V2638_1836) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2638_1836, [], KL_ARG_V2859_1756]), [setattr(KL_CTX, 'KL_LOC_Result_1838', [setattr(KL_CTX, 'KL_LOC_Hyp_1839', KL_CTX.KL_LOC_V2623_1817[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2858_1755, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1822, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1830, KL_ARG_V2859_1756]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1824, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_1834, KL_ARG_V2859_1756]), []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1839, KL_ARG_V2859_1756])]], KL_ARG_V2859_1756, KL_ARG_V2860_1757])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2638_1836, KL_ARG_V2859_1756]), KL_CTX.KL_LOC_Result_1838][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2638_1836]) else False))][(-1)] if ([] == KL_CTX.KL_LOC_V2637_1835) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2637_1835, [], KL_ARG_V2859_1756]), [setattr(KL_CTX, 'KL_LOC_Result_1840', [setattr(KL_CTX, 'KL_LOC_V2639_1841', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2632_1828[1], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1842', KL_CTX.KL_LOC_V2623_1817[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2858_1755, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1822, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1830, KL_ARG_V2859_1756]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1824, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_1834, KL_ARG_V2859_1756]), []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1842, KL_ARG_V2859_1756])]], KL_ARG_V2859_1756, KL_ARG_V2860_1757])][(-1)]][(-1)] if ([] == KL_CTX.KL_LOC_V2639_1841) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2639_1841, [], KL_ARG_V2859_1756]), [setattr(KL_CTX, 'KL_LOC_Result_1843', [setattr(KL_CTX, 'KL_LOC_Hyp_1844', KL_CTX.KL_LOC_V2623_1817[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2858_1755, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1822, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1830, KL_ARG_V2859_1756]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1824, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_1834, KL_ARG_V2859_1756]), []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1844, KL_ARG_V2859_1756])]], KL_ARG_V2859_1756, KL_ARG_V2860_1757])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2639_1841, KL_ARG_V2859_1756]), KL_CTX.KL_LOC_Result_1843][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2639_1841]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2637_1835, KL_ARG_V2859_1756]), KL_CTX.KL_LOC_Result_1840][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2637_1835]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2636_1833) else ([setattr(KL_CTX, 'KL_LOC_B_1845', tco_apply(shen_newpv, [KL_ARG_V2859_1756])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2636_1833, [KL_CTX.KL_LOC_B_1845, []], KL_ARG_V2859_1756]), [setattr(KL_CTX, 'KL_LOC_Result_1846', [setattr(KL_CTX, 'KL_LOC_V2640_1847', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2632_1828[1], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1848', KL_CTX.KL_LOC_V2623_1817[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2858_1755, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1822, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1830, KL_ARG_V2859_1756]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1824, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_1845, KL_ARG_V2859_1756]), []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1848, KL_ARG_V2859_1756])]], KL_ARG_V2859_1756, KL_ARG_V2860_1757])][(-1)]][(-1)] if ([] == KL_CTX.KL_LOC_V2640_1847) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2640_1847, [], KL_ARG_V2859_1756]), [setattr(KL_CTX, 'KL_LOC_Result_1849', [setattr(KL_CTX, 'KL_LOC_Hyp_1850', KL_CTX.KL_LOC_V2623_1817[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2858_1755, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1822, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1830, KL_ARG_V2859_1756]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1824, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_1845, KL_ARG_V2859_1756]), []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1850, KL_ARG_V2859_1756])]], KL_ARG_V2859_1756, KL_ARG_V2860_1757])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2640_1847, KL_ARG_V2859_1756]), KL_CTX.KL_LOC_Result_1849][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2640_1847]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2636_1833, KL_ARG_V2859_1756]), KL_CTX.KL_LOC_Result_1846][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2636_1833]) else False))][(-1)] if (symdic.symdic_kl_x42 == KL_CTX.KL_LOC_V2635_1832) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2635_1832, symdic.symdic_kl_x42, KL_ARG_V2859_1756]), [setattr(KL_CTX, 'KL_LOC_Result_1851', [setattr(KL_CTX, 'KL_LOC_V2641_1852', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2634_1831[1], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_B_1853', KL_CTX.KL_LOC_V2641_1852[0]), [setattr(KL_CTX, 'KL_LOC_V2642_1854', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2641_1852[1], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_V2643_1855', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2632_1828[1], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1856', KL_CTX.KL_LOC_V2623_1817[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2858_1755, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1822, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1830, KL_ARG_V2859_1756]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1824, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_1853, KL_ARG_V2859_1756]), []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1856, KL_ARG_V2859_1756])]], KL_ARG_V2859_1756, KL_ARG_V2860_1757])][(-1)]][(-1)] if ([] == KL_CTX.KL_LOC_V2643_1855) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2643_1855, [], KL_ARG_V2859_1756]), [setattr(KL_CTX, 'KL_LOC_Result_1857', [setattr(KL_CTX, 'KL_LOC_Hyp_1858', KL_CTX.KL_LOC_V2623_1817[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2858_1755, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1822, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1830, KL_ARG_V2859_1756]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1824, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_1853, KL_ARG_V2859_1756]), []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1858, KL_ARG_V2859_1756])]], KL_ARG_V2859_1756, KL_ARG_V2860_1757])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2643_1855, KL_ARG_V2859_1756]), KL_CTX.KL_LOC_Result_1857][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2643_1855]) else False))][(-1)] if ([] == KL_CTX.KL_LOC_V2642_1854) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2642_1854, [], KL_ARG_V2859_1756]), [setattr(KL_CTX, 'KL_LOC_Result_1859', [setattr(KL_CTX, 'KL_LOC_V2644_1860', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2632_1828[1], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1861', KL_CTX.KL_LOC_V2623_1817[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2858_1755, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1822, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1830, KL_ARG_V2859_1756]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1824, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_1853, KL_ARG_V2859_1756]), []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1861, KL_ARG_V2859_1756])]], KL_ARG_V2859_1756, KL_ARG_V2860_1757])][(-1)]][(-1)] if ([] == KL_CTX.KL_LOC_V2644_1860) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2644_1860, [], KL_ARG_V2859_1756]), [setattr(KL_CTX, 'KL_LOC_Result_1862', [setattr(KL_CTX, 'KL_LOC_Hyp_1863', KL_CTX.KL_LOC_V2623_1817[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2858_1755, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1822, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1830, KL_ARG_V2859_1756]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1824, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_1853, KL_ARG_V2859_1756]), []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1863, KL_ARG_V2859_1756])]], KL_ARG_V2859_1756, KL_ARG_V2860_1757])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2644_1860, KL_ARG_V2859_1756]), KL_CTX.KL_LOC_Result_1862][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2644_1860]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2642_1854, KL_ARG_V2859_1756]), KL_CTX.KL_LOC_Result_1859][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2642_1854]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2641_1852) else ([setattr(KL_CTX, 'KL_LOC_B_1864', tco_apply(shen_newpv, [KL_ARG_V2859_1756])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2641_1852, [KL_CTX.KL_LOC_B_1864, []], KL_ARG_V2859_1756]), [setattr(KL_CTX, 'KL_LOC_Result_1865', [setattr(KL_CTX, 'KL_LOC_V2645_1866', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2632_1828[1], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1867', KL_CTX.KL_LOC_V2623_1817[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2858_1755, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1822, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1830, KL_ARG_V2859_1756]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1824, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_1864, KL_ARG_V2859_1756]), []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1867, KL_ARG_V2859_1756])]], KL_ARG_V2859_1756, KL_ARG_V2860_1757])][(-1)]][(-1)] if ([] == KL_CTX.KL_LOC_V2645_1866) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2645_1866, [], KL_ARG_V2859_1756]), [setattr(KL_CTX, 'KL_LOC_Result_1868', [setattr(KL_CTX, 'KL_LOC_Hyp_1869', KL_CTX.KL_LOC_V2623_1817[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2858_1755, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1822, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1830, KL_ARG_V2859_1756]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1824, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_1864, KL_ARG_V2859_1756]), []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1869, KL_ARG_V2859_1756])]], KL_ARG_V2859_1756, KL_ARG_V2860_1757])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2645_1866, KL_ARG_V2859_1756]), KL_CTX.KL_LOC_Result_1868][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2645_1866]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2641_1852, KL_ARG_V2859_1756]), KL_CTX.KL_LOC_Result_1865][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2641_1852]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2635_1832, KL_ARG_V2859_1756]), KL_CTX.KL_LOC_Result_1851][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2635_1832]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2634_1831) else ([setattr(KL_CTX, 'KL_LOC_B_1870', tco_apply(shen_newpv, [KL_ARG_V2859_1756])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2634_1831, [symdic.symdic_kl_x42, [KL_CTX.KL_LOC_B_1870, []]], KL_ARG_V2859_1756]), [setattr(KL_CTX, 'KL_LOC_Result_1871', [setattr(KL_CTX, 'KL_LOC_V2646_1872', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2632_1828[1], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1873', KL_CTX.KL_LOC_V2623_1817[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2858_1755, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1822, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1830, KL_ARG_V2859_1756]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1824, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_1870, KL_ARG_V2859_1756]), []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1873, KL_ARG_V2859_1756])]], KL_ARG_V2859_1756, KL_ARG_V2860_1757])][(-1)]][(-1)] if ([] == KL_CTX.KL_LOC_V2646_1872) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2646_1872, [], KL_ARG_V2859_1756]), [setattr(KL_CTX, 'KL_LOC_Result_1874', [setattr(KL_CTX, 'KL_LOC_Hyp_1875', KL_CTX.KL_LOC_V2623_1817[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2858_1755, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1822, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1830, KL_ARG_V2859_1756]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1824, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_1870, KL_ARG_V2859_1756]), []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1875, KL_ARG_V2859_1756])]], KL_ARG_V2859_1756, KL_ARG_V2860_1757])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2646_1872, KL_ARG_V2859_1756]), KL_CTX.KL_LOC_Result_1874][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2646_1872]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2634_1831, KL_ARG_V2859_1756]), KL_CTX.KL_LOC_Result_1871][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2634_1831]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2633_1829) else ([setattr(KL_CTX, 'KL_LOC_A_1876', tco_apply(shen_newpv, [KL_ARG_V2859_1756])), [setattr(KL_CTX, 'KL_LOC_B_1877', tco_apply(shen_newpv, [KL_ARG_V2859_1756])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2633_1829, [KL_CTX.KL_LOC_A_1876, [symdic.symdic_kl_x42, [KL_CTX.KL_LOC_B_1877, []]]], KL_ARG_V2859_1756]), [setattr(KL_CTX, 'KL_LOC_Result_1878', [setattr(KL_CTX, 'KL_LOC_V2647_1879', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2632_1828[1], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1880', KL_CTX.KL_LOC_V2623_1817[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2858_1755, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1822, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1876, KL_ARG_V2859_1756]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1824, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_1877, KL_ARG_V2859_1756]), []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1880, KL_ARG_V2859_1756])]], KL_ARG_V2859_1756, KL_ARG_V2860_1757])][(-1)]][(-1)] if ([] == KL_CTX.KL_LOC_V2647_1879) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2647_1879, [], KL_ARG_V2859_1756]), [setattr(KL_CTX, 'KL_LOC_Result_1881', [setattr(KL_CTX, 'KL_LOC_Hyp_1882', KL_CTX.KL_LOC_V2623_1817[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2858_1755, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1822, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1876, KL_ARG_V2859_1756]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1824, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_1877, KL_ARG_V2859_1756]), []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1882, KL_ARG_V2859_1756])]], KL_ARG_V2859_1756, KL_ARG_V2860_1757])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2647_1879, KL_ARG_V2859_1756]), KL_CTX.KL_LOC_Result_1881][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2647_1879]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2633_1829, KL_ARG_V2859_1756]), KL_CTX.KL_LOC_Result_1878][(-1)]][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2633_1829]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2632_1828) else False)][(-1)] if (symdic.symdic_kl_x58 == KL_CTX.KL_LOC_V2631_1827) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2630_1826) else False)][(-1)] if ([] == KL_CTX.KL_LOC_V2629_1825) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2628_1823) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2627_1821) else False)][(-1)] if (symdic.symdic_kl_x64p == KL_CTX.KL_LOC_V2626_1820) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2625_1819) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2624_1818) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2623_1817) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1883', [setattr(KL_CTX, 'KL_LOC_V2648_1884', tco_apply(shen_lazyderef, [KL_ARG_V2857_1754, KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_V2649_1885', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2648_1884[0], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_V2650_1886', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2649_1885[0], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_V2651_1887', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2650_1886[0], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_V2652_1888', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2650_1886[1], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_X_1889', KL_CTX.KL_LOC_V2652_1888[0]), [setattr(KL_CTX, 'KL_LOC_V2653_1890', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2652_1888[1], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_Y_1891', KL_CTX.KL_LOC_V2653_1890[0]), [setattr(KL_CTX, 'KL_LOC_V2654_1892', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2653_1890[1], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_V2655_1893', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2649_1885[1], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_V2656_1894', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2655_1893[0], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_V2657_1895', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2655_1893[1], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_V2658_1896', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2657_1895[0], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_V2659_1897', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2658_1896[0], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_V2660_1898', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2658_1896[1], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_A_1899', KL_CTX.KL_LOC_V2660_1898[0]), [setattr(KL_CTX, 'KL_LOC_V2661_1900', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2660_1898[1], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_V2662_1901', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2657_1895[1], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1902', KL_CTX.KL_LOC_V2648_1884[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2858_1755, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1889, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1899, KL_ARG_V2859_1756]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1891, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_vector, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1899, KL_ARG_V2859_1756]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1902, KL_ARG_V2859_1756])]], KL_ARG_V2859_1756, KL_ARG_V2860_1757])][(-1)]][(-1)] if ([] == KL_CTX.KL_LOC_V2662_1901) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2662_1901, [], KL_ARG_V2859_1756]), [setattr(KL_CTX, 'KL_LOC_Result_1903', [setattr(KL_CTX, 'KL_LOC_Hyp_1904', KL_CTX.KL_LOC_V2648_1884[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2858_1755, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1889, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1899, KL_ARG_V2859_1756]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1891, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_vector, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1899, KL_ARG_V2859_1756]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1904, KL_ARG_V2859_1756])]], KL_ARG_V2859_1756, KL_ARG_V2860_1757])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2662_1901, KL_ARG_V2859_1756]), KL_CTX.KL_LOC_Result_1903][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2662_1901]) else False))][(-1)] if ([] == KL_CTX.KL_LOC_V2661_1900) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2661_1900, [], KL_ARG_V2859_1756]), [setattr(KL_CTX, 'KL_LOC_Result_1905', [setattr(KL_CTX, 'KL_LOC_V2663_1906', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2657_1895[1], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1907', KL_CTX.KL_LOC_V2648_1884[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2858_1755, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1889, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1899, KL_ARG_V2859_1756]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1891, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_vector, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1899, KL_ARG_V2859_1756]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1907, KL_ARG_V2859_1756])]], KL_ARG_V2859_1756, KL_ARG_V2860_1757])][(-1)]][(-1)] if ([] == KL_CTX.KL_LOC_V2663_1906) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2663_1906, [], KL_ARG_V2859_1756]), [setattr(KL_CTX, 'KL_LOC_Result_1908', [setattr(KL_CTX, 'KL_LOC_Hyp_1909', KL_CTX.KL_LOC_V2648_1884[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2858_1755, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1889, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1899, KL_ARG_V2859_1756]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1891, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_vector, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1899, KL_ARG_V2859_1756]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1909, KL_ARG_V2859_1756])]], KL_ARG_V2859_1756, KL_ARG_V2860_1757])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2663_1906, KL_ARG_V2859_1756]), KL_CTX.KL_LOC_Result_1908][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2663_1906]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2661_1900, KL_ARG_V2859_1756]), KL_CTX.KL_LOC_Result_1905][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2661_1900]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2660_1898) else ([setattr(KL_CTX, 'KL_LOC_A_1910', tco_apply(shen_newpv, [KL_ARG_V2859_1756])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2660_1898, [KL_CTX.KL_LOC_A_1910, []], KL_ARG_V2859_1756]), [setattr(KL_CTX, 'KL_LOC_Result_1911', [setattr(KL_CTX, 'KL_LOC_V2664_1912', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2657_1895[1], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1913', KL_CTX.KL_LOC_V2648_1884[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2858_1755, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1889, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1910, KL_ARG_V2859_1756]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1891, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_vector, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1910, KL_ARG_V2859_1756]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1913, KL_ARG_V2859_1756])]], KL_ARG_V2859_1756, KL_ARG_V2860_1757])][(-1)]][(-1)] if ([] == KL_CTX.KL_LOC_V2664_1912) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2664_1912, [], KL_ARG_V2859_1756]), [setattr(KL_CTX, 'KL_LOC_Result_1914', [setattr(KL_CTX, 'KL_LOC_Hyp_1915', KL_CTX.KL_LOC_V2648_1884[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2858_1755, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1889, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1910, KL_ARG_V2859_1756]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1891, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_vector, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1910, KL_ARG_V2859_1756]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1915, KL_ARG_V2859_1756])]], KL_ARG_V2859_1756, KL_ARG_V2860_1757])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2664_1912, KL_ARG_V2859_1756]), KL_CTX.KL_LOC_Result_1914][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2664_1912]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2660_1898, KL_ARG_V2859_1756]), KL_CTX.KL_LOC_Result_1911][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2660_1898]) else False))][(-1)] if (symdic.symdic_kl_vector == KL_CTX.KL_LOC_V2659_1897) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2659_1897, symdic.symdic_kl_vector, KL_ARG_V2859_1756]), [setattr(KL_CTX, 'KL_LOC_Result_1916', [setattr(KL_CTX, 'KL_LOC_V2665_1917', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2658_1896[1], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_A_1918', KL_CTX.KL_LOC_V2665_1917[0]), [setattr(KL_CTX, 'KL_LOC_V2666_1919', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2665_1917[1], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_V2667_1920', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2657_1895[1], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1921', KL_CTX.KL_LOC_V2648_1884[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2858_1755, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1889, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1918, KL_ARG_V2859_1756]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1891, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_vector, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1918, KL_ARG_V2859_1756]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1921, KL_ARG_V2859_1756])]], KL_ARG_V2859_1756, KL_ARG_V2860_1757])][(-1)]][(-1)] if ([] == KL_CTX.KL_LOC_V2667_1920) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2667_1920, [], KL_ARG_V2859_1756]), [setattr(KL_CTX, 'KL_LOC_Result_1922', [setattr(KL_CTX, 'KL_LOC_Hyp_1923', KL_CTX.KL_LOC_V2648_1884[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2858_1755, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1889, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1918, KL_ARG_V2859_1756]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1891, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_vector, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1918, KL_ARG_V2859_1756]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1923, KL_ARG_V2859_1756])]], KL_ARG_V2859_1756, KL_ARG_V2860_1757])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2667_1920, KL_ARG_V2859_1756]), KL_CTX.KL_LOC_Result_1922][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2667_1920]) else False))][(-1)] if ([] == KL_CTX.KL_LOC_V2666_1919) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2666_1919, [], KL_ARG_V2859_1756]), [setattr(KL_CTX, 'KL_LOC_Result_1924', [setattr(KL_CTX, 'KL_LOC_V2668_1925', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2657_1895[1], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1926', KL_CTX.KL_LOC_V2648_1884[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2858_1755, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1889, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1918, KL_ARG_V2859_1756]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1891, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_vector, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1918, KL_ARG_V2859_1756]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1926, KL_ARG_V2859_1756])]], KL_ARG_V2859_1756, KL_ARG_V2860_1757])][(-1)]][(-1)] if ([] == KL_CTX.KL_LOC_V2668_1925) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2668_1925, [], KL_ARG_V2859_1756]), [setattr(KL_CTX, 'KL_LOC_Result_1927', [setattr(KL_CTX, 'KL_LOC_Hyp_1928', KL_CTX.KL_LOC_V2648_1884[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2858_1755, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1889, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1918, KL_ARG_V2859_1756]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1891, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_vector, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1918, KL_ARG_V2859_1756]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1928, KL_ARG_V2859_1756])]], KL_ARG_V2859_1756, KL_ARG_V2860_1757])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2668_1925, KL_ARG_V2859_1756]), KL_CTX.KL_LOC_Result_1927][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2668_1925]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2666_1919, KL_ARG_V2859_1756]), KL_CTX.KL_LOC_Result_1924][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2666_1919]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2665_1917) else ([setattr(KL_CTX, 'KL_LOC_A_1929', tco_apply(shen_newpv, [KL_ARG_V2859_1756])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2665_1917, [KL_CTX.KL_LOC_A_1929, []], KL_ARG_V2859_1756]), [setattr(KL_CTX, 'KL_LOC_Result_1930', [setattr(KL_CTX, 'KL_LOC_V2669_1931', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2657_1895[1], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1932', KL_CTX.KL_LOC_V2648_1884[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2858_1755, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1889, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1929, KL_ARG_V2859_1756]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1891, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_vector, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1929, KL_ARG_V2859_1756]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1932, KL_ARG_V2859_1756])]], KL_ARG_V2859_1756, KL_ARG_V2860_1757])][(-1)]][(-1)] if ([] == KL_CTX.KL_LOC_V2669_1931) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2669_1931, [], KL_ARG_V2859_1756]), [setattr(KL_CTX, 'KL_LOC_Result_1933', [setattr(KL_CTX, 'KL_LOC_Hyp_1934', KL_CTX.KL_LOC_V2648_1884[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2858_1755, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1889, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1929, KL_ARG_V2859_1756]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1891, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_vector, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1929, KL_ARG_V2859_1756]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1934, KL_ARG_V2859_1756])]], KL_ARG_V2859_1756, KL_ARG_V2860_1757])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2669_1931, KL_ARG_V2859_1756]), KL_CTX.KL_LOC_Result_1933][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2669_1931]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2665_1917, KL_ARG_V2859_1756]), KL_CTX.KL_LOC_Result_1930][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2665_1917]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2659_1897, KL_ARG_V2859_1756]), KL_CTX.KL_LOC_Result_1916][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2659_1897]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2658_1896) else ([setattr(KL_CTX, 'KL_LOC_A_1935', tco_apply(shen_newpv, [KL_ARG_V2859_1756])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2658_1896, [symdic.symdic_kl_vector, [KL_CTX.KL_LOC_A_1935, []]], KL_ARG_V2859_1756]), [setattr(KL_CTX, 'KL_LOC_Result_1936', [setattr(KL_CTX, 'KL_LOC_V2670_1937', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2657_1895[1], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1938', KL_CTX.KL_LOC_V2648_1884[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2858_1755, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1889, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1935, KL_ARG_V2859_1756]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1891, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_vector, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1935, KL_ARG_V2859_1756]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1938, KL_ARG_V2859_1756])]], KL_ARG_V2859_1756, KL_ARG_V2860_1757])][(-1)]][(-1)] if ([] == KL_CTX.KL_LOC_V2670_1937) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2670_1937, [], KL_ARG_V2859_1756]), [setattr(KL_CTX, 'KL_LOC_Result_1939', [setattr(KL_CTX, 'KL_LOC_Hyp_1940', KL_CTX.KL_LOC_V2648_1884[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2858_1755, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1889, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1935, KL_ARG_V2859_1756]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1891, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_vector, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1935, KL_ARG_V2859_1756]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1940, KL_ARG_V2859_1756])]], KL_ARG_V2859_1756, KL_ARG_V2860_1757])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2670_1937, KL_ARG_V2859_1756]), KL_CTX.KL_LOC_Result_1939][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2670_1937]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2658_1896, KL_ARG_V2859_1756]), KL_CTX.KL_LOC_Result_1936][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2658_1896]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2657_1895) else False)][(-1)] if (symdic.symdic_kl_x58 == KL_CTX.KL_LOC_V2656_1894) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2655_1893) else False)][(-1)] if ([] == KL_CTX.KL_LOC_V2654_1892) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2653_1890) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2652_1888) else False)][(-1)] if (symdic.symdic_kl_x64v == KL_CTX.KL_LOC_V2651_1887) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2650_1886) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2649_1885) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2648_1884) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1941', [setattr(KL_CTX, 'KL_LOC_V2671_1942', tco_apply(shen_lazyderef, [KL_ARG_V2857_1754, KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_V2672_1943', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2671_1942[0], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_V2673_1944', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2672_1943[0], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_V2674_1945', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2673_1944[0], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_V2675_1946', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2673_1944[1], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_X_1947', KL_CTX.KL_LOC_V2675_1946[0]), [setattr(KL_CTX, 'KL_LOC_V2676_1948', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2675_1946[1], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_Y_1949', KL_CTX.KL_LOC_V2676_1948[0]), [setattr(KL_CTX, 'KL_LOC_V2677_1950', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2676_1948[1], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_V2678_1951', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2672_1943[1], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_V2679_1952', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2678_1951[0], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_V2680_1953', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2678_1951[1], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_V2681_1954', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2680_1953[0], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_V2682_1955', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2680_1953[1], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1956', KL_CTX.KL_LOC_V2671_1942[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2858_1755, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1947, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [symdic.symdic_kl_string, []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1949, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [symdic.symdic_kl_string, []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1956, KL_ARG_V2859_1756])]], KL_ARG_V2859_1756, KL_ARG_V2860_1757])][(-1)]][(-1)] if ([] == KL_CTX.KL_LOC_V2682_1955) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2682_1955, [], KL_ARG_V2859_1756]), [setattr(KL_CTX, 'KL_LOC_Result_1957', [setattr(KL_CTX, 'KL_LOC_Hyp_1958', KL_CTX.KL_LOC_V2671_1942[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2858_1755, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1947, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [symdic.symdic_kl_string, []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1949, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [symdic.symdic_kl_string, []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1958, KL_ARG_V2859_1756])]], KL_ARG_V2859_1756, KL_ARG_V2860_1757])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2682_1955, KL_ARG_V2859_1756]), KL_CTX.KL_LOC_Result_1957][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2682_1955]) else False))][(-1)] if (symdic.symdic_kl_string == KL_CTX.KL_LOC_V2681_1954) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2681_1954, symdic.symdic_kl_string, KL_ARG_V2859_1756]), [setattr(KL_CTX, 'KL_LOC_Result_1959', [setattr(KL_CTX, 'KL_LOC_V2683_1960', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2680_1953[1], KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1961', KL_CTX.KL_LOC_V2671_1942[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2858_1755, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1947, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [symdic.symdic_kl_string, []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1949, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [symdic.symdic_kl_string, []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1961, KL_ARG_V2859_1756])]], KL_ARG_V2859_1756, KL_ARG_V2860_1757])][(-1)]][(-1)] if ([] == KL_CTX.KL_LOC_V2683_1960) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2683_1960, [], KL_ARG_V2859_1756]), [setattr(KL_CTX, 'KL_LOC_Result_1962', [setattr(KL_CTX, 'KL_LOC_Hyp_1963', KL_CTX.KL_LOC_V2671_1942[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2858_1755, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1947, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [symdic.symdic_kl_string, []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1949, KL_ARG_V2859_1756]), [symdic.symdic_kl_x58, [symdic.symdic_kl_string, []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1963, KL_ARG_V2859_1756])]], KL_ARG_V2859_1756, KL_ARG_V2860_1757])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2683_1960, KL_ARG_V2859_1756]), KL_CTX.KL_LOC_Result_1962][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2683_1960]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2681_1954, KL_ARG_V2859_1756]), KL_CTX.KL_LOC_Result_1959][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2681_1954]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2680_1953) else False)][(-1)] if (symdic.symdic_kl_x58 == KL_CTX.KL_LOC_V2679_1952) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2678_1951) else False)][(-1)] if ([] == KL_CTX.KL_LOC_V2677_1950) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2676_1948) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2675_1946) else False)][(-1)] if (symdic.symdic_kl_x64s == KL_CTX.KL_LOC_V2674_1945) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2673_1944) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2672_1943) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2671_1942) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_V2684_1964', tco_apply(shen_lazyderef, [KL_ARG_V2857_1754, KL_ARG_V2859_1756])), ([setattr(KL_CTX, 'KL_LOC_X_1965', KL_CTX.KL_LOC_V2684_1964[0]), [setattr(KL_CTX, 'KL_LOC_Hyp_1966', KL_CTX.KL_LOC_V2684_1964[1]), [setattr(KL_CTX, 'KL_LOC_NewHyps_1967', tco_apply(shen_newpv, [KL_ARG_V2859_1756])), [tco_apply(shen_incinfs, []), tail_call(kl_bind, [KL_ARG_V2858_1755, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1965, KL_ARG_V2859_1756]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_NewHyps_1967, KL_ARG_V2859_1756])], KL_ARG_V2859_1756, (lambda : tail_call(shen_tx42x45hyps, [KL_CTX.KL_LOC_Hyp_1966, KL_CTX.KL_LOC_NewHyps_1967, KL_ARG_V2859_1756, KL_ARG_V2860_1757]))])][(-1)]][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2684_1964) else False)][(-1)] if (KL_CTX.KL_LOC_Case_1941 == False) else KL_CTX.KL_LOC_Case_1941)][(-1)] if (KL_CTX.KL_LOC_Case_1883 == False) else KL_CTX.KL_LOC_Case_1883)][(-1)] if (KL_CTX.KL_LOC_Case_1816 == False) else KL_CTX.KL_LOC_Case_1816)][(-1)] if (KL_CTX.KL_LOC_Case_1758 == False) else KL_CTX.KL_LOC_Case_1758)][(-1)]
shen_add_fun('shen.t*-hyps', shen_tx42x45hyps, 4)

@tail_recursion
def shen_show(KL_ARG_V2873_1968, KL_ARG_V2874_1969, KL_ARG_V2875_1970, KL_ARG_V2876_1971):
    global symdic
    return ([tco_apply(shen_line, []), [tco_apply(shen_showx45p, [tco_apply(shen_deref, [KL_ARG_V2873_1968, KL_ARG_V2875_1970])]), [tco_apply(kl_nl, [1]), [tco_apply(kl_nl, [1]), [tco_apply(shen_showx45assumptions, [tco_apply(shen_deref, [KL_ARG_V2874_1969, KL_ARG_V2875_1970]), 1]), [tco_apply(shen_prhush, ['\r\n> ', tco_apply(kl_stoutput, [])]), [tco_apply(shen_pausex45forx45user, [shen_get(symdic.symdic_kl_x42languagex42)]), tail_call(kl_thaw, [KL_ARG_V2876_1971])][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)] if shen_get(symdic.symdic_shen_x42spyx42) else (tail_call(kl_thaw, [KL_ARG_V2876_1971]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.show', shen_show, 4)

@tail_recursion
def shen_line():

    class KL_Context:
        KL_LOC_Infs_1972 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Infs_1972', tco_apply(kl_inferences, [])), tail_call(shen_prhush, [('____________________________________________________________ ' + tco_apply(shen_app, [KL_CTX.KL_LOC_Infs_1972, (' inference' + tco_apply(shen_app, [('' if (1 == KL_CTX.KL_LOC_Infs_1972) else 's'), ' \r\n?- ', symdic.symdic_shen_a])), symdic.symdic_shen_a])), tco_apply(kl_stoutput, [])])][(-1)]
shen_add_fun('shen.line', shen_line, 0)

@tail_recursion
def shen_showx45p(KL_ARG_V2877_1973):
    global symdic
    return (tail_call(shen_prhush, [tco_apply(shen_app, [KL_ARG_V2877_1973[0], (' : ' + tco_apply(shen_app, [KL_ARG_V2877_1973[1][1][0], '', symdic.symdic_shen_r])), symdic.symdic_shen_r]), tco_apply(kl_stoutput, [])]) if ((((([] == KL_ARG_V2877_1973[1][1][1]) if shen_consp(KL_ARG_V2877_1973[1][1]) else False) if (symdic.symdic_kl_x58 == KL_ARG_V2877_1973[1][0]) else False) if shen_consp(KL_ARG_V2877_1973[1]) else False) if shen_consp(KL_ARG_V2877_1973) else False) else (tail_call(shen_prhush, [tco_apply(shen_app, [KL_ARG_V2877_1973, '', symdic.symdic_shen_r]), tco_apply(kl_stoutput, [])]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.show-p', shen_showx45p, 1)

@tail_recursion
def shen_showx45assumptions(KL_ARG_V2880_1974, KL_ARG_V2881_1975):
    global symdic
    return (symdic.symdic_shen_skip if ([] == KL_ARG_V2880_1974) else ([tco_apply(shen_prhush, [tco_apply(shen_app, [KL_ARG_V2881_1975, '. ', symdic.symdic_shen_a]), tco_apply(kl_stoutput, [])]), [tco_apply(shen_showx45p, [KL_ARG_V2880_1974[0]]), [tco_apply(kl_nl, [1]), tail_call(shen_showx45assumptions, [KL_ARG_V2880_1974[1], (KL_ARG_V2881_1975 + 1)])][(-1)]][(-1)]][(-1)] if shen_consp(KL_ARG_V2880_1974) else (tail_call(shen_sysx45error, [symdic.symdic_shen_showx45assumptions]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.show-assumptions', shen_showx45assumptions, 2)

@tail_recursion
def shen_pausex45forx45user(KL_ARG_V2886_1976):

    class KL_Context:
        KL_LOC_I_1977 = None
        KL_LOC_I_1978 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_I_1977', tco_apply(FORMAT, [[], '~C', tco_apply(READx45CHAR, [])])), (shen_simple_error('input aborted\r\n') if (KL_CTX.KL_LOC_I_1977 == 'a') else tail_call(kl_nl, [1]))][(-1)] if ('Common Lisp' == KL_ARG_V2886_1976) else ([setattr(KL_CTX, 'KL_LOC_I_1978', tco_apply(shen_readx45char, [])), (shen_simple_error('input aborted\r\n') if (KL_CTX.KL_LOC_I_1978 == 'a') else tail_call(kl_nl, [1]))][(-1)] if True else shen_simple_error('condition failure')))
shen_add_fun('shen.pause-for-user', shen_pausex45forx45user, 1)

@tail_recursion
def shen_readx45char():
    global symdic
    return tail_call(shen_readx45charx45h, [shen_read_byte(tco_apply(kl_stinput, [])), 0])
shen_add_fun('shen.read-char', shen_readx45char, 0)

@tail_recursion
def shen_readx45charx45h(KL_ARG_V2889_1979, KL_ARG_V2890_1980):
    global symdic
    return (tail_call(shen_readx45charx45h, [shen_read_byte(tco_apply(kl_stinput, [])), 1]) if ((0 == KL_ARG_V2890_1980) if ((-1) == KL_ARG_V2889_1979) else False) else (tail_call(shen_readx45charx45h, [shen_read_byte(tco_apply(kl_stinput, [])), 0]) if (0 == KL_ARG_V2890_1980) else (tail_call(shen_readx45charx45h, [shen_read_byte(tco_apply(kl_stinput, [])), 1]) if ((1 == KL_ARG_V2890_1980) if ((-1) == KL_ARG_V2889_1979) else False) else (chr(KL_ARG_V2889_1979) if (1 == KL_ARG_V2890_1980) else (tail_call(shen_sysx45error, [symdic.symdic_shen_readx45charx45h]) if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.read-char-h', shen_readx45charx45h, 2)

@tail_recursion
def shen_typedfx63(KL_ARG_V2891_1981):
    global symdic
    return shen_consp(tco_apply(kl_assoc, [KL_ARG_V2891_1981, shen_get(symdic.symdic_shen_x42signedfuncsx42)]))
shen_add_fun('shen.typedf?', shen_typedfx63, 1)

@tail_recursion
def shen_sigf(KL_ARG_V2892_1982):
    global symdic
    return tail_call(kl_concat, [symdic.symdic_shen_typex45signaturex45ofx45, KL_ARG_V2892_1982])
shen_add_fun('shen.sigf', shen_sigf, 1)

@tail_recursion
def shen_placeholder():
    global symdic
    return tail_call(kl_gensym, [symdic.symdic_kl_x38x38])
shen_add_fun('shen.placeholder', shen_placeholder, 0)

@tail_recursion
def shen_base(KL_ARG_V2893_1983, KL_ARG_V2894_1984, KL_ARG_V2895_1985, KL_ARG_V2896_1986):

    class KL_Context:
        KL_LOC_Case_1987 = None
        KL_LOC_V2587_1988 = None
        KL_LOC_Result_1989 = None
        KL_LOC_Case_1990 = None
        KL_LOC_V2588_1991 = None
        KL_LOC_Result_1992 = None
        KL_LOC_Case_1993 = None
        KL_LOC_V2589_1994 = None
        KL_LOC_Result_1995 = None
        KL_LOC_Case_1996 = None
        KL_LOC_V2590_1997 = None
        KL_LOC_Result_1998 = None
        KL_LOC_V2591_1999 = None
        KL_LOC_V2592_2000 = None
        KL_LOC_V2593_2001 = None
        KL_LOC_V2594_2002 = None
        KL_LOC_A_2003 = None
        KL_LOC_V2595_2004 = None
        KL_LOC_Result_2005 = None
        KL_LOC_A_2006 = None
        KL_LOC_Result_2007 = None
        KL_LOC_Result_2008 = None
        KL_LOC_V2596_2009 = None
        KL_LOC_A_2010 = None
        KL_LOC_V2597_2011 = None
        KL_LOC_Result_2012 = None
        KL_LOC_A_2013 = None
        KL_LOC_Result_2014 = None
        KL_LOC_A_2015 = None
        KL_LOC_Result_2016 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Case_1987', [setattr(KL_CTX, 'KL_LOC_V2587_1988', tco_apply(shen_lazyderef, [KL_ARG_V2894_1984, KL_ARG_V2895_1985])), ([tco_apply(shen_incinfs, []), tco_apply(kl_fwhen, [isinstance(tco_apply(shen_lazyderef, [KL_ARG_V2893_1983, KL_ARG_V2895_1985]), numbers.Number), KL_ARG_V2895_1985, KL_ARG_V2896_1986])][(-1)] if (symdic.symdic_kl_number == KL_CTX.KL_LOC_V2587_1988) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2587_1988, symdic.symdic_kl_number, KL_ARG_V2895_1985]), [setattr(KL_CTX, 'KL_LOC_Result_1989', [tco_apply(shen_incinfs, []), tco_apply(kl_fwhen, [isinstance(tco_apply(shen_lazyderef, [KL_ARG_V2893_1983, KL_ARG_V2895_1985]), numbers.Number), KL_ARG_V2895_1985, KL_ARG_V2896_1986])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2587_1988, KL_ARG_V2895_1985]), KL_CTX.KL_LOC_Result_1989][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2587_1988]) else False))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1990', [setattr(KL_CTX, 'KL_LOC_V2588_1991', tco_apply(shen_lazyderef, [KL_ARG_V2894_1984, KL_ARG_V2895_1985])), ([tco_apply(shen_incinfs, []), tco_apply(kl_fwhen, [tco_apply(kl_booleanx63, [tco_apply(shen_lazyderef, [KL_ARG_V2893_1983, KL_ARG_V2895_1985])]), KL_ARG_V2895_1985, KL_ARG_V2896_1986])][(-1)] if (symdic.symdic_kl_boolean == KL_CTX.KL_LOC_V2588_1991) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2588_1991, symdic.symdic_kl_boolean, KL_ARG_V2895_1985]), [setattr(KL_CTX, 'KL_LOC_Result_1992', [tco_apply(shen_incinfs, []), tco_apply(kl_fwhen, [tco_apply(kl_booleanx63, [tco_apply(shen_lazyderef, [KL_ARG_V2893_1983, KL_ARG_V2895_1985])]), KL_ARG_V2895_1985, KL_ARG_V2896_1986])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2588_1991, KL_ARG_V2895_1985]), KL_CTX.KL_LOC_Result_1992][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2588_1991]) else False))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1993', [setattr(KL_CTX, 'KL_LOC_V2589_1994', tco_apply(shen_lazyderef, [KL_ARG_V2894_1984, KL_ARG_V2895_1985])), ([tco_apply(shen_incinfs, []), tco_apply(kl_fwhen, [isinstance(tco_apply(shen_lazyderef, [KL_ARG_V2893_1983, KL_ARG_V2895_1985]), str), KL_ARG_V2895_1985, KL_ARG_V2896_1986])][(-1)] if (symdic.symdic_kl_string == KL_CTX.KL_LOC_V2589_1994) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2589_1994, symdic.symdic_kl_string, KL_ARG_V2895_1985]), [setattr(KL_CTX, 'KL_LOC_Result_1995', [tco_apply(shen_incinfs, []), tco_apply(kl_fwhen, [isinstance(tco_apply(shen_lazyderef, [KL_ARG_V2893_1983, KL_ARG_V2895_1985]), str), KL_ARG_V2895_1985, KL_ARG_V2896_1986])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2589_1994, KL_ARG_V2895_1985]), KL_CTX.KL_LOC_Result_1995][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2589_1994]) else False))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1996', [setattr(KL_CTX, 'KL_LOC_V2590_1997', tco_apply(shen_lazyderef, [KL_ARG_V2894_1984, KL_ARG_V2895_1985])), ([tco_apply(shen_incinfs, []), tco_apply(kl_fwhen, [tco_apply(kl_symbolx63, [tco_apply(shen_lazyderef, [KL_ARG_V2893_1983, KL_ARG_V2895_1985])]), KL_ARG_V2895_1985, (lambda : tail_call(kl_fwhen, [(not tco_apply(shen_uex63, [tco_apply(shen_lazyderef, [KL_ARG_V2893_1983, KL_ARG_V2895_1985])])), KL_ARG_V2895_1985, KL_ARG_V2896_1986]))])][(-1)] if (symdic.symdic_kl_symbol == KL_CTX.KL_LOC_V2590_1997) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2590_1997, symdic.symdic_kl_symbol, KL_ARG_V2895_1985]), [setattr(KL_CTX, 'KL_LOC_Result_1998', [tco_apply(shen_incinfs, []), tco_apply(kl_fwhen, [tco_apply(kl_symbolx63, [tco_apply(shen_lazyderef, [KL_ARG_V2893_1983, KL_ARG_V2895_1985])]), KL_ARG_V2895_1985, (lambda : tail_call(kl_fwhen, [(not tco_apply(shen_uex63, [tco_apply(shen_lazyderef, [KL_ARG_V2893_1983, KL_ARG_V2895_1985])])), KL_ARG_V2895_1985, KL_ARG_V2896_1986]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2590_1997, KL_ARG_V2895_1985]), KL_CTX.KL_LOC_Result_1998][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2590_1997]) else False))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_V2591_1999', tco_apply(shen_lazyderef, [KL_ARG_V2893_1983, KL_ARG_V2895_1985])), ([setattr(KL_CTX, 'KL_LOC_V2592_2000', tco_apply(shen_lazyderef, [KL_ARG_V2894_1984, KL_ARG_V2895_1985])), ([setattr(KL_CTX, 'KL_LOC_V2593_2001', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2592_2000[0], KL_ARG_V2895_1985])), ([setattr(KL_CTX, 'KL_LOC_V2594_2002', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2592_2000[1], KL_ARG_V2895_1985])), ([setattr(KL_CTX, 'KL_LOC_A_2003', KL_CTX.KL_LOC_V2594_2002[0]), [setattr(KL_CTX, 'KL_LOC_V2595_2004', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2594_2002[1], KL_ARG_V2895_1985])), ([tco_apply(shen_incinfs, []), tail_call(kl_thaw, [KL_ARG_V2896_1986])][(-1)] if ([] == KL_CTX.KL_LOC_V2595_2004) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2595_2004, [], KL_ARG_V2895_1985]), [setattr(KL_CTX, 'KL_LOC_Result_2005', [tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V2896_1986])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2595_2004, KL_ARG_V2895_1985]), KL_CTX.KL_LOC_Result_2005][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2595_2004]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2594_2002) else ([setattr(KL_CTX, 'KL_LOC_A_2006', tco_apply(shen_newpv, [KL_ARG_V2895_1985])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2594_2002, [KL_CTX.KL_LOC_A_2006, []], KL_ARG_V2895_1985]), [setattr(KL_CTX, 'KL_LOC_Result_2007', [tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V2896_1986])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2594_2002, KL_ARG_V2895_1985]), KL_CTX.KL_LOC_Result_2007][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2594_2002]) else False))][(-1)] if (symdic.symdic_kl_list == KL_CTX.KL_LOC_V2593_2001) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2593_2001, symdic.symdic_kl_list, KL_ARG_V2895_1985]), [setattr(KL_CTX, 'KL_LOC_Result_2008', [setattr(KL_CTX, 'KL_LOC_V2596_2009', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2592_2000[1], KL_ARG_V2895_1985])), ([setattr(KL_CTX, 'KL_LOC_A_2010', KL_CTX.KL_LOC_V2596_2009[0]), [setattr(KL_CTX, 'KL_LOC_V2597_2011', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2596_2009[1], KL_ARG_V2895_1985])), ([tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V2896_1986])][(-1)] if ([] == KL_CTX.KL_LOC_V2597_2011) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2597_2011, [], KL_ARG_V2895_1985]), [setattr(KL_CTX, 'KL_LOC_Result_2012', [tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V2896_1986])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2597_2011, KL_ARG_V2895_1985]), KL_CTX.KL_LOC_Result_2012][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2597_2011]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2596_2009) else ([setattr(KL_CTX, 'KL_LOC_A_2013', tco_apply(shen_newpv, [KL_ARG_V2895_1985])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2596_2009, [KL_CTX.KL_LOC_A_2013, []], KL_ARG_V2895_1985]), [setattr(KL_CTX, 'KL_LOC_Result_2014', [tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V2896_1986])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2596_2009, KL_ARG_V2895_1985]), KL_CTX.KL_LOC_Result_2014][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2596_2009]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2593_2001, KL_ARG_V2895_1985]), KL_CTX.KL_LOC_Result_2008][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2593_2001]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2592_2000) else ([setattr(KL_CTX, 'KL_LOC_A_2015', tco_apply(shen_newpv, [KL_ARG_V2895_1985])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2592_2000, [symdic.symdic_kl_list, [KL_CTX.KL_LOC_A_2015, []]], KL_ARG_V2895_1985]), [setattr(KL_CTX, 'KL_LOC_Result_2016', [tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V2896_1986])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2592_2000, KL_ARG_V2895_1985]), KL_CTX.KL_LOC_Result_2016][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2592_2000]) else False))][(-1)] if ([] == KL_CTX.KL_LOC_V2591_1999) else False)][(-1)] if (KL_CTX.KL_LOC_Case_1996 == False) else KL_CTX.KL_LOC_Case_1996)][(-1)] if (KL_CTX.KL_LOC_Case_1993 == False) else KL_CTX.KL_LOC_Case_1993)][(-1)] if (KL_CTX.KL_LOC_Case_1990 == False) else KL_CTX.KL_LOC_Case_1990)][(-1)] if (KL_CTX.KL_LOC_Case_1987 == False) else KL_CTX.KL_LOC_Case_1987)][(-1)]
shen_add_fun('shen.base', shen_base, 4)

@tail_recursion
def shen_by_hypothesis(KL_ARG_V2897_2017, KL_ARG_V2898_2018, KL_ARG_V2899_2019, KL_ARG_V2900_2020, KL_ARG_V2901_2021):

    class KL_Context:
        KL_LOC_Case_2022 = None
        KL_LOC_V2578_2023 = None
        KL_LOC_V2579_2024 = None
        KL_LOC_Y_2025 = None
        KL_LOC_V2580_2026 = None
        KL_LOC_V2581_2027 = None
        KL_LOC_V2582_2028 = None
        KL_LOC_B_2029 = None
        KL_LOC_V2583_2030 = None
        KL_LOC_V2584_2031 = None
        KL_LOC_Hyp_2032 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Case_2022', [setattr(KL_CTX, 'KL_LOC_V2578_2023', tco_apply(shen_lazyderef, [KL_ARG_V2899_2019, KL_ARG_V2900_2020])), ([setattr(KL_CTX, 'KL_LOC_V2579_2024', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2578_2023[0], KL_ARG_V2900_2020])), ([setattr(KL_CTX, 'KL_LOC_Y_2025', KL_CTX.KL_LOC_V2579_2024[0]), [setattr(KL_CTX, 'KL_LOC_V2580_2026', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2579_2024[1], KL_ARG_V2900_2020])), ([setattr(KL_CTX, 'KL_LOC_V2581_2027', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2580_2026[0], KL_ARG_V2900_2020])), ([setattr(KL_CTX, 'KL_LOC_V2582_2028', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2580_2026[1], KL_ARG_V2900_2020])), ([setattr(KL_CTX, 'KL_LOC_B_2029', KL_CTX.KL_LOC_V2582_2028[0]), [setattr(KL_CTX, 'KL_LOC_V2583_2030', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2582_2028[1], KL_ARG_V2900_2020])), ([tco_apply(shen_incinfs, []), tco_apply(kl_identical, [KL_ARG_V2897_2017, KL_CTX.KL_LOC_Y_2025, KL_ARG_V2900_2020, (lambda : tail_call(kl_unifyx33, [KL_ARG_V2898_2018, KL_CTX.KL_LOC_B_2029, KL_ARG_V2900_2020, KL_ARG_V2901_2021]))])][(-1)] if ([] == KL_CTX.KL_LOC_V2583_2030) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2582_2028) else False)][(-1)] if (symdic.symdic_kl_x58 == KL_CTX.KL_LOC_V2581_2027) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2580_2026) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2579_2024) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2578_2023) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_V2584_2031', tco_apply(shen_lazyderef, [KL_ARG_V2899_2019, KL_ARG_V2900_2020])), ([setattr(KL_CTX, 'KL_LOC_Hyp_2032', KL_CTX.KL_LOC_V2584_2031[1]), [tco_apply(shen_incinfs, []), tail_call(shen_by_hypothesis, [KL_ARG_V2897_2017, KL_ARG_V2898_2018, KL_CTX.KL_LOC_Hyp_2032, KL_ARG_V2900_2020, KL_ARG_V2901_2021])][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2584_2031) else False)][(-1)] if (KL_CTX.KL_LOC_Case_2022 == False) else KL_CTX.KL_LOC_Case_2022)][(-1)]
shen_add_fun('shen.by_hypothesis', shen_by_hypothesis, 5)

@tail_recursion
def shen_tx42x45def(KL_ARG_V2902_2033, KL_ARG_V2903_2034, KL_ARG_V2904_2035, KL_ARG_V2905_2036, KL_ARG_V2906_2037):

    class KL_Context:
        KL_LOC_V2572_2038 = None
        KL_LOC_V2573_2039 = None
        KL_LOC_V2574_2040 = None
        KL_LOC_F_2041 = None
        KL_LOC_X_2042 = None
        KL_LOC_E_2043 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_V2572_2038', tco_apply(shen_lazyderef, [KL_ARG_V2902_2033, KL_ARG_V2905_2036])), ([setattr(KL_CTX, 'KL_LOC_V2573_2039', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2572_2038[0], KL_ARG_V2905_2036])), ([setattr(KL_CTX, 'KL_LOC_V2574_2040', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2572_2038[1], KL_ARG_V2905_2036])), ([setattr(KL_CTX, 'KL_LOC_F_2041', KL_CTX.KL_LOC_V2574_2040[0]), [setattr(KL_CTX, 'KL_LOC_X_2042', KL_CTX.KL_LOC_V2574_2040[1]), [setattr(KL_CTX, 'KL_LOC_E_2043', tco_apply(shen_newpv, [KL_ARG_V2905_2036])), [tco_apply(shen_incinfs, []), tail_call(shen_tx42x45defh, [tco_apply(kl_compile, [symdic.symdic_shen_x60sigx43rulesx62, KL_CTX.KL_LOC_X_2042, (lambda KL_ARG_E_2044: (shen_simple_error(('parse error here: ' + tco_apply(shen_app, [KL_ARG_E_2044, '\r\n', symdic.symdic_shen_s]))) if shen_consp(KL_ARG_E_2044) else shen_simple_error('parse error\r\n')))]), KL_CTX.KL_LOC_F_2041, KL_ARG_V2903_2034, KL_ARG_V2904_2035, KL_ARG_V2905_2036, KL_ARG_V2906_2037])][(-1)]][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2574_2040) else False)][(-1)] if (symdic.symdic_kl_define == KL_CTX.KL_LOC_V2573_2039) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2572_2038) else False)][(-1)]
shen_add_fun('shen.t*-def', shen_tx42x45def, 5)

@tail_recursion
def shen_tx42x45defh(KL_ARG_V2907_2045, KL_ARG_V2908_2046, KL_ARG_V2909_2047, KL_ARG_V2910_2048, KL_ARG_V2911_2049, KL_ARG_V2912_2050):

    class KL_Context:
        KL_LOC_V2568_2051 = None
        KL_LOC_Sig_2052 = None
        KL_LOC_Rules_2053 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_V2568_2051', tco_apply(shen_lazyderef, [KL_ARG_V2907_2045, KL_ARG_V2911_2049])), ([setattr(KL_CTX, 'KL_LOC_Sig_2052', KL_CTX.KL_LOC_V2568_2051[0]), [setattr(KL_CTX, 'KL_LOC_Rules_2053', KL_CTX.KL_LOC_V2568_2051[1]), [tco_apply(shen_incinfs, []), tail_call(shen_tx42x45defhh, [KL_CTX.KL_LOC_Sig_2052, tco_apply(shen_ue, [KL_CTX.KL_LOC_Sig_2052]), KL_ARG_V2908_2046, KL_ARG_V2909_2047, KL_ARG_V2910_2048, KL_CTX.KL_LOC_Rules_2053, KL_ARG_V2911_2049, KL_ARG_V2912_2050])][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2568_2051) else False)][(-1)]
shen_add_fun('shen.t*-defh', shen_tx42x45defh, 6)

@tail_recursion
def shen_tx42x45defhh(KL_ARG_V2913_2054, KL_ARG_V2914_2055, KL_ARG_V2915_2056, KL_ARG_V2916_2057, KL_ARG_V2917_2058, KL_ARG_V2918_2059, KL_ARG_V2919_2060, KL_ARG_V2920_2061):
    global symdic
    return [tco_apply(shen_incinfs, []), tail_call(shen_tx42x45rules, [KL_ARG_V2918_2059, KL_ARG_V2914_2055, 1, KL_ARG_V2915_2056, [[KL_ARG_V2915_2056, [symdic.symdic_kl_x58, [KL_ARG_V2914_2055, []]]], KL_ARG_V2917_2058], KL_ARG_V2919_2060, (lambda : tail_call(shen_memo, [KL_ARG_V2915_2056, KL_ARG_V2913_2054, KL_ARG_V2916_2057, KL_ARG_V2919_2060, KL_ARG_V2920_2061]))])][(-1)]
shen_add_fun('shen.t*-defhh', shen_tx42x45defhh, 8)

@tail_recursion
def shen_memo(KL_ARG_V2921_2062, KL_ARG_V2922_2063, KL_ARG_V2923_2064, KL_ARG_V2924_2065, KL_ARG_V2925_2066):

    class KL_Context:
        KL_LOC_Jnk_2067 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Jnk_2067', tco_apply(shen_newpv, [KL_ARG_V2924_2065])), [tco_apply(shen_incinfs, []), tail_call(kl_unifyx33, [KL_ARG_V2923_2064, KL_ARG_V2922_2063, KL_ARG_V2924_2065, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Jnk_2067, apply(kl_declare, [tco_apply(shen_lazyderef, [KL_ARG_V2921_2062, KL_ARG_V2924_2065]), tco_apply(shen_lazyderef, [KL_ARG_V2923_2064, KL_ARG_V2924_2065])]), KL_ARG_V2924_2065, KL_ARG_V2925_2066]))])][(-1)]][(-1)]
shen_add_fun('shen.memo', shen_memo, 5)

@tail_recursion
def shen_x60sigx43rulesx62(KL_ARG_V2930_2068):

    class KL_Context:
        KL_LOC_Result_2069 = None
        KL_LOC_Parse_shen_x60signaturex62_2070 = None
        KL_LOC_Parse_shen_x60rulesx62_2071 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_2069', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60signaturex62_2070', tco_apply(shen_x60signaturex62, [KL_ARG_V2930_2068])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60rulesx62_2071', tco_apply(shen_x60rulesx62, [KL_CTX.KL_LOC_Parse_shen_x60signaturex62_2070])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60rulesx62_2071[0], [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60signaturex62_2070]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60rulesx62_2071])]]) if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60rulesx62_2071)) else tco_apply(kl_fail, []))][(-1)] if (not (tco_apply(kl_fail, []) == KL_CTX.KL_LOC_Parse_shen_x60signaturex62_2070)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if (KL_CTX.KL_LOC_Result_2069 == tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_2069)][(-1)]
shen_add_fun('shen.<sig+rules>', shen_x60sigx43rulesx62, 1)

@tail_recursion
def shen_ue(KL_ARG_V2931_2072):
    global symdic
    return (tail_call(kl_map, [symdic.symdic_shen_ue, KL_ARG_V2931_2072]) if shen_consp(KL_ARG_V2931_2072) else (tail_call(kl_concat, [symdic.symdic_kl_x38x38, KL_ARG_V2931_2072]) if tco_apply(kl_variablex63, [KL_ARG_V2931_2072]) else (KL_ARG_V2931_2072 if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.ue', shen_ue, 1)

@tail_recursion
def shen_ues(KL_ARG_V2936_2073):
    global symdic
    return ([KL_ARG_V2936_2073, []] if tco_apply(shen_uex63, [KL_ARG_V2936_2073]) else (tail_call(kl_union, [tco_apply(shen_ues, [KL_ARG_V2936_2073[0]]), tco_apply(shen_ues, [KL_ARG_V2936_2073[1]])]) if shen_consp(KL_ARG_V2936_2073) else ([] if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.ues', shen_ues, 1)

@tail_recursion
def shen_uex63(KL_ARG_V2937_2074):
    global symdic
    return (tail_call(shen_uex45hx63, [str(KL_ARG_V2937_2074)]) if tco_apply(kl_symbolx63, [KL_ARG_V2937_2074]) else False)
shen_add_fun('shen.ue?', shen_uex63, 1)

@tail_recursion
def shen_uex45hx63(KL_ARG_V2944_2075):
    global symdic
    return (True if (((('&' == KL_ARG_V2944_2075[1:][0]) if tco_apply(shen_x43stringx63, [KL_ARG_V2944_2075[1:]]) else False) if ('&' == KL_ARG_V2944_2075[0]) else False) if tco_apply(shen_x43stringx63, [KL_ARG_V2944_2075]) else False) else (False if True else shen_simple_error('condition failure')))
shen_add_fun('shen.ue-h?', shen_uex45hx63, 1)

@tail_recursion
def shen_tx42x45rules(KL_ARG_V2945_2076, KL_ARG_V2946_2077, KL_ARG_V2947_2078, KL_ARG_V2948_2079, KL_ARG_V2949_2080, KL_ARG_V2950_2081, KL_ARG_V2951_2082):

    class KL_Context:
        KL_LOC_Throwcontrol_2083 = None
        KL_LOC_Case_2084 = None
        KL_LOC_V2543_2085 = None
        KL_LOC_Case_2086 = None
        KL_LOC_V2544_2087 = None
        KL_LOC_V2545_2088 = None
        KL_LOC_V2546_2089 = None
        KL_LOC_V2547_2090 = None
        KL_LOC_Action_2091 = None
        KL_LOC_V2548_2092 = None
        KL_LOC_Rules_2093 = None
        KL_LOC_V2549_2094 = None
        KL_LOC_V2550_2095 = None
        KL_LOC_V2551_2096 = None
        KL_LOC_A_2097 = None
        KL_LOC_V2552_2098 = None
        KL_LOC_Case_2099 = None
        KL_LOC_V2553_2100 = None
        KL_LOC_Rule_2101 = None
        KL_LOC_Rules_2102 = None
        KL_LOC_Err_2103 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Throwcontrol_2083', tco_apply(shen_catchpoint, [])), tail_call(shen_cutpoint, [KL_CTX.KL_LOC_Throwcontrol_2083, [setattr(KL_CTX, 'KL_LOC_Case_2084', [setattr(KL_CTX, 'KL_LOC_V2543_2085', tco_apply(shen_lazyderef, [KL_ARG_V2945_2076, KL_ARG_V2950_2081])), ([tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V2951_2082])][(-1)] if ([] == KL_CTX.KL_LOC_V2543_2085) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_2086', [setattr(KL_CTX, 'KL_LOC_V2544_2087', tco_apply(shen_lazyderef, [KL_ARG_V2945_2076, KL_ARG_V2950_2081])), ([setattr(KL_CTX, 'KL_LOC_V2545_2088', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2544_2087[0], KL_ARG_V2950_2081])), ([setattr(KL_CTX, 'KL_LOC_V2546_2089', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2545_2088[0], KL_ARG_V2950_2081])), ([setattr(KL_CTX, 'KL_LOC_V2547_2090', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2545_2088[1], KL_ARG_V2950_2081])), ([setattr(KL_CTX, 'KL_LOC_Action_2091', KL_CTX.KL_LOC_V2547_2090[0]), [setattr(KL_CTX, 'KL_LOC_V2548_2092', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2547_2090[1], KL_ARG_V2950_2081])), ([setattr(KL_CTX, 'KL_LOC_Rules_2093', KL_CTX.KL_LOC_V2544_2087[1]), [setattr(KL_CTX, 'KL_LOC_V2549_2094', tco_apply(shen_lazyderef, [KL_ARG_V2946_2077, KL_ARG_V2950_2081])), ([setattr(KL_CTX, 'KL_LOC_V2550_2095', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2549_2094[0], KL_ARG_V2950_2081])), ([setattr(KL_CTX, 'KL_LOC_V2551_2096', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2549_2094[1], KL_ARG_V2950_2081])), ([setattr(KL_CTX, 'KL_LOC_A_2097', KL_CTX.KL_LOC_V2551_2096[0]), [setattr(KL_CTX, 'KL_LOC_V2552_2098', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2551_2096[1], KL_ARG_V2950_2081])), ([tco_apply(shen_incinfs, []), tco_apply(shen_tx42x45rule, [[[], [tco_apply(shen_ue, [KL_CTX.KL_LOC_Action_2091]), []]], KL_CTX.KL_LOC_A_2097, KL_ARG_V2949_2080, KL_ARG_V2950_2081, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2083, KL_ARG_V2950_2081, (lambda : tail_call(shen_tx42x45rules, [KL_CTX.KL_LOC_Rules_2093, KL_CTX.KL_LOC_A_2097, (KL_ARG_V2947_2078 + 1), KL_ARG_V2948_2079, KL_ARG_V2949_2080, KL_ARG_V2950_2081, KL_ARG_V2951_2082]))]))])][(-1)] if ([] == KL_CTX.KL_LOC_V2552_2098) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2551_2096) else False)][(-1)] if (symdic.symdic_kl_x45x45x62 == KL_CTX.KL_LOC_V2550_2095) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2549_2094) else False)][(-1)]][(-1)] if ([] == KL_CTX.KL_LOC_V2548_2092) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2547_2090) else False)][(-1)] if ([] == KL_CTX.KL_LOC_V2546_2089) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2545_2088) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2544_2087) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_2099', [setattr(KL_CTX, 'KL_LOC_V2553_2100', tco_apply(shen_lazyderef, [KL_ARG_V2945_2076, KL_ARG_V2950_2081])), ([setattr(KL_CTX, 'KL_LOC_Rule_2101', KL_CTX.KL_LOC_V2553_2100[0]), [setattr(KL_CTX, 'KL_LOC_Rules_2102', KL_CTX.KL_LOC_V2553_2100[1]), [tco_apply(shen_incinfs, []), tco_apply(shen_tx42x45rule, [tco_apply(shen_ue, [KL_CTX.KL_LOC_Rule_2101]), KL_ARG_V2946_2077, KL_ARG_V2949_2080, KL_ARG_V2950_2081, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2083, KL_ARG_V2950_2081, (lambda : tail_call(shen_tx42x45rules, [KL_CTX.KL_LOC_Rules_2102, KL_ARG_V2946_2077, (KL_ARG_V2947_2078 + 1), KL_ARG_V2948_2079, KL_ARG_V2949_2080, KL_ARG_V2950_2081, KL_ARG_V2951_2082]))]))])][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2553_2100) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Err_2103', tco_apply(shen_newpv, [KL_ARG_V2950_2081])), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_CTX.KL_LOC_Err_2103, shen_simple_error(('type error in rule ' + tco_apply(shen_app, [tco_apply(shen_lazyderef, [KL_ARG_V2947_2078, KL_ARG_V2950_2081]), (' of ' + tco_apply(shen_app, [tco_apply(shen_lazyderef, [KL_ARG_V2948_2079, KL_ARG_V2950_2081]), '', symdic.symdic_shen_a])), symdic.symdic_shen_a]))), KL_ARG_V2950_2081, KL_ARG_V2951_2082])][(-1)]][(-1)] if (KL_CTX.KL_LOC_Case_2099 == False) else KL_CTX.KL_LOC_Case_2099)][(-1)] if (KL_CTX.KL_LOC_Case_2086 == False) else KL_CTX.KL_LOC_Case_2086)][(-1)] if (KL_CTX.KL_LOC_Case_2084 == False) else KL_CTX.KL_LOC_Case_2084)][(-1)]])][(-1)]
shen_add_fun('shen.t*-rules', shen_tx42x45rules, 7)

@tail_recursion
def shen_tx42x45rule(KL_ARG_V2952_2104, KL_ARG_V2953_2105, KL_ARG_V2954_2106, KL_ARG_V2955_2107, KL_ARG_V2956_2108):

    class KL_Context:
        KL_LOC_Throwcontrol_2109 = None
        KL_LOC_Case_2110 = None
        KL_LOC_V2525_2111 = None
        KL_LOC_V2526_2112 = None
        KL_LOC_V2527_2113 = None
        KL_LOC_Action_2114 = None
        KL_LOC_V2528_2115 = None
        KL_LOC_V2529_2116 = None
        KL_LOC_V2530_2117 = None
        KL_LOC_Pattern_2118 = None
        KL_LOC_Patterns_2119 = None
        KL_LOC_V2531_2120 = None
        KL_LOC_Action_2121 = None
        KL_LOC_V2532_2122 = None
        KL_LOC_V2533_2123 = None
        KL_LOC_A_2124 = None
        KL_LOC_V2534_2125 = None
        KL_LOC_V2535_2126 = None
        KL_LOC_V2536_2127 = None
        KL_LOC_B_2128 = None
        KL_LOC_V2537_2129 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Throwcontrol_2109', tco_apply(shen_catchpoint, [])), tail_call(shen_cutpoint, [KL_CTX.KL_LOC_Throwcontrol_2109, [setattr(KL_CTX, 'KL_LOC_Case_2110', [setattr(KL_CTX, 'KL_LOC_V2525_2111', tco_apply(shen_lazyderef, [KL_ARG_V2952_2104, KL_ARG_V2955_2107])), ([setattr(KL_CTX, 'KL_LOC_V2526_2112', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2525_2111[0], KL_ARG_V2955_2107])), ([setattr(KL_CTX, 'KL_LOC_V2527_2113', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2525_2111[1], KL_ARG_V2955_2107])), ([setattr(KL_CTX, 'KL_LOC_Action_2114', KL_CTX.KL_LOC_V2527_2113[0]), [setattr(KL_CTX, 'KL_LOC_V2528_2115', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2527_2113[1], KL_ARG_V2955_2107])), ([tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2109, KL_ARG_V2955_2107, (lambda : tail_call(shen_tx42x45action, [tco_apply(shen_curry, [KL_CTX.KL_LOC_Action_2114]), KL_ARG_V2953_2105, KL_ARG_V2954_2106, KL_ARG_V2955_2107, KL_ARG_V2956_2108]))])][(-1)] if ([] == KL_CTX.KL_LOC_V2528_2115) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2527_2113) else False)][(-1)] if ([] == KL_CTX.KL_LOC_V2526_2112) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2525_2111) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_V2529_2116', tco_apply(shen_lazyderef, [KL_ARG_V2952_2104, KL_ARG_V2955_2107])), ([setattr(KL_CTX, 'KL_LOC_V2530_2117', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2529_2116[0], KL_ARG_V2955_2107])), ([setattr(KL_CTX, 'KL_LOC_Pattern_2118', KL_CTX.KL_LOC_V2530_2117[0]), [setattr(KL_CTX, 'KL_LOC_Patterns_2119', KL_CTX.KL_LOC_V2530_2117[1]), [setattr(KL_CTX, 'KL_LOC_V2531_2120', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2529_2116[1], KL_ARG_V2955_2107])), ([setattr(KL_CTX, 'KL_LOC_Action_2121', KL_CTX.KL_LOC_V2531_2120[0]), [setattr(KL_CTX, 'KL_LOC_V2532_2122', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2531_2120[1], KL_ARG_V2955_2107])), ([setattr(KL_CTX, 'KL_LOC_V2533_2123', tco_apply(shen_lazyderef, [KL_ARG_V2953_2105, KL_ARG_V2955_2107])), ([setattr(KL_CTX, 'KL_LOC_A_2124', KL_CTX.KL_LOC_V2533_2123[0]), [setattr(KL_CTX, 'KL_LOC_V2534_2125', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2533_2123[1], KL_ARG_V2955_2107])), ([setattr(KL_CTX, 'KL_LOC_V2535_2126', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2534_2125[0], KL_ARG_V2955_2107])), ([setattr(KL_CTX, 'KL_LOC_V2536_2127', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2534_2125[1], KL_ARG_V2955_2107])), ([setattr(KL_CTX, 'KL_LOC_B_2128', KL_CTX.KL_LOC_V2536_2127[0]), [setattr(KL_CTX, 'KL_LOC_V2537_2129', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2536_2127[1], KL_ARG_V2955_2107])), ([tco_apply(shen_incinfs, []), tco_apply(shen_tx42x45pattern, [KL_CTX.KL_LOC_Pattern_2118, KL_CTX.KL_LOC_A_2124, KL_ARG_V2955_2107, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2109, KL_ARG_V2955_2107, (lambda : tail_call(shen_tx42x45rule, [[KL_CTX.KL_LOC_Patterns_2119, [KL_CTX.KL_LOC_Action_2121, []]], KL_CTX.KL_LOC_B_2128, [[KL_CTX.KL_LOC_Pattern_2118, [symdic.symdic_kl_x58, [KL_CTX.KL_LOC_A_2124, []]]], KL_ARG_V2954_2106], KL_ARG_V2955_2107, KL_ARG_V2956_2108]))]))])][(-1)] if ([] == KL_CTX.KL_LOC_V2537_2129) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2536_2127) else False)][(-1)] if (symdic.symdic_kl_x45x45x62 == KL_CTX.KL_LOC_V2535_2126) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2534_2125) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2533_2123) else False)][(-1)] if ([] == KL_CTX.KL_LOC_V2532_2122) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2531_2120) else False)][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2530_2117) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2529_2116) else False)][(-1)] if (KL_CTX.KL_LOC_Case_2110 == False) else KL_CTX.KL_LOC_Case_2110)][(-1)]])][(-1)]
shen_add_fun('shen.t*-rule', shen_tx42x45rule, 5)

@tail_recursion
def shen_tx42x45action(KL_ARG_V2957_2130, KL_ARG_V2958_2131, KL_ARG_V2959_2132, KL_ARG_V2960_2133, KL_ARG_V2961_2134):

    class KL_Context:
        KL_LOC_Throwcontrol_2135 = None
        KL_LOC_Case_2136 = None
        KL_LOC_V2502_2137 = None
        KL_LOC_V2503_2138 = None
        KL_LOC_V2504_2139 = None
        KL_LOC_P_2140 = None
        KL_LOC_V2505_2141 = None
        KL_LOC_Action_2142 = None
        KL_LOC_V2506_2143 = None
        KL_LOC_Case_2144 = None
        KL_LOC_V2507_2145 = None
        KL_LOC_V2508_2146 = None
        KL_LOC_V2509_2147 = None
        KL_LOC_V2510_2148 = None
        KL_LOC_V2511_2149 = None
        KL_LOC_V2512_2150 = None
        KL_LOC_V2513_2151 = None
        KL_LOC_F_2152 = None
        KL_LOC_V2514_2153 = None
        KL_LOC_V2515_2154 = None
        KL_LOC_Action_2155 = None
        KL_LOC_V2516_2156 = None
        KL_LOC_V2517_2157 = None
        KL_LOC_Case_2158 = None
        KL_LOC_V2518_2159 = None
        KL_LOC_V2519_2160 = None
        KL_LOC_V2520_2161 = None
        KL_LOC_Action_2162 = None
        KL_LOC_V2521_2163 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Throwcontrol_2135', tco_apply(shen_catchpoint, [])), tail_call(shen_cutpoint, [KL_CTX.KL_LOC_Throwcontrol_2135, [setattr(KL_CTX, 'KL_LOC_Case_2136', [setattr(KL_CTX, 'KL_LOC_V2502_2137', tco_apply(shen_lazyderef, [KL_ARG_V2957_2130, KL_ARG_V2960_2133])), ([setattr(KL_CTX, 'KL_LOC_V2503_2138', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2502_2137[0], KL_ARG_V2960_2133])), ([setattr(KL_CTX, 'KL_LOC_V2504_2139', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2502_2137[1], KL_ARG_V2960_2133])), ([setattr(KL_CTX, 'KL_LOC_P_2140', KL_CTX.KL_LOC_V2504_2139[0]), [setattr(KL_CTX, 'KL_LOC_V2505_2141', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2504_2139[1], KL_ARG_V2960_2133])), ([setattr(KL_CTX, 'KL_LOC_Action_2142', KL_CTX.KL_LOC_V2505_2141[0]), [setattr(KL_CTX, 'KL_LOC_V2506_2143', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2505_2141[1], KL_ARG_V2960_2133])), ([tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2135, KL_ARG_V2960_2133, (lambda : tail_call(shen_tx42, [[KL_CTX.KL_LOC_P_2140, [symdic.symdic_kl_x58, [symdic.symdic_kl_boolean, []]]], KL_ARG_V2959_2132, KL_ARG_V2960_2133, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2135, KL_ARG_V2960_2133, (lambda : tail_call(shen_tx42x45action, [KL_CTX.KL_LOC_Action_2142, KL_ARG_V2958_2131, [[KL_CTX.KL_LOC_P_2140, [symdic.symdic_kl_x58, [symdic.symdic_kl_verified, []]]], KL_ARG_V2959_2132], KL_ARG_V2960_2133, KL_ARG_V2961_2134]))]))]))])][(-1)] if ([] == KL_CTX.KL_LOC_V2506_2143) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2505_2141) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2504_2139) else False)][(-1)] if (symdic.symdic_kl_where == KL_CTX.KL_LOC_V2503_2138) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2502_2137) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_2144', [setattr(KL_CTX, 'KL_LOC_V2507_2145', tco_apply(shen_lazyderef, [KL_ARG_V2957_2130, KL_ARG_V2960_2133])), ([setattr(KL_CTX, 'KL_LOC_V2508_2146', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2507_2145[0], KL_ARG_V2960_2133])), ([setattr(KL_CTX, 'KL_LOC_V2509_2147', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2507_2145[1], KL_ARG_V2960_2133])), ([setattr(KL_CTX, 'KL_LOC_V2510_2148', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2509_2147[0], KL_ARG_V2960_2133])), ([setattr(KL_CTX, 'KL_LOC_V2511_2149', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2510_2148[0], KL_ARG_V2960_2133])), ([setattr(KL_CTX, 'KL_LOC_V2512_2150', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2511_2149[0], KL_ARG_V2960_2133])), ([setattr(KL_CTX, 'KL_LOC_V2513_2151', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2511_2149[1], KL_ARG_V2960_2133])), ([setattr(KL_CTX, 'KL_LOC_F_2152', KL_CTX.KL_LOC_V2513_2151[0]), [setattr(KL_CTX, 'KL_LOC_V2514_2153', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2513_2151[1], KL_ARG_V2960_2133])), ([setattr(KL_CTX, 'KL_LOC_V2515_2154', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2510_2148[1], KL_ARG_V2960_2133])), ([setattr(KL_CTX, 'KL_LOC_Action_2155', KL_CTX.KL_LOC_V2515_2154[0]), [setattr(KL_CTX, 'KL_LOC_V2516_2156', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2515_2154[1], KL_ARG_V2960_2133])), ([setattr(KL_CTX, 'KL_LOC_V2517_2157', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2509_2147[1], KL_ARG_V2960_2133])), ([tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2135, KL_ARG_V2960_2133, (lambda : tail_call(shen_tx42x45action, [[symdic.symdic_kl_where, [[symdic.symdic_kl_not, [[KL_CTX.KL_LOC_F_2152, [KL_CTX.KL_LOC_Action_2155, []]], []]], [KL_CTX.KL_LOC_Action_2155, []]]], KL_ARG_V2958_2131, KL_ARG_V2959_2132, KL_ARG_V2960_2133, KL_ARG_V2961_2134]))])][(-1)] if ([] == KL_CTX.KL_LOC_V2517_2157) else False)][(-1)] if ([] == KL_CTX.KL_LOC_V2516_2156) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2515_2154) else False)][(-1)] if ([] == KL_CTX.KL_LOC_V2514_2153) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2513_2151) else False)][(-1)] if (symdic.symdic_kl_failx45if == KL_CTX.KL_LOC_V2512_2150) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2511_2149) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2510_2148) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2509_2147) else False)][(-1)] if (symdic.symdic_shen_choicepointx33 == KL_CTX.KL_LOC_V2508_2146) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2507_2145) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_2158', [setattr(KL_CTX, 'KL_LOC_V2518_2159', tco_apply(shen_lazyderef, [KL_ARG_V2957_2130, KL_ARG_V2960_2133])), ([setattr(KL_CTX, 'KL_LOC_V2519_2160', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2518_2159[0], KL_ARG_V2960_2133])), ([setattr(KL_CTX, 'KL_LOC_V2520_2161', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2518_2159[1], KL_ARG_V2960_2133])), ([setattr(KL_CTX, 'KL_LOC_Action_2162', KL_CTX.KL_LOC_V2520_2161[0]), [setattr(KL_CTX, 'KL_LOC_V2521_2163', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2520_2161[1], KL_ARG_V2960_2133])), ([tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2135, KL_ARG_V2960_2133, (lambda : tail_call(shen_tx42x45action, [[symdic.symdic_kl_where, [[symdic.symdic_kl_not, [[[symdic.symdic_kl_x61, [KL_CTX.KL_LOC_Action_2162, []]], [[symdic.symdic_kl_fail, []], []]], []]], [KL_CTX.KL_LOC_Action_2162, []]]], KL_ARG_V2958_2131, KL_ARG_V2959_2132, KL_ARG_V2960_2133, KL_ARG_V2961_2134]))])][(-1)] if ([] == KL_CTX.KL_LOC_V2521_2163) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2520_2161) else False)][(-1)] if (symdic.symdic_shen_choicepointx33 == KL_CTX.KL_LOC_V2519_2160) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2518_2159) else False)][(-1)]), ([tco_apply(shen_incinfs, []), tco_apply(shen_tx42, [[KL_ARG_V2957_2130, [symdic.symdic_kl_x58, [KL_ARG_V2958_2131, []]]], KL_ARG_V2959_2132, KL_ARG_V2960_2133, KL_ARG_V2961_2134])][(-1)] if (KL_CTX.KL_LOC_Case_2158 == False) else KL_CTX.KL_LOC_Case_2158)][(-1)] if (KL_CTX.KL_LOC_Case_2144 == False) else KL_CTX.KL_LOC_Case_2144)][(-1)] if (KL_CTX.KL_LOC_Case_2136 == False) else KL_CTX.KL_LOC_Case_2136)][(-1)]])][(-1)]
shen_add_fun('shen.t*-action', shen_tx42x45action, 5)

@tail_recursion
def shen_tx42x45pattern(KL_ARG_V2962_2164, KL_ARG_V2963_2165, KL_ARG_V2964_2166, KL_ARG_V2965_2167):

    class KL_Context:
        KL_LOC_Throwcontrol_2168 = None
        KL_LOC_Hyp_2169 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Throwcontrol_2168', tco_apply(shen_catchpoint, [])), tail_call(shen_cutpoint, [KL_CTX.KL_LOC_Throwcontrol_2168, [setattr(KL_CTX, 'KL_LOC_Hyp_2169', tco_apply(shen_newpv, [KL_ARG_V2964_2166])), [tco_apply(shen_incinfs, []), tco_apply(shen_tmsx45x62hyp, [tco_apply(shen_ues, [KL_ARG_V2962_2164]), KL_CTX.KL_LOC_Hyp_2169, KL_ARG_V2964_2166, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2168, KL_ARG_V2964_2166, (lambda : tail_call(shen_tx42, [[KL_ARG_V2962_2164, [symdic.symdic_kl_x58, [KL_ARG_V2963_2165, []]]], KL_CTX.KL_LOC_Hyp_2169, KL_ARG_V2964_2166, KL_ARG_V2965_2167]))]))])][(-1)]][(-1)]])][(-1)]
shen_add_fun('shen.t*-pattern', shen_tx42x45pattern, 4)

@tail_recursion
def shen_tmsx45x62hyp(KL_ARG_V2966_2170, KL_ARG_V2967_2171, KL_ARG_V2968_2172, KL_ARG_V2969_2173):

    class KL_Context:
        KL_LOC_Case_2174 = None
        KL_LOC_V2486_2175 = None
        KL_LOC_V2487_2176 = None
        KL_LOC_Result_2177 = None
        KL_LOC_V2488_2178 = None
        KL_LOC_Tm2483_2179 = None
        KL_LOC_Tms_2180 = None
        KL_LOC_V2489_2181 = None
        KL_LOC_V2490_2182 = None
        KL_LOC_Tm_2183 = None
        KL_LOC_V2491_2184 = None
        KL_LOC_V2492_2185 = None
        KL_LOC_V2493_2186 = None
        KL_LOC_A_2187 = None
        KL_LOC_V2494_2188 = None
        KL_LOC_Hyp_2189 = None
        KL_LOC_Result_2190 = None
        KL_LOC_Hyp_2191 = None
        KL_LOC_A_2192 = None
        KL_LOC_Result_2193 = None
        KL_LOC_Hyp_2194 = None
        KL_LOC_Result_2195 = None
        KL_LOC_V2495_2196 = None
        KL_LOC_A_2197 = None
        KL_LOC_V2496_2198 = None
        KL_LOC_Hyp_2199 = None
        KL_LOC_Result_2200 = None
        KL_LOC_Hyp_2201 = None
        KL_LOC_A_2202 = None
        KL_LOC_Result_2203 = None
        KL_LOC_Hyp_2204 = None
        KL_LOC_A_2205 = None
        KL_LOC_Result_2206 = None
        KL_LOC_Hyp_2207 = None
        KL_LOC_Tm_2208 = None
        KL_LOC_A_2209 = None
        KL_LOC_Result_2210 = None
        KL_LOC_Hyp_2211 = None
        KL_LOC_Tm_2212 = None
        KL_LOC_A_2213 = None
        KL_LOC_Hyp_2214 = None
        KL_LOC_Result_2215 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Case_2174', [setattr(KL_CTX, 'KL_LOC_V2486_2175', tco_apply(shen_lazyderef, [KL_ARG_V2966_2170, KL_ARG_V2968_2172])), ([setattr(KL_CTX, 'KL_LOC_V2487_2176', tco_apply(shen_lazyderef, [KL_ARG_V2967_2171, KL_ARG_V2968_2172])), ([tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V2969_2173])][(-1)] if ([] == KL_CTX.KL_LOC_V2487_2176) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2487_2176, [], KL_ARG_V2968_2172]), [setattr(KL_CTX, 'KL_LOC_Result_2177', [tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V2969_2173])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2487_2176, KL_ARG_V2968_2172]), KL_CTX.KL_LOC_Result_2177][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2487_2176]) else False))][(-1)] if ([] == KL_CTX.KL_LOC_V2486_2175) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_V2488_2178', tco_apply(shen_lazyderef, [KL_ARG_V2966_2170, KL_ARG_V2968_2172])), ([setattr(KL_CTX, 'KL_LOC_Tm2483_2179', KL_CTX.KL_LOC_V2488_2178[0]), [setattr(KL_CTX, 'KL_LOC_Tms_2180', KL_CTX.KL_LOC_V2488_2178[1]), [setattr(KL_CTX, 'KL_LOC_V2489_2181', tco_apply(shen_lazyderef, [KL_ARG_V2967_2171, KL_ARG_V2968_2172])), ([setattr(KL_CTX, 'KL_LOC_V2490_2182', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2489_2181[0], KL_ARG_V2968_2172])), ([setattr(KL_CTX, 'KL_LOC_Tm_2183', KL_CTX.KL_LOC_V2490_2182[0]), [setattr(KL_CTX, 'KL_LOC_V2491_2184', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2490_2182[1], KL_ARG_V2968_2172])), ([setattr(KL_CTX, 'KL_LOC_V2492_2185', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2491_2184[0], KL_ARG_V2968_2172])), ([setattr(KL_CTX, 'KL_LOC_V2493_2186', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2491_2184[1], KL_ARG_V2968_2172])), ([setattr(KL_CTX, 'KL_LOC_A_2187', KL_CTX.KL_LOC_V2493_2186[0]), [setattr(KL_CTX, 'KL_LOC_V2494_2188', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2493_2186[1], KL_ARG_V2968_2172])), ([setattr(KL_CTX, 'KL_LOC_Hyp_2189', KL_CTX.KL_LOC_V2489_2181[1]), [tco_apply(shen_incinfs, []), tail_call(kl_unifyx33, [KL_CTX.KL_LOC_Tm_2183, KL_CTX.KL_LOC_Tm2483_2179, KL_ARG_V2968_2172, (lambda : tail_call(shen_tmsx45x62hyp, [KL_CTX.KL_LOC_Tms_2180, KL_CTX.KL_LOC_Hyp_2189, KL_ARG_V2968_2172, KL_ARG_V2969_2173]))])][(-1)]][(-1)] if ([] == KL_CTX.KL_LOC_V2494_2188) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2494_2188, [], KL_ARG_V2968_2172]), [setattr(KL_CTX, 'KL_LOC_Result_2190', [setattr(KL_CTX, 'KL_LOC_Hyp_2191', KL_CTX.KL_LOC_V2489_2181[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_Tm_2183, KL_CTX.KL_LOC_Tm2483_2179, KL_ARG_V2968_2172, (lambda : tail_call(shen_tmsx45x62hyp, [KL_CTX.KL_LOC_Tms_2180, KL_CTX.KL_LOC_Hyp_2191, KL_ARG_V2968_2172, KL_ARG_V2969_2173]))])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2494_2188, KL_ARG_V2968_2172]), KL_CTX.KL_LOC_Result_2190][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2494_2188]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2493_2186) else ([setattr(KL_CTX, 'KL_LOC_A_2192', tco_apply(shen_newpv, [KL_ARG_V2968_2172])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2493_2186, [KL_CTX.KL_LOC_A_2192, []], KL_ARG_V2968_2172]), [setattr(KL_CTX, 'KL_LOC_Result_2193', [setattr(KL_CTX, 'KL_LOC_Hyp_2194', KL_CTX.KL_LOC_V2489_2181[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_Tm_2183, KL_CTX.KL_LOC_Tm2483_2179, KL_ARG_V2968_2172, (lambda : tail_call(shen_tmsx45x62hyp, [KL_CTX.KL_LOC_Tms_2180, KL_CTX.KL_LOC_Hyp_2194, KL_ARG_V2968_2172, KL_ARG_V2969_2173]))])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2493_2186, KL_ARG_V2968_2172]), KL_CTX.KL_LOC_Result_2193][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2493_2186]) else False))][(-1)] if (symdic.symdic_kl_x58 == KL_CTX.KL_LOC_V2492_2185) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2492_2185, symdic.symdic_kl_x58, KL_ARG_V2968_2172]), [setattr(KL_CTX, 'KL_LOC_Result_2195', [setattr(KL_CTX, 'KL_LOC_V2495_2196', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2491_2184[1], KL_ARG_V2968_2172])), ([setattr(KL_CTX, 'KL_LOC_A_2197', KL_CTX.KL_LOC_V2495_2196[0]), [setattr(KL_CTX, 'KL_LOC_V2496_2198', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2495_2196[1], KL_ARG_V2968_2172])), ([setattr(KL_CTX, 'KL_LOC_Hyp_2199', KL_CTX.KL_LOC_V2489_2181[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_Tm_2183, KL_CTX.KL_LOC_Tm2483_2179, KL_ARG_V2968_2172, (lambda : tail_call(shen_tmsx45x62hyp, [KL_CTX.KL_LOC_Tms_2180, KL_CTX.KL_LOC_Hyp_2199, KL_ARG_V2968_2172, KL_ARG_V2969_2173]))])][(-1)]][(-1)] if ([] == KL_CTX.KL_LOC_V2496_2198) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2496_2198, [], KL_ARG_V2968_2172]), [setattr(KL_CTX, 'KL_LOC_Result_2200', [setattr(KL_CTX, 'KL_LOC_Hyp_2201', KL_CTX.KL_LOC_V2489_2181[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_Tm_2183, KL_CTX.KL_LOC_Tm2483_2179, KL_ARG_V2968_2172, (lambda : tail_call(shen_tmsx45x62hyp, [KL_CTX.KL_LOC_Tms_2180, KL_CTX.KL_LOC_Hyp_2201, KL_ARG_V2968_2172, KL_ARG_V2969_2173]))])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2496_2198, KL_ARG_V2968_2172]), KL_CTX.KL_LOC_Result_2200][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2496_2198]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2495_2196) else ([setattr(KL_CTX, 'KL_LOC_A_2202', tco_apply(shen_newpv, [KL_ARG_V2968_2172])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2495_2196, [KL_CTX.KL_LOC_A_2202, []], KL_ARG_V2968_2172]), [setattr(KL_CTX, 'KL_LOC_Result_2203', [setattr(KL_CTX, 'KL_LOC_Hyp_2204', KL_CTX.KL_LOC_V2489_2181[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_Tm_2183, KL_CTX.KL_LOC_Tm2483_2179, KL_ARG_V2968_2172, (lambda : tail_call(shen_tmsx45x62hyp, [KL_CTX.KL_LOC_Tms_2180, KL_CTX.KL_LOC_Hyp_2204, KL_ARG_V2968_2172, KL_ARG_V2969_2173]))])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2495_2196, KL_ARG_V2968_2172]), KL_CTX.KL_LOC_Result_2203][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2495_2196]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2492_2185, KL_ARG_V2968_2172]), KL_CTX.KL_LOC_Result_2195][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2492_2185]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2491_2184) else ([setattr(KL_CTX, 'KL_LOC_A_2205', tco_apply(shen_newpv, [KL_ARG_V2968_2172])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2491_2184, [symdic.symdic_kl_x58, [KL_CTX.KL_LOC_A_2205, []]], KL_ARG_V2968_2172]), [setattr(KL_CTX, 'KL_LOC_Result_2206', [setattr(KL_CTX, 'KL_LOC_Hyp_2207', KL_CTX.KL_LOC_V2489_2181[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_Tm_2183, KL_CTX.KL_LOC_Tm2483_2179, KL_ARG_V2968_2172, (lambda : tail_call(shen_tmsx45x62hyp, [KL_CTX.KL_LOC_Tms_2180, KL_CTX.KL_LOC_Hyp_2207, KL_ARG_V2968_2172, KL_ARG_V2969_2173]))])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2491_2184, KL_ARG_V2968_2172]), KL_CTX.KL_LOC_Result_2206][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2491_2184]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2490_2182) else ([setattr(KL_CTX, 'KL_LOC_Tm_2208', tco_apply(shen_newpv, [KL_ARG_V2968_2172])), [setattr(KL_CTX, 'KL_LOC_A_2209', tco_apply(shen_newpv, [KL_ARG_V2968_2172])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2490_2182, [KL_CTX.KL_LOC_Tm_2208, [symdic.symdic_kl_x58, [KL_CTX.KL_LOC_A_2209, []]]], KL_ARG_V2968_2172]), [setattr(KL_CTX, 'KL_LOC_Result_2210', [setattr(KL_CTX, 'KL_LOC_Hyp_2211', KL_CTX.KL_LOC_V2489_2181[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_Tm_2208, KL_CTX.KL_LOC_Tm2483_2179, KL_ARG_V2968_2172, (lambda : tail_call(shen_tmsx45x62hyp, [KL_CTX.KL_LOC_Tms_2180, KL_CTX.KL_LOC_Hyp_2211, KL_ARG_V2968_2172, KL_ARG_V2969_2173]))])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2490_2182, KL_ARG_V2968_2172]), KL_CTX.KL_LOC_Result_2210][(-1)]][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2490_2182]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2489_2181) else ([setattr(KL_CTX, 'KL_LOC_Tm_2212', tco_apply(shen_newpv, [KL_ARG_V2968_2172])), [setattr(KL_CTX, 'KL_LOC_A_2213', tco_apply(shen_newpv, [KL_ARG_V2968_2172])), [setattr(KL_CTX, 'KL_LOC_Hyp_2214', tco_apply(shen_newpv, [KL_ARG_V2968_2172])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2489_2181, [[KL_CTX.KL_LOC_Tm_2212, [symdic.symdic_kl_x58, [KL_CTX.KL_LOC_A_2213, []]]], KL_CTX.KL_LOC_Hyp_2214], KL_ARG_V2968_2172]), [setattr(KL_CTX, 'KL_LOC_Result_2215', [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_Tm_2212, KL_CTX.KL_LOC_Tm2483_2179, KL_ARG_V2968_2172, (lambda : tail_call(shen_tmsx45x62hyp, [KL_CTX.KL_LOC_Tms_2180, KL_CTX.KL_LOC_Hyp_2214, KL_ARG_V2968_2172, KL_ARG_V2969_2173]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2489_2181, KL_ARG_V2968_2172]), KL_CTX.KL_LOC_Result_2215][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2489_2181]) else False))][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2488_2178) else False)][(-1)] if (KL_CTX.KL_LOC_Case_2174 == False) else KL_CTX.KL_LOC_Case_2174)][(-1)]
shen_add_fun('shen.tms->hyp', shen_tmsx45x62hyp, 4)

@tail_recursion
def kl_findall(KL_ARG_V2970_2216, KL_ARG_V2971_2217, KL_ARG_V2972_2218, KL_ARG_V2973_2219, KL_ARG_V2974_2220):

    class KL_Context:
        KL_LOC_B_2221 = None
        KL_LOC_A_2222 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_B_2221', tco_apply(shen_newpv, [KL_ARG_V2973_2219])), [setattr(KL_CTX, 'KL_LOC_A_2222', tco_apply(shen_newpv, [KL_ARG_V2973_2219])), [tco_apply(shen_incinfs, []), tail_call(kl_bind, [KL_CTX.KL_LOC_A_2222, tco_apply(kl_gensym, [symdic.symdic_shen_a]), KL_ARG_V2973_2219, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_B_2221, shen_set(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_2222, KL_ARG_V2973_2219]), []), KL_ARG_V2973_2219, (lambda : tail_call(shen_findallhelp, [KL_ARG_V2970_2216, KL_ARG_V2971_2217, KL_ARG_V2972_2218, KL_CTX.KL_LOC_A_2222, KL_ARG_V2973_2219, KL_ARG_V2974_2220]))]))])][(-1)]][(-1)]][(-1)]
shen_add_fun('findall', kl_findall, 5)

@tail_recursion
def shen_findallhelp(KL_ARG_V2975_2223, KL_ARG_V2976_2224, KL_ARG_V2977_2225, KL_ARG_V2978_2226, KL_ARG_V2979_2227, KL_ARG_V2980_2228):

    class KL_Context:
        KL_LOC_Case_2229 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Case_2229', [tco_apply(shen_incinfs, []), tco_apply(kl_call, [KL_ARG_V2976_2224, KL_ARG_V2979_2227, (lambda : tail_call(shen_remember, [KL_ARG_V2978_2226, KL_ARG_V2975_2223, KL_ARG_V2979_2227, (lambda : tail_call(kl_fwhen, [False, KL_ARG_V2979_2227, KL_ARG_V2980_2228]))]))])][(-1)]), ([tco_apply(shen_incinfs, []), tail_call(kl_bind, [KL_ARG_V2977_2225, shen_get(tco_apply(shen_lazyderef, [KL_ARG_V2978_2226, KL_ARG_V2979_2227])), KL_ARG_V2979_2227, KL_ARG_V2980_2228])][(-1)] if (KL_CTX.KL_LOC_Case_2229 == False) else KL_CTX.KL_LOC_Case_2229)][(-1)]
shen_add_fun('shen.findallhelp', shen_findallhelp, 6)

@tail_recursion
def shen_remember(KL_ARG_V2981_2230, KL_ARG_V2982_2231, KL_ARG_V2983_2232, KL_ARG_V2984_2233):

    class KL_Context:
        KL_LOC_B_2234 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_B_2234', tco_apply(shen_newpv, [KL_ARG_V2983_2232])), [tco_apply(shen_incinfs, []), tail_call(kl_bind, [KL_CTX.KL_LOC_B_2234, shen_set(tco_apply(shen_deref, [KL_ARG_V2981_2230, KL_ARG_V2983_2232]), [tco_apply(shen_deref, [KL_ARG_V2982_2231, KL_ARG_V2983_2232]), shen_get(tco_apply(shen_deref, [KL_ARG_V2981_2230, KL_ARG_V2983_2232]))]), KL_ARG_V2983_2232, KL_ARG_V2984_2233])][(-1)]][(-1)]
shen_add_fun('shen.remember', shen_remember, 4)

@tail_recursion
def shen_tx42x45defcc(KL_ARG_V2985_2235, KL_ARG_V2986_2236, KL_ARG_V2987_2237, KL_ARG_V2988_2238, KL_ARG_V2989_2239):

    class KL_Context:
        KL_LOC_Throwcontrol_2240 = None
        KL_LOC_V2459_2241 = None
        KL_LOC_V2460_2242 = None
        KL_LOC_V2461_2243 = None
        KL_LOC_F_2244 = None
        KL_LOC_V2462_2245 = None
        KL_LOC_V2463_2246 = None
        KL_LOC_V2464_2247 = None
        KL_LOC_V2465_2248 = None
        KL_LOC_V2466_2249 = None
        KL_LOC_V2467_2250 = None
        KL_LOC_A_2251 = None
        KL_LOC_V2468_2252 = None
        KL_LOC_V2469_2253 = None
        KL_LOC_V2470_2254 = None
        KL_LOC_V2471_2255 = None
        KL_LOC_B_2256 = None
        KL_LOC_V2472_2257 = None
        KL_LOC_V2473_2258 = None
        KL_LOC_Rest_2259 = None
        KL_LOC_Restx38_2260 = None
        KL_LOC_Restx38x38_2261 = None
        KL_LOC_Rules_2262 = None
        KL_LOC_ListAx38x38_2263 = None
        KL_LOC_Bx38x38_2264 = None
        KL_LOC_Sig_2265 = None
        KL_LOC_Declare_2266 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Throwcontrol_2240', tco_apply(shen_catchpoint, [])), tail_call(shen_cutpoint, [KL_CTX.KL_LOC_Throwcontrol_2240, [setattr(KL_CTX, 'KL_LOC_V2459_2241', tco_apply(shen_lazyderef, [KL_ARG_V2985_2235, KL_ARG_V2988_2238])), ([setattr(KL_CTX, 'KL_LOC_V2460_2242', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2459_2241[0], KL_ARG_V2988_2238])), ([setattr(KL_CTX, 'KL_LOC_V2461_2243', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2459_2241[1], KL_ARG_V2988_2238])), ([setattr(KL_CTX, 'KL_LOC_F_2244', KL_CTX.KL_LOC_V2461_2243[0]), [setattr(KL_CTX, 'KL_LOC_V2462_2245', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2461_2243[1], KL_ARG_V2988_2238])), ([setattr(KL_CTX, 'KL_LOC_V2463_2246', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2462_2245[0], KL_ARG_V2988_2238])), ([setattr(KL_CTX, 'KL_LOC_V2464_2247', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2462_2245[1], KL_ARG_V2988_2238])), ([setattr(KL_CTX, 'KL_LOC_V2465_2248', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2464_2247[0], KL_ARG_V2988_2238])), ([setattr(KL_CTX, 'KL_LOC_V2466_2249', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2465_2248[0], KL_ARG_V2988_2238])), ([setattr(KL_CTX, 'KL_LOC_V2467_2250', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2465_2248[1], KL_ARG_V2988_2238])), ([setattr(KL_CTX, 'KL_LOC_A_2251', KL_CTX.KL_LOC_V2467_2250[0]), [setattr(KL_CTX, 'KL_LOC_V2468_2252', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2467_2250[1], KL_ARG_V2988_2238])), ([setattr(KL_CTX, 'KL_LOC_V2469_2253', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2464_2247[1], KL_ARG_V2988_2238])), ([setattr(KL_CTX, 'KL_LOC_V2470_2254', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2469_2253[0], KL_ARG_V2988_2238])), ([setattr(KL_CTX, 'KL_LOC_V2471_2255', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2469_2253[1], KL_ARG_V2988_2238])), ([setattr(KL_CTX, 'KL_LOC_B_2256', KL_CTX.KL_LOC_V2471_2255[0]), [setattr(KL_CTX, 'KL_LOC_V2472_2257', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2471_2255[1], KL_ARG_V2988_2238])), ([setattr(KL_CTX, 'KL_LOC_V2473_2258', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2472_2257[0], KL_ARG_V2988_2238])), ([setattr(KL_CTX, 'KL_LOC_Rest_2259', KL_CTX.KL_LOC_V2472_2257[1]), [setattr(KL_CTX, 'KL_LOC_Restx38_2260', tco_apply(shen_newpv, [KL_ARG_V2988_2238])), [setattr(KL_CTX, 'KL_LOC_Restx38x38_2261', tco_apply(shen_newpv, [KL_ARG_V2988_2238])), [setattr(KL_CTX, 'KL_LOC_Rules_2262', tco_apply(shen_newpv, [KL_ARG_V2988_2238])), [setattr(KL_CTX, 'KL_LOC_ListAx38x38_2263', tco_apply(shen_newpv, [KL_ARG_V2988_2238])), [setattr(KL_CTX, 'KL_LOC_Bx38x38_2264', tco_apply(shen_newpv, [KL_ARG_V2988_2238])), [setattr(KL_CTX, 'KL_LOC_Sig_2265', tco_apply(shen_newpv, [KL_ARG_V2988_2238])), [setattr(KL_CTX, 'KL_LOC_Declare_2266', tco_apply(shen_newpv, [KL_ARG_V2988_2238])), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_CTX.KL_LOC_Sig_2265, tco_apply(shen_ue, [[[symdic.symdic_kl_list, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_2251, KL_ARG_V2988_2238]), []]], [symdic.symdic_kl_x61x61x62, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_2256, KL_ARG_V2988_2238]), []]]]]), KL_ARG_V2988_2238, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_ListAx38x38_2263, tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Sig_2265, KL_ARG_V2988_2238])[0], KL_ARG_V2988_2238, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Bx38x38_2264, tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Sig_2265, KL_ARG_V2988_2238])[1][1][0], KL_ARG_V2988_2238, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Restx38_2260, tco_apply(shen_plugx45wildcards, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Rest_2259, KL_ARG_V2988_2238])]), KL_ARG_V2988_2238, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Restx38x38_2261, tco_apply(shen_ue, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Restx38_2260, KL_ARG_V2988_2238])]), KL_ARG_V2988_2238, (lambda : tail_call(shen_getx45rules, [KL_CTX.KL_LOC_Rules_2262, KL_CTX.KL_LOC_Restx38x38_2261, KL_ARG_V2988_2238, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2240, KL_ARG_V2988_2238, (lambda : tail_call(shen_tcx45rules, [KL_CTX.KL_LOC_F_2244, KL_CTX.KL_LOC_Rules_2262, KL_CTX.KL_LOC_ListAx38x38_2263, KL_CTX.KL_LOC_Bx38x38_2264, [[KL_CTX.KL_LOC_F_2244, [symdic.symdic_kl_x58, [KL_CTX.KL_LOC_Sig_2265, []]]], KL_ARG_V2987_2237], 1, KL_ARG_V2988_2238, (lambda : tail_call(kl_unify, [KL_ARG_V2986_2236, [[symdic.symdic_kl_list, [KL_CTX.KL_LOC_A_2251, []]], [symdic.symdic_kl_x61x61x62, [KL_CTX.KL_LOC_B_2256, []]]], KL_ARG_V2988_2238, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Declare_2266, apply(kl_declare, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_F_2244, KL_ARG_V2988_2238]), [[symdic.symdic_kl_list, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_2251, KL_ARG_V2988_2238]), []]], [symdic.symdic_kl_x61x61x62, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_2256, KL_ARG_V2988_2238]), []]]]]), KL_ARG_V2988_2238, KL_ARG_V2989_2239]))]))]))]))]))]))]))]))]))])][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)] if (symdic.symdic_kl_x125 == KL_CTX.KL_LOC_V2473_2258) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2472_2257) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2471_2255) else False)][(-1)] if (symdic.symdic_kl_x61x61x62 == KL_CTX.KL_LOC_V2470_2254) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2469_2253) else False)][(-1)] if ([] == KL_CTX.KL_LOC_V2468_2252) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2467_2250) else False)][(-1)] if (symdic.symdic_kl_list == KL_CTX.KL_LOC_V2466_2249) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2465_2248) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2464_2247) else False)][(-1)] if (symdic.symdic_kl_x123 == KL_CTX.KL_LOC_V2463_2246) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2462_2245) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2461_2243) else False)][(-1)] if (symdic.symdic_kl_defcc == KL_CTX.KL_LOC_V2460_2242) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2459_2241) else False)][(-1)]])][(-1)]
shen_add_fun('shen.t*-defcc', shen_tx42x45defcc, 5)

@tail_recursion
def shen_plugx45wildcards(KL_ARG_V2990_2267):
    global symdic
    return (tail_call(kl_map, [symdic.symdic_shen_plugx45wildcards, KL_ARG_V2990_2267]) if shen_consp(KL_ARG_V2990_2267) else (tail_call(kl_gensym, [shen_intern('X')]) if (KL_ARG_V2990_2267 == symdic.symdic_kl__) else (KL_ARG_V2990_2267 if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.plug-wildcards', shen_plugx45wildcards, 1)

@tail_recursion
def shen_getx45rules(KL_ARG_V2991_2268, KL_ARG_V2992_2269, KL_ARG_V2993_2270, KL_ARG_V2994_2271):

    class KL_Context:
        KL_LOC_Throwcontrol_2272 = None
        KL_LOC_Case_2273 = None
        KL_LOC_V2452_2274 = None
        KL_LOC_V2453_2275 = None
        KL_LOC_Result_2276 = None
        KL_LOC_V2454_2277 = None
        KL_LOC_V2455_2278 = None
        KL_LOC_Rule_2279 = None
        KL_LOC_Rules_2280 = None
        KL_LOC_Other_2281 = None
        KL_LOC_Rule_2282 = None
        KL_LOC_Rules_2283 = None
        KL_LOC_Result_2284 = None
        KL_LOC_Other_2285 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Throwcontrol_2272', tco_apply(shen_catchpoint, [])), tail_call(shen_cutpoint, [KL_CTX.KL_LOC_Throwcontrol_2272, [setattr(KL_CTX, 'KL_LOC_Case_2273', [setattr(KL_CTX, 'KL_LOC_V2452_2274', tco_apply(shen_lazyderef, [KL_ARG_V2991_2268, KL_ARG_V2993_2270])), ([setattr(KL_CTX, 'KL_LOC_V2453_2275', tco_apply(shen_lazyderef, [KL_ARG_V2992_2269, KL_ARG_V2993_2270])), ([tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2272, KL_ARG_V2993_2270, KL_ARG_V2994_2271])][(-1)] if ([] == KL_CTX.KL_LOC_V2453_2275) else False)][(-1)] if ([] == KL_CTX.KL_LOC_V2452_2274) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2452_2274, [], KL_ARG_V2993_2270]), [setattr(KL_CTX, 'KL_LOC_Result_2276', [setattr(KL_CTX, 'KL_LOC_V2454_2277', tco_apply(shen_lazyderef, [KL_ARG_V2992_2269, KL_ARG_V2993_2270])), ([tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2272, KL_ARG_V2993_2270, KL_ARG_V2994_2271])][(-1)] if ([] == KL_CTX.KL_LOC_V2454_2277) else False)][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2452_2274, KL_ARG_V2993_2270]), KL_CTX.KL_LOC_Result_2276][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2452_2274]) else False))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_V2455_2278', tco_apply(shen_lazyderef, [KL_ARG_V2991_2268, KL_ARG_V2993_2270])), ([setattr(KL_CTX, 'KL_LOC_Rule_2279', KL_CTX.KL_LOC_V2455_2278[0]), [setattr(KL_CTX, 'KL_LOC_Rules_2280', KL_CTX.KL_LOC_V2455_2278[1]), [setattr(KL_CTX, 'KL_LOC_Other_2281', tco_apply(shen_newpv, [KL_ARG_V2993_2270])), [tco_apply(shen_incinfs, []), tco_apply(shen_firstx45rule, [KL_ARG_V2992_2269, KL_CTX.KL_LOC_Rule_2279, KL_CTX.KL_LOC_Other_2281, KL_ARG_V2993_2270, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2272, KL_ARG_V2993_2270, (lambda : tail_call(shen_getx45rules, [KL_CTX.KL_LOC_Rules_2280, KL_CTX.KL_LOC_Other_2281, KL_ARG_V2993_2270, KL_ARG_V2994_2271]))]))])][(-1)]][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2455_2278) else ([setattr(KL_CTX, 'KL_LOC_Rule_2282', tco_apply(shen_newpv, [KL_ARG_V2993_2270])), [setattr(KL_CTX, 'KL_LOC_Rules_2283', tco_apply(shen_newpv, [KL_ARG_V2993_2270])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2455_2278, [KL_CTX.KL_LOC_Rule_2282, KL_CTX.KL_LOC_Rules_2283], KL_ARG_V2993_2270]), [setattr(KL_CTX, 'KL_LOC_Result_2284', [setattr(KL_CTX, 'KL_LOC_Other_2285', tco_apply(shen_newpv, [KL_ARG_V2993_2270])), [tco_apply(shen_incinfs, []), tco_apply(shen_firstx45rule, [KL_ARG_V2992_2269, KL_CTX.KL_LOC_Rule_2282, KL_CTX.KL_LOC_Other_2285, KL_ARG_V2993_2270, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2272, KL_ARG_V2993_2270, (lambda : tail_call(shen_getx45rules, [KL_CTX.KL_LOC_Rules_2283, KL_CTX.KL_LOC_Other_2285, KL_ARG_V2993_2270, KL_ARG_V2994_2271]))]))])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2455_2278, KL_ARG_V2993_2270]), KL_CTX.KL_LOC_Result_2284][(-1)]][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2455_2278]) else False))][(-1)] if (KL_CTX.KL_LOC_Case_2273 == False) else KL_CTX.KL_LOC_Case_2273)][(-1)]])][(-1)]
shen_add_fun('shen.get-rules', shen_getx45rules, 4)

@tail_recursion
def shen_firstx45rule(KL_ARG_V2995_2286, KL_ARG_V2996_2287, KL_ARG_V2997_2288, KL_ARG_V2998_2289, KL_ARG_V2999_2290):

    class KL_Context:
        KL_LOC_Throwcontrol_2291 = None
        KL_LOC_Case_2292 = None
        KL_LOC_V2445_2293 = None
        KL_LOC_V2446_2294 = None
        KL_LOC_Other2440_2295 = None
        KL_LOC_V2447_2296 = None
        KL_LOC_Result_2297 = None
        KL_LOC_V2448_2298 = None
        KL_LOC_X2441_2299 = None
        KL_LOC_Rest_2300 = None
        KL_LOC_V2449_2301 = None
        KL_LOC_X_2302 = None
        KL_LOC_Rule_2303 = None
        KL_LOC_X_2304 = None
        KL_LOC_Rule_2305 = None
        KL_LOC_Result_2306 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Throwcontrol_2291', tco_apply(shen_catchpoint, [])), tail_call(shen_cutpoint, [KL_CTX.KL_LOC_Throwcontrol_2291, [setattr(KL_CTX, 'KL_LOC_Case_2292', [setattr(KL_CTX, 'KL_LOC_V2445_2293', tco_apply(shen_lazyderef, [KL_ARG_V2995_2286, KL_ARG_V2998_2289])), ([setattr(KL_CTX, 'KL_LOC_V2446_2294', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2445_2293[0], KL_ARG_V2998_2289])), ([setattr(KL_CTX, 'KL_LOC_Other2440_2295', KL_CTX.KL_LOC_V2445_2293[1]), [setattr(KL_CTX, 'KL_LOC_V2447_2296', tco_apply(shen_lazyderef, [KL_ARG_V2996_2287, KL_ARG_V2998_2289])), ([tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_ARG_V2997_2288, KL_CTX.KL_LOC_Other2440_2295, KL_ARG_V2998_2289, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2291, KL_ARG_V2998_2289, KL_ARG_V2999_2290]))])][(-1)] if ([] == KL_CTX.KL_LOC_V2447_2296) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2447_2296, [], KL_ARG_V2998_2289]), [setattr(KL_CTX, 'KL_LOC_Result_2297', [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_ARG_V2997_2288, KL_CTX.KL_LOC_Other2440_2295, KL_ARG_V2998_2289, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2291, KL_ARG_V2998_2289, KL_ARG_V2999_2290]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2447_2296, KL_ARG_V2998_2289]), KL_CTX.KL_LOC_Result_2297][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2447_2296]) else False))][(-1)]][(-1)] if (symdic.symdic_kl_x59 == KL_CTX.KL_LOC_V2446_2294) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2445_2293) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_V2448_2298', tco_apply(shen_lazyderef, [KL_ARG_V2995_2286, KL_ARG_V2998_2289])), ([setattr(KL_CTX, 'KL_LOC_X2441_2299', KL_CTX.KL_LOC_V2448_2298[0]), [setattr(KL_CTX, 'KL_LOC_Rest_2300', KL_CTX.KL_LOC_V2448_2298[1]), [setattr(KL_CTX, 'KL_LOC_V2449_2301', tco_apply(shen_lazyderef, [KL_ARG_V2996_2287, KL_ARG_V2998_2289])), ([setattr(KL_CTX, 'KL_LOC_X_2302', KL_CTX.KL_LOC_V2449_2301[0]), [setattr(KL_CTX, 'KL_LOC_Rule_2303', KL_CTX.KL_LOC_V2449_2301[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_X_2302, KL_CTX.KL_LOC_X2441_2299, KL_ARG_V2998_2289, (lambda : tail_call(shen_firstx45rule, [KL_CTX.KL_LOC_Rest_2300, KL_CTX.KL_LOC_Rule_2303, KL_ARG_V2997_2288, KL_ARG_V2998_2289, KL_ARG_V2999_2290]))])][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2449_2301) else ([setattr(KL_CTX, 'KL_LOC_X_2304', tco_apply(shen_newpv, [KL_ARG_V2998_2289])), [setattr(KL_CTX, 'KL_LOC_Rule_2305', tco_apply(shen_newpv, [KL_ARG_V2998_2289])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2449_2301, [KL_CTX.KL_LOC_X_2304, KL_CTX.KL_LOC_Rule_2305], KL_ARG_V2998_2289]), [setattr(KL_CTX, 'KL_LOC_Result_2306', [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_X_2304, KL_CTX.KL_LOC_X2441_2299, KL_ARG_V2998_2289, (lambda : tail_call(shen_firstx45rule, [KL_CTX.KL_LOC_Rest_2300, KL_CTX.KL_LOC_Rule_2305, KL_ARG_V2997_2288, KL_ARG_V2998_2289, KL_ARG_V2999_2290]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2449_2301, KL_ARG_V2998_2289]), KL_CTX.KL_LOC_Result_2306][(-1)]][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2449_2301]) else False))][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2448_2298) else False)][(-1)] if (KL_CTX.KL_LOC_Case_2292 == False) else KL_CTX.KL_LOC_Case_2292)][(-1)]])][(-1)]
shen_add_fun('shen.first-rule', shen_firstx45rule, 5)

@tail_recursion
def shen_tcx45rules(KL_ARG_V3000_2307, KL_ARG_V3001_2308, KL_ARG_V3002_2309, KL_ARG_V3003_2310, KL_ARG_V3004_2311, KL_ARG_V3005_2312, KL_ARG_V3006_2313, KL_ARG_V3007_2314):

    class KL_Context:
        KL_LOC_Throwcontrol_2315 = None
        KL_LOC_Case_2316 = None
        KL_LOC_V2434_2317 = None
        KL_LOC_V2435_2318 = None
        KL_LOC_Rule_2319 = None
        KL_LOC_Rules_2320 = None
        KL_LOC_V2436_2321 = None
        KL_LOC_V2437_2322 = None
        KL_LOC_V2438_2323 = None
        KL_LOC_A_2324 = None
        KL_LOC_V2439_2325 = None
        KL_LOC_M_2326 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Throwcontrol_2315', tco_apply(shen_catchpoint, [])), tail_call(shen_cutpoint, [KL_CTX.KL_LOC_Throwcontrol_2315, [setattr(KL_CTX, 'KL_LOC_Case_2316', [setattr(KL_CTX, 'KL_LOC_V2434_2317', tco_apply(shen_lazyderef, [KL_ARG_V3001_2308, KL_ARG_V3006_2313])), ([tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V3007_2314])][(-1)] if ([] == KL_CTX.KL_LOC_V2434_2317) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_V2435_2318', tco_apply(shen_lazyderef, [KL_ARG_V3001_2308, KL_ARG_V3006_2313])), ([setattr(KL_CTX, 'KL_LOC_Rule_2319', KL_CTX.KL_LOC_V2435_2318[0]), [setattr(KL_CTX, 'KL_LOC_Rules_2320', KL_CTX.KL_LOC_V2435_2318[1]), [setattr(KL_CTX, 'KL_LOC_V2436_2321', tco_apply(shen_lazyderef, [KL_ARG_V3002_2309, KL_ARG_V3006_2313])), ([setattr(KL_CTX, 'KL_LOC_V2437_2322', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2436_2321[0], KL_ARG_V3006_2313])), ([setattr(KL_CTX, 'KL_LOC_V2438_2323', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2436_2321[1], KL_ARG_V3006_2313])), ([setattr(KL_CTX, 'KL_LOC_A_2324', KL_CTX.KL_LOC_V2438_2323[0]), [setattr(KL_CTX, 'KL_LOC_V2439_2325', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2438_2323[1], KL_ARG_V3006_2313])), ([setattr(KL_CTX, 'KL_LOC_M_2326', tco_apply(shen_newpv, [KL_ARG_V3006_2313])), [tco_apply(shen_incinfs, []), tco_apply(shen_tcx45rule, [KL_ARG_V3000_2307, KL_CTX.KL_LOC_Rule_2319, KL_CTX.KL_LOC_A_2324, KL_ARG_V3003_2310, KL_ARG_V3004_2311, KL_ARG_V3005_2312, KL_ARG_V3006_2313, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_M_2326, (tco_apply(shen_deref, [KL_ARG_V3005_2312, KL_ARG_V3006_2313]) + 1), KL_ARG_V3006_2313, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2315, KL_ARG_V3006_2313, (lambda : tail_call(shen_tcx45rules, [KL_ARG_V3000_2307, KL_CTX.KL_LOC_Rules_2320, [symdic.symdic_kl_list, [KL_CTX.KL_LOC_A_2324, []]], KL_ARG_V3003_2310, KL_ARG_V3004_2311, KL_CTX.KL_LOC_M_2326, KL_ARG_V3006_2313, KL_ARG_V3007_2314]))]))]))])][(-1)]][(-1)] if ([] == KL_CTX.KL_LOC_V2439_2325) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2438_2323) else False)][(-1)] if (symdic.symdic_kl_list == KL_CTX.KL_LOC_V2437_2322) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2436_2321) else False)][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2435_2318) else False)][(-1)] if (KL_CTX.KL_LOC_Case_2316 == False) else KL_CTX.KL_LOC_Case_2316)][(-1)]])][(-1)]
shen_add_fun('shen.tc-rules', shen_tcx45rules, 8)

@tail_recursion
def shen_tcx45rule(KL_ARG_V3008_2327, KL_ARG_V3009_2328, KL_ARG_V3010_2329, KL_ARG_V3011_2330, KL_ARG_V3012_2331, KL_ARG_V3013_2332, KL_ARG_V3014_2333, KL_ARG_V3015_2334):

    class KL_Context:
        KL_LOC_Case_2335 = None
        KL_LOC_Err_2336 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Case_2335', [tco_apply(shen_incinfs, []), tco_apply(shen_checkx45defccx45rule, [KL_ARG_V3009_2328, KL_ARG_V3010_2329, KL_ARG_V3011_2330, KL_ARG_V3012_2331, KL_ARG_V3014_2333, KL_ARG_V3015_2334])][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Err_2336', tco_apply(shen_newpv, [KL_ARG_V3014_2333])), [tco_apply(shen_incinfs, []), tail_call(kl_bind, [KL_CTX.KL_LOC_Err_2336, shen_simple_error(('type error in rule ' + tco_apply(shen_app, [tco_apply(shen_lazyderef, [KL_ARG_V3013_2332, KL_ARG_V3014_2333]), (' of ' + tco_apply(shen_app, [tco_apply(shen_lazyderef, [KL_ARG_V3008_2327, KL_ARG_V3014_2333]), '', symdic.symdic_shen_a])), symdic.symdic_shen_a]))), KL_ARG_V3014_2333, KL_ARG_V3015_2334])][(-1)]][(-1)] if (KL_CTX.KL_LOC_Case_2335 == False) else KL_CTX.KL_LOC_Case_2335)][(-1)]
shen_add_fun('shen.tc-rule', shen_tcx45rule, 8)

@tail_recursion
def shen_checkx45defccx45rule(KL_ARG_V3016_2337, KL_ARG_V3017_2338, KL_ARG_V3018_2339, KL_ARG_V3019_2340, KL_ARG_V3020_2341, KL_ARG_V3021_2342):

    class KL_Context:
        KL_LOC_Throwcontrol_2343 = None
        KL_LOC_Syntax_2344 = None
        KL_LOC_Semantics_2345 = None
        KL_LOC_SynHyps_2346 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Throwcontrol_2343', tco_apply(shen_catchpoint, [])), tail_call(shen_cutpoint, [KL_CTX.KL_LOC_Throwcontrol_2343, [setattr(KL_CTX, 'KL_LOC_Syntax_2344', tco_apply(shen_newpv, [KL_ARG_V3020_2341])), [setattr(KL_CTX, 'KL_LOC_Semantics_2345', tco_apply(shen_newpv, [KL_ARG_V3020_2341])), [setattr(KL_CTX, 'KL_LOC_SynHyps_2346', tco_apply(shen_newpv, [KL_ARG_V3020_2341])), [tco_apply(shen_incinfs, []), tco_apply(shen_getx45syntaxx43semantics, [KL_CTX.KL_LOC_Syntax_2344, KL_CTX.KL_LOC_Semantics_2345, KL_ARG_V3016_2337, KL_ARG_V3020_2341, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2343, KL_ARG_V3020_2341, (lambda : tail_call(shen_syntaxx45hyps, [KL_CTX.KL_LOC_Syntax_2344, KL_ARG_V3019_2340, KL_CTX.KL_LOC_SynHyps_2346, KL_ARG_V3017_2338, KL_ARG_V3020_2341, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2343, KL_ARG_V3020_2341, (lambda : tail_call(shen_syntaxx45check, [KL_CTX.KL_LOC_Syntax_2344, KL_ARG_V3017_2338, KL_CTX.KL_LOC_SynHyps_2346, KL_ARG_V3020_2341, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2343, KL_ARG_V3020_2341, (lambda : tail_call(shen_semanticsx45check, [KL_CTX.KL_LOC_Semantics_2345, KL_ARG_V3018_2339, KL_CTX.KL_LOC_SynHyps_2346, KL_ARG_V3020_2341, KL_ARG_V3021_2342]))]))]))]))]))]))])][(-1)]][(-1)]][(-1)]][(-1)]])][(-1)]
shen_add_fun('shen.check-defcc-rule', shen_checkx45defccx45rule, 6)

@tail_recursion
def shen_syntaxx45hyps(KL_ARG_V3022_2347, KL_ARG_V3023_2348, KL_ARG_V3024_2349, KL_ARG_V3025_2350, KL_ARG_V3026_2351, KL_ARG_V3027_2352):

    class KL_Context:
        KL_LOC_Throwcontrol_2353 = None
        KL_LOC_Case_2354 = None
        KL_LOC_V2407_2355 = None
        KL_LOC_Case_2356 = None
        KL_LOC_V2408_2357 = None
        KL_LOC_X2401_2358 = None
        KL_LOC_Y_2359 = None
        KL_LOC_V2409_2360 = None
        KL_LOC_V2410_2361 = None
        KL_LOC_X_2362 = None
        KL_LOC_V2411_2363 = None
        KL_LOC_V2412_2364 = None
        KL_LOC_V2413_2365 = None
        KL_LOC_A2402_2366 = None
        KL_LOC_V2414_2367 = None
        KL_LOC_SynHyps_2368 = None
        KL_LOC_Result_2369 = None
        KL_LOC_SynHyps_2370 = None
        KL_LOC_A2402_2371 = None
        KL_LOC_Result_2372 = None
        KL_LOC_SynHyps_2373 = None
        KL_LOC_Result_2374 = None
        KL_LOC_V2415_2375 = None
        KL_LOC_A2402_2376 = None
        KL_LOC_V2416_2377 = None
        KL_LOC_SynHyps_2378 = None
        KL_LOC_Result_2379 = None
        KL_LOC_SynHyps_2380 = None
        KL_LOC_A2402_2381 = None
        KL_LOC_Result_2382 = None
        KL_LOC_SynHyps_2383 = None
        KL_LOC_A2402_2384 = None
        KL_LOC_Result_2385 = None
        KL_LOC_SynHyps_2386 = None
        KL_LOC_X_2387 = None
        KL_LOC_A2402_2388 = None
        KL_LOC_Result_2389 = None
        KL_LOC_SynHyps_2390 = None
        KL_LOC_X_2391 = None
        KL_LOC_A2402_2392 = None
        KL_LOC_SynHyps_2393 = None
        KL_LOC_Result_2394 = None
        KL_LOC_V2417_2395 = None
        KL_LOC_Y_2396 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Throwcontrol_2353', tco_apply(shen_catchpoint, [])), tail_call(shen_cutpoint, [KL_CTX.KL_LOC_Throwcontrol_2353, [setattr(KL_CTX, 'KL_LOC_Case_2354', [setattr(KL_CTX, 'KL_LOC_V2407_2355', tco_apply(shen_lazyderef, [KL_ARG_V3022_2347, KL_ARG_V3026_2351])), ([tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_ARG_V3024_2349, KL_ARG_V3023_2348, KL_ARG_V3026_2351, KL_ARG_V3027_2352])][(-1)] if ([] == KL_CTX.KL_LOC_V2407_2355) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_2356', [setattr(KL_CTX, 'KL_LOC_V2408_2357', tco_apply(shen_lazyderef, [KL_ARG_V3022_2347, KL_ARG_V3026_2351])), ([setattr(KL_CTX, 'KL_LOC_X2401_2358', KL_CTX.KL_LOC_V2408_2357[0]), [setattr(KL_CTX, 'KL_LOC_Y_2359', KL_CTX.KL_LOC_V2408_2357[1]), [setattr(KL_CTX, 'KL_LOC_V2409_2360', tco_apply(shen_lazyderef, [KL_ARG_V3024_2349, KL_ARG_V3026_2351])), ([setattr(KL_CTX, 'KL_LOC_V2410_2361', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2409_2360[0], KL_ARG_V3026_2351])), ([setattr(KL_CTX, 'KL_LOC_X_2362', KL_CTX.KL_LOC_V2410_2361[0]), [setattr(KL_CTX, 'KL_LOC_V2411_2363', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2410_2361[1], KL_ARG_V3026_2351])), ([setattr(KL_CTX, 'KL_LOC_V2412_2364', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2411_2363[0], KL_ARG_V3026_2351])), ([setattr(KL_CTX, 'KL_LOC_V2413_2365', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2411_2363[1], KL_ARG_V3026_2351])), ([setattr(KL_CTX, 'KL_LOC_A2402_2366', KL_CTX.KL_LOC_V2413_2365[0]), [setattr(KL_CTX, 'KL_LOC_V2414_2367', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2413_2365[1], KL_ARG_V3026_2351])), ([setattr(KL_CTX, 'KL_LOC_SynHyps_2368', KL_CTX.KL_LOC_V2409_2360[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_ARG_V3025_2350, KL_CTX.KL_LOC_A2402_2366, KL_ARG_V3026_2351, (lambda : tail_call(kl_unifyx33, [KL_CTX.KL_LOC_X_2362, KL_CTX.KL_LOC_X2401_2358, KL_ARG_V3026_2351, (lambda : tail_call(kl_fwhen, [tco_apply(shen_uex63, [tco_apply(shen_deref, [KL_CTX.KL_LOC_X_2362, KL_ARG_V3026_2351])]), KL_ARG_V3026_2351, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2353, KL_ARG_V3026_2351, (lambda : tail_call(shen_syntaxx45hyps, [KL_CTX.KL_LOC_Y_2359, KL_ARG_V3023_2348, KL_CTX.KL_LOC_SynHyps_2368, KL_ARG_V3025_2350, KL_ARG_V3026_2351, KL_ARG_V3027_2352]))]))]))]))])][(-1)]][(-1)] if ([] == KL_CTX.KL_LOC_V2414_2367) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2414_2367, [], KL_ARG_V3026_2351]), [setattr(KL_CTX, 'KL_LOC_Result_2369', [setattr(KL_CTX, 'KL_LOC_SynHyps_2370', KL_CTX.KL_LOC_V2409_2360[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_ARG_V3025_2350, KL_CTX.KL_LOC_A2402_2366, KL_ARG_V3026_2351, (lambda : tail_call(kl_unifyx33, [KL_CTX.KL_LOC_X_2362, KL_CTX.KL_LOC_X2401_2358, KL_ARG_V3026_2351, (lambda : tail_call(kl_fwhen, [tco_apply(shen_uex63, [tco_apply(shen_deref, [KL_CTX.KL_LOC_X_2362, KL_ARG_V3026_2351])]), KL_ARG_V3026_2351, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2353, KL_ARG_V3026_2351, (lambda : tail_call(shen_syntaxx45hyps, [KL_CTX.KL_LOC_Y_2359, KL_ARG_V3023_2348, KL_CTX.KL_LOC_SynHyps_2370, KL_ARG_V3025_2350, KL_ARG_V3026_2351, KL_ARG_V3027_2352]))]))]))]))])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2414_2367, KL_ARG_V3026_2351]), KL_CTX.KL_LOC_Result_2369][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2414_2367]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2413_2365) else ([setattr(KL_CTX, 'KL_LOC_A2402_2371', tco_apply(shen_newpv, [KL_ARG_V3026_2351])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2413_2365, [KL_CTX.KL_LOC_A2402_2371, []], KL_ARG_V3026_2351]), [setattr(KL_CTX, 'KL_LOC_Result_2372', [setattr(KL_CTX, 'KL_LOC_SynHyps_2373', KL_CTX.KL_LOC_V2409_2360[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_ARG_V3025_2350, KL_CTX.KL_LOC_A2402_2371, KL_ARG_V3026_2351, (lambda : tail_call(kl_unifyx33, [KL_CTX.KL_LOC_X_2362, KL_CTX.KL_LOC_X2401_2358, KL_ARG_V3026_2351, (lambda : tail_call(kl_fwhen, [tco_apply(shen_uex63, [tco_apply(shen_deref, [KL_CTX.KL_LOC_X_2362, KL_ARG_V3026_2351])]), KL_ARG_V3026_2351, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2353, KL_ARG_V3026_2351, (lambda : tail_call(shen_syntaxx45hyps, [KL_CTX.KL_LOC_Y_2359, KL_ARG_V3023_2348, KL_CTX.KL_LOC_SynHyps_2373, KL_ARG_V3025_2350, KL_ARG_V3026_2351, KL_ARG_V3027_2352]))]))]))]))])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2413_2365, KL_ARG_V3026_2351]), KL_CTX.KL_LOC_Result_2372][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2413_2365]) else False))][(-1)] if (symdic.symdic_kl_x58 == KL_CTX.KL_LOC_V2412_2364) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2412_2364, symdic.symdic_kl_x58, KL_ARG_V3026_2351]), [setattr(KL_CTX, 'KL_LOC_Result_2374', [setattr(KL_CTX, 'KL_LOC_V2415_2375', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2411_2363[1], KL_ARG_V3026_2351])), ([setattr(KL_CTX, 'KL_LOC_A2402_2376', KL_CTX.KL_LOC_V2415_2375[0]), [setattr(KL_CTX, 'KL_LOC_V2416_2377', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2415_2375[1], KL_ARG_V3026_2351])), ([setattr(KL_CTX, 'KL_LOC_SynHyps_2378', KL_CTX.KL_LOC_V2409_2360[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_ARG_V3025_2350, KL_CTX.KL_LOC_A2402_2376, KL_ARG_V3026_2351, (lambda : tail_call(kl_unifyx33, [KL_CTX.KL_LOC_X_2362, KL_CTX.KL_LOC_X2401_2358, KL_ARG_V3026_2351, (lambda : tail_call(kl_fwhen, [tco_apply(shen_uex63, [tco_apply(shen_deref, [KL_CTX.KL_LOC_X_2362, KL_ARG_V3026_2351])]), KL_ARG_V3026_2351, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2353, KL_ARG_V3026_2351, (lambda : tail_call(shen_syntaxx45hyps, [KL_CTX.KL_LOC_Y_2359, KL_ARG_V3023_2348, KL_CTX.KL_LOC_SynHyps_2378, KL_ARG_V3025_2350, KL_ARG_V3026_2351, KL_ARG_V3027_2352]))]))]))]))])][(-1)]][(-1)] if ([] == KL_CTX.KL_LOC_V2416_2377) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2416_2377, [], KL_ARG_V3026_2351]), [setattr(KL_CTX, 'KL_LOC_Result_2379', [setattr(KL_CTX, 'KL_LOC_SynHyps_2380', KL_CTX.KL_LOC_V2409_2360[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_ARG_V3025_2350, KL_CTX.KL_LOC_A2402_2376, KL_ARG_V3026_2351, (lambda : tail_call(kl_unifyx33, [KL_CTX.KL_LOC_X_2362, KL_CTX.KL_LOC_X2401_2358, KL_ARG_V3026_2351, (lambda : tail_call(kl_fwhen, [tco_apply(shen_uex63, [tco_apply(shen_deref, [KL_CTX.KL_LOC_X_2362, KL_ARG_V3026_2351])]), KL_ARG_V3026_2351, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2353, KL_ARG_V3026_2351, (lambda : tail_call(shen_syntaxx45hyps, [KL_CTX.KL_LOC_Y_2359, KL_ARG_V3023_2348, KL_CTX.KL_LOC_SynHyps_2380, KL_ARG_V3025_2350, KL_ARG_V3026_2351, KL_ARG_V3027_2352]))]))]))]))])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2416_2377, KL_ARG_V3026_2351]), KL_CTX.KL_LOC_Result_2379][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2416_2377]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2415_2375) else ([setattr(KL_CTX, 'KL_LOC_A2402_2381', tco_apply(shen_newpv, [KL_ARG_V3026_2351])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2415_2375, [KL_CTX.KL_LOC_A2402_2381, []], KL_ARG_V3026_2351]), [setattr(KL_CTX, 'KL_LOC_Result_2382', [setattr(KL_CTX, 'KL_LOC_SynHyps_2383', KL_CTX.KL_LOC_V2409_2360[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_ARG_V3025_2350, KL_CTX.KL_LOC_A2402_2381, KL_ARG_V3026_2351, (lambda : tail_call(kl_unifyx33, [KL_CTX.KL_LOC_X_2362, KL_CTX.KL_LOC_X2401_2358, KL_ARG_V3026_2351, (lambda : tail_call(kl_fwhen, [tco_apply(shen_uex63, [tco_apply(shen_deref, [KL_CTX.KL_LOC_X_2362, KL_ARG_V3026_2351])]), KL_ARG_V3026_2351, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2353, KL_ARG_V3026_2351, (lambda : tail_call(shen_syntaxx45hyps, [KL_CTX.KL_LOC_Y_2359, KL_ARG_V3023_2348, KL_CTX.KL_LOC_SynHyps_2383, KL_ARG_V3025_2350, KL_ARG_V3026_2351, KL_ARG_V3027_2352]))]))]))]))])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2415_2375, KL_ARG_V3026_2351]), KL_CTX.KL_LOC_Result_2382][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2415_2375]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2412_2364, KL_ARG_V3026_2351]), KL_CTX.KL_LOC_Result_2374][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2412_2364]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2411_2363) else ([setattr(KL_CTX, 'KL_LOC_A2402_2384', tco_apply(shen_newpv, [KL_ARG_V3026_2351])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2411_2363, [symdic.symdic_kl_x58, [KL_CTX.KL_LOC_A2402_2384, []]], KL_ARG_V3026_2351]), [setattr(KL_CTX, 'KL_LOC_Result_2385', [setattr(KL_CTX, 'KL_LOC_SynHyps_2386', KL_CTX.KL_LOC_V2409_2360[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_ARG_V3025_2350, KL_CTX.KL_LOC_A2402_2384, KL_ARG_V3026_2351, (lambda : tail_call(kl_unifyx33, [KL_CTX.KL_LOC_X_2362, KL_CTX.KL_LOC_X2401_2358, KL_ARG_V3026_2351, (lambda : tail_call(kl_fwhen, [tco_apply(shen_uex63, [tco_apply(shen_deref, [KL_CTX.KL_LOC_X_2362, KL_ARG_V3026_2351])]), KL_ARG_V3026_2351, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2353, KL_ARG_V3026_2351, (lambda : tail_call(shen_syntaxx45hyps, [KL_CTX.KL_LOC_Y_2359, KL_ARG_V3023_2348, KL_CTX.KL_LOC_SynHyps_2386, KL_ARG_V3025_2350, KL_ARG_V3026_2351, KL_ARG_V3027_2352]))]))]))]))])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2411_2363, KL_ARG_V3026_2351]), KL_CTX.KL_LOC_Result_2385][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2411_2363]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2410_2361) else ([setattr(KL_CTX, 'KL_LOC_X_2387', tco_apply(shen_newpv, [KL_ARG_V3026_2351])), [setattr(KL_CTX, 'KL_LOC_A2402_2388', tco_apply(shen_newpv, [KL_ARG_V3026_2351])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2410_2361, [KL_CTX.KL_LOC_X_2387, [symdic.symdic_kl_x58, [KL_CTX.KL_LOC_A2402_2388, []]]], KL_ARG_V3026_2351]), [setattr(KL_CTX, 'KL_LOC_Result_2389', [setattr(KL_CTX, 'KL_LOC_SynHyps_2390', KL_CTX.KL_LOC_V2409_2360[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_ARG_V3025_2350, KL_CTX.KL_LOC_A2402_2388, KL_ARG_V3026_2351, (lambda : tail_call(kl_unifyx33, [KL_CTX.KL_LOC_X_2387, KL_CTX.KL_LOC_X2401_2358, KL_ARG_V3026_2351, (lambda : tail_call(kl_fwhen, [tco_apply(shen_uex63, [tco_apply(shen_deref, [KL_CTX.KL_LOC_X_2387, KL_ARG_V3026_2351])]), KL_ARG_V3026_2351, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2353, KL_ARG_V3026_2351, (lambda : tail_call(shen_syntaxx45hyps, [KL_CTX.KL_LOC_Y_2359, KL_ARG_V3023_2348, KL_CTX.KL_LOC_SynHyps_2390, KL_ARG_V3025_2350, KL_ARG_V3026_2351, KL_ARG_V3027_2352]))]))]))]))])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2410_2361, KL_ARG_V3026_2351]), KL_CTX.KL_LOC_Result_2389][(-1)]][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2410_2361]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2409_2360) else ([setattr(KL_CTX, 'KL_LOC_X_2391', tco_apply(shen_newpv, [KL_ARG_V3026_2351])), [setattr(KL_CTX, 'KL_LOC_A2402_2392', tco_apply(shen_newpv, [KL_ARG_V3026_2351])), [setattr(KL_CTX, 'KL_LOC_SynHyps_2393', tco_apply(shen_newpv, [KL_ARG_V3026_2351])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2409_2360, [[KL_CTX.KL_LOC_X_2391, [symdic.symdic_kl_x58, [KL_CTX.KL_LOC_A2402_2392, []]]], KL_CTX.KL_LOC_SynHyps_2393], KL_ARG_V3026_2351]), [setattr(KL_CTX, 'KL_LOC_Result_2394', [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_ARG_V3025_2350, KL_CTX.KL_LOC_A2402_2392, KL_ARG_V3026_2351, (lambda : tail_call(kl_unifyx33, [KL_CTX.KL_LOC_X_2391, KL_CTX.KL_LOC_X2401_2358, KL_ARG_V3026_2351, (lambda : tail_call(kl_fwhen, [tco_apply(shen_uex63, [tco_apply(shen_deref, [KL_CTX.KL_LOC_X_2391, KL_ARG_V3026_2351])]), KL_ARG_V3026_2351, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2353, KL_ARG_V3026_2351, (lambda : tail_call(shen_syntaxx45hyps, [KL_CTX.KL_LOC_Y_2359, KL_ARG_V3023_2348, KL_CTX.KL_LOC_SynHyps_2393, KL_ARG_V3025_2350, KL_ARG_V3026_2351, KL_ARG_V3027_2352]))]))]))]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2409_2360, KL_ARG_V3026_2351]), KL_CTX.KL_LOC_Result_2394][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2409_2360]) else False))][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2408_2357) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_V2417_2395', tco_apply(shen_lazyderef, [KL_ARG_V3022_2347, KL_ARG_V3026_2351])), ([setattr(KL_CTX, 'KL_LOC_Y_2396', KL_CTX.KL_LOC_V2417_2395[1]), [tco_apply(shen_incinfs, []), tco_apply(shen_syntaxx45hyps, [KL_CTX.KL_LOC_Y_2396, KL_ARG_V3023_2348, KL_ARG_V3024_2349, KL_ARG_V3025_2350, KL_ARG_V3026_2351, KL_ARG_V3027_2352])][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2417_2395) else False)][(-1)] if (KL_CTX.KL_LOC_Case_2356 == False) else KL_CTX.KL_LOC_Case_2356)][(-1)] if (KL_CTX.KL_LOC_Case_2354 == False) else KL_CTX.KL_LOC_Case_2354)][(-1)]])][(-1)]
shen_add_fun('shen.syntax-hyps', shen_syntaxx45hyps, 6)

@tail_recursion
def shen_getx45syntaxx43semantics(KL_ARG_V3028_2397, KL_ARG_V3029_2398, KL_ARG_V3030_2399, KL_ARG_V3031_2400, KL_ARG_V3032_2401):

    class KL_Context:
        KL_LOC_Throwcontrol_2402 = None
        KL_LOC_Case_2403 = None
        KL_LOC_V2373_2404 = None
        KL_LOC_V2374_2405 = None
        KL_LOC_V2375_2406 = None
        KL_LOC_V2376_2407 = None
        KL_LOC_Semantics_2408 = None
        KL_LOC_V2377_2409 = None
        KL_LOC_Result_2410 = None
        KL_LOC_V2378_2411 = None
        KL_LOC_V2379_2412 = None
        KL_LOC_V2380_2413 = None
        KL_LOC_Semantics_2414 = None
        KL_LOC_V2381_2415 = None
        KL_LOC_Case_2416 = None
        KL_LOC_V2382_2417 = None
        KL_LOC_V2383_2418 = None
        KL_LOC_V2384_2419 = None
        KL_LOC_V2385_2420 = None
        KL_LOC_Semantics_2421 = None
        KL_LOC_V2386_2422 = None
        KL_LOC_V2387_2423 = None
        KL_LOC_V2388_2424 = None
        KL_LOC_G_2425 = None
        KL_LOC_V2389_2426 = None
        KL_LOC_Result_2427 = None
        KL_LOC_V2390_2428 = None
        KL_LOC_V2391_2429 = None
        KL_LOC_V2392_2430 = None
        KL_LOC_Semantics_2431 = None
        KL_LOC_V2393_2432 = None
        KL_LOC_V2394_2433 = None
        KL_LOC_V2395_2434 = None
        KL_LOC_G_2435 = None
        KL_LOC_V2396_2436 = None
        KL_LOC_V2397_2437 = None
        KL_LOC_X2369_2438 = None
        KL_LOC_Syntax_2439 = None
        KL_LOC_V2398_2440 = None
        KL_LOC_X_2441 = None
        KL_LOC_Rule_2442 = None
        KL_LOC_X2369_2443 = None
        KL_LOC_Syntax_2444 = None
        KL_LOC_Result_2445 = None
        KL_LOC_V2399_2446 = None
        KL_LOC_X_2447 = None
        KL_LOC_Rule_2448 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Throwcontrol_2402', tco_apply(shen_catchpoint, [])), tail_call(shen_cutpoint, [KL_CTX.KL_LOC_Throwcontrol_2402, [setattr(KL_CTX, 'KL_LOC_Case_2403', [setattr(KL_CTX, 'KL_LOC_V2373_2404', tco_apply(shen_lazyderef, [KL_ARG_V3028_2397, KL_ARG_V3031_2400])), ([setattr(KL_CTX, 'KL_LOC_V2374_2405', tco_apply(shen_lazyderef, [KL_ARG_V3030_2399, KL_ARG_V3031_2400])), ([setattr(KL_CTX, 'KL_LOC_V2375_2406', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2374_2405[0], KL_ARG_V3031_2400])), ([setattr(KL_CTX, 'KL_LOC_V2376_2407', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2374_2405[1], KL_ARG_V3031_2400])), ([setattr(KL_CTX, 'KL_LOC_Semantics_2408', KL_CTX.KL_LOC_V2376_2407[0]), [setattr(KL_CTX, 'KL_LOC_V2377_2409', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2376_2407[1], KL_ARG_V3031_2400])), ([tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2402, KL_ARG_V3031_2400, (lambda : tail_call(kl_bind, [KL_ARG_V3029_2398, tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Semantics_2408, KL_ARG_V3031_2400]), KL_ARG_V3031_2400, KL_ARG_V3032_2401]))])][(-1)] if ([] == KL_CTX.KL_LOC_V2377_2409) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2376_2407) else False)][(-1)] if (symdic.symdic_kl_x58x61 == KL_CTX.KL_LOC_V2375_2406) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2374_2405) else False)][(-1)] if ([] == KL_CTX.KL_LOC_V2373_2404) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2373_2404, [], KL_ARG_V3031_2400]), [setattr(KL_CTX, 'KL_LOC_Result_2410', [setattr(KL_CTX, 'KL_LOC_V2378_2411', tco_apply(shen_lazyderef, [KL_ARG_V3030_2399, KL_ARG_V3031_2400])), ([setattr(KL_CTX, 'KL_LOC_V2379_2412', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2378_2411[0], KL_ARG_V3031_2400])), ([setattr(KL_CTX, 'KL_LOC_V2380_2413', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2378_2411[1], KL_ARG_V3031_2400])), ([setattr(KL_CTX, 'KL_LOC_Semantics_2414', KL_CTX.KL_LOC_V2380_2413[0]), [setattr(KL_CTX, 'KL_LOC_V2381_2415', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2380_2413[1], KL_ARG_V3031_2400])), ([tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2402, KL_ARG_V3031_2400, (lambda : tail_call(kl_bind, [KL_ARG_V3029_2398, tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Semantics_2414, KL_ARG_V3031_2400]), KL_ARG_V3031_2400, KL_ARG_V3032_2401]))])][(-1)] if ([] == KL_CTX.KL_LOC_V2381_2415) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2380_2413) else False)][(-1)] if (symdic.symdic_kl_x58x61 == KL_CTX.KL_LOC_V2379_2412) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2378_2411) else False)][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2373_2404, KL_ARG_V3031_2400]), KL_CTX.KL_LOC_Result_2410][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2373_2404]) else False))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_2416', [setattr(KL_CTX, 'KL_LOC_V2382_2417', tco_apply(shen_lazyderef, [KL_ARG_V3028_2397, KL_ARG_V3031_2400])), ([setattr(KL_CTX, 'KL_LOC_V2383_2418', tco_apply(shen_lazyderef, [KL_ARG_V3030_2399, KL_ARG_V3031_2400])), ([setattr(KL_CTX, 'KL_LOC_V2384_2419', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2383_2418[0], KL_ARG_V3031_2400])), ([setattr(KL_CTX, 'KL_LOC_V2385_2420', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2383_2418[1], KL_ARG_V3031_2400])), ([setattr(KL_CTX, 'KL_LOC_Semantics_2421', KL_CTX.KL_LOC_V2385_2420[0]), [setattr(KL_CTX, 'KL_LOC_V2386_2422', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2385_2420[1], KL_ARG_V3031_2400])), ([setattr(KL_CTX, 'KL_LOC_V2387_2423', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2386_2422[0], KL_ARG_V3031_2400])), ([setattr(KL_CTX, 'KL_LOC_V2388_2424', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2386_2422[1], KL_ARG_V3031_2400])), ([setattr(KL_CTX, 'KL_LOC_G_2425', KL_CTX.KL_LOC_V2388_2424[0]), [setattr(KL_CTX, 'KL_LOC_V2389_2426', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2388_2424[1], KL_ARG_V3031_2400])), ([tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2402, KL_ARG_V3031_2400, (lambda : tail_call(kl_bind, [KL_ARG_V3029_2398, [symdic.symdic_kl_where, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_G_2425, KL_ARG_V3031_2400]), [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Semantics_2421, KL_ARG_V3031_2400]), []]]], KL_ARG_V3031_2400, KL_ARG_V3032_2401]))])][(-1)] if ([] == KL_CTX.KL_LOC_V2389_2426) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2388_2424) else False)][(-1)] if (symdic.symdic_kl_where == KL_CTX.KL_LOC_V2387_2423) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2386_2422) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2385_2420) else False)][(-1)] if (symdic.symdic_kl_x58x61 == KL_CTX.KL_LOC_V2384_2419) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2383_2418) else False)][(-1)] if ([] == KL_CTX.KL_LOC_V2382_2417) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2382_2417, [], KL_ARG_V3031_2400]), [setattr(KL_CTX, 'KL_LOC_Result_2427', [setattr(KL_CTX, 'KL_LOC_V2390_2428', tco_apply(shen_lazyderef, [KL_ARG_V3030_2399, KL_ARG_V3031_2400])), ([setattr(KL_CTX, 'KL_LOC_V2391_2429', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2390_2428[0], KL_ARG_V3031_2400])), ([setattr(KL_CTX, 'KL_LOC_V2392_2430', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2390_2428[1], KL_ARG_V3031_2400])), ([setattr(KL_CTX, 'KL_LOC_Semantics_2431', KL_CTX.KL_LOC_V2392_2430[0]), [setattr(KL_CTX, 'KL_LOC_V2393_2432', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2392_2430[1], KL_ARG_V3031_2400])), ([setattr(KL_CTX, 'KL_LOC_V2394_2433', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2393_2432[0], KL_ARG_V3031_2400])), ([setattr(KL_CTX, 'KL_LOC_V2395_2434', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2393_2432[1], KL_ARG_V3031_2400])), ([setattr(KL_CTX, 'KL_LOC_G_2435', KL_CTX.KL_LOC_V2395_2434[0]), [setattr(KL_CTX, 'KL_LOC_V2396_2436', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2395_2434[1], KL_ARG_V3031_2400])), ([tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2402, KL_ARG_V3031_2400, (lambda : tail_call(kl_bind, [KL_ARG_V3029_2398, [symdic.symdic_kl_where, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_G_2435, KL_ARG_V3031_2400]), [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Semantics_2431, KL_ARG_V3031_2400]), []]]], KL_ARG_V3031_2400, KL_ARG_V3032_2401]))])][(-1)] if ([] == KL_CTX.KL_LOC_V2396_2436) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2395_2434) else False)][(-1)] if (symdic.symdic_kl_where == KL_CTX.KL_LOC_V2394_2433) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2393_2432) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2392_2430) else False)][(-1)] if (symdic.symdic_kl_x58x61 == KL_CTX.KL_LOC_V2391_2429) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2390_2428) else False)][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2382_2417, KL_ARG_V3031_2400]), KL_CTX.KL_LOC_Result_2427][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2382_2417]) else False))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_V2397_2437', tco_apply(shen_lazyderef, [KL_ARG_V3028_2397, KL_ARG_V3031_2400])), ([setattr(KL_CTX, 'KL_LOC_X2369_2438', KL_CTX.KL_LOC_V2397_2437[0]), [setattr(KL_CTX, 'KL_LOC_Syntax_2439', KL_CTX.KL_LOC_V2397_2437[1]), [setattr(KL_CTX, 'KL_LOC_V2398_2440', tco_apply(shen_lazyderef, [KL_ARG_V3030_2399, KL_ARG_V3031_2400])), ([setattr(KL_CTX, 'KL_LOC_X_2441', KL_CTX.KL_LOC_V2398_2440[0]), [setattr(KL_CTX, 'KL_LOC_Rule_2442', KL_CTX.KL_LOC_V2398_2440[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_X_2441, KL_CTX.KL_LOC_X2369_2438, KL_ARG_V3031_2400, (lambda : tail_call(shen_getx45syntaxx43semantics, [KL_CTX.KL_LOC_Syntax_2439, KL_ARG_V3029_2398, KL_CTX.KL_LOC_Rule_2442, KL_ARG_V3031_2400, KL_ARG_V3032_2401]))])][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2398_2440) else False)][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2397_2437) else ([setattr(KL_CTX, 'KL_LOC_X2369_2443', tco_apply(shen_newpv, [KL_ARG_V3031_2400])), [setattr(KL_CTX, 'KL_LOC_Syntax_2444', tco_apply(shen_newpv, [KL_ARG_V3031_2400])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2397_2437, [KL_CTX.KL_LOC_X2369_2443, KL_CTX.KL_LOC_Syntax_2444], KL_ARG_V3031_2400]), [setattr(KL_CTX, 'KL_LOC_Result_2445', [setattr(KL_CTX, 'KL_LOC_V2399_2446', tco_apply(shen_lazyderef, [KL_ARG_V3030_2399, KL_ARG_V3031_2400])), ([setattr(KL_CTX, 'KL_LOC_X_2447', KL_CTX.KL_LOC_V2399_2446[0]), [setattr(KL_CTX, 'KL_LOC_Rule_2448', KL_CTX.KL_LOC_V2399_2446[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_X_2447, KL_CTX.KL_LOC_X2369_2443, KL_ARG_V3031_2400, (lambda : tail_call(shen_getx45syntaxx43semantics, [KL_CTX.KL_LOC_Syntax_2444, KL_ARG_V3029_2398, KL_CTX.KL_LOC_Rule_2448, KL_ARG_V3031_2400, KL_ARG_V3032_2401]))])][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2399_2446) else False)][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2397_2437, KL_ARG_V3031_2400]), KL_CTX.KL_LOC_Result_2445][(-1)]][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2397_2437]) else False))][(-1)] if (KL_CTX.KL_LOC_Case_2416 == False) else KL_CTX.KL_LOC_Case_2416)][(-1)] if (KL_CTX.KL_LOC_Case_2403 == False) else KL_CTX.KL_LOC_Case_2403)][(-1)]])][(-1)]
shen_add_fun('shen.get-syntax+semantics', shen_getx45syntaxx43semantics, 5)

@tail_recursion
def shen_syntaxx45check(KL_ARG_V3033_2449, KL_ARG_V3034_2450, KL_ARG_V3035_2451, KL_ARG_V3036_2452, KL_ARG_V3037_2453):

    class KL_Context:
        KL_LOC_Throwcontrol_2454 = None
        KL_LOC_Case_2455 = None
        KL_LOC_V2366_2456 = None
        KL_LOC_Case_2457 = None
        KL_LOC_V2367_2458 = None
        KL_LOC_X_2459 = None
        KL_LOC_Syntax_2460 = None
        KL_LOC_C_2461 = None
        KL_LOC_Xx38x38_2462 = None
        KL_LOC_B_2463 = None
        KL_LOC_V2368_2464 = None
        KL_LOC_X_2465 = None
        KL_LOC_Syntax_2466 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Throwcontrol_2454', tco_apply(shen_catchpoint, [])), tail_call(shen_cutpoint, [KL_CTX.KL_LOC_Throwcontrol_2454, [setattr(KL_CTX, 'KL_LOC_Case_2455', [setattr(KL_CTX, 'KL_LOC_V2366_2456', tco_apply(shen_lazyderef, [KL_ARG_V3033_2449, KL_ARG_V3036_2452])), ([tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V3037_2453])][(-1)] if ([] == KL_CTX.KL_LOC_V2366_2456) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_2457', [setattr(KL_CTX, 'KL_LOC_V2367_2458', tco_apply(shen_lazyderef, [KL_ARG_V3033_2449, KL_ARG_V3036_2452])), ([setattr(KL_CTX, 'KL_LOC_X_2459', KL_CTX.KL_LOC_V2367_2458[0]), [setattr(KL_CTX, 'KL_LOC_Syntax_2460', KL_CTX.KL_LOC_V2367_2458[1]), [setattr(KL_CTX, 'KL_LOC_C_2461', tco_apply(shen_newpv, [KL_ARG_V3036_2452])), [setattr(KL_CTX, 'KL_LOC_Xx38x38_2462', tco_apply(shen_newpv, [KL_ARG_V3036_2452])), [setattr(KL_CTX, 'KL_LOC_B_2463', tco_apply(shen_newpv, [KL_ARG_V3036_2452])), [tco_apply(shen_incinfs, []), tco_apply(kl_fwhen, [tco_apply(shen_grammar_symbolx63, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_2459, KL_ARG_V3036_2452])]), KL_ARG_V3036_2452, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2454, KL_ARG_V3036_2452, (lambda : tail_call(shen_tx42, [[KL_CTX.KL_LOC_X_2459, [symdic.symdic_kl_x58, [[[symdic.symdic_kl_list, [KL_CTX.KL_LOC_B_2463, []]], [symdic.symdic_kl_x61x61x62, [KL_CTX.KL_LOC_C_2461, []]]], []]]], KL_ARG_V3035_2451, KL_ARG_V3036_2452, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2454, KL_ARG_V3036_2452, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Xx38x38_2462, tco_apply(kl_concat, [symdic.symdic_kl_x38x38, tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_2459, KL_ARG_V3036_2452])]), KL_ARG_V3036_2452, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2454, KL_ARG_V3036_2452, (lambda : tail_call(shen_tx42, [[KL_CTX.KL_LOC_Xx38x38_2462, [symdic.symdic_kl_x58, [[symdic.symdic_kl_list, [KL_ARG_V3034_2450, []]], []]]], [[KL_CTX.KL_LOC_Xx38x38_2462, [symdic.symdic_kl_x58, [[symdic.symdic_kl_list, [KL_CTX.KL_LOC_B_2463, []]], []]]], KL_ARG_V3035_2451], KL_ARG_V3036_2452, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2454, KL_ARG_V3036_2452, (lambda : tail_call(shen_syntaxx45check, [KL_CTX.KL_LOC_Syntax_2460, KL_ARG_V3034_2450, KL_ARG_V3035_2451, KL_ARG_V3036_2452, KL_ARG_V3037_2453]))]))]))]))]))]))]))]))])][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2367_2458) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_V2368_2464', tco_apply(shen_lazyderef, [KL_ARG_V3033_2449, KL_ARG_V3036_2452])), ([setattr(KL_CTX, 'KL_LOC_X_2465', KL_CTX.KL_LOC_V2368_2464[0]), [setattr(KL_CTX, 'KL_LOC_Syntax_2466', KL_CTX.KL_LOC_V2368_2464[1]), [tco_apply(shen_incinfs, []), tco_apply(shen_tx42, [[KL_CTX.KL_LOC_X_2465, [symdic.symdic_kl_x58, [KL_ARG_V3034_2450, []]]], KL_ARG_V3035_2451, KL_ARG_V3036_2452, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2454, KL_ARG_V3036_2452, (lambda : tail_call(shen_syntaxx45check, [KL_CTX.KL_LOC_Syntax_2466, KL_ARG_V3034_2450, KL_ARG_V3035_2451, KL_ARG_V3036_2452, KL_ARG_V3037_2453]))]))])][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2368_2464) else False)][(-1)] if (KL_CTX.KL_LOC_Case_2457 == False) else KL_CTX.KL_LOC_Case_2457)][(-1)] if (KL_CTX.KL_LOC_Case_2455 == False) else KL_CTX.KL_LOC_Case_2455)][(-1)]])][(-1)]
shen_add_fun('shen.syntax-check', shen_syntaxx45check, 5)

@tail_recursion
def shen_semanticsx45check(KL_ARG_V3038_2467, KL_ARG_V3039_2468, KL_ARG_V3040_2469, KL_ARG_V3041_2470, KL_ARG_V3042_2471):

    class KL_Context:
        KL_LOC_Semanticsx42_2472 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Semanticsx42_2472', tco_apply(shen_newpv, [KL_ARG_V3041_2470])), [tco_apply(shen_incinfs, []), tail_call(kl_bind, [KL_CTX.KL_LOC_Semanticsx42_2472, tco_apply(shen_curry, [tco_apply(shen_renamex45semantics, [tco_apply(shen_deref, [KL_ARG_V3038_2467, KL_ARG_V3041_2470])])]), KL_ARG_V3041_2470, (lambda : tail_call(shen_tx42, [[KL_CTX.KL_LOC_Semanticsx42_2472, [symdic.symdic_kl_x58, [KL_ARG_V3039_2468, []]]], KL_ARG_V3040_2469, KL_ARG_V3041_2470, KL_ARG_V3042_2471]))])][(-1)]][(-1)]
shen_add_fun('shen.semantics-check', shen_semanticsx45check, 5)

@tail_recursion
def shen_renamex45semantics(KL_ARG_V3043_2473):
    global symdic
    return ([tco_apply(shen_renamex45semantics, [KL_ARG_V3043_2473[0]]), tco_apply(shen_renamex45semantics, [KL_ARG_V3043_2473[1]])] if shen_consp(KL_ARG_V3043_2473) else ([symdic.symdic_shen_x60x45sem, [KL_ARG_V3043_2473, []]] if tco_apply(shen_grammar_symbolx63, [KL_ARG_V3043_2473]) else (KL_ARG_V3043_2473 if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.rename-semantics', shen_renamex45semantics, 1)
shen_initialise_arity_table(shen_to_cons([Sym('absvector'), 1, symdic.symdic_kl_adjoin, 2, symdic.symdic_kl_and, 2, symdic.symdic_kl_append, 2, symdic.symdic_kl_arity, 1, symdic.symdic_kl_assoc, 2, symdic.symdic_kl_booleanx63, 1, symdic.symdic_kl_cd, 1, symdic.symdic_kl_compile, 3, Sym('concat'), 2, symdic.symdic_kl_cons, 2, symdic.symdic_kl_consx63, 1, symdic.symdic_kl_cn, 2, Sym('declare'), 2, symdic.symdic_kl_destroy, 1, symdic.symdic_kl_difference, 2, symdic.symdic_kl_do, 2, symdic.symdic_kl_elementx63, 2, symdic.symdic_kl_emptyx63, 1, symdic.symdic_kl_enablex45typex45theory, 1, Sym('interror'), 2, Sym('eval'), 1, symdic.symdic_kl_evalx45kl, 1, symdic.symdic_kl_explode, 1, symdic.symdic_kl_external, 1, symdic.symdic_kl_failx45if, 2, symdic.symdic_kl_fail, 0, symdic.symdic_kl_fix, 2, symdic.symdic_kl_findall, 5, symdic.symdic_kl_freeze, 1, symdic.symdic_kl_fst, 1, symdic.symdic_kl_gensym, 1, symdic.symdic_kl_get, 3, symdic.symdic_kl_getx45time, 1, symdic.symdic_kl_addressx45x62, 3, symdic.symdic_kl_x60x45address, 2, symdic.symdic_kl_x60x45vector, 2, symdic.symdic_kl_x62, 2, symdic.symdic_kl_x62x61, 2, symdic.symdic_kl_x61, 2, symdic.symdic_kl_hd, 1, symdic.symdic_kl_hdv, 1, symdic.symdic_kl_hdstr, 1, symdic.symdic_kl_head, 1, symdic.symdic_kl_if, 3, symdic.symdic_kl_integerx63, 1, symdic.symdic_kl_intern, 1, symdic.symdic_kl_identical, 4, symdic.symdic_kl_inferences, 0, symdic.symdic_kl_intersection, 2, symdic.symdic_kill, 0, symdic.symdic_kl_length, 1, symdic.symdic_kl_lineread, 0, symdic.symdic_kl_load, 1, symdic.symdic_kl_x60, 2, symdic.symdic_kl_x60x61, 2, symdic.symdic_kl_vector, 1, symdic.symdic_kl_macroexpand, 1, symdic.symdic_kl_map, 2, symdic.symdic_kl_mapcan, 2, symdic.symdic_kl_maxinferences, 1, symdic.symdic_kl_not, 1, symdic.symdic_kl_nth, 2, symdic.symdic_kl_nx45x62string, 1, symdic.symdic_kl_numberx63, 1, symdic.symdic_kl_occursx45check, 1, symdic.symdic_kl_occurrences, 2, symdic.symdic_kl_occursx45check, 1, symdic.symdic_optimise, 1, symdic.symdic_kl_or, 2, symdic.symdic_kl_package, 3, symdic.symdic_kl_pos, 2, symdic.symdic_kl_print, 1, symdic.symdic_kl_profile, 1, symdic.symdic_kl_profilex45results, 0, symdic.symdic_kl_pr, 2, symdic.symdic_kl_ps, 1, symdic.symdic_kl_preclude, 1, symdic.symdic_kl_precludex45allx45but, 1, symdic.symdic_kl_protect, 1, symdic.symdic_kl_addressx45x62, 3, symdic.symdic_kl_put, 4, Sym('shen.reassemble'), 2, symdic.symdic_kl_readx45filex45asx45string, 1, symdic.symdic_kl_readx45file, 1, symdic.symdic_kl_readx45byte, 1, symdic.symdic_kl_readx45fromx45string, 1, symdic.symdic_kl_remove, 2, symdic.symdic_kl_reverse, 1, symdic.symdic_kl_set, 2, symdic.symdic_kl_simplex45error, 1, symdic.symdic_kl_snd, 1, symdic.symdic_kl_specialise, 1, symdic.symdic_kl_spy, 1, symdic.symdic_kl_step, 1, symdic.symdic_kl_stinput, 0, symdic.symdic_kl_stoutput, 0, symdic.symdic_kl_stringx45x62n, 1, symdic.symdic_kl_stringx45x62symbol, 1, symdic.symdic_kl_stringx63, 1, Sym('shen.strong-warning'), 1, symdic.symdic_kl_subst, 3, symdic.symdic_shen_sum, 1, symdic.symdic_kl_symbolx63, 1, symdic.symdic_kl_tail, 1, symdic.symdic_kl_tl, 1, symdic.symdic_kl_tc, 1, symdic.symdic_kl_tcx63, 1, symdic.symdic_kl_thaw, 1, symdic.symdic_kl_tlstr, 1, symdic.symdic_kl_track, 1, symdic.symdic_kl_trapx45error, 2, symdic.symdic_kl_tuplex63, 1, symdic.symdic_kl_type, 1, symdic.symdic_kl_return, 3, symdic.symdic_kl_undefmacro, 1, symdic.symdic_kl_unprofile, 1, symdic.symdic_kl_unify, 4, symdic.symdic_kl_unifyx33, 4, symdic.symdic_kl_union, 2, symdic.symdic_kl_untrack, 1, symdic.symdic_kl_unspecialise, 1, symdic.symdic_kl_undefmacro, 1, symdic.symdic_kl_vector, 1, symdic.symdic_kl_vectorx45x62, 3, symdic.symdic_kl_value, 1, symdic.symdic_kl_variablex63, 1, symdic.symdic_kl_version, 1, Sym('warn'), 1, symdic.symdic_kl_writex45tox45file, 2, symdic.symdic_kl_yx45orx45nx63, 1, symdic.symdic_kl_x43, 2, symdic.symdic_kl_x42, 2, symdic.symdic_kl_x47, 2, symdic.symdic_kl_x45, 2, symdic.symdic_kl_x61x61, 2, symdic.symdic_kl_x60ex62, 1, symdic.symdic_kl_x64p, 2, symdic.symdic_kl_x64v, 2, symdic.symdic_kl_x64s, 2, symdic.symdic_kl_preclude, 1, symdic.symdic_kl_include, 1, symdic.symdic_kl_precludex45allx45but, 1, symdic.symdic_kl_includex45allx45but, 1, symdic.symdic_kl_where, 2]))
kl_put(shen_intern('shen'), symdic.symdic_shen_externalx45symbols, shen_to_cons([symdic.symdic_kl_x33, symdic.symdic_kl_x125, symdic.symdic_kl_x123, symdic.symdic_kl_x45x45x62, symdic.symdic_kl_x60x45x45, symdic.symdic_kl_x38x38, symdic.symdic_kl_x58, symdic.symdic_kl_x59, symdic.symdic_kl_x58x45, symdic.symdic_kl_x58x61, symdic.symdic_kl__, symdic.symdic_kl_x42languagex42, symdic.symdic_kl_x42implementationx42, symdic.symdic_kl_x42stinputx42, symdic.symdic_kl_x42homex45directoryx42, symdic.symdic_kl_x42versionx42, symdic.symdic_kl_x42maximumx45printx45sequencex45sizex42, symdic.symdic_kl_x42macrosx42, Sym('*os*'), Sym('*release*'), symdic.symdic_kl_x42propertyx45vectorx42, symdic.symdic_kl_x64v, symdic.symdic_kl_x64p, symdic.symdic_kl_x64s, symdic.symdic_kl_x42portx42, symdic.symdic_kl_x42portersx42, symdic.symdic_x42hushx42, symdic.symdic_kl_x60x45, symdic.symdic_kl_x45x62, symdic.symdic_kl_x60ex62, symdic.symdic_kl_x61x61, symdic.symdic_kl_x61, symdic.symdic_kl_x62x61, symdic.symdic_kl_x62, symdic.symdic_kl_x47_, symdic.symdic_kl_x61x33, symdic.symdic_kl_x36, symdic.symdic_kl_x45, symdic.symdic_kl_x47, symdic.symdic_kl_x42, symdic.symdic_kl_x43, symdic.symdic_kl_x60x61, symdic.symdic_kl_x60, symdic.symdic_kl_x62x62, tco_apply(kl_vector, [0]), symdic.symdic_kl_x61x61x62, symdic.symdic_kl_yx45orx45nx63, symdic.symdic_kl_writex45tox45file, symdic.symdic_kl_where, symdic.symdic_kl_when, Sym('warn'), symdic.symdic_kl_version, symdic.symdic_kl_verified, symdic.symdic_kl_variablex63, symdic.symdic_kl_value, symdic.symdic_kl_vectorx45x62, symdic.symdic_kl_x60x45vector, symdic.symdic_kl_vector, symdic.symdic_kl_vectorx63, symdic.symdic_kl_unspecialise, symdic.symdic_kl_untrack, symdic.symdic_kl_unit, Sym('shen.unix'), symdic.symdic_kl_union, symdic.symdic_kl_unify, symdic.symdic_kl_unifyx33, symdic.symdic_kl_unprofile, symdic.symdic_kl_undefmacro, symdic.symdic_kl_return, symdic.symdic_kl_type, symdic.symdic_kl_tuplex63, True, symdic.symdic_kl_trapx45error, symdic.symdic_kl_track, symdic.symdic_kl_time, symdic.symdic_kl_thaw, symdic.symdic_kl_tcx63, symdic.symdic_kl_tc, symdic.symdic_kl_tl, symdic.symdic_kl_tlstr, symdic.symdic_kl_tlv, symdic.symdic_kl_tail, symdic.symdic_kl_systemf, symdic.symdic_kl_synonyms, symdic.symdic_kl_symbol, symdic.symdic_kl_symbolx63, symdic.symdic_kl_stringx45x62symbol, symdic.symdic_kl_subst, symdic.symdic_kl_stringx63, symdic.symdic_kl_stringx45x62n, symdic.symdic_kl_stream, symdic.symdic_kl_string, symdic.symdic_kl_stinput, symdic.symdic_kl_stoutput, symdic.symdic_kl_step, symdic.symdic_kl_spy, symdic.symdic_kl_specialise, symdic.symdic_kl_snd, symdic.symdic_kl_simplex45error, symdic.symdic_kl_set, Sym('save'), symdic.symdic_kl_str, symdic.symdic_kl_run, symdic.symdic_kl_reverse, symdic.symdic_kl_remove, symdic.symdic_kl_read, symdic.symdic_readx43, symdic.symdic_kl_readx45file, symdic.symdic_kl_readx45filex45asx45bytelist, symdic.symdic_kl_readx45filex45asx45string, symdic.symdic_kl_readx45byte, symdic.symdic_kl_readx45fromx45string, Sym('quit'), symdic.symdic_kl_put, symdic.symdic_kl_preclude, symdic.symdic_kl_precludex45allx45but, symdic.symdic_kl_ps, symdic.symdic_kl_prologx63, symdic.symdic_kl_protect, symdic.symdic_kl_profilex45results, symdic.symdic_kl_profile, symdic.symdic_kl_print, symdic.symdic_kl_pr, symdic.symdic_kl_pos, symdic.symdic_kl_package, symdic.symdic_kl_output, symdic.symdic_kl_out, symdic.symdic_kl_or, symdic.symdic_kl_open, symdic.symdic_kl_occurrences, symdic.symdic_kl_occursx45check, symdic.symdic_kl_nx45x62string, symdic.symdic_kl_numberx63, symdic.symdic_kl_number, symdic.symdic_kl_null, symdic.symdic_kl_nth, symdic.symdic_kl_not, symdic.symdic_kl_nl, symdic.symdic_kl_mode, Sym('macro'), symdic.symdic_kl_macroexpand, symdic.symdic_kl_maxinferences, symdic.symdic_kl_mapcan, symdic.symdic_kl_map, symdic.symdic_kl_makex45string, symdic.symdic_kl_load, symdic.symdic_kl_loaded, symdic.symdic_kl_list, symdic.symdic_kl_lineread, symdic.symdic_kl_limit, symdic.symdic_kl_length, symdic.symdic_kl_let, symdic.symdic_kl_lazy, symdic.symdic_kl_lambda, symdic.symdic_kill, symdic.symdic_kl_is, symdic.symdic_kl_intersection, symdic.symdic_kl_inferences, symdic.symdic_kl_intern, symdic.symdic_kl_integerx63, symdic.symdic_kl_input, symdic.symdic_kl_inputx43, symdic.symdic_kl_include, symdic.symdic_kl_includex45allx45but, symdic.symdic_kl_in, symdic.symdic_kl_if, symdic.symdic_kl_identical, symdic.symdic_kl_head, symdic.symdic_kl_hd, symdic.symdic_kl_hdv, symdic.symdic_kl_hdstr, symdic.symdic_kl_hash, symdic.symdic_kl_get, symdic.symdic_kl_getx45time, symdic.symdic_kl_gensym, symdic.symdic_kl_function, symdic.symdic_kl_fst, symdic.symdic_kl_freeze, symdic.symdic_kl_fix, symdic.symdic_kl_file, symdic.symdic_kl_fail, symdic.symdic_kl_failx45if, symdic.symdic_kl_fwhen, symdic.symdic_kl_findall, False, symdic.symdic_kl_enablex45typex45theory, symdic.symdic_kl_explode, symdic.symdic_kl_external, symdic.symdic_kl_exception, symdic.symdic_kl_evalx45kl, Sym('eval'), symdic.symdic_kl_errorx45tox45string, symdic.symdic_kl_error, symdic.symdic_kl_emptyx63, symdic.symdic_kl_elementx63, symdic.symdic_kl_do, symdic.symdic_kl_difference, symdic.symdic_kl_destroy, symdic.symdic_kl_defun, symdic.symdic_kl_define, symdic.symdic_kl_defmacro, symdic.symdic_kl_defcc, symdic.symdic_kl_defprolog, Sym('declare'), symdic.symdic_kl_datatype, symdic.symdic_kl_cut, symdic.symdic_kl_cn, symdic.symdic_kl_consx63, symdic.symdic_kl_cons, symdic.symdic_kl_cond, Sym('concat'), symdic.symdic_kl_compile, symdic.symdic_kl_cd, symdic.symdic_kl_cases, symdic.symdic_kl_call, symdic.symdic_kl_close, symdic.symdic_kl_bind, symdic.symdic_kl_boundx63, symdic.symdic_kl_booleanx63, symdic.symdic_kl_boolean, symdic.symdic_kl_barx33, symdic.symdic_kl_assoc, symdic.symdic_kl_arity, symdic.symdic_kl_append, symdic.symdic_kl_and, symdic.symdic_kl_adjoin, symdic.symdic_kl_x60x45address, symdic.symdic_kl_addressx45x62, symdic.symdic_kl_absvectorx63, Sym('absvector'), symdic.symdic_kl_abort]), shen_get(symdic.symdic_kl_x42propertyx45vectorx42))
apply(kl_declare, [symdic.symdic_kl_absvectorx63, [symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_boolean, []]]]])
apply(kl_declare, [symdic.symdic_kl_adjoin, [symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [[[symdic.symdic_kl_list, [symdic.symdic_A, []]], [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_list, [symdic.symdic_A, []]], []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_and, [symdic.symdic_kl_boolean, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_boolean, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_boolean, []]]], []]]]])
apply(kl_declare, [symdic.symdic_shen_app, [symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_string, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_symbol, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_string, []]]], []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_append, [[symdic.symdic_kl_list, [symdic.symdic_A, []]], [symdic.symdic_kl_x45x45x62, [[[symdic.symdic_kl_list, [symdic.symdic_A, []]], [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_list, [symdic.symdic_A, []]], []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_arity, [symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_number, []]]]])
apply(kl_declare, [symdic.symdic_kl_assoc, [symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [[[symdic.symdic_kl_list, [[symdic.symdic_kl_list, [symdic.symdic_A, []]], []]], [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_list, [symdic.symdic_A, []]], []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_booleanx63, [symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_boolean, []]]]])
apply(kl_declare, [symdic.symdic_kl_boundx63, [symdic.symdic_kl_symbol, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_boolean, []]]]])
apply(kl_declare, [symdic.symdic_kl_cd, [symdic.symdic_kl_string, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_string, []]]]])
apply(kl_declare, [symdic.symdic_kl_close, [[symdic.symdic_kl_stream, [symdic.symdic_A, []]], [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_list, [symdic.symdic_B, []]], []]]]])
apply(kl_declare, [symdic.symdic_kl_cn, [symdic.symdic_kl_string, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_string, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_string, []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_compile, [[[symdic.symdic_kl_list, [symdic.symdic_A, []]], [symdic.symdic_kl_x61x61x62, [symdic.symdic_B, []]]], [symdic.symdic_kl_x45x45x62, [[[symdic.symdic_kl_list, [symdic.symdic_A, []]], [symdic.symdic_kl_x45x45x62, [[[[symdic.symdic_kl_list, [symdic.symdic_A, []]], [symdic.symdic_kl_x45x45x62, [symdic.symdic_B, []]]], [symdic.symdic_kl_x45x45x62, [symdic.symdic_B, []]]], []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_consx63, [symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_boolean, []]]]])
apply(kl_declare, [symdic.symdic_kl_destroy, [[symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [symdic.symdic_B, []]]], [symdic.symdic_kl_x45x45x62, [[symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [symdic.symdic_B, []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_difference, [[symdic.symdic_kl_list, [symdic.symdic_A, []]], [symdic.symdic_kl_x45x45x62, [[[symdic.symdic_kl_list, [symdic.symdic_A, []]], [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_list, [symdic.symdic_A, []]], []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_do, [symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_B, [symdic.symdic_kl_x45x45x62, [symdic.symdic_B, []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_x60ex62, [[symdic.symdic_kl_list, [symdic.symdic_A, []]], [symdic.symdic_kl_x61x61x62, [[symdic.symdic_kl_list, [symdic.symdic_B, []]], []]]]])
apply(kl_declare, [symdic.symdic_x60x33x62, [[symdic.symdic_kl_list, [symdic.symdic_A, []]], [symdic.symdic_kl_x61x61x62, [[symdic.symdic_kl_list, [symdic.symdic_A, []]], []]]]])
apply(kl_declare, [symdic.symdic_kl_elementx63, [symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [[[symdic.symdic_kl_list, [symdic.symdic_A, []]], [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_boolean, []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_emptyx63, [symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_boolean, []]]]])
apply(kl_declare, [symdic.symdic_kl_enablex45typex45theory, [symdic.symdic_kl_symbol, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_boolean, []]]]])
apply(kl_declare, [symdic.symdic_kl_external, [symdic.symdic_kl_symbol, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_list, [symdic.symdic_kl_symbol, []]], []]]]])
apply(kl_declare, [symdic.symdic_kl_errorx45tox45string, [symdic.symdic_kl_exception, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_string, []]]]])
apply(kl_declare, [symdic.symdic_kl_explode, [symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_list, [symdic.symdic_kl_string, []]], []]]]])
apply(kl_declare, [symdic.symdic_kl_failx45if, [[symdic.symdic_kl_symbol, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_boolean, []]]], [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_symbol, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_symbol, []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_fix, [[symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [symdic.symdic_A, []]]], [symdic.symdic_kl_x45x45x62, [[symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [symdic.symdic_A, []]]], []]]]])
apply(kl_declare, [symdic.symdic_format, [[symdic.symdic_kl_stream, [symdic.symdic_kl_out, []]], [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_string, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_string, []]]], []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_freeze, [symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_lazy, [symdic.symdic_A, []]], []]]]])
apply(kl_declare, [symdic.symdic_kl_fst, [[symdic.symdic_A, [symdic.symdic_kl_x42, [symdic.symdic_B, []]]], [symdic.symdic_kl_x45x45x62, [symdic.symdic_A, []]]]])
apply(kl_declare, [symdic.symdic_kl_gensym, [symdic.symdic_kl_symbol, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_symbol, []]]]])
apply(kl_declare, [symdic.symdic_kl_x60x45vector, [[symdic.symdic_kl_vector, [symdic.symdic_A, []]], [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_number, [symdic.symdic_kl_x45x45x62, [symdic.symdic_A, []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_vectorx45x62, [[symdic.symdic_kl_vector, [symdic.symdic_A, []]], [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_number, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_vector, [symdic.symdic_A, []]], []]]], []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_vector, [symdic.symdic_kl_number, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_vector, [symdic.symdic_A, []]], []]]]])
apply(kl_declare, [symdic.symdic_kl_getx45time, [symdic.symdic_kl_symbol, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_number, []]]]])
apply(kl_declare, [symdic.symdic_kl_hash, [symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_number, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_number, []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_head, [[symdic.symdic_kl_list, [symdic.symdic_A, []]], [symdic.symdic_kl_x45x45x62, [symdic.symdic_A, []]]]])
apply(kl_declare, [symdic.symdic_kl_hdv, [[symdic.symdic_kl_vector, [symdic.symdic_A, []]], [symdic.symdic_kl_x45x45x62, [symdic.symdic_A, []]]]])
apply(kl_declare, [symdic.symdic_kl_hdstr, [symdic.symdic_kl_string, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_string, []]]]])
apply(kl_declare, [symdic.symdic_kl_if, [symdic.symdic_kl_boolean, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [symdic.symdic_A, []]]], []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_include, [[symdic.symdic_kl_list, [symdic.symdic_kl_symbol, []]], [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_list, [symdic.symdic_kl_symbol, []]], []]]]])
apply(kl_declare, [symdic.symdic_kl_includex45allx45but, [[symdic.symdic_kl_list, [symdic.symdic_kl_symbol, []]], [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_list, [symdic.symdic_kl_symbol, []]], []]]]])
apply(kl_declare, [symdic.symdic_kl_inferences, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_number, []]]])
apply(kl_declare, [symdic.symdic_shen_insert, [symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_string, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_string, []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_integerx63, [symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_boolean, []]]]])
apply(kl_declare, [symdic.symdic_kl_intersection, [[symdic.symdic_kl_list, [symdic.symdic_A, []]], [symdic.symdic_kl_x45x45x62, [[[symdic.symdic_kl_list, [symdic.symdic_A, []]], [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_list, [symdic.symdic_A, []]], []]]], []]]]])
apply(kl_declare, [symdic.symdic_kill, [symdic.symdic_kl_x45x45x62, [symdic.symdic_A, []]]])
apply(kl_declare, [symdic.symdic_kl_length, [[symdic.symdic_kl_list, [symdic.symdic_A, []]], [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_number, []]]]])
apply(kl_declare, [symdic.symdic_kl_limit, [[symdic.symdic_kl_vector, [symdic.symdic_A, []]], [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_number, []]]]])
apply(kl_declare, [symdic.symdic_kl_load, [symdic.symdic_kl_string, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_symbol, []]]]])
apply(kl_declare, [symdic.symdic_kl_map, [[symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [symdic.symdic_B, []]]], [symdic.symdic_kl_x45x45x62, [[[symdic.symdic_kl_list, [symdic.symdic_A, []]], [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_list, [symdic.symdic_B, []]], []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_mapcan, [[symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_list, [symdic.symdic_B, []]], []]]], [symdic.symdic_kl_x45x45x62, [[[symdic.symdic_kl_list, [symdic.symdic_A, []]], [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_list, [symdic.symdic_B, []]], []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_maxinferences, [symdic.symdic_kl_number, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_number, []]]]])
apply(kl_declare, [symdic.symdic_kl_nx45x62string, [symdic.symdic_kl_number, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_string, []]]]])
apply(kl_declare, [symdic.symdic_kl_nl, [symdic.symdic_kl_number, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_number, []]]]])
apply(kl_declare, [symdic.symdic_kl_not, [symdic.symdic_kl_boolean, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_boolean, []]]]])
apply(kl_declare, [symdic.symdic_kl_nth, [symdic.symdic_kl_number, [symdic.symdic_kl_x45x45x62, [[[symdic.symdic_kl_list, [symdic.symdic_A, []]], [symdic.symdic_kl_x45x45x62, [symdic.symdic_A, []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_numberx63, [symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_boolean, []]]]])
apply(kl_declare, [symdic.symdic_kl_occurrences, [symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_B, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_number, []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_occursx45check, [symdic.symdic_kl_symbol, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_boolean, []]]]])
apply(kl_declare, [symdic.symdic_optimise, [symdic.symdic_kl_symbol, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_boolean, []]]]])
apply(kl_declare, [symdic.symdic_kl_or, [symdic.symdic_kl_boolean, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_boolean, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_boolean, []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_pos, [symdic.symdic_kl_string, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_number, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_string, []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_pr, [symdic.symdic_kl_string, [symdic.symdic_kl_x45x45x62, [[[symdic.symdic_kl_stream, [symdic.symdic_kl_out, []]], [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_string, []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_print, [symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [symdic.symdic_A, []]]]])
apply(kl_declare, [symdic.symdic_kl_profile, [[symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [symdic.symdic_B, []]]], [symdic.symdic_kl_x45x45x62, [[symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [symdic.symdic_B, []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_preclude, [[symdic.symdic_kl_list, [symdic.symdic_kl_symbol, []]], [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_list, [symdic.symdic_kl_symbol, []]], []]]]])
apply(kl_declare, [symdic.symdic_shen_procx45nl, [symdic.symdic_kl_string, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_string, []]]]])
apply(kl_declare, [symdic.symdic_kl_profilex45results, [symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_symbol, []]]]])
apply(kl_declare, [symdic.symdic_kl_protect, [symdic.symdic_kl_symbol, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_symbol, []]]]])
apply(kl_declare, [symdic.symdic_kl_precludex45allx45but, [[symdic.symdic_kl_list, [symdic.symdic_kl_symbol, []]], [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_list, [symdic.symdic_kl_symbol, []]], []]]]])
apply(kl_declare, [symdic.symdic_shen_prhush, [symdic.symdic_kl_string, [symdic.symdic_kl_x45x45x62, [[[symdic.symdic_kl_stream, [symdic.symdic_kl_out, []]], [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_string, []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_ps, [symdic.symdic_kl_symbol, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_list, [symdic.symdic_kl_unit, []]], []]]]])
apply(kl_declare, [symdic.symdic_kl_readx45byte, [[symdic.symdic_kl_stream, [symdic.symdic_kl_in, []]], [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_number, []]]]])
apply(kl_declare, [symdic.symdic_kl_readx45filex45asx45bytelist, [symdic.symdic_kl_string, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_list, [symdic.symdic_kl_number, []]], []]]]])
apply(kl_declare, [symdic.symdic_kl_readx45filex45asx45string, [symdic.symdic_kl_string, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_string, []]]]])
apply(kl_declare, [symdic.symdic_kl_readx45file, [symdic.symdic_kl_string, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_list, [symdic.symdic_kl_unit, []]], []]]]])
apply(kl_declare, [symdic.symdic_kl_readx45fromx45string, [symdic.symdic_kl_string, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_list, [symdic.symdic_kl_unit, []]], []]]]])
apply(kl_declare, [symdic.symdic_kl_remove, [symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [[[symdic.symdic_kl_list, [symdic.symdic_A, []]], [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_list, [symdic.symdic_A, []]], []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_reverse, [[symdic.symdic_kl_list, [symdic.symdic_A, []]], [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_list, [symdic.symdic_A, []]], []]]]])
apply(kl_declare, [symdic.symdic_kl_simplex45error, [symdic.symdic_kl_string, [symdic.symdic_kl_x45x45x62, [symdic.symdic_A, []]]]])
apply(kl_declare, [symdic.symdic_kl_snd, [[symdic.symdic_A, [symdic.symdic_kl_x42, [symdic.symdic_B, []]]], [symdic.symdic_kl_x45x45x62, [symdic.symdic_B, []]]]])
apply(kl_declare, [symdic.symdic_kl_specialise, [symdic.symdic_kl_symbol, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_symbol, []]]]])
apply(kl_declare, [symdic.symdic_kl_spy, [symdic.symdic_kl_symbol, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_boolean, []]]]])
apply(kl_declare, [symdic.symdic_kl_step, [symdic.symdic_kl_symbol, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_boolean, []]]]])
apply(kl_declare, [symdic.symdic_kl_stinput, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_stream, [symdic.symdic_kl_in, []]], []]]])
apply(kl_declare, [symdic.symdic_kl_stoutput, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_stream, [symdic.symdic_kl_out, []]], []]]])
apply(kl_declare, [symdic.symdic_kl_stringx63, [symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_boolean, []]]]])
apply(kl_declare, [symdic.symdic_kl_str, [symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_string, []]]]])
apply(kl_declare, [symdic.symdic_kl_stringx45x62n, [symdic.symdic_kl_string, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_number, []]]]])
apply(kl_declare, [symdic.symdic_kl_stringx45x62symbol, [symdic.symdic_kl_string, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_symbol, []]]]])
apply(kl_declare, [symdic.symdic_shen_sum, [[symdic.symdic_kl_list, [symdic.symdic_kl_number, []]], [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_number, []]]]])
apply(kl_declare, [symdic.symdic_kl_symbolx63, [symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_boolean, []]]]])
apply(kl_declare, [symdic.symdic_kl_systemf, [symdic.symdic_kl_symbol, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_list, [symdic.symdic_kl_symbol, []]], []]]]])
apply(kl_declare, [symdic.symdic_kl_tail, [[symdic.symdic_kl_list, [symdic.symdic_A, []]], [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_list, [symdic.symdic_A, []]], []]]]])
apply(kl_declare, [symdic.symdic_kl_tlstr, [symdic.symdic_kl_string, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_string, []]]]])
apply(kl_declare, [symdic.symdic_kl_tlv, [[symdic.symdic_kl_vector, [symdic.symdic_A, []]], [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_vector, [symdic.symdic_A, []]], []]]]])
apply(kl_declare, [symdic.symdic_kl_tc, [symdic.symdic_kl_symbol, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_boolean, []]]]])
apply(kl_declare, [symdic.symdic_kl_tcx63, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_boolean, []]]])
apply(kl_declare, [symdic.symdic_kl_thaw, [[symdic.symdic_kl_lazy, [symdic.symdic_A, []]], [symdic.symdic_kl_x45x45x62, [symdic.symdic_A, []]]]])
apply(kl_declare, [symdic.symdic_kl_track, [symdic.symdic_kl_symbol, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_symbol, []]]]])
apply(kl_declare, [symdic.symdic_kl_trapx45error, [symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [[[symdic.symdic_kl_exception, [symdic.symdic_kl_x45x45x62, [symdic.symdic_A, []]]], [symdic.symdic_kl_x45x45x62, [symdic.symdic_A, []]]], []]]]])
apply(kl_declare, [symdic.symdic_shen_truncate, [symdic.symdic_kl_string, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_string, []]]]])
apply(kl_declare, [symdic.symdic_kl_tuplex63, [symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_boolean, []]]]])
apply(kl_declare, [symdic.symdic_kl_undefmacro, [symdic.symdic_kl_symbol, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_symbol, []]]]])
apply(kl_declare, [symdic.symdic_kl_union, [[symdic.symdic_kl_list, [symdic.symdic_A, []]], [symdic.symdic_kl_x45x45x62, [[[symdic.symdic_kl_list, [symdic.symdic_A, []]], [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_list, [symdic.symdic_A, []]], []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_unprofile, [[symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [symdic.symdic_B, []]]], [symdic.symdic_kl_x45x45x62, [[symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [symdic.symdic_B, []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_untrack, [symdic.symdic_kl_symbol, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_symbol, []]]]])
apply(kl_declare, [symdic.symdic_kl_unspecialise, [symdic.symdic_kl_symbol, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_symbol, []]]]])
apply(kl_declare, [symdic.symdic_kl_variablex63, [symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_boolean, []]]]])
apply(kl_declare, [symdic.symdic_kl_vectorx63, [symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_boolean, []]]]])
apply(kl_declare, [symdic.symdic_kl_version, [symdic.symdic_kl_string, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_string, []]]]])
apply(kl_declare, [symdic.symdic_kl_writex45tox45file, [symdic.symdic_kl_string, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [symdic.symdic_A, []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_yx45orx45nx63, [symdic.symdic_kl_string, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_boolean, []]]]])
apply(kl_declare, [symdic.symdic_kl_x62, [symdic.symdic_kl_number, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_number, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_boolean, []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_x60, [symdic.symdic_kl_number, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_number, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_boolean, []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_x62x61, [symdic.symdic_kl_number, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_number, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_boolean, []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_x60x61, [symdic.symdic_kl_number, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_number, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_boolean, []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_x61, [symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_boolean, []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_x43, [symdic.symdic_kl_number, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_number, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_number, []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_x47, [symdic.symdic_kl_number, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_number, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_number, []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_x45, [symdic.symdic_kl_number, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_number, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_number, []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_x42, [symdic.symdic_kl_number, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_number, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_number, []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_x61x61, [symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_B, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_boolean, []]]], []]]]])
# included at the end of shen.py

def shen_expt(KL_ARG_V1518_757, KL_ARG_V1519_758):
    KL_ARG_V1518_757, KL_ARG_V1519_758 = float(KL_ARG_V1518_757), float(KL_ARG_V1519_758)
    return (1 if (0 == KL_ARG_V1519_758) else ((KL_ARG_V1518_757 * tco_apply(shen_expt, [KL_ARG_V1518_757, (KL_ARG_V1519_758 - 1)])) if (KL_ARG_V1519_758 > 0) else ((1 * (tco_apply(shen_expt, [KL_ARG_V1518_757, (KL_ARG_V1519_758 + 1)]) / KL_ARG_V1518_757)) if True else shen_simple_error('condition failure'))))

def kl_booleanx63(KL_ARG_V1857_1068):
    if isinstance(KL_ARG_V1857_1068, Sym) and (KL_ARG_V1857_1068.sym == "true" or KL_ARG_V1857_1068.sym == "false"):
        return True
    else:
        return (True if (True == KL_ARG_V1857_1068) else (True if (False == KL_ARG_V1857_1068) else (False if True else shen_simple_error('condition failure'))))

