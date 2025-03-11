> The original link of the following content: [http://www.iausofa.org/changes_2016_0503.html](http://www.iausofa.org/changes_2016_0503.html)
<div id="textbox">
 <h3>
  Changes for SOFA Issue: 2016-05-03
 </h3>
 <h4>
  SOFA FORTRAN Library
 </h4>
 <ul>
  <li class="list">
   [New Material]  The addition of four routines to the Precession/Nutation/Polar motion section,which
                                 deliver long-term (+/-200,000 years) precession using the model of Vondrak, Capitaine
                                 and Wallace (2011, 2012).
  </li>
  <ul>
   <li class="list">
    iau_LTP
    <li class="list">
     iau_LTPB
     <li class="list">
      iau_LTPECL
      <li class="list">
       iau_LTPEQU
      </li>
     </li>
    </li>
   </li>
  </ul>
  <li class="list">
   [New Material]  Introduction of a new section entitled Ecliptic Coordinates. This section consists of
                                 six routines dealing with the transformation between equatorial and ecliptic coordinates
                                 using either the IAU 2006 precession model or the long term precession model of Vondrak et al.
  </li>
  <ul>
   <li class="list">
    iau_ECEQ06
    <li class="list">
     iau_ECM06
     <li class="list">
      iau_EQEC06
      <li class="list">
       iau_LTECEQ
       <li class="list">
        iau_LTECM
        <li class="list">
         iau_LTEQEC
        </li>
       </li>
      </li>
     </li>
    </li>
   </li>
  </ul>
  <li class="list">
   [Update/Change] Update to t_sofa_f.for to accommodate the ten new routines.
  </li>
  <li class="list">
   [Revision/Doc.] List of called routines corrected in iau_ATCO13 and iau_ATIO13.
  </li>
 </ul>
 <h4>
  SOFA ANSI C Library
 </h4>
 <ul>
  <li class="list">
   [New Material]  The addition of four routines to the Precession/Nutation/Polar motion section,which
                                 deliver long-term (+/-200,000 years) precession using the model of Vondrak, Capitaine
                                 and Wallace (2011, 2012).
  </li>
  <ul>
   <li class="list">
    iauLtp
    <li class="list">
     iauLtpb
     <li class="list">
      iauLtpecl
      <li class="list">
       iau_Ltpequ
      </li>
     </li>
    </li>
   </li>
  </ul>
  <li class="list">
   [New Material]  Introduction of a new section Entitled Ecliptic Coordinates. This section consists of
                                 six routines dealing with the transformation between equatorial and ecliptic coordinates
                                 using either the IAU 2006 precession model or the long term precession model of Vondrak et al.
  </li>
  <ul>
   <li class="list">
    iauEceq06
    <li class="list">
     iauEcm06
     <li class="list">
      iauEqec06
      <li class="list">
       iauLteceq
       <li class="list">
        iauLtecm
        <li class="list">
         iauLteqec
        </li>
       </li>
      </li>
     </li>
    </li>
   </li>
  </ul>
  <li class="list">
   [Update/Change] Update to sofa.h to allow addition of prototypes for the ten new functions listed above.
  </li>
  <li class="list">
   [Update/Change] Update to t_sofa_c.c to accommodate the ten new routines.
  </li>
  <li class="list">
   [Revision/Doc.] List of called routines corrected in iauAtco13 and iauAtio13.
  </li>
 </ul>
 <h4>
  SOFA Documentation Files
 </h4>
 <ul>
  <li class="list">
   [Update/Change] board.lis – inclusion of new board members.
  </li>
  <li class="list">
   [Update/Change] title.lis – release number and date updated.
  </li>
  <li class="list">
   [Update/Change] intro.lis– updated to reflect the updates and additions of this twelfth release.
  </li>
  <li class="list">
   [Update/Change] sofa_lib.lis – new routines added.
  </li>
  <li class="list">
   [Update/Change] sofa_pn_f.pdf – SOFA Earth Attitude Cookbook for those using Fortran. The former
                                 Fortran-only version was called sofa_pn.pdf. A few typographic corrections have been made.
  </li>
  <li class="list">
   [Update/Change] sofa_pn_c.pdf – SOFA Earth Attitude Cookbook for those using ANSI C. Like the former
                                 Fortran-only version but with function names and argument lists appropriate for the C case.
  </li>
 </ul>
 <!-- Minor Release 12a -->
 <h3>
  Changes for SOFA Issue: 2016-07-29
 </h3>
 <h4>
  SOFA FORTRAN Library
 </h4>
 <ul>
  <li class="list">
   [Update/Change] Update to iau_DAT to accommodate the leap second on 2016 December 31.
  </li>
  <li class="list">
   [Update/Change] Change to iau_LDSUN. The internal threshold value changed from 1D-9 to DLIM, where
                                 DLIM = 1D-6 / MAX(EM*EM,1D0) and EM is the distance in au from the Sun to the observer.
  </li>
  <li class="list">
   [Update/Change] Update to t_sofa_f.for to accommodate the addition of the leap second to iau_DAT.
  </li>
 </ul>
 <h4>
  SOFA ANSI C Library
 </h4>
 <ul>
  <li class="list">
   [Update/Change] Update to iauDat to accommodate the leap second on 2016 December 31.
  </li>
  <li class="list">
   [Update/Change] Change to iauLdsun. The internal threshold value changed from 1D-9 to DLIM, where
                                 DLIM = 1D-6 / MAX(EM*EM,1D0) and EM is the distance in au from the Sun to the observer.
  </li>
  <li class="list">
   [Update/Change] Change to Cr: In the list of "Returned:" arguments listed in the documentation the 
                                 one argument was listed as "char[]" rather than just "c".
  </li>
  <li class="list">
   [Update/Change] Update to t_sofa_c.c to accommodate the addition of the leap second to iauDat.
  </li>
 </ul>
 <h4>
  SOFA Documentation Files
 </h4>
 <ul>
  <li class="list">
   [Update/Change] sofa_ast_f.pdf &amp; sofa_ast_c.pdf : Astrometry cookbook has been modified to
                                 take account of the updated LDSUN/Ldsun routines.
  </li>
  <li class="list">
   [Update/Change] sofa_ts_f.pdf &amp; sofa_ts_c.pdf: Version number of this cookbook corrected.
  </li>
 </ul>
 <!-- Minor Release 12b -->
 <h3>
  Changes for SOFA Issue: 2016-12-21
 </h3>
 <h4>
  SOFA FORTRAN Library
 </h4>
 <ul>
  <li class="list">
   [Update/Change] Change to iau_STARPV. An expression (sqrt(1-x)-1), where x is usually tiny,
                                 has been replaced with (-x/(sqrt(1-x)+1) to improve numerical precision.
  </li>
  <li class="list">
   [Update/Change] Change to iau_REFCO. The line that forms the temperature (TK) in degrees Kelvin
                                 uses the input temperature (TC), rather than T, the TC restricted to the "safe"
                                 range of -15° Celsius to +200° Celsius.
  </li>
 </ul>
 <h4>
  SOFA ANSI C Library
 </h4>
 <ul>
  <li class="list">
   [Update/Change] Change to iauJd2cal (see below).
  </li>
  <li class="list">
   [Update/Change] Change to iauJdcalf. The current C versions of the JD2CAL and JDCALF routines
                                 can, under certain special circumstances, produce incorrect results. The
                                 coding of the new versions has been changed to remove this possibility. The
                                 Fortran versions do not have the problem.
   <br/>
   <p>
    The misbehavior has been detected only under the following circumstances:
   </p>
   <ul>
    <li class="list">
     on Intel and AMD processors;
    </li>
    <li class="list">
     when compiled with the GNU C compiler (gcc);
    </li>
    <li class="list">
     on any operating system that produces a 32-bit executable file;
    </li>
    <li class="list">
     with certain combinations of compiler flags, such as "-fno-caller-saves -m32"; and
    </li>
    <li class="list">
     Julian dates split (dj1+dj2) such that dj2 is in the range 0.1 to 0.5.
    </li>
   </ul>
   <p>
    Calling iauJd2cal or iauJdcalf in these circumstances sometimes returns a result one day too small.
   </p>
   <p>
    As an example, take 2014 September 24 at 19:12:00, which is Julian date 2456925.3 (exactly).
                                 If we elect to split the JD as follows:
   </p>
   <center>
    dj1 = 2456925.0, dj2 = 0.3,
   </center>
   <p>
    then the old iauJd2cal returns 2014 9 23 0.8, which is incorrect, while the new iauJd2cal returns
                                 the correct 2014 9 24 0.8.
   </p>
  </li>
  <li class="list">
   [Update/Change] Change to iauStarpv. An expression (sqrt(1-x)-1), where x is usually tiny,
                                 has been replaced with (-x/(sqrt(1-x)+1) to improve numerical precision.
  </li>
 </ul>
 <h4>
  SOFA Documentation Files
 </h4>
 <ul>
  <li class="list">
   [Update/Change] The ANSI C version of the Time Scales and Calendar Tools cookbook sofa_ts_c.pdf. Julian epoch
                                 2000 has been changed to Julian epoch 2000.0.
  </li>
 </ul>
 <!-- Minor Release 12c -->
 <h3>
  Changes for SOFA Issue: 2016-12-23
 </h3>
 <p>
  Changes/updates for this minor release (12c) fall into the category of changes to the test-bed
routines only. Minor release 12c differs from 12b only in terms of the Fortran and ANSI C test-bed
routines t_sofa_f and t_sofa_c respectively.
 </p>
 <h4>
  SOFA FORTRAN Library
 </h4>
 <ul>
  <li class="list">
   [Update/Change] Change to t_sofa_f. This test program has been modified to reflect
                                 the changes introduced in minor release 12b described above.
  </li>
 </ul>
 <h4>
  SOFA ANSI C Library
 </h4>
 <ul>
  <li class="list">
   [Update/Change] Change to t_sofa_c. This test program has been modified to reflect
                                 the changes introduced in minor release 12b described above.
  </li>
 </ul>
</div>
