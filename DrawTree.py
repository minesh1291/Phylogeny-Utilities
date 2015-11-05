from ete2 import Tree, faces, AttrFace, TreeStyle, NodeStyle, CircleFace

inputTreeFile = "<inputTreeFile>"

t = Tree(inputTreeFile,format=2)

#~ print t
#~ t.write(format=1, outfile="new_tree.nw")
#~ t.show()

def layout(node):
    if node.is_leaf():
        
        #######################################################
        #~ Taxon Label Size and Margin Adjustment
        N = AttrFace("name", fsize=1200,fgcolor="#000000")
        N.margin_top = 250
        N.margin_right = 100 #outside
        N.margin_left = 1000 #inside
        N.margin_bottom = 250
        #######################################################
        
        #######################################################
        #~ Taxon Label Background Color Setting
        tmp = "<myTaxaonLabel>" 
        #~ if not(node.name.find(tmp)) : N.background.color="#FF9999"
        #######################################################
        
        faces.add_face_to_node(N, node, 0, position="aligned")

    if (not node.is_leaf()) :
        S=faces.AttrFace("support", fsize=200, fgcolor="#000000")
        S.margin_top = 20
        S.margin_right = 10
        S.margin_left = 20
        S.margin_bottom = 20
        faces.add_face_to_node( S, node, column=0 , position = "float")
        if "support" in node.features:
        # Creates a sphere face whose size is proportional to node's
        # feature "weight"
            C = CircleFace(radius=node.support*20, color="RoyalBlue", style="sphere")
        # Let's make the sphere transparent 
            C.opacity = 0.3
        # And place as a float face over the tree
            faces.add_face_to_node(C, node, position="float",column=1)
    style = NodeStyle()
    style["size"] = 0
    style["vt_line_width"] = 150
    style["hz_line_width"] = 150
    style["vt_line_type"] = 0 # 0 solid, 1 dashed, 2 dotted
    style["hz_line_type"] = 0
    node.set_style(style)

    bgcol1="#FFCCCC"
    bgcol2="#FFE5CC"
    bgcol3="#FFFFCC"
    bgcol4="#E5FFCC"
    bgcol5="#CCFFCC"
    bgcol6="#CCFFE5"
    bgcol7="#FFCCE5"
    bgcol8="#CCFFFF"
    bgcol9="#CCE5FF"
    bgcol10="#CCCCFF"
    bgcol11="#E5CCFF"

    #######################################################
    #~ Setting Clade Color
    #~ cs1 = NodeStyle()
    #~ cs1["bgcolor"] = "#FFCCCC"
    #~ c1 = t.get_common_ancestor("<TaxonLabel1>", "<TaxonLabel2>")
    #~ c1.set_style(cs1)
    #######################################################
    
    
    
#Style
ts = TreeStyle()
ts.mode = "c" # draw tree in circular mode
ts.root_opening_factor = 0
#~ ts.arc_start = -180 # 0 degrees = 3 o'clock
#~ ts.arc_span = 180
#~ ts.scale = 20
ts.show_leaf_name = False
#~ ts.show_branch_length = True
#~ ts.show_branch_support = True
#~ ts.optimal_scale_level= "full"
ts.layout_fn = layout
#~ ts.min_leaf_separation = 1000
ts.force_topology=True
#~ ts.guiding_lines_type=0

t.render("image.png", w=1200, dpi=60, units="px", tree_style=ts)

