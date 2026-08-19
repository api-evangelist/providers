---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.2
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 445
  human_in_the_loop: 0
  name: Ios Agentic Access
  operation_count: 1208
  slug: ios-agentic-access
  summary_line: 1208 operations · 445 acting
api_count: 199
apis:
- description: The App Store Server API is the server-to-server REST API for managing App Store transactions — looking up transaction history, fetching all subscription statuses for a customer, requesting test notif
  name: App Store Server API
  slug: app-store-server-api
- description: App Store Server Notifications v2 is Apple's webhook surface for in-app purchase and subscription lifecycle events — SUBSCRIBED, DID_RENEW, EXPIRED, REFUND, GRACE_PERIOD_EXPIRED, REVOKE, CONSUMPTION_R
  name: App Store Server Notifications
  slug: app-store-server-notifications
- description: The Apple Push Notification service (APNs) is the HTTP/2 + JSON push delivery surface for sending remote notifications, background updates, VoIP pushes, and Live Activity updates to iOS, iPadOS, watch
  name: Apple Push Notification Service (APNs)
  slug: apns
- description: DeviceCheck allows servers to set and query two bits of per-device state and to verify that a request is coming from a genuine Apple device. App Attest, exposed through the same service, lets a server
  name: DeviceCheck and App Attest
  slug: devicecheck
- description: Sign in with Apple is Apple's OpenID Connect-style identity provider for iOS, web, and other Apple-platform apps. The REST surface, hosted at appleid.apple.com, exposes /auth/token (authorization-code
  name: Sign in with Apple REST API
  slug: sign-in-with-apple
- description: 'The Apple Music API is Apple''s REST surface for Apple Music catalog, library, ratings, playlists, recommendations, and search. Calls are authenticated with a developer token (JWT) and, when accessing '
  name: Apple Music API
  slug: apple-music-api
- description: The PassKit Web Service is a server-side HTTP contract that Wallet pass providers must implement so that Apple Wallet can register devices, enumerate pass serial numbers, fetch the latest pass version
  name: Wallet / PassKit Web Service
  slug: wallet-passkit-web-service
- description: The AccessibilityDeclarations API from iOS — 2 operation(s) for accessibilitydeclarations.
  name: iOS AccessibilityDeclarations API
  slug: ios-accessibilitydeclarations-api
- description: The Actors API from iOS — 2 operation(s) for actors.
  name: iOS Actors API
  slug: ios-actors-api
- description: The AgeRatingDeclarations API from iOS — 1 operation(s) for ageratingdeclarations.
  name: iOS AgeRatingDeclarations API
  slug: ios-ageratingdeclarations-api
- description: The AlternativeDistributionDomains API from iOS — 2 operation(s) for alternativedistributiondomains.
  name: iOS AlternativeDistributionDomains API
  slug: ios-alternativedistributiondomains-api
- description: The AlternativeDistributionKeys API from iOS — 2 operation(s) for alternativedistributionkeys.
  name: iOS AlternativeDistributionKeys API
  slug: ios-alternativedistributionkeys-api
- description: The AlternativeDistributionPackageDeltas API from iOS — 1 operation(s) for alternativedistributionpackagedeltas.
  name: iOS AlternativeDistributionPackageDeltas API
  slug: ios-alternativedistributionpackagedeltas-api
- description: The AlternativeDistributionPackages API from iOS — 4 operation(s) for alternativedistributionpackages.
  name: iOS AlternativeDistributionPackages API
  slug: ios-alternativedistributionpackages-api
- description: The AlternativeDistributionPackageVariants API from iOS — 1 operation(s) for alternativedistributionpackagevariants.
  name: iOS AlternativeDistributionPackageVariants API
  slug: ios-alternativedistributionpackagevariants-api
- description: The AlternativeDistributionPackageVersions API from iOS — 5 operation(s) for alternativedistributionpackageversions.
  name: iOS AlternativeDistributionPackageVersions API
  slug: ios-alternativedistributionpackageversions-api
- description: The AnalyticsReportInstances API from iOS — 3 operation(s) for analyticsreportinstances.
  name: iOS AnalyticsReportInstances API
  slug: ios-analyticsreportinstances-api
- description: The AnalyticsReportRequests API from iOS — 4 operation(s) for analyticsreportrequests.
  name: iOS AnalyticsReportRequests API
  slug: ios-analyticsreportrequests-api
- description: The AnalyticsReports API from iOS — 3 operation(s) for analyticsreports.
  name: iOS AnalyticsReports API
  slug: ios-analyticsreports-api
- description: The AnalyticsReportSegments API from iOS — 1 operation(s) for analyticsreportsegments.
  name: iOS AnalyticsReportSegments API
  slug: ios-analyticsreportsegments-api
- description: The AndroidToIosAppMappingDetails API from iOS — 2 operation(s) for androidtoiosappmappingdetails.
  name: iOS AndroidToIosAppMappingDetails API
  slug: ios-androidtoiosappmappingdetails-api
- description: The AppAvailabilities API from iOS — 4 operation(s) for appavailabilities.
  name: iOS AppAvailabilities API
  slug: ios-appavailabilities-api
- description: The AppCategories API from iOS — 6 operation(s) for appcategories.
  name: iOS AppCategories API
  slug: ios-appcategories-api
- description: The AppClipAdvancedExperienceImages API from iOS — 2 operation(s) for appclipadvancedexperienceimages.
  name: iOS AppClipAdvancedExperienceImages API
  slug: ios-appclipadvancedexperienceimages-api
- description: The AppClipAdvancedExperiences API from iOS — 2 operation(s) for appclipadvancedexperiences.
  name: iOS AppClipAdvancedExperiences API
  slug: ios-appclipadvancedexperiences-api
- description: The AppClipAppStoreReviewDetails API from iOS — 2 operation(s) for appclipappstorereviewdetails.
  name: iOS AppClipAppStoreReviewDetails API
  slug: ios-appclipappstorereviewdetails-api
- description: The AppClipDefaultExperienceLocalizations API from iOS — 4 operation(s) for appclipdefaultexperiencelocalizations.
  name: iOS AppClipDefaultExperienceLocalizations API
  slug: ios-appclipdefaultexperiencelocalizations-api
- description: The AppClipDefaultExperiences API from iOS — 8 operation(s) for appclipdefaultexperiences.
  name: iOS AppClipDefaultExperiences API
  slug: ios-appclipdefaultexperiences-api
- description: The AppClipHeaderImages API from iOS — 2 operation(s) for appclipheaderimages.
  name: iOS AppClipHeaderImages API
  slug: ios-appclipheaderimages-api
- description: The AppClips API from iOS — 5 operation(s) for appclips.
  name: iOS AppClips API
  slug: ios-appclips-api
- description: The AppCustomProductPageLocalizations API from iOS — 8 operation(s) for appcustomproductpagelocalizations.
  name: iOS AppCustomProductPageLocalizations API
  slug: ios-appcustomproductpagelocalizations-api
- description: The AppCustomProductPages API from iOS — 4 operation(s) for appcustomproductpages.
  name: iOS AppCustomProductPages API
  slug: ios-appcustomproductpages-api
- description: The AppCustomProductPageVersions API from iOS — 4 operation(s) for appcustomproductpageversions.
  name: iOS AppCustomProductPageVersions API
  slug: ios-appcustomproductpageversions-api
- description: The AppEncryptionDeclarationDocuments API from iOS — 2 operation(s) for appencryptiondeclarationdocuments.
  name: iOS AppEncryptionDeclarationDocuments API
  slug: ios-appencryptiondeclarationdocuments-api
- description: The AppEncryptionDeclarations API from iOS — 7 operation(s) for appencryptiondeclarations.
  name: iOS AppEncryptionDeclarations API
  slug: ios-appencryptiondeclarations-api
- description: The AppEventLocalizations API from iOS — 6 operation(s) for appeventlocalizations.
  name: iOS AppEventLocalizations API
  slug: ios-appeventlocalizations-api
- description: The AppEvents API from iOS — 4 operation(s) for appevents.
  name: iOS AppEvents API
  slug: ios-appevents-api
- description: The AppEventScreenshots API from iOS — 2 operation(s) for appeventscreenshots.
  name: iOS AppEventScreenshots API
  slug: ios-appeventscreenshots-api
- description: The AppEventVideoClips API from iOS — 2 operation(s) for appeventvideoclips.
  name: iOS AppEventVideoClips API
  slug: ios-appeventvideoclips-api
- description: The AppInfoLocalizations API from iOS — 2 operation(s) for appinfolocalizations.
  name: iOS AppInfoLocalizations API
  slug: ios-appinfolocalizations-api
- description: The AppInfos API from iOS — 19 operation(s) for appinfos.
  name: iOS AppInfos API
  slug: ios-appinfos-api
- description: The AppPreviews API from iOS — 2 operation(s) for apppreviews.
  name: iOS AppPreviews API
  slug: ios-apppreviews-api
- description: The AppPreviewSets API from iOS — 4 operation(s) for apppreviewsets.
  name: iOS AppPreviewSets API
  slug: ios-apppreviewsets-api
- description: The AppPricePoints API from iOS — 3 operation(s) for apppricepoints.
  name: iOS AppPricePoints API
  slug: ios-apppricepoints-api
- description: The AppPriceSchedules API from iOS — 8 operation(s) for apppriceschedules.
  name: iOS AppPriceSchedules API
  slug: ios-apppriceschedules-api
- description: The Apps API from iOS — 84 operation(s) for apps.
  name: iOS Apps API
  slug: ios-apps-api
- description: The AppScreenshots API from iOS — 2 operation(s) for appscreenshots.
  name: iOS AppScreenshots API
  slug: ios-appscreenshots-api
- description: The AppScreenshotSets API from iOS — 4 operation(s) for appscreenshotsets.
  name: iOS AppScreenshotSets API
  slug: ios-appscreenshotsets-api
- description: The AppStoreReviewAttachments API from iOS — 2 operation(s) for appstorereviewattachments.
  name: iOS AppStoreReviewAttachments API
  slug: ios-appstorereviewattachments-api
- description: The AppStoreReviewDetails API from iOS — 4 operation(s) for appstorereviewdetails.
  name: iOS AppStoreReviewDetails API
  slug: ios-appstorereviewdetails-api
