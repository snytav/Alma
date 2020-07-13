0. Add debug output flag to block debug output
1. insert time measurement (as written in Petro lecture on Python)
2. insert built-in profiling 
2. 1. push 
2. 2. field solver
3. Save times 
3.1. for every timestep 
3.2. with hostname 
3.3. and CPU
3.4. Also unique computation ID
4. save this to some web resource to begin forming The Great Table
5. Visualization with MayaVi and Matplotlib - same as in Book (step through the code to mark where each of the points is done)
5.1. Field and potential - p.72, fig. 2.5. output.cpp:12
5.1.2. In 3D plot:
5.1.2.2. size of X and Y as params
5.1.2.3. Axes title as titles and triplet
5.1.2.4. Colour map
5.1.2.5. Save to file
5.1.2.6. Picture size as parameter
5.2. Number density -      p.83, fig. 2.10. output.cpp:51
5.3.  p.84, fig. 2.11
5.4. Quiet start  - p.86, fig. 2.12
5.5. Energy conservation, p.100, fig. 2.15. output.cpp 104.
5.6. Particles, p.101 - unknown. Maybe start with text output for gnuplot and then smth.
6. Changing it all to NumPy (Organize sublist with priorities)
7. Insert PyCUDA, Dask, Maybe Concurrent Futures
8. Add MPI
9. Change solver to ConjGrad
10. Think about FDTD.
