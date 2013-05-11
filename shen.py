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
    symdic_kl_number = Sym('number')
    symdic_shen_linearise_help = Sym('shen.linearise_help')
    symdic_shen_explodex45h = Sym('shen.explode-h')
    symdic_kl_tl = Sym('tl')
    symdic_shen_curryx45type = Sym('shen.curry-type')
    symdic_kl_adjoin = Sym('adjoin')
    symdic_shen_yacc = Sym('shen.yacc')
    symdic_kl_include = Sym('include')
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
    symdic_shen_split_cc_rules = Sym('shen.split_cc_rules')
    symdic_shen_cc_body = Sym('shen.cc_body')
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
    symdic_shen_prologx45aritycheck = Sym('shen.prolog-aritycheck')
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
    symdic_shen_mapx45h = Sym('shen.map-h')
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
    symdic_shen_incinfs = Sym('shen.incinfs')
    symdic_shen_defprologx45macro = Sym('shen.defprolog-macro')
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
    symdic_shen_product = Sym('shen.product')
    symdic_shen_makex45stringx45macro = Sym('shen.make-string-macro')
    symdic_shen_to = Sym('shen.to')
    symdic_Y = Sym('Y')
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
    symdic_shen_mu = Sym('shen.mu')
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
    symdic_kl_when = Sym('when')
    symdic_kl_stringx63 = Sym('string?')
    symdic_kl_absvectorx63 = Sym('absvector?')
    symdic_shen_x42maxcomplexityx42 = Sym('shen.*maxcomplexity*')
    symdic_shen_rememberx45datatype = Sym('shen.remember-datatype')
    symdic_kl_x42maximumx45printx45sequencex45sizex42 = Sym('*maximum-print-sequence-size*')
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
VARS.update({'*language*': 'Python', '*implementation*': 'pyshen', '*release*': 10, '*port*': 0.135, '*porters*': 'Matthieu Lagacherie, Yannick Drant', '*home-directory*': '~/', '*stinput*': sys.stdin, '*stoutput*': sys.stdout, '*version*': 0.1})


#============================== toplevel.kl==============================



@tail_recursion
def shen_shen():
    global symdic
    return [tco_apply(shen_credits, []), tail_call(shen_loop, [])][(-1)]
shen_add_fun('shen.shen', shen_shen)

@tail_recursion
def shen_loop():
    global symdic
    return [tco_apply(shen_initialise_environment, []), [tco_apply(shen_prompt, []), [shen_try_except((lambda : tco_apply(shen_readx45evaluatex45print, [])), (lambda KL_ARG_E_0: shen_pr(KL_ARG_E_0.message, tco_apply(kl_stoutput, [])))), tail_call(shen_loop, [])][(-1)]][(-1)]][(-1)]
shen_add_fun('shen.loop', shen_loop)

@tail_recursion
def kl_version(KL_ARG_V2247_1):
    global symdic
    return shen_set(symdic.symdic_kl_x42versionx42, KL_ARG_V2247_1)
shen_add_fun('version', kl_version)
tail_call(kl_version, ['version 9.2'])

@tail_recursion
def shen_credits():
    global symdic
    return [shen_pr('\r\nShen 2010, copyright (C) 2010 Mark Tarver\r\n', tco_apply(kl_stoutput, [])), [shen_pr(('www.shenlanguage.org, ' + tco_apply(shen_app, [shen_get(symdic.symdic_kl_x42versionx42), '\r\n', symdic.symdic_shen_a])), tco_apply(kl_stoutput, [])), [shen_pr(('running under ' + tco_apply(shen_app, [shen_get(symdic.symdic_kl_x42languagex42), (', implementation: ' + tco_apply(shen_app, [shen_get(symdic.symdic_kl_x42implementationx42), '', symdic.symdic_shen_a])), symdic.symdic_shen_a])), tco_apply(kl_stoutput, [])), shen_pr(('\r\nport ' + tco_apply(shen_app, [shen_get(symdic.symdic_kl_x42portx42), (' ported by ' + tco_apply(shen_app, [shen_get(symdic.symdic_kl_x42portersx42), '\r\n', symdic.symdic_shen_a])), symdic.symdic_shen_a])), tco_apply(kl_stoutput, []))][(-1)]][(-1)]][(-1)]
shen_add_fun('shen.credits', shen_credits)

@tail_recursion
def shen_initialise_environment():
    global symdic
    return tail_call(shen_multiplex45set, [[symdic.symdic_shen_x42callx42, [0, [symdic.symdic_shen_x42infsx42, [0, [symdic.symdic_shen_x42processx45counterx42, [0, [symdic.symdic_shen_x42catchx42, [0, []]]]]]]]]])
shen_add_fun('shen.initialise_environment', shen_initialise_environment)

@tail_recursion
def shen_multiplex45set(KL_ARG_V2248_2):
    global symdic
    return ([] if shen_eq([], KL_ARG_V2248_2) else ([shen_set(KL_ARG_V2248_2[0], KL_ARG_V2248_2[1][0]), tail_call(shen_multiplex45set, [KL_ARG_V2248_2[1][1]])][(-1)] if (shen_consp(KL_ARG_V2248_2) and shen_consp(KL_ARG_V2248_2[1])) else (tail_call(shen_sysx45error, [symdic.symdic_shen_multiplex45set]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.multiple-set', shen_multiplex45set)

@tail_recursion
def kl_destroy(KL_ARG_V2249_3):
    global symdic
    return apply(kl_declare, [KL_ARG_V2249_3, []])
shen_add_fun('destroy', kl_destroy)
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
shen_add_fun('shen.read-evaluate-print', shen_readx45evaluatex45print)

@tail_recursion
def shen_retrievex45fromx45historyx45ifx45needed(KL_ARG_V2259_9, KL_ARG_V2260_10):

    class KL_Context:
        KL_LOC_PastPrint_11 = None
        KL_LOC_Keyx63_12 = None
        KL_LOC_Find_13 = None
        KL_LOC_PastPrint_14 = None
        KL_LOC_Keyx63_16 = None
        KL_LOC_Pastprint_17 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_PastPrint_11', tco_apply(shen_prbytes, [tco_apply(kl_snd, [KL_ARG_V2260_10[0]])])), KL_ARG_V2260_10[0]][(-1)] if (tco_apply(kl_tuplex63, [KL_ARG_V2259_9]) and (shen_consp(tco_apply(kl_snd, [KL_ARG_V2259_9])) and (shen_consp(tco_apply(kl_snd, [KL_ARG_V2259_9])[1]) and (shen_eq([], tco_apply(kl_snd, [KL_ARG_V2259_9])[1][1]) and (shen_consp(KL_ARG_V2260_10) and (shen_eq(tco_apply(kl_snd, [KL_ARG_V2259_9])[0], tco_apply(shen_exclamation, [])) and shen_eq(tco_apply(kl_snd, [KL_ARG_V2259_9])[1][0], tco_apply(shen_exclamation, [])))))))) else ([setattr(KL_CTX, 'KL_LOC_Keyx63_12', tco_apply(shen_makex45key, [tco_apply(kl_snd, [KL_ARG_V2259_9])[1], KL_ARG_V2260_10])), [setattr(KL_CTX, 'KL_LOC_Find_13', tco_apply(kl_head, [tco_apply(shen_findx45pastx45inputs, [KL_CTX.KL_LOC_Keyx63_12, KL_ARG_V2260_10])])), [setattr(KL_CTX, 'KL_LOC_PastPrint_14', tco_apply(shen_prbytes, [tco_apply(kl_snd, [KL_CTX.KL_LOC_Find_13])])), KL_CTX.KL_LOC_Find_13][(-1)]][(-1)]][(-1)] if (tco_apply(kl_tuplex63, [KL_ARG_V2259_9]) and (shen_consp(tco_apply(kl_snd, [KL_ARG_V2259_9])) and shen_eq(tco_apply(kl_snd, [KL_ARG_V2259_9])[0], tco_apply(shen_exclamation, [])))) else ([tco_apply(shen_printx45pastx45inputs, [(lambda KL_ARG_X_15: True), tco_apply(kl_reverse, [KL_ARG_V2260_10]), 0]), tail_call(kl_abort, [])][(-1)] if (tco_apply(kl_tuplex63, [KL_ARG_V2259_9]) and (shen_consp(tco_apply(kl_snd, [KL_ARG_V2259_9])) and (shen_eq([], tco_apply(kl_snd, [KL_ARG_V2259_9])[1]) and shen_eq(tco_apply(kl_snd, [KL_ARG_V2259_9])[0], tco_apply(shen_percent, []))))) else ([setattr(KL_CTX, 'KL_LOC_Keyx63_16', tco_apply(shen_makex45key, [tco_apply(kl_snd, [KL_ARG_V2259_9])[1], KL_ARG_V2260_10])), [setattr(KL_CTX, 'KL_LOC_Pastprint_17', tco_apply(shen_printx45pastx45inputs, [KL_CTX.KL_LOC_Keyx63_16, tco_apply(kl_reverse, [KL_ARG_V2260_10]), 0])), tail_call(kl_abort, [])][(-1)]][(-1)] if (tco_apply(kl_tuplex63, [KL_ARG_V2259_9]) and (shen_consp(tco_apply(kl_snd, [KL_ARG_V2259_9])) and shen_eq(tco_apply(kl_snd, [KL_ARG_V2259_9])[0], tco_apply(shen_percent, [])))) else (KL_ARG_V2259_9 if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.retrieve-from-history-if-needed', shen_retrievex45fromx45historyx45ifx45needed)

@tail_recursion
def shen_percent():
    global symdic
    return 37
shen_add_fun('shen.percent', shen_percent)

@tail_recursion
def shen_exclamation():
    global symdic
    return 33
shen_add_fun('shen.exclamation', shen_exclamation)

@tail_recursion
def shen_prbytes(KL_ARG_V2261_18):
    global symdic
    return [tco_apply(kl_map, [(lambda KL_ARG_Byte_19: shen_pr(chr(KL_ARG_Byte_19), tco_apply(kl_stoutput, []))), KL_ARG_V2261_18]), tail_call(kl_nl, [1])][(-1)]
shen_add_fun('shen.prbytes', shen_prbytes)

@tail_recursion
def shen_update_history(KL_ARG_V2262_20, KL_ARG_V2263_21):
    global symdic
    return shen_set(symdic.symdic_shen_x42historyx42, [KL_ARG_V2262_20, KL_ARG_V2263_21])
shen_add_fun('shen.update_history', shen_update_history)

@tail_recursion
def shen_toplineread():
    global symdic
    return tail_call(shen_toplineread_loop, [shen_read_byte(tco_apply(kl_stinput, [])), []])
shen_add_fun('shen.toplineread', shen_toplineread)

@tail_recursion
def shen_toplineread_loop(KL_ARG_V2265_22, KL_ARG_V2266_23):

    class KL_Context:
        KL_LOC_Line_24 = None
    KL_CTX = KL_Context()
    global symdic
    return (shen_simple_error('line read aborted') if shen_eq(KL_ARG_V2265_22, tco_apply(shen_hat, [])) else ([setattr(KL_CTX, 'KL_LOC_Line_24', tco_apply(kl_compile, [symdic.symdic_shen_x60st_inputx62, KL_ARG_V2266_23, (lambda KL_ARG_E_25: symdic.symdic_shen_nextline)])), (tail_call(shen_toplineread_loop, [shen_read_byte(tco_apply(kl_stinput, [])), tco_apply(kl_append, [KL_ARG_V2266_23, [KL_ARG_V2265_22, []]])]) if (shen_eq(KL_CTX.KL_LOC_Line_24, symdic.symdic_shen_nextline) or tco_apply(kl_emptyx63, [KL_CTX.KL_LOC_Line_24])) else tail_call(kl_x64p, [KL_CTX.KL_LOC_Line_24, KL_ARG_V2266_23]))][(-1)] if tco_apply(kl_elementx63, [KL_ARG_V2265_22, [tco_apply(shen_newline, []), [tco_apply(shen_carriagex45return, []), []]]]) else (tail_call(shen_toplineread_loop, [shen_read_byte(tco_apply(kl_stinput, [])), tco_apply(kl_append, [KL_ARG_V2266_23, [KL_ARG_V2265_22, []]])]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.toplineread_loop', shen_toplineread_loop)

@tail_recursion
def shen_hat():
    global symdic
    return 94
shen_add_fun('shen.hat', shen_hat)

@tail_recursion
def shen_newline():
    global symdic
    return 10
shen_add_fun('shen.newline', shen_newline)

@tail_recursion
def shen_carriagex45return():
    global symdic
    return 13
shen_add_fun('shen.carriage-return', shen_carriagex45return)

@tail_recursion
def kl_tc(KL_ARG_V2271_26):
    global symdic
    return (shen_set(symdic.symdic_shen_x42tcx42, True) if shen_eq(symdic.symdic_kl_x43, KL_ARG_V2271_26) else (shen_set(symdic.symdic_shen_x42tcx42, False) if shen_eq(symdic.symdic_kl_x45, KL_ARG_V2271_26) else (shen_simple_error('tc expects a + or -') if True else shen_simple_error('condition failure'))))
shen_add_fun('tc', kl_tc)

@tail_recursion
def shen_prompt():
    global symdic
    return (shen_pr(('\r\n\r\n(' + tco_apply(shen_app, [tco_apply(kl_length, [shen_get(symdic.symdic_shen_x42historyx42)]), '+) ', symdic.symdic_shen_a])), tco_apply(kl_stoutput, [])) if shen_get(symdic.symdic_shen_x42tcx42) else shen_pr(('\r\n\r\n(' + tco_apply(shen_app, [tco_apply(kl_length, [shen_get(symdic.symdic_shen_x42historyx42)]), '-) ', symdic.symdic_shen_a])), tco_apply(kl_stoutput, [])))
shen_add_fun('shen.prompt', shen_prompt)

@tail_recursion
def shen_toplevel(KL_ARG_V2272_27):
    global symdic
    return tail_call(shen_toplevel_evaluate, [KL_ARG_V2272_27, shen_get(symdic.symdic_shen_x42tcx42)])
shen_add_fun('shen.toplevel', shen_toplevel)

@tail_recursion
def shen_findx45pastx45inputs(KL_ARG_V2273_28, KL_ARG_V2274_29):

    class KL_Context:
        KL_LOC_F_30 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_F_30', tco_apply(shen_find, [KL_ARG_V2273_28, KL_ARG_V2274_29])), (shen_simple_error('input not found\r\n') if tco_apply(kl_emptyx63, [KL_CTX.KL_LOC_F_30]) else KL_CTX.KL_LOC_F_30)][(-1)]
shen_add_fun('shen.find-past-inputs', shen_findx45pastx45inputs)

@tail_recursion
def shen_makex45key(KL_ARG_V2275_31, KL_ARG_V2276_32):

    class KL_Context:
        KL_LOC_Atom_33 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Atom_33', tco_apply(kl_compile, [symdic.symdic_shen_x60st_inputx62, KL_ARG_V2275_31, (lambda KL_ARG_E_34: (shen_simple_error(('parse error here: ' + tco_apply(shen_app, [KL_ARG_E_34, '\r\n', symdic.symdic_shen_s]))) if shen_consp(KL_ARG_E_34) else shen_simple_error('parse error\r\n')))])[0]), ((lambda KL_ARG_X_35: shen_eq(KL_ARG_X_35, tco_apply(kl_nth, [(KL_CTX.KL_LOC_Atom_33 + 1), tco_apply(kl_reverse, [KL_ARG_V2276_32])]))) if tco_apply(kl_integerx63, [KL_CTX.KL_LOC_Atom_33]) else (lambda KL_ARG_X_36: tail_call(shen_prefixx63, [KL_ARG_V2275_31, tco_apply(shen_trimx45gubbins, [tco_apply(kl_snd, [KL_ARG_X_36])])])))][(-1)]
shen_add_fun('shen.make-key', shen_makex45key)

@tail_recursion
def shen_trimx45gubbins(KL_ARG_V2277_37):
    global symdic
    return (tail_call(shen_trimx45gubbins, [KL_ARG_V2277_37[1]]) if (shen_consp(KL_ARG_V2277_37) and shen_eq(KL_ARG_V2277_37[0], tco_apply(shen_space, []))) else (tail_call(shen_trimx45gubbins, [KL_ARG_V2277_37[1]]) if (shen_consp(KL_ARG_V2277_37) and shen_eq(KL_ARG_V2277_37[0], tco_apply(shen_newline, []))) else (tail_call(shen_trimx45gubbins, [KL_ARG_V2277_37[1]]) if (shen_consp(KL_ARG_V2277_37) and shen_eq(KL_ARG_V2277_37[0], tco_apply(shen_carriagex45return, []))) else (tail_call(shen_trimx45gubbins, [KL_ARG_V2277_37[1]]) if (shen_consp(KL_ARG_V2277_37) and shen_eq(KL_ARG_V2277_37[0], tco_apply(shen_tab, []))) else (tail_call(shen_trimx45gubbins, [KL_ARG_V2277_37[1]]) if (shen_consp(KL_ARG_V2277_37) and shen_eq(KL_ARG_V2277_37[0], tco_apply(shen_leftx45round, []))) else (KL_ARG_V2277_37 if True else shen_simple_error('condition failure')))))))
shen_add_fun('shen.trim-gubbins', shen_trimx45gubbins)

@tail_recursion
def shen_space():
    global symdic
    return 32
shen_add_fun('shen.space', shen_space)

@tail_recursion
def shen_tab():
    global symdic
    return 9
shen_add_fun('shen.tab', shen_tab)

@tail_recursion
def shen_leftx45round():
    global symdic
    return 40
shen_add_fun('shen.left-round', shen_leftx45round)

@tail_recursion
def shen_find(KL_ARG_V2284_38, KL_ARG_V2285_39):
    global symdic
    return ([] if shen_eq([], KL_ARG_V2285_39) else ([KL_ARG_V2285_39[0], tco_apply(shen_find, [KL_ARG_V2284_38, KL_ARG_V2285_39[1]])] if (shen_consp(KL_ARG_V2285_39) and shen_apply(KL_ARG_V2284_38, [KL_ARG_V2285_39[0]])) else (tail_call(shen_find, [KL_ARG_V2284_38, KL_ARG_V2285_39[1]]) if shen_consp(KL_ARG_V2285_39) else (tail_call(shen_sysx45error, [symdic.symdic_shen_find]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.find', shen_find)

@tail_recursion
def shen_prefixx63(KL_ARG_V2296_40, KL_ARG_V2297_41):
    global symdic
    return (True if shen_eq([], KL_ARG_V2296_40) else (tail_call(shen_prefixx63, [KL_ARG_V2296_40[1], KL_ARG_V2297_41[1]]) if (shen_consp(KL_ARG_V2296_40) and (shen_consp(KL_ARG_V2297_41) and shen_eq(KL_ARG_V2297_41[0], KL_ARG_V2296_40[0]))) else (False if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.prefix?', shen_prefixx63)

@tail_recursion
def shen_printx45pastx45inputs(KL_ARG_V2307_42, KL_ARG_V2308_43, KL_ARG_V2309_44):
    global symdic
    return (symdic.symdic_kl__ if shen_eq([], KL_ARG_V2308_43) else (tail_call(shen_printx45pastx45inputs, [KL_ARG_V2307_42, KL_ARG_V2308_43[1], (KL_ARG_V2309_44 + 1)]) if (shen_consp(KL_ARG_V2308_43) and (not shen_apply(KL_ARG_V2307_42, [KL_ARG_V2308_43[0]]))) else ([shen_pr(tco_apply(shen_app, [KL_ARG_V2309_44, '. ', symdic.symdic_shen_a]), tco_apply(kl_stoutput, [])), [tco_apply(shen_prbytes, [tco_apply(kl_snd, [KL_ARG_V2308_43[0]])]), tail_call(shen_printx45pastx45inputs, [KL_ARG_V2307_42, KL_ARG_V2308_43[1], (KL_ARG_V2309_44 + 1)])][(-1)]][(-1)] if (shen_consp(KL_ARG_V2308_43) and tco_apply(kl_tuplex63, [KL_ARG_V2308_43[0]])) else (tail_call(shen_sysx45error, [symdic.symdic_shen_printx45pastx45inputs]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.print-past-inputs', shen_printx45pastx45inputs)

@tail_recursion
def shen_toplevel_evaluate(KL_ARG_V2310_45, KL_ARG_V2311_46):

    class KL_Context:
        KL_LOC_Eval_47 = None
    KL_CTX = KL_Context()
    global symdic
    return (tail_call(shen_typecheckx45andx45evaluate, [KL_ARG_V2310_45[0], KL_ARG_V2310_45[1][1][0]]) if (shen_consp(KL_ARG_V2310_45) and (shen_consp(KL_ARG_V2310_45[1]) and (shen_eq(symdic.symdic_kl_x58, KL_ARG_V2310_45[1][0]) and (shen_consp(KL_ARG_V2310_45[1][1]) and (shen_eq([], KL_ARG_V2310_45[1][1][1]) and shen_eq(True, KL_ARG_V2311_46)))))) else ([tco_apply(shen_toplevel_evaluate, [[KL_ARG_V2310_45[0], []], KL_ARG_V2311_46]), [tco_apply(kl_nl, [1]), tail_call(shen_toplevel_evaluate, [KL_ARG_V2310_45[1], KL_ARG_V2311_46])][(-1)]][(-1)] if (shen_consp(KL_ARG_V2310_45) and shen_consp(KL_ARG_V2310_45[1])) else (tail_call(shen_typecheckx45andx45evaluate, [KL_ARG_V2310_45[0], tco_apply(kl_gensym, [symdic.symdic_A])]) if (shen_consp(KL_ARG_V2310_45) and (shen_eq([], KL_ARG_V2310_45[1]) and shen_eq(True, KL_ARG_V2311_46))) else ([setattr(KL_CTX, 'KL_LOC_Eval_47', tco_apply(shen_evalx45withoutx45macros, [KL_ARG_V2310_45[0]])), tail_call(kl_print, [KL_CTX.KL_LOC_Eval_47])][(-1)] if (shen_consp(KL_ARG_V2310_45) and (shen_eq([], KL_ARG_V2310_45[1]) and shen_eq(False, KL_ARG_V2311_46))) else (tail_call(shen_sysx45error, [symdic.symdic_shen_toplevel_evaluate]) if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.toplevel_evaluate', shen_toplevel_evaluate)

@tail_recursion
def shen_typecheckx45andx45evaluate(KL_ARG_V2312_48, KL_ARG_V2313_49):

    class KL_Context:
        KL_LOC_Typecheck_50 = None
        KL_LOC_Eval_51 = None
        KL_LOC_Type_52 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Typecheck_50', tco_apply(shen_typecheck, [KL_ARG_V2312_48, KL_ARG_V2313_49])), (shen_simple_error('type error\r\n') if shen_eq(KL_CTX.KL_LOC_Typecheck_50, False) else [setattr(KL_CTX, 'KL_LOC_Eval_51', tco_apply(shen_evalx45withoutx45macros, [KL_ARG_V2312_48])), [setattr(KL_CTX, 'KL_LOC_Type_52', tco_apply(shen_prettyx45type, [KL_CTX.KL_LOC_Typecheck_50])), shen_pr(tco_apply(shen_app, [KL_CTX.KL_LOC_Eval_51, (' : ' + tco_apply(shen_app, [KL_CTX.KL_LOC_Type_52, '', symdic.symdic_shen_r])), symdic.symdic_shen_s]), tco_apply(kl_stoutput, []))][(-1)]][(-1)])][(-1)]
shen_add_fun('shen.typecheck-and-evaluate', shen_typecheckx45andx45evaluate)

@tail_recursion
def shen_prettyx45type(KL_ARG_V2314_53):
    global symdic
    return tail_call(shen_mult_subst, [shen_get(symdic.symdic_shen_x42alphabetx42), tco_apply(shen_extractx45pvars, [KL_ARG_V2314_53]), KL_ARG_V2314_53])
shen_add_fun('shen.pretty-type', shen_prettyx45type)

@tail_recursion
def shen_extractx45pvars(KL_ARG_V2319_54):
    global symdic
    return ([KL_ARG_V2319_54, []] if tco_apply(shen_pvarx63, [KL_ARG_V2319_54]) else (tail_call(kl_union, [tco_apply(shen_extractx45pvars, [KL_ARG_V2319_54[0]]), tco_apply(shen_extractx45pvars, [KL_ARG_V2319_54[1]])]) if shen_consp(KL_ARG_V2319_54) else ([] if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.extract-pvars', shen_extractx45pvars)

@tail_recursion
def shen_mult_subst(KL_ARG_V2324_55, KL_ARG_V2325_56, KL_ARG_V2326_57):
    global symdic
    return (KL_ARG_V2326_57 if shen_eq([], KL_ARG_V2324_55) else (KL_ARG_V2326_57 if shen_eq([], KL_ARG_V2325_56) else (tail_call(shen_mult_subst, [KL_ARG_V2324_55[1], KL_ARG_V2325_56[1], tco_apply(kl_subst, [KL_ARG_V2324_55[0], KL_ARG_V2325_56[0], KL_ARG_V2326_57])]) if (shen_consp(KL_ARG_V2324_55) and shen_consp(KL_ARG_V2325_56)) else (tail_call(shen_sysx45error, [symdic.symdic_shen_mult_subst]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.mult_subst', shen_mult_subst)


#============================== core.kl==============================



@tail_recursion
def shen_shenx45x62kl(KL_ARG_V605_58, KL_ARG_V606_59):
    global symdic
    return tail_call(kl_compile, [symdic.symdic_shen_x60definex62, [KL_ARG_V605_58, KL_ARG_V606_59], (lambda KL_ARG_X_60: tail_call(shen_shenx45syntaxx45error, [KL_ARG_V605_58, KL_ARG_X_60]))])
shen_add_fun('shen.shen->kl', shen_shenx45x62kl)

@tail_recursion
def shen_shenx45syntaxx45error(KL_ARG_V607_61, KL_ARG_V608_62):
    global symdic
    return shen_simple_error(('syntax error in ' + tco_apply(shen_app, [KL_ARG_V607_61, (' here:\r\n\r\n ' + tco_apply(shen_app, [tco_apply(shen_nextx4550, [50, KL_ARG_V608_62]), '\r\n', symdic.symdic_shen_a])), symdic.symdic_shen_a])))
shen_add_fun('shen.shen-syntax-error', shen_shenx45syntaxx45error)

@tail_recursion
def shen_x60definex62(KL_ARG_V613_63):

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
    return [setattr(KL_CTX, 'KL_LOC_Result_64', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60namex62_65', tco_apply(shen_x60namex62, [KL_ARG_V613_63])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60signaturex62_66', tco_apply(shen_x60signaturex62, [KL_CTX.KL_LOC_Parse_shen_x60namex62_65])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60rulesx62_67', tco_apply(shen_x60rulesx62, [KL_CTX.KL_LOC_Parse_shen_x60signaturex62_66])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60rulesx62_67[0], tco_apply(shen_compile_to_machine_code, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60namex62_65]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60rulesx62_67])])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60rulesx62_67)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60signaturex62_66)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60namex62_65)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_68', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60namex62_69', tco_apply(shen_x60namex62, [KL_ARG_V613_63])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60rulesx62_70', tco_apply(shen_x60rulesx62, [KL_CTX.KL_LOC_Parse_shen_x60namex62_69])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60rulesx62_70[0], tco_apply(shen_compile_to_machine_code, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60namex62_69]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60rulesx62_70])])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60rulesx62_70)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60namex62_69)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_68, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_68)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_64, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_64)][(-1)]
shen_add_fun('shen.<define>', shen_x60definex62)

@tail_recursion
def shen_x60namex62(KL_ARG_V618_71):

    class KL_Context:
        KL_LOC_Result_72 = None
        KL_LOC_Parse_X_73 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_72', ([setattr(KL_CTX, 'KL_LOC_Parse_X_73', KL_ARG_V618_71[0][0]), tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V618_71[0][1], tco_apply(shen_hdtl, [KL_ARG_V618_71])])[0], (KL_CTX.KL_LOC_Parse_X_73 if (tco_apply(kl_symbolx63, [KL_CTX.KL_LOC_Parse_X_73]) and (not tco_apply(shen_sysfuncx63, [KL_CTX.KL_LOC_Parse_X_73]))) else shen_simple_error(tco_apply(shen_app, [KL_CTX.KL_LOC_Parse_X_73, ' is not a legitimate function name.\r\n', symdic.symdic_shen_a])))])][(-1)] if shen_consp(KL_ARG_V618_71[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_72, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_72)][(-1)]
shen_add_fun('shen.<name>', shen_x60namex62)

@tail_recursion
def shen_sysfuncx63(KL_ARG_V619_74):
    global symdic
    return tail_call(kl_elementx63, [KL_ARG_V619_74, tco_apply(kl_get, [shen_intern('shen'), symdic.symdic_shen_externalx45symbols, shen_get(symdic.symdic_kl_x42propertyx45vectorx42)])])
shen_add_fun('shen.sysfunc?', shen_sysfuncx63)

@tail_recursion
def shen_x60signaturex62(KL_ARG_V624_75):

    class KL_Context:
        KL_LOC_Result_76 = None
        KL_LOC_Parse_shen_x60signaturex45helpx62_77 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_76', ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60signaturex45helpx62_77', tco_apply(shen_x60signaturex45helpx62, [tco_apply(shen_pair, [KL_ARG_V624_75[0][1], tco_apply(shen_hdtl, [KL_ARG_V624_75])])])), ((tco_apply(shen_pair, [tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60signaturex45helpx62_77[0][1], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60signaturex45helpx62_77])])[0], tco_apply(shen_demodulate, [tco_apply(shen_curryx45type, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60signaturex45helpx62_77])])])]) if (shen_consp(KL_CTX.KL_LOC_Parse_shen_x60signaturex45helpx62_77[0]) and shen_eq(symdic.symdic_kl_x125, KL_CTX.KL_LOC_Parse_shen_x60signaturex45helpx62_77[0][0])) else tco_apply(kl_fail, [])) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60signaturex45helpx62_77)) else tco_apply(kl_fail, []))][(-1)] if (shen_consp(KL_ARG_V624_75[0]) and shen_eq(symdic.symdic_kl_x123, KL_ARG_V624_75[0][0])) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_76, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_76)][(-1)]
shen_add_fun('shen.<signature>', shen_x60signaturex62)

@tail_recursion
def shen_curryx45type(KL_ARG_V627_78):
    global symdic
    return (tail_call(shen_curryx45type, [[KL_ARG_V627_78[0], [symdic.symdic_kl_x45x45x62, [KL_ARG_V627_78[1][1], []]]]]) if (shen_consp(KL_ARG_V627_78) and (shen_consp(KL_ARG_V627_78[1]) and (shen_eq(symdic.symdic_kl_x45x45x62, KL_ARG_V627_78[1][0]) and (shen_consp(KL_ARG_V627_78[1][1]) and (shen_consp(KL_ARG_V627_78[1][1][1]) and shen_eq(symdic.symdic_kl_x45x45x62, KL_ARG_V627_78[1][1][1][0])))))) else ([symdic.symdic_kl_list, [tco_apply(shen_curryx45type, [KL_ARG_V627_78[1][0]]), []]] if (shen_consp(KL_ARG_V627_78) and (shen_eq(symdic.symdic_kl_cons, KL_ARG_V627_78[0]) and (shen_consp(KL_ARG_V627_78[1]) and (shen_consp(KL_ARG_V627_78[1][1]) and shen_eq([], KL_ARG_V627_78[1][1][1]))))) else (tail_call(shen_curryx45type, [[KL_ARG_V627_78[0], [symdic.symdic_kl_x42, [KL_ARG_V627_78[1][1], []]]]]) if (shen_consp(KL_ARG_V627_78) and (shen_consp(KL_ARG_V627_78[1]) and (shen_eq(symdic.symdic_kl_x42, KL_ARG_V627_78[1][0]) and (shen_consp(KL_ARG_V627_78[1][1]) and (shen_consp(KL_ARG_V627_78[1][1][1]) and shen_eq(symdic.symdic_kl_x42, KL_ARG_V627_78[1][1][1][0])))))) else (tail_call(kl_map, [symdic.symdic_shen_curryx45type, KL_ARG_V627_78]) if shen_consp(KL_ARG_V627_78) else (KL_ARG_V627_78 if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.curry-type', shen_curryx45type)

@tail_recursion
def shen_x60signaturex45helpx62(KL_ARG_V632_79):

    class KL_Context:
        KL_LOC_Result_80 = None
        KL_LOC_Parse_X_81 = None
        KL_LOC_Parse_shen_x60signaturex45helpx62_82 = None
        KL_LOC_Result_83 = None
        KL_LOC_Parse_x60ex62_84 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_80', ([setattr(KL_CTX, 'KL_LOC_Parse_X_81', KL_ARG_V632_79[0][0]), [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60signaturex45helpx62_82', tco_apply(shen_x60signaturex45helpx62, [tco_apply(shen_pair, [KL_ARG_V632_79[0][1], tco_apply(shen_hdtl, [KL_ARG_V632_79])])])), ((tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60signaturex45helpx62_82[0], [KL_CTX.KL_LOC_Parse_X_81, tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60signaturex45helpx62_82])]]) if (not tco_apply(kl_elementx63, [KL_CTX.KL_LOC_Parse_X_81, [symdic.symdic_kl_x123, [symdic.symdic_kl_x125, []]]])) else tco_apply(kl_fail, [])) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60signaturex45helpx62_82)) else tco_apply(kl_fail, []))][(-1)]][(-1)] if shen_consp(KL_ARG_V632_79[0]) else tco_apply(kl_fail, []))), ([setattr(KL_CTX, 'KL_LOC_Result_83', [setattr(KL_CTX, 'KL_LOC_Parse_x60ex62_84', tco_apply(kl_x60ex62, [KL_ARG_V632_79])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_x60ex62_84[0], []]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_x60ex62_84)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_83, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_83)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_80, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_80)][(-1)]
shen_add_fun('shen.<signature-help>', shen_x60signaturex45helpx62)

@tail_recursion
def shen_x60rulesx62(KL_ARG_V637_85):

    class KL_Context:
        KL_LOC_Result_86 = None
        KL_LOC_Parse_shen_x60rulex62_87 = None
        KL_LOC_Parse_shen_x60rulesx62_88 = None
        KL_LOC_Result_89 = None
        KL_LOC_Parse_shen_x60rulex62_90 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_86', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60rulex62_87', tco_apply(shen_x60rulex62, [KL_ARG_V637_85])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60rulesx62_88', tco_apply(shen_x60rulesx62, [KL_CTX.KL_LOC_Parse_shen_x60rulex62_87])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60rulesx62_88[0], [tco_apply(shen_linearise, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60rulex62_87])]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60rulesx62_88])]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60rulesx62_88)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60rulex62_87)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_89', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60rulex62_90', tco_apply(shen_x60rulex62, [KL_ARG_V637_85])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60rulex62_90[0], [tco_apply(shen_linearise, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60rulex62_90])]), []]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60rulex62_90)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_89, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_89)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_86, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_86)][(-1)]
shen_add_fun('shen.<rules>', shen_x60rulesx62)

@tail_recursion
def shen_x60rulex62(KL_ARG_V642_91):

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
    return [setattr(KL_CTX, 'KL_LOC_Result_92', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60patternsx62_93', tco_apply(shen_x60patternsx62, [KL_ARG_V642_91])), (([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60actionx62_94', tco_apply(shen_x60actionx62, [tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_93[0][1], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_93])])])), (([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60guardx62_95', tco_apply(shen_x60guardx62, [tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60actionx62_94[0][1], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60actionx62_94])])])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60guardx62_95[0], [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_93]), [[symdic.symdic_kl_where, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60guardx62_95]), [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60actionx62_94]), []]]], []]]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60guardx62_95)) else tco_apply(kl_fail, []))][(-1)] if (shen_consp(KL_CTX.KL_LOC_Parse_shen_x60actionx62_94[0]) and shen_eq(symdic.symdic_kl_where, KL_CTX.KL_LOC_Parse_shen_x60actionx62_94[0][0])) else tco_apply(kl_fail, [])) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60actionx62_94)) else tco_apply(kl_fail, []))][(-1)] if (shen_consp(KL_CTX.KL_LOC_Parse_shen_x60patternsx62_93[0]) and shen_eq(symdic.symdic_kl_x45x62, KL_CTX.KL_LOC_Parse_shen_x60patternsx62_93[0][0])) else tco_apply(kl_fail, [])) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60patternsx62_93)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_96', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60patternsx62_97', tco_apply(shen_x60patternsx62, [KL_ARG_V642_91])), (([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60actionx62_98', tco_apply(shen_x60actionx62, [tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_97[0][1], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_97])])])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60actionx62_98[0], [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_97]), [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60actionx62_98]), []]]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60actionx62_98)) else tco_apply(kl_fail, []))][(-1)] if (shen_consp(KL_CTX.KL_LOC_Parse_shen_x60patternsx62_97[0]) and shen_eq(symdic.symdic_kl_x45x62, KL_CTX.KL_LOC_Parse_shen_x60patternsx62_97[0][0])) else tco_apply(kl_fail, [])) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60patternsx62_97)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_99', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60patternsx62_100', tco_apply(shen_x60patternsx62, [KL_ARG_V642_91])), (([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60actionx62_101', tco_apply(shen_x60actionx62, [tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_100[0][1], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_100])])])), (([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60guardx62_102', tco_apply(shen_x60guardx62, [tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60actionx62_101[0][1], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60actionx62_101])])])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60guardx62_102[0], [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_100]), [[symdic.symdic_kl_where, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60guardx62_102]), [[symdic.symdic_shen_choicepointx33, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60actionx62_101]), []]], []]]], []]]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60guardx62_102)) else tco_apply(kl_fail, []))][(-1)] if (shen_consp(KL_CTX.KL_LOC_Parse_shen_x60actionx62_101[0]) and shen_eq(symdic.symdic_kl_where, KL_CTX.KL_LOC_Parse_shen_x60actionx62_101[0][0])) else tco_apply(kl_fail, [])) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60actionx62_101)) else tco_apply(kl_fail, []))][(-1)] if (shen_consp(KL_CTX.KL_LOC_Parse_shen_x60patternsx62_100[0]) and shen_eq(symdic.symdic_kl_x60x45, KL_CTX.KL_LOC_Parse_shen_x60patternsx62_100[0][0])) else tco_apply(kl_fail, [])) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60patternsx62_100)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_103', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60patternsx62_104', tco_apply(shen_x60patternsx62, [KL_ARG_V642_91])), (([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60actionx62_105', tco_apply(shen_x60actionx62, [tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_104[0][1], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_104])])])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60actionx62_105[0], [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_104]), [[symdic.symdic_shen_choicepointx33, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60actionx62_105]), []]], []]]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60actionx62_105)) else tco_apply(kl_fail, []))][(-1)] if (shen_consp(KL_CTX.KL_LOC_Parse_shen_x60patternsx62_104[0]) and shen_eq(symdic.symdic_kl_x60x45, KL_CTX.KL_LOC_Parse_shen_x60patternsx62_104[0][0])) else tco_apply(kl_fail, [])) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60patternsx62_104)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_103, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_103)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_99, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_99)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_96, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_96)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_92, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_92)][(-1)]
shen_add_fun('shen.<rule>', shen_x60rulex62)

@tail_recursion
def shen_fail_if(KL_ARG_V643_106, KL_ARG_V644_107):
    global symdic
    return (tail_call(kl_fail, []) if shen_apply(KL_ARG_V643_106, [KL_ARG_V644_107]) else KL_ARG_V644_107)
shen_add_fun('shen.fail_if', shen_fail_if)

@tail_recursion
def shen_succeedsx63(KL_ARG_V649_108):
    global symdic
    return (False if shen_eq(KL_ARG_V649_108, tco_apply(kl_fail, [])) else (True if True else shen_simple_error('condition failure')))
shen_add_fun('shen.succeeds?', shen_succeedsx63)

@tail_recursion
def shen_x60patternsx62(KL_ARG_V654_109):

    class KL_Context:
        KL_LOC_Result_110 = None
        KL_LOC_Parse_shen_x60patternx62_111 = None
        KL_LOC_Parse_shen_x60patternsx62_112 = None
        KL_LOC_Result_113 = None
        KL_LOC_Parse_x60ex62_114 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_110', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60patternx62_111', tco_apply(shen_x60patternx62, [KL_ARG_V654_109])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60patternsx62_112', tco_apply(shen_x60patternsx62, [KL_CTX.KL_LOC_Parse_shen_x60patternx62_111])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_112[0], [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternx62_111]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_112])]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60patternsx62_112)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60patternx62_111)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_113', [setattr(KL_CTX, 'KL_LOC_Parse_x60ex62_114', tco_apply(kl_x60ex62, [KL_ARG_V654_109])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_x60ex62_114[0], []]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_x60ex62_114)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_113, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_113)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_110, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_110)][(-1)]
shen_add_fun('shen.<patterns>', shen_x60patternsx62)

@tail_recursion
def shen_x60patternx62(KL_ARG_V659_115):

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
    return [setattr(KL_CTX, 'KL_LOC_Result_116', (tco_apply(shen_sndx45orx45fail, [([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60pattern1x62_117', tco_apply(shen_x60pattern1x62, [tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V659_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V659_115])])[0][1], tco_apply(shen_hdtl, [tco_apply(shen_pair, [KL_ARG_V659_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V659_115])])])])])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60pattern2x62_118', tco_apply(shen_x60pattern2x62, [KL_CTX.KL_LOC_Parse_shen_x60pattern1x62_117])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60pattern2x62_118[0], tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V659_115[0][1], tco_apply(shen_hdtl, [KL_ARG_V659_115])])[0], [symdic.symdic_kl_x64p, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60pattern1x62_117]), [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60pattern2x62_118]), []]]]])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60pattern2x62_118)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60pattern1x62_117)) else tco_apply(kl_fail, []))][(-1)] if (shen_consp(tco_apply(shen_pair, [KL_ARG_V659_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V659_115])])[0]) and shen_eq(symdic.symdic_kl_x64p, tco_apply(shen_pair, [KL_ARG_V659_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V659_115])])[0][0])) else tco_apply(kl_fail, []))]) if (shen_consp(KL_ARG_V659_115[0]) and shen_consp(KL_ARG_V659_115[0][0])) else tco_apply(kl_fail, []))), ([setattr(KL_CTX, 'KL_LOC_Result_119', (tco_apply(shen_sndx45orx45fail, [([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60pattern1x62_120', tco_apply(shen_x60pattern1x62, [tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V659_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V659_115])])[0][1], tco_apply(shen_hdtl, [tco_apply(shen_pair, [KL_ARG_V659_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V659_115])])])])])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60pattern2x62_121', tco_apply(shen_x60pattern2x62, [KL_CTX.KL_LOC_Parse_shen_x60pattern1x62_120])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60pattern2x62_121[0], tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V659_115[0][1], tco_apply(shen_hdtl, [KL_ARG_V659_115])])[0], [symdic.symdic_kl_cons, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60pattern1x62_120]), [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60pattern2x62_121]), []]]]])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60pattern2x62_121)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60pattern1x62_120)) else tco_apply(kl_fail, []))][(-1)] if (shen_consp(tco_apply(shen_pair, [KL_ARG_V659_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V659_115])])[0]) and shen_eq(symdic.symdic_kl_cons, tco_apply(shen_pair, [KL_ARG_V659_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V659_115])])[0][0])) else tco_apply(kl_fail, []))]) if (shen_consp(KL_ARG_V659_115[0]) and shen_consp(KL_ARG_V659_115[0][0])) else tco_apply(kl_fail, []))), ([setattr(KL_CTX, 'KL_LOC_Result_122', (tco_apply(shen_sndx45orx45fail, [([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60pattern1x62_123', tco_apply(shen_x60pattern1x62, [tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V659_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V659_115])])[0][1], tco_apply(shen_hdtl, [tco_apply(shen_pair, [KL_ARG_V659_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V659_115])])])])])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60pattern2x62_124', tco_apply(shen_x60pattern2x62, [KL_CTX.KL_LOC_Parse_shen_x60pattern1x62_123])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60pattern2x62_124[0], tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V659_115[0][1], tco_apply(shen_hdtl, [KL_ARG_V659_115])])[0], [symdic.symdic_kl_x64v, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60pattern1x62_123]), [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60pattern2x62_124]), []]]]])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60pattern2x62_124)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60pattern1x62_123)) else tco_apply(kl_fail, []))][(-1)] if (shen_consp(tco_apply(shen_pair, [KL_ARG_V659_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V659_115])])[0]) and shen_eq(symdic.symdic_kl_x64v, tco_apply(shen_pair, [KL_ARG_V659_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V659_115])])[0][0])) else tco_apply(kl_fail, []))]) if (shen_consp(KL_ARG_V659_115[0]) and shen_consp(KL_ARG_V659_115[0][0])) else tco_apply(kl_fail, []))), ([setattr(KL_CTX, 'KL_LOC_Result_125', (tco_apply(shen_sndx45orx45fail, [([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60pattern1x62_126', tco_apply(shen_x60pattern1x62, [tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V659_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V659_115])])[0][1], tco_apply(shen_hdtl, [tco_apply(shen_pair, [KL_ARG_V659_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V659_115])])])])])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60pattern2x62_127', tco_apply(shen_x60pattern2x62, [KL_CTX.KL_LOC_Parse_shen_x60pattern1x62_126])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60pattern2x62_127[0], tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V659_115[0][1], tco_apply(shen_hdtl, [KL_ARG_V659_115])])[0], [symdic.symdic_kl_x64s, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60pattern1x62_126]), [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60pattern2x62_127]), []]]]])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60pattern2x62_127)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60pattern1x62_126)) else tco_apply(kl_fail, []))][(-1)] if (shen_consp(tco_apply(shen_pair, [KL_ARG_V659_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V659_115])])[0]) and shen_eq(symdic.symdic_kl_x64s, tco_apply(shen_pair, [KL_ARG_V659_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V659_115])])[0][0])) else tco_apply(kl_fail, []))]) if (shen_consp(KL_ARG_V659_115[0]) and shen_consp(KL_ARG_V659_115[0][0])) else tco_apply(kl_fail, []))), ([setattr(KL_CTX, 'KL_LOC_Result_128', (tco_apply(shen_sndx45orx45fail, [((tco_apply(shen_pair, [tco_apply(shen_pair, [tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V659_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V659_115])])[0][1], tco_apply(shen_hdtl, [tco_apply(shen_pair, [KL_ARG_V659_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V659_115])])])])[0][1], tco_apply(shen_hdtl, [tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V659_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V659_115])])[0][1], tco_apply(shen_hdtl, [tco_apply(shen_pair, [KL_ARG_V659_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V659_115])])])])])])[0], tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V659_115[0][1], tco_apply(shen_hdtl, [KL_ARG_V659_115])])[0], [symdic.symdic_kl_vector, [0, []]]])]) if (shen_consp(tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V659_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V659_115])])[0][1], tco_apply(shen_hdtl, [tco_apply(shen_pair, [KL_ARG_V659_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V659_115])])])])[0]) and shen_eq(0, tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V659_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V659_115])])[0][1], tco_apply(shen_hdtl, [tco_apply(shen_pair, [KL_ARG_V659_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V659_115])])])])[0][0])) else tco_apply(kl_fail, [])) if (shen_consp(tco_apply(shen_pair, [KL_ARG_V659_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V659_115])])[0]) and shen_eq(symdic.symdic_kl_vector, tco_apply(shen_pair, [KL_ARG_V659_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V659_115])])[0][0])) else tco_apply(kl_fail, []))]) if (shen_consp(KL_ARG_V659_115[0]) and shen_consp(KL_ARG_V659_115[0][0])) else tco_apply(kl_fail, []))), ([setattr(KL_CTX, 'KL_LOC_Result_129', ([setattr(KL_CTX, 'KL_LOC_Parse_X_130', KL_ARG_V659_115[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V659_115[0][1], tco_apply(shen_hdtl, [KL_ARG_V659_115])])[0], tco_apply(shen_constructorx45error, [KL_CTX.KL_LOC_Parse_X_130])]) if shen_consp(KL_CTX.KL_LOC_Parse_X_130) else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V659_115[0]) else tco_apply(kl_fail, []))), ([setattr(KL_CTX, 'KL_LOC_Result_131', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60simple_patternx62_132', tco_apply(shen_x60simple_patternx62, [KL_ARG_V659_115])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60simple_patternx62_132[0], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60simple_patternx62_132])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60simple_patternx62_132)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_131, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_131)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_129, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_129)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_128, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_128)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_125, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_125)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_122, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_122)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_119, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_119)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_116, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_116)][(-1)]
shen_add_fun('shen.<pattern>', shen_x60patternx62)

@tail_recursion
def shen_constructorx45error(KL_ARG_V660_133):
    global symdic
    return shen_simple_error(tco_apply(shen_app, [KL_ARG_V660_133, ' is not a legitimate constructor\r\n', symdic.symdic_shen_a]))
shen_add_fun('shen.constructor-error', shen_constructorx45error)

@tail_recursion
def shen_x60simple_patternx62(KL_ARG_V665_134):

    class KL_Context:
        KL_LOC_Result_135 = None
        KL_LOC_Parse_X_136 = None
        KL_LOC_Result_137 = None
        KL_LOC_Parse_X_138 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_135', ([setattr(KL_CTX, 'KL_LOC_Parse_X_136', KL_ARG_V665_134[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V665_134[0][1], tco_apply(shen_hdtl, [KL_ARG_V665_134])])[0], tco_apply(kl_gensym, [symdic.symdic_Parse_Y])]) if shen_eq(KL_CTX.KL_LOC_Parse_X_136, symdic.symdic_kl__) else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V665_134[0]) else tco_apply(kl_fail, []))), ([setattr(KL_CTX, 'KL_LOC_Result_137', ([setattr(KL_CTX, 'KL_LOC_Parse_X_138', KL_ARG_V665_134[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V665_134[0][1], tco_apply(shen_hdtl, [KL_ARG_V665_134])])[0], KL_CTX.KL_LOC_Parse_X_138]) if (not tco_apply(kl_elementx63, [KL_CTX.KL_LOC_Parse_X_138, [symdic.symdic_kl_x45x62, [symdic.symdic_kl_x60x45, []]]])) else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V665_134[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_137, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_137)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_135, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_135)][(-1)]
shen_add_fun('shen.<simple_pattern>', shen_x60simple_patternx62)

@tail_recursion
def shen_x60pattern1x62(KL_ARG_V670_139):

    class KL_Context:
        KL_LOC_Result_140 = None
        KL_LOC_Parse_shen_x60patternx62_141 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_140', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60patternx62_141', tco_apply(shen_x60patternx62, [KL_ARG_V670_139])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60patternx62_141[0], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternx62_141])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60patternx62_141)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_140, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_140)][(-1)]
shen_add_fun('shen.<pattern1>', shen_x60pattern1x62)

@tail_recursion
def shen_x60pattern2x62(KL_ARG_V675_142):

    class KL_Context:
        KL_LOC_Result_143 = None
        KL_LOC_Parse_shen_x60patternx62_144 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_143', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60patternx62_144', tco_apply(shen_x60patternx62, [KL_ARG_V675_142])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60patternx62_144[0], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternx62_144])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60patternx62_144)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_143, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_143)][(-1)]
shen_add_fun('shen.<pattern2>', shen_x60pattern2x62)

@tail_recursion
def shen_x60actionx62(KL_ARG_V680_145):

    class KL_Context:
        KL_LOC_Result_146 = None
        KL_LOC_Parse_X_147 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_146', ([setattr(KL_CTX, 'KL_LOC_Parse_X_147', KL_ARG_V680_145[0][0]), tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V680_145[0][1], tco_apply(shen_hdtl, [KL_ARG_V680_145])])[0], KL_CTX.KL_LOC_Parse_X_147])][(-1)] if shen_consp(KL_ARG_V680_145[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_146, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_146)][(-1)]
shen_add_fun('shen.<action>', shen_x60actionx62)

@tail_recursion
def shen_x60guardx62(KL_ARG_V685_148):

    class KL_Context:
        KL_LOC_Result_149 = None
        KL_LOC_Parse_X_150 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_149', ([setattr(KL_CTX, 'KL_LOC_Parse_X_150', KL_ARG_V685_148[0][0]), tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V685_148[0][1], tco_apply(shen_hdtl, [KL_ARG_V685_148])])[0], KL_CTX.KL_LOC_Parse_X_150])][(-1)] if shen_consp(KL_ARG_V685_148[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_149, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_149)][(-1)]
shen_add_fun('shen.<guard>', shen_x60guardx62)

@tail_recursion
def shen_compile_to_machine_code(KL_ARG_V686_151, KL_ARG_V687_152):

    class KL_Context:
        KL_LOC_Lambdax43_153 = None
        KL_LOC_KL_154 = None
        KL_LOC_Record_155 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Lambdax43_153', tco_apply(shen_compile_to_lambdax43, [KL_ARG_V686_151, KL_ARG_V687_152])), [setattr(KL_CTX, 'KL_LOC_KL_154', tco_apply(shen_compile_to_kl, [KL_ARG_V686_151, KL_CTX.KL_LOC_Lambdax43_153])), [setattr(KL_CTX, 'KL_LOC_Record_155', tco_apply(shen_recordx45source, [KL_ARG_V686_151, KL_CTX.KL_LOC_KL_154])), KL_CTX.KL_LOC_KL_154][(-1)]][(-1)]][(-1)]
shen_add_fun('shen.compile_to_machine_code', shen_compile_to_machine_code)

@tail_recursion
def shen_recordx45source(KL_ARG_V690_156, KL_ARG_V691_157):
    global symdic
    return (symdic.symdic_shen_skip if shen_get(symdic.symdic_shen_x42installingx45klx42) else (tail_call(kl_put, [KL_ARG_V690_156, symdic.symdic_shen_source, KL_ARG_V691_157, shen_get(symdic.symdic_kl_x42propertyx45vectorx42)]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.record-source', shen_recordx45source)

@tail_recursion
def shen_compile_to_lambdax43(KL_ARG_V692_158, KL_ARG_V693_159):

    class KL_Context:
        KL_LOC_Arity_160 = None
        KL_LOC_Free_161 = None
        KL_LOC_Variables_163 = None
        KL_LOC_Strip_164 = None
        KL_LOC_Abstractions_165 = None
        KL_LOC_Applications_166 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Arity_160', tco_apply(shen_aritycheck, [KL_ARG_V692_158, KL_ARG_V693_159])), [setattr(KL_CTX, 'KL_LOC_Free_161', tco_apply(kl_map, [(lambda KL_ARG_Rule_162: tail_call(shen_free_variable_check, [KL_ARG_V692_158, KL_ARG_Rule_162])), KL_ARG_V693_159])), [setattr(KL_CTX, 'KL_LOC_Variables_163', tco_apply(shen_parameters, [KL_CTX.KL_LOC_Arity_160])), [setattr(KL_CTX, 'KL_LOC_Strip_164', tco_apply(kl_map, [symdic.symdic_shen_stripx45protect, KL_ARG_V693_159])), [setattr(KL_CTX, 'KL_LOC_Abstractions_165', tco_apply(kl_map, [symdic.symdic_shen_abstract_rule, KL_CTX.KL_LOC_Strip_164])), [setattr(KL_CTX, 'KL_LOC_Applications_166', tco_apply(kl_map, [(lambda KL_ARG_X_167: tail_call(shen_application_build, [KL_CTX.KL_LOC_Variables_163, KL_ARG_X_167])), KL_CTX.KL_LOC_Abstractions_165])), [KL_CTX.KL_LOC_Variables_163, [KL_CTX.KL_LOC_Applications_166, []]]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]
shen_add_fun('shen.compile_to_lambda+', shen_compile_to_lambdax43)

@tail_recursion
def shen_free_variable_check(KL_ARG_V694_168, KL_ARG_V695_169):

    class KL_Context:
        KL_LOC_Bound_170 = None
        KL_LOC_Free_171 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_Bound_170', tco_apply(shen_extract_vars, [KL_ARG_V695_169[0]])), [setattr(KL_CTX, 'KL_LOC_Free_171', tco_apply(shen_extract_free_vars, [KL_CTX.KL_LOC_Bound_170, KL_ARG_V695_169[1][0]])), tail_call(shen_free_variable_warnings, [KL_ARG_V694_168, KL_CTX.KL_LOC_Free_171])][(-1)]][(-1)] if (shen_consp(KL_ARG_V695_169) and (shen_consp(KL_ARG_V695_169[1]) and shen_eq([], KL_ARG_V695_169[1][1]))) else (tail_call(shen_sysx45error, [symdic.symdic_shen_free_variable_check]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.free_variable_check', shen_free_variable_check)

@tail_recursion
def shen_extract_vars(KL_ARG_V696_172):
    global symdic
    return ([KL_ARG_V696_172, []] if tco_apply(kl_variablex63, [KL_ARG_V696_172]) else (tail_call(kl_union, [tco_apply(shen_extract_vars, [KL_ARG_V696_172[0]]), tco_apply(shen_extract_vars, [KL_ARG_V696_172[1]])]) if shen_consp(KL_ARG_V696_172) else ([] if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.extract_vars', shen_extract_vars)

@tail_recursion
def shen_extract_free_vars(KL_ARG_V706_173, KL_ARG_V707_174):
    global symdic
    return ([] if (shen_consp(KL_ARG_V707_174) and (shen_consp(KL_ARG_V707_174[1]) and (shen_eq([], KL_ARG_V707_174[1][1]) and shen_eq(KL_ARG_V707_174[0], symdic.symdic_kl_protect)))) else ([KL_ARG_V707_174, []] if (tco_apply(kl_variablex63, [KL_ARG_V707_174]) and (not tco_apply(kl_elementx63, [KL_ARG_V707_174, KL_ARG_V706_173]))) else (tail_call(shen_extract_free_vars, [[KL_ARG_V707_174[1][0], KL_ARG_V706_173], KL_ARG_V707_174[1][1][0]]) if (shen_consp(KL_ARG_V707_174) and (shen_eq(symdic.symdic_kl_lambda, KL_ARG_V707_174[0]) and (shen_consp(KL_ARG_V707_174[1]) and (shen_consp(KL_ARG_V707_174[1][1]) and shen_eq([], KL_ARG_V707_174[1][1][1]))))) else (tail_call(kl_union, [tco_apply(shen_extract_free_vars, [KL_ARG_V706_173, KL_ARG_V707_174[1][1][0]]), tco_apply(shen_extract_free_vars, [[KL_ARG_V707_174[1][0], KL_ARG_V706_173], KL_ARG_V707_174[1][1][1][0]])]) if (shen_consp(KL_ARG_V707_174) and (shen_eq(symdic.symdic_kl_let, KL_ARG_V707_174[0]) and (shen_consp(KL_ARG_V707_174[1]) and (shen_consp(KL_ARG_V707_174[1][1]) and (shen_consp(KL_ARG_V707_174[1][1][1]) and shen_eq([], KL_ARG_V707_174[1][1][1][1])))))) else (tail_call(kl_union, [tco_apply(shen_extract_free_vars, [KL_ARG_V706_173, KL_ARG_V707_174[0]]), tco_apply(shen_extract_free_vars, [KL_ARG_V706_173, KL_ARG_V707_174[1]])]) if shen_consp(KL_ARG_V707_174) else ([] if True else shen_simple_error('condition failure')))))))
shen_add_fun('shen.extract_free_vars', shen_extract_free_vars)

@tail_recursion
def shen_free_variable_warnings(KL_ARG_V710_175, KL_ARG_V711_176):
    global symdic
    return (symdic.symdic_kl__ if shen_eq([], KL_ARG_V711_176) else (shen_simple_error(('error: the following variables are free in ' + tco_apply(shen_app, [KL_ARG_V710_175, (': ' + tco_apply(shen_app, [tco_apply(shen_list_variables, [KL_ARG_V711_176]), '', symdic.symdic_shen_a])), symdic.symdic_shen_a]))) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.free_variable_warnings', shen_free_variable_warnings)

@tail_recursion
def shen_list_variables(KL_ARG_V712_177):
    global symdic
    return ((str(KL_ARG_V712_177[0]) + '.') if (shen_consp(KL_ARG_V712_177) and shen_eq([], KL_ARG_V712_177[1])) else ((str(KL_ARG_V712_177[0]) + (', ' + tco_apply(shen_list_variables, [KL_ARG_V712_177[1]]))) if shen_consp(KL_ARG_V712_177) else (tail_call(shen_sysx45error, [symdic.symdic_shen_list_variables]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.list_variables', shen_list_variables)

@tail_recursion
def shen_stripx45protect(KL_ARG_V713_178):
    global symdic
    return (KL_ARG_V713_178[1][0] if (shen_consp(KL_ARG_V713_178) and (shen_consp(KL_ARG_V713_178[1]) and (shen_eq([], KL_ARG_V713_178[1][1]) and shen_eq(KL_ARG_V713_178[0], symdic.symdic_kl_protect)))) else ([tco_apply(shen_stripx45protect, [KL_ARG_V713_178[0]]), tco_apply(shen_stripx45protect, [KL_ARG_V713_178[1]])] if shen_consp(KL_ARG_V713_178) else (KL_ARG_V713_178 if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.strip-protect', shen_stripx45protect)

@tail_recursion
def shen_linearise(KL_ARG_V714_179):
    global symdic
    return (tail_call(shen_linearise_help, [tco_apply(shen_flatten, [KL_ARG_V714_179[0]]), KL_ARG_V714_179[0], KL_ARG_V714_179[1][0]]) if (shen_consp(KL_ARG_V714_179) and (shen_consp(KL_ARG_V714_179[1]) and shen_eq([], KL_ARG_V714_179[1][1]))) else (tail_call(shen_sysx45error, [symdic.symdic_shen_linearise]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.linearise', shen_linearise)

@tail_recursion
def shen_flatten(KL_ARG_V715_180):
    global symdic
    return ([] if shen_eq([], KL_ARG_V715_180) else (tail_call(kl_append, [tco_apply(shen_flatten, [KL_ARG_V715_180[0]]), tco_apply(shen_flatten, [KL_ARG_V715_180[1]])]) if shen_consp(KL_ARG_V715_180) else ([KL_ARG_V715_180, []] if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.flatten', shen_flatten)

@tail_recursion
def shen_linearise_help(KL_ARG_V716_181, KL_ARG_V717_182, KL_ARG_V718_183):

    class KL_Context:
        KL_LOC_Var_184 = None
        KL_LOC_NewAction_185 = None
        KL_LOC_NewPatts_186 = None
    KL_CTX = KL_Context()
    global symdic
    return ([KL_ARG_V717_182, [KL_ARG_V718_183, []]] if shen_eq([], KL_ARG_V716_181) else (([setattr(KL_CTX, 'KL_LOC_Var_184', tco_apply(kl_gensym, [KL_ARG_V716_181[0]])), [setattr(KL_CTX, 'KL_LOC_NewAction_185', [symdic.symdic_kl_where, [[symdic.symdic_kl_x61, [KL_ARG_V716_181[0], [KL_CTX.KL_LOC_Var_184, []]]], [KL_ARG_V718_183, []]]]), [setattr(KL_CTX, 'KL_LOC_NewPatts_186', tco_apply(shen_linearise_X, [KL_ARG_V716_181[0], KL_CTX.KL_LOC_Var_184, KL_ARG_V717_182])), tail_call(shen_linearise_help, [KL_ARG_V716_181[1], KL_CTX.KL_LOC_NewPatts_186, KL_CTX.KL_LOC_NewAction_185])][(-1)]][(-1)]][(-1)] if (tco_apply(kl_variablex63, [KL_ARG_V716_181[0]]) and tco_apply(kl_elementx63, [KL_ARG_V716_181[0], KL_ARG_V716_181[1]])) else tail_call(shen_linearise_help, [KL_ARG_V716_181[1], KL_ARG_V717_182, KL_ARG_V718_183])) if shen_consp(KL_ARG_V716_181) else (tail_call(shen_sysx45error, [symdic.symdic_shen_linearise_help]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.linearise_help', shen_linearise_help)

@tail_recursion
def shen_linearise_X(KL_ARG_V727_187, KL_ARG_V728_188, KL_ARG_V729_189):

    class KL_Context:
        KL_LOC_L_190 = None
    KL_CTX = KL_Context()
    global symdic
    return (KL_ARG_V728_188 if shen_eq(KL_ARG_V729_189, KL_ARG_V727_187) else ([setattr(KL_CTX, 'KL_LOC_L_190', tco_apply(shen_linearise_X, [KL_ARG_V727_187, KL_ARG_V728_188, KL_ARG_V729_189[0]])), ([KL_ARG_V729_189[0], tco_apply(shen_linearise_X, [KL_ARG_V727_187, KL_ARG_V728_188, KL_ARG_V729_189[1]])] if shen_eq(KL_CTX.KL_LOC_L_190, KL_ARG_V729_189[0]) else [KL_CTX.KL_LOC_L_190, KL_ARG_V729_189[1]])][(-1)] if shen_consp(KL_ARG_V729_189) else (KL_ARG_V729_189 if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.linearise_X', shen_linearise_X)

@tail_recursion
def shen_aritycheck(KL_ARG_V731_191, KL_ARG_V732_192):
    global symdic
    return ([tco_apply(shen_aritycheckx45action, [KL_ARG_V732_192[0][1][0]]), tail_call(shen_aritycheckx45name, [KL_ARG_V731_191, tco_apply(kl_arity, [KL_ARG_V731_191]), tco_apply(kl_length, [KL_ARG_V732_192[0][0]])])][(-1)] if (shen_consp(KL_ARG_V732_192) and (shen_consp(KL_ARG_V732_192[0]) and (shen_consp(KL_ARG_V732_192[0][1]) and (shen_eq([], KL_ARG_V732_192[0][1][1]) and shen_eq([], KL_ARG_V732_192[1]))))) else (([tco_apply(shen_aritycheckx45action, [KL_ARG_V732_192[0][1][0]]), tail_call(shen_aritycheck, [KL_ARG_V731_191, KL_ARG_V732_192[1]])][(-1)] if shen_eq(tco_apply(kl_length, [KL_ARG_V732_192[0][0]]), tco_apply(kl_length, [KL_ARG_V732_192[1][0][0]])) else shen_simple_error(('arity error in ' + tco_apply(shen_app, [KL_ARG_V731_191, '\r\n', symdic.symdic_shen_a])))) if (shen_consp(KL_ARG_V732_192) and (shen_consp(KL_ARG_V732_192[0]) and (shen_consp(KL_ARG_V732_192[0][1]) and (shen_eq([], KL_ARG_V732_192[0][1][1]) and (shen_consp(KL_ARG_V732_192[1]) and (shen_consp(KL_ARG_V732_192[1][0]) and (shen_consp(KL_ARG_V732_192[1][0][1]) and shen_eq([], KL_ARG_V732_192[1][0][1][1])))))))) else (tail_call(shen_sysx45error, [symdic.symdic_shen_aritycheck]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.aritycheck', shen_aritycheck)

@tail_recursion
def shen_aritycheckx45name(KL_ARG_V741_193, KL_ARG_V742_194, KL_ARG_V743_195):
    global symdic
    return (KL_ARG_V743_195 if shen_eq((-1), KL_ARG_V742_194) else (KL_ARG_V743_195 if shen_eq(KL_ARG_V743_195, KL_ARG_V742_194) else ([shen_pr(('\r\nwarning: changing the arity of ' + tco_apply(shen_app, [KL_ARG_V741_193, ' can cause errors.\r\n', symdic.symdic_shen_a])), tco_apply(kl_stoutput, [])), KL_ARG_V743_195][(-1)] if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.aritycheck-name', shen_aritycheckx45name)

@tail_recursion
def shen_aritycheckx45action(KL_ARG_V749_196):
    global symdic
    return ([tco_apply(shen_aah, [KL_ARG_V749_196[0], KL_ARG_V749_196[1]]), tail_call(kl_map, [symdic.symdic_shen_aritycheckx45action, KL_ARG_V749_196])][(-1)] if shen_consp(KL_ARG_V749_196) else (symdic.symdic_shen_skip if True else shen_simple_error('condition failure')))
shen_add_fun('shen.aritycheck-action', shen_aritycheckx45action)

@tail_recursion
def shen_aah(KL_ARG_V750_197, KL_ARG_V751_198):

    class KL_Context:
        KL_LOC_Arity_199 = None
        KL_LOC_Len_200 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Arity_199', tco_apply(kl_arity, [KL_ARG_V750_197])), [setattr(KL_CTX, 'KL_LOC_Len_200', tco_apply(kl_length, [KL_ARG_V751_198])), (shen_pr(('warning: ' + tco_apply(shen_app, [KL_ARG_V750_197, (' might not like ' + tco_apply(shen_app, [KL_CTX.KL_LOC_Len_200, (' argument' + tco_apply(shen_app, [('s' if (KL_CTX.KL_LOC_Len_200 > 1) else ''), '.\r\n', symdic.symdic_shen_a])), symdic.symdic_shen_a])), symdic.symdic_shen_a])), tco_apply(kl_stoutput, [])) if ((KL_CTX.KL_LOC_Arity_199 > (-1)) and (KL_CTX.KL_LOC_Len_200 > KL_CTX.KL_LOC_Arity_199)) else symdic.symdic_shen_skip)][(-1)]][(-1)]
shen_add_fun('shen.aah', shen_aah)

@tail_recursion
def shen_abstract_rule(KL_ARG_V752_201):
    global symdic
    return (tail_call(shen_abstraction_build, [KL_ARG_V752_201[0], KL_ARG_V752_201[1][0]]) if (shen_consp(KL_ARG_V752_201) and (shen_consp(KL_ARG_V752_201[1]) and shen_eq([], KL_ARG_V752_201[1][1]))) else (tail_call(shen_sysx45error, [symdic.symdic_shen_abstract_rule]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.abstract_rule', shen_abstract_rule)

@tail_recursion
def shen_abstraction_build(KL_ARG_V753_202, KL_ARG_V754_203):
    global symdic
    return (KL_ARG_V754_203 if shen_eq([], KL_ARG_V753_202) else ([symdic.symdic_kl_x47_, [KL_ARG_V753_202[0], [tco_apply(shen_abstraction_build, [KL_ARG_V753_202[1], KL_ARG_V754_203]), []]]] if shen_consp(KL_ARG_V753_202) else (tail_call(shen_sysx45error, [symdic.symdic_shen_abstraction_build]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.abstraction_build', shen_abstraction_build)

@tail_recursion
def shen_parameters(KL_ARG_V755_204):
    global symdic
    return ([] if shen_eq(0, KL_ARG_V755_204) else ([tco_apply(kl_gensym, [symdic.symdic_V]), tco_apply(shen_parameters, [(KL_ARG_V755_204 - 1)])] if True else shen_simple_error('condition failure')))
shen_add_fun('shen.parameters', shen_parameters)

@tail_recursion
def shen_application_build(KL_ARG_V756_205, KL_ARG_V757_206):
    global symdic
    return (KL_ARG_V757_206 if shen_eq([], KL_ARG_V756_205) else (tail_call(shen_application_build, [KL_ARG_V756_205[1], [KL_ARG_V757_206, [KL_ARG_V756_205[0], []]]]) if shen_consp(KL_ARG_V756_205) else (tail_call(shen_sysx45error, [symdic.symdic_shen_application_build]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.application_build', shen_application_build)

@tail_recursion
def shen_compile_to_kl(KL_ARG_V758_207, KL_ARG_V759_208):

    class KL_Context:
        KL_LOC_Arity_209 = None
        KL_LOC_Reduce_210 = None
        KL_LOC_CondExpression_211 = None
        KL_LOC_KL_212 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_Arity_209', tco_apply(shen_storex45arity, [KL_ARG_V758_207, tco_apply(kl_length, [KL_ARG_V759_208[0]])])), [setattr(KL_CTX, 'KL_LOC_Reduce_210', tco_apply(kl_map, [symdic.symdic_shen_reduce, KL_ARG_V759_208[1][0]])), [setattr(KL_CTX, 'KL_LOC_CondExpression_211', tco_apply(shen_condx45expression, [KL_ARG_V758_207, KL_ARG_V759_208[0], KL_CTX.KL_LOC_Reduce_210])), [setattr(KL_CTX, 'KL_LOC_KL_212', [symdic.symdic_kl_defun, [KL_ARG_V758_207, [KL_ARG_V759_208[0], [KL_CTX.KL_LOC_CondExpression_211, []]]]]), KL_CTX.KL_LOC_KL_212][(-1)]][(-1)]][(-1)]][(-1)] if (shen_consp(KL_ARG_V759_208) and (shen_consp(KL_ARG_V759_208[1]) and shen_eq([], KL_ARG_V759_208[1][1]))) else (tail_call(shen_sysx45error, [symdic.symdic_shen_compile_to_kl]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.compile_to_kl', shen_compile_to_kl)

@tail_recursion
def shen_storex45arity(KL_ARG_V762_213, KL_ARG_V763_214):
    global symdic
    return (symdic.symdic_shen_skip if shen_get(symdic.symdic_shen_x42installingx45klx42) else (tail_call(kl_put, [KL_ARG_V762_213, symdic.symdic_kl_arity, KL_ARG_V763_214, shen_get(symdic.symdic_kl_x42propertyx45vectorx42)]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.store-arity', shen_storex45arity)

@tail_recursion
def shen_reduce(KL_ARG_V764_215):

    class KL_Context:
        KL_LOC_Result_216 = None
    KL_CTX = KL_Context()
    global symdic
    return [shen_set(symdic.symdic_shen_x42teststackx42, []), [setattr(KL_CTX, 'KL_LOC_Result_216', tco_apply(shen_reduce_help, [KL_ARG_V764_215])), [[symdic.symdic_kl_x58, [symdic.symdic_shen_tests, tco_apply(kl_reverse, [shen_get(symdic.symdic_shen_x42teststackx42)])]], [KL_CTX.KL_LOC_Result_216, []]]][(-1)]][(-1)]
shen_add_fun('shen.reduce', shen_reduce)

@tail_recursion
def shen_reduce_help(KL_ARG_V765_217):

    class KL_Context:
        KL_LOC_Abstraction_218 = None
        KL_LOC_Application_219 = None
        KL_LOC_Abstraction_220 = None
        KL_LOC_Application_221 = None
        KL_LOC_Abstraction_222 = None
        KL_LOC_Application_223 = None
        KL_LOC_Abstraction_224 = None
        KL_LOC_Application_225 = None
        KL_LOC_Z_226 = None
    KL_CTX = KL_Context()
    global symdic
    return ([tco_apply(shen_add_test, [[symdic.symdic_kl_consx63, KL_ARG_V765_217[1]]]), [setattr(KL_CTX, 'KL_LOC_Abstraction_218', [symdic.symdic_kl_x47_, [KL_ARG_V765_217[0][1][0][1][0], [[symdic.symdic_kl_x47_, [KL_ARG_V765_217[0][1][0][1][1][0], [tco_apply(shen_ebr, [KL_ARG_V765_217[1][0], KL_ARG_V765_217[0][1][0], KL_ARG_V765_217[0][1][1][0]]), []]]], []]]]), [setattr(KL_CTX, 'KL_LOC_Application_219', [[KL_CTX.KL_LOC_Abstraction_218, [[symdic.symdic_kl_hd, KL_ARG_V765_217[1]], []]], [[symdic.symdic_kl_tl, KL_ARG_V765_217[1]], []]]), tail_call(shen_reduce_help, [KL_CTX.KL_LOC_Application_219])][(-1)]][(-1)]][(-1)] if (shen_consp(KL_ARG_V765_217) and (shen_consp(KL_ARG_V765_217[0]) and (shen_eq(symdic.symdic_kl_x47_, KL_ARG_V765_217[0][0]) and (shen_consp(KL_ARG_V765_217[0][1]) and (shen_consp(KL_ARG_V765_217[0][1][0]) and (shen_eq(symdic.symdic_kl_cons, KL_ARG_V765_217[0][1][0][0]) and (shen_consp(KL_ARG_V765_217[0][1][0][1]) and (shen_consp(KL_ARG_V765_217[0][1][0][1][1]) and (shen_eq([], KL_ARG_V765_217[0][1][0][1][1][1]) and (shen_consp(KL_ARG_V765_217[0][1][1]) and (shen_eq([], KL_ARG_V765_217[0][1][1][1]) and (shen_consp(KL_ARG_V765_217[1]) and shen_eq([], KL_ARG_V765_217[1][1]))))))))))))) else ([tco_apply(shen_add_test, [[symdic.symdic_kl_tuplex63, KL_ARG_V765_217[1]]]), [setattr(KL_CTX, 'KL_LOC_Abstraction_220', [symdic.symdic_kl_x47_, [KL_ARG_V765_217[0][1][0][1][0], [[symdic.symdic_kl_x47_, [KL_ARG_V765_217[0][1][0][1][1][0], [tco_apply(shen_ebr, [KL_ARG_V765_217[1][0], KL_ARG_V765_217[0][1][0], KL_ARG_V765_217[0][1][1][0]]), []]]], []]]]), [setattr(KL_CTX, 'KL_LOC_Application_221', [[KL_CTX.KL_LOC_Abstraction_220, [[symdic.symdic_kl_fst, KL_ARG_V765_217[1]], []]], [[symdic.symdic_kl_snd, KL_ARG_V765_217[1]], []]]), tail_call(shen_reduce_help, [KL_CTX.KL_LOC_Application_221])][(-1)]][(-1)]][(-1)] if (shen_consp(KL_ARG_V765_217) and (shen_consp(KL_ARG_V765_217[0]) and (shen_eq(symdic.symdic_kl_x47_, KL_ARG_V765_217[0][0]) and (shen_consp(KL_ARG_V765_217[0][1]) and (shen_consp(KL_ARG_V765_217[0][1][0]) and (shen_eq(symdic.symdic_kl_x64p, KL_ARG_V765_217[0][1][0][0]) and (shen_consp(KL_ARG_V765_217[0][1][0][1]) and (shen_consp(KL_ARG_V765_217[0][1][0][1][1]) and (shen_eq([], KL_ARG_V765_217[0][1][0][1][1][1]) and (shen_consp(KL_ARG_V765_217[0][1][1]) and (shen_eq([], KL_ARG_V765_217[0][1][1][1]) and (shen_consp(KL_ARG_V765_217[1]) and shen_eq([], KL_ARG_V765_217[1][1]))))))))))))) else ([tco_apply(shen_add_test, [[symdic.symdic_shen_x43vectorx63, KL_ARG_V765_217[1]]]), [setattr(KL_CTX, 'KL_LOC_Abstraction_222', [symdic.symdic_kl_x47_, [KL_ARG_V765_217[0][1][0][1][0], [[symdic.symdic_kl_x47_, [KL_ARG_V765_217[0][1][0][1][1][0], [tco_apply(shen_ebr, [KL_ARG_V765_217[1][0], KL_ARG_V765_217[0][1][0], KL_ARG_V765_217[0][1][1][0]]), []]]], []]]]), [setattr(KL_CTX, 'KL_LOC_Application_223', [[KL_CTX.KL_LOC_Abstraction_222, [[symdic.symdic_kl_hdv, KL_ARG_V765_217[1]], []]], [[symdic.symdic_kl_tlv, KL_ARG_V765_217[1]], []]]), tail_call(shen_reduce_help, [KL_CTX.KL_LOC_Application_223])][(-1)]][(-1)]][(-1)] if (shen_consp(KL_ARG_V765_217) and (shen_consp(KL_ARG_V765_217[0]) and (shen_eq(symdic.symdic_kl_x47_, KL_ARG_V765_217[0][0]) and (shen_consp(KL_ARG_V765_217[0][1]) and (shen_consp(KL_ARG_V765_217[0][1][0]) and (shen_eq(symdic.symdic_kl_x64v, KL_ARG_V765_217[0][1][0][0]) and (shen_consp(KL_ARG_V765_217[0][1][0][1]) and (shen_consp(KL_ARG_V765_217[0][1][0][1][1]) and (shen_eq([], KL_ARG_V765_217[0][1][0][1][1][1]) and (shen_consp(KL_ARG_V765_217[0][1][1]) and (shen_eq([], KL_ARG_V765_217[0][1][1][1]) and (shen_consp(KL_ARG_V765_217[1]) and shen_eq([], KL_ARG_V765_217[1][1]))))))))))))) else ([tco_apply(shen_add_test, [[symdic.symdic_shen_x43stringx63, KL_ARG_V765_217[1]]]), [setattr(KL_CTX, 'KL_LOC_Abstraction_224', [symdic.symdic_kl_x47_, [KL_ARG_V765_217[0][1][0][1][0], [[symdic.symdic_kl_x47_, [KL_ARG_V765_217[0][1][0][1][1][0], [tco_apply(shen_ebr, [KL_ARG_V765_217[1][0], KL_ARG_V765_217[0][1][0], KL_ARG_V765_217[0][1][1][0]]), []]]], []]]]), [setattr(KL_CTX, 'KL_LOC_Application_225', [[KL_CTX.KL_LOC_Abstraction_224, [[symdic.symdic_kl_pos, [KL_ARG_V765_217[1][0], [0, []]]], []]], [[symdic.symdic_kl_tlstr, KL_ARG_V765_217[1]], []]]), tail_call(shen_reduce_help, [KL_CTX.KL_LOC_Application_225])][(-1)]][(-1)]][(-1)] if (shen_consp(KL_ARG_V765_217) and (shen_consp(KL_ARG_V765_217[0]) and (shen_eq(symdic.symdic_kl_x47_, KL_ARG_V765_217[0][0]) and (shen_consp(KL_ARG_V765_217[0][1]) and (shen_consp(KL_ARG_V765_217[0][1][0]) and (shen_eq(symdic.symdic_kl_x64s, KL_ARG_V765_217[0][1][0][0]) and (shen_consp(KL_ARG_V765_217[0][1][0][1]) and (shen_consp(KL_ARG_V765_217[0][1][0][1][1]) and (shen_eq([], KL_ARG_V765_217[0][1][0][1][1][1]) and (shen_consp(KL_ARG_V765_217[0][1][1]) and (shen_eq([], KL_ARG_V765_217[0][1][1][1]) and (shen_consp(KL_ARG_V765_217[1]) and shen_eq([], KL_ARG_V765_217[1][1]))))))))))))) else ([tco_apply(shen_add_test, [[symdic.symdic_kl_x61, [KL_ARG_V765_217[0][1][0], KL_ARG_V765_217[1]]]]), tail_call(shen_reduce_help, [KL_ARG_V765_217[0][1][1][0]])][(-1)] if (shen_consp(KL_ARG_V765_217) and (shen_consp(KL_ARG_V765_217[0]) and (shen_eq(symdic.symdic_kl_x47_, KL_ARG_V765_217[0][0]) and (shen_consp(KL_ARG_V765_217[0][1]) and (shen_consp(KL_ARG_V765_217[0][1][1]) and (shen_eq([], KL_ARG_V765_217[0][1][1][1]) and (shen_consp(KL_ARG_V765_217[1]) and (shen_eq([], KL_ARG_V765_217[1][1]) and (not tco_apply(kl_variablex63, [KL_ARG_V765_217[0][1][0]])))))))))) else (tail_call(shen_reduce_help, [tco_apply(shen_ebr, [KL_ARG_V765_217[1][0], KL_ARG_V765_217[0][1][0], KL_ARG_V765_217[0][1][1][0]])]) if (shen_consp(KL_ARG_V765_217) and (shen_consp(KL_ARG_V765_217[0]) and (shen_eq(symdic.symdic_kl_x47_, KL_ARG_V765_217[0][0]) and (shen_consp(KL_ARG_V765_217[0][1]) and (shen_consp(KL_ARG_V765_217[0][1][1]) and (shen_eq([], KL_ARG_V765_217[0][1][1][1]) and (shen_consp(KL_ARG_V765_217[1]) and shen_eq([], KL_ARG_V765_217[1][1])))))))) else ([tco_apply(shen_add_test, [KL_ARG_V765_217[1][0]]), tail_call(shen_reduce_help, [KL_ARG_V765_217[1][1][0]])][(-1)] if (shen_consp(KL_ARG_V765_217) and (shen_eq(symdic.symdic_kl_where, KL_ARG_V765_217[0]) and (shen_consp(KL_ARG_V765_217[1]) and (shen_consp(KL_ARG_V765_217[1][1]) and shen_eq([], KL_ARG_V765_217[1][1][1]))))) else ([setattr(KL_CTX, 'KL_LOC_Z_226', tco_apply(shen_reduce_help, [KL_ARG_V765_217[0]])), (KL_ARG_V765_217 if shen_eq(KL_ARG_V765_217[0], KL_CTX.KL_LOC_Z_226) else tail_call(shen_reduce_help, [[KL_CTX.KL_LOC_Z_226, KL_ARG_V765_217[1]]]))][(-1)] if (shen_consp(KL_ARG_V765_217) and (shen_consp(KL_ARG_V765_217[1]) and shen_eq([], KL_ARG_V765_217[1][1]))) else (KL_ARG_V765_217 if True else shen_simple_error('condition failure'))))))))))
shen_add_fun('shen.reduce_help', shen_reduce_help)

@tail_recursion
def shen_x43stringx63(KL_ARG_V766_227):
    global symdic
    return (False if shen_eq('', KL_ARG_V766_227) else (isinstance(KL_ARG_V766_227, str) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.+string?', shen_x43stringx63)

@tail_recursion
def shen_x43vector(KL_ARG_V767_228):
    global symdic
    return (False if shen_eq(KL_ARG_V767_228, tco_apply(kl_vector, [0])) else (tail_call(kl_vectorx63, [KL_ARG_V767_228]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.+vector', shen_x43vector)

@tail_recursion
def shen_ebr(KL_ARG_V776_229, KL_ARG_V777_230, KL_ARG_V778_231):
    global symdic
    return (KL_ARG_V776_229 if shen_eq(KL_ARG_V778_231, KL_ARG_V777_230) else (KL_ARG_V778_231 if (shen_consp(KL_ARG_V778_231) and (shen_eq(symdic.symdic_kl_x47_, KL_ARG_V778_231[0]) and (shen_consp(KL_ARG_V778_231[1]) and (shen_consp(KL_ARG_V778_231[1][1]) and (shen_eq([], KL_ARG_V778_231[1][1][1]) and (tco_apply(kl_occurrences, [KL_ARG_V777_230, KL_ARG_V778_231[1][0]]) > 0)))))) else ([symdic.symdic_kl_let, [KL_ARG_V778_231[1][0], [tco_apply(shen_ebr, [KL_ARG_V776_229, KL_ARG_V778_231[1][0], KL_ARG_V778_231[1][1][0]]), KL_ARG_V778_231[1][1][1]]]] if (shen_consp(KL_ARG_V778_231) and (shen_eq(symdic.symdic_kl_let, KL_ARG_V778_231[0]) and (shen_consp(KL_ARG_V778_231[1]) and (shen_consp(KL_ARG_V778_231[1][1]) and (shen_consp(KL_ARG_V778_231[1][1][1]) and (shen_eq([], KL_ARG_V778_231[1][1][1][1]) and shen_eq(KL_ARG_V778_231[1][0], KL_ARG_V777_230))))))) else ([tco_apply(shen_ebr, [KL_ARG_V776_229, KL_ARG_V777_230, KL_ARG_V778_231[0]]), tco_apply(shen_ebr, [KL_ARG_V776_229, KL_ARG_V777_230, KL_ARG_V778_231[1]])] if shen_consp(KL_ARG_V778_231) else (KL_ARG_V778_231 if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.ebr', shen_ebr)

@tail_recursion
def shen_add_test(KL_ARG_V781_232):
    global symdic
    return shen_set(symdic.symdic_shen_x42teststackx42, [KL_ARG_V781_232, shen_get(symdic.symdic_shen_x42teststackx42)])
shen_add_fun('shen.add_test', shen_add_test)

@tail_recursion
def shen_condx45expression(KL_ARG_V782_233, KL_ARG_V783_234, KL_ARG_V784_235):

    class KL_Context:
        KL_LOC_Err_236 = None
        KL_LOC_Cases_237 = None
        KL_LOC_EncodeChoices_238 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Err_236', tco_apply(shen_errx45condition, [KL_ARG_V782_233])), [setattr(KL_CTX, 'KL_LOC_Cases_237', tco_apply(shen_casex45form, [KL_ARG_V784_235, KL_CTX.KL_LOC_Err_236])), [setattr(KL_CTX, 'KL_LOC_EncodeChoices_238', tco_apply(shen_encodex45choices, [KL_CTX.KL_LOC_Cases_237, KL_ARG_V782_233])), tail_call(shen_condx45form, [KL_CTX.KL_LOC_EncodeChoices_238])][(-1)]][(-1)]][(-1)]
shen_add_fun('shen.cond-expression', shen_condx45expression)

@tail_recursion
def shen_condx45form(KL_ARG_V787_239):
    global symdic
    return (KL_ARG_V787_239[0][1][0] if (shen_consp(KL_ARG_V787_239) and (shen_consp(KL_ARG_V787_239[0]) and (shen_eq(True, KL_ARG_V787_239[0][0]) and (shen_consp(KL_ARG_V787_239[0][1]) and shen_eq([], KL_ARG_V787_239[0][1][1]))))) else ([symdic.symdic_kl_cond, KL_ARG_V787_239] if True else shen_simple_error('condition failure')))
shen_add_fun('shen.cond-form', shen_condx45form)

@tail_recursion
def shen_encodex45choices(KL_ARG_V790_240, KL_ARG_V791_241):
    global symdic
    return ([] if shen_eq([], KL_ARG_V790_240) else ([[True, [[symdic.symdic_kl_let, [symdic.symdic_Result, [KL_ARG_V790_240[0][1][0][1][0], [[symdic.symdic_kl_if, [[symdic.symdic_kl_x61, [symdic.symdic_Result, [[symdic.symdic_kl_fail, []], []]]], [([symdic.symdic_shen_sysx45error, [KL_ARG_V791_241, []]] if shen_get(symdic.symdic_shen_x42installingx45klx42) else [symdic.symdic_shen_f_error, [KL_ARG_V791_241, []]]), [symdic.symdic_Result, []]]]], []]]]], []]], []] if (shen_consp(KL_ARG_V790_240) and (shen_consp(KL_ARG_V790_240[0]) and (shen_eq(True, KL_ARG_V790_240[0][0]) and (shen_consp(KL_ARG_V790_240[0][1]) and (shen_consp(KL_ARG_V790_240[0][1][0]) and (shen_eq(symdic.symdic_shen_choicepointx33, KL_ARG_V790_240[0][1][0][0]) and (shen_consp(KL_ARG_V790_240[0][1][0][1]) and (shen_eq([], KL_ARG_V790_240[0][1][0][1][1]) and (shen_eq([], KL_ARG_V790_240[0][1][1]) and shen_eq([], KL_ARG_V790_240[1])))))))))) else ([[True, [[symdic.symdic_kl_let, [symdic.symdic_Result, [KL_ARG_V790_240[0][1][0][1][0], [[symdic.symdic_kl_if, [[symdic.symdic_kl_x61, [symdic.symdic_Result, [[symdic.symdic_kl_fail, []], []]]], [tco_apply(shen_condx45form, [tco_apply(shen_encodex45choices, [KL_ARG_V790_240[1], KL_ARG_V791_241])]), [symdic.symdic_Result, []]]]], []]]]], []]], []] if (shen_consp(KL_ARG_V790_240) and (shen_consp(KL_ARG_V790_240[0]) and (shen_eq(True, KL_ARG_V790_240[0][0]) and (shen_consp(KL_ARG_V790_240[0][1]) and (shen_consp(KL_ARG_V790_240[0][1][0]) and (shen_eq(symdic.symdic_shen_choicepointx33, KL_ARG_V790_240[0][1][0][0]) and (shen_consp(KL_ARG_V790_240[0][1][0][1]) and (shen_eq([], KL_ARG_V790_240[0][1][0][1][1]) and shen_eq([], KL_ARG_V790_240[0][1][1]))))))))) else ([[True, [[symdic.symdic_kl_let, [symdic.symdic_Freeze, [[symdic.symdic_kl_freeze, [tco_apply(shen_condx45form, [tco_apply(shen_encodex45choices, [KL_ARG_V790_240[1], KL_ARG_V791_241])]), []]], [[symdic.symdic_kl_if, [KL_ARG_V790_240[0][0], [[symdic.symdic_kl_let, [symdic.symdic_Result, [KL_ARG_V790_240[0][1][0][1][0], [[symdic.symdic_kl_if, [[symdic.symdic_kl_x61, [symdic.symdic_Result, [[symdic.symdic_kl_fail, []], []]]], [[symdic.symdic_kl_thaw, [symdic.symdic_Freeze, []]], [symdic.symdic_Result, []]]]], []]]]], [[symdic.symdic_kl_thaw, [symdic.symdic_Freeze, []]], []]]]], []]]]], []]], []] if (shen_consp(KL_ARG_V790_240) and (shen_consp(KL_ARG_V790_240[0]) and (shen_consp(KL_ARG_V790_240[0][1]) and (shen_consp(KL_ARG_V790_240[0][1][0]) and (shen_eq(symdic.symdic_shen_choicepointx33, KL_ARG_V790_240[0][1][0][0]) and (shen_consp(KL_ARG_V790_240[0][1][0][1]) and (shen_eq([], KL_ARG_V790_240[0][1][0][1][1]) and shen_eq([], KL_ARG_V790_240[0][1][1])))))))) else ([KL_ARG_V790_240[0], tco_apply(shen_encodex45choices, [KL_ARG_V790_240[1], KL_ARG_V791_241])] if (shen_consp(KL_ARG_V790_240) and (shen_consp(KL_ARG_V790_240[0]) and (shen_consp(KL_ARG_V790_240[0][1]) and shen_eq([], KL_ARG_V790_240[0][1][1])))) else (tail_call(shen_sysx45error, [symdic.symdic_shen_encodex45choices]) if True else shen_simple_error('condition failure')))))))
shen_add_fun('shen.encode-choices', shen_encodex45choices)

@tail_recursion
def shen_casex45form(KL_ARG_V796_242, KL_ARG_V797_243):
    global symdic
    return ([KL_ARG_V797_243, []] if shen_eq([], KL_ARG_V796_242) else ([[True, KL_ARG_V796_242[0][1]], tco_apply(shen_casex45form, [KL_ARG_V796_242[1], KL_ARG_V797_243])] if (shen_consp(KL_ARG_V796_242) and (shen_consp(KL_ARG_V796_242[0]) and (shen_consp(KL_ARG_V796_242[0][0]) and (shen_eq(symdic.symdic_kl_x58, KL_ARG_V796_242[0][0][0]) and (shen_consp(KL_ARG_V796_242[0][0][1]) and (shen_eq(symdic.symdic_shen_tests, KL_ARG_V796_242[0][0][1][0]) and (shen_eq([], KL_ARG_V796_242[0][0][1][1]) and (shen_consp(KL_ARG_V796_242[0][1]) and (shen_consp(KL_ARG_V796_242[0][1][0]) and (shen_eq(symdic.symdic_shen_choicepointx33, KL_ARG_V796_242[0][1][0][0]) and (shen_consp(KL_ARG_V796_242[0][1][0][1]) and (shen_eq([], KL_ARG_V796_242[0][1][0][1][1]) and shen_eq([], KL_ARG_V796_242[0][1][1]))))))))))))) else ([[True, KL_ARG_V796_242[0][1]], []] if (shen_consp(KL_ARG_V796_242) and (shen_consp(KL_ARG_V796_242[0]) and (shen_consp(KL_ARG_V796_242[0][0]) and (shen_eq(symdic.symdic_kl_x58, KL_ARG_V796_242[0][0][0]) and (shen_consp(KL_ARG_V796_242[0][0][1]) and (shen_eq(symdic.symdic_shen_tests, KL_ARG_V796_242[0][0][1][0]) and (shen_eq([], KL_ARG_V796_242[0][0][1][1]) and (shen_consp(KL_ARG_V796_242[0][1]) and shen_eq([], KL_ARG_V796_242[0][1][1]))))))))) else ([[tco_apply(shen_embedx45and, [KL_ARG_V796_242[0][0][1][1]]), KL_ARG_V796_242[0][1]], tco_apply(shen_casex45form, [KL_ARG_V796_242[1], KL_ARG_V797_243])] if (shen_consp(KL_ARG_V796_242) and (shen_consp(KL_ARG_V796_242[0]) and (shen_consp(KL_ARG_V796_242[0][0]) and (shen_eq(symdic.symdic_kl_x58, KL_ARG_V796_242[0][0][0]) and (shen_consp(KL_ARG_V796_242[0][0][1]) and (shen_eq(symdic.symdic_shen_tests, KL_ARG_V796_242[0][0][1][0]) and (shen_consp(KL_ARG_V796_242[0][1]) and shen_eq([], KL_ARG_V796_242[0][1][1])))))))) else (tail_call(shen_sysx45error, [symdic.symdic_shen_casex45form]) if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.case-form', shen_casex45form)

@tail_recursion
def shen_embedx45and(KL_ARG_V798_244):
    global symdic
    return (KL_ARG_V798_244[0] if (shen_consp(KL_ARG_V798_244) and shen_eq([], KL_ARG_V798_244[1])) else ([symdic.symdic_kl_and, [KL_ARG_V798_244[0], [tco_apply(shen_embedx45and, [KL_ARG_V798_244[1]]), []]]] if shen_consp(KL_ARG_V798_244) else (tail_call(shen_sysx45error, [symdic.symdic_shen_embedx45and]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.embed-and', shen_embedx45and)

@tail_recursion
def shen_errx45condition(KL_ARG_V799_245):
    global symdic
    return [True, [[symdic.symdic_shen_f_error, [KL_ARG_V799_245, []]], []]]
shen_add_fun('shen.err-condition', shen_errx45condition)

@tail_recursion
def shen_sysx45error(KL_ARG_V800_246):
    global symdic
    return shen_simple_error(('system function ' + tco_apply(shen_app, [KL_ARG_V800_246, ': unexpected argument\r\n', symdic.symdic_shen_a])))
shen_add_fun('shen.sys-error', shen_sysx45error)


#============================== sys.kl==============================



@tail_recursion
def kl_thaw(KL_ARG_V1759_247):
    global symdic
    return shen_apply(KL_ARG_V1759_247, [])
shen_add_fun('thaw', kl_thaw)

@tail_recursion
def kl_eval(KL_ARG_V1760_248):

    class KL_Context:
        KL_LOC_Macroexpand_249 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Macroexpand_249', tco_apply(shen_walk, [(lambda KL_ARG_V1757_250: tail_call(kl_macroexpand, [KL_ARG_V1757_250])), KL_ARG_V1760_248])), (tail_call(kl_map, [symdic.symdic_shen_evalx45withoutx45macros, tco_apply(shen_packagex45contents, [KL_CTX.KL_LOC_Macroexpand_249])]) if tco_apply(shen_packagedx63, [KL_CTX.KL_LOC_Macroexpand_249]) else tail_call(shen_evalx45withoutx45macros, [KL_CTX.KL_LOC_Macroexpand_249]))][(-1)]
shen_add_fun('eval', kl_eval)

@tail_recursion
def shen_evalx45withoutx45macros(KL_ARG_V1761_251):
    global symdic
    return shen_eval_kl(tco_apply(shen_elimx45define, [tco_apply(shen_procx45inputx43, [KL_ARG_V1761_251])]))
shen_add_fun('shen.eval-without-macros', shen_evalx45withoutx45macros)

@tail_recursion
def shen_procx45inputx43(KL_ARG_V1762_252):
    global symdic
    return ([symdic.symdic_kl_inputx43, [KL_ARG_V1762_252[1][0], [tco_apply(shen_rcons_form, [KL_ARG_V1762_252[1][1][0]]), []]]] if (shen_consp(KL_ARG_V1762_252) and (shen_eq(symdic.symdic_kl_inputx43, KL_ARG_V1762_252[0]) and (shen_consp(KL_ARG_V1762_252[1]) and (shen_consp(KL_ARG_V1762_252[1][1]) and shen_eq([], KL_ARG_V1762_252[1][1][1]))))) else (tail_call(kl_map, [symdic.symdic_shen_procx45inputx43, KL_ARG_V1762_252]) if shen_consp(KL_ARG_V1762_252) else (KL_ARG_V1762_252 if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.proc-input+', shen_procx45inputx43)

@tail_recursion
def shen_elimx45define(KL_ARG_V1763_253):
    global symdic
    return (tail_call(shen_shenx45x62kl, [KL_ARG_V1763_253[1][0], KL_ARG_V1763_253[1][1]]) if (shen_consp(KL_ARG_V1763_253) and (shen_eq(symdic.symdic_kl_define, KL_ARG_V1763_253[0]) and shen_consp(KL_ARG_V1763_253[1]))) else (tail_call(shen_elimx45define, [tco_apply(shen_yacc, [KL_ARG_V1763_253])]) if (shen_consp(KL_ARG_V1763_253) and (shen_eq(symdic.symdic_kl_defcc, KL_ARG_V1763_253[0]) and shen_consp(KL_ARG_V1763_253[1]))) else (tail_call(kl_map, [symdic.symdic_shen_elimx45define, KL_ARG_V1763_253]) if shen_consp(KL_ARG_V1763_253) else (KL_ARG_V1763_253 if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.elim-define', shen_elimx45define)

@tail_recursion
def shen_packagedx63(KL_ARG_V1770_254):
    global symdic
    return (True if (shen_consp(KL_ARG_V1770_254) and (shen_eq(symdic.symdic_kl_package, KL_ARG_V1770_254[0]) and (shen_consp(KL_ARG_V1770_254[1]) and shen_consp(KL_ARG_V1770_254[1][1])))) else (False if True else shen_simple_error('condition failure')))
shen_add_fun('shen.packaged?', shen_packagedx63)

@tail_recursion
def kl_external(KL_ARG_V1771_255):
    global symdic
    return shen_try_except((lambda : tco_apply(kl_get, [KL_ARG_V1771_255, symdic.symdic_shen_externalx45symbols, shen_get(symdic.symdic_kl_x42propertyx45vectorx42)])), (lambda KL_ARG_E_256: shen_simple_error(('package ' + tco_apply(shen_app, [KL_ARG_V1771_255, ' has not been used.\r\n', symdic.symdic_shen_a])))))
shen_add_fun('external', kl_external)

@tail_recursion
def shen_packagex45contents(KL_ARG_V1774_257):
    global symdic
    return (KL_ARG_V1774_257[1][1][1] if (shen_consp(KL_ARG_V1774_257) and (shen_eq(symdic.symdic_kl_package, KL_ARG_V1774_257[0]) and (shen_consp(KL_ARG_V1774_257[1]) and (shen_eq(symdic.symdic_kl_null, KL_ARG_V1774_257[1][0]) and shen_consp(KL_ARG_V1774_257[1][1]))))) else (tail_call(shen_packageh, [KL_ARG_V1774_257[1][0], KL_ARG_V1774_257[1][1][0], KL_ARG_V1774_257[1][1][1]]) if (shen_consp(KL_ARG_V1774_257) and (shen_eq(symdic.symdic_kl_package, KL_ARG_V1774_257[0]) and (shen_consp(KL_ARG_V1774_257[1]) and shen_consp(KL_ARG_V1774_257[1][1])))) else (tail_call(shen_sysx45error, [symdic.symdic_shen_packagex45contents]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.package-contents', shen_packagex45contents)

@tail_recursion
def shen_walk(KL_ARG_V1775_258, KL_ARG_V1776_259):
    global symdic
    return (shen_apply(KL_ARG_V1775_258, [tco_apply(kl_map, [(lambda KL_ARG_Z_260: tail_call(shen_walk, [KL_ARG_V1775_258, KL_ARG_Z_260])), KL_ARG_V1776_259])]) if shen_consp(KL_ARG_V1776_259) else (shen_apply(KL_ARG_V1775_258, [KL_ARG_V1776_259]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.walk', shen_walk)

@tail_recursion
def kl_compile(KL_ARG_V1777_261, KL_ARG_V1778_262, KL_ARG_V1779_263):

    class KL_Context:
        KL_LOC_O_264 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_O_264', shen_apply(KL_ARG_V1777_261, [[KL_ARG_V1778_262, [[], []]]])), (shen_apply(KL_ARG_V1779_263, [KL_CTX.KL_LOC_O_264]) if (shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_O_264) or (not tco_apply(kl_emptyx63, [KL_CTX.KL_LOC_O_264[0]]))) else tail_call(shen_hdtl, [KL_CTX.KL_LOC_O_264]))][(-1)]
shen_add_fun('compile', kl_compile)

@tail_recursion
def kl_failx45if(KL_ARG_V1780_265, KL_ARG_V1781_266):
    global symdic
    return (tail_call(kl_fail, []) if shen_apply(KL_ARG_V1780_265, [KL_ARG_V1781_266]) else KL_ARG_V1781_266)
shen_add_fun('fail-if', kl_failx45if)

@tail_recursion
def kl_x64s(KL_ARG_V1782_267, KL_ARG_V1783_268):
    global symdic
    return (KL_ARG_V1782_267 + KL_ARG_V1783_268)
shen_add_fun('@s', kl_x64s)

@tail_recursion
def kl_tcx63(KL_ARG_V1788_269):
    global symdic
    return shen_get(symdic.symdic_shen_x42tcx42)
shen_add_fun('tc?', kl_tcx63)

@tail_recursion
def kl_ps(KL_ARG_V1789_270):
    global symdic
    return shen_try_except((lambda : tco_apply(kl_get, [KL_ARG_V1789_270, symdic.symdic_shen_source, shen_get(symdic.symdic_kl_x42propertyx45vectorx42)])), (lambda KL_ARG_E_271: shen_simple_error(tco_apply(shen_app, [KL_ARG_V1789_270, ' not found.\r\n', symdic.symdic_shen_a]))))
shen_add_fun('ps', kl_ps)

@tail_recursion
def kl_stinput():
    global symdic
    return shen_get(symdic.symdic_kl_x42stinputx42)
shen_add_fun('stinput', kl_stinput)

@tail_recursion
def shen_x43vectorx63(KL_ARG_V1790_272):
    global symdic
    return (shen_absvectorp(KL_ARG_V1790_272) and (shen_absvector_get(KL_ARG_V1790_272, 0) > 0))
shen_add_fun('shen.+vector?', shen_x43vectorx63)

@tail_recursion
def kl_vector(KL_ARG_V1791_273):

    class KL_Context:
        KL_LOC_Vector_274 = None
        KL_LOC_ZeroStamp_275 = None
        KL_LOC_Standard_276 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Vector_274', shen_absvector((KL_ARG_V1791_273 + 1))), [setattr(KL_CTX, 'KL_LOC_ZeroStamp_275', shen_absvector_set(KL_CTX.KL_LOC_Vector_274, 0, KL_ARG_V1791_273)), [setattr(KL_CTX, 'KL_LOC_Standard_276', (KL_CTX.KL_LOC_ZeroStamp_275 if shen_eq(KL_ARG_V1791_273, 0) else tco_apply(shen_fillvector, [KL_CTX.KL_LOC_ZeroStamp_275, 1, KL_ARG_V1791_273, tco_apply(kl_fail, [])]))), KL_CTX.KL_LOC_Standard_276][(-1)]][(-1)]][(-1)]
shen_add_fun('vector', kl_vector)

@tail_recursion
def shen_fillvector(KL_ARG_V1792_277, KL_ARG_V1793_278, KL_ARG_V1794_279, KL_ARG_V1795_280):
    global symdic
    return (shen_absvector_set(KL_ARG_V1792_277, KL_ARG_V1794_279, KL_ARG_V1795_280) if shen_eq(KL_ARG_V1794_279, KL_ARG_V1793_278) else (tail_call(shen_fillvector, [shen_absvector_set(KL_ARG_V1792_277, KL_ARG_V1793_278, KL_ARG_V1795_280), (1 + KL_ARG_V1793_278), KL_ARG_V1794_279, KL_ARG_V1795_280]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.fillvector', shen_fillvector)

@tail_recursion
def kl_vectorx63(KL_ARG_V1797_281):
    global symdic
    return (shen_absvectorp(KL_ARG_V1797_281) and shen_try_except((lambda : (shen_absvector_get(KL_ARG_V1797_281, 0) >= 0)), (lambda KL_ARG_E_282: False)))
shen_add_fun('vector?', kl_vectorx63)

@tail_recursion
def kl_vectorx45x62(KL_ARG_V1798_283, KL_ARG_V1799_284, KL_ARG_V1800_285):
    global symdic
    return (shen_simple_error('cannot access 0th element of a vector\r\n') if shen_eq(KL_ARG_V1799_284, 0) else shen_absvector_set(KL_ARG_V1798_283, KL_ARG_V1799_284, KL_ARG_V1800_285))
shen_add_fun('vector->', kl_vectorx45x62)

@tail_recursion
def kl_x60x45vector(KL_ARG_V1801_286, KL_ARG_V1802_287):

    class KL_Context:
        KL_LOC_VectorElement_288 = None
    KL_CTX = KL_Context()
    global symdic
    return (shen_simple_error('cannot access 0th element of a vector\r\n') if shen_eq(KL_ARG_V1802_287, 0) else [setattr(KL_CTX, 'KL_LOC_VectorElement_288', shen_absvector_get(KL_ARG_V1801_286, KL_ARG_V1802_287)), (shen_simple_error('vector element not found\r\n') if shen_eq(KL_CTX.KL_LOC_VectorElement_288, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_VectorElement_288)][(-1)])
shen_add_fun('<-vector', kl_x60x45vector)

@tail_recursion
def shen_posintx63(KL_ARG_V1803_289):
    global symdic
    return (tco_apply(kl_integerx63, [KL_ARG_V1803_289]) and (KL_ARG_V1803_289 >= 0))
shen_add_fun('shen.posint?', shen_posintx63)

@tail_recursion
def kl_limit(KL_ARG_V1804_290):
    global symdic
    return shen_absvector_get(KL_ARG_V1804_290, 0)
shen_add_fun('limit', kl_limit)

@tail_recursion
def kl_symbolx63(KL_ARG_V1805_291):

    class KL_Context:
        KL_LOC_String_292 = None
    KL_CTX = KL_Context()
    global symdic
    return (False if (tco_apply(kl_booleanx63, [KL_ARG_V1805_291]) or (isinstance(KL_ARG_V1805_291, numbers.Number) or isinstance(KL_ARG_V1805_291, str))) else (shen_try_except((lambda : [setattr(KL_CTX, 'KL_LOC_String_292', str(KL_ARG_V1805_291)), tco_apply(shen_analysex45symbolx63, [KL_CTX.KL_LOC_String_292])][(-1)]), (lambda KL_ARG_E_293: False)) if True else shen_simple_error('condition failure')))
shen_add_fun('symbol?', kl_symbolx63)

@tail_recursion
def shen_analysex45symbolx63(KL_ARG_V1806_294):
    global symdic
    return ((tco_apply(shen_alphax63, [KL_ARG_V1806_294[0]]) and tco_apply(shen_alphanumsx63, [KL_ARG_V1806_294[1:]])) if tco_apply(shen_x43stringx63, [KL_ARG_V1806_294]) else (tail_call(shen_sysx45error, [symdic.symdic_shen_analysex45symbolx63]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.analyse-symbol?', shen_analysex45symbolx63)

@tail_recursion
def shen_alphax63(KL_ARG_V1807_295):
    global symdic
    return tail_call(kl_elementx63, [KL_ARG_V1807_295, ['A', ['B', ['C', ['D', ['E', ['F', ['G', ['H', ['I', ['J', ['K', ['L', ['M', ['N', ['O', ['P', ['Q', ['R', ['S', ['T', ['U', ['V', ['W', ['X', ['Y', ['Z', ['a', ['b', ['c', ['d', ['e', ['f', ['g', ['h', ['i', ['j', ['k', ['l', ['m', ['n', ['o', ['p', ['q', ['r', ['s', ['t', ['u', ['v', ['w', ['x', ['y', ['z', ['=', ['*', ['/', ['+', ['-', ['_', ['?', ['$', ['!', ['@', ['~', ['>', ['<', ['&', ['%', ['{', ['}', [':', [';', ['`', ['#', ["'", ['.', []]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]])
shen_add_fun('shen.alpha?', shen_alphax63)

@tail_recursion
def shen_alphanumsx63(KL_ARG_V1808_296):
    global symdic
    return (True if shen_eq('', KL_ARG_V1808_296) else ((tco_apply(shen_alphanumx63, [KL_ARG_V1808_296[0]]) and tco_apply(shen_alphanumsx63, [KL_ARG_V1808_296[1:]])) if tco_apply(shen_x43stringx63, [KL_ARG_V1808_296]) else (tail_call(shen_sysx45error, [symdic.symdic_shen_alphanumsx63]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.alphanums?', shen_alphanumsx63)

@tail_recursion
def shen_alphanumx63(KL_ARG_V1809_297):
    global symdic
    return (tco_apply(shen_alphax63, [KL_ARG_V1809_297]) or tco_apply(shen_digitx63, [KL_ARG_V1809_297]))
shen_add_fun('shen.alphanum?', shen_alphanumx63)

@tail_recursion
def shen_digitx63(KL_ARG_V1810_298):
    global symdic
    return tail_call(kl_elementx63, [KL_ARG_V1810_298, ['1', ['2', ['3', ['4', ['5', ['6', ['7', ['8', ['9', ['0', []]]]]]]]]]]])
shen_add_fun('shen.digit?', shen_digitx63)

@tail_recursion
def kl_variablex63(KL_ARG_V1811_299):

    class KL_Context:
        KL_LOC_String_300 = None
    KL_CTX = KL_Context()
    global symdic
    return (False if (tco_apply(kl_booleanx63, [KL_ARG_V1811_299]) or (isinstance(KL_ARG_V1811_299, numbers.Number) or isinstance(KL_ARG_V1811_299, str))) else (shen_try_except((lambda : [setattr(KL_CTX, 'KL_LOC_String_300', str(KL_ARG_V1811_299)), tco_apply(shen_analysex45variablex63, [KL_CTX.KL_LOC_String_300])][(-1)]), (lambda KL_ARG_E_301: False)) if True else shen_simple_error('condition failure')))
shen_add_fun('variable?', kl_variablex63)

@tail_recursion
def shen_analysex45variablex63(KL_ARG_V1812_302):
    global symdic
    return ((tco_apply(shen_uppercasex63, [KL_ARG_V1812_302[0]]) and tco_apply(shen_alphanumsx63, [KL_ARG_V1812_302[1:]])) if tco_apply(shen_x43stringx63, [KL_ARG_V1812_302]) else (tail_call(shen_sysx45error, [symdic.symdic_shen_analysex45variablex63]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.analyse-variable?', shen_analysex45variablex63)

@tail_recursion
def shen_uppercasex63(KL_ARG_V1813_303):
    global symdic
    return tail_call(kl_elementx63, [KL_ARG_V1813_303, ['A', ['B', ['C', ['D', ['E', ['F', ['G', ['H', ['I', ['J', ['K', ['L', ['M', ['N', ['O', ['P', ['Q', ['R', ['S', ['T', ['U', ['V', ['W', ['X', ['Y', ['Z', []]]]]]]]]]]]]]]]]]]]]]]]]]]])
shen_add_fun('shen.uppercase?', shen_uppercasex63)

@tail_recursion
def kl_gensym(KL_ARG_V1814_304):
    global symdic
    return tail_call(kl_concat, [KL_ARG_V1814_304, shen_set(symdic.symdic_shen_x42gensymx42, (1 + shen_get(symdic.symdic_shen_x42gensymx42)))])
shen_add_fun('gensym', kl_gensym)

@tail_recursion
def kl_concat(KL_ARG_V1815_305, KL_ARG_V1816_306):
    global symdic
    return shen_intern((str(KL_ARG_V1815_305) + str(KL_ARG_V1816_306)))
shen_add_fun('concat', kl_concat)

@tail_recursion
def kl_x64p(KL_ARG_V1817_307, KL_ARG_V1818_308):

    class KL_Context:
        KL_LOC_Vector_309 = None
        KL_LOC_Tag_310 = None
        KL_LOC_Fst_311 = None
        KL_LOC_Snd_312 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Vector_309', shen_absvector(3)), [setattr(KL_CTX, 'KL_LOC_Tag_310', shen_absvector_set(KL_CTX.KL_LOC_Vector_309, 0, symdic.symdic_shen_tuple)), [setattr(KL_CTX, 'KL_LOC_Fst_311', shen_absvector_set(KL_CTX.KL_LOC_Vector_309, 1, KL_ARG_V1817_307)), [setattr(KL_CTX, 'KL_LOC_Snd_312', shen_absvector_set(KL_CTX.KL_LOC_Vector_309, 2, KL_ARG_V1818_308)), KL_CTX.KL_LOC_Vector_309][(-1)]][(-1)]][(-1)]][(-1)]
shen_add_fun('@p', kl_x64p)

@tail_recursion
def kl_fst(KL_ARG_V1819_313):
    global symdic
    return shen_absvector_get(KL_ARG_V1819_313, 1)
shen_add_fun('fst', kl_fst)

@tail_recursion
def kl_snd(KL_ARG_V1820_314):
    global symdic
    return shen_absvector_get(KL_ARG_V1820_314, 2)
shen_add_fun('snd', kl_snd)

@tail_recursion
def kl_tuplex63(KL_ARG_V1821_315):
    global symdic
    return shen_try_except((lambda : (shen_absvectorp(KL_ARG_V1821_315) and shen_eq(symdic.symdic_shen_tuple, shen_absvector_get(KL_ARG_V1821_315, 0)))), (lambda KL_ARG_E_316: False))
shen_add_fun('tuple?', kl_tuplex63)

@tail_recursion
def kl_append(KL_ARG_V1822_317, KL_ARG_V1823_318):
    global symdic
    return (KL_ARG_V1823_318 if shen_eq([], KL_ARG_V1822_317) else ([KL_ARG_V1822_317[0], tco_apply(kl_append, [KL_ARG_V1822_317[1], KL_ARG_V1823_318])] if shen_consp(KL_ARG_V1822_317) else (tail_call(shen_sysx45error, [symdic.symdic_kl_append]) if True else shen_simple_error('condition failure'))))
shen_add_fun('append', kl_append)

@tail_recursion
def kl_x64v(KL_ARG_V1824_319, KL_ARG_V1825_320):

    class KL_Context:
        KL_LOC_Limit_321 = None
        KL_LOC_NewVector_322 = None
        KL_LOC_Xx43NewVector_323 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Limit_321', tco_apply(kl_limit, [KL_ARG_V1825_320])), [setattr(KL_CTX, 'KL_LOC_NewVector_322', tco_apply(kl_vector, [(KL_CTX.KL_LOC_Limit_321 + 1)])), [setattr(KL_CTX, 'KL_LOC_Xx43NewVector_323', tco_apply(kl_vectorx45x62, [KL_CTX.KL_LOC_NewVector_322, 1, KL_ARG_V1824_319])), (KL_CTX.KL_LOC_Xx43NewVector_323 if shen_eq(KL_CTX.KL_LOC_Limit_321, 0) else tail_call(shen_x64vx45help, [KL_ARG_V1825_320, 1, KL_CTX.KL_LOC_Limit_321, KL_CTX.KL_LOC_Xx43NewVector_323]))][(-1)]][(-1)]][(-1)]
shen_add_fun('@v', kl_x64v)

@tail_recursion
def shen_x64vx45help(KL_ARG_V1826_324, KL_ARG_V1827_325, KL_ARG_V1828_326, KL_ARG_V1829_327):
    global symdic
    return (tail_call(shen_copyfromvector, [KL_ARG_V1826_324, KL_ARG_V1829_327, KL_ARG_V1828_326, (KL_ARG_V1828_326 + 1)]) if shen_eq(KL_ARG_V1828_326, KL_ARG_V1827_325) else (tail_call(shen_x64vx45help, [KL_ARG_V1826_324, (KL_ARG_V1827_325 + 1), KL_ARG_V1828_326, tco_apply(shen_copyfromvector, [KL_ARG_V1826_324, KL_ARG_V1829_327, KL_ARG_V1827_325, (KL_ARG_V1827_325 + 1)])]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.@v-help', shen_x64vx45help)

@tail_recursion
def shen_copyfromvector(KL_ARG_V1831_328, KL_ARG_V1832_329, KL_ARG_V1833_330, KL_ARG_V1834_331):
    global symdic
    return shen_try_except((lambda : tco_apply(kl_vectorx45x62, [KL_ARG_V1832_329, KL_ARG_V1834_331, tco_apply(kl_x60x45vector, [KL_ARG_V1831_328, KL_ARG_V1833_330])])), (lambda KL_ARG_E_332: KL_ARG_V1832_329))
shen_add_fun('shen.copyfromvector', shen_copyfromvector)

@tail_recursion
def kl_hdv(KL_ARG_V1835_333):
    global symdic
    return shen_try_except((lambda : tco_apply(kl_x60x45vector, [KL_ARG_V1835_333, 1])), (lambda KL_ARG_E_334: shen_simple_error(('hdv needs a non-empty vector as an argument; not ' + tco_apply(shen_app, [KL_ARG_V1835_333, '\r\n', symdic.symdic_shen_s])))))
shen_add_fun('hdv', kl_hdv)

@tail_recursion
def kl_tlv(KL_ARG_V1836_335):

    class KL_Context:
        KL_LOC_Limit_336 = None
        KL_LOC_NewVector_337 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Limit_336', tco_apply(kl_limit, [KL_ARG_V1836_335])), (shen_simple_error('cannot take the tail of the empty vector\r\n') if shen_eq(KL_CTX.KL_LOC_Limit_336, 0) else (tail_call(kl_vector, [0]) if shen_eq(KL_CTX.KL_LOC_Limit_336, 1) else [setattr(KL_CTX, 'KL_LOC_NewVector_337', tco_apply(kl_vector, [(KL_CTX.KL_LOC_Limit_336 - 1)])), tail_call(shen_tlvx45help, [KL_ARG_V1836_335, 2, KL_CTX.KL_LOC_Limit_336, tco_apply(kl_vector, [(KL_CTX.KL_LOC_Limit_336 - 1)])])][(-1)]))][(-1)]
shen_add_fun('tlv', kl_tlv)

@tail_recursion
def shen_tlvx45help(KL_ARG_V1837_338, KL_ARG_V1838_339, KL_ARG_V1839_340, KL_ARG_V1840_341):
    global symdic
    return (tail_call(shen_copyfromvector, [KL_ARG_V1837_338, KL_ARG_V1840_341, KL_ARG_V1839_340, (KL_ARG_V1839_340 - 1)]) if shen_eq(KL_ARG_V1839_340, KL_ARG_V1838_339) else (tail_call(shen_tlvx45help, [KL_ARG_V1837_338, (KL_ARG_V1838_339 + 1), KL_ARG_V1839_340, tco_apply(shen_copyfromvector, [KL_ARG_V1837_338, KL_ARG_V1840_341, KL_ARG_V1838_339, (KL_ARG_V1838_339 - 1)])]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.tlv-help', shen_tlvx45help)

@tail_recursion
def kl_assoc(KL_ARG_V1850_342, KL_ARG_V1851_343):
    global symdic
    return ([] if shen_eq([], KL_ARG_V1851_343) else (KL_ARG_V1851_343[0] if (shen_consp(KL_ARG_V1851_343) and (shen_consp(KL_ARG_V1851_343[0]) and shen_eq(KL_ARG_V1851_343[0][0], KL_ARG_V1850_342))) else (tail_call(kl_assoc, [KL_ARG_V1850_342, KL_ARG_V1851_343[1]]) if shen_consp(KL_ARG_V1851_343) else (tail_call(shen_sysx45error, [symdic.symdic_kl_assoc]) if True else shen_simple_error('condition failure')))))
shen_add_fun('assoc', kl_assoc)

@tail_recursion
def kl_booleanx63(KL_ARG_V1857_344):
    global symdic
    return (True if shen_eq(True, KL_ARG_V1857_344) else (True if shen_eq(False, KL_ARG_V1857_344) else (False if True else shen_simple_error('condition failure'))))
shen_add_fun('boolean?', kl_booleanx63)

@tail_recursion
def kl_nl(KL_ARG_V1858_345):
    global symdic
    return (0 if shen_eq(0, KL_ARG_V1858_345) else ([shen_pr('\r\n', tco_apply(kl_stoutput, [])), tail_call(kl_nl, [(KL_ARG_V1858_345 - 1)])][(-1)] if True else shen_simple_error('condition failure')))
shen_add_fun('nl', kl_nl)

@tail_recursion
def kl_difference(KL_ARG_V1861_346, KL_ARG_V1862_347):
    global symdic
    return ([] if shen_eq([], KL_ARG_V1861_346) else ((tail_call(kl_difference, [KL_ARG_V1861_346[1], KL_ARG_V1862_347]) if tco_apply(kl_elementx63, [KL_ARG_V1861_346[0], KL_ARG_V1862_347]) else [KL_ARG_V1861_346[0], tco_apply(kl_difference, [KL_ARG_V1861_346[1], KL_ARG_V1862_347])]) if shen_consp(KL_ARG_V1861_346) else (tail_call(shen_sysx45error, [symdic.symdic_kl_difference]) if True else shen_simple_error('condition failure'))))
shen_add_fun('difference', kl_difference)

@tail_recursion
def kl_do(KL_ARG_V1863_348, KL_ARG_V1864_349):
    global symdic
    return KL_ARG_V1864_349
shen_add_fun('do', kl_do)

@tail_recursion
def kl_elementx63(KL_ARG_V1873_350, KL_ARG_V1874_351):
    global symdic
    return (False if shen_eq([], KL_ARG_V1874_351) else (True if (shen_consp(KL_ARG_V1874_351) and shen_eq(KL_ARG_V1874_351[0], KL_ARG_V1873_350)) else (tail_call(kl_elementx63, [KL_ARG_V1873_350, KL_ARG_V1874_351[1]]) if shen_consp(KL_ARG_V1874_351) else (tail_call(shen_sysx45error, [symdic.symdic_kl_elementx63]) if True else shen_simple_error('condition failure')))))
shen_add_fun('element?', kl_elementx63)

@tail_recursion
def kl_emptyx63(KL_ARG_V1880_352):
    global symdic
    return (True if shen_eq([], KL_ARG_V1880_352) else (False if True else shen_simple_error('condition failure')))
shen_add_fun('empty?', kl_emptyx63)

@tail_recursion
def kl_fix(KL_ARG_V1881_353, KL_ARG_V1882_354):
    global symdic
    return tail_call(shen_fixx45help, [KL_ARG_V1881_353, KL_ARG_V1882_354, shen_apply(KL_ARG_V1881_353, [KL_ARG_V1882_354])])
shen_add_fun('fix', kl_fix)

@tail_recursion
def shen_fixx45help(KL_ARG_V1889_355, KL_ARG_V1890_356, KL_ARG_V1891_357):
    global symdic
    return (KL_ARG_V1891_357 if shen_eq(KL_ARG_V1891_357, KL_ARG_V1890_356) else (tail_call(shen_fixx45help, [KL_ARG_V1889_355, KL_ARG_V1891_357, shen_apply(KL_ARG_V1889_355, [KL_ARG_V1891_357])]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.fix-help', shen_fixx45help)

@tail_recursion
def kl_put(KL_ARG_V1893_358, KL_ARG_V1894_359, KL_ARG_V1895_360, KL_ARG_V1896_361):

    class KL_Context:
        KL_LOC_N_362 = None
        KL_LOC_Entry_363 = None
        KL_LOC_Change_365 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_N_362', tco_apply(kl_hash, [KL_ARG_V1893_358, tco_apply(kl_limit, [KL_ARG_V1896_361])])), [setattr(KL_CTX, 'KL_LOC_Entry_363', shen_try_except((lambda : tco_apply(kl_x60x45vector, [KL_ARG_V1896_361, KL_CTX.KL_LOC_N_362])), (lambda KL_ARG_E_364: []))), [setattr(KL_CTX, 'KL_LOC_Change_365', tco_apply(kl_vectorx45x62, [KL_ARG_V1896_361, KL_CTX.KL_LOC_N_362, tco_apply(shen_changex45pointerx45value, [KL_ARG_V1893_358, KL_ARG_V1894_359, KL_ARG_V1895_360, KL_CTX.KL_LOC_Entry_363])])), KL_ARG_V1895_360][(-1)]][(-1)]][(-1)]
shen_add_fun('put', kl_put)

@tail_recursion
def shen_changex45pointerx45value(KL_ARG_V1899_366, KL_ARG_V1900_367, KL_ARG_V1901_368, KL_ARG_V1902_369):
    global symdic
    return ([[[KL_ARG_V1899_366, [KL_ARG_V1900_367, []]], KL_ARG_V1901_368], []] if shen_eq([], KL_ARG_V1902_369) else ([[KL_ARG_V1902_369[0][0], KL_ARG_V1901_368], KL_ARG_V1902_369[1]] if (shen_consp(KL_ARG_V1902_369) and (shen_consp(KL_ARG_V1902_369[0]) and (shen_consp(KL_ARG_V1902_369[0][0]) and (shen_consp(KL_ARG_V1902_369[0][0][1]) and (shen_eq([], KL_ARG_V1902_369[0][0][1][1]) and (shen_eq(KL_ARG_V1902_369[0][0][1][0], KL_ARG_V1900_367) and shen_eq(KL_ARG_V1902_369[0][0][0], KL_ARG_V1899_366))))))) else ([KL_ARG_V1902_369[0], tco_apply(shen_changex45pointerx45value, [KL_ARG_V1899_366, KL_ARG_V1900_367, KL_ARG_V1901_368, KL_ARG_V1902_369[1]])] if shen_consp(KL_ARG_V1902_369) else (tail_call(shen_sysx45error, [symdic.symdic_shen_changex45pointerx45value]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.change-pointer-value', shen_changex45pointerx45value)

@tail_recursion
def kl_get(KL_ARG_V1905_370, KL_ARG_V1906_371, KL_ARG_V1907_372):

    class KL_Context:
        KL_LOC_N_373 = None
        KL_LOC_Entry_374 = None
        KL_LOC_Result_376 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_N_373', tco_apply(kl_hash, [KL_ARG_V1905_370, tco_apply(kl_limit, [KL_ARG_V1907_372])])), [setattr(KL_CTX, 'KL_LOC_Entry_374', shen_try_except((lambda : tco_apply(kl_x60x45vector, [KL_ARG_V1907_372, KL_CTX.KL_LOC_N_373])), (lambda KL_ARG_E_375: shen_simple_error('pointer not found\r\n')))), [setattr(KL_CTX, 'KL_LOC_Result_376', tco_apply(kl_assoc, [[KL_ARG_V1905_370, [KL_ARG_V1906_371, []]], KL_CTX.KL_LOC_Entry_374])), (shen_simple_error('value not found\r\n') if tco_apply(kl_emptyx63, [KL_CTX.KL_LOC_Result_376]) else KL_CTX.KL_LOC_Result_376[1])][(-1)]][(-1)]][(-1)]
shen_add_fun('get', kl_get)

@tail_recursion
def kl_hash(KL_ARG_V1908_377, KL_ARG_V1909_378):

    class KL_Context:
        KL_LOC_Hash_379 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Hash_379', tco_apply(shen_mod, [tco_apply(shen_sum, [tco_apply(kl_map, [(lambda KL_ARG_V1758_380: ord(KL_ARG_V1758_380)), tco_apply(kl_explode, [KL_ARG_V1908_377])])]), KL_ARG_V1909_378])), (1 if shen_eq(0, KL_CTX.KL_LOC_Hash_379) else KL_CTX.KL_LOC_Hash_379)][(-1)]
shen_add_fun('hash', kl_hash)

@tail_recursion
def shen_mod(KL_ARG_V1910_381, KL_ARG_V1911_382):
    global symdic
    return tail_call(shen_modh, [KL_ARG_V1910_381, tco_apply(shen_multiples, [KL_ARG_V1910_381, [KL_ARG_V1911_382, []]])])
shen_add_fun('shen.mod', shen_mod)

@tail_recursion
def shen_multiples(KL_ARG_V1912_383, KL_ARG_V1913_384):
    global symdic
    return (KL_ARG_V1913_384[1] if (shen_consp(KL_ARG_V1913_384) and (KL_ARG_V1913_384[0] > KL_ARG_V1912_383)) else (tail_call(shen_multiples, [KL_ARG_V1912_383, [(2 * KL_ARG_V1913_384[0]), KL_ARG_V1913_384]]) if shen_consp(KL_ARG_V1913_384) else (tail_call(shen_sysx45error, [symdic.symdic_shen_multiples]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.multiples', shen_multiples)

@tail_recursion
def shen_modh(KL_ARG_V1916_385, KL_ARG_V1917_386):
    global symdic
    return (0 if shen_eq(0, KL_ARG_V1916_385) else (KL_ARG_V1916_385 if shen_eq([], KL_ARG_V1917_386) else ((KL_ARG_V1916_385 if tco_apply(kl_emptyx63, [KL_ARG_V1917_386[1]]) else tail_call(shen_modh, [KL_ARG_V1916_385, KL_ARG_V1917_386[1]])) if (shen_consp(KL_ARG_V1917_386) and (KL_ARG_V1917_386[0] > KL_ARG_V1916_385)) else (tail_call(shen_modh, [(KL_ARG_V1916_385 - KL_ARG_V1917_386[0]), KL_ARG_V1917_386]) if shen_consp(KL_ARG_V1917_386) else (tail_call(shen_sysx45error, [symdic.symdic_shen_modh]) if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.modh', shen_modh)

@tail_recursion
def shen_sum(KL_ARG_V1918_387):
    global symdic
    return (0 if shen_eq([], KL_ARG_V1918_387) else ((KL_ARG_V1918_387[0] + tco_apply(shen_sum, [KL_ARG_V1918_387[1]])) if shen_consp(KL_ARG_V1918_387) else (tail_call(shen_sysx45error, [symdic.symdic_shen_sum]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.sum', shen_sum)

@tail_recursion
def kl_head(KL_ARG_V1925_388):
    global symdic
    return (KL_ARG_V1925_388[0] if shen_consp(KL_ARG_V1925_388) else (shen_simple_error('head expects a non-empty list') if True else shen_simple_error('condition failure')))
shen_add_fun('head', kl_head)

@tail_recursion
def kl_tail(KL_ARG_V1932_389):
    global symdic
    return (KL_ARG_V1932_389[1] if shen_consp(KL_ARG_V1932_389) else (shen_simple_error('tail expects a non-empty list') if True else shen_simple_error('condition failure')))
shen_add_fun('tail', kl_tail)

@tail_recursion
def kl_hdstr(KL_ARG_V1933_390):
    global symdic
    return KL_ARG_V1933_390[0]
shen_add_fun('hdstr', kl_hdstr)

@tail_recursion
def kl_intersection(KL_ARG_V1936_391, KL_ARG_V1937_392):
    global symdic
    return ([] if shen_eq([], KL_ARG_V1936_391) else (([KL_ARG_V1936_391[0], tco_apply(kl_intersection, [KL_ARG_V1936_391[1], KL_ARG_V1937_392])] if tco_apply(kl_elementx63, [KL_ARG_V1936_391[0], KL_ARG_V1937_392]) else tail_call(kl_intersection, [KL_ARG_V1936_391[1], KL_ARG_V1937_392])) if shen_consp(KL_ARG_V1936_391) else (tail_call(shen_sysx45error, [symdic.symdic_kl_intersection]) if True else shen_simple_error('condition failure'))))
shen_add_fun('intersection', kl_intersection)

@tail_recursion
def kl_reverse(KL_ARG_V1938_393):
    global symdic
    return tail_call(shen_reverse_help, [KL_ARG_V1938_393, []])
shen_add_fun('reverse', kl_reverse)

@tail_recursion
def shen_reverse_help(KL_ARG_V1939_394, KL_ARG_V1940_395):
    global symdic
    return (KL_ARG_V1940_395 if shen_eq([], KL_ARG_V1939_394) else (tail_call(shen_reverse_help, [KL_ARG_V1939_394[1], [KL_ARG_V1939_394[0], KL_ARG_V1940_395]]) if shen_consp(KL_ARG_V1939_394) else (tail_call(shen_sysx45error, [symdic.symdic_shen_reverse_help]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.reverse_help', shen_reverse_help)

@tail_recursion
def kl_union(KL_ARG_V1941_396, KL_ARG_V1942_397):
    global symdic
    return (KL_ARG_V1942_397 if shen_eq([], KL_ARG_V1941_396) else ((tail_call(kl_union, [KL_ARG_V1941_396[1], KL_ARG_V1942_397]) if tco_apply(kl_elementx63, [KL_ARG_V1941_396[0], KL_ARG_V1942_397]) else [KL_ARG_V1941_396[0], tco_apply(kl_union, [KL_ARG_V1941_396[1], KL_ARG_V1942_397])]) if shen_consp(KL_ARG_V1941_396) else (tail_call(shen_sysx45error, [symdic.symdic_kl_union]) if True else shen_simple_error('condition failure'))))
shen_add_fun('union', kl_union)

@tail_recursion
def kl_yx45orx45nx63(KL_ARG_V1943_398):

    class KL_Context:
        KL_LOC_Message_399 = None
        KL_LOC_Yx45orx45N_400 = None
        KL_LOC_Input_401 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Message_399', shen_pr(tco_apply(shen_procx45nl, [KL_ARG_V1943_398]), tco_apply(kl_stoutput, []))), [setattr(KL_CTX, 'KL_LOC_Yx45orx45N_400', shen_pr(' (y/n) ', tco_apply(kl_stoutput, []))), [setattr(KL_CTX, 'KL_LOC_Input_401', tco_apply(shen_app, [tco_apply(kl_input, []), '', symdic.symdic_shen_s])), (True if shen_eq('y', KL_CTX.KL_LOC_Input_401) else (False if shen_eq('n', KL_CTX.KL_LOC_Input_401) else [shen_pr('please answer y or n\r\n', tco_apply(kl_stoutput, [])), tail_call(kl_yx45orx45nx63, [KL_ARG_V1943_398])][(-1)]))][(-1)]][(-1)]][(-1)]
shen_add_fun('y-or-n?', kl_yx45orx45nx63)

@tail_recursion
def kl_not(KL_ARG_V1944_402):
    global symdic
    return (False if KL_ARG_V1944_402 else True)
shen_add_fun('not', kl_not)

@tail_recursion
def kl_subst(KL_ARG_V1953_403, KL_ARG_V1954_404, KL_ARG_V1955_405):
    global symdic
    return (KL_ARG_V1953_403 if shen_eq(KL_ARG_V1955_405, KL_ARG_V1954_404) else ([tco_apply(kl_subst, [KL_ARG_V1953_403, KL_ARG_V1954_404, KL_ARG_V1955_405[0]]), tco_apply(kl_subst, [KL_ARG_V1953_403, KL_ARG_V1954_404, KL_ARG_V1955_405[1]])] if shen_consp(KL_ARG_V1955_405) else (KL_ARG_V1955_405 if True else shen_simple_error('condition failure'))))
shen_add_fun('subst', kl_subst)

@tail_recursion
def kl_explode(KL_ARG_V1957_406):
    global symdic
    return tail_call(shen_explodex45h, [tco_apply(shen_app, [KL_ARG_V1957_406, '', symdic.symdic_shen_a])])
shen_add_fun('explode', kl_explode)

@tail_recursion
def shen_explodex45h(KL_ARG_V1958_407):
    global symdic
    return ([] if shen_eq('', KL_ARG_V1958_407) else ([KL_ARG_V1958_407[0], tco_apply(shen_explodex45h, [KL_ARG_V1958_407[1:]])] if tco_apply(shen_x43stringx63, [KL_ARG_V1958_407]) else (tail_call(shen_sysx45error, [symdic.symdic_shen_explodex45h]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.explode-h', shen_explodex45h)

@tail_recursion
def kl_cd(KL_ARG_V1959_408):
    global symdic
    return shen_set(symdic.symdic_kl_x42homex45directoryx42, ('' if shen_eq(KL_ARG_V1959_408, '') else tco_apply(shen_app, [KL_ARG_V1959_408, '/', symdic.symdic_shen_a])))
shen_add_fun('cd', kl_cd)

@tail_recursion
def kl_map(KL_ARG_V1960_409, KL_ARG_V1961_410):
    global symdic
    return tail_call(shen_mapx45h, [KL_ARG_V1960_409, KL_ARG_V1961_410, []])
shen_add_fun('map', kl_map)

@tail_recursion
def shen_mapx45h(KL_ARG_V1964_411, KL_ARG_V1965_412, KL_ARG_V1966_413):
    global symdic
    return (tail_call(kl_reverse, [KL_ARG_V1966_413]) if shen_eq([], KL_ARG_V1965_412) else (tail_call(shen_mapx45h, [KL_ARG_V1964_411, KL_ARG_V1965_412[1], [shen_apply(KL_ARG_V1964_411, [KL_ARG_V1965_412[0]]), KL_ARG_V1966_413]]) if shen_consp(KL_ARG_V1965_412) else (tail_call(shen_sysx45error, [symdic.symdic_shen_mapx45h]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.map-h', shen_mapx45h)

@tail_recursion
def kl_length(KL_ARG_V1967_414):
    global symdic
    return tail_call(shen_lengthx45h, [KL_ARG_V1967_414, 0])
shen_add_fun('length', kl_length)

@tail_recursion
def shen_lengthx45h(KL_ARG_V1968_415, KL_ARG_V1969_416):
    global symdic
    return (KL_ARG_V1969_416 if shen_eq([], KL_ARG_V1968_415) else (tail_call(shen_lengthx45h, [KL_ARG_V1968_415[1], (KL_ARG_V1969_416 + 1)]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.length-h', shen_lengthx45h)

@tail_recursion
def kl_occurrences(KL_ARG_V1978_417, KL_ARG_V1979_418):
    global symdic
    return (1 if shen_eq(KL_ARG_V1979_418, KL_ARG_V1978_417) else ((tco_apply(kl_occurrences, [KL_ARG_V1978_417, KL_ARG_V1979_418[0]]) + tco_apply(kl_occurrences, [KL_ARG_V1978_417, KL_ARG_V1979_418[1]])) if shen_consp(KL_ARG_V1979_418) else (0 if True else shen_simple_error('condition failure'))))
shen_add_fun('occurrences', kl_occurrences)

@tail_recursion
def kl_nth(KL_ARG_V1987_419, KL_ARG_V1988_420):
    global symdic
    return (KL_ARG_V1988_420[0] if (shen_eq(1, KL_ARG_V1987_419) and shen_consp(KL_ARG_V1988_420)) else (tail_call(kl_nth, [(KL_ARG_V1987_419 - 1), KL_ARG_V1988_420[1]]) if shen_consp(KL_ARG_V1988_420) else (tail_call(shen_sysx45error, [symdic.symdic_kl_nth]) if True else shen_simple_error('condition failure'))))
shen_add_fun('nth', kl_nth)

@tail_recursion
def kl_integerx63(KL_ARG_V1989_421):

    class KL_Context:
        KL_LOC_Abs_422 = None
    KL_CTX = KL_Context()
    global symdic
    return (isinstance(KL_ARG_V1989_421, numbers.Number) and [setattr(KL_CTX, 'KL_LOC_Abs_422', tco_apply(shen_abs, [KL_ARG_V1989_421])), tco_apply(shen_integerx45testx63, [KL_CTX.KL_LOC_Abs_422, tco_apply(shen_magless, [KL_CTX.KL_LOC_Abs_422, 1])])][(-1)])
shen_add_fun('integer?', kl_integerx63)

@tail_recursion
def shen_abs(KL_ARG_V1990_423):
    global symdic
    return (KL_ARG_V1990_423 if (KL_ARG_V1990_423 > 0) else (0 - KL_ARG_V1990_423))
shen_add_fun('shen.abs', shen_abs)

@tail_recursion
def shen_magless(KL_ARG_V1991_424, KL_ARG_V1992_425):

    class KL_Context:
        KL_LOC_Nx2_426 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Nx2_426', (KL_ARG_V1992_425 * 2)), (KL_ARG_V1992_425 if (KL_CTX.KL_LOC_Nx2_426 > KL_ARG_V1991_424) else tail_call(shen_magless, [KL_ARG_V1991_424, KL_CTX.KL_LOC_Nx2_426]))][(-1)]
shen_add_fun('shen.magless', shen_magless)

@tail_recursion
def shen_integerx45testx63(KL_ARG_V1996_427, KL_ARG_V1997_428):

    class KL_Context:
        KL_LOC_Absx45N_429 = None
    KL_CTX = KL_Context()
    global symdic
    return (True if shen_eq(0, KL_ARG_V1996_427) else (False if (1 > KL_ARG_V1996_427) else ([setattr(KL_CTX, 'KL_LOC_Absx45N_429', (KL_ARG_V1996_427 - KL_ARG_V1997_428)), (tail_call(kl_integerx63, [KL_ARG_V1996_427]) if (0 > KL_CTX.KL_LOC_Absx45N_429) else tail_call(shen_integerx45testx63, [KL_CTX.KL_LOC_Absx45N_429, KL_ARG_V1997_428]))][(-1)] if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.integer-test?', shen_integerx45testx63)

@tail_recursion
def kl_mapcan(KL_ARG_V2000_430, KL_ARG_V2001_431):
    global symdic
    return ([] if shen_eq([], KL_ARG_V2001_431) else (tail_call(kl_append, [shen_apply(KL_ARG_V2000_430, [KL_ARG_V2001_431[0]]), tco_apply(kl_mapcan, [KL_ARG_V2000_430, KL_ARG_V2001_431[1]])]) if shen_consp(KL_ARG_V2001_431) else (tail_call(shen_sysx45error, [symdic.symdic_kl_mapcan]) if True else shen_simple_error('condition failure'))))
shen_add_fun('mapcan', kl_mapcan)

@tail_recursion
def kl_readx45filex45asx45bytelist(KL_ARG_V2002_432):

    class KL_Context:
        KL_LOC_Stream_433 = None
        KL_LOC_Byte_434 = None
        KL_LOC_Bytes_435 = None
        KL_LOC_Close_436 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Stream_433', shen_open(symdic.symdic_kl_file, KL_ARG_V2002_432, symdic.symdic_kl_in)), [setattr(KL_CTX, 'KL_LOC_Byte_434', shen_read_byte(KL_CTX.KL_LOC_Stream_433)), [setattr(KL_CTX, 'KL_LOC_Bytes_435', tco_apply(shen_readx45filex45asx45bytelistx45help, [KL_CTX.KL_LOC_Stream_433, KL_CTX.KL_LOC_Byte_434, []])), [setattr(KL_CTX, 'KL_LOC_Close_436', shen_close(KL_CTX.KL_LOC_Stream_433)), tail_call(kl_reverse, [KL_CTX.KL_LOC_Bytes_435])][(-1)]][(-1)]][(-1)]][(-1)]
shen_add_fun('read-file-as-bytelist', kl_readx45filex45asx45bytelist)

@tail_recursion
def shen_readx45filex45asx45bytelistx45help(KL_ARG_V2003_437, KL_ARG_V2004_438, KL_ARG_V2005_439):
    global symdic
    return (KL_ARG_V2005_439 if shen_eq((-1), KL_ARG_V2004_438) else (tail_call(shen_readx45filex45asx45bytelistx45help, [KL_ARG_V2003_437, shen_read_byte(KL_ARG_V2003_437), [KL_ARG_V2004_438, KL_ARG_V2005_439]]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.read-file-as-bytelist-help', shen_readx45filex45asx45bytelistx45help)

@tail_recursion
def kl_readx45filex45asx45string(KL_ARG_V2006_440):

    class KL_Context:
        KL_LOC_Stream_441 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Stream_441', shen_open(symdic.symdic_kl_file, KL_ARG_V2006_440, symdic.symdic_kl_in)), tail_call(shen_rfasx45h, [KL_CTX.KL_LOC_Stream_441, shen_read_byte(KL_CTX.KL_LOC_Stream_441), ''])][(-1)]
shen_add_fun('read-file-as-string', kl_readx45filex45asx45string)

@tail_recursion
def shen_rfasx45h(KL_ARG_V2007_442, KL_ARG_V2008_443, KL_ARG_V2009_444):
    global symdic
    return ([shen_close(KL_ARG_V2007_442), KL_ARG_V2009_444][(-1)] if shen_eq((-1), KL_ARG_V2008_443) else (tail_call(shen_rfasx45h, [KL_ARG_V2007_442, shen_read_byte(KL_ARG_V2007_442), (KL_ARG_V2009_444 + chr(KL_ARG_V2008_443))]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.rfas-h', shen_rfasx45h)

@tail_recursion
def kl_x61x61(KL_ARG_V2018_445, KL_ARG_V2019_446):
    global symdic
    return (True if shen_eq(KL_ARG_V2019_446, KL_ARG_V2018_445) else (False if True else shen_simple_error('condition failure')))
shen_add_fun('==', kl_x61x61)

@tail_recursion
def kl_abort():
    global symdic
    return shen_simple_error('')
shen_add_fun('abort', kl_abort)

@tail_recursion
def kl_read():
    global symdic
    return tco_apply(kl_lineread, [])[0]
shen_add_fun('read', kl_read)

@tail_recursion
def kl_input():
    global symdic
    return tail_call(kl_eval, [tco_apply(kl_read, [])])
shen_add_fun('input', kl_input)

@tail_recursion
def kl_inputx43(KL_ARG_V2025_447, KL_ARG_V2026_448):

    class KL_Context:
        KL_LOC_Input_449 = None
        KL_LOC_Check_450 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Input_449', tco_apply(kl_read, [])), [setattr(KL_CTX, 'KL_LOC_Check_450', tco_apply(shen_typecheck, [KL_CTX.KL_LOC_Input_449, KL_ARG_V2026_448])), ([shen_pr(('input is not of type ' + tco_apply(shen_app, [KL_ARG_V2026_448, ': please re-enter ', symdic.symdic_shen_r])), tco_apply(kl_stoutput, [])), tail_call(kl_inputx43, [symdic.symdic_kl_x58, KL_ARG_V2026_448])][(-1)] if shen_eq(False, KL_CTX.KL_LOC_Check_450) else tail_call(kl_eval, [KL_CTX.KL_LOC_Input_449]))][(-1)]][(-1)]
shen_add_fun('input+', kl_inputx43)

@tail_recursion
def kl_boundx63(KL_ARG_V2027_451):

    class KL_Context:
        KL_LOC_Val_452 = None
    KL_CTX = KL_Context()
    global symdic
    return (tco_apply(kl_symbolx63, [KL_ARG_V2027_451]) and [setattr(KL_CTX, 'KL_LOC_Val_452', shen_try_except((lambda : shen_get(KL_ARG_V2027_451)), (lambda KL_ARG_E_453: symdic.symdic_shen_thisx45symbolx45isx45unbound))), (False if shen_eq(KL_CTX.KL_LOC_Val_452, symdic.symdic_shen_thisx45symbolx45isx45unbound) else True)][(-1)])
shen_add_fun('bound?', kl_boundx63)

@tail_recursion
def shen_stringx45x62bytes(KL_ARG_V2028_454):
    global symdic
    return ([] if shen_eq('', KL_ARG_V2028_454) else ([ord(KL_ARG_V2028_454[0]), tco_apply(shen_stringx45x62bytes, [KL_ARG_V2028_454[1:]])] if True else shen_simple_error('condition failure')))
shen_add_fun('shen.string->bytes', shen_stringx45x62bytes)

@tail_recursion
def kl_maxinferences(KL_ARG_V2029_455):
    global symdic
    return shen_set(symdic.symdic_shen_x42maxinferencesx42, KL_ARG_V2029_455)
shen_add_fun('maxinferences', kl_maxinferences)

@tail_recursion
def kl_inferences():
    global symdic
    return shen_get(symdic.symdic_shen_x42infsx42)
shen_add_fun('inferences', kl_inferences)

@tail_recursion
def kl_protect(KL_ARG_V2030_456):
    global symdic
    return KL_ARG_V2030_456
shen_add_fun('protect', kl_protect)

@tail_recursion
def kl_stoutput():
    global symdic
    return shen_get(symdic.symdic_x42stoutputx42)
shen_add_fun('stoutput', kl_stoutput)

@tail_recursion
def kl_stringx45x62symbol(KL_ARG_V2031_457):

    class KL_Context:
        KL_LOC_Symbol_458 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Symbol_458', shen_intern(KL_ARG_V2031_457)), (KL_CTX.KL_LOC_Symbol_458 if tco_apply(kl_symbolx63, [KL_CTX.KL_LOC_Symbol_458]) else shen_simple_error(('cannot intern ' + tco_apply(shen_app, [KL_ARG_V2031_457, ' to a symbol', symdic.symdic_shen_s]))))][(-1)]
shen_add_fun('string->symbol', kl_stringx45x62symbol)


#============================== sequent.kl==============================



@tail_recursion
def shen_datatypex45error(KL_ARG_V1591_459):
    global symdic
    return (shen_simple_error(('datatype syntax error here:\r\n\r\n ' + tco_apply(shen_app, [tco_apply(shen_nextx4550, [50, KL_ARG_V1591_459[0]]), '\r\n', symdic.symdic_shen_a]))) if (shen_consp(KL_ARG_V1591_459) and (shen_consp(KL_ARG_V1591_459[1]) and shen_eq([], KL_ARG_V1591_459[1][1]))) else (tail_call(shen_sysx45error, [symdic.symdic_shen_datatypex45error]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.datatype-error', shen_datatypex45error)

@tail_recursion
def shen_x60datatypex45rulesx62(KL_ARG_V1596_460):

    class KL_Context:
        KL_LOC_Result_461 = None
        KL_LOC_Parse_shen_x60datatypex45rulex62_462 = None
        KL_LOC_Parse_shen_x60datatypex45rulesx62_463 = None
        KL_LOC_Result_464 = None
        KL_LOC_Parse_x60ex62_465 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_461', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60datatypex45rulex62_462', tco_apply(shen_x60datatypex45rulex62, [KL_ARG_V1596_460])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60datatypex45rulesx62_463', tco_apply(shen_x60datatypex45rulesx62, [KL_CTX.KL_LOC_Parse_shen_x60datatypex45rulex62_462])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60datatypex45rulesx62_463[0], [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60datatypex45rulex62_462]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60datatypex45rulesx62_463])]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60datatypex45rulesx62_463)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60datatypex45rulex62_462)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_464', [setattr(KL_CTX, 'KL_LOC_Parse_x60ex62_465', tco_apply(kl_x60ex62, [KL_ARG_V1596_460])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_x60ex62_465[0], []]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_x60ex62_465)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_464, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_464)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_461, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_461)][(-1)]
shen_add_fun('shen.<datatype-rules>', shen_x60datatypex45rulesx62)

@tail_recursion
def shen_x60datatypex45rulex62(KL_ARG_V1601_466):

    class KL_Context:
        KL_LOC_Result_467 = None
        KL_LOC_Parse_shen_x60sidex45conditionsx62_468 = None
        KL_LOC_Parse_shen_x60premisesx62_469 = None
        KL_LOC_Parse_shen_x60singleunderlinex62_470 = None
        KL_LOC_Parse_shen_x60conclusionx62_471 = None
        KL_LOC_Result_472 = None
        KL_LOC_Parse_shen_x60sidex45conditionsx62_473 = None
        KL_LOC_Parse_shen_x60premisesx62_474 = None
        KL_LOC_Parse_shen_x60doubleunderlinex62_475 = None
        KL_LOC_Parse_shen_x60conclusionx62_476 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_467', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60sidex45conditionsx62_468', tco_apply(shen_x60sidex45conditionsx62, [KL_ARG_V1601_466])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60premisesx62_469', tco_apply(shen_x60premisesx62, [KL_CTX.KL_LOC_Parse_shen_x60sidex45conditionsx62_468])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60singleunderlinex62_470', tco_apply(shen_x60singleunderlinex62, [KL_CTX.KL_LOC_Parse_shen_x60premisesx62_469])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60conclusionx62_471', tco_apply(shen_x60conclusionx62, [KL_CTX.KL_LOC_Parse_shen_x60singleunderlinex62_470])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60conclusionx62_471[0], tco_apply(shen_sequent, [symdic.symdic_shen_single, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60sidex45conditionsx62_468]), [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60premisesx62_469]), [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60conclusionx62_471]), []]]]])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60conclusionx62_471)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60singleunderlinex62_470)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60premisesx62_469)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60sidex45conditionsx62_468)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_472', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60sidex45conditionsx62_473', tco_apply(shen_x60sidex45conditionsx62, [KL_ARG_V1601_466])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60premisesx62_474', tco_apply(shen_x60premisesx62, [KL_CTX.KL_LOC_Parse_shen_x60sidex45conditionsx62_473])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60doubleunderlinex62_475', tco_apply(shen_x60doubleunderlinex62, [KL_CTX.KL_LOC_Parse_shen_x60premisesx62_474])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60conclusionx62_476', tco_apply(shen_x60conclusionx62, [KL_CTX.KL_LOC_Parse_shen_x60doubleunderlinex62_475])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60conclusionx62_476[0], tco_apply(shen_sequent, [symdic.symdic_shen_double, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60sidex45conditionsx62_473]), [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60premisesx62_474]), [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60conclusionx62_476]), []]]]])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60conclusionx62_476)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60doubleunderlinex62_475)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60premisesx62_474)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60sidex45conditionsx62_473)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_472, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_472)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_467, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_467)][(-1)]
shen_add_fun('shen.<datatype-rule>', shen_x60datatypex45rulex62)

@tail_recursion
def shen_x60sidex45conditionsx62(KL_ARG_V1606_477):

    class KL_Context:
        KL_LOC_Result_478 = None
        KL_LOC_Parse_shen_x60sidex45conditionx62_479 = None
        KL_LOC_Parse_shen_x60sidex45conditionsx62_480 = None
        KL_LOC_Result_481 = None
        KL_LOC_Parse_x60ex62_482 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_478', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60sidex45conditionx62_479', tco_apply(shen_x60sidex45conditionx62, [KL_ARG_V1606_477])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60sidex45conditionsx62_480', tco_apply(shen_x60sidex45conditionsx62, [KL_CTX.KL_LOC_Parse_shen_x60sidex45conditionx62_479])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60sidex45conditionsx62_480[0], [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60sidex45conditionx62_479]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60sidex45conditionsx62_480])]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60sidex45conditionsx62_480)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60sidex45conditionx62_479)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_481', [setattr(KL_CTX, 'KL_LOC_Parse_x60ex62_482', tco_apply(kl_x60ex62, [KL_ARG_V1606_477])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_x60ex62_482[0], []]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_x60ex62_482)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_481, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_481)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_478, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_478)][(-1)]
shen_add_fun('shen.<side-conditions>', shen_x60sidex45conditionsx62)

@tail_recursion
def shen_x60sidex45conditionx62(KL_ARG_V1611_483):

    class KL_Context:
        KL_LOC_Result_484 = None
        KL_LOC_Parse_shen_x60exprx62_485 = None
        KL_LOC_Result_486 = None
        KL_LOC_Parse_shen_x60variablex63x62_487 = None
        KL_LOC_Parse_shen_x60exprx62_488 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_484', ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60exprx62_485', tco_apply(shen_x60exprx62, [tco_apply(shen_pair, [KL_ARG_V1611_483[0][1], tco_apply(shen_hdtl, [KL_ARG_V1611_483])])])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60exprx62_485[0], [symdic.symdic_kl_if, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60exprx62_485]), []]]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60exprx62_485)) else tco_apply(kl_fail, []))][(-1)] if (shen_consp(KL_ARG_V1611_483[0]) and shen_eq(symdic.symdic_kl_if, KL_ARG_V1611_483[0][0])) else tco_apply(kl_fail, []))), ([setattr(KL_CTX, 'KL_LOC_Result_486', ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60variablex63x62_487', tco_apply(shen_x60variablex63x62, [tco_apply(shen_pair, [KL_ARG_V1611_483[0][1], tco_apply(shen_hdtl, [KL_ARG_V1611_483])])])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60exprx62_488', tco_apply(shen_x60exprx62, [KL_CTX.KL_LOC_Parse_shen_x60variablex63x62_487])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60exprx62_488[0], [symdic.symdic_kl_let, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60variablex63x62_487]), [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60exprx62_488]), []]]]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60exprx62_488)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60variablex63x62_487)) else tco_apply(kl_fail, []))][(-1)] if (shen_consp(KL_ARG_V1611_483[0]) and shen_eq(symdic.symdic_kl_let, KL_ARG_V1611_483[0][0])) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_486, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_486)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_484, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_484)][(-1)]
shen_add_fun('shen.<side-condition>', shen_x60sidex45conditionx62)

@tail_recursion
def shen_x60variablex63x62(KL_ARG_V1616_489):

    class KL_Context:
        KL_LOC_Result_490 = None
        KL_LOC_Parse_X_491 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_490', ([setattr(KL_CTX, 'KL_LOC_Parse_X_491', KL_ARG_V1616_489[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1616_489[0][1], tco_apply(shen_hdtl, [KL_ARG_V1616_489])])[0], KL_CTX.KL_LOC_Parse_X_491]) if tco_apply(kl_variablex63, [KL_CTX.KL_LOC_Parse_X_491]) else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V1616_489[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_490, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_490)][(-1)]
shen_add_fun('shen.<variable?>', shen_x60variablex63x62)

@tail_recursion
def shen_x60exprx62(KL_ARG_V1621_492):

    class KL_Context:
        KL_LOC_Result_493 = None
        KL_LOC_Parse_X_494 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_493', ([setattr(KL_CTX, 'KL_LOC_Parse_X_494', KL_ARG_V1621_492[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1621_492[0][1], tco_apply(shen_hdtl, [KL_ARG_V1621_492])])[0], tco_apply(shen_removex45bar, [KL_CTX.KL_LOC_Parse_X_494])]) if (not (tco_apply(kl_elementx63, [KL_CTX.KL_LOC_Parse_X_494, [symdic.symdic_kl_x62x62, [symdic.symdic_kl_x59, []]]]) or (tco_apply(shen_singleunderlinex63, [KL_CTX.KL_LOC_Parse_X_494]) or tco_apply(shen_doubleunderlinex63, [KL_CTX.KL_LOC_Parse_X_494])))) else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V1621_492[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_493, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_493)][(-1)]
shen_add_fun('shen.<expr>', shen_x60exprx62)

@tail_recursion
def shen_removex45bar(KL_ARG_V1622_495):
    global symdic
    return ([KL_ARG_V1622_495[0], KL_ARG_V1622_495[1][1][0]] if (shen_consp(KL_ARG_V1622_495) and (shen_consp(KL_ARG_V1622_495[1]) and (shen_consp(KL_ARG_V1622_495[1][1]) and (shen_eq([], KL_ARG_V1622_495[1][1][1]) and shen_eq(KL_ARG_V1622_495[1][0], symdic.symdic_kl_barx33))))) else ([tco_apply(shen_removex45bar, [KL_ARG_V1622_495[0]]), tco_apply(shen_removex45bar, [KL_ARG_V1622_495[1]])] if shen_consp(KL_ARG_V1622_495) else (KL_ARG_V1622_495 if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.remove-bar', shen_removex45bar)

@tail_recursion
def shen_x60premisesx62(KL_ARG_V1627_496):

    class KL_Context:
        KL_LOC_Result_497 = None
        KL_LOC_Parse_shen_x60premisex62_498 = None
        KL_LOC_Parse_shen_x60semicolonx45symbolx62_499 = None
        KL_LOC_Parse_shen_x60premisesx62_500 = None
        KL_LOC_Result_501 = None
        KL_LOC_Parse_x60ex62_502 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_497', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60premisex62_498', tco_apply(shen_x60premisex62, [KL_ARG_V1627_496])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60semicolonx45symbolx62_499', tco_apply(shen_x60semicolonx45symbolx62, [KL_CTX.KL_LOC_Parse_shen_x60premisex62_498])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60premisesx62_500', tco_apply(shen_x60premisesx62, [KL_CTX.KL_LOC_Parse_shen_x60semicolonx45symbolx62_499])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60premisesx62_500[0], [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60premisex62_498]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60premisesx62_500])]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60premisesx62_500)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60semicolonx45symbolx62_499)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60premisex62_498)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_501', [setattr(KL_CTX, 'KL_LOC_Parse_x60ex62_502', tco_apply(kl_x60ex62, [KL_ARG_V1627_496])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_x60ex62_502[0], []]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_x60ex62_502)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_501, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_501)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_497, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_497)][(-1)]
shen_add_fun('shen.<premises>', shen_x60premisesx62)

@tail_recursion
def shen_x60semicolonx45symbolx62(KL_ARG_V1632_503):

    class KL_Context:
        KL_LOC_Result_504 = None
        KL_LOC_Parse_X_505 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_504', ([setattr(KL_CTX, 'KL_LOC_Parse_X_505', KL_ARG_V1632_503[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1632_503[0][1], tco_apply(shen_hdtl, [KL_ARG_V1632_503])])[0], symdic.symdic_shen_skip]) if shen_eq(KL_CTX.KL_LOC_Parse_X_505, symdic.symdic_kl_x59) else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V1632_503[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_504, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_504)][(-1)]
shen_add_fun('shen.<semicolon-symbol>', shen_x60semicolonx45symbolx62)

@tail_recursion
def shen_x60premisex62(KL_ARG_V1637_506):

    class KL_Context:
        KL_LOC_Result_507 = None
        KL_LOC_Result_508 = None
        KL_LOC_Parse_shen_x60formulaex62_509 = None
        KL_LOC_Parse_shen_x60formulax62_510 = None
        KL_LOC_Result_511 = None
        KL_LOC_Parse_shen_x60formulax62_512 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_507', (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1637_506[0][1], tco_apply(shen_hdtl, [KL_ARG_V1637_506])])[0], symdic.symdic_kl_x33]) if (shen_consp(KL_ARG_V1637_506[0]) and shen_eq(symdic.symdic_kl_x33, KL_ARG_V1637_506[0][0])) else tco_apply(kl_fail, []))), ([setattr(KL_CTX, 'KL_LOC_Result_508', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60formulaex62_509', tco_apply(shen_x60formulaex62, [KL_ARG_V1637_506])), (([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60formulax62_510', tco_apply(shen_x60formulax62, [tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60formulaex62_509[0][1], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60formulaex62_509])])])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60formulax62_510[0], tco_apply(shen_sequent, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60formulaex62_509]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60formulax62_510])])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60formulax62_510)) else tco_apply(kl_fail, []))][(-1)] if (shen_consp(KL_CTX.KL_LOC_Parse_shen_x60formulaex62_509[0]) and shen_eq(symdic.symdic_kl_x62x62, KL_CTX.KL_LOC_Parse_shen_x60formulaex62_509[0][0])) else tco_apply(kl_fail, [])) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60formulaex62_509)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_511', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60formulax62_512', tco_apply(shen_x60formulax62, [KL_ARG_V1637_506])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60formulax62_512[0], tco_apply(shen_sequent, [[], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60formulax62_512])])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60formulax62_512)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_511, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_511)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_508, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_508)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_507, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_507)][(-1)]
shen_add_fun('shen.<premise>', shen_x60premisex62)

@tail_recursion
def shen_x60conclusionx62(KL_ARG_V1642_513):

    class KL_Context:
        KL_LOC_Result_514 = None
        KL_LOC_Parse_shen_x60formulaex62_515 = None
        KL_LOC_Parse_shen_x60formulax62_516 = None
        KL_LOC_Parse_shen_x60semicolonx45symbolx62_517 = None
        KL_LOC_Result_518 = None
        KL_LOC_Parse_shen_x60formulax62_519 = None
        KL_LOC_Parse_shen_x60semicolonx45symbolx62_520 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_514', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60formulaex62_515', tco_apply(shen_x60formulaex62, [KL_ARG_V1642_513])), (([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60formulax62_516', tco_apply(shen_x60formulax62, [tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60formulaex62_515[0][1], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60formulaex62_515])])])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60semicolonx45symbolx62_517', tco_apply(shen_x60semicolonx45symbolx62, [KL_CTX.KL_LOC_Parse_shen_x60formulax62_516])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60semicolonx45symbolx62_517[0], tco_apply(shen_sequent, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60formulaex62_515]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60formulax62_516])])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60semicolonx45symbolx62_517)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60formulax62_516)) else tco_apply(kl_fail, []))][(-1)] if (shen_consp(KL_CTX.KL_LOC_Parse_shen_x60formulaex62_515[0]) and shen_eq(symdic.symdic_kl_x62x62, KL_CTX.KL_LOC_Parse_shen_x60formulaex62_515[0][0])) else tco_apply(kl_fail, [])) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60formulaex62_515)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_518', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60formulax62_519', tco_apply(shen_x60formulax62, [KL_ARG_V1642_513])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60semicolonx45symbolx62_520', tco_apply(shen_x60semicolonx45symbolx62, [KL_CTX.KL_LOC_Parse_shen_x60formulax62_519])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60semicolonx45symbolx62_520[0], tco_apply(shen_sequent, [[], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60formulax62_519])])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60semicolonx45symbolx62_520)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60formulax62_519)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_518, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_518)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_514, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_514)][(-1)]
shen_add_fun('shen.<conclusion>', shen_x60conclusionx62)

@tail_recursion
def shen_sequent(KL_ARG_V1643_521, KL_ARG_V1644_522):
    global symdic
    return tail_call(kl_x64p, [KL_ARG_V1643_521, KL_ARG_V1644_522])
shen_add_fun('shen.sequent', shen_sequent)

@tail_recursion
def shen_x60formulaex62(KL_ARG_V1649_523):

    class KL_Context:
        KL_LOC_Result_524 = None
        KL_LOC_Parse_shen_x60formulax62_525 = None
        KL_LOC_Parse_shen_x60commax45symbolx62_526 = None
        KL_LOC_Parse_shen_x60formulaex62_527 = None
        KL_LOC_Result_528 = None
        KL_LOC_Parse_shen_x60formulax62_529 = None
        KL_LOC_Result_530 = None
        KL_LOC_Parse_x60ex62_531 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_524', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60formulax62_525', tco_apply(shen_x60formulax62, [KL_ARG_V1649_523])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60commax45symbolx62_526', tco_apply(shen_x60commax45symbolx62, [KL_CTX.KL_LOC_Parse_shen_x60formulax62_525])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60formulaex62_527', tco_apply(shen_x60formulaex62, [KL_CTX.KL_LOC_Parse_shen_x60commax45symbolx62_526])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60formulaex62_527[0], [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60formulax62_525]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60formulaex62_527])]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60formulaex62_527)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60commax45symbolx62_526)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60formulax62_525)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_528', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60formulax62_529', tco_apply(shen_x60formulax62, [KL_ARG_V1649_523])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60formulax62_529[0], [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60formulax62_529]), []]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60formulax62_529)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_530', [setattr(KL_CTX, 'KL_LOC_Parse_x60ex62_531', tco_apply(kl_x60ex62, [KL_ARG_V1649_523])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_x60ex62_531[0], []]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_x60ex62_531)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_530, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_530)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_528, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_528)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_524, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_524)][(-1)]
shen_add_fun('shen.<formulae>', shen_x60formulaex62)

@tail_recursion
def shen_x60commax45symbolx62(KL_ARG_V1654_532):

    class KL_Context:
        KL_LOC_Result_533 = None
        KL_LOC_Parse_X_534 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_533', ([setattr(KL_CTX, 'KL_LOC_Parse_X_534', KL_ARG_V1654_532[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1654_532[0][1], tco_apply(shen_hdtl, [KL_ARG_V1654_532])])[0], symdic.symdic_shen_skip]) if shen_eq(KL_CTX.KL_LOC_Parse_X_534, shen_intern(',')) else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V1654_532[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_533, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_533)][(-1)]
shen_add_fun('shen.<comma-symbol>', shen_x60commax45symbolx62)

@tail_recursion
def shen_x60formulax62(KL_ARG_V1659_535):

    class KL_Context:
        KL_LOC_Result_536 = None
        KL_LOC_Parse_shen_x60exprx62_537 = None
        KL_LOC_Parse_shen_x60typex62_538 = None
        KL_LOC_Result_539 = None
        KL_LOC_Parse_shen_x60exprx62_540 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_536', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60exprx62_537', tco_apply(shen_x60exprx62, [KL_ARG_V1659_535])), (([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60typex62_538', tco_apply(shen_x60typex62, [tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60exprx62_537[0][1], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60exprx62_537])])])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60typex62_538[0], [tco_apply(shen_curry, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60exprx62_537])]), [symdic.symdic_kl_x58, [tco_apply(shen_demodulate, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60typex62_538])]), []]]]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60typex62_538)) else tco_apply(kl_fail, []))][(-1)] if (shen_consp(KL_CTX.KL_LOC_Parse_shen_x60exprx62_537[0]) and shen_eq(symdic.symdic_kl_x58, KL_CTX.KL_LOC_Parse_shen_x60exprx62_537[0][0])) else tco_apply(kl_fail, [])) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60exprx62_537)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_539', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60exprx62_540', tco_apply(shen_x60exprx62, [KL_ARG_V1659_535])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60exprx62_540[0], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60exprx62_540])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60exprx62_540)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_539, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_539)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_536, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_536)][(-1)]
shen_add_fun('shen.<formula>', shen_x60formulax62)

@tail_recursion
def shen_x60typex62(KL_ARG_V1664_541):

    class KL_Context:
        KL_LOC_Result_542 = None
        KL_LOC_Parse_shen_x60exprx62_543 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_542', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60exprx62_543', tco_apply(shen_x60exprx62, [KL_ARG_V1664_541])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60exprx62_543[0], tco_apply(shen_curryx45type, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60exprx62_543])])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60exprx62_543)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_542, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_542)][(-1)]
shen_add_fun('shen.<type>', shen_x60typex62)

@tail_recursion
def shen_x60doubleunderlinex62(KL_ARG_V1669_544):

    class KL_Context:
        KL_LOC_Result_545 = None
        KL_LOC_Parse_X_546 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_545', ([setattr(KL_CTX, 'KL_LOC_Parse_X_546', KL_ARG_V1669_544[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1669_544[0][1], tco_apply(shen_hdtl, [KL_ARG_V1669_544])])[0], KL_CTX.KL_LOC_Parse_X_546]) if tco_apply(shen_doubleunderlinex63, [KL_CTX.KL_LOC_Parse_X_546]) else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V1669_544[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_545, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_545)][(-1)]
shen_add_fun('shen.<doubleunderline>', shen_x60doubleunderlinex62)

@tail_recursion
def shen_x60singleunderlinex62(KL_ARG_V1674_547):

    class KL_Context:
        KL_LOC_Result_548 = None
        KL_LOC_Parse_X_549 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_548', ([setattr(KL_CTX, 'KL_LOC_Parse_X_549', KL_ARG_V1674_547[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1674_547[0][1], tco_apply(shen_hdtl, [KL_ARG_V1674_547])])[0], KL_CTX.KL_LOC_Parse_X_549]) if tco_apply(shen_singleunderlinex63, [KL_CTX.KL_LOC_Parse_X_549]) else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V1674_547[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_548, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_548)][(-1)]
shen_add_fun('shen.<singleunderline>', shen_x60singleunderlinex62)

@tail_recursion
def shen_singleunderlinex63(KL_ARG_V1675_550):
    global symdic
    return (tco_apply(kl_symbolx63, [KL_ARG_V1675_550]) and tco_apply(shen_shx63, [str(KL_ARG_V1675_550)]))
shen_add_fun('shen.singleunderline?', shen_singleunderlinex63)

@tail_recursion
def shen_shx63(KL_ARG_V1676_551):
    global symdic
    return (True if shen_eq('_', KL_ARG_V1676_551) else ((shen_eq(KL_ARG_V1676_551[0], '_') and tco_apply(shen_shx63, [KL_ARG_V1676_551[1:]])) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.sh?', shen_shx63)

@tail_recursion
def shen_doubleunderlinex63(KL_ARG_V1677_552):
    global symdic
    return (tco_apply(kl_symbolx63, [KL_ARG_V1677_552]) and tco_apply(shen_dhx63, [str(KL_ARG_V1677_552)]))
shen_add_fun('shen.doubleunderline?', shen_doubleunderlinex63)

@tail_recursion
def shen_dhx63(KL_ARG_V1678_553):
    global symdic
    return (True if shen_eq('=', KL_ARG_V1678_553) else ((shen_eq(KL_ARG_V1678_553[0], '=') and tco_apply(shen_dhx63, [KL_ARG_V1678_553[1:]])) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.dh?', shen_dhx63)

@tail_recursion
def shen_processx45datatype(KL_ARG_V1679_554, KL_ARG_V1680_555):
    global symdic
    return tail_call(shen_rememberx45datatype, [tco_apply(shen_sx45prolog, [tco_apply(shen_rulesx45x62hornx45clauses, [KL_ARG_V1679_554, KL_ARG_V1680_555])])])
shen_add_fun('shen.process-datatype', shen_processx45datatype)

@tail_recursion
def shen_rememberx45datatype(KL_ARG_V1685_556):
    global symdic
    return ([shen_set(symdic.symdic_shen_x42datatypesx42, tco_apply(kl_adjoin, [KL_ARG_V1685_556[0], shen_get(symdic.symdic_shen_x42datatypesx42)])), [shen_set(symdic.symdic_shen_x42alldatatypesx42, tco_apply(kl_adjoin, [KL_ARG_V1685_556[0], shen_get(symdic.symdic_shen_x42alldatatypesx42)])), KL_ARG_V1685_556[0]][(-1)]][(-1)] if shen_consp(KL_ARG_V1685_556) else (tail_call(shen_sysx45error, [symdic.symdic_shen_rememberx45datatype]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.remember-datatype', shen_rememberx45datatype)

@tail_recursion
def shen_rulesx45x62hornx45clauses(KL_ARG_V1688_557, KL_ARG_V1689_558):
    global symdic
    return ([] if shen_eq([], KL_ARG_V1689_558) else ([tco_apply(shen_rulex45x62hornx45clause, [KL_ARG_V1688_557, tco_apply(kl_snd, [KL_ARG_V1689_558[0]])]), tco_apply(shen_rulesx45x62hornx45clauses, [KL_ARG_V1688_557, KL_ARG_V1689_558[1]])] if (shen_consp(KL_ARG_V1689_558) and (tco_apply(kl_tuplex63, [KL_ARG_V1689_558[0]]) and shen_eq(symdic.symdic_shen_single, tco_apply(kl_fst, [KL_ARG_V1689_558[0]])))) else (tail_call(shen_rulesx45x62hornx45clauses, [KL_ARG_V1688_557, tco_apply(kl_append, [tco_apply(shen_doublex45x62singles, [tco_apply(kl_snd, [KL_ARG_V1689_558[0]])]), KL_ARG_V1689_558[1]])]) if (shen_consp(KL_ARG_V1689_558) and (tco_apply(kl_tuplex63, [KL_ARG_V1689_558[0]]) and shen_eq(symdic.symdic_shen_double, tco_apply(kl_fst, [KL_ARG_V1689_558[0]])))) else (tail_call(shen_sysx45error, [symdic.symdic_shen_rulesx45x62hornx45clauses]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.rules->horn-clauses', shen_rulesx45x62hornx45clauses)

@tail_recursion
def shen_doublex45x62singles(KL_ARG_V1690_559):
    global symdic
    return [tco_apply(shen_rightx45rule, [KL_ARG_V1690_559]), [tco_apply(shen_leftx45rule, [KL_ARG_V1690_559]), []]]
shen_add_fun('shen.double->singles', shen_doublex45x62singles)

@tail_recursion
def shen_rightx45rule(KL_ARG_V1691_560):
    global symdic
    return tail_call(kl_x64p, [symdic.symdic_shen_single, KL_ARG_V1691_560])
shen_add_fun('shen.right-rule', shen_rightx45rule)

@tail_recursion
def shen_leftx45rule(KL_ARG_V1692_561):

    class KL_Context:
        KL_LOC_Q_562 = None
        KL_LOC_NewConclusion_563 = None
        KL_LOC_NewPremises_564 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_Q_562', tco_apply(kl_gensym, [symdic.symdic_Qv])), [setattr(KL_CTX, 'KL_LOC_NewConclusion_563', tco_apply(kl_x64p, [[tco_apply(kl_snd, [KL_ARG_V1692_561[1][1][0]]), []], KL_CTX.KL_LOC_Q_562])), [setattr(KL_CTX, 'KL_LOC_NewPremises_564', [tco_apply(kl_x64p, [tco_apply(kl_map, [symdic.symdic_shen_rightx45x62left, KL_ARG_V1692_561[1][0]]), KL_CTX.KL_LOC_Q_562]), []]), tail_call(kl_x64p, [symdic.symdic_shen_single, [KL_ARG_V1692_561[0], [KL_CTX.KL_LOC_NewPremises_564, [KL_CTX.KL_LOC_NewConclusion_563, []]]]])][(-1)]][(-1)]][(-1)] if (shen_consp(KL_ARG_V1692_561) and (shen_consp(KL_ARG_V1692_561[1]) and (shen_consp(KL_ARG_V1692_561[1][1]) and (tco_apply(kl_tuplex63, [KL_ARG_V1692_561[1][1][0]]) and (shen_eq([], tco_apply(kl_fst, [KL_ARG_V1692_561[1][1][0]])) and shen_eq([], KL_ARG_V1692_561[1][1][1])))))) else (tail_call(shen_sysx45error, [symdic.symdic_shen_leftx45rule]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.left-rule', shen_leftx45rule)

@tail_recursion
def shen_rightx45x62left(KL_ARG_V1697_565):
    global symdic
    return (tail_call(kl_snd, [KL_ARG_V1697_565]) if (tco_apply(kl_tuplex63, [KL_ARG_V1697_565]) and shen_eq([], tco_apply(kl_fst, [KL_ARG_V1697_565]))) else (shen_simple_error('syntax error with ==========\r\n') if True else shen_simple_error('condition failure')))
shen_add_fun('shen.right->left', shen_rightx45x62left)

@tail_recursion
def shen_rulex45x62hornx45clause(KL_ARG_V1698_566, KL_ARG_V1699_567):
    global symdic
    return ([tco_apply(shen_rulex45x62hornx45clausex45head, [KL_ARG_V1698_566, tco_apply(kl_snd, [KL_ARG_V1699_567[1][1][0]])]), [symdic.symdic_kl_x58x45, [tco_apply(shen_rulex45x62hornx45clausex45body, [KL_ARG_V1699_567[0], KL_ARG_V1699_567[1][0], tco_apply(kl_fst, [KL_ARG_V1699_567[1][1][0]])]), []]]] if (shen_consp(KL_ARG_V1699_567) and (shen_consp(KL_ARG_V1699_567[1]) and (shen_consp(KL_ARG_V1699_567[1][1]) and (tco_apply(kl_tuplex63, [KL_ARG_V1699_567[1][1][0]]) and shen_eq([], KL_ARG_V1699_567[1][1][1]))))) else (tail_call(shen_sysx45error, [symdic.symdic_shen_rulex45x62hornx45clause]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.rule->horn-clause', shen_rulex45x62hornx45clause)

@tail_recursion
def shen_rulex45x62hornx45clausex45head(KL_ARG_V1700_568, KL_ARG_V1701_569):
    global symdic
    return [KL_ARG_V1700_568, [tco_apply(shen_modex45ify, [KL_ARG_V1701_569]), [symdic.symdic_Context_1957, []]]]
shen_add_fun('shen.rule->horn-clause-head', shen_rulex45x62hornx45clausex45head)

@tail_recursion
def shen_modex45ify(KL_ARG_V1702_570):
    global symdic
    return ([symdic.symdic_kl_mode, [[KL_ARG_V1702_570[0], [symdic.symdic_kl_x58, [[symdic.symdic_kl_mode, [KL_ARG_V1702_570[1][1][0], [symdic.symdic_kl_x43, []]]], []]]], [symdic.symdic_kl_x45, []]]] if (shen_consp(KL_ARG_V1702_570) and (shen_consp(KL_ARG_V1702_570[1]) and (shen_eq(symdic.symdic_kl_x58, KL_ARG_V1702_570[1][0]) and (shen_consp(KL_ARG_V1702_570[1][1]) and shen_eq([], KL_ARG_V1702_570[1][1][1]))))) else (KL_ARG_V1702_570 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.mode-ify', shen_modex45ify)

@tail_recursion
def shen_rulex45x62hornx45clausex45body(KL_ARG_V1703_571, KL_ARG_V1704_572, KL_ARG_V1705_573):

    class KL_Context:
        KL_LOC_Variables_574 = None
        KL_LOC_Predicates_575 = None
        KL_LOC_SearchLiterals_577 = None
        KL_LOC_SearchClauses_578 = None
        KL_LOC_SideLiterals_579 = None
        KL_LOC_PremissLiterals_580 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Variables_574', tco_apply(kl_map, [symdic.symdic_shen_extract_vars, KL_ARG_V1705_573])), [setattr(KL_CTX, 'KL_LOC_Predicates_575', tco_apply(kl_map, [(lambda KL_ARG_X_576: tail_call(kl_gensym, [symdic.symdic_shen_cl])), KL_ARG_V1705_573])), [setattr(KL_CTX, 'KL_LOC_SearchLiterals_577', tco_apply(shen_constructx45searchx45literals, [KL_CTX.KL_LOC_Predicates_575, KL_CTX.KL_LOC_Variables_574, symdic.symdic_Context_1957, symdic.symdic_Context1_1957])), [setattr(KL_CTX, 'KL_LOC_SearchClauses_578', tco_apply(shen_constructx45searchx45clauses, [KL_CTX.KL_LOC_Predicates_575, KL_ARG_V1705_573, KL_CTX.KL_LOC_Variables_574])), [setattr(KL_CTX, 'KL_LOC_SideLiterals_579', tco_apply(shen_constructx45sidex45literals, [KL_ARG_V1703_571])), [setattr(KL_CTX, 'KL_LOC_PremissLiterals_580', tco_apply(kl_map, [(lambda KL_ARG_X_581: tail_call(shen_constructx45premissx45literal, [KL_ARG_X_581, tco_apply(kl_emptyx63, [KL_ARG_V1705_573])])), KL_ARG_V1704_572])), tail_call(kl_append, [KL_CTX.KL_LOC_SearchLiterals_577, tco_apply(kl_append, [KL_CTX.KL_LOC_SideLiterals_579, KL_CTX.KL_LOC_PremissLiterals_580])])][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]
shen_add_fun('shen.rule->horn-clause-body', shen_rulex45x62hornx45clausex45body)

@tail_recursion
def shen_constructx45searchx45literals(KL_ARG_V1710_582, KL_ARG_V1711_583, KL_ARG_V1712_584, KL_ARG_V1713_585):
    global symdic
    return ([] if (shen_eq([], KL_ARG_V1710_582) and shen_eq([], KL_ARG_V1711_583)) else (tail_call(shen_cslx45help, [KL_ARG_V1710_582, KL_ARG_V1711_583, KL_ARG_V1712_584, KL_ARG_V1713_585]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.construct-search-literals', shen_constructx45searchx45literals)

@tail_recursion
def shen_cslx45help(KL_ARG_V1716_586, KL_ARG_V1717_587, KL_ARG_V1718_588, KL_ARG_V1719_589):
    global symdic
    return ([[symdic.symdic_kl_bind, [symdic.symdic_ContextOut_1957, [KL_ARG_V1718_588, []]]], []] if (shen_eq([], KL_ARG_V1716_586) and shen_eq([], KL_ARG_V1717_587)) else ([[KL_ARG_V1716_586[0], [KL_ARG_V1718_588, [KL_ARG_V1719_589, KL_ARG_V1717_587[0]]]], tco_apply(shen_cslx45help, [KL_ARG_V1716_586[1], KL_ARG_V1717_587[1], KL_ARG_V1719_589, tco_apply(kl_gensym, [symdic.symdic_Context])])] if (shen_consp(KL_ARG_V1716_586) and shen_consp(KL_ARG_V1717_587)) else (tail_call(shen_sysx45error, [symdic.symdic_shen_cslx45help]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.csl-help', shen_cslx45help)

@tail_recursion
def shen_constructx45searchx45clauses(KL_ARG_V1720_590, KL_ARG_V1721_591, KL_ARG_V1722_592):
    global symdic
    return (symdic.symdic_shen_skip if (shen_eq([], KL_ARG_V1720_590) and (shen_eq([], KL_ARG_V1721_591) and shen_eq([], KL_ARG_V1722_592))) else ([tco_apply(shen_constructx45searchx45clause, [KL_ARG_V1720_590[0], KL_ARG_V1721_591[0], KL_ARG_V1722_592[0]]), tail_call(shen_constructx45searchx45clauses, [KL_ARG_V1720_590[1], KL_ARG_V1721_591[1], KL_ARG_V1722_592[1]])][(-1)] if (shen_consp(KL_ARG_V1720_590) and (shen_consp(KL_ARG_V1721_591) and shen_consp(KL_ARG_V1722_592))) else (tail_call(shen_sysx45error, [symdic.symdic_shen_constructx45searchx45clauses]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.construct-search-clauses', shen_constructx45searchx45clauses)

@tail_recursion
def shen_constructx45searchx45clause(KL_ARG_V1723_593, KL_ARG_V1724_594, KL_ARG_V1725_595):
    global symdic
    return tail_call(shen_sx45prolog, [[tco_apply(shen_constructx45basex45searchx45clause, [KL_ARG_V1723_593, KL_ARG_V1724_594, KL_ARG_V1725_595]), [tco_apply(shen_constructx45recursivex45searchx45clause, [KL_ARG_V1723_593, KL_ARG_V1724_594, KL_ARG_V1725_595]), []]]])
shen_add_fun('shen.construct-search-clause', shen_constructx45searchx45clause)

@tail_recursion
def shen_constructx45basex45searchx45clause(KL_ARG_V1726_596, KL_ARG_V1727_597, KL_ARG_V1728_598):
    global symdic
    return [[KL_ARG_V1726_596, [[tco_apply(shen_modex45ify, [KL_ARG_V1727_597]), symdic.symdic_In_1957], [symdic.symdic_In_1957, KL_ARG_V1728_598]]], [symdic.symdic_kl_x58x45, [[], []]]]
shen_add_fun('shen.construct-base-search-clause', shen_constructx45basex45searchx45clause)

@tail_recursion
def shen_constructx45recursivex45searchx45clause(KL_ARG_V1729_599, KL_ARG_V1730_600, KL_ARG_V1731_601):
    global symdic
    return [[KL_ARG_V1729_599, [[symdic.symdic_Assumption_1957, symdic.symdic_Assumptions_1957], [[symdic.symdic_Assumption_1957, symdic.symdic_Out_1957], KL_ARG_V1731_601]]], [symdic.symdic_kl_x58x45, [[[KL_ARG_V1729_599, [symdic.symdic_Assumptions_1957, [symdic.symdic_Out_1957, KL_ARG_V1731_601]]], []], []]]]
shen_add_fun('shen.construct-recursive-search-clause', shen_constructx45recursivex45searchx45clause)

@tail_recursion
def shen_constructx45sidex45literals(KL_ARG_V1736_602):
    global symdic
    return ([] if shen_eq([], KL_ARG_V1736_602) else ([[symdic.symdic_kl_when, KL_ARG_V1736_602[0][1]], tco_apply(shen_constructx45sidex45literals, [KL_ARG_V1736_602[1]])] if (shen_consp(KL_ARG_V1736_602) and (shen_consp(KL_ARG_V1736_602[0]) and (shen_eq(symdic.symdic_kl_if, KL_ARG_V1736_602[0][0]) and (shen_consp(KL_ARG_V1736_602[0][1]) and shen_eq([], KL_ARG_V1736_602[0][1][1]))))) else ([[symdic.symdic_kl_is, KL_ARG_V1736_602[0][1]], tco_apply(shen_constructx45sidex45literals, [KL_ARG_V1736_602[1]])] if (shen_consp(KL_ARG_V1736_602) and (shen_consp(KL_ARG_V1736_602[0]) and (shen_eq(symdic.symdic_kl_let, KL_ARG_V1736_602[0][0]) and (shen_consp(KL_ARG_V1736_602[0][1]) and (shen_consp(KL_ARG_V1736_602[0][1][1]) and shen_eq([], KL_ARG_V1736_602[0][1][1][1])))))) else (tail_call(shen_constructx45sidex45literals, [KL_ARG_V1736_602[1]]) if shen_consp(KL_ARG_V1736_602) else (tail_call(shen_sysx45error, [symdic.symdic_shen_constructx45sidex45literals]) if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.construct-side-literals', shen_constructx45sidex45literals)

@tail_recursion
def shen_constructx45premissx45literal(KL_ARG_V1741_603, KL_ARG_V1742_604):
    global symdic
    return ([symdic.symdic_shen_tx42, [tco_apply(shen_recursive_cons_form, [tco_apply(kl_snd, [KL_ARG_V1741_603])]), [tco_apply(shen_constructx45context, [KL_ARG_V1742_604, tco_apply(kl_fst, [KL_ARG_V1741_603])]), []]]] if tco_apply(kl_tuplex63, [KL_ARG_V1741_603]) else ([symdic.symdic_kl_cut, [symdic.symdic_Throwcontrol, []]] if shen_eq(symdic.symdic_kl_x33, KL_ARG_V1741_603) else (tail_call(shen_sysx45error, [symdic.symdic_shen_constructx45premissx45literal]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.construct-premiss-literal', shen_constructx45premissx45literal)

@tail_recursion
def shen_constructx45context(KL_ARG_V1743_605, KL_ARG_V1744_606):
    global symdic
    return (symdic.symdic_Context_1957 if (shen_eq(True, KL_ARG_V1743_605) and shen_eq([], KL_ARG_V1744_606)) else (symdic.symdic_ContextOut_1957 if (shen_eq(False, KL_ARG_V1743_605) and shen_eq([], KL_ARG_V1744_606)) else ([symdic.symdic_kl_cons, [tco_apply(shen_recursive_cons_form, [KL_ARG_V1744_606[0]]), [tco_apply(shen_constructx45context, [KL_ARG_V1743_605, KL_ARG_V1744_606[1]]), []]]] if shen_consp(KL_ARG_V1744_606) else (tail_call(shen_sysx45error, [symdic.symdic_shen_constructx45context]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.construct-context', shen_constructx45context)

@tail_recursion
def shen_recursive_cons_form(KL_ARG_V1745_607):
    global symdic
    return ([symdic.symdic_kl_cons, [tco_apply(shen_recursive_cons_form, [KL_ARG_V1745_607[0]]), [tco_apply(shen_recursive_cons_form, [KL_ARG_V1745_607[1]]), []]]] if shen_consp(KL_ARG_V1745_607) else (KL_ARG_V1745_607 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.recursive_cons_form', shen_recursive_cons_form)

@tail_recursion
def kl_preclude(KL_ARG_V1746_608):

    class KL_Context:
        KL_LOC_FilterDatatypes_609 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_FilterDatatypes_609', shen_set(symdic.symdic_shen_x42datatypesx42, tco_apply(kl_difference, [shen_get(symdic.symdic_shen_x42datatypesx42), KL_ARG_V1746_608]))), shen_get(symdic.symdic_shen_x42datatypesx42)][(-1)]
shen_add_fun('preclude', kl_preclude)

@tail_recursion
def kl_include(KL_ARG_V1747_610):

    class KL_Context:
        KL_LOC_ValidTypes_611 = None
        KL_LOC_NewDatatypes_612 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_ValidTypes_611', tco_apply(kl_intersection, [KL_ARG_V1747_610, shen_get(symdic.symdic_shen_x42alldatatypesx42)])), [setattr(KL_CTX, 'KL_LOC_NewDatatypes_612', shen_set(symdic.symdic_shen_x42datatypesx42, tco_apply(kl_union, [KL_CTX.KL_LOC_ValidTypes_611, shen_get(symdic.symdic_shen_x42datatypesx42)]))), shen_get(symdic.symdic_shen_x42datatypesx42)][(-1)]][(-1)]
shen_add_fun('include', kl_include)

@tail_recursion
def kl_precludex45allx45but(KL_ARG_V1748_613):
    global symdic
    return tail_call(kl_preclude, [tco_apply(kl_difference, [shen_get(symdic.symdic_shen_x42alldatatypesx42), KL_ARG_V1748_613])])
shen_add_fun('preclude-all-but', kl_precludex45allx45but)

@tail_recursion
def kl_includex45allx45but(KL_ARG_V1749_614):
    global symdic
    return tail_call(kl_include, [tco_apply(kl_difference, [shen_get(symdic.symdic_shen_x42alldatatypesx42), KL_ARG_V1749_614])])
shen_add_fun('include-all-but', kl_includex45allx45but)

@tail_recursion
def shen_synonymsx45help(KL_ARG_V1754_615):
    global symdic
    return (symdic.symdic_kl_synonyms if shen_eq([], KL_ARG_V1754_615) else ([tco_apply(shen_pushnew, [[KL_ARG_V1754_615[0], tco_apply(shen_curryx45type, [KL_ARG_V1754_615[1][0]])], symdic.symdic_shen_x42synonymsx42]), tail_call(shen_synonymsx45help, [KL_ARG_V1754_615[1][1]])][(-1)] if (shen_consp(KL_ARG_V1754_615) and shen_consp(KL_ARG_V1754_615[1])) else (shen_simple_error(('odd number of synonyms\r\n' + '')) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.synonyms-help', shen_synonymsx45help)

@tail_recursion
def shen_pushnew(KL_ARG_V1755_616, KL_ARG_V1756_617):
    global symdic
    return (shen_get(KL_ARG_V1756_617) if tco_apply(kl_elementx63, [KL_ARG_V1755_616, shen_get(KL_ARG_V1756_617)]) else shen_set(KL_ARG_V1756_617, [KL_ARG_V1755_616, shen_get(KL_ARG_V1756_617)]))
shen_add_fun('shen.pushnew', shen_pushnew)


#============================== yacc.kl==============================



@tail_recursion
def shen_yacc(KL_ARG_V2096_618):
    global symdic
    return (tail_call(shen_yacc, [[symdic.symdic_kl_defcc, [KL_ARG_V2096_618[1][0], KL_ARG_V2096_618[1][1][1][1][1][1][1]]]]) if (shen_consp(KL_ARG_V2096_618) and (shen_eq(symdic.symdic_kl_defcc, KL_ARG_V2096_618[0]) and (shen_consp(KL_ARG_V2096_618[1]) and (shen_consp(KL_ARG_V2096_618[1][1]) and (shen_eq(symdic.symdic_kl_x123, KL_ARG_V2096_618[1][1][0]) and (shen_consp(KL_ARG_V2096_618[1][1][1]) and (shen_consp(KL_ARG_V2096_618[1][1][1][1]) and (shen_eq(symdic.symdic_kl_x61x61x62, KL_ARG_V2096_618[1][1][1][1][0]) and (shen_consp(KL_ARG_V2096_618[1][1][1][1][1]) and (shen_consp(KL_ARG_V2096_618[1][1][1][1][1][1]) and shen_eq(symdic.symdic_kl_x125, KL_ARG_V2096_618[1][1][1][1][1][1][0]))))))))))) else (tail_call(shen_yaccx45x62shen, [KL_ARG_V2096_618[1][0], KL_ARG_V2096_618[1][1]]) if (shen_consp(KL_ARG_V2096_618) and (shen_eq(symdic.symdic_kl_defcc, KL_ARG_V2096_618[0]) and shen_consp(KL_ARG_V2096_618[1]))) else (tail_call(shen_sysx45error, [symdic.symdic_shen_yacc]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.yacc', shen_yacc)

@tail_recursion
def shen_yaccx45x62shen(KL_ARG_V2097_619, KL_ARG_V2098_620):
    global symdic
    return [symdic.symdic_kl_define, [KL_ARG_V2097_619, tco_apply(shen_yacc_cases, [tco_apply(kl_map, [symdic.symdic_shen_cc_body, tco_apply(shen_split_cc_rules, [KL_ARG_V2098_620, []])])])]]
shen_add_fun('shen.yacc->shen', shen_yaccx45x62shen)

@tail_recursion
def shen_yacc_cases(KL_ARG_V2099_621):
    global symdic
    return tail_call(kl_append, [tco_apply(kl_mapcan, [(lambda KL_ARG_Case_622: [symdic.symdic_Stream, [symdic.symdic_kl_x60x45, [KL_ARG_Case_622, []]]]), KL_ARG_V2099_621]), [symdic.symdic_kl__, [symdic.symdic_kl_x45x62, [[symdic.symdic_kl_fail, []], []]]]])
shen_add_fun('shen.yacc_cases', shen_yacc_cases)

@tail_recursion
def shen_first_n(KL_ARG_V2104_623, KL_ARG_V2105_624):
    global symdic
    return ([] if shen_eq(0, KL_ARG_V2104_623) else ([] if shen_eq([], KL_ARG_V2105_624) else ([KL_ARG_V2105_624[0], tco_apply(shen_first_n, [(KL_ARG_V2104_623 - 1), KL_ARG_V2105_624[1]])] if shen_consp(KL_ARG_V2105_624) else (tail_call(shen_sysx45error, [symdic.symdic_shen_first_n]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.first_n', shen_first_n)

@tail_recursion
def shen_split_cc_rules(KL_ARG_V2106_625, KL_ARG_V2107_626):
    global symdic
    return ([] if (shen_eq([], KL_ARG_V2106_625) and shen_eq([], KL_ARG_V2107_626)) else ([tco_apply(shen_split_cc_rule, [tco_apply(kl_reverse, [KL_ARG_V2107_626]), []]), []] if shen_eq([], KL_ARG_V2106_625) else ([tco_apply(shen_split_cc_rule, [tco_apply(kl_reverse, [KL_ARG_V2107_626]), []]), tco_apply(shen_split_cc_rules, [KL_ARG_V2106_625[1], []])] if (shen_consp(KL_ARG_V2106_625) and shen_eq(symdic.symdic_kl_x59, KL_ARG_V2106_625[0])) else (tail_call(shen_split_cc_rules, [KL_ARG_V2106_625[1], [KL_ARG_V2106_625[0], KL_ARG_V2107_626]]) if shen_consp(KL_ARG_V2106_625) else (tail_call(shen_sysx45error, [symdic.symdic_shen_split_cc_rules]) if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.split_cc_rules', shen_split_cc_rules)

@tail_recursion
def shen_split_cc_rule(KL_ARG_V2108_627, KL_ARG_V2109_628):
    global symdic
    return ([tco_apply(kl_reverse, [KL_ARG_V2109_628]), KL_ARG_V2108_627[1]] if (shen_consp(KL_ARG_V2108_627) and (shen_eq(symdic.symdic_kl_x58x61, KL_ARG_V2108_627[0]) and (shen_consp(KL_ARG_V2108_627[1]) and shen_eq([], KL_ARG_V2108_627[1][1])))) else ([tco_apply(kl_reverse, [KL_ARG_V2109_628]), [[symdic.symdic_kl_where, [KL_ARG_V2108_627[1][1][1][0], [KL_ARG_V2108_627[1][0], []]]], []]] if (shen_consp(KL_ARG_V2108_627) and (shen_eq(symdic.symdic_kl_x58x61, KL_ARG_V2108_627[0]) and (shen_consp(KL_ARG_V2108_627[1]) and (shen_consp(KL_ARG_V2108_627[1][1]) and (shen_eq(symdic.symdic_kl_where, KL_ARG_V2108_627[1][1][0]) and (shen_consp(KL_ARG_V2108_627[1][1][1]) and shen_eq([], KL_ARG_V2108_627[1][1][1][1]))))))) else ([shen_pr('warning: ', tco_apply(kl_stoutput, [])), [tco_apply(kl_map, [(lambda KL_ARG_X_629: shen_pr(tco_apply(shen_app, [KL_ARG_X_629, ' ', symdic.symdic_shen_a]), tco_apply(kl_stoutput, []))), tco_apply(kl_reverse, [KL_ARG_V2109_628])]), [shen_pr('has no semantics.\r\n', tco_apply(kl_stoutput, [])), tail_call(shen_split_cc_rule, [[symdic.symdic_kl_x58x61, [tco_apply(shen_default_semantics, [tco_apply(kl_reverse, [KL_ARG_V2109_628])]), []]], KL_ARG_V2109_628])][(-1)]][(-1)]][(-1)] if shen_eq([], KL_ARG_V2108_627) else (tail_call(shen_split_cc_rule, [KL_ARG_V2108_627[1], [KL_ARG_V2108_627[0], KL_ARG_V2109_628]]) if shen_consp(KL_ARG_V2108_627) else (tail_call(shen_sysx45error, [symdic.symdic_shen_split_cc_rule]) if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.split_cc_rule', shen_split_cc_rule)

@tail_recursion
def shen_default_semantics(KL_ARG_V2110_630):
    global symdic
    return ([] if shen_eq([], KL_ARG_V2110_630) else ([symdic.symdic_kl_append, [KL_ARG_V2110_630[0], [tco_apply(shen_default_semantics, [KL_ARG_V2110_630[1]]), []]]] if (shen_consp(KL_ARG_V2110_630) and tco_apply(shen_grammar_symbolx63, [KL_ARG_V2110_630[0]])) else ([symdic.symdic_kl_cons, [KL_ARG_V2110_630[0], [tco_apply(shen_default_semantics, [KL_ARG_V2110_630[1]]), []]]] if shen_consp(KL_ARG_V2110_630) else (tail_call(shen_sysx45error, [symdic.symdic_shen_default_semantics]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.default_semantics', shen_default_semantics)

@tail_recursion
def shen_cc_body(KL_ARG_V2111_631):
    global symdic
    return (tail_call(shen_syntax, [KL_ARG_V2111_631[0], symdic.symdic_Stream, KL_ARG_V2111_631[1][0]]) if (shen_consp(KL_ARG_V2111_631) and (shen_consp(KL_ARG_V2111_631[1]) and shen_eq([], KL_ARG_V2111_631[1][1]))) else (tail_call(shen_sysx45error, [symdic.symdic_shen_cc_body]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.cc_body', shen_cc_body)

@tail_recursion
def shen_syntax(KL_ARG_V2112_632, KL_ARG_V2113_633, KL_ARG_V2114_634):
    global symdic
    return ([symdic.symdic_kl_if, [tco_apply(shen_semantics, [KL_ARG_V2114_634[1][0]]), [[symdic.symdic_shen_pair, [[symdic.symdic_kl_hd, [KL_ARG_V2113_633, []]], [tco_apply(shen_semantics, [KL_ARG_V2114_634[1][1][0]]), []]]], [[symdic.symdic_kl_fail, []], []]]]] if (shen_eq([], KL_ARG_V2112_632) and (shen_consp(KL_ARG_V2114_634) and (shen_eq(symdic.symdic_kl_where, KL_ARG_V2114_634[0]) and (shen_consp(KL_ARG_V2114_634[1]) and (shen_consp(KL_ARG_V2114_634[1][1]) and shen_eq([], KL_ARG_V2114_634[1][1][1])))))) else ([symdic.symdic_shen_pair, [[symdic.symdic_kl_hd, [KL_ARG_V2113_633, []]], [tco_apply(shen_semantics, [KL_ARG_V2114_634]), []]]] if shen_eq([], KL_ARG_V2112_632) else ((tail_call(shen_recursive_descent, [KL_ARG_V2112_632, KL_ARG_V2113_633, KL_ARG_V2114_634]) if tco_apply(shen_grammar_symbolx63, [KL_ARG_V2112_632[0]]) else (tail_call(shen_variablex45match, [KL_ARG_V2112_632, KL_ARG_V2113_633, KL_ARG_V2114_634]) if tco_apply(kl_variablex63, [KL_ARG_V2112_632[0]]) else (tail_call(shen_check_stream, [KL_ARG_V2112_632, KL_ARG_V2113_633, KL_ARG_V2114_634]) if tco_apply(shen_terminalx63, [KL_ARG_V2112_632[0]]) else (tail_call(shen_jump_stream, [KL_ARG_V2112_632, KL_ARG_V2113_633, KL_ARG_V2114_634]) if tco_apply(shen_jump_streamx63, [KL_ARG_V2112_632[0]]) else (tail_call(shen_list_stream, [tco_apply(shen_decons, [KL_ARG_V2112_632[0]]), KL_ARG_V2112_632[1], KL_ARG_V2113_633, KL_ARG_V2114_634]) if tco_apply(shen_list_streamx63, [KL_ARG_V2112_632[0]]) else shen_simple_error(tco_apply(shen_app, [KL_ARG_V2112_632[0], ' is not legal syntax\r\n', symdic.symdic_shen_a]))))))) if shen_consp(KL_ARG_V2112_632) else (tail_call(shen_sysx45error, [symdic.symdic_shen_syntax]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.syntax', shen_syntax)

@tail_recursion
def shen_list_streamx63(KL_ARG_V2123_635):
    global symdic
    return (True if shen_consp(KL_ARG_V2123_635) else (False if True else shen_simple_error('condition failure')))
shen_add_fun('shen.list_stream?', shen_list_streamx63)

@tail_recursion
def shen_decons(KL_ARG_V2124_636):
    global symdic
    return ([KL_ARG_V2124_636[1][0], tco_apply(shen_decons, [KL_ARG_V2124_636[1][1][0]])] if (shen_consp(KL_ARG_V2124_636) and (shen_eq(symdic.symdic_kl_cons, KL_ARG_V2124_636[0]) and (shen_consp(KL_ARG_V2124_636[1]) and (shen_consp(KL_ARG_V2124_636[1][1]) and shen_eq([], KL_ARG_V2124_636[1][1][1]))))) else (KL_ARG_V2124_636 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.decons', shen_decons)

@tail_recursion
def shen_list_stream(KL_ARG_V2125_637, KL_ARG_V2126_638, KL_ARG_V2127_639, KL_ARG_V2128_640):

    class KL_Context:
        KL_LOC_Test_641 = None
        KL_LOC_Action_642 = None
        KL_LOC_Else_643 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Test_641', [symdic.symdic_kl_and, [[symdic.symdic_kl_consx63, [[symdic.symdic_kl_hd, [KL_ARG_V2127_639, []]], []]], [[symdic.symdic_kl_consx63, [[symdic.symdic_kl_hd, [[symdic.symdic_kl_hd, [KL_ARG_V2127_639, []]], []]], []]], []]]]), [setattr(KL_CTX, 'KL_LOC_Action_642', [symdic.symdic_shen_sndx45orx45fail, [tco_apply(shen_syntax, [KL_ARG_V2125_637, [symdic.symdic_shen_pair, [[symdic.symdic_kl_hd, [[symdic.symdic_kl_hd, [KL_ARG_V2127_639, []]], []]], [[symdic.symdic_shen_hdtl, [KL_ARG_V2127_639, []]], []]]], [symdic.symdic_shen_leavex33, [tco_apply(shen_syntax, [KL_ARG_V2126_638, [symdic.symdic_shen_pair, [[symdic.symdic_kl_tl, [[symdic.symdic_kl_hd, [KL_ARG_V2127_639, []]], []]], [[symdic.symdic_shen_hdtl, [KL_ARG_V2127_639, []]], []]]], KL_ARG_V2128_640]), []]]]), []]]), [setattr(KL_CTX, 'KL_LOC_Else_643', [symdic.symdic_kl_fail, []]), [symdic.symdic_kl_if, [KL_CTX.KL_LOC_Test_641, [KL_CTX.KL_LOC_Action_642, [KL_CTX.KL_LOC_Else_643, []]]]]][(-1)]][(-1)]][(-1)]
shen_add_fun('shen.list_stream', shen_list_stream)

@tail_recursion
def shen_sndx45orx45fail(KL_ARG_V2135_644):
    global symdic
    return (KL_ARG_V2135_644[1][0] if (shen_consp(KL_ARG_V2135_644) and (shen_consp(KL_ARG_V2135_644[1]) and shen_eq([], KL_ARG_V2135_644[1][1]))) else (tail_call(kl_fail, []) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.snd-or-fail', shen_sndx45orx45fail)

@tail_recursion
def shen_grammar_symbolx63(KL_ARG_V2136_645):

    class KL_Context:
        KL_LOC_Cs_646 = None
    KL_CTX = KL_Context()
    global symdic
    return (tco_apply(kl_symbolx63, [KL_ARG_V2136_645]) and [setattr(KL_CTX, 'KL_LOC_Cs_646', tco_apply(kl_explode, [KL_ARG_V2136_645])), (shen_eq(KL_CTX.KL_LOC_Cs_646[0], '<') and shen_eq(tco_apply(kl_reverse, [KL_CTX.KL_LOC_Cs_646])[0], '>'))][(-1)])
shen_add_fun('shen.grammar_symbol?', shen_grammar_symbolx63)

@tail_recursion
def shen_recursive_descent(KL_ARG_V2137_647, KL_ARG_V2138_648, KL_ARG_V2139_649):

    class KL_Context:
        KL_LOC_Test_650 = None
        KL_LOC_Action_651 = None
        KL_LOC_Else_652 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_Test_650', [KL_ARG_V2137_647[0], [KL_ARG_V2138_648, []]]), [setattr(KL_CTX, 'KL_LOC_Action_651', tco_apply(shen_syntax, [KL_ARG_V2137_647[1], tco_apply(kl_concat, [symdic.symdic_Parse_, KL_ARG_V2137_647[0]]), KL_ARG_V2139_649])), [setattr(KL_CTX, 'KL_LOC_Else_652', [symdic.symdic_kl_fail, []]), [symdic.symdic_kl_let, [tco_apply(kl_concat, [symdic.symdic_Parse_, KL_ARG_V2137_647[0]]), [KL_CTX.KL_LOC_Test_650, [[symdic.symdic_kl_if, [[symdic.symdic_kl_not, [[symdic.symdic_kl_x61, [[symdic.symdic_kl_fail, []], [tco_apply(kl_concat, [symdic.symdic_Parse_, KL_ARG_V2137_647[0]]), []]]], []]], [KL_CTX.KL_LOC_Action_651, [KL_CTX.KL_LOC_Else_652, []]]]], []]]]]][(-1)]][(-1)]][(-1)] if shen_consp(KL_ARG_V2137_647) else (tail_call(shen_sysx45error, [symdic.symdic_shen_recursive_descent]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.recursive_descent', shen_recursive_descent)

@tail_recursion
def shen_variablex45match(KL_ARG_V2140_653, KL_ARG_V2141_654, KL_ARG_V2142_655):

    class KL_Context:
        KL_LOC_Test_656 = None
        KL_LOC_Action_657 = None
        KL_LOC_Else_658 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_Test_656', [symdic.symdic_kl_consx63, [[symdic.symdic_kl_hd, [KL_ARG_V2141_654, []]], []]]), [setattr(KL_CTX, 'KL_LOC_Action_657', [symdic.symdic_kl_let, [tco_apply(kl_concat, [symdic.symdic_Parse_, KL_ARG_V2140_653[0]]), [[symdic.symdic_kl_hd, [[symdic.symdic_kl_hd, [KL_ARG_V2141_654, []]], []]], [tco_apply(shen_syntax, [KL_ARG_V2140_653[1], [symdic.symdic_shen_pair, [[symdic.symdic_kl_tl, [[symdic.symdic_kl_hd, [KL_ARG_V2141_654, []]], []]], [[symdic.symdic_shen_hdtl, [KL_ARG_V2141_654, []]], []]]], KL_ARG_V2142_655]), []]]]]), [setattr(KL_CTX, 'KL_LOC_Else_658', [symdic.symdic_kl_fail, []]), [symdic.symdic_kl_if, [KL_CTX.KL_LOC_Test_656, [KL_CTX.KL_LOC_Action_657, [KL_CTX.KL_LOC_Else_658, []]]]]][(-1)]][(-1)]][(-1)] if shen_consp(KL_ARG_V2140_653) else (tail_call(shen_sysx45error, [symdic.symdic_shen_variablex45match]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.variable-match', shen_variablex45match)

@tail_recursion
def shen_terminalx63(KL_ARG_V2151_659):
    global symdic
    return (False if shen_consp(KL_ARG_V2151_659) else (False if tco_apply(kl_variablex63, [KL_ARG_V2151_659]) else (True if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.terminal?', shen_terminalx63)

@tail_recursion
def shen_jump_streamx63(KL_ARG_V2156_660):
    global symdic
    return (True if shen_eq(KL_ARG_V2156_660, symdic.symdic_kl__) else (False if True else shen_simple_error('condition failure')))
shen_add_fun('shen.jump_stream?', shen_jump_streamx63)

@tail_recursion
def shen_check_stream(KL_ARG_V2157_661, KL_ARG_V2158_662, KL_ARG_V2159_663):

    class KL_Context:
        KL_LOC_Test_664 = None
        KL_LOC_Action_665 = None
        KL_LOC_Else_666 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_Test_664', [symdic.symdic_kl_and, [[symdic.symdic_kl_consx63, [[symdic.symdic_kl_hd, [KL_ARG_V2158_662, []]], []]], [[symdic.symdic_kl_x61, [KL_ARG_V2157_661[0], [[symdic.symdic_kl_hd, [[symdic.symdic_kl_hd, [KL_ARG_V2158_662, []]], []]], []]]], []]]]), [setattr(KL_CTX, 'KL_LOC_Action_665', tco_apply(shen_syntax, [KL_ARG_V2157_661[1], [symdic.symdic_shen_pair, [[symdic.symdic_kl_tl, [[symdic.symdic_kl_hd, [KL_ARG_V2158_662, []]], []]], [[symdic.symdic_shen_hdtl, [KL_ARG_V2158_662, []]], []]]], KL_ARG_V2159_663])), [setattr(KL_CTX, 'KL_LOC_Else_666', [symdic.symdic_kl_fail, []]), [symdic.symdic_kl_if, [KL_CTX.KL_LOC_Test_664, [KL_CTX.KL_LOC_Action_665, [KL_CTX.KL_LOC_Else_666, []]]]]][(-1)]][(-1)]][(-1)] if shen_consp(KL_ARG_V2157_661) else (tail_call(shen_sysx45error, [symdic.symdic_shen_check_stream]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.check_stream', shen_check_stream)

@tail_recursion
def shen_jump_stream(KL_ARG_V2160_667, KL_ARG_V2161_668, KL_ARG_V2162_669):

    class KL_Context:
        KL_LOC_Test_670 = None
        KL_LOC_Action_671 = None
        KL_LOC_Else_672 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_Test_670', [symdic.symdic_kl_consx63, [[symdic.symdic_kl_hd, [KL_ARG_V2161_668, []]], []]]), [setattr(KL_CTX, 'KL_LOC_Action_671', tco_apply(shen_syntax, [KL_ARG_V2160_667[1], [symdic.symdic_shen_pair, [[symdic.symdic_kl_tl, [[symdic.symdic_kl_hd, [KL_ARG_V2161_668, []]], []]], [[symdic.symdic_shen_hdtl, [KL_ARG_V2161_668, []]], []]]], KL_ARG_V2162_669])), [setattr(KL_CTX, 'KL_LOC_Else_672', [symdic.symdic_kl_fail, []]), [symdic.symdic_kl_if, [KL_CTX.KL_LOC_Test_670, [KL_CTX.KL_LOC_Action_671, [KL_CTX.KL_LOC_Else_672, []]]]]][(-1)]][(-1)]][(-1)] if shen_consp(KL_ARG_V2160_667) else (tail_call(shen_sysx45error, [symdic.symdic_shen_jump_stream]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.jump_stream', shen_jump_stream)

@tail_recursion
def shen_semantics(KL_ARG_V2163_673):
    global symdic
    return (KL_ARG_V2163_673[1][0] if (shen_consp(KL_ARG_V2163_673) and (shen_eq(symdic.symdic_shen_leavex33, KL_ARG_V2163_673[0]) and (shen_consp(KL_ARG_V2163_673[1]) and shen_eq([], KL_ARG_V2163_673[1][1])))) else ([] if shen_eq([], KL_ARG_V2163_673) else ([symdic.symdic_shen_hdtl, [tco_apply(kl_concat, [symdic.symdic_Parse_, KL_ARG_V2163_673]), []]] if tco_apply(shen_grammar_symbolx63, [KL_ARG_V2163_673]) else (tail_call(kl_concat, [symdic.symdic_Parse_, KL_ARG_V2163_673]) if tco_apply(kl_variablex63, [KL_ARG_V2163_673]) else (tail_call(kl_map, [symdic.symdic_shen_semantics, KL_ARG_V2163_673]) if shen_consp(KL_ARG_V2163_673) else (KL_ARG_V2163_673 if True else shen_simple_error('condition failure')))))))
shen_add_fun('shen.semantics', shen_semantics)

@tail_recursion
def kl_fail():
    global symdic
    return symdic.symdic_shen_failx33
shen_add_fun('fail', kl_fail)

@tail_recursion
def shen_pair(KL_ARG_V2164_674, KL_ARG_V2165_675):
    global symdic
    return [KL_ARG_V2164_674, [KL_ARG_V2165_675, []]]
shen_add_fun('shen.pair', shen_pair)

@tail_recursion
def shen_hdtl(KL_ARG_V2166_676):
    global symdic
    return KL_ARG_V2166_676[1][0]
shen_add_fun('shen.hdtl', shen_hdtl)

@tail_recursion
def x60x33x62(KL_ARG_V2173_677):
    global symdic
    return ([[], [KL_ARG_V2173_677[0], []]] if (shen_consp(KL_ARG_V2173_677) and (shen_consp(KL_ARG_V2173_677[1]) and shen_eq([], KL_ARG_V2173_677[1][1]))) else (tail_call(kl_fail, []) if True else shen_simple_error('condition failure')))
shen_add_fun('<!>', x60x33x62)

@tail_recursion
def kl_x60ex62(KL_ARG_V2178_678):
    global symdic
    return ([KL_ARG_V2178_678[0], [[], []]] if (shen_consp(KL_ARG_V2178_678) and (shen_consp(KL_ARG_V2178_678[1]) and shen_eq([], KL_ARG_V2178_678[1][1]))) else (tail_call(shen_sysx45error, [symdic.symdic_kl_x60ex62]) if True else shen_simple_error('condition failure')))
shen_add_fun('<e>', kl_x60ex62)


#============================== reader.kl==============================



@tail_recursion
def kl_lineread():
    global symdic
    return tail_call(shen_linereadx45loop, [shen_read_byte(tco_apply(kl_stinput, [])), []])
shen_add_fun('lineread', kl_lineread)

@tail_recursion
def shen_linereadx45loop(KL_ARG_V1300_679, KL_ARG_V1301_680):

    class KL_Context:
        KL_LOC_Line_681 = None
    KL_CTX = KL_Context()
    global symdic
    return (shen_simple_error('line read aborted') if shen_eq(KL_ARG_V1300_679, tco_apply(shen_hat, [])) else ([setattr(KL_CTX, 'KL_LOC_Line_681', tco_apply(kl_compile, [symdic.symdic_shen_x60st_inputx62, KL_ARG_V1301_680, (lambda KL_ARG_E_682: symdic.symdic_shen_nextline)])), (tail_call(shen_linereadx45loop, [shen_read_byte(tco_apply(kl_stinput, [])), tco_apply(kl_append, [KL_ARG_V1301_680, [KL_ARG_V1300_679, []]])]) if (shen_eq(KL_CTX.KL_LOC_Line_681, symdic.symdic_shen_nextline) or tco_apply(kl_emptyx63, [KL_CTX.KL_LOC_Line_681])) else KL_CTX.KL_LOC_Line_681)][(-1)] if tco_apply(kl_elementx63, [KL_ARG_V1300_679, [tco_apply(shen_newline, []), [tco_apply(shen_carriagex45return, []), []]]]) else (tail_call(shen_linereadx45loop, [shen_read_byte(tco_apply(kl_stinput, [])), tco_apply(kl_append, [KL_ARG_V1301_680, [KL_ARG_V1300_679, []]])]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.lineread-loop', shen_linereadx45loop)

@tail_recursion
def kl_readx45file(KL_ARG_V1302_683):

    class KL_Context:
        KL_LOC_Bytelist_684 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Bytelist_684', tco_apply(kl_readx45filex45asx45bytelist, [KL_ARG_V1302_683])), tail_call(kl_compile, [symdic.symdic_shen_x60st_inputx62, KL_CTX.KL_LOC_Bytelist_684, symdic.symdic_shen_readx45error])][(-1)]
shen_add_fun('read-file', kl_readx45file)

@tail_recursion
def shen_readx45error(KL_ARG_V1309_685):
    global symdic
    return (shen_simple_error(('read error here:\r\n\r\n ' + tco_apply(shen_app, [tco_apply(shen_compressx4550, [50, KL_ARG_V1309_685[0]]), '\r\n', symdic.symdic_shen_a]))) if (shen_consp(KL_ARG_V1309_685) and (shen_consp(KL_ARG_V1309_685[0]) and (shen_consp(KL_ARG_V1309_685[1]) and shen_eq([], KL_ARG_V1309_685[1][1])))) else (shen_simple_error('read error\r\n') if True else shen_simple_error('condition failure')))
shen_add_fun('shen.read-error', shen_readx45error)

@tail_recursion
def shen_compressx4550(KL_ARG_V1314_686, KL_ARG_V1315_687):
    global symdic
    return ('' if shen_eq([], KL_ARG_V1315_687) else ('' if shen_eq(0, KL_ARG_V1314_686) else ((chr(KL_ARG_V1315_687[0]) + tco_apply(shen_compressx4550, [(KL_ARG_V1314_686 - 1), KL_ARG_V1315_687[1]])) if shen_consp(KL_ARG_V1315_687) else (tail_call(shen_sysx45error, [symdic.symdic_shen_compressx4550]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.compress-50', shen_compressx4550)

@tail_recursion
def shen_x60st_inputx62(KL_ARG_V1320_688):

    class KL_Context:
        KL_LOC_Result_689 = None
        KL_LOC_Parse_shen_x60lsbx62_690 = None
        KL_LOC_Parse_shen_x60st_input1x62_691 = None
        KL_LOC_Parse_shen_x60rsbx62_692 = None
        KL_LOC_Parse_shen_x60st_input2x62_693 = None
        KL_LOC_Result_694 = None
        KL_LOC_Parse_shen_x60lrbx62_695 = None
        KL_LOC_Parse_shen_x60st_input1x62_696 = None
        KL_LOC_Parse_shen_x60rrbx62_697 = None
        KL_LOC_Parse_shen_x60st_input2x62_698 = None
        KL_LOC_Result_699 = None
        KL_LOC_Parse_shen_x60lcurlyx62_700 = None
        KL_LOC_Parse_shen_x60st_inputx62_701 = None
        KL_LOC_Result_702 = None
        KL_LOC_Parse_shen_x60rcurlyx62_703 = None
        KL_LOC_Parse_shen_x60st_inputx62_704 = None
        KL_LOC_Result_705 = None
        KL_LOC_Parse_shen_x60barx62_706 = None
        KL_LOC_Parse_shen_x60st_inputx62_707 = None
        KL_LOC_Result_708 = None
        KL_LOC_Parse_shen_x60semicolonx62_709 = None
        KL_LOC_Parse_shen_x60st_inputx62_710 = None
        KL_LOC_Result_711 = None
        KL_LOC_Parse_shen_x60colonx62_712 = None
        KL_LOC_Parse_shen_x60equalx62_713 = None
        KL_LOC_Parse_shen_x60st_inputx62_714 = None
        KL_LOC_Result_715 = None
        KL_LOC_Parse_shen_x60colonx62_716 = None
        KL_LOC_Parse_shen_x60minusx62_717 = None
        KL_LOC_Parse_shen_x60st_inputx62_718 = None
        KL_LOC_Result_719 = None
        KL_LOC_Parse_shen_x60colonx62_720 = None
        KL_LOC_Parse_shen_x60st_inputx62_721 = None
        KL_LOC_Result_722 = None
        KL_LOC_Parse_shen_x60commax62_723 = None
        KL_LOC_Parse_shen_x60st_inputx62_724 = None
        KL_LOC_Result_725 = None
        KL_LOC_Parse_shen_x60commentx62_726 = None
        KL_LOC_Parse_shen_x60st_inputx62_727 = None
        KL_LOC_Result_728 = None
        KL_LOC_Parse_shen_x60atomx62_729 = None
        KL_LOC_Parse_shen_x60st_inputx62_730 = None
        KL_LOC_Result_731 = None
        KL_LOC_Parse_shen_x60whitespacesx62_732 = None
        KL_LOC_Parse_shen_x60st_inputx62_733 = None
        KL_LOC_Result_734 = None
        KL_LOC_Parse_x60ex62_735 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_689', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60lsbx62_690', tco_apply(shen_x60lsbx62, [KL_ARG_V1320_688])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_input1x62_691', tco_apply(shen_x60st_input1x62, [KL_CTX.KL_LOC_Parse_shen_x60lsbx62_690])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60rsbx62_692', tco_apply(shen_x60rsbx62, [KL_CTX.KL_LOC_Parse_shen_x60st_input1x62_691])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_input2x62_693', tco_apply(shen_x60st_input2x62, [KL_CTX.KL_LOC_Parse_shen_x60rsbx62_692])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60st_input2x62_693[0], [tco_apply(kl_macroexpand, [tco_apply(shen_cons_form, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_input1x62_691])])]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_input2x62_693])]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60st_input2x62_693)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60rsbx62_692)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60st_input1x62_691)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60lsbx62_690)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_694', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60lrbx62_695', tco_apply(shen_x60lrbx62, [KL_ARG_V1320_688])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_input1x62_696', tco_apply(shen_x60st_input1x62, [KL_CTX.KL_LOC_Parse_shen_x60lrbx62_695])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60rrbx62_697', tco_apply(shen_x60rrbx62, [KL_CTX.KL_LOC_Parse_shen_x60st_input1x62_696])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_input2x62_698', tco_apply(shen_x60st_input2x62, [KL_CTX.KL_LOC_Parse_shen_x60rrbx62_697])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60st_input2x62_698[0], tco_apply(shen_packagex45macro, [tco_apply(kl_macroexpand, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_input1x62_696])]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_input2x62_698])])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60st_input2x62_698)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60rrbx62_697)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60st_input1x62_696)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60lrbx62_695)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_699', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60lcurlyx62_700', tco_apply(shen_x60lcurlyx62, [KL_ARG_V1320_688])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_inputx62_701', tco_apply(shen_x60st_inputx62, [KL_CTX.KL_LOC_Parse_shen_x60lcurlyx62_700])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_701[0], [symdic.symdic_kl_x123, tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_701])]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_701)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60lcurlyx62_700)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_702', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60rcurlyx62_703', tco_apply(shen_x60rcurlyx62, [KL_ARG_V1320_688])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_inputx62_704', tco_apply(shen_x60st_inputx62, [KL_CTX.KL_LOC_Parse_shen_x60rcurlyx62_703])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_704[0], [symdic.symdic_kl_x125, tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_704])]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_704)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60rcurlyx62_703)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_705', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60barx62_706', tco_apply(shen_x60barx62, [KL_ARG_V1320_688])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_inputx62_707', tco_apply(shen_x60st_inputx62, [KL_CTX.KL_LOC_Parse_shen_x60barx62_706])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_707[0], [symdic.symdic_kl_barx33, tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_707])]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_707)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60barx62_706)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_708', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60semicolonx62_709', tco_apply(shen_x60semicolonx62, [KL_ARG_V1320_688])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_inputx62_710', tco_apply(shen_x60st_inputx62, [KL_CTX.KL_LOC_Parse_shen_x60semicolonx62_709])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_710[0], [symdic.symdic_kl_x59, tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_710])]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_710)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60semicolonx62_709)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_711', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60colonx62_712', tco_apply(shen_x60colonx62, [KL_ARG_V1320_688])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60equalx62_713', tco_apply(shen_x60equalx62, [KL_CTX.KL_LOC_Parse_shen_x60colonx62_712])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_inputx62_714', tco_apply(shen_x60st_inputx62, [KL_CTX.KL_LOC_Parse_shen_x60equalx62_713])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_714[0], [symdic.symdic_kl_x58x61, tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_714])]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_714)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60equalx62_713)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60colonx62_712)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_715', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60colonx62_716', tco_apply(shen_x60colonx62, [KL_ARG_V1320_688])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60minusx62_717', tco_apply(shen_x60minusx62, [KL_CTX.KL_LOC_Parse_shen_x60colonx62_716])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_inputx62_718', tco_apply(shen_x60st_inputx62, [KL_CTX.KL_LOC_Parse_shen_x60minusx62_717])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_718[0], [symdic.symdic_kl_x58x45, tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_718])]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_718)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60minusx62_717)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60colonx62_716)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_719', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60colonx62_720', tco_apply(shen_x60colonx62, [KL_ARG_V1320_688])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_inputx62_721', tco_apply(shen_x60st_inputx62, [KL_CTX.KL_LOC_Parse_shen_x60colonx62_720])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_721[0], [symdic.symdic_kl_x58, tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_721])]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_721)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60colonx62_720)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_722', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60commax62_723', tco_apply(shen_x60commax62, [KL_ARG_V1320_688])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_inputx62_724', tco_apply(shen_x60st_inputx62, [KL_CTX.KL_LOC_Parse_shen_x60commax62_723])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_724[0], [shen_intern(','), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_724])]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_724)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60commax62_723)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_725', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60commentx62_726', tco_apply(shen_x60commentx62, [KL_ARG_V1320_688])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_inputx62_727', tco_apply(shen_x60st_inputx62, [KL_CTX.KL_LOC_Parse_shen_x60commentx62_726])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_727[0], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_727])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_727)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60commentx62_726)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_728', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60atomx62_729', tco_apply(shen_x60atomx62, [KL_ARG_V1320_688])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_inputx62_730', tco_apply(shen_x60st_inputx62, [KL_CTX.KL_LOC_Parse_shen_x60atomx62_729])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_730[0], [tco_apply(kl_macroexpand, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60atomx62_729])]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_730])]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_730)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60atomx62_729)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_731', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60whitespacesx62_732', tco_apply(shen_x60whitespacesx62, [KL_ARG_V1320_688])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_inputx62_733', tco_apply(shen_x60st_inputx62, [KL_CTX.KL_LOC_Parse_shen_x60whitespacesx62_732])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_733[0], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_733])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_733)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60whitespacesx62_732)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_734', [setattr(KL_CTX, 'KL_LOC_Parse_x60ex62_735', tco_apply(kl_x60ex62, [KL_ARG_V1320_688])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_x60ex62_735[0], []]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_x60ex62_735)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_734, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_734)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_731, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_731)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_728, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_728)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_725, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_725)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_722, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_722)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_719, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_719)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_715, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_715)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_711, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_711)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_708, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_708)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_705, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_705)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_702, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_702)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_699, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_699)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_694, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_694)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_689, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_689)][(-1)]
shen_add_fun('shen.<st_input>', shen_x60st_inputx62)

@tail_recursion
def shen_x60lsbx62(KL_ARG_V1325_736):

    class KL_Context:
        KL_LOC_Result_737 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_737', (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1325_736[0][1], tco_apply(shen_hdtl, [KL_ARG_V1325_736])])[0], symdic.symdic_shen_skip]) if (shen_consp(KL_ARG_V1325_736[0]) and shen_eq(91, KL_ARG_V1325_736[0][0])) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_737, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_737)][(-1)]
shen_add_fun('shen.<lsb>', shen_x60lsbx62)

@tail_recursion
def shen_x60rsbx62(KL_ARG_V1330_738):

    class KL_Context:
        KL_LOC_Result_739 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_739', (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1330_738[0][1], tco_apply(shen_hdtl, [KL_ARG_V1330_738])])[0], symdic.symdic_shen_skip]) if (shen_consp(KL_ARG_V1330_738[0]) and shen_eq(93, KL_ARG_V1330_738[0][0])) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_739, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_739)][(-1)]
shen_add_fun('shen.<rsb>', shen_x60rsbx62)

@tail_recursion
def shen_x60lcurlyx62(KL_ARG_V1335_740):

    class KL_Context:
        KL_LOC_Result_741 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_741', (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1335_740[0][1], tco_apply(shen_hdtl, [KL_ARG_V1335_740])])[0], symdic.symdic_shen_skip]) if (shen_consp(KL_ARG_V1335_740[0]) and shen_eq(123, KL_ARG_V1335_740[0][0])) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_741, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_741)][(-1)]
shen_add_fun('shen.<lcurly>', shen_x60lcurlyx62)

@tail_recursion
def shen_x60rcurlyx62(KL_ARG_V1340_742):

    class KL_Context:
        KL_LOC_Result_743 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_743', (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1340_742[0][1], tco_apply(shen_hdtl, [KL_ARG_V1340_742])])[0], symdic.symdic_shen_skip]) if (shen_consp(KL_ARG_V1340_742[0]) and shen_eq(125, KL_ARG_V1340_742[0][0])) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_743, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_743)][(-1)]
shen_add_fun('shen.<rcurly>', shen_x60rcurlyx62)

@tail_recursion
def shen_x60barx62(KL_ARG_V1345_744):

    class KL_Context:
        KL_LOC_Result_745 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_745', (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1345_744[0][1], tco_apply(shen_hdtl, [KL_ARG_V1345_744])])[0], symdic.symdic_shen_skip]) if (shen_consp(KL_ARG_V1345_744[0]) and shen_eq(124, KL_ARG_V1345_744[0][0])) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_745, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_745)][(-1)]
shen_add_fun('shen.<bar>', shen_x60barx62)

@tail_recursion
def shen_x60semicolonx62(KL_ARG_V1350_746):

    class KL_Context:
        KL_LOC_Result_747 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_747', (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1350_746[0][1], tco_apply(shen_hdtl, [KL_ARG_V1350_746])])[0], symdic.symdic_shen_skip]) if (shen_consp(KL_ARG_V1350_746[0]) and shen_eq(59, KL_ARG_V1350_746[0][0])) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_747, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_747)][(-1)]
shen_add_fun('shen.<semicolon>', shen_x60semicolonx62)

@tail_recursion
def shen_x60colonx62(KL_ARG_V1355_748):

    class KL_Context:
        KL_LOC_Result_749 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_749', (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1355_748[0][1], tco_apply(shen_hdtl, [KL_ARG_V1355_748])])[0], symdic.symdic_shen_skip]) if (shen_consp(KL_ARG_V1355_748[0]) and shen_eq(58, KL_ARG_V1355_748[0][0])) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_749, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_749)][(-1)]
shen_add_fun('shen.<colon>', shen_x60colonx62)

@tail_recursion
def shen_x60commax62(KL_ARG_V1360_750):

    class KL_Context:
        KL_LOC_Result_751 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_751', (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1360_750[0][1], tco_apply(shen_hdtl, [KL_ARG_V1360_750])])[0], symdic.symdic_shen_skip]) if (shen_consp(KL_ARG_V1360_750[0]) and shen_eq(44, KL_ARG_V1360_750[0][0])) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_751, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_751)][(-1)]
shen_add_fun('shen.<comma>', shen_x60commax62)

@tail_recursion
def shen_x60equalx62(KL_ARG_V1365_752):

    class KL_Context:
        KL_LOC_Result_753 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_753', (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1365_752[0][1], tco_apply(shen_hdtl, [KL_ARG_V1365_752])])[0], symdic.symdic_shen_skip]) if (shen_consp(KL_ARG_V1365_752[0]) and shen_eq(61, KL_ARG_V1365_752[0][0])) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_753, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_753)][(-1)]
shen_add_fun('shen.<equal>', shen_x60equalx62)

@tail_recursion
def shen_x60minusx62(KL_ARG_V1370_754):

    class KL_Context:
        KL_LOC_Result_755 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_755', (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1370_754[0][1], tco_apply(shen_hdtl, [KL_ARG_V1370_754])])[0], symdic.symdic_shen_skip]) if (shen_consp(KL_ARG_V1370_754[0]) and shen_eq(45, KL_ARG_V1370_754[0][0])) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_755, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_755)][(-1)]
shen_add_fun('shen.<minus>', shen_x60minusx62)

@tail_recursion
def shen_x60lrbx62(KL_ARG_V1375_756):

    class KL_Context:
        KL_LOC_Result_757 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_757', (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1375_756[0][1], tco_apply(shen_hdtl, [KL_ARG_V1375_756])])[0], symdic.symdic_shen_skip]) if (shen_consp(KL_ARG_V1375_756[0]) and shen_eq(40, KL_ARG_V1375_756[0][0])) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_757, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_757)][(-1)]
shen_add_fun('shen.<lrb>', shen_x60lrbx62)

@tail_recursion
def shen_x60rrbx62(KL_ARG_V1380_758):

    class KL_Context:
        KL_LOC_Result_759 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_759', (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1380_758[0][1], tco_apply(shen_hdtl, [KL_ARG_V1380_758])])[0], symdic.symdic_shen_skip]) if (shen_consp(KL_ARG_V1380_758[0]) and shen_eq(41, KL_ARG_V1380_758[0][0])) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_759, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_759)][(-1)]
shen_add_fun('shen.<rrb>', shen_x60rrbx62)

@tail_recursion
def shen_x60atomx62(KL_ARG_V1385_760):

    class KL_Context:
        KL_LOC_Result_761 = None
        KL_LOC_Parse_shen_x60strx62_762 = None
        KL_LOC_Result_763 = None
        KL_LOC_Parse_shen_x60numberx62_764 = None
        KL_LOC_Result_765 = None
        KL_LOC_Parse_shen_x60symx62_766 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_761', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60strx62_762', tco_apply(shen_x60strx62, [KL_ARG_V1385_760])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60strx62_762[0], tco_apply(shen_controlx45chars, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60strx62_762])])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60strx62_762)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_763', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60numberx62_764', tco_apply(shen_x60numberx62, [KL_ARG_V1385_760])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60numberx62_764[0], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60numberx62_764])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60numberx62_764)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_765', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60symx62_766', tco_apply(shen_x60symx62, [KL_ARG_V1385_760])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60symx62_766[0], ([symdic.symdic_kl_vector, [0, []]] if shen_eq(tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60symx62_766]), '<>') else shen_intern(tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60symx62_766])))]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60symx62_766)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_765, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_765)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_763, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_763)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_761, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_761)][(-1)]
shen_add_fun('shen.<atom>', shen_x60atomx62)

@tail_recursion
def shen_controlx45chars(KL_ARG_V1386_767):

    class KL_Context:
        KL_LOC_CodePoint_768 = None
        KL_LOC_AfterCodePoint_769 = None
    KL_CTX = KL_Context()
    global symdic
    return ('' if shen_eq([], KL_ARG_V1386_767) else ([setattr(KL_CTX, 'KL_LOC_CodePoint_768', tco_apply(shen_codex45point, [KL_ARG_V1386_767[1][1]])), [setattr(KL_CTX, 'KL_LOC_AfterCodePoint_769', tco_apply(shen_afterx45codepoint, [KL_ARG_V1386_767[1][1]])), tail_call(kl_x64s, [chr(tco_apply(shen_decimalise, [KL_CTX.KL_LOC_CodePoint_768])), tco_apply(shen_controlx45chars, [KL_CTX.KL_LOC_AfterCodePoint_769])])][(-1)]][(-1)] if (shen_consp(KL_ARG_V1386_767) and (shen_eq('c', KL_ARG_V1386_767[0]) and (shen_consp(KL_ARG_V1386_767[1]) and shen_eq('#', KL_ARG_V1386_767[1][0])))) else (tail_call(kl_x64s, [KL_ARG_V1386_767[0], tco_apply(shen_controlx45chars, [KL_ARG_V1386_767[1]])]) if shen_consp(KL_ARG_V1386_767) else (tail_call(shen_sysx45error, [symdic.symdic_shen_controlx45chars]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.control-chars', shen_controlx45chars)

@tail_recursion
def shen_codex45point(KL_ARG_V1389_770):
    global symdic
    return ('' if (shen_consp(KL_ARG_V1389_770) and shen_eq(';', KL_ARG_V1389_770[0])) else ([KL_ARG_V1389_770[0], tco_apply(shen_codex45point, [KL_ARG_V1389_770[1]])] if (shen_consp(KL_ARG_V1389_770) and tco_apply(kl_elementx63, [KL_ARG_V1389_770[0], ['0', ['1', ['2', ['3', ['4', ['5', ['6', ['7', ['8', ['9', ['0', []]]]]]]]]]]]])) else (shen_simple_error(('code point parse error ' + tco_apply(shen_app, [KL_ARG_V1389_770, '\r\n', symdic.symdic_shen_a]))) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.code-point', shen_codex45point)

@tail_recursion
def shen_afterx45codepoint(KL_ARG_V1394_771):
    global symdic
    return ([] if shen_eq([], KL_ARG_V1394_771) else (KL_ARG_V1394_771[1] if (shen_consp(KL_ARG_V1394_771) and shen_eq(';', KL_ARG_V1394_771[0])) else (tail_call(shen_afterx45codepoint, [KL_ARG_V1394_771[1]]) if shen_consp(KL_ARG_V1394_771) else (tail_call(shen_sysx45error, [symdic.symdic_shen_afterx45codepoint]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.after-codepoint', shen_afterx45codepoint)

@tail_recursion
def shen_decimalise(KL_ARG_V1395_772):
    global symdic
    return tail_call(shen_pre, [tco_apply(kl_reverse, [tco_apply(shen_digitsx45x62integers, [KL_ARG_V1395_772])]), 0])
shen_add_fun('shen.decimalise', shen_decimalise)

@tail_recursion
def shen_digitsx45x62integers(KL_ARG_V1400_773):
    global symdic
    return ([0, tco_apply(shen_digitsx45x62integers, [KL_ARG_V1400_773[1]])] if (shen_consp(KL_ARG_V1400_773) and shen_eq('0', KL_ARG_V1400_773[0])) else ([1, tco_apply(shen_digitsx45x62integers, [KL_ARG_V1400_773[1]])] if (shen_consp(KL_ARG_V1400_773) and shen_eq('1', KL_ARG_V1400_773[0])) else ([2, tco_apply(shen_digitsx45x62integers, [KL_ARG_V1400_773[1]])] if (shen_consp(KL_ARG_V1400_773) and shen_eq('2', KL_ARG_V1400_773[0])) else ([3, tco_apply(shen_digitsx45x62integers, [KL_ARG_V1400_773[1]])] if (shen_consp(KL_ARG_V1400_773) and shen_eq('3', KL_ARG_V1400_773[0])) else ([4, tco_apply(shen_digitsx45x62integers, [KL_ARG_V1400_773[1]])] if (shen_consp(KL_ARG_V1400_773) and shen_eq('4', KL_ARG_V1400_773[0])) else ([5, tco_apply(shen_digitsx45x62integers, [KL_ARG_V1400_773[1]])] if (shen_consp(KL_ARG_V1400_773) and shen_eq('5', KL_ARG_V1400_773[0])) else ([6, tco_apply(shen_digitsx45x62integers, [KL_ARG_V1400_773[1]])] if (shen_consp(KL_ARG_V1400_773) and shen_eq('6', KL_ARG_V1400_773[0])) else ([7, tco_apply(shen_digitsx45x62integers, [KL_ARG_V1400_773[1]])] if (shen_consp(KL_ARG_V1400_773) and shen_eq('7', KL_ARG_V1400_773[0])) else ([8, tco_apply(shen_digitsx45x62integers, [KL_ARG_V1400_773[1]])] if (shen_consp(KL_ARG_V1400_773) and shen_eq('8', KL_ARG_V1400_773[0])) else ([9, tco_apply(shen_digitsx45x62integers, [KL_ARG_V1400_773[1]])] if (shen_consp(KL_ARG_V1400_773) and shen_eq('9', KL_ARG_V1400_773[0])) else ([] if True else shen_simple_error('condition failure'))))))))))))
shen_add_fun('shen.digits->integers', shen_digitsx45x62integers)

@tail_recursion
def shen_x60symx62(KL_ARG_V1405_774):

    class KL_Context:
        KL_LOC_Result_775 = None
        KL_LOC_Parse_shen_x60alphax62_776 = None
        KL_LOC_Parse_shen_x60alphanumsx62_777 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_775', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60alphax62_776', tco_apply(shen_x60alphax62, [KL_ARG_V1405_774])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60alphanumsx62_777', tco_apply(shen_x60alphanumsx62, [KL_CTX.KL_LOC_Parse_shen_x60alphax62_776])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60alphanumsx62_777[0], tco_apply(kl_x64s, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60alphax62_776]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60alphanumsx62_777])])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60alphanumsx62_777)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60alphax62_776)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_775, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_775)][(-1)]
shen_add_fun('shen.<sym>', shen_x60symx62)

@tail_recursion
def shen_x60alphanumsx62(KL_ARG_V1410_778):

    class KL_Context:
        KL_LOC_Result_779 = None
        KL_LOC_Parse_shen_x60alphanumx62_780 = None
        KL_LOC_Parse_shen_x60alphanumsx62_781 = None
        KL_LOC_Result_782 = None
        KL_LOC_Parse_x60ex62_783 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_779', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60alphanumx62_780', tco_apply(shen_x60alphanumx62, [KL_ARG_V1410_778])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60alphanumsx62_781', tco_apply(shen_x60alphanumsx62, [KL_CTX.KL_LOC_Parse_shen_x60alphanumx62_780])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60alphanumsx62_781[0], tco_apply(kl_x64s, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60alphanumx62_780]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60alphanumsx62_781])])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60alphanumsx62_781)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60alphanumx62_780)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_782', [setattr(KL_CTX, 'KL_LOC_Parse_x60ex62_783', tco_apply(kl_x60ex62, [KL_ARG_V1410_778])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_x60ex62_783[0], '']) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_x60ex62_783)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_782, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_782)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_779, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_779)][(-1)]
shen_add_fun('shen.<alphanums>', shen_x60alphanumsx62)

@tail_recursion
def shen_x60alphanumx62(KL_ARG_V1415_784):

    class KL_Context:
        KL_LOC_Result_785 = None
        KL_LOC_Parse_shen_x60alphax62_786 = None
        KL_LOC_Result_787 = None
        KL_LOC_Parse_shen_x60numx62_788 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_785', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60alphax62_786', tco_apply(shen_x60alphax62, [KL_ARG_V1415_784])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60alphax62_786[0], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60alphax62_786])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60alphax62_786)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_787', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60numx62_788', tco_apply(shen_x60numx62, [KL_ARG_V1415_784])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60numx62_788[0], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60numx62_788])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60numx62_788)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_787, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_787)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_785, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_785)][(-1)]
shen_add_fun('shen.<alphanum>', shen_x60alphanumx62)

@tail_recursion
def shen_x60numx62(KL_ARG_V1420_789):

    class KL_Context:
        KL_LOC_Result_790 = None
        KL_LOC_Parse_Byte_791 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_790', ([setattr(KL_CTX, 'KL_LOC_Parse_Byte_791', KL_ARG_V1420_789[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1420_789[0][1], tco_apply(shen_hdtl, [KL_ARG_V1420_789])])[0], chr(KL_CTX.KL_LOC_Parse_Byte_791)]) if tco_apply(shen_numbytex63, [KL_CTX.KL_LOC_Parse_Byte_791]) else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V1420_789[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_790, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_790)][(-1)]
shen_add_fun('shen.<num>', shen_x60numx62)

@tail_recursion
def shen_numbytex63(KL_ARG_V1425_792):
    global symdic
    return (True if shen_eq(48, KL_ARG_V1425_792) else (True if shen_eq(49, KL_ARG_V1425_792) else (True if shen_eq(50, KL_ARG_V1425_792) else (True if shen_eq(51, KL_ARG_V1425_792) else (True if shen_eq(52, KL_ARG_V1425_792) else (True if shen_eq(53, KL_ARG_V1425_792) else (True if shen_eq(54, KL_ARG_V1425_792) else (True if shen_eq(55, KL_ARG_V1425_792) else (True if shen_eq(56, KL_ARG_V1425_792) else (True if shen_eq(57, KL_ARG_V1425_792) else (False if True else shen_simple_error('condition failure'))))))))))))
shen_add_fun('shen.numbyte?', shen_numbytex63)

@tail_recursion
def shen_x60alphax62(KL_ARG_V1430_793):

    class KL_Context:
        KL_LOC_Result_794 = None
        KL_LOC_Parse_Byte_795 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_794', ([setattr(KL_CTX, 'KL_LOC_Parse_Byte_795', KL_ARG_V1430_793[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1430_793[0][1], tco_apply(shen_hdtl, [KL_ARG_V1430_793])])[0], chr(KL_CTX.KL_LOC_Parse_Byte_795)]) if tco_apply(shen_symbolx45codex63, [KL_CTX.KL_LOC_Parse_Byte_795]) else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V1430_793[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_794, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_794)][(-1)]
shen_add_fun('shen.<alpha>', shen_x60alphax62)

@tail_recursion
def shen_symbolx45codex63(KL_ARG_V1431_796):
    global symdic
    return (shen_eq(KL_ARG_V1431_796, 126) or (((KL_ARG_V1431_796 > 94) and (KL_ARG_V1431_796 < 123)) or (((KL_ARG_V1431_796 > 59) and (KL_ARG_V1431_796 < 91)) or (((KL_ARG_V1431_796 > 41) and ((KL_ARG_V1431_796 < 58) and (not shen_eq(KL_ARG_V1431_796, 44)))) or (((KL_ARG_V1431_796 > 34) and (KL_ARG_V1431_796 < 40)) or shen_eq(KL_ARG_V1431_796, 33))))))
shen_add_fun('shen.symbol-code?', shen_symbolx45codex63)

@tail_recursion
def shen_x60strx62(KL_ARG_V1436_797):

    class KL_Context:
        KL_LOC_Result_798 = None
        KL_LOC_Parse_shen_x60dbqx62_799 = None
        KL_LOC_Parse_shen_x60strcontentsx62_800 = None
        KL_LOC_Parse_shen_x60dbqx62_801 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_798', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60dbqx62_799', tco_apply(shen_x60dbqx62, [KL_ARG_V1436_797])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60strcontentsx62_800', tco_apply(shen_x60strcontentsx62, [KL_CTX.KL_LOC_Parse_shen_x60dbqx62_799])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60dbqx62_801', tco_apply(shen_x60dbqx62, [KL_CTX.KL_LOC_Parse_shen_x60strcontentsx62_800])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60dbqx62_801[0], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60strcontentsx62_800])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60dbqx62_801)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60strcontentsx62_800)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60dbqx62_799)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_798, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_798)][(-1)]
shen_add_fun('shen.<str>', shen_x60strx62)

@tail_recursion
def shen_x60dbqx62(KL_ARG_V1441_802):

    class KL_Context:
        KL_LOC_Result_803 = None
        KL_LOC_Parse_Byte_804 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_803', ([setattr(KL_CTX, 'KL_LOC_Parse_Byte_804', KL_ARG_V1441_802[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1441_802[0][1], tco_apply(shen_hdtl, [KL_ARG_V1441_802])])[0], KL_CTX.KL_LOC_Parse_Byte_804]) if shen_eq(KL_CTX.KL_LOC_Parse_Byte_804, 34) else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V1441_802[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_803, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_803)][(-1)]
shen_add_fun('shen.<dbq>', shen_x60dbqx62)

@tail_recursion
def shen_x60strcontentsx62(KL_ARG_V1446_805):

    class KL_Context:
        KL_LOC_Result_806 = None
        KL_LOC_Parse_shen_x60strcx62_807 = None
        KL_LOC_Parse_shen_x60strcontentsx62_808 = None
        KL_LOC_Result_809 = None
        KL_LOC_Parse_x60ex62_810 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_806', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60strcx62_807', tco_apply(shen_x60strcx62, [KL_ARG_V1446_805])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60strcontentsx62_808', tco_apply(shen_x60strcontentsx62, [KL_CTX.KL_LOC_Parse_shen_x60strcx62_807])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60strcontentsx62_808[0], [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60strcx62_807]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60strcontentsx62_808])]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60strcontentsx62_808)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60strcx62_807)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_809', [setattr(KL_CTX, 'KL_LOC_Parse_x60ex62_810', tco_apply(kl_x60ex62, [KL_ARG_V1446_805])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_x60ex62_810[0], []]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_x60ex62_810)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_809, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_809)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_806, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_806)][(-1)]
shen_add_fun('shen.<strcontents>', shen_x60strcontentsx62)

@tail_recursion
def shen_x60bytex62(KL_ARG_V1451_811):

    class KL_Context:
        KL_LOC_Result_812 = None
        KL_LOC_Parse_Byte_813 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_812', ([setattr(KL_CTX, 'KL_LOC_Parse_Byte_813', KL_ARG_V1451_811[0][0]), tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1451_811[0][1], tco_apply(shen_hdtl, [KL_ARG_V1451_811])])[0], chr(KL_CTX.KL_LOC_Parse_Byte_813)])][(-1)] if shen_consp(KL_ARG_V1451_811[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_812, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_812)][(-1)]
shen_add_fun('shen.<byte>', shen_x60bytex62)

@tail_recursion
def shen_x60strcx62(KL_ARG_V1456_814):

    class KL_Context:
        KL_LOC_Result_815 = None
        KL_LOC_Parse_Byte_816 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_815', ([setattr(KL_CTX, 'KL_LOC_Parse_Byte_816', KL_ARG_V1456_814[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1456_814[0][1], tco_apply(shen_hdtl, [KL_ARG_V1456_814])])[0], chr(KL_CTX.KL_LOC_Parse_Byte_816)]) if (not shen_eq(KL_CTX.KL_LOC_Parse_Byte_816, 34)) else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V1456_814[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_815, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_815)][(-1)]
shen_add_fun('shen.<strc>', shen_x60strcx62)

@tail_recursion
def shen_x60backslashx62(KL_ARG_V1461_817):

    class KL_Context:
        KL_LOC_Result_818 = None
        KL_LOC_Parse_Byte_819 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_818', ([setattr(KL_CTX, 'KL_LOC_Parse_Byte_819', KL_ARG_V1461_817[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1461_817[0][1], tco_apply(shen_hdtl, [KL_ARG_V1461_817])])[0], chr(KL_CTX.KL_LOC_Parse_Byte_819)]) if shen_eq(KL_CTX.KL_LOC_Parse_Byte_819, 92) else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V1461_817[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_818, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_818)][(-1)]
shen_add_fun('shen.<backslash>', shen_x60backslashx62)

@tail_recursion
def shen_x60numberx62(KL_ARG_V1466_820):

    class KL_Context:
        KL_LOC_Result_821 = None
        KL_LOC_Parse_shen_x60minusx62_822 = None
        KL_LOC_Parse_shen_x60numberx62_823 = None
        KL_LOC_Result_824 = None
        KL_LOC_Parse_shen_x60plusx62_825 = None
        KL_LOC_Parse_shen_x60numberx62_826 = None
        KL_LOC_Result_827 = None
        KL_LOC_Parse_shen_x60predigitsx62_828 = None
        KL_LOC_Parse_shen_x60stopx62_829 = None
        KL_LOC_Parse_shen_x60postdigitsx62_830 = None
        KL_LOC_Parse_shen_x60Ex62_831 = None
        KL_LOC_Parse_shen_x60log10x62_832 = None
        KL_LOC_Result_833 = None
        KL_LOC_Parse_shen_x60digitsx62_834 = None
        KL_LOC_Parse_shen_x60Ex62_835 = None
        KL_LOC_Parse_shen_x60log10x62_836 = None
        KL_LOC_Result_837 = None
        KL_LOC_Parse_shen_x60predigitsx62_838 = None
        KL_LOC_Parse_shen_x60stopx62_839 = None
        KL_LOC_Parse_shen_x60postdigitsx62_840 = None
        KL_LOC_Result_841 = None
        KL_LOC_Parse_shen_x60digitsx62_842 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_821', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60minusx62_822', tco_apply(shen_x60minusx62, [KL_ARG_V1466_820])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60numberx62_823', tco_apply(shen_x60numberx62, [KL_CTX.KL_LOC_Parse_shen_x60minusx62_822])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60numberx62_823[0], (0 - tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60numberx62_823]))]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60numberx62_823)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60minusx62_822)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_824', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60plusx62_825', tco_apply(shen_x60plusx62, [KL_ARG_V1466_820])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60numberx62_826', tco_apply(shen_x60numberx62, [KL_CTX.KL_LOC_Parse_shen_x60plusx62_825])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60numberx62_826[0], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60numberx62_826])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60numberx62_826)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60plusx62_825)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_827', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60predigitsx62_828', tco_apply(shen_x60predigitsx62, [KL_ARG_V1466_820])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60stopx62_829', tco_apply(shen_x60stopx62, [KL_CTX.KL_LOC_Parse_shen_x60predigitsx62_828])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60postdigitsx62_830', tco_apply(shen_x60postdigitsx62, [KL_CTX.KL_LOC_Parse_shen_x60stopx62_829])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60Ex62_831', tco_apply(shen_x60Ex62, [KL_CTX.KL_LOC_Parse_shen_x60postdigitsx62_830])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60log10x62_832', tco_apply(shen_x60log10x62, [KL_CTX.KL_LOC_Parse_shen_x60Ex62_831])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60log10x62_832[0], (tco_apply(shen_expt, [10, tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60log10x62_832])]) * (tco_apply(shen_pre, [tco_apply(kl_reverse, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60predigitsx62_828])]), 0]) + tco_apply(shen_post, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60postdigitsx62_830]), 1])))]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60log10x62_832)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60Ex62_831)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60postdigitsx62_830)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60stopx62_829)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60predigitsx62_828)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_833', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60digitsx62_834', tco_apply(shen_x60digitsx62, [KL_ARG_V1466_820])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60Ex62_835', tco_apply(shen_x60Ex62, [KL_CTX.KL_LOC_Parse_shen_x60digitsx62_834])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60log10x62_836', tco_apply(shen_x60log10x62, [KL_CTX.KL_LOC_Parse_shen_x60Ex62_835])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60log10x62_836[0], (tco_apply(shen_expt, [10, tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60log10x62_836])]) * tco_apply(shen_pre, [tco_apply(kl_reverse, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60digitsx62_834])]), 0]))]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60log10x62_836)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60Ex62_835)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60digitsx62_834)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_837', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60predigitsx62_838', tco_apply(shen_x60predigitsx62, [KL_ARG_V1466_820])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60stopx62_839', tco_apply(shen_x60stopx62, [KL_CTX.KL_LOC_Parse_shen_x60predigitsx62_838])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60postdigitsx62_840', tco_apply(shen_x60postdigitsx62, [KL_CTX.KL_LOC_Parse_shen_x60stopx62_839])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60postdigitsx62_840[0], (tco_apply(shen_pre, [tco_apply(kl_reverse, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60predigitsx62_838])]), 0]) + tco_apply(shen_post, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60postdigitsx62_840]), 1]))]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60postdigitsx62_840)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60stopx62_839)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60predigitsx62_838)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_841', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60digitsx62_842', tco_apply(shen_x60digitsx62, [KL_ARG_V1466_820])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60digitsx62_842[0], tco_apply(shen_pre, [tco_apply(kl_reverse, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60digitsx62_842])]), 0])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60digitsx62_842)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_841, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_841)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_837, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_837)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_833, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_833)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_827, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_827)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_824, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_824)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_821, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_821)][(-1)]
shen_add_fun('shen.<number>', shen_x60numberx62)

@tail_recursion
def shen_x60Ex62(KL_ARG_V1471_843):

    class KL_Context:
        KL_LOC_Result_844 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_844', (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1471_843[0][1], tco_apply(shen_hdtl, [KL_ARG_V1471_843])])[0], symdic.symdic_shen_skip]) if (shen_consp(KL_ARG_V1471_843[0]) and shen_eq(101, KL_ARG_V1471_843[0][0])) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_844, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_844)][(-1)]
shen_add_fun('shen.<E>', shen_x60Ex62)

@tail_recursion
def shen_x60log10x62(KL_ARG_V1476_845):

    class KL_Context:
        KL_LOC_Result_846 = None
        KL_LOC_Parse_shen_x60minusx62_847 = None
        KL_LOC_Parse_shen_x60digitsx62_848 = None
        KL_LOC_Result_849 = None
        KL_LOC_Parse_shen_x60digitsx62_850 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_846', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60minusx62_847', tco_apply(shen_x60minusx62, [KL_ARG_V1476_845])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60digitsx62_848', tco_apply(shen_x60digitsx62, [KL_CTX.KL_LOC_Parse_shen_x60minusx62_847])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60digitsx62_848[0], (0 - tco_apply(shen_pre, [tco_apply(kl_reverse, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60digitsx62_848])]), 0]))]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60digitsx62_848)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60minusx62_847)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_849', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60digitsx62_850', tco_apply(shen_x60digitsx62, [KL_ARG_V1476_845])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60digitsx62_850[0], tco_apply(shen_pre, [tco_apply(kl_reverse, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60digitsx62_850])]), 0])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60digitsx62_850)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_849, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_849)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_846, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_846)][(-1)]
shen_add_fun('shen.<log10>', shen_x60log10x62)

@tail_recursion
def shen_x60plusx62(KL_ARG_V1481_851):

    class KL_Context:
        KL_LOC_Result_852 = None
        KL_LOC_Parse_Byte_853 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_852', ([setattr(KL_CTX, 'KL_LOC_Parse_Byte_853', KL_ARG_V1481_851[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1481_851[0][1], tco_apply(shen_hdtl, [KL_ARG_V1481_851])])[0], KL_CTX.KL_LOC_Parse_Byte_853]) if shen_eq(KL_CTX.KL_LOC_Parse_Byte_853, 43) else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V1481_851[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_852, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_852)][(-1)]
shen_add_fun('shen.<plus>', shen_x60plusx62)

@tail_recursion
def shen_x60stopx62(KL_ARG_V1486_854):

    class KL_Context:
        KL_LOC_Result_855 = None
        KL_LOC_Parse_Byte_856 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_855', ([setattr(KL_CTX, 'KL_LOC_Parse_Byte_856', KL_ARG_V1486_854[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1486_854[0][1], tco_apply(shen_hdtl, [KL_ARG_V1486_854])])[0], KL_CTX.KL_LOC_Parse_Byte_856]) if shen_eq(KL_CTX.KL_LOC_Parse_Byte_856, 46) else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V1486_854[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_855, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_855)][(-1)]
shen_add_fun('shen.<stop>', shen_x60stopx62)

@tail_recursion
def shen_x60predigitsx62(KL_ARG_V1491_857):

    class KL_Context:
        KL_LOC_Result_858 = None
        KL_LOC_Parse_shen_x60digitsx62_859 = None
        KL_LOC_Result_860 = None
        KL_LOC_Parse_x60ex62_861 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_858', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60digitsx62_859', tco_apply(shen_x60digitsx62, [KL_ARG_V1491_857])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60digitsx62_859[0], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60digitsx62_859])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60digitsx62_859)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_860', [setattr(KL_CTX, 'KL_LOC_Parse_x60ex62_861', tco_apply(kl_x60ex62, [KL_ARG_V1491_857])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_x60ex62_861[0], []]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_x60ex62_861)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_860, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_860)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_858, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_858)][(-1)]
shen_add_fun('shen.<predigits>', shen_x60predigitsx62)

@tail_recursion
def shen_x60postdigitsx62(KL_ARG_V1496_862):

    class KL_Context:
        KL_LOC_Result_863 = None
        KL_LOC_Parse_shen_x60digitsx62_864 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_863', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60digitsx62_864', tco_apply(shen_x60digitsx62, [KL_ARG_V1496_862])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60digitsx62_864[0], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60digitsx62_864])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60digitsx62_864)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_863, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_863)][(-1)]
shen_add_fun('shen.<postdigits>', shen_x60postdigitsx62)

@tail_recursion
def shen_x60digitsx62(KL_ARG_V1501_865):

    class KL_Context:
        KL_LOC_Result_866 = None
        KL_LOC_Parse_shen_x60digitx62_867 = None
        KL_LOC_Parse_shen_x60digitsx62_868 = None
        KL_LOC_Result_869 = None
        KL_LOC_Parse_shen_x60digitx62_870 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_866', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60digitx62_867', tco_apply(shen_x60digitx62, [KL_ARG_V1501_865])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60digitsx62_868', tco_apply(shen_x60digitsx62, [KL_CTX.KL_LOC_Parse_shen_x60digitx62_867])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60digitsx62_868[0], [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60digitx62_867]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60digitsx62_868])]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60digitsx62_868)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60digitx62_867)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_869', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60digitx62_870', tco_apply(shen_x60digitx62, [KL_ARG_V1501_865])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60digitx62_870[0], [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60digitx62_870]), []]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60digitx62_870)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_869, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_869)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_866, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_866)][(-1)]
shen_add_fun('shen.<digits>', shen_x60digitsx62)

@tail_recursion
def shen_x60digitx62(KL_ARG_V1506_871):

    class KL_Context:
        KL_LOC_Result_872 = None
        KL_LOC_Parse_X_873 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_872', ([setattr(KL_CTX, 'KL_LOC_Parse_X_873', KL_ARG_V1506_871[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1506_871[0][1], tco_apply(shen_hdtl, [KL_ARG_V1506_871])])[0], tco_apply(shen_bytex45x62digit, [KL_CTX.KL_LOC_Parse_X_873])]) if tco_apply(shen_numbytex63, [KL_CTX.KL_LOC_Parse_X_873]) else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V1506_871[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_872, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_872)][(-1)]
shen_add_fun('shen.<digit>', shen_x60digitx62)

@tail_recursion
def shen_bytex45x62digit(KL_ARG_V1507_874):
    global symdic
    return (0 if shen_eq(48, KL_ARG_V1507_874) else (1 if shen_eq(49, KL_ARG_V1507_874) else (2 if shen_eq(50, KL_ARG_V1507_874) else (3 if shen_eq(51, KL_ARG_V1507_874) else (4 if shen_eq(52, KL_ARG_V1507_874) else (5 if shen_eq(53, KL_ARG_V1507_874) else (6 if shen_eq(54, KL_ARG_V1507_874) else (7 if shen_eq(55, KL_ARG_V1507_874) else (8 if shen_eq(56, KL_ARG_V1507_874) else (9 if shen_eq(57, KL_ARG_V1507_874) else (tail_call(shen_sysx45error, [symdic.symdic_shen_bytex45x62digit]) if True else shen_simple_error('condition failure'))))))))))))
shen_add_fun('shen.byte->digit', shen_bytex45x62digit)

@tail_recursion
def shen_pre(KL_ARG_V1510_875, KL_ARG_V1511_876):
    global symdic
    return (0 if shen_eq([], KL_ARG_V1510_875) else (((tco_apply(shen_expt, [10, KL_ARG_V1511_876]) * KL_ARG_V1510_875[0]) + tco_apply(shen_pre, [KL_ARG_V1510_875[1], (KL_ARG_V1511_876 + 1)])) if shen_consp(KL_ARG_V1510_875) else (tail_call(shen_sysx45error, [symdic.symdic_shen_pre]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.pre', shen_pre)

@tail_recursion
def shen_post(KL_ARG_V1514_877, KL_ARG_V1515_878):
    global symdic
    return (0 if shen_eq([], KL_ARG_V1514_877) else (((tco_apply(shen_expt, [10, (0 - KL_ARG_V1515_878)]) * KL_ARG_V1514_877[0]) + tco_apply(shen_post, [KL_ARG_V1514_877[1], (KL_ARG_V1515_878 + 1)])) if shen_consp(KL_ARG_V1514_877) else (tail_call(shen_sysx45error, [symdic.symdic_shen_post]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.post', shen_post)

@tail_recursion
def shen_expt(KL_ARG_V1518_879, KL_ARG_V1519_880):
    global symdic
    return (1 if shen_eq(0, KL_ARG_V1519_880) else ((KL_ARG_V1518_879 * tco_apply(shen_expt, [KL_ARG_V1518_879, (KL_ARG_V1519_880 - 1)])) if (KL_ARG_V1519_880 > 0) else ((1 * (tco_apply(shen_expt, [KL_ARG_V1518_879, (KL_ARG_V1519_880 + 1)]) / KL_ARG_V1518_879)) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.expt', shen_expt)

@tail_recursion
def shen_x60st_input1x62(KL_ARG_V1524_881):

    class KL_Context:
        KL_LOC_Result_882 = None
        KL_LOC_Parse_shen_x60st_inputx62_883 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_882', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_inputx62_883', tco_apply(shen_x60st_inputx62, [KL_ARG_V1524_881])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_883[0], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_883])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_883)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_882, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_882)][(-1)]
shen_add_fun('shen.<st_input1>', shen_x60st_input1x62)

@tail_recursion
def shen_x60st_input2x62(KL_ARG_V1529_884):

    class KL_Context:
        KL_LOC_Result_885 = None
        KL_LOC_Parse_shen_x60st_inputx62_886 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_885', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_inputx62_886', tco_apply(shen_x60st_inputx62, [KL_ARG_V1529_884])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_886[0], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_886])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_886)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_885, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_885)][(-1)]
shen_add_fun('shen.<st_input2>', shen_x60st_input2x62)

@tail_recursion
def shen_x60commentx62(KL_ARG_V1534_887):

    class KL_Context:
        KL_LOC_Result_888 = None
        KL_LOC_Parse_shen_x60backslashx62_889 = None
        KL_LOC_Parse_shen_x60timesx62_890 = None
        KL_LOC_Parse_shen_x60anyx62_891 = None
        KL_LOC_Parse_shen_x60timesx62_892 = None
        KL_LOC_Parse_shen_x60backslashx62_893 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_888', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60backslashx62_889', tco_apply(shen_x60backslashx62, [KL_ARG_V1534_887])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60timesx62_890', tco_apply(shen_x60timesx62, [KL_CTX.KL_LOC_Parse_shen_x60backslashx62_889])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60anyx62_891', tco_apply(shen_x60anyx62, [KL_CTX.KL_LOC_Parse_shen_x60timesx62_890])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60timesx62_892', tco_apply(shen_x60timesx62, [KL_CTX.KL_LOC_Parse_shen_x60anyx62_891])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60backslashx62_893', tco_apply(shen_x60backslashx62, [KL_CTX.KL_LOC_Parse_shen_x60timesx62_892])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60backslashx62_893[0], symdic.symdic_shen_skip]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60backslashx62_893)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60timesx62_892)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60anyx62_891)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60timesx62_890)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60backslashx62_889)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_888, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_888)][(-1)]
shen_add_fun('shen.<comment>', shen_x60commentx62)

@tail_recursion
def shen_x60timesx62(KL_ARG_V1539_894):

    class KL_Context:
        KL_LOC_Result_895 = None
        KL_LOC_Parse_Byte_896 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_895', ([setattr(KL_CTX, 'KL_LOC_Parse_Byte_896', KL_ARG_V1539_894[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1539_894[0][1], tco_apply(shen_hdtl, [KL_ARG_V1539_894])])[0], KL_CTX.KL_LOC_Parse_Byte_896]) if shen_eq(KL_CTX.KL_LOC_Parse_Byte_896, 42) else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V1539_894[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_895, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_895)][(-1)]
shen_add_fun('shen.<times>', shen_x60timesx62)

@tail_recursion
def shen_x60anyx62(KL_ARG_V1544_897):

    class KL_Context:
        KL_LOC_Result_898 = None
        KL_LOC_Parse_shen_x60commentx62_899 = None
        KL_LOC_Parse_shen_x60anyx62_900 = None
        KL_LOC_Result_901 = None
        KL_LOC_Parse_shen_x60blahx62_902 = None
        KL_LOC_Parse_shen_x60anyx62_903 = None
        KL_LOC_Result_904 = None
        KL_LOC_Parse_x60ex62_905 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_898', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60commentx62_899', tco_apply(shen_x60commentx62, [KL_ARG_V1544_897])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60anyx62_900', tco_apply(shen_x60anyx62, [KL_CTX.KL_LOC_Parse_shen_x60commentx62_899])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60anyx62_900[0], symdic.symdic_shen_skip]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60anyx62_900)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60commentx62_899)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_901', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60blahx62_902', tco_apply(shen_x60blahx62, [KL_ARG_V1544_897])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60anyx62_903', tco_apply(shen_x60anyx62, [KL_CTX.KL_LOC_Parse_shen_x60blahx62_902])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60anyx62_903[0], symdic.symdic_shen_skip]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60anyx62_903)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60blahx62_902)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_904', [setattr(KL_CTX, 'KL_LOC_Parse_x60ex62_905', tco_apply(kl_x60ex62, [KL_ARG_V1544_897])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_x60ex62_905[0], symdic.symdic_shen_skip]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_x60ex62_905)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_904, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_904)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_901, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_901)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_898, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_898)][(-1)]
shen_add_fun('shen.<any>', shen_x60anyx62)

@tail_recursion
def shen_x60blahx62(KL_ARG_V1557_906):
    global symdic
    return (tail_call(kl_fail, []) if (shen_consp(KL_ARG_V1557_906) and (shen_consp(KL_ARG_V1557_906[0]) and (shen_eq(42, KL_ARG_V1557_906[0][0]) and (shen_consp(KL_ARG_V1557_906[0][1]) and shen_eq(92, KL_ARG_V1557_906[0][1][0]))))) else ([KL_ARG_V1557_906[0][1], [symdic.symdic_shen_skip, []]] if (shen_consp(KL_ARG_V1557_906) and (shen_consp(KL_ARG_V1557_906[0]) and (shen_consp(KL_ARG_V1557_906[1]) and shen_eq([], KL_ARG_V1557_906[1][1])))) else (tail_call(kl_fail, []) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.<blah>', shen_x60blahx62)

@tail_recursion
def shen_x60whitespacesx62(KL_ARG_V1562_907):

    class KL_Context:
        KL_LOC_Result_908 = None
        KL_LOC_Parse_shen_x60whitespacex62_909 = None
        KL_LOC_Parse_shen_x60whitespacesx62_910 = None
        KL_LOC_Result_911 = None
        KL_LOC_Parse_shen_x60whitespacex62_912 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_908', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60whitespacex62_909', tco_apply(shen_x60whitespacex62, [KL_ARG_V1562_907])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60whitespacesx62_910', tco_apply(shen_x60whitespacesx62, [KL_CTX.KL_LOC_Parse_shen_x60whitespacex62_909])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60whitespacesx62_910[0], symdic.symdic_shen_skip]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60whitespacesx62_910)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60whitespacex62_909)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_911', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60whitespacex62_912', tco_apply(shen_x60whitespacex62, [KL_ARG_V1562_907])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60whitespacex62_912[0], symdic.symdic_shen_skip]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60whitespacex62_912)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_911, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_911)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_908, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_908)][(-1)]
shen_add_fun('shen.<whitespaces>', shen_x60whitespacesx62)

@tail_recursion
def shen_x60whitespacex62(KL_ARG_V1567_913):

    class KL_Context:
        KL_LOC_Result_914 = None
        KL_LOC_Parse_X_915 = None
        KL_LOC_Parse_Case_916 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_914', ([setattr(KL_CTX, 'KL_LOC_Parse_X_915', KL_ARG_V1567_913[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1567_913[0][1], tco_apply(shen_hdtl, [KL_ARG_V1567_913])])[0], symdic.symdic_shen_skip]) if [setattr(KL_CTX, 'KL_LOC_Parse_Case_916', KL_CTX.KL_LOC_Parse_X_915), (shen_eq(KL_CTX.KL_LOC_Parse_Case_916, 32) or (shen_eq(KL_CTX.KL_LOC_Parse_Case_916, 13) or (shen_eq(KL_CTX.KL_LOC_Parse_Case_916, 10) or shen_eq(KL_CTX.KL_LOC_Parse_Case_916, 9))))][(-1)] else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V1567_913[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_914, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_914)][(-1)]
shen_add_fun('shen.<whitespace>', shen_x60whitespacex62)

@tail_recursion
def shen_cons_form(KL_ARG_V1568_917):
    global symdic
    return ([] if shen_eq([], KL_ARG_V1568_917) else ([symdic.symdic_kl_cons, [KL_ARG_V1568_917[0], KL_ARG_V1568_917[1][1]]] if (shen_consp(KL_ARG_V1568_917) and (shen_consp(KL_ARG_V1568_917[1]) and (shen_consp(KL_ARG_V1568_917[1][1]) and (shen_eq([], KL_ARG_V1568_917[1][1][1]) and shen_eq(KL_ARG_V1568_917[1][0], symdic.symdic_kl_barx33))))) else ([symdic.symdic_kl_cons, [KL_ARG_V1568_917[0], [tco_apply(shen_cons_form, [KL_ARG_V1568_917[1]]), []]]] if shen_consp(KL_ARG_V1568_917) else (tail_call(shen_sysx45error, [symdic.symdic_shen_cons_form]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.cons_form', shen_cons_form)

@tail_recursion
def shen_packagex45macro(KL_ARG_V1571_918, KL_ARG_V1572_919):

    class KL_Context:
        KL_LOC_ListofExceptions_920 = None
        KL_LOC_Record_921 = None
        KL_LOC_PackageNameDot_922 = None
    KL_CTX = KL_Context()
    global symdic
    return (tail_call(kl_append, [tco_apply(kl_explode, [KL_ARG_V1571_918[1][0]]), KL_ARG_V1572_919]) if (shen_consp(KL_ARG_V1571_918) and (shen_eq(symdic.symdic_kl_x36, KL_ARG_V1571_918[0]) and (shen_consp(KL_ARG_V1571_918[1]) and shen_eq([], KL_ARG_V1571_918[1][1])))) else (tail_call(kl_append, [KL_ARG_V1571_918[1][1][1], KL_ARG_V1572_919]) if (shen_consp(KL_ARG_V1571_918) and (shen_eq(symdic.symdic_kl_package, KL_ARG_V1571_918[0]) and (shen_consp(KL_ARG_V1571_918[1]) and (shen_eq(symdic.symdic_kl_null, KL_ARG_V1571_918[1][0]) and shen_consp(KL_ARG_V1571_918[1][1]))))) else ([setattr(KL_CTX, 'KL_LOC_ListofExceptions_920', tco_apply(shen_evalx45withoutx45macros, [KL_ARG_V1571_918[1][1][0]])), [setattr(KL_CTX, 'KL_LOC_Record_921', tco_apply(shen_recordx45exceptions, [KL_CTX.KL_LOC_ListofExceptions_920, KL_ARG_V1571_918[1][0]])), [setattr(KL_CTX, 'KL_LOC_PackageNameDot_922', shen_intern((str(KL_ARG_V1571_918[1][0]) + '.'))), tail_call(kl_append, [tco_apply(shen_packageh, [KL_CTX.KL_LOC_PackageNameDot_922, KL_CTX.KL_LOC_ListofExceptions_920, KL_ARG_V1571_918[1][1][1]]), KL_ARG_V1572_919])][(-1)]][(-1)]][(-1)] if (shen_consp(KL_ARG_V1571_918) and (shen_eq(symdic.symdic_kl_package, KL_ARG_V1571_918[0]) and (shen_consp(KL_ARG_V1571_918[1]) and shen_consp(KL_ARG_V1571_918[1][1])))) else ([KL_ARG_V1571_918, KL_ARG_V1572_919] if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.package-macro', shen_packagex45macro)

@tail_recursion
def shen_recordx45exceptions(KL_ARG_V1573_923, KL_ARG_V1574_924):

    class KL_Context:
        KL_LOC_CurrExceptions_925 = None
        KL_LOC_AllExceptions_927 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_CurrExceptions_925', shen_try_except((lambda : tco_apply(kl_get, [KL_ARG_V1574_924, symdic.symdic_shen_externalx45symbols, shen_get(symdic.symdic_kl_x42propertyx45vectorx42)])), (lambda KL_ARG_E_926: []))), [setattr(KL_CTX, 'KL_LOC_AllExceptions_927', tco_apply(kl_union, [KL_ARG_V1573_923, KL_CTX.KL_LOC_CurrExceptions_925])), tail_call(kl_put, [KL_ARG_V1574_924, symdic.symdic_shen_externalx45symbols, KL_CTX.KL_LOC_AllExceptions_927, shen_get(symdic.symdic_kl_x42propertyx45vectorx42)])][(-1)]][(-1)]
shen_add_fun('shen.record-exceptions', shen_recordx45exceptions)

@tail_recursion
def shen_packageh(KL_ARG_V1583_928, KL_ARG_V1584_929, KL_ARG_V1585_930):
    global symdic
    return ([tco_apply(shen_packageh, [KL_ARG_V1583_928, KL_ARG_V1584_929, KL_ARG_V1585_930[0]]), tco_apply(shen_packageh, [KL_ARG_V1583_928, KL_ARG_V1584_929, KL_ARG_V1585_930[1]])] if shen_consp(KL_ARG_V1585_930) else (KL_ARG_V1585_930 if (tco_apply(shen_sysfuncx63, [KL_ARG_V1585_930]) or (tco_apply(kl_variablex63, [KL_ARG_V1585_930]) or (tco_apply(kl_elementx63, [KL_ARG_V1585_930, KL_ARG_V1584_929]) or (tco_apply(shen_doubleunderlinex63, [KL_ARG_V1585_930]) or tco_apply(shen_singleunderlinex63, [KL_ARG_V1585_930]))))) else (tail_call(kl_concat, [KL_ARG_V1583_928, KL_ARG_V1585_930]) if (tco_apply(kl_symbolx63, [KL_ARG_V1585_930]) and (not tco_apply(shen_prefixx63, [['s', ['h', ['e', ['n', ['.', []]]]]], tco_apply(kl_explode, [KL_ARG_V1585_930])]))) else (KL_ARG_V1585_930 if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.packageh', shen_packageh)

@tail_recursion
def kl_readx45fromx45string(KL_ARG_V1586_931):

    class KL_Context:
        KL_LOC_Ns_932 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Ns_932', tco_apply(kl_map, [(lambda KL_ARG_V1298_933: ord(KL_ARG_V1298_933)), tco_apply(kl_explode, [KL_ARG_V1586_931])])), tail_call(kl_compile, [symdic.symdic_shen_x60st_inputx62, KL_CTX.KL_LOC_Ns_932, symdic.symdic_shen_readx45error])][(-1)]
shen_add_fun('read-from-string', kl_readx45fromx45string)


#============================== prolog.kl==============================



@tail_recursion
def shen_x60defprologx62(KL_ARG_V898_934):

    class KL_Context:
        KL_LOC_Result_935 = None
        KL_LOC_Parse_shen_x60predicatex42x62_936 = None
        KL_LOC_Parse_shen_x60clausesx42x62_937 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_935', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60predicatex42x62_936', tco_apply(shen_x60predicatex42x62, [KL_ARG_V898_934])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60clausesx42x62_937', tco_apply(shen_x60clausesx42x62, [KL_CTX.KL_LOC_Parse_shen_x60predicatex42x62_936])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60clausesx42x62_937[0], tco_apply(shen_prologx45x62shen, [tco_apply(kl_map, [(lambda KL_ARG_Parse_X_938: tail_call(shen_insertx45predicate, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60predicatex42x62_936]), KL_ARG_Parse_X_938])), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60clausesx42x62_937])])])[0]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60clausesx42x62_937)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60predicatex42x62_936)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_935, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_935)][(-1)]
shen_add_fun('shen.<defprolog>', shen_x60defprologx62)

@tail_recursion
def shen_prologx45error(KL_ARG_V905_939, KL_ARG_V906_940):
    global symdic
    return (shen_simple_error(('prolog syntax error in ' + tco_apply(shen_app, [KL_ARG_V905_939, (' here:\r\n\r\n ' + tco_apply(shen_app, [tco_apply(shen_nextx4550, [50, KL_ARG_V906_940[0]]), '\r\n', symdic.symdic_shen_a])), symdic.symdic_shen_a]))) if (shen_consp(KL_ARG_V906_940) and (shen_consp(KL_ARG_V906_940[1]) and shen_eq([], KL_ARG_V906_940[1][1]))) else (shen_simple_error(('prolog syntax error in ' + tco_apply(shen_app, [KL_ARG_V905_939, '\r\n', symdic.symdic_shen_a]))) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.prolog-error', shen_prologx45error)

@tail_recursion
def shen_nextx4550(KL_ARG_V911_941, KL_ARG_V912_942):
    global symdic
    return ('' if shen_eq([], KL_ARG_V912_942) else ('' if shen_eq(0, KL_ARG_V911_941) else ((tco_apply(shen_deconsx45string, [KL_ARG_V912_942[0]]) + tco_apply(shen_nextx4550, [(KL_ARG_V911_941 - 1), KL_ARG_V912_942[1]])) if shen_consp(KL_ARG_V912_942) else (tail_call(shen_sysx45error, [symdic.symdic_shen_nextx4550]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.next-50', shen_nextx4550)

@tail_recursion
def shen_deconsx45string(KL_ARG_V913_943):
    global symdic
    return (tail_call(shen_app, [tco_apply(shen_evalx45cons, [KL_ARG_V913_943]), ' ', symdic.symdic_shen_s]) if (shen_consp(KL_ARG_V913_943) and (shen_eq(symdic.symdic_kl_cons, KL_ARG_V913_943[0]) and (shen_consp(KL_ARG_V913_943[1]) and (shen_consp(KL_ARG_V913_943[1][1]) and shen_eq([], KL_ARG_V913_943[1][1][1]))))) else (tail_call(shen_app, [KL_ARG_V913_943, ' ', symdic.symdic_shen_r]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.decons-string', shen_deconsx45string)

@tail_recursion
def shen_insertx45predicate(KL_ARG_V914_944, KL_ARG_V915_945):
    global symdic
    return ([[KL_ARG_V914_944, KL_ARG_V915_945[0]], [symdic.symdic_kl_x58x45, KL_ARG_V915_945[1]]] if (shen_consp(KL_ARG_V915_945) and (shen_consp(KL_ARG_V915_945[1]) and shen_eq([], KL_ARG_V915_945[1][1]))) else (tail_call(shen_sysx45error, [symdic.symdic_shen_insertx45predicate]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.insert-predicate', shen_insertx45predicate)

@tail_recursion
def shen_x60predicatex42x62(KL_ARG_V920_946):

    class KL_Context:
        KL_LOC_Result_947 = None
        KL_LOC_Parse_X_948 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_947', ([setattr(KL_CTX, 'KL_LOC_Parse_X_948', KL_ARG_V920_946[0][0]), tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V920_946[0][1], tco_apply(shen_hdtl, [KL_ARG_V920_946])])[0], KL_CTX.KL_LOC_Parse_X_948])][(-1)] if shen_consp(KL_ARG_V920_946[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_947, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_947)][(-1)]
shen_add_fun('shen.<predicate*>', shen_x60predicatex42x62)

@tail_recursion
def shen_x60clausesx42x62(KL_ARG_V925_949):

    class KL_Context:
        KL_LOC_Result_950 = None
        KL_LOC_Parse_shen_x60clausex42x62_951 = None
        KL_LOC_Parse_shen_x60clausesx42x62_952 = None
        KL_LOC_Result_953 = None
        KL_LOC_Parse_x60ex62_954 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_950', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60clausex42x62_951', tco_apply(shen_x60clausex42x62, [KL_ARG_V925_949])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60clausesx42x62_952', tco_apply(shen_x60clausesx42x62, [KL_CTX.KL_LOC_Parse_shen_x60clausex42x62_951])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60clausesx42x62_952[0], [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60clausex42x62_951]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60clausesx42x62_952])]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60clausesx42x62_952)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60clausex42x62_951)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_953', [setattr(KL_CTX, 'KL_LOC_Parse_x60ex62_954', tco_apply(kl_x60ex62, [KL_ARG_V925_949])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_x60ex62_954[0], tco_apply(kl_append, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_x60ex62_954]), []])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_x60ex62_954)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_953, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_953)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_950, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_950)][(-1)]
shen_add_fun('shen.<clauses*>', shen_x60clausesx42x62)

@tail_recursion
def shen_x60clausex42x62(KL_ARG_V930_955):

    class KL_Context:
        KL_LOC_Result_956 = None
        KL_LOC_Parse_shen_x60headx42x62_957 = None
        KL_LOC_Parse_shen_x60bodyx42x62_958 = None
        KL_LOC_Parse_shen_x60endx42x62_959 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_956', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60headx42x62_957', tco_apply(shen_x60headx42x62, [KL_ARG_V930_955])), (([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60bodyx42x62_958', tco_apply(shen_x60bodyx42x62, [tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60headx42x62_957[0][1], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60headx42x62_957])])])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60endx42x62_959', tco_apply(shen_x60endx42x62, [KL_CTX.KL_LOC_Parse_shen_x60bodyx42x62_958])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60endx42x62_959[0], [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60headx42x62_957]), [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60bodyx42x62_958]), []]]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60endx42x62_959)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60bodyx42x62_958)) else tco_apply(kl_fail, []))][(-1)] if (shen_consp(KL_CTX.KL_LOC_Parse_shen_x60headx42x62_957[0]) and shen_eq(symdic.symdic_kl_x60x45x45, KL_CTX.KL_LOC_Parse_shen_x60headx42x62_957[0][0])) else tco_apply(kl_fail, [])) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60headx42x62_957)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_956, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_956)][(-1)]
shen_add_fun('shen.<clause*>', shen_x60clausex42x62)

@tail_recursion
def shen_x60headx42x62(KL_ARG_V935_960):

    class KL_Context:
        KL_LOC_Result_961 = None
        KL_LOC_Parse_shen_x60termx42x62_962 = None
        KL_LOC_Parse_shen_x60headx42x62_963 = None
        KL_LOC_Result_964 = None
        KL_LOC_Parse_x60ex62_965 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_961', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60termx42x62_962', tco_apply(shen_x60termx42x62, [KL_ARG_V935_960])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60headx42x62_963', tco_apply(shen_x60headx42x62, [KL_CTX.KL_LOC_Parse_shen_x60termx42x62_962])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60headx42x62_963[0], [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60termx42x62_962]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60headx42x62_963])]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60headx42x62_963)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60termx42x62_962)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_964', [setattr(KL_CTX, 'KL_LOC_Parse_x60ex62_965', tco_apply(kl_x60ex62, [KL_ARG_V935_960])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_x60ex62_965[0], tco_apply(kl_append, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_x60ex62_965]), []])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_x60ex62_965)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_964, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_964)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_961, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_961)][(-1)]
shen_add_fun('shen.<head*>', shen_x60headx42x62)

@tail_recursion
def shen_x60termx42x62(KL_ARG_V940_966):

    class KL_Context:
        KL_LOC_Result_967 = None
        KL_LOC_Parse_X_968 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_967', ([setattr(KL_CTX, 'KL_LOC_Parse_X_968', KL_ARG_V940_966[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V940_966[0][1], tco_apply(shen_hdtl, [KL_ARG_V940_966])])[0], tco_apply(shen_evalx45cons, [KL_CTX.KL_LOC_Parse_X_968])]) if ((not shen_eq(symdic.symdic_kl_x60x45x45, KL_CTX.KL_LOC_Parse_X_968)) and tco_apply(shen_legitimatex45termx63, [KL_CTX.KL_LOC_Parse_X_968])) else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V940_966[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_967, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_967)][(-1)]
shen_add_fun('shen.<term*>', shen_x60termx42x62)

@tail_recursion
def shen_legitimatex45termx63(KL_ARG_V945_969):
    global symdic
    return ((tco_apply(shen_legitimatex45termx63, [KL_ARG_V945_969[1][0]]) and tco_apply(shen_legitimatex45termx63, [KL_ARG_V945_969[1][1][0]])) if (shen_consp(KL_ARG_V945_969) and (shen_eq(symdic.symdic_kl_cons, KL_ARG_V945_969[0]) and (shen_consp(KL_ARG_V945_969[1]) and (shen_consp(KL_ARG_V945_969[1][1]) and shen_eq([], KL_ARG_V945_969[1][1][1]))))) else (tail_call(shen_legitimatex45termx63, [KL_ARG_V945_969[1][0]]) if (shen_consp(KL_ARG_V945_969) and (shen_eq(symdic.symdic_kl_mode, KL_ARG_V945_969[0]) and (shen_consp(KL_ARG_V945_969[1]) and (shen_consp(KL_ARG_V945_969[1][1]) and (shen_eq(symdic.symdic_kl_x43, KL_ARG_V945_969[1][1][0]) and shen_eq([], KL_ARG_V945_969[1][1][1])))))) else (tail_call(shen_legitimatex45termx63, [KL_ARG_V945_969[1][0]]) if (shen_consp(KL_ARG_V945_969) and (shen_eq(symdic.symdic_kl_mode, KL_ARG_V945_969[0]) and (shen_consp(KL_ARG_V945_969[1]) and (shen_consp(KL_ARG_V945_969[1][1]) and (shen_eq(symdic.symdic_kl_x45, KL_ARG_V945_969[1][1][0]) and shen_eq([], KL_ARG_V945_969[1][1][1])))))) else (False if shen_consp(KL_ARG_V945_969) else (True if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.legitimate-term?', shen_legitimatex45termx63)

@tail_recursion
def shen_evalx45cons(KL_ARG_V946_970):
    global symdic
    return ([tco_apply(shen_evalx45cons, [KL_ARG_V946_970[1][0]]), tco_apply(shen_evalx45cons, [KL_ARG_V946_970[1][1][0]])] if (shen_consp(KL_ARG_V946_970) and (shen_eq(symdic.symdic_kl_cons, KL_ARG_V946_970[0]) and (shen_consp(KL_ARG_V946_970[1]) and (shen_consp(KL_ARG_V946_970[1][1]) and shen_eq([], KL_ARG_V946_970[1][1][1]))))) else ([symdic.symdic_kl_mode, [tco_apply(shen_evalx45cons, [KL_ARG_V946_970[1][0]]), KL_ARG_V946_970[1][1]]] if (shen_consp(KL_ARG_V946_970) and (shen_eq(symdic.symdic_kl_mode, KL_ARG_V946_970[0]) and (shen_consp(KL_ARG_V946_970[1]) and (shen_consp(KL_ARG_V946_970[1][1]) and shen_eq([], KL_ARG_V946_970[1][1][1]))))) else (KL_ARG_V946_970 if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.eval-cons', shen_evalx45cons)

@tail_recursion
def shen_x60bodyx42x62(KL_ARG_V951_971):

    class KL_Context:
        KL_LOC_Result_972 = None
        KL_LOC_Parse_shen_x60literalx42x62_973 = None
        KL_LOC_Parse_shen_x60bodyx42x62_974 = None
        KL_LOC_Result_975 = None
        KL_LOC_Parse_x60ex62_976 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_972', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60literalx42x62_973', tco_apply(shen_x60literalx42x62, [KL_ARG_V951_971])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60bodyx42x62_974', tco_apply(shen_x60bodyx42x62, [KL_CTX.KL_LOC_Parse_shen_x60literalx42x62_973])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60bodyx42x62_974[0], [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60literalx42x62_973]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60bodyx42x62_974])]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60bodyx42x62_974)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60literalx42x62_973)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_975', [setattr(KL_CTX, 'KL_LOC_Parse_x60ex62_976', tco_apply(kl_x60ex62, [KL_ARG_V951_971])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_x60ex62_976[0], tco_apply(kl_append, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_x60ex62_976]), []])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_x60ex62_976)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_975, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_975)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_972, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_972)][(-1)]
shen_add_fun('shen.<body*>', shen_x60bodyx42x62)

@tail_recursion
def shen_x60literalx42x62(KL_ARG_V956_977):

    class KL_Context:
        KL_LOC_Result_978 = None
        KL_LOC_Result_979 = None
        KL_LOC_Parse_X_980 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_978', (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V956_977[0][1], tco_apply(shen_hdtl, [KL_ARG_V956_977])])[0], [symdic.symdic_kl_cut, [shen_intern('Throwcontrol'), []]]]) if (shen_consp(KL_ARG_V956_977[0]) and shen_eq(symdic.symdic_kl_x33, KL_ARG_V956_977[0][0])) else tco_apply(kl_fail, []))), ([setattr(KL_CTX, 'KL_LOC_Result_979', ([setattr(KL_CTX, 'KL_LOC_Parse_X_980', KL_ARG_V956_977[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V956_977[0][1], tco_apply(shen_hdtl, [KL_ARG_V956_977])])[0], KL_CTX.KL_LOC_Parse_X_980]) if shen_consp(KL_CTX.KL_LOC_Parse_X_980) else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V956_977[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_979, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_979)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_978, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_978)][(-1)]
shen_add_fun('shen.<literal*>', shen_x60literalx42x62)

@tail_recursion
def shen_x60endx42x62(KL_ARG_V961_981):

    class KL_Context:
        KL_LOC_Result_982 = None
        KL_LOC_Parse_X_983 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_982', ([setattr(KL_CTX, 'KL_LOC_Parse_X_983', KL_ARG_V961_981[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V961_981[0][1], tco_apply(shen_hdtl, [KL_ARG_V961_981])])[0], KL_CTX.KL_LOC_Parse_X_983]) if shen_eq(KL_CTX.KL_LOC_Parse_X_983, symdic.symdic_kl_x59) else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V961_981[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_982, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_982)][(-1)]
shen_add_fun('shen.<end*>', shen_x60endx42x62)

@tail_recursion
def kl_cut(KL_ARG_V962_984, KL_ARG_V963_985, KL_ARG_V964_986):

    class KL_Context:
        KL_LOC_Result_987 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_987', tco_apply(kl_thaw, [KL_ARG_V964_986])), (KL_ARG_V962_984 if shen_eq(KL_CTX.KL_LOC_Result_987, False) else KL_CTX.KL_LOC_Result_987)][(-1)]
shen_add_fun('cut', kl_cut)

@tail_recursion
def shen_insert_modes(KL_ARG_V965_988):
    global symdic
    return (KL_ARG_V965_988 if (shen_consp(KL_ARG_V965_988) and (shen_eq(symdic.symdic_kl_mode, KL_ARG_V965_988[0]) and (shen_consp(KL_ARG_V965_988[1]) and (shen_consp(KL_ARG_V965_988[1][1]) and shen_eq([], KL_ARG_V965_988[1][1][1]))))) else ([] if shen_eq([], KL_ARG_V965_988) else ([[symdic.symdic_kl_mode, [KL_ARG_V965_988[0], [symdic.symdic_kl_x43, []]]], [symdic.symdic_kl_mode, [tco_apply(shen_insert_modes, [KL_ARG_V965_988[1]]), [symdic.symdic_kl_x45, []]]]] if shen_consp(KL_ARG_V965_988) else (KL_ARG_V965_988 if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.insert_modes', shen_insert_modes)

@tail_recursion
def shen_sx45prolog(KL_ARG_V966_989):
    global symdic
    return tail_call(kl_map, [(lambda KL_ARG_V892_990: tail_call(kl_eval, [KL_ARG_V892_990])), tco_apply(shen_prologx45x62shen, [KL_ARG_V966_989])])
shen_add_fun('shen.s-prolog', shen_sx45prolog)

@tail_recursion
def shen_prologx45x62shen(KL_ARG_V967_991):
    global symdic
    return tail_call(kl_map, [symdic.symdic_shen_compile_prolog_procedure, tco_apply(shen_group_clauses, [tco_apply(kl_map, [symdic.symdic_shen_sx45prolog_clause, tco_apply(kl_mapcan, [symdic.symdic_shen_head_abstraction, KL_ARG_V967_991])])])])
shen_add_fun('shen.prolog->shen', shen_prologx45x62shen)

@tail_recursion
def shen_sx45prolog_clause(KL_ARG_V968_992):
    global symdic
    return ([KL_ARG_V968_992[0], [symdic.symdic_kl_x58x45, [tco_apply(kl_map, [symdic.symdic_shen_sx45prolog_literal, KL_ARG_V968_992[1][1][0]]), []]]] if (shen_consp(KL_ARG_V968_992) and (shen_consp(KL_ARG_V968_992[1]) and (shen_eq(symdic.symdic_kl_x58x45, KL_ARG_V968_992[1][0]) and (shen_consp(KL_ARG_V968_992[1][1]) and shen_eq([], KL_ARG_V968_992[1][1][1]))))) else (tail_call(shen_sysx45error, [symdic.symdic_shen_sx45prolog_clause]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.s-prolog_clause', shen_sx45prolog_clause)

@tail_recursion
def shen_head_abstraction(KL_ARG_V969_993):

    class KL_Context:
        KL_LOC_Terms_994 = None
        KL_LOC_XTerms_996 = None
        KL_LOC_Literal_997 = None
        KL_LOC_Clause_998 = None
    KL_CTX = KL_Context()
    global symdic
    return ([KL_ARG_V969_993, []] if (shen_consp(KL_ARG_V969_993) and (shen_consp(KL_ARG_V969_993[1]) and (shen_eq(symdic.symdic_kl_x58x45, KL_ARG_V969_993[1][0]) and (shen_consp(KL_ARG_V969_993[1][1]) and (shen_eq([], KL_ARG_V969_993[1][1][1]) and (tco_apply(shen_complexity_head, [KL_ARG_V969_993[0]]) < shen_get(symdic.symdic_shen_x42maxcomplexityx42))))))) else ([setattr(KL_CTX, 'KL_LOC_Terms_994', tco_apply(kl_map, [(lambda KL_ARG_Y_995: tail_call(kl_gensym, [symdic.symdic_V])), KL_ARG_V969_993[0][1]])), [setattr(KL_CTX, 'KL_LOC_XTerms_996', tco_apply(shen_rcons_form, [tco_apply(shen_remove_modes, [KL_ARG_V969_993[0][1]])])), [setattr(KL_CTX, 'KL_LOC_Literal_997', [symdic.symdic_kl_unify, [tco_apply(shen_cons_form, [KL_CTX.KL_LOC_Terms_994]), [KL_CTX.KL_LOC_XTerms_996, []]]]), [setattr(KL_CTX, 'KL_LOC_Clause_998', [[KL_ARG_V969_993[0][0], KL_CTX.KL_LOC_Terms_994], [symdic.symdic_kl_x58x45, [[KL_CTX.KL_LOC_Literal_997, KL_ARG_V969_993[1][1][0]], []]]]), [KL_CTX.KL_LOC_Clause_998, []]][(-1)]][(-1)]][(-1)]][(-1)] if (shen_consp(KL_ARG_V969_993) and (shen_consp(KL_ARG_V969_993[0]) and (shen_consp(KL_ARG_V969_993[1]) and (shen_eq(symdic.symdic_kl_x58x45, KL_ARG_V969_993[1][0]) and (shen_consp(KL_ARG_V969_993[1][1]) and shen_eq([], KL_ARG_V969_993[1][1][1])))))) else (tail_call(shen_sysx45error, [symdic.symdic_shen_head_abstraction]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.head_abstraction', shen_head_abstraction)

@tail_recursion
def shen_complexity_head(KL_ARG_V974_999):
    global symdic
    return (tail_call(shen_product, [tco_apply(kl_map, [symdic.symdic_shen_complexity, KL_ARG_V974_999[1]])]) if shen_consp(KL_ARG_V974_999) else (tail_call(shen_sysx45error, [symdic.symdic_shen_complexity_head]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.complexity_head', shen_complexity_head)

@tail_recursion
def shen_complexity(KL_ARG_V982_1000):
    global symdic
    return (tail_call(shen_complexity, [KL_ARG_V982_1000[1][0]]) if (shen_consp(KL_ARG_V982_1000) and (shen_eq(symdic.symdic_kl_mode, KL_ARG_V982_1000[0]) and (shen_consp(KL_ARG_V982_1000[1]) and (shen_consp(KL_ARG_V982_1000[1][0]) and (shen_eq(symdic.symdic_kl_mode, KL_ARG_V982_1000[1][0][0]) and (shen_consp(KL_ARG_V982_1000[1][0][1]) and (shen_consp(KL_ARG_V982_1000[1][0][1][1]) and (shen_eq([], KL_ARG_V982_1000[1][0][1][1][1]) and (shen_consp(KL_ARG_V982_1000[1][1]) and shen_eq([], KL_ARG_V982_1000[1][1][1])))))))))) else ((2 * (tco_apply(shen_complexity, [[symdic.symdic_kl_mode, [KL_ARG_V982_1000[1][0][0], KL_ARG_V982_1000[1][1]]]]) * tco_apply(shen_complexity, [[symdic.symdic_kl_mode, [KL_ARG_V982_1000[1][0][1], KL_ARG_V982_1000[1][1]]]]))) if (shen_consp(KL_ARG_V982_1000) and (shen_eq(symdic.symdic_kl_mode, KL_ARG_V982_1000[0]) and (shen_consp(KL_ARG_V982_1000[1]) and (shen_consp(KL_ARG_V982_1000[1][0]) and (shen_consp(KL_ARG_V982_1000[1][1]) and (shen_eq(symdic.symdic_kl_x43, KL_ARG_V982_1000[1][1][0]) and shen_eq([], KL_ARG_V982_1000[1][1][1]))))))) else ((tco_apply(shen_complexity, [[symdic.symdic_kl_mode, [KL_ARG_V982_1000[1][0][0], KL_ARG_V982_1000[1][1]]]]) * tco_apply(shen_complexity, [[symdic.symdic_kl_mode, [KL_ARG_V982_1000[1][0][1], KL_ARG_V982_1000[1][1]]]])) if (shen_consp(KL_ARG_V982_1000) and (shen_eq(symdic.symdic_kl_mode, KL_ARG_V982_1000[0]) and (shen_consp(KL_ARG_V982_1000[1]) and (shen_consp(KL_ARG_V982_1000[1][0]) and (shen_consp(KL_ARG_V982_1000[1][1]) and (shen_eq(symdic.symdic_kl_x45, KL_ARG_V982_1000[1][1][0]) and shen_eq([], KL_ARG_V982_1000[1][1][1]))))))) else (1 if (shen_consp(KL_ARG_V982_1000) and (shen_eq(symdic.symdic_kl_mode, KL_ARG_V982_1000[0]) and (shen_consp(KL_ARG_V982_1000[1]) and (shen_consp(KL_ARG_V982_1000[1][1]) and (shen_eq([], KL_ARG_V982_1000[1][1][1]) and tco_apply(kl_variablex63, [KL_ARG_V982_1000[1][0]])))))) else (2 if (shen_consp(KL_ARG_V982_1000) and (shen_eq(symdic.symdic_kl_mode, KL_ARG_V982_1000[0]) and (shen_consp(KL_ARG_V982_1000[1]) and (shen_consp(KL_ARG_V982_1000[1][1]) and (shen_eq(symdic.symdic_kl_x43, KL_ARG_V982_1000[1][1][0]) and shen_eq([], KL_ARG_V982_1000[1][1][1])))))) else (1 if (shen_consp(KL_ARG_V982_1000) and (shen_eq(symdic.symdic_kl_mode, KL_ARG_V982_1000[0]) and (shen_consp(KL_ARG_V982_1000[1]) and (shen_consp(KL_ARG_V982_1000[1][1]) and (shen_eq(symdic.symdic_kl_x45, KL_ARG_V982_1000[1][1][0]) and shen_eq([], KL_ARG_V982_1000[1][1][1])))))) else (tail_call(shen_complexity, [[symdic.symdic_kl_mode, [KL_ARG_V982_1000, [symdic.symdic_kl_x43, []]]]]) if True else shen_simple_error('condition failure'))))))))
shen_add_fun('shen.complexity', shen_complexity)

@tail_recursion
def shen_product(KL_ARG_V983_1001):
    global symdic
    return (1 if shen_eq([], KL_ARG_V983_1001) else ((KL_ARG_V983_1001[0] * tco_apply(shen_product, [KL_ARG_V983_1001[1]])) if shen_consp(KL_ARG_V983_1001) else (tail_call(shen_sysx45error, [symdic.symdic_shen_product]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.product', shen_product)

@tail_recursion
def shen_sx45prolog_literal(KL_ARG_V984_1002):
    global symdic
    return ([symdic.symdic_kl_bind, [KL_ARG_V984_1002[1][0], [tco_apply(shen_insert_deref, [KL_ARG_V984_1002[1][1][0]]), []]]] if (shen_consp(KL_ARG_V984_1002) and (shen_eq(symdic.symdic_kl_is, KL_ARG_V984_1002[0]) and (shen_consp(KL_ARG_V984_1002[1]) and (shen_consp(KL_ARG_V984_1002[1][1]) and shen_eq([], KL_ARG_V984_1002[1][1][1]))))) else ([symdic.symdic_kl_fwhen, [tco_apply(shen_insert_deref, [KL_ARG_V984_1002[1][0]]), []]] if (shen_consp(KL_ARG_V984_1002) and (shen_eq(symdic.symdic_kl_when, KL_ARG_V984_1002[0]) and (shen_consp(KL_ARG_V984_1002[1]) and shen_eq([], KL_ARG_V984_1002[1][1])))) else ([symdic.symdic_kl_bind, [KL_ARG_V984_1002[1][0], [tco_apply(shen_insert_lazyderef, [KL_ARG_V984_1002[1][1][0]]), []]]] if (shen_consp(KL_ARG_V984_1002) and (shen_eq(symdic.symdic_kl_bind, KL_ARG_V984_1002[0]) and (shen_consp(KL_ARG_V984_1002[1]) and (shen_consp(KL_ARG_V984_1002[1][1]) and shen_eq([], KL_ARG_V984_1002[1][1][1]))))) else ([symdic.symdic_kl_fwhen, [tco_apply(shen_insert_lazyderef, [KL_ARG_V984_1002[1][0]]), []]] if (shen_consp(KL_ARG_V984_1002) and (shen_eq(symdic.symdic_kl_fwhen, KL_ARG_V984_1002[0]) and (shen_consp(KL_ARG_V984_1002[1]) and shen_eq([], KL_ARG_V984_1002[1][1])))) else ([tco_apply(shen_m_prolog_to_sx45prolog_predicate, [KL_ARG_V984_1002[0]]), KL_ARG_V984_1002[1]] if shen_consp(KL_ARG_V984_1002) else (tail_call(shen_sysx45error, [symdic.symdic_shen_sx45prolog_literal]) if True else shen_simple_error('condition failure')))))))
shen_add_fun('shen.s-prolog_literal', shen_sx45prolog_literal)

@tail_recursion
def shen_insert_deref(KL_ARG_V985_1003):
    global symdic
    return ([symdic.symdic_shen_deref, [KL_ARG_V985_1003, [symdic.symdic_ProcessN, []]]] if tco_apply(kl_variablex63, [KL_ARG_V985_1003]) else ([tco_apply(shen_insert_deref, [KL_ARG_V985_1003[0]]), tco_apply(shen_insert_deref, [KL_ARG_V985_1003[1]])] if shen_consp(KL_ARG_V985_1003) else (KL_ARG_V985_1003 if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.insert_deref', shen_insert_deref)

@tail_recursion
def shen_insert_lazyderef(KL_ARG_V986_1004):
    global symdic
    return ([symdic.symdic_shen_lazyderef, [KL_ARG_V986_1004, [symdic.symdic_ProcessN, []]]] if tco_apply(kl_variablex63, [KL_ARG_V986_1004]) else ([tco_apply(shen_insert_lazyderef, [KL_ARG_V986_1004[0]]), tco_apply(shen_insert_lazyderef, [KL_ARG_V986_1004[1]])] if shen_consp(KL_ARG_V986_1004) else (KL_ARG_V986_1004 if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.insert_lazyderef', shen_insert_lazyderef)

@tail_recursion
def shen_m_prolog_to_sx45prolog_predicate(KL_ARG_V987_1005):
    global symdic
    return (symdic.symdic_kl_unify if shen_eq(symdic.symdic_kl_x61, KL_ARG_V987_1005) else (symdic.symdic_kl_unifyx33 if shen_eq(symdic.symdic_kl_x61x33, KL_ARG_V987_1005) else (symdic.symdic_kl_identical if shen_eq(symdic.symdic_kl_x61x61, KL_ARG_V987_1005) else (KL_ARG_V987_1005 if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.m_prolog_to_s-prolog_predicate', shen_m_prolog_to_sx45prolog_predicate)

@tail_recursion
def shen_group_clauses(KL_ARG_V988_1006):

    class KL_Context:
        KL_LOC_Group_1007 = None
        KL_LOC_Rest_1009 = None
    KL_CTX = KL_Context()
    global symdic
    return ([] if shen_eq([], KL_ARG_V988_1006) else ([setattr(KL_CTX, 'KL_LOC_Group_1007', tco_apply(shen_collect, [(lambda KL_ARG_X_1008: tail_call(shen_same_predicatex63, [KL_ARG_V988_1006[0], KL_ARG_X_1008])), KL_ARG_V988_1006])), [setattr(KL_CTX, 'KL_LOC_Rest_1009', tco_apply(kl_difference, [KL_ARG_V988_1006, KL_CTX.KL_LOC_Group_1007])), [KL_CTX.KL_LOC_Group_1007, tco_apply(shen_group_clauses, [KL_CTX.KL_LOC_Rest_1009])]][(-1)]][(-1)] if shen_consp(KL_ARG_V988_1006) else (tail_call(shen_sysx45error, [symdic.symdic_shen_group_clauses]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.group_clauses', shen_group_clauses)

@tail_recursion
def shen_collect(KL_ARG_V991_1010, KL_ARG_V992_1011):
    global symdic
    return ([] if shen_eq([], KL_ARG_V992_1011) else (([KL_ARG_V992_1011[0], tco_apply(shen_collect, [KL_ARG_V991_1010, KL_ARG_V992_1011[1]])] if shen_apply(KL_ARG_V991_1010, [KL_ARG_V992_1011[0]]) else tail_call(shen_collect, [KL_ARG_V991_1010, KL_ARG_V992_1011[1]])) if shen_consp(KL_ARG_V992_1011) else (tail_call(shen_sysx45error, [symdic.symdic_shen_collect]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.collect', shen_collect)

@tail_recursion
def shen_same_predicatex63(KL_ARG_V1009_1012, KL_ARG_V1010_1013):
    global symdic
    return (shen_eq(KL_ARG_V1009_1012[0][0], KL_ARG_V1010_1013[0][0]) if (shen_consp(KL_ARG_V1009_1012) and (shen_consp(KL_ARG_V1009_1012[0]) and (shen_consp(KL_ARG_V1010_1013) and shen_consp(KL_ARG_V1010_1013[0])))) else (tail_call(shen_sysx45error, [symdic.symdic_shen_same_predicatex63]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.same_predicate?', shen_same_predicatex63)

@tail_recursion
def shen_compile_prolog_procedure(KL_ARG_V1011_1014):

    class KL_Context:
        KL_LOC_F_1015 = None
        KL_LOC_Shen_1016 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_F_1015', tco_apply(shen_procedure_name, [KL_ARG_V1011_1014])), [setattr(KL_CTX, 'KL_LOC_Shen_1016', tco_apply(shen_clausesx45tox45shen, [KL_CTX.KL_LOC_F_1015, KL_ARG_V1011_1014])), KL_CTX.KL_LOC_Shen_1016][(-1)]][(-1)]
shen_add_fun('shen.compile_prolog_procedure', shen_compile_prolog_procedure)

@tail_recursion
def shen_procedure_name(KL_ARG_V1024_1017):
    global symdic
    return (KL_ARG_V1024_1017[0][0][0] if (shen_consp(KL_ARG_V1024_1017) and (shen_consp(KL_ARG_V1024_1017[0]) and shen_consp(KL_ARG_V1024_1017[0][0]))) else (tail_call(shen_sysx45error, [symdic.symdic_shen_procedure_name]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.procedure_name', shen_procedure_name)

@tail_recursion
def shen_clausesx45tox45shen(KL_ARG_V1025_1018, KL_ARG_V1026_1019):

    class KL_Context:
        KL_LOC_Linear_1020 = None
        KL_LOC_Arity_1021 = None
        KL_LOC_Parameters_1023 = None
        KL_LOC_AUM_instructions_1024 = None
        KL_LOC_Code_1026 = None
        KL_LOC_ShenDef_1027 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Linear_1020', tco_apply(kl_map, [symdic.symdic_shen_linearisex45clause, KL_ARG_V1026_1019])), [setattr(KL_CTX, 'KL_LOC_Arity_1021', tco_apply(shen_prologx45aritycheck, [KL_ARG_V1025_1018, tco_apply(kl_map, [(lambda KL_ARG_V893_1022: tail_call(kl_head, [KL_ARG_V893_1022])), KL_ARG_V1026_1019])])), [setattr(KL_CTX, 'KL_LOC_Parameters_1023', tco_apply(shen_parameters, [KL_CTX.KL_LOC_Arity_1021])), [setattr(KL_CTX, 'KL_LOC_AUM_instructions_1024', tco_apply(kl_map, [(lambda KL_ARG_X_1025: tail_call(shen_aum, [KL_ARG_X_1025, KL_CTX.KL_LOC_Parameters_1023])), KL_CTX.KL_LOC_Linear_1020])), [setattr(KL_CTX, 'KL_LOC_Code_1026', tco_apply(shen_catchx45cut, [tco_apply(shen_nestx45disjunct, [tco_apply(kl_map, [symdic.symdic_shen_aum_to_shen, KL_CTX.KL_LOC_AUM_instructions_1024])])])), [setattr(KL_CTX, 'KL_LOC_ShenDef_1027', [symdic.symdic_kl_define, [KL_ARG_V1025_1018, tco_apply(kl_append, [KL_CTX.KL_LOC_Parameters_1023, tco_apply(kl_append, [[symdic.symdic_ProcessN, [symdic.symdic_Continuation, []]], [symdic.symdic_kl_x45x62, [KL_CTX.KL_LOC_Code_1026, []]]])])]]), KL_CTX.KL_LOC_ShenDef_1027][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]
shen_add_fun('shen.clauses-to-shen', shen_clausesx45tox45shen)

@tail_recursion
def shen_catchx45cut(KL_ARG_V1027_1028):
    global symdic
    return (KL_ARG_V1027_1028 if (not tco_apply(shen_occursx63, [symdic.symdic_kl_cut, KL_ARG_V1027_1028])) else ([symdic.symdic_kl_let, [symdic.symdic_Throwcontrol, [[symdic.symdic_shen_catchpoint, []], [[symdic.symdic_shen_cutpoint, [symdic.symdic_Throwcontrol, [KL_ARG_V1027_1028, []]]], []]]]] if True else shen_simple_error('condition failure')))
shen_add_fun('shen.catch-cut', shen_catchx45cut)

@tail_recursion
def shen_catchpoint():
    global symdic
    return shen_set(symdic.symdic_shen_x42catchx42, (1 + shen_get(symdic.symdic_shen_x42catchx42)))
shen_add_fun('shen.catchpoint', shen_catchpoint)

@tail_recursion
def shen_cutpoint(KL_ARG_V1032_1029, KL_ARG_V1033_1030):
    global symdic
    return (False if shen_eq(KL_ARG_V1033_1030, KL_ARG_V1032_1029) else (KL_ARG_V1033_1030 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.cutpoint', shen_cutpoint)

@tail_recursion
def shen_nestx45disjunct(KL_ARG_V1035_1031):
    global symdic
    return (KL_ARG_V1035_1031[0] if (shen_consp(KL_ARG_V1035_1031) and shen_eq([], KL_ARG_V1035_1031[1])) else (tail_call(shen_lispx45or, [KL_ARG_V1035_1031[0], tco_apply(shen_nestx45disjunct, [KL_ARG_V1035_1031[1]])]) if shen_consp(KL_ARG_V1035_1031) else (tail_call(shen_sysx45error, [symdic.symdic_shen_nestx45disjunct]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.nest-disjunct', shen_nestx45disjunct)

@tail_recursion
def shen_lispx45or(KL_ARG_V1036_1032, KL_ARG_V1037_1033):
    global symdic
    return [symdic.symdic_kl_let, [symdic.symdic_Case, [KL_ARG_V1036_1032, [[symdic.symdic_kl_if, [[symdic.symdic_kl_x61, [symdic.symdic_Case, [False, []]]], [KL_ARG_V1037_1033, [symdic.symdic_Case, []]]]], []]]]]
shen_add_fun('shen.lisp-or', shen_lispx45or)

@tail_recursion
def shen_prologx45aritycheck(KL_ARG_V1040_1034, KL_ARG_V1041_1035):
    global symdic
    return ((tco_apply(kl_length, [KL_ARG_V1041_1035[0]]) - 1) if (shen_consp(KL_ARG_V1041_1035) and shen_eq([], KL_ARG_V1041_1035[1])) else ((tail_call(shen_prologx45aritycheck, [KL_ARG_V1040_1034, KL_ARG_V1041_1035[1]]) if shen_eq(tco_apply(kl_length, [KL_ARG_V1041_1035[0]]), tco_apply(kl_length, [KL_ARG_V1041_1035[1][0]])) else shen_simple_error(('arity error in prolog procedure ' + tco_apply(shen_app, [[KL_ARG_V1040_1034, []], '\r\n', symdic.symdic_shen_a])))) if (shen_consp(KL_ARG_V1041_1035) and shen_consp(KL_ARG_V1041_1035[1])) else (tail_call(shen_sysx45error, [symdic.symdic_shen_prologx45aritycheck]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.prolog-aritycheck', shen_prologx45aritycheck)

@tail_recursion
def shen_linearisex45clause(KL_ARG_V1042_1036):

    class KL_Context:
        KL_LOC_Linear_1037 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_Linear_1037', tco_apply(shen_linearise, [[KL_ARG_V1042_1036[0], KL_ARG_V1042_1036[1][1]]])), tail_call(shen_clause_form, [KL_CTX.KL_LOC_Linear_1037])][(-1)] if (shen_consp(KL_ARG_V1042_1036) and (shen_consp(KL_ARG_V1042_1036[1]) and (shen_eq(symdic.symdic_kl_x58x45, KL_ARG_V1042_1036[1][0]) and (shen_consp(KL_ARG_V1042_1036[1][1]) and shen_eq([], KL_ARG_V1042_1036[1][1][1]))))) else (tail_call(shen_sysx45error, [symdic.symdic_shen_linearisex45clause]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.linearise-clause', shen_linearisex45clause)

@tail_recursion
def shen_clause_form(KL_ARG_V1043_1038):
    global symdic
    return ([tco_apply(shen_explicit_modes, [KL_ARG_V1043_1038[0]]), [symdic.symdic_kl_x58x45, [tco_apply(shen_cf_help, [KL_ARG_V1043_1038[1][0]]), []]]] if (shen_consp(KL_ARG_V1043_1038) and (shen_consp(KL_ARG_V1043_1038[1]) and shen_eq([], KL_ARG_V1043_1038[1][1]))) else (tail_call(shen_sysx45error, [symdic.symdic_shen_clause_form]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.clause_form', shen_clause_form)

@tail_recursion
def shen_explicit_modes(KL_ARG_V1044_1039):
    global symdic
    return ([KL_ARG_V1044_1039[0], tco_apply(kl_map, [symdic.symdic_shen_em_help, KL_ARG_V1044_1039[1]])] if shen_consp(KL_ARG_V1044_1039) else (tail_call(shen_sysx45error, [symdic.symdic_shen_explicit_modes]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.explicit_modes', shen_explicit_modes)

@tail_recursion
def shen_em_help(KL_ARG_V1045_1040):
    global symdic
    return (KL_ARG_V1045_1040 if (shen_consp(KL_ARG_V1045_1040) and (shen_eq(symdic.symdic_kl_mode, KL_ARG_V1045_1040[0]) and (shen_consp(KL_ARG_V1045_1040[1]) and (shen_consp(KL_ARG_V1045_1040[1][1]) and shen_eq([], KL_ARG_V1045_1040[1][1][1]))))) else ([symdic.symdic_kl_mode, [KL_ARG_V1045_1040, [symdic.symdic_kl_x43, []]]] if True else shen_simple_error('condition failure')))
shen_add_fun('shen.em_help', shen_em_help)

@tail_recursion
def shen_cf_help(KL_ARG_V1046_1041):
    global symdic
    return ([[(symdic.symdic_kl_unifyx33 if shen_get(symdic.symdic_shen_x42occursx42) else symdic.symdic_kl_unify), KL_ARG_V1046_1041[1][0][1]], tco_apply(shen_cf_help, [KL_ARG_V1046_1041[1][1][0]])] if (shen_consp(KL_ARG_V1046_1041) and (shen_eq(symdic.symdic_kl_where, KL_ARG_V1046_1041[0]) and (shen_consp(KL_ARG_V1046_1041[1]) and (shen_consp(KL_ARG_V1046_1041[1][0]) and (shen_eq(symdic.symdic_kl_x61, KL_ARG_V1046_1041[1][0][0]) and (shen_consp(KL_ARG_V1046_1041[1][0][1]) and (shen_consp(KL_ARG_V1046_1041[1][0][1][1]) and (shen_eq([], KL_ARG_V1046_1041[1][0][1][1][1]) and (shen_consp(KL_ARG_V1046_1041[1][1]) and shen_eq([], KL_ARG_V1046_1041[1][1][1])))))))))) else (KL_ARG_V1046_1041 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.cf_help', shen_cf_help)

@tail_recursion
def kl_occursx45check(KL_ARG_V1051_1042):
    global symdic
    return (shen_set(symdic.symdic_shen_x42occursx42, True) if shen_eq(symdic.symdic_kl_x43, KL_ARG_V1051_1042) else (shen_set(symdic.symdic_shen_x42occursx42, False) if shen_eq(symdic.symdic_kl_x45, KL_ARG_V1051_1042) else (shen_simple_error('occurs-check expects + or -\r\n') if True else shen_simple_error('condition failure'))))
shen_add_fun('occurs-check', kl_occursx45check)

@tail_recursion
def shen_aum(KL_ARG_V1052_1043, KL_ARG_V1053_1044):

    class KL_Context:
        KL_LOC_MuApplication_1045 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_MuApplication_1045', tco_apply(shen_make_mu_application, [[symdic.symdic_shen_mu, [KL_ARG_V1052_1043[0][1], [tco_apply(shen_continuation_call, [KL_ARG_V1052_1043[0][1], KL_ARG_V1052_1043[1][1][0]]), []]]], KL_ARG_V1053_1044])), tail_call(shen_mu_reduction, [KL_CTX.KL_LOC_MuApplication_1045, symdic.symdic_kl_x43])][(-1)] if (shen_consp(KL_ARG_V1052_1043) and (shen_consp(KL_ARG_V1052_1043[0]) and (shen_consp(KL_ARG_V1052_1043[1]) and (shen_eq(symdic.symdic_kl_x58x45, KL_ARG_V1052_1043[1][0]) and (shen_consp(KL_ARG_V1052_1043[1][1]) and shen_eq([], KL_ARG_V1052_1043[1][1][1])))))) else (tail_call(shen_sysx45error, [symdic.symdic_shen_aum]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.aum', shen_aum)

@tail_recursion
def shen_continuation_call(KL_ARG_V1054_1046, KL_ARG_V1055_1047):

    class KL_Context:
        KL_LOC_VTerms_1048 = None
        KL_LOC_VBody_1049 = None
        KL_LOC_Free_1050 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_VTerms_1048', [symdic.symdic_ProcessN, tco_apply(shen_extract_vars, [KL_ARG_V1054_1046])]), [setattr(KL_CTX, 'KL_LOC_VBody_1049', tco_apply(shen_extract_vars, [KL_ARG_V1055_1047])), [setattr(KL_CTX, 'KL_LOC_Free_1050', tco_apply(kl_remove, [symdic.symdic_Throwcontrol, tco_apply(kl_difference, [KL_CTX.KL_LOC_VBody_1049, KL_CTX.KL_LOC_VTerms_1048])])), tail_call(shen_cc_help, [KL_CTX.KL_LOC_Free_1050, KL_ARG_V1055_1047])][(-1)]][(-1)]][(-1)]
shen_add_fun('shen.continuation_call', shen_continuation_call)

@tail_recursion
def kl_remove(KL_ARG_V1056_1051, KL_ARG_V1057_1052):
    global symdic
    return tail_call(shen_removex45h, [KL_ARG_V1056_1051, KL_ARG_V1057_1052, []])
shen_add_fun('remove', kl_remove)

@tail_recursion
def shen_removex45h(KL_ARG_V1060_1053, KL_ARG_V1061_1054, KL_ARG_V1062_1055):
    global symdic
    return (tail_call(kl_reverse, [KL_ARG_V1062_1055]) if shen_eq([], KL_ARG_V1061_1054) else (tail_call(shen_removex45h, [KL_ARG_V1061_1054[0], KL_ARG_V1061_1054[1], KL_ARG_V1062_1055]) if (shen_consp(KL_ARG_V1061_1054) and shen_eq(KL_ARG_V1061_1054[0], KL_ARG_V1060_1053)) else (tail_call(shen_removex45h, [KL_ARG_V1060_1053, KL_ARG_V1061_1054[1], [KL_ARG_V1061_1054[0], KL_ARG_V1062_1055]]) if shen_consp(KL_ARG_V1061_1054) else (tail_call(shen_sysx45error, [symdic.symdic_shen_removex45h]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.remove-h', shen_removex45h)

@tail_recursion
def shen_cc_help(KL_ARG_V1064_1056, KL_ARG_V1065_1057):
    global symdic
    return ([symdic.symdic_shen_pop, [symdic.symdic_shen_the, [symdic.symdic_shen_stack, []]]] if (shen_eq([], KL_ARG_V1064_1056) and shen_eq([], KL_ARG_V1065_1057)) else ([symdic.symdic_shen_rename, [symdic.symdic_shen_the, [symdic.symdic_shen_variables, [symdic.symdic_kl_in, [KL_ARG_V1064_1056, [symdic.symdic_kl_and, [symdic.symdic_shen_then, [[symdic.symdic_shen_pop, [symdic.symdic_shen_the, [symdic.symdic_shen_stack, []]]], []]]]]]]]] if shen_eq([], KL_ARG_V1065_1057) else ([symdic.symdic_kl_call, [symdic.symdic_shen_the, [symdic.symdic_shen_continuation, [KL_ARG_V1065_1057, []]]]] if shen_eq([], KL_ARG_V1064_1056) else ([symdic.symdic_shen_rename, [symdic.symdic_shen_the, [symdic.symdic_shen_variables, [symdic.symdic_kl_in, [KL_ARG_V1064_1056, [symdic.symdic_kl_and, [symdic.symdic_shen_then, [[symdic.symdic_kl_call, [symdic.symdic_shen_the, [symdic.symdic_shen_continuation, [KL_ARG_V1065_1057, []]]]], []]]]]]]]] if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.cc_help', shen_cc_help)

@tail_recursion
def shen_make_mu_application(KL_ARG_V1066_1058, KL_ARG_V1067_1059):
    global symdic
    return (KL_ARG_V1066_1058[1][1][0] if (shen_consp(KL_ARG_V1066_1058) and (shen_eq(symdic.symdic_shen_mu, KL_ARG_V1066_1058[0]) and (shen_consp(KL_ARG_V1066_1058[1]) and (shen_eq([], KL_ARG_V1066_1058[1][0]) and (shen_consp(KL_ARG_V1066_1058[1][1]) and (shen_eq([], KL_ARG_V1066_1058[1][1][1]) and shen_eq([], KL_ARG_V1067_1059))))))) else ([[symdic.symdic_shen_mu, [KL_ARG_V1066_1058[1][0][0], [tco_apply(shen_make_mu_application, [[symdic.symdic_shen_mu, [KL_ARG_V1066_1058[1][0][1], KL_ARG_V1066_1058[1][1]]], KL_ARG_V1067_1059[1]]), []]]], [KL_ARG_V1067_1059[0], []]] if (shen_consp(KL_ARG_V1066_1058) and (shen_eq(symdic.symdic_shen_mu, KL_ARG_V1066_1058[0]) and (shen_consp(KL_ARG_V1066_1058[1]) and (shen_consp(KL_ARG_V1066_1058[1][0]) and (shen_consp(KL_ARG_V1066_1058[1][1]) and (shen_eq([], KL_ARG_V1066_1058[1][1][1]) and shen_consp(KL_ARG_V1067_1059))))))) else (tail_call(shen_sysx45error, [symdic.symdic_shen_make_mu_application]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.make_mu_application', shen_make_mu_application)

@tail_recursion
def shen_mu_reduction(KL_ARG_V1074_1060, KL_ARG_V1075_1061):

    class KL_Context:
        KL_LOC_Z_1062 = None
        KL_LOC_Z_1063 = None
        KL_LOC_Z_1064 = None
        KL_LOC_Z_1065 = None
    KL_CTX = KL_Context()
    global symdic
    return (tail_call(shen_mu_reduction, [[[symdic.symdic_shen_mu, [KL_ARG_V1074_1060[0][1][0][1][0], KL_ARG_V1074_1060[0][1][1]]], KL_ARG_V1074_1060[1]], KL_ARG_V1074_1060[0][1][0][1][1][0]]) if (shen_consp(KL_ARG_V1074_1060) and (shen_consp(KL_ARG_V1074_1060[0]) and (shen_eq(symdic.symdic_shen_mu, KL_ARG_V1074_1060[0][0]) and (shen_consp(KL_ARG_V1074_1060[0][1]) and (shen_consp(KL_ARG_V1074_1060[0][1][0]) and (shen_eq(symdic.symdic_kl_mode, KL_ARG_V1074_1060[0][1][0][0]) and (shen_consp(KL_ARG_V1074_1060[0][1][0][1]) and (shen_consp(KL_ARG_V1074_1060[0][1][0][1][1]) and (shen_eq([], KL_ARG_V1074_1060[0][1][0][1][1][1]) and (shen_consp(KL_ARG_V1074_1060[0][1][1]) and (shen_eq([], KL_ARG_V1074_1060[0][1][1][1]) and (shen_consp(KL_ARG_V1074_1060[1]) and shen_eq([], KL_ARG_V1074_1060[1][1]))))))))))))) else (tail_call(shen_mu_reduction, [KL_ARG_V1074_1060[0][1][1][0], KL_ARG_V1075_1061]) if (shen_consp(KL_ARG_V1074_1060) and (shen_consp(KL_ARG_V1074_1060[0]) and (shen_eq(symdic.symdic_shen_mu, KL_ARG_V1074_1060[0][0]) and (shen_consp(KL_ARG_V1074_1060[0][1]) and (shen_consp(KL_ARG_V1074_1060[0][1][1]) and (shen_eq([], KL_ARG_V1074_1060[0][1][1][1]) and (shen_consp(KL_ARG_V1074_1060[1]) and (shen_eq([], KL_ARG_V1074_1060[1][1]) and shen_eq(symdic.symdic_kl__, KL_ARG_V1074_1060[0][1][0]))))))))) else (tail_call(kl_subst, [KL_ARG_V1074_1060[1][0], KL_ARG_V1074_1060[0][1][0], tco_apply(shen_mu_reduction, [KL_ARG_V1074_1060[0][1][1][0], KL_ARG_V1075_1061])]) if (shen_consp(KL_ARG_V1074_1060) and (shen_consp(KL_ARG_V1074_1060[0]) and (shen_eq(symdic.symdic_shen_mu, KL_ARG_V1074_1060[0][0]) and (shen_consp(KL_ARG_V1074_1060[0][1]) and (shen_consp(KL_ARG_V1074_1060[0][1][1]) and (shen_eq([], KL_ARG_V1074_1060[0][1][1][1]) and (shen_consp(KL_ARG_V1074_1060[1]) and (shen_eq([], KL_ARG_V1074_1060[1][1]) and tco_apply(shen_ephemeral_variablex63, [KL_ARG_V1074_1060[0][1][0], KL_ARG_V1074_1060[1][0]]))))))))) else ([symdic.symdic_kl_let, [KL_ARG_V1074_1060[0][1][0], [symdic.symdic_shen_be, [KL_ARG_V1074_1060[1][0], [symdic.symdic_kl_in, [tco_apply(shen_mu_reduction, [KL_ARG_V1074_1060[0][1][1][0], KL_ARG_V1075_1061]), []]]]]]] if (shen_consp(KL_ARG_V1074_1060) and (shen_consp(KL_ARG_V1074_1060[0]) and (shen_eq(symdic.symdic_shen_mu, KL_ARG_V1074_1060[0][0]) and (shen_consp(KL_ARG_V1074_1060[0][1]) and (shen_consp(KL_ARG_V1074_1060[0][1][1]) and (shen_eq([], KL_ARG_V1074_1060[0][1][1][1]) and (shen_consp(KL_ARG_V1074_1060[1]) and (shen_eq([], KL_ARG_V1074_1060[1][1]) and tco_apply(kl_variablex63, [KL_ARG_V1074_1060[0][1][0]]))))))))) else ([setattr(KL_CTX, 'KL_LOC_Z_1062', tco_apply(kl_gensym, [symdic.symdic_V])), [symdic.symdic_kl_let, [KL_CTX.KL_LOC_Z_1062, [symdic.symdic_shen_be, [[symdic.symdic_shen_the, [symdic.symdic_shen_result, [symdic.symdic_shen_of, [symdic.symdic_shen_dereferencing, KL_ARG_V1074_1060[1]]]]], [symdic.symdic_kl_in, [[symdic.symdic_kl_if, [[KL_CTX.KL_LOC_Z_1062, [symdic.symdic_kl_is, [symdic.symdic_kl_identical, [symdic.symdic_shen_to, [KL_ARG_V1074_1060[0][1][0], []]]]]], [symdic.symdic_shen_then, [tco_apply(shen_mu_reduction, [KL_ARG_V1074_1060[0][1][1][0], symdic.symdic_kl_x45]), [symdic.symdic_shen_else, [symdic.symdic_shen_failedx33, []]]]]]], []]]]]]]][(-1)] if (shen_consp(KL_ARG_V1074_1060) and (shen_consp(KL_ARG_V1074_1060[0]) and (shen_eq(symdic.symdic_shen_mu, KL_ARG_V1074_1060[0][0]) and (shen_consp(KL_ARG_V1074_1060[0][1]) and (shen_consp(KL_ARG_V1074_1060[0][1][1]) and (shen_eq([], KL_ARG_V1074_1060[0][1][1][1]) and (shen_consp(KL_ARG_V1074_1060[1]) and (shen_eq([], KL_ARG_V1074_1060[1][1]) and (shen_eq(symdic.symdic_kl_x45, KL_ARG_V1075_1061) and tco_apply(shen_prolog_constantx63, [KL_ARG_V1074_1060[0][1][0]])))))))))) else ([setattr(KL_CTX, 'KL_LOC_Z_1063', tco_apply(kl_gensym, [symdic.symdic_V])), [symdic.symdic_kl_let, [KL_CTX.KL_LOC_Z_1063, [symdic.symdic_shen_be, [[symdic.symdic_shen_the, [symdic.symdic_shen_result, [symdic.symdic_shen_of, [symdic.symdic_shen_dereferencing, KL_ARG_V1074_1060[1]]]]], [symdic.symdic_kl_in, [[symdic.symdic_kl_if, [[KL_CTX.KL_LOC_Z_1063, [symdic.symdic_kl_is, [symdic.symdic_kl_identical, [symdic.symdic_shen_to, [KL_ARG_V1074_1060[0][1][0], []]]]]], [symdic.symdic_shen_then, [tco_apply(shen_mu_reduction, [KL_ARG_V1074_1060[0][1][1][0], symdic.symdic_kl_x43]), [symdic.symdic_shen_else, [[symdic.symdic_kl_if, [[KL_CTX.KL_LOC_Z_1063, [symdic.symdic_kl_is, [symdic.symdic_shen_a, [symdic.symdic_shen_variable, []]]]], [symdic.symdic_shen_then, [[symdic.symdic_kl_bind, [KL_CTX.KL_LOC_Z_1063, [symdic.symdic_shen_to, [KL_ARG_V1074_1060[0][1][0], [symdic.symdic_kl_in, [tco_apply(shen_mu_reduction, [KL_ARG_V1074_1060[0][1][1][0], symdic.symdic_kl_x43]), []]]]]]], [symdic.symdic_shen_else, [symdic.symdic_shen_failedx33, []]]]]]], []]]]]]], []]]]]]]][(-1)] if (shen_consp(KL_ARG_V1074_1060) and (shen_consp(KL_ARG_V1074_1060[0]) and (shen_eq(symdic.symdic_shen_mu, KL_ARG_V1074_1060[0][0]) and (shen_consp(KL_ARG_V1074_1060[0][1]) and (shen_consp(KL_ARG_V1074_1060[0][1][1]) and (shen_eq([], KL_ARG_V1074_1060[0][1][1][1]) and (shen_consp(KL_ARG_V1074_1060[1]) and (shen_eq([], KL_ARG_V1074_1060[1][1]) and (shen_eq(symdic.symdic_kl_x43, KL_ARG_V1075_1061) and tco_apply(shen_prolog_constantx63, [KL_ARG_V1074_1060[0][1][0]])))))))))) else ([setattr(KL_CTX, 'KL_LOC_Z_1064', tco_apply(kl_gensym, [symdic.symdic_V])), [symdic.symdic_kl_let, [KL_CTX.KL_LOC_Z_1064, [symdic.symdic_shen_be, [[symdic.symdic_shen_the, [symdic.symdic_shen_result, [symdic.symdic_shen_of, [symdic.symdic_shen_dereferencing, KL_ARG_V1074_1060[1]]]]], [symdic.symdic_kl_in, [[symdic.symdic_kl_if, [[KL_CTX.KL_LOC_Z_1064, [symdic.symdic_kl_is, [symdic.symdic_shen_a, [symdic.symdic_shen_nonx45empty, [symdic.symdic_kl_list, []]]]]], [symdic.symdic_shen_then, [tco_apply(shen_mu_reduction, [[[symdic.symdic_shen_mu, [KL_ARG_V1074_1060[0][1][0][0], [[[symdic.symdic_shen_mu, [KL_ARG_V1074_1060[0][1][0][1], KL_ARG_V1074_1060[0][1][1]]], [[symdic.symdic_shen_the, [symdic.symdic_kl_tail, [symdic.symdic_shen_of, [KL_CTX.KL_LOC_Z_1064, []]]]], []]], []]]], [[symdic.symdic_shen_the, [symdic.symdic_kl_head, [symdic.symdic_shen_of, [KL_CTX.KL_LOC_Z_1064, []]]]], []]], symdic.symdic_kl_x45]), [symdic.symdic_shen_else, [symdic.symdic_shen_failedx33, []]]]]]], []]]]]]]][(-1)] if (shen_consp(KL_ARG_V1074_1060) and (shen_consp(KL_ARG_V1074_1060[0]) and (shen_eq(symdic.symdic_shen_mu, KL_ARG_V1074_1060[0][0]) and (shen_consp(KL_ARG_V1074_1060[0][1]) and (shen_consp(KL_ARG_V1074_1060[0][1][0]) and (shen_consp(KL_ARG_V1074_1060[0][1][1]) and (shen_eq([], KL_ARG_V1074_1060[0][1][1][1]) and (shen_consp(KL_ARG_V1074_1060[1]) and (shen_eq([], KL_ARG_V1074_1060[1][1]) and shen_eq(symdic.symdic_kl_x45, KL_ARG_V1075_1061)))))))))) else ([setattr(KL_CTX, 'KL_LOC_Z_1065', tco_apply(kl_gensym, [symdic.symdic_V])), [symdic.symdic_kl_let, [KL_CTX.KL_LOC_Z_1065, [symdic.symdic_shen_be, [[symdic.symdic_shen_the, [symdic.symdic_shen_result, [symdic.symdic_shen_of, [symdic.symdic_shen_dereferencing, KL_ARG_V1074_1060[1]]]]], [symdic.symdic_kl_in, [[symdic.symdic_kl_if, [[KL_CTX.KL_LOC_Z_1065, [symdic.symdic_kl_is, [symdic.symdic_shen_a, [symdic.symdic_shen_nonx45empty, [symdic.symdic_kl_list, []]]]]], [symdic.symdic_shen_then, [tco_apply(shen_mu_reduction, [[[symdic.symdic_shen_mu, [KL_ARG_V1074_1060[0][1][0][0], [[[symdic.symdic_shen_mu, [KL_ARG_V1074_1060[0][1][0][1], KL_ARG_V1074_1060[0][1][1]]], [[symdic.symdic_shen_the, [symdic.symdic_kl_tail, [symdic.symdic_shen_of, [KL_CTX.KL_LOC_Z_1065, []]]]], []]], []]]], [[symdic.symdic_shen_the, [symdic.symdic_kl_head, [symdic.symdic_shen_of, [KL_CTX.KL_LOC_Z_1065, []]]]], []]], symdic.symdic_kl_x43]), [symdic.symdic_shen_else, [[symdic.symdic_kl_if, [[KL_CTX.KL_LOC_Z_1065, [symdic.symdic_kl_is, [symdic.symdic_shen_a, [symdic.symdic_shen_variable, []]]]], [symdic.symdic_shen_then, [[symdic.symdic_shen_rename, [symdic.symdic_shen_the, [symdic.symdic_shen_variables, [symdic.symdic_kl_in, [tco_apply(shen_extract_vars, [KL_ARG_V1074_1060[0][1][0]]), [symdic.symdic_kl_and, [symdic.symdic_shen_then, [[symdic.symdic_kl_bind, [KL_CTX.KL_LOC_Z_1065, [symdic.symdic_shen_to, [tco_apply(shen_rcons_form, [tco_apply(shen_remove_modes, [KL_ARG_V1074_1060[0][1][0]])]), [symdic.symdic_kl_in, [tco_apply(shen_mu_reduction, [KL_ARG_V1074_1060[0][1][1][0], symdic.symdic_kl_x43]), []]]]]]], []]]]]]]]], [symdic.symdic_shen_else, [symdic.symdic_shen_failedx33, []]]]]]], []]]]]]], []]]]]]]][(-1)] if (shen_consp(KL_ARG_V1074_1060) and (shen_consp(KL_ARG_V1074_1060[0]) and (shen_eq(symdic.symdic_shen_mu, KL_ARG_V1074_1060[0][0]) and (shen_consp(KL_ARG_V1074_1060[0][1]) and (shen_consp(KL_ARG_V1074_1060[0][1][0]) and (shen_consp(KL_ARG_V1074_1060[0][1][1]) and (shen_eq([], KL_ARG_V1074_1060[0][1][1][1]) and (shen_consp(KL_ARG_V1074_1060[1]) and (shen_eq([], KL_ARG_V1074_1060[1][1]) and shen_eq(symdic.symdic_kl_x43, KL_ARG_V1075_1061)))))))))) else (KL_ARG_V1074_1060 if True else shen_simple_error('condition failure'))))))))))
shen_add_fun('shen.mu_reduction', shen_mu_reduction)

@tail_recursion
def shen_rcons_form(KL_ARG_V1076_1066):
    global symdic
    return ([symdic.symdic_kl_cons, [tco_apply(shen_rcons_form, [KL_ARG_V1076_1066[0]]), [tco_apply(shen_rcons_form, [KL_ARG_V1076_1066[1]]), []]]] if shen_consp(KL_ARG_V1076_1066) else (KL_ARG_V1076_1066 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.rcons_form', shen_rcons_form)

@tail_recursion
def shen_remove_modes(KL_ARG_V1077_1067):
    global symdic
    return (tail_call(shen_remove_modes, [KL_ARG_V1077_1067[1][0]]) if (shen_consp(KL_ARG_V1077_1067) and (shen_eq(symdic.symdic_kl_mode, KL_ARG_V1077_1067[0]) and (shen_consp(KL_ARG_V1077_1067[1]) and (shen_consp(KL_ARG_V1077_1067[1][1]) and (shen_eq(symdic.symdic_kl_x43, KL_ARG_V1077_1067[1][1][0]) and shen_eq([], KL_ARG_V1077_1067[1][1][1])))))) else (tail_call(shen_remove_modes, [KL_ARG_V1077_1067[1][0]]) if (shen_consp(KL_ARG_V1077_1067) and (shen_eq(symdic.symdic_kl_mode, KL_ARG_V1077_1067[0]) and (shen_consp(KL_ARG_V1077_1067[1]) and (shen_consp(KL_ARG_V1077_1067[1][1]) and (shen_eq(symdic.symdic_kl_x45, KL_ARG_V1077_1067[1][1][0]) and shen_eq([], KL_ARG_V1077_1067[1][1][1])))))) else ([tco_apply(shen_remove_modes, [KL_ARG_V1077_1067[0]]), tco_apply(shen_remove_modes, [KL_ARG_V1077_1067[1]])] if shen_consp(KL_ARG_V1077_1067) else (KL_ARG_V1077_1067 if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.remove_modes', shen_remove_modes)

@tail_recursion
def shen_ephemeral_variablex63(KL_ARG_V1078_1068, KL_ARG_V1079_1069):
    global symdic
    return (tco_apply(kl_variablex63, [KL_ARG_V1078_1068]) and tco_apply(kl_variablex63, [KL_ARG_V1079_1069]))
shen_add_fun('shen.ephemeral_variable?', shen_ephemeral_variablex63)

@tail_recursion
def shen_prolog_constantx63(KL_ARG_V1088_1070):
    global symdic
    return (False if shen_consp(KL_ARG_V1088_1070) else (True if True else shen_simple_error('condition failure')))
shen_add_fun('shen.prolog_constant?', shen_prolog_constantx63)

@tail_recursion
def shen_aum_to_shen(KL_ARG_V1089_1071):
    global symdic
    return ([symdic.symdic_kl_let, [KL_ARG_V1089_1071[1][0], [tco_apply(shen_aum_to_shen, [KL_ARG_V1089_1071[1][1][1][0]]), [tco_apply(shen_aum_to_shen, [KL_ARG_V1089_1071[1][1][1][1][1][0]]), []]]]] if (shen_consp(KL_ARG_V1089_1071) and (shen_eq(symdic.symdic_kl_let, KL_ARG_V1089_1071[0]) and (shen_consp(KL_ARG_V1089_1071[1]) and (shen_consp(KL_ARG_V1089_1071[1][1]) and (shen_eq(symdic.symdic_shen_be, KL_ARG_V1089_1071[1][1][0]) and (shen_consp(KL_ARG_V1089_1071[1][1][1]) and (shen_consp(KL_ARG_V1089_1071[1][1][1][1]) and (shen_eq(symdic.symdic_kl_in, KL_ARG_V1089_1071[1][1][1][1][0]) and (shen_consp(KL_ARG_V1089_1071[1][1][1][1][1]) and shen_eq([], KL_ARG_V1089_1071[1][1][1][1][1][1])))))))))) else ([symdic.symdic_shen_lazyderef, [tco_apply(shen_aum_to_shen, [KL_ARG_V1089_1071[1][1][1][1][0]]), [symdic.symdic_ProcessN, []]]] if (shen_consp(KL_ARG_V1089_1071) and (shen_eq(symdic.symdic_shen_the, KL_ARG_V1089_1071[0]) and (shen_consp(KL_ARG_V1089_1071[1]) and (shen_eq(symdic.symdic_shen_result, KL_ARG_V1089_1071[1][0]) and (shen_consp(KL_ARG_V1089_1071[1][1]) and (shen_eq(symdic.symdic_shen_of, KL_ARG_V1089_1071[1][1][0]) and (shen_consp(KL_ARG_V1089_1071[1][1][1]) and (shen_eq(symdic.symdic_shen_dereferencing, KL_ARG_V1089_1071[1][1][1][0]) and (shen_consp(KL_ARG_V1089_1071[1][1][1][1]) and shen_eq([], KL_ARG_V1089_1071[1][1][1][1][1])))))))))) else ([symdic.symdic_kl_if, [tco_apply(shen_aum_to_shen, [KL_ARG_V1089_1071[1][0]]), [tco_apply(shen_aum_to_shen, [KL_ARG_V1089_1071[1][1][1][0]]), [tco_apply(shen_aum_to_shen, [KL_ARG_V1089_1071[1][1][1][1][1][0]]), []]]]] if (shen_consp(KL_ARG_V1089_1071) and (shen_eq(symdic.symdic_kl_if, KL_ARG_V1089_1071[0]) and (shen_consp(KL_ARG_V1089_1071[1]) and (shen_consp(KL_ARG_V1089_1071[1][1]) and (shen_eq(symdic.symdic_shen_then, KL_ARG_V1089_1071[1][1][0]) and (shen_consp(KL_ARG_V1089_1071[1][1][1]) and (shen_consp(KL_ARG_V1089_1071[1][1][1][1]) and (shen_eq(symdic.symdic_shen_else, KL_ARG_V1089_1071[1][1][1][1][0]) and (shen_consp(KL_ARG_V1089_1071[1][1][1][1][1]) and shen_eq([], KL_ARG_V1089_1071[1][1][1][1][1][1])))))))))) else ([symdic.symdic_shen_pvarx63, [KL_ARG_V1089_1071[0], []]] if (shen_consp(KL_ARG_V1089_1071) and (shen_consp(KL_ARG_V1089_1071[1]) and (shen_eq(symdic.symdic_kl_is, KL_ARG_V1089_1071[1][0]) and (shen_consp(KL_ARG_V1089_1071[1][1]) and (shen_eq(symdic.symdic_shen_a, KL_ARG_V1089_1071[1][1][0]) and (shen_consp(KL_ARG_V1089_1071[1][1][1]) and (shen_eq(symdic.symdic_shen_variable, KL_ARG_V1089_1071[1][1][1][0]) and shen_eq([], KL_ARG_V1089_1071[1][1][1][1])))))))) else ([symdic.symdic_kl_consx63, [KL_ARG_V1089_1071[0], []]] if (shen_consp(KL_ARG_V1089_1071) and (shen_consp(KL_ARG_V1089_1071[1]) and (shen_eq(symdic.symdic_kl_is, KL_ARG_V1089_1071[1][0]) and (shen_consp(KL_ARG_V1089_1071[1][1]) and (shen_eq(symdic.symdic_shen_a, KL_ARG_V1089_1071[1][1][0]) and (shen_consp(KL_ARG_V1089_1071[1][1][1]) and (shen_eq(symdic.symdic_shen_nonx45empty, KL_ARG_V1089_1071[1][1][1][0]) and (shen_consp(KL_ARG_V1089_1071[1][1][1][1]) and (shen_eq(symdic.symdic_kl_list, KL_ARG_V1089_1071[1][1][1][1][0]) and shen_eq([], KL_ARG_V1089_1071[1][1][1][1][1])))))))))) else (tail_call(shen_aum_to_shen, [KL_ARG_V1089_1071[1][1][1][1][1][1][1][0]]) if (shen_consp(KL_ARG_V1089_1071) and (shen_eq(symdic.symdic_shen_rename, KL_ARG_V1089_1071[0]) and (shen_consp(KL_ARG_V1089_1071[1]) and (shen_eq(symdic.symdic_shen_the, KL_ARG_V1089_1071[1][0]) and (shen_consp(KL_ARG_V1089_1071[1][1]) and (shen_eq(symdic.symdic_shen_variables, KL_ARG_V1089_1071[1][1][0]) and (shen_consp(KL_ARG_V1089_1071[1][1][1]) and (shen_eq(symdic.symdic_kl_in, KL_ARG_V1089_1071[1][1][1][0]) and (shen_consp(KL_ARG_V1089_1071[1][1][1][1]) and (shen_eq([], KL_ARG_V1089_1071[1][1][1][1][0]) and (shen_consp(KL_ARG_V1089_1071[1][1][1][1][1]) and (shen_eq(symdic.symdic_kl_and, KL_ARG_V1089_1071[1][1][1][1][1][0]) and (shen_consp(KL_ARG_V1089_1071[1][1][1][1][1][1]) and (shen_eq(symdic.symdic_shen_then, KL_ARG_V1089_1071[1][1][1][1][1][1][0]) and (shen_consp(KL_ARG_V1089_1071[1][1][1][1][1][1][1]) and shen_eq([], KL_ARG_V1089_1071[1][1][1][1][1][1][1][1])))))))))))))))) else ([symdic.symdic_kl_let, [KL_ARG_V1089_1071[1][1][1][1][0][0], [[symdic.symdic_shen_newpv, [symdic.symdic_ProcessN, []]], [tco_apply(shen_aum_to_shen, [[symdic.symdic_shen_rename, [symdic.symdic_shen_the, [symdic.symdic_shen_variables, [symdic.symdic_kl_in, [KL_ARG_V1089_1071[1][1][1][1][0][1], KL_ARG_V1089_1071[1][1][1][1][1]]]]]]]), []]]]] if (shen_consp(KL_ARG_V1089_1071) and (shen_eq(symdic.symdic_shen_rename, KL_ARG_V1089_1071[0]) and (shen_consp(KL_ARG_V1089_1071[1]) and (shen_eq(symdic.symdic_shen_the, KL_ARG_V1089_1071[1][0]) and (shen_consp(KL_ARG_V1089_1071[1][1]) and (shen_eq(symdic.symdic_shen_variables, KL_ARG_V1089_1071[1][1][0]) and (shen_consp(KL_ARG_V1089_1071[1][1][1]) and (shen_eq(symdic.symdic_kl_in, KL_ARG_V1089_1071[1][1][1][0]) and (shen_consp(KL_ARG_V1089_1071[1][1][1][1]) and (shen_consp(KL_ARG_V1089_1071[1][1][1][1][0]) and (shen_consp(KL_ARG_V1089_1071[1][1][1][1][1]) and (shen_eq(symdic.symdic_kl_and, KL_ARG_V1089_1071[1][1][1][1][1][0]) and (shen_consp(KL_ARG_V1089_1071[1][1][1][1][1][1]) and (shen_eq(symdic.symdic_shen_then, KL_ARG_V1089_1071[1][1][1][1][1][1][0]) and (shen_consp(KL_ARG_V1089_1071[1][1][1][1][1][1][1]) and shen_eq([], KL_ARG_V1089_1071[1][1][1][1][1][1][1][1])))))))))))))))) else ([symdic.symdic_kl_do, [[symdic.symdic_shen_bindv, [KL_ARG_V1089_1071[1][0], [tco_apply(shen_chwild, [KL_ARG_V1089_1071[1][1][1][0]]), [symdic.symdic_ProcessN, []]]]], [[symdic.symdic_kl_let, [symdic.symdic_Result, [tco_apply(shen_aum_to_shen, [KL_ARG_V1089_1071[1][1][1][1][1][0]]), [[symdic.symdic_kl_do, [[symdic.symdic_shen_unbindv, [KL_ARG_V1089_1071[1][0], [symdic.symdic_ProcessN, []]]], [symdic.symdic_Result, []]]], []]]]], []]]] if (shen_consp(KL_ARG_V1089_1071) and (shen_eq(symdic.symdic_kl_bind, KL_ARG_V1089_1071[0]) and (shen_consp(KL_ARG_V1089_1071[1]) and (shen_consp(KL_ARG_V1089_1071[1][1]) and (shen_eq(symdic.symdic_shen_to, KL_ARG_V1089_1071[1][1][0]) and (shen_consp(KL_ARG_V1089_1071[1][1][1]) and (shen_consp(KL_ARG_V1089_1071[1][1][1][1]) and (shen_eq(symdic.symdic_kl_in, KL_ARG_V1089_1071[1][1][1][1][0]) and (shen_consp(KL_ARG_V1089_1071[1][1][1][1][1]) and shen_eq([], KL_ARG_V1089_1071[1][1][1][1][1][1])))))))))) else ([symdic.symdic_kl_x61, [KL_ARG_V1089_1071[1][1][1][1][0], [KL_ARG_V1089_1071[0], []]]] if (shen_consp(KL_ARG_V1089_1071) and (shen_consp(KL_ARG_V1089_1071[1]) and (shen_eq(symdic.symdic_kl_is, KL_ARG_V1089_1071[1][0]) and (shen_consp(KL_ARG_V1089_1071[1][1]) and (shen_eq(symdic.symdic_kl_identical, KL_ARG_V1089_1071[1][1][0]) and (shen_consp(KL_ARG_V1089_1071[1][1][1]) and (shen_eq(symdic.symdic_shen_to, KL_ARG_V1089_1071[1][1][1][0]) and (shen_consp(KL_ARG_V1089_1071[1][1][1][1]) and shen_eq([], KL_ARG_V1089_1071[1][1][1][1][1]))))))))) else (False if shen_eq(symdic.symdic_shen_failedx33, KL_ARG_V1089_1071) else ([symdic.symdic_kl_hd, KL_ARG_V1089_1071[1][1][1]] if (shen_consp(KL_ARG_V1089_1071) and (shen_eq(symdic.symdic_shen_the, KL_ARG_V1089_1071[0]) and (shen_consp(KL_ARG_V1089_1071[1]) and (shen_eq(symdic.symdic_kl_head, KL_ARG_V1089_1071[1][0]) and (shen_consp(KL_ARG_V1089_1071[1][1]) and (shen_eq(symdic.symdic_shen_of, KL_ARG_V1089_1071[1][1][0]) and (shen_consp(KL_ARG_V1089_1071[1][1][1]) and shen_eq([], KL_ARG_V1089_1071[1][1][1][1])))))))) else ([symdic.symdic_kl_tl, KL_ARG_V1089_1071[1][1][1]] if (shen_consp(KL_ARG_V1089_1071) and (shen_eq(symdic.symdic_shen_the, KL_ARG_V1089_1071[0]) and (shen_consp(KL_ARG_V1089_1071[1]) and (shen_eq(symdic.symdic_kl_tail, KL_ARG_V1089_1071[1][0]) and (shen_consp(KL_ARG_V1089_1071[1][1]) and (shen_eq(symdic.symdic_shen_of, KL_ARG_V1089_1071[1][1][0]) and (shen_consp(KL_ARG_V1089_1071[1][1][1]) and shen_eq([], KL_ARG_V1089_1071[1][1][1][1])))))))) else ([symdic.symdic_kl_do, [[symdic.symdic_shen_incinfs, []], [[symdic.symdic_kl_thaw, [symdic.symdic_Continuation, []]], []]]] if (shen_consp(KL_ARG_V1089_1071) and (shen_eq(symdic.symdic_shen_pop, KL_ARG_V1089_1071[0]) and (shen_consp(KL_ARG_V1089_1071[1]) and (shen_eq(symdic.symdic_shen_the, KL_ARG_V1089_1071[1][0]) and (shen_consp(KL_ARG_V1089_1071[1][1]) and (shen_eq(symdic.symdic_shen_stack, KL_ARG_V1089_1071[1][1][0]) and shen_eq([], KL_ARG_V1089_1071[1][1][1]))))))) else ([symdic.symdic_kl_do, [[symdic.symdic_shen_incinfs, []], [tco_apply(shen_call_the_continuation, [tco_apply(shen_chwild, [KL_ARG_V1089_1071[1][1][1][0]]), symdic.symdic_ProcessN, symdic.symdic_Continuation]), []]]] if (shen_consp(KL_ARG_V1089_1071) and (shen_eq(symdic.symdic_kl_call, KL_ARG_V1089_1071[0]) and (shen_consp(KL_ARG_V1089_1071[1]) and (shen_eq(symdic.symdic_shen_the, KL_ARG_V1089_1071[1][0]) and (shen_consp(KL_ARG_V1089_1071[1][1]) and (shen_eq(symdic.symdic_shen_continuation, KL_ARG_V1089_1071[1][1][0]) and (shen_consp(KL_ARG_V1089_1071[1][1][1]) and shen_eq([], KL_ARG_V1089_1071[1][1][1][1])))))))) else (KL_ARG_V1089_1071 if True else shen_simple_error('condition failure'))))))))))))))))
shen_add_fun('shen.aum_to_shen', shen_aum_to_shen)

@tail_recursion
def shen_chwild(KL_ARG_V1090_1072):
    global symdic
    return ([symdic.symdic_shen_newpv, [symdic.symdic_ProcessN, []]] if shen_eq(KL_ARG_V1090_1072, symdic.symdic_kl__) else (tail_call(kl_map, [symdic.symdic_shen_chwild, KL_ARG_V1090_1072]) if shen_consp(KL_ARG_V1090_1072) else (KL_ARG_V1090_1072 if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.chwild', shen_chwild)

@tail_recursion
def shen_newpv(KL_ARG_V1091_1073):

    class KL_Context:
        KL_LOC_Countx431_1074 = None
        KL_LOC_IncVar_1075 = None
        KL_LOC_Vector_1076 = None
        KL_LOC_ResizeVectorIfNeeded_1077 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Countx431_1074', (shen_absvector_get(shen_get(symdic.symdic_shen_x42varcounterx42), KL_ARG_V1091_1073) + 1)), [setattr(KL_CTX, 'KL_LOC_IncVar_1075', shen_absvector_set(shen_get(symdic.symdic_shen_x42varcounterx42), KL_ARG_V1091_1073, KL_CTX.KL_LOC_Countx431_1074)), [setattr(KL_CTX, 'KL_LOC_Vector_1076', shen_absvector_get(shen_get(symdic.symdic_shen_x42prologvectorsx42), KL_ARG_V1091_1073)), [setattr(KL_CTX, 'KL_LOC_ResizeVectorIfNeeded_1077', (tco_apply(shen_resizeprocessvector, [KL_ARG_V1091_1073, KL_CTX.KL_LOC_Countx431_1074]) if shen_eq(KL_CTX.KL_LOC_Countx431_1074, tco_apply(kl_limit, [KL_CTX.KL_LOC_Vector_1076])) else symdic.symdic_shen_skip)), tail_call(shen_mkx45pvar, [KL_CTX.KL_LOC_Countx431_1074])][(-1)]][(-1)]][(-1)]][(-1)]
shen_add_fun('shen.newpv', shen_newpv)

@tail_recursion
def shen_resizeprocessvector(KL_ARG_V1092_1078, KL_ARG_V1093_1079):

    class KL_Context:
        KL_LOC_Vector_1080 = None
        KL_LOC_BigVector_1081 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Vector_1080', shen_absvector_get(shen_get(symdic.symdic_shen_x42prologvectorsx42), KL_ARG_V1092_1078)), [setattr(KL_CTX, 'KL_LOC_BigVector_1081', tco_apply(shen_resizex45vector, [KL_CTX.KL_LOC_Vector_1080, (KL_ARG_V1093_1079 + KL_ARG_V1093_1079), symdic.symdic_shen_x45nullx45])), shen_absvector_set(shen_get(symdic.symdic_shen_x42prologvectorsx42), KL_ARG_V1092_1078, KL_CTX.KL_LOC_BigVector_1081)][(-1)]][(-1)]
shen_add_fun('shen.resizeprocessvector', shen_resizeprocessvector)

@tail_recursion
def shen_resizex45vector(KL_ARG_V1094_1082, KL_ARG_V1095_1083, KL_ARG_V1096_1084):

    class KL_Context:
        KL_LOC_BigVector_1085 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_BigVector_1085', shen_absvector_set(shen_absvector((1 + KL_ARG_V1095_1083)), 0, KL_ARG_V1095_1083)), tail_call(shen_copyx45vector, [KL_ARG_V1094_1082, KL_CTX.KL_LOC_BigVector_1085, tco_apply(kl_limit, [KL_ARG_V1094_1082]), KL_ARG_V1095_1083, KL_ARG_V1096_1084])][(-1)]
shen_add_fun('shen.resize-vector', shen_resizex45vector)

@tail_recursion
def shen_copyx45vector(KL_ARG_V1097_1086, KL_ARG_V1098_1087, KL_ARG_V1099_1088, KL_ARG_V1100_1089, KL_ARG_V1101_1090):
    global symdic
    return tail_call(shen_copyx45vectorx45stagex452, [(1 + KL_ARG_V1099_1088), (KL_ARG_V1100_1089 + 1), KL_ARG_V1101_1090, tco_apply(shen_copyx45vectorx45stagex451, [1, KL_ARG_V1097_1086, KL_ARG_V1098_1087, (1 + KL_ARG_V1099_1088)])])
shen_add_fun('shen.copy-vector', shen_copyx45vector)

@tail_recursion
def shen_copyx45vectorx45stagex451(KL_ARG_V1104_1091, KL_ARG_V1105_1092, KL_ARG_V1106_1093, KL_ARG_V1107_1094):
    global symdic
    return (KL_ARG_V1106_1093 if shen_eq(KL_ARG_V1107_1094, KL_ARG_V1104_1091) else (tail_call(shen_copyx45vectorx45stagex451, [(1 + KL_ARG_V1104_1091), KL_ARG_V1105_1092, shen_absvector_set(KL_ARG_V1106_1093, KL_ARG_V1104_1091, shen_absvector_get(KL_ARG_V1105_1092, KL_ARG_V1104_1091)), KL_ARG_V1107_1094]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.copy-vector-stage-1', shen_copyx45vectorx45stagex451)

@tail_recursion
def shen_copyx45vectorx45stagex452(KL_ARG_V1111_1095, KL_ARG_V1112_1096, KL_ARG_V1113_1097, KL_ARG_V1114_1098):
    global symdic
    return (KL_ARG_V1114_1098 if shen_eq(KL_ARG_V1112_1096, KL_ARG_V1111_1095) else (tail_call(shen_copyx45vectorx45stagex452, [(KL_ARG_V1111_1095 + 1), KL_ARG_V1112_1096, KL_ARG_V1113_1097, shen_absvector_set(KL_ARG_V1114_1098, KL_ARG_V1111_1095, KL_ARG_V1113_1097)]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.copy-vector-stage-2', shen_copyx45vectorx45stagex452)

@tail_recursion
def shen_mkx45pvar(KL_ARG_V1116_1099):
    global symdic
    return shen_absvector_set(shen_absvector_set(shen_absvector(2), 0, symdic.symdic_shen_pvar), 1, KL_ARG_V1116_1099)
shen_add_fun('shen.mk-pvar', shen_mkx45pvar)

@tail_recursion
def shen_pvarx63(KL_ARG_V1117_1100):
    global symdic
    return (shen_absvectorp(KL_ARG_V1117_1100) and shen_eq(shen_absvector_get(KL_ARG_V1117_1100, 0), symdic.symdic_shen_pvar))
shen_add_fun('shen.pvar?', shen_pvarx63)

@tail_recursion
def shen_bindv(KL_ARG_V1118_1101, KL_ARG_V1119_1102, KL_ARG_V1120_1103):

    class KL_Context:
        KL_LOC_Vector_1104 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Vector_1104', shen_absvector_get(shen_get(symdic.symdic_shen_x42prologvectorsx42), KL_ARG_V1120_1103)), shen_absvector_set(KL_CTX.KL_LOC_Vector_1104, shen_absvector_get(KL_ARG_V1118_1101, 1), KL_ARG_V1119_1102)][(-1)]
shen_add_fun('shen.bindv', shen_bindv)

@tail_recursion
def shen_unbindv(KL_ARG_V1121_1105, KL_ARG_V1122_1106):

    class KL_Context:
        KL_LOC_Vector_1107 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Vector_1107', shen_absvector_get(shen_get(symdic.symdic_shen_x42prologvectorsx42), KL_ARG_V1122_1106)), shen_absvector_set(KL_CTX.KL_LOC_Vector_1107, shen_absvector_get(KL_ARG_V1121_1105, 1), symdic.symdic_shen_x45nullx45)][(-1)]
shen_add_fun('shen.unbindv', shen_unbindv)

@tail_recursion
def shen_incinfs():
    global symdic
    return shen_set(symdic.symdic_shen_x42infsx42, (1 + shen_get(symdic.symdic_shen_x42infsx42)))
shen_add_fun('shen.incinfs', shen_incinfs)

@tail_recursion
def shen_call_the_continuation(KL_ARG_V1123_1108, KL_ARG_V1124_1109, KL_ARG_V1125_1110):

    class KL_Context:
        KL_LOC_NewContinuation_1111 = None
    KL_CTX = KL_Context()
    global symdic
    return ([KL_ARG_V1123_1108[0][0], tco_apply(kl_append, [KL_ARG_V1123_1108[0][1], [KL_ARG_V1124_1109, [KL_ARG_V1125_1110, []]]])] if (shen_consp(KL_ARG_V1123_1108) and (shen_consp(KL_ARG_V1123_1108[0]) and shen_eq([], KL_ARG_V1123_1108[1]))) else ([setattr(KL_CTX, 'KL_LOC_NewContinuation_1111', tco_apply(shen_newcontinuation, [KL_ARG_V1123_1108[1], KL_ARG_V1124_1109, KL_ARG_V1125_1110])), [KL_ARG_V1123_1108[0][0], tco_apply(kl_append, [KL_ARG_V1123_1108[0][1], [KL_ARG_V1124_1109, [KL_CTX.KL_LOC_NewContinuation_1111, []]]])]][(-1)] if (shen_consp(KL_ARG_V1123_1108) and shen_consp(KL_ARG_V1123_1108[0])) else (tail_call(shen_sysx45error, [symdic.symdic_shen_call_the_continuation]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.call_the_continuation', shen_call_the_continuation)

@tail_recursion
def shen_newcontinuation(KL_ARG_V1126_1112, KL_ARG_V1127_1113, KL_ARG_V1128_1114):
    global symdic
    return (KL_ARG_V1128_1114 if shen_eq([], KL_ARG_V1126_1112) else ([symdic.symdic_kl_freeze, [[KL_ARG_V1126_1112[0][0], tco_apply(kl_append, [KL_ARG_V1126_1112[0][1], [KL_ARG_V1127_1113, [tco_apply(shen_newcontinuation, [KL_ARG_V1126_1112[1], KL_ARG_V1127_1113, KL_ARG_V1128_1114]), []]]])], []]] if (shen_consp(KL_ARG_V1126_1112) and shen_consp(KL_ARG_V1126_1112[0])) else (tail_call(shen_sysx45error, [symdic.symdic_shen_newcontinuation]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.newcontinuation', shen_newcontinuation)

@tail_recursion
def kl_return(KL_ARG_V1133_1115, KL_ARG_V1134_1116, KL_ARG_V1135_1117):
    global symdic
    return tail_call(shen_deref, [KL_ARG_V1133_1115, KL_ARG_V1134_1116])
shen_add_fun('return', kl_return)

@tail_recursion
def shen_measurex38return(KL_ARG_V1140_1118, KL_ARG_V1141_1119, KL_ARG_V1142_1120):
    global symdic
    return [shen_pr(tco_apply(shen_app, [shen_get(symdic.symdic_shen_x42infsx42), ' inferences\r\n', symdic.symdic_shen_a]), tco_apply(kl_stoutput, [])), tail_call(shen_deref, [KL_ARG_V1140_1118, KL_ARG_V1141_1119])][(-1)]
shen_add_fun('shen.measure&return', shen_measurex38return)

@tail_recursion
def kl_unify(KL_ARG_V1143_1121, KL_ARG_V1144_1122, KL_ARG_V1145_1123, KL_ARG_V1146_1124):
    global symdic
    return tail_call(shen_lzyx61, [tco_apply(shen_lazyderef, [KL_ARG_V1143_1121, KL_ARG_V1145_1123]), tco_apply(shen_lazyderef, [KL_ARG_V1144_1122, KL_ARG_V1145_1123]), KL_ARG_V1145_1123, KL_ARG_V1146_1124])
shen_add_fun('unify', kl_unify)

@tail_recursion
def shen_lzyx61(KL_ARG_V1163_1125, KL_ARG_V1164_1126, KL_ARG_V1165_1127, KL_ARG_V1166_1128):
    global symdic
    return (tail_call(kl_thaw, [KL_ARG_V1166_1128]) if shen_eq(KL_ARG_V1164_1126, KL_ARG_V1163_1125) else (tail_call(kl_bind, [KL_ARG_V1163_1125, KL_ARG_V1164_1126, KL_ARG_V1165_1127, KL_ARG_V1166_1128]) if tco_apply(shen_pvarx63, [KL_ARG_V1163_1125]) else (tail_call(kl_bind, [KL_ARG_V1164_1126, KL_ARG_V1163_1125, KL_ARG_V1165_1127, KL_ARG_V1166_1128]) if tco_apply(shen_pvarx63, [KL_ARG_V1164_1126]) else (tail_call(shen_lzyx61, [tco_apply(shen_lazyderef, [KL_ARG_V1163_1125[0], KL_ARG_V1165_1127]), tco_apply(shen_lazyderef, [KL_ARG_V1164_1126[0], KL_ARG_V1165_1127]), KL_ARG_V1165_1127, (lambda : tail_call(shen_lzyx61, [tco_apply(shen_lazyderef, [KL_ARG_V1163_1125[1], KL_ARG_V1165_1127]), tco_apply(shen_lazyderef, [KL_ARG_V1164_1126[1], KL_ARG_V1165_1127]), KL_ARG_V1165_1127, KL_ARG_V1166_1128]))]) if (shen_consp(KL_ARG_V1163_1125) and shen_consp(KL_ARG_V1164_1126)) else (False if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.lzy=', shen_lzyx61)

@tail_recursion
def shen_deref(KL_ARG_V1168_1129, KL_ARG_V1169_1130):

    class KL_Context:
        KL_LOC_Value_1131 = None
    KL_CTX = KL_Context()
    global symdic
    return ([tco_apply(shen_deref, [KL_ARG_V1168_1129[0], KL_ARG_V1169_1130]), tco_apply(shen_deref, [KL_ARG_V1168_1129[1], KL_ARG_V1169_1130])] if shen_consp(KL_ARG_V1168_1129) else (([setattr(KL_CTX, 'KL_LOC_Value_1131', tco_apply(shen_valvector, [KL_ARG_V1168_1129, KL_ARG_V1169_1130])), (KL_ARG_V1168_1129 if shen_eq(KL_CTX.KL_LOC_Value_1131, symdic.symdic_shen_x45nullx45) else tail_call(shen_deref, [KL_CTX.KL_LOC_Value_1131, KL_ARG_V1169_1130]))][(-1)] if tco_apply(shen_pvarx63, [KL_ARG_V1168_1129]) else KL_ARG_V1168_1129) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.deref', shen_deref)

@tail_recursion
def shen_lazyderef(KL_ARG_V1170_1132, KL_ARG_V1171_1133):

    class KL_Context:
        KL_LOC_Value_1134 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_Value_1134', tco_apply(shen_valvector, [KL_ARG_V1170_1132, KL_ARG_V1171_1133])), (KL_ARG_V1170_1132 if shen_eq(KL_CTX.KL_LOC_Value_1134, symdic.symdic_shen_x45nullx45) else tail_call(shen_lazyderef, [KL_CTX.KL_LOC_Value_1134, KL_ARG_V1171_1133]))][(-1)] if tco_apply(shen_pvarx63, [KL_ARG_V1170_1132]) else KL_ARG_V1170_1132)
shen_add_fun('shen.lazyderef', shen_lazyderef)

@tail_recursion
def shen_valvector(KL_ARG_V1172_1135, KL_ARG_V1173_1136):
    global symdic
    return shen_absvector_get(shen_absvector_get(shen_get(symdic.symdic_shen_x42prologvectorsx42), KL_ARG_V1173_1136), shen_absvector_get(KL_ARG_V1172_1135, 1))
shen_add_fun('shen.valvector', shen_valvector)

@tail_recursion
def kl_unifyx33(KL_ARG_V1174_1137, KL_ARG_V1175_1138, KL_ARG_V1176_1139, KL_ARG_V1177_1140):
    global symdic
    return tail_call(shen_lzyx61x33, [tco_apply(shen_lazyderef, [KL_ARG_V1174_1137, KL_ARG_V1176_1139]), tco_apply(shen_lazyderef, [KL_ARG_V1175_1138, KL_ARG_V1176_1139]), KL_ARG_V1176_1139, KL_ARG_V1177_1140])
shen_add_fun('unify!', kl_unifyx33)

@tail_recursion
def shen_lzyx61x33(KL_ARG_V1194_1141, KL_ARG_V1195_1142, KL_ARG_V1196_1143, KL_ARG_V1197_1144):
    global symdic
    return (tail_call(kl_thaw, [KL_ARG_V1197_1144]) if shen_eq(KL_ARG_V1195_1142, KL_ARG_V1194_1141) else (tail_call(kl_bind, [KL_ARG_V1194_1141, KL_ARG_V1195_1142, KL_ARG_V1196_1143, KL_ARG_V1197_1144]) if (tco_apply(shen_pvarx63, [KL_ARG_V1194_1141]) and (not tco_apply(shen_occursx63, [KL_ARG_V1194_1141, tco_apply(shen_deref, [KL_ARG_V1195_1142, KL_ARG_V1196_1143])]))) else (tail_call(kl_bind, [KL_ARG_V1195_1142, KL_ARG_V1194_1141, KL_ARG_V1196_1143, KL_ARG_V1197_1144]) if (tco_apply(shen_pvarx63, [KL_ARG_V1195_1142]) and (not tco_apply(shen_occursx63, [KL_ARG_V1195_1142, tco_apply(shen_deref, [KL_ARG_V1194_1141, KL_ARG_V1196_1143])]))) else (tail_call(shen_lzyx61x33, [tco_apply(shen_lazyderef, [KL_ARG_V1194_1141[0], KL_ARG_V1196_1143]), tco_apply(shen_lazyderef, [KL_ARG_V1195_1142[0], KL_ARG_V1196_1143]), KL_ARG_V1196_1143, (lambda : tail_call(shen_lzyx61x33, [tco_apply(shen_lazyderef, [KL_ARG_V1194_1141[1], KL_ARG_V1196_1143]), tco_apply(shen_lazyderef, [KL_ARG_V1195_1142[1], KL_ARG_V1196_1143]), KL_ARG_V1196_1143, KL_ARG_V1197_1144]))]) if (shen_consp(KL_ARG_V1194_1141) and shen_consp(KL_ARG_V1195_1142)) else (False if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.lzy=!', shen_lzyx61x33)

@tail_recursion
def shen_occursx63(KL_ARG_V1207_1145, KL_ARG_V1208_1146):
    global symdic
    return (True if shen_eq(KL_ARG_V1208_1146, KL_ARG_V1207_1145) else ((tco_apply(shen_occursx63, [KL_ARG_V1207_1145, KL_ARG_V1208_1146[0]]) or tco_apply(shen_occursx63, [KL_ARG_V1207_1145, KL_ARG_V1208_1146[1]])) if shen_consp(KL_ARG_V1208_1146) else (False if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.occurs?', shen_occursx63)

@tail_recursion
def kl_identical(KL_ARG_V1210_1147, KL_ARG_V1211_1148, KL_ARG_V1212_1149, KL_ARG_V1213_1150):
    global symdic
    return tail_call(shen_lzyx61x61, [tco_apply(shen_lazyderef, [KL_ARG_V1210_1147, KL_ARG_V1212_1149]), tco_apply(shen_lazyderef, [KL_ARG_V1211_1148, KL_ARG_V1212_1149]), KL_ARG_V1212_1149, KL_ARG_V1213_1150])
shen_add_fun('identical', kl_identical)

@tail_recursion
def shen_lzyx61x61(KL_ARG_V1230_1151, KL_ARG_V1231_1152, KL_ARG_V1232_1153, KL_ARG_V1233_1154):
    global symdic
    return (tail_call(kl_thaw, [KL_ARG_V1233_1154]) if shen_eq(KL_ARG_V1231_1152, KL_ARG_V1230_1151) else (tail_call(shen_lzyx61x61, [tco_apply(shen_lazyderef, [KL_ARG_V1230_1151[0], KL_ARG_V1232_1153]), tco_apply(shen_lazyderef, [KL_ARG_V1231_1152[0], KL_ARG_V1232_1153]), KL_ARG_V1232_1153, (lambda : tail_call(shen_lzyx61x61, [KL_ARG_V1230_1151[1], KL_ARG_V1231_1152[1], KL_ARG_V1232_1153, KL_ARG_V1233_1154]))]) if (shen_consp(KL_ARG_V1230_1151) and shen_consp(KL_ARG_V1231_1152)) else (False if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.lzy==', shen_lzyx61x61)

@tail_recursion
def shen_pvar(KL_ARG_V1235_1155):
    global symdic
    return ('Var' + tco_apply(shen_app, [shen_absvector_get(KL_ARG_V1235_1155, 1), '', symdic.symdic_shen_a]))
shen_add_fun('shen.pvar', shen_pvar)

@tail_recursion
def kl_bind(KL_ARG_V1236_1156, KL_ARG_V1237_1157, KL_ARG_V1238_1158, KL_ARG_V1239_1159):

    class KL_Context:
        KL_LOC_Result_1160 = None
    KL_CTX = KL_Context()
    global symdic
    return [tco_apply(shen_bindv, [KL_ARG_V1236_1156, KL_ARG_V1237_1157, KL_ARG_V1238_1158]), [setattr(KL_CTX, 'KL_LOC_Result_1160', tco_apply(kl_thaw, [KL_ARG_V1239_1159])), [tco_apply(shen_unbindv, [KL_ARG_V1236_1156, KL_ARG_V1238_1158]), KL_CTX.KL_LOC_Result_1160][(-1)]][(-1)]][(-1)]
shen_add_fun('bind', kl_bind)

@tail_recursion
def kl_fwhen(KL_ARG_V1254_1161, KL_ARG_V1255_1162, KL_ARG_V1256_1163):
    global symdic
    return (tail_call(kl_thaw, [KL_ARG_V1256_1163]) if shen_eq(True, KL_ARG_V1254_1161) else (False if shen_eq(False, KL_ARG_V1254_1161) else (shen_simple_error(('fwhen expects a boolean: not ' + tco_apply(shen_app, [KL_ARG_V1254_1161, '%', symdic.symdic_shen_s]))) if True else shen_simple_error('condition failure'))))
shen_add_fun('fwhen', kl_fwhen)

@tail_recursion
def kl_call(KL_ARG_V1269_1164, KL_ARG_V1270_1165, KL_ARG_V1271_1166):
    global symdic
    return (tail_call(shen_callx45help, [tco_apply(shen_m_prolog_to_sx45prolog_predicate, [tco_apply(shen_lazyderef, [KL_ARG_V1269_1164[0], KL_ARG_V1270_1165])]), KL_ARG_V1269_1164[1], KL_ARG_V1270_1165, KL_ARG_V1271_1166]) if shen_consp(KL_ARG_V1269_1164) else (False if True else shen_simple_error('condition failure')))
shen_add_fun('call', kl_call)

@tail_recursion
def shen_callx45help(KL_ARG_V1272_1167, KL_ARG_V1273_1168, KL_ARG_V1274_1169, KL_ARG_V1275_1170):
    global symdic
    return (shen_apply(KL_ARG_V1272_1167, [KL_ARG_V1274_1169, KL_ARG_V1275_1170]) if shen_eq([], KL_ARG_V1273_1168) else (tail_call(shen_callx45help, [shen_apply(KL_ARG_V1272_1167, [KL_ARG_V1273_1168[0]]), KL_ARG_V1273_1168[1], KL_ARG_V1274_1169, KL_ARG_V1275_1170]) if shen_consp(KL_ARG_V1273_1168) else (tail_call(shen_sysx45error, [symdic.symdic_shen_callx45help]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.call-help', shen_callx45help)

@tail_recursion
def shen_intprolog(KL_ARG_V1276_1171):

    class KL_Context:
        KL_LOC_ProcessN_1172 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_ProcessN_1172', tco_apply(shen_startx45newx45prologx45process, [])), tail_call(shen_intprologx45help, [KL_ARG_V1276_1171[0][0], tco_apply(shen_insertx45prologx45variables, [[KL_ARG_V1276_1171[0][1], [KL_ARG_V1276_1171[1], []]], KL_CTX.KL_LOC_ProcessN_1172]), KL_CTX.KL_LOC_ProcessN_1172])][(-1)] if (shen_consp(KL_ARG_V1276_1171) and shen_consp(KL_ARG_V1276_1171[0])) else (tail_call(shen_sysx45error, [symdic.symdic_shen_intprolog]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.intprolog', shen_intprolog)

@tail_recursion
def shen_intprologx45help(KL_ARG_V1277_1173, KL_ARG_V1278_1174, KL_ARG_V1279_1175):
    global symdic
    return (tail_call(shen_intprologx45helpx45help, [KL_ARG_V1277_1173, KL_ARG_V1278_1174[0], KL_ARG_V1278_1174[1][0], KL_ARG_V1279_1175]) if (shen_consp(KL_ARG_V1278_1174) and (shen_consp(KL_ARG_V1278_1174[1]) and shen_eq([], KL_ARG_V1278_1174[1][1]))) else (tail_call(shen_sysx45error, [symdic.symdic_shen_intprologx45help]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.intprolog-help', shen_intprologx45help)

@tail_recursion
def shen_intprologx45helpx45help(KL_ARG_V1280_1176, KL_ARG_V1281_1177, KL_ARG_V1282_1178, KL_ARG_V1283_1179):
    global symdic
    return (shen_apply(KL_ARG_V1280_1176, [KL_ARG_V1283_1179, (lambda : tail_call(shen_callx45rest, [KL_ARG_V1282_1178, KL_ARG_V1283_1179]))]) if shen_eq([], KL_ARG_V1281_1177) else (tail_call(shen_intprologx45helpx45help, [shen_apply(KL_ARG_V1280_1176, [KL_ARG_V1281_1177[0]]), KL_ARG_V1281_1177[1], KL_ARG_V1282_1178, KL_ARG_V1283_1179]) if shen_consp(KL_ARG_V1281_1177) else (tail_call(shen_sysx45error, [symdic.symdic_shen_intprologx45helpx45help]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.intprolog-help-help', shen_intprologx45helpx45help)

@tail_recursion
def shen_callx45rest(KL_ARG_V1286_1180, KL_ARG_V1287_1181):
    global symdic
    return (True if shen_eq([], KL_ARG_V1286_1180) else (tail_call(shen_callx45rest, [[[tco_apply(KL_ARG_V1286_1180[0][0], [KL_ARG_V1286_1180[0][1][0]]), KL_ARG_V1286_1180[0][1][1]], KL_ARG_V1286_1180[1]], KL_ARG_V1287_1181]) if (shen_consp(KL_ARG_V1286_1180) and (shen_consp(KL_ARG_V1286_1180[0]) and shen_consp(KL_ARG_V1286_1180[0][1]))) else (tail_call(KL_ARG_V1286_1180[0][0], [KL_ARG_V1287_1181, (lambda : tail_call(shen_callx45rest, [KL_ARG_V1286_1180[1], KL_ARG_V1287_1181]))]) if (shen_consp(KL_ARG_V1286_1180) and (shen_consp(KL_ARG_V1286_1180[0]) and shen_eq([], KL_ARG_V1286_1180[0][1]))) else (tail_call(shen_sysx45error, [symdic.symdic_shen_callx45rest]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.call-rest', shen_callx45rest)

@tail_recursion
def shen_startx45newx45prologx45process():

    class KL_Context:
        KL_LOC_IncrementProcessCounter_1182 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_IncrementProcessCounter_1182', shen_set(symdic.symdic_shen_x42processx45counterx42, (1 + shen_get(symdic.symdic_shen_x42processx45counterx42)))), tail_call(shen_initialisex45prolog, [KL_CTX.KL_LOC_IncrementProcessCounter_1182])][(-1)]
shen_add_fun('shen.start-new-prolog-process', shen_startx45newx45prologx45process)

@tail_recursion
def shen_insertx45prologx45variables(KL_ARG_V1288_1183, KL_ARG_V1289_1184):
    global symdic
    return tail_call(shen_insertx45prologx45variablesx45help, [KL_ARG_V1288_1183, tco_apply(shen_flatten, [KL_ARG_V1288_1183]), KL_ARG_V1289_1184])
shen_add_fun('shen.insert-prolog-variables', shen_insertx45prologx45variables)

@tail_recursion
def shen_insertx45prologx45variablesx45help(KL_ARG_V1294_1185, KL_ARG_V1295_1186, KL_ARG_V1296_1187):

    class KL_Context:
        KL_LOC_V_1188 = None
        KL_LOC_XVx47Y_1189 = None
        KL_LOC_Zx45Y_1190 = None
    KL_CTX = KL_Context()
    global symdic
    return (KL_ARG_V1294_1185 if shen_eq([], KL_ARG_V1295_1186) else ([setattr(KL_CTX, 'KL_LOC_V_1188', tco_apply(shen_newpv, [KL_ARG_V1296_1187])), [setattr(KL_CTX, 'KL_LOC_XVx47Y_1189', tco_apply(kl_subst, [KL_CTX.KL_LOC_V_1188, KL_ARG_V1295_1186[0], KL_ARG_V1294_1185])), [setattr(KL_CTX, 'KL_LOC_Zx45Y_1190', tco_apply(kl_remove, [KL_ARG_V1295_1186[0], KL_ARG_V1295_1186[1]])), tail_call(shen_insertx45prologx45variablesx45help, [KL_CTX.KL_LOC_XVx47Y_1189, KL_CTX.KL_LOC_Zx45Y_1190, KL_ARG_V1296_1187])][(-1)]][(-1)]][(-1)] if (shen_consp(KL_ARG_V1295_1186) and tco_apply(kl_variablex63, [KL_ARG_V1295_1186[0]])) else (tail_call(shen_insertx45prologx45variablesx45help, [KL_ARG_V1294_1185, KL_ARG_V1295_1186[1], KL_ARG_V1296_1187]) if shen_consp(KL_ARG_V1295_1186) else (tail_call(shen_sysx45error, [symdic.symdic_shen_insertx45prologx45variablesx45help]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.insert-prolog-variables-help', shen_insertx45prologx45variablesx45help)

@tail_recursion
def shen_initialisex45prolog(KL_ARG_V1297_1191):

    class KL_Context:
        KL_LOC_Vector_1192 = None
        KL_LOC_Counter_1193 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Vector_1192', shen_absvector_set(shen_get(symdic.symdic_shen_x42prologvectorsx42), KL_ARG_V1297_1191, tco_apply(shen_fillvector, [tco_apply(kl_vector, [10]), 1, 10, symdic.symdic_shen_x45nullx45]))), [setattr(KL_CTX, 'KL_LOC_Counter_1193', shen_absvector_set(shen_get(symdic.symdic_shen_x42varcounterx42), KL_ARG_V1297_1191, 1)), KL_ARG_V1297_1191][(-1)]][(-1)]
shen_add_fun('shen.initialise-prolog', shen_initialisex45prolog)


#============================== track.kl==============================



@tail_recursion
def shen_f_error(KL_ARG_V2032_1194):
    global symdic
    return [shen_pr(('partial function ' + tco_apply(shen_app, [KL_ARG_V2032_1194, ';\r\n', symdic.symdic_shen_a])), tco_apply(kl_stoutput, [])), [(tco_apply(shen_trackx45function, [tco_apply(kl_ps, [KL_ARG_V2032_1194])]) if ((not tco_apply(shen_trackedx63, [KL_ARG_V2032_1194])) and tco_apply(kl_yx45orx45nx63, [('track ' + tco_apply(shen_app, [KL_ARG_V2032_1194, '? ', symdic.symdic_shen_a]))])) else symdic.symdic_shen_ok), shen_simple_error('aborted')][(-1)]][(-1)]
shen_add_fun('shen.f_error', shen_f_error)

@tail_recursion
def shen_trackedx63(KL_ARG_V2033_1195):
    global symdic
    return tail_call(kl_elementx63, [KL_ARG_V2033_1195, shen_get(symdic.symdic_shen_x42trackingx42)])
shen_add_fun('shen.tracked?', shen_trackedx63)

@tail_recursion
def kl_track(KL_ARG_V2034_1196):

    class KL_Context:
        KL_LOC_Source_1197 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Source_1197', tco_apply(kl_ps, [KL_ARG_V2034_1196])), tail_call(shen_trackx45function, [KL_CTX.KL_LOC_Source_1197])][(-1)]
shen_add_fun('track', kl_track)

@tail_recursion
def shen_trackx45function(KL_ARG_V2035_1198):

    class KL_Context:
        KL_LOC_KL_1199 = None
        KL_LOC_Ob_1200 = None
        KL_LOC_Tr_1201 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_KL_1199', [symdic.symdic_kl_defun, [KL_ARG_V2035_1198[1][0], [KL_ARG_V2035_1198[1][1][0], [tco_apply(shen_insertx45trackingx45code, [KL_ARG_V2035_1198[1][0], KL_ARG_V2035_1198[1][1][0], KL_ARG_V2035_1198[1][1][1][0]]), []]]]]), [setattr(KL_CTX, 'KL_LOC_Ob_1200', tco_apply(kl_eval, [KL_CTX.KL_LOC_KL_1199])), [setattr(KL_CTX, 'KL_LOC_Tr_1201', shen_set(symdic.symdic_shen_x42trackingx42, [KL_CTX.KL_LOC_Ob_1200, shen_get(symdic.symdic_shen_x42trackingx42)])), KL_CTX.KL_LOC_Ob_1200][(-1)]][(-1)]][(-1)] if (shen_consp(KL_ARG_V2035_1198) and (shen_eq(symdic.symdic_kl_defun, KL_ARG_V2035_1198[0]) and (shen_consp(KL_ARG_V2035_1198[1]) and (shen_consp(KL_ARG_V2035_1198[1][1]) and (shen_consp(KL_ARG_V2035_1198[1][1][1]) and shen_eq([], KL_ARG_V2035_1198[1][1][1][1])))))) else (tail_call(shen_sysx45error, [symdic.symdic_shen_trackx45function]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.track-function', shen_trackx45function)

@tail_recursion
def shen_insertx45trackingx45code(KL_ARG_V2036_1202, KL_ARG_V2037_1203, KL_ARG_V2038_1204):
    global symdic
    return [symdic.symdic_kl_do, [[symdic.symdic_kl_set, [symdic.symdic_shen_x42callx42, [[symdic.symdic_kl_x43, [[symdic.symdic_kl_value, [symdic.symdic_shen_x42callx42, []]], [1, []]]], []]]], [[symdic.symdic_kl_do, [[symdic.symdic_shen_inputx45track, [[symdic.symdic_kl_value, [symdic.symdic_shen_x42callx42, []]], [KL_ARG_V2036_1202, [tco_apply(shen_cons_form, [KL_ARG_V2037_1203]), []]]]], [[symdic.symdic_kl_do, [[symdic.symdic_shen_terprix45orx45readx45char, []], [[symdic.symdic_kl_let, [symdic.symdic_Result, [KL_ARG_V2038_1204, [[symdic.symdic_kl_do, [[symdic.symdic_shen_outputx45track, [[symdic.symdic_kl_value, [symdic.symdic_shen_x42callx42, []]], [KL_ARG_V2036_1202, [symdic.symdic_Result, []]]]], [[symdic.symdic_kl_do, [[symdic.symdic_kl_set, [symdic.symdic_shen_x42callx42, [[symdic.symdic_kl_x45, [[symdic.symdic_kl_value, [symdic.symdic_shen_x42callx42, []]], [1, []]]], []]]], [[symdic.symdic_kl_do, [[symdic.symdic_shen_terprix45orx45readx45char, []], [symdic.symdic_Result, []]]], []]]], []]]], []]]]], []]]], []]]], []]]]
shen_add_fun('shen.insert-tracking-code', shen_insertx45trackingx45code)
shen_set(symdic.symdic_shen_x42stepx42, False)

@tail_recursion
def kl_step(KL_ARG_V2043_1205):
    global symdic
    return (shen_set(symdic.symdic_shen_x42stepx42, True) if shen_eq(symdic.symdic_kl_x43, KL_ARG_V2043_1205) else (shen_set(symdic.symdic_shen_x42stepx42, False) if shen_eq(symdic.symdic_kl_x45, KL_ARG_V2043_1205) else (shen_simple_error('step expects a + or a -.\r\n') if True else shen_simple_error('condition failure'))))
shen_add_fun('step', kl_step)

@tail_recursion
def kl_spy(KL_ARG_V2048_1206):
    global symdic
    return (shen_set(symdic.symdic_shen_x42spyx42, True) if shen_eq(symdic.symdic_kl_x43, KL_ARG_V2048_1206) else (shen_set(symdic.symdic_shen_x42spyx42, False) if shen_eq(symdic.symdic_kl_x45, KL_ARG_V2048_1206) else (shen_simple_error('spy expects a + or a -.\r\n') if True else shen_simple_error('condition failure'))))
shen_add_fun('spy', kl_spy)

@tail_recursion
def shen_terprix45orx45readx45char():
    global symdic
    return (tail_call(shen_checkx45byte, [shen_read_byte(shen_get(symdic.symdic_kl_x42stinputx42))]) if shen_get(symdic.symdic_shen_x42stepx42) else tail_call(kl_nl, [1]))
shen_add_fun('shen.terpri-or-read-char', shen_terprix45orx45readx45char)

@tail_recursion
def shen_checkx45byte(KL_ARG_V2053_1207):
    global symdic
    return (shen_simple_error('aborted') if shen_eq(KL_ARG_V2053_1207, tco_apply(shen_hat, [])) else (True if True else shen_simple_error('condition failure')))
shen_add_fun('shen.check-byte', shen_checkx45byte)

@tail_recursion
def shen_inputx45track(KL_ARG_V2054_1208, KL_ARG_V2055_1209, KL_ARG_V2056_1210):
    global symdic
    return [shen_pr(('\r\n' + tco_apply(shen_app, [tco_apply(shen_spaces, [KL_ARG_V2054_1208]), ('<' + tco_apply(shen_app, [KL_ARG_V2054_1208, ('> Inputs to ' + tco_apply(shen_app, [KL_ARG_V2055_1209, (' \r\n' + tco_apply(shen_app, [tco_apply(shen_spaces, [KL_ARG_V2054_1208]), '', symdic.symdic_shen_a])), symdic.symdic_shen_a])), symdic.symdic_shen_a])), symdic.symdic_shen_a])), tco_apply(kl_stoutput, [])), tail_call(shen_recursivelyx45print, [KL_ARG_V2056_1210])][(-1)]
shen_add_fun('shen.input-track', shen_inputx45track)

@tail_recursion
def shen_recursivelyx45print(KL_ARG_V2057_1211):
    global symdic
    return (shen_pr(' ==>', tco_apply(kl_stoutput, [])) if shen_eq([], KL_ARG_V2057_1211) else ([tco_apply(kl_print, [KL_ARG_V2057_1211[0]]), [shen_pr(', ', tco_apply(kl_stoutput, [])), tail_call(shen_recursivelyx45print, [KL_ARG_V2057_1211[1]])][(-1)]][(-1)] if shen_consp(KL_ARG_V2057_1211) else (tail_call(shen_sysx45error, [symdic.symdic_shen_recursivelyx45print]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.recursively-print', shen_recursivelyx45print)

@tail_recursion
def shen_spaces(KL_ARG_V2058_1212):
    global symdic
    return ('' if shen_eq(0, KL_ARG_V2058_1212) else ((' ' + tco_apply(shen_spaces, [(KL_ARG_V2058_1212 - 1)])) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.spaces', shen_spaces)

@tail_recursion
def shen_outputx45track(KL_ARG_V2059_1213, KL_ARG_V2060_1214, KL_ARG_V2061_1215):
    global symdic
    return shen_pr(('\r\n' + tco_apply(shen_app, [tco_apply(shen_spaces, [KL_ARG_V2059_1213]), ('<' + tco_apply(shen_app, [KL_ARG_V2059_1213, ('> Output from ' + tco_apply(shen_app, [KL_ARG_V2060_1214, (' \r\n' + tco_apply(shen_app, [tco_apply(shen_spaces, [KL_ARG_V2059_1213]), ('==> ' + tco_apply(shen_app, [KL_ARG_V2061_1215, '', symdic.symdic_shen_s])), symdic.symdic_shen_a])), symdic.symdic_shen_a])), symdic.symdic_shen_a])), symdic.symdic_shen_a])), tco_apply(kl_stoutput, []))
shen_add_fun('shen.output-track', shen_outputx45track)

@tail_recursion
def kl_untrack(KL_ARG_V2062_1216):
    global symdic
    return tail_call(kl_eval, [tco_apply(kl_ps, [KL_ARG_V2062_1216])])
shen_add_fun('untrack', kl_untrack)

@tail_recursion
def kl_profile(KL_ARG_V2063_1217):
    global symdic
    return tail_call(shen_profilex45help, [tco_apply(kl_ps, [KL_ARG_V2063_1217])])
shen_add_fun('profile', kl_profile)

@tail_recursion
def shen_profilex45help(KL_ARG_V2068_1218):

    class KL_Context:
        KL_LOC_G_1219 = None
        KL_LOC_Profile_1220 = None
        KL_LOC_Def_1221 = None
        KL_LOC_CompileProfile_1222 = None
        KL_LOC_CompileG_1223 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_G_1219', tco_apply(kl_gensym, [symdic.symdic_shen_f])), [setattr(KL_CTX, 'KL_LOC_Profile_1220', [symdic.symdic_kl_defun, [KL_ARG_V2068_1218[1][0], [KL_ARG_V2068_1218[1][1][0], [tco_apply(shen_profilex45func, [KL_ARG_V2068_1218[1][0], KL_ARG_V2068_1218[1][1][0], [KL_CTX.KL_LOC_G_1219, KL_ARG_V2068_1218[1][1][0]]]), []]]]]), [setattr(KL_CTX, 'KL_LOC_Def_1221', [symdic.symdic_kl_defun, [KL_CTX.KL_LOC_G_1219, [KL_ARG_V2068_1218[1][1][0], [tco_apply(kl_subst, [KL_CTX.KL_LOC_G_1219, KL_ARG_V2068_1218[1][0], KL_ARG_V2068_1218[1][1][1][0]]), []]]]]), [setattr(KL_CTX, 'KL_LOC_CompileProfile_1222', tco_apply(shen_evalx45withoutx45macros, [KL_CTX.KL_LOC_Profile_1220])), [setattr(KL_CTX, 'KL_LOC_CompileG_1223', tco_apply(shen_evalx45withoutx45macros, [KL_CTX.KL_LOC_Def_1221])), KL_ARG_V2068_1218[1][0]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)] if (shen_consp(KL_ARG_V2068_1218) and (shen_eq(symdic.symdic_kl_defun, KL_ARG_V2068_1218[0]) and (shen_consp(KL_ARG_V2068_1218[1]) and (shen_consp(KL_ARG_V2068_1218[1][1]) and (shen_consp(KL_ARG_V2068_1218[1][1][1]) and shen_eq([], KL_ARG_V2068_1218[1][1][1][1])))))) else (shen_simple_error('Cannot profile.\r\n') if True else shen_simple_error('condition failure')))
shen_add_fun('shen.profile-help', shen_profilex45help)

@tail_recursion
def kl_unprofile(KL_ARG_V2069_1224):
    global symdic
    return tail_call(kl_untrack, [KL_ARG_V2069_1224])
shen_add_fun('unprofile', kl_unprofile)

@tail_recursion
def shen_profilex45func(KL_ARG_V2070_1225, KL_ARG_V2071_1226, KL_ARG_V2072_1227):
    global symdic
    return [symdic.symdic_kl_let, [symdic.symdic_Start, [[symdic.symdic_kl_getx45time, [symdic.symdic_kl_run, []]], [[symdic.symdic_kl_let, [symdic.symdic_Result, [KL_ARG_V2072_1227, [[symdic.symdic_kl_let, [symdic.symdic_Finish, [[symdic.symdic_kl_x45, [[symdic.symdic_kl_getx45time, [symdic.symdic_kl_run, []]], [symdic.symdic_Start, []]]], [[symdic.symdic_kl_let, [symdic.symdic_Record, [[symdic.symdic_shen_putx45profile, [KL_ARG_V2070_1225, [[symdic.symdic_kl_x43, [[symdic.symdic_shen_getx45profile, [KL_ARG_V2070_1225, []]], [symdic.symdic_Finish, []]]], []]]], [symdic.symdic_Result, []]]]], []]]]], []]]]], []]]]]
shen_add_fun('shen.profile-func', shen_profilex45func)

@tail_recursion
def kl_profilex45results(KL_ARG_V2073_1228):

    class KL_Context:
        KL_LOC_Results_1229 = None
        KL_LOC_Initialise_1230 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Results_1229', tco_apply(shen_getx45profile, [KL_ARG_V2073_1228])), [setattr(KL_CTX, 'KL_LOC_Initialise_1230', tco_apply(shen_putx45profile, [KL_ARG_V2073_1228, 0])), tail_call(kl_x64p, [KL_ARG_V2073_1228, KL_CTX.KL_LOC_Results_1229])][(-1)]][(-1)]
shen_add_fun('profile-results', kl_profilex45results)

@tail_recursion
def shen_getx45profile(KL_ARG_V2074_1231):
    global symdic
    return shen_try_except((lambda : tco_apply(kl_get, [KL_ARG_V2074_1231, symdic.symdic_kl_profile, shen_get(symdic.symdic_kl_x42propertyx45vectorx42)])), (lambda KL_ARG_E_1232: 0))
shen_add_fun('shen.get-profile', shen_getx45profile)

@tail_recursion
def shen_putx45profile(KL_ARG_V2075_1233, KL_ARG_V2076_1234):
    global symdic
    return tail_call(kl_put, [KL_ARG_V2075_1233, symdic.symdic_kl_profile, KL_ARG_V2076_1234, shen_get(symdic.symdic_kl_x42propertyx45vectorx42)])
shen_add_fun('shen.put-profile', shen_putx45profile)


#============================== load.kl==============================



@tail_recursion
def kl_load(KL_ARG_V808_1235):

    class KL_Context:
        KL_LOC_Load_1236 = None
        KL_LOC_Start_1237 = None
        KL_LOC_Result_1238 = None
        KL_LOC_Finish_1239 = None
        KL_LOC_Time_1240 = None
        KL_LOC_Message_1241 = None
        KL_LOC_Infs_1242 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Load_1236', [setattr(KL_CTX, 'KL_LOC_Start_1237', shen_get_time(symdic.symdic_kl_run)), [setattr(KL_CTX, 'KL_LOC_Result_1238', tco_apply(shen_loadx45help, [shen_get(symdic.symdic_shen_x42tcx42), tco_apply(kl_readx45file, [KL_ARG_V808_1235])])), [setattr(KL_CTX, 'KL_LOC_Finish_1239', shen_get_time(symdic.symdic_kl_run)), [setattr(KL_CTX, 'KL_LOC_Time_1240', (KL_CTX.KL_LOC_Finish_1239 - KL_CTX.KL_LOC_Start_1237)), [setattr(KL_CTX, 'KL_LOC_Message_1241', shen_pr(('\r\nrun time: ' + (str(KL_CTX.KL_LOC_Time_1240) + ' secs\r\n')), tco_apply(kl_stoutput, []))), KL_CTX.KL_LOC_Result_1238][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]), [setattr(KL_CTX, 'KL_LOC_Infs_1242', (shen_pr(('\r\ntypechecked in ' + tco_apply(shen_app, [tco_apply(kl_inferences, []), ' inferences\r\n', symdic.symdic_shen_a])), tco_apply(kl_stoutput, [])) if shen_get(symdic.symdic_shen_x42tcx42) else symdic.symdic_shen_skip)), symdic.symdic_kl_loaded][(-1)]][(-1)]
shen_add_fun('load', kl_load)

@tail_recursion
def shen_loadx45help(KL_ARG_V813_1243, KL_ARG_V814_1244):

    class KL_Context:
        KL_LOC_RemoveSynonyms_1246 = None
        KL_LOC_Table_1247 = None
        KL_LOC_Assume_1248 = None
    KL_CTX = KL_Context()
    global symdic
    return (tail_call(kl_map, [(lambda KL_ARG_X_1245: shen_pr(tco_apply(shen_app, [tco_apply(shen_evalx45withoutx45macros, [KL_ARG_X_1245]), '\r\n', symdic.symdic_shen_s]), tco_apply(kl_stoutput, []))), KL_ARG_V814_1244]) if shen_eq(False, KL_ARG_V813_1243) else ([setattr(KL_CTX, 'KL_LOC_RemoveSynonyms_1246', tco_apply(kl_mapcan, [symdic.symdic_shen_removex45synonyms, KL_ARG_V814_1244])), [setattr(KL_CTX, 'KL_LOC_Table_1247', tco_apply(kl_mapcan, [symdic.symdic_shen_typetable, KL_CTX.KL_LOC_RemoveSynonyms_1246])), [setattr(KL_CTX, 'KL_LOC_Assume_1248', tco_apply(kl_map, [symdic.symdic_shen_assumetype, KL_CTX.KL_LOC_Table_1247])), shen_try_except((lambda : tco_apply(kl_map, [symdic.symdic_shen_typecheckx45andx45load, KL_CTX.KL_LOC_RemoveSynonyms_1246])), (lambda KL_ARG_E_1249: tail_call(shen_unwindx45types, [KL_ARG_E_1249, KL_CTX.KL_LOC_Table_1247])))][(-1)]][(-1)]][(-1)] if True else shen_simple_error('condition failure')))
shen_add_fun('shen.load-help', shen_loadx45help)

@tail_recursion
def shen_removex45synonyms(KL_ARG_V815_1250):
    global symdic
    return ([tco_apply(kl_eval, [KL_ARG_V815_1250]), []][(-1)] if (shen_consp(KL_ARG_V815_1250) and shen_eq(symdic.symdic_shen_synonymsx45help, KL_ARG_V815_1250[0])) else ([KL_ARG_V815_1250, []] if True else shen_simple_error('condition failure')))
shen_add_fun('shen.remove-synonyms', shen_removex45synonyms)

@tail_recursion
def shen_typecheckx45andx45load(KL_ARG_V816_1251):
    global symdic
    return [tco_apply(kl_nl, [1]), tail_call(shen_typecheckx45andx45evaluate, [KL_ARG_V816_1251, tco_apply(kl_gensym, [symdic.symdic_A])])][(-1)]
shen_add_fun('shen.typecheck-and-load', shen_typecheckx45andx45load)

@tail_recursion
def shen_typetable(KL_ARG_V825_1252):

    class KL_Context:
        KL_LOC_Sig_1253 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_Sig_1253', tco_apply(kl_compile, [symdic.symdic_shen_x60sigx43restx62, KL_ARG_V825_1252[1][1], []])), (shen_simple_error(tco_apply(shen_app, [KL_ARG_V825_1252[1][0], ' lacks a proper signature.\r\n', symdic.symdic_shen_a])) if shen_eq(KL_CTX.KL_LOC_Sig_1253, tco_apply(kl_fail, [])) else [[KL_ARG_V825_1252[1][0], KL_CTX.KL_LOC_Sig_1253], []])][(-1)] if (shen_consp(KL_ARG_V825_1252) and (shen_eq(symdic.symdic_kl_define, KL_ARG_V825_1252[0]) and shen_consp(KL_ARG_V825_1252[1]))) else ([[KL_ARG_V825_1252[1][0], [KL_ARG_V825_1252[1][1][1][0], [symdic.symdic_kl_x61x61x62, [KL_ARG_V825_1252[1][1][1][1][1][0], []]]]], []] if (shen_consp(KL_ARG_V825_1252) and (shen_eq(symdic.symdic_kl_defcc, KL_ARG_V825_1252[0]) and (shen_consp(KL_ARG_V825_1252[1]) and (shen_consp(KL_ARG_V825_1252[1][1]) and (shen_eq(symdic.symdic_kl_x123, KL_ARG_V825_1252[1][1][0]) and (shen_consp(KL_ARG_V825_1252[1][1][1]) and (shen_consp(KL_ARG_V825_1252[1][1][1][0]) and (shen_eq(symdic.symdic_kl_list, KL_ARG_V825_1252[1][1][1][0][0]) and (shen_consp(KL_ARG_V825_1252[1][1][1][0][1]) and (shen_eq([], KL_ARG_V825_1252[1][1][1][0][1][1]) and (shen_consp(KL_ARG_V825_1252[1][1][1][1]) and (shen_eq(symdic.symdic_kl_x61x61x62, KL_ARG_V825_1252[1][1][1][1][0]) and (shen_consp(KL_ARG_V825_1252[1][1][1][1][1]) and (shen_consp(KL_ARG_V825_1252[1][1][1][1][1][1]) and shen_eq(symdic.symdic_kl_x125, KL_ARG_V825_1252[1][1][1][1][1][1][0]))))))))))))))) else (shen_simple_error(tco_apply(shen_app, [KL_ARG_V825_1252[1][0], ' lacks a proper signature.\r\n', symdic.symdic_shen_a])) if (shen_consp(KL_ARG_V825_1252) and (shen_eq(symdic.symdic_kl_defcc, KL_ARG_V825_1252[0]) and shen_consp(KL_ARG_V825_1252[1]))) else ([] if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.typetable', shen_typetable)

@tail_recursion
def shen_assumetype(KL_ARG_V826_1254):
    global symdic
    return (apply(kl_declare, [KL_ARG_V826_1254[0], KL_ARG_V826_1254[1]]) if shen_consp(KL_ARG_V826_1254) else (tail_call(shen_sysx45error, [symdic.symdic_shen_assumetype]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.assumetype', shen_assumetype)

@tail_recursion
def shen_unwindx45types(KL_ARG_V831_1255, KL_ARG_V832_1256):
    global symdic
    return (shen_simple_error(KL_ARG_V831_1255.message) if shen_eq([], KL_ARG_V832_1256) else ([tco_apply(shen_remtype, [KL_ARG_V832_1256[0][0]]), tail_call(shen_unwindx45types, [KL_ARG_V831_1255, KL_ARG_V832_1256[1]])][(-1)] if (shen_consp(KL_ARG_V832_1256) and shen_consp(KL_ARG_V832_1256[0])) else (tail_call(shen_sysx45error, [symdic.symdic_shen_unwindx45types]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.unwind-types', shen_unwindx45types)

@tail_recursion
def shen_remtype(KL_ARG_V833_1257):
    global symdic
    return [shen_set(symdic.symdic_shen_x42signedfuncsx42, tco_apply(kl_remove, [KL_ARG_V833_1257, shen_get(symdic.symdic_shen_x42signedfuncsx42)])), KL_ARG_V833_1257][(-1)]
shen_add_fun('shen.remtype', shen_remtype)

@tail_recursion
def shen_x60sigx43restx62(KL_ARG_V838_1258):

    class KL_Context:
        KL_LOC_Result_1259 = None
        KL_LOC_Parse_shen_x60signaturex62_1260 = None
        KL_LOC_Parse_shen_x60anyx62_1261 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_1259', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60signaturex62_1260', tco_apply(shen_x60signaturex62, [KL_ARG_V838_1258])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60anyx62_1261', tco_apply(shen_x60anyx62, [KL_CTX.KL_LOC_Parse_shen_x60signaturex62_1260])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60anyx62_1261[0], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60signaturex62_1260])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60anyx62_1261)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60signaturex62_1260)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_1259, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_1259)][(-1)]
shen_add_fun('shen.<sig+rest>', shen_x60sigx43restx62)

@tail_recursion
def kl_writex45tox45file(KL_ARG_V839_1262, KL_ARG_V840_1263):

    class KL_Context:
        KL_LOC_Stream_1264 = None
        KL_LOC_String_1265 = None
        KL_LOC_Write_1266 = None
        KL_LOC_Close_1267 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Stream_1264', shen_open(symdic.symdic_kl_file, KL_ARG_V839_1262, symdic.symdic_kl_out)), [setattr(KL_CTX, 'KL_LOC_String_1265', (tco_apply(shen_app, [KL_ARG_V840_1263, '\r\n\r\n', symdic.symdic_shen_a]) if isinstance(KL_ARG_V840_1263, str) else tco_apply(shen_app, [KL_ARG_V840_1263, '\r\n\r\n', symdic.symdic_shen_s]))), [setattr(KL_CTX, 'KL_LOC_Write_1266', shen_pr(KL_CTX.KL_LOC_String_1265, KL_CTX.KL_LOC_Stream_1264)), [setattr(KL_CTX, 'KL_LOC_Close_1267', shen_close(KL_CTX.KL_LOC_Stream_1264)), KL_ARG_V840_1263][(-1)]][(-1)]][(-1)]][(-1)]
shen_add_fun('write-to-file', kl_writex45tox45file)


#============================== writer.kl==============================



@tail_recursion
def kl_print(KL_ARG_V2179_1268):

    class KL_Context:
        KL_LOC_String_1269 = None
        KL_LOC_Print_1270 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_String_1269', tco_apply(shen_insert, [KL_ARG_V2179_1268, '~S'])), [setattr(KL_CTX, 'KL_LOC_Print_1270', shen_pr(KL_CTX.KL_LOC_String_1269, tco_apply(kl_stoutput, []))), KL_ARG_V2179_1268][(-1)]][(-1)]
shen_add_fun('print', kl_print)

@tail_recursion
def shen_mkstr(KL_ARG_V2180_1271, KL_ARG_V2181_1272):
    global symdic
    return (tail_call(shen_mkstrx45l, [tco_apply(shen_procx45nl, [KL_ARG_V2180_1271]), KL_ARG_V2181_1272]) if isinstance(KL_ARG_V2180_1271, str) else (tail_call(shen_mkstrx45r, [[symdic.symdic_shen_procx45nl, [KL_ARG_V2180_1271, []]], KL_ARG_V2181_1272]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.mkstr', shen_mkstr)

@tail_recursion
def shen_mkstrx45l(KL_ARG_V2182_1273, KL_ARG_V2183_1274):
    global symdic
    return (KL_ARG_V2182_1273 if shen_eq([], KL_ARG_V2183_1274) else (tail_call(shen_mkstrx45l, [tco_apply(shen_insertx45l, [KL_ARG_V2183_1274[0], KL_ARG_V2182_1273]), KL_ARG_V2183_1274[1]]) if shen_consp(KL_ARG_V2183_1274) else (tail_call(shen_sysx45error, [symdic.symdic_shen_mkstrx45l]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.mkstr-l', shen_mkstrx45l)

@tail_recursion
def shen_insertx45l(KL_ARG_V2186_1275, KL_ARG_V2187_1276):
    global symdic
    return ('' if shen_eq('', KL_ARG_V2187_1276) else ([symdic.symdic_shen_app, [KL_ARG_V2186_1275, [KL_ARG_V2187_1276[1:][1:], [symdic.symdic_shen_a, []]]]] if (tco_apply(shen_x43stringx63, [KL_ARG_V2187_1276]) and (shen_eq('~', KL_ARG_V2187_1276[0]) and (tco_apply(shen_x43stringx63, [KL_ARG_V2187_1276[1:]]) and shen_eq('A', KL_ARG_V2187_1276[1:][0])))) else ([symdic.symdic_shen_app, [KL_ARG_V2186_1275, [KL_ARG_V2187_1276[1:][1:], [symdic.symdic_shen_r, []]]]] if (tco_apply(shen_x43stringx63, [KL_ARG_V2187_1276]) and (shen_eq('~', KL_ARG_V2187_1276[0]) and (tco_apply(shen_x43stringx63, [KL_ARG_V2187_1276[1:]]) and shen_eq('R', KL_ARG_V2187_1276[1:][0])))) else ([symdic.symdic_shen_app, [KL_ARG_V2186_1275, [KL_ARG_V2187_1276[1:][1:], [symdic.symdic_shen_s, []]]]] if (tco_apply(shen_x43stringx63, [KL_ARG_V2187_1276]) and (shen_eq('~', KL_ARG_V2187_1276[0]) and (tco_apply(shen_x43stringx63, [KL_ARG_V2187_1276[1:]]) and shen_eq('S', KL_ARG_V2187_1276[1:][0])))) else (tail_call(shen_factorx45cn, [[symdic.symdic_kl_cn, [KL_ARG_V2187_1276[0], [tco_apply(shen_insertx45l, [KL_ARG_V2186_1275, KL_ARG_V2187_1276[1:]]), []]]]]) if tco_apply(shen_x43stringx63, [KL_ARG_V2187_1276]) else ([symdic.symdic_kl_cn, [KL_ARG_V2187_1276[1][0], [tco_apply(shen_insertx45l, [KL_ARG_V2186_1275, KL_ARG_V2187_1276[1][1][0]]), []]]] if (shen_consp(KL_ARG_V2187_1276) and (shen_eq(symdic.symdic_kl_cn, KL_ARG_V2187_1276[0]) and (shen_consp(KL_ARG_V2187_1276[1]) and (shen_consp(KL_ARG_V2187_1276[1][1]) and shen_eq([], KL_ARG_V2187_1276[1][1][1]))))) else ([symdic.symdic_shen_app, [KL_ARG_V2187_1276[1][0], [tco_apply(shen_insertx45l, [KL_ARG_V2186_1275, KL_ARG_V2187_1276[1][1][0]]), KL_ARG_V2187_1276[1][1][1]]]] if (shen_consp(KL_ARG_V2187_1276) and (shen_eq(symdic.symdic_shen_app, KL_ARG_V2187_1276[0]) and (shen_consp(KL_ARG_V2187_1276[1]) and (shen_consp(KL_ARG_V2187_1276[1][1]) and (shen_consp(KL_ARG_V2187_1276[1][1][1]) and shen_eq([], KL_ARG_V2187_1276[1][1][1][1])))))) else (tail_call(shen_sysx45error, [symdic.symdic_shen_insertx45l]) if True else shen_simple_error('condition failure')))))))))
shen_add_fun('shen.insert-l', shen_insertx45l)

@tail_recursion
def shen_factorx45cn(KL_ARG_V2188_1277):
    global symdic
    return ([symdic.symdic_kl_cn, [(KL_ARG_V2188_1277[1][0] + KL_ARG_V2188_1277[1][1][0][1][0]), KL_ARG_V2188_1277[1][1][0][1][1]]] if (shen_consp(KL_ARG_V2188_1277) and (shen_eq(symdic.symdic_kl_cn, KL_ARG_V2188_1277[0]) and (shen_consp(KL_ARG_V2188_1277[1]) and (shen_consp(KL_ARG_V2188_1277[1][1]) and (shen_consp(KL_ARG_V2188_1277[1][1][0]) and (shen_eq(symdic.symdic_kl_cn, KL_ARG_V2188_1277[1][1][0][0]) and (shen_consp(KL_ARG_V2188_1277[1][1][0][1]) and (shen_consp(KL_ARG_V2188_1277[1][1][0][1][1]) and (shen_eq([], KL_ARG_V2188_1277[1][1][0][1][1][1]) and (shen_eq([], KL_ARG_V2188_1277[1][1][1]) and (isinstance(KL_ARG_V2188_1277[1][0], str) and isinstance(KL_ARG_V2188_1277[1][1][0][1][0], str)))))))))))) else (KL_ARG_V2188_1277 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.factor-cn', shen_factorx45cn)

@tail_recursion
def shen_procx45nl(KL_ARG_V2189_1278):
    global symdic
    return ('' if shen_eq('', KL_ARG_V2189_1278) else ((chr(10) + tco_apply(shen_procx45nl, [KL_ARG_V2189_1278[1:][1:]])) if (tco_apply(shen_x43stringx63, [KL_ARG_V2189_1278]) and (shen_eq('~', KL_ARG_V2189_1278[0]) and (tco_apply(shen_x43stringx63, [KL_ARG_V2189_1278[1:]]) and shen_eq('%', KL_ARG_V2189_1278[1:][0])))) else ((KL_ARG_V2189_1278[0] + tco_apply(shen_procx45nl, [KL_ARG_V2189_1278[1:]])) if tco_apply(shen_x43stringx63, [KL_ARG_V2189_1278]) else (tail_call(shen_sysx45error, [symdic.symdic_shen_procx45nl]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.proc-nl', shen_procx45nl)

@tail_recursion
def shen_mkstrx45r(KL_ARG_V2190_1279, KL_ARG_V2191_1280):
    global symdic
    return (KL_ARG_V2190_1279 if shen_eq([], KL_ARG_V2191_1280) else (tail_call(shen_mkstrx45r, [[symdic.symdic_shen_insert, [KL_ARG_V2191_1280[0], [KL_ARG_V2190_1279, []]]], KL_ARG_V2191_1280[1]]) if shen_consp(KL_ARG_V2191_1280) else (tail_call(shen_sysx45error, [symdic.symdic_shen_mkstrx45r]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.mkstr-r', shen_mkstrx45r)

@tail_recursion
def shen_insert(KL_ARG_V2192_1281, KL_ARG_V2193_1282):
    global symdic
    return tail_call(shen_insertx45h, [KL_ARG_V2192_1281, KL_ARG_V2193_1282, ''])
shen_add_fun('shen.insert', shen_insert)

@tail_recursion
def shen_insertx45h(KL_ARG_V2196_1283, KL_ARG_V2197_1284, KL_ARG_V2198_1285):
    global symdic
    return (KL_ARG_V2198_1285 if shen_eq('', KL_ARG_V2197_1284) else ((KL_ARG_V2198_1285 + tco_apply(shen_app, [KL_ARG_V2196_1283, KL_ARG_V2197_1284[1:][1:], symdic.symdic_shen_a])) if (tco_apply(shen_x43stringx63, [KL_ARG_V2197_1284]) and (shen_eq('~', KL_ARG_V2197_1284[0]) and (tco_apply(shen_x43stringx63, [KL_ARG_V2197_1284[1:]]) and shen_eq('A', KL_ARG_V2197_1284[1:][0])))) else ((KL_ARG_V2198_1285 + tco_apply(shen_app, [KL_ARG_V2196_1283, KL_ARG_V2197_1284[1:][1:], symdic.symdic_shen_r])) if (tco_apply(shen_x43stringx63, [KL_ARG_V2197_1284]) and (shen_eq('~', KL_ARG_V2197_1284[0]) and (tco_apply(shen_x43stringx63, [KL_ARG_V2197_1284[1:]]) and shen_eq('R', KL_ARG_V2197_1284[1:][0])))) else ((KL_ARG_V2198_1285 + tco_apply(shen_app, [KL_ARG_V2196_1283, KL_ARG_V2197_1284[1:][1:], symdic.symdic_shen_s])) if (tco_apply(shen_x43stringx63, [KL_ARG_V2197_1284]) and (shen_eq('~', KL_ARG_V2197_1284[0]) and (tco_apply(shen_x43stringx63, [KL_ARG_V2197_1284[1:]]) and shen_eq('S', KL_ARG_V2197_1284[1:][0])))) else (tail_call(shen_insertx45h, [KL_ARG_V2196_1283, KL_ARG_V2197_1284[1:], (KL_ARG_V2198_1285 + KL_ARG_V2197_1284[0])]) if tco_apply(shen_x43stringx63, [KL_ARG_V2197_1284]) else (tail_call(shen_sysx45error, [symdic.symdic_shen_insertx45h]) if True else shen_simple_error('condition failure')))))))
shen_add_fun('shen.insert-h', shen_insertx45h)

@tail_recursion
def shen_app(KL_ARG_V2199_1286, KL_ARG_V2200_1287, KL_ARG_V2201_1288):
    global symdic
    return (tco_apply(shen_argx45x62str, [KL_ARG_V2199_1286, KL_ARG_V2201_1288]) + KL_ARG_V2200_1287)
shen_add_fun('shen.app', shen_app)

@tail_recursion
def shen_argx45x62str(KL_ARG_V2207_1289, KL_ARG_V2208_1290):
    global symdic
    return ('...' if shen_eq(KL_ARG_V2207_1289, tco_apply(kl_fail, [])) else (tail_call(shen_listx45x62str, [KL_ARG_V2207_1289, KL_ARG_V2208_1290]) if tco_apply(shen_listx63, [KL_ARG_V2207_1289]) else (tail_call(shen_strx45x62str, [KL_ARG_V2207_1289, KL_ARG_V2208_1290]) if isinstance(KL_ARG_V2207_1289, str) else (tail_call(shen_vectorx45x62str, [KL_ARG_V2207_1289, KL_ARG_V2208_1290]) if shen_absvectorp(KL_ARG_V2207_1289) else (tail_call(shen_atomx45x62str, [KL_ARG_V2207_1289]) if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.arg->str', shen_argx45x62str)

@tail_recursion
def shen_listx45x62str(KL_ARG_V2209_1291, KL_ARG_V2210_1292):
    global symdic
    return (tail_call(kl_x64s, ['(', tco_apply(kl_x64s, [tco_apply(shen_iterx45list, [KL_ARG_V2209_1291, symdic.symdic_shen_r, tco_apply(shen_maxseq, [])]), ')'])]) if shen_eq(symdic.symdic_shen_r, KL_ARG_V2210_1292) else (tail_call(kl_x64s, ['[', tco_apply(kl_x64s, [tco_apply(shen_iterx45list, [KL_ARG_V2209_1291, KL_ARG_V2210_1292, tco_apply(shen_maxseq, [])]), ']'])]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.list->str', shen_listx45x62str)

@tail_recursion
def shen_maxseq():
    global symdic
    return shen_get(symdic.symdic_kl_x42maximumx45printx45sequencex45sizex42)
shen_add_fun('shen.maxseq', shen_maxseq)

@tail_recursion
def shen_iterx45list(KL_ARG_V2221_1293, KL_ARG_V2222_1294, KL_ARG_V2223_1295):
    global symdic
    return ('' if shen_eq([], KL_ARG_V2221_1293) else ('... etc' if shen_eq(0, KL_ARG_V2223_1295) else (tail_call(shen_argx45x62str, [KL_ARG_V2221_1293[0], KL_ARG_V2222_1294]) if (shen_consp(KL_ARG_V2221_1293) and shen_eq([], KL_ARG_V2221_1293[1])) else (tail_call(kl_x64s, [tco_apply(shen_argx45x62str, [KL_ARG_V2221_1293[0], KL_ARG_V2222_1294]), tco_apply(kl_x64s, [' ', tco_apply(shen_iterx45list, [KL_ARG_V2221_1293[1], KL_ARG_V2222_1294, (KL_ARG_V2223_1295 - 1)])])]) if shen_consp(KL_ARG_V2221_1293) else (tail_call(kl_x64s, [' ', tco_apply(kl_x64s, ['|', tco_apply(kl_x64s, [' ', tco_apply(shen_argx45x62str, [KL_ARG_V2221_1293, KL_ARG_V2222_1294])])])]) if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.iter-list', shen_iterx45list)

@tail_recursion
def shen_strx45x62str(KL_ARG_V2228_1296, KL_ARG_V2229_1297):
    global symdic
    return (KL_ARG_V2228_1296 if shen_eq(symdic.symdic_shen_a, KL_ARG_V2229_1297) else (tail_call(kl_x64s, [chr(34), tco_apply(kl_x64s, [KL_ARG_V2228_1296, chr(34)])]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.str->str', shen_strx45x62str)

@tail_recursion
def shen_vectorx45x62str(KL_ARG_V2230_1298, KL_ARG_V2231_1299):
    global symdic
    return (tail_call(shen_absvector_get(KL_ARG_V2230_1298, 0), [KL_ARG_V2230_1298]) if tco_apply(shen_printx45vectorx63, [KL_ARG_V2230_1298]) else (tail_call(kl_x64s, ['<', tco_apply(kl_x64s, [tco_apply(shen_iterx45vector, [KL_ARG_V2230_1298, 1, KL_ARG_V2231_1299, tco_apply(shen_maxseq, [])]), '>'])]) if tco_apply(kl_vectorx63, [KL_ARG_V2230_1298]) else tail_call(kl_x64s, ['<', tco_apply(kl_x64s, ['<', tco_apply(kl_x64s, [tco_apply(shen_iterx45vector, [KL_ARG_V2230_1298, 0, KL_ARG_V2231_1299, tco_apply(shen_maxseq, [])]), '>>'])])])))
shen_add_fun('shen.vector->str', shen_vectorx45x62str)

@tail_recursion
def shen_printx45vectorx63(KL_ARG_V2232_1300):

    class KL_Context:
        KL_LOC_Zero_1301 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Zero_1301', shen_absvector_get(KL_ARG_V2232_1300, 0)), (True if shen_eq(KL_CTX.KL_LOC_Zero_1301, symdic.symdic_shen_tuple) else (True if shen_eq(KL_CTX.KL_LOC_Zero_1301, symdic.symdic_shen_pvar) else (tail_call(shen_fboundx63, [KL_CTX.KL_LOC_Zero_1301]) if (not isinstance(KL_CTX.KL_LOC_Zero_1301, numbers.Number)) else False)))][(-1)]
shen_add_fun('shen.print-vector?', shen_printx45vectorx63)

@tail_recursion
def shen_fboundx63(KL_ARG_V2233_1302):
    global symdic
    return shen_try_except((lambda : [tco_apply(kl_ps, [KL_ARG_V2233_1302]), True][(-1)]), (lambda KL_ARG_E_1303: False))
shen_add_fun('shen.fbound?', shen_fboundx63)

@tail_recursion
def shen_tuple(KL_ARG_V2234_1304):
    global symdic
    return ('(@p ' + tco_apply(shen_app, [shen_absvector_get(KL_ARG_V2234_1304, 1), (' ' + tco_apply(shen_app, [shen_absvector_get(KL_ARG_V2234_1304, 2), ')', symdic.symdic_shen_s])), symdic.symdic_shen_s]))
shen_add_fun('shen.tuple', shen_tuple)

@tail_recursion
def shen_iterx45vector(KL_ARG_V2241_1305, KL_ARG_V2242_1306, KL_ARG_V2243_1307, KL_ARG_V2244_1308):

    class KL_Context:
        KL_LOC_Item_1309 = None
        KL_LOC_Next_1311 = None
    KL_CTX = KL_Context()
    global symdic
    return ('... etc' if shen_eq(0, KL_ARG_V2244_1308) else ([setattr(KL_CTX, 'KL_LOC_Item_1309', shen_try_except((lambda : shen_absvector_get(KL_ARG_V2241_1305, KL_ARG_V2242_1306)), (lambda KL_ARG_E_1310: symdic.symdic_shen_outx45ofx45bounds))), [setattr(KL_CTX, 'KL_LOC_Next_1311', shen_try_except((lambda : shen_absvector_get(KL_ARG_V2241_1305, (KL_ARG_V2242_1306 + 1))), (lambda KL_ARG_E_1312: symdic.symdic_shen_outx45ofx45bounds))), ('' if shen_eq(KL_CTX.KL_LOC_Item_1309, symdic.symdic_shen_outx45ofx45bounds) else (tail_call(shen_argx45x62str, [KL_CTX.KL_LOC_Item_1309, KL_ARG_V2243_1307]) if shen_eq(KL_CTX.KL_LOC_Next_1311, symdic.symdic_shen_outx45ofx45bounds) else tail_call(kl_x64s, [tco_apply(shen_argx45x62str, [KL_CTX.KL_LOC_Item_1309, KL_ARG_V2243_1307]), tco_apply(kl_x64s, [' ', tco_apply(shen_iterx45vector, [KL_ARG_V2241_1305, (KL_ARG_V2242_1306 + 1), KL_ARG_V2243_1307, (KL_ARG_V2244_1308 - 1)])])])))][(-1)]][(-1)] if True else shen_simple_error('condition failure')))
shen_add_fun('shen.iter-vector', shen_iterx45vector)

@tail_recursion
def shen_atomx45x62str(KL_ARG_V2245_1313):
    global symdic
    return shen_try_except((lambda : str(KL_ARG_V2245_1313)), (lambda KL_ARG_E_1314: tail_call(shen_funexstring, [])))
shen_add_fun('shen.atom->str', shen_atomx45x62str)

@tail_recursion
def shen_funexstring():
    global symdic
    return tail_call(kl_x64s, ['\x10', tco_apply(kl_x64s, ['f', tco_apply(kl_x64s, ['u', tco_apply(kl_x64s, ['n', tco_apply(kl_x64s, ['e', tco_apply(kl_x64s, [tco_apply(shen_argx45x62str, [tco_apply(kl_gensym, [shen_intern('x')]), symdic.symdic_shen_a]), '\x11'])])])])])])
shen_add_fun('shen.funexstring', shen_funexstring)

@tail_recursion
def shen_listx63(KL_ARG_V2246_1315):
    global symdic
    return (tco_apply(kl_emptyx63, [KL_ARG_V2246_1315]) or shen_consp(KL_ARG_V2246_1315))
shen_add_fun('shen.list?', shen_listx63)


#============================== macros.kl==============================



@tail_recursion
def kl_macroexpand(KL_ARG_V841_1316):

    class KL_Context:
        KL_LOC_Y_1317 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Y_1317', tco_apply(shen_compose, [shen_get(symdic.symdic_kl_x42macrosx42), KL_ARG_V841_1316])), (KL_ARG_V841_1316 if shen_eq(KL_ARG_V841_1316, KL_CTX.KL_LOC_Y_1317) else tail_call(shen_walk, [symdic.symdic_kl_macroexpand, KL_CTX.KL_LOC_Y_1317]))][(-1)]
shen_add_fun('macroexpand', kl_macroexpand)
shen_set(symdic.symdic_kl_x42macrosx42, [symdic.symdic_shen_timerx45macro, [symdic.symdic_shen_casesx45macro, [symdic.symdic_shen_absx45macro, [symdic.symdic_shen_putx47getx45macro, [symdic.symdic_shen_compilex45macro, [symdic.symdic_shen_datatypex45macro, [symdic.symdic_shen_letx45macro, [symdic.symdic_shen_assocx45macro, [symdic.symdic_shen_makex45stringx45macro, [symdic.symdic_shen_outputx45macro, [symdic.symdic_shen_errorx45macro, [symdic.symdic_shen_prologx45macro, [symdic.symdic_shen_synonymsx45macro, [symdic.symdic_shen_nlx45macro, [symdic.symdic_shen_x64sx45macro, [symdic.symdic_shen_defmacrox45macro, [symdic.symdic_shen_defprologx45macro, [symdic.symdic_shen_functionx45macro, []]]]]]]]]]]]]]]]]]])

@tail_recursion
def shen_errorx45macro(KL_ARG_V842_1318):
    global symdic
    return ([symdic.symdic_kl_simplex45error, [tco_apply(shen_mkstr, [KL_ARG_V842_1318[1][0], KL_ARG_V842_1318[1][1]]), []]] if (shen_consp(KL_ARG_V842_1318) and (shen_eq(symdic.symdic_kl_error, KL_ARG_V842_1318[0]) and shen_consp(KL_ARG_V842_1318[1]))) else (KL_ARG_V842_1318 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.error-macro', shen_errorx45macro)

@tail_recursion
def shen_outputx45macro(KL_ARG_V843_1319):
    global symdic
    return ([symdic.symdic_kl_pr, [tco_apply(shen_mkstr, [KL_ARG_V843_1319[1][0], KL_ARG_V843_1319[1][1]]), [[symdic.symdic_kl_stoutput, []], []]]] if (shen_consp(KL_ARG_V843_1319) and (shen_eq(symdic.symdic_kl_output, KL_ARG_V843_1319[0]) and shen_consp(KL_ARG_V843_1319[1]))) else (KL_ARG_V843_1319 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.output-macro', shen_outputx45macro)

@tail_recursion
def shen_makex45stringx45macro(KL_ARG_V844_1320):
    global symdic
    return (tail_call(shen_mkstr, [KL_ARG_V844_1320[1][0], KL_ARG_V844_1320[1][1]]) if (shen_consp(KL_ARG_V844_1320) and (shen_eq(symdic.symdic_kl_makex45string, KL_ARG_V844_1320[0]) and shen_consp(KL_ARG_V844_1320[1]))) else (KL_ARG_V844_1320 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.make-string-macro', shen_makex45stringx45macro)

@tail_recursion
def shen_compose(KL_ARG_V845_1321, KL_ARG_V846_1322):
    global symdic
    return (KL_ARG_V846_1322 if shen_eq([], KL_ARG_V845_1321) else (tail_call(shen_compose, [KL_ARG_V845_1321[1], tco_apply(KL_ARG_V845_1321[0], [KL_ARG_V846_1322])]) if shen_consp(KL_ARG_V845_1321) else (tail_call(shen_sysx45error, [symdic.symdic_shen_compose]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.compose', shen_compose)

@tail_recursion
def shen_compilex45macro(KL_ARG_V847_1323):
    global symdic
    return ([symdic.symdic_kl_compile, [KL_ARG_V847_1323[1][0], [KL_ARG_V847_1323[1][1][0], [[symdic.symdic_kl_lambda, [symdic.symdic_E, [[symdic.symdic_kl_if, [[symdic.symdic_kl_consx63, [symdic.symdic_E, []]], [[symdic.symdic_kl_error, ['parse error here: ~S~%', [symdic.symdic_E, []]]], [[symdic.symdic_kl_error, ['parse error~%', []]], []]]]], []]]], []]]]] if (shen_consp(KL_ARG_V847_1323) and (shen_eq(symdic.symdic_kl_compile, KL_ARG_V847_1323[0]) and (shen_consp(KL_ARG_V847_1323[1]) and (shen_consp(KL_ARG_V847_1323[1][1]) and shen_eq([], KL_ARG_V847_1323[1][1][1]))))) else (KL_ARG_V847_1323 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.compile-macro', shen_compilex45macro)

@tail_recursion
def shen_prologx45macro(KL_ARG_V848_1324):
    global symdic
    return ([symdic.symdic_shen_intprolog, [tco_apply(shen_prologx45form, [KL_ARG_V848_1324[1]]), []]] if (shen_consp(KL_ARG_V848_1324) and shen_eq(symdic.symdic_kl_prologx63, KL_ARG_V848_1324[0])) else (KL_ARG_V848_1324 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.prolog-macro', shen_prologx45macro)

@tail_recursion
def shen_defprologx45macro(KL_ARG_V849_1325):
    global symdic
    return (tail_call(kl_compile, [symdic.symdic_shen_x60defprologx62, KL_ARG_V849_1325[1], (lambda KL_ARG_Y_1326: tail_call(shen_prologx45error, [KL_ARG_V849_1325[1][0], KL_ARG_Y_1326]))]) if (shen_consp(KL_ARG_V849_1325) and (shen_eq(symdic.symdic_kl_defprolog, KL_ARG_V849_1325[0]) and shen_consp(KL_ARG_V849_1325[1]))) else (KL_ARG_V849_1325 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.defprolog-macro', shen_defprologx45macro)

@tail_recursion
def shen_prologx45form(KL_ARG_V850_1327):
    global symdic
    return tail_call(shen_cons_form, [tco_apply(kl_map, [symdic.symdic_shen_cons_form, KL_ARG_V850_1327])])
shen_add_fun('shen.prolog-form', shen_prologx45form)

@tail_recursion
def shen_datatypex45macro(KL_ARG_V851_1328):
    global symdic
    return ([symdic.symdic_shen_processx45datatype, [shen_intern(('type#' + str(KL_ARG_V851_1328[1][0]))), [[symdic.symdic_kl_compile, [[symdic.symdic_kl_function, [symdic.symdic_shen_x60datatypex45rulesx62, []]], [tco_apply(shen_rcons_form, [KL_ARG_V851_1328[1][1]]), [[symdic.symdic_kl_function, [symdic.symdic_shen_datatypex45error, []]], []]]]], []]]] if (shen_consp(KL_ARG_V851_1328) and (shen_eq(symdic.symdic_kl_datatype, KL_ARG_V851_1328[0]) and shen_consp(KL_ARG_V851_1328[1]))) else (KL_ARG_V851_1328 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.datatype-macro', shen_datatypex45macro)

@tail_recursion
def shen_defmacrox45macro(KL_ARG_V852_1329):

    class KL_Context:
        KL_LOC_Macro_1330 = None
        KL_LOC_Declare_1331 = None
        KL_LOC_Package_1332 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_Macro_1330', [symdic.symdic_kl_define, [KL_ARG_V852_1329[1][0], tco_apply(kl_append, [KL_ARG_V852_1329[1][1], [symdic.symdic_X, [symdic.symdic_kl_x45x62, [symdic.symdic_X, []]]]])]]), [setattr(KL_CTX, 'KL_LOC_Declare_1331', [symdic.symdic_kl_do, [[symdic.symdic_kl_set, [symdic.symdic_kl_x42macrosx42, [[symdic.symdic_kl_adjoin, [KL_ARG_V852_1329[1][0], [[symdic.symdic_kl_value, [symdic.symdic_kl_x42macrosx42, []]], []]]], []]]], [symdic.symdic_kl_macro, []]]]), [setattr(KL_CTX, 'KL_LOC_Package_1332', [symdic.symdic_kl_package, [symdic.symdic_kl_null, [[], [KL_CTX.KL_LOC_Declare_1331, [KL_CTX.KL_LOC_Macro_1330, []]]]]]), KL_CTX.KL_LOC_Package_1332][(-1)]][(-1)]][(-1)] if (shen_consp(KL_ARG_V852_1329) and (shen_eq(symdic.symdic_kl_defmacro, KL_ARG_V852_1329[0]) and shen_consp(KL_ARG_V852_1329[1]))) else (KL_ARG_V852_1329 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.defmacro-macro', shen_defmacrox45macro)

@tail_recursion
def shen_x60defmacrox62(KL_ARG_V857_1333):

    class KL_Context:
        KL_LOC_Result_1334 = None
        KL_LOC_Parse_shen_x60namex62_1335 = None
        KL_LOC_Parse_shen_x60macrorulesx62_1336 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_1334', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60namex62_1335', tco_apply(shen_x60namex62, [KL_ARG_V857_1333])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60macrorulesx62_1336', tco_apply(shen_x60macrorulesx62, [KL_CTX.KL_LOC_Parse_shen_x60namex62_1335])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60macrorulesx62_1336[0], [symdic.symdic_kl_define, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60namex62_1335]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60macrorulesx62_1336])]]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60macrorulesx62_1336)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60namex62_1335)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_1334, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_1334)][(-1)]
shen_add_fun('shen.<defmacro>', shen_x60defmacrox62)

@tail_recursion
def shen_x60macrorulesx62(KL_ARG_V862_1337):

    class KL_Context:
        KL_LOC_Result_1338 = None
        KL_LOC_Parse_shen_x60macrorulex62_1339 = None
        KL_LOC_Parse_shen_x60macrorulesx62_1340 = None
        KL_LOC_Result_1341 = None
        KL_LOC_Parse_shen_x60macrorulex62_1342 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_1338', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60macrorulex62_1339', tco_apply(shen_x60macrorulex62, [KL_ARG_V862_1337])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60macrorulesx62_1340', tco_apply(shen_x60macrorulesx62, [KL_CTX.KL_LOC_Parse_shen_x60macrorulex62_1339])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60macrorulesx62_1340[0], tco_apply(kl_append, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60macrorulex62_1339]), tco_apply(kl_append, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60macrorulesx62_1340]), []])])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60macrorulesx62_1340)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60macrorulex62_1339)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_1341', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60macrorulex62_1342', tco_apply(shen_x60macrorulex62, [KL_ARG_V862_1337])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60macrorulex62_1342[0], tco_apply(kl_append, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60macrorulex62_1342]), [symdic.symdic_Parse_X, [symdic.symdic_kl_x45x62, [symdic.symdic_Parse_X, []]]]])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60macrorulex62_1342)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_1341, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_1341)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_1338, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_1338)][(-1)]
shen_add_fun('shen.<macrorules>', shen_x60macrorulesx62)

@tail_recursion
def shen_x60macrorulex62(KL_ARG_V867_1343):

    class KL_Context:
        KL_LOC_Result_1344 = None
        KL_LOC_Parse_shen_x60patternsx62_1345 = None
        KL_LOC_Parse_shen_x60macroactionx62_1346 = None
        KL_LOC_Parse_shen_x60guardx62_1347 = None
        KL_LOC_Result_1348 = None
        KL_LOC_Parse_shen_x60patternsx62_1349 = None
        KL_LOC_Parse_shen_x60macroactionx62_1350 = None
        KL_LOC_Result_1351 = None
        KL_LOC_Parse_shen_x60patternsx62_1352 = None
        KL_LOC_Parse_shen_x60macroactionx62_1353 = None
        KL_LOC_Parse_shen_x60guardx62_1354 = None
        KL_LOC_Result_1355 = None
        KL_LOC_Parse_shen_x60patternsx62_1356 = None
        KL_LOC_Parse_shen_x60macroactionx62_1357 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_1344', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60patternsx62_1345', tco_apply(shen_x60patternsx62, [KL_ARG_V867_1343])), (([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60macroactionx62_1346', tco_apply(shen_x60macroactionx62, [tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1345[0][1], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1345])])])), (([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60guardx62_1347', tco_apply(shen_x60guardx62, [tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60macroactionx62_1346[0][1], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60macroactionx62_1346])])])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60guardx62_1347[0], tco_apply(kl_append, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1345]), [symdic.symdic_kl_x45x62, tco_apply(kl_append, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60macroactionx62_1346]), [symdic.symdic_kl_where, tco_apply(kl_append, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60guardx62_1347]), []])]])]])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60guardx62_1347)) else tco_apply(kl_fail, []))][(-1)] if (shen_consp(KL_CTX.KL_LOC_Parse_shen_x60macroactionx62_1346[0]) and shen_eq(symdic.symdic_kl_where, KL_CTX.KL_LOC_Parse_shen_x60macroactionx62_1346[0][0])) else tco_apply(kl_fail, [])) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60macroactionx62_1346)) else tco_apply(kl_fail, []))][(-1)] if (shen_consp(KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1345[0]) and shen_eq(symdic.symdic_kl_x45x62, KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1345[0][0])) else tco_apply(kl_fail, [])) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1345)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_1348', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60patternsx62_1349', tco_apply(shen_x60patternsx62, [KL_ARG_V867_1343])), (([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60macroactionx62_1350', tco_apply(shen_x60macroactionx62, [tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1349[0][1], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1349])])])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60macroactionx62_1350[0], tco_apply(kl_append, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1349]), [symdic.symdic_kl_x45x62, tco_apply(kl_append, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60macroactionx62_1350]), []])]])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60macroactionx62_1350)) else tco_apply(kl_fail, []))][(-1)] if (shen_consp(KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1349[0]) and shen_eq(symdic.symdic_kl_x45x62, KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1349[0][0])) else tco_apply(kl_fail, [])) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1349)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_1351', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60patternsx62_1352', tco_apply(shen_x60patternsx62, [KL_ARG_V867_1343])), (([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60macroactionx62_1353', tco_apply(shen_x60macroactionx62, [tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1352[0][1], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1352])])])), (([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60guardx62_1354', tco_apply(shen_x60guardx62, [tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60macroactionx62_1353[0][1], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60macroactionx62_1353])])])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60guardx62_1354[0], tco_apply(kl_append, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1352]), [symdic.symdic_kl_x60x45, tco_apply(kl_append, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60macroactionx62_1353]), [symdic.symdic_kl_where, tco_apply(kl_append, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60guardx62_1354]), []])]])]])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60guardx62_1354)) else tco_apply(kl_fail, []))][(-1)] if (shen_consp(KL_CTX.KL_LOC_Parse_shen_x60macroactionx62_1353[0]) and shen_eq(symdic.symdic_kl_where, KL_CTX.KL_LOC_Parse_shen_x60macroactionx62_1353[0][0])) else tco_apply(kl_fail, [])) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60macroactionx62_1353)) else tco_apply(kl_fail, []))][(-1)] if (shen_consp(KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1352[0]) and shen_eq(symdic.symdic_kl_x60x45, KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1352[0][0])) else tco_apply(kl_fail, [])) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1352)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_1355', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60patternsx62_1356', tco_apply(shen_x60patternsx62, [KL_ARG_V867_1343])), (([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60macroactionx62_1357', tco_apply(shen_x60macroactionx62, [tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1356[0][1], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1356])])])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60macroactionx62_1357[0], tco_apply(kl_append, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1356]), [symdic.symdic_kl_x60x45, tco_apply(kl_append, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60macroactionx62_1357]), []])]])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60macroactionx62_1357)) else tco_apply(kl_fail, []))][(-1)] if (shen_consp(KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1356[0]) and shen_eq(symdic.symdic_kl_x60x45, KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1356[0][0])) else tco_apply(kl_fail, [])) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1356)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_1355, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_1355)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_1351, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_1351)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_1348, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_1348)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_1344, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_1344)][(-1)]
shen_add_fun('shen.<macrorule>', shen_x60macrorulex62)

@tail_recursion
def shen_x60macroactionx62(KL_ARG_V872_1358):

    class KL_Context:
        KL_LOC_Result_1359 = None
        KL_LOC_Parse_shen_x60actionx62_1360 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_1359', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60actionx62_1360', tco_apply(shen_x60actionx62, [KL_ARG_V872_1358])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60actionx62_1360[0], [[symdic.symdic_shen_walk, [[symdic.symdic_kl_function, [symdic.symdic_kl_macroexpand, []]], [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60actionx62_1360]), []]]], []]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60actionx62_1360)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_1359, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_1359)][(-1)]
shen_add_fun('shen.<macroaction>', shen_x60macroactionx62)

@tail_recursion
def shen_x64sx45macro(KL_ARG_V873_1361):

    class KL_Context:
        KL_LOC_E_1362 = None
    KL_CTX = KL_Context()
    global symdic
    return ([symdic.symdic_kl_x64s, [KL_ARG_V873_1361[1][0], [tco_apply(shen_x64sx45macro, [[symdic.symdic_kl_x64s, KL_ARG_V873_1361[1][1]]]), []]]] if (shen_consp(KL_ARG_V873_1361) and (shen_eq(symdic.symdic_kl_x64s, KL_ARG_V873_1361[0]) and (shen_consp(KL_ARG_V873_1361[1]) and (shen_consp(KL_ARG_V873_1361[1][1]) and shen_consp(KL_ARG_V873_1361[1][1][1]))))) else ([setattr(KL_CTX, 'KL_LOC_E_1362', tco_apply(kl_explode, [KL_ARG_V873_1361[1][0]])), (tail_call(shen_x64sx45macro, [[symdic.symdic_kl_x64s, tco_apply(kl_append, [KL_CTX.KL_LOC_E_1362, KL_ARG_V873_1361[1][1]])]]) if (tco_apply(kl_length, [KL_CTX.KL_LOC_E_1362]) > 1) else KL_ARG_V873_1361)][(-1)] if (shen_consp(KL_ARG_V873_1361) and (shen_eq(symdic.symdic_kl_x64s, KL_ARG_V873_1361[0]) and (shen_consp(KL_ARG_V873_1361[1]) and (shen_consp(KL_ARG_V873_1361[1][1]) and (shen_eq([], KL_ARG_V873_1361[1][1][1]) and isinstance(KL_ARG_V873_1361[1][0], str)))))) else (KL_ARG_V873_1361 if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.@s-macro', shen_x64sx45macro)

@tail_recursion
def shen_synonymsx45macro(KL_ARG_V874_1363):
    global symdic
    return ([symdic.symdic_shen_synonymsx45help, [tco_apply(shen_rcons_form, [KL_ARG_V874_1363[1]]), []]] if (shen_consp(KL_ARG_V874_1363) and shen_eq(symdic.symdic_kl_synonyms, KL_ARG_V874_1363[0])) else (KL_ARG_V874_1363 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.synonyms-macro', shen_synonymsx45macro)

@tail_recursion
def shen_nlx45macro(KL_ARG_V875_1364):
    global symdic
    return ([symdic.symdic_kl_nl, [1, []]] if (shen_consp(KL_ARG_V875_1364) and (shen_eq(symdic.symdic_kl_nl, KL_ARG_V875_1364[0]) and shen_eq([], KL_ARG_V875_1364[1]))) else (KL_ARG_V875_1364 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.nl-macro', shen_nlx45macro)

@tail_recursion
def shen_assocx45macro(KL_ARG_V876_1365):
    global symdic
    return ([KL_ARG_V876_1365[0], [KL_ARG_V876_1365[1][0], [tco_apply(shen_assocx45macro, [[KL_ARG_V876_1365[0], KL_ARG_V876_1365[1][1]]]), []]]] if (shen_consp(KL_ARG_V876_1365) and (shen_consp(KL_ARG_V876_1365[1]) and (shen_consp(KL_ARG_V876_1365[1][1]) and (shen_consp(KL_ARG_V876_1365[1][1][1]) and tco_apply(kl_elementx63, [KL_ARG_V876_1365[0], [symdic.symdic_kl_x64p, [symdic.symdic_kl_x64v, [symdic.symdic_kl_append, [symdic.symdic_kl_and, [symdic.symdic_kl_or, [symdic.symdic_kl_x43, [symdic.symdic_kl_x42, [symdic.symdic_kl_do, []]]]]]]]]]))))) else (KL_ARG_V876_1365 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.assoc-macro', shen_assocx45macro)

@tail_recursion
def shen_letx45macro(KL_ARG_V877_1366):
    global symdic
    return ([symdic.symdic_kl_let, [KL_ARG_V877_1366[1][0], [KL_ARG_V877_1366[1][1][0], [tco_apply(shen_letx45macro, [[symdic.symdic_kl_let, KL_ARG_V877_1366[1][1][1]]]), []]]]] if (shen_consp(KL_ARG_V877_1366) and (shen_eq(symdic.symdic_kl_let, KL_ARG_V877_1366[0]) and (shen_consp(KL_ARG_V877_1366[1]) and (shen_consp(KL_ARG_V877_1366[1][1]) and (shen_consp(KL_ARG_V877_1366[1][1][1]) and shen_consp(KL_ARG_V877_1366[1][1][1][1])))))) else (KL_ARG_V877_1366 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.let-macro', shen_letx45macro)

@tail_recursion
def shen_absx45macro(KL_ARG_V878_1367):
    global symdic
    return ([symdic.symdic_kl_lambda, [KL_ARG_V878_1367[1][0], [tco_apply(shen_absx45macro, [[symdic.symdic_kl_x47_, KL_ARG_V878_1367[1][1]]]), []]]] if (shen_consp(KL_ARG_V878_1367) and (shen_eq(symdic.symdic_kl_x47_, KL_ARG_V878_1367[0]) and (shen_consp(KL_ARG_V878_1367[1]) and (shen_consp(KL_ARG_V878_1367[1][1]) and shen_consp(KL_ARG_V878_1367[1][1][1]))))) else ([symdic.symdic_kl_lambda, KL_ARG_V878_1367[1]] if (shen_consp(KL_ARG_V878_1367) and (shen_eq(symdic.symdic_kl_x47_, KL_ARG_V878_1367[0]) and (shen_consp(KL_ARG_V878_1367[1]) and (shen_consp(KL_ARG_V878_1367[1][1]) and shen_eq([], KL_ARG_V878_1367[1][1][1]))))) else (KL_ARG_V878_1367 if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.abs-macro', shen_absx45macro)

@tail_recursion
def shen_casesx45macro(KL_ARG_V881_1368):
    global symdic
    return (KL_ARG_V881_1368[1][1][0] if (shen_consp(KL_ARG_V881_1368) and (shen_eq(symdic.symdic_kl_cases, KL_ARG_V881_1368[0]) and (shen_consp(KL_ARG_V881_1368[1]) and (shen_eq(True, KL_ARG_V881_1368[1][0]) and shen_consp(KL_ARG_V881_1368[1][1]))))) else ([symdic.symdic_kl_if, [KL_ARG_V881_1368[1][0], [KL_ARG_V881_1368[1][1][0], [[symdic.symdic_kl_simplex45error, ['error: cases exhausted', []]], []]]]] if (shen_consp(KL_ARG_V881_1368) and (shen_eq(symdic.symdic_kl_cases, KL_ARG_V881_1368[0]) and (shen_consp(KL_ARG_V881_1368[1]) and (shen_consp(KL_ARG_V881_1368[1][1]) and shen_eq([], KL_ARG_V881_1368[1][1][1]))))) else ([symdic.symdic_kl_if, [KL_ARG_V881_1368[1][0], [KL_ARG_V881_1368[1][1][0], [tco_apply(shen_casesx45macro, [[symdic.symdic_kl_cases, KL_ARG_V881_1368[1][1][1]]]), []]]]] if (shen_consp(KL_ARG_V881_1368) and (shen_eq(symdic.symdic_kl_cases, KL_ARG_V881_1368[0]) and (shen_consp(KL_ARG_V881_1368[1]) and shen_consp(KL_ARG_V881_1368[1][1])))) else (shen_simple_error('error: odd number of case elements\r\n') if (shen_consp(KL_ARG_V881_1368) and (shen_eq(symdic.symdic_kl_cases, KL_ARG_V881_1368[0]) and (shen_consp(KL_ARG_V881_1368[1]) and shen_eq([], KL_ARG_V881_1368[1][1])))) else (KL_ARG_V881_1368 if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.cases-macro', shen_casesx45macro)

@tail_recursion
def shen_timerx45macro(KL_ARG_V882_1369):
    global symdic
    return (tail_call(shen_letx45macro, [[symdic.symdic_kl_let, [symdic.symdic_Start, [[symdic.symdic_kl_getx45time, [symdic.symdic_kl_run, []]], [symdic.symdic_Result, [KL_ARG_V882_1369[1][0], [symdic.symdic_Finish, [[symdic.symdic_kl_getx45time, [symdic.symdic_kl_run, []]], [symdic.symdic_Time, [[symdic.symdic_kl_x45, [symdic.symdic_Finish, [symdic.symdic_Start, []]]], [symdic.symdic_Message, [[symdic.symdic_kl_pr, [[symdic.symdic_kl_cn, ['\r\nrun time: ', [[symdic.symdic_kl_cn, [[symdic.symdic_kl_str, [symdic.symdic_Time, []]], [' secs\r\n', []]]], []]]], [[symdic.symdic_kl_stoutput, []], []]]], [symdic.symdic_Result, []]]]]]]]]]]]]]) if (shen_consp(KL_ARG_V882_1369) and (shen_eq(symdic.symdic_kl_time, KL_ARG_V882_1369[0]) and (shen_consp(KL_ARG_V882_1369[1]) and shen_eq([], KL_ARG_V882_1369[1][1])))) else (KL_ARG_V882_1369 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.timer-macro', shen_timerx45macro)

@tail_recursion
def shen_tuplex45up(KL_ARG_V883_1370):
    global symdic
    return ([symdic.symdic_kl_x64p, [KL_ARG_V883_1370[0], [tco_apply(shen_tuplex45up, [KL_ARG_V883_1370[1]]), []]]] if shen_consp(KL_ARG_V883_1370) else (KL_ARG_V883_1370 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.tuple-up', shen_tuplex45up)

@tail_recursion
def shen_putx47getx45macro(KL_ARG_V884_1371):
    global symdic
    return ([symdic.symdic_kl_put, [KL_ARG_V884_1371[1][0], [KL_ARG_V884_1371[1][1][0], [KL_ARG_V884_1371[1][1][1][0], [[symdic.symdic_kl_value, [symdic.symdic_kl_x42propertyx45vectorx42, []]], []]]]]] if (shen_consp(KL_ARG_V884_1371) and (shen_eq(symdic.symdic_kl_put, KL_ARG_V884_1371[0]) and (shen_consp(KL_ARG_V884_1371[1]) and (shen_consp(KL_ARG_V884_1371[1][1]) and (shen_consp(KL_ARG_V884_1371[1][1][1]) and shen_eq([], KL_ARG_V884_1371[1][1][1][1])))))) else ([symdic.symdic_kl_get, [KL_ARG_V884_1371[1][0], [KL_ARG_V884_1371[1][1][0], [[symdic.symdic_kl_value, [symdic.symdic_kl_x42propertyx45vectorx42, []]], []]]]] if (shen_consp(KL_ARG_V884_1371) and (shen_eq(symdic.symdic_kl_get, KL_ARG_V884_1371[0]) and (shen_consp(KL_ARG_V884_1371[1]) and (shen_consp(KL_ARG_V884_1371[1][1]) and shen_eq([], KL_ARG_V884_1371[1][1][1]))))) else (KL_ARG_V884_1371 if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.put/get-macro', shen_putx47getx45macro)

@tail_recursion
def shen_functionx45macro(KL_ARG_V885_1372):
    global symdic
    return (tail_call(shen_functionx45abstraction, [KL_ARG_V885_1372[1][0], tco_apply(kl_arity, [KL_ARG_V885_1372[1][0]])]) if (shen_consp(KL_ARG_V885_1372) and (shen_eq(symdic.symdic_kl_function, KL_ARG_V885_1372[0]) and (shen_consp(KL_ARG_V885_1372[1]) and shen_eq([], KL_ARG_V885_1372[1][1])))) else (KL_ARG_V885_1372 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.function-macro', shen_functionx45macro)

@tail_recursion
def shen_functionx45abstraction(KL_ARG_V886_1373, KL_ARG_V887_1374):
    global symdic
    return ([symdic.symdic_kl_freeze, [KL_ARG_V886_1373, []]] if shen_eq(0, KL_ARG_V887_1374) else (KL_ARG_V886_1373 if shen_eq((-1), KL_ARG_V887_1374) else (tail_call(shen_functionx45abstractionx45help, [KL_ARG_V886_1373, KL_ARG_V887_1374, []]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.function-abstraction', shen_functionx45abstraction)

@tail_recursion
def shen_functionx45abstractionx45help(KL_ARG_V888_1375, KL_ARG_V889_1376, KL_ARG_V890_1377):

    class KL_Context:
        KL_LOC_X_1378 = None
    KL_CTX = KL_Context()
    global symdic
    return ([KL_ARG_V888_1375, KL_ARG_V890_1377] if shen_eq(0, KL_ARG_V889_1376) else ([setattr(KL_CTX, 'KL_LOC_X_1378', tco_apply(kl_gensym, [symdic.symdic_V])), [symdic.symdic_kl_x47_, [KL_CTX.KL_LOC_X_1378, [tco_apply(shen_functionx45abstractionx45help, [KL_ARG_V888_1375, (KL_ARG_V889_1376 - 1), tco_apply(kl_append, [KL_ARG_V890_1377, [KL_CTX.KL_LOC_X_1378, []]])]), []]]]][(-1)] if True else shen_simple_error('condition failure')))
shen_add_fun('shen.function-abstraction-help', shen_functionx45abstractionx45help)

@tail_recursion
def kl_undefmacro(KL_ARG_V891_1379):
    global symdic
    return [shen_set(symdic.symdic_kl_x42macrosx42, tco_apply(kl_remove, [KL_ARG_V891_1379, shen_get(symdic.symdic_kl_x42macrosx42)])), KL_ARG_V891_1379][(-1)]
shen_add_fun('undefmacro', kl_undefmacro)


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
shen_set(symdic.symdic_shen_x42extraspecialx42, [symdic.symdic_kl_define, [symdic.symdic_shen_processx45datatype, [symdic.symdic_kl_inputx43, [symdic.symdic_kl_defcc, []]]]])
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

@tail_recursion
def shen_initialise_arity_table(KL_ARG_V801_1380):

    class KL_Context:
        KL_LOC_DecArity_1381 = None
    KL_CTX = KL_Context()
    global symdic
    return ([] if shen_eq([], KL_ARG_V801_1380) else ([setattr(KL_CTX, 'KL_LOC_DecArity_1381', tco_apply(kl_put, [KL_ARG_V801_1380[0], symdic.symdic_kl_arity, KL_ARG_V801_1380[1][0], shen_get(symdic.symdic_kl_x42propertyx45vectorx42)])), tail_call(shen_initialise_arity_table, [KL_ARG_V801_1380[1][1]])][(-1)] if (shen_consp(KL_ARG_V801_1380) and shen_consp(KL_ARG_V801_1380[1])) else (tail_call(shen_sysx45error, [symdic.symdic_shen_initialise_arity_table]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.initialise_arity_table', shen_initialise_arity_table)

@tail_recursion
def kl_arity(KL_ARG_V802_1382):
    global symdic
    return shen_try_except((lambda : tco_apply(kl_get, [KL_ARG_V802_1382, symdic.symdic_kl_arity, shen_get(symdic.symdic_kl_x42propertyx45vectorx42)])), (lambda KL_ARG_E_1383: (-1)))
shen_add_fun('arity', kl_arity)

@tail_recursion
def kl_systemf(KL_ARG_V803_1384):

    class KL_Context:
        KL_LOC_Shen_1385 = None
        KL_LOC_External_1386 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Shen_1385', shen_intern('shen')), [setattr(KL_CTX, 'KL_LOC_External_1386', tco_apply(kl_get, [KL_CTX.KL_LOC_Shen_1385, symdic.symdic_shen_externalx45symbols, shen_get(symdic.symdic_kl_x42propertyx45vectorx42)])), tail_call(kl_put, [KL_CTX.KL_LOC_Shen_1385, symdic.symdic_shen_externalx45symbols, tco_apply(kl_adjoin, [KL_ARG_V803_1384, KL_CTX.KL_LOC_External_1386]), shen_get(symdic.symdic_kl_x42propertyx45vectorx42)])][(-1)]][(-1)]
shen_add_fun('systemf', kl_systemf)

@tail_recursion
def kl_adjoin(KL_ARG_V804_1387, KL_ARG_V805_1388):
    global symdic
    return (KL_ARG_V805_1388 if tco_apply(kl_elementx63, [KL_ARG_V804_1387, KL_ARG_V805_1388]) else [KL_ARG_V804_1387, KL_ARG_V805_1388])
shen_add_fun('adjoin', kl_adjoin)

@tail_recursion
def kl_specialise(KL_ARG_V806_1389):
    global symdic
    return [shen_set(symdic.symdic_shen_x42specialx42, [KL_ARG_V806_1389, shen_get(symdic.symdic_shen_x42specialx42)]), KL_ARG_V806_1389][(-1)]
shen_add_fun('specialise', kl_specialise)

@tail_recursion
def kl_unspecialise(KL_ARG_V807_1390):
    global symdic
    return [shen_set(symdic.symdic_shen_x42specialx42, tco_apply(kl_remove, [KL_ARG_V807_1390, shen_get(symdic.symdic_shen_x42specialx42)])), KL_ARG_V807_1390][(-1)]
shen_add_fun('unspecialise', kl_unspecialise)


#============================== types.kl==============================



@tail_recursion
def kl_declare(KL_ARG_V2077_1391, KL_ARG_V2078_1392):

    class KL_Context:
        KL_LOC_Record_1393 = None
        KL_LOC_Variancy_1394 = None
        KL_LOC_Type_1396 = None
        KL_LOC_Fx42_1397 = None
        KL_LOC_Parameters_1398 = None
        KL_LOC_Clause_1399 = None
        KL_LOC_AUM_instruction_1400 = None
        KL_LOC_Code_1401 = None
        KL_LOC_ShenDef_1402 = None
        KL_LOC_Eval_1403 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Record_1393', shen_set(symdic.symdic_shen_x42signedfuncsx42, tco_apply(kl_adjoin, [KL_ARG_V2077_1391, shen_get(symdic.symdic_shen_x42signedfuncsx42)]))), [setattr(KL_CTX, 'KL_LOC_Variancy_1394', shen_try_except((lambda : tco_apply(shen_variancyx45test, [KL_ARG_V2077_1391, KL_ARG_V2078_1392])), (lambda KL_ARG_E_1395: symdic.symdic_shen_skip))), [setattr(KL_CTX, 'KL_LOC_Type_1396', tco_apply(shen_rcons_form, [tco_apply(shen_demodulate, [KL_ARG_V2078_1392])])), [setattr(KL_CTX, 'KL_LOC_Fx42_1397', tco_apply(kl_concat, [symdic.symdic_shen_typex45signaturex45ofx45, KL_ARG_V2077_1391])), [setattr(KL_CTX, 'KL_LOC_Parameters_1398', tco_apply(shen_parameters, [1])), [setattr(KL_CTX, 'KL_LOC_Clause_1399', [[KL_CTX.KL_LOC_Fx42_1397, [symdic.symdic_X, []]], [symdic.symdic_kl_x58x45, [[[symdic.symdic_kl_unifyx33, [symdic.symdic_X, [KL_CTX.KL_LOC_Type_1396, []]]], []], []]]]), [setattr(KL_CTX, 'KL_LOC_AUM_instruction_1400', tco_apply(shen_aum, [KL_CTX.KL_LOC_Clause_1399, KL_CTX.KL_LOC_Parameters_1398])), [setattr(KL_CTX, 'KL_LOC_Code_1401', tco_apply(shen_aum_to_shen, [KL_CTX.KL_LOC_AUM_instruction_1400])), [setattr(KL_CTX, 'KL_LOC_ShenDef_1402', [symdic.symdic_kl_define, [KL_CTX.KL_LOC_Fx42_1397, tco_apply(kl_append, [KL_CTX.KL_LOC_Parameters_1398, tco_apply(kl_append, [[symdic.symdic_ProcessN, [symdic.symdic_Continuation, []]], [symdic.symdic_kl_x45x62, [KL_CTX.KL_LOC_Code_1401, []]]])])]]), [setattr(KL_CTX, 'KL_LOC_Eval_1403', tco_apply(shen_evalx45withoutx45macros, [KL_CTX.KL_LOC_ShenDef_1402])), KL_ARG_V2077_1391][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]
shen_add_fun('declare', kl_declare)

@tail_recursion
def shen_demodulate(KL_ARG_V2079_1404):
    global symdic
    return tail_call(kl_fix, [symdic.symdic_shen_demodh, KL_ARG_V2079_1404])
shen_add_fun('shen.demodulate', shen_demodulate)

@tail_recursion
def shen_demodh(KL_ARG_V2080_1405):
    global symdic
    return (tail_call(kl_map, [symdic.symdic_shen_demodh, KL_ARG_V2080_1405]) if shen_consp(KL_ARG_V2080_1405) else (tail_call(shen_demodx45atom, [KL_ARG_V2080_1405]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.demodh', shen_demodh)

@tail_recursion
def shen_demodx45atom(KL_ARG_V2081_1406):

    class KL_Context:
        KL_LOC_Val_1407 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Val_1407', tco_apply(kl_assoc, [KL_ARG_V2081_1406, shen_get(symdic.symdic_shen_x42synonymsx42)])), (KL_ARG_V2081_1406 if tco_apply(kl_emptyx63, [KL_CTX.KL_LOC_Val_1407]) else KL_CTX.KL_LOC_Val_1407[1])][(-1)]
shen_add_fun('shen.demod-atom', shen_demodx45atom)

@tail_recursion
def shen_variancyx45test(KL_ARG_V2082_1408, KL_ARG_V2083_1409):

    class KL_Context:
        KL_LOC_TypeF_1410 = None
        KL_LOC_Check_1411 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_TypeF_1410', tco_apply(shen_typecheck, [KL_ARG_V2082_1408, symdic.symdic_B])), [setattr(KL_CTX, 'KL_LOC_Check_1411', (symdic.symdic_shen_skip if shen_eq(symdic.symdic_kl_symbol, KL_CTX.KL_LOC_TypeF_1410) else (symdic.symdic_shen_skip if tco_apply(shen_variantx63, [KL_CTX.KL_LOC_TypeF_1410, KL_ARG_V2083_1409]) else shen_pr(('warning: changing the type of ' + tco_apply(shen_app, [KL_ARG_V2082_1408, ' may create errors\r\n', symdic.symdic_shen_a])), tco_apply(kl_stoutput, []))))), symdic.symdic_shen_skip][(-1)]][(-1)]
shen_add_fun('shen.variancy-test', shen_variancyx45test)

@tail_recursion
def shen_variantx63(KL_ARG_V2092_1412, KL_ARG_V2093_1413):
    global symdic
    return (True if shen_eq(KL_ARG_V2093_1413, KL_ARG_V2092_1412) else (tail_call(shen_variantx63, [KL_ARG_V2092_1412[1], KL_ARG_V2093_1413[1]]) if (shen_consp(KL_ARG_V2092_1412) and (shen_consp(KL_ARG_V2093_1413) and shen_eq(KL_ARG_V2093_1413[0], KL_ARG_V2092_1412[0]))) else (tail_call(shen_variantx63, [tco_apply(kl_subst, [symdic.symdic_shen_a, KL_ARG_V2092_1412[0], KL_ARG_V2092_1412[1]]), tco_apply(kl_subst, [symdic.symdic_shen_a, KL_ARG_V2093_1413[0], KL_ARG_V2093_1413[1]])]) if (shen_consp(KL_ARG_V2092_1412) and (shen_consp(KL_ARG_V2093_1413) and (tco_apply(shen_pvarx63, [KL_ARG_V2092_1412[0]]) and tco_apply(kl_variablex63, [KL_ARG_V2093_1413[0]])))) else (tail_call(shen_variantx63, [tco_apply(kl_append, [KL_ARG_V2092_1412[0], KL_ARG_V2092_1412[1]]), tco_apply(kl_append, [KL_ARG_V2093_1413[0], KL_ARG_V2093_1413[1]])]) if (shen_consp(KL_ARG_V2092_1412) and (shen_consp(KL_ARG_V2092_1412[0]) and (shen_consp(KL_ARG_V2093_1413) and shen_consp(KL_ARG_V2093_1413[0])))) else (False if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.variant?', shen_variantx63)


#============================== t-star.kl==============================



@tail_recursion
def shen_typecheck(KL_ARG_V2786_1414, KL_ARG_V2787_1415):

    class KL_Context:
        KL_LOC_Curry_1416 = None
        KL_LOC_ProcessN_1417 = None
        KL_LOC_Type_1418 = None
        KL_LOC_Continuation_1419 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Curry_1416', tco_apply(shen_curry, [KL_ARG_V2786_1414])), [setattr(KL_CTX, 'KL_LOC_ProcessN_1417', tco_apply(shen_startx45newx45prologx45process, [])), [setattr(KL_CTX, 'KL_LOC_Type_1418', tco_apply(shen_insertx45prologx45variables, [tco_apply(shen_demodulate, [tco_apply(shen_curryx45type, [KL_ARG_V2787_1415])]), KL_CTX.KL_LOC_ProcessN_1417])), [setattr(KL_CTX, 'KL_LOC_Continuation_1419', (lambda : tail_call(kl_return, [KL_CTX.KL_LOC_Type_1418, KL_CTX.KL_LOC_ProcessN_1417, symdic.symdic_shen_void]))), tail_call(shen_tx42, [[KL_CTX.KL_LOC_Curry_1416, [symdic.symdic_kl_x58, [KL_CTX.KL_LOC_Type_1418, []]]], [], KL_CTX.KL_LOC_ProcessN_1417, KL_CTX.KL_LOC_Continuation_1419])][(-1)]][(-1)]][(-1)]][(-1)]
shen_add_fun('shen.typecheck', shen_typecheck)

@tail_recursion
def shen_curry(KL_ARG_V2788_1420):
    global symdic
    return ([KL_ARG_V2788_1420[0], tco_apply(kl_map, [symdic.symdic_shen_curry, KL_ARG_V2788_1420[1]])] if (shen_consp(KL_ARG_V2788_1420) and tco_apply(shen_specialx63, [KL_ARG_V2788_1420[0]])) else (KL_ARG_V2788_1420 if (shen_consp(KL_ARG_V2788_1420) and (shen_consp(KL_ARG_V2788_1420[1]) and tco_apply(shen_extraspecialx63, [KL_ARG_V2788_1420[0]]))) else (tail_call(shen_curry, [[[KL_ARG_V2788_1420[0], [KL_ARG_V2788_1420[1][0], []]], KL_ARG_V2788_1420[1][1]]]) if (shen_consp(KL_ARG_V2788_1420) and (shen_consp(KL_ARG_V2788_1420[1]) and shen_consp(KL_ARG_V2788_1420[1][1]))) else ([tco_apply(shen_curry, [KL_ARG_V2788_1420[0]]), [tco_apply(shen_curry, [KL_ARG_V2788_1420[1][0]]), []]] if (shen_consp(KL_ARG_V2788_1420) and (shen_consp(KL_ARG_V2788_1420[1]) and shen_eq([], KL_ARG_V2788_1420[1][1]))) else (KL_ARG_V2788_1420 if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.curry', shen_curry)

@tail_recursion
def shen_specialx63(KL_ARG_V2789_1421):
    global symdic
    return tail_call(kl_elementx63, [KL_ARG_V2789_1421, shen_get(symdic.symdic_shen_x42specialx42)])
shen_add_fun('shen.special?', shen_specialx63)

@tail_recursion
def shen_extraspecialx63(KL_ARG_V2790_1422):
    global symdic
    return tail_call(kl_elementx63, [KL_ARG_V2790_1422, shen_get(symdic.symdic_shen_x42extraspecialx42)])
shen_add_fun('shen.extraspecial?', shen_extraspecialx63)

@tail_recursion
def shen_tx42(KL_ARG_V2791_1423, KL_ARG_V2792_1424, KL_ARG_V2793_1425, KL_ARG_V2794_1426):

    class KL_Context:
        KL_LOC_Throwcontrol_1427 = None
        KL_LOC_Case_1428 = None
        KL_LOC_Error_1429 = None
        KL_LOC_Case_1430 = None
        KL_LOC_V2780_1431 = None
        KL_LOC_Case_1432 = None
        KL_LOC_V2781_1433 = None
        KL_LOC_X_1434 = None
        KL_LOC_V2782_1435 = None
        KL_LOC_V2783_1436 = None
        KL_LOC_V2784_1437 = None
        KL_LOC_A_1438 = None
        KL_LOC_V2785_1439 = None
        KL_LOC_Datatypes_1440 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Throwcontrol_1427', tco_apply(shen_catchpoint, [])), tail_call(shen_cutpoint, [KL_CTX.KL_LOC_Throwcontrol_1427, [setattr(KL_CTX, 'KL_LOC_Case_1428', [setattr(KL_CTX, 'KL_LOC_Error_1429', tco_apply(shen_newpv, [KL_ARG_V2793_1425])), [tco_apply(shen_incinfs, []), tco_apply(kl_fwhen, [tco_apply(shen_maxinfexceededx63, []), KL_ARG_V2793_1425, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Error_1429, tco_apply(shen_errormaxinfs, []), KL_ARG_V2793_1425, KL_ARG_V2794_1426]))])][(-1)]][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1430', [setattr(KL_CTX, 'KL_LOC_V2780_1431', tco_apply(shen_lazyderef, [KL_ARG_V2791_1423, KL_ARG_V2793_1425])), ([tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1427, KL_ARG_V2793_1425, (lambda : tail_call(shen_prologx45failure, [KL_ARG_V2793_1425, KL_ARG_V2794_1426]))])][(-1)] if shen_eq(symdic.symdic_kl_fail, KL_CTX.KL_LOC_V2780_1431) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1432', [setattr(KL_CTX, 'KL_LOC_V2781_1433', tco_apply(shen_lazyderef, [KL_ARG_V2791_1423, KL_ARG_V2793_1425])), ([setattr(KL_CTX, 'KL_LOC_X_1434', KL_CTX.KL_LOC_V2781_1433[0]), [setattr(KL_CTX, 'KL_LOC_V2782_1435', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2781_1433[1], KL_ARG_V2793_1425])), ([setattr(KL_CTX, 'KL_LOC_V2783_1436', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2782_1435[0], KL_ARG_V2793_1425])), ([setattr(KL_CTX, 'KL_LOC_V2784_1437', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2782_1435[1], KL_ARG_V2793_1425])), ([setattr(KL_CTX, 'KL_LOC_A_1438', KL_CTX.KL_LOC_V2784_1437[0]), [setattr(KL_CTX, 'KL_LOC_V2785_1439', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2784_1437[1], KL_ARG_V2793_1425])), ([tco_apply(shen_incinfs, []), tco_apply(kl_fwhen, [tco_apply(shen_typex45theoryx45enabledx63, []), KL_ARG_V2793_1425, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1427, KL_ARG_V2793_1425, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_X_1434, KL_CTX.KL_LOC_A_1438, KL_ARG_V2792_1424, KL_ARG_V2793_1425, KL_ARG_V2794_1426]))]))])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2785_1439) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2784_1437) else False)][(-1)] if shen_eq(symdic.symdic_kl_x58, KL_CTX.KL_LOC_V2783_1436) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2782_1435) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2781_1433) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Datatypes_1440', tco_apply(shen_newpv, [KL_ARG_V2793_1425])), [tco_apply(shen_incinfs, []), tco_apply(shen_show, [KL_ARG_V2791_1423, KL_ARG_V2792_1424, KL_ARG_V2793_1425, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Datatypes_1440, shen_get(symdic.symdic_shen_x42datatypesx42), KL_ARG_V2793_1425, (lambda : tail_call(shen_udefsx42, [KL_ARG_V2791_1423, KL_ARG_V2792_1424, KL_CTX.KL_LOC_Datatypes_1440, KL_ARG_V2793_1425, KL_ARG_V2794_1426]))]))])][(-1)]][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1432, False) else KL_CTX.KL_LOC_Case_1432)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1430, False) else KL_CTX.KL_LOC_Case_1430)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1428, False) else KL_CTX.KL_LOC_Case_1428)][(-1)]])][(-1)]
shen_add_fun('shen.t*', shen_tx42)

@tail_recursion
def shen_typex45theoryx45enabledx63():
    global symdic
    return shen_get(symdic.symdic_shen_x42shenx45typex45theoryx45enabledx63x42)
shen_add_fun('shen.type-theory-enabled?', shen_typex45theoryx45enabledx63)

@tail_recursion
def kl_enablex45typex45theory(KL_ARG_V2799_1441):
    global symdic
    return (shen_set(symdic.symdic_shen_x42shenx45typex45theoryx45enabledx63x42, True) if shen_eq(symdic.symdic_kl_x43, KL_ARG_V2799_1441) else (shen_set(symdic.symdic_shen_x42shenx45typex45theoryx45enabledx63x42, False) if shen_eq(symdic.symdic_kl_x45, KL_ARG_V2799_1441) else (shen_simple_error('enable-type-theory expects a + or a -\r\n') if True else shen_simple_error('condition failure'))))
shen_add_fun('enable-type-theory', kl_enablex45typex45theory)

@tail_recursion
def shen_prologx45failure(KL_ARG_V2808_1442, KL_ARG_V2809_1443):
    global symdic
    return False
shen_add_fun('shen.prolog-failure', shen_prologx45failure)

@tail_recursion
def shen_maxinfexceededx63():
    global symdic
    return (tco_apply(kl_inferences, []) > shen_get(symdic.symdic_shen_x42maxinferencesx42))
shen_add_fun('shen.maxinfexceeded?', shen_maxinfexceededx63)

@tail_recursion
def shen_errormaxinfs():
    global symdic
    return shen_simple_error('maximum inferences exceeded~%')
shen_add_fun('shen.errormaxinfs', shen_errormaxinfs)

@tail_recursion
def shen_udefsx42(KL_ARG_V2810_1444, KL_ARG_V2811_1445, KL_ARG_V2812_1446, KL_ARG_V2813_1447, KL_ARG_V2814_1448):

    class KL_Context:
        KL_LOC_Case_1449 = None
        KL_LOC_V2776_1450 = None
        KL_LOC_D_1451 = None
        KL_LOC_V2777_1452 = None
        KL_LOC_Ds_1453 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Case_1449', [setattr(KL_CTX, 'KL_LOC_V2776_1450', tco_apply(shen_lazyderef, [KL_ARG_V2812_1446, KL_ARG_V2813_1447])), ([setattr(KL_CTX, 'KL_LOC_D_1451', KL_CTX.KL_LOC_V2776_1450[0]), [tco_apply(shen_incinfs, []), tco_apply(kl_call, [[KL_CTX.KL_LOC_D_1451, [KL_ARG_V2810_1444, [KL_ARG_V2811_1445, []]]], KL_ARG_V2813_1447, KL_ARG_V2814_1448])][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2776_1450) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_V2777_1452', tco_apply(shen_lazyderef, [KL_ARG_V2812_1446, KL_ARG_V2813_1447])), ([setattr(KL_CTX, 'KL_LOC_Ds_1453', KL_CTX.KL_LOC_V2777_1452[1]), [tco_apply(shen_incinfs, []), tail_call(shen_udefsx42, [KL_ARG_V2810_1444, KL_ARG_V2811_1445, KL_CTX.KL_LOC_Ds_1453, KL_ARG_V2813_1447, KL_ARG_V2814_1448])][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2777_1452) else False)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1449, False) else KL_CTX.KL_LOC_Case_1449)][(-1)]
shen_add_fun('shen.udefs*', shen_udefsx42)

@tail_recursion
def shen_thx42(KL_ARG_V2815_1454, KL_ARG_V2816_1455, KL_ARG_V2817_1456, KL_ARG_V2818_1457, KL_ARG_V2819_1458):

    class KL_Context:
        KL_LOC_Throwcontrol_1459 = None
        KL_LOC_Case_1460 = None
        KL_LOC_Case_1461 = None
        KL_LOC_F_1462 = None
        KL_LOC_Case_1463 = None
        KL_LOC_Case_1464 = None
        KL_LOC_Case_1465 = None
        KL_LOC_V2656_1466 = None
        KL_LOC_F_1467 = None
        KL_LOC_V2657_1468 = None
        KL_LOC_Case_1469 = None
        KL_LOC_V2658_1470 = None
        KL_LOC_F_1471 = None
        KL_LOC_V2659_1472 = None
        KL_LOC_X_1473 = None
        KL_LOC_V2660_1474 = None
        KL_LOC_B_1475 = None
        KL_LOC_Case_1476 = None
        KL_LOC_V2661_1477 = None
        KL_LOC_V2662_1478 = None
        KL_LOC_V2663_1479 = None
        KL_LOC_X_1480 = None
        KL_LOC_V2664_1481 = None
        KL_LOC_Y_1482 = None
        KL_LOC_V2665_1483 = None
        KL_LOC_V2666_1484 = None
        KL_LOC_V2667_1485 = None
        KL_LOC_V2668_1486 = None
        KL_LOC_A_1487 = None
        KL_LOC_V2669_1488 = None
        KL_LOC_Result_1489 = None
        KL_LOC_A_1490 = None
        KL_LOC_Result_1491 = None
        KL_LOC_Result_1492 = None
        KL_LOC_V2670_1493 = None
        KL_LOC_A_1494 = None
        KL_LOC_V2671_1495 = None
        KL_LOC_Result_1496 = None
        KL_LOC_A_1497 = None
        KL_LOC_Result_1498 = None
        KL_LOC_A_1499 = None
        KL_LOC_Result_1500 = None
        KL_LOC_Case_1501 = None
        KL_LOC_V2672_1502 = None
        KL_LOC_V2673_1503 = None
        KL_LOC_V2674_1504 = None
        KL_LOC_X_1505 = None
        KL_LOC_V2675_1506 = None
        KL_LOC_Y_1507 = None
        KL_LOC_V2676_1508 = None
        KL_LOC_V2677_1509 = None
        KL_LOC_A_1510 = None
        KL_LOC_V2678_1511 = None
        KL_LOC_V2679_1512 = None
        KL_LOC_V2680_1513 = None
        KL_LOC_B_1514 = None
        KL_LOC_V2681_1515 = None
        KL_LOC_Result_1516 = None
        KL_LOC_B_1517 = None
        KL_LOC_Result_1518 = None
        KL_LOC_Result_1519 = None
        KL_LOC_V2682_1520 = None
        KL_LOC_B_1521 = None
        KL_LOC_V2683_1522 = None
        KL_LOC_Result_1523 = None
        KL_LOC_B_1524 = None
        KL_LOC_Result_1525 = None
        KL_LOC_B_1526 = None
        KL_LOC_Result_1527 = None
        KL_LOC_A_1528 = None
        KL_LOC_B_1529 = None
        KL_LOC_Result_1530 = None
        KL_LOC_Case_1531 = None
        KL_LOC_V2684_1532 = None
        KL_LOC_V2685_1533 = None
        KL_LOC_V2686_1534 = None
        KL_LOC_X_1535 = None
        KL_LOC_V2687_1536 = None
        KL_LOC_Y_1537 = None
        KL_LOC_V2688_1538 = None
        KL_LOC_V2689_1539 = None
        KL_LOC_V2690_1540 = None
        KL_LOC_V2691_1541 = None
        KL_LOC_A_1542 = None
        KL_LOC_V2692_1543 = None
        KL_LOC_Result_1544 = None
        KL_LOC_A_1545 = None
        KL_LOC_Result_1546 = None
        KL_LOC_Result_1547 = None
        KL_LOC_V2693_1548 = None
        KL_LOC_A_1549 = None
        KL_LOC_V2694_1550 = None
        KL_LOC_Result_1551 = None
        KL_LOC_A_1552 = None
        KL_LOC_Result_1553 = None
        KL_LOC_A_1554 = None
        KL_LOC_Result_1555 = None
        KL_LOC_Case_1556 = None
        KL_LOC_V2695_1557 = None
        KL_LOC_V2696_1558 = None
        KL_LOC_V2697_1559 = None
        KL_LOC_X_1560 = None
        KL_LOC_V2698_1561 = None
        KL_LOC_Y_1562 = None
        KL_LOC_V2699_1563 = None
        KL_LOC_V2700_1564 = None
        KL_LOC_Result_1565 = None
        KL_LOC_Case_1566 = None
        KL_LOC_V2701_1567 = None
        KL_LOC_V2702_1568 = None
        KL_LOC_V2703_1569 = None
        KL_LOC_X_1570 = None
        KL_LOC_V2704_1571 = None
        KL_LOC_Y_1572 = None
        KL_LOC_V2705_1573 = None
        KL_LOC_V2706_1574 = None
        KL_LOC_A_1575 = None
        KL_LOC_V2707_1576 = None
        KL_LOC_V2708_1577 = None
        KL_LOC_V2709_1578 = None
        KL_LOC_B_1579 = None
        KL_LOC_V2710_1580 = None
        KL_LOC_Z_1581 = None
        KL_LOC_Xx38x38_1582 = None
        KL_LOC_Result_1583 = None
        KL_LOC_Z_1584 = None
        KL_LOC_Xx38x38_1585 = None
        KL_LOC_B_1586 = None
        KL_LOC_Result_1587 = None
        KL_LOC_Z_1588 = None
        KL_LOC_Xx38x38_1589 = None
        KL_LOC_Result_1590 = None
        KL_LOC_V2711_1591 = None
        KL_LOC_B_1592 = None
        KL_LOC_V2712_1593 = None
        KL_LOC_Z_1594 = None
        KL_LOC_Xx38x38_1595 = None
        KL_LOC_Result_1596 = None
        KL_LOC_Z_1597 = None
        KL_LOC_Xx38x38_1598 = None
        KL_LOC_B_1599 = None
        KL_LOC_Result_1600 = None
        KL_LOC_Z_1601 = None
        KL_LOC_Xx38x38_1602 = None
        KL_LOC_B_1603 = None
        KL_LOC_Result_1604 = None
        KL_LOC_Z_1605 = None
        KL_LOC_Xx38x38_1606 = None
        KL_LOC_A_1607 = None
        KL_LOC_B_1608 = None
        KL_LOC_Result_1609 = None
        KL_LOC_Z_1610 = None
        KL_LOC_Xx38x38_1611 = None
        KL_LOC_Case_1612 = None
        KL_LOC_V2713_1613 = None
        KL_LOC_V2714_1614 = None
        KL_LOC_V2715_1615 = None
        KL_LOC_X_1616 = None
        KL_LOC_V2716_1617 = None
        KL_LOC_Y_1618 = None
        KL_LOC_V2717_1619 = None
        KL_LOC_Z_1620 = None
        KL_LOC_V2718_1621 = None
        KL_LOC_W_1622 = None
        KL_LOC_Xx38x38_1623 = None
        KL_LOC_B_1624 = None
        KL_LOC_Case_1625 = None
        KL_LOC_V2719_1626 = None
        KL_LOC_V2720_1627 = None
        KL_LOC_V2721_1628 = None
        KL_LOC_V2722_1629 = None
        KL_LOC_V2723_1630 = None
        KL_LOC_FileName_1631 = None
        KL_LOC_V2724_1632 = None
        KL_LOC_Direction2652_1633 = None
        KL_LOC_V2725_1634 = None
        KL_LOC_V2726_1635 = None
        KL_LOC_V2727_1636 = None
        KL_LOC_V2728_1637 = None
        KL_LOC_Direction_1638 = None
        KL_LOC_V2729_1639 = None
        KL_LOC_Result_1640 = None
        KL_LOC_Direction_1641 = None
        KL_LOC_Result_1642 = None
        KL_LOC_Result_1643 = None
        KL_LOC_V2730_1644 = None
        KL_LOC_Direction_1645 = None
        KL_LOC_V2731_1646 = None
        KL_LOC_Result_1647 = None
        KL_LOC_Direction_1648 = None
        KL_LOC_Result_1649 = None
        KL_LOC_Direction_1650 = None
        KL_LOC_Result_1651 = None
        KL_LOC_Case_1652 = None
        KL_LOC_V2732_1653 = None
        KL_LOC_V2733_1654 = None
        KL_LOC_V2734_1655 = None
        KL_LOC_X_1656 = None
        KL_LOC_V2735_1657 = None
        KL_LOC_A_1658 = None
        KL_LOC_V2736_1659 = None
        KL_LOC_Case_1660 = None
        KL_LOC_V2737_1661 = None
        KL_LOC_V2738_1662 = None
        KL_LOC_V2739_1663 = None
        KL_LOC_V2740_1664 = None
        KL_LOC_V2741_1665 = None
        KL_LOC_A_1666 = None
        KL_LOC_V2742_1667 = None
        KL_LOC_C_1668 = None
        KL_LOC_Case_1669 = None
        KL_LOC_V2743_1670 = None
        KL_LOC_V2744_1671 = None
        KL_LOC_V2745_1672 = None
        KL_LOC_P_1673 = None
        KL_LOC_V2746_1674 = None
        KL_LOC_X_1675 = None
        KL_LOC_V2747_1676 = None
        KL_LOC_Case_1677 = None
        KL_LOC_V2748_1678 = None
        KL_LOC_V2749_1679 = None
        KL_LOC_V2750_1680 = None
        KL_LOC_Var_1681 = None
        KL_LOC_V2751_1682 = None
        KL_LOC_Val_1683 = None
        KL_LOC_V2752_1684 = None
        KL_LOC_Case_1685 = None
        KL_LOC_V2753_1686 = None
        KL_LOC_V2754_1687 = None
        KL_LOC_V2755_1688 = None
        KL_LOC_F_1689 = None
        KL_LOC_V2756_1690 = None
        KL_LOC_A_1691 = None
        KL_LOC_Fx38x38_1692 = None
        KL_LOC_B_1693 = None
        KL_LOC_Case_1694 = None
        KL_LOC_V2757_1695 = None
        KL_LOC_V2758_1696 = None
        KL_LOC_V2759_1697 = None
        KL_LOC_V2760_1698 = None
        KL_LOC_Result_1699 = None
        KL_LOC_Case_1700 = None
        KL_LOC_NewHyp_1701 = None
        KL_LOC_Case_1702 = None
        KL_LOC_V2761_1703 = None
        KL_LOC_V2762_1704 = None
        KL_LOC_V2763_1705 = None
        KL_LOC_F_1706 = None
        KL_LOC_X_1707 = None
        KL_LOC_Case_1708 = None
        KL_LOC_V2764_1709 = None
        KL_LOC_V2765_1710 = None
        KL_LOC_V2766_1711 = None
        KL_LOC_F_1712 = None
        KL_LOC_X_1713 = None
        KL_LOC_Case_1714 = None
        KL_LOC_V2767_1715 = None
        KL_LOC_V2768_1716 = None
        KL_LOC_V2769_1717 = None
        KL_LOC_Result_1718 = None
        KL_LOC_Case_1719 = None
        KL_LOC_V2770_1720 = None
        KL_LOC_V2771_1721 = None
        KL_LOC_V2772_1722 = None
        KL_LOC_Result_1723 = None
        KL_LOC_Datatypes_1724 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Throwcontrol_1459', tco_apply(shen_catchpoint, [])), tail_call(shen_cutpoint, [KL_CTX.KL_LOC_Throwcontrol_1459, [setattr(KL_CTX, 'KL_LOC_Case_1460', [tco_apply(shen_incinfs, []), tco_apply(shen_show, [[KL_ARG_V2815_1454, [symdic.symdic_kl_x58, [KL_ARG_V2816_1455, []]]], KL_ARG_V2817_1456, KL_ARG_V2818_1457, (lambda : tail_call(kl_fwhen, [False, KL_ARG_V2818_1457, KL_ARG_V2819_1458]))])][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1461', [setattr(KL_CTX, 'KL_LOC_F_1462', tco_apply(shen_newpv, [KL_ARG_V2818_1457])), [tco_apply(shen_incinfs, []), tco_apply(kl_fwhen, [tco_apply(shen_typedfx63, [tco_apply(shen_lazyderef, [KL_ARG_V2815_1454, KL_ARG_V2818_1457])]), KL_ARG_V2818_1457, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_F_1462, tco_apply(shen_sigf, [tco_apply(shen_lazyderef, [KL_ARG_V2815_1454, KL_ARG_V2818_1457])]), KL_ARG_V2818_1457, (lambda : tail_call(kl_call, [[KL_CTX.KL_LOC_F_1462, [KL_ARG_V2816_1455, []]], KL_ARG_V2818_1457, KL_ARG_V2819_1458]))]))])][(-1)]][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1463', [tco_apply(shen_incinfs, []), tco_apply(shen_base, [KL_ARG_V2815_1454, KL_ARG_V2816_1455, KL_ARG_V2818_1457, KL_ARG_V2819_1458])][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1464', [tco_apply(shen_incinfs, []), tco_apply(shen_by_hypothesis, [KL_ARG_V2815_1454, KL_ARG_V2816_1455, KL_ARG_V2817_1456, KL_ARG_V2818_1457, KL_ARG_V2819_1458])][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1465', [setattr(KL_CTX, 'KL_LOC_V2656_1466', tco_apply(shen_lazyderef, [KL_ARG_V2815_1454, KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_F_1467', KL_CTX.KL_LOC_V2656_1466[0]), [setattr(KL_CTX, 'KL_LOC_V2657_1468', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2656_1466[1], KL_ARG_V2818_1457])), ([tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_F_1467, [symdic.symdic_kl_x45x45x62, [KL_ARG_V2816_1455, []]], KL_ARG_V2817_1456, KL_ARG_V2818_1457, KL_ARG_V2819_1458])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2657_1468) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2656_1466) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1469', [setattr(KL_CTX, 'KL_LOC_V2658_1470', tco_apply(shen_lazyderef, [KL_ARG_V2815_1454, KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_F_1471', KL_CTX.KL_LOC_V2658_1470[0]), [setattr(KL_CTX, 'KL_LOC_V2659_1472', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2658_1470[1], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_X_1473', KL_CTX.KL_LOC_V2659_1472[0]), [setattr(KL_CTX, 'KL_LOC_V2660_1474', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2659_1472[1], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_B_1475', tco_apply(shen_newpv, [KL_ARG_V2818_1457])), [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_F_1471, [KL_CTX.KL_LOC_B_1475, [symdic.symdic_kl_x45x45x62, [KL_ARG_V2816_1455, []]]], KL_ARG_V2817_1456, KL_ARG_V2818_1457, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_X_1473, KL_CTX.KL_LOC_B_1475, KL_ARG_V2817_1456, KL_ARG_V2818_1457, KL_ARG_V2819_1458]))])][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2660_1474) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2659_1472) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2658_1470) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1476', [setattr(KL_CTX, 'KL_LOC_V2661_1477', tco_apply(shen_lazyderef, [KL_ARG_V2815_1454, KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_V2662_1478', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2661_1477[0], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_V2663_1479', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2661_1477[1], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_X_1480', KL_CTX.KL_LOC_V2663_1479[0]), [setattr(KL_CTX, 'KL_LOC_V2664_1481', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2663_1479[1], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_Y_1482', KL_CTX.KL_LOC_V2664_1481[0]), [setattr(KL_CTX, 'KL_LOC_V2665_1483', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2664_1481[1], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_V2666_1484', tco_apply(shen_lazyderef, [KL_ARG_V2816_1455, KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_V2667_1485', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2666_1484[0], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_V2668_1486', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2666_1484[1], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_A_1487', KL_CTX.KL_LOC_V2668_1486[0]), [setattr(KL_CTX, 'KL_LOC_V2669_1488', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2668_1486[1], KL_ARG_V2818_1457])), ([tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1480, KL_CTX.KL_LOC_A_1487, KL_ARG_V2817_1456, KL_ARG_V2818_1457, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1482, [symdic.symdic_kl_list, [KL_CTX.KL_LOC_A_1487, []]], KL_ARG_V2817_1456, KL_ARG_V2818_1457, KL_ARG_V2819_1458]))])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2669_1488) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2669_1488, [], KL_ARG_V2818_1457]), [setattr(KL_CTX, 'KL_LOC_Result_1489', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1480, KL_CTX.KL_LOC_A_1487, KL_ARG_V2817_1456, KL_ARG_V2818_1457, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1482, [symdic.symdic_kl_list, [KL_CTX.KL_LOC_A_1487, []]], KL_ARG_V2817_1456, KL_ARG_V2818_1457, KL_ARG_V2819_1458]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2669_1488, KL_ARG_V2818_1457]), KL_CTX.KL_LOC_Result_1489][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2669_1488]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2668_1486) else ([setattr(KL_CTX, 'KL_LOC_A_1490', tco_apply(shen_newpv, [KL_ARG_V2818_1457])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2668_1486, [KL_CTX.KL_LOC_A_1490, []], KL_ARG_V2818_1457]), [setattr(KL_CTX, 'KL_LOC_Result_1491', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1480, KL_CTX.KL_LOC_A_1490, KL_ARG_V2817_1456, KL_ARG_V2818_1457, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1482, [symdic.symdic_kl_list, [KL_CTX.KL_LOC_A_1490, []]], KL_ARG_V2817_1456, KL_ARG_V2818_1457, KL_ARG_V2819_1458]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2668_1486, KL_ARG_V2818_1457]), KL_CTX.KL_LOC_Result_1491][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2668_1486]) else False))][(-1)] if shen_eq(symdic.symdic_kl_list, KL_CTX.KL_LOC_V2667_1485) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2667_1485, symdic.symdic_kl_list, KL_ARG_V2818_1457]), [setattr(KL_CTX, 'KL_LOC_Result_1492', [setattr(KL_CTX, 'KL_LOC_V2670_1493', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2666_1484[1], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_A_1494', KL_CTX.KL_LOC_V2670_1493[0]), [setattr(KL_CTX, 'KL_LOC_V2671_1495', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2670_1493[1], KL_ARG_V2818_1457])), ([tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1480, KL_CTX.KL_LOC_A_1494, KL_ARG_V2817_1456, KL_ARG_V2818_1457, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1482, [symdic.symdic_kl_list, [KL_CTX.KL_LOC_A_1494, []]], KL_ARG_V2817_1456, KL_ARG_V2818_1457, KL_ARG_V2819_1458]))])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2671_1495) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2671_1495, [], KL_ARG_V2818_1457]), [setattr(KL_CTX, 'KL_LOC_Result_1496', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1480, KL_CTX.KL_LOC_A_1494, KL_ARG_V2817_1456, KL_ARG_V2818_1457, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1482, [symdic.symdic_kl_list, [KL_CTX.KL_LOC_A_1494, []]], KL_ARG_V2817_1456, KL_ARG_V2818_1457, KL_ARG_V2819_1458]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2671_1495, KL_ARG_V2818_1457]), KL_CTX.KL_LOC_Result_1496][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2671_1495]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2670_1493) else ([setattr(KL_CTX, 'KL_LOC_A_1497', tco_apply(shen_newpv, [KL_ARG_V2818_1457])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2670_1493, [KL_CTX.KL_LOC_A_1497, []], KL_ARG_V2818_1457]), [setattr(KL_CTX, 'KL_LOC_Result_1498', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1480, KL_CTX.KL_LOC_A_1497, KL_ARG_V2817_1456, KL_ARG_V2818_1457, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1482, [symdic.symdic_kl_list, [KL_CTX.KL_LOC_A_1497, []]], KL_ARG_V2817_1456, KL_ARG_V2818_1457, KL_ARG_V2819_1458]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2670_1493, KL_ARG_V2818_1457]), KL_CTX.KL_LOC_Result_1498][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2670_1493]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2667_1485, KL_ARG_V2818_1457]), KL_CTX.KL_LOC_Result_1492][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2667_1485]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2666_1484) else ([setattr(KL_CTX, 'KL_LOC_A_1499', tco_apply(shen_newpv, [KL_ARG_V2818_1457])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2666_1484, [symdic.symdic_kl_list, [KL_CTX.KL_LOC_A_1499, []]], KL_ARG_V2818_1457]), [setattr(KL_CTX, 'KL_LOC_Result_1500', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1480, KL_CTX.KL_LOC_A_1499, KL_ARG_V2817_1456, KL_ARG_V2818_1457, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1482, [symdic.symdic_kl_list, [KL_CTX.KL_LOC_A_1499, []]], KL_ARG_V2817_1456, KL_ARG_V2818_1457, KL_ARG_V2819_1458]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2666_1484, KL_ARG_V2818_1457]), KL_CTX.KL_LOC_Result_1500][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2666_1484]) else False))][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2665_1483) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2664_1481) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2663_1479) else False)][(-1)] if shen_eq(symdic.symdic_kl_cons, KL_CTX.KL_LOC_V2662_1478) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2661_1477) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1501', [setattr(KL_CTX, 'KL_LOC_V2672_1502', tco_apply(shen_lazyderef, [KL_ARG_V2815_1454, KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_V2673_1503', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2672_1502[0], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_V2674_1504', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2672_1502[1], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_X_1505', KL_CTX.KL_LOC_V2674_1504[0]), [setattr(KL_CTX, 'KL_LOC_V2675_1506', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2674_1504[1], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_Y_1507', KL_CTX.KL_LOC_V2675_1506[0]), [setattr(KL_CTX, 'KL_LOC_V2676_1508', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2675_1506[1], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_V2677_1509', tco_apply(shen_lazyderef, [KL_ARG_V2816_1455, KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_A_1510', KL_CTX.KL_LOC_V2677_1509[0]), [setattr(KL_CTX, 'KL_LOC_V2678_1511', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2677_1509[1], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_V2679_1512', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2678_1511[0], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_V2680_1513', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2678_1511[1], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_B_1514', KL_CTX.KL_LOC_V2680_1513[0]), [setattr(KL_CTX, 'KL_LOC_V2681_1515', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2680_1513[1], KL_ARG_V2818_1457])), ([tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1505, KL_CTX.KL_LOC_A_1510, KL_ARG_V2817_1456, KL_ARG_V2818_1457, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1507, KL_CTX.KL_LOC_B_1514, KL_ARG_V2817_1456, KL_ARG_V2818_1457, KL_ARG_V2819_1458]))])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2681_1515) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2681_1515, [], KL_ARG_V2818_1457]), [setattr(KL_CTX, 'KL_LOC_Result_1516', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1505, KL_CTX.KL_LOC_A_1510, KL_ARG_V2817_1456, KL_ARG_V2818_1457, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1507, KL_CTX.KL_LOC_B_1514, KL_ARG_V2817_1456, KL_ARG_V2818_1457, KL_ARG_V2819_1458]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2681_1515, KL_ARG_V2818_1457]), KL_CTX.KL_LOC_Result_1516][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2681_1515]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2680_1513) else ([setattr(KL_CTX, 'KL_LOC_B_1517', tco_apply(shen_newpv, [KL_ARG_V2818_1457])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2680_1513, [KL_CTX.KL_LOC_B_1517, []], KL_ARG_V2818_1457]), [setattr(KL_CTX, 'KL_LOC_Result_1518', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1505, KL_CTX.KL_LOC_A_1510, KL_ARG_V2817_1456, KL_ARG_V2818_1457, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1507, KL_CTX.KL_LOC_B_1517, KL_ARG_V2817_1456, KL_ARG_V2818_1457, KL_ARG_V2819_1458]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2680_1513, KL_ARG_V2818_1457]), KL_CTX.KL_LOC_Result_1518][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2680_1513]) else False))][(-1)] if shen_eq(symdic.symdic_kl_x42, KL_CTX.KL_LOC_V2679_1512) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2679_1512, symdic.symdic_kl_x42, KL_ARG_V2818_1457]), [setattr(KL_CTX, 'KL_LOC_Result_1519', [setattr(KL_CTX, 'KL_LOC_V2682_1520', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2678_1511[1], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_B_1521', KL_CTX.KL_LOC_V2682_1520[0]), [setattr(KL_CTX, 'KL_LOC_V2683_1522', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2682_1520[1], KL_ARG_V2818_1457])), ([tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1505, KL_CTX.KL_LOC_A_1510, KL_ARG_V2817_1456, KL_ARG_V2818_1457, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1507, KL_CTX.KL_LOC_B_1521, KL_ARG_V2817_1456, KL_ARG_V2818_1457, KL_ARG_V2819_1458]))])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2683_1522) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2683_1522, [], KL_ARG_V2818_1457]), [setattr(KL_CTX, 'KL_LOC_Result_1523', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1505, KL_CTX.KL_LOC_A_1510, KL_ARG_V2817_1456, KL_ARG_V2818_1457, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1507, KL_CTX.KL_LOC_B_1521, KL_ARG_V2817_1456, KL_ARG_V2818_1457, KL_ARG_V2819_1458]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2683_1522, KL_ARG_V2818_1457]), KL_CTX.KL_LOC_Result_1523][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2683_1522]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2682_1520) else ([setattr(KL_CTX, 'KL_LOC_B_1524', tco_apply(shen_newpv, [KL_ARG_V2818_1457])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2682_1520, [KL_CTX.KL_LOC_B_1524, []], KL_ARG_V2818_1457]), [setattr(KL_CTX, 'KL_LOC_Result_1525', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1505, KL_CTX.KL_LOC_A_1510, KL_ARG_V2817_1456, KL_ARG_V2818_1457, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1507, KL_CTX.KL_LOC_B_1524, KL_ARG_V2817_1456, KL_ARG_V2818_1457, KL_ARG_V2819_1458]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2682_1520, KL_ARG_V2818_1457]), KL_CTX.KL_LOC_Result_1525][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2682_1520]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2679_1512, KL_ARG_V2818_1457]), KL_CTX.KL_LOC_Result_1519][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2679_1512]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2678_1511) else ([setattr(KL_CTX, 'KL_LOC_B_1526', tco_apply(shen_newpv, [KL_ARG_V2818_1457])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2678_1511, [symdic.symdic_kl_x42, [KL_CTX.KL_LOC_B_1526, []]], KL_ARG_V2818_1457]), [setattr(KL_CTX, 'KL_LOC_Result_1527', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1505, KL_CTX.KL_LOC_A_1510, KL_ARG_V2817_1456, KL_ARG_V2818_1457, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1507, KL_CTX.KL_LOC_B_1526, KL_ARG_V2817_1456, KL_ARG_V2818_1457, KL_ARG_V2819_1458]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2678_1511, KL_ARG_V2818_1457]), KL_CTX.KL_LOC_Result_1527][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2678_1511]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2677_1509) else ([setattr(KL_CTX, 'KL_LOC_A_1528', tco_apply(shen_newpv, [KL_ARG_V2818_1457])), [setattr(KL_CTX, 'KL_LOC_B_1529', tco_apply(shen_newpv, [KL_ARG_V2818_1457])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2677_1509, [KL_CTX.KL_LOC_A_1528, [symdic.symdic_kl_x42, [KL_CTX.KL_LOC_B_1529, []]]], KL_ARG_V2818_1457]), [setattr(KL_CTX, 'KL_LOC_Result_1530', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1505, KL_CTX.KL_LOC_A_1528, KL_ARG_V2817_1456, KL_ARG_V2818_1457, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1507, KL_CTX.KL_LOC_B_1529, KL_ARG_V2817_1456, KL_ARG_V2818_1457, KL_ARG_V2819_1458]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2677_1509, KL_ARG_V2818_1457]), KL_CTX.KL_LOC_Result_1530][(-1)]][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2677_1509]) else False))][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2676_1508) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2675_1506) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2674_1504) else False)][(-1)] if shen_eq(symdic.symdic_kl_x64p, KL_CTX.KL_LOC_V2673_1503) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2672_1502) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1531', [setattr(KL_CTX, 'KL_LOC_V2684_1532', tco_apply(shen_lazyderef, [KL_ARG_V2815_1454, KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_V2685_1533', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2684_1532[0], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_V2686_1534', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2684_1532[1], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_X_1535', KL_CTX.KL_LOC_V2686_1534[0]), [setattr(KL_CTX, 'KL_LOC_V2687_1536', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2686_1534[1], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_Y_1537', KL_CTX.KL_LOC_V2687_1536[0]), [setattr(KL_CTX, 'KL_LOC_V2688_1538', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2687_1536[1], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_V2689_1539', tco_apply(shen_lazyderef, [KL_ARG_V2816_1455, KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_V2690_1540', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2689_1539[0], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_V2691_1541', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2689_1539[1], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_A_1542', KL_CTX.KL_LOC_V2691_1541[0]), [setattr(KL_CTX, 'KL_LOC_V2692_1543', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2691_1541[1], KL_ARG_V2818_1457])), ([tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1535, KL_CTX.KL_LOC_A_1542, KL_ARG_V2817_1456, KL_ARG_V2818_1457, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1537, [symdic.symdic_kl_vector, [KL_CTX.KL_LOC_A_1542, []]], KL_ARG_V2817_1456, KL_ARG_V2818_1457, KL_ARG_V2819_1458]))])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2692_1543) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2692_1543, [], KL_ARG_V2818_1457]), [setattr(KL_CTX, 'KL_LOC_Result_1544', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1535, KL_CTX.KL_LOC_A_1542, KL_ARG_V2817_1456, KL_ARG_V2818_1457, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1537, [symdic.symdic_kl_vector, [KL_CTX.KL_LOC_A_1542, []]], KL_ARG_V2817_1456, KL_ARG_V2818_1457, KL_ARG_V2819_1458]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2692_1543, KL_ARG_V2818_1457]), KL_CTX.KL_LOC_Result_1544][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2692_1543]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2691_1541) else ([setattr(KL_CTX, 'KL_LOC_A_1545', tco_apply(shen_newpv, [KL_ARG_V2818_1457])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2691_1541, [KL_CTX.KL_LOC_A_1545, []], KL_ARG_V2818_1457]), [setattr(KL_CTX, 'KL_LOC_Result_1546', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1535, KL_CTX.KL_LOC_A_1545, KL_ARG_V2817_1456, KL_ARG_V2818_1457, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1537, [symdic.symdic_kl_vector, [KL_CTX.KL_LOC_A_1545, []]], KL_ARG_V2817_1456, KL_ARG_V2818_1457, KL_ARG_V2819_1458]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2691_1541, KL_ARG_V2818_1457]), KL_CTX.KL_LOC_Result_1546][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2691_1541]) else False))][(-1)] if shen_eq(symdic.symdic_kl_vector, KL_CTX.KL_LOC_V2690_1540) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2690_1540, symdic.symdic_kl_vector, KL_ARG_V2818_1457]), [setattr(KL_CTX, 'KL_LOC_Result_1547', [setattr(KL_CTX, 'KL_LOC_V2693_1548', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2689_1539[1], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_A_1549', KL_CTX.KL_LOC_V2693_1548[0]), [setattr(KL_CTX, 'KL_LOC_V2694_1550', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2693_1548[1], KL_ARG_V2818_1457])), ([tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1535, KL_CTX.KL_LOC_A_1549, KL_ARG_V2817_1456, KL_ARG_V2818_1457, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1537, [symdic.symdic_kl_vector, [KL_CTX.KL_LOC_A_1549, []]], KL_ARG_V2817_1456, KL_ARG_V2818_1457, KL_ARG_V2819_1458]))])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2694_1550) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2694_1550, [], KL_ARG_V2818_1457]), [setattr(KL_CTX, 'KL_LOC_Result_1551', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1535, KL_CTX.KL_LOC_A_1549, KL_ARG_V2817_1456, KL_ARG_V2818_1457, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1537, [symdic.symdic_kl_vector, [KL_CTX.KL_LOC_A_1549, []]], KL_ARG_V2817_1456, KL_ARG_V2818_1457, KL_ARG_V2819_1458]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2694_1550, KL_ARG_V2818_1457]), KL_CTX.KL_LOC_Result_1551][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2694_1550]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2693_1548) else ([setattr(KL_CTX, 'KL_LOC_A_1552', tco_apply(shen_newpv, [KL_ARG_V2818_1457])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2693_1548, [KL_CTX.KL_LOC_A_1552, []], KL_ARG_V2818_1457]), [setattr(KL_CTX, 'KL_LOC_Result_1553', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1535, KL_CTX.KL_LOC_A_1552, KL_ARG_V2817_1456, KL_ARG_V2818_1457, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1537, [symdic.symdic_kl_vector, [KL_CTX.KL_LOC_A_1552, []]], KL_ARG_V2817_1456, KL_ARG_V2818_1457, KL_ARG_V2819_1458]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2693_1548, KL_ARG_V2818_1457]), KL_CTX.KL_LOC_Result_1553][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2693_1548]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2690_1540, KL_ARG_V2818_1457]), KL_CTX.KL_LOC_Result_1547][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2690_1540]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2689_1539) else ([setattr(KL_CTX, 'KL_LOC_A_1554', tco_apply(shen_newpv, [KL_ARG_V2818_1457])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2689_1539, [symdic.symdic_kl_vector, [KL_CTX.KL_LOC_A_1554, []]], KL_ARG_V2818_1457]), [setattr(KL_CTX, 'KL_LOC_Result_1555', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1535, KL_CTX.KL_LOC_A_1554, KL_ARG_V2817_1456, KL_ARG_V2818_1457, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1537, [symdic.symdic_kl_vector, [KL_CTX.KL_LOC_A_1554, []]], KL_ARG_V2817_1456, KL_ARG_V2818_1457, KL_ARG_V2819_1458]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2689_1539, KL_ARG_V2818_1457]), KL_CTX.KL_LOC_Result_1555][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2689_1539]) else False))][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2688_1538) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2687_1536) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2686_1534) else False)][(-1)] if shen_eq(symdic.symdic_kl_x64v, KL_CTX.KL_LOC_V2685_1533) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2684_1532) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1556', [setattr(KL_CTX, 'KL_LOC_V2695_1557', tco_apply(shen_lazyderef, [KL_ARG_V2815_1454, KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_V2696_1558', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2695_1557[0], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_V2697_1559', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2695_1557[1], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_X_1560', KL_CTX.KL_LOC_V2697_1559[0]), [setattr(KL_CTX, 'KL_LOC_V2698_1561', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2697_1559[1], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_Y_1562', KL_CTX.KL_LOC_V2698_1561[0]), [setattr(KL_CTX, 'KL_LOC_V2699_1563', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2698_1561[1], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_V2700_1564', tco_apply(shen_lazyderef, [KL_ARG_V2816_1455, KL_ARG_V2818_1457])), ([tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1560, symdic.symdic_kl_string, KL_ARG_V2817_1456, KL_ARG_V2818_1457, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1562, symdic.symdic_kl_string, KL_ARG_V2817_1456, KL_ARG_V2818_1457, KL_ARG_V2819_1458]))])][(-1)] if shen_eq(symdic.symdic_kl_string, KL_CTX.KL_LOC_V2700_1564) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2700_1564, symdic.symdic_kl_string, KL_ARG_V2818_1457]), [setattr(KL_CTX, 'KL_LOC_Result_1565', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1560, symdic.symdic_kl_string, KL_ARG_V2817_1456, KL_ARG_V2818_1457, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1562, symdic.symdic_kl_string, KL_ARG_V2817_1456, KL_ARG_V2818_1457, KL_ARG_V2819_1458]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2700_1564, KL_ARG_V2818_1457]), KL_CTX.KL_LOC_Result_1565][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2700_1564]) else False))][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2699_1563) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2698_1561) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2697_1559) else False)][(-1)] if shen_eq(symdic.symdic_kl_x64s, KL_CTX.KL_LOC_V2696_1558) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2695_1557) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1566', [setattr(KL_CTX, 'KL_LOC_V2701_1567', tco_apply(shen_lazyderef, [KL_ARG_V2815_1454, KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_V2702_1568', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2701_1567[0], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_V2703_1569', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2701_1567[1], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_X_1570', KL_CTX.KL_LOC_V2703_1569[0]), [setattr(KL_CTX, 'KL_LOC_V2704_1571', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2703_1569[1], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_Y_1572', KL_CTX.KL_LOC_V2704_1571[0]), [setattr(KL_CTX, 'KL_LOC_V2705_1573', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2704_1571[1], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_V2706_1574', tco_apply(shen_lazyderef, [KL_ARG_V2816_1455, KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_A_1575', KL_CTX.KL_LOC_V2706_1574[0]), [setattr(KL_CTX, 'KL_LOC_V2707_1576', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2706_1574[1], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_V2708_1577', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2707_1576[0], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_V2709_1578', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2707_1576[1], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_B_1579', KL_CTX.KL_LOC_V2709_1578[0]), [setattr(KL_CTX, 'KL_LOC_V2710_1580', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2709_1578[1], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_Z_1581', tco_apply(shen_newpv, [KL_ARG_V2818_1457])), [setattr(KL_CTX, 'KL_LOC_Xx38x38_1582', tco_apply(shen_newpv, [KL_ARG_V2818_1457])), [tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1459, KL_ARG_V2818_1457, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Xx38x38_1582, tco_apply(shen_placeholder, []), KL_ARG_V2818_1457, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Z_1581, tco_apply(shen_ebr, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Xx38x38_1582, KL_ARG_V2818_1457]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1570, KL_ARG_V2818_1457]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1572, KL_ARG_V2818_1457])]), KL_ARG_V2818_1457, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Z_1581, KL_CTX.KL_LOC_B_1579, [[KL_CTX.KL_LOC_Xx38x38_1582, [symdic.symdic_kl_x58, [KL_CTX.KL_LOC_A_1575, []]]], KL_ARG_V2817_1456], KL_ARG_V2818_1457, KL_ARG_V2819_1458]))]))]))])][(-1)]][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2710_1580) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2710_1580, [], KL_ARG_V2818_1457]), [setattr(KL_CTX, 'KL_LOC_Result_1583', [setattr(KL_CTX, 'KL_LOC_Z_1584', tco_apply(shen_newpv, [KL_ARG_V2818_1457])), [setattr(KL_CTX, 'KL_LOC_Xx38x38_1585', tco_apply(shen_newpv, [KL_ARG_V2818_1457])), [tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1459, KL_ARG_V2818_1457, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Xx38x38_1585, tco_apply(shen_placeholder, []), KL_ARG_V2818_1457, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Z_1584, tco_apply(shen_ebr, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Xx38x38_1585, KL_ARG_V2818_1457]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1570, KL_ARG_V2818_1457]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1572, KL_ARG_V2818_1457])]), KL_ARG_V2818_1457, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Z_1584, KL_CTX.KL_LOC_B_1579, [[KL_CTX.KL_LOC_Xx38x38_1585, [symdic.symdic_kl_x58, [KL_CTX.KL_LOC_A_1575, []]]], KL_ARG_V2817_1456], KL_ARG_V2818_1457, KL_ARG_V2819_1458]))]))]))])][(-1)]][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2710_1580, KL_ARG_V2818_1457]), KL_CTX.KL_LOC_Result_1583][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2710_1580]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2709_1578) else ([setattr(KL_CTX, 'KL_LOC_B_1586', tco_apply(shen_newpv, [KL_ARG_V2818_1457])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2709_1578, [KL_CTX.KL_LOC_B_1586, []], KL_ARG_V2818_1457]), [setattr(KL_CTX, 'KL_LOC_Result_1587', [setattr(KL_CTX, 'KL_LOC_Z_1588', tco_apply(shen_newpv, [KL_ARG_V2818_1457])), [setattr(KL_CTX, 'KL_LOC_Xx38x38_1589', tco_apply(shen_newpv, [KL_ARG_V2818_1457])), [tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1459, KL_ARG_V2818_1457, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Xx38x38_1589, tco_apply(shen_placeholder, []), KL_ARG_V2818_1457, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Z_1588, tco_apply(shen_ebr, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Xx38x38_1589, KL_ARG_V2818_1457]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1570, KL_ARG_V2818_1457]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1572, KL_ARG_V2818_1457])]), KL_ARG_V2818_1457, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Z_1588, KL_CTX.KL_LOC_B_1586, [[KL_CTX.KL_LOC_Xx38x38_1589, [symdic.symdic_kl_x58, [KL_CTX.KL_LOC_A_1575, []]]], KL_ARG_V2817_1456], KL_ARG_V2818_1457, KL_ARG_V2819_1458]))]))]))])][(-1)]][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2709_1578, KL_ARG_V2818_1457]), KL_CTX.KL_LOC_Result_1587][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2709_1578]) else False))][(-1)] if shen_eq(symdic.symdic_kl_x45x45x62, KL_CTX.KL_LOC_V2708_1577) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2708_1577, symdic.symdic_kl_x45x45x62, KL_ARG_V2818_1457]), [setattr(KL_CTX, 'KL_LOC_Result_1590', [setattr(KL_CTX, 'KL_LOC_V2711_1591', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2707_1576[1], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_B_1592', KL_CTX.KL_LOC_V2711_1591[0]), [setattr(KL_CTX, 'KL_LOC_V2712_1593', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2711_1591[1], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_Z_1594', tco_apply(shen_newpv, [KL_ARG_V2818_1457])), [setattr(KL_CTX, 'KL_LOC_Xx38x38_1595', tco_apply(shen_newpv, [KL_ARG_V2818_1457])), [tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1459, KL_ARG_V2818_1457, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Xx38x38_1595, tco_apply(shen_placeholder, []), KL_ARG_V2818_1457, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Z_1594, tco_apply(shen_ebr, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Xx38x38_1595, KL_ARG_V2818_1457]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1570, KL_ARG_V2818_1457]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1572, KL_ARG_V2818_1457])]), KL_ARG_V2818_1457, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Z_1594, KL_CTX.KL_LOC_B_1592, [[KL_CTX.KL_LOC_Xx38x38_1595, [symdic.symdic_kl_x58, [KL_CTX.KL_LOC_A_1575, []]]], KL_ARG_V2817_1456], KL_ARG_V2818_1457, KL_ARG_V2819_1458]))]))]))])][(-1)]][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2712_1593) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2712_1593, [], KL_ARG_V2818_1457]), [setattr(KL_CTX, 'KL_LOC_Result_1596', [setattr(KL_CTX, 'KL_LOC_Z_1597', tco_apply(shen_newpv, [KL_ARG_V2818_1457])), [setattr(KL_CTX, 'KL_LOC_Xx38x38_1598', tco_apply(shen_newpv, [KL_ARG_V2818_1457])), [tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1459, KL_ARG_V2818_1457, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Xx38x38_1598, tco_apply(shen_placeholder, []), KL_ARG_V2818_1457, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Z_1597, tco_apply(shen_ebr, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Xx38x38_1598, KL_ARG_V2818_1457]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1570, KL_ARG_V2818_1457]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1572, KL_ARG_V2818_1457])]), KL_ARG_V2818_1457, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Z_1597, KL_CTX.KL_LOC_B_1592, [[KL_CTX.KL_LOC_Xx38x38_1598, [symdic.symdic_kl_x58, [KL_CTX.KL_LOC_A_1575, []]]], KL_ARG_V2817_1456], KL_ARG_V2818_1457, KL_ARG_V2819_1458]))]))]))])][(-1)]][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2712_1593, KL_ARG_V2818_1457]), KL_CTX.KL_LOC_Result_1596][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2712_1593]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2711_1591) else ([setattr(KL_CTX, 'KL_LOC_B_1599', tco_apply(shen_newpv, [KL_ARG_V2818_1457])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2711_1591, [KL_CTX.KL_LOC_B_1599, []], KL_ARG_V2818_1457]), [setattr(KL_CTX, 'KL_LOC_Result_1600', [setattr(KL_CTX, 'KL_LOC_Z_1601', tco_apply(shen_newpv, [KL_ARG_V2818_1457])), [setattr(KL_CTX, 'KL_LOC_Xx38x38_1602', tco_apply(shen_newpv, [KL_ARG_V2818_1457])), [tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1459, KL_ARG_V2818_1457, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Xx38x38_1602, tco_apply(shen_placeholder, []), KL_ARG_V2818_1457, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Z_1601, tco_apply(shen_ebr, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Xx38x38_1602, KL_ARG_V2818_1457]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1570, KL_ARG_V2818_1457]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1572, KL_ARG_V2818_1457])]), KL_ARG_V2818_1457, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Z_1601, KL_CTX.KL_LOC_B_1599, [[KL_CTX.KL_LOC_Xx38x38_1602, [symdic.symdic_kl_x58, [KL_CTX.KL_LOC_A_1575, []]]], KL_ARG_V2817_1456], KL_ARG_V2818_1457, KL_ARG_V2819_1458]))]))]))])][(-1)]][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2711_1591, KL_ARG_V2818_1457]), KL_CTX.KL_LOC_Result_1600][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2711_1591]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2708_1577, KL_ARG_V2818_1457]), KL_CTX.KL_LOC_Result_1590][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2708_1577]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2707_1576) else ([setattr(KL_CTX, 'KL_LOC_B_1603', tco_apply(shen_newpv, [KL_ARG_V2818_1457])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2707_1576, [symdic.symdic_kl_x45x45x62, [KL_CTX.KL_LOC_B_1603, []]], KL_ARG_V2818_1457]), [setattr(KL_CTX, 'KL_LOC_Result_1604', [setattr(KL_CTX, 'KL_LOC_Z_1605', tco_apply(shen_newpv, [KL_ARG_V2818_1457])), [setattr(KL_CTX, 'KL_LOC_Xx38x38_1606', tco_apply(shen_newpv, [KL_ARG_V2818_1457])), [tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1459, KL_ARG_V2818_1457, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Xx38x38_1606, tco_apply(shen_placeholder, []), KL_ARG_V2818_1457, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Z_1605, tco_apply(shen_ebr, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Xx38x38_1606, KL_ARG_V2818_1457]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1570, KL_ARG_V2818_1457]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1572, KL_ARG_V2818_1457])]), KL_ARG_V2818_1457, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Z_1605, KL_CTX.KL_LOC_B_1603, [[KL_CTX.KL_LOC_Xx38x38_1606, [symdic.symdic_kl_x58, [KL_CTX.KL_LOC_A_1575, []]]], KL_ARG_V2817_1456], KL_ARG_V2818_1457, KL_ARG_V2819_1458]))]))]))])][(-1)]][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2707_1576, KL_ARG_V2818_1457]), KL_CTX.KL_LOC_Result_1604][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2707_1576]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2706_1574) else ([setattr(KL_CTX, 'KL_LOC_A_1607', tco_apply(shen_newpv, [KL_ARG_V2818_1457])), [setattr(KL_CTX, 'KL_LOC_B_1608', tco_apply(shen_newpv, [KL_ARG_V2818_1457])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2706_1574, [KL_CTX.KL_LOC_A_1607, [symdic.symdic_kl_x45x45x62, [KL_CTX.KL_LOC_B_1608, []]]], KL_ARG_V2818_1457]), [setattr(KL_CTX, 'KL_LOC_Result_1609', [setattr(KL_CTX, 'KL_LOC_Z_1610', tco_apply(shen_newpv, [KL_ARG_V2818_1457])), [setattr(KL_CTX, 'KL_LOC_Xx38x38_1611', tco_apply(shen_newpv, [KL_ARG_V2818_1457])), [tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1459, KL_ARG_V2818_1457, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Xx38x38_1611, tco_apply(shen_placeholder, []), KL_ARG_V2818_1457, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Z_1610, tco_apply(shen_ebr, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Xx38x38_1611, KL_ARG_V2818_1457]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1570, KL_ARG_V2818_1457]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1572, KL_ARG_V2818_1457])]), KL_ARG_V2818_1457, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Z_1610, KL_CTX.KL_LOC_B_1608, [[KL_CTX.KL_LOC_Xx38x38_1611, [symdic.symdic_kl_x58, [KL_CTX.KL_LOC_A_1607, []]]], KL_ARG_V2817_1456], KL_ARG_V2818_1457, KL_ARG_V2819_1458]))]))]))])][(-1)]][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2706_1574, KL_ARG_V2818_1457]), KL_CTX.KL_LOC_Result_1609][(-1)]][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2706_1574]) else False))][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2705_1573) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2704_1571) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2703_1569) else False)][(-1)] if shen_eq(symdic.symdic_kl_lambda, KL_CTX.KL_LOC_V2702_1568) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2701_1567) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1612', [setattr(KL_CTX, 'KL_LOC_V2713_1613', tco_apply(shen_lazyderef, [KL_ARG_V2815_1454, KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_V2714_1614', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2713_1613[0], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_V2715_1615', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2713_1613[1], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_X_1616', KL_CTX.KL_LOC_V2715_1615[0]), [setattr(KL_CTX, 'KL_LOC_V2716_1617', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2715_1615[1], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_Y_1618', KL_CTX.KL_LOC_V2716_1617[0]), [setattr(KL_CTX, 'KL_LOC_V2717_1619', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2716_1617[1], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_Z_1620', KL_CTX.KL_LOC_V2717_1619[0]), [setattr(KL_CTX, 'KL_LOC_V2718_1621', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2717_1619[1], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_W_1622', tco_apply(shen_newpv, [KL_ARG_V2818_1457])), [setattr(KL_CTX, 'KL_LOC_Xx38x38_1623', tco_apply(shen_newpv, [KL_ARG_V2818_1457])), [setattr(KL_CTX, 'KL_LOC_B_1624', tco_apply(shen_newpv, [KL_ARG_V2818_1457])), [tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1459, KL_ARG_V2818_1457, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1618, KL_CTX.KL_LOC_B_1624, KL_ARG_V2817_1456, KL_ARG_V2818_1457, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Xx38x38_1623, tco_apply(shen_placeholder, []), KL_ARG_V2818_1457, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_W_1622, tco_apply(shen_ebr, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Xx38x38_1623, KL_ARG_V2818_1457]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1616, KL_ARG_V2818_1457]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Z_1620, KL_ARG_V2818_1457])]), KL_ARG_V2818_1457, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_W_1622, KL_ARG_V2816_1455, [[KL_CTX.KL_LOC_Xx38x38_1623, [symdic.symdic_kl_x58, [KL_CTX.KL_LOC_B_1624, []]]], KL_ARG_V2817_1456], KL_ARG_V2818_1457, KL_ARG_V2819_1458]))]))]))]))])][(-1)]][(-1)]][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2718_1621) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2717_1619) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2716_1617) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2715_1615) else False)][(-1)] if shen_eq(symdic.symdic_kl_let, KL_CTX.KL_LOC_V2714_1614) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2713_1613) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1625', [setattr(KL_CTX, 'KL_LOC_V2719_1626', tco_apply(shen_lazyderef, [KL_ARG_V2815_1454, KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_V2720_1627', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2719_1626[0], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_V2721_1628', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2719_1626[1], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_V2722_1629', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2721_1628[0], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_V2723_1630', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2721_1628[1], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_FileName_1631', KL_CTX.KL_LOC_V2723_1630[0]), [setattr(KL_CTX, 'KL_LOC_V2724_1632', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2723_1630[1], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_Direction2652_1633', KL_CTX.KL_LOC_V2724_1632[0]), [setattr(KL_CTX, 'KL_LOC_V2725_1634', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2724_1632[1], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_V2726_1635', tco_apply(shen_lazyderef, [KL_ARG_V2816_1455, KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_V2727_1636', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2726_1635[0], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_V2728_1637', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2726_1635[1], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_Direction_1638', KL_CTX.KL_LOC_V2728_1637[0]), [setattr(KL_CTX, 'KL_LOC_V2729_1639', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2728_1637[1], KL_ARG_V2818_1457])), ([tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_Direction_1638, KL_CTX.KL_LOC_Direction2652_1633, KL_ARG_V2818_1457, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1459, KL_ARG_V2818_1457, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_FileName_1631, symdic.symdic_kl_string, KL_ARG_V2817_1456, KL_ARG_V2818_1457, KL_ARG_V2819_1458]))]))])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2729_1639) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2729_1639, [], KL_ARG_V2818_1457]), [setattr(KL_CTX, 'KL_LOC_Result_1640', [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_Direction_1638, KL_CTX.KL_LOC_Direction2652_1633, KL_ARG_V2818_1457, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1459, KL_ARG_V2818_1457, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_FileName_1631, symdic.symdic_kl_string, KL_ARG_V2817_1456, KL_ARG_V2818_1457, KL_ARG_V2819_1458]))]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2729_1639, KL_ARG_V2818_1457]), KL_CTX.KL_LOC_Result_1640][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2729_1639]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2728_1637) else ([setattr(KL_CTX, 'KL_LOC_Direction_1641', tco_apply(shen_newpv, [KL_ARG_V2818_1457])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2728_1637, [KL_CTX.KL_LOC_Direction_1641, []], KL_ARG_V2818_1457]), [setattr(KL_CTX, 'KL_LOC_Result_1642', [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_Direction_1641, KL_CTX.KL_LOC_Direction2652_1633, KL_ARG_V2818_1457, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1459, KL_ARG_V2818_1457, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_FileName_1631, symdic.symdic_kl_string, KL_ARG_V2817_1456, KL_ARG_V2818_1457, KL_ARG_V2819_1458]))]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2728_1637, KL_ARG_V2818_1457]), KL_CTX.KL_LOC_Result_1642][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2728_1637]) else False))][(-1)] if shen_eq(symdic.symdic_kl_stream, KL_CTX.KL_LOC_V2727_1636) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2727_1636, symdic.symdic_kl_stream, KL_ARG_V2818_1457]), [setattr(KL_CTX, 'KL_LOC_Result_1643', [setattr(KL_CTX, 'KL_LOC_V2730_1644', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2726_1635[1], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_Direction_1645', KL_CTX.KL_LOC_V2730_1644[0]), [setattr(KL_CTX, 'KL_LOC_V2731_1646', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2730_1644[1], KL_ARG_V2818_1457])), ([tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_Direction_1645, KL_CTX.KL_LOC_Direction2652_1633, KL_ARG_V2818_1457, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1459, KL_ARG_V2818_1457, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_FileName_1631, symdic.symdic_kl_string, KL_ARG_V2817_1456, KL_ARG_V2818_1457, KL_ARG_V2819_1458]))]))])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2731_1646) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2731_1646, [], KL_ARG_V2818_1457]), [setattr(KL_CTX, 'KL_LOC_Result_1647', [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_Direction_1645, KL_CTX.KL_LOC_Direction2652_1633, KL_ARG_V2818_1457, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1459, KL_ARG_V2818_1457, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_FileName_1631, symdic.symdic_kl_string, KL_ARG_V2817_1456, KL_ARG_V2818_1457, KL_ARG_V2819_1458]))]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2731_1646, KL_ARG_V2818_1457]), KL_CTX.KL_LOC_Result_1647][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2731_1646]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2730_1644) else ([setattr(KL_CTX, 'KL_LOC_Direction_1648', tco_apply(shen_newpv, [KL_ARG_V2818_1457])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2730_1644, [KL_CTX.KL_LOC_Direction_1648, []], KL_ARG_V2818_1457]), [setattr(KL_CTX, 'KL_LOC_Result_1649', [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_Direction_1648, KL_CTX.KL_LOC_Direction2652_1633, KL_ARG_V2818_1457, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1459, KL_ARG_V2818_1457, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_FileName_1631, symdic.symdic_kl_string, KL_ARG_V2817_1456, KL_ARG_V2818_1457, KL_ARG_V2819_1458]))]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2730_1644, KL_ARG_V2818_1457]), KL_CTX.KL_LOC_Result_1649][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2730_1644]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2727_1636, KL_ARG_V2818_1457]), KL_CTX.KL_LOC_Result_1643][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2727_1636]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2726_1635) else ([setattr(KL_CTX, 'KL_LOC_Direction_1650', tco_apply(shen_newpv, [KL_ARG_V2818_1457])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2726_1635, [symdic.symdic_kl_stream, [KL_CTX.KL_LOC_Direction_1650, []]], KL_ARG_V2818_1457]), [setattr(KL_CTX, 'KL_LOC_Result_1651', [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_Direction_1650, KL_CTX.KL_LOC_Direction2652_1633, KL_ARG_V2818_1457, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1459, KL_ARG_V2818_1457, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_FileName_1631, symdic.symdic_kl_string, KL_ARG_V2817_1456, KL_ARG_V2818_1457, KL_ARG_V2819_1458]))]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2726_1635, KL_ARG_V2818_1457]), KL_CTX.KL_LOC_Result_1651][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2726_1635]) else False))][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2725_1634) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2724_1632) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2723_1630) else False)][(-1)] if shen_eq(symdic.symdic_kl_file, KL_CTX.KL_LOC_V2722_1629) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2721_1628) else False)][(-1)] if shen_eq(symdic.symdic_kl_open, KL_CTX.KL_LOC_V2720_1627) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2719_1626) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1652', [setattr(KL_CTX, 'KL_LOC_V2732_1653', tco_apply(shen_lazyderef, [KL_ARG_V2815_1454, KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_V2733_1654', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2732_1653[0], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_V2734_1655', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2732_1653[1], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_X_1656', KL_CTX.KL_LOC_V2734_1655[0]), [setattr(KL_CTX, 'KL_LOC_V2735_1657', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2734_1655[1], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_A_1658', KL_CTX.KL_LOC_V2735_1657[0]), [setattr(KL_CTX, 'KL_LOC_V2736_1659', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2735_1657[1], KL_ARG_V2818_1457])), ([tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1459, KL_ARG_V2818_1457, (lambda : tail_call(kl_unify, [KL_CTX.KL_LOC_A_1658, KL_ARG_V2816_1455, KL_ARG_V2818_1457, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_X_1656, KL_CTX.KL_LOC_A_1658, KL_ARG_V2817_1456, KL_ARG_V2818_1457, KL_ARG_V2819_1458]))]))])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2736_1659) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2735_1657) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2734_1655) else False)][(-1)] if shen_eq(symdic.symdic_kl_type, KL_CTX.KL_LOC_V2733_1654) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2732_1653) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1660', [setattr(KL_CTX, 'KL_LOC_V2737_1661', tco_apply(shen_lazyderef, [KL_ARG_V2815_1454, KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_V2738_1662', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2737_1661[0], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_V2739_1663', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2737_1661[1], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_V2740_1664', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2739_1663[0], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_V2741_1665', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2739_1663[1], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_A_1666', KL_CTX.KL_LOC_V2741_1665[0]), [setattr(KL_CTX, 'KL_LOC_V2742_1667', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2741_1665[1], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_C_1668', tco_apply(shen_newpv, [KL_ARG_V2818_1457])), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_CTX.KL_LOC_C_1668, tco_apply(shen_demodulate, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1666, KL_ARG_V2818_1457])]), KL_ARG_V2818_1457, (lambda : tail_call(kl_unify, [KL_ARG_V2816_1455, KL_CTX.KL_LOC_C_1668, KL_ARG_V2818_1457, KL_ARG_V2819_1458]))])][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2742_1667) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2741_1665) else False)][(-1)] if shen_eq(symdic.symdic_kl_x58, KL_CTX.KL_LOC_V2740_1664) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2739_1663) else False)][(-1)] if shen_eq(symdic.symdic_kl_inputx43, KL_CTX.KL_LOC_V2738_1662) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2737_1661) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1669', [setattr(KL_CTX, 'KL_LOC_V2743_1670', tco_apply(shen_lazyderef, [KL_ARG_V2815_1454, KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_V2744_1671', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2743_1670[0], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_V2745_1672', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2743_1670[1], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_P_1673', KL_CTX.KL_LOC_V2745_1672[0]), [setattr(KL_CTX, 'KL_LOC_V2746_1674', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2745_1672[1], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_X_1675', KL_CTX.KL_LOC_V2746_1674[0]), [setattr(KL_CTX, 'KL_LOC_V2747_1676', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2746_1674[1], KL_ARG_V2818_1457])), ([tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1459, KL_ARG_V2818_1457, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_P_1673, symdic.symdic_kl_boolean, KL_ARG_V2817_1456, KL_ARG_V2818_1457, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1459, KL_ARG_V2818_1457, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_X_1675, KL_ARG_V2816_1455, [[KL_CTX.KL_LOC_P_1673, [symdic.symdic_kl_x58, [symdic.symdic_kl_verified, []]]], KL_ARG_V2817_1456], KL_ARG_V2818_1457, KL_ARG_V2819_1458]))]))]))])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2747_1676) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2746_1674) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2745_1672) else False)][(-1)] if shen_eq(symdic.symdic_kl_where, KL_CTX.KL_LOC_V2744_1671) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2743_1670) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1677', [setattr(KL_CTX, 'KL_LOC_V2748_1678', tco_apply(shen_lazyderef, [KL_ARG_V2815_1454, KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_V2749_1679', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2748_1678[0], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_V2750_1680', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2748_1678[1], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_Var_1681', KL_CTX.KL_LOC_V2750_1680[0]), [setattr(KL_CTX, 'KL_LOC_V2751_1682', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2750_1680[1], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_Val_1683', KL_CTX.KL_LOC_V2751_1682[0]), [setattr(KL_CTX, 'KL_LOC_V2752_1684', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2751_1682[1], KL_ARG_V2818_1457])), ([tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1459, KL_ARG_V2818_1457, (lambda : tail_call(shen_thx42, [[symdic.symdic_kl_value, [KL_CTX.KL_LOC_Var_1681, []]], KL_ARG_V2816_1455, KL_ARG_V2817_1456, KL_ARG_V2818_1457, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Val_1683, KL_ARG_V2816_1455, KL_ARG_V2817_1456, KL_ARG_V2818_1457, KL_ARG_V2819_1458]))]))])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2752_1684) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2751_1682) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2750_1680) else False)][(-1)] if shen_eq(symdic.symdic_kl_set, KL_CTX.KL_LOC_V2749_1679) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2748_1678) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1685', [setattr(KL_CTX, 'KL_LOC_V2753_1686', tco_apply(shen_lazyderef, [KL_ARG_V2815_1454, KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_V2754_1687', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2753_1686[0], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_V2755_1688', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2753_1686[1], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_F_1689', KL_CTX.KL_LOC_V2755_1688[0]), [setattr(KL_CTX, 'KL_LOC_V2756_1690', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2755_1688[1], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_A_1691', tco_apply(shen_newpv, [KL_ARG_V2818_1457])), [setattr(KL_CTX, 'KL_LOC_Fx38x38_1692', tco_apply(shen_newpv, [KL_ARG_V2818_1457])), [setattr(KL_CTX, 'KL_LOC_B_1693', tco_apply(shen_newpv, [KL_ARG_V2818_1457])), [tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1459, KL_ARG_V2818_1457, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_F_1689, [KL_CTX.KL_LOC_A_1691, [symdic.symdic_kl_x61x61x62, [KL_CTX.KL_LOC_B_1693, []]]], KL_ARG_V2817_1456, KL_ARG_V2818_1457, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1459, KL_ARG_V2818_1457, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Fx38x38_1692, tco_apply(kl_concat, [symdic.symdic_kl_x38x38, tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_F_1689, KL_ARG_V2818_1457])]), KL_ARG_V2818_1457, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1459, KL_ARG_V2818_1457, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Fx38x38_1692, KL_ARG_V2816_1455, [[KL_CTX.KL_LOC_Fx38x38_1692, [symdic.symdic_kl_x58, [KL_CTX.KL_LOC_B_1693, []]]], KL_ARG_V2817_1456], KL_ARG_V2818_1457, KL_ARG_V2819_1458]))]))]))]))]))])][(-1)]][(-1)]][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2756_1690) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2755_1688) else False)][(-1)] if shen_eq(symdic.symdic_shen_x60x45sem, KL_CTX.KL_LOC_V2754_1687) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2753_1686) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1694', [setattr(KL_CTX, 'KL_LOC_V2757_1695', tco_apply(shen_lazyderef, [KL_ARG_V2815_1454, KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_V2758_1696', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2757_1695[0], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_V2759_1697', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2757_1695[1], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_V2760_1698', tco_apply(shen_lazyderef, [KL_ARG_V2816_1455, KL_ARG_V2818_1457])), ([tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V2819_1458])][(-1)] if shen_eq(symdic.symdic_kl_symbol, KL_CTX.KL_LOC_V2760_1698) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2760_1698, symdic.symdic_kl_symbol, KL_ARG_V2818_1457]), [setattr(KL_CTX, 'KL_LOC_Result_1699', [tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V2819_1458])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2760_1698, KL_ARG_V2818_1457]), KL_CTX.KL_LOC_Result_1699][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2760_1698]) else False))][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2759_1697) else False)][(-1)] if shen_eq(symdic.symdic_kl_fail, KL_CTX.KL_LOC_V2758_1696) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2757_1695) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1700', [setattr(KL_CTX, 'KL_LOC_NewHyp_1701', tco_apply(shen_newpv, [KL_ARG_V2818_1457])), [tco_apply(shen_incinfs, []), tco_apply(shen_tx42x45hyps, [KL_ARG_V2817_1456, KL_CTX.KL_LOC_NewHyp_1701, KL_ARG_V2818_1457, (lambda : tail_call(shen_thx42, [KL_ARG_V2815_1454, KL_ARG_V2816_1455, KL_CTX.KL_LOC_NewHyp_1701, KL_ARG_V2818_1457, KL_ARG_V2819_1458]))])][(-1)]][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1702', [setattr(KL_CTX, 'KL_LOC_V2761_1703', tco_apply(shen_lazyderef, [KL_ARG_V2815_1454, KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_V2762_1704', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2761_1703[0], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_V2763_1705', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2761_1703[1], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_F_1706', KL_CTX.KL_LOC_V2763_1705[0]), [setattr(KL_CTX, 'KL_LOC_X_1707', KL_CTX.KL_LOC_V2763_1705[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1459, KL_ARG_V2818_1457, (lambda : tail_call(shen_tx42x45def, [[symdic.symdic_kl_define, [KL_CTX.KL_LOC_F_1706, KL_CTX.KL_LOC_X_1707]], KL_ARG_V2816_1455, KL_ARG_V2817_1456, KL_ARG_V2818_1457, KL_ARG_V2819_1458]))])][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2763_1705) else False)][(-1)] if shen_eq(symdic.symdic_kl_define, KL_CTX.KL_LOC_V2762_1704) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2761_1703) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1708', [setattr(KL_CTX, 'KL_LOC_V2764_1709', tco_apply(shen_lazyderef, [KL_ARG_V2815_1454, KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_V2765_1710', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2764_1709[0], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_V2766_1711', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2764_1709[1], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_F_1712', KL_CTX.KL_LOC_V2766_1711[0]), [setattr(KL_CTX, 'KL_LOC_X_1713', KL_CTX.KL_LOC_V2766_1711[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1459, KL_ARG_V2818_1457, (lambda : tail_call(shen_tx42x45defcc, [[symdic.symdic_kl_defcc, [KL_CTX.KL_LOC_F_1712, KL_CTX.KL_LOC_X_1713]], KL_ARG_V2816_1455, KL_ARG_V2817_1456, KL_ARG_V2818_1457, KL_ARG_V2819_1458]))])][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2766_1711) else False)][(-1)] if shen_eq(symdic.symdic_kl_defcc, KL_CTX.KL_LOC_V2765_1710) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2764_1709) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1714', [setattr(KL_CTX, 'KL_LOC_V2767_1715', tco_apply(shen_lazyderef, [KL_ARG_V2815_1454, KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_V2768_1716', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2767_1715[0], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_V2769_1717', tco_apply(shen_lazyderef, [KL_ARG_V2816_1455, KL_ARG_V2818_1457])), ([tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V2819_1458])][(-1)] if shen_eq(symdic.symdic_kl_symbol, KL_CTX.KL_LOC_V2769_1717) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2769_1717, symdic.symdic_kl_symbol, KL_ARG_V2818_1457]), [setattr(KL_CTX, 'KL_LOC_Result_1718', [tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V2819_1458])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2769_1717, KL_ARG_V2818_1457]), KL_CTX.KL_LOC_Result_1718][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2769_1717]) else False))][(-1)] if shen_eq(symdic.symdic_shen_processx45datatype, KL_CTX.KL_LOC_V2768_1716) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2767_1715) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1719', [setattr(KL_CTX, 'KL_LOC_V2770_1720', tco_apply(shen_lazyderef, [KL_ARG_V2815_1454, KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_V2771_1721', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2770_1720[0], KL_ARG_V2818_1457])), ([setattr(KL_CTX, 'KL_LOC_V2772_1722', tco_apply(shen_lazyderef, [KL_ARG_V2816_1455, KL_ARG_V2818_1457])), ([tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V2819_1458])][(-1)] if shen_eq(symdic.symdic_kl_symbol, KL_CTX.KL_LOC_V2772_1722) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2772_1722, symdic.symdic_kl_symbol, KL_ARG_V2818_1457]), [setattr(KL_CTX, 'KL_LOC_Result_1723', [tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V2819_1458])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2772_1722, KL_ARG_V2818_1457]), KL_CTX.KL_LOC_Result_1723][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2772_1722]) else False))][(-1)] if shen_eq(symdic.symdic_shen_synonymsx45help, KL_CTX.KL_LOC_V2771_1721) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2770_1720) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Datatypes_1724', tco_apply(shen_newpv, [KL_ARG_V2818_1457])), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_CTX.KL_LOC_Datatypes_1724, shen_get(symdic.symdic_shen_x42datatypesx42), KL_ARG_V2818_1457, (lambda : tail_call(shen_udefsx42, [[KL_ARG_V2815_1454, [symdic.symdic_kl_x58, [KL_ARG_V2816_1455, []]]], KL_ARG_V2817_1456, KL_CTX.KL_LOC_Datatypes_1724, KL_ARG_V2818_1457, KL_ARG_V2819_1458]))])][(-1)]][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1719, False) else KL_CTX.KL_LOC_Case_1719)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1714, False) else KL_CTX.KL_LOC_Case_1714)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1708, False) else KL_CTX.KL_LOC_Case_1708)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1702, False) else KL_CTX.KL_LOC_Case_1702)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1700, False) else KL_CTX.KL_LOC_Case_1700)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1694, False) else KL_CTX.KL_LOC_Case_1694)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1685, False) else KL_CTX.KL_LOC_Case_1685)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1677, False) else KL_CTX.KL_LOC_Case_1677)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1669, False) else KL_CTX.KL_LOC_Case_1669)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1660, False) else KL_CTX.KL_LOC_Case_1660)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1652, False) else KL_CTX.KL_LOC_Case_1652)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1625, False) else KL_CTX.KL_LOC_Case_1625)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1612, False) else KL_CTX.KL_LOC_Case_1612)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1566, False) else KL_CTX.KL_LOC_Case_1566)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1556, False) else KL_CTX.KL_LOC_Case_1556)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1531, False) else KL_CTX.KL_LOC_Case_1531)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1501, False) else KL_CTX.KL_LOC_Case_1501)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1476, False) else KL_CTX.KL_LOC_Case_1476)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1469, False) else KL_CTX.KL_LOC_Case_1469)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1465, False) else KL_CTX.KL_LOC_Case_1465)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1464, False) else KL_CTX.KL_LOC_Case_1464)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1463, False) else KL_CTX.KL_LOC_Case_1463)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1461, False) else KL_CTX.KL_LOC_Case_1461)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1460, False) else KL_CTX.KL_LOC_Case_1460)][(-1)]])][(-1)]
shen_add_fun('shen.th*', shen_thx42)

@tail_recursion
def shen_tx42x45hyps(KL_ARG_V2820_1725, KL_ARG_V2821_1726, KL_ARG_V2822_1727, KL_ARG_V2823_1728):

    class KL_Context:
        KL_LOC_Case_1729 = None
        KL_LOC_V2567_1730 = None
        KL_LOC_V2568_1731 = None
        KL_LOC_V2569_1732 = None
        KL_LOC_V2570_1733 = None
        KL_LOC_V2571_1734 = None
        KL_LOC_X_1735 = None
        KL_LOC_V2572_1736 = None
        KL_LOC_Y_1737 = None
        KL_LOC_V2573_1738 = None
        KL_LOC_V2574_1739 = None
        KL_LOC_V2575_1740 = None
        KL_LOC_V2576_1741 = None
        KL_LOC_V2577_1742 = None
        KL_LOC_V2578_1743 = None
        KL_LOC_V2579_1744 = None
        KL_LOC_A_1745 = None
        KL_LOC_V2580_1746 = None
        KL_LOC_V2581_1747 = None
        KL_LOC_Hyp_1748 = None
        KL_LOC_Result_1749 = None
        KL_LOC_Hyp_1750 = None
        KL_LOC_Result_1751 = None
        KL_LOC_V2582_1752 = None
        KL_LOC_Hyp_1753 = None
        KL_LOC_Result_1754 = None
        KL_LOC_Hyp_1755 = None
        KL_LOC_A_1756 = None
        KL_LOC_Result_1757 = None
        KL_LOC_V2583_1758 = None
        KL_LOC_Hyp_1759 = None
        KL_LOC_Result_1760 = None
        KL_LOC_Hyp_1761 = None
        KL_LOC_Result_1762 = None
        KL_LOC_V2584_1763 = None
        KL_LOC_A_1764 = None
        KL_LOC_V2585_1765 = None
        KL_LOC_V2586_1766 = None
        KL_LOC_Hyp_1767 = None
        KL_LOC_Result_1768 = None
        KL_LOC_Hyp_1769 = None
        KL_LOC_Result_1770 = None
        KL_LOC_V2587_1771 = None
        KL_LOC_Hyp_1772 = None
        KL_LOC_Result_1773 = None
        KL_LOC_Hyp_1774 = None
        KL_LOC_A_1775 = None
        KL_LOC_Result_1776 = None
        KL_LOC_V2588_1777 = None
        KL_LOC_Hyp_1778 = None
        KL_LOC_Result_1779 = None
        KL_LOC_Hyp_1780 = None
        KL_LOC_A_1781 = None
        KL_LOC_Result_1782 = None
        KL_LOC_V2589_1783 = None
        KL_LOC_Hyp_1784 = None
        KL_LOC_Result_1785 = None
        KL_LOC_Hyp_1786 = None
        KL_LOC_Case_1787 = None
        KL_LOC_V2590_1788 = None
        KL_LOC_V2591_1789 = None
        KL_LOC_V2592_1790 = None
        KL_LOC_V2593_1791 = None
        KL_LOC_V2594_1792 = None
        KL_LOC_X_1793 = None
        KL_LOC_V2595_1794 = None
        KL_LOC_Y_1795 = None
        KL_LOC_V2596_1796 = None
        KL_LOC_V2597_1797 = None
        KL_LOC_V2598_1798 = None
        KL_LOC_V2599_1799 = None
        KL_LOC_V2600_1800 = None
        KL_LOC_A_1801 = None
        KL_LOC_V2601_1802 = None
        KL_LOC_V2602_1803 = None
        KL_LOC_V2603_1804 = None
        KL_LOC_B_1805 = None
        KL_LOC_V2604_1806 = None
        KL_LOC_V2605_1807 = None
        KL_LOC_Hyp_1808 = None
        KL_LOC_Result_1809 = None
        KL_LOC_Hyp_1810 = None
        KL_LOC_Result_1811 = None
        KL_LOC_V2606_1812 = None
        KL_LOC_Hyp_1813 = None
        KL_LOC_Result_1814 = None
        KL_LOC_Hyp_1815 = None
        KL_LOC_B_1816 = None
        KL_LOC_Result_1817 = None
        KL_LOC_V2607_1818 = None
        KL_LOC_Hyp_1819 = None
        KL_LOC_Result_1820 = None
        KL_LOC_Hyp_1821 = None
        KL_LOC_Result_1822 = None
        KL_LOC_V2608_1823 = None
        KL_LOC_B_1824 = None
        KL_LOC_V2609_1825 = None
        KL_LOC_V2610_1826 = None
        KL_LOC_Hyp_1827 = None
        KL_LOC_Result_1828 = None
        KL_LOC_Hyp_1829 = None
        KL_LOC_Result_1830 = None
        KL_LOC_V2611_1831 = None
        KL_LOC_Hyp_1832 = None
        KL_LOC_Result_1833 = None
        KL_LOC_Hyp_1834 = None
        KL_LOC_B_1835 = None
        KL_LOC_Result_1836 = None
        KL_LOC_V2612_1837 = None
        KL_LOC_Hyp_1838 = None
        KL_LOC_Result_1839 = None
        KL_LOC_Hyp_1840 = None
        KL_LOC_B_1841 = None
        KL_LOC_Result_1842 = None
        KL_LOC_V2613_1843 = None
        KL_LOC_Hyp_1844 = None
        KL_LOC_Result_1845 = None
        KL_LOC_Hyp_1846 = None
        KL_LOC_A_1847 = None
        KL_LOC_B_1848 = None
        KL_LOC_Result_1849 = None
        KL_LOC_V2614_1850 = None
        KL_LOC_Hyp_1851 = None
        KL_LOC_Result_1852 = None
        KL_LOC_Hyp_1853 = None
        KL_LOC_Case_1854 = None
        KL_LOC_V2615_1855 = None
        KL_LOC_V2616_1856 = None
        KL_LOC_V2617_1857 = None
        KL_LOC_V2618_1858 = None
        KL_LOC_V2619_1859 = None
        KL_LOC_X_1860 = None
        KL_LOC_V2620_1861 = None
        KL_LOC_Y_1862 = None
        KL_LOC_V2621_1863 = None
        KL_LOC_V2622_1864 = None
        KL_LOC_V2623_1865 = None
        KL_LOC_V2624_1866 = None
        KL_LOC_V2625_1867 = None
        KL_LOC_V2626_1868 = None
        KL_LOC_V2627_1869 = None
        KL_LOC_A_1870 = None
        KL_LOC_V2628_1871 = None
        KL_LOC_V2629_1872 = None
        KL_LOC_Hyp_1873 = None
        KL_LOC_Result_1874 = None
        KL_LOC_Hyp_1875 = None
        KL_LOC_Result_1876 = None
        KL_LOC_V2630_1877 = None
        KL_LOC_Hyp_1878 = None
        KL_LOC_Result_1879 = None
        KL_LOC_Hyp_1880 = None
        KL_LOC_A_1881 = None
        KL_LOC_Result_1882 = None
        KL_LOC_V2631_1883 = None
        KL_LOC_Hyp_1884 = None
        KL_LOC_Result_1885 = None
        KL_LOC_Hyp_1886 = None
        KL_LOC_Result_1887 = None
        KL_LOC_V2632_1888 = None
        KL_LOC_A_1889 = None
        KL_LOC_V2633_1890 = None
        KL_LOC_V2634_1891 = None
        KL_LOC_Hyp_1892 = None
        KL_LOC_Result_1893 = None
        KL_LOC_Hyp_1894 = None
        KL_LOC_Result_1895 = None
        KL_LOC_V2635_1896 = None
        KL_LOC_Hyp_1897 = None
        KL_LOC_Result_1898 = None
        KL_LOC_Hyp_1899 = None
        KL_LOC_A_1900 = None
        KL_LOC_Result_1901 = None
        KL_LOC_V2636_1902 = None
        KL_LOC_Hyp_1903 = None
        KL_LOC_Result_1904 = None
        KL_LOC_Hyp_1905 = None
        KL_LOC_A_1906 = None
        KL_LOC_Result_1907 = None
        KL_LOC_V2637_1908 = None
        KL_LOC_Hyp_1909 = None
        KL_LOC_Result_1910 = None
        KL_LOC_Hyp_1911 = None
        KL_LOC_Case_1912 = None
        KL_LOC_V2638_1913 = None
        KL_LOC_V2639_1914 = None
        KL_LOC_V2640_1915 = None
        KL_LOC_V2641_1916 = None
        KL_LOC_V2642_1917 = None
        KL_LOC_X_1918 = None
        KL_LOC_V2643_1919 = None
        KL_LOC_Y_1920 = None
        KL_LOC_V2644_1921 = None
        KL_LOC_V2645_1922 = None
        KL_LOC_V2646_1923 = None
        KL_LOC_V2647_1924 = None
        KL_LOC_V2648_1925 = None
        KL_LOC_V2649_1926 = None
        KL_LOC_Hyp_1927 = None
        KL_LOC_Result_1928 = None
        KL_LOC_Hyp_1929 = None
        KL_LOC_Result_1930 = None
        KL_LOC_V2650_1931 = None
        KL_LOC_Hyp_1932 = None
        KL_LOC_Result_1933 = None
        KL_LOC_Hyp_1934 = None
        KL_LOC_V2651_1935 = None
        KL_LOC_X_1936 = None
        KL_LOC_Hyp_1937 = None
        KL_LOC_NewHyps_1938 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Case_1729', [setattr(KL_CTX, 'KL_LOC_V2567_1730', tco_apply(shen_lazyderef, [KL_ARG_V2820_1725, KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_V2568_1731', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2567_1730[0], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_V2569_1732', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2568_1731[0], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_V2570_1733', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2569_1732[0], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_V2571_1734', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2569_1732[1], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_X_1735', KL_CTX.KL_LOC_V2571_1734[0]), [setattr(KL_CTX, 'KL_LOC_V2572_1736', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2571_1734[1], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_Y_1737', KL_CTX.KL_LOC_V2572_1736[0]), [setattr(KL_CTX, 'KL_LOC_V2573_1738', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2572_1736[1], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_V2574_1739', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2568_1731[1], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_V2575_1740', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2574_1739[0], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_V2576_1741', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2574_1739[1], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_V2577_1742', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2576_1741[0], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_V2578_1743', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2577_1742[0], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_V2579_1744', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2577_1742[1], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_A_1745', KL_CTX.KL_LOC_V2579_1744[0]), [setattr(KL_CTX, 'KL_LOC_V2580_1746', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2579_1744[1], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_V2581_1747', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2576_1741[1], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1748', KL_CTX.KL_LOC_V2567_1730[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2821_1726, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1735, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1745, KL_ARG_V2822_1727]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1737, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_list, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1745, KL_ARG_V2822_1727]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1748, KL_ARG_V2822_1727])]], KL_ARG_V2822_1727, KL_ARG_V2823_1728])][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2581_1747) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2581_1747, [], KL_ARG_V2822_1727]), [setattr(KL_CTX, 'KL_LOC_Result_1749', [setattr(KL_CTX, 'KL_LOC_Hyp_1750', KL_CTX.KL_LOC_V2567_1730[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2821_1726, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1735, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1745, KL_ARG_V2822_1727]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1737, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_list, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1745, KL_ARG_V2822_1727]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1750, KL_ARG_V2822_1727])]], KL_ARG_V2822_1727, KL_ARG_V2823_1728])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2581_1747, KL_ARG_V2822_1727]), KL_CTX.KL_LOC_Result_1749][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2581_1747]) else False))][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2580_1746) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2580_1746, [], KL_ARG_V2822_1727]), [setattr(KL_CTX, 'KL_LOC_Result_1751', [setattr(KL_CTX, 'KL_LOC_V2582_1752', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2576_1741[1], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1753', KL_CTX.KL_LOC_V2567_1730[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2821_1726, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1735, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1745, KL_ARG_V2822_1727]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1737, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_list, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1745, KL_ARG_V2822_1727]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1753, KL_ARG_V2822_1727])]], KL_ARG_V2822_1727, KL_ARG_V2823_1728])][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2582_1752) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2582_1752, [], KL_ARG_V2822_1727]), [setattr(KL_CTX, 'KL_LOC_Result_1754', [setattr(KL_CTX, 'KL_LOC_Hyp_1755', KL_CTX.KL_LOC_V2567_1730[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2821_1726, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1735, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1745, KL_ARG_V2822_1727]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1737, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_list, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1745, KL_ARG_V2822_1727]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1755, KL_ARG_V2822_1727])]], KL_ARG_V2822_1727, KL_ARG_V2823_1728])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2582_1752, KL_ARG_V2822_1727]), KL_CTX.KL_LOC_Result_1754][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2582_1752]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2580_1746, KL_ARG_V2822_1727]), KL_CTX.KL_LOC_Result_1751][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2580_1746]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2579_1744) else ([setattr(KL_CTX, 'KL_LOC_A_1756', tco_apply(shen_newpv, [KL_ARG_V2822_1727])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2579_1744, [KL_CTX.KL_LOC_A_1756, []], KL_ARG_V2822_1727]), [setattr(KL_CTX, 'KL_LOC_Result_1757', [setattr(KL_CTX, 'KL_LOC_V2583_1758', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2576_1741[1], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1759', KL_CTX.KL_LOC_V2567_1730[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2821_1726, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1735, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1756, KL_ARG_V2822_1727]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1737, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_list, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1756, KL_ARG_V2822_1727]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1759, KL_ARG_V2822_1727])]], KL_ARG_V2822_1727, KL_ARG_V2823_1728])][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2583_1758) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2583_1758, [], KL_ARG_V2822_1727]), [setattr(KL_CTX, 'KL_LOC_Result_1760', [setattr(KL_CTX, 'KL_LOC_Hyp_1761', KL_CTX.KL_LOC_V2567_1730[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2821_1726, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1735, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1756, KL_ARG_V2822_1727]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1737, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_list, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1756, KL_ARG_V2822_1727]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1761, KL_ARG_V2822_1727])]], KL_ARG_V2822_1727, KL_ARG_V2823_1728])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2583_1758, KL_ARG_V2822_1727]), KL_CTX.KL_LOC_Result_1760][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2583_1758]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2579_1744, KL_ARG_V2822_1727]), KL_CTX.KL_LOC_Result_1757][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2579_1744]) else False))][(-1)] if shen_eq(symdic.symdic_kl_list, KL_CTX.KL_LOC_V2578_1743) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2578_1743, symdic.symdic_kl_list, KL_ARG_V2822_1727]), [setattr(KL_CTX, 'KL_LOC_Result_1762', [setattr(KL_CTX, 'KL_LOC_V2584_1763', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2577_1742[1], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_A_1764', KL_CTX.KL_LOC_V2584_1763[0]), [setattr(KL_CTX, 'KL_LOC_V2585_1765', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2584_1763[1], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_V2586_1766', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2576_1741[1], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1767', KL_CTX.KL_LOC_V2567_1730[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2821_1726, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1735, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1764, KL_ARG_V2822_1727]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1737, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_list, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1764, KL_ARG_V2822_1727]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1767, KL_ARG_V2822_1727])]], KL_ARG_V2822_1727, KL_ARG_V2823_1728])][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2586_1766) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2586_1766, [], KL_ARG_V2822_1727]), [setattr(KL_CTX, 'KL_LOC_Result_1768', [setattr(KL_CTX, 'KL_LOC_Hyp_1769', KL_CTX.KL_LOC_V2567_1730[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2821_1726, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1735, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1764, KL_ARG_V2822_1727]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1737, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_list, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1764, KL_ARG_V2822_1727]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1769, KL_ARG_V2822_1727])]], KL_ARG_V2822_1727, KL_ARG_V2823_1728])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2586_1766, KL_ARG_V2822_1727]), KL_CTX.KL_LOC_Result_1768][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2586_1766]) else False))][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2585_1765) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2585_1765, [], KL_ARG_V2822_1727]), [setattr(KL_CTX, 'KL_LOC_Result_1770', [setattr(KL_CTX, 'KL_LOC_V2587_1771', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2576_1741[1], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1772', KL_CTX.KL_LOC_V2567_1730[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2821_1726, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1735, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1764, KL_ARG_V2822_1727]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1737, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_list, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1764, KL_ARG_V2822_1727]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1772, KL_ARG_V2822_1727])]], KL_ARG_V2822_1727, KL_ARG_V2823_1728])][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2587_1771) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2587_1771, [], KL_ARG_V2822_1727]), [setattr(KL_CTX, 'KL_LOC_Result_1773', [setattr(KL_CTX, 'KL_LOC_Hyp_1774', KL_CTX.KL_LOC_V2567_1730[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2821_1726, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1735, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1764, KL_ARG_V2822_1727]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1737, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_list, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1764, KL_ARG_V2822_1727]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1774, KL_ARG_V2822_1727])]], KL_ARG_V2822_1727, KL_ARG_V2823_1728])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2587_1771, KL_ARG_V2822_1727]), KL_CTX.KL_LOC_Result_1773][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2587_1771]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2585_1765, KL_ARG_V2822_1727]), KL_CTX.KL_LOC_Result_1770][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2585_1765]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2584_1763) else ([setattr(KL_CTX, 'KL_LOC_A_1775', tco_apply(shen_newpv, [KL_ARG_V2822_1727])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2584_1763, [KL_CTX.KL_LOC_A_1775, []], KL_ARG_V2822_1727]), [setattr(KL_CTX, 'KL_LOC_Result_1776', [setattr(KL_CTX, 'KL_LOC_V2588_1777', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2576_1741[1], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1778', KL_CTX.KL_LOC_V2567_1730[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2821_1726, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1735, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1775, KL_ARG_V2822_1727]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1737, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_list, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1775, KL_ARG_V2822_1727]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1778, KL_ARG_V2822_1727])]], KL_ARG_V2822_1727, KL_ARG_V2823_1728])][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2588_1777) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2588_1777, [], KL_ARG_V2822_1727]), [setattr(KL_CTX, 'KL_LOC_Result_1779', [setattr(KL_CTX, 'KL_LOC_Hyp_1780', KL_CTX.KL_LOC_V2567_1730[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2821_1726, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1735, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1775, KL_ARG_V2822_1727]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1737, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_list, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1775, KL_ARG_V2822_1727]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1780, KL_ARG_V2822_1727])]], KL_ARG_V2822_1727, KL_ARG_V2823_1728])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2588_1777, KL_ARG_V2822_1727]), KL_CTX.KL_LOC_Result_1779][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2588_1777]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2584_1763, KL_ARG_V2822_1727]), KL_CTX.KL_LOC_Result_1776][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2584_1763]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2578_1743, KL_ARG_V2822_1727]), KL_CTX.KL_LOC_Result_1762][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2578_1743]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2577_1742) else ([setattr(KL_CTX, 'KL_LOC_A_1781', tco_apply(shen_newpv, [KL_ARG_V2822_1727])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2577_1742, [symdic.symdic_kl_list, [KL_CTX.KL_LOC_A_1781, []]], KL_ARG_V2822_1727]), [setattr(KL_CTX, 'KL_LOC_Result_1782', [setattr(KL_CTX, 'KL_LOC_V2589_1783', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2576_1741[1], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1784', KL_CTX.KL_LOC_V2567_1730[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2821_1726, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1735, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1781, KL_ARG_V2822_1727]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1737, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_list, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1781, KL_ARG_V2822_1727]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1784, KL_ARG_V2822_1727])]], KL_ARG_V2822_1727, KL_ARG_V2823_1728])][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2589_1783) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2589_1783, [], KL_ARG_V2822_1727]), [setattr(KL_CTX, 'KL_LOC_Result_1785', [setattr(KL_CTX, 'KL_LOC_Hyp_1786', KL_CTX.KL_LOC_V2567_1730[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2821_1726, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1735, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1781, KL_ARG_V2822_1727]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1737, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_list, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1781, KL_ARG_V2822_1727]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1786, KL_ARG_V2822_1727])]], KL_ARG_V2822_1727, KL_ARG_V2823_1728])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2589_1783, KL_ARG_V2822_1727]), KL_CTX.KL_LOC_Result_1785][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2589_1783]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2577_1742, KL_ARG_V2822_1727]), KL_CTX.KL_LOC_Result_1782][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2577_1742]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2576_1741) else False)][(-1)] if shen_eq(symdic.symdic_kl_x58, KL_CTX.KL_LOC_V2575_1740) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2574_1739) else False)][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2573_1738) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2572_1736) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2571_1734) else False)][(-1)] if shen_eq(symdic.symdic_kl_cons, KL_CTX.KL_LOC_V2570_1733) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2569_1732) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2568_1731) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2567_1730) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1787', [setattr(KL_CTX, 'KL_LOC_V2590_1788', tco_apply(shen_lazyderef, [KL_ARG_V2820_1725, KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_V2591_1789', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2590_1788[0], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_V2592_1790', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2591_1789[0], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_V2593_1791', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2592_1790[0], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_V2594_1792', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2592_1790[1], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_X_1793', KL_CTX.KL_LOC_V2594_1792[0]), [setattr(KL_CTX, 'KL_LOC_V2595_1794', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2594_1792[1], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_Y_1795', KL_CTX.KL_LOC_V2595_1794[0]), [setattr(KL_CTX, 'KL_LOC_V2596_1796', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2595_1794[1], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_V2597_1797', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2591_1789[1], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_V2598_1798', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2597_1797[0], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_V2599_1799', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2597_1797[1], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_V2600_1800', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2599_1799[0], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_A_1801', KL_CTX.KL_LOC_V2600_1800[0]), [setattr(KL_CTX, 'KL_LOC_V2601_1802', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2600_1800[1], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_V2602_1803', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2601_1802[0], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_V2603_1804', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2601_1802[1], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_B_1805', KL_CTX.KL_LOC_V2603_1804[0]), [setattr(KL_CTX, 'KL_LOC_V2604_1806', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2603_1804[1], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_V2605_1807', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2599_1799[1], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1808', KL_CTX.KL_LOC_V2590_1788[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2821_1726, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1793, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1801, KL_ARG_V2822_1727]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1795, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_1805, KL_ARG_V2822_1727]), []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1808, KL_ARG_V2822_1727])]], KL_ARG_V2822_1727, KL_ARG_V2823_1728])][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2605_1807) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2605_1807, [], KL_ARG_V2822_1727]), [setattr(KL_CTX, 'KL_LOC_Result_1809', [setattr(KL_CTX, 'KL_LOC_Hyp_1810', KL_CTX.KL_LOC_V2590_1788[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2821_1726, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1793, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1801, KL_ARG_V2822_1727]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1795, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_1805, KL_ARG_V2822_1727]), []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1810, KL_ARG_V2822_1727])]], KL_ARG_V2822_1727, KL_ARG_V2823_1728])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2605_1807, KL_ARG_V2822_1727]), KL_CTX.KL_LOC_Result_1809][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2605_1807]) else False))][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2604_1806) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2604_1806, [], KL_ARG_V2822_1727]), [setattr(KL_CTX, 'KL_LOC_Result_1811', [setattr(KL_CTX, 'KL_LOC_V2606_1812', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2599_1799[1], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1813', KL_CTX.KL_LOC_V2590_1788[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2821_1726, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1793, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1801, KL_ARG_V2822_1727]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1795, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_1805, KL_ARG_V2822_1727]), []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1813, KL_ARG_V2822_1727])]], KL_ARG_V2822_1727, KL_ARG_V2823_1728])][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2606_1812) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2606_1812, [], KL_ARG_V2822_1727]), [setattr(KL_CTX, 'KL_LOC_Result_1814', [setattr(KL_CTX, 'KL_LOC_Hyp_1815', KL_CTX.KL_LOC_V2590_1788[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2821_1726, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1793, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1801, KL_ARG_V2822_1727]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1795, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_1805, KL_ARG_V2822_1727]), []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1815, KL_ARG_V2822_1727])]], KL_ARG_V2822_1727, KL_ARG_V2823_1728])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2606_1812, KL_ARG_V2822_1727]), KL_CTX.KL_LOC_Result_1814][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2606_1812]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2604_1806, KL_ARG_V2822_1727]), KL_CTX.KL_LOC_Result_1811][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2604_1806]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2603_1804) else ([setattr(KL_CTX, 'KL_LOC_B_1816', tco_apply(shen_newpv, [KL_ARG_V2822_1727])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2603_1804, [KL_CTX.KL_LOC_B_1816, []], KL_ARG_V2822_1727]), [setattr(KL_CTX, 'KL_LOC_Result_1817', [setattr(KL_CTX, 'KL_LOC_V2607_1818', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2599_1799[1], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1819', KL_CTX.KL_LOC_V2590_1788[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2821_1726, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1793, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1801, KL_ARG_V2822_1727]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1795, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_1816, KL_ARG_V2822_1727]), []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1819, KL_ARG_V2822_1727])]], KL_ARG_V2822_1727, KL_ARG_V2823_1728])][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2607_1818) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2607_1818, [], KL_ARG_V2822_1727]), [setattr(KL_CTX, 'KL_LOC_Result_1820', [setattr(KL_CTX, 'KL_LOC_Hyp_1821', KL_CTX.KL_LOC_V2590_1788[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2821_1726, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1793, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1801, KL_ARG_V2822_1727]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1795, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_1816, KL_ARG_V2822_1727]), []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1821, KL_ARG_V2822_1727])]], KL_ARG_V2822_1727, KL_ARG_V2823_1728])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2607_1818, KL_ARG_V2822_1727]), KL_CTX.KL_LOC_Result_1820][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2607_1818]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2603_1804, KL_ARG_V2822_1727]), KL_CTX.KL_LOC_Result_1817][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2603_1804]) else False))][(-1)] if shen_eq(symdic.symdic_kl_x42, KL_CTX.KL_LOC_V2602_1803) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2602_1803, symdic.symdic_kl_x42, KL_ARG_V2822_1727]), [setattr(KL_CTX, 'KL_LOC_Result_1822', [setattr(KL_CTX, 'KL_LOC_V2608_1823', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2601_1802[1], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_B_1824', KL_CTX.KL_LOC_V2608_1823[0]), [setattr(KL_CTX, 'KL_LOC_V2609_1825', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2608_1823[1], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_V2610_1826', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2599_1799[1], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1827', KL_CTX.KL_LOC_V2590_1788[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2821_1726, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1793, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1801, KL_ARG_V2822_1727]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1795, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_1824, KL_ARG_V2822_1727]), []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1827, KL_ARG_V2822_1727])]], KL_ARG_V2822_1727, KL_ARG_V2823_1728])][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2610_1826) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2610_1826, [], KL_ARG_V2822_1727]), [setattr(KL_CTX, 'KL_LOC_Result_1828', [setattr(KL_CTX, 'KL_LOC_Hyp_1829', KL_CTX.KL_LOC_V2590_1788[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2821_1726, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1793, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1801, KL_ARG_V2822_1727]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1795, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_1824, KL_ARG_V2822_1727]), []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1829, KL_ARG_V2822_1727])]], KL_ARG_V2822_1727, KL_ARG_V2823_1728])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2610_1826, KL_ARG_V2822_1727]), KL_CTX.KL_LOC_Result_1828][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2610_1826]) else False))][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2609_1825) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2609_1825, [], KL_ARG_V2822_1727]), [setattr(KL_CTX, 'KL_LOC_Result_1830', [setattr(KL_CTX, 'KL_LOC_V2611_1831', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2599_1799[1], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1832', KL_CTX.KL_LOC_V2590_1788[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2821_1726, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1793, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1801, KL_ARG_V2822_1727]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1795, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_1824, KL_ARG_V2822_1727]), []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1832, KL_ARG_V2822_1727])]], KL_ARG_V2822_1727, KL_ARG_V2823_1728])][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2611_1831) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2611_1831, [], KL_ARG_V2822_1727]), [setattr(KL_CTX, 'KL_LOC_Result_1833', [setattr(KL_CTX, 'KL_LOC_Hyp_1834', KL_CTX.KL_LOC_V2590_1788[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2821_1726, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1793, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1801, KL_ARG_V2822_1727]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1795, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_1824, KL_ARG_V2822_1727]), []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1834, KL_ARG_V2822_1727])]], KL_ARG_V2822_1727, KL_ARG_V2823_1728])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2611_1831, KL_ARG_V2822_1727]), KL_CTX.KL_LOC_Result_1833][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2611_1831]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2609_1825, KL_ARG_V2822_1727]), KL_CTX.KL_LOC_Result_1830][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2609_1825]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2608_1823) else ([setattr(KL_CTX, 'KL_LOC_B_1835', tco_apply(shen_newpv, [KL_ARG_V2822_1727])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2608_1823, [KL_CTX.KL_LOC_B_1835, []], KL_ARG_V2822_1727]), [setattr(KL_CTX, 'KL_LOC_Result_1836', [setattr(KL_CTX, 'KL_LOC_V2612_1837', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2599_1799[1], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1838', KL_CTX.KL_LOC_V2590_1788[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2821_1726, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1793, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1801, KL_ARG_V2822_1727]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1795, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_1835, KL_ARG_V2822_1727]), []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1838, KL_ARG_V2822_1727])]], KL_ARG_V2822_1727, KL_ARG_V2823_1728])][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2612_1837) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2612_1837, [], KL_ARG_V2822_1727]), [setattr(KL_CTX, 'KL_LOC_Result_1839', [setattr(KL_CTX, 'KL_LOC_Hyp_1840', KL_CTX.KL_LOC_V2590_1788[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2821_1726, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1793, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1801, KL_ARG_V2822_1727]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1795, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_1835, KL_ARG_V2822_1727]), []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1840, KL_ARG_V2822_1727])]], KL_ARG_V2822_1727, KL_ARG_V2823_1728])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2612_1837, KL_ARG_V2822_1727]), KL_CTX.KL_LOC_Result_1839][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2612_1837]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2608_1823, KL_ARG_V2822_1727]), KL_CTX.KL_LOC_Result_1836][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2608_1823]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2602_1803, KL_ARG_V2822_1727]), KL_CTX.KL_LOC_Result_1822][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2602_1803]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2601_1802) else ([setattr(KL_CTX, 'KL_LOC_B_1841', tco_apply(shen_newpv, [KL_ARG_V2822_1727])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2601_1802, [symdic.symdic_kl_x42, [KL_CTX.KL_LOC_B_1841, []]], KL_ARG_V2822_1727]), [setattr(KL_CTX, 'KL_LOC_Result_1842', [setattr(KL_CTX, 'KL_LOC_V2613_1843', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2599_1799[1], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1844', KL_CTX.KL_LOC_V2590_1788[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2821_1726, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1793, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1801, KL_ARG_V2822_1727]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1795, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_1841, KL_ARG_V2822_1727]), []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1844, KL_ARG_V2822_1727])]], KL_ARG_V2822_1727, KL_ARG_V2823_1728])][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2613_1843) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2613_1843, [], KL_ARG_V2822_1727]), [setattr(KL_CTX, 'KL_LOC_Result_1845', [setattr(KL_CTX, 'KL_LOC_Hyp_1846', KL_CTX.KL_LOC_V2590_1788[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2821_1726, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1793, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1801, KL_ARG_V2822_1727]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1795, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_1841, KL_ARG_V2822_1727]), []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1846, KL_ARG_V2822_1727])]], KL_ARG_V2822_1727, KL_ARG_V2823_1728])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2613_1843, KL_ARG_V2822_1727]), KL_CTX.KL_LOC_Result_1845][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2613_1843]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2601_1802, KL_ARG_V2822_1727]), KL_CTX.KL_LOC_Result_1842][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2601_1802]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2600_1800) else ([setattr(KL_CTX, 'KL_LOC_A_1847', tco_apply(shen_newpv, [KL_ARG_V2822_1727])), [setattr(KL_CTX, 'KL_LOC_B_1848', tco_apply(shen_newpv, [KL_ARG_V2822_1727])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2600_1800, [KL_CTX.KL_LOC_A_1847, [symdic.symdic_kl_x42, [KL_CTX.KL_LOC_B_1848, []]]], KL_ARG_V2822_1727]), [setattr(KL_CTX, 'KL_LOC_Result_1849', [setattr(KL_CTX, 'KL_LOC_V2614_1850', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2599_1799[1], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1851', KL_CTX.KL_LOC_V2590_1788[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2821_1726, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1793, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1847, KL_ARG_V2822_1727]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1795, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_1848, KL_ARG_V2822_1727]), []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1851, KL_ARG_V2822_1727])]], KL_ARG_V2822_1727, KL_ARG_V2823_1728])][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2614_1850) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2614_1850, [], KL_ARG_V2822_1727]), [setattr(KL_CTX, 'KL_LOC_Result_1852', [setattr(KL_CTX, 'KL_LOC_Hyp_1853', KL_CTX.KL_LOC_V2590_1788[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2821_1726, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1793, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1847, KL_ARG_V2822_1727]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1795, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_1848, KL_ARG_V2822_1727]), []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1853, KL_ARG_V2822_1727])]], KL_ARG_V2822_1727, KL_ARG_V2823_1728])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2614_1850, KL_ARG_V2822_1727]), KL_CTX.KL_LOC_Result_1852][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2614_1850]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2600_1800, KL_ARG_V2822_1727]), KL_CTX.KL_LOC_Result_1849][(-1)]][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2600_1800]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2599_1799) else False)][(-1)] if shen_eq(symdic.symdic_kl_x58, KL_CTX.KL_LOC_V2598_1798) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2597_1797) else False)][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2596_1796) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2595_1794) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2594_1792) else False)][(-1)] if shen_eq(symdic.symdic_kl_x64p, KL_CTX.KL_LOC_V2593_1791) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2592_1790) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2591_1789) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2590_1788) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1854', [setattr(KL_CTX, 'KL_LOC_V2615_1855', tco_apply(shen_lazyderef, [KL_ARG_V2820_1725, KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_V2616_1856', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2615_1855[0], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_V2617_1857', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2616_1856[0], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_V2618_1858', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2617_1857[0], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_V2619_1859', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2617_1857[1], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_X_1860', KL_CTX.KL_LOC_V2619_1859[0]), [setattr(KL_CTX, 'KL_LOC_V2620_1861', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2619_1859[1], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_Y_1862', KL_CTX.KL_LOC_V2620_1861[0]), [setattr(KL_CTX, 'KL_LOC_V2621_1863', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2620_1861[1], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_V2622_1864', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2616_1856[1], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_V2623_1865', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2622_1864[0], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_V2624_1866', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2622_1864[1], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_V2625_1867', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2624_1866[0], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_V2626_1868', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2625_1867[0], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_V2627_1869', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2625_1867[1], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_A_1870', KL_CTX.KL_LOC_V2627_1869[0]), [setattr(KL_CTX, 'KL_LOC_V2628_1871', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2627_1869[1], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_V2629_1872', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2624_1866[1], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1873', KL_CTX.KL_LOC_V2615_1855[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2821_1726, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1860, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1870, KL_ARG_V2822_1727]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1862, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_vector, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1870, KL_ARG_V2822_1727]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1873, KL_ARG_V2822_1727])]], KL_ARG_V2822_1727, KL_ARG_V2823_1728])][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2629_1872) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2629_1872, [], KL_ARG_V2822_1727]), [setattr(KL_CTX, 'KL_LOC_Result_1874', [setattr(KL_CTX, 'KL_LOC_Hyp_1875', KL_CTX.KL_LOC_V2615_1855[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2821_1726, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1860, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1870, KL_ARG_V2822_1727]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1862, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_vector, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1870, KL_ARG_V2822_1727]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1875, KL_ARG_V2822_1727])]], KL_ARG_V2822_1727, KL_ARG_V2823_1728])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2629_1872, KL_ARG_V2822_1727]), KL_CTX.KL_LOC_Result_1874][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2629_1872]) else False))][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2628_1871) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2628_1871, [], KL_ARG_V2822_1727]), [setattr(KL_CTX, 'KL_LOC_Result_1876', [setattr(KL_CTX, 'KL_LOC_V2630_1877', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2624_1866[1], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1878', KL_CTX.KL_LOC_V2615_1855[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2821_1726, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1860, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1870, KL_ARG_V2822_1727]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1862, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_vector, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1870, KL_ARG_V2822_1727]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1878, KL_ARG_V2822_1727])]], KL_ARG_V2822_1727, KL_ARG_V2823_1728])][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2630_1877) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2630_1877, [], KL_ARG_V2822_1727]), [setattr(KL_CTX, 'KL_LOC_Result_1879', [setattr(KL_CTX, 'KL_LOC_Hyp_1880', KL_CTX.KL_LOC_V2615_1855[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2821_1726, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1860, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1870, KL_ARG_V2822_1727]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1862, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_vector, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1870, KL_ARG_V2822_1727]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1880, KL_ARG_V2822_1727])]], KL_ARG_V2822_1727, KL_ARG_V2823_1728])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2630_1877, KL_ARG_V2822_1727]), KL_CTX.KL_LOC_Result_1879][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2630_1877]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2628_1871, KL_ARG_V2822_1727]), KL_CTX.KL_LOC_Result_1876][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2628_1871]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2627_1869) else ([setattr(KL_CTX, 'KL_LOC_A_1881', tco_apply(shen_newpv, [KL_ARG_V2822_1727])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2627_1869, [KL_CTX.KL_LOC_A_1881, []], KL_ARG_V2822_1727]), [setattr(KL_CTX, 'KL_LOC_Result_1882', [setattr(KL_CTX, 'KL_LOC_V2631_1883', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2624_1866[1], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1884', KL_CTX.KL_LOC_V2615_1855[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2821_1726, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1860, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1881, KL_ARG_V2822_1727]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1862, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_vector, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1881, KL_ARG_V2822_1727]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1884, KL_ARG_V2822_1727])]], KL_ARG_V2822_1727, KL_ARG_V2823_1728])][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2631_1883) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2631_1883, [], KL_ARG_V2822_1727]), [setattr(KL_CTX, 'KL_LOC_Result_1885', [setattr(KL_CTX, 'KL_LOC_Hyp_1886', KL_CTX.KL_LOC_V2615_1855[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2821_1726, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1860, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1881, KL_ARG_V2822_1727]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1862, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_vector, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1881, KL_ARG_V2822_1727]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1886, KL_ARG_V2822_1727])]], KL_ARG_V2822_1727, KL_ARG_V2823_1728])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2631_1883, KL_ARG_V2822_1727]), KL_CTX.KL_LOC_Result_1885][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2631_1883]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2627_1869, KL_ARG_V2822_1727]), KL_CTX.KL_LOC_Result_1882][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2627_1869]) else False))][(-1)] if shen_eq(symdic.symdic_kl_vector, KL_CTX.KL_LOC_V2626_1868) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2626_1868, symdic.symdic_kl_vector, KL_ARG_V2822_1727]), [setattr(KL_CTX, 'KL_LOC_Result_1887', [setattr(KL_CTX, 'KL_LOC_V2632_1888', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2625_1867[1], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_A_1889', KL_CTX.KL_LOC_V2632_1888[0]), [setattr(KL_CTX, 'KL_LOC_V2633_1890', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2632_1888[1], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_V2634_1891', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2624_1866[1], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1892', KL_CTX.KL_LOC_V2615_1855[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2821_1726, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1860, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1889, KL_ARG_V2822_1727]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1862, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_vector, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1889, KL_ARG_V2822_1727]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1892, KL_ARG_V2822_1727])]], KL_ARG_V2822_1727, KL_ARG_V2823_1728])][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2634_1891) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2634_1891, [], KL_ARG_V2822_1727]), [setattr(KL_CTX, 'KL_LOC_Result_1893', [setattr(KL_CTX, 'KL_LOC_Hyp_1894', KL_CTX.KL_LOC_V2615_1855[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2821_1726, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1860, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1889, KL_ARG_V2822_1727]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1862, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_vector, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1889, KL_ARG_V2822_1727]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1894, KL_ARG_V2822_1727])]], KL_ARG_V2822_1727, KL_ARG_V2823_1728])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2634_1891, KL_ARG_V2822_1727]), KL_CTX.KL_LOC_Result_1893][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2634_1891]) else False))][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2633_1890) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2633_1890, [], KL_ARG_V2822_1727]), [setattr(KL_CTX, 'KL_LOC_Result_1895', [setattr(KL_CTX, 'KL_LOC_V2635_1896', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2624_1866[1], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1897', KL_CTX.KL_LOC_V2615_1855[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2821_1726, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1860, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1889, KL_ARG_V2822_1727]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1862, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_vector, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1889, KL_ARG_V2822_1727]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1897, KL_ARG_V2822_1727])]], KL_ARG_V2822_1727, KL_ARG_V2823_1728])][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2635_1896) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2635_1896, [], KL_ARG_V2822_1727]), [setattr(KL_CTX, 'KL_LOC_Result_1898', [setattr(KL_CTX, 'KL_LOC_Hyp_1899', KL_CTX.KL_LOC_V2615_1855[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2821_1726, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1860, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1889, KL_ARG_V2822_1727]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1862, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_vector, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1889, KL_ARG_V2822_1727]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1899, KL_ARG_V2822_1727])]], KL_ARG_V2822_1727, KL_ARG_V2823_1728])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2635_1896, KL_ARG_V2822_1727]), KL_CTX.KL_LOC_Result_1898][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2635_1896]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2633_1890, KL_ARG_V2822_1727]), KL_CTX.KL_LOC_Result_1895][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2633_1890]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2632_1888) else ([setattr(KL_CTX, 'KL_LOC_A_1900', tco_apply(shen_newpv, [KL_ARG_V2822_1727])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2632_1888, [KL_CTX.KL_LOC_A_1900, []], KL_ARG_V2822_1727]), [setattr(KL_CTX, 'KL_LOC_Result_1901', [setattr(KL_CTX, 'KL_LOC_V2636_1902', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2624_1866[1], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1903', KL_CTX.KL_LOC_V2615_1855[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2821_1726, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1860, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1900, KL_ARG_V2822_1727]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1862, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_vector, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1900, KL_ARG_V2822_1727]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1903, KL_ARG_V2822_1727])]], KL_ARG_V2822_1727, KL_ARG_V2823_1728])][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2636_1902) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2636_1902, [], KL_ARG_V2822_1727]), [setattr(KL_CTX, 'KL_LOC_Result_1904', [setattr(KL_CTX, 'KL_LOC_Hyp_1905', KL_CTX.KL_LOC_V2615_1855[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2821_1726, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1860, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1900, KL_ARG_V2822_1727]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1862, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_vector, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1900, KL_ARG_V2822_1727]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1905, KL_ARG_V2822_1727])]], KL_ARG_V2822_1727, KL_ARG_V2823_1728])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2636_1902, KL_ARG_V2822_1727]), KL_CTX.KL_LOC_Result_1904][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2636_1902]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2632_1888, KL_ARG_V2822_1727]), KL_CTX.KL_LOC_Result_1901][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2632_1888]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2626_1868, KL_ARG_V2822_1727]), KL_CTX.KL_LOC_Result_1887][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2626_1868]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2625_1867) else ([setattr(KL_CTX, 'KL_LOC_A_1906', tco_apply(shen_newpv, [KL_ARG_V2822_1727])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2625_1867, [symdic.symdic_kl_vector, [KL_CTX.KL_LOC_A_1906, []]], KL_ARG_V2822_1727]), [setattr(KL_CTX, 'KL_LOC_Result_1907', [setattr(KL_CTX, 'KL_LOC_V2637_1908', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2624_1866[1], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1909', KL_CTX.KL_LOC_V2615_1855[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2821_1726, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1860, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1906, KL_ARG_V2822_1727]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1862, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_vector, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1906, KL_ARG_V2822_1727]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1909, KL_ARG_V2822_1727])]], KL_ARG_V2822_1727, KL_ARG_V2823_1728])][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2637_1908) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2637_1908, [], KL_ARG_V2822_1727]), [setattr(KL_CTX, 'KL_LOC_Result_1910', [setattr(KL_CTX, 'KL_LOC_Hyp_1911', KL_CTX.KL_LOC_V2615_1855[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2821_1726, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1860, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1906, KL_ARG_V2822_1727]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1862, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_vector, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1906, KL_ARG_V2822_1727]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1911, KL_ARG_V2822_1727])]], KL_ARG_V2822_1727, KL_ARG_V2823_1728])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2637_1908, KL_ARG_V2822_1727]), KL_CTX.KL_LOC_Result_1910][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2637_1908]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2625_1867, KL_ARG_V2822_1727]), KL_CTX.KL_LOC_Result_1907][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2625_1867]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2624_1866) else False)][(-1)] if shen_eq(symdic.symdic_kl_x58, KL_CTX.KL_LOC_V2623_1865) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2622_1864) else False)][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2621_1863) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2620_1861) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2619_1859) else False)][(-1)] if shen_eq(symdic.symdic_kl_x64v, KL_CTX.KL_LOC_V2618_1858) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2617_1857) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2616_1856) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2615_1855) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1912', [setattr(KL_CTX, 'KL_LOC_V2638_1913', tco_apply(shen_lazyderef, [KL_ARG_V2820_1725, KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_V2639_1914', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2638_1913[0], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_V2640_1915', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2639_1914[0], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_V2641_1916', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2640_1915[0], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_V2642_1917', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2640_1915[1], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_X_1918', KL_CTX.KL_LOC_V2642_1917[0]), [setattr(KL_CTX, 'KL_LOC_V2643_1919', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2642_1917[1], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_Y_1920', KL_CTX.KL_LOC_V2643_1919[0]), [setattr(KL_CTX, 'KL_LOC_V2644_1921', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2643_1919[1], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_V2645_1922', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2639_1914[1], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_V2646_1923', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2645_1922[0], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_V2647_1924', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2645_1922[1], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_V2648_1925', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2647_1924[0], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_V2649_1926', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2647_1924[1], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1927', KL_CTX.KL_LOC_V2638_1913[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2821_1726, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1918, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [symdic.symdic_kl_string, []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1920, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [symdic.symdic_kl_string, []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1927, KL_ARG_V2822_1727])]], KL_ARG_V2822_1727, KL_ARG_V2823_1728])][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2649_1926) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2649_1926, [], KL_ARG_V2822_1727]), [setattr(KL_CTX, 'KL_LOC_Result_1928', [setattr(KL_CTX, 'KL_LOC_Hyp_1929', KL_CTX.KL_LOC_V2638_1913[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2821_1726, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1918, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [symdic.symdic_kl_string, []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1920, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [symdic.symdic_kl_string, []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1929, KL_ARG_V2822_1727])]], KL_ARG_V2822_1727, KL_ARG_V2823_1728])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2649_1926, KL_ARG_V2822_1727]), KL_CTX.KL_LOC_Result_1928][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2649_1926]) else False))][(-1)] if shen_eq(symdic.symdic_kl_string, KL_CTX.KL_LOC_V2648_1925) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2648_1925, symdic.symdic_kl_string, KL_ARG_V2822_1727]), [setattr(KL_CTX, 'KL_LOC_Result_1930', [setattr(KL_CTX, 'KL_LOC_V2650_1931', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2647_1924[1], KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1932', KL_CTX.KL_LOC_V2638_1913[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2821_1726, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1918, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [symdic.symdic_kl_string, []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1920, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [symdic.symdic_kl_string, []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1932, KL_ARG_V2822_1727])]], KL_ARG_V2822_1727, KL_ARG_V2823_1728])][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2650_1931) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2650_1931, [], KL_ARG_V2822_1727]), [setattr(KL_CTX, 'KL_LOC_Result_1933', [setattr(KL_CTX, 'KL_LOC_Hyp_1934', KL_CTX.KL_LOC_V2638_1913[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2821_1726, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1918, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [symdic.symdic_kl_string, []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1920, KL_ARG_V2822_1727]), [symdic.symdic_kl_x58, [symdic.symdic_kl_string, []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1934, KL_ARG_V2822_1727])]], KL_ARG_V2822_1727, KL_ARG_V2823_1728])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2650_1931, KL_ARG_V2822_1727]), KL_CTX.KL_LOC_Result_1933][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2650_1931]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2648_1925, KL_ARG_V2822_1727]), KL_CTX.KL_LOC_Result_1930][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2648_1925]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2647_1924) else False)][(-1)] if shen_eq(symdic.symdic_kl_x58, KL_CTX.KL_LOC_V2646_1923) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2645_1922) else False)][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2644_1921) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2643_1919) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2642_1917) else False)][(-1)] if shen_eq(symdic.symdic_kl_x64s, KL_CTX.KL_LOC_V2641_1916) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2640_1915) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2639_1914) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2638_1913) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_V2651_1935', tco_apply(shen_lazyderef, [KL_ARG_V2820_1725, KL_ARG_V2822_1727])), ([setattr(KL_CTX, 'KL_LOC_X_1936', KL_CTX.KL_LOC_V2651_1935[0]), [setattr(KL_CTX, 'KL_LOC_Hyp_1937', KL_CTX.KL_LOC_V2651_1935[1]), [setattr(KL_CTX, 'KL_LOC_NewHyps_1938', tco_apply(shen_newpv, [KL_ARG_V2822_1727])), [tco_apply(shen_incinfs, []), tail_call(kl_bind, [KL_ARG_V2821_1726, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1936, KL_ARG_V2822_1727]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_NewHyps_1938, KL_ARG_V2822_1727])], KL_ARG_V2822_1727, (lambda : tail_call(shen_tx42x45hyps, [KL_CTX.KL_LOC_Hyp_1937, KL_CTX.KL_LOC_NewHyps_1938, KL_ARG_V2822_1727, KL_ARG_V2823_1728]))])][(-1)]][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2651_1935) else False)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1912, False) else KL_CTX.KL_LOC_Case_1912)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1854, False) else KL_CTX.KL_LOC_Case_1854)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1787, False) else KL_CTX.KL_LOC_Case_1787)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1729, False) else KL_CTX.KL_LOC_Case_1729)][(-1)]
shen_add_fun('shen.t*-hyps', shen_tx42x45hyps)

@tail_recursion
def shen_show(KL_ARG_V2836_1939, KL_ARG_V2837_1940, KL_ARG_V2838_1941, KL_ARG_V2839_1942):
    global symdic
    return ([tco_apply(shen_line, []), [tco_apply(shen_showx45p, [tco_apply(shen_deref, [KL_ARG_V2836_1939, KL_ARG_V2838_1941])]), [tco_apply(kl_nl, [1]), [tco_apply(kl_nl, [1]), [tco_apply(shen_showx45assumptions, [tco_apply(shen_deref, [KL_ARG_V2837_1940, KL_ARG_V2838_1941]), 1]), [shen_pr('\r\n> ', tco_apply(kl_stoutput, [])), [tco_apply(shen_pausex45forx45user, [shen_get(symdic.symdic_kl_x42languagex42)]), tail_call(kl_thaw, [KL_ARG_V2839_1942])][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)] if shen_get(symdic.symdic_shen_x42spyx42) else (tail_call(kl_thaw, [KL_ARG_V2839_1942]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.show', shen_show)

@tail_recursion
def shen_line():

    class KL_Context:
        KL_LOC_Infs_1943 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Infs_1943', tco_apply(kl_inferences, [])), shen_pr(('____________________________________________________________ ' + tco_apply(shen_app, [KL_CTX.KL_LOC_Infs_1943, (' inference' + tco_apply(shen_app, [('' if shen_eq(1, KL_CTX.KL_LOC_Infs_1943) else 's'), ' \r\n?- ', symdic.symdic_shen_a])), symdic.symdic_shen_a])), tco_apply(kl_stoutput, []))][(-1)]
shen_add_fun('shen.line', shen_line)

@tail_recursion
def shen_showx45p(KL_ARG_V2840_1944):
    global symdic
    return (shen_pr(tco_apply(shen_app, [KL_ARG_V2840_1944[0], (' : ' + tco_apply(shen_app, [KL_ARG_V2840_1944[1][1][0], '', symdic.symdic_shen_r])), symdic.symdic_shen_r]), tco_apply(kl_stoutput, [])) if (shen_consp(KL_ARG_V2840_1944) and (shen_consp(KL_ARG_V2840_1944[1]) and (shen_eq(symdic.symdic_kl_x58, KL_ARG_V2840_1944[1][0]) and (shen_consp(KL_ARG_V2840_1944[1][1]) and shen_eq([], KL_ARG_V2840_1944[1][1][1]))))) else (shen_pr(tco_apply(shen_app, [KL_ARG_V2840_1944, '', symdic.symdic_shen_r]), tco_apply(kl_stoutput, [])) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.show-p', shen_showx45p)

@tail_recursion
def shen_showx45assumptions(KL_ARG_V2843_1945, KL_ARG_V2844_1946):
    global symdic
    return (symdic.symdic_shen_skip if shen_eq([], KL_ARG_V2843_1945) else ([shen_pr(tco_apply(shen_app, [KL_ARG_V2844_1946, '. ', symdic.symdic_shen_a]), tco_apply(kl_stoutput, [])), [tco_apply(shen_showx45p, [KL_ARG_V2843_1945[0]]), [tco_apply(kl_nl, [1]), tail_call(shen_showx45assumptions, [KL_ARG_V2843_1945[1], (KL_ARG_V2844_1946 + 1)])][(-1)]][(-1)]][(-1)] if shen_consp(KL_ARG_V2843_1945) else (tail_call(shen_sysx45error, [symdic.symdic_shen_showx45assumptions]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.show-assumptions', shen_showx45assumptions)

@tail_recursion
def shen_pausex45forx45user(KL_ARG_V2849_1947):

    class KL_Context:
        KL_LOC_I_1948 = None
        KL_LOC_I_1949 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_I_1948', tco_apply(FORMAT, [[], '~C', tco_apply(READx45CHAR, [])])), (shen_simple_error('input aborted\r\n') if shen_eq(KL_CTX.KL_LOC_I_1948, 'a') else tail_call(kl_nl, [1]))][(-1)] if shen_eq('Common Lisp', KL_ARG_V2849_1947) else ([setattr(KL_CTX, 'KL_LOC_I_1949', tco_apply(shen_readx45char, [])), (shen_simple_error('input aborted\r\n') if shen_eq(KL_CTX.KL_LOC_I_1949, 'a') else tail_call(kl_nl, [1]))][(-1)] if True else shen_simple_error('condition failure')))
shen_add_fun('shen.pause-for-user', shen_pausex45forx45user)

@tail_recursion
def shen_readx45char():
    global symdic
    return tail_call(shen_readx45charx45h, [shen_read_byte(tco_apply(kl_stinput, [])), 0])
shen_add_fun('shen.read-char', shen_readx45char)

@tail_recursion
def shen_readx45charx45h(KL_ARG_V2852_1950, KL_ARG_V2853_1951):
    global symdic
    return (tail_call(shen_readx45charx45h, [shen_read_byte(tco_apply(kl_stinput, [])), 1]) if (shen_eq((-1), KL_ARG_V2852_1950) and shen_eq(0, KL_ARG_V2853_1951)) else (tail_call(shen_readx45charx45h, [shen_read_byte(tco_apply(kl_stinput, [])), 0]) if shen_eq(0, KL_ARG_V2853_1951) else (tail_call(shen_readx45charx45h, [shen_read_byte(tco_apply(kl_stinput, [])), 1]) if (shen_eq((-1), KL_ARG_V2852_1950) and shen_eq(1, KL_ARG_V2853_1951)) else (chr(KL_ARG_V2852_1950) if shen_eq(1, KL_ARG_V2853_1951) else (tail_call(shen_sysx45error, [symdic.symdic_shen_readx45charx45h]) if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.read-char-h', shen_readx45charx45h)

@tail_recursion
def shen_typedfx63(KL_ARG_V2854_1952):
    global symdic
    return tail_call(kl_elementx63, [KL_ARG_V2854_1952, shen_get(symdic.symdic_shen_x42signedfuncsx42)])
shen_add_fun('shen.typedf?', shen_typedfx63)

@tail_recursion
def shen_sigf(KL_ARG_V2855_1953):
    global symdic
    return tail_call(kl_concat, [symdic.symdic_shen_typex45signaturex45ofx45, KL_ARG_V2855_1953])
shen_add_fun('shen.sigf', shen_sigf)

@tail_recursion
def shen_placeholder():
    global symdic
    return tail_call(kl_gensym, [symdic.symdic_kl_x38x38])
shen_add_fun('shen.placeholder', shen_placeholder)

@tail_recursion
def shen_base(KL_ARG_V2856_1954, KL_ARG_V2857_1955, KL_ARG_V2858_1956, KL_ARG_V2859_1957):

    class KL_Context:
        KL_LOC_Case_1958 = None
        KL_LOC_V2554_1959 = None
        KL_LOC_Result_1960 = None
        KL_LOC_Case_1961 = None
        KL_LOC_V2555_1962 = None
        KL_LOC_Result_1963 = None
        KL_LOC_Case_1964 = None
        KL_LOC_V2556_1965 = None
        KL_LOC_Result_1966 = None
        KL_LOC_Case_1967 = None
        KL_LOC_V2557_1968 = None
        KL_LOC_Result_1969 = None
        KL_LOC_V2558_1970 = None
        KL_LOC_V2559_1971 = None
        KL_LOC_V2560_1972 = None
        KL_LOC_V2561_1973 = None
        KL_LOC_A_1974 = None
        KL_LOC_V2562_1975 = None
        KL_LOC_Result_1976 = None
        KL_LOC_A_1977 = None
        KL_LOC_Result_1978 = None
        KL_LOC_Result_1979 = None
        KL_LOC_V2563_1980 = None
        KL_LOC_A_1981 = None
        KL_LOC_V2564_1982 = None
        KL_LOC_Result_1983 = None
        KL_LOC_A_1984 = None
        KL_LOC_Result_1985 = None
        KL_LOC_A_1986 = None
        KL_LOC_Result_1987 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Case_1958', [setattr(KL_CTX, 'KL_LOC_V2554_1959', tco_apply(shen_lazyderef, [KL_ARG_V2857_1955, KL_ARG_V2858_1956])), ([tco_apply(shen_incinfs, []), tco_apply(kl_fwhen, [isinstance(tco_apply(shen_lazyderef, [KL_ARG_V2856_1954, KL_ARG_V2858_1956]), numbers.Number), KL_ARG_V2858_1956, KL_ARG_V2859_1957])][(-1)] if shen_eq(symdic.symdic_kl_number, KL_CTX.KL_LOC_V2554_1959) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2554_1959, symdic.symdic_kl_number, KL_ARG_V2858_1956]), [setattr(KL_CTX, 'KL_LOC_Result_1960', [tco_apply(shen_incinfs, []), tco_apply(kl_fwhen, [isinstance(tco_apply(shen_lazyderef, [KL_ARG_V2856_1954, KL_ARG_V2858_1956]), numbers.Number), KL_ARG_V2858_1956, KL_ARG_V2859_1957])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2554_1959, KL_ARG_V2858_1956]), KL_CTX.KL_LOC_Result_1960][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2554_1959]) else False))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1961', [setattr(KL_CTX, 'KL_LOC_V2555_1962', tco_apply(shen_lazyderef, [KL_ARG_V2857_1955, KL_ARG_V2858_1956])), ([tco_apply(shen_incinfs, []), tco_apply(kl_fwhen, [tco_apply(kl_booleanx63, [tco_apply(shen_lazyderef, [KL_ARG_V2856_1954, KL_ARG_V2858_1956])]), KL_ARG_V2858_1956, KL_ARG_V2859_1957])][(-1)] if shen_eq(symdic.symdic_kl_boolean, KL_CTX.KL_LOC_V2555_1962) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2555_1962, symdic.symdic_kl_boolean, KL_ARG_V2858_1956]), [setattr(KL_CTX, 'KL_LOC_Result_1963', [tco_apply(shen_incinfs, []), tco_apply(kl_fwhen, [tco_apply(kl_booleanx63, [tco_apply(shen_lazyderef, [KL_ARG_V2856_1954, KL_ARG_V2858_1956])]), KL_ARG_V2858_1956, KL_ARG_V2859_1957])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2555_1962, KL_ARG_V2858_1956]), KL_CTX.KL_LOC_Result_1963][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2555_1962]) else False))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1964', [setattr(KL_CTX, 'KL_LOC_V2556_1965', tco_apply(shen_lazyderef, [KL_ARG_V2857_1955, KL_ARG_V2858_1956])), ([tco_apply(shen_incinfs, []), tco_apply(kl_fwhen, [isinstance(tco_apply(shen_lazyderef, [KL_ARG_V2856_1954, KL_ARG_V2858_1956]), str), KL_ARG_V2858_1956, KL_ARG_V2859_1957])][(-1)] if shen_eq(symdic.symdic_kl_string, KL_CTX.KL_LOC_V2556_1965) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2556_1965, symdic.symdic_kl_string, KL_ARG_V2858_1956]), [setattr(KL_CTX, 'KL_LOC_Result_1966', [tco_apply(shen_incinfs, []), tco_apply(kl_fwhen, [isinstance(tco_apply(shen_lazyderef, [KL_ARG_V2856_1954, KL_ARG_V2858_1956]), str), KL_ARG_V2858_1956, KL_ARG_V2859_1957])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2556_1965, KL_ARG_V2858_1956]), KL_CTX.KL_LOC_Result_1966][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2556_1965]) else False))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1967', [setattr(KL_CTX, 'KL_LOC_V2557_1968', tco_apply(shen_lazyderef, [KL_ARG_V2857_1955, KL_ARG_V2858_1956])), ([tco_apply(shen_incinfs, []), tco_apply(kl_fwhen, [tco_apply(kl_symbolx63, [tco_apply(shen_lazyderef, [KL_ARG_V2856_1954, KL_ARG_V2858_1956])]), KL_ARG_V2858_1956, (lambda : tail_call(kl_fwhen, [(not tco_apply(shen_uex63, [tco_apply(shen_lazyderef, [KL_ARG_V2856_1954, KL_ARG_V2858_1956])])), KL_ARG_V2858_1956, KL_ARG_V2859_1957]))])][(-1)] if shen_eq(symdic.symdic_kl_symbol, KL_CTX.KL_LOC_V2557_1968) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2557_1968, symdic.symdic_kl_symbol, KL_ARG_V2858_1956]), [setattr(KL_CTX, 'KL_LOC_Result_1969', [tco_apply(shen_incinfs, []), tco_apply(kl_fwhen, [tco_apply(kl_symbolx63, [tco_apply(shen_lazyderef, [KL_ARG_V2856_1954, KL_ARG_V2858_1956])]), KL_ARG_V2858_1956, (lambda : tail_call(kl_fwhen, [(not tco_apply(shen_uex63, [tco_apply(shen_lazyderef, [KL_ARG_V2856_1954, KL_ARG_V2858_1956])])), KL_ARG_V2858_1956, KL_ARG_V2859_1957]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2557_1968, KL_ARG_V2858_1956]), KL_CTX.KL_LOC_Result_1969][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2557_1968]) else False))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_V2558_1970', tco_apply(shen_lazyderef, [KL_ARG_V2856_1954, KL_ARG_V2858_1956])), ([setattr(KL_CTX, 'KL_LOC_V2559_1971', tco_apply(shen_lazyderef, [KL_ARG_V2857_1955, KL_ARG_V2858_1956])), ([setattr(KL_CTX, 'KL_LOC_V2560_1972', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2559_1971[0], KL_ARG_V2858_1956])), ([setattr(KL_CTX, 'KL_LOC_V2561_1973', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2559_1971[1], KL_ARG_V2858_1956])), ([setattr(KL_CTX, 'KL_LOC_A_1974', KL_CTX.KL_LOC_V2561_1973[0]), [setattr(KL_CTX, 'KL_LOC_V2562_1975', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2561_1973[1], KL_ARG_V2858_1956])), ([tco_apply(shen_incinfs, []), tail_call(kl_thaw, [KL_ARG_V2859_1957])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2562_1975) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2562_1975, [], KL_ARG_V2858_1956]), [setattr(KL_CTX, 'KL_LOC_Result_1976', [tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V2859_1957])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2562_1975, KL_ARG_V2858_1956]), KL_CTX.KL_LOC_Result_1976][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2562_1975]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2561_1973) else ([setattr(KL_CTX, 'KL_LOC_A_1977', tco_apply(shen_newpv, [KL_ARG_V2858_1956])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2561_1973, [KL_CTX.KL_LOC_A_1977, []], KL_ARG_V2858_1956]), [setattr(KL_CTX, 'KL_LOC_Result_1978', [tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V2859_1957])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2561_1973, KL_ARG_V2858_1956]), KL_CTX.KL_LOC_Result_1978][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2561_1973]) else False))][(-1)] if shen_eq(symdic.symdic_kl_list, KL_CTX.KL_LOC_V2560_1972) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2560_1972, symdic.symdic_kl_list, KL_ARG_V2858_1956]), [setattr(KL_CTX, 'KL_LOC_Result_1979', [setattr(KL_CTX, 'KL_LOC_V2563_1980', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2559_1971[1], KL_ARG_V2858_1956])), ([setattr(KL_CTX, 'KL_LOC_A_1981', KL_CTX.KL_LOC_V2563_1980[0]), [setattr(KL_CTX, 'KL_LOC_V2564_1982', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2563_1980[1], KL_ARG_V2858_1956])), ([tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V2859_1957])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2564_1982) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2564_1982, [], KL_ARG_V2858_1956]), [setattr(KL_CTX, 'KL_LOC_Result_1983', [tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V2859_1957])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2564_1982, KL_ARG_V2858_1956]), KL_CTX.KL_LOC_Result_1983][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2564_1982]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2563_1980) else ([setattr(KL_CTX, 'KL_LOC_A_1984', tco_apply(shen_newpv, [KL_ARG_V2858_1956])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2563_1980, [KL_CTX.KL_LOC_A_1984, []], KL_ARG_V2858_1956]), [setattr(KL_CTX, 'KL_LOC_Result_1985', [tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V2859_1957])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2563_1980, KL_ARG_V2858_1956]), KL_CTX.KL_LOC_Result_1985][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2563_1980]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2560_1972, KL_ARG_V2858_1956]), KL_CTX.KL_LOC_Result_1979][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2560_1972]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2559_1971) else ([setattr(KL_CTX, 'KL_LOC_A_1986', tco_apply(shen_newpv, [KL_ARG_V2858_1956])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2559_1971, [symdic.symdic_kl_list, [KL_CTX.KL_LOC_A_1986, []]], KL_ARG_V2858_1956]), [setattr(KL_CTX, 'KL_LOC_Result_1987', [tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V2859_1957])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2559_1971, KL_ARG_V2858_1956]), KL_CTX.KL_LOC_Result_1987][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2559_1971]) else False))][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2558_1970) else False)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1967, False) else KL_CTX.KL_LOC_Case_1967)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1964, False) else KL_CTX.KL_LOC_Case_1964)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1961, False) else KL_CTX.KL_LOC_Case_1961)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1958, False) else KL_CTX.KL_LOC_Case_1958)][(-1)]
shen_add_fun('shen.base', shen_base)

@tail_recursion
def shen_by_hypothesis(KL_ARG_V2860_1988, KL_ARG_V2861_1989, KL_ARG_V2862_1990, KL_ARG_V2863_1991, KL_ARG_V2864_1992):

    class KL_Context:
        KL_LOC_Case_1993 = None
        KL_LOC_V2545_1994 = None
        KL_LOC_V2546_1995 = None
        KL_LOC_Y_1996 = None
        KL_LOC_V2547_1997 = None
        KL_LOC_V2548_1998 = None
        KL_LOC_V2549_1999 = None
        KL_LOC_B_2000 = None
        KL_LOC_V2550_2001 = None
        KL_LOC_V2551_2002 = None
        KL_LOC_Hyp_2003 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Case_1993', [setattr(KL_CTX, 'KL_LOC_V2545_1994', tco_apply(shen_lazyderef, [KL_ARG_V2862_1990, KL_ARG_V2863_1991])), ([setattr(KL_CTX, 'KL_LOC_V2546_1995', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2545_1994[0], KL_ARG_V2863_1991])), ([setattr(KL_CTX, 'KL_LOC_Y_1996', KL_CTX.KL_LOC_V2546_1995[0]), [setattr(KL_CTX, 'KL_LOC_V2547_1997', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2546_1995[1], KL_ARG_V2863_1991])), ([setattr(KL_CTX, 'KL_LOC_V2548_1998', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2547_1997[0], KL_ARG_V2863_1991])), ([setattr(KL_CTX, 'KL_LOC_V2549_1999', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2547_1997[1], KL_ARG_V2863_1991])), ([setattr(KL_CTX, 'KL_LOC_B_2000', KL_CTX.KL_LOC_V2549_1999[0]), [setattr(KL_CTX, 'KL_LOC_V2550_2001', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2549_1999[1], KL_ARG_V2863_1991])), ([tco_apply(shen_incinfs, []), tco_apply(kl_identical, [KL_ARG_V2860_1988, KL_CTX.KL_LOC_Y_1996, KL_ARG_V2863_1991, (lambda : tail_call(kl_unifyx33, [KL_ARG_V2861_1989, KL_CTX.KL_LOC_B_2000, KL_ARG_V2863_1991, KL_ARG_V2864_1992]))])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2550_2001) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2549_1999) else False)][(-1)] if shen_eq(symdic.symdic_kl_x58, KL_CTX.KL_LOC_V2548_1998) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2547_1997) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2546_1995) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2545_1994) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_V2551_2002', tco_apply(shen_lazyderef, [KL_ARG_V2862_1990, KL_ARG_V2863_1991])), ([setattr(KL_CTX, 'KL_LOC_Hyp_2003', KL_CTX.KL_LOC_V2551_2002[1]), [tco_apply(shen_incinfs, []), tail_call(shen_by_hypothesis, [KL_ARG_V2860_1988, KL_ARG_V2861_1989, KL_CTX.KL_LOC_Hyp_2003, KL_ARG_V2863_1991, KL_ARG_V2864_1992])][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2551_2002) else False)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1993, False) else KL_CTX.KL_LOC_Case_1993)][(-1)]
shen_add_fun('shen.by_hypothesis', shen_by_hypothesis)

@tail_recursion
def shen_tx42x45def(KL_ARG_V2865_2004, KL_ARG_V2866_2005, KL_ARG_V2867_2006, KL_ARG_V2868_2007, KL_ARG_V2869_2008):

    class KL_Context:
        KL_LOC_V2539_2009 = None
        KL_LOC_V2540_2010 = None
        KL_LOC_V2541_2011 = None
        KL_LOC_F_2012 = None
        KL_LOC_X_2013 = None
        KL_LOC_E_2014 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_V2539_2009', tco_apply(shen_lazyderef, [KL_ARG_V2865_2004, KL_ARG_V2868_2007])), ([setattr(KL_CTX, 'KL_LOC_V2540_2010', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2539_2009[0], KL_ARG_V2868_2007])), ([setattr(KL_CTX, 'KL_LOC_V2541_2011', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2539_2009[1], KL_ARG_V2868_2007])), ([setattr(KL_CTX, 'KL_LOC_F_2012', KL_CTX.KL_LOC_V2541_2011[0]), [setattr(KL_CTX, 'KL_LOC_X_2013', KL_CTX.KL_LOC_V2541_2011[1]), [setattr(KL_CTX, 'KL_LOC_E_2014', tco_apply(shen_newpv, [KL_ARG_V2868_2007])), [tco_apply(shen_incinfs, []), tail_call(shen_tx42x45defh, [tco_apply(kl_compile, [symdic.symdic_shen_x60sigx43rulesx62, KL_CTX.KL_LOC_X_2013, (lambda KL_ARG_E_2015: (shen_simple_error(('parse error here: ' + tco_apply(shen_app, [KL_ARG_E_2015, '\r\n', symdic.symdic_shen_s]))) if shen_consp(KL_ARG_E_2015) else shen_simple_error('parse error\r\n')))]), KL_CTX.KL_LOC_F_2012, KL_ARG_V2866_2005, KL_ARG_V2867_2006, KL_ARG_V2868_2007, KL_ARG_V2869_2008])][(-1)]][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2541_2011) else False)][(-1)] if shen_eq(symdic.symdic_kl_define, KL_CTX.KL_LOC_V2540_2010) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2539_2009) else False)][(-1)]
shen_add_fun('shen.t*-def', shen_tx42x45def)

@tail_recursion
def shen_tx42x45defh(KL_ARG_V2870_2016, KL_ARG_V2871_2017, KL_ARG_V2872_2018, KL_ARG_V2873_2019, KL_ARG_V2874_2020, KL_ARG_V2875_2021):

    class KL_Context:
        KL_LOC_V2535_2022 = None
        KL_LOC_Sig_2023 = None
        KL_LOC_Rules_2024 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_V2535_2022', tco_apply(shen_lazyderef, [KL_ARG_V2870_2016, KL_ARG_V2874_2020])), ([setattr(KL_CTX, 'KL_LOC_Sig_2023', KL_CTX.KL_LOC_V2535_2022[0]), [setattr(KL_CTX, 'KL_LOC_Rules_2024', KL_CTX.KL_LOC_V2535_2022[1]), [tco_apply(shen_incinfs, []), tail_call(shen_tx42x45defhh, [KL_CTX.KL_LOC_Sig_2023, tco_apply(shen_ue, [KL_CTX.KL_LOC_Sig_2023]), KL_ARG_V2871_2017, KL_ARG_V2872_2018, KL_ARG_V2873_2019, KL_CTX.KL_LOC_Rules_2024, KL_ARG_V2874_2020, KL_ARG_V2875_2021])][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2535_2022) else False)][(-1)]
shen_add_fun('shen.t*-defh', shen_tx42x45defh)

@tail_recursion
def shen_tx42x45defhh(KL_ARG_V2876_2025, KL_ARG_V2877_2026, KL_ARG_V2878_2027, KL_ARG_V2879_2028, KL_ARG_V2880_2029, KL_ARG_V2881_2030, KL_ARG_V2882_2031, KL_ARG_V2883_2032):
    global symdic
    return [tco_apply(shen_incinfs, []), tail_call(shen_tx42x45rules, [KL_ARG_V2881_2030, KL_ARG_V2877_2026, 1, KL_ARG_V2878_2027, [[KL_ARG_V2878_2027, [symdic.symdic_kl_x58, [KL_ARG_V2877_2026, []]]], KL_ARG_V2880_2029], KL_ARG_V2882_2031, (lambda : tail_call(shen_memo, [KL_ARG_V2878_2027, KL_ARG_V2876_2025, KL_ARG_V2879_2028, KL_ARG_V2882_2031, KL_ARG_V2883_2032]))])][(-1)]
shen_add_fun('shen.t*-defhh', shen_tx42x45defhh)

@tail_recursion
def shen_memo(KL_ARG_V2884_2033, KL_ARG_V2885_2034, KL_ARG_V2886_2035, KL_ARG_V2887_2036, KL_ARG_V2888_2037):

    class KL_Context:
        KL_LOC_Jnk_2038 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Jnk_2038', tco_apply(shen_newpv, [KL_ARG_V2887_2036])), [tco_apply(shen_incinfs, []), tail_call(kl_unifyx33, [KL_ARG_V2886_2035, KL_ARG_V2885_2034, KL_ARG_V2887_2036, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Jnk_2038, apply(kl_declare, [tco_apply(shen_lazyderef, [KL_ARG_V2884_2033, KL_ARG_V2887_2036]), tco_apply(shen_lazyderef, [KL_ARG_V2886_2035, KL_ARG_V2887_2036])]), KL_ARG_V2887_2036, KL_ARG_V2888_2037]))])][(-1)]][(-1)]
shen_add_fun('shen.memo', shen_memo)

@tail_recursion
def shen_x60sigx43rulesx62(KL_ARG_V2893_2039):

    class KL_Context:
        KL_LOC_Result_2040 = None
        KL_LOC_Parse_shen_x60signaturex62_2041 = None
        KL_LOC_Parse_shen_x60rulesx62_2042 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_2040', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60signaturex62_2041', tco_apply(shen_x60signaturex62, [KL_ARG_V2893_2039])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60rulesx62_2042', tco_apply(shen_x60rulesx62, [KL_CTX.KL_LOC_Parse_shen_x60signaturex62_2041])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60rulesx62_2042[0], [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60signaturex62_2041]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60rulesx62_2042])]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60rulesx62_2042)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60signaturex62_2041)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_2040, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_2040)][(-1)]
shen_add_fun('shen.<sig+rules>', shen_x60sigx43rulesx62)

@tail_recursion
def shen_ue(KL_ARG_V2894_2043):
    global symdic
    return (tail_call(kl_map, [symdic.symdic_shen_ue, KL_ARG_V2894_2043]) if shen_consp(KL_ARG_V2894_2043) else (tail_call(kl_concat, [symdic.symdic_kl_x38x38, KL_ARG_V2894_2043]) if tco_apply(kl_variablex63, [KL_ARG_V2894_2043]) else (KL_ARG_V2894_2043 if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.ue', shen_ue)

@tail_recursion
def shen_ues(KL_ARG_V2899_2044):
    global symdic
    return ([KL_ARG_V2899_2044, []] if tco_apply(shen_uex63, [KL_ARG_V2899_2044]) else (tail_call(kl_union, [tco_apply(shen_ues, [KL_ARG_V2899_2044[0]]), tco_apply(shen_ues, [KL_ARG_V2899_2044[1]])]) if shen_consp(KL_ARG_V2899_2044) else ([] if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.ues', shen_ues)

@tail_recursion
def shen_uex63(KL_ARG_V2900_2045):
    global symdic
    return (tco_apply(kl_symbolx63, [KL_ARG_V2900_2045]) and tco_apply(shen_uex45hx63, [str(KL_ARG_V2900_2045)]))
shen_add_fun('shen.ue?', shen_uex63)

@tail_recursion
def shen_uex45hx63(KL_ARG_V2907_2046):
    global symdic
    return (True if (tco_apply(shen_x43stringx63, [KL_ARG_V2907_2046]) and (shen_eq('&', KL_ARG_V2907_2046[0]) and (tco_apply(shen_x43stringx63, [KL_ARG_V2907_2046[1:]]) and shen_eq('&', KL_ARG_V2907_2046[1:][0])))) else (False if True else shen_simple_error('condition failure')))
shen_add_fun('shen.ue-h?', shen_uex45hx63)

@tail_recursion
def shen_tx42x45rules(KL_ARG_V2908_2047, KL_ARG_V2909_2048, KL_ARG_V2910_2049, KL_ARG_V2911_2050, KL_ARG_V2912_2051, KL_ARG_V2913_2052, KL_ARG_V2914_2053):

    class KL_Context:
        KL_LOC_Throwcontrol_2054 = None
        KL_LOC_Case_2055 = None
        KL_LOC_V2510_2056 = None
        KL_LOC_Case_2057 = None
        KL_LOC_V2511_2058 = None
        KL_LOC_V2512_2059 = None
        KL_LOC_V2513_2060 = None
        KL_LOC_V2514_2061 = None
        KL_LOC_Action_2062 = None
        KL_LOC_V2515_2063 = None
        KL_LOC_Rules_2064 = None
        KL_LOC_V2516_2065 = None
        KL_LOC_V2517_2066 = None
        KL_LOC_V2518_2067 = None
        KL_LOC_A_2068 = None
        KL_LOC_V2519_2069 = None
        KL_LOC_Case_2070 = None
        KL_LOC_V2520_2071 = None
        KL_LOC_Rule_2072 = None
        KL_LOC_Rules_2073 = None
        KL_LOC_Err_2074 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Throwcontrol_2054', tco_apply(shen_catchpoint, [])), tail_call(shen_cutpoint, [KL_CTX.KL_LOC_Throwcontrol_2054, [setattr(KL_CTX, 'KL_LOC_Case_2055', [setattr(KL_CTX, 'KL_LOC_V2510_2056', tco_apply(shen_lazyderef, [KL_ARG_V2908_2047, KL_ARG_V2913_2052])), ([tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V2914_2053])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2510_2056) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_2057', [setattr(KL_CTX, 'KL_LOC_V2511_2058', tco_apply(shen_lazyderef, [KL_ARG_V2908_2047, KL_ARG_V2913_2052])), ([setattr(KL_CTX, 'KL_LOC_V2512_2059', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2511_2058[0], KL_ARG_V2913_2052])), ([setattr(KL_CTX, 'KL_LOC_V2513_2060', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2512_2059[0], KL_ARG_V2913_2052])), ([setattr(KL_CTX, 'KL_LOC_V2514_2061', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2512_2059[1], KL_ARG_V2913_2052])), ([setattr(KL_CTX, 'KL_LOC_Action_2062', KL_CTX.KL_LOC_V2514_2061[0]), [setattr(KL_CTX, 'KL_LOC_V2515_2063', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2514_2061[1], KL_ARG_V2913_2052])), ([setattr(KL_CTX, 'KL_LOC_Rules_2064', KL_CTX.KL_LOC_V2511_2058[1]), [setattr(KL_CTX, 'KL_LOC_V2516_2065', tco_apply(shen_lazyderef, [KL_ARG_V2909_2048, KL_ARG_V2913_2052])), ([setattr(KL_CTX, 'KL_LOC_V2517_2066', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2516_2065[0], KL_ARG_V2913_2052])), ([setattr(KL_CTX, 'KL_LOC_V2518_2067', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2516_2065[1], KL_ARG_V2913_2052])), ([setattr(KL_CTX, 'KL_LOC_A_2068', KL_CTX.KL_LOC_V2518_2067[0]), [setattr(KL_CTX, 'KL_LOC_V2519_2069', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2518_2067[1], KL_ARG_V2913_2052])), ([tco_apply(shen_incinfs, []), tco_apply(shen_tx42x45rule, [[[], [tco_apply(shen_ue, [KL_CTX.KL_LOC_Action_2062]), []]], KL_CTX.KL_LOC_A_2068, KL_ARG_V2912_2051, KL_ARG_V2913_2052, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2054, KL_ARG_V2913_2052, (lambda : tail_call(shen_tx42x45rules, [KL_CTX.KL_LOC_Rules_2064, KL_CTX.KL_LOC_A_2068, (KL_ARG_V2910_2049 + 1), KL_ARG_V2911_2050, KL_ARG_V2912_2051, KL_ARG_V2913_2052, KL_ARG_V2914_2053]))]))])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2519_2069) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2518_2067) else False)][(-1)] if shen_eq(symdic.symdic_kl_x45x45x62, KL_CTX.KL_LOC_V2517_2066) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2516_2065) else False)][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2515_2063) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2514_2061) else False)][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2513_2060) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2512_2059) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2511_2058) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_2070', [setattr(KL_CTX, 'KL_LOC_V2520_2071', tco_apply(shen_lazyderef, [KL_ARG_V2908_2047, KL_ARG_V2913_2052])), ([setattr(KL_CTX, 'KL_LOC_Rule_2072', KL_CTX.KL_LOC_V2520_2071[0]), [setattr(KL_CTX, 'KL_LOC_Rules_2073', KL_CTX.KL_LOC_V2520_2071[1]), [tco_apply(shen_incinfs, []), tco_apply(shen_tx42x45rule, [tco_apply(shen_ue, [KL_CTX.KL_LOC_Rule_2072]), KL_ARG_V2909_2048, KL_ARG_V2912_2051, KL_ARG_V2913_2052, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2054, KL_ARG_V2913_2052, (lambda : tail_call(shen_tx42x45rules, [KL_CTX.KL_LOC_Rules_2073, KL_ARG_V2909_2048, (KL_ARG_V2910_2049 + 1), KL_ARG_V2911_2050, KL_ARG_V2912_2051, KL_ARG_V2913_2052, KL_ARG_V2914_2053]))]))])][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2520_2071) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Err_2074', tco_apply(shen_newpv, [KL_ARG_V2913_2052])), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_CTX.KL_LOC_Err_2074, shen_simple_error(('type error in rule ' + tco_apply(shen_app, [tco_apply(shen_lazyderef, [KL_ARG_V2910_2049, KL_ARG_V2913_2052]), (' of ' + tco_apply(shen_app, [tco_apply(shen_lazyderef, [KL_ARG_V2911_2050, KL_ARG_V2913_2052]), '', symdic.symdic_shen_a])), symdic.symdic_shen_a]))), KL_ARG_V2913_2052, KL_ARG_V2914_2053])][(-1)]][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2070, False) else KL_CTX.KL_LOC_Case_2070)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2057, False) else KL_CTX.KL_LOC_Case_2057)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2055, False) else KL_CTX.KL_LOC_Case_2055)][(-1)]])][(-1)]
shen_add_fun('shen.t*-rules', shen_tx42x45rules)

@tail_recursion
def shen_tx42x45rule(KL_ARG_V2915_2075, KL_ARG_V2916_2076, KL_ARG_V2917_2077, KL_ARG_V2918_2078, KL_ARG_V2919_2079):

    class KL_Context:
        KL_LOC_Throwcontrol_2080 = None
        KL_LOC_Case_2081 = None
        KL_LOC_V2492_2082 = None
        KL_LOC_V2493_2083 = None
        KL_LOC_V2494_2084 = None
        KL_LOC_Action_2085 = None
        KL_LOC_V2495_2086 = None
        KL_LOC_V2496_2087 = None
        KL_LOC_V2497_2088 = None
        KL_LOC_Pattern_2089 = None
        KL_LOC_Patterns_2090 = None
        KL_LOC_V2498_2091 = None
        KL_LOC_Action_2092 = None
        KL_LOC_V2499_2093 = None
        KL_LOC_V2500_2094 = None
        KL_LOC_A_2095 = None
        KL_LOC_V2501_2096 = None
        KL_LOC_V2502_2097 = None
        KL_LOC_V2503_2098 = None
        KL_LOC_B_2099 = None
        KL_LOC_V2504_2100 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Throwcontrol_2080', tco_apply(shen_catchpoint, [])), tail_call(shen_cutpoint, [KL_CTX.KL_LOC_Throwcontrol_2080, [setattr(KL_CTX, 'KL_LOC_Case_2081', [setattr(KL_CTX, 'KL_LOC_V2492_2082', tco_apply(shen_lazyderef, [KL_ARG_V2915_2075, KL_ARG_V2918_2078])), ([setattr(KL_CTX, 'KL_LOC_V2493_2083', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2492_2082[0], KL_ARG_V2918_2078])), ([setattr(KL_CTX, 'KL_LOC_V2494_2084', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2492_2082[1], KL_ARG_V2918_2078])), ([setattr(KL_CTX, 'KL_LOC_Action_2085', KL_CTX.KL_LOC_V2494_2084[0]), [setattr(KL_CTX, 'KL_LOC_V2495_2086', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2494_2084[1], KL_ARG_V2918_2078])), ([tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2080, KL_ARG_V2918_2078, (lambda : tail_call(shen_tx42x45action, [tco_apply(shen_curry, [KL_CTX.KL_LOC_Action_2085]), KL_ARG_V2916_2076, KL_ARG_V2917_2077, KL_ARG_V2918_2078, KL_ARG_V2919_2079]))])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2495_2086) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2494_2084) else False)][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2493_2083) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2492_2082) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_V2496_2087', tco_apply(shen_lazyderef, [KL_ARG_V2915_2075, KL_ARG_V2918_2078])), ([setattr(KL_CTX, 'KL_LOC_V2497_2088', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2496_2087[0], KL_ARG_V2918_2078])), ([setattr(KL_CTX, 'KL_LOC_Pattern_2089', KL_CTX.KL_LOC_V2497_2088[0]), [setattr(KL_CTX, 'KL_LOC_Patterns_2090', KL_CTX.KL_LOC_V2497_2088[1]), [setattr(KL_CTX, 'KL_LOC_V2498_2091', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2496_2087[1], KL_ARG_V2918_2078])), ([setattr(KL_CTX, 'KL_LOC_Action_2092', KL_CTX.KL_LOC_V2498_2091[0]), [setattr(KL_CTX, 'KL_LOC_V2499_2093', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2498_2091[1], KL_ARG_V2918_2078])), ([setattr(KL_CTX, 'KL_LOC_V2500_2094', tco_apply(shen_lazyderef, [KL_ARG_V2916_2076, KL_ARG_V2918_2078])), ([setattr(KL_CTX, 'KL_LOC_A_2095', KL_CTX.KL_LOC_V2500_2094[0]), [setattr(KL_CTX, 'KL_LOC_V2501_2096', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2500_2094[1], KL_ARG_V2918_2078])), ([setattr(KL_CTX, 'KL_LOC_V2502_2097', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2501_2096[0], KL_ARG_V2918_2078])), ([setattr(KL_CTX, 'KL_LOC_V2503_2098', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2501_2096[1], KL_ARG_V2918_2078])), ([setattr(KL_CTX, 'KL_LOC_B_2099', KL_CTX.KL_LOC_V2503_2098[0]), [setattr(KL_CTX, 'KL_LOC_V2504_2100', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2503_2098[1], KL_ARG_V2918_2078])), ([tco_apply(shen_incinfs, []), tco_apply(shen_tx42x45pattern, [KL_CTX.KL_LOC_Pattern_2089, KL_CTX.KL_LOC_A_2095, KL_ARG_V2918_2078, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2080, KL_ARG_V2918_2078, (lambda : tail_call(shen_tx42x45rule, [[KL_CTX.KL_LOC_Patterns_2090, [KL_CTX.KL_LOC_Action_2092, []]], KL_CTX.KL_LOC_B_2099, [[KL_CTX.KL_LOC_Pattern_2089, [symdic.symdic_kl_x58, [KL_CTX.KL_LOC_A_2095, []]]], KL_ARG_V2917_2077], KL_ARG_V2918_2078, KL_ARG_V2919_2079]))]))])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2504_2100) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2503_2098) else False)][(-1)] if shen_eq(symdic.symdic_kl_x45x45x62, KL_CTX.KL_LOC_V2502_2097) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2501_2096) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2500_2094) else False)][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2499_2093) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2498_2091) else False)][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2497_2088) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2496_2087) else False)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2081, False) else KL_CTX.KL_LOC_Case_2081)][(-1)]])][(-1)]
shen_add_fun('shen.t*-rule', shen_tx42x45rule)

@tail_recursion
def shen_tx42x45action(KL_ARG_V2920_2101, KL_ARG_V2921_2102, KL_ARG_V2922_2103, KL_ARG_V2923_2104, KL_ARG_V2924_2105):

    class KL_Context:
        KL_LOC_Throwcontrol_2106 = None
        KL_LOC_Case_2107 = None
        KL_LOC_V2469_2108 = None
        KL_LOC_V2470_2109 = None
        KL_LOC_V2471_2110 = None
        KL_LOC_P_2111 = None
        KL_LOC_V2472_2112 = None
        KL_LOC_Action_2113 = None
        KL_LOC_V2473_2114 = None
        KL_LOC_Case_2115 = None
        KL_LOC_V2474_2116 = None
        KL_LOC_V2475_2117 = None
        KL_LOC_V2476_2118 = None
        KL_LOC_V2477_2119 = None
        KL_LOC_V2478_2120 = None
        KL_LOC_V2479_2121 = None
        KL_LOC_V2480_2122 = None
        KL_LOC_F_2123 = None
        KL_LOC_V2481_2124 = None
        KL_LOC_V2482_2125 = None
        KL_LOC_Action_2126 = None
        KL_LOC_V2483_2127 = None
        KL_LOC_V2484_2128 = None
        KL_LOC_Case_2129 = None
        KL_LOC_V2485_2130 = None
        KL_LOC_V2486_2131 = None
        KL_LOC_V2487_2132 = None
        KL_LOC_Action_2133 = None
        KL_LOC_V2488_2134 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Throwcontrol_2106', tco_apply(shen_catchpoint, [])), tail_call(shen_cutpoint, [KL_CTX.KL_LOC_Throwcontrol_2106, [setattr(KL_CTX, 'KL_LOC_Case_2107', [setattr(KL_CTX, 'KL_LOC_V2469_2108', tco_apply(shen_lazyderef, [KL_ARG_V2920_2101, KL_ARG_V2923_2104])), ([setattr(KL_CTX, 'KL_LOC_V2470_2109', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2469_2108[0], KL_ARG_V2923_2104])), ([setattr(KL_CTX, 'KL_LOC_V2471_2110', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2469_2108[1], KL_ARG_V2923_2104])), ([setattr(KL_CTX, 'KL_LOC_P_2111', KL_CTX.KL_LOC_V2471_2110[0]), [setattr(KL_CTX, 'KL_LOC_V2472_2112', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2471_2110[1], KL_ARG_V2923_2104])), ([setattr(KL_CTX, 'KL_LOC_Action_2113', KL_CTX.KL_LOC_V2472_2112[0]), [setattr(KL_CTX, 'KL_LOC_V2473_2114', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2472_2112[1], KL_ARG_V2923_2104])), ([tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2106, KL_ARG_V2923_2104, (lambda : tail_call(shen_tx42, [[KL_CTX.KL_LOC_P_2111, [symdic.symdic_kl_x58, [symdic.symdic_kl_boolean, []]]], KL_ARG_V2922_2103, KL_ARG_V2923_2104, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2106, KL_ARG_V2923_2104, (lambda : tail_call(shen_tx42x45action, [KL_CTX.KL_LOC_Action_2113, KL_ARG_V2921_2102, [[KL_CTX.KL_LOC_P_2111, [symdic.symdic_kl_x58, [symdic.symdic_kl_verified, []]]], KL_ARG_V2922_2103], KL_ARG_V2923_2104, KL_ARG_V2924_2105]))]))]))])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2473_2114) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2472_2112) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2471_2110) else False)][(-1)] if shen_eq(symdic.symdic_kl_where, KL_CTX.KL_LOC_V2470_2109) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2469_2108) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_2115', [setattr(KL_CTX, 'KL_LOC_V2474_2116', tco_apply(shen_lazyderef, [KL_ARG_V2920_2101, KL_ARG_V2923_2104])), ([setattr(KL_CTX, 'KL_LOC_V2475_2117', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2474_2116[0], KL_ARG_V2923_2104])), ([setattr(KL_CTX, 'KL_LOC_V2476_2118', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2474_2116[1], KL_ARG_V2923_2104])), ([setattr(KL_CTX, 'KL_LOC_V2477_2119', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2476_2118[0], KL_ARG_V2923_2104])), ([setattr(KL_CTX, 'KL_LOC_V2478_2120', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2477_2119[0], KL_ARG_V2923_2104])), ([setattr(KL_CTX, 'KL_LOC_V2479_2121', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2478_2120[0], KL_ARG_V2923_2104])), ([setattr(KL_CTX, 'KL_LOC_V2480_2122', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2478_2120[1], KL_ARG_V2923_2104])), ([setattr(KL_CTX, 'KL_LOC_F_2123', KL_CTX.KL_LOC_V2480_2122[0]), [setattr(KL_CTX, 'KL_LOC_V2481_2124', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2480_2122[1], KL_ARG_V2923_2104])), ([setattr(KL_CTX, 'KL_LOC_V2482_2125', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2477_2119[1], KL_ARG_V2923_2104])), ([setattr(KL_CTX, 'KL_LOC_Action_2126', KL_CTX.KL_LOC_V2482_2125[0]), [setattr(KL_CTX, 'KL_LOC_V2483_2127', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2482_2125[1], KL_ARG_V2923_2104])), ([setattr(KL_CTX, 'KL_LOC_V2484_2128', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2476_2118[1], KL_ARG_V2923_2104])), ([tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2106, KL_ARG_V2923_2104, (lambda : tail_call(shen_tx42x45action, [[symdic.symdic_kl_where, [[symdic.symdic_kl_not, [[KL_CTX.KL_LOC_F_2123, [KL_CTX.KL_LOC_Action_2126, []]], []]], [KL_CTX.KL_LOC_Action_2126, []]]], KL_ARG_V2921_2102, KL_ARG_V2922_2103, KL_ARG_V2923_2104, KL_ARG_V2924_2105]))])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2484_2128) else False)][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2483_2127) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2482_2125) else False)][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2481_2124) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2480_2122) else False)][(-1)] if shen_eq(symdic.symdic_kl_failx45if, KL_CTX.KL_LOC_V2479_2121) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2478_2120) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2477_2119) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2476_2118) else False)][(-1)] if shen_eq(symdic.symdic_shen_choicepointx33, KL_CTX.KL_LOC_V2475_2117) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2474_2116) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_2129', [setattr(KL_CTX, 'KL_LOC_V2485_2130', tco_apply(shen_lazyderef, [KL_ARG_V2920_2101, KL_ARG_V2923_2104])), ([setattr(KL_CTX, 'KL_LOC_V2486_2131', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2485_2130[0], KL_ARG_V2923_2104])), ([setattr(KL_CTX, 'KL_LOC_V2487_2132', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2485_2130[1], KL_ARG_V2923_2104])), ([setattr(KL_CTX, 'KL_LOC_Action_2133', KL_CTX.KL_LOC_V2487_2132[0]), [setattr(KL_CTX, 'KL_LOC_V2488_2134', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2487_2132[1], KL_ARG_V2923_2104])), ([tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2106, KL_ARG_V2923_2104, (lambda : tail_call(shen_tx42x45action, [[symdic.symdic_kl_where, [[symdic.symdic_kl_not, [[[symdic.symdic_kl_x61, [KL_CTX.KL_LOC_Action_2133, []]], [[symdic.symdic_kl_fail, []], []]], []]], [KL_CTX.KL_LOC_Action_2133, []]]], KL_ARG_V2921_2102, KL_ARG_V2922_2103, KL_ARG_V2923_2104, KL_ARG_V2924_2105]))])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2488_2134) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2487_2132) else False)][(-1)] if shen_eq(symdic.symdic_shen_choicepointx33, KL_CTX.KL_LOC_V2486_2131) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2485_2130) else False)][(-1)]), ([tco_apply(shen_incinfs, []), tco_apply(shen_tx42, [[KL_ARG_V2920_2101, [symdic.symdic_kl_x58, [KL_ARG_V2921_2102, []]]], KL_ARG_V2922_2103, KL_ARG_V2923_2104, KL_ARG_V2924_2105])][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2129, False) else KL_CTX.KL_LOC_Case_2129)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2115, False) else KL_CTX.KL_LOC_Case_2115)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2107, False) else KL_CTX.KL_LOC_Case_2107)][(-1)]])][(-1)]
shen_add_fun('shen.t*-action', shen_tx42x45action)

@tail_recursion
def shen_tx42x45pattern(KL_ARG_V2925_2135, KL_ARG_V2926_2136, KL_ARG_V2927_2137, KL_ARG_V2928_2138):

    class KL_Context:
        KL_LOC_Throwcontrol_2139 = None
        KL_LOC_Hyp_2140 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Throwcontrol_2139', tco_apply(shen_catchpoint, [])), tail_call(shen_cutpoint, [KL_CTX.KL_LOC_Throwcontrol_2139, [setattr(KL_CTX, 'KL_LOC_Hyp_2140', tco_apply(shen_newpv, [KL_ARG_V2927_2137])), [tco_apply(shen_incinfs, []), tco_apply(shen_tmsx45x62hyp, [tco_apply(shen_ues, [KL_ARG_V2925_2135]), KL_CTX.KL_LOC_Hyp_2140, KL_ARG_V2927_2137, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2139, KL_ARG_V2927_2137, (lambda : tail_call(shen_tx42, [[KL_ARG_V2925_2135, [symdic.symdic_kl_x58, [KL_ARG_V2926_2136, []]]], KL_CTX.KL_LOC_Hyp_2140, KL_ARG_V2927_2137, KL_ARG_V2928_2138]))]))])][(-1)]][(-1)]])][(-1)]
shen_add_fun('shen.t*-pattern', shen_tx42x45pattern)

@tail_recursion
def shen_tmsx45x62hyp(KL_ARG_V2929_2141, KL_ARG_V2930_2142, KL_ARG_V2931_2143, KL_ARG_V2932_2144):

    class KL_Context:
        KL_LOC_Case_2145 = None
        KL_LOC_V2453_2146 = None
        KL_LOC_V2454_2147 = None
        KL_LOC_Result_2148 = None
        KL_LOC_V2455_2149 = None
        KL_LOC_Tm2450_2150 = None
        KL_LOC_Tms_2151 = None
        KL_LOC_V2456_2152 = None
        KL_LOC_V2457_2153 = None
        KL_LOC_Tm_2154 = None
        KL_LOC_V2458_2155 = None
        KL_LOC_V2459_2156 = None
        KL_LOC_V2460_2157 = None
        KL_LOC_A_2158 = None
        KL_LOC_V2461_2159 = None
        KL_LOC_Hyp_2160 = None
        KL_LOC_Result_2161 = None
        KL_LOC_Hyp_2162 = None
        KL_LOC_A_2163 = None
        KL_LOC_Result_2164 = None
        KL_LOC_Hyp_2165 = None
        KL_LOC_Result_2166 = None
        KL_LOC_V2462_2167 = None
        KL_LOC_A_2168 = None
        KL_LOC_V2463_2169 = None
        KL_LOC_Hyp_2170 = None
        KL_LOC_Result_2171 = None
        KL_LOC_Hyp_2172 = None
        KL_LOC_A_2173 = None
        KL_LOC_Result_2174 = None
        KL_LOC_Hyp_2175 = None
        KL_LOC_A_2176 = None
        KL_LOC_Result_2177 = None
        KL_LOC_Hyp_2178 = None
        KL_LOC_Tm_2179 = None
        KL_LOC_A_2180 = None
        KL_LOC_Result_2181 = None
        KL_LOC_Hyp_2182 = None
        KL_LOC_Tm_2183 = None
        KL_LOC_A_2184 = None
        KL_LOC_Hyp_2185 = None
        KL_LOC_Result_2186 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Case_2145', [setattr(KL_CTX, 'KL_LOC_V2453_2146', tco_apply(shen_lazyderef, [KL_ARG_V2929_2141, KL_ARG_V2931_2143])), ([setattr(KL_CTX, 'KL_LOC_V2454_2147', tco_apply(shen_lazyderef, [KL_ARG_V2930_2142, KL_ARG_V2931_2143])), ([tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V2932_2144])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2454_2147) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2454_2147, [], KL_ARG_V2931_2143]), [setattr(KL_CTX, 'KL_LOC_Result_2148', [tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V2932_2144])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2454_2147, KL_ARG_V2931_2143]), KL_CTX.KL_LOC_Result_2148][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2454_2147]) else False))][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2453_2146) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_V2455_2149', tco_apply(shen_lazyderef, [KL_ARG_V2929_2141, KL_ARG_V2931_2143])), ([setattr(KL_CTX, 'KL_LOC_Tm2450_2150', KL_CTX.KL_LOC_V2455_2149[0]), [setattr(KL_CTX, 'KL_LOC_Tms_2151', KL_CTX.KL_LOC_V2455_2149[1]), [setattr(KL_CTX, 'KL_LOC_V2456_2152', tco_apply(shen_lazyderef, [KL_ARG_V2930_2142, KL_ARG_V2931_2143])), ([setattr(KL_CTX, 'KL_LOC_V2457_2153', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2456_2152[0], KL_ARG_V2931_2143])), ([setattr(KL_CTX, 'KL_LOC_Tm_2154', KL_CTX.KL_LOC_V2457_2153[0]), [setattr(KL_CTX, 'KL_LOC_V2458_2155', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2457_2153[1], KL_ARG_V2931_2143])), ([setattr(KL_CTX, 'KL_LOC_V2459_2156', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2458_2155[0], KL_ARG_V2931_2143])), ([setattr(KL_CTX, 'KL_LOC_V2460_2157', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2458_2155[1], KL_ARG_V2931_2143])), ([setattr(KL_CTX, 'KL_LOC_A_2158', KL_CTX.KL_LOC_V2460_2157[0]), [setattr(KL_CTX, 'KL_LOC_V2461_2159', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2460_2157[1], KL_ARG_V2931_2143])), ([setattr(KL_CTX, 'KL_LOC_Hyp_2160', KL_CTX.KL_LOC_V2456_2152[1]), [tco_apply(shen_incinfs, []), tail_call(kl_unifyx33, [KL_CTX.KL_LOC_Tm_2154, KL_CTX.KL_LOC_Tm2450_2150, KL_ARG_V2931_2143, (lambda : tail_call(shen_tmsx45x62hyp, [KL_CTX.KL_LOC_Tms_2151, KL_CTX.KL_LOC_Hyp_2160, KL_ARG_V2931_2143, KL_ARG_V2932_2144]))])][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2461_2159) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2461_2159, [], KL_ARG_V2931_2143]), [setattr(KL_CTX, 'KL_LOC_Result_2161', [setattr(KL_CTX, 'KL_LOC_Hyp_2162', KL_CTX.KL_LOC_V2456_2152[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_Tm_2154, KL_CTX.KL_LOC_Tm2450_2150, KL_ARG_V2931_2143, (lambda : tail_call(shen_tmsx45x62hyp, [KL_CTX.KL_LOC_Tms_2151, KL_CTX.KL_LOC_Hyp_2162, KL_ARG_V2931_2143, KL_ARG_V2932_2144]))])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2461_2159, KL_ARG_V2931_2143]), KL_CTX.KL_LOC_Result_2161][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2461_2159]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2460_2157) else ([setattr(KL_CTX, 'KL_LOC_A_2163', tco_apply(shen_newpv, [KL_ARG_V2931_2143])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2460_2157, [KL_CTX.KL_LOC_A_2163, []], KL_ARG_V2931_2143]), [setattr(KL_CTX, 'KL_LOC_Result_2164', [setattr(KL_CTX, 'KL_LOC_Hyp_2165', KL_CTX.KL_LOC_V2456_2152[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_Tm_2154, KL_CTX.KL_LOC_Tm2450_2150, KL_ARG_V2931_2143, (lambda : tail_call(shen_tmsx45x62hyp, [KL_CTX.KL_LOC_Tms_2151, KL_CTX.KL_LOC_Hyp_2165, KL_ARG_V2931_2143, KL_ARG_V2932_2144]))])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2460_2157, KL_ARG_V2931_2143]), KL_CTX.KL_LOC_Result_2164][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2460_2157]) else False))][(-1)] if shen_eq(symdic.symdic_kl_x58, KL_CTX.KL_LOC_V2459_2156) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2459_2156, symdic.symdic_kl_x58, KL_ARG_V2931_2143]), [setattr(KL_CTX, 'KL_LOC_Result_2166', [setattr(KL_CTX, 'KL_LOC_V2462_2167', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2458_2155[1], KL_ARG_V2931_2143])), ([setattr(KL_CTX, 'KL_LOC_A_2168', KL_CTX.KL_LOC_V2462_2167[0]), [setattr(KL_CTX, 'KL_LOC_V2463_2169', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2462_2167[1], KL_ARG_V2931_2143])), ([setattr(KL_CTX, 'KL_LOC_Hyp_2170', KL_CTX.KL_LOC_V2456_2152[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_Tm_2154, KL_CTX.KL_LOC_Tm2450_2150, KL_ARG_V2931_2143, (lambda : tail_call(shen_tmsx45x62hyp, [KL_CTX.KL_LOC_Tms_2151, KL_CTX.KL_LOC_Hyp_2170, KL_ARG_V2931_2143, KL_ARG_V2932_2144]))])][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2463_2169) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2463_2169, [], KL_ARG_V2931_2143]), [setattr(KL_CTX, 'KL_LOC_Result_2171', [setattr(KL_CTX, 'KL_LOC_Hyp_2172', KL_CTX.KL_LOC_V2456_2152[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_Tm_2154, KL_CTX.KL_LOC_Tm2450_2150, KL_ARG_V2931_2143, (lambda : tail_call(shen_tmsx45x62hyp, [KL_CTX.KL_LOC_Tms_2151, KL_CTX.KL_LOC_Hyp_2172, KL_ARG_V2931_2143, KL_ARG_V2932_2144]))])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2463_2169, KL_ARG_V2931_2143]), KL_CTX.KL_LOC_Result_2171][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2463_2169]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2462_2167) else ([setattr(KL_CTX, 'KL_LOC_A_2173', tco_apply(shen_newpv, [KL_ARG_V2931_2143])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2462_2167, [KL_CTX.KL_LOC_A_2173, []], KL_ARG_V2931_2143]), [setattr(KL_CTX, 'KL_LOC_Result_2174', [setattr(KL_CTX, 'KL_LOC_Hyp_2175', KL_CTX.KL_LOC_V2456_2152[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_Tm_2154, KL_CTX.KL_LOC_Tm2450_2150, KL_ARG_V2931_2143, (lambda : tail_call(shen_tmsx45x62hyp, [KL_CTX.KL_LOC_Tms_2151, KL_CTX.KL_LOC_Hyp_2175, KL_ARG_V2931_2143, KL_ARG_V2932_2144]))])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2462_2167, KL_ARG_V2931_2143]), KL_CTX.KL_LOC_Result_2174][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2462_2167]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2459_2156, KL_ARG_V2931_2143]), KL_CTX.KL_LOC_Result_2166][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2459_2156]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2458_2155) else ([setattr(KL_CTX, 'KL_LOC_A_2176', tco_apply(shen_newpv, [KL_ARG_V2931_2143])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2458_2155, [symdic.symdic_kl_x58, [KL_CTX.KL_LOC_A_2176, []]], KL_ARG_V2931_2143]), [setattr(KL_CTX, 'KL_LOC_Result_2177', [setattr(KL_CTX, 'KL_LOC_Hyp_2178', KL_CTX.KL_LOC_V2456_2152[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_Tm_2154, KL_CTX.KL_LOC_Tm2450_2150, KL_ARG_V2931_2143, (lambda : tail_call(shen_tmsx45x62hyp, [KL_CTX.KL_LOC_Tms_2151, KL_CTX.KL_LOC_Hyp_2178, KL_ARG_V2931_2143, KL_ARG_V2932_2144]))])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2458_2155, KL_ARG_V2931_2143]), KL_CTX.KL_LOC_Result_2177][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2458_2155]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2457_2153) else ([setattr(KL_CTX, 'KL_LOC_Tm_2179', tco_apply(shen_newpv, [KL_ARG_V2931_2143])), [setattr(KL_CTX, 'KL_LOC_A_2180', tco_apply(shen_newpv, [KL_ARG_V2931_2143])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2457_2153, [KL_CTX.KL_LOC_Tm_2179, [symdic.symdic_kl_x58, [KL_CTX.KL_LOC_A_2180, []]]], KL_ARG_V2931_2143]), [setattr(KL_CTX, 'KL_LOC_Result_2181', [setattr(KL_CTX, 'KL_LOC_Hyp_2182', KL_CTX.KL_LOC_V2456_2152[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_Tm_2179, KL_CTX.KL_LOC_Tm2450_2150, KL_ARG_V2931_2143, (lambda : tail_call(shen_tmsx45x62hyp, [KL_CTX.KL_LOC_Tms_2151, KL_CTX.KL_LOC_Hyp_2182, KL_ARG_V2931_2143, KL_ARG_V2932_2144]))])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2457_2153, KL_ARG_V2931_2143]), KL_CTX.KL_LOC_Result_2181][(-1)]][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2457_2153]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2456_2152) else ([setattr(KL_CTX, 'KL_LOC_Tm_2183', tco_apply(shen_newpv, [KL_ARG_V2931_2143])), [setattr(KL_CTX, 'KL_LOC_A_2184', tco_apply(shen_newpv, [KL_ARG_V2931_2143])), [setattr(KL_CTX, 'KL_LOC_Hyp_2185', tco_apply(shen_newpv, [KL_ARG_V2931_2143])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2456_2152, [[KL_CTX.KL_LOC_Tm_2183, [symdic.symdic_kl_x58, [KL_CTX.KL_LOC_A_2184, []]]], KL_CTX.KL_LOC_Hyp_2185], KL_ARG_V2931_2143]), [setattr(KL_CTX, 'KL_LOC_Result_2186', [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_Tm_2183, KL_CTX.KL_LOC_Tm2450_2150, KL_ARG_V2931_2143, (lambda : tail_call(shen_tmsx45x62hyp, [KL_CTX.KL_LOC_Tms_2151, KL_CTX.KL_LOC_Hyp_2185, KL_ARG_V2931_2143, KL_ARG_V2932_2144]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2456_2152, KL_ARG_V2931_2143]), KL_CTX.KL_LOC_Result_2186][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2456_2152]) else False))][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2455_2149) else False)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2145, False) else KL_CTX.KL_LOC_Case_2145)][(-1)]
shen_add_fun('shen.tms->hyp', shen_tmsx45x62hyp)

@tail_recursion
def kl_findall(KL_ARG_V2933_2187, KL_ARG_V2934_2188, KL_ARG_V2935_2189, KL_ARG_V2936_2190, KL_ARG_V2937_2191):

    class KL_Context:
        KL_LOC_B_2192 = None
        KL_LOC_A_2193 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_B_2192', tco_apply(shen_newpv, [KL_ARG_V2936_2190])), [setattr(KL_CTX, 'KL_LOC_A_2193', tco_apply(shen_newpv, [KL_ARG_V2936_2190])), [tco_apply(shen_incinfs, []), tail_call(kl_bind, [KL_CTX.KL_LOC_A_2193, tco_apply(kl_gensym, [symdic.symdic_shen_a]), KL_ARG_V2936_2190, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_B_2192, shen_set(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_2193, KL_ARG_V2936_2190]), []), KL_ARG_V2936_2190, (lambda : tail_call(shen_findallhelp, [KL_ARG_V2933_2187, KL_ARG_V2934_2188, KL_ARG_V2935_2189, KL_CTX.KL_LOC_A_2193, KL_ARG_V2936_2190, KL_ARG_V2937_2191]))]))])][(-1)]][(-1)]][(-1)]
shen_add_fun('findall', kl_findall)

@tail_recursion
def shen_findallhelp(KL_ARG_V2938_2194, KL_ARG_V2939_2195, KL_ARG_V2940_2196, KL_ARG_V2941_2197, KL_ARG_V2942_2198, KL_ARG_V2943_2199):

    class KL_Context:
        KL_LOC_Case_2200 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Case_2200', [tco_apply(shen_incinfs, []), tco_apply(kl_call, [KL_ARG_V2939_2195, KL_ARG_V2942_2198, (lambda : tail_call(shen_remember, [KL_ARG_V2941_2197, KL_ARG_V2938_2194, KL_ARG_V2942_2198, (lambda : tail_call(kl_fwhen, [False, KL_ARG_V2942_2198, KL_ARG_V2943_2199]))]))])][(-1)]), ([tco_apply(shen_incinfs, []), tail_call(kl_bind, [KL_ARG_V2940_2196, shen_get(tco_apply(shen_lazyderef, [KL_ARG_V2941_2197, KL_ARG_V2942_2198])), KL_ARG_V2942_2198, KL_ARG_V2943_2199])][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2200, False) else KL_CTX.KL_LOC_Case_2200)][(-1)]
shen_add_fun('shen.findallhelp', shen_findallhelp)

@tail_recursion
def shen_remember(KL_ARG_V2944_2201, KL_ARG_V2945_2202, KL_ARG_V2946_2203, KL_ARG_V2947_2204):

    class KL_Context:
        KL_LOC_B_2205 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_B_2205', tco_apply(shen_newpv, [KL_ARG_V2946_2203])), [tco_apply(shen_incinfs, []), tail_call(kl_bind, [KL_CTX.KL_LOC_B_2205, shen_set(tco_apply(shen_deref, [KL_ARG_V2944_2201, KL_ARG_V2946_2203]), [tco_apply(shen_deref, [KL_ARG_V2945_2202, KL_ARG_V2946_2203]), shen_get(tco_apply(shen_deref, [KL_ARG_V2944_2201, KL_ARG_V2946_2203]))]), KL_ARG_V2946_2203, KL_ARG_V2947_2204])][(-1)]][(-1)]
shen_add_fun('shen.remember', shen_remember)

@tail_recursion
def shen_tx42x45defcc(KL_ARG_V2948_2206, KL_ARG_V2949_2207, KL_ARG_V2950_2208, KL_ARG_V2951_2209, KL_ARG_V2952_2210):

    class KL_Context:
        KL_LOC_Throwcontrol_2211 = None
        KL_LOC_V2426_2212 = None
        KL_LOC_V2427_2213 = None
        KL_LOC_V2428_2214 = None
        KL_LOC_F_2215 = None
        KL_LOC_V2429_2216 = None
        KL_LOC_V2430_2217 = None
        KL_LOC_V2431_2218 = None
        KL_LOC_V2432_2219 = None
        KL_LOC_V2433_2220 = None
        KL_LOC_V2434_2221 = None
        KL_LOC_A_2222 = None
        KL_LOC_V2435_2223 = None
        KL_LOC_V2436_2224 = None
        KL_LOC_V2437_2225 = None
        KL_LOC_V2438_2226 = None
        KL_LOC_B_2227 = None
        KL_LOC_V2439_2228 = None
        KL_LOC_V2440_2229 = None
        KL_LOC_Rest_2230 = None
        KL_LOC_Restx38_2231 = None
        KL_LOC_Restx38x38_2232 = None
        KL_LOC_Rules_2233 = None
        KL_LOC_ListAx38x38_2234 = None
        KL_LOC_Bx38x38_2235 = None
        KL_LOC_Sig_2236 = None
        KL_LOC_Declare_2237 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Throwcontrol_2211', tco_apply(shen_catchpoint, [])), tail_call(shen_cutpoint, [KL_CTX.KL_LOC_Throwcontrol_2211, [setattr(KL_CTX, 'KL_LOC_V2426_2212', tco_apply(shen_lazyderef, [KL_ARG_V2948_2206, KL_ARG_V2951_2209])), ([setattr(KL_CTX, 'KL_LOC_V2427_2213', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2426_2212[0], KL_ARG_V2951_2209])), ([setattr(KL_CTX, 'KL_LOC_V2428_2214', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2426_2212[1], KL_ARG_V2951_2209])), ([setattr(KL_CTX, 'KL_LOC_F_2215', KL_CTX.KL_LOC_V2428_2214[0]), [setattr(KL_CTX, 'KL_LOC_V2429_2216', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2428_2214[1], KL_ARG_V2951_2209])), ([setattr(KL_CTX, 'KL_LOC_V2430_2217', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2429_2216[0], KL_ARG_V2951_2209])), ([setattr(KL_CTX, 'KL_LOC_V2431_2218', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2429_2216[1], KL_ARG_V2951_2209])), ([setattr(KL_CTX, 'KL_LOC_V2432_2219', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2431_2218[0], KL_ARG_V2951_2209])), ([setattr(KL_CTX, 'KL_LOC_V2433_2220', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2432_2219[0], KL_ARG_V2951_2209])), ([setattr(KL_CTX, 'KL_LOC_V2434_2221', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2432_2219[1], KL_ARG_V2951_2209])), ([setattr(KL_CTX, 'KL_LOC_A_2222', KL_CTX.KL_LOC_V2434_2221[0]), [setattr(KL_CTX, 'KL_LOC_V2435_2223', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2434_2221[1], KL_ARG_V2951_2209])), ([setattr(KL_CTX, 'KL_LOC_V2436_2224', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2431_2218[1], KL_ARG_V2951_2209])), ([setattr(KL_CTX, 'KL_LOC_V2437_2225', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2436_2224[0], KL_ARG_V2951_2209])), ([setattr(KL_CTX, 'KL_LOC_V2438_2226', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2436_2224[1], KL_ARG_V2951_2209])), ([setattr(KL_CTX, 'KL_LOC_B_2227', KL_CTX.KL_LOC_V2438_2226[0]), [setattr(KL_CTX, 'KL_LOC_V2439_2228', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2438_2226[1], KL_ARG_V2951_2209])), ([setattr(KL_CTX, 'KL_LOC_V2440_2229', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2439_2228[0], KL_ARG_V2951_2209])), ([setattr(KL_CTX, 'KL_LOC_Rest_2230', KL_CTX.KL_LOC_V2439_2228[1]), [setattr(KL_CTX, 'KL_LOC_Restx38_2231', tco_apply(shen_newpv, [KL_ARG_V2951_2209])), [setattr(KL_CTX, 'KL_LOC_Restx38x38_2232', tco_apply(shen_newpv, [KL_ARG_V2951_2209])), [setattr(KL_CTX, 'KL_LOC_Rules_2233', tco_apply(shen_newpv, [KL_ARG_V2951_2209])), [setattr(KL_CTX, 'KL_LOC_ListAx38x38_2234', tco_apply(shen_newpv, [KL_ARG_V2951_2209])), [setattr(KL_CTX, 'KL_LOC_Bx38x38_2235', tco_apply(shen_newpv, [KL_ARG_V2951_2209])), [setattr(KL_CTX, 'KL_LOC_Sig_2236', tco_apply(shen_newpv, [KL_ARG_V2951_2209])), [setattr(KL_CTX, 'KL_LOC_Declare_2237', tco_apply(shen_newpv, [KL_ARG_V2951_2209])), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_CTX.KL_LOC_Sig_2236, tco_apply(shen_ue, [[[symdic.symdic_kl_list, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_2222, KL_ARG_V2951_2209]), []]], [symdic.symdic_kl_x61x61x62, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_2227, KL_ARG_V2951_2209]), []]]]]), KL_ARG_V2951_2209, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_ListAx38x38_2234, tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Sig_2236, KL_ARG_V2951_2209])[0], KL_ARG_V2951_2209, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Bx38x38_2235, tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Sig_2236, KL_ARG_V2951_2209])[1][1][0], KL_ARG_V2951_2209, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Restx38_2231, tco_apply(shen_plugx45wildcards, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Rest_2230, KL_ARG_V2951_2209])]), KL_ARG_V2951_2209, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Restx38x38_2232, tco_apply(shen_ue, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Restx38_2231, KL_ARG_V2951_2209])]), KL_ARG_V2951_2209, (lambda : tail_call(shen_getx45rules, [KL_CTX.KL_LOC_Rules_2233, KL_CTX.KL_LOC_Restx38x38_2232, KL_ARG_V2951_2209, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2211, KL_ARG_V2951_2209, (lambda : tail_call(shen_tcx45rules, [KL_CTX.KL_LOC_F_2215, KL_CTX.KL_LOC_Rules_2233, KL_CTX.KL_LOC_ListAx38x38_2234, KL_CTX.KL_LOC_Bx38x38_2235, [[KL_CTX.KL_LOC_F_2215, [symdic.symdic_kl_x58, [KL_CTX.KL_LOC_Sig_2236, []]]], KL_ARG_V2950_2208], 1, KL_ARG_V2951_2209, (lambda : tail_call(kl_unify, [KL_ARG_V2949_2207, [[symdic.symdic_kl_list, [KL_CTX.KL_LOC_A_2222, []]], [symdic.symdic_kl_x61x61x62, [KL_CTX.KL_LOC_B_2227, []]]], KL_ARG_V2951_2209, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Declare_2237, apply(kl_declare, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_F_2215, KL_ARG_V2951_2209]), [[symdic.symdic_kl_list, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_2222, KL_ARG_V2951_2209]), []]], [symdic.symdic_kl_x61x61x62, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_2227, KL_ARG_V2951_2209]), []]]]]), KL_ARG_V2951_2209, KL_ARG_V2952_2210]))]))]))]))]))]))]))]))]))])][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)] if shen_eq(symdic.symdic_kl_x125, KL_CTX.KL_LOC_V2440_2229) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2439_2228) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2438_2226) else False)][(-1)] if shen_eq(symdic.symdic_kl_x61x61x62, KL_CTX.KL_LOC_V2437_2225) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2436_2224) else False)][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2435_2223) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2434_2221) else False)][(-1)] if shen_eq(symdic.symdic_kl_list, KL_CTX.KL_LOC_V2433_2220) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2432_2219) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2431_2218) else False)][(-1)] if shen_eq(symdic.symdic_kl_x123, KL_CTX.KL_LOC_V2430_2217) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2429_2216) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2428_2214) else False)][(-1)] if shen_eq(symdic.symdic_kl_defcc, KL_CTX.KL_LOC_V2427_2213) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2426_2212) else False)][(-1)]])][(-1)]
shen_add_fun('shen.t*-defcc', shen_tx42x45defcc)

@tail_recursion
def shen_plugx45wildcards(KL_ARG_V2953_2238):
    global symdic
    return (tail_call(kl_map, [symdic.symdic_shen_plugx45wildcards, KL_ARG_V2953_2238]) if shen_consp(KL_ARG_V2953_2238) else (tail_call(kl_gensym, [shen_intern('X')]) if shen_eq(KL_ARG_V2953_2238, symdic.symdic_kl__) else (KL_ARG_V2953_2238 if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.plug-wildcards', shen_plugx45wildcards)

@tail_recursion
def shen_getx45rules(KL_ARG_V2954_2239, KL_ARG_V2955_2240, KL_ARG_V2956_2241, KL_ARG_V2957_2242):

    class KL_Context:
        KL_LOC_Throwcontrol_2243 = None
        KL_LOC_Case_2244 = None
        KL_LOC_V2419_2245 = None
        KL_LOC_V2420_2246 = None
        KL_LOC_Result_2247 = None
        KL_LOC_V2421_2248 = None
        KL_LOC_V2422_2249 = None
        KL_LOC_Rule_2250 = None
        KL_LOC_Rules_2251 = None
        KL_LOC_Other_2252 = None
        KL_LOC_Rule_2253 = None
        KL_LOC_Rules_2254 = None
        KL_LOC_Result_2255 = None
        KL_LOC_Other_2256 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Throwcontrol_2243', tco_apply(shen_catchpoint, [])), tail_call(shen_cutpoint, [KL_CTX.KL_LOC_Throwcontrol_2243, [setattr(KL_CTX, 'KL_LOC_Case_2244', [setattr(KL_CTX, 'KL_LOC_V2419_2245', tco_apply(shen_lazyderef, [KL_ARG_V2954_2239, KL_ARG_V2956_2241])), ([setattr(KL_CTX, 'KL_LOC_V2420_2246', tco_apply(shen_lazyderef, [KL_ARG_V2955_2240, KL_ARG_V2956_2241])), ([tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2243, KL_ARG_V2956_2241, KL_ARG_V2957_2242])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2420_2246) else False)][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2419_2245) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2419_2245, [], KL_ARG_V2956_2241]), [setattr(KL_CTX, 'KL_LOC_Result_2247', [setattr(KL_CTX, 'KL_LOC_V2421_2248', tco_apply(shen_lazyderef, [KL_ARG_V2955_2240, KL_ARG_V2956_2241])), ([tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2243, KL_ARG_V2956_2241, KL_ARG_V2957_2242])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2421_2248) else False)][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2419_2245, KL_ARG_V2956_2241]), KL_CTX.KL_LOC_Result_2247][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2419_2245]) else False))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_V2422_2249', tco_apply(shen_lazyderef, [KL_ARG_V2954_2239, KL_ARG_V2956_2241])), ([setattr(KL_CTX, 'KL_LOC_Rule_2250', KL_CTX.KL_LOC_V2422_2249[0]), [setattr(KL_CTX, 'KL_LOC_Rules_2251', KL_CTX.KL_LOC_V2422_2249[1]), [setattr(KL_CTX, 'KL_LOC_Other_2252', tco_apply(shen_newpv, [KL_ARG_V2956_2241])), [tco_apply(shen_incinfs, []), tco_apply(shen_firstx45rule, [KL_ARG_V2955_2240, KL_CTX.KL_LOC_Rule_2250, KL_CTX.KL_LOC_Other_2252, KL_ARG_V2956_2241, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2243, KL_ARG_V2956_2241, (lambda : tail_call(shen_getx45rules, [KL_CTX.KL_LOC_Rules_2251, KL_CTX.KL_LOC_Other_2252, KL_ARG_V2956_2241, KL_ARG_V2957_2242]))]))])][(-1)]][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2422_2249) else ([setattr(KL_CTX, 'KL_LOC_Rule_2253', tco_apply(shen_newpv, [KL_ARG_V2956_2241])), [setattr(KL_CTX, 'KL_LOC_Rules_2254', tco_apply(shen_newpv, [KL_ARG_V2956_2241])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2422_2249, [KL_CTX.KL_LOC_Rule_2253, KL_CTX.KL_LOC_Rules_2254], KL_ARG_V2956_2241]), [setattr(KL_CTX, 'KL_LOC_Result_2255', [setattr(KL_CTX, 'KL_LOC_Other_2256', tco_apply(shen_newpv, [KL_ARG_V2956_2241])), [tco_apply(shen_incinfs, []), tco_apply(shen_firstx45rule, [KL_ARG_V2955_2240, KL_CTX.KL_LOC_Rule_2253, KL_CTX.KL_LOC_Other_2256, KL_ARG_V2956_2241, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2243, KL_ARG_V2956_2241, (lambda : tail_call(shen_getx45rules, [KL_CTX.KL_LOC_Rules_2254, KL_CTX.KL_LOC_Other_2256, KL_ARG_V2956_2241, KL_ARG_V2957_2242]))]))])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2422_2249, KL_ARG_V2956_2241]), KL_CTX.KL_LOC_Result_2255][(-1)]][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2422_2249]) else False))][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2244, False) else KL_CTX.KL_LOC_Case_2244)][(-1)]])][(-1)]
shen_add_fun('shen.get-rules', shen_getx45rules)

@tail_recursion
def shen_firstx45rule(KL_ARG_V2958_2257, KL_ARG_V2959_2258, KL_ARG_V2960_2259, KL_ARG_V2961_2260, KL_ARG_V2962_2261):

    class KL_Context:
        KL_LOC_Throwcontrol_2262 = None
        KL_LOC_Case_2263 = None
        KL_LOC_V2412_2264 = None
        KL_LOC_V2413_2265 = None
        KL_LOC_Other2407_2266 = None
        KL_LOC_V2414_2267 = None
        KL_LOC_Result_2268 = None
        KL_LOC_V2415_2269 = None
        KL_LOC_X2408_2270 = None
        KL_LOC_Rest_2271 = None
        KL_LOC_V2416_2272 = None
        KL_LOC_X_2273 = None
        KL_LOC_Rule_2274 = None
        KL_LOC_X_2275 = None
        KL_LOC_Rule_2276 = None
        KL_LOC_Result_2277 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Throwcontrol_2262', tco_apply(shen_catchpoint, [])), tail_call(shen_cutpoint, [KL_CTX.KL_LOC_Throwcontrol_2262, [setattr(KL_CTX, 'KL_LOC_Case_2263', [setattr(KL_CTX, 'KL_LOC_V2412_2264', tco_apply(shen_lazyderef, [KL_ARG_V2958_2257, KL_ARG_V2961_2260])), ([setattr(KL_CTX, 'KL_LOC_V2413_2265', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2412_2264[0], KL_ARG_V2961_2260])), ([setattr(KL_CTX, 'KL_LOC_Other2407_2266', KL_CTX.KL_LOC_V2412_2264[1]), [setattr(KL_CTX, 'KL_LOC_V2414_2267', tco_apply(shen_lazyderef, [KL_ARG_V2959_2258, KL_ARG_V2961_2260])), ([tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_ARG_V2960_2259, KL_CTX.KL_LOC_Other2407_2266, KL_ARG_V2961_2260, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2262, KL_ARG_V2961_2260, KL_ARG_V2962_2261]))])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2414_2267) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2414_2267, [], KL_ARG_V2961_2260]), [setattr(KL_CTX, 'KL_LOC_Result_2268', [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_ARG_V2960_2259, KL_CTX.KL_LOC_Other2407_2266, KL_ARG_V2961_2260, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2262, KL_ARG_V2961_2260, KL_ARG_V2962_2261]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2414_2267, KL_ARG_V2961_2260]), KL_CTX.KL_LOC_Result_2268][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2414_2267]) else False))][(-1)]][(-1)] if shen_eq(symdic.symdic_kl_x59, KL_CTX.KL_LOC_V2413_2265) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2412_2264) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_V2415_2269', tco_apply(shen_lazyderef, [KL_ARG_V2958_2257, KL_ARG_V2961_2260])), ([setattr(KL_CTX, 'KL_LOC_X2408_2270', KL_CTX.KL_LOC_V2415_2269[0]), [setattr(KL_CTX, 'KL_LOC_Rest_2271', KL_CTX.KL_LOC_V2415_2269[1]), [setattr(KL_CTX, 'KL_LOC_V2416_2272', tco_apply(shen_lazyderef, [KL_ARG_V2959_2258, KL_ARG_V2961_2260])), ([setattr(KL_CTX, 'KL_LOC_X_2273', KL_CTX.KL_LOC_V2416_2272[0]), [setattr(KL_CTX, 'KL_LOC_Rule_2274', KL_CTX.KL_LOC_V2416_2272[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_X_2273, KL_CTX.KL_LOC_X2408_2270, KL_ARG_V2961_2260, (lambda : tail_call(shen_firstx45rule, [KL_CTX.KL_LOC_Rest_2271, KL_CTX.KL_LOC_Rule_2274, KL_ARG_V2960_2259, KL_ARG_V2961_2260, KL_ARG_V2962_2261]))])][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2416_2272) else ([setattr(KL_CTX, 'KL_LOC_X_2275', tco_apply(shen_newpv, [KL_ARG_V2961_2260])), [setattr(KL_CTX, 'KL_LOC_Rule_2276', tco_apply(shen_newpv, [KL_ARG_V2961_2260])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2416_2272, [KL_CTX.KL_LOC_X_2275, KL_CTX.KL_LOC_Rule_2276], KL_ARG_V2961_2260]), [setattr(KL_CTX, 'KL_LOC_Result_2277', [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_X_2275, KL_CTX.KL_LOC_X2408_2270, KL_ARG_V2961_2260, (lambda : tail_call(shen_firstx45rule, [KL_CTX.KL_LOC_Rest_2271, KL_CTX.KL_LOC_Rule_2276, KL_ARG_V2960_2259, KL_ARG_V2961_2260, KL_ARG_V2962_2261]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2416_2272, KL_ARG_V2961_2260]), KL_CTX.KL_LOC_Result_2277][(-1)]][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2416_2272]) else False))][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2415_2269) else False)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2263, False) else KL_CTX.KL_LOC_Case_2263)][(-1)]])][(-1)]
shen_add_fun('shen.first-rule', shen_firstx45rule)

@tail_recursion
def shen_tcx45rules(KL_ARG_V2963_2278, KL_ARG_V2964_2279, KL_ARG_V2965_2280, KL_ARG_V2966_2281, KL_ARG_V2967_2282, KL_ARG_V2968_2283, KL_ARG_V2969_2284, KL_ARG_V2970_2285):

    class KL_Context:
        KL_LOC_Throwcontrol_2286 = None
        KL_LOC_Case_2287 = None
        KL_LOC_V2401_2288 = None
        KL_LOC_V2402_2289 = None
        KL_LOC_Rule_2290 = None
        KL_LOC_Rules_2291 = None
        KL_LOC_V2403_2292 = None
        KL_LOC_V2404_2293 = None
        KL_LOC_V2405_2294 = None
        KL_LOC_A_2295 = None
        KL_LOC_V2406_2296 = None
        KL_LOC_M_2297 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Throwcontrol_2286', tco_apply(shen_catchpoint, [])), tail_call(shen_cutpoint, [KL_CTX.KL_LOC_Throwcontrol_2286, [setattr(KL_CTX, 'KL_LOC_Case_2287', [setattr(KL_CTX, 'KL_LOC_V2401_2288', tco_apply(shen_lazyderef, [KL_ARG_V2964_2279, KL_ARG_V2969_2284])), ([tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V2970_2285])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2401_2288) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_V2402_2289', tco_apply(shen_lazyderef, [KL_ARG_V2964_2279, KL_ARG_V2969_2284])), ([setattr(KL_CTX, 'KL_LOC_Rule_2290', KL_CTX.KL_LOC_V2402_2289[0]), [setattr(KL_CTX, 'KL_LOC_Rules_2291', KL_CTX.KL_LOC_V2402_2289[1]), [setattr(KL_CTX, 'KL_LOC_V2403_2292', tco_apply(shen_lazyderef, [KL_ARG_V2965_2280, KL_ARG_V2969_2284])), ([setattr(KL_CTX, 'KL_LOC_V2404_2293', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2403_2292[0], KL_ARG_V2969_2284])), ([setattr(KL_CTX, 'KL_LOC_V2405_2294', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2403_2292[1], KL_ARG_V2969_2284])), ([setattr(KL_CTX, 'KL_LOC_A_2295', KL_CTX.KL_LOC_V2405_2294[0]), [setattr(KL_CTX, 'KL_LOC_V2406_2296', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2405_2294[1], KL_ARG_V2969_2284])), ([setattr(KL_CTX, 'KL_LOC_M_2297', tco_apply(shen_newpv, [KL_ARG_V2969_2284])), [tco_apply(shen_incinfs, []), tco_apply(shen_tcx45rule, [KL_ARG_V2963_2278, KL_CTX.KL_LOC_Rule_2290, KL_CTX.KL_LOC_A_2295, KL_ARG_V2966_2281, KL_ARG_V2967_2282, KL_ARG_V2968_2283, KL_ARG_V2969_2284, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_M_2297, (tco_apply(shen_deref, [KL_ARG_V2968_2283, KL_ARG_V2969_2284]) + 1), KL_ARG_V2969_2284, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2286, KL_ARG_V2969_2284, (lambda : tail_call(shen_tcx45rules, [KL_ARG_V2963_2278, KL_CTX.KL_LOC_Rules_2291, [symdic.symdic_kl_list, [KL_CTX.KL_LOC_A_2295, []]], KL_ARG_V2966_2281, KL_ARG_V2967_2282, KL_CTX.KL_LOC_M_2297, KL_ARG_V2969_2284, KL_ARG_V2970_2285]))]))]))])][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2406_2296) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2405_2294) else False)][(-1)] if shen_eq(symdic.symdic_kl_list, KL_CTX.KL_LOC_V2404_2293) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2403_2292) else False)][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2402_2289) else False)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2287, False) else KL_CTX.KL_LOC_Case_2287)][(-1)]])][(-1)]
shen_add_fun('shen.tc-rules', shen_tcx45rules)

@tail_recursion
def shen_tcx45rule(KL_ARG_V2971_2298, KL_ARG_V2972_2299, KL_ARG_V2973_2300, KL_ARG_V2974_2301, KL_ARG_V2975_2302, KL_ARG_V2976_2303, KL_ARG_V2977_2304, KL_ARG_V2978_2305):

    class KL_Context:
        KL_LOC_Case_2306 = None
        KL_LOC_Err_2307 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Case_2306', [tco_apply(shen_incinfs, []), tco_apply(shen_checkx45defccx45rule, [KL_ARG_V2972_2299, KL_ARG_V2973_2300, KL_ARG_V2974_2301, KL_ARG_V2975_2302, KL_ARG_V2977_2304, KL_ARG_V2978_2305])][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Err_2307', tco_apply(shen_newpv, [KL_ARG_V2977_2304])), [tco_apply(shen_incinfs, []), tail_call(kl_bind, [KL_CTX.KL_LOC_Err_2307, shen_simple_error(('type error in rule ' + tco_apply(shen_app, [tco_apply(shen_lazyderef, [KL_ARG_V2976_2303, KL_ARG_V2977_2304]), (' of ' + tco_apply(shen_app, [tco_apply(shen_lazyderef, [KL_ARG_V2971_2298, KL_ARG_V2977_2304]), '', symdic.symdic_shen_a])), symdic.symdic_shen_a]))), KL_ARG_V2977_2304, KL_ARG_V2978_2305])][(-1)]][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2306, False) else KL_CTX.KL_LOC_Case_2306)][(-1)]
shen_add_fun('shen.tc-rule', shen_tcx45rule)

@tail_recursion
def shen_checkx45defccx45rule(KL_ARG_V2979_2308, KL_ARG_V2980_2309, KL_ARG_V2981_2310, KL_ARG_V2982_2311, KL_ARG_V2983_2312, KL_ARG_V2984_2313):

    class KL_Context:
        KL_LOC_Throwcontrol_2314 = None
        KL_LOC_Syntax_2315 = None
        KL_LOC_Semantics_2316 = None
        KL_LOC_SynHyps_2317 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Throwcontrol_2314', tco_apply(shen_catchpoint, [])), tail_call(shen_cutpoint, [KL_CTX.KL_LOC_Throwcontrol_2314, [setattr(KL_CTX, 'KL_LOC_Syntax_2315', tco_apply(shen_newpv, [KL_ARG_V2983_2312])), [setattr(KL_CTX, 'KL_LOC_Semantics_2316', tco_apply(shen_newpv, [KL_ARG_V2983_2312])), [setattr(KL_CTX, 'KL_LOC_SynHyps_2317', tco_apply(shen_newpv, [KL_ARG_V2983_2312])), [tco_apply(shen_incinfs, []), tco_apply(shen_getx45syntaxx43semantics, [KL_CTX.KL_LOC_Syntax_2315, KL_CTX.KL_LOC_Semantics_2316, KL_ARG_V2979_2308, KL_ARG_V2983_2312, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2314, KL_ARG_V2983_2312, (lambda : tail_call(shen_syntaxx45hyps, [KL_CTX.KL_LOC_Syntax_2315, KL_ARG_V2982_2311, KL_CTX.KL_LOC_SynHyps_2317, KL_ARG_V2980_2309, KL_ARG_V2983_2312, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2314, KL_ARG_V2983_2312, (lambda : tail_call(shen_syntaxx45check, [KL_CTX.KL_LOC_Syntax_2315, KL_ARG_V2980_2309, KL_CTX.KL_LOC_SynHyps_2317, KL_ARG_V2983_2312, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2314, KL_ARG_V2983_2312, (lambda : tail_call(shen_semanticsx45check, [KL_CTX.KL_LOC_Semantics_2316, KL_ARG_V2981_2310, KL_CTX.KL_LOC_SynHyps_2317, KL_ARG_V2983_2312, KL_ARG_V2984_2313]))]))]))]))]))]))])][(-1)]][(-1)]][(-1)]][(-1)]])][(-1)]
shen_add_fun('shen.check-defcc-rule', shen_checkx45defccx45rule)

@tail_recursion
def shen_syntaxx45hyps(KL_ARG_V2985_2318, KL_ARG_V2986_2319, KL_ARG_V2987_2320, KL_ARG_V2988_2321, KL_ARG_V2989_2322, KL_ARG_V2990_2323):

    class KL_Context:
        KL_LOC_Throwcontrol_2324 = None
        KL_LOC_Case_2325 = None
        KL_LOC_V2374_2326 = None
        KL_LOC_Case_2327 = None
        KL_LOC_V2375_2328 = None
        KL_LOC_X2368_2329 = None
        KL_LOC_Y_2330 = None
        KL_LOC_V2376_2331 = None
        KL_LOC_V2377_2332 = None
        KL_LOC_X_2333 = None
        KL_LOC_V2378_2334 = None
        KL_LOC_V2379_2335 = None
        KL_LOC_V2380_2336 = None
        KL_LOC_A2369_2337 = None
        KL_LOC_V2381_2338 = None
        KL_LOC_SynHyps_2339 = None
        KL_LOC_Result_2340 = None
        KL_LOC_SynHyps_2341 = None
        KL_LOC_A2369_2342 = None
        KL_LOC_Result_2343 = None
        KL_LOC_SynHyps_2344 = None
        KL_LOC_Result_2345 = None
        KL_LOC_V2382_2346 = None
        KL_LOC_A2369_2347 = None
        KL_LOC_V2383_2348 = None
        KL_LOC_SynHyps_2349 = None
        KL_LOC_Result_2350 = None
        KL_LOC_SynHyps_2351 = None
        KL_LOC_A2369_2352 = None
        KL_LOC_Result_2353 = None
        KL_LOC_SynHyps_2354 = None
        KL_LOC_A2369_2355 = None
        KL_LOC_Result_2356 = None
        KL_LOC_SynHyps_2357 = None
        KL_LOC_X_2358 = None
        KL_LOC_A2369_2359 = None
        KL_LOC_Result_2360 = None
        KL_LOC_SynHyps_2361 = None
        KL_LOC_X_2362 = None
        KL_LOC_A2369_2363 = None
        KL_LOC_SynHyps_2364 = None
        KL_LOC_Result_2365 = None
        KL_LOC_V2384_2366 = None
        KL_LOC_Y_2367 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Throwcontrol_2324', tco_apply(shen_catchpoint, [])), tail_call(shen_cutpoint, [KL_CTX.KL_LOC_Throwcontrol_2324, [setattr(KL_CTX, 'KL_LOC_Case_2325', [setattr(KL_CTX, 'KL_LOC_V2374_2326', tco_apply(shen_lazyderef, [KL_ARG_V2985_2318, KL_ARG_V2989_2322])), ([tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_ARG_V2987_2320, KL_ARG_V2986_2319, KL_ARG_V2989_2322, KL_ARG_V2990_2323])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2374_2326) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_2327', [setattr(KL_CTX, 'KL_LOC_V2375_2328', tco_apply(shen_lazyderef, [KL_ARG_V2985_2318, KL_ARG_V2989_2322])), ([setattr(KL_CTX, 'KL_LOC_X2368_2329', KL_CTX.KL_LOC_V2375_2328[0]), [setattr(KL_CTX, 'KL_LOC_Y_2330', KL_CTX.KL_LOC_V2375_2328[1]), [setattr(KL_CTX, 'KL_LOC_V2376_2331', tco_apply(shen_lazyderef, [KL_ARG_V2987_2320, KL_ARG_V2989_2322])), ([setattr(KL_CTX, 'KL_LOC_V2377_2332', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2376_2331[0], KL_ARG_V2989_2322])), ([setattr(KL_CTX, 'KL_LOC_X_2333', KL_CTX.KL_LOC_V2377_2332[0]), [setattr(KL_CTX, 'KL_LOC_V2378_2334', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2377_2332[1], KL_ARG_V2989_2322])), ([setattr(KL_CTX, 'KL_LOC_V2379_2335', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2378_2334[0], KL_ARG_V2989_2322])), ([setattr(KL_CTX, 'KL_LOC_V2380_2336', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2378_2334[1], KL_ARG_V2989_2322])), ([setattr(KL_CTX, 'KL_LOC_A2369_2337', KL_CTX.KL_LOC_V2380_2336[0]), [setattr(KL_CTX, 'KL_LOC_V2381_2338', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2380_2336[1], KL_ARG_V2989_2322])), ([setattr(KL_CTX, 'KL_LOC_SynHyps_2339', KL_CTX.KL_LOC_V2376_2331[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_ARG_V2988_2321, KL_CTX.KL_LOC_A2369_2337, KL_ARG_V2989_2322, (lambda : tail_call(kl_unifyx33, [KL_CTX.KL_LOC_X_2333, KL_CTX.KL_LOC_X2368_2329, KL_ARG_V2989_2322, (lambda : tail_call(kl_fwhen, [tco_apply(shen_uex63, [tco_apply(shen_deref, [KL_CTX.KL_LOC_X_2333, KL_ARG_V2989_2322])]), KL_ARG_V2989_2322, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2324, KL_ARG_V2989_2322, (lambda : tail_call(shen_syntaxx45hyps, [KL_CTX.KL_LOC_Y_2330, KL_ARG_V2986_2319, KL_CTX.KL_LOC_SynHyps_2339, KL_ARG_V2988_2321, KL_ARG_V2989_2322, KL_ARG_V2990_2323]))]))]))]))])][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2381_2338) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2381_2338, [], KL_ARG_V2989_2322]), [setattr(KL_CTX, 'KL_LOC_Result_2340', [setattr(KL_CTX, 'KL_LOC_SynHyps_2341', KL_CTX.KL_LOC_V2376_2331[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_ARG_V2988_2321, KL_CTX.KL_LOC_A2369_2337, KL_ARG_V2989_2322, (lambda : tail_call(kl_unifyx33, [KL_CTX.KL_LOC_X_2333, KL_CTX.KL_LOC_X2368_2329, KL_ARG_V2989_2322, (lambda : tail_call(kl_fwhen, [tco_apply(shen_uex63, [tco_apply(shen_deref, [KL_CTX.KL_LOC_X_2333, KL_ARG_V2989_2322])]), KL_ARG_V2989_2322, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2324, KL_ARG_V2989_2322, (lambda : tail_call(shen_syntaxx45hyps, [KL_CTX.KL_LOC_Y_2330, KL_ARG_V2986_2319, KL_CTX.KL_LOC_SynHyps_2341, KL_ARG_V2988_2321, KL_ARG_V2989_2322, KL_ARG_V2990_2323]))]))]))]))])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2381_2338, KL_ARG_V2989_2322]), KL_CTX.KL_LOC_Result_2340][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2381_2338]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2380_2336) else ([setattr(KL_CTX, 'KL_LOC_A2369_2342', tco_apply(shen_newpv, [KL_ARG_V2989_2322])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2380_2336, [KL_CTX.KL_LOC_A2369_2342, []], KL_ARG_V2989_2322]), [setattr(KL_CTX, 'KL_LOC_Result_2343', [setattr(KL_CTX, 'KL_LOC_SynHyps_2344', KL_CTX.KL_LOC_V2376_2331[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_ARG_V2988_2321, KL_CTX.KL_LOC_A2369_2342, KL_ARG_V2989_2322, (lambda : tail_call(kl_unifyx33, [KL_CTX.KL_LOC_X_2333, KL_CTX.KL_LOC_X2368_2329, KL_ARG_V2989_2322, (lambda : tail_call(kl_fwhen, [tco_apply(shen_uex63, [tco_apply(shen_deref, [KL_CTX.KL_LOC_X_2333, KL_ARG_V2989_2322])]), KL_ARG_V2989_2322, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2324, KL_ARG_V2989_2322, (lambda : tail_call(shen_syntaxx45hyps, [KL_CTX.KL_LOC_Y_2330, KL_ARG_V2986_2319, KL_CTX.KL_LOC_SynHyps_2344, KL_ARG_V2988_2321, KL_ARG_V2989_2322, KL_ARG_V2990_2323]))]))]))]))])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2380_2336, KL_ARG_V2989_2322]), KL_CTX.KL_LOC_Result_2343][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2380_2336]) else False))][(-1)] if shen_eq(symdic.symdic_kl_x58, KL_CTX.KL_LOC_V2379_2335) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2379_2335, symdic.symdic_kl_x58, KL_ARG_V2989_2322]), [setattr(KL_CTX, 'KL_LOC_Result_2345', [setattr(KL_CTX, 'KL_LOC_V2382_2346', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2378_2334[1], KL_ARG_V2989_2322])), ([setattr(KL_CTX, 'KL_LOC_A2369_2347', KL_CTX.KL_LOC_V2382_2346[0]), [setattr(KL_CTX, 'KL_LOC_V2383_2348', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2382_2346[1], KL_ARG_V2989_2322])), ([setattr(KL_CTX, 'KL_LOC_SynHyps_2349', KL_CTX.KL_LOC_V2376_2331[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_ARG_V2988_2321, KL_CTX.KL_LOC_A2369_2347, KL_ARG_V2989_2322, (lambda : tail_call(kl_unifyx33, [KL_CTX.KL_LOC_X_2333, KL_CTX.KL_LOC_X2368_2329, KL_ARG_V2989_2322, (lambda : tail_call(kl_fwhen, [tco_apply(shen_uex63, [tco_apply(shen_deref, [KL_CTX.KL_LOC_X_2333, KL_ARG_V2989_2322])]), KL_ARG_V2989_2322, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2324, KL_ARG_V2989_2322, (lambda : tail_call(shen_syntaxx45hyps, [KL_CTX.KL_LOC_Y_2330, KL_ARG_V2986_2319, KL_CTX.KL_LOC_SynHyps_2349, KL_ARG_V2988_2321, KL_ARG_V2989_2322, KL_ARG_V2990_2323]))]))]))]))])][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2383_2348) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2383_2348, [], KL_ARG_V2989_2322]), [setattr(KL_CTX, 'KL_LOC_Result_2350', [setattr(KL_CTX, 'KL_LOC_SynHyps_2351', KL_CTX.KL_LOC_V2376_2331[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_ARG_V2988_2321, KL_CTX.KL_LOC_A2369_2347, KL_ARG_V2989_2322, (lambda : tail_call(kl_unifyx33, [KL_CTX.KL_LOC_X_2333, KL_CTX.KL_LOC_X2368_2329, KL_ARG_V2989_2322, (lambda : tail_call(kl_fwhen, [tco_apply(shen_uex63, [tco_apply(shen_deref, [KL_CTX.KL_LOC_X_2333, KL_ARG_V2989_2322])]), KL_ARG_V2989_2322, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2324, KL_ARG_V2989_2322, (lambda : tail_call(shen_syntaxx45hyps, [KL_CTX.KL_LOC_Y_2330, KL_ARG_V2986_2319, KL_CTX.KL_LOC_SynHyps_2351, KL_ARG_V2988_2321, KL_ARG_V2989_2322, KL_ARG_V2990_2323]))]))]))]))])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2383_2348, KL_ARG_V2989_2322]), KL_CTX.KL_LOC_Result_2350][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2383_2348]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2382_2346) else ([setattr(KL_CTX, 'KL_LOC_A2369_2352', tco_apply(shen_newpv, [KL_ARG_V2989_2322])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2382_2346, [KL_CTX.KL_LOC_A2369_2352, []], KL_ARG_V2989_2322]), [setattr(KL_CTX, 'KL_LOC_Result_2353', [setattr(KL_CTX, 'KL_LOC_SynHyps_2354', KL_CTX.KL_LOC_V2376_2331[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_ARG_V2988_2321, KL_CTX.KL_LOC_A2369_2352, KL_ARG_V2989_2322, (lambda : tail_call(kl_unifyx33, [KL_CTX.KL_LOC_X_2333, KL_CTX.KL_LOC_X2368_2329, KL_ARG_V2989_2322, (lambda : tail_call(kl_fwhen, [tco_apply(shen_uex63, [tco_apply(shen_deref, [KL_CTX.KL_LOC_X_2333, KL_ARG_V2989_2322])]), KL_ARG_V2989_2322, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2324, KL_ARG_V2989_2322, (lambda : tail_call(shen_syntaxx45hyps, [KL_CTX.KL_LOC_Y_2330, KL_ARG_V2986_2319, KL_CTX.KL_LOC_SynHyps_2354, KL_ARG_V2988_2321, KL_ARG_V2989_2322, KL_ARG_V2990_2323]))]))]))]))])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2382_2346, KL_ARG_V2989_2322]), KL_CTX.KL_LOC_Result_2353][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2382_2346]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2379_2335, KL_ARG_V2989_2322]), KL_CTX.KL_LOC_Result_2345][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2379_2335]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2378_2334) else ([setattr(KL_CTX, 'KL_LOC_A2369_2355', tco_apply(shen_newpv, [KL_ARG_V2989_2322])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2378_2334, [symdic.symdic_kl_x58, [KL_CTX.KL_LOC_A2369_2355, []]], KL_ARG_V2989_2322]), [setattr(KL_CTX, 'KL_LOC_Result_2356', [setattr(KL_CTX, 'KL_LOC_SynHyps_2357', KL_CTX.KL_LOC_V2376_2331[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_ARG_V2988_2321, KL_CTX.KL_LOC_A2369_2355, KL_ARG_V2989_2322, (lambda : tail_call(kl_unifyx33, [KL_CTX.KL_LOC_X_2333, KL_CTX.KL_LOC_X2368_2329, KL_ARG_V2989_2322, (lambda : tail_call(kl_fwhen, [tco_apply(shen_uex63, [tco_apply(shen_deref, [KL_CTX.KL_LOC_X_2333, KL_ARG_V2989_2322])]), KL_ARG_V2989_2322, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2324, KL_ARG_V2989_2322, (lambda : tail_call(shen_syntaxx45hyps, [KL_CTX.KL_LOC_Y_2330, KL_ARG_V2986_2319, KL_CTX.KL_LOC_SynHyps_2357, KL_ARG_V2988_2321, KL_ARG_V2989_2322, KL_ARG_V2990_2323]))]))]))]))])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2378_2334, KL_ARG_V2989_2322]), KL_CTX.KL_LOC_Result_2356][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2378_2334]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2377_2332) else ([setattr(KL_CTX, 'KL_LOC_X_2358', tco_apply(shen_newpv, [KL_ARG_V2989_2322])), [setattr(KL_CTX, 'KL_LOC_A2369_2359', tco_apply(shen_newpv, [KL_ARG_V2989_2322])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2377_2332, [KL_CTX.KL_LOC_X_2358, [symdic.symdic_kl_x58, [KL_CTX.KL_LOC_A2369_2359, []]]], KL_ARG_V2989_2322]), [setattr(KL_CTX, 'KL_LOC_Result_2360', [setattr(KL_CTX, 'KL_LOC_SynHyps_2361', KL_CTX.KL_LOC_V2376_2331[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_ARG_V2988_2321, KL_CTX.KL_LOC_A2369_2359, KL_ARG_V2989_2322, (lambda : tail_call(kl_unifyx33, [KL_CTX.KL_LOC_X_2358, KL_CTX.KL_LOC_X2368_2329, KL_ARG_V2989_2322, (lambda : tail_call(kl_fwhen, [tco_apply(shen_uex63, [tco_apply(shen_deref, [KL_CTX.KL_LOC_X_2358, KL_ARG_V2989_2322])]), KL_ARG_V2989_2322, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2324, KL_ARG_V2989_2322, (lambda : tail_call(shen_syntaxx45hyps, [KL_CTX.KL_LOC_Y_2330, KL_ARG_V2986_2319, KL_CTX.KL_LOC_SynHyps_2361, KL_ARG_V2988_2321, KL_ARG_V2989_2322, KL_ARG_V2990_2323]))]))]))]))])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2377_2332, KL_ARG_V2989_2322]), KL_CTX.KL_LOC_Result_2360][(-1)]][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2377_2332]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2376_2331) else ([setattr(KL_CTX, 'KL_LOC_X_2362', tco_apply(shen_newpv, [KL_ARG_V2989_2322])), [setattr(KL_CTX, 'KL_LOC_A2369_2363', tco_apply(shen_newpv, [KL_ARG_V2989_2322])), [setattr(KL_CTX, 'KL_LOC_SynHyps_2364', tco_apply(shen_newpv, [KL_ARG_V2989_2322])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2376_2331, [[KL_CTX.KL_LOC_X_2362, [symdic.symdic_kl_x58, [KL_CTX.KL_LOC_A2369_2363, []]]], KL_CTX.KL_LOC_SynHyps_2364], KL_ARG_V2989_2322]), [setattr(KL_CTX, 'KL_LOC_Result_2365', [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_ARG_V2988_2321, KL_CTX.KL_LOC_A2369_2363, KL_ARG_V2989_2322, (lambda : tail_call(kl_unifyx33, [KL_CTX.KL_LOC_X_2362, KL_CTX.KL_LOC_X2368_2329, KL_ARG_V2989_2322, (lambda : tail_call(kl_fwhen, [tco_apply(shen_uex63, [tco_apply(shen_deref, [KL_CTX.KL_LOC_X_2362, KL_ARG_V2989_2322])]), KL_ARG_V2989_2322, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2324, KL_ARG_V2989_2322, (lambda : tail_call(shen_syntaxx45hyps, [KL_CTX.KL_LOC_Y_2330, KL_ARG_V2986_2319, KL_CTX.KL_LOC_SynHyps_2364, KL_ARG_V2988_2321, KL_ARG_V2989_2322, KL_ARG_V2990_2323]))]))]))]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2376_2331, KL_ARG_V2989_2322]), KL_CTX.KL_LOC_Result_2365][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2376_2331]) else False))][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2375_2328) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_V2384_2366', tco_apply(shen_lazyderef, [KL_ARG_V2985_2318, KL_ARG_V2989_2322])), ([setattr(KL_CTX, 'KL_LOC_Y_2367', KL_CTX.KL_LOC_V2384_2366[1]), [tco_apply(shen_incinfs, []), tco_apply(shen_syntaxx45hyps, [KL_CTX.KL_LOC_Y_2367, KL_ARG_V2986_2319, KL_ARG_V2987_2320, KL_ARG_V2988_2321, KL_ARG_V2989_2322, KL_ARG_V2990_2323])][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2384_2366) else False)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2327, False) else KL_CTX.KL_LOC_Case_2327)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2325, False) else KL_CTX.KL_LOC_Case_2325)][(-1)]])][(-1)]
shen_add_fun('shen.syntax-hyps', shen_syntaxx45hyps)

@tail_recursion
def shen_getx45syntaxx43semantics(KL_ARG_V2991_2368, KL_ARG_V2992_2369, KL_ARG_V2993_2370, KL_ARG_V2994_2371, KL_ARG_V2995_2372):

    class KL_Context:
        KL_LOC_Throwcontrol_2373 = None
        KL_LOC_Case_2374 = None
        KL_LOC_V2340_2375 = None
        KL_LOC_V2341_2376 = None
        KL_LOC_V2342_2377 = None
        KL_LOC_V2343_2378 = None
        KL_LOC_Semantics_2379 = None
        KL_LOC_V2344_2380 = None
        KL_LOC_Result_2381 = None
        KL_LOC_V2345_2382 = None
        KL_LOC_V2346_2383 = None
        KL_LOC_V2347_2384 = None
        KL_LOC_Semantics_2385 = None
        KL_LOC_V2348_2386 = None
        KL_LOC_Case_2387 = None
        KL_LOC_V2349_2388 = None
        KL_LOC_V2350_2389 = None
        KL_LOC_V2351_2390 = None
        KL_LOC_V2352_2391 = None
        KL_LOC_Semantics_2392 = None
        KL_LOC_V2353_2393 = None
        KL_LOC_V2354_2394 = None
        KL_LOC_V2355_2395 = None
        KL_LOC_G_2396 = None
        KL_LOC_V2356_2397 = None
        KL_LOC_Result_2398 = None
        KL_LOC_V2357_2399 = None
        KL_LOC_V2358_2400 = None
        KL_LOC_V2359_2401 = None
        KL_LOC_Semantics_2402 = None
        KL_LOC_V2360_2403 = None
        KL_LOC_V2361_2404 = None
        KL_LOC_V2362_2405 = None
        KL_LOC_G_2406 = None
        KL_LOC_V2363_2407 = None
        KL_LOC_V2364_2408 = None
        KL_LOC_X2336_2409 = None
        KL_LOC_Syntax_2410 = None
        KL_LOC_V2365_2411 = None
        KL_LOC_X_2412 = None
        KL_LOC_Rule_2413 = None
        KL_LOC_X2336_2414 = None
        KL_LOC_Syntax_2415 = None
        KL_LOC_Result_2416 = None
        KL_LOC_V2366_2417 = None
        KL_LOC_X_2418 = None
        KL_LOC_Rule_2419 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Throwcontrol_2373', tco_apply(shen_catchpoint, [])), tail_call(shen_cutpoint, [KL_CTX.KL_LOC_Throwcontrol_2373, [setattr(KL_CTX, 'KL_LOC_Case_2374', [setattr(KL_CTX, 'KL_LOC_V2340_2375', tco_apply(shen_lazyderef, [KL_ARG_V2991_2368, KL_ARG_V2994_2371])), ([setattr(KL_CTX, 'KL_LOC_V2341_2376', tco_apply(shen_lazyderef, [KL_ARG_V2993_2370, KL_ARG_V2994_2371])), ([setattr(KL_CTX, 'KL_LOC_V2342_2377', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2341_2376[0], KL_ARG_V2994_2371])), ([setattr(KL_CTX, 'KL_LOC_V2343_2378', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2341_2376[1], KL_ARG_V2994_2371])), ([setattr(KL_CTX, 'KL_LOC_Semantics_2379', KL_CTX.KL_LOC_V2343_2378[0]), [setattr(KL_CTX, 'KL_LOC_V2344_2380', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2343_2378[1], KL_ARG_V2994_2371])), ([tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2373, KL_ARG_V2994_2371, (lambda : tail_call(kl_bind, [KL_ARG_V2992_2369, tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Semantics_2379, KL_ARG_V2994_2371]), KL_ARG_V2994_2371, KL_ARG_V2995_2372]))])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2344_2380) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2343_2378) else False)][(-1)] if shen_eq(symdic.symdic_kl_x58x61, KL_CTX.KL_LOC_V2342_2377) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2341_2376) else False)][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2340_2375) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2340_2375, [], KL_ARG_V2994_2371]), [setattr(KL_CTX, 'KL_LOC_Result_2381', [setattr(KL_CTX, 'KL_LOC_V2345_2382', tco_apply(shen_lazyderef, [KL_ARG_V2993_2370, KL_ARG_V2994_2371])), ([setattr(KL_CTX, 'KL_LOC_V2346_2383', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2345_2382[0], KL_ARG_V2994_2371])), ([setattr(KL_CTX, 'KL_LOC_V2347_2384', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2345_2382[1], KL_ARG_V2994_2371])), ([setattr(KL_CTX, 'KL_LOC_Semantics_2385', KL_CTX.KL_LOC_V2347_2384[0]), [setattr(KL_CTX, 'KL_LOC_V2348_2386', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2347_2384[1], KL_ARG_V2994_2371])), ([tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2373, KL_ARG_V2994_2371, (lambda : tail_call(kl_bind, [KL_ARG_V2992_2369, tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Semantics_2385, KL_ARG_V2994_2371]), KL_ARG_V2994_2371, KL_ARG_V2995_2372]))])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2348_2386) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2347_2384) else False)][(-1)] if shen_eq(symdic.symdic_kl_x58x61, KL_CTX.KL_LOC_V2346_2383) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2345_2382) else False)][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2340_2375, KL_ARG_V2994_2371]), KL_CTX.KL_LOC_Result_2381][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2340_2375]) else False))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_2387', [setattr(KL_CTX, 'KL_LOC_V2349_2388', tco_apply(shen_lazyderef, [KL_ARG_V2991_2368, KL_ARG_V2994_2371])), ([setattr(KL_CTX, 'KL_LOC_V2350_2389', tco_apply(shen_lazyderef, [KL_ARG_V2993_2370, KL_ARG_V2994_2371])), ([setattr(KL_CTX, 'KL_LOC_V2351_2390', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2350_2389[0], KL_ARG_V2994_2371])), ([setattr(KL_CTX, 'KL_LOC_V2352_2391', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2350_2389[1], KL_ARG_V2994_2371])), ([setattr(KL_CTX, 'KL_LOC_Semantics_2392', KL_CTX.KL_LOC_V2352_2391[0]), [setattr(KL_CTX, 'KL_LOC_V2353_2393', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2352_2391[1], KL_ARG_V2994_2371])), ([setattr(KL_CTX, 'KL_LOC_V2354_2394', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2353_2393[0], KL_ARG_V2994_2371])), ([setattr(KL_CTX, 'KL_LOC_V2355_2395', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2353_2393[1], KL_ARG_V2994_2371])), ([setattr(KL_CTX, 'KL_LOC_G_2396', KL_CTX.KL_LOC_V2355_2395[0]), [setattr(KL_CTX, 'KL_LOC_V2356_2397', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2355_2395[1], KL_ARG_V2994_2371])), ([tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2373, KL_ARG_V2994_2371, (lambda : tail_call(kl_bind, [KL_ARG_V2992_2369, [symdic.symdic_kl_where, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_G_2396, KL_ARG_V2994_2371]), [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Semantics_2392, KL_ARG_V2994_2371]), []]]], KL_ARG_V2994_2371, KL_ARG_V2995_2372]))])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2356_2397) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2355_2395) else False)][(-1)] if shen_eq(symdic.symdic_kl_where, KL_CTX.KL_LOC_V2354_2394) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2353_2393) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2352_2391) else False)][(-1)] if shen_eq(symdic.symdic_kl_x58x61, KL_CTX.KL_LOC_V2351_2390) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2350_2389) else False)][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2349_2388) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2349_2388, [], KL_ARG_V2994_2371]), [setattr(KL_CTX, 'KL_LOC_Result_2398', [setattr(KL_CTX, 'KL_LOC_V2357_2399', tco_apply(shen_lazyderef, [KL_ARG_V2993_2370, KL_ARG_V2994_2371])), ([setattr(KL_CTX, 'KL_LOC_V2358_2400', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2357_2399[0], KL_ARG_V2994_2371])), ([setattr(KL_CTX, 'KL_LOC_V2359_2401', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2357_2399[1], KL_ARG_V2994_2371])), ([setattr(KL_CTX, 'KL_LOC_Semantics_2402', KL_CTX.KL_LOC_V2359_2401[0]), [setattr(KL_CTX, 'KL_LOC_V2360_2403', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2359_2401[1], KL_ARG_V2994_2371])), ([setattr(KL_CTX, 'KL_LOC_V2361_2404', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2360_2403[0], KL_ARG_V2994_2371])), ([setattr(KL_CTX, 'KL_LOC_V2362_2405', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2360_2403[1], KL_ARG_V2994_2371])), ([setattr(KL_CTX, 'KL_LOC_G_2406', KL_CTX.KL_LOC_V2362_2405[0]), [setattr(KL_CTX, 'KL_LOC_V2363_2407', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2362_2405[1], KL_ARG_V2994_2371])), ([tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2373, KL_ARG_V2994_2371, (lambda : tail_call(kl_bind, [KL_ARG_V2992_2369, [symdic.symdic_kl_where, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_G_2406, KL_ARG_V2994_2371]), [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Semantics_2402, KL_ARG_V2994_2371]), []]]], KL_ARG_V2994_2371, KL_ARG_V2995_2372]))])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2363_2407) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2362_2405) else False)][(-1)] if shen_eq(symdic.symdic_kl_where, KL_CTX.KL_LOC_V2361_2404) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2360_2403) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2359_2401) else False)][(-1)] if shen_eq(symdic.symdic_kl_x58x61, KL_CTX.KL_LOC_V2358_2400) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2357_2399) else False)][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2349_2388, KL_ARG_V2994_2371]), KL_CTX.KL_LOC_Result_2398][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2349_2388]) else False))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_V2364_2408', tco_apply(shen_lazyderef, [KL_ARG_V2991_2368, KL_ARG_V2994_2371])), ([setattr(KL_CTX, 'KL_LOC_X2336_2409', KL_CTX.KL_LOC_V2364_2408[0]), [setattr(KL_CTX, 'KL_LOC_Syntax_2410', KL_CTX.KL_LOC_V2364_2408[1]), [setattr(KL_CTX, 'KL_LOC_V2365_2411', tco_apply(shen_lazyderef, [KL_ARG_V2993_2370, KL_ARG_V2994_2371])), ([setattr(KL_CTX, 'KL_LOC_X_2412', KL_CTX.KL_LOC_V2365_2411[0]), [setattr(KL_CTX, 'KL_LOC_Rule_2413', KL_CTX.KL_LOC_V2365_2411[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_X_2412, KL_CTX.KL_LOC_X2336_2409, KL_ARG_V2994_2371, (lambda : tail_call(shen_getx45syntaxx43semantics, [KL_CTX.KL_LOC_Syntax_2410, KL_ARG_V2992_2369, KL_CTX.KL_LOC_Rule_2413, KL_ARG_V2994_2371, KL_ARG_V2995_2372]))])][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2365_2411) else False)][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2364_2408) else ([setattr(KL_CTX, 'KL_LOC_X2336_2414', tco_apply(shen_newpv, [KL_ARG_V2994_2371])), [setattr(KL_CTX, 'KL_LOC_Syntax_2415', tco_apply(shen_newpv, [KL_ARG_V2994_2371])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2364_2408, [KL_CTX.KL_LOC_X2336_2414, KL_CTX.KL_LOC_Syntax_2415], KL_ARG_V2994_2371]), [setattr(KL_CTX, 'KL_LOC_Result_2416', [setattr(KL_CTX, 'KL_LOC_V2366_2417', tco_apply(shen_lazyderef, [KL_ARG_V2993_2370, KL_ARG_V2994_2371])), ([setattr(KL_CTX, 'KL_LOC_X_2418', KL_CTX.KL_LOC_V2366_2417[0]), [setattr(KL_CTX, 'KL_LOC_Rule_2419', KL_CTX.KL_LOC_V2366_2417[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_X_2418, KL_CTX.KL_LOC_X2336_2414, KL_ARG_V2994_2371, (lambda : tail_call(shen_getx45syntaxx43semantics, [KL_CTX.KL_LOC_Syntax_2415, KL_ARG_V2992_2369, KL_CTX.KL_LOC_Rule_2419, KL_ARG_V2994_2371, KL_ARG_V2995_2372]))])][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2366_2417) else False)][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2364_2408, KL_ARG_V2994_2371]), KL_CTX.KL_LOC_Result_2416][(-1)]][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2364_2408]) else False))][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2387, False) else KL_CTX.KL_LOC_Case_2387)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2374, False) else KL_CTX.KL_LOC_Case_2374)][(-1)]])][(-1)]
shen_add_fun('shen.get-syntax+semantics', shen_getx45syntaxx43semantics)

@tail_recursion
def shen_syntaxx45check(KL_ARG_V2996_2420, KL_ARG_V2997_2421, KL_ARG_V2998_2422, KL_ARG_V2999_2423, KL_ARG_V3000_2424):

    class KL_Context:
        KL_LOC_Throwcontrol_2425 = None
        KL_LOC_Case_2426 = None
        KL_LOC_V2333_2427 = None
        KL_LOC_Case_2428 = None
        KL_LOC_V2334_2429 = None
        KL_LOC_X_2430 = None
        KL_LOC_Syntax_2431 = None
        KL_LOC_C_2432 = None
        KL_LOC_Xx38x38_2433 = None
        KL_LOC_B_2434 = None
        KL_LOC_V2335_2435 = None
        KL_LOC_X_2436 = None
        KL_LOC_Syntax_2437 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Throwcontrol_2425', tco_apply(shen_catchpoint, [])), tail_call(shen_cutpoint, [KL_CTX.KL_LOC_Throwcontrol_2425, [setattr(KL_CTX, 'KL_LOC_Case_2426', [setattr(KL_CTX, 'KL_LOC_V2333_2427', tco_apply(shen_lazyderef, [KL_ARG_V2996_2420, KL_ARG_V2999_2423])), ([tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V3000_2424])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2333_2427) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_2428', [setattr(KL_CTX, 'KL_LOC_V2334_2429', tco_apply(shen_lazyderef, [KL_ARG_V2996_2420, KL_ARG_V2999_2423])), ([setattr(KL_CTX, 'KL_LOC_X_2430', KL_CTX.KL_LOC_V2334_2429[0]), [setattr(KL_CTX, 'KL_LOC_Syntax_2431', KL_CTX.KL_LOC_V2334_2429[1]), [setattr(KL_CTX, 'KL_LOC_C_2432', tco_apply(shen_newpv, [KL_ARG_V2999_2423])), [setattr(KL_CTX, 'KL_LOC_Xx38x38_2433', tco_apply(shen_newpv, [KL_ARG_V2999_2423])), [setattr(KL_CTX, 'KL_LOC_B_2434', tco_apply(shen_newpv, [KL_ARG_V2999_2423])), [tco_apply(shen_incinfs, []), tco_apply(kl_fwhen, [tco_apply(shen_grammar_symbolx63, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_2430, KL_ARG_V2999_2423])]), KL_ARG_V2999_2423, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2425, KL_ARG_V2999_2423, (lambda : tail_call(shen_tx42, [[KL_CTX.KL_LOC_X_2430, [symdic.symdic_kl_x58, [[[symdic.symdic_kl_list, [KL_CTX.KL_LOC_B_2434, []]], [symdic.symdic_kl_x61x61x62, [KL_CTX.KL_LOC_C_2432, []]]], []]]], KL_ARG_V2998_2422, KL_ARG_V2999_2423, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2425, KL_ARG_V2999_2423, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Xx38x38_2433, tco_apply(kl_concat, [symdic.symdic_kl_x38x38, tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_2430, KL_ARG_V2999_2423])]), KL_ARG_V2999_2423, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2425, KL_ARG_V2999_2423, (lambda : tail_call(shen_tx42, [[KL_CTX.KL_LOC_Xx38x38_2433, [symdic.symdic_kl_x58, [[symdic.symdic_kl_list, [KL_ARG_V2997_2421, []]], []]]], [[KL_CTX.KL_LOC_Xx38x38_2433, [symdic.symdic_kl_x58, [[symdic.symdic_kl_list, [KL_CTX.KL_LOC_B_2434, []]], []]]], KL_ARG_V2998_2422], KL_ARG_V2999_2423, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2425, KL_ARG_V2999_2423, (lambda : tail_call(shen_syntaxx45check, [KL_CTX.KL_LOC_Syntax_2431, KL_ARG_V2997_2421, KL_ARG_V2998_2422, KL_ARG_V2999_2423, KL_ARG_V3000_2424]))]))]))]))]))]))]))]))])][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2334_2429) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_V2335_2435', tco_apply(shen_lazyderef, [KL_ARG_V2996_2420, KL_ARG_V2999_2423])), ([setattr(KL_CTX, 'KL_LOC_X_2436', KL_CTX.KL_LOC_V2335_2435[0]), [setattr(KL_CTX, 'KL_LOC_Syntax_2437', KL_CTX.KL_LOC_V2335_2435[1]), [tco_apply(shen_incinfs, []), tco_apply(shen_tx42, [[KL_CTX.KL_LOC_X_2436, [symdic.symdic_kl_x58, [KL_ARG_V2997_2421, []]]], KL_ARG_V2998_2422, KL_ARG_V2999_2423, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2425, KL_ARG_V2999_2423, (lambda : tail_call(shen_syntaxx45check, [KL_CTX.KL_LOC_Syntax_2437, KL_ARG_V2997_2421, KL_ARG_V2998_2422, KL_ARG_V2999_2423, KL_ARG_V3000_2424]))]))])][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2335_2435) else False)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2428, False) else KL_CTX.KL_LOC_Case_2428)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2426, False) else KL_CTX.KL_LOC_Case_2426)][(-1)]])][(-1)]
shen_add_fun('shen.syntax-check', shen_syntaxx45check)

@tail_recursion
def shen_semanticsx45check(KL_ARG_V3001_2438, KL_ARG_V3002_2439, KL_ARG_V3003_2440, KL_ARG_V3004_2441, KL_ARG_V3005_2442):

    class KL_Context:
        KL_LOC_Semanticsx42_2443 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Semanticsx42_2443', tco_apply(shen_newpv, [KL_ARG_V3004_2441])), [tco_apply(shen_incinfs, []), tail_call(kl_bind, [KL_CTX.KL_LOC_Semanticsx42_2443, tco_apply(shen_curry, [tco_apply(shen_renamex45semantics, [tco_apply(shen_deref, [KL_ARG_V3001_2438, KL_ARG_V3004_2441])])]), KL_ARG_V3004_2441, (lambda : tail_call(shen_tx42, [[KL_CTX.KL_LOC_Semanticsx42_2443, [symdic.symdic_kl_x58, [KL_ARG_V3002_2439, []]]], KL_ARG_V3003_2440, KL_ARG_V3004_2441, KL_ARG_V3005_2442]))])][(-1)]][(-1)]
shen_add_fun('shen.semantics-check', shen_semanticsx45check)

@tail_recursion
def shen_renamex45semantics(KL_ARG_V3006_2444):
    global symdic
    return ([tco_apply(shen_renamex45semantics, [KL_ARG_V3006_2444[0]]), tco_apply(shen_renamex45semantics, [KL_ARG_V3006_2444[1]])] if shen_consp(KL_ARG_V3006_2444) else ([symdic.symdic_shen_x60x45sem, [KL_ARG_V3006_2444, []]] if tco_apply(shen_grammar_symbolx63, [KL_ARG_V3006_2444]) else (KL_ARG_V3006_2444 if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.rename-semantics', shen_renamex45semantics)
shen_initialise_arity_table(shen_to_cons([Sym('absvector'), 1, Sym('adjoin'), 2, Sym('and'), 2, Sym('append'), 2, Sym('arity'), 1, Sym('assoc'), 2, Sym('boolean?'), 1, Sym('cd'), 1, Sym('compile'), 3, Sym('concat'), 2, Sym('cons'), 2, Sym('cons?'), 1, Sym('cn'), 2, Sym('declare'), 2, Sym('destroy'), 1, Sym('difference'), 2, Sym('do'), 2, Sym('element?'), 2, Sym('empty?'), 1, Sym('enable-type-theory'), 1, Sym('interror'), 2, Sym('eval'), 1, Sym('eval-kl'), 1, Sym('explode'), 1, Sym('external'), 1, Sym('fail-if'), 2, Sym('fail'), 0, Sym('fix'), 2, Sym('findall'), 5, Sym('freeze'), 1, Sym('fst'), 1, Sym('gensym'), 1, Sym('get'), 3, Sym('get-time'), 1, Sym('address->'), 3, Sym('<-address'), 2, Sym('<-vector'), 2, Sym('>'), 2, Sym('>='), 2, Sym('='), 2, Sym('hd'), 1, Sym('hdv'), 1, Sym('hdstr'), 1, Sym('head'), 1, Sym('if'), 3, Sym('integer?'), 1, Sym('identical'), 4, Sym('inferences'), 0, Sym('intersection'), 2, Sym('length'), 1, Sym('lineread'), 0, Sym('load'), 1, Sym('<'), 2, Sym('<='), 2, Sym('vector'), 1, Sym('macroexpand'), 1, Sym('map'), 2, Sym('mapcan'), 2, Sym('maxinferences'), 1, Sym('not'), 1, Sym('nth'), 2, Sym('n->string'), 1, Sym('number?'), 1, Sym('occurs-check'), 1, Sym('occurrences'), 2, Sym('occurs-check'), 1, Sym('or'), 2, Sym('package'), 3, Sym('pos'), 2, Sym('print'), 1, Sym('profile'), 1, Sym('profile-results'), 0, Sym('pr'), 2, Sym('ps'), 1, Sym('preclude'), 1, Sym('preclude-all-but'), 1, Sym('protect'), 1, Sym('address->'), 3, Sym('put'), 4, Sym('shen.reassemble'), 2, Sym('read-file-as-string'), 1, Sym('read-file'), 1, Sym('read-byte'), 1, Sym('read-from-string'), 1, Sym('remove'), 2, Sym('reverse'), 1, Sym('set'), 2, Sym('simple-error'), 1, Sym('snd'), 1, Sym('specialise'), 1, Sym('spy'), 1, Sym('step'), 1, Sym('stinput'), 0, Sym('stoutput'), 0, Sym('string->n'), 1, Sym('string->symbol'), 1, Sym('string?'), 1, Sym('shen.strong-warning'), 1, Sym('subst'), 3, Sym('shen.sum'), 1, Sym('symbol?'), 1, Sym('tail'), 1, Sym('tl'), 1, Sym('tc'), 1, Sym('tc?'), 1, Sym('thaw'), 1, Sym('track'), 1, Sym('trap-error'), 2, Sym('tuple?'), 1, Sym('type'), 1, Sym('return'), 3, Sym('undefmacro'), 1, Sym('unprofile'), 1, Sym('unify'), 4, Sym('unify!'), 4, Sym('union'), 2, Sym('untrack'), 1, Sym('unspecialise'), 1, Sym('undefmacro'), 1, Sym('vector'), 1, Sym('vector->'), 3, Sym('value'), 1, Sym('variable?'), 1, Sym('version'), 1, Sym('warn'), 1, Sym('write-to-file'), 2, Sym('y-or-n?'), 1, Sym('+'), 2, Sym('*'), 2, Sym('/'), 2, Sym('-'), 2, Sym('=='), 2, Sym('shen.<1>'), 1, Sym('<e>'), 1, Sym('@p'), 2, Sym('@v'), 2, Sym('@s'), 2, Sym('preclude'), 1, Sym('include'), 1, Sym('preclude-all-but'), 1, Sym('include-all-but'), 1, Sym('where'), 2]))
kl_put(shen_intern('shen'), Sym('shen.external-symbols'), shen_to_cons([Sym('!'), Sym('}'), Sym('{'), Sym('-->'), Sym('<--'), Sym('&&'), Sym(':'), Sym(';'), Sym(':-'), Sym(':='), Sym('_'), Sym('*language*'), Sym('*implementation*'), Sym('*stinput*'), Sym('*home-directory*'), Sym('*version*'), Sym('*maximum-print-sequence-size*'), Sym('*macros*'), Sym('*os*'), Sym('*release*'), Sym('*property-vector*'), Sym('@v'), Sym('@p'), Sym('@s'), Sym('*port*'), Sym('*porters*'), Sym('<-'), Sym('->'), Sym('<e>'), Sym('=='), Sym('='), Sym('>='), Sym('>'), Sym('/.'), Sym('=!'), Sym('$'), Sym('-'), Sym('/'), Sym('*'), Sym('+'), Sym('<='), Sym('<'), Sym('>>'), tco_apply(kl_vector, [0]), Sym('==>'), Sym('y-or-n?'), Sym('write-to-file'), Sym('where'), Sym('when'), Sym('warn'), Sym('version'), Sym('verified'), Sym('variable?'), Sym('value'), Sym('vector->'), Sym('<-vector'), Sym('vector'), Sym('vector?'), Sym('unspecialise'), Sym('untrack'), Sym('unit'), Sym('shen.unix'), Sym('union'), Sym('unify'), Sym('unify!'), Sym('unprofile'), Sym('undefmacro'), Sym('return'), Sym('type'), Sym('tuple?'), Sym('true'), Sym('trap-error'), Sym('track'), Sym('time'), Sym('thaw'), Sym('tc?'), Sym('tc'), Sym('tl'), Sym('tlstr'), Sym('tlv'), Sym('tail'), Sym('systemf'), Sym('synonyms'), Sym('symbol'), Sym('symbol?'), Sym('string->symbol'), Sym('subst'), Sym('string?'), Sym('string->n'), Sym('stream'), Sym('string'), Sym('stinput'), Sym('stoutput'), Sym('step'), Sym('spy'), Sym('specialise'), Sym('snd'), Sym('simple-error'), Sym('set'), Sym('save'), Sym('str'), Sym('run'), Sym('reverse'), Sym('remove'), Sym('read'), Sym('read-file'), Sym('read-file-as-bytelist'), Sym('read-file-as-string'), Sym('read-byte'), Sym('read-from-string'), Sym('quit'), Sym('put'), Sym('preclude'), Sym('preclude-all-but'), Sym('ps'), Sym('prolog?'), Sym('protect'), Sym('profile-results'), Sym('profile'), Sym('print'), Sym('pr'), Sym('pos'), Sym('package'), Sym('output'), Sym('out'), Sym('or'), Sym('open'), Sym('occurrences'), Sym('occurs-check'), Sym('n->string'), Sym('number?'), Sym('number'), Sym('null'), Sym('nth'), Sym('not'), Sym('nl'), Sym('mode'), Sym('macro'), Sym('macroexpand'), Sym('maxinferences'), Sym('mapcan'), Sym('map'), Sym('make-string'), Sym('load'), Sym('loaded'), Sym('list'), Sym('lineread'), Sym('limit'), Sym('length'), Sym('let'), Sym('lazy'), Sym('lambda'), Sym('is'), Sym('intersection'), Sym('inferences'), Sym('intern'), Sym('integer?'), Sym('input'), Sym('input+'), Sym('include'), Sym('include-all-but'), Sym('in'), Sym('if'), Sym('identical'), Sym('head'), Sym('hd'), Sym('hdv'), Sym('hdstr'), Sym('hash'), Sym('get'), Sym('get-time'), Sym('gensym'), Sym('function'), Sym('fst'), Sym('freeze'), Sym('fix'), Sym('file'), Sym('fail'), Sym('fail-if'), Sym('fwhen'), Sym('findall'), Sym('false'), Sym('enable-type-theory'), Sym('explode'), Sym('external'), Sym('exception'), Sym('eval-kl'), Sym('eval'), Sym('error-to-string'), Sym('error'), Sym('empty?'), Sym('element?'), Sym('do'), Sym('difference'), Sym('destroy'), Sym('defun'), Sym('define'), Sym('defmacro'), Sym('defcc'), Sym('defprolog'), Sym('declare'), Sym('datatype'), Sym('cut'), Sym('cn'), Sym('cons?'), Sym('cons'), Sym('cond'), Sym('concat'), Sym('compile'), Sym('cd'), Sym('cases'), Sym('call'), Sym('close'), Sym('bind'), Sym('bound?'), Sym('boolean?'), Sym('boolean'), Sym('bar!'), Sym('assoc'), Sym('arity'), Sym('append'), Sym('and'), Sym('adjoin'), Sym('<-address'), Sym('address->'), Sym('absvector?'), Sym('absvector'), Sym('abort')]), shen_get(Sym('*property-vector*')))
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
apply(kl_declare, [symdic.symdic_kl_tcx63, [symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_boolean, []]]]])
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

def shen_expt(KL_ARG_V1518_757, KL_ARG_V1519_758):
    KL_ARG_V1518_757, KL_ARG_V1519_758 = float(KL_ARG_V1518_757), float(KL_ARG_V1519_758)
    return (1 if (0 == KL_ARG_V1519_758) else ((KL_ARG_V1518_757 * tco_apply(shen_expt, [KL_ARG_V1518_757, (KL_ARG_V1519_758 - 1)])) if (KL_ARG_V1519_758 > 0) else ((1 * (tco_apply(shen_expt, [KL_ARG_V1518_757, (KL_ARG_V1519_758 + 1)]) / KL_ARG_V1518_757)) if True else shen_simple_error('condition failure'))))

def kl_booleanx63(KL_ARG_V1857_1068):
    if isinstance(KL_ARG_V1857_1068, Sym) and (KL_ARG_V1857_1068.sym == "true" or KL_ARG_V1857_1068.sym == "false"):
        return True
    else:
        return (True if (True == KL_ARG_V1857_1068) else (True if (False == KL_ARG_V1857_1068) else (False if True else shen_simple_error('condition failure'))))