- description: The AppStoreVersionExperiments API from iOS — 8 operation(s) for appstoreversionexperiments.
  name: iOS AppStoreVersionExperiments API
  slug: ios-appstoreversionexperiments-api
- description: The AppStoreVersionExperimentTreatmentLocalizations API from iOS — 6 operation(s) for appstoreversionexperimenttreatmentlocalizations.
  name: iOS AppStoreVersionExperimentTreatmentLocalizations API
  slug: ios-appstoreversionexperimenttreatmentlocalizations-api
- description: The AppStoreVersionExperimentTreatments API from iOS — 4 operation(s) for appstoreversionexperimenttreatments.
  name: iOS AppStoreVersionExperimentTreatments API
  slug: ios-appstoreversionexperimenttreatments-api
- description: The AppStoreVersionLocalizations API from iOS — 8 operation(s) for appstoreversionlocalizations.
  name: iOS AppStoreVersionLocalizations API
  slug: ios-appstoreversionlocalizations-api
- description: The AppStoreVersionPhasedReleases API from iOS — 2 operation(s) for appstoreversionphasedreleases.
  name: iOS AppStoreVersionPhasedReleases API
  slug: ios-appstoreversionphasedreleases-api
- description: The AppStoreVersionPromotions API from iOS — 1 operation(s) for appstoreversionpromotions.
  name: iOS AppStoreVersionPromotions API
  slug: ios-appstoreversionpromotions-api
- description: The AppStoreVersionReleaseRequests API from iOS — 1 operation(s) for appstoreversionreleaserequests.
  name: iOS AppStoreVersionReleaseRequests API
  slug: ios-appstoreversionreleaserequests-api
- description: The AppStoreVersions API from iOS — 26 operation(s) for appstoreversions.
  name: iOS AppStoreVersions API
  slug: ios-appstoreversions-api
- description: The AppStoreVersionSubmissions API from iOS — 1 operation(s) for appstoreversionsubmissions.
  name: iOS AppStoreVersionSubmissions API
  slug: ios-appstoreversionsubmissions-api
- description: The AppTags API from iOS — 3 operation(s) for apptags.
  name: iOS AppTags API
  slug: ios-apptags-api
- description: The BackgroundAssets API from iOS — 4 operation(s) for backgroundassets.
  name: iOS BackgroundAssets API
  slug: ios-backgroundassets-api
- description: The BackgroundAssetUploadFiles API from iOS — 2 operation(s) for backgroundassetuploadfiles.
  name: iOS BackgroundAssetUploadFiles API
  slug: ios-backgroundassetuploadfiles-api
- description: The BackgroundAssetVersionAppStoreReleases API from iOS — 1 operation(s) for backgroundassetversionappstorereleases.
  name: iOS BackgroundAssetVersionAppStoreReleases API
  slug: ios-backgroundassetversionappstorereleases-api
- description: The BackgroundAssetVersionExternalBetaReleases API from iOS — 1 operation(s) for backgroundassetversionexternalbetareleases.
  name: iOS BackgroundAssetVersionExternalBetaReleases API
  slug: ios-backgroundassetversionexternalbetareleases-api
- description: The BackgroundAssetVersionInternalBetaReleases API from iOS — 1 operation(s) for backgroundassetversioninternalbetareleases.
  name: iOS BackgroundAssetVersionInternalBetaReleases API
  slug: ios-backgroundassetversioninternalbetareleases-api
- description: The BackgroundAssetVersions API from iOS — 4 operation(s) for backgroundassetversions.
  name: iOS BackgroundAssetVersions API
  slug: ios-backgroundassetversions-api
- description: The BetaAppClipInvocationLocalizations API from iOS — 2 operation(s) for betaappclipinvocationlocalizations.
  name: iOS BetaAppClipInvocationLocalizations API
  slug: ios-betaappclipinvocationlocalizations-api
- description: The BetaAppClipInvocations API from iOS — 2 operation(s) for betaappclipinvocations.
  name: iOS BetaAppClipInvocations API
  slug: ios-betaappclipinvocations-api
- description: The BetaAppLocalizations API from iOS — 4 operation(s) for betaapplocalizations.
  name: iOS BetaAppLocalizations API
  slug: ios-betaapplocalizations-api
- description: The BetaAppReviewDetails API from iOS — 4 operation(s) for betaappreviewdetails.
  name: iOS BetaAppReviewDetails API
  slug: ios-betaappreviewdetails-api
- description: The BetaAppReviewSubmissions API from iOS — 4 operation(s) for betaappreviewsubmissions.
  name: iOS BetaAppReviewSubmissions API
  slug: ios-betaappreviewsubmissions-api
- description: The BetaBuildLocalizations API from iOS — 4 operation(s) for betabuildlocalizations.
  name: iOS BetaBuildLocalizations API
  slug: ios-betabuildlocalizations-api
- description: The BetaCrashLogs API from iOS — 1 operation(s) for betacrashlogs.
  name: iOS BetaCrashLogs API
  slug: ios-betacrashlogs-api
- description: The BetaFeedbackCrashSubmissions API from iOS — 3 operation(s) for betafeedbackcrashsubmissions.
  name: iOS BetaFeedbackCrashSubmissions API
  slug: ios-betafeedbackcrashsubmissions-api
- description: The BetaFeedbackScreenshotSubmissions API from iOS — 1 operation(s) for betafeedbackscreenshotsubmissions.
  name: iOS BetaFeedbackScreenshotSubmissions API
  slug: ios-betafeedbackscreenshotsubmissions-api
- description: The BetaGroups API from iOS — 14 operation(s) for betagroups.
  name: iOS BetaGroups API
  slug: ios-betagroups-api
- description: The BetaLicenseAgreements API from iOS — 4 operation(s) for betalicenseagreements.
  name: iOS BetaLicenseAgreements API
  slug: ios-betalicenseagreements-api
- description: The BetaRecruitmentCriteria API from iOS — 2 operation(s) for betarecruitmentcriteria.
  name: iOS BetaRecruitmentCriteria API
  slug: ios-betarecruitmentcriteria-api
- description: The BetaRecruitmentCriterionOptions API from iOS — 1 operation(s) for betarecruitmentcriterionoptions.
  name: iOS BetaRecruitmentCriterionOptions API
  slug: ios-betarecruitmentcriterionoptions-api
- description: The BetaTesterInvitations API from iOS — 1 operation(s) for betatesterinvitations.
  name: iOS BetaTesterInvitations API
  slug: ios-betatesterinvitations-api
- description: The BetaTesters API from iOS — 9 operation(s) for betatesters.
  name: iOS BetaTesters API
  slug: ios-betatesters-api
- description: The BuildBetaDetails API from iOS — 4 operation(s) for buildbetadetails.
  name: iOS BuildBetaDetails API
  slug: ios-buildbetadetails-api
- description: The BuildBetaNotifications API from iOS — 1 operation(s) for buildbetanotifications.
  name: iOS BuildBetaNotifications API
  slug: ios-buildbetanotifications-api
- description: The BuildBundles API from iOS — 8 operation(s) for buildbundles.
  name: iOS BuildBundles API
  slug: ios-buildbundles-api
- description: The Builds API from iOS — 25 operation(s) for builds.
  name: iOS Builds API
  slug: ios-builds-api
- description: The BuildUploadFiles API from iOS — 2 operation(s) for builduploadfiles.
  name: iOS BuildUploadFiles API
  slug: ios-builduploadfiles-api
- description: The BuildUploads API from iOS — 4 operation(s) for builduploads.
  name: iOS BuildUploads API
  slug: ios-builduploads-api
- description: The BundleIdCapabilities API from iOS — 2 operation(s) for bundleidcapabilities.
  name: iOS BundleIdCapabilities API
  slug: ios-bundleidcapabilities-api
- description: The BundleIds API from iOS — 8 operation(s) for bundleids.
  name: iOS BundleIds API
  slug: ios-bundleids-api
- description: The Certificates API from iOS — 4 operation(s) for certificates.
  name: iOS Certificates API
  slug: ios-certificates-api
- description: The CiArtifacts API from iOS — 1 operation(s) for ciartifacts.
  name: iOS CiArtifacts API
  slug: ios-ciartifacts-api
- description: The CiBuildActions API from iOS — 9 operation(s) for cibuildactions.
  name: iOS CiBuildActions API
  slug: ios-cibuildactions-api
- description: The CiBuildRuns API from iOS — 6 operation(s) for cibuildruns.
  name: iOS CiBuildRuns API
  slug: ios-cibuildruns-api
- description: The CiIssues API from iOS — 1 operation(s) for ciissues.
  name: iOS CiIssues API
  slug: ios-ciissues-api
- description: The CiMacOsVersions API from iOS — 4 operation(s) for cimacosversions.
  name: iOS CiMacOsVersions API
  slug: ios-cimacosversions-api
- description: The CiProducts API from iOS — 12 operation(s) for ciproducts.
  name: iOS CiProducts API
  slug: ios-ciproducts-api
- description: The CiTestResults API from iOS — 1 operation(s) for citestresults.
  name: iOS CiTestResults API
  slug: ios-citestresults-api
- description: The CiWorkflows API from iOS — 6 operation(s) for ciworkflows.
  name: iOS CiWorkflows API
  slug: ios-ciworkflows-api
- description: The CiXcodeVersions API from iOS — 4 operation(s) for cixcodeversions.
  name: iOS CiXcodeVersions API
  slug: ios-cixcodeversions-api
- description: The CustomerReviewResponses API from iOS — 2 operation(s) for customerreviewresponses.
  name: iOS CustomerReviewResponses API
  slug: ios-customerreviewresponses-api
- description: The CustomerReviews API from iOS — 3 operation(s) for customerreviews.
  name: iOS CustomerReviews API
  slug: ios-customerreviews-api
- description: The Devices API from iOS — 2 operation(s) for devices.
  name: iOS Devices API
  slug: ios-devices-api
- description: The DiagnosticSignatures API from iOS — 1 operation(s) for diagnosticsignatures.
  name: iOS DiagnosticSignatures API
  slug: ios-diagnosticsignatures-api
- description: The EndAppAvailabilityPreOrders API from iOS — 1 operation(s) for endappavailabilitypreorders.
  name: iOS EndAppAvailabilityPreOrders API
  slug: ios-endappavailabilitypreorders-api
- description: The EndUserLicenseAgreements API from iOS — 4 operation(s) for enduserlicenseagreements.
  name: iOS EndUserLicenseAgreements API
  slug: ios-enduserlicenseagreements-api
- description: The FinanceReports API from iOS — 1 operation(s) for financereports.
  name: iOS FinanceReports API
  slug: ios-financereports-api
- description: The GameCenterAchievementImages API from iOS — 4 operation(s) for gamecenterachievementimages.
  name: iOS GameCenterAchievementImages API
  slug: ios-gamecenterachievementimages-api
- description: The GameCenterAchievementLocalizations API from iOS — 10 operation(s) for gamecenterachievementlocalizations.
  name: iOS GameCenterAchievementLocalizations API
  slug: ios-gamecenterachievementlocalizations-api
- description: The GameCenterAchievementReleases API from iOS — 2 operation(s) for gamecenterachievementreleases.
  name: iOS GameCenterAchievementReleases API
  slug: ios-gamecenterachievementreleases-api
- description: The GameCenterAchievements API from iOS — 14 operation(s) for gamecenterachievements.
  name: iOS GameCenterAchievements API
  slug: ios-gamecenterachievements-api
- description: The GameCenterAchievementVersions API from iOS — 4 operation(s) for gamecenterachievementversions.
  name: iOS GameCenterAchievementVersions API
  slug: ios-gamecenterachievementversions-api
- description: The GameCenterActivities API from iOS — 8 operation(s) for gamecenteractivities.
  name: iOS GameCenterActivities API
  slug: ios-gamecenteractivities-api
- description: The GameCenterActivityImages API from iOS — 2 operation(s) for gamecenteractivityimages.
  name: iOS GameCenterActivityImages API
  slug: ios-gamecenteractivityimages-api
- description: The GameCenterActivityLocalizations API from iOS — 4 operation(s) for gamecenteractivitylocalizations.
  name: iOS GameCenterActivityLocalizations API
  slug: ios-gamecenteractivitylocalizations-api
- description: The GameCenterActivityVersionReleases API from iOS — 2 operation(s) for gamecenteractivityversionreleases.
  name: iOS GameCenterActivityVersionReleases API
  slug: ios-gamecenteractivityversionreleases-api
- description: The GameCenterActivityVersions API from iOS — 6 operation(s) for gamecenteractivityversions.
  name: iOS GameCenterActivityVersions API
  slug: ios-gamecenteractivityversions-api
- description: The GameCenterAppVersions API from iOS — 6 operation(s) for gamecenterappversions.
  name: iOS GameCenterAppVersions API
  slug: ios-gamecenterappversions-api
- description: The GameCenterChallengeImages API from iOS — 2 operation(s) for gamecenterchallengeimages.
  name: iOS GameCenterChallengeImages API
  slug: ios-gamecenterchallengeimages-api
- description: The GameCenterChallengeLocalizations API from iOS — 4 operation(s) for gamecenterchallengelocalizations.
  name: iOS GameCenterChallengeLocalizations API
  slug: ios-gamecenterchallengelocalizations-api
- description: The GameCenterChallenges API from iOS — 6 operation(s) for gamecenterchallenges.
  name: iOS GameCenterChallenges API
  slug: ios-gamecenterchallenges-api
- description: The GameCenterChallengeVersionReleases API from iOS — 2 operation(s) for gamecenterchallengeversionreleases.
  name: iOS GameCenterChallengeVersionReleases API
  slug: ios-gamecenterchallengeversionreleases-api
- description: The GameCenterChallengeVersions API from iOS — 6 operation(s) for gamecenterchallengeversions.
  name: iOS GameCenterChallengeVersions API
  slug: ios-gamecenterchallengeversions-api
- description: The GameCenterDetails API from iOS — 35 operation(s) for gamecenterdetails.
  name: iOS GameCenterDetails API
  slug: ios-gamecenterdetails-api
- description: The GameCenterEnabledVersions API from iOS — 2 operation(s) for gamecenterenabledversions.
  name: iOS GameCenterEnabledVersions API
  slug: ios-gamecenterenabledversions-api
- description: The GameCenterGroups API from iOS — 20 operation(s) for gamecentergroups.
  name: iOS GameCenterGroups API
  slug: ios-gamecentergroups-api
- description: The GameCenterLeaderboardEntrySubmissions API from iOS — 1 operation(s) for gamecenterleaderboardentrysubmissions.
  name: iOS GameCenterLeaderboardEntrySubmissions API
  slug: ios-gamecenterleaderboardentrysubmissions-api
- description: The GameCenterLeaderboardImages API from iOS — 4 operation(s) for gamecenterleaderboardimages.
  name: iOS GameCenterLeaderboardImages API
  slug: ios-gamecenterleaderboardimages-api
- description: The GameCenterLeaderboardLocalizations API from iOS — 8 operation(s) for gamecenterleaderboardlocalizations.
  name: iOS GameCenterLeaderboardLocalizations API
  slug: ios-gamecenterleaderboardlocalizations-api
- description: The GameCenterLeaderboardReleases API from iOS — 2 operation(s) for gamecenterleaderboardreleases.
  name: iOS GameCenterLeaderboardReleases API
  slug: ios-gamecenterleaderboardreleases-api
- description: The GameCenterLeaderboards API from iOS — 16 operation(s) for gamecenterleaderboards.
  name: iOS GameCenterLeaderboards API
  slug: ios-gamecenterleaderboards-api
- description: The GameCenterLeaderboardSetImages API from iOS — 4 operation(s) for gamecenterleaderboardsetimages.
  name: iOS GameCenterLeaderboardSetImages API
  slug: ios-gamecenterleaderboardsetimages-api
- description: The GameCenterLeaderboardSetLocalizations API from iOS — 8 operation(s) for gamecenterleaderboardsetlocalizations.
  name: iOS GameCenterLeaderboardSetLocalizations API
  slug: ios-gamecenterleaderboardsetlocalizations-api
- description: The GameCenterLeaderboardSetMemberLocalizations API from iOS — 6 operation(s) for gamecenterleaderboardsetmemberlocalizations.
  name: iOS GameCenterLeaderboardSetMemberLocalizations API
  slug: ios-gamecenterleaderboardsetmemberlocalizations-api
- description: The GameCenterLeaderboardSetReleases API from iOS — 2 operation(s) for gamecenterleaderboardsetreleases.
  name: iOS GameCenterLeaderboardSetReleases API
  slug: ios-gamecenterleaderboardsetreleases-api
- description: The GameCenterLeaderboardSets API from iOS — 16 operation(s) for gamecenterleaderboardsets.
  name: iOS GameCenterLeaderboardSets API
  slug: ios-gamecenterleaderboardsets-api
- description: The GameCenterLeaderboardSetVersions API from iOS — 4 operation(s) for gamecenterleaderboardsetversions.
  name: iOS GameCenterLeaderboardSetVersions API
  slug: ios-gamecenterleaderboardsetversions-api
- description: The GameCenterLeaderboardVersions API from iOS — 4 operation(s) for gamecenterleaderboardversions.
  name: iOS GameCenterLeaderboardVersions API
  slug: ios-gamecenterleaderboardversions-api
- description: The GameCenterMatchmakingQueues API from iOS — 7 operation(s) for gamecentermatchmakingqueues.
  name: iOS GameCenterMatchmakingQueues API
  slug: ios-gamecentermatchmakingqueues-api
- description: The GameCenterMatchmakingRules API from iOS — 5 operation(s) for gamecentermatchmakingrules.
  name: iOS GameCenterMatchmakingRules API
  slug: ios-gamecentermatchmakingrules-api
- description: The GameCenterMatchmakingRuleSets API from iOS — 8 operation(s) for gamecentermatchmakingrulesets.
  name: iOS GameCenterMatchmakingRuleSets API
  slug: ios-gamecentermatchmakingrulesets-api
- description: The GameCenterMatchmakingRuleSetTests API from iOS — 1 operation(s) for gamecentermatchmakingrulesettests.
  name: iOS GameCenterMatchmakingRuleSetTests API
  slug: ios-gamecentermatchmakingrulesettests-api
- description: The GameCenterMatchmakingTeams API from iOS — 2 operation(s) for gamecentermatchmakingteams.
  name: iOS GameCenterMatchmakingTeams API
  slug: ios-gamecentermatchmakingteams-api
- description: The GameCenterPlayerAchievementSubmissions API from iOS — 1 operation(s) for gamecenterplayerachievementsubmissions.
  name: iOS GameCenterPlayerAchievementSubmissions API
  slug: ios-gamecenterplayerachievementsubmissions-api
- description: The InAppPurchaseAppStoreReviewScreenshots API from iOS — 2 operation(s) for inapppurchaseappstorereviewscreenshots.
  name: iOS InAppPurchaseAppStoreReviewScreenshots API
  slug: ios-inapppurchaseappstorereviewscreenshots-api
- description: The InAppPurchaseAvailabilities API from iOS — 4 operation(s) for inapppurchaseavailabilities.
  name: iOS InAppPurchaseAvailabilities API
  slug: ios-inapppurchaseavailabilities-api
- description: The InAppPurchaseContents API from iOS — 1 operation(s) for inapppurchasecontents.
  name: iOS InAppPurchaseContents API
  slug: ios-inapppurchasecontents-api
- description: The InAppPurchaseImages API from iOS — 2 operation(s) for inapppurchaseimages.
  name: iOS InAppPurchaseImages API
  slug: ios-inapppurchaseimages-api
- description: The InAppPurchaseLocalizations API from iOS — 2 operation(s) for inapppurchaselocalizations.
  name: iOS InAppPurchaseLocalizations API
  slug: ios-inapppurchaselocalizations-api
- description: The InAppPurchaseOfferCodeCustomCodes API from iOS — 2 operation(s) for inapppurchaseoffercodecustomcodes.
  name: iOS InAppPurchaseOfferCodeCustomCodes API
  slug: ios-inapppurchaseoffercodecustomcodes-api
- description: The InAppPurchaseOfferCodeOneTimeUseCodes API from iOS — 3 operation(s) for inapppurchaseoffercodeonetimeusecodes.
  name: iOS InAppPurchaseOfferCodeOneTimeUseCodes API
  slug: ios-inapppurchaseoffercodeonetimeusecodes-api
- description: The InAppPurchaseOfferCodes API from iOS — 8 operation(s) for inapppurchaseoffercodes.
  name: iOS InAppPurchaseOfferCodes API
  slug: ios-inapppurchaseoffercodes-api
- description: The InAppPurchasePricePoints API from iOS — 2 operation(s) for inapppurchasepricepoints.
  name: iOS InAppPurchasePricePoints API
  slug: ios-inapppurchasepricepoints-api
- description: The InAppPurchasePriceSchedules API from iOS — 8 operation(s) for inapppurchasepriceschedules.
  name: iOS InAppPurchasePriceSchedules API
  slug: ios-inapppurchasepriceschedules-api
- description: The InAppPurchases API from iOS — 21 operation(s) for inapppurchases.
  name: iOS InAppPurchases API
  slug: ios-inapppurchases-api
- description: The InAppPurchaseSubmissions API from iOS — 1 operation(s) for inapppurchasesubmissions.
  name: iOS InAppPurchaseSubmissions API
  slug: ios-inapppurchasesubmissions-api
- description: The MarketplaceSearchDetails API from iOS — 2 operation(s) for marketplacesearchdetails.
  name: iOS MarketplaceSearchDetails API
  slug: ios-marketplacesearchdetails-api
- description: The MarketplaceWebhooks API from iOS — 2 operation(s) for marketplacewebhooks.
  name: iOS MarketplaceWebhooks API
  slug: ios-marketplacewebhooks-api
- description: The MerchantIds API from iOS — 4 operation(s) for merchantids.
  name: iOS MerchantIds API
  slug: ios-merchantids-api
- description: The Metrics API from iOS — 15 operation(s) for metrics.
  name: iOS Metrics API
  slug: ios-metrics-api
- description: The Nominations API from iOS — 2 operation(s) for nominations.
  name: iOS Nominations API
  slug: ios-nominations-api
- description: The PassTypeIds API from iOS — 4 operation(s) for passtypeids.
  name: iOS PassTypeIds API
  slug: ios-passtypeids-api
- description: The PreReleaseVersions API from iOS — 6 operation(s) for prereleaseversions.
  name: iOS PreReleaseVersions API
  slug: ios-prereleaseversions-api
- description: The Profiles API from iOS — 8 operation(s) for profiles.
  name: iOS Profiles API
  slug: ios-profiles-api
- description: The PromotedPurchases API from iOS — 2 operation(s) for promotedpurchases.
  name: iOS PromotedPurchases API
  slug: ios-promotedpurchases-api
- description: The ReviewSubmissionItems API from iOS — 2 operation(s) for reviewsubmissionitems.
  name: iOS ReviewSubmissionItems API
  slug: ios-reviewsubmissionitems-api
- description: The ReviewSubmissions API from iOS — 4 operation(s) for reviewsubmissions.
  name: iOS ReviewSubmissions API
  slug: ios-reviewsubmissions-api
- description: The RoutingAppCoverages API from iOS — 2 operation(s) for routingappcoverages.
  name: iOS RoutingAppCoverages API
  slug: ios-routingappcoverages-api
- description: The SalesReports API from iOS — 1 operation(s) for salesreports.
  name: iOS SalesReports API
  slug: ios-salesreports-api
- description: The SandboxTesters API from iOS — 2 operation(s) for sandboxtesters.
  name: iOS SandboxTesters API
  slug: ios-sandboxtesters-api
- description: The SandboxTestersClearPurchaseHistoryRequest API from iOS — 1 operation(s) for sandboxtestersclearpurchasehistoryrequest.
  name: iOS SandboxTestersClearPurchaseHistoryRequest API
  slug: ios-sandboxtestersclearpurchasehistoryrequest-api
- description: The ScmGitReferences API from iOS — 1 operation(s) for scmgitreferences.
  name: iOS ScmGitReferences API
  slug: ios-scmgitreferences-api
- description: The ScmProviders API from iOS — 4 operation(s) for scmproviders.
  name: iOS ScmProviders API
  slug: ios-scmproviders-api
- description: The ScmPullRequests API from iOS — 1 operation(s) for scmpullrequests.
  name: iOS ScmPullRequests API
  slug: ios-scmpullrequests-api
- description: The ScmRepositories API from iOS — 6 operation(s) for scmrepositories.
  name: iOS ScmRepositories API
  slug: ios-scmrepositories-api
- description: The SubscriptionAppStoreReviewScreenshots API from iOS — 2 operation(s) for subscriptionappstorereviewscreenshots.
  name: iOS SubscriptionAppStoreReviewScreenshots API
  slug: ios-subscriptionappstorereviewscreenshots-api
- description: The SubscriptionAvailabilities API from iOS — 4 operation(s) for subscriptionavailabilities.
  name: iOS SubscriptionAvailabilities API
  slug: ios-subscriptionavailabilities-api
- description: The SubscriptionGracePeriods API from iOS — 1 operation(s) for subscriptiongraceperiods.
  name: iOS SubscriptionGracePeriods API
  slug: ios-subscriptiongraceperiods-api
- description: The SubscriptionGroupLocalizations API from iOS — 2 operation(s) for subscriptiongrouplocalizations.
  name: iOS SubscriptionGroupLocalizations API
  slug: ios-subscriptiongrouplocalizations-api
- description: The SubscriptionGroups API from iOS — 6 operation(s) for subscriptiongroups.
  name: iOS SubscriptionGroups API
  slug: ios-subscriptiongroups-api
- description: The SubscriptionGroupSubmissions API from iOS — 1 operation(s) for subscriptiongroupsubmissions.
  name: iOS SubscriptionGroupSubmissions API
  slug: ios-subscriptiongroupsubmissions-api
- description: The SubscriptionImages API from iOS — 2 operation(s) for subscriptionimages.
  name: iOS SubscriptionImages API
  slug: ios-subscriptionimages-api
- description: The SubscriptionIntroductoryOffers API from iOS — 2 operation(s) for subscriptionintroductoryoffers.
  name: iOS SubscriptionIntroductoryOffers API
  slug: ios-subscriptionintroductoryoffers-api
- description: The SubscriptionLocalizations API from iOS — 2 operation(s) for subscriptionlocalizations.
  name: iOS SubscriptionLocalizations API
  slug: ios-subscriptionlocalizations-api
- description: The SubscriptionOfferCodeCustomCodes API from iOS — 2 operation(s) for subscriptionoffercodecustomcodes.
  name: iOS SubscriptionOfferCodeCustomCodes API
  slug: ios-subscriptionoffercodecustomcodes-api
- description: The SubscriptionOfferCodeOneTimeUseCodes API from iOS — 3 operation(s) for subscriptionoffercodeonetimeusecodes.
  name: iOS SubscriptionOfferCodeOneTimeUseCodes API
  slug: ios-subscriptionoffercodeonetimeusecodes-api
- description: The SubscriptionOfferCodes API from iOS — 8 operation(s) for subscriptionoffercodes.
  name: iOS SubscriptionOfferCodes API
  slug: ios-subscriptionoffercodes-api
- description: The SubscriptionPricePoints API from iOS — 3 operation(s) for subscriptionpricepoints.
  name: iOS SubscriptionPricePoints API
  slug: ios-subscriptionpricepoints-api
- description: The SubscriptionPrices API from iOS — 2 operation(s) for subscriptionprices.
  name: iOS SubscriptionPrices API
  slug: ios-subscriptionprices-api
- description: The SubscriptionPromotionalOffers API from iOS — 4 operation(s) for subscriptionpromotionaloffers.
  name: iOS SubscriptionPromotionalOffers API
  slug: ios-subscriptionpromotionaloffers-api
- description: The Subscriptions API from iOS — 24 operation(s) for subscriptions.
  name: iOS Subscriptions API
  slug: ios-subscriptions-api
- description: The SubscriptionSubmissions API from iOS — 1 operation(s) for subscriptionsubmissions.
  name: iOS SubscriptionSubmissions API
  slug: ios-subscriptionsubmissions-api
- description: The Territories API from iOS — 1 operation(s) for territories.
  name: iOS Territories API
  slug: ios-territories-api
- description: The TerritoryAvailabilities API from iOS — 1 operation(s) for territoryavailabilities.
  name: iOS TerritoryAvailabilities API
  slug: ios-territoryavailabilities-api
- description: The UserInvitations API from iOS — 4 operation(s) for userinvitations.
  name: iOS UserInvitations API
  slug: ios-userinvitations-api
- description: The Users API from iOS — 4 operation(s) for users.
  name: iOS Users API
  slug: ios-users-api
- description: The WebhookDeliveries API from iOS — 1 operation(s) for webhookdeliveries.
  name: iOS WebhookDeliveries API
  slug: ios-webhookdeliveries-api
- description: The WebhookPings API from iOS — 1 operation(s) for webhookpings.
  name: iOS WebhookPings API
  slug: ios-webhookpings-api
- description: The Webhooks API from iOS — 4 operation(s) for webhooks.
  name: iOS Webhooks API
  slug: ios-webhooks-api
- description: The WinBackOffers API from iOS — 4 operation(s) for winbackoffers.
  name: iOS WinBackOffers API
  slug: ios-winbackoffers-api
arazzos:
- description: Create a new App Store version, add its primary localization, and attach a build.
  name: iOS Create an App Store Version
  slug: ios-create-app-store-version-workflow
- description: Create a TestFlight beta group for an app, find a build by version, and make that build available to the group.
  name: iOS Create a TestFlight Beta Group and Assign a Build
  slug: ios-create-beta-group-assign-build-workflow
- description: Create an in-app purchase, add its localized display name, and submit it for review.
  name: iOS Create and Submit an In-App Purchase
  slug: ios-create-in-app-purchase-workflow
- description: Submit a certificate signing request, then read the issued certificate back for download.
  name: iOS Create a Signing Certificate
  slug: ios-create-signing-certificate-workflow
- description: Create a subscription group, add a subscription to it, and localize the subscription.
  name: iOS Create an Auto-Renewable Subscription
  slug: ios-create-subscription-workflow
- description: Create a bundle identifier and enable a capability such as Push Notifications or iCloud on it.
  name: iOS Enable a Capability on a Bundle ID
  slug: ios-enable-bundle-id-capability-workflow
- description: Create a beta tester, add them to a beta group, and send an App Store Connect invitation.
  name: iOS Invite a TestFlight Beta Tester
  slug: ios-invite-beta-tester-workflow
- description: Find a build, push a TestFlight notification to its testers, and confirm the build's beta state.
  name: iOS Notify TestFlight Testers of a New Build
  slug: ios-notify-testers-new-build-workflow
- description: Register a test device, create a bundle identifier, and generate a provisioning profile that ties them together.
  name: iOS Register a Provisioning Profile
  slug: ios-register-provisioning-profile-workflow
- description: Find the most recent low-rated review for an app and post a developer response to it.
  name: iOS Respond to a Customer Review
  slug: ios-respond-to-customer-review-workflow
- description: Find a build, add localized "What to Test" notes, and submit it for external beta review.
  name: iOS Submit a Build for TestFlight Beta Review
  slug: ios-submit-build-for-beta-review-workflow
- description: Open a review submission, add the App Store version as an item, and submit it to App Review.
  name: iOS Submit an App Store Version for Review
  slug: ios-submit-version-for-review-workflow
artifact_total: 606
asyncapis:
- description: App Store Server Notifications V2 is Apple's webhook surface for in-app purchase and subscription lifecycle events. Apple POSTs a JWS-signed payload to the production and sandbox URLs registered in Ap
  name: App Store Server Notifications V2
  slug: app-store-server-notifications-asyncapi
collections:
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations API
  slug: postman-ios-accessibilitydeclarations-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations Actors API
  slug: postman-ios-actors-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations AgeRatingDeclarations API
  slug: postman-ios-ageratingdeclarations-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations AlternativeDistributionDomains API
  slug: postman-ios-alternativedistributiondomains-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations AlternativeDistributionKeys API
  slug: postman-ios-alternativedistributionkeys-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations AlternativeDistributionPackageDeltas API
  slug: postman-ios-alternativedistributionpackagedeltas-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations AlternativeDistributionPackages API
  slug: postman-ios-alternativedistributionpackages-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations AlternativeDistributionPackageVariants API
  slug: postman-ios-alternativedistributionpackagevariants-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations AlternativeDistributionPackageVersions API
  slug: postman-ios-alternativedistributionpackageversions-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations AnalyticsReportInstances API
  slug: postman-ios-analyticsreportinstances-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations AnalyticsReportRequests API
  slug: postman-ios-analyticsreportrequests-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations AnalyticsReports API
  slug: postman-ios-analyticsreports-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations AnalyticsReportSegments API
  slug: postman-ios-analyticsreportsegments-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations AndroidToIosAppMappingDetails API
  slug: postman-ios-androidtoiosappmappingdetails-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations AppAvailabilities API
  slug: postman-ios-appavailabilities-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations AppCategories API
  slug: postman-ios-appcategories-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations AppClipAdvancedExperienceImages API
  slug: postman-ios-appclipadvancedexperienceimages-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations AppClipAdvancedExperiences API
  slug: postman-ios-appclipadvancedexperiences-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations AppClipAppStoreReviewDetails API
  slug: postman-ios-appclipappstorereviewdetails-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations AppClipDefaultExperienceLocalizations API
  slug: postman-ios-appclipdefaultexperiencelocalizations-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations AppClipDefaultExperiences API
  slug: postman-ios-appclipdefaultexperiences-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations AppClipHeaderImages API
  slug: postman-ios-appclipheaderimages-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations AppClips API
  slug: postman-ios-appclips-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations AppCustomProductPageLocalizations API
  slug: postman-ios-appcustomproductpagelocalizations-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations AppCustomProductPages API
  slug: postman-ios-appcustomproductpages-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations AppCustomProductPageVersions API
  slug: postman-ios-appcustomproductpageversions-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations AppEncryptionDeclarationDocuments API
  slug: postman-ios-appencryptiondeclarationdocuments-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations AppEncryptionDeclarations API
  slug: postman-ios-appencryptiondeclarations-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations AppEventLocalizations API
  slug: postman-ios-appeventlocalizations-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations AppEvents API
  slug: postman-ios-appevents-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations AppEventScreenshots API
  slug: postman-ios-appeventscreenshots-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations AppEventVideoClips API
  slug: postman-ios-appeventvideoclips-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations AppInfoLocalizations API
  slug: postman-ios-appinfolocalizations-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations AppInfos API
  slug: postman-ios-appinfos-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations AppPreviews API
  slug: postman-ios-apppreviews-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations AppPreviewSets API
  slug: postman-ios-apppreviewsets-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations AppPricePoints API
  slug: postman-ios-apppricepoints-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations AppPriceSchedules API
  slug: postman-ios-apppriceschedules-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations Apps API
  slug: postman-ios-apps-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations AppScreenshots API
  slug: postman-ios-appscreenshots-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations AppScreenshotSets API
  slug: postman-ios-appscreenshotsets-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations AppStoreReviewAttachments API
  slug: postman-ios-appstorereviewattachments-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations AppStoreReviewDetails API
  slug: postman-ios-appstorereviewdetails-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations AppStoreVersionExperiments API
  slug: postman-ios-appstoreversionexperiments-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations AppStoreVersionExperimentTreatmentLocalizations API
  slug: postman-ios-appstoreversionexperimenttreatmentlocalizations-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations AppStoreVersionExperimentTreatments API
  slug: postman-ios-appstoreversionexperimenttreatments-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations AppStoreVersionLocalizations API
  slug: postman-ios-appstoreversionlocalizations-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations AppStoreVersionPhasedReleases API
  slug: postman-ios-appstoreversionphasedreleases-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations AppStoreVersionPromotions API
  slug: postman-ios-appstoreversionpromotions-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations AppStoreVersionReleaseRequests API
  slug: postman-ios-appstoreversionreleaserequests-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations AppStoreVersions API
  slug: postman-ios-appstoreversions-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations AppStoreVersionSubmissions API
  slug: postman-ios-appstoreversionsubmissions-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations AppTags API
  slug: postman-ios-apptags-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations BackgroundAssets API
  slug: postman-ios-backgroundassets-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations BackgroundAssetUploadFiles API
  slug: postman-ios-backgroundassetuploadfiles-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations BackgroundAssetVersionAppStoreReleases API
  slug: postman-ios-backgroundassetversionappstorereleases-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations BackgroundAssetVersionExternalBetaReleases API
  slug: postman-ios-backgroundassetversionexternalbetareleases-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations BackgroundAssetVersionInternalBetaReleases API
  slug: postman-ios-backgroundassetversioninternalbetareleases-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations BackgroundAssetVersions API
  slug: postman-ios-backgroundassetversions-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations BetaAppClipInvocationLocalizations API
  slug: postman-ios-betaappclipinvocationlocalizations-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations BetaAppClipInvocations API
  slug: postman-ios-betaappclipinvocations-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations BetaAppLocalizations API
  slug: postman-ios-betaapplocalizations-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations BetaAppReviewDetails API
  slug: postman-ios-betaappreviewdetails-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations BetaAppReviewSubmissions API
  slug: postman-ios-betaappreviewsubmissions-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations BetaBuildLocalizations API
  slug: postman-ios-betabuildlocalizations-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations BetaCrashLogs API
  slug: postman-ios-betacrashlogs-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations BetaFeedbackCrashSubmissions API
  slug: postman-ios-betafeedbackcrashsubmissions-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations BetaFeedbackScreenshotSubmissions API
  slug: postman-ios-betafeedbackscreenshotsubmissions-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations BetaGroups API
  slug: postman-ios-betagroups-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations BetaLicenseAgreements API
  slug: postman-ios-betalicenseagreements-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations BetaRecruitmentCriteria API
  slug: postman-ios-betarecruitmentcriteria-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations BetaRecruitmentCriterionOptions API
  slug: postman-ios-betarecruitmentcriterionoptions-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations BetaTesterInvitations API
  slug: postman-ios-betatesterinvitations-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations BetaTesters API
  slug: postman-ios-betatesters-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations BuildBetaDetails API
  slug: postman-ios-buildbetadetails-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations BuildBetaNotifications API
  slug: postman-ios-buildbetanotifications-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations BuildBundles API
  slug: postman-ios-buildbundles-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations Builds API
  slug: postman-ios-builds-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations BuildUploadFiles API
  slug: postman-ios-builduploadfiles-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations BuildUploads API
  slug: postman-ios-builduploads-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations BundleIdCapabilities API
  slug: postman-ios-bundleidcapabilities-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations BundleIds API
  slug: postman-ios-bundleids-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations Certificates API
  slug: postman-ios-certificates-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations CiArtifacts API
  slug: postman-ios-ciartifacts-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations CiBuildActions API
  slug: postman-ios-cibuildactions-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations CiBuildRuns API
  slug: postman-ios-cibuildruns-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations CiIssues API
  slug: postman-ios-ciissues-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations CiMacOsVersions API
  slug: postman-ios-cimacosversions-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations CiProducts API
  slug: postman-ios-ciproducts-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations CiTestResults API
  slug: postman-ios-citestresults-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations CiWorkflows API
  slug: postman-ios-ciworkflows-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations CiXcodeVersions API
  slug: postman-ios-cixcodeversions-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations CustomerReviewResponses API
  slug: postman-ios-customerreviewresponses-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations CustomerReviews API
  slug: postman-ios-customerreviews-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations Devices API
  slug: postman-ios-devices-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations DiagnosticSignatures API
  slug: postman-ios-diagnosticsignatures-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations EndAppAvailabilityPreOrders API
  slug: postman-ios-endappavailabilitypreorders-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations EndUserLicenseAgreements API
  slug: postman-ios-enduserlicenseagreements-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations FinanceReports API
  slug: postman-ios-financereports-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations GameCenterAchievementImages API
  slug: postman-ios-gamecenterachievementimages-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations GameCenterAchievementLocalizations API
  slug: postman-ios-gamecenterachievementlocalizations-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations GameCenterAchievementReleases API
  slug: postman-ios-gamecenterachievementreleases-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations GameCenterAchievements API
  slug: postman-ios-gamecenterachievements-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations GameCenterAchievementVersions API
  slug: postman-ios-gamecenterachievementversions-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations GameCenterActivities API
  slug: postman-ios-gamecenteractivities-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations GameCenterActivityImages API
  slug: postman-ios-gamecenteractivityimages-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations GameCenterActivityLocalizations API
  slug: postman-ios-gamecenteractivitylocalizations-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations GameCenterActivityVersionReleases API
  slug: postman-ios-gamecenteractivityversionreleases-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations GameCenterActivityVersions API
  slug: postman-ios-gamecenteractivityversions-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations GameCenterAppVersions API
  slug: postman-ios-gamecenterappversions-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations GameCenterChallengeImages API
  slug: postman-ios-gamecenterchallengeimages-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations GameCenterChallengeLocalizations API
  slug: postman-ios-gamecenterchallengelocalizations-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations GameCenterChallenges API
  slug: postman-ios-gamecenterchallenges-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations GameCenterChallengeVersionReleases API
  slug: postman-ios-gamecenterchallengeversionreleases-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations GameCenterChallengeVersions API
  slug: postman-ios-gamecenterchallengeversions-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations GameCenterDetails API
  slug: postman-ios-gamecenterdetails-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations GameCenterEnabledVersions API
  slug: postman-ios-gamecenterenabledversions-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations GameCenterGroups API
  slug: postman-ios-gamecentergroups-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations GameCenterLeaderboardEntrySubmissions API
  slug: postman-ios-gamecenterleaderboardentrysubmissions-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations GameCenterLeaderboardImages API
  slug: postman-ios-gamecenterleaderboardimages-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations GameCenterLeaderboardLocalizations API
  slug: postman-ios-gamecenterleaderboardlocalizations-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations GameCenterLeaderboardReleases API
  slug: postman-ios-gamecenterleaderboardreleases-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations GameCenterLeaderboards API
  slug: postman-ios-gamecenterleaderboards-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations GameCenterLeaderboardSetImages API
  slug: postman-ios-gamecenterleaderboardsetimages-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations GameCenterLeaderboardSetLocalizations API
  slug: postman-ios-gamecenterleaderboardsetlocalizations-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations GameCenterLeaderboardSetMemberLocalizations API
  slug: postman-ios-gamecenterleaderboardsetmemberlocalizations-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations GameCenterLeaderboardSetReleases API
  slug: postman-ios-gamecenterleaderboardsetreleases-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations GameCenterLeaderboardSets API
  slug: postman-ios-gamecenterleaderboardsets-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations GameCenterLeaderboardSetVersions API
  slug: postman-ios-gamecenterleaderboardsetversions-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations GameCenterLeaderboardVersions API
  slug: postman-ios-gamecenterleaderboardversions-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations GameCenterMatchmakingQueues API
  slug: postman-ios-gamecentermatchmakingqueues-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations GameCenterMatchmakingRules API
  slug: postman-ios-gamecentermatchmakingrules-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations GameCenterMatchmakingRuleSets API
  slug: postman-ios-gamecentermatchmakingrulesets-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations GameCenterMatchmakingRuleSetTests API
  slug: postman-ios-gamecentermatchmakingrulesettests-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations GameCenterMatchmakingTeams API
  slug: postman-ios-gamecentermatchmakingteams-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations GameCenterPlayerAchievementSubmissions API
  slug: postman-ios-gamecenterplayerachievementsubmissions-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations InAppPurchaseAppStoreReviewScreenshots API
  slug: postman-ios-inapppurchaseappstorereviewscreenshots-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations InAppPurchaseAvailabilities API
  slug: postman-ios-inapppurchaseavailabilities-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations InAppPurchaseContents API
  slug: postman-ios-inapppurchasecontents-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations InAppPurchaseImages API
  slug: postman-ios-inapppurchaseimages-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations InAppPurchaseLocalizations API
  slug: postman-ios-inapppurchaselocalizations-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations InAppPurchaseOfferCodeCustomCodes API
  slug: postman-ios-inapppurchaseoffercodecustomcodes-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations InAppPurchaseOfferCodeOneTimeUseCodes API
  slug: postman-ios-inapppurchaseoffercodeonetimeusecodes-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations InAppPurchaseOfferCodes API
  slug: postman-ios-inapppurchaseoffercodes-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations InAppPurchasePricePoints API
  slug: postman-ios-inapppurchasepricepoints-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations InAppPurchasePriceSchedules API
  slug: postman-ios-inapppurchasepriceschedules-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations InAppPurchases API
  slug: postman-ios-inapppurchases-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations InAppPurchaseSubmissions API
  slug: postman-ios-inapppurchasesubmissions-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations MarketplaceSearchDetails API
  slug: postman-ios-marketplacesearchdetails-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations MarketplaceWebhooks API
  slug: postman-ios-marketplacewebhooks-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations MerchantIds API
  slug: postman-ios-merchantids-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations Metrics API
  slug: postman-ios-metrics-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations Nominations API
  slug: postman-ios-nominations-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations PassTypeIds API
  slug: postman-ios-passtypeids-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations PreReleaseVersions API
  slug: postman-ios-prereleaseversions-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations Profiles API
  slug: postman-ios-profiles-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations PromotedPurchases API
  slug: postman-ios-promotedpurchases-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations ReviewSubmissionItems API
  slug: postman-ios-reviewsubmissionitems-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations ReviewSubmissions API
  slug: postman-ios-reviewsubmissions-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations RoutingAppCoverages API
  slug: postman-ios-routingappcoverages-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations SalesReports API
  slug: postman-ios-salesreports-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations SandboxTesters API
  slug: postman-ios-sandboxtesters-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations SandboxTestersClearPurchaseHistoryRequest API
  slug: postman-ios-sandboxtestersclearpurchasehistoryrequest-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations ScmGitReferences API
  slug: postman-ios-scmgitreferences-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations ScmProviders API
  slug: postman-ios-scmproviders-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations ScmPullRequests API
  slug: postman-ios-scmpullrequests-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations ScmRepositories API
  slug: postman-ios-scmrepositories-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations SubscriptionAppStoreReviewScreenshots API
  slug: postman-ios-subscriptionappstorereviewscreenshots-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations SubscriptionAvailabilities API
  slug: postman-ios-subscriptionavailabilities-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations SubscriptionGracePeriods API
  slug: postman-ios-subscriptiongraceperiods-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations SubscriptionGroupLocalizations API
  slug: postman-ios-subscriptiongrouplocalizations-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations SubscriptionGroups API
  slug: postman-ios-subscriptiongroups-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations SubscriptionGroupSubmissions API
  slug: postman-ios-subscriptiongroupsubmissions-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations SubscriptionImages API
  slug: postman-ios-subscriptionimages-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations SubscriptionIntroductoryOffers API
  slug: postman-ios-subscriptionintroductoryoffers-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations SubscriptionLocalizations API
  slug: postman-ios-subscriptionlocalizations-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations SubscriptionOfferCodeCustomCodes API
  slug: postman-ios-subscriptionoffercodecustomcodes-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations SubscriptionOfferCodeOneTimeUseCodes API
  slug: postman-ios-subscriptionoffercodeonetimeusecodes-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations SubscriptionOfferCodes API
  slug: postman-ios-subscriptionoffercodes-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations SubscriptionPricePoints API
  slug: postman-ios-subscriptionpricepoints-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations SubscriptionPrices API
  slug: postman-ios-subscriptionprices-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations SubscriptionPromotionalOffers API
  slug: postman-ios-subscriptionpromotionaloffers-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations Subscriptions API
  slug: postman-ios-subscriptions-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations SubscriptionSubmissions API
  slug: postman-ios-subscriptionsubmissions-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations Territories API
  slug: postman-ios-territories-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations TerritoryAvailabilities API
  slug: postman-ios-territoryavailabilities-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations UserInvitations API
  slug: postman-ios-userinvitations-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations Users API
  slug: postman-ios-users-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations WebhookDeliveries API
  slug: postman-ios-webhookdeliveries-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations WebhookPings API
  slug: postman-ios-webhookpings-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations Webhooks API
  slug: postman-ios-webhooks-api
- collection_type: postman
  name: App Store Connect AccessibilityDeclarations WinBackOffers API
  slug: postman-ios-winbackoffers-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: App Store Connect API
  slug: open-app-store-connect
- collection_type: open
  name: App Store Connect AccessibilityDeclarations API
  slug: open-ios-accessibilitydeclarations-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations Actors API
  slug: open-ios-actors-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations AgeRatingDeclarations API
  slug: open-ios-ageratingdeclarations-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations AlternativeDistributionDomains API
  slug: open-ios-alternativedistributiondomains-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations AlternativeDistributionKeys API
  slug: open-ios-alternativedistributionkeys-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations AlternativeDistributionPackageDeltas API
  slug: open-ios-alternativedistributionpackagedeltas-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations AlternativeDistributionPackages API
  slug: open-ios-alternativedistributionpackages-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations AlternativeDistributionPackageVariants API
  slug: open-ios-alternativedistributionpackagevariants-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations AlternativeDistributionPackageVersions API
  slug: open-ios-alternativedistributionpackageversions-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations AnalyticsReportInstances API
  slug: open-ios-analyticsreportinstances-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations AnalyticsReportRequests API
  slug: open-ios-analyticsreportrequests-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations AnalyticsReports API
  slug: open-ios-analyticsreports-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations AnalyticsReportSegments API
  slug: open-ios-analyticsreportsegments-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations AndroidToIosAppMappingDetails API
  slug: open-ios-androidtoiosappmappingdetails-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations AppAvailabilities API
  slug: open-ios-appavailabilities-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations AppCategories API
  slug: open-ios-appcategories-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations AppClipAdvancedExperienceImages API
  slug: open-ios-appclipadvancedexperienceimages-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations AppClipAdvancedExperiences API
  slug: open-ios-appclipadvancedexperiences-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations AppClipDefaultExperienceLocalizations API
  slug: open-ios-appclipdefaultexperiencelocalizations-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations AppClipDefaultExperiences API
  slug: open-ios-appclipdefaultexperiences-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations AppClipHeaderImages API
  slug: open-ios-appclipheaderimages-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations AppClips API
  slug: open-ios-appclips-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations AppCustomProductPageLocalizations API
  slug: open-ios-appcustomproductpagelocalizations-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations AppCustomProductPages API
  slug: open-ios-appcustomproductpages-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations AppCustomProductPageVersions API
  slug: open-ios-appcustomproductpageversions-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations AppEncryptionDeclarationDocuments API
  slug: open-ios-appencryptiondeclarationdocuments-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations AppEncryptionDeclarations API
  slug: open-ios-appencryptiondeclarations-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations AppEventLocalizations API
  slug: open-ios-appeventlocalizations-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations AppEvents API
  slug: open-ios-appevents-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations AppEventScreenshots API
  slug: open-ios-appeventscreenshots-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations AppEventVideoClips API
  slug: open-ios-appeventvideoclips-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations AppInfoLocalizations API
  slug: open-ios-appinfolocalizations-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations AppInfos API
  slug: open-ios-appinfos-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations AppPricePoints API
  slug: open-ios-apppricepoints-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations AppPriceSchedules API
  slug: open-ios-apppriceschedules-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations Apps API
  slug: open-ios-apps-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations AppScreenshots API
  slug: open-ios-appscreenshots-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations AppScreenshotSets API
  slug: open-ios-appscreenshotsets-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations AppStoreVersionExperiments API
  slug: open-ios-appstoreversionexperiments-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations AppStoreVersionExperimentTreatmentLocalizations API
  slug: open-ios-appstoreversionexperimenttreatmentlocalizations-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations AppStoreVersionExperimentTreatments API
  slug: open-ios-appstoreversionexperimenttreatments-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations AppStoreVersionLocalizations API
  slug: open-ios-appstoreversionlocalizations-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations AppStoreVersionPhasedReleases API
  slug: open-ios-appstoreversionphasedreleases-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations AppStoreVersionPromotions API
  slug: open-ios-appstoreversionpromotions-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations AppStoreVersionReleaseRequests API
  slug: open-ios-appstoreversionreleaserequests-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations AppStoreVersions API
  slug: open-ios-appstoreversions-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations AppStoreVersionSubmissions API
  slug: open-ios-appstoreversionsubmissions-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations AppTags API
  slug: open-ios-apptags-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations BackgroundAssets API
  slug: open-ios-backgroundassets-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations BackgroundAssetUploadFiles API
  slug: open-ios-backgroundassetuploadfiles-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations BackgroundAssetVersionAppStoreReleases API
  slug: open-ios-backgroundassetversionappstorereleases-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations BackgroundAssetVersionExternalBetaReleases API
  slug: open-ios-backgroundassetversionexternalbetareleases-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations BackgroundAssetVersionInternalBetaReleases API
  slug: open-ios-backgroundassetversioninternalbetareleases-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations BackgroundAssetVersions API
  slug: open-ios-backgroundassetversions-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations BetaAppClipInvocationLocalizations API
  slug: open-ios-betaappclipinvocationlocalizations-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations BetaAppClipInvocations API
  slug: open-ios-betaappclipinvocations-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations BetaAppLocalizations API
  slug: open-ios-betaapplocalizations-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations BetaBuildLocalizations API
  slug: open-ios-betabuildlocalizations-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations BetaCrashLogs API
  slug: open-ios-betacrashlogs-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations BetaFeedbackCrashSubmissions API
  slug: open-ios-betafeedbackcrashsubmissions-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations BetaFeedbackScreenshotSubmissions API
  slug: open-ios-betafeedbackscreenshotsubmissions-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations BetaGroups API
  slug: open-ios-betagroups-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations BetaLicenseAgreements API
  slug: open-ios-betalicenseagreements-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations BetaRecruitmentCriteria API
  slug: open-ios-betarecruitmentcriteria-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations BetaRecruitmentCriterionOptions API
  slug: open-ios-betarecruitmentcriterionoptions-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations BetaTesterInvitations API
  slug: open-ios-betatesterinvitations-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations BetaTesters API
  slug: open-ios-betatesters-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations BuildBetaDetails API
  slug: open-ios-buildbetadetails-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations BuildBetaNotifications API
  slug: open-ios-buildbetanotifications-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations BuildBundles API
  slug: open-ios-buildbundles-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations Builds API
  slug: open-ios-builds-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations BuildUploadFiles API
  slug: open-ios-builduploadfiles-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations BuildUploads API
  slug: open-ios-builduploads-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations BundleIdCapabilities API
  slug: open-ios-bundleidcapabilities-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations BundleIds API
  slug: open-ios-bundleids-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations Certificates API
  slug: open-ios-certificates-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations CiArtifacts API
  slug: open-ios-ciartifacts-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations CiBuildActions API
  slug: open-ios-cibuildactions-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations CiBuildRuns API
  slug: open-ios-cibuildruns-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations CiIssues API
  slug: open-ios-ciissues-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations CiMacOsVersions API
  slug: open-ios-cimacosversions-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations CiProducts API
  slug: open-ios-ciproducts-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations CiTestResults API
  slug: open-ios-citestresults-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations CiWorkflows API
  slug: open-ios-ciworkflows-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations CiXcodeVersions API
  slug: open-ios-cixcodeversions-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations Devices API
  slug: open-ios-devices-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations DiagnosticSignatures API
  slug: open-ios-diagnosticsignatures-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations EndAppAvailabilityPreOrders API
  slug: open-ios-endappavailabilitypreorders-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations EndUserLicenseAgreements API
  slug: open-ios-enduserlicenseagreements-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations FinanceReports API
  slug: open-ios-financereports-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations GameCenterAchievementImages API
  slug: open-ios-gamecenterachievementimages-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations GameCenterAchievementLocalizations API
  slug: open-ios-gamecenterachievementlocalizations-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations GameCenterAchievementReleases API
  slug: open-ios-gamecenterachievementreleases-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations GameCenterAchievements API
  slug: open-ios-gamecenterachievements-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations GameCenterAchievementVersions API
  slug: open-ios-gamecenterachievementversions-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations GameCenterActivities API
  slug: open-ios-gamecenteractivities-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations GameCenterActivityImages API
  slug: open-ios-gamecenteractivityimages-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations GameCenterActivityLocalizations API
  slug: open-ios-gamecenteractivitylocalizations-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations GameCenterActivityVersionReleases API
  slug: open-ios-gamecenteractivityversionreleases-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations GameCenterActivityVersions API
  slug: open-ios-gamecenteractivityversions-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations GameCenterAppVersions API
  slug: open-ios-gamecenterappversions-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations GameCenterChallengeImages API
  slug: open-ios-gamecenterchallengeimages-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations GameCenterChallengeLocalizations API
  slug: open-ios-gamecenterchallengelocalizations-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations GameCenterChallenges API
  slug: open-ios-gamecenterchallenges-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations GameCenterChallengeVersionReleases API
  slug: open-ios-gamecenterchallengeversionreleases-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations GameCenterChallengeVersions API
  slug: open-ios-gamecenterchallengeversions-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations GameCenterDetails API
  slug: open-ios-gamecenterdetails-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations GameCenterEnabledVersions API
  slug: open-ios-gamecenterenabledversions-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations GameCenterGroups API
  slug: open-ios-gamecentergroups-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations GameCenterLeaderboardEntrySubmissions API
  slug: open-ios-gamecenterleaderboardentrysubmissions-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations GameCenterLeaderboardImages API
  slug: open-ios-gamecenterleaderboardimages-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations GameCenterLeaderboardLocalizations API
  slug: open-ios-gamecenterleaderboardlocalizations-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations GameCenterLeaderboardReleases API
  slug: open-ios-gamecenterleaderboardreleases-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations GameCenterLeaderboards API
  slug: open-ios-gamecenterleaderboards-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations GameCenterLeaderboardSetImages API
  slug: open-ios-gamecenterleaderboardsetimages-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations GameCenterLeaderboardSetLocalizations API
  slug: open-ios-gamecenterleaderboardsetlocalizations-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations GameCenterLeaderboardSetMemberLocalizations API
  slug: open-ios-gamecenterleaderboardsetmemberlocalizations-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations GameCenterLeaderboardSetReleases API
  slug: open-ios-gamecenterleaderboardsetreleases-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations GameCenterLeaderboardSets API
  slug: open-ios-gamecenterleaderboardsets-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations GameCenterLeaderboardSetVersions API
  slug: open-ios-gamecenterleaderboardsetversions-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations GameCenterLeaderboardVersions API
  slug: open-ios-gamecenterleaderboardversions-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations GameCenterMatchmakingQueues API
  slug: open-ios-gamecentermatchmakingqueues-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations GameCenterMatchmakingRules API
  slug: open-ios-gamecentermatchmakingrules-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations GameCenterMatchmakingRuleSets API
  slug: open-ios-gamecentermatchmakingrulesets-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations GameCenterMatchmakingRuleSetTests API
  slug: open-ios-gamecentermatchmakingrulesettests-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations GameCenterMatchmakingTeams API
  slug: open-ios-gamecentermatchmakingteams-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations GameCenterPlayerAchievementSubmissions API
  slug: open-ios-gamecenterplayerachievementsubmissions-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations InAppPurchaseAvailabilities API
  slug: open-ios-inapppurchaseavailabilities-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations InAppPurchaseContents API
  slug: open-ios-inapppurchasecontents-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations InAppPurchaseImages API
  slug: open-ios-inapppurchaseimages-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations InAppPurchaseLocalizations API
  slug: open-ios-inapppurchaselocalizations-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations InAppPurchaseOfferCodeCustomCodes API
  slug: open-ios-inapppurchaseoffercodecustomcodes-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations InAppPurchaseOfferCodeOneTimeUseCodes API
  slug: open-ios-inapppurchaseoffercodeonetimeusecodes-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations InAppPurchaseOfferCodes API
  slug: open-ios-inapppurchaseoffercodes-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations InAppPurchasePricePoints API
  slug: open-ios-inapppurchasepricepoints-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations InAppPurchasePriceSchedules API
  slug: open-ios-inapppurchasepriceschedules-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations InAppPurchases API
  slug: open-ios-inapppurchases-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations InAppPurchaseSubmissions API
  slug: open-ios-inapppurchasesubmissions-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations MarketplaceSearchDetails API
  slug: open-ios-marketplacesearchdetails-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations MarketplaceWebhooks API
  slug: open-ios-marketplacewebhooks-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations MerchantIds API
  slug: open-ios-merchantids-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations Metrics API
  slug: open-ios-metrics-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations Nominations API
  slug: open-ios-nominations-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations PassTypeIds API
  slug: open-ios-passtypeids-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations PreReleaseVersions API
  slug: open-ios-prereleaseversions-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations Profiles API
  slug: open-ios-profiles-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations PromotedPurchases API
  slug: open-ios-promotedpurchases-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations RoutingAppCoverages API
  slug: open-ios-routingappcoverages-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations SalesReports API
  slug: open-ios-salesreports-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations SandboxTesters API
  slug: open-ios-sandboxtesters-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations SandboxTestersClearPurchaseHistoryRequest API
  slug: open-ios-sandboxtestersclearpurchasehistoryrequest-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations ScmGitReferences API
  slug: open-ios-scmgitreferences-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations ScmProviders API
  slug: open-ios-scmproviders-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations ScmPullRequests API
  slug: open-ios-scmpullrequests-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations ScmRepositories API
  slug: open-ios-scmrepositories-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations SubscriptionAvailabilities API
  slug: open-ios-subscriptionavailabilities-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations SubscriptionGracePeriods API
  slug: open-ios-subscriptiongraceperiods-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations SubscriptionGroupLocalizations API
  slug: open-ios-subscriptiongrouplocalizations-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations SubscriptionGroups API
  slug: open-ios-subscriptiongroups-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations SubscriptionGroupSubmissions API
  slug: open-ios-subscriptiongroupsubmissions-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations SubscriptionImages API
  slug: open-ios-subscriptionimages-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations SubscriptionIntroductoryOffers API
  slug: open-ios-subscriptionintroductoryoffers-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations SubscriptionLocalizations API
  slug: open-ios-subscriptionlocalizations-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations SubscriptionOfferCodeCustomCodes API
  slug: open-ios-subscriptionoffercodecustomcodes-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations SubscriptionOfferCodeOneTimeUseCodes API
  slug: open-ios-subscriptionoffercodeonetimeusecodes-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations SubscriptionOfferCodes API
  slug: open-ios-subscriptionoffercodes-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations SubscriptionPricePoints API
  slug: open-ios-subscriptionpricepoints-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations SubscriptionPrices API
  slug: open-ios-subscriptionprices-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations SubscriptionPromotionalOffers API
  slug: open-ios-subscriptionpromotionaloffers-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations Subscriptions API
  slug: open-ios-subscriptions-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations SubscriptionSubmissions API
  slug: open-ios-subscriptionsubmissions-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations Territories API
  slug: open-ios-territories-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations TerritoryAvailabilities API
  slug: open-ios-territoryavailabilities-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations UserInvitations API
  slug: open-ios-userinvitations-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations Users API
  slug: open-ios-users-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations WebhookDeliveries API
  slug: open-ios-webhookdeliveries-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations WebhookPings API
  slug: open-ios-webhookpings-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations Webhooks API
  slug: open-ios-webhooks-api
- collection_type: open
  name: App Store Connect AccessibilityDeclarations WinBackOffers API
  slug: open-ios-winbackoffers-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/ios/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ios-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ios-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ios-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ios-authentication.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ios-create-app-store-version-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ios-create-beta-group-assign-build-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ios-create-in-app-purchase-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ios-create-signing-certificate-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ios-create-subscription-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ios-enable-bundle-id-capability-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ios-invite-beta-tester-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ios-notify-testers-new-build-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ios-register-provisioning-profile-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ios-respond-to-customer-review-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ios-submit-build-for-beta-review-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ios-submit-version-for-review-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.apple.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.apple.com/ios/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.apple.com/documentation/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.apple.com/documentation/appstoreconnectapi
- group: start
  title: ''
  type: Signup
  url: https://developer.apple.com/programs/enroll/
- group: commercial
  title: ''
  type: Pricing
  url: https://developer.apple.com/programs/whats-included/
- group: commercial
  title: ''
  type: Plans
  url: https://developer.apple.com/programs/
- group: operate
  title: ''
  type: StatusPage
  url: https://developer.apple.com/system-status/
- group: company
  title: ''
  type: Blog
  url: https://developer.apple.com/news/
- group: other
  title: ''
  type: RSS
  url: https://developer.apple.com/news/rss/news.rss
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://developer.apple.com/news/releases/
- group: operate
  title: ''
  type: Forums
  url: https://developer.apple.com/forums/
- group: operate
  title: ''
  type: Support
  url: https://developer.apple.com/support/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apple
- group: other
  title: ''
  type: Events
  url: https://developer.apple.com/wwdc/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/appledevelopers
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.apple.com/support/terms/
- group: commercial
  title: ''
  type: Privacy
  url: https://developer.apple.com/support/privacy/
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/ios/main/openapi/app-store-connect-openapi.json
- group: docs
  title: ''
  type: AsyncAPI
  url: https://raw.githubusercontent.com/api-evangelist/ios/main/asyncapi/app-store-server-notifications-asyncapi.yml
- group: design
  title: ''
  type: Spectral
  url: https://raw.githubusercontent.com/api-evangelist/ios/main/rules/app-store-connect-rules.yml
- group: docs
  title: ''
  type: JSONSchema
  url: https://github.com/api-evangelist/ios/tree/main/json-schema
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/ios/main/json-ld/ios-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/ios/main/vocabulary/ios-vocabulary.yml
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/ios/main/plans/ios-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/ios/main/rate-limits/ios-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/ios/main/finops/ios-finops.yml
created: '2026-05-11'
description: iOS is Apple's mobile operating system and the developer platform behind iPhone apps. While the bulk of the iOS SDK is delivered as Swift / Objective-C client frameworks (UIKit, SwiftUI, MapKit, HealthKit, HomeKit, SiriKit, StoreKit, AppIntents, PassKit, WidgetKit, ActivityKit), Apple also exposes a substantial set of server-side HTTPS APIs that iOS developers, publishers, and back-end systems consume directly. This repository indexes that server-side surface — App Store Connect API, App Store Server API, App Store Server Notifications, Apple Push Notification service (APNs), DeviceCheck / App Attest, Sign in with Apple, Apple Music API, the Wallet / PassKit Web Service contract, and related developer infrastructure — and points to the matching OpenAPI artifacts where Apple publishes them.
examples:
- key_count: 2
  name: Apns Send Notification Example
  slug: apns-send-notification-example
- key_count: 2
  name: App Store Connect List Apps Example
  slug: app-store-connect-list-apps-example
- key_count: 4
  name: App Store Server Notification Subscribed Example
  slug: app-store-server-notification-subscribed-example
- key_count: 3
  name: Sign In With Apple Token Example
  slug: sign-in-with-apple-token-example
finops:
- name: Ios Finops
  service_category: ''
  slug: ios-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ios.png
json_schemas:
- name: APNs Notification Payload
  property_count: 1
  slug: apns-notification-payload
- name: App
  property_count: 5
  slug: app-store-connect-app
- name: Build
  property_count: 3
  slug: app-store-connect-build
- name: JWSTransactionDecodedPayload
  property_count: 22
  slug: app-store-server-transaction
- name: Sign in with Apple ID Token Claims
  property_count: 12
  slug: sign-in-with-apple-id-token
json_structures:
- name: Ios Server Apis Structure
  property_count: 3
  slug: ios-server-apis-structure
jsonld:
- class_count: 21
  name: Ios Context
  property_count: 6
  slug: ios-context
layout: provider
modified: '2026-05-23'
name: iOS
nav: Providers
network: true
overview: 'iOS publishes 193 APIs on the [APIs.io](https://apis.io/) network, including App Store Server Notifications, AccessibilityDeclarations API, Actors API, and 190 more. Tagged areas include iOS, Apple, Mobile, App Store, and Push Notifications.


  The iOS catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  iOS''s developer surface includes authentication, developer portal, documentation, API reference, signup flow, pricing, engineering blog, and 37 more developer resources.'
plans:
- name: Ios Plans Pricing
  plan_count: 5
  slug: ios-plans-pricing
random_paper: 33
rate_limits:
- limit_count: 7
  name: Ios Rate Limits
  slug: ios-rate-limits
rules:
- effective_rule_count: 48
  extends:
  - spectral:oas
  name: iOS API Rules
  rule_count: 7
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 3
  slug: app-store-connect-rules
- effective_rule_count: 28
  extends:
  - spectral:asyncapi
  name: iOS API Rules
  rule_count: 1
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 1
  slug: ios-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: iOS API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: ios-jsonschema-spectral-rules
score:
  band: exemplar
  composite: 69.2
  delta: 9.4
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 69.7
    contract_quality: 67.3
    developer_ergonomics: 50.0
    discoverability: 59.3
    governance: 69.7
    operational_transparency: 68.4
  previous_composite: 59.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 192
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 48.4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/ios/refs/heads/main/screenshots/ios-2026-06-20T183533.png
security:
- kind: authentication
  name: Ios Authentication
  slug: ios-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Ios Domain Security
  slug: ios-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ios Vulnerability Disclosure
  slug: ios-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ios
tags:
- iOS
- Apple
- Mobile
- App Store
- Push Notifications
- In-App Purchases
- Subscriptions
- Authentication
- Wallet
- Developer Platform
website: https://developer.apple.com/ios/
---
