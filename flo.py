import idaapi
import sys

hotkey_str = "Alt-s"
hotkey_str2 = "Alt-g"
default_operand = 0
comment_dict = dict()


class CommentUIHook(idaapi.UI_Hooks):
    def __init__(self):
        idaapi.UI_Hooks.__init__(self)
        self.cmdname = "<no command>"

    def get_ea_hint(self, ea):
        """
        The UI wants to display a simple hint for an address in the navigation band
        
        @param ea: The address
        @return: String with the hint or None
        """
        print("get_ea_hint(%x)" % ea)
        

#---------------------------------------------------------------------
# Remove an existing hook on second run
try:
    ui_hook_stat = "un"
    print("UI hook: checking for hook...")
    uihook
    print("UI hook: unhooking....")
    uihook.unhook()
    del uihook
except:
    print("UI hook: not installed, installing now....")
    ui_hook_stat = ""
    uihook = CommentUIHook()
    uihook.hook()

print("UI hook %sinstalled. Run the script again to %sinstall" % (ui_hook_stat, ui_hook_stat))


class CommentViewer(simplecustviewer_t):
    def Create(self, sn=None):
        # Form the title
        title = "Comment Viewer"
        # Create the customviewer
        if not simplecustviewer_t.Create(self, title):
            return False
        self.menu_hello = self.AddPopupMenu("Hello")
        self.menu_world = self.AddPopupMenu("World")

        #self.AddLine("Line %d" % i)
        return True

    def OnClick(self, shift):
        """
        Cursor position changed.
        @return: Nothing
        """
        print "OnClick"


g = CommentViewer()
g.Create()
g.Show()


def on_click():
    sEA = ScreenEA()
    print GetFunctionCmt(sEA,0)
    #lnum = GetLineNumber(sEA)
    #if lnum in comment_dict:
    #        print comment_dict(lnum)        


def on_hotkey():
    sEA = ScreenEA()
    #operand = GetOpnd(sEA,default_operand)
    #operand_val = GetOperandValue(sEA,default_operand)
    #print "Operand: "+str(operand)
    #if operand_val:
    #    print "Value: "+str(operand_val)
    #lnum = GetLineNumber(sEA)
    #comment = sys.stdin.readlines()
    #comment_dict[lnum] = comment
    #MakeComm(sEA,"Test Comment")
    SetFunctionCmt(sEA,"Test Comment",0)
    graph()


def go_callback(*args):
    go()
    return 1


# IDA binds hotkeys to IDC functions so a trampoline IDC function must be created
idaapi.CompileLine('static flopy_key() { RunPythonStatement("on_hotkey()"); }')
add_idc_hotkey(hotkey_str, 'flopy_key')
idaapi.CompileLine('static flopy_click() { RunPythonStatement("on_click()"); }')
add_idc_hotkey(hotkey_str2, 'flopy_click')


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

