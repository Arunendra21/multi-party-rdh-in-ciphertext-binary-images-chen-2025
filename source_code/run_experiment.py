import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "_toolkit"))
import build_binary_paper as B, binary_papers_content as BC
c=BC.CONTENT[27]
B._run(os.path.join(os.path.dirname(__file__),"..","figures"),
       os.path.join(os.path.dirname(__file__),"..","outputs"), use_vc=c.get("use_vc",False))
print("experiment done paper 27")
