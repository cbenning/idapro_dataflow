import idaapi

hotkey_str = "Alt-r"

def go():
        print GetDisasm(ScreenEA())

try:
        del_idc_hotkey(hotkey_str)
except:
        pass

# IDA binds hotkeys to IDC functions so a trampoline IDC function must be created
CompileLine('static sobpy_key() { RunPythonStatement("go()"); }')

# Add the hotkey
add_idc_hotkey(hotkey_str, 'sobpy_key')




   #  ua_ana0(get_screen_ea());
   #AnalyseArea((), eEA)
   #  if (get_nb_op())
#    num = getOpNum();
#    if ( !(cmd.Operands[0].showed()) )
#    op = new df_op_t(num);
#    op->normalize();
#    basic_ana::set_option(ANA_OPTIONS);
#    global_ana::set_depth_limit(DEPTH_MIN,DEPTH_MAX);
#    global_ana::add_limits(area_t(EA_MIN,EA_MAX));
#    gti = global_ana::global_trace(get_screen_ea(),op,TRACE_BACKWARD);
#    gti = global_ana::global_trace(get_screen_ea(),op,TRACE_FORWARD);

