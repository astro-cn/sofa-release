> The original link of the following content: [http://www.iausofa.org/changes_2021_0125.html](http://www.iausofa.org/changes_2021_0125.html)
<div id="textbox">
 <h3>
  Changes for SOFA Issue: 2021-01-25 (Release 17)
 </h3>
 <h4>
  Summary of Changes
 </h4>
 <p>
  The changes for this major release fall into the following categories:
 </p>
 <ol>
  <li class="list">
   Extra defensive precautions when computing atmospheric
                 refraction at low altitudes.
  </li>
  <li class="list">
   Application of polar motion handling changed to rigorous. 
                 These improvements may result in differences which will
                 be less than 1 mu arcsecond (0.000 001 arc seconds).
  </li>
  <li class="list">
   Expanded documentation including a new cookbook for the
                 SOFA Vector Matrix Library.
  </li>
  <li class="list">
   Typographical and other minor corrections.
  </li>
  <li class="list">
   Changes to the test program.
  </li>
 </ol>
 <h4>
  Changes to the SOFA FORTRAN Library
 </h4>
 <ol>
  <li class="list">
   iau_ATIOQ — Include a limit in altitude (about 3 degrees) below
                 which atmospheric refraction is held constant, for
                 defense and to make it consistent with iau_atoiq.
  </li>
  <li class="list">
   iau_ATIOQ, iau_ATOIQ, iau_APCO, iau_APIO — Application of polar
                 motion calculation made rigorous for canonical consistency.
   <li class="list">
    The updates in the following routines were documentation corrections/additions:
    <ul>
     <li class="list">
      iau_EE00B — IERS Conventions reference updated to (2003)
     </li>
     <li class="list">
      iau_GST00B — IERS Conventions reference updated to (2003)
     </li>
     <li class="list">
      iau_PMAT06 — IAU reference added
     </li>
     <li class="list">
      iau_PNM06A — Variable renamed to follow SOFA nomenclature
     </li>
     <li class="list">
      iau_PNM80 — Date variables now correctly labelled as TT
     </li>
     <li class="list">
      iau_TRXPV —Action corrected to R^T * PV together with additional note
     </li>
    </ul>
   </li>
   <li class="list">
    The updates in the following routines are documentation improvements and
                 typographical corrections:
    <ul>
     <li class="list">
      iau_AF2A
     </li>
     <li class="list">
      iau_BI00
     </li>
     <li class="list">
      iau_C2I00A, iau_C2T00A, iau_C2T00B, iau_C2T06A, iau_C2TPE, iau_C2TXY, iau_CAL2JD
     </li>
     <li class="list">
      iau_EO06A, iau_EORS, iau_EPB2JD, iau_EPJ2JD
     </li>
     <li class="list">
      iau_FAOM03, iau_FW2M
     </li>
     <li class="list">
      iau_GMST00, iau_GMST06, iau_GST00A, iau_GST06, iau_GST06A, iau_GST94
     </li>
     <li class="list">
      iau_JD2CAL, iau_JDCALF
     </li>
     <li class="list">
      iau_NUM00A
     </li>
     <li class="list">
      iau_PMAT00, iau_PNM00A, iau_PNM00B, iau_POM00, iau_PVU, iau_REFCO
     </li>
     <li class="list">
      iau_RV2M, iau_RXPV
     </li>
     <li class="list">
      iau_TCGTT, iau_TF2A
     </li>
     <li class="list">
      iau_UT1UTC
     </li>
     <li class="list">
      iau_XYS00B, iau_XYS06A
     </li>
     <li class="list">
      iau_ZP, iau_ZPV
     </li>
    </ul>
   </li>
   <li class="list">
    Test program t_sofa_f.f was updated due to items (1) and (2) above.
   </li>
  </li>
 </ol>
 <h4>
  Changes to the SOFA ANSI C Library
 </h4>
 <ol>
  <li class="list">
   iauAtoiq — Include a limit in altitude (about 3 degrees)
                 below which atmospheric refraction is held constant, for
                 defense and to make it consistent with iauAtioq.
  </li>
  <li class="list">
   iauAtioq, iauAtoiq, iauApco, iauApio — Application of polar
                 motion calculation made rigorous for canonical consistency.
  </li>
  <li class="list">
   The updates in the following functions were documentation corrections:
   <ul>
    <li class="list">
     iauEe00b — IERS Conventions reference updated to (2003)
    </li>
    <li class="list">
     iaugst00b — IERS Conventions reference updated to (2003)
    </li>
    <li class="list">
     iauPmat06 — IAU reference added
    </li>
    <li class="list">
     iauPnm06a — Variable renamed to follow SOFA nomenclature
    </li>
    <li class="list">
     iauTrxpv — Action corrected to R^T * PV together with additional note
    </li>
   </ul>
  </li>
  <li class="list">
   The updates in the following functions are documentation improvements
                 and typographical corrections:
   <ul>
    <li class="list">
     iauAtciqn, iauAticqn
    </li>
    <li class="list">
     iauBi00
    </li>
    <li class="list">
     iauC2i00a, iauC2t00a, iauC2t00b, iauC2t06a, iauC2tpe, iauC2txy
    </li>
    <li class="list">
     iauEo06a, iauEors
    </li>
    <li class="list">
     iauFaom03, iauFk45z, iauFk54z, iauFw2m
    </li>
    <li class="list">
     iauGmst00, iauGst00a, iauGst06, iauGst06a, iauGst94
    </li>
    <li class="list">
     iauJd2cal, iauJdcalf
    </li>
    <li class="list">
     iauNum00a
    </li>
    <li class="list">
     iauPmat00, iauPn00a, iauPn00b, iauPn06, iauPnm00a, iauPnm00b, iauPnm80, iauPom00
    </li>
    <li class="list">
     iauRefco, iauRv2m, iauRxpv
    </li>
    <li class="list">
     iauS00, iauSxpv
    </li>
    <li class="list">
     iautcgtt
    </li>
    <li class="list">
     iauUt1utc
    </li>
    <li class="list">
     iauXys00b, iauXys06a
    </li>
    <li class="list">
     iauZp, iauZpv
    </li>
   </ul>
  </li>
  <li class="list">
   Test program t_sofa_c.c was updated due to items (1) and (2) above.
  </li>
 </ol>
 <p>
  The SOFA Board thanks all those who have reported the various issues 
that go to ensuring the libraries and documentation are kept up-to-date
and relevant.
 </p>
 <p>
  <b>
   SOFA Release 17
  </b>
  : This changes file was updated on 2021 January 8.
 </p>
 <!-- Minor Release 17a -->
 <h3>
  Changes for SOFA Issue: 2021-02-24
 </h3>
 <p>
  The change for this minor release (17a) relates to dealing with
leap seconds during the period 1960 and 1971.
 </p>
 <p>
  Between the introduction of UTC at the start of 1960 and the first
leap second at the end of 1971 there were a series of small offsets
and rate changes with respect to TAI.  The SOFA routine D2DTF takes
these into account, but a shortcoming in the algorithm meant that
under certain conditions a leap second could be flagged even though
none had occurred.
 </p>
 <p>
  Such cases were extremely rare, and moreover depended to some extent 
on compiler behaviour, affecting rounding.
 </p>
 <p>
  SOFA is grateful to the Astropy group for reporting an instance of
this bug, which has been corrected.
 </p>
 <h4>
  Changes to the SOFA FORTRAN Library
 </h4>
 <ul>
  <li class="list">
   Change to iau_d2dtf. Format for output a 2-part Julian Date
                 (or in the case of UTC a quasi-JD form that includes special
                 provision for leap seconds).
  </li>
 </ul>
 <h4>
  Changes to the SOFA ANSI C Library
 </h4>
 <ul>
  <li class="list">
   Change to iauD2dtf. Format for output a 2-part Julian Date
                 (or in the case of UTC a quasi-JD form that includes special
                 provision for leap seconds).
  </li>
 </ul>
 <p>
  <b>
   SOFA Release 17a
  </b>
  : This changes file was updated on 2021 February 23.
 </p>
</div>
