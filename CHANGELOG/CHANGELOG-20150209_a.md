> The original link of the following content: [http://www.iausofa.org/changes_2015_0209.html](http://www.iausofa.org/changes_2015_0209.html)
<div id="textbox">
 <h3>
  Changes for SOFA Issue: 2015-02-09
 </h3>
 <h4>
  SOFA FORTRAN Library
 </h4>
 <ul>
  <li class="list">
   [New Material]  2 routines, iau_G2ICRS and iau_ICRS2G, have been released for the new Galactic 
                                 Coordinates section. They allow transformations to be made between the 1958 IAU
                                 galactic coordinate system and the ICRS.
  </li>
  <li class="list">
   [Update/Change] Updated iau_DAT to account for the leap second at the end of June 2015.
  </li>
  <li class="list">
   [Update/Change] Updated iau_CAL2JD.A value in a DATA-initialized array was being changed
                                 during execution.  This had consequences for multi-thread code.  The algorithm 
                                 has been changed to avoid this difficulty.
  </li>
  <li class="list">
   [Update/Change] Changes to iau_C2IXYS, iau_GC2GDE, iau_RM2V and iau_RV2M. There was a test for
                                 zero that could potentially cause compiler warnings.  The test has been changed.
  </li>
  <li class="list">
   [Update/Change] Update to t_sofa_f.for to accommodate the new routines.
  </li>
 </ul>
 <h4>
  SOFA ANSI C Library
 </h4>
 <ul>
  <li class="list">
   [New Material]  2 routines, iauG2icrs and iauIcrs2g, have been released for the new Galactic 
                                 Coordinates section. They allow transformations to be made between the 1958 IAU
                                 galactic coordinate system and the ICRS.
  </li>
  <li class="list">
   [Update/Change] Updated iauDat to account for the leap second at the end of June 2015.
  </li>
  <li class="list">
   [Update/Change] Changes to iauC2ixys, iauGc2gde, iauRm2v and iauRv2m. There was a test for
                                 zero that could potentially cause compiler warnings.  The test has been changed.
  </li>
  <li class="list">
   [Update/Change] Changes to sofa.h. Addition of the new functions, removal of duplicate functions.
                                 All functions are listed in the categories that are given on the website and in the
                                 manual.
  </li>
  <li class="list">
   [Update/Change] Update to t_sofa_c.c to accommodate the new routines.
  </li>
 </ul>
 <h4>
  SOFA Documentation Files
 </h4>
 <ul>
  <li class="list">
   [Update/Change] Minor changes to intro.lis.
  </li>
  <li class="list">
   [Update/Change] New routines added to sofa_lib.lis. The routines STARPV, PVSTAR, PMSAFE and STARPM 
                                 heve been moved into the Astrometry Section. The category Star Space Motion has been
                                 deleted. This list harmonised with sofa.h and the website.
  </li>
 </ul>
 <h3>
  Changes for SOFA Issue: 2015-04-02
 </h3>
 <p>
  This minor release (11a) contains a change to suppress a warning message given by one C compiler for the routine
iauDat. The change does not affect the behaviour of the routine and it is not essential that you update your libraries
(particularly if you are a Fortran user). The change had been already made in the 2014 September 9 (10c) release, but
due to an oversight was not present in the initial version 11 release. The Fortran code has also been modified for 
harmony.
 </p>
 <h4>
  SOFA FORTRAN Library
 </h4>
 <ul>
  <li class="list">
   [Update/Change] A change has been made to the Fortran routine iau_DAT to ensure equivalence between the
                                 Fortran and C versions.
  </li>
 </ul>
 <h4>
  SOFA ANSI C Library
 </h4>
 <ul>
  <li class="list">
   [Update/Change] A change has been made to the Fortran routine iauDat to ensure equivalence between the
                                 Fortran and C versions.
  </li>
 </ul>
</div>
