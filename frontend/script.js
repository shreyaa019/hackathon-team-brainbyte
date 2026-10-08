/* ==========================================================================
   MYSURU RAILWAY JUNCTION SMART NAVIGATION SYSTEM
   Multilingual, Accessible, Interactive Station Indoor Guide & Reroute Engine
   ========================================================================== */

// --------------------------------------------------------------------------
// 1. MULTILINGUAL TRANSLATION DICTIONARY
// --------------------------------------------------------------------------
const i18n = {
  en: {
    appTitle: "Mysuru Junction Smart Navigation",
    appSubtitle: "Mysuru Junction (MYS) • Indian Railways",
    disclaimerBadge: "DEMO PROTOTYPE",
    disclaimerText: "Conceptual station map. Facility positions and routes require on-site verification.",
    tabHome: "Home",
    tabMap: "Navigation & Map",
    tabFacilities: "Nearby Facilities",
    tabHelp: "Staff Assistance",
    welcomeHeading: "Welcome to Mysuru Junction Smart Navigation",
    heroDesc: "An accessible indoor navigation portal helping all passengers—including users with physical, visual, or hearing disabilities—navigate between platforms, concourses, ticket counters, and station facilities.",
    btnStartNav: "Start Navigation",
    btnFacilities: "Find Nearby Facilities",
    btnAssistance: "Get Staff Assistance",
    assistanceModesTitle: "Choose Assistance Mode",
    assistanceModesSub: "Tailor directions to your specific mobility or sensory preference.",
    modeGeneralTitle: "General Passenger Mode",
    modeGeneralDesc: "Standard indoor station map, route highlighting, estimated walk times, and step-by-step guidance.",
    modeWheelchairTitle: "Wheelchair Accessible",
    modeWheelchairDesc: "Step-free routes using verified ramps and lifts. Automatically avoids all stairs and escalators.",
    modeVisualTitle: "Visual Assistance Mode",
    modeVisualDesc: "Screen-reader optimized, high contrast, Web Speech voice navigation, large touch controls, and spoken updates.",
    modeHearingTitle: "Hearing Assistance Mode",
    modeHearingDesc: "Visual-first step directions, high visibility alerts, visual cues, and silent staff request triggers.",
    routeFinderTitle: "Route Finder & Map",
    reportBlockageBtn: "Report Blockage",
    labelStartPoint: "Starting Point (Current Location)",
    labelDestPoint: "Destination",
    locateMe: "Locate Me (GPS)",
    wheelchairOpt: "Wheelchair Accessible Route (Lifts & Ramps only)",
    noStairsOpt: "Avoid Stairs (No stair climbing)",
    btnFindRoute: "Find Route",
    routeDirectionsTitle: "Route Directions",
    speakInstruction: "Speak Instruction",
    readDestination: "Read Destination",
    noRouteTitle: "No Route Selected",
    noRouteDesc: "Select a starting point and destination above, then click 'Find Route' to calculate step-by-step directions.",
    prevStep: "Previous Step",
    nextStep: "Next Step",
    startNavAction: "Start Navigation",
    cancelNavAction: "Cancel Navigation",
    facilitiesHeading: "Station Facilities & Amenities",
    facilitiesSub: "Browse verified and demonstration amenities across Mysuru Junction. Select any facility to navigate directly to it.",
    searchPlaceholder: "Search facilities (e.g., Washroom, Water, Ticket)...",
    helpHeading: "Request Passenger Assistance",
    helpFormDesc: "Passengers requiring wheelchair escort, visual assistance, or general station support can request immediate help here.",
    submitHelpReq: "Submit Assistance Request",
    navigateHere: "Navigate Here"
  },
  kn: {
    appTitle: "ಮೈಸೂರು ಜಂಕ್ಷನ್ ಸ್ಮಾರ್ಟ್ ನ್ಯಾವಿಗೇಷನ್",
    appSubtitle: "ಮೈಸೂರು ಜಂಕ್ಷನ್ (MYS) • ಭಾರತೀಯ ರೈಲ್ವೆ",
    disclaimerBadge: "ಡೆಮೊ ಮಾದರಿ",
    disclaimerText: "ಸ್ಥಳ ಪರಿಶೀಲನೆ ಅಗತ್ಯವಿರುವ ನಿಲ್ದಾಣದ ಪ್ರದರ್ಶನ ನಕ್ಷೆ.",
    tabHome: "ಮುಖ್ಯ ಪುಟ",
    tabMap: "ನ್ಯಾವಿಗೇಷನ್ ಮತ್ತು ನಕ್ಷೆ",
    tabFacilities: "ಸೌಲಭ್ಯಗಳು",
    tabHelp: "ಸಿಬ್ಬಂದಿ ನೆರವು",
    welcomeHeading: "ಮೈಸೂರು ಜಂಕ್ಷನ್ ಸ್ಮಾರ್ಟ್ ನ್ಯಾವಿಗೇಷನ್‌ಗೆ ಸುಸ್ವಾಗತ",
    heroDesc: "ಪ್ಲಾಟ್‌ಫಾರ್ಮ್‌ಗಳು, ಟಿಕೆಟ್ ಕೌಂಟರ್‌ಗಳು ಮತ್ತು ಸೌಲಭ್ಯಗಳ ನಡುವೆ ಸುರಕ್ಷಿತವಾಗಿ ಸಂಚರಿಸಲು ಎಲ್ಲಾ ಪ್ರಯಾಣಿಕರಿಗೆ ನೆರವಾಗುವ ನ್ಯಾವಿಗೇಷನ್ ವ್ಯವಸ್ಥೆ.",
    btnStartNav: "ನ್ಯಾವಿಗೇಷನ್ ಪ್ರಾರಂಭಿಸಿ",
    btnFacilities: "ಸೌಲಭ್ಯಗಳನ್ನು ಹುಡುಕಿ",
    btnAssistance: "ಸಿಬ್ಬಂದಿ ನೆರವು ಪಡೆಯಿರಿ",
    assistanceModesTitle: "ನೆರವಿನ ಮಾದರಿಯನ್ನು ಆಯ್ಕೆಮಾಡಿ",
    assistanceModesSub: "ನಿಮ್ಮ ಚಲನಶೀಲತೆ ಅಥವಾ ಆದ್ಯತೆಗೆ ಅನುಗುಣವಾಗಿ ನಿರ್ದೇಶನಗಳನ್ನು ಕಸ್ಟಮೈಸ್ ಮಾಡಿ.",
    modeGeneralTitle: "ಸಾಮಾನ್ಯ ಪ್ರಯಾಣಿಕರ ಮೋಡ್",
    modeGeneralDesc: "ಸಾಮಾನ್ಯ ನಿಲ್ದಾಣದ ನಕ್ಷೆ, ಹಂತ-ಹಂತದ ನಿರ್ದೇಶನಗಳು ಮತ್ತು ಅಂದಾಜು ನಡಿಗೆ ಸಮಯ.",
    modeWheelchairTitle: "ವೀಲ್‌ಚೇರ್ ಸುಲಭ ಮೋಡ್",
    modeWheelchairDesc: "ಮೆಟ್ಟಿಲುಗಳನ್ನು ಸಂಪೂರ್ಣವಾಗಿ ಹೊರತುಪಡಿಸಿ ಲಿಫ್ಟ್‌ಗಳು ಮತ್ತು ರಾಂಪ್‌ಗಳನ್ನು ಬಳಸುವ ಮಾರ್ಗಗಳು.",
    modeVisualTitle: "ದೃಷ್ಟಿ ನೆರವು ಮೋಡ್",
    modeVisualDesc: "ಧ್ವನಿ ನ್ಯಾವಿಗೇಷನ್, ಹೆಚ್ಚಿನ ಕಾಂಟ್ರಾಸ್ಟ್ ಮತ್ತು ಪರದೆ ಓದುಗರಿಗೆ ಹೊಂದುವ ವಿನ್ಯಾಸ.",
    modeHearingTitle: "ಶ್ರವಣ ನೆರವು ಮೋಡ್",
    modeHearingDesc: "ದೃಶ್ಯ ಆಧಾರಿತ ಹಂತ-ಹಂತದ ಮಾರ್ಗದರ್ಶನ ಮತ್ತು ಎಚ್ಚರಿಕೆ ಸೂಚನೆಗಳು.",
    routeFinderTitle: "ಮಾರ್ಗ ಶೋಧಕ ಮತ್ತು ನಕ್ಷೆ",
    reportBlockageBtn: "ತಡೆಯನ್ನು ವರದಿ ಮಾಡಿ",
    labelStartPoint: "ಪ್ರಾರಂಭದ ಸ್ಥಳ (ಪ್ರಸ್ತುತ ಸ್ಥಳ)",
    labelDestPoint: "ತಲುಪಬೇಕಾದ ಸ್ಥಳ",
    locateMe: "ನನ್ನ ಸ್ಥಳ (GPS)",
    wheelchairOpt: "ವೀಲ್‌ಚೇರ್ ಸೌಲಭ್ಯ ಮಾರ್ಗ (ಲಿಫ್ಟ್ ಮತ್ತು ರಾಂಪ್ ಮಾತ್ರ)",
    noStairsOpt: "ಮೆಟ್ಟಿಲುಗಳನ್ನು ತಡೆಯಿರಿ",
    btnFindRoute: "ಮಾರ್ಗವನ್ನು ಹುಡುಕಿ",
    routeDirectionsTitle: "ಮಾರ್ಗದ ನಿರ್ದೇಶನಗಳು",
    speakInstruction: "ನಿರ್ದೇಶನವನ್ನು ಆಲಿಸಿ",
    readDestination: "ಗಮ್ಯಸ್ಥಾನವನ್ನು ಓದಿ",
    noRouteTitle: "ಯಾವ ಮಾರ್ಗವನ್ನೂ ಆಯ್ಕೆ ಮಾಡಲಾಗಿಲ್ಲ",
    noRouteDesc: "ಪ್ರಾರಂಭ ಮತ್ತು ಗಮ್ಯಸ್ಥಾನವನ್ನು ಆಯ್ಕೆ ಮಾಡಿ 'ಮಾರ್ಗವನ್ನು ಹುಡುಕಿ' ಕ್ಲಿಕ್ ಮಾಡಿ.",
    prevStep: "ಹಿಂದಿನ ಹಂತ",
    nextStep: "ಮುಂದಿನ ಹಂತ",
    startNavAction: "ನ್ಯಾವಿಗೇಷನ್ ಪ್ರಾರಂಭಿಸಿ",
    cancelNavAction: "ರದ್ದುಮಾಡಿ",
    facilitiesHeading: "ನಿಲ್ದಾಣದ ಸೌಲಭ್ಯಗಳು",
    facilitiesSub: "ಮೈಸೂರು ಜಂಕ್ಷನ್‌ನಲ್ಲಿ ಲಭ್ಯವಿರುವ ಸೌಲಭ್ಯಗಳನ್ನು ವೀಕ್ಷಿಸಿ ಮತ್ತು ನೇರವಾಗಿ ಮಾರ್ಗವನ್ನು ಕಂಡುಕೊಳ್ಳಿ.",
    searchPlaceholder: "ಸೌಲಭ್ಯಗಳನ್ನು ಹುಡುಕಿ (ಉದಾ: ಶೌಚಾಲಯ, ಕುಡಿಯುವ ನೀರು)...",
    helpHeading: "ಪ್ರಯಾಣಿಕರ ನೆರವು ಕೋರಿ",
    helpFormDesc: "ವೀಲ್‌ಚೇರ್ ಅಥವಾ ದೃಷ್ಟಿ ನೆರವು ಅಗತ್ಯವಿರುವ ಪ್ರಯಾಣಿಕರು ಇಲ್ಲಿ ವಿನಂತಿಸಬಹುದು.",
    submitHelpReq: "ವಿನಂತಿಯನ್ನು ಸಲ್ಲಿಸಿ",
    navigateHere: "ಇಲ್ಲಿಗೆ ಮಾರ್ಗ ತೋರಿಸಿ"
  },
  ta: {
    appTitle: "மைசூர் சந்திப்பு ஸ்மார்ட் வழிகாட்டி",
    appSubtitle: "மைசூர் சந்திப்பு (MYS) • இந்திய இரயில்வே",
    disclaimerBadge: "டெமோ மாதிரி",
    disclaimerText: "நிலையத்தின் உத்தேச வரைபடம். நேரடி சரிபார்ப்பு தேவை.",
    tabHome: "முகப்பு",
    tabMap: "வழிகாட்டி & வரைபடம்",
    tabFacilities: "வசதிகள்",
    tabHelp: "உதவி",
    welcomeHeading: "மைசூர் சந்திப்பு ஸ்மார்ட் வழிகாட்டிக்கு வரவேற்கிறோம்",
    heroDesc: "அனைத்து பயணிகளும் தளங்கள் மற்றும் வசதிகளுக்கு இடையே எளிதாக பயணிக்க உதவும் வழிகாட்டி அமைப்பு.",
    btnStartNav: "வழிகாட்டியைத் தொடங்கு",
    btnFacilities: "வசதிகளைக் கண்டறி",
    btnAssistance: "உதவி பெறுக",
    assistanceModesTitle: "உதவி முறையைத் தேர்ந்தெடுக்கவும்",
    assistanceModesSub: "உங்கள் விருப்பத்திற்கு ஏற்ப வழிகாட்டுதலைப் பெறுங்கள்.",
    modeGeneralTitle: "பொதுப் பயனர் முறை",
    modeGeneralDesc: "நிலையான நிலைய வரைபடம் மற்றும் படிப்படியான வழிகாட்டல்.",
    modeWheelchairTitle: "சக்கர நாற்காலி முறை",
    modeWheelchairDesc: "படிகளுக்குப் பதிலாக மின்சார தூக்கிகள் மற்றும் சாய்வுப் பாதைகளைப் பயன்படுத்தும் வழிகள்.",
    modeVisualTitle: "பார்வை உதவி முறை",
    modeVisualDesc: "குரல் வழிகாட்டுதல் மற்றும் அதிக மாறுபட்ட வண்ண அமைப்பு.",
    modeHearingTitle: "செவிப்புலன் உதவி முறை",
    modeHearingDesc: "காட்சி அடிப்படையிலான வழிமுறைகள் மற்றும் எச்சரிக்கைகள்.",
    routeFinderTitle: "வழி கண்டுபிடிப்பான்",
    reportBlockageBtn: "தடையைப் புகாரளி",
    labelStartPoint: "தொடக்கப் புள்ளி",
    labelDestPoint: "செல்ல வேண்டிய இடம்",
    locateMe: "இருப்பிடத்தைக் கண்டறி",
    wheelchairOpt: "சக்கர நாற்காலி வழி (தூக்கி மட்டும்)",
    noStairsOpt: "படிகளைத் தவிர்க்கவும்",
    btnFindRoute: "வழியைக் கண்டுபிடி",
    routeDirectionsTitle: "வழிமுறைகள்",
    speakInstruction: "குரல் வழிமுறை",
    readDestination: "இலக்கை வாசிக்கவும்",
    noRouteTitle: "வழி தேர்ந்தெடுக்கப்படவில்லை",
    noRouteDesc: "தொடக்கப் புள்ளி மற்றும் இலக்கைத் தேர்ந்தெடுத்து 'வழியைக் கண்டுபிடி' என்பதைக் கிளிக் செய்யவும்.",
    prevStep: "முந்தைய நிலை",
    nextStep: "அடுத்த நிலை",
    startNavAction: "வழிகாட்டியைத் தொடங்கு",
    cancelNavAction: "ரத்து செய்",
    facilitiesHeading: "நிலைய வசதிகள்",
    facilitiesSub: "மைசூர் சந்திப்பில் உள்ள வசதிகளைப் பார்த்து நேரடியாகச் செல்லுங்கள்.",
    searchPlaceholder: "வசதிகளைத் தேடுங்கள் (எ.கா. கழிப்பறை, நீர்)...",
    helpHeading: "உதவி கோரிக்கை",
    helpFormDesc: "உதவி தேவைப்படும் பயணிகள் இங்கு கோரிக்கை வைக்கலாம்.",
    submitHelpReq: "கோரிக்கையைச் சமர்ப்பி",
    navigateHere: "இங்கே செல்"
  },
  te: {
    appTitle: "మైసూర్ జంక్షన్ స్మార్ట్ నావిగేషన్",
    appSubtitle: "మైసూర్ జంక్షన్ (MYS) • ఇండియన్ రైల్వేస్",
    disclaimerBadge: "డెమో ప్రోటోటైప్",
    disclaimerText: "స్టేషన్ మ్యాప్ నమూనా. ప్రత్యక్ష పరిశీలన అవసరం.",
    tabHome: "హోమ్",
    tabMap: "నావిగేషన్ & మ్యాప్",
    tabFacilities: "సదుపాయాలు",
    tabHelp: "సహాయం",
    welcomeHeading: "మైసూర్ జంక్షన్ నావిగేషన్‌కు స్వాగతం",
    heroDesc: "ప్రయాణికులందరికీ ప్లాట్‌ఫారమ్‌లు మరియు సౌకర్యాల మధ్య సులభంగా నావిగేట్ చేయడానికి సహాయపడే సిస్టమ్.",
    btnStartNav: "నావిగేషన్ ప్రారంభించండి",
    btnFacilities: "సౌకర్యాలను కనుగొనండి",
    btnAssistance: "సహాయం పొందండి",
    assistanceModesTitle: "సహాయ రకాన్ని ఎంచుకోండి",
    assistanceModesSub: "మీ ప్రాధాన్యత ప్రకారం దిశలను పొందండి.",
    modeGeneralTitle: "సాధారణ ప్రయాణీకుల మోడ్",
    modeGeneralDesc: "సాధారణ స్టేషన్ మ్యాప్ మరియు దశల వారీ మార్గదర్శకత్వం.",
    modeWheelchairTitle: "వీల్‌చైర్ యాక్సెస్ మోడ్",
    modeWheelchairDesc: "మెట్లకు బదులుగా లిఫ్ట్‌లు మరియు ర్యాంప్‌లను ఉపయోగించే మార్గాలు.",
    modeVisualTitle: "దృష్టి సహాయక మోడ్",
    modeVisualDesc: "వాయిస్ నావిగేషన్ మరియు అధిక కాంట్రాస్ట్ డిజైన్.",
    modeHearingTitle: "శ్రవణ సహాయక మోడ్",
    modeHearingDesc: "దృశ్య ఆధారిత దిశలు మరియు హెచ్చరికలు.",
    routeFinderTitle: "రూట్ ఫైండర్",
    reportBlockageBtn: "ఆటంకాన్ని నివేదించండి",
    labelStartPoint: "ప్రారంభ ప్రాంతం",
    labelDestPoint: "గమ్యస్థానం",
    locateMe: "నా లొకేషన్ (GPS)",
    wheelchairOpt: "వీల్‌చైర్ మార్గం (లిఫ్ట్ మాత్రమే)",
    noStairsOpt: "మెట్లను నివారించండి",
    btnFindRoute: "మార్గం కనుగొనండి",
    routeDirectionsTitle: "మార్గదర్శకత్వం",
    speakInstruction: "వాయిస్ వినండి",
    readDestination: "గమ్యస్థానం వినండి",
    noRouteTitle: "మార్గం ఎంచుకోలేదు",
    noRouteDesc: "ప్రారంభం మరియు గమ్యాన్ని ఎంచుకుని 'మార్గం కనుగొనండి' క్లిక్ చేయండి.",
    prevStep: "మునుపటి దశ",
    nextStep: "తరువాతి దశ",
    startNavAction: "ప్రారంభించండి",
    cancelNavAction: "రద్దు చేయి",
    facilitiesHeading: "స్టేషన్ సౌకర్యాలు",
    facilitiesSub: "మైసూర్ జంక్షన్‌లోని సౌకర్యాలను చూడండి.",
    searchPlaceholder: "సౌకర్యాలను శోధించండి...",
    helpHeading: "సహాయం అభ్యర్థించండి",
    helpFormDesc: "సహాయం కావలసిన ప్రయాణికులు ఇక్కడ అభ్యర్థించవచ్చు.",
    submitHelpReq: "అభ్యర్థన పంపు",
    navigateHere: "ఇక్కడకు మార్గం"
  },
  ml: {
    appTitle: "മൈസൂരു ജംഗ്ഷൻ സ്മാർട്ട് നാവിഗേഷൻ",
    appSubtitle: "മൈസൂരു ജംഗ്ഷൻ (MYS) • ഇന്ത്യൻ റെയിൽവേ",
    disclaimerBadge: "ഡെമോ മാതൃക",
    disclaimerText: "സ്റ്റേഷൻ മാപ്പ് മാതൃക. നേരിട്ടുള്ള പരിശോധന ആവശ്യമാണ്.",
    tabHome: "ഹോം",
    tabMap: "നാവിഗേഷൻ & മാപ്പ്",
    tabFacilities: "സൗകര്യങ്ങൾ",
    tabHelp: "സഹായം",
    welcomeHeading: "മൈസൂരു ജംഗ്ഷൻ നാവിഗേഷനിലേക്ക് സ്വാഗതം",
    heroDesc: "എല്ലാ യാത്രക്കാർക്കും പ്ലാറ്റ്‌ഫോമുകൾക്കിടയിൽ എളുപ്പത്തിൽ സഞ്ചരിക്കാൻ സഹായിക്കുന്ന സംവിധാനം.",
    btnStartNav: "നാവിഗേഷൻ ആരംഭിക്കുക",
    btnFacilities: "സൗകര്യങ്ങൾ കണ്ടെത്തുക",
    btnAssistance: "സഹായം നേടുക",
    assistanceModesTitle: "സഹായ രീതി തിരഞ്ഞെടുക്കുക",
    assistanceModesSub: "നിങ്ങളുടെ ആവശ്യത്തിനനുസരിച്ച് ദിശകൾ ക്രമീകരിക്കുക.",
    modeGeneralTitle: "സാധാരണ യാത്രാ മോഡ്",
    modeGeneralDesc: "സാധാരണ സ്റ്റേഷൻ മാപ്പും ഘട്ടം ഘട്ടമായുള്ള വഴികളും.",
    modeWheelchairTitle: "വീൽചെയർ മോഡ്",
    modeWheelchairDesc: "ലിഫ്റ്റുകളും റാംപുകളും മാത്രം ഉപയോഗിക്കുന്ന വഴികൾ.",
    modeVisualTitle: "കാഴ്ച സഹായ മോഡ്",
    modeVisualDesc: "ശബ്ദ നാവിഗേഷനും ഉയർന്ന കോൺട്രാസ്റ്റും.",
    modeHearingTitle: "ശ്രവണ സഹായ മോഡ്",
    modeHearingDesc: "ദൃശ്യാധിഷ്ഠിത നിർദ്ദേശങ്ങളും മുന്നറിയിപ്പുകളും.",
    routeFinderTitle: "റൂട്ട് ഫൈൻഡർ",
    reportBlockageBtn: "തടസ്സം റിപ്പോർട്ട് ചെയ്യുക",
    labelStartPoint: "തുടക്ക സ്ഥലം",
    labelDestPoint: "ലക്ഷ്യസ്ഥാനം",
    locateMe: "എന്റെ സ്ഥാനം (GPS)",
    wheelchairOpt: "വീൽചെയർ റൂട്ട് (ലിഫ്റ്റ് മാത്രം)",
    noStairsOpt: "പടികൾ ഒഴിവാക്കുക",
    btnFindRoute: "വഴി കണ്ടെത്തുക",
    routeDirectionsTitle: "വഴി നിർദ്ദേശങ്ങൾ",
    speakInstruction: "ശബ്ദ നിർദ്ദേശം കേൾക്കുക",
    readDestination: "ലക്ഷ്യസ്ഥാനം കേൾക്കുക",
    noRouteTitle: "വഴി തിരഞ്ഞെടുത്തിട്ടില്ല",
    noRouteDesc: "തുടക്ക സ്ഥലവും ലക്ഷ്യസ്ഥാനവും തിരഞ്ഞെടുത്ത് 'വഴി കണ്ടെത്തുക' ക്ലിക്ക് ചെയ്യുക.",
    prevStep: "മുമ്പത്തെ ഘട്ടം",
    nextStep: "അടുത്ത ഘട്ടം",
    startNavAction: "ആരംഭിക്കുക",
    cancelNavAction: "റദ്ദാക്കുക",
    facilitiesHeading: "സ്റ്റേഷൻ സൗകര്യങ്ങൾ",
    facilitiesSub: "മൈസൂരു ജംഗ്ഷനിലെ സൗകര്യങ്ങൾ കാണുക.",
    searchPlaceholder: "സൗകര്യങ്ങൾ തിരയുക...",
    helpHeading: "സഹായം ആവശ്യപ്പെടുക",
    helpFormDesc: "സഹായം ആവശ്യമുള്ള യാത്രക്കാർക്ക് ഇവിടെ അപേക്ഷിക്കാം.",
    submitHelpReq: "അപേക്ഷ നൽകുക",
    navigateHere: "ഇവിടേക്ക് പോവുക"
  },
  hi: {
    appTitle: "मैसूरु जंक्शन स्मार्ट नेविगेशन",
    appSubtitle: "मैसूरु जंक्शन (MYS) • भारतीय रेल",
    disclaimerBadge: "डेमो मॉडल",
    disclaimerText: "स्टेशन का काल्पनिक मानचित्र। स्थान सत्यापन आवश्यक है।",
    tabHome: "मुख्य पृष्ठ",
    tabMap: "नेविगेशन और मानचित्र",
    tabFacilities: "सुविधाएं",
    tabHelp: "कर्मचारी सहायता",
    welcomeHeading: "मैसूरु जंक्शन स्मार्ट नेविगेशन में आपका स्वागत है",
    heroDesc: "सभी यात्रियों को प्लेटफॉर्मों, टिकट काउंटरों और सुविधाओं के बीच सुगम नेविगेशन प्रदान करने वाला सुलभ पोर्टल।",
    btnStartNav: "नेविगेशन शुरू करें",
    btnFacilities: "सुविधाएं खोजें",
    btnAssistance: "कर्मचारी सहायता प्राप्त करें",
    assistanceModesTitle: "सहायता मोड चुनें",
    assistanceModesSub: "अपनी सुविधा और आवश्यकता के अनुसार दिशा-निर्देश प्राप्त करें।",
    modeGeneralTitle: "सामान्य यात्री मोड",
    modeGeneralDesc: "मानक स्टेशन मानचित्र, मार्ग हाइलाइटिंग और चरण-दर-चरण मार्गदर्शन।",
    modeWheelchairTitle: "व्हीलचेयर सुलभ मोड",
    modeWheelchairDesc: "सीढ़ियों के बिना केवल लिफ्ट और रैंप का उपयोग करने वाले मार्ग।",
    modeVisualTitle: "दृष्टि सहायता मोड",
    modeVisualDesc: "वॉइस नेविगेशन, हाई कंट्रास्ट और स्क्रीन रीडर अनुकूलित डिज़ाइन।",
    modeHearingTitle: "श्रवण सहायता मोड",
    modeHearingDesc: "दृश्य-आधारित चरण-दर-चरण निर्देश और अलर्ट।",
    routeFinderTitle: "मार्ग खोजक और मानचित्र",
    reportBlockageBtn: "रुकावट की रिपोर्ट करें",
    labelStartPoint: "प्रारंभिक बिंदु (वर्तमान स्थान)",
    labelDestPoint: "गंतव्य",
    locateMe: "मेरा स्थान (GPS)",
    wheelchairOpt: "व्हीलचेयर सुलभ मार्ग (केवल लिफ्ट व रैंप)",
    noStairsOpt: "सीढ़ियों से बचें",
    btnFindRoute: "मार्ग खोजें",
    routeDirectionsTitle: "मार्ग के निर्देश",
    speakInstruction: "निर्देश सुनें",
    readDestination: "गंतव्य सुनें",
    noRouteTitle: "कोई मार्ग नहीं चुना गया",
    noRouteDesc: "प्रारंभिक बिंदु और गंतव्य चुनकर 'मार्ग खोजें' पर क्लिक करें।",
    prevStep: "पिछला चरण",
    nextStep: "अगला चरण",
    startNavAction: "नेविगेशन प्रारंभ करें",
    cancelNavAction: "रद्द करें",
    facilitiesHeading: "स्टेशन की सुविधाएं",
    facilitiesSub: "मैसूरु जंक्शन की सुविधाओं को देखें और सीधे मार्ग खोजें।",
    searchPlaceholder: "सुविधाएं खोजें (उदा. शौचालय, पेयजल)...",
    helpHeading: "यात्री सहायता का अनुरोध करें",
    helpFormDesc: "व्हीलचेयर या दृष्टि सहायता की आवश्यकता वाले यात्री यहां अनुरोध कर सकते हैं।",
    submitHelpReq: "अनुरोध सबमिट करें",
    navigateHere: "यहां का मार्ग देखें"
  }
};

