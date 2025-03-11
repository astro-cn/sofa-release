> The original link of the following content: [http://www.iausofa.org/changes_2017_0420.html](http://www.iausofa.org/changes_2017_0420.html)
<div id="textbox">
 <h3>
  Changes for SOFA Issue: 2017-04-20
 </h3>
 <p>
  The changes fall into the following categories:
 </p>
 <ul>
  <li class="list">
   Implementation of the IAU 2012 definition of the astronomical unit (au). Not only has this constant been updated, but also
   <ul>
    <li>
     all derived quantities are evaluated via the appropriate formulas, and
    </li>
    <li>
     all documentation now uses the appropriate symbols for the unit, for example, 1 au and 2.3 au/day.
    </li>
   </ul>
  </li>
  <li class="list">
   Update to PVSTAR to make it consistent with the version of STARPV that was updated in the previous release.
  </li>
  <li class="list">
   Other minor typographical corrections to various routines.
  </li>
 </ul>
 <h4>
  Changes to the SOFA FORTRAN Library
 </h4>
 <ul>
  <li class="list">
   The IAU 2012 value of the astronomical unit (au) is now implemented in these six routines:
  </li>
  <ul>
   <li class="list">
    iau_APCS
   </li>
   <li class="list">
    iau_LDN
   </li>
   <li class="list">
    iau_PMPX
   </li>
   <li class="list">
    iau_PVSTAR
   </li>
   <li class="list">
    iau_STARPM
   </li>
   <li class="list">
    iau_STARPV
   </li>
  </ul>
  <li class="list">
   An expression (sqrt(1-x)-1), where x is usually tiny, has been replaced with (-x/(sqrt(1-x)+1) to improve numerical precision in iau_PVSTAR.
  </li>
  <li class="list">
   Check values in the validation program t_sofa_f have been updated due to the change in the astronomical unit.
  </li>
  <li class="list">
   The SOFA Astrometry Tools cookbook sofa_ast_f.pdf:
   <ul>
    <li class="list">
     In the table on page 22 there is a change of +1×10
     <sup>
      -7
     </sup>
     seconds in RA for three results when compared to using the previous value for the au.  
                 These cases are repeated on the next 2 pages.
    </li>
    <li class="list">
     The listing of the relativistic version of the routine iau_PMPX in the Appendix has been updated on page 77 with the required changes for the au.
    </li>
   </ul>
  </li>
 </ul>
 <h4>
  Changes to the SOFA ANSI C Library
 </h4>
 <ul>
  <li class="list">
   The astronomical unit (au) has been updated in the sofam.h include file and all constants that are derived from the au have been replaced by the appropriate formulas.
  </li>
  <li class="list">
   An expression (sqrt(1-x)-1), where x is usually tiny, has been replaced with (-x/(sqrt(1-x)+1) to improve numerical precision in iauPvstar.
  </li>
  <li class="list">
   Check values in the validation program t_sofa_c have been updated due to the change in the astronomical unit.
  </li>
  <li class="list">
   The SOFA Astrometry Tools cookbook sofa_ast_c.pdf:
   <ul>
    <li class="list">
     In the table on page 20 there is a change of +1×10
     <sup>
      -7
     </sup>
     seconds in RA for three results when compared to using the previous value for the au.
                 These cases are repeated on the next three pages.
    </li>
   </ul>
  </li>
 </ul>
</div>
