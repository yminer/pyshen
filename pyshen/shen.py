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
    symdic_kl_x58x45 = Sym(':-')
    symdic_kl_mapcan = Sym('mapcan')
    symdic_V = Sym('V')
    symdic_shen_casesx45macro = Sym('shen.cases-macro')
    symdic_kl_integerx63 = Sym('integer?')
    symdic_kl_x58x61 = Sym(':=')
    symdic_shen_sysx45error = Sym('shen.sys-error')
    symdic_shen_explicit_modes = Sym('shen.explicit_modes')
    symdic_shen_free_variable_check = Sym('shen.free_variable_check')
    symdic_kl_inferences = Sym('inferences')
    symdic_shen_linearise_help = Sym('shen.linearise_help')
    symdic_shen_explodex45h = Sym('shen.explode-h')
    symdic_kl_tl = Sym('tl')
    symdic_shen_curryx45type = Sym('shen.curry-type')
    symdic_kl_adjoin = Sym('adjoin')
    symdic_shen_yacc = Sym('shen.yacc')
    symdic_kl_include = Sym('include')
    symdic_shen_incinfs = Sym('shen.incinfs')
    symdic_kl_tc = Sym('tc')
    symdic_shen_printx45pastx45inputs = Sym('shen.print-past-inputs')
    symdic_kl_booleanx63 = Sym('boolean?')
    symdic_kl_string = Sym('string')
    symdic_shen_procx45inputx43 = Sym('shen.proc-input+')
    symdic_shen_x45nullx45 = Sym('shen.-null-')
    symdic_P = Sym('P')
    symdic_shen_readx45charx45h = Sym('shen.read-char-h')
    symdic_kl_difference = Sym('difference')
    symdic_kl_readx45filex45asx45string = Sym('read-file-as-string')
    symdic_shen_ue = Sym('shen.ue')
    symdic_kl_reverse = Sym('reverse')
    symdic_kl_x42macrosx42 = Sym('*macros*')
    symdic_kl_list = Sym('list')
    symdic_kl_gensym = Sym('gensym')
    symdic_kl_consx63 = Sym('cons?')
    symdic_kl_vector = Sym('vector')
    symdic_shen_complexity = Sym('shen.complexity')
    symdic_shen_post = Sym('shen.post')
    symdic_kl_x45x62 = Sym('->')
    symdic_shen_assocx45macro = Sym('shen.assoc-macro')
    symdic_shen_constructx45premissx45literal = Sym('shen.construct-premiss-literal')
    symdic_kl_prologx63 = Sym('prolog?')
    symdic_shen_typetable = Sym('shen.typetable')
    symdic_kl_x42stinputx42 = Sym('*stinput*')
    symdic_kl_append = Sym('append')
    symdic_G = Sym('G')
    symdic_kl_vectorx63 = Sym('vector?')
    symdic_kl_x43 = Sym('+')
    symdic_shen_nextline = Sym('shen.nextline')
    symdic_kl_x64s = Sym('@s')
    symdic_kl_x64p = Sym('@p')
    symdic_kl_version = Sym('version')
    symdic_kl_x64v = Sym('@v')
    symdic_shen_synonymsx45help = Sym('shen.synonyms-help')
    symdic_kl_x59 = Sym(';')
    symdic_shen_em_help = Sym('shen.em_help')
    symdic_kl_undefmacro = Sym('undefmacro')
    symdic_kl_hash = Sym('hash')
    symdic_shen_x42datatypesx42 = Sym('shen.*datatypes*')
    symdic_K = Sym('K')
    symdic_kl_trapx45error = Sym('trap-error')
    symdic_shen_absx45macro = Sym('shen.abs-macro')
    symdic_kl_x60x45vector = Sym('<-vector')
    symdic_kl_let = Sym('let')
    symdic_kl_x38x38 = Sym('&&')
    symdic_shen_cl = Sym('shen.cl')
    symdic_kl_tlstr = Sym('tlstr')
    symdic_shen_prologx45macro = Sym('shen.prolog-macro')
    symdic_shen_toplevel_evaluate = Sym('shen.toplevel_evaluate')
    symdic_Stream = Sym('Stream')
    symdic_Record = Sym('Record')
    symdic_shen_bytex45x62digit = Sym('shen.byte->digit')
    symdic_shen_processx45datatype = Sym('shen.process-datatype')
    symdic_Freeze = Sym('Freeze')
    symdic_kl_x123 = Sym('{')
    symdic_shen_group_clauses = Sym('shen.group_clauses')
    symdic_kl_simplex45error = Sym('simple-error')
    symdic_shen_pvarx63 = Sym('shen.pvar?')
    symdic_kl_boolean = Sym('boolean')
    symdic_shen_collect = Sym('shen.collect')
    symdic_kl_unit = Sym('unit')
    symdic_kl_x60x45x45 = Sym('<--')
    symdic_shen_make_mu_application = Sym('shen.make_mu_application')
    symdic_shen_complexity_head = Sym('shen.complexity_head')
    symdic_shen_x42signedfuncsx42 = Sym('shen.*signedfuncs*')
    symdic_kl_tail = Sym('tail')
    symdic_kl_call = Sym('call')
    symdic_kl_type = Sym('type')
    symdic_kl_nx45x62string = Sym('n->string')
    symdic_kl_x60x61 = Sym('<=')
    symdic_shen_pvar = Sym('shen.pvar')
    symdic_F = Sym('F')
    symdic_shen_x42spyx42 = Sym('shen.*spy*')
    symdic_kl_stinput = Sym('stinput')
    symdic_shen_embedx45and = Sym('shen.embed-and')
    symdic_kl_cases = Sym('cases')
    symdic_shen_internx45type = Sym('shen.intern-type')
    symdic_shen_split_cc_rules = Sym('shen.split_cc_rules')
    symdic_shen_cc_body = Sym('shen.cc_body')
    symdic_shen_removetype = Sym('shen.removetype')
    symdic_kl_spy = Sym('spy')
    symdic_kl_stream = Sym('stream')
    symdic_shen_aritycheck = Sym('shen.aritycheck')
    symdic_shen_single = Sym('shen.single')
    symdic_shen_then = Sym('shen.then')
    symdic_shen_showx45assumptions = Sym('shen.show-assumptions')
    symdic_shen_readx45error = Sym('shen.read-error')
    symdic_kl_inputx43 = Sym('input+')
    symdic_shen_unbindv = Sym('shen.unbindv')
    symdic_kl_x33 = Sym('!')
    symdic_shen_unwindx45types = Sym('shen.unwind-types')
    symdic_shen_extract_vars = Sym('shen.extract_vars')
    symdic_kl_includex45allx45but = Sym('include-all-but')
    symdic_shen_removex45synonyms = Sym('shen.remove-synonyms')
    symdic_kl_emptyx63 = Sym('empty?')
    symdic_kl_x42homex45directoryx42 = Sym('*home-directory*')
    symdic_shen_rulesx45x62hornx45clauses = Sym('shen.rules->horn-clauses')
    symdic_shen_aum = Sym('shen.aum')
    symdic_kl_profile = Sym('profile')
    symdic_shen_nextx4550 = Sym('shen.next-50')
    symdic_kl_snd = Sym('snd')
    symdic_shen_failx33 = Sym('shen.fail!')
    symdic_shen_initialise_arity_table = Sym('shen.initialise_arity_table')
    symdic_shen_x42gensymx42 = Sym('shen.*gensym*')
    symdic_shen_x42varcounterx42 = Sym('shen.*varcounter*')
    symdic_kl_numberx63 = Sym('number?')
    symdic_shen_putx47getx45macro = Sym('shen.put/get-macro')
    symdic_kl_datatype = Sym('datatype')
    symdic_kl_bind = Sym('bind')
    symdic_kl_readx45byte = Sym('read-byte')
    symdic_ContextOut_1957 = Sym('ContextOut_1957')
    symdic_kl_readx45fromx45string = Sym('read-from-string')
    symdic_shen_analysex45variablex63 = Sym('shen.analyse-variable?')
    symdic_shen_x42synonymsx42 = Sym('shen.*synonyms*')
    symdic_shen_stack = Sym('shen.stack')
    symdic_kl_synonyms = Sym('synonyms')
    symdic_shen_reverse_help = Sym('shen.reverse_help')
    symdic_kl_systemf = Sym('systemf')
    symdic_kl_writex45tox45file = Sym('write-to-file')
    symdic_Finish = Sym('Finish')
    symdic_kl_failx45if = Sym('fail-if')
    symdic_kl_fix = Sym('fix')
    symdic_shen_f_error = Sym('shen.f_error')
    symdic_kl_x60 = Sym('<')
    symdic_shen_skip = Sym('shen.skip')
    symdic_kl_unifyx33 = Sym('unify!')
    symdic_shen_pre = Sym('shen.pre')
    symdic_shen_getx45profile = Sym('shen.get-profile')
    symdic_ProcessN = Sym('ProcessN')
    symdic_L = Sym('L')
    symdic_shen_mapx45h = Sym('shen.map-h')
    symdic_Out_1957 = Sym('Out_1957')
    symdic_kl_not = Sym('not')
    symdic_kl_fwhen = Sym('fwhen')
    symdic_kl_symbolx63 = Sym('symbol?')
    symdic_shen_failedx33 = Sym('shen.failed!')
    symdic_shen_x42infsx42 = Sym('shen.*infs*')
    symdic_shen_recursivelyx45print = Sym('shen.recursively-print')
    symdic_shen_void = Sym('shen.void')
    symdic_shen_r = Sym('shen.r')
    symdic_shen_s = Sym('shen.s')
    symdic_shen_x42maxinferencesx42 = Sym('shen.*maxinferences*')
    symdic_kl_mode = Sym('mode')
    symdic_shen_a = Sym('shen.a')
    symdic_shen_f = Sym('shen.f')
    symdic_A = Sym('A')
    symdic_kl_map = Sym('map')
    symdic_shen_compressx4550 = Sym('shen.compress-50')
    symdic_shen_inputx45track = Sym('shen.input-track')
    symdic_kl_out = Sym('out')
    symdic_kl_vectorx45x62 = Sym('vector->')
    symdic_shen_application_build = Sym('shen.application_build')
    symdic_kl_stringx45x62symbol = Sym('string->symbol')
    symdic_shen_x60st_inputx62 = Sym('shen.<st_input>')
    symdic_shen_list_variables = Sym('shen.list_variables')
    symdic_kl_print = Sym('print')
    symdic_shen_procx45nl = Sym('shen.proc-nl')
    symdic_shen_dereferencing = Sym('shen.dereferencing')
    symdic_shen_compose = Sym('shen.compose')
    symdic_kl_nth = Sym('nth')
    symdic_W = Sym('W')
    symdic_kl_put = Sym('put')
    symdic_Q = Sym('Q')
    symdic_shen_recursive_descent = Sym('shen.recursive_descent')
    symdic_shen_cons_form = Sym('shen.cons_form')
    symdic_shen_datatypex45error = Sym('shen.datatype-error')
    symdic_shen_x42installingx45klx42 = Sym('shen.*installing-kl*')
    symdic_kl_length = Sym('length')
    symdic_kl_readx45filex45asx45bytelist = Sym('read-file-as-bytelist')
    symdic_shen_choicepointx33 = Sym('shen.choicepoint!')
    symdic_kl_lambda = Sym('lambda')
    symdic_shen_else = Sym('shen.else')
    symdic_kl_x62x61 = Sym('>=')
    symdic_kl_x62x62 = Sym('>>')
    symdic_kl_number = Sym('number')
    symdic_kl_readx45file = Sym('read-file')
    symdic_shen_catchpoint = Sym('shen.catchpoint')
    symdic_Start = Sym('Start')
    symdic_kl_occurrences = Sym('occurrences')
    symdic_shen_lazyderef = Sym('shen.lazyderef')
    symdic_shen_syntax = Sym('shen.syntax')
    symdic_shen_callx45rest = Sym('shen.call-rest')
    symdic_kl_open = Sym('open')
    symdic_shen_x42shenx45typex45theoryx45enabledx63x42 = Sym('shen.*shen-type-theory-enabled?*')
    symdic_shen_datatypex45macro = Sym('shen.datatype-macro')
    symdic_B = Sym('B')
    symdic_kl_thaw = Sym('thaw')
    symdic_kl_preclude = Sym('preclude')
    symdic_kl_variablex63 = Sym('variable?')
    symdic_kl_x42implementationx42 = Sym('*implementation*')
    symdic_shen_multiplex45set = Sym('shen.multiple-set')
    symdic_kl_arity = Sym('arity')
    symdic_R = Sym('R')
    symdic_kl_getx45time = Sym('get-time')
    symdic_shen_x60defprologx62 = Sym('shen.<defprolog>')
    symdic_kl_x61x61x62 = Sym('==>')
    symdic_optimise = Sym('optimise')
    symdic_shen_x60sigx43rulesx62 = Sym('shen.<sig+rules>')
    symdic_kl_untrack = Sym('untrack')
    symdic_shen_the = Sym('shen.the')
    symdic_shen_aritycheckx45action = Sym('shen.aritycheck-action')
    symdic_shen_aum_to_shen = Sym('shen.aum_to_shen')
    symdic_kl_str = Sym('str')
    symdic_kl_and = Sym('and')
    symdic_shen_demodh = Sym('shen.demodh')
    symdic_shen_synonymsx45macro = Sym('shen.synonyms-macro')
    symdic_shen_controlx45chars = Sym('shen.control-chars')
    symdic_shen_rename = Sym('shen.rename')
    symdic_shen_chwild = Sym('shen.chwild')
    symdic_shen_nlx45macro = Sym('shen.nl-macro')
    symdic_kl_null = Sym('null')
    symdic_shen_x43vectorx63 = Sym('shen.+vector?')
    symdic_shen_truncate = Sym('shen.truncate')
    symdic_kl_x45 = Sym('-')
    symdic_shen_of = Sym('shen.of')
    symdic_shen_deref = Sym('shen.deref')
    symdic_kl_destroy = Sym('destroy')
    symdic_kl_x61 = Sym('=')
    symdic_shen_outputx45track = Sym('shen.output-track')
    symdic_Qv = Sym('Qv')
    symdic_kl_track = Sym('track')
    symdic_M = Sym('M')
    symdic_kl_assoc = Sym('assoc')
    symdic_shen_hdtl = Sym('shen.hdtl')
    symdic_x42hushx42 = Sym('*hush*')
    symdic_kl_x42maximumx45printx45sequencex45sizex42 = Sym('*maximum-print-sequence-size*')
    symdic_shen_source = Sym('shen.source')
    symdic_kl_x125 = Sym('}')
    symdic_shen_find = Sym('shen.find')
    symdic_shen_encodex45choices = Sym('shen.encode-choices')
    symdic_kl_x42propertyx45vectorx42 = Sym('*property-vector*')
    symdic_shen_split_cc_rule = Sym('shen.split_cc_rule')
    symdic_kl_x42portersx42 = Sym('*porters*')
    symdic_shen_outx45ofx45bounds = Sym('shen.out-of-bounds')
    symdic_shen_semantics = Sym('shen.semantics')
    symdic_kl_macroexpand = Sym('macroexpand')
    symdic_Parse_Y = Sym('Parse_Y')
    symdic_Parse_X = Sym('Parse_X')
    symdic_shen_rightx45x62left = Sym('shen.right->left')
    symdic_shen_casex45form = Sym('shen.case-form')
    symdic_kl_x42versionx42 = Sym('*version*')
    symdic_Assumption_1957 = Sym('Assumption_1957')
    symdic_shen_callx45help = Sym('shen.call-help')
    symdic_kl_hdstr = Sym('hdstr')
    symdic_kl_do = Sym('do')
    symdic_shen_x42catchx42 = Sym('shen.*catch*')
    symdic_kl_get = Sym('get')
    symdic_kl_x61x61 = Sym('==')
    symdic_H = Sym('H')
    symdic_shen_tests = Sym('shen.tests')
    symdic_kl_x61x33 = Sym('=!')
    symdic_shen_packagex45contents = Sym('shen.package-contents')
    symdic_X = Sym('X')
    symdic_shen_insertx45predicate = Sym('shen.insert-predicate')
    symdic_shen_nonx45empty = Sym('shen.non-empty')
    symdic_kl_enablex45typex45theory = Sym('enable-type-theory')
    symdic_shen_check_stream = Sym('shen.check_stream')
    symdic_kl_remove = Sym('remove')
    symdic_kl_where = Sym('where')
    symdic_kl_set = Sym('set')
    symdic_kl_lazy = Sym('lazy')
    symdic_kl_freeze = Sym('freeze')
    symdic_shen_defmacrox45macro = Sym('shen.defmacro-macro')
    symdic_kl_fail = Sym('fail')
    symdic_kl_close = Sym('close')
    symdic_shen_evalx45withoutx45macros = Sym('shen.eval-without-macros')
    symdic_shen_insert = Sym('shen.insert')
    symdic_shen_intprologx45help = Sym('shen.intprolog-help')
    symdic_shen_externalx45symbols = Sym('shen.external-symbols')
    symdic_shen_linearise = Sym('shen.linearise')
    symdic_C = Sym('C')
    symdic_shen_outputx45macro = Sym('shen.output-macro')
    symdic_shen_functionx45macro = Sym('shen.function-macro')
    symdic_kl_barx33 = Sym('bar!')
    symdic_shen_x42alphabetx42 = Sym('shen.*alphabet*')
    symdic_shen_thisx45symbolx45isx45unbound = Sym('shen.this-symbol-is-unbound')
    symdic_kl_specialise = Sym('specialise')
    symdic_kl_protect = Sym('protect')
    symdic_shen_newpv = Sym('shen.newpv')
    symdic_kl_tlv = Sym('tlv')
    symdic_shen_reduce = Sym('shen.reduce')
    symdic_kl_errorx45tox45string = Sym('error-to-string')
    symdic_S = Sym('S')
    symdic_shen_x42stepx42 = Sym('shen.*step*')
    symdic_shen_constructx45sidex45literals = Sym('shen.construct-side-literals')
    symdic_Result = Sym('Result')
    symdic_shen_alphanumsx63 = Sym('shen.alphanums?')
    symdic_shen_insertx45prologx45variablesx45help = Sym('shen.insert-prolog-variables-help')
    symdic_shen_x42prologvectorsx42 = Sym('shen.*prologvectors*')
    symdic_shen_mult_subst = Sym('shen.mult_subst')
    symdic_kl_precludex45allx45but = Sym('preclude-all-but')
    symdic_shen_errorx45macro = Sym('shen.error-macro')
    symdic_kl_load = Sym('load')
    symdic_shen_x42processx45counterx42 = Sym('shen.*process-counter*')
    symdic_kl_cn = Sym('cn')
    symdic_kl_pos = Sym('pos')
    symdic_shen_timerx45macro = Sym('shen.timer-macro')
    symdic_kl_cd = Sym('cd')
    symdic_shen_x42trackingx42 = Sym('shen.*tracking*')
    symdic_kl_x45x45x62 = Sym('-->')
    symdic_shen_x42historyx42 = Sym('shen.*history*')
    symdic_kl_loaded = Sym('loaded')
    symdic_kl_pr = Sym('pr')
    symdic_kl_ps = Sym('ps')
    symdic_shen_mu = Sym('shen.mu')
    symdic_kl_union = Sym('union')
    symdic_shen_removex45h = Sym('shen.remove-h')
    symdic_kl_stoutput = Sym('stoutput')
    symdic_shen_x60definex62 = Sym('shen.<define>')
    symdic_kl_define = Sym('define')
    symdic_shen_terprix45orx45readx45char = Sym('shen.terpri-or-read-char')
    symdic_Time = Sym('Time')
    symdic_shen_call_the_continuation = Sym('shen.call_the_continuation')
    symdic_kl_occursx45check = Sym('occurs-check')
    symdic_N = Sym('N')
    symdic_shen_elimx45define = Sym('shen.elim-define')
    symdic_kl_external = Sym('external')
    symdic_shen_x42occursx42 = Sym('shen.*occurs*')
    symdic_shen_app = Sym('shen.app')
    symdic_x42stoutputx42 = Sym('*stoutput*')
    symdic_kl_hdv = Sym('hdv')
    symdic_kl_exception = Sym('exception')
    symdic_kl_unify = Sym('unify')
    symdic_shen_clause_form = Sym('shen.clause_form')
    symdic_shen_sx45prolog_literal = Sym('shen.s-prolog_literal')
    symdic_Continuation = Sym('Continuation')
    symdic_shen_prhush = Sym('shen.prhush')
    symdic_kl_value = Sym('value')
    symdic_kl_compile = Sym('compile')
    symdic_shen_variable = Sym('shen.variable')
    symdic_kl_error = Sym('error')
    symdic_shen_letx45macro = Sym('shen.let-macro')
    symdic_shen_x42readerx45macrosx42 = Sym('shen.*reader-macros*')
    symdic_shen_typex45signaturex45ofx45 = Sym('shen.type-signature-of-')
    symdic_shen_variablex45match = Sym('shen.variable-match')
    symdic_kl_cons = Sym('cons')
    symdic_kl_is = Sym('is')
    symdic_shen_x60sigx43restx62 = Sym('shen.<sig+rest>')
    symdic_shen_tx42 = Sym('shen.t*')
    symdic_kl_cond = Sym('cond')
    symdic_kl_in = Sym('in')
    symdic_kl_x60x45 = Sym('<-')
    symdic_shen_x42systemx42 = Sym('shen.*system*')
    symdic_kl_if = Sym('if')
    symdic_kl_verified = Sym('verified')
    symdic_shen_x42specialx42 = Sym('shen.*special*')
    symdic_kl_defun = Sym('defun')
    symdic_shen_tuple = Sym('shen.tuple')
    symdic_shen_jump_stream = Sym('shen.jump_stream')
    symdic_I = Sym('I')
    symdic_shen_sx45prolog_clause = Sym('shen.s-prolog_clause')
    symdic_readx43 = Sym('read+')
    symdic_shen_product = Sym('shen.product')
    symdic_shen_makex45stringx45macro = Sym('shen.make-string-macro')
    symdic_shen_to = Sym('shen.to')
    symdic_Y = Sym('Y')
    symdic_shen_prologx45aritycheck = Sym('shen.prolog-aritycheck')
    symdic_kl_x42languagex42 = Sym('*language*')
    symdic_kl_x47_ = Sym('/.')
    symdic_kl_macro = Sym('macro')
    symdic_shen_mkstrx45l = Sym('shen.mkstr-l')
    symdic_shen_mkstrx45r = Sym('shen.mkstr-r')
    symdic_shen_x64sx45macro = Sym('shen.@s-macro')
    symdic_shen_plugx45wildcards = Sym('shen.plug-wildcards')
    symdic_shen_ok = Sym('shen.ok')
    symdic_shen_rulex45x62hornx45clause = Sym('shen.rule->horn-clause')
    symdic_shen_newcontinuation = Sym('shen.newcontinuation')
    symdic_shen_sndx45orx45fail = Sym('shen.snd-or-fail')
    symdic_shen_compile_to_kl = Sym('shen.compile_to_kl')
    symdic_shen_be = Sym('shen.be')
    symdic_kl_defcc = Sym('defcc')
    symdic_shen_compilex45macro = Sym('shen.compile-macro')
    symdic_kl_cut = Sym('cut')
    symdic_kl_x36 = Sym('$')
    symdic_shen_variables = Sym('shen.variables')
    symdic_shen_intprolog = Sym('shen.intprolog')
    symdic_kl_identical = Sym('identical')
    symdic_kl_tcx63 = Sym('tc?')
    symdic_D = Sym('D')
    symdic_format = Sym('format')
    symdic_shen_head_abstraction = Sym('shen.head_abstraction')
    symdic_kl_maxinferences = Sym('maxinferences')
    symdic_shen_x43stringx63 = Sym('shen.+string?')
    symdic_T = Sym('T')
    symdic_shen_result = Sym('shen.result')
    symdic_shen_curry = Sym('shen.curry')
    symdic_kl_intersection = Sym('intersection')
    symdic_shen_compile_prolog_procedure = Sym('shen.compile_prolog_procedure')
    symdic_shen_x42tcx42 = Sym('shen.*tc*')
    symdic_kl_makex45string = Sym('make-string')
    symdic_kl_output = Sym('output')
    symdic_Context1_1957 = Sym('Context1_1957')
    symdic_kl_tuplex63 = Sym('tuple?')
    symdic_shen_leftx45rule = Sym('shen.left-rule')
    symdic_shen_x42optimisex42 = Sym('shen.*optimise*')
    symdic_shen_x42alldatatypesx42 = Sym('shen.*alldatatypes*')
    symdic_shen_abstraction_build = Sym('shen.abstraction_build')
    symdic_shen_x42extraspecialx42 = Sym('shen.*extraspecial*')
    symdic_shen_insertx45h = Sym('shen.insert-h')
    symdic_shen_assumetype = Sym('shen.assumetype')
    symdic_shen_x60x45sem = Sym('shen.<-sem')
    symdic_kl_explode = Sym('explode')
    symdic_shen_same_predicatex63 = Sym('shen.same_predicate?')
    symdic_shen_x42callx42 = Sym('shen.*call*')
    symdic_kl_x47 = Sym('/')
    symdic_kl_defprolog = Sym('defprolog')
    symdic_Throwcontrol = Sym('Throwcontrol')
    symdic_kl_run = Sym('run')
    symdic_Parse_ = Sym('Parse_')
    symdic_O = Sym('O')
    symdic_shen_bindv = Sym('shen.bindv')
    symdic_kl_step = Sym('step')
    symdic_shen_typecheckx45andx45load = Sym('shen.typecheck-and-load')
    symdic_kl__ = Sym('_')
    symdic_kl_x42portx42 = Sym('*port*')
    symdic_shen_cslx45help = Sym('shen.csl-help')
    symdic_shen_intprologx45helpx45help = Sym('shen.intprolog-help-help')
    symdic_kl_package = Sym('package')
    symdic_shen_double = Sym('shen.double')
    symdic_shen_default_semantics = Sym('shen.default_semantics')
    symdic_kl_unprofile = Sym('unprofile')
    symdic_shen_x60datatypex45rulesx62 = Sym('shen.<datatype-rules>')
    symdic_Message = Sym('Message')
    symdic_shen_trackx45function = Sym('shen.track-function')
    symdic_kl_or = Sym('or')
    symdic_shen_walk = Sym('shen.walk')
    symdic_shen_first_n = Sym('shen.first_n')
    symdic_In_1957 = Sym('In_1957')
    symdic_shen_putx45profile = Sym('shen.put-profile')
    symdic_shen_constructx45searchx45clauses = Sym('shen.construct-search-clauses')
    symdic_shen_abstract_rule = Sym('shen.abstract_rule')
    symdic_kl_boundx63 = Sym('bound?')
    symdic_kl_unspecialise = Sym('unspecialise')
    symdic_kl_x42 = Sym('*')
    symdic_Context_1957 = Sym('Context_1957')
    symdic_shen_sum = Sym('shen.sum')
    symdic_kl_x58 = Sym(':')
    symdic_kl_function = Sym('function')
    symdic_shen_analysex45symbolx63 = Sym('shen.analyse-symbol?')
    symdic_kl_head = Sym('head')
    symdic_J = Sym('J')
    symdic_kl_defmacro = Sym('defmacro')
    symdic_shen_pop = Sym('shen.pop')
    symdic_Z = Sym('Z')
    symdic_kl_hd = Sym('hd')
    symdic_shen_modh = Sym('shen.modh')
    symdic_kl_limit = Sym('limit')
    symdic_shen_stripx45protect = Sym('shen.strip-protect')
    symdic_kl_x62 = Sym('>')
    symdic_shen_nestx45disjunct = Sym('shen.nest-disjunct')
    symdic_shen_procedure_name = Sym('shen.procedure_name')
    symdic_shen_pair = Sym('shen.pair')
    symdic_shen_cutpoint = Sym('shen.cutpoint')
    symdic_Assumptions_1957 = Sym('Assumptions_1957')
    symdic_shen_x42teststackx42 = Sym('shen.*teststack*')
    symdic_shen_insertx45l = Sym('shen.insert-l')
    symdic_kl_x60ex62 = Sym('<e>')
    symdic_kl_elementx63 = Sym('element?')
    symdic_kl_stringx45x62n = Sym('string->n')
    symdic_shen_constructx45context = Sym('shen.construct-context')
    symdic_kl_file = Sym('file')
    symdic_shen_leavex33 = Sym('shen.leave!')
    symdic_shen_afterx45codepoint = Sym('shen.after-codepoint')
    symdic_shen_linearisex45clause = Sym('shen.linearise-clause')
    symdic_kl_nl = Sym('nl')
    symdic_shen_changex45pointerx45value = Sym('shen.change-pointer-value')
    symdic_shen_stripx45pathname = Sym('shen.strip-pathname')
    symdic_kl_when = Sym('when')
    symdic_kl_stringx63 = Sym('string?')
    symdic_kl_absvectorx63 = Sym('absvector?')
    symdic_shen_x42maxcomplexityx42 = Sym('shen.*maxcomplexity*')
    symdic_shen_rememberx45datatype = Sym('shen.remember-datatype')
    symdic_shen_defprologx45macro = Sym('shen.defprolog-macro')
    symdic_Case = Sym('Case')
    symdic_kl_yx45orx45nx63 = Sym('y-or-n?')
    symdic_x60x33x62 = Sym('<!>')
    symdic_E = Sym('E')
    symdic_shen_continuation = Sym('shen.continuation')
    symdic_kl_symbol = Sym('symbol')
    symdic_kl_profilex45results = Sym('profile-results')
    symdic_U = Sym('U')
    symdic_Context = Sym('Context')
    symdic_shen_multiples = Sym('shen.multiples')
    symdic_kl_fst = Sym('fst')
    symdic_kl_time = Sym('time')
symdic = SymDic()
FUNCTIONS.update({'or': shen_or, 'and': shen_and})
VARS.update({'*language*': 'Python', '*implementation*': 'pyshen', '*release*': '', '*port*': '0.135', '*porters*': 'Matthieu Lagacherie and Yannick Drant', '*home-directory*': '~/', '*stinput*': sys.stdin, '*stoutput*': sys.stdout, '*version*': 'version 11'})


#============================== toplevel.kl==============================



@tail_recursion
def shen_shen(*FUN_ARGS):
    FUN_ARITY = 0
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_shen, (FUN_ARGS + lambdaargs)))
    global symdic
    return [tco_apply(shen_credits, []), tail_call(shen_loop, [])][(-1)]
shen_add_fun('shen.shen', shen_shen, 0)

@tail_recursion
def shen_loop(*FUN_ARGS):
    FUN_ARITY = 0
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_loop, (FUN_ARGS + lambdaargs)))
    global symdic
    return [tco_apply(shen_initialise_environment, []), [tco_apply(shen_prompt, []), [shen_try_except((lambda : tco_apply(shen_readx45evaluatex45print, [])), (lambda KL_ARG_E_0: shen_pr(KL_ARG_E_0.message, tco_apply(kl_stoutput, [])))), tail_call(shen_loop, [])][(-1)]][(-1)]][(-1)]
shen_add_fun('shen.loop', shen_loop, 0)

@tail_recursion
def kl_version(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_version, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2308_1 = FUN_ARGS[0]
    global symdic
    return shen_set(symdic.symdic_kl_x42versionx42, KL_ARG_V2308_1)
shen_add_fun('version', kl_version, 1)
tail_call(kl_version, ['version 11'])

@tail_recursion
def shen_credits(*FUN_ARGS):
    FUN_ARITY = 0
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_credits, (FUN_ARGS + lambdaargs)))
    global symdic
    return [tco_apply(shen_prhush, ['\r\nShen 2010, copyright (C) 2010 Mark Tarver\r\n', tco_apply(kl_stoutput, [])]), [tco_apply(shen_prhush, ['released under the Shen license\r\n', tco_apply(kl_stoutput, [])]), [tco_apply(shen_prhush, [('www.shenlanguage.org, ' + tco_apply(shen_app, [shen_get(symdic.symdic_kl_x42versionx42), '\r\n', symdic.symdic_shen_a])), tco_apply(kl_stoutput, [])]), [tco_apply(shen_prhush, [('running under ' + tco_apply(shen_app, [shen_get(symdic.symdic_kl_x42languagex42), (', implementation: ' + tco_apply(shen_app, [shen_get(symdic.symdic_kl_x42implementationx42), '', symdic.symdic_shen_a])), symdic.symdic_shen_a])), tco_apply(kl_stoutput, [])]), tail_call(shen_prhush, [('\r\nport ' + tco_apply(shen_app, [shen_get(symdic.symdic_kl_x42portx42), (' ported by ' + tco_apply(shen_app, [shen_get(symdic.symdic_kl_x42portersx42), '\r\n', symdic.symdic_shen_a])), symdic.symdic_shen_a])), tco_apply(kl_stoutput, [])])][(-1)]][(-1)]][(-1)]][(-1)]
shen_add_fun('shen.credits', shen_credits, 0)

@tail_recursion
def shen_initialise_environment(*FUN_ARGS):
    FUN_ARITY = 0
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_initialise_environment, (FUN_ARGS + lambdaargs)))
    global symdic
    return tail_call(shen_multiplex45set, [Cons(symdic.symdic_shen_x42callx42, Cons(0, Cons(symdic.symdic_shen_x42infsx42, Cons(0, Cons(symdic.symdic_shen_x42processx45counterx42, Cons(0, Cons(symdic.symdic_shen_x42catchx42, Cons(0, nil))))))))])
shen_add_fun('shen.initialise_environment', shen_initialise_environment, 0)

@tail_recursion
def shen_multiplex45set(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_multiplex45set, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2309_2 = FUN_ARGS[0]
    global symdic
    return (nil if shen_eq(nil, KL_ARG_V2309_2) else ([shen_set(car(KL_ARG_V2309_2), car(cdr(KL_ARG_V2309_2))), tail_call(shen_multiplex45set, [cdr(cdr(KL_ARG_V2309_2))])][(-1)] if (shen_consp(cdr(KL_ARG_V2309_2)) if shen_consp(KL_ARG_V2309_2) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_multiplex45set]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.multiple-set', shen_multiplex45set, 1)

@tail_recursion
def kl_destroy(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_destroy, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2310_3 = FUN_ARGS[0]
    global symdic
    return apply(kl_declare, [KL_ARG_V2310_3, nil])
shen_add_fun('destroy', kl_destroy, 1)
shen_set(symdic.symdic_shen_x42historyx42, nil)

@tail_recursion
def shen_readx45evaluatex45print(*FUN_ARGS):
    FUN_ARITY = 0
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_readx45evaluatex45print, (FUN_ARGS + lambdaargs)))

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
def shen_retrievex45fromx45historyx45ifx45needed(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_retrievex45fromx45historyx45ifx45needed, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2320_9 = FUN_ARGS[0]
    KL_ARG_V2321_10 = FUN_ARGS[1]

    class KL_Context:
        KL_LOC_PastPrint_11 = None
        KL_LOC_Keyx63_12 = None
        KL_LOC_Find_13 = None
        KL_LOC_PastPrint_14 = None
        KL_LOC_Keyx63_16 = None
        KL_LOC_Pastprint_17 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_PastPrint_11', tco_apply(shen_prbytes, [tco_apply(kl_snd, [car(KL_ARG_V2321_10)])])), car(KL_ARG_V2321_10)][(-1)] if ((((((shen_eq(car(cdr(tco_apply(kl_snd, [KL_ARG_V2320_9]))), tco_apply(shen_exclamation, [])) if shen_eq(car(tco_apply(kl_snd, [KL_ARG_V2320_9])), tco_apply(shen_exclamation, [])) else False) if shen_consp(KL_ARG_V2321_10) else False) if shen_eq(nil, cdr(cdr(tco_apply(kl_snd, [KL_ARG_V2320_9])))) else False) if shen_consp(cdr(tco_apply(kl_snd, [KL_ARG_V2320_9]))) else False) if shen_consp(tco_apply(kl_snd, [KL_ARG_V2320_9])) else False) if tco_apply(kl_tuplex63, [KL_ARG_V2320_9]) else False) else ([setattr(KL_CTX, 'KL_LOC_Keyx63_12', tco_apply(shen_makex45key, [cdr(tco_apply(kl_snd, [KL_ARG_V2320_9])), KL_ARG_V2321_10])), [setattr(KL_CTX, 'KL_LOC_Find_13', tco_apply(kl_head, [tco_apply(shen_findx45pastx45inputs, [KL_CTX.KL_LOC_Keyx63_12, KL_ARG_V2321_10])])), [setattr(KL_CTX, 'KL_LOC_PastPrint_14', tco_apply(shen_prbytes, [tco_apply(kl_snd, [KL_CTX.KL_LOC_Find_13])])), KL_CTX.KL_LOC_Find_13][(-1)]][(-1)]][(-1)] if ((shen_eq(car(tco_apply(kl_snd, [KL_ARG_V2320_9])), tco_apply(shen_exclamation, [])) if shen_consp(tco_apply(kl_snd, [KL_ARG_V2320_9])) else False) if tco_apply(kl_tuplex63, [KL_ARG_V2320_9]) else False) else ([tco_apply(shen_printx45pastx45inputs, [(lambda KL_ARG_X_15: True), tco_apply(kl_reverse, [KL_ARG_V2321_10]), 0]), tail_call(kl_abort, [])][(-1)] if (((shen_eq(car(tco_apply(kl_snd, [KL_ARG_V2320_9])), tco_apply(shen_percent, [])) if shen_eq(nil, cdr(tco_apply(kl_snd, [KL_ARG_V2320_9]))) else False) if shen_consp(tco_apply(kl_snd, [KL_ARG_V2320_9])) else False) if tco_apply(kl_tuplex63, [KL_ARG_V2320_9]) else False) else ([setattr(KL_CTX, 'KL_LOC_Keyx63_16', tco_apply(shen_makex45key, [cdr(tco_apply(kl_snd, [KL_ARG_V2320_9])), KL_ARG_V2321_10])), [setattr(KL_CTX, 'KL_LOC_Pastprint_17', tco_apply(shen_printx45pastx45inputs, [KL_CTX.KL_LOC_Keyx63_16, tco_apply(kl_reverse, [KL_ARG_V2321_10]), 0])), tail_call(kl_abort, [])][(-1)]][(-1)] if ((shen_eq(car(tco_apply(kl_snd, [KL_ARG_V2320_9])), tco_apply(shen_percent, [])) if shen_consp(tco_apply(kl_snd, [KL_ARG_V2320_9])) else False) if tco_apply(kl_tuplex63, [KL_ARG_V2320_9]) else False) else (KL_ARG_V2320_9 if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.retrieve-from-history-if-needed', shen_retrievex45fromx45historyx45ifx45needed, 2)

@tail_recursion
def shen_percent(*FUN_ARGS):
    FUN_ARITY = 0
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_percent, (FUN_ARGS + lambdaargs)))
    global symdic
    return 37
shen_add_fun('shen.percent', shen_percent, 0)

@tail_recursion
def shen_exclamation(*FUN_ARGS):
    FUN_ARITY = 0
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_exclamation, (FUN_ARGS + lambdaargs)))
    global symdic
    return 33
shen_add_fun('shen.exclamation', shen_exclamation, 0)

@tail_recursion
def shen_prbytes(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_prbytes, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2322_18 = FUN_ARGS[0]
    global symdic
    return [tco_apply(kl_map, [(lambda KL_ARG_Byte_19: shen_pr(chr(KL_ARG_Byte_19), tco_apply(kl_stoutput, []))), KL_ARG_V2322_18]), tail_call(kl_nl, [1])][(-1)]
shen_add_fun('shen.prbytes', shen_prbytes, 1)

@tail_recursion
def shen_update_history(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_update_history, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2323_20 = FUN_ARGS[0]
    KL_ARG_V2324_21 = FUN_ARGS[1]
    global symdic
    return shen_set(symdic.symdic_shen_x42historyx42, Cons(KL_ARG_V2323_20, KL_ARG_V2324_21))
shen_add_fun('shen.update_history', shen_update_history, 2)

@tail_recursion
def shen_toplineread(*FUN_ARGS):
    FUN_ARITY = 0
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_toplineread, (FUN_ARGS + lambdaargs)))
    global symdic
    return tail_call(shen_toplineread_loop, [shen_read_byte(tco_apply(kl_stinput, [])), nil])
shen_add_fun('shen.toplineread', shen_toplineread, 0)

@tail_recursion
def shen_toplineread_loop(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_toplineread_loop, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2326_22 = FUN_ARGS[0]
    KL_ARG_V2327_23 = FUN_ARGS[1]

    class KL_Context:
        KL_LOC_Line_24 = None
    KL_CTX = KL_Context()
    global symdic
    return (shen_simple_error('line read aborted') if shen_eq(KL_ARG_V2326_22, tco_apply(shen_hat, [])) else ([setattr(KL_CTX, 'KL_LOC_Line_24', tco_apply(kl_compile, [symdic.symdic_shen_x60st_inputx62, KL_ARG_V2327_23, (lambda KL_ARG_E_25: symdic.symdic_shen_nextline)])), (tail_call(shen_toplineread_loop, [shen_read_byte(tco_apply(kl_stinput, [])), tco_apply(kl_append, [KL_ARG_V2327_23, Cons(KL_ARG_V2326_22, nil)])]) if (True if shen_eq(KL_CTX.KL_LOC_Line_24, symdic.symdic_shen_nextline) else tco_apply(kl_emptyx63, [KL_CTX.KL_LOC_Line_24])) else tail_call(kl_x64p, [KL_CTX.KL_LOC_Line_24, KL_ARG_V2327_23]))][(-1)] if tco_apply(kl_elementx63, [KL_ARG_V2326_22, Cons(tco_apply(shen_newline, []), Cons(tco_apply(shen_carriagex45return, []), nil))]) else (tail_call(shen_toplineread_loop, [shen_read_byte(tco_apply(kl_stinput, [])), tco_apply(kl_append, [KL_ARG_V2327_23, Cons(KL_ARG_V2326_22, nil)])]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.toplineread_loop', shen_toplineread_loop, 2)

@tail_recursion
def shen_hat(*FUN_ARGS):
    FUN_ARITY = 0
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_hat, (FUN_ARGS + lambdaargs)))
    global symdic
    return 94
shen_add_fun('shen.hat', shen_hat, 0)

@tail_recursion
def shen_newline(*FUN_ARGS):
    FUN_ARITY = 0
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_newline, (FUN_ARGS + lambdaargs)))
    global symdic
    return 10
shen_add_fun('shen.newline', shen_newline, 0)

@tail_recursion
def shen_carriagex45return(*FUN_ARGS):
    FUN_ARITY = 0
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_carriagex45return, (FUN_ARGS + lambdaargs)))
    global symdic
    return 13
shen_add_fun('shen.carriage-return', shen_carriagex45return, 0)

@tail_recursion
def kl_tc(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_tc, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2332_26 = FUN_ARGS[0]
    global symdic
    return (shen_set(symdic.symdic_shen_x42tcx42, True) if shen_eq(symdic.symdic_kl_x43, KL_ARG_V2332_26) else (shen_set(symdic.symdic_shen_x42tcx42, False) if shen_eq(symdic.symdic_kl_x45, KL_ARG_V2332_26) else (shen_simple_error('tc expects a + or -') if True else shen_simple_error('condition failure'))))
shen_add_fun('tc', kl_tc, 1)

@tail_recursion
def shen_prompt(*FUN_ARGS):
    FUN_ARITY = 0
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_prompt, (FUN_ARGS + lambdaargs)))
    global symdic
    return (tail_call(shen_prhush, [('\r\n\r\n(' + tco_apply(shen_app, [tco_apply(kl_length, [shen_get(symdic.symdic_shen_x42historyx42)]), '+) ', symdic.symdic_shen_a])), tco_apply(kl_stoutput, [])]) if shen_get(symdic.symdic_shen_x42tcx42) else tail_call(shen_prhush, [('\r\n\r\n(' + tco_apply(shen_app, [tco_apply(kl_length, [shen_get(symdic.symdic_shen_x42historyx42)]), '-) ', symdic.symdic_shen_a])), tco_apply(kl_stoutput, [])]))
shen_add_fun('shen.prompt', shen_prompt, 0)

@tail_recursion
def shen_toplevel(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_toplevel, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2333_27 = FUN_ARGS[0]
    global symdic
    return tail_call(shen_toplevel_evaluate, [KL_ARG_V2333_27, shen_get(symdic.symdic_shen_x42tcx42)])
shen_add_fun('shen.toplevel', shen_toplevel, 1)

@tail_recursion
def shen_findx45pastx45inputs(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_findx45pastx45inputs, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2334_28 = FUN_ARGS[0]
    KL_ARG_V2335_29 = FUN_ARGS[1]

    class KL_Context:
        KL_LOC_F_30 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_F_30', tco_apply(shen_find, [KL_ARG_V2334_28, KL_ARG_V2335_29])), (shen_simple_error('input not found\r\n') if tco_apply(kl_emptyx63, [KL_CTX.KL_LOC_F_30]) else KL_CTX.KL_LOC_F_30)][(-1)]
shen_add_fun('shen.find-past-inputs', shen_findx45pastx45inputs, 2)

@tail_recursion
def shen_makex45key(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_makex45key, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2336_31 = FUN_ARGS[0]
    KL_ARG_V2337_32 = FUN_ARGS[1]

    class KL_Context:
        KL_LOC_Atom_33 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Atom_33', car(tco_apply(kl_compile, [symdic.symdic_shen_x60st_inputx62, KL_ARG_V2336_31, (lambda KL_ARG_E_34: (shen_simple_error(('parse error here: ' + tco_apply(shen_app, [KL_ARG_E_34, '\r\n', symdic.symdic_shen_s]))) if shen_consp(KL_ARG_E_34) else shen_simple_error('parse error\r\n')))]))), ((lambda KL_ARG_X_35: shen_eq(KL_ARG_X_35, tco_apply(kl_nth, [(KL_CTX.KL_LOC_Atom_33 + 1), tco_apply(kl_reverse, [KL_ARG_V2337_32])]))) if tco_apply(kl_integerx63, [KL_CTX.KL_LOC_Atom_33]) else (lambda KL_ARG_X_36: tail_call(shen_prefixx63, [KL_ARG_V2336_31, tco_apply(shen_trimx45gubbins, [tco_apply(kl_snd, [KL_ARG_X_36])])])))][(-1)]
shen_add_fun('shen.make-key', shen_makex45key, 2)

@tail_recursion
def shen_trimx45gubbins(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_trimx45gubbins, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2338_37 = FUN_ARGS[0]
    global symdic
    return (tail_call(shen_trimx45gubbins, [cdr(KL_ARG_V2338_37)]) if (shen_eq(car(KL_ARG_V2338_37), tco_apply(shen_space, [])) if shen_consp(KL_ARG_V2338_37) else False) else (tail_call(shen_trimx45gubbins, [cdr(KL_ARG_V2338_37)]) if (shen_eq(car(KL_ARG_V2338_37), tco_apply(shen_newline, [])) if shen_consp(KL_ARG_V2338_37) else False) else (tail_call(shen_trimx45gubbins, [cdr(KL_ARG_V2338_37)]) if (shen_eq(car(KL_ARG_V2338_37), tco_apply(shen_carriagex45return, [])) if shen_consp(KL_ARG_V2338_37) else False) else (tail_call(shen_trimx45gubbins, [cdr(KL_ARG_V2338_37)]) if (shen_eq(car(KL_ARG_V2338_37), tco_apply(shen_tab, [])) if shen_consp(KL_ARG_V2338_37) else False) else (tail_call(shen_trimx45gubbins, [cdr(KL_ARG_V2338_37)]) if (shen_eq(car(KL_ARG_V2338_37), tco_apply(shen_leftx45round, [])) if shen_consp(KL_ARG_V2338_37) else False) else (KL_ARG_V2338_37 if True else shen_simple_error('condition failure')))))))
shen_add_fun('shen.trim-gubbins', shen_trimx45gubbins, 1)

@tail_recursion
def shen_space(*FUN_ARGS):
    FUN_ARITY = 0
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_space, (FUN_ARGS + lambdaargs)))
    global symdic
    return 32
shen_add_fun('shen.space', shen_space, 0)

@tail_recursion
def shen_tab(*FUN_ARGS):
    FUN_ARITY = 0
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_tab, (FUN_ARGS + lambdaargs)))
    global symdic
    return 9
shen_add_fun('shen.tab', shen_tab, 0)

@tail_recursion
def shen_leftx45round(*FUN_ARGS):
    FUN_ARITY = 0
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_leftx45round, (FUN_ARGS + lambdaargs)))
    global symdic
    return 40
shen_add_fun('shen.left-round', shen_leftx45round, 0)

@tail_recursion
def shen_find(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_find, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2345_38 = FUN_ARGS[0]
    KL_ARG_V2346_39 = FUN_ARGS[1]
    global symdic
    return (nil if shen_eq(nil, KL_ARG_V2346_39) else (Cons(car(KL_ARG_V2346_39), tco_apply(shen_find, [KL_ARG_V2345_38, cdr(KL_ARG_V2346_39)])) if (shen_apply(KL_ARG_V2345_38, [car(KL_ARG_V2346_39)]) if shen_consp(KL_ARG_V2346_39) else False) else (tail_call(shen_find, [KL_ARG_V2345_38, cdr(KL_ARG_V2346_39)]) if shen_consp(KL_ARG_V2346_39) else (tail_call(shen_sysx45error, [symdic.symdic_shen_find]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.find', shen_find, 2)

@tail_recursion
def shen_prefixx63(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_prefixx63, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2357_40 = FUN_ARGS[0]
    KL_ARG_V2358_41 = FUN_ARGS[1]
    global symdic
    return (True if shen_eq(nil, KL_ARG_V2357_40) else (tail_call(shen_prefixx63, [cdr(KL_ARG_V2357_40), cdr(KL_ARG_V2358_41)]) if ((shen_eq(car(KL_ARG_V2358_41), car(KL_ARG_V2357_40)) if shen_consp(KL_ARG_V2358_41) else False) if shen_consp(KL_ARG_V2357_40) else False) else (False if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.prefix?', shen_prefixx63, 2)

@tail_recursion
def shen_printx45pastx45inputs(*FUN_ARGS):
    FUN_ARITY = 3
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_printx45pastx45inputs, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2368_42 = FUN_ARGS[0]
    KL_ARG_V2369_43 = FUN_ARGS[1]
    KL_ARG_V2370_44 = FUN_ARGS[2]
    global symdic
    return (symdic.symdic_kl__ if shen_eq(nil, KL_ARG_V2369_43) else (tail_call(shen_printx45pastx45inputs, [KL_ARG_V2368_42, cdr(KL_ARG_V2369_43), (KL_ARG_V2370_44 + 1)]) if ((not shen_apply(KL_ARG_V2368_42, [car(KL_ARG_V2369_43)])) if shen_consp(KL_ARG_V2369_43) else False) else ([tco_apply(shen_prhush, [tco_apply(shen_app, [KL_ARG_V2370_44, '. ', symdic.symdic_shen_a]), tco_apply(kl_stoutput, [])]), [tco_apply(shen_prbytes, [tco_apply(kl_snd, [car(KL_ARG_V2369_43)])]), tail_call(shen_printx45pastx45inputs, [KL_ARG_V2368_42, cdr(KL_ARG_V2369_43), (KL_ARG_V2370_44 + 1)])][(-1)]][(-1)] if (tco_apply(kl_tuplex63, [car(KL_ARG_V2369_43)]) if shen_consp(KL_ARG_V2369_43) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_printx45pastx45inputs]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.print-past-inputs', shen_printx45pastx45inputs, 3)

@tail_recursion
def shen_toplevel_evaluate(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_toplevel_evaluate, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2371_45 = FUN_ARGS[0]
    KL_ARG_V2372_46 = FUN_ARGS[1]

    class KL_Context:
        KL_LOC_Eval_47 = None
    KL_CTX = KL_Context()
    global symdic
    return (tail_call(shen_typecheckx45andx45evaluate, [car(KL_ARG_V2371_45), car(cdr(cdr(KL_ARG_V2371_45)))]) if (((((shen_eq(True, KL_ARG_V2372_46) if shen_eq(nil, cdr(cdr(cdr(KL_ARG_V2371_45)))) else False) if shen_consp(cdr(cdr(KL_ARG_V2371_45))) else False) if shen_eq(symdic.symdic_kl_x58, car(cdr(KL_ARG_V2371_45))) else False) if shen_consp(cdr(KL_ARG_V2371_45)) else False) if shen_consp(KL_ARG_V2371_45) else False) else ([tco_apply(shen_toplevel_evaluate, [Cons(car(KL_ARG_V2371_45), nil), KL_ARG_V2372_46]), [tco_apply(kl_nl, [1]), tail_call(shen_toplevel_evaluate, [cdr(KL_ARG_V2371_45), KL_ARG_V2372_46])][(-1)]][(-1)] if (shen_consp(cdr(KL_ARG_V2371_45)) if shen_consp(KL_ARG_V2371_45) else False) else (tail_call(shen_typecheckx45andx45evaluate, [car(KL_ARG_V2371_45), tco_apply(kl_gensym, [symdic.symdic_A])]) if ((shen_eq(True, KL_ARG_V2372_46) if shen_eq(nil, cdr(KL_ARG_V2371_45)) else False) if shen_consp(KL_ARG_V2371_45) else False) else ([setattr(KL_CTX, 'KL_LOC_Eval_47', tco_apply(shen_evalx45withoutx45macros, [car(KL_ARG_V2371_45)])), tail_call(kl_print, [KL_CTX.KL_LOC_Eval_47])][(-1)] if ((shen_eq(False, KL_ARG_V2372_46) if shen_eq(nil, cdr(KL_ARG_V2371_45)) else False) if shen_consp(KL_ARG_V2371_45) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_toplevel_evaluate]) if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.toplevel_evaluate', shen_toplevel_evaluate, 2)

@tail_recursion
def shen_typecheckx45andx45evaluate(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_typecheckx45andx45evaluate, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2373_48 = FUN_ARGS[0]
    KL_ARG_V2374_49 = FUN_ARGS[1]

    class KL_Context:
        KL_LOC_Typecheck_50 = None
        KL_LOC_Eval_51 = None
        KL_LOC_Type_52 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Typecheck_50', tco_apply(shen_typecheck, [KL_ARG_V2373_48, KL_ARG_V2374_49])), (shen_simple_error('type error\r\n') if shen_eq(KL_CTX.KL_LOC_Typecheck_50, False) else [setattr(KL_CTX, 'KL_LOC_Eval_51', tco_apply(shen_evalx45withoutx45macros, [KL_ARG_V2373_48])), [setattr(KL_CTX, 'KL_LOC_Type_52', tco_apply(shen_prettyx45type, [KL_CTX.KL_LOC_Typecheck_50])), tail_call(shen_prhush, [tco_apply(shen_app, [KL_CTX.KL_LOC_Eval_51, (' : ' + tco_apply(shen_app, [KL_CTX.KL_LOC_Type_52, '', symdic.symdic_shen_r])), symdic.symdic_shen_s]), tco_apply(kl_stoutput, [])])][(-1)]][(-1)])][(-1)]
shen_add_fun('shen.typecheck-and-evaluate', shen_typecheckx45andx45evaluate, 2)

@tail_recursion
def shen_prettyx45type(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_prettyx45type, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2375_53 = FUN_ARGS[0]
    global symdic
    return tail_call(shen_mult_subst, [shen_get(symdic.symdic_shen_x42alphabetx42), tco_apply(shen_extractx45pvars, [KL_ARG_V2375_53]), KL_ARG_V2375_53])
shen_add_fun('shen.pretty-type', shen_prettyx45type, 1)

@tail_recursion
def shen_extractx45pvars(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_extractx45pvars, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2380_54 = FUN_ARGS[0]
    global symdic
    return (Cons(KL_ARG_V2380_54, nil) if tco_apply(shen_pvarx63, [KL_ARG_V2380_54]) else (tail_call(kl_union, [tco_apply(shen_extractx45pvars, [car(KL_ARG_V2380_54)]), tco_apply(shen_extractx45pvars, [cdr(KL_ARG_V2380_54)])]) if shen_consp(KL_ARG_V2380_54) else (nil if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.extract-pvars', shen_extractx45pvars, 1)

@tail_recursion
def shen_mult_subst(*FUN_ARGS):
    FUN_ARITY = 3
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_mult_subst, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2385_55 = FUN_ARGS[0]
    KL_ARG_V2386_56 = FUN_ARGS[1]
    KL_ARG_V2387_57 = FUN_ARGS[2]
    global symdic
    return (KL_ARG_V2387_57 if shen_eq(nil, KL_ARG_V2385_55) else (KL_ARG_V2387_57 if shen_eq(nil, KL_ARG_V2386_56) else (tail_call(shen_mult_subst, [cdr(KL_ARG_V2385_55), cdr(KL_ARG_V2386_56), tco_apply(kl_subst, [car(KL_ARG_V2385_55), car(KL_ARG_V2386_56), KL_ARG_V2387_57])]) if (shen_consp(KL_ARG_V2386_56) if shen_consp(KL_ARG_V2385_55) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_mult_subst]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.mult_subst', shen_mult_subst, 3)


#============================== core.kl==============================



@tail_recursion
def shen_shenx45x62kl(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_shenx45x62kl, (FUN_ARGS + lambdaargs)))
    KL_ARG_V607_58 = FUN_ARGS[0]
    KL_ARG_V608_59 = FUN_ARGS[1]
    global symdic
    return tail_call(kl_compile, [symdic.symdic_shen_x60definex62, Cons(KL_ARG_V607_58, KL_ARG_V608_59), (lambda KL_ARG_X_60: tail_call(shen_shenx45syntaxx45error, [KL_ARG_V607_58, KL_ARG_X_60]))])
shen_add_fun('shen.shen->kl', shen_shenx45x62kl, 2)

@tail_recursion
def shen_shenx45syntaxx45error(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_shenx45syntaxx45error, (FUN_ARGS + lambdaargs)))
    KL_ARG_V609_61 = FUN_ARGS[0]
    KL_ARG_V610_62 = FUN_ARGS[1]
    global symdic
    return shen_simple_error(('syntax error in ' + tco_apply(shen_app, [KL_ARG_V609_61, (' here:\r\n\r\n ' + tco_apply(shen_app, [tco_apply(shen_nextx4550, [50, KL_ARG_V610_62]), '\r\n', symdic.symdic_shen_a])), symdic.symdic_shen_a])))
shen_add_fun('shen.shen-syntax-error', shen_shenx45syntaxx45error, 2)

@tail_recursion
def shen_x60definex62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60definex62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V615_63 = FUN_ARGS[0]

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
    return [setattr(KL_CTX, 'KL_LOC_Result_64', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60namex62_65', tco_apply(shen_x60namex62, [KL_ARG_V615_63])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60signaturex62_66', tco_apply(shen_x60signaturex62, [KL_CTX.KL_LOC_Parse_shen_x60namex62_65])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60rulesx62_67', tco_apply(shen_x60rulesx62, [KL_CTX.KL_LOC_Parse_shen_x60signaturex62_66])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60rulesx62_67), tco_apply(shen_compile_to_machine_code, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60namex62_65]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60rulesx62_67])])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60rulesx62_67)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60signaturex62_66)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60namex62_65)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_68', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60namex62_69', tco_apply(shen_x60namex62, [KL_ARG_V615_63])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60rulesx62_70', tco_apply(shen_x60rulesx62, [KL_CTX.KL_LOC_Parse_shen_x60namex62_69])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60rulesx62_70), tco_apply(shen_compile_to_machine_code, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60namex62_69]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60rulesx62_70])])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60rulesx62_70)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60namex62_69)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_68, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_68)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_64, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_64)][(-1)]
shen_add_fun('shen.<define>', shen_x60definex62, 1)

@tail_recursion
def shen_x60namex62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60namex62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V620_71 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_72 = None
        KL_LOC_Parse_X_73 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_72', ([setattr(KL_CTX, 'KL_LOC_Parse_X_73', car(car(KL_ARG_V620_71))), tco_apply(shen_pair, [car(tco_apply(shen_pair, [cdr(car(KL_ARG_V620_71)), tco_apply(shen_hdtl, [KL_ARG_V620_71])])), (KL_CTX.KL_LOC_Parse_X_73 if ((not tco_apply(shen_sysfuncx63, [KL_CTX.KL_LOC_Parse_X_73])) if tco_apply(kl_symbolx63, [KL_CTX.KL_LOC_Parse_X_73]) else False) else shen_simple_error(tco_apply(shen_app, [KL_CTX.KL_LOC_Parse_X_73, ' is not a legitimate function name.\r\n', symdic.symdic_shen_a])))])][(-1)] if shen_consp(car(KL_ARG_V620_71)) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_72, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_72)][(-1)]
shen_add_fun('shen.<name>', shen_x60namex62, 1)

@tail_recursion
def shen_sysfuncx63(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_sysfuncx63, (FUN_ARGS + lambdaargs)))
    KL_ARG_V621_74 = FUN_ARGS[0]
    global symdic
    return tail_call(kl_elementx63, [KL_ARG_V621_74, tco_apply(kl_get, [shen_intern('shen'), symdic.symdic_shen_externalx45symbols, shen_get(symdic.symdic_kl_x42propertyx45vectorx42)])])
shen_add_fun('shen.sysfunc?', shen_sysfuncx63, 1)

@tail_recursion
def shen_x60signaturex62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60signaturex62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V626_75 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_76 = None
        KL_LOC_Parse_shen_x60signaturex45helpx62_77 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_76', ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60signaturex45helpx62_77', tco_apply(shen_x60signaturex45helpx62, [tco_apply(shen_pair, [cdr(car(KL_ARG_V626_75)), tco_apply(shen_hdtl, [KL_ARG_V626_75])])])), ((tco_apply(shen_pair, [car(tco_apply(shen_pair, [cdr(car(KL_CTX.KL_LOC_Parse_shen_x60signaturex45helpx62_77)), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60signaturex45helpx62_77])])), tco_apply(shen_demodulate, [tco_apply(shen_curryx45type, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60signaturex45helpx62_77])])])]) if (shen_eq(symdic.symdic_kl_x125, car(car(KL_CTX.KL_LOC_Parse_shen_x60signaturex45helpx62_77))) if shen_consp(car(KL_CTX.KL_LOC_Parse_shen_x60signaturex45helpx62_77)) else False) else tco_apply(kl_fail, [])) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60signaturex45helpx62_77)) else tco_apply(kl_fail, []))][(-1)] if (shen_eq(symdic.symdic_kl_x123, car(car(KL_ARG_V626_75))) if shen_consp(car(KL_ARG_V626_75)) else False) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_76, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_76)][(-1)]
shen_add_fun('shen.<signature>', shen_x60signaturex62, 1)

@tail_recursion
def shen_curryx45type(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_curryx45type, (FUN_ARGS + lambdaargs)))
    KL_ARG_V629_78 = FUN_ARGS[0]
    global symdic
    return (tail_call(shen_curryx45type, [Cons(car(KL_ARG_V629_78), Cons(symdic.symdic_kl_x45x45x62, Cons(cdr(cdr(KL_ARG_V629_78)), nil)))]) if (((((shen_eq(symdic.symdic_kl_x45x45x62, car(cdr(cdr(cdr(KL_ARG_V629_78))))) if shen_consp(cdr(cdr(cdr(KL_ARG_V629_78)))) else False) if shen_consp(cdr(cdr(KL_ARG_V629_78))) else False) if shen_eq(symdic.symdic_kl_x45x45x62, car(cdr(KL_ARG_V629_78))) else False) if shen_consp(cdr(KL_ARG_V629_78)) else False) if shen_consp(KL_ARG_V629_78) else False) else (Cons(symdic.symdic_kl_list, Cons(tco_apply(shen_curryx45type, [car(cdr(KL_ARG_V629_78))]), nil)) if ((((shen_eq(nil, cdr(cdr(cdr(KL_ARG_V629_78)))) if shen_consp(cdr(cdr(KL_ARG_V629_78))) else False) if shen_consp(cdr(KL_ARG_V629_78)) else False) if shen_eq(symdic.symdic_kl_cons, car(KL_ARG_V629_78)) else False) if shen_consp(KL_ARG_V629_78) else False) else (tail_call(shen_curryx45type, [Cons(car(KL_ARG_V629_78), Cons(symdic.symdic_kl_x42, Cons(cdr(cdr(KL_ARG_V629_78)), nil)))]) if (((((shen_eq(symdic.symdic_kl_x42, car(cdr(cdr(cdr(KL_ARG_V629_78))))) if shen_consp(cdr(cdr(cdr(KL_ARG_V629_78)))) else False) if shen_consp(cdr(cdr(KL_ARG_V629_78))) else False) if shen_eq(symdic.symdic_kl_x42, car(cdr(KL_ARG_V629_78))) else False) if shen_consp(cdr(KL_ARG_V629_78)) else False) if shen_consp(KL_ARG_V629_78) else False) else (tail_call(kl_map, [symdic.symdic_shen_curryx45type, KL_ARG_V629_78]) if shen_consp(KL_ARG_V629_78) else (KL_ARG_V629_78 if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.curry-type', shen_curryx45type, 1)

@tail_recursion
def shen_x60signaturex45helpx62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60signaturex45helpx62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V634_79 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_80 = None
        KL_LOC_Parse_X_81 = None
        KL_LOC_Parse_shen_x60signaturex45helpx62_82 = None
        KL_LOC_Result_83 = None
        KL_LOC_Parse_x60ex62_84 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_80', ([setattr(KL_CTX, 'KL_LOC_Parse_X_81', car(car(KL_ARG_V634_79))), [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60signaturex45helpx62_82', tco_apply(shen_x60signaturex45helpx62, [tco_apply(shen_pair, [cdr(car(KL_ARG_V634_79)), tco_apply(shen_hdtl, [KL_ARG_V634_79])])])), ((tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60signaturex45helpx62_82), Cons(KL_CTX.KL_LOC_Parse_X_81, tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60signaturex45helpx62_82]))]) if (not tco_apply(kl_elementx63, [KL_CTX.KL_LOC_Parse_X_81, Cons(symdic.symdic_kl_x123, Cons(symdic.symdic_kl_x125, nil))])) else tco_apply(kl_fail, [])) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60signaturex45helpx62_82)) else tco_apply(kl_fail, []))][(-1)]][(-1)] if shen_consp(car(KL_ARG_V634_79)) else tco_apply(kl_fail, []))), ([setattr(KL_CTX, 'KL_LOC_Result_83', [setattr(KL_CTX, 'KL_LOC_Parse_x60ex62_84', tco_apply(kl_x60ex62, [KL_ARG_V634_79])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_x60ex62_84), nil]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_x60ex62_84)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_83, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_83)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_80, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_80)][(-1)]
shen_add_fun('shen.<signature-help>', shen_x60signaturex45helpx62, 1)

@tail_recursion
def shen_x60rulesx62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60rulesx62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V639_85 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_86 = None
        KL_LOC_Parse_shen_x60rulex62_87 = None
        KL_LOC_Parse_shen_x60rulesx62_88 = None
        KL_LOC_Result_89 = None
        KL_LOC_Parse_shen_x60rulex62_90 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_86', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60rulex62_87', tco_apply(shen_x60rulex62, [KL_ARG_V639_85])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60rulesx62_88', tco_apply(shen_x60rulesx62, [KL_CTX.KL_LOC_Parse_shen_x60rulex62_87])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60rulesx62_88), Cons(tco_apply(shen_linearise, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60rulex62_87])]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60rulesx62_88]))]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60rulesx62_88)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60rulex62_87)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_89', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60rulex62_90', tco_apply(shen_x60rulex62, [KL_ARG_V639_85])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60rulex62_90), Cons(tco_apply(shen_linearise, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60rulex62_90])]), nil)]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60rulex62_90)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_89, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_89)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_86, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_86)][(-1)]
shen_add_fun('shen.<rules>', shen_x60rulesx62, 1)

@tail_recursion
def shen_x60rulex62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60rulex62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V644_91 = FUN_ARGS[0]

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
    return [setattr(KL_CTX, 'KL_LOC_Result_92', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60patternsx62_93', tco_apply(shen_x60patternsx62, [KL_ARG_V644_91])), (([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60actionx62_94', tco_apply(shen_x60actionx62, [tco_apply(shen_pair, [cdr(car(KL_CTX.KL_LOC_Parse_shen_x60patternsx62_93)), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_93])])])), (([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60guardx62_95', tco_apply(shen_x60guardx62, [tco_apply(shen_pair, [cdr(car(KL_CTX.KL_LOC_Parse_shen_x60actionx62_94)), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60actionx62_94])])])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60guardx62_95), Cons(tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_93]), Cons(Cons(symdic.symdic_kl_where, Cons(tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60guardx62_95]), Cons(tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60actionx62_94]), nil))), nil))]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60guardx62_95)) else tco_apply(kl_fail, []))][(-1)] if (shen_eq(symdic.symdic_kl_where, car(car(KL_CTX.KL_LOC_Parse_shen_x60actionx62_94))) if shen_consp(car(KL_CTX.KL_LOC_Parse_shen_x60actionx62_94)) else False) else tco_apply(kl_fail, [])) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60actionx62_94)) else tco_apply(kl_fail, []))][(-1)] if (shen_eq(symdic.symdic_kl_x45x62, car(car(KL_CTX.KL_LOC_Parse_shen_x60patternsx62_93))) if shen_consp(car(KL_CTX.KL_LOC_Parse_shen_x60patternsx62_93)) else False) else tco_apply(kl_fail, [])) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60patternsx62_93)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_96', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60patternsx62_97', tco_apply(shen_x60patternsx62, [KL_ARG_V644_91])), (([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60actionx62_98', tco_apply(shen_x60actionx62, [tco_apply(shen_pair, [cdr(car(KL_CTX.KL_LOC_Parse_shen_x60patternsx62_97)), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_97])])])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60actionx62_98), Cons(tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_97]), Cons(tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60actionx62_98]), nil))]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60actionx62_98)) else tco_apply(kl_fail, []))][(-1)] if (shen_eq(symdic.symdic_kl_x45x62, car(car(KL_CTX.KL_LOC_Parse_shen_x60patternsx62_97))) if shen_consp(car(KL_CTX.KL_LOC_Parse_shen_x60patternsx62_97)) else False) else tco_apply(kl_fail, [])) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60patternsx62_97)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_99', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60patternsx62_100', tco_apply(shen_x60patternsx62, [KL_ARG_V644_91])), (([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60actionx62_101', tco_apply(shen_x60actionx62, [tco_apply(shen_pair, [cdr(car(KL_CTX.KL_LOC_Parse_shen_x60patternsx62_100)), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_100])])])), (([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60guardx62_102', tco_apply(shen_x60guardx62, [tco_apply(shen_pair, [cdr(car(KL_CTX.KL_LOC_Parse_shen_x60actionx62_101)), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60actionx62_101])])])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60guardx62_102), Cons(tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_100]), Cons(Cons(symdic.symdic_kl_where, Cons(tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60guardx62_102]), Cons(Cons(symdic.symdic_shen_choicepointx33, Cons(tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60actionx62_101]), nil)), nil))), nil))]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60guardx62_102)) else tco_apply(kl_fail, []))][(-1)] if (shen_eq(symdic.symdic_kl_where, car(car(KL_CTX.KL_LOC_Parse_shen_x60actionx62_101))) if shen_consp(car(KL_CTX.KL_LOC_Parse_shen_x60actionx62_101)) else False) else tco_apply(kl_fail, [])) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60actionx62_101)) else tco_apply(kl_fail, []))][(-1)] if (shen_eq(symdic.symdic_kl_x60x45, car(car(KL_CTX.KL_LOC_Parse_shen_x60patternsx62_100))) if shen_consp(car(KL_CTX.KL_LOC_Parse_shen_x60patternsx62_100)) else False) else tco_apply(kl_fail, [])) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60patternsx62_100)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_103', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60patternsx62_104', tco_apply(shen_x60patternsx62, [KL_ARG_V644_91])), (([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60actionx62_105', tco_apply(shen_x60actionx62, [tco_apply(shen_pair, [cdr(car(KL_CTX.KL_LOC_Parse_shen_x60patternsx62_104)), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_104])])])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60actionx62_105), Cons(tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_104]), Cons(Cons(symdic.symdic_shen_choicepointx33, Cons(tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60actionx62_105]), nil)), nil))]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60actionx62_105)) else tco_apply(kl_fail, []))][(-1)] if (shen_eq(symdic.symdic_kl_x60x45, car(car(KL_CTX.KL_LOC_Parse_shen_x60patternsx62_104))) if shen_consp(car(KL_CTX.KL_LOC_Parse_shen_x60patternsx62_104)) else False) else tco_apply(kl_fail, [])) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60patternsx62_104)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_103, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_103)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_99, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_99)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_96, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_96)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_92, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_92)][(-1)]
shen_add_fun('shen.<rule>', shen_x60rulex62, 1)

@tail_recursion
def shen_fail_if(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_fail_if, (FUN_ARGS + lambdaargs)))
    KL_ARG_V645_106 = FUN_ARGS[0]
    KL_ARG_V646_107 = FUN_ARGS[1]
    global symdic
    return (tail_call(kl_fail, []) if shen_apply(KL_ARG_V645_106, [KL_ARG_V646_107]) else KL_ARG_V646_107)
shen_add_fun('shen.fail_if', shen_fail_if, 2)

@tail_recursion
def shen_succeedsx63(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_succeedsx63, (FUN_ARGS + lambdaargs)))
    KL_ARG_V651_108 = FUN_ARGS[0]
    global symdic
    return (False if shen_eq(KL_ARG_V651_108, tco_apply(kl_fail, [])) else (True if True else shen_simple_error('condition failure')))
shen_add_fun('shen.succeeds?', shen_succeedsx63, 1)

@tail_recursion
def shen_x60patternsx62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60patternsx62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V656_109 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_110 = None
        KL_LOC_Parse_shen_x60patternx62_111 = None
        KL_LOC_Parse_shen_x60patternsx62_112 = None
        KL_LOC_Result_113 = None
        KL_LOC_Parse_x60ex62_114 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_110', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60patternx62_111', tco_apply(shen_x60patternx62, [KL_ARG_V656_109])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60patternsx62_112', tco_apply(shen_x60patternsx62, [KL_CTX.KL_LOC_Parse_shen_x60patternx62_111])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60patternsx62_112), Cons(tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternx62_111]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_112]))]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60patternsx62_112)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60patternx62_111)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_113', [setattr(KL_CTX, 'KL_LOC_Parse_x60ex62_114', tco_apply(kl_x60ex62, [KL_ARG_V656_109])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_x60ex62_114), nil]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_x60ex62_114)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_113, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_113)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_110, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_110)][(-1)]
shen_add_fun('shen.<patterns>', shen_x60patternsx62, 1)

@tail_recursion
def shen_x60patternx62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60patternx62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V661_115 = FUN_ARGS[0]

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
    return [setattr(KL_CTX, 'KL_LOC_Result_116', (tco_apply(shen_sndx45orx45fail, [([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60pattern1x62_117', tco_apply(shen_x60pattern1x62, [tco_apply(shen_pair, [cdr(car(tco_apply(shen_pair, [car(car(KL_ARG_V661_115)), tco_apply(shen_hdtl, [KL_ARG_V661_115])]))), tco_apply(shen_hdtl, [tco_apply(shen_pair, [car(car(KL_ARG_V661_115)), tco_apply(shen_hdtl, [KL_ARG_V661_115])])])])])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60pattern2x62_118', tco_apply(shen_x60pattern2x62, [KL_CTX.KL_LOC_Parse_shen_x60pattern1x62_117])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60pattern2x62_118), tco_apply(shen_pair, [car(tco_apply(shen_pair, [cdr(car(KL_ARG_V661_115)), tco_apply(shen_hdtl, [KL_ARG_V661_115])])), Cons(symdic.symdic_kl_x64p, Cons(tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60pattern1x62_117]), Cons(tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60pattern2x62_118]), nil)))])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60pattern2x62_118)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60pattern1x62_117)) else tco_apply(kl_fail, []))][(-1)] if (shen_eq(symdic.symdic_kl_x64p, car(car(tco_apply(shen_pair, [car(car(KL_ARG_V661_115)), tco_apply(shen_hdtl, [KL_ARG_V661_115])])))) if shen_consp(car(tco_apply(shen_pair, [car(car(KL_ARG_V661_115)), tco_apply(shen_hdtl, [KL_ARG_V661_115])]))) else False) else tco_apply(kl_fail, []))]) if (shen_consp(car(car(KL_ARG_V661_115))) if shen_consp(car(KL_ARG_V661_115)) else False) else tco_apply(kl_fail, []))), ([setattr(KL_CTX, 'KL_LOC_Result_119', (tco_apply(shen_sndx45orx45fail, [([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60pattern1x62_120', tco_apply(shen_x60pattern1x62, [tco_apply(shen_pair, [cdr(car(tco_apply(shen_pair, [car(car(KL_ARG_V661_115)), tco_apply(shen_hdtl, [KL_ARG_V661_115])]))), tco_apply(shen_hdtl, [tco_apply(shen_pair, [car(car(KL_ARG_V661_115)), tco_apply(shen_hdtl, [KL_ARG_V661_115])])])])])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60pattern2x62_121', tco_apply(shen_x60pattern2x62, [KL_CTX.KL_LOC_Parse_shen_x60pattern1x62_120])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60pattern2x62_121), tco_apply(shen_pair, [car(tco_apply(shen_pair, [cdr(car(KL_ARG_V661_115)), tco_apply(shen_hdtl, [KL_ARG_V661_115])])), Cons(symdic.symdic_kl_cons, Cons(tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60pattern1x62_120]), Cons(tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60pattern2x62_121]), nil)))])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60pattern2x62_121)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60pattern1x62_120)) else tco_apply(kl_fail, []))][(-1)] if (shen_eq(symdic.symdic_kl_cons, car(car(tco_apply(shen_pair, [car(car(KL_ARG_V661_115)), tco_apply(shen_hdtl, [KL_ARG_V661_115])])))) if shen_consp(car(tco_apply(shen_pair, [car(car(KL_ARG_V661_115)), tco_apply(shen_hdtl, [KL_ARG_V661_115])]))) else False) else tco_apply(kl_fail, []))]) if (shen_consp(car(car(KL_ARG_V661_115))) if shen_consp(car(KL_ARG_V661_115)) else False) else tco_apply(kl_fail, []))), ([setattr(KL_CTX, 'KL_LOC_Result_122', (tco_apply(shen_sndx45orx45fail, [([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60pattern1x62_123', tco_apply(shen_x60pattern1x62, [tco_apply(shen_pair, [cdr(car(tco_apply(shen_pair, [car(car(KL_ARG_V661_115)), tco_apply(shen_hdtl, [KL_ARG_V661_115])]))), tco_apply(shen_hdtl, [tco_apply(shen_pair, [car(car(KL_ARG_V661_115)), tco_apply(shen_hdtl, [KL_ARG_V661_115])])])])])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60pattern2x62_124', tco_apply(shen_x60pattern2x62, [KL_CTX.KL_LOC_Parse_shen_x60pattern1x62_123])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60pattern2x62_124), tco_apply(shen_pair, [car(tco_apply(shen_pair, [cdr(car(KL_ARG_V661_115)), tco_apply(shen_hdtl, [KL_ARG_V661_115])])), Cons(symdic.symdic_kl_x64v, Cons(tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60pattern1x62_123]), Cons(tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60pattern2x62_124]), nil)))])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60pattern2x62_124)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60pattern1x62_123)) else tco_apply(kl_fail, []))][(-1)] if (shen_eq(symdic.symdic_kl_x64v, car(car(tco_apply(shen_pair, [car(car(KL_ARG_V661_115)), tco_apply(shen_hdtl, [KL_ARG_V661_115])])))) if shen_consp(car(tco_apply(shen_pair, [car(car(KL_ARG_V661_115)), tco_apply(shen_hdtl, [KL_ARG_V661_115])]))) else False) else tco_apply(kl_fail, []))]) if (shen_consp(car(car(KL_ARG_V661_115))) if shen_consp(car(KL_ARG_V661_115)) else False) else tco_apply(kl_fail, []))), ([setattr(KL_CTX, 'KL_LOC_Result_125', (tco_apply(shen_sndx45orx45fail, [([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60pattern1x62_126', tco_apply(shen_x60pattern1x62, [tco_apply(shen_pair, [cdr(car(tco_apply(shen_pair, [car(car(KL_ARG_V661_115)), tco_apply(shen_hdtl, [KL_ARG_V661_115])]))), tco_apply(shen_hdtl, [tco_apply(shen_pair, [car(car(KL_ARG_V661_115)), tco_apply(shen_hdtl, [KL_ARG_V661_115])])])])])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60pattern2x62_127', tco_apply(shen_x60pattern2x62, [KL_CTX.KL_LOC_Parse_shen_x60pattern1x62_126])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60pattern2x62_127), tco_apply(shen_pair, [car(tco_apply(shen_pair, [cdr(car(KL_ARG_V661_115)), tco_apply(shen_hdtl, [KL_ARG_V661_115])])), Cons(symdic.symdic_kl_x64s, Cons(tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60pattern1x62_126]), Cons(tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60pattern2x62_127]), nil)))])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60pattern2x62_127)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60pattern1x62_126)) else tco_apply(kl_fail, []))][(-1)] if (shen_eq(symdic.symdic_kl_x64s, car(car(tco_apply(shen_pair, [car(car(KL_ARG_V661_115)), tco_apply(shen_hdtl, [KL_ARG_V661_115])])))) if shen_consp(car(tco_apply(shen_pair, [car(car(KL_ARG_V661_115)), tco_apply(shen_hdtl, [KL_ARG_V661_115])]))) else False) else tco_apply(kl_fail, []))]) if (shen_consp(car(car(KL_ARG_V661_115))) if shen_consp(car(KL_ARG_V661_115)) else False) else tco_apply(kl_fail, []))), ([setattr(KL_CTX, 'KL_LOC_Result_128', (tco_apply(shen_sndx45orx45fail, [((tco_apply(shen_pair, [car(tco_apply(shen_pair, [cdr(car(tco_apply(shen_pair, [cdr(car(tco_apply(shen_pair, [car(car(KL_ARG_V661_115)), tco_apply(shen_hdtl, [KL_ARG_V661_115])]))), tco_apply(shen_hdtl, [tco_apply(shen_pair, [car(car(KL_ARG_V661_115)), tco_apply(shen_hdtl, [KL_ARG_V661_115])])])]))), tco_apply(shen_hdtl, [tco_apply(shen_pair, [cdr(car(tco_apply(shen_pair, [car(car(KL_ARG_V661_115)), tco_apply(shen_hdtl, [KL_ARG_V661_115])]))), tco_apply(shen_hdtl, [tco_apply(shen_pair, [car(car(KL_ARG_V661_115)), tco_apply(shen_hdtl, [KL_ARG_V661_115])])])])])])), tco_apply(shen_pair, [car(tco_apply(shen_pair, [cdr(car(KL_ARG_V661_115)), tco_apply(shen_hdtl, [KL_ARG_V661_115])])), Cons(symdic.symdic_kl_vector, Cons(0, nil))])]) if (shen_eq(0, car(car(tco_apply(shen_pair, [cdr(car(tco_apply(shen_pair, [car(car(KL_ARG_V661_115)), tco_apply(shen_hdtl, [KL_ARG_V661_115])]))), tco_apply(shen_hdtl, [tco_apply(shen_pair, [car(car(KL_ARG_V661_115)), tco_apply(shen_hdtl, [KL_ARG_V661_115])])])])))) if shen_consp(car(tco_apply(shen_pair, [cdr(car(tco_apply(shen_pair, [car(car(KL_ARG_V661_115)), tco_apply(shen_hdtl, [KL_ARG_V661_115])]))), tco_apply(shen_hdtl, [tco_apply(shen_pair, [car(car(KL_ARG_V661_115)), tco_apply(shen_hdtl, [KL_ARG_V661_115])])])]))) else False) else tco_apply(kl_fail, [])) if (shen_eq(symdic.symdic_kl_vector, car(car(tco_apply(shen_pair, [car(car(KL_ARG_V661_115)), tco_apply(shen_hdtl, [KL_ARG_V661_115])])))) if shen_consp(car(tco_apply(shen_pair, [car(car(KL_ARG_V661_115)), tco_apply(shen_hdtl, [KL_ARG_V661_115])]))) else False) else tco_apply(kl_fail, []))]) if (shen_consp(car(car(KL_ARG_V661_115))) if shen_consp(car(KL_ARG_V661_115)) else False) else tco_apply(kl_fail, []))), ([setattr(KL_CTX, 'KL_LOC_Result_129', ([setattr(KL_CTX, 'KL_LOC_Parse_X_130', car(car(KL_ARG_V661_115))), (tco_apply(shen_pair, [car(tco_apply(shen_pair, [cdr(car(KL_ARG_V661_115)), tco_apply(shen_hdtl, [KL_ARG_V661_115])])), tco_apply(shen_constructorx45error, [KL_CTX.KL_LOC_Parse_X_130])]) if shen_consp(KL_CTX.KL_LOC_Parse_X_130) else tco_apply(kl_fail, []))][(-1)] if shen_consp(car(KL_ARG_V661_115)) else tco_apply(kl_fail, []))), ([setattr(KL_CTX, 'KL_LOC_Result_131', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60simple_patternx62_132', tco_apply(shen_x60simple_patternx62, [KL_ARG_V661_115])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60simple_patternx62_132), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60simple_patternx62_132])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60simple_patternx62_132)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_131, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_131)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_129, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_129)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_128, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_128)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_125, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_125)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_122, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_122)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_119, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_119)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_116, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_116)][(-1)]
shen_add_fun('shen.<pattern>', shen_x60patternx62, 1)

@tail_recursion
def shen_constructorx45error(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_constructorx45error, (FUN_ARGS + lambdaargs)))
    KL_ARG_V662_133 = FUN_ARGS[0]
    global symdic
    return shen_simple_error(tco_apply(shen_app, [KL_ARG_V662_133, ' is not a legitimate constructor\r\n', symdic.symdic_shen_a]))
shen_add_fun('shen.constructor-error', shen_constructorx45error, 1)

@tail_recursion
def shen_x60simple_patternx62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60simple_patternx62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V667_134 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_135 = None
        KL_LOC_Parse_X_136 = None
        KL_LOC_Result_137 = None
        KL_LOC_Parse_X_138 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_135', ([setattr(KL_CTX, 'KL_LOC_Parse_X_136', car(car(KL_ARG_V667_134))), (tco_apply(shen_pair, [car(tco_apply(shen_pair, [cdr(car(KL_ARG_V667_134)), tco_apply(shen_hdtl, [KL_ARG_V667_134])])), tco_apply(kl_gensym, [symdic.symdic_Parse_Y])]) if shen_eq(KL_CTX.KL_LOC_Parse_X_136, symdic.symdic_kl__) else tco_apply(kl_fail, []))][(-1)] if shen_consp(car(KL_ARG_V667_134)) else tco_apply(kl_fail, []))), ([setattr(KL_CTX, 'KL_LOC_Result_137', ([setattr(KL_CTX, 'KL_LOC_Parse_X_138', car(car(KL_ARG_V667_134))), (tco_apply(shen_pair, [car(tco_apply(shen_pair, [cdr(car(KL_ARG_V667_134)), tco_apply(shen_hdtl, [KL_ARG_V667_134])])), KL_CTX.KL_LOC_Parse_X_138]) if (not tco_apply(kl_elementx63, [KL_CTX.KL_LOC_Parse_X_138, Cons(symdic.symdic_kl_x45x62, Cons(symdic.symdic_kl_x60x45, nil))])) else tco_apply(kl_fail, []))][(-1)] if shen_consp(car(KL_ARG_V667_134)) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_137, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_137)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_135, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_135)][(-1)]
shen_add_fun('shen.<simple_pattern>', shen_x60simple_patternx62, 1)

@tail_recursion
def shen_x60pattern1x62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60pattern1x62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V672_139 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_140 = None
        KL_LOC_Parse_shen_x60patternx62_141 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_140', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60patternx62_141', tco_apply(shen_x60patternx62, [KL_ARG_V672_139])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60patternx62_141), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternx62_141])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60patternx62_141)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_140, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_140)][(-1)]
shen_add_fun('shen.<pattern1>', shen_x60pattern1x62, 1)

@tail_recursion
def shen_x60pattern2x62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60pattern2x62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V677_142 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_143 = None
        KL_LOC_Parse_shen_x60patternx62_144 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_143', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60patternx62_144', tco_apply(shen_x60patternx62, [KL_ARG_V677_142])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60patternx62_144), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternx62_144])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60patternx62_144)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_143, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_143)][(-1)]
shen_add_fun('shen.<pattern2>', shen_x60pattern2x62, 1)

@tail_recursion
def shen_x60actionx62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60actionx62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V682_145 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_146 = None
        KL_LOC_Parse_X_147 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_146', ([setattr(KL_CTX, 'KL_LOC_Parse_X_147', car(car(KL_ARG_V682_145))), tco_apply(shen_pair, [car(tco_apply(shen_pair, [cdr(car(KL_ARG_V682_145)), tco_apply(shen_hdtl, [KL_ARG_V682_145])])), KL_CTX.KL_LOC_Parse_X_147])][(-1)] if shen_consp(car(KL_ARG_V682_145)) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_146, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_146)][(-1)]
shen_add_fun('shen.<action>', shen_x60actionx62, 1)

@tail_recursion
def shen_x60guardx62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60guardx62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V687_148 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_149 = None
        KL_LOC_Parse_X_150 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_149', ([setattr(KL_CTX, 'KL_LOC_Parse_X_150', car(car(KL_ARG_V687_148))), tco_apply(shen_pair, [car(tco_apply(shen_pair, [cdr(car(KL_ARG_V687_148)), tco_apply(shen_hdtl, [KL_ARG_V687_148])])), KL_CTX.KL_LOC_Parse_X_150])][(-1)] if shen_consp(car(KL_ARG_V687_148)) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_149, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_149)][(-1)]
shen_add_fun('shen.<guard>', shen_x60guardx62, 1)

@tail_recursion
def shen_compile_to_machine_code(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_compile_to_machine_code, (FUN_ARGS + lambdaargs)))
    KL_ARG_V688_151 = FUN_ARGS[0]
    KL_ARG_V689_152 = FUN_ARGS[1]

    class KL_Context:
        KL_LOC_Lambdax43_153 = None
        KL_LOC_KL_154 = None
        KL_LOC_Record_155 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Lambdax43_153', tco_apply(shen_compile_to_lambdax43, [KL_ARG_V688_151, KL_ARG_V689_152])), [setattr(KL_CTX, 'KL_LOC_KL_154', tco_apply(shen_compile_to_kl, [KL_ARG_V688_151, KL_CTX.KL_LOC_Lambdax43_153])), [setattr(KL_CTX, 'KL_LOC_Record_155', tco_apply(shen_recordx45source, [KL_ARG_V688_151, KL_CTX.KL_LOC_KL_154])), KL_CTX.KL_LOC_KL_154][(-1)]][(-1)]][(-1)]
shen_add_fun('shen.compile_to_machine_code', shen_compile_to_machine_code, 2)

@tail_recursion
def shen_recordx45source(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_recordx45source, (FUN_ARGS + lambdaargs)))
    KL_ARG_V692_156 = FUN_ARGS[0]
    KL_ARG_V693_157 = FUN_ARGS[1]
    global symdic
    return (symdic.symdic_shen_skip if shen_get(symdic.symdic_shen_x42installingx45klx42) else (tail_call(kl_put, [KL_ARG_V692_156, symdic.symdic_shen_source, KL_ARG_V693_157, shen_get(symdic.symdic_kl_x42propertyx45vectorx42)]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.record-source', shen_recordx45source, 2)

@tail_recursion
def shen_compile_to_lambdax43(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_compile_to_lambdax43, (FUN_ARGS + lambdaargs)))
    KL_ARG_V694_158 = FUN_ARGS[0]
    KL_ARG_V695_159 = FUN_ARGS[1]

    class KL_Context:
        KL_LOC_Arity_160 = None
        KL_LOC_Free_161 = None
        KL_LOC_Variables_163 = None
        KL_LOC_Strip_164 = None
        KL_LOC_Abstractions_165 = None
        KL_LOC_Applications_166 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Arity_160', tco_apply(shen_aritycheck, [KL_ARG_V694_158, KL_ARG_V695_159])), [setattr(KL_CTX, 'KL_LOC_Free_161', tco_apply(kl_map, [(lambda KL_ARG_Rule_162: tail_call(shen_free_variable_check, [KL_ARG_V694_158, KL_ARG_Rule_162])), KL_ARG_V695_159])), [setattr(KL_CTX, 'KL_LOC_Variables_163', tco_apply(shen_parameters, [KL_CTX.KL_LOC_Arity_160])), [setattr(KL_CTX, 'KL_LOC_Strip_164', tco_apply(kl_map, [symdic.symdic_shen_stripx45protect, KL_ARG_V695_159])), [setattr(KL_CTX, 'KL_LOC_Abstractions_165', tco_apply(kl_map, [symdic.symdic_shen_abstract_rule, KL_CTX.KL_LOC_Strip_164])), [setattr(KL_CTX, 'KL_LOC_Applications_166', tco_apply(kl_map, [(lambda KL_ARG_X_167: tail_call(shen_application_build, [KL_CTX.KL_LOC_Variables_163, KL_ARG_X_167])), KL_CTX.KL_LOC_Abstractions_165])), Cons(KL_CTX.KL_LOC_Variables_163, Cons(KL_CTX.KL_LOC_Applications_166, nil))][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]
shen_add_fun('shen.compile_to_lambda+', shen_compile_to_lambdax43, 2)

@tail_recursion
def shen_free_variable_check(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_free_variable_check, (FUN_ARGS + lambdaargs)))
    KL_ARG_V696_168 = FUN_ARGS[0]
    KL_ARG_V697_169 = FUN_ARGS[1]

    class KL_Context:
        KL_LOC_Bound_170 = None
        KL_LOC_Free_171 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_Bound_170', tco_apply(shen_extract_vars, [car(KL_ARG_V697_169)])), [setattr(KL_CTX, 'KL_LOC_Free_171', tco_apply(shen_extract_free_vars, [KL_CTX.KL_LOC_Bound_170, car(cdr(KL_ARG_V697_169))])), tail_call(shen_free_variable_warnings, [KL_ARG_V696_168, KL_CTX.KL_LOC_Free_171])][(-1)]][(-1)] if ((shen_eq(nil, cdr(cdr(KL_ARG_V697_169))) if shen_consp(cdr(KL_ARG_V697_169)) else False) if shen_consp(KL_ARG_V697_169) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_free_variable_check]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.free_variable_check', shen_free_variable_check, 2)

@tail_recursion
def shen_extract_vars(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_extract_vars, (FUN_ARGS + lambdaargs)))
    KL_ARG_V698_172 = FUN_ARGS[0]
    global symdic
    return (Cons(KL_ARG_V698_172, nil) if tco_apply(kl_variablex63, [KL_ARG_V698_172]) else (tail_call(kl_union, [tco_apply(shen_extract_vars, [car(KL_ARG_V698_172)]), tco_apply(shen_extract_vars, [cdr(KL_ARG_V698_172)])]) if shen_consp(KL_ARG_V698_172) else (nil if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.extract_vars', shen_extract_vars, 1)

@tail_recursion
def shen_extract_free_vars(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_extract_free_vars, (FUN_ARGS + lambdaargs)))
    KL_ARG_V708_173 = FUN_ARGS[0]
    KL_ARG_V709_174 = FUN_ARGS[1]
    global symdic
    return (nil if (((shen_eq(car(KL_ARG_V709_174), symdic.symdic_kl_protect) if shen_eq(nil, cdr(cdr(KL_ARG_V709_174))) else False) if shen_consp(cdr(KL_ARG_V709_174)) else False) if shen_consp(KL_ARG_V709_174) else False) else (Cons(KL_ARG_V709_174, nil) if ((not tco_apply(kl_elementx63, [KL_ARG_V709_174, KL_ARG_V708_173])) if tco_apply(kl_variablex63, [KL_ARG_V709_174]) else False) else (tail_call(shen_extract_free_vars, [Cons(car(cdr(KL_ARG_V709_174)), KL_ARG_V708_173), car(cdr(cdr(KL_ARG_V709_174)))]) if ((((shen_eq(nil, cdr(cdr(cdr(KL_ARG_V709_174)))) if shen_consp(cdr(cdr(KL_ARG_V709_174))) else False) if shen_consp(cdr(KL_ARG_V709_174)) else False) if shen_eq(symdic.symdic_kl_lambda, car(KL_ARG_V709_174)) else False) if shen_consp(KL_ARG_V709_174) else False) else (tail_call(kl_union, [tco_apply(shen_extract_free_vars, [KL_ARG_V708_173, car(cdr(cdr(KL_ARG_V709_174)))]), tco_apply(shen_extract_free_vars, [Cons(car(cdr(KL_ARG_V709_174)), KL_ARG_V708_173), car(cdr(cdr(cdr(KL_ARG_V709_174))))])]) if (((((shen_eq(nil, cdr(cdr(cdr(cdr(KL_ARG_V709_174))))) if shen_consp(cdr(cdr(cdr(KL_ARG_V709_174)))) else False) if shen_consp(cdr(cdr(KL_ARG_V709_174))) else False) if shen_consp(cdr(KL_ARG_V709_174)) else False) if shen_eq(symdic.symdic_kl_let, car(KL_ARG_V709_174)) else False) if shen_consp(KL_ARG_V709_174) else False) else (tail_call(kl_union, [tco_apply(shen_extract_free_vars, [KL_ARG_V708_173, car(KL_ARG_V709_174)]), tco_apply(shen_extract_free_vars, [KL_ARG_V708_173, cdr(KL_ARG_V709_174)])]) if shen_consp(KL_ARG_V709_174) else (nil if True else shen_simple_error('condition failure')))))))
shen_add_fun('shen.extract_free_vars', shen_extract_free_vars, 2)

@tail_recursion
def shen_free_variable_warnings(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_free_variable_warnings, (FUN_ARGS + lambdaargs)))
    KL_ARG_V712_175 = FUN_ARGS[0]
    KL_ARG_V713_176 = FUN_ARGS[1]
    global symdic
    return (symdic.symdic_kl__ if shen_eq(nil, KL_ARG_V713_176) else (shen_simple_error(('error: the following variables are free in ' + tco_apply(shen_app, [KL_ARG_V712_175, (': ' + tco_apply(shen_app, [tco_apply(shen_list_variables, [KL_ARG_V713_176]), '', symdic.symdic_shen_a])), symdic.symdic_shen_a]))) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.free_variable_warnings', shen_free_variable_warnings, 2)

@tail_recursion
def shen_list_variables(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_list_variables, (FUN_ARGS + lambdaargs)))
    KL_ARG_V714_177 = FUN_ARGS[0]
    global symdic
    return ((str(car(KL_ARG_V714_177)) + '.') if (shen_eq(nil, cdr(KL_ARG_V714_177)) if shen_consp(KL_ARG_V714_177) else False) else ((str(car(KL_ARG_V714_177)) + (', ' + tco_apply(shen_list_variables, [cdr(KL_ARG_V714_177)]))) if shen_consp(KL_ARG_V714_177) else (tail_call(shen_sysx45error, [symdic.symdic_shen_list_variables]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.list_variables', shen_list_variables, 1)

@tail_recursion
def shen_stripx45protect(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_stripx45protect, (FUN_ARGS + lambdaargs)))
    KL_ARG_V715_178 = FUN_ARGS[0]
    global symdic
    return (car(cdr(KL_ARG_V715_178)) if (((shen_eq(car(KL_ARG_V715_178), symdic.symdic_kl_protect) if shen_eq(nil, cdr(cdr(KL_ARG_V715_178))) else False) if shen_consp(cdr(KL_ARG_V715_178)) else False) if shen_consp(KL_ARG_V715_178) else False) else (Cons(tco_apply(shen_stripx45protect, [car(KL_ARG_V715_178)]), tco_apply(shen_stripx45protect, [cdr(KL_ARG_V715_178)])) if shen_consp(KL_ARG_V715_178) else (KL_ARG_V715_178 if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.strip-protect', shen_stripx45protect, 1)

@tail_recursion
def shen_linearise(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_linearise, (FUN_ARGS + lambdaargs)))
    KL_ARG_V716_179 = FUN_ARGS[0]
    global symdic
    return (tail_call(shen_linearise_help, [tco_apply(shen_flatten, [car(KL_ARG_V716_179)]), car(KL_ARG_V716_179), car(cdr(KL_ARG_V716_179))]) if ((shen_eq(nil, cdr(cdr(KL_ARG_V716_179))) if shen_consp(cdr(KL_ARG_V716_179)) else False) if shen_consp(KL_ARG_V716_179) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_linearise]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.linearise', shen_linearise, 1)

@tail_recursion
def shen_flatten(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_flatten, (FUN_ARGS + lambdaargs)))
    KL_ARG_V717_180 = FUN_ARGS[0]
    global symdic
    return (nil if shen_eq(nil, KL_ARG_V717_180) else (tail_call(kl_append, [tco_apply(shen_flatten, [car(KL_ARG_V717_180)]), tco_apply(shen_flatten, [cdr(KL_ARG_V717_180)])]) if shen_consp(KL_ARG_V717_180) else (Cons(KL_ARG_V717_180, nil) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.flatten', shen_flatten, 1)

@tail_recursion
def shen_linearise_help(*FUN_ARGS):
    FUN_ARITY = 3
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_linearise_help, (FUN_ARGS + lambdaargs)))
    KL_ARG_V718_181 = FUN_ARGS[0]
    KL_ARG_V719_182 = FUN_ARGS[1]
    KL_ARG_V720_183 = FUN_ARGS[2]

    class KL_Context:
        KL_LOC_Var_184 = None
        KL_LOC_NewAction_185 = None
        KL_LOC_NewPatts_186 = None
    KL_CTX = KL_Context()
    global symdic
    return (Cons(KL_ARG_V719_182, Cons(KL_ARG_V720_183, nil)) if shen_eq(nil, KL_ARG_V718_181) else (([setattr(KL_CTX, 'KL_LOC_Var_184', tco_apply(kl_gensym, [car(KL_ARG_V718_181)])), [setattr(KL_CTX, 'KL_LOC_NewAction_185', Cons(symdic.symdic_kl_where, Cons(Cons(symdic.symdic_kl_x61, Cons(car(KL_ARG_V718_181), Cons(KL_CTX.KL_LOC_Var_184, nil))), Cons(KL_ARG_V720_183, nil)))), [setattr(KL_CTX, 'KL_LOC_NewPatts_186', tco_apply(shen_linearise_X, [car(KL_ARG_V718_181), KL_CTX.KL_LOC_Var_184, KL_ARG_V719_182])), tail_call(shen_linearise_help, [cdr(KL_ARG_V718_181), KL_CTX.KL_LOC_NewPatts_186, KL_CTX.KL_LOC_NewAction_185])][(-1)]][(-1)]][(-1)] if (tco_apply(kl_elementx63, [car(KL_ARG_V718_181), cdr(KL_ARG_V718_181)]) if tco_apply(kl_variablex63, [car(KL_ARG_V718_181)]) else False) else tail_call(shen_linearise_help, [cdr(KL_ARG_V718_181), KL_ARG_V719_182, KL_ARG_V720_183])) if shen_consp(KL_ARG_V718_181) else (tail_call(shen_sysx45error, [symdic.symdic_shen_linearise_help]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.linearise_help', shen_linearise_help, 3)

@tail_recursion
def shen_linearise_X(*FUN_ARGS):
    FUN_ARITY = 3
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_linearise_X, (FUN_ARGS + lambdaargs)))
    KL_ARG_V729_187 = FUN_ARGS[0]
    KL_ARG_V730_188 = FUN_ARGS[1]
    KL_ARG_V731_189 = FUN_ARGS[2]

    class KL_Context:
        KL_LOC_L_190 = None
    KL_CTX = KL_Context()
    global symdic
    return (KL_ARG_V730_188 if shen_eq(KL_ARG_V731_189, KL_ARG_V729_187) else ([setattr(KL_CTX, 'KL_LOC_L_190', tco_apply(shen_linearise_X, [KL_ARG_V729_187, KL_ARG_V730_188, car(KL_ARG_V731_189)])), (Cons(car(KL_ARG_V731_189), tco_apply(shen_linearise_X, [KL_ARG_V729_187, KL_ARG_V730_188, cdr(KL_ARG_V731_189)])) if shen_eq(KL_CTX.KL_LOC_L_190, car(KL_ARG_V731_189)) else Cons(KL_CTX.KL_LOC_L_190, cdr(KL_ARG_V731_189)))][(-1)] if shen_consp(KL_ARG_V731_189) else (KL_ARG_V731_189 if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.linearise_X', shen_linearise_X, 3)

@tail_recursion
def shen_aritycheck(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_aritycheck, (FUN_ARGS + lambdaargs)))
    KL_ARG_V733_191 = FUN_ARGS[0]
    KL_ARG_V734_192 = FUN_ARGS[1]
    global symdic
    return ([tco_apply(shen_aritycheckx45action, [car(cdr(car(KL_ARG_V734_192)))]), tail_call(shen_aritycheckx45name, [KL_ARG_V733_191, tco_apply(kl_arity, [KL_ARG_V733_191]), tco_apply(kl_length, [car(car(KL_ARG_V734_192))])])][(-1)] if ((((shen_eq(nil, cdr(KL_ARG_V734_192)) if shen_eq(nil, cdr(cdr(car(KL_ARG_V734_192)))) else False) if shen_consp(cdr(car(KL_ARG_V734_192))) else False) if shen_consp(car(KL_ARG_V734_192)) else False) if shen_consp(KL_ARG_V734_192) else False) else (([tco_apply(shen_aritycheckx45action, [car(cdr(car(KL_ARG_V734_192)))]), tail_call(shen_aritycheck, [KL_ARG_V733_191, cdr(KL_ARG_V734_192)])][(-1)] if shen_eq(tco_apply(kl_length, [car(car(KL_ARG_V734_192))]), tco_apply(kl_length, [car(car(cdr(KL_ARG_V734_192)))])) else shen_simple_error(('arity error in ' + tco_apply(shen_app, [KL_ARG_V733_191, '\r\n', symdic.symdic_shen_a])))) if (((((((shen_eq(nil, cdr(cdr(car(cdr(KL_ARG_V734_192))))) if shen_consp(cdr(car(cdr(KL_ARG_V734_192)))) else False) if shen_consp(car(cdr(KL_ARG_V734_192))) else False) if shen_consp(cdr(KL_ARG_V734_192)) else False) if shen_eq(nil, cdr(cdr(car(KL_ARG_V734_192)))) else False) if shen_consp(cdr(car(KL_ARG_V734_192))) else False) if shen_consp(car(KL_ARG_V734_192)) else False) if shen_consp(KL_ARG_V734_192) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_aritycheck]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.aritycheck', shen_aritycheck, 2)

@tail_recursion
def shen_aritycheckx45name(*FUN_ARGS):
    FUN_ARITY = 3
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_aritycheckx45name, (FUN_ARGS + lambdaargs)))
    KL_ARG_V743_193 = FUN_ARGS[0]
    KL_ARG_V744_194 = FUN_ARGS[1]
    KL_ARG_V745_195 = FUN_ARGS[2]
    global symdic
    return (KL_ARG_V745_195 if shen_eq((-1), KL_ARG_V744_194) else (KL_ARG_V745_195 if shen_eq(KL_ARG_V745_195, KL_ARG_V744_194) else ([tco_apply(shen_prhush, [('\r\nwarning: changing the arity of ' + tco_apply(shen_app, [KL_ARG_V743_193, ' can cause errors.\r\n', symdic.symdic_shen_a])), tco_apply(kl_stoutput, [])]), KL_ARG_V745_195][(-1)] if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.aritycheck-name', shen_aritycheckx45name, 3)

@tail_recursion
def shen_aritycheckx45action(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_aritycheckx45action, (FUN_ARGS + lambdaargs)))
    KL_ARG_V751_196 = FUN_ARGS[0]
    global symdic
    return ([tco_apply(shen_aah, [car(KL_ARG_V751_196), cdr(KL_ARG_V751_196)]), tail_call(kl_map, [symdic.symdic_shen_aritycheckx45action, KL_ARG_V751_196])][(-1)] if shen_consp(KL_ARG_V751_196) else (symdic.symdic_shen_skip if True else shen_simple_error('condition failure')))
shen_add_fun('shen.aritycheck-action', shen_aritycheckx45action, 1)

@tail_recursion
def shen_aah(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_aah, (FUN_ARGS + lambdaargs)))
    KL_ARG_V752_197 = FUN_ARGS[0]
    KL_ARG_V753_198 = FUN_ARGS[1]

    class KL_Context:
        KL_LOC_Arity_199 = None
        KL_LOC_Len_200 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Arity_199', tco_apply(kl_arity, [KL_ARG_V752_197])), [setattr(KL_CTX, 'KL_LOC_Len_200', tco_apply(kl_length, [KL_ARG_V753_198])), (tail_call(shen_prhush, [('warning: ' + tco_apply(shen_app, [KL_ARG_V752_197, (' might not like ' + tco_apply(shen_app, [KL_CTX.KL_LOC_Len_200, (' argument' + tco_apply(shen_app, [('s' if (KL_CTX.KL_LOC_Len_200 > 1) else ''), '.\r\n', symdic.symdic_shen_a])), symdic.symdic_shen_a])), symdic.symdic_shen_a])), tco_apply(kl_stoutput, [])]) if ((KL_CTX.KL_LOC_Len_200 > KL_CTX.KL_LOC_Arity_199) if (KL_CTX.KL_LOC_Arity_199 > (-1)) else False) else symdic.symdic_shen_skip)][(-1)]][(-1)]
shen_add_fun('shen.aah', shen_aah, 2)

@tail_recursion
def shen_abstract_rule(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_abstract_rule, (FUN_ARGS + lambdaargs)))
    KL_ARG_V754_201 = FUN_ARGS[0]
    global symdic
    return (tail_call(shen_abstraction_build, [car(KL_ARG_V754_201), car(cdr(KL_ARG_V754_201))]) if ((shen_eq(nil, cdr(cdr(KL_ARG_V754_201))) if shen_consp(cdr(KL_ARG_V754_201)) else False) if shen_consp(KL_ARG_V754_201) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_abstract_rule]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.abstract_rule', shen_abstract_rule, 1)

@tail_recursion
def shen_abstraction_build(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_abstraction_build, (FUN_ARGS + lambdaargs)))
    KL_ARG_V755_202 = FUN_ARGS[0]
    KL_ARG_V756_203 = FUN_ARGS[1]
    global symdic
    return (KL_ARG_V756_203 if shen_eq(nil, KL_ARG_V755_202) else (Cons(symdic.symdic_kl_x47_, Cons(car(KL_ARG_V755_202), Cons(tco_apply(shen_abstraction_build, [cdr(KL_ARG_V755_202), KL_ARG_V756_203]), nil))) if shen_consp(KL_ARG_V755_202) else (tail_call(shen_sysx45error, [symdic.symdic_shen_abstraction_build]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.abstraction_build', shen_abstraction_build, 2)

@tail_recursion
def shen_parameters(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_parameters, (FUN_ARGS + lambdaargs)))
    KL_ARG_V757_204 = FUN_ARGS[0]
    global symdic
    return (nil if shen_eq(0, KL_ARG_V757_204) else (Cons(tco_apply(kl_gensym, [symdic.symdic_V]), tco_apply(shen_parameters, [(KL_ARG_V757_204 - 1)])) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.parameters', shen_parameters, 1)

@tail_recursion
def shen_application_build(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_application_build, (FUN_ARGS + lambdaargs)))
    KL_ARG_V758_205 = FUN_ARGS[0]
    KL_ARG_V759_206 = FUN_ARGS[1]
    global symdic
    return (KL_ARG_V759_206 if shen_eq(nil, KL_ARG_V758_205) else (tail_call(shen_application_build, [cdr(KL_ARG_V758_205), Cons(KL_ARG_V759_206, Cons(car(KL_ARG_V758_205), nil))]) if shen_consp(KL_ARG_V758_205) else (tail_call(shen_sysx45error, [symdic.symdic_shen_application_build]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.application_build', shen_application_build, 2)

@tail_recursion
def shen_compile_to_kl(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_compile_to_kl, (FUN_ARGS + lambdaargs)))
    KL_ARG_V760_207 = FUN_ARGS[0]
    KL_ARG_V761_208 = FUN_ARGS[1]

    class KL_Context:
        KL_LOC_Arity_209 = None
        KL_LOC_Reduce_210 = None
        KL_LOC_CondExpression_211 = None
        KL_LOC_TypeTable_212 = None
        KL_LOC_TypedCondExpression_213 = None
        KL_LOC_KL_214 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_Arity_209', tco_apply(shen_storex45arity, [KL_ARG_V760_207, tco_apply(kl_length, [car(KL_ARG_V761_208)])])), [setattr(KL_CTX, 'KL_LOC_Reduce_210', tco_apply(kl_map, [symdic.symdic_shen_reduce, car(cdr(KL_ARG_V761_208))])), [setattr(KL_CTX, 'KL_LOC_CondExpression_211', tco_apply(shen_condx45expression, [KL_ARG_V760_207, car(KL_ARG_V761_208), KL_CTX.KL_LOC_Reduce_210])), [setattr(KL_CTX, 'KL_LOC_TypeTable_212', (tco_apply(shen_typextable, [tco_apply(shen_getx45type, [KL_ARG_V760_207]), car(KL_ARG_V761_208)]) if shen_get(symdic.symdic_shen_x42optimisex42) else symdic.symdic_shen_skip)), [setattr(KL_CTX, 'KL_LOC_TypedCondExpression_213', (tco_apply(shen_assignx45types, [car(KL_ARG_V761_208), KL_CTX.KL_LOC_TypeTable_212, KL_CTX.KL_LOC_CondExpression_211]) if shen_get(symdic.symdic_shen_x42optimisex42) else KL_CTX.KL_LOC_CondExpression_211)), [setattr(KL_CTX, 'KL_LOC_KL_214', Cons(symdic.symdic_kl_defun, Cons(KL_ARG_V760_207, Cons(car(KL_ARG_V761_208), Cons(KL_CTX.KL_LOC_TypedCondExpression_213, nil))))), KL_CTX.KL_LOC_KL_214][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)] if ((shen_eq(nil, cdr(cdr(KL_ARG_V761_208))) if shen_consp(cdr(KL_ARG_V761_208)) else False) if shen_consp(KL_ARG_V761_208) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_compile_to_kl]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.compile_to_kl', shen_compile_to_kl, 2)

@tail_recursion
def shen_getx45type(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_getx45type, (FUN_ARGS + lambdaargs)))
    KL_ARG_V766_215 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_FType_216 = None
    KL_CTX = KL_Context()
    global symdic
    return (symdic.symdic_shen_skip if shen_consp(KL_ARG_V766_215) else ([setattr(KL_CTX, 'KL_LOC_FType_216', tco_apply(kl_assoc, [KL_ARG_V766_215, shen_get(symdic.symdic_shen_x42signedfuncsx42)])), (symdic.symdic_shen_skip if tco_apply(kl_emptyx63, [KL_CTX.KL_LOC_FType_216]) else cdr(KL_CTX.KL_LOC_FType_216))][(-1)] if True else shen_simple_error('condition failure')))
shen_add_fun('shen.get-type', shen_getx45type, 1)

@tail_recursion
def shen_typextable(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_typextable, (FUN_ARGS + lambdaargs)))
    KL_ARG_V775_217 = FUN_ARGS[0]
    KL_ARG_V776_218 = FUN_ARGS[1]
    global symdic
    return ((tail_call(shen_typextable, [car(cdr(cdr(KL_ARG_V775_217))), cdr(KL_ARG_V776_218)]) if tco_apply(kl_variablex63, [car(KL_ARG_V775_217)]) else Cons(Cons(car(KL_ARG_V776_218), car(KL_ARG_V775_217)), tco_apply(shen_typextable, [car(cdr(cdr(KL_ARG_V775_217))), cdr(KL_ARG_V776_218)]))) if (((((shen_consp(KL_ARG_V776_218) if shen_eq(nil, cdr(cdr(cdr(KL_ARG_V775_217)))) else False) if shen_consp(cdr(cdr(KL_ARG_V775_217))) else False) if shen_eq(symdic.symdic_kl_x45x45x62, car(cdr(KL_ARG_V775_217))) else False) if shen_consp(cdr(KL_ARG_V775_217)) else False) if shen_consp(KL_ARG_V775_217) else False) else (nil if True else shen_simple_error('condition failure')))
shen_add_fun('shen.typextable', shen_typextable, 2)

@tail_recursion
def shen_assignx45types(*FUN_ARGS):
    FUN_ARITY = 3
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_assignx45types, (FUN_ARGS + lambdaargs)))
    KL_ARG_V777_219 = FUN_ARGS[0]
    KL_ARG_V778_220 = FUN_ARGS[1]
    KL_ARG_V779_221 = FUN_ARGS[2]

    class KL_Context:
        KL_LOC_NewTable_223 = None
        KL_LOC_AtomType_225 = None
    KL_CTX = KL_Context()
    global symdic
    return (Cons(symdic.symdic_kl_let, Cons(car(cdr(KL_ARG_V779_221)), Cons(tco_apply(shen_assignx45types, [KL_ARG_V777_219, KL_ARG_V778_220, car(cdr(cdr(KL_ARG_V779_221)))]), Cons(tco_apply(shen_assignx45types, [Cons(car(cdr(KL_ARG_V779_221)), KL_ARG_V777_219), KL_ARG_V778_220, car(cdr(cdr(cdr(KL_ARG_V779_221))))]), nil)))) if (((((shen_eq(nil, cdr(cdr(cdr(cdr(KL_ARG_V779_221))))) if shen_consp(cdr(cdr(cdr(KL_ARG_V779_221)))) else False) if shen_consp(cdr(cdr(KL_ARG_V779_221))) else False) if shen_consp(cdr(KL_ARG_V779_221)) else False) if shen_eq(symdic.symdic_kl_let, car(KL_ARG_V779_221)) else False) if shen_consp(KL_ARG_V779_221) else False) else (Cons(symdic.symdic_kl_lambda, Cons(car(cdr(KL_ARG_V779_221)), Cons(tco_apply(shen_assignx45types, [Cons(car(cdr(KL_ARG_V779_221)), KL_ARG_V777_219), KL_ARG_V778_220, car(cdr(cdr(KL_ARG_V779_221)))]), nil))) if ((((shen_eq(nil, cdr(cdr(cdr(KL_ARG_V779_221)))) if shen_consp(cdr(cdr(KL_ARG_V779_221))) else False) if shen_consp(cdr(KL_ARG_V779_221)) else False) if shen_eq(symdic.symdic_kl_lambda, car(KL_ARG_V779_221)) else False) if shen_consp(KL_ARG_V779_221) else False) else (Cons(symdic.symdic_kl_cond, tco_apply(kl_map, [(lambda KL_ARG_Y_222: Cons(tco_apply(shen_assignx45types, [KL_ARG_V777_219, KL_ARG_V778_220, car(KL_ARG_Y_222)]), Cons(tco_apply(shen_assignx45types, [KL_ARG_V777_219, KL_ARG_V778_220, car(cdr(KL_ARG_Y_222))]), nil))), cdr(KL_ARG_V779_221)])) if (shen_eq(symdic.symdic_kl_cond, car(KL_ARG_V779_221)) if shen_consp(KL_ARG_V779_221) else False) else ([setattr(KL_CTX, 'KL_LOC_NewTable_223', tco_apply(shen_typextable, [tco_apply(shen_getx45type, [car(KL_ARG_V779_221)]), cdr(KL_ARG_V779_221)])), Cons(car(KL_ARG_V779_221), tco_apply(kl_map, [(lambda KL_ARG_Y_224: tail_call(shen_assignx45types, [KL_ARG_V777_219, tco_apply(kl_append, [KL_ARG_V778_220, KL_CTX.KL_LOC_NewTable_223]), KL_ARG_Y_224])), cdr(KL_ARG_V779_221)]))][(-1)] if shen_consp(KL_ARG_V779_221) else ([setattr(KL_CTX, 'KL_LOC_AtomType_225', tco_apply(kl_assoc, [KL_ARG_V779_221, KL_ARG_V778_220])), (Cons(symdic.symdic_kl_type, Cons(KL_ARG_V779_221, Cons(cdr(KL_CTX.KL_LOC_AtomType_225), nil))) if shen_consp(KL_CTX.KL_LOC_AtomType_225) else (KL_ARG_V779_221 if tco_apply(kl_elementx63, [KL_ARG_V779_221, KL_ARG_V777_219]) else tail_call(shen_atomx45type, [KL_ARG_V779_221])))][(-1)] if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.assign-types', shen_assignx45types, 3)

@tail_recursion
def shen_atomx45type(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_atomx45type, (FUN_ARGS + lambdaargs)))
    KL_ARG_V780_226 = FUN_ARGS[0]
    global symdic
    return (Cons(symdic.symdic_kl_type, Cons(KL_ARG_V780_226, Cons(symdic.symdic_kl_string, nil))) if isinstance(KL_ARG_V780_226, str) else (Cons(symdic.symdic_kl_type, Cons(KL_ARG_V780_226, Cons(symdic.symdic_kl_number, nil))) if isinstance(KL_ARG_V780_226, numbers.Number) else (Cons(symdic.symdic_kl_type, Cons(KL_ARG_V780_226, Cons(symdic.symdic_kl_boolean, nil))) if tco_apply(kl_booleanx63, [KL_ARG_V780_226]) else (Cons(symdic.symdic_kl_type, Cons(KL_ARG_V780_226, Cons(symdic.symdic_kl_symbol, nil))) if tco_apply(kl_symbolx63, [KL_ARG_V780_226]) else KL_ARG_V780_226))))
shen_add_fun('shen.atom-type', shen_atomx45type, 1)

@tail_recursion
def shen_storex45arity(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_storex45arity, (FUN_ARGS + lambdaargs)))
    KL_ARG_V783_227 = FUN_ARGS[0]
    KL_ARG_V784_228 = FUN_ARGS[1]
    global symdic
    return (symdic.symdic_shen_skip if shen_get(symdic.symdic_shen_x42installingx45klx42) else (tail_call(kl_put, [KL_ARG_V783_227, symdic.symdic_kl_arity, KL_ARG_V784_228, shen_get(symdic.symdic_kl_x42propertyx45vectorx42)]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.store-arity', shen_storex45arity, 2)

@tail_recursion
def shen_reduce(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_reduce, (FUN_ARGS + lambdaargs)))
    KL_ARG_V785_229 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_230 = None
    KL_CTX = KL_Context()
    global symdic
    return [shen_set(symdic.symdic_shen_x42teststackx42, nil), [setattr(KL_CTX, 'KL_LOC_Result_230', tco_apply(shen_reduce_help, [KL_ARG_V785_229])), Cons(Cons(symdic.symdic_kl_x58, Cons(symdic.symdic_shen_tests, tco_apply(kl_reverse, [shen_get(symdic.symdic_shen_x42teststackx42)]))), Cons(KL_CTX.KL_LOC_Result_230, nil))][(-1)]][(-1)]
shen_add_fun('shen.reduce', shen_reduce, 1)

@tail_recursion
def shen_reduce_help(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_reduce_help, (FUN_ARGS + lambdaargs)))
    KL_ARG_V786_231 = FUN_ARGS[0]

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
    return ([tco_apply(shen_add_test, [Cons(symdic.symdic_kl_consx63, cdr(KL_ARG_V786_231))]), [setattr(KL_CTX, 'KL_LOC_Abstraction_232', Cons(symdic.symdic_kl_x47_, Cons(car(cdr(car(cdr(car(KL_ARG_V786_231))))), Cons(Cons(symdic.symdic_kl_x47_, Cons(car(cdr(cdr(car(cdr(car(KL_ARG_V786_231)))))), Cons(tco_apply(shen_ebr, [car(cdr(KL_ARG_V786_231)), car(cdr(car(KL_ARG_V786_231))), car(cdr(cdr(car(KL_ARG_V786_231))))]), nil))), nil)))), [setattr(KL_CTX, 'KL_LOC_Application_233', Cons(Cons(KL_CTX.KL_LOC_Abstraction_232, Cons(Cons(symdic.symdic_kl_hd, cdr(KL_ARG_V786_231)), nil)), Cons(Cons(symdic.symdic_kl_tl, cdr(KL_ARG_V786_231)), nil))), tail_call(shen_reduce_help, [KL_CTX.KL_LOC_Application_233])][(-1)]][(-1)]][(-1)] if ((((((((((((shen_eq(nil, cdr(cdr(KL_ARG_V786_231))) if shen_consp(cdr(KL_ARG_V786_231)) else False) if shen_eq(nil, cdr(cdr(cdr(car(KL_ARG_V786_231))))) else False) if shen_consp(cdr(cdr(car(KL_ARG_V786_231)))) else False) if shen_eq(nil, cdr(cdr(cdr(car(cdr(car(KL_ARG_V786_231))))))) else False) if shen_consp(cdr(cdr(car(cdr(car(KL_ARG_V786_231)))))) else False) if shen_consp(cdr(car(cdr(car(KL_ARG_V786_231))))) else False) if shen_eq(symdic.symdic_kl_cons, car(car(cdr(car(KL_ARG_V786_231))))) else False) if shen_consp(car(cdr(car(KL_ARG_V786_231)))) else False) if shen_consp(cdr(car(KL_ARG_V786_231))) else False) if shen_eq(symdic.symdic_kl_x47_, car(car(KL_ARG_V786_231))) else False) if shen_consp(car(KL_ARG_V786_231)) else False) if shen_consp(KL_ARG_V786_231) else False) else ([tco_apply(shen_add_test, [Cons(symdic.symdic_kl_tuplex63, cdr(KL_ARG_V786_231))]), [setattr(KL_CTX, 'KL_LOC_Abstraction_234', Cons(symdic.symdic_kl_x47_, Cons(car(cdr(car(cdr(car(KL_ARG_V786_231))))), Cons(Cons(symdic.symdic_kl_x47_, Cons(car(cdr(cdr(car(cdr(car(KL_ARG_V786_231)))))), Cons(tco_apply(shen_ebr, [car(cdr(KL_ARG_V786_231)), car(cdr(car(KL_ARG_V786_231))), car(cdr(cdr(car(KL_ARG_V786_231))))]), nil))), nil)))), [setattr(KL_CTX, 'KL_LOC_Application_235', Cons(Cons(KL_CTX.KL_LOC_Abstraction_234, Cons(Cons(symdic.symdic_kl_fst, cdr(KL_ARG_V786_231)), nil)), Cons(Cons(symdic.symdic_kl_snd, cdr(KL_ARG_V786_231)), nil))), tail_call(shen_reduce_help, [KL_CTX.KL_LOC_Application_235])][(-1)]][(-1)]][(-1)] if ((((((((((((shen_eq(nil, cdr(cdr(KL_ARG_V786_231))) if shen_consp(cdr(KL_ARG_V786_231)) else False) if shen_eq(nil, cdr(cdr(cdr(car(KL_ARG_V786_231))))) else False) if shen_consp(cdr(cdr(car(KL_ARG_V786_231)))) else False) if shen_eq(nil, cdr(cdr(cdr(car(cdr(car(KL_ARG_V786_231))))))) else False) if shen_consp(cdr(cdr(car(cdr(car(KL_ARG_V786_231)))))) else False) if shen_consp(cdr(car(cdr(car(KL_ARG_V786_231))))) else False) if shen_eq(symdic.symdic_kl_x64p, car(car(cdr(car(KL_ARG_V786_231))))) else False) if shen_consp(car(cdr(car(KL_ARG_V786_231)))) else False) if shen_consp(cdr(car(KL_ARG_V786_231))) else False) if shen_eq(symdic.symdic_kl_x47_, car(car(KL_ARG_V786_231))) else False) if shen_consp(car(KL_ARG_V786_231)) else False) if shen_consp(KL_ARG_V786_231) else False) else ([tco_apply(shen_add_test, [Cons(symdic.symdic_shen_x43vectorx63, cdr(KL_ARG_V786_231))]), [setattr(KL_CTX, 'KL_LOC_Abstraction_236', Cons(symdic.symdic_kl_x47_, Cons(car(cdr(car(cdr(car(KL_ARG_V786_231))))), Cons(Cons(symdic.symdic_kl_x47_, Cons(car(cdr(cdr(car(cdr(car(KL_ARG_V786_231)))))), Cons(tco_apply(shen_ebr, [car(cdr(KL_ARG_V786_231)), car(cdr(car(KL_ARG_V786_231))), car(cdr(cdr(car(KL_ARG_V786_231))))]), nil))), nil)))), [setattr(KL_CTX, 'KL_LOC_Application_237', Cons(Cons(KL_CTX.KL_LOC_Abstraction_236, Cons(Cons(symdic.symdic_kl_hdv, cdr(KL_ARG_V786_231)), nil)), Cons(Cons(symdic.symdic_kl_tlv, cdr(KL_ARG_V786_231)), nil))), tail_call(shen_reduce_help, [KL_CTX.KL_LOC_Application_237])][(-1)]][(-1)]][(-1)] if ((((((((((((shen_eq(nil, cdr(cdr(KL_ARG_V786_231))) if shen_consp(cdr(KL_ARG_V786_231)) else False) if shen_eq(nil, cdr(cdr(cdr(car(KL_ARG_V786_231))))) else False) if shen_consp(cdr(cdr(car(KL_ARG_V786_231)))) else False) if shen_eq(nil, cdr(cdr(cdr(car(cdr(car(KL_ARG_V786_231))))))) else False) if shen_consp(cdr(cdr(car(cdr(car(KL_ARG_V786_231)))))) else False) if shen_consp(cdr(car(cdr(car(KL_ARG_V786_231))))) else False) if shen_eq(symdic.symdic_kl_x64v, car(car(cdr(car(KL_ARG_V786_231))))) else False) if shen_consp(car(cdr(car(KL_ARG_V786_231)))) else False) if shen_consp(cdr(car(KL_ARG_V786_231))) else False) if shen_eq(symdic.symdic_kl_x47_, car(car(KL_ARG_V786_231))) else False) if shen_consp(car(KL_ARG_V786_231)) else False) if shen_consp(KL_ARG_V786_231) else False) else ([tco_apply(shen_add_test, [Cons(symdic.symdic_shen_x43stringx63, cdr(KL_ARG_V786_231))]), [setattr(KL_CTX, 'KL_LOC_Abstraction_238', Cons(symdic.symdic_kl_x47_, Cons(car(cdr(car(cdr(car(KL_ARG_V786_231))))), Cons(Cons(symdic.symdic_kl_x47_, Cons(car(cdr(cdr(car(cdr(car(KL_ARG_V786_231)))))), Cons(tco_apply(shen_ebr, [car(cdr(KL_ARG_V786_231)), car(cdr(car(KL_ARG_V786_231))), car(cdr(cdr(car(KL_ARG_V786_231))))]), nil))), nil)))), [setattr(KL_CTX, 'KL_LOC_Application_239', Cons(Cons(KL_CTX.KL_LOC_Abstraction_238, Cons(Cons(symdic.symdic_kl_pos, Cons(car(cdr(KL_ARG_V786_231)), Cons(0, nil))), nil)), Cons(Cons(symdic.symdic_kl_tlstr, cdr(KL_ARG_V786_231)), nil))), tail_call(shen_reduce_help, [KL_CTX.KL_LOC_Application_239])][(-1)]][(-1)]][(-1)] if ((((((((((((shen_eq(nil, cdr(cdr(KL_ARG_V786_231))) if shen_consp(cdr(KL_ARG_V786_231)) else False) if shen_eq(nil, cdr(cdr(cdr(car(KL_ARG_V786_231))))) else False) if shen_consp(cdr(cdr(car(KL_ARG_V786_231)))) else False) if shen_eq(nil, cdr(cdr(cdr(car(cdr(car(KL_ARG_V786_231))))))) else False) if shen_consp(cdr(cdr(car(cdr(car(KL_ARG_V786_231)))))) else False) if shen_consp(cdr(car(cdr(car(KL_ARG_V786_231))))) else False) if shen_eq(symdic.symdic_kl_x64s, car(car(cdr(car(KL_ARG_V786_231))))) else False) if shen_consp(car(cdr(car(KL_ARG_V786_231)))) else False) if shen_consp(cdr(car(KL_ARG_V786_231))) else False) if shen_eq(symdic.symdic_kl_x47_, car(car(KL_ARG_V786_231))) else False) if shen_consp(car(KL_ARG_V786_231)) else False) if shen_consp(KL_ARG_V786_231) else False) else ([tco_apply(shen_add_test, [Cons(symdic.symdic_kl_x61, Cons(car(cdr(car(KL_ARG_V786_231))), cdr(KL_ARG_V786_231)))]), tail_call(shen_reduce_help, [car(cdr(cdr(car(KL_ARG_V786_231))))])][(-1)] if (((((((((not tco_apply(kl_variablex63, [car(cdr(car(KL_ARG_V786_231)))])) if shen_eq(nil, cdr(cdr(KL_ARG_V786_231))) else False) if shen_consp(cdr(KL_ARG_V786_231)) else False) if shen_eq(nil, cdr(cdr(cdr(car(KL_ARG_V786_231))))) else False) if shen_consp(cdr(cdr(car(KL_ARG_V786_231)))) else False) if shen_consp(cdr(car(KL_ARG_V786_231))) else False) if shen_eq(symdic.symdic_kl_x47_, car(car(KL_ARG_V786_231))) else False) if shen_consp(car(KL_ARG_V786_231)) else False) if shen_consp(KL_ARG_V786_231) else False) else (tail_call(shen_reduce_help, [tco_apply(shen_ebr, [car(cdr(KL_ARG_V786_231)), car(cdr(car(KL_ARG_V786_231))), car(cdr(cdr(car(KL_ARG_V786_231))))])]) if (((((((shen_eq(nil, cdr(cdr(KL_ARG_V786_231))) if shen_consp(cdr(KL_ARG_V786_231)) else False) if shen_eq(nil, cdr(cdr(cdr(car(KL_ARG_V786_231))))) else False) if shen_consp(cdr(cdr(car(KL_ARG_V786_231)))) else False) if shen_consp(cdr(car(KL_ARG_V786_231))) else False) if shen_eq(symdic.symdic_kl_x47_, car(car(KL_ARG_V786_231))) else False) if shen_consp(car(KL_ARG_V786_231)) else False) if shen_consp(KL_ARG_V786_231) else False) else ([tco_apply(shen_add_test, [car(cdr(KL_ARG_V786_231))]), tail_call(shen_reduce_help, [car(cdr(cdr(KL_ARG_V786_231)))])][(-1)] if ((((shen_eq(nil, cdr(cdr(cdr(KL_ARG_V786_231)))) if shen_consp(cdr(cdr(KL_ARG_V786_231))) else False) if shen_consp(cdr(KL_ARG_V786_231)) else False) if shen_eq(symdic.symdic_kl_where, car(KL_ARG_V786_231)) else False) if shen_consp(KL_ARG_V786_231) else False) else ([setattr(KL_CTX, 'KL_LOC_Z_240', tco_apply(shen_reduce_help, [car(KL_ARG_V786_231)])), (KL_ARG_V786_231 if shen_eq(car(KL_ARG_V786_231), KL_CTX.KL_LOC_Z_240) else tail_call(shen_reduce_help, [Cons(KL_CTX.KL_LOC_Z_240, cdr(KL_ARG_V786_231))]))][(-1)] if ((shen_eq(nil, cdr(cdr(KL_ARG_V786_231))) if shen_consp(cdr(KL_ARG_V786_231)) else False) if shen_consp(KL_ARG_V786_231) else False) else (KL_ARG_V786_231 if True else shen_simple_error('condition failure'))))))))))
shen_add_fun('shen.reduce_help', shen_reduce_help, 1)

@tail_recursion
def shen_x43stringx63(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x43stringx63, (FUN_ARGS + lambdaargs)))
    KL_ARG_V787_241 = FUN_ARGS[0]
    global symdic
    return (False if shen_eq('', KL_ARG_V787_241) else (isinstance(KL_ARG_V787_241, str) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.+string?', shen_x43stringx63, 1)

@tail_recursion
def shen_x43vector(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x43vector, (FUN_ARGS + lambdaargs)))
    KL_ARG_V788_242 = FUN_ARGS[0]
    global symdic
    return (False if shen_eq(KL_ARG_V788_242, tco_apply(kl_vector, [0])) else (tail_call(kl_vectorx63, [KL_ARG_V788_242]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.+vector', shen_x43vector, 1)

@tail_recursion
def shen_ebr(*FUN_ARGS):
    FUN_ARITY = 3
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_ebr, (FUN_ARGS + lambdaargs)))
    KL_ARG_V797_243 = FUN_ARGS[0]
    KL_ARG_V798_244 = FUN_ARGS[1]
    KL_ARG_V799_245 = FUN_ARGS[2]
    global symdic
    return (KL_ARG_V797_243 if shen_eq(KL_ARG_V799_245, KL_ARG_V798_244) else (KL_ARG_V799_245 if ((((((tco_apply(kl_occurrences, [KL_ARG_V798_244, car(cdr(KL_ARG_V799_245))]) > 0) if shen_eq(nil, cdr(cdr(cdr(KL_ARG_V799_245)))) else False) if shen_consp(cdr(cdr(KL_ARG_V799_245))) else False) if shen_consp(cdr(KL_ARG_V799_245)) else False) if shen_eq(symdic.symdic_kl_x47_, car(KL_ARG_V799_245)) else False) if shen_consp(KL_ARG_V799_245) else False) else (Cons(symdic.symdic_kl_let, Cons(car(cdr(KL_ARG_V799_245)), Cons(tco_apply(shen_ebr, [KL_ARG_V797_243, car(cdr(KL_ARG_V799_245)), car(cdr(cdr(KL_ARG_V799_245)))]), cdr(cdr(cdr(KL_ARG_V799_245)))))) if ((((((shen_eq(car(cdr(KL_ARG_V799_245)), KL_ARG_V798_244) if shen_eq(nil, cdr(cdr(cdr(cdr(KL_ARG_V799_245))))) else False) if shen_consp(cdr(cdr(cdr(KL_ARG_V799_245)))) else False) if shen_consp(cdr(cdr(KL_ARG_V799_245))) else False) if shen_consp(cdr(KL_ARG_V799_245)) else False) if shen_eq(symdic.symdic_kl_let, car(KL_ARG_V799_245)) else False) if shen_consp(KL_ARG_V799_245) else False) else (Cons(tco_apply(shen_ebr, [KL_ARG_V797_243, KL_ARG_V798_244, car(KL_ARG_V799_245)]), tco_apply(shen_ebr, [KL_ARG_V797_243, KL_ARG_V798_244, cdr(KL_ARG_V799_245)])) if shen_consp(KL_ARG_V799_245) else (KL_ARG_V799_245 if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.ebr', shen_ebr, 3)

@tail_recursion
def shen_add_test(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_add_test, (FUN_ARGS + lambdaargs)))
    KL_ARG_V802_246 = FUN_ARGS[0]
    global symdic
    return shen_set(symdic.symdic_shen_x42teststackx42, Cons(KL_ARG_V802_246, shen_get(symdic.symdic_shen_x42teststackx42)))
shen_add_fun('shen.add_test', shen_add_test, 1)

@tail_recursion
def shen_condx45expression(*FUN_ARGS):
    FUN_ARITY = 3
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_condx45expression, (FUN_ARGS + lambdaargs)))
    KL_ARG_V803_247 = FUN_ARGS[0]
    KL_ARG_V804_248 = FUN_ARGS[1]
    KL_ARG_V805_249 = FUN_ARGS[2]

    class KL_Context:
        KL_LOC_Err_250 = None
        KL_LOC_Cases_251 = None
        KL_LOC_EncodeChoices_252 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Err_250', tco_apply(shen_errx45condition, [KL_ARG_V803_247])), [setattr(KL_CTX, 'KL_LOC_Cases_251', tco_apply(shen_casex45form, [KL_ARG_V805_249, KL_CTX.KL_LOC_Err_250])), [setattr(KL_CTX, 'KL_LOC_EncodeChoices_252', tco_apply(shen_encodex45choices, [KL_CTX.KL_LOC_Cases_251, KL_ARG_V803_247])), tail_call(shen_condx45form, [KL_CTX.KL_LOC_EncodeChoices_252])][(-1)]][(-1)]][(-1)]
shen_add_fun('shen.cond-expression', shen_condx45expression, 3)

@tail_recursion
def shen_condx45form(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_condx45form, (FUN_ARGS + lambdaargs)))
    KL_ARG_V808_253 = FUN_ARGS[0]
    global symdic
    return (car(cdr(car(KL_ARG_V808_253))) if ((((shen_eq(nil, cdr(cdr(car(KL_ARG_V808_253)))) if shen_consp(cdr(car(KL_ARG_V808_253))) else False) if shen_eq(True, car(car(KL_ARG_V808_253))) else False) if shen_consp(car(KL_ARG_V808_253)) else False) if shen_consp(KL_ARG_V808_253) else False) else (Cons(symdic.symdic_kl_cond, KL_ARG_V808_253) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.cond-form', shen_condx45form, 1)

@tail_recursion
def shen_encodex45choices(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_encodex45choices, (FUN_ARGS + lambdaargs)))
    KL_ARG_V811_254 = FUN_ARGS[0]
    KL_ARG_V812_255 = FUN_ARGS[1]
    global symdic
    return (nil if shen_eq(nil, KL_ARG_V811_254) else (Cons(Cons(True, Cons(Cons(symdic.symdic_kl_let, Cons(symdic.symdic_Result, Cons(car(cdr(car(cdr(car(KL_ARG_V811_254))))), Cons(Cons(symdic.symdic_kl_if, Cons(Cons(symdic.symdic_kl_x61, Cons(symdic.symdic_Result, Cons(Cons(symdic.symdic_kl_fail, nil), nil))), Cons((Cons(symdic.symdic_shen_sysx45error, Cons(KL_ARG_V812_255, nil)) if shen_get(symdic.symdic_shen_x42installingx45klx42) else Cons(symdic.symdic_shen_f_error, Cons(KL_ARG_V812_255, nil))), Cons(symdic.symdic_Result, nil)))), nil)))), nil)), nil) if (((((((((shen_eq(nil, cdr(KL_ARG_V811_254)) if shen_eq(nil, cdr(cdr(car(KL_ARG_V811_254)))) else False) if shen_eq(nil, cdr(cdr(car(cdr(car(KL_ARG_V811_254)))))) else False) if shen_consp(cdr(car(cdr(car(KL_ARG_V811_254))))) else False) if shen_eq(symdic.symdic_shen_choicepointx33, car(car(cdr(car(KL_ARG_V811_254))))) else False) if shen_consp(car(cdr(car(KL_ARG_V811_254)))) else False) if shen_consp(cdr(car(KL_ARG_V811_254))) else False) if shen_eq(True, car(car(KL_ARG_V811_254))) else False) if shen_consp(car(KL_ARG_V811_254)) else False) if shen_consp(KL_ARG_V811_254) else False) else (Cons(Cons(True, Cons(Cons(symdic.symdic_kl_let, Cons(symdic.symdic_Result, Cons(car(cdr(car(cdr(car(KL_ARG_V811_254))))), Cons(Cons(symdic.symdic_kl_if, Cons(Cons(symdic.symdic_kl_x61, Cons(symdic.symdic_Result, Cons(Cons(symdic.symdic_kl_fail, nil), nil))), Cons(tco_apply(shen_condx45form, [tco_apply(shen_encodex45choices, [cdr(KL_ARG_V811_254), KL_ARG_V812_255])]), Cons(symdic.symdic_Result, nil)))), nil)))), nil)), nil) if ((((((((shen_eq(nil, cdr(cdr(car(KL_ARG_V811_254)))) if shen_eq(nil, cdr(cdr(car(cdr(car(KL_ARG_V811_254)))))) else False) if shen_consp(cdr(car(cdr(car(KL_ARG_V811_254))))) else False) if shen_eq(symdic.symdic_shen_choicepointx33, car(car(cdr(car(KL_ARG_V811_254))))) else False) if shen_consp(car(cdr(car(KL_ARG_V811_254)))) else False) if shen_consp(cdr(car(KL_ARG_V811_254))) else False) if shen_eq(True, car(car(KL_ARG_V811_254))) else False) if shen_consp(car(KL_ARG_V811_254)) else False) if shen_consp(KL_ARG_V811_254) else False) else (Cons(Cons(True, Cons(Cons(symdic.symdic_kl_let, Cons(symdic.symdic_Freeze, Cons(Cons(symdic.symdic_kl_freeze, Cons(tco_apply(shen_condx45form, [tco_apply(shen_encodex45choices, [cdr(KL_ARG_V811_254), KL_ARG_V812_255])]), nil)), Cons(Cons(symdic.symdic_kl_if, Cons(car(car(KL_ARG_V811_254)), Cons(Cons(symdic.symdic_kl_let, Cons(symdic.symdic_Result, Cons(car(cdr(car(cdr(car(KL_ARG_V811_254))))), Cons(Cons(symdic.symdic_kl_if, Cons(Cons(symdic.symdic_kl_x61, Cons(symdic.symdic_Result, Cons(Cons(symdic.symdic_kl_fail, nil), nil))), Cons(Cons(symdic.symdic_kl_thaw, Cons(symdic.symdic_Freeze, nil)), Cons(symdic.symdic_Result, nil)))), nil)))), Cons(Cons(symdic.symdic_kl_thaw, Cons(symdic.symdic_Freeze, nil)), nil)))), nil)))), nil)), nil) if (((((((shen_eq(nil, cdr(cdr(car(KL_ARG_V811_254)))) if shen_eq(nil, cdr(cdr(car(cdr(car(KL_ARG_V811_254)))))) else False) if shen_consp(cdr(car(cdr(car(KL_ARG_V811_254))))) else False) if shen_eq(symdic.symdic_shen_choicepointx33, car(car(cdr(car(KL_ARG_V811_254))))) else False) if shen_consp(car(cdr(car(KL_ARG_V811_254)))) else False) if shen_consp(cdr(car(KL_ARG_V811_254))) else False) if shen_consp(car(KL_ARG_V811_254)) else False) if shen_consp(KL_ARG_V811_254) else False) else (Cons(car(KL_ARG_V811_254), tco_apply(shen_encodex45choices, [cdr(KL_ARG_V811_254), KL_ARG_V812_255])) if (((shen_eq(nil, cdr(cdr(car(KL_ARG_V811_254)))) if shen_consp(cdr(car(KL_ARG_V811_254))) else False) if shen_consp(car(KL_ARG_V811_254)) else False) if shen_consp(KL_ARG_V811_254) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_encodex45choices]) if True else shen_simple_error('condition failure')))))))
shen_add_fun('shen.encode-choices', shen_encodex45choices, 2)

@tail_recursion
def shen_casex45form(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_casex45form, (FUN_ARGS + lambdaargs)))
    KL_ARG_V817_256 = FUN_ARGS[0]
    KL_ARG_V818_257 = FUN_ARGS[1]
    global symdic
    return (Cons(KL_ARG_V818_257, nil) if shen_eq(nil, KL_ARG_V817_256) else (Cons(Cons(True, cdr(car(KL_ARG_V817_256))), tco_apply(shen_casex45form, [cdr(KL_ARG_V817_256), KL_ARG_V818_257])) if ((((((((((((shen_eq(nil, cdr(cdr(car(KL_ARG_V817_256)))) if shen_eq(nil, cdr(cdr(car(cdr(car(KL_ARG_V817_256)))))) else False) if shen_consp(cdr(car(cdr(car(KL_ARG_V817_256))))) else False) if shen_eq(symdic.symdic_shen_choicepointx33, car(car(cdr(car(KL_ARG_V817_256))))) else False) if shen_consp(car(cdr(car(KL_ARG_V817_256)))) else False) if shen_consp(cdr(car(KL_ARG_V817_256))) else False) if shen_eq(nil, cdr(cdr(car(car(KL_ARG_V817_256))))) else False) if shen_eq(symdic.symdic_shen_tests, car(cdr(car(car(KL_ARG_V817_256))))) else False) if shen_consp(cdr(car(car(KL_ARG_V817_256)))) else False) if shen_eq(symdic.symdic_kl_x58, car(car(car(KL_ARG_V817_256)))) else False) if shen_consp(car(car(KL_ARG_V817_256))) else False) if shen_consp(car(KL_ARG_V817_256)) else False) if shen_consp(KL_ARG_V817_256) else False) else (Cons(Cons(True, cdr(car(KL_ARG_V817_256))), nil) if ((((((((shen_eq(nil, cdr(cdr(car(KL_ARG_V817_256)))) if shen_consp(cdr(car(KL_ARG_V817_256))) else False) if shen_eq(nil, cdr(cdr(car(car(KL_ARG_V817_256))))) else False) if shen_eq(symdic.symdic_shen_tests, car(cdr(car(car(KL_ARG_V817_256))))) else False) if shen_consp(cdr(car(car(KL_ARG_V817_256)))) else False) if shen_eq(symdic.symdic_kl_x58, car(car(car(KL_ARG_V817_256)))) else False) if shen_consp(car(car(KL_ARG_V817_256))) else False) if shen_consp(car(KL_ARG_V817_256)) else False) if shen_consp(KL_ARG_V817_256) else False) else (Cons(Cons(tco_apply(shen_embedx45and, [cdr(cdr(car(car(KL_ARG_V817_256))))]), cdr(car(KL_ARG_V817_256))), tco_apply(shen_casex45form, [cdr(KL_ARG_V817_256), KL_ARG_V818_257])) if (((((((shen_eq(nil, cdr(cdr(car(KL_ARG_V817_256)))) if shen_consp(cdr(car(KL_ARG_V817_256))) else False) if shen_eq(symdic.symdic_shen_tests, car(cdr(car(car(KL_ARG_V817_256))))) else False) if shen_consp(cdr(car(car(KL_ARG_V817_256)))) else False) if shen_eq(symdic.symdic_kl_x58, car(car(car(KL_ARG_V817_256)))) else False) if shen_consp(car(car(KL_ARG_V817_256))) else False) if shen_consp(car(KL_ARG_V817_256)) else False) if shen_consp(KL_ARG_V817_256) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_casex45form]) if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.case-form', shen_casex45form, 2)

@tail_recursion
def shen_embedx45and(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_embedx45and, (FUN_ARGS + lambdaargs)))
    KL_ARG_V819_258 = FUN_ARGS[0]
    global symdic
    return (car(KL_ARG_V819_258) if (shen_eq(nil, cdr(KL_ARG_V819_258)) if shen_consp(KL_ARG_V819_258) else False) else (Cons(symdic.symdic_kl_and, Cons(car(KL_ARG_V819_258), Cons(tco_apply(shen_embedx45and, [cdr(KL_ARG_V819_258)]), nil))) if shen_consp(KL_ARG_V819_258) else (tail_call(shen_sysx45error, [symdic.symdic_shen_embedx45and]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.embed-and', shen_embedx45and, 1)

@tail_recursion
def shen_errx45condition(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_errx45condition, (FUN_ARGS + lambdaargs)))
    KL_ARG_V820_259 = FUN_ARGS[0]
    global symdic
    return Cons(True, Cons(Cons(symdic.symdic_shen_f_error, Cons(KL_ARG_V820_259, nil)), nil))
shen_add_fun('shen.err-condition', shen_errx45condition, 1)

@tail_recursion
def shen_sysx45error(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_sysx45error, (FUN_ARGS + lambdaargs)))
    KL_ARG_V821_260 = FUN_ARGS[0]
    global symdic
    return shen_simple_error(('system function ' + tco_apply(shen_app, [KL_ARG_V821_260, ': unexpected argument\r\n', symdic.symdic_shen_a])))
shen_add_fun('shen.sys-error', shen_sysx45error, 1)


#============================== sys.kl==============================



@tail_recursion
def kl_thaw(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_thaw, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1802_261 = FUN_ARGS[0]
    global symdic
    return shen_apply(KL_ARG_V1802_261, [])
shen_add_fun('thaw', kl_thaw, 1)

@tail_recursion
def kl_eval(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_eval, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1803_262 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Macroexpand_263 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Macroexpand_263', tco_apply(shen_walk, [(lambda KL_ARG_V1800_264: tail_call(kl_macroexpand, [KL_ARG_V1800_264])), KL_ARG_V1803_262])), (tail_call(kl_map, [symdic.symdic_shen_evalx45withoutx45macros, tco_apply(shen_packagex45contents, [KL_CTX.KL_LOC_Macroexpand_263])]) if tco_apply(shen_packagedx63, [KL_CTX.KL_LOC_Macroexpand_263]) else tail_call(shen_evalx45withoutx45macros, [KL_CTX.KL_LOC_Macroexpand_263]))][(-1)]
shen_add_fun('eval', kl_eval, 1)

@tail_recursion
def shen_evalx45withoutx45macros(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_evalx45withoutx45macros, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1804_265 = FUN_ARGS[0]
    global symdic
    return shen_eval_kl(tco_apply(shen_elimx45define, [tco_apply(shen_procx45inputx43, [KL_ARG_V1804_265])]))
shen_add_fun('shen.eval-without-macros', shen_evalx45withoutx45macros, 1)

@tail_recursion
def shen_procx45inputx43(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_procx45inputx43, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1805_266 = FUN_ARGS[0]
    global symdic
    return (Cons(symdic.symdic_kl_inputx43, Cons(car(cdr(KL_ARG_V1805_266)), Cons(tco_apply(shen_rcons_form, [car(cdr(cdr(KL_ARG_V1805_266)))]), nil))) if ((((shen_eq(nil, cdr(cdr(cdr(KL_ARG_V1805_266)))) if shen_consp(cdr(cdr(KL_ARG_V1805_266))) else False) if shen_consp(cdr(KL_ARG_V1805_266)) else False) if shen_eq(symdic.symdic_kl_inputx43, car(KL_ARG_V1805_266)) else False) if shen_consp(KL_ARG_V1805_266) else False) else (Cons(symdic.symdic_readx43, Cons(car(cdr(KL_ARG_V1805_266)), Cons(tco_apply(shen_rcons_form, [car(cdr(cdr(KL_ARG_V1805_266)))]), nil))) if ((((shen_eq(nil, cdr(cdr(cdr(KL_ARG_V1805_266)))) if shen_consp(cdr(cdr(KL_ARG_V1805_266))) else False) if shen_consp(cdr(KL_ARG_V1805_266)) else False) if shen_eq(symdic.symdic_readx43, car(KL_ARG_V1805_266)) else False) if shen_consp(KL_ARG_V1805_266) else False) else (tail_call(kl_map, [symdic.symdic_shen_procx45inputx43, KL_ARG_V1805_266]) if shen_consp(KL_ARG_V1805_266) else (KL_ARG_V1805_266 if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.proc-input+', shen_procx45inputx43, 1)

@tail_recursion
def shen_elimx45define(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_elimx45define, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1806_267 = FUN_ARGS[0]
    global symdic
    return (tail_call(shen_shenx45x62kl, [car(cdr(KL_ARG_V1806_267)), cdr(cdr(KL_ARG_V1806_267))]) if ((shen_consp(cdr(KL_ARG_V1806_267)) if shen_eq(symdic.symdic_kl_define, car(KL_ARG_V1806_267)) else False) if shen_consp(KL_ARG_V1806_267) else False) else (tail_call(shen_elimx45define, [tco_apply(shen_yacc, [KL_ARG_V1806_267])]) if ((shen_consp(cdr(KL_ARG_V1806_267)) if shen_eq(symdic.symdic_kl_defcc, car(KL_ARG_V1806_267)) else False) if shen_consp(KL_ARG_V1806_267) else False) else (tail_call(kl_map, [symdic.symdic_shen_elimx45define, KL_ARG_V1806_267]) if shen_consp(KL_ARG_V1806_267) else (KL_ARG_V1806_267 if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.elim-define', shen_elimx45define, 1)

@tail_recursion
def shen_packagedx63(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_packagedx63, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1813_268 = FUN_ARGS[0]
    global symdic
    return (True if (((shen_consp(cdr(cdr(KL_ARG_V1813_268))) if shen_consp(cdr(KL_ARG_V1813_268)) else False) if shen_eq(symdic.symdic_kl_package, car(KL_ARG_V1813_268)) else False) if shen_consp(KL_ARG_V1813_268) else False) else (False if True else shen_simple_error('condition failure')))
shen_add_fun('shen.packaged?', shen_packagedx63, 1)

@tail_recursion
def kl_external(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_external, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1814_269 = FUN_ARGS[0]
    global symdic
    return shen_try_except((lambda : tco_apply(kl_get, [KL_ARG_V1814_269, symdic.symdic_shen_externalx45symbols, shen_get(symdic.symdic_kl_x42propertyx45vectorx42)])), (lambda KL_ARG_E_270: shen_simple_error(('package ' + tco_apply(shen_app, [KL_ARG_V1814_269, ' has not been used.\r\n', symdic.symdic_shen_a])))))
shen_add_fun('external', kl_external, 1)

@tail_recursion
def shen_packagex45contents(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_packagex45contents, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1817_271 = FUN_ARGS[0]
    global symdic
    return (cdr(cdr(cdr(KL_ARG_V1817_271))) if ((((shen_consp(cdr(cdr(KL_ARG_V1817_271))) if shen_eq(symdic.symdic_kl_null, car(cdr(KL_ARG_V1817_271))) else False) if shen_consp(cdr(KL_ARG_V1817_271)) else False) if shen_eq(symdic.symdic_kl_package, car(KL_ARG_V1817_271)) else False) if shen_consp(KL_ARG_V1817_271) else False) else (tail_call(shen_packageh, [car(cdr(KL_ARG_V1817_271)), car(cdr(cdr(KL_ARG_V1817_271))), cdr(cdr(cdr(KL_ARG_V1817_271)))]) if (((shen_consp(cdr(cdr(KL_ARG_V1817_271))) if shen_consp(cdr(KL_ARG_V1817_271)) else False) if shen_eq(symdic.symdic_kl_package, car(KL_ARG_V1817_271)) else False) if shen_consp(KL_ARG_V1817_271) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_packagex45contents]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.package-contents', shen_packagex45contents, 1)

@tail_recursion
def shen_walk(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_walk, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1818_272 = FUN_ARGS[0]
    KL_ARG_V1819_273 = FUN_ARGS[1]
    global symdic
    return (shen_apply(KL_ARG_V1818_272, [tco_apply(kl_map, [(lambda KL_ARG_Z_274: tail_call(shen_walk, [KL_ARG_V1818_272, KL_ARG_Z_274])), KL_ARG_V1819_273])]) if shen_consp(KL_ARG_V1819_273) else (shen_apply(KL_ARG_V1818_272, [KL_ARG_V1819_273]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.walk', shen_walk, 2)

@tail_recursion
def kl_compile(*FUN_ARGS):
    FUN_ARITY = 3
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_compile, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1820_275 = FUN_ARGS[0]
    KL_ARG_V1821_276 = FUN_ARGS[1]
    KL_ARG_V1822_277 = FUN_ARGS[2]

    class KL_Context:
        KL_LOC_O_278 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_O_278', shen_apply(KL_ARG_V1820_275, [Cons(KL_ARG_V1821_276, Cons(nil, nil))])), (shen_apply(KL_ARG_V1822_277, [KL_CTX.KL_LOC_O_278]) if (True if shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_O_278) else (not tco_apply(kl_emptyx63, [car(KL_CTX.KL_LOC_O_278)]))) else tail_call(shen_hdtl, [KL_CTX.KL_LOC_O_278]))][(-1)]
shen_add_fun('compile', kl_compile, 3)

@tail_recursion
def kl_failx45if(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_failx45if, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1823_279 = FUN_ARGS[0]
    KL_ARG_V1824_280 = FUN_ARGS[1]
    global symdic
    return (tail_call(kl_fail, []) if shen_apply(KL_ARG_V1823_279, [KL_ARG_V1824_280]) else KL_ARG_V1824_280)
shen_add_fun('fail-if', kl_failx45if, 2)

@tail_recursion
def kl_x64s(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_x64s, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1825_281 = FUN_ARGS[0]
    KL_ARG_V1826_282 = FUN_ARGS[1]
    global symdic
    return (KL_ARG_V1825_281 + KL_ARG_V1826_282)
shen_add_fun('@s', kl_x64s, 2)

@tail_recursion
def kl_tcx63(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_tcx63, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1831_283 = FUN_ARGS[0]
    global symdic
    return shen_get(symdic.symdic_shen_x42tcx42)
shen_add_fun('tc?', kl_tcx63, 1)

@tail_recursion
def kl_ps(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_ps, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1832_284 = FUN_ARGS[0]
    global symdic
    return shen_try_except((lambda : tco_apply(kl_get, [KL_ARG_V1832_284, symdic.symdic_shen_source, shen_get(symdic.symdic_kl_x42propertyx45vectorx42)])), (lambda KL_ARG_E_285: shen_simple_error(tco_apply(shen_app, [KL_ARG_V1832_284, ' not found.\r\n', symdic.symdic_shen_a]))))
shen_add_fun('ps', kl_ps, 1)

@tail_recursion
def kl_stinput(*FUN_ARGS):
    FUN_ARITY = 0
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_stinput, (FUN_ARGS + lambdaargs)))
    global symdic
    return shen_get(symdic.symdic_kl_x42stinputx42)
shen_add_fun('stinput', kl_stinput, 0)

@tail_recursion
def shen_x43vectorx63(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x43vectorx63, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1833_286 = FUN_ARGS[0]
    global symdic
    return ((shen_absvector_get(KL_ARG_V1833_286, 0) > 0) if shen_absvectorp(KL_ARG_V1833_286) else False)
shen_add_fun('shen.+vector?', shen_x43vectorx63, 1)

@tail_recursion
def kl_vector(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_vector, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1834_287 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Vector_288 = None
        KL_LOC_ZeroStamp_289 = None
        KL_LOC_Standard_290 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Vector_288', shen_absvector((KL_ARG_V1834_287 + 1))), [setattr(KL_CTX, 'KL_LOC_ZeroStamp_289', shen_absvector_set(KL_CTX.KL_LOC_Vector_288, 0, KL_ARG_V1834_287)), [setattr(KL_CTX, 'KL_LOC_Standard_290', (KL_CTX.KL_LOC_ZeroStamp_289 if shen_eq(KL_ARG_V1834_287, 0) else tco_apply(shen_fillvector, [KL_CTX.KL_LOC_ZeroStamp_289, 1, KL_ARG_V1834_287, tco_apply(kl_fail, [])]))), KL_CTX.KL_LOC_Standard_290][(-1)]][(-1)]][(-1)]
shen_add_fun('vector', kl_vector, 1)

@tail_recursion
def shen_fillvector(*FUN_ARGS):
    FUN_ARITY = 4
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_fillvector, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1835_291 = FUN_ARGS[0]
    KL_ARG_V1836_292 = FUN_ARGS[1]
    KL_ARG_V1837_293 = FUN_ARGS[2]
    KL_ARG_V1838_294 = FUN_ARGS[3]
    global symdic
    return (shen_absvector_set(KL_ARG_V1835_291, KL_ARG_V1837_293, KL_ARG_V1838_294) if shen_eq(KL_ARG_V1837_293, KL_ARG_V1836_292) else (tail_call(shen_fillvector, [shen_absvector_set(KL_ARG_V1835_291, KL_ARG_V1836_292, KL_ARG_V1838_294), (1 + KL_ARG_V1836_292), KL_ARG_V1837_293, KL_ARG_V1838_294]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.fillvector', shen_fillvector, 4)

@tail_recursion
def kl_vectorx63(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_vectorx63, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1840_295 = FUN_ARGS[0]
    global symdic
    return (shen_try_except((lambda : (shen_absvector_get(KL_ARG_V1840_295, 0) >= 0)), (lambda KL_ARG_E_296: False)) if shen_absvectorp(KL_ARG_V1840_295) else False)
shen_add_fun('vector?', kl_vectorx63, 1)

@tail_recursion
def kl_vectorx45x62(*FUN_ARGS):
    FUN_ARITY = 3
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_vectorx45x62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1841_297 = FUN_ARGS[0]
    KL_ARG_V1842_298 = FUN_ARGS[1]
    KL_ARG_V1843_299 = FUN_ARGS[2]
    global symdic
    return (shen_simple_error('cannot access 0th element of a vector\r\n') if shen_eq(KL_ARG_V1842_298, 0) else shen_absvector_set(KL_ARG_V1841_297, KL_ARG_V1842_298, KL_ARG_V1843_299))
shen_add_fun('vector->', kl_vectorx45x62, 3)

@tail_recursion
def kl_x60x45vector(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_x60x45vector, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1844_300 = FUN_ARGS[0]
    KL_ARG_V1845_301 = FUN_ARGS[1]

    class KL_Context:
        KL_LOC_VectorElement_302 = None
    KL_CTX = KL_Context()
    global symdic
    return (shen_simple_error('cannot access 0th element of a vector\r\n') if shen_eq(KL_ARG_V1845_301, 0) else [setattr(KL_CTX, 'KL_LOC_VectorElement_302', shen_absvector_get(KL_ARG_V1844_300, KL_ARG_V1845_301)), (shen_simple_error('vector element not found\r\n') if shen_eq(KL_CTX.KL_LOC_VectorElement_302, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_VectorElement_302)][(-1)])
shen_add_fun('<-vector', kl_x60x45vector, 2)

@tail_recursion
def shen_posintx63(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_posintx63, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1846_303 = FUN_ARGS[0]
    global symdic
    return ((KL_ARG_V1846_303 >= 0) if tco_apply(kl_integerx63, [KL_ARG_V1846_303]) else False)
shen_add_fun('shen.posint?', shen_posintx63, 1)

@tail_recursion
def kl_limit(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_limit, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1847_304 = FUN_ARGS[0]
    global symdic
    return shen_absvector_get(KL_ARG_V1847_304, 0)
shen_add_fun('limit', kl_limit, 1)

@tail_recursion
def kl_symbolx63(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_symbolx63, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1848_305 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_String_306 = None
    KL_CTX = KL_Context()
    global symdic
    return (False if (True if tco_apply(kl_booleanx63, [KL_ARG_V1848_305]) else (True if isinstance(KL_ARG_V1848_305, numbers.Number) else isinstance(KL_ARG_V1848_305, str))) else (shen_try_except((lambda : [setattr(KL_CTX, 'KL_LOC_String_306', str(KL_ARG_V1848_305)), tco_apply(shen_analysex45symbolx63, [KL_CTX.KL_LOC_String_306])][(-1)]), (lambda KL_ARG_E_307: False)) if True else shen_simple_error('condition failure')))
shen_add_fun('symbol?', kl_symbolx63, 1)

@tail_recursion
def shen_analysex45symbolx63(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_analysex45symbolx63, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1849_308 = FUN_ARGS[0]
    global symdic
    return ((tail_call(shen_alphanumsx63, [KL_ARG_V1849_308[1:]]) if tco_apply(shen_alphax63, [KL_ARG_V1849_308[0]]) else False) if tco_apply(shen_x43stringx63, [KL_ARG_V1849_308]) else (tail_call(shen_sysx45error, [symdic.symdic_shen_analysex45symbolx63]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.analyse-symbol?', shen_analysex45symbolx63, 1)

@tail_recursion
def shen_alphax63(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_alphax63, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1850_309 = FUN_ARGS[0]
    global symdic
    return tail_call(kl_elementx63, [KL_ARG_V1850_309, Cons('A', Cons('B', Cons('C', Cons('D', Cons('E', Cons('F', Cons('G', Cons('H', Cons('I', Cons('J', Cons('K', Cons('L', Cons('M', Cons('N', Cons('O', Cons('P', Cons('Q', Cons('R', Cons('S', Cons('T', Cons('U', Cons('V', Cons('W', Cons('X', Cons('Y', Cons('Z', Cons('a', Cons('b', Cons('c', Cons('d', Cons('e', Cons('f', Cons('g', Cons('h', Cons('i', Cons('j', Cons('k', Cons('l', Cons('m', Cons('n', Cons('o', Cons('p', Cons('q', Cons('r', Cons('s', Cons('t', Cons('u', Cons('v', Cons('w', Cons('x', Cons('y', Cons('z', Cons('=', Cons('*', Cons('/', Cons('+', Cons('-', Cons('_', Cons('?', Cons('$', Cons('!', Cons('@', Cons('~', Cons('>', Cons('<', Cons('&', Cons('%', Cons('{', Cons('}', Cons(':', Cons(';', Cons('`', Cons('#', Cons("'", Cons('.', nil)))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))])
shen_add_fun('shen.alpha?', shen_alphax63, 1)

@tail_recursion
def shen_alphanumsx63(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_alphanumsx63, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1851_310 = FUN_ARGS[0]
    global symdic
    return (True if shen_eq('', KL_ARG_V1851_310) else ((tail_call(shen_alphanumsx63, [KL_ARG_V1851_310[1:]]) if tco_apply(shen_alphanumx63, [KL_ARG_V1851_310[0]]) else False) if tco_apply(shen_x43stringx63, [KL_ARG_V1851_310]) else (tail_call(shen_sysx45error, [symdic.symdic_shen_alphanumsx63]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.alphanums?', shen_alphanumsx63, 1)

@tail_recursion
def shen_alphanumx63(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_alphanumx63, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1852_311 = FUN_ARGS[0]
    global symdic
    return (True if tco_apply(shen_alphax63, [KL_ARG_V1852_311]) else tail_call(shen_digitx63, [KL_ARG_V1852_311]))
shen_add_fun('shen.alphanum?', shen_alphanumx63, 1)

@tail_recursion
def shen_digitx63(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_digitx63, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1853_312 = FUN_ARGS[0]
    global symdic
    return tail_call(kl_elementx63, [KL_ARG_V1853_312, Cons('1', Cons('2', Cons('3', Cons('4', Cons('5', Cons('6', Cons('7', Cons('8', Cons('9', Cons('0', nil))))))))))])
shen_add_fun('shen.digit?', shen_digitx63, 1)

@tail_recursion
def kl_variablex63(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_variablex63, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1854_313 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_String_314 = None
    KL_CTX = KL_Context()
    global symdic
    return (False if (True if tco_apply(kl_booleanx63, [KL_ARG_V1854_313]) else (True if isinstance(KL_ARG_V1854_313, numbers.Number) else isinstance(KL_ARG_V1854_313, str))) else (shen_try_except((lambda : [setattr(KL_CTX, 'KL_LOC_String_314', str(KL_ARG_V1854_313)), tco_apply(shen_analysex45variablex63, [KL_CTX.KL_LOC_String_314])][(-1)]), (lambda KL_ARG_E_315: False)) if True else shen_simple_error('condition failure')))
shen_add_fun('variable?', kl_variablex63, 1)

@tail_recursion
def shen_analysex45variablex63(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_analysex45variablex63, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1855_316 = FUN_ARGS[0]
    global symdic
    return ((tail_call(shen_alphanumsx63, [KL_ARG_V1855_316[1:]]) if tco_apply(shen_uppercasex63, [KL_ARG_V1855_316[0]]) else False) if tco_apply(shen_x43stringx63, [KL_ARG_V1855_316]) else (tail_call(shen_sysx45error, [symdic.symdic_shen_analysex45variablex63]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.analyse-variable?', shen_analysex45variablex63, 1)

@tail_recursion
def shen_uppercasex63(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_uppercasex63, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1856_317 = FUN_ARGS[0]
    global symdic
    return tail_call(kl_elementx63, [KL_ARG_V1856_317, Cons('A', Cons('B', Cons('C', Cons('D', Cons('E', Cons('F', Cons('G', Cons('H', Cons('I', Cons('J', Cons('K', Cons('L', Cons('M', Cons('N', Cons('O', Cons('P', Cons('Q', Cons('R', Cons('S', Cons('T', Cons('U', Cons('V', Cons('W', Cons('X', Cons('Y', Cons('Z', nil))))))))))))))))))))))))))])
shen_add_fun('shen.uppercase?', shen_uppercasex63, 1)

@tail_recursion
def kl_gensym(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_gensym, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1857_318 = FUN_ARGS[0]
    global symdic
    return tail_call(kl_concat, [KL_ARG_V1857_318, shen_set(symdic.symdic_shen_x42gensymx42, (1 + shen_get(symdic.symdic_shen_x42gensymx42)))])
shen_add_fun('gensym', kl_gensym, 1)

@tail_recursion
def kl_concat(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_concat, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1858_319 = FUN_ARGS[0]
    KL_ARG_V1859_320 = FUN_ARGS[1]
    global symdic
    return shen_intern((str(KL_ARG_V1858_319) + str(KL_ARG_V1859_320)))
shen_add_fun('concat', kl_concat, 2)

@tail_recursion
def kl_x64p(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_x64p, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1860_321 = FUN_ARGS[0]
    KL_ARG_V1861_322 = FUN_ARGS[1]

    class KL_Context:
        KL_LOC_Vector_323 = None
        KL_LOC_Tag_324 = None
        KL_LOC_Fst_325 = None
        KL_LOC_Snd_326 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Vector_323', shen_absvector(3)), [setattr(KL_CTX, 'KL_LOC_Tag_324', shen_absvector_set(KL_CTX.KL_LOC_Vector_323, 0, symdic.symdic_shen_tuple)), [setattr(KL_CTX, 'KL_LOC_Fst_325', shen_absvector_set(KL_CTX.KL_LOC_Vector_323, 1, KL_ARG_V1860_321)), [setattr(KL_CTX, 'KL_LOC_Snd_326', shen_absvector_set(KL_CTX.KL_LOC_Vector_323, 2, KL_ARG_V1861_322)), KL_CTX.KL_LOC_Vector_323][(-1)]][(-1)]][(-1)]][(-1)]
shen_add_fun('@p', kl_x64p, 2)

@tail_recursion
def kl_fst(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_fst, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1862_327 = FUN_ARGS[0]
    global symdic
    return shen_absvector_get(KL_ARG_V1862_327, 1)
shen_add_fun('fst', kl_fst, 1)

@tail_recursion
def kl_snd(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_snd, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1863_328 = FUN_ARGS[0]
    global symdic
    return shen_absvector_get(KL_ARG_V1863_328, 2)
shen_add_fun('snd', kl_snd, 1)

@tail_recursion
def kl_tuplex63(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_tuplex63, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1864_329 = FUN_ARGS[0]
    global symdic
    return shen_try_except((lambda : (shen_eq(symdic.symdic_shen_tuple, shen_absvector_get(KL_ARG_V1864_329, 0)) if shen_absvectorp(KL_ARG_V1864_329) else False)), (lambda KL_ARG_E_330: False))
shen_add_fun('tuple?', kl_tuplex63, 1)

@tail_recursion
def kl_append(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_append, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1865_331 = FUN_ARGS[0]
    KL_ARG_V1866_332 = FUN_ARGS[1]
    global symdic
    return (KL_ARG_V1866_332 if shen_eq(nil, KL_ARG_V1865_331) else (Cons(car(KL_ARG_V1865_331), tco_apply(kl_append, [cdr(KL_ARG_V1865_331), KL_ARG_V1866_332])) if shen_consp(KL_ARG_V1865_331) else (tail_call(shen_sysx45error, [symdic.symdic_kl_append]) if True else shen_simple_error('condition failure'))))
shen_add_fun('append', kl_append, 2)

@tail_recursion
def kl_x64v(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_x64v, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1867_333 = FUN_ARGS[0]
    KL_ARG_V1868_334 = FUN_ARGS[1]

    class KL_Context:
        KL_LOC_Limit_335 = None
        KL_LOC_NewVector_336 = None
        KL_LOC_Xx43NewVector_337 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Limit_335', tco_apply(kl_limit, [KL_ARG_V1868_334])), [setattr(KL_CTX, 'KL_LOC_NewVector_336', tco_apply(kl_vector, [(KL_CTX.KL_LOC_Limit_335 + 1)])), [setattr(KL_CTX, 'KL_LOC_Xx43NewVector_337', tco_apply(kl_vectorx45x62, [KL_CTX.KL_LOC_NewVector_336, 1, KL_ARG_V1867_333])), (KL_CTX.KL_LOC_Xx43NewVector_337 if shen_eq(KL_CTX.KL_LOC_Limit_335, 0) else tail_call(shen_x64vx45help, [KL_ARG_V1868_334, 1, KL_CTX.KL_LOC_Limit_335, KL_CTX.KL_LOC_Xx43NewVector_337]))][(-1)]][(-1)]][(-1)]
shen_add_fun('@v', kl_x64v, 2)

@tail_recursion
def shen_x64vx45help(*FUN_ARGS):
    FUN_ARITY = 4
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x64vx45help, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1869_338 = FUN_ARGS[0]
    KL_ARG_V1870_339 = FUN_ARGS[1]
    KL_ARG_V1871_340 = FUN_ARGS[2]
    KL_ARG_V1872_341 = FUN_ARGS[3]
    global symdic
    return (tail_call(shen_copyfromvector, [KL_ARG_V1869_338, KL_ARG_V1872_341, KL_ARG_V1871_340, (KL_ARG_V1871_340 + 1)]) if shen_eq(KL_ARG_V1871_340, KL_ARG_V1870_339) else (tail_call(shen_x64vx45help, [KL_ARG_V1869_338, (KL_ARG_V1870_339 + 1), KL_ARG_V1871_340, tco_apply(shen_copyfromvector, [KL_ARG_V1869_338, KL_ARG_V1872_341, KL_ARG_V1870_339, (KL_ARG_V1870_339 + 1)])]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.@v-help', shen_x64vx45help, 4)

@tail_recursion
def shen_copyfromvector(*FUN_ARGS):
    FUN_ARITY = 4
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_copyfromvector, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1874_342 = FUN_ARGS[0]
    KL_ARG_V1875_343 = FUN_ARGS[1]
    KL_ARG_V1876_344 = FUN_ARGS[2]
    KL_ARG_V1877_345 = FUN_ARGS[3]
    global symdic
    return shen_try_except((lambda : tco_apply(kl_vectorx45x62, [KL_ARG_V1875_343, KL_ARG_V1877_345, tco_apply(kl_x60x45vector, [KL_ARG_V1874_342, KL_ARG_V1876_344])])), (lambda KL_ARG_E_346: KL_ARG_V1875_343))
shen_add_fun('shen.copyfromvector', shen_copyfromvector, 4)

@tail_recursion
def kl_hdv(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_hdv, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1878_347 = FUN_ARGS[0]
    global symdic
    return shen_try_except((lambda : tco_apply(kl_x60x45vector, [KL_ARG_V1878_347, 1])), (lambda KL_ARG_E_348: shen_simple_error(('hdv needs a non-empty vector as an argument; not ' + tco_apply(shen_app, [KL_ARG_V1878_347, '\r\n', symdic.symdic_shen_s])))))
shen_add_fun('hdv', kl_hdv, 1)

@tail_recursion
def kl_tlv(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_tlv, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1879_349 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Limit_350 = None
        KL_LOC_NewVector_351 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Limit_350', tco_apply(kl_limit, [KL_ARG_V1879_349])), (shen_simple_error('cannot take the tail of the empty vector\r\n') if shen_eq(KL_CTX.KL_LOC_Limit_350, 0) else (tail_call(kl_vector, [0]) if shen_eq(KL_CTX.KL_LOC_Limit_350, 1) else [setattr(KL_CTX, 'KL_LOC_NewVector_351', tco_apply(kl_vector, [(KL_CTX.KL_LOC_Limit_350 - 1)])), tail_call(shen_tlvx45help, [KL_ARG_V1879_349, 2, KL_CTX.KL_LOC_Limit_350, tco_apply(kl_vector, [(KL_CTX.KL_LOC_Limit_350 - 1)])])][(-1)]))][(-1)]
shen_add_fun('tlv', kl_tlv, 1)

@tail_recursion
def shen_tlvx45help(*FUN_ARGS):
    FUN_ARITY = 4
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_tlvx45help, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1880_352 = FUN_ARGS[0]
    KL_ARG_V1881_353 = FUN_ARGS[1]
    KL_ARG_V1882_354 = FUN_ARGS[2]
    KL_ARG_V1883_355 = FUN_ARGS[3]
    global symdic
    return (tail_call(shen_copyfromvector, [KL_ARG_V1880_352, KL_ARG_V1883_355, KL_ARG_V1882_354, (KL_ARG_V1882_354 - 1)]) if shen_eq(KL_ARG_V1882_354, KL_ARG_V1881_353) else (tail_call(shen_tlvx45help, [KL_ARG_V1880_352, (KL_ARG_V1881_353 + 1), KL_ARG_V1882_354, tco_apply(shen_copyfromvector, [KL_ARG_V1880_352, KL_ARG_V1883_355, KL_ARG_V1881_353, (KL_ARG_V1881_353 - 1)])]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.tlv-help', shen_tlvx45help, 4)

@tail_recursion
def kl_assoc(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_assoc, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1893_356 = FUN_ARGS[0]
    KL_ARG_V1894_357 = FUN_ARGS[1]
    global symdic
    return (nil if shen_eq(nil, KL_ARG_V1894_357) else (car(KL_ARG_V1894_357) if ((shen_eq(car(car(KL_ARG_V1894_357)), KL_ARG_V1893_356) if shen_consp(car(KL_ARG_V1894_357)) else False) if shen_consp(KL_ARG_V1894_357) else False) else (tail_call(kl_assoc, [KL_ARG_V1893_356, cdr(KL_ARG_V1894_357)]) if shen_consp(KL_ARG_V1894_357) else (tail_call(shen_sysx45error, [symdic.symdic_kl_assoc]) if True else shen_simple_error('condition failure')))))
shen_add_fun('assoc', kl_assoc, 2)

@tail_recursion
def kl_booleanx63(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_booleanx63, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1900_358 = FUN_ARGS[0]
    global symdic
    return (True if shen_eq(True, KL_ARG_V1900_358) else (True if shen_eq(False, KL_ARG_V1900_358) else (False if True else shen_simple_error('condition failure'))))
shen_add_fun('boolean?', kl_booleanx63, 1)

@tail_recursion
def kl_nl(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_nl, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1901_359 = FUN_ARGS[0]
    global symdic
    return (0 if shen_eq(0, KL_ARG_V1901_359) else ([tco_apply(shen_prhush, ['\r\n', tco_apply(kl_stoutput, [])]), tail_call(kl_nl, [(KL_ARG_V1901_359 - 1)])][(-1)] if True else shen_simple_error('condition failure')))
shen_add_fun('nl', kl_nl, 1)

@tail_recursion
def kl_difference(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_difference, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1904_360 = FUN_ARGS[0]
    KL_ARG_V1905_361 = FUN_ARGS[1]
    global symdic
    return (nil if shen_eq(nil, KL_ARG_V1904_360) else ((tail_call(kl_difference, [cdr(KL_ARG_V1904_360), KL_ARG_V1905_361]) if tco_apply(kl_elementx63, [car(KL_ARG_V1904_360), KL_ARG_V1905_361]) else Cons(car(KL_ARG_V1904_360), tco_apply(kl_difference, [cdr(KL_ARG_V1904_360), KL_ARG_V1905_361]))) if shen_consp(KL_ARG_V1904_360) else (tail_call(shen_sysx45error, [symdic.symdic_kl_difference]) if True else shen_simple_error('condition failure'))))
shen_add_fun('difference', kl_difference, 2)

@tail_recursion
def kl_do(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_do, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1906_362 = FUN_ARGS[0]
    KL_ARG_V1907_363 = FUN_ARGS[1]
    global symdic
    return KL_ARG_V1907_363
shen_add_fun('do', kl_do, 2)

@tail_recursion
def kl_elementx63(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_elementx63, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1916_364 = FUN_ARGS[0]
    KL_ARG_V1917_365 = FUN_ARGS[1]
    global symdic
    return (False if shen_eq(nil, KL_ARG_V1917_365) else (True if (shen_eq(car(KL_ARG_V1917_365), KL_ARG_V1916_364) if shen_consp(KL_ARG_V1917_365) else False) else (tail_call(kl_elementx63, [KL_ARG_V1916_364, cdr(KL_ARG_V1917_365)]) if shen_consp(KL_ARG_V1917_365) else (tail_call(shen_sysx45error, [symdic.symdic_kl_elementx63]) if True else shen_simple_error('condition failure')))))
shen_add_fun('element?', kl_elementx63, 2)

@tail_recursion
def kl_emptyx63(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_emptyx63, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1923_366 = FUN_ARGS[0]
    global symdic
    return (True if shen_eq(nil, KL_ARG_V1923_366) else (False if True else shen_simple_error('condition failure')))
shen_add_fun('empty?', kl_emptyx63, 1)

@tail_recursion
def kl_fix(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_fix, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1924_367 = FUN_ARGS[0]
    KL_ARG_V1925_368 = FUN_ARGS[1]
    global symdic
    return tail_call(shen_fixx45help, [KL_ARG_V1924_367, KL_ARG_V1925_368, shen_apply(KL_ARG_V1924_367, [KL_ARG_V1925_368])])
shen_add_fun('fix', kl_fix, 2)

@tail_recursion
def shen_fixx45help(*FUN_ARGS):
    FUN_ARITY = 3
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_fixx45help, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1932_369 = FUN_ARGS[0]
    KL_ARG_V1933_370 = FUN_ARGS[1]
    KL_ARG_V1934_371 = FUN_ARGS[2]
    global symdic
    return (KL_ARG_V1934_371 if shen_eq(KL_ARG_V1934_371, KL_ARG_V1933_370) else (tail_call(shen_fixx45help, [KL_ARG_V1932_369, KL_ARG_V1934_371, shen_apply(KL_ARG_V1932_369, [KL_ARG_V1934_371])]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.fix-help', shen_fixx45help, 3)

@tail_recursion
def kl_put(*FUN_ARGS):
    FUN_ARITY = 4
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_put, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1936_372 = FUN_ARGS[0]
    KL_ARG_V1937_373 = FUN_ARGS[1]
    KL_ARG_V1938_374 = FUN_ARGS[2]
    KL_ARG_V1939_375 = FUN_ARGS[3]

    class KL_Context:
        KL_LOC_N_376 = None
        KL_LOC_Entry_377 = None
        KL_LOC_Change_379 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_N_376', tco_apply(kl_hash, [KL_ARG_V1936_372, tco_apply(kl_limit, [KL_ARG_V1939_375])])), [setattr(KL_CTX, 'KL_LOC_Entry_377', shen_try_except((lambda : tco_apply(kl_x60x45vector, [KL_ARG_V1939_375, KL_CTX.KL_LOC_N_376])), (lambda KL_ARG_E_378: nil))), [setattr(KL_CTX, 'KL_LOC_Change_379', tco_apply(kl_vectorx45x62, [KL_ARG_V1939_375, KL_CTX.KL_LOC_N_376, tco_apply(shen_changex45pointerx45value, [KL_ARG_V1936_372, KL_ARG_V1937_373, KL_ARG_V1938_374, KL_CTX.KL_LOC_Entry_377])])), KL_ARG_V1938_374][(-1)]][(-1)]][(-1)]
shen_add_fun('put', kl_put, 4)

@tail_recursion
def shen_changex45pointerx45value(*FUN_ARGS):
    FUN_ARITY = 4
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_changex45pointerx45value, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1942_380 = FUN_ARGS[0]
    KL_ARG_V1943_381 = FUN_ARGS[1]
    KL_ARG_V1944_382 = FUN_ARGS[2]
    KL_ARG_V1945_383 = FUN_ARGS[3]
    global symdic
    return (Cons(Cons(Cons(KL_ARG_V1942_380, Cons(KL_ARG_V1943_381, nil)), KL_ARG_V1944_382), nil) if shen_eq(nil, KL_ARG_V1945_383) else (Cons(Cons(car(car(KL_ARG_V1945_383)), KL_ARG_V1944_382), cdr(KL_ARG_V1945_383)) if ((((((shen_eq(car(car(car(KL_ARG_V1945_383))), KL_ARG_V1942_380) if shen_eq(car(cdr(car(car(KL_ARG_V1945_383)))), KL_ARG_V1943_381) else False) if shen_eq(nil, cdr(cdr(car(car(KL_ARG_V1945_383))))) else False) if shen_consp(cdr(car(car(KL_ARG_V1945_383)))) else False) if shen_consp(car(car(KL_ARG_V1945_383))) else False) if shen_consp(car(KL_ARG_V1945_383)) else False) if shen_consp(KL_ARG_V1945_383) else False) else (Cons(car(KL_ARG_V1945_383), tco_apply(shen_changex45pointerx45value, [KL_ARG_V1942_380, KL_ARG_V1943_381, KL_ARG_V1944_382, cdr(KL_ARG_V1945_383)])) if shen_consp(KL_ARG_V1945_383) else (tail_call(shen_sysx45error, [symdic.symdic_shen_changex45pointerx45value]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.change-pointer-value', shen_changex45pointerx45value, 4)

@tail_recursion
def kl_get(*FUN_ARGS):
    FUN_ARITY = 3
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_get, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1948_384 = FUN_ARGS[0]
    KL_ARG_V1949_385 = FUN_ARGS[1]
    KL_ARG_V1950_386 = FUN_ARGS[2]

    class KL_Context:
        KL_LOC_N_387 = None
        KL_LOC_Entry_388 = None
        KL_LOC_Result_390 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_N_387', tco_apply(kl_hash, [KL_ARG_V1948_384, tco_apply(kl_limit, [KL_ARG_V1950_386])])), [setattr(KL_CTX, 'KL_LOC_Entry_388', shen_try_except((lambda : tco_apply(kl_x60x45vector, [KL_ARG_V1950_386, KL_CTX.KL_LOC_N_387])), (lambda KL_ARG_E_389: shen_simple_error('pointer not found\r\n')))), [setattr(KL_CTX, 'KL_LOC_Result_390', tco_apply(kl_assoc, [Cons(KL_ARG_V1948_384, Cons(KL_ARG_V1949_385, nil)), KL_CTX.KL_LOC_Entry_388])), (shen_simple_error('value not found\r\n') if tco_apply(kl_emptyx63, [KL_CTX.KL_LOC_Result_390]) else cdr(KL_CTX.KL_LOC_Result_390))][(-1)]][(-1)]][(-1)]
shen_add_fun('get', kl_get, 3)

@tail_recursion
def kl_hash(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_hash, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1951_391 = FUN_ARGS[0]
    KL_ARG_V1952_392 = FUN_ARGS[1]

    class KL_Context:
        KL_LOC_Hash_393 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Hash_393', tco_apply(shen_mod, [tco_apply(shen_sum, [tco_apply(kl_map, [(lambda KL_ARG_V1801_394: ord(KL_ARG_V1801_394)), tco_apply(kl_explode, [KL_ARG_V1951_391])])]), KL_ARG_V1952_392])), (1 if shen_eq(0, KL_CTX.KL_LOC_Hash_393) else KL_CTX.KL_LOC_Hash_393)][(-1)]
shen_add_fun('hash', kl_hash, 2)

@tail_recursion
def shen_mod(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_mod, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1953_395 = FUN_ARGS[0]
    KL_ARG_V1954_396 = FUN_ARGS[1]
    global symdic
    return tail_call(shen_modh, [KL_ARG_V1953_395, tco_apply(shen_multiples, [KL_ARG_V1953_395, Cons(KL_ARG_V1954_396, nil)])])
shen_add_fun('shen.mod', shen_mod, 2)

@tail_recursion
def shen_multiples(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_multiples, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1955_397 = FUN_ARGS[0]
    KL_ARG_V1956_398 = FUN_ARGS[1]
    global symdic
    return (cdr(KL_ARG_V1956_398) if ((car(KL_ARG_V1956_398) > KL_ARG_V1955_397) if shen_consp(KL_ARG_V1956_398) else False) else (tail_call(shen_multiples, [KL_ARG_V1955_397, Cons((2 * car(KL_ARG_V1956_398)), KL_ARG_V1956_398)]) if shen_consp(KL_ARG_V1956_398) else (tail_call(shen_sysx45error, [symdic.symdic_shen_multiples]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.multiples', shen_multiples, 2)

@tail_recursion
def shen_modh(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_modh, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1959_399 = FUN_ARGS[0]
    KL_ARG_V1960_400 = FUN_ARGS[1]
    global symdic
    return (0 if shen_eq(0, KL_ARG_V1959_399) else (KL_ARG_V1959_399 if shen_eq(nil, KL_ARG_V1960_400) else ((KL_ARG_V1959_399 if tco_apply(kl_emptyx63, [cdr(KL_ARG_V1960_400)]) else tail_call(shen_modh, [KL_ARG_V1959_399, cdr(KL_ARG_V1960_400)])) if ((car(KL_ARG_V1960_400) > KL_ARG_V1959_399) if shen_consp(KL_ARG_V1960_400) else False) else (tail_call(shen_modh, [(KL_ARG_V1959_399 - car(KL_ARG_V1960_400)), KL_ARG_V1960_400]) if shen_consp(KL_ARG_V1960_400) else (tail_call(shen_sysx45error, [symdic.symdic_shen_modh]) if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.modh', shen_modh, 2)

@tail_recursion
def shen_sum(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_sum, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1961_401 = FUN_ARGS[0]
    global symdic
    return (0 if shen_eq(nil, KL_ARG_V1961_401) else ((car(KL_ARG_V1961_401) + tco_apply(shen_sum, [cdr(KL_ARG_V1961_401)])) if shen_consp(KL_ARG_V1961_401) else (tail_call(shen_sysx45error, [symdic.symdic_shen_sum]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.sum', shen_sum, 1)

@tail_recursion
def kl_head(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_head, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1968_402 = FUN_ARGS[0]
    global symdic
    return (car(KL_ARG_V1968_402) if shen_consp(KL_ARG_V1968_402) else (shen_simple_error('head expects a non-empty list') if True else shen_simple_error('condition failure')))
shen_add_fun('head', kl_head, 1)

@tail_recursion
def kl_tail(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_tail, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1975_403 = FUN_ARGS[0]
    global symdic
    return (cdr(KL_ARG_V1975_403) if shen_consp(KL_ARG_V1975_403) else (shen_simple_error('tail expects a non-empty list') if True else shen_simple_error('condition failure')))
shen_add_fun('tail', kl_tail, 1)

@tail_recursion
def kl_hdstr(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_hdstr, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1976_404 = FUN_ARGS[0]
    global symdic
    return KL_ARG_V1976_404[0]
shen_add_fun('hdstr', kl_hdstr, 1)

@tail_recursion
def kl_intersection(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_intersection, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1979_405 = FUN_ARGS[0]
    KL_ARG_V1980_406 = FUN_ARGS[1]
    global symdic
    return (nil if shen_eq(nil, KL_ARG_V1979_405) else ((Cons(car(KL_ARG_V1979_405), tco_apply(kl_intersection, [cdr(KL_ARG_V1979_405), KL_ARG_V1980_406])) if tco_apply(kl_elementx63, [car(KL_ARG_V1979_405), KL_ARG_V1980_406]) else tail_call(kl_intersection, [cdr(KL_ARG_V1979_405), KL_ARG_V1980_406])) if shen_consp(KL_ARG_V1979_405) else (tail_call(shen_sysx45error, [symdic.symdic_kl_intersection]) if True else shen_simple_error('condition failure'))))
shen_add_fun('intersection', kl_intersection, 2)

@tail_recursion
def kl_reverse(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_reverse, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1981_407 = FUN_ARGS[0]
    global symdic
    return tail_call(shen_reverse_help, [KL_ARG_V1981_407, nil])
shen_add_fun('reverse', kl_reverse, 1)

@tail_recursion
def shen_reverse_help(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_reverse_help, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1982_408 = FUN_ARGS[0]
    KL_ARG_V1983_409 = FUN_ARGS[1]
    global symdic
    return (KL_ARG_V1983_409 if shen_eq(nil, KL_ARG_V1982_408) else (tail_call(shen_reverse_help, [cdr(KL_ARG_V1982_408), Cons(car(KL_ARG_V1982_408), KL_ARG_V1983_409)]) if shen_consp(KL_ARG_V1982_408) else (tail_call(shen_sysx45error, [symdic.symdic_shen_reverse_help]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.reverse_help', shen_reverse_help, 2)

@tail_recursion
def kl_union(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_union, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1984_410 = FUN_ARGS[0]
    KL_ARG_V1985_411 = FUN_ARGS[1]
    global symdic
    return (KL_ARG_V1985_411 if shen_eq(nil, KL_ARG_V1984_410) else ((tail_call(kl_union, [cdr(KL_ARG_V1984_410), KL_ARG_V1985_411]) if tco_apply(kl_elementx63, [car(KL_ARG_V1984_410), KL_ARG_V1985_411]) else Cons(car(KL_ARG_V1984_410), tco_apply(kl_union, [cdr(KL_ARG_V1984_410), KL_ARG_V1985_411]))) if shen_consp(KL_ARG_V1984_410) else (tail_call(shen_sysx45error, [symdic.symdic_kl_union]) if True else shen_simple_error('condition failure'))))
shen_add_fun('union', kl_union, 2)

@tail_recursion
def kl_yx45orx45nx63(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_yx45orx45nx63, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1986_412 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Message_413 = None
        KL_LOC_Yx45orx45N_414 = None
        KL_LOC_Input_415 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Message_413', tco_apply(shen_prhush, [tco_apply(shen_procx45nl, [KL_ARG_V1986_412]), tco_apply(kl_stoutput, [])])), [setattr(KL_CTX, 'KL_LOC_Yx45orx45N_414', tco_apply(shen_prhush, [' (y/n) ', tco_apply(kl_stoutput, [])])), [setattr(KL_CTX, 'KL_LOC_Input_415', tco_apply(shen_app, [tco_apply(kl_input, []), '', symdic.symdic_shen_s])), (True if shen_eq('y', KL_CTX.KL_LOC_Input_415) else (False if shen_eq('n', KL_CTX.KL_LOC_Input_415) else [tco_apply(shen_prhush, ['please answer y or n\r\n', tco_apply(kl_stoutput, [])]), tail_call(kl_yx45orx45nx63, [KL_ARG_V1986_412])][(-1)]))][(-1)]][(-1)]][(-1)]
shen_add_fun('y-or-n?', kl_yx45orx45nx63, 1)

@tail_recursion
def kl_not(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_not, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1987_416 = FUN_ARGS[0]
    global symdic
    return (False if KL_ARG_V1987_416 else True)
shen_add_fun('not', kl_not, 1)

@tail_recursion
def kl_subst(*FUN_ARGS):
    FUN_ARITY = 3
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_subst, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1996_417 = FUN_ARGS[0]
    KL_ARG_V1997_418 = FUN_ARGS[1]
    KL_ARG_V1998_419 = FUN_ARGS[2]
    global symdic
    return (KL_ARG_V1996_417 if shen_eq(KL_ARG_V1998_419, KL_ARG_V1997_418) else (Cons(tco_apply(kl_subst, [KL_ARG_V1996_417, KL_ARG_V1997_418, car(KL_ARG_V1998_419)]), tco_apply(kl_subst, [KL_ARG_V1996_417, KL_ARG_V1997_418, cdr(KL_ARG_V1998_419)])) if shen_consp(KL_ARG_V1998_419) else (KL_ARG_V1998_419 if True else shen_simple_error('condition failure'))))
shen_add_fun('subst', kl_subst, 3)

@tail_recursion
def kl_explode(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_explode, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2000_420 = FUN_ARGS[0]
    global symdic
    return tail_call(shen_explodex45h, [tco_apply(shen_app, [KL_ARG_V2000_420, '', symdic.symdic_shen_a])])
shen_add_fun('explode', kl_explode, 1)

@tail_recursion
def shen_explodex45h(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_explodex45h, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2001_421 = FUN_ARGS[0]
    global symdic
    return (nil if shen_eq('', KL_ARG_V2001_421) else (Cons(KL_ARG_V2001_421[0], tco_apply(shen_explodex45h, [KL_ARG_V2001_421[1:]])) if tco_apply(shen_x43stringx63, [KL_ARG_V2001_421]) else (tail_call(shen_sysx45error, [symdic.symdic_shen_explodex45h]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.explode-h', shen_explodex45h, 1)

@tail_recursion
def kl_cd(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_cd, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2002_422 = FUN_ARGS[0]
    global symdic
    return shen_set(symdic.symdic_kl_x42homex45directoryx42, ('' if shen_eq(KL_ARG_V2002_422, '') else tco_apply(shen_app, [KL_ARG_V2002_422, '/', symdic.symdic_shen_a])))
shen_add_fun('cd', kl_cd, 1)

@tail_recursion
def kl_map(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_map, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2003_423 = FUN_ARGS[0]
    KL_ARG_V2004_424 = FUN_ARGS[1]
    global symdic
    return tail_call(shen_mapx45h, [KL_ARG_V2003_423, KL_ARG_V2004_424, nil])
shen_add_fun('map', kl_map, 2)

@tail_recursion
def shen_mapx45h(*FUN_ARGS):
    FUN_ARITY = 3
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_mapx45h, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2007_425 = FUN_ARGS[0]
    KL_ARG_V2008_426 = FUN_ARGS[1]
    KL_ARG_V2009_427 = FUN_ARGS[2]
    global symdic
    return (tail_call(kl_reverse, [KL_ARG_V2009_427]) if shen_eq(nil, KL_ARG_V2008_426) else (tail_call(shen_mapx45h, [KL_ARG_V2007_425, cdr(KL_ARG_V2008_426), Cons(shen_apply(KL_ARG_V2007_425, [car(KL_ARG_V2008_426)]), KL_ARG_V2009_427)]) if shen_consp(KL_ARG_V2008_426) else (tail_call(shen_sysx45error, [symdic.symdic_shen_mapx45h]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.map-h', shen_mapx45h, 3)

@tail_recursion
def kl_length(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_length, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2010_428 = FUN_ARGS[0]
    global symdic
    return tail_call(shen_lengthx45h, [KL_ARG_V2010_428, 0])
shen_add_fun('length', kl_length, 1)

@tail_recursion
def shen_lengthx45h(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_lengthx45h, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2011_429 = FUN_ARGS[0]
    KL_ARG_V2012_430 = FUN_ARGS[1]
    global symdic
    return (KL_ARG_V2012_430 if shen_eq(nil, KL_ARG_V2011_429) else (tail_call(shen_lengthx45h, [cdr(KL_ARG_V2011_429), (KL_ARG_V2012_430 + 1)]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.length-h', shen_lengthx45h, 2)

@tail_recursion
def kl_occurrences(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_occurrences, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2021_431 = FUN_ARGS[0]
    KL_ARG_V2022_432 = FUN_ARGS[1]
    global symdic
    return (1 if shen_eq(KL_ARG_V2022_432, KL_ARG_V2021_431) else ((tco_apply(kl_occurrences, [KL_ARG_V2021_431, car(KL_ARG_V2022_432)]) + tco_apply(kl_occurrences, [KL_ARG_V2021_431, cdr(KL_ARG_V2022_432)])) if shen_consp(KL_ARG_V2022_432) else (0 if True else shen_simple_error('condition failure'))))
shen_add_fun('occurrences', kl_occurrences, 2)

@tail_recursion
def kl_nth(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_nth, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2030_433 = FUN_ARGS[0]
    KL_ARG_V2031_434 = FUN_ARGS[1]
    global symdic
    return (car(KL_ARG_V2031_434) if (shen_consp(KL_ARG_V2031_434) if shen_eq(1, KL_ARG_V2030_433) else False) else (tail_call(kl_nth, [(KL_ARG_V2030_433 - 1), cdr(KL_ARG_V2031_434)]) if shen_consp(KL_ARG_V2031_434) else (tail_call(shen_sysx45error, [symdic.symdic_kl_nth]) if True else shen_simple_error('condition failure'))))
shen_add_fun('nth', kl_nth, 2)

@tail_recursion
def kl_integerx63(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_integerx63, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2032_435 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Abs_436 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_Abs_436', tco_apply(shen_abs, [KL_ARG_V2032_435])), tail_call(shen_integerx45testx63, [KL_CTX.KL_LOC_Abs_436, tco_apply(shen_magless, [KL_CTX.KL_LOC_Abs_436, 1])])][(-1)] if isinstance(KL_ARG_V2032_435, numbers.Number) else False)
shen_add_fun('integer?', kl_integerx63, 1)

@tail_recursion
def shen_abs(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_abs, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2033_437 = FUN_ARGS[0]
    global symdic
    return (KL_ARG_V2033_437 if (KL_ARG_V2033_437 > 0) else (0 - KL_ARG_V2033_437))
shen_add_fun('shen.abs', shen_abs, 1)

@tail_recursion
def shen_magless(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_magless, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2034_438 = FUN_ARGS[0]
    KL_ARG_V2035_439 = FUN_ARGS[1]

    class KL_Context:
        KL_LOC_Nx2_440 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Nx2_440', (KL_ARG_V2035_439 * 2)), (KL_ARG_V2035_439 if (KL_CTX.KL_LOC_Nx2_440 > KL_ARG_V2034_438) else tail_call(shen_magless, [KL_ARG_V2034_438, KL_CTX.KL_LOC_Nx2_440]))][(-1)]
shen_add_fun('shen.magless', shen_magless, 2)

@tail_recursion
def shen_integerx45testx63(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_integerx45testx63, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2039_441 = FUN_ARGS[0]
    KL_ARG_V2040_442 = FUN_ARGS[1]

    class KL_Context:
        KL_LOC_Absx45N_443 = None
    KL_CTX = KL_Context()
    global symdic
    return (True if shen_eq(0, KL_ARG_V2039_441) else (False if (1 > KL_ARG_V2039_441) else ([setattr(KL_CTX, 'KL_LOC_Absx45N_443', (KL_ARG_V2039_441 - KL_ARG_V2040_442)), (tail_call(kl_integerx63, [KL_ARG_V2039_441]) if (0 > KL_CTX.KL_LOC_Absx45N_443) else tail_call(shen_integerx45testx63, [KL_CTX.KL_LOC_Absx45N_443, KL_ARG_V2040_442]))][(-1)] if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.integer-test?', shen_integerx45testx63, 2)

@tail_recursion
def kl_mapcan(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_mapcan, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2043_444 = FUN_ARGS[0]
    KL_ARG_V2044_445 = FUN_ARGS[1]
    global symdic
    return (nil if shen_eq(nil, KL_ARG_V2044_445) else (tail_call(kl_append, [shen_apply(KL_ARG_V2043_444, [car(KL_ARG_V2044_445)]), tco_apply(kl_mapcan, [KL_ARG_V2043_444, cdr(KL_ARG_V2044_445)])]) if shen_consp(KL_ARG_V2044_445) else (tail_call(shen_sysx45error, [symdic.symdic_kl_mapcan]) if True else shen_simple_error('condition failure'))))
shen_add_fun('mapcan', kl_mapcan, 2)

@tail_recursion
def kl_readx45filex45asx45bytelist(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_readx45filex45asx45bytelist, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2045_446 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Stream_447 = None
        KL_LOC_Byte_448 = None
        KL_LOC_Bytes_449 = None
        KL_LOC_Close_450 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Stream_447', shen_open(symdic.symdic_kl_file, KL_ARG_V2045_446, symdic.symdic_kl_in)), [setattr(KL_CTX, 'KL_LOC_Byte_448', shen_read_byte(KL_CTX.KL_LOC_Stream_447)), [setattr(KL_CTX, 'KL_LOC_Bytes_449', tco_apply(shen_readx45filex45asx45bytelistx45help, [KL_CTX.KL_LOC_Stream_447, KL_CTX.KL_LOC_Byte_448, nil])), [setattr(KL_CTX, 'KL_LOC_Close_450', shen_close(KL_CTX.KL_LOC_Stream_447)), tail_call(kl_reverse, [KL_CTX.KL_LOC_Bytes_449])][(-1)]][(-1)]][(-1)]][(-1)]
shen_add_fun('read-file-as-bytelist', kl_readx45filex45asx45bytelist, 1)

@tail_recursion
def shen_readx45filex45asx45bytelistx45help(*FUN_ARGS):
    FUN_ARITY = 3
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_readx45filex45asx45bytelistx45help, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2046_451 = FUN_ARGS[0]
    KL_ARG_V2047_452 = FUN_ARGS[1]
    KL_ARG_V2048_453 = FUN_ARGS[2]
    global symdic
    return (KL_ARG_V2048_453 if shen_eq((-1), KL_ARG_V2047_452) else (tail_call(shen_readx45filex45asx45bytelistx45help, [KL_ARG_V2046_451, shen_read_byte(KL_ARG_V2046_451), Cons(KL_ARG_V2047_452, KL_ARG_V2048_453)]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.read-file-as-bytelist-help', shen_readx45filex45asx45bytelistx45help, 3)

@tail_recursion
def kl_readx45filex45asx45string(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_readx45filex45asx45string, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2049_454 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Stream_455 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Stream_455', shen_open(symdic.symdic_kl_file, KL_ARG_V2049_454, symdic.symdic_kl_in)), tail_call(shen_rfasx45h, [KL_CTX.KL_LOC_Stream_455, shen_read_byte(KL_CTX.KL_LOC_Stream_455), ''])][(-1)]
shen_add_fun('read-file-as-string', kl_readx45filex45asx45string, 1)

@tail_recursion
def shen_rfasx45h(*FUN_ARGS):
    FUN_ARITY = 3
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_rfasx45h, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2050_456 = FUN_ARGS[0]
    KL_ARG_V2051_457 = FUN_ARGS[1]
    KL_ARG_V2052_458 = FUN_ARGS[2]
    global symdic
    return ([shen_close(KL_ARG_V2050_456), KL_ARG_V2052_458][(-1)] if shen_eq((-1), KL_ARG_V2051_457) else (tail_call(shen_rfasx45h, [KL_ARG_V2050_456, shen_read_byte(KL_ARG_V2050_456), (KL_ARG_V2052_458 + chr(KL_ARG_V2051_457))]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.rfas-h', shen_rfasx45h, 3)

@tail_recursion
def kl_x61x61(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_x61x61, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2061_459 = FUN_ARGS[0]
    KL_ARG_V2062_460 = FUN_ARGS[1]
    global symdic
    return (True if shen_eq(KL_ARG_V2062_460, KL_ARG_V2061_459) else (False if True else shen_simple_error('condition failure')))
shen_add_fun('==', kl_x61x61, 2)

@tail_recursion
def kl_abort(*FUN_ARGS):
    FUN_ARITY = 0
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_abort, (FUN_ARGS + lambdaargs)))
    global symdic
    return shen_simple_error('')
shen_add_fun('abort', kl_abort, 0)

@tail_recursion
def kl_read(*FUN_ARGS):
    FUN_ARITY = 0
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_read, (FUN_ARGS + lambdaargs)))
    global symdic
    return car(tco_apply(kl_lineread, []))
shen_add_fun('read', kl_read, 0)

@tail_recursion
def kl_input(*FUN_ARGS):
    FUN_ARITY = 0
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_input, (FUN_ARGS + lambdaargs)))
    global symdic
    return tail_call(kl_eval, [tco_apply(kl_read, [])])
shen_add_fun('input', kl_input, 0)

@tail_recursion
def kl_inputx43(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_inputx43, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2068_461 = FUN_ARGS[0]
    KL_ARG_V2069_462 = FUN_ARGS[1]

    class KL_Context:
        KL_LOC_Input_463 = None
        KL_LOC_Check_464 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Input_463', tco_apply(kl_read, [])), [setattr(KL_CTX, 'KL_LOC_Check_464', tco_apply(shen_typecheck, [KL_CTX.KL_LOC_Input_463, KL_ARG_V2069_462])), ([tco_apply(shen_prhush, [('input is not of type ' + tco_apply(shen_app, [KL_ARG_V2069_462, ': please re-enter ', symdic.symdic_shen_r])), tco_apply(kl_stoutput, [])]), tail_call(kl_inputx43, [symdic.symdic_kl_x58, KL_ARG_V2069_462])][(-1)] if shen_eq(False, KL_CTX.KL_LOC_Check_464) else tail_call(kl_eval, [KL_CTX.KL_LOC_Input_463]))][(-1)]][(-1)]
shen_add_fun('input+', kl_inputx43, 2)

@tail_recursion
def readx43(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(readx43, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2074_465 = FUN_ARGS[0]
    KL_ARG_V2075_466 = FUN_ARGS[1]

    class KL_Context:
        KL_LOC_Input_467 = None
        KL_LOC_Check_468 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Input_467', tco_apply(kl_read, [])), [setattr(KL_CTX, 'KL_LOC_Check_468', tco_apply(shen_typecheck, [tco_apply(shen_rcons_form, [KL_CTX.KL_LOC_Input_467]), KL_ARG_V2075_466])), ([tco_apply(shen_prhush, [('input is not of type ' + tco_apply(shen_app, [KL_ARG_V2075_466, ': please re-enter ', symdic.symdic_shen_r])), tco_apply(kl_stoutput, [])]), tail_call(readx43, [symdic.symdic_kl_x58, KL_ARG_V2075_466])][(-1)] if shen_eq(False, KL_CTX.KL_LOC_Check_468) else KL_CTX.KL_LOC_Input_467)][(-1)]][(-1)]
shen_add_fun('read+', readx43, 2)

@tail_recursion
def kl_boundx63(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_boundx63, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2076_469 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Val_470 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_Val_470', shen_try_except((lambda : shen_get(KL_ARG_V2076_469)), (lambda KL_ARG_E_471: symdic.symdic_shen_thisx45symbolx45isx45unbound))), (False if shen_eq(KL_CTX.KL_LOC_Val_470, symdic.symdic_shen_thisx45symbolx45isx45unbound) else True)][(-1)] if tco_apply(kl_symbolx63, [KL_ARG_V2076_469]) else False)
shen_add_fun('bound?', kl_boundx63, 1)

@tail_recursion
def shen_stringx45x62bytes(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_stringx45x62bytes, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2077_472 = FUN_ARGS[0]
    global symdic
    return (nil if shen_eq('', KL_ARG_V2077_472) else (Cons(ord(KL_ARG_V2077_472[0]), tco_apply(shen_stringx45x62bytes, [KL_ARG_V2077_472[1:]])) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.string->bytes', shen_stringx45x62bytes, 1)

@tail_recursion
def kl_maxinferences(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_maxinferences, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2078_473 = FUN_ARGS[0]
    global symdic
    return shen_set(symdic.symdic_shen_x42maxinferencesx42, KL_ARG_V2078_473)
shen_add_fun('maxinferences', kl_maxinferences, 1)

@tail_recursion
def kl_inferences(*FUN_ARGS):
    FUN_ARITY = 0
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_inferences, (FUN_ARGS + lambdaargs)))
    global symdic
    return shen_get(symdic.symdic_shen_x42infsx42)
shen_add_fun('inferences', kl_inferences, 0)

@tail_recursion
def kl_protect(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_protect, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2079_474 = FUN_ARGS[0]
    global symdic
    return KL_ARG_V2079_474
shen_add_fun('protect', kl_protect, 1)

@tail_recursion
def kl_stoutput(*FUN_ARGS):
    FUN_ARITY = 0
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_stoutput, (FUN_ARGS + lambdaargs)))
    global symdic
    return shen_get(symdic.symdic_x42stoutputx42)
shen_add_fun('stoutput', kl_stoutput, 0)

@tail_recursion
def kl_stringx45x62symbol(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_stringx45x62symbol, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2080_475 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Symbol_476 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Symbol_476', shen_intern(KL_ARG_V2080_475)), (KL_CTX.KL_LOC_Symbol_476 if tco_apply(kl_symbolx63, [KL_CTX.KL_LOC_Symbol_476]) else shen_simple_error(('cannot intern ' + tco_apply(shen_app, [KL_ARG_V2080_475, ' to a symbol', symdic.symdic_shen_s]))))][(-1)]
shen_add_fun('string->symbol', kl_stringx45x62symbol, 1)

@tail_recursion
def shen_optimise(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_optimise, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2085_477 = FUN_ARGS[0]
    global symdic
    return (shen_set(symdic.symdic_shen_x42optimisex42, True) if shen_eq(symdic.symdic_kl_x43, KL_ARG_V2085_477) else (shen_set(symdic.symdic_shen_x42optimisex42, False) if shen_eq(symdic.symdic_kl_x45, KL_ARG_V2085_477) else (shen_simple_error('optimise expects a + or a -.\r\n') if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.optimise', shen_optimise, 1)


#============================== sequent.kl==============================



@tail_recursion
def shen_datatypex45error(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_datatypex45error, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1632_478 = FUN_ARGS[0]
    global symdic
    return (shen_simple_error(('datatype syntax error here:\r\n\r\n ' + tco_apply(shen_app, [tco_apply(shen_nextx4550, [50, car(KL_ARG_V1632_478)]), '\r\n', symdic.symdic_shen_a]))) if ((shen_eq(nil, cdr(cdr(KL_ARG_V1632_478))) if shen_consp(cdr(KL_ARG_V1632_478)) else False) if shen_consp(KL_ARG_V1632_478) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_datatypex45error]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.datatype-error', shen_datatypex45error, 1)

@tail_recursion
def shen_x60datatypex45rulesx62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60datatypex45rulesx62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1637_479 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_480 = None
        KL_LOC_Parse_shen_x60datatypex45rulex62_481 = None
        KL_LOC_Parse_shen_x60datatypex45rulesx62_482 = None
        KL_LOC_Result_483 = None
        KL_LOC_Parse_x60ex62_484 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_480', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60datatypex45rulex62_481', tco_apply(shen_x60datatypex45rulex62, [KL_ARG_V1637_479])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60datatypex45rulesx62_482', tco_apply(shen_x60datatypex45rulesx62, [KL_CTX.KL_LOC_Parse_shen_x60datatypex45rulex62_481])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60datatypex45rulesx62_482), Cons(tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60datatypex45rulex62_481]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60datatypex45rulesx62_482]))]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60datatypex45rulesx62_482)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60datatypex45rulex62_481)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_483', [setattr(KL_CTX, 'KL_LOC_Parse_x60ex62_484', tco_apply(kl_x60ex62, [KL_ARG_V1637_479])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_x60ex62_484), nil]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_x60ex62_484)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_483, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_483)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_480, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_480)][(-1)]
shen_add_fun('shen.<datatype-rules>', shen_x60datatypex45rulesx62, 1)

@tail_recursion
def shen_x60datatypex45rulex62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60datatypex45rulex62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1642_485 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_486 = None
        KL_LOC_Parse_shen_x60sidex45conditionsx62_487 = None
        KL_LOC_Parse_shen_x60premisesx62_488 = None
        KL_LOC_Parse_shen_x60singleunderlinex62_489 = None
        KL_LOC_Parse_shen_x60conclusionx62_490 = None
        KL_LOC_Result_491 = None
        KL_LOC_Parse_shen_x60sidex45conditionsx62_492 = None
        KL_LOC_Parse_shen_x60premisesx62_493 = None
        KL_LOC_Parse_shen_x60doubleunderlinex62_494 = None
        KL_LOC_Parse_shen_x60conclusionx62_495 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_486', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60sidex45conditionsx62_487', tco_apply(shen_x60sidex45conditionsx62, [KL_ARG_V1642_485])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60premisesx62_488', tco_apply(shen_x60premisesx62, [KL_CTX.KL_LOC_Parse_shen_x60sidex45conditionsx62_487])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60singleunderlinex62_489', tco_apply(shen_x60singleunderlinex62, [KL_CTX.KL_LOC_Parse_shen_x60premisesx62_488])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60conclusionx62_490', tco_apply(shen_x60conclusionx62, [KL_CTX.KL_LOC_Parse_shen_x60singleunderlinex62_489])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60conclusionx62_490), tco_apply(shen_sequent, [symdic.symdic_shen_single, Cons(tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60sidex45conditionsx62_487]), Cons(tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60premisesx62_488]), Cons(tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60conclusionx62_490]), nil)))])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60conclusionx62_490)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60singleunderlinex62_489)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60premisesx62_488)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60sidex45conditionsx62_487)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_491', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60sidex45conditionsx62_492', tco_apply(shen_x60sidex45conditionsx62, [KL_ARG_V1642_485])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60premisesx62_493', tco_apply(shen_x60premisesx62, [KL_CTX.KL_LOC_Parse_shen_x60sidex45conditionsx62_492])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60doubleunderlinex62_494', tco_apply(shen_x60doubleunderlinex62, [KL_CTX.KL_LOC_Parse_shen_x60premisesx62_493])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60conclusionx62_495', tco_apply(shen_x60conclusionx62, [KL_CTX.KL_LOC_Parse_shen_x60doubleunderlinex62_494])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60conclusionx62_495), tco_apply(shen_sequent, [symdic.symdic_shen_double, Cons(tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60sidex45conditionsx62_492]), Cons(tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60premisesx62_493]), Cons(tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60conclusionx62_495]), nil)))])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60conclusionx62_495)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60doubleunderlinex62_494)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60premisesx62_493)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60sidex45conditionsx62_492)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_491, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_491)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_486, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_486)][(-1)]
shen_add_fun('shen.<datatype-rule>', shen_x60datatypex45rulex62, 1)

@tail_recursion
def shen_x60sidex45conditionsx62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60sidex45conditionsx62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1647_496 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_497 = None
        KL_LOC_Parse_shen_x60sidex45conditionx62_498 = None
        KL_LOC_Parse_shen_x60sidex45conditionsx62_499 = None
        KL_LOC_Result_500 = None
        KL_LOC_Parse_x60ex62_501 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_497', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60sidex45conditionx62_498', tco_apply(shen_x60sidex45conditionx62, [KL_ARG_V1647_496])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60sidex45conditionsx62_499', tco_apply(shen_x60sidex45conditionsx62, [KL_CTX.KL_LOC_Parse_shen_x60sidex45conditionx62_498])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60sidex45conditionsx62_499), Cons(tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60sidex45conditionx62_498]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60sidex45conditionsx62_499]))]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60sidex45conditionsx62_499)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60sidex45conditionx62_498)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_500', [setattr(KL_CTX, 'KL_LOC_Parse_x60ex62_501', tco_apply(kl_x60ex62, [KL_ARG_V1647_496])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_x60ex62_501), nil]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_x60ex62_501)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_500, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_500)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_497, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_497)][(-1)]
shen_add_fun('shen.<side-conditions>', shen_x60sidex45conditionsx62, 1)

@tail_recursion
def shen_x60sidex45conditionx62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60sidex45conditionx62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1652_502 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_503 = None
        KL_LOC_Parse_shen_x60exprx62_504 = None
        KL_LOC_Result_505 = None
        KL_LOC_Parse_shen_x60variablex63x62_506 = None
        KL_LOC_Parse_shen_x60exprx62_507 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_503', ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60exprx62_504', tco_apply(shen_x60exprx62, [tco_apply(shen_pair, [cdr(car(KL_ARG_V1652_502)), tco_apply(shen_hdtl, [KL_ARG_V1652_502])])])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60exprx62_504), Cons(symdic.symdic_kl_if, Cons(tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60exprx62_504]), nil))]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60exprx62_504)) else tco_apply(kl_fail, []))][(-1)] if (shen_eq(symdic.symdic_kl_if, car(car(KL_ARG_V1652_502))) if shen_consp(car(KL_ARG_V1652_502)) else False) else tco_apply(kl_fail, []))), ([setattr(KL_CTX, 'KL_LOC_Result_505', ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60variablex63x62_506', tco_apply(shen_x60variablex63x62, [tco_apply(shen_pair, [cdr(car(KL_ARG_V1652_502)), tco_apply(shen_hdtl, [KL_ARG_V1652_502])])])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60exprx62_507', tco_apply(shen_x60exprx62, [KL_CTX.KL_LOC_Parse_shen_x60variablex63x62_506])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60exprx62_507), Cons(symdic.symdic_kl_let, Cons(tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60variablex63x62_506]), Cons(tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60exprx62_507]), nil)))]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60exprx62_507)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60variablex63x62_506)) else tco_apply(kl_fail, []))][(-1)] if (shen_eq(symdic.symdic_kl_let, car(car(KL_ARG_V1652_502))) if shen_consp(car(KL_ARG_V1652_502)) else False) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_505, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_505)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_503, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_503)][(-1)]
shen_add_fun('shen.<side-condition>', shen_x60sidex45conditionx62, 1)

@tail_recursion
def shen_x60variablex63x62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60variablex63x62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1657_508 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_509 = None
        KL_LOC_Parse_X_510 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_509', ([setattr(KL_CTX, 'KL_LOC_Parse_X_510', car(car(KL_ARG_V1657_508))), (tco_apply(shen_pair, [car(tco_apply(shen_pair, [cdr(car(KL_ARG_V1657_508)), tco_apply(shen_hdtl, [KL_ARG_V1657_508])])), KL_CTX.KL_LOC_Parse_X_510]) if tco_apply(kl_variablex63, [KL_CTX.KL_LOC_Parse_X_510]) else tco_apply(kl_fail, []))][(-1)] if shen_consp(car(KL_ARG_V1657_508)) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_509, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_509)][(-1)]
shen_add_fun('shen.<variable?>', shen_x60variablex63x62, 1)

@tail_recursion
def shen_x60exprx62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60exprx62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1662_511 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_512 = None
        KL_LOC_Parse_X_513 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_512', ([setattr(KL_CTX, 'KL_LOC_Parse_X_513', car(car(KL_ARG_V1662_511))), (tco_apply(shen_pair, [car(tco_apply(shen_pair, [cdr(car(KL_ARG_V1662_511)), tco_apply(shen_hdtl, [KL_ARG_V1662_511])])), tco_apply(shen_removex45bar, [KL_CTX.KL_LOC_Parse_X_513])]) if (not (True if tco_apply(kl_elementx63, [KL_CTX.KL_LOC_Parse_X_513, Cons(symdic.symdic_kl_x62x62, Cons(symdic.symdic_kl_x59, nil))]) else (True if tco_apply(shen_singleunderlinex63, [KL_CTX.KL_LOC_Parse_X_513]) else tco_apply(shen_doubleunderlinex63, [KL_CTX.KL_LOC_Parse_X_513])))) else tco_apply(kl_fail, []))][(-1)] if shen_consp(car(KL_ARG_V1662_511)) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_512, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_512)][(-1)]
shen_add_fun('shen.<expr>', shen_x60exprx62, 1)

@tail_recursion
def shen_removex45bar(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_removex45bar, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1663_514 = FUN_ARGS[0]
    global symdic
    return (Cons(car(KL_ARG_V1663_514), car(cdr(cdr(KL_ARG_V1663_514)))) if ((((shen_eq(car(cdr(KL_ARG_V1663_514)), symdic.symdic_kl_barx33) if shen_eq(nil, cdr(cdr(cdr(KL_ARG_V1663_514)))) else False) if shen_consp(cdr(cdr(KL_ARG_V1663_514))) else False) if shen_consp(cdr(KL_ARG_V1663_514)) else False) if shen_consp(KL_ARG_V1663_514) else False) else (Cons(tco_apply(shen_removex45bar, [car(KL_ARG_V1663_514)]), tco_apply(shen_removex45bar, [cdr(KL_ARG_V1663_514)])) if shen_consp(KL_ARG_V1663_514) else (KL_ARG_V1663_514 if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.remove-bar', shen_removex45bar, 1)

@tail_recursion
def shen_x60premisesx62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60premisesx62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1668_515 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_516 = None
        KL_LOC_Parse_shen_x60premisex62_517 = None
        KL_LOC_Parse_shen_x60semicolonx45symbolx62_518 = None
        KL_LOC_Parse_shen_x60premisesx62_519 = None
        KL_LOC_Result_520 = None
        KL_LOC_Parse_x60ex62_521 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_516', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60premisex62_517', tco_apply(shen_x60premisex62, [KL_ARG_V1668_515])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60semicolonx45symbolx62_518', tco_apply(shen_x60semicolonx45symbolx62, [KL_CTX.KL_LOC_Parse_shen_x60premisex62_517])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60premisesx62_519', tco_apply(shen_x60premisesx62, [KL_CTX.KL_LOC_Parse_shen_x60semicolonx45symbolx62_518])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60premisesx62_519), Cons(tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60premisex62_517]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60premisesx62_519]))]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60premisesx62_519)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60semicolonx45symbolx62_518)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60premisex62_517)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_520', [setattr(KL_CTX, 'KL_LOC_Parse_x60ex62_521', tco_apply(kl_x60ex62, [KL_ARG_V1668_515])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_x60ex62_521), nil]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_x60ex62_521)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_520, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_520)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_516, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_516)][(-1)]
shen_add_fun('shen.<premises>', shen_x60premisesx62, 1)

@tail_recursion
def shen_x60semicolonx45symbolx62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60semicolonx45symbolx62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1673_522 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_523 = None
        KL_LOC_Parse_X_524 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_523', ([setattr(KL_CTX, 'KL_LOC_Parse_X_524', car(car(KL_ARG_V1673_522))), (tco_apply(shen_pair, [car(tco_apply(shen_pair, [cdr(car(KL_ARG_V1673_522)), tco_apply(shen_hdtl, [KL_ARG_V1673_522])])), symdic.symdic_shen_skip]) if shen_eq(KL_CTX.KL_LOC_Parse_X_524, symdic.symdic_kl_x59) else tco_apply(kl_fail, []))][(-1)] if shen_consp(car(KL_ARG_V1673_522)) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_523, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_523)][(-1)]
shen_add_fun('shen.<semicolon-symbol>', shen_x60semicolonx45symbolx62, 1)

@tail_recursion
def shen_x60premisex62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60premisex62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1678_525 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_526 = None
        KL_LOC_Result_527 = None
        KL_LOC_Parse_shen_x60formulaex62_528 = None
        KL_LOC_Parse_shen_x60formulax62_529 = None
        KL_LOC_Result_530 = None
        KL_LOC_Parse_shen_x60formulax62_531 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_526', (tco_apply(shen_pair, [car(tco_apply(shen_pair, [cdr(car(KL_ARG_V1678_525)), tco_apply(shen_hdtl, [KL_ARG_V1678_525])])), symdic.symdic_kl_x33]) if (shen_eq(symdic.symdic_kl_x33, car(car(KL_ARG_V1678_525))) if shen_consp(car(KL_ARG_V1678_525)) else False) else tco_apply(kl_fail, []))), ([setattr(KL_CTX, 'KL_LOC_Result_527', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60formulaex62_528', tco_apply(shen_x60formulaex62, [KL_ARG_V1678_525])), (([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60formulax62_529', tco_apply(shen_x60formulax62, [tco_apply(shen_pair, [cdr(car(KL_CTX.KL_LOC_Parse_shen_x60formulaex62_528)), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60formulaex62_528])])])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60formulax62_529), tco_apply(shen_sequent, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60formulaex62_528]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60formulax62_529])])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60formulax62_529)) else tco_apply(kl_fail, []))][(-1)] if (shen_eq(symdic.symdic_kl_x62x62, car(car(KL_CTX.KL_LOC_Parse_shen_x60formulaex62_528))) if shen_consp(car(KL_CTX.KL_LOC_Parse_shen_x60formulaex62_528)) else False) else tco_apply(kl_fail, [])) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60formulaex62_528)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_530', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60formulax62_531', tco_apply(shen_x60formulax62, [KL_ARG_V1678_525])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60formulax62_531), tco_apply(shen_sequent, [nil, tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60formulax62_531])])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60formulax62_531)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_530, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_530)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_527, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_527)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_526, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_526)][(-1)]
shen_add_fun('shen.<premise>', shen_x60premisex62, 1)

@tail_recursion
def shen_x60conclusionx62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60conclusionx62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1683_532 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_533 = None
        KL_LOC_Parse_shen_x60formulaex62_534 = None
        KL_LOC_Parse_shen_x60formulax62_535 = None
        KL_LOC_Parse_shen_x60semicolonx45symbolx62_536 = None
        KL_LOC_Result_537 = None
        KL_LOC_Parse_shen_x60formulax62_538 = None
        KL_LOC_Parse_shen_x60semicolonx45symbolx62_539 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_533', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60formulaex62_534', tco_apply(shen_x60formulaex62, [KL_ARG_V1683_532])), (([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60formulax62_535', tco_apply(shen_x60formulax62, [tco_apply(shen_pair, [cdr(car(KL_CTX.KL_LOC_Parse_shen_x60formulaex62_534)), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60formulaex62_534])])])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60semicolonx45symbolx62_536', tco_apply(shen_x60semicolonx45symbolx62, [KL_CTX.KL_LOC_Parse_shen_x60formulax62_535])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60semicolonx45symbolx62_536), tco_apply(shen_sequent, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60formulaex62_534]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60formulax62_535])])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60semicolonx45symbolx62_536)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60formulax62_535)) else tco_apply(kl_fail, []))][(-1)] if (shen_eq(symdic.symdic_kl_x62x62, car(car(KL_CTX.KL_LOC_Parse_shen_x60formulaex62_534))) if shen_consp(car(KL_CTX.KL_LOC_Parse_shen_x60formulaex62_534)) else False) else tco_apply(kl_fail, [])) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60formulaex62_534)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_537', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60formulax62_538', tco_apply(shen_x60formulax62, [KL_ARG_V1683_532])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60semicolonx45symbolx62_539', tco_apply(shen_x60semicolonx45symbolx62, [KL_CTX.KL_LOC_Parse_shen_x60formulax62_538])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60semicolonx45symbolx62_539), tco_apply(shen_sequent, [nil, tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60formulax62_538])])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60semicolonx45symbolx62_539)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60formulax62_538)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_537, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_537)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_533, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_533)][(-1)]
shen_add_fun('shen.<conclusion>', shen_x60conclusionx62, 1)

@tail_recursion
def shen_sequent(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_sequent, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1684_540 = FUN_ARGS[0]
    KL_ARG_V1685_541 = FUN_ARGS[1]
    global symdic
    return tail_call(kl_x64p, [KL_ARG_V1684_540, KL_ARG_V1685_541])
shen_add_fun('shen.sequent', shen_sequent, 2)

@tail_recursion
def shen_x60formulaex62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60formulaex62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1690_542 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_543 = None
        KL_LOC_Parse_shen_x60formulax62_544 = None
        KL_LOC_Parse_shen_x60commax45symbolx62_545 = None
        KL_LOC_Parse_shen_x60formulaex62_546 = None
        KL_LOC_Result_547 = None
        KL_LOC_Parse_shen_x60formulax62_548 = None
        KL_LOC_Result_549 = None
        KL_LOC_Parse_x60ex62_550 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_543', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60formulax62_544', tco_apply(shen_x60formulax62, [KL_ARG_V1690_542])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60commax45symbolx62_545', tco_apply(shen_x60commax45symbolx62, [KL_CTX.KL_LOC_Parse_shen_x60formulax62_544])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60formulaex62_546', tco_apply(shen_x60formulaex62, [KL_CTX.KL_LOC_Parse_shen_x60commax45symbolx62_545])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60formulaex62_546), Cons(tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60formulax62_544]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60formulaex62_546]))]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60formulaex62_546)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60commax45symbolx62_545)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60formulax62_544)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_547', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60formulax62_548', tco_apply(shen_x60formulax62, [KL_ARG_V1690_542])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60formulax62_548), Cons(tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60formulax62_548]), nil)]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60formulax62_548)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_549', [setattr(KL_CTX, 'KL_LOC_Parse_x60ex62_550', tco_apply(kl_x60ex62, [KL_ARG_V1690_542])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_x60ex62_550), nil]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_x60ex62_550)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_549, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_549)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_547, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_547)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_543, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_543)][(-1)]
shen_add_fun('shen.<formulae>', shen_x60formulaex62, 1)

@tail_recursion
def shen_x60commax45symbolx62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60commax45symbolx62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1695_551 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_552 = None
        KL_LOC_Parse_X_553 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_552', ([setattr(KL_CTX, 'KL_LOC_Parse_X_553', car(car(KL_ARG_V1695_551))), (tco_apply(shen_pair, [car(tco_apply(shen_pair, [cdr(car(KL_ARG_V1695_551)), tco_apply(shen_hdtl, [KL_ARG_V1695_551])])), symdic.symdic_shen_skip]) if shen_eq(KL_CTX.KL_LOC_Parse_X_553, shen_intern(',')) else tco_apply(kl_fail, []))][(-1)] if shen_consp(car(KL_ARG_V1695_551)) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_552, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_552)][(-1)]
shen_add_fun('shen.<comma-symbol>', shen_x60commax45symbolx62, 1)

@tail_recursion
def shen_x60formulax62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60formulax62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1700_554 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_555 = None
        KL_LOC_Parse_shen_x60exprx62_556 = None
        KL_LOC_Parse_shen_x60typex62_557 = None
        KL_LOC_Result_558 = None
        KL_LOC_Parse_shen_x60exprx62_559 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_555', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60exprx62_556', tco_apply(shen_x60exprx62, [KL_ARG_V1700_554])), (([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60typex62_557', tco_apply(shen_x60typex62, [tco_apply(shen_pair, [cdr(car(KL_CTX.KL_LOC_Parse_shen_x60exprx62_556)), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60exprx62_556])])])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60typex62_557), Cons(tco_apply(shen_curry, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60exprx62_556])]), Cons(symdic.symdic_kl_x58, Cons(tco_apply(shen_demodulate, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60typex62_557])]), nil)))]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60typex62_557)) else tco_apply(kl_fail, []))][(-1)] if (shen_eq(symdic.symdic_kl_x58, car(car(KL_CTX.KL_LOC_Parse_shen_x60exprx62_556))) if shen_consp(car(KL_CTX.KL_LOC_Parse_shen_x60exprx62_556)) else False) else tco_apply(kl_fail, [])) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60exprx62_556)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_558', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60exprx62_559', tco_apply(shen_x60exprx62, [KL_ARG_V1700_554])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60exprx62_559), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60exprx62_559])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60exprx62_559)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_558, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_558)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_555, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_555)][(-1)]
shen_add_fun('shen.<formula>', shen_x60formulax62, 1)

@tail_recursion
def shen_x60typex62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60typex62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1705_560 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_561 = None
        KL_LOC_Parse_shen_x60exprx62_562 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_561', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60exprx62_562', tco_apply(shen_x60exprx62, [KL_ARG_V1705_560])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60exprx62_562), tco_apply(shen_curryx45type, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60exprx62_562])])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60exprx62_562)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_561, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_561)][(-1)]
shen_add_fun('shen.<type>', shen_x60typex62, 1)

@tail_recursion
def shen_x60doubleunderlinex62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60doubleunderlinex62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1710_563 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_564 = None
        KL_LOC_Parse_X_565 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_564', ([setattr(KL_CTX, 'KL_LOC_Parse_X_565', car(car(KL_ARG_V1710_563))), (tco_apply(shen_pair, [car(tco_apply(shen_pair, [cdr(car(KL_ARG_V1710_563)), tco_apply(shen_hdtl, [KL_ARG_V1710_563])])), KL_CTX.KL_LOC_Parse_X_565]) if tco_apply(shen_doubleunderlinex63, [KL_CTX.KL_LOC_Parse_X_565]) else tco_apply(kl_fail, []))][(-1)] if shen_consp(car(KL_ARG_V1710_563)) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_564, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_564)][(-1)]
shen_add_fun('shen.<doubleunderline>', shen_x60doubleunderlinex62, 1)

@tail_recursion
def shen_x60singleunderlinex62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60singleunderlinex62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1715_566 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_567 = None
        KL_LOC_Parse_X_568 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_567', ([setattr(KL_CTX, 'KL_LOC_Parse_X_568', car(car(KL_ARG_V1715_566))), (tco_apply(shen_pair, [car(tco_apply(shen_pair, [cdr(car(KL_ARG_V1715_566)), tco_apply(shen_hdtl, [KL_ARG_V1715_566])])), KL_CTX.KL_LOC_Parse_X_568]) if tco_apply(shen_singleunderlinex63, [KL_CTX.KL_LOC_Parse_X_568]) else tco_apply(kl_fail, []))][(-1)] if shen_consp(car(KL_ARG_V1715_566)) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_567, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_567)][(-1)]
shen_add_fun('shen.<singleunderline>', shen_x60singleunderlinex62, 1)

@tail_recursion
def shen_singleunderlinex63(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_singleunderlinex63, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1716_569 = FUN_ARGS[0]
    global symdic
    return (tail_call(shen_shx63, [str(KL_ARG_V1716_569)]) if tco_apply(kl_symbolx63, [KL_ARG_V1716_569]) else False)
shen_add_fun('shen.singleunderline?', shen_singleunderlinex63, 1)

@tail_recursion
def shen_shx63(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_shx63, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1717_570 = FUN_ARGS[0]
    global symdic
    return (True if shen_eq('_', KL_ARG_V1717_570) else ((tail_call(shen_shx63, [KL_ARG_V1717_570[1:]]) if shen_eq(KL_ARG_V1717_570[0], '_') else False) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.sh?', shen_shx63, 1)

@tail_recursion
def shen_doubleunderlinex63(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_doubleunderlinex63, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1718_571 = FUN_ARGS[0]
    global symdic
    return (tail_call(shen_dhx63, [str(KL_ARG_V1718_571)]) if tco_apply(kl_symbolx63, [KL_ARG_V1718_571]) else False)
shen_add_fun('shen.doubleunderline?', shen_doubleunderlinex63, 1)

@tail_recursion
def shen_dhx63(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_dhx63, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1719_572 = FUN_ARGS[0]
    global symdic
    return (True if shen_eq('=', KL_ARG_V1719_572) else ((tail_call(shen_dhx63, [KL_ARG_V1719_572[1:]]) if shen_eq(KL_ARG_V1719_572[0], '=') else False) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.dh?', shen_dhx63, 1)

@tail_recursion
def shen_processx45datatype(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_processx45datatype, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1720_573 = FUN_ARGS[0]
    KL_ARG_V1721_574 = FUN_ARGS[1]
    global symdic
    return tail_call(shen_rememberx45datatype, [tco_apply(shen_sx45prolog, [tco_apply(shen_rulesx45x62hornx45clauses, [KL_ARG_V1720_573, KL_ARG_V1721_574])])])
shen_add_fun('shen.process-datatype', shen_processx45datatype, 2)

@tail_recursion
def shen_rememberx45datatype(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_rememberx45datatype, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1726_575 = FUN_ARGS[0]
    global symdic
    return ([shen_set(symdic.symdic_shen_x42datatypesx42, tco_apply(kl_adjoin, [car(KL_ARG_V1726_575), shen_get(symdic.symdic_shen_x42datatypesx42)])), [shen_set(symdic.symdic_shen_x42alldatatypesx42, tco_apply(kl_adjoin, [car(KL_ARG_V1726_575), shen_get(symdic.symdic_shen_x42alldatatypesx42)])), car(KL_ARG_V1726_575)][(-1)]][(-1)] if shen_consp(KL_ARG_V1726_575) else (tail_call(shen_sysx45error, [symdic.symdic_shen_rememberx45datatype]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.remember-datatype', shen_rememberx45datatype, 1)

@tail_recursion
def shen_rulesx45x62hornx45clauses(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_rulesx45x62hornx45clauses, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1729_576 = FUN_ARGS[0]
    KL_ARG_V1730_577 = FUN_ARGS[1]
    global symdic
    return (nil if shen_eq(nil, KL_ARG_V1730_577) else (Cons(tco_apply(shen_rulex45x62hornx45clause, [KL_ARG_V1729_576, tco_apply(kl_snd, [car(KL_ARG_V1730_577)])]), tco_apply(shen_rulesx45x62hornx45clauses, [KL_ARG_V1729_576, cdr(KL_ARG_V1730_577)])) if ((shen_eq(symdic.symdic_shen_single, tco_apply(kl_fst, [car(KL_ARG_V1730_577)])) if tco_apply(kl_tuplex63, [car(KL_ARG_V1730_577)]) else False) if shen_consp(KL_ARG_V1730_577) else False) else (tail_call(shen_rulesx45x62hornx45clauses, [KL_ARG_V1729_576, tco_apply(kl_append, [tco_apply(shen_doublex45x62singles, [tco_apply(kl_snd, [car(KL_ARG_V1730_577)])]), cdr(KL_ARG_V1730_577)])]) if ((shen_eq(symdic.symdic_shen_double, tco_apply(kl_fst, [car(KL_ARG_V1730_577)])) if tco_apply(kl_tuplex63, [car(KL_ARG_V1730_577)]) else False) if shen_consp(KL_ARG_V1730_577) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_rulesx45x62hornx45clauses]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.rules->horn-clauses', shen_rulesx45x62hornx45clauses, 2)

@tail_recursion
def shen_doublex45x62singles(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_doublex45x62singles, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1731_578 = FUN_ARGS[0]
    global symdic
    return Cons(tco_apply(shen_rightx45rule, [KL_ARG_V1731_578]), Cons(tco_apply(shen_leftx45rule, [KL_ARG_V1731_578]), nil))
shen_add_fun('shen.double->singles', shen_doublex45x62singles, 1)

@tail_recursion
def shen_rightx45rule(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_rightx45rule, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1732_579 = FUN_ARGS[0]
    global symdic
    return tail_call(kl_x64p, [symdic.symdic_shen_single, KL_ARG_V1732_579])
shen_add_fun('shen.right-rule', shen_rightx45rule, 1)

@tail_recursion
def shen_leftx45rule(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_leftx45rule, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1733_580 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Q_581 = None
        KL_LOC_NewConclusion_582 = None
        KL_LOC_NewPremises_583 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_Q_581', tco_apply(kl_gensym, [symdic.symdic_Qv])), [setattr(KL_CTX, 'KL_LOC_NewConclusion_582', tco_apply(kl_x64p, [Cons(tco_apply(kl_snd, [car(cdr(cdr(KL_ARG_V1733_580)))]), nil), KL_CTX.KL_LOC_Q_581])), [setattr(KL_CTX, 'KL_LOC_NewPremises_583', Cons(tco_apply(kl_x64p, [tco_apply(kl_map, [symdic.symdic_shen_rightx45x62left, car(cdr(KL_ARG_V1733_580))]), KL_CTX.KL_LOC_Q_581]), nil)), tail_call(kl_x64p, [symdic.symdic_shen_single, Cons(car(KL_ARG_V1733_580), Cons(KL_CTX.KL_LOC_NewPremises_583, Cons(KL_CTX.KL_LOC_NewConclusion_582, nil)))])][(-1)]][(-1)]][(-1)] if (((((shen_eq(nil, cdr(cdr(cdr(KL_ARG_V1733_580)))) if shen_eq(nil, tco_apply(kl_fst, [car(cdr(cdr(KL_ARG_V1733_580)))])) else False) if tco_apply(kl_tuplex63, [car(cdr(cdr(KL_ARG_V1733_580)))]) else False) if shen_consp(cdr(cdr(KL_ARG_V1733_580))) else False) if shen_consp(cdr(KL_ARG_V1733_580)) else False) if shen_consp(KL_ARG_V1733_580) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_leftx45rule]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.left-rule', shen_leftx45rule, 1)

@tail_recursion
def shen_rightx45x62left(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_rightx45x62left, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1738_584 = FUN_ARGS[0]
    global symdic
    return (tail_call(kl_snd, [KL_ARG_V1738_584]) if (shen_eq(nil, tco_apply(kl_fst, [KL_ARG_V1738_584])) if tco_apply(kl_tuplex63, [KL_ARG_V1738_584]) else False) else (shen_simple_error('syntax error with ==========\r\n') if True else shen_simple_error('condition failure')))
shen_add_fun('shen.right->left', shen_rightx45x62left, 1)

@tail_recursion
def shen_rulex45x62hornx45clause(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_rulex45x62hornx45clause, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1739_585 = FUN_ARGS[0]
    KL_ARG_V1740_586 = FUN_ARGS[1]
    global symdic
    return (Cons(tco_apply(shen_rulex45x62hornx45clausex45head, [KL_ARG_V1739_585, tco_apply(kl_snd, [car(cdr(cdr(KL_ARG_V1740_586)))])]), Cons(symdic.symdic_kl_x58x45, Cons(tco_apply(shen_rulex45x62hornx45clausex45body, [car(KL_ARG_V1740_586), car(cdr(KL_ARG_V1740_586)), tco_apply(kl_fst, [car(cdr(cdr(KL_ARG_V1740_586)))])]), nil))) if ((((shen_eq(nil, cdr(cdr(cdr(KL_ARG_V1740_586)))) if tco_apply(kl_tuplex63, [car(cdr(cdr(KL_ARG_V1740_586)))]) else False) if shen_consp(cdr(cdr(KL_ARG_V1740_586))) else False) if shen_consp(cdr(KL_ARG_V1740_586)) else False) if shen_consp(KL_ARG_V1740_586) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_rulex45x62hornx45clause]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.rule->horn-clause', shen_rulex45x62hornx45clause, 2)

@tail_recursion
def shen_rulex45x62hornx45clausex45head(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_rulex45x62hornx45clausex45head, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1741_587 = FUN_ARGS[0]
    KL_ARG_V1742_588 = FUN_ARGS[1]
    global symdic
    return Cons(KL_ARG_V1741_587, Cons(tco_apply(shen_modex45ify, [KL_ARG_V1742_588]), Cons(symdic.symdic_Context_1957, nil)))
shen_add_fun('shen.rule->horn-clause-head', shen_rulex45x62hornx45clausex45head, 2)

@tail_recursion
def shen_modex45ify(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_modex45ify, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1743_589 = FUN_ARGS[0]
    global symdic
    return (Cons(symdic.symdic_kl_mode, Cons(Cons(car(KL_ARG_V1743_589), Cons(symdic.symdic_kl_x58, Cons(Cons(symdic.symdic_kl_mode, Cons(car(cdr(cdr(KL_ARG_V1743_589))), Cons(symdic.symdic_kl_x43, nil))), nil))), Cons(symdic.symdic_kl_x45, nil))) if ((((shen_eq(nil, cdr(cdr(cdr(KL_ARG_V1743_589)))) if shen_consp(cdr(cdr(KL_ARG_V1743_589))) else False) if shen_eq(symdic.symdic_kl_x58, car(cdr(KL_ARG_V1743_589))) else False) if shen_consp(cdr(KL_ARG_V1743_589)) else False) if shen_consp(KL_ARG_V1743_589) else False) else (KL_ARG_V1743_589 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.mode-ify', shen_modex45ify, 1)

@tail_recursion
def shen_rulex45x62hornx45clausex45body(*FUN_ARGS):
    FUN_ARITY = 3
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_rulex45x62hornx45clausex45body, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1744_590 = FUN_ARGS[0]
    KL_ARG_V1745_591 = FUN_ARGS[1]
    KL_ARG_V1746_592 = FUN_ARGS[2]

    class KL_Context:
        KL_LOC_Variables_593 = None
        KL_LOC_Predicates_594 = None
        KL_LOC_SearchLiterals_596 = None
        KL_LOC_SearchClauses_597 = None
        KL_LOC_SideLiterals_598 = None
        KL_LOC_PremissLiterals_599 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Variables_593', tco_apply(kl_map, [symdic.symdic_shen_extract_vars, KL_ARG_V1746_592])), [setattr(KL_CTX, 'KL_LOC_Predicates_594', tco_apply(kl_map, [(lambda KL_ARG_X_595: tail_call(kl_gensym, [symdic.symdic_shen_cl])), KL_ARG_V1746_592])), [setattr(KL_CTX, 'KL_LOC_SearchLiterals_596', tco_apply(shen_constructx45searchx45literals, [KL_CTX.KL_LOC_Predicates_594, KL_CTX.KL_LOC_Variables_593, symdic.symdic_Context_1957, symdic.symdic_Context1_1957])), [setattr(KL_CTX, 'KL_LOC_SearchClauses_597', tco_apply(shen_constructx45searchx45clauses, [KL_CTX.KL_LOC_Predicates_594, KL_ARG_V1746_592, KL_CTX.KL_LOC_Variables_593])), [setattr(KL_CTX, 'KL_LOC_SideLiterals_598', tco_apply(shen_constructx45sidex45literals, [KL_ARG_V1744_590])), [setattr(KL_CTX, 'KL_LOC_PremissLiterals_599', tco_apply(kl_map, [(lambda KL_ARG_X_600: tail_call(shen_constructx45premissx45literal, [KL_ARG_X_600, tco_apply(kl_emptyx63, [KL_ARG_V1746_592])])), KL_ARG_V1745_591])), tail_call(kl_append, [KL_CTX.KL_LOC_SearchLiterals_596, tco_apply(kl_append, [KL_CTX.KL_LOC_SideLiterals_598, KL_CTX.KL_LOC_PremissLiterals_599])])][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]
shen_add_fun('shen.rule->horn-clause-body', shen_rulex45x62hornx45clausex45body, 3)

@tail_recursion
def shen_constructx45searchx45literals(*FUN_ARGS):
    FUN_ARITY = 4
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_constructx45searchx45literals, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1751_601 = FUN_ARGS[0]
    KL_ARG_V1752_602 = FUN_ARGS[1]
    KL_ARG_V1753_603 = FUN_ARGS[2]
    KL_ARG_V1754_604 = FUN_ARGS[3]
    global symdic
    return (nil if (shen_eq(nil, KL_ARG_V1752_602) if shen_eq(nil, KL_ARG_V1751_601) else False) else (tail_call(shen_cslx45help, [KL_ARG_V1751_601, KL_ARG_V1752_602, KL_ARG_V1753_603, KL_ARG_V1754_604]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.construct-search-literals', shen_constructx45searchx45literals, 4)

@tail_recursion
def shen_cslx45help(*FUN_ARGS):
    FUN_ARITY = 4
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_cslx45help, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1757_605 = FUN_ARGS[0]
    KL_ARG_V1758_606 = FUN_ARGS[1]
    KL_ARG_V1759_607 = FUN_ARGS[2]
    KL_ARG_V1760_608 = FUN_ARGS[3]
    global symdic
    return (Cons(Cons(symdic.symdic_kl_bind, Cons(symdic.symdic_ContextOut_1957, Cons(KL_ARG_V1759_607, nil))), nil) if (shen_eq(nil, KL_ARG_V1758_606) if shen_eq(nil, KL_ARG_V1757_605) else False) else (Cons(Cons(car(KL_ARG_V1757_605), Cons(KL_ARG_V1759_607, Cons(KL_ARG_V1760_608, car(KL_ARG_V1758_606)))), tco_apply(shen_cslx45help, [cdr(KL_ARG_V1757_605), cdr(KL_ARG_V1758_606), KL_ARG_V1760_608, tco_apply(kl_gensym, [symdic.symdic_Context])])) if (shen_consp(KL_ARG_V1758_606) if shen_consp(KL_ARG_V1757_605) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_cslx45help]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.csl-help', shen_cslx45help, 4)

@tail_recursion
def shen_constructx45searchx45clauses(*FUN_ARGS):
    FUN_ARITY = 3
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_constructx45searchx45clauses, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1761_609 = FUN_ARGS[0]
    KL_ARG_V1762_610 = FUN_ARGS[1]
    KL_ARG_V1763_611 = FUN_ARGS[2]
    global symdic
    return (symdic.symdic_shen_skip if ((shen_eq(nil, KL_ARG_V1763_611) if shen_eq(nil, KL_ARG_V1762_610) else False) if shen_eq(nil, KL_ARG_V1761_609) else False) else ([tco_apply(shen_constructx45searchx45clause, [car(KL_ARG_V1761_609), car(KL_ARG_V1762_610), car(KL_ARG_V1763_611)]), tail_call(shen_constructx45searchx45clauses, [cdr(KL_ARG_V1761_609), cdr(KL_ARG_V1762_610), cdr(KL_ARG_V1763_611)])][(-1)] if ((shen_consp(KL_ARG_V1763_611) if shen_consp(KL_ARG_V1762_610) else False) if shen_consp(KL_ARG_V1761_609) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_constructx45searchx45clauses]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.construct-search-clauses', shen_constructx45searchx45clauses, 3)

@tail_recursion
def shen_constructx45searchx45clause(*FUN_ARGS):
    FUN_ARITY = 3
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_constructx45searchx45clause, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1764_612 = FUN_ARGS[0]
    KL_ARG_V1765_613 = FUN_ARGS[1]
    KL_ARG_V1766_614 = FUN_ARGS[2]
    global symdic
    return tail_call(shen_sx45prolog, [Cons(tco_apply(shen_constructx45basex45searchx45clause, [KL_ARG_V1764_612, KL_ARG_V1765_613, KL_ARG_V1766_614]), Cons(tco_apply(shen_constructx45recursivex45searchx45clause, [KL_ARG_V1764_612, KL_ARG_V1765_613, KL_ARG_V1766_614]), nil))])
shen_add_fun('shen.construct-search-clause', shen_constructx45searchx45clause, 3)

@tail_recursion
def shen_constructx45basex45searchx45clause(*FUN_ARGS):
    FUN_ARITY = 3
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_constructx45basex45searchx45clause, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1767_615 = FUN_ARGS[0]
    KL_ARG_V1768_616 = FUN_ARGS[1]
    KL_ARG_V1769_617 = FUN_ARGS[2]
    global symdic
    return Cons(Cons(KL_ARG_V1767_615, Cons(Cons(tco_apply(shen_modex45ify, [KL_ARG_V1768_616]), symdic.symdic_In_1957), Cons(symdic.symdic_In_1957, KL_ARG_V1769_617))), Cons(symdic.symdic_kl_x58x45, Cons(nil, nil)))
shen_add_fun('shen.construct-base-search-clause', shen_constructx45basex45searchx45clause, 3)

@tail_recursion
def shen_constructx45recursivex45searchx45clause(*FUN_ARGS):
    FUN_ARITY = 3
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_constructx45recursivex45searchx45clause, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1770_618 = FUN_ARGS[0]
    KL_ARG_V1771_619 = FUN_ARGS[1]
    KL_ARG_V1772_620 = FUN_ARGS[2]
    global symdic
    return Cons(Cons(KL_ARG_V1770_618, Cons(Cons(symdic.symdic_Assumption_1957, symdic.symdic_Assumptions_1957), Cons(Cons(symdic.symdic_Assumption_1957, symdic.symdic_Out_1957), KL_ARG_V1772_620))), Cons(symdic.symdic_kl_x58x45, Cons(Cons(Cons(KL_ARG_V1770_618, Cons(symdic.symdic_Assumptions_1957, Cons(symdic.symdic_Out_1957, KL_ARG_V1772_620))), nil), nil)))
shen_add_fun('shen.construct-recursive-search-clause', shen_constructx45recursivex45searchx45clause, 3)

@tail_recursion
def shen_constructx45sidex45literals(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_constructx45sidex45literals, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1777_621 = FUN_ARGS[0]
    global symdic
    return (nil if shen_eq(nil, KL_ARG_V1777_621) else (Cons(Cons(symdic.symdic_kl_when, cdr(car(KL_ARG_V1777_621))), tco_apply(shen_constructx45sidex45literals, [cdr(KL_ARG_V1777_621)])) if ((((shen_eq(nil, cdr(cdr(car(KL_ARG_V1777_621)))) if shen_consp(cdr(car(KL_ARG_V1777_621))) else False) if shen_eq(symdic.symdic_kl_if, car(car(KL_ARG_V1777_621))) else False) if shen_consp(car(KL_ARG_V1777_621)) else False) if shen_consp(KL_ARG_V1777_621) else False) else (Cons(Cons(symdic.symdic_kl_is, cdr(car(KL_ARG_V1777_621))), tco_apply(shen_constructx45sidex45literals, [cdr(KL_ARG_V1777_621)])) if (((((shen_eq(nil, cdr(cdr(cdr(car(KL_ARG_V1777_621))))) if shen_consp(cdr(cdr(car(KL_ARG_V1777_621)))) else False) if shen_consp(cdr(car(KL_ARG_V1777_621))) else False) if shen_eq(symdic.symdic_kl_let, car(car(KL_ARG_V1777_621))) else False) if shen_consp(car(KL_ARG_V1777_621)) else False) if shen_consp(KL_ARG_V1777_621) else False) else (tail_call(shen_constructx45sidex45literals, [cdr(KL_ARG_V1777_621)]) if shen_consp(KL_ARG_V1777_621) else (tail_call(shen_sysx45error, [symdic.symdic_shen_constructx45sidex45literals]) if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.construct-side-literals', shen_constructx45sidex45literals, 1)

@tail_recursion
def shen_constructx45premissx45literal(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_constructx45premissx45literal, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1782_622 = FUN_ARGS[0]
    KL_ARG_V1783_623 = FUN_ARGS[1]
    global symdic
    return (Cons(symdic.symdic_shen_tx42, Cons(tco_apply(shen_recursive_cons_form, [tco_apply(kl_snd, [KL_ARG_V1782_622])]), Cons(tco_apply(shen_constructx45context, [KL_ARG_V1783_623, tco_apply(kl_fst, [KL_ARG_V1782_622])]), nil))) if tco_apply(kl_tuplex63, [KL_ARG_V1782_622]) else (Cons(symdic.symdic_kl_cut, Cons(symdic.symdic_Throwcontrol, nil)) if shen_eq(symdic.symdic_kl_x33, KL_ARG_V1782_622) else (tail_call(shen_sysx45error, [symdic.symdic_shen_constructx45premissx45literal]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.construct-premiss-literal', shen_constructx45premissx45literal, 2)

@tail_recursion
def shen_constructx45context(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_constructx45context, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1784_624 = FUN_ARGS[0]
    KL_ARG_V1785_625 = FUN_ARGS[1]
    global symdic
    return (symdic.symdic_Context_1957 if (shen_eq(nil, KL_ARG_V1785_625) if shen_eq(True, KL_ARG_V1784_624) else False) else (symdic.symdic_ContextOut_1957 if (shen_eq(nil, KL_ARG_V1785_625) if shen_eq(False, KL_ARG_V1784_624) else False) else (Cons(symdic.symdic_kl_cons, Cons(tco_apply(shen_recursive_cons_form, [car(KL_ARG_V1785_625)]), Cons(tco_apply(shen_constructx45context, [KL_ARG_V1784_624, cdr(KL_ARG_V1785_625)]), nil))) if shen_consp(KL_ARG_V1785_625) else (tail_call(shen_sysx45error, [symdic.symdic_shen_constructx45context]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.construct-context', shen_constructx45context, 2)

@tail_recursion
def shen_recursive_cons_form(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_recursive_cons_form, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1786_626 = FUN_ARGS[0]
    global symdic
    return (Cons(symdic.symdic_kl_cons, Cons(tco_apply(shen_recursive_cons_form, [car(KL_ARG_V1786_626)]), Cons(tco_apply(shen_recursive_cons_form, [cdr(KL_ARG_V1786_626)]), nil))) if shen_consp(KL_ARG_V1786_626) else (KL_ARG_V1786_626 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.recursive_cons_form', shen_recursive_cons_form, 1)

@tail_recursion
def kl_preclude(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_preclude, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1787_627 = FUN_ARGS[0]
    global symdic
    return tail_call(shen_precludex45h, [tco_apply(kl_map, [symdic.symdic_shen_internx45type, KL_ARG_V1787_627])])
shen_add_fun('preclude', kl_preclude, 1)

@tail_recursion
def shen_precludex45h(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_precludex45h, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1788_628 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_FilterDatatypes_629 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_FilterDatatypes_629', shen_set(symdic.symdic_shen_x42datatypesx42, tco_apply(kl_difference, [shen_get(symdic.symdic_shen_x42datatypesx42), KL_ARG_V1788_628]))), shen_get(symdic.symdic_shen_x42datatypesx42)][(-1)]
shen_add_fun('shen.preclude-h', shen_precludex45h, 1)

@tail_recursion
def kl_include(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_include, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1789_630 = FUN_ARGS[0]
    global symdic
    return tail_call(shen_includex45h, [tco_apply(kl_map, [symdic.symdic_shen_internx45type, KL_ARG_V1789_630])])
shen_add_fun('include', kl_include, 1)

@tail_recursion
def shen_includex45h(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_includex45h, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1790_631 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_ValidTypes_632 = None
        KL_LOC_NewDatatypes_633 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_ValidTypes_632', tco_apply(kl_intersection, [KL_ARG_V1790_631, shen_get(symdic.symdic_shen_x42alldatatypesx42)])), [setattr(KL_CTX, 'KL_LOC_NewDatatypes_633', shen_set(symdic.symdic_shen_x42datatypesx42, tco_apply(kl_union, [KL_CTX.KL_LOC_ValidTypes_632, shen_get(symdic.symdic_shen_x42datatypesx42)]))), shen_get(symdic.symdic_shen_x42datatypesx42)][(-1)]][(-1)]
shen_add_fun('shen.include-h', shen_includex45h, 1)

@tail_recursion
def kl_precludex45allx45but(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_precludex45allx45but, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1791_634 = FUN_ARGS[0]
    global symdic
    return tail_call(shen_precludex45h, [tco_apply(kl_difference, [shen_get(symdic.symdic_shen_x42alldatatypesx42), tco_apply(kl_map, [symdic.symdic_shen_internx45type, KL_ARG_V1791_634])])])
shen_add_fun('preclude-all-but', kl_precludex45allx45but, 1)

@tail_recursion
def kl_includex45allx45but(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_includex45allx45but, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1792_635 = FUN_ARGS[0]
    global symdic
    return tail_call(shen_includex45h, [tco_apply(kl_difference, [shen_get(symdic.symdic_shen_x42alldatatypesx42), tco_apply(kl_map, [symdic.symdic_shen_internx45type, KL_ARG_V1792_635])])])
shen_add_fun('include-all-but', kl_includex45allx45but, 1)

@tail_recursion
def shen_synonymsx45help(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_synonymsx45help, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1797_636 = FUN_ARGS[0]
    global symdic
    return (symdic.symdic_kl_synonyms if shen_eq(nil, KL_ARG_V1797_636) else ([tco_apply(shen_pushnew, [Cons(car(KL_ARG_V1797_636), tco_apply(shen_curryx45type, [car(cdr(KL_ARG_V1797_636))])), symdic.symdic_shen_x42synonymsx42]), tail_call(shen_synonymsx45help, [cdr(cdr(KL_ARG_V1797_636))])][(-1)] if (shen_consp(cdr(KL_ARG_V1797_636)) if shen_consp(KL_ARG_V1797_636) else False) else (shen_simple_error(('odd number of synonyms\r\n' + '')) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.synonyms-help', shen_synonymsx45help, 1)

@tail_recursion
def shen_pushnew(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_pushnew, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1798_637 = FUN_ARGS[0]
    KL_ARG_V1799_638 = FUN_ARGS[1]
    global symdic
    return (shen_get(KL_ARG_V1799_638) if tco_apply(kl_elementx63, [KL_ARG_V1798_637, shen_get(KL_ARG_V1799_638)]) else shen_set(KL_ARG_V1799_638, Cons(KL_ARG_V1798_637, shen_get(KL_ARG_V1799_638))))
shen_add_fun('shen.pushnew', shen_pushnew, 2)


#============================== yacc.kl==============================



@tail_recursion
def shen_yacc(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_yacc, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2150_639 = FUN_ARGS[0]
    global symdic
    return (tail_call(shen_yacc, [Cons(symdic.symdic_kl_defcc, Cons(car(cdr(KL_ARG_V2150_639)), cdr(cdr(cdr(cdr(cdr(cdr(cdr(KL_ARG_V2150_639)))))))))]) if ((((((((((shen_eq(symdic.symdic_kl_x125, car(cdr(cdr(cdr(cdr(cdr(cdr(KL_ARG_V2150_639)))))))) if shen_consp(cdr(cdr(cdr(cdr(cdr(cdr(KL_ARG_V2150_639))))))) else False) if shen_consp(cdr(cdr(cdr(cdr(cdr(KL_ARG_V2150_639)))))) else False) if shen_eq(symdic.symdic_kl_x61x61x62, car(cdr(cdr(cdr(cdr(KL_ARG_V2150_639)))))) else False) if shen_consp(cdr(cdr(cdr(cdr(KL_ARG_V2150_639))))) else False) if shen_consp(cdr(cdr(cdr(KL_ARG_V2150_639)))) else False) if shen_eq(symdic.symdic_kl_x123, car(cdr(cdr(KL_ARG_V2150_639)))) else False) if shen_consp(cdr(cdr(KL_ARG_V2150_639))) else False) if shen_consp(cdr(KL_ARG_V2150_639)) else False) if shen_eq(symdic.symdic_kl_defcc, car(KL_ARG_V2150_639)) else False) if shen_consp(KL_ARG_V2150_639) else False) else (tail_call(shen_yaccx45x62shen, [car(cdr(KL_ARG_V2150_639)), cdr(cdr(KL_ARG_V2150_639))]) if ((shen_consp(cdr(KL_ARG_V2150_639)) if shen_eq(symdic.symdic_kl_defcc, car(KL_ARG_V2150_639)) else False) if shen_consp(KL_ARG_V2150_639) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_yacc]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.yacc', shen_yacc, 1)

@tail_recursion
def shen_yaccx45x62shen(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_yaccx45x62shen, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2151_640 = FUN_ARGS[0]
    KL_ARG_V2152_641 = FUN_ARGS[1]
    global symdic
    return Cons(symdic.symdic_kl_define, Cons(KL_ARG_V2151_640, tco_apply(shen_yacc_cases, [tco_apply(kl_map, [symdic.symdic_shen_cc_body, tco_apply(shen_split_cc_rules, [KL_ARG_V2152_641, nil])])])))
shen_add_fun('shen.yacc->shen', shen_yaccx45x62shen, 2)

@tail_recursion
def shen_yacc_cases(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_yacc_cases, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2153_642 = FUN_ARGS[0]
    global symdic
    return tail_call(kl_append, [tco_apply(kl_mapcan, [(lambda KL_ARG_Case_643: Cons(symdic.symdic_Stream, Cons(symdic.symdic_kl_x60x45, Cons(KL_ARG_Case_643, nil)))), KL_ARG_V2153_642]), Cons(symdic.symdic_kl__, Cons(symdic.symdic_kl_x45x62, Cons(Cons(symdic.symdic_kl_fail, nil), nil)))])
shen_add_fun('shen.yacc_cases', shen_yacc_cases, 1)

@tail_recursion
def shen_first_n(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_first_n, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2158_644 = FUN_ARGS[0]
    KL_ARG_V2159_645 = FUN_ARGS[1]
    global symdic
    return (nil if shen_eq(0, KL_ARG_V2158_644) else (nil if shen_eq(nil, KL_ARG_V2159_645) else (Cons(car(KL_ARG_V2159_645), tco_apply(shen_first_n, [(KL_ARG_V2158_644 - 1), cdr(KL_ARG_V2159_645)])) if shen_consp(KL_ARG_V2159_645) else (tail_call(shen_sysx45error, [symdic.symdic_shen_first_n]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.first_n', shen_first_n, 2)

@tail_recursion
def shen_split_cc_rules(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_split_cc_rules, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2160_646 = FUN_ARGS[0]
    KL_ARG_V2161_647 = FUN_ARGS[1]
    global symdic
    return (nil if (shen_eq(nil, KL_ARG_V2161_647) if shen_eq(nil, KL_ARG_V2160_646) else False) else (Cons(tco_apply(shen_split_cc_rule, [tco_apply(kl_reverse, [KL_ARG_V2161_647]), nil]), nil) if shen_eq(nil, KL_ARG_V2160_646) else (Cons(tco_apply(shen_split_cc_rule, [tco_apply(kl_reverse, [KL_ARG_V2161_647]), nil]), tco_apply(shen_split_cc_rules, [cdr(KL_ARG_V2160_646), nil])) if (shen_eq(symdic.symdic_kl_x59, car(KL_ARG_V2160_646)) if shen_consp(KL_ARG_V2160_646) else False) else (tail_call(shen_split_cc_rules, [cdr(KL_ARG_V2160_646), Cons(car(KL_ARG_V2160_646), KL_ARG_V2161_647)]) if shen_consp(KL_ARG_V2160_646) else (tail_call(shen_sysx45error, [symdic.symdic_shen_split_cc_rules]) if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.split_cc_rules', shen_split_cc_rules, 2)

@tail_recursion
def shen_split_cc_rule(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_split_cc_rule, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2162_648 = FUN_ARGS[0]
    KL_ARG_V2163_649 = FUN_ARGS[1]
    global symdic
    return (Cons(tco_apply(kl_reverse, [KL_ARG_V2163_649]), cdr(KL_ARG_V2162_648)) if (((shen_eq(nil, cdr(cdr(KL_ARG_V2162_648))) if shen_consp(cdr(KL_ARG_V2162_648)) else False) if shen_eq(symdic.symdic_kl_x58x61, car(KL_ARG_V2162_648)) else False) if shen_consp(KL_ARG_V2162_648) else False) else (Cons(tco_apply(kl_reverse, [KL_ARG_V2163_649]), Cons(Cons(symdic.symdic_kl_where, Cons(car(cdr(cdr(cdr(KL_ARG_V2162_648)))), Cons(car(cdr(KL_ARG_V2162_648)), nil))), nil)) if ((((((shen_eq(nil, cdr(cdr(cdr(cdr(KL_ARG_V2162_648))))) if shen_consp(cdr(cdr(cdr(KL_ARG_V2162_648)))) else False) if shen_eq(symdic.symdic_kl_where, car(cdr(cdr(KL_ARG_V2162_648)))) else False) if shen_consp(cdr(cdr(KL_ARG_V2162_648))) else False) if shen_consp(cdr(KL_ARG_V2162_648)) else False) if shen_eq(symdic.symdic_kl_x58x61, car(KL_ARG_V2162_648)) else False) if shen_consp(KL_ARG_V2162_648) else False) else ([tco_apply(shen_prhush, ['warning: ', tco_apply(kl_stoutput, [])]), [tco_apply(kl_map, [(lambda KL_ARG_X_650: tail_call(shen_prhush, [tco_apply(shen_app, [KL_ARG_X_650, ' ', symdic.symdic_shen_a]), tco_apply(kl_stoutput, [])])), tco_apply(kl_reverse, [KL_ARG_V2163_649])]), [tco_apply(shen_prhush, ['has no semantics.\r\n', tco_apply(kl_stoutput, [])]), tail_call(shen_split_cc_rule, [Cons(symdic.symdic_kl_x58x61, Cons(tco_apply(shen_default_semantics, [tco_apply(kl_reverse, [KL_ARG_V2163_649])]), nil)), KL_ARG_V2163_649])][(-1)]][(-1)]][(-1)] if shen_eq(nil, KL_ARG_V2162_648) else (tail_call(shen_split_cc_rule, [cdr(KL_ARG_V2162_648), Cons(car(KL_ARG_V2162_648), KL_ARG_V2163_649)]) if shen_consp(KL_ARG_V2162_648) else (tail_call(shen_sysx45error, [symdic.symdic_shen_split_cc_rule]) if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.split_cc_rule', shen_split_cc_rule, 2)

@tail_recursion
def shen_default_semantics(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_default_semantics, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2164_651 = FUN_ARGS[0]
    global symdic
    return (nil if shen_eq(nil, KL_ARG_V2164_651) else (Cons(symdic.symdic_kl_append, Cons(car(KL_ARG_V2164_651), Cons(tco_apply(shen_default_semantics, [cdr(KL_ARG_V2164_651)]), nil))) if (tco_apply(shen_grammar_symbolx63, [car(KL_ARG_V2164_651)]) if shen_consp(KL_ARG_V2164_651) else False) else (Cons(symdic.symdic_kl_cons, Cons(car(KL_ARG_V2164_651), Cons(tco_apply(shen_default_semantics, [cdr(KL_ARG_V2164_651)]), nil))) if shen_consp(KL_ARG_V2164_651) else (tail_call(shen_sysx45error, [symdic.symdic_shen_default_semantics]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.default_semantics', shen_default_semantics, 1)

@tail_recursion
def shen_cc_body(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_cc_body, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2165_652 = FUN_ARGS[0]
    global symdic
    return (tail_call(shen_syntax, [car(KL_ARG_V2165_652), symdic.symdic_Stream, car(cdr(KL_ARG_V2165_652))]) if ((shen_eq(nil, cdr(cdr(KL_ARG_V2165_652))) if shen_consp(cdr(KL_ARG_V2165_652)) else False) if shen_consp(KL_ARG_V2165_652) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_cc_body]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.cc_body', shen_cc_body, 1)

@tail_recursion
def shen_syntax(*FUN_ARGS):
    FUN_ARITY = 3
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_syntax, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2166_653 = FUN_ARGS[0]
    KL_ARG_V2167_654 = FUN_ARGS[1]
    KL_ARG_V2168_655 = FUN_ARGS[2]
    global symdic
    return (Cons(symdic.symdic_kl_if, Cons(tco_apply(shen_semantics, [car(cdr(KL_ARG_V2168_655))]), Cons(Cons(symdic.symdic_shen_pair, Cons(Cons(symdic.symdic_kl_hd, Cons(KL_ARG_V2167_654, nil)), Cons(tco_apply(shen_semantics, [car(cdr(cdr(KL_ARG_V2168_655)))]), nil))), Cons(Cons(symdic.symdic_kl_fail, nil), nil)))) if (((((shen_eq(nil, cdr(cdr(cdr(KL_ARG_V2168_655)))) if shen_consp(cdr(cdr(KL_ARG_V2168_655))) else False) if shen_consp(cdr(KL_ARG_V2168_655)) else False) if shen_eq(symdic.symdic_kl_where, car(KL_ARG_V2168_655)) else False) if shen_consp(KL_ARG_V2168_655) else False) if shen_eq(nil, KL_ARG_V2166_653) else False) else (Cons(symdic.symdic_shen_pair, Cons(Cons(symdic.symdic_kl_hd, Cons(KL_ARG_V2167_654, nil)), Cons(tco_apply(shen_semantics, [KL_ARG_V2168_655]), nil))) if shen_eq(nil, KL_ARG_V2166_653) else ((tail_call(shen_recursive_descent, [KL_ARG_V2166_653, KL_ARG_V2167_654, KL_ARG_V2168_655]) if tco_apply(shen_grammar_symbolx63, [car(KL_ARG_V2166_653)]) else (tail_call(shen_variablex45match, [KL_ARG_V2166_653, KL_ARG_V2167_654, KL_ARG_V2168_655]) if tco_apply(kl_variablex63, [car(KL_ARG_V2166_653)]) else (tail_call(shen_check_stream, [KL_ARG_V2166_653, KL_ARG_V2167_654, KL_ARG_V2168_655]) if tco_apply(shen_terminalx63, [car(KL_ARG_V2166_653)]) else (tail_call(shen_jump_stream, [KL_ARG_V2166_653, KL_ARG_V2167_654, KL_ARG_V2168_655]) if tco_apply(shen_jump_streamx63, [car(KL_ARG_V2166_653)]) else (tail_call(shen_list_stream, [tco_apply(shen_decons, [car(KL_ARG_V2166_653)]), cdr(KL_ARG_V2166_653), KL_ARG_V2167_654, KL_ARG_V2168_655]) if tco_apply(shen_list_streamx63, [car(KL_ARG_V2166_653)]) else shen_simple_error(tco_apply(shen_app, [car(KL_ARG_V2166_653), ' is not legal syntax\r\n', symdic.symdic_shen_a]))))))) if shen_consp(KL_ARG_V2166_653) else (tail_call(shen_sysx45error, [symdic.symdic_shen_syntax]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.syntax', shen_syntax, 3)

@tail_recursion
def shen_list_streamx63(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_list_streamx63, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2177_656 = FUN_ARGS[0]
    global symdic
    return (True if shen_consp(KL_ARG_V2177_656) else (False if True else shen_simple_error('condition failure')))
shen_add_fun('shen.list_stream?', shen_list_streamx63, 1)

@tail_recursion
def shen_decons(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_decons, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2178_657 = FUN_ARGS[0]
    global symdic
    return (Cons(car(cdr(KL_ARG_V2178_657)), tco_apply(shen_decons, [car(cdr(cdr(KL_ARG_V2178_657)))])) if ((((shen_eq(nil, cdr(cdr(cdr(KL_ARG_V2178_657)))) if shen_consp(cdr(cdr(KL_ARG_V2178_657))) else False) if shen_consp(cdr(KL_ARG_V2178_657)) else False) if shen_eq(symdic.symdic_kl_cons, car(KL_ARG_V2178_657)) else False) if shen_consp(KL_ARG_V2178_657) else False) else (KL_ARG_V2178_657 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.decons', shen_decons, 1)

@tail_recursion
def shen_list_stream(*FUN_ARGS):
    FUN_ARITY = 4
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_list_stream, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2179_658 = FUN_ARGS[0]
    KL_ARG_V2180_659 = FUN_ARGS[1]
    KL_ARG_V2181_660 = FUN_ARGS[2]
    KL_ARG_V2182_661 = FUN_ARGS[3]

    class KL_Context:
        KL_LOC_Test_662 = None
        KL_LOC_Action_663 = None
        KL_LOC_Else_664 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Test_662', Cons(symdic.symdic_kl_and, Cons(Cons(symdic.symdic_kl_consx63, Cons(Cons(symdic.symdic_kl_hd, Cons(KL_ARG_V2181_660, nil)), nil)), Cons(Cons(symdic.symdic_kl_consx63, Cons(Cons(symdic.symdic_kl_hd, Cons(Cons(symdic.symdic_kl_hd, Cons(KL_ARG_V2181_660, nil)), nil)), nil)), nil)))), [setattr(KL_CTX, 'KL_LOC_Action_663', Cons(symdic.symdic_shen_sndx45orx45fail, Cons(tco_apply(shen_syntax, [KL_ARG_V2179_658, Cons(symdic.symdic_shen_pair, Cons(Cons(symdic.symdic_kl_hd, Cons(Cons(symdic.symdic_kl_hd, Cons(KL_ARG_V2181_660, nil)), nil)), Cons(Cons(symdic.symdic_shen_hdtl, Cons(KL_ARG_V2181_660, nil)), nil))), Cons(symdic.symdic_shen_leavex33, Cons(tco_apply(shen_syntax, [KL_ARG_V2180_659, Cons(symdic.symdic_shen_pair, Cons(Cons(symdic.symdic_kl_tl, Cons(Cons(symdic.symdic_kl_hd, Cons(KL_ARG_V2181_660, nil)), nil)), Cons(Cons(symdic.symdic_shen_hdtl, Cons(KL_ARG_V2181_660, nil)), nil))), KL_ARG_V2182_661]), nil))]), nil))), [setattr(KL_CTX, 'KL_LOC_Else_664', Cons(symdic.symdic_kl_fail, nil)), Cons(symdic.symdic_kl_if, Cons(KL_CTX.KL_LOC_Test_662, Cons(KL_CTX.KL_LOC_Action_663, Cons(KL_CTX.KL_LOC_Else_664, nil))))][(-1)]][(-1)]][(-1)]
shen_add_fun('shen.list_stream', shen_list_stream, 4)

@tail_recursion
def shen_sndx45orx45fail(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_sndx45orx45fail, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2189_665 = FUN_ARGS[0]
    global symdic
    return (car(cdr(KL_ARG_V2189_665)) if ((shen_eq(nil, cdr(cdr(KL_ARG_V2189_665))) if shen_consp(cdr(KL_ARG_V2189_665)) else False) if shen_consp(KL_ARG_V2189_665) else False) else (tail_call(kl_fail, []) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.snd-or-fail', shen_sndx45orx45fail, 1)

@tail_recursion
def shen_grammar_symbolx63(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_grammar_symbolx63, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2190_666 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Cs_667 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_Cs_667', tco_apply(shen_stripx45pathname, [tco_apply(kl_explode, [KL_ARG_V2190_666])])), (shen_eq(car(tco_apply(kl_reverse, [KL_CTX.KL_LOC_Cs_667])), '>') if shen_eq(car(KL_CTX.KL_LOC_Cs_667), '<') else False)][(-1)] if tco_apply(kl_symbolx63, [KL_ARG_V2190_666]) else False)
shen_add_fun('shen.grammar_symbol?', shen_grammar_symbolx63, 1)

@tail_recursion
def shen_stripx45pathname(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_stripx45pathname, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2195_668 = FUN_ARGS[0]
    global symdic
    return (KL_ARG_V2195_668 if (not tco_apply(kl_elementx63, ['.', KL_ARG_V2195_668])) else (tail_call(shen_stripx45pathname, [cdr(KL_ARG_V2195_668)]) if shen_consp(KL_ARG_V2195_668) else (tail_call(shen_sysx45error, [symdic.symdic_shen_stripx45pathname]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.strip-pathname', shen_stripx45pathname, 1)

@tail_recursion
def shen_recursive_descent(*FUN_ARGS):
    FUN_ARITY = 3
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_recursive_descent, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2196_669 = FUN_ARGS[0]
    KL_ARG_V2197_670 = FUN_ARGS[1]
    KL_ARG_V2198_671 = FUN_ARGS[2]

    class KL_Context:
        KL_LOC_Test_672 = None
        KL_LOC_Action_673 = None
        KL_LOC_Else_674 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_Test_672', Cons(car(KL_ARG_V2196_669), Cons(KL_ARG_V2197_670, nil))), [setattr(KL_CTX, 'KL_LOC_Action_673', tco_apply(shen_syntax, [cdr(KL_ARG_V2196_669), tco_apply(kl_concat, [symdic.symdic_Parse_, car(KL_ARG_V2196_669)]), KL_ARG_V2198_671])), [setattr(KL_CTX, 'KL_LOC_Else_674', Cons(symdic.symdic_kl_fail, nil)), Cons(symdic.symdic_kl_let, Cons(tco_apply(kl_concat, [symdic.symdic_Parse_, car(KL_ARG_V2196_669)]), Cons(KL_CTX.KL_LOC_Test_672, Cons(Cons(symdic.symdic_kl_if, Cons(Cons(symdic.symdic_kl_not, Cons(Cons(symdic.symdic_kl_x61, Cons(Cons(symdic.symdic_kl_fail, nil), Cons(tco_apply(kl_concat, [symdic.symdic_Parse_, car(KL_ARG_V2196_669)]), nil))), nil)), Cons(KL_CTX.KL_LOC_Action_673, Cons(KL_CTX.KL_LOC_Else_674, nil)))), nil))))][(-1)]][(-1)]][(-1)] if shen_consp(KL_ARG_V2196_669) else (tail_call(shen_sysx45error, [symdic.symdic_shen_recursive_descent]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.recursive_descent', shen_recursive_descent, 3)

@tail_recursion
def shen_variablex45match(*FUN_ARGS):
    FUN_ARITY = 3
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_variablex45match, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2199_675 = FUN_ARGS[0]
    KL_ARG_V2200_676 = FUN_ARGS[1]
    KL_ARG_V2201_677 = FUN_ARGS[2]

    class KL_Context:
        KL_LOC_Test_678 = None
        KL_LOC_Action_679 = None
        KL_LOC_Else_680 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_Test_678', Cons(symdic.symdic_kl_consx63, Cons(Cons(symdic.symdic_kl_hd, Cons(KL_ARG_V2200_676, nil)), nil))), [setattr(KL_CTX, 'KL_LOC_Action_679', Cons(symdic.symdic_kl_let, Cons(tco_apply(kl_concat, [symdic.symdic_Parse_, car(KL_ARG_V2199_675)]), Cons(Cons(symdic.symdic_kl_hd, Cons(Cons(symdic.symdic_kl_hd, Cons(KL_ARG_V2200_676, nil)), nil)), Cons(tco_apply(shen_syntax, [cdr(KL_ARG_V2199_675), Cons(symdic.symdic_shen_pair, Cons(Cons(symdic.symdic_kl_tl, Cons(Cons(symdic.symdic_kl_hd, Cons(KL_ARG_V2200_676, nil)), nil)), Cons(Cons(symdic.symdic_shen_hdtl, Cons(KL_ARG_V2200_676, nil)), nil))), KL_ARG_V2201_677]), nil))))), [setattr(KL_CTX, 'KL_LOC_Else_680', Cons(symdic.symdic_kl_fail, nil)), Cons(symdic.symdic_kl_if, Cons(KL_CTX.KL_LOC_Test_678, Cons(KL_CTX.KL_LOC_Action_679, Cons(KL_CTX.KL_LOC_Else_680, nil))))][(-1)]][(-1)]][(-1)] if shen_consp(KL_ARG_V2199_675) else (tail_call(shen_sysx45error, [symdic.symdic_shen_variablex45match]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.variable-match', shen_variablex45match, 3)

@tail_recursion
def shen_terminalx63(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_terminalx63, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2210_681 = FUN_ARGS[0]
    global symdic
    return (False if shen_consp(KL_ARG_V2210_681) else (False if tco_apply(kl_variablex63, [KL_ARG_V2210_681]) else (True if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.terminal?', shen_terminalx63, 1)

@tail_recursion
def shen_jump_streamx63(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_jump_streamx63, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2215_682 = FUN_ARGS[0]
    global symdic
    return (True if shen_eq(KL_ARG_V2215_682, symdic.symdic_kl__) else (False if True else shen_simple_error('condition failure')))
shen_add_fun('shen.jump_stream?', shen_jump_streamx63, 1)

@tail_recursion
def shen_check_stream(*FUN_ARGS):
    FUN_ARITY = 3
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_check_stream, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2216_683 = FUN_ARGS[0]
    KL_ARG_V2217_684 = FUN_ARGS[1]
    KL_ARG_V2218_685 = FUN_ARGS[2]

    class KL_Context:
        KL_LOC_Test_686 = None
        KL_LOC_Action_687 = None
        KL_LOC_Else_688 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_Test_686', Cons(symdic.symdic_kl_and, Cons(Cons(symdic.symdic_kl_consx63, Cons(Cons(symdic.symdic_kl_hd, Cons(KL_ARG_V2217_684, nil)), nil)), Cons(Cons(symdic.symdic_kl_x61, Cons(car(KL_ARG_V2216_683), Cons(Cons(symdic.symdic_kl_hd, Cons(Cons(symdic.symdic_kl_hd, Cons(KL_ARG_V2217_684, nil)), nil)), nil))), nil)))), [setattr(KL_CTX, 'KL_LOC_Action_687', tco_apply(shen_syntax, [cdr(KL_ARG_V2216_683), Cons(symdic.symdic_shen_pair, Cons(Cons(symdic.symdic_kl_tl, Cons(Cons(symdic.symdic_kl_hd, Cons(KL_ARG_V2217_684, nil)), nil)), Cons(Cons(symdic.symdic_shen_hdtl, Cons(KL_ARG_V2217_684, nil)), nil))), KL_ARG_V2218_685])), [setattr(KL_CTX, 'KL_LOC_Else_688', Cons(symdic.symdic_kl_fail, nil)), Cons(symdic.symdic_kl_if, Cons(KL_CTX.KL_LOC_Test_686, Cons(KL_CTX.KL_LOC_Action_687, Cons(KL_CTX.KL_LOC_Else_688, nil))))][(-1)]][(-1)]][(-1)] if shen_consp(KL_ARG_V2216_683) else (tail_call(shen_sysx45error, [symdic.symdic_shen_check_stream]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.check_stream', shen_check_stream, 3)

@tail_recursion
def shen_jump_stream(*FUN_ARGS):
    FUN_ARITY = 3
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_jump_stream, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2219_689 = FUN_ARGS[0]
    KL_ARG_V2220_690 = FUN_ARGS[1]
    KL_ARG_V2221_691 = FUN_ARGS[2]

    class KL_Context:
        KL_LOC_Test_692 = None
        KL_LOC_Action_693 = None
        KL_LOC_Else_694 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_Test_692', Cons(symdic.symdic_kl_consx63, Cons(Cons(symdic.symdic_kl_hd, Cons(KL_ARG_V2220_690, nil)), nil))), [setattr(KL_CTX, 'KL_LOC_Action_693', tco_apply(shen_syntax, [cdr(KL_ARG_V2219_689), Cons(symdic.symdic_shen_pair, Cons(Cons(symdic.symdic_kl_tl, Cons(Cons(symdic.symdic_kl_hd, Cons(KL_ARG_V2220_690, nil)), nil)), Cons(Cons(symdic.symdic_shen_hdtl, Cons(KL_ARG_V2220_690, nil)), nil))), KL_ARG_V2221_691])), [setattr(KL_CTX, 'KL_LOC_Else_694', Cons(symdic.symdic_kl_fail, nil)), Cons(symdic.symdic_kl_if, Cons(KL_CTX.KL_LOC_Test_692, Cons(KL_CTX.KL_LOC_Action_693, Cons(KL_CTX.KL_LOC_Else_694, nil))))][(-1)]][(-1)]][(-1)] if shen_consp(KL_ARG_V2219_689) else (tail_call(shen_sysx45error, [symdic.symdic_shen_jump_stream]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.jump_stream', shen_jump_stream, 3)

@tail_recursion
def shen_semantics(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_semantics, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2222_695 = FUN_ARGS[0]
    global symdic
    return (car(cdr(KL_ARG_V2222_695)) if (((shen_eq(nil, cdr(cdr(KL_ARG_V2222_695))) if shen_consp(cdr(KL_ARG_V2222_695)) else False) if shen_eq(symdic.symdic_shen_leavex33, car(KL_ARG_V2222_695)) else False) if shen_consp(KL_ARG_V2222_695) else False) else (nil if shen_eq(nil, KL_ARG_V2222_695) else (Cons(symdic.symdic_shen_hdtl, Cons(tco_apply(kl_concat, [symdic.symdic_Parse_, KL_ARG_V2222_695]), nil)) if tco_apply(shen_grammar_symbolx63, [KL_ARG_V2222_695]) else (tail_call(kl_concat, [symdic.symdic_Parse_, KL_ARG_V2222_695]) if tco_apply(kl_variablex63, [KL_ARG_V2222_695]) else (tail_call(kl_map, [symdic.symdic_shen_semantics, KL_ARG_V2222_695]) if shen_consp(KL_ARG_V2222_695) else (KL_ARG_V2222_695 if True else shen_simple_error('condition failure')))))))
shen_add_fun('shen.semantics', shen_semantics, 1)

@tail_recursion
def kl_fail(*FUN_ARGS):
    FUN_ARITY = 0
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_fail, (FUN_ARGS + lambdaargs)))
    global symdic
    return symdic.symdic_shen_failx33
shen_add_fun('fail', kl_fail, 0)

@tail_recursion
def shen_pair(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_pair, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2223_696 = FUN_ARGS[0]
    KL_ARG_V2224_697 = FUN_ARGS[1]
    global symdic
    return Cons(KL_ARG_V2223_696, Cons(KL_ARG_V2224_697, nil))
shen_add_fun('shen.pair', shen_pair, 2)

@tail_recursion
def shen_hdtl(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_hdtl, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2225_698 = FUN_ARGS[0]
    global symdic
    return car(cdr(KL_ARG_V2225_698))
shen_add_fun('shen.hdtl', shen_hdtl, 1)

@tail_recursion
def x60x33x62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(x60x33x62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2232_699 = FUN_ARGS[0]
    global symdic
    return (Cons(nil, Cons(car(KL_ARG_V2232_699), nil)) if ((shen_eq(nil, cdr(cdr(KL_ARG_V2232_699))) if shen_consp(cdr(KL_ARG_V2232_699)) else False) if shen_consp(KL_ARG_V2232_699) else False) else (tail_call(kl_fail, []) if True else shen_simple_error('condition failure')))
shen_add_fun('<!>', x60x33x62, 1)

@tail_recursion
def kl_x60ex62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_x60ex62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2237_700 = FUN_ARGS[0]
    global symdic
    return (Cons(car(KL_ARG_V2237_700), Cons(nil, nil)) if ((shen_eq(nil, cdr(cdr(KL_ARG_V2237_700))) if shen_consp(cdr(KL_ARG_V2237_700)) else False) if shen_consp(KL_ARG_V2237_700) else False) else (tail_call(shen_sysx45error, [symdic.symdic_kl_x60ex62]) if True else shen_simple_error('condition failure')))
shen_add_fun('<e>', kl_x60ex62, 1)


#============================== reader.kl==============================



@tail_recursion
def kl_lineread(*FUN_ARGS):
    FUN_ARITY = 0
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_lineread, (FUN_ARGS + lambdaargs)))
    global symdic
    return tail_call(shen_linereadx45loop, [shen_read_byte(tco_apply(kl_stinput, [])), nil])
shen_add_fun('lineread', kl_lineread, 0)

@tail_recursion
def shen_linereadx45loop(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_linereadx45loop, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1329_701 = FUN_ARGS[0]
    KL_ARG_V1330_702 = FUN_ARGS[1]

    class KL_Context:
        KL_LOC_Line_703 = None
    KL_CTX = KL_Context()
    global symdic
    return (shen_simple_error('line read aborted') if shen_eq(KL_ARG_V1329_701, tco_apply(shen_hat, [])) else ([setattr(KL_CTX, 'KL_LOC_Line_703', tco_apply(kl_compile, [symdic.symdic_shen_x60st_inputx62, KL_ARG_V1330_702, (lambda KL_ARG_E_704: symdic.symdic_shen_nextline)])), (tail_call(shen_linereadx45loop, [shen_read_byte(tco_apply(kl_stinput, [])), tco_apply(kl_append, [KL_ARG_V1330_702, Cons(KL_ARG_V1329_701, nil)])]) if (True if shen_eq(KL_CTX.KL_LOC_Line_703, symdic.symdic_shen_nextline) else tco_apply(kl_emptyx63, [KL_CTX.KL_LOC_Line_703])) else KL_CTX.KL_LOC_Line_703)][(-1)] if tco_apply(kl_elementx63, [KL_ARG_V1329_701, Cons(tco_apply(shen_newline, []), Cons(tco_apply(shen_carriagex45return, []), nil))]) else (tail_call(shen_linereadx45loop, [shen_read_byte(tco_apply(kl_stinput, [])), tco_apply(kl_append, [KL_ARG_V1330_702, Cons(KL_ARG_V1329_701, nil)])]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.lineread-loop', shen_linereadx45loop, 2)

@tail_recursion
def kl_readx45file(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_readx45file, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1331_705 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Bytelist_706 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Bytelist_706', tco_apply(kl_readx45filex45asx45bytelist, [KL_ARG_V1331_705])), tail_call(kl_compile, [symdic.symdic_shen_x60st_inputx62, KL_CTX.KL_LOC_Bytelist_706, symdic.symdic_shen_readx45error])][(-1)]
shen_add_fun('read-file', kl_readx45file, 1)

@tail_recursion
def shen_readx45error(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_readx45error, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1338_707 = FUN_ARGS[0]
    global symdic
    return (shen_simple_error(('read error here:\r\n\r\n ' + tco_apply(shen_app, [tco_apply(shen_compressx4550, [50, car(KL_ARG_V1338_707)]), '\r\n', symdic.symdic_shen_a]))) if (((shen_eq(nil, cdr(cdr(KL_ARG_V1338_707))) if shen_consp(cdr(KL_ARG_V1338_707)) else False) if shen_consp(car(KL_ARG_V1338_707)) else False) if shen_consp(KL_ARG_V1338_707) else False) else (shen_simple_error('read error\r\n') if True else shen_simple_error('condition failure')))
shen_add_fun('shen.read-error', shen_readx45error, 1)

@tail_recursion
def shen_compressx4550(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_compressx4550, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1343_708 = FUN_ARGS[0]
    KL_ARG_V1344_709 = FUN_ARGS[1]
    global symdic
    return ('' if shen_eq(nil, KL_ARG_V1344_709) else ('' if shen_eq(0, KL_ARG_V1343_708) else ((chr(car(KL_ARG_V1344_709)) + tco_apply(shen_compressx4550, [(KL_ARG_V1343_708 - 1), cdr(KL_ARG_V1344_709)])) if shen_consp(KL_ARG_V1344_709) else (tail_call(shen_sysx45error, [symdic.symdic_shen_compressx4550]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.compress-50', shen_compressx4550, 2)

@tail_recursion
def shen_x60st_inputx62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60st_inputx62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1349_710 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_711 = None
        KL_LOC_Parse_shen_x60lsbx62_712 = None
        KL_LOC_Parse_shen_x60st_input1x62_713 = None
        KL_LOC_Parse_shen_x60rsbx62_714 = None
        KL_LOC_Parse_shen_x60st_input2x62_715 = None
        KL_LOC_Result_716 = None
        KL_LOC_Parse_shen_x60lrbx62_717 = None
        KL_LOC_Parse_shen_x60st_input1x62_718 = None
        KL_LOC_Parse_shen_x60rrbx62_719 = None
        KL_LOC_Parse_shen_x60st_input2x62_720 = None
        KL_LOC_Result_721 = None
        KL_LOC_Parse_shen_x60lcurlyx62_722 = None
        KL_LOC_Parse_shen_x60st_inputx62_723 = None
        KL_LOC_Result_724 = None
        KL_LOC_Parse_shen_x60rcurlyx62_725 = None
        KL_LOC_Parse_shen_x60st_inputx62_726 = None
        KL_LOC_Result_727 = None
        KL_LOC_Parse_shen_x60barx62_728 = None
        KL_LOC_Parse_shen_x60st_inputx62_729 = None
        KL_LOC_Result_730 = None
        KL_LOC_Parse_shen_x60semicolonx62_731 = None
        KL_LOC_Parse_shen_x60st_inputx62_732 = None
        KL_LOC_Result_733 = None
        KL_LOC_Parse_shen_x60colonx62_734 = None
        KL_LOC_Parse_shen_x60equalx62_735 = None
        KL_LOC_Parse_shen_x60st_inputx62_736 = None
        KL_LOC_Result_737 = None
        KL_LOC_Parse_shen_x60colonx62_738 = None
        KL_LOC_Parse_shen_x60minusx62_739 = None
        KL_LOC_Parse_shen_x60st_inputx62_740 = None
        KL_LOC_Result_741 = None
        KL_LOC_Parse_shen_x60colonx62_742 = None
        KL_LOC_Parse_shen_x60st_inputx62_743 = None
        KL_LOC_Result_744 = None
        KL_LOC_Parse_shen_x60commax62_745 = None
        KL_LOC_Parse_shen_x60st_inputx62_746 = None
        KL_LOC_Result_747 = None
        KL_LOC_Parse_shen_x60commentx62_748 = None
        KL_LOC_Parse_shen_x60st_inputx62_749 = None
        KL_LOC_Result_750 = None
        KL_LOC_Parse_shen_x60atomx62_751 = None
        KL_LOC_Parse_shen_x60st_inputx62_752 = None
        KL_LOC_Result_753 = None
        KL_LOC_Parse_shen_x60whitespacesx62_754 = None
        KL_LOC_Parse_shen_x60st_inputx62_755 = None
        KL_LOC_Result_756 = None
        KL_LOC_Parse_x60ex62_757 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_711', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60lsbx62_712', tco_apply(shen_x60lsbx62, [KL_ARG_V1349_710])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_input1x62_713', tco_apply(shen_x60st_input1x62, [KL_CTX.KL_LOC_Parse_shen_x60lsbx62_712])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60rsbx62_714', tco_apply(shen_x60rsbx62, [KL_CTX.KL_LOC_Parse_shen_x60st_input1x62_713])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_input2x62_715', tco_apply(shen_x60st_input2x62, [KL_CTX.KL_LOC_Parse_shen_x60rsbx62_714])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60st_input2x62_715), Cons(tco_apply(kl_macroexpand, [tco_apply(shen_cons_form, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_input1x62_713])])]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_input2x62_715]))]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60st_input2x62_715)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60rsbx62_714)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60st_input1x62_713)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60lsbx62_712)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_716', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60lrbx62_717', tco_apply(shen_x60lrbx62, [KL_ARG_V1349_710])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_input1x62_718', tco_apply(shen_x60st_input1x62, [KL_CTX.KL_LOC_Parse_shen_x60lrbx62_717])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60rrbx62_719', tco_apply(shen_x60rrbx62, [KL_CTX.KL_LOC_Parse_shen_x60st_input1x62_718])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_input2x62_720', tco_apply(shen_x60st_input2x62, [KL_CTX.KL_LOC_Parse_shen_x60rrbx62_719])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60st_input2x62_720), tco_apply(shen_packagex45macro, [tco_apply(kl_macroexpand, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_input1x62_718])]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_input2x62_720])])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60st_input2x62_720)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60rrbx62_719)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60st_input1x62_718)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60lrbx62_717)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_721', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60lcurlyx62_722', tco_apply(shen_x60lcurlyx62, [KL_ARG_V1349_710])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_inputx62_723', tco_apply(shen_x60st_inputx62, [KL_CTX.KL_LOC_Parse_shen_x60lcurlyx62_722])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_723), Cons(symdic.symdic_kl_x123, tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_723]))]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_723)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60lcurlyx62_722)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_724', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60rcurlyx62_725', tco_apply(shen_x60rcurlyx62, [KL_ARG_V1349_710])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_inputx62_726', tco_apply(shen_x60st_inputx62, [KL_CTX.KL_LOC_Parse_shen_x60rcurlyx62_725])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_726), Cons(symdic.symdic_kl_x125, tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_726]))]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_726)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60rcurlyx62_725)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_727', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60barx62_728', tco_apply(shen_x60barx62, [KL_ARG_V1349_710])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_inputx62_729', tco_apply(shen_x60st_inputx62, [KL_CTX.KL_LOC_Parse_shen_x60barx62_728])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_729), Cons(symdic.symdic_kl_barx33, tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_729]))]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_729)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60barx62_728)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_730', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60semicolonx62_731', tco_apply(shen_x60semicolonx62, [KL_ARG_V1349_710])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_inputx62_732', tco_apply(shen_x60st_inputx62, [KL_CTX.KL_LOC_Parse_shen_x60semicolonx62_731])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_732), Cons(symdic.symdic_kl_x59, tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_732]))]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_732)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60semicolonx62_731)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_733', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60colonx62_734', tco_apply(shen_x60colonx62, [KL_ARG_V1349_710])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60equalx62_735', tco_apply(shen_x60equalx62, [KL_CTX.KL_LOC_Parse_shen_x60colonx62_734])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_inputx62_736', tco_apply(shen_x60st_inputx62, [KL_CTX.KL_LOC_Parse_shen_x60equalx62_735])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_736), Cons(symdic.symdic_kl_x58x61, tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_736]))]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_736)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60equalx62_735)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60colonx62_734)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_737', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60colonx62_738', tco_apply(shen_x60colonx62, [KL_ARG_V1349_710])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60minusx62_739', tco_apply(shen_x60minusx62, [KL_CTX.KL_LOC_Parse_shen_x60colonx62_738])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_inputx62_740', tco_apply(shen_x60st_inputx62, [KL_CTX.KL_LOC_Parse_shen_x60minusx62_739])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_740), Cons(symdic.symdic_kl_x58x45, tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_740]))]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_740)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60minusx62_739)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60colonx62_738)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_741', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60colonx62_742', tco_apply(shen_x60colonx62, [KL_ARG_V1349_710])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_inputx62_743', tco_apply(shen_x60st_inputx62, [KL_CTX.KL_LOC_Parse_shen_x60colonx62_742])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_743), Cons(symdic.symdic_kl_x58, tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_743]))]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_743)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60colonx62_742)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_744', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60commax62_745', tco_apply(shen_x60commax62, [KL_ARG_V1349_710])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_inputx62_746', tco_apply(shen_x60st_inputx62, [KL_CTX.KL_LOC_Parse_shen_x60commax62_745])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_746), Cons(shen_intern(','), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_746]))]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_746)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60commax62_745)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_747', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60commentx62_748', tco_apply(shen_x60commentx62, [KL_ARG_V1349_710])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_inputx62_749', tco_apply(shen_x60st_inputx62, [KL_CTX.KL_LOC_Parse_shen_x60commentx62_748])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_749), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_749])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_749)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60commentx62_748)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_750', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60atomx62_751', tco_apply(shen_x60atomx62, [KL_ARG_V1349_710])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_inputx62_752', tco_apply(shen_x60st_inputx62, [KL_CTX.KL_LOC_Parse_shen_x60atomx62_751])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_752), Cons(tco_apply(kl_macroexpand, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60atomx62_751])]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_752]))]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_752)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60atomx62_751)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_753', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60whitespacesx62_754', tco_apply(shen_x60whitespacesx62, [KL_ARG_V1349_710])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_inputx62_755', tco_apply(shen_x60st_inputx62, [KL_CTX.KL_LOC_Parse_shen_x60whitespacesx62_754])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_755), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_755])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_755)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60whitespacesx62_754)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_756', [setattr(KL_CTX, 'KL_LOC_Parse_x60ex62_757', tco_apply(kl_x60ex62, [KL_ARG_V1349_710])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_x60ex62_757), nil]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_x60ex62_757)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_756, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_756)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_753, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_753)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_750, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_750)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_747, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_747)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_744, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_744)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_741, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_741)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_737, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_737)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_733, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_733)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_730, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_730)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_727, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_727)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_724, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_724)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_721, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_721)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_716, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_716)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_711, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_711)][(-1)]
shen_add_fun('shen.<st_input>', shen_x60st_inputx62, 1)

@tail_recursion
def shen_x60lsbx62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60lsbx62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1354_758 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_759 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_759', (tco_apply(shen_pair, [car(tco_apply(shen_pair, [cdr(car(KL_ARG_V1354_758)), tco_apply(shen_hdtl, [KL_ARG_V1354_758])])), symdic.symdic_shen_skip]) if (shen_eq(91, car(car(KL_ARG_V1354_758))) if shen_consp(car(KL_ARG_V1354_758)) else False) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_759, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_759)][(-1)]
shen_add_fun('shen.<lsb>', shen_x60lsbx62, 1)

@tail_recursion
def shen_x60rsbx62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60rsbx62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1359_760 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_761 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_761', (tco_apply(shen_pair, [car(tco_apply(shen_pair, [cdr(car(KL_ARG_V1359_760)), tco_apply(shen_hdtl, [KL_ARG_V1359_760])])), symdic.symdic_shen_skip]) if (shen_eq(93, car(car(KL_ARG_V1359_760))) if shen_consp(car(KL_ARG_V1359_760)) else False) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_761, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_761)][(-1)]
shen_add_fun('shen.<rsb>', shen_x60rsbx62, 1)

@tail_recursion
def shen_x60lcurlyx62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60lcurlyx62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1364_762 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_763 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_763', (tco_apply(shen_pair, [car(tco_apply(shen_pair, [cdr(car(KL_ARG_V1364_762)), tco_apply(shen_hdtl, [KL_ARG_V1364_762])])), symdic.symdic_shen_skip]) if (shen_eq(123, car(car(KL_ARG_V1364_762))) if shen_consp(car(KL_ARG_V1364_762)) else False) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_763, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_763)][(-1)]
shen_add_fun('shen.<lcurly>', shen_x60lcurlyx62, 1)

@tail_recursion
def shen_x60rcurlyx62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60rcurlyx62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1369_764 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_765 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_765', (tco_apply(shen_pair, [car(tco_apply(shen_pair, [cdr(car(KL_ARG_V1369_764)), tco_apply(shen_hdtl, [KL_ARG_V1369_764])])), symdic.symdic_shen_skip]) if (shen_eq(125, car(car(KL_ARG_V1369_764))) if shen_consp(car(KL_ARG_V1369_764)) else False) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_765, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_765)][(-1)]
shen_add_fun('shen.<rcurly>', shen_x60rcurlyx62, 1)

@tail_recursion
def shen_x60barx62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60barx62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1374_766 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_767 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_767', (tco_apply(shen_pair, [car(tco_apply(shen_pair, [cdr(car(KL_ARG_V1374_766)), tco_apply(shen_hdtl, [KL_ARG_V1374_766])])), symdic.symdic_shen_skip]) if (shen_eq(124, car(car(KL_ARG_V1374_766))) if shen_consp(car(KL_ARG_V1374_766)) else False) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_767, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_767)][(-1)]
shen_add_fun('shen.<bar>', shen_x60barx62, 1)

@tail_recursion
def shen_x60semicolonx62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60semicolonx62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1379_768 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_769 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_769', (tco_apply(shen_pair, [car(tco_apply(shen_pair, [cdr(car(KL_ARG_V1379_768)), tco_apply(shen_hdtl, [KL_ARG_V1379_768])])), symdic.symdic_shen_skip]) if (shen_eq(59, car(car(KL_ARG_V1379_768))) if shen_consp(car(KL_ARG_V1379_768)) else False) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_769, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_769)][(-1)]
shen_add_fun('shen.<semicolon>', shen_x60semicolonx62, 1)

@tail_recursion
def shen_x60colonx62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60colonx62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1384_770 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_771 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_771', (tco_apply(shen_pair, [car(tco_apply(shen_pair, [cdr(car(KL_ARG_V1384_770)), tco_apply(shen_hdtl, [KL_ARG_V1384_770])])), symdic.symdic_shen_skip]) if (shen_eq(58, car(car(KL_ARG_V1384_770))) if shen_consp(car(KL_ARG_V1384_770)) else False) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_771, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_771)][(-1)]
shen_add_fun('shen.<colon>', shen_x60colonx62, 1)

@tail_recursion
def shen_x60commax62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60commax62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1389_772 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_773 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_773', (tco_apply(shen_pair, [car(tco_apply(shen_pair, [cdr(car(KL_ARG_V1389_772)), tco_apply(shen_hdtl, [KL_ARG_V1389_772])])), symdic.symdic_shen_skip]) if (shen_eq(44, car(car(KL_ARG_V1389_772))) if shen_consp(car(KL_ARG_V1389_772)) else False) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_773, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_773)][(-1)]
shen_add_fun('shen.<comma>', shen_x60commax62, 1)

@tail_recursion
def shen_x60equalx62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60equalx62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1394_774 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_775 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_775', (tco_apply(shen_pair, [car(tco_apply(shen_pair, [cdr(car(KL_ARG_V1394_774)), tco_apply(shen_hdtl, [KL_ARG_V1394_774])])), symdic.symdic_shen_skip]) if (shen_eq(61, car(car(KL_ARG_V1394_774))) if shen_consp(car(KL_ARG_V1394_774)) else False) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_775, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_775)][(-1)]
shen_add_fun('shen.<equal>', shen_x60equalx62, 1)

@tail_recursion
def shen_x60minusx62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60minusx62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1399_776 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_777 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_777', (tco_apply(shen_pair, [car(tco_apply(shen_pair, [cdr(car(KL_ARG_V1399_776)), tco_apply(shen_hdtl, [KL_ARG_V1399_776])])), symdic.symdic_shen_skip]) if (shen_eq(45, car(car(KL_ARG_V1399_776))) if shen_consp(car(KL_ARG_V1399_776)) else False) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_777, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_777)][(-1)]
shen_add_fun('shen.<minus>', shen_x60minusx62, 1)

@tail_recursion
def shen_x60lrbx62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60lrbx62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1404_778 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_779 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_779', (tco_apply(shen_pair, [car(tco_apply(shen_pair, [cdr(car(KL_ARG_V1404_778)), tco_apply(shen_hdtl, [KL_ARG_V1404_778])])), symdic.symdic_shen_skip]) if (shen_eq(40, car(car(KL_ARG_V1404_778))) if shen_consp(car(KL_ARG_V1404_778)) else False) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_779, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_779)][(-1)]
shen_add_fun('shen.<lrb>', shen_x60lrbx62, 1)

@tail_recursion
def shen_x60rrbx62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60rrbx62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1409_780 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_781 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_781', (tco_apply(shen_pair, [car(tco_apply(shen_pair, [cdr(car(KL_ARG_V1409_780)), tco_apply(shen_hdtl, [KL_ARG_V1409_780])])), symdic.symdic_shen_skip]) if (shen_eq(41, car(car(KL_ARG_V1409_780))) if shen_consp(car(KL_ARG_V1409_780)) else False) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_781, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_781)][(-1)]
shen_add_fun('shen.<rrb>', shen_x60rrbx62, 1)

@tail_recursion
def shen_x60atomx62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60atomx62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1414_782 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_783 = None
        KL_LOC_Parse_shen_x60strx62_784 = None
        KL_LOC_Result_785 = None
        KL_LOC_Parse_shen_x60numberx62_786 = None
        KL_LOC_Result_787 = None
        KL_LOC_Parse_shen_x60symx62_788 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_783', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60strx62_784', tco_apply(shen_x60strx62, [KL_ARG_V1414_782])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60strx62_784), tco_apply(shen_controlx45chars, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60strx62_784])])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60strx62_784)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_785', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60numberx62_786', tco_apply(shen_x60numberx62, [KL_ARG_V1414_782])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60numberx62_786), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60numberx62_786])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60numberx62_786)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_787', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60symx62_788', tco_apply(shen_x60symx62, [KL_ARG_V1414_782])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60symx62_788), (Cons(symdic.symdic_kl_vector, Cons(0, nil)) if shen_eq(tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60symx62_788]), '<>') else shen_intern(tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60symx62_788])))]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60symx62_788)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_787, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_787)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_785, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_785)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_783, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_783)][(-1)]
shen_add_fun('shen.<atom>', shen_x60atomx62, 1)

@tail_recursion
def shen_controlx45chars(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_controlx45chars, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1415_789 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_CodePoint_790 = None
        KL_LOC_AfterCodePoint_791 = None
    KL_CTX = KL_Context()
    global symdic
    return ('' if shen_eq(nil, KL_ARG_V1415_789) else ([setattr(KL_CTX, 'KL_LOC_CodePoint_790', tco_apply(shen_codex45point, [cdr(cdr(KL_ARG_V1415_789))])), [setattr(KL_CTX, 'KL_LOC_AfterCodePoint_791', tco_apply(shen_afterx45codepoint, [cdr(cdr(KL_ARG_V1415_789))])), tail_call(kl_x64s, [chr(tco_apply(shen_decimalise, [KL_CTX.KL_LOC_CodePoint_790])), tco_apply(shen_controlx45chars, [KL_CTX.KL_LOC_AfterCodePoint_791])])][(-1)]][(-1)] if (((shen_eq('#', car(cdr(KL_ARG_V1415_789))) if shen_consp(cdr(KL_ARG_V1415_789)) else False) if shen_eq('c', car(KL_ARG_V1415_789)) else False) if shen_consp(KL_ARG_V1415_789) else False) else (tail_call(kl_x64s, [car(KL_ARG_V1415_789), tco_apply(shen_controlx45chars, [cdr(KL_ARG_V1415_789)])]) if shen_consp(KL_ARG_V1415_789) else (tail_call(shen_sysx45error, [symdic.symdic_shen_controlx45chars]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.control-chars', shen_controlx45chars, 1)

@tail_recursion
def shen_codex45point(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_codex45point, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1418_792 = FUN_ARGS[0]
    global symdic
    return ('' if (shen_eq(';', car(KL_ARG_V1418_792)) if shen_consp(KL_ARG_V1418_792) else False) else (Cons(car(KL_ARG_V1418_792), tco_apply(shen_codex45point, [cdr(KL_ARG_V1418_792)])) if (tco_apply(kl_elementx63, [car(KL_ARG_V1418_792), Cons('0', Cons('1', Cons('2', Cons('3', Cons('4', Cons('5', Cons('6', Cons('7', Cons('8', Cons('9', Cons('0', nil)))))))))))]) if shen_consp(KL_ARG_V1418_792) else False) else (shen_simple_error(('code point parse error ' + tco_apply(shen_app, [KL_ARG_V1418_792, '\r\n', symdic.symdic_shen_a]))) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.code-point', shen_codex45point, 1)

@tail_recursion
def shen_afterx45codepoint(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_afterx45codepoint, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1423_793 = FUN_ARGS[0]
    global symdic
    return (nil if shen_eq(nil, KL_ARG_V1423_793) else (cdr(KL_ARG_V1423_793) if (shen_eq(';', car(KL_ARG_V1423_793)) if shen_consp(KL_ARG_V1423_793) else False) else (tail_call(shen_afterx45codepoint, [cdr(KL_ARG_V1423_793)]) if shen_consp(KL_ARG_V1423_793) else (tail_call(shen_sysx45error, [symdic.symdic_shen_afterx45codepoint]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.after-codepoint', shen_afterx45codepoint, 1)

@tail_recursion
def shen_decimalise(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_decimalise, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1424_794 = FUN_ARGS[0]
    global symdic
    return tail_call(shen_pre, [tco_apply(kl_reverse, [tco_apply(shen_digitsx45x62integers, [KL_ARG_V1424_794])]), 0])
shen_add_fun('shen.decimalise', shen_decimalise, 1)

@tail_recursion
def shen_digitsx45x62integers(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_digitsx45x62integers, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1429_795 = FUN_ARGS[0]
    global symdic
    return (Cons(0, tco_apply(shen_digitsx45x62integers, [cdr(KL_ARG_V1429_795)])) if (shen_eq('0', car(KL_ARG_V1429_795)) if shen_consp(KL_ARG_V1429_795) else False) else (Cons(1, tco_apply(shen_digitsx45x62integers, [cdr(KL_ARG_V1429_795)])) if (shen_eq('1', car(KL_ARG_V1429_795)) if shen_consp(KL_ARG_V1429_795) else False) else (Cons(2, tco_apply(shen_digitsx45x62integers, [cdr(KL_ARG_V1429_795)])) if (shen_eq('2', car(KL_ARG_V1429_795)) if shen_consp(KL_ARG_V1429_795) else False) else (Cons(3, tco_apply(shen_digitsx45x62integers, [cdr(KL_ARG_V1429_795)])) if (shen_eq('3', car(KL_ARG_V1429_795)) if shen_consp(KL_ARG_V1429_795) else False) else (Cons(4, tco_apply(shen_digitsx45x62integers, [cdr(KL_ARG_V1429_795)])) if (shen_eq('4', car(KL_ARG_V1429_795)) if shen_consp(KL_ARG_V1429_795) else False) else (Cons(5, tco_apply(shen_digitsx45x62integers, [cdr(KL_ARG_V1429_795)])) if (shen_eq('5', car(KL_ARG_V1429_795)) if shen_consp(KL_ARG_V1429_795) else False) else (Cons(6, tco_apply(shen_digitsx45x62integers, [cdr(KL_ARG_V1429_795)])) if (shen_eq('6', car(KL_ARG_V1429_795)) if shen_consp(KL_ARG_V1429_795) else False) else (Cons(7, tco_apply(shen_digitsx45x62integers, [cdr(KL_ARG_V1429_795)])) if (shen_eq('7', car(KL_ARG_V1429_795)) if shen_consp(KL_ARG_V1429_795) else False) else (Cons(8, tco_apply(shen_digitsx45x62integers, [cdr(KL_ARG_V1429_795)])) if (shen_eq('8', car(KL_ARG_V1429_795)) if shen_consp(KL_ARG_V1429_795) else False) else (Cons(9, tco_apply(shen_digitsx45x62integers, [cdr(KL_ARG_V1429_795)])) if (shen_eq('9', car(KL_ARG_V1429_795)) if shen_consp(KL_ARG_V1429_795) else False) else (nil if True else shen_simple_error('condition failure'))))))))))))
shen_add_fun('shen.digits->integers', shen_digitsx45x62integers, 1)

@tail_recursion
def shen_x60symx62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60symx62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1434_796 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_797 = None
        KL_LOC_Parse_shen_x60alphax62_798 = None
        KL_LOC_Parse_shen_x60alphanumsx62_799 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_797', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60alphax62_798', tco_apply(shen_x60alphax62, [KL_ARG_V1434_796])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60alphanumsx62_799', tco_apply(shen_x60alphanumsx62, [KL_CTX.KL_LOC_Parse_shen_x60alphax62_798])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60alphanumsx62_799), tco_apply(kl_x64s, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60alphax62_798]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60alphanumsx62_799])])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60alphanumsx62_799)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60alphax62_798)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_797, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_797)][(-1)]
shen_add_fun('shen.<sym>', shen_x60symx62, 1)

@tail_recursion
def shen_x60alphanumsx62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60alphanumsx62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1439_800 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_801 = None
        KL_LOC_Parse_shen_x60alphanumx62_802 = None
        KL_LOC_Parse_shen_x60alphanumsx62_803 = None
        KL_LOC_Result_804 = None
        KL_LOC_Parse_x60ex62_805 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_801', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60alphanumx62_802', tco_apply(shen_x60alphanumx62, [KL_ARG_V1439_800])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60alphanumsx62_803', tco_apply(shen_x60alphanumsx62, [KL_CTX.KL_LOC_Parse_shen_x60alphanumx62_802])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60alphanumsx62_803), tco_apply(kl_x64s, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60alphanumx62_802]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60alphanumsx62_803])])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60alphanumsx62_803)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60alphanumx62_802)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_804', [setattr(KL_CTX, 'KL_LOC_Parse_x60ex62_805', tco_apply(kl_x60ex62, [KL_ARG_V1439_800])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_x60ex62_805), '']) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_x60ex62_805)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_804, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_804)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_801, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_801)][(-1)]
shen_add_fun('shen.<alphanums>', shen_x60alphanumsx62, 1)

@tail_recursion
def shen_x60alphanumx62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60alphanumx62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1444_806 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_807 = None
        KL_LOC_Parse_shen_x60alphax62_808 = None
        KL_LOC_Result_809 = None
        KL_LOC_Parse_shen_x60numx62_810 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_807', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60alphax62_808', tco_apply(shen_x60alphax62, [KL_ARG_V1444_806])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60alphax62_808), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60alphax62_808])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60alphax62_808)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_809', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60numx62_810', tco_apply(shen_x60numx62, [KL_ARG_V1444_806])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60numx62_810), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60numx62_810])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60numx62_810)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_809, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_809)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_807, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_807)][(-1)]
shen_add_fun('shen.<alphanum>', shen_x60alphanumx62, 1)

@tail_recursion
def shen_x60numx62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60numx62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1449_811 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_812 = None
        KL_LOC_Parse_Byte_813 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_812', ([setattr(KL_CTX, 'KL_LOC_Parse_Byte_813', car(car(KL_ARG_V1449_811))), (tco_apply(shen_pair, [car(tco_apply(shen_pair, [cdr(car(KL_ARG_V1449_811)), tco_apply(shen_hdtl, [KL_ARG_V1449_811])])), chr(KL_CTX.KL_LOC_Parse_Byte_813)]) if tco_apply(shen_numbytex63, [KL_CTX.KL_LOC_Parse_Byte_813]) else tco_apply(kl_fail, []))][(-1)] if shen_consp(car(KL_ARG_V1449_811)) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_812, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_812)][(-1)]
shen_add_fun('shen.<num>', shen_x60numx62, 1)

@tail_recursion
def shen_numbytex63(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_numbytex63, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1454_814 = FUN_ARGS[0]
    global symdic
    return (True if shen_eq(48, KL_ARG_V1454_814) else (True if shen_eq(49, KL_ARG_V1454_814) else (True if shen_eq(50, KL_ARG_V1454_814) else (True if shen_eq(51, KL_ARG_V1454_814) else (True if shen_eq(52, KL_ARG_V1454_814) else (True if shen_eq(53, KL_ARG_V1454_814) else (True if shen_eq(54, KL_ARG_V1454_814) else (True if shen_eq(55, KL_ARG_V1454_814) else (True if shen_eq(56, KL_ARG_V1454_814) else (True if shen_eq(57, KL_ARG_V1454_814) else (False if True else shen_simple_error('condition failure'))))))))))))
shen_add_fun('shen.numbyte?', shen_numbytex63, 1)

@tail_recursion
def shen_x60alphax62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60alphax62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1459_815 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_816 = None
        KL_LOC_Parse_Byte_817 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_816', ([setattr(KL_CTX, 'KL_LOC_Parse_Byte_817', car(car(KL_ARG_V1459_815))), (tco_apply(shen_pair, [car(tco_apply(shen_pair, [cdr(car(KL_ARG_V1459_815)), tco_apply(shen_hdtl, [KL_ARG_V1459_815])])), chr(KL_CTX.KL_LOC_Parse_Byte_817)]) if tco_apply(shen_symbolx45codex63, [KL_CTX.KL_LOC_Parse_Byte_817]) else tco_apply(kl_fail, []))][(-1)] if shen_consp(car(KL_ARG_V1459_815)) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_816, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_816)][(-1)]
shen_add_fun('shen.<alpha>', shen_x60alphax62, 1)

@tail_recursion
def shen_symbolx45codex63(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_symbolx45codex63, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1460_818 = FUN_ARGS[0]
    global symdic
    return (True if shen_eq(KL_ARG_V1460_818, 126) else (True if ((KL_ARG_V1460_818 < 123) if (KL_ARG_V1460_818 > 94) else False) else (True if ((KL_ARG_V1460_818 < 91) if (KL_ARG_V1460_818 > 59) else False) else (True if (((not shen_eq(KL_ARG_V1460_818, 44)) if (KL_ARG_V1460_818 < 58) else False) if (KL_ARG_V1460_818 > 41) else False) else (True if ((KL_ARG_V1460_818 < 40) if (KL_ARG_V1460_818 > 34) else False) else shen_eq(KL_ARG_V1460_818, 33))))))
shen_add_fun('shen.symbol-code?', shen_symbolx45codex63, 1)

@tail_recursion
def shen_x60strx62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60strx62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1465_819 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_820 = None
        KL_LOC_Parse_shen_x60dbqx62_821 = None
        KL_LOC_Parse_shen_x60strcontentsx62_822 = None
        KL_LOC_Parse_shen_x60dbqx62_823 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_820', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60dbqx62_821', tco_apply(shen_x60dbqx62, [KL_ARG_V1465_819])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60strcontentsx62_822', tco_apply(shen_x60strcontentsx62, [KL_CTX.KL_LOC_Parse_shen_x60dbqx62_821])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60dbqx62_823', tco_apply(shen_x60dbqx62, [KL_CTX.KL_LOC_Parse_shen_x60strcontentsx62_822])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60dbqx62_823), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60strcontentsx62_822])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60dbqx62_823)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60strcontentsx62_822)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60dbqx62_821)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_820, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_820)][(-1)]
shen_add_fun('shen.<str>', shen_x60strx62, 1)

@tail_recursion
def shen_x60dbqx62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60dbqx62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1470_824 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_825 = None
        KL_LOC_Parse_Byte_826 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_825', ([setattr(KL_CTX, 'KL_LOC_Parse_Byte_826', car(car(KL_ARG_V1470_824))), (tco_apply(shen_pair, [car(tco_apply(shen_pair, [cdr(car(KL_ARG_V1470_824)), tco_apply(shen_hdtl, [KL_ARG_V1470_824])])), KL_CTX.KL_LOC_Parse_Byte_826]) if shen_eq(KL_CTX.KL_LOC_Parse_Byte_826, 34) else tco_apply(kl_fail, []))][(-1)] if shen_consp(car(KL_ARG_V1470_824)) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_825, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_825)][(-1)]
shen_add_fun('shen.<dbq>', shen_x60dbqx62, 1)

@tail_recursion
def shen_x60strcontentsx62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60strcontentsx62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1475_827 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_828 = None
        KL_LOC_Parse_shen_x60strcx62_829 = None
        KL_LOC_Parse_shen_x60strcontentsx62_830 = None
        KL_LOC_Result_831 = None
        KL_LOC_Parse_x60ex62_832 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_828', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60strcx62_829', tco_apply(shen_x60strcx62, [KL_ARG_V1475_827])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60strcontentsx62_830', tco_apply(shen_x60strcontentsx62, [KL_CTX.KL_LOC_Parse_shen_x60strcx62_829])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60strcontentsx62_830), Cons(tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60strcx62_829]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60strcontentsx62_830]))]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60strcontentsx62_830)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60strcx62_829)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_831', [setattr(KL_CTX, 'KL_LOC_Parse_x60ex62_832', tco_apply(kl_x60ex62, [KL_ARG_V1475_827])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_x60ex62_832), nil]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_x60ex62_832)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_831, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_831)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_828, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_828)][(-1)]
shen_add_fun('shen.<strcontents>', shen_x60strcontentsx62, 1)

@tail_recursion
def shen_x60bytex62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60bytex62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1480_833 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_834 = None
        KL_LOC_Parse_Byte_835 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_834', ([setattr(KL_CTX, 'KL_LOC_Parse_Byte_835', car(car(KL_ARG_V1480_833))), tco_apply(shen_pair, [car(tco_apply(shen_pair, [cdr(car(KL_ARG_V1480_833)), tco_apply(shen_hdtl, [KL_ARG_V1480_833])])), chr(KL_CTX.KL_LOC_Parse_Byte_835)])][(-1)] if shen_consp(car(KL_ARG_V1480_833)) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_834, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_834)][(-1)]
shen_add_fun('shen.<byte>', shen_x60bytex62, 1)

@tail_recursion
def shen_x60strcx62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60strcx62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1485_836 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_837 = None
        KL_LOC_Parse_Byte_838 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_837', ([setattr(KL_CTX, 'KL_LOC_Parse_Byte_838', car(car(KL_ARG_V1485_836))), (tco_apply(shen_pair, [car(tco_apply(shen_pair, [cdr(car(KL_ARG_V1485_836)), tco_apply(shen_hdtl, [KL_ARG_V1485_836])])), chr(KL_CTX.KL_LOC_Parse_Byte_838)]) if (not shen_eq(KL_CTX.KL_LOC_Parse_Byte_838, 34)) else tco_apply(kl_fail, []))][(-1)] if shen_consp(car(KL_ARG_V1485_836)) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_837, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_837)][(-1)]
shen_add_fun('shen.<strc>', shen_x60strcx62, 1)

@tail_recursion
def shen_x60numberx62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60numberx62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1490_839 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_840 = None
        KL_LOC_Parse_shen_x60minusx62_841 = None
        KL_LOC_Parse_shen_x60numberx62_842 = None
        KL_LOC_Result_843 = None
        KL_LOC_Parse_shen_x60plusx62_844 = None
        KL_LOC_Parse_shen_x60numberx62_845 = None
        KL_LOC_Result_846 = None
        KL_LOC_Parse_shen_x60predigitsx62_847 = None
        KL_LOC_Parse_shen_x60stopx62_848 = None
        KL_LOC_Parse_shen_x60postdigitsx62_849 = None
        KL_LOC_Parse_shen_x60Ex62_850 = None
        KL_LOC_Parse_shen_x60log10x62_851 = None
        KL_LOC_Result_852 = None
        KL_LOC_Parse_shen_x60digitsx62_853 = None
        KL_LOC_Parse_shen_x60Ex62_854 = None
        KL_LOC_Parse_shen_x60log10x62_855 = None
        KL_LOC_Result_856 = None
        KL_LOC_Parse_shen_x60predigitsx62_857 = None
        KL_LOC_Parse_shen_x60stopx62_858 = None
        KL_LOC_Parse_shen_x60postdigitsx62_859 = None
        KL_LOC_Result_860 = None
        KL_LOC_Parse_shen_x60digitsx62_861 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_840', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60minusx62_841', tco_apply(shen_x60minusx62, [KL_ARG_V1490_839])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60numberx62_842', tco_apply(shen_x60numberx62, [KL_CTX.KL_LOC_Parse_shen_x60minusx62_841])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60numberx62_842), (0 - tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60numberx62_842]))]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60numberx62_842)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60minusx62_841)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_843', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60plusx62_844', tco_apply(shen_x60plusx62, [KL_ARG_V1490_839])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60numberx62_845', tco_apply(shen_x60numberx62, [KL_CTX.KL_LOC_Parse_shen_x60plusx62_844])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60numberx62_845), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60numberx62_845])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60numberx62_845)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60plusx62_844)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_846', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60predigitsx62_847', tco_apply(shen_x60predigitsx62, [KL_ARG_V1490_839])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60stopx62_848', tco_apply(shen_x60stopx62, [KL_CTX.KL_LOC_Parse_shen_x60predigitsx62_847])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60postdigitsx62_849', tco_apply(shen_x60postdigitsx62, [KL_CTX.KL_LOC_Parse_shen_x60stopx62_848])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60Ex62_850', tco_apply(shen_x60Ex62, [KL_CTX.KL_LOC_Parse_shen_x60postdigitsx62_849])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60log10x62_851', tco_apply(shen_x60log10x62, [KL_CTX.KL_LOC_Parse_shen_x60Ex62_850])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60log10x62_851), (tco_apply(shen_expt, [10, tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60log10x62_851])]) * (tco_apply(shen_pre, [tco_apply(kl_reverse, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60predigitsx62_847])]), 0]) + tco_apply(shen_post, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60postdigitsx62_849]), 1])))]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60log10x62_851)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60Ex62_850)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60postdigitsx62_849)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60stopx62_848)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60predigitsx62_847)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_852', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60digitsx62_853', tco_apply(shen_x60digitsx62, [KL_ARG_V1490_839])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60Ex62_854', tco_apply(shen_x60Ex62, [KL_CTX.KL_LOC_Parse_shen_x60digitsx62_853])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60log10x62_855', tco_apply(shen_x60log10x62, [KL_CTX.KL_LOC_Parse_shen_x60Ex62_854])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60log10x62_855), (tco_apply(shen_expt, [10, tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60log10x62_855])]) * tco_apply(shen_pre, [tco_apply(kl_reverse, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60digitsx62_853])]), 0]))]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60log10x62_855)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60Ex62_854)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60digitsx62_853)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_856', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60predigitsx62_857', tco_apply(shen_x60predigitsx62, [KL_ARG_V1490_839])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60stopx62_858', tco_apply(shen_x60stopx62, [KL_CTX.KL_LOC_Parse_shen_x60predigitsx62_857])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60postdigitsx62_859', tco_apply(shen_x60postdigitsx62, [KL_CTX.KL_LOC_Parse_shen_x60stopx62_858])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60postdigitsx62_859), (tco_apply(shen_pre, [tco_apply(kl_reverse, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60predigitsx62_857])]), 0]) + tco_apply(shen_post, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60postdigitsx62_859]), 1]))]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60postdigitsx62_859)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60stopx62_858)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60predigitsx62_857)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_860', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60digitsx62_861', tco_apply(shen_x60digitsx62, [KL_ARG_V1490_839])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60digitsx62_861), tco_apply(shen_pre, [tco_apply(kl_reverse, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60digitsx62_861])]), 0])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60digitsx62_861)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_860, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_860)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_856, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_856)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_852, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_852)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_846, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_846)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_843, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_843)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_840, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_840)][(-1)]
shen_add_fun('shen.<number>', shen_x60numberx62, 1)

@tail_recursion
def shen_x60Ex62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60Ex62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1495_862 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_863 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_863', (tco_apply(shen_pair, [car(tco_apply(shen_pair, [cdr(car(KL_ARG_V1495_862)), tco_apply(shen_hdtl, [KL_ARG_V1495_862])])), symdic.symdic_shen_skip]) if (shen_eq(101, car(car(KL_ARG_V1495_862))) if shen_consp(car(KL_ARG_V1495_862)) else False) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_863, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_863)][(-1)]
shen_add_fun('shen.<E>', shen_x60Ex62, 1)

@tail_recursion
def shen_x60log10x62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60log10x62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1500_864 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_865 = None
        KL_LOC_Parse_shen_x60minusx62_866 = None
        KL_LOC_Parse_shen_x60digitsx62_867 = None
        KL_LOC_Result_868 = None
        KL_LOC_Parse_shen_x60digitsx62_869 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_865', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60minusx62_866', tco_apply(shen_x60minusx62, [KL_ARG_V1500_864])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60digitsx62_867', tco_apply(shen_x60digitsx62, [KL_CTX.KL_LOC_Parse_shen_x60minusx62_866])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60digitsx62_867), (0 - tco_apply(shen_pre, [tco_apply(kl_reverse, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60digitsx62_867])]), 0]))]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60digitsx62_867)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60minusx62_866)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_868', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60digitsx62_869', tco_apply(shen_x60digitsx62, [KL_ARG_V1500_864])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60digitsx62_869), tco_apply(shen_pre, [tco_apply(kl_reverse, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60digitsx62_869])]), 0])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60digitsx62_869)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_868, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_868)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_865, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_865)][(-1)]
shen_add_fun('shen.<log10>', shen_x60log10x62, 1)

@tail_recursion
def shen_x60plusx62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60plusx62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1505_870 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_871 = None
        KL_LOC_Parse_Byte_872 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_871', ([setattr(KL_CTX, 'KL_LOC_Parse_Byte_872', car(car(KL_ARG_V1505_870))), (tco_apply(shen_pair, [car(tco_apply(shen_pair, [cdr(car(KL_ARG_V1505_870)), tco_apply(shen_hdtl, [KL_ARG_V1505_870])])), KL_CTX.KL_LOC_Parse_Byte_872]) if shen_eq(KL_CTX.KL_LOC_Parse_Byte_872, 43) else tco_apply(kl_fail, []))][(-1)] if shen_consp(car(KL_ARG_V1505_870)) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_871, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_871)][(-1)]
shen_add_fun('shen.<plus>', shen_x60plusx62, 1)

@tail_recursion
def shen_x60stopx62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60stopx62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1510_873 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_874 = None
        KL_LOC_Parse_Byte_875 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_874', ([setattr(KL_CTX, 'KL_LOC_Parse_Byte_875', car(car(KL_ARG_V1510_873))), (tco_apply(shen_pair, [car(tco_apply(shen_pair, [cdr(car(KL_ARG_V1510_873)), tco_apply(shen_hdtl, [KL_ARG_V1510_873])])), KL_CTX.KL_LOC_Parse_Byte_875]) if shen_eq(KL_CTX.KL_LOC_Parse_Byte_875, 46) else tco_apply(kl_fail, []))][(-1)] if shen_consp(car(KL_ARG_V1510_873)) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_874, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_874)][(-1)]
shen_add_fun('shen.<stop>', shen_x60stopx62, 1)

@tail_recursion
def shen_x60predigitsx62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60predigitsx62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1515_876 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_877 = None
        KL_LOC_Parse_shen_x60digitsx62_878 = None
        KL_LOC_Result_879 = None
        KL_LOC_Parse_x60ex62_880 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_877', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60digitsx62_878', tco_apply(shen_x60digitsx62, [KL_ARG_V1515_876])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60digitsx62_878), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60digitsx62_878])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60digitsx62_878)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_879', [setattr(KL_CTX, 'KL_LOC_Parse_x60ex62_880', tco_apply(kl_x60ex62, [KL_ARG_V1515_876])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_x60ex62_880), nil]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_x60ex62_880)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_879, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_879)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_877, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_877)][(-1)]
shen_add_fun('shen.<predigits>', shen_x60predigitsx62, 1)

@tail_recursion
def shen_x60postdigitsx62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60postdigitsx62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1520_881 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_882 = None
        KL_LOC_Parse_shen_x60digitsx62_883 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_882', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60digitsx62_883', tco_apply(shen_x60digitsx62, [KL_ARG_V1520_881])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60digitsx62_883), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60digitsx62_883])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60digitsx62_883)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_882, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_882)][(-1)]
shen_add_fun('shen.<postdigits>', shen_x60postdigitsx62, 1)

@tail_recursion
def shen_x60digitsx62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60digitsx62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1525_884 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_885 = None
        KL_LOC_Parse_shen_x60digitx62_886 = None
        KL_LOC_Parse_shen_x60digitsx62_887 = None
        KL_LOC_Result_888 = None
        KL_LOC_Parse_shen_x60digitx62_889 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_885', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60digitx62_886', tco_apply(shen_x60digitx62, [KL_ARG_V1525_884])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60digitsx62_887', tco_apply(shen_x60digitsx62, [KL_CTX.KL_LOC_Parse_shen_x60digitx62_886])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60digitsx62_887), Cons(tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60digitx62_886]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60digitsx62_887]))]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60digitsx62_887)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60digitx62_886)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_888', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60digitx62_889', tco_apply(shen_x60digitx62, [KL_ARG_V1525_884])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60digitx62_889), Cons(tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60digitx62_889]), nil)]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60digitx62_889)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_888, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_888)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_885, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_885)][(-1)]
shen_add_fun('shen.<digits>', shen_x60digitsx62, 1)

@tail_recursion
def shen_x60digitx62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60digitx62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1530_890 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_891 = None
        KL_LOC_Parse_X_892 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_891', ([setattr(KL_CTX, 'KL_LOC_Parse_X_892', car(car(KL_ARG_V1530_890))), (tco_apply(shen_pair, [car(tco_apply(shen_pair, [cdr(car(KL_ARG_V1530_890)), tco_apply(shen_hdtl, [KL_ARG_V1530_890])])), tco_apply(shen_bytex45x62digit, [KL_CTX.KL_LOC_Parse_X_892])]) if tco_apply(shen_numbytex63, [KL_CTX.KL_LOC_Parse_X_892]) else tco_apply(kl_fail, []))][(-1)] if shen_consp(car(KL_ARG_V1530_890)) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_891, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_891)][(-1)]
shen_add_fun('shen.<digit>', shen_x60digitx62, 1)

@tail_recursion
def shen_bytex45x62digit(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_bytex45x62digit, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1531_893 = FUN_ARGS[0]
    global symdic
    return (0 if shen_eq(48, KL_ARG_V1531_893) else (1 if shen_eq(49, KL_ARG_V1531_893) else (2 if shen_eq(50, KL_ARG_V1531_893) else (3 if shen_eq(51, KL_ARG_V1531_893) else (4 if shen_eq(52, KL_ARG_V1531_893) else (5 if shen_eq(53, KL_ARG_V1531_893) else (6 if shen_eq(54, KL_ARG_V1531_893) else (7 if shen_eq(55, KL_ARG_V1531_893) else (8 if shen_eq(56, KL_ARG_V1531_893) else (9 if shen_eq(57, KL_ARG_V1531_893) else (tail_call(shen_sysx45error, [symdic.symdic_shen_bytex45x62digit]) if True else shen_simple_error('condition failure'))))))))))))
shen_add_fun('shen.byte->digit', shen_bytex45x62digit, 1)

@tail_recursion
def shen_pre(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_pre, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1534_894 = FUN_ARGS[0]
    KL_ARG_V1535_895 = FUN_ARGS[1]
    global symdic
    return (0 if shen_eq(nil, KL_ARG_V1534_894) else (((tco_apply(shen_expt, [10, KL_ARG_V1535_895]) * car(KL_ARG_V1534_894)) + tco_apply(shen_pre, [cdr(KL_ARG_V1534_894), (KL_ARG_V1535_895 + 1)])) if shen_consp(KL_ARG_V1534_894) else (tail_call(shen_sysx45error, [symdic.symdic_shen_pre]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.pre', shen_pre, 2)

@tail_recursion
def shen_post(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_post, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1538_896 = FUN_ARGS[0]
    KL_ARG_V1539_897 = FUN_ARGS[1]
    global symdic
    return (0 if shen_eq(nil, KL_ARG_V1538_896) else (((tco_apply(shen_expt, [10, (0 - KL_ARG_V1539_897)]) * car(KL_ARG_V1538_896)) + tco_apply(shen_post, [cdr(KL_ARG_V1538_896), (KL_ARG_V1539_897 + 1)])) if shen_consp(KL_ARG_V1538_896) else (tail_call(shen_sysx45error, [symdic.symdic_shen_post]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.post', shen_post, 2)

@tail_recursion
def shen_expt(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_expt, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1542_898 = FUN_ARGS[0]
    KL_ARG_V1543_899 = FUN_ARGS[1]
    global symdic
    return (1 if shen_eq(0, KL_ARG_V1543_899) else ((KL_ARG_V1542_898 * tco_apply(shen_expt, [KL_ARG_V1542_898, (KL_ARG_V1543_899 - 1)])) if (KL_ARG_V1543_899 > 0) else ((1 * (tco_apply(shen_expt, [KL_ARG_V1542_898, (KL_ARG_V1543_899 + 1)]) / KL_ARG_V1542_898)) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.expt', shen_expt, 2)

@tail_recursion
def shen_x60st_input1x62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60st_input1x62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1548_900 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_901 = None
        KL_LOC_Parse_shen_x60st_inputx62_902 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_901', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_inputx62_902', tco_apply(shen_x60st_inputx62, [KL_ARG_V1548_900])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_902), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_902])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_902)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_901, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_901)][(-1)]
shen_add_fun('shen.<st_input1>', shen_x60st_input1x62, 1)

@tail_recursion
def shen_x60st_input2x62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60st_input2x62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1553_903 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_904 = None
        KL_LOC_Parse_shen_x60st_inputx62_905 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_904', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_inputx62_905', tco_apply(shen_x60st_inputx62, [KL_ARG_V1553_903])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_905), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_905])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_905)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_904, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_904)][(-1)]
shen_add_fun('shen.<st_input2>', shen_x60st_input2x62, 1)

@tail_recursion
def shen_x60commentx62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60commentx62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1558_906 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_907 = None
        KL_LOC_Parse_shen_x60singlelinex62_908 = None
        KL_LOC_Result_909 = None
        KL_LOC_Parse_shen_x60multilinex62_910 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_907', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60singlelinex62_908', tco_apply(shen_x60singlelinex62, [KL_ARG_V1558_906])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60singlelinex62_908), symdic.symdic_shen_skip]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60singlelinex62_908)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_909', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60multilinex62_910', tco_apply(shen_x60multilinex62, [KL_ARG_V1558_906])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60multilinex62_910), symdic.symdic_shen_skip]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60multilinex62_910)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_909, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_909)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_907, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_907)][(-1)]
shen_add_fun('shen.<comment>', shen_x60commentx62, 1)

@tail_recursion
def shen_x60singlelinex62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60singlelinex62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1563_911 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_912 = None
        KL_LOC_Parse_shen_x60backslashx62_913 = None
        KL_LOC_Parse_shen_x60backslashx62_914 = None
        KL_LOC_Parse_shen_x60anysinglex62_915 = None
        KL_LOC_Parse_shen_x60returnx62_916 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_912', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60backslashx62_913', tco_apply(shen_x60backslashx62, [KL_ARG_V1563_911])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60backslashx62_914', tco_apply(shen_x60backslashx62, [KL_CTX.KL_LOC_Parse_shen_x60backslashx62_913])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60anysinglex62_915', tco_apply(shen_x60anysinglex62, [KL_CTX.KL_LOC_Parse_shen_x60backslashx62_914])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60returnx62_916', tco_apply(shen_x60returnx62, [KL_CTX.KL_LOC_Parse_shen_x60anysinglex62_915])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60returnx62_916), symdic.symdic_shen_skip]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60returnx62_916)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60anysinglex62_915)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60backslashx62_914)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60backslashx62_913)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_912, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_912)][(-1)]
shen_add_fun('shen.<singleline>', shen_x60singlelinex62, 1)

@tail_recursion
def shen_x60backslashx62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60backslashx62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1568_917 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_918 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_918', (tco_apply(shen_pair, [car(tco_apply(shen_pair, [cdr(car(KL_ARG_V1568_917)), tco_apply(shen_hdtl, [KL_ARG_V1568_917])])), symdic.symdic_shen_skip]) if (shen_eq(92, car(car(KL_ARG_V1568_917))) if shen_consp(car(KL_ARG_V1568_917)) else False) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_918, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_918)][(-1)]
shen_add_fun('shen.<backslash>', shen_x60backslashx62, 1)

@tail_recursion
def shen_x60anysinglex62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60anysinglex62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1573_919 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_920 = None
        KL_LOC_Parse_shen_x60nonx45returnx62_921 = None
        KL_LOC_Parse_shen_x60anysinglex62_922 = None
        KL_LOC_Result_923 = None
        KL_LOC_Parse_x60ex62_924 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_920', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60nonx45returnx62_921', tco_apply(shen_x60nonx45returnx62, [KL_ARG_V1573_919])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60anysinglex62_922', tco_apply(shen_x60anysinglex62, [KL_CTX.KL_LOC_Parse_shen_x60nonx45returnx62_921])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60anysinglex62_922), symdic.symdic_shen_skip]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60anysinglex62_922)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60nonx45returnx62_921)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_923', [setattr(KL_CTX, 'KL_LOC_Parse_x60ex62_924', tco_apply(kl_x60ex62, [KL_ARG_V1573_919])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_x60ex62_924), symdic.symdic_shen_skip]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_x60ex62_924)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_923, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_923)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_920, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_920)][(-1)]
shen_add_fun('shen.<anysingle>', shen_x60anysinglex62, 1)

@tail_recursion
def shen_x60nonx45returnx62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60nonx45returnx62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1578_925 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_926 = None
        KL_LOC_Parse_X_927 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_926', ([setattr(KL_CTX, 'KL_LOC_Parse_X_927', car(car(KL_ARG_V1578_925))), (tco_apply(shen_pair, [car(tco_apply(shen_pair, [cdr(car(KL_ARG_V1578_925)), tco_apply(shen_hdtl, [KL_ARG_V1578_925])])), symdic.symdic_shen_skip]) if (not tco_apply(kl_elementx63, [KL_CTX.KL_LOC_Parse_X_927, Cons(10, Cons(13, nil))])) else tco_apply(kl_fail, []))][(-1)] if shen_consp(car(KL_ARG_V1578_925)) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_926, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_926)][(-1)]
shen_add_fun('shen.<non-return>', shen_x60nonx45returnx62, 1)

@tail_recursion
def shen_x60returnx62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60returnx62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1583_928 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_929 = None
        KL_LOC_Parse_X_930 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_929', ([setattr(KL_CTX, 'KL_LOC_Parse_X_930', car(car(KL_ARG_V1583_928))), (tco_apply(shen_pair, [car(tco_apply(shen_pair, [cdr(car(KL_ARG_V1583_928)), tco_apply(shen_hdtl, [KL_ARG_V1583_928])])), symdic.symdic_shen_skip]) if tco_apply(kl_elementx63, [KL_CTX.KL_LOC_Parse_X_930, Cons(10, Cons(13, nil))]) else tco_apply(kl_fail, []))][(-1)] if shen_consp(car(KL_ARG_V1583_928)) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_929, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_929)][(-1)]
shen_add_fun('shen.<return>', shen_x60returnx62, 1)

@tail_recursion
def shen_x60multilinex62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60multilinex62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1588_931 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_932 = None
        KL_LOC_Parse_shen_x60backslashx62_933 = None
        KL_LOC_Parse_shen_x60timesx62_934 = None
        KL_LOC_Parse_shen_x60anymultix62_935 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_932', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60backslashx62_933', tco_apply(shen_x60backslashx62, [KL_ARG_V1588_931])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60timesx62_934', tco_apply(shen_x60timesx62, [KL_CTX.KL_LOC_Parse_shen_x60backslashx62_933])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60anymultix62_935', tco_apply(shen_x60anymultix62, [KL_CTX.KL_LOC_Parse_shen_x60timesx62_934])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60anymultix62_935), symdic.symdic_shen_skip]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60anymultix62_935)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60timesx62_934)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60backslashx62_933)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_932, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_932)][(-1)]
shen_add_fun('shen.<multiline>', shen_x60multilinex62, 1)

@tail_recursion
def shen_x60timesx62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60timesx62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1593_936 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_937 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_937', (tco_apply(shen_pair, [car(tco_apply(shen_pair, [cdr(car(KL_ARG_V1593_936)), tco_apply(shen_hdtl, [KL_ARG_V1593_936])])), symdic.symdic_shen_skip]) if (shen_eq(42, car(car(KL_ARG_V1593_936))) if shen_consp(car(KL_ARG_V1593_936)) else False) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_937, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_937)][(-1)]
shen_add_fun('shen.<times>', shen_x60timesx62, 1)

@tail_recursion
def shen_x60anymultix62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60anymultix62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1598_938 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_939 = None
        KL_LOC_Parse_shen_x60commentx62_940 = None
        KL_LOC_Parse_shen_x60anymultix62_941 = None
        KL_LOC_Result_942 = None
        KL_LOC_Parse_shen_x60timesx62_943 = None
        KL_LOC_Parse_shen_x60backslashx62_944 = None
        KL_LOC_Result_945 = None
        KL_LOC_Parse_X_946 = None
        KL_LOC_Parse_shen_x60anymultix62_947 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_939', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60commentx62_940', tco_apply(shen_x60commentx62, [KL_ARG_V1598_938])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60anymultix62_941', tco_apply(shen_x60anymultix62, [KL_CTX.KL_LOC_Parse_shen_x60commentx62_940])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60anymultix62_941), symdic.symdic_shen_skip]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60anymultix62_941)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60commentx62_940)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_942', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60timesx62_943', tco_apply(shen_x60timesx62, [KL_ARG_V1598_938])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60backslashx62_944', tco_apply(shen_x60backslashx62, [KL_CTX.KL_LOC_Parse_shen_x60timesx62_943])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60backslashx62_944), symdic.symdic_shen_skip]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60backslashx62_944)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60timesx62_943)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_945', ([setattr(KL_CTX, 'KL_LOC_Parse_X_946', car(car(KL_ARG_V1598_938))), [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60anymultix62_947', tco_apply(shen_x60anymultix62, [tco_apply(shen_pair, [cdr(car(KL_ARG_V1598_938)), tco_apply(shen_hdtl, [KL_ARG_V1598_938])])])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60anymultix62_947), symdic.symdic_shen_skip]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60anymultix62_947)) else tco_apply(kl_fail, []))][(-1)]][(-1)] if shen_consp(car(KL_ARG_V1598_938)) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_945, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_945)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_942, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_942)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_939, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_939)][(-1)]
shen_add_fun('shen.<anymulti>', shen_x60anymultix62, 1)

@tail_recursion
def shen_x60whitespacesx62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60whitespacesx62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1603_948 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_949 = None
        KL_LOC_Parse_shen_x60whitespacex62_950 = None
        KL_LOC_Parse_shen_x60whitespacesx62_951 = None
        KL_LOC_Result_952 = None
        KL_LOC_Parse_shen_x60whitespacex62_953 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_949', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60whitespacex62_950', tco_apply(shen_x60whitespacex62, [KL_ARG_V1603_948])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60whitespacesx62_951', tco_apply(shen_x60whitespacesx62, [KL_CTX.KL_LOC_Parse_shen_x60whitespacex62_950])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60whitespacesx62_951), symdic.symdic_shen_skip]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60whitespacesx62_951)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60whitespacex62_950)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_952', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60whitespacex62_953', tco_apply(shen_x60whitespacex62, [KL_ARG_V1603_948])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60whitespacex62_953), symdic.symdic_shen_skip]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60whitespacex62_953)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_952, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_952)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_949, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_949)][(-1)]
shen_add_fun('shen.<whitespaces>', shen_x60whitespacesx62, 1)

@tail_recursion
def shen_x60whitespacex62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60whitespacex62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1608_954 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_955 = None
        KL_LOC_Parse_X_956 = None
        KL_LOC_Parse_Case_957 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_955', ([setattr(KL_CTX, 'KL_LOC_Parse_X_956', car(car(KL_ARG_V1608_954))), (tco_apply(shen_pair, [car(tco_apply(shen_pair, [cdr(car(KL_ARG_V1608_954)), tco_apply(shen_hdtl, [KL_ARG_V1608_954])])), symdic.symdic_shen_skip]) if [setattr(KL_CTX, 'KL_LOC_Parse_Case_957', KL_CTX.KL_LOC_Parse_X_956), (True if shen_eq(KL_CTX.KL_LOC_Parse_Case_957, 32) else (True if shen_eq(KL_CTX.KL_LOC_Parse_Case_957, 13) else (True if shen_eq(KL_CTX.KL_LOC_Parse_Case_957, 10) else shen_eq(KL_CTX.KL_LOC_Parse_Case_957, 9))))][(-1)] else tco_apply(kl_fail, []))][(-1)] if shen_consp(car(KL_ARG_V1608_954)) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_955, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_955)][(-1)]
shen_add_fun('shen.<whitespace>', shen_x60whitespacex62, 1)

@tail_recursion
def shen_cons_form(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_cons_form, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1609_958 = FUN_ARGS[0]
    global symdic
    return (nil if shen_eq(nil, KL_ARG_V1609_958) else (Cons(symdic.symdic_kl_cons, Cons(car(KL_ARG_V1609_958), cdr(cdr(KL_ARG_V1609_958)))) if ((((shen_eq(car(cdr(KL_ARG_V1609_958)), symdic.symdic_kl_barx33) if shen_eq(nil, cdr(cdr(cdr(KL_ARG_V1609_958)))) else False) if shen_consp(cdr(cdr(KL_ARG_V1609_958))) else False) if shen_consp(cdr(KL_ARG_V1609_958)) else False) if shen_consp(KL_ARG_V1609_958) else False) else (Cons(symdic.symdic_kl_cons, Cons(car(KL_ARG_V1609_958), Cons(tco_apply(shen_cons_form, [cdr(KL_ARG_V1609_958)]), nil))) if shen_consp(KL_ARG_V1609_958) else (tail_call(shen_sysx45error, [symdic.symdic_shen_cons_form]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.cons_form', shen_cons_form, 1)

@tail_recursion
def shen_packagex45macro(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_packagex45macro, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1612_959 = FUN_ARGS[0]
    KL_ARG_V1613_960 = FUN_ARGS[1]

    class KL_Context:
        KL_LOC_ListofExceptions_961 = None
        KL_LOC_Record_962 = None
        KL_LOC_PackageNameDot_963 = None
    KL_CTX = KL_Context()
    global symdic
    return (tail_call(kl_append, [tco_apply(kl_explode, [car(cdr(KL_ARG_V1612_959))]), KL_ARG_V1613_960]) if (((shen_eq(nil, cdr(cdr(KL_ARG_V1612_959))) if shen_consp(cdr(KL_ARG_V1612_959)) else False) if shen_eq(symdic.symdic_kl_x36, car(KL_ARG_V1612_959)) else False) if shen_consp(KL_ARG_V1612_959) else False) else (tail_call(kl_append, [cdr(cdr(cdr(KL_ARG_V1612_959))), KL_ARG_V1613_960]) if ((((shen_consp(cdr(cdr(KL_ARG_V1612_959))) if shen_eq(symdic.symdic_kl_null, car(cdr(KL_ARG_V1612_959))) else False) if shen_consp(cdr(KL_ARG_V1612_959)) else False) if shen_eq(symdic.symdic_kl_package, car(KL_ARG_V1612_959)) else False) if shen_consp(KL_ARG_V1612_959) else False) else ([setattr(KL_CTX, 'KL_LOC_ListofExceptions_961', tco_apply(shen_evalx45withoutx45macros, [car(cdr(cdr(KL_ARG_V1612_959)))])), [setattr(KL_CTX, 'KL_LOC_Record_962', tco_apply(shen_recordx45exceptions, [KL_CTX.KL_LOC_ListofExceptions_961, car(cdr(KL_ARG_V1612_959))])), [setattr(KL_CTX, 'KL_LOC_PackageNameDot_963', shen_intern((str(car(cdr(KL_ARG_V1612_959))) + '.'))), tail_call(kl_append, [tco_apply(shen_packageh, [KL_CTX.KL_LOC_PackageNameDot_963, KL_CTX.KL_LOC_ListofExceptions_961, cdr(cdr(cdr(KL_ARG_V1612_959)))]), KL_ARG_V1613_960])][(-1)]][(-1)]][(-1)] if (((shen_consp(cdr(cdr(KL_ARG_V1612_959))) if shen_consp(cdr(KL_ARG_V1612_959)) else False) if shen_eq(symdic.symdic_kl_package, car(KL_ARG_V1612_959)) else False) if shen_consp(KL_ARG_V1612_959) else False) else (Cons(KL_ARG_V1612_959, KL_ARG_V1613_960) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.package-macro', shen_packagex45macro, 2)

@tail_recursion
def shen_recordx45exceptions(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_recordx45exceptions, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1614_964 = FUN_ARGS[0]
    KL_ARG_V1615_965 = FUN_ARGS[1]

    class KL_Context:
        KL_LOC_CurrExceptions_966 = None
        KL_LOC_AllExceptions_968 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_CurrExceptions_966', shen_try_except((lambda : tco_apply(kl_get, [KL_ARG_V1615_965, symdic.symdic_shen_externalx45symbols, shen_get(symdic.symdic_kl_x42propertyx45vectorx42)])), (lambda KL_ARG_E_967: nil))), [setattr(KL_CTX, 'KL_LOC_AllExceptions_968', tco_apply(kl_union, [KL_ARG_V1614_964, KL_CTX.KL_LOC_CurrExceptions_966])), tail_call(kl_put, [KL_ARG_V1615_965, symdic.symdic_shen_externalx45symbols, KL_CTX.KL_LOC_AllExceptions_968, shen_get(symdic.symdic_kl_x42propertyx45vectorx42)])][(-1)]][(-1)]
shen_add_fun('shen.record-exceptions', shen_recordx45exceptions, 2)

@tail_recursion
def shen_packageh(*FUN_ARGS):
    FUN_ARITY = 3
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_packageh, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1624_969 = FUN_ARGS[0]
    KL_ARG_V1625_970 = FUN_ARGS[1]
    KL_ARG_V1626_971 = FUN_ARGS[2]
    global symdic
    return (Cons(tco_apply(shen_packageh, [KL_ARG_V1624_969, KL_ARG_V1625_970, car(KL_ARG_V1626_971)]), tco_apply(shen_packageh, [KL_ARG_V1624_969, KL_ARG_V1625_970, cdr(KL_ARG_V1626_971)])) if shen_consp(KL_ARG_V1626_971) else (KL_ARG_V1626_971 if (True if tco_apply(shen_sysfuncx63, [KL_ARG_V1626_971]) else (True if tco_apply(kl_variablex63, [KL_ARG_V1626_971]) else (True if tco_apply(kl_elementx63, [KL_ARG_V1626_971, KL_ARG_V1625_970]) else (True if tco_apply(shen_doubleunderlinex63, [KL_ARG_V1626_971]) else tco_apply(shen_singleunderlinex63, [KL_ARG_V1626_971]))))) else (tail_call(kl_concat, [KL_ARG_V1624_969, KL_ARG_V1626_971]) if ((not tco_apply(shen_prefixx63, [Cons('s', Cons('h', Cons('e', Cons('n', Cons('.', nil))))), tco_apply(kl_explode, [KL_ARG_V1626_971])])) if tco_apply(kl_symbolx63, [KL_ARG_V1626_971]) else False) else (KL_ARG_V1626_971 if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.packageh', shen_packageh, 3)

@tail_recursion
def kl_readx45fromx45string(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_readx45fromx45string, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1627_972 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Ns_973 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Ns_973', tco_apply(kl_map, [(lambda KL_ARG_V1327_974: ord(KL_ARG_V1327_974)), tco_apply(kl_explode, [KL_ARG_V1627_972])])), tail_call(kl_compile, [symdic.symdic_shen_x60st_inputx62, KL_CTX.KL_LOC_Ns_973, symdic.symdic_shen_readx45error])][(-1)]
shen_add_fun('read-from-string', kl_readx45fromx45string, 1)


#============================== prolog.kl==============================



@tail_recursion
def shen_x60defprologx62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60defprologx62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V927_975 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_976 = None
        KL_LOC_Parse_shen_x60predicatex42x62_977 = None
        KL_LOC_Parse_shen_x60clausesx42x62_978 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_976', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60predicatex42x62_977', tco_apply(shen_x60predicatex42x62, [KL_ARG_V927_975])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60clausesx42x62_978', tco_apply(shen_x60clausesx42x62, [KL_CTX.KL_LOC_Parse_shen_x60predicatex42x62_977])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60clausesx42x62_978), car(tco_apply(shen_prologx45x62shen, [tco_apply(kl_map, [(lambda KL_ARG_Parse_X_979: tail_call(shen_insertx45predicate, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60predicatex42x62_977]), KL_ARG_Parse_X_979])), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60clausesx42x62_978])])]))]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60clausesx42x62_978)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60predicatex42x62_977)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_976, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_976)][(-1)]
shen_add_fun('shen.<defprolog>', shen_x60defprologx62, 1)

@tail_recursion
def shen_prologx45error(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_prologx45error, (FUN_ARGS + lambdaargs)))
    KL_ARG_V934_980 = FUN_ARGS[0]
    KL_ARG_V935_981 = FUN_ARGS[1]
    global symdic
    return (shen_simple_error(('prolog syntax error in ' + tco_apply(shen_app, [KL_ARG_V934_980, (' here:\r\n\r\n ' + tco_apply(shen_app, [tco_apply(shen_nextx4550, [50, car(KL_ARG_V935_981)]), '\r\n', symdic.symdic_shen_a])), symdic.symdic_shen_a]))) if ((shen_eq(nil, cdr(cdr(KL_ARG_V935_981))) if shen_consp(cdr(KL_ARG_V935_981)) else False) if shen_consp(KL_ARG_V935_981) else False) else (shen_simple_error(('prolog syntax error in ' + tco_apply(shen_app, [KL_ARG_V934_980, '\r\n', symdic.symdic_shen_a]))) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.prolog-error', shen_prologx45error, 2)

@tail_recursion
def shen_nextx4550(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_nextx4550, (FUN_ARGS + lambdaargs)))
    KL_ARG_V940_982 = FUN_ARGS[0]
    KL_ARG_V941_983 = FUN_ARGS[1]
    global symdic
    return ('' if shen_eq(nil, KL_ARG_V941_983) else ('' if shen_eq(0, KL_ARG_V940_982) else ((tco_apply(shen_deconsx45string, [car(KL_ARG_V941_983)]) + tco_apply(shen_nextx4550, [(KL_ARG_V940_982 - 1), cdr(KL_ARG_V941_983)])) if shen_consp(KL_ARG_V941_983) else (tail_call(shen_sysx45error, [symdic.symdic_shen_nextx4550]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.next-50', shen_nextx4550, 2)

@tail_recursion
def shen_deconsx45string(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_deconsx45string, (FUN_ARGS + lambdaargs)))
    KL_ARG_V942_984 = FUN_ARGS[0]
    global symdic
    return (tail_call(shen_app, [tco_apply(shen_evalx45cons, [KL_ARG_V942_984]), ' ', symdic.symdic_shen_s]) if ((((shen_eq(nil, cdr(cdr(cdr(KL_ARG_V942_984)))) if shen_consp(cdr(cdr(KL_ARG_V942_984))) else False) if shen_consp(cdr(KL_ARG_V942_984)) else False) if shen_eq(symdic.symdic_kl_cons, car(KL_ARG_V942_984)) else False) if shen_consp(KL_ARG_V942_984) else False) else (tail_call(shen_app, [KL_ARG_V942_984, ' ', symdic.symdic_shen_r]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.decons-string', shen_deconsx45string, 1)

@tail_recursion
def shen_insertx45predicate(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_insertx45predicate, (FUN_ARGS + lambdaargs)))
    KL_ARG_V943_985 = FUN_ARGS[0]
    KL_ARG_V944_986 = FUN_ARGS[1]
    global symdic
    return (Cons(Cons(KL_ARG_V943_985, car(KL_ARG_V944_986)), Cons(symdic.symdic_kl_x58x45, cdr(KL_ARG_V944_986))) if ((shen_eq(nil, cdr(cdr(KL_ARG_V944_986))) if shen_consp(cdr(KL_ARG_V944_986)) else False) if shen_consp(KL_ARG_V944_986) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_insertx45predicate]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.insert-predicate', shen_insertx45predicate, 2)

@tail_recursion
def shen_x60predicatex42x62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60predicatex42x62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V949_987 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_988 = None
        KL_LOC_Parse_X_989 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_988', ([setattr(KL_CTX, 'KL_LOC_Parse_X_989', car(car(KL_ARG_V949_987))), tco_apply(shen_pair, [car(tco_apply(shen_pair, [cdr(car(KL_ARG_V949_987)), tco_apply(shen_hdtl, [KL_ARG_V949_987])])), KL_CTX.KL_LOC_Parse_X_989])][(-1)] if shen_consp(car(KL_ARG_V949_987)) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_988, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_988)][(-1)]
shen_add_fun('shen.<predicate*>', shen_x60predicatex42x62, 1)

@tail_recursion
def shen_x60clausesx42x62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60clausesx42x62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V954_990 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_991 = None
        KL_LOC_Parse_shen_x60clausex42x62_992 = None
        KL_LOC_Parse_shen_x60clausesx42x62_993 = None
        KL_LOC_Result_994 = None
        KL_LOC_Parse_x60ex62_995 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_991', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60clausex42x62_992', tco_apply(shen_x60clausex42x62, [KL_ARG_V954_990])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60clausesx42x62_993', tco_apply(shen_x60clausesx42x62, [KL_CTX.KL_LOC_Parse_shen_x60clausex42x62_992])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60clausesx42x62_993), Cons(tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60clausex42x62_992]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60clausesx42x62_993]))]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60clausesx42x62_993)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60clausex42x62_992)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_994', [setattr(KL_CTX, 'KL_LOC_Parse_x60ex62_995', tco_apply(kl_x60ex62, [KL_ARG_V954_990])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_x60ex62_995), tco_apply(kl_append, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_x60ex62_995]), nil])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_x60ex62_995)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_994, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_994)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_991, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_991)][(-1)]
shen_add_fun('shen.<clauses*>', shen_x60clausesx42x62, 1)

@tail_recursion
def shen_x60clausex42x62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60clausex42x62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V959_996 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_997 = None
        KL_LOC_Parse_shen_x60headx42x62_998 = None
        KL_LOC_Parse_shen_x60bodyx42x62_999 = None
        KL_LOC_Parse_shen_x60endx42x62_1000 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_997', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60headx42x62_998', tco_apply(shen_x60headx42x62, [KL_ARG_V959_996])), (([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60bodyx42x62_999', tco_apply(shen_x60bodyx42x62, [tco_apply(shen_pair, [cdr(car(KL_CTX.KL_LOC_Parse_shen_x60headx42x62_998)), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60headx42x62_998])])])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60endx42x62_1000', tco_apply(shen_x60endx42x62, [KL_CTX.KL_LOC_Parse_shen_x60bodyx42x62_999])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60endx42x62_1000), Cons(tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60headx42x62_998]), Cons(tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60bodyx42x62_999]), nil))]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60endx42x62_1000)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60bodyx42x62_999)) else tco_apply(kl_fail, []))][(-1)] if (shen_eq(symdic.symdic_kl_x60x45x45, car(car(KL_CTX.KL_LOC_Parse_shen_x60headx42x62_998))) if shen_consp(car(KL_CTX.KL_LOC_Parse_shen_x60headx42x62_998)) else False) else tco_apply(kl_fail, [])) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60headx42x62_998)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_997, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_997)][(-1)]
shen_add_fun('shen.<clause*>', shen_x60clausex42x62, 1)

@tail_recursion
def shen_x60headx42x62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60headx42x62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V964_1001 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_1002 = None
        KL_LOC_Parse_shen_x60termx42x62_1003 = None
        KL_LOC_Parse_shen_x60headx42x62_1004 = None
        KL_LOC_Result_1005 = None
        KL_LOC_Parse_x60ex62_1006 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_1002', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60termx42x62_1003', tco_apply(shen_x60termx42x62, [KL_ARG_V964_1001])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60headx42x62_1004', tco_apply(shen_x60headx42x62, [KL_CTX.KL_LOC_Parse_shen_x60termx42x62_1003])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60headx42x62_1004), Cons(tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60termx42x62_1003]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60headx42x62_1004]))]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60headx42x62_1004)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60termx42x62_1003)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_1005', [setattr(KL_CTX, 'KL_LOC_Parse_x60ex62_1006', tco_apply(kl_x60ex62, [KL_ARG_V964_1001])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_x60ex62_1006), tco_apply(kl_append, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_x60ex62_1006]), nil])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_x60ex62_1006)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_1005, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_1005)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_1002, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_1002)][(-1)]
shen_add_fun('shen.<head*>', shen_x60headx42x62, 1)

@tail_recursion
def shen_x60termx42x62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60termx42x62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V969_1007 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_1008 = None
        KL_LOC_Parse_X_1009 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_1008', ([setattr(KL_CTX, 'KL_LOC_Parse_X_1009', car(car(KL_ARG_V969_1007))), (tco_apply(shen_pair, [car(tco_apply(shen_pair, [cdr(car(KL_ARG_V969_1007)), tco_apply(shen_hdtl, [KL_ARG_V969_1007])])), tco_apply(shen_evalx45cons, [KL_CTX.KL_LOC_Parse_X_1009])]) if (tco_apply(shen_legitimatex45termx63, [KL_CTX.KL_LOC_Parse_X_1009]) if (not shen_eq(symdic.symdic_kl_x60x45x45, KL_CTX.KL_LOC_Parse_X_1009)) else False) else tco_apply(kl_fail, []))][(-1)] if shen_consp(car(KL_ARG_V969_1007)) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_1008, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_1008)][(-1)]
shen_add_fun('shen.<term*>', shen_x60termx42x62, 1)

@tail_recursion
def shen_legitimatex45termx63(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_legitimatex45termx63, (FUN_ARGS + lambdaargs)))
    KL_ARG_V974_1010 = FUN_ARGS[0]
    global symdic
    return ((tail_call(shen_legitimatex45termx63, [car(cdr(cdr(KL_ARG_V974_1010)))]) if tco_apply(shen_legitimatex45termx63, [car(cdr(KL_ARG_V974_1010))]) else False) if ((((shen_eq(nil, cdr(cdr(cdr(KL_ARG_V974_1010)))) if shen_consp(cdr(cdr(KL_ARG_V974_1010))) else False) if shen_consp(cdr(KL_ARG_V974_1010)) else False) if shen_eq(symdic.symdic_kl_cons, car(KL_ARG_V974_1010)) else False) if shen_consp(KL_ARG_V974_1010) else False) else (tail_call(shen_legitimatex45termx63, [car(cdr(KL_ARG_V974_1010))]) if (((((shen_eq(nil, cdr(cdr(cdr(KL_ARG_V974_1010)))) if shen_eq(symdic.symdic_kl_x43, car(cdr(cdr(KL_ARG_V974_1010)))) else False) if shen_consp(cdr(cdr(KL_ARG_V974_1010))) else False) if shen_consp(cdr(KL_ARG_V974_1010)) else False) if shen_eq(symdic.symdic_kl_mode, car(KL_ARG_V974_1010)) else False) if shen_consp(KL_ARG_V974_1010) else False) else (tail_call(shen_legitimatex45termx63, [car(cdr(KL_ARG_V974_1010))]) if (((((shen_eq(nil, cdr(cdr(cdr(KL_ARG_V974_1010)))) if shen_eq(symdic.symdic_kl_x45, car(cdr(cdr(KL_ARG_V974_1010)))) else False) if shen_consp(cdr(cdr(KL_ARG_V974_1010))) else False) if shen_consp(cdr(KL_ARG_V974_1010)) else False) if shen_eq(symdic.symdic_kl_mode, car(KL_ARG_V974_1010)) else False) if shen_consp(KL_ARG_V974_1010) else False) else (False if shen_consp(KL_ARG_V974_1010) else (True if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.legitimate-term?', shen_legitimatex45termx63, 1)

@tail_recursion
def shen_evalx45cons(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_evalx45cons, (FUN_ARGS + lambdaargs)))
    KL_ARG_V975_1011 = FUN_ARGS[0]
    global symdic
    return (Cons(tco_apply(shen_evalx45cons, [car(cdr(KL_ARG_V975_1011))]), tco_apply(shen_evalx45cons, [car(cdr(cdr(KL_ARG_V975_1011)))])) if ((((shen_eq(nil, cdr(cdr(cdr(KL_ARG_V975_1011)))) if shen_consp(cdr(cdr(KL_ARG_V975_1011))) else False) if shen_consp(cdr(KL_ARG_V975_1011)) else False) if shen_eq(symdic.symdic_kl_cons, car(KL_ARG_V975_1011)) else False) if shen_consp(KL_ARG_V975_1011) else False) else (Cons(symdic.symdic_kl_mode, Cons(tco_apply(shen_evalx45cons, [car(cdr(KL_ARG_V975_1011))]), cdr(cdr(KL_ARG_V975_1011)))) if ((((shen_eq(nil, cdr(cdr(cdr(KL_ARG_V975_1011)))) if shen_consp(cdr(cdr(KL_ARG_V975_1011))) else False) if shen_consp(cdr(KL_ARG_V975_1011)) else False) if shen_eq(symdic.symdic_kl_mode, car(KL_ARG_V975_1011)) else False) if shen_consp(KL_ARG_V975_1011) else False) else (KL_ARG_V975_1011 if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.eval-cons', shen_evalx45cons, 1)

@tail_recursion
def shen_x60bodyx42x62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60bodyx42x62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V980_1012 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_1013 = None
        KL_LOC_Parse_shen_x60literalx42x62_1014 = None
        KL_LOC_Parse_shen_x60bodyx42x62_1015 = None
        KL_LOC_Result_1016 = None
        KL_LOC_Parse_x60ex62_1017 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_1013', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60literalx42x62_1014', tco_apply(shen_x60literalx42x62, [KL_ARG_V980_1012])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60bodyx42x62_1015', tco_apply(shen_x60bodyx42x62, [KL_CTX.KL_LOC_Parse_shen_x60literalx42x62_1014])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60bodyx42x62_1015), Cons(tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60literalx42x62_1014]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60bodyx42x62_1015]))]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60bodyx42x62_1015)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60literalx42x62_1014)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_1016', [setattr(KL_CTX, 'KL_LOC_Parse_x60ex62_1017', tco_apply(kl_x60ex62, [KL_ARG_V980_1012])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_x60ex62_1017), tco_apply(kl_append, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_x60ex62_1017]), nil])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_x60ex62_1017)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_1016, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_1016)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_1013, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_1013)][(-1)]
shen_add_fun('shen.<body*>', shen_x60bodyx42x62, 1)

@tail_recursion
def shen_x60literalx42x62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60literalx42x62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V985_1018 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_1019 = None
        KL_LOC_Result_1020 = None
        KL_LOC_Parse_X_1021 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_1019', (tco_apply(shen_pair, [car(tco_apply(shen_pair, [cdr(car(KL_ARG_V985_1018)), tco_apply(shen_hdtl, [KL_ARG_V985_1018])])), Cons(symdic.symdic_kl_cut, Cons(shen_intern('Throwcontrol'), nil))]) if (shen_eq(symdic.symdic_kl_x33, car(car(KL_ARG_V985_1018))) if shen_consp(car(KL_ARG_V985_1018)) else False) else tco_apply(kl_fail, []))), ([setattr(KL_CTX, 'KL_LOC_Result_1020', ([setattr(KL_CTX, 'KL_LOC_Parse_X_1021', car(car(KL_ARG_V985_1018))), (tco_apply(shen_pair, [car(tco_apply(shen_pair, [cdr(car(KL_ARG_V985_1018)), tco_apply(shen_hdtl, [KL_ARG_V985_1018])])), KL_CTX.KL_LOC_Parse_X_1021]) if shen_consp(KL_CTX.KL_LOC_Parse_X_1021) else tco_apply(kl_fail, []))][(-1)] if shen_consp(car(KL_ARG_V985_1018)) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_1020, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_1020)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_1019, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_1019)][(-1)]
shen_add_fun('shen.<literal*>', shen_x60literalx42x62, 1)

@tail_recursion
def shen_x60endx42x62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60endx42x62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V990_1022 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_1023 = None
        KL_LOC_Parse_X_1024 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_1023', ([setattr(KL_CTX, 'KL_LOC_Parse_X_1024', car(car(KL_ARG_V990_1022))), (tco_apply(shen_pair, [car(tco_apply(shen_pair, [cdr(car(KL_ARG_V990_1022)), tco_apply(shen_hdtl, [KL_ARG_V990_1022])])), KL_CTX.KL_LOC_Parse_X_1024]) if shen_eq(KL_CTX.KL_LOC_Parse_X_1024, symdic.symdic_kl_x59) else tco_apply(kl_fail, []))][(-1)] if shen_consp(car(KL_ARG_V990_1022)) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_1023, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_1023)][(-1)]
shen_add_fun('shen.<end*>', shen_x60endx42x62, 1)

@tail_recursion
def kl_cut(*FUN_ARGS):
    FUN_ARITY = 3
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_cut, (FUN_ARGS + lambdaargs)))
    KL_ARG_V991_1025 = FUN_ARGS[0]
    KL_ARG_V992_1026 = FUN_ARGS[1]
    KL_ARG_V993_1027 = FUN_ARGS[2]

    class KL_Context:
        KL_LOC_Result_1028 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_1028', tco_apply(kl_thaw, [KL_ARG_V993_1027])), (KL_ARG_V991_1025 if shen_eq(KL_CTX.KL_LOC_Result_1028, False) else KL_CTX.KL_LOC_Result_1028)][(-1)]
shen_add_fun('cut', kl_cut, 3)

@tail_recursion
def shen_insert_modes(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_insert_modes, (FUN_ARGS + lambdaargs)))
    KL_ARG_V994_1029 = FUN_ARGS[0]
    global symdic
    return (KL_ARG_V994_1029 if ((((shen_eq(nil, cdr(cdr(cdr(KL_ARG_V994_1029)))) if shen_consp(cdr(cdr(KL_ARG_V994_1029))) else False) if shen_consp(cdr(KL_ARG_V994_1029)) else False) if shen_eq(symdic.symdic_kl_mode, car(KL_ARG_V994_1029)) else False) if shen_consp(KL_ARG_V994_1029) else False) else (nil if shen_eq(nil, KL_ARG_V994_1029) else (Cons(Cons(symdic.symdic_kl_mode, Cons(car(KL_ARG_V994_1029), Cons(symdic.symdic_kl_x43, nil))), Cons(symdic.symdic_kl_mode, Cons(tco_apply(shen_insert_modes, [cdr(KL_ARG_V994_1029)]), Cons(symdic.symdic_kl_x45, nil)))) if shen_consp(KL_ARG_V994_1029) else (KL_ARG_V994_1029 if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.insert_modes', shen_insert_modes, 1)

@tail_recursion
def shen_sx45prolog(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_sx45prolog, (FUN_ARGS + lambdaargs)))
    KL_ARG_V995_1030 = FUN_ARGS[0]
    global symdic
    return tail_call(kl_map, [(lambda KL_ARG_V921_1031: tail_call(kl_eval, [KL_ARG_V921_1031])), tco_apply(shen_prologx45x62shen, [KL_ARG_V995_1030])])
shen_add_fun('shen.s-prolog', shen_sx45prolog, 1)

@tail_recursion
def shen_prologx45x62shen(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_prologx45x62shen, (FUN_ARGS + lambdaargs)))
    KL_ARG_V996_1032 = FUN_ARGS[0]
    global symdic
    return tail_call(kl_map, [symdic.symdic_shen_compile_prolog_procedure, tco_apply(shen_group_clauses, [tco_apply(kl_map, [symdic.symdic_shen_sx45prolog_clause, tco_apply(kl_mapcan, [symdic.symdic_shen_head_abstraction, KL_ARG_V996_1032])])])])
shen_add_fun('shen.prolog->shen', shen_prologx45x62shen, 1)

@tail_recursion
def shen_sx45prolog_clause(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_sx45prolog_clause, (FUN_ARGS + lambdaargs)))
    KL_ARG_V997_1033 = FUN_ARGS[0]
    global symdic
    return (Cons(car(KL_ARG_V997_1033), Cons(symdic.symdic_kl_x58x45, Cons(tco_apply(kl_map, [symdic.symdic_shen_sx45prolog_literal, car(cdr(cdr(KL_ARG_V997_1033)))]), nil))) if ((((shen_eq(nil, cdr(cdr(cdr(KL_ARG_V997_1033)))) if shen_consp(cdr(cdr(KL_ARG_V997_1033))) else False) if shen_eq(symdic.symdic_kl_x58x45, car(cdr(KL_ARG_V997_1033))) else False) if shen_consp(cdr(KL_ARG_V997_1033)) else False) if shen_consp(KL_ARG_V997_1033) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_sx45prolog_clause]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.s-prolog_clause', shen_sx45prolog_clause, 1)

@tail_recursion
def shen_head_abstraction(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_head_abstraction, (FUN_ARGS + lambdaargs)))
    KL_ARG_V998_1034 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Terms_1035 = None
        KL_LOC_XTerms_1037 = None
        KL_LOC_Literal_1038 = None
        KL_LOC_Clause_1039 = None
    KL_CTX = KL_Context()
    global symdic
    return (Cons(KL_ARG_V998_1034, nil) if ((((((tco_apply(shen_complexity_head, [car(KL_ARG_V998_1034)]) < shen_get(symdic.symdic_shen_x42maxcomplexityx42)) if shen_eq(nil, cdr(cdr(cdr(KL_ARG_V998_1034)))) else False) if shen_consp(cdr(cdr(KL_ARG_V998_1034))) else False) if shen_eq(symdic.symdic_kl_x58x45, car(cdr(KL_ARG_V998_1034))) else False) if shen_consp(cdr(KL_ARG_V998_1034)) else False) if shen_consp(KL_ARG_V998_1034) else False) else ([setattr(KL_CTX, 'KL_LOC_Terms_1035', tco_apply(kl_map, [(lambda KL_ARG_Y_1036: tail_call(kl_gensym, [symdic.symdic_V])), cdr(car(KL_ARG_V998_1034))])), [setattr(KL_CTX, 'KL_LOC_XTerms_1037', tco_apply(shen_rcons_form, [tco_apply(shen_remove_modes, [cdr(car(KL_ARG_V998_1034))])])), [setattr(KL_CTX, 'KL_LOC_Literal_1038', Cons(symdic.symdic_kl_unify, Cons(tco_apply(shen_cons_form, [KL_CTX.KL_LOC_Terms_1035]), Cons(KL_CTX.KL_LOC_XTerms_1037, nil)))), [setattr(KL_CTX, 'KL_LOC_Clause_1039', Cons(Cons(car(car(KL_ARG_V998_1034)), KL_CTX.KL_LOC_Terms_1035), Cons(symdic.symdic_kl_x58x45, Cons(Cons(KL_CTX.KL_LOC_Literal_1038, car(cdr(cdr(KL_ARG_V998_1034)))), nil)))), Cons(KL_CTX.KL_LOC_Clause_1039, nil)][(-1)]][(-1)]][(-1)]][(-1)] if (((((shen_eq(nil, cdr(cdr(cdr(KL_ARG_V998_1034)))) if shen_consp(cdr(cdr(KL_ARG_V998_1034))) else False) if shen_eq(symdic.symdic_kl_x58x45, car(cdr(KL_ARG_V998_1034))) else False) if shen_consp(cdr(KL_ARG_V998_1034)) else False) if shen_consp(car(KL_ARG_V998_1034)) else False) if shen_consp(KL_ARG_V998_1034) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_head_abstraction]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.head_abstraction', shen_head_abstraction, 1)

@tail_recursion
def shen_complexity_head(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_complexity_head, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1003_1040 = FUN_ARGS[0]
    global symdic
    return (tail_call(shen_product, [tco_apply(kl_map, [symdic.symdic_shen_complexity, cdr(KL_ARG_V1003_1040)])]) if shen_consp(KL_ARG_V1003_1040) else (tail_call(shen_sysx45error, [symdic.symdic_shen_complexity_head]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.complexity_head', shen_complexity_head, 1)

@tail_recursion
def shen_complexity(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_complexity, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1011_1041 = FUN_ARGS[0]
    global symdic
    return (tail_call(shen_complexity, [car(cdr(KL_ARG_V1011_1041))]) if (((((((((shen_eq(nil, cdr(cdr(cdr(KL_ARG_V1011_1041)))) if shen_consp(cdr(cdr(KL_ARG_V1011_1041))) else False) if shen_eq(nil, cdr(cdr(cdr(car(cdr(KL_ARG_V1011_1041)))))) else False) if shen_consp(cdr(cdr(car(cdr(KL_ARG_V1011_1041))))) else False) if shen_consp(cdr(car(cdr(KL_ARG_V1011_1041)))) else False) if shen_eq(symdic.symdic_kl_mode, car(car(cdr(KL_ARG_V1011_1041)))) else False) if shen_consp(car(cdr(KL_ARG_V1011_1041))) else False) if shen_consp(cdr(KL_ARG_V1011_1041)) else False) if shen_eq(symdic.symdic_kl_mode, car(KL_ARG_V1011_1041)) else False) if shen_consp(KL_ARG_V1011_1041) else False) else ((2 * (tco_apply(shen_complexity, [Cons(symdic.symdic_kl_mode, Cons(car(car(cdr(KL_ARG_V1011_1041))), cdr(cdr(KL_ARG_V1011_1041))))]) * tco_apply(shen_complexity, [Cons(symdic.symdic_kl_mode, Cons(cdr(car(cdr(KL_ARG_V1011_1041))), cdr(cdr(KL_ARG_V1011_1041))))]))) if ((((((shen_eq(nil, cdr(cdr(cdr(KL_ARG_V1011_1041)))) if shen_eq(symdic.symdic_kl_x43, car(cdr(cdr(KL_ARG_V1011_1041)))) else False) if shen_consp(cdr(cdr(KL_ARG_V1011_1041))) else False) if shen_consp(car(cdr(KL_ARG_V1011_1041))) else False) if shen_consp(cdr(KL_ARG_V1011_1041)) else False) if shen_eq(symdic.symdic_kl_mode, car(KL_ARG_V1011_1041)) else False) if shen_consp(KL_ARG_V1011_1041) else False) else ((tco_apply(shen_complexity, [Cons(symdic.symdic_kl_mode, Cons(car(car(cdr(KL_ARG_V1011_1041))), cdr(cdr(KL_ARG_V1011_1041))))]) * tco_apply(shen_complexity, [Cons(symdic.symdic_kl_mode, Cons(cdr(car(cdr(KL_ARG_V1011_1041))), cdr(cdr(KL_ARG_V1011_1041))))])) if ((((((shen_eq(nil, cdr(cdr(cdr(KL_ARG_V1011_1041)))) if shen_eq(symdic.symdic_kl_x45, car(cdr(cdr(KL_ARG_V1011_1041)))) else False) if shen_consp(cdr(cdr(KL_ARG_V1011_1041))) else False) if shen_consp(car(cdr(KL_ARG_V1011_1041))) else False) if shen_consp(cdr(KL_ARG_V1011_1041)) else False) if shen_eq(symdic.symdic_kl_mode, car(KL_ARG_V1011_1041)) else False) if shen_consp(KL_ARG_V1011_1041) else False) else (1 if (((((tco_apply(kl_variablex63, [car(cdr(KL_ARG_V1011_1041))]) if shen_eq(nil, cdr(cdr(cdr(KL_ARG_V1011_1041)))) else False) if shen_consp(cdr(cdr(KL_ARG_V1011_1041))) else False) if shen_consp(cdr(KL_ARG_V1011_1041)) else False) if shen_eq(symdic.symdic_kl_mode, car(KL_ARG_V1011_1041)) else False) if shen_consp(KL_ARG_V1011_1041) else False) else (2 if (((((shen_eq(nil, cdr(cdr(cdr(KL_ARG_V1011_1041)))) if shen_eq(symdic.symdic_kl_x43, car(cdr(cdr(KL_ARG_V1011_1041)))) else False) if shen_consp(cdr(cdr(KL_ARG_V1011_1041))) else False) if shen_consp(cdr(KL_ARG_V1011_1041)) else False) if shen_eq(symdic.symdic_kl_mode, car(KL_ARG_V1011_1041)) else False) if shen_consp(KL_ARG_V1011_1041) else False) else (1 if (((((shen_eq(nil, cdr(cdr(cdr(KL_ARG_V1011_1041)))) if shen_eq(symdic.symdic_kl_x45, car(cdr(cdr(KL_ARG_V1011_1041)))) else False) if shen_consp(cdr(cdr(KL_ARG_V1011_1041))) else False) if shen_consp(cdr(KL_ARG_V1011_1041)) else False) if shen_eq(symdic.symdic_kl_mode, car(KL_ARG_V1011_1041)) else False) if shen_consp(KL_ARG_V1011_1041) else False) else (tail_call(shen_complexity, [Cons(symdic.symdic_kl_mode, Cons(KL_ARG_V1011_1041, Cons(symdic.symdic_kl_x43, nil)))]) if True else shen_simple_error('condition failure'))))))))
shen_add_fun('shen.complexity', shen_complexity, 1)

@tail_recursion
def shen_product(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_product, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1012_1042 = FUN_ARGS[0]
    global symdic
    return (1 if shen_eq(nil, KL_ARG_V1012_1042) else ((car(KL_ARG_V1012_1042) * tco_apply(shen_product, [cdr(KL_ARG_V1012_1042)])) if shen_consp(KL_ARG_V1012_1042) else (tail_call(shen_sysx45error, [symdic.symdic_shen_product]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.product', shen_product, 1)

@tail_recursion
def shen_sx45prolog_literal(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_sx45prolog_literal, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1013_1043 = FUN_ARGS[0]
    global symdic
    return (Cons(symdic.symdic_kl_bind, Cons(car(cdr(KL_ARG_V1013_1043)), Cons(tco_apply(shen_insert_deref, [car(cdr(cdr(KL_ARG_V1013_1043)))]), nil))) if ((((shen_eq(nil, cdr(cdr(cdr(KL_ARG_V1013_1043)))) if shen_consp(cdr(cdr(KL_ARG_V1013_1043))) else False) if shen_consp(cdr(KL_ARG_V1013_1043)) else False) if shen_eq(symdic.symdic_kl_is, car(KL_ARG_V1013_1043)) else False) if shen_consp(KL_ARG_V1013_1043) else False) else (Cons(symdic.symdic_kl_fwhen, Cons(tco_apply(shen_insert_deref, [car(cdr(KL_ARG_V1013_1043))]), nil)) if (((shen_eq(nil, cdr(cdr(KL_ARG_V1013_1043))) if shen_consp(cdr(KL_ARG_V1013_1043)) else False) if shen_eq(symdic.symdic_kl_when, car(KL_ARG_V1013_1043)) else False) if shen_consp(KL_ARG_V1013_1043) else False) else (Cons(symdic.symdic_kl_bind, Cons(car(cdr(KL_ARG_V1013_1043)), Cons(tco_apply(shen_insert_lazyderef, [car(cdr(cdr(KL_ARG_V1013_1043)))]), nil))) if ((((shen_eq(nil, cdr(cdr(cdr(KL_ARG_V1013_1043)))) if shen_consp(cdr(cdr(KL_ARG_V1013_1043))) else False) if shen_consp(cdr(KL_ARG_V1013_1043)) else False) if shen_eq(symdic.symdic_kl_bind, car(KL_ARG_V1013_1043)) else False) if shen_consp(KL_ARG_V1013_1043) else False) else (Cons(symdic.symdic_kl_fwhen, Cons(tco_apply(shen_insert_lazyderef, [car(cdr(KL_ARG_V1013_1043))]), nil)) if (((shen_eq(nil, cdr(cdr(KL_ARG_V1013_1043))) if shen_consp(cdr(KL_ARG_V1013_1043)) else False) if shen_eq(symdic.symdic_kl_fwhen, car(KL_ARG_V1013_1043)) else False) if shen_consp(KL_ARG_V1013_1043) else False) else (Cons(tco_apply(shen_m_prolog_to_sx45prolog_predicate, [car(KL_ARG_V1013_1043)]), cdr(KL_ARG_V1013_1043)) if shen_consp(KL_ARG_V1013_1043) else (tail_call(shen_sysx45error, [symdic.symdic_shen_sx45prolog_literal]) if True else shen_simple_error('condition failure')))))))
shen_add_fun('shen.s-prolog_literal', shen_sx45prolog_literal, 1)

@tail_recursion
def shen_insert_deref(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_insert_deref, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1014_1044 = FUN_ARGS[0]
    global symdic
    return (Cons(symdic.symdic_shen_deref, Cons(KL_ARG_V1014_1044, Cons(symdic.symdic_ProcessN, nil))) if tco_apply(kl_variablex63, [KL_ARG_V1014_1044]) else (Cons(tco_apply(shen_insert_deref, [car(KL_ARG_V1014_1044)]), tco_apply(shen_insert_deref, [cdr(KL_ARG_V1014_1044)])) if shen_consp(KL_ARG_V1014_1044) else (KL_ARG_V1014_1044 if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.insert_deref', shen_insert_deref, 1)

@tail_recursion
def shen_insert_lazyderef(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_insert_lazyderef, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1015_1045 = FUN_ARGS[0]
    global symdic
    return (Cons(symdic.symdic_shen_lazyderef, Cons(KL_ARG_V1015_1045, Cons(symdic.symdic_ProcessN, nil))) if tco_apply(kl_variablex63, [KL_ARG_V1015_1045]) else (Cons(tco_apply(shen_insert_lazyderef, [car(KL_ARG_V1015_1045)]), tco_apply(shen_insert_lazyderef, [cdr(KL_ARG_V1015_1045)])) if shen_consp(KL_ARG_V1015_1045) else (KL_ARG_V1015_1045 if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.insert_lazyderef', shen_insert_lazyderef, 1)

@tail_recursion
def shen_m_prolog_to_sx45prolog_predicate(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_m_prolog_to_sx45prolog_predicate, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1016_1046 = FUN_ARGS[0]
    global symdic
    return (symdic.symdic_kl_unify if shen_eq(symdic.symdic_kl_x61, KL_ARG_V1016_1046) else (symdic.symdic_kl_unifyx33 if shen_eq(symdic.symdic_kl_x61x33, KL_ARG_V1016_1046) else (symdic.symdic_kl_identical if shen_eq(symdic.symdic_kl_x61x61, KL_ARG_V1016_1046) else (KL_ARG_V1016_1046 if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.m_prolog_to_s-prolog_predicate', shen_m_prolog_to_sx45prolog_predicate, 1)

@tail_recursion
def shen_group_clauses(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_group_clauses, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1017_1047 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Group_1048 = None
        KL_LOC_Rest_1050 = None
    KL_CTX = KL_Context()
    global symdic
    return (nil if shen_eq(nil, KL_ARG_V1017_1047) else ([setattr(KL_CTX, 'KL_LOC_Group_1048', tco_apply(shen_collect, [(lambda KL_ARG_X_1049: tail_call(shen_same_predicatex63, [car(KL_ARG_V1017_1047), KL_ARG_X_1049])), KL_ARG_V1017_1047])), [setattr(KL_CTX, 'KL_LOC_Rest_1050', tco_apply(kl_difference, [KL_ARG_V1017_1047, KL_CTX.KL_LOC_Group_1048])), Cons(KL_CTX.KL_LOC_Group_1048, tco_apply(shen_group_clauses, [KL_CTX.KL_LOC_Rest_1050]))][(-1)]][(-1)] if shen_consp(KL_ARG_V1017_1047) else (tail_call(shen_sysx45error, [symdic.symdic_shen_group_clauses]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.group_clauses', shen_group_clauses, 1)

@tail_recursion
def shen_collect(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_collect, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1020_1051 = FUN_ARGS[0]
    KL_ARG_V1021_1052 = FUN_ARGS[1]
    global symdic
    return (nil if shen_eq(nil, KL_ARG_V1021_1052) else ((Cons(car(KL_ARG_V1021_1052), tco_apply(shen_collect, [KL_ARG_V1020_1051, cdr(KL_ARG_V1021_1052)])) if shen_apply(KL_ARG_V1020_1051, [car(KL_ARG_V1021_1052)]) else tail_call(shen_collect, [KL_ARG_V1020_1051, cdr(KL_ARG_V1021_1052)])) if shen_consp(KL_ARG_V1021_1052) else (tail_call(shen_sysx45error, [symdic.symdic_shen_collect]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.collect', shen_collect, 2)

@tail_recursion
def shen_same_predicatex63(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_same_predicatex63, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1038_1053 = FUN_ARGS[0]
    KL_ARG_V1039_1054 = FUN_ARGS[1]
    global symdic
    return (shen_eq(car(car(KL_ARG_V1038_1053)), car(car(KL_ARG_V1039_1054))) if (((shen_consp(car(KL_ARG_V1039_1054)) if shen_consp(KL_ARG_V1039_1054) else False) if shen_consp(car(KL_ARG_V1038_1053)) else False) if shen_consp(KL_ARG_V1038_1053) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_same_predicatex63]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.same_predicate?', shen_same_predicatex63, 2)

@tail_recursion
def shen_compile_prolog_procedure(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_compile_prolog_procedure, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1040_1055 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_F_1056 = None
        KL_LOC_Shen_1057 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_F_1056', tco_apply(shen_procedure_name, [KL_ARG_V1040_1055])), [setattr(KL_CTX, 'KL_LOC_Shen_1057', tco_apply(shen_clausesx45tox45shen, [KL_CTX.KL_LOC_F_1056, KL_ARG_V1040_1055])), KL_CTX.KL_LOC_Shen_1057][(-1)]][(-1)]
shen_add_fun('shen.compile_prolog_procedure', shen_compile_prolog_procedure, 1)

@tail_recursion
def shen_procedure_name(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_procedure_name, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1053_1058 = FUN_ARGS[0]
    global symdic
    return (car(car(car(KL_ARG_V1053_1058))) if ((shen_consp(car(car(KL_ARG_V1053_1058))) if shen_consp(car(KL_ARG_V1053_1058)) else False) if shen_consp(KL_ARG_V1053_1058) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_procedure_name]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.procedure_name', shen_procedure_name, 1)

@tail_recursion
def shen_clausesx45tox45shen(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_clausesx45tox45shen, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1054_1059 = FUN_ARGS[0]
    KL_ARG_V1055_1060 = FUN_ARGS[1]

    class KL_Context:
        KL_LOC_Linear_1061 = None
        KL_LOC_Arity_1062 = None
        KL_LOC_Parameters_1064 = None
        KL_LOC_AUM_instructions_1065 = None
        KL_LOC_Code_1067 = None
        KL_LOC_ShenDef_1068 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Linear_1061', tco_apply(kl_map, [symdic.symdic_shen_linearisex45clause, KL_ARG_V1055_1060])), [setattr(KL_CTX, 'KL_LOC_Arity_1062', tco_apply(shen_prologx45aritycheck, [KL_ARG_V1054_1059, tco_apply(kl_map, [(lambda KL_ARG_V922_1063: tail_call(kl_head, [KL_ARG_V922_1063])), KL_ARG_V1055_1060])])), [setattr(KL_CTX, 'KL_LOC_Parameters_1064', tco_apply(shen_parameters, [KL_CTX.KL_LOC_Arity_1062])), [setattr(KL_CTX, 'KL_LOC_AUM_instructions_1065', tco_apply(kl_map, [(lambda KL_ARG_X_1066: tail_call(shen_aum, [KL_ARG_X_1066, KL_CTX.KL_LOC_Parameters_1064])), KL_CTX.KL_LOC_Linear_1061])), [setattr(KL_CTX, 'KL_LOC_Code_1067', tco_apply(shen_catchx45cut, [tco_apply(shen_nestx45disjunct, [tco_apply(kl_map, [symdic.symdic_shen_aum_to_shen, KL_CTX.KL_LOC_AUM_instructions_1065])])])), [setattr(KL_CTX, 'KL_LOC_ShenDef_1068', Cons(symdic.symdic_kl_define, Cons(KL_ARG_V1054_1059, tco_apply(kl_append, [KL_CTX.KL_LOC_Parameters_1064, tco_apply(kl_append, [Cons(symdic.symdic_ProcessN, Cons(symdic.symdic_Continuation, nil)), Cons(symdic.symdic_kl_x45x62, Cons(KL_CTX.KL_LOC_Code_1067, nil))])])))), KL_CTX.KL_LOC_ShenDef_1068][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]
shen_add_fun('shen.clauses-to-shen', shen_clausesx45tox45shen, 2)

@tail_recursion
def shen_catchx45cut(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_catchx45cut, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1056_1069 = FUN_ARGS[0]
    global symdic
    return (KL_ARG_V1056_1069 if (not tco_apply(shen_occursx63, [symdic.symdic_kl_cut, KL_ARG_V1056_1069])) else (Cons(symdic.symdic_kl_let, Cons(symdic.symdic_Throwcontrol, Cons(Cons(symdic.symdic_shen_catchpoint, nil), Cons(Cons(symdic.symdic_shen_cutpoint, Cons(symdic.symdic_Throwcontrol, Cons(KL_ARG_V1056_1069, nil))), nil)))) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.catch-cut', shen_catchx45cut, 1)

@tail_recursion
def shen_catchpoint(*FUN_ARGS):
    FUN_ARITY = 0
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_catchpoint, (FUN_ARGS + lambdaargs)))
    global symdic
    return shen_set(symdic.symdic_shen_x42catchx42, (1 + shen_get(symdic.symdic_shen_x42catchx42)))
shen_add_fun('shen.catchpoint', shen_catchpoint, 0)

@tail_recursion
def shen_cutpoint(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_cutpoint, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1061_1070 = FUN_ARGS[0]
    KL_ARG_V1062_1071 = FUN_ARGS[1]
    global symdic
    return (False if shen_eq(KL_ARG_V1062_1071, KL_ARG_V1061_1070) else (KL_ARG_V1062_1071 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.cutpoint', shen_cutpoint, 2)

@tail_recursion
def shen_nestx45disjunct(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_nestx45disjunct, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1064_1072 = FUN_ARGS[0]
    global symdic
    return (car(KL_ARG_V1064_1072) if (shen_eq(nil, cdr(KL_ARG_V1064_1072)) if shen_consp(KL_ARG_V1064_1072) else False) else (tail_call(shen_lispx45or, [car(KL_ARG_V1064_1072), tco_apply(shen_nestx45disjunct, [cdr(KL_ARG_V1064_1072)])]) if shen_consp(KL_ARG_V1064_1072) else (tail_call(shen_sysx45error, [symdic.symdic_shen_nestx45disjunct]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.nest-disjunct', shen_nestx45disjunct, 1)

@tail_recursion
def shen_lispx45or(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_lispx45or, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1065_1073 = FUN_ARGS[0]
    KL_ARG_V1066_1074 = FUN_ARGS[1]
    global symdic
    return Cons(symdic.symdic_kl_let, Cons(symdic.symdic_Case, Cons(KL_ARG_V1065_1073, Cons(Cons(symdic.symdic_kl_if, Cons(Cons(symdic.symdic_kl_x61, Cons(symdic.symdic_Case, Cons(False, nil))), Cons(KL_ARG_V1066_1074, Cons(symdic.symdic_Case, nil)))), nil))))
shen_add_fun('shen.lisp-or', shen_lispx45or, 2)

@tail_recursion
def shen_prologx45aritycheck(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_prologx45aritycheck, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1069_1075 = FUN_ARGS[0]
    KL_ARG_V1070_1076 = FUN_ARGS[1]
    global symdic
    return ((tco_apply(kl_length, [car(KL_ARG_V1070_1076)]) - 1) if (shen_eq(nil, cdr(KL_ARG_V1070_1076)) if shen_consp(KL_ARG_V1070_1076) else False) else ((tail_call(shen_prologx45aritycheck, [KL_ARG_V1069_1075, cdr(KL_ARG_V1070_1076)]) if shen_eq(tco_apply(kl_length, [car(KL_ARG_V1070_1076)]), tco_apply(kl_length, [car(cdr(KL_ARG_V1070_1076))])) else shen_simple_error(('arity error in prolog procedure ' + tco_apply(shen_app, [Cons(KL_ARG_V1069_1075, nil), '\r\n', symdic.symdic_shen_a])))) if (shen_consp(cdr(KL_ARG_V1070_1076)) if shen_consp(KL_ARG_V1070_1076) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_prologx45aritycheck]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.prolog-aritycheck', shen_prologx45aritycheck, 2)

@tail_recursion
def shen_linearisex45clause(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_linearisex45clause, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1071_1077 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Linear_1078 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_Linear_1078', tco_apply(shen_linearise, [Cons(car(KL_ARG_V1071_1077), cdr(cdr(KL_ARG_V1071_1077)))])), tail_call(shen_clause_form, [KL_CTX.KL_LOC_Linear_1078])][(-1)] if ((((shen_eq(nil, cdr(cdr(cdr(KL_ARG_V1071_1077)))) if shen_consp(cdr(cdr(KL_ARG_V1071_1077))) else False) if shen_eq(symdic.symdic_kl_x58x45, car(cdr(KL_ARG_V1071_1077))) else False) if shen_consp(cdr(KL_ARG_V1071_1077)) else False) if shen_consp(KL_ARG_V1071_1077) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_linearisex45clause]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.linearise-clause', shen_linearisex45clause, 1)

@tail_recursion
def shen_clause_form(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_clause_form, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1072_1079 = FUN_ARGS[0]
    global symdic
    return (Cons(tco_apply(shen_explicit_modes, [car(KL_ARG_V1072_1079)]), Cons(symdic.symdic_kl_x58x45, Cons(tco_apply(shen_cf_help, [car(cdr(KL_ARG_V1072_1079))]), nil))) if ((shen_eq(nil, cdr(cdr(KL_ARG_V1072_1079))) if shen_consp(cdr(KL_ARG_V1072_1079)) else False) if shen_consp(KL_ARG_V1072_1079) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_clause_form]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.clause_form', shen_clause_form, 1)

@tail_recursion
def shen_explicit_modes(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_explicit_modes, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1073_1080 = FUN_ARGS[0]
    global symdic
    return (Cons(car(KL_ARG_V1073_1080), tco_apply(kl_map, [symdic.symdic_shen_em_help, cdr(KL_ARG_V1073_1080)])) if shen_consp(KL_ARG_V1073_1080) else (tail_call(shen_sysx45error, [symdic.symdic_shen_explicit_modes]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.explicit_modes', shen_explicit_modes, 1)

@tail_recursion
def shen_em_help(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_em_help, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1074_1081 = FUN_ARGS[0]
    global symdic
    return (KL_ARG_V1074_1081 if ((((shen_eq(nil, cdr(cdr(cdr(KL_ARG_V1074_1081)))) if shen_consp(cdr(cdr(KL_ARG_V1074_1081))) else False) if shen_consp(cdr(KL_ARG_V1074_1081)) else False) if shen_eq(symdic.symdic_kl_mode, car(KL_ARG_V1074_1081)) else False) if shen_consp(KL_ARG_V1074_1081) else False) else (Cons(symdic.symdic_kl_mode, Cons(KL_ARG_V1074_1081, Cons(symdic.symdic_kl_x43, nil))) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.em_help', shen_em_help, 1)

@tail_recursion
def shen_cf_help(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_cf_help, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1075_1082 = FUN_ARGS[0]
    global symdic
    return (Cons(Cons((symdic.symdic_kl_unifyx33 if shen_get(symdic.symdic_shen_x42occursx42) else symdic.symdic_kl_unify), cdr(car(cdr(KL_ARG_V1075_1082)))), tco_apply(shen_cf_help, [car(cdr(cdr(KL_ARG_V1075_1082)))])) if (((((((((shen_eq(nil, cdr(cdr(cdr(KL_ARG_V1075_1082)))) if shen_consp(cdr(cdr(KL_ARG_V1075_1082))) else False) if shen_eq(nil, cdr(cdr(cdr(car(cdr(KL_ARG_V1075_1082)))))) else False) if shen_consp(cdr(cdr(car(cdr(KL_ARG_V1075_1082))))) else False) if shen_consp(cdr(car(cdr(KL_ARG_V1075_1082)))) else False) if shen_eq(symdic.symdic_kl_x61, car(car(cdr(KL_ARG_V1075_1082)))) else False) if shen_consp(car(cdr(KL_ARG_V1075_1082))) else False) if shen_consp(cdr(KL_ARG_V1075_1082)) else False) if shen_eq(symdic.symdic_kl_where, car(KL_ARG_V1075_1082)) else False) if shen_consp(KL_ARG_V1075_1082) else False) else (KL_ARG_V1075_1082 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.cf_help', shen_cf_help, 1)

@tail_recursion
def kl_occursx45check(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_occursx45check, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1080_1083 = FUN_ARGS[0]
    global symdic
    return (shen_set(symdic.symdic_shen_x42occursx42, True) if shen_eq(symdic.symdic_kl_x43, KL_ARG_V1080_1083) else (shen_set(symdic.symdic_shen_x42occursx42, False) if shen_eq(symdic.symdic_kl_x45, KL_ARG_V1080_1083) else (shen_simple_error('occurs-check expects + or -\r\n') if True else shen_simple_error('condition failure'))))
shen_add_fun('occurs-check', kl_occursx45check, 1)

@tail_recursion
def shen_aum(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_aum, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1081_1084 = FUN_ARGS[0]
    KL_ARG_V1082_1085 = FUN_ARGS[1]

    class KL_Context:
        KL_LOC_MuApplication_1086 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_MuApplication_1086', tco_apply(shen_make_mu_application, [Cons(symdic.symdic_shen_mu, Cons(cdr(car(KL_ARG_V1081_1084)), Cons(tco_apply(shen_continuation_call, [cdr(car(KL_ARG_V1081_1084)), car(cdr(cdr(KL_ARG_V1081_1084)))]), nil))), KL_ARG_V1082_1085])), tail_call(shen_mu_reduction, [KL_CTX.KL_LOC_MuApplication_1086, symdic.symdic_kl_x43])][(-1)] if (((((shen_eq(nil, cdr(cdr(cdr(KL_ARG_V1081_1084)))) if shen_consp(cdr(cdr(KL_ARG_V1081_1084))) else False) if shen_eq(symdic.symdic_kl_x58x45, car(cdr(KL_ARG_V1081_1084))) else False) if shen_consp(cdr(KL_ARG_V1081_1084)) else False) if shen_consp(car(KL_ARG_V1081_1084)) else False) if shen_consp(KL_ARG_V1081_1084) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_aum]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.aum', shen_aum, 2)

@tail_recursion
def shen_continuation_call(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_continuation_call, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1083_1087 = FUN_ARGS[0]
    KL_ARG_V1084_1088 = FUN_ARGS[1]

    class KL_Context:
        KL_LOC_VTerms_1089 = None
        KL_LOC_VBody_1090 = None
        KL_LOC_Free_1091 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_VTerms_1089', Cons(symdic.symdic_ProcessN, tco_apply(shen_extract_vars, [KL_ARG_V1083_1087]))), [setattr(KL_CTX, 'KL_LOC_VBody_1090', tco_apply(shen_extract_vars, [KL_ARG_V1084_1088])), [setattr(KL_CTX, 'KL_LOC_Free_1091', tco_apply(kl_remove, [symdic.symdic_Throwcontrol, tco_apply(kl_difference, [KL_CTX.KL_LOC_VBody_1090, KL_CTX.KL_LOC_VTerms_1089])])), tail_call(shen_cc_help, [KL_CTX.KL_LOC_Free_1091, KL_ARG_V1084_1088])][(-1)]][(-1)]][(-1)]
shen_add_fun('shen.continuation_call', shen_continuation_call, 2)

@tail_recursion
def kl_remove(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_remove, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1085_1092 = FUN_ARGS[0]
    KL_ARG_V1086_1093 = FUN_ARGS[1]
    global symdic
    return tail_call(shen_removex45h, [KL_ARG_V1085_1092, KL_ARG_V1086_1093, nil])
shen_add_fun('remove', kl_remove, 2)

@tail_recursion
def shen_removex45h(*FUN_ARGS):
    FUN_ARITY = 3
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_removex45h, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1089_1094 = FUN_ARGS[0]
    KL_ARG_V1090_1095 = FUN_ARGS[1]
    KL_ARG_V1091_1096 = FUN_ARGS[2]
    global symdic
    return (tail_call(kl_reverse, [KL_ARG_V1091_1096]) if shen_eq(nil, KL_ARG_V1090_1095) else (tail_call(shen_removex45h, [car(KL_ARG_V1090_1095), cdr(KL_ARG_V1090_1095), KL_ARG_V1091_1096]) if (shen_eq(car(KL_ARG_V1090_1095), KL_ARG_V1089_1094) if shen_consp(KL_ARG_V1090_1095) else False) else (tail_call(shen_removex45h, [KL_ARG_V1089_1094, cdr(KL_ARG_V1090_1095), Cons(car(KL_ARG_V1090_1095), KL_ARG_V1091_1096)]) if shen_consp(KL_ARG_V1090_1095) else (tail_call(shen_sysx45error, [symdic.symdic_shen_removex45h]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.remove-h', shen_removex45h, 3)

@tail_recursion
def shen_cc_help(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_cc_help, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1093_1097 = FUN_ARGS[0]
    KL_ARG_V1094_1098 = FUN_ARGS[1]
    global symdic
    return (Cons(symdic.symdic_shen_pop, Cons(symdic.symdic_shen_the, Cons(symdic.symdic_shen_stack, nil))) if (shen_eq(nil, KL_ARG_V1094_1098) if shen_eq(nil, KL_ARG_V1093_1097) else False) else (Cons(symdic.symdic_shen_rename, Cons(symdic.symdic_shen_the, Cons(symdic.symdic_shen_variables, Cons(symdic.symdic_kl_in, Cons(KL_ARG_V1093_1097, Cons(symdic.symdic_kl_and, Cons(symdic.symdic_shen_then, Cons(Cons(symdic.symdic_shen_pop, Cons(symdic.symdic_shen_the, Cons(symdic.symdic_shen_stack, nil))), nil)))))))) if shen_eq(nil, KL_ARG_V1094_1098) else (Cons(symdic.symdic_kl_call, Cons(symdic.symdic_shen_the, Cons(symdic.symdic_shen_continuation, Cons(KL_ARG_V1094_1098, nil)))) if shen_eq(nil, KL_ARG_V1093_1097) else (Cons(symdic.symdic_shen_rename, Cons(symdic.symdic_shen_the, Cons(symdic.symdic_shen_variables, Cons(symdic.symdic_kl_in, Cons(KL_ARG_V1093_1097, Cons(symdic.symdic_kl_and, Cons(symdic.symdic_shen_then, Cons(Cons(symdic.symdic_kl_call, Cons(symdic.symdic_shen_the, Cons(symdic.symdic_shen_continuation, Cons(KL_ARG_V1094_1098, nil)))), nil)))))))) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.cc_help', shen_cc_help, 2)

@tail_recursion
def shen_make_mu_application(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_make_mu_application, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1095_1099 = FUN_ARGS[0]
    KL_ARG_V1096_1100 = FUN_ARGS[1]
    global symdic
    return (car(cdr(cdr(KL_ARG_V1095_1099))) if ((((((shen_eq(nil, KL_ARG_V1096_1100) if shen_eq(nil, cdr(cdr(cdr(KL_ARG_V1095_1099)))) else False) if shen_consp(cdr(cdr(KL_ARG_V1095_1099))) else False) if shen_eq(nil, car(cdr(KL_ARG_V1095_1099))) else False) if shen_consp(cdr(KL_ARG_V1095_1099)) else False) if shen_eq(symdic.symdic_shen_mu, car(KL_ARG_V1095_1099)) else False) if shen_consp(KL_ARG_V1095_1099) else False) else (Cons(Cons(symdic.symdic_shen_mu, Cons(car(car(cdr(KL_ARG_V1095_1099))), Cons(tco_apply(shen_make_mu_application, [Cons(symdic.symdic_shen_mu, Cons(cdr(car(cdr(KL_ARG_V1095_1099))), cdr(cdr(KL_ARG_V1095_1099)))), cdr(KL_ARG_V1096_1100)]), nil))), Cons(car(KL_ARG_V1096_1100), nil)) if ((((((shen_consp(KL_ARG_V1096_1100) if shen_eq(nil, cdr(cdr(cdr(KL_ARG_V1095_1099)))) else False) if shen_consp(cdr(cdr(KL_ARG_V1095_1099))) else False) if shen_consp(car(cdr(KL_ARG_V1095_1099))) else False) if shen_consp(cdr(KL_ARG_V1095_1099)) else False) if shen_eq(symdic.symdic_shen_mu, car(KL_ARG_V1095_1099)) else False) if shen_consp(KL_ARG_V1095_1099) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_make_mu_application]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.make_mu_application', shen_make_mu_application, 2)

@tail_recursion
def shen_mu_reduction(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_mu_reduction, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1103_1101 = FUN_ARGS[0]
    KL_ARG_V1104_1102 = FUN_ARGS[1]

    class KL_Context:
        KL_LOC_Z_1103 = None
        KL_LOC_Z_1104 = None
        KL_LOC_Z_1105 = None
        KL_LOC_Z_1106 = None
    KL_CTX = KL_Context()
    global symdic
    return (tail_call(shen_mu_reduction, [Cons(Cons(symdic.symdic_shen_mu, Cons(car(cdr(car(cdr(car(KL_ARG_V1103_1101))))), cdr(cdr(car(KL_ARG_V1103_1101))))), cdr(KL_ARG_V1103_1101)), car(cdr(cdr(car(cdr(car(KL_ARG_V1103_1101))))))]) if ((((((((((((shen_eq(nil, cdr(cdr(KL_ARG_V1103_1101))) if shen_consp(cdr(KL_ARG_V1103_1101)) else False) if shen_eq(nil, cdr(cdr(cdr(car(KL_ARG_V1103_1101))))) else False) if shen_consp(cdr(cdr(car(KL_ARG_V1103_1101)))) else False) if shen_eq(nil, cdr(cdr(cdr(car(cdr(car(KL_ARG_V1103_1101))))))) else False) if shen_consp(cdr(cdr(car(cdr(car(KL_ARG_V1103_1101)))))) else False) if shen_consp(cdr(car(cdr(car(KL_ARG_V1103_1101))))) else False) if shen_eq(symdic.symdic_kl_mode, car(car(cdr(car(KL_ARG_V1103_1101))))) else False) if shen_consp(car(cdr(car(KL_ARG_V1103_1101)))) else False) if shen_consp(cdr(car(KL_ARG_V1103_1101))) else False) if shen_eq(symdic.symdic_shen_mu, car(car(KL_ARG_V1103_1101))) else False) if shen_consp(car(KL_ARG_V1103_1101)) else False) if shen_consp(KL_ARG_V1103_1101) else False) else (tail_call(shen_mu_reduction, [car(cdr(cdr(car(KL_ARG_V1103_1101)))), KL_ARG_V1104_1102]) if ((((((((shen_eq(symdic.symdic_kl__, car(cdr(car(KL_ARG_V1103_1101)))) if shen_eq(nil, cdr(cdr(KL_ARG_V1103_1101))) else False) if shen_consp(cdr(KL_ARG_V1103_1101)) else False) if shen_eq(nil, cdr(cdr(cdr(car(KL_ARG_V1103_1101))))) else False) if shen_consp(cdr(cdr(car(KL_ARG_V1103_1101)))) else False) if shen_consp(cdr(car(KL_ARG_V1103_1101))) else False) if shen_eq(symdic.symdic_shen_mu, car(car(KL_ARG_V1103_1101))) else False) if shen_consp(car(KL_ARG_V1103_1101)) else False) if shen_consp(KL_ARG_V1103_1101) else False) else (tail_call(kl_subst, [car(cdr(KL_ARG_V1103_1101)), car(cdr(car(KL_ARG_V1103_1101))), tco_apply(shen_mu_reduction, [car(cdr(cdr(car(KL_ARG_V1103_1101)))), KL_ARG_V1104_1102])]) if ((((((((tco_apply(shen_ephemeral_variablex63, [car(cdr(car(KL_ARG_V1103_1101))), car(cdr(KL_ARG_V1103_1101))]) if shen_eq(nil, cdr(cdr(KL_ARG_V1103_1101))) else False) if shen_consp(cdr(KL_ARG_V1103_1101)) else False) if shen_eq(nil, cdr(cdr(cdr(car(KL_ARG_V1103_1101))))) else False) if shen_consp(cdr(cdr(car(KL_ARG_V1103_1101)))) else False) if shen_consp(cdr(car(KL_ARG_V1103_1101))) else False) if shen_eq(symdic.symdic_shen_mu, car(car(KL_ARG_V1103_1101))) else False) if shen_consp(car(KL_ARG_V1103_1101)) else False) if shen_consp(KL_ARG_V1103_1101) else False) else (Cons(symdic.symdic_kl_let, Cons(car(cdr(car(KL_ARG_V1103_1101))), Cons(symdic.symdic_shen_be, Cons(car(cdr(KL_ARG_V1103_1101)), Cons(symdic.symdic_kl_in, Cons(tco_apply(shen_mu_reduction, [car(cdr(cdr(car(KL_ARG_V1103_1101)))), KL_ARG_V1104_1102]), nil)))))) if ((((((((tco_apply(kl_variablex63, [car(cdr(car(KL_ARG_V1103_1101)))]) if shen_eq(nil, cdr(cdr(KL_ARG_V1103_1101))) else False) if shen_consp(cdr(KL_ARG_V1103_1101)) else False) if shen_eq(nil, cdr(cdr(cdr(car(KL_ARG_V1103_1101))))) else False) if shen_consp(cdr(cdr(car(KL_ARG_V1103_1101)))) else False) if shen_consp(cdr(car(KL_ARG_V1103_1101))) else False) if shen_eq(symdic.symdic_shen_mu, car(car(KL_ARG_V1103_1101))) else False) if shen_consp(car(KL_ARG_V1103_1101)) else False) if shen_consp(KL_ARG_V1103_1101) else False) else ([setattr(KL_CTX, 'KL_LOC_Z_1103', tco_apply(kl_gensym, [symdic.symdic_V])), Cons(symdic.symdic_kl_let, Cons(KL_CTX.KL_LOC_Z_1103, Cons(symdic.symdic_shen_be, Cons(Cons(symdic.symdic_shen_the, Cons(symdic.symdic_shen_result, Cons(symdic.symdic_shen_of, Cons(symdic.symdic_shen_dereferencing, cdr(KL_ARG_V1103_1101))))), Cons(symdic.symdic_kl_in, Cons(Cons(symdic.symdic_kl_if, Cons(Cons(KL_CTX.KL_LOC_Z_1103, Cons(symdic.symdic_kl_is, Cons(symdic.symdic_kl_identical, Cons(symdic.symdic_shen_to, Cons(car(cdr(car(KL_ARG_V1103_1101))), nil))))), Cons(symdic.symdic_shen_then, Cons(tco_apply(shen_mu_reduction, [car(cdr(cdr(car(KL_ARG_V1103_1101)))), symdic.symdic_kl_x45]), Cons(symdic.symdic_shen_else, Cons(symdic.symdic_shen_failedx33, nil)))))), nil))))))][(-1)] if (((((((((tco_apply(shen_prolog_constantx63, [car(cdr(car(KL_ARG_V1103_1101)))]) if shen_eq(symdic.symdic_kl_x45, KL_ARG_V1104_1102) else False) if shen_eq(nil, cdr(cdr(KL_ARG_V1103_1101))) else False) if shen_consp(cdr(KL_ARG_V1103_1101)) else False) if shen_eq(nil, cdr(cdr(cdr(car(KL_ARG_V1103_1101))))) else False) if shen_consp(cdr(cdr(car(KL_ARG_V1103_1101)))) else False) if shen_consp(cdr(car(KL_ARG_V1103_1101))) else False) if shen_eq(symdic.symdic_shen_mu, car(car(KL_ARG_V1103_1101))) else False) if shen_consp(car(KL_ARG_V1103_1101)) else False) if shen_consp(KL_ARG_V1103_1101) else False) else ([setattr(KL_CTX, 'KL_LOC_Z_1104', tco_apply(kl_gensym, [symdic.symdic_V])), Cons(symdic.symdic_kl_let, Cons(KL_CTX.KL_LOC_Z_1104, Cons(symdic.symdic_shen_be, Cons(Cons(symdic.symdic_shen_the, Cons(symdic.symdic_shen_result, Cons(symdic.symdic_shen_of, Cons(symdic.symdic_shen_dereferencing, cdr(KL_ARG_V1103_1101))))), Cons(symdic.symdic_kl_in, Cons(Cons(symdic.symdic_kl_if, Cons(Cons(KL_CTX.KL_LOC_Z_1104, Cons(symdic.symdic_kl_is, Cons(symdic.symdic_kl_identical, Cons(symdic.symdic_shen_to, Cons(car(cdr(car(KL_ARG_V1103_1101))), nil))))), Cons(symdic.symdic_shen_then, Cons(tco_apply(shen_mu_reduction, [car(cdr(cdr(car(KL_ARG_V1103_1101)))), symdic.symdic_kl_x43]), Cons(symdic.symdic_shen_else, Cons(Cons(symdic.symdic_kl_if, Cons(Cons(KL_CTX.KL_LOC_Z_1104, Cons(symdic.symdic_kl_is, Cons(symdic.symdic_shen_a, Cons(symdic.symdic_shen_variable, nil)))), Cons(symdic.symdic_shen_then, Cons(Cons(symdic.symdic_kl_bind, Cons(KL_CTX.KL_LOC_Z_1104, Cons(symdic.symdic_shen_to, Cons(car(cdr(car(KL_ARG_V1103_1101))), Cons(symdic.symdic_kl_in, Cons(tco_apply(shen_mu_reduction, [car(cdr(cdr(car(KL_ARG_V1103_1101)))), symdic.symdic_kl_x43]), nil)))))), Cons(symdic.symdic_shen_else, Cons(symdic.symdic_shen_failedx33, nil)))))), nil)))))), nil))))))][(-1)] if (((((((((tco_apply(shen_prolog_constantx63, [car(cdr(car(KL_ARG_V1103_1101)))]) if shen_eq(symdic.symdic_kl_x43, KL_ARG_V1104_1102) else False) if shen_eq(nil, cdr(cdr(KL_ARG_V1103_1101))) else False) if shen_consp(cdr(KL_ARG_V1103_1101)) else False) if shen_eq(nil, cdr(cdr(cdr(car(KL_ARG_V1103_1101))))) else False) if shen_consp(cdr(cdr(car(KL_ARG_V1103_1101)))) else False) if shen_consp(cdr(car(KL_ARG_V1103_1101))) else False) if shen_eq(symdic.symdic_shen_mu, car(car(KL_ARG_V1103_1101))) else False) if shen_consp(car(KL_ARG_V1103_1101)) else False) if shen_consp(KL_ARG_V1103_1101) else False) else ([setattr(KL_CTX, 'KL_LOC_Z_1105', tco_apply(kl_gensym, [symdic.symdic_V])), Cons(symdic.symdic_kl_let, Cons(KL_CTX.KL_LOC_Z_1105, Cons(symdic.symdic_shen_be, Cons(Cons(symdic.symdic_shen_the, Cons(symdic.symdic_shen_result, Cons(symdic.symdic_shen_of, Cons(symdic.symdic_shen_dereferencing, cdr(KL_ARG_V1103_1101))))), Cons(symdic.symdic_kl_in, Cons(Cons(symdic.symdic_kl_if, Cons(Cons(KL_CTX.KL_LOC_Z_1105, Cons(symdic.symdic_kl_is, Cons(symdic.symdic_shen_a, Cons(symdic.symdic_shen_nonx45empty, Cons(symdic.symdic_kl_list, nil))))), Cons(symdic.symdic_shen_then, Cons(tco_apply(shen_mu_reduction, [Cons(Cons(symdic.symdic_shen_mu, Cons(car(car(cdr(car(KL_ARG_V1103_1101)))), Cons(Cons(Cons(symdic.symdic_shen_mu, Cons(cdr(car(cdr(car(KL_ARG_V1103_1101)))), cdr(cdr(car(KL_ARG_V1103_1101))))), Cons(Cons(symdic.symdic_shen_the, Cons(symdic.symdic_kl_tail, Cons(symdic.symdic_shen_of, Cons(KL_CTX.KL_LOC_Z_1105, nil)))), nil)), nil))), Cons(Cons(symdic.symdic_shen_the, Cons(symdic.symdic_kl_head, Cons(symdic.symdic_shen_of, Cons(KL_CTX.KL_LOC_Z_1105, nil)))), nil)), symdic.symdic_kl_x45]), Cons(symdic.symdic_shen_else, Cons(symdic.symdic_shen_failedx33, nil)))))), nil))))))][(-1)] if (((((((((shen_eq(symdic.symdic_kl_x45, KL_ARG_V1104_1102) if shen_eq(nil, cdr(cdr(KL_ARG_V1103_1101))) else False) if shen_consp(cdr(KL_ARG_V1103_1101)) else False) if shen_eq(nil, cdr(cdr(cdr(car(KL_ARG_V1103_1101))))) else False) if shen_consp(cdr(cdr(car(KL_ARG_V1103_1101)))) else False) if shen_consp(car(cdr(car(KL_ARG_V1103_1101)))) else False) if shen_consp(cdr(car(KL_ARG_V1103_1101))) else False) if shen_eq(symdic.symdic_shen_mu, car(car(KL_ARG_V1103_1101))) else False) if shen_consp(car(KL_ARG_V1103_1101)) else False) if shen_consp(KL_ARG_V1103_1101) else False) else ([setattr(KL_CTX, 'KL_LOC_Z_1106', tco_apply(kl_gensym, [symdic.symdic_V])), Cons(symdic.symdic_kl_let, Cons(KL_CTX.KL_LOC_Z_1106, Cons(symdic.symdic_shen_be, Cons(Cons(symdic.symdic_shen_the, Cons(symdic.symdic_shen_result, Cons(symdic.symdic_shen_of, Cons(symdic.symdic_shen_dereferencing, cdr(KL_ARG_V1103_1101))))), Cons(symdic.symdic_kl_in, Cons(Cons(symdic.symdic_kl_if, Cons(Cons(KL_CTX.KL_LOC_Z_1106, Cons(symdic.symdic_kl_is, Cons(symdic.symdic_shen_a, Cons(symdic.symdic_shen_nonx45empty, Cons(symdic.symdic_kl_list, nil))))), Cons(symdic.symdic_shen_then, Cons(tco_apply(shen_mu_reduction, [Cons(Cons(symdic.symdic_shen_mu, Cons(car(car(cdr(car(KL_ARG_V1103_1101)))), Cons(Cons(Cons(symdic.symdic_shen_mu, Cons(cdr(car(cdr(car(KL_ARG_V1103_1101)))), cdr(cdr(car(KL_ARG_V1103_1101))))), Cons(Cons(symdic.symdic_shen_the, Cons(symdic.symdic_kl_tail, Cons(symdic.symdic_shen_of, Cons(KL_CTX.KL_LOC_Z_1106, nil)))), nil)), nil))), Cons(Cons(symdic.symdic_shen_the, Cons(symdic.symdic_kl_head, Cons(symdic.symdic_shen_of, Cons(KL_CTX.KL_LOC_Z_1106, nil)))), nil)), symdic.symdic_kl_x43]), Cons(symdic.symdic_shen_else, Cons(Cons(symdic.symdic_kl_if, Cons(Cons(KL_CTX.KL_LOC_Z_1106, Cons(symdic.symdic_kl_is, Cons(symdic.symdic_shen_a, Cons(symdic.symdic_shen_variable, nil)))), Cons(symdic.symdic_shen_then, Cons(Cons(symdic.symdic_shen_rename, Cons(symdic.symdic_shen_the, Cons(symdic.symdic_shen_variables, Cons(symdic.symdic_kl_in, Cons(tco_apply(shen_extract_vars, [car(cdr(car(KL_ARG_V1103_1101)))]), Cons(symdic.symdic_kl_and, Cons(symdic.symdic_shen_then, Cons(Cons(symdic.symdic_kl_bind, Cons(KL_CTX.KL_LOC_Z_1106, Cons(symdic.symdic_shen_to, Cons(tco_apply(shen_rcons_form, [tco_apply(shen_remove_modes, [car(cdr(car(KL_ARG_V1103_1101)))])]), Cons(symdic.symdic_kl_in, Cons(tco_apply(shen_mu_reduction, [car(cdr(cdr(car(KL_ARG_V1103_1101)))), symdic.symdic_kl_x43]), nil)))))), nil)))))))), Cons(symdic.symdic_shen_else, Cons(symdic.symdic_shen_failedx33, nil)))))), nil)))))), nil))))))][(-1)] if (((((((((shen_eq(symdic.symdic_kl_x43, KL_ARG_V1104_1102) if shen_eq(nil, cdr(cdr(KL_ARG_V1103_1101))) else False) if shen_consp(cdr(KL_ARG_V1103_1101)) else False) if shen_eq(nil, cdr(cdr(cdr(car(KL_ARG_V1103_1101))))) else False) if shen_consp(cdr(cdr(car(KL_ARG_V1103_1101)))) else False) if shen_consp(car(cdr(car(KL_ARG_V1103_1101)))) else False) if shen_consp(cdr(car(KL_ARG_V1103_1101))) else False) if shen_eq(symdic.symdic_shen_mu, car(car(KL_ARG_V1103_1101))) else False) if shen_consp(car(KL_ARG_V1103_1101)) else False) if shen_consp(KL_ARG_V1103_1101) else False) else (KL_ARG_V1103_1101 if True else shen_simple_error('condition failure'))))))))))
shen_add_fun('shen.mu_reduction', shen_mu_reduction, 2)

@tail_recursion
def shen_rcons_form(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_rcons_form, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1105_1107 = FUN_ARGS[0]
    global symdic
    return (Cons(symdic.symdic_kl_cons, Cons(tco_apply(shen_rcons_form, [car(KL_ARG_V1105_1107)]), Cons(tco_apply(shen_rcons_form, [cdr(KL_ARG_V1105_1107)]), nil))) if shen_consp(KL_ARG_V1105_1107) else (KL_ARG_V1105_1107 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.rcons_form', shen_rcons_form, 1)

@tail_recursion
def shen_remove_modes(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_remove_modes, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1106_1108 = FUN_ARGS[0]
    global symdic
    return (tail_call(shen_remove_modes, [car(cdr(KL_ARG_V1106_1108))]) if (((((shen_eq(nil, cdr(cdr(cdr(KL_ARG_V1106_1108)))) if shen_eq(symdic.symdic_kl_x43, car(cdr(cdr(KL_ARG_V1106_1108)))) else False) if shen_consp(cdr(cdr(KL_ARG_V1106_1108))) else False) if shen_consp(cdr(KL_ARG_V1106_1108)) else False) if shen_eq(symdic.symdic_kl_mode, car(KL_ARG_V1106_1108)) else False) if shen_consp(KL_ARG_V1106_1108) else False) else (tail_call(shen_remove_modes, [car(cdr(KL_ARG_V1106_1108))]) if (((((shen_eq(nil, cdr(cdr(cdr(KL_ARG_V1106_1108)))) if shen_eq(symdic.symdic_kl_x45, car(cdr(cdr(KL_ARG_V1106_1108)))) else False) if shen_consp(cdr(cdr(KL_ARG_V1106_1108))) else False) if shen_consp(cdr(KL_ARG_V1106_1108)) else False) if shen_eq(symdic.symdic_kl_mode, car(KL_ARG_V1106_1108)) else False) if shen_consp(KL_ARG_V1106_1108) else False) else (Cons(tco_apply(shen_remove_modes, [car(KL_ARG_V1106_1108)]), tco_apply(shen_remove_modes, [cdr(KL_ARG_V1106_1108)])) if shen_consp(KL_ARG_V1106_1108) else (KL_ARG_V1106_1108 if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.remove_modes', shen_remove_modes, 1)

@tail_recursion
def shen_ephemeral_variablex63(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_ephemeral_variablex63, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1107_1109 = FUN_ARGS[0]
    KL_ARG_V1108_1110 = FUN_ARGS[1]
    global symdic
    return (tail_call(kl_variablex63, [KL_ARG_V1108_1110]) if tco_apply(kl_variablex63, [KL_ARG_V1107_1109]) else False)
shen_add_fun('shen.ephemeral_variable?', shen_ephemeral_variablex63, 2)

@tail_recursion
def shen_prolog_constantx63(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_prolog_constantx63, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1117_1111 = FUN_ARGS[0]
    global symdic
    return (False if shen_consp(KL_ARG_V1117_1111) else (True if True else shen_simple_error('condition failure')))
shen_add_fun('shen.prolog_constant?', shen_prolog_constantx63, 1)

@tail_recursion
def shen_aum_to_shen(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_aum_to_shen, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1118_1112 = FUN_ARGS[0]
    global symdic
    return (Cons(symdic.symdic_kl_let, Cons(car(cdr(KL_ARG_V1118_1112)), Cons(tco_apply(shen_aum_to_shen, [car(cdr(cdr(cdr(KL_ARG_V1118_1112))))]), Cons(tco_apply(shen_aum_to_shen, [car(cdr(cdr(cdr(cdr(cdr(KL_ARG_V1118_1112))))))]), nil)))) if (((((((((shen_eq(nil, cdr(cdr(cdr(cdr(cdr(cdr(KL_ARG_V1118_1112))))))) if shen_consp(cdr(cdr(cdr(cdr(cdr(KL_ARG_V1118_1112)))))) else False) if shen_eq(symdic.symdic_kl_in, car(cdr(cdr(cdr(cdr(KL_ARG_V1118_1112)))))) else False) if shen_consp(cdr(cdr(cdr(cdr(KL_ARG_V1118_1112))))) else False) if shen_consp(cdr(cdr(cdr(KL_ARG_V1118_1112)))) else False) if shen_eq(symdic.symdic_shen_be, car(cdr(cdr(KL_ARG_V1118_1112)))) else False) if shen_consp(cdr(cdr(KL_ARG_V1118_1112))) else False) if shen_consp(cdr(KL_ARG_V1118_1112)) else False) if shen_eq(symdic.symdic_kl_let, car(KL_ARG_V1118_1112)) else False) if shen_consp(KL_ARG_V1118_1112) else False) else (Cons(symdic.symdic_shen_lazyderef, Cons(tco_apply(shen_aum_to_shen, [car(cdr(cdr(cdr(cdr(KL_ARG_V1118_1112)))))]), Cons(symdic.symdic_ProcessN, nil))) if (((((((((shen_eq(nil, cdr(cdr(cdr(cdr(cdr(KL_ARG_V1118_1112)))))) if shen_consp(cdr(cdr(cdr(cdr(KL_ARG_V1118_1112))))) else False) if shen_eq(symdic.symdic_shen_dereferencing, car(cdr(cdr(cdr(KL_ARG_V1118_1112))))) else False) if shen_consp(cdr(cdr(cdr(KL_ARG_V1118_1112)))) else False) if shen_eq(symdic.symdic_shen_of, car(cdr(cdr(KL_ARG_V1118_1112)))) else False) if shen_consp(cdr(cdr(KL_ARG_V1118_1112))) else False) if shen_eq(symdic.symdic_shen_result, car(cdr(KL_ARG_V1118_1112))) else False) if shen_consp(cdr(KL_ARG_V1118_1112)) else False) if shen_eq(symdic.symdic_shen_the, car(KL_ARG_V1118_1112)) else False) if shen_consp(KL_ARG_V1118_1112) else False) else (Cons(symdic.symdic_kl_if, Cons(tco_apply(shen_aum_to_shen, [car(cdr(KL_ARG_V1118_1112))]), Cons(tco_apply(shen_aum_to_shen, [car(cdr(cdr(cdr(KL_ARG_V1118_1112))))]), Cons(tco_apply(shen_aum_to_shen, [car(cdr(cdr(cdr(cdr(cdr(KL_ARG_V1118_1112))))))]), nil)))) if (((((((((shen_eq(nil, cdr(cdr(cdr(cdr(cdr(cdr(KL_ARG_V1118_1112))))))) if shen_consp(cdr(cdr(cdr(cdr(cdr(KL_ARG_V1118_1112)))))) else False) if shen_eq(symdic.symdic_shen_else, car(cdr(cdr(cdr(cdr(KL_ARG_V1118_1112)))))) else False) if shen_consp(cdr(cdr(cdr(cdr(KL_ARG_V1118_1112))))) else False) if shen_consp(cdr(cdr(cdr(KL_ARG_V1118_1112)))) else False) if shen_eq(symdic.symdic_shen_then, car(cdr(cdr(KL_ARG_V1118_1112)))) else False) if shen_consp(cdr(cdr(KL_ARG_V1118_1112))) else False) if shen_consp(cdr(KL_ARG_V1118_1112)) else False) if shen_eq(symdic.symdic_kl_if, car(KL_ARG_V1118_1112)) else False) if shen_consp(KL_ARG_V1118_1112) else False) else (Cons(symdic.symdic_shen_pvarx63, Cons(car(KL_ARG_V1118_1112), nil)) if (((((((shen_eq(nil, cdr(cdr(cdr(cdr(KL_ARG_V1118_1112))))) if shen_eq(symdic.symdic_shen_variable, car(cdr(cdr(cdr(KL_ARG_V1118_1112))))) else False) if shen_consp(cdr(cdr(cdr(KL_ARG_V1118_1112)))) else False) if shen_eq(symdic.symdic_shen_a, car(cdr(cdr(KL_ARG_V1118_1112)))) else False) if shen_consp(cdr(cdr(KL_ARG_V1118_1112))) else False) if shen_eq(symdic.symdic_kl_is, car(cdr(KL_ARG_V1118_1112))) else False) if shen_consp(cdr(KL_ARG_V1118_1112)) else False) if shen_consp(KL_ARG_V1118_1112) else False) else (Cons(symdic.symdic_kl_consx63, Cons(car(KL_ARG_V1118_1112), nil)) if (((((((((shen_eq(nil, cdr(cdr(cdr(cdr(cdr(KL_ARG_V1118_1112)))))) if shen_eq(symdic.symdic_kl_list, car(cdr(cdr(cdr(cdr(KL_ARG_V1118_1112)))))) else False) if shen_consp(cdr(cdr(cdr(cdr(KL_ARG_V1118_1112))))) else False) if shen_eq(symdic.symdic_shen_nonx45empty, car(cdr(cdr(cdr(KL_ARG_V1118_1112))))) else False) if shen_consp(cdr(cdr(cdr(KL_ARG_V1118_1112)))) else False) if shen_eq(symdic.symdic_shen_a, car(cdr(cdr(KL_ARG_V1118_1112)))) else False) if shen_consp(cdr(cdr(KL_ARG_V1118_1112))) else False) if shen_eq(symdic.symdic_kl_is, car(cdr(KL_ARG_V1118_1112))) else False) if shen_consp(cdr(KL_ARG_V1118_1112)) else False) if shen_consp(KL_ARG_V1118_1112) else False) else (tail_call(shen_aum_to_shen, [car(cdr(cdr(cdr(cdr(cdr(cdr(cdr(KL_ARG_V1118_1112))))))))]) if (((((((((((((((shen_eq(nil, cdr(cdr(cdr(cdr(cdr(cdr(cdr(cdr(KL_ARG_V1118_1112))))))))) if shen_consp(cdr(cdr(cdr(cdr(cdr(cdr(cdr(KL_ARG_V1118_1112)))))))) else False) if shen_eq(symdic.symdic_shen_then, car(cdr(cdr(cdr(cdr(cdr(cdr(KL_ARG_V1118_1112)))))))) else False) if shen_consp(cdr(cdr(cdr(cdr(cdr(cdr(KL_ARG_V1118_1112))))))) else False) if shen_eq(symdic.symdic_kl_and, car(cdr(cdr(cdr(cdr(cdr(KL_ARG_V1118_1112))))))) else False) if shen_consp(cdr(cdr(cdr(cdr(cdr(KL_ARG_V1118_1112)))))) else False) if shen_eq(nil, car(cdr(cdr(cdr(cdr(KL_ARG_V1118_1112)))))) else False) if shen_consp(cdr(cdr(cdr(cdr(KL_ARG_V1118_1112))))) else False) if shen_eq(symdic.symdic_kl_in, car(cdr(cdr(cdr(KL_ARG_V1118_1112))))) else False) if shen_consp(cdr(cdr(cdr(KL_ARG_V1118_1112)))) else False) if shen_eq(symdic.symdic_shen_variables, car(cdr(cdr(KL_ARG_V1118_1112)))) else False) if shen_consp(cdr(cdr(KL_ARG_V1118_1112))) else False) if shen_eq(symdic.symdic_shen_the, car(cdr(KL_ARG_V1118_1112))) else False) if shen_consp(cdr(KL_ARG_V1118_1112)) else False) if shen_eq(symdic.symdic_shen_rename, car(KL_ARG_V1118_1112)) else False) if shen_consp(KL_ARG_V1118_1112) else False) else (Cons(symdic.symdic_kl_let, Cons(car(car(cdr(cdr(cdr(cdr(KL_ARG_V1118_1112)))))), Cons(Cons(symdic.symdic_shen_newpv, Cons(symdic.symdic_ProcessN, nil)), Cons(tco_apply(shen_aum_to_shen, [Cons(symdic.symdic_shen_rename, Cons(symdic.symdic_shen_the, Cons(symdic.symdic_shen_variables, Cons(symdic.symdic_kl_in, Cons(cdr(car(cdr(cdr(cdr(cdr(KL_ARG_V1118_1112)))))), cdr(cdr(cdr(cdr(cdr(KL_ARG_V1118_1112))))))))))]), nil)))) if (((((((((((((((shen_eq(nil, cdr(cdr(cdr(cdr(cdr(cdr(cdr(cdr(KL_ARG_V1118_1112))))))))) if shen_consp(cdr(cdr(cdr(cdr(cdr(cdr(cdr(KL_ARG_V1118_1112)))))))) else False) if shen_eq(symdic.symdic_shen_then, car(cdr(cdr(cdr(cdr(cdr(cdr(KL_ARG_V1118_1112)))))))) else False) if shen_consp(cdr(cdr(cdr(cdr(cdr(cdr(KL_ARG_V1118_1112))))))) else False) if shen_eq(symdic.symdic_kl_and, car(cdr(cdr(cdr(cdr(cdr(KL_ARG_V1118_1112))))))) else False) if shen_consp(cdr(cdr(cdr(cdr(cdr(KL_ARG_V1118_1112)))))) else False) if shen_consp(car(cdr(cdr(cdr(cdr(KL_ARG_V1118_1112)))))) else False) if shen_consp(cdr(cdr(cdr(cdr(KL_ARG_V1118_1112))))) else False) if shen_eq(symdic.symdic_kl_in, car(cdr(cdr(cdr(KL_ARG_V1118_1112))))) else False) if shen_consp(cdr(cdr(cdr(KL_ARG_V1118_1112)))) else False) if shen_eq(symdic.symdic_shen_variables, car(cdr(cdr(KL_ARG_V1118_1112)))) else False) if shen_consp(cdr(cdr(KL_ARG_V1118_1112))) else False) if shen_eq(symdic.symdic_shen_the, car(cdr(KL_ARG_V1118_1112))) else False) if shen_consp(cdr(KL_ARG_V1118_1112)) else False) if shen_eq(symdic.symdic_shen_rename, car(KL_ARG_V1118_1112)) else False) if shen_consp(KL_ARG_V1118_1112) else False) else (Cons(symdic.symdic_kl_do, Cons(Cons(symdic.symdic_shen_bindv, Cons(car(cdr(KL_ARG_V1118_1112)), Cons(tco_apply(shen_chwild, [car(cdr(cdr(cdr(KL_ARG_V1118_1112))))]), Cons(symdic.symdic_ProcessN, nil)))), Cons(Cons(symdic.symdic_kl_let, Cons(symdic.symdic_Result, Cons(tco_apply(shen_aum_to_shen, [car(cdr(cdr(cdr(cdr(cdr(KL_ARG_V1118_1112))))))]), Cons(Cons(symdic.symdic_kl_do, Cons(Cons(symdic.symdic_shen_unbindv, Cons(car(cdr(KL_ARG_V1118_1112)), Cons(symdic.symdic_ProcessN, nil))), Cons(symdic.symdic_Result, nil))), nil)))), nil))) if (((((((((shen_eq(nil, cdr(cdr(cdr(cdr(cdr(cdr(KL_ARG_V1118_1112))))))) if shen_consp(cdr(cdr(cdr(cdr(cdr(KL_ARG_V1118_1112)))))) else False) if shen_eq(symdic.symdic_kl_in, car(cdr(cdr(cdr(cdr(KL_ARG_V1118_1112)))))) else False) if shen_consp(cdr(cdr(cdr(cdr(KL_ARG_V1118_1112))))) else False) if shen_consp(cdr(cdr(cdr(KL_ARG_V1118_1112)))) else False) if shen_eq(symdic.symdic_shen_to, car(cdr(cdr(KL_ARG_V1118_1112)))) else False) if shen_consp(cdr(cdr(KL_ARG_V1118_1112))) else False) if shen_consp(cdr(KL_ARG_V1118_1112)) else False) if shen_eq(symdic.symdic_kl_bind, car(KL_ARG_V1118_1112)) else False) if shen_consp(KL_ARG_V1118_1112) else False) else (Cons(symdic.symdic_kl_x61, Cons(car(cdr(cdr(cdr(cdr(KL_ARG_V1118_1112))))), Cons(car(KL_ARG_V1118_1112), nil))) if ((((((((shen_eq(nil, cdr(cdr(cdr(cdr(cdr(KL_ARG_V1118_1112)))))) if shen_consp(cdr(cdr(cdr(cdr(KL_ARG_V1118_1112))))) else False) if shen_eq(symdic.symdic_shen_to, car(cdr(cdr(cdr(KL_ARG_V1118_1112))))) else False) if shen_consp(cdr(cdr(cdr(KL_ARG_V1118_1112)))) else False) if shen_eq(symdic.symdic_kl_identical, car(cdr(cdr(KL_ARG_V1118_1112)))) else False) if shen_consp(cdr(cdr(KL_ARG_V1118_1112))) else False) if shen_eq(symdic.symdic_kl_is, car(cdr(KL_ARG_V1118_1112))) else False) if shen_consp(cdr(KL_ARG_V1118_1112)) else False) if shen_consp(KL_ARG_V1118_1112) else False) else (False if shen_eq(symdic.symdic_shen_failedx33, KL_ARG_V1118_1112) else (Cons(symdic.symdic_kl_hd, cdr(cdr(cdr(KL_ARG_V1118_1112)))) if (((((((shen_eq(nil, cdr(cdr(cdr(cdr(KL_ARG_V1118_1112))))) if shen_consp(cdr(cdr(cdr(KL_ARG_V1118_1112)))) else False) if shen_eq(symdic.symdic_shen_of, car(cdr(cdr(KL_ARG_V1118_1112)))) else False) if shen_consp(cdr(cdr(KL_ARG_V1118_1112))) else False) if shen_eq(symdic.symdic_kl_head, car(cdr(KL_ARG_V1118_1112))) else False) if shen_consp(cdr(KL_ARG_V1118_1112)) else False) if shen_eq(symdic.symdic_shen_the, car(KL_ARG_V1118_1112)) else False) if shen_consp(KL_ARG_V1118_1112) else False) else (Cons(symdic.symdic_kl_tl, cdr(cdr(cdr(KL_ARG_V1118_1112)))) if (((((((shen_eq(nil, cdr(cdr(cdr(cdr(KL_ARG_V1118_1112))))) if shen_consp(cdr(cdr(cdr(KL_ARG_V1118_1112)))) else False) if shen_eq(symdic.symdic_shen_of, car(cdr(cdr(KL_ARG_V1118_1112)))) else False) if shen_consp(cdr(cdr(KL_ARG_V1118_1112))) else False) if shen_eq(symdic.symdic_kl_tail, car(cdr(KL_ARG_V1118_1112))) else False) if shen_consp(cdr(KL_ARG_V1118_1112)) else False) if shen_eq(symdic.symdic_shen_the, car(KL_ARG_V1118_1112)) else False) if shen_consp(KL_ARG_V1118_1112) else False) else (Cons(symdic.symdic_kl_do, Cons(Cons(symdic.symdic_shen_incinfs, nil), Cons(Cons(symdic.symdic_kl_thaw, Cons(symdic.symdic_Continuation, nil)), nil))) if ((((((shen_eq(nil, cdr(cdr(cdr(KL_ARG_V1118_1112)))) if shen_eq(symdic.symdic_shen_stack, car(cdr(cdr(KL_ARG_V1118_1112)))) else False) if shen_consp(cdr(cdr(KL_ARG_V1118_1112))) else False) if shen_eq(symdic.symdic_shen_the, car(cdr(KL_ARG_V1118_1112))) else False) if shen_consp(cdr(KL_ARG_V1118_1112)) else False) if shen_eq(symdic.symdic_shen_pop, car(KL_ARG_V1118_1112)) else False) if shen_consp(KL_ARG_V1118_1112) else False) else (Cons(symdic.symdic_kl_do, Cons(Cons(symdic.symdic_shen_incinfs, nil), Cons(tco_apply(shen_call_the_continuation, [tco_apply(shen_chwild, [car(cdr(cdr(cdr(KL_ARG_V1118_1112))))]), symdic.symdic_ProcessN, symdic.symdic_Continuation]), nil))) if (((((((shen_eq(nil, cdr(cdr(cdr(cdr(KL_ARG_V1118_1112))))) if shen_consp(cdr(cdr(cdr(KL_ARG_V1118_1112)))) else False) if shen_eq(symdic.symdic_shen_continuation, car(cdr(cdr(KL_ARG_V1118_1112)))) else False) if shen_consp(cdr(cdr(KL_ARG_V1118_1112))) else False) if shen_eq(symdic.symdic_shen_the, car(cdr(KL_ARG_V1118_1112))) else False) if shen_consp(cdr(KL_ARG_V1118_1112)) else False) if shen_eq(symdic.symdic_kl_call, car(KL_ARG_V1118_1112)) else False) if shen_consp(KL_ARG_V1118_1112) else False) else (KL_ARG_V1118_1112 if True else shen_simple_error('condition failure'))))))))))))))))
shen_add_fun('shen.aum_to_shen', shen_aum_to_shen, 1)

@tail_recursion
def shen_chwild(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_chwild, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1119_1113 = FUN_ARGS[0]
    global symdic
    return (Cons(symdic.symdic_shen_newpv, Cons(symdic.symdic_ProcessN, nil)) if shen_eq(KL_ARG_V1119_1113, symdic.symdic_kl__) else (tail_call(kl_map, [symdic.symdic_shen_chwild, KL_ARG_V1119_1113]) if shen_consp(KL_ARG_V1119_1113) else (KL_ARG_V1119_1113 if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.chwild', shen_chwild, 1)

@tail_recursion
def shen_newpv(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_newpv, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1120_1114 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Countx431_1115 = None
        KL_LOC_IncVar_1116 = None
        KL_LOC_Vector_1117 = None
        KL_LOC_ResizeVectorIfNeeded_1118 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Countx431_1115', (shen_absvector_get(shen_get(symdic.symdic_shen_x42varcounterx42), KL_ARG_V1120_1114) + 1)), [setattr(KL_CTX, 'KL_LOC_IncVar_1116', shen_absvector_set(shen_get(symdic.symdic_shen_x42varcounterx42), KL_ARG_V1120_1114, KL_CTX.KL_LOC_Countx431_1115)), [setattr(KL_CTX, 'KL_LOC_Vector_1117', shen_absvector_get(shen_get(symdic.symdic_shen_x42prologvectorsx42), KL_ARG_V1120_1114)), [setattr(KL_CTX, 'KL_LOC_ResizeVectorIfNeeded_1118', (tco_apply(shen_resizeprocessvector, [KL_ARG_V1120_1114, KL_CTX.KL_LOC_Countx431_1115]) if shen_eq(KL_CTX.KL_LOC_Countx431_1115, tco_apply(kl_limit, [KL_CTX.KL_LOC_Vector_1117])) else symdic.symdic_shen_skip)), tail_call(shen_mkx45pvar, [KL_CTX.KL_LOC_Countx431_1115])][(-1)]][(-1)]][(-1)]][(-1)]
shen_add_fun('shen.newpv', shen_newpv, 1)

@tail_recursion
def shen_resizeprocessvector(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_resizeprocessvector, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1121_1119 = FUN_ARGS[0]
    KL_ARG_V1122_1120 = FUN_ARGS[1]

    class KL_Context:
        KL_LOC_Vector_1121 = None
        KL_LOC_BigVector_1122 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Vector_1121', shen_absvector_get(shen_get(symdic.symdic_shen_x42prologvectorsx42), KL_ARG_V1121_1119)), [setattr(KL_CTX, 'KL_LOC_BigVector_1122', tco_apply(shen_resizex45vector, [KL_CTX.KL_LOC_Vector_1121, (KL_ARG_V1122_1120 + KL_ARG_V1122_1120), symdic.symdic_shen_x45nullx45])), shen_absvector_set(shen_get(symdic.symdic_shen_x42prologvectorsx42), KL_ARG_V1121_1119, KL_CTX.KL_LOC_BigVector_1122)][(-1)]][(-1)]
shen_add_fun('shen.resizeprocessvector', shen_resizeprocessvector, 2)

@tail_recursion
def shen_resizex45vector(*FUN_ARGS):
    FUN_ARITY = 3
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_resizex45vector, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1123_1123 = FUN_ARGS[0]
    KL_ARG_V1124_1124 = FUN_ARGS[1]
    KL_ARG_V1125_1125 = FUN_ARGS[2]

    class KL_Context:
        KL_LOC_BigVector_1126 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_BigVector_1126', shen_absvector_set(shen_absvector((1 + KL_ARG_V1124_1124)), 0, KL_ARG_V1124_1124)), tail_call(shen_copyx45vector, [KL_ARG_V1123_1123, KL_CTX.KL_LOC_BigVector_1126, tco_apply(kl_limit, [KL_ARG_V1123_1123]), KL_ARG_V1124_1124, KL_ARG_V1125_1125])][(-1)]
shen_add_fun('shen.resize-vector', shen_resizex45vector, 3)

@tail_recursion
def shen_copyx45vector(*FUN_ARGS):
    FUN_ARITY = 5
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_copyx45vector, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1126_1127 = FUN_ARGS[0]
    KL_ARG_V1127_1128 = FUN_ARGS[1]
    KL_ARG_V1128_1129 = FUN_ARGS[2]
    KL_ARG_V1129_1130 = FUN_ARGS[3]
    KL_ARG_V1130_1131 = FUN_ARGS[4]
    global symdic
    return tail_call(shen_copyx45vectorx45stagex452, [(1 + KL_ARG_V1128_1129), (KL_ARG_V1129_1130 + 1), KL_ARG_V1130_1131, tco_apply(shen_copyx45vectorx45stagex451, [1, KL_ARG_V1126_1127, KL_ARG_V1127_1128, (1 + KL_ARG_V1128_1129)])])
shen_add_fun('shen.copy-vector', shen_copyx45vector, 5)

@tail_recursion
def shen_copyx45vectorx45stagex451(*FUN_ARGS):
    FUN_ARITY = 4
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_copyx45vectorx45stagex451, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1133_1132 = FUN_ARGS[0]
    KL_ARG_V1134_1133 = FUN_ARGS[1]
    KL_ARG_V1135_1134 = FUN_ARGS[2]
    KL_ARG_V1136_1135 = FUN_ARGS[3]
    global symdic
    return (KL_ARG_V1135_1134 if shen_eq(KL_ARG_V1136_1135, KL_ARG_V1133_1132) else (tail_call(shen_copyx45vectorx45stagex451, [(1 + KL_ARG_V1133_1132), KL_ARG_V1134_1133, shen_absvector_set(KL_ARG_V1135_1134, KL_ARG_V1133_1132, shen_absvector_get(KL_ARG_V1134_1133, KL_ARG_V1133_1132)), KL_ARG_V1136_1135]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.copy-vector-stage-1', shen_copyx45vectorx45stagex451, 4)

@tail_recursion
def shen_copyx45vectorx45stagex452(*FUN_ARGS):
    FUN_ARITY = 4
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_copyx45vectorx45stagex452, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1140_1136 = FUN_ARGS[0]
    KL_ARG_V1141_1137 = FUN_ARGS[1]
    KL_ARG_V1142_1138 = FUN_ARGS[2]
    KL_ARG_V1143_1139 = FUN_ARGS[3]
    global symdic
    return (KL_ARG_V1143_1139 if shen_eq(KL_ARG_V1141_1137, KL_ARG_V1140_1136) else (tail_call(shen_copyx45vectorx45stagex452, [(KL_ARG_V1140_1136 + 1), KL_ARG_V1141_1137, KL_ARG_V1142_1138, shen_absvector_set(KL_ARG_V1143_1139, KL_ARG_V1140_1136, KL_ARG_V1142_1138)]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.copy-vector-stage-2', shen_copyx45vectorx45stagex452, 4)

@tail_recursion
def shen_mkx45pvar(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_mkx45pvar, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1145_1140 = FUN_ARGS[0]
    global symdic
    return shen_absvector_set(shen_absvector_set(shen_absvector(2), 0, symdic.symdic_shen_pvar), 1, KL_ARG_V1145_1140)
shen_add_fun('shen.mk-pvar', shen_mkx45pvar, 1)

@tail_recursion
def shen_pvarx63(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_pvarx63, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1146_1141 = FUN_ARGS[0]
    global symdic
    return (shen_eq(shen_absvector_get(KL_ARG_V1146_1141, 0), symdic.symdic_shen_pvar) if shen_absvectorp(KL_ARG_V1146_1141) else False)
shen_add_fun('shen.pvar?', shen_pvarx63, 1)

@tail_recursion
def shen_bindv(*FUN_ARGS):
    FUN_ARITY = 3
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_bindv, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1147_1142 = FUN_ARGS[0]
    KL_ARG_V1148_1143 = FUN_ARGS[1]
    KL_ARG_V1149_1144 = FUN_ARGS[2]

    class KL_Context:
        KL_LOC_Vector_1145 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Vector_1145', shen_absvector_get(shen_get(symdic.symdic_shen_x42prologvectorsx42), KL_ARG_V1149_1144)), shen_absvector_set(KL_CTX.KL_LOC_Vector_1145, shen_absvector_get(KL_ARG_V1147_1142, 1), KL_ARG_V1148_1143)][(-1)]
shen_add_fun('shen.bindv', shen_bindv, 3)

@tail_recursion
def shen_unbindv(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_unbindv, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1150_1146 = FUN_ARGS[0]
    KL_ARG_V1151_1147 = FUN_ARGS[1]

    class KL_Context:
        KL_LOC_Vector_1148 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Vector_1148', shen_absvector_get(shen_get(symdic.symdic_shen_x42prologvectorsx42), KL_ARG_V1151_1147)), shen_absvector_set(KL_CTX.KL_LOC_Vector_1148, shen_absvector_get(KL_ARG_V1150_1146, 1), symdic.symdic_shen_x45nullx45)][(-1)]
shen_add_fun('shen.unbindv', shen_unbindv, 2)

@tail_recursion
def shen_incinfs(*FUN_ARGS):
    FUN_ARITY = 0
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_incinfs, (FUN_ARGS + lambdaargs)))
    global symdic
    return shen_set(symdic.symdic_shen_x42infsx42, (1 + shen_get(symdic.symdic_shen_x42infsx42)))
shen_add_fun('shen.incinfs', shen_incinfs, 0)

@tail_recursion
def shen_call_the_continuation(*FUN_ARGS):
    FUN_ARITY = 3
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_call_the_continuation, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1152_1149 = FUN_ARGS[0]
    KL_ARG_V1153_1150 = FUN_ARGS[1]
    KL_ARG_V1154_1151 = FUN_ARGS[2]

    class KL_Context:
        KL_LOC_NewContinuation_1152 = None
    KL_CTX = KL_Context()
    global symdic
    return (Cons(car(car(KL_ARG_V1152_1149)), tco_apply(kl_append, [cdr(car(KL_ARG_V1152_1149)), Cons(KL_ARG_V1153_1150, Cons(KL_ARG_V1154_1151, nil))])) if ((shen_eq(nil, cdr(KL_ARG_V1152_1149)) if shen_consp(car(KL_ARG_V1152_1149)) else False) if shen_consp(KL_ARG_V1152_1149) else False) else ([setattr(KL_CTX, 'KL_LOC_NewContinuation_1152', tco_apply(shen_newcontinuation, [cdr(KL_ARG_V1152_1149), KL_ARG_V1153_1150, KL_ARG_V1154_1151])), Cons(car(car(KL_ARG_V1152_1149)), tco_apply(kl_append, [cdr(car(KL_ARG_V1152_1149)), Cons(KL_ARG_V1153_1150, Cons(KL_CTX.KL_LOC_NewContinuation_1152, nil))]))][(-1)] if (shen_consp(car(KL_ARG_V1152_1149)) if shen_consp(KL_ARG_V1152_1149) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_call_the_continuation]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.call_the_continuation', shen_call_the_continuation, 3)

@tail_recursion
def shen_newcontinuation(*FUN_ARGS):
    FUN_ARITY = 3
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_newcontinuation, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1155_1153 = FUN_ARGS[0]
    KL_ARG_V1156_1154 = FUN_ARGS[1]
    KL_ARG_V1157_1155 = FUN_ARGS[2]
    global symdic
    return (KL_ARG_V1157_1155 if shen_eq(nil, KL_ARG_V1155_1153) else (Cons(symdic.symdic_kl_freeze, Cons(Cons(car(car(KL_ARG_V1155_1153)), tco_apply(kl_append, [cdr(car(KL_ARG_V1155_1153)), Cons(KL_ARG_V1156_1154, Cons(tco_apply(shen_newcontinuation, [cdr(KL_ARG_V1155_1153), KL_ARG_V1156_1154, KL_ARG_V1157_1155]), nil))])), nil)) if (shen_consp(car(KL_ARG_V1155_1153)) if shen_consp(KL_ARG_V1155_1153) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_newcontinuation]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.newcontinuation', shen_newcontinuation, 3)

@tail_recursion
def kl_return(*FUN_ARGS):
    FUN_ARITY = 3
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_return, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1162_1156 = FUN_ARGS[0]
    KL_ARG_V1163_1157 = FUN_ARGS[1]
    KL_ARG_V1164_1158 = FUN_ARGS[2]
    global symdic
    return tail_call(shen_deref, [KL_ARG_V1162_1156, KL_ARG_V1163_1157])
shen_add_fun('return', kl_return, 3)

@tail_recursion
def shen_measurex38return(*FUN_ARGS):
    FUN_ARITY = 3
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_measurex38return, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1169_1159 = FUN_ARGS[0]
    KL_ARG_V1170_1160 = FUN_ARGS[1]
    KL_ARG_V1171_1161 = FUN_ARGS[2]
    global symdic
    return [tco_apply(shen_prhush, [tco_apply(shen_app, [shen_get(symdic.symdic_shen_x42infsx42), ' inferences\r\n', symdic.symdic_shen_a]), tco_apply(kl_stoutput, [])]), tail_call(shen_deref, [KL_ARG_V1169_1159, KL_ARG_V1170_1160])][(-1)]
shen_add_fun('shen.measure&return', shen_measurex38return, 3)

@tail_recursion
def kl_unify(*FUN_ARGS):
    FUN_ARITY = 4
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_unify, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1172_1162 = FUN_ARGS[0]
    KL_ARG_V1173_1163 = FUN_ARGS[1]
    KL_ARG_V1174_1164 = FUN_ARGS[2]
    KL_ARG_V1175_1165 = FUN_ARGS[3]
    global symdic
    return tail_call(shen_lzyx61, [tco_apply(shen_lazyderef, [KL_ARG_V1172_1162, KL_ARG_V1174_1164]), tco_apply(shen_lazyderef, [KL_ARG_V1173_1163, KL_ARG_V1174_1164]), KL_ARG_V1174_1164, KL_ARG_V1175_1165])
shen_add_fun('unify', kl_unify, 4)

@tail_recursion
def shen_lzyx61(*FUN_ARGS):
    FUN_ARITY = 4
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_lzyx61, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1192_1166 = FUN_ARGS[0]
    KL_ARG_V1193_1167 = FUN_ARGS[1]
    KL_ARG_V1194_1168 = FUN_ARGS[2]
    KL_ARG_V1195_1169 = FUN_ARGS[3]
    global symdic
    return (tail_call(kl_thaw, [KL_ARG_V1195_1169]) if shen_eq(KL_ARG_V1193_1167, KL_ARG_V1192_1166) else (tail_call(kl_bind, [KL_ARG_V1192_1166, KL_ARG_V1193_1167, KL_ARG_V1194_1168, KL_ARG_V1195_1169]) if tco_apply(shen_pvarx63, [KL_ARG_V1192_1166]) else (tail_call(kl_bind, [KL_ARG_V1193_1167, KL_ARG_V1192_1166, KL_ARG_V1194_1168, KL_ARG_V1195_1169]) if tco_apply(shen_pvarx63, [KL_ARG_V1193_1167]) else (tail_call(shen_lzyx61, [tco_apply(shen_lazyderef, [car(KL_ARG_V1192_1166), KL_ARG_V1194_1168]), tco_apply(shen_lazyderef, [car(KL_ARG_V1193_1167), KL_ARG_V1194_1168]), KL_ARG_V1194_1168, (lambda : tail_call(shen_lzyx61, [tco_apply(shen_lazyderef, [cdr(KL_ARG_V1192_1166), KL_ARG_V1194_1168]), tco_apply(shen_lazyderef, [cdr(KL_ARG_V1193_1167), KL_ARG_V1194_1168]), KL_ARG_V1194_1168, KL_ARG_V1195_1169]))]) if (shen_consp(KL_ARG_V1193_1167) if shen_consp(KL_ARG_V1192_1166) else False) else (False if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.lzy=', shen_lzyx61, 4)

@tail_recursion
def shen_deref(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_deref, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1197_1170 = FUN_ARGS[0]
    KL_ARG_V1198_1171 = FUN_ARGS[1]

    class KL_Context:
        KL_LOC_Value_1172 = None
    KL_CTX = KL_Context()
    global symdic
    return (Cons(tco_apply(shen_deref, [car(KL_ARG_V1197_1170), KL_ARG_V1198_1171]), tco_apply(shen_deref, [cdr(KL_ARG_V1197_1170), KL_ARG_V1198_1171])) if shen_consp(KL_ARG_V1197_1170) else (([setattr(KL_CTX, 'KL_LOC_Value_1172', tco_apply(shen_valvector, [KL_ARG_V1197_1170, KL_ARG_V1198_1171])), (KL_ARG_V1197_1170 if shen_eq(KL_CTX.KL_LOC_Value_1172, symdic.symdic_shen_x45nullx45) else tail_call(shen_deref, [KL_CTX.KL_LOC_Value_1172, KL_ARG_V1198_1171]))][(-1)] if tco_apply(shen_pvarx63, [KL_ARG_V1197_1170]) else KL_ARG_V1197_1170) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.deref', shen_deref, 2)

@tail_recursion
def shen_lazyderef(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_lazyderef, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1199_1173 = FUN_ARGS[0]
    KL_ARG_V1200_1174 = FUN_ARGS[1]

    class KL_Context:
        KL_LOC_Value_1175 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_Value_1175', tco_apply(shen_valvector, [KL_ARG_V1199_1173, KL_ARG_V1200_1174])), (KL_ARG_V1199_1173 if shen_eq(KL_CTX.KL_LOC_Value_1175, symdic.symdic_shen_x45nullx45) else tail_call(shen_lazyderef, [KL_CTX.KL_LOC_Value_1175, KL_ARG_V1200_1174]))][(-1)] if tco_apply(shen_pvarx63, [KL_ARG_V1199_1173]) else KL_ARG_V1199_1173)
shen_add_fun('shen.lazyderef', shen_lazyderef, 2)

@tail_recursion
def shen_valvector(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_valvector, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1201_1176 = FUN_ARGS[0]
    KL_ARG_V1202_1177 = FUN_ARGS[1]
    global symdic
    return shen_absvector_get(shen_absvector_get(shen_get(symdic.symdic_shen_x42prologvectorsx42), KL_ARG_V1202_1177), shen_absvector_get(KL_ARG_V1201_1176, 1))
shen_add_fun('shen.valvector', shen_valvector, 2)

@tail_recursion
def kl_unifyx33(*FUN_ARGS):
    FUN_ARITY = 4
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_unifyx33, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1203_1178 = FUN_ARGS[0]
    KL_ARG_V1204_1179 = FUN_ARGS[1]
    KL_ARG_V1205_1180 = FUN_ARGS[2]
    KL_ARG_V1206_1181 = FUN_ARGS[3]
    global symdic
    return tail_call(shen_lzyx61x33, [tco_apply(shen_lazyderef, [KL_ARG_V1203_1178, KL_ARG_V1205_1180]), tco_apply(shen_lazyderef, [KL_ARG_V1204_1179, KL_ARG_V1205_1180]), KL_ARG_V1205_1180, KL_ARG_V1206_1181])
shen_add_fun('unify!', kl_unifyx33, 4)

@tail_recursion
def shen_lzyx61x33(*FUN_ARGS):
    FUN_ARITY = 4
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_lzyx61x33, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1223_1182 = FUN_ARGS[0]
    KL_ARG_V1224_1183 = FUN_ARGS[1]
    KL_ARG_V1225_1184 = FUN_ARGS[2]
    KL_ARG_V1226_1185 = FUN_ARGS[3]
    global symdic
    return (tail_call(kl_thaw, [KL_ARG_V1226_1185]) if shen_eq(KL_ARG_V1224_1183, KL_ARG_V1223_1182) else (tail_call(kl_bind, [KL_ARG_V1223_1182, KL_ARG_V1224_1183, KL_ARG_V1225_1184, KL_ARG_V1226_1185]) if ((not tco_apply(shen_occursx63, [KL_ARG_V1223_1182, tco_apply(shen_deref, [KL_ARG_V1224_1183, KL_ARG_V1225_1184])])) if tco_apply(shen_pvarx63, [KL_ARG_V1223_1182]) else False) else (tail_call(kl_bind, [KL_ARG_V1224_1183, KL_ARG_V1223_1182, KL_ARG_V1225_1184, KL_ARG_V1226_1185]) if ((not tco_apply(shen_occursx63, [KL_ARG_V1224_1183, tco_apply(shen_deref, [KL_ARG_V1223_1182, KL_ARG_V1225_1184])])) if tco_apply(shen_pvarx63, [KL_ARG_V1224_1183]) else False) else (tail_call(shen_lzyx61x33, [tco_apply(shen_lazyderef, [car(KL_ARG_V1223_1182), KL_ARG_V1225_1184]), tco_apply(shen_lazyderef, [car(KL_ARG_V1224_1183), KL_ARG_V1225_1184]), KL_ARG_V1225_1184, (lambda : tail_call(shen_lzyx61x33, [tco_apply(shen_lazyderef, [cdr(KL_ARG_V1223_1182), KL_ARG_V1225_1184]), tco_apply(shen_lazyderef, [cdr(KL_ARG_V1224_1183), KL_ARG_V1225_1184]), KL_ARG_V1225_1184, KL_ARG_V1226_1185]))]) if (shen_consp(KL_ARG_V1224_1183) if shen_consp(KL_ARG_V1223_1182) else False) else (False if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.lzy=!', shen_lzyx61x33, 4)

@tail_recursion
def shen_occursx63(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_occursx63, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1236_1186 = FUN_ARGS[0]
    KL_ARG_V1237_1187 = FUN_ARGS[1]
    global symdic
    return (True if shen_eq(KL_ARG_V1237_1187, KL_ARG_V1236_1186) else ((True if tco_apply(shen_occursx63, [KL_ARG_V1236_1186, car(KL_ARG_V1237_1187)]) else tail_call(shen_occursx63, [KL_ARG_V1236_1186, cdr(KL_ARG_V1237_1187)])) if shen_consp(KL_ARG_V1237_1187) else (False if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.occurs?', shen_occursx63, 2)

@tail_recursion
def kl_identical(*FUN_ARGS):
    FUN_ARITY = 4
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_identical, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1239_1188 = FUN_ARGS[0]
    KL_ARG_V1240_1189 = FUN_ARGS[1]
    KL_ARG_V1241_1190 = FUN_ARGS[2]
    KL_ARG_V1242_1191 = FUN_ARGS[3]
    global symdic
    return tail_call(shen_lzyx61x61, [tco_apply(shen_lazyderef, [KL_ARG_V1239_1188, KL_ARG_V1241_1190]), tco_apply(shen_lazyderef, [KL_ARG_V1240_1189, KL_ARG_V1241_1190]), KL_ARG_V1241_1190, KL_ARG_V1242_1191])
shen_add_fun('identical', kl_identical, 4)

@tail_recursion
def shen_lzyx61x61(*FUN_ARGS):
    FUN_ARITY = 4
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_lzyx61x61, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1259_1192 = FUN_ARGS[0]
    KL_ARG_V1260_1193 = FUN_ARGS[1]
    KL_ARG_V1261_1194 = FUN_ARGS[2]
    KL_ARG_V1262_1195 = FUN_ARGS[3]
    global symdic
    return (tail_call(kl_thaw, [KL_ARG_V1262_1195]) if shen_eq(KL_ARG_V1260_1193, KL_ARG_V1259_1192) else (tail_call(shen_lzyx61x61, [tco_apply(shen_lazyderef, [car(KL_ARG_V1259_1192), KL_ARG_V1261_1194]), tco_apply(shen_lazyderef, [car(KL_ARG_V1260_1193), KL_ARG_V1261_1194]), KL_ARG_V1261_1194, (lambda : tail_call(shen_lzyx61x61, [cdr(KL_ARG_V1259_1192), cdr(KL_ARG_V1260_1193), KL_ARG_V1261_1194, KL_ARG_V1262_1195]))]) if (shen_consp(KL_ARG_V1260_1193) if shen_consp(KL_ARG_V1259_1192) else False) else (False if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.lzy==', shen_lzyx61x61, 4)

@tail_recursion
def shen_pvar(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_pvar, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1264_1196 = FUN_ARGS[0]
    global symdic
    return ('Var' + tco_apply(shen_app, [shen_absvector_get(KL_ARG_V1264_1196, 1), '', symdic.symdic_shen_a]))
shen_add_fun('shen.pvar', shen_pvar, 1)

@tail_recursion
def kl_bind(*FUN_ARGS):
    FUN_ARITY = 4
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_bind, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1265_1197 = FUN_ARGS[0]
    KL_ARG_V1266_1198 = FUN_ARGS[1]
    KL_ARG_V1267_1199 = FUN_ARGS[2]
    KL_ARG_V1268_1200 = FUN_ARGS[3]

    class KL_Context:
        KL_LOC_Result_1201 = None
    KL_CTX = KL_Context()
    global symdic
    return [tco_apply(shen_bindv, [KL_ARG_V1265_1197, KL_ARG_V1266_1198, KL_ARG_V1267_1199]), [setattr(KL_CTX, 'KL_LOC_Result_1201', tco_apply(kl_thaw, [KL_ARG_V1268_1200])), [tco_apply(shen_unbindv, [KL_ARG_V1265_1197, KL_ARG_V1267_1199]), KL_CTX.KL_LOC_Result_1201][(-1)]][(-1)]][(-1)]
shen_add_fun('bind', kl_bind, 4)

@tail_recursion
def kl_fwhen(*FUN_ARGS):
    FUN_ARITY = 3
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_fwhen, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1283_1202 = FUN_ARGS[0]
    KL_ARG_V1284_1203 = FUN_ARGS[1]
    KL_ARG_V1285_1204 = FUN_ARGS[2]
    global symdic
    return (tail_call(kl_thaw, [KL_ARG_V1285_1204]) if shen_eq(True, KL_ARG_V1283_1202) else (False if shen_eq(False, KL_ARG_V1283_1202) else (shen_simple_error(('fwhen expects a boolean: not ' + tco_apply(shen_app, [KL_ARG_V1283_1202, '%', symdic.symdic_shen_s]))) if True else shen_simple_error('condition failure'))))
shen_add_fun('fwhen', kl_fwhen, 3)

@tail_recursion
def kl_call(*FUN_ARGS):
    FUN_ARITY = 3
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_call, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1298_1205 = FUN_ARGS[0]
    KL_ARG_V1299_1206 = FUN_ARGS[1]
    KL_ARG_V1300_1207 = FUN_ARGS[2]
    global symdic
    return (tail_call(shen_callx45help, [tco_apply(shen_m_prolog_to_sx45prolog_predicate, [tco_apply(shen_lazyderef, [car(KL_ARG_V1298_1205), KL_ARG_V1299_1206])]), cdr(KL_ARG_V1298_1205), KL_ARG_V1299_1206, KL_ARG_V1300_1207]) if shen_consp(KL_ARG_V1298_1205) else (False if True else shen_simple_error('condition failure')))
shen_add_fun('call', kl_call, 3)

@tail_recursion
def shen_callx45help(*FUN_ARGS):
    FUN_ARITY = 4
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_callx45help, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1301_1208 = FUN_ARGS[0]
    KL_ARG_V1302_1209 = FUN_ARGS[1]
    KL_ARG_V1303_1210 = FUN_ARGS[2]
    KL_ARG_V1304_1211 = FUN_ARGS[3]
    global symdic
    return (shen_apply(KL_ARG_V1301_1208, [KL_ARG_V1303_1210, KL_ARG_V1304_1211]) if shen_eq(nil, KL_ARG_V1302_1209) else (tail_call(shen_callx45help, [shen_apply(KL_ARG_V1301_1208, [car(KL_ARG_V1302_1209)]), cdr(KL_ARG_V1302_1209), KL_ARG_V1303_1210, KL_ARG_V1304_1211]) if shen_consp(KL_ARG_V1302_1209) else (tail_call(shen_sysx45error, [symdic.symdic_shen_callx45help]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.call-help', shen_callx45help, 4)

@tail_recursion
def shen_intprolog(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_intprolog, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1305_1212 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_ProcessN_1213 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_ProcessN_1213', tco_apply(shen_startx45newx45prologx45process, [])), tail_call(shen_intprologx45help, [car(car(KL_ARG_V1305_1212)), tco_apply(shen_insertx45prologx45variables, [Cons(cdr(car(KL_ARG_V1305_1212)), Cons(cdr(KL_ARG_V1305_1212), nil)), KL_CTX.KL_LOC_ProcessN_1213]), KL_CTX.KL_LOC_ProcessN_1213])][(-1)] if (shen_consp(car(KL_ARG_V1305_1212)) if shen_consp(KL_ARG_V1305_1212) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_intprolog]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.intprolog', shen_intprolog, 1)

@tail_recursion
def shen_intprologx45help(*FUN_ARGS):
    FUN_ARITY = 3
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_intprologx45help, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1306_1214 = FUN_ARGS[0]
    KL_ARG_V1307_1215 = FUN_ARGS[1]
    KL_ARG_V1308_1216 = FUN_ARGS[2]
    global symdic
    return (tail_call(shen_intprologx45helpx45help, [KL_ARG_V1306_1214, car(KL_ARG_V1307_1215), car(cdr(KL_ARG_V1307_1215)), KL_ARG_V1308_1216]) if ((shen_eq(nil, cdr(cdr(KL_ARG_V1307_1215))) if shen_consp(cdr(KL_ARG_V1307_1215)) else False) if shen_consp(KL_ARG_V1307_1215) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_intprologx45help]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.intprolog-help', shen_intprologx45help, 3)

@tail_recursion
def shen_intprologx45helpx45help(*FUN_ARGS):
    FUN_ARITY = 4
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_intprologx45helpx45help, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1309_1217 = FUN_ARGS[0]
    KL_ARG_V1310_1218 = FUN_ARGS[1]
    KL_ARG_V1311_1219 = FUN_ARGS[2]
    KL_ARG_V1312_1220 = FUN_ARGS[3]
    global symdic
    return (shen_apply(KL_ARG_V1309_1217, [KL_ARG_V1312_1220, (lambda : tail_call(shen_callx45rest, [KL_ARG_V1311_1219, KL_ARG_V1312_1220]))]) if shen_eq(nil, KL_ARG_V1310_1218) else (tail_call(shen_intprologx45helpx45help, [shen_apply(KL_ARG_V1309_1217, [car(KL_ARG_V1310_1218)]), cdr(KL_ARG_V1310_1218), KL_ARG_V1311_1219, KL_ARG_V1312_1220]) if shen_consp(KL_ARG_V1310_1218) else (tail_call(shen_sysx45error, [symdic.symdic_shen_intprologx45helpx45help]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.intprolog-help-help', shen_intprologx45helpx45help, 4)

@tail_recursion
def shen_callx45rest(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_callx45rest, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1315_1221 = FUN_ARGS[0]
    KL_ARG_V1316_1222 = FUN_ARGS[1]
    global symdic
    return (True if shen_eq(nil, KL_ARG_V1315_1221) else (tail_call(shen_callx45rest, [Cons(Cons(tco_apply(car(car(KL_ARG_V1315_1221)), [car(cdr(car(KL_ARG_V1315_1221)))]), cdr(cdr(car(KL_ARG_V1315_1221)))), cdr(KL_ARG_V1315_1221)), KL_ARG_V1316_1222]) if ((shen_consp(cdr(car(KL_ARG_V1315_1221))) if shen_consp(car(KL_ARG_V1315_1221)) else False) if shen_consp(KL_ARG_V1315_1221) else False) else (tail_call(car(car(KL_ARG_V1315_1221)), [KL_ARG_V1316_1222, (lambda : tail_call(shen_callx45rest, [cdr(KL_ARG_V1315_1221), KL_ARG_V1316_1222]))]) if ((shen_eq(nil, cdr(car(KL_ARG_V1315_1221))) if shen_consp(car(KL_ARG_V1315_1221)) else False) if shen_consp(KL_ARG_V1315_1221) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_callx45rest]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.call-rest', shen_callx45rest, 2)

@tail_recursion
def shen_startx45newx45prologx45process(*FUN_ARGS):
    FUN_ARITY = 0
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_startx45newx45prologx45process, (FUN_ARGS + lambdaargs)))

    class KL_Context:
        KL_LOC_IncrementProcessCounter_1223 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_IncrementProcessCounter_1223', shen_set(symdic.symdic_shen_x42processx45counterx42, (1 + shen_get(symdic.symdic_shen_x42processx45counterx42)))), tail_call(shen_initialisex45prolog, [KL_CTX.KL_LOC_IncrementProcessCounter_1223])][(-1)]
shen_add_fun('shen.start-new-prolog-process', shen_startx45newx45prologx45process, 0)

@tail_recursion
def shen_insertx45prologx45variables(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_insertx45prologx45variables, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1317_1224 = FUN_ARGS[0]
    KL_ARG_V1318_1225 = FUN_ARGS[1]
    global symdic
    return tail_call(shen_insertx45prologx45variablesx45help, [KL_ARG_V1317_1224, tco_apply(shen_flatten, [KL_ARG_V1317_1224]), KL_ARG_V1318_1225])
shen_add_fun('shen.insert-prolog-variables', shen_insertx45prologx45variables, 2)

@tail_recursion
def shen_insertx45prologx45variablesx45help(*FUN_ARGS):
    FUN_ARITY = 3
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_insertx45prologx45variablesx45help, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1323_1226 = FUN_ARGS[0]
    KL_ARG_V1324_1227 = FUN_ARGS[1]
    KL_ARG_V1325_1228 = FUN_ARGS[2]

    class KL_Context:
        KL_LOC_V_1229 = None
        KL_LOC_XVx47Y_1230 = None
        KL_LOC_Zx45Y_1231 = None
    KL_CTX = KL_Context()
    global symdic
    return (KL_ARG_V1323_1226 if shen_eq(nil, KL_ARG_V1324_1227) else ([setattr(KL_CTX, 'KL_LOC_V_1229', tco_apply(shen_newpv, [KL_ARG_V1325_1228])), [setattr(KL_CTX, 'KL_LOC_XVx47Y_1230', tco_apply(kl_subst, [KL_CTX.KL_LOC_V_1229, car(KL_ARG_V1324_1227), KL_ARG_V1323_1226])), [setattr(KL_CTX, 'KL_LOC_Zx45Y_1231', tco_apply(kl_remove, [car(KL_ARG_V1324_1227), cdr(KL_ARG_V1324_1227)])), tail_call(shen_insertx45prologx45variablesx45help, [KL_CTX.KL_LOC_XVx47Y_1230, KL_CTX.KL_LOC_Zx45Y_1231, KL_ARG_V1325_1228])][(-1)]][(-1)]][(-1)] if (tco_apply(kl_variablex63, [car(KL_ARG_V1324_1227)]) if shen_consp(KL_ARG_V1324_1227) else False) else (tail_call(shen_insertx45prologx45variablesx45help, [KL_ARG_V1323_1226, cdr(KL_ARG_V1324_1227), KL_ARG_V1325_1228]) if shen_consp(KL_ARG_V1324_1227) else (tail_call(shen_sysx45error, [symdic.symdic_shen_insertx45prologx45variablesx45help]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.insert-prolog-variables-help', shen_insertx45prologx45variablesx45help, 3)

@tail_recursion
def shen_initialisex45prolog(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_initialisex45prolog, (FUN_ARGS + lambdaargs)))
    KL_ARG_V1326_1232 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Vector_1233 = None
        KL_LOC_Counter_1234 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Vector_1233', shen_absvector_set(shen_get(symdic.symdic_shen_x42prologvectorsx42), KL_ARG_V1326_1232, tco_apply(shen_fillvector, [tco_apply(kl_vector, [10]), 1, 10, symdic.symdic_shen_x45nullx45]))), [setattr(KL_CTX, 'KL_LOC_Counter_1234', shen_absvector_set(shen_get(symdic.symdic_shen_x42varcounterx42), KL_ARG_V1326_1232, 1)), KL_ARG_V1326_1232][(-1)]][(-1)]
shen_add_fun('shen.initialise-prolog', shen_initialisex45prolog, 1)


#============================== track.kl==============================



@tail_recursion
def shen_f_error(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_f_error, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2086_1235 = FUN_ARGS[0]
    global symdic
    return [tco_apply(shen_prhush, [('partial function ' + tco_apply(shen_app, [KL_ARG_V2086_1235, ';\r\n', symdic.symdic_shen_a])), tco_apply(kl_stoutput, [])]), [(tco_apply(shen_trackx45function, [tco_apply(kl_ps, [KL_ARG_V2086_1235])]) if (tco_apply(kl_yx45orx45nx63, [('track ' + tco_apply(shen_app, [KL_ARG_V2086_1235, '? ', symdic.symdic_shen_a]))]) if (not tco_apply(shen_trackedx63, [KL_ARG_V2086_1235])) else False) else symdic.symdic_shen_ok), shen_simple_error('aborted')][(-1)]][(-1)]
shen_add_fun('shen.f_error', shen_f_error, 1)

@tail_recursion
def shen_trackedx63(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_trackedx63, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2087_1236 = FUN_ARGS[0]
    global symdic
    return tail_call(kl_elementx63, [KL_ARG_V2087_1236, shen_get(symdic.symdic_shen_x42trackingx42)])
shen_add_fun('shen.tracked?', shen_trackedx63, 1)

@tail_recursion
def kl_track(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_track, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2088_1237 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Source_1238 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Source_1238', tco_apply(kl_ps, [KL_ARG_V2088_1237])), tail_call(shen_trackx45function, [KL_CTX.KL_LOC_Source_1238])][(-1)]
shen_add_fun('track', kl_track, 1)

@tail_recursion
def shen_trackx45function(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_trackx45function, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2089_1239 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_KL_1240 = None
        KL_LOC_Ob_1241 = None
        KL_LOC_Tr_1242 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_KL_1240', Cons(symdic.symdic_kl_defun, Cons(car(cdr(KL_ARG_V2089_1239)), Cons(car(cdr(cdr(KL_ARG_V2089_1239))), Cons(tco_apply(shen_insertx45trackingx45code, [car(cdr(KL_ARG_V2089_1239)), car(cdr(cdr(KL_ARG_V2089_1239))), car(cdr(cdr(cdr(KL_ARG_V2089_1239))))]), nil))))), [setattr(KL_CTX, 'KL_LOC_Ob_1241', tco_apply(kl_eval, [KL_CTX.KL_LOC_KL_1240])), [setattr(KL_CTX, 'KL_LOC_Tr_1242', shen_set(symdic.symdic_shen_x42trackingx42, Cons(KL_CTX.KL_LOC_Ob_1241, shen_get(symdic.symdic_shen_x42trackingx42)))), KL_CTX.KL_LOC_Ob_1241][(-1)]][(-1)]][(-1)] if (((((shen_eq(nil, cdr(cdr(cdr(cdr(KL_ARG_V2089_1239))))) if shen_consp(cdr(cdr(cdr(KL_ARG_V2089_1239)))) else False) if shen_consp(cdr(cdr(KL_ARG_V2089_1239))) else False) if shen_consp(cdr(KL_ARG_V2089_1239)) else False) if shen_eq(symdic.symdic_kl_defun, car(KL_ARG_V2089_1239)) else False) if shen_consp(KL_ARG_V2089_1239) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_trackx45function]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.track-function', shen_trackx45function, 1)

@tail_recursion
def shen_insertx45trackingx45code(*FUN_ARGS):
    FUN_ARITY = 3
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_insertx45trackingx45code, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2090_1243 = FUN_ARGS[0]
    KL_ARG_V2091_1244 = FUN_ARGS[1]
    KL_ARG_V2092_1245 = FUN_ARGS[2]
    global symdic
    return Cons(symdic.symdic_kl_do, Cons(Cons(symdic.symdic_kl_set, Cons(symdic.symdic_shen_x42callx42, Cons(Cons(symdic.symdic_kl_x43, Cons(Cons(symdic.symdic_kl_value, Cons(symdic.symdic_shen_x42callx42, nil)), Cons(1, nil))), nil))), Cons(Cons(symdic.symdic_kl_do, Cons(Cons(symdic.symdic_shen_inputx45track, Cons(Cons(symdic.symdic_kl_value, Cons(symdic.symdic_shen_x42callx42, nil)), Cons(KL_ARG_V2090_1243, Cons(tco_apply(shen_cons_form, [KL_ARG_V2091_1244]), nil)))), Cons(Cons(symdic.symdic_kl_do, Cons(Cons(symdic.symdic_shen_terprix45orx45readx45char, nil), Cons(Cons(symdic.symdic_kl_let, Cons(symdic.symdic_Result, Cons(KL_ARG_V2092_1245, Cons(Cons(symdic.symdic_kl_do, Cons(Cons(symdic.symdic_shen_outputx45track, Cons(Cons(symdic.symdic_kl_value, Cons(symdic.symdic_shen_x42callx42, nil)), Cons(KL_ARG_V2090_1243, Cons(symdic.symdic_Result, nil)))), Cons(Cons(symdic.symdic_kl_do, Cons(Cons(symdic.symdic_kl_set, Cons(symdic.symdic_shen_x42callx42, Cons(Cons(symdic.symdic_kl_x45, Cons(Cons(symdic.symdic_kl_value, Cons(symdic.symdic_shen_x42callx42, nil)), Cons(1, nil))), nil))), Cons(Cons(symdic.symdic_kl_do, Cons(Cons(symdic.symdic_shen_terprix45orx45readx45char, nil), Cons(symdic.symdic_Result, nil))), nil))), nil))), nil)))), nil))), nil))), nil)))
shen_add_fun('shen.insert-tracking-code', shen_insertx45trackingx45code, 3)
shen_set(symdic.symdic_shen_x42stepx42, False)

@tail_recursion
def kl_step(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_step, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2097_1246 = FUN_ARGS[0]
    global symdic
    return (shen_set(symdic.symdic_shen_x42stepx42, True) if shen_eq(symdic.symdic_kl_x43, KL_ARG_V2097_1246) else (shen_set(symdic.symdic_shen_x42stepx42, False) if shen_eq(symdic.symdic_kl_x45, KL_ARG_V2097_1246) else (shen_simple_error('step expects a + or a -.\r\n') if True else shen_simple_error('condition failure'))))
shen_add_fun('step', kl_step, 1)

@tail_recursion
def kl_spy(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_spy, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2102_1247 = FUN_ARGS[0]
    global symdic
    return (shen_set(symdic.symdic_shen_x42spyx42, True) if shen_eq(symdic.symdic_kl_x43, KL_ARG_V2102_1247) else (shen_set(symdic.symdic_shen_x42spyx42, False) if shen_eq(symdic.symdic_kl_x45, KL_ARG_V2102_1247) else (shen_simple_error('spy expects a + or a -.\r\n') if True else shen_simple_error('condition failure'))))
shen_add_fun('spy', kl_spy, 1)

@tail_recursion
def shen_terprix45orx45readx45char(*FUN_ARGS):
    FUN_ARITY = 0
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_terprix45orx45readx45char, (FUN_ARGS + lambdaargs)))
    global symdic
    return (tail_call(shen_checkx45byte, [shen_read_byte(shen_get(symdic.symdic_kl_x42stinputx42))]) if shen_get(symdic.symdic_shen_x42stepx42) else tail_call(kl_nl, [1]))
shen_add_fun('shen.terpri-or-read-char', shen_terprix45orx45readx45char, 0)

@tail_recursion
def shen_checkx45byte(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_checkx45byte, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2107_1248 = FUN_ARGS[0]
    global symdic
    return (shen_simple_error('aborted') if shen_eq(KL_ARG_V2107_1248, tco_apply(shen_hat, [])) else (True if True else shen_simple_error('condition failure')))
shen_add_fun('shen.check-byte', shen_checkx45byte, 1)

@tail_recursion
def shen_inputx45track(*FUN_ARGS):
    FUN_ARITY = 3
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_inputx45track, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2108_1249 = FUN_ARGS[0]
    KL_ARG_V2109_1250 = FUN_ARGS[1]
    KL_ARG_V2110_1251 = FUN_ARGS[2]
    global symdic
    return [tco_apply(shen_prhush, [('\r\n' + tco_apply(shen_app, [tco_apply(shen_spaces, [KL_ARG_V2108_1249]), ('<' + tco_apply(shen_app, [KL_ARG_V2108_1249, ('> Inputs to ' + tco_apply(shen_app, [KL_ARG_V2109_1250, (' \r\n' + tco_apply(shen_app, [tco_apply(shen_spaces, [KL_ARG_V2108_1249]), '', symdic.symdic_shen_a])), symdic.symdic_shen_a])), symdic.symdic_shen_a])), symdic.symdic_shen_a])), tco_apply(kl_stoutput, [])]), tail_call(shen_recursivelyx45print, [KL_ARG_V2110_1251])][(-1)]
shen_add_fun('shen.input-track', shen_inputx45track, 3)

@tail_recursion
def shen_recursivelyx45print(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_recursivelyx45print, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2111_1252 = FUN_ARGS[0]
    global symdic
    return (tail_call(shen_prhush, [' ==>', tco_apply(kl_stoutput, [])]) if shen_eq(nil, KL_ARG_V2111_1252) else ([tco_apply(kl_print, [car(KL_ARG_V2111_1252)]), [tco_apply(shen_prhush, [', ', tco_apply(kl_stoutput, [])]), tail_call(shen_recursivelyx45print, [cdr(KL_ARG_V2111_1252)])][(-1)]][(-1)] if shen_consp(KL_ARG_V2111_1252) else (tail_call(shen_sysx45error, [symdic.symdic_shen_recursivelyx45print]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.recursively-print', shen_recursivelyx45print, 1)

@tail_recursion
def shen_spaces(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_spaces, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2112_1253 = FUN_ARGS[0]
    global symdic
    return ('' if shen_eq(0, KL_ARG_V2112_1253) else ((' ' + tco_apply(shen_spaces, [(KL_ARG_V2112_1253 - 1)])) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.spaces', shen_spaces, 1)

@tail_recursion
def shen_outputx45track(*FUN_ARGS):
    FUN_ARITY = 3
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_outputx45track, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2113_1254 = FUN_ARGS[0]
    KL_ARG_V2114_1255 = FUN_ARGS[1]
    KL_ARG_V2115_1256 = FUN_ARGS[2]
    global symdic
    return tail_call(shen_prhush, [('\r\n' + tco_apply(shen_app, [tco_apply(shen_spaces, [KL_ARG_V2113_1254]), ('<' + tco_apply(shen_app, [KL_ARG_V2113_1254, ('> Output from ' + tco_apply(shen_app, [KL_ARG_V2114_1255, (' \r\n' + tco_apply(shen_app, [tco_apply(shen_spaces, [KL_ARG_V2113_1254]), ('==> ' + tco_apply(shen_app, [KL_ARG_V2115_1256, '', symdic.symdic_shen_s])), symdic.symdic_shen_a])), symdic.symdic_shen_a])), symdic.symdic_shen_a])), symdic.symdic_shen_a])), tco_apply(kl_stoutput, [])])
shen_add_fun('shen.output-track', shen_outputx45track, 3)

@tail_recursion
def kl_untrack(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_untrack, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2116_1257 = FUN_ARGS[0]
    global symdic
    return tail_call(kl_eval, [tco_apply(kl_ps, [KL_ARG_V2116_1257])])
shen_add_fun('untrack', kl_untrack, 1)

@tail_recursion
def kl_profile(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_profile, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2117_1258 = FUN_ARGS[0]
    global symdic
    return tail_call(shen_profilex45help, [tco_apply(kl_ps, [KL_ARG_V2117_1258])])
shen_add_fun('profile', kl_profile, 1)

@tail_recursion
def shen_profilex45help(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_profilex45help, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2122_1259 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_G_1260 = None
        KL_LOC_Profile_1261 = None
        KL_LOC_Def_1262 = None
        KL_LOC_CompileProfile_1263 = None
        KL_LOC_CompileG_1264 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_G_1260', tco_apply(kl_gensym, [symdic.symdic_shen_f])), [setattr(KL_CTX, 'KL_LOC_Profile_1261', Cons(symdic.symdic_kl_defun, Cons(car(cdr(KL_ARG_V2122_1259)), Cons(car(cdr(cdr(KL_ARG_V2122_1259))), Cons(tco_apply(shen_profilex45func, [car(cdr(KL_ARG_V2122_1259)), car(cdr(cdr(KL_ARG_V2122_1259))), Cons(KL_CTX.KL_LOC_G_1260, car(cdr(cdr(KL_ARG_V2122_1259))))]), nil))))), [setattr(KL_CTX, 'KL_LOC_Def_1262', Cons(symdic.symdic_kl_defun, Cons(KL_CTX.KL_LOC_G_1260, Cons(car(cdr(cdr(KL_ARG_V2122_1259))), Cons(tco_apply(kl_subst, [KL_CTX.KL_LOC_G_1260, car(cdr(KL_ARG_V2122_1259)), car(cdr(cdr(cdr(KL_ARG_V2122_1259))))]), nil))))), [setattr(KL_CTX, 'KL_LOC_CompileProfile_1263', tco_apply(shen_evalx45withoutx45macros, [KL_CTX.KL_LOC_Profile_1261])), [setattr(KL_CTX, 'KL_LOC_CompileG_1264', tco_apply(shen_evalx45withoutx45macros, [KL_CTX.KL_LOC_Def_1262])), car(cdr(KL_ARG_V2122_1259))][(-1)]][(-1)]][(-1)]][(-1)]][(-1)] if (((((shen_eq(nil, cdr(cdr(cdr(cdr(KL_ARG_V2122_1259))))) if shen_consp(cdr(cdr(cdr(KL_ARG_V2122_1259)))) else False) if shen_consp(cdr(cdr(KL_ARG_V2122_1259))) else False) if shen_consp(cdr(KL_ARG_V2122_1259)) else False) if shen_eq(symdic.symdic_kl_defun, car(KL_ARG_V2122_1259)) else False) if shen_consp(KL_ARG_V2122_1259) else False) else (shen_simple_error('Cannot profile.\r\n') if True else shen_simple_error('condition failure')))
shen_add_fun('shen.profile-help', shen_profilex45help, 1)

@tail_recursion
def kl_unprofile(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_unprofile, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2123_1265 = FUN_ARGS[0]
    global symdic
    return tail_call(kl_untrack, [KL_ARG_V2123_1265])
shen_add_fun('unprofile', kl_unprofile, 1)

@tail_recursion
def shen_profilex45func(*FUN_ARGS):
    FUN_ARITY = 3
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_profilex45func, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2124_1266 = FUN_ARGS[0]
    KL_ARG_V2125_1267 = FUN_ARGS[1]
    KL_ARG_V2126_1268 = FUN_ARGS[2]
    global symdic
    return Cons(symdic.symdic_kl_let, Cons(symdic.symdic_Start, Cons(Cons(symdic.symdic_kl_getx45time, Cons(symdic.symdic_kl_run, nil)), Cons(Cons(symdic.symdic_kl_let, Cons(symdic.symdic_Result, Cons(KL_ARG_V2126_1268, Cons(Cons(symdic.symdic_kl_let, Cons(symdic.symdic_Finish, Cons(Cons(symdic.symdic_kl_x45, Cons(Cons(symdic.symdic_kl_getx45time, Cons(symdic.symdic_kl_run, nil)), Cons(symdic.symdic_Start, nil))), Cons(Cons(symdic.symdic_kl_let, Cons(symdic.symdic_Record, Cons(Cons(symdic.symdic_shen_putx45profile, Cons(KL_ARG_V2124_1266, Cons(Cons(symdic.symdic_kl_x43, Cons(Cons(symdic.symdic_shen_getx45profile, Cons(KL_ARG_V2124_1266, nil)), Cons(symdic.symdic_Finish, nil))), nil))), Cons(symdic.symdic_Result, nil)))), nil)))), nil)))), nil))))
shen_add_fun('shen.profile-func', shen_profilex45func, 3)

@tail_recursion
def kl_profilex45results(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_profilex45results, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2127_1269 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Results_1270 = None
        KL_LOC_Initialise_1271 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Results_1270', tco_apply(shen_getx45profile, [KL_ARG_V2127_1269])), [setattr(KL_CTX, 'KL_LOC_Initialise_1271', tco_apply(shen_putx45profile, [KL_ARG_V2127_1269, 0])), tail_call(kl_x64p, [KL_ARG_V2127_1269, KL_CTX.KL_LOC_Results_1270])][(-1)]][(-1)]
shen_add_fun('profile-results', kl_profilex45results, 1)

@tail_recursion
def shen_getx45profile(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_getx45profile, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2128_1272 = FUN_ARGS[0]
    global symdic
    return shen_try_except((lambda : tco_apply(kl_get, [KL_ARG_V2128_1272, symdic.symdic_kl_profile, shen_get(symdic.symdic_kl_x42propertyx45vectorx42)])), (lambda KL_ARG_E_1273: 0))
shen_add_fun('shen.get-profile', shen_getx45profile, 1)

@tail_recursion
def shen_putx45profile(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_putx45profile, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2129_1274 = FUN_ARGS[0]
    KL_ARG_V2130_1275 = FUN_ARGS[1]
    global symdic
    return tail_call(kl_put, [KL_ARG_V2129_1274, symdic.symdic_kl_profile, KL_ARG_V2130_1275, shen_get(symdic.symdic_kl_x42propertyx45vectorx42)])
shen_add_fun('shen.put-profile', shen_putx45profile, 2)


#============================== load.kl==============================



@tail_recursion
def kl_load(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_load, (FUN_ARGS + lambdaargs)))
    KL_ARG_V829_1276 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Load_1277 = None
        KL_LOC_Start_1278 = None
        KL_LOC_Result_1279 = None
        KL_LOC_Finish_1280 = None
        KL_LOC_Time_1281 = None
        KL_LOC_Message_1282 = None
        KL_LOC_Infs_1283 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Load_1277', [setattr(KL_CTX, 'KL_LOC_Start_1278', shen_get_time(symdic.symdic_kl_run)), [setattr(KL_CTX, 'KL_LOC_Result_1279', tco_apply(shen_loadx45help, [shen_get(symdic.symdic_shen_x42tcx42), tco_apply(kl_readx45file, [KL_ARG_V829_1276])])), [setattr(KL_CTX, 'KL_LOC_Finish_1280', shen_get_time(symdic.symdic_kl_run)), [setattr(KL_CTX, 'KL_LOC_Time_1281', (KL_CTX.KL_LOC_Finish_1280 - KL_CTX.KL_LOC_Start_1278)), [setattr(KL_CTX, 'KL_LOC_Message_1282', tco_apply(shen_prhush, [('\r\nrun time: ' + (str(KL_CTX.KL_LOC_Time_1281) + ' secs\r\n')), tco_apply(kl_stoutput, [])])), KL_CTX.KL_LOC_Result_1279][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]), [setattr(KL_CTX, 'KL_LOC_Infs_1283', (tco_apply(shen_prhush, [('\r\ntypechecked in ' + tco_apply(shen_app, [tco_apply(kl_inferences, []), ' inferences\r\n', symdic.symdic_shen_a])), tco_apply(kl_stoutput, [])]) if shen_get(symdic.symdic_shen_x42tcx42) else symdic.symdic_shen_skip)), symdic.symdic_kl_loaded][(-1)]][(-1)]
shen_add_fun('load', kl_load, 1)

@tail_recursion
def shen_loadx45help(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_loadx45help, (FUN_ARGS + lambdaargs)))
    KL_ARG_V834_1284 = FUN_ARGS[0]
    KL_ARG_V835_1285 = FUN_ARGS[1]

    class KL_Context:
        KL_LOC_RemoveSynonyms_1287 = None
        KL_LOC_Table_1288 = None
        KL_LOC_Assume_1289 = None
    KL_CTX = KL_Context()
    global symdic
    return (tail_call(kl_map, [(lambda KL_ARG_X_1286: tail_call(shen_prhush, [tco_apply(shen_app, [tco_apply(shen_evalx45withoutx45macros, [KL_ARG_X_1286]), '\r\n', symdic.symdic_shen_s]), tco_apply(kl_stoutput, [])])), KL_ARG_V835_1285]) if shen_eq(False, KL_ARG_V834_1284) else ([setattr(KL_CTX, 'KL_LOC_RemoveSynonyms_1287', tco_apply(kl_mapcan, [symdic.symdic_shen_removex45synonyms, KL_ARG_V835_1285])), [setattr(KL_CTX, 'KL_LOC_Table_1288', tco_apply(kl_mapcan, [symdic.symdic_shen_typetable, KL_CTX.KL_LOC_RemoveSynonyms_1287])), [setattr(KL_CTX, 'KL_LOC_Assume_1289', tco_apply(kl_map, [symdic.symdic_shen_assumetype, KL_CTX.KL_LOC_Table_1288])), shen_try_except((lambda : tco_apply(kl_map, [symdic.symdic_shen_typecheckx45andx45load, KL_CTX.KL_LOC_RemoveSynonyms_1287])), (lambda KL_ARG_E_1290: tail_call(shen_unwindx45types, [KL_ARG_E_1290, KL_CTX.KL_LOC_Table_1288])))][(-1)]][(-1)]][(-1)] if True else shen_simple_error('condition failure')))
shen_add_fun('shen.load-help', shen_loadx45help, 2)

@tail_recursion
def shen_removex45synonyms(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_removex45synonyms, (FUN_ARGS + lambdaargs)))
    KL_ARG_V836_1291 = FUN_ARGS[0]
    global symdic
    return ([tco_apply(kl_eval, [KL_ARG_V836_1291]), nil][(-1)] if (shen_eq(symdic.symdic_shen_synonymsx45help, car(KL_ARG_V836_1291)) if shen_consp(KL_ARG_V836_1291) else False) else (Cons(KL_ARG_V836_1291, nil) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.remove-synonyms', shen_removex45synonyms, 1)

@tail_recursion
def shen_typecheckx45andx45load(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_typecheckx45andx45load, (FUN_ARGS + lambdaargs)))
    KL_ARG_V837_1292 = FUN_ARGS[0]
    global symdic
    return [tco_apply(kl_nl, [1]), tail_call(shen_typecheckx45andx45evaluate, [KL_ARG_V837_1292, tco_apply(kl_gensym, [symdic.symdic_A])])][(-1)]
shen_add_fun('shen.typecheck-and-load', shen_typecheckx45andx45load, 1)

@tail_recursion
def shen_typetable(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_typetable, (FUN_ARGS + lambdaargs)))
    KL_ARG_V846_1293 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Sig_1294 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_Sig_1294', tco_apply(kl_compile, [symdic.symdic_shen_x60sigx43restx62, cdr(cdr(KL_ARG_V846_1293)), nil])), (shen_simple_error(tco_apply(shen_app, [car(cdr(KL_ARG_V846_1293)), ' lacks a proper signature.\r\n', symdic.symdic_shen_a])) if shen_eq(KL_CTX.KL_LOC_Sig_1294, tco_apply(kl_fail, [])) else Cons(Cons(car(cdr(KL_ARG_V846_1293)), KL_CTX.KL_LOC_Sig_1294), nil))][(-1)] if ((shen_consp(cdr(KL_ARG_V846_1293)) if shen_eq(symdic.symdic_kl_define, car(KL_ARG_V846_1293)) else False) if shen_consp(KL_ARG_V846_1293) else False) else (Cons(Cons(car(cdr(KL_ARG_V846_1293)), Cons(car(cdr(cdr(cdr(KL_ARG_V846_1293)))), Cons(symdic.symdic_kl_x61x61x62, Cons(car(cdr(cdr(cdr(cdr(cdr(KL_ARG_V846_1293)))))), nil)))), nil) if ((((((((((((((shen_eq(symdic.symdic_kl_x125, car(cdr(cdr(cdr(cdr(cdr(cdr(KL_ARG_V846_1293)))))))) if shen_consp(cdr(cdr(cdr(cdr(cdr(cdr(KL_ARG_V846_1293))))))) else False) if shen_consp(cdr(cdr(cdr(cdr(cdr(KL_ARG_V846_1293)))))) else False) if shen_eq(symdic.symdic_kl_x61x61x62, car(cdr(cdr(cdr(cdr(KL_ARG_V846_1293)))))) else False) if shen_consp(cdr(cdr(cdr(cdr(KL_ARG_V846_1293))))) else False) if shen_eq(nil, cdr(cdr(car(cdr(cdr(cdr(KL_ARG_V846_1293))))))) else False) if shen_consp(cdr(car(cdr(cdr(cdr(KL_ARG_V846_1293)))))) else False) if shen_eq(symdic.symdic_kl_list, car(car(cdr(cdr(cdr(KL_ARG_V846_1293)))))) else False) if shen_consp(car(cdr(cdr(cdr(KL_ARG_V846_1293))))) else False) if shen_consp(cdr(cdr(cdr(KL_ARG_V846_1293)))) else False) if shen_eq(symdic.symdic_kl_x123, car(cdr(cdr(KL_ARG_V846_1293)))) else False) if shen_consp(cdr(cdr(KL_ARG_V846_1293))) else False) if shen_consp(cdr(KL_ARG_V846_1293)) else False) if shen_eq(symdic.symdic_kl_defcc, car(KL_ARG_V846_1293)) else False) if shen_consp(KL_ARG_V846_1293) else False) else (shen_simple_error(tco_apply(shen_app, [car(cdr(KL_ARG_V846_1293)), ' lacks a proper signature.\r\n', symdic.symdic_shen_a])) if ((shen_consp(cdr(KL_ARG_V846_1293)) if shen_eq(symdic.symdic_kl_defcc, car(KL_ARG_V846_1293)) else False) if shen_consp(KL_ARG_V846_1293) else False) else (nil if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.typetable', shen_typetable, 1)

@tail_recursion
def shen_assumetype(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_assumetype, (FUN_ARGS + lambdaargs)))
    KL_ARG_V847_1295 = FUN_ARGS[0]
    global symdic
    return (apply(kl_declare, [car(KL_ARG_V847_1295), cdr(KL_ARG_V847_1295)]) if shen_consp(KL_ARG_V847_1295) else (tail_call(shen_sysx45error, [symdic.symdic_shen_assumetype]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.assumetype', shen_assumetype, 1)

@tail_recursion
def shen_unwindx45types(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_unwindx45types, (FUN_ARGS + lambdaargs)))
    KL_ARG_V852_1296 = FUN_ARGS[0]
    KL_ARG_V853_1297 = FUN_ARGS[1]
    global symdic
    return (shen_simple_error(KL_ARG_V852_1296.message) if shen_eq(nil, KL_ARG_V853_1297) else ([tco_apply(shen_remtype, [car(car(KL_ARG_V853_1297))]), tail_call(shen_unwindx45types, [KL_ARG_V852_1296, cdr(KL_ARG_V853_1297)])][(-1)] if (shen_consp(car(KL_ARG_V853_1297)) if shen_consp(KL_ARG_V853_1297) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_unwindx45types]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.unwind-types', shen_unwindx45types, 2)

@tail_recursion
def shen_remtype(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_remtype, (FUN_ARGS + lambdaargs)))
    KL_ARG_V854_1298 = FUN_ARGS[0]
    global symdic
    return shen_set(symdic.symdic_shen_x42signedfuncsx42, tco_apply(shen_removetype, [KL_ARG_V854_1298, shen_get(symdic.symdic_shen_x42signedfuncsx42)]))
shen_add_fun('shen.remtype', shen_remtype, 1)

@tail_recursion
def shen_removetype(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_removetype, (FUN_ARGS + lambdaargs)))
    KL_ARG_V859_1299 = FUN_ARGS[0]
    KL_ARG_V860_1300 = FUN_ARGS[1]
    global symdic
    return (nil if shen_eq(nil, KL_ARG_V860_1300) else (tail_call(shen_removetype, [car(car(KL_ARG_V860_1300)), cdr(KL_ARG_V860_1300)]) if ((shen_eq(car(car(KL_ARG_V860_1300)), KL_ARG_V859_1299) if shen_consp(car(KL_ARG_V860_1300)) else False) if shen_consp(KL_ARG_V860_1300) else False) else (Cons(car(KL_ARG_V860_1300), tco_apply(shen_removetype, [KL_ARG_V859_1299, cdr(KL_ARG_V860_1300)])) if shen_consp(KL_ARG_V860_1300) else (tail_call(shen_sysx45error, [symdic.symdic_shen_removetype]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.removetype', shen_removetype, 2)

@tail_recursion
def shen_x60sigx43restx62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60sigx43restx62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V866_1301 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_1302 = None
        KL_LOC_Parse_shen_x60signaturex62_1303 = None
        KL_LOC_Parse_x60x33x62_1304 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_1302', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60signaturex62_1303', tco_apply(shen_x60signaturex62, [KL_ARG_V866_1301])), ([setattr(KL_CTX, 'KL_LOC_Parse_x60x33x62_1304', tco_apply(x60x33x62, [KL_CTX.KL_LOC_Parse_shen_x60signaturex62_1303])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_x60x33x62_1304), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60signaturex62_1303])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_x60x33x62_1304)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60signaturex62_1303)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_1302, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_1302)][(-1)]
shen_add_fun('shen.<sig+rest>', shen_x60sigx43restx62, 1)

@tail_recursion
def kl_writex45tox45file(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_writex45tox45file, (FUN_ARGS + lambdaargs)))
    KL_ARG_V867_1305 = FUN_ARGS[0]
    KL_ARG_V868_1306 = FUN_ARGS[1]

    class KL_Context:
        KL_LOC_Stream_1307 = None
        KL_LOC_String_1308 = None
        KL_LOC_Write_1309 = None
        KL_LOC_Close_1310 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Stream_1307', shen_open(symdic.symdic_kl_file, KL_ARG_V867_1305, symdic.symdic_kl_out)), [setattr(KL_CTX, 'KL_LOC_String_1308', (tco_apply(shen_app, [KL_ARG_V868_1306, '\r\n\r\n', symdic.symdic_shen_a]) if isinstance(KL_ARG_V868_1306, str) else tco_apply(shen_app, [KL_ARG_V868_1306, '\r\n\r\n', symdic.symdic_shen_s]))), [setattr(KL_CTX, 'KL_LOC_Write_1309', shen_pr(KL_CTX.KL_LOC_String_1308, KL_CTX.KL_LOC_Stream_1307)), [setattr(KL_CTX, 'KL_LOC_Close_1310', shen_close(KL_CTX.KL_LOC_Stream_1307)), KL_ARG_V868_1306][(-1)]][(-1)]][(-1)]][(-1)]
shen_add_fun('write-to-file', kl_writex45tox45file, 2)


#============================== writer.kl==============================



@tail_recursion
def kl_print(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_print, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2238_1311 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_String_1312 = None
        KL_LOC_Print_1313 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_String_1312', tco_apply(shen_insert, [KL_ARG_V2238_1311, '~S'])), [setattr(KL_CTX, 'KL_LOC_Print_1313', tco_apply(shen_prhush, [KL_CTX.KL_LOC_String_1312, tco_apply(kl_stoutput, [])])), KL_ARG_V2238_1311][(-1)]][(-1)]
shen_add_fun('print', kl_print, 1)

@tail_recursion
def shen_prhush(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_prhush, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2239_1314 = FUN_ARGS[0]
    KL_ARG_V2240_1315 = FUN_ARGS[1]
    global symdic
    return (KL_ARG_V2239_1314 if shen_get(symdic.symdic_x42hushx42) else shen_pr(KL_ARG_V2239_1314, KL_ARG_V2240_1315))
shen_add_fun('shen.prhush', shen_prhush, 2)

@tail_recursion
def shen_mkstr(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_mkstr, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2241_1316 = FUN_ARGS[0]
    KL_ARG_V2242_1317 = FUN_ARGS[1]
    global symdic
    return (tail_call(shen_mkstrx45l, [tco_apply(shen_procx45nl, [KL_ARG_V2241_1316]), KL_ARG_V2242_1317]) if isinstance(KL_ARG_V2241_1316, str) else (tail_call(shen_mkstrx45r, [Cons(symdic.symdic_shen_procx45nl, Cons(KL_ARG_V2241_1316, nil)), KL_ARG_V2242_1317]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.mkstr', shen_mkstr, 2)

@tail_recursion
def shen_mkstrx45l(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_mkstrx45l, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2243_1318 = FUN_ARGS[0]
    KL_ARG_V2244_1319 = FUN_ARGS[1]
    global symdic
    return (KL_ARG_V2243_1318 if shen_eq(nil, KL_ARG_V2244_1319) else (tail_call(shen_mkstrx45l, [tco_apply(shen_insertx45l, [car(KL_ARG_V2244_1319), KL_ARG_V2243_1318]), cdr(KL_ARG_V2244_1319)]) if shen_consp(KL_ARG_V2244_1319) else (tail_call(shen_sysx45error, [symdic.symdic_shen_mkstrx45l]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.mkstr-l', shen_mkstrx45l, 2)

@tail_recursion
def shen_insertx45l(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_insertx45l, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2247_1320 = FUN_ARGS[0]
    KL_ARG_V2248_1321 = FUN_ARGS[1]
    global symdic
    return ('' if shen_eq('', KL_ARG_V2248_1321) else (Cons(symdic.symdic_shen_app, Cons(KL_ARG_V2247_1320, Cons(KL_ARG_V2248_1321[1:][1:], Cons(symdic.symdic_shen_a, nil)))) if (((shen_eq('A', KL_ARG_V2248_1321[1:][0]) if tco_apply(shen_x43stringx63, [KL_ARG_V2248_1321[1:]]) else False) if shen_eq('~', KL_ARG_V2248_1321[0]) else False) if tco_apply(shen_x43stringx63, [KL_ARG_V2248_1321]) else False) else (Cons(symdic.symdic_shen_app, Cons(KL_ARG_V2247_1320, Cons(KL_ARG_V2248_1321[1:][1:], Cons(symdic.symdic_shen_r, nil)))) if (((shen_eq('R', KL_ARG_V2248_1321[1:][0]) if tco_apply(shen_x43stringx63, [KL_ARG_V2248_1321[1:]]) else False) if shen_eq('~', KL_ARG_V2248_1321[0]) else False) if tco_apply(shen_x43stringx63, [KL_ARG_V2248_1321]) else False) else (Cons(symdic.symdic_shen_app, Cons(KL_ARG_V2247_1320, Cons(KL_ARG_V2248_1321[1:][1:], Cons(symdic.symdic_shen_s, nil)))) if (((shen_eq('S', KL_ARG_V2248_1321[1:][0]) if tco_apply(shen_x43stringx63, [KL_ARG_V2248_1321[1:]]) else False) if shen_eq('~', KL_ARG_V2248_1321[0]) else False) if tco_apply(shen_x43stringx63, [KL_ARG_V2248_1321]) else False) else (tail_call(shen_factorx45cn, [Cons(symdic.symdic_kl_cn, Cons(KL_ARG_V2248_1321[0], Cons(tco_apply(shen_insertx45l, [KL_ARG_V2247_1320, KL_ARG_V2248_1321[1:]]), nil)))]) if tco_apply(shen_x43stringx63, [KL_ARG_V2248_1321]) else (Cons(symdic.symdic_kl_cn, Cons(car(cdr(KL_ARG_V2248_1321)), Cons(tco_apply(shen_insertx45l, [KL_ARG_V2247_1320, car(cdr(cdr(KL_ARG_V2248_1321)))]), nil))) if ((((shen_eq(nil, cdr(cdr(cdr(KL_ARG_V2248_1321)))) if shen_consp(cdr(cdr(KL_ARG_V2248_1321))) else False) if shen_consp(cdr(KL_ARG_V2248_1321)) else False) if shen_eq(symdic.symdic_kl_cn, car(KL_ARG_V2248_1321)) else False) if shen_consp(KL_ARG_V2248_1321) else False) else (Cons(symdic.symdic_shen_app, Cons(car(cdr(KL_ARG_V2248_1321)), Cons(tco_apply(shen_insertx45l, [KL_ARG_V2247_1320, car(cdr(cdr(KL_ARG_V2248_1321)))]), cdr(cdr(cdr(KL_ARG_V2248_1321)))))) if (((((shen_eq(nil, cdr(cdr(cdr(cdr(KL_ARG_V2248_1321))))) if shen_consp(cdr(cdr(cdr(KL_ARG_V2248_1321)))) else False) if shen_consp(cdr(cdr(KL_ARG_V2248_1321))) else False) if shen_consp(cdr(KL_ARG_V2248_1321)) else False) if shen_eq(symdic.symdic_shen_app, car(KL_ARG_V2248_1321)) else False) if shen_consp(KL_ARG_V2248_1321) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_insertx45l]) if True else shen_simple_error('condition failure')))))))))
shen_add_fun('shen.insert-l', shen_insertx45l, 2)

@tail_recursion
def shen_factorx45cn(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_factorx45cn, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2249_1322 = FUN_ARGS[0]
    global symdic
    return (Cons(symdic.symdic_kl_cn, Cons((car(cdr(KL_ARG_V2249_1322)) + car(cdr(car(cdr(cdr(KL_ARG_V2249_1322)))))), cdr(cdr(car(cdr(cdr(KL_ARG_V2249_1322))))))) if (((((((((((isinstance(car(cdr(car(cdr(cdr(KL_ARG_V2249_1322))))), str) if isinstance(car(cdr(KL_ARG_V2249_1322)), str) else False) if shen_eq(nil, cdr(cdr(cdr(KL_ARG_V2249_1322)))) else False) if shen_eq(nil, cdr(cdr(cdr(car(cdr(cdr(KL_ARG_V2249_1322))))))) else False) if shen_consp(cdr(cdr(car(cdr(cdr(KL_ARG_V2249_1322)))))) else False) if shen_consp(cdr(car(cdr(cdr(KL_ARG_V2249_1322))))) else False) if shen_eq(symdic.symdic_kl_cn, car(car(cdr(cdr(KL_ARG_V2249_1322))))) else False) if shen_consp(car(cdr(cdr(KL_ARG_V2249_1322)))) else False) if shen_consp(cdr(cdr(KL_ARG_V2249_1322))) else False) if shen_consp(cdr(KL_ARG_V2249_1322)) else False) if shen_eq(symdic.symdic_kl_cn, car(KL_ARG_V2249_1322)) else False) if shen_consp(KL_ARG_V2249_1322) else False) else (KL_ARG_V2249_1322 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.factor-cn', shen_factorx45cn, 1)

@tail_recursion
def shen_procx45nl(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_procx45nl, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2250_1323 = FUN_ARGS[0]
    global symdic
    return ('' if shen_eq('', KL_ARG_V2250_1323) else ((chr(10) + tco_apply(shen_procx45nl, [KL_ARG_V2250_1323[1:][1:]])) if (((shen_eq('%', KL_ARG_V2250_1323[1:][0]) if tco_apply(shen_x43stringx63, [KL_ARG_V2250_1323[1:]]) else False) if shen_eq('~', KL_ARG_V2250_1323[0]) else False) if tco_apply(shen_x43stringx63, [KL_ARG_V2250_1323]) else False) else ((KL_ARG_V2250_1323[0] + tco_apply(shen_procx45nl, [KL_ARG_V2250_1323[1:]])) if tco_apply(shen_x43stringx63, [KL_ARG_V2250_1323]) else (tail_call(shen_sysx45error, [symdic.symdic_shen_procx45nl]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.proc-nl', shen_procx45nl, 1)

@tail_recursion
def shen_mkstrx45r(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_mkstrx45r, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2251_1324 = FUN_ARGS[0]
    KL_ARG_V2252_1325 = FUN_ARGS[1]
    global symdic
    return (KL_ARG_V2251_1324 if shen_eq(nil, KL_ARG_V2252_1325) else (tail_call(shen_mkstrx45r, [Cons(symdic.symdic_shen_insert, Cons(car(KL_ARG_V2252_1325), Cons(KL_ARG_V2251_1324, nil))), cdr(KL_ARG_V2252_1325)]) if shen_consp(KL_ARG_V2252_1325) else (tail_call(shen_sysx45error, [symdic.symdic_shen_mkstrx45r]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.mkstr-r', shen_mkstrx45r, 2)

@tail_recursion
def shen_insert(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_insert, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2253_1326 = FUN_ARGS[0]
    KL_ARG_V2254_1327 = FUN_ARGS[1]
    global symdic
    return tail_call(shen_insertx45h, [KL_ARG_V2253_1326, KL_ARG_V2254_1327, ''])
shen_add_fun('shen.insert', shen_insert, 2)

@tail_recursion
def shen_insertx45h(*FUN_ARGS):
    FUN_ARITY = 3
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_insertx45h, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2257_1328 = FUN_ARGS[0]
    KL_ARG_V2258_1329 = FUN_ARGS[1]
    KL_ARG_V2259_1330 = FUN_ARGS[2]
    global symdic
    return (KL_ARG_V2259_1330 if shen_eq('', KL_ARG_V2258_1329) else ((KL_ARG_V2259_1330 + tco_apply(shen_app, [KL_ARG_V2257_1328, KL_ARG_V2258_1329[1:][1:], symdic.symdic_shen_a])) if (((shen_eq('A', KL_ARG_V2258_1329[1:][0]) if tco_apply(shen_x43stringx63, [KL_ARG_V2258_1329[1:]]) else False) if shen_eq('~', KL_ARG_V2258_1329[0]) else False) if tco_apply(shen_x43stringx63, [KL_ARG_V2258_1329]) else False) else ((KL_ARG_V2259_1330 + tco_apply(shen_app, [KL_ARG_V2257_1328, KL_ARG_V2258_1329[1:][1:], symdic.symdic_shen_r])) if (((shen_eq('R', KL_ARG_V2258_1329[1:][0]) if tco_apply(shen_x43stringx63, [KL_ARG_V2258_1329[1:]]) else False) if shen_eq('~', KL_ARG_V2258_1329[0]) else False) if tco_apply(shen_x43stringx63, [KL_ARG_V2258_1329]) else False) else ((KL_ARG_V2259_1330 + tco_apply(shen_app, [KL_ARG_V2257_1328, KL_ARG_V2258_1329[1:][1:], symdic.symdic_shen_s])) if (((shen_eq('S', KL_ARG_V2258_1329[1:][0]) if tco_apply(shen_x43stringx63, [KL_ARG_V2258_1329[1:]]) else False) if shen_eq('~', KL_ARG_V2258_1329[0]) else False) if tco_apply(shen_x43stringx63, [KL_ARG_V2258_1329]) else False) else (tail_call(shen_insertx45h, [KL_ARG_V2257_1328, KL_ARG_V2258_1329[1:], (KL_ARG_V2259_1330 + KL_ARG_V2258_1329[0])]) if tco_apply(shen_x43stringx63, [KL_ARG_V2258_1329]) else (tail_call(shen_sysx45error, [symdic.symdic_shen_insertx45h]) if True else shen_simple_error('condition failure')))))))
shen_add_fun('shen.insert-h', shen_insertx45h, 3)

@tail_recursion
def shen_app(*FUN_ARGS):
    FUN_ARITY = 3
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_app, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2260_1331 = FUN_ARGS[0]
    KL_ARG_V2261_1332 = FUN_ARGS[1]
    KL_ARG_V2262_1333 = FUN_ARGS[2]
    global symdic
    return (tco_apply(shen_argx45x62str, [KL_ARG_V2260_1331, KL_ARG_V2262_1333]) + KL_ARG_V2261_1332)
shen_add_fun('shen.app', shen_app, 3)

@tail_recursion
def shen_argx45x62str(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_argx45x62str, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2268_1334 = FUN_ARGS[0]
    KL_ARG_V2269_1335 = FUN_ARGS[1]
    global symdic
    return ('...' if shen_eq(KL_ARG_V2268_1334, tco_apply(kl_fail, [])) else (tail_call(shen_listx45x62str, [KL_ARG_V2268_1334, KL_ARG_V2269_1335]) if tco_apply(shen_listx63, [KL_ARG_V2268_1334]) else (tail_call(shen_strx45x62str, [KL_ARG_V2268_1334, KL_ARG_V2269_1335]) if isinstance(KL_ARG_V2268_1334, str) else (tail_call(shen_vectorx45x62str, [KL_ARG_V2268_1334, KL_ARG_V2269_1335]) if shen_absvectorp(KL_ARG_V2268_1334) else (tail_call(shen_atomx45x62str, [KL_ARG_V2268_1334]) if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.arg->str', shen_argx45x62str, 2)

@tail_recursion
def shen_listx45x62str(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_listx45x62str, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2270_1336 = FUN_ARGS[0]
    KL_ARG_V2271_1337 = FUN_ARGS[1]
    global symdic
    return (tail_call(kl_x64s, ['(', tco_apply(kl_x64s, [tco_apply(shen_iterx45list, [KL_ARG_V2270_1336, symdic.symdic_shen_r, tco_apply(shen_maxseq, [])]), ')'])]) if shen_eq(symdic.symdic_shen_r, KL_ARG_V2271_1337) else (tail_call(kl_x64s, ['[', tco_apply(kl_x64s, [tco_apply(shen_iterx45list, [KL_ARG_V2270_1336, KL_ARG_V2271_1337, tco_apply(shen_maxseq, [])]), ']'])]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.list->str', shen_listx45x62str, 2)

@tail_recursion
def shen_maxseq(*FUN_ARGS):
    FUN_ARITY = 0
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_maxseq, (FUN_ARGS + lambdaargs)))
    global symdic
    return shen_get(symdic.symdic_kl_x42maximumx45printx45sequencex45sizex42)
shen_add_fun('shen.maxseq', shen_maxseq, 0)

@tail_recursion
def shen_iterx45list(*FUN_ARGS):
    FUN_ARITY = 3
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_iterx45list, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2282_1338 = FUN_ARGS[0]
    KL_ARG_V2283_1339 = FUN_ARGS[1]
    KL_ARG_V2284_1340 = FUN_ARGS[2]
    global symdic
    return ('' if shen_eq(nil, KL_ARG_V2282_1338) else ('... etc' if shen_eq(0, KL_ARG_V2284_1340) else (tail_call(shen_argx45x62str, [car(KL_ARG_V2282_1338), KL_ARG_V2283_1339]) if (shen_eq(nil, cdr(KL_ARG_V2282_1338)) if shen_consp(KL_ARG_V2282_1338) else False) else (tail_call(kl_x64s, [tco_apply(shen_argx45x62str, [car(KL_ARG_V2282_1338), KL_ARG_V2283_1339]), tco_apply(kl_x64s, [' ', tco_apply(shen_iterx45list, [cdr(KL_ARG_V2282_1338), KL_ARG_V2283_1339, (KL_ARG_V2284_1340 - 1)])])]) if shen_consp(KL_ARG_V2282_1338) else (tail_call(kl_x64s, ['|', tco_apply(kl_x64s, [' ', tco_apply(shen_argx45x62str, [KL_ARG_V2282_1338, KL_ARG_V2283_1339])])]) if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.iter-list', shen_iterx45list, 3)

@tail_recursion
def shen_strx45x62str(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_strx45x62str, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2289_1341 = FUN_ARGS[0]
    KL_ARG_V2290_1342 = FUN_ARGS[1]
    global symdic
    return (KL_ARG_V2289_1341 if shen_eq(symdic.symdic_shen_a, KL_ARG_V2290_1342) else (tail_call(kl_x64s, [chr(34), tco_apply(kl_x64s, [KL_ARG_V2289_1341, chr(34)])]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.str->str', shen_strx45x62str, 2)

@tail_recursion
def shen_vectorx45x62str(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_vectorx45x62str, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2291_1343 = FUN_ARGS[0]
    KL_ARG_V2292_1344 = FUN_ARGS[1]
    global symdic
    return (tail_call(shen_absvector_get(KL_ARG_V2291_1343, 0), [KL_ARG_V2291_1343]) if tco_apply(shen_printx45vectorx63, [KL_ARG_V2291_1343]) else (tail_call(kl_x64s, ['<', tco_apply(kl_x64s, [tco_apply(shen_iterx45vector, [KL_ARG_V2291_1343, 1, KL_ARG_V2292_1344, tco_apply(shen_maxseq, [])]), '>'])]) if tco_apply(kl_vectorx63, [KL_ARG_V2291_1343]) else tail_call(kl_x64s, ['<', tco_apply(kl_x64s, ['<', tco_apply(kl_x64s, [tco_apply(shen_iterx45vector, [KL_ARG_V2291_1343, 0, KL_ARG_V2292_1344, tco_apply(shen_maxseq, [])]), '>>'])])])))
shen_add_fun('shen.vector->str', shen_vectorx45x62str, 2)

@tail_recursion
def shen_printx45vectorx63(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_printx45vectorx63, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2293_1345 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Zero_1346 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Zero_1346', shen_absvector_get(KL_ARG_V2293_1345, 0)), (True if shen_eq(KL_CTX.KL_LOC_Zero_1346, symdic.symdic_shen_tuple) else (True if shen_eq(KL_CTX.KL_LOC_Zero_1346, symdic.symdic_shen_pvar) else (tail_call(shen_fboundx63, [KL_CTX.KL_LOC_Zero_1346]) if (not isinstance(KL_CTX.KL_LOC_Zero_1346, numbers.Number)) else False)))][(-1)]
shen_add_fun('shen.print-vector?', shen_printx45vectorx63, 1)

@tail_recursion
def shen_fboundx63(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_fboundx63, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2294_1347 = FUN_ARGS[0]
    global symdic
    return shen_try_except((lambda : [tco_apply(kl_ps, [KL_ARG_V2294_1347]), True][(-1)]), (lambda KL_ARG_E_1348: False))
shen_add_fun('shen.fbound?', shen_fboundx63, 1)

@tail_recursion
def shen_tuple(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_tuple, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2295_1349 = FUN_ARGS[0]
    global symdic
    return ('(@p ' + tco_apply(shen_app, [shen_absvector_get(KL_ARG_V2295_1349, 1), (' ' + tco_apply(shen_app, [shen_absvector_get(KL_ARG_V2295_1349, 2), ')', symdic.symdic_shen_s])), symdic.symdic_shen_s]))
shen_add_fun('shen.tuple', shen_tuple, 1)

@tail_recursion
def shen_iterx45vector(*FUN_ARGS):
    FUN_ARITY = 4
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_iterx45vector, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2302_1350 = FUN_ARGS[0]
    KL_ARG_V2303_1351 = FUN_ARGS[1]
    KL_ARG_V2304_1352 = FUN_ARGS[2]
    KL_ARG_V2305_1353 = FUN_ARGS[3]

    class KL_Context:
        KL_LOC_Item_1354 = None
        KL_LOC_Next_1356 = None
    KL_CTX = KL_Context()
    global symdic
    return ('... etc' if shen_eq(0, KL_ARG_V2305_1353) else ([setattr(KL_CTX, 'KL_LOC_Item_1354', shen_try_except((lambda : shen_absvector_get(KL_ARG_V2302_1350, KL_ARG_V2303_1351)), (lambda KL_ARG_E_1355: symdic.symdic_shen_outx45ofx45bounds))), [setattr(KL_CTX, 'KL_LOC_Next_1356', shen_try_except((lambda : shen_absvector_get(KL_ARG_V2302_1350, (KL_ARG_V2303_1351 + 1))), (lambda KL_ARG_E_1357: symdic.symdic_shen_outx45ofx45bounds))), ('' if shen_eq(KL_CTX.KL_LOC_Item_1354, symdic.symdic_shen_outx45ofx45bounds) else (tail_call(shen_argx45x62str, [KL_CTX.KL_LOC_Item_1354, KL_ARG_V2304_1352]) if shen_eq(KL_CTX.KL_LOC_Next_1356, symdic.symdic_shen_outx45ofx45bounds) else tail_call(kl_x64s, [tco_apply(shen_argx45x62str, [KL_CTX.KL_LOC_Item_1354, KL_ARG_V2304_1352]), tco_apply(kl_x64s, [' ', tco_apply(shen_iterx45vector, [KL_ARG_V2302_1350, (KL_ARG_V2303_1351 + 1), KL_ARG_V2304_1352, (KL_ARG_V2305_1353 - 1)])])])))][(-1)]][(-1)] if True else shen_simple_error('condition failure')))
shen_add_fun('shen.iter-vector', shen_iterx45vector, 4)

@tail_recursion
def shen_atomx45x62str(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_atomx45x62str, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2306_1358 = FUN_ARGS[0]
    global symdic
    return shen_try_except((lambda : str(KL_ARG_V2306_1358)), (lambda KL_ARG_E_1359: tail_call(shen_funexstring, [])))
shen_add_fun('shen.atom->str', shen_atomx45x62str, 1)

@tail_recursion
def shen_funexstring(*FUN_ARGS):
    FUN_ARITY = 0
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_funexstring, (FUN_ARGS + lambdaargs)))
    global symdic
    return tail_call(kl_x64s, ['\x10', tco_apply(kl_x64s, ['f', tco_apply(kl_x64s, ['u', tco_apply(kl_x64s, ['n', tco_apply(kl_x64s, ['e', tco_apply(kl_x64s, [tco_apply(shen_argx45x62str, [tco_apply(kl_gensym, [shen_intern('x')]), symdic.symdic_shen_a]), '\x11'])])])])])])
shen_add_fun('shen.funexstring', shen_funexstring, 0)

@tail_recursion
def shen_listx63(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_listx63, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2307_1360 = FUN_ARGS[0]
    global symdic
    return (True if tco_apply(kl_emptyx63, [KL_ARG_V2307_1360]) else shen_consp(KL_ARG_V2307_1360))
shen_add_fun('shen.list?', shen_listx63, 1)


#============================== macros.kl==============================



@tail_recursion
def kl_macroexpand(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_macroexpand, (FUN_ARGS + lambdaargs)))
    KL_ARG_V869_1361 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Y_1362 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Y_1362', tco_apply(shen_compose, [shen_get(symdic.symdic_kl_x42macrosx42), KL_ARG_V869_1361])), (KL_ARG_V869_1361 if shen_eq(KL_ARG_V869_1361, KL_CTX.KL_LOC_Y_1362) else tail_call(shen_walk, [symdic.symdic_kl_macroexpand, KL_CTX.KL_LOC_Y_1362]))][(-1)]
shen_add_fun('macroexpand', kl_macroexpand, 1)
shen_set(symdic.symdic_kl_x42macrosx42, Cons(symdic.symdic_shen_timerx45macro, Cons(symdic.symdic_shen_casesx45macro, Cons(symdic.symdic_shen_absx45macro, Cons(symdic.symdic_shen_putx47getx45macro, Cons(symdic.symdic_shen_compilex45macro, Cons(symdic.symdic_shen_datatypex45macro, Cons(symdic.symdic_shen_letx45macro, Cons(symdic.symdic_shen_assocx45macro, Cons(symdic.symdic_shen_makex45stringx45macro, Cons(symdic.symdic_shen_outputx45macro, Cons(symdic.symdic_shen_errorx45macro, Cons(symdic.symdic_shen_prologx45macro, Cons(symdic.symdic_shen_synonymsx45macro, Cons(symdic.symdic_shen_nlx45macro, Cons(symdic.symdic_shen_x64sx45macro, Cons(symdic.symdic_shen_defmacrox45macro, Cons(symdic.symdic_shen_defprologx45macro, Cons(symdic.symdic_shen_functionx45macro, nil)))))))))))))))))))

@tail_recursion
def shen_errorx45macro(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_errorx45macro, (FUN_ARGS + lambdaargs)))
    KL_ARG_V870_1363 = FUN_ARGS[0]
    global symdic
    return (Cons(symdic.symdic_kl_simplex45error, Cons(tco_apply(shen_mkstr, [car(cdr(KL_ARG_V870_1363)), cdr(cdr(KL_ARG_V870_1363))]), nil)) if ((shen_consp(cdr(KL_ARG_V870_1363)) if shen_eq(symdic.symdic_kl_error, car(KL_ARG_V870_1363)) else False) if shen_consp(KL_ARG_V870_1363) else False) else (KL_ARG_V870_1363 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.error-macro', shen_errorx45macro, 1)

@tail_recursion
def shen_outputx45macro(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_outputx45macro, (FUN_ARGS + lambdaargs)))
    KL_ARG_V871_1364 = FUN_ARGS[0]
    global symdic
    return (Cons(symdic.symdic_shen_prhush, Cons(tco_apply(shen_mkstr, [car(cdr(KL_ARG_V871_1364)), cdr(cdr(KL_ARG_V871_1364))]), Cons(Cons(symdic.symdic_kl_stoutput, nil), nil))) if ((shen_consp(cdr(KL_ARG_V871_1364)) if shen_eq(symdic.symdic_kl_output, car(KL_ARG_V871_1364)) else False) if shen_consp(KL_ARG_V871_1364) else False) else (KL_ARG_V871_1364 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.output-macro', shen_outputx45macro, 1)

@tail_recursion
def shen_makex45stringx45macro(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_makex45stringx45macro, (FUN_ARGS + lambdaargs)))
    KL_ARG_V872_1365 = FUN_ARGS[0]
    global symdic
    return (tail_call(shen_mkstr, [car(cdr(KL_ARG_V872_1365)), cdr(cdr(KL_ARG_V872_1365))]) if ((shen_consp(cdr(KL_ARG_V872_1365)) if shen_eq(symdic.symdic_kl_makex45string, car(KL_ARG_V872_1365)) else False) if shen_consp(KL_ARG_V872_1365) else False) else (KL_ARG_V872_1365 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.make-string-macro', shen_makex45stringx45macro, 1)

@tail_recursion
def shen_compose(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_compose, (FUN_ARGS + lambdaargs)))
    KL_ARG_V873_1366 = FUN_ARGS[0]
    KL_ARG_V874_1367 = FUN_ARGS[1]
    global symdic
    return (KL_ARG_V874_1367 if shen_eq(nil, KL_ARG_V873_1366) else (tail_call(shen_compose, [cdr(KL_ARG_V873_1366), tco_apply(car(KL_ARG_V873_1366), [KL_ARG_V874_1367])]) if shen_consp(KL_ARG_V873_1366) else (tail_call(shen_sysx45error, [symdic.symdic_shen_compose]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.compose', shen_compose, 2)

@tail_recursion
def shen_compilex45macro(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_compilex45macro, (FUN_ARGS + lambdaargs)))
    KL_ARG_V875_1368 = FUN_ARGS[0]
    global symdic
    return (Cons(symdic.symdic_kl_compile, Cons(car(cdr(KL_ARG_V875_1368)), Cons(car(cdr(cdr(KL_ARG_V875_1368))), Cons(Cons(symdic.symdic_kl_lambda, Cons(symdic.symdic_E, Cons(Cons(symdic.symdic_kl_if, Cons(Cons(symdic.symdic_kl_consx63, Cons(symdic.symdic_E, nil)), Cons(Cons(symdic.symdic_kl_error, Cons('parse error here: ~S~%', Cons(symdic.symdic_E, nil))), Cons(Cons(symdic.symdic_kl_error, Cons('parse error~%', nil)), nil)))), nil))), nil)))) if ((((shen_eq(nil, cdr(cdr(cdr(KL_ARG_V875_1368)))) if shen_consp(cdr(cdr(KL_ARG_V875_1368))) else False) if shen_consp(cdr(KL_ARG_V875_1368)) else False) if shen_eq(symdic.symdic_kl_compile, car(KL_ARG_V875_1368)) else False) if shen_consp(KL_ARG_V875_1368) else False) else (KL_ARG_V875_1368 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.compile-macro', shen_compilex45macro, 1)

@tail_recursion
def shen_prologx45macro(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_prologx45macro, (FUN_ARGS + lambdaargs)))
    KL_ARG_V876_1369 = FUN_ARGS[0]
    global symdic
    return (Cons(symdic.symdic_shen_intprolog, Cons(tco_apply(shen_prologx45form, [cdr(KL_ARG_V876_1369)]), nil)) if (shen_eq(symdic.symdic_kl_prologx63, car(KL_ARG_V876_1369)) if shen_consp(KL_ARG_V876_1369) else False) else (KL_ARG_V876_1369 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.prolog-macro', shen_prologx45macro, 1)

@tail_recursion
def shen_defprologx45macro(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_defprologx45macro, (FUN_ARGS + lambdaargs)))
    KL_ARG_V877_1370 = FUN_ARGS[0]
    global symdic
    return (tail_call(kl_compile, [symdic.symdic_shen_x60defprologx62, cdr(KL_ARG_V877_1370), (lambda KL_ARG_Y_1371: tail_call(shen_prologx45error, [car(cdr(KL_ARG_V877_1370)), KL_ARG_Y_1371]))]) if ((shen_consp(cdr(KL_ARG_V877_1370)) if shen_eq(symdic.symdic_kl_defprolog, car(KL_ARG_V877_1370)) else False) if shen_consp(KL_ARG_V877_1370) else False) else (KL_ARG_V877_1370 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.defprolog-macro', shen_defprologx45macro, 1)

@tail_recursion
def shen_prologx45form(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_prologx45form, (FUN_ARGS + lambdaargs)))
    KL_ARG_V878_1372 = FUN_ARGS[0]
    global symdic
    return tail_call(shen_cons_form, [tco_apply(kl_map, [symdic.symdic_shen_cons_form, KL_ARG_V878_1372])])
shen_add_fun('shen.prolog-form', shen_prologx45form, 1)

@tail_recursion
def shen_datatypex45macro(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_datatypex45macro, (FUN_ARGS + lambdaargs)))
    KL_ARG_V879_1373 = FUN_ARGS[0]
    global symdic
    return (Cons(symdic.symdic_shen_processx45datatype, Cons(tco_apply(shen_internx45type, [car(cdr(KL_ARG_V879_1373))]), Cons(Cons(symdic.symdic_kl_compile, Cons(Cons(symdic.symdic_kl_function, Cons(symdic.symdic_shen_x60datatypex45rulesx62, nil)), Cons(tco_apply(shen_rcons_form, [cdr(cdr(KL_ARG_V879_1373))]), Cons(Cons(symdic.symdic_kl_function, Cons(symdic.symdic_shen_datatypex45error, nil)), nil)))), nil))) if ((shen_consp(cdr(KL_ARG_V879_1373)) if shen_eq(symdic.symdic_kl_datatype, car(KL_ARG_V879_1373)) else False) if shen_consp(KL_ARG_V879_1373) else False) else (KL_ARG_V879_1373 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.datatype-macro', shen_datatypex45macro, 1)

@tail_recursion
def shen_internx45type(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_internx45type, (FUN_ARGS + lambdaargs)))
    KL_ARG_V880_1374 = FUN_ARGS[0]
    global symdic
    return shen_intern(('type#' + str(KL_ARG_V880_1374)))
shen_add_fun('shen.intern-type', shen_internx45type, 1)

@tail_recursion
def shen_defmacrox45macro(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_defmacrox45macro, (FUN_ARGS + lambdaargs)))
    KL_ARG_V881_1375 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Macro_1376 = None
        KL_LOC_Declare_1377 = None
        KL_LOC_Package_1378 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_Macro_1376', Cons(symdic.symdic_kl_define, Cons(car(cdr(KL_ARG_V881_1375)), tco_apply(kl_append, [cdr(cdr(KL_ARG_V881_1375)), Cons(symdic.symdic_X, Cons(symdic.symdic_kl_x45x62, Cons(symdic.symdic_X, nil)))])))), [setattr(KL_CTX, 'KL_LOC_Declare_1377', Cons(symdic.symdic_kl_do, Cons(Cons(symdic.symdic_kl_set, Cons(symdic.symdic_kl_x42macrosx42, Cons(Cons(symdic.symdic_kl_adjoin, Cons(car(cdr(KL_ARG_V881_1375)), Cons(Cons(symdic.symdic_kl_value, Cons(symdic.symdic_kl_x42macrosx42, nil)), nil))), nil))), Cons(symdic.symdic_kl_macro, nil)))), [setattr(KL_CTX, 'KL_LOC_Package_1378', Cons(symdic.symdic_kl_package, Cons(symdic.symdic_kl_null, Cons(nil, Cons(KL_CTX.KL_LOC_Declare_1377, Cons(KL_CTX.KL_LOC_Macro_1376, nil)))))), KL_CTX.KL_LOC_Package_1378][(-1)]][(-1)]][(-1)] if ((shen_consp(cdr(KL_ARG_V881_1375)) if shen_eq(symdic.symdic_kl_defmacro, car(KL_ARG_V881_1375)) else False) if shen_consp(KL_ARG_V881_1375) else False) else (KL_ARG_V881_1375 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.defmacro-macro', shen_defmacrox45macro, 1)

@tail_recursion
def shen_x60defmacrox62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60defmacrox62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V886_1379 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_1380 = None
        KL_LOC_Parse_shen_x60namex62_1381 = None
        KL_LOC_Parse_shen_x60macrorulesx62_1382 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_1380', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60namex62_1381', tco_apply(shen_x60namex62, [KL_ARG_V886_1379])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60macrorulesx62_1382', tco_apply(shen_x60macrorulesx62, [KL_CTX.KL_LOC_Parse_shen_x60namex62_1381])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60macrorulesx62_1382), Cons(symdic.symdic_kl_define, Cons(tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60namex62_1381]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60macrorulesx62_1382])))]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60macrorulesx62_1382)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60namex62_1381)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_1380, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_1380)][(-1)]
shen_add_fun('shen.<defmacro>', shen_x60defmacrox62, 1)

@tail_recursion
def shen_x60macrorulesx62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60macrorulesx62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V891_1383 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_1384 = None
        KL_LOC_Parse_shen_x60macrorulex62_1385 = None
        KL_LOC_Parse_shen_x60macrorulesx62_1386 = None
        KL_LOC_Result_1387 = None
        KL_LOC_Parse_shen_x60macrorulex62_1388 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_1384', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60macrorulex62_1385', tco_apply(shen_x60macrorulex62, [KL_ARG_V891_1383])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60macrorulesx62_1386', tco_apply(shen_x60macrorulesx62, [KL_CTX.KL_LOC_Parse_shen_x60macrorulex62_1385])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60macrorulesx62_1386), tco_apply(kl_append, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60macrorulex62_1385]), tco_apply(kl_append, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60macrorulesx62_1386]), nil])])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60macrorulesx62_1386)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60macrorulex62_1385)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_1387', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60macrorulex62_1388', tco_apply(shen_x60macrorulex62, [KL_ARG_V891_1383])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60macrorulex62_1388), tco_apply(kl_append, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60macrorulex62_1388]), Cons(symdic.symdic_Parse_X, Cons(symdic.symdic_kl_x45x62, Cons(symdic.symdic_Parse_X, nil)))])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60macrorulex62_1388)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_1387, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_1387)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_1384, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_1384)][(-1)]
shen_add_fun('shen.<macrorules>', shen_x60macrorulesx62, 1)

@tail_recursion
def shen_x60macrorulex62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60macrorulex62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V896_1389 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_1390 = None
        KL_LOC_Parse_shen_x60patternsx62_1391 = None
        KL_LOC_Parse_shen_x60macroactionx62_1392 = None
        KL_LOC_Parse_shen_x60guardx62_1393 = None
        KL_LOC_Result_1394 = None
        KL_LOC_Parse_shen_x60patternsx62_1395 = None
        KL_LOC_Parse_shen_x60macroactionx62_1396 = None
        KL_LOC_Result_1397 = None
        KL_LOC_Parse_shen_x60patternsx62_1398 = None
        KL_LOC_Parse_shen_x60macroactionx62_1399 = None
        KL_LOC_Parse_shen_x60guardx62_1400 = None
        KL_LOC_Result_1401 = None
        KL_LOC_Parse_shen_x60patternsx62_1402 = None
        KL_LOC_Parse_shen_x60macroactionx62_1403 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_1390', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60patternsx62_1391', tco_apply(shen_x60patternsx62, [KL_ARG_V896_1389])), (([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60macroactionx62_1392', tco_apply(shen_x60macroactionx62, [tco_apply(shen_pair, [cdr(car(KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1391)), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1391])])])), (([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60guardx62_1393', tco_apply(shen_x60guardx62, [tco_apply(shen_pair, [cdr(car(KL_CTX.KL_LOC_Parse_shen_x60macroactionx62_1392)), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60macroactionx62_1392])])])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60guardx62_1393), tco_apply(kl_append, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1391]), Cons(symdic.symdic_kl_x45x62, tco_apply(kl_append, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60macroactionx62_1392]), Cons(symdic.symdic_kl_where, tco_apply(kl_append, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60guardx62_1393]), nil]))]))])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60guardx62_1393)) else tco_apply(kl_fail, []))][(-1)] if (shen_eq(symdic.symdic_kl_where, car(car(KL_CTX.KL_LOC_Parse_shen_x60macroactionx62_1392))) if shen_consp(car(KL_CTX.KL_LOC_Parse_shen_x60macroactionx62_1392)) else False) else tco_apply(kl_fail, [])) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60macroactionx62_1392)) else tco_apply(kl_fail, []))][(-1)] if (shen_eq(symdic.symdic_kl_x45x62, car(car(KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1391))) if shen_consp(car(KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1391)) else False) else tco_apply(kl_fail, [])) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1391)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_1394', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60patternsx62_1395', tco_apply(shen_x60patternsx62, [KL_ARG_V896_1389])), (([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60macroactionx62_1396', tco_apply(shen_x60macroactionx62, [tco_apply(shen_pair, [cdr(car(KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1395)), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1395])])])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60macroactionx62_1396), tco_apply(kl_append, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1395]), Cons(symdic.symdic_kl_x45x62, tco_apply(kl_append, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60macroactionx62_1396]), nil]))])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60macroactionx62_1396)) else tco_apply(kl_fail, []))][(-1)] if (shen_eq(symdic.symdic_kl_x45x62, car(car(KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1395))) if shen_consp(car(KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1395)) else False) else tco_apply(kl_fail, [])) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1395)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_1397', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60patternsx62_1398', tco_apply(shen_x60patternsx62, [KL_ARG_V896_1389])), (([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60macroactionx62_1399', tco_apply(shen_x60macroactionx62, [tco_apply(shen_pair, [cdr(car(KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1398)), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1398])])])), (([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60guardx62_1400', tco_apply(shen_x60guardx62, [tco_apply(shen_pair, [cdr(car(KL_CTX.KL_LOC_Parse_shen_x60macroactionx62_1399)), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60macroactionx62_1399])])])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60guardx62_1400), tco_apply(kl_append, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1398]), Cons(symdic.symdic_kl_x60x45, tco_apply(kl_append, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60macroactionx62_1399]), Cons(symdic.symdic_kl_where, tco_apply(kl_append, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60guardx62_1400]), nil]))]))])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60guardx62_1400)) else tco_apply(kl_fail, []))][(-1)] if (shen_eq(symdic.symdic_kl_where, car(car(KL_CTX.KL_LOC_Parse_shen_x60macroactionx62_1399))) if shen_consp(car(KL_CTX.KL_LOC_Parse_shen_x60macroactionx62_1399)) else False) else tco_apply(kl_fail, [])) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60macroactionx62_1399)) else tco_apply(kl_fail, []))][(-1)] if (shen_eq(symdic.symdic_kl_x60x45, car(car(KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1398))) if shen_consp(car(KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1398)) else False) else tco_apply(kl_fail, [])) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1398)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_1401', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60patternsx62_1402', tco_apply(shen_x60patternsx62, [KL_ARG_V896_1389])), (([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60macroactionx62_1403', tco_apply(shen_x60macroactionx62, [tco_apply(shen_pair, [cdr(car(KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1402)), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1402])])])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60macroactionx62_1403), tco_apply(kl_append, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1402]), Cons(symdic.symdic_kl_x60x45, tco_apply(kl_append, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60macroactionx62_1403]), nil]))])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60macroactionx62_1403)) else tco_apply(kl_fail, []))][(-1)] if (shen_eq(symdic.symdic_kl_x60x45, car(car(KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1402))) if shen_consp(car(KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1402)) else False) else tco_apply(kl_fail, [])) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1402)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_1401, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_1401)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_1397, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_1397)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_1394, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_1394)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_1390, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_1390)][(-1)]
shen_add_fun('shen.<macrorule>', shen_x60macrorulex62, 1)

@tail_recursion
def shen_x60macroactionx62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60macroactionx62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V901_1404 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_1405 = None
        KL_LOC_Parse_shen_x60actionx62_1406 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_1405', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60actionx62_1406', tco_apply(shen_x60actionx62, [KL_ARG_V901_1404])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60actionx62_1406), Cons(Cons(symdic.symdic_shen_walk, Cons(Cons(symdic.symdic_kl_function, Cons(symdic.symdic_kl_macroexpand, nil)), Cons(tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60actionx62_1406]), nil))), nil)]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60actionx62_1406)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_1405, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_1405)][(-1)]
shen_add_fun('shen.<macroaction>', shen_x60macroactionx62, 1)

@tail_recursion
def shen_x64sx45macro(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x64sx45macro, (FUN_ARGS + lambdaargs)))
    KL_ARG_V902_1407 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_E_1408 = None
    KL_CTX = KL_Context()
    global symdic
    return (Cons(symdic.symdic_kl_x64s, Cons(car(cdr(KL_ARG_V902_1407)), Cons(tco_apply(shen_x64sx45macro, [Cons(symdic.symdic_kl_x64s, cdr(cdr(KL_ARG_V902_1407)))]), nil))) if ((((shen_consp(cdr(cdr(cdr(KL_ARG_V902_1407)))) if shen_consp(cdr(cdr(KL_ARG_V902_1407))) else False) if shen_consp(cdr(KL_ARG_V902_1407)) else False) if shen_eq(symdic.symdic_kl_x64s, car(KL_ARG_V902_1407)) else False) if shen_consp(KL_ARG_V902_1407) else False) else ([setattr(KL_CTX, 'KL_LOC_E_1408', tco_apply(kl_explode, [car(cdr(KL_ARG_V902_1407))])), (tail_call(shen_x64sx45macro, [Cons(symdic.symdic_kl_x64s, tco_apply(kl_append, [KL_CTX.KL_LOC_E_1408, cdr(cdr(KL_ARG_V902_1407))]))]) if (tco_apply(kl_length, [KL_CTX.KL_LOC_E_1408]) > 1) else KL_ARG_V902_1407)][(-1)] if (((((isinstance(car(cdr(KL_ARG_V902_1407)), str) if shen_eq(nil, cdr(cdr(cdr(KL_ARG_V902_1407)))) else False) if shen_consp(cdr(cdr(KL_ARG_V902_1407))) else False) if shen_consp(cdr(KL_ARG_V902_1407)) else False) if shen_eq(symdic.symdic_kl_x64s, car(KL_ARG_V902_1407)) else False) if shen_consp(KL_ARG_V902_1407) else False) else (KL_ARG_V902_1407 if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.@s-macro', shen_x64sx45macro, 1)

@tail_recursion
def shen_synonymsx45macro(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_synonymsx45macro, (FUN_ARGS + lambdaargs)))
    KL_ARG_V903_1409 = FUN_ARGS[0]
    global symdic
    return (Cons(symdic.symdic_shen_synonymsx45help, Cons(tco_apply(shen_rcons_form, [cdr(KL_ARG_V903_1409)]), nil)) if (shen_eq(symdic.symdic_kl_synonyms, car(KL_ARG_V903_1409)) if shen_consp(KL_ARG_V903_1409) else False) else (KL_ARG_V903_1409 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.synonyms-macro', shen_synonymsx45macro, 1)

@tail_recursion
def shen_nlx45macro(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_nlx45macro, (FUN_ARGS + lambdaargs)))
    KL_ARG_V904_1410 = FUN_ARGS[0]
    global symdic
    return (Cons(symdic.symdic_kl_nl, Cons(1, nil)) if ((shen_eq(nil, cdr(KL_ARG_V904_1410)) if shen_eq(symdic.symdic_kl_nl, car(KL_ARG_V904_1410)) else False) if shen_consp(KL_ARG_V904_1410) else False) else (KL_ARG_V904_1410 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.nl-macro', shen_nlx45macro, 1)

@tail_recursion
def shen_assocx45macro(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_assocx45macro, (FUN_ARGS + lambdaargs)))
    KL_ARG_V905_1411 = FUN_ARGS[0]
    global symdic
    return (Cons(car(KL_ARG_V905_1411), Cons(car(cdr(KL_ARG_V905_1411)), Cons(tco_apply(shen_assocx45macro, [Cons(car(KL_ARG_V905_1411), cdr(cdr(KL_ARG_V905_1411)))]), nil))) if ((((tco_apply(kl_elementx63, [car(KL_ARG_V905_1411), Cons(symdic.symdic_kl_x64p, Cons(symdic.symdic_kl_x64v, Cons(symdic.symdic_kl_append, Cons(symdic.symdic_kl_and, Cons(symdic.symdic_kl_or, Cons(symdic.symdic_kl_x43, Cons(symdic.symdic_kl_x42, Cons(symdic.symdic_kl_do, nil))))))))]) if shen_consp(cdr(cdr(cdr(KL_ARG_V905_1411)))) else False) if shen_consp(cdr(cdr(KL_ARG_V905_1411))) else False) if shen_consp(cdr(KL_ARG_V905_1411)) else False) if shen_consp(KL_ARG_V905_1411) else False) else (KL_ARG_V905_1411 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.assoc-macro', shen_assocx45macro, 1)

@tail_recursion
def shen_letx45macro(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_letx45macro, (FUN_ARGS + lambdaargs)))
    KL_ARG_V906_1412 = FUN_ARGS[0]
    global symdic
    return (Cons(symdic.symdic_kl_let, Cons(car(cdr(KL_ARG_V906_1412)), Cons(car(cdr(cdr(KL_ARG_V906_1412))), Cons(tco_apply(shen_letx45macro, [Cons(symdic.symdic_kl_let, cdr(cdr(cdr(KL_ARG_V906_1412))))]), nil)))) if (((((shen_consp(cdr(cdr(cdr(cdr(KL_ARG_V906_1412))))) if shen_consp(cdr(cdr(cdr(KL_ARG_V906_1412)))) else False) if shen_consp(cdr(cdr(KL_ARG_V906_1412))) else False) if shen_consp(cdr(KL_ARG_V906_1412)) else False) if shen_eq(symdic.symdic_kl_let, car(KL_ARG_V906_1412)) else False) if shen_consp(KL_ARG_V906_1412) else False) else (KL_ARG_V906_1412 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.let-macro', shen_letx45macro, 1)

@tail_recursion
def shen_absx45macro(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_absx45macro, (FUN_ARGS + lambdaargs)))
    KL_ARG_V907_1413 = FUN_ARGS[0]
    global symdic
    return (Cons(symdic.symdic_kl_lambda, Cons(car(cdr(KL_ARG_V907_1413)), Cons(tco_apply(shen_absx45macro, [Cons(symdic.symdic_kl_x47_, cdr(cdr(KL_ARG_V907_1413)))]), nil))) if ((((shen_consp(cdr(cdr(cdr(KL_ARG_V907_1413)))) if shen_consp(cdr(cdr(KL_ARG_V907_1413))) else False) if shen_consp(cdr(KL_ARG_V907_1413)) else False) if shen_eq(symdic.symdic_kl_x47_, car(KL_ARG_V907_1413)) else False) if shen_consp(KL_ARG_V907_1413) else False) else (Cons(symdic.symdic_kl_lambda, cdr(KL_ARG_V907_1413)) if ((((shen_eq(nil, cdr(cdr(cdr(KL_ARG_V907_1413)))) if shen_consp(cdr(cdr(KL_ARG_V907_1413))) else False) if shen_consp(cdr(KL_ARG_V907_1413)) else False) if shen_eq(symdic.symdic_kl_x47_, car(KL_ARG_V907_1413)) else False) if shen_consp(KL_ARG_V907_1413) else False) else (KL_ARG_V907_1413 if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.abs-macro', shen_absx45macro, 1)

@tail_recursion
def shen_casesx45macro(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_casesx45macro, (FUN_ARGS + lambdaargs)))
    KL_ARG_V910_1414 = FUN_ARGS[0]
    global symdic
    return (car(cdr(cdr(KL_ARG_V910_1414))) if ((((shen_consp(cdr(cdr(KL_ARG_V910_1414))) if shen_eq(True, car(cdr(KL_ARG_V910_1414))) else False) if shen_consp(cdr(KL_ARG_V910_1414)) else False) if shen_eq(symdic.symdic_kl_cases, car(KL_ARG_V910_1414)) else False) if shen_consp(KL_ARG_V910_1414) else False) else (Cons(symdic.symdic_kl_if, Cons(car(cdr(KL_ARG_V910_1414)), Cons(car(cdr(cdr(KL_ARG_V910_1414))), Cons(Cons(symdic.symdic_kl_simplex45error, Cons('error: cases exhausted', nil)), nil)))) if ((((shen_eq(nil, cdr(cdr(cdr(KL_ARG_V910_1414)))) if shen_consp(cdr(cdr(KL_ARG_V910_1414))) else False) if shen_consp(cdr(KL_ARG_V910_1414)) else False) if shen_eq(symdic.symdic_kl_cases, car(KL_ARG_V910_1414)) else False) if shen_consp(KL_ARG_V910_1414) else False) else (Cons(symdic.symdic_kl_if, Cons(car(cdr(KL_ARG_V910_1414)), Cons(car(cdr(cdr(KL_ARG_V910_1414))), Cons(tco_apply(shen_casesx45macro, [Cons(symdic.symdic_kl_cases, cdr(cdr(cdr(KL_ARG_V910_1414))))]), nil)))) if (((shen_consp(cdr(cdr(KL_ARG_V910_1414))) if shen_consp(cdr(KL_ARG_V910_1414)) else False) if shen_eq(symdic.symdic_kl_cases, car(KL_ARG_V910_1414)) else False) if shen_consp(KL_ARG_V910_1414) else False) else (shen_simple_error('error: odd number of case elements\r\n') if (((shen_eq(nil, cdr(cdr(KL_ARG_V910_1414))) if shen_consp(cdr(KL_ARG_V910_1414)) else False) if shen_eq(symdic.symdic_kl_cases, car(KL_ARG_V910_1414)) else False) if shen_consp(KL_ARG_V910_1414) else False) else (KL_ARG_V910_1414 if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.cases-macro', shen_casesx45macro, 1)

@tail_recursion
def shen_timerx45macro(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_timerx45macro, (FUN_ARGS + lambdaargs)))
    KL_ARG_V911_1415 = FUN_ARGS[0]
    global symdic
    return (tail_call(shen_letx45macro, [Cons(symdic.symdic_kl_let, Cons(symdic.symdic_Start, Cons(Cons(symdic.symdic_kl_getx45time, Cons(symdic.symdic_kl_run, nil)), Cons(symdic.symdic_Result, Cons(car(cdr(KL_ARG_V911_1415)), Cons(symdic.symdic_Finish, Cons(Cons(symdic.symdic_kl_getx45time, Cons(symdic.symdic_kl_run, nil)), Cons(symdic.symdic_Time, Cons(Cons(symdic.symdic_kl_x45, Cons(symdic.symdic_Finish, Cons(symdic.symdic_Start, nil))), Cons(symdic.symdic_Message, Cons(Cons(symdic.symdic_shen_prhush, Cons(Cons(symdic.symdic_kl_cn, Cons('\r\nrun time: ', Cons(Cons(symdic.symdic_kl_cn, Cons(Cons(symdic.symdic_kl_str, Cons(symdic.symdic_Time, nil)), Cons(' secs\r\n', nil))), nil))), Cons(Cons(symdic.symdic_kl_stoutput, nil), nil))), Cons(symdic.symdic_Result, nil))))))))))))]) if (((shen_eq(nil, cdr(cdr(KL_ARG_V911_1415))) if shen_consp(cdr(KL_ARG_V911_1415)) else False) if shen_eq(symdic.symdic_kl_time, car(KL_ARG_V911_1415)) else False) if shen_consp(KL_ARG_V911_1415) else False) else (KL_ARG_V911_1415 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.timer-macro', shen_timerx45macro, 1)

@tail_recursion
def shen_tuplex45up(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_tuplex45up, (FUN_ARGS + lambdaargs)))
    KL_ARG_V912_1416 = FUN_ARGS[0]
    global symdic
    return (Cons(symdic.symdic_kl_x64p, Cons(car(KL_ARG_V912_1416), Cons(tco_apply(shen_tuplex45up, [cdr(KL_ARG_V912_1416)]), nil))) if shen_consp(KL_ARG_V912_1416) else (KL_ARG_V912_1416 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.tuple-up', shen_tuplex45up, 1)

@tail_recursion
def shen_putx47getx45macro(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_putx47getx45macro, (FUN_ARGS + lambdaargs)))
    KL_ARG_V913_1417 = FUN_ARGS[0]
    global symdic
    return (Cons(symdic.symdic_kl_put, Cons(car(cdr(KL_ARG_V913_1417)), Cons(car(cdr(cdr(KL_ARG_V913_1417))), Cons(car(cdr(cdr(cdr(KL_ARG_V913_1417)))), Cons(Cons(symdic.symdic_kl_value, Cons(symdic.symdic_kl_x42propertyx45vectorx42, nil)), nil))))) if (((((shen_eq(nil, cdr(cdr(cdr(cdr(KL_ARG_V913_1417))))) if shen_consp(cdr(cdr(cdr(KL_ARG_V913_1417)))) else False) if shen_consp(cdr(cdr(KL_ARG_V913_1417))) else False) if shen_consp(cdr(KL_ARG_V913_1417)) else False) if shen_eq(symdic.symdic_kl_put, car(KL_ARG_V913_1417)) else False) if shen_consp(KL_ARG_V913_1417) else False) else (Cons(symdic.symdic_kl_get, Cons(car(cdr(KL_ARG_V913_1417)), Cons(car(cdr(cdr(KL_ARG_V913_1417))), Cons(Cons(symdic.symdic_kl_value, Cons(symdic.symdic_kl_x42propertyx45vectorx42, nil)), nil)))) if ((((shen_eq(nil, cdr(cdr(cdr(KL_ARG_V913_1417)))) if shen_consp(cdr(cdr(KL_ARG_V913_1417))) else False) if shen_consp(cdr(KL_ARG_V913_1417)) else False) if shen_eq(symdic.symdic_kl_get, car(KL_ARG_V913_1417)) else False) if shen_consp(KL_ARG_V913_1417) else False) else (KL_ARG_V913_1417 if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.put/get-macro', shen_putx47getx45macro, 1)

@tail_recursion
def shen_functionx45macro(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_functionx45macro, (FUN_ARGS + lambdaargs)))
    KL_ARG_V914_1418 = FUN_ARGS[0]
    global symdic
    return (tail_call(shen_functionx45abstraction, [car(cdr(KL_ARG_V914_1418)), tco_apply(kl_arity, [car(cdr(KL_ARG_V914_1418))])]) if (((shen_eq(nil, cdr(cdr(KL_ARG_V914_1418))) if shen_consp(cdr(KL_ARG_V914_1418)) else False) if shen_eq(symdic.symdic_kl_function, car(KL_ARG_V914_1418)) else False) if shen_consp(KL_ARG_V914_1418) else False) else (KL_ARG_V914_1418 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.function-macro', shen_functionx45macro, 1)

@tail_recursion
def shen_functionx45abstraction(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_functionx45abstraction, (FUN_ARGS + lambdaargs)))
    KL_ARG_V915_1419 = FUN_ARGS[0]
    KL_ARG_V916_1420 = FUN_ARGS[1]
    global symdic
    return (Cons(symdic.symdic_kl_freeze, Cons(KL_ARG_V915_1419, nil)) if shen_eq(0, KL_ARG_V916_1420) else (KL_ARG_V915_1419 if shen_eq((-1), KL_ARG_V916_1420) else (tail_call(shen_functionx45abstractionx45help, [KL_ARG_V915_1419, KL_ARG_V916_1420, nil]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.function-abstraction', shen_functionx45abstraction, 2)

@tail_recursion
def shen_functionx45abstractionx45help(*FUN_ARGS):
    FUN_ARITY = 3
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_functionx45abstractionx45help, (FUN_ARGS + lambdaargs)))
    KL_ARG_V917_1421 = FUN_ARGS[0]
    KL_ARG_V918_1422 = FUN_ARGS[1]
    KL_ARG_V919_1423 = FUN_ARGS[2]

    class KL_Context:
        KL_LOC_X_1424 = None
    KL_CTX = KL_Context()
    global symdic
    return (Cons(KL_ARG_V917_1421, KL_ARG_V919_1423) if shen_eq(0, KL_ARG_V918_1422) else ([setattr(KL_CTX, 'KL_LOC_X_1424', tco_apply(kl_gensym, [symdic.symdic_V])), Cons(symdic.symdic_kl_x47_, Cons(KL_CTX.KL_LOC_X_1424, Cons(tco_apply(shen_functionx45abstractionx45help, [KL_ARG_V917_1421, (KL_ARG_V918_1422 - 1), tco_apply(kl_append, [KL_ARG_V919_1423, Cons(KL_CTX.KL_LOC_X_1424, nil)])]), nil)))][(-1)] if True else shen_simple_error('condition failure')))
shen_add_fun('shen.function-abstraction-help', shen_functionx45abstractionx45help, 3)

@tail_recursion
def kl_undefmacro(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_undefmacro, (FUN_ARGS + lambdaargs)))
    KL_ARG_V920_1425 = FUN_ARGS[0]
    global symdic
    return [shen_set(symdic.symdic_kl_x42macrosx42, tco_apply(kl_remove, [KL_ARG_V920_1425, shen_get(symdic.symdic_kl_x42macrosx42)])), KL_ARG_V920_1425][(-1)]
shen_add_fun('undefmacro', kl_undefmacro, 1)


#============================== declarations.kl==============================


shen_set(symdic.symdic_shen_x42installingx45klx42, False)
shen_set(symdic.symdic_shen_x42historyx42, nil)
shen_set(symdic.symdic_shen_x42tcx42, False)
shen_set(symdic.symdic_kl_x42propertyx45vectorx42, tco_apply(kl_vector, [20000]))
shen_set(symdic.symdic_shen_x42processx45counterx42, 0)
shen_set(symdic.symdic_shen_x42varcounterx42, tco_apply(kl_vector, [1000]))
shen_set(symdic.symdic_shen_x42prologvectorsx42, tco_apply(kl_vector, [1000]))
shen_set(symdic.symdic_shen_x42readerx45macrosx42, nil)
shen_set(symdic.symdic_kl_x42homex45directoryx42, nil)
shen_set(symdic.symdic_shen_x42gensymx42, 0)
shen_set(symdic.symdic_shen_x42trackingx42, nil)
shen_set(symdic.symdic_kl_x42homex45directoryx42, '')
shen_set(symdic.symdic_shen_x42alphabetx42, Cons(symdic.symdic_A, Cons(symdic.symdic_B, Cons(symdic.symdic_C, Cons(symdic.symdic_D, Cons(symdic.symdic_E, Cons(symdic.symdic_F, Cons(symdic.symdic_G, Cons(symdic.symdic_H, Cons(symdic.symdic_I, Cons(symdic.symdic_J, Cons(symdic.symdic_K, Cons(symdic.symdic_L, Cons(symdic.symdic_M, Cons(symdic.symdic_N, Cons(symdic.symdic_O, Cons(symdic.symdic_P, Cons(symdic.symdic_Q, Cons(symdic.symdic_R, Cons(symdic.symdic_S, Cons(symdic.symdic_T, Cons(symdic.symdic_U, Cons(symdic.symdic_V, Cons(symdic.symdic_W, Cons(symdic.symdic_X, Cons(symdic.symdic_Y, Cons(symdic.symdic_Z, nil)))))))))))))))))))))))))))
shen_set(symdic.symdic_shen_x42specialx42, Cons(symdic.symdic_kl_x64p, Cons(symdic.symdic_kl_x64s, Cons(symdic.symdic_kl_x64v, Cons(symdic.symdic_kl_cons, Cons(symdic.symdic_kl_lambda, Cons(symdic.symdic_kl_let, Cons(symdic.symdic_kl_type, Cons(symdic.symdic_kl_where, Cons(symdic.symdic_kl_set, Cons(symdic.symdic_kl_open, nil)))))))))))
shen_set(symdic.symdic_shen_x42extraspecialx42, Cons(symdic.symdic_kl_define, Cons(symdic.symdic_shen_processx45datatype, Cons(symdic.symdic_kl_inputx43, Cons(symdic.symdic_kl_defcc, Cons(symdic.symdic_readx43, nil))))))
shen_set(symdic.symdic_shen_x42spyx42, False)
shen_set(symdic.symdic_shen_x42datatypesx42, nil)
shen_set(symdic.symdic_shen_x42alldatatypesx42, nil)
shen_set(symdic.symdic_shen_x42shenx45typex45theoryx45enabledx63x42, True)
shen_set(symdic.symdic_shen_x42synonymsx42, nil)
shen_set(symdic.symdic_shen_x42systemx42, nil)
shen_set(symdic.symdic_shen_x42signedfuncsx42, nil)
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
def shen_initialise_arity_table(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_initialise_arity_table, (FUN_ARGS + lambdaargs)))
    KL_ARG_V822_1426 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_DecArity_1427 = None
    KL_CTX = KL_Context()
    global symdic
    return (nil if shen_eq(nil, KL_ARG_V822_1426) else ([setattr(KL_CTX, 'KL_LOC_DecArity_1427', tco_apply(kl_put, [car(KL_ARG_V822_1426), symdic.symdic_kl_arity, car(cdr(KL_ARG_V822_1426)), shen_get(symdic.symdic_kl_x42propertyx45vectorx42)])), tail_call(shen_initialise_arity_table, [cdr(cdr(KL_ARG_V822_1426))])][(-1)] if (shen_consp(cdr(KL_ARG_V822_1426)) if shen_consp(KL_ARG_V822_1426) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_initialise_arity_table]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.initialise_arity_table', shen_initialise_arity_table, 1)

@tail_recursion
def kl_arity(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_arity, (FUN_ARGS + lambdaargs)))
    KL_ARG_V823_1428 = FUN_ARGS[0]
    global symdic
    return shen_try_except((lambda : tco_apply(kl_get, [KL_ARG_V823_1428, symdic.symdic_kl_arity, shen_get(symdic.symdic_kl_x42propertyx45vectorx42)])), (lambda KL_ARG_E_1429: (-1)))
shen_add_fun('arity', kl_arity, 1)

@tail_recursion
def kl_systemf(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_systemf, (FUN_ARGS + lambdaargs)))
    KL_ARG_V824_1430 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Shen_1431 = None
        KL_LOC_External_1432 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Shen_1431', shen_intern('shen')), [setattr(KL_CTX, 'KL_LOC_External_1432', tco_apply(kl_get, [KL_CTX.KL_LOC_Shen_1431, symdic.symdic_shen_externalx45symbols, shen_get(symdic.symdic_kl_x42propertyx45vectorx42)])), tail_call(kl_put, [KL_CTX.KL_LOC_Shen_1431, symdic.symdic_shen_externalx45symbols, tco_apply(kl_adjoin, [KL_ARG_V824_1430, KL_CTX.KL_LOC_External_1432]), shen_get(symdic.symdic_kl_x42propertyx45vectorx42)])][(-1)]][(-1)]
shen_add_fun('systemf', kl_systemf, 1)

@tail_recursion
def kl_adjoin(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_adjoin, (FUN_ARGS + lambdaargs)))
    KL_ARG_V825_1433 = FUN_ARGS[0]
    KL_ARG_V826_1434 = FUN_ARGS[1]
    global symdic
    return (KL_ARG_V826_1434 if tco_apply(kl_elementx63, [KL_ARG_V825_1433, KL_ARG_V826_1434]) else Cons(KL_ARG_V825_1433, KL_ARG_V826_1434))
shen_add_fun('adjoin', kl_adjoin, 2)

@tail_recursion
def kl_specialise(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_specialise, (FUN_ARGS + lambdaargs)))
    KL_ARG_V827_1435 = FUN_ARGS[0]
    global symdic
    return [shen_set(symdic.symdic_shen_x42specialx42, Cons(KL_ARG_V827_1435, shen_get(symdic.symdic_shen_x42specialx42))), KL_ARG_V827_1435][(-1)]
shen_add_fun('specialise', kl_specialise, 1)

@tail_recursion
def kl_unspecialise(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_unspecialise, (FUN_ARGS + lambdaargs)))
    KL_ARG_V828_1436 = FUN_ARGS[0]
    global symdic
    return [shen_set(symdic.symdic_shen_x42specialx42, tco_apply(kl_remove, [KL_ARG_V828_1436, shen_get(symdic.symdic_shen_x42specialx42)])), KL_ARG_V828_1436][(-1)]
shen_add_fun('unspecialise', kl_unspecialise, 1)


#============================== types.kl==============================



@tail_recursion
def kl_declare(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_declare, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2131_1437 = FUN_ARGS[0]
    KL_ARG_V2132_1438 = FUN_ARGS[1]

    class KL_Context:
        KL_LOC_Record_1439 = None
        KL_LOC_Variancy_1440 = None
        KL_LOC_Type_1442 = None
        KL_LOC_Fx42_1443 = None
        KL_LOC_Parameters_1444 = None
        KL_LOC_Clause_1445 = None
        KL_LOC_AUM_instruction_1446 = None
        KL_LOC_Code_1447 = None
        KL_LOC_ShenDef_1448 = None
        KL_LOC_Eval_1449 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Record_1439', shen_set(symdic.symdic_shen_x42signedfuncsx42, Cons(Cons(KL_ARG_V2131_1437, KL_ARG_V2132_1438), shen_get(symdic.symdic_shen_x42signedfuncsx42)))), [setattr(KL_CTX, 'KL_LOC_Variancy_1440', shen_try_except((lambda : tco_apply(shen_variancyx45test, [KL_ARG_V2131_1437, KL_ARG_V2132_1438])), (lambda KL_ARG_E_1441: symdic.symdic_shen_skip))), [setattr(KL_CTX, 'KL_LOC_Type_1442', tco_apply(shen_rcons_form, [tco_apply(shen_demodulate, [KL_ARG_V2132_1438])])), [setattr(KL_CTX, 'KL_LOC_Fx42_1443', tco_apply(kl_concat, [symdic.symdic_shen_typex45signaturex45ofx45, KL_ARG_V2131_1437])), [setattr(KL_CTX, 'KL_LOC_Parameters_1444', tco_apply(shen_parameters, [1])), [setattr(KL_CTX, 'KL_LOC_Clause_1445', Cons(Cons(KL_CTX.KL_LOC_Fx42_1443, Cons(symdic.symdic_X, nil)), Cons(symdic.symdic_kl_x58x45, Cons(Cons(Cons(symdic.symdic_kl_unifyx33, Cons(symdic.symdic_X, Cons(KL_CTX.KL_LOC_Type_1442, nil))), nil), nil)))), [setattr(KL_CTX, 'KL_LOC_AUM_instruction_1446', tco_apply(shen_aum, [KL_CTX.KL_LOC_Clause_1445, KL_CTX.KL_LOC_Parameters_1444])), [setattr(KL_CTX, 'KL_LOC_Code_1447', tco_apply(shen_aum_to_shen, [KL_CTX.KL_LOC_AUM_instruction_1446])), [setattr(KL_CTX, 'KL_LOC_ShenDef_1448', Cons(symdic.symdic_kl_define, Cons(KL_CTX.KL_LOC_Fx42_1443, tco_apply(kl_append, [KL_CTX.KL_LOC_Parameters_1444, tco_apply(kl_append, [Cons(symdic.symdic_ProcessN, Cons(symdic.symdic_Continuation, nil)), Cons(symdic.symdic_kl_x45x62, Cons(KL_CTX.KL_LOC_Code_1447, nil))])])))), [setattr(KL_CTX, 'KL_LOC_Eval_1449', tco_apply(shen_evalx45withoutx45macros, [KL_CTX.KL_LOC_ShenDef_1448])), KL_ARG_V2131_1437][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]
shen_add_fun('declare', kl_declare, 2)

@tail_recursion
def shen_demodulate(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_demodulate, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2133_1450 = FUN_ARGS[0]
    global symdic
    return tail_call(kl_fix, [symdic.symdic_shen_demodh, KL_ARG_V2133_1450])
shen_add_fun('shen.demodulate', shen_demodulate, 1)

@tail_recursion
def shen_demodh(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_demodh, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2134_1451 = FUN_ARGS[0]
    global symdic
    return (tail_call(kl_map, [symdic.symdic_shen_demodh, KL_ARG_V2134_1451]) if shen_consp(KL_ARG_V2134_1451) else (tail_call(shen_demodx45atom, [KL_ARG_V2134_1451]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.demodh', shen_demodh, 1)

@tail_recursion
def shen_demodx45atom(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_demodx45atom, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2135_1452 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Val_1453 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Val_1453', tco_apply(kl_assoc, [KL_ARG_V2135_1452, shen_get(symdic.symdic_shen_x42synonymsx42)])), (KL_ARG_V2135_1452 if tco_apply(kl_emptyx63, [KL_CTX.KL_LOC_Val_1453]) else cdr(KL_CTX.KL_LOC_Val_1453))][(-1)]
shen_add_fun('shen.demod-atom', shen_demodx45atom, 1)

@tail_recursion
def shen_variancyx45test(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_variancyx45test, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2136_1454 = FUN_ARGS[0]
    KL_ARG_V2137_1455 = FUN_ARGS[1]

    class KL_Context:
        KL_LOC_TypeF_1456 = None
        KL_LOC_Check_1457 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_TypeF_1456', tco_apply(shen_typecheck, [KL_ARG_V2136_1454, symdic.symdic_B])), [setattr(KL_CTX, 'KL_LOC_Check_1457', (symdic.symdic_shen_skip if shen_eq(symdic.symdic_kl_symbol, KL_CTX.KL_LOC_TypeF_1456) else (symdic.symdic_shen_skip if tco_apply(shen_variantx63, [KL_CTX.KL_LOC_TypeF_1456, KL_ARG_V2137_1455]) else tco_apply(shen_prhush, [('warning: changing the type of ' + tco_apply(shen_app, [KL_ARG_V2136_1454, ' may create errors\r\n', symdic.symdic_shen_a])), tco_apply(kl_stoutput, [])])))), symdic.symdic_shen_skip][(-1)]][(-1)]
shen_add_fun('shen.variancy-test', shen_variancyx45test, 2)

@tail_recursion
def shen_variantx63(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_variantx63, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2146_1458 = FUN_ARGS[0]
    KL_ARG_V2147_1459 = FUN_ARGS[1]
    global symdic
    return (True if shen_eq(KL_ARG_V2147_1459, KL_ARG_V2146_1458) else (tail_call(shen_variantx63, [cdr(KL_ARG_V2146_1458), cdr(KL_ARG_V2147_1459)]) if ((shen_eq(car(KL_ARG_V2147_1459), car(KL_ARG_V2146_1458)) if shen_consp(KL_ARG_V2147_1459) else False) if shen_consp(KL_ARG_V2146_1458) else False) else (tail_call(shen_variantx63, [tco_apply(kl_subst, [symdic.symdic_shen_a, car(KL_ARG_V2146_1458), cdr(KL_ARG_V2146_1458)]), tco_apply(kl_subst, [symdic.symdic_shen_a, car(KL_ARG_V2147_1459), cdr(KL_ARG_V2147_1459)])]) if (((tco_apply(kl_variablex63, [car(KL_ARG_V2147_1459)]) if tco_apply(shen_pvarx63, [car(KL_ARG_V2146_1458)]) else False) if shen_consp(KL_ARG_V2147_1459) else False) if shen_consp(KL_ARG_V2146_1458) else False) else (tail_call(shen_variantx63, [tco_apply(kl_append, [car(KL_ARG_V2146_1458), cdr(KL_ARG_V2146_1458)]), tco_apply(kl_append, [car(KL_ARG_V2147_1459), cdr(KL_ARG_V2147_1459)])]) if (((shen_consp(car(KL_ARG_V2147_1459)) if shen_consp(KL_ARG_V2147_1459) else False) if shen_consp(car(KL_ARG_V2146_1458)) else False) if shen_consp(KL_ARG_V2146_1458) else False) else (False if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.variant?', shen_variantx63, 2)


#============================== t-star.kl==============================



@tail_recursion
def shen_typecheck(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_typecheck, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2848_1460 = FUN_ARGS[0]
    KL_ARG_V2849_1461 = FUN_ARGS[1]

    class KL_Context:
        KL_LOC_Curry_1462 = None
        KL_LOC_ProcessN_1463 = None
        KL_LOC_Type_1464 = None
        KL_LOC_Continuation_1465 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Curry_1462', tco_apply(shen_curry, [KL_ARG_V2848_1460])), [setattr(KL_CTX, 'KL_LOC_ProcessN_1463', tco_apply(shen_startx45newx45prologx45process, [])), [setattr(KL_CTX, 'KL_LOC_Type_1464', tco_apply(shen_insertx45prologx45variables, [tco_apply(shen_demodulate, [tco_apply(shen_curryx45type, [KL_ARG_V2849_1461])]), KL_CTX.KL_LOC_ProcessN_1463])), [setattr(KL_CTX, 'KL_LOC_Continuation_1465', (lambda : tail_call(kl_return, [KL_CTX.KL_LOC_Type_1464, KL_CTX.KL_LOC_ProcessN_1463, symdic.symdic_shen_void]))), tail_call(shen_tx42, [Cons(KL_CTX.KL_LOC_Curry_1462, Cons(symdic.symdic_kl_x58, Cons(KL_CTX.KL_LOC_Type_1464, nil))), nil, KL_CTX.KL_LOC_ProcessN_1463, KL_CTX.KL_LOC_Continuation_1465])][(-1)]][(-1)]][(-1)]][(-1)]
shen_add_fun('shen.typecheck', shen_typecheck, 2)

@tail_recursion
def shen_curry(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_curry, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2850_1466 = FUN_ARGS[0]
    global symdic
    return (Cons(car(KL_ARG_V2850_1466), tco_apply(kl_map, [symdic.symdic_shen_curry, cdr(KL_ARG_V2850_1466)])) if (tco_apply(shen_specialx63, [car(KL_ARG_V2850_1466)]) if shen_consp(KL_ARG_V2850_1466) else False) else (KL_ARG_V2850_1466 if ((tco_apply(shen_extraspecialx63, [car(KL_ARG_V2850_1466)]) if shen_consp(cdr(KL_ARG_V2850_1466)) else False) if shen_consp(KL_ARG_V2850_1466) else False) else (tail_call(shen_curry, [Cons(Cons(car(KL_ARG_V2850_1466), Cons(car(cdr(KL_ARG_V2850_1466)), nil)), cdr(cdr(KL_ARG_V2850_1466)))]) if ((shen_consp(cdr(cdr(KL_ARG_V2850_1466))) if shen_consp(cdr(KL_ARG_V2850_1466)) else False) if shen_consp(KL_ARG_V2850_1466) else False) else (Cons(tco_apply(shen_curry, [car(KL_ARG_V2850_1466)]), Cons(tco_apply(shen_curry, [car(cdr(KL_ARG_V2850_1466))]), nil)) if ((shen_eq(nil, cdr(cdr(KL_ARG_V2850_1466))) if shen_consp(cdr(KL_ARG_V2850_1466)) else False) if shen_consp(KL_ARG_V2850_1466) else False) else (KL_ARG_V2850_1466 if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.curry', shen_curry, 1)

@tail_recursion
def shen_specialx63(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_specialx63, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2851_1467 = FUN_ARGS[0]
    global symdic
    return tail_call(kl_elementx63, [KL_ARG_V2851_1467, shen_get(symdic.symdic_shen_x42specialx42)])
shen_add_fun('shen.special?', shen_specialx63, 1)

@tail_recursion
def shen_extraspecialx63(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_extraspecialx63, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2852_1468 = FUN_ARGS[0]
    global symdic
    return tail_call(kl_elementx63, [KL_ARG_V2852_1468, shen_get(symdic.symdic_shen_x42extraspecialx42)])
shen_add_fun('shen.extraspecial?', shen_extraspecialx63, 1)

@tail_recursion
def shen_tx42(*FUN_ARGS):
    FUN_ARITY = 4
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_tx42, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2853_1469 = FUN_ARGS[0]
    KL_ARG_V2854_1470 = FUN_ARGS[1]
    KL_ARG_V2855_1471 = FUN_ARGS[2]
    KL_ARG_V2856_1472 = FUN_ARGS[3]

    class KL_Context:
        KL_LOC_Throwcontrol_1473 = None
        KL_LOC_Case_1474 = None
        KL_LOC_Error_1475 = None
        KL_LOC_Case_1476 = None
        KL_LOC_V2842_1477 = None
        KL_LOC_Case_1478 = None
        KL_LOC_V2843_1479 = None
        KL_LOC_X_1480 = None
        KL_LOC_V2844_1481 = None
        KL_LOC_V2845_1482 = None
        KL_LOC_V2846_1483 = None
        KL_LOC_A_1484 = None
        KL_LOC_V2847_1485 = None
        KL_LOC_Datatypes_1486 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Throwcontrol_1473', tco_apply(shen_catchpoint, [])), tail_call(shen_cutpoint, [KL_CTX.KL_LOC_Throwcontrol_1473, [setattr(KL_CTX, 'KL_LOC_Case_1474', [setattr(KL_CTX, 'KL_LOC_Error_1475', tco_apply(shen_newpv, [KL_ARG_V2855_1471])), [tco_apply(shen_incinfs, []), tco_apply(kl_fwhen, [tco_apply(shen_maxinfexceededx63, []), KL_ARG_V2855_1471, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Error_1475, tco_apply(shen_errormaxinfs, []), KL_ARG_V2855_1471, KL_ARG_V2856_1472]))])][(-1)]][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1476', [setattr(KL_CTX, 'KL_LOC_V2842_1477', tco_apply(shen_lazyderef, [KL_ARG_V2853_1469, KL_ARG_V2855_1471])), ([tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1473, KL_ARG_V2855_1471, (lambda : tail_call(shen_prologx45failure, [KL_ARG_V2855_1471, KL_ARG_V2856_1472]))])][(-1)] if shen_eq(symdic.symdic_kl_fail, KL_CTX.KL_LOC_V2842_1477) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1478', [setattr(KL_CTX, 'KL_LOC_V2843_1479', tco_apply(shen_lazyderef, [KL_ARG_V2853_1469, KL_ARG_V2855_1471])), ([setattr(KL_CTX, 'KL_LOC_X_1480', car(KL_CTX.KL_LOC_V2843_1479)), [setattr(KL_CTX, 'KL_LOC_V2844_1481', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2843_1479), KL_ARG_V2855_1471])), ([setattr(KL_CTX, 'KL_LOC_V2845_1482', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2844_1481), KL_ARG_V2855_1471])), ([setattr(KL_CTX, 'KL_LOC_V2846_1483', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2844_1481), KL_ARG_V2855_1471])), ([setattr(KL_CTX, 'KL_LOC_A_1484', car(KL_CTX.KL_LOC_V2846_1483)), [setattr(KL_CTX, 'KL_LOC_V2847_1485', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2846_1483), KL_ARG_V2855_1471])), ([tco_apply(shen_incinfs, []), tco_apply(kl_fwhen, [tco_apply(shen_typex45theoryx45enabledx63, []), KL_ARG_V2855_1471, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1473, KL_ARG_V2855_1471, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_X_1480, KL_CTX.KL_LOC_A_1484, KL_ARG_V2854_1470, KL_ARG_V2855_1471, KL_ARG_V2856_1472]))]))])][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2847_1485) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2846_1483) else False)][(-1)] if shen_eq(symdic.symdic_kl_x58, KL_CTX.KL_LOC_V2845_1482) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2844_1481) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2843_1479) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Datatypes_1486', tco_apply(shen_newpv, [KL_ARG_V2855_1471])), [tco_apply(shen_incinfs, []), tco_apply(shen_show, [KL_ARG_V2853_1469, KL_ARG_V2854_1470, KL_ARG_V2855_1471, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Datatypes_1486, shen_get(symdic.symdic_shen_x42datatypesx42), KL_ARG_V2855_1471, (lambda : tail_call(shen_udefsx42, [KL_ARG_V2853_1469, KL_ARG_V2854_1470, KL_CTX.KL_LOC_Datatypes_1486, KL_ARG_V2855_1471, KL_ARG_V2856_1472]))]))])][(-1)]][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1478, False) else KL_CTX.KL_LOC_Case_1478)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1476, False) else KL_CTX.KL_LOC_Case_1476)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1474, False) else KL_CTX.KL_LOC_Case_1474)][(-1)]])][(-1)]
shen_add_fun('shen.t*', shen_tx42, 4)

@tail_recursion
def shen_typex45theoryx45enabledx63(*FUN_ARGS):
    FUN_ARITY = 0
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_typex45theoryx45enabledx63, (FUN_ARGS + lambdaargs)))
    global symdic
    return shen_get(symdic.symdic_shen_x42shenx45typex45theoryx45enabledx63x42)
shen_add_fun('shen.type-theory-enabled?', shen_typex45theoryx45enabledx63, 0)

@tail_recursion
def kl_enablex45typex45theory(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_enablex45typex45theory, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2861_1487 = FUN_ARGS[0]
    global symdic
    return (shen_set(symdic.symdic_shen_x42shenx45typex45theoryx45enabledx63x42, True) if shen_eq(symdic.symdic_kl_x43, KL_ARG_V2861_1487) else (shen_set(symdic.symdic_shen_x42shenx45typex45theoryx45enabledx63x42, False) if shen_eq(symdic.symdic_kl_x45, KL_ARG_V2861_1487) else (shen_simple_error('enable-type-theory expects a + or a -\r\n') if True else shen_simple_error('condition failure'))))
shen_add_fun('enable-type-theory', kl_enablex45typex45theory, 1)

@tail_recursion
def shen_prologx45failure(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_prologx45failure, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2870_1488 = FUN_ARGS[0]
    KL_ARG_V2871_1489 = FUN_ARGS[1]
    global symdic
    return False
shen_add_fun('shen.prolog-failure', shen_prologx45failure, 2)

@tail_recursion
def shen_maxinfexceededx63(*FUN_ARGS):
    FUN_ARITY = 0
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_maxinfexceededx63, (FUN_ARGS + lambdaargs)))
    global symdic
    return (tco_apply(kl_inferences, []) > shen_get(symdic.symdic_shen_x42maxinferencesx42))
shen_add_fun('shen.maxinfexceeded?', shen_maxinfexceededx63, 0)

@tail_recursion
def shen_errormaxinfs(*FUN_ARGS):
    FUN_ARITY = 0
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_errormaxinfs, (FUN_ARGS + lambdaargs)))
    global symdic
    return shen_simple_error('maximum inferences exceeded~%')
shen_add_fun('shen.errormaxinfs', shen_errormaxinfs, 0)

@tail_recursion
def shen_udefsx42(*FUN_ARGS):
    FUN_ARITY = 5
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_udefsx42, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2872_1490 = FUN_ARGS[0]
    KL_ARG_V2873_1491 = FUN_ARGS[1]
    KL_ARG_V2874_1492 = FUN_ARGS[2]
    KL_ARG_V2875_1493 = FUN_ARGS[3]
    KL_ARG_V2876_1494 = FUN_ARGS[4]

    class KL_Context:
        KL_LOC_Case_1495 = None
        KL_LOC_V2838_1496 = None
        KL_LOC_D_1497 = None
        KL_LOC_V2839_1498 = None
        KL_LOC_Ds_1499 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Case_1495', [setattr(KL_CTX, 'KL_LOC_V2838_1496', tco_apply(shen_lazyderef, [KL_ARG_V2874_1492, KL_ARG_V2875_1493])), ([setattr(KL_CTX, 'KL_LOC_D_1497', car(KL_CTX.KL_LOC_V2838_1496)), [tco_apply(shen_incinfs, []), tco_apply(kl_call, [Cons(KL_CTX.KL_LOC_D_1497, Cons(KL_ARG_V2872_1490, Cons(KL_ARG_V2873_1491, nil))), KL_ARG_V2875_1493, KL_ARG_V2876_1494])][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2838_1496) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_V2839_1498', tco_apply(shen_lazyderef, [KL_ARG_V2874_1492, KL_ARG_V2875_1493])), ([setattr(KL_CTX, 'KL_LOC_Ds_1499', cdr(KL_CTX.KL_LOC_V2839_1498)), [tco_apply(shen_incinfs, []), tail_call(shen_udefsx42, [KL_ARG_V2872_1490, KL_ARG_V2873_1491, KL_CTX.KL_LOC_Ds_1499, KL_ARG_V2875_1493, KL_ARG_V2876_1494])][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2839_1498) else False)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1495, False) else KL_CTX.KL_LOC_Case_1495)][(-1)]
shen_add_fun('shen.udefs*', shen_udefsx42, 5)

@tail_recursion
def shen_thx42(*FUN_ARGS):
    FUN_ARITY = 5
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_thx42, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2877_1500 = FUN_ARGS[0]
    KL_ARG_V2878_1501 = FUN_ARGS[1]
    KL_ARG_V2879_1502 = FUN_ARGS[2]
    KL_ARG_V2880_1503 = FUN_ARGS[3]
    KL_ARG_V2881_1504 = FUN_ARGS[4]

    class KL_Context:
        KL_LOC_Throwcontrol_1505 = None
        KL_LOC_Case_1506 = None
        KL_LOC_Case_1507 = None
        KL_LOC_F_1508 = None
        KL_LOC_Case_1509 = None
        KL_LOC_Case_1510 = None
        KL_LOC_Case_1511 = None
        KL_LOC_V2717_1512 = None
        KL_LOC_F_1513 = None
        KL_LOC_V2718_1514 = None
        KL_LOC_Case_1515 = None
        KL_LOC_V2719_1516 = None
        KL_LOC_F_1517 = None
        KL_LOC_V2720_1518 = None
        KL_LOC_X_1519 = None
        KL_LOC_V2721_1520 = None
        KL_LOC_B_1521 = None
        KL_LOC_Case_1522 = None
        KL_LOC_V2722_1523 = None
        KL_LOC_V2723_1524 = None
        KL_LOC_V2724_1525 = None
        KL_LOC_X_1526 = None
        KL_LOC_V2725_1527 = None
        KL_LOC_Y_1528 = None
        KL_LOC_V2726_1529 = None
        KL_LOC_V2727_1530 = None
        KL_LOC_V2728_1531 = None
        KL_LOC_V2729_1532 = None
        KL_LOC_A_1533 = None
        KL_LOC_V2730_1534 = None
        KL_LOC_Result_1535 = None
        KL_LOC_A_1536 = None
        KL_LOC_Result_1537 = None
        KL_LOC_Result_1538 = None
        KL_LOC_V2731_1539 = None
        KL_LOC_A_1540 = None
        KL_LOC_V2732_1541 = None
        KL_LOC_Result_1542 = None
        KL_LOC_A_1543 = None
        KL_LOC_Result_1544 = None
        KL_LOC_A_1545 = None
        KL_LOC_Result_1546 = None
        KL_LOC_Case_1547 = None
        KL_LOC_V2733_1548 = None
        KL_LOC_V2734_1549 = None
        KL_LOC_V2735_1550 = None
        KL_LOC_X_1551 = None
        KL_LOC_V2736_1552 = None
        KL_LOC_Y_1553 = None
        KL_LOC_V2737_1554 = None
        KL_LOC_V2738_1555 = None
        KL_LOC_A_1556 = None
        KL_LOC_V2739_1557 = None
        KL_LOC_V2740_1558 = None
        KL_LOC_V2741_1559 = None
        KL_LOC_B_1560 = None
        KL_LOC_V2742_1561 = None
        KL_LOC_Result_1562 = None
        KL_LOC_B_1563 = None
        KL_LOC_Result_1564 = None
        KL_LOC_Result_1565 = None
        KL_LOC_V2743_1566 = None
        KL_LOC_B_1567 = None
        KL_LOC_V2744_1568 = None
        KL_LOC_Result_1569 = None
        KL_LOC_B_1570 = None
        KL_LOC_Result_1571 = None
        KL_LOC_B_1572 = None
        KL_LOC_Result_1573 = None
        KL_LOC_A_1574 = None
        KL_LOC_B_1575 = None
        KL_LOC_Result_1576 = None
        KL_LOC_Case_1577 = None
        KL_LOC_V2745_1578 = None
        KL_LOC_V2746_1579 = None
        KL_LOC_V2747_1580 = None
        KL_LOC_X_1581 = None
        KL_LOC_V2748_1582 = None
        KL_LOC_Y_1583 = None
        KL_LOC_V2749_1584 = None
        KL_LOC_V2750_1585 = None
        KL_LOC_V2751_1586 = None
        KL_LOC_V2752_1587 = None
        KL_LOC_A_1588 = None
        KL_LOC_V2753_1589 = None
        KL_LOC_Result_1590 = None
        KL_LOC_A_1591 = None
        KL_LOC_Result_1592 = None
        KL_LOC_Result_1593 = None
        KL_LOC_V2754_1594 = None
        KL_LOC_A_1595 = None
        KL_LOC_V2755_1596 = None
        KL_LOC_Result_1597 = None
        KL_LOC_A_1598 = None
        KL_LOC_Result_1599 = None
        KL_LOC_A_1600 = None
        KL_LOC_Result_1601 = None
        KL_LOC_Case_1602 = None
        KL_LOC_V2756_1603 = None
        KL_LOC_V2757_1604 = None
        KL_LOC_V2758_1605 = None
        KL_LOC_X_1606 = None
        KL_LOC_V2759_1607 = None
        KL_LOC_Y_1608 = None
        KL_LOC_V2760_1609 = None
        KL_LOC_V2761_1610 = None
        KL_LOC_Result_1611 = None
        KL_LOC_Case_1612 = None
        KL_LOC_V2762_1613 = None
        KL_LOC_V2763_1614 = None
        KL_LOC_V2764_1615 = None
        KL_LOC_X_1616 = None
        KL_LOC_V2765_1617 = None
        KL_LOC_Y_1618 = None
        KL_LOC_V2766_1619 = None
        KL_LOC_V2767_1620 = None
        KL_LOC_A_1621 = None
        KL_LOC_V2768_1622 = None
        KL_LOC_V2769_1623 = None
        KL_LOC_V2770_1624 = None
        KL_LOC_B_1625 = None
        KL_LOC_V2771_1626 = None
        KL_LOC_Z_1627 = None
        KL_LOC_Xx38x38_1628 = None
        KL_LOC_Result_1629 = None
        KL_LOC_Z_1630 = None
        KL_LOC_Xx38x38_1631 = None
        KL_LOC_B_1632 = None
        KL_LOC_Result_1633 = None
        KL_LOC_Z_1634 = None
        KL_LOC_Xx38x38_1635 = None
        KL_LOC_Result_1636 = None
        KL_LOC_V2772_1637 = None
        KL_LOC_B_1638 = None
        KL_LOC_V2773_1639 = None
        KL_LOC_Z_1640 = None
        KL_LOC_Xx38x38_1641 = None
        KL_LOC_Result_1642 = None
        KL_LOC_Z_1643 = None
        KL_LOC_Xx38x38_1644 = None
        KL_LOC_B_1645 = None
        KL_LOC_Result_1646 = None
        KL_LOC_Z_1647 = None
        KL_LOC_Xx38x38_1648 = None
        KL_LOC_B_1649 = None
        KL_LOC_Result_1650 = None
        KL_LOC_Z_1651 = None
        KL_LOC_Xx38x38_1652 = None
        KL_LOC_A_1653 = None
        KL_LOC_B_1654 = None
        KL_LOC_Result_1655 = None
        KL_LOC_Z_1656 = None
        KL_LOC_Xx38x38_1657 = None
        KL_LOC_Case_1658 = None
        KL_LOC_V2774_1659 = None
        KL_LOC_V2775_1660 = None
        KL_LOC_V2776_1661 = None
        KL_LOC_X_1662 = None
        KL_LOC_V2777_1663 = None
        KL_LOC_Y_1664 = None
        KL_LOC_V2778_1665 = None
        KL_LOC_Z_1666 = None
        KL_LOC_V2779_1667 = None
        KL_LOC_W_1668 = None
        KL_LOC_Xx38x38_1669 = None
        KL_LOC_B_1670 = None
        KL_LOC_Case_1671 = None
        KL_LOC_V2780_1672 = None
        KL_LOC_V2781_1673 = None
        KL_LOC_V2782_1674 = None
        KL_LOC_V2783_1675 = None
        KL_LOC_V2784_1676 = None
        KL_LOC_FileName_1677 = None
        KL_LOC_V2785_1678 = None
        KL_LOC_Direction2713_1679 = None
        KL_LOC_V2786_1680 = None
        KL_LOC_V2787_1681 = None
        KL_LOC_V2788_1682 = None
        KL_LOC_V2789_1683 = None
        KL_LOC_Direction_1684 = None
        KL_LOC_V2790_1685 = None
        KL_LOC_Result_1686 = None
        KL_LOC_Direction_1687 = None
        KL_LOC_Result_1688 = None
        KL_LOC_Result_1689 = None
        KL_LOC_V2791_1690 = None
        KL_LOC_Direction_1691 = None
        KL_LOC_V2792_1692 = None
        KL_LOC_Result_1693 = None
        KL_LOC_Direction_1694 = None
        KL_LOC_Result_1695 = None
        KL_LOC_Direction_1696 = None
        KL_LOC_Result_1697 = None
        KL_LOC_Case_1698 = None
        KL_LOC_V2793_1699 = None
        KL_LOC_V2794_1700 = None
        KL_LOC_V2795_1701 = None
        KL_LOC_X_1702 = None
        KL_LOC_V2796_1703 = None
        KL_LOC_A_1704 = None
        KL_LOC_V2797_1705 = None
        KL_LOC_Case_1706 = None
        KL_LOC_V2798_1707 = None
        KL_LOC_V2799_1708 = None
        KL_LOC_V2800_1709 = None
        KL_LOC_V2801_1710 = None
        KL_LOC_V2802_1711 = None
        KL_LOC_A_1712 = None
        KL_LOC_V2803_1713 = None
        KL_LOC_C_1714 = None
        KL_LOC_Case_1715 = None
        KL_LOC_V2804_1716 = None
        KL_LOC_V2805_1717 = None
        KL_LOC_V2806_1718 = None
        KL_LOC_V2807_1719 = None
        KL_LOC_V2808_1720 = None
        KL_LOC_A_1721 = None
        KL_LOC_V2809_1722 = None
        KL_LOC_C_1723 = None
        KL_LOC_Case_1724 = None
        KL_LOC_V2810_1725 = None
        KL_LOC_V2811_1726 = None
        KL_LOC_V2812_1727 = None
        KL_LOC_Var_1728 = None
        KL_LOC_V2813_1729 = None
        KL_LOC_Val_1730 = None
        KL_LOC_V2814_1731 = None
        KL_LOC_Case_1732 = None
        KL_LOC_V2815_1733 = None
        KL_LOC_V2816_1734 = None
        KL_LOC_V2817_1735 = None
        KL_LOC_F_1736 = None
        KL_LOC_V2818_1737 = None
        KL_LOC_A_1738 = None
        KL_LOC_Fx38x38_1739 = None
        KL_LOC_B_1740 = None
        KL_LOC_Case_1741 = None
        KL_LOC_V2819_1742 = None
        KL_LOC_V2820_1743 = None
        KL_LOC_V2821_1744 = None
        KL_LOC_V2822_1745 = None
        KL_LOC_Result_1746 = None
        KL_LOC_Case_1747 = None
        KL_LOC_NewHyp_1748 = None
        KL_LOC_Case_1749 = None
        KL_LOC_V2823_1750 = None
        KL_LOC_V2824_1751 = None
        KL_LOC_V2825_1752 = None
        KL_LOC_F_1753 = None
        KL_LOC_X_1754 = None
        KL_LOC_Case_1755 = None
        KL_LOC_V2826_1756 = None
        KL_LOC_V2827_1757 = None
        KL_LOC_V2828_1758 = None
        KL_LOC_F_1759 = None
        KL_LOC_X_1760 = None
        KL_LOC_Case_1761 = None
        KL_LOC_V2829_1762 = None
        KL_LOC_V2830_1763 = None
        KL_LOC_V2831_1764 = None
        KL_LOC_Result_1765 = None
        KL_LOC_Case_1766 = None
        KL_LOC_V2832_1767 = None
        KL_LOC_V2833_1768 = None
        KL_LOC_V2834_1769 = None
        KL_LOC_Result_1770 = None
        KL_LOC_Datatypes_1771 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Throwcontrol_1505', tco_apply(shen_catchpoint, [])), tail_call(shen_cutpoint, [KL_CTX.KL_LOC_Throwcontrol_1505, [setattr(KL_CTX, 'KL_LOC_Case_1506', [tco_apply(shen_incinfs, []), tco_apply(shen_show, [Cons(KL_ARG_V2877_1500, Cons(symdic.symdic_kl_x58, Cons(KL_ARG_V2878_1501, nil))), KL_ARG_V2879_1502, KL_ARG_V2880_1503, (lambda : tail_call(kl_fwhen, [False, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))])][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1507', [setattr(KL_CTX, 'KL_LOC_F_1508', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_incinfs, []), tco_apply(kl_fwhen, [tco_apply(shen_typedfx63, [tco_apply(shen_lazyderef, [KL_ARG_V2877_1500, KL_ARG_V2880_1503])]), KL_ARG_V2880_1503, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_F_1508, tco_apply(shen_sigf, [tco_apply(shen_lazyderef, [KL_ARG_V2877_1500, KL_ARG_V2880_1503])]), KL_ARG_V2880_1503, (lambda : tail_call(kl_call, [Cons(KL_CTX.KL_LOC_F_1508, Cons(KL_ARG_V2878_1501, nil)), KL_ARG_V2880_1503, KL_ARG_V2881_1504]))]))])][(-1)]][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1509', [tco_apply(shen_incinfs, []), tco_apply(shen_base, [KL_ARG_V2877_1500, KL_ARG_V2878_1501, KL_ARG_V2880_1503, KL_ARG_V2881_1504])][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1510', [tco_apply(shen_incinfs, []), tco_apply(shen_by_hypothesis, [KL_ARG_V2877_1500, KL_ARG_V2878_1501, KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504])][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1511', [setattr(KL_CTX, 'KL_LOC_V2717_1512', tco_apply(shen_lazyderef, [KL_ARG_V2877_1500, KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_F_1513', car(KL_CTX.KL_LOC_V2717_1512)), [setattr(KL_CTX, 'KL_LOC_V2718_1514', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2717_1512), KL_ARG_V2880_1503])), ([tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_F_1513, Cons(symdic.symdic_kl_x45x45x62, Cons(KL_ARG_V2878_1501, nil)), KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504])][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2718_1514) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2717_1512) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1515', [setattr(KL_CTX, 'KL_LOC_V2719_1516', tco_apply(shen_lazyderef, [KL_ARG_V2877_1500, KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_F_1517', car(KL_CTX.KL_LOC_V2719_1516)), [setattr(KL_CTX, 'KL_LOC_V2720_1518', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2719_1516), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_X_1519', car(KL_CTX.KL_LOC_V2720_1518)), [setattr(KL_CTX, 'KL_LOC_V2721_1520', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2720_1518), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_B_1521', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_F_1517, Cons(KL_CTX.KL_LOC_B_1521, Cons(symdic.symdic_kl_x45x45x62, Cons(KL_ARG_V2878_1501, nil))), KL_ARG_V2879_1502, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_X_1519, KL_CTX.KL_LOC_B_1521, KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))])][(-1)]][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2721_1520) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2720_1518) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2719_1516) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1522', [setattr(KL_CTX, 'KL_LOC_V2722_1523', tco_apply(shen_lazyderef, [KL_ARG_V2877_1500, KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2723_1524', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2722_1523), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2724_1525', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2722_1523), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_X_1526', car(KL_CTX.KL_LOC_V2724_1525)), [setattr(KL_CTX, 'KL_LOC_V2725_1527', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2724_1525), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_Y_1528', car(KL_CTX.KL_LOC_V2725_1527)), [setattr(KL_CTX, 'KL_LOC_V2726_1529', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2725_1527), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2727_1530', tco_apply(shen_lazyderef, [KL_ARG_V2878_1501, KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2728_1531', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2727_1530), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2729_1532', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2727_1530), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_A_1533', car(KL_CTX.KL_LOC_V2729_1532)), [setattr(KL_CTX, 'KL_LOC_V2730_1534', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2729_1532), KL_ARG_V2880_1503])), ([tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1526, KL_CTX.KL_LOC_A_1533, KL_ARG_V2879_1502, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1528, Cons(symdic.symdic_kl_list, Cons(KL_CTX.KL_LOC_A_1533, nil)), KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))])][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2730_1534) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2730_1534, nil, KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1535', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1526, KL_CTX.KL_LOC_A_1533, KL_ARG_V2879_1502, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1528, Cons(symdic.symdic_kl_list, Cons(KL_CTX.KL_LOC_A_1533, nil)), KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2730_1534, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1535][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2730_1534]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2729_1532) else ([setattr(KL_CTX, 'KL_LOC_A_1536', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2729_1532, Cons(KL_CTX.KL_LOC_A_1536, nil), KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1537', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1526, KL_CTX.KL_LOC_A_1536, KL_ARG_V2879_1502, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1528, Cons(symdic.symdic_kl_list, Cons(KL_CTX.KL_LOC_A_1536, nil)), KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2729_1532, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1537][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2729_1532]) else False))][(-1)] if shen_eq(symdic.symdic_kl_list, KL_CTX.KL_LOC_V2728_1531) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2728_1531, symdic.symdic_kl_list, KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1538', [setattr(KL_CTX, 'KL_LOC_V2731_1539', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2727_1530), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_A_1540', car(KL_CTX.KL_LOC_V2731_1539)), [setattr(KL_CTX, 'KL_LOC_V2732_1541', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2731_1539), KL_ARG_V2880_1503])), ([tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1526, KL_CTX.KL_LOC_A_1540, KL_ARG_V2879_1502, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1528, Cons(symdic.symdic_kl_list, Cons(KL_CTX.KL_LOC_A_1540, nil)), KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))])][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2732_1541) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2732_1541, nil, KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1542', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1526, KL_CTX.KL_LOC_A_1540, KL_ARG_V2879_1502, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1528, Cons(symdic.symdic_kl_list, Cons(KL_CTX.KL_LOC_A_1540, nil)), KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2732_1541, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1542][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2732_1541]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2731_1539) else ([setattr(KL_CTX, 'KL_LOC_A_1543', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2731_1539, Cons(KL_CTX.KL_LOC_A_1543, nil), KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1544', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1526, KL_CTX.KL_LOC_A_1543, KL_ARG_V2879_1502, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1528, Cons(symdic.symdic_kl_list, Cons(KL_CTX.KL_LOC_A_1543, nil)), KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2731_1539, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1544][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2731_1539]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2728_1531, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1538][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2728_1531]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2727_1530) else ([setattr(KL_CTX, 'KL_LOC_A_1545', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2727_1530, Cons(symdic.symdic_kl_list, Cons(KL_CTX.KL_LOC_A_1545, nil)), KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1546', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1526, KL_CTX.KL_LOC_A_1545, KL_ARG_V2879_1502, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1528, Cons(symdic.symdic_kl_list, Cons(KL_CTX.KL_LOC_A_1545, nil)), KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2727_1530, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1546][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2727_1530]) else False))][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2726_1529) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2725_1527) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2724_1525) else False)][(-1)] if shen_eq(symdic.symdic_kl_cons, KL_CTX.KL_LOC_V2723_1524) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2722_1523) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1547', [setattr(KL_CTX, 'KL_LOC_V2733_1548', tco_apply(shen_lazyderef, [KL_ARG_V2877_1500, KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2734_1549', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2733_1548), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2735_1550', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2733_1548), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_X_1551', car(KL_CTX.KL_LOC_V2735_1550)), [setattr(KL_CTX, 'KL_LOC_V2736_1552', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2735_1550), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_Y_1553', car(KL_CTX.KL_LOC_V2736_1552)), [setattr(KL_CTX, 'KL_LOC_V2737_1554', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2736_1552), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2738_1555', tco_apply(shen_lazyderef, [KL_ARG_V2878_1501, KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_A_1556', car(KL_CTX.KL_LOC_V2738_1555)), [setattr(KL_CTX, 'KL_LOC_V2739_1557', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2738_1555), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2740_1558', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2739_1557), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2741_1559', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2739_1557), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_B_1560', car(KL_CTX.KL_LOC_V2741_1559)), [setattr(KL_CTX, 'KL_LOC_V2742_1561', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2741_1559), KL_ARG_V2880_1503])), ([tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1551, KL_CTX.KL_LOC_A_1556, KL_ARG_V2879_1502, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1553, KL_CTX.KL_LOC_B_1560, KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))])][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2742_1561) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2742_1561, nil, KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1562', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1551, KL_CTX.KL_LOC_A_1556, KL_ARG_V2879_1502, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1553, KL_CTX.KL_LOC_B_1560, KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2742_1561, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1562][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2742_1561]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2741_1559) else ([setattr(KL_CTX, 'KL_LOC_B_1563', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2741_1559, Cons(KL_CTX.KL_LOC_B_1563, nil), KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1564', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1551, KL_CTX.KL_LOC_A_1556, KL_ARG_V2879_1502, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1553, KL_CTX.KL_LOC_B_1563, KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2741_1559, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1564][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2741_1559]) else False))][(-1)] if shen_eq(symdic.symdic_kl_x42, KL_CTX.KL_LOC_V2740_1558) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2740_1558, symdic.symdic_kl_x42, KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1565', [setattr(KL_CTX, 'KL_LOC_V2743_1566', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2739_1557), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_B_1567', car(KL_CTX.KL_LOC_V2743_1566)), [setattr(KL_CTX, 'KL_LOC_V2744_1568', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2743_1566), KL_ARG_V2880_1503])), ([tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1551, KL_CTX.KL_LOC_A_1556, KL_ARG_V2879_1502, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1553, KL_CTX.KL_LOC_B_1567, KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))])][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2744_1568) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2744_1568, nil, KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1569', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1551, KL_CTX.KL_LOC_A_1556, KL_ARG_V2879_1502, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1553, KL_CTX.KL_LOC_B_1567, KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2744_1568, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1569][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2744_1568]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2743_1566) else ([setattr(KL_CTX, 'KL_LOC_B_1570', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2743_1566, Cons(KL_CTX.KL_LOC_B_1570, nil), KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1571', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1551, KL_CTX.KL_LOC_A_1556, KL_ARG_V2879_1502, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1553, KL_CTX.KL_LOC_B_1570, KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2743_1566, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1571][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2743_1566]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2740_1558, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1565][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2740_1558]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2739_1557) else ([setattr(KL_CTX, 'KL_LOC_B_1572', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2739_1557, Cons(symdic.symdic_kl_x42, Cons(KL_CTX.KL_LOC_B_1572, nil)), KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1573', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1551, KL_CTX.KL_LOC_A_1556, KL_ARG_V2879_1502, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1553, KL_CTX.KL_LOC_B_1572, KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2739_1557, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1573][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2739_1557]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2738_1555) else ([setattr(KL_CTX, 'KL_LOC_A_1574', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [setattr(KL_CTX, 'KL_LOC_B_1575', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2738_1555, Cons(KL_CTX.KL_LOC_A_1574, Cons(symdic.symdic_kl_x42, Cons(KL_CTX.KL_LOC_B_1575, nil))), KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1576', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1551, KL_CTX.KL_LOC_A_1574, KL_ARG_V2879_1502, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1553, KL_CTX.KL_LOC_B_1575, KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2738_1555, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1576][(-1)]][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2738_1555]) else False))][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2737_1554) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2736_1552) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2735_1550) else False)][(-1)] if shen_eq(symdic.symdic_kl_x64p, KL_CTX.KL_LOC_V2734_1549) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2733_1548) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1577', [setattr(KL_CTX, 'KL_LOC_V2745_1578', tco_apply(shen_lazyderef, [KL_ARG_V2877_1500, KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2746_1579', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2745_1578), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2747_1580', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2745_1578), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_X_1581', car(KL_CTX.KL_LOC_V2747_1580)), [setattr(KL_CTX, 'KL_LOC_V2748_1582', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2747_1580), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_Y_1583', car(KL_CTX.KL_LOC_V2748_1582)), [setattr(KL_CTX, 'KL_LOC_V2749_1584', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2748_1582), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2750_1585', tco_apply(shen_lazyderef, [KL_ARG_V2878_1501, KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2751_1586', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2750_1585), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2752_1587', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2750_1585), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_A_1588', car(KL_CTX.KL_LOC_V2752_1587)), [setattr(KL_CTX, 'KL_LOC_V2753_1589', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2752_1587), KL_ARG_V2880_1503])), ([tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1581, KL_CTX.KL_LOC_A_1588, KL_ARG_V2879_1502, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1583, Cons(symdic.symdic_kl_vector, Cons(KL_CTX.KL_LOC_A_1588, nil)), KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))])][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2753_1589) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2753_1589, nil, KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1590', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1581, KL_CTX.KL_LOC_A_1588, KL_ARG_V2879_1502, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1583, Cons(symdic.symdic_kl_vector, Cons(KL_CTX.KL_LOC_A_1588, nil)), KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2753_1589, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1590][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2753_1589]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2752_1587) else ([setattr(KL_CTX, 'KL_LOC_A_1591', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2752_1587, Cons(KL_CTX.KL_LOC_A_1591, nil), KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1592', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1581, KL_CTX.KL_LOC_A_1591, KL_ARG_V2879_1502, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1583, Cons(symdic.symdic_kl_vector, Cons(KL_CTX.KL_LOC_A_1591, nil)), KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2752_1587, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1592][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2752_1587]) else False))][(-1)] if shen_eq(symdic.symdic_kl_vector, KL_CTX.KL_LOC_V2751_1586) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2751_1586, symdic.symdic_kl_vector, KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1593', [setattr(KL_CTX, 'KL_LOC_V2754_1594', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2750_1585), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_A_1595', car(KL_CTX.KL_LOC_V2754_1594)), [setattr(KL_CTX, 'KL_LOC_V2755_1596', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2754_1594), KL_ARG_V2880_1503])), ([tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1581, KL_CTX.KL_LOC_A_1595, KL_ARG_V2879_1502, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1583, Cons(symdic.symdic_kl_vector, Cons(KL_CTX.KL_LOC_A_1595, nil)), KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))])][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2755_1596) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2755_1596, nil, KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1597', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1581, KL_CTX.KL_LOC_A_1595, KL_ARG_V2879_1502, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1583, Cons(symdic.symdic_kl_vector, Cons(KL_CTX.KL_LOC_A_1595, nil)), KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2755_1596, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1597][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2755_1596]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2754_1594) else ([setattr(KL_CTX, 'KL_LOC_A_1598', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2754_1594, Cons(KL_CTX.KL_LOC_A_1598, nil), KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1599', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1581, KL_CTX.KL_LOC_A_1598, KL_ARG_V2879_1502, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1583, Cons(symdic.symdic_kl_vector, Cons(KL_CTX.KL_LOC_A_1598, nil)), KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2754_1594, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1599][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2754_1594]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2751_1586, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1593][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2751_1586]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2750_1585) else ([setattr(KL_CTX, 'KL_LOC_A_1600', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2750_1585, Cons(symdic.symdic_kl_vector, Cons(KL_CTX.KL_LOC_A_1600, nil)), KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1601', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1581, KL_CTX.KL_LOC_A_1600, KL_ARG_V2879_1502, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1583, Cons(symdic.symdic_kl_vector, Cons(KL_CTX.KL_LOC_A_1600, nil)), KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2750_1585, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1601][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2750_1585]) else False))][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2749_1584) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2748_1582) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2747_1580) else False)][(-1)] if shen_eq(symdic.symdic_kl_x64v, KL_CTX.KL_LOC_V2746_1579) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2745_1578) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1602', [setattr(KL_CTX, 'KL_LOC_V2756_1603', tco_apply(shen_lazyderef, [KL_ARG_V2877_1500, KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2757_1604', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2756_1603), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2758_1605', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2756_1603), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_X_1606', car(KL_CTX.KL_LOC_V2758_1605)), [setattr(KL_CTX, 'KL_LOC_V2759_1607', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2758_1605), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_Y_1608', car(KL_CTX.KL_LOC_V2759_1607)), [setattr(KL_CTX, 'KL_LOC_V2760_1609', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2759_1607), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2761_1610', tco_apply(shen_lazyderef, [KL_ARG_V2878_1501, KL_ARG_V2880_1503])), ([tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1606, symdic.symdic_kl_string, KL_ARG_V2879_1502, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1608, symdic.symdic_kl_string, KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))])][(-1)] if shen_eq(symdic.symdic_kl_string, KL_CTX.KL_LOC_V2761_1610) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2761_1610, symdic.symdic_kl_string, KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1611', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1606, symdic.symdic_kl_string, KL_ARG_V2879_1502, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1608, symdic.symdic_kl_string, KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2761_1610, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1611][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2761_1610]) else False))][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2760_1609) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2759_1607) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2758_1605) else False)][(-1)] if shen_eq(symdic.symdic_kl_x64s, KL_CTX.KL_LOC_V2757_1604) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2756_1603) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1612', [setattr(KL_CTX, 'KL_LOC_V2762_1613', tco_apply(shen_lazyderef, [KL_ARG_V2877_1500, KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2763_1614', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2762_1613), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2764_1615', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2762_1613), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_X_1616', car(KL_CTX.KL_LOC_V2764_1615)), [setattr(KL_CTX, 'KL_LOC_V2765_1617', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2764_1615), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_Y_1618', car(KL_CTX.KL_LOC_V2765_1617)), [setattr(KL_CTX, 'KL_LOC_V2766_1619', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2765_1617), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2767_1620', tco_apply(shen_lazyderef, [KL_ARG_V2878_1501, KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_A_1621', car(KL_CTX.KL_LOC_V2767_1620)), [setattr(KL_CTX, 'KL_LOC_V2768_1622', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2767_1620), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2769_1623', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2768_1622), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2770_1624', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2768_1622), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_B_1625', car(KL_CTX.KL_LOC_V2770_1624)), [setattr(KL_CTX, 'KL_LOC_V2771_1626', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2770_1624), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_Z_1627', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [setattr(KL_CTX, 'KL_LOC_Xx38x38_1628', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1505, KL_ARG_V2880_1503, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Xx38x38_1628, tco_apply(shen_placeholder, []), KL_ARG_V2880_1503, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Z_1627, tco_apply(shen_ebr, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Xx38x38_1628, KL_ARG_V2880_1503]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1616, KL_ARG_V2880_1503]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1618, KL_ARG_V2880_1503])]), KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Z_1627, KL_CTX.KL_LOC_B_1625, Cons(Cons(KL_CTX.KL_LOC_Xx38x38_1628, Cons(symdic.symdic_kl_x58, Cons(KL_CTX.KL_LOC_A_1621, nil))), KL_ARG_V2879_1502), KL_ARG_V2880_1503, KL_ARG_V2881_1504]))]))]))])][(-1)]][(-1)]][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2771_1626) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2771_1626, nil, KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1629', [setattr(KL_CTX, 'KL_LOC_Z_1630', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [setattr(KL_CTX, 'KL_LOC_Xx38x38_1631', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1505, KL_ARG_V2880_1503, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Xx38x38_1631, tco_apply(shen_placeholder, []), KL_ARG_V2880_1503, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Z_1630, tco_apply(shen_ebr, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Xx38x38_1631, KL_ARG_V2880_1503]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1616, KL_ARG_V2880_1503]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1618, KL_ARG_V2880_1503])]), KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Z_1630, KL_CTX.KL_LOC_B_1625, Cons(Cons(KL_CTX.KL_LOC_Xx38x38_1631, Cons(symdic.symdic_kl_x58, Cons(KL_CTX.KL_LOC_A_1621, nil))), KL_ARG_V2879_1502), KL_ARG_V2880_1503, KL_ARG_V2881_1504]))]))]))])][(-1)]][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2771_1626, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1629][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2771_1626]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2770_1624) else ([setattr(KL_CTX, 'KL_LOC_B_1632', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2770_1624, Cons(KL_CTX.KL_LOC_B_1632, nil), KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1633', [setattr(KL_CTX, 'KL_LOC_Z_1634', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [setattr(KL_CTX, 'KL_LOC_Xx38x38_1635', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1505, KL_ARG_V2880_1503, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Xx38x38_1635, tco_apply(shen_placeholder, []), KL_ARG_V2880_1503, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Z_1634, tco_apply(shen_ebr, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Xx38x38_1635, KL_ARG_V2880_1503]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1616, KL_ARG_V2880_1503]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1618, KL_ARG_V2880_1503])]), KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Z_1634, KL_CTX.KL_LOC_B_1632, Cons(Cons(KL_CTX.KL_LOC_Xx38x38_1635, Cons(symdic.symdic_kl_x58, Cons(KL_CTX.KL_LOC_A_1621, nil))), KL_ARG_V2879_1502), KL_ARG_V2880_1503, KL_ARG_V2881_1504]))]))]))])][(-1)]][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2770_1624, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1633][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2770_1624]) else False))][(-1)] if shen_eq(symdic.symdic_kl_x45x45x62, KL_CTX.KL_LOC_V2769_1623) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2769_1623, symdic.symdic_kl_x45x45x62, KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1636', [setattr(KL_CTX, 'KL_LOC_V2772_1637', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2768_1622), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_B_1638', car(KL_CTX.KL_LOC_V2772_1637)), [setattr(KL_CTX, 'KL_LOC_V2773_1639', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2772_1637), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_Z_1640', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [setattr(KL_CTX, 'KL_LOC_Xx38x38_1641', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1505, KL_ARG_V2880_1503, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Xx38x38_1641, tco_apply(shen_placeholder, []), KL_ARG_V2880_1503, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Z_1640, tco_apply(shen_ebr, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Xx38x38_1641, KL_ARG_V2880_1503]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1616, KL_ARG_V2880_1503]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1618, KL_ARG_V2880_1503])]), KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Z_1640, KL_CTX.KL_LOC_B_1638, Cons(Cons(KL_CTX.KL_LOC_Xx38x38_1641, Cons(symdic.symdic_kl_x58, Cons(KL_CTX.KL_LOC_A_1621, nil))), KL_ARG_V2879_1502), KL_ARG_V2880_1503, KL_ARG_V2881_1504]))]))]))])][(-1)]][(-1)]][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2773_1639) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2773_1639, nil, KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1642', [setattr(KL_CTX, 'KL_LOC_Z_1643', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [setattr(KL_CTX, 'KL_LOC_Xx38x38_1644', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1505, KL_ARG_V2880_1503, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Xx38x38_1644, tco_apply(shen_placeholder, []), KL_ARG_V2880_1503, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Z_1643, tco_apply(shen_ebr, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Xx38x38_1644, KL_ARG_V2880_1503]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1616, KL_ARG_V2880_1503]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1618, KL_ARG_V2880_1503])]), KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Z_1643, KL_CTX.KL_LOC_B_1638, Cons(Cons(KL_CTX.KL_LOC_Xx38x38_1644, Cons(symdic.symdic_kl_x58, Cons(KL_CTX.KL_LOC_A_1621, nil))), KL_ARG_V2879_1502), KL_ARG_V2880_1503, KL_ARG_V2881_1504]))]))]))])][(-1)]][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2773_1639, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1642][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2773_1639]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2772_1637) else ([setattr(KL_CTX, 'KL_LOC_B_1645', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2772_1637, Cons(KL_CTX.KL_LOC_B_1645, nil), KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1646', [setattr(KL_CTX, 'KL_LOC_Z_1647', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [setattr(KL_CTX, 'KL_LOC_Xx38x38_1648', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1505, KL_ARG_V2880_1503, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Xx38x38_1648, tco_apply(shen_placeholder, []), KL_ARG_V2880_1503, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Z_1647, tco_apply(shen_ebr, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Xx38x38_1648, KL_ARG_V2880_1503]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1616, KL_ARG_V2880_1503]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1618, KL_ARG_V2880_1503])]), KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Z_1647, KL_CTX.KL_LOC_B_1645, Cons(Cons(KL_CTX.KL_LOC_Xx38x38_1648, Cons(symdic.symdic_kl_x58, Cons(KL_CTX.KL_LOC_A_1621, nil))), KL_ARG_V2879_1502), KL_ARG_V2880_1503, KL_ARG_V2881_1504]))]))]))])][(-1)]][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2772_1637, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1646][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2772_1637]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2769_1623, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1636][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2769_1623]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2768_1622) else ([setattr(KL_CTX, 'KL_LOC_B_1649', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2768_1622, Cons(symdic.symdic_kl_x45x45x62, Cons(KL_CTX.KL_LOC_B_1649, nil)), KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1650', [setattr(KL_CTX, 'KL_LOC_Z_1651', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [setattr(KL_CTX, 'KL_LOC_Xx38x38_1652', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1505, KL_ARG_V2880_1503, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Xx38x38_1652, tco_apply(shen_placeholder, []), KL_ARG_V2880_1503, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Z_1651, tco_apply(shen_ebr, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Xx38x38_1652, KL_ARG_V2880_1503]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1616, KL_ARG_V2880_1503]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1618, KL_ARG_V2880_1503])]), KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Z_1651, KL_CTX.KL_LOC_B_1649, Cons(Cons(KL_CTX.KL_LOC_Xx38x38_1652, Cons(symdic.symdic_kl_x58, Cons(KL_CTX.KL_LOC_A_1621, nil))), KL_ARG_V2879_1502), KL_ARG_V2880_1503, KL_ARG_V2881_1504]))]))]))])][(-1)]][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2768_1622, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1650][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2768_1622]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2767_1620) else ([setattr(KL_CTX, 'KL_LOC_A_1653', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [setattr(KL_CTX, 'KL_LOC_B_1654', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2767_1620, Cons(KL_CTX.KL_LOC_A_1653, Cons(symdic.symdic_kl_x45x45x62, Cons(KL_CTX.KL_LOC_B_1654, nil))), KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1655', [setattr(KL_CTX, 'KL_LOC_Z_1656', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [setattr(KL_CTX, 'KL_LOC_Xx38x38_1657', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1505, KL_ARG_V2880_1503, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Xx38x38_1657, tco_apply(shen_placeholder, []), KL_ARG_V2880_1503, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Z_1656, tco_apply(shen_ebr, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Xx38x38_1657, KL_ARG_V2880_1503]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1616, KL_ARG_V2880_1503]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1618, KL_ARG_V2880_1503])]), KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Z_1656, KL_CTX.KL_LOC_B_1654, Cons(Cons(KL_CTX.KL_LOC_Xx38x38_1657, Cons(symdic.symdic_kl_x58, Cons(KL_CTX.KL_LOC_A_1653, nil))), KL_ARG_V2879_1502), KL_ARG_V2880_1503, KL_ARG_V2881_1504]))]))]))])][(-1)]][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2767_1620, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1655][(-1)]][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2767_1620]) else False))][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2766_1619) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2765_1617) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2764_1615) else False)][(-1)] if shen_eq(symdic.symdic_kl_lambda, KL_CTX.KL_LOC_V2763_1614) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2762_1613) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1658', [setattr(KL_CTX, 'KL_LOC_V2774_1659', tco_apply(shen_lazyderef, [KL_ARG_V2877_1500, KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2775_1660', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2774_1659), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2776_1661', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2774_1659), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_X_1662', car(KL_CTX.KL_LOC_V2776_1661)), [setattr(KL_CTX, 'KL_LOC_V2777_1663', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2776_1661), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_Y_1664', car(KL_CTX.KL_LOC_V2777_1663)), [setattr(KL_CTX, 'KL_LOC_V2778_1665', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2777_1663), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_Z_1666', car(KL_CTX.KL_LOC_V2778_1665)), [setattr(KL_CTX, 'KL_LOC_V2779_1667', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2778_1665), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_W_1668', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [setattr(KL_CTX, 'KL_LOC_Xx38x38_1669', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [setattr(KL_CTX, 'KL_LOC_B_1670', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1505, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1664, KL_CTX.KL_LOC_B_1670, KL_ARG_V2879_1502, KL_ARG_V2880_1503, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Xx38x38_1669, tco_apply(shen_placeholder, []), KL_ARG_V2880_1503, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_W_1668, tco_apply(shen_ebr, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Xx38x38_1669, KL_ARG_V2880_1503]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1662, KL_ARG_V2880_1503]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Z_1666, KL_ARG_V2880_1503])]), KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_W_1668, KL_ARG_V2878_1501, Cons(Cons(KL_CTX.KL_LOC_Xx38x38_1669, Cons(symdic.symdic_kl_x58, Cons(KL_CTX.KL_LOC_B_1670, nil))), KL_ARG_V2879_1502), KL_ARG_V2880_1503, KL_ARG_V2881_1504]))]))]))]))])][(-1)]][(-1)]][(-1)]][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2779_1667) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2778_1665) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2777_1663) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2776_1661) else False)][(-1)] if shen_eq(symdic.symdic_kl_let, KL_CTX.KL_LOC_V2775_1660) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2774_1659) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1671', [setattr(KL_CTX, 'KL_LOC_V2780_1672', tco_apply(shen_lazyderef, [KL_ARG_V2877_1500, KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2781_1673', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2780_1672), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2782_1674', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2780_1672), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2783_1675', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2782_1674), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2784_1676', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2782_1674), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_FileName_1677', car(KL_CTX.KL_LOC_V2784_1676)), [setattr(KL_CTX, 'KL_LOC_V2785_1678', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2784_1676), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_Direction2713_1679', car(KL_CTX.KL_LOC_V2785_1678)), [setattr(KL_CTX, 'KL_LOC_V2786_1680', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2785_1678), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2787_1681', tco_apply(shen_lazyderef, [KL_ARG_V2878_1501, KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2788_1682', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2787_1681), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2789_1683', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2787_1681), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_Direction_1684', car(KL_CTX.KL_LOC_V2789_1683)), [setattr(KL_CTX, 'KL_LOC_V2790_1685', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2789_1683), KL_ARG_V2880_1503])), ([tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_Direction_1684, KL_CTX.KL_LOC_Direction2713_1679, KL_ARG_V2880_1503, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1505, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_FileName_1677, symdic.symdic_kl_string, KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))]))])][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2790_1685) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2790_1685, nil, KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1686', [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_Direction_1684, KL_CTX.KL_LOC_Direction2713_1679, KL_ARG_V2880_1503, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1505, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_FileName_1677, symdic.symdic_kl_string, KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2790_1685, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1686][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2790_1685]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2789_1683) else ([setattr(KL_CTX, 'KL_LOC_Direction_1687', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2789_1683, Cons(KL_CTX.KL_LOC_Direction_1687, nil), KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1688', [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_Direction_1687, KL_CTX.KL_LOC_Direction2713_1679, KL_ARG_V2880_1503, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1505, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_FileName_1677, symdic.symdic_kl_string, KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2789_1683, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1688][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2789_1683]) else False))][(-1)] if shen_eq(symdic.symdic_kl_stream, KL_CTX.KL_LOC_V2788_1682) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2788_1682, symdic.symdic_kl_stream, KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1689', [setattr(KL_CTX, 'KL_LOC_V2791_1690', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2787_1681), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_Direction_1691', car(KL_CTX.KL_LOC_V2791_1690)), [setattr(KL_CTX, 'KL_LOC_V2792_1692', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2791_1690), KL_ARG_V2880_1503])), ([tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_Direction_1691, KL_CTX.KL_LOC_Direction2713_1679, KL_ARG_V2880_1503, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1505, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_FileName_1677, symdic.symdic_kl_string, KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))]))])][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2792_1692) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2792_1692, nil, KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1693', [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_Direction_1691, KL_CTX.KL_LOC_Direction2713_1679, KL_ARG_V2880_1503, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1505, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_FileName_1677, symdic.symdic_kl_string, KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2792_1692, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1693][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2792_1692]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2791_1690) else ([setattr(KL_CTX, 'KL_LOC_Direction_1694', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2791_1690, Cons(KL_CTX.KL_LOC_Direction_1694, nil), KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1695', [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_Direction_1694, KL_CTX.KL_LOC_Direction2713_1679, KL_ARG_V2880_1503, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1505, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_FileName_1677, symdic.symdic_kl_string, KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2791_1690, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1695][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2791_1690]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2788_1682, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1689][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2788_1682]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2787_1681) else ([setattr(KL_CTX, 'KL_LOC_Direction_1696', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2787_1681, Cons(symdic.symdic_kl_stream, Cons(KL_CTX.KL_LOC_Direction_1696, nil)), KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1697', [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_Direction_1696, KL_CTX.KL_LOC_Direction2713_1679, KL_ARG_V2880_1503, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1505, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_FileName_1677, symdic.symdic_kl_string, KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2787_1681, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1697][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2787_1681]) else False))][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2786_1680) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2785_1678) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2784_1676) else False)][(-1)] if shen_eq(symdic.symdic_kl_file, KL_CTX.KL_LOC_V2783_1675) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2782_1674) else False)][(-1)] if shen_eq(symdic.symdic_kl_open, KL_CTX.KL_LOC_V2781_1673) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2780_1672) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1698', [setattr(KL_CTX, 'KL_LOC_V2793_1699', tco_apply(shen_lazyderef, [KL_ARG_V2877_1500, KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2794_1700', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2793_1699), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2795_1701', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2793_1699), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_X_1702', car(KL_CTX.KL_LOC_V2795_1701)), [setattr(KL_CTX, 'KL_LOC_V2796_1703', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2795_1701), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_A_1704', car(KL_CTX.KL_LOC_V2796_1703)), [setattr(KL_CTX, 'KL_LOC_V2797_1705', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2796_1703), KL_ARG_V2880_1503])), ([tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1505, KL_ARG_V2880_1503, (lambda : tail_call(kl_unify, [KL_CTX.KL_LOC_A_1704, KL_ARG_V2878_1501, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_X_1702, KL_CTX.KL_LOC_A_1704, KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))]))])][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2797_1705) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2796_1703) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2795_1701) else False)][(-1)] if shen_eq(symdic.symdic_kl_type, KL_CTX.KL_LOC_V2794_1700) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2793_1699) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1706', [setattr(KL_CTX, 'KL_LOC_V2798_1707', tco_apply(shen_lazyderef, [KL_ARG_V2877_1500, KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2799_1708', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2798_1707), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2800_1709', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2798_1707), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2801_1710', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2800_1709), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2802_1711', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2800_1709), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_A_1712', car(KL_CTX.KL_LOC_V2802_1711)), [setattr(KL_CTX, 'KL_LOC_V2803_1713', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2802_1711), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_C_1714', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_CTX.KL_LOC_C_1714, tco_apply(shen_demodulate, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1712, KL_ARG_V2880_1503])]), KL_ARG_V2880_1503, (lambda : tail_call(kl_unify, [KL_ARG_V2878_1501, KL_CTX.KL_LOC_C_1714, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))])][(-1)]][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2803_1713) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2802_1711) else False)][(-1)] if shen_eq(symdic.symdic_kl_x58, KL_CTX.KL_LOC_V2801_1710) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2800_1709) else False)][(-1)] if shen_eq(symdic.symdic_kl_inputx43, KL_CTX.KL_LOC_V2799_1708) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2798_1707) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1715', [setattr(KL_CTX, 'KL_LOC_V2804_1716', tco_apply(shen_lazyderef, [KL_ARG_V2877_1500, KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2805_1717', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2804_1716), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2806_1718', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2804_1716), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2807_1719', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2806_1718), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2808_1720', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2806_1718), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_A_1721', car(KL_CTX.KL_LOC_V2808_1720)), [setattr(KL_CTX, 'KL_LOC_V2809_1722', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2808_1720), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_C_1723', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_CTX.KL_LOC_C_1723, tco_apply(shen_demodulate, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1721, KL_ARG_V2880_1503])]), KL_ARG_V2880_1503, (lambda : tail_call(kl_unify, [KL_ARG_V2878_1501, KL_CTX.KL_LOC_C_1723, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))])][(-1)]][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2809_1722) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2808_1720) else False)][(-1)] if shen_eq(symdic.symdic_kl_x58, KL_CTX.KL_LOC_V2807_1719) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2806_1718) else False)][(-1)] if shen_eq(symdic.symdic_readx43, KL_CTX.KL_LOC_V2805_1717) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2804_1716) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1724', [setattr(KL_CTX, 'KL_LOC_V2810_1725', tco_apply(shen_lazyderef, [KL_ARG_V2877_1500, KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2811_1726', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2810_1725), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2812_1727', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2810_1725), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_Var_1728', car(KL_CTX.KL_LOC_V2812_1727)), [setattr(KL_CTX, 'KL_LOC_V2813_1729', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2812_1727), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_Val_1730', car(KL_CTX.KL_LOC_V2813_1729)), [setattr(KL_CTX, 'KL_LOC_V2814_1731', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2813_1729), KL_ARG_V2880_1503])), ([tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1505, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Var_1728, symdic.symdic_kl_symbol, KL_ARG_V2879_1502, KL_ARG_V2880_1503, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1505, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [Cons(symdic.symdic_kl_value, Cons(KL_CTX.KL_LOC_Var_1728, nil)), KL_ARG_V2878_1501, KL_ARG_V2879_1502, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Val_1730, KL_ARG_V2878_1501, KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))]))]))]))])][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2814_1731) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2813_1729) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2812_1727) else False)][(-1)] if shen_eq(symdic.symdic_kl_set, KL_CTX.KL_LOC_V2811_1726) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2810_1725) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1732', [setattr(KL_CTX, 'KL_LOC_V2815_1733', tco_apply(shen_lazyderef, [KL_ARG_V2877_1500, KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2816_1734', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2815_1733), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2817_1735', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2815_1733), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_F_1736', car(KL_CTX.KL_LOC_V2817_1735)), [setattr(KL_CTX, 'KL_LOC_V2818_1737', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2817_1735), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_A_1738', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [setattr(KL_CTX, 'KL_LOC_Fx38x38_1739', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [setattr(KL_CTX, 'KL_LOC_B_1740', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1505, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_F_1736, Cons(KL_CTX.KL_LOC_A_1738, Cons(symdic.symdic_kl_x61x61x62, Cons(KL_CTX.KL_LOC_B_1740, nil))), KL_ARG_V2879_1502, KL_ARG_V2880_1503, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1505, KL_ARG_V2880_1503, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Fx38x38_1739, tco_apply(kl_concat, [symdic.symdic_kl_x38x38, tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_F_1736, KL_ARG_V2880_1503])]), KL_ARG_V2880_1503, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1505, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Fx38x38_1739, KL_ARG_V2878_1501, Cons(Cons(KL_CTX.KL_LOC_Fx38x38_1739, Cons(symdic.symdic_kl_x58, Cons(KL_CTX.KL_LOC_B_1740, nil))), KL_ARG_V2879_1502), KL_ARG_V2880_1503, KL_ARG_V2881_1504]))]))]))]))]))])][(-1)]][(-1)]][(-1)]][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2818_1737) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2817_1735) else False)][(-1)] if shen_eq(symdic.symdic_shen_x60x45sem, KL_CTX.KL_LOC_V2816_1734) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2815_1733) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1741', [setattr(KL_CTX, 'KL_LOC_V2819_1742', tco_apply(shen_lazyderef, [KL_ARG_V2877_1500, KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2820_1743', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2819_1742), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2821_1744', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2819_1742), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2822_1745', tco_apply(shen_lazyderef, [KL_ARG_V2878_1501, KL_ARG_V2880_1503])), ([tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V2881_1504])][(-1)] if shen_eq(symdic.symdic_kl_symbol, KL_CTX.KL_LOC_V2822_1745) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2822_1745, symdic.symdic_kl_symbol, KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1746', [tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V2881_1504])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2822_1745, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1746][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2822_1745]) else False))][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2821_1744) else False)][(-1)] if shen_eq(symdic.symdic_kl_fail, KL_CTX.KL_LOC_V2820_1743) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2819_1742) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1747', [setattr(KL_CTX, 'KL_LOC_NewHyp_1748', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_incinfs, []), tco_apply(shen_tx42x45hyps, [KL_ARG_V2879_1502, KL_CTX.KL_LOC_NewHyp_1748, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_ARG_V2877_1500, KL_ARG_V2878_1501, KL_CTX.KL_LOC_NewHyp_1748, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))])][(-1)]][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1749', [setattr(KL_CTX, 'KL_LOC_V2823_1750', tco_apply(shen_lazyderef, [KL_ARG_V2877_1500, KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2824_1751', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2823_1750), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2825_1752', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2823_1750), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_F_1753', car(KL_CTX.KL_LOC_V2825_1752)), [setattr(KL_CTX, 'KL_LOC_X_1754', cdr(KL_CTX.KL_LOC_V2825_1752)), [tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1505, KL_ARG_V2880_1503, (lambda : tail_call(shen_tx42x45def, [Cons(symdic.symdic_kl_define, Cons(KL_CTX.KL_LOC_F_1753, KL_CTX.KL_LOC_X_1754)), KL_ARG_V2878_1501, KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))])][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2825_1752) else False)][(-1)] if shen_eq(symdic.symdic_kl_define, KL_CTX.KL_LOC_V2824_1751) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2823_1750) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1755', [setattr(KL_CTX, 'KL_LOC_V2826_1756', tco_apply(shen_lazyderef, [KL_ARG_V2877_1500, KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2827_1757', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2826_1756), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2828_1758', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2826_1756), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_F_1759', car(KL_CTX.KL_LOC_V2828_1758)), [setattr(KL_CTX, 'KL_LOC_X_1760', cdr(KL_CTX.KL_LOC_V2828_1758)), [tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1505, KL_ARG_V2880_1503, (lambda : tail_call(shen_tx42x45defcc, [Cons(symdic.symdic_kl_defcc, Cons(KL_CTX.KL_LOC_F_1759, KL_CTX.KL_LOC_X_1760)), KL_ARG_V2878_1501, KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))])][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2828_1758) else False)][(-1)] if shen_eq(symdic.symdic_kl_defcc, KL_CTX.KL_LOC_V2827_1757) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2826_1756) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1761', [setattr(KL_CTX, 'KL_LOC_V2829_1762', tco_apply(shen_lazyderef, [KL_ARG_V2877_1500, KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2830_1763', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2829_1762), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2831_1764', tco_apply(shen_lazyderef, [KL_ARG_V2878_1501, KL_ARG_V2880_1503])), ([tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V2881_1504])][(-1)] if shen_eq(symdic.symdic_kl_symbol, KL_CTX.KL_LOC_V2831_1764) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2831_1764, symdic.symdic_kl_symbol, KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1765', [tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V2881_1504])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2831_1764, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1765][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2831_1764]) else False))][(-1)] if shen_eq(symdic.symdic_shen_processx45datatype, KL_CTX.KL_LOC_V2830_1763) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2829_1762) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1766', [setattr(KL_CTX, 'KL_LOC_V2832_1767', tco_apply(shen_lazyderef, [KL_ARG_V2877_1500, KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2833_1768', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2832_1767), KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2834_1769', tco_apply(shen_lazyderef, [KL_ARG_V2878_1501, KL_ARG_V2880_1503])), ([tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V2881_1504])][(-1)] if shen_eq(symdic.symdic_kl_symbol, KL_CTX.KL_LOC_V2834_1769) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2834_1769, symdic.symdic_kl_symbol, KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1770', [tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V2881_1504])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2834_1769, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1770][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2834_1769]) else False))][(-1)] if shen_eq(symdic.symdic_shen_synonymsx45help, KL_CTX.KL_LOC_V2833_1768) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2832_1767) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Datatypes_1771', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_CTX.KL_LOC_Datatypes_1771, shen_get(symdic.symdic_shen_x42datatypesx42), KL_ARG_V2880_1503, (lambda : tail_call(shen_udefsx42, [Cons(KL_ARG_V2877_1500, Cons(symdic.symdic_kl_x58, Cons(KL_ARG_V2878_1501, nil))), KL_ARG_V2879_1502, KL_CTX.KL_LOC_Datatypes_1771, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))])][(-1)]][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1766, False) else KL_CTX.KL_LOC_Case_1766)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1761, False) else KL_CTX.KL_LOC_Case_1761)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1755, False) else KL_CTX.KL_LOC_Case_1755)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1749, False) else KL_CTX.KL_LOC_Case_1749)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1747, False) else KL_CTX.KL_LOC_Case_1747)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1741, False) else KL_CTX.KL_LOC_Case_1741)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1732, False) else KL_CTX.KL_LOC_Case_1732)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1724, False) else KL_CTX.KL_LOC_Case_1724)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1715, False) else KL_CTX.KL_LOC_Case_1715)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1706, False) else KL_CTX.KL_LOC_Case_1706)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1698, False) else KL_CTX.KL_LOC_Case_1698)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1671, False) else KL_CTX.KL_LOC_Case_1671)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1658, False) else KL_CTX.KL_LOC_Case_1658)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1612, False) else KL_CTX.KL_LOC_Case_1612)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1602, False) else KL_CTX.KL_LOC_Case_1602)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1577, False) else KL_CTX.KL_LOC_Case_1577)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1547, False) else KL_CTX.KL_LOC_Case_1547)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1522, False) else KL_CTX.KL_LOC_Case_1522)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1515, False) else KL_CTX.KL_LOC_Case_1515)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1511, False) else KL_CTX.KL_LOC_Case_1511)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1510, False) else KL_CTX.KL_LOC_Case_1510)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1509, False) else KL_CTX.KL_LOC_Case_1509)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1507, False) else KL_CTX.KL_LOC_Case_1507)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1506, False) else KL_CTX.KL_LOC_Case_1506)][(-1)]])][(-1)]
shen_add_fun('shen.th*', shen_thx42, 5)

@tail_recursion
def shen_tx42x45hyps(*FUN_ARGS):
    FUN_ARITY = 4
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_tx42x45hyps, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2882_1772 = FUN_ARGS[0]
    KL_ARG_V2883_1773 = FUN_ARGS[1]
    KL_ARG_V2884_1774 = FUN_ARGS[2]
    KL_ARG_V2885_1775 = FUN_ARGS[3]

    class KL_Context:
        KL_LOC_Case_1776 = None
        KL_LOC_V2628_1777 = None
        KL_LOC_V2629_1778 = None
        KL_LOC_V2630_1779 = None
        KL_LOC_V2631_1780 = None
        KL_LOC_V2632_1781 = None
        KL_LOC_X_1782 = None
        KL_LOC_V2633_1783 = None
        KL_LOC_Y_1784 = None
        KL_LOC_V2634_1785 = None
        KL_LOC_V2635_1786 = None
        KL_LOC_V2636_1787 = None
        KL_LOC_V2637_1788 = None
        KL_LOC_V2638_1789 = None
        KL_LOC_V2639_1790 = None
        KL_LOC_V2640_1791 = None
        KL_LOC_A_1792 = None
        KL_LOC_V2641_1793 = None
        KL_LOC_V2642_1794 = None
        KL_LOC_Hyp_1795 = None
        KL_LOC_Result_1796 = None
        KL_LOC_Hyp_1797 = None
        KL_LOC_Result_1798 = None
        KL_LOC_V2643_1799 = None
        KL_LOC_Hyp_1800 = None
        KL_LOC_Result_1801 = None
        KL_LOC_Hyp_1802 = None
        KL_LOC_A_1803 = None
        KL_LOC_Result_1804 = None
        KL_LOC_V2644_1805 = None
        KL_LOC_Hyp_1806 = None
        KL_LOC_Result_1807 = None
        KL_LOC_Hyp_1808 = None
        KL_LOC_Result_1809 = None
        KL_LOC_V2645_1810 = None
        KL_LOC_A_1811 = None
        KL_LOC_V2646_1812 = None
        KL_LOC_V2647_1813 = None
        KL_LOC_Hyp_1814 = None
        KL_LOC_Result_1815 = None
        KL_LOC_Hyp_1816 = None
        KL_LOC_Result_1817 = None
        KL_LOC_V2648_1818 = None
        KL_LOC_Hyp_1819 = None
        KL_LOC_Result_1820 = None
        KL_LOC_Hyp_1821 = None
        KL_LOC_A_1822 = None
        KL_LOC_Result_1823 = None
        KL_LOC_V2649_1824 = None
        KL_LOC_Hyp_1825 = None
        KL_LOC_Result_1826 = None
        KL_LOC_Hyp_1827 = None
        KL_LOC_A_1828 = None
        KL_LOC_Result_1829 = None
        KL_LOC_V2650_1830 = None
        KL_LOC_Hyp_1831 = None
        KL_LOC_Result_1832 = None
        KL_LOC_Hyp_1833 = None
        KL_LOC_Case_1834 = None
        KL_LOC_V2651_1835 = None
        KL_LOC_V2652_1836 = None
        KL_LOC_V2653_1837 = None
        KL_LOC_V2654_1838 = None
        KL_LOC_V2655_1839 = None
        KL_LOC_X_1840 = None
        KL_LOC_V2656_1841 = None
        KL_LOC_Y_1842 = None
        KL_LOC_V2657_1843 = None
        KL_LOC_V2658_1844 = None
        KL_LOC_V2659_1845 = None
        KL_LOC_V2660_1846 = None
        KL_LOC_V2661_1847 = None
        KL_LOC_A_1848 = None
        KL_LOC_V2662_1849 = None
        KL_LOC_V2663_1850 = None
        KL_LOC_V2664_1851 = None
        KL_LOC_B_1852 = None
        KL_LOC_V2665_1853 = None
        KL_LOC_V2666_1854 = None
        KL_LOC_Hyp_1855 = None
        KL_LOC_Result_1856 = None
        KL_LOC_Hyp_1857 = None
        KL_LOC_Result_1858 = None
        KL_LOC_V2667_1859 = None
        KL_LOC_Hyp_1860 = None
        KL_LOC_Result_1861 = None
        KL_LOC_Hyp_1862 = None
        KL_LOC_B_1863 = None
        KL_LOC_Result_1864 = None
        KL_LOC_V2668_1865 = None
        KL_LOC_Hyp_1866 = None
        KL_LOC_Result_1867 = None
        KL_LOC_Hyp_1868 = None
        KL_LOC_Result_1869 = None
        KL_LOC_V2669_1870 = None
        KL_LOC_B_1871 = None
        KL_LOC_V2670_1872 = None
        KL_LOC_V2671_1873 = None
        KL_LOC_Hyp_1874 = None
        KL_LOC_Result_1875 = None
        KL_LOC_Hyp_1876 = None
        KL_LOC_Result_1877 = None
        KL_LOC_V2672_1878 = None
        KL_LOC_Hyp_1879 = None
        KL_LOC_Result_1880 = None
        KL_LOC_Hyp_1881 = None
        KL_LOC_B_1882 = None
        KL_LOC_Result_1883 = None
        KL_LOC_V2673_1884 = None
        KL_LOC_Hyp_1885 = None
        KL_LOC_Result_1886 = None
        KL_LOC_Hyp_1887 = None
        KL_LOC_B_1888 = None
        KL_LOC_Result_1889 = None
        KL_LOC_V2674_1890 = None
        KL_LOC_Hyp_1891 = None
        KL_LOC_Result_1892 = None
        KL_LOC_Hyp_1893 = None
        KL_LOC_A_1894 = None
        KL_LOC_B_1895 = None
        KL_LOC_Result_1896 = None
        KL_LOC_V2675_1897 = None
        KL_LOC_Hyp_1898 = None
        KL_LOC_Result_1899 = None
        KL_LOC_Hyp_1900 = None
        KL_LOC_Case_1901 = None
        KL_LOC_V2676_1902 = None
        KL_LOC_V2677_1903 = None
        KL_LOC_V2678_1904 = None
        KL_LOC_V2679_1905 = None
        KL_LOC_V2680_1906 = None
        KL_LOC_X_1907 = None
        KL_LOC_V2681_1908 = None
        KL_LOC_Y_1909 = None
        KL_LOC_V2682_1910 = None
        KL_LOC_V2683_1911 = None
        KL_LOC_V2684_1912 = None
        KL_LOC_V2685_1913 = None
        KL_LOC_V2686_1914 = None
        KL_LOC_V2687_1915 = None
        KL_LOC_V2688_1916 = None
        KL_LOC_A_1917 = None
        KL_LOC_V2689_1918 = None
        KL_LOC_V2690_1919 = None
        KL_LOC_Hyp_1920 = None
        KL_LOC_Result_1921 = None
        KL_LOC_Hyp_1922 = None
        KL_LOC_Result_1923 = None
        KL_LOC_V2691_1924 = None
        KL_LOC_Hyp_1925 = None
        KL_LOC_Result_1926 = None
        KL_LOC_Hyp_1927 = None
        KL_LOC_A_1928 = None
        KL_LOC_Result_1929 = None
        KL_LOC_V2692_1930 = None
        KL_LOC_Hyp_1931 = None
        KL_LOC_Result_1932 = None
        KL_LOC_Hyp_1933 = None
        KL_LOC_Result_1934 = None
        KL_LOC_V2693_1935 = None
        KL_LOC_A_1936 = None
        KL_LOC_V2694_1937 = None
        KL_LOC_V2695_1938 = None
        KL_LOC_Hyp_1939 = None
        KL_LOC_Result_1940 = None
        KL_LOC_Hyp_1941 = None
        KL_LOC_Result_1942 = None
        KL_LOC_V2696_1943 = None
        KL_LOC_Hyp_1944 = None
        KL_LOC_Result_1945 = None
        KL_LOC_Hyp_1946 = None
        KL_LOC_A_1947 = None
        KL_LOC_Result_1948 = None
        KL_LOC_V2697_1949 = None
        KL_LOC_Hyp_1950 = None
        KL_LOC_Result_1951 = None
        KL_LOC_Hyp_1952 = None
        KL_LOC_A_1953 = None
        KL_LOC_Result_1954 = None
        KL_LOC_V2698_1955 = None
        KL_LOC_Hyp_1956 = None
        KL_LOC_Result_1957 = None
        KL_LOC_Hyp_1958 = None
        KL_LOC_Case_1959 = None
        KL_LOC_V2699_1960 = None
        KL_LOC_V2700_1961 = None
        KL_LOC_V2701_1962 = None
        KL_LOC_V2702_1963 = None
        KL_LOC_V2703_1964 = None
        KL_LOC_X_1965 = None
        KL_LOC_V2704_1966 = None
        KL_LOC_Y_1967 = None
        KL_LOC_V2705_1968 = None
        KL_LOC_V2706_1969 = None
        KL_LOC_V2707_1970 = None
        KL_LOC_V2708_1971 = None
        KL_LOC_V2709_1972 = None
        KL_LOC_V2710_1973 = None
        KL_LOC_Hyp_1974 = None
        KL_LOC_Result_1975 = None
        KL_LOC_Hyp_1976 = None
        KL_LOC_Result_1977 = None
        KL_LOC_V2711_1978 = None
        KL_LOC_Hyp_1979 = None
        KL_LOC_Result_1980 = None
        KL_LOC_Hyp_1981 = None
        KL_LOC_V2712_1982 = None
        KL_LOC_X_1983 = None
        KL_LOC_Hyp_1984 = None
        KL_LOC_NewHyps_1985 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Case_1776', [setattr(KL_CTX, 'KL_LOC_V2628_1777', tco_apply(shen_lazyderef, [KL_ARG_V2882_1772, KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2629_1778', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2628_1777), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2630_1779', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2629_1778), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2631_1780', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2630_1779), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2632_1781', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2630_1779), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_X_1782', car(KL_CTX.KL_LOC_V2632_1781)), [setattr(KL_CTX, 'KL_LOC_V2633_1783', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2632_1781), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_Y_1784', car(KL_CTX.KL_LOC_V2633_1783)), [setattr(KL_CTX, 'KL_LOC_V2634_1785', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2633_1783), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2635_1786', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2629_1778), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2636_1787', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2635_1786), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2637_1788', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2635_1786), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2638_1789', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2637_1788), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2639_1790', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2638_1789), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2640_1791', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2638_1789), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_A_1792', car(KL_CTX.KL_LOC_V2640_1791)), [setattr(KL_CTX, 'KL_LOC_V2641_1793', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2640_1791), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2642_1794', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2637_1788), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1795', cdr(KL_CTX.KL_LOC_V2628_1777)), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1782, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1792, KL_ARG_V2884_1774]), nil))), Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1784, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(Cons(symdic.symdic_kl_list, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1792, KL_ARG_V2884_1774]), nil)), nil))), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1795, KL_ARG_V2884_1774]))), KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2642_1794) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2642_1794, nil, KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1796', [setattr(KL_CTX, 'KL_LOC_Hyp_1797', cdr(KL_CTX.KL_LOC_V2628_1777)), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1782, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1792, KL_ARG_V2884_1774]), nil))), Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1784, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(Cons(symdic.symdic_kl_list, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1792, KL_ARG_V2884_1774]), nil)), nil))), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1797, KL_ARG_V2884_1774]))), KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2642_1794, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1796][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2642_1794]) else False))][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2641_1793) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2641_1793, nil, KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1798', [setattr(KL_CTX, 'KL_LOC_V2643_1799', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2637_1788), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1800', cdr(KL_CTX.KL_LOC_V2628_1777)), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1782, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1792, KL_ARG_V2884_1774]), nil))), Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1784, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(Cons(symdic.symdic_kl_list, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1792, KL_ARG_V2884_1774]), nil)), nil))), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1800, KL_ARG_V2884_1774]))), KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2643_1799) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2643_1799, nil, KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1801', [setattr(KL_CTX, 'KL_LOC_Hyp_1802', cdr(KL_CTX.KL_LOC_V2628_1777)), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1782, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1792, KL_ARG_V2884_1774]), nil))), Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1784, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(Cons(symdic.symdic_kl_list, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1792, KL_ARG_V2884_1774]), nil)), nil))), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1802, KL_ARG_V2884_1774]))), KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2643_1799, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1801][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2643_1799]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2641_1793, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1798][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2641_1793]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2640_1791) else ([setattr(KL_CTX, 'KL_LOC_A_1803', tco_apply(shen_newpv, [KL_ARG_V2884_1774])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2640_1791, Cons(KL_CTX.KL_LOC_A_1803, nil), KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1804', [setattr(KL_CTX, 'KL_LOC_V2644_1805', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2637_1788), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1806', cdr(KL_CTX.KL_LOC_V2628_1777)), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1782, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1803, KL_ARG_V2884_1774]), nil))), Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1784, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(Cons(symdic.symdic_kl_list, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1803, KL_ARG_V2884_1774]), nil)), nil))), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1806, KL_ARG_V2884_1774]))), KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2644_1805) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2644_1805, nil, KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1807', [setattr(KL_CTX, 'KL_LOC_Hyp_1808', cdr(KL_CTX.KL_LOC_V2628_1777)), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1782, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1803, KL_ARG_V2884_1774]), nil))), Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1784, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(Cons(symdic.symdic_kl_list, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1803, KL_ARG_V2884_1774]), nil)), nil))), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1808, KL_ARG_V2884_1774]))), KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2644_1805, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1807][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2644_1805]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2640_1791, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1804][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2640_1791]) else False))][(-1)] if shen_eq(symdic.symdic_kl_list, KL_CTX.KL_LOC_V2639_1790) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2639_1790, symdic.symdic_kl_list, KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1809', [setattr(KL_CTX, 'KL_LOC_V2645_1810', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2638_1789), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_A_1811', car(KL_CTX.KL_LOC_V2645_1810)), [setattr(KL_CTX, 'KL_LOC_V2646_1812', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2645_1810), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2647_1813', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2637_1788), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1814', cdr(KL_CTX.KL_LOC_V2628_1777)), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1782, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1811, KL_ARG_V2884_1774]), nil))), Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1784, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(Cons(symdic.symdic_kl_list, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1811, KL_ARG_V2884_1774]), nil)), nil))), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1814, KL_ARG_V2884_1774]))), KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2647_1813) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2647_1813, nil, KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1815', [setattr(KL_CTX, 'KL_LOC_Hyp_1816', cdr(KL_CTX.KL_LOC_V2628_1777)), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1782, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1811, KL_ARG_V2884_1774]), nil))), Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1784, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(Cons(symdic.symdic_kl_list, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1811, KL_ARG_V2884_1774]), nil)), nil))), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1816, KL_ARG_V2884_1774]))), KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2647_1813, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1815][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2647_1813]) else False))][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2646_1812) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2646_1812, nil, KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1817', [setattr(KL_CTX, 'KL_LOC_V2648_1818', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2637_1788), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1819', cdr(KL_CTX.KL_LOC_V2628_1777)), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1782, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1811, KL_ARG_V2884_1774]), nil))), Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1784, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(Cons(symdic.symdic_kl_list, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1811, KL_ARG_V2884_1774]), nil)), nil))), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1819, KL_ARG_V2884_1774]))), KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2648_1818) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2648_1818, nil, KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1820', [setattr(KL_CTX, 'KL_LOC_Hyp_1821', cdr(KL_CTX.KL_LOC_V2628_1777)), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1782, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1811, KL_ARG_V2884_1774]), nil))), Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1784, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(Cons(symdic.symdic_kl_list, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1811, KL_ARG_V2884_1774]), nil)), nil))), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1821, KL_ARG_V2884_1774]))), KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2648_1818, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1820][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2648_1818]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2646_1812, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1817][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2646_1812]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2645_1810) else ([setattr(KL_CTX, 'KL_LOC_A_1822', tco_apply(shen_newpv, [KL_ARG_V2884_1774])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2645_1810, Cons(KL_CTX.KL_LOC_A_1822, nil), KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1823', [setattr(KL_CTX, 'KL_LOC_V2649_1824', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2637_1788), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1825', cdr(KL_CTX.KL_LOC_V2628_1777)), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1782, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1822, KL_ARG_V2884_1774]), nil))), Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1784, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(Cons(symdic.symdic_kl_list, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1822, KL_ARG_V2884_1774]), nil)), nil))), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1825, KL_ARG_V2884_1774]))), KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2649_1824) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2649_1824, nil, KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1826', [setattr(KL_CTX, 'KL_LOC_Hyp_1827', cdr(KL_CTX.KL_LOC_V2628_1777)), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1782, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1822, KL_ARG_V2884_1774]), nil))), Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1784, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(Cons(symdic.symdic_kl_list, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1822, KL_ARG_V2884_1774]), nil)), nil))), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1827, KL_ARG_V2884_1774]))), KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2649_1824, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1826][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2649_1824]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2645_1810, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1823][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2645_1810]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2639_1790, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1809][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2639_1790]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2638_1789) else ([setattr(KL_CTX, 'KL_LOC_A_1828', tco_apply(shen_newpv, [KL_ARG_V2884_1774])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2638_1789, Cons(symdic.symdic_kl_list, Cons(KL_CTX.KL_LOC_A_1828, nil)), KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1829', [setattr(KL_CTX, 'KL_LOC_V2650_1830', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2637_1788), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1831', cdr(KL_CTX.KL_LOC_V2628_1777)), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1782, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1828, KL_ARG_V2884_1774]), nil))), Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1784, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(Cons(symdic.symdic_kl_list, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1828, KL_ARG_V2884_1774]), nil)), nil))), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1831, KL_ARG_V2884_1774]))), KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2650_1830) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2650_1830, nil, KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1832', [setattr(KL_CTX, 'KL_LOC_Hyp_1833', cdr(KL_CTX.KL_LOC_V2628_1777)), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1782, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1828, KL_ARG_V2884_1774]), nil))), Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1784, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(Cons(symdic.symdic_kl_list, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1828, KL_ARG_V2884_1774]), nil)), nil))), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1833, KL_ARG_V2884_1774]))), KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2650_1830, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1832][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2650_1830]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2638_1789, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1829][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2638_1789]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2637_1788) else False)][(-1)] if shen_eq(symdic.symdic_kl_x58, KL_CTX.KL_LOC_V2636_1787) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2635_1786) else False)][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2634_1785) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2633_1783) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2632_1781) else False)][(-1)] if shen_eq(symdic.symdic_kl_cons, KL_CTX.KL_LOC_V2631_1780) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2630_1779) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2629_1778) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2628_1777) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1834', [setattr(KL_CTX, 'KL_LOC_V2651_1835', tco_apply(shen_lazyderef, [KL_ARG_V2882_1772, KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2652_1836', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2651_1835), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2653_1837', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2652_1836), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2654_1838', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2653_1837), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2655_1839', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2653_1837), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_X_1840', car(KL_CTX.KL_LOC_V2655_1839)), [setattr(KL_CTX, 'KL_LOC_V2656_1841', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2655_1839), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_Y_1842', car(KL_CTX.KL_LOC_V2656_1841)), [setattr(KL_CTX, 'KL_LOC_V2657_1843', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2656_1841), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2658_1844', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2652_1836), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2659_1845', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2658_1844), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2660_1846', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2658_1844), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2661_1847', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2660_1846), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_A_1848', car(KL_CTX.KL_LOC_V2661_1847)), [setattr(KL_CTX, 'KL_LOC_V2662_1849', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2661_1847), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2663_1850', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2662_1849), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2664_1851', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2662_1849), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_B_1852', car(KL_CTX.KL_LOC_V2664_1851)), [setattr(KL_CTX, 'KL_LOC_V2665_1853', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2664_1851), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2666_1854', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2660_1846), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1855', cdr(KL_CTX.KL_LOC_V2651_1835)), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1840, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1848, KL_ARG_V2884_1774]), nil))), Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1842, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_1852, KL_ARG_V2884_1774]), nil))), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1855, KL_ARG_V2884_1774]))), KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2666_1854) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2666_1854, nil, KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1856', [setattr(KL_CTX, 'KL_LOC_Hyp_1857', cdr(KL_CTX.KL_LOC_V2651_1835)), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1840, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1848, KL_ARG_V2884_1774]), nil))), Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1842, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_1852, KL_ARG_V2884_1774]), nil))), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1857, KL_ARG_V2884_1774]))), KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2666_1854, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1856][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2666_1854]) else False))][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2665_1853) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2665_1853, nil, KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1858', [setattr(KL_CTX, 'KL_LOC_V2667_1859', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2660_1846), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1860', cdr(KL_CTX.KL_LOC_V2651_1835)), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1840, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1848, KL_ARG_V2884_1774]), nil))), Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1842, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_1852, KL_ARG_V2884_1774]), nil))), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1860, KL_ARG_V2884_1774]))), KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2667_1859) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2667_1859, nil, KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1861', [setattr(KL_CTX, 'KL_LOC_Hyp_1862', cdr(KL_CTX.KL_LOC_V2651_1835)), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1840, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1848, KL_ARG_V2884_1774]), nil))), Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1842, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_1852, KL_ARG_V2884_1774]), nil))), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1862, KL_ARG_V2884_1774]))), KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2667_1859, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1861][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2667_1859]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2665_1853, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1858][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2665_1853]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2664_1851) else ([setattr(KL_CTX, 'KL_LOC_B_1863', tco_apply(shen_newpv, [KL_ARG_V2884_1774])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2664_1851, Cons(KL_CTX.KL_LOC_B_1863, nil), KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1864', [setattr(KL_CTX, 'KL_LOC_V2668_1865', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2660_1846), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1866', cdr(KL_CTX.KL_LOC_V2651_1835)), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1840, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1848, KL_ARG_V2884_1774]), nil))), Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1842, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_1863, KL_ARG_V2884_1774]), nil))), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1866, KL_ARG_V2884_1774]))), KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2668_1865) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2668_1865, nil, KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1867', [setattr(KL_CTX, 'KL_LOC_Hyp_1868', cdr(KL_CTX.KL_LOC_V2651_1835)), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1840, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1848, KL_ARG_V2884_1774]), nil))), Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1842, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_1863, KL_ARG_V2884_1774]), nil))), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1868, KL_ARG_V2884_1774]))), KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2668_1865, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1867][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2668_1865]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2664_1851, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1864][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2664_1851]) else False))][(-1)] if shen_eq(symdic.symdic_kl_x42, KL_CTX.KL_LOC_V2663_1850) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2663_1850, symdic.symdic_kl_x42, KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1869', [setattr(KL_CTX, 'KL_LOC_V2669_1870', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2662_1849), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_B_1871', car(KL_CTX.KL_LOC_V2669_1870)), [setattr(KL_CTX, 'KL_LOC_V2670_1872', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2669_1870), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2671_1873', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2660_1846), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1874', cdr(KL_CTX.KL_LOC_V2651_1835)), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1840, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1848, KL_ARG_V2884_1774]), nil))), Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1842, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_1871, KL_ARG_V2884_1774]), nil))), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1874, KL_ARG_V2884_1774]))), KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2671_1873) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2671_1873, nil, KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1875', [setattr(KL_CTX, 'KL_LOC_Hyp_1876', cdr(KL_CTX.KL_LOC_V2651_1835)), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1840, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1848, KL_ARG_V2884_1774]), nil))), Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1842, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_1871, KL_ARG_V2884_1774]), nil))), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1876, KL_ARG_V2884_1774]))), KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2671_1873, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1875][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2671_1873]) else False))][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2670_1872) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2670_1872, nil, KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1877', [setattr(KL_CTX, 'KL_LOC_V2672_1878', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2660_1846), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1879', cdr(KL_CTX.KL_LOC_V2651_1835)), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1840, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1848, KL_ARG_V2884_1774]), nil))), Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1842, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_1871, KL_ARG_V2884_1774]), nil))), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1879, KL_ARG_V2884_1774]))), KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2672_1878) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2672_1878, nil, KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1880', [setattr(KL_CTX, 'KL_LOC_Hyp_1881', cdr(KL_CTX.KL_LOC_V2651_1835)), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1840, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1848, KL_ARG_V2884_1774]), nil))), Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1842, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_1871, KL_ARG_V2884_1774]), nil))), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1881, KL_ARG_V2884_1774]))), KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2672_1878, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1880][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2672_1878]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2670_1872, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1877][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2670_1872]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2669_1870) else ([setattr(KL_CTX, 'KL_LOC_B_1882', tco_apply(shen_newpv, [KL_ARG_V2884_1774])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2669_1870, Cons(KL_CTX.KL_LOC_B_1882, nil), KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1883', [setattr(KL_CTX, 'KL_LOC_V2673_1884', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2660_1846), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1885', cdr(KL_CTX.KL_LOC_V2651_1835)), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1840, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1848, KL_ARG_V2884_1774]), nil))), Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1842, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_1882, KL_ARG_V2884_1774]), nil))), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1885, KL_ARG_V2884_1774]))), KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2673_1884) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2673_1884, nil, KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1886', [setattr(KL_CTX, 'KL_LOC_Hyp_1887', cdr(KL_CTX.KL_LOC_V2651_1835)), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1840, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1848, KL_ARG_V2884_1774]), nil))), Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1842, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_1882, KL_ARG_V2884_1774]), nil))), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1887, KL_ARG_V2884_1774]))), KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2673_1884, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1886][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2673_1884]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2669_1870, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1883][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2669_1870]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2663_1850, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1869][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2663_1850]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2662_1849) else ([setattr(KL_CTX, 'KL_LOC_B_1888', tco_apply(shen_newpv, [KL_ARG_V2884_1774])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2662_1849, Cons(symdic.symdic_kl_x42, Cons(KL_CTX.KL_LOC_B_1888, nil)), KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1889', [setattr(KL_CTX, 'KL_LOC_V2674_1890', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2660_1846), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1891', cdr(KL_CTX.KL_LOC_V2651_1835)), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1840, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1848, KL_ARG_V2884_1774]), nil))), Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1842, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_1888, KL_ARG_V2884_1774]), nil))), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1891, KL_ARG_V2884_1774]))), KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2674_1890) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2674_1890, nil, KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1892', [setattr(KL_CTX, 'KL_LOC_Hyp_1893', cdr(KL_CTX.KL_LOC_V2651_1835)), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1840, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1848, KL_ARG_V2884_1774]), nil))), Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1842, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_1888, KL_ARG_V2884_1774]), nil))), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1893, KL_ARG_V2884_1774]))), KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2674_1890, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1892][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2674_1890]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2662_1849, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1889][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2662_1849]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2661_1847) else ([setattr(KL_CTX, 'KL_LOC_A_1894', tco_apply(shen_newpv, [KL_ARG_V2884_1774])), [setattr(KL_CTX, 'KL_LOC_B_1895', tco_apply(shen_newpv, [KL_ARG_V2884_1774])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2661_1847, Cons(KL_CTX.KL_LOC_A_1894, Cons(symdic.symdic_kl_x42, Cons(KL_CTX.KL_LOC_B_1895, nil))), KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1896', [setattr(KL_CTX, 'KL_LOC_V2675_1897', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2660_1846), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1898', cdr(KL_CTX.KL_LOC_V2651_1835)), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1840, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1894, KL_ARG_V2884_1774]), nil))), Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1842, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_1895, KL_ARG_V2884_1774]), nil))), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1898, KL_ARG_V2884_1774]))), KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2675_1897) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2675_1897, nil, KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1899', [setattr(KL_CTX, 'KL_LOC_Hyp_1900', cdr(KL_CTX.KL_LOC_V2651_1835)), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1840, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1894, KL_ARG_V2884_1774]), nil))), Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1842, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_1895, KL_ARG_V2884_1774]), nil))), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1900, KL_ARG_V2884_1774]))), KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2675_1897, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1899][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2675_1897]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2661_1847, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1896][(-1)]][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2661_1847]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2660_1846) else False)][(-1)] if shen_eq(symdic.symdic_kl_x58, KL_CTX.KL_LOC_V2659_1845) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2658_1844) else False)][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2657_1843) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2656_1841) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2655_1839) else False)][(-1)] if shen_eq(symdic.symdic_kl_x64p, KL_CTX.KL_LOC_V2654_1838) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2653_1837) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2652_1836) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2651_1835) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1901', [setattr(KL_CTX, 'KL_LOC_V2676_1902', tco_apply(shen_lazyderef, [KL_ARG_V2882_1772, KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2677_1903', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2676_1902), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2678_1904', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2677_1903), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2679_1905', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2678_1904), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2680_1906', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2678_1904), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_X_1907', car(KL_CTX.KL_LOC_V2680_1906)), [setattr(KL_CTX, 'KL_LOC_V2681_1908', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2680_1906), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_Y_1909', car(KL_CTX.KL_LOC_V2681_1908)), [setattr(KL_CTX, 'KL_LOC_V2682_1910', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2681_1908), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2683_1911', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2677_1903), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2684_1912', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2683_1911), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2685_1913', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2683_1911), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2686_1914', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2685_1913), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2687_1915', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2686_1914), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2688_1916', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2686_1914), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_A_1917', car(KL_CTX.KL_LOC_V2688_1916)), [setattr(KL_CTX, 'KL_LOC_V2689_1918', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2688_1916), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2690_1919', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2685_1913), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1920', cdr(KL_CTX.KL_LOC_V2676_1902)), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1907, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1917, KL_ARG_V2884_1774]), nil))), Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1909, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(Cons(symdic.symdic_kl_vector, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1917, KL_ARG_V2884_1774]), nil)), nil))), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1920, KL_ARG_V2884_1774]))), KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2690_1919) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2690_1919, nil, KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1921', [setattr(KL_CTX, 'KL_LOC_Hyp_1922', cdr(KL_CTX.KL_LOC_V2676_1902)), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1907, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1917, KL_ARG_V2884_1774]), nil))), Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1909, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(Cons(symdic.symdic_kl_vector, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1917, KL_ARG_V2884_1774]), nil)), nil))), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1922, KL_ARG_V2884_1774]))), KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2690_1919, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1921][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2690_1919]) else False))][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2689_1918) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2689_1918, nil, KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1923', [setattr(KL_CTX, 'KL_LOC_V2691_1924', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2685_1913), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1925', cdr(KL_CTX.KL_LOC_V2676_1902)), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1907, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1917, KL_ARG_V2884_1774]), nil))), Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1909, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(Cons(symdic.symdic_kl_vector, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1917, KL_ARG_V2884_1774]), nil)), nil))), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1925, KL_ARG_V2884_1774]))), KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2691_1924) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2691_1924, nil, KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1926', [setattr(KL_CTX, 'KL_LOC_Hyp_1927', cdr(KL_CTX.KL_LOC_V2676_1902)), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1907, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1917, KL_ARG_V2884_1774]), nil))), Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1909, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(Cons(symdic.symdic_kl_vector, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1917, KL_ARG_V2884_1774]), nil)), nil))), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1927, KL_ARG_V2884_1774]))), KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2691_1924, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1926][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2691_1924]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2689_1918, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1923][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2689_1918]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2688_1916) else ([setattr(KL_CTX, 'KL_LOC_A_1928', tco_apply(shen_newpv, [KL_ARG_V2884_1774])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2688_1916, Cons(KL_CTX.KL_LOC_A_1928, nil), KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1929', [setattr(KL_CTX, 'KL_LOC_V2692_1930', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2685_1913), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1931', cdr(KL_CTX.KL_LOC_V2676_1902)), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1907, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1928, KL_ARG_V2884_1774]), nil))), Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1909, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(Cons(symdic.symdic_kl_vector, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1928, KL_ARG_V2884_1774]), nil)), nil))), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1931, KL_ARG_V2884_1774]))), KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2692_1930) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2692_1930, nil, KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1932', [setattr(KL_CTX, 'KL_LOC_Hyp_1933', cdr(KL_CTX.KL_LOC_V2676_1902)), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1907, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1928, KL_ARG_V2884_1774]), nil))), Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1909, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(Cons(symdic.symdic_kl_vector, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1928, KL_ARG_V2884_1774]), nil)), nil))), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1933, KL_ARG_V2884_1774]))), KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2692_1930, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1932][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2692_1930]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2688_1916, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1929][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2688_1916]) else False))][(-1)] if shen_eq(symdic.symdic_kl_vector, KL_CTX.KL_LOC_V2687_1915) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2687_1915, symdic.symdic_kl_vector, KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1934', [setattr(KL_CTX, 'KL_LOC_V2693_1935', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2686_1914), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_A_1936', car(KL_CTX.KL_LOC_V2693_1935)), [setattr(KL_CTX, 'KL_LOC_V2694_1937', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2693_1935), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2695_1938', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2685_1913), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1939', cdr(KL_CTX.KL_LOC_V2676_1902)), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1907, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1936, KL_ARG_V2884_1774]), nil))), Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1909, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(Cons(symdic.symdic_kl_vector, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1936, KL_ARG_V2884_1774]), nil)), nil))), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1939, KL_ARG_V2884_1774]))), KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2695_1938) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2695_1938, nil, KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1940', [setattr(KL_CTX, 'KL_LOC_Hyp_1941', cdr(KL_CTX.KL_LOC_V2676_1902)), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1907, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1936, KL_ARG_V2884_1774]), nil))), Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1909, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(Cons(symdic.symdic_kl_vector, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1936, KL_ARG_V2884_1774]), nil)), nil))), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1941, KL_ARG_V2884_1774]))), KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2695_1938, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1940][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2695_1938]) else False))][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2694_1937) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2694_1937, nil, KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1942', [setattr(KL_CTX, 'KL_LOC_V2696_1943', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2685_1913), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1944', cdr(KL_CTX.KL_LOC_V2676_1902)), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1907, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1936, KL_ARG_V2884_1774]), nil))), Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1909, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(Cons(symdic.symdic_kl_vector, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1936, KL_ARG_V2884_1774]), nil)), nil))), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1944, KL_ARG_V2884_1774]))), KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2696_1943) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2696_1943, nil, KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1945', [setattr(KL_CTX, 'KL_LOC_Hyp_1946', cdr(KL_CTX.KL_LOC_V2676_1902)), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1907, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1936, KL_ARG_V2884_1774]), nil))), Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1909, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(Cons(symdic.symdic_kl_vector, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1936, KL_ARG_V2884_1774]), nil)), nil))), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1946, KL_ARG_V2884_1774]))), KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2696_1943, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1945][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2696_1943]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2694_1937, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1942][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2694_1937]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2693_1935) else ([setattr(KL_CTX, 'KL_LOC_A_1947', tco_apply(shen_newpv, [KL_ARG_V2884_1774])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2693_1935, Cons(KL_CTX.KL_LOC_A_1947, nil), KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1948', [setattr(KL_CTX, 'KL_LOC_V2697_1949', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2685_1913), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1950', cdr(KL_CTX.KL_LOC_V2676_1902)), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1907, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1947, KL_ARG_V2884_1774]), nil))), Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1909, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(Cons(symdic.symdic_kl_vector, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1947, KL_ARG_V2884_1774]), nil)), nil))), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1950, KL_ARG_V2884_1774]))), KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2697_1949) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2697_1949, nil, KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1951', [setattr(KL_CTX, 'KL_LOC_Hyp_1952', cdr(KL_CTX.KL_LOC_V2676_1902)), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1907, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1947, KL_ARG_V2884_1774]), nil))), Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1909, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(Cons(symdic.symdic_kl_vector, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1947, KL_ARG_V2884_1774]), nil)), nil))), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1952, KL_ARG_V2884_1774]))), KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2697_1949, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1951][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2697_1949]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2693_1935, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1948][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2693_1935]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2687_1915, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1934][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2687_1915]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2686_1914) else ([setattr(KL_CTX, 'KL_LOC_A_1953', tco_apply(shen_newpv, [KL_ARG_V2884_1774])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2686_1914, Cons(symdic.symdic_kl_vector, Cons(KL_CTX.KL_LOC_A_1953, nil)), KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1954', [setattr(KL_CTX, 'KL_LOC_V2698_1955', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2685_1913), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1956', cdr(KL_CTX.KL_LOC_V2676_1902)), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1907, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1953, KL_ARG_V2884_1774]), nil))), Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1909, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(Cons(symdic.symdic_kl_vector, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1953, KL_ARG_V2884_1774]), nil)), nil))), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1956, KL_ARG_V2884_1774]))), KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2698_1955) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2698_1955, nil, KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1957', [setattr(KL_CTX, 'KL_LOC_Hyp_1958', cdr(KL_CTX.KL_LOC_V2676_1902)), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1907, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1953, KL_ARG_V2884_1774]), nil))), Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1909, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(Cons(symdic.symdic_kl_vector, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1953, KL_ARG_V2884_1774]), nil)), nil))), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1958, KL_ARG_V2884_1774]))), KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2698_1955, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1957][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2698_1955]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2686_1914, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1954][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2686_1914]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2685_1913) else False)][(-1)] if shen_eq(symdic.symdic_kl_x58, KL_CTX.KL_LOC_V2684_1912) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2683_1911) else False)][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2682_1910) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2681_1908) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2680_1906) else False)][(-1)] if shen_eq(symdic.symdic_kl_x64v, KL_CTX.KL_LOC_V2679_1905) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2678_1904) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2677_1903) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2676_1902) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1959', [setattr(KL_CTX, 'KL_LOC_V2699_1960', tco_apply(shen_lazyderef, [KL_ARG_V2882_1772, KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2700_1961', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2699_1960), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2701_1962', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2700_1961), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2702_1963', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2701_1962), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2703_1964', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2701_1962), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_X_1965', car(KL_CTX.KL_LOC_V2703_1964)), [setattr(KL_CTX, 'KL_LOC_V2704_1966', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2703_1964), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_Y_1967', car(KL_CTX.KL_LOC_V2704_1966)), [setattr(KL_CTX, 'KL_LOC_V2705_1968', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2704_1966), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2706_1969', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2700_1961), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2707_1970', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2706_1969), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2708_1971', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2706_1969), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2709_1972', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2708_1971), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2710_1973', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2708_1971), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1974', cdr(KL_CTX.KL_LOC_V2699_1960)), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1965, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(symdic.symdic_kl_string, nil))), Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1967, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(symdic.symdic_kl_string, nil))), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1974, KL_ARG_V2884_1774]))), KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2710_1973) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2710_1973, nil, KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1975', [setattr(KL_CTX, 'KL_LOC_Hyp_1976', cdr(KL_CTX.KL_LOC_V2699_1960)), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1965, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(symdic.symdic_kl_string, nil))), Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1967, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(symdic.symdic_kl_string, nil))), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1976, KL_ARG_V2884_1774]))), KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2710_1973, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1975][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2710_1973]) else False))][(-1)] if shen_eq(symdic.symdic_kl_string, KL_CTX.KL_LOC_V2709_1972) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2709_1972, symdic.symdic_kl_string, KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1977', [setattr(KL_CTX, 'KL_LOC_V2711_1978', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2708_1971), KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1979', cdr(KL_CTX.KL_LOC_V2699_1960)), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1965, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(symdic.symdic_kl_string, nil))), Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1967, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(symdic.symdic_kl_string, nil))), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1979, KL_ARG_V2884_1774]))), KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2711_1978) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2711_1978, nil, KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1980', [setattr(KL_CTX, 'KL_LOC_Hyp_1981', cdr(KL_CTX.KL_LOC_V2699_1960)), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1965, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(symdic.symdic_kl_string, nil))), Cons(Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1967, KL_ARG_V2884_1774]), Cons(symdic.symdic_kl_x58, Cons(symdic.symdic_kl_string, nil))), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1981, KL_ARG_V2884_1774]))), KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2711_1978, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1980][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2711_1978]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2709_1972, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1977][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2709_1972]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2708_1971) else False)][(-1)] if shen_eq(symdic.symdic_kl_x58, KL_CTX.KL_LOC_V2707_1970) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2706_1969) else False)][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2705_1968) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2704_1966) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2703_1964) else False)][(-1)] if shen_eq(symdic.symdic_kl_x64s, KL_CTX.KL_LOC_V2702_1963) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2701_1962) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2700_1961) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2699_1960) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_V2712_1982', tco_apply(shen_lazyderef, [KL_ARG_V2882_1772, KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_X_1983', car(KL_CTX.KL_LOC_V2712_1982)), [setattr(KL_CTX, 'KL_LOC_Hyp_1984', cdr(KL_CTX.KL_LOC_V2712_1982)), [setattr(KL_CTX, 'KL_LOC_NewHyps_1985', tco_apply(shen_newpv, [KL_ARG_V2884_1774])), [tco_apply(shen_incinfs, []), tail_call(kl_bind, [KL_ARG_V2883_1773, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1983, KL_ARG_V2884_1774]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_NewHyps_1985, KL_ARG_V2884_1774])), KL_ARG_V2884_1774, (lambda : tail_call(shen_tx42x45hyps, [KL_CTX.KL_LOC_Hyp_1984, KL_CTX.KL_LOC_NewHyps_1985, KL_ARG_V2884_1774, KL_ARG_V2885_1775]))])][(-1)]][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2712_1982) else False)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1959, False) else KL_CTX.KL_LOC_Case_1959)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1901, False) else KL_CTX.KL_LOC_Case_1901)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1834, False) else KL_CTX.KL_LOC_Case_1834)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1776, False) else KL_CTX.KL_LOC_Case_1776)][(-1)]
shen_add_fun('shen.t*-hyps', shen_tx42x45hyps, 4)

@tail_recursion
def shen_show(*FUN_ARGS):
    FUN_ARITY = 4
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_show, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2898_1986 = FUN_ARGS[0]
    KL_ARG_V2899_1987 = FUN_ARGS[1]
    KL_ARG_V2900_1988 = FUN_ARGS[2]
    KL_ARG_V2901_1989 = FUN_ARGS[3]
    global symdic
    return ([tco_apply(shen_line, []), [tco_apply(shen_showx45p, [tco_apply(shen_deref, [KL_ARG_V2898_1986, KL_ARG_V2900_1988])]), [tco_apply(kl_nl, [1]), [tco_apply(kl_nl, [1]), [tco_apply(shen_showx45assumptions, [tco_apply(shen_deref, [KL_ARG_V2899_1987, KL_ARG_V2900_1988]), 1]), [tco_apply(shen_prhush, ['\r\n> ', tco_apply(kl_stoutput, [])]), [tco_apply(shen_pausex45forx45user, [shen_get(symdic.symdic_kl_x42languagex42)]), tail_call(kl_thaw, [KL_ARG_V2901_1989])][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)] if shen_get(symdic.symdic_shen_x42spyx42) else (tail_call(kl_thaw, [KL_ARG_V2901_1989]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.show', shen_show, 4)

@tail_recursion
def shen_line(*FUN_ARGS):
    FUN_ARITY = 0
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_line, (FUN_ARGS + lambdaargs)))

    class KL_Context:
        KL_LOC_Infs_1990 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Infs_1990', tco_apply(kl_inferences, [])), tail_call(shen_prhush, [('____________________________________________________________ ' + tco_apply(shen_app, [KL_CTX.KL_LOC_Infs_1990, (' inference' + tco_apply(shen_app, [('' if shen_eq(1, KL_CTX.KL_LOC_Infs_1990) else 's'), ' \r\n?- ', symdic.symdic_shen_a])), symdic.symdic_shen_a])), tco_apply(kl_stoutput, [])])][(-1)]
shen_add_fun('shen.line', shen_line, 0)

@tail_recursion
def shen_showx45p(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_showx45p, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2902_1991 = FUN_ARGS[0]
    global symdic
    return (tail_call(shen_prhush, [tco_apply(shen_app, [car(KL_ARG_V2902_1991), (' : ' + tco_apply(shen_app, [car(cdr(cdr(KL_ARG_V2902_1991))), '', symdic.symdic_shen_r])), symdic.symdic_shen_r]), tco_apply(kl_stoutput, [])]) if ((((shen_eq(nil, cdr(cdr(cdr(KL_ARG_V2902_1991)))) if shen_consp(cdr(cdr(KL_ARG_V2902_1991))) else False) if shen_eq(symdic.symdic_kl_x58, car(cdr(KL_ARG_V2902_1991))) else False) if shen_consp(cdr(KL_ARG_V2902_1991)) else False) if shen_consp(KL_ARG_V2902_1991) else False) else (tail_call(shen_prhush, [tco_apply(shen_app, [KL_ARG_V2902_1991, '', symdic.symdic_shen_r]), tco_apply(kl_stoutput, [])]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.show-p', shen_showx45p, 1)

@tail_recursion
def shen_showx45assumptions(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_showx45assumptions, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2905_1992 = FUN_ARGS[0]
    KL_ARG_V2906_1993 = FUN_ARGS[1]
    global symdic
    return (symdic.symdic_shen_skip if shen_eq(nil, KL_ARG_V2905_1992) else ([tco_apply(shen_prhush, [tco_apply(shen_app, [KL_ARG_V2906_1993, '. ', symdic.symdic_shen_a]), tco_apply(kl_stoutput, [])]), [tco_apply(shen_showx45p, [car(KL_ARG_V2905_1992)]), [tco_apply(kl_nl, [1]), tail_call(shen_showx45assumptions, [cdr(KL_ARG_V2905_1992), (KL_ARG_V2906_1993 + 1)])][(-1)]][(-1)]][(-1)] if shen_consp(KL_ARG_V2905_1992) else (tail_call(shen_sysx45error, [symdic.symdic_shen_showx45assumptions]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.show-assumptions', shen_showx45assumptions, 2)

@tail_recursion
def shen_pausex45forx45user(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_pausex45forx45user, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2911_1994 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_I_1995 = None
        KL_LOC_I_1996 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_I_1995', tco_apply(FORMAT, [nil, '~C', tco_apply(READx45CHAR, [])])), (shen_simple_error('input aborted\r\n') if shen_eq(KL_CTX.KL_LOC_I_1995, 'a') else tail_call(kl_nl, [1]))][(-1)] if shen_eq('Common Lisp', KL_ARG_V2911_1994) else ([setattr(KL_CTX, 'KL_LOC_I_1996', tco_apply(shen_readx45char, [])), (shen_simple_error('input aborted\r\n') if shen_eq(KL_CTX.KL_LOC_I_1996, 'a') else tail_call(kl_nl, [1]))][(-1)] if True else shen_simple_error('condition failure')))
shen_add_fun('shen.pause-for-user', shen_pausex45forx45user, 1)

@tail_recursion
def shen_readx45char(*FUN_ARGS):
    FUN_ARITY = 0
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_readx45char, (FUN_ARGS + lambdaargs)))
    global symdic
    return tail_call(shen_readx45charx45h, [shen_read_byte(tco_apply(kl_stinput, [])), 0])
shen_add_fun('shen.read-char', shen_readx45char, 0)

@tail_recursion
def shen_readx45charx45h(*FUN_ARGS):
    FUN_ARITY = 2
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_readx45charx45h, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2914_1997 = FUN_ARGS[0]
    KL_ARG_V2915_1998 = FUN_ARGS[1]
    global symdic
    return (tail_call(shen_readx45charx45h, [shen_read_byte(tco_apply(kl_stinput, [])), 1]) if (shen_eq(0, KL_ARG_V2915_1998) if shen_eq((-1), KL_ARG_V2914_1997) else False) else (tail_call(shen_readx45charx45h, [shen_read_byte(tco_apply(kl_stinput, [])), 0]) if shen_eq(0, KL_ARG_V2915_1998) else (tail_call(shen_readx45charx45h, [shen_read_byte(tco_apply(kl_stinput, [])), 1]) if (shen_eq(1, KL_ARG_V2915_1998) if shen_eq((-1), KL_ARG_V2914_1997) else False) else (chr(KL_ARG_V2914_1997) if shen_eq(1, KL_ARG_V2915_1998) else (tail_call(shen_sysx45error, [symdic.symdic_shen_readx45charx45h]) if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.read-char-h', shen_readx45charx45h, 2)

@tail_recursion
def shen_typedfx63(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_typedfx63, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2916_1999 = FUN_ARGS[0]
    global symdic
    return shen_consp(tco_apply(kl_assoc, [KL_ARG_V2916_1999, shen_get(symdic.symdic_shen_x42signedfuncsx42)]))
shen_add_fun('shen.typedf?', shen_typedfx63, 1)

@tail_recursion
def shen_sigf(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_sigf, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2917_2000 = FUN_ARGS[0]
    global symdic
    return tail_call(kl_concat, [symdic.symdic_shen_typex45signaturex45ofx45, KL_ARG_V2917_2000])
shen_add_fun('shen.sigf', shen_sigf, 1)

@tail_recursion
def shen_placeholder(*FUN_ARGS):
    FUN_ARITY = 0
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_placeholder, (FUN_ARGS + lambdaargs)))
    global symdic
    return tail_call(kl_gensym, [symdic.symdic_kl_x38x38])
shen_add_fun('shen.placeholder', shen_placeholder, 0)

@tail_recursion
def shen_base(*FUN_ARGS):
    FUN_ARITY = 4
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_base, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2918_2001 = FUN_ARGS[0]
    KL_ARG_V2919_2002 = FUN_ARGS[1]
    KL_ARG_V2920_2003 = FUN_ARGS[2]
    KL_ARG_V2921_2004 = FUN_ARGS[3]

    class KL_Context:
        KL_LOC_Case_2005 = None
        KL_LOC_V2615_2006 = None
        KL_LOC_Result_2007 = None
        KL_LOC_Case_2008 = None
        KL_LOC_V2616_2009 = None
        KL_LOC_Result_2010 = None
        KL_LOC_Case_2011 = None
        KL_LOC_V2617_2012 = None
        KL_LOC_Result_2013 = None
        KL_LOC_Case_2014 = None
        KL_LOC_V2618_2015 = None
        KL_LOC_Result_2016 = None
        KL_LOC_V2619_2017 = None
        KL_LOC_V2620_2018 = None
        KL_LOC_V2621_2019 = None
        KL_LOC_V2622_2020 = None
        KL_LOC_A_2021 = None
        KL_LOC_V2623_2022 = None
        KL_LOC_Result_2023 = None
        KL_LOC_A_2024 = None
        KL_LOC_Result_2025 = None
        KL_LOC_Result_2026 = None
        KL_LOC_V2624_2027 = None
        KL_LOC_A_2028 = None
        KL_LOC_V2625_2029 = None
        KL_LOC_Result_2030 = None
        KL_LOC_A_2031 = None
        KL_LOC_Result_2032 = None
        KL_LOC_A_2033 = None
        KL_LOC_Result_2034 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Case_2005', [setattr(KL_CTX, 'KL_LOC_V2615_2006', tco_apply(shen_lazyderef, [KL_ARG_V2919_2002, KL_ARG_V2920_2003])), ([tco_apply(shen_incinfs, []), tco_apply(kl_fwhen, [isinstance(tco_apply(shen_lazyderef, [KL_ARG_V2918_2001, KL_ARG_V2920_2003]), numbers.Number), KL_ARG_V2920_2003, KL_ARG_V2921_2004])][(-1)] if shen_eq(symdic.symdic_kl_number, KL_CTX.KL_LOC_V2615_2006) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2615_2006, symdic.symdic_kl_number, KL_ARG_V2920_2003]), [setattr(KL_CTX, 'KL_LOC_Result_2007', [tco_apply(shen_incinfs, []), tco_apply(kl_fwhen, [isinstance(tco_apply(shen_lazyderef, [KL_ARG_V2918_2001, KL_ARG_V2920_2003]), numbers.Number), KL_ARG_V2920_2003, KL_ARG_V2921_2004])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2615_2006, KL_ARG_V2920_2003]), KL_CTX.KL_LOC_Result_2007][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2615_2006]) else False))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_2008', [setattr(KL_CTX, 'KL_LOC_V2616_2009', tco_apply(shen_lazyderef, [KL_ARG_V2919_2002, KL_ARG_V2920_2003])), ([tco_apply(shen_incinfs, []), tco_apply(kl_fwhen, [tco_apply(kl_booleanx63, [tco_apply(shen_lazyderef, [KL_ARG_V2918_2001, KL_ARG_V2920_2003])]), KL_ARG_V2920_2003, KL_ARG_V2921_2004])][(-1)] if shen_eq(symdic.symdic_kl_boolean, KL_CTX.KL_LOC_V2616_2009) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2616_2009, symdic.symdic_kl_boolean, KL_ARG_V2920_2003]), [setattr(KL_CTX, 'KL_LOC_Result_2010', [tco_apply(shen_incinfs, []), tco_apply(kl_fwhen, [tco_apply(kl_booleanx63, [tco_apply(shen_lazyderef, [KL_ARG_V2918_2001, KL_ARG_V2920_2003])]), KL_ARG_V2920_2003, KL_ARG_V2921_2004])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2616_2009, KL_ARG_V2920_2003]), KL_CTX.KL_LOC_Result_2010][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2616_2009]) else False))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_2011', [setattr(KL_CTX, 'KL_LOC_V2617_2012', tco_apply(shen_lazyderef, [KL_ARG_V2919_2002, KL_ARG_V2920_2003])), ([tco_apply(shen_incinfs, []), tco_apply(kl_fwhen, [isinstance(tco_apply(shen_lazyderef, [KL_ARG_V2918_2001, KL_ARG_V2920_2003]), str), KL_ARG_V2920_2003, KL_ARG_V2921_2004])][(-1)] if shen_eq(symdic.symdic_kl_string, KL_CTX.KL_LOC_V2617_2012) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2617_2012, symdic.symdic_kl_string, KL_ARG_V2920_2003]), [setattr(KL_CTX, 'KL_LOC_Result_2013', [tco_apply(shen_incinfs, []), tco_apply(kl_fwhen, [isinstance(tco_apply(shen_lazyderef, [KL_ARG_V2918_2001, KL_ARG_V2920_2003]), str), KL_ARG_V2920_2003, KL_ARG_V2921_2004])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2617_2012, KL_ARG_V2920_2003]), KL_CTX.KL_LOC_Result_2013][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2617_2012]) else False))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_2014', [setattr(KL_CTX, 'KL_LOC_V2618_2015', tco_apply(shen_lazyderef, [KL_ARG_V2919_2002, KL_ARG_V2920_2003])), ([tco_apply(shen_incinfs, []), tco_apply(kl_fwhen, [tco_apply(kl_symbolx63, [tco_apply(shen_lazyderef, [KL_ARG_V2918_2001, KL_ARG_V2920_2003])]), KL_ARG_V2920_2003, (lambda : tail_call(kl_fwhen, [(not tco_apply(shen_uex63, [tco_apply(shen_lazyderef, [KL_ARG_V2918_2001, KL_ARG_V2920_2003])])), KL_ARG_V2920_2003, KL_ARG_V2921_2004]))])][(-1)] if shen_eq(symdic.symdic_kl_symbol, KL_CTX.KL_LOC_V2618_2015) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2618_2015, symdic.symdic_kl_symbol, KL_ARG_V2920_2003]), [setattr(KL_CTX, 'KL_LOC_Result_2016', [tco_apply(shen_incinfs, []), tco_apply(kl_fwhen, [tco_apply(kl_symbolx63, [tco_apply(shen_lazyderef, [KL_ARG_V2918_2001, KL_ARG_V2920_2003])]), KL_ARG_V2920_2003, (lambda : tail_call(kl_fwhen, [(not tco_apply(shen_uex63, [tco_apply(shen_lazyderef, [KL_ARG_V2918_2001, KL_ARG_V2920_2003])])), KL_ARG_V2920_2003, KL_ARG_V2921_2004]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2618_2015, KL_ARG_V2920_2003]), KL_CTX.KL_LOC_Result_2016][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2618_2015]) else False))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_V2619_2017', tco_apply(shen_lazyderef, [KL_ARG_V2918_2001, KL_ARG_V2920_2003])), ([setattr(KL_CTX, 'KL_LOC_V2620_2018', tco_apply(shen_lazyderef, [KL_ARG_V2919_2002, KL_ARG_V2920_2003])), ([setattr(KL_CTX, 'KL_LOC_V2621_2019', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2620_2018), KL_ARG_V2920_2003])), ([setattr(KL_CTX, 'KL_LOC_V2622_2020', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2620_2018), KL_ARG_V2920_2003])), ([setattr(KL_CTX, 'KL_LOC_A_2021', car(KL_CTX.KL_LOC_V2622_2020)), [setattr(KL_CTX, 'KL_LOC_V2623_2022', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2622_2020), KL_ARG_V2920_2003])), ([tco_apply(shen_incinfs, []), tail_call(kl_thaw, [KL_ARG_V2921_2004])][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2623_2022) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2623_2022, nil, KL_ARG_V2920_2003]), [setattr(KL_CTX, 'KL_LOC_Result_2023', [tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V2921_2004])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2623_2022, KL_ARG_V2920_2003]), KL_CTX.KL_LOC_Result_2023][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2623_2022]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2622_2020) else ([setattr(KL_CTX, 'KL_LOC_A_2024', tco_apply(shen_newpv, [KL_ARG_V2920_2003])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2622_2020, Cons(KL_CTX.KL_LOC_A_2024, nil), KL_ARG_V2920_2003]), [setattr(KL_CTX, 'KL_LOC_Result_2025', [tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V2921_2004])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2622_2020, KL_ARG_V2920_2003]), KL_CTX.KL_LOC_Result_2025][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2622_2020]) else False))][(-1)] if shen_eq(symdic.symdic_kl_list, KL_CTX.KL_LOC_V2621_2019) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2621_2019, symdic.symdic_kl_list, KL_ARG_V2920_2003]), [setattr(KL_CTX, 'KL_LOC_Result_2026', [setattr(KL_CTX, 'KL_LOC_V2624_2027', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2620_2018), KL_ARG_V2920_2003])), ([setattr(KL_CTX, 'KL_LOC_A_2028', car(KL_CTX.KL_LOC_V2624_2027)), [setattr(KL_CTX, 'KL_LOC_V2625_2029', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2624_2027), KL_ARG_V2920_2003])), ([tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V2921_2004])][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2625_2029) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2625_2029, nil, KL_ARG_V2920_2003]), [setattr(KL_CTX, 'KL_LOC_Result_2030', [tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V2921_2004])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2625_2029, KL_ARG_V2920_2003]), KL_CTX.KL_LOC_Result_2030][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2625_2029]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2624_2027) else ([setattr(KL_CTX, 'KL_LOC_A_2031', tco_apply(shen_newpv, [KL_ARG_V2920_2003])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2624_2027, Cons(KL_CTX.KL_LOC_A_2031, nil), KL_ARG_V2920_2003]), [setattr(KL_CTX, 'KL_LOC_Result_2032', [tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V2921_2004])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2624_2027, KL_ARG_V2920_2003]), KL_CTX.KL_LOC_Result_2032][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2624_2027]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2621_2019, KL_ARG_V2920_2003]), KL_CTX.KL_LOC_Result_2026][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2621_2019]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2620_2018) else ([setattr(KL_CTX, 'KL_LOC_A_2033', tco_apply(shen_newpv, [KL_ARG_V2920_2003])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2620_2018, Cons(symdic.symdic_kl_list, Cons(KL_CTX.KL_LOC_A_2033, nil)), KL_ARG_V2920_2003]), [setattr(KL_CTX, 'KL_LOC_Result_2034', [tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V2921_2004])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2620_2018, KL_ARG_V2920_2003]), KL_CTX.KL_LOC_Result_2034][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2620_2018]) else False))][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2619_2017) else False)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2014, False) else KL_CTX.KL_LOC_Case_2014)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2011, False) else KL_CTX.KL_LOC_Case_2011)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2008, False) else KL_CTX.KL_LOC_Case_2008)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2005, False) else KL_CTX.KL_LOC_Case_2005)][(-1)]
shen_add_fun('shen.base', shen_base, 4)

@tail_recursion
def shen_by_hypothesis(*FUN_ARGS):
    FUN_ARITY = 5
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_by_hypothesis, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2922_2035 = FUN_ARGS[0]
    KL_ARG_V2923_2036 = FUN_ARGS[1]
    KL_ARG_V2924_2037 = FUN_ARGS[2]
    KL_ARG_V2925_2038 = FUN_ARGS[3]
    KL_ARG_V2926_2039 = FUN_ARGS[4]

    class KL_Context:
        KL_LOC_Case_2040 = None
        KL_LOC_V2606_2041 = None
        KL_LOC_V2607_2042 = None
        KL_LOC_Y_2043 = None
        KL_LOC_V2608_2044 = None
        KL_LOC_V2609_2045 = None
        KL_LOC_V2610_2046 = None
        KL_LOC_B_2047 = None
        KL_LOC_V2611_2048 = None
        KL_LOC_V2612_2049 = None
        KL_LOC_Hyp_2050 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Case_2040', [setattr(KL_CTX, 'KL_LOC_V2606_2041', tco_apply(shen_lazyderef, [KL_ARG_V2924_2037, KL_ARG_V2925_2038])), ([setattr(KL_CTX, 'KL_LOC_V2607_2042', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2606_2041), KL_ARG_V2925_2038])), ([setattr(KL_CTX, 'KL_LOC_Y_2043', car(KL_CTX.KL_LOC_V2607_2042)), [setattr(KL_CTX, 'KL_LOC_V2608_2044', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2607_2042), KL_ARG_V2925_2038])), ([setattr(KL_CTX, 'KL_LOC_V2609_2045', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2608_2044), KL_ARG_V2925_2038])), ([setattr(KL_CTX, 'KL_LOC_V2610_2046', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2608_2044), KL_ARG_V2925_2038])), ([setattr(KL_CTX, 'KL_LOC_B_2047', car(KL_CTX.KL_LOC_V2610_2046)), [setattr(KL_CTX, 'KL_LOC_V2611_2048', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2610_2046), KL_ARG_V2925_2038])), ([tco_apply(shen_incinfs, []), tco_apply(kl_identical, [KL_ARG_V2922_2035, KL_CTX.KL_LOC_Y_2043, KL_ARG_V2925_2038, (lambda : tail_call(kl_unifyx33, [KL_ARG_V2923_2036, KL_CTX.KL_LOC_B_2047, KL_ARG_V2925_2038, KL_ARG_V2926_2039]))])][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2611_2048) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2610_2046) else False)][(-1)] if shen_eq(symdic.symdic_kl_x58, KL_CTX.KL_LOC_V2609_2045) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2608_2044) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2607_2042) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2606_2041) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_V2612_2049', tco_apply(shen_lazyderef, [KL_ARG_V2924_2037, KL_ARG_V2925_2038])), ([setattr(KL_CTX, 'KL_LOC_Hyp_2050', cdr(KL_CTX.KL_LOC_V2612_2049)), [tco_apply(shen_incinfs, []), tail_call(shen_by_hypothesis, [KL_ARG_V2922_2035, KL_ARG_V2923_2036, KL_CTX.KL_LOC_Hyp_2050, KL_ARG_V2925_2038, KL_ARG_V2926_2039])][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2612_2049) else False)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2040, False) else KL_CTX.KL_LOC_Case_2040)][(-1)]
shen_add_fun('shen.by_hypothesis', shen_by_hypothesis, 5)

@tail_recursion
def shen_tx42x45def(*FUN_ARGS):
    FUN_ARITY = 5
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_tx42x45def, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2927_2051 = FUN_ARGS[0]
    KL_ARG_V2928_2052 = FUN_ARGS[1]
    KL_ARG_V2929_2053 = FUN_ARGS[2]
    KL_ARG_V2930_2054 = FUN_ARGS[3]
    KL_ARG_V2931_2055 = FUN_ARGS[4]

    class KL_Context:
        KL_LOC_V2600_2056 = None
        KL_LOC_V2601_2057 = None
        KL_LOC_V2602_2058 = None
        KL_LOC_F_2059 = None
        KL_LOC_X_2060 = None
        KL_LOC_E_2061 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_V2600_2056', tco_apply(shen_lazyderef, [KL_ARG_V2927_2051, KL_ARG_V2930_2054])), ([setattr(KL_CTX, 'KL_LOC_V2601_2057', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2600_2056), KL_ARG_V2930_2054])), ([setattr(KL_CTX, 'KL_LOC_V2602_2058', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2600_2056), KL_ARG_V2930_2054])), ([setattr(KL_CTX, 'KL_LOC_F_2059', car(KL_CTX.KL_LOC_V2602_2058)), [setattr(KL_CTX, 'KL_LOC_X_2060', cdr(KL_CTX.KL_LOC_V2602_2058)), [setattr(KL_CTX, 'KL_LOC_E_2061', tco_apply(shen_newpv, [KL_ARG_V2930_2054])), [tco_apply(shen_incinfs, []), tail_call(shen_tx42x45defh, [tco_apply(kl_compile, [symdic.symdic_shen_x60sigx43rulesx62, KL_CTX.KL_LOC_X_2060, (lambda KL_ARG_E_2062: (shen_simple_error(('parse error here: ' + tco_apply(shen_app, [KL_ARG_E_2062, '\r\n', symdic.symdic_shen_s]))) if shen_consp(KL_ARG_E_2062) else shen_simple_error('parse error\r\n')))]), KL_CTX.KL_LOC_F_2059, KL_ARG_V2928_2052, KL_ARG_V2929_2053, KL_ARG_V2930_2054, KL_ARG_V2931_2055])][(-1)]][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2602_2058) else False)][(-1)] if shen_eq(symdic.symdic_kl_define, KL_CTX.KL_LOC_V2601_2057) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2600_2056) else False)][(-1)]
shen_add_fun('shen.t*-def', shen_tx42x45def, 5)

@tail_recursion
def shen_tx42x45defh(*FUN_ARGS):
    FUN_ARITY = 6
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_tx42x45defh, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2932_2063 = FUN_ARGS[0]
    KL_ARG_V2933_2064 = FUN_ARGS[1]
    KL_ARG_V2934_2065 = FUN_ARGS[2]
    KL_ARG_V2935_2066 = FUN_ARGS[3]
    KL_ARG_V2936_2067 = FUN_ARGS[4]
    KL_ARG_V2937_2068 = FUN_ARGS[5]

    class KL_Context:
        KL_LOC_V2596_2069 = None
        KL_LOC_Sig_2070 = None
        KL_LOC_Rules_2071 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_V2596_2069', tco_apply(shen_lazyderef, [KL_ARG_V2932_2063, KL_ARG_V2936_2067])), ([setattr(KL_CTX, 'KL_LOC_Sig_2070', car(KL_CTX.KL_LOC_V2596_2069)), [setattr(KL_CTX, 'KL_LOC_Rules_2071', cdr(KL_CTX.KL_LOC_V2596_2069)), [tco_apply(shen_incinfs, []), tail_call(shen_tx42x45defhh, [KL_CTX.KL_LOC_Sig_2070, tco_apply(shen_ue, [KL_CTX.KL_LOC_Sig_2070]), KL_ARG_V2933_2064, KL_ARG_V2934_2065, KL_ARG_V2935_2066, KL_CTX.KL_LOC_Rules_2071, KL_ARG_V2936_2067, KL_ARG_V2937_2068])][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2596_2069) else False)][(-1)]
shen_add_fun('shen.t*-defh', shen_tx42x45defh, 6)

@tail_recursion
def shen_tx42x45defhh(*FUN_ARGS):
    FUN_ARITY = 8
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_tx42x45defhh, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2938_2072 = FUN_ARGS[0]
    KL_ARG_V2939_2073 = FUN_ARGS[1]
    KL_ARG_V2940_2074 = FUN_ARGS[2]
    KL_ARG_V2941_2075 = FUN_ARGS[3]
    KL_ARG_V2942_2076 = FUN_ARGS[4]
    KL_ARG_V2943_2077 = FUN_ARGS[5]
    KL_ARG_V2944_2078 = FUN_ARGS[6]
    KL_ARG_V2945_2079 = FUN_ARGS[7]
    global symdic
    return [tco_apply(shen_incinfs, []), tail_call(shen_tx42x45rules, [KL_ARG_V2943_2077, KL_ARG_V2939_2073, 1, KL_ARG_V2940_2074, Cons(Cons(KL_ARG_V2940_2074, Cons(symdic.symdic_kl_x58, Cons(KL_ARG_V2939_2073, nil))), KL_ARG_V2942_2076), KL_ARG_V2944_2078, (lambda : tail_call(shen_memo, [KL_ARG_V2940_2074, KL_ARG_V2938_2072, KL_ARG_V2941_2075, KL_ARG_V2944_2078, KL_ARG_V2945_2079]))])][(-1)]
shen_add_fun('shen.t*-defhh', shen_tx42x45defhh, 8)

@tail_recursion
def shen_memo(*FUN_ARGS):
    FUN_ARITY = 5
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_memo, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2946_2080 = FUN_ARGS[0]
    KL_ARG_V2947_2081 = FUN_ARGS[1]
    KL_ARG_V2948_2082 = FUN_ARGS[2]
    KL_ARG_V2949_2083 = FUN_ARGS[3]
    KL_ARG_V2950_2084 = FUN_ARGS[4]

    class KL_Context:
        KL_LOC_Jnk_2085 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Jnk_2085', tco_apply(shen_newpv, [KL_ARG_V2949_2083])), [tco_apply(shen_incinfs, []), tail_call(kl_unifyx33, [KL_ARG_V2948_2082, KL_ARG_V2947_2081, KL_ARG_V2949_2083, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Jnk_2085, apply(kl_declare, [tco_apply(shen_lazyderef, [KL_ARG_V2946_2080, KL_ARG_V2949_2083]), tco_apply(shen_lazyderef, [KL_ARG_V2948_2082, KL_ARG_V2949_2083])]), KL_ARG_V2949_2083, KL_ARG_V2950_2084]))])][(-1)]][(-1)]
shen_add_fun('shen.memo', shen_memo, 5)

@tail_recursion
def shen_x60sigx43rulesx62(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_x60sigx43rulesx62, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2955_2086 = FUN_ARGS[0]

    class KL_Context:
        KL_LOC_Result_2087 = None
        KL_LOC_Parse_shen_x60signaturex62_2088 = None
        KL_LOC_Parse_shen_x60rulesx62_2089 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_2087', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60signaturex62_2088', tco_apply(shen_x60signaturex62, [KL_ARG_V2955_2086])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60rulesx62_2089', tco_apply(shen_x60rulesx62, [KL_CTX.KL_LOC_Parse_shen_x60signaturex62_2088])), (tco_apply(shen_pair, [car(KL_CTX.KL_LOC_Parse_shen_x60rulesx62_2089), Cons(tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60signaturex62_2088]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60rulesx62_2089]))]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60rulesx62_2089)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60signaturex62_2088)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_2087, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_2087)][(-1)]
shen_add_fun('shen.<sig+rules>', shen_x60sigx43rulesx62, 1)

@tail_recursion
def shen_ue(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_ue, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2956_2090 = FUN_ARGS[0]
    global symdic
    return (tail_call(kl_map, [symdic.symdic_shen_ue, KL_ARG_V2956_2090]) if shen_consp(KL_ARG_V2956_2090) else (tail_call(kl_concat, [symdic.symdic_kl_x38x38, KL_ARG_V2956_2090]) if tco_apply(kl_variablex63, [KL_ARG_V2956_2090]) else (KL_ARG_V2956_2090 if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.ue', shen_ue, 1)

@tail_recursion
def shen_ues(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_ues, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2961_2091 = FUN_ARGS[0]
    global symdic
    return (Cons(KL_ARG_V2961_2091, nil) if tco_apply(shen_uex63, [KL_ARG_V2961_2091]) else (tail_call(kl_union, [tco_apply(shen_ues, [car(KL_ARG_V2961_2091)]), tco_apply(shen_ues, [cdr(KL_ARG_V2961_2091)])]) if shen_consp(KL_ARG_V2961_2091) else (nil if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.ues', shen_ues, 1)

@tail_recursion
def shen_uex63(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_uex63, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2962_2092 = FUN_ARGS[0]
    global symdic
    return (tail_call(shen_uex45hx63, [str(KL_ARG_V2962_2092)]) if tco_apply(kl_symbolx63, [KL_ARG_V2962_2092]) else False)
shen_add_fun('shen.ue?', shen_uex63, 1)

@tail_recursion
def shen_uex45hx63(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_uex45hx63, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2969_2093 = FUN_ARGS[0]
    global symdic
    return (True if (((shen_eq('&', KL_ARG_V2969_2093[1:][0]) if tco_apply(shen_x43stringx63, [KL_ARG_V2969_2093[1:]]) else False) if shen_eq('&', KL_ARG_V2969_2093[0]) else False) if tco_apply(shen_x43stringx63, [KL_ARG_V2969_2093]) else False) else (False if True else shen_simple_error('condition failure')))
shen_add_fun('shen.ue-h?', shen_uex45hx63, 1)

@tail_recursion
def shen_tx42x45rules(*FUN_ARGS):
    FUN_ARITY = 7
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_tx42x45rules, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2970_2094 = FUN_ARGS[0]
    KL_ARG_V2971_2095 = FUN_ARGS[1]
    KL_ARG_V2972_2096 = FUN_ARGS[2]
    KL_ARG_V2973_2097 = FUN_ARGS[3]
    KL_ARG_V2974_2098 = FUN_ARGS[4]
    KL_ARG_V2975_2099 = FUN_ARGS[5]
    KL_ARG_V2976_2100 = FUN_ARGS[6]

    class KL_Context:
        KL_LOC_Throwcontrol_2101 = None
        KL_LOC_Case_2102 = None
        KL_LOC_V2571_2103 = None
        KL_LOC_Case_2104 = None
        KL_LOC_V2572_2105 = None
        KL_LOC_V2573_2106 = None
        KL_LOC_V2574_2107 = None
        KL_LOC_V2575_2108 = None
        KL_LOC_Action_2109 = None
        KL_LOC_V2576_2110 = None
        KL_LOC_Rules_2111 = None
        KL_LOC_V2577_2112 = None
        KL_LOC_V2578_2113 = None
        KL_LOC_V2579_2114 = None
        KL_LOC_A_2115 = None
        KL_LOC_V2580_2116 = None
        KL_LOC_Case_2117 = None
        KL_LOC_V2581_2118 = None
        KL_LOC_Rule_2119 = None
        KL_LOC_Rules_2120 = None
        KL_LOC_Err_2121 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Throwcontrol_2101', tco_apply(shen_catchpoint, [])), tail_call(shen_cutpoint, [KL_CTX.KL_LOC_Throwcontrol_2101, [setattr(KL_CTX, 'KL_LOC_Case_2102', [setattr(KL_CTX, 'KL_LOC_V2571_2103', tco_apply(shen_lazyderef, [KL_ARG_V2970_2094, KL_ARG_V2975_2099])), ([tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V2976_2100])][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2571_2103) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_2104', [setattr(KL_CTX, 'KL_LOC_V2572_2105', tco_apply(shen_lazyderef, [KL_ARG_V2970_2094, KL_ARG_V2975_2099])), ([setattr(KL_CTX, 'KL_LOC_V2573_2106', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2572_2105), KL_ARG_V2975_2099])), ([setattr(KL_CTX, 'KL_LOC_V2574_2107', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2573_2106), KL_ARG_V2975_2099])), ([setattr(KL_CTX, 'KL_LOC_V2575_2108', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2573_2106), KL_ARG_V2975_2099])), ([setattr(KL_CTX, 'KL_LOC_Action_2109', car(KL_CTX.KL_LOC_V2575_2108)), [setattr(KL_CTX, 'KL_LOC_V2576_2110', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2575_2108), KL_ARG_V2975_2099])), ([setattr(KL_CTX, 'KL_LOC_Rules_2111', cdr(KL_CTX.KL_LOC_V2572_2105)), [setattr(KL_CTX, 'KL_LOC_V2577_2112', tco_apply(shen_lazyderef, [KL_ARG_V2971_2095, KL_ARG_V2975_2099])), ([setattr(KL_CTX, 'KL_LOC_V2578_2113', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2577_2112), KL_ARG_V2975_2099])), ([setattr(KL_CTX, 'KL_LOC_V2579_2114', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2577_2112), KL_ARG_V2975_2099])), ([setattr(KL_CTX, 'KL_LOC_A_2115', car(KL_CTX.KL_LOC_V2579_2114)), [setattr(KL_CTX, 'KL_LOC_V2580_2116', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2579_2114), KL_ARG_V2975_2099])), ([tco_apply(shen_incinfs, []), tco_apply(shen_tx42x45rule, [Cons(nil, Cons(tco_apply(shen_ue, [KL_CTX.KL_LOC_Action_2109]), nil)), KL_CTX.KL_LOC_A_2115, KL_ARG_V2974_2098, KL_ARG_V2975_2099, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2101, KL_ARG_V2975_2099, (lambda : tail_call(shen_tx42x45rules, [KL_CTX.KL_LOC_Rules_2111, KL_CTX.KL_LOC_A_2115, (KL_ARG_V2972_2096 + 1), KL_ARG_V2973_2097, KL_ARG_V2974_2098, KL_ARG_V2975_2099, KL_ARG_V2976_2100]))]))])][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2580_2116) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2579_2114) else False)][(-1)] if shen_eq(symdic.symdic_kl_x45x45x62, KL_CTX.KL_LOC_V2578_2113) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2577_2112) else False)][(-1)]][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2576_2110) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2575_2108) else False)][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2574_2107) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2573_2106) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2572_2105) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_2117', [setattr(KL_CTX, 'KL_LOC_V2581_2118', tco_apply(shen_lazyderef, [KL_ARG_V2970_2094, KL_ARG_V2975_2099])), ([setattr(KL_CTX, 'KL_LOC_Rule_2119', car(KL_CTX.KL_LOC_V2581_2118)), [setattr(KL_CTX, 'KL_LOC_Rules_2120', cdr(KL_CTX.KL_LOC_V2581_2118)), [tco_apply(shen_incinfs, []), tco_apply(shen_tx42x45rule, [tco_apply(shen_ue, [KL_CTX.KL_LOC_Rule_2119]), KL_ARG_V2971_2095, KL_ARG_V2974_2098, KL_ARG_V2975_2099, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2101, KL_ARG_V2975_2099, (lambda : tail_call(shen_tx42x45rules, [KL_CTX.KL_LOC_Rules_2120, KL_ARG_V2971_2095, (KL_ARG_V2972_2096 + 1), KL_ARG_V2973_2097, KL_ARG_V2974_2098, KL_ARG_V2975_2099, KL_ARG_V2976_2100]))]))])][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2581_2118) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Err_2121', tco_apply(shen_newpv, [KL_ARG_V2975_2099])), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_CTX.KL_LOC_Err_2121, shen_simple_error(('type error in rule ' + tco_apply(shen_app, [tco_apply(shen_lazyderef, [KL_ARG_V2972_2096, KL_ARG_V2975_2099]), (' of ' + tco_apply(shen_app, [tco_apply(shen_lazyderef, [KL_ARG_V2973_2097, KL_ARG_V2975_2099]), '', symdic.symdic_shen_a])), symdic.symdic_shen_a]))), KL_ARG_V2975_2099, KL_ARG_V2976_2100])][(-1)]][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2117, False) else KL_CTX.KL_LOC_Case_2117)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2104, False) else KL_CTX.KL_LOC_Case_2104)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2102, False) else KL_CTX.KL_LOC_Case_2102)][(-1)]])][(-1)]
shen_add_fun('shen.t*-rules', shen_tx42x45rules, 7)

@tail_recursion
def shen_tx42x45rule(*FUN_ARGS):
    FUN_ARITY = 5
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_tx42x45rule, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2977_2122 = FUN_ARGS[0]
    KL_ARG_V2978_2123 = FUN_ARGS[1]
    KL_ARG_V2979_2124 = FUN_ARGS[2]
    KL_ARG_V2980_2125 = FUN_ARGS[3]
    KL_ARG_V2981_2126 = FUN_ARGS[4]

    class KL_Context:
        KL_LOC_Throwcontrol_2127 = None
        KL_LOC_Case_2128 = None
        KL_LOC_V2553_2129 = None
        KL_LOC_V2554_2130 = None
        KL_LOC_V2555_2131 = None
        KL_LOC_Action_2132 = None
        KL_LOC_V2556_2133 = None
        KL_LOC_V2557_2134 = None
        KL_LOC_V2558_2135 = None
        KL_LOC_Pattern_2136 = None
        KL_LOC_Patterns_2137 = None
        KL_LOC_V2559_2138 = None
        KL_LOC_Action_2139 = None
        KL_LOC_V2560_2140 = None
        KL_LOC_V2561_2141 = None
        KL_LOC_A_2142 = None
        KL_LOC_V2562_2143 = None
        KL_LOC_V2563_2144 = None
        KL_LOC_V2564_2145 = None
        KL_LOC_B_2146 = None
        KL_LOC_V2565_2147 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Throwcontrol_2127', tco_apply(shen_catchpoint, [])), tail_call(shen_cutpoint, [KL_CTX.KL_LOC_Throwcontrol_2127, [setattr(KL_CTX, 'KL_LOC_Case_2128', [setattr(KL_CTX, 'KL_LOC_V2553_2129', tco_apply(shen_lazyderef, [KL_ARG_V2977_2122, KL_ARG_V2980_2125])), ([setattr(KL_CTX, 'KL_LOC_V2554_2130', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2553_2129), KL_ARG_V2980_2125])), ([setattr(KL_CTX, 'KL_LOC_V2555_2131', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2553_2129), KL_ARG_V2980_2125])), ([setattr(KL_CTX, 'KL_LOC_Action_2132', car(KL_CTX.KL_LOC_V2555_2131)), [setattr(KL_CTX, 'KL_LOC_V2556_2133', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2555_2131), KL_ARG_V2980_2125])), ([tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2127, KL_ARG_V2980_2125, (lambda : tail_call(shen_tx42x45action, [tco_apply(shen_curry, [KL_CTX.KL_LOC_Action_2132]), KL_ARG_V2978_2123, KL_ARG_V2979_2124, KL_ARG_V2980_2125, KL_ARG_V2981_2126]))])][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2556_2133) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2555_2131) else False)][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2554_2130) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2553_2129) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_V2557_2134', tco_apply(shen_lazyderef, [KL_ARG_V2977_2122, KL_ARG_V2980_2125])), ([setattr(KL_CTX, 'KL_LOC_V2558_2135', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2557_2134), KL_ARG_V2980_2125])), ([setattr(KL_CTX, 'KL_LOC_Pattern_2136', car(KL_CTX.KL_LOC_V2558_2135)), [setattr(KL_CTX, 'KL_LOC_Patterns_2137', cdr(KL_CTX.KL_LOC_V2558_2135)), [setattr(KL_CTX, 'KL_LOC_V2559_2138', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2557_2134), KL_ARG_V2980_2125])), ([setattr(KL_CTX, 'KL_LOC_Action_2139', car(KL_CTX.KL_LOC_V2559_2138)), [setattr(KL_CTX, 'KL_LOC_V2560_2140', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2559_2138), KL_ARG_V2980_2125])), ([setattr(KL_CTX, 'KL_LOC_V2561_2141', tco_apply(shen_lazyderef, [KL_ARG_V2978_2123, KL_ARG_V2980_2125])), ([setattr(KL_CTX, 'KL_LOC_A_2142', car(KL_CTX.KL_LOC_V2561_2141)), [setattr(KL_CTX, 'KL_LOC_V2562_2143', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2561_2141), KL_ARG_V2980_2125])), ([setattr(KL_CTX, 'KL_LOC_V2563_2144', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2562_2143), KL_ARG_V2980_2125])), ([setattr(KL_CTX, 'KL_LOC_V2564_2145', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2562_2143), KL_ARG_V2980_2125])), ([setattr(KL_CTX, 'KL_LOC_B_2146', car(KL_CTX.KL_LOC_V2564_2145)), [setattr(KL_CTX, 'KL_LOC_V2565_2147', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2564_2145), KL_ARG_V2980_2125])), ([tco_apply(shen_incinfs, []), tco_apply(shen_tx42x45pattern, [KL_CTX.KL_LOC_Pattern_2136, KL_CTX.KL_LOC_A_2142, KL_ARG_V2980_2125, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2127, KL_ARG_V2980_2125, (lambda : tail_call(shen_tx42x45rule, [Cons(KL_CTX.KL_LOC_Patterns_2137, Cons(KL_CTX.KL_LOC_Action_2139, nil)), KL_CTX.KL_LOC_B_2146, Cons(Cons(KL_CTX.KL_LOC_Pattern_2136, Cons(symdic.symdic_kl_x58, Cons(KL_CTX.KL_LOC_A_2142, nil))), KL_ARG_V2979_2124), KL_ARG_V2980_2125, KL_ARG_V2981_2126]))]))])][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2565_2147) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2564_2145) else False)][(-1)] if shen_eq(symdic.symdic_kl_x45x45x62, KL_CTX.KL_LOC_V2563_2144) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2562_2143) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2561_2141) else False)][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2560_2140) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2559_2138) else False)][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2558_2135) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2557_2134) else False)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2128, False) else KL_CTX.KL_LOC_Case_2128)][(-1)]])][(-1)]
shen_add_fun('shen.t*-rule', shen_tx42x45rule, 5)

@tail_recursion
def shen_tx42x45action(*FUN_ARGS):
    FUN_ARITY = 5
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_tx42x45action, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2982_2148 = FUN_ARGS[0]
    KL_ARG_V2983_2149 = FUN_ARGS[1]
    KL_ARG_V2984_2150 = FUN_ARGS[2]
    KL_ARG_V2985_2151 = FUN_ARGS[3]
    KL_ARG_V2986_2152 = FUN_ARGS[4]

    class KL_Context:
        KL_LOC_Throwcontrol_2153 = None
        KL_LOC_Case_2154 = None
        KL_LOC_V2530_2155 = None
        KL_LOC_V2531_2156 = None
        KL_LOC_V2532_2157 = None
        KL_LOC_P_2158 = None
        KL_LOC_V2533_2159 = None
        KL_LOC_Action_2160 = None
        KL_LOC_V2534_2161 = None
        KL_LOC_Case_2162 = None
        KL_LOC_V2535_2163 = None
        KL_LOC_V2536_2164 = None
        KL_LOC_V2537_2165 = None
        KL_LOC_V2538_2166 = None
        KL_LOC_V2539_2167 = None
        KL_LOC_V2540_2168 = None
        KL_LOC_V2541_2169 = None
        KL_LOC_F_2170 = None
        KL_LOC_V2542_2171 = None
        KL_LOC_V2543_2172 = None
        KL_LOC_Action_2173 = None
        KL_LOC_V2544_2174 = None
        KL_LOC_V2545_2175 = None
        KL_LOC_Case_2176 = None
        KL_LOC_V2546_2177 = None
        KL_LOC_V2547_2178 = None
        KL_LOC_V2548_2179 = None
        KL_LOC_Action_2180 = None
        KL_LOC_V2549_2181 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Throwcontrol_2153', tco_apply(shen_catchpoint, [])), tail_call(shen_cutpoint, [KL_CTX.KL_LOC_Throwcontrol_2153, [setattr(KL_CTX, 'KL_LOC_Case_2154', [setattr(KL_CTX, 'KL_LOC_V2530_2155', tco_apply(shen_lazyderef, [KL_ARG_V2982_2148, KL_ARG_V2985_2151])), ([setattr(KL_CTX, 'KL_LOC_V2531_2156', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2530_2155), KL_ARG_V2985_2151])), ([setattr(KL_CTX, 'KL_LOC_V2532_2157', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2530_2155), KL_ARG_V2985_2151])), ([setattr(KL_CTX, 'KL_LOC_P_2158', car(KL_CTX.KL_LOC_V2532_2157)), [setattr(KL_CTX, 'KL_LOC_V2533_2159', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2532_2157), KL_ARG_V2985_2151])), ([setattr(KL_CTX, 'KL_LOC_Action_2160', car(KL_CTX.KL_LOC_V2533_2159)), [setattr(KL_CTX, 'KL_LOC_V2534_2161', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2533_2159), KL_ARG_V2985_2151])), ([tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2153, KL_ARG_V2985_2151, (lambda : tail_call(shen_tx42, [Cons(KL_CTX.KL_LOC_P_2158, Cons(symdic.symdic_kl_x58, Cons(symdic.symdic_kl_boolean, nil))), KL_ARG_V2984_2150, KL_ARG_V2985_2151, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2153, KL_ARG_V2985_2151, (lambda : tail_call(shen_tx42x45action, [KL_CTX.KL_LOC_Action_2160, KL_ARG_V2983_2149, Cons(Cons(KL_CTX.KL_LOC_P_2158, Cons(symdic.symdic_kl_x58, Cons(symdic.symdic_kl_verified, nil))), KL_ARG_V2984_2150), KL_ARG_V2985_2151, KL_ARG_V2986_2152]))]))]))])][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2534_2161) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2533_2159) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2532_2157) else False)][(-1)] if shen_eq(symdic.symdic_kl_where, KL_CTX.KL_LOC_V2531_2156) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2530_2155) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_2162', [setattr(KL_CTX, 'KL_LOC_V2535_2163', tco_apply(shen_lazyderef, [KL_ARG_V2982_2148, KL_ARG_V2985_2151])), ([setattr(KL_CTX, 'KL_LOC_V2536_2164', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2535_2163), KL_ARG_V2985_2151])), ([setattr(KL_CTX, 'KL_LOC_V2537_2165', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2535_2163), KL_ARG_V2985_2151])), ([setattr(KL_CTX, 'KL_LOC_V2538_2166', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2537_2165), KL_ARG_V2985_2151])), ([setattr(KL_CTX, 'KL_LOC_V2539_2167', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2538_2166), KL_ARG_V2985_2151])), ([setattr(KL_CTX, 'KL_LOC_V2540_2168', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2539_2167), KL_ARG_V2985_2151])), ([setattr(KL_CTX, 'KL_LOC_V2541_2169', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2539_2167), KL_ARG_V2985_2151])), ([setattr(KL_CTX, 'KL_LOC_F_2170', car(KL_CTX.KL_LOC_V2541_2169)), [setattr(KL_CTX, 'KL_LOC_V2542_2171', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2541_2169), KL_ARG_V2985_2151])), ([setattr(KL_CTX, 'KL_LOC_V2543_2172', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2538_2166), KL_ARG_V2985_2151])), ([setattr(KL_CTX, 'KL_LOC_Action_2173', car(KL_CTX.KL_LOC_V2543_2172)), [setattr(KL_CTX, 'KL_LOC_V2544_2174', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2543_2172), KL_ARG_V2985_2151])), ([setattr(KL_CTX, 'KL_LOC_V2545_2175', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2537_2165), KL_ARG_V2985_2151])), ([tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2153, KL_ARG_V2985_2151, (lambda : tail_call(shen_tx42x45action, [Cons(symdic.symdic_kl_where, Cons(Cons(symdic.symdic_kl_not, Cons(Cons(KL_CTX.KL_LOC_F_2170, Cons(KL_CTX.KL_LOC_Action_2173, nil)), nil)), Cons(KL_CTX.KL_LOC_Action_2173, nil))), KL_ARG_V2983_2149, KL_ARG_V2984_2150, KL_ARG_V2985_2151, KL_ARG_V2986_2152]))])][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2545_2175) else False)][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2544_2174) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2543_2172) else False)][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2542_2171) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2541_2169) else False)][(-1)] if shen_eq(symdic.symdic_kl_failx45if, KL_CTX.KL_LOC_V2540_2168) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2539_2167) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2538_2166) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2537_2165) else False)][(-1)] if shen_eq(symdic.symdic_shen_choicepointx33, KL_CTX.KL_LOC_V2536_2164) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2535_2163) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_2176', [setattr(KL_CTX, 'KL_LOC_V2546_2177', tco_apply(shen_lazyderef, [KL_ARG_V2982_2148, KL_ARG_V2985_2151])), ([setattr(KL_CTX, 'KL_LOC_V2547_2178', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2546_2177), KL_ARG_V2985_2151])), ([setattr(KL_CTX, 'KL_LOC_V2548_2179', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2546_2177), KL_ARG_V2985_2151])), ([setattr(KL_CTX, 'KL_LOC_Action_2180', car(KL_CTX.KL_LOC_V2548_2179)), [setattr(KL_CTX, 'KL_LOC_V2549_2181', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2548_2179), KL_ARG_V2985_2151])), ([tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2153, KL_ARG_V2985_2151, (lambda : tail_call(shen_tx42x45action, [Cons(symdic.symdic_kl_where, Cons(Cons(symdic.symdic_kl_not, Cons(Cons(Cons(symdic.symdic_kl_x61, Cons(KL_CTX.KL_LOC_Action_2180, nil)), Cons(Cons(symdic.symdic_kl_fail, nil), nil)), nil)), Cons(KL_CTX.KL_LOC_Action_2180, nil))), KL_ARG_V2983_2149, KL_ARG_V2984_2150, KL_ARG_V2985_2151, KL_ARG_V2986_2152]))])][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2549_2181) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2548_2179) else False)][(-1)] if shen_eq(symdic.symdic_shen_choicepointx33, KL_CTX.KL_LOC_V2547_2178) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2546_2177) else False)][(-1)]), ([tco_apply(shen_incinfs, []), tco_apply(shen_tx42, [Cons(KL_ARG_V2982_2148, Cons(symdic.symdic_kl_x58, Cons(KL_ARG_V2983_2149, nil))), KL_ARG_V2984_2150, KL_ARG_V2985_2151, KL_ARG_V2986_2152])][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2176, False) else KL_CTX.KL_LOC_Case_2176)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2162, False) else KL_CTX.KL_LOC_Case_2162)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2154, False) else KL_CTX.KL_LOC_Case_2154)][(-1)]])][(-1)]
shen_add_fun('shen.t*-action', shen_tx42x45action, 5)

@tail_recursion
def shen_tx42x45pattern(*FUN_ARGS):
    FUN_ARITY = 4
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_tx42x45pattern, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2987_2182 = FUN_ARGS[0]
    KL_ARG_V2988_2183 = FUN_ARGS[1]
    KL_ARG_V2989_2184 = FUN_ARGS[2]
    KL_ARG_V2990_2185 = FUN_ARGS[3]

    class KL_Context:
        KL_LOC_Throwcontrol_2186 = None
        KL_LOC_Hyp_2187 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Throwcontrol_2186', tco_apply(shen_catchpoint, [])), tail_call(shen_cutpoint, [KL_CTX.KL_LOC_Throwcontrol_2186, [setattr(KL_CTX, 'KL_LOC_Hyp_2187', tco_apply(shen_newpv, [KL_ARG_V2989_2184])), [tco_apply(shen_incinfs, []), tco_apply(shen_tmsx45x62hyp, [tco_apply(shen_ues, [KL_ARG_V2987_2182]), KL_CTX.KL_LOC_Hyp_2187, KL_ARG_V2989_2184, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2186, KL_ARG_V2989_2184, (lambda : tail_call(shen_tx42, [Cons(KL_ARG_V2987_2182, Cons(symdic.symdic_kl_x58, Cons(KL_ARG_V2988_2183, nil))), KL_CTX.KL_LOC_Hyp_2187, KL_ARG_V2989_2184, KL_ARG_V2990_2185]))]))])][(-1)]][(-1)]])][(-1)]
shen_add_fun('shen.t*-pattern', shen_tx42x45pattern, 4)

@tail_recursion
def shen_tmsx45x62hyp(*FUN_ARGS):
    FUN_ARITY = 4
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_tmsx45x62hyp, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2991_2188 = FUN_ARGS[0]
    KL_ARG_V2992_2189 = FUN_ARGS[1]
    KL_ARG_V2993_2190 = FUN_ARGS[2]
    KL_ARG_V2994_2191 = FUN_ARGS[3]

    class KL_Context:
        KL_LOC_Case_2192 = None
        KL_LOC_V2514_2193 = None
        KL_LOC_V2515_2194 = None
        KL_LOC_Result_2195 = None
        KL_LOC_V2516_2196 = None
        KL_LOC_Tm2511_2197 = None
        KL_LOC_Tms_2198 = None
        KL_LOC_V2517_2199 = None
        KL_LOC_V2518_2200 = None
        KL_LOC_Tm_2201 = None
        KL_LOC_V2519_2202 = None
        KL_LOC_V2520_2203 = None
        KL_LOC_V2521_2204 = None
        KL_LOC_A_2205 = None
        KL_LOC_V2522_2206 = None
        KL_LOC_Hyp_2207 = None
        KL_LOC_Result_2208 = None
        KL_LOC_Hyp_2209 = None
        KL_LOC_A_2210 = None
        KL_LOC_Result_2211 = None
        KL_LOC_Hyp_2212 = None
        KL_LOC_Result_2213 = None
        KL_LOC_V2523_2214 = None
        KL_LOC_A_2215 = None
        KL_LOC_V2524_2216 = None
        KL_LOC_Hyp_2217 = None
        KL_LOC_Result_2218 = None
        KL_LOC_Hyp_2219 = None
        KL_LOC_A_2220 = None
        KL_LOC_Result_2221 = None
        KL_LOC_Hyp_2222 = None
        KL_LOC_A_2223 = None
        KL_LOC_Result_2224 = None
        KL_LOC_Hyp_2225 = None
        KL_LOC_Tm_2226 = None
        KL_LOC_A_2227 = None
        KL_LOC_Result_2228 = None
        KL_LOC_Hyp_2229 = None
        KL_LOC_Tm_2230 = None
        KL_LOC_A_2231 = None
        KL_LOC_Hyp_2232 = None
        KL_LOC_Result_2233 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Case_2192', [setattr(KL_CTX, 'KL_LOC_V2514_2193', tco_apply(shen_lazyderef, [KL_ARG_V2991_2188, KL_ARG_V2993_2190])), ([setattr(KL_CTX, 'KL_LOC_V2515_2194', tco_apply(shen_lazyderef, [KL_ARG_V2992_2189, KL_ARG_V2993_2190])), ([tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V2994_2191])][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2515_2194) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2515_2194, nil, KL_ARG_V2993_2190]), [setattr(KL_CTX, 'KL_LOC_Result_2195', [tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V2994_2191])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2515_2194, KL_ARG_V2993_2190]), KL_CTX.KL_LOC_Result_2195][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2515_2194]) else False))][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2514_2193) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_V2516_2196', tco_apply(shen_lazyderef, [KL_ARG_V2991_2188, KL_ARG_V2993_2190])), ([setattr(KL_CTX, 'KL_LOC_Tm2511_2197', car(KL_CTX.KL_LOC_V2516_2196)), [setattr(KL_CTX, 'KL_LOC_Tms_2198', cdr(KL_CTX.KL_LOC_V2516_2196)), [setattr(KL_CTX, 'KL_LOC_V2517_2199', tco_apply(shen_lazyderef, [KL_ARG_V2992_2189, KL_ARG_V2993_2190])), ([setattr(KL_CTX, 'KL_LOC_V2518_2200', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2517_2199), KL_ARG_V2993_2190])), ([setattr(KL_CTX, 'KL_LOC_Tm_2201', car(KL_CTX.KL_LOC_V2518_2200)), [setattr(KL_CTX, 'KL_LOC_V2519_2202', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2518_2200), KL_ARG_V2993_2190])), ([setattr(KL_CTX, 'KL_LOC_V2520_2203', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2519_2202), KL_ARG_V2993_2190])), ([setattr(KL_CTX, 'KL_LOC_V2521_2204', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2519_2202), KL_ARG_V2993_2190])), ([setattr(KL_CTX, 'KL_LOC_A_2205', car(KL_CTX.KL_LOC_V2521_2204)), [setattr(KL_CTX, 'KL_LOC_V2522_2206', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2521_2204), KL_ARG_V2993_2190])), ([setattr(KL_CTX, 'KL_LOC_Hyp_2207', cdr(KL_CTX.KL_LOC_V2517_2199)), [tco_apply(shen_incinfs, []), tail_call(kl_unifyx33, [KL_CTX.KL_LOC_Tm_2201, KL_CTX.KL_LOC_Tm2511_2197, KL_ARG_V2993_2190, (lambda : tail_call(shen_tmsx45x62hyp, [KL_CTX.KL_LOC_Tms_2198, KL_CTX.KL_LOC_Hyp_2207, KL_ARG_V2993_2190, KL_ARG_V2994_2191]))])][(-1)]][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2522_2206) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2522_2206, nil, KL_ARG_V2993_2190]), [setattr(KL_CTX, 'KL_LOC_Result_2208', [setattr(KL_CTX, 'KL_LOC_Hyp_2209', cdr(KL_CTX.KL_LOC_V2517_2199)), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_Tm_2201, KL_CTX.KL_LOC_Tm2511_2197, KL_ARG_V2993_2190, (lambda : tail_call(shen_tmsx45x62hyp, [KL_CTX.KL_LOC_Tms_2198, KL_CTX.KL_LOC_Hyp_2209, KL_ARG_V2993_2190, KL_ARG_V2994_2191]))])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2522_2206, KL_ARG_V2993_2190]), KL_CTX.KL_LOC_Result_2208][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2522_2206]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2521_2204) else ([setattr(KL_CTX, 'KL_LOC_A_2210', tco_apply(shen_newpv, [KL_ARG_V2993_2190])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2521_2204, Cons(KL_CTX.KL_LOC_A_2210, nil), KL_ARG_V2993_2190]), [setattr(KL_CTX, 'KL_LOC_Result_2211', [setattr(KL_CTX, 'KL_LOC_Hyp_2212', cdr(KL_CTX.KL_LOC_V2517_2199)), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_Tm_2201, KL_CTX.KL_LOC_Tm2511_2197, KL_ARG_V2993_2190, (lambda : tail_call(shen_tmsx45x62hyp, [KL_CTX.KL_LOC_Tms_2198, KL_CTX.KL_LOC_Hyp_2212, KL_ARG_V2993_2190, KL_ARG_V2994_2191]))])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2521_2204, KL_ARG_V2993_2190]), KL_CTX.KL_LOC_Result_2211][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2521_2204]) else False))][(-1)] if shen_eq(symdic.symdic_kl_x58, KL_CTX.KL_LOC_V2520_2203) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2520_2203, symdic.symdic_kl_x58, KL_ARG_V2993_2190]), [setattr(KL_CTX, 'KL_LOC_Result_2213', [setattr(KL_CTX, 'KL_LOC_V2523_2214', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2519_2202), KL_ARG_V2993_2190])), ([setattr(KL_CTX, 'KL_LOC_A_2215', car(KL_CTX.KL_LOC_V2523_2214)), [setattr(KL_CTX, 'KL_LOC_V2524_2216', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2523_2214), KL_ARG_V2993_2190])), ([setattr(KL_CTX, 'KL_LOC_Hyp_2217', cdr(KL_CTX.KL_LOC_V2517_2199)), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_Tm_2201, KL_CTX.KL_LOC_Tm2511_2197, KL_ARG_V2993_2190, (lambda : tail_call(shen_tmsx45x62hyp, [KL_CTX.KL_LOC_Tms_2198, KL_CTX.KL_LOC_Hyp_2217, KL_ARG_V2993_2190, KL_ARG_V2994_2191]))])][(-1)]][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2524_2216) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2524_2216, nil, KL_ARG_V2993_2190]), [setattr(KL_CTX, 'KL_LOC_Result_2218', [setattr(KL_CTX, 'KL_LOC_Hyp_2219', cdr(KL_CTX.KL_LOC_V2517_2199)), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_Tm_2201, KL_CTX.KL_LOC_Tm2511_2197, KL_ARG_V2993_2190, (lambda : tail_call(shen_tmsx45x62hyp, [KL_CTX.KL_LOC_Tms_2198, KL_CTX.KL_LOC_Hyp_2219, KL_ARG_V2993_2190, KL_ARG_V2994_2191]))])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2524_2216, KL_ARG_V2993_2190]), KL_CTX.KL_LOC_Result_2218][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2524_2216]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2523_2214) else ([setattr(KL_CTX, 'KL_LOC_A_2220', tco_apply(shen_newpv, [KL_ARG_V2993_2190])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2523_2214, Cons(KL_CTX.KL_LOC_A_2220, nil), KL_ARG_V2993_2190]), [setattr(KL_CTX, 'KL_LOC_Result_2221', [setattr(KL_CTX, 'KL_LOC_Hyp_2222', cdr(KL_CTX.KL_LOC_V2517_2199)), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_Tm_2201, KL_CTX.KL_LOC_Tm2511_2197, KL_ARG_V2993_2190, (lambda : tail_call(shen_tmsx45x62hyp, [KL_CTX.KL_LOC_Tms_2198, KL_CTX.KL_LOC_Hyp_2222, KL_ARG_V2993_2190, KL_ARG_V2994_2191]))])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2523_2214, KL_ARG_V2993_2190]), KL_CTX.KL_LOC_Result_2221][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2523_2214]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2520_2203, KL_ARG_V2993_2190]), KL_CTX.KL_LOC_Result_2213][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2520_2203]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2519_2202) else ([setattr(KL_CTX, 'KL_LOC_A_2223', tco_apply(shen_newpv, [KL_ARG_V2993_2190])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2519_2202, Cons(symdic.symdic_kl_x58, Cons(KL_CTX.KL_LOC_A_2223, nil)), KL_ARG_V2993_2190]), [setattr(KL_CTX, 'KL_LOC_Result_2224', [setattr(KL_CTX, 'KL_LOC_Hyp_2225', cdr(KL_CTX.KL_LOC_V2517_2199)), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_Tm_2201, KL_CTX.KL_LOC_Tm2511_2197, KL_ARG_V2993_2190, (lambda : tail_call(shen_tmsx45x62hyp, [KL_CTX.KL_LOC_Tms_2198, KL_CTX.KL_LOC_Hyp_2225, KL_ARG_V2993_2190, KL_ARG_V2994_2191]))])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2519_2202, KL_ARG_V2993_2190]), KL_CTX.KL_LOC_Result_2224][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2519_2202]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2518_2200) else ([setattr(KL_CTX, 'KL_LOC_Tm_2226', tco_apply(shen_newpv, [KL_ARG_V2993_2190])), [setattr(KL_CTX, 'KL_LOC_A_2227', tco_apply(shen_newpv, [KL_ARG_V2993_2190])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2518_2200, Cons(KL_CTX.KL_LOC_Tm_2226, Cons(symdic.symdic_kl_x58, Cons(KL_CTX.KL_LOC_A_2227, nil))), KL_ARG_V2993_2190]), [setattr(KL_CTX, 'KL_LOC_Result_2228', [setattr(KL_CTX, 'KL_LOC_Hyp_2229', cdr(KL_CTX.KL_LOC_V2517_2199)), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_Tm_2226, KL_CTX.KL_LOC_Tm2511_2197, KL_ARG_V2993_2190, (lambda : tail_call(shen_tmsx45x62hyp, [KL_CTX.KL_LOC_Tms_2198, KL_CTX.KL_LOC_Hyp_2229, KL_ARG_V2993_2190, KL_ARG_V2994_2191]))])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2518_2200, KL_ARG_V2993_2190]), KL_CTX.KL_LOC_Result_2228][(-1)]][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2518_2200]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2517_2199) else ([setattr(KL_CTX, 'KL_LOC_Tm_2230', tco_apply(shen_newpv, [KL_ARG_V2993_2190])), [setattr(KL_CTX, 'KL_LOC_A_2231', tco_apply(shen_newpv, [KL_ARG_V2993_2190])), [setattr(KL_CTX, 'KL_LOC_Hyp_2232', tco_apply(shen_newpv, [KL_ARG_V2993_2190])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2517_2199, Cons(Cons(KL_CTX.KL_LOC_Tm_2230, Cons(symdic.symdic_kl_x58, Cons(KL_CTX.KL_LOC_A_2231, nil))), KL_CTX.KL_LOC_Hyp_2232), KL_ARG_V2993_2190]), [setattr(KL_CTX, 'KL_LOC_Result_2233', [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_Tm_2230, KL_CTX.KL_LOC_Tm2511_2197, KL_ARG_V2993_2190, (lambda : tail_call(shen_tmsx45x62hyp, [KL_CTX.KL_LOC_Tms_2198, KL_CTX.KL_LOC_Hyp_2232, KL_ARG_V2993_2190, KL_ARG_V2994_2191]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2517_2199, KL_ARG_V2993_2190]), KL_CTX.KL_LOC_Result_2233][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2517_2199]) else False))][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2516_2196) else False)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2192, False) else KL_CTX.KL_LOC_Case_2192)][(-1)]
shen_add_fun('shen.tms->hyp', shen_tmsx45x62hyp, 4)

@tail_recursion
def kl_findall(*FUN_ARGS):
    FUN_ARITY = 5
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(kl_findall, (FUN_ARGS + lambdaargs)))
    KL_ARG_V2995_2234 = FUN_ARGS[0]
    KL_ARG_V2996_2235 = FUN_ARGS[1]
    KL_ARG_V2997_2236 = FUN_ARGS[2]
    KL_ARG_V2998_2237 = FUN_ARGS[3]
    KL_ARG_V2999_2238 = FUN_ARGS[4]

    class KL_Context:
        KL_LOC_B_2239 = None
        KL_LOC_A_2240 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_B_2239', tco_apply(shen_newpv, [KL_ARG_V2998_2237])), [setattr(KL_CTX, 'KL_LOC_A_2240', tco_apply(shen_newpv, [KL_ARG_V2998_2237])), [tco_apply(shen_incinfs, []), tail_call(kl_bind, [KL_CTX.KL_LOC_A_2240, tco_apply(kl_gensym, [symdic.symdic_shen_a]), KL_ARG_V2998_2237, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_B_2239, shen_set(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_2240, KL_ARG_V2998_2237]), nil), KL_ARG_V2998_2237, (lambda : tail_call(shen_findallhelp, [KL_ARG_V2995_2234, KL_ARG_V2996_2235, KL_ARG_V2997_2236, KL_CTX.KL_LOC_A_2240, KL_ARG_V2998_2237, KL_ARG_V2999_2238]))]))])][(-1)]][(-1)]][(-1)]
shen_add_fun('findall', kl_findall, 5)

@tail_recursion
def shen_findallhelp(*FUN_ARGS):
    FUN_ARITY = 6
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_findallhelp, (FUN_ARGS + lambdaargs)))
    KL_ARG_V3000_2241 = FUN_ARGS[0]
    KL_ARG_V3001_2242 = FUN_ARGS[1]
    KL_ARG_V3002_2243 = FUN_ARGS[2]
    KL_ARG_V3003_2244 = FUN_ARGS[3]
    KL_ARG_V3004_2245 = FUN_ARGS[4]
    KL_ARG_V3005_2246 = FUN_ARGS[5]

    class KL_Context:
        KL_LOC_Case_2247 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Case_2247', [tco_apply(shen_incinfs, []), tco_apply(kl_call, [KL_ARG_V3001_2242, KL_ARG_V3004_2245, (lambda : tail_call(shen_remember, [KL_ARG_V3003_2244, KL_ARG_V3000_2241, KL_ARG_V3004_2245, (lambda : tail_call(kl_fwhen, [False, KL_ARG_V3004_2245, KL_ARG_V3005_2246]))]))])][(-1)]), ([tco_apply(shen_incinfs, []), tail_call(kl_bind, [KL_ARG_V3002_2243, shen_get(tco_apply(shen_lazyderef, [KL_ARG_V3003_2244, KL_ARG_V3004_2245])), KL_ARG_V3004_2245, KL_ARG_V3005_2246])][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2247, False) else KL_CTX.KL_LOC_Case_2247)][(-1)]
shen_add_fun('shen.findallhelp', shen_findallhelp, 6)

@tail_recursion
def shen_remember(*FUN_ARGS):
    FUN_ARITY = 4
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_remember, (FUN_ARGS + lambdaargs)))
    KL_ARG_V3006_2248 = FUN_ARGS[0]
    KL_ARG_V3007_2249 = FUN_ARGS[1]
    KL_ARG_V3008_2250 = FUN_ARGS[2]
    KL_ARG_V3009_2251 = FUN_ARGS[3]

    class KL_Context:
        KL_LOC_B_2252 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_B_2252', tco_apply(shen_newpv, [KL_ARG_V3008_2250])), [tco_apply(shen_incinfs, []), tail_call(kl_bind, [KL_CTX.KL_LOC_B_2252, shen_set(tco_apply(shen_deref, [KL_ARG_V3006_2248, KL_ARG_V3008_2250]), Cons(tco_apply(shen_deref, [KL_ARG_V3007_2249, KL_ARG_V3008_2250]), shen_get(tco_apply(shen_deref, [KL_ARG_V3006_2248, KL_ARG_V3008_2250])))), KL_ARG_V3008_2250, KL_ARG_V3009_2251])][(-1)]][(-1)]
shen_add_fun('shen.remember', shen_remember, 4)

@tail_recursion
def shen_tx42x45defcc(*FUN_ARGS):
    FUN_ARITY = 5
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_tx42x45defcc, (FUN_ARGS + lambdaargs)))
    KL_ARG_V3010_2253 = FUN_ARGS[0]
    KL_ARG_V3011_2254 = FUN_ARGS[1]
    KL_ARG_V3012_2255 = FUN_ARGS[2]
    KL_ARG_V3013_2256 = FUN_ARGS[3]
    KL_ARG_V3014_2257 = FUN_ARGS[4]

    class KL_Context:
        KL_LOC_Throwcontrol_2258 = None
        KL_LOC_V2487_2259 = None
        KL_LOC_V2488_2260 = None
        KL_LOC_V2489_2261 = None
        KL_LOC_F_2262 = None
        KL_LOC_V2490_2263 = None
        KL_LOC_V2491_2264 = None
        KL_LOC_V2492_2265 = None
        KL_LOC_V2493_2266 = None
        KL_LOC_V2494_2267 = None
        KL_LOC_V2495_2268 = None
        KL_LOC_A_2269 = None
        KL_LOC_V2496_2270 = None
        KL_LOC_V2497_2271 = None
        KL_LOC_V2498_2272 = None
        KL_LOC_V2499_2273 = None
        KL_LOC_B_2274 = None
        KL_LOC_V2500_2275 = None
        KL_LOC_V2501_2276 = None
        KL_LOC_Rest_2277 = None
        KL_LOC_Restx38_2278 = None
        KL_LOC_Restx38x38_2279 = None
        KL_LOC_Rules_2280 = None
        KL_LOC_ListAx38x38_2281 = None
        KL_LOC_Bx38x38_2282 = None
        KL_LOC_Sig_2283 = None
        KL_LOC_Declare_2284 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Throwcontrol_2258', tco_apply(shen_catchpoint, [])), tail_call(shen_cutpoint, [KL_CTX.KL_LOC_Throwcontrol_2258, [setattr(KL_CTX, 'KL_LOC_V2487_2259', tco_apply(shen_lazyderef, [KL_ARG_V3010_2253, KL_ARG_V3013_2256])), ([setattr(KL_CTX, 'KL_LOC_V2488_2260', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2487_2259), KL_ARG_V3013_2256])), ([setattr(KL_CTX, 'KL_LOC_V2489_2261', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2487_2259), KL_ARG_V3013_2256])), ([setattr(KL_CTX, 'KL_LOC_F_2262', car(KL_CTX.KL_LOC_V2489_2261)), [setattr(KL_CTX, 'KL_LOC_V2490_2263', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2489_2261), KL_ARG_V3013_2256])), ([setattr(KL_CTX, 'KL_LOC_V2491_2264', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2490_2263), KL_ARG_V3013_2256])), ([setattr(KL_CTX, 'KL_LOC_V2492_2265', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2490_2263), KL_ARG_V3013_2256])), ([setattr(KL_CTX, 'KL_LOC_V2493_2266', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2492_2265), KL_ARG_V3013_2256])), ([setattr(KL_CTX, 'KL_LOC_V2494_2267', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2493_2266), KL_ARG_V3013_2256])), ([setattr(KL_CTX, 'KL_LOC_V2495_2268', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2493_2266), KL_ARG_V3013_2256])), ([setattr(KL_CTX, 'KL_LOC_A_2269', car(KL_CTX.KL_LOC_V2495_2268)), [setattr(KL_CTX, 'KL_LOC_V2496_2270', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2495_2268), KL_ARG_V3013_2256])), ([setattr(KL_CTX, 'KL_LOC_V2497_2271', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2492_2265), KL_ARG_V3013_2256])), ([setattr(KL_CTX, 'KL_LOC_V2498_2272', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2497_2271), KL_ARG_V3013_2256])), ([setattr(KL_CTX, 'KL_LOC_V2499_2273', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2497_2271), KL_ARG_V3013_2256])), ([setattr(KL_CTX, 'KL_LOC_B_2274', car(KL_CTX.KL_LOC_V2499_2273)), [setattr(KL_CTX, 'KL_LOC_V2500_2275', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2499_2273), KL_ARG_V3013_2256])), ([setattr(KL_CTX, 'KL_LOC_V2501_2276', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2500_2275), KL_ARG_V3013_2256])), ([setattr(KL_CTX, 'KL_LOC_Rest_2277', cdr(KL_CTX.KL_LOC_V2500_2275)), [setattr(KL_CTX, 'KL_LOC_Restx38_2278', tco_apply(shen_newpv, [KL_ARG_V3013_2256])), [setattr(KL_CTX, 'KL_LOC_Restx38x38_2279', tco_apply(shen_newpv, [KL_ARG_V3013_2256])), [setattr(KL_CTX, 'KL_LOC_Rules_2280', tco_apply(shen_newpv, [KL_ARG_V3013_2256])), [setattr(KL_CTX, 'KL_LOC_ListAx38x38_2281', tco_apply(shen_newpv, [KL_ARG_V3013_2256])), [setattr(KL_CTX, 'KL_LOC_Bx38x38_2282', tco_apply(shen_newpv, [KL_ARG_V3013_2256])), [setattr(KL_CTX, 'KL_LOC_Sig_2283', tco_apply(shen_newpv, [KL_ARG_V3013_2256])), [setattr(KL_CTX, 'KL_LOC_Declare_2284', tco_apply(shen_newpv, [KL_ARG_V3013_2256])), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_CTX.KL_LOC_Sig_2283, tco_apply(shen_ue, [Cons(Cons(symdic.symdic_kl_list, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_2269, KL_ARG_V3013_2256]), nil)), Cons(symdic.symdic_kl_x61x61x62, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_2274, KL_ARG_V3013_2256]), nil)))]), KL_ARG_V3013_2256, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_ListAx38x38_2281, car(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Sig_2283, KL_ARG_V3013_2256])), KL_ARG_V3013_2256, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Bx38x38_2282, car(cdr(cdr(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Sig_2283, KL_ARG_V3013_2256])))), KL_ARG_V3013_2256, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Restx38_2278, tco_apply(shen_plugx45wildcards, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Rest_2277, KL_ARG_V3013_2256])]), KL_ARG_V3013_2256, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Restx38x38_2279, tco_apply(shen_ue, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Restx38_2278, KL_ARG_V3013_2256])]), KL_ARG_V3013_2256, (lambda : tail_call(shen_getx45rules, [KL_CTX.KL_LOC_Rules_2280, KL_CTX.KL_LOC_Restx38x38_2279, KL_ARG_V3013_2256, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2258, KL_ARG_V3013_2256, (lambda : tail_call(shen_tcx45rules, [KL_CTX.KL_LOC_F_2262, KL_CTX.KL_LOC_Rules_2280, KL_CTX.KL_LOC_ListAx38x38_2281, KL_CTX.KL_LOC_Bx38x38_2282, Cons(Cons(KL_CTX.KL_LOC_F_2262, Cons(symdic.symdic_kl_x58, Cons(KL_CTX.KL_LOC_Sig_2283, nil))), KL_ARG_V3012_2255), 1, KL_ARG_V3013_2256, (lambda : tail_call(kl_unify, [KL_ARG_V3011_2254, Cons(Cons(symdic.symdic_kl_list, Cons(KL_CTX.KL_LOC_A_2269, nil)), Cons(symdic.symdic_kl_x61x61x62, Cons(KL_CTX.KL_LOC_B_2274, nil))), KL_ARG_V3013_2256, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Declare_2284, apply(kl_declare, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_F_2262, KL_ARG_V3013_2256]), Cons(Cons(symdic.symdic_kl_list, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_2269, KL_ARG_V3013_2256]), nil)), Cons(symdic.symdic_kl_x61x61x62, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_2274, KL_ARG_V3013_2256]), nil)))]), KL_ARG_V3013_2256, KL_ARG_V3014_2257]))]))]))]))]))]))]))]))]))])][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)] if shen_eq(symdic.symdic_kl_x125, KL_CTX.KL_LOC_V2501_2276) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2500_2275) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2499_2273) else False)][(-1)] if shen_eq(symdic.symdic_kl_x61x61x62, KL_CTX.KL_LOC_V2498_2272) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2497_2271) else False)][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2496_2270) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2495_2268) else False)][(-1)] if shen_eq(symdic.symdic_kl_list, KL_CTX.KL_LOC_V2494_2267) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2493_2266) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2492_2265) else False)][(-1)] if shen_eq(symdic.symdic_kl_x123, KL_CTX.KL_LOC_V2491_2264) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2490_2263) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2489_2261) else False)][(-1)] if shen_eq(symdic.symdic_kl_defcc, KL_CTX.KL_LOC_V2488_2260) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2487_2259) else False)][(-1)]])][(-1)]
shen_add_fun('shen.t*-defcc', shen_tx42x45defcc, 5)

@tail_recursion
def shen_plugx45wildcards(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_plugx45wildcards, (FUN_ARGS + lambdaargs)))
    KL_ARG_V3015_2285 = FUN_ARGS[0]
    global symdic
    return (tail_call(kl_map, [symdic.symdic_shen_plugx45wildcards, KL_ARG_V3015_2285]) if shen_consp(KL_ARG_V3015_2285) else (tail_call(kl_gensym, [shen_intern('X')]) if shen_eq(KL_ARG_V3015_2285, symdic.symdic_kl__) else (KL_ARG_V3015_2285 if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.plug-wildcards', shen_plugx45wildcards, 1)

@tail_recursion
def shen_getx45rules(*FUN_ARGS):
    FUN_ARITY = 4
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_getx45rules, (FUN_ARGS + lambdaargs)))
    KL_ARG_V3016_2286 = FUN_ARGS[0]
    KL_ARG_V3017_2287 = FUN_ARGS[1]
    KL_ARG_V3018_2288 = FUN_ARGS[2]
    KL_ARG_V3019_2289 = FUN_ARGS[3]

    class KL_Context:
        KL_LOC_Throwcontrol_2290 = None
        KL_LOC_Case_2291 = None
        KL_LOC_V2480_2292 = None
        KL_LOC_V2481_2293 = None
        KL_LOC_Result_2294 = None
        KL_LOC_V2482_2295 = None
        KL_LOC_V2483_2296 = None
        KL_LOC_Rule_2297 = None
        KL_LOC_Rules_2298 = None
        KL_LOC_Other_2299 = None
        KL_LOC_Rule_2300 = None
        KL_LOC_Rules_2301 = None
        KL_LOC_Result_2302 = None
        KL_LOC_Other_2303 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Throwcontrol_2290', tco_apply(shen_catchpoint, [])), tail_call(shen_cutpoint, [KL_CTX.KL_LOC_Throwcontrol_2290, [setattr(KL_CTX, 'KL_LOC_Case_2291', [setattr(KL_CTX, 'KL_LOC_V2480_2292', tco_apply(shen_lazyderef, [KL_ARG_V3016_2286, KL_ARG_V3018_2288])), ([setattr(KL_CTX, 'KL_LOC_V2481_2293', tco_apply(shen_lazyderef, [KL_ARG_V3017_2287, KL_ARG_V3018_2288])), ([tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2290, KL_ARG_V3018_2288, KL_ARG_V3019_2289])][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2481_2293) else False)][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2480_2292) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2480_2292, nil, KL_ARG_V3018_2288]), [setattr(KL_CTX, 'KL_LOC_Result_2294', [setattr(KL_CTX, 'KL_LOC_V2482_2295', tco_apply(shen_lazyderef, [KL_ARG_V3017_2287, KL_ARG_V3018_2288])), ([tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2290, KL_ARG_V3018_2288, KL_ARG_V3019_2289])][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2482_2295) else False)][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2480_2292, KL_ARG_V3018_2288]), KL_CTX.KL_LOC_Result_2294][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2480_2292]) else False))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_V2483_2296', tco_apply(shen_lazyderef, [KL_ARG_V3016_2286, KL_ARG_V3018_2288])), ([setattr(KL_CTX, 'KL_LOC_Rule_2297', car(KL_CTX.KL_LOC_V2483_2296)), [setattr(KL_CTX, 'KL_LOC_Rules_2298', cdr(KL_CTX.KL_LOC_V2483_2296)), [setattr(KL_CTX, 'KL_LOC_Other_2299', tco_apply(shen_newpv, [KL_ARG_V3018_2288])), [tco_apply(shen_incinfs, []), tco_apply(shen_firstx45rule, [KL_ARG_V3017_2287, KL_CTX.KL_LOC_Rule_2297, KL_CTX.KL_LOC_Other_2299, KL_ARG_V3018_2288, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2290, KL_ARG_V3018_2288, (lambda : tail_call(shen_getx45rules, [KL_CTX.KL_LOC_Rules_2298, KL_CTX.KL_LOC_Other_2299, KL_ARG_V3018_2288, KL_ARG_V3019_2289]))]))])][(-1)]][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2483_2296) else ([setattr(KL_CTX, 'KL_LOC_Rule_2300', tco_apply(shen_newpv, [KL_ARG_V3018_2288])), [setattr(KL_CTX, 'KL_LOC_Rules_2301', tco_apply(shen_newpv, [KL_ARG_V3018_2288])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2483_2296, Cons(KL_CTX.KL_LOC_Rule_2300, KL_CTX.KL_LOC_Rules_2301), KL_ARG_V3018_2288]), [setattr(KL_CTX, 'KL_LOC_Result_2302', [setattr(KL_CTX, 'KL_LOC_Other_2303', tco_apply(shen_newpv, [KL_ARG_V3018_2288])), [tco_apply(shen_incinfs, []), tco_apply(shen_firstx45rule, [KL_ARG_V3017_2287, KL_CTX.KL_LOC_Rule_2300, KL_CTX.KL_LOC_Other_2303, KL_ARG_V3018_2288, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2290, KL_ARG_V3018_2288, (lambda : tail_call(shen_getx45rules, [KL_CTX.KL_LOC_Rules_2301, KL_CTX.KL_LOC_Other_2303, KL_ARG_V3018_2288, KL_ARG_V3019_2289]))]))])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2483_2296, KL_ARG_V3018_2288]), KL_CTX.KL_LOC_Result_2302][(-1)]][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2483_2296]) else False))][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2291, False) else KL_CTX.KL_LOC_Case_2291)][(-1)]])][(-1)]
shen_add_fun('shen.get-rules', shen_getx45rules, 4)

@tail_recursion
def shen_firstx45rule(*FUN_ARGS):
    FUN_ARITY = 5
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_firstx45rule, (FUN_ARGS + lambdaargs)))
    KL_ARG_V3020_2304 = FUN_ARGS[0]
    KL_ARG_V3021_2305 = FUN_ARGS[1]
    KL_ARG_V3022_2306 = FUN_ARGS[2]
    KL_ARG_V3023_2307 = FUN_ARGS[3]
    KL_ARG_V3024_2308 = FUN_ARGS[4]

    class KL_Context:
        KL_LOC_Throwcontrol_2309 = None
        KL_LOC_Case_2310 = None
        KL_LOC_V2473_2311 = None
        KL_LOC_V2474_2312 = None
        KL_LOC_Other2468_2313 = None
        KL_LOC_V2475_2314 = None
        KL_LOC_Result_2315 = None
        KL_LOC_V2476_2316 = None
        KL_LOC_X2469_2317 = None
        KL_LOC_Rest_2318 = None
        KL_LOC_V2477_2319 = None
        KL_LOC_X_2320 = None
        KL_LOC_Rule_2321 = None
        KL_LOC_X_2322 = None
        KL_LOC_Rule_2323 = None
        KL_LOC_Result_2324 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Throwcontrol_2309', tco_apply(shen_catchpoint, [])), tail_call(shen_cutpoint, [KL_CTX.KL_LOC_Throwcontrol_2309, [setattr(KL_CTX, 'KL_LOC_Case_2310', [setattr(KL_CTX, 'KL_LOC_V2473_2311', tco_apply(shen_lazyderef, [KL_ARG_V3020_2304, KL_ARG_V3023_2307])), ([setattr(KL_CTX, 'KL_LOC_V2474_2312', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2473_2311), KL_ARG_V3023_2307])), ([setattr(KL_CTX, 'KL_LOC_Other2468_2313', cdr(KL_CTX.KL_LOC_V2473_2311)), [setattr(KL_CTX, 'KL_LOC_V2475_2314', tco_apply(shen_lazyderef, [KL_ARG_V3021_2305, KL_ARG_V3023_2307])), ([tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_ARG_V3022_2306, KL_CTX.KL_LOC_Other2468_2313, KL_ARG_V3023_2307, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2309, KL_ARG_V3023_2307, KL_ARG_V3024_2308]))])][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2475_2314) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2475_2314, nil, KL_ARG_V3023_2307]), [setattr(KL_CTX, 'KL_LOC_Result_2315', [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_ARG_V3022_2306, KL_CTX.KL_LOC_Other2468_2313, KL_ARG_V3023_2307, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2309, KL_ARG_V3023_2307, KL_ARG_V3024_2308]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2475_2314, KL_ARG_V3023_2307]), KL_CTX.KL_LOC_Result_2315][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2475_2314]) else False))][(-1)]][(-1)] if shen_eq(symdic.symdic_kl_x59, KL_CTX.KL_LOC_V2474_2312) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2473_2311) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_V2476_2316', tco_apply(shen_lazyderef, [KL_ARG_V3020_2304, KL_ARG_V3023_2307])), ([setattr(KL_CTX, 'KL_LOC_X2469_2317', car(KL_CTX.KL_LOC_V2476_2316)), [setattr(KL_CTX, 'KL_LOC_Rest_2318', cdr(KL_CTX.KL_LOC_V2476_2316)), [setattr(KL_CTX, 'KL_LOC_V2477_2319', tco_apply(shen_lazyderef, [KL_ARG_V3021_2305, KL_ARG_V3023_2307])), ([setattr(KL_CTX, 'KL_LOC_X_2320', car(KL_CTX.KL_LOC_V2477_2319)), [setattr(KL_CTX, 'KL_LOC_Rule_2321', cdr(KL_CTX.KL_LOC_V2477_2319)), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_X_2320, KL_CTX.KL_LOC_X2469_2317, KL_ARG_V3023_2307, (lambda : tail_call(shen_firstx45rule, [KL_CTX.KL_LOC_Rest_2318, KL_CTX.KL_LOC_Rule_2321, KL_ARG_V3022_2306, KL_ARG_V3023_2307, KL_ARG_V3024_2308]))])][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2477_2319) else ([setattr(KL_CTX, 'KL_LOC_X_2322', tco_apply(shen_newpv, [KL_ARG_V3023_2307])), [setattr(KL_CTX, 'KL_LOC_Rule_2323', tco_apply(shen_newpv, [KL_ARG_V3023_2307])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2477_2319, Cons(KL_CTX.KL_LOC_X_2322, KL_CTX.KL_LOC_Rule_2323), KL_ARG_V3023_2307]), [setattr(KL_CTX, 'KL_LOC_Result_2324', [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_X_2322, KL_CTX.KL_LOC_X2469_2317, KL_ARG_V3023_2307, (lambda : tail_call(shen_firstx45rule, [KL_CTX.KL_LOC_Rest_2318, KL_CTX.KL_LOC_Rule_2323, KL_ARG_V3022_2306, KL_ARG_V3023_2307, KL_ARG_V3024_2308]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2477_2319, KL_ARG_V3023_2307]), KL_CTX.KL_LOC_Result_2324][(-1)]][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2477_2319]) else False))][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2476_2316) else False)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2310, False) else KL_CTX.KL_LOC_Case_2310)][(-1)]])][(-1)]
shen_add_fun('shen.first-rule', shen_firstx45rule, 5)

@tail_recursion
def shen_tcx45rules(*FUN_ARGS):
    FUN_ARITY = 8
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_tcx45rules, (FUN_ARGS + lambdaargs)))
    KL_ARG_V3025_2325 = FUN_ARGS[0]
    KL_ARG_V3026_2326 = FUN_ARGS[1]
    KL_ARG_V3027_2327 = FUN_ARGS[2]
    KL_ARG_V3028_2328 = FUN_ARGS[3]
    KL_ARG_V3029_2329 = FUN_ARGS[4]
    KL_ARG_V3030_2330 = FUN_ARGS[5]
    KL_ARG_V3031_2331 = FUN_ARGS[6]
    KL_ARG_V3032_2332 = FUN_ARGS[7]

    class KL_Context:
        KL_LOC_Throwcontrol_2333 = None
        KL_LOC_Case_2334 = None
        KL_LOC_V2462_2335 = None
        KL_LOC_V2463_2336 = None
        KL_LOC_Rule_2337 = None
        KL_LOC_Rules_2338 = None
        KL_LOC_V2464_2339 = None
        KL_LOC_V2465_2340 = None
        KL_LOC_V2466_2341 = None
        KL_LOC_A_2342 = None
        KL_LOC_V2467_2343 = None
        KL_LOC_M_2344 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Throwcontrol_2333', tco_apply(shen_catchpoint, [])), tail_call(shen_cutpoint, [KL_CTX.KL_LOC_Throwcontrol_2333, [setattr(KL_CTX, 'KL_LOC_Case_2334', [setattr(KL_CTX, 'KL_LOC_V2462_2335', tco_apply(shen_lazyderef, [KL_ARG_V3026_2326, KL_ARG_V3031_2331])), ([tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V3032_2332])][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2462_2335) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_V2463_2336', tco_apply(shen_lazyderef, [KL_ARG_V3026_2326, KL_ARG_V3031_2331])), ([setattr(KL_CTX, 'KL_LOC_Rule_2337', car(KL_CTX.KL_LOC_V2463_2336)), [setattr(KL_CTX, 'KL_LOC_Rules_2338', cdr(KL_CTX.KL_LOC_V2463_2336)), [setattr(KL_CTX, 'KL_LOC_V2464_2339', tco_apply(shen_lazyderef, [KL_ARG_V3027_2327, KL_ARG_V3031_2331])), ([setattr(KL_CTX, 'KL_LOC_V2465_2340', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2464_2339), KL_ARG_V3031_2331])), ([setattr(KL_CTX, 'KL_LOC_V2466_2341', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2464_2339), KL_ARG_V3031_2331])), ([setattr(KL_CTX, 'KL_LOC_A_2342', car(KL_CTX.KL_LOC_V2466_2341)), [setattr(KL_CTX, 'KL_LOC_V2467_2343', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2466_2341), KL_ARG_V3031_2331])), ([setattr(KL_CTX, 'KL_LOC_M_2344', tco_apply(shen_newpv, [KL_ARG_V3031_2331])), [tco_apply(shen_incinfs, []), tco_apply(shen_tcx45rule, [KL_ARG_V3025_2325, KL_CTX.KL_LOC_Rule_2337, KL_CTX.KL_LOC_A_2342, KL_ARG_V3028_2328, KL_ARG_V3029_2329, KL_ARG_V3030_2330, KL_ARG_V3031_2331, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_M_2344, (tco_apply(shen_deref, [KL_ARG_V3030_2330, KL_ARG_V3031_2331]) + 1), KL_ARG_V3031_2331, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2333, KL_ARG_V3031_2331, (lambda : tail_call(shen_tcx45rules, [KL_ARG_V3025_2325, KL_CTX.KL_LOC_Rules_2338, Cons(symdic.symdic_kl_list, Cons(KL_CTX.KL_LOC_A_2342, nil)), KL_ARG_V3028_2328, KL_ARG_V3029_2329, KL_CTX.KL_LOC_M_2344, KL_ARG_V3031_2331, KL_ARG_V3032_2332]))]))]))])][(-1)]][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2467_2343) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2466_2341) else False)][(-1)] if shen_eq(symdic.symdic_kl_list, KL_CTX.KL_LOC_V2465_2340) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2464_2339) else False)][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2463_2336) else False)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2334, False) else KL_CTX.KL_LOC_Case_2334)][(-1)]])][(-1)]
shen_add_fun('shen.tc-rules', shen_tcx45rules, 8)

@tail_recursion
def shen_tcx45rule(*FUN_ARGS):
    FUN_ARITY = 8
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_tcx45rule, (FUN_ARGS + lambdaargs)))
    KL_ARG_V3033_2345 = FUN_ARGS[0]
    KL_ARG_V3034_2346 = FUN_ARGS[1]
    KL_ARG_V3035_2347 = FUN_ARGS[2]
    KL_ARG_V3036_2348 = FUN_ARGS[3]
    KL_ARG_V3037_2349 = FUN_ARGS[4]
    KL_ARG_V3038_2350 = FUN_ARGS[5]
    KL_ARG_V3039_2351 = FUN_ARGS[6]
    KL_ARG_V3040_2352 = FUN_ARGS[7]

    class KL_Context:
        KL_LOC_Case_2353 = None
        KL_LOC_Err_2354 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Case_2353', [tco_apply(shen_incinfs, []), tco_apply(shen_checkx45defccx45rule, [KL_ARG_V3034_2346, KL_ARG_V3035_2347, KL_ARG_V3036_2348, KL_ARG_V3037_2349, KL_ARG_V3039_2351, KL_ARG_V3040_2352])][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Err_2354', tco_apply(shen_newpv, [KL_ARG_V3039_2351])), [tco_apply(shen_incinfs, []), tail_call(kl_bind, [KL_CTX.KL_LOC_Err_2354, shen_simple_error(('type error in rule ' + tco_apply(shen_app, [tco_apply(shen_lazyderef, [KL_ARG_V3038_2350, KL_ARG_V3039_2351]), (' of ' + tco_apply(shen_app, [tco_apply(shen_lazyderef, [KL_ARG_V3033_2345, KL_ARG_V3039_2351]), '', symdic.symdic_shen_a])), symdic.symdic_shen_a]))), KL_ARG_V3039_2351, KL_ARG_V3040_2352])][(-1)]][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2353, False) else KL_CTX.KL_LOC_Case_2353)][(-1)]
shen_add_fun('shen.tc-rule', shen_tcx45rule, 8)

@tail_recursion
def shen_checkx45defccx45rule(*FUN_ARGS):
    FUN_ARITY = 6
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_checkx45defccx45rule, (FUN_ARGS + lambdaargs)))
    KL_ARG_V3041_2355 = FUN_ARGS[0]
    KL_ARG_V3042_2356 = FUN_ARGS[1]
    KL_ARG_V3043_2357 = FUN_ARGS[2]
    KL_ARG_V3044_2358 = FUN_ARGS[3]
    KL_ARG_V3045_2359 = FUN_ARGS[4]
    KL_ARG_V3046_2360 = FUN_ARGS[5]

    class KL_Context:
        KL_LOC_Throwcontrol_2361 = None
        KL_LOC_Syntax_2362 = None
        KL_LOC_Semantics_2363 = None
        KL_LOC_SynHyps_2364 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Throwcontrol_2361', tco_apply(shen_catchpoint, [])), tail_call(shen_cutpoint, [KL_CTX.KL_LOC_Throwcontrol_2361, [setattr(KL_CTX, 'KL_LOC_Syntax_2362', tco_apply(shen_newpv, [KL_ARG_V3045_2359])), [setattr(KL_CTX, 'KL_LOC_Semantics_2363', tco_apply(shen_newpv, [KL_ARG_V3045_2359])), [setattr(KL_CTX, 'KL_LOC_SynHyps_2364', tco_apply(shen_newpv, [KL_ARG_V3045_2359])), [tco_apply(shen_incinfs, []), tco_apply(shen_getx45syntaxx43semantics, [KL_CTX.KL_LOC_Syntax_2362, KL_CTX.KL_LOC_Semantics_2363, KL_ARG_V3041_2355, KL_ARG_V3045_2359, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2361, KL_ARG_V3045_2359, (lambda : tail_call(shen_syntaxx45hyps, [KL_CTX.KL_LOC_Syntax_2362, KL_ARG_V3044_2358, KL_CTX.KL_LOC_SynHyps_2364, KL_ARG_V3042_2356, KL_ARG_V3045_2359, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2361, KL_ARG_V3045_2359, (lambda : tail_call(shen_syntaxx45check, [KL_CTX.KL_LOC_Syntax_2362, KL_ARG_V3042_2356, KL_CTX.KL_LOC_SynHyps_2364, KL_ARG_V3045_2359, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2361, KL_ARG_V3045_2359, (lambda : tail_call(shen_semanticsx45check, [KL_CTX.KL_LOC_Semantics_2363, KL_ARG_V3043_2357, KL_CTX.KL_LOC_SynHyps_2364, KL_ARG_V3045_2359, KL_ARG_V3046_2360]))]))]))]))]))]))])][(-1)]][(-1)]][(-1)]][(-1)]])][(-1)]
shen_add_fun('shen.check-defcc-rule', shen_checkx45defccx45rule, 6)

@tail_recursion
def shen_syntaxx45hyps(*FUN_ARGS):
    FUN_ARITY = 6
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_syntaxx45hyps, (FUN_ARGS + lambdaargs)))
    KL_ARG_V3047_2365 = FUN_ARGS[0]
    KL_ARG_V3048_2366 = FUN_ARGS[1]
    KL_ARG_V3049_2367 = FUN_ARGS[2]
    KL_ARG_V3050_2368 = FUN_ARGS[3]
    KL_ARG_V3051_2369 = FUN_ARGS[4]
    KL_ARG_V3052_2370 = FUN_ARGS[5]

    class KL_Context:
        KL_LOC_Throwcontrol_2371 = None
        KL_LOC_Case_2372 = None
        KL_LOC_V2435_2373 = None
        KL_LOC_Case_2374 = None
        KL_LOC_V2436_2375 = None
        KL_LOC_X2429_2376 = None
        KL_LOC_Y_2377 = None
        KL_LOC_V2437_2378 = None
        KL_LOC_V2438_2379 = None
        KL_LOC_X_2380 = None
        KL_LOC_V2439_2381 = None
        KL_LOC_V2440_2382 = None
        KL_LOC_V2441_2383 = None
        KL_LOC_A2430_2384 = None
        KL_LOC_V2442_2385 = None
        KL_LOC_SynHyps_2386 = None
        KL_LOC_Result_2387 = None
        KL_LOC_SynHyps_2388 = None
        KL_LOC_A2430_2389 = None
        KL_LOC_Result_2390 = None
        KL_LOC_SynHyps_2391 = None
        KL_LOC_Result_2392 = None
        KL_LOC_V2443_2393 = None
        KL_LOC_A2430_2394 = None
        KL_LOC_V2444_2395 = None
        KL_LOC_SynHyps_2396 = None
        KL_LOC_Result_2397 = None
        KL_LOC_SynHyps_2398 = None
        KL_LOC_A2430_2399 = None
        KL_LOC_Result_2400 = None
        KL_LOC_SynHyps_2401 = None
        KL_LOC_A2430_2402 = None
        KL_LOC_Result_2403 = None
        KL_LOC_SynHyps_2404 = None
        KL_LOC_X_2405 = None
        KL_LOC_A2430_2406 = None
        KL_LOC_Result_2407 = None
        KL_LOC_SynHyps_2408 = None
        KL_LOC_X_2409 = None
        KL_LOC_A2430_2410 = None
        KL_LOC_SynHyps_2411 = None
        KL_LOC_Result_2412 = None
        KL_LOC_V2445_2413 = None
        KL_LOC_Y_2414 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Throwcontrol_2371', tco_apply(shen_catchpoint, [])), tail_call(shen_cutpoint, [KL_CTX.KL_LOC_Throwcontrol_2371, [setattr(KL_CTX, 'KL_LOC_Case_2372', [setattr(KL_CTX, 'KL_LOC_V2435_2373', tco_apply(shen_lazyderef, [KL_ARG_V3047_2365, KL_ARG_V3051_2369])), ([tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_ARG_V3049_2367, KL_ARG_V3048_2366, KL_ARG_V3051_2369, KL_ARG_V3052_2370])][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2435_2373) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_2374', [setattr(KL_CTX, 'KL_LOC_V2436_2375', tco_apply(shen_lazyderef, [KL_ARG_V3047_2365, KL_ARG_V3051_2369])), ([setattr(KL_CTX, 'KL_LOC_X2429_2376', car(KL_CTX.KL_LOC_V2436_2375)), [setattr(KL_CTX, 'KL_LOC_Y_2377', cdr(KL_CTX.KL_LOC_V2436_2375)), [setattr(KL_CTX, 'KL_LOC_V2437_2378', tco_apply(shen_lazyderef, [KL_ARG_V3049_2367, KL_ARG_V3051_2369])), ([setattr(KL_CTX, 'KL_LOC_V2438_2379', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2437_2378), KL_ARG_V3051_2369])), ([setattr(KL_CTX, 'KL_LOC_X_2380', car(KL_CTX.KL_LOC_V2438_2379)), [setattr(KL_CTX, 'KL_LOC_V2439_2381', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2438_2379), KL_ARG_V3051_2369])), ([setattr(KL_CTX, 'KL_LOC_V2440_2382', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2439_2381), KL_ARG_V3051_2369])), ([setattr(KL_CTX, 'KL_LOC_V2441_2383', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2439_2381), KL_ARG_V3051_2369])), ([setattr(KL_CTX, 'KL_LOC_A2430_2384', car(KL_CTX.KL_LOC_V2441_2383)), [setattr(KL_CTX, 'KL_LOC_V2442_2385', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2441_2383), KL_ARG_V3051_2369])), ([setattr(KL_CTX, 'KL_LOC_SynHyps_2386', cdr(KL_CTX.KL_LOC_V2437_2378)), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_ARG_V3050_2368, KL_CTX.KL_LOC_A2430_2384, KL_ARG_V3051_2369, (lambda : tail_call(kl_unifyx33, [KL_CTX.KL_LOC_X_2380, KL_CTX.KL_LOC_X2429_2376, KL_ARG_V3051_2369, (lambda : tail_call(kl_fwhen, [tco_apply(shen_uex63, [tco_apply(shen_deref, [KL_CTX.KL_LOC_X_2380, KL_ARG_V3051_2369])]), KL_ARG_V3051_2369, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2371, KL_ARG_V3051_2369, (lambda : tail_call(shen_syntaxx45hyps, [KL_CTX.KL_LOC_Y_2377, KL_ARG_V3048_2366, KL_CTX.KL_LOC_SynHyps_2386, KL_ARG_V3050_2368, KL_ARG_V3051_2369, KL_ARG_V3052_2370]))]))]))]))])][(-1)]][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2442_2385) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2442_2385, nil, KL_ARG_V3051_2369]), [setattr(KL_CTX, 'KL_LOC_Result_2387', [setattr(KL_CTX, 'KL_LOC_SynHyps_2388', cdr(KL_CTX.KL_LOC_V2437_2378)), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_ARG_V3050_2368, KL_CTX.KL_LOC_A2430_2384, KL_ARG_V3051_2369, (lambda : tail_call(kl_unifyx33, [KL_CTX.KL_LOC_X_2380, KL_CTX.KL_LOC_X2429_2376, KL_ARG_V3051_2369, (lambda : tail_call(kl_fwhen, [tco_apply(shen_uex63, [tco_apply(shen_deref, [KL_CTX.KL_LOC_X_2380, KL_ARG_V3051_2369])]), KL_ARG_V3051_2369, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2371, KL_ARG_V3051_2369, (lambda : tail_call(shen_syntaxx45hyps, [KL_CTX.KL_LOC_Y_2377, KL_ARG_V3048_2366, KL_CTX.KL_LOC_SynHyps_2388, KL_ARG_V3050_2368, KL_ARG_V3051_2369, KL_ARG_V3052_2370]))]))]))]))])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2442_2385, KL_ARG_V3051_2369]), KL_CTX.KL_LOC_Result_2387][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2442_2385]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2441_2383) else ([setattr(KL_CTX, 'KL_LOC_A2430_2389', tco_apply(shen_newpv, [KL_ARG_V3051_2369])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2441_2383, Cons(KL_CTX.KL_LOC_A2430_2389, nil), KL_ARG_V3051_2369]), [setattr(KL_CTX, 'KL_LOC_Result_2390', [setattr(KL_CTX, 'KL_LOC_SynHyps_2391', cdr(KL_CTX.KL_LOC_V2437_2378)), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_ARG_V3050_2368, KL_CTX.KL_LOC_A2430_2389, KL_ARG_V3051_2369, (lambda : tail_call(kl_unifyx33, [KL_CTX.KL_LOC_X_2380, KL_CTX.KL_LOC_X2429_2376, KL_ARG_V3051_2369, (lambda : tail_call(kl_fwhen, [tco_apply(shen_uex63, [tco_apply(shen_deref, [KL_CTX.KL_LOC_X_2380, KL_ARG_V3051_2369])]), KL_ARG_V3051_2369, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2371, KL_ARG_V3051_2369, (lambda : tail_call(shen_syntaxx45hyps, [KL_CTX.KL_LOC_Y_2377, KL_ARG_V3048_2366, KL_CTX.KL_LOC_SynHyps_2391, KL_ARG_V3050_2368, KL_ARG_V3051_2369, KL_ARG_V3052_2370]))]))]))]))])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2441_2383, KL_ARG_V3051_2369]), KL_CTX.KL_LOC_Result_2390][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2441_2383]) else False))][(-1)] if shen_eq(symdic.symdic_kl_x58, KL_CTX.KL_LOC_V2440_2382) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2440_2382, symdic.symdic_kl_x58, KL_ARG_V3051_2369]), [setattr(KL_CTX, 'KL_LOC_Result_2392', [setattr(KL_CTX, 'KL_LOC_V2443_2393', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2439_2381), KL_ARG_V3051_2369])), ([setattr(KL_CTX, 'KL_LOC_A2430_2394', car(KL_CTX.KL_LOC_V2443_2393)), [setattr(KL_CTX, 'KL_LOC_V2444_2395', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2443_2393), KL_ARG_V3051_2369])), ([setattr(KL_CTX, 'KL_LOC_SynHyps_2396', cdr(KL_CTX.KL_LOC_V2437_2378)), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_ARG_V3050_2368, KL_CTX.KL_LOC_A2430_2394, KL_ARG_V3051_2369, (lambda : tail_call(kl_unifyx33, [KL_CTX.KL_LOC_X_2380, KL_CTX.KL_LOC_X2429_2376, KL_ARG_V3051_2369, (lambda : tail_call(kl_fwhen, [tco_apply(shen_uex63, [tco_apply(shen_deref, [KL_CTX.KL_LOC_X_2380, KL_ARG_V3051_2369])]), KL_ARG_V3051_2369, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2371, KL_ARG_V3051_2369, (lambda : tail_call(shen_syntaxx45hyps, [KL_CTX.KL_LOC_Y_2377, KL_ARG_V3048_2366, KL_CTX.KL_LOC_SynHyps_2396, KL_ARG_V3050_2368, KL_ARG_V3051_2369, KL_ARG_V3052_2370]))]))]))]))])][(-1)]][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2444_2395) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2444_2395, nil, KL_ARG_V3051_2369]), [setattr(KL_CTX, 'KL_LOC_Result_2397', [setattr(KL_CTX, 'KL_LOC_SynHyps_2398', cdr(KL_CTX.KL_LOC_V2437_2378)), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_ARG_V3050_2368, KL_CTX.KL_LOC_A2430_2394, KL_ARG_V3051_2369, (lambda : tail_call(kl_unifyx33, [KL_CTX.KL_LOC_X_2380, KL_CTX.KL_LOC_X2429_2376, KL_ARG_V3051_2369, (lambda : tail_call(kl_fwhen, [tco_apply(shen_uex63, [tco_apply(shen_deref, [KL_CTX.KL_LOC_X_2380, KL_ARG_V3051_2369])]), KL_ARG_V3051_2369, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2371, KL_ARG_V3051_2369, (lambda : tail_call(shen_syntaxx45hyps, [KL_CTX.KL_LOC_Y_2377, KL_ARG_V3048_2366, KL_CTX.KL_LOC_SynHyps_2398, KL_ARG_V3050_2368, KL_ARG_V3051_2369, KL_ARG_V3052_2370]))]))]))]))])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2444_2395, KL_ARG_V3051_2369]), KL_CTX.KL_LOC_Result_2397][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2444_2395]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2443_2393) else ([setattr(KL_CTX, 'KL_LOC_A2430_2399', tco_apply(shen_newpv, [KL_ARG_V3051_2369])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2443_2393, Cons(KL_CTX.KL_LOC_A2430_2399, nil), KL_ARG_V3051_2369]), [setattr(KL_CTX, 'KL_LOC_Result_2400', [setattr(KL_CTX, 'KL_LOC_SynHyps_2401', cdr(KL_CTX.KL_LOC_V2437_2378)), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_ARG_V3050_2368, KL_CTX.KL_LOC_A2430_2399, KL_ARG_V3051_2369, (lambda : tail_call(kl_unifyx33, [KL_CTX.KL_LOC_X_2380, KL_CTX.KL_LOC_X2429_2376, KL_ARG_V3051_2369, (lambda : tail_call(kl_fwhen, [tco_apply(shen_uex63, [tco_apply(shen_deref, [KL_CTX.KL_LOC_X_2380, KL_ARG_V3051_2369])]), KL_ARG_V3051_2369, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2371, KL_ARG_V3051_2369, (lambda : tail_call(shen_syntaxx45hyps, [KL_CTX.KL_LOC_Y_2377, KL_ARG_V3048_2366, KL_CTX.KL_LOC_SynHyps_2401, KL_ARG_V3050_2368, KL_ARG_V3051_2369, KL_ARG_V3052_2370]))]))]))]))])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2443_2393, KL_ARG_V3051_2369]), KL_CTX.KL_LOC_Result_2400][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2443_2393]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2440_2382, KL_ARG_V3051_2369]), KL_CTX.KL_LOC_Result_2392][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2440_2382]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2439_2381) else ([setattr(KL_CTX, 'KL_LOC_A2430_2402', tco_apply(shen_newpv, [KL_ARG_V3051_2369])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2439_2381, Cons(symdic.symdic_kl_x58, Cons(KL_CTX.KL_LOC_A2430_2402, nil)), KL_ARG_V3051_2369]), [setattr(KL_CTX, 'KL_LOC_Result_2403', [setattr(KL_CTX, 'KL_LOC_SynHyps_2404', cdr(KL_CTX.KL_LOC_V2437_2378)), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_ARG_V3050_2368, KL_CTX.KL_LOC_A2430_2402, KL_ARG_V3051_2369, (lambda : tail_call(kl_unifyx33, [KL_CTX.KL_LOC_X_2380, KL_CTX.KL_LOC_X2429_2376, KL_ARG_V3051_2369, (lambda : tail_call(kl_fwhen, [tco_apply(shen_uex63, [tco_apply(shen_deref, [KL_CTX.KL_LOC_X_2380, KL_ARG_V3051_2369])]), KL_ARG_V3051_2369, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2371, KL_ARG_V3051_2369, (lambda : tail_call(shen_syntaxx45hyps, [KL_CTX.KL_LOC_Y_2377, KL_ARG_V3048_2366, KL_CTX.KL_LOC_SynHyps_2404, KL_ARG_V3050_2368, KL_ARG_V3051_2369, KL_ARG_V3052_2370]))]))]))]))])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2439_2381, KL_ARG_V3051_2369]), KL_CTX.KL_LOC_Result_2403][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2439_2381]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2438_2379) else ([setattr(KL_CTX, 'KL_LOC_X_2405', tco_apply(shen_newpv, [KL_ARG_V3051_2369])), [setattr(KL_CTX, 'KL_LOC_A2430_2406', tco_apply(shen_newpv, [KL_ARG_V3051_2369])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2438_2379, Cons(KL_CTX.KL_LOC_X_2405, Cons(symdic.symdic_kl_x58, Cons(KL_CTX.KL_LOC_A2430_2406, nil))), KL_ARG_V3051_2369]), [setattr(KL_CTX, 'KL_LOC_Result_2407', [setattr(KL_CTX, 'KL_LOC_SynHyps_2408', cdr(KL_CTX.KL_LOC_V2437_2378)), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_ARG_V3050_2368, KL_CTX.KL_LOC_A2430_2406, KL_ARG_V3051_2369, (lambda : tail_call(kl_unifyx33, [KL_CTX.KL_LOC_X_2405, KL_CTX.KL_LOC_X2429_2376, KL_ARG_V3051_2369, (lambda : tail_call(kl_fwhen, [tco_apply(shen_uex63, [tco_apply(shen_deref, [KL_CTX.KL_LOC_X_2405, KL_ARG_V3051_2369])]), KL_ARG_V3051_2369, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2371, KL_ARG_V3051_2369, (lambda : tail_call(shen_syntaxx45hyps, [KL_CTX.KL_LOC_Y_2377, KL_ARG_V3048_2366, KL_CTX.KL_LOC_SynHyps_2408, KL_ARG_V3050_2368, KL_ARG_V3051_2369, KL_ARG_V3052_2370]))]))]))]))])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2438_2379, KL_ARG_V3051_2369]), KL_CTX.KL_LOC_Result_2407][(-1)]][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2438_2379]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2437_2378) else ([setattr(KL_CTX, 'KL_LOC_X_2409', tco_apply(shen_newpv, [KL_ARG_V3051_2369])), [setattr(KL_CTX, 'KL_LOC_A2430_2410', tco_apply(shen_newpv, [KL_ARG_V3051_2369])), [setattr(KL_CTX, 'KL_LOC_SynHyps_2411', tco_apply(shen_newpv, [KL_ARG_V3051_2369])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2437_2378, Cons(Cons(KL_CTX.KL_LOC_X_2409, Cons(symdic.symdic_kl_x58, Cons(KL_CTX.KL_LOC_A2430_2410, nil))), KL_CTX.KL_LOC_SynHyps_2411), KL_ARG_V3051_2369]), [setattr(KL_CTX, 'KL_LOC_Result_2412', [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_ARG_V3050_2368, KL_CTX.KL_LOC_A2430_2410, KL_ARG_V3051_2369, (lambda : tail_call(kl_unifyx33, [KL_CTX.KL_LOC_X_2409, KL_CTX.KL_LOC_X2429_2376, KL_ARG_V3051_2369, (lambda : tail_call(kl_fwhen, [tco_apply(shen_uex63, [tco_apply(shen_deref, [KL_CTX.KL_LOC_X_2409, KL_ARG_V3051_2369])]), KL_ARG_V3051_2369, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2371, KL_ARG_V3051_2369, (lambda : tail_call(shen_syntaxx45hyps, [KL_CTX.KL_LOC_Y_2377, KL_ARG_V3048_2366, KL_CTX.KL_LOC_SynHyps_2411, KL_ARG_V3050_2368, KL_ARG_V3051_2369, KL_ARG_V3052_2370]))]))]))]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2437_2378, KL_ARG_V3051_2369]), KL_CTX.KL_LOC_Result_2412][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2437_2378]) else False))][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2436_2375) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_V2445_2413', tco_apply(shen_lazyderef, [KL_ARG_V3047_2365, KL_ARG_V3051_2369])), ([setattr(KL_CTX, 'KL_LOC_Y_2414', cdr(KL_CTX.KL_LOC_V2445_2413)), [tco_apply(shen_incinfs, []), tco_apply(shen_syntaxx45hyps, [KL_CTX.KL_LOC_Y_2414, KL_ARG_V3048_2366, KL_ARG_V3049_2367, KL_ARG_V3050_2368, KL_ARG_V3051_2369, KL_ARG_V3052_2370])][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2445_2413) else False)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2374, False) else KL_CTX.KL_LOC_Case_2374)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2372, False) else KL_CTX.KL_LOC_Case_2372)][(-1)]])][(-1)]
shen_add_fun('shen.syntax-hyps', shen_syntaxx45hyps, 6)

@tail_recursion
def shen_getx45syntaxx43semantics(*FUN_ARGS):
    FUN_ARITY = 5
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_getx45syntaxx43semantics, (FUN_ARGS + lambdaargs)))
    KL_ARG_V3053_2415 = FUN_ARGS[0]
    KL_ARG_V3054_2416 = FUN_ARGS[1]
    KL_ARG_V3055_2417 = FUN_ARGS[2]
    KL_ARG_V3056_2418 = FUN_ARGS[3]
    KL_ARG_V3057_2419 = FUN_ARGS[4]

    class KL_Context:
        KL_LOC_Throwcontrol_2420 = None
        KL_LOC_Case_2421 = None
        KL_LOC_V2401_2422 = None
        KL_LOC_V2402_2423 = None
        KL_LOC_V2403_2424 = None
        KL_LOC_V2404_2425 = None
        KL_LOC_Semantics_2426 = None
        KL_LOC_V2405_2427 = None
        KL_LOC_Result_2428 = None
        KL_LOC_V2406_2429 = None
        KL_LOC_V2407_2430 = None
        KL_LOC_V2408_2431 = None
        KL_LOC_Semantics_2432 = None
        KL_LOC_V2409_2433 = None
        KL_LOC_Case_2434 = None
        KL_LOC_V2410_2435 = None
        KL_LOC_V2411_2436 = None
        KL_LOC_V2412_2437 = None
        KL_LOC_V2413_2438 = None
        KL_LOC_Semantics_2439 = None
        KL_LOC_V2414_2440 = None
        KL_LOC_V2415_2441 = None
        KL_LOC_V2416_2442 = None
        KL_LOC_G_2443 = None
        KL_LOC_V2417_2444 = None
        KL_LOC_Result_2445 = None
        KL_LOC_V2418_2446 = None
        KL_LOC_V2419_2447 = None
        KL_LOC_V2420_2448 = None
        KL_LOC_Semantics_2449 = None
        KL_LOC_V2421_2450 = None
        KL_LOC_V2422_2451 = None
        KL_LOC_V2423_2452 = None
        KL_LOC_G_2453 = None
        KL_LOC_V2424_2454 = None
        KL_LOC_V2425_2455 = None
        KL_LOC_X2397_2456 = None
        KL_LOC_Syntax_2457 = None
        KL_LOC_V2426_2458 = None
        KL_LOC_X_2459 = None
        KL_LOC_Rule_2460 = None
        KL_LOC_X2397_2461 = None
        KL_LOC_Syntax_2462 = None
        KL_LOC_Result_2463 = None
        KL_LOC_V2427_2464 = None
        KL_LOC_X_2465 = None
        KL_LOC_Rule_2466 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Throwcontrol_2420', tco_apply(shen_catchpoint, [])), tail_call(shen_cutpoint, [KL_CTX.KL_LOC_Throwcontrol_2420, [setattr(KL_CTX, 'KL_LOC_Case_2421', [setattr(KL_CTX, 'KL_LOC_V2401_2422', tco_apply(shen_lazyderef, [KL_ARG_V3053_2415, KL_ARG_V3056_2418])), ([setattr(KL_CTX, 'KL_LOC_V2402_2423', tco_apply(shen_lazyderef, [KL_ARG_V3055_2417, KL_ARG_V3056_2418])), ([setattr(KL_CTX, 'KL_LOC_V2403_2424', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2402_2423), KL_ARG_V3056_2418])), ([setattr(KL_CTX, 'KL_LOC_V2404_2425', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2402_2423), KL_ARG_V3056_2418])), ([setattr(KL_CTX, 'KL_LOC_Semantics_2426', car(KL_CTX.KL_LOC_V2404_2425)), [setattr(KL_CTX, 'KL_LOC_V2405_2427', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2404_2425), KL_ARG_V3056_2418])), ([tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2420, KL_ARG_V3056_2418, (lambda : tail_call(kl_bind, [KL_ARG_V3054_2416, tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Semantics_2426, KL_ARG_V3056_2418]), KL_ARG_V3056_2418, KL_ARG_V3057_2419]))])][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2405_2427) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2404_2425) else False)][(-1)] if shen_eq(symdic.symdic_kl_x58x61, KL_CTX.KL_LOC_V2403_2424) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2402_2423) else False)][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2401_2422) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2401_2422, nil, KL_ARG_V3056_2418]), [setattr(KL_CTX, 'KL_LOC_Result_2428', [setattr(KL_CTX, 'KL_LOC_V2406_2429', tco_apply(shen_lazyderef, [KL_ARG_V3055_2417, KL_ARG_V3056_2418])), ([setattr(KL_CTX, 'KL_LOC_V2407_2430', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2406_2429), KL_ARG_V3056_2418])), ([setattr(KL_CTX, 'KL_LOC_V2408_2431', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2406_2429), KL_ARG_V3056_2418])), ([setattr(KL_CTX, 'KL_LOC_Semantics_2432', car(KL_CTX.KL_LOC_V2408_2431)), [setattr(KL_CTX, 'KL_LOC_V2409_2433', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2408_2431), KL_ARG_V3056_2418])), ([tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2420, KL_ARG_V3056_2418, (lambda : tail_call(kl_bind, [KL_ARG_V3054_2416, tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Semantics_2432, KL_ARG_V3056_2418]), KL_ARG_V3056_2418, KL_ARG_V3057_2419]))])][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2409_2433) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2408_2431) else False)][(-1)] if shen_eq(symdic.symdic_kl_x58x61, KL_CTX.KL_LOC_V2407_2430) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2406_2429) else False)][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2401_2422, KL_ARG_V3056_2418]), KL_CTX.KL_LOC_Result_2428][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2401_2422]) else False))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_2434', [setattr(KL_CTX, 'KL_LOC_V2410_2435', tco_apply(shen_lazyderef, [KL_ARG_V3053_2415, KL_ARG_V3056_2418])), ([setattr(KL_CTX, 'KL_LOC_V2411_2436', tco_apply(shen_lazyderef, [KL_ARG_V3055_2417, KL_ARG_V3056_2418])), ([setattr(KL_CTX, 'KL_LOC_V2412_2437', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2411_2436), KL_ARG_V3056_2418])), ([setattr(KL_CTX, 'KL_LOC_V2413_2438', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2411_2436), KL_ARG_V3056_2418])), ([setattr(KL_CTX, 'KL_LOC_Semantics_2439', car(KL_CTX.KL_LOC_V2413_2438)), [setattr(KL_CTX, 'KL_LOC_V2414_2440', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2413_2438), KL_ARG_V3056_2418])), ([setattr(KL_CTX, 'KL_LOC_V2415_2441', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2414_2440), KL_ARG_V3056_2418])), ([setattr(KL_CTX, 'KL_LOC_V2416_2442', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2414_2440), KL_ARG_V3056_2418])), ([setattr(KL_CTX, 'KL_LOC_G_2443', car(KL_CTX.KL_LOC_V2416_2442)), [setattr(KL_CTX, 'KL_LOC_V2417_2444', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2416_2442), KL_ARG_V3056_2418])), ([tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2420, KL_ARG_V3056_2418, (lambda : tail_call(kl_bind, [KL_ARG_V3054_2416, Cons(symdic.symdic_kl_where, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_G_2443, KL_ARG_V3056_2418]), Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Semantics_2439, KL_ARG_V3056_2418]), nil))), KL_ARG_V3056_2418, KL_ARG_V3057_2419]))])][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2417_2444) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2416_2442) else False)][(-1)] if shen_eq(symdic.symdic_kl_where, KL_CTX.KL_LOC_V2415_2441) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2414_2440) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2413_2438) else False)][(-1)] if shen_eq(symdic.symdic_kl_x58x61, KL_CTX.KL_LOC_V2412_2437) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2411_2436) else False)][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2410_2435) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2410_2435, nil, KL_ARG_V3056_2418]), [setattr(KL_CTX, 'KL_LOC_Result_2445', [setattr(KL_CTX, 'KL_LOC_V2418_2446', tco_apply(shen_lazyderef, [KL_ARG_V3055_2417, KL_ARG_V3056_2418])), ([setattr(KL_CTX, 'KL_LOC_V2419_2447', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2418_2446), KL_ARG_V3056_2418])), ([setattr(KL_CTX, 'KL_LOC_V2420_2448', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2418_2446), KL_ARG_V3056_2418])), ([setattr(KL_CTX, 'KL_LOC_Semantics_2449', car(KL_CTX.KL_LOC_V2420_2448)), [setattr(KL_CTX, 'KL_LOC_V2421_2450', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2420_2448), KL_ARG_V3056_2418])), ([setattr(KL_CTX, 'KL_LOC_V2422_2451', tco_apply(shen_lazyderef, [car(KL_CTX.KL_LOC_V2421_2450), KL_ARG_V3056_2418])), ([setattr(KL_CTX, 'KL_LOC_V2423_2452', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2421_2450), KL_ARG_V3056_2418])), ([setattr(KL_CTX, 'KL_LOC_G_2453', car(KL_CTX.KL_LOC_V2423_2452)), [setattr(KL_CTX, 'KL_LOC_V2424_2454', tco_apply(shen_lazyderef, [cdr(KL_CTX.KL_LOC_V2423_2452), KL_ARG_V3056_2418])), ([tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2420, KL_ARG_V3056_2418, (lambda : tail_call(kl_bind, [KL_ARG_V3054_2416, Cons(symdic.symdic_kl_where, Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_G_2453, KL_ARG_V3056_2418]), Cons(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Semantics_2449, KL_ARG_V3056_2418]), nil))), KL_ARG_V3056_2418, KL_ARG_V3057_2419]))])][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2424_2454) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2423_2452) else False)][(-1)] if shen_eq(symdic.symdic_kl_where, KL_CTX.KL_LOC_V2422_2451) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2421_2450) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2420_2448) else False)][(-1)] if shen_eq(symdic.symdic_kl_x58x61, KL_CTX.KL_LOC_V2419_2447) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2418_2446) else False)][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2410_2435, KL_ARG_V3056_2418]), KL_CTX.KL_LOC_Result_2445][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2410_2435]) else False))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_V2425_2455', tco_apply(shen_lazyderef, [KL_ARG_V3053_2415, KL_ARG_V3056_2418])), ([setattr(KL_CTX, 'KL_LOC_X2397_2456', car(KL_CTX.KL_LOC_V2425_2455)), [setattr(KL_CTX, 'KL_LOC_Syntax_2457', cdr(KL_CTX.KL_LOC_V2425_2455)), [setattr(KL_CTX, 'KL_LOC_V2426_2458', tco_apply(shen_lazyderef, [KL_ARG_V3055_2417, KL_ARG_V3056_2418])), ([setattr(KL_CTX, 'KL_LOC_X_2459', car(KL_CTX.KL_LOC_V2426_2458)), [setattr(KL_CTX, 'KL_LOC_Rule_2460', cdr(KL_CTX.KL_LOC_V2426_2458)), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_X_2459, KL_CTX.KL_LOC_X2397_2456, KL_ARG_V3056_2418, (lambda : tail_call(shen_getx45syntaxx43semantics, [KL_CTX.KL_LOC_Syntax_2457, KL_ARG_V3054_2416, KL_CTX.KL_LOC_Rule_2460, KL_ARG_V3056_2418, KL_ARG_V3057_2419]))])][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2426_2458) else False)][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2425_2455) else ([setattr(KL_CTX, 'KL_LOC_X2397_2461', tco_apply(shen_newpv, [KL_ARG_V3056_2418])), [setattr(KL_CTX, 'KL_LOC_Syntax_2462', tco_apply(shen_newpv, [KL_ARG_V3056_2418])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2425_2455, Cons(KL_CTX.KL_LOC_X2397_2461, KL_CTX.KL_LOC_Syntax_2462), KL_ARG_V3056_2418]), [setattr(KL_CTX, 'KL_LOC_Result_2463', [setattr(KL_CTX, 'KL_LOC_V2427_2464', tco_apply(shen_lazyderef, [KL_ARG_V3055_2417, KL_ARG_V3056_2418])), ([setattr(KL_CTX, 'KL_LOC_X_2465', car(KL_CTX.KL_LOC_V2427_2464)), [setattr(KL_CTX, 'KL_LOC_Rule_2466', cdr(KL_CTX.KL_LOC_V2427_2464)), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_X_2465, KL_CTX.KL_LOC_X2397_2461, KL_ARG_V3056_2418, (lambda : tail_call(shen_getx45syntaxx43semantics, [KL_CTX.KL_LOC_Syntax_2462, KL_ARG_V3054_2416, KL_CTX.KL_LOC_Rule_2466, KL_ARG_V3056_2418, KL_ARG_V3057_2419]))])][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2427_2464) else False)][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2425_2455, KL_ARG_V3056_2418]), KL_CTX.KL_LOC_Result_2463][(-1)]][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2425_2455]) else False))][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2434, False) else KL_CTX.KL_LOC_Case_2434)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2421, False) else KL_CTX.KL_LOC_Case_2421)][(-1)]])][(-1)]
shen_add_fun('shen.get-syntax+semantics', shen_getx45syntaxx43semantics, 5)

@tail_recursion
def shen_syntaxx45check(*FUN_ARGS):
    FUN_ARITY = 5
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_syntaxx45check, (FUN_ARGS + lambdaargs)))
    KL_ARG_V3058_2467 = FUN_ARGS[0]
    KL_ARG_V3059_2468 = FUN_ARGS[1]
    KL_ARG_V3060_2469 = FUN_ARGS[2]
    KL_ARG_V3061_2470 = FUN_ARGS[3]
    KL_ARG_V3062_2471 = FUN_ARGS[4]

    class KL_Context:
        KL_LOC_Throwcontrol_2472 = None
        KL_LOC_Case_2473 = None
        KL_LOC_V2394_2474 = None
        KL_LOC_Case_2475 = None
        KL_LOC_V2395_2476 = None
        KL_LOC_X_2477 = None
        KL_LOC_Syntax_2478 = None
        KL_LOC_C_2479 = None
        KL_LOC_Xx38x38_2480 = None
        KL_LOC_B_2481 = None
        KL_LOC_V2396_2482 = None
        KL_LOC_X_2483 = None
        KL_LOC_Syntax_2484 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Throwcontrol_2472', tco_apply(shen_catchpoint, [])), tail_call(shen_cutpoint, [KL_CTX.KL_LOC_Throwcontrol_2472, [setattr(KL_CTX, 'KL_LOC_Case_2473', [setattr(KL_CTX, 'KL_LOC_V2394_2474', tco_apply(shen_lazyderef, [KL_ARG_V3058_2467, KL_ARG_V3061_2470])), ([tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V3062_2471])][(-1)] if shen_eq(nil, KL_CTX.KL_LOC_V2394_2474) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_2475', [setattr(KL_CTX, 'KL_LOC_V2395_2476', tco_apply(shen_lazyderef, [KL_ARG_V3058_2467, KL_ARG_V3061_2470])), ([setattr(KL_CTX, 'KL_LOC_X_2477', car(KL_CTX.KL_LOC_V2395_2476)), [setattr(KL_CTX, 'KL_LOC_Syntax_2478', cdr(KL_CTX.KL_LOC_V2395_2476)), [setattr(KL_CTX, 'KL_LOC_C_2479', tco_apply(shen_newpv, [KL_ARG_V3061_2470])), [setattr(KL_CTX, 'KL_LOC_Xx38x38_2480', tco_apply(shen_newpv, [KL_ARG_V3061_2470])), [setattr(KL_CTX, 'KL_LOC_B_2481', tco_apply(shen_newpv, [KL_ARG_V3061_2470])), [tco_apply(shen_incinfs, []), tco_apply(kl_fwhen, [tco_apply(shen_grammar_symbolx63, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_2477, KL_ARG_V3061_2470])]), KL_ARG_V3061_2470, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2472, KL_ARG_V3061_2470, (lambda : tail_call(shen_tx42, [Cons(KL_CTX.KL_LOC_X_2477, Cons(symdic.symdic_kl_x58, Cons(Cons(Cons(symdic.symdic_kl_list, Cons(KL_CTX.KL_LOC_B_2481, nil)), Cons(symdic.symdic_kl_x61x61x62, Cons(KL_CTX.KL_LOC_C_2479, nil))), nil))), KL_ARG_V3060_2469, KL_ARG_V3061_2470, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2472, KL_ARG_V3061_2470, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Xx38x38_2480, tco_apply(kl_concat, [symdic.symdic_kl_x38x38, tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_2477, KL_ARG_V3061_2470])]), KL_ARG_V3061_2470, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2472, KL_ARG_V3061_2470, (lambda : tail_call(shen_tx42, [Cons(KL_CTX.KL_LOC_Xx38x38_2480, Cons(symdic.symdic_kl_x58, Cons(Cons(symdic.symdic_kl_list, Cons(KL_ARG_V3059_2468, nil)), nil))), Cons(Cons(KL_CTX.KL_LOC_Xx38x38_2480, Cons(symdic.symdic_kl_x58, Cons(Cons(symdic.symdic_kl_list, Cons(KL_CTX.KL_LOC_B_2481, nil)), nil))), KL_ARG_V3060_2469), KL_ARG_V3061_2470, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2472, KL_ARG_V3061_2470, (lambda : tail_call(shen_syntaxx45check, [KL_CTX.KL_LOC_Syntax_2478, KL_ARG_V3059_2468, KL_ARG_V3060_2469, KL_ARG_V3061_2470, KL_ARG_V3062_2471]))]))]))]))]))]))]))]))])][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2395_2476) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_V2396_2482', tco_apply(shen_lazyderef, [KL_ARG_V3058_2467, KL_ARG_V3061_2470])), ([setattr(KL_CTX, 'KL_LOC_X_2483', car(KL_CTX.KL_LOC_V2396_2482)), [setattr(KL_CTX, 'KL_LOC_Syntax_2484', cdr(KL_CTX.KL_LOC_V2396_2482)), [tco_apply(shen_incinfs, []), tco_apply(shen_tx42, [Cons(KL_CTX.KL_LOC_X_2483, Cons(symdic.symdic_kl_x58, Cons(KL_ARG_V3059_2468, nil))), KL_ARG_V3060_2469, KL_ARG_V3061_2470, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2472, KL_ARG_V3061_2470, (lambda : tail_call(shen_syntaxx45check, [KL_CTX.KL_LOC_Syntax_2484, KL_ARG_V3059_2468, KL_ARG_V3060_2469, KL_ARG_V3061_2470, KL_ARG_V3062_2471]))]))])][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2396_2482) else False)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2475, False) else KL_CTX.KL_LOC_Case_2475)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2473, False) else KL_CTX.KL_LOC_Case_2473)][(-1)]])][(-1)]
shen_add_fun('shen.syntax-check', shen_syntaxx45check, 5)

@tail_recursion
def shen_semanticsx45check(*FUN_ARGS):
    FUN_ARITY = 5
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_semanticsx45check, (FUN_ARGS + lambdaargs)))
    KL_ARG_V3063_2485 = FUN_ARGS[0]
    KL_ARG_V3064_2486 = FUN_ARGS[1]
    KL_ARG_V3065_2487 = FUN_ARGS[2]
    KL_ARG_V3066_2488 = FUN_ARGS[3]
    KL_ARG_V3067_2489 = FUN_ARGS[4]

    class KL_Context:
        KL_LOC_Semanticsx42_2490 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Semanticsx42_2490', tco_apply(shen_newpv, [KL_ARG_V3066_2488])), [tco_apply(shen_incinfs, []), tail_call(kl_bind, [KL_CTX.KL_LOC_Semanticsx42_2490, tco_apply(shen_curry, [tco_apply(shen_renamex45semantics, [tco_apply(shen_deref, [KL_ARG_V3063_2485, KL_ARG_V3066_2488])])]), KL_ARG_V3066_2488, (lambda : tail_call(shen_tx42, [Cons(KL_CTX.KL_LOC_Semanticsx42_2490, Cons(symdic.symdic_kl_x58, Cons(KL_ARG_V3064_2486, nil))), KL_ARG_V3065_2487, KL_ARG_V3066_2488, KL_ARG_V3067_2489]))])][(-1)]][(-1)]
shen_add_fun('shen.semantics-check', shen_semanticsx45check, 5)

@tail_recursion
def shen_renamex45semantics(*FUN_ARGS):
    FUN_ARITY = 1
    if (len(FUN_ARGS) < FUN_ARITY):
        return (lambda *lambdaargs: apply(shen_renamex45semantics, (FUN_ARGS + lambdaargs)))
    KL_ARG_V3068_2491 = FUN_ARGS[0]
    global symdic
    return (Cons(tco_apply(shen_renamex45semantics, [car(KL_ARG_V3068_2491)]), tco_apply(shen_renamex45semantics, [cdr(KL_ARG_V3068_2491)])) if shen_consp(KL_ARG_V3068_2491) else (Cons(symdic.symdic_shen_x60x45sem, Cons(KL_ARG_V3068_2491, nil)) if tco_apply(shen_grammar_symbolx63, [KL_ARG_V3068_2491]) else (KL_ARG_V3068_2491 if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.rename-semantics', shen_renamex45semantics, 1)
shen_initialise_arity_table(shen_to_cons([Sym('absvector'), 1, Sym('adjoin'), 2, Sym('and'), 2, Sym('append'), 2, Sym('arity'), 1, Sym('assoc'), 2, Sym('boolean?'), 1, Sym('cd'), 1, Sym('compile'), 3, Sym('concat'), 2, Sym('cons'), 2, Sym('cons?'), 1, Sym('cn'), 2, Sym('declare'), 2, Sym('destroy'), 1, Sym('difference'), 2, Sym('do'), 2, Sym('element?'), 2, Sym('empty?'), 1, Sym('enable-type-theory'), 1, Sym('interror'), 2, Sym('eval'), 1, Sym('eval-kl'), 1, Sym('explode'), 1, Sym('external'), 1, Sym('fail-if'), 2, Sym('fail'), 0, Sym('fix'), 2, Sym('findall'), 5, Sym('freeze'), 1, Sym('fst'), 1, Sym('gensym'), 1, Sym('get'), 3, Sym('get-time'), 1, Sym('address->'), 3, Sym('<-address'), 2, Sym('<-vector'), 2, Sym('>'), 2, Sym('>='), 2, Sym('='), 2, Sym('hd'), 1, Sym('hdv'), 1, Sym('hdstr'), 1, Sym('head'), 1, Sym('if'), 3, Sym('integer?'), 1, Sym('identical'), 4, Sym('inferences'), 0, Sym('intersection'), 2, Sym('length'), 1, Sym('lineread'), 0, Sym('load'), 1, Sym('<'), 2, Sym('<='), 2, Sym('vector'), 1, Sym('macroexpand'), 1, Sym('map'), 2, Sym('mapcan'), 2, Sym('maxinferences'), 1, Sym('not'), 1, Sym('nth'), 2, Sym('n->string'), 1, Sym('number?'), 1, Sym('occurs-check'), 1, Sym('occurrences'), 2, Sym('occurs-check'), 1, Sym('or'), 2, Sym('package'), 3, Sym('pos'), 2, Sym('print'), 1, Sym('profile'), 1, Sym('profile-results'), 0, Sym('pr'), 2, Sym('ps'), 1, Sym('preclude'), 1, Sym('preclude-all-but'), 1, Sym('protect'), 1, Sym('address->'), 3, Sym('put'), 4, Sym('shen.reassemble'), 2, Sym('read-file-as-string'), 1, Sym('read-file'), 1, Sym('read-byte'), 1, Sym('read-from-string'), 1, Sym('remove'), 2, Sym('reverse'), 1, Sym('set'), 2, Sym('simple-error'), 1, Sym('snd'), 1, Sym('specialise'), 1, Sym('spy'), 1, Sym('step'), 1, Sym('stinput'), 0, Sym('stoutput'), 0, Sym('string->n'), 1, Sym('string->symbol'), 1, Sym('string?'), 1, Sym('shen.strong-warning'), 1, Sym('subst'), 3, Sym('shen.sum'), 1, Sym('symbol?'), 1, Sym('tail'), 1, Sym('tl'), 1, Sym('tc'), 1, Sym('tc?'), 1, Sym('thaw'), 1, Sym('track'), 1, Sym('trap-error'), 2, Sym('tuple?'), 1, Sym('type'), 1, Sym('return'), 3, Sym('undefmacro'), 1, Sym('unprofile'), 1, Sym('unify'), 4, Sym('unify!'), 4, Sym('union'), 2, Sym('untrack'), 1, Sym('unspecialise'), 1, Sym('undefmacro'), 1, Sym('vector'), 1, Sym('vector->'), 3, Sym('value'), 1, Sym('variable?'), 1, Sym('version'), 1, Sym('warn'), 1, Sym('write-to-file'), 2, Sym('y-or-n?'), 1, Sym('+'), 2, Sym('*'), 2, Sym('/'), 2, Sym('-'), 2, Sym('=='), 2, Sym('shen.<1>'), 1, Sym('<e>'), 1, Sym('@p'), 2, Sym('@v'), 2, Sym('@s'), 2, Sym('preclude'), 1, Sym('include'), 1, Sym('preclude-all-but'), 1, Sym('include-all-but'), 1, Sym('where'), 2]))
kl_put(shen_intern('shen'), Sym('shen.external-symbols'), shen_to_cons([Sym('!'), Sym('}'), Sym('{'), Sym('-->'), Sym('<--'), Sym('&&'), Sym(':'), Sym(';'), Sym(':-'), Sym(':='), Sym('_'), Sym('*language*'), Sym('*implementation*'), Sym('*stinput*'), Sym('*home-directory*'), Sym('*version*'), Sym('*maximum-print-sequence-size*'), Sym('*macros*'), Sym('*os*'), Sym('*release*'), Sym('*property-vector*'), Sym('@v'), Sym('@p'), Sym('@s'), Sym('*port*'), Sym('*porters*'), Sym('<-'), Sym('->'), Sym('<e>'), Sym('=='), Sym('='), Sym('>='), Sym('>'), Sym('/.'), Sym('=!'), Sym('$'), Sym('-'), Sym('/'), Sym('*'), Sym('+'), Sym('<='), Sym('<'), Sym('>>'), tco_apply(kl_vector, [0]), Sym('==>'), Sym('y-or-n?'), Sym('write-to-file'), Sym('where'), Sym('when'), Sym('warn'), Sym('version'), Sym('verified'), Sym('variable?'), Sym('value'), Sym('vector->'), Sym('<-vector'), Sym('vector'), Sym('vector?'), Sym('unspecialise'), Sym('untrack'), Sym('unit'), Sym('shen.unix'), Sym('union'), Sym('unify'), Sym('unify!'), Sym('unprofile'), Sym('undefmacro'), Sym('return'), Sym('type'), Sym('tuple?'), Sym('true'), Sym('trap-error'), Sym('track'), Sym('time'), Sym('thaw'), Sym('tc?'), Sym('tc'), Sym('tl'), Sym('tlstr'), Sym('tlv'), Sym('tail'), Sym('systemf'), Sym('synonyms'), Sym('symbol'), Sym('symbol?'), Sym('string->symbol'), Sym('subst'), Sym('string?'), Sym('string->n'), Sym('stream'), Sym('string'), Sym('stinput'), Sym('stoutput'), Sym('step'), Sym('spy'), Sym('specialise'), Sym('snd'), Sym('simple-error'), Sym('set'), Sym('save'), Sym('str'), Sym('run'), Sym('reverse'), Sym('remove'), Sym('read'), Sym('read-file'), Sym('read-file-as-bytelist'), Sym('read-file-as-string'), Sym('read-byte'), Sym('read-from-string'), Sym('quit'), Sym('put'), Sym('preclude'), Sym('preclude-all-but'), Sym('ps'), Sym('prolog?'), Sym('protect'), Sym('profile-results'), Sym('profile'), Sym('print'), Sym('pr'), Sym('pos'), Sym('package'), Sym('output'), Sym('out'), Sym('or'), Sym('open'), Sym('occurrences'), Sym('occurs-check'), Sym('n->string'), Sym('number?'), Sym('number'), Sym('null'), Sym('nth'), Sym('not'), Sym('nl'), Sym('mode'), Sym('macro'), Sym('macroexpand'), Sym('maxinferences'), Sym('mapcan'), Sym('map'), Sym('make-string'), Sym('load'), Sym('loaded'), Sym('list'), Sym('lineread'), Sym('limit'), Sym('length'), Sym('let'), Sym('lazy'), Sym('lambda'), Sym('is'), Sym('intersection'), Sym('inferences'), Sym('intern'), Sym('integer?'), Sym('input'), Sym('input+'), Sym('include'), Sym('include-all-but'), Sym('in'), Sym('if'), Sym('identical'), Sym('head'), Sym('hd'), Sym('hdv'), Sym('hdstr'), Sym('hash'), Sym('get'), Sym('get-time'), Sym('gensym'), Sym('function'), Sym('fst'), Sym('freeze'), Sym('fix'), Sym('file'), Sym('fail'), Sym('fail-if'), Sym('fwhen'), Sym('findall'), Sym('false'), Sym('enable-type-theory'), Sym('explode'), Sym('external'), Sym('exception'), Sym('eval-kl'), Sym('eval'), Sym('error-to-string'), Sym('error'), Sym('empty?'), Sym('element?'), Sym('do'), Sym('difference'), Sym('destroy'), Sym('defun'), Sym('define'), Sym('defmacro'), Sym('defcc'), Sym('defprolog'), Sym('declare'), Sym('datatype'), Sym('cut'), Sym('cn'), Sym('cons?'), Sym('cons'), Sym('cond'), Sym('concat'), Sym('compile'), Sym('cd'), Sym('cases'), Sym('call'), Sym('close'), Sym('bind'), Sym('bound?'), Sym('boolean?'), Sym('boolean'), Sym('bar!'), Sym('assoc'), Sym('arity'), Sym('append'), Sym('and'), Sym('adjoin'), Sym('<-address'), Sym('address->'), Sym('absvector?'), Sym('absvector'), Sym('abort')]), shen_get(Sym('*property-vector*')))
apply(kl_declare, [symdic.symdic_kl_absvectorx63, Cons(symdic.symdic_A, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_boolean, nil)))])
apply(kl_declare, [symdic.symdic_kl_adjoin, Cons(symdic.symdic_A, Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(Cons(symdic.symdic_kl_list, Cons(symdic.symdic_A, nil)), Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(symdic.symdic_kl_list, Cons(symdic.symdic_A, nil)), nil))), nil)))])
apply(kl_declare, [symdic.symdic_kl_and, Cons(symdic.symdic_kl_boolean, Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(symdic.symdic_kl_boolean, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_boolean, nil))), nil)))])
apply(kl_declare, [symdic.symdic_shen_app, Cons(symdic.symdic_A, Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(symdic.symdic_kl_string, Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(symdic.symdic_kl_symbol, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_string, nil))), nil))), nil)))])
apply(kl_declare, [symdic.symdic_kl_append, Cons(Cons(symdic.symdic_kl_list, Cons(symdic.symdic_A, nil)), Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(Cons(symdic.symdic_kl_list, Cons(symdic.symdic_A, nil)), Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(symdic.symdic_kl_list, Cons(symdic.symdic_A, nil)), nil))), nil)))])
apply(kl_declare, [symdic.symdic_kl_arity, Cons(symdic.symdic_A, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_number, nil)))])
apply(kl_declare, [symdic.symdic_kl_assoc, Cons(symdic.symdic_A, Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(Cons(symdic.symdic_kl_list, Cons(Cons(symdic.symdic_kl_list, Cons(symdic.symdic_A, nil)), nil)), Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(symdic.symdic_kl_list, Cons(symdic.symdic_A, nil)), nil))), nil)))])
apply(kl_declare, [symdic.symdic_kl_booleanx63, Cons(symdic.symdic_A, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_boolean, nil)))])
apply(kl_declare, [symdic.symdic_kl_boundx63, Cons(symdic.symdic_kl_symbol, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_boolean, nil)))])
apply(kl_declare, [symdic.symdic_kl_cd, Cons(symdic.symdic_kl_string, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_string, nil)))])
apply(kl_declare, [symdic.symdic_kl_close, Cons(Cons(symdic.symdic_kl_stream, Cons(symdic.symdic_A, nil)), Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(symdic.symdic_kl_list, Cons(symdic.symdic_B, nil)), nil)))])
apply(kl_declare, [symdic.symdic_kl_cn, Cons(symdic.symdic_kl_string, Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(symdic.symdic_kl_string, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_string, nil))), nil)))])
apply(kl_declare, [symdic.symdic_kl_compile, Cons(Cons(Cons(symdic.symdic_kl_list, Cons(symdic.symdic_A, nil)), Cons(symdic.symdic_kl_x61x61x62, Cons(symdic.symdic_B, nil))), Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(Cons(symdic.symdic_kl_list, Cons(symdic.symdic_A, nil)), Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(Cons(Cons(symdic.symdic_kl_list, Cons(symdic.symdic_A, nil)), Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_B, nil))), Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_B, nil))), nil))), nil)))])
apply(kl_declare, [symdic.symdic_kl_consx63, Cons(symdic.symdic_A, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_boolean, nil)))])
apply(kl_declare, [symdic.symdic_kl_destroy, Cons(Cons(symdic.symdic_A, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_B, nil))), Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(symdic.symdic_A, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_B, nil))), nil)))])
apply(kl_declare, [symdic.symdic_kl_difference, Cons(Cons(symdic.symdic_kl_list, Cons(symdic.symdic_A, nil)), Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(Cons(symdic.symdic_kl_list, Cons(symdic.symdic_A, nil)), Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(symdic.symdic_kl_list, Cons(symdic.symdic_A, nil)), nil))), nil)))])
apply(kl_declare, [symdic.symdic_kl_do, Cons(symdic.symdic_A, Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(symdic.symdic_B, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_B, nil))), nil)))])
apply(kl_declare, [symdic.symdic_kl_x60ex62, Cons(Cons(symdic.symdic_kl_list, Cons(symdic.symdic_A, nil)), Cons(symdic.symdic_kl_x61x61x62, Cons(Cons(symdic.symdic_kl_list, Cons(symdic.symdic_B, nil)), nil)))])
apply(kl_declare, [symdic.symdic_x60x33x62, Cons(Cons(symdic.symdic_kl_list, Cons(symdic.symdic_A, nil)), Cons(symdic.symdic_kl_x61x61x62, Cons(Cons(symdic.symdic_kl_list, Cons(symdic.symdic_A, nil)), nil)))])
apply(kl_declare, [symdic.symdic_kl_elementx63, Cons(symdic.symdic_A, Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(Cons(symdic.symdic_kl_list, Cons(symdic.symdic_A, nil)), Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_boolean, nil))), nil)))])
apply(kl_declare, [symdic.symdic_kl_emptyx63, Cons(symdic.symdic_A, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_boolean, nil)))])
apply(kl_declare, [symdic.symdic_kl_enablex45typex45theory, Cons(symdic.symdic_kl_symbol, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_boolean, nil)))])
apply(kl_declare, [symdic.symdic_kl_external, Cons(symdic.symdic_kl_symbol, Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(symdic.symdic_kl_list, Cons(symdic.symdic_kl_symbol, nil)), nil)))])
apply(kl_declare, [symdic.symdic_kl_errorx45tox45string, Cons(symdic.symdic_kl_exception, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_string, nil)))])
apply(kl_declare, [symdic.symdic_kl_explode, Cons(symdic.symdic_A, Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(symdic.symdic_kl_list, Cons(symdic.symdic_kl_string, nil)), nil)))])
apply(kl_declare, [symdic.symdic_kl_failx45if, Cons(Cons(symdic.symdic_kl_symbol, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_boolean, nil))), Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(symdic.symdic_kl_symbol, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_symbol, nil))), nil)))])
apply(kl_declare, [symdic.symdic_kl_fix, Cons(Cons(symdic.symdic_A, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_A, nil))), Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(symdic.symdic_A, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_A, nil))), nil)))])
apply(kl_declare, [symdic.symdic_format, Cons(Cons(symdic.symdic_kl_stream, Cons(symdic.symdic_kl_out, nil)), Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(symdic.symdic_kl_string, Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(symdic.symdic_A, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_string, nil))), nil))), nil)))])
apply(kl_declare, [symdic.symdic_kl_freeze, Cons(symdic.symdic_A, Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(symdic.symdic_kl_lazy, Cons(symdic.symdic_A, nil)), nil)))])
apply(kl_declare, [symdic.symdic_kl_fst, Cons(Cons(symdic.symdic_A, Cons(symdic.symdic_kl_x42, Cons(symdic.symdic_B, nil))), Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_A, nil)))])
apply(kl_declare, [symdic.symdic_kl_gensym, Cons(symdic.symdic_kl_symbol, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_symbol, nil)))])
apply(kl_declare, [symdic.symdic_kl_x60x45vector, Cons(Cons(symdic.symdic_kl_vector, Cons(symdic.symdic_A, nil)), Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(symdic.symdic_kl_number, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_A, nil))), nil)))])
apply(kl_declare, [symdic.symdic_kl_vectorx45x62, Cons(Cons(symdic.symdic_kl_vector, Cons(symdic.symdic_A, nil)), Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(symdic.symdic_kl_number, Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(symdic.symdic_A, Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(symdic.symdic_kl_vector, Cons(symdic.symdic_A, nil)), nil))), nil))), nil)))])
apply(kl_declare, [symdic.symdic_kl_vector, Cons(symdic.symdic_kl_number, Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(symdic.symdic_kl_vector, Cons(symdic.symdic_A, nil)), nil)))])
apply(kl_declare, [symdic.symdic_kl_getx45time, Cons(symdic.symdic_kl_symbol, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_number, nil)))])
apply(kl_declare, [symdic.symdic_kl_hash, Cons(symdic.symdic_A, Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(symdic.symdic_kl_number, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_number, nil))), nil)))])
apply(kl_declare, [symdic.symdic_kl_head, Cons(Cons(symdic.symdic_kl_list, Cons(symdic.symdic_A, nil)), Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_A, nil)))])
apply(kl_declare, [symdic.symdic_kl_hdv, Cons(Cons(symdic.symdic_kl_vector, Cons(symdic.symdic_A, nil)), Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_A, nil)))])
apply(kl_declare, [symdic.symdic_kl_hdstr, Cons(symdic.symdic_kl_string, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_string, nil)))])
apply(kl_declare, [symdic.symdic_kl_if, Cons(symdic.symdic_kl_boolean, Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(symdic.symdic_A, Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(symdic.symdic_A, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_A, nil))), nil))), nil)))])
apply(kl_declare, [symdic.symdic_kl_include, Cons(Cons(symdic.symdic_kl_list, Cons(symdic.symdic_kl_symbol, nil)), Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(symdic.symdic_kl_list, Cons(symdic.symdic_kl_symbol, nil)), nil)))])
apply(kl_declare, [symdic.symdic_kl_includex45allx45but, Cons(Cons(symdic.symdic_kl_list, Cons(symdic.symdic_kl_symbol, nil)), Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(symdic.symdic_kl_list, Cons(symdic.symdic_kl_symbol, nil)), nil)))])
apply(kl_declare, [symdic.symdic_kl_inferences, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_number, nil))])
apply(kl_declare, [symdic.symdic_shen_insert, Cons(symdic.symdic_A, Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(symdic.symdic_kl_string, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_string, nil))), nil)))])
apply(kl_declare, [symdic.symdic_kl_integerx63, Cons(symdic.symdic_A, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_boolean, nil)))])
apply(kl_declare, [symdic.symdic_kl_intersection, Cons(Cons(symdic.symdic_kl_list, Cons(symdic.symdic_A, nil)), Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(Cons(symdic.symdic_kl_list, Cons(symdic.symdic_A, nil)), Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(symdic.symdic_kl_list, Cons(symdic.symdic_A, nil)), nil))), nil)))])
apply(kl_declare, [symdic.symdic_kl_length, Cons(Cons(symdic.symdic_kl_list, Cons(symdic.symdic_A, nil)), Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_number, nil)))])
apply(kl_declare, [symdic.symdic_kl_limit, Cons(Cons(symdic.symdic_kl_vector, Cons(symdic.symdic_A, nil)), Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_number, nil)))])
apply(kl_declare, [symdic.symdic_kl_load, Cons(symdic.symdic_kl_string, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_symbol, nil)))])
apply(kl_declare, [symdic.symdic_kl_map, Cons(Cons(symdic.symdic_A, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_B, nil))), Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(Cons(symdic.symdic_kl_list, Cons(symdic.symdic_A, nil)), Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(symdic.symdic_kl_list, Cons(symdic.symdic_B, nil)), nil))), nil)))])
apply(kl_declare, [symdic.symdic_kl_mapcan, Cons(Cons(symdic.symdic_A, Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(symdic.symdic_kl_list, Cons(symdic.symdic_B, nil)), nil))), Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(Cons(symdic.symdic_kl_list, Cons(symdic.symdic_A, nil)), Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(symdic.symdic_kl_list, Cons(symdic.symdic_B, nil)), nil))), nil)))])
apply(kl_declare, [symdic.symdic_kl_maxinferences, Cons(symdic.symdic_kl_number, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_number, nil)))])
apply(kl_declare, [symdic.symdic_kl_nx45x62string, Cons(symdic.symdic_kl_number, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_string, nil)))])
apply(kl_declare, [symdic.symdic_kl_nl, Cons(symdic.symdic_kl_number, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_number, nil)))])
apply(kl_declare, [symdic.symdic_kl_not, Cons(symdic.symdic_kl_boolean, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_boolean, nil)))])
apply(kl_declare, [symdic.symdic_kl_nth, Cons(symdic.symdic_kl_number, Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(Cons(symdic.symdic_kl_list, Cons(symdic.symdic_A, nil)), Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_A, nil))), nil)))])
apply(kl_declare, [symdic.symdic_kl_numberx63, Cons(symdic.symdic_A, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_boolean, nil)))])
apply(kl_declare, [symdic.symdic_kl_occurrences, Cons(symdic.symdic_A, Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(symdic.symdic_B, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_number, nil))), nil)))])
apply(kl_declare, [symdic.symdic_kl_occursx45check, Cons(symdic.symdic_kl_symbol, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_boolean, nil)))])
apply(kl_declare, [symdic.symdic_optimise, Cons(symdic.symdic_kl_symbol, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_boolean, nil)))])
apply(kl_declare, [symdic.symdic_kl_or, Cons(symdic.symdic_kl_boolean, Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(symdic.symdic_kl_boolean, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_boolean, nil))), nil)))])
apply(kl_declare, [symdic.symdic_kl_pos, Cons(symdic.symdic_kl_string, Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(symdic.symdic_kl_number, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_string, nil))), nil)))])
apply(kl_declare, [symdic.symdic_kl_pr, Cons(symdic.symdic_kl_string, Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(Cons(symdic.symdic_kl_stream, Cons(symdic.symdic_kl_out, nil)), Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_string, nil))), nil)))])
apply(kl_declare, [symdic.symdic_kl_print, Cons(symdic.symdic_A, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_A, nil)))])
apply(kl_declare, [symdic.symdic_kl_profile, Cons(Cons(symdic.symdic_A, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_B, nil))), Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(symdic.symdic_A, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_B, nil))), nil)))])
apply(kl_declare, [symdic.symdic_kl_preclude, Cons(Cons(symdic.symdic_kl_list, Cons(symdic.symdic_kl_symbol, nil)), Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(symdic.symdic_kl_list, Cons(symdic.symdic_kl_symbol, nil)), nil)))])
apply(kl_declare, [symdic.symdic_shen_procx45nl, Cons(symdic.symdic_kl_string, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_string, nil)))])
apply(kl_declare, [symdic.symdic_kl_profilex45results, Cons(symdic.symdic_A, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_symbol, nil)))])
apply(kl_declare, [symdic.symdic_kl_protect, Cons(symdic.symdic_kl_symbol, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_symbol, nil)))])
apply(kl_declare, [symdic.symdic_kl_precludex45allx45but, Cons(Cons(symdic.symdic_kl_list, Cons(symdic.symdic_kl_symbol, nil)), Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(symdic.symdic_kl_list, Cons(symdic.symdic_kl_symbol, nil)), nil)))])
apply(kl_declare, [symdic.symdic_shen_prhush, Cons(symdic.symdic_kl_string, Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(Cons(symdic.symdic_kl_stream, Cons(symdic.symdic_kl_out, nil)), Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_string, nil))), nil)))])
apply(kl_declare, [symdic.symdic_kl_ps, Cons(symdic.symdic_kl_symbol, Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(symdic.symdic_kl_list, Cons(symdic.symdic_kl_unit, nil)), nil)))])
apply(kl_declare, [symdic.symdic_kl_readx45byte, Cons(Cons(symdic.symdic_kl_stream, Cons(symdic.symdic_kl_in, nil)), Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_number, nil)))])
apply(kl_declare, [symdic.symdic_kl_readx45filex45asx45bytelist, Cons(symdic.symdic_kl_string, Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(symdic.symdic_kl_list, Cons(symdic.symdic_kl_number, nil)), nil)))])
apply(kl_declare, [symdic.symdic_kl_readx45filex45asx45string, Cons(symdic.symdic_kl_string, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_string, nil)))])
apply(kl_declare, [symdic.symdic_kl_readx45file, Cons(symdic.symdic_kl_string, Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(symdic.symdic_kl_list, Cons(symdic.symdic_kl_unit, nil)), nil)))])
apply(kl_declare, [symdic.symdic_kl_readx45fromx45string, Cons(symdic.symdic_kl_string, Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(symdic.symdic_kl_list, Cons(symdic.symdic_kl_unit, nil)), nil)))])
apply(kl_declare, [symdic.symdic_kl_remove, Cons(symdic.symdic_A, Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(Cons(symdic.symdic_kl_list, Cons(symdic.symdic_A, nil)), Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(symdic.symdic_kl_list, Cons(symdic.symdic_A, nil)), nil))), nil)))])
apply(kl_declare, [symdic.symdic_kl_reverse, Cons(Cons(symdic.symdic_kl_list, Cons(symdic.symdic_A, nil)), Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(symdic.symdic_kl_list, Cons(symdic.symdic_A, nil)), nil)))])
apply(kl_declare, [symdic.symdic_kl_simplex45error, Cons(symdic.symdic_kl_string, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_A, nil)))])
apply(kl_declare, [symdic.symdic_kl_snd, Cons(Cons(symdic.symdic_A, Cons(symdic.symdic_kl_x42, Cons(symdic.symdic_B, nil))), Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_B, nil)))])
apply(kl_declare, [symdic.symdic_kl_specialise, Cons(symdic.symdic_kl_symbol, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_symbol, nil)))])
apply(kl_declare, [symdic.symdic_kl_spy, Cons(symdic.symdic_kl_symbol, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_boolean, nil)))])
apply(kl_declare, [symdic.symdic_kl_step, Cons(symdic.symdic_kl_symbol, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_boolean, nil)))])
apply(kl_declare, [symdic.symdic_kl_stinput, Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(symdic.symdic_kl_stream, Cons(symdic.symdic_kl_in, nil)), nil))])
apply(kl_declare, [symdic.symdic_kl_stoutput, Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(symdic.symdic_kl_stream, Cons(symdic.symdic_kl_out, nil)), nil))])
apply(kl_declare, [symdic.symdic_kl_stringx63, Cons(symdic.symdic_A, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_boolean, nil)))])
apply(kl_declare, [symdic.symdic_kl_str, Cons(symdic.symdic_A, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_string, nil)))])
apply(kl_declare, [symdic.symdic_kl_stringx45x62n, Cons(symdic.symdic_kl_string, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_number, nil)))])
apply(kl_declare, [symdic.symdic_kl_stringx45x62symbol, Cons(symdic.symdic_kl_string, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_symbol, nil)))])
apply(kl_declare, [symdic.symdic_shen_sum, Cons(Cons(symdic.symdic_kl_list, Cons(symdic.symdic_kl_number, nil)), Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_number, nil)))])
apply(kl_declare, [symdic.symdic_kl_symbolx63, Cons(symdic.symdic_A, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_boolean, nil)))])
apply(kl_declare, [symdic.symdic_kl_systemf, Cons(symdic.symdic_kl_symbol, Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(symdic.symdic_kl_list, Cons(symdic.symdic_kl_symbol, nil)), nil)))])
apply(kl_declare, [symdic.symdic_kl_tail, Cons(Cons(symdic.symdic_kl_list, Cons(symdic.symdic_A, nil)), Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(symdic.symdic_kl_list, Cons(symdic.symdic_A, nil)), nil)))])
apply(kl_declare, [symdic.symdic_kl_tlstr, Cons(symdic.symdic_kl_string, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_string, nil)))])
apply(kl_declare, [symdic.symdic_kl_tlv, Cons(Cons(symdic.symdic_kl_vector, Cons(symdic.symdic_A, nil)), Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(symdic.symdic_kl_vector, Cons(symdic.symdic_A, nil)), nil)))])
apply(kl_declare, [symdic.symdic_kl_tc, Cons(symdic.symdic_kl_symbol, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_boolean, nil)))])
apply(kl_declare, [symdic.symdic_kl_tcx63, Cons(symdic.symdic_A, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_boolean, nil)))])
apply(kl_declare, [symdic.symdic_kl_thaw, Cons(Cons(symdic.symdic_kl_lazy, Cons(symdic.symdic_A, nil)), Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_A, nil)))])
apply(kl_declare, [symdic.symdic_kl_track, Cons(symdic.symdic_kl_symbol, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_symbol, nil)))])
apply(kl_declare, [symdic.symdic_kl_trapx45error, Cons(symdic.symdic_A, Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(Cons(symdic.symdic_kl_exception, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_A, nil))), Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_A, nil))), nil)))])
apply(kl_declare, [symdic.symdic_shen_truncate, Cons(symdic.symdic_kl_string, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_string, nil)))])
apply(kl_declare, [symdic.symdic_kl_tuplex63, Cons(symdic.symdic_A, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_boolean, nil)))])
apply(kl_declare, [symdic.symdic_kl_undefmacro, Cons(symdic.symdic_kl_symbol, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_symbol, nil)))])
apply(kl_declare, [symdic.symdic_kl_union, Cons(Cons(symdic.symdic_kl_list, Cons(symdic.symdic_A, nil)), Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(Cons(symdic.symdic_kl_list, Cons(symdic.symdic_A, nil)), Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(symdic.symdic_kl_list, Cons(symdic.symdic_A, nil)), nil))), nil)))])
apply(kl_declare, [symdic.symdic_kl_unprofile, Cons(Cons(symdic.symdic_A, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_B, nil))), Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(symdic.symdic_A, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_B, nil))), nil)))])
apply(kl_declare, [symdic.symdic_kl_untrack, Cons(symdic.symdic_kl_symbol, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_symbol, nil)))])
apply(kl_declare, [symdic.symdic_kl_unspecialise, Cons(symdic.symdic_kl_symbol, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_symbol, nil)))])
apply(kl_declare, [symdic.symdic_kl_variablex63, Cons(symdic.symdic_A, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_boolean, nil)))])
apply(kl_declare, [symdic.symdic_kl_vectorx63, Cons(symdic.symdic_A, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_boolean, nil)))])
apply(kl_declare, [symdic.symdic_kl_version, Cons(symdic.symdic_kl_string, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_string, nil)))])
apply(kl_declare, [symdic.symdic_kl_writex45tox45file, Cons(symdic.symdic_kl_string, Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(symdic.symdic_A, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_A, nil))), nil)))])
apply(kl_declare, [symdic.symdic_kl_yx45orx45nx63, Cons(symdic.symdic_kl_string, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_boolean, nil)))])
apply(kl_declare, [symdic.symdic_kl_x62, Cons(symdic.symdic_kl_number, Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(symdic.symdic_kl_number, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_boolean, nil))), nil)))])
apply(kl_declare, [symdic.symdic_kl_x60, Cons(symdic.symdic_kl_number, Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(symdic.symdic_kl_number, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_boolean, nil))), nil)))])
apply(kl_declare, [symdic.symdic_kl_x62x61, Cons(symdic.symdic_kl_number, Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(symdic.symdic_kl_number, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_boolean, nil))), nil)))])
apply(kl_declare, [symdic.symdic_kl_x60x61, Cons(symdic.symdic_kl_number, Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(symdic.symdic_kl_number, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_boolean, nil))), nil)))])
apply(kl_declare, [symdic.symdic_kl_x61, Cons(symdic.symdic_A, Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(symdic.symdic_A, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_boolean, nil))), nil)))])
apply(kl_declare, [symdic.symdic_kl_x43, Cons(symdic.symdic_kl_number, Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(symdic.symdic_kl_number, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_number, nil))), nil)))])
apply(kl_declare, [symdic.symdic_kl_x47, Cons(symdic.symdic_kl_number, Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(symdic.symdic_kl_number, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_number, nil))), nil)))])
apply(kl_declare, [symdic.symdic_kl_x45, Cons(symdic.symdic_kl_number, Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(symdic.symdic_kl_number, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_number, nil))), nil)))])
apply(kl_declare, [symdic.symdic_kl_x42, Cons(symdic.symdic_kl_number, Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(symdic.symdic_kl_number, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_number, nil))), nil)))])
apply(kl_declare, [symdic.symdic_kl_x61x61, Cons(symdic.symdic_A, Cons(symdic.symdic_kl_x45x45x62, Cons(Cons(symdic.symdic_B, Cons(symdic.symdic_kl_x45x45x62, Cons(symdic.symdic_kl_boolean, nil))), nil)))])
# included at the end of shen.py

def shen_expt(KL_ARG_V1518_757, KL_ARG_V1519_758):
    KL_ARG_V1518_757, KL_ARG_V1519_758 = float(KL_ARG_V1518_757), float(KL_ARG_V1519_758)
    return (1 if (0 == KL_ARG_V1519_758) else ((KL_ARG_V1518_757 * tco_apply(shen_expt, [KL_ARG_V1518_757, (KL_ARG_V1519_758 - 1)])) if (KL_ARG_V1519_758 > 0) else ((1 * (tco_apply(shen_expt, [KL_ARG_V1518_757, (KL_ARG_V1519_758 + 1)]) / KL_ARG_V1518_757)) if True else shen_simple_error('condition failure'))))

def kl_booleanx63(KL_ARG_V1857_1068):
    if isinstance(KL_ARG_V1857_1068, Sym) and (KL_ARG_V1857_1068.sym == "true" or KL_ARG_V1857_1068.sym == "false"):
        return True
    else:
        return (True if (True == KL_ARG_V1857_1068) else (True if (False == KL_ARG_V1857_1068) else (False if True else shen_simple_error('condition failure'))))