// --------------------------------------------------------------------------
// 2. MYSURU JUNCTION STATION NODES & GRAPH (6 PLATFORMS & AMENITIES)
// --------------------------------------------------------------------------
const stationNodes = {
  entrance: { id: "entrance", names: { en: "Main Entrance / Exit Gate 🚪", kn: "ಮುಖ್ಯ ಪ್ರವೇಶದ್ವಾರ / ನಿರ್ಗಮನ ಗೇಟ್ 🚪", ta: "முதன்மை நுழைவாயில் 🚪", te: "ముఖ్య ద్వారం 🚪", ml: "പ്രധാന കവാടം 🚪", hi: "मुख्य प्रवेश / निकास द्वार 🚪" }, x: 500, y: 600, category: "transport" },
  concourse: { id: "concourse", names: { en: "Main Station Concourse", kn: "ಮುಖ್ಯ ಕಾಂಕೋರ್ಸ್ ಹಾಲ್", ta: "முதன்மை கூடம்", te: "ప్రధాన కాంకోర్స్", ml: "പ്രധാന കോൺകോഴ്സ്", hi: "मुख्य कॉनकोर्स हॉल" }, x: 500, y: 465, category: "services" },
  ticket: { id: "ticket", names: { en: "Ticket Counters & UTS 🎫", kn: "ಟಿಕೆಟ್ ಕೌಂಟರ್‌ಗಳು 🎫", ta: "டிக்கெட் கவுண்டர்கள் 🎫", te: "టికెట్ కౌంటర్లు 🎫", ml: "ടിക്കറ്റ് കൗണ്ടറുകൾ 🎫", hi: "टिकट काउंटर व यूटीएस 🎫" }, x: 275, y: 515, category: "services" },
  enquiry: { id: "enquiry", names: { en: "Help Desk & Information ℹ️", kn: "ಮಾಹಿತಿ ಕೇಂದ್ರ / ವಿಚಾರಣೆ ℹ️", ta: "தகவல் மையம் ℹ️", te: "సమాచార కేంద్రం ℹ️", ml: "വിവരകേന്ദ്രം ℹ️", hi: "पूछताछ व सहायता केंद्र ℹ️" }, x: 415, y: 515, category: "services" },
  waiting: { id: "waiting", names: { en: "Executive Waiting Hall 🪑", kn: "ಕಾಯುವ ಕೊಠಡಿ 🪑", ta: "காத்திருப்போர் அறை 🪑", te: "వేచివుండే గది 🪑", ml: "വെയിറ്റിംഗ് ഹാൾ 🪑", hi: "यात्री प्रतीक्षालय 🪑" }, x: 555, y: 515, category: "waiting" },
  washroom_main: { id: "washroom_main", names: { en: "Accessible Toilets & Washrooms 🚻", kn: "ಶೌಚಾಲಯಗಳು 🚻", ta: "கழிப்பறைகள் 🚻", te: "శౌచాలయాలు 🚻", ml: "ശൗചാലയം 🚻", hi: "सुलभ शौचालय 🚻" }, x: 705, y: 510, category: "washroom" },
  parking_west: { id: "parking_west", names: { en: "West Parking & Auto Stand 🛺", kn: "ಪಶ್ಚಿಮ ಪಾರ್ಕಿಂಗ್ / ಆಟೋ ನಿಲ್ದಾಣ 🛺", ta: "மேற்கு பார்க்கிங் 🛺", te: "పశ్చిమ పార్కింగ్ 🛺", ml: "പശ്ചിമ പാർക്കിംഗ് 🛺", hi: "पश्चिम पार्किंग व ऑटो स्टैंड 🛺" }, x: 155, y: 540, category: "transport" },
  parking_east: { id: "parking_east", names: { en: "East Parking & Taxi Stand 🚕", kn: "ಪೂರ್ವ ಪಾರ್ಕಿಂಗ್ / ಟ್ಯಾಕ್ಸಿ ನಿಲ್ದಾಣ 🚕", ta: "கிழக்கு பார்க்கிಂಗ್ 🚕", te: "తూర్పు పార్కింగ్ 🚕", ml: "കിഴക്ക് പാർക്കിംഗ് 🚕", hi: "पूर्व पार्किंग व टैक्सी स्टैंड 🚕" }, x: 835, y: 540, category: "transport" },
  
  // Platforms 1 to 6
  platform1: { id: "platform1", names: { en: "Platform 1 (Main Side - Bengaluru/Chennai)", kn: "ಪ್ಲಾಟ್‌ಫಾರ್ಮ್ 1 (ಬೆಂಗಳೂರು ಮಾರ್ಗ)", ta: "நடைமேடை 1", te: "ప్లాట్‌ఫార్మ్ 1", ml: "പ്ലാറ്റ്ഫോം 1", hi: "प्लेटफॉर्म 1 (मुख्य साइड)" }, x: 500, y: 72, category: "platforms" },
  platform2: { id: "platform2", names: { en: "Platform 2 (Island Platform 2/3)", kn: "ಪ್ಲಾಟ್‌ಫಾರ್ಮ್ 2", ta: "நடைமேடை 2", te: "ప్లాట్‌ఫార్మ్ 2", ml: "പ്ലാറ്റ്ഫോം 2", hi: "प्लेटफॉर्म 2" }, x: 300, y: 150, category: "platforms" },
  platform3: { id: "platform3", names: { en: "Platform 3 (Island Platform 2/3)", kn: "ಪ್ಲಾಟ್‌ಫಾರ್ಮ್ 3", ta: "நடைமேடை 3", te: "ప్లాట్‌ಫಾರ್ಮ್ 3", ml: "പ്ലാറ്റ്ഫോം 3", hi: "प्लेटफॉर्म 3" }, x: 700, y: 150, category: "platforms" },
  platform4: { id: "platform4", names: { en: "Platform 4 (Island Platform 4/5)", kn: "ಪ್ಲಾಟ್‌ಫಾರ್ಮ್ 4", ta: "நடைமேடை 4", te: "ప్లాట్‌ಫಾರ್ಮ್ 4", ml: "പ്ലാറ്റ്ഫോം 4", hi: "प्लेटफॉर्म 4" }, x: 300, y: 270, category: "platforms" },
  platform5: { id: "platform5", names: { en: "Platform 5 (Island Platform 4/5)", kn: "ಪ್ಲಾಟ್‌ಫಾರ್ಮ್ 5", ta: "நடைமேடை 5", te: "ಪ್ಲಾట్‌ಫಾರ್ಮ್ 5", ml: "പ്ലാറ്റ്ഫോം 5", hi: "प्लेटफॉर्म 5" }, x: 700, y: 270, category: "platforms" },
  platform6: { id: "platform6", names: { en: "Platform 6 (South Concourse Side)", kn: "ಪ್ಲಾಟ್‌ಫಾರ್ಮ್ 6", ta: "நடைமேடை 6", te: "ప్లాట్‌ఫಾರ್ಮ್ 6", ml: "പ്ലാറ്റ്ഫോം 6", hi: "प्लेटफॉर्म 6" }, x: 500, y: 390, category: "platforms" },
  
  // Foot Overbridges with Lifts/Stairs
  fob_west: { id: "fob_west", names: { en: "West Foot Overbridge 1 (Stairs & Lift 🛗)", kn: "ಪಶ್ಚಿಮ ಕಾಲ್ನಡಿಗೆ ಮೇಲ್ಸೇತುವೆ (ಲಿಫ್ಟ್ 🛗)", ta: "மேற்கு மேம்பாலம் (மின்சார தூக்கி 🛗)", te: "పశ్చిమ నడక వంతెన (లిఫ్ట్ 🛗)", ml: "പശ്ചിമ മേൽപ്പാലം (ലിഫ്റ്റ് 🛗)", hi: "पश्चिम फुट ओवरब्रिज (लिफ्ट 🛗)" }, x: 210, y: 220, category: "services" },
  fob_east: { id: "fob_east", names: { en: "East Foot Overbridge 2 (Escalator & Lift 🛗)", kn: "ಪೂರ್ವ ಕಾಲ್ನಡಿಗೆ ಮೇಲ್ಸೇತುವೆ (ಲಿಫ್ಟ್ 🛗)", ta: "கிழக்கு மேம்பாலம் (மின்சார தூக்கி 🛗)", te: "తూర్పు నడక వంతెన (లిఫ్ట్ 🛗)", ml: "കിഴക്ക് മേൽപ്പാലം (ലിഫ്റ്റ് 🛗)", hi: "पूर्व फुट ओवरब्रिज (लिफ्ट 🛗)" }, x: 790, y: 220, category: "services" }
};

