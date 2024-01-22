SinglePoreAreaConserved.Morpho
- Attempts to satisfy the constraint of conservation of mass by allowing deformation of the outer boundary of the mesh. (A different approach is better)
SinglePoreFixedBnds.Morpho
- Simply fixes the boundary and lets the inner region iterate 
SinglePoreFixedCont.Morpho
- Uses continuation; slowly changes parameters to se the evolution of a system.
SinglePoreAreafunc.Morpho
- Places an energy functional on the area of the region to acount for the chemical potential of exchanging rods across the boundary. (Better than conserving area)
MultiplePoreFixedBnds.Morpho
- Creates mesh and solves for the system with multiple pores in an array.