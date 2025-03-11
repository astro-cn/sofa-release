> The original link of the following content: [http://www.iausofa.org/changes_2020_0721.html](http://www.iausofa.org/changes_2020_0721.html)
<div id="textbox">
 <h3>
  Changes for SOFA Issue: 2020-07-21
 </h3>
 <h4>
  Summary of Changes
 </h4>
 <p>
  The changes fall into the following categories:
 </p>
 <ul>
  <li class="list">
   Correction of a sign in routine P06E.
  </li>
  <li class="list">
   Correction in the ANSI C macro function dnint in the include file
                 sofam.h, to improve rounding.
  </li>
  <li class="list">
   Improvements in precision and rounding (see items 2 and 3 below).
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
   iau_P06E — Correction. The series are taken from Table 1 of Hilton,
                 J. et al., 2006, Celest. Mech. Dyn. Astron. 94, 351., and it has been
                 discovered that the one for general precession, p_A, had the wrong sign
                 for the t^5 coefficient.  The error in the paper has been corrected in
                 the SOFA code. The correct value is -0.0000000383 arcsec.  (Even after
                 five centuries the error would be lower than 250 microarcsec.)
  </li>
  <li class="list">
   iau_PB06 — Improvements in the method of decomposing the rotation
                   matrix by ensuring that angles near zero are preferred.
  </li>
  <li class="list">
   Improvements by ensuring precision is not lost when splitting date and time.
   <ul>
    <li class="list">
     iau_JD2CAL
    </li>
    <li class="list">
     iau_JDCALF
    </li>
   </ul>
  </li>
  <li class="list">
   iau_DAT — Release year updated.
  </li>
  <li class="list">
   t_sofa_f.for — Updated due to the correction in iau_P06E.
  </li>
  <li class="list">
   Minor corrections/improvements to the documentation of the following routines
   <ul>
    <li class="list">
     iau_FK524
    </li>
    <li class="list">
     iau_FW2M
    </li>
    <li class="list">
     iau_GMST82
    </li>
    <li class="list">
     iau_TRXP
    </li>
    <li class="list">
     iau_XYS00A
    </li>
   </ul>
  </li>
 </ul>
 <h4>
  Changes to the SOFA ANSI C Library
 </h4>
 <ul>
  <li class="list">
   iauP06e —  Correction. Correction. The series are taken from Table 1
                 of Hilton, J. et al., 2006, Celest. Mech. Dyn. Astron. 94, 351., and it has
                 been discovered that the one for general precession, p_A, had the wrong sign
                 for the t^5 coefficient.  The error in the paper has been corrected in the
                 SOFA code. The correct value is -0.0000000383 arcsec.  (Even after five
                 centuries the error would be lower than 250 microarcsec.)
  </li>
  <li class="list">
   sofam.h — Correction to dnint(A). The existing dnint macro could
                 incorrectly round numbers just over -0.5 and just under +0.5 due to
                 the loss of precision when calculating ceil(A-0.5) or floor(A+0.5). A
                 preliminary test for |A|&lt;0.5 has been added to ensure that such numbers
                 always round to zero.  As none of the SOFA C functions depend critically
                 on perfect rounding, the change is unlikely to affect user applications
                 noticeably, though critical round-trip tests may see an improvement.
  </li>
  <li class="list">
   iauPb06 — Improvements in the method of decomposing the rotation
                 matrix by ensuring that angles near zero are preferred.
  </li>
  <li class="list">
   Improvements by ensuring precision is not lost when splitting date and time.
   <ul>
    <li class="list">
     iauJd2cal
    </li>
    <li class="list">
     iauJdcalf
    </li>
   </ul>
  </li>
  <li class="list">
   iauDat — Release year updated.
  </li>
  <li class="list">
   t_sofa_f.for — Updated due to the correction in iauP06e.
  </li>
  <li class="list">
   Minor corrections/improvements to the documentation of the following routines
   <ul>
    <li class="list">
     iauA2af
    </li>
    <li class="list">
     iauA2tf
    </li>
    <li class="list">
     iauD2tf
    </li>
    <li class="list">
     iauFk524
    </li>
    <li class="list">
     iauFw2m
    </li>
    <li class="list">
     iauGmst82
    </li>
    <li class="list">
     iauTrxp
    </li>
    <li class="list">
     iauXys00a
    </li>
   </ul>
  </li>
 </ul>
 <p>
  The SOFA Board thanks all those who have reported the various issues 
that go to ensuring the libraries and documentation are kept up-to-date
and relevant.
 </p>
 <p>
  <b>
   SOFA Release 16
  </b>
  : This changes file was updated on 2020 July 21.
 </p>
</div>