// Graph Edges (Weighted Connections with Stair/Lift metadata)
const stationEdges = [
  { from: "entrance", to: "concourse", distance: 40, hasStairs: false, hasLift: false, isRamp: true },
  { from: "concourse", to: "ticket", distance: 30, hasStairs: false, hasLift: false, isRamp: true },
  { from: "concourse", to: "enquiry", distance: 20, hasStairs: false, hasLift: false, isRamp: true },
  { from: "concourse", to: "waiting", distance: 25, hasStairs: false, hasLift: false, isRamp: true },
  { from: "concourse", to: "washroom_main", distance: 45, hasStairs: false, hasLift: false, isRamp: true },
  { from: "concourse", to: "parking_west", distance: 60, hasStairs: false, hasLift: false, isRamp: true },
  { from: "concourse", to: "parking_east", distance: 65, hasStairs: false, hasLift: false, isRamp: true },
  
  // Concourse to Platform 6 (Direct level walkway)
  { from: "concourse", to: "platform6", distance: 30, hasStairs: false, hasLift: false, isRamp: true },
  
  // Concourse to FOBs
  { from: "concourse", to: "fob_west", distance: 90, hasStairs: false, hasLift: true, isRamp: true },
  { from: "concourse", to: "fob_east", distance: 95, hasStairs: false, hasLift: true, isRamp: true },
  
  // FOB West connects Platforms 1 to 6 (Stairs & Accessible Lift)
  { from: "fob_west", to: "platform1", distance: 45, hasStairs: true, hasLift: true, isRamp: false },
  { from: "fob_west", to: "platform2", distance: 35, hasStairs: true, hasLift: true, isRamp: false },
  { from: "fob_west", to: "platform3", distance: 35, hasStairs: true, hasLift: true, isRamp: false },
  { from: "fob_west", to: "platform4", distance: 40, hasStairs: true, hasLift: true, isRamp: false },
  { from: "fob_west", to: "platform5", distance: 40, hasStairs: true, hasLift: true, isRamp: false },
  { from: "fob_west", to: "platform6", distance: 50, hasStairs: true, hasLift: true, isRamp: false },
  
  // FOB East connects Platforms 1 to 6 (Escalators & Lift)
  { from: "fob_east", to: "platform1", distance: 45, hasStairs: true, hasLift: true, isRamp: false },
  { from: "fob_east", to: "platform2", distance: 35, hasStairs: true, hasLift: true, isRamp: false },
  { from: "fob_east", to: "platform3", distance: 35, hasStairs: true, hasLift: true, isRamp: false },
  { from: "fob_east", to: "platform4", distance: 40, hasStairs: true, hasLift: true, isRamp: false },
  { from: "fob_east", to: "platform5", distance: 40, hasStairs: true, hasLift: true, isRamp: false },
  { from: "fob_east", to: "platform6", distance: 50, hasStairs: true, hasLift: true, isRamp: false }
];

