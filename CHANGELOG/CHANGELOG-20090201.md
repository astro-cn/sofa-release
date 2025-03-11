> The original link of the following content: [http://www.iausofa.org/changes_2009_0201.html](http://www.iausofa.org/changes_2009_0201.html)
<div id="textbox">
 <h3>
  Changes for SOFA Issue: 2009-02-01
 </h3>
 <ol>
  <li class="list">
   The leap second of 2008 December 31 was added to the iau_DAT routine, and the "release year" 
changed to 2009.
   <li class="list">
    Cosmetic changes were made to: bi00.for, bp00.for, bp06.for, dtdb.for, eect00.for, eors.for, 
epb.for, epb2jd.for, epj.for, epj2jd.for, epv00.for, eqeq94.for, era00.for, fk5hz.for, gmst00.for, 
gmst06.for, gmst82.for, gst06a.for, hfk5z.for, nut00a.for, nut00b.for, nut06a.for, nut80.for, 
obl06.for, obl80.for, p06e.for, pfw06.for, plan94.for, pmat76.for, pn00a.for, pn00b.for, pn06.for, 
pnm06a.for, pr00.for, prec76.for,  pv2s.for, pvup.for, rm2v.for, rv2m.for, s00.for, s06.for, 
sp00.for, starpm.for and xy06.for
    <li class="list">
     Revised license text.
     <li class="list">
      The file board.lis was updated to reflect membership changes.
      <li class="list">
       Revised intro.lis, sofa_vml.lis and sofa_lib.lis, covering the new C version.
       <li class="list">
        Test program t_sofa_f.for added.
       </li>
      </li>
     </li>
    </li>
   </li>
  </li>
 </ol>
 <h3>
  Revisions: 2009-03-03
 </h3>
 <ol>
  <li class="list">
   An error in the C version of the DAT routine was corrected. The error, not 
present in the Fortran version, applied only to dates in the first half of 1972. 
The consequences were platform-dependent; in the test environment the error left 
the results unaffected, but with other compilers and computers, wrong answers or 
even arithmetical exceptions were possible.
  </li>
 </ol>
 <h3>
  Revisions: 2009-03-18
 </h3>
 <ol>
  <li class="list">
   A bug affecting the routines FK52H and H2FK5 (both Fortran and C) has been 
corrected. This caused erroneous proper motions (and also radial velocity) to be 
returned.
   <li class="list">
    The testbeds t_sofa_f.for and t_sofa_c.c have been updated to reflect the 
changes to FK52H and H2FK5.
    <li class="list">
     In the C header file sofa.h, an unused reference has been removed.
     <li class="list">
      In the C functions iauFk5hip, iauGmst00, iauObl80 and iauObl06, use of the 
ANSI C language feature "unary plus" has been eliminated, to avoid difficulties
with older compilers.
     </li>
    </li>
   </li>
  </li>
 </ol>
 <h3>
  Revisions: 2009-04-02
 </h3>
 <ol>
  <li class="list">
   An error in the description of the coordinates of the Celestial Intermediate
Pole with respect to the International Terrestrial Reference System in the routines 
C2T00A, C2T00B, C2T06A, C2TPE, C2TXY and POM00 has been corrected in both the 
Fortran and C libraries. These revisions have no effect on the results produced by 
these routines.
  </li>
 </ol>
</div>
