> The original link of the following content: [http://www.iausofa.org/changes_2019_0722.html](http://www.iausofa.org/changes_2019_0722.html)
<div id="textbox">
 <h3>
  Changes for SOFA Issue: 2019-07-22
 </h3>
 <h4>
  Summary of Changes
 </h4>
 <p>
  The changes fall into the following categories:
 </p>
 <ul>
  <li class="list">
   A wrong sign in the ANSI C function iauTdbtcb has been corrected.
  </li>
  <li class="list">
   Update the DAT routine to the release year.
  </li>
  <li class="list">
   Implementation of four new routines that have been added to the
                 Star Catalog Conversions section dealing with the transformation
                 between the FK4 and the FK5 reference systems.  These routines
                 have have been included partly for completeness but mainly so that
                 positions in publications pre-1984 can be properly handled.  They
                 cover conversions between B1950.0 FK4 and J2000.0 FK5, with and
                 without proper motion.
  </li>
  <li class="list">
   Enhancement of 17 routines that compare the two components of
                 given date/time arguments to minimize rounding errors, so that
                 optimum results are achieved even when one of the arguments is
                 negative. (SOFA is grateful to the Astropy group for drawing
                 attention to the deficiency.)
  </li>
  <li class="list">
   Due to introducing these new routines, the Astrometry Tools
                 Cookbook, the test program and other supporting files have also
                 been updated.
  </li>
  <li class="list">
   Miscellaneous typographical corrections and improvements to
                 various other documents.
  </li>
 </ul>
 <h4>
  Changes to the SOFA FORTRAN Library
 </h4>
 <ul>
  <li class="list">
   iau_DAT.for — Release Year ....
  </li>
  <li class="list">
   iau_FK425 — Convert B1950.0 FK4 star catalog data to J2000.0 FK5.
   <br/>
   iau_FK524 — Convert J2000.0 FK5 star catalog data to B1950.0 FK4.
   <br/>
   iau_FK45Z — Convert a B1950.0 FK4 star position to J2000.0 FK5,
                                   assuming zero proper motion in the FK5 system.
   <br/>
   iau_FK54Z — Convert a J2000.0 FK5 star position to B1950.0 FK4,
                                   assuming zero proper motion in FK5 and zero parallax.
   <br/>
  </li>
  <li class="list">
   In all these seventeen routines the Fortran function ABS was included when comparing the two argument data/time parameter.
   <ul>
    <li class="list">
     iau_JD2CAL
    </li>
    <li class="list">
     iau_JD2CALF
    </li>
    <li class="list">
     iau_TAITT
    </li>
    <li class="list">
     iau_TAIUT1
    </li>
    <li class="list">
     iau_TAIUTC
    </li>
    <li class="list">
     iau_TCBTDB
    </li>
    <li class="list">
     iau_TCGTT
    </li>
    <li class="list">
     iau_TDBTCB
    </li>
    <li class="list">
     iau_TDBTT
    </li>
    <li class="list">
     iau_TTTAI
    </li>
    <li class="list">
     iau_TTTCG
    </li>
    <li class="list">
     iau_TTTDB
    </li>
    <li class="list">
     iau_TTUT1
    </li>
    <li class="list">
     iau_UT1TAI
    </li>
    <li class="list">
     iau_UT1TT
    </li>
    <li class="list">
     iau_UT1UTC
    </li>
    <li class="list">
     iau_UTCTAI
    </li>
   </ul>
  </li>
  <li class="list">
   t_sofa_f.for — Addition of new routines.
  </li>
 </ul>
 <h4>
  Changes to the SOFA ANSI C Library
 </h4>
 <ul>
  <li class="list">
   iauTdbtcb.c —
   <em>
    Replace
   </em>
   <br/>
   <br/>
   *tcb1 = f - ( d - ( f - t77tf ) ) * elbb;
   <em>
    by
   </em>
   *tcb1 = f + ( d - ( f - t77tf ) ) * elbb;
   <br/>
   <br/>
   n.b. the sign error affects only one of two paths through the code.
  </li>
  <li class="list">
   iauDat — Release Year ....
  </li>
  <li class="list">
   iauFk425 — Convert B1950.0 FK4 star catalog data to J2000.0 FK5.
   <br/>
   iauFk524 — Convert J2000.0 FK5 star catalog data to B1950.0 FK4.
   <br/>
   iauFk45z — Convert a B1950.0 FK4 star position to J2000.0 FK5,
                                   assuming zero proper motion in the FK5 system.
   <br/>
   iauFk54z — Convert a J2000.0 FK5 star position to B1950.0 FK4,
                                   assuming zero proper motion in FK5 and zero parallax.
   <br/>
   sofa.h   — Inclusion of the above routines' prototype declarations.
   <br/>
  </li>
  <li class="list">
   In all these seventeen routines the ANSI C function fabs() was included when comparing the two argument data/time parameter.
   <ul>
    <li class="list">
     iauJd2cal
    </li>
    <li class="list">
     iauJd2calf
    </li>
    <li class="list">
     iauTaitt
    </li>
    <li class="list">
     iauTaiut1
    </li>
    <li class="list">
     iauTaiutc
    </li>
    <li class="list">
     iauTcbtdb
    </li>
    <li class="list">
     iauTcgtt
    </li>
    <li class="list">
     iauTdbtcb
    </li>
    <li class="list">
     iauTdbtt
    </li>
    <li class="list">
     iauTttai
    </li>
    <li class="list">
     iauTttcg
    </li>
    <li class="list">
     iauTttdb
    </li>
    <li class="list">
     iauTtut1
    </li>
    <li class="list">
     iauUt1tai
    </li>
    <li class="list">
     iauUt1tt
    </li>
    <li class="list">
     iauUt1utc
    </li>
    <li class="list">
     iauUtctai
    </li>
   </ul>
  </li>
  <li class="list">
   t_sofa_c.c — Addition of new routines.
  </li>
 </ul>
 <p>
  The SOFA Board thanks all those who have reported the various issues 
that go to ensuring the libraries and documentation are kept up-to-date
and relevant.
 </p>
 <p>
  <b>
   SOFA Release 15
  </b>
  : This changes file was updated on 2019 July 22.
 </p>
</div>