// --------------------------------------------------------------------------
// 3. APPLICATION STATE
// --------------------------------------------------------------------------
const appState = {
  currentLang: "en",
  activeProfile: "general", // "general", "wheelchair", "visual", "hearing"
  textSize: "normal",
  highContrast: false,
  ttsEnabled: false,
  reducedMotion: false,
  blockedNodes: new Set(),
  blockedEdges: new Set(),
  calculatedRoute: null,
  currentStepIndex: 0,
  isNavigating: false,
  selectedNodeId: null,
  mapZoom: 1,
  mapPan: { x: 0, y: 0 }
};

// --------------------------------------------------------------------------
// 4. DIJKSTRA SHORTEST PATHFINDING ALGORITHM
// --------------------------------------------------------------------------
function findShortestRoute(startId, destId, options = {}) {
  if (startId === destId) return { path: [startId], totalDistance: 0, steps: [] };

  const distances = {};
  const previous = {};
  const edgeUsed = {};
  const unvisited = new Set(Object.keys(stationNodes));

  Object.keys(stationNodes).forEach(node => {
    distances[node] = Infinity;
    previous[node] = null;
  });
  distances[startId] = 0;

  // Build Adjacency List
  const adj = {};
  Object.keys(stationNodes).forEach(node => { adj[node] = []; });

  stationEdges.forEach(edge => {
    // Skip blocked edges or nodes
    if (appState.blockedNodes.has(edge.from) || appState.blockedNodes.has(edge.to)) return;

    // Filter based on wheelchair / no stairs preferences
    if (options.requireWheelchair && edge.hasStairs && !edge.hasLift && !edge.isRamp) return;
    if (options.avoidStairs && edge.hasStairs && !edge.hasLift) return;

    adj[edge.from].push({ node: edge.to, distance: edge.distance, meta: edge });
    adj[edge.to].push({ node: edge.from, distance: edge.distance, meta: edge });
  });

  while (unvisited.size > 0) {
    // Pick unvisited node with smallest distance
    let current = null;
    let minDistance = Infinity;
    unvisited.forEach(node => {
      if (distances[node] < minDistance) {
        minDistance = distances[node];
        current = node;
      }
    });

    if (current === null || distances[current] === Infinity) break;
    if (current === destId) break;

    unvisited.delete(current);

    adj[current].forEach(neighbor => {
      if (unvisited.has(neighbor.node)) {
        const alt = distances[current] + neighbor.distance;
        if (alt < distances[neighbor.node]) {
          distances[neighbor.node] = alt;
          previous[neighbor.node] = current;
          edgeUsed[neighbor.node] = neighbor.meta;
        }
      }
    });
  }

  if (distances[destId] === Infinity) return null;

  // Reconstruct path
  const path = [];
  let curr = destId;
  while (curr) {
    path.unshift(curr);
    curr = previous[curr];
  }

  // Generate directions steps
  const steps = [];
  for (let i = 0; i < path.length - 1; i++) {
    const fromNode = stationNodes[path[i]];
    const toNode = stationNodes[path[i+1]];
    const edge = edgeUsed[path[i+1]];

    let modeText = "Walk";
    let icon = "🚶";
    if (edge && edge.hasLift && options.requireWheelchair) {
      modeText = "Take Lift/Elevator";
      icon = "🛗";
    } else if (edge && edge.hasStairs) {
      modeText = "Climb Stairs or Use Lift";
      icon = "🪜";
    } else if (edge && edge.isRamp) {
      modeText = "Walk via Ramp / Level Concourse";
      icon = "♿";
    }

    steps.push({
      stepNumber: i + 1,
      from: fromNode.names[appState.currentLang] || fromNode.names["en"],
      to: toNode.names[appState.currentLang] || toNode.names["en"],
      distance: edge ? edge.distance : 30,
      modeText: modeText,
      icon: icon
    });
  }

  return {
    path: path,
    totalDistance: distances[destId],
    estimatedTimeMins: Math.ceil(distances[destId] / 45), // ~45 meters/min walk speed
    steps: steps
  };
}

