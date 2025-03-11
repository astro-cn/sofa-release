> The original link of the following content: [http://www.iausofa.org/changes_2023_1011.html](http://www.iausofa.org/changes_2023_1011.html)
<div id="textbox">
 <h3>
  Changes for SOFA Issue: 2023-10-11 (Release 19)
 </h3>
 <h4>
  Summary of Changes
 </h4>
 <p>
  This is the list of updates and changes that are actual errors. Additions, such as including the units "radians", and/or
typographical alterations are not listed. They include changing capitalisation, e.g. AU -&gt; au and Of -&gt; of, and consistent
spelling i.e. catalogue -&gt; catalog.
 </p>
 <h4>
  Corrections to code in the SOFA FORTRAN Library
 </h4>
 <ul>
  <li class="list">
   STARPV &amp; PVSTAR — Code changes to make better use of machine precision
  </li>
 </ul>
 <h4>
  Corrections to code in the SOFA C Library
 </h4>
 <ul>
  <li class="list">
   Starpv &amp; Pvstar — Code changes to make better use of machine precision
  </li>
 </ul>
 <h4>
  Updated parameters in the SOFA FORTRAN Library
 </h4>
 <ul>
  <li class="list">
   DAT — PARAMETER ( IYV = 2023 )
  </li>
 </ul>
 <h4>
  Updated parameters in the SOFA C Library
 </h4>
 <ul>
  <li class="list">
   Dat — enum { IYV = 2023 };
  </li>
 </ul>
 <h4>
  Corrections to  comments in the SOFA FORTRAN Library
 </h4>
 <ol>
  <li class="list">
   A2TF &amp; D2TF — Notes: 3, last line
   <br/>
   <span style="white-space: pre-wrap">
    *     by testing for IHMSF(1)=24 and setting IHMSF(2-4) to zero.
   </span>
   <li class="list">
    ATOIQ — Notes: 1, first line
    <br/>
    <span style="white-space: pre-wrap">
     *  1) "Observed" Az,ZD means ...
    </span>
    <li class="list">
     C2T06A — Notes: 1, 2nd line, i.e. the end of the first sentence is
     <br/>
     <span style="white-space: pre-wrap">
      *     apportioned in any convenient way between the two arguments.
     </span>
     <li class="list">
      FK45Z — Notes: 4, last sentence
      <br/>
      <span style="white-space: pre-wrap">
       *     stars, whether polar or not.  At epoch J2000.0,  ...
      </span>
      <li class="list">
       FK54Z — Notes 3, first line is
       <br/>
       <span style="white-space: pre-wrap">
        3) Conversion from J2000.0 FK5 to B1950.0 FK4 only is provided for.
       </span>
       <li class="list">
        HFK5Z — Notes: 6, first line
        <br/>
        <span style="white-space: pre-wrap">
         6) See also iau_FK52H, iau_H2FK5, iau_FK5HZ.
        </span>
        <li class="list">
         LTPB — Notes: 1, line 3
         <br/>
         <span style="white-space: pre-wrap">
          *     where P_ICRS is a vector in the International Celestial Reference
         </span>
        </li>
       </li>
      </li>
     </li>
    </li>
   </li>
  </li>
 </ol>
 <h4>
  Corrections to comments in the SOFA C Library
 </h4>
 <ol>
  <li class="list">
   A2tf — Note 3, last line
   <br/>
   <span style="white-space: pre-wrap">
    **     by testing for ihmsf[0]=24 and setting ihmsf[1-3] to zero.
   </span>
   <li class="list">
    Atoiq — Notes: 1, first line
    <br/>
    <span style="white-space: pre-wrap">
     **  1) "Observed" Az,ZD means ...
    </span>
    <li class="list">
     C2t06a — Notes: 1, 2nd line, i.e. the end of the first sentence is
     <br/>
     <span style="white-space: pre-wrap">
      &lt; **     apportioned in any convenient way between the two arguments.
     </span>
     <li class="list">
      Fk45z — Notes: 4, last sentence
      <br/>
      <span style="white-space: pre-wrap">
       **     motions for all stars, whether polar or not.  At epoch J2000.0,
      </span>
      <li class="list">
       Fk54z — Notes 3, first line is
       <br/>
       <span style="white-space: pre-wrap">
        **  3) Conversion from J2000.0 FK5 to B1950.0 FK4 only is provided for.
       </span>
       <li class="list">
        Hfk5z — Notes: 6, first line
        <br/>
        <span style="white-space: pre-wrap">
         **  6) See also iauFk52h, iauH2fk5, iauFk5hz.&lt;
        </span>
        <li class="list">
         The test program t_sofa_c.c. In the routine t_atccq the list of called routines is
         <br/>
         <span style="white-space: pre-wrap">
          **  Called:  iauApci13, iauAtccq, vvd
         </span>
        </li>
       </li>
      </li>
     </li>
    </li>
   </li>
  </li>
 </ol>
 <p>
  <b>
   SOFA Release 19
  </b>
  : This changes file was updated on 2023 May 31.
 </p>
</div>
