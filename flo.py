from idaapi import *

hotkey_str = "Alt-r"
default_operand = 0

def go():
        print "GO"
        sEA = ScreenEA()
        operand = GetOpnd(sEA,default_operand)
        operand_val = GetOperandValue(sEA,default_operand)
        print "Operand: "+str(operand)
        if operand_val:
            print "Value: "+str(operand_val)

def go_callback(*args):
        go()
        return 1

# IDA binds hotkeys to IDC functions so a trampoline IDC function must be created
idaapi.CompileLine('static flopy_key() { RunPythonStatement("go()"); }')
add_idc_hotkey(hotkey_str, 'flopy_key')

# Add menu item
try:
    if ctx:
        idaapi.del_menu_item(ctx)
except:
    pass

ctx = idaapi.add_menu_item("Search/", "Go", "", 0, go_callback, tuple("hello world"))
if ctx is None:
    print "Failed to add menu!"
    del ctx
else:
    print "Menu added successfully!"


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