// --------------------------------------------------------------------------
// 5. MAIN INITIALIZATION & DOM READY HANDLER
// --------------------------------------------------------------------------
document.addEventListener("DOMContentLoaded", function () {
  console.log("Initializing Mysuru Junction Smart Navigation app...");

  // Verify core required HTML elements
  const findButton = document.getElementById("btn-find-route");
  const startSelect = document.getElementById("select-start");
  const destinationSelect = document.getElementById("select-dest");
  const stepsContainer = document.getElementById("steps-container");

  if (!findButton || !startSelect || !destinationSelect || !stepsContainer) {
    console.error("Error: Required HTML elements were not found.");
    return;
  }

  // Populate Location Dropdowns
  populateDropdowns();

  // Draw Initial SVG Schematic Map
  renderSvgMap();

  // Setup Event Listeners
  setupEventListeners();

  // Render Facilities List
  renderFacilitiesList("all");

  // Apply initial translations
  updateLanguage(appState.currentLang);

  console.log("Mysuru Junction Navigation script initialized successfully.");
});

// --------------------------------------------------------------------------
// 6. POPULATE LOCATION DROPDOWNS
// --------------------------------------------------------------------------
function populateDropdowns() {
  const startSelect = document.getElementById("select-start");
  const destSelect = document.getElementById("select-dest");
  const helpSelect = document.getElementById("select-help-location");
  const blockageSelect = document.getElementById("select-blockage-node");

  if (!startSelect || !destSelect) return;

  const optionsHtml = Object.values(stationNodes).map(node => {
    const name = node.names[appState.currentLang] || node.names["en"];
    return `<option value="${node.id}">${name}</option>`;
  }).join("");

  startSelect.innerHTML = optionsHtml;
  destSelect.innerHTML = optionsHtml;
  if (helpSelect) helpSelect.innerHTML = optionsHtml;
  if (blockageSelect) blockageSelect.innerHTML = optionsHtml;

  // Set default starting point to Main Entrance & destination to Platform 1
  startSelect.value = "entrance";
  destSelect.value = "platform1";
}

