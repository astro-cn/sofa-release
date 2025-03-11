> The original link of the following content: [http://www.iausofa.org/changes_2021_0512.html](http://www.iausofa.org/changes_2021_0512.html)
<div id="textbox">
 <h3>
  Changes for SOFA Issue: 2021-05-12 (Release 18)
 </h3>
 <h4>
  Summary of Changes
 </h4>
 <p>
  The changes for this major release fall into the following categories:
 </p>
 <ol>
  <li class="list">
   Introduction of three new support routines. Two deal with 
                 calculating astrometric places, while the third provides the 
                 approximate lunar position and velocity. The validation program 
                 has been duly updated.
  </li>
  <li class="list">
   A rearrangement of the ANSI C header files sofam.h and sofa.h. 
                 The consequence of this is that an explicit #include "sofam.h" 
                 has been added to many of the SOFA functions. Thus developers 
                 of applications that use constants from sofa.h will now need to 
                 include an explicit #include &lt;sofam.h&gt;. Further explanation 
                 is given below.
  </li>
  <li class="list">
   The year of validity for the leap second (dat) routine has been 
                 extended.
  </li>
  <li class="list">
   Typographical and other minor corrections to the documentation. 
                 Those that are purely typographical (e.g. punctuation) are not 
                 listed).
  </li>
 </ol>
 <h4>
  Changes to the SOFA FORTRAN Library
 </h4>
 <ol>
  <li class="list">
   iau_ATCC13 — New support routine to transform a star's
                 ICRS catalog entry (epoch J2000.0) into ICRS astrometric place.
   <li class="list">
    iau_ATCCQ — New support routine; a "quick" transformation
                 of a star's ICRS catalog entry (epoch J2000.0) into ICRS
                 astrometric place, given precomputed star-independent astrometry 
                 parameters.
   </li>
   <li class="list">
    iau_dat — Year extended to 2021.
   </li>
   <li class="list">
    iau_G2ICRS &amp; iau_ICRS2G — Documentation updated.
   </li>
   <li class="list">
    iau_MOON98 — New support routine for calculating approximate
                 geocentric position and velocity of the Moon.
   </li>
   <li class="list">
    iau_PLAN94 — Documentation updates and corrections.
   </li>
   <li class="list">
    t_sofa_f — The test program has been updated to include the
                 three new routines.
   </li>
  </li>
 </ol>
 <p>
  N.B. Both iau_MOON98 and iau_PLAN94 provide only approximate positions and do
not use IAU endorsed theories.
 </p>
 <h4>
  Changes to the SOFA ANSI C Library
 </h4>
 <ol>
  <li class="list">
   sofa.h &amp; sofam.h — The information in both these files
                 has been rearranged to eliminate problems encountered by C++
                 developers. The change has
   <br/>
   <ol>
    <li class="list" style="list-style-type: lower-roman">
     moved the structures from sofam.h into sofa.h and
    </li>
    <li class="list" style="list-style-type: lower-roman">
     thus eliminated the #include "sofam.h" from sofa.h.
    </li>
   </ol>
   <p>
    The consequence of this change for SOFA functions is that 
                 an explicit #include "sofam.h" has had to be added to some 
                 of them.
   </p>
   <p>
    Previously, sofam.h contained both structure definitions and
                 constants, and was #included by sofa.h, which was otherwise
                 dedicated to function prototypes. The difficulty was that 
                 short uppercase names in sofam.h were colliding with 
                 C++ variables.
   </p>
   <p>
    The consequence of the change for developers is that any 
                 application that uses constants from sofa.h will now need an 
                 explicit #include &lt;sofam.h&gt;. It should, however, be noted 
                 that the contents of sofam.h are not formally part of the 
                 SOFA API, and so such an application is vulnerable to 
                 future changes. Rather than adding an #include &lt;sofam.h&gt; 
                 to applications, it would be better to replicate the needed 
                 macros in the user code.
   </p>
  </li>
  <li class="list">
   iauAtcc13 — New support function to transform a star's ICRS 
                 catalog entry (epoch J2000.0) into ICRS astrometric place.
   <li class="list">
    iauAtccq — New support function, a "quick" transformation
                 of a star's ICRS catalog entry (epoch J2000.0) into ICRS astrometric 
                 place, given precomputed star-independent astrometry parameters.
   </li>
   <li class="list">
    iauDat — Year extended to 2021.
   </li>
   <li class="list">
    iauG2icrs &amp; iauIcrs2g — Documentation updated.
   </li>
   <li class="list">
    makefile — An error has been corrected when using "make check". 
                 The directory for the include files was incorrect.
   </li>
   <li class="list">
    iauMoon98 — New support function for calculating approximate
                 geocentric position and velocity of the Moon.
   </li>
   <li class="list">
    iauPlan94 — Documentation updates and corrections.
   </li>
   <li class="list">
    t_sofa_c — The test program has been updated to include the
                 three new routines.
   </li>
   <li class="list">
    Cosmetic changes to improve consistency have been made to the ANSI C code.
   </li>
  </li>
 </ol>
 <p>
  N.B. Both iauMoon98 and iauPlan94 provide only approximate positions and do
   not use IAU endorsed theories.
  <p>
   <p>
    The SOFA Board thanks all those who have reported the various issues 
that go to ensuring the libraries and documentation are kept up-to-date
and relevant.
   </p>
   <p>
    <b>
     SOFA Release 18
    </b>
    : This changes file was updated on 2021 May 11.
   </p>
  </p>
 </p>
</div>
