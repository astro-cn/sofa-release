> The original link of the following content: [http://www.iausofa.org/changes_2013_1202.html](http://www.iausofa.org/changes_2013_1202.html)
<div id="textbox">
 <h3>
  Changes for SOFA Issue: 2013-12-02
 </h3>
 <h4>
  SOFA FORTRAN Library
 </h4>
 <ul>
  <li class="list">
   [New Material]  32 routines have been released for the new Astrometry section as well as one 
                                 new routine for the Star Catalog Conversion section. A cookbook and summary 
                                 information to accompany the new section has also been released.
  </li>
  <li class="list">
   [Update/Change] Corrected due to bug with TAI-&gt;UTC 1960-1972:  d2dtf.for, dtf2d.for, taiutc.for 
                                 and utctai.for.
  </li>
  <li class="list">
   [Update/Change] Corrected; if an error condition arises, ELONG is now set to -1d9 in gc2gd.for.
  </li>
  <li class="list">
   [Update/Change] Minor changes to bp00.for, bp06.for, dat.for and prec76.for.
  </li>
  <li class="list">
   [Documentation] Minor changes to comments in c2tcio.for, c2teqx.for,  epb.for, epv00.for, eqeq94.for, 
                                 fk5hz.for, fw2xy.for, hfk5z.for, nutm80.for, plan94.for pn06.for, pnm80.for, 
                                 ut1utc.for, utcut1.for, and xys06a.for.
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
   [New Material]  32 routines have been released for the new Astrometry section as well as one 
                                 new routine for the Star Catalog Conversion section. A cookbook and summary 
                                 information to accompany the new section has also been released.
  </li>
  <li class="list">
   [Update/Change] Corrected due to bug with TAI-&gt;UTC 1960-1972: d2dtf.c, dtf2d.c, taiutc.c and 
                                 utctai.c.
  </li>
  <li class="list">
   [Update/Change] Corrected; if an error condition arises, elong is now set to -1e9 in gc2gd.c.
  </li>
  <li class="list">
   [Change/Update] sofa.h updated and now #includes sofam.h. sofam.h also updated.
  </li>
  <li class="list">
   [Change/Update] All source files: inclusion of sofam.h was replaced with sofa.h which now includes 
                                 sofam.h (with the exception of ee00.c, ee00a.c, ee00b.c, ee06a.c and gst94.c).
  </li>
  <li class="list">
   [Update/Change] Minor changes to bp00.c, bp06.c, cal2jc.c, dat.c, epb.c, epb2jd.c, epj2jd.c,
                                 jdcal.c, pm.c, prec76.c and xy06.c.
  </li>
  <li class="list">
   [Documentation] Minor changes to comments in a2tf.c, c2i06a.c, c2tcio.c, c2teqx.c, eo06a.c, epj.c, 
                                 eqeq94.c, fw2xy.c, gmst82.c, pn00a.c, pn00b.c, pn06.c, pn06a.c, s00a.c, s00b.c,
                                 starpm.c, sxpv.c, ut1utc.c and xys06a.c.
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
   [Update/Change] Added note in sofa_pn.pdf that in the example numerical values for polar motion 
                                 and UT1-UTC are for illustration only.
  </li>
  <li class="list">
   [Update/Change] In sofa_ts_f.pdf and sofa_ts_c.pdf, units information has been added since
   <ol>
    <li class="list">
     In the equation for TCG in terms of TT in Sect.3.6.4, TCG and TT are in JD or MJD form, though
           that is not stated.
    </li>
    <li class="list">
     In the equation for TDB in terms of TCB in Sect. 3.6.5 (which is taken straight from the IAU
           resolution) TDB and TCB are in seconds, and that also is not stated.
    </li>
   </ol>
  </li>
  <li class="list">
   [Update/Change] On page 23 of sofa_ts_c.pdf, the xyz array should be dimensioned to 3.
  </li>
  <li class="list">
   [Update/Change] Changes to board.lis reflecting the composition of the SOFA board, changes to 
                                 intro.lis and sofa_lib.lis dealing with the addition of the new Astrometry 
                                 section and a cosmetic change to copyr.lis.
  </li>
 </ul>
 <h3>
  Revisions for SOFA Issue: 2013-12-02
 </h3>
 <h4>
  SOFA FORTRAN Library only
 </h4>
 <ul>
  <li class="list">
   [Update/Change] Harmonize the Fortran and C versions of the ATIOQ routine.  A recent change 
                                 was to return azimuth in the range 0 to 2pi radians rather than +/- pi 
                                 radians, and though the new C version was released the Fortran version was 
                                 inadvertently not released.
   <li class="list">
    [Update/Change] Change of declaration from character*1 S to character S in af2a.for, tf2a.for
                                 and tf2d.for.
    <li class="list">
     [Update/Change] Non-critical removal of unused constants in eect00.for, taiutc.for and xy06.for.
    </li>
   </li>
  </li>
 </ul>
 <h3>
  Revisions for SOFA Issue: 2014-02-20
 </h3>
 <h4>
  SOFA FORTRAN and ANSI C Libraries
 </h4>
 <ul>
  <li class="list">
   [Error/Change]  Error correction in routine d2dtf. The routine truncated rather than rounded
                                 in the (uncommon) case of a time in the second half of a leap second and a
                                 precision of 1 second.  In addition, the rounding behavior during leap seconds
                                 has been changed so that for a precision of 10 seconds or coarser the beginning
                                 of the next day is used in preference to the start of the leap second.
  </li>
  <li class="list">
   [Documentation] Documentation error in routine apco13. Given argument THETA Earth rotation angle
                                 (radians) included incorrectly in the information list.
  </li>
  <li class="list">
   [Documentation] Documentation error in routine atioq. Returned argument DOB, which is the observed
                                 declination (CIO-based, radians), was described incorrectly and the argument ROB,
                                 observed right ascension (CIO-based, radians), was missing from the information list.
  </li>
  <li class="list">
   [Documentation] Documentation in files sofa_ts_f.pdf and sofa_ts_c.pdf. Two errors in the examples
                                 in Section 4.4: "A comprehensive example: transform UTC into other times"
   <ol>
    <li class="list">
     +0.5 is required to be added to the UT variable (page 23 C version, page 24 Fortran)
                                 as time is measured from midnight;
    </li>
    <li class="list">
     On page 24, in the routine DTDB the units for the variables, U and V (i.e. the last two
                                 arguments) are required in kilometers and not in meters as calculated.
    </li>
   </ol>
   This results, on page 25, in a small difference in the TDB and TCB times reported.
  </li>
 </ul>
 <h3>
  Revisions for SOFA Issue: 2014-09-08
 </h3>
 <ul>
  <li class="list">
   [Error/Change]  Error correction in routine pmsafe.c. An operator precedence bug that under some 
                                 circumstances could return the wrong error status has been corrected.
  </li>
  <li class="list">
   [Error/Change]  Change to dat.c. A correction has been made to suppress an array bounds warning
                                 produced by recent gcc versions.
  </li>
  <li class="list">
   [Error/Change]  Change to sofa.h. Editing to make the arguments consistent with those of the routines.
  </li>
  <li class="list">
   [Documentation] Commeting for ldsun.for and ldsun.c has been updated.
  </li>
  <li class="list">
   [Documentation] Documentation in sofa_pn.pdf, sofa_ast_f.pdf and sofa_ast_c.pdf. All changes in the 
                                 Cookbooks are correcting comments in the example code.
  </li>
 </ul>
 <h3>
  Revisions for SOFA Issue: 2014-10-07
 </h3>
 <ul>
  <li class="list">
   [Documentation] Documentation in sofa_ast_f.pdf and sofa_ast_c.pdf. Correct page references for 
                                 iau_ATCIQN to iau_ATICQN on page 52 in sofa_ast_f.pdf and for iauAtciqn to 
                                 iauAticqn on page 52 in sofa_ast_c.pdf. Also remove pages 52/53 in both versions
                                 to replace comments for the appropriate routine.
  </li>
 </ul>
</div>
