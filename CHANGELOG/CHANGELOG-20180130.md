> The original link of the following content: [http://www.iausofa.org/changes_2018_0130.html](http://www.iausofa.org/changes_2018_0130.html)
<div id="textbox">
 <h3>
  Changes for SOFA Issue: 2018-01-30
 </h3>
 <p>
  The changes fall into the following categories:
 </p>
 <ul>
  <li class="list">
   Change in the copyright status of the DAT routine.
  </li>
  <li>
   Implementation of two new categories of routines, viz:
   <ul>
    <li>
     There are three routines for the horizon/equatorial plane coordinates.
    </li>
    <li>
     There are six routines dealing with gnomonic (tangent plane) projections.
    </li>
   </ul>
   <li>
    Due to the introduction of these new routines, The Astrometry Tools Cookbook, the test 
     program and other supporting files have also been updated.
   </li>
   <li>
    Other minor documentation/typographical corrections to various files.
   </li>
  </li>
 </ul>
 <h4>
  Changes to the SOFA FORTRAN Library
 </h4>
 <ul>
  <li class="list">
   iau_DAT.for — Code now classified as "user-replaceable support
                                     routine".  Thus the terms and conditions at the end
                                     are also modified.
   <br/>
   sofa_ts_f.pdf — Updated Cookbook to include information about the
                                       change in status.
  </li>
  <li class="list">
   iau_AE2HD — (azimuth, altitude) to (hour angle, declination)
   <br/>
   iau_HD2AE — (hour angle, declination) to (azimuth, altitude)
   <br/>
   iau_HD2PA — parallactic angle
  </li>
  <li clsss="list">
   iau_TPORS — solve for tangent point, spherical
   <br/>
   iau_TPORV — solve for tangent point, vector
   <br/>
   iau_TPSTS — project tangent plane to celestial, spherical
   <br/>
   iau_TPSTV — project tangent plane to celestial, vector
   <br/>
   iau_TPXES — project celestial to tangent plane, spherical
   <br/>
   iau_TPXEV — project celestial to tangent plane, vector
  </li>
  <li class="list">
   t_sofa_f.for — Validation program
   <br/>
   sofa_ast_f.pdf — Astrometry Tools Cookbook, with added information on the new routines
  </li>
  <li class="list">
   board.lis, copyr.lis, intro.lis, sofa_lib.lis &amp; title.lis — updated compononents of the manual.
  </li>
  <li class="list">
   The following routines/files have had very minor documentation changes, mostly typographical:
   <ul>
    <li class="list">
     iau_ATIOQ
    </li>
    <li class="list">
     iau_EECT00
    </li>
    <li class="list">
     iau_EQEQ94
    </li>
    <li class="list">
     iau_FK52H
    </li>
    <li class="list">
     iau_FK5HIP
    </li>
    <li class="list">
     iau_GMST82
    </li>
    <li class="list">
     iau_H2FK5
    </li>
    <li class="list">
     iau_PLAN94
    </li>
    <li class="list">
     sofa_pn_f.pdf
    </li>
   </ul>
  </li>
 </ul>
 <h4>
  Changes to the SOFA ANSI C Library
 </h4>
 <ul>
  <li class="list">
   iauDat.c — Code now classified as "user-replaceable support
                                  routine".  Thus the terms and conditions at the end
                                  are also modified.
   <br/>
   sofa_ts_c.pdf — Updated Cookbook to include information about the
                                       change in status.
  </li>
  <li class="list">
   iauAe2hd — (azimuth, altitude) to (hour angle, declination)
   <br/>
   iauHd2ae — (hour angle, declination) to (azimuth, altitude)
   <br/>
   iauHd2pa — parallactic angle
  </li>
  <li clsss="list">
   iauTpors — solve for tangent point, spherical
   <br/>
   iauTporv — solve for tangent point, vector
   <br/>
   iauTpsts — project tangent plane to celestial, spherical
   <br/>
   iauTpstv — project tangent plane to celestial, vector
   <br/>
   iauTpxes — project celestial to tangent plane, spherical
   <br/>
   iauTpxev — project celestial to tangent plane, vector
  </li>
  <li class="list">
   sofa_h — The include file updated with the new routines
   <br/>
   t_sofa_c.c — Validation program
   <br/>
   sofa_ast_c.pdf — Astrometry Tools Cookbook, with added information on the new routines
  </li>
  <li class="list">
   board.lis, copyr.lis, intro.lis, sofa_lib.lis &amp; title.lis — updated compononents of the manual.
  </li>
  <li class="list">
   The following routines/files have had very minor documentation changes, mostly typographical:
   <ul>
    <li class="list">
     iauDtdb
    </li>
    <li class="list">
     iauEect00
    </li>
    <li class="list">
     iauEpv00
    </li>
    <li class="list">
     iauEqeq94
    </li>
    <li class="list">
     iauFk52h
    </li>
    <li class="list">
     iauFk5hip
    </li>
    <li class="list">
     iauG2icrs
    </li>
    <li class="list">
     iauGmst82
    </li>
    <li class="list">
     iauH2fk5
    </li>
    <li class="list">
     iauIcrs2g
    </li>
    <li class="list">
     iauNut00a
    </li>
    <li class="list">
     iauNut00b
    </li>
    <li class="list">
     iauNut80
    </li>
    <li class="list">
     iauPlan94
    </li>
    <li class="list">
     iauS00
    </li>
    <li class="list">
     iauS06
    </li>
    <li class="list">
     iauXy06
    </li>
    <li class="list">
     sofa_pn_c.pdf
    </li>
   </ul>
  </li>
 </ul>
 <p>
  SOFA Release 14: This changes file was updated on 2018 January 29.
 </p>
</div>
