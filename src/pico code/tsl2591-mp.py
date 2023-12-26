# This is a simple python library for the Adafruit TSL2591 breakout board based on the Arduino library from Adafruit.
# python-tsl2591 was developed to work on a Raspberry PI. I then forked it to create a Micropython version. 
# There were two changes from the original:
#
# Micropython does not provide an smbus api, so smbus was emulated on top of the lower-level I2C library it does provide.
# The ESP8266 and other chips are severely memory limited. With the Raspberry Pi version, even importing the tsl2591 module caused it to run out of memory on the ESP8266. 
# The code was simplified were possible and all the comments stripped out.






<!DOCTYPE html>
<html
  lang="en"
  
  data-color-mode="auto" data-light-theme="light" data-dark-theme="dark"
  data-a11y-animated-images="system" data-a11y-link-underlines="true"
  >




  <head>
    <meta charset="utf-8">
  <link rel="dns-prefetch" href="https://github.githubassets.com">
  <link rel="dns-prefetch" href="https://avatars.githubusercontent.com">
  <link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com">
  <link rel="dns-prefetch" href="https://user-images.githubusercontent.com/">
  <link rel="preconnect" href="https://github.githubassets.com" crossorigin>
  <link rel="preconnect" href="https://avatars.githubusercontent.com">

  


  <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/light-38f1bf52eeeb.css" /><link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/dark-56010aa53a8f.css" /><link data-color-theme="dark_dimmed" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_dimmed-b2e1b478d5b4.css" /><link data-color-theme="dark_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_high_contrast-e7f12ffa82f3.css" /><link data-color-theme="dark_colorblind" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_colorblind-ddca79c20026.css" /><link data-color-theme="light_colorblind" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_colorblind-8017b9c4037b.css" /><link data-color-theme="light_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_high_contrast-3ce2d3d8a4d3.css" /><link data-color-theme="light_tritanopia" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_tritanopia-02059c141ad5.css" /><link data-color-theme="dark_tritanopia" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_tritanopia-870ee47909bf.css" />
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/primer-primitives-971c6be3ec9f.css" />
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/primer-fb122a21966c.css" />
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/global-8ba101c75c8c.css" />
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/github-9ed33716809f.css" />
  <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/repository-2e5f0ce2e282.css" />
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/code-8f92bf8847ed.css" />

  

  <script type="application/json" id="client-env">{"locale":"en","featureFlags":["copilot_conversational_ux_streaming","copilot_cosmos_docsets","docset_management_ui","failbot_handle_non_errors","geojson_azure_maps","image_metric_tracking","turbo_experiment_risky","sample_network_conn_type","no_character_key_shortcuts_in_inputs"]}</script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/wp-runtime-305bcdf2887c.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_dompurify_dist_purify_js-6890e890956f.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_stacktrace-parser_dist_stack-trace-parser_esm_js-node_modules_github_bro-a4c183-79f9611c275b.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_github_hydro-analytics-client_dist_analytics-client_js-node_modules_gith-6a10dd-8837a7c17569.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/ui_packages_soft-nav_soft-nav_ts-3e05ff0dd044.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/environment-30e216bc209e.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_github_selector-observer_dist_index_esm_js-9f960d9b217c.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_behaviors_dist_esm_focus-zone_js-086f7a27bac0.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_github_relative-time-element_dist_index_js-c6fd49e3fd28.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_fzy_js_index_js-node_modules_github_combobox-nav_dist_index_js-node_modu-344bff-421f7a8c1008.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_delegated-events_dist_index_js-node_modules_github_details-dialog-elemen-29dc30-a2a71f11a507.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_github_filter-input-element_dist_index_js-node_modules_github_remote-inp-59c459-d0c49521eb35.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_github_file-attachment-element_dist_index_js-node_modules_primer_view-co-eb424d-e705be3ac5fd.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/github-elements-871cc8490a1f.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/element-registry-02245952093f.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_github_catalyst_lib_index_js-node_modules_github_hydro-analytics-client_-978abc0-15861e0630b6.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_lit-html_lit-html_js-5b376145beff.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_github_mini-throttle_dist_index_js-node_modules_github_alive-client_dist-bf5aa2-1b562c29ab8e.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_morphdom_dist_morphdom-esm_js-5bff297a06de.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_github_turbo_dist_turbo_es2017-esm_js-c91f4ad18b62.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_color-convert_index_js-72c9fbde5ad4.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_github_remote-form_dist_index_js-node_modules_scroll-anchoring_dist_scro-231ccf-aa129238d13b.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_github_session-resume_dist_index_js-node_modules_primer_behaviors_dist_e-ac74c6-c3eb71941f78.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_behaviors_dist_esm_dimensions_js-node_modules_github_jtml_lib_index_js-95b84ee6bc34.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_github_paste-markdown_dist_index_esm_js-node_modules_github_quote-select-618d6c-59676cf880fb.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/app_assets_modules_github_updatable-content_ts-793542f6e0fb.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/app_assets_modules_github_behaviors_task-list_ts-app_assets_modules_github_onfocus_ts-app_ass-079b43-06bdd3d1733f.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/app_assets_modules_github_sticky-scroll-into-view_ts-3aa02466adc1.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/app_assets_modules_github_behaviors_ajax-error_ts-app_assets_modules_github_behaviors_include-2e2258-70fc444f4dc3.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/app_assets_modules_github_behaviors_commenting_edit_ts-app_assets_modules_github_behaviors_ht-83c235-b85e9f4f1304.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/behaviors-5bf0b89f0de8.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_delegated-events_dist_index_js-node_modules_github_catalyst_lib_index_js-d0256ebff5cd.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/notifications-global-99d196517b1b.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/code-menu-2658b004279a.js"></script>
  
  <script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/react-lib-1fbfc5be2c18.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_octicons-react_dist_index_esm_js-node_modules_primer_react_lib-es-2e8e7c-8c382c96424c.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_lib-esm_Box_Box_js-ebfceb11fb57.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_lib-esm_Button_Button_js-8dba6638f78f.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_lib-esm_ActionList_index_js-64637eb4b092.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_lib-esm_Overlay_Overlay_js-node_modules_primer_react_lib-es-fa1130-68d43d9edda0.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_lib-esm_Text_Text_js-node_modules_primer_react_lib-esm_Text-85a14b-1f9979205253.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_lib-esm_AnchoredOverlay_AnchoredOverlay_js-node_modules_pri-b1f750-6fe378190175.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_lib-esm_FormControl_FormControl_js-c755973d1d95.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_react-router-dom_dist_index_js-cc35d258380c.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_lib-esm_PageLayout_PageLayout_js-ba78d3966b63.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_lib-esm_ConfirmationDialog_ConfirmationDialog_js-a4005c918a5e.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_lib-esm_Label_Label_js-node_modules_primer_react_lib-esm_Se-7a5fb9-bc014456cbfa.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_lib-esm_UnderlineNav_index_js-31fc785d7be7.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_lib-esm_AvatarStack_AvatarStack_js-node_modules_primer_reac-40f070-f8d674375999.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_lib-esm_Avatar_Avatar_js-node_modules_primer_react_lib-esm_-5d5372-988d6d9fd06c.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/ui_packages_react-core_create-browser-history_ts-ui_packages_react-core_deferred-registry_ts--ebbb92-f862877dad23.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/ui_packages_react-core_register-app_ts-9f191f2c684e.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/ui_packages_paths_index_ts-ddcba26493fd.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/ui_packages_ref-selector_RefSelector_tsx-858bb94813b1.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/app_assets_modules_github_blob-anchor_ts-app_assets_modules_github_filter-sort_ts-app_assets_-681869-277ebf7a9489.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/ui_packages_commit-attribution_index_ts-ui_packages_commit-checks-status_index_ts-ui_packages-5acf59-b1ba821344de.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/app_assets_modules_react-code-view_pages_CodeView_tsx-6a038b48e667.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/react-code-view-06c1645c719b.js"></script>


  <title>micropython-tsl2591/tsl2591.py at master · jfischer/micropython-tsl2591 · GitHub</title>



  <meta name="route-pattern" content="/:user_id/:repository/blob/*name(/*path)">

    
  <meta name="current-catalog-service-hash" content="82c569b93da5c18ed649ebd4c2c79437db4611a6a1373e805a3cb001c64130b7">


  <meta name="request-id" content="FEE7:3B2F36:10168D6B:10567467:658A35EB" data-pjax-transient="true"/><meta name="html-safe-nonce" content="191fb411be241cf6a25edf8730aca3575ed7266872629a28a6a59e4df5ccc0c9" data-pjax-transient="true"/><meta name="visitor-payload" content="eyJyZWZlcnJlciI6Imh0dHBzOi8vZ2l0aHViLmNvbS9qZmlzY2hlci9taWNyb3B5dGhvbi10c2wyNTkxIiwicmVxdWVzdF9pZCI6IkZFRTc6M0IyRjM2OjEwMTY4RDZCOjEwNTY3NDY3OjY1OEEzNUVCIiwidmlzaXRvcl9pZCI6IjI2NDM5MDUxMzA5Mzk5Mjg0NDIiLCJyZWdpb25fZWRnZSI6ImZyYSIsInJlZ2lvbl9yZW5kZXIiOiJmcmEifQ==" data-pjax-transient="true"/><meta name="visitor-hmac" content="bd23dcc1e382f0f381e872cb4c8a08afc9f85d3ce6cb13be3ad71042145eb315" data-pjax-transient="true"/>


    <meta name="hovercard-subject-tag" content="repository:62343362" data-turbo-transient>


  <meta name="github-keyboard-shortcuts" content="repository,source-code,file-tree" data-turbo-transient="true" />
  

  <meta name="selected-link" value="repo_source" data-turbo-transient>
  <link rel="assets" href="https://github.githubassets.com/">

    <meta name="google-site-verification" content="c1kuD-K2HIVF635lypcsWPoD4kilo5-jA_wBFyT4uMY">
  <meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU">
  <meta name="google-site-verification" content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA">
  <meta name="google-site-verification" content="GXs5KoUUkNCoaAZn7wPN-t01Pywp9M3sEjnt_3_ZWPc">
  <meta name="google-site-verification" content="Apib7-x98H0j5cPqHWwSMm6dNU4GmODRoqxLiDzdx9I">

<meta name="octolytics-url" content="https://collector.github.com/github/collect" />

  <meta name="analytics-location" content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-turbo-transient="true" />

  




  

    <meta name="user-login" content="">

  

    <meta name="viewport" content="width=device-width">
    
      <meta name="description" content="Port of maxlklaxl/python-tsl2591for micropython-based devices like the ESP8266. - micropython-tsl2591/tsl2591.py at master · jfischer/micropython-tsl2591">
      <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
    <meta property="fb:app_id" content="1401488693436528">
    <meta name="apple-itunes-app" content="app-id=1477376905, app-argument=https://github.com/jfischer/micropython-tsl2591/blob/master/tsl2591.py" />
      <meta name="twitter:image:src" content="https://opengraph.githubassets.com/0c9517ca9b17633712b6a721566bbc4274f05789e623662a4806db4f3caba73b/jfischer/micropython-tsl2591" /><meta name="twitter:site" content="@github" /><meta name="twitter:card" content="summary_large_image" /><meta name="twitter:title" content="micropython-tsl2591/tsl2591.py at master · jfischer/micropython-tsl2591" /><meta name="twitter:description" content="Port of maxlklaxl/python-tsl2591for micropython-based devices like the ESP8266. - jfischer/micropython-tsl2591" />
      <meta property="og:image" content="https://opengraph.githubassets.com/0c9517ca9b17633712b6a721566bbc4274f05789e623662a4806db4f3caba73b/jfischer/micropython-tsl2591" /><meta property="og:image:alt" content="Port of maxlklaxl/python-tsl2591for micropython-based devices like the ESP8266. - jfischer/micropython-tsl2591" /><meta property="og:image:width" content="1200" /><meta property="og:image:height" content="600" /><meta property="og:site_name" content="GitHub" /><meta property="og:type" content="object" /><meta property="og:title" content="micropython-tsl2591/tsl2591.py at master · jfischer/micropython-tsl2591" /><meta property="og:url" content="https://github.com/jfischer/micropython-tsl2591/blob/master/tsl2591.py" /><meta property="og:description" content="Port of maxlklaxl/python-tsl2591for micropython-based devices like the ESP8266. - jfischer/micropython-tsl2591" />
      



        <meta name="hostname" content="github.com">



        <meta name="expected-hostname" content="github.com">


  <meta http-equiv="x-pjax-version" content="80bd94eacfac033a62c188f8ea12d4bc4fe728be0e6261011a28599c6da9eac8" data-turbo-track="reload">
  <meta http-equiv="x-pjax-csp-version" content="611e3beaf6df2ba8f98070845c8e5ef70f0ffc535519af6685e8341fcd41c235" data-turbo-track="reload">
  <meta http-equiv="x-pjax-css-version" content="c4cb55d347cf7b0d10da54ebe2715d93a40d93e6d23973b95b92ac2b54b64160" data-turbo-track="reload">
  <meta http-equiv="x-pjax-js-version" content="c88d1c3e5723444522b9716ba1ba8dbe4d249b21258c05e1c4bf050131e67a8c" data-turbo-track="reload">

  <meta name="turbo-cache-control" content="no-preview" data-turbo-transient="">

      <meta name="turbo-cache-control" content="no-cache" data-turbo-transient>
    <meta data-hydrostats="publish">

  <meta name="go-import" content="github.com/jfischer/micropython-tsl2591 git https://github.com/jfischer/micropython-tsl2591.git">

  <meta name="octolytics-dimension-user_id" content="86544" /><meta name="octolytics-dimension-user_login" content="jfischer" /><meta name="octolytics-dimension-repository_id" content="62343362" /><meta name="octolytics-dimension-repository_nwo" content="jfischer/micropython-tsl2591" /><meta name="octolytics-dimension-repository_public" content="true" /><meta name="octolytics-dimension-repository_is_fork" content="true" /><meta name="octolytics-dimension-repository_parent_id" content="35221230" /><meta name="octolytics-dimension-repository_parent_nwo" content="maxlklaxl/python-tsl2591" /><meta name="octolytics-dimension-repository_network_root_id" content="35221230" /><meta name="octolytics-dimension-repository_network_root_nwo" content="maxlklaxl/python-tsl2591" />



  <meta name="turbo-body-classes" content="logged-out env-production page-responsive">


  <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">

  <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">

  <meta name="browser-optimizely-client-errors-url" content="https://api.github.com/_private/browser/optimizely_client/errors">

  <link rel="mask-icon" href="https://github.githubassets.com/assets/pinned-octocat-093da3e6fa40.svg" color="#000000">
  <link rel="alternate icon" class="js-site-favicon" type="image/png" href="https://github.githubassets.com/favicons/favicon.png">
  <link rel="icon" class="js-site-favicon" type="image/svg+xml" href="https://github.githubassets.com/favicons/favicon.svg">

<meta name="theme-color" content="#1e2327">
<meta name="color-scheme" content="light dark" />


  <link rel="manifest" href="/manifest.json" crossOrigin="use-credentials">

  </head>

  <body class="logged-out env-production page-responsive" style="word-wrap: break-word;">
    <div data-turbo-body class="logged-out env-production page-responsive" style="word-wrap: break-word;">
      


    <div class="position-relative js-header-wrapper ">
      <a href="#start-of-content" class="px-2 py-4 color-bg-accent-emphasis color-fg-on-emphasis show-on-focus js-skip-to-content">Skip to content</a>
      <span data-view-component="true" class="progress-pjax-loader Progress position-fixed width-full">
    <span style="width: 0%;" data-view-component="true" class="Progress-item progress-pjax-loader-bar left-0 top-0 color-bg-accent-emphasis"></span>
</span>      
      
  




<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_lib-esm_Button_IconButton_js-node_modules_primer_react_lib--23bcad-d7f33099bdde.js"></script>

<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/keyboard-shortcuts-dialog-1a0f5528b004.js"></script>

<react-partial
  partial-name="keyboard-shortcuts-dialog"
  data-ssr="false"
>
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{}}</script>
  <div data-target="react-partial.reactRoot"></div>
</react-partial>



      

        

            

<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_github_remote-form_dist_index_js-node_modules_delegated-events_dist_inde-94fd67-99519581d0f8.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/sessions-1164ee5f3e37.js"></script>
<header class="Header-old header-logged-out js-details-container Details position-relative f4 py-3" role="banner" data-color-mode=light data-light-theme=light data-dark-theme=dark>
  <button type="button" class="Header-backdrop d-lg-none border-0 position-fixed top-0 left-0 width-full height-full js-details-target" aria-label="Toggle navigation">
    <span class="d-none">Toggle navigation</span>
  </button>

  <div class=" d-flex flex-column flex-lg-row flex-items-center p-responsive height-full position-relative z-1">
    <div class="d-flex flex-justify-between flex-items-center width-full width-lg-auto">
      <a class="mr-lg-3 color-fg-inherit flex-order-2" href="https://github.com/" aria-label="Homepage" data-ga-click="(Logged out) Header, go to homepage, icon:logo-wordmark">
        <svg height="32" aria-hidden="true" viewBox="0 0 16 16" version="1.1" width="32" data-view-component="true" class="octicon octicon-mark-github">
    <path d="M8 0c4.42 0 8 3.58 8 8a8.013 8.013 0 0 1-5.45 7.59c-.4.08-.55-.17-.55-.38 0-.27.01-1.13.01-2.2 0-.75-.25-1.23-.54-1.48 1.78-.2 3.65-.88 3.65-3.95 0-.88-.31-1.59-.82-2.15.08-.2.36-1.02-.08-2.12 0 0-.67-.22-2.2.82-.64-.18-1.32-.27-2-.27-.68 0-1.36.09-2 .27-1.53-1.03-2.2-.82-2.2-.82-.44 1.1-.16 1.92-.08 2.12-.51.56-.82 1.28-.82 2.15 0 3.06 1.86 3.75 3.64 3.95-.23.2-.44.55-.51 1.07-.46.21-1.61.55-2.33-.66-.15-.24-.6-.83-1.23-.82-.67.01-.27.38.01.53.34.19.73.9.82 1.13.16.45.68 1.31 2.69.94 0 .67.01 1.3.01 1.49 0 .21-.15.45-.55.38A7.995 7.995 0 0 1 0 8c0-4.42 3.58-8 8-8Z"></path>
</svg>
      </a>

      <div class="flex-1">
        <a href="/login?return_to=https%3A%2F%2Fgithub.com%2Fjfischer%2Fmicropython-tsl2591%2Fblob%2Fmaster%2Ftsl2591.py"
          class="d-inline-block d-lg-none flex-order-1 f5 no-underline border color-border-default rounded-2 px-2 py-1 color-fg-inherit"
          data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;site header menu&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;SIGN_UP&quot;,&quot;originating_url&quot;:&quot;https://github.com/jfischer/micropython-tsl2591/blob/master/tsl2591.py&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="b57cb1f9e4436a3be5596c2fbe2a5c33e9d0ee0e2211017a7816ccf0adf7e958"
          data-ga-click="(Logged out) Header, clicked Sign in, text:sign-in">
          Sign in
        </a>
      </div>

      <div class="flex-1 flex-order-2 text-right">
        <button aria-label="Toggle navigation" aria-expanded="false" type="button" data-view-component="true" class="js-details-target Button--link Button--medium Button d-lg-none color-fg-inherit p-1">  <span class="Button-content">
    <span class="Button-label"><div class="HeaderMenu-toggle-bar rounded my-1"></div>
            <div class="HeaderMenu-toggle-bar rounded my-1"></div>
            <div class="HeaderMenu-toggle-bar rounded my-1"></div></span>
  </span>
</button>
      </div>
    </div>


    <div class="HeaderMenu--logged-out p-responsive height-fit position-lg-relative d-lg-flex flex-column flex-auto pt-7 pb-4 top-0">
      <div class="header-menu-wrapper d-flex flex-column flex-self-end flex-lg-row flex-justify-between flex-auto p-3 p-lg-0 rounded rounded-lg-0 mt-3 mt-lg-0">
          <nav class="mt-0 px-3 px-lg-0 mb-3 mb-lg-0" aria-label="Global">
            <ul class="d-lg-flex list-style-none">
                <li class="HeaderMenu-item position-relative flex-wrap flex-justify-between flex-items-center d-block d-lg-flex flex-lg-nowrap flex-lg-items-center js-details-container js-header-menu-item">
      <button type="button" class="HeaderMenu-link border-0 width-full width-lg-auto px-0 px-lg-2 py-3 py-lg-2 no-wrap d-flex flex-items-center flex-justify-between js-details-target" aria-expanded="false">
        Product
        <svg opacity="0.5" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-chevron-down HeaderMenu-icon ml-1">
    <path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path>
