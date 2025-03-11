> The original link of the following content: [http://www.iausofa.org/changes_2012_0301.html](http://www.iausofa.org/changes_2012_0301.html)
<div id="textbox">
 <h3>
  Changes for SOFA Issue: 2012-03-01
 </h3>
 <h4>
  SOFA Terms &amp; Conditions
 </h4>
 <p>
  The license terms and conditions have been changed slightly. The stipulation that modified 
versions must not bear names that have the prefix "iau" or "sofa" has been clarified, and 
acknowledgement of SOFA has been downgraded to a request.
 </p>
 <h4>
  SOFA FORTRAN Library
 </h4>
 <ol>
  <li class="list">
   [Update/change] Leap second for 2012 June 30 added to dat.for. Code has been improved.
  </li>
  <li class="list">
   [Documentation] Errata in af2a.for, dtf2d.for, nut06a.for, p06e.for, tdbtt.for, tf2a.for,
                                 tf2d.for and ut1tt.for have been corrected.
  </li>
  <li class="list">
   [Documentation] Cosmetic changes have been made to taiut1.for, taiutc.for, tcbtdb.for,
                                 tdbtcb.for, tttdb.for, ttut1.for, ut1tai.for and ut1utc.for.
  </li>
 </ol>
 <h4>
  SOFA ANSI C Library
 </h4>
 <ol>
  <li class="list">
   Version number of ANSI C release aligned with the Fortran version number to 9.
  </li>
  <li class="list">
   [Update/Change] Leap second for 2012 June 30 added to dat.c. In iauDat a leap second has 
                                 been added for 2012 June 30.
  </li>
  <li class="list">
   [Update/Change] First argument changed from 'int s' to 'char s' in af2a, tf2a and tf2d. In 
                                 iauAf2a, iauTf2a and iauTf2d, the data type of the sign argument has been 
                                 changed to char, for clarity and for consistency with the converse functions 
                                 iauA2af, iauA2tf and iauD2tf.
  </li>
  <li class="list">
   [Update/Change] First argument changed from 'char *scale' to 'const char *scale' in d2dtf and 
                                 dtf2d. The scale arguments of the C functions iauD2dtf and iauDtf2d have been 
                                 changed from char* to const char* to allow read-only strings (in particular 
                                 string literals) to be used without risking compiler warnings. Analogous changes 
                                 have been made to the viv and vvd functions inside the test program t_sofa_c.
  </li>
  <li class="list">
   [Update/Change] Test program t_sofa_c updated due to the above.
  </li>
  <li class="list">
   [Update/Change] Header file sofa.h updated to reflect the changes listed above.
  </li>
  <li class="list">
   [Update/Change] For sofam.h, a note has been added that the constants defined in the file are 
                                 used only in the context of the SOFA Software, and have no official IAU status. 
                                 Reference Ellipsoids defined via symbols WGS84=1, GRS80=2 and WGS72=3. In 
                                 iauEform, iauGc2gd and iauGd2gc can use the symbols defined in the sofam.h file 
                                 for the reference ellipsoids WGS84=1, GRS80=2 and WGS72=3.
  </li>
  <li class="list">
   [Update/Errata] In sofam.h, the function dsign(A,B) was only valid for +ve A. The comment for 
                                 the constant DS2R has been corrected.
  </li>
  <li class="list">
   [Documentation] Errata in d2tf.c, dtdb.c, nut06a.c, p06e.c, tdbtt.c, ut1tai.c and ut1tt.c have 
                                 been corrected.
  </li>
  <li class="list">
   [Documentation] Cosmetic changes have been made to taitt.c, taiut1.c, taiutc.c, tcbtdb.c, 
                                 tdbtcb.c, tttai.c, tttdb.c, ttut1.c and ut1utc.c.
  </li>
 </ol>
 <h3>
  Revisions: 2012-07-10
 </h3>
 <ol>
  <li class="list">
   [Update/change] The test on the FD argument in dat.for and dat.c has been eased to include the 
                                 case where FD equals 1. This ensures proper operation of the routine when FD is
                                 close to 1.
   <li class="list">
    [Update/change] ir.for, ir.c, rx.for, rx.c, ry.for, ry.c, rz.for, rz.c, zr.for and zr.c have 
                                 arrays explicitly set up to improve efficiency.
    <li class="list">
     [Documentation] Previously reported error in documentation for plan94.c has been corrected.
    </li>
   </li>
  </li>
 </ol>
</div>