// --------------------------------------------------------------------------
// 7. RENDER SVG INTERACTIVE MAP
// --------------------------------------------------------------------------
function renderSvgMap() {
  const svgEdgesLayer = document.getElementById("svg-edges-layer");
  const svgNodesLayer = document.getElementById("svg-nodes-layer");
  if (!svgEdgesLayer || !svgNodesLayer) return;

  // Clear existing rendered layers
  svgEdgesLayer.innerHTML = "";
  svgNodesLayer.innerHTML = "";

  // Render Edges as light dotted corridors
  stationEdges.forEach(edge => {
    const fromNode = stationNodes[edge.from];
    const toNode = stationNodes[edge.to];
    if (!fromNode || !toNode) return;

    const line = document.createElementNS("http://www.w3.org/2000/svg", "line");
    line.setAttribute("x1", fromNode.x);
    line.setAttribute("y1", fromNode.y);
    line.setAttribute("x2", toNode.x);
    line.setAttribute("y2", toNode.y);
    line.setAttribute("class", "edge-line");
    svgEdgesLayer.appendChild(line);
  });

  // Render Interactive Nodes
  Object.values(stationNodes).forEach(node => {
    const g = document.createElementNS("http://www.w3.org/2000/svg", "g");
    g.setAttribute("class", "map-node-group");
    g.setAttribute("data-node-id", node.id);

    const circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    circle.setAttribute("cx", node.x);
    circle.setAttribute("cy", node.y);
    circle.setAttribute("r", 9);
    circle.setAttribute("class", "node-circle");
    if (appState.blockedNodes.has(node.id)) {
      circle.classList.add("blocked-node");
    }

    const text = document.createElementNS("http://www.w3.org/2000/svg", "text");
    text.setAttribute("x", node.x);
    text.setAttribute("y", node.y - 14);
    text.setAttribute("class", "node-text");
    text.textContent = (node.names[appState.currentLang] || node.names["en"]).split(" ")[0];

    g.appendChild(circle);
    g.appendChild(text);

    // Node click handler opens context popup
    g.addEventListener("click", (e) => {
      e.stopPropagation();
      openNodePopup(node, e);
    });

    svgNodesLayer.appendChild(g);
  });
}

// --------------------------------------------------------------------------
// 8. RENDER CALCULATED ROUTE ON SVG MAP
// --------------------------------------------------------------------------
function renderRouteOnMap(route) {
  const svgRouteLayer = document.getElementById("svg-route-layer");
  if (!svgRouteLayer) return;
  svgRouteLayer.innerHTML = "";

  if (!route || !route.path || route.path.length < 2) return;

  // Reset node circle highlighting
  document.querySelectorAll(".node-circle").forEach(circle => {
    circle.classList.remove("start-node", "dest-node");
  });

  // Highlight Start & Destination Nodes
  const startId = route.path[0];
  const destId = route.path[route.path.length - 1];
  const startCircle = document.querySelector(`.map-node-group[data-node-id="${startId}"] .node-circle`);
  const destCircle = document.querySelector(`.map-node-group[data-node-id="${destId}"] .node-circle`);
  if (startCircle) startCircle.classList.add("start-node");
  if (destCircle) destCircle.classList.add("dest-node");

  // Draw Polyline for Route
  const points = route.path.map(id => {
    const node = stationNodes[id];
    return `${node.x},${node.y}`;
  }).join(" ");

  const polyline = document.createElementNS("http://www.w3.org/2000/svg", "polyline");
  polyline.setAttribute("points", points);
  polyline.setAttribute("class", "route-edge");
  polyline.setAttribute("marker-end", "url(#arrow)");
  svgRouteLayer.appendChild(polyline);
}

// --------------------------------------------------------------------------
// 9. NODE CONTEXT POPUP HANDLER
// --------------------------------------------------------------------------
function openNodePopup(node, event) {
  const popup = document.getElementById("node-popup");
  const title = document.getElementById("popup-node-title");
  const desc = document.getElementById("popup-node-desc");
  if (!popup || !title) return;

  appState.selectedNodeId = node.id;
  title.textContent = node.names[appState.currentLang] || node.names["en"];
  if (desc) desc.textContent = `Coordinates: (${node.x}, ${node.y})`;

  const mapViewport = document.getElementById("map-viewport");
  const rect = mapViewport.getBoundingClientRect();
  const left = event.clientX - rect.left;
  const top = event.clientY - rect.top;

  popup.style.left = `${left}px`;
  popup.style.top = `${top}px`;
  popup.classList.remove("hidden");
}

function closeNodePopup() {
  const popup = document.getElementById("node-popup");
  if (popup) popup.classList.add("hidden");
}