</svg>
      </button>
      <div class="HeaderMenu-dropdown dropdown-menu rounded m-0 p-0 py-2 py-lg-4 position-relative position-lg-absolute left-0 left-lg-n3 d-lg-flex dropdown-menu-wide">
          <div class="px-lg-4 border-lg-right mb-4 mb-lg-0 pr-lg-7">
            <ul class="list-style-none f5" >
                <li>
  <a class="HeaderMenu-dropdown-link lh-condensed d-block no-underline position-relative py-2 Link--secondary d-flex flex-items-center pb-lg-3" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Product&quot;,&quot;action&quot;:&quot;click to go to Actions&quot;,&quot;label&quot;:&quot;ref_cta:Actions;&quot;}" href="/features/actions">
      <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-workflow color-fg-subtle mr-3">
    <path d="M1 3a2 2 0 0 1 2-2h6.5a2 2 0 0 1 2 2v6.5a2 2 0 0 1-2 2H7v4.063C7 16.355 7.644 17 8.438 17H12.5v-2.5a2 2 0 0 1 2-2H21a2 2 0 0 1 2 2V21a2 2 0 0 1-2 2h-6.5a2 2 0 0 1-2-2v-2.5H8.437A2.939 2.939 0 0 1 5.5 15.562V11.5H3a2 2 0 0 1-2-2Zm2-.5a.5.5 0 0 0-.5.5v6.5a.5.5 0 0 0 .5.5h6.5a.5.5 0 0 0 .5-.5V3a.5.5 0 0 0-.5-.5ZM14.5 14a.5.5 0 0 0-.5.5V21a.5.5 0 0 0 .5.5H21a.5.5 0 0 0 .5-.5v-6.5a.5.5 0 0 0-.5-.5Z"></path>
</svg>
      <div>
        <div class="color-fg-default h4">Actions</div>
        Automate any workflow
      </div>

    
</a></li>

                <li>
  <a class="HeaderMenu-dropdown-link lh-condensed d-block no-underline position-relative py-2 Link--secondary d-flex flex-items-center pb-lg-3" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Product&quot;,&quot;action&quot;:&quot;click to go to Packages&quot;,&quot;label&quot;:&quot;ref_cta:Packages;&quot;}" href="/features/packages">
      <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-package color-fg-subtle mr-3">
    <path d="M12.876.64V.639l8.25 4.763c.541.313.875.89.875 1.515v9.525a1.75 1.75 0 0 1-.875 1.516l-8.25 4.762a1.748 1.748 0 0 1-1.75 0l-8.25-4.763a1.75 1.75 0 0 1-.875-1.515V6.917c0-.625.334-1.202.875-1.515L11.126.64a1.748 1.748 0 0 1 1.75 0Zm-1 1.298L4.251 6.34l7.75 4.474 7.75-4.474-7.625-4.402a.248.248 0 0 0-.25 0Zm.875 19.123 7.625-4.402a.25.25 0 0 0 .125-.216V7.639l-7.75 4.474ZM3.501 7.64v8.803c0 .09.048.172.125.216l7.625 4.402v-8.947Z"></path>
</svg>
      <div>
        <div class="color-fg-default h4">Packages</div>
        Host and manage packages
      </div>

    
</a></li>

                <li>
  <a class="HeaderMenu-dropdown-link lh-condensed d-block no-underline position-relative py-2 Link--secondary d-flex flex-items-center pb-lg-3" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Product&quot;,&quot;action&quot;:&quot;click to go to Security&quot;,&quot;label&quot;:&quot;ref_cta:Security;&quot;}" href="/features/security">
      <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-shield-check color-fg-subtle mr-3">
    <path d="M16.53 9.78a.75.75 0 0 0-1.06-1.06L11 13.19l-1.97-1.97a.75.75 0 0 0-1.06 1.06l2.5 2.5a.75.75 0 0 0 1.06 0l5-5Z"></path><path d="m12.54.637 8.25 2.675A1.75 1.75 0 0 1 22 4.976V10c0 6.19-3.771 10.704-9.401 12.83a1.704 1.704 0 0 1-1.198 0C5.77 20.705 2 16.19 2 10V4.976c0-.758.489-1.43 1.21-1.664L11.46.637a1.748 1.748 0 0 1 1.08 0Zm-.617 1.426-8.25 2.676a.249.249 0 0 0-.173.237V10c0 5.46 3.28 9.483 8.43 11.426a.199.199 0 0 0 .14 0C17.22 19.483 20.5 15.461 20.5 10V4.976a.25.25 0 0 0-.173-.237l-8.25-2.676a.253.253 0 0 0-.154 0Z"></path>
</svg>
      <div>
        <div class="color-fg-default h4">Security</div>
        Find and fix vulnerabilities
      </div>

    
</a></li>

                <li>
  <a class="HeaderMenu-dropdown-link lh-condensed d-block no-underline position-relative py-2 Link--secondary d-flex flex-items-center pb-lg-3" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Product&quot;,&quot;action&quot;:&quot;click to go to Codespaces&quot;,&quot;label&quot;:&quot;ref_cta:Codespaces;&quot;}" href="/features/codespaces">
      <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-codespaces color-fg-subtle mr-3">
    <path d="M3.5 3.75C3.5 2.784 4.284 2 5.25 2h13.5c.966 0 1.75.784 1.75 1.75v7.5A1.75 1.75 0 0 1 18.75 13H5.25a1.75 1.75 0 0 1-1.75-1.75Zm-2 12c0-.966.784-1.75 1.75-1.75h17.5c.966 0 1.75.784 1.75 1.75v4a1.75 1.75 0 0 1-1.75 1.75H3.25a1.75 1.75 0 0 1-1.75-1.75ZM5.25 3.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h13.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Zm-2 12a.25.25 0 0 0-.25.25v4c0 .138.112.25.25.25h17.5a.25.25 0 0 0 .25-.25v-4a.25.25 0 0 0-.25-.25Z"></path><path d="M10 17.75a.75.75 0 0 1 .75-.75h6.5a.75.75 0 0 1 0 1.5h-6.5a.75.75 0 0 1-.75-.75Zm-4 0a.75.75 0 0 1 .75-.75h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1-.75-.75Z"></path>
</svg>
      <div>
        <div class="color-fg-default h4">Codespaces</div>
        Instant dev environments
      </div>

    
</a></li>

                <li>
  <a class="HeaderMenu-dropdown-link lh-condensed d-block no-underline position-relative py-2 Link--secondary d-flex flex-items-center pb-lg-3" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Product&quot;,&quot;action&quot;:&quot;click to go to Copilot&quot;,&quot;label&quot;:&quot;ref_cta:Copilot;&quot;}" href="/features/copilot">
      <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-copilot color-fg-subtle mr-3">
    <path d="M23.922 16.992c-.861 1.495-5.859 5.023-11.922 5.023-6.063 0-11.061-3.528-11.922-5.023A.641.641 0 0 1 0 16.736v-2.869a.841.841 0 0 1 .053-.22c.372-.935 1.347-2.292 2.605-2.656.167-.429.414-1.055.644-1.517a10.195 10.195 0 0 1-.052-1.086c0-1.331.282-2.499 1.132-3.368.397-.406.89-.717 1.474-.952 1.399-1.136 3.392-2.093 6.122-2.093 2.731 0 4.767.957 6.166 2.093.584.235 1.077.546 1.474.952.85.869 1.132 2.037 1.132 3.368 0 .368-.014.733-.052 1.086.23.462.477 1.088.644 1.517 1.258.364 2.233 1.721 2.605 2.656a.832.832 0 0 1 .053.22v2.869a.641.641 0 0 1-.078.256ZM12.172 11h-.344a4.323 4.323 0 0 1-.355.508C10.703 12.455 9.555 13 7.965 13c-1.725 0-2.989-.359-3.782-1.259a2.005 2.005 0 0 1-.085-.104L4 11.741v6.585c1.435.779 4.514 2.179 8 2.179 3.486 0 6.565-1.4 8-2.179v-6.585l-.098-.104s-.033.045-.085.104c-.793.9-2.057 1.259-3.782 1.259-1.59 0-2.738-.545-3.508-1.492a4.323 4.323 0 0 1-.355-.508h-.016.016Zm.641-2.935c.136 1.057.403 1.913.878 2.497.442.544 1.134.938 2.344.938 1.573 0 2.292-.337 2.657-.751.384-.435.558-1.15.558-2.361 0-1.14-.243-1.847-.705-2.319-.477-.488-1.319-.862-2.824-1.025-1.487-.161-2.192.138-2.533.529-.269.307-.437.808-.438 1.578v.021c0 .265.021.562.063.893Zm-1.626 0c.042-.331.063-.628.063-.894v-.02c-.001-.77-.169-1.271-.438-1.578-.341-.391-1.046-.69-2.533-.529-1.505.163-2.347.537-2.824 1.025-.462.472-.705 1.179-.705 2.319 0 1.211.175 1.926.558 2.361.365.414 1.084.751 2.657.751 1.21 0 1.902-.394 2.344-.938.475-.584.742-1.44.878-2.497Z"></path><path d="M14.5 14.25a1 1 0 0 1 1 1v2a1 1 0 0 1-2 0v-2a1 1 0 0 1 1-1Zm-5 0a1 1 0 0 1 1 1v2a1 1 0 0 1-2 0v-2a1 1 0 0 1 1-1Z"></path>
</svg>
      <div>
        <div class="color-fg-default h4">Copilot</div>
        Write better code with AI
      </div>

    
</a></li>

                <li>
  <a class="HeaderMenu-dropdown-link lh-condensed d-block no-underline position-relative py-2 Link--secondary d-flex flex-items-center pb-lg-3" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Product&quot;,&quot;action&quot;:&quot;click to go to Code review&quot;,&quot;label&quot;:&quot;ref_cta:Code review;&quot;}" href="/features/code-review">
      <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-code-review color-fg-subtle mr-3">
    <path d="M10.3 6.74a.75.75 0 0 1-.04 1.06l-2.908 2.7 2.908 2.7a.75.75 0 1 1-1.02 1.1l-3.5-3.25a.75.75 0 0 1 0-1.1l3.5-3.25a.75.75 0 0 1 1.06.04Zm3.44 1.06a.75.75 0 1 1 1.02-1.1l3.5 3.25a.75.75 0 0 1 0 1.1l-3.5 3.25a.75.75 0 1 1-1.02-1.1l2.908-2.7-2.908-2.7Z"></path><path d="M1.5 4.25c0-.966.784-1.75 1.75-1.75h17.5c.966 0 1.75.784 1.75 1.75v12.5a1.75 1.75 0 0 1-1.75 1.75h-9.69l-3.573 3.573A1.458 1.458 0 0 1 5 21.043V18.5H3.25a1.75 1.75 0 0 1-1.75-1.75ZM3.25 4a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h2.5a.75.75 0 0 1 .75.75v3.19l3.72-3.72a.749.749 0 0 1 .53-.22h10a.25.25 0 0 0 .25-.25V4.25a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <div>
        <div class="color-fg-default h4">Code review</div>
        Manage code changes
      </div>

    
</a></li>

                <li>
  <a class="HeaderMenu-dropdown-link lh-condensed d-block no-underline position-relative py-2 Link--secondary d-flex flex-items-center pb-lg-3" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Product&quot;,&quot;action&quot;:&quot;click to go to Issues&quot;,&quot;label&quot;:&quot;ref_cta:Issues;&quot;}" href="/features/issues">
      <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-issue-opened color-fg-subtle mr-3">
    <path d="M12 1c6.075 0 11 4.925 11 11s-4.925 11-11 11S1 18.075 1 12 5.925 1 12 1ZM2.5 12a9.5 9.5 0 0 0 9.5 9.5 9.5 9.5 0 0 0 9.5-9.5A9.5 9.5 0 0 0 12 2.5 9.5 9.5 0 0 0 2.5 12Zm9.5 2a2 2 0 1 1-.001-3.999A2 2 0 0 1 12 14Z"></path>
</svg>
      <div>
        <div class="color-fg-default h4">Issues</div>
        Plan and track work
      </div>

    
</a></li>

                <li>
  <a class="HeaderMenu-dropdown-link lh-condensed d-block no-underline position-relative py-2 Link--secondary d-flex flex-items-center" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Product&quot;,&quot;action&quot;:&quot;click to go to Discussions&quot;,&quot;label&quot;:&quot;ref_cta:Discussions;&quot;}" href="/features/discussions">
      <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-comment-discussion color-fg-subtle mr-3">
    <path d="M1.75 1h12.5c.966 0 1.75.784 1.75 1.75v9.5A1.75 1.75 0 0 1 14.25 14H8.061l-2.574 2.573A1.458 1.458 0 0 1 3 15.543V14H1.75A1.75 1.75 0 0 1 0 12.25v-9.5C0 1.784.784 1 1.75 1ZM1.5 2.75v9.5c0 .138.112.25.25.25h2a.75.75 0 0 1 .75.75v2.19l2.72-2.72a.749.749 0 0 1 .53-.22h6.5a.25.25 0 0 0 .25-.25v-9.5a.25.25 0 0 0-.25-.25H1.75a.25.25 0 0 0-.25.25Z"></path><path d="M22.5 8.75a.25.25 0 0 0-.25-.25h-3.5a.75.75 0 0 1 0-1.5h3.5c.966 0 1.75.784 1.75 1.75v9.5A1.75 1.75 0 0 1 22.25 20H21v1.543a1.457 1.457 0 0 1-2.487 1.03L15.939 20H10.75A1.75 1.75 0 0 1 9 18.25v-1.465a.75.75 0 0 1 1.5 0v1.465c0 .138.112.25.25.25h5.5a.75.75 0 0 1 .53.22l2.72 2.72v-2.19a.75.75 0 0 1 .75-.75h2a.25.25 0 0 0 .25-.25v-9.5Z"></path>
</svg>
      <div>
        <div class="color-fg-default h4">Discussions</div>
        Collaborate outside of code
      </div>

    
</a></li>

            </ul>
          </div>
          <div class="px-lg-4">
              <span class="d-block h4 color-fg-default my-1" id="product-explore-heading">Explore</span>
            <ul class="list-style-none f5" aria-labelledby="product-explore-heading">
                <li>
  <a class="HeaderMenu-dropdown-link lh-condensed d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Product&quot;,&quot;action&quot;:&quot;click to go to All features&quot;,&quot;label&quot;:&quot;ref_cta:All features;&quot;}" href="/features">
      All features

    
</a></li>

                <li>
  <a class="HeaderMenu-dropdown-link lh-condensed d-block no-underline position-relative py-2 Link--secondary" target="_blank" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Product&quot;,&quot;action&quot;:&quot;click to go to Documentation&quot;,&quot;label&quot;:&quot;ref_cta:Documentation;&quot;}" href="https://docs.github.com">
      Documentation

    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-link-external HeaderMenu-external-icon color-fg-subtle">
    <path d="M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-3.5a.75.75 0 0 1 1.5 0v3.5A1.75 1.75 0 0 1 12.25 14h-8.5A1.75 1.75 0 0 1 2 12.25v-8.5C2 2.784 2.784 2 3.75 2Zm6.854-1h4.146a.25.25 0 0 1 .25.25v4.146a.25.25 0 0 1-.427.177L13.03 4.03 9.28 7.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.75-3.75-1.543-1.543A.25.25 0 0 1 10.604 1Z"></path>
</svg>
</a></li>

                <li>
  <a class="HeaderMenu-dropdown-link lh-condensed d-block no-underline position-relative py-2 Link--secondary" target="_blank" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Product&quot;,&quot;action&quot;:&quot;click to go to GitHub Skills&quot;,&quot;label&quot;:&quot;ref_cta:GitHub Skills;&quot;}" href="https://skills.github.com/">
      GitHub Skills

    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-link-external HeaderMenu-external-icon color-fg-subtle">
    <path d="M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-3.5a.75.75 0 0 1 1.5 0v3.5A1.75 1.75 0 0 1 12.25 14h-8.5A1.75 1.75 0 0 1 2 12.25v-8.5C2 2.784 2.784 2 3.75 2Zm6.854-1h4.146a.25.25 0 0 1 .25.25v4.146a.25.25 0 0 1-.427.177L13.03 4.03 9.28 7.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.75-3.75-1.543-1.543A.25.25 0 0 1 10.604 1Z"></path>
</svg>
</a></li>

                <li>
  <a class="HeaderMenu-dropdown-link lh-condensed d-block no-underline position-relative py-2 Link--secondary" target="_blank" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Product&quot;,&quot;action&quot;:&quot;click to go to Blog&quot;,&quot;label&quot;:&quot;ref_cta:Blog;&quot;}" href="https://github.blog">
      Blog

    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-link-external HeaderMenu-external-icon color-fg-subtle">
    <path d="M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-3.5a.75.75 0 0 1 1.5 0v3.5A1.75 1.75 0 0 1 12.25 14h-8.5A1.75 1.75 0 0 1 2 12.25v-8.5C2 2.784 2.784 2 3.75 2Zm6.854-1h4.146a.25.25 0 0 1 .25.25v4.146a.25.25 0 0 1-.427.177L13.03 4.03 9.28 7.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.75-3.75-1.543-1.543A.25.25 0 0 1 10.604 1Z"></path>
</svg>
</a></li>

            </ul>
          </div>
      </div>
</li>


                <li class="HeaderMenu-item position-relative flex-wrap flex-justify-between flex-items-center d-block d-lg-flex flex-lg-nowrap flex-lg-items-center js-details-container js-header-menu-item">
      <button type="button" class="HeaderMenu-link border-0 width-full width-lg-auto px-0 px-lg-2 py-3 py-lg-2 no-wrap d-flex flex-items-center flex-justify-between js-details-target" aria-expanded="false">
        Solutions
        <svg opacity="0.5" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-chevron-down HeaderMenu-icon ml-1">
    <path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path>
</svg>
      </button>
      <div class="HeaderMenu-dropdown dropdown-menu rounded m-0 p-0 py-2 py-lg-4 position-relative position-lg-absolute left-0 left-lg-n3 px-lg-4">
          <div class="border-bottom pb-3 mb-3">
              <span class="d-block h4 color-fg-default my-1" id="solutions-for-heading">For</span>
            <ul class="list-style-none f5" aria-labelledby="solutions-for-heading">
                <li>
  <a class="HeaderMenu-dropdown-link lh-condensed d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Solutions&quot;,&quot;action&quot;:&quot;click to go to Enterprise&quot;,&quot;label&quot;:&quot;ref_cta:Enterprise;&quot;}" href="/enterprise">
      Enterprise

    
</a></li>

                <li>
  <a class="HeaderMenu-dropdown-link lh-condensed d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Solutions&quot;,&quot;action&quot;:&quot;click to go to Teams&quot;,&quot;label&quot;:&quot;ref_cta:Teams;&quot;}" href="/team">
      Teams

    
</a></li>

                <li>
  <a class="HeaderMenu-dropdown-link lh-condensed d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Solutions&quot;,&quot;action&quot;:&quot;click to go to Startups&quot;,&quot;label&quot;:&quot;ref_cta:Startups;&quot;}" href="/enterprise/startups">
      Startups

    
</a></li>

                <li>
  <a class="HeaderMenu-dropdown-link lh-condensed d-block no-underline position-relative py-2 Link--secondary" target="_blank" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Solutions&quot;,&quot;action&quot;:&quot;click to go to Education&quot;,&quot;label&quot;:&quot;ref_cta:Education;&quot;}" href="https://education.github.com">
      Education

    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-link-external HeaderMenu-external-icon color-fg-subtle">
    <path d="M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-3.5a.75.75 0 0 1 1.5 0v3.5A1.75 1.75 0 0 1 12.25 14h-8.5A1.75 1.75 0 0 1 2 12.25v-8.5C2 2.784 2.784 2 3.75 2Zm6.854-1h4.146a.25.25 0 0 1 .25.25v4.146a.25.25 0 0 1-.427.177L13.03 4.03 9.28 7.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.75-3.75-1.543-1.543A.25.25 0 0 1 10.604 1Z"></path>
</svg>
</a></li>

            </ul>
          </div>
          <div class="border-bottom pb-3 mb-3">
              <span class="d-block h4 color-fg-default my-1" id="solutions-by-solution-heading">By Solution</span>
            <ul class="list-style-none f5" aria-labelledby="solutions-by-solution-heading">
                <li>
  <a class="HeaderMenu-dropdown-link lh-condensed d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Solutions&quot;,&quot;action&quot;:&quot;click to go to CI/CD &amp;amp; Automation&quot;,&quot;label&quot;:&quot;ref_cta:CI/CD &amp;amp; Automation;&quot;}" href="/solutions/ci-cd/">
      CI/CD &amp; Automation

    
</a></li>

                <li>
  <a class="HeaderMenu-dropdown-link lh-condensed d-block no-underline position-relative py-2 Link--secondary" target="_blank" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Solutions&quot;,&quot;action&quot;:&quot;click to go to DevOps&quot;,&quot;label&quot;:&quot;ref_cta:DevOps;&quot;}" href="https://resources.github.com/devops/">
      DevOps

    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-link-external HeaderMenu-external-icon color-fg-subtle">
    <path d="M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-3.5a.75.75 0 0 1 1.5 0v3.5A1.75 1.75 0 0 1 12.25 14h-8.5A1.75 1.75 0 0 1 2 12.25v-8.5C2 2.784 2.784 2 3.75 2Zm6.854-1h4.146a.25.25 0 0 1 .25.25v4.146a.25.25 0 0 1-.427.177L13.03 4.03 9.28 7.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.75-3.75-1.543-1.543A.25.25 0 0 1 10.604 1Z"></path>
</svg>
</a></li>

                <li>
  <a class="HeaderMenu-dropdown-link lh-condensed d-block no-underline position-relative py-2 Link--secondary" target="_blank" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Solutions&quot;,&quot;action&quot;:&quot;click to go to DevSecOps&quot;,&quot;label&quot;:&quot;ref_cta:DevSecOps;&quot;}" href="https://resources.github.com/devops/fundamentals/devsecops/">
      DevSecOps

    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-link-external HeaderMenu-external-icon color-fg-subtle">
    <path d="M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-3.5a.75.75 0 0 1 1.5 0v3.5A1.75 1.75 0 0 1 12.25 14h-8.5A1.75 1.75 0 0 1 2 12.25v-8.5C2 2.784 2.784 2 3.75 2Zm6.854-1h4.146a.25.25 0 0 1 .25.25v4.146a.25.25 0 0 1-.427.177L13.03 4.03 9.28 7.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.75-3.75-1.543-1.543A.25.25 0 0 1 10.604 1Z"></path>
</svg>
</a></li>

            </ul>
          </div>
          <div class="">
              <span class="d-block h4 color-fg-default my-1" id="solutions-resources-heading">Resources</span>
            <ul class="list-style-none f5" aria-labelledby="solutions-resources-heading">
                <li>
  <a class="HeaderMenu-dropdown-link lh-condensed d-block no-underline position-relative py-2 Link--secondary" target="_blank" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Solutions&quot;,&quot;action&quot;:&quot;click to go to Learning Pathways&quot;,&quot;label&quot;:&quot;ref_cta:Learning Pathways;&quot;}" href="https://resources.github.com/learn/pathways/">
      Learning Pathways

    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-link-external HeaderMenu-external-icon color-fg-subtle">
    <path d="M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-3.5a.75.75 0 0 1 1.5 0v3.5A1.75 1.75 0 0 1 12.25 14h-8.5A1.75 1.75 0 0 1 2 12.25v-8.5C2 2.784 2.784 2 3.75 2Zm6.854-1h4.146a.25.25 0 0 1 .25.25v4.146a.25.25 0 0 1-.427.177L13.03 4.03 9.28 7.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.75-3.75-1.543-1.543A.25.25 0 0 1 10.604 1Z"></path>
</svg>
</a></li>

                <li>
  <a class="HeaderMenu-dropdown-link lh-condensed d-block no-underline position-relative py-2 Link--secondary" target="_blank" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Solutions&quot;,&quot;action&quot;:&quot;click to go to White papers, Ebooks, Webinars&quot;,&quot;label&quot;:&quot;ref_cta:White papers, Ebooks, Webinars;&quot;}" href="https://resources.github.com/">
      White papers, Ebooks, Webinars

    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-link-external HeaderMenu-external-icon color-fg-subtle">
    <path d="M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-3.5a.75.75 0 0 1 1.5 0v3.5A1.75 1.75 0 0 1 12.25 14h-8.5A1.75 1.75 0 0 1 2 12.25v-8.5C2 2.784 2.784 2 3.75 2Zm6.854-1h4.146a.25.25 0 0 1 .25.25v4.146a.25.25 0 0 1-.427.177L13.03 4.03 9.28 7.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.75-3.75-1.543-1.543A.25.25 0 0 1 10.604 1Z"></path>
</svg>
</a></li>

                <li>
  <a class="HeaderMenu-dropdown-link lh-condensed d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Solutions&quot;,&quot;action&quot;:&quot;click to go to Customer Stories&quot;,&quot;label&quot;:&quot;ref_cta:Customer Stories;&quot;}" href="/customer-stories">
      Customer Stories

    
</a></li>

                <li>
  <a class="HeaderMenu-dropdown-link lh-condensed d-block no-underline position-relative py-2 Link--secondary" target="_blank" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Solutions&quot;,&quot;action&quot;:&quot;click to go to Partners&quot;,&quot;label&quot;:&quot;ref_cta:Partners;&quot;}" href="https://partner.github.com/">
      Partners

    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-link-external HeaderMenu-external-icon color-fg-subtle">
    <path d="M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-3.5a.75.75 0 0 1 1.5 0v3.5A1.75 1.75 0 0 1 12.25 14h-8.5A1.75 1.75 0 0 1 2 12.25v-8.5C2 2.784 2.784 2 3.75 2Zm6.854-1h4.146a.25.25 0 0 1 .25.25v4.146a.25.25 0 0 1-.427.177L13.03 4.03 9.28 7.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.75-3.75-1.543-1.543A.25.25 0 0 1 10.604 1Z"></path>
</svg>
</a></li>

            </ul>
          </div>
      </div>
</li>


                <li class="HeaderMenu-item position-relative flex-wrap flex-justify-between flex-items-center d-block d-lg-flex flex-lg-nowrap flex-lg-items-center js-details-container js-header-menu-item">
      <button type="button" class="HeaderMenu-link border-0 width-full width-lg-auto px-0 px-lg-2 py-3 py-lg-2 no-wrap d-flex flex-items-center flex-justify-between js-details-target" aria-expanded="false">
        Open Source
        <svg opacity="0.5" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-chevron-down HeaderMenu-icon ml-1">
    <path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path>
</svg>
      </button>
      <div class="HeaderMenu-dropdown dropdown-menu rounded m-0 p-0 py-2 py-lg-4 position-relative position-lg-absolute left-0 left-lg-n3 px-lg-4">
          <div class="border-bottom pb-3 mb-3">
            <ul class="list-style-none f5" >
                <li>
  <a class="HeaderMenu-dropdown-link lh-condensed d-block no-underline position-relative py-2 Link--secondary d-flex flex-items-center" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Open Source&quot;,&quot;action&quot;:&quot;click to go to GitHub Sponsors&quot;,&quot;label&quot;:&quot;ref_cta:GitHub Sponsors;&quot;}" href="/sponsors">
      
      <div>
        <div class="color-fg-default h4">GitHub Sponsors</div>
        Fund open source developers
      </div>

    
</a></li>

            </ul>
          </div>
          <div class="border-bottom pb-3 mb-3">
            <ul class="list-style-none f5" >
                <li>
  <a class="HeaderMenu-dropdown-link lh-condensed d-block no-underline position-relative py-2 Link--secondary d-flex flex-items-center" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Open Source&quot;,&quot;action&quot;:&quot;click to go to The ReadME Project&quot;,&quot;label&quot;:&quot;ref_cta:The ReadME Project;&quot;}" href="/readme">
      
      <div>
        <div class="color-fg-default h4">The ReadME Project</div>
        GitHub community articles
      </div>

    
</a></li>

            </ul>
          </div>
          <div class="">
              <span class="d-block h4 color-fg-default my-1" id="open-source-repositories-heading">Repositories</span>
            <ul class="list-style-none f5" aria-labelledby="open-source-repositories-heading">
                <li>
  <a class="HeaderMenu-dropdown-link lh-condensed d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Open Source&quot;,&quot;action&quot;:&quot;click to go to Topics&quot;,&quot;label&quot;:&quot;ref_cta:Topics;&quot;}" href="/topics">
      Topics

    
</a></li>

                <li>
  <a class="HeaderMenu-dropdown-link lh-condensed d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Open Source&quot;,&quot;action&quot;:&quot;click to go to Trending&quot;,&quot;label&quot;:&quot;ref_cta:Trending;&quot;}" href="/trending">
      Trending

    
</a></li>

                <li>
  <a class="HeaderMenu-dropdown-link lh-condensed d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Open Source&quot;,&quot;action&quot;:&quot;click to go to Collections&quot;,&quot;label&quot;:&quot;ref_cta:Collections;&quot;}" href="/collections">
      Collections

    
</a></li>

            </ul>
          </div>
      </div>
</li>


                <li class="HeaderMenu-item position-relative flex-wrap flex-justify-between flex-items-center d-block d-lg-flex flex-lg-nowrap flex-lg-items-center js-details-container js-header-menu-item">
    <a class="HeaderMenu-link no-underline px-0 px-lg-2 py-3 py-lg-2 d-block d-lg-inline-block" data-analytics-event="{&quot;category&quot;:&quot;Header menu top item (logged out)&quot;,&quot;action&quot;:&quot;click to go to Pricing&quot;,&quot;label&quot;:&quot;ref_cta:Pricing;&quot;}" href="/pricing">Pricing</a>
</li>

            </ul>
          </nav>

        <div class="d-lg-flex flex-items-center mb-3 mb-lg-0 text-center text-lg-left ml-3" style="">
                


<qbsearch-input class="search-input" data-scope="repo:jfischer/micropython-tsl2591" data-custom-scopes-path="/search/custom_scopes" data-delete-custom-scopes-csrf="F4C8y6mfirIkFVYbM3jGCkIWvoM9Mj4n4IhDahy_fSz6-WfwsS7GMaNTPvEnQ-EUzV-CEmTjlgC-9iOgTNBIHQ" data-max-custom-scopes="10" data-header-redesign-enabled="false" data-initial-value="" data-blackbird-suggestions-path="/search/suggestions" data-jump-to-suggestions-path="/_graphql/GetSuggestedNavigationDestinations" data-current-repository="jfischer/micropython-tsl2591" data-current-org="" data-current-owner="jfischer" data-logged-in="false" data-copilot-chat-enabled="false" data-blackbird-indexed-repo-csrf="<esi:include src=&quot;/_esi/rails_csrf_token_form_hidden?r=hWN6OVHyLine61pYxGatY86yZ8fc7wuYoPd%2B7K1lak%2B5HBCYt0aNYWr4c6mdGq5C%2FI4wZE5KJoJy6%2BzZsmC%2B1JgPfAudwnFYZmZdTX8GRFMyF0jqWFh5m4FHAbP6ITxaLnsc0o%2BcU2ULfUK%2BoQPADTbzbKMB%2FEo821EQ1L0MLBOPqR4F1p96wGqbHxaoYcVMBC10bEtgoMCqotvtQ7Od5RF8l8E6JqnuX%2FRwBUSexuLgkIqmyVdQzj%2FT8TJ8K8G9s0hnbnm%2FDwVxXabdg0bUv4pNopqx0MJWk2CCPZQ%2FkKbroYvuO0k11u59Ufzfb04LiThZImfmtErtjhzpvWlBKW%2FrLDrFv5wsxkMB2haesAfY8C63YanSPfBHz6evg7qut5UF%2Bi%2B2pETKxi9LS%2BudhplnblIIoGiaa1oDoPe33RVJaz6GUzV9axdAgOn21U%2FRYWNM1r3JJsGXIBcedaM6f0PccAjEAVRhYcM6gaZFKM4pL1pck7naFoDqChMjoHj%2FmNYfNpdCBfS%2FaEkuPbXV%2FRcZ3Gf7F0sGrrVD5ekZeRqa%2BsC%2F7l53%2BDpOOkL6%2Fwc2TEFR6K8m343qgg%3D%3D--NmvIk%2FhE05qnpfhV--n3NH6d4ztZtjkAS4YOU42w%3D%3D&quot; />">
  <div
    class="search-input-container search-with-dialog position-relative d-flex flex-row flex-items-center mr-4 rounded"
    data-action="click:qbsearch-input#searchInputContainerClicked"
  >
      <button
        type="button"
        class="header-search-button placeholder  input-button form-control d-flex flex-1 flex-self-stretch flex-items-center no-wrap width-full py-0 pl-2 pr-0 text-left border-0 box-shadow-none"
        data-target="qbsearch-input.inputButton"
        placeholder="Search or jump to..."
        data-hotkey=s,/
        autocapitalize="off"
        data-action="click:qbsearch-input#handleExpand"
      >
        <div class="mr-2 color-fg-muted">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
        </div>
        <span class="flex-1" data-target="qbsearch-input.inputButtonText">Search or jump to...</span>
          <div class="d-flex" data-target="qbsearch-input.hotkeyIndicator">
            <svg xmlns="http://www.w3.org/2000/svg" width="22" height="20" aria-hidden="true" class="mr-1"><path fill="none" stroke="#979A9C" opacity=".4" d="M3.5.5h12c1.7 0 3 1.3 3 3v13c0 1.7-1.3 3-3 3h-12c-1.7 0-3-1.3-3-3v-13c0-1.7 1.3-3 3-3z"></path><path fill="#979A9C" d="M11.8 6L8 15.1h-.9L10.8 6h1z"></path></svg>

          </div>
      </button>

    <input type="hidden" name="type" class="js-site-search-type-field">

    
<div class="Overlay--hidden " data-modal-dialog-overlay>
  <modal-dialog data-action="close:qbsearch-input#handleClose cancel:qbsearch-input#handleClose" data-target="qbsearch-input.searchSuggestionsDialog" role="dialog" id="search-suggestions-dialog" aria-modal="true" aria-labelledby="search-suggestions-dialog-header" data-view-component="true" class="Overlay Overlay--width-large Overlay--height-auto">
      <h1 id="search-suggestions-dialog-header" class="sr-only">Search code, repositories, users, issues, pull requests...</h1>
    <div class="Overlay-body Overlay-body--paddingNone">
      
          <div data-view-component="true">        <div class="search-suggestions position-fixed width-full color-shadow-large border color-fg-default color-bg-default overflow-hidden d-flex flex-column query-builder-container"
          style="border-radius: 12px;"
          data-target="qbsearch-input.queryBuilderContainer"
          hidden
        >
          <!-- '"` --><!-- </textarea></xmp> --></option></form><form id="query-builder-test-form" action="" accept-charset="UTF-8" method="get">
  <query-builder data-target="qbsearch-input.queryBuilder" id="query-builder-query-builder-test" data-filter-key=":" data-view-component="true" class="QueryBuilder search-query-builder">
    <div class="FormControl FormControl--fullWidth">
      <label id="query-builder-test-label" for="query-builder-test" class="FormControl-label sr-only">
        Search
      </label>
      <div
        class="QueryBuilder-StyledInput width-fit "
        data-target="query-builder.styledInput"
      >
          <span id="query-builder-test-leadingvisual-wrap" class="FormControl-input-leadingVisualWrap QueryBuilder-leadingVisualWrap">
            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search FormControl-input-leadingVisual">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
          </span>
        <div data-target="query-builder.styledInputContainer" class="QueryBuilder-StyledInputContainer">
          <div
            aria-hidden="true"
            class="QueryBuilder-StyledInputContent"
            data-target="query-builder.styledInputContent"
          ></div>
          <div class="QueryBuilder-InputWrapper">
            <div aria-hidden="true" class="QueryBuilder-Sizer" data-target="query-builder.sizer"></div>
            <input id="query-builder-test" name="query-builder-test" value="" autocomplete="off" type="text" role="combobox" spellcheck="false" aria-expanded="false" aria-describedby="validation-14cd0ce9-7b67-4cb3-acee-ce52f36d1e7c" data-target="query-builder.input" data-action="
          input:query-builder#inputChange
          blur:query-builder#inputBlur
          keydown:query-builder#inputKeydown
          focus:query-builder#inputFocus
        " data-view-component="true" class="FormControl-input QueryBuilder-Input FormControl-medium" />
          </div>
        </div>
          <span class="sr-only" id="query-builder-test-clear">Clear</span>
          <button role="button" id="query-builder-test-clear-button" aria-labelledby="query-builder-test-clear query-builder-test-label" data-target="query-builder.clearButton" data-action="
                click:query-builder#clear
                focus:query-builder#clearButtonFocus
                blur:query-builder#clearButtonBlur
              " variant="small" hidden="hidden" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium mr-1 px-2 py-0 d-flex flex-items-center rounded-1 color-fg-muted">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x-circle-fill Button-visual">
    <path d="M2.343 13.657A8 8 0 1 1 13.658 2.343 8 8 0 0 1 2.343 13.657ZM6.03 4.97a.751.751 0 0 0-1.042.018.751.751 0 0 0-.018 1.042L6.94 8 4.97 9.97a.749.749 0 0 0 .326 1.275.749.749 0 0 0 .734-.215L8 9.06l1.97 1.97a.749.749 0 0 0 1.275-.326.749.749 0 0 0-.215-.734L9.06 8l1.97-1.97a.749.749 0 0 0-.326-1.275.749.749 0 0 0-.734.215L8 6.94Z"></path>
</svg>
</button>

      </div>
      <template id="search-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
</template>

<template id="code-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code">
    <path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path>
</svg>
</template>

<template id="file-code-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-file-code">
    <path d="M4 1.75C4 .784 4.784 0 5.75 0h5.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v8.586A1.75 1.75 0 0 1 14.25 15h-9a.75.75 0 0 1 0-1.5h9a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 10 4.25V1.5H5.75a.25.25 0 0 0-.25.25v2.5a.75.75 0 0 1-1.5 0Zm1.72 4.97a.75.75 0 0 1 1.06 0l2 2a.75.75 0 0 1 0 1.06l-2 2a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734l1.47-1.47-1.47-1.47a.75.75 0 0 1 0-1.06ZM3.28 7.78 1.81 9.25l1.47 1.47a.751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018l-2-2a.75.75 0 0 1 0-1.06l2-2a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Zm8.22-6.218V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path>
</svg>
</template>

<template id="history-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-history">
    <path d="m.427 1.927 1.215 1.215a8.002 8.002 0 1 1-1.6 5.685.75.75 0 1 1 1.493-.154 6.5 6.5 0 1 0 1.18-4.458l1.358 1.358A.25.25 0 0 1 3.896 6H.25A.25.25 0 0 1 0 5.75V2.104a.25.25 0 0 1 .427-.177ZM7.75 4a.75.75 0 0 1 .75.75v2.992l2.028.812a.75.75 0 0 1-.557 1.392l-2.5-1A.751.751 0 0 1 7 8.25v-3.5A.75.75 0 0 1 7.75 4Z"></path>
</svg>
</template>

<template id="repo-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo">
    <path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"></path>
</svg>
</template>

<template id="bookmark-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-bookmark">
    <path d="M3 2.75C3 1.784 3.784 1 4.75 1h6.5c.966 0 1.75.784 1.75 1.75v11.5a.75.75 0 0 1-1.227.579L8 11.722l-3.773 3.107A.751.751 0 0 1 3 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v9.91l3.023-2.489a.75.75 0 0 1 .954 0l3.023 2.49V2.75a.25.25 0 0 0-.25-.25Z"></path>
</svg>
</template>

<template id="plus-circle-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus-circle">
    <path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Zm7.25-3.25v2.5h2.5a.75.75 0 0 1 0 1.5h-2.5v2.5a.75.75 0 0 1-1.5 0v-2.5h-2.5a.75.75 0 0 1 0-1.5h2.5v-2.5a.75.75 0 0 1 1.5 0Z"></path>
</svg>
</template>

<template id="circle-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-dot-fill">
    <path d="M8 4a4 4 0 1 1 0 8 4 4 0 0 1 0-8Z"></path>
</svg>
</template>

<template id="trash-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-trash">
    <path d="M11 1.75V3h2.25a.75.75 0 0 1 0 1.5H2.75a.75.75 0 0 1 0-1.5H5V1.75C5 .784 5.784 0 6.75 0h2.5C10.216 0 11 .784 11 1.75ZM4.496 6.675l.66 6.6a.25.25 0 0 0 .249.225h5.19a.25.25 0 0 0 .249-.225l.66-6.6a.75.75 0 0 1 1.492.149l-.66 6.6A1.748 1.748 0 0 1 10.595 15h-5.19a1.75 1.75 0 0 1-1.741-1.575l-.66-6.6a.75.75 0 1 1 1.492-.15ZM6.5 1.75V3h3V1.75a.25.25 0 0 0-.25-.25h-2.5a.25.25 0 0 0-.25.25Z"></path>
</svg>
</template>

<template id="team-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-people">
    <path d="M2 5.5a3.5 3.5 0 1 1 5.898 2.549 5.508 5.508 0 0 1 3.034 4.084.75.75 0 1 1-1.482.235 4 4 0 0 0-7.9 0 .75.75 0 0 1-1.482-.236A5.507 5.507 0 0 1 3.102 8.05 3.493 3.493 0 0 1 2 5.5ZM11 4a3.001 3.001 0 0 1 2.22 5.018 5.01 5.01 0 0 1 2.56 3.012.749.749 0 0 1-.885.954.752.752 0 0 1-.549-.514 3.507 3.507 0 0 0-2.522-2.372.75.75 0 0 1-.574-.73v-.352a.75.75 0 0 1 .416-.672A1.5 1.5 0 0 0 11 5.5.75.75 0 0 1 11 4Zm-5.5-.5a2 2 0 1 0-.001 3.999A2 2 0 0 0 5.5 3.5Z"></path>
</svg>
</template>

<template id="project-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-project">
    <path d="M1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25V1.75C0 .784.784 0 1.75 0ZM1.5 1.75v12.5c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25H1.75a.25.25 0 0 0-.25.25ZM11.75 3a.75.75 0 0 1 .75.75v7.5a.75.75 0 0 1-1.5 0v-7.5a.75.75 0 0 1 .75-.75Zm-8.25.75a.75.75 0 0 1 1.5 0v5.5a.75.75 0 0 1-1.5 0ZM8 3a.75.75 0 0 1 .75.75v3.5a.75.75 0 0 1-1.5 0v-3.5A.75.75 0 0 1 8 3Z"></path>
</svg>
</template>

<template id="pencil-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-pencil">
    <path d="M11.013 1.427a1.75 1.75 0 0 1 2.474 0l1.086 1.086a1.75 1.75 0 0 1 0 2.474l-8.61 8.61c-.21.21-.47.364-.756.445l-3.251.93a.75.75 0 0 1-.927-.928l.929-3.25c.081-.286.235-.547.445-.758l8.61-8.61Zm.176 4.823L9.75 4.81l-6.286 6.287a.253.253 0 0 0-.064.108l-.558 1.953 1.953-.558a.253.253 0 0 0 .108-.064Zm1.238-3.763a.25.25 0 0 0-.354 0L10.811 3.75l1.439 1.44 1.263-1.263a.25.25 0 0 0 0-.354Z"></path>
</svg>
</template>

<template id="copilot-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copilot">
    <path d="M7.998 15.035c-4.562 0-7.873-2.914-7.998-3.749V9.338c.085-.628.677-1.686 1.588-2.065.013-.07.024-.143.036-.218.029-.183.06-.384.126-.612-.201-.508-.254-1.084-.254-1.656 0-.87.128-1.769.693-2.484.579-.733 1.494-1.124 2.724-1.261 1.206-.134 2.262.034 2.944.765.05.053.096.108.139.165.044-.057.094-.112.143-.165.682-.731 1.738-.899 2.944-.765 1.23.137 2.145.528 2.724 1.261.566.715.693 1.614.693 2.484 0 .572-.053 1.148-.254 1.656.066.228.098.429.126.612.012.076.024.148.037.218.924.385 1.522 1.471 1.591 2.095v1.872c0 .766-3.351 3.795-8.002 3.795Zm0-1.485c2.28 0 4.584-1.11 5.002-1.433V7.862l-.023-.116c-.49.21-1.075.291-1.727.291-1.146 0-2.059-.327-2.71-.991A3.222 3.222 0 0 1 8 6.303a3.24 3.24 0 0 1-.544.743c-.65.664-1.563.991-2.71.991-.652 0-1.236-.081-1.727-.291l-.023.116v4.255c.419.323 2.722 1.433 5.002 1.433ZM6.762 2.83c-.193-.206-.637-.413-1.682-.297-1.019.113-1.479.404-1.713.7-.247.312-.369.789-.369 1.554 0 .793.129 1.171.308 1.371.162.181.519.379 1.442.379.853 0 1.339-.235 1.638-.54.315-.322.527-.827.617-1.553.117-.935-.037-1.395-.241-1.614Zm4.155-.297c-1.044-.116-1.488.091-1.681.297-.204.219-.359.679-.242 1.614.091.726.303 1.231.618 1.553.299.305.784.54 1.638.54.922 0 1.28-.198 1.442-.379.179-.2.308-.578.308-1.371 0-.765-.123-1.242-.37-1.554-.233-.296-.693-.587-1.713-.7Z"></path><path d="M6.25 9.037a.75.75 0 0 1 .75.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 .75-.75Zm4.25.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 1.5 0Z"></path>
</svg>
</template>

        <div class="position-relative">
                <ul
                  role="listbox"
                  class="ActionListWrap QueryBuilder-ListWrap"
                  aria-label="Suggestions"
                  data-action="
                    combobox-commit:query-builder#comboboxCommit
                    mousedown:query-builder#resultsMousedown
                  "
                  data-target="query-builder.resultsList"
                  data-persist-list=false
                  id="query-builder-test-results"
                ></ul>
        </div>
      <div class="FormControl-inlineValidation" id="validation-14cd0ce9-7b67-4cb3-acee-ce52f36d1e7c" hidden="hidden">
        <span class="FormControl-inlineValidation--visual">
          <svg aria-hidden="true" height="12" viewBox="0 0 12 12" version="1.1" width="12" data-view-component="true" class="octicon octicon-alert-fill">
    <path d="M4.855.708c.5-.896 1.79-.896 2.29 0l4.675 8.351a1.312 1.312 0 0 1-1.146 1.954H1.33A1.313 1.313 0 0 1 .183 9.058ZM7 7V3H5v4Zm-1 3a1 1 0 1 0 0-2 1 1 0 0 0 0 2Z"></path>
</svg>
        </span>
        <span></span>
</div>    </div>
    <div data-target="query-builder.screenReaderFeedback" aria-live="polite" aria-atomic="true" class="sr-only"></div>
</query-builder></form>
          <div class="d-flex flex-row color-fg-muted px-3 text-small color-bg-default search-feedback-prompt">
            <a target="_blank" href="https://docs.github.com/en/search-github/github-code-search/understanding-github-code-search-syntax" data-view-component="true" class="Link color-fg-accent text-normal ml-2">
              Search syntax tips
</a>            <div class="d-flex flex-1"></div>
          </div>
        </div>
</div>

    </div>
</modal-dialog></div>
  </div>
  <div data-action="click:qbsearch-input#retract" class="dark-backdrop position-fixed" hidden data-target="qbsearch-input.darkBackdrop"></div>
  <div class="color-fg-default">
    
<div class="Overlay--hidden Overlay-backdrop--center" data-modal-dialog-overlay>
  <modal-dialog data-target="qbsearch-input.feedbackDialog" data-action="close:qbsearch-input#handleDialogClose cancel:qbsearch-input#handleDialogClose" role="dialog" id="feedback-dialog" aria-modal="true" aria-disabled="true" aria-labelledby="feedback-dialog-title" aria-describedby="feedback-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade">
    <div data-view-component="true" class="Overlay-header">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="feedback-dialog-title">
        Provide feedback
      </h1>
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="feedback-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
</div>
      <div data-view-component="true" class="Overlay-body">        <!-- '"` --><!-- </textarea></xmp> --></option></form><form id="code-search-feedback-form" data-turbo="false" action="/search/feedback" accept-charset="UTF-8" method="post"><input type="hidden" data-csrf="true" name="authenticity_token" value="djAosVxppGYm29rNi6s8H6ExUPHxPxA9pd1Ru/VqG98GKv3GAbDeo64rsIzcVpPEejYyW9KpmO/exh+wQ2x5iA==" />
          <p>We read every piece of feedback, and take your input very seriously.</p>
          <textarea name="feedback" class="form-control width-full mb-2" style="height: 120px" id="feedback"></textarea>
          <input name="include_email" id="include_email" aria-label="Include my email address so I can be contacted" class="form-control mr-2" type="checkbox">
          <label for="include_email" style="font-weight: normal">Include my email address so I can be contacted</label>
</form></div>
      <div data-view-component="true" class="Overlay-footer Overlay-footer--alignEnd">          <button data-close-dialog-id="feedback-dialog" type="button" data-view-component="true" class="btn">    Cancel
</button>
          <button form="code-search-feedback-form" data-action="click:qbsearch-input#submitFeedback" type="submit" data-view-component="true" class="btn-primary btn">    Submit feedback
</button>
</div>
</modal-dialog></div>

    <custom-scopes data-target="qbsearch-input.customScopesManager">
    
<div class="Overlay--hidden Overlay-backdrop--center" data-modal-dialog-overlay>
  <modal-dialog data-target="custom-scopes.customScopesModalDialog" data-action="close:qbsearch-input#handleDialogClose cancel:qbsearch-input#handleDialogClose" role="dialog" id="custom-scopes-dialog" aria-modal="true" aria-disabled="true" aria-labelledby="custom-scopes-dialog-title" aria-describedby="custom-scopes-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade">
    <div data-view-component="true" class="Overlay-header Overlay-header--divided">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="custom-scopes-dialog-title">
        Saved searches
      </h1>
        <h2 id="custom-scopes-dialog-description" class="Overlay-description">Use saved searches to filter your results more quickly</h2>
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="custom-scopes-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
</div>
      <div data-view-component="true" class="Overlay-body">        <div data-target="custom-scopes.customScopesModalDialogFlash"></div>

        <div hidden class="create-custom-scope-form" data-target="custom-scopes.createCustomScopeForm">
        <!-- '"` --><!-- </textarea></xmp> --></option></form><form id="custom-scopes-dialog-form" data-turbo="false" action="/search/custom_scopes" accept-charset="UTF-8" method="post"><input type="hidden" data-csrf="true" name="authenticity_token" value="tQwjyFJhtO+MaG+qps/EkO7jesKlmZyRFK42rz//V4yJJk5P68OBeYKp+9a2RnYwtzAHCXlsZjZIxBqC6h4VEg==" />
          <div data-target="custom-scopes.customScopesModalDialogFlash"></div>

          <input type="hidden" id="custom_scope_id" name="custom_scope_id" data-target="custom-scopes.customScopesIdField">

          <div class="form-group">
            <label for="custom_scope_name">Name</label>
            <auto-check src="/search/custom_scopes/check_name" required>
              <input
                type="text"
                name="custom_scope_name"
                id="custom_scope_name"
                data-target="custom-scopes.customScopesNameField"
                class="form-control"
                autocomplete="off"
                placeholder="github-ruby"
                required
                maxlength="50">
              <input type="hidden" data-csrf="true" value="WC1Zzt43ZriXfn2/XOiDH5YvNy+mZPjNNTFMQrHzOGBkGj8boMotufQvxTLqG5mjnL6ObDXd6A9gnBitS3EQiA==" />
            </auto-check>
          </div>

          <div class="form-group">
            <label for="custom_scope_query">Query</label>
            <input
              type="text"
              name="custom_scope_query"
              id="custom_scope_query"
              data-target="custom-scopes.customScopesQueryField"
              class="form-control"
              autocomplete="off"
              placeholder="(repo:mona/a OR repo:mona/b) AND lang:python"
              required
              maxlength="500">
          </div>

          <p class="text-small color-fg-muted">
            To see all available qualifiers, see our <a class="Link--inTextBlock" href="https://docs.github.com/en/search-github/github-code-search/understanding-github-code-search-syntax">documentation</a>.
          </p>
</form>        </div>

        <div data-target="custom-scopes.manageCustomScopesForm">
          <div data-target="custom-scopes.list"></div>
        </div>

</div>
      <div data-view-component="true" class="Overlay-footer Overlay-footer--alignEnd Overlay-footer--divided">          <button data-action="click:custom-scopes#customScopesCancel" type="button" data-view-component="true" class="btn">    Cancel
</button>
          <button form="custom-scopes-dialog-form" data-action="click:custom-scopes#customScopesSubmit" data-target="custom-scopes.customScopesSubmitButton" type="submit" data-view-component="true" class="btn-primary btn">    Create saved search
</button>
</div>
</modal-dialog></div>
    </custom-scopes>
  </div>
</qbsearch-input><input type="hidden" data-csrf="true" class="js-data-jump-to-suggestions-path-csrf" value="87hbKTOooSomY0rUWG5xNnusDH6oVyToSrWy3QwgH2VQrJuHDwW0PRq6yaZe/e4LAV12Hrh+LxTkl2dSBL5TfQ==" />


          <div class="position-relative mr-lg-3 d-lg-inline-block">
            <a href="/login?return_to=https%3A%2F%2Fgithub.com%2Fjfischer%2Fmicropython-tsl2591%2Fblob%2Fmaster%2Ftsl2591.py"
              class="HeaderMenu-link HeaderMenu-link--sign-in flex-shrink-0 no-underline d-block d-lg-inline-block border border-lg-0 rounded rounded-lg-0 p-2 p-lg-0"
              data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;site header menu&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;SIGN_UP&quot;,&quot;originating_url&quot;:&quot;https://github.com/jfischer/micropython-tsl2591/blob/master/tsl2591.py&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="b57cb1f9e4436a3be5596c2fbe2a5c33e9d0ee0e2211017a7816ccf0adf7e958"
              data-ga-click="(Logged out) Header, clicked Sign in, text:sign-in">
              Sign in
            </a>
          </div>

            <a href="/signup?ref_cta=Sign+up&amp;ref_loc=header+logged+out&amp;ref_page=%2F%3Cuser-name%3E%2F%3Crepo-name%3E%2Fblob%2Fshow&amp;source=header-repo&amp;source_repo=jfischer%2Fmicropython-tsl2591"
              class="HeaderMenu-link HeaderMenu-link--sign-up flex-shrink-0 d-none d-lg-inline-block no-underline border color-border-default rounded px-2 py-1"
              data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;site header menu&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;SIGN_UP&quot;,&quot;originating_url&quot;:&quot;https://github.com/jfischer/micropython-tsl2591/blob/master/tsl2591.py&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="b57cb1f9e4436a3be5596c2fbe2a5c33e9d0ee0e2211017a7816ccf0adf7e958"
              data-analytics-event="{&quot;category&quot;:&quot;Sign up&quot;,&quot;action&quot;:&quot;click to sign up for account&quot;,&quot;label&quot;:&quot;ref_page:/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show;ref_cta:Sign up;ref_loc:header logged out&quot;}"
            >
              Sign up
            </a>
        </div>
      </div>
    </div>
  </div>
</header>

      <div hidden="hidden" data-view-component="true" class="js-stale-session-flash stale-session-flash flash flash-warn flash-full mb-3">
  
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
        <span class="js-stale-session-flash-signed-in" hidden>You signed in with another tab or window. <a class="Link--inTextBlock" href="">Reload</a> to refresh your session.</span>
        <span class="js-stale-session-flash-signed-out" hidden>You signed out in another tab or window. <a class="Link--inTextBlock" href="">Reload</a> to refresh your session.</span>
        <span class="js-stale-session-flash-switched" hidden>You switched accounts on another tab or window. <a class="Link--inTextBlock" href="">Reload</a> to refresh your session.</span>

    <button id="icon-button-61f5c397-c7f4-482c-a1bf-3107a9f52f0f" aria-labelledby="tooltip-0cf52d0c-cd94-4c22-86ba-088e00e46781" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium flash-close js-flash-close">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x Button-visual">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
</button><tool-tip id="tooltip-0cf52d0c-cd94-4c22-86ba-088e00e46781" for="icon-button-61f5c397-c7f4-482c-a1bf-3107a9f52f0f" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute">Dismiss alert</tool-tip>


  
</div>
    </div>

  <div id="start-of-content" class="show-on-focus"></div>








    <div id="js-flash-container" data-turbo-replace>


      <include-fragment src="/settings/two_factor_authentication/holiday_warning_banner"></include-fragment>



  <template class="js-flash-template">
    
<div class="flash flash-full   {{ className }}">
  <div class="px-2" >
    <button autofocus class="flash-close js-flash-close" type="button" aria-label="Dismiss this message">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
    </button>
    <div aria-atomic="true" role="alert" class="js-flash-alert">
      
      <div>{{ message }}</div>

    </div>
  </div>
</div>
  </template>
</div>


    
    <include-fragment class="js-notification-shelf-include-fragment" data-base-src="https://github.com/notifications/beta/shelf"></include-fragment>






  <div
    class="application-main "
    data-commit-hovercards-enabled
    data-discussion-hovercards-enabled
    data-issue-and-pr-hovercards-enabled
  >
        <div itemscope itemtype="http://schema.org/SoftwareSourceCode" class="">
    <main id="js-repo-pjax-container" >
      
      
      






  
  <div id="repository-container-header"  class="pt-3 hide-full-screen" style="background-color: var(--page-header-bgColor, var(--color-page-header-bg));" data-turbo-replace>

      <div class="d-flex flex-wrap flex-justify-end mb-3  px-3 px-md-4 px-lg-5" style="gap: 1rem;">

        <div class="flex-auto min-width-0 width-fit mr-3">
            
  <div class=" d-flex flex-wrap flex-items-center wb-break-word f3 text-normal">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo-forked color-fg-muted mr-2">
    <path d="M5 5.372v.878c0 .414.336.75.75.75h4.5a.75.75 0 0 0 .75-.75v-.878a2.25 2.25 0 1 1 1.5 0v.878a2.25 2.25 0 0 1-2.25 2.25h-1.5v2.128a2.251 2.251 0 1 1-1.5 0V8.5h-1.5A2.25 2.25 0 0 1 3.5 6.25v-.878a2.25 2.25 0 1 1 1.5 0ZM5 3.25a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Zm6.75.75a.75.75 0 1 0 0-1.5.75.75 0 0 0 0 1.5Zm-3 8.75a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Z"></path>
</svg>
    
    <span class="author flex-self-stretch" itemprop="author">
      <a class="url fn" rel="author" data-hovercard-type="user" data-hovercard-url="/users/jfischer/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/jfischer">
        jfischer
</a>    </span>
    <span class="mx-1 flex-self-stretch color-fg-muted">/</span>
    <strong itemprop="name" class="mr-2 flex-self-stretch">
      <a data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" href="/jfischer/micropython-tsl2591">micropython-tsl2591</a>
    </strong>

    <span></span><span class="Label Label--secondary v-align-middle mr-1">Public</span>
  </div>
    <span class="text-small lh-condensed-ultra no-wrap mt-1" data-repository-hovercards-enabled>
      forked from <a data-hovercard-type="repository" data-hovercard-url="/maxlklaxl/python-tsl2591/hovercard" class="Link--inTextBlock" href="/maxlklaxl/python-tsl2591">maxlklaxl/python-tsl2591</a>
    </span>


        </div>

        <div id="repository-details-container" data-turbo-replace>
            <ul class="pagehead-actions flex-shrink-0 d-none d-md-inline" style="padding: 2px 0;">
    
      

  <li>
            <a href="/login?return_to=%2Fjfischer%2Fmicropython-tsl2591" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;notification subscription menu watch&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;LOG_IN&quot;,&quot;originating_url&quot;:&quot;https://github.com/jfischer/micropython-tsl2591/blob/master/tsl2591.py&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="5d37ba56d3d060dc3a08e7238cf2266dab2505f7658d643ac19eca7ec479313e" aria-label="You must be signed in to change notification settings" data-view-component="true" class="tooltipped tooltipped-s btn-sm btn">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-bell mr-2">
    <path d="M8 16a2 2 0 0 0 1.985-1.75c.017-.137-.097-.25-.235-.25h-3.5c-.138 0-.252.113-.235.25A2 2 0 0 0 8 16ZM3 5a5 5 0 0 1 10 0v2.947c0 .05.015.098.042.139l1.703 2.555A1.519 1.519 0 0 1 13.482 13H2.518a1.516 1.516 0 0 1-1.263-2.36l1.703-2.554A.255.255 0 0 0 3 7.947Zm5-3.5A3.5 3.5 0 0 0 4.5 5v2.947c0 .346-.102.683-.294.97l-1.703 2.556a.017.017 0 0 0-.003.01l.001.006c0 .002.002.004.004.006l.006.004.007.001h10.964l.007-.001.006-.004.004-.006.001-.007a.017.017 0 0 0-.003-.01l-1.703-2.554a1.745 1.745 0 0 1-.294-.97V5A3.5 3.5 0 0 0 8 1.5Z"></path>
</svg>Notifications
</a>
  </li>

  <li>
          <a icon="repo-forked" id="fork-button" href="/login?return_to=%2Fjfischer%2Fmicropython-tsl2591" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;repo details fork button&quot;,&quot;repository_id&quot;:62343362,&quot;auth_type&quot;:&quot;LOG_IN&quot;,&quot;originating_url&quot;:&quot;https://github.com/jfischer/micropython-tsl2591/blob/master/tsl2591.py&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="2fd3395d1df18b3b2ef53318cc1afcb018287091a88cebb7ccfc0061fd6494b4" data-view-component="true" class="btn-sm btn">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo-forked mr-2">
    <path d="M5 5.372v.878c0 .414.336.75.75.75h4.5a.75.75 0 0 0 .75-.75v-.878a2.25 2.25 0 1 1 1.5 0v.878a2.25 2.25 0 0 1-2.25 2.25h-1.5v2.128a2.251 2.251 0 1 1-1.5 0V8.5h-1.5A2.25 2.25 0 0 1 3.5 6.25v-.878a2.25 2.25 0 1 1 1.5 0ZM5 3.25a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Zm6.75.75a.75.75 0 1 0 0-1.5.75.75 0 0 0 0 1.5Zm-3 8.75a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Z"></path>
</svg>Fork
    <span id="repo-network-counter" data-pjax-replace="true" data-turbo-replace="true" title="23" data-view-component="true" class="Counter">23</span>
</a>
  </li>

  <li>
        <div data-view-component="true" class="BtnGroup d-flex">
        <a href="/login?return_to=%2Fjfischer%2Fmicropython-tsl2591" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;star button&quot;,&quot;repository_id&quot;:62343362,&quot;auth_type&quot;:&quot;LOG_IN&quot;,&quot;originating_url&quot;:&quot;https://github.com/jfischer/micropython-tsl2591/blob/master/tsl2591.py&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="46586ecd8b95202d14d57cacabcade4044ac997da7646d405d27cbf2c2ca83f8" aria-label="You must be signed in to star a repository" data-view-component="true" class="tooltipped tooltipped-s btn-sm btn BtnGroup-item">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-star v-align-text-bottom d-inline-block mr-2">
    <path d="M8 .25a.75.75 0 0 1 .673.418l1.882 3.815 4.21.612a.75.75 0 0 1 .416 1.279l-3.046 2.97.719 4.192a.751.751 0 0 1-1.088.791L8 12.347l-3.766 1.98a.75.75 0 0 1-1.088-.79l.72-4.194L.818 6.374a.75.75 0 0 1 .416-1.28l4.21-.611L7.327.668A.75.75 0 0 1 8 .25Zm0 2.445L6.615 5.5a.75.75 0 0 1-.564.41l-3.097.45 2.24 2.184a.75.75 0 0 1 .216.664l-.528 3.084 2.769-1.456a.75.75 0 0 1 .698 0l2.77 1.456-.53-3.084a.75.75 0 0 1 .216-.664l2.24-2.183-3.096-.45a.75.75 0 0 1-.564-.41L8 2.694Z"></path>
</svg><span data-view-component="true" class="d-inline">
          Star
</span>          <span id="repo-stars-counter-star" aria-label="6 users starred this repository" data-singular-suffix="user starred this repository" data-plural-suffix="users starred this repository" data-turbo-replace="true" title="6" data-view-component="true" class="Counter js-social-count">6</span>
</a>        <button aria-label="You must be signed in to add this repository to a list" type="button" disabled="disabled" data-view-component="true" class="btn-sm btn BtnGroup-item px-2">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-triangle-down">
    <path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path>
</svg>
</button></div>
  </li>

</ul>

        </div>
      </div>

        <div id="responsive-meta-container" data-turbo-replace>
</div>


          <nav data-pjax="#js-repo-pjax-container" aria-label="Repository" data-view-component="true" class="js-repo-nav js-sidenav-container-pjax js-responsive-underlinenav overflow-hidden UnderlineNav px-3 px-md-4 px-lg-5">

  <ul data-view-component="true" class="UnderlineNav-body list-style-none">
      <li data-view-component="true" class="d-inline-flex">
  <a id="code-tab" href="/jfischer/micropython-tsl2591" data-tab-item="i0code-tab" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages repo_deployments repo_attestations /jfischer/micropython-tsl2591" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g c" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Code&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" aria-current="page" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item selected">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code UnderlineNav-octicon d-none d-sm-inline">
    <path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path>
</svg>
        <span data-content="Code">Code</span>
          <span id="code-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="pull-requests-tab" href="/jfischer/micropython-tsl2591/pulls" data-tab-item="i1pull-requests-tab" data-selected-links="repo_pulls checks /jfischer/micropython-tsl2591/pulls" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g p" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Pull requests&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request UnderlineNav-octicon d-none d-sm-inline">
    <path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path>
</svg>
        <span data-content="Pull requests">Pull requests</span>
          <span id="pull-requests-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="0" hidden="hidden" data-view-component="true" class="Counter">0</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="actions-tab" href="/jfischer/micropython-tsl2591/actions" data-tab-item="i2actions-tab" data-selected-links="repo_actions /jfischer/micropython-tsl2591/actions" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g a" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Actions&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-play UnderlineNav-octicon d-none d-sm-inline">
    <path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Zm4.879-2.773 4.264 2.559a.25.25 0 0 1 0 .428l-4.264 2.559A.25.25 0 0 1 6 10.559V5.442a.25.25 0 0 1 .379-.215Z"></path>
</svg>
        <span data-content="Actions">Actions</span>
          <span id="actions-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="projects-tab" href="/jfischer/micropython-tsl2591/projects" data-tab-item="i3projects-tab" data-selected-links="repo_projects new_repo_project repo_project /jfischer/micropython-tsl2591/projects" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g b" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Projects&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-table UnderlineNav-octicon d-none d-sm-inline">
    <path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25ZM6.5 6.5v8h7.75a.25.25 0 0 0 .25-.25V6.5Zm8-1.5V1.75a.25.25 0 0 0-.25-.25H6.5V5Zm-13 1.5v7.75c0 .138.112.25.25.25H5v-8ZM5 5V1.5H1.75a.25.25 0 0 0-.25.25V5Z"></path>
</svg>
        <span data-content="Projects">Projects</span>
          <span id="projects-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="0" hidden="hidden" data-view-component="true" class="Counter">0</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="wiki-tab" href="/jfischer/micropython-tsl2591/wiki" data-tab-item="i4wiki-tab" data-selected-links="repo_wiki /jfischer/micropython-tsl2591/wiki" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g w" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Wiki&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-book UnderlineNav-octicon d-none d-sm-inline">
    <path d="M0 1.75A.75.75 0 0 1 .75 1h4.253c1.227 0 2.317.59 3 1.501A3.743 3.743 0 0 1 11.006 1h4.245a.75.75 0 0 1 .75.75v10.5a.75.75 0 0 1-.75.75h-4.507a2.25 2.25 0 0 0-1.591.659l-.622.621a.75.75 0 0 1-1.06 0l-.622-.621A2.25 2.25 0 0 0 5.258 13H.75a.75.75 0 0 1-.75-.75Zm7.251 10.324.004-5.073-.002-2.253A2.25 2.25 0 0 0 5.003 2.5H1.5v9h3.757a3.75 3.75 0 0 1 1.994.574ZM8.755 4.75l-.004 7.322a3.752 3.752 0 0 1 1.992-.572H14.5v-9h-3.495a2.25 2.25 0 0 0-2.25 2.25Z"></path>
</svg>
        <span data-content="Wiki">Wiki</span>
          <span id="wiki-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="security-tab" href="/jfischer/micropython-tsl2591/security" data-tab-item="i5security-tab" data-selected-links="security overview alerts policy token_scanning code_scanning /jfischer/micropython-tsl2591/security" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g s" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Security&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-shield UnderlineNav-octicon d-none d-sm-inline">
    <path d="M7.467.133a1.748 1.748 0 0 1 1.066 0l5.25 1.68A1.75 1.75 0 0 1 15 3.48V7c0 1.566-.32 3.182-1.303 4.682-.983 1.498-2.585 2.813-5.032 3.855a1.697 1.697 0 0 1-1.33 0c-2.447-1.042-4.049-2.357-5.032-3.855C1.32 10.182 1 8.566 1 7V3.48a1.75 1.75 0 0 1 1.217-1.667Zm.61 1.429a.25.25 0 0 0-.153 0l-5.25 1.68a.25.25 0 0 0-.174.238V7c0 1.358.275 2.666 1.057 3.86.784 1.194 2.121 2.34 4.366 3.297a.196.196 0 0 0 .154 0c2.245-.956 3.582-2.104 4.366-3.298C13.225 9.666 13.5 8.36 13.5 7V3.48a.251.251 0 0 0-.174-.237l-5.25-1.68ZM8.75 4.75v3a.75.75 0 0 1-1.5 0v-3a.75.75 0 0 1 1.5 0ZM9 10.5a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
        <span data-content="Security">Security</span>
          <include-fragment src="/jfischer/micropython-tsl2591/security/overall-count" accept="text/fragment+html"></include-fragment>

    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="insights-tab" href="/jfischer/micropython-tsl2591/pulse" data-tab-item="i6insights-tab" data-selected-links="repo_graphs repo_contributors dependency_graph dependabot_updates pulse people community /jfischer/micropython-tsl2591/pulse" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Insights&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-graph UnderlineNav-octicon d-none d-sm-inline">
    <path d="M1.5 1.75V13.5h13.75a.75.75 0 0 1 0 1.5H.75a.75.75 0 0 1-.75-.75V1.75a.75.75 0 0 1 1.5 0Zm14.28 2.53-5.25 5.25a.75.75 0 0 1-1.06 0L7 7.06 4.28 9.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.25-3.25a.75.75 0 0 1 1.06 0L10 7.94l4.72-4.72a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Z"></path>
</svg>
        <span data-content="Insights">Insights</span>
          <span id="insights-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
</ul>
    <div style="visibility:hidden;" data-view-component="true" class="UnderlineNav-actions js-responsive-underlinenav-overflow position-absolute pr-3 pr-md-4 pr-lg-5 right-0">      <action-menu data-select-variant="none" data-view-component="true">
  <focus-group direction="vertical" mnemonics retain>
    <button id="action-menu-afdde19b-8e93-4147-9554-5359781fecf4-button" popovertarget="action-menu-afdde19b-8e93-4147-9554-5359781fecf4-overlay" aria-controls="action-menu-afdde19b-8e93-4147-9554-5359781fecf4-list" aria-haspopup="true" aria-labelledby="tooltip-187a4249-19da-4208-b799-9e649fb9a2f1" type="button" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium UnderlineNav-item">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-kebab-horizontal Button-visual">
    <path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path>
</svg>
</button><tool-tip id="tooltip-187a4249-19da-4208-b799-9e649fb9a2f1" for="action-menu-afdde19b-8e93-4147-9554-5359781fecf4-button" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute">Additional navigation options</tool-tip>


<anchored-position id="action-menu-afdde19b-8e93-4147-9554-5359781fecf4-overlay" anchor="action-menu-afdde19b-8e93-4147-9554-5359781fecf4-button" align="start" side="outside-bottom" anchor-offset="normal" popover="auto" data-view-component="true">
  <div data-view-component="true" class="Overlay Overlay--size-auto">
    
      <div data-view-component="true" class="Overlay-body Overlay-body--paddingNone">          <div data-view-component="true">
  <ul aria-labelledby="action-menu-afdde19b-8e93-4147-9554-5359781fecf4-button" id="action-menu-afdde19b-8e93-4147-9554-5359781fecf4-list" role="menu" data-view-component="true" class="ActionListWrap--inset ActionListWrap">
      <li hidden="hidden" data-menu-item="i0code-tab" data-targets="action-list.items action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    <a tabindex="-1" id="item-79175bc0-ce84-4e1a-a9be-635c3ae09c28" href="/jfischer/micropython-tsl2591" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code">
    <path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Code
</span></a>
  
  
</li>
      <li hidden="hidden" data-menu-item="i1pull-requests-tab" data-targets="action-list.items action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    <a tabindex="-1" id="item-a6ecbe18-595e-4cf8-a372-74bf7088155d" href="/jfischer/micropython-tsl2591/pulls" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request">
    <path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Pull requests
</span></a>
  
  
</li>
      <li hidden="hidden" data-menu-item="i2actions-tab" data-targets="action-list.items action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    <a tabindex="-1" id="item-aac510d7-38e6-4989-bb22-c3b300d37314" href="/jfischer/micropython-tsl2591/actions" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-play">
    <path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Zm4.879-2.773 4.264 2.559a.25.25 0 0 1 0 .428l-4.264 2.559A.25.25 0 0 1 6 10.559V5.442a.25.25 0 0 1 .379-.215Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Actions
</span></a>
  
  
</li>
      <li hidden="hidden" data-menu-item="i3projects-tab" data-targets="action-list.items action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    <a tabindex="-1" id="item-576fe214-52ad-4310-8c94-f76dad97a192" href="/jfischer/micropython-tsl2591/projects" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-table">
    <path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25ZM6.5 6.5v8h7.75a.25.25 0 0 0 .25-.25V6.5Zm8-1.5V1.75a.25.25 0 0 0-.25-.25H6.5V5Zm-13 1.5v7.75c0 .138.112.25.25.25H5v-8ZM5 5V1.5H1.75a.25.25 0 0 0-.25.25V5Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Projects
</span></a>
  
  
</li>
      <li hidden="hidden" data-menu-item="i4wiki-tab" data-targets="action-list.items action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    <a tabindex="-1" id="item-ac70dfee-8a50-471b-9c93-cab8e933c69c" href="/jfischer/micropython-tsl2591/wiki" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-book">
    <path d="M0 1.75A.75.75 0 0 1 .75 1h4.253c1.227 0 2.317.59 3 1.501A3.743 3.743 0 0 1 11.006 1h4.245a.75.75 0 0 1 .75.75v10.5a.75.75 0 0 1-.75.75h-4.507a2.25 2.25 0 0 0-1.591.659l-.622.621a.75.75 0 0 1-1.06 0l-.622-.621A2.25 2.25 0 0 0 5.258 13H.75a.75.75 0 0 1-.75-.75Zm7.251 10.324.004-5.073-.002-2.253A2.25 2.25 0 0 0 5.003 2.5H1.5v9h3.757a3.75 3.75 0 0 1 1.994.574ZM8.755 4.75l-.004 7.322a3.752 3.752 0 0 1 1.992-.572H14.5v-9h-3.495a2.25 2.25 0 0 0-2.25 2.25Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Wiki
</span></a>
  
  
</li>
      <li hidden="hidden" data-menu-item="i5security-tab" data-targets="action-list.items action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    <a tabindex="-1" id="item-e3a799f4-354b-4886-ae5c-5228117e6eb2" href="/jfischer/micropython-tsl2591/security" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-shield">
    <path d="M7.467.133a1.748 1.748 0 0 1 1.066 0l5.25 1.68A1.75 1.75 0 0 1 15 3.48V7c0 1.566-.32 3.182-1.303 4.682-.983 1.498-2.585 2.813-5.032 3.855a1.697 1.697 0 0 1-1.33 0c-2.447-1.042-4.049-2.357-5.032-3.855C1.32 10.182 1 8.566 1 7V3.48a1.75 1.75 0 0 1 1.217-1.667Zm.61 1.429a.25.25 0 0 0-.153 0l-5.25 1.68a.25.25 0 0 0-.174.238V7c0 1.358.275 2.666 1.057 3.86.784 1.194 2.121 2.34 4.366 3.297a.196.196 0 0 0 .154 0c2.245-.956 3.582-2.104 4.366-3.298C13.225 9.666 13.5 8.36 13.5 7V3.48a.251.251 0 0 0-.174-.237l-5.25-1.68ZM8.75 4.75v3a.75.75 0 0 1-1.5 0v-3a.75.75 0 0 1 1.5 0ZM9 10.5a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Security
</span></a>
  
  
</li>
      <li hidden="hidden" data-menu-item="i6insights-tab" data-targets="action-list.items action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    <a tabindex="-1" id="item-8f2ebe92-7a7d-4b2e-ad65-da3872854234" href="/jfischer/micropython-tsl2591/pulse" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-graph">
    <path d="M1.5 1.75V13.5h13.75a.75.75 0 0 1 0 1.5H.75a.75.75 0 0 1-.75-.75V1.75a.75.75 0 0 1 1.5 0Zm14.28 2.53-5.25 5.25a.75.75 0 0 1-1.06 0L7 7.06 4.28 9.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.25-3.25a.75.75 0 0 1 1.06 0L10 7.94l4.72-4.72a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Insights
</span></a>
  
  
</li>
</ul>  
</div>

</div>
      
</div></anchored-position>  </focus-group>
</action-menu></div>
</nav>

  </div>

  



<turbo-frame id="repo-content-turbo-frame" target="_top" data-turbo-action="advance" class="">
    <div id="repo-content-pjax-container" class="repository-content " >
    


    
      
    





<react-app
  app-name="react-code-view"
  initial-path="/jfischer/micropython-tsl2591/blob/master/tsl2591.py"
  style="min-height: calc(100vh - 64px)" 
  data-ssr="false"
  data-lazy="false"
  data-alternate="false"
>
  
  <script type="application/json" data-target="react-app.embeddedData">{"payload":{"allShortcutsEnabled":false,"fileTree":{"":{"items":[{"name":".gitignore","path":".gitignore","contentType":"file"},{"name":"LICENSE.md","path":"LICENSE.md","contentType":"file"},{"name":"README.md","path":"README.md","contentType":"file"},{"name":"tsl2591.py","path":"tsl2591.py","contentType":"file"}],"totalCount":4}},"fileTreeProcessingTime":1.767704,"foldersToFetch":[],"reducedMotionEnabled":null,"repo":{"id":62343362,"defaultBranch":"master","name":"micropython-tsl2591","ownerLogin":"jfischer","currentUserCanPush":false,"isFork":true,"isEmpty":false,"createdAt":"2016-06-30T21:28:02.000Z","ownerAvatar":"https://avatars.githubusercontent.com/u/86544?v=4","public":true,"private":false,"isOrgOwned":false},"symbolsExpanded":false,"treeExpanded":true,"refInfo":{"name":"master","listCacheKey":"v0:1613894703.1834052","canEdit":false,"refType":"branch","currentOid":"74943ec4b89c6c134960cc3bdfd7af5261fbadb0"},"path":"tsl2591.py","currentUser":null,"blob":{"rawLines":["# tsl2591 lux sensor interface","import time","","VISIBLE = 2","INFRARED = 1","FULLSPECTRUM = 0","","ADDR = 0x29","READBIT = 0x01","COMMAND_BIT = 0xA0","CLEAR_BIT = 0x40","WORD_BIT = 0x20","BLOCK_BIT = 0x10","ENABLE_POWERON = 0x01","ENABLE_POWEROFF = 0x00","ENABLE_AEN = 0x02","ENABLE_AIEN = 0x10","CONTROL_RESET = 0x80","LUX_DF = 408.0","LUX_COEFB = 1.64","LUX_COEFC = 0.59","LUX_COEFD = 0.86","","REGISTER_ENABLE = 0x00","REGISTER_CONTROL = 0x01","REGISTER_THRESHHOLDL_LOW = 0x02","REGISTER_THRESHHOLDL_HIGH = 0x03","REGISTER_THRESHHOLDH_LOW = 0x04","REGISTER_THRESHHOLDH_HIGH = 0x05","REGISTER_INTERRUPT = 0x06","REGISTER_CRC = 0x08","REGISTER_ID = 0x0A","REGISTER_CHAN0_LOW = 0x14","REGISTER_CHAN0_HIGH = 0x15","REGISTER_CHAN1_LOW = 0x16","REGISTER_CHAN1_HIGH = 0x17","INTEGRATIONTIME_100MS = 0x00","INTEGRATIONTIME_200MS = 0x01","INTEGRATIONTIME_300MS = 0x02","INTEGRATIONTIME_400MS = 0x03","INTEGRATIONTIME_500MS = 0x04","INTEGRATIONTIME_600MS = 0x05","","GAIN_LOW = 0x00","GAIN_MED = 0x10","GAIN_HIGH = 0x20","GAIN_MAX = 0x30","","def _bytes_to_int(data):","    return data[0] + (data[1]\u003c\u003c8)","","from machine import I2C, Pin","class SMBusEmulator:","    __slots__ = ('i2c',)","    def __init__(self, scl_pinno=5, sda_pinno=4):","        self.i2c = I2C(scl=Pin(scl_pinno, Pin.IN),","                       sda=Pin(sda_pinno, Pin.IN))","","    def write_byte_data(self, addr, cmd, val):","        buf = bytes([cmd, val])","        self.i2c.writeto(addr, buf)","","    def read_word_data(self, addr, cmd):","        assert cmd \u003c 256","        buf = bytes([cmd])","        self.i2c.writeto(addr, buf)","        data = self.i2c.readfrom(addr, 4)","        return _bytes_to_int(data)","","SENSOR_ADDRESS=0x29","","class Tsl2591:","    def __init__(","                 self,","                 sensor_id,","                 integration=INTEGRATIONTIME_100MS,","                 gain=GAIN_LOW","                 ):","        self.sensor_id = sensor_id","        self.bus = SMBusEmulator()","        self.integration_time = integration","        self.gain = gain","        self.set_timing(self.integration_time)","        self.set_gain(self.gain)","        self.disable()","","    def set_timing(self, integration):","        self.enable()","        self.integration_time = integration","        self.bus.write_byte_data(","                    SENSOR_ADDRESS,","                    COMMAND_BIT | REGISTER_CONTROL,","                    self.integration_time | self.gain","                    )","        self.disable()","","    def set_gain(self, gain):","        self.enable()","        self.gain = gain","        self.bus.write_byte_data(","                    SENSOR_ADDRESS,","                    COMMAND_BIT | REGISTER_CONTROL,","                    self.integration_time | self.gain","                    )","        self.disable()","","    def calculate_lux(self, full, ir):","        if (full == 0xFFFF) | (ir == 0xFFFF):","            return 0","            ","        case_integ = {","            INTEGRATIONTIME_100MS: 100.,","            INTEGRATIONTIME_200MS: 200.,","            INTEGRATIONTIME_300MS: 300.,","            INTEGRATIONTIME_400MS: 400.,","            INTEGRATIONTIME_500MS: 500.,","            INTEGRATIONTIME_600MS: 600.,","            }","        if self.integration_time in case_integ.keys():","            atime = case_integ[self.integration_time]","        else:","            atime = 100.","","        case_gain = {","            GAIN_LOW: 1.,","            GAIN_MED: 25.,","            GAIN_HIGH: 428.,","            GAIN_MAX: 9876.,","            }","","        if self.gain in case_gain.keys():","            again = case_gain[self.gain]","        else:","            again = 1.","","        cpl = (atime * again) / LUX_DF","        lux1 = (full - (LUX_COEFB * ir)) / cpl","","        lux2 = ((LUX_COEFC * full) - (LUX_COEFD * ir)) / cpl","","        return max([lux1, lux2])","","    def enable(self):","        self.bus.write_byte_data(","                    SENSOR_ADDRESS,","                    COMMAND_BIT | REGISTER_ENABLE,","                    ENABLE_POWERON | ENABLE_AEN | ENABLE_AIEN","                    )","","    def disable(self):","        self.bus.write_byte_data(","                    SENSOR_ADDRESS,","                    COMMAND_BIT | REGISTER_ENABLE,","                    ENABLE_POWEROFF","                    )","","    def get_full_luminosity(self):","        self.enable()","        time.sleep(0.120*self.integration_time+1)","        full = self.bus.read_word_data(","                    SENSOR_ADDRESS, COMMAND_BIT | REGISTER_CHAN0_LOW","                    )","        ir = self.bus.read_word_data(","                    SENSOR_ADDRESS, COMMAND_BIT | REGISTER_CHAN1_LOW","                    )                    ","        self.disable()","        return full, ir","","    def get_luminosity(self, channel):","        full, ir = self.get_full_luminosity()","        if channel == FULLSPECTRUM:","            return full","        elif channel == INFRARED:","            return ir","        elif channel == VISIBLE:","            return full - ir","        else:","            return 0","","    def sample(self):","        full, ir = self.get_full_luminosity()","        return self.calculate_lux(full, ir)"],"stylingDirectives":[[{"start":0,"end":30,"cssClass":"pl-c"}],[{"start":0,"end":6,"cssClass":"pl-k"},{"start":7,"end":11,"cssClass":"pl-s1"}],[],[{"start":0,"end":7,"cssClass":"pl-v"},{"start":8,"end":9,"cssClass":"pl-c1"},{"start":10,"end":11,"cssClass":"pl-c1"}],[{"start":0,"end":8,"cssClass":"pl-v"},{"start":9,"end":10,"cssClass":"pl-c1"},{"start":11,"end":12,"cssClass":"pl-c1"}],[{"start":0,"end":12,"cssClass":"pl-v"},{"start":13,"end":14,"cssClass":"pl-c1"},{"start":15,"end":16,"cssClass":"pl-c1"}],[],[{"start":0,"end":4,"cssClass":"pl-v"},{"start":5,"end":6,"cssClass":"pl-c1"},{"start":7,"end":11,"cssClass":"pl-c1"}],[{"start":0,"end":7,"cssClass":"pl-v"},{"start":8,"end":9,"cssClass":"pl-c1"},{"start":10,"end":14,"cssClass":"pl-c1"}],[{"start":0,"end":11,"cssClass":"pl-v"},{"start":12,"end":13,"cssClass":"pl-c1"},{"start":14,"end":18,"cssClass":"pl-c1"}],[{"start":0,"end":9,"cssClass":"pl-v"},{"start":10,"end":11,"cssClass":"pl-c1"},{"start":12,"end":16,"cssClass":"pl-c1"}],[{"start":0,"end":8,"cssClass":"pl-v"},{"start":9,"end":10,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"}],[{"start":0,"end":9,"cssClass":"pl-v"},{"start":10,"end":11,"cssClass":"pl-c1"},{"start":12,"end":16,"cssClass":"pl-c1"}],[{"start":0,"end":14,"cssClass":"pl-v"},{"start":15,"end":16,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"}],[{"start":0,"end":15,"cssClass":"pl-v"},{"start":16,"end":17,"cssClass":"pl-c1"},{"start":18,"end":22,"cssClass":"pl-c1"}],[{"start":0,"end":10,"cssClass":"pl-v"},{"start":11,"end":12,"cssClass":"pl-c1"},{"start":13,"end":17,"cssClass":"pl-c1"}],[{"start":0,"end":11,"cssClass":"pl-v"},{"start":12,"end":13,"cssClass":"pl-c1"},{"start":14,"end":18,"cssClass":"pl-c1"}],[{"start":0,"end":13,"cssClass":"pl-v"},{"start":14,"end":15,"cssClass":"pl-c1"},{"start":16,"end":20,"cssClass":"pl-c1"}],[{"start":0,"end":6,"cssClass":"pl-v"},{"start":7,"end":8,"cssClass":"pl-c1"},{"start":9,"end":14,"cssClass":"pl-c1"}],[{"start":0,"end":9,"cssClass":"pl-v"},{"start":10,"end":11,"cssClass":"pl-c1"},{"start":12,"end":16,"cssClass":"pl-c1"}],[{"start":0,"end":9,"cssClass":"pl-v"},{"start":10,"end":11,"cssClass":"pl-c1"},{"start":12,"end":16,"cssClass":"pl-c1"}],[{"start":0,"end":9,"cssClass":"pl-v"},{"start":10,"end":11,"cssClass":"pl-c1"},{"start":12,"end":16,"cssClass":"pl-c1"}],[],[{"start":0,"end":15,"cssClass":"pl-v"},{"start":16,"end":17,"cssClass":"pl-c1"},{"start":18,"end":22,"cssClass":"pl-c1"}],[{"start":0,"end":16,"cssClass":"pl-v"},{"start":17,"end":18,"cssClass":"pl-c1"},{"start":19,"end":23,"cssClass":"pl-c1"}],[{"start":0,"end":24,"cssClass":"pl-v"},{"start":25,"end":26,"cssClass":"pl-c1"},{"start":27,"end":31,"cssClass":"pl-c1"}],[{"start":0,"end":25,"cssClass":"pl-v"},{"start":26,"end":27,"cssClass":"pl-c1"},{"start":28,"end":32,"cssClass":"pl-c1"}],[{"start":0,"end":24,"cssClass":"pl-v"},{"start":25,"end":26,"cssClass":"pl-c1"},{"start":27,"end":31,"cssClass":"pl-c1"}],[{"start":0,"end":25,"cssClass":"pl-v"},{"start":26,"end":27,"cssClass":"pl-c1"},{"start":28,"end":32,"cssClass":"pl-c1"}],[{"start":0,"end":18,"cssClass":"pl-v"},{"start":19,"end":20,"cssClass":"pl-c1"},{"start":21,"end":25,"cssClass":"pl-c1"}],[{"start":0,"end":12,"cssClass":"pl-v"},{"start":13,"end":14,"cssClass":"pl-c1"},{"start":15,"end":19,"cssClass":"pl-c1"}],[{"start":0,"end":11,"cssClass":"pl-v"},{"start":12,"end":13,"cssClass":"pl-c1"},{"start":14,"end":18,"cssClass":"pl-c1"}],[{"start":0,"end":18,"cssClass":"pl-v"},{"start":19,"end":20,"cssClass":"pl-c1"},{"start":21,"end":25,"cssClass":"pl-c1"}],[{"start":0,"end":19,"cssClass":"pl-v"},{"start":20,"end":21,"cssClass":"pl-c1"},{"start":22,"end":26,"cssClass":"pl-c1"}],[{"start":0,"end":18,"cssClass":"pl-v"},{"start":19,"end":20,"cssClass":"pl-c1"},{"start":21,"end":25,"cssClass":"pl-c1"}],[{"start":0,"end":19,"cssClass":"pl-v"},{"start":20,"end":21,"cssClass":"pl-c1"},{"start":22,"end":26,"cssClass":"pl-c1"}],[{"start":0,"end":21,"cssClass":"pl-v"},{"start":22,"end":23,"cssClass":"pl-c1"},{"start":24,"end":28,"cssClass":"pl-c1"}],[{"start":0,"end":21,"cssClass":"pl-v"},{"start":22,"end":23,"cssClass":"pl-c1"},{"start":24,"end":28,"cssClass":"pl-c1"}],[{"start":0,"end":21,"cssClass":"pl-v"},{"start":22,"end":23,"cssClass":"pl-c1"},{"start":24,"end":28,"cssClass":"pl-c1"}],[{"start":0,"end":21,"cssClass":"pl-v"},{"start":22,"end":23,"cssClass":"pl-c1"},{"start":24,"end":28,"cssClass":"pl-c1"}],[{"start":0,"end":21,"cssClass":"pl-v"},{"start":22,"end":23,"cssClass":"pl-c1"},{"start":24,"end":28,"cssClass":"pl-c1"}],[{"start":0,"end":21,"cssClass":"pl-v"},{"start":22,"end":23,"cssClass":"pl-c1"},{"start":24,"end":28,"cssClass":"pl-c1"}],[],[{"start":0,"end":8,"cssClass":"pl-v"},{"start":9,"end":10,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"}],[{"start":0,"end":8,"cssClass":"pl-v"},{"start":9,"end":10,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"}],[{"start":0,"end":9,"cssClass":"pl-v"},{"start":10,"end":11,"cssClass":"pl-c1"},{"start":12,"end":16,"cssClass":"pl-c1"}],[{"start":0,"end":8,"cssClass":"pl-v"},{"start":9,"end":10,"cssClass":"pl-c1"},{"start":11,"end":15,"cssClass":"pl-c1"}],[],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":17,"cssClass":"pl-en"},{"start":18,"end":22,"cssClass":"pl-s1"}],[{"start":4,"end":10,"cssClass":"pl-k"},{"start":11,"end":15,"cssClass":"pl-s1"},{"start":16,"end":17,"cssClass":"pl-c1"},{"start":19,"end":20,"cssClass":"pl-c1"},{"start":22,"end":26,"cssClass":"pl-s1"},{"start":27,"end":28,"cssClass":"pl-c1"},{"start":29,"end":31,"cssClass":"pl-c1"},{"start":31,"end":32,"cssClass":"pl-c1"}],[],[{"start":0,"end":4,"cssClass":"pl-k"},{"start":5,"end":12,"cssClass":"pl-s1"},{"start":13,"end":19,"cssClass":"pl-k"},{"start":20,"end":23,"cssClass":"pl-v"},{"start":25,"end":28,"cssClass":"pl-v"}],[{"start":0,"end":5,"cssClass":"pl-k"},{"start":6,"end":19,"cssClass":"pl-v"}],[{"start":4,"end":13,"cssClass":"pl-s1"},{"start":14,"end":15,"cssClass":"pl-c1"},{"start":17,"end":22,"cssClass":"pl-s"}],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":16,"cssClass":"pl-en"},{"start":17,"end":21,"cssClass":"pl-s1"},{"start":23,"end":32,"cssClass":"pl-s1"},{"start":32,"end":33,"cssClass":"pl-c1"},{"start":33,"end":34,"cssClass":"pl-c1"},{"start":36,"end":45,"cssClass":"pl-s1"},{"start":45,"end":46,"cssClass":"pl-c1"},{"start":46,"end":47,"cssClass":"pl-c1"}],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":16,"cssClass":"pl-s1"},{"start":17,"end":18,"cssClass":"pl-c1"},{"start":19,"end":22,"cssClass":"pl-v"},{"start":23,"end":26,"cssClass":"pl-s1"},{"start":26,"end":27,"cssClass":"pl-c1"},{"start":27,"end":30,"cssClass":"pl-v"},{"start":31,"end":40,"cssClass":"pl-s1"},{"start":42,"end":45,"cssClass":"pl-v"},{"start":46,"end":48,"cssClass":"pl-v"}],[{"start":23,"end":26,"cssClass":"pl-s1"},{"start":26,"end":27,"cssClass":"pl-c1"},{"start":27,"end":30,"cssClass":"pl-v"},{"start":31,"end":40,"cssClass":"pl-s1"},{"start":42,"end":45,"cssClass":"pl-v"},{"start":46,"end":48,"cssClass":"pl-v"}],[],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":23,"cssClass":"pl-en"},{"start":24,"end":28,"cssClass":"pl-s1"},{"start":30,"end":34,"cssClass":"pl-s1"},{"start":36,"end":39,"cssClass":"pl-s1"},{"start":41,"end":44,"cssClass":"pl-s1"}],[{"start":8,"end":11,"cssClass":"pl-s1"},{"start":12,"end":13,"cssClass":"pl-c1"},{"start":14,"end":19,"cssClass":"pl-en"},{"start":21,"end":24,"cssClass":"pl-s1"},{"start":26,"end":29,"cssClass":"pl-s1"}],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":16,"cssClass":"pl-s1"},{"start":17,"end":24,"cssClass":"pl-en"},{"start":25,"end":29,"cssClass":"pl-s1"},{"start":31,"end":34,"cssClass":"pl-s1"}],[],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":22,"cssClass":"pl-en"},{"start":23,"end":27,"cssClass":"pl-s1"},{"start":29,"end":33,"cssClass":"pl-s1"},{"start":35,"end":38,"cssClass":"pl-s1"}],[{"start":8,"end":14,"cssClass":"pl-k"},{"start":15,"end":18,"cssClass":"pl-s1"},{"start":19,"end":20,"cssClass":"pl-c1"},{"start":21,"end":24,"cssClass":"pl-c1"}],[{"start":8,"end":11,"cssClass":"pl-s1"},{"start":12,"end":13,"cssClass":"pl-c1"},{"start":14,"end":19,"cssClass":"pl-en"},{"start":21,"end":24,"cssClass":"pl-s1"}],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":16,"cssClass":"pl-s1"},{"start":17,"end":24,"cssClass":"pl-en"},{"start":25,"end":29,"cssClass":"pl-s1"},{"start":31,"end":34,"cssClass":"pl-s1"}],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":14,"cssClass":"pl-c1"},{"start":15,"end":19,"cssClass":"pl-s1"},{"start":20,"end":23,"cssClass":"pl-s1"},{"start":24,"end":32,"cssClass":"pl-en"},{"start":33,"end":37,"cssClass":"pl-s1"},{"start":39,"end":40,"cssClass":"pl-c1"}],[{"start":8,"end":14,"cssClass":"pl-k"},{"start":15,"end":28,"cssClass":"pl-en"},{"start":29,"end":33,"cssClass":"pl-s1"}],[],[{"start":0,"end":14,"cssClass":"pl-v"},{"start":14,"end":15,"cssClass":"pl-c1"},{"start":15,"end":19,"cssClass":"pl-c1"}],[],[{"start":0,"end":5,"cssClass":"pl-k"},{"start":6,"end":13,"cssClass":"pl-v"}],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":16,"cssClass":"pl-en"}],[{"start":17,"end":21,"cssClass":"pl-s1"}],[{"start":17,"end":26,"cssClass":"pl-s1"}],[{"start":17,"end":28,"cssClass":"pl-s1"},{"start":28,"end":29,"cssClass":"pl-c1"},{"start":29,"end":50,"cssClass":"pl-v"}],[{"start":17,"end":21,"cssClass":"pl-s1"},{"start":21,"end":22,"cssClass":"pl-c1"},{"start":22,"end":30,"cssClass":"pl-v"}],[],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":22,"cssClass":"pl-s1"},{"start":23,"end":24,"cssClass":"pl-c1"},{"start":25,"end":34,"cssClass":"pl-s1"}],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":16,"cssClass":"pl-s1"},{"start":17,"end":18,"cssClass":"pl-c1"},{"start":19,"end":32,"cssClass":"pl-v"}],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":29,"cssClass":"pl-s1"},{"start":30,"end":31,"cssClass":"pl-c1"},{"start":32,"end":43,"cssClass":"pl-s1"}],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":17,"cssClass":"pl-s1"},{"start":18,"end":19,"cssClass":"pl-c1"},{"start":20,"end":24,"cssClass":"pl-s1"}],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":23,"cssClass":"pl-en"},{"start":24,"end":28,"cssClass":"pl-s1"},{"start":29,"end":45,"cssClass":"pl-s1"}],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":21,"cssClass":"pl-en"},{"start":22,"end":26,"cssClass":"pl-s1"},{"start":27,"end":31,"cssClass":"pl-s1"}],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":20,"cssClass":"pl-en"}],[],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":18,"cssClass":"pl-en"},{"start":19,"end":23,"cssClass":"pl-s1"},{"start":25,"end":36,"cssClass":"pl-s1"}],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":19,"cssClass":"pl-en"}],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":29,"cssClass":"pl-s1"},{"start":30,"end":31,"cssClass":"pl-c1"},{"start":32,"end":43,"cssClass":"pl-s1"}],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":16,"cssClass":"pl-s1"},{"start":17,"end":32,"cssClass":"pl-en"}],[{"start":20,"end":34,"cssClass":"pl-v"}],[{"start":20,"end":31,"cssClass":"pl-v"},{"start":32,"end":33,"cssClass":"pl-c1"},{"start":34,"end":50,"cssClass":"pl-v"}],[{"start":20,"end":24,"cssClass":"pl-s1"},{"start":25,"end":41,"cssClass":"pl-s1"},{"start":42,"end":43,"cssClass":"pl-c1"},{"start":44,"end":48,"cssClass":"pl-s1"},{"start":49,"end":53,"cssClass":"pl-s1"}],[],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":20,"cssClass":"pl-en"}],[],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":16,"cssClass":"pl-en"},{"start":17,"end":21,"cssClass":"pl-s1"},{"start":23,"end":27,"cssClass":"pl-s1"}],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":19,"cssClass":"pl-en"}],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":17,"cssClass":"pl-s1"},{"start":18,"end":19,"cssClass":"pl-c1"},{"start":20,"end":24,"cssClass":"pl-s1"}],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":16,"cssClass":"pl-s1"},{"start":17,"end":32,"cssClass":"pl-en"}],[{"start":20,"end":34,"cssClass":"pl-v"}],[{"start":20,"end":31,"cssClass":"pl-v"},{"start":32,"end":33,"cssClass":"pl-c1"},{"start":34,"end":50,"cssClass":"pl-v"}],[{"start":20,"end":24,"cssClass":"pl-s1"},{"start":25,"end":41,"cssClass":"pl-s1"},{"start":42,"end":43,"cssClass":"pl-c1"},{"start":44,"end":48,"cssClass":"pl-s1"},{"start":49,"end":53,"cssClass":"pl-s1"}],[],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":20,"cssClass":"pl-en"}],[],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":21,"cssClass":"pl-en"},{"start":22,"end":26,"cssClass":"pl-s1"},{"start":28,"end":32,"cssClass":"pl-s1"},{"start":34,"end":36,"cssClass":"pl-s1"}],[{"start":8,"end":10,"cssClass":"pl-k"},{"start":12,"end":16,"cssClass":"pl-s1"},{"start":17,"end":19,"cssClass":"pl-c1"},{"start":20,"end":26,"cssClass":"pl-c1"},{"start":28,"end":29,"cssClass":"pl-c1"},{"start":31,"end":33,"cssClass":"pl-s1"},{"start":34,"end":36,"cssClass":"pl-c1"},{"start":37,"end":43,"cssClass":"pl-c1"}],[{"start":12,"end":18,"cssClass":"pl-k"},{"start":19,"end":20,"cssClass":"pl-c1"}],[],[{"start":8,"end":18,"cssClass":"pl-s1"},{"start":19,"end":20,"cssClass":"pl-c1"}],[{"start":12,"end":33,"cssClass":"pl-v"},{"start":35,"end":39,"cssClass":"pl-c1"}],[{"start":12,"end":33,"cssClass":"pl-v"},{"start":35,"end":39,"cssClass":"pl-c1"}],[{"start":12,"end":33,"cssClass":"pl-v"},{"start":35,"end":39,"cssClass":"pl-c1"}],[{"start":12,"end":33,"cssClass":"pl-v"},{"start":35,"end":39,"cssClass":"pl-c1"}],[{"start":12,"end":33,"cssClass":"pl-v"},{"start":35,"end":39,"cssClass":"pl-c1"}],[{"start":12,"end":33,"cssClass":"pl-v"},{"start":35,"end":39,"cssClass":"pl-c1"}],[],[{"start":8,"end":10,"cssClass":"pl-k"},{"start":11,"end":15,"cssClass":"pl-s1"},{"start":16,"end":32,"cssClass":"pl-s1"},{"start":33,"end":35,"cssClass":"pl-c1"},{"start":36,"end":46,"cssClass":"pl-s1"},{"start":47,"end":51,"cssClass":"pl-en"}],[{"start":12,"end":17,"cssClass":"pl-s1"},{"start":18,"end":19,"cssClass":"pl-c1"},{"start":20,"end":30,"cssClass":"pl-s1"},{"start":31,"end":35,"cssClass":"pl-s1"},{"start":36,"end":52,"cssClass":"pl-s1"}],[{"start":8,"end":12,"cssClass":"pl-k"}],[{"start":12,"end":17,"cssClass":"pl-s1"},{"start":18,"end":19,"cssClass":"pl-c1"},{"start":20,"end":24,"cssClass":"pl-c1"}],[],[{"start":8,"end":17,"cssClass":"pl-s1"},{"start":18,"end":19,"cssClass":"pl-c1"}],[{"start":12,"end":20,"cssClass":"pl-v"},{"start":22,"end":24,"cssClass":"pl-c1"}],[{"start":12,"end":20,"cssClass":"pl-v"},{"start":22,"end":25,"cssClass":"pl-c1"}],[{"start":12,"end":21,"cssClass":"pl-v"},{"start":23,"end":27,"cssClass":"pl-c1"}],[{"start":12,"end":20,"cssClass":"pl-v"},{"start":22,"end":27,"cssClass":"pl-c1"}],[],[],[{"start":8,"end":10,"cssClass":"pl-k"},{"start":11,"end":15,"cssClass":"pl-s1"},{"start":16,"end":20,"cssClass":"pl-s1"},{"start":21,"end":23,"cssClass":"pl-c1"},{"start":24,"end":33,"cssClass":"pl-s1"},{"start":34,"end":38,"cssClass":"pl-en"}],[{"start":12,"end":17,"cssClass":"pl-s1"},{"start":18,"end":19,"cssClass":"pl-c1"},{"start":20,"end":29,"cssClass":"pl-s1"},{"start":30,"end":34,"cssClass":"pl-s1"},{"start":35,"end":39,"cssClass":"pl-s1"}],[{"start":8,"end":12,"cssClass":"pl-k"}],[{"start":12,"end":17,"cssClass":"pl-s1"},{"start":18,"end":19,"cssClass":"pl-c1"},{"start":20,"end":22,"cssClass":"pl-c1"}],[],[{"start":8,"end":11,"cssClass":"pl-s1"},{"start":12,"end":13,"cssClass":"pl-c1"},{"start":15,"end":20,"cssClass":"pl-s1"},{"start":21,"end":22,"cssClass":"pl-c1"},{"start":23,"end":28,"cssClass":"pl-s1"},{"start":30,"end":31,"cssClass":"pl-c1"},{"start":32,"end":38,"cssClass":"pl-v"}],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":14,"cssClass":"pl-c1"},{"start":16,"end":20,"cssClass":"pl-s1"},{"start":21,"end":22,"cssClass":"pl-c1"},{"start":24,"end":33,"cssClass":"pl-v"},{"start":34,"end":35,"cssClass":"pl-c1"},{"start":36,"end":38,"cssClass":"pl-s1"},{"start":41,"end":42,"cssClass":"pl-c1"},{"start":43,"end":46,"cssClass":"pl-s1"}],[],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":14,"cssClass":"pl-c1"},{"start":17,"end":26,"cssClass":"pl-v"},{"start":27,"end":28,"cssClass":"pl-c1"},{"start":29,"end":33,"cssClass":"pl-s1"},{"start":35,"end":36,"cssClass":"pl-c1"},{"start":38,"end":47,"cssClass":"pl-v"},{"start":48,"end":49,"cssClass":"pl-c1"},{"start":50,"end":52,"cssClass":"pl-s1"},{"start":55,"end":56,"cssClass":"pl-c1"},{"start":57,"end":60,"cssClass":"pl-s1"}],[],[{"start":8,"end":14,"cssClass":"pl-k"},{"start":15,"end":18,"cssClass":"pl-en"},{"start":20,"end":24,"cssClass":"pl-s1"},{"start":26,"end":30,"cssClass":"pl-s1"}],[],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":14,"cssClass":"pl-en"},{"start":15,"end":19,"cssClass":"pl-s1"}],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":16,"cssClass":"pl-s1"},{"start":17,"end":32,"cssClass":"pl-en"}],[{"start":20,"end":34,"cssClass":"pl-v"}],[{"start":20,"end":31,"cssClass":"pl-v"},{"start":32,"end":33,"cssClass":"pl-c1"},{"start":34,"end":49,"cssClass":"pl-v"}],[{"start":20,"end":34,"cssClass":"pl-v"},{"start":35,"end":36,"cssClass":"pl-c1"},{"start":37,"end":47,"cssClass":"pl-v"},{"start":48,"end":49,"cssClass":"pl-c1"},{"start":50,"end":61,"cssClass":"pl-v"}],[],[],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":15,"cssClass":"pl-en"},{"start":16,"end":20,"cssClass":"pl-s1"}],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":16,"cssClass":"pl-s1"},{"start":17,"end":32,"cssClass":"pl-en"}],[{"start":20,"end":34,"cssClass":"pl-v"}],[{"start":20,"end":31,"cssClass":"pl-v"},{"start":32,"end":33,"cssClass":"pl-c1"},{"start":34,"end":49,"cssClass":"pl-v"}],[{"start":20,"end":35,"cssClass":"pl-v"}],[],[],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":27,"cssClass":"pl-en"},{"start":28,"end":32,"cssClass":"pl-s1"}],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":19,"cssClass":"pl-en"}],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":18,"cssClass":"pl-en"},{"start":19,"end":24,"cssClass":"pl-c1"},{"start":24,"end":25,"cssClass":"pl-c1"},{"start":25,"end":29,"cssClass":"pl-s1"},{"start":30,"end":46,"cssClass":"pl-s1"},{"start":46,"end":47,"cssClass":"pl-c1"},{"start":47,"end":48,"cssClass":"pl-c1"}],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":14,"cssClass":"pl-c1"},{"start":15,"end":19,"cssClass":"pl-s1"},{"start":20,"end":23,"cssClass":"pl-s1"},{"start":24,"end":38,"cssClass":"pl-en"}],[{"start":20,"end":34,"cssClass":"pl-v"},{"start":36,"end":47,"cssClass":"pl-v"},{"start":48,"end":49,"cssClass":"pl-c1"},{"start":50,"end":68,"cssClass":"pl-v"}],[],[{"start":8,"end":10,"cssClass":"pl-s1"},{"start":11,"end":12,"cssClass":"pl-c1"},{"start":13,"end":17,"cssClass":"pl-s1"},{"start":18,"end":21,"cssClass":"pl-s1"},{"start":22,"end":36,"cssClass":"pl-en"}],[{"start":20,"end":34,"cssClass":"pl-v"},{"start":36,"end":47,"cssClass":"pl-v"},{"start":48,"end":49,"cssClass":"pl-c1"},{"start":50,"end":68,"cssClass":"pl-v"}],[],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":20,"cssClass":"pl-en"}],[{"start":8,"end":14,"cssClass":"pl-k"},{"start":15,"end":19,"cssClass":"pl-s1"},{"start":21,"end":23,"cssClass":"pl-s1"}],[],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":22,"cssClass":"pl-en"},{"start":23,"end":27,"cssClass":"pl-s1"},{"start":29,"end":36,"cssClass":"pl-s1"}],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":14,"end":16,"cssClass":"pl-s1"},{"start":17,"end":18,"cssClass":"pl-c1"},{"start":19,"end":23,"cssClass":"pl-s1"},{"start":24,"end":43,"cssClass":"pl-en"}],[{"start":8,"end":10,"cssClass":"pl-k"},{"start":11,"end":18,"cssClass":"pl-s1"},{"start":19,"end":21,"cssClass":"pl-c1"},{"start":22,"end":34,"cssClass":"pl-v"}],[{"start":12,"end":18,"cssClass":"pl-k"},{"start":19,"end":23,"cssClass":"pl-s1"}],[{"start":8,"end":12,"cssClass":"pl-k"},{"start":13,"end":20,"cssClass":"pl-s1"},{"start":21,"end":23,"cssClass":"pl-c1"},{"start":24,"end":32,"cssClass":"pl-v"}],[{"start":12,"end":18,"cssClass":"pl-k"},{"start":19,"end":21,"cssClass":"pl-s1"}],[{"start":8,"end":12,"cssClass":"pl-k"},{"start":13,"end":20,"cssClass":"pl-s1"},{"start":21,"end":23,"cssClass":"pl-c1"},{"start":24,"end":31,"cssClass":"pl-v"}],[{"start":12,"end":18,"cssClass":"pl-k"},{"start":19,"end":23,"cssClass":"pl-s1"},{"start":24,"end":25,"cssClass":"pl-c1"},{"start":26,"end":28,"cssClass":"pl-s1"}],[{"start":8,"end":12,"cssClass":"pl-k"}],[{"start":12,"end":18,"cssClass":"pl-k"},{"start":19,"end":20,"cssClass":"pl-c1"}],[],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":14,"cssClass":"pl-en"},{"start":15,"end":19,"cssClass":"pl-s1"}],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":14,"end":16,"cssClass":"pl-s1"},{"start":17,"end":18,"cssClass":"pl-c1"},{"start":19,"end":23,"cssClass":"pl-s1"},{"start":24,"end":43,"cssClass":"pl-en"}],[{"start":8,"end":14,"cssClass":"pl-k"},{"start":15,"end":19,"cssClass":"pl-s1"},{"start":20,"end":33,"cssClass":"pl-en"},{"start":34,"end":38,"cssClass":"pl-s1"},{"start":40,"end":42,"cssClass":"pl-s1"}],[]],"csv":null,"csvError":null,"dependabotInfo":{"showConfigurationBanner":false,"configFilePath":null,"networkDependabotPath":"/jfischer/micropython-tsl2591/network/updates","dismissConfigurationNoticePath":"/settings/dismiss-notice/dependabot_configuration_notice","configurationNoticeDismissed":null,"repoAlertsPath":"/jfischer/micropython-tsl2591/security/dependabot","repoSecurityAndAnalysisPath":"/jfischer/micropython-tsl2591/settings/security_analysis","repoOwnerIsOrg":false,"currentUserCanAdminRepo":false},"displayName":"tsl2591.py","displayUrl":"https://github.com/jfischer/micropython-tsl2591/blob/master/tsl2591.py?raw=true","headerInfo":{"blobSize":"4.8 KB","deleteInfo":{"deleteTooltip":"You must be signed in to make or propose changes"},"editInfo":{"editTooltip":"You must be signed in to make or propose changes"},"ghDesktopPath":"https://desktop.github.com","gitLfsPath":null,"onBranch":true,"shortPath":"d355a26","siteNavLoginPath":"/login?return_to=https%3A%2F%2Fgithub.com%2Fjfischer%2Fmicropython-tsl2591%2Fblob%2Fmaster%2Ftsl2591.py","isCSV":false,"isRichtext":false,"toc":null,"lineInfo":{"truncatedLoc":"183","truncatedSloc":"158"},"mode":"file"},"image":false,"isCodeownersFile":null,"isPlain":false,"isValidLegacyIssueTemplate":false,"issueTemplateHelpUrl":"https://docs.github.com/articles/about-issue-and-pull-request-templates","issueTemplate":null,"discussionTemplate":null,"language":"Python","languageID":303,"large":false,"loggedIn":false,"newDiscussionPath":"/jfischer/micropython-tsl2591/discussions/new","newIssuePath":"/jfischer/micropython-tsl2591/issues/new","planSupportInfo":{"repoIsFork":null,"repoOwnedByCurrentUser":null,"requestFullPath":"/jfischer/micropython-tsl2591/blob/master/tsl2591.py","showFreeOrgGatedFeatureMessage":null,"showPlanSupportBanner":null,"upgradeDataAttributes":null,"upgradePath":null},"publishBannersInfo":{"dismissActionNoticePath":"/settings/dismiss-notice/publish_action_from_dockerfile","dismissStackNoticePath":"/settings/dismiss-notice/publish_stack_from_file","releasePath":"/jfischer/micropython-tsl2591/releases/new?marketplace=true","showPublishActionBanner":false,"showPublishStackBanner":false},"rawBlobUrl":"https://github.com/jfischer/micropython-tsl2591/raw/master/tsl2591.py","renderImageOrRaw":false,"richText":null,"renderedFileInfo":null,"shortPath":null,"tabSize":8,"topBannersInfo":{"overridingGlobalFundingFile":false,"globalPreferredFundingPath":null,"repoOwner":"jfischer","repoName":"micropython-tsl2591","showInvalidCitationWarning":false,"citationHelpUrl":"https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-citation-files","showDependabotConfigurationBanner":false,"actionsOnboardingTip":null},"truncated":false,"viewable":true,"workflowRedirectUrl":null,"symbols":{"timed_out":false,"not_analyzed":false,"symbols":[{"name":"VISIBLE","kind":"constant","ident_start":44,"ident_end":51,"extent_start":44,"extent_end":55,"fully_qualified_name":"VISIBLE","ident_utf16":{"start":{"line_number":3,"utf16_col":0},"end":{"line_number":3,"utf16_col":7}},"extent_utf16":{"start":{"line_number":3,"utf16_col":0},"end":{"line_number":3,"utf16_col":11}}},{"name":"INFRARED","kind":"constant","ident_start":56,"ident_end":64,"extent_start":56,"extent_end":68,"fully_qualified_name":"INFRARED","ident_utf16":{"start":{"line_number":4,"utf16_col":0},"end":{"line_number":4,"utf16_col":8}},"extent_utf16":{"start":{"line_number":4,"utf16_col":0},"end":{"line_number":4,"utf16_col":12}}},{"name":"FULLSPECTRUM","kind":"constant","ident_start":69,"ident_end":81,"extent_start":69,"extent_end":85,"fully_qualified_name":"FULLSPECTRUM","ident_utf16":{"start":{"line_number":5,"utf16_col":0},"end":{"line_number":5,"utf16_col":12}},"extent_utf16":{"start":{"line_number":5,"utf16_col":0},"end":{"line_number":5,"utf16_col":16}}},{"name":"ADDR","kind":"constant","ident_start":87,"ident_end":91,"extent_start":87,"extent_end":98,"fully_qualified_name":"ADDR","ident_utf16":{"start":{"line_number":7,"utf16_col":0},"end":{"line_number":7,"utf16_col":4}},"extent_utf16":{"start":{"line_number":7,"utf16_col":0},"end":{"line_number":7,"utf16_col":11}}},{"name":"READBIT","kind":"constant","ident_start":99,"ident_end":106,"extent_start":99,"extent_end":113,"fully_qualified_name":"READBIT","ident_utf16":{"start":{"line_number":8,"utf16_col":0},"end":{"line_number":8,"utf16_col":7}},"extent_utf16":{"start":{"line_number":8,"utf16_col":0},"end":{"line_number":8,"utf16_col":14}}},{"name":"COMMAND_BIT","kind":"constant","ident_start":114,"ident_end":125,"extent_start":114,"extent_end":132,"fully_qualified_name":"COMMAND_BIT","ident_utf16":{"start":{"line_number":9,"utf16_col":0},"end":{"line_number":9,"utf16_col":11}},"extent_utf16":{"start":{"line_number":9,"utf16_col":0},"end":{"line_number":9,"utf16_col":18}}},{"name":"CLEAR_BIT","kind":"constant","ident_start":133,"ident_end":142,"extent_start":133,"extent_end":149,"fully_qualified_name":"CLEAR_BIT","ident_utf16":{"start":{"line_number":10,"utf16_col":0},"end":{"line_number":10,"utf16_col":9}},"extent_utf16":{"start":{"line_number":10,"utf16_col":0},"end":{"line_number":10,"utf16_col":16}}},{"name":"WORD_BIT","kind":"constant","ident_start":150,"ident_end":158,"extent_start":150,"extent_end":165,"fully_qualified_name":"WORD_BIT","ident_utf16":{"start":{"line_number":11,"utf16_col":0},"end":{"line_number":11,"utf16_col":8}},"extent_utf16":{"start":{"line_number":11,"utf16_col":0},"end":{"line_number":11,"utf16_col":15}}},{"name":"BLOCK_BIT","kind":"constant","ident_start":166,"ident_end":175,"extent_start":166,"extent_end":182,"fully_qualified_name":"BLOCK_BIT","ident_utf16":{"start":{"line_number":12,"utf16_col":0},"end":{"line_number":12,"utf16_col":9}},"extent_utf16":{"start":{"line_number":12,"utf16_col":0},"end":{"line_number":12,"utf16_col":16}}},{"name":"ENABLE_POWERON","kind":"constant","ident_start":183,"ident_end":197,"extent_start":183,"extent_end":204,"fully_qualified_name":"ENABLE_POWERON","ident_utf16":{"start":{"line_number":13,"utf16_col":0},"end":{"line_number":13,"utf16_col":14}},"extent_utf16":{"start":{"line_number":13,"utf16_col":0},"end":{"line_number":13,"utf16_col":21}}},{"name":"ENABLE_POWEROFF","kind":"constant","ident_start":205,"ident_end":220,"extent_start":205,"extent_end":227,"fully_qualified_name":"ENABLE_POWEROFF","ident_utf16":{"start":{"line_number":14,"utf16_col":0},"end":{"line_number":14,"utf16_col":15}},"extent_utf16":{"start":{"line_number":14,"utf16_col":0},"end":{"line_number":14,"utf16_col":22}}},{"name":"ENABLE_AEN","kind":"constant","ident_start":228,"ident_end":238,"extent_start":228,"extent_end":245,"fully_qualified_name":"ENABLE_AEN","ident_utf16":{"start":{"line_number":15,"utf16_col":0},"end":{"line_number":15,"utf16_col":10}},"extent_utf16":{"start":{"line_number":15,"utf16_col":0},"end":{"line_number":15,"utf16_col":17}}},{"name":"ENABLE_AIEN","kind":"constant","ident_start":246,"ident_end":257,"extent_start":246,"extent_end":264,"fully_qualified_name":"ENABLE_AIEN","ident_utf16":{"start":{"line_number":16,"utf16_col":0},"end":{"line_number":16,"utf16_col":11}},"extent_utf16":{"start":{"line_number":16,"utf16_col":0},"end":{"line_number":16,"utf16_col":18}}},{"name":"CONTROL_RESET","kind":"constant","ident_start":265,"ident_end":278,"extent_start":265,"extent_end":285,"fully_qualified_name":"CONTROL_RESET","ident_utf16":{"start":{"line_number":17,"utf16_col":0},"end":{"line_number":17,"utf16_col":13}},"extent_utf16":{"start":{"line_number":17,"utf16_col":0},"end":{"line_number":17,"utf16_col":20}}},{"name":"LUX_DF","kind":"constant","ident_start":286,"ident_end":292,"extent_start":286,"extent_end":300,"fully_qualified_name":"LUX_DF","ident_utf16":{"start":{"line_number":18,"utf16_col":0},"end":{"line_number":18,"utf16_col":6}},"extent_utf16":{"start":{"line_number":18,"utf16_col":0},"end":{"line_number":18,"utf16_col":14}}},{"name":"LUX_COEFB","kind":"constant","ident_start":301,"ident_end":310,"extent_start":301,"extent_end":317,"fully_qualified_name":"LUX_COEFB","ident_utf16":{"start":{"line_number":19,"utf16_col":0},"end":{"line_number":19,"utf16_col":9}},"extent_utf16":{"start":{"line_number":19,"utf16_col":0},"end":{"line_number":19,"utf16_col":16}}},{"name":"LUX_COEFC","kind":"constant","ident_start":318,"ident_end":327,"extent_start":318,"extent_end":334,"fully_qualified_name":"LUX_COEFC","ident_utf16":{"start":{"line_number":20,"utf16_col":0},"end":{"line_number":20,"utf16_col":9}},"extent_utf16":{"start":{"line_number":20,"utf16_col":0},"end":{"line_number":20,"utf16_col":16}}},{"name":"LUX_COEFD","kind":"constant","ident_start":335,"ident_end":344,"extent_start":335,"extent_end":351,"fully_qualified_name":"LUX_COEFD","ident_utf16":{"start":{"line_number":21,"utf16_col":0},"end":{"line_number":21,"utf16_col":9}},"extent_utf16":{"start":{"line_number":21,"utf16_col":0},"end":{"line_number":21,"utf16_col":16}}},{"name":"REGISTER_ENABLE","kind":"constant","ident_start":353,"ident_end":368,"extent_start":353,"extent_end":375,"fully_qualified_name":"REGISTER_ENABLE","ident_utf16":{"start":{"line_number":23,"utf16_col":0},"end":{"line_number":23,"utf16_col":15}},"extent_utf16":{"start":{"line_number":23,"utf16_col":0},"end":{"line_number":23,"utf16_col":22}}},{"name":"REGISTER_CONTROL","kind":"constant","ident_start":376,"ident_end":392,"extent_start":376,"extent_end":399,"fully_qualified_name":"REGISTER_CONTROL","ident_utf16":{"start":{"line_number":24,"utf16_col":0},"end":{"line_number":24,"utf16_col":16}},"extent_utf16":{"start":{"line_number":24,"utf16_col":0},"end":{"line_number":24,"utf16_col":23}}},{"name":"REGISTER_THRESHHOLDL_LOW","kind":"constant","ident_start":400,"ident_end":424,"extent_start":400,"extent_end":431,"fully_qualified_name":"REGISTER_THRESHHOLDL_LOW","ident_utf16":{"start":{"line_number":25,"utf16_col":0},"end":{"line_number":25,"utf16_col":24}},"extent_utf16":{"start":{"line_number":25,"utf16_col":0},"end":{"line_number":25,"utf16_col":31}}},{"name":"REGISTER_THRESHHOLDL_HIGH","kind":"constant","ident_start":432,"ident_end":457,"extent_start":432,"extent_end":464,"fully_qualified_name":"REGISTER_THRESHHOLDL_HIGH","ident_utf16":{"start":{"line_number":26,"utf16_col":0},"end":{"line_number":26,"utf16_col":25}},"extent_utf16":{"start":{"line_number":26,"utf16_col":0},"end":{"line_number":26,"utf16_col":32}}},{"name":"REGISTER_THRESHHOLDH_LOW","kind":"constant","ident_start":465,"ident_end":489,"extent_start":465,"extent_end":496,"fully_qualified_name":"REGISTER_THRESHHOLDH_LOW","ident_utf16":{"start":{"line_number":27,"utf16_col":0},"end":{"line_number":27,"utf16_col":24}},"extent_utf16":{"start":{"line_number":27,"utf16_col":0},"end":{"line_number":27,"utf16_col":31}}},{"name":"REGISTER_THRESHHOLDH_HIGH","kind":"constant","ident_start":497,"ident_end":522,"extent_start":497,"extent_end":529,"fully_qualified_name":"REGISTER_THRESHHOLDH_HIGH","ident_utf16":{"start":{"line_number":28,"utf16_col":0},"end":{"line_number":28,"utf16_col":25}},"extent_utf16":{"start":{"line_number":28,"utf16_col":0},"end":{"line_number":28,"utf16_col":32}}},{"name":"REGISTER_INTERRUPT","kind":"constant","ident_start":530,"ident_end":548,"extent_start":530,"extent_end":555,"fully_qualified_name":"REGISTER_INTERRUPT","ident_utf16":{"start":{"line_number":29,"utf16_col":0},"end":{"line_number":29,"utf16_col":18}},"extent_utf16":{"start":{"line_number":29,"utf16_col":0},"end":{"line_number":29,"utf16_col":25}}},{"name":"REGISTER_CRC","kind":"constant","ident_start":556,"ident_end":568,"extent_start":556,"extent_end":575,"fully_qualified_name":"REGISTER_CRC","ident_utf16":{"start":{"line_number":30,"utf16_col":0},"end":{"line_number":30,"utf16_col":12}},"extent_utf16":{"start":{"line_number":30,"utf16_col":0},"end":{"line_number":30,"utf16_col":19}}},{"name":"REGISTER_ID","kind":"constant","ident_start":576,"ident_end":587,"extent_start":576,"extent_end":594,"fully_qualified_name":"REGISTER_ID","ident_utf16":{"start":{"line_number":31,"utf16_col":0},"end":{"line_number":31,"utf16_col":11}},"extent_utf16":{"start":{"line_number":31,"utf16_col":0},"end":{"line_number":31,"utf16_col":18}}},{"name":"REGISTER_CHAN0_LOW","kind":"constant","ident_start":595,"ident_end":613,"extent_start":595,"extent_end":620,"fully_qualified_name":"REGISTER_CHAN0_LOW","ident_utf16":{"start":{"line_number":32,"utf16_col":0},"end":{"line_number":32,"utf16_col":18}},"extent_utf16":{"start":{"line_number":32,"utf16_col":0},"end":{"line_number":32,"utf16_col":25}}},{"name":"REGISTER_CHAN0_HIGH","kind":"constant","ident_start":621,"ident_end":640,"extent_start":621,"extent_end":647,"fully_qualified_name":"REGISTER_CHAN0_HIGH","ident_utf16":{"start":{"line_number":33,"utf16_col":0},"end":{"line_number":33,"utf16_col":19}},"extent_utf16":{"start":{"line_number":33,"utf16_col":0},"end":{"line_number":33,"utf16_col":26}}},{"name":"REGISTER_CHAN1_LOW","kind":"constant","ident_start":648,"ident_end":666,"extent_start":648,"extent_end":673,"fully_qualified_name":"REGISTER_CHAN1_LOW","ident_utf16":{"start":{"line_number":34,"utf16_col":0},"end":{"line_number":34,"utf16_col":18}},"extent_utf16":{"start":{"line_number":34,"utf16_col":0},"end":{"line_number":34,"utf16_col":25}}},{"name":"REGISTER_CHAN1_HIGH","kind":"constant","ident_start":674,"ident_end":693,"extent_start":674,"extent_end":700,"fully_qualified_name":"REGISTER_CHAN1_HIGH","ident_utf16":{"start":{"line_number":35,"utf16_col":0},"end":{"line_number":35,"utf16_col":19}},"extent_utf16":{"start":{"line_number":35,"utf16_col":0},"end":{"line_number":35,"utf16_col":26}}},{"name":"INTEGRATIONTIME_100MS","kind":"constant","ident_start":701,"ident_end":722,"extent_start":701,"extent_end":729,"fully_qualified_name":"INTEGRATIONTIME_100MS","ident_utf16":{"start":{"line_number":36,"utf16_col":0},"end":{"line_number":36,"utf16_col":21}},"extent_utf16":{"start":{"line_number":36,"utf16_col":0},"end":{"line_number":36,"utf16_col":28}}},{"name":"INTEGRATIONTIME_200MS","kind":"constant","ident_start":730,"ident_end":751,"extent_start":730,"extent_end":758,"fully_qualified_name":"INTEGRATIONTIME_200MS","ident_utf16":{"start":{"line_number":37,"utf16_col":0},"end":{"line_number":37,"utf16_col":21}},"extent_utf16":{"start":{"line_number":37,"utf16_col":0},"end":{"line_number":37,"utf16_col":28}}},{"name":"INTEGRATIONTIME_300MS","kind":"constant","ident_start":759,"ident_end":780,"extent_start":759,"extent_end":787,"fully_qualified_name":"INTEGRATIONTIME_300MS","ident_utf16":{"start":{"line_number":38,"utf16_col":0},"end":{"line_number":38,"utf16_col":21}},"extent_utf16":{"start":{"line_number":38,"utf16_col":0},"end":{"line_number":38,"utf16_col":28}}},{"name":"INTEGRATIONTIME_400MS","kind":"constant","ident_start":788,"ident_end":809,"extent_start":788,"extent_end":816,"fully_qualified_name":"INTEGRATIONTIME_400MS","ident_utf16":{"start":{"line_number":39,"utf16_col":0},"end":{"line_number":39,"utf16_col":21}},"extent_utf16":{"start":{"line_number":39,"utf16_col":0},"end":{"line_number":39,"utf16_col":28}}},{"name":"INTEGRATIONTIME_500MS","kind":"constant","ident_start":817,"ident_end":838,"extent_start":817,"extent_end":845,"fully_qualified_name":"INTEGRATIONTIME_500MS","ident_utf16":{"start":{"line_number":40,"utf16_col":0},"end":{"line_number":40,"utf16_col":21}},"extent_utf16":{"start":{"line_number":40,"utf16_col":0},"end":{"line_number":40,"utf16_col":28}}},{"name":"INTEGRATIONTIME_600MS","kind":"constant","ident_start":846,"ident_end":867,"extent_start":846,"extent_end":874,"fully_qualified_name":"INTEGRATIONTIME_600MS","ident_utf16":{"start":{"line_number":41,"utf16_col":0},"end":{"line_number":41,"utf16_col":21}},"extent_utf16":{"start":{"line_number":41,"utf16_col":0},"end":{"line_number":41,"utf16_col":28}}},{"name":"GAIN_LOW","kind":"constant","ident_start":876,"ident_end":884,"extent_start":876,"extent_end":891,"fully_qualified_name":"GAIN_LOW","ident_utf16":{"start":{"line_number":43,"utf16_col":0},"end":{"line_number":43,"utf16_col":8}},"extent_utf16":{"start":{"line_number":43,"utf16_col":0},"end":{"line_number":43,"utf16_col":15}}},{"name":"GAIN_MED","kind":"constant","ident_start":892,"ident_end":900,"extent_start":892,"extent_end":907,"fully_qualified_name":"GAIN_MED","ident_utf16":{"start":{"line_number":44,"utf16_col":0},"end":{"line_number":44,"utf16_col":8}},"extent_utf16":{"start":{"line_number":44,"utf16_col":0},"end":{"line_number":44,"utf16_col":15}}},{"name":"GAIN_HIGH","kind":"constant","ident_start":908,"ident_end":917,"extent_start":908,"extent_end":924,"fully_qualified_name":"GAIN_HIGH","ident_utf16":{"start":{"line_number":45,"utf16_col":0},"end":{"line_number":45,"utf16_col":9}},"extent_utf16":{"start":{"line_number":45,"utf16_col":0},"end":{"line_number":45,"utf16_col":16}}},{"name":"GAIN_MAX","kind":"constant","ident_start":925,"ident_end":933,"extent_start":925,"extent_end":940,"fully_qualified_name":"GAIN_MAX","ident_utf16":{"start":{"line_number":46,"utf16_col":0},"end":{"line_number":46,"utf16_col":8}},"extent_utf16":{"start":{"line_number":46,"utf16_col":0},"end":{"line_number":46,"utf16_col":15}}},{"name":"_bytes_to_int","kind":"function","ident_start":946,"ident_end":959,"extent_start":942,"extent_end":1000,"fully_qualified_name":"_bytes_to_int","ident_utf16":{"start":{"line_number":48,"utf16_col":4},"end":{"line_number":48,"utf16_col":17}},"extent_utf16":{"start":{"line_number":48,"utf16_col":0},"end":{"line_number":49,"utf16_col":33}}},{"name":"SMBusEmulator","kind":"class","ident_start":1037,"ident_end":1050,"extent_start":1031,"extent_end":1551,"fully_qualified_name":"SMBusEmulator","ident_utf16":{"start":{"line_number":52,"utf16_col":6},"end":{"line_number":52,"utf16_col":19}},"extent_utf16":{"start":{"line_number":52,"utf16_col":0},"end":{"line_number":67,"utf16_col":34}}},{"name":"__slots__","kind":"constant","ident_start":1056,"ident_end":1065,"extent_start":1056,"extent_end":1076,"fully_qualified_name":"SMBusEmulator.__slots__","ident_utf16":{"start":{"line_number":53,"utf16_col":4},"end":{"line_number":53,"utf16_col":13}},"extent_utf16":{"start":{"line_number":53,"utf16_col":4},"end":{"line_number":53,"utf16_col":24}}},{"name":"__init__","kind":"function","ident_start":1085,"ident_end":1093,"extent_start":1081,"extent_end":1228,"fully_qualified_name":"SMBusEmulator.__init__","ident_utf16":{"start":{"line_number":54,"utf16_col":8},"end":{"line_number":54,"utf16_col":16}},"extent_utf16":{"start":{"line_number":54,"utf16_col":4},"end":{"line_number":56,"utf16_col":50}}},{"name":"write_byte_data","kind":"function","ident_start":1238,"ident_end":1253,"extent_start":1234,"extent_end":1344,"fully_qualified_name":"SMBusEmulator.write_byte_data","ident_utf16":{"start":{"line_number":58,"utf16_col":8},"end":{"line_number":58,"utf16_col":23}},"extent_utf16":{"start":{"line_number":58,"utf16_col":4},"end":{"line_number":60,"utf16_col":35}}},{"name":"read_word_data","kind":"function","ident_start":1354,"ident_end":1368,"extent_start":1350,"extent_end":1551,"fully_qualified_name":"SMBusEmulator.read_word_data","ident_utf16":{"start":{"line_number":62,"utf16_col":8},"end":{"line_number":62,"utf16_col":22}},"extent_utf16":{"start":{"line_number":62,"utf16_col":4},"end":{"line_number":67,"utf16_col":34}}},{"name":"SENSOR_ADDRESS","kind":"constant","ident_start":1553,"ident_end":1567,"extent_start":1553,"extent_end":1572,"fully_qualified_name":"SENSOR_ADDRESS","ident_utf16":{"start":{"line_number":69,"utf16_col":0},"end":{"line_number":69,"utf16_col":14}},"extent_utf16":{"start":{"line_number":69,"utf16_col":0},"end":{"line_number":69,"utf16_col":19}}},{"name":"Tsl2591","kind":"class","ident_start":1580,"ident_end":1587,"extent_start":1574,"extent_end":4909,"fully_qualified_name":"Tsl2591","ident_utf16":{"start":{"line_number":71,"utf16_col":6},"end":{"line_number":71,"utf16_col":13}},"extent_utf16":{"start":{"line_number":71,"utf16_col":0},"end":{"line_number":181,"utf16_col":43}}},{"name":"__init__","kind":"function","ident_start":1597,"ident_end":1605,"extent_start":1593,"extent_end":2002,"fully_qualified_name":"Tsl2591.__init__","ident_utf16":{"start":{"line_number":72,"utf16_col":8},"end":{"line_number":72,"utf16_col":16}},"extent_utf16":{"start":{"line_number":72,"utf16_col":4},"end":{"line_number":84,"utf16_col":22}}},{"name":"set_timing","kind":"function","ident_start":2012,"ident_end":2022,"extent_start":2008,"extent_end":2329,"fully_qualified_name":"Tsl2591.set_timing","ident_utf16":{"start":{"line_number":86,"utf16_col":8},"end":{"line_number":86,"utf16_col":18}},"extent_utf16":{"start":{"line_number":86,"utf16_col":4},"end":{"line_number":94,"utf16_col":22}}},{"name":"set_gain","kind":"function","ident_start":2339,"ident_end":2347,"extent_start":2335,"extent_end":2628,"fully_qualified_name":"Tsl2591.set_gain","ident_utf16":{"start":{"line_number":96,"utf16_col":8},"end":{"line_number":96,"utf16_col":16}},"extent_utf16":{"start":{"line_number":96,"utf16_col":4},"end":{"line_number":104,"utf16_col":22}}},{"name":"calculate_lux","kind":"function","ident_start":2638,"ident_end":2651,"extent_start":2634,"extent_end":3631,"fully_qualified_name":"Tsl2591.calculate_lux","ident_utf16":{"start":{"line_number":106,"utf16_col":8},"end":{"line_number":106,"utf16_col":21}},"extent_utf16":{"start":{"line_number":106,"utf16_col":4},"end":{"line_number":140,"utf16_col":32}}},{"name":"enable","kind":"function","ident_start":3641,"ident_end":3647,"extent_start":3637,"extent_end":3859,"fully_qualified_name":"Tsl2591.enable","ident_utf16":{"start":{"line_number":142,"utf16_col":8},"end":{"line_number":142,"utf16_col":14}},"extent_utf16":{"start":{"line_number":142,"utf16_col":4},"end":{"line_number":147,"utf16_col":21}}},{"name":"disable","kind":"function","ident_start":3869,"ident_end":3876,"extent_start":3865,"extent_end":4062,"fully_qualified_name":"Tsl2591.disable","ident_utf16":{"start":{"line_number":149,"utf16_col":8},"end":{"line_number":149,"utf16_col":15}},"extent_utf16":{"start":{"line_number":149,"utf16_col":4},"end":{"line_number":154,"utf16_col":21}}},{"name":"get_full_luminosity","kind":"function","ident_start":4072,"ident_end":4091,"extent_start":4068,"extent_end":4497,"fully_qualified_name":"Tsl2591.get_full_luminosity","ident_utf16":{"start":{"line_number":156,"utf16_col":8},"end":{"line_number":156,"utf16_col":27}},"extent_utf16":{"start":{"line_number":156,"utf16_col":4},"end":{"line_number":166,"utf16_col":23}}},{"name":"get_luminosity","kind":"function","ident_start":4507,"ident_end":4521,"extent_start":4503,"extent_end":4796,"fully_qualified_name":"Tsl2591.get_luminosity","ident_utf16":{"start":{"line_number":168,"utf16_col":8},"end":{"line_number":168,"utf16_col":22}},"extent_utf16":{"start":{"line_number":168,"utf16_col":4},"end":{"line_number":177,"utf16_col":20}}},{"name":"sample","kind":"function","ident_start":4806,"ident_end":4812,"extent_start":4802,"extent_end":4909,"fully_qualified_name":"Tsl2591.sample","ident_utf16":{"start":{"line_number":179,"utf16_col":8},"end":{"line_number":179,"utf16_col":14}},"extent_utf16":{"start":{"line_number":179,"utf16_col":4},"end":{"line_number":181,"utf16_col":43}}}]}},"copilotInfo":null,"copilotAccessAllowed":false,"csrf_tokens":{"/jfischer/micropython-tsl2591/branches":{"post":"WBdc6mXBcmIWWmL9z8sC3RS1A1K1tDHgJ-ZunY5W4wWXJ54F6GxD28qgAdpUjyoLo-GAL99Wyp1-ilahID--Sg"},"/repos/preferences":{"post":"ZzaeieghL6BaBoSmad20u1lgl8vIb96emR9KWS3RUao7iXmZZyIazp0fRk99t_IUUkAfsBcpBqA6XL7SK7PMEA"}}},"title":"micropython-tsl2591/tsl2591.py at master · jfischer/micropython-tsl2591","appPayload":{"helpUrl":"https://docs.github.com","findFileWorkerPath":"/assets-cdn/worker/find-file-worker-32bb159cc57c.js","findInFileWorkerPath":"/assets-cdn/worker/find-in-file-worker-c6704d501c10.js","githubDevUrl":null,"enabled_features":{"code_nav_ui_events":false,"copilot_conversational_ux":false,"copilot_conversational_ux_embedding_update":false,"copilot_conversational_ux_streaming":true,"copilot_popover_file_editor_header":false,"copilot_smell_icebreaker_ux":false,"react_blob_snake_symbols":false}}}</script>
  <div data-target="react-app.reactRoot"></div>
</react-app>
</turbo-frame>



  </div>

</turbo-frame>

    </main>
  </div>

  </div>

          <footer class="footer p-responsive pt-8 pb-6 f6 color-fg-muted" role="contentinfo">
  <h2 class='sr-only'>Footer</h2>


  <div class="d-flex flex-justify-center flex-items-center flex-column-reverse flex-lg-row flex-wrap flex-lg-nowrap">
    <div class="d-flex flex-items-center mx-2">
      <a aria-label="Homepage" title="GitHub" class="footer-octicon mr-2" href="https://github.com">
        <svg aria-hidden="true" height="24" viewBox="0 0 16 16" version="1.1" width="24" data-view-component="true" class="octicon octicon-mark-github">
    <path d="M8 0c4.42 0 8 3.58 8 8a8.013 8.013 0 0 1-5.45 7.59c-.4.08-.55-.17-.55-.38 0-.27.01-1.13.01-2.2 0-.75-.25-1.23-.54-1.48 1.78-.2 3.65-.88 3.65-3.95 0-.88-.31-1.59-.82-2.15.08-.2.36-1.02-.08-2.12 0 0-.67-.22-2.2.82-.64-.18-1.32-.27-2-.27-.68 0-1.36.09-2 .27-1.53-1.03-2.2-.82-2.2-.82-.44 1.1-.16 1.92-.08 2.12-.51.56-.82 1.28-.82 2.15 0 3.06 1.86 3.75 3.64 3.95-.23.2-.44.55-.51 1.07-.46.21-1.61.55-2.33-.66-.15-.24-.6-.83-1.23-.82-.67.01-.27.38.01.53.34.19.73.9.82 1.13.16.45.68 1.31 2.69.94 0 .67.01 1.3.01 1.49 0 .21-.15.45-.55.38A7.995 7.995 0 0 1 0 8c0-4.42 3.58-8 8-8Z"></path>
</svg>
</a>
      <span>
        &copy; 2023 GitHub, Inc.
      </span>
    </div>

    <nav aria-label="Footer">
      <h3 class="sr-only" id="sr-footer-heading">Footer navigation</h3>

      <ul class="list-style-none d-flex flex-justify-center flex-wrap mb-2 mb-lg-0" aria-labelledby="sr-footer-heading">

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to Terms&quot;,&quot;label&quot;:&quot;text:terms&quot;}" href="https://docs.github.com/site-policy/github-terms/github-terms-of-service" data-view-component="true" class="Link--secondary Link">Terms</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to privacy&quot;,&quot;label&quot;:&quot;text:privacy&quot;}" href="https://docs.github.com/site-policy/privacy-policies/github-privacy-statement" data-view-component="true" class="Link--secondary Link">Privacy</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to security&quot;,&quot;label&quot;:&quot;text:security&quot;}" href="https://github.com/security" data-view-component="true" class="Link--secondary Link">Security</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to status&quot;,&quot;label&quot;:&quot;text:status&quot;}" href="https://www.githubstatus.com/" data-view-component="true" class="Link--secondary Link">Status</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to docs&quot;,&quot;label&quot;:&quot;text:docs&quot;}" href="https://docs.github.com" data-view-component="true" class="Link--secondary Link">Docs</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to contact&quot;,&quot;label&quot;:&quot;text:contact&quot;}" href="https://support.github.com?tags=dotcom-footer" data-view-component="true" class="Link--secondary Link">Contact</a>
          </li>

          <li class="mx-2">
  <cookie-consent-link>
    <button type="button" class="Link--secondary underline-on-hover border-0 p-0 color-bg-transparent" data-action="click:cookie-consent-link#showConsentManagement">
      Manage cookies
    </button>
  </cookie-consent-link>
</li>

<li class="mx-2">
  <cookie-consent-link>
    <button type="button" class="Link--secondary underline-on-hover border-0 p-0 color-bg-transparent" data-action="click:cookie-consent-link#showConsentManagement">
      Do not share my personal information
    </button>
  </cookie-consent-link>
</li>

      </ul>
    </nav>
  </div>

</footer>




    <cookie-consent id="cookie-consent-banner" class="position-fixed bottom-0 left-0" style="z-index: 999999" data-initial-cookie-consent-allowed="" data-cookie-consent-required="true"></cookie-consent>


  <div id="ajax-error-message" class="ajax-error-message flash flash-error" hidden>
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
    <button type="button" class="flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
    </button>
    You can’t perform that action at this time.
  </div>

    <template id="site-details-dialog">
  <details class="details-reset details-overlay details-overlay-dark lh-default color-fg-default hx_rsm" open>
    <summary role="button" aria-label="Close dialog"></summary>
    <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast hx_rsm-dialog hx_rsm-modal">
      <button class="Box-btn-octicon m-0 btn-octicon position-absolute right-0 top-0" type="button" aria-label="Close dialog" data-close-dialog>
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
      </button>
      <div class="octocat-spinner my-6 js-details-dialog-spinner"></div>
    </details-dialog>
  </details>
</template>

    <div class="Popover js-hovercard-content position-absolute" style="display: none; outline: none;" tabindex="0">
  <div class="Popover-message Popover-message--bottom-left Popover-message--large Box color-shadow-large" style="width:360px;">
  </div>
</div>

    <template id="snippet-clipboard-copy-button">
  <div class="zeroclipboard-container position-absolute right-0 top-0">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn js-clipboard-copy m-2 p-0 tooltipped-no-delay" data-copy-feedback="Copied!" data-tooltip-direction="w">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon m-2">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none m-2">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div>
</template>
<template id="snippet-clipboard-copy-button-unpositioned">
  <div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 tooltipped-no-delay d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div>
</template>




    </div>

    <div id="js-global-screen-reader-notice" class="sr-only" aria-live="polite" aria-atomic="true" ></div>
    <div id="js-global-screen-reader-notice-assertive" class="sr-only" aria-live="assertive" aria-atomic="true"></div>
  </body>
</html>

