import unittest
from scrapy.selector import Selector
from scrapy.http import HtmlResponse

class Xpath(unittest.TestCase):
    def test_cards(self):
        body = '''
        <div id="ranking-data-load" class="margin-top-20px non-indicators">
         <div class="visible-rows-page-number" pageno="0"></div>
   <div class="ind firstloaded main ranking-row-js-294850" nid="294850">
      <div class="">
         <div class="new-ranking-cards  normal-row">

            <div class="left-div-200">
               <div class="rank-square height-97px dark-blue padding-top-24">
                  <span class="rank-title mobile-upper">Rank</span>
                  <span class="rank-no">
                     1
                     <span class="dagger-icon-new d-none">
                        <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/dagger.svg" alt="Dagger Icon">
                     </span>
                  </span>
               </div>
               <div class="height-1px">
               </div>
               
               


               <div class="rank-square height-163px light-blue padding-top-32 text-align-mobile">
                  
                  

                 

                 


                  <span class="rank-title di-inline">Overall Score:</span>
                  <span class="rank-score di-inline">100</span>
               </div>
            </div>

            <div class="right-div-200">

               <div class="row">
                  <div class="col-lg-7 col-md-12 col-sm-12">
                     <div class="university-details-name">

                        <div class="univ-names-text">
                           <span class="logo-wrapper new-rank ">
                              <a href="/universities/massachusetts-institute-technology-mit">
                                <img fetchpriority="low" loading="lazy" src="https://www.topuniversities.com/sites/default/files/massachusetts-institute-of-technology-mit_410_medium.jpg" alt="Massachusetts Institute of Technology (MIT) " title="Massachusetts Institute of Technology (MIT) " height="78" width="78">
                              </a>
                           </span>

                           <a href="/universities/massachusetts-institute-technology-mit" class="uni-link">Massachusetts Institute of Technology (MIT) </a>

                           <div class="location">
                              <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/location.svg" height="12" width="12" alt="location" title="location"> Cambridge,  United States
                           </div>

                           <div class="stars d-none">
                             <span class="ranking-star">
                               <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/stars.svg" height="20" width="20" alt="QS stars" title="QS stars">
                             </span>
                             <span class="rating_number"></span>
                             <span class="qs-stars-font">QS Stars</span>
                           </div> 



                        </div>
                     </div>
                  </div>

               <div class="col-lg-5 col-md-12 col-sm-12">
                  <div class="shortlist-compare-div">
                     <div class="shortlist_div_new">
                        <a class="wishlist _directorypage shortlistnonloggedglobaljs   _shortlist_nid_294850  shortlistnonloggedglobaljs_dlyr" progoruniv="univ" nid="294850" onclick="Drupal.behaviors.tu_d8._adduniversityShortlist(this, 294850, 'university')">
                           <i class="fa fa-heart" aria-hidden="true"></i>
                           <i class="fal fa-heart" aria-hidden="true"></i>
                           <span class="_addShortText">Shortlist</span>
                        </a>
                     </div>

                     <div class="compare_div_new">
                        <a href="javascript:void(0)" class="compare _globCompUniv_js _globcompare_universityCookie_js_294850 comparenonloggedglobaljs_dlyr" nid="294850" progoruniv="univ" onclick="Drupal.behaviors.tu_d8._adduniversityCompare(this, 294850)">
                           <span class="two-square-icon">
                              <i class="fal fa-circle" aria-hidden="true"></i>
                           </span>
                           <span class="change-text">Compare</span>
                        </a>
                     </div>
                  </div>
               </div>

               </div>



               <div class="new-rankings-tab-content-wrapper">
                  <div class="arrows-left-right-tab arrows-left-right-tab-js">
                     <button class="btn-arrows btn-right-pick btn-arrows-js" scrollnid="294850" direction="right" aria-label="rightButton">
                        <img src="/modules/custom/qs_rankings_rest_api/assets/chevron-right.png" alt="Arrows">
                     </button>
                     <button class="btn-arrows btn-left-pick btn-arrows-js d-none" scrollnid="294850" direction="left" aria-label="leftButton">
                        <img src="/modules/custom/qs_rankings_rest_api/assets/chevron-left.png" alt="Arrows">
                     </button>
                  </div>
                  <ul class="nav nav-tabs m-0 scroll-this-side-294850-js" id="myTab" role="none">
                     <li class="nav-item ">
                                   <a class="nav-link active" id="research-discovery-294850" data-toggle="tab" href="#research-discovery-294850-tab">
                                   Research &amp; Discovery
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="learning-experience-294850" data-toggle="tab" href="#learning-experience-294850-tab">
                                   Learning Experience
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="employability-294850" data-toggle="tab" href="#employability-294850-tab">
                                   Employability
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="global-engagement-294850" data-toggle="tab" href="#global-engagement-294850-tab">
                                   Global Engagement
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="sustainability-294850" data-toggle="tab" href="#sustainability-294850-tab">
                                   Sustainability
                                   </a>
                                </li>
                     <li class="nav-item" role="none">
                        <a class="nav-link" id="more-info-tab-294850" data-toggle="tab" href="#more-info-tab-294850-tab">More Info
                           <span class="new-line">NEW</span>
                           <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/lock.svg" height="14" width="12" alt="lock" title="lock" class="lock-icon-checked-js d-none">
                        </a>
                     </li>
                  </ul>
                  <div class="tab-content py-2" id="myTabContent">

                     <div class="tab-pane fade show active" id="research-discovery-294850-tab" role="tabpanel" aria-labelledby="research-discovery-294850">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Academic Reputation</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="academic-reputation" role="progressbar" aria-label="progress" title="academic-reputation" aria-labelledby="academic-reputation" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">100</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Citations per Faculty</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="citations-per-faculty" role="progressbar" aria-label="progress" title="citations-per-faculty" aria-labelledby="citations-per-faculty" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">100</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="learning-experience-294850-tab" role="tabpanel" aria-labelledby="learning-experience-294850">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Faculty Student Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="faculty-student-ratio" role="progressbar" aria-label="progress" title="faculty-student-ratio" aria-labelledby="faculty-student-ratio" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">100</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="employability-294850-tab" role="tabpanel" aria-labelledby="employability-294850">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Employer Reputation</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="employer-reputation" role="progressbar" aria-label="progress" title="employer-reputation" aria-labelledby="employer-reputation" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">100</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Employment Outcomes</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="employment-outcomes" role="progressbar" aria-label="progress" title="employment-outcomes" aria-labelledby="employment-outcomes" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">100</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="global-engagement-294850-tab" role="tabpanel" aria-labelledby="global-engagement-294850">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Student Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-student-ratio" role="progressbar" aria-label="progress" title="international-student-ratio" aria-labelledby="international-student-ratio" style="width: 86.8%" aria-valuenow="86.8" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">86.8</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Research Network</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-research-network" role="progressbar" aria-label="progress" title="international-research-network" aria-labelledby="international-research-network" style="width: 96%" aria-valuenow="96" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">96</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Faculty Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-faculty-ratio" role="progressbar" aria-label="progress" title="international-faculty-ratio" aria-labelledby="international-faculty-ratio" style="width: 99.3%" aria-valuenow="99.3" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">99.3</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="sustainability-294850-tab" role="tabpanel" aria-labelledby="sustainability-294850">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Sustainability Score</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="sustainability-score" role="progressbar" aria-label="progress" title="sustainability-score" aria-labelledby="sustainability-score" style="width: 99%" aria-valuenow="99" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">99</div>
                           </div>
                        </div>
                         </div>
                      </div>

                     <div class="tab-pane fade" id="more-info-tab-294850-tab" role="tabpanel" aria-labelledby="more-info-tab-294850">
                        <div class="new-rankings-indicator-wrap py-2">

                           <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Fees</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                -
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Scholarship</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                No
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Student Mix</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                Domestic 67%   International 33%
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">English Tests</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                <a href="javascript:void(0)" class="_openfilter_results_js">Generate Result</a>
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Academic Tests</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                <a href="javascript:void(0)" class="_openfilter_results_js">Generate Result</a>
                              </div>
                           </div>
                        </div>


                        </div>

                        <div class="signup-for-user signup-for-user-js d-none">
                           <p>In order to see the data <a href="javascript:void(0)" class="signup-for-user-js-dlyr" data-toggle="modal" data-target="#emailModal">Sign up for free</a></p>
                        </div>


                     </div>

                  </div>
               </div>


            </div>

         </div>
      </div>
   </div>

   <div class="ind firstloaded main ranking-row-js-294030" nid="294030">
      <div class="">
         <div class="new-ranking-cards advanced_profile new normal-row">

            <div class="left-div-200">
               <div class="rank-square height-97px dark-blue padding-top-24">
                  <span class="rank-title mobile-upper">Rank</span>
                  <span class="rank-no">
                     2
                     <span class="dagger-icon-new d-none">
                        <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/dagger.svg" alt="Dagger Icon">
                     </span>
                  </span>
               </div>
               <div class="height-1px">
               </div>
               
               


               <div class="rank-square height-163px light-blue padding-top-32 text-align-mobile">
                  
                  

                 

                 


                  <span class="rank-title di-inline">Overall Score:</span>
                  <span class="rank-score di-inline">98.5</span>
               </div>
            </div>

            <div class="right-div-200">

               <div class="row">
                  <div class="col-lg-7 col-md-12 col-sm-12">
                     <div class="university-details-name">

                        <div class="univ-names-text">
                           <span class="logo-wrapper new-rank ">
                              <a href="/universities/imperial-college-london">
                                <img fetchpriority="low" loading="lazy" src="https://www.topuniversities.com/sites/default/files/240430033452pm869301QS-Imperial-Logo-white-text-blue-background-90x90.jpg" alt="Imperial College London" title="Imperial College London" height="78" width="78">
                              </a>
                           </span>

                           <a href="/universities/imperial-college-london" class="uni-link">Imperial College London</a>

                           <div class="location">
                              <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/location.svg" height="12" width="12" alt="location" title="location"> London,  United Kingdom
                           </div>

                           <div class="stars d-none">
                             <span class="ranking-star">
                               <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/stars.svg" height="20" width="20" alt="QS stars" title="QS stars">
                             </span>
                             <span class="rating_number"></span>
                             <span class="qs-stars-font">QS Stars</span>
                           </div> 



                        </div>
                     </div>
                  </div>

               <div class="col-lg-5 col-md-12 col-sm-12">
                  <div class="shortlist-compare-div">
                     <div class="shortlist_div_new">
                        <a class="wishlist _directorypage shortlistnonloggedglobaljs   _shortlist_nid_294030  shortlistnonloggedglobaljs_dlyr" progoruniv="univ" nid="294030" onclick="Drupal.behaviors.tu_d8._adduniversityShortlist(this, 294030, 'university')">
                           <i class="fa fa-heart" aria-hidden="true"></i>
                           <i class="fal fa-heart" aria-hidden="true"></i>
                           <span class="_addShortText">Shortlist</span>
                        </a>
                     </div>

                     <div class="compare_div_new">
                        <a href="javascript:void(0)" class="compare _globCompUniv_js _globcompare_universityCookie_js_294030 comparenonloggedglobaljs_dlyr" nid="294030" progoruniv="univ" onclick="Drupal.behaviors.tu_d8._adduniversityCompare(this, 294030)">
                           <span class="two-square-icon">
                              <i class="fal fa-circle" aria-hidden="true"></i>
                           </span>
                           <span class="change-text">Compare</span>
                        </a>
                     </div>
                  </div>
               </div>

               </div>



               <div class="new-rankings-tab-content-wrapper">
                  <div class="arrows-left-right-tab arrows-left-right-tab-js">
                     <button class="btn-arrows btn-right-pick btn-arrows-js" scrollnid="294030" direction="right" aria-label="rightButton">
                        <img src="/modules/custom/qs_rankings_rest_api/assets/chevron-right.png" alt="Arrows">
                     </button>
                     <button class="btn-arrows btn-left-pick btn-arrows-js d-none" scrollnid="294030" direction="left" aria-label="leftButton">
                        <img src="/modules/custom/qs_rankings_rest_api/assets/chevron-left.png" alt="Arrows">
                     </button>
                  </div>
                  <ul class="nav nav-tabs m-0 scroll-this-side-294030-js" id="myTab" role="none">
                     <li class="nav-item ">
                                   <a class="nav-link active" id="research-discovery-294030" data-toggle="tab" href="#research-discovery-294030-tab">
                                   Research &amp; Discovery
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="learning-experience-294030" data-toggle="tab" href="#learning-experience-294030-tab">
                                   Learning Experience
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="employability-294030" data-toggle="tab" href="#employability-294030-tab">
                                   Employability
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="global-engagement-294030" data-toggle="tab" href="#global-engagement-294030-tab">
                                   Global Engagement
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="sustainability-294030" data-toggle="tab" href="#sustainability-294030-tab">
                                   Sustainability
                                   </a>
                                </li>
                     <li class="nav-item" role="none">
                        <a class="nav-link" id="more-info-tab-294030" data-toggle="tab" href="#more-info-tab-294030-tab">More Info
                           <span class="new-line">NEW</span>
                           <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/lock.svg" height="14" width="12" alt="lock" title="lock" class="lock-icon-checked-js d-none">
                        </a>
                     </li>
                  </ul>
                  <div class="tab-content py-2" id="myTabContent">

                     <div class="tab-pane fade show active" id="research-discovery-294030-tab" role="tabpanel" aria-labelledby="research-discovery-294030">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Academic Reputation</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="academic-reputation" role="progressbar" aria-label="progress" title="academic-reputation" aria-labelledby="academic-reputation" style="width: 98.5%" aria-valuenow="98.5" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">98.5</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Citations per Faculty</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="citations-per-faculty" role="progressbar" aria-label="progress" title="citations-per-faculty" aria-labelledby="citations-per-faculty" style="width: 93.9%" aria-valuenow="93.9" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">93.9</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="learning-experience-294030-tab" role="tabpanel" aria-labelledby="learning-experience-294030">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Faculty Student Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="faculty-student-ratio" role="progressbar" aria-label="progress" title="faculty-student-ratio" aria-labelledby="faculty-student-ratio" style="width: 98.2%" aria-valuenow="98.2" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">98.2</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="employability-294030-tab" role="tabpanel" aria-labelledby="employability-294030">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Employer Reputation</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="employer-reputation" role="progressbar" aria-label="progress" title="employer-reputation" aria-labelledby="employer-reputation" style="width: 99.5%" aria-valuenow="99.5" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">99.5</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Employment Outcomes</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="employment-outcomes" role="progressbar" aria-label="progress" title="employment-outcomes" aria-labelledby="employment-outcomes" style="width: 93.4%" aria-valuenow="93.4" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">93.4</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="global-engagement-294030-tab" role="tabpanel" aria-labelledby="global-engagement-294030">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Student Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-student-ratio" role="progressbar" aria-label="progress" title="international-student-ratio" aria-labelledby="international-student-ratio" style="width: 99.6%" aria-valuenow="99.6" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">99.6</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Research Network</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-research-network" role="progressbar" aria-label="progress" title="international-research-network" aria-labelledby="international-research-network" style="width: 97.4%" aria-valuenow="97.4" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">97.4</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Faculty Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-faculty-ratio" role="progressbar" aria-label="progress" title="international-faculty-ratio" aria-labelledby="international-faculty-ratio" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">100</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="sustainability-294030-tab" role="tabpanel" aria-labelledby="sustainability-294030">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Sustainability Score</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="sustainability-score" role="progressbar" aria-label="progress" title="sustainability-score" aria-labelledby="sustainability-score" style="width: 99.7%" aria-valuenow="99.7" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">99.7</div>
                           </div>
                        </div>
                         </div>
                      </div>

                     <div class="tab-pane fade" id="more-info-tab-294030-tab" role="tabpanel" aria-labelledby="more-info-tab-294030">
                        <div class="new-rankings-indicator-wrap py-2">

                           <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Fees</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                35000(GBP)
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Scholarship</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                Yes
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Student Mix</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                Domestic 55%   International 45%
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">English Tests</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                <a href="javascript:void(0)" class="_openfilter_results_js">Generate Result</a>
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Academic Tests</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                <a href="javascript:void(0)" class="_openfilter_results_js">Generate Result</a>
                              </div>
                           </div>
                        </div>


                        </div>

                        <div class="signup-for-user signup-for-user-js d-none">
                           <p>In order to see the data <a href="javascript:void(0)" class="signup-for-user-js-dlyr" data-toggle="modal" data-target="#emailModal">Sign up for free</a></p>
                        </div>


                     </div>

                  </div>
               </div>


            </div>

         </div>
      </div>
   </div>

   <div class="ind firstloaded main ranking-row-js-294654" nid="294654">
      <div class="">
         <div class="new-ranking-cards  normal-row">

            <div class="left-div-200">
               <div class="rank-square height-97px dark-blue padding-top-24">
                  <span class="rank-title mobile-upper">Rank</span>
                  <span class="rank-no">
                     3
                     <span class="dagger-icon-new d-none">
                        <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/dagger.svg" alt="Dagger Icon">
                     </span>
                  </span>
               </div>
               <div class="height-1px">
               </div>
               
               


               <div class="rank-square height-163px light-blue padding-top-32 text-align-mobile">
                  
                  

                 

                 


                  <span class="rank-title di-inline">Overall Score:</span>
                  <span class="rank-score di-inline">96.9</span>
               </div>
            </div>

            <div class="right-div-200">

               <div class="row">
                  <div class="col-lg-7 col-md-12 col-sm-12">
                     <div class="university-details-name">

                        <div class="univ-names-text">
                           <span class="logo-wrapper new-rank ">
                              <a href="/universities/university-oxford">
                                <img fetchpriority="low" loading="lazy" src="https://www.topuniversities.com/sites/default/files/university-of-oxford_478_medium.jpg" alt="University of Oxford" title="University of Oxford" height="78" width="78">
                              </a>
                           </span>

                           <a href="/universities/university-oxford" class="uni-link">University of Oxford</a>

                           <div class="location">
                              <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/location.svg" height="12" width="12" alt="location" title="location"> Oxford,  United Kingdom
                           </div>

                           <div class="stars d-none">
                             <span class="ranking-star">
                               <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/stars.svg" height="20" width="20" alt="QS stars" title="QS stars">
                             </span>
                             <span class="rating_number"></span>
                             <span class="qs-stars-font">QS Stars</span>
                           </div> 



                        </div>
                     </div>
                  </div>

               <div class="col-lg-5 col-md-12 col-sm-12">
                  <div class="shortlist-compare-div">
                     <div class="shortlist_div_new">
                        <a class="wishlist _directorypage shortlistnonloggedglobaljs   _shortlist_nid_294654  shortlistnonloggedglobaljs_dlyr" progoruniv="univ" nid="294654" onclick="Drupal.behaviors.tu_d8._adduniversityShortlist(this, 294654, 'university')">
                           <i class="fa fa-heart" aria-hidden="true"></i>
                           <i class="fal fa-heart" aria-hidden="true"></i>
                           <span class="_addShortText">Shortlist</span>
                        </a>
                     </div>

                     <div class="compare_div_new">
                        <a href="javascript:void(0)" class="compare _globCompUniv_js _globcompare_universityCookie_js_294654 comparenonloggedglobaljs_dlyr" nid="294654" progoruniv="univ" onclick="Drupal.behaviors.tu_d8._adduniversityCompare(this, 294654)">
                           <span class="two-square-icon">
                              <i class="fal fa-circle" aria-hidden="true"></i>
                           </span>
                           <span class="change-text">Compare</span>
                        </a>
                     </div>
                  </div>
               </div>

               </div>



               <div class="new-rankings-tab-content-wrapper">
                  <div class="arrows-left-right-tab arrows-left-right-tab-js">
                     <button class="btn-arrows btn-right-pick btn-arrows-js" scrollnid="294654" direction="right" aria-label="rightButton">
                        <img src="/modules/custom/qs_rankings_rest_api/assets/chevron-right.png" alt="Arrows">
                     </button>
                     <button class="btn-arrows btn-left-pick btn-arrows-js d-none" scrollnid="294654" direction="left" aria-label="leftButton">
                        <img src="/modules/custom/qs_rankings_rest_api/assets/chevron-left.png" alt="Arrows">
                     </button>
                  </div>
                  <ul class="nav nav-tabs m-0 scroll-this-side-294654-js" id="myTab" role="none">
                     <li class="nav-item ">
                                   <a class="nav-link active" id="research-discovery-294654" data-toggle="tab" href="#research-discovery-294654-tab">
                                   Research &amp; Discovery
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="learning-experience-294654" data-toggle="tab" href="#learning-experience-294654-tab">
                                   Learning Experience
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="employability-294654" data-toggle="tab" href="#employability-294654-tab">
                                   Employability
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="global-engagement-294654" data-toggle="tab" href="#global-engagement-294654-tab">
                                   Global Engagement
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="sustainability-294654" data-toggle="tab" href="#sustainability-294654-tab">
                                   Sustainability
                                   </a>
                                </li>
                     <li class="nav-item" role="none">
                        <a class="nav-link" id="more-info-tab-294654" data-toggle="tab" href="#more-info-tab-294654-tab">More Info
                           <span class="new-line">NEW</span>
                           <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/lock.svg" height="14" width="12" alt="lock" title="lock" class="lock-icon-checked-js d-none">
                        </a>
                     </li>
                  </ul>
                  <div class="tab-content py-2" id="myTabContent">

                     <div class="tab-pane fade show active" id="research-discovery-294654-tab" role="tabpanel" aria-labelledby="research-discovery-294654">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Academic Reputation</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="academic-reputation" role="progressbar" aria-label="progress" title="academic-reputation" aria-labelledby="academic-reputation" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">100</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Citations per Faculty</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="citations-per-faculty" role="progressbar" aria-label="progress" title="citations-per-faculty" aria-labelledby="citations-per-faculty" style="width: 84.8%" aria-valuenow="84.8" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">84.8</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="learning-experience-294654-tab" role="tabpanel" aria-labelledby="learning-experience-294654">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Faculty Student Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="faculty-student-ratio" role="progressbar" aria-label="progress" title="faculty-student-ratio" aria-labelledby="faculty-student-ratio" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">100</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="employability-294654-tab" role="tabpanel" aria-labelledby="employability-294654">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Employer Reputation</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="employer-reputation" role="progressbar" aria-label="progress" title="employer-reputation" aria-labelledby="employer-reputation" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">100</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Employment Outcomes</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="employment-outcomes" role="progressbar" aria-label="progress" title="employment-outcomes" aria-labelledby="employment-outcomes" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">100</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="global-engagement-294654-tab" role="tabpanel" aria-labelledby="global-engagement-294654">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Student Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-student-ratio" role="progressbar" aria-label="progress" title="international-student-ratio" aria-labelledby="international-student-ratio" style="width: 97.7%" aria-valuenow="97.7" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">97.7</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Research Network</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-research-network" role="progressbar" aria-label="progress" title="international-research-network" aria-labelledby="international-research-network" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">100</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Faculty Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-faculty-ratio" role="progressbar" aria-label="progress" title="international-faculty-ratio" aria-labelledby="international-faculty-ratio" style="width: 98.1%" aria-valuenow="98.1" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">98.1</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="sustainability-294654-tab" role="tabpanel" aria-labelledby="sustainability-294654">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Sustainability Score</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="sustainability-score" role="progressbar" aria-label="progress" title="sustainability-score" aria-labelledby="sustainability-score" style="width: 85%" aria-valuenow="85" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">85</div>
                           </div>
                        </div>
                         </div>
                      </div>

                     <div class="tab-pane fade" id="more-info-tab-294654-tab" role="tabpanel" aria-labelledby="more-info-tab-294654">
                        <div class="new-rankings-indicator-wrap py-2">

                           <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Fees</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                -
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Scholarship</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                Yes
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Student Mix</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                Domestic 59%   International 41%
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">English Tests</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                <a href="javascript:void(0)" class="_openfilter_results_js">Generate Result</a>
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Academic Tests</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                <a href="javascript:void(0)" class="_openfilter_results_js">Generate Result</a>
                              </div>
                           </div>
                        </div>


                        </div>

                        <div class="signup-for-user signup-for-user-js d-none">
                           <p>In order to see the data <a href="javascript:void(0)" class="signup-for-user-js-dlyr" data-toggle="modal" data-target="#emailModal">Sign up for free</a></p>
                        </div>


                     </div>

                  </div>
               </div>


            </div>

         </div>
      </div>
   </div><div class="row need-section-margin dynamic-block-ranking-1" position="3" customblock="true">
  <div class="_ifdfp_1 _ifdfp_1_divcss scroll-in-mobile td-wrap col-lg-12">
                       
             <div id="js-dfp-tag-responsive_ad_1" class="text-center" data-google-query-id="CPXtjr6m04oDFT1ZwgUd2F4t_w">
               
              <div id="google_ads_iframe_8070/Topuni-Web/world-university-rankings_0__container__" style="border: 0pt none;"><iframe id="google_ads_iframe_8070/Topuni-Web/world-university-rankings_0" name="google_ads_iframe_8070/Topuni-Web/world-university-rankings_0" title="3rd party ad content" width="750" height="200" scrolling="no" marginwidth="0" marginheight="0" frameborder="0" aria-label="Advertisement" tabindex="0" allow="private-state-token-redemption;attribution-reporting" data-load-complete="true" data-google-container-id="6" style="border: 0px; vertical-align: bottom; visibility: visible;"></iframe></div></div>
                          </div>
</div>

   <div class="ind firstloaded main ranking-row-js-294270" nid="294270">
      <div class="">
         <div class="new-ranking-cards  normal-row">

            <div class="left-div-200">
               <div class="rank-square height-97px dark-blue padding-top-24">
                  <span class="rank-title mobile-upper">Rank</span>
                  <span class="rank-no">
                     4
                     <span class="dagger-icon-new d-none">
                        <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/dagger.svg" alt="Dagger Icon">
                     </span>
                  </span>
               </div>
               <div class="height-1px">
               </div>
               
               


               <div class="rank-square height-163px light-blue padding-top-32 text-align-mobile">
                  
                  

                 

                 


                  <span class="rank-title di-inline">Overall Score:</span>
                  <span class="rank-score di-inline">96.8</span>
               </div>
            </div>

            <div class="right-div-200">

               <div class="row">
                  <div class="col-lg-7 col-md-12 col-sm-12">
                     <div class="university-details-name">

                        <div class="univ-names-text">
                           <span class="logo-wrapper new-rank ">
                              <a href="/universities/harvard-university">
                                <img fetchpriority="low" loading="lazy" src="https://www.topuniversities.com/sites/default/files/harvard-university_253_medium.jpg" alt="Harvard University" title="Harvard University" height="78" width="78">
                              </a>
                           </span>

                           <a href="/universities/harvard-university" class="uni-link">Harvard University</a>

                           <div class="location">
                              <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/location.svg" height="12" width="12" alt="location" title="location"> Cambridge,  United States
                           </div>

                           <div class="stars d-none">
                             <span class="ranking-star">
                               <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/stars.svg" height="20" width="20" alt="QS stars" title="QS stars">
                             </span>
                             <span class="rating_number"></span>
                             <span class="qs-stars-font">QS Stars</span>
                           </div> 



                        </div>
                     </div>
                  </div>

               <div class="col-lg-5 col-md-12 col-sm-12">
                  <div class="shortlist-compare-div">
                     <div class="shortlist_div_new">
                        <a class="wishlist _directorypage shortlistnonloggedglobaljs   _shortlist_nid_294270  shortlistnonloggedglobaljs_dlyr" progoruniv="univ" nid="294270" onclick="Drupal.behaviors.tu_d8._adduniversityShortlist(this, 294270, 'university')">
                           <i class="fa fa-heart" aria-hidden="true"></i>
                           <i class="fal fa-heart" aria-hidden="true"></i>
                           <span class="_addShortText">Shortlist</span>
                        </a>
                     </div>

                     <div class="compare_div_new">
                        <a href="javascript:void(0)" class="compare _globCompUniv_js _globcompare_universityCookie_js_294270 comparenonloggedglobaljs_dlyr" nid="294270" progoruniv="univ" onclick="Drupal.behaviors.tu_d8._adduniversityCompare(this, 294270)">
                           <span class="two-square-icon">
                              <i class="fal fa-circle" aria-hidden="true"></i>
                           </span>
                           <span class="change-text">Compare</span>
                        </a>
                     </div>
                  </div>
               </div>

               </div>



               <div class="new-rankings-tab-content-wrapper">
                  <div class="arrows-left-right-tab arrows-left-right-tab-js">
                     <button class="btn-arrows btn-right-pick btn-arrows-js" scrollnid="294270" direction="right" aria-label="rightButton">
                        <img src="/modules/custom/qs_rankings_rest_api/assets/chevron-right.png" alt="Arrows">
                     </button>
                     <button class="btn-arrows btn-left-pick btn-arrows-js d-none" scrollnid="294270" direction="left" aria-label="leftButton">
                        <img src="/modules/custom/qs_rankings_rest_api/assets/chevron-left.png" alt="Arrows">
                     </button>
                  </div>
                  <ul class="nav nav-tabs m-0 scroll-this-side-294270-js" id="myTab" role="none">
                     <li class="nav-item ">
                                   <a class="nav-link active" id="research-discovery-294270" data-toggle="tab" href="#research-discovery-294270-tab">
                                   Research &amp; Discovery
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="learning-experience-294270" data-toggle="tab" href="#learning-experience-294270-tab">
                                   Learning Experience
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="employability-294270" data-toggle="tab" href="#employability-294270-tab">
                                   Employability
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="global-engagement-294270" data-toggle="tab" href="#global-engagement-294270-tab">
                                   Global Engagement
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="sustainability-294270" data-toggle="tab" href="#sustainability-294270-tab">
                                   Sustainability
                                   </a>
                                </li>
                     <li class="nav-item" role="none">
                        <a class="nav-link" id="more-info-tab-294270" data-toggle="tab" href="#more-info-tab-294270-tab">More Info
                           <span class="new-line">NEW</span>
                           <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/lock.svg" height="14" width="12" alt="lock" title="lock" class="lock-icon-checked-js d-none">
                        </a>
                     </li>
                  </ul>
                  <div class="tab-content py-2" id="myTabContent">

                     <div class="tab-pane fade show active" id="research-discovery-294270-tab" role="tabpanel" aria-labelledby="research-discovery-294270">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Academic Reputation</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="academic-reputation" role="progressbar" aria-label="progress" title="academic-reputation" aria-labelledby="academic-reputation" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">100</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Citations per Faculty</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="citations-per-faculty" role="progressbar" aria-label="progress" title="citations-per-faculty" aria-labelledby="citations-per-faculty" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">100</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="learning-experience-294270-tab" role="tabpanel" aria-labelledby="learning-experience-294270">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Faculty Student Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="faculty-student-ratio" role="progressbar" aria-label="progress" title="faculty-student-ratio" aria-labelledby="faculty-student-ratio" style="width: 96.3%" aria-valuenow="96.3" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">96.3</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="employability-294270-tab" role="tabpanel" aria-labelledby="employability-294270">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Employer Reputation</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="employer-reputation" role="progressbar" aria-label="progress" title="employer-reputation" aria-labelledby="employer-reputation" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">100</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Employment Outcomes</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="employment-outcomes" role="progressbar" aria-label="progress" title="employment-outcomes" aria-labelledby="employment-outcomes" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">100</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="global-engagement-294270-tab" role="tabpanel" aria-labelledby="global-engagement-294270">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Student Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-student-ratio" role="progressbar" aria-label="progress" title="international-student-ratio" aria-labelledby="international-student-ratio" style="width: 69%" aria-valuenow="69" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">69</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Research Network</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-research-network" role="progressbar" aria-label="progress" title="international-research-network" aria-labelledby="international-research-network" style="width: 99.6%" aria-valuenow="99.6" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">99.6</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Faculty Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-faculty-ratio" role="progressbar" aria-label="progress" title="international-faculty-ratio" aria-labelledby="international-faculty-ratio" style="width: 74.1%" aria-valuenow="74.1" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">74.1</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="sustainability-294270-tab" role="tabpanel" aria-labelledby="sustainability-294270">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Sustainability Score</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="sustainability-score" role="progressbar" aria-label="progress" title="sustainability-score" aria-labelledby="sustainability-score" style="width: 84.4%" aria-valuenow="84.4" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">84.4</div>
                           </div>
                        </div>
                         </div>
                      </div>

                     <div class="tab-pane fade" id="more-info-tab-294270-tab" role="tabpanel" aria-labelledby="more-info-tab-294270">
                        <div class="new-rankings-indicator-wrap py-2">

                           <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Fees</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                -
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Scholarship</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                No
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Student Mix</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                Domestic 73%   International 27%
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">English Tests</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                <a href="javascript:void(0)" class="_openfilter_results_js">Generate Result</a>
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Academic Tests</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                <a href="javascript:void(0)" class="_openfilter_results_js">Generate Result</a>
                              </div>
                           </div>
                        </div>


                        </div>

                        <div class="signup-for-user signup-for-user-js d-none">
                           <p>In order to see the data <a href="javascript:void(0)" class="signup-for-user-js-dlyr" data-toggle="modal" data-target="#emailModal">Sign up for free</a></p>
                        </div>


                     </div>

                  </div>
               </div>


            </div>

         </div>
      </div>
   </div>

   <div class="ind firstloaded main ranking-row-js-294561" nid="294561">
      <div class="">
         <div class="new-ranking-cards  normal-row">

            <div class="left-div-200">
               <div class="rank-square height-97px dark-blue padding-top-24">
                  <span class="rank-title mobile-upper">Rank</span>
                  <span class="rank-no">
                     5
                     <span class="dagger-icon-new d-none">
                        <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/dagger.svg" alt="Dagger Icon">
                     </span>
                  </span>
               </div>
               <div class="height-1px">
               </div>
               
               


               <div class="rank-square height-163px light-blue padding-top-32 text-align-mobile">
                  
                  

                 

                 


                  <span class="rank-title di-inline">Overall Score:</span>
                  <span class="rank-score di-inline">96.7</span>
               </div>
            </div>

            <div class="right-div-200">

               <div class="row">
                  <div class="col-lg-7 col-md-12 col-sm-12">
                     <div class="university-details-name">

                        <div class="univ-names-text">
                           <span class="logo-wrapper new-rank ">
                              <a href="/universities/university-cambridge">
                                <img fetchpriority="low" loading="lazy" src="https://www.topuniversities.com/sites/default/files/university-of-cambridge_95_medium.jpg" alt="University of Cambridge" title="University of Cambridge" height="78" width="78">
                              </a>
                           </span>

                           <a href="/universities/university-cambridge" class="uni-link">University of Cambridge</a>

                           <div class="location">
                              <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/location.svg" height="12" width="12" alt="location" title="location"> Cambridge,  United Kingdom
                           </div>

                           <div class="stars d-none">
                             <span class="ranking-star">
                               <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/stars.svg" height="20" width="20" alt="QS stars" title="QS stars">
                             </span>
                             <span class="rating_number"></span>
                             <span class="qs-stars-font">QS Stars</span>
                           </div> 



                        </div>
                     </div>
                  </div>

               <div class="col-lg-5 col-md-12 col-sm-12">
                  <div class="shortlist-compare-div">
                     <div class="shortlist_div_new">
                        <a class="wishlist _directorypage shortlistnonloggedglobaljs   _shortlist_nid_294561  shortlistnonloggedglobaljs_dlyr" progoruniv="univ" nid="294561" onclick="Drupal.behaviors.tu_d8._adduniversityShortlist(this, 294561, 'university')">
                           <i class="fa fa-heart" aria-hidden="true"></i>
                           <i class="fal fa-heart" aria-hidden="true"></i>
                           <span class="_addShortText">Shortlist</span>
                        </a>
                     </div>

                     <div class="compare_div_new">
                        <a href="javascript:void(0)" class="compare _globCompUniv_js _globcompare_universityCookie_js_294561 comparenonloggedglobaljs_dlyr" nid="294561" progoruniv="univ" onclick="Drupal.behaviors.tu_d8._adduniversityCompare(this, 294561)">
                           <span class="two-square-icon">
                              <i class="fal fa-circle" aria-hidden="true"></i>
                           </span>
                           <span class="change-text">Compare</span>
                        </a>
                     </div>
                  </div>
               </div>

               </div>



               <div class="new-rankings-tab-content-wrapper">
                  <div class="arrows-left-right-tab arrows-left-right-tab-js">
                     <button class="btn-arrows btn-right-pick btn-arrows-js" scrollnid="294561" direction="right" aria-label="rightButton">
                        <img src="/modules/custom/qs_rankings_rest_api/assets/chevron-right.png" alt="Arrows">
                     </button>
                     <button class="btn-arrows btn-left-pick btn-arrows-js d-none" scrollnid="294561" direction="left" aria-label="leftButton">
                        <img src="/modules/custom/qs_rankings_rest_api/assets/chevron-left.png" alt="Arrows">
                     </button>
                  </div>
                  <ul class="nav nav-tabs m-0 scroll-this-side-294561-js" id="myTab" role="none">
                     <li class="nav-item ">
                                   <a class="nav-link active" id="research-discovery-294561" data-toggle="tab" href="#research-discovery-294561-tab">
                                   Research &amp; Discovery
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="learning-experience-294561" data-toggle="tab" href="#learning-experience-294561-tab">
                                   Learning Experience
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="employability-294561" data-toggle="tab" href="#employability-294561-tab">
                                   Employability
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="global-engagement-294561" data-toggle="tab" href="#global-engagement-294561-tab">
                                   Global Engagement
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="sustainability-294561" data-toggle="tab" href="#sustainability-294561-tab">
                                   Sustainability
                                   </a>
                                </li>
                     <li class="nav-item" role="none">
                        <a class="nav-link" id="more-info-tab-294561" data-toggle="tab" href="#more-info-tab-294561-tab">More Info
                           <span class="new-line">NEW</span>
                           <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/lock.svg" height="14" width="12" alt="lock" title="lock" class="lock-icon-checked-js d-none">
                        </a>
                     </li>
                  </ul>
                  <div class="tab-content py-2" id="myTabContent">

                     <div class="tab-pane fade show active" id="research-discovery-294561-tab" role="tabpanel" aria-labelledby="research-discovery-294561">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Academic Reputation</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="academic-reputation" role="progressbar" aria-label="progress" title="academic-reputation" aria-labelledby="academic-reputation" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">100</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Citations per Faculty</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="citations-per-faculty" role="progressbar" aria-label="progress" title="citations-per-faculty" aria-labelledby="citations-per-faculty" style="width: 84.6%" aria-valuenow="84.6" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">84.6</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="learning-experience-294561-tab" role="tabpanel" aria-labelledby="learning-experience-294561">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Faculty Student Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="faculty-student-ratio" role="progressbar" aria-label="progress" title="faculty-student-ratio" aria-labelledby="faculty-student-ratio" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">100</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="employability-294561-tab" role="tabpanel" aria-labelledby="employability-294561">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Employer Reputation</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="employer-reputation" role="progressbar" aria-label="progress" title="employer-reputation" aria-labelledby="employer-reputation" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">100</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Employment Outcomes</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="employment-outcomes" role="progressbar" aria-label="progress" title="employment-outcomes" aria-labelledby="employment-outcomes" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">100</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="global-engagement-294561-tab" role="tabpanel" aria-labelledby="global-engagement-294561">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Student Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-student-ratio" role="progressbar" aria-label="progress" title="international-student-ratio" aria-labelledby="international-student-ratio" style="width: 94.8%" aria-valuenow="94.8" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">94.8</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Research Network</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-research-network" role="progressbar" aria-label="progress" title="international-research-network" aria-labelledby="international-research-network" style="width: 99.3%" aria-valuenow="99.3" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">99.3</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Faculty Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-faculty-ratio" role="progressbar" aria-label="progress" title="international-faculty-ratio" aria-labelledby="international-faculty-ratio" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">100</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="sustainability-294561-tab" role="tabpanel" aria-labelledby="sustainability-294561">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Sustainability Score</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="sustainability-score" role="progressbar" aria-label="progress" title="sustainability-score" aria-labelledby="sustainability-score" style="width: 84.8%" aria-valuenow="84.8" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">84.8</div>
                           </div>
                        </div>
                         </div>
                      </div>

                     <div class="tab-pane fade" id="more-info-tab-294561-tab" role="tabpanel" aria-labelledby="more-info-tab-294561">
                        <div class="new-rankings-indicator-wrap py-2">

                           <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Fees</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                -
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Scholarship</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                Yes
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Student Mix</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                Domestic 62%   International 38%
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">English Tests</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                <a href="javascript:void(0)" class="_openfilter_results_js">Generate Result</a>
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Academic Tests</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                <a href="javascript:void(0)" class="_openfilter_results_js">Generate Result</a>
                              </div>
                           </div>
                        </div>


                        </div>

                        <div class="signup-for-user signup-for-user-js d-none">
                           <p>In order to see the data <a href="javascript:void(0)" class="signup-for-user-js-dlyr" data-toggle="modal" data-target="#emailModal">Sign up for free</a></p>
                        </div>


                     </div>

                  </div>
               </div>


            </div>

         </div>
      </div>
   </div>

   <div class="ind firstloaded main ranking-row-js-297282" nid="297282">
      <div class="">
         <div class="new-ranking-cards  normal-row">

            <div class="left-div-200">
               <div class="rank-square height-97px dark-blue padding-top-24">
                  <span class="rank-title mobile-upper">Rank</span>
                  <span class="rank-no">
                     6
                     <span class="dagger-icon-new d-none">
                        <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/dagger.svg" alt="Dagger Icon">
                     </span>
                  </span>
               </div>
               <div class="height-1px">
               </div>
               
               


               <div class="rank-square height-163px light-blue padding-top-32 text-align-mobile">
                  
                  

                 

                 


                  <span class="rank-title di-inline">Overall Score:</span>
                  <span class="rank-score di-inline">96.1</span>
               </div>
            </div>

            <div class="right-div-200">

               <div class="row">
                  <div class="col-lg-7 col-md-12 col-sm-12">
                     <div class="university-details-name">

                        <div class="univ-names-text">
                           <span class="logo-wrapper new-rank ">
                              <a href="/universities/stanford-university">
                                <img fetchpriority="low" loading="lazy" src="https://www.topuniversities.com/sites/default/files/stanford-university_573_medium.jpg" alt="Stanford University" title="Stanford University" height="78" width="78">
                              </a>
                           </span>

                           <a href="/universities/stanford-university" class="uni-link">Stanford University</a>

                           <div class="location">
                              <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/location.svg" height="12" width="12" alt="location" title="location"> Stanford,  United States
                           </div>

                           <div class="stars d-none">
                             <span class="ranking-star">
                               <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/stars.svg" height="20" width="20" alt="QS stars" title="QS stars">
                             </span>
                             <span class="rating_number"></span>
                             <span class="qs-stars-font">QS Stars</span>
                           </div> 



                        </div>
                     </div>
                  </div>

               <div class="col-lg-5 col-md-12 col-sm-12">
                  <div class="shortlist-compare-div">
                     <div class="shortlist_div_new">
                        <a class="wishlist _directorypage shortlistnonloggedglobaljs   _shortlist_nid_297282  shortlistnonloggedglobaljs_dlyr" progoruniv="univ" nid="297282" onclick="Drupal.behaviors.tu_d8._adduniversityShortlist(this, 297282, 'university')">
                           <i class="fa fa-heart" aria-hidden="true"></i>
                           <i class="fal fa-heart" aria-hidden="true"></i>
                           <span class="_addShortText">Shortlist</span>
                        </a>
                     </div>

                     <div class="compare_div_new">
                        <a href="javascript:void(0)" class="compare _globCompUniv_js _globcompare_universityCookie_js_297282 comparenonloggedglobaljs_dlyr" nid="297282" progoruniv="univ" onclick="Drupal.behaviors.tu_d8._adduniversityCompare(this, 297282)">
                           <span class="two-square-icon">
                              <i class="fal fa-circle" aria-hidden="true"></i>
                           </span>
                           <span class="change-text">Compare</span>
                        </a>
                     </div>
                  </div>
               </div>

               </div>



               <div class="new-rankings-tab-content-wrapper">
                  <div class="arrows-left-right-tab arrows-left-right-tab-js">
                     <button class="btn-arrows btn-right-pick btn-arrows-js" scrollnid="297282" direction="right" aria-label="rightButton">
                        <img src="/modules/custom/qs_rankings_rest_api/assets/chevron-right.png" alt="Arrows">
                     </button>
                     <button class="btn-arrows btn-left-pick btn-arrows-js d-none" scrollnid="297282" direction="left" aria-label="leftButton">
                        <img src="/modules/custom/qs_rankings_rest_api/assets/chevron-left.png" alt="Arrows">
                     </button>
                  </div>
                  <ul class="nav nav-tabs m-0 scroll-this-side-297282-js" id="myTab" role="none">
                     <li class="nav-item ">
                                   <a class="nav-link active" id="research-discovery-297282" data-toggle="tab" href="#research-discovery-297282-tab">
                                   Research &amp; Discovery
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="learning-experience-297282" data-toggle="tab" href="#learning-experience-297282-tab">
                                   Learning Experience
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="employability-297282" data-toggle="tab" href="#employability-297282-tab">
                                   Employability
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="global-engagement-297282" data-toggle="tab" href="#global-engagement-297282-tab">
                                   Global Engagement
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="sustainability-297282" data-toggle="tab" href="#sustainability-297282-tab">
                                   Sustainability
                                   </a>
                                </li>
                     <li class="nav-item" role="none">
                        <a class="nav-link" id="more-info-tab-297282" data-toggle="tab" href="#more-info-tab-297282-tab">More Info
                           <span class="new-line">NEW</span>
                           <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/lock.svg" height="14" width="12" alt="lock" title="lock" class="lock-icon-checked-js d-none">
                        </a>
                     </li>
                  </ul>
                  <div class="tab-content py-2" id="myTabContent">

                     <div class="tab-pane fade show active" id="research-discovery-297282-tab" role="tabpanel" aria-labelledby="research-discovery-297282">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Academic Reputation</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="academic-reputation" role="progressbar" aria-label="progress" title="academic-reputation" aria-labelledby="academic-reputation" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">100</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Citations per Faculty</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="citations-per-faculty" role="progressbar" aria-label="progress" title="citations-per-faculty" aria-labelledby="citations-per-faculty" style="width: 99%" aria-valuenow="99" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">99</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="learning-experience-297282-tab" role="tabpanel" aria-labelledby="learning-experience-297282">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Faculty Student Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="faculty-student-ratio" role="progressbar" aria-label="progress" title="faculty-student-ratio" aria-labelledby="faculty-student-ratio" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">100</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="employability-297282-tab" role="tabpanel" aria-labelledby="employability-297282">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Employer Reputation</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="employer-reputation" role="progressbar" aria-label="progress" title="employer-reputation" aria-labelledby="employer-reputation" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">100</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Employment Outcomes</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="employment-outcomes" role="progressbar" aria-label="progress" title="employment-outcomes" aria-labelledby="employment-outcomes" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">100</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="global-engagement-297282-tab" role="tabpanel" aria-labelledby="global-engagement-297282">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Student Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-student-ratio" role="progressbar" aria-label="progress" title="international-student-ratio" aria-labelledby="international-student-ratio" style="width: 60.8%" aria-valuenow="60.8" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">60.8</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Research Network</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-research-network" role="progressbar" aria-label="progress" title="international-research-network" aria-labelledby="international-research-network" style="width: 96.8%" aria-valuenow="96.8" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">96.8</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Faculty Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-faculty-ratio" role="progressbar" aria-label="progress" title="international-faculty-ratio" aria-labelledby="international-faculty-ratio" style="width: 70.3%" aria-valuenow="70.3" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">70.3</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="sustainability-297282-tab" role="tabpanel" aria-labelledby="sustainability-297282">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Sustainability Score</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="sustainability-score" role="progressbar" aria-label="progress" title="sustainability-score" aria-labelledby="sustainability-score" style="width: 81.2%" aria-valuenow="81.2" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">81.2</div>
                           </div>
                        </div>
                         </div>
                      </div>

                     <div class="tab-pane fade" id="more-info-tab-297282-tab" role="tabpanel" aria-labelledby="more-info-tab-297282">
                        <div class="new-rankings-indicator-wrap py-2">

                           <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Fees</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                -
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Scholarship</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                No
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Student Mix</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                Domestic 75%   International 25%
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">English Tests</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                <a href="javascript:void(0)" class="_openfilter_results_js">Generate Result</a>
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Academic Tests</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                <a href="javascript:void(0)" class="_openfilter_results_js">Generate Result</a>
                              </div>
                           </div>
                        </div>


                        </div>

                        <div class="signup-for-user signup-for-user-js d-none">
                           <p>In order to see the data <a href="javascript:void(0)" class="signup-for-user-js-dlyr" data-toggle="modal" data-target="#emailModal">Sign up for free</a></p>
                        </div>


                     </div>

                  </div>
               </div>


            </div>

         </div>
      </div>
   </div>

   <div class="ind firstloaded main ranking-row-js-294432" nid="294432">
      <div class="">
         <div class="new-ranking-cards  normal-row">

            <div class="left-div-200">
               <div class="rank-square height-97px dark-blue padding-top-24">
                  <span class="rank-title mobile-upper">Rank</span>
                  <span class="rank-no">
                     7
                     <span class="dagger-icon-new d-none">
                        <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/dagger.svg" alt="Dagger Icon">
                     </span>
                  </span>
               </div>
               <div class="height-1px">
               </div>
               
               


               <div class="rank-square height-163px light-blue padding-top-32 text-align-mobile">
                  
                  

                 

                 


                  <span class="rank-title di-inline">Overall Score:</span>
                  <span class="rank-score di-inline">93.9</span>
               </div>
            </div>

            <div class="right-div-200">

               <div class="row">
                  <div class="col-lg-7 col-md-12 col-sm-12">
                     <div class="university-details-name">

                        <div class="univ-names-text">
                           <span class="logo-wrapper new-rank ">
                              <a href="/universities/eth-zurich">
                                <img fetchpriority="low" loading="lazy" src="https://www.topuniversities.com/sites/default/files/eth-zurich-swiss-federal-institute-of-technology_201_medium.jpg" alt="ETH Zurich" title="ETH Zurich" height="78" width="78">
                              </a>
                           </span>

                           <a href="/universities/eth-zurich" class="uni-link">ETH Zurich</a>

                           <div class="location">
                              <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/location.svg" height="12" width="12" alt="location" title="location"> Zürich,  Switzerland
                           </div>

                           <div class="stars d-none">
                             <span class="ranking-star">
                               <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/stars.svg" height="20" width="20" alt="QS stars" title="QS stars">
                             </span>
                             <span class="rating_number"></span>
                             <span class="qs-stars-font">QS Stars</span>
                           </div> 



                        </div>
                     </div>
                  </div>

               <div class="col-lg-5 col-md-12 col-sm-12">
                  <div class="shortlist-compare-div">
                     <div class="shortlist_div_new">
                        <a class="wishlist _directorypage shortlistnonloggedglobaljs   _shortlist_nid_294432  shortlistnonloggedglobaljs_dlyr" progoruniv="univ" nid="294432" onclick="Drupal.behaviors.tu_d8._adduniversityShortlist(this, 294432, 'university')">
                           <i class="fa fa-heart" aria-hidden="true"></i>
                           <i class="fal fa-heart" aria-hidden="true"></i>
                           <span class="_addShortText">Shortlist</span>
                        </a>
                     </div>

                     <div class="compare_div_new">
                        <a href="javascript:void(0)" class="compare _globCompUniv_js _globcompare_universityCookie_js_294432 comparenonloggedglobaljs_dlyr" nid="294432" progoruniv="univ" onclick="Drupal.behaviors.tu_d8._adduniversityCompare(this, 294432)">
                           <span class="two-square-icon">
                              <i class="fal fa-circle" aria-hidden="true"></i>
                           </span>
                           <span class="change-text">Compare</span>
                        </a>
                     </div>
                  </div>
               </div>

               </div>



               <div class="new-rankings-tab-content-wrapper">
                  <div class="arrows-left-right-tab arrows-left-right-tab-js">
                     <button class="btn-arrows btn-right-pick btn-arrows-js" scrollnid="294432" direction="right" aria-label="rightButton">
                        <img src="/modules/custom/qs_rankings_rest_api/assets/chevron-right.png" alt="Arrows">
                     </button>
                     <button class="btn-arrows btn-left-pick btn-arrows-js d-none" scrollnid="294432" direction="left" aria-label="leftButton">
                        <img src="/modules/custom/qs_rankings_rest_api/assets/chevron-left.png" alt="Arrows">
                     </button>
                  </div>
                  <ul class="nav nav-tabs m-0 scroll-this-side-294432-js" id="myTab" role="none">
                     <li class="nav-item ">
                                   <a class="nav-link active" id="research-discovery-294432" data-toggle="tab" href="#research-discovery-294432-tab">
                                   Research &amp; Discovery
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="learning-experience-294432" data-toggle="tab" href="#learning-experience-294432-tab">
                                   Learning Experience
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="employability-294432" data-toggle="tab" href="#employability-294432-tab">
                                   Employability
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="global-engagement-294432" data-toggle="tab" href="#global-engagement-294432-tab">
                                   Global Engagement
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="sustainability-294432" data-toggle="tab" href="#sustainability-294432-tab">
                                   Sustainability
                                   </a>
                                </li>
                     <li class="nav-item" role="none">
                        <a class="nav-link" id="more-info-tab-294432" data-toggle="tab" href="#more-info-tab-294432-tab">More Info
                           <span class="new-line">NEW</span>
                           <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/lock.svg" height="14" width="12" alt="lock" title="lock" class="lock-icon-checked-js d-none">
                        </a>
                     </li>
                  </ul>
                  <div class="tab-content py-2" id="myTabContent">

                     <div class="tab-pane fade show active" id="research-discovery-294432-tab" role="tabpanel" aria-labelledby="research-discovery-294432">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Academic Reputation</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="academic-reputation" role="progressbar" aria-label="progress" title="academic-reputation" aria-labelledby="academic-reputation" style="width: 98.8%" aria-valuenow="98.8" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">98.8</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Citations per Faculty</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="citations-per-faculty" role="progressbar" aria-label="progress" title="citations-per-faculty" aria-labelledby="citations-per-faculty" style="width: 97.9%" aria-valuenow="97.9" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">97.9</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="learning-experience-294432-tab" role="tabpanel" aria-labelledby="learning-experience-294432">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Faculty Student Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="faculty-student-ratio" role="progressbar" aria-label="progress" title="faculty-student-ratio" aria-labelledby="faculty-student-ratio" style="width: 65.9%" aria-valuenow="65.9" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">65.9</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="employability-294432-tab" role="tabpanel" aria-labelledby="employability-294432">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Employer Reputation</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="employer-reputation" role="progressbar" aria-label="progress" title="employer-reputation" aria-labelledby="employer-reputation" style="width: 87.2%" aria-valuenow="87.2" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">87.2</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Employment Outcomes</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="employment-outcomes" role="progressbar" aria-label="progress" title="employment-outcomes" aria-labelledby="employment-outcomes" style="width: 90.5%" aria-valuenow="90.5" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">90.5</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="global-engagement-294432-tab" role="tabpanel" aria-labelledby="global-engagement-294432">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Student Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-student-ratio" role="progressbar" aria-label="progress" title="international-student-ratio" aria-labelledby="international-student-ratio" style="width: 98.6%" aria-valuenow="98.6" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">98.6</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Research Network</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-research-network" role="progressbar" aria-label="progress" title="international-research-network" aria-labelledby="international-research-network" style="width: 95.7%" aria-valuenow="95.7" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">95.7</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Faculty Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-faculty-ratio" role="progressbar" aria-label="progress" title="international-faculty-ratio" aria-labelledby="international-faculty-ratio" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">100</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="sustainability-294432-tab" role="tabpanel" aria-labelledby="sustainability-294432">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Sustainability Score</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="sustainability-score" role="progressbar" aria-label="progress" title="sustainability-score" aria-labelledby="sustainability-score" style="width: 98.8%" aria-valuenow="98.8" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">98.8</div>
                           </div>
                        </div>
                         </div>
                      </div>

                     <div class="tab-pane fade" id="more-info-tab-294432-tab" role="tabpanel" aria-labelledby="more-info-tab-294432">
                        <div class="new-rankings-indicator-wrap py-2">

                           <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Fees</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                1460(CHF)
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Scholarship</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                No
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Student Mix</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                Domestic 57%   International 43%
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">English Tests</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                <a href="javascript:void(0)" class="_openfilter_results_js">Generate Result</a>
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Academic Tests</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                <a href="javascript:void(0)" class="_openfilter_results_js">Generate Result</a>
                              </div>
                           </div>
                        </div>


                        </div>

                        <div class="signup-for-user signup-for-user-js d-none">
                           <p>In order to see the data <a href="javascript:void(0)" class="signup-for-user-js-dlyr" data-toggle="modal" data-target="#emailModal">Sign up for free</a></p>
                        </div>


                     </div>

                  </div>
               </div>


            </div>

         </div>
      </div>
   </div>

   <div class="ind firstloaded main ranking-row-js-294798" nid="294798">
      <div class="">
         <div class="new-ranking-cards advanced_profile new normal-row">

            <div class="left-div-200">
               <div class="rank-square height-97px dark-blue padding-top-24">
                  <span class="rank-title mobile-upper">Rank</span>
                  <span class="rank-no">
                     8
                     <span class="dagger-icon-new d-none">
                        <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/dagger.svg" alt="Dagger Icon">
                     </span>
                  </span>
               </div>
               <div class="height-1px">
               </div>
               
               


               <div class="rank-square height-163px light-blue padding-top-32 text-align-mobile">
                  
                  

                 

                 


                  <span class="rank-title di-inline">Overall Score:</span>
                  <span class="rank-score di-inline">93.7</span>
               </div>
            </div>

            <div class="right-div-200">

               <div class="row">
                  <div class="col-lg-7 col-md-12 col-sm-12">
                     <div class="university-details-name">

                        <div class="univ-names-text">
                           <span class="logo-wrapper new-rank ">
                              <a href="/universities/national-university-singapore-nus">
                                <img fetchpriority="low" loading="lazy" src="https://www.topuniversities.com/sites/default/files/national-university-of-singapore-nus_443_medium.jpg" alt="National University of Singapore (NUS)" title="National University of Singapore (NUS)" height="78" width="78">
                              </a>
                           </span>

                           <a href="/universities/national-university-singapore-nus" class="uni-link">National University of Singapore (NUS)</a>

                           <div class="location">
                              <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/location.svg" height="12" width="12" alt="location" title="location"> Singapore,  Singapore
                           </div>

                           <div class="stars d-none">
                             <span class="ranking-star">
                               <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/stars.svg" height="20" width="20" alt="QS stars" title="QS stars">
                             </span>
                             <span class="rating_number"></span>
                             <span class="qs-stars-font">QS Stars</span>
                           </div> 



                        </div>
                     </div>
                  </div>

               <div class="col-lg-5 col-md-12 col-sm-12">
                  <div class="shortlist-compare-div">
                     <div class="shortlist_div_new">
                        <a class="wishlist _directorypage shortlistnonloggedglobaljs   _shortlist_nid_294798  shortlistnonloggedglobaljs_dlyr" progoruniv="univ" nid="294798" onclick="Drupal.behaviors.tu_d8._adduniversityShortlist(this, 294798, 'university')">
                           <i class="fa fa-heart" aria-hidden="true"></i>
                           <i class="fal fa-heart" aria-hidden="true"></i>
                           <span class="_addShortText">Shortlist</span>
                        </a>
                     </div>

                     <div class="compare_div_new">
                        <a href="javascript:void(0)" class="compare _globCompUniv_js _globcompare_universityCookie_js_294798 comparenonloggedglobaljs_dlyr" nid="294798" progoruniv="univ" onclick="Drupal.behaviors.tu_d8._adduniversityCompare(this, 294798)">
                           <span class="two-square-icon">
                              <i class="fal fa-circle" aria-hidden="true"></i>
                           </span>
                           <span class="change-text">Compare</span>
                        </a>
                     </div>
                  </div>
               </div>

               </div>



               <div class="new-rankings-tab-content-wrapper">
                  <div class="arrows-left-right-tab arrows-left-right-tab-js">
                     <button class="btn-arrows btn-right-pick btn-arrows-js" scrollnid="294798" direction="right" aria-label="rightButton">
                        <img src="/modules/custom/qs_rankings_rest_api/assets/chevron-right.png" alt="Arrows">
                     </button>
                     <button class="btn-arrows btn-left-pick btn-arrows-js d-none" scrollnid="294798" direction="left" aria-label="leftButton">
                        <img src="/modules/custom/qs_rankings_rest_api/assets/chevron-left.png" alt="Arrows">
                     </button>
                  </div>
                  <ul class="nav nav-tabs m-0 scroll-this-side-294798-js" id="myTab" role="none">
                     <li class="nav-item ">
                                   <a class="nav-link active" id="research-discovery-294798" data-toggle="tab" href="#research-discovery-294798-tab">
                                   Research &amp; Discovery
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="learning-experience-294798" data-toggle="tab" href="#learning-experience-294798-tab">
                                   Learning Experience
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="employability-294798" data-toggle="tab" href="#employability-294798-tab">
                                   Employability
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="global-engagement-294798" data-toggle="tab" href="#global-engagement-294798-tab">
                                   Global Engagement
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="sustainability-294798" data-toggle="tab" href="#sustainability-294798-tab">
                                   Sustainability
                                   </a>
                                </li>
                     <li class="nav-item" role="none">
                        <a class="nav-link" id="more-info-tab-294798" data-toggle="tab" href="#more-info-tab-294798-tab">More Info
                           <span class="new-line">NEW</span>
                           <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/lock.svg" height="14" width="12" alt="lock" title="lock" class="lock-icon-checked-js d-none">
                        </a>
                     </li>
                  </ul>
                  <div class="tab-content py-2" id="myTabContent">

                     <div class="tab-pane fade show active" id="research-discovery-294798-tab" role="tabpanel" aria-labelledby="research-discovery-294798">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Academic Reputation</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="academic-reputation" role="progressbar" aria-label="progress" title="academic-reputation" aria-labelledby="academic-reputation" style="width: 99.5%" aria-valuenow="99.5" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">99.5</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Citations per Faculty</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="citations-per-faculty" role="progressbar" aria-label="progress" title="citations-per-faculty" aria-labelledby="citations-per-faculty" style="width: 93.1%" aria-valuenow="93.1" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">93.1</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="learning-experience-294798-tab" role="tabpanel" aria-labelledby="learning-experience-294798">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Faculty Student Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="faculty-student-ratio" role="progressbar" aria-label="progress" title="faculty-student-ratio" aria-labelledby="faculty-student-ratio" style="width: 68.8%" aria-valuenow="68.8" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">68.8</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="employability-294798-tab" role="tabpanel" aria-labelledby="employability-294798">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Employer Reputation</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="employer-reputation" role="progressbar" aria-label="progress" title="employer-reputation" aria-labelledby="employer-reputation" style="width: 91.1%" aria-valuenow="91.1" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">91.1</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Employment Outcomes</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="employment-outcomes" role="progressbar" aria-label="progress" title="employment-outcomes" aria-labelledby="employment-outcomes" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">100</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="global-engagement-294798-tab" role="tabpanel" aria-labelledby="global-engagement-294798">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Student Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-student-ratio" role="progressbar" aria-label="progress" title="international-student-ratio" aria-labelledby="international-student-ratio" style="width: 88.9%" aria-valuenow="88.9" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">88.9</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Research Network</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-research-network" role="progressbar" aria-label="progress" title="international-research-network" aria-labelledby="international-research-network" style="width: 91.6%" aria-valuenow="91.6" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">91.6</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Faculty Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-faculty-ratio" role="progressbar" aria-label="progress" title="international-faculty-ratio" aria-labelledby="international-faculty-ratio" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">100</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="sustainability-294798-tab" role="tabpanel" aria-labelledby="sustainability-294798">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Sustainability Score</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="sustainability-score" role="progressbar" aria-label="progress" title="sustainability-score" aria-labelledby="sustainability-score" style="width: 97.7%" aria-valuenow="97.7" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">97.7</div>
                           </div>
                        </div>
                         </div>
                      </div>

                     <div class="tab-pane fade" id="more-info-tab-294798-tab" role="tabpanel" aria-labelledby="more-info-tab-294798">
                        <div class="new-rankings-indicator-wrap py-2">

                           <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Fees</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                17650(SGD)
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Scholarship</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                No
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Student Mix</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                Domestic 64%   International 36%
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">English Tests</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                <a href="javascript:void(0)" class="_openfilter_results_js">Generate Result</a>
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Academic Tests</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                <a href="javascript:void(0)" class="_openfilter_results_js">Generate Result</a>
                              </div>
                           </div>
                        </div>


                        </div>

                        <div class="signup-for-user signup-for-user-js d-none">
                           <p>In order to see the data <a href="javascript:void(0)" class="signup-for-user-js-dlyr" data-toggle="modal" data-target="#emailModal">Sign up for free</a></p>
                        </div>


                     </div>

                  </div>
               </div>


            </div>

         </div>
      </div>
   </div>

   <div class="ind firstloaded main ranking-row-js-294014" nid="294014">
      <div class="">
         <div class="new-ranking-cards advanced_profile new normal-row">

            <div class="left-div-200">
               <div class="rank-square height-97px dark-blue padding-top-24">
                  <span class="rank-title mobile-upper">Rank</span>
                  <span class="rank-no">
                     9
                     <span class="dagger-icon-new d-none">
                        <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/dagger.svg" alt="Dagger Icon">
                     </span>
                  </span>
               </div>
               <div class="height-1px">
               </div>
               
               


               <div class="rank-square height-163px light-blue padding-top-32 text-align-mobile">
                  
                  

                 

                 


                  <span class="rank-title di-inline">Overall Score:</span>
                  <span class="rank-score di-inline">91.6</span>
               </div>
            </div>

            <div class="right-div-200">

               <div class="row">
                  <div class="col-lg-7 col-md-12 col-sm-12">
                     <div class="university-details-name">

                        <div class="univ-names-text">
                           <span class="logo-wrapper new-rank ">
                              <a href="/universities/ucl">
                                <img fetchpriority="low" loading="lazy" src="https://www.topuniversities.com/sites/default/files/240209111134am850728QS-UCL-icon-90x90.jpg" alt="UCL" title="UCL" height="78" width="78">
                              </a>
                           </span>

                           <a href="/universities/ucl" class="uni-link">UCL</a>

                           <div class="location">
                              <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/location.svg" height="12" width="12" alt="location" title="location"> London,  United Kingdom
                           </div>

                           <div class="stars d-none">
                             <span class="ranking-star">
                               <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/stars.svg" height="20" width="20" alt="QS stars" title="QS stars">
                             </span>
                             <span class="rating_number"></span>
                             <span class="qs-stars-font">QS Stars</span>
                           </div> 



                        </div>
                     </div>
                  </div>

               <div class="col-lg-5 col-md-12 col-sm-12">
                  <div class="shortlist-compare-div">
                     <div class="shortlist_div_new">
                        <a class="wishlist _directorypage shortlistnonloggedglobaljs   _shortlist_nid_294014  shortlistnonloggedglobaljs_dlyr" progoruniv="univ" nid="294014" onclick="Drupal.behaviors.tu_d8._adduniversityShortlist(this, 294014, 'university')">
                           <i class="fa fa-heart" aria-hidden="true"></i>
                           <i class="fal fa-heart" aria-hidden="true"></i>
                           <span class="_addShortText">Shortlist</span>
                        </a>
                     </div>

                     <div class="compare_div_new">
                        <a href="javascript:void(0)" class="compare _globCompUniv_js _globcompare_universityCookie_js_294014 comparenonloggedglobaljs_dlyr" nid="294014" progoruniv="univ" onclick="Drupal.behaviors.tu_d8._adduniversityCompare(this, 294014)">
                           <span class="two-square-icon">
                              <i class="fal fa-circle" aria-hidden="true"></i>
                           </span>
                           <span class="change-text">Compare</span>
                        </a>
                     </div>
                  </div>
               </div>

               </div>



               <div class="new-rankings-tab-content-wrapper">
                  <div class="arrows-left-right-tab arrows-left-right-tab-js">
                     <button class="btn-arrows btn-right-pick btn-arrows-js" scrollnid="294014" direction="right" aria-label="rightButton">
                        <img src="/modules/custom/qs_rankings_rest_api/assets/chevron-right.png" alt="Arrows">
                     </button>
                     <button class="btn-arrows btn-left-pick btn-arrows-js d-none" scrollnid="294014" direction="left" aria-label="leftButton">
                        <img src="/modules/custom/qs_rankings_rest_api/assets/chevron-left.png" alt="Arrows">
                     </button>
                  </div>
                  <ul class="nav nav-tabs m-0 scroll-this-side-294014-js" id="myTab" role="none">
                     <li class="nav-item ">
                                   <a class="nav-link active" id="research-discovery-294014" data-toggle="tab" href="#research-discovery-294014-tab">
                                   Research &amp; Discovery
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="learning-experience-294014" data-toggle="tab" href="#learning-experience-294014-tab">
                                   Learning Experience
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="employability-294014" data-toggle="tab" href="#employability-294014-tab">
                                   Employability
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="global-engagement-294014" data-toggle="tab" href="#global-engagement-294014-tab">
                                   Global Engagement
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="sustainability-294014" data-toggle="tab" href="#sustainability-294014-tab">
                                   Sustainability
                                   </a>
                                </li>
                     <li class="nav-item" role="none">
                        <a class="nav-link" id="more-info-tab-294014" data-toggle="tab" href="#more-info-tab-294014-tab">More Info
                           <span class="new-line">NEW</span>
                           <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/lock.svg" height="14" width="12" alt="lock" title="lock" class="lock-icon-checked-js d-none">
                        </a>
                     </li>
                  </ul>
                  <div class="tab-content py-2" id="myTabContent">

                     <div class="tab-pane fade show active" id="research-discovery-294014-tab" role="tabpanel" aria-labelledby="research-discovery-294014">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Academic Reputation</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="academic-reputation" role="progressbar" aria-label="progress" title="academic-reputation" aria-labelledby="academic-reputation" style="width: 99.5%" aria-valuenow="99.5" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">99.5</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Citations per Faculty</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="citations-per-faculty" role="progressbar" aria-label="progress" title="citations-per-faculty" aria-labelledby="citations-per-faculty" style="width: 72.2%" aria-valuenow="72.2" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">72.2</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="learning-experience-294014-tab" role="tabpanel" aria-labelledby="learning-experience-294014">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Faculty Student Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="faculty-student-ratio" role="progressbar" aria-label="progress" title="faculty-student-ratio" aria-labelledby="faculty-student-ratio" style="width: 95.9%" aria-valuenow="95.9" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">95.9</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="employability-294014-tab" role="tabpanel" aria-labelledby="employability-294014">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Employer Reputation</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="employer-reputation" role="progressbar" aria-label="progress" title="employer-reputation" aria-labelledby="employer-reputation" style="width: 98.3%" aria-valuenow="98.3" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">98.3</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Employment Outcomes</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="employment-outcomes" role="progressbar" aria-label="progress" title="employment-outcomes" aria-labelledby="employment-outcomes" style="width: 70.3%" aria-valuenow="70.3" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">70.3</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="global-engagement-294014-tab" role="tabpanel" aria-labelledby="global-engagement-294014">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Student Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-student-ratio" role="progressbar" aria-label="progress" title="international-student-ratio" aria-labelledby="international-student-ratio" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">100</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Research Network</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-research-network" role="progressbar" aria-label="progress" title="international-research-network" aria-labelledby="international-research-network" style="width: 99.9%" aria-valuenow="99.9" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">99.9</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Faculty Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-faculty-ratio" role="progressbar" aria-label="progress" title="international-faculty-ratio" aria-labelledby="international-faculty-ratio" style="width: 99%" aria-valuenow="99" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">99</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="sustainability-294014-tab" role="tabpanel" aria-labelledby="sustainability-294014">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Sustainability Score</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="sustainability-score" role="progressbar" aria-label="progress" title="sustainability-score" aria-labelledby="sustainability-score" style="width: 74.8%" aria-valuenow="74.8" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">74.8</div>
                           </div>
                        </div>
                         </div>
                      </div>

                     <div class="tab-pane fade" id="more-info-tab-294014-tab" role="tabpanel" aria-labelledby="more-info-tab-294014">
                        <div class="new-rankings-indicator-wrap py-2">

                           <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Fees</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                24000(GBP)
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Scholarship</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                Yes
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Student Mix</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                Domestic 43%   International 57%
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">English Tests</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                <a href="javascript:void(0)" class="_openfilter_results_js">Generate Result</a>
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Academic Tests</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                <a href="javascript:void(0)" class="_openfilter_results_js">Generate Result</a>
                              </div>
                           </div>
                        </div>


                        </div>

                        <div class="signup-for-user signup-for-user-js d-none">
                           <p>In order to see the data <a href="javascript:void(0)" class="signup-for-user-js-dlyr" data-toggle="modal" data-target="#emailModal">Sign up for free</a></p>
                        </div>


                     </div>

                  </div>
               </div>


            </div>

         </div>
      </div>
   </div>

   <div class="ind firstloaded main ranking-row-js-294562 before_ad_2" nid="294562">
      <div class="">
         <div class="new-ranking-cards  normal-row">

            <div class="left-div-200">
               <div class="rank-square height-97px dark-blue padding-top-24">
                  <span class="rank-title mobile-upper">Rank</span>
                  <span class="rank-no">
                     10
                     <span class="dagger-icon-new d-none">
                        <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/dagger.svg" alt="Dagger Icon">
                     </span>
                  </span>
               </div>
               <div class="height-1px">
               </div>
               
               


               <div class="rank-square height-163px light-blue padding-top-32 text-align-mobile">
                  
                  

                 

                 


                  <span class="rank-title di-inline">Overall Score:</span>
                  <span class="rank-score di-inline">90.9</span>
               </div>
            </div>

            <div class="right-div-200">

               <div class="row">
                  <div class="col-lg-7 col-md-12 col-sm-12">
                     <div class="university-details-name">

                        <div class="univ-names-text">
                           <span class="logo-wrapper new-rank ">
                              <a href="/universities/california-institute-technology-caltech">
                                <img fetchpriority="low" loading="lazy" src="https://www.topuniversities.com/sites/default/files/california-institute-of-technology-caltech_94_medium.jpg" alt="California Institute of Technology (Caltech)" title="California Institute of Technology (Caltech)" height="78" width="78">
                              </a>
                           </span>

                           <a href="/universities/california-institute-technology-caltech" class="uni-link">California Institute of Technology (Caltech)</a>

                           <div class="location">
                              <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/location.svg" height="12" width="12" alt="location" title="location"> Pasadena,  United States
                           </div>

                           <div class="stars d-none">
                             <span class="ranking-star">
                               <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/stars.svg" height="20" width="20" alt="QS stars" title="QS stars">
                             </span>
                             <span class="rating_number"></span>
                             <span class="qs-stars-font">QS Stars</span>
                           </div> 



                        </div>
                     </div>
                  </div>

               <div class="col-lg-5 col-md-12 col-sm-12">
                  <div class="shortlist-compare-div">
                     <div class="shortlist_div_new">
                        <a class="wishlist _directorypage shortlistnonloggedglobaljs   _shortlist_nid_294562  shortlistnonloggedglobaljs_dlyr" progoruniv="univ" nid="294562" onclick="Drupal.behaviors.tu_d8._adduniversityShortlist(this, 294562, 'university')">
                           <i class="fa fa-heart" aria-hidden="true"></i>
                           <i class="fal fa-heart" aria-hidden="true"></i>
                           <span class="_addShortText">Shortlist</span>
                        </a>
                     </div>

                     <div class="compare_div_new">
                        <a href="javascript:void(0)" class="compare _globCompUniv_js _globcompare_universityCookie_js_294562 comparenonloggedglobaljs_dlyr" nid="294562" progoruniv="univ" onclick="Drupal.behaviors.tu_d8._adduniversityCompare(this, 294562)">
                           <span class="two-square-icon">
                              <i class="fal fa-circle" aria-hidden="true"></i>
                           </span>
                           <span class="change-text">Compare</span>
                        </a>
                     </div>
                  </div>
               </div>

               </div>



               <div class="new-rankings-tab-content-wrapper">
                  <div class="arrows-left-right-tab arrows-left-right-tab-js">
                     <button class="btn-arrows btn-right-pick btn-arrows-js" scrollnid="294562" direction="right" aria-label="rightButton">
                        <img src="/modules/custom/qs_rankings_rest_api/assets/chevron-right.png" alt="Arrows">
                     </button>
                     <button class="btn-arrows btn-left-pick btn-arrows-js d-none" scrollnid="294562" direction="left" aria-label="leftButton">
                        <img src="/modules/custom/qs_rankings_rest_api/assets/chevron-left.png" alt="Arrows">
                     </button>
                  </div>
                  <ul class="nav nav-tabs m-0 scroll-this-side-294562-js" id="myTab" role="none">
                     <li class="nav-item ">
                                   <a class="nav-link active" id="research-discovery-294562" data-toggle="tab" href="#research-discovery-294562-tab">
                                   Research &amp; Discovery
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="learning-experience-294562" data-toggle="tab" href="#learning-experience-294562-tab">
                                   Learning Experience
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="employability-294562" data-toggle="tab" href="#employability-294562-tab">
                                   Employability
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="global-engagement-294562" data-toggle="tab" href="#global-engagement-294562-tab">
                                   Global Engagement
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="sustainability-294562" data-toggle="tab" href="#sustainability-294562-tab">
                                   Sustainability
                                   </a>
                                </li>
                     <li class="nav-item" role="none">
                        <a class="nav-link" id="more-info-tab-294562" data-toggle="tab" href="#more-info-tab-294562-tab">More Info
                           <span class="new-line">NEW</span>
                           <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/lock.svg" height="14" width="12" alt="lock" title="lock" class="lock-icon-checked-js d-none">
                        </a>
                     </li>
                  </ul>
                  <div class="tab-content py-2" id="myTabContent">

                     <div class="tab-pane fade show active" id="research-discovery-294562-tab" role="tabpanel" aria-labelledby="research-discovery-294562">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Academic Reputation</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="academic-reputation" role="progressbar" aria-label="progress" title="academic-reputation" aria-labelledby="academic-reputation" style="width: 96.5%" aria-valuenow="96.5" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">96.5</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Citations per Faculty</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="citations-per-faculty" role="progressbar" aria-label="progress" title="citations-per-faculty" aria-labelledby="citations-per-faculty" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">100</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="learning-experience-294562-tab" role="tabpanel" aria-labelledby="learning-experience-294562">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Faculty Student Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="faculty-student-ratio" role="progressbar" aria-label="progress" title="faculty-student-ratio" aria-labelledby="faculty-student-ratio" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">100</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="employability-294562-tab" role="tabpanel" aria-labelledby="employability-294562">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Employer Reputation</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="employer-reputation" role="progressbar" aria-label="progress" title="employer-reputation" aria-labelledby="employer-reputation" style="width: 95.3%" aria-valuenow="95.3" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">95.3</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Employment Outcomes</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="employment-outcomes" role="progressbar" aria-label="progress" title="employment-outcomes" aria-labelledby="employment-outcomes" style="width: 31%" aria-valuenow="31" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">31</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="global-engagement-294562-tab" role="tabpanel" aria-labelledby="global-engagement-294562">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Student Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-student-ratio" role="progressbar" aria-label="progress" title="international-student-ratio" aria-labelledby="international-student-ratio" style="width: 79.8%" aria-valuenow="79.8" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">79.8</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Research Network</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-research-network" role="progressbar" aria-label="progress" title="international-research-network" aria-labelledby="international-research-network" style="width: 65.5%" aria-valuenow="65.5" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">65.5</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Faculty Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-faculty-ratio" role="progressbar" aria-label="progress" title="international-faculty-ratio" aria-labelledby="international-faculty-ratio" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">100</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="sustainability-294562-tab" role="tabpanel" aria-labelledby="sustainability-294562">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Sustainability Score</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="sustainability-score" role="progressbar" aria-label="progress" title="sustainability-score" aria-labelledby="sustainability-score" style="width: 62.5%" aria-valuenow="62.5" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">62.5</div>
                           </div>
                        </div>
                         </div>
                      </div>

                     <div class="tab-pane fade" id="more-info-tab-294562-tab" role="tabpanel" aria-labelledby="more-info-tab-294562">
                        <div class="new-rankings-indicator-wrap py-2">

                           <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Fees</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                -
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Scholarship</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                No
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Student Mix</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                Domestic 70%   International 30%
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">English Tests</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                <a href="javascript:void(0)" class="_openfilter_results_js">Generate Result</a>
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Academic Tests</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                <a href="javascript:void(0)" class="_openfilter_results_js">Generate Result</a>
                              </div>
                           </div>
                        </div>


                        </div>

                        <div class="signup-for-user signup-for-user-js d-none">
                           <p>In order to see the data <a href="javascript:void(0)" class="signup-for-user-js-dlyr" data-toggle="modal" data-target="#emailModal">Sign up for free</a></p>
                        </div>


                     </div>

                  </div>
               </div>


            </div>

         </div>
      </div>
   </div><div class="row need-section-margin dynamic-block-ranking-2" position="10" customblock="true">
  <div class="_ifdfp_1 td-wrap col-lg-12 _ifdfp_1_divcss scroll-in-mobile">
                                         <div id="js-dfp-tag-responsive_ad_2" class="text-center" data-google-query-id="CMTtjr6m04oDFSREwgUdmXksWw">
               
              <div id="google_ads_iframe_8070/Topuni-Web/world-university-rankings_1__container__" style="border: 0pt none;"><iframe id="google_ads_iframe_8070/Topuni-Web/world-university-rankings_1" name="google_ads_iframe_8070/Topuni-Web/world-university-rankings_1" title="3rd party ad content" width="750" height="200" scrolling="no" marginwidth="0" marginheight="0" frameborder="0" aria-label="Advertisement" tabindex="0" allow="private-state-token-redemption;attribution-reporting" data-load-complete="true" data-google-container-id="7" style="border: 0px; vertical-align: bottom; visibility: visible;"></iframe></div></div>
                            </div>
</div>

   <div class="ind firstloaded main ranking-row-js-297569" nid="297569">
      <div class="">
         <div class="new-ranking-cards  normal-row">

            <div class="left-div-200">
               <div class="rank-square height-97px dark-blue padding-top-24">
                  <span class="rank-title mobile-upper">Rank</span>
                  <span class="rank-no">
                     11
                     <span class="dagger-icon-new d-none">
                        <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/dagger.svg" alt="Dagger Icon">
                     </span>
                  </span>
               </div>
               <div class="height-1px">
               </div>
               
               


               <div class="rank-square height-163px light-blue padding-top-32 text-align-mobile">
                  
                  

                 

                 


                  <span class="rank-title di-inline">Overall Score:</span>
                  <span class="rank-score di-inline">90.3</span>
               </div>
            </div>

            <div class="right-div-200">

               <div class="row">
                  <div class="col-lg-7 col-md-12 col-sm-12">
                     <div class="university-details-name">

                        <div class="univ-names-text">
                           <span class="logo-wrapper new-rank ">
                              <a href="/universities/university-pennsylvania">
                                <img fetchpriority="low" loading="lazy" src="https://www.topuniversities.com/sites/default/files/university-of-pennsylvania_495_medium.jpg" alt="University of Pennsylvania" title="University of Pennsylvania" height="78" width="78">
                              </a>
                           </span>

                           <a href="/universities/university-pennsylvania" class="uni-link">University of Pennsylvania</a>

                           <div class="location">
                              <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/location.svg" height="12" width="12" alt="location" title="location"> Philadelphia,  United States
                           </div>

                           <div class="stars d-none">
                             <span class="ranking-star">
                               <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/stars.svg" height="20" width="20" alt="QS stars" title="QS stars">
                             </span>
                             <span class="rating_number"></span>
                             <span class="qs-stars-font">QS Stars</span>
                           </div> 



                        </div>
                     </div>
                  </div>

               <div class="col-lg-5 col-md-12 col-sm-12">
                  <div class="shortlist-compare-div">
                     <div class="shortlist_div_new">
                        <a class="wishlist _directorypage shortlistnonloggedglobaljs   _shortlist_nid_297569  shortlistnonloggedglobaljs_dlyr" progoruniv="univ" nid="297569" onclick="Drupal.behaviors.tu_d8._adduniversityShortlist(this, 297569, 'university')">
                           <i class="fa fa-heart" aria-hidden="true"></i>
                           <i class="fal fa-heart" aria-hidden="true"></i>
                           <span class="_addShortText">Shortlist</span>
                        </a>
                     </div>

                     <div class="compare_div_new">
                        <a href="javascript:void(0)" class="compare _globCompUniv_js _globcompare_universityCookie_js_297569 comparenonloggedglobaljs_dlyr" nid="297569" progoruniv="univ" onclick="Drupal.behaviors.tu_d8._adduniversityCompare(this, 297569)">
                           <span class="two-square-icon">
                              <i class="fal fa-circle" aria-hidden="true"></i>
                           </span>
                           <span class="change-text">Compare</span>
                        </a>
                     </div>
                  </div>
               </div>

               </div>



               <div class="new-rankings-tab-content-wrapper">
                  <div class="arrows-left-right-tab arrows-left-right-tab-js">
                     <button class="btn-arrows btn-right-pick btn-arrows-js" scrollnid="297569" direction="right" aria-label="rightButton">
                        <img src="/modules/custom/qs_rankings_rest_api/assets/chevron-right.png" alt="Arrows">
                     </button>
                     <button class="btn-arrows btn-left-pick btn-arrows-js d-none" scrollnid="297569" direction="left" aria-label="leftButton">
                        <img src="/modules/custom/qs_rankings_rest_api/assets/chevron-left.png" alt="Arrows">
                     </button>
                  </div>
                  <ul class="nav nav-tabs m-0 scroll-this-side-297569-js" id="myTab" role="none">
                     <li class="nav-item ">
                                   <a class="nav-link active" id="research-discovery-297569" data-toggle="tab" href="#research-discovery-297569-tab">
                                   Research &amp; Discovery
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="learning-experience-297569" data-toggle="tab" href="#learning-experience-297569-tab">
                                   Learning Experience
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="employability-297569" data-toggle="tab" href="#employability-297569-tab">
                                   Employability
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="global-engagement-297569" data-toggle="tab" href="#global-engagement-297569-tab">
                                   Global Engagement
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="sustainability-297569" data-toggle="tab" href="#sustainability-297569-tab">
                                   Sustainability
                                   </a>
                                </li>
                     <li class="nav-item" role="none">
                        <a class="nav-link" id="more-info-tab-297569" data-toggle="tab" href="#more-info-tab-297569-tab">More Info
                           <span class="new-line">NEW</span>
                           <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/lock.svg" height="14" width="12" alt="lock" title="lock" class="lock-icon-checked-js d-none">
                        </a>
                     </li>
                  </ul>
                  <div class="tab-content py-2" id="myTabContent">

                     <div class="tab-pane fade show active" id="research-discovery-297569-tab" role="tabpanel" aria-labelledby="research-discovery-297569">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Academic Reputation</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="academic-reputation" role="progressbar" aria-label="progress" title="academic-reputation" aria-labelledby="academic-reputation" style="width: 96.3%" aria-valuenow="96.3" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">96.3</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Citations per Faculty</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="citations-per-faculty" role="progressbar" aria-label="progress" title="citations-per-faculty" aria-labelledby="citations-per-faculty" style="width: 74%" aria-valuenow="74" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">74</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="learning-experience-297569-tab" role="tabpanel" aria-labelledby="learning-experience-297569">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Faculty Student Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="faculty-student-ratio" role="progressbar" aria-label="progress" title="faculty-student-ratio" aria-labelledby="faculty-student-ratio" style="width: 99.8%" aria-valuenow="99.8" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">99.8</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="employability-297569-tab" role="tabpanel" aria-labelledby="employability-297569">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Employer Reputation</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="employer-reputation" role="progressbar" aria-label="progress" title="employer-reputation" aria-labelledby="employer-reputation" style="width: 91.9%" aria-valuenow="91.9" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">91.9</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Employment Outcomes</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="employment-outcomes" role="progressbar" aria-label="progress" title="employment-outcomes" aria-labelledby="employment-outcomes" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">100</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="global-engagement-297569-tab" role="tabpanel" aria-labelledby="global-engagement-297569">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Student Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-student-ratio" role="progressbar" aria-label="progress" title="international-student-ratio" aria-labelledby="international-student-ratio" style="width: 66.2%" aria-valuenow="66.2" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">66.2</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Research Network</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-research-network" role="progressbar" aria-label="progress" title="international-research-network" aria-labelledby="international-research-network" style="width: 91.9%" aria-valuenow="91.9" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">91.9</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Faculty Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-faculty-ratio" role="progressbar" aria-label="progress" title="international-faculty-ratio" aria-labelledby="international-faculty-ratio" style="width: 90.9%" aria-valuenow="90.9" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">90.9</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="sustainability-297569-tab" role="tabpanel" aria-labelledby="sustainability-297569">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Sustainability Score</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="sustainability-score" role="progressbar" aria-label="progress" title="sustainability-score" aria-labelledby="sustainability-score" style="width: 93%" aria-valuenow="93" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">93</div>
                           </div>
                        </div>
                         </div>
                      </div>

                     <div class="tab-pane fade" id="more-info-tab-297569-tab" role="tabpanel" aria-labelledby="more-info-tab-297569">
                        <div class="new-rankings-indicator-wrap py-2">

                           <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Fees</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                -
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Scholarship</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                Yes
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Student Mix</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                Domestic 74%   International 26%
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">English Tests</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                <a href="javascript:void(0)" class="_openfilter_results_js">Generate Result</a>
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Academic Tests</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                <a href="javascript:void(0)" class="_openfilter_results_js">Generate Result</a>
                              </div>
                           </div>
                        </div>


                        </div>

                        <div class="signup-for-user signup-for-user-js d-none">
                           <p>In order to see the data <a href="javascript:void(0)" class="signup-for-user-js-dlyr" data-toggle="modal" data-target="#emailModal">Sign up for free</a></p>
                        </div>


                     </div>

                  </div>
               </div>


            </div>

         </div>
      </div>
   </div>

   <div class="ind firstloaded main ranking-row-js-294572" nid="294572">
      <div class="">
         <div class="new-ranking-cards  normal-row">

            <div class="left-div-200">
               <div class="rank-square height-97px dark-blue padding-top-24">
                  <span class="rank-title mobile-upper">Rank</span>
                  <span class="rank-no">
                     12
                     <span class="dagger-icon-new d-none">
                        <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/dagger.svg" alt="Dagger Icon">
                     </span>
                  </span>
               </div>
               <div class="height-1px">
               </div>
               
               


               <div class="rank-square height-163px light-blue padding-top-32 text-align-mobile">
                  
                  

                 

                 


                  <span class="rank-title di-inline">Overall Score:</span>
                  <span class="rank-score di-inline">90.1</span>
               </div>
            </div>

            <div class="right-div-200">

               <div class="row">
                  <div class="col-lg-7 col-md-12 col-sm-12">
                     <div class="university-details-name">

                        <div class="univ-names-text">
                           <span class="logo-wrapper new-rank ">
                              <a href="/universities/university-california-berkeley-ucb">
                                <img fetchpriority="low" loading="lazy" src="https://www.topuniversities.com/sites/default/files/university-of-california-berkeley-ucb_84_medium.jpg" alt="University of California, Berkeley (UCB)" title="University of California, Berkeley (UCB)" height="78" width="78">
                              </a>
                           </span>

                           <a href="/universities/university-california-berkeley-ucb" class="uni-link">University of California, Berkeley (UCB)</a>

                           <div class="location">
                              <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/location.svg" height="12" width="12" alt="location" title="location"> Berkeley,  United States
                           </div>

                           <div class="stars d-none">
                             <span class="ranking-star">
                               <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/stars.svg" height="20" width="20" alt="QS stars" title="QS stars">
                             </span>
                             <span class="rating_number"></span>
                             <span class="qs-stars-font">QS Stars</span>
                           </div> 



                        </div>
                     </div>
                  </div>

               <div class="col-lg-5 col-md-12 col-sm-12">
                  <div class="shortlist-compare-div">
                     <div class="shortlist_div_new">
                        <a class="wishlist _directorypage shortlistnonloggedglobaljs   _shortlist_nid_294572  shortlistnonloggedglobaljs_dlyr" progoruniv="univ" nid="294572" onclick="Drupal.behaviors.tu_d8._adduniversityShortlist(this, 294572, 'university')">
                           <i class="fa fa-heart" aria-hidden="true"></i>
                           <i class="fal fa-heart" aria-hidden="true"></i>
                           <span class="_addShortText">Shortlist</span>
                        </a>
                     </div>

                     <div class="compare_div_new">
                        <a href="javascript:void(0)" class="compare _globCompUniv_js _globcompare_universityCookie_js_294572 comparenonloggedglobaljs_dlyr" nid="294572" progoruniv="univ" onclick="Drupal.behaviors.tu_d8._adduniversityCompare(this, 294572)">
                           <span class="two-square-icon">
                              <i class="fal fa-circle" aria-hidden="true"></i>
                           </span>
                           <span class="change-text">Compare</span>
                        </a>
                     </div>
                  </div>
               </div>

               </div>



               <div class="new-rankings-tab-content-wrapper">
                  <div class="arrows-left-right-tab arrows-left-right-tab-js">
                     <button class="btn-arrows btn-right-pick btn-arrows-js" scrollnid="294572" direction="right" aria-label="rightButton">
                        <img src="/modules/custom/qs_rankings_rest_api/assets/chevron-right.png" alt="Arrows">
                     </button>
                     <button class="btn-arrows btn-left-pick btn-arrows-js d-none" scrollnid="294572" direction="left" aria-label="leftButton">
                        <img src="/modules/custom/qs_rankings_rest_api/assets/chevron-left.png" alt="Arrows">
                     </button>
                  </div>
                  <ul class="nav nav-tabs m-0 scroll-this-side-294572-js" id="myTab" role="none">
                     <li class="nav-item ">
                                   <a class="nav-link active" id="research-discovery-294572" data-toggle="tab" href="#research-discovery-294572-tab">
                                   Research &amp; Discovery
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="learning-experience-294572" data-toggle="tab" href="#learning-experience-294572-tab">
                                   Learning Experience
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="employability-294572" data-toggle="tab" href="#employability-294572-tab">
                                   Employability
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="global-engagement-294572" data-toggle="tab" href="#global-engagement-294572-tab">
                                   Global Engagement
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="sustainability-294572" data-toggle="tab" href="#sustainability-294572-tab">
                                   Sustainability
                                   </a>
                                </li>
                     <li class="nav-item" role="none">
                        <a class="nav-link" id="more-info-tab-294572" data-toggle="tab" href="#more-info-tab-294572-tab">More Info
                           <span class="new-line">NEW</span>
                           <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/lock.svg" height="14" width="12" alt="lock" title="lock" class="lock-icon-checked-js d-none">
                        </a>
                     </li>
                  </ul>
                  <div class="tab-content py-2" id="myTabContent">

                     <div class="tab-pane fade show active" id="research-discovery-294572-tab" role="tabpanel" aria-labelledby="research-discovery-294572">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Academic Reputation</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="academic-reputation" role="progressbar" aria-label="progress" title="academic-reputation" aria-labelledby="academic-reputation" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">100</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Citations per Faculty</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="citations-per-faculty" role="progressbar" aria-label="progress" title="citations-per-faculty" aria-labelledby="citations-per-faculty" style="width: 98.2%" aria-valuenow="98.2" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">98.2</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="learning-experience-294572-tab" role="tabpanel" aria-labelledby="learning-experience-294572">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Faculty Student Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="faculty-student-ratio" role="progressbar" aria-label="progress" title="faculty-student-ratio" aria-labelledby="faculty-student-ratio" style="width: 23.5%" aria-valuenow="23.5" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">23.5</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="employability-294572-tab" role="tabpanel" aria-labelledby="employability-294572">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Employer Reputation</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="employer-reputation" role="progressbar" aria-label="progress" title="employer-reputation" aria-labelledby="employer-reputation" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">100</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Employment Outcomes</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="employment-outcomes" role="progressbar" aria-label="progress" title="employment-outcomes" aria-labelledby="employment-outcomes" style="width: 98.4%" aria-valuenow="98.4" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">98.4</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="global-engagement-294572-tab" role="tabpanel" aria-labelledby="global-engagement-294572">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Student Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-student-ratio" role="progressbar" aria-label="progress" title="international-student-ratio" aria-labelledby="international-student-ratio" style="width: 61%" aria-valuenow="61" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">61</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Research Network</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-research-network" role="progressbar" aria-label="progress" title="international-research-network" aria-labelledby="international-research-network" style="width: 97.2%" aria-valuenow="97.2" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">97.2</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Faculty Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-faculty-ratio" role="progressbar" aria-label="progress" title="international-faculty-ratio" aria-labelledby="international-faculty-ratio" style="width: 91.5%" aria-valuenow="91.5" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">91.5</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="sustainability-294572-tab" role="tabpanel" aria-labelledby="sustainability-294572">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Sustainability Score</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="sustainability-score" role="progressbar" aria-label="progress" title="sustainability-score" aria-labelledby="sustainability-score" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">100</div>
                           </div>
                        </div>
                         </div>
                      </div>

                     <div class="tab-pane fade" id="more-info-tab-294572-tab" role="tabpanel" aria-labelledby="more-info-tab-294572">
                        <div class="new-rankings-indicator-wrap py-2">

                           <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Fees</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                -
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Scholarship</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                No
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Student Mix</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                Domestic 76%   International 24%
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">English Tests</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                <a href="javascript:void(0)" class="_openfilter_results_js">Generate Result</a>
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Academic Tests</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                <a href="javascript:void(0)" class="_openfilter_results_js">Generate Result</a>
                              </div>
                           </div>
                        </div>


                        </div>

                        <div class="signup-for-user signup-for-user-js d-none">
                           <p>In order to see the data <a href="javascript:void(0)" class="signup-for-user-js-dlyr" data-toggle="modal" data-target="#emailModal">Sign up for free</a></p>
                        </div>


                     </div>

                  </div>
               </div>


            </div>

         </div>
      </div>
   </div>

   <div class="ind firstloaded main ranking-row-js-294861" nid="294861">
      <div class="">
         <div class="new-ranking-cards  normal-row">

            <div class="left-div-200">
               <div class="rank-square height-97px dark-blue padding-top-24">
                  <span class="rank-title mobile-upper">Rank</span>
                  <span class="rank-no">
                     13
                     <span class="dagger-icon-new d-none">
                        <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/dagger.svg" alt="Dagger Icon">
                     </span>
                  </span>
               </div>
               <div class="height-1px">
               </div>
               
               


               <div class="rank-square height-163px light-blue padding-top-32 text-align-mobile">
                  
                  

                 

                 


                  <span class="rank-title di-inline">Overall Score:</span>
                  <span class="rank-score di-inline">88.9</span>
               </div>
            </div>

            <div class="right-div-200">

               <div class="row">
                  <div class="col-lg-7 col-md-12 col-sm-12">
                     <div class="university-details-name">

                        <div class="univ-names-text">
                           <span class="logo-wrapper new-rank ">
                              <a href="/universities/university-melbourne">
                                <img fetchpriority="low" loading="lazy" src="https://www.topuniversities.com/sites/default/files/211118103607am165180PRIMARY-A-A4-Vertical-Housed-RGB-200px-90x90.jpg" alt="The University of Melbourne" title="The University of Melbourne" height="78" width="78">
                              </a>
                           </span>

                           <a href="/universities/university-melbourne" class="uni-link">The University of Melbourne</a>

                           <div class="location">
                              <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/location.svg" height="12" width="12" alt="location" title="location"> Parkville,  Australia
                           </div>

                           <div class="stars d-none">
                             <span class="ranking-star">
                               <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/stars.svg" height="20" width="20" alt="QS stars" title="QS stars">
                             </span>
                             <span class="rating_number"></span>
                             <span class="qs-stars-font">QS Stars</span>
                           </div> 



                        </div>
                     </div>
                  </div>

               <div class="col-lg-5 col-md-12 col-sm-12">
                  <div class="shortlist-compare-div">
                     <div class="shortlist_div_new">
                        <a class="wishlist _directorypage shortlistnonloggedglobaljs   _shortlist_nid_294861  shortlistnonloggedglobaljs_dlyr" progoruniv="univ" nid="294861" onclick="Drupal.behaviors.tu_d8._adduniversityShortlist(this, 294861, 'university')">
                           <i class="fa fa-heart" aria-hidden="true"></i>
                           <i class="fal fa-heart" aria-hidden="true"></i>
                           <span class="_addShortText">Shortlist</span>
                        </a>
                     </div>

                     <div class="compare_div_new">
                        <a href="javascript:void(0)" class="compare _globCompUniv_js _globcompare_universityCookie_js_294861 comparenonloggedglobaljs_dlyr" nid="294861" progoruniv="univ" onclick="Drupal.behaviors.tu_d8._adduniversityCompare(this, 294861)">
                           <span class="two-square-icon">
                              <i class="fal fa-circle" aria-hidden="true"></i>
                           </span>
                           <span class="change-text">Compare</span>
                        </a>
                     </div>
                  </div>
               </div>

               </div>



               <div class="new-rankings-tab-content-wrapper">
                  <div class="arrows-left-right-tab arrows-left-right-tab-js">
                     <button class="btn-arrows btn-right-pick btn-arrows-js" scrollnid="294861" direction="right" aria-label="rightButton">
                        <img src="/modules/custom/qs_rankings_rest_api/assets/chevron-right.png" alt="Arrows">
                     </button>
                     <button class="btn-arrows btn-left-pick btn-arrows-js d-none" scrollnid="294861" direction="left" aria-label="leftButton">
                        <img src="/modules/custom/qs_rankings_rest_api/assets/chevron-left.png" alt="Arrows">
                     </button>
                  </div>
                  <ul class="nav nav-tabs m-0 scroll-this-side-294861-js" id="myTab" role="none">
                     <li class="nav-item ">
                                   <a class="nav-link active" id="research-discovery-294861" data-toggle="tab" href="#research-discovery-294861-tab">
                                   Research &amp; Discovery
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="learning-experience-294861" data-toggle="tab" href="#learning-experience-294861-tab">
                                   Learning Experience
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="employability-294861" data-toggle="tab" href="#employability-294861-tab">
                                   Employability
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="global-engagement-294861" data-toggle="tab" href="#global-engagement-294861-tab">
                                   Global Engagement
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="sustainability-294861" data-toggle="tab" href="#sustainability-294861-tab">
                                   Sustainability
                                   </a>
                                </li>
                     <li class="nav-item" role="none">
                        <a class="nav-link" id="more-info-tab-294861" data-toggle="tab" href="#more-info-tab-294861-tab">More Info
                           <span class="new-line">NEW</span>
                           <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/lock.svg" height="14" width="12" alt="lock" title="lock" class="lock-icon-checked-js d-none">
                        </a>
                     </li>
                  </ul>
                  <div class="tab-content py-2" id="myTabContent">

                     <div class="tab-pane fade show active" id="research-discovery-294861-tab" role="tabpanel" aria-labelledby="research-discovery-294861">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Academic Reputation</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="academic-reputation" role="progressbar" aria-label="progress" title="academic-reputation" aria-labelledby="academic-reputation" style="width: 98.5%" aria-valuenow="98.5" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">98.5</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Citations per Faculty</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="citations-per-faculty" role="progressbar" aria-label="progress" title="citations-per-faculty" aria-labelledby="citations-per-faculty" style="width: 93%" aria-valuenow="93" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">93</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="learning-experience-294861-tab" role="tabpanel" aria-labelledby="learning-experience-294861">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Faculty Student Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="faculty-student-ratio" role="progressbar" aria-label="progress" title="faculty-student-ratio" aria-labelledby="faculty-student-ratio" style="width: 15.4%" aria-valuenow="15.4" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">15.4</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="employability-294861-tab" role="tabpanel" aria-labelledby="employability-294861">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Employer Reputation</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="employer-reputation" role="progressbar" aria-label="progress" title="employer-reputation" aria-labelledby="employer-reputation" style="width: 93.9%" aria-valuenow="93.9" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">93.9</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Employment Outcomes</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="employment-outcomes" role="progressbar" aria-label="progress" title="employment-outcomes" aria-labelledby="employment-outcomes" style="width: 96.5%" aria-valuenow="96.5" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">96.5</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="global-engagement-294861-tab" role="tabpanel" aria-labelledby="global-engagement-294861">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Student Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-student-ratio" role="progressbar" aria-label="progress" title="international-student-ratio" aria-labelledby="international-student-ratio" style="width: 99.8%" aria-valuenow="99.8" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">99.8</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Research Network</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-research-network" role="progressbar" aria-label="progress" title="international-research-network" aria-labelledby="international-research-network" style="width: 97.4%" aria-valuenow="97.4" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">97.4</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Faculty Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-faculty-ratio" role="progressbar" aria-label="progress" title="international-faculty-ratio" aria-labelledby="international-faculty-ratio" style="width: 95.1%" aria-valuenow="95.1" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">95.1</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="sustainability-294861-tab" role="tabpanel" aria-labelledby="sustainability-294861">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Sustainability Score</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="sustainability-score" role="progressbar" aria-label="progress" title="sustainability-score" aria-labelledby="sustainability-score" style="width: 99.6%" aria-valuenow="99.6" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">99.6</div>
                           </div>
                        </div>
                         </div>
                      </div>

                     <div class="tab-pane fade" id="more-info-tab-294861-tab" role="tabpanel" aria-labelledby="more-info-tab-294861">
                        <div class="new-rankings-indicator-wrap py-2">

                           <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Fees</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                -
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Scholarship</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                Yes
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Student Mix</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                Domestic 52%   International 48%
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">English Tests</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                <a href="javascript:void(0)" class="_openfilter_results_js">Generate Result</a>
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Academic Tests</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                <a href="javascript:void(0)" class="_openfilter_results_js">Generate Result</a>
                              </div>
                           </div>
                        </div>


                        </div>

                        <div class="signup-for-user signup-for-user-js d-none">
                           <p>In order to see the data <a href="javascript:void(0)" class="signup-for-user-js-dlyr" data-toggle="modal" data-target="#emailModal">Sign up for free</a></p>
                        </div>


                     </div>

                  </div>
               </div>


            </div>

         </div>
      </div>
   </div>

   <div class="ind firstloaded main ranking-row-js-294606" nid="294606">
      <div class="">
         <div class="new-ranking-cards  normal-row">

            <div class="left-div-200">
               <div class="rank-square height-97px dark-blue padding-top-24">
                  <span class="rank-title mobile-upper">Rank</span>
                  <span class="rank-no">
                     14
                     <span class="dagger-icon-new d-none">
                        <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/dagger.svg" alt="Dagger Icon">
                     </span>
                  </span>
               </div>
               <div class="height-1px">
               </div>
               
               


               <div class="rank-square height-163px light-blue padding-top-32 text-align-mobile">
                  
                  

                 

                 


                  <span class="rank-title di-inline">Overall Score:</span>
                  <span class="rank-score di-inline">88.5</span>
               </div>
            </div>

            <div class="right-div-200">

               <div class="row">
                  <div class="col-lg-7 col-md-12 col-sm-12">
                     <div class="university-details-name">

                        <div class="univ-names-text">
                           <span class="logo-wrapper new-rank ">
                              <a href="/universities/peking-university">
                                <img fetchpriority="low" loading="lazy" src="https://www.topuniversities.com/sites/default/files/peking-university_50_medium.jpg" alt="Peking University" title="Peking University" height="78" width="78">
                              </a>
                           </span>

                           <a href="/universities/peking-university" class="uni-link">Peking University</a>

                           <div class="location">
                              <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/location.svg" height="12" width="12" alt="location" title="location"> Beijing,  China (Mainland)
                           </div>

                           <div class="stars d-none">
                             <span class="ranking-star">
                               <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/stars.svg" height="20" width="20" alt="QS stars" title="QS stars">
                             </span>
                             <span class="rating_number"></span>
                             <span class="qs-stars-font">QS Stars</span>
                           </div> 



                        </div>
                     </div>
                  </div>

               <div class="col-lg-5 col-md-12 col-sm-12">
                  <div class="shortlist-compare-div">
                     <div class="shortlist_div_new">
                        <a class="wishlist _directorypage shortlistnonloggedglobaljs   _shortlist_nid_294606  shortlistnonloggedglobaljs_dlyr" progoruniv="univ" nid="294606" onclick="Drupal.behaviors.tu_d8._adduniversityShortlist(this, 294606, 'university')">
                           <i class="fa fa-heart" aria-hidden="true"></i>
                           <i class="fal fa-heart" aria-hidden="true"></i>
                           <span class="_addShortText">Shortlist</span>
                        </a>
                     </div>

                     <div class="compare_div_new">
                        <a href="javascript:void(0)" class="compare _globCompUniv_js _globcompare_universityCookie_js_294606 comparenonloggedglobaljs_dlyr" nid="294606" progoruniv="univ" onclick="Drupal.behaviors.tu_d8._adduniversityCompare(this, 294606)">
                           <span class="two-square-icon">
                              <i class="fal fa-circle" aria-hidden="true"></i>
                           </span>
                           <span class="change-text">Compare</span>
                        </a>
                     </div>
                  </div>
               </div>

               </div>



               <div class="new-rankings-tab-content-wrapper">
                  <div class="arrows-left-right-tab arrows-left-right-tab-js">
                     <button class="btn-arrows btn-right-pick btn-arrows-js" scrollnid="294606" direction="right" aria-label="rightButton">
                        <img src="/modules/custom/qs_rankings_rest_api/assets/chevron-right.png" alt="Arrows">
                     </button>
                     <button class="btn-arrows btn-left-pick btn-arrows-js d-none" scrollnid="294606" direction="left" aria-label="leftButton">
                        <img src="/modules/custom/qs_rankings_rest_api/assets/chevron-left.png" alt="Arrows">
                     </button>
                  </div>
                  <ul class="nav nav-tabs m-0 scroll-this-side-294606-js" id="myTab" role="none">
                     <li class="nav-item ">
                                   <a class="nav-link active" id="research-discovery-294606" data-toggle="tab" href="#research-discovery-294606-tab">
                                   Research &amp; Discovery
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="learning-experience-294606" data-toggle="tab" href="#learning-experience-294606-tab">
                                   Learning Experience
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="employability-294606" data-toggle="tab" href="#employability-294606-tab">
                                   Employability
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="global-engagement-294606" data-toggle="tab" href="#global-engagement-294606-tab">
                                   Global Engagement
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="sustainability-294606" data-toggle="tab" href="#sustainability-294606-tab">
                                   Sustainability
                                   </a>
                                </li>
                     <li class="nav-item" role="none">
                        <a class="nav-link" id="more-info-tab-294606" data-toggle="tab" href="#more-info-tab-294606-tab">More Info
                           <span class="new-line">NEW</span>
                           <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/lock.svg" height="14" width="12" alt="lock" title="lock" class="lock-icon-checked-js d-none">
                        </a>
                     </li>
                  </ul>
                  <div class="tab-content py-2" id="myTabContent">

                     <div class="tab-pane fade show active" id="research-discovery-294606-tab" role="tabpanel" aria-labelledby="research-discovery-294606">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Academic Reputation</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="academic-reputation" role="progressbar" aria-label="progress" title="academic-reputation" aria-labelledby="academic-reputation" style="width: 99.5%" aria-valuenow="99.5" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">99.5</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Citations per Faculty</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="citations-per-faculty" role="progressbar" aria-label="progress" title="citations-per-faculty" aria-labelledby="citations-per-faculty" style="width: 97.7%" aria-valuenow="97.7" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">97.7</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="learning-experience-294606-tab" role="tabpanel" aria-labelledby="learning-experience-294606">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Faculty Student Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="faculty-student-ratio" role="progressbar" aria-label="progress" title="faculty-student-ratio" aria-labelledby="faculty-student-ratio" style="width: 92.6%" aria-valuenow="92.6" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">92.6</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="employability-294606-tab" role="tabpanel" aria-labelledby="employability-294606">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Employer Reputation</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="employer-reputation" role="progressbar" aria-label="progress" title="employer-reputation" aria-labelledby="employer-reputation" style="width: 96.6%" aria-valuenow="96.6" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">96.6</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Employment Outcomes</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="employment-outcomes" role="progressbar" aria-label="progress" title="employment-outcomes" aria-labelledby="employment-outcomes" style="width: 94.2%" aria-valuenow="94.2" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">94.2</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="global-engagement-294606-tab" role="tabpanel" aria-labelledby="global-engagement-294606">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Student Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-student-ratio" role="progressbar" aria-label="progress" title="international-student-ratio" aria-labelledby="international-student-ratio" style="width: 23.6%" aria-valuenow="23.6" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">23.6</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Research Network</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-research-network" role="progressbar" aria-label="progress" title="international-research-network" aria-labelledby="international-research-network" style="width: 79.8%" aria-valuenow="79.8" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">79.8</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Faculty Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-faculty-ratio" role="progressbar" aria-label="progress" title="international-faculty-ratio" aria-labelledby="international-faculty-ratio" style="width: 50.3%" aria-valuenow="50.3" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">50.3</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="sustainability-294606-tab" role="tabpanel" aria-labelledby="sustainability-294606">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Sustainability Score</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="sustainability-score" role="progressbar" aria-label="progress" title="sustainability-score" aria-labelledby="sustainability-score" style="width: 46.9%" aria-valuenow="46.9" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">46.9</div>
                           </div>
                        </div>
                         </div>
                      </div>

                     <div class="tab-pane fade" id="more-info-tab-294606-tab" role="tabpanel" aria-labelledby="more-info-tab-294606">
                        <div class="new-rankings-indicator-wrap py-2">

                           <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Fees</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                -
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Scholarship</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                No
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Student Mix</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                Domestic 85%   International 15%
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">English Tests</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                <a href="javascript:void(0)" class="_openfilter_results_js">Generate Result</a>
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Academic Tests</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                <a href="javascript:void(0)" class="_openfilter_results_js">Generate Result</a>
                              </div>
                           </div>
                        </div>


                        </div>

                        <div class="signup-for-user signup-for-user-js d-none">
                           <p>In order to see the data <a href="javascript:void(0)" class="signup-for-user-js-dlyr" data-toggle="modal" data-target="#emailModal">Sign up for free</a></p>
                        </div>


                     </div>

                  </div>
               </div>


            </div>

         </div>
      </div>
   </div>

   <div class="ind firstloaded main ranking-row-js-294821" nid="294821">
      <div class="">
         <div class="new-ranking-cards advanced_profile new normal-row">

            <div class="left-div-200">
               <div class="rank-square height-97px dark-blue padding-top-24">
                  <span class="rank-title mobile-upper">Rank</span>
                  <span class="rank-no">
                     15
                     <span class="dagger-icon-new d-none">
                        <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/dagger.svg" alt="Dagger Icon">
                     </span>
                  </span>
               </div>
               <div class="height-1px">
               </div>
               
               


               <div class="rank-square height-163px light-blue padding-top-32 text-align-mobile">
                  
                  

                 

                 


                  <span class="rank-title di-inline">Overall Score:</span>
                  <span class="rank-score di-inline">88.4</span>
               </div>
            </div>

            <div class="right-div-200">

               <div class="row">
                  <div class="col-lg-7 col-md-12 col-sm-12">
                     <div class="university-details-name">

                        <div class="univ-names-text">
                           <span class="logo-wrapper new-rank ">
                              <a href="/universities/nanyang-technological-university-singapore-ntu-singapore">
                                <img fetchpriority="low" loading="lazy" src="https://www.topuniversities.com/sites/default/files/nanyang-technological-university-singapore-ntu_592560cf2aeae70239af4c32_medium.jpg" alt="Nanyang Technological University, Singapore (NTU Singapore)" title="Nanyang Technological University, Singapore (NTU Singapore)" height="78" width="78">
                              </a>
                           </span>

                           <a href="/universities/nanyang-technological-university-singapore-ntu-singapore" class="uni-link">Nanyang Technological University, Singapore (NTU Singapore)</a>

                           <div class="location">
                              <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/location.svg" height="12" width="12" alt="location" title="location"> Singapore,  Singapore
                           </div>

                           <div class="stars d-none">
                             <span class="ranking-star">
                               <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/stars.svg" height="20" width="20" alt="QS stars" title="QS stars">
                             </span>
                             <span class="rating_number"></span>
                             <span class="qs-stars-font">QS Stars</span>
                           </div> 



                        </div>
                     </div>
                  </div>

               <div class="col-lg-5 col-md-12 col-sm-12">
                  <div class="shortlist-compare-div">
                     <div class="shortlist_div_new">
                        <a class="wishlist _directorypage shortlistnonloggedglobaljs   _shortlist_nid_294821  shortlistnonloggedglobaljs_dlyr" progoruniv="univ" nid="294821" onclick="Drupal.behaviors.tu_d8._adduniversityShortlist(this, 294821, 'university')">
                           <i class="fa fa-heart" aria-hidden="true"></i>
                           <i class="fal fa-heart" aria-hidden="true"></i>
                           <span class="_addShortText">Shortlist</span>
                        </a>
                     </div>

                     <div class="compare_div_new">
                        <a href="javascript:void(0)" class="compare _globCompUniv_js _globcompare_universityCookie_js_294821 comparenonloggedglobaljs_dlyr" nid="294821" progoruniv="univ" onclick="Drupal.behaviors.tu_d8._adduniversityCompare(this, 294821)">
                           <span class="two-square-icon">
                              <i class="fal fa-circle" aria-hidden="true"></i>
                           </span>
                           <span class="change-text">Compare</span>
                        </a>
                     </div>
                  </div>
               </div>

               </div>



               <div class="new-rankings-tab-content-wrapper">
                  <div class="arrows-left-right-tab arrows-left-right-tab-js">
                     <button class="btn-arrows btn-right-pick btn-arrows-js" scrollnid="294821" direction="right" aria-label="rightButton">
                        <img src="/modules/custom/qs_rankings_rest_api/assets/chevron-right.png" alt="Arrows">
                     </button>
                     <button class="btn-arrows btn-left-pick btn-arrows-js d-none" scrollnid="294821" direction="left" aria-label="leftButton">
                        <img src="/modules/custom/qs_rankings_rest_api/assets/chevron-left.png" alt="Arrows">
                     </button>
                  </div>
                  <ul class="nav nav-tabs m-0 scroll-this-side-294821-js" id="myTab" role="none">
                     <li class="nav-item ">
                                   <a class="nav-link active" id="research-discovery-294821" data-toggle="tab" href="#research-discovery-294821-tab">
                                   Research &amp; Discovery
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="learning-experience-294821" data-toggle="tab" href="#learning-experience-294821-tab">
                                   Learning Experience
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="employability-294821" data-toggle="tab" href="#employability-294821-tab">
                                   Employability
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="global-engagement-294821" data-toggle="tab" href="#global-engagement-294821-tab">
                                   Global Engagement
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="sustainability-294821" data-toggle="tab" href="#sustainability-294821-tab">
                                   Sustainability
                                   </a>
                                </li>
                     <li class="nav-item" role="none">
                        <a class="nav-link" id="more-info-tab-294821" data-toggle="tab" href="#more-info-tab-294821-tab">More Info
                           <span class="new-line">NEW</span>
                           <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/lock.svg" height="14" width="12" alt="lock" title="lock" class="lock-icon-checked-js d-none">
                        </a>
                     </li>
                  </ul>
                  <div class="tab-content py-2" id="myTabContent">

                     <div class="tab-pane fade show active" id="research-discovery-294821-tab" role="tabpanel" aria-labelledby="research-discovery-294821">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Academic Reputation</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="academic-reputation" role="progressbar" aria-label="progress" title="academic-reputation" aria-labelledby="academic-reputation" style="width: 91.9%" aria-valuenow="91.9" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">91.9</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Citations per Faculty</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="citations-per-faculty" role="progressbar" aria-label="progress" title="citations-per-faculty" aria-labelledby="citations-per-faculty" style="width: 92.4%" aria-valuenow="92.4" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">92.4</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="learning-experience-294821-tab" role="tabpanel" aria-labelledby="learning-experience-294821">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Faculty Student Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="faculty-student-ratio" role="progressbar" aria-label="progress" title="faculty-student-ratio" aria-labelledby="faculty-student-ratio" style="width: 80.6%" aria-valuenow="80.6" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">80.6</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="employability-294821-tab" role="tabpanel" aria-labelledby="employability-294821">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Employer Reputation</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="employer-reputation" role="progressbar" aria-label="progress" title="employer-reputation" aria-labelledby="employer-reputation" style="width: 73.3%" aria-valuenow="73.3" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">73.3</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Employment Outcomes</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="employment-outcomes" role="progressbar" aria-label="progress" title="employment-outcomes" aria-labelledby="employment-outcomes" style="width: 83.9%" aria-valuenow="83.9" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">83.9</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="global-engagement-294821-tab" role="tabpanel" aria-labelledby="global-engagement-294821">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Student Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-student-ratio" role="progressbar" aria-label="progress" title="international-student-ratio" aria-labelledby="international-student-ratio" style="width: 83.5%" aria-valuenow="83.5" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">83.5</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Research Network</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-research-network" role="progressbar" aria-label="progress" title="international-research-network" aria-labelledby="international-research-network" style="width: 89.4%" aria-valuenow="89.4" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">89.4</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Faculty Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-faculty-ratio" role="progressbar" aria-label="progress" title="international-faculty-ratio" aria-labelledby="international-faculty-ratio" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">100</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="sustainability-294821-tab" role="tabpanel" aria-labelledby="sustainability-294821">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Sustainability Score</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="sustainability-score" role="progressbar" aria-label="progress" title="sustainability-score" aria-labelledby="sustainability-score" style="width: 95.6%" aria-valuenow="95.6" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">95.6</div>
                           </div>
                        </div>
                         </div>
                      </div>

                     <div class="tab-pane fade" id="more-info-tab-294821-tab" role="tabpanel" aria-labelledby="more-info-tab-294821">
                        <div class="new-rankings-indicator-wrap py-2">

                           <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Fees</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                -
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Scholarship</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                No
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Student Mix</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                Domestic 69%   International 31%
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">English Tests</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                <a href="javascript:void(0)" class="_openfilter_results_js">Generate Result</a>
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Academic Tests</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                <a href="javascript:void(0)" class="_openfilter_results_js">Generate Result</a>
                              </div>
                           </div>
                        </div>


                        </div>

                        <div class="signup-for-user signup-for-user-js d-none">
                           <p>In order to see the data <a href="javascript:void(0)" class="signup-for-user-js-dlyr" data-toggle="modal" data-target="#emailModal">Sign up for free</a></p>
                        </div>


                     </div>

                  </div>
               </div>


            </div>

         </div>
      </div>
   </div>

   <div class="ind firstloaded main ranking-row-js-294514" nid="294514">
      <div class="">
         <div class="new-ranking-cards  normal-row">

            <div class="left-div-200">
               <div class="rank-square height-97px dark-blue padding-top-24">
                  <span class="rank-title mobile-upper">Rank</span>
                  <span class="rank-no">
                     16
                     <span class="dagger-icon-new d-none">
                        <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/dagger.svg" alt="Dagger Icon">
                     </span>
                  </span>
               </div>
               <div class="height-1px">
               </div>
               
               


               <div class="rank-square height-163px light-blue padding-top-32 text-align-mobile">
                  
                  

                 

                 


                  <span class="rank-title di-inline">Overall Score:</span>
                  <span class="rank-score di-inline">87.9</span>
               </div>
            </div>

            <div class="right-div-200">

               <div class="row">
                  <div class="col-lg-7 col-md-12 col-sm-12">
                     <div class="university-details-name">

                        <div class="univ-names-text">
                           <span class="logo-wrapper new-rank ">
                              <a href="/universities/cornell-university">
                                <img fetchpriority="low" loading="lazy" src="https://www.topuniversities.com/sites/default/files/cornell-university_143_medium.jpg" alt="Cornell University" title="Cornell University" height="78" width="78">
                              </a>
                           </span>

                           <a href="/universities/cornell-university" class="uni-link">Cornell University</a>

                           <div class="location">
                              <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/location.svg" height="12" width="12" alt="location" title="location"> Ithaca,  United States
                           </div>

                           <div class="stars d-none">
                             <span class="ranking-star">
                               <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/stars.svg" height="20" width="20" alt="QS stars" title="QS stars">
                             </span>
                             <span class="rating_number"></span>
                             <span class="qs-stars-font">QS Stars</span>
                           </div> 



                        </div>
                     </div>
                  </div>

               <div class="col-lg-5 col-md-12 col-sm-12">
                  <div class="shortlist-compare-div">
                     <div class="shortlist_div_new">
                        <a class="wishlist _directorypage shortlistnonloggedglobaljs   _shortlist_nid_294514  shortlistnonloggedglobaljs_dlyr" progoruniv="univ" nid="294514" onclick="Drupal.behaviors.tu_d8._adduniversityShortlist(this, 294514, 'university')">
                           <i class="fa fa-heart" aria-hidden="true"></i>
                           <i class="fal fa-heart" aria-hidden="true"></i>
                           <span class="_addShortText">Shortlist</span>
                        </a>
                     </div>

                     <div class="compare_div_new">
                        <a href="javascript:void(0)" class="compare _globCompUniv_js _globcompare_universityCookie_js_294514 comparenonloggedglobaljs_dlyr" nid="294514" progoruniv="univ" onclick="Drupal.behaviors.tu_d8._adduniversityCompare(this, 294514)">
                           <span class="two-square-icon">
                              <i class="fal fa-circle" aria-hidden="true"></i>
                           </span>
                           <span class="change-text">Compare</span>
                        </a>
                     </div>
                  </div>
               </div>

               </div>



               <div class="new-rankings-tab-content-wrapper">
                  <div class="arrows-left-right-tab arrows-left-right-tab-js">
                     <button class="btn-arrows btn-right-pick btn-arrows-js" scrollnid="294514" direction="right" aria-label="rightButton">
                        <img src="/modules/custom/qs_rankings_rest_api/assets/chevron-right.png" alt="Arrows">
                     </button>
                     <button class="btn-arrows btn-left-pick btn-arrows-js d-none" scrollnid="294514" direction="left" aria-label="leftButton">
                        <img src="/modules/custom/qs_rankings_rest_api/assets/chevron-left.png" alt="Arrows">
                     </button>
                  </div>
                  <ul class="nav nav-tabs m-0 scroll-this-side-294514-js" id="myTab" role="none">
                     <li class="nav-item ">
                                   <a class="nav-link active" id="research-discovery-294514" data-toggle="tab" href="#research-discovery-294514-tab">
                                   Research &amp; Discovery
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="learning-experience-294514" data-toggle="tab" href="#learning-experience-294514-tab">
                                   Learning Experience
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="employability-294514" data-toggle="tab" href="#employability-294514-tab">
                                   Employability
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="global-engagement-294514" data-toggle="tab" href="#global-engagement-294514-tab">
                                   Global Engagement
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="sustainability-294514" data-toggle="tab" href="#sustainability-294514-tab">
                                   Sustainability
                                   </a>
                                </li>
                     <li class="nav-item" role="none">
                        <a class="nav-link" id="more-info-tab-294514" data-toggle="tab" href="#more-info-tab-294514-tab">More Info
                           <span class="new-line">NEW</span>
                           <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/lock.svg" height="14" width="12" alt="lock" title="lock" class="lock-icon-checked-js d-none">
                        </a>
                     </li>
                  </ul>
                  <div class="tab-content py-2" id="myTabContent">

                     <div class="tab-pane fade show active" id="research-discovery-294514-tab" role="tabpanel" aria-labelledby="research-discovery-294514">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Academic Reputation</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="academic-reputation" role="progressbar" aria-label="progress" title="academic-reputation" aria-labelledby="academic-reputation" style="width: 98.3%" aria-valuenow="98.3" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">98.3</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Citations per Faculty</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="citations-per-faculty" role="progressbar" aria-label="progress" title="citations-per-faculty" aria-labelledby="citations-per-faculty" style="width: 97.5%" aria-valuenow="97.5" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">97.5</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="learning-experience-294514-tab" role="tabpanel" aria-labelledby="learning-experience-294514">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Faculty Student Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="faculty-student-ratio" role="progressbar" aria-label="progress" title="faculty-student-ratio" aria-labelledby="faculty-student-ratio" style="width: 52.7%" aria-valuenow="52.7" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">52.7</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="employability-294514-tab" role="tabpanel" aria-labelledby="employability-294514">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Employer Reputation</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="employer-reputation" role="progressbar" aria-label="progress" title="employer-reputation" aria-labelledby="employer-reputation" style="width: 93.1%" aria-valuenow="93.1" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">93.1</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Employment Outcomes</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="employment-outcomes" role="progressbar" aria-label="progress" title="employment-outcomes" aria-labelledby="employment-outcomes" style="width: 97.1%" aria-valuenow="97.1" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">97.1</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="global-engagement-294514-tab" role="tabpanel" aria-labelledby="global-engagement-294514">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Student Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-student-ratio" role="progressbar" aria-label="progress" title="international-student-ratio" aria-labelledby="international-student-ratio" style="width: 63.4%" aria-valuenow="63.4" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">63.4</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Research Network</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-research-network" role="progressbar" aria-label="progress" title="international-research-network" aria-labelledby="international-research-network" style="width: 94%" aria-valuenow="94" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">94</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Faculty Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-faculty-ratio" role="progressbar" aria-label="progress" title="international-faculty-ratio" aria-labelledby="international-faculty-ratio" style="width: 54.2%" aria-valuenow="54.2" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">54.2</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="sustainability-294514-tab" role="tabpanel" aria-labelledby="sustainability-294514">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Sustainability Score</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="sustainability-score" role="progressbar" aria-label="progress" title="sustainability-score" aria-labelledby="sustainability-score" style="width: 72.1%" aria-valuenow="72.1" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">72.1</div>
                           </div>
                        </div>
                         </div>
                      </div>

                     <div class="tab-pane fade" id="more-info-tab-294514-tab" role="tabpanel" aria-labelledby="more-info-tab-294514">
                        <div class="new-rankings-indicator-wrap py-2">

                           <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Fees</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                -
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Scholarship</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                Yes
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Student Mix</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                Domestic 75%   International 25%
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">English Tests</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                <a href="javascript:void(0)" class="_openfilter_results_js">Generate Result</a>
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Academic Tests</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                <a href="javascript:void(0)" class="_openfilter_results_js">Generate Result</a>
                              </div>
                           </div>
                        </div>


                        </div>

                        <div class="signup-for-user signup-for-user-js d-none">
                           <p>In order to see the data <a href="javascript:void(0)" class="signup-for-user-js-dlyr" data-toggle="modal" data-target="#emailModal">Sign up for free</a></p>
                        </div>


                     </div>

                  </div>
               </div>


            </div>

         </div>
      </div>
   </div>

   <div class="ind firstloaded main ranking-row-js-294256" nid="294256">
      <div class="">
         <div class="new-ranking-cards  normal-row">

            <div class="left-div-200">
               <div class="rank-square height-97px dark-blue padding-top-24">
                  <span class="rank-title mobile-upper">Rank</span>
                  <span class="rank-no">
                     17
                     <span class="dagger-icon-new d-none">
                        <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/dagger.svg" alt="Dagger Icon">
                     </span>
                  </span>
               </div>
               <div class="height-1px">
               </div>
               
               


               <div class="rank-square height-163px light-blue padding-top-32 text-align-mobile">
                  
                  

                 

                 


                  <span class="rank-title di-inline">Overall Score:</span>
                  <span class="rank-score di-inline">87.6</span>
               </div>
            </div>

            <div class="right-div-200">

               <div class="row">
                  <div class="col-lg-7 col-md-12 col-sm-12">
                     <div class="university-details-name">

                        <div class="univ-names-text">
                           <span class="logo-wrapper new-rank ">
                              <a href="/universities/university-hong-kong">
                                <img fetchpriority="low" loading="lazy" src="https://www.topuniversities.com/sites/default/files/the-university-of-hong-kong_268_medium.jpg" alt="The University of Hong Kong" title="The University of Hong Kong" height="78" width="78">
                              </a>
                           </span>

                           <a href="/universities/university-hong-kong" class="uni-link">The University of Hong Kong</a>

                           <div class="location">
                              <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/location.svg" height="12" width="12" alt="location" title="location"> Hong Kong,  Hong Kong SAR
                           </div>

                           <div class="stars d-none">
                             <span class="ranking-star">
                               <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/stars.svg" height="20" width="20" alt="QS stars" title="QS stars">
                             </span>
                             <span class="rating_number"></span>
                             <span class="qs-stars-font">QS Stars</span>
                           </div> 



                        </div>
                     </div>
                  </div>

               <div class="col-lg-5 col-md-12 col-sm-12">
                  <div class="shortlist-compare-div">
                     <div class="shortlist_div_new">
                        <a class="wishlist _directorypage shortlistnonloggedglobaljs   _shortlist_nid_294256  shortlistnonloggedglobaljs_dlyr" progoruniv="univ" nid="294256" onclick="Drupal.behaviors.tu_d8._adduniversityShortlist(this, 294256, 'university')">
                           <i class="fa fa-heart" aria-hidden="true"></i>
                           <i class="fal fa-heart" aria-hidden="true"></i>
                           <span class="_addShortText">Shortlist</span>
                        </a>
                     </div>

                     <div class="compare_div_new">
                        <a href="javascript:void(0)" class="compare _globCompUniv_js _globcompare_universityCookie_js_294256 comparenonloggedglobaljs_dlyr" nid="294256" progoruniv="univ" onclick="Drupal.behaviors.tu_d8._adduniversityCompare(this, 294256)">
                           <span class="two-square-icon">
                              <i class="fal fa-circle" aria-hidden="true"></i>
                           </span>
                           <span class="change-text">Compare</span>
                        </a>
                     </div>
                  </div>
               </div>

               </div>



               <div class="new-rankings-tab-content-wrapper">
                  <div class="arrows-left-right-tab arrows-left-right-tab-js">
                     <button class="btn-arrows btn-right-pick btn-arrows-js" scrollnid="294256" direction="right" aria-label="rightButton">
                        <img src="/modules/custom/qs_rankings_rest_api/assets/chevron-right.png" alt="Arrows">
                     </button>
                     <button class="btn-arrows btn-left-pick btn-arrows-js d-none" scrollnid="294256" direction="left" aria-label="leftButton">
                        <img src="/modules/custom/qs_rankings_rest_api/assets/chevron-left.png" alt="Arrows">
                     </button>
                  </div>
                  <ul class="nav nav-tabs m-0 scroll-this-side-294256-js" id="myTab" role="none">
                     <li class="nav-item ">
                                   <a class="nav-link active" id="research-discovery-294256" data-toggle="tab" href="#research-discovery-294256-tab">
                                   Research &amp; Discovery
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="learning-experience-294256" data-toggle="tab" href="#learning-experience-294256-tab">
                                   Learning Experience
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="employability-294256" data-toggle="tab" href="#employability-294256-tab">
                                   Employability
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="global-engagement-294256" data-toggle="tab" href="#global-engagement-294256-tab">
                                   Global Engagement
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="sustainability-294256" data-toggle="tab" href="#sustainability-294256-tab">
                                   Sustainability
                                   </a>
                                </li>
                     <li class="nav-item" role="none">
                        <a class="nav-link" id="more-info-tab-294256" data-toggle="tab" href="#more-info-tab-294256-tab">More Info
                           <span class="new-line">NEW</span>
                           <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/lock.svg" height="14" width="12" alt="lock" title="lock" class="lock-icon-checked-js d-none">
                        </a>
                     </li>
                  </ul>
                  <div class="tab-content py-2" id="myTabContent">

                     <div class="tab-pane fade show active" id="research-discovery-294256-tab" role="tabpanel" aria-labelledby="research-discovery-294256">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Academic Reputation</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="academic-reputation" role="progressbar" aria-label="progress" title="academic-reputation" aria-labelledby="academic-reputation" style="width: 97.4%" aria-valuenow="97.4" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">97.4</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Citations per Faculty</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="citations-per-faculty" role="progressbar" aria-label="progress" title="citations-per-faculty" aria-labelledby="citations-per-faculty" style="width: 86.4%" aria-valuenow="86.4" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">86.4</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="learning-experience-294256-tab" role="tabpanel" aria-labelledby="learning-experience-294256">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Faculty Student Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="faculty-student-ratio" role="progressbar" aria-label="progress" title="faculty-student-ratio" aria-labelledby="faculty-student-ratio" style="width: 81.2%" aria-valuenow="81.2" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">81.2</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="employability-294256-tab" role="tabpanel" aria-labelledby="employability-294256">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Employer Reputation</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="employer-reputation" role="progressbar" aria-label="progress" title="employer-reputation" aria-labelledby="employer-reputation" style="width: 59.4%" aria-valuenow="59.4" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">59.4</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Employment Outcomes</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="employment-outcomes" role="progressbar" aria-label="progress" title="employment-outcomes" aria-labelledby="employment-outcomes" style="width: 99.7%" aria-valuenow="99.7" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">99.7</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="global-engagement-294256-tab" role="tabpanel" aria-labelledby="global-engagement-294256">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Student Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-student-ratio" role="progressbar" aria-label="progress" title="international-student-ratio" aria-labelledby="international-student-ratio" style="width: 99.3%" aria-valuenow="99.3" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">99.3</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Research Network</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-research-network" role="progressbar" aria-label="progress" title="international-research-network" aria-labelledby="international-research-network" style="width: 81.4%" aria-valuenow="81.4" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">81.4</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Faculty Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-faculty-ratio" role="progressbar" aria-label="progress" title="international-faculty-ratio" aria-labelledby="international-faculty-ratio" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">100</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="sustainability-294256-tab" role="tabpanel" aria-labelledby="sustainability-294256">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Sustainability Score</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="sustainability-score" role="progressbar" aria-label="progress" title="sustainability-score" aria-labelledby="sustainability-score" style="width: 89.2%" aria-valuenow="89.2" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">89.2</div>
                           </div>
                        </div>
                         </div>
                      </div>

                     <div class="tab-pane fade" id="more-info-tab-294256-tab" role="tabpanel" aria-labelledby="more-info-tab-294256">
                        <div class="new-rankings-indicator-wrap py-2">

                           <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Fees</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                -
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Scholarship</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                Yes
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Student Mix</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                Domestic 55%   International 45%
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">English Tests</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                <a href="javascript:void(0)" class="_openfilter_results_js">Generate Result</a>
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Academic Tests</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                <a href="javascript:void(0)" class="_openfilter_results_js">Generate Result</a>
                              </div>
                           </div>
                        </div>


                        </div>

                        <div class="signup-for-user signup-for-user-js d-none">
                           <p>In order to see the data <a href="javascript:void(0)" class="signup-for-user-js-dlyr" data-toggle="modal" data-target="#emailModal">Sign up for free</a></p>
                        </div>


                     </div>

                  </div>
               </div>


            </div>

         </div>
      </div>
   </div>

   <div class="ind firstloaded main ranking-row-js-296815" nid="296815">
      <div class="">
         <div class="new-ranking-cards advanced_profile new normal-row">

            <div class="left-div-200">
               <div class="rank-square height-97px dark-blue padding-top-24">
                  <span class="rank-title mobile-upper">Rank</span>
                  <span class="rank-no">
                     18
                     <span class="dagger-icon-new d-none">
                        <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/dagger.svg" alt="Dagger Icon">
                     </span>
                  </span>
               </div>
               <div class="height-1px">
               </div>
               
               


               <div class="rank-square height-163px light-blue padding-top-32 text-align-mobile">
                  
                  

                 

                 


                  <span class="rank-title di-inline">Overall Score:</span>
                  <span class="rank-score di-inline">87.3</span>
               </div>
            </div>

            <div class="right-div-200">

               <div class="row">
                  <div class="col-lg-7 col-md-12 col-sm-12">
                     <div class="university-details-name">

                        <div class="univ-names-text">
                           <span class="logo-wrapper new-rank ">
                              <a href="/universities/university-sydney">
                                <img fetchpriority="low" loading="lazy" src="https://www.topuniversities.com/sites/default/files/the-university-of-sydney_592560cf2aeae70239af4cd0_medium.jpg" alt="The University of Sydney" title="The University of Sydney" height="78" width="78">
                              </a>
                           </span>

                           <a href="/universities/university-sydney" class="uni-link">The University of Sydney</a>

                           <div class="location">
                              <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/location.svg" height="12" width="12" alt="location" title="location"> Sydney,  Australia
                           </div>

                           <div class="stars d-none">
                             <span class="ranking-star">
                               <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/stars.svg" height="20" width="20" alt="QS stars" title="QS stars">
                             </span>
                             <span class="rating_number"></span>
                             <span class="qs-stars-font">QS Stars</span>
                           </div> 



                        </div>
                     </div>
                  </div>

               <div class="col-lg-5 col-md-12 col-sm-12">
                  <div class="shortlist-compare-div">
                     <div class="shortlist_div_new">
                        <a class="wishlist _directorypage shortlistnonloggedglobaljs   _shortlist_nid_296815  shortlistnonloggedglobaljs_dlyr" progoruniv="univ" nid="296815" onclick="Drupal.behaviors.tu_d8._adduniversityShortlist(this, 296815, 'university')">
                           <i class="fa fa-heart" aria-hidden="true"></i>
                           <i class="fal fa-heart" aria-hidden="true"></i>
                           <span class="_addShortText">Shortlist</span>
                        </a>
                     </div>

                     <div class="compare_div_new">
                        <a href="javascript:void(0)" class="compare _globCompUniv_js _globcompare_universityCookie_js_296815 comparenonloggedglobaljs_dlyr" nid="296815" progoruniv="univ" onclick="Drupal.behaviors.tu_d8._adduniversityCompare(this, 296815)">
                           <span class="two-square-icon">
                              <i class="fal fa-circle" aria-hidden="true"></i>
                           </span>
                           <span class="change-text">Compare</span>
                        </a>
                     </div>
                  </div>
               </div>

               </div>



               <div class="new-rankings-tab-content-wrapper">
                  <div class="arrows-left-right-tab arrows-left-right-tab-js">
                     <button class="btn-arrows btn-right-pick btn-arrows-js" scrollnid="296815" direction="right" aria-label="rightButton">
                        <img src="/modules/custom/qs_rankings_rest_api/assets/chevron-right.png" alt="Arrows">
                     </button>
                     <button class="btn-arrows btn-left-pick btn-arrows-js d-none" scrollnid="296815" direction="left" aria-label="leftButton">
                        <img src="/modules/custom/qs_rankings_rest_api/assets/chevron-left.png" alt="Arrows">
                     </button>
                  </div>
                  <ul class="nav nav-tabs m-0 scroll-this-side-296815-js" id="myTab" role="none">
                     <li class="nav-item ">
                                   <a class="nav-link active" id="research-discovery-296815" data-toggle="tab" href="#research-discovery-296815-tab">
                                   Research &amp; Discovery
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="learning-experience-296815" data-toggle="tab" href="#learning-experience-296815-tab">
                                   Learning Experience
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="employability-296815" data-toggle="tab" href="#employability-296815-tab">
                                   Employability
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="global-engagement-296815" data-toggle="tab" href="#global-engagement-296815-tab">
                                   Global Engagement
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="sustainability-296815" data-toggle="tab" href="#sustainability-296815-tab">
                                   Sustainability
                                   </a>
                                </li>
                     <li class="nav-item" role="none">
                        <a class="nav-link" id="more-info-tab-296815" data-toggle="tab" href="#more-info-tab-296815-tab">More Info
                           <span class="new-line">NEW</span>
                           <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/lock.svg" height="14" width="12" alt="lock" title="lock" class="lock-icon-checked-js d-none">
                        </a>
                     </li>
                  </ul>
                  <div class="tab-content py-2" id="myTabContent">

                     <div class="tab-pane fade show active" id="research-discovery-296815-tab" role="tabpanel" aria-labelledby="research-discovery-296815">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Academic Reputation</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="academic-reputation" role="progressbar" aria-label="progress" title="academic-reputation" aria-labelledby="academic-reputation" style="width: 96.4%" aria-valuenow="96.4" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">96.4</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Citations per Faculty</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="citations-per-faculty" role="progressbar" aria-label="progress" title="citations-per-faculty" aria-labelledby="citations-per-faculty" style="width: 93.7%" aria-valuenow="93.7" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">93.7</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="learning-experience-296815-tab" role="tabpanel" aria-labelledby="learning-experience-296815">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Faculty Student Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="faculty-student-ratio" role="progressbar" aria-label="progress" title="faculty-student-ratio" aria-labelledby="faculty-student-ratio" style="width: 10.9%" aria-valuenow="10.9" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">10.9</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="employability-296815-tab" role="tabpanel" aria-labelledby="employability-296815">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Employer Reputation</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="employer-reputation" role="progressbar" aria-label="progress" title="employer-reputation" aria-labelledby="employer-reputation" style="width: 90%" aria-valuenow="90" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">90</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Employment Outcomes</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="employment-outcomes" role="progressbar" aria-label="progress" title="employment-outcomes" aria-labelledby="employment-outcomes" style="width: 93.1%" aria-valuenow="93.1" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">93.1</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="global-engagement-296815-tab" role="tabpanel" aria-labelledby="global-engagement-296815">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Student Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-student-ratio" role="progressbar" aria-label="progress" title="international-student-ratio" aria-labelledby="international-student-ratio" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">100</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Research Network</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-research-network" role="progressbar" aria-label="progress" title="international-research-network" aria-labelledby="international-research-network" style="width: 95.8%" aria-valuenow="95.8" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">95.8</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Faculty Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-faculty-ratio" role="progressbar" aria-label="progress" title="international-faculty-ratio" aria-labelledby="international-faculty-ratio" style="width: 99.9%" aria-valuenow="99.9" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">99.9</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="sustainability-296815-tab" role="tabpanel" aria-labelledby="sustainability-296815">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Sustainability Score</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="sustainability-score" role="progressbar" aria-label="progress" title="sustainability-score" aria-labelledby="sustainability-score" style="width: 99.6%" aria-valuenow="99.6" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">99.6</div>
                           </div>
                        </div>
                         </div>
                      </div>

                     <div class="tab-pane fade" id="more-info-tab-296815-tab" role="tabpanel" aria-labelledby="more-info-tab-296815">
                        <div class="new-rankings-indicator-wrap py-2">

                           <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Fees</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                -
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Scholarship</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                Yes
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Student Mix</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                Domestic 39%   International 61%
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">English Tests</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                <a href="javascript:void(0)" class="_openfilter_results_js">Generate Result</a>
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Academic Tests</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                <a href="javascript:void(0)" class="_openfilter_results_js">Generate Result</a>
                              </div>
                           </div>
                        </div>


                        </div>

                        <div class="signup-for-user signup-for-user-js d-none">
                           <p>In order to see the data <a href="javascript:void(0)" class="signup-for-user-js-dlyr" data-toggle="modal" data-target="#emailModal">Sign up for free</a></p>
                        </div>


                     </div>

                  </div>
               </div>


            </div>

         </div>
      </div>
   </div>

   <div class="ind firstloaded main ranking-row-js-294788" nid="294788">
      <div class="">
         <div class="new-ranking-cards advanced_profile new normal-row">

            <div class="left-div-200">
               <div class="rank-square height-97px dark-blue padding-top-24">
                  <span class="rank-title mobile-upper">Rank</span>
                  <span class="rank-no">
                     19
                     <span class="dagger-icon-new d-none">
                        <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/dagger.svg" alt="Dagger Icon">
                     </span>
                  </span>
               </div>
               <div class="height-1px">
               </div>
               
               


               <div class="rank-square height-163px light-blue padding-top-32 text-align-mobile">
                  
                  

                 

                 


                  <span class="rank-title di-inline">Overall Score:</span>
                  <span class="rank-score di-inline">87.1</span>
               </div>
            </div>

            <div class="right-div-200">

               <div class="row">
                  <div class="col-lg-7 col-md-12 col-sm-12">
                     <div class="university-details-name">

                        <div class="univ-names-text">
                           <span class="logo-wrapper new-rank ">
                              <a href="/universities/university-new-south-wales-unsw-sydney">
                                <img fetchpriority="low" loading="lazy" src="https://www.topuniversities.com/sites/default/files/221220094647am317557UNSW-Sydney-Logo-jpeg-90x90.jpg" alt="The University of New South Wales (UNSW Sydney)" title="The University of New South Wales (UNSW Sydney)" height="78" width="78">
                              </a>
                           </span>

                           <a href="/universities/university-new-south-wales-unsw-sydney" class="uni-link">The University of New South Wales (UNSW Sydney)</a>

                           <div class="location">
                              <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/location.svg" height="12" width="12" alt="location" title="location"> Sydney,  Australia
                           </div>

                           <div class="stars d-none">
                             <span class="ranking-star">
                               <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/stars.svg" height="20" width="20" alt="QS stars" title="QS stars">
                             </span>
                             <span class="rating_number"></span>
                             <span class="qs-stars-font">QS Stars</span>
                           </div> 



                        </div>
                     </div>
                  </div>

               <div class="col-lg-5 col-md-12 col-sm-12">
                  <div class="shortlist-compare-div">
                     <div class="shortlist_div_new">
                        <a class="wishlist _directorypage shortlistnonloggedglobaljs   _shortlist_nid_294788  shortlistnonloggedglobaljs_dlyr" progoruniv="univ" nid="294788" onclick="Drupal.behaviors.tu_d8._adduniversityShortlist(this, 294788, 'university')">
                           <i class="fa fa-heart" aria-hidden="true"></i>
                           <i class="fal fa-heart" aria-hidden="true"></i>
                           <span class="_addShortText">Shortlist</span>
                        </a>
                     </div>

                     <div class="compare_div_new">
                        <a href="javascript:void(0)" class="compare _globCompUniv_js _globcompare_universityCookie_js_294788 comparenonloggedglobaljs_dlyr" nid="294788" progoruniv="univ" onclick="Drupal.behaviors.tu_d8._adduniversityCompare(this, 294788)">
                           <span class="two-square-icon">
                              <i class="fal fa-circle" aria-hidden="true"></i>
                           </span>
                           <span class="change-text">Compare</span>
                        </a>
                     </div>
                  </div>
               </div>

               </div>



               <div class="new-rankings-tab-content-wrapper">
                  <div class="arrows-left-right-tab arrows-left-right-tab-js">
                     <button class="btn-arrows btn-right-pick btn-arrows-js" scrollnid="294788" direction="right" aria-label="rightButton">
                        <img src="/modules/custom/qs_rankings_rest_api/assets/chevron-right.png" alt="Arrows">
                     </button>
                     <button class="btn-arrows btn-left-pick btn-arrows-js d-none" scrollnid="294788" direction="left" aria-label="leftButton">
                        <img src="/modules/custom/qs_rankings_rest_api/assets/chevron-left.png" alt="Arrows">
                     </button>
                  </div>
                  <ul class="nav nav-tabs m-0 scroll-this-side-294788-js" id="myTab" role="none">
                     <li class="nav-item ">
                                   <a class="nav-link active" id="research-discovery-294788" data-toggle="tab" href="#research-discovery-294788-tab">
                                   Research &amp; Discovery
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="learning-experience-294788" data-toggle="tab" href="#learning-experience-294788-tab">
                                   Learning Experience
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="employability-294788" data-toggle="tab" href="#employability-294788-tab">
                                   Employability
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="global-engagement-294788" data-toggle="tab" href="#global-engagement-294788-tab">
                                   Global Engagement
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="sustainability-294788" data-toggle="tab" href="#sustainability-294788-tab">
                                   Sustainability
                                   </a>
                                </li>
                     <li class="nav-item" role="none">
                        <a class="nav-link" id="more-info-tab-294788" data-toggle="tab" href="#more-info-tab-294788-tab">More Info
                           <span class="new-line">NEW</span>
                           <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/lock.svg" height="14" width="12" alt="lock" title="lock" class="lock-icon-checked-js d-none">
                        </a>
                     </li>
                  </ul>
                  <div class="tab-content py-2" id="myTabContent">

                     <div class="tab-pane fade show active" id="research-discovery-294788-tab" role="tabpanel" aria-labelledby="research-discovery-294788">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Academic Reputation</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="academic-reputation" role="progressbar" aria-label="progress" title="academic-reputation" aria-labelledby="academic-reputation" style="width: 90.5%" aria-valuenow="90.5" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">90.5</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Citations per Faculty</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="citations-per-faculty" role="progressbar" aria-label="progress" title="citations-per-faculty" aria-labelledby="citations-per-faculty" style="width: 94.9%" aria-valuenow="94.9" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">94.9</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="learning-experience-294788-tab" role="tabpanel" aria-labelledby="learning-experience-294788">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Faculty Student Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="faculty-student-ratio" role="progressbar" aria-label="progress" title="faculty-student-ratio" aria-labelledby="faculty-student-ratio" style="width: 20.6%" aria-valuenow="20.6" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">20.6</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="employability-294788-tab" role="tabpanel" aria-labelledby="employability-294788">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Employer Reputation</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="employer-reputation" role="progressbar" aria-label="progress" title="employer-reputation" aria-labelledby="employer-reputation" style="width: 90.4%" aria-valuenow="90.4" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">90.4</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Employment Outcomes</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="employment-outcomes" role="progressbar" aria-label="progress" title="employment-outcomes" aria-labelledby="employment-outcomes" style="width: 97.7%" aria-valuenow="97.7" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">97.7</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="global-engagement-294788-tab" role="tabpanel" aria-labelledby="global-engagement-294788">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Student Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-student-ratio" role="progressbar" aria-label="progress" title="international-student-ratio" aria-labelledby="international-student-ratio" style="width: 99.4%" aria-valuenow="99.4" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">99.4</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Research Network</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-research-network" role="progressbar" aria-label="progress" title="international-research-network" aria-labelledby="international-research-network" style="width: 98.3%" aria-valuenow="98.3" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">98.3</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Faculty Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-faculty-ratio" role="progressbar" aria-label="progress" title="international-faculty-ratio" aria-labelledby="international-faculty-ratio" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">100</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="sustainability-294788-tab" role="tabpanel" aria-labelledby="sustainability-294788">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Sustainability Score</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="sustainability-score" role="progressbar" aria-label="progress" title="sustainability-score" aria-labelledby="sustainability-score" style="width: 99.2%" aria-valuenow="99.2" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">99.2</div>
                           </div>
                        </div>
                         </div>
                      </div>

                     <div class="tab-pane fade" id="more-info-tab-294788-tab" role="tabpanel" aria-labelledby="more-info-tab-294788">
                        <div class="new-rankings-indicator-wrap py-2">

                           <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Fees</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                -
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Scholarship</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                Yes
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Student Mix</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                Domestic 54%   International 46%
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">English Tests</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                <a href="javascript:void(0)" class="_openfilter_results_js">Generate Result</a>
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Academic Tests</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                <a href="javascript:void(0)" class="_openfilter_results_js">Generate Result</a>
                              </div>
                           </div>
                        </div>


                        </div>

                        <div class="signup-for-user signup-for-user-js d-none">
                           <p>In order to see the data <a href="javascript:void(0)" class="signup-for-user-js-dlyr" data-toggle="modal" data-target="#emailModal">Sign up for free</a></p>
                        </div>


                     </div>

                  </div>
               </div>


            </div>

         </div>
      </div>
   </div>

   <div class="ind firstloaded main ranking-row-js-297235 before_ad_3" nid="297235">
      <div class="">
         <div class="new-ranking-cards  normal-row">

            <div class="left-div-200">
               <div class="rank-square height-97px dark-blue padding-top-24">
                  <span class="rank-title mobile-upper">Rank</span>
                  <span class="rank-no">
                     20
                     <span class="dagger-icon-new d-none">
                        <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/dagger.svg" alt="Dagger Icon">
                     </span>
                  </span>
               </div>
               <div class="height-1px">
               </div>
               
               


               <div class="rank-square height-163px light-blue padding-top-32 text-align-mobile">
                  
                  

                 

                 


                  <span class="rank-title di-inline">Overall Score:</span>
                  <span class="rank-score di-inline">86.5</span>
               </div>
            </div>

            <div class="right-div-200">

               <div class="row">
                  <div class="col-lg-7 col-md-12 col-sm-12">
                     <div class="university-details-name">

                        <div class="univ-names-text">
                           <span class="logo-wrapper new-rank ">
                              <a href="/universities/tsinghua-university">
                                <img fetchpriority="low" loading="lazy" src="https://www.topuniversities.com/sites/default/files/tsinghua-university_626_medium.jpg" alt="Tsinghua University" title="Tsinghua University" height="78" width="78">
                              </a>
                           </span>

                           <a href="/universities/tsinghua-university" class="uni-link">Tsinghua University</a>

                           <div class="location">
                              <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/location.svg" height="12" width="12" alt="location" title="location"> Beijing,  China (Mainland)
                           </div>

                           <div class="stars d-none">
                             <span class="ranking-star">
                               <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/stars.svg" height="20" width="20" alt="QS stars" title="QS stars">
                             </span>
                             <span class="rating_number"></span>
                             <span class="qs-stars-font">QS Stars</span>
                           </div> 



                        </div>
                     </div>
                  </div>

               <div class="col-lg-5 col-md-12 col-sm-12">
                  <div class="shortlist-compare-div">
                     <div class="shortlist_div_new">
                        <a class="wishlist _directorypage shortlistnonloggedglobaljs   _shortlist_nid_297235  shortlistnonloggedglobaljs_dlyr" progoruniv="univ" nid="297235" onclick="Drupal.behaviors.tu_d8._adduniversityShortlist(this, 297235, 'university')">
                           <i class="fa fa-heart" aria-hidden="true"></i>
                           <i class="fal fa-heart" aria-hidden="true"></i>
                           <span class="_addShortText">Shortlist</span>
                        </a>
                     </div>

                     <div class="compare_div_new">
                        <a href="javascript:void(0)" class="compare _globCompUniv_js _globcompare_universityCookie_js_297235 comparenonloggedglobaljs_dlyr" nid="297235" progoruniv="univ" onclick="Drupal.behaviors.tu_d8._adduniversityCompare(this, 297235)">
                           <span class="two-square-icon">
                              <i class="fal fa-circle" aria-hidden="true"></i>
                           </span>
                           <span class="change-text">Compare</span>
                        </a>
                     </div>
                  </div>
               </div>

               </div>



               <div class="new-rankings-tab-content-wrapper">
                  <div class="arrows-left-right-tab arrows-left-right-tab-js">
                     <button class="btn-arrows btn-right-pick btn-arrows-js" scrollnid="297235" direction="right" aria-label="rightButton">
                        <img src="/modules/custom/qs_rankings_rest_api/assets/chevron-right.png" alt="Arrows">
                     </button>
                     <button class="btn-arrows btn-left-pick btn-arrows-js d-none" scrollnid="297235" direction="left" aria-label="leftButton">
                        <img src="/modules/custom/qs_rankings_rest_api/assets/chevron-left.png" alt="Arrows">
                     </button>
                  </div>
                  <ul class="nav nav-tabs m-0 scroll-this-side-297235-js" id="myTab" role="none">
                     <li class="nav-item ">
                                   <a class="nav-link active" id="research-discovery-297235" data-toggle="tab" href="#research-discovery-297235-tab">
                                   Research &amp; Discovery
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="learning-experience-297235" data-toggle="tab" href="#learning-experience-297235-tab">
                                   Learning Experience
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="employability-297235" data-toggle="tab" href="#employability-297235-tab">
                                   Employability
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="global-engagement-297235" data-toggle="tab" href="#global-engagement-297235-tab">
                                   Global Engagement
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="sustainability-297235" data-toggle="tab" href="#sustainability-297235-tab">
                                   Sustainability
                                   </a>
                                </li>
                     <li class="nav-item" role="none">
                        <a class="nav-link" id="more-info-tab-297235" data-toggle="tab" href="#more-info-tab-297235-tab">More Info
                           <span class="new-line">NEW</span>
                           <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/lock.svg" height="14" width="12" alt="lock" title="lock" class="lock-icon-checked-js d-none">
                        </a>
                     </li>
                  </ul>
                  <div class="tab-content py-2" id="myTabContent">

                     <div class="tab-pane fade show active" id="research-discovery-297235-tab" role="tabpanel" aria-labelledby="research-discovery-297235">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Academic Reputation</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="academic-reputation" role="progressbar" aria-label="progress" title="academic-reputation" aria-labelledby="academic-reputation" style="width: 99.2%" aria-valuenow="99.2" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">99.2</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Citations per Faculty</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="citations-per-faculty" role="progressbar" aria-label="progress" title="citations-per-faculty" aria-labelledby="citations-per-faculty" style="width: 99.1%" aria-valuenow="99.1" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">99.1</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="learning-experience-297235-tab" role="tabpanel" aria-labelledby="learning-experience-297235">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Faculty Student Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="faculty-student-ratio" role="progressbar" aria-label="progress" title="faculty-student-ratio" aria-labelledby="faculty-student-ratio" style="width: 95%" aria-valuenow="95" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">95</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="employability-297235-tab" role="tabpanel" aria-labelledby="employability-297235">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Employer Reputation</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="employer-reputation" role="progressbar" aria-label="progress" title="employer-reputation" aria-labelledby="employer-reputation" style="width: 97.7%" aria-valuenow="97.7" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">97.7</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Employment Outcomes</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="employment-outcomes" role="progressbar" aria-label="progress" title="employment-outcomes" aria-labelledby="employment-outcomes" style="width: 92.3%" aria-valuenow="92.3" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">92.3</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="global-engagement-297235-tab" role="tabpanel" aria-labelledby="global-engagement-297235">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Student Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-student-ratio" role="progressbar" aria-label="progress" title="international-student-ratio" aria-labelledby="international-student-ratio" style="width: 13.4%" aria-valuenow="13.4" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">13.4</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Research Network</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-research-network" role="progressbar" aria-label="progress" title="international-research-network" aria-labelledby="international-research-network" style="width: 79.2%" aria-valuenow="79.2" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">79.2</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Faculty Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-faculty-ratio" role="progressbar" aria-label="progress" title="international-faculty-ratio" aria-labelledby="international-faculty-ratio" style="width: 18.1%" aria-valuenow="18.1" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">18.1</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="sustainability-297235-tab" role="tabpanel" aria-labelledby="sustainability-297235">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Sustainability Score</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="sustainability-score" role="progressbar" aria-label="progress" title="sustainability-score" aria-labelledby="sustainability-score" style="width: 40.4%" aria-valuenow="40.4" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">40.4</div>
                           </div>
                        </div>
                         </div>
                      </div>

                     <div class="tab-pane fade" id="more-info-tab-297235-tab" role="tabpanel" aria-labelledby="more-info-tab-297235">
                        <div class="new-rankings-indicator-wrap py-2">

                           <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Fees</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                -
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Scholarship</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                No
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Student Mix</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                Domestic 89%   International 11%
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">English Tests</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                <a href="javascript:void(0)" class="_openfilter_results_js">Generate Result</a>
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Academic Tests</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                <a href="javascript:void(0)" class="_openfilter_results_js">Generate Result</a>
                              </div>
                           </div>
                        </div>


                        </div>

                        <div class="signup-for-user signup-for-user-js d-none">
                           <p>In order to see the data <a href="javascript:void(0)" class="signup-for-user-js-dlyr" data-toggle="modal" data-target="#emailModal">Sign up for free</a></p>
                        </div>


                     </div>

                  </div>
               </div>


            </div>

         </div>
      </div>
   </div><div class="row need-section-margin dynamic-block-ranking-3" position="20" customblock="true">
  <div class="_ifdfp_1 td-wrap col-lg-12 _ifdfp_1_divcss scroll-in-mobile">
                            <div id="js-dfp-tag-responsive_ad_3" class="text-center" data-google-query-id="CNiQj76m04oDFWdFwgUdoRUs0A">
            
          <div id="google_ads_iframe_8070/Topuni-Web/world-university-rankings_2__container__" style="border: 0pt none;"><iframe id="google_ads_iframe_8070/Topuni-Web/world-university-rankings_2" name="google_ads_iframe_8070/Topuni-Web/world-university-rankings_2" title="3rd party ad content" width="750" height="200" scrolling="no" marginwidth="0" marginheight="0" frameborder="0" aria-label="Advertisement" tabindex="0" allow="private-state-token-redemption;attribution-reporting" data-load-complete="true" data-google-container-id="8" style="border: 0px; vertical-align: bottom; visibility: visible;"></iframe></div></div>
                    </div>
</div>

   <div class="ind firstloaded main ranking-row-js-294536" nid="294536">
      <div class="">
         <div class="new-ranking-cards  normal-row">

            <div class="left-div-200">
               <div class="rank-square height-97px dark-blue padding-top-24">
                  <span class="rank-title mobile-upper">Rank</span>
                  <span class="rank-no">
                     21
                     <span class="dagger-icon-new d-none">
                        <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/dagger.svg" alt="Dagger Icon">
                     </span>
                  </span>
               </div>
               <div class="height-1px">
               </div>
               
               


               <div class="rank-square height-163px light-blue padding-top-32 text-align-mobile">
                  
                  

                 

                 


                  <span class="rank-title di-inline">Overall Score:</span>
                  <span class="rank-score di-inline">86.2</span>
               </div>
            </div>

            <div class="right-div-200">

               <div class="row">
                  <div class="col-lg-7 col-md-12 col-sm-12">
                     <div class="university-details-name">

                        <div class="univ-names-text">
                           <span class="logo-wrapper new-rank ">
                              <a href="/universities/university-chicago">
                                <img fetchpriority="low" loading="lazy" src="https://www.topuniversities.com/sites/default/files/university-of-chicago_120_medium.jpg" alt="University of Chicago" title="University of Chicago" height="78" width="78">
                              </a>
                           </span>

                           <a href="/universities/university-chicago" class="uni-link">University of Chicago</a>

                           <div class="location">
                              <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/location.svg" height="12" width="12" alt="location" title="location"> Chicago,  United States
                           </div>

                           <div class="stars d-none">
                             <span class="ranking-star">
                               <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/stars.svg" height="20" width="20" alt="QS stars" title="QS stars">
                             </span>
                             <span class="rating_number"></span>
                             <span class="qs-stars-font">QS Stars</span>
                           </div> 



                        </div>
                     </div>
                  </div>

               <div class="col-lg-5 col-md-12 col-sm-12">
                  <div class="shortlist-compare-div">
                     <div class="shortlist_div_new">
                        <a class="wishlist _directorypage shortlistnonloggedglobaljs   _shortlist_nid_294536  shortlistnonloggedglobaljs_dlyr" progoruniv="univ" nid="294536" onclick="Drupal.behaviors.tu_d8._adduniversityShortlist(this, 294536, 'university')">
                           <i class="fa fa-heart" aria-hidden="true"></i>
                           <i class="fal fa-heart" aria-hidden="true"></i>
                           <span class="_addShortText">Shortlist</span>
                        </a>
                     </div>

                     <div class="compare_div_new">
                        <a href="javascript:void(0)" class="compare _globCompUniv_js _globcompare_universityCookie_js_294536 comparenonloggedglobaljs_dlyr" nid="294536" progoruniv="univ" onclick="Drupal.behaviors.tu_d8._adduniversityCompare(this, 294536)">
                           <span class="two-square-icon">
                              <i class="fal fa-circle" aria-hidden="true"></i>
                           </span>
                           <span class="change-text">Compare</span>
                        </a>
                     </div>
                  </div>
               </div>

               </div>



               <div class="new-rankings-tab-content-wrapper">
                  <div class="arrows-left-right-tab arrows-left-right-tab-js">
                     <button class="btn-arrows btn-right-pick btn-arrows-js" scrollnid="294536" direction="right" aria-label="rightButton">
                        <img src="/modules/custom/qs_rankings_rest_api/assets/chevron-right.png" alt="Arrows">
                     </button>
                     <button class="btn-arrows btn-left-pick btn-arrows-js d-none" scrollnid="294536" direction="left" aria-label="leftButton">
                        <img src="/modules/custom/qs_rankings_rest_api/assets/chevron-left.png" alt="Arrows">
                     </button>
                  </div>
                  <ul class="nav nav-tabs m-0 scroll-this-side-294536-js" id="myTab" role="none">
                     <li class="nav-item ">
                                   <a class="nav-link active" id="research-discovery-294536" data-toggle="tab" href="#research-discovery-294536-tab">
                                   Research &amp; Discovery
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="learning-experience-294536" data-toggle="tab" href="#learning-experience-294536-tab">
                                   Learning Experience
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="employability-294536" data-toggle="tab" href="#employability-294536-tab">
                                   Employability
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="global-engagement-294536" data-toggle="tab" href="#global-engagement-294536-tab">
                                   Global Engagement
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="sustainability-294536" data-toggle="tab" href="#sustainability-294536-tab">
                                   Sustainability
                                   </a>
                                </li>
                     <li class="nav-item" role="none">
                        <a class="nav-link" id="more-info-tab-294536" data-toggle="tab" href="#more-info-tab-294536-tab">More Info
                           <span class="new-line">NEW</span>
                           <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/lock.svg" height="14" width="12" alt="lock" title="lock" class="lock-icon-checked-js d-none">
                        </a>
                     </li>
                  </ul>
                  <div class="tab-content py-2" id="myTabContent">

                     <div class="tab-pane fade show active" id="research-discovery-294536-tab" role="tabpanel" aria-labelledby="research-discovery-294536">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Academic Reputation</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="academic-reputation" role="progressbar" aria-label="progress" title="academic-reputation" aria-labelledby="academic-reputation" style="width: 99.1%" aria-valuenow="99.1" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">99.1</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Citations per Faculty</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="citations-per-faculty" role="progressbar" aria-label="progress" title="citations-per-faculty" aria-labelledby="citations-per-faculty" style="width: 60.8%" aria-valuenow="60.8" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">60.8</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="learning-experience-294536-tab" role="tabpanel" aria-labelledby="learning-experience-294536">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Faculty Student Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="faculty-student-ratio" role="progressbar" aria-label="progress" title="faculty-student-ratio" aria-labelledby="faculty-student-ratio" style="width: 94.2%" aria-valuenow="94.2" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">94.2</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="employability-294536-tab" role="tabpanel" aria-labelledby="employability-294536">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Employer Reputation</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="employer-reputation" role="progressbar" aria-label="progress" title="employer-reputation" aria-labelledby="employer-reputation" style="width: 96.4%" aria-valuenow="96.4" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">96.4</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Employment Outcomes</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="employment-outcomes" role="progressbar" aria-label="progress" title="employment-outcomes" aria-labelledby="employment-outcomes" style="width: 99.1%" aria-valuenow="99.1" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">99.1</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="global-engagement-294536-tab" role="tabpanel" aria-labelledby="global-engagement-294536">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Student Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-student-ratio" role="progressbar" aria-label="progress" title="international-student-ratio" aria-labelledby="international-student-ratio" style="width: 87%" aria-valuenow="87" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">87</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Research Network</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-research-network" role="progressbar" aria-label="progress" title="international-research-network" aria-labelledby="international-research-network" style="width: 85.1%" aria-valuenow="85.1" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">85.1</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Faculty Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-faculty-ratio" role="progressbar" aria-label="progress" title="international-faculty-ratio" aria-labelledby="international-faculty-ratio" style="width: 79%" aria-valuenow="79" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">79</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="sustainability-294536-tab" role="tabpanel" aria-labelledby="sustainability-294536">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Sustainability Score</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="sustainability-score" role="progressbar" aria-label="progress" title="sustainability-score" aria-labelledby="sustainability-score" style="width: 46.9%" aria-valuenow="46.9" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">46.9</div>
                           </div>
                        </div>
                         </div>
                      </div>

                     <div class="tab-pane fade" id="more-info-tab-294536-tab" role="tabpanel" aria-labelledby="more-info-tab-294536">
                        <div class="new-rankings-indicator-wrap py-2">

                           <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Fees</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                -
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Scholarship</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                Yes
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Student Mix</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                Domestic 67%   International 33%
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">English Tests</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                <a href="javascript:void(0)" class="_openfilter_results_js">Generate Result</a>
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Academic Tests</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                <a href="javascript:void(0)" class="_openfilter_results_js">Generate Result</a>
                              </div>
                           </div>
                        </div>


                        </div>

                        <div class="signup-for-user signup-for-user-js d-none">
                           <p>In order to see the data <a href="javascript:void(0)" class="signup-for-user-js-dlyr" data-toggle="modal" data-target="#emailModal">Sign up for free</a></p>
                        </div>


                     </div>

                  </div>
               </div>


            </div>

         </div>
      </div>
   </div>

   <div class="ind firstloaded main ranking-row-js-297490" nid="297490">
      <div class="">
         <div class="new-ranking-cards  normal-row">

            <div class="left-div-200">
               <div class="rank-square height-97px dark-blue padding-top-24">
                  <span class="rank-title mobile-upper">Rank</span>
                  <span class="rank-no">
                     22
                     <span class="dagger-icon-new d-none">
                        <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/dagger.svg" alt="Dagger Icon">
                     </span>
                  </span>
               </div>
               <div class="height-1px">
               </div>
               
               


               <div class="rank-square height-163px light-blue padding-top-32 text-align-mobile">
                  
                  

                 

                 


                  <span class="rank-title di-inline">Overall Score:</span>
                  <span class="rank-score di-inline">85.5</span>
               </div>
            </div>

            <div class="right-div-200">

               <div class="row">
                  <div class="col-lg-7 col-md-12 col-sm-12">
                     <div class="university-details-name">

                        <div class="univ-names-text">
                           <span class="logo-wrapper new-rank ">
                              <a href="/universities/princeton-university">
                                <img fetchpriority="low" loading="lazy" src="https://www.topuniversities.com/sites/default/files/princeton-university_508_medium.jpg" alt="Princeton University" title="Princeton University" height="78" width="78">
                              </a>
                           </span>

                           <a href="/universities/princeton-university" class="uni-link">Princeton University</a>

                           <div class="location">
                              <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/location.svg" height="12" width="12" alt="location" title="location"> Princeton,  United States
                           </div>

                           <div class="stars d-none">
                             <span class="ranking-star">
                               <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/stars.svg" height="20" width="20" alt="QS stars" title="QS stars">
                             </span>
                             <span class="rating_number"></span>
                             <span class="qs-stars-font">QS Stars</span>
                           </div> 



                        </div>
                     </div>
                  </div>

               <div class="col-lg-5 col-md-12 col-sm-12">
                  <div class="shortlist-compare-div">
                     <div class="shortlist_div_new">
                        <a class="wishlist _directorypage shortlistnonloggedglobaljs   _shortlist_nid_297490  shortlistnonloggedglobaljs_dlyr" progoruniv="univ" nid="297490" onclick="Drupal.behaviors.tu_d8._adduniversityShortlist(this, 297490, 'university')">
                           <i class="fa fa-heart" aria-hidden="true"></i>
                           <i class="fal fa-heart" aria-hidden="true"></i>
                           <span class="_addShortText">Shortlist</span>
                        </a>
                     </div>

                     <div class="compare_div_new">
                        <a href="javascript:void(0)" class="compare _globCompUniv_js _globcompare_universityCookie_js_297490 comparenonloggedglobaljs_dlyr" nid="297490" progoruniv="univ" onclick="Drupal.behaviors.tu_d8._adduniversityCompare(this, 297490)">
                           <span class="two-square-icon">
                              <i class="fal fa-circle" aria-hidden="true"></i>
                           </span>
                           <span class="change-text">Compare</span>
                        </a>
                     </div>
                  </div>
               </div>

               </div>



               <div class="new-rankings-tab-content-wrapper">
                  <div class="arrows-left-right-tab arrows-left-right-tab-js">
                     <button class="btn-arrows btn-right-pick btn-arrows-js" scrollnid="297490" direction="right" aria-label="rightButton">
                        <img src="/modules/custom/qs_rankings_rest_api/assets/chevron-right.png" alt="Arrows">
                     </button>
                     <button class="btn-arrows btn-left-pick btn-arrows-js d-none" scrollnid="297490" direction="left" aria-label="leftButton">
                        <img src="/modules/custom/qs_rankings_rest_api/assets/chevron-left.png" alt="Arrows">
                     </button>
                  </div>
                  <ul class="nav nav-tabs m-0 scroll-this-side-297490-js" id="myTab" role="none">
                     <li class="nav-item ">
                                   <a class="nav-link active" id="research-discovery-297490" data-toggle="tab" href="#research-discovery-297490-tab">
                                   Research &amp; Discovery
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="learning-experience-297490" data-toggle="tab" href="#learning-experience-297490-tab">
                                   Learning Experience
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="employability-297490" data-toggle="tab" href="#employability-297490-tab">
                                   Employability
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="global-engagement-297490" data-toggle="tab" href="#global-engagement-297490-tab">
                                   Global Engagement
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="sustainability-297490" data-toggle="tab" href="#sustainability-297490-tab">
                                   Sustainability
                                   </a>
                                </li>
                     <li class="nav-item" role="none">
                        <a class="nav-link" id="more-info-tab-297490" data-toggle="tab" href="#more-info-tab-297490-tab">More Info
                           <span class="new-line">NEW</span>
                           <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/lock.svg" height="14" width="12" alt="lock" title="lock" class="lock-icon-checked-js d-none">
                        </a>
                     </li>
                  </ul>
                  <div class="tab-content py-2" id="myTabContent">

                     <div class="tab-pane fade show active" id="research-discovery-297490-tab" role="tabpanel" aria-labelledby="research-discovery-297490">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Academic Reputation</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="academic-reputation" role="progressbar" aria-label="progress" title="academic-reputation" aria-labelledby="academic-reputation" style="width: 99.8%" aria-valuenow="99.8" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">99.8</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Citations per Faculty</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="citations-per-faculty" role="progressbar" aria-label="progress" title="citations-per-faculty" aria-labelledby="citations-per-faculty" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">100</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="learning-experience-297490-tab" role="tabpanel" aria-labelledby="learning-experience-297490">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Faculty Student Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="faculty-student-ratio" role="progressbar" aria-label="progress" title="faculty-student-ratio" aria-labelledby="faculty-student-ratio" style="width: 57%" aria-valuenow="57" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">57</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="employability-297490-tab" role="tabpanel" aria-labelledby="employability-297490">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Employer Reputation</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="employer-reputation" role="progressbar" aria-label="progress" title="employer-reputation" aria-labelledby="employer-reputation" style="width: 98.3%" aria-valuenow="98.3" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">98.3</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Employment Outcomes</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="employment-outcomes" role="progressbar" aria-label="progress" title="employment-outcomes" aria-labelledby="employment-outcomes" style="width: 95.7%" aria-valuenow="95.7" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">95.7</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="global-engagement-297490-tab" role="tabpanel" aria-labelledby="global-engagement-297490">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Student Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-student-ratio" role="progressbar" aria-label="progress" title="international-student-ratio" aria-labelledby="international-student-ratio" style="width: 56.6%" aria-valuenow="56.6" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">56.6</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Research Network</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-research-network" role="progressbar" aria-label="progress" title="international-research-network" aria-labelledby="international-research-network" style="width: 78.3%" aria-valuenow="78.3" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">78.3</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Faculty Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-faculty-ratio" role="progressbar" aria-label="progress" title="international-faculty-ratio" aria-labelledby="international-faculty-ratio" style="width: 9.6%" aria-valuenow="9.6" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">9.6</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="sustainability-297490-tab" role="tabpanel" aria-labelledby="sustainability-297490">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Sustainability Score</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="sustainability-score" role="progressbar" aria-label="progress" title="sustainability-score" aria-labelledby="sustainability-score" style="width: 51.5%" aria-valuenow="51.5" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">51.5</div>
                           </div>
                        </div>
                         </div>
                      </div>

                     <div class="tab-pane fade" id="more-info-tab-297490-tab" role="tabpanel" aria-labelledby="more-info-tab-297490">
                        <div class="new-rankings-indicator-wrap py-2">

                           <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Fees</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                -
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Scholarship</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                No
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Student Mix</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                Domestic 77%   International 23%
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">English Tests</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                <a href="javascript:void(0)" class="_openfilter_results_js">Generate Result</a>
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Academic Tests</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                <a href="javascript:void(0)" class="_openfilter_results_js">Generate Result</a>
                              </div>
                           </div>
                        </div>


                        </div>

                        <div class="signup-for-user signup-for-user-js d-none">
                           <p>In order to see the data <a href="javascript:void(0)" class="signup-for-user-js-dlyr" data-toggle="modal" data-target="#emailModal">Sign up for free</a></p>
                        </div>


                     </div>

                  </div>
               </div>


            </div>

         </div>
      </div>
   </div>

   <div class="ind firstloaded main ranking-row-js-297177" nid="297177">
      <div class="">
         <div class="new-ranking-cards  normal-row">

            <div class="left-div-200">
               <div class="rank-square height-97px dark-blue padding-top-24">
                  <span class="rank-title mobile-upper">Rank</span>
                  <span class="rank-no">
                     23
                     <span class="dagger-icon-new d-none">
                        <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/dagger.svg" alt="Dagger Icon">
                     </span>
                  </span>
               </div>
               <div class="height-1px">
               </div>
               
               


               <div class="rank-square height-163px light-blue padding-top-32 text-align-mobile">
                  
                  

                 

                 


                  <span class="rank-title di-inline">Overall Score:</span>
                  <span class="rank-score di-inline">85.2</span>
               </div>
            </div>

            <div class="right-div-200">

               <div class="row">
                  <div class="col-lg-7 col-md-12 col-sm-12">
                     <div class="university-details-name">

                        <div class="univ-names-text">
                           <span class="logo-wrapper new-rank ">
                              <a href="/universities/yale-university">
                                <img fetchpriority="low" loading="lazy" src="https://www.topuniversities.com/sites/default/files/yale-university_684_medium.jpg" alt="Yale University" title="Yale University" height="78" width="78">
                              </a>
                           </span>

                           <a href="/universities/yale-university" class="uni-link">Yale University</a>

                           <div class="location">
                              <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/location.svg" height="12" width="12" alt="location" title="location"> New Haven,  United States
                           </div>

                           <div class="stars d-none">
                             <span class="ranking-star">
                               <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/stars.svg" height="20" width="20" alt="QS stars" title="QS stars">
                             </span>
                             <span class="rating_number"></span>
                             <span class="qs-stars-font">QS Stars</span>
                           </div> 



                        </div>
                     </div>
                  </div>

               <div class="col-lg-5 col-md-12 col-sm-12">
                  <div class="shortlist-compare-div">
                     <div class="shortlist_div_new">
                        <a class="wishlist _directorypage shortlistnonloggedglobaljs   _shortlist_nid_297177  shortlistnonloggedglobaljs_dlyr" progoruniv="univ" nid="297177" onclick="Drupal.behaviors.tu_d8._adduniversityShortlist(this, 297177, 'university')">
                           <i class="fa fa-heart" aria-hidden="true"></i>
                           <i class="fal fa-heart" aria-hidden="true"></i>
                           <span class="_addShortText">Shortlist</span>
                        </a>
                     </div>

                     <div class="compare_div_new">
                        <a href="javascript:void(0)" class="compare _globCompUniv_js _globcompare_universityCookie_js_297177 comparenonloggedglobaljs_dlyr" nid="297177" progoruniv="univ" onclick="Drupal.behaviors.tu_d8._adduniversityCompare(this, 297177)">
                           <span class="two-square-icon">
                              <i class="fal fa-circle" aria-hidden="true"></i>
                           </span>
                           <span class="change-text">Compare</span>
                        </a>
                     </div>
                  </div>
               </div>

               </div>



               <div class="new-rankings-tab-content-wrapper">
                  <div class="arrows-left-right-tab arrows-left-right-tab-js">
                     <button class="btn-arrows btn-right-pick btn-arrows-js" scrollnid="297177" direction="right" aria-label="rightButton">
                        <img src="/modules/custom/qs_rankings_rest_api/assets/chevron-right.png" alt="Arrows">
                     </button>
                     <button class="btn-arrows btn-left-pick btn-arrows-js d-none" scrollnid="297177" direction="left" aria-label="leftButton">
                        <img src="/modules/custom/qs_rankings_rest_api/assets/chevron-left.png" alt="Arrows">
                     </button>
                  </div>
                  <ul class="nav nav-tabs m-0 scroll-this-side-297177-js" id="myTab" role="none">
                     <li class="nav-item ">
                                   <a class="nav-link active" id="research-discovery-297177" data-toggle="tab" href="#research-discovery-297177-tab">
                                   Research &amp; Discovery
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="learning-experience-297177" data-toggle="tab" href="#learning-experience-297177-tab">
                                   Learning Experience
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="employability-297177" data-toggle="tab" href="#employability-297177-tab">
                                   Employability
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="global-engagement-297177" data-toggle="tab" href="#global-engagement-297177-tab">
                                   Global Engagement
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="sustainability-297177" data-toggle="tab" href="#sustainability-297177-tab">
                                   Sustainability
                                   </a>
                                </li>
                     <li class="nav-item" role="none">
                        <a class="nav-link" id="more-info-tab-297177" data-toggle="tab" href="#more-info-tab-297177-tab">More Info
                           <span class="new-line">NEW</span>
                           <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/lock.svg" height="14" width="12" alt="lock" title="lock" class="lock-icon-checked-js d-none">
                        </a>
                     </li>
                  </ul>
                  <div class="tab-content py-2" id="myTabContent">

                     <div class="tab-pane fade show active" id="research-discovery-297177-tab" role="tabpanel" aria-labelledby="research-discovery-297177">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Academic Reputation</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="academic-reputation" role="progressbar" aria-label="progress" title="academic-reputation" aria-labelledby="academic-reputation" style="width: 99.9%" aria-valuenow="99.9" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">99.9</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Citations per Faculty</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="citations-per-faculty" role="progressbar" aria-label="progress" title="citations-per-faculty" aria-labelledby="citations-per-faculty" style="width: 38.6%" aria-valuenow="38.6" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">38.6</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="learning-experience-297177-tab" role="tabpanel" aria-labelledby="learning-experience-297177">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Faculty Student Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="faculty-student-ratio" role="progressbar" aria-label="progress" title="faculty-student-ratio" aria-labelledby="faculty-student-ratio" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">100</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="employability-297177-tab" role="tabpanel" aria-labelledby="employability-297177">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Employer Reputation</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="employer-reputation" role="progressbar" aria-label="progress" title="employer-reputation" aria-labelledby="employer-reputation" style="width: 99.9%" aria-valuenow="99.9" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">99.9</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Employment Outcomes</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="employment-outcomes" role="progressbar" aria-label="progress" title="employment-outcomes" aria-labelledby="employment-outcomes" style="width: 98.5%" aria-valuenow="98.5" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">98.5</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="global-engagement-297177-tab" role="tabpanel" aria-labelledby="global-engagement-297177">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Student Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-student-ratio" role="progressbar" aria-label="progress" title="international-student-ratio" aria-labelledby="international-student-ratio" style="width: 63.3%" aria-valuenow="63.3" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">63.3</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Research Network</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-research-network" role="progressbar" aria-label="progress" title="international-research-network" aria-labelledby="international-research-network" style="width: 93.9%" aria-valuenow="93.9" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">93.9</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Faculty Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-faculty-ratio" role="progressbar" aria-label="progress" title="international-faculty-ratio" aria-labelledby="international-faculty-ratio" style="width: 91.5%" aria-valuenow="91.5" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">91.5</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="sustainability-297177-tab" role="tabpanel" aria-labelledby="sustainability-297177">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Sustainability Score</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="sustainability-score" role="progressbar" aria-label="progress" title="sustainability-score" aria-labelledby="sustainability-score" style="width: 92.2%" aria-valuenow="92.2" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">92.2</div>
                           </div>
                        </div>
                         </div>
                      </div>

                     <div class="tab-pane fade" id="more-info-tab-297177-tab" role="tabpanel" aria-labelledby="more-info-tab-297177">
                        <div class="new-rankings-indicator-wrap py-2">

                           <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Fees</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                -
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Scholarship</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                Yes
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Student Mix</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                Domestic 76%   International 24%
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">English Tests</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                <a href="javascript:void(0)" class="_openfilter_results_js">Generate Result</a>
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Academic Tests</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                <a href="javascript:void(0)" class="_openfilter_results_js">Generate Result</a>
                              </div>
                           </div>
                        </div>


                        </div>

                        <div class="signup-for-user signup-for-user-js d-none">
                           <p>In order to see the data <a href="javascript:void(0)" class="signup-for-user-js-dlyr" data-toggle="modal" data-target="#emailModal">Sign up for free</a></p>
                        </div>


                     </div>

                  </div>
               </div>


            </div>

         </div>
      </div>
   </div>

   <div class="ind firstloaded main ranking-row-js-397503" nid="397503">
      <div class="">
         <div class="new-ranking-cards  normal-row">

            <div class="left-div-200">
               <div class="rank-square height-97px dark-blue padding-top-24">
                  <span class="rank-title mobile-upper">Rank</span>
                  <span class="rank-no">
                     24
                     <span class="dagger-icon-new d-none">
                        <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/dagger.svg" alt="Dagger Icon">
                     </span>
                  </span>
               </div>
               <div class="height-1px">
               </div>
               
               


               <div class="rank-square height-163px light-blue padding-top-32 text-align-mobile">
                  
                  

                 

                 


                  <span class="rank-title di-inline">Overall Score:</span>
                  <span class="rank-score di-inline">84.7</span>
               </div>
            </div>

            <div class="right-div-200">

               <div class="row">
                  <div class="col-lg-7 col-md-12 col-sm-12">
                     <div class="university-details-name">

                        <div class="univ-names-text">
                           <span class="logo-wrapper new-rank ">
                              <a href="/universities/universite-psl">
                                <img fetchpriority="low" loading="lazy" src="https://www.topuniversities.com/sites/default/files/universit-psl_592560e69988f300e2321dfe_medium.jpg" alt="Université PSL" title="Université PSL" height="78" width="78">
                              </a>
                           </span>

                           <a href="/universities/universite-psl" class="uni-link">Université PSL</a>

                           <div class="location">
                              <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/location.svg" height="12" width="12" alt="location" title="location"> Paris,  France
                           </div>

                           <div class="stars d-none">
                             <span class="ranking-star">
                               <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/stars.svg" height="20" width="20" alt="QS stars" title="QS stars">
                             </span>
                             <span class="rating_number"></span>
                             <span class="qs-stars-font">QS Stars</span>
                           </div> 



                        </div>
                     </div>
                  </div>

               <div class="col-lg-5 col-md-12 col-sm-12">
                  <div class="shortlist-compare-div">
                     <div class="shortlist_div_new">
                        <a class="wishlist _directorypage shortlistnonloggedglobaljs   _shortlist_nid_397503  shortlistnonloggedglobaljs_dlyr" progoruniv="univ" nid="397503" onclick="Drupal.behaviors.tu_d8._adduniversityShortlist(this, 397503, 'university')">
                           <i class="fa fa-heart" aria-hidden="true"></i>
                           <i class="fal fa-heart" aria-hidden="true"></i>
                           <span class="_addShortText">Shortlist</span>
                        </a>
                     </div>

                     <div class="compare_div_new">
                        <a href="javascript:void(0)" class="compare _globCompUniv_js _globcompare_universityCookie_js_397503 comparenonloggedglobaljs_dlyr" nid="397503" progoruniv="univ" onclick="Drupal.behaviors.tu_d8._adduniversityCompare(this, 397503)">
                           <span class="two-square-icon">
                              <i class="fal fa-circle" aria-hidden="true"></i>
                           </span>
                           <span class="change-text">Compare</span>
                        </a>
                     </div>
                  </div>
               </div>

               </div>



               <div class="new-rankings-tab-content-wrapper">
                  <div class="arrows-left-right-tab arrows-left-right-tab-js">
                     <button class="btn-arrows btn-right-pick btn-arrows-js" scrollnid="397503" direction="right" aria-label="rightButton">
                        <img src="/modules/custom/qs_rankings_rest_api/assets/chevron-right.png" alt="Arrows">
                     </button>
                     <button class="btn-arrows btn-left-pick btn-arrows-js d-none" scrollnid="397503" direction="left" aria-label="leftButton">
                        <img src="/modules/custom/qs_rankings_rest_api/assets/chevron-left.png" alt="Arrows">
                     </button>
                  </div>
                  <ul class="nav nav-tabs m-0 scroll-this-side-397503-js" id="myTab" role="none">
                     <li class="nav-item ">
                                   <a class="nav-link active" id="research-discovery-397503" data-toggle="tab" href="#research-discovery-397503-tab">
                                   Research &amp; Discovery
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="learning-experience-397503" data-toggle="tab" href="#learning-experience-397503-tab">
                                   Learning Experience
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="employability-397503" data-toggle="tab" href="#employability-397503-tab">
                                   Employability
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="global-engagement-397503" data-toggle="tab" href="#global-engagement-397503-tab">
                                   Global Engagement
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="sustainability-397503" data-toggle="tab" href="#sustainability-397503-tab">
                                   Sustainability
                                   </a>
                                </li>
                     <li class="nav-item" role="none">
                        <a class="nav-link" id="more-info-tab-397503" data-toggle="tab" href="#more-info-tab-397503-tab">More Info
                           <span class="new-line">NEW</span>
                           <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/lock.svg" height="14" width="12" alt="lock" title="lock" class="lock-icon-checked-js d-none">
                        </a>
                     </li>
                  </ul>
                  <div class="tab-content py-2" id="myTabContent">

                     <div class="tab-pane fade show active" id="research-discovery-397503-tab" role="tabpanel" aria-labelledby="research-discovery-397503">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Academic Reputation</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="academic-reputation" role="progressbar" aria-label="progress" title="academic-reputation" aria-labelledby="academic-reputation" style="width: 74.4%" aria-valuenow="74.4" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">74.4</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Citations per Faculty</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="citations-per-faculty" role="progressbar" aria-label="progress" title="citations-per-faculty" aria-labelledby="citations-per-faculty" style="width: 87.6%" aria-valuenow="87.6" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">87.6</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="learning-experience-397503-tab" role="tabpanel" aria-labelledby="learning-experience-397503">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Faculty Student Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="faculty-student-ratio" role="progressbar" aria-label="progress" title="faculty-student-ratio" aria-labelledby="faculty-student-ratio" style="width: 98.1%" aria-valuenow="98.1" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">98.1</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="employability-397503-tab" role="tabpanel" aria-labelledby="employability-397503">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Employer Reputation</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="employer-reputation" role="progressbar" aria-label="progress" title="employer-reputation" aria-labelledby="employer-reputation" style="width: 97.6%" aria-valuenow="97.6" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">97.6</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Employment Outcomes</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="employment-outcomes" role="progressbar" aria-label="progress" title="employment-outcomes" aria-labelledby="employment-outcomes" style="width: 97.1%" aria-valuenow="97.1" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">97.1</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="global-engagement-397503-tab" role="tabpanel" aria-labelledby="global-engagement-397503">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Student Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-student-ratio" role="progressbar" aria-label="progress" title="international-student-ratio" aria-labelledby="international-student-ratio" style="width: 65%" aria-valuenow="65" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">65</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Research Network</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-research-network" role="progressbar" aria-label="progress" title="international-research-network" aria-labelledby="international-research-network" style="width: 99.8%" aria-valuenow="99.8" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">99.8</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Faculty Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-faculty-ratio" role="progressbar" aria-label="progress" title="international-faculty-ratio" aria-labelledby="international-faculty-ratio" style="width: 62.3%" aria-valuenow="62.3" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">62.3</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="sustainability-397503-tab" role="tabpanel" aria-labelledby="sustainability-397503">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Sustainability Score</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="sustainability-score" role="progressbar" aria-label="progress" title="sustainability-score" aria-labelledby="sustainability-score" style="width: 73.4%" aria-valuenow="73.4" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">73.4</div>
                           </div>
                        </div>
                         </div>
                      </div>

                     <div class="tab-pane fade" id="more-info-tab-397503-tab" role="tabpanel" aria-labelledby="more-info-tab-397503">
                        <div class="new-rankings-indicator-wrap py-2">

                           <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Fees</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                250(EUR)
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Scholarship</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                No
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Student Mix</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                Domestic 75%   International 25%
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">English Tests</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                <a href="javascript:void(0)" class="_openfilter_results_js">Generate Result</a>
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Academic Tests</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                <a href="javascript:void(0)" class="_openfilter_results_js">Generate Result</a>
                              </div>
                           </div>
                        </div>


                        </div>

                        <div class="signup-for-user signup-for-user-js d-none">
                           <p>In order to see the data <a href="javascript:void(0)" class="signup-for-user-js-dlyr" data-toggle="modal" data-target="#emailModal">Sign up for free</a></p>
                        </div>


                     </div>

                  </div>
               </div>


            </div>

         </div>
      </div>
   </div>

   <div class="ind firstloaded main ranking-row-js-297242" nid="297242">
      <div class="">
         <div class="new-ranking-cards  normal-row">

            <div class="left-div-200">
               <div class="rank-square height-97px dark-blue padding-top-24">
                  <span class="rank-title mobile-upper">Rank</span>
                  <span class="rank-no">
                     25
                     <span class="dagger-icon-new d-none">
                        <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/dagger.svg" alt="Dagger Icon">
                     </span>
                  </span>
               </div>
               <div class="height-1px">
               </div>
               
               


               <div class="rank-square height-163px light-blue padding-top-32 text-align-mobile">
                  
                  

                 

                 


                  <span class="rank-title di-inline">Overall Score:</span>
                  <span class="rank-score di-inline">84.1</span>
               </div>
            </div>

            <div class="right-div-200">

               <div class="row">
                  <div class="col-lg-7 col-md-12 col-sm-12">
                     <div class="university-details-name">

                        <div class="univ-names-text">
                           <span class="logo-wrapper new-rank ">
                              <a href="/universities/university-toronto">
                                <img fetchpriority="low" loading="lazy" src="https://www.topuniversities.com/sites/default/files/university-of-toronto_619_medium.jpg" alt="University of Toronto" title="University of Toronto" height="78" width="78">
                              </a>
                           </span>

                           <a href="/universities/university-toronto" class="uni-link">University of Toronto</a>

                           <div class="location">
                              <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/location.svg" height="12" width="12" alt="location" title="location"> Toronto,  Canada
                           </div>

                           <div class="stars d-none">
                             <span class="ranking-star">
                               <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/stars.svg" height="20" width="20" alt="QS stars" title="QS stars">
                             </span>
                             <span class="rating_number"></span>
                             <span class="qs-stars-font">QS Stars</span>
                           </div> 



                        </div>
                     </div>
                  </div>

               <div class="col-lg-5 col-md-12 col-sm-12">
                  <div class="shortlist-compare-div">
                     <div class="shortlist_div_new">
                        <a class="wishlist _directorypage shortlistnonloggedglobaljs   _shortlist_nid_297242  shortlistnonloggedglobaljs_dlyr" progoruniv="univ" nid="297242" onclick="Drupal.behaviors.tu_d8._adduniversityShortlist(this, 297242, 'university')">
                           <i class="fa fa-heart" aria-hidden="true"></i>
                           <i class="fal fa-heart" aria-hidden="true"></i>
                           <span class="_addShortText">Shortlist</span>
                        </a>
                     </div>

                     <div class="compare_div_new">
                        <a href="javascript:void(0)" class="compare _globCompUniv_js _globcompare_universityCookie_js_297242 comparenonloggedglobaljs_dlyr" nid="297242" progoruniv="univ" onclick="Drupal.behaviors.tu_d8._adduniversityCompare(this, 297242)">
                           <span class="two-square-icon">
                              <i class="fal fa-circle" aria-hidden="true"></i>
                           </span>
                           <span class="change-text">Compare</span>
                        </a>
                     </div>
                  </div>
               </div>

               </div>



               <div class="new-rankings-tab-content-wrapper">
                  <div class="arrows-left-right-tab arrows-left-right-tab-js">
                     <button class="btn-arrows btn-right-pick btn-arrows-js" scrollnid="297242" direction="right" aria-label="rightButton">
                        <img src="/modules/custom/qs_rankings_rest_api/assets/chevron-right.png" alt="Arrows">
                     </button>
                     <button class="btn-arrows btn-left-pick btn-arrows-js d-none" scrollnid="297242" direction="left" aria-label="leftButton">
                        <img src="/modules/custom/qs_rankings_rest_api/assets/chevron-left.png" alt="Arrows">
                     </button>
                  </div>
                  <ul class="nav nav-tabs m-0 scroll-this-side-297242-js" id="myTab" role="none">
                     <li class="nav-item ">
                                   <a class="nav-link active" id="research-discovery-297242" data-toggle="tab" href="#research-discovery-297242-tab">
                                   Research &amp; Discovery
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="learning-experience-297242" data-toggle="tab" href="#learning-experience-297242-tab">
                                   Learning Experience
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="employability-297242" data-toggle="tab" href="#employability-297242-tab">
                                   Employability
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="global-engagement-297242" data-toggle="tab" href="#global-engagement-297242-tab">
                                   Global Engagement
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="sustainability-297242" data-toggle="tab" href="#sustainability-297242-tab">
                                   Sustainability
                                   </a>
                                </li>
                     <li class="nav-item" role="none">
                        <a class="nav-link" id="more-info-tab-297242" data-toggle="tab" href="#more-info-tab-297242-tab">More Info
                           <span class="new-line">NEW</span>
                           <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/lock.svg" height="14" width="12" alt="lock" title="lock" class="lock-icon-checked-js d-none">
                        </a>
                     </li>
                  </ul>
                  <div class="tab-content py-2" id="myTabContent">

                     <div class="tab-pane fade show active" id="research-discovery-297242-tab" role="tabpanel" aria-labelledby="research-discovery-297242">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Academic Reputation</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="academic-reputation" role="progressbar" aria-label="progress" title="academic-reputation" aria-labelledby="academic-reputation" style="width: 99.7%" aria-valuenow="99.7" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">99.7</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Citations per Faculty</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="citations-per-faculty" role="progressbar" aria-label="progress" title="citations-per-faculty" aria-labelledby="citations-per-faculty" style="width: 50.8%" aria-valuenow="50.8" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">50.8</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="learning-experience-297242-tab" role="tabpanel" aria-labelledby="learning-experience-297242">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Faculty Student Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="faculty-student-ratio" role="progressbar" aria-label="progress" title="faculty-student-ratio" aria-labelledby="faculty-student-ratio" style="width: 44.9%" aria-valuenow="44.9" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">44.9</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="employability-297242-tab" role="tabpanel" aria-labelledby="employability-297242">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Employer Reputation</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="employer-reputation" role="progressbar" aria-label="progress" title="employer-reputation" aria-labelledby="employer-reputation" style="width: 96.9%" aria-valuenow="96.9" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">96.9</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Employment Outcomes</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="employment-outcomes" role="progressbar" aria-label="progress" title="employment-outcomes" aria-labelledby="employment-outcomes" style="width: 98.7%" aria-valuenow="98.7" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">98.7</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="global-engagement-297242-tab" role="tabpanel" aria-labelledby="global-engagement-297242">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Student Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-student-ratio" role="progressbar" aria-label="progress" title="international-student-ratio" aria-labelledby="international-student-ratio" style="width: 96.1%" aria-valuenow="96.1" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">96.1</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Research Network</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-research-network" role="progressbar" aria-label="progress" title="international-research-network" aria-labelledby="international-research-network" style="width: 97.7%" aria-valuenow="97.7" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">97.7</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Faculty Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-faculty-ratio" role="progressbar" aria-label="progress" title="international-faculty-ratio" aria-labelledby="international-faculty-ratio" style="width: 96.9%" aria-valuenow="96.9" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">96.9</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="sustainability-297242-tab" role="tabpanel" aria-labelledby="sustainability-297242">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Sustainability Score</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="sustainability-score" role="progressbar" aria-label="progress" title="sustainability-score" aria-labelledby="sustainability-score" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">100</div>
                           </div>
                        </div>
                         </div>
                      </div>

                     <div class="tab-pane fade" id="more-info-tab-297242-tab" role="tabpanel" aria-labelledby="more-info-tab-297242">
                        <div class="new-rankings-indicator-wrap py-2">

                           <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Fees</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                -
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Scholarship</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                Yes
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Student Mix</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                Domestic 61%   International 39%
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">English Tests</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                <a href="javascript:void(0)" class="_openfilter_results_js">Generate Result</a>
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Academic Tests</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                <a href="javascript:void(0)" class="_openfilter_results_js">Generate Result</a>
                              </div>
                           </div>
                        </div>


                        </div>

                        <div class="signup-for-user signup-for-user-js d-none">
                           <p>In order to see the data <a href="javascript:void(0)" class="signup-for-user-js-dlyr" data-toggle="modal" data-target="#emailModal">Sign up for free</a></p>
                        </div>


                     </div>

                  </div>
               </div>


            </div>

         </div>
      </div>
   </div>

   <div class="ind firstloaded main ranking-row-js-294481" nid="294481">
      <div class="">
         <div class="new-ranking-cards  normal-row">

            <div class="left-div-200">
               <div class="rank-square height-97px dark-blue padding-top-24">
                  <span class="rank-title mobile-upper">Rank</span>
                  <span class="rank-no">
                     26
                     <span class="dagger-icon-new d-none">
                        <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/dagger.svg" alt="Dagger Icon">
                     </span>
                  </span>
               </div>
               <div class="height-1px">
               </div>
               
               


               <div class="rank-square height-163px light-blue padding-top-32 text-align-mobile">
                  
                  

                 

                 


                  <span class="rank-title di-inline">Overall Score:</span>
                  <span class="rank-score di-inline">83.5</span>
               </div>
            </div>

            <div class="right-div-200">

               <div class="row">
                  <div class="col-lg-7 col-md-12 col-sm-12">
                     <div class="university-details-name">

                        <div class="univ-names-text">
                           <span class="logo-wrapper new-rank ">
                              <a href="/universities/epfl-ecole-polytechnique-federale-de-lausanne">
                                <img fetchpriority="low" loading="lazy" src="https://www.topuniversities.com/sites/default/files/epfl-ecole-polytechnique-federale-de-lausanne_592560cf2aeae70239af4b34_medium.jpg" alt="EPFL – École polytechnique fédérale de Lausanne" title="EPFL – École polytechnique fédérale de Lausanne" height="78" width="78">
                              </a>
                           </span>

                           <a href="/universities/epfl-ecole-polytechnique-federale-de-lausanne" class="uni-link">EPFL – École polytechnique fédérale de Lausanne</a>

                           <div class="location">
                              <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/location.svg" height="12" width="12" alt="location" title="location"> Lausanne,  Switzerland
                           </div>

                           <div class="stars d-none">
                             <span class="ranking-star">
                               <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/stars.svg" height="20" width="20" alt="QS stars" title="QS stars">
                             </span>
                             <span class="rating_number"></span>
                             <span class="qs-stars-font">QS Stars</span>
                           </div> 



                        </div>
                     </div>
                  </div>

               <div class="col-lg-5 col-md-12 col-sm-12">
                  <div class="shortlist-compare-div">
                     <div class="shortlist_div_new">
                        <a class="wishlist _directorypage shortlistnonloggedglobaljs   _shortlist_nid_294481  shortlistnonloggedglobaljs_dlyr" progoruniv="univ" nid="294481" onclick="Drupal.behaviors.tu_d8._adduniversityShortlist(this, 294481, 'university')">
                           <i class="fa fa-heart" aria-hidden="true"></i>
                           <i class="fal fa-heart" aria-hidden="true"></i>
                           <span class="_addShortText">Shortlist</span>
                        </a>
                     </div>

                     <div class="compare_div_new">
                        <a href="javascript:void(0)" class="compare _globCompUniv_js _globcompare_universityCookie_js_294481 comparenonloggedglobaljs_dlyr" nid="294481" progoruniv="univ" onclick="Drupal.behaviors.tu_d8._adduniversityCompare(this, 294481)">
                           <span class="two-square-icon">
                              <i class="fal fa-circle" aria-hidden="true"></i>
                           </span>
                           <span class="change-text">Compare</span>
                        </a>
                     </div>
                  </div>
               </div>

               </div>



               <div class="new-rankings-tab-content-wrapper">
                  <div class="arrows-left-right-tab arrows-left-right-tab-js">
                     <button class="btn-arrows btn-right-pick btn-arrows-js" scrollnid="294481" direction="right" aria-label="rightButton">
                        <img src="/modules/custom/qs_rankings_rest_api/assets/chevron-right.png" alt="Arrows">
                     </button>
                     <button class="btn-arrows btn-left-pick btn-arrows-js d-none" scrollnid="294481" direction="left" aria-label="leftButton">
                        <img src="/modules/custom/qs_rankings_rest_api/assets/chevron-left.png" alt="Arrows">
                     </button>
                  </div>
                  <ul class="nav nav-tabs m-0 scroll-this-side-294481-js" id="myTab" role="none">
                     <li class="nav-item ">
                                   <a class="nav-link active" id="research-discovery-294481" data-toggle="tab" href="#research-discovery-294481-tab">
                                   Research &amp; Discovery
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="learning-experience-294481" data-toggle="tab" href="#learning-experience-294481-tab">
                                   Learning Experience
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="employability-294481" data-toggle="tab" href="#employability-294481-tab">
                                   Employability
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="global-engagement-294481" data-toggle="tab" href="#global-engagement-294481-tab">
                                   Global Engagement
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="sustainability-294481" data-toggle="tab" href="#sustainability-294481-tab">
                                   Sustainability
                                   </a>
                                </li>
                     <li class="nav-item" role="none">
                        <a class="nav-link" id="more-info-tab-294481" data-toggle="tab" href="#more-info-tab-294481-tab">More Info
                           <span class="new-line">NEW</span>
                           <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/lock.svg" height="14" width="12" alt="lock" title="lock" class="lock-icon-checked-js d-none">
                        </a>
                     </li>
                  </ul>
                  <div class="tab-content py-2" id="myTabContent">

                     <div class="tab-pane fade show active" id="research-discovery-294481-tab" role="tabpanel" aria-labelledby="research-discovery-294481">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Academic Reputation</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="academic-reputation" role="progressbar" aria-label="progress" title="academic-reputation" aria-labelledby="academic-reputation" style="width: 84.2%" aria-valuenow="84.2" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">84.2</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Citations per Faculty</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="citations-per-faculty" role="progressbar" aria-label="progress" title="citations-per-faculty" aria-labelledby="citations-per-faculty" style="width: 93.6%" aria-valuenow="93.6" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">93.6</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="learning-experience-294481-tab" role="tabpanel" aria-labelledby="learning-experience-294481">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Faculty Student Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="faculty-student-ratio" role="progressbar" aria-label="progress" title="faculty-student-ratio" aria-labelledby="faculty-student-ratio" style="width: 91.2%" aria-valuenow="91.2" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">91.2</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="employability-294481-tab" role="tabpanel" aria-labelledby="employability-294481">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Employer Reputation</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="employer-reputation" role="progressbar" aria-label="progress" title="employer-reputation" aria-labelledby="employer-reputation" style="width: 67.2%" aria-valuenow="67.2" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">67.2</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Employment Outcomes</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="employment-outcomes" role="progressbar" aria-label="progress" title="employment-outcomes" aria-labelledby="employment-outcomes" style="width: 27.2%" aria-valuenow="27.2" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">27.2</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="global-engagement-294481-tab" role="tabpanel" aria-labelledby="global-engagement-294481">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Student Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-student-ratio" role="progressbar" aria-label="progress" title="international-student-ratio" aria-labelledby="international-student-ratio" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">100</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Research Network</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-research-network" role="progressbar" aria-label="progress" title="international-research-network" aria-labelledby="international-research-network" style="width: 81.7%" aria-valuenow="81.7" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">81.7</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Faculty Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-faculty-ratio" role="progressbar" aria-label="progress" title="international-faculty-ratio" aria-labelledby="international-faculty-ratio" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">100</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="sustainability-294481-tab" role="tabpanel" aria-labelledby="sustainability-294481">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Sustainability Score</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="sustainability-score" role="progressbar" aria-label="progress" title="sustainability-score" aria-labelledby="sustainability-score" style="width: 86.7%" aria-valuenow="86.7" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">86.7</div>
                           </div>
                        </div>
                         </div>
                      </div>

                     <div class="tab-pane fade" id="more-info-tab-294481-tab" role="tabpanel" aria-labelledby="more-info-tab-294481">
                        <div class="new-rankings-indicator-wrap py-2">

                           <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Fees</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                1540(CHF)
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Scholarship</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                Yes
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Student Mix</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                Domestic 36%   International 64%
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">English Tests</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                <a href="javascript:void(0)" class="_openfilter_results_js">Generate Result</a>
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Academic Tests</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                <a href="javascript:void(0)" class="_openfilter_results_js">Generate Result</a>
                              </div>
                           </div>
                        </div>


                        </div>

                        <div class="signup-for-user signup-for-user-js d-none">
                           <p>In order to see the data <a href="javascript:void(0)" class="signup-for-user-js-dlyr" data-toggle="modal" data-target="#emailModal">Sign up for free</a></p>
                        </div>


                     </div>

                  </div>
               </div>


            </div>

         </div>
      </div>
   </div>

   <div class="ind firstloaded main ranking-row-js-294478" nid="294478">
      <div class="">
         <div class="new-ranking-cards advanced_profile new normal-row">

            <div class="left-div-200">
               <div class="rank-square height-97px dark-blue padding-top-24">
                  <span class="rank-title mobile-upper">Rank</span>
                  <span class="rank-no">
                     27
                     <span class="dagger-icon-new d-none">
                        <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/dagger.svg" alt="Dagger Icon">
                     </span>
                  </span>
               </div>
               <div class="height-1px">
               </div>
               
               


               <div class="rank-square height-163px light-blue padding-top-32 text-align-mobile">
                  
                  

                 

                 


                  <span class="rank-title di-inline">Overall Score:</span>
                  <span class="rank-score di-inline">83.3</span>
               </div>
            </div>

            <div class="right-div-200">

               <div class="row">
                  <div class="col-lg-7 col-md-12 col-sm-12">
                     <div class="university-details-name">

                        <div class="univ-names-text">
                           <span class="logo-wrapper new-rank ">
                              <a href="/universities/university-edinburgh">
                                <img fetchpriority="low" loading="lazy" src="https://www.topuniversities.com/sites/default/files/the-university-of-edinburgh_180_medium.jpg" alt="The University of Edinburgh" title="The University of Edinburgh" height="78" width="78">
                              </a>
                           </span>

                           <a href="/universities/university-edinburgh" class="uni-link">The University of Edinburgh</a>

                           <div class="location">
                              <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/location.svg" height="12" width="12" alt="location" title="location"> Edinburgh,  United Kingdom
                           </div>

                           <div class="stars d-none">
                             <span class="ranking-star">
                               <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/stars.svg" height="20" width="20" alt="QS stars" title="QS stars">
                             </span>
                             <span class="rating_number"></span>
                             <span class="qs-stars-font">QS Stars</span>
                           </div> 



                        </div>
                     </div>
                  </div>

               <div class="col-lg-5 col-md-12 col-sm-12">
                  <div class="shortlist-compare-div">
                     <div class="shortlist_div_new">
                        <a class="wishlist _directorypage shortlistnonloggedglobaljs   _shortlist_nid_294478  shortlistnonloggedglobaljs_dlyr" progoruniv="univ" nid="294478" onclick="Drupal.behaviors.tu_d8._adduniversityShortlist(this, 294478, 'university')">
                           <i class="fa fa-heart" aria-hidden="true"></i>
                           <i class="fal fa-heart" aria-hidden="true"></i>
                           <span class="_addShortText">Shortlist</span>
                        </a>
                     </div>

                     <div class="compare_div_new">
                        <a href="javascript:void(0)" class="compare _globCompUniv_js _globcompare_universityCookie_js_294478 comparenonloggedglobaljs_dlyr" nid="294478" progoruniv="univ" onclick="Drupal.behaviors.tu_d8._adduniversityCompare(this, 294478)">
                           <span class="two-square-icon">
                              <i class="fal fa-circle" aria-hidden="true"></i>
                           </span>
                           <span class="change-text">Compare</span>
                        </a>
                     </div>
                  </div>
               </div>

               </div>



               <div class="new-rankings-tab-content-wrapper">
                  <div class="arrows-left-right-tab arrows-left-right-tab-js">
                     <button class="btn-arrows btn-right-pick btn-arrows-js" scrollnid="294478" direction="right" aria-label="rightButton">
                        <img src="/modules/custom/qs_rankings_rest_api/assets/chevron-right.png" alt="Arrows">
                     </button>
                     <button class="btn-arrows btn-left-pick btn-arrows-js d-none" scrollnid="294478" direction="left" aria-label="leftButton">
                        <img src="/modules/custom/qs_rankings_rest_api/assets/chevron-left.png" alt="Arrows">
                     </button>
                  </div>
                  <ul class="nav nav-tabs m-0 scroll-this-side-294478-js" id="myTab" role="none">
                     <li class="nav-item ">
                                   <a class="nav-link active" id="research-discovery-294478" data-toggle="tab" href="#research-discovery-294478-tab">
                                   Research &amp; Discovery
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="learning-experience-294478" data-toggle="tab" href="#learning-experience-294478-tab">
                                   Learning Experience
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="employability-294478" data-toggle="tab" href="#employability-294478-tab">
                                   Employability
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="global-engagement-294478" data-toggle="tab" href="#global-engagement-294478-tab">
                                   Global Engagement
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="sustainability-294478" data-toggle="tab" href="#sustainability-294478-tab">
                                   Sustainability
                                   </a>
                                </li>
                     <li class="nav-item" role="none">
                        <a class="nav-link" id="more-info-tab-294478" data-toggle="tab" href="#more-info-tab-294478-tab">More Info
                           <span class="new-line">NEW</span>
                           <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/lock.svg" height="14" width="12" alt="lock" title="lock" class="lock-icon-checked-js d-none">
                        </a>
                     </li>
                  </ul>
                  <div class="tab-content py-2" id="myTabContent">

                     <div class="tab-pane fade show active" id="research-discovery-294478-tab" role="tabpanel" aria-labelledby="research-discovery-294478">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Academic Reputation</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="academic-reputation" role="progressbar" aria-label="progress" title="academic-reputation" aria-labelledby="academic-reputation" style="width: 98.3%" aria-valuenow="98.3" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">98.3</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Citations per Faculty</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="citations-per-faculty" role="progressbar" aria-label="progress" title="citations-per-faculty" aria-labelledby="citations-per-faculty" style="width: 47.7%" aria-valuenow="47.7" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">47.7</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="learning-experience-294478-tab" role="tabpanel" aria-labelledby="learning-experience-294478">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Faculty Student Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="faculty-student-ratio" role="progressbar" aria-label="progress" title="faculty-student-ratio" aria-labelledby="faculty-student-ratio" style="width: 65.5%" aria-valuenow="65.5" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">65.5</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="employability-294478-tab" role="tabpanel" aria-labelledby="employability-294478">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Employer Reputation</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="employer-reputation" role="progressbar" aria-label="progress" title="employer-reputation" aria-labelledby="employer-reputation" style="width: 97.2%" aria-valuenow="97.2" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">97.2</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Employment Outcomes</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="employment-outcomes" role="progressbar" aria-label="progress" title="employment-outcomes" aria-labelledby="employment-outcomes" style="width: 55.9%" aria-valuenow="55.9" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">55.9</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="global-engagement-294478-tab" role="tabpanel" aria-labelledby="global-engagement-294478">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Student Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-student-ratio" role="progressbar" aria-label="progress" title="international-student-ratio" aria-labelledby="international-student-ratio" style="width: 99.8%" aria-valuenow="99.8" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">99.8</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Research Network</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-research-network" role="progressbar" aria-label="progress" title="international-research-network" aria-labelledby="international-research-network" style="width: 99.5%" aria-valuenow="99.5" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">99.5</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Faculty Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-faculty-ratio" role="progressbar" aria-label="progress" title="international-faculty-ratio" aria-labelledby="international-faculty-ratio" style="width: 98.7%" aria-valuenow="98.7" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">98.7</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="sustainability-294478-tab" role="tabpanel" aria-labelledby="sustainability-294478">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Sustainability Score</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="sustainability-score" role="progressbar" aria-label="progress" title="sustainability-score" aria-labelledby="sustainability-score" style="width: 99%" aria-valuenow="99" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">99</div>
                           </div>
                        </div>
                         </div>
                      </div>

                     <div class="tab-pane fade" id="more-info-tab-294478-tab" role="tabpanel" aria-labelledby="more-info-tab-294478">
                        <div class="new-rankings-indicator-wrap py-2">

                           <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Fees</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                -
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Scholarship</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                Yes
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Student Mix</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                Domestic 52%   International 48%
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">English Tests</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                <a href="javascript:void(0)" class="_openfilter_results_js">Generate Result</a>
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Academic Tests</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                <a href="javascript:void(0)" class="_openfilter_results_js">Generate Result</a>
                              </div>
                           </div>
                        </div>


                        </div>

                        <div class="signup-for-user signup-for-user-js d-none">
                           <p>In order to see the data <a href="javascript:void(0)" class="signup-for-user-js-dlyr" data-toggle="modal" data-target="#emailModal">Sign up for free</a></p>
                        </div>


                     </div>

                  </div>
               </div>


            </div>

         </div>
      </div>
   </div>

   <div class="ind firstloaded main ranking-row-js-297262" nid="297262">
      <div class="">
         <div class="new-ranking-cards  normal-row">

            <div class="left-div-200">
               <div class="rank-square height-97px dark-blue padding-top-24">
                  <span class="rank-title mobile-upper">Rank</span>
                  <span class="rank-no">
                     28
                     <span class="dagger-icon-new d-none">
                        <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/dagger.svg" alt="Dagger Icon">
                     </span>
                  </span>
               </div>
               <div class="height-1px">
               </div>
               
               


               <div class="rank-square height-163px light-blue padding-top-32 text-align-mobile">
                  
                  

                 

                 


                  <span class="rank-title di-inline">Overall Score:</span>
                  <span class="rank-score di-inline">83.2</span>
               </div>
            </div>

            <div class="right-div-200">

               <div class="row">
                  <div class="col-lg-7 col-md-12 col-sm-12">
                     <div class="university-details-name">

                        <div class="univ-names-text">
                           <span class="logo-wrapper new-rank ">
                              <a href="/universities/technical-university-munich">
                                <img fetchpriority="low" loading="lazy" src="https://www.topuniversities.com/sites/default/files/technical-university-of-munich_599_medium.jpg" alt="Technical University of Munich" title="Technical University of Munich" height="78" width="78">
                              </a>
                           </span>

                           <a href="/universities/technical-university-munich" class="uni-link">Technical University of Munich</a>

                           <div class="location">
                              <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/location.svg" height="12" width="12" alt="location" title="location"> Munich,  Germany
                           </div>

                           <div class="stars d-none">
                             <span class="ranking-star">
                               <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/stars.svg" height="20" width="20" alt="QS stars" title="QS stars">
                             </span>
                             <span class="rating_number"></span>
                             <span class="qs-stars-font">QS Stars</span>
                           </div> 



                        </div>
                     </div>
                  </div>

               <div class="col-lg-5 col-md-12 col-sm-12">
                  <div class="shortlist-compare-div">
                     <div class="shortlist_div_new">
                        <a class="wishlist _directorypage shortlistnonloggedglobaljs   _shortlist_nid_297262  shortlistnonloggedglobaljs_dlyr" progoruniv="univ" nid="297262" onclick="Drupal.behaviors.tu_d8._adduniversityShortlist(this, 297262, 'university')">
                           <i class="fa fa-heart" aria-hidden="true"></i>
                           <i class="fal fa-heart" aria-hidden="true"></i>
                           <span class="_addShortText">Shortlist</span>
                        </a>
                     </div>

                     <div class="compare_div_new">
                        <a href="javascript:void(0)" class="compare _globCompUniv_js _globcompare_universityCookie_js_297262 comparenonloggedglobaljs_dlyr" nid="297262" progoruniv="univ" onclick="Drupal.behaviors.tu_d8._adduniversityCompare(this, 297262)">
                           <span class="two-square-icon">
                              <i class="fal fa-circle" aria-hidden="true"></i>
                           </span>
                           <span class="change-text">Compare</span>
                        </a>
                     </div>
                  </div>
               </div>

               </div>



               <div class="new-rankings-tab-content-wrapper">
                  <div class="arrows-left-right-tab arrows-left-right-tab-js">
                     <button class="btn-arrows btn-right-pick btn-arrows-js" scrollnid="297262" direction="right" aria-label="rightButton">
                        <img src="/modules/custom/qs_rankings_rest_api/assets/chevron-right.png" alt="Arrows">
                     </button>
                     <button class="btn-arrows btn-left-pick btn-arrows-js d-none" scrollnid="297262" direction="left" aria-label="leftButton">
                        <img src="/modules/custom/qs_rankings_rest_api/assets/chevron-left.png" alt="Arrows">
                     </button>
                  </div>
                  <ul class="nav nav-tabs m-0 scroll-this-side-297262-js" id="myTab" role="none">
                     <li class="nav-item ">
                                   <a class="nav-link active" id="research-discovery-297262" data-toggle="tab" href="#research-discovery-297262-tab">
                                   Research &amp; Discovery
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="learning-experience-297262" data-toggle="tab" href="#learning-experience-297262-tab">
                                   Learning Experience
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="employability-297262" data-toggle="tab" href="#employability-297262-tab">
                                   Employability
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="global-engagement-297262" data-toggle="tab" href="#global-engagement-297262-tab">
                                   Global Engagement
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="sustainability-297262" data-toggle="tab" href="#sustainability-297262-tab">
                                   Sustainability
                                   </a>
                                </li>
                     <li class="nav-item" role="none">
                        <a class="nav-link" id="more-info-tab-297262" data-toggle="tab" href="#more-info-tab-297262-tab">More Info
                           <span class="new-line">NEW</span>
                           <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/lock.svg" height="14" width="12" alt="lock" title="lock" class="lock-icon-checked-js d-none">
                        </a>
                     </li>
                  </ul>
                  <div class="tab-content py-2" id="myTabContent">

                     <div class="tab-pane fade show active" id="research-discovery-297262-tab" role="tabpanel" aria-labelledby="research-discovery-297262">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Academic Reputation</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="academic-reputation" role="progressbar" aria-label="progress" title="academic-reputation" aria-labelledby="academic-reputation" style="width: 83%" aria-valuenow="83" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">83</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Citations per Faculty</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="citations-per-faculty" role="progressbar" aria-label="progress" title="citations-per-faculty" aria-labelledby="citations-per-faculty" style="width: 75.9%" aria-valuenow="75.9" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">75.9</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="learning-experience-297262-tab" role="tabpanel" aria-labelledby="learning-experience-297262">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Faculty Student Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="faculty-student-ratio" role="progressbar" aria-label="progress" title="faculty-student-ratio" aria-labelledby="faculty-student-ratio" style="width: 76.8%" aria-valuenow="76.8" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">76.8</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="employability-297262-tab" role="tabpanel" aria-labelledby="employability-297262">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Employer Reputation</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="employer-reputation" role="progressbar" aria-label="progress" title="employer-reputation" aria-labelledby="employer-reputation" style="width: 98.6%" aria-valuenow="98.6" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">98.6</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Employment Outcomes</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="employment-outcomes" role="progressbar" aria-label="progress" title="employment-outcomes" aria-labelledby="employment-outcomes" style="width: 34.5%" aria-valuenow="34.5" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">34.5</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="global-engagement-297262-tab" role="tabpanel" aria-labelledby="global-engagement-297262">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Student Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-student-ratio" role="progressbar" aria-label="progress" title="international-student-ratio" aria-labelledby="international-student-ratio" style="width: 98.6%" aria-valuenow="98.6" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">98.6</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Research Network</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-research-network" role="progressbar" aria-label="progress" title="international-research-network" aria-labelledby="international-research-network" style="width: 95.6%" aria-valuenow="95.6" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">95.6</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Faculty Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-faculty-ratio" role="progressbar" aria-label="progress" title="international-faculty-ratio" aria-labelledby="international-faculty-ratio" style="width: 80.4%" aria-valuenow="80.4" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">80.4</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="sustainability-297262-tab" role="tabpanel" aria-labelledby="sustainability-297262">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Sustainability Score</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="sustainability-score" role="progressbar" aria-label="progress" title="sustainability-score" aria-labelledby="sustainability-score" style="width: 93.1%" aria-valuenow="93.1" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">93.1</div>
                           </div>
                        </div>
                         </div>
                      </div>

                     <div class="tab-pane fade" id="more-info-tab-297262-tab" role="tabpanel" aria-labelledby="more-info-tab-297262">
                        <div class="new-rankings-indicator-wrap py-2">

                           <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Fees</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                -
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Scholarship</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                No
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Student Mix</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                Domestic 56%   International 44%
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">English Tests</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                <a href="javascript:void(0)" class="_openfilter_results_js">Generate Result</a>
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Academic Tests</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                <a href="javascript:void(0)" class="_openfilter_results_js">Generate Result</a>
                              </div>
                           </div>
                        </div>


                        </div>

                        <div class="signup-for-user signup-for-user-js d-none">
                           <p>In order to see the data <a href="javascript:void(0)" class="signup-for-user-js-dlyr" data-toggle="modal" data-target="#emailModal">Sign up for free</a></p>
                        </div>


                     </div>

                  </div>
               </div>


            </div>

         </div>
      </div>
   </div>

   <div class="ind firstloaded main ranking-row-js-294864" nid="294864">
      <div class="">
         <div class="new-ranking-cards advanced_profile new normal-row">

            <div class="left-div-200">
               <div class="rank-square height-97px dark-blue padding-top-24">
                  <span class="rank-title mobile-upper">Rank</span>
                  <span class="rank-no">
                     29
                     <span class="dagger-icon-new d-none">
                        <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/dagger.svg" alt="Dagger Icon">
                     </span>
                  </span>
               </div>
               <div class="height-1px">
               </div>
               
               


               <div class="rank-square height-163px light-blue padding-top-32 text-align-mobile">
                  
                  

                 

                 


                  <span class="rank-title di-inline">Overall Score:</span>
                  <span class="rank-score di-inline">83</span>
               </div>
            </div>

            <div class="right-div-200">

               <div class="row">
                  <div class="col-lg-7 col-md-12 col-sm-12">
                     <div class="university-details-name">

                        <div class="univ-names-text">
                           <span class="logo-wrapper new-rank ">
                              <a href="/universities/mcgill-university">
                                <img fetchpriority="low" loading="lazy" src="https://www.topuniversities.com/sites/default/files/241015074048pm463694McGill-Martlet-90x90.jpg" alt="McGill University" title="McGill University" height="78" width="78">
                              </a>
                           </span>

                           <a href="/universities/mcgill-university" class="uni-link">McGill University</a>

                           <div class="location">
                              <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/location.svg" height="12" width="12" alt="location" title="location"> Montreal,  Canada
                           </div>

                           <div class="stars d-none">
                             <span class="ranking-star">
                               <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/stars.svg" height="20" width="20" alt="QS stars" title="QS stars">
                             </span>
                             <span class="rating_number"></span>
                             <span class="qs-stars-font">QS Stars</span>
                           </div> 



                        </div>
                     </div>
                  </div>

               <div class="col-lg-5 col-md-12 col-sm-12">
                  <div class="shortlist-compare-div">
                     <div class="shortlist_div_new">
                        <a class="wishlist _directorypage shortlistnonloggedglobaljs   _shortlist_nid_294864  shortlistnonloggedglobaljs_dlyr" progoruniv="univ" nid="294864" onclick="Drupal.behaviors.tu_d8._adduniversityShortlist(this, 294864, 'university')">
                           <i class="fa fa-heart" aria-hidden="true"></i>
                           <i class="fal fa-heart" aria-hidden="true"></i>
                           <span class="_addShortText">Shortlist</span>
                        </a>
                     </div>

                     <div class="compare_div_new">
                        <a href="javascript:void(0)" class="compare _globCompUniv_js _globcompare_universityCookie_js_294864 comparenonloggedglobaljs_dlyr" nid="294864" progoruniv="univ" onclick="Drupal.behaviors.tu_d8._adduniversityCompare(this, 294864)">
                           <span class="two-square-icon">
                              <i class="fal fa-circle" aria-hidden="true"></i>
                           </span>
                           <span class="change-text">Compare</span>
                        </a>
                     </div>
                  </div>
               </div>

               </div>



               <div class="new-rankings-tab-content-wrapper">
                  <div class="arrows-left-right-tab arrows-left-right-tab-js">
                     <button class="btn-arrows btn-right-pick btn-arrows-js" scrollnid="294864" direction="right" aria-label="rightButton">
                        <img src="/modules/custom/qs_rankings_rest_api/assets/chevron-right.png" alt="Arrows">
                     </button>
                     <button class="btn-arrows btn-left-pick btn-arrows-js d-none" scrollnid="294864" direction="left" aria-label="leftButton">
                        <img src="/modules/custom/qs_rankings_rest_api/assets/chevron-left.png" alt="Arrows">
                     </button>
                  </div>
                  <ul class="nav nav-tabs m-0 scroll-this-side-294864-js" id="myTab" role="none">
                     <li class="nav-item ">
                                   <a class="nav-link active" id="research-discovery-294864" data-toggle="tab" href="#research-discovery-294864-tab">
                                   Research &amp; Discovery
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="learning-experience-294864" data-toggle="tab" href="#learning-experience-294864-tab">
                                   Learning Experience
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="employability-294864" data-toggle="tab" href="#employability-294864-tab">
                                   Employability
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="global-engagement-294864" data-toggle="tab" href="#global-engagement-294864-tab">
                                   Global Engagement
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="sustainability-294864" data-toggle="tab" href="#sustainability-294864-tab">
                                   Sustainability
                                   </a>
                                </li>
                     <li class="nav-item" role="none">
                        <a class="nav-link" id="more-info-tab-294864" data-toggle="tab" href="#more-info-tab-294864-tab">More Info
                           <span class="new-line">NEW</span>
                           <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/lock.svg" height="14" width="12" alt="lock" title="lock" class="lock-icon-checked-js d-none">
                        </a>
                     </li>
                  </ul>
                  <div class="tab-content py-2" id="myTabContent">

                     <div class="tab-pane fade show active" id="research-discovery-294864-tab" role="tabpanel" aria-labelledby="research-discovery-294864">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Academic Reputation</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="academic-reputation" role="progressbar" aria-label="progress" title="academic-reputation" aria-labelledby="academic-reputation" style="width: 94.3%" aria-valuenow="94.3" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">94.3</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Citations per Faculty</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="citations-per-faculty" role="progressbar" aria-label="progress" title="citations-per-faculty" aria-labelledby="citations-per-faculty" style="width: 57.9%" aria-valuenow="57.9" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">57.9</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="learning-experience-294864-tab" role="tabpanel" aria-labelledby="learning-experience-294864">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Faculty Student Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="faculty-student-ratio" role="progressbar" aria-label="progress" title="faculty-student-ratio" aria-labelledby="faculty-student-ratio" style="width: 62.3%" aria-valuenow="62.3" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">62.3</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="employability-294864-tab" role="tabpanel" aria-labelledby="employability-294864">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Employer Reputation</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="employer-reputation" role="progressbar" aria-label="progress" title="employer-reputation" aria-labelledby="employer-reputation" style="width: 87.6%" aria-valuenow="87.6" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">87.6</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Employment Outcomes</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="employment-outcomes" role="progressbar" aria-label="progress" title="employment-outcomes" aria-labelledby="employment-outcomes" style="width: 98.3%" aria-valuenow="98.3" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">98.3</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="global-engagement-294864-tab" role="tabpanel" aria-labelledby="global-engagement-294864">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Student Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-student-ratio" role="progressbar" aria-label="progress" title="international-student-ratio" aria-labelledby="international-student-ratio" style="width: 89.6%" aria-valuenow="89.6" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">89.6</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Research Network</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-research-network" role="progressbar" aria-label="progress" title="international-research-network" aria-labelledby="international-research-network" style="width: 94.2%" aria-valuenow="94.2" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">94.2</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Faculty Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-faculty-ratio" role="progressbar" aria-label="progress" title="international-faculty-ratio" aria-labelledby="international-faculty-ratio" style="width: 83.7%" aria-valuenow="83.7" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">83.7</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="sustainability-294864-tab" role="tabpanel" aria-labelledby="sustainability-294864">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Sustainability Score</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="sustainability-score" role="progressbar" aria-label="progress" title="sustainability-score" aria-labelledby="sustainability-score" style="width: 99.1%" aria-valuenow="99.1" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">99.1</div>
                           </div>
                        </div>
                         </div>
                      </div>

                     <div class="tab-pane fade" id="more-info-tab-294864-tab" role="tabpanel" aria-labelledby="more-info-tab-294864">
                        <div class="new-rankings-indicator-wrap py-2">

                           <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Fees</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                35000(CAD)
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Scholarship</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                Yes
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Student Mix</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                Domestic 66%   International 34%
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">English Tests</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                <a href="javascript:void(0)" class="_openfilter_results_js">Generate Result</a>
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Academic Tests</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                <a href="javascript:void(0)" class="_openfilter_results_js">Generate Result</a>
                              </div>
                           </div>
                        </div>


                        </div>

                        <div class="signup-for-user signup-for-user-js d-none">
                           <p>In order to see the data <a href="javascript:void(0)" class="signup-for-user-js-dlyr" data-toggle="modal" data-target="#emailModal">Sign up for free</a></p>
                        </div>


                     </div>

                  </div>
               </div>


            </div>

         </div>
      </div>
   </div>

   <div class="ind firstloaded main ranking-row-js-294616" nid="294616">
      <div class="">
         <div class="new-ranking-cards advanced_profile new normal-row">

            <div class="left-div-200">
               <div class="rank-square height-97px dark-blue padding-top-24">
                  <span class="rank-title mobile-upper">Rank</span>
                  <span class="rank-no">
                     30
                     <span class="dagger-icon-new d-none">
                        <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/dagger.svg" alt="Dagger Icon">
                     </span>
                  </span>
               </div>
               <div class="height-1px">
               </div>
               
               


               <div class="rank-square height-163px light-blue padding-top-32 text-align-mobile">
                  
                  

                 

                 


                  <span class="rank-title di-inline">Overall Score:</span>
                  <span class="rank-score di-inline">82.4</span>
               </div>
            </div>

            <div class="right-div-200">

               <div class="row">
                  <div class="col-lg-7 col-md-12 col-sm-12">
                     <div class="university-details-name">

                        <div class="univ-names-text">
                           <span class="logo-wrapper new-rank ">
                              <a href="/universities/australian-national-university-anu">
                                <img fetchpriority="low" loading="lazy" src="https://www.topuniversities.com/sites/default/files/ANU-crest-90x90.jpg" alt="Australian National University (ANU)" title="Australian National University (ANU)" height="78" width="78">
                              </a>
                           </span>

                           <a href="/universities/australian-national-university-anu" class="uni-link">Australian National University (ANU)</a>

                           <div class="location">
                              <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/location.svg" height="12" width="12" alt="location" title="location"> Canberra,  Australia
                           </div>

                           <div class="stars d-none">
                             <span class="ranking-star">
                               <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/stars.svg" height="20" width="20" alt="QS stars" title="QS stars">
                             </span>
                             <span class="rating_number"></span>
                             <span class="qs-stars-font">QS Stars</span>
                           </div> 



                        </div>
                     </div>
                  </div>

               <div class="col-lg-5 col-md-12 col-sm-12">
                  <div class="shortlist-compare-div">
                     <div class="shortlist_div_new">
                        <a class="wishlist _directorypage shortlistnonloggedglobaljs   _shortlist_nid_294616  shortlistnonloggedglobaljs_dlyr" progoruniv="univ" nid="294616" onclick="Drupal.behaviors.tu_d8._adduniversityShortlist(this, 294616, 'university')">
                           <i class="fa fa-heart" aria-hidden="true"></i>
                           <i class="fal fa-heart" aria-hidden="true"></i>
                           <span class="_addShortText">Shortlist</span>
                        </a>
                     </div>

                     <div class="compare_div_new">
                        <a href="javascript:void(0)" class="compare _globCompUniv_js _globcompare_universityCookie_js_294616 comparenonloggedglobaljs_dlyr" nid="294616" progoruniv="univ" onclick="Drupal.behaviors.tu_d8._adduniversityCompare(this, 294616)">
                           <span class="two-square-icon">
                              <i class="fal fa-circle" aria-hidden="true"></i>
                           </span>
                           <span class="change-text">Compare</span>
                        </a>
                     </div>
                  </div>
               </div>

               </div>



               <div class="new-rankings-tab-content-wrapper">
                  <div class="arrows-left-right-tab arrows-left-right-tab-js">
                     <button class="btn-arrows btn-right-pick btn-arrows-js" scrollnid="294616" direction="right" aria-label="rightButton">
                        <img src="/modules/custom/qs_rankings_rest_api/assets/chevron-right.png" alt="Arrows">
                     </button>
                     <button class="btn-arrows btn-left-pick btn-arrows-js d-none" scrollnid="294616" direction="left" aria-label="leftButton">
                        <img src="/modules/custom/qs_rankings_rest_api/assets/chevron-left.png" alt="Arrows">
                     </button>
                  </div>
                  <ul class="nav nav-tabs m-0 scroll-this-side-294616-js" id="myTab" role="none">
                     <li class="nav-item ">
                                   <a class="nav-link active" id="research-discovery-294616" data-toggle="tab" href="#research-discovery-294616-tab">
                                   Research &amp; Discovery
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="learning-experience-294616" data-toggle="tab" href="#learning-experience-294616-tab">
                                   Learning Experience
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="employability-294616" data-toggle="tab" href="#employability-294616-tab">
                                   Employability
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="global-engagement-294616" data-toggle="tab" href="#global-engagement-294616-tab">
                                   Global Engagement
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="sustainability-294616" data-toggle="tab" href="#sustainability-294616-tab">
                                   Sustainability
                                   </a>
                                </li>
                     <li class="nav-item" role="none">
                        <a class="nav-link" id="more-info-tab-294616" data-toggle="tab" href="#more-info-tab-294616-tab">More Info
                           <span class="new-line">NEW</span>
                           <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/lock.svg" height="14" width="12" alt="lock" title="lock" class="lock-icon-checked-js d-none">
                        </a>
                     </li>
                  </ul>
                  <div class="tab-content py-2" id="myTabContent">

                     <div class="tab-pane fade show active" id="research-discovery-294616-tab" role="tabpanel" aria-labelledby="research-discovery-294616">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Academic Reputation</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="academic-reputation" role="progressbar" aria-label="progress" title="academic-reputation" aria-labelledby="academic-reputation" style="width: 93.8%" aria-valuenow="93.8" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">93.8</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Citations per Faculty</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="citations-per-faculty" role="progressbar" aria-label="progress" title="citations-per-faculty" aria-labelledby="citations-per-faculty" style="width: 84.6%" aria-valuenow="84.6" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">84.6</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="learning-experience-294616-tab" role="tabpanel" aria-labelledby="learning-experience-294616">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Faculty Student Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="faculty-student-ratio" role="progressbar" aria-label="progress" title="faculty-student-ratio" aria-labelledby="faculty-student-ratio" style="width: 34.6%" aria-valuenow="34.6" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">34.6</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="employability-294616-tab" role="tabpanel" aria-labelledby="employability-294616">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Employer Reputation</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="employer-reputation" role="progressbar" aria-label="progress" title="employer-reputation" aria-labelledby="employer-reputation" style="width: 75.4%" aria-valuenow="75.4" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">75.4</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Employment Outcomes</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="employment-outcomes" role="progressbar" aria-label="progress" title="employment-outcomes" aria-labelledby="employment-outcomes" style="width: 56.6%" aria-valuenow="56.6" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">56.6</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="global-engagement-294616-tab" role="tabpanel" aria-labelledby="global-engagement-294616">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Student Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-student-ratio" role="progressbar" aria-label="progress" title="international-student-ratio" aria-labelledby="international-student-ratio" style="width: 96.2%" aria-valuenow="96.2" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">96.2</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Research Network</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-research-network" role="progressbar" aria-label="progress" title="international-research-network" aria-labelledby="international-research-network" style="width: 91.4%" aria-valuenow="91.4" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">91.4</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Faculty Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-faculty-ratio" role="progressbar" aria-label="progress" title="international-faculty-ratio" aria-labelledby="international-faculty-ratio" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">100</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="sustainability-294616-tab" role="tabpanel" aria-labelledby="sustainability-294616">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Sustainability Score</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="sustainability-score" role="progressbar" aria-label="progress" title="sustainability-score" aria-labelledby="sustainability-score" style="width: 97.1%" aria-valuenow="97.1" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">97.1</div>
                           </div>
                        </div>
                         </div>
                      </div>

                     <div class="tab-pane fade" id="more-info-tab-294616-tab" role="tabpanel" aria-labelledby="more-info-tab-294616">
                        <div class="new-rankings-indicator-wrap py-2">

                           <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Fees</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                39024(AUD)
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Scholarship</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                Yes
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Student Mix</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                Domestic 60%   International 40%
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">English Tests</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                <a href="javascript:void(0)" class="_openfilter_results_js">Generate Result</a>
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Academic Tests</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                <a href="javascript:void(0)" class="_openfilter_results_js">Generate Result</a>
                              </div>
                           </div>
                        </div>


                        </div>

                        <div class="signup-for-user signup-for-user-js d-none">
                           <p>In order to see the data <a href="javascript:void(0)" class="signup-for-user-js-dlyr" data-toggle="modal" data-target="#emailModal">Sign up for free</a></p>
                        </div>


                     </div>

                  </div>
               </div>


            </div>

         </div>
      </div>
   </div>
</div>
        '''
        response = HtmlResponse(url="http://www.example.com", body=body, encoding='utf8')
        selector = Selector(response)
        rows = selector.xpath('//div[contains(@class, "new-ranking-cards")]')
        print(len(rows))
        self.assertTrue(len(rows) > 10)

    def test_card(self):
        body = '''
        <div class="ind firstloaded main ranking-row-js-294850" nid="294850">
      <div class="">
         <div class="new-ranking-cards  normal-row">

            <div class="left-div-200">
               <div class="rank-square height-97px dark-blue padding-top-24">
                  <span class="rank-title mobile-upper">Rank</span>
                  <span class="rank-no">
                     1
                     <span class="dagger-icon-new d-none">
                        <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/dagger.svg" alt="Dagger Icon">
                     </span>
                  </span>
               </div>
               <div class="height-1px">
               </div>
               
               


               <div class="rank-square height-163px light-blue padding-top-32 text-align-mobile">
                  
                  

                 

                 


                  <span class="rank-title di-inline">Overall Score:</span>
                  <span class="rank-score di-inline">100</span>
               </div>
            </div>

            <div class="right-div-200">

               <div class="row">
                  <div class="col-lg-7 col-md-12 col-sm-12">
                     <div class="university-details-name">

                        <div class="univ-names-text">
                           <span class="logo-wrapper new-rank ">
                              <a href="/universities/massachusetts-institute-technology-mit">
                                <img fetchpriority="low" loading="lazy" src="https://www.topuniversities.com/sites/default/files/massachusetts-institute-of-technology-mit_410_medium.jpg" alt="Massachusetts Institute of Technology (MIT) " title="Massachusetts Institute of Technology (MIT) " height="78" width="78">
                              </a>
                           </span>

                           <a href="/universities/massachusetts-institute-technology-mit" class="uni-link">Massachusetts Institute of Technology (MIT) </a>

                           <div class="location">
                              <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/location.svg" height="12" width="12" alt="location" title="location"> Cambridge,  United States
                           </div>

                           <div class="stars d-none">
                             <span class="ranking-star">
                               <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/stars.svg" height="20" width="20" alt="QS stars" title="QS stars">
                             </span>
                             <span class="rating_number"></span>
                             <span class="qs-stars-font">QS Stars</span>
                           </div> 



                        </div>
                     </div>
                  </div>

               <div class="col-lg-5 col-md-12 col-sm-12">
                  <div class="shortlist-compare-div">
                     <div class="shortlist_div_new">
                        <a class="wishlist _directorypage shortlistnonloggedglobaljs   _shortlist_nid_294850  shortlistnonloggedglobaljs_dlyr" progoruniv="univ" nid="294850" onclick="Drupal.behaviors.tu_d8._adduniversityShortlist(this, 294850, 'university')">
                           <i class="fa fa-heart" aria-hidden="true"></i>
                           <i class="fal fa-heart" aria-hidden="true"></i>
                           <span class="_addShortText">Shortlist</span>
                        </a>
                     </div>

                     <div class="compare_div_new">
                        <a href="javascript:void(0)" class="compare _globCompUniv_js _globcompare_universityCookie_js_294850 comparenonloggedglobaljs_dlyr" nid="294850" progoruniv="univ" onclick="Drupal.behaviors.tu_d8._adduniversityCompare(this, 294850)">
                           <span class="two-square-icon">
                              <i class="fal fa-circle" aria-hidden="true"></i>
                           </span>
                           <span class="change-text">Compare</span>
                        </a>
                     </div>
                  </div>
               </div>

               </div>



               <div class="new-rankings-tab-content-wrapper">
                  <div class="arrows-left-right-tab arrows-left-right-tab-js">
                     <button class="btn-arrows btn-right-pick btn-arrows-js" scrollnid="294850" direction="right" aria-label="rightButton">
                        <img src="/modules/custom/qs_rankings_rest_api/assets/chevron-right.png" alt="Arrows">
                     </button>
                     <button class="btn-arrows btn-left-pick btn-arrows-js d-none" scrollnid="294850" direction="left" aria-label="leftButton">
                        <img src="/modules/custom/qs_rankings_rest_api/assets/chevron-left.png" alt="Arrows">
                     </button>
                  </div>
                  <ul class="nav nav-tabs m-0 scroll-this-side-294850-js" id="myTab" role="none">
                     <li class="nav-item ">
                                   <a class="nav-link active" id="research-discovery-294850" data-toggle="tab" href="#research-discovery-294850-tab">
                                   Research &amp; Discovery
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="learning-experience-294850" data-toggle="tab" href="#learning-experience-294850-tab">
                                   Learning Experience
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="employability-294850" data-toggle="tab" href="#employability-294850-tab">
                                   Employability
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="global-engagement-294850" data-toggle="tab" href="#global-engagement-294850-tab">
                                   Global Engagement
                                   </a>
                                </li><li class="nav-item ">
                                   <a class="nav-link" id="sustainability-294850" data-toggle="tab" href="#sustainability-294850-tab">
                                   Sustainability
                                   </a>
                                </li>
                     <li class="nav-item" role="none">
                        <a class="nav-link" id="more-info-tab-294850" data-toggle="tab" href="#more-info-tab-294850-tab">More Info
                           <span class="new-line">NEW</span>
                           <img fetchpriority="low" loading="lazy" src="/modules/custom/qs_rankings_rest_api/assets/lock.svg" height="14" width="12" alt="lock" title="lock" class="lock-icon-checked-js d-none">
                        </a>
                     </li>
                  </ul>
                  <div class="tab-content py-2" id="myTabContent">

                     <div class="tab-pane fade show active" id="research-discovery-294850-tab" role="tabpanel" aria-labelledby="research-discovery-294850">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Academic Reputation</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="academic-reputation" role="progressbar" aria-label="progress" title="academic-reputation" aria-labelledby="academic-reputation" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">100</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Citations per Faculty</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="citations-per-faculty" role="progressbar" aria-label="progress" title="citations-per-faculty" aria-labelledby="citations-per-faculty" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">100</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="learning-experience-294850-tab" role="tabpanel" aria-labelledby="learning-experience-294850">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Faculty Student Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="faculty-student-ratio" role="progressbar" aria-label="progress" title="faculty-student-ratio" aria-labelledby="faculty-student-ratio" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">100</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="employability-294850-tab" role="tabpanel" aria-labelledby="employability-294850">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Employer Reputation</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="employer-reputation" role="progressbar" aria-label="progress" title="employer-reputation" aria-labelledby="employer-reputation" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">100</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Employment Outcomes</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="employment-outcomes" role="progressbar" aria-label="progress" title="employment-outcomes" aria-labelledby="employment-outcomes" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">100</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="global-engagement-294850-tab" role="tabpanel" aria-labelledby="global-engagement-294850">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Student Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-student-ratio" role="progressbar" aria-label="progress" title="international-student-ratio" aria-labelledby="international-student-ratio" style="width: 86.8%" aria-valuenow="86.8" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">86.8</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Research Network</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-research-network" role="progressbar" aria-label="progress" title="international-research-network" aria-labelledby="international-research-network" style="width: 96%" aria-valuenow="96" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">96</div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Faculty Ratio</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="international-faculty-ratio" role="progressbar" aria-label="progress" title="international-faculty-ratio" aria-labelledby="international-faculty-ratio" style="width: 99.3%" aria-valuenow="99.3" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">99.3</div>
                           </div>
                        </div>
                         </div>
                      </div><div class="tab-pane fade" id="sustainability-294850-tab" role="tabpanel" aria-labelledby="sustainability-294850">
                         <div class="new-rankings-indicator-wrap py-2">
                            <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Sustainability Score</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="progress">
                                 <div class="progress-bar" id="sustainability-score" role="progressbar" aria-label="progress" title="sustainability-score" aria-labelledby="sustainability-score" style="width: 99%" aria-valuenow="99" aria-valuemin="0" aria-valuemax="100"></div>
                              </div>
                              <div class="new-rankings-ind-val">99</div>
                           </div>
                        </div>
                         </div>
                      </div>

                     <div class="tab-pane fade" id="more-info-tab-294850-tab" role="tabpanel" aria-labelledby="more-info-tab-294850">
                        <div class="new-rankings-indicator-wrap py-2">

                           <div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">International Fees</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                -
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Scholarship</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                No
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Student Mix</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                Domestic 67%   International 33%
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">English Tests</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                <a href="javascript:void(0)" class="_openfilter_results_js">Generate Result</a>
                              </div>
                           </div>
                        </div><div class="new-rankings-indicator-container ">
                           <h2 class="new-rankings-ind">Academic Tests</h2>
                           <div class="new-rankings-ind-wrap">
                              <div class="new-rankings-ind-val">
                                <a href="javascript:void(0)" class="_openfilter_results_js">Generate Result</a>
                              </div>
                           </div>
                        </div>


                        </div>

                        <div class="signup-for-user signup-for-user-js d-none">
                           <p>In order to see the data <a href="javascript:void(0)" class="signup-for-user-js-dlyr" data-toggle="modal" data-target="#emailModal">Sign up for free</a></p>
                        </div>


                     </div>

                  </div>
               </div>


            </div>

         </div>
      </div>
   </div>
        '''
        response = HtmlResponse(url="http://www.example.com", body=body, encoding='utf8')
        selector = Selector(response)
        ranking = int(selector.xpath('.//span[@class="rank-no"]/text()').get())
        self.assertEqual(1, ranking)

        univerity_name = selector.xpath('.//div[@class="univ-names-text"]/a/text()').get().strip()
        self.assertEqual("'Massachusetts Institute of Technology (MIT)", univerity_name)

if __name__ == '__main__':
    unittest.main()