// --------------------------------------------------------------------------
// 10. SETUP ALL EVENT LISTENERS
// --------------------------------------------------------------------------
function setupEventListeners() {
  // Navigation Tabs Switching (Desktop & Mobile)
  const tabs = document.querySelectorAll(".nav-tab, .mobile-nav-btn");
  tabs.forEach(tab => {
    tab.addEventListener("click", function () {
      const targetView = this.getAttribute("data-target");
      if (!targetView) return;

      tabs.forEach(t => t.classList.remove("active"));
      document.querySelectorAll(`.nav-tab[data-target="${targetView}"], .mobile-nav-btn[data-target="${targetView}"]`)
        .forEach(t => t.classList.add("active"));

      document.querySelectorAll(".app-view").forEach(view => {
        view.classList.remove("active");
      });
      const activeViewEl = document.getElementById(targetView);
      if (activeViewEl) activeViewEl.classList.add("active");
    });
  });

  // Hero Section Buttons
  const btnHomeNav = document.getElementById("btn-home-start-nav");
  if (btnHomeNav) {
    btnHomeNav.addEventListener("click", () => switchTab("view-map"));
  }
  const btnHomeFac = document.getElementById("btn-home-facilities");
  if (btnHomeFac) {
    btnHomeFac.addEventListener("click", () => switchTab("view-facilities"));
  }
  const btnHomeAssist = document.getElementById("btn-home-assistance");
  if (btnHomeAssist) {
    btnHomeAssist.addEventListener("click", () => switchTab("view-help"));
  }

  // Assistance Profile Selection Cards
  const modeCards = document.querySelectorAll(".mode-card");
  modeCards.forEach(card => {
    card.addEventListener("click", function () {
      modeCards.forEach(c => c.classList.remove("active"));
      this.classList.add("active");

      const mode = this.getAttribute("data-mode");
      appState.activeProfile = mode;

      const chkWheelchair = document.getElementById("chk-wheelchair");
      const chkNoStairs = document.getElementById("chk-no-stairs");
      const modeChip = document.getElementById("chip-mode-indicator");

      if (mode === "wheelchair") {
        if (chkWheelchair) chkWheelchair.checked = true;
        if (chkNoStairs) chkNoStairs.checked = true;
        if (modeChip) modeChip.textContent = "Wheelchair Mode";
      } else if (mode === "visual") {
        appState.highContrast = true;
        document.body.classList.add("high-contrast");
        const speechToolbar = document.getElementById("speech-toolbar");
        if (speechToolbar) speechToolbar.classList.remove("hidden");
        if (modeChip) modeChip.textContent = "Visual Mode";
      } else {
        if (modeChip) modeChip.textContent = "General Mode";
      }
    });
  });

  // Swap Locations Button
  const btnSwap = document.getElementById("btn-swap-locations");
  if (btnSwap) {
    btnSwap.addEventListener("click", function () {
      const startSelect = document.getElementById("select-start");
      const destSelect = document.getElementById("select-dest");
      if (startSelect && destSelect) {
        const temp = startSelect.value;
        startSelect.value = destSelect.value;
        destSelect.value = temp;
      }
    });
  }

  // Find Route Button & Form Submit
  const routeForm = document.getElementById("route-form");
  if (routeForm) {
    routeForm.addEventListener("submit", function (e) {
      e.preventDefault();
      calculateAndDisplayRoute();
    });
  }

  // Popup Context Buttons
  const btnPopupStart = document.getElementById("btn-popup-set-start");
  if (btnPopupStart) {
    btnPopupStart.addEventListener("click", function () {
      const startSelect = document.getElementById("select-start");
      if (startSelect && appState.selectedNodeId) {
        startSelect.value = appState.selectedNodeId;
      }
      closeNodePopup();
    });
  }
  const btnPopupDest = document.getElementById("btn-popup-set-dest");
  if (btnPopupDest) {
    btnPopupDest.addEventListener("click", function () {
      const destSelect = document.getElementById("select-dest");
      if (destSelect && appState.selectedNodeId) {
        destSelect.value = appState.selectedNodeId;
      }
      closeNodePopup();
    });
  }
  const btnPopupClose = document.getElementById("btn-popup-close");
  if (btnPopupClose) {
    btnPopupClose.addEventListener("click", closeNodePopup);
  }

  // Map Zoom Controls
  const btnZoomIn = document.getElementById("btn-map-zoom-in");
  const btnZoomOut = document.getElementById("btn-map-zoom-out");
  const btnReset = document.getElementById("btn-map-reset");
  const zoomGroup = document.getElementById("map-zoom-group");

  if (btnZoomIn && zoomGroup) {
    btnZoomIn.addEventListener("click", () => {
      appState.mapZoom = Math.min(appState.mapZoom + 0.25, 2.5);
      zoomGroup.setAttribute("transform", `scale(${appState.mapZoom})`);
    });
  }
  if (btnZoomOut && zoomGroup) {
    btnZoomOut.addEventListener("click", () => {
      appState.mapZoom = Math.max(appState.mapZoom - 0.25, 0.75);
      zoomGroup.setAttribute("transform", `scale(${appState.mapZoom})`);
    });
  }
  if (btnReset && zoomGroup) {
    btnReset.addEventListener("click", () => {
      appState.mapZoom = 1;
      zoomGroup.setAttribute("transform", `scale(1)`);
    });
  }

  // Text-to-Speech Controls
  const btnSpeechStep = document.getElementById("btn-speech-read-step");
  if (btnSpeechStep) {
    btnSpeechStep.addEventListener("click", function () {
      if (appState.calculatedRoute && appState.calculatedRoute.steps.length > 0) {
        const step = appState.calculatedRoute.steps[appState.currentStepIndex];
        speakText(`Step ${step.stepNumber}: ${step.modeText} from ${step.from} to ${step.to}`);
      }
    });
  }

  // Navigation Steps Prev / Next Controls
  const btnPrev = document.getElementById("btn-prev-step");
  const btnNext = document.getElementById("btn-next-step");
  if (btnPrev && btnNext) {
    btnPrev.addEventListener("click", () => changeNavigationStep(-1));
    btnNext.addEventListener("click", () => changeNavigationStep(1));
  }

  // Navigation Action Buttons (Start / Cancel Nav)
  const btnStartNavAction = document.getElementById("btn-start-nav");
  const btnCancelNavAction = document.getElementById("btn-cancel-nav");
  if (btnStartNavAction) {
    btnStartNavAction.addEventListener("click", startActiveNavigation);
  }
  if (btnCancelNavAction) {
    btnCancelNavAction.addEventListener("click", cancelActiveNavigation);
  }

  // Facilities Category Filter Pills
  const catPills = document.querySelectorAll(".cat-pill");
  catPills.forEach(pill => {
    pill.addEventListener("click", function () {
      catPills.forEach(p => p.classList.remove("active"));
      this.classList.add("active");
      const category = this.getAttribute("data-category");
      renderFacilitiesList(category);
    });
  });

  // Facilities Search Box
  const facilitySearch = document.getElementById("facility-search-input");
  if (facilitySearch) {
    facilitySearch.addEventListener("input", function () {
      const query = this.value.toLowerCase();
      renderFacilitiesList("all", query);
    });
  }

  // Language Selector Change
  const langSelect = document.getElementById("lang-select");
  if (langSelect) {
    langSelect.addEventListener("change", function () {
      updateLanguage(this.value);
    });
  }

  // High Contrast Mode Toggle
  const btnContrast = document.getElementById("btn-toggle-contrast");
  if (btnContrast) {
    btnContrast.addEventListener("click", toggleHighContrast);
  }

  // Font Size Buttons
  const btnTextDec = document.getElementById("btn-text-decrease");
  const btnTextInc = document.getElementById("btn-text-increase");
  if (btnTextDec && btnTextInc) {
    btnTextDec.addEventListener("click", () => changeTextSize(-1));
    btnTextInc.addEventListener("click", () => changeTextSize(1));
  }

  // Modals Open / Close Event Handlers
  setupModalHandlers();
}

// --------------------------------------------------------------------------
// 11. CALCULATE AND DISPLAY ROUTE
// --------------------------------------------------------------------------
function calculateAndDisplayRoute() {
  const startSelect = document.getElementById("select-start");
  const destSelect = document.getElementById("select-dest");
  const chkWheelchair = document.getElementById("chk-wheelchair");
  const chkNoStairs = document.getElementById("chk-no-stairs");
  const stepsContainer = document.getElementById("steps-container");
  const distTag = document.getElementById("route-distance-tag");
  const timeTag = document.getElementById("route-time-tag");
  const navActionBtns = document.getElementById("nav-action-buttons");

  if (!startSelect || !destSelect || !stepsContainer) return;

  const startId = startSelect.value;
  const destId = destSelect.value;

  if (startId === destId) {
    stepsContainer.innerHTML = `
      <div class="alert-banner-warning text-center">
        <strong>📍 Same Location Selected</strong>
        <p>You are already at your destination!</p>
      </div>`;
    return;
  }

  const route = findShortestRoute(startId, destId, {
    requireWheelchair: chkWheelchair ? chkWheelchair.checked : false,
    avoidStairs: chkNoStairs ? chkNoStairs.checked : false
  });

  if (!route) {
    stepsContainer.innerHTML = `
      <div class="alert-banner-warning text-center">
        <strong>⚠️ No Route Found</strong>
        <p>No available step-free path between selected locations. Try unchecking stair restrictions or reporting an alternate path.</p>
      </div>`;
    return;
  }

  appState.calculatedRoute = route;
  appState.currentStepIndex = 0;

  if (distTag) distTag.textContent = `${route.totalDistance} m`;
  if (timeTag) timeTag.textContent = `${route.estimatedTimeMins} mins`;

  // Render Steps HTML
  const stepsHtml = route.steps.map((step, idx) => `
    <div class="step-card ${idx === 0 ? 'active' : ''}" data-step-index="${idx}">
      <div class="step-number">${step.stepNumber}</div>
      <div class="step-content">
        <div class="step-title">${step.icon} ${step.modeText}</div>
        <div class="step-detail">From <strong>${step.from}</strong> to <strong>${step.to}</strong> (${step.distance}m)</div>
      </div>
    </div>
  `).join("");

  stepsContainer.innerHTML = stepsHtml;

  // Show Step Controls & Action Buttons
  const stepControls = document.getElementById("step-nav-controls");
  if (stepControls) stepControls.classList.remove("hidden");
  if (navActionBtns) navActionBtns.classList.remove("hidden");

  // Render route polyline on SVG map
  renderRouteOnMap(route);

  // Auto-speak first instruction if TTS is enabled
  if (appState.ttsEnabled) {
    speakText(`Route found. Distance ${route.totalDistance} meters. Step 1: ${route.steps[0].modeText}`);
  }
}

// --------------------------------------------------------------------------
// 12. ACTIVE NAVIGATION STEP COUNTER & ACTIONS
// --------------------------------------------------------------------------
function changeNavigationStep(delta) {
  if (!appState.calculatedRoute) return;
  const maxIdx = appState.calculatedRoute.steps.length - 1;
  appState.currentStepIndex = Math.max(0, Math.min(maxIdx, appState.currentStepIndex + delta));

  document.querySelectorAll(".step-card").forEach((card, idx) => {
    if (idx === appState.currentStepIndex) {
      card.classList.add("active");
      card.scrollIntoView({ behavior: "smooth", block: "nearest" });
    } else {
      card.classList.remove("active");
    }
  });

  const stepCounter = document.getElementById("step-counter");
  if (stepCounter) {
    stepCounter.textContent = `Step ${appState.currentStepIndex + 1} of ${maxIdx + 1}`;
  }

  const btnPrev = document.getElementById("btn-prev-step");
  const btnNext = document.getElementById("btn-next-step");
  if (btnPrev) btnPrev.disabled = (appState.currentStepIndex === 0);
  if (btnNext) btnNext.disabled = (appState.currentStepIndex === maxIdx);

  if (appState.ttsEnabled) {
    const step = appState.calculatedRoute.steps[appState.currentStepIndex];
    speakText(`Step ${appState.currentStepIndex + 1}: ${step.modeText} to ${step.to}`);
  }
}

function startActiveNavigation() {
  appState.isNavigating = true;
  const statusBanner = document.getElementById("nav-active-status");
  const btnStart = document.getElementById("btn-start-nav");
  const btnCancel = document.getElementById("btn-cancel-nav");

  if (statusBanner) statusBanner.classList.remove("hidden");
  if (btnStart) btnStart.classList.add("hidden");
  if (btnCancel) btnCancel.classList.remove("hidden");
}

function cancelActiveNavigation() {
  appState.isNavigating = false;
  const statusBanner = document.getElementById("nav-active-status");
  const btnStart = document.getElementById("btn-start-nav");
  const btnCancel = document.getElementById("btn-cancel-nav");

  if (statusBanner) statusBanner.classList.add("hidden");
  if (btnStart) btnStart.classList.remove("hidden");
  if (btnCancel) btnCancel.classList.add("hidden");
}

// --------------------------------------------------------------------------
// 13. RENDER FACILITIES LIST & SEARCH
// --------------------------------------------------------------------------
function renderFacilitiesList(categoryFilter = "all", searchQuery = "") {
  const grid = document.getElementById("facilities-grid");
  if (!grid) return;

  const facilities = Object.values(stationNodes).filter(node => {
    const matchesCategory = (categoryFilter === "all" || node.category === categoryFilter);
    const name = (node.names[appState.currentLang] || node.names["en"]).toLowerCase();
    const matchesSearch = (!searchQuery || name.includes(searchQuery));
    return matchesCategory && matchesSearch;
  });

  const html = facilities.map(fac => {
    const name = fac.names[appState.currentLang] || fac.names["en"];
    return `
      <div class="facility-card">
        <div class="facility-top">
          <div class="facility-icon-badge">📍</div>
          <span class="facility-location-tag">${fac.category.toUpperCase()}</span>
        </div>
        <div class="facility-title">${name}</div>
        <div class="facility-desc">Located within Mysuru Junction station layout. Click below to start route navigation.</div>
        <button class="btn btn-primary btn-sm btn-nav-facility" data-node-id="${fac.id}">
          ${i18n[appState.currentLang].navigateHere || "Navigate Here"}
        </button>
      </div>
    `;
  }).join("");

  grid.innerHTML = html;

  // Bind Navigate Here buttons
  document.querySelectorAll(".btn-nav-facility").forEach(btn => {
    btn.addEventListener("click", function () {
      const nodeId = this.getAttribute("data-node-id");
      const destSelect = document.getElementById("select-dest");
      if (destSelect) destSelect.value = nodeId;
      switchTab("view-map");
      calculateAndDisplayRoute();
    });
  });
}

// --------------------------------------------------------------------------
// 14. MULTILINGUAL DICTIONARY UPDATER
// --------------------------------------------------------------------------
function updateLanguage(lang) {
  if (!i18n[lang]) return;
  appState.currentLang = lang;

  const dict = i18n[lang];

  // Update static text elements by ID
  const textMappings = {
    "app-title": dict.appTitle,
    "app-subtitle": dict.appSubtitle,
    "disclaimer-badge-text": dict.disclaimerBadge,
    "disclaimer-text": dict.disclaimerText,
    "tab-text-home": dict.tabHome,
    "tab-text-map": dict.tabMap,
    "tab-text-facilities": dict.tabFacilities,
    "tab-text-help": dict.tabHelp,
    "mob-txt-home": dict.tabHome,
    "mob-txt-map": dict.tabMap,
    "mob-txt-facilities": dict.tabFacilities,
    "mob-txt-help": dict.tabHelp,
    "home-heading": dict.welcomeHeading,
    "hero-desc": dict.heroDesc,
    "txt-home-start-nav": dict.btnStartNav,
    "txt-home-facilities": dict.btnFacilities,
    "txt-home-assistance": dict.btnAssistance,
    "title-assistance-modes": dict.assistanceModesTitle,
    "sub-assistance-modes": dict.assistanceModesSub,
    "mode-title-general": dict.modeGeneralTitle,
    "mode-desc-general": dict.modeGeneralDesc,
    "mode-title-wheelchair": dict.modeWheelchairTitle,
    "mode-desc-wheelchair": dict.modeWheelchairDesc,
    "mode-title-visual": dict.modeVisualTitle,
    "mode-desc-visual": dict.modeVisualDesc,
    "mode-title-hearing": dict.modeHearingTitle,
    "mode-desc-hearing": dict.modeHearingDesc,
    "map-heading": dict.routeFinderTitle,
    "txt-btn-report-blockage": dict.reportBlockageBtn,
    "label-start-point": dict.labelStartPoint,
    "label-dest-point": dict.labelDestPoint,
    "txt-gps-locate": dict.locateMe,
    "lbl-chk-wheelchair": dict.wheelchairOpt,
    "lbl-chk-no-stairs": dict.noStairsOpt,
    "txt-find-route": dict.btnFindRoute,
    "title-route-directions": dict.routeDirectionsTitle,
    "txt-speech-read": dict.speakInstruction,
    "txt-speech-dest": dict.readDestination,
    "txt-empty-steps-title": dict.noRouteTitle,
    "txt-empty-steps-desc": dict.noRouteDesc,
    "txt-prev-step": dict.prevStep,
    "txt-next-step": dict.nextStep,
    "txt-start-nav-action": dict.startNavAction,
    "txt-cancel-nav-action": dict.cancelNavAction,
    "facilities-heading": dict.facilitiesHeading,
    "sub-facilities": dict.facilitiesSub,
    "help-heading": dict.helpHeading,
    "desc-help-form": dict.helpFormDesc,
    "txt-submit-help": dict.submitHelpReq
  };

  Object.keys(textMappings).forEach(id => {
    const el = document.getElementById(id);
    if (el && textMappings[id]) el.textContent = textMappings[id];
  });

  // Refresh Dropdowns & Map SVG Labels
  populateDropdowns();
  renderSvgMap();
  renderFacilitiesList("all");
}

// --------------------------------------------------------------------------
// 15. ACCESSIBILITY TOGGLES & MODALS HANDLERS
// --------------------------------------------------------------------------
function toggleHighContrast() {
  appState.highContrast = !appState.highContrast;
  if (appState.highContrast) {
    document.body.classList.add("high-contrast");
  } else {
    document.body.classList.remove("high-contrast");
  }
}

function changeTextSize(delta) {
  const sizes = ["normal", "large", "xlarge"];
  let currIdx = sizes.indexOf(appState.textSize);
  currIdx = Math.max(0, Math.min(sizes.length - 1, currIdx + delta));
  appState.textSize = sizes[currIdx];

  document.documentElement.setAttribute("data-text-size", appState.textSize);
  const indicator = document.getElementById("current-text-size");
  if (indicator) {
    indicator.textContent = appState.textSize === "normal" ? "100%" : (appState.textSize === "large" ? "125%" : "150%");
  }
}

function speakText(text) {
  if ('speechSynthesis' in window) {
    window.speechSynthesis.cancel();
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.rate = 0.95;
    window.speechSynthesis.speak(utterance);
  }
}

function switchTab(viewId) {
  const tabBtn = document.querySelector(`.nav-tab[data-target="${viewId}"], .mobile-nav-btn[data-target="${viewId}"]`);
  if (tabBtn) tabBtn.click();
}

function setupModalHandlers() {
  // Accessibility Modal
  const btnOpenA11y = document.getElementById("btn-open-a11y");
  const btnCloseA11y = document.getElementById("btn-close-a11y");
  const btnSaveA11y = document.getElementById("btn-save-a11y");
  const modalA11y = document.getElementById("modal-a11y");

  if (btnOpenA11y && modalA11y) {
    btnOpenA11y.addEventListener("click", () => modalA11y.classList.remove("hidden"));
  }
  if (btnCloseA11y && modalA11y) {
    btnCloseA11y.addEventListener("click", () => modalA11y.classList.add("hidden"));
  }
  if (btnSaveA11y && modalA11y) {
    btnSaveA11y.addEventListener("click", () => modalA11y.classList.add("hidden"));
  }

  // Blockage Modal
  const btnOpenBlk = document.getElementById("btn-open-blockage-modal");
  const btnCloseBlk = document.getElementById("btn-close-blockage-modal");
  const modalBlk = document.getElementById("modal-report-blockage");
  const formBlk = document.getElementById("form-report-blockage");

  if (btnOpenBlk && modalBlk) {
    btnOpenBlk.addEventListener("click", () => modalBlk.classList.remove("hidden"));
  }
  if (btnCloseBlk && modalBlk) {
    btnCloseBlk.addEventListener("click", () => modalBlk.classList.add("hidden"));
  }
  if (formBlk) {
    formBlk.addEventListener("submit", function (e) {
      e.preventDefault();
      const nodeSelect = document.getElementById("select-blockage-node");
      if (nodeSelect) {
        const nodeId = nodeSelect.value;
        appState.blockedNodes.add(nodeId);
        renderSvgMap();
        const banner = document.getElementById("blockage-alert-banner");
        if (banner) banner.classList.remove("hidden");
        if (modalBlk) modalBlk.classList.add("hidden");
      }
    });
  }

  // Help Form Submit Modal
  const helpForm = document.getElementById("assistance-form");
  const modalConfirm = document.getElementById("modal-request-confirm");
  const btnCloseConfirm = document.getElementById("btn-close-req-confirm");

  if (helpForm) {
    helpForm.addEventListener("submit", function (e) {
      e.preventDefault();
      if (modalConfirm) modalConfirm.classList.remove("hidden");
    });
  }
  if (btnCloseConfirm && modalConfirm) {
    btnCloseConfirm.addEventListener("click", () => modalConfirm.classList.add("hidden"));
  }
}