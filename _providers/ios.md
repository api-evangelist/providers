---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 445
  human_in_the_loop: 0
  name: Ios Agentic Access
  operation_count: 1208
  slug: ios-agentic-access
  summary_line: 1208 operations · 445 acting
api_count: 1
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
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The AccessibilityDeclarations API from iOS — 2 operation(s) for accessibilitydeclarations.
  name: iOS AccessibilityDeclarations API
  phrasing_intents:
  - id: accessibilityDeclarations_createInstance
    intent: Create an accessibility declaration
    question: How do I declare which accessibility features my app supports on a device type?
  - id: accessibilityDeclarations_getInstance
    intent: Get an accessibility declaration
    question: Which accessibility features did I declare for my app on a device family?
  - id: accessibilityDeclarations_updateInstance
    intent: Update an accessibility declaration
    question: How do I add captions support to an existing accessibility declaration?
  - id: accessibilityDeclarations_deleteInstance
    intent: Delete an accessibility declaration
    question: Can I remove an accessibility declaration from my app?
  phrasing_ops: 4
  slug: ios-accessibilitydeclarations-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The Actors API from iOS — 2 operation(s) for actors.
  name: iOS Actors API
  phrasing_intents:
  - id: actors_getCollection
    intent: Look up the actors behind App Store Connect changes
    question: Who made a change in App Store Connect, given the actor IDs?
  - id: actors_getInstance
    intent: Get one App Store Connect actor
    question: Was a particular change made by a person, an API key or Apple?
  phrasing_ops: 2
  slug: ios-actors-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The AgeRatingDeclarations API from iOS — 1 operation(s) for ageratingdeclarations.
  name: iOS AgeRatingDeclarations API
  phrasing_intents:
  - id: ageRatingDeclarations_updateInstance
    intent: Update an app's age rating declaration
    question: Can I revise my app's age rating questionnaire answers?
  phrasing_ops: 1
  slug: ios-ageratingdeclarations-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The AlternativeDistributionDomains API from iOS — 2 operation(s) for alternativedistributiondomains.
  name: iOS AlternativeDistributionDomains API
  phrasing_intents:
  - id: alternativeDistributionDomains_getCollection
    intent: List alternative distribution domains
    question: Which domains have I registered for alternative app distribution?
  - id: alternativeDistributionDomains_createInstance
    intent: Add an alternative distribution domain
    question: How do I register a domain for distributing apps outside the App Store?
  - id: alternativeDistributionDomains_getInstance
    intent: Get an alternative distribution domain
    question: What details are stored for one alternative distribution domain?
  - id: alternativeDistributionDomains_deleteInstance
    intent: Remove an alternative distribution domain
    question: How do I remove a domain from alternative distribution?
  phrasing_ops: 4
  slug: ios-alternativedistributiondomains-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The AlternativeDistributionKeys API from iOS — 2 operation(s) for alternativedistributionkeys.
  name: iOS AlternativeDistributionKeys API
  phrasing_intents:
  - id: alternativeDistributionKeys_getCollection
    intent: List alternative distribution keys
    question: How do I list my alternative distribution keys?
  - id: alternativeDistributionKeys_createInstance
    intent: Add an alternative distribution key
    question: How do I add a public key for alternative app distribution?
  - id: alternativeDistributionKeys_getInstance
    intent: Get an alternative distribution key
    question: Can I look up a single alternative distribution key by ID?
  - id: alternativeDistributionKeys_deleteInstance
    intent: Delete an alternative distribution key
    question: Is there a way to revoke an alternative distribution key?
  phrasing_ops: 4
  slug: ios-alternativedistributionkeys-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The AlternativeDistributionPackageDeltas API from iOS — 1 operation(s) for alternativedistributionpackagedeltas.
  name: iOS AlternativeDistributionPackageDeltas API
  phrasing_intents:
  - id: alternativeDistributionPackageDeltas_getInstance
    intent: Get an alternative distribution package delta
    question: Where do I get the delta update file for an alternative distribution package?
  phrasing_ops: 1
  slug: ios-alternativedistributionpackagedeltas-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The AlternativeDistributionPackages API from iOS — 4 operation(s) for alternativedistributionpackages.
  name: iOS AlternativeDistributionPackages API
  phrasing_intents:
  - id: alternativeDistributionPackages_createInstance
    intent: Create an alternative distribution package
    question: How do I create a package to distribute my app through an alternative marketplace?
  - id: alternativeDistributionPackages_getInstance
    intent: Get an alternative distribution package
    question: What's in an alternative distribution package I created?
  - id: alternativeDistributionPackages_versions_getToManyRelationship
    intent: List version IDs of a distribution package
    question: Can I get just the version IDs of an alternative distribution package?
  - id: alternativeDistributionPackages_versions_getToManyRelated
    intent: List versions of a distribution package
    question: Which package versions are ready for alternative distribution?
  phrasing_ops: 4
  slug: ios-alternativedistributionpackages-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The AlternativeDistributionPackageVariants API from iOS — 1 operation(s) for alternativedistributionpackagevariants.
  name: iOS AlternativeDistributionPackageVariants API
  phrasing_intents:
  - id: alternativeDistributionPackageVariants_getInstance
    intent: Get an alternative distribution package variant
    question: Where do I get the download URL for an alternative distribution package variant?
  phrasing_ops: 1
  slug: ios-alternativedistributionpackagevariants-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The AlternativeDistributionPackageVersions API from iOS — 5 operation(s) for alternativedistributionpackageversions.
  name: iOS AlternativeDistributionPackageVersions API
  phrasing_intents:
  - id: alternativeDistributionPackageVersions_getInstance
    intent: Get an alternative distribution package version
    question: What is the state and download URL of an alternative marketplace package version?
  - id: alternativeDistributionPackageVersions_deltas_getToManyRelationship
    intent: List delta IDs for a package version
    question: Which delta package IDs exist for an alternative distribution version?
  - id: alternativeDistributionPackageVersions_deltas_getToManyRelated
    intent: List the delta update packages of a version
    question: What delta update files are available for an alternative marketplace version?
  - id: alternativeDistributionPackageVersions_variants_getToManyRelationship
    intent: List variant IDs for a package version
    question: Which variant IDs belong to an alternative distribution package version?
  - id: alternativeDistributionPackageVersions_variants_getToManyRelated
    intent: List the device variants of a package version
    question: What device-specific variants were generated for my alternative distribution package?
  phrasing_ops: 5
  slug: ios-alternativedistributionpackageversions-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The AnalyticsReportInstances API from iOS — 3 operation(s) for analyticsreportinstances.
  name: iOS AnalyticsReportInstances API
  phrasing_intents:
  - id: analyticsReportInstances_getInstance
    intent: Get an analytics report instance
    question: Which date and granularity does an analytics report instance cover?
  - id: analyticsReportInstances_segments_getToManyRelationship
    intent: List segment IDs of an analytics report instance
    question: Can I get only the IDs of the segments in an analytics report instance?
  - id: analyticsReportInstances_segments_getToManyRelated
    intent: List downloadable segments of a report instance
    question: Where do I get the download URLs for an analytics report's data files?
  phrasing_ops: 3
  slug: ios-analyticsreportinstances-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The AnalyticsReportRequests API from iOS — 4 operation(s) for analyticsreportrequests.
  name: iOS AnalyticsReportRequests API
  phrasing_intents:
  - id: analyticsReportRequests_createInstance
    intent: Request analytics reports for an app
    question: How do I start getting App Store analytics reports for my app?
  - id: analyticsReportRequests_getInstance
    intent: Get an analytics report request
    question: What is the status of an analytics report request I made?
  - id: analyticsReportRequests_deleteInstance
    intent: Cancel an analytics report request
    question: How do I stop an ongoing analytics report request?
  - id: analyticsReportRequests_reports_getToManyRelationship
    intent: List report IDs for a request
    question: How do I get just the report IDs produced by a request?
  - id: analyticsReportRequests_reports_getToManyRelated
    intent: List reports for a request
    question: Which analytics reports are available from my request?
  phrasing_ops: 5
  slug: ios-analyticsreportrequests-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The AnalyticsReportSegments API from iOS — 1 operation(s) for analyticsreportsegments.
  name: iOS AnalyticsReportSegments API
  phrasing_intents:
  - id: analyticsReportSegments_getInstance
    intent: Get an analytics report segment
    question: How do I get the download URL for a segment of an analytics report?
  phrasing_ops: 1
  slug: ios-analyticsreportsegments-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The AndroidToIosAppMappingDetails API from iOS — 2 operation(s) for androidtoiosappmappingdetails.
  name: iOS AndroidToIosAppMappingDetails API
  phrasing_intents:
  - id: androidToIosAppMappingDetails_createInstance
    intent: Map an Android app to an iOS app
    question: How do I link my Android app's package to my iOS app for migration?
  - id: androidToIosAppMappingDetails_getInstance
    intent: Get an Android-to-iOS app mapping
    question: Can I view an existing Android-to-iOS app mapping?
  - id: androidToIosAppMappingDetails_updateInstance
    intent: Update an Android-to-iOS app mapping
    question: Can I change the Android package name or fingerprints on a mapping?
  - id: androidToIosAppMappingDetails_deleteInstance
    intent: Delete an Android-to-iOS app mapping
    question: How do I remove the link between my Android and iOS apps?
  phrasing_ops: 4
  slug: ios-androidtoiosappmappingdetails-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The AppAvailabilities API from iOS — 4 operation(s) for appavailabilities.
  name: iOS AppAvailabilities API
  phrasing_intents:
  - id: appAvailabilitiesV2_createInstance
    intent: Set where an app is available
    question: How do I choose which countries my app is sold in?
  - id: appAvailabilitiesV2_getInstance
    intent: Get an app's availability settings
    question: Is my app set to become available in new territories automatically?
  - id: appAvailabilitiesV2_territoryAvailabilities_getToManyRelationship
    intent: List territory availability IDs for an app
    question: Which territory availability IDs belong to an app availability?
  - id: appAvailabilitiesV2_territoryAvailabilities_getToManyRelated
    intent: List per-territory availability for an app
    question: In which countries is my app available, and are any pre-order only?
  phrasing_ops: 4
  slug: ios-appavailabilities-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The AppClipAdvancedExperienceImages API from iOS — 2 operation(s) for appclipadvancedexperienceimages.
  name: iOS AppClipAdvancedExperienceImages API
  phrasing_intents:
  - id: appClipAdvancedExperienceImages_createInstance
    intent: Reserve an image upload for an advanced App Clip experience
    question: How do I upload a header image for an advanced App Clip experience?
  - id: appClipAdvancedExperienceImages_getInstance
    intent: Get an advanced App Clip experience image
    question: Has my advanced App Clip experience image finished processing?
  - id: appClipAdvancedExperienceImages_updateInstance
    intent: Commit an advanced App Clip experience image upload
    question: How do I mark an App Clip experience image upload as complete?
  phrasing_ops: 3
  slug: ios-appclipadvancedexperienceimages-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The AppClipAdvancedExperiences API from iOS — 2 operation(s) for appclipadvancedexperiences.
  name: iOS AppClipAdvancedExperiences API
  phrasing_intents:
  - id: appClipAdvancedExperiences_createInstance
    intent: Create an advanced App Clip experience
    question: How do I set up an advanced App Clip experience for a specific location or URL?
  - id: appClipAdvancedExperiences_getInstance
    intent: Get an advanced App Clip experience
    question: What invocation URL, action and business details are set on an advanced App Clip experience?
  - id: appClipAdvancedExperiences_updateInstance
    intent: Update or deactivate an advanced App Clip experience
    question: How do I change the header image or action on an advanced App Clip experience?
  phrasing_ops: 3
  slug: ios-appclipadvancedexperiences-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The AppClipAppStoreReviewDetails API from iOS — 2 operation(s) for appclipappstorereviewdetails.
  name: iOS AppClipAppStoreReviewDetails API
  phrasing_intents:
  - id: appClipAppStoreReviewDetails_createInstance
    intent: Add App Review details for an App Clip
    question: How do I give App Review the invocation URLs to test my App Clip?
  - id: appClipAppStoreReviewDetails_getInstance
    intent: Get App Review details for an App Clip
    question: What invocation URLs have I already given App Review for my App Clip?
  - id: appClipAppStoreReviewDetails_updateInstance
    intent: Update App Review details for an App Clip
    question: Can I change the App Clip invocation URLs I submitted for review?
  phrasing_ops: 3
  slug: ios-appclipappstorereviewdetails-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The AppClipDefaultExperienceLocalizations API from iOS — 4 operation(s) for appclipdefaultexperiencelocalizations.
  name: iOS AppClipDefaultExperienceLocalizations API
  phrasing_intents:
  - id: appClipDefaultExperienceLocalizations_createInstance
    intent: Localize an App Clip default experience
    question: How do I add a localized subtitle for my App Clip's default experience?
  - id: appClipDefaultExperienceLocalizations_getInstance
    intent: Get an App Clip default experience localization
    question: Can I view one localized version of my App Clip default experience?
  - id: appClipDefaultExperienceLocalizations_updateInstance
    intent: Update an App Clip experience localization
    question: Can I change the subtitle on a localized App Clip card?
  - id: appClipDefaultExperienceLocalizations_deleteInstance
    intent: Delete an App Clip experience localization
    question: How do I remove a language from my App Clip default experience?
  - id: appClipDefaultExperienceLocalizations_appClipHeaderImage_getToOneRelationship
    intent: Get the header image ID of an App Clip localization
    question: Which header image ID is set on an App Clip localization?
  - id: appClipDefaultExperienceLocalizations_appClipHeaderImage_getToOneRelated
    intent: Get the header image of an App Clip localization
    question: What header image is shown on my localized App Clip card?
  phrasing_ops: 6
  slug: ios-appclipdefaultexperiencelocalizations-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The AppClipDefaultExperiences API from iOS — 8 operation(s) for appclipdefaultexperiences.
  name: iOS AppClipDefaultExperiences API
  phrasing_intents:
  - id: appClipDefaultExperiences_createInstance
    intent: Create an App Clip default experience
    question: How do I set up the default experience for my App Clip?
  - id: appClipDefaultExperiences_getInstance
    intent: Get an App Clip default experience
    question: What action and settings does my App Clip default experience use?
  - id: appClipDefaultExperiences_updateInstance
    intent: Update an App Clip default experience
    question: How do I change the call-to-action on my App Clip card?
  - id: appClipDefaultExperiences_deleteInstance
    intent: Delete an App Clip default experience
    question: Can I delete a default experience I no longer need for my App Clip?
  - id: appClipDefaultExperiences_appClipAppStoreReviewDetail_getToOneRelationship
    intent: Get the review detail ID for an App Clip experience
    question: Which App Store review detail ID is linked to my App Clip default experience?
  - id: appClipDefaultExperiences_appClipAppStoreReviewDetail_getToOneRelated
    intent: Get App Review details for an App Clip experience
    question: What invocation URLs did I give App Review for my App Clip?
  - id: appClipDefaultExperiences_appClipDefaultExperienceLocalizations_getToManyRelationship
    intent: List localization IDs of an App Clip experience
    question: Which localization IDs belong to my App Clip default experience?
  - id: appClipDefaultExperiences_appClipDefaultExperienceLocalizations_getToManyRelated
    intent: List an App Clip experience's localized subtitles
    question: What subtitles does my App Clip card show in each language?
  phrasing_ops: 11
  slug: ios-appclipdefaultexperiences-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The AppClipHeaderImages API from iOS — 2 operation(s) for appclipheaderimages.
  name: iOS AppClipHeaderImages API
  phrasing_intents:
  - id: appClipHeaderImages_createInstance
    intent: Reserve an App Clip card header image upload
    question: How do I add a header image to my App Clip card?
  - id: appClipHeaderImages_getInstance
    intent: Get an App Clip header image
    question: What is the upload state of my App Clip card header image?
  - id: appClipHeaderImages_updateInstance
    intent: Commit an App Clip header image upload
    question: Once I've uploaded the App Clip header image bytes, what marks the upload complete?
  - id: appClipHeaderImages_deleteInstance
    intent: Delete an App Clip header image
    question: How do I remove the header image from an App Clip card?
  phrasing_ops: 4
  slug: ios-appclipheaderimages-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The AppClips API from iOS — 5 operation(s) for appclips.
  name: iOS AppClips API
  phrasing_intents:
  - id: appClips_getInstance
    intent: Get an App Clip
    question: How do I look up an App Clip by ID?
  - id: appClips_appClipAdvancedExperiences_getToManyRelationship
    intent: List advanced experience IDs of an App Clip
    question: Which advanced experience IDs are attached to my App Clip?
  - id: appClips_appClipAdvancedExperiences_getToManyRelated
    intent: List an App Clip's advanced experiences
    question: Where can I see the advanced experiences configured for an App Clip?
  - id: appClips_appClipDefaultExperiences_getToManyRelationship
    intent: List default experience IDs of an App Clip
    question: Which default experience IDs belong to my App Clip?
  - id: appClips_appClipDefaultExperiences_getToManyRelated
    intent: List an App Clip's default experiences
    question: What default experiences are set up for my App Clip?
  phrasing_ops: 5
  slug: ios-appclips-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The AppCustomProductPageLocalizations API from iOS — 8 operation(s) for appcustomproductpagelocalizations.
  name: iOS AppCustomProductPageLocalizations API
  phrasing_intents:
  - id: appCustomProductPageLocalizations_createInstance
    intent: Add a localization to a custom product page
    question: How do I add a new language to an App Store custom product page?
  - id: appCustomProductPageLocalizations_getInstance
    intent: Get a custom product page localization
    question: What's in one localization of my custom product page?
  - id: appCustomProductPageLocalizations_updateInstance
    intent: Update a custom product page localization
    question: Can I change the promotional text of a localized custom product page?
  - id: appCustomProductPageLocalizations_deleteInstance
    intent: Delete a custom product page localization
    question: How do I drop a language from a custom product page?
  - id: appCustomProductPageLocalizations_appPreviewSets_getToManyRelationship
    intent: List preview set IDs of a custom page localization
    question: Can I get just the app preview set IDs for a custom page localization?
  - id: appCustomProductPageLocalizations_appPreviewSets_getToManyRelated
    intent: List app preview sets of a custom page localization
    question: What app preview videos are on a localized custom product page?
  - id: appCustomProductPageLocalizations_appScreenshotSets_getToManyRelationship
    intent: List screenshot set IDs of a custom page localization
    question: Can I get only the screenshot set IDs for a custom page localization?
  - id: appCustomProductPageLocalizations_appScreenshotSets_getToManyRelated
    intent: List screenshot sets of a custom page localization
    question: What screenshots are shown on a localized custom product page?
  phrasing_ops: 12
  slug: ios-appcustomproductpagelocalizations-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The AppCustomProductPages API from iOS — 4 operation(s) for appcustomproductpages.
  name: iOS AppCustomProductPages API
  phrasing_intents:
  - id: appCustomProductPages_createInstance
    intent: Create a custom product page
    question: How do I make a custom App Store product page for a specific ad campaign?
  - id: appCustomProductPages_getInstance
    intent: Get a custom product page
    question: What is the name, URL and visibility of one custom product page?
  - id: appCustomProductPages_updateInstance
    intent: Update a custom product page
    question: Can I rename a custom product page or hide it from visibility?
  - id: appCustomProductPages_deleteInstance
    intent: Delete a custom product page
    question: Can I remove a custom product page once its campaign is over?
  - id: appCustomProductPages_appCustomProductPageVersions_getToManyRelationship
    intent: List version IDs of a custom product page
    question: Which version IDs belong to a custom product page?
  - id: appCustomProductPages_appCustomProductPageVersions_getToManyRelated
    intent: List versions of a custom product page
    question: What versions of a custom product page exist and which one is approved?
  phrasing_ops: 6
  slug: ios-appcustomproductpages-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The AppCustomProductPageVersions API from iOS — 4 operation(s) for appcustomproductpageversions.
  name: iOS AppCustomProductPageVersions API
  phrasing_intents:
  - id: appCustomProductPageVersions_createInstance
    intent: Create a custom product page version
    question: How do I start a new version of a custom product page?
  - id: appCustomProductPageVersions_getInstance
    intent: Get a custom product page version
    question: What state and deep link does a custom product page version have?
  - id: appCustomProductPageVersions_updateInstance
    intent: Update a custom product page version
    question: Can I change the deep link on a custom product page version?
  - id: appCustomProductPageVersions_appCustomProductPageLocalizations_getToManyRelationship
    intent: List localization IDs of a product page version
    question: Can I get only the IDs of a custom product page version's localizations?
  - id: appCustomProductPageVersions_appCustomProductPageLocalizations_getToManyRelated
    intent: List a product page version's localizations
    question: What promotional text is set in each language on my custom product page?
  phrasing_ops: 5
  slug: ios-appcustomproductpageversions-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The AppEncryptionDeclarationDocuments API from iOS — 2 operation(s) for appencryptiondeclarationdocuments.
  name: iOS AppEncryptionDeclarationDocuments API
  phrasing_intents:
  - id: appEncryptionDeclarationDocuments_createInstance
    intent: Reserve an encryption declaration document upload
    question: How do I upload export compliance paperwork for my app's encryption declaration?
  - id: appEncryptionDeclarationDocuments_getInstance
    intent: Get an encryption declaration document
    question: Did my export compliance document finish uploading?
  - id: appEncryptionDeclarationDocuments_updateInstance
    intent: Commit an encryption declaration document upload
    question: How do I finalize an export compliance document upload?
  phrasing_ops: 3
  slug: ios-appencryptiondeclarationdocuments-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The AppEncryptionDeclarations API from iOS — 7 operation(s) for appencryptiondeclarations.
  name: iOS AppEncryptionDeclarations API
  phrasing_intents:
  - id: appEncryptionDeclarations_getCollection
    intent: List export compliance encryption declarations
    question: How do I list the export compliance encryption declarations for my app?
  - id: appEncryptionDeclarations_createInstance
    intent: Submit an export compliance encryption declaration
    question: How do I submit an export compliance encryption declaration?
  - id: appEncryptionDeclarations_getInstance
    intent: Get an encryption declaration
    question: Can I look up one encryption declaration by ID?
  - id: appEncryptionDeclarations_app_getToOneRelationship
    intent: Get the app ID of an encryption declaration
    question: Which app ID is an encryption declaration attached to?
  - id: appEncryptionDeclarations_app_getToOneRelated
    intent: Get the app an encryption declaration covers
    question: Which app does this encryption declaration belong to?
  - id: appEncryptionDeclarations_appEncryptionDeclarationDocument_getToOneRelationship
    intent: Get the document ID of an encryption declaration
    question: What's the document ID attached to my encryption declaration?
  - id: appEncryptionDeclarations_appEncryptionDeclarationDocument_getToOneRelated
    intent: Get an encryption declaration's document
    question: How do I see the uploaded document for an encryption declaration?
  - id: appEncryptionDeclarations_builds_createToManyRelationship
    intent: Attach builds to an encryption declaration
    question: How do I attach builds to an existing encryption declaration?
  phrasing_ops: 8
  slug: ios-appencryptiondeclarations-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The AppEventLocalizations API from iOS — 6 operation(s) for appeventlocalizations.
  name: iOS AppEventLocalizations API
  phrasing_intents:
  - id: appEventLocalizations_createInstance
    intent: Add a language to an in-app event
    question: How do I add a localized name and description for an in-app event?
  - id: appEventLocalizations_getInstance
    intent: Get an in-app event localization
    question: Can I view the localized text for one in-app event language?
  - id: appEventLocalizations_updateInstance
    intent: Update an in-app event localization
    question: Can I edit the localized name or descriptions of an in-app event?
  - id: appEventLocalizations_deleteInstance
    intent: Delete an in-app event localization
    question: How do I remove a language from an in-app event?
  - id: appEventLocalizations_appEventScreenshots_getToManyRelationship
    intent: List IDs of an event localization's screenshots
    question: Can I get just the screenshot IDs for an in-app event localization?
  - id: appEventLocalizations_appEventScreenshots_getToManyRelated
    intent: List an event localization's screenshots
    question: What screenshots are uploaded for an in-app event in a given language?
  - id: appEventLocalizations_appEventVideoClips_getToManyRelationship
    intent: List IDs of an event localization's video clips
    question: Can I fetch only the video clip IDs for an in-app event localization?
  - id: appEventLocalizations_appEventVideoClips_getToManyRelated
    intent: List an event localization's video clips
    question: What video clips are attached to my in-app event in this language?
  phrasing_ops: 8
  slug: ios-appeventlocalizations-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The AppEventScreenshots API from iOS — 2 operation(s) for appeventscreenshots.
  name: iOS AppEventScreenshots API
  phrasing_intents:
  - id: appEventScreenshots_createInstance
    intent: Reserve an in-app event screenshot
    question: How do I upload a screenshot for an in-app event?
  - id: appEventScreenshots_getInstance
    intent: Get an in-app event screenshot
    question: Has my in-app event screenshot finished processing?
  - id: appEventScreenshots_updateInstance
    intent: Commit an in-app event screenshot upload
    question: How do I mark an app event screenshot upload as complete?
  - id: appEventScreenshots_deleteInstance
    intent: Delete an in-app event screenshot
    question: Can I remove a screenshot from an in-app event?
  phrasing_ops: 4
  slug: ios-appeventscreenshots-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The AppEventVideoClips API from iOS — 2 operation(s) for appeventvideoclips.
  name: iOS AppEventVideoClips API
  phrasing_intents:
  - id: appEventVideoClips_createInstance
    intent: Reserve an in-app event video clip upload
    question: How do I upload a video for an in-app event on the App Store?
  - id: appEventVideoClips_getInstance
    intent: Get an in-app event video clip
    question: Has my in-app event video finished processing?
  - id: appEventVideoClips_updateInstance
    intent: Commit or adjust an in-app event video clip
    question: How do I confirm an in-app event video upload is complete?
  - id: appEventVideoClips_deleteInstance
    intent: Delete an in-app event video clip
    question: Can I remove a video from my in-app event?
  phrasing_ops: 4
  slug: ios-appeventvideoclips-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The AppInfoLocalizations API from iOS — 2 operation(s) for appinfolocalizations.
  name: iOS AppInfoLocalizations API
  phrasing_intents:
  - id: appInfoLocalizations_createInstance
    intent: Add an app info localization
    question: How do I add my app's name and subtitle in a new language?
  - id: appInfoLocalizations_getInstance
    intent: Get an app info localization
    question: What localized name and privacy policy URL are set for one locale?
  - id: appInfoLocalizations_updateInstance
    intent: Update an app info localization
    question: How do I change my app's localized name or subtitle?
  - id: appInfoLocalizations_deleteInstance
    intent: Delete an app info localization
    question: How do I remove a language from my app info?
  phrasing_ops: 4
  slug: ios-appinfolocalizations-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The AppInfos API from iOS — 19 operation(s) for appinfos.
  name: iOS AppInfos API
  phrasing_intents:
  - id: appInfos_getInstance
    intent: Get an app's App Store info record
    question: How do I look up an app info record by ID?
  - id: appInfos_updateInstance
    intent: Update an app's App Store info
    question: Can I change my app's App Store info record, such as its categories?
  - id: appInfos_ageRatingDeclaration_getToOneRelationship
    intent: Get the age rating declaration ID for an app
    question: Which age rating declaration ID is linked to my app info?
  - id: appInfos_ageRatingDeclaration_getToOneRelated
    intent: Get an app's age rating declaration
    question: Where can I see the age rating questionnaire answers for my app?
  - id: appInfos_appInfoLocalizations_getToManyRelationship
    intent: List localization IDs of an app info record
    question: Which localization IDs belong to an app info record?
  - id: appInfos_appInfoLocalizations_getToManyRelated
    intent: List an app's localized App Store info
    question: How do I see my app's localized App Store details for each language?
  - id: appInfos_primaryCategory_getToOneRelationship
    intent: Get the primary category ID of an app
    question: Which category ID is set as my app's primary category?
  - id: appInfos_primaryCategory_getToOneRelated
    intent: Get an app's primary App Store category
    question: What primary App Store category is my app listed under?
  phrasing_ops: 20
  slug: ios-appinfos-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The AppPreviewSets API from iOS — 4 operation(s) for apppreviewsets.
  name: iOS AppPreviewSets API
  phrasing_intents:
  - id: appPreviewSets_createInstance
    intent: Create an app preview set
    question: How do I create a set to hold app preview videos for a display type?
  - id: appPreviewSets_getInstance
    intent: Get an app preview set
    question: What device type does a given app preview set target?
  - id: appPreviewSets_deleteInstance
    intent: Delete an app preview set
    question: How do I remove an app preview set and its videos?
  - id: appPreviewSets_appPreviews_getToManyRelationship
    intent: List preview IDs in a set
    question: How do I get just the IDs of the previews in a set, in order?
  - id: appPreviewSets_appPreviews_replaceToManyRelationship
    intent: Reorder or replace previews in a set
    question: How do I change the order of app previews in a set?
  - id: appPreviewSets_appPreviews_getToManyRelated
    intent: List previews in a set
    question: Which preview videos are in a set, with their upload details?
  phrasing_ops: 6
  slug: ios-apppreviewsets-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The AppPricePoints API from iOS — 3 operation(s) for apppricepoints.
  name: iOS AppPricePoints API
  phrasing_intents:
  - id: appPricePointsV3_getInstance
    intent: Get an app price point
    question: What customer price and proceeds does an app price point have?
  - id: appPricePointsV3_equalizations_getToManyRelationship
    intent: List IDs of a price point's equivalents
    question: Can I get just the IDs of the equalized price points in other territories?
  - id: appPricePointsV3_equalizations_getToManyRelated
    intent: List equivalent prices in other territories
    question: What would my app's price be in other countries at the same tier?
  phrasing_ops: 3
  slug: ios-apppricepoints-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The AppPriceSchedules API from iOS — 8 operation(s) for apppriceschedules.
  name: iOS AppPriceSchedules API
  phrasing_intents:
  - id: appPriceSchedules_createInstance
    intent: Set an app's price schedule
    question: How do I change the price of my paid app starting on a future date?
  - id: appPriceSchedules_getInstance
    intent: Get an app's price schedule
    question: What does my app's current price schedule look like?
  - id: appPriceSchedules_automaticPrices_getToManyRelationship
    intent: List automatic app price IDs in a schedule
    question: Which automatically equalized app price IDs belong to a price schedule?
  - id: appPriceSchedules_automaticPrices_getToManyRelated
    intent: List automatically equalized app prices
    question: What prices did Apple automatically set for my app in other countries?
  - id: appPriceSchedules_baseTerritory_getToOneRelationship
    intent: Get the base territory ID of an app price schedule
    question: Which territory ID is the base for my app's price schedule?
  - id: appPriceSchedules_baseTerritory_getToOneRelated
    intent: Get the base territory of an app price schedule
    question: Which country and currency is my app's pricing anchored to?
  - id: appPriceSchedules_manualPrices_getToManyRelationship
    intent: List manual app price IDs in a schedule
    question: Which manually set app price IDs are in a price schedule?
  - id: appPriceSchedules_manualPrices_getToManyRelated
    intent: List manually set app prices
    question: What prices did I set by hand for my app, and when do they take effect?
  phrasing_ops: 8
  slug: ios-apppriceschedules-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The Apps API from iOS — 84 operation(s) for apps.
  name: iOS Apps API
  phrasing_intents:
  - id: apps_getCollection
    intent: List my apps
    question: How do I see every app in my App Store Connect account?
  - id: apps_getInstance
    intent: Get an app's details
    question: What details can I pull for a single app, like its bundle ID and primary locale?
  - id: apps_updateInstance
    intent: Update an app's settings
    question: Can I change an app's primary locale or content rights declaration?
  - id: apps_accessibilityDeclarations_getToManyRelationship
    intent: List accessibility declaration IDs for an app
    question: Can I get only the IDs of the accessibility declarations linked to an app?
  - id: apps_accessibilityDeclarations_getToManyRelated
    intent: List an app's accessibility declarations
    question: What accessibility support has my app declared on the App Store?
  - id: apps_alternativeDistributionKey_getToOneRelationship
    intent: Get an app's alternative distribution key ID
    question: Can I get just the ID of the alternative distribution key tied to an app?
  - id: apps_alternativeDistributionKey_getToOneRelated
    intent: Get an app's alternative distribution key
    question: Where do I read the public key my app uses for alternative distribution?
  - id: apps_analyticsReportRequests_getToManyRelationship
    intent: List analytics report request IDs for an app
    question: Can I get only the IDs of the analytics report requests made for an app?
  phrasing_ops: 86
  slug: ios-apps-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The AppScreenshots API from iOS — 2 operation(s) for appscreenshots.
  name: iOS AppScreenshots API
  phrasing_intents:
  - id: appScreenshots_createInstance
    intent: Reserve an App Store screenshot upload
    question: How do I upload a new screenshot to my App Store listing?
  - id: appScreenshots_getInstance
    intent: Get an App Store screenshot
    question: Has my screenshot finished processing?
  - id: appScreenshots_updateInstance
    intent: Commit or update a screenshot upload
    question: How do I mark a screenshot upload as complete after sending the file?
  - id: appScreenshots_deleteInstance
    intent: Delete an App Store screenshot
    question: How do I remove a screenshot from my App Store page?
  phrasing_ops: 4
  slug: ios-appscreenshots-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The AppScreenshotSets API from iOS — 4 operation(s) for appscreenshotsets.
  name: iOS AppScreenshotSets API
  phrasing_intents:
  - id: appScreenshotSets_createInstance
    intent: Create a screenshot set for a display size
    question: How do I add a new screenshot set for a specific device display size?
  - id: appScreenshotSets_getInstance
    intent: Get a screenshot set
    question: What display type and localization does a screenshot set belong to?
  - id: appScreenshotSets_deleteInstance
    intent: Delete a screenshot set
    question: Can I remove an entire screenshot set for a display size?
  - id: appScreenshotSets_appScreenshots_getToManyRelationship
    intent: List screenshot IDs in a set in order
    question: Can I get only the IDs of the screenshots in a set, in display order?
  - id: appScreenshotSets_appScreenshots_replaceToManyRelationship
    intent: Reorder the screenshots in a set
    question: How do I change the order my App Store screenshots appear in?
  - id: appScreenshotSets_appScreenshots_getToManyRelated
    intent: List the screenshots in a set
    question: What screenshots are in a set, with their file names and upload state?
  phrasing_ops: 6
  slug: ios-appscreenshotsets-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The AppStoreReviewAttachments API from iOS — 2 operation(s) for appstorereviewattachments.
  name: iOS AppStoreReviewAttachments API
  phrasing_intents:
  - id: appStoreReviewAttachments_createInstance
    intent: Reserve an attachment for App Review
    question: How do I attach a file or demo video for the App Review team?
  - id: appStoreReviewAttachments_getInstance
    intent: Get an App Review attachment
    question: Did my App Review attachment finish uploading?
  - id: appStoreReviewAttachments_updateInstance
    intent: Commit an App Review attachment upload
    question: How do I mark a review attachment upload as finished?
  - id: appStoreReviewAttachments_deleteInstance
    intent: Delete an App Review attachment
    question: Can I remove a file I attached for App Review?
  phrasing_ops: 4
  slug: ios-appstorereviewattachments-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The AppStoreReviewDetails API from iOS — 4 operation(s) for appstorereviewdetails.
  name: iOS AppStoreReviewDetails API
  phrasing_intents:
  - id: appStoreReviewDetails_createInstance
    intent: Add App Review contact and demo details
    question: How do I give App Review a demo account and contact person for a version?
  - id: appStoreReviewDetails_getInstance
    intent: Get App Review details for a version
    question: What contact info and demo account did I give App Review?
  - id: appStoreReviewDetails_updateInstance
    intent: Update App Review details
    question: How do I change the demo account password I gave App Review?
  - id: appStoreReviewDetails_appStoreReviewAttachments_getToManyRelationship
    intent: List attachment IDs on App Review details
    question: Which attachment IDs are attached to my App Review details?
  - id: appStoreReviewDetails_appStoreReviewAttachments_getToManyRelated
    intent: List files attached for App Review
    question: What files have I attached to help App Review test my app?
  phrasing_ops: 5
  slug: ios-appstorereviewdetails-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The AppStoreVersionExperiments API from iOS — 8 operation(s) for appstoreversionexperiments.
  name: iOS AppStoreVersionExperiments API
  phrasing_intents:
  - id: appStoreVersionExperimentsV2_createInstance
    intent: Create a product page optimization test
    question: How do I start a new A/B test of my App Store product page?
  - id: appStoreVersionExperimentsV2_getInstance
    intent: Get a product page optimization test
    question: Can I look up a product page experiment by ID?
  - id: appStoreVersionExperimentsV2_updateInstance
    intent: Update a product page optimization test
    question: Can I edit an App Store version experiment after creating it?
  - id: appStoreVersionExperimentsV2_deleteInstance
    intent: Delete a product page optimization test
    question: Can I delete a product page experiment I no longer need?
  - id: appStoreVersionExperiments_createInstance
    intent: Create a version experiment (legacy v1)
    question: Can I still create a version experiment through the legacy v1 endpoint?
  - id: appStoreVersionExperiments_getInstance
    intent: Get a version experiment (legacy v1)
    question: Is fetching a version experiment still possible through the legacy v1 endpoint?
  - id: appStoreVersionExperiments_updateInstance
    intent: Update a version experiment (legacy v1)
    question: Is editing a product page test still possible on the older v1 API?
  - id: appStoreVersionExperiments_deleteInstance
    intent: Delete a version experiment (legacy v1)
    question: Can I delete a version experiment through the legacy v1 endpoint?
  phrasing_ops: 12
  slug: ios-appstoreversionexperiments-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The AppStoreVersionExperimentTreatmentLocalizations API from iOS — 6 operation(s) for appstoreversionexperimenttreatmentlocalizations.
  name: iOS AppStoreVersionExperimentTreatmentLocalizations API
  phrasing_intents:
  - id: appStoreVersionExperimentTreatmentLocalizations_createInstance
    intent: Localize a product page test treatment
    question: How do I add a locale to a treatment in my App Store product page optimization test?
  - id: appStoreVersionExperimentTreatmentLocalizations_getInstance
    intent: Get a treatment localization
    question: Which locale does a given experiment treatment localization cover?
  - id: appStoreVersionExperimentTreatmentLocalizations_deleteInstance
    intent: Delete a treatment localization
    question: Can I remove a language from a product page optimization treatment?
  - id: appStoreVersionExperimentTreatmentLocalizations_appPreviewSets_getToManyRelationship
    intent: List preview set IDs for a treatment locale
    question: Which app preview set IDs are attached to my treatment localization?
  - id: appStoreVersionExperimentTreatmentLocalizations_appPreviewSets_getToManyRelated
    intent: List preview sets for a treatment locale
    question: What app preview videos am I testing in this treatment localization?
  - id: appStoreVersionExperimentTreatmentLocalizations_appScreenshotSets_getToManyRelationship
    intent: List screenshot set IDs for a treatment locale
    question: Which screenshot set IDs belong to my treatment localization?
  - id: appStoreVersionExperimentTreatmentLocalizations_appScreenshotSets_getToManyRelated
    intent: List screenshot sets for a treatment locale
    question: What screenshots am I testing in this product page treatment localization?
  phrasing_ops: 7
  slug: ios-appstoreversionexperimenttreatmentlocalizations-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The AppStoreVersionExperimentTreatments API from iOS — 4 operation(s) for appstoreversionexperimenttreatments.
  name: iOS AppStoreVersionExperimentTreatments API
  phrasing_intents:
  - id: appStoreVersionExperimentTreatments_createInstance
    intent: Create a product page test treatment
    question: How do I add a variant to an App Store product page optimization test?
  - id: appStoreVersionExperimentTreatments_getInstance
    intent: Get a product page test treatment
    question: What does one treatment in my product page test contain?
  - id: appStoreVersionExperimentTreatments_updateInstance
    intent: Update a product page test treatment
    question: Can I rename a treatment or change its icon?
  - id: appStoreVersionExperimentTreatments_deleteInstance
    intent: Delete a product page test treatment
    question: How do I remove a variant from a product page optimization test?
  - id: appStoreVersionExperimentTreatments_appStoreVersionExperimentTreatmentLocalizations_getToManyRelationship
    intent: List localization IDs of a test treatment
    question: Can I get just the localization IDs of an experiment treatment?
  - id: appStoreVersionExperimentTreatments_appStoreVersionExperimentTreatmentLocalizations_getToManyRelated
    intent: List localizations of a test treatment
    question: Which languages does a product page test variant have assets for?
  phrasing_ops: 6
  slug: ios-appstoreversionexperimenttreatments-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The AppStoreVersionLocalizations API from iOS — 8 operation(s) for appstoreversionlocalizations.
  name: iOS AppStoreVersionLocalizations API
  phrasing_intents:
  - id: appStoreVersionLocalizations_createInstance
    intent: Add a language to an App Store version
    question: How do I add a Japanese description and keywords to my upcoming App Store version?
  - id: appStoreVersionLocalizations_getInstance
    intent: Get an App Store version localization
    question: What description, promotional text and what's-new notes does one version localization hold?
  - id: appStoreVersionLocalizations_updateInstance
    intent: Update a version's localized store text
    question: Can I change the what's-new text for one language after I already created it?
  - id: appStoreVersionLocalizations_deleteInstance
    intent: Delete an App Store version localization
    question: Can I remove a language from my version's App Store listing?
  - id: appStoreVersionLocalizations_appPreviewSets_getToManyRelationship
    intent: List app preview set IDs for a version localization
    question: Which app preview set IDs belong to a version localization?
  - id: appStoreVersionLocalizations_appPreviewSets_getToManyRelated
    intent: List app preview video sets for a version localization
    question: What app preview video sets exist for this language of my listing?
  - id: appStoreVersionLocalizations_appScreenshotSets_getToManyRelationship
    intent: List screenshot set IDs for a version localization
    question: Which screenshot set IDs are attached to a version localization?
  - id: appStoreVersionLocalizations_appScreenshotSets_getToManyRelated
    intent: List screenshot sets for a version localization
    question: Which device sizes have screenshots uploaded for this language of my version?
  phrasing_ops: 12
  slug: ios-appstoreversionlocalizations-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The AppStoreVersionPhasedReleases API from iOS — 2 operation(s) for appstoreversionphasedreleases.
  name: iOS AppStoreVersionPhasedReleases API
  phrasing_intents:
  - id: appStoreVersionPhasedReleases_createInstance
    intent: Turn on phased release for an app version
    question: How do I roll out an app update gradually over seven days instead of to everyone at once?
  - id: appStoreVersionPhasedReleases_updateInstance
    intent: Pause, resume or complete a phased release
    question: How can I pause a phased rollout when I spot a crash in the new version?
  - id: appStoreVersionPhasedReleases_deleteInstance
    intent: Remove phased release from an app version
    question: Can I cancel the phased rollout and go back to releasing to all users?
  phrasing_ops: 3
  slug: ios-appstoreversionphasedreleases-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The AppStoreVersionPromotions API from iOS — 1 operation(s) for appstoreversionpromotions.
  name: iOS AppStoreVersionPromotions API
  phrasing_intents:
  - id: appStoreVersionPromotions_createInstance
    intent: Promote a product page experiment treatment to a version
    question: How do I apply the winning treatment from a product page test to my app version?
  phrasing_ops: 1
  slug: ios-appstoreversionpromotions-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The AppStoreVersionReleaseRequests API from iOS — 1 operation(s) for appstoreversionreleaserequests.
  name: iOS AppStoreVersionReleaseRequests API
  phrasing_intents:
  - id: appStoreVersionReleaseRequests_createInstance
    intent: Release an approved App Store version
    question: My app version is approved but set to manual release; what makes it go live now?
  phrasing_ops: 1
  slug: ios-appstoreversionreleaserequests-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The AppStoreVersions API from iOS — 26 operation(s) for appstoreversions.
  name: iOS AppStoreVersions API
  phrasing_intents:
  - id: appStoreVersions_createInstance
    intent: Create a new App Store version for an app
    question: How do I start a new App Store version so I can prepare my next release in App Store Connect?
  - id: appStoreVersions_getInstance
    intent: Get an App Store version
    question: What state is a specific App Store version in right now?
  - id: appStoreVersions_updateInstance
    intent: Update an App Store version
    question: Can I change the version string or release type of an App Store version that already exists?
  - id: appStoreVersions_deleteInstance
    intent: Delete an App Store version
    question: Can I throw away an App Store version I created by mistake?
  - id: appStoreVersions_alternativeDistributionPackage_getToOneRelationship
    intent: Get the alternative distribution package ID for a version
    question: Which alternative distribution package ID is linked to an App Store version, without the full package details?
  - id: appStoreVersions_alternativeDistributionPackage_getToOneRelated
    intent: Get the alternative distribution package for a version
    question: Where can I see the full alternative distribution package record for an App Store version?
  - id: appStoreVersions_appClipDefaultExperience_getToOneRelationship
    intent: Get the App Clip default experience ID for a version
    question: Which App Clip default experience ID is currently linked to an App Store version?
  - id: appStoreVersions_appClipDefaultExperience_updateToOneRelationship
    intent: Link a default App Clip experience to a version
    question: Can I point an App Store version at a different default App Clip experience?
  phrasing_ops: 30
  slug: ios-appstoreversions-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The AppStoreVersionSubmissions API from iOS — 1 operation(s) for appstoreversionsubmissions.
  name: iOS AppStoreVersionSubmissions API
  phrasing_intents:
  - id: appStoreVersionSubmissions_deleteInstance
    intent: Withdraw an App Store version submission
    question: Can I pull an App Store version back out of review?
  phrasing_ops: 1
  slug: ios-appstoreversionsubmissions-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The AppTags API from iOS — 3 operation(s) for apptags.
  name: iOS AppTags API
  phrasing_intents:
  - id: appTags_updateInstance
    intent: Show or hide an App Store tag on my app
    question: How do I turn off an App Store tag that was assigned to my app?
  - id: appTags_territories_getToManyRelationship
    intent: List territory IDs for an app tag
    question: Which territory IDs is an app tag applied in?
  - id: appTags_territories_getToManyRelated
    intent: List the territories where an app tag shows
    question: In which countries and regions does an App Store tag appear for my app?
  phrasing_ops: 3
  slug: ios-apptags-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The BackgroundAssets API from iOS — 4 operation(s) for backgroundassets.
  name: iOS BackgroundAssets API
  phrasing_intents:
  - id: backgroundAssets_createInstance
    intent: Create a background asset
    question: How do I register a new background asset pack for my app?
  - id: backgroundAssets_getInstance
    intent: Get a background asset
    question: What details are stored for one background asset?
  - id: backgroundAssets_updateInstance
    intent: Update a background asset
    question: How do I change a background asset's attributes?
  - id: backgroundAssets_versions_getToManyRelationship
    intent: List version IDs of a background asset
    question: How do I get just the version IDs of a background asset?
  - id: backgroundAssets_versions_getToManyRelated
    intent: List versions of a background asset
    question: Which versions of a background asset are in beta or on the App Store?
  phrasing_ops: 5
  slug: ios-backgroundassets-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The BackgroundAssetUploadFiles API from iOS — 2 operation(s) for backgroundassetuploadfiles.
  name: iOS BackgroundAssetUploadFiles API
  phrasing_intents:
  - id: backgroundAssetUploadFiles_createInstance
    intent: Reserve a background asset upload file
    question: How do I start uploading a file for a background asset version?
  - id: backgroundAssetUploadFiles_getInstance
    intent: Get a background asset upload file
    question: Has my background asset file finished uploading and processing?
  - id: backgroundAssetUploadFiles_updateInstance
    intent: Commit a background asset upload file
    question: Can I mark a background asset file as uploaded once all parts are sent?
  phrasing_ops: 3
  slug: ios-backgroundassetuploadfiles-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The BackgroundAssetVersionAppStoreReleases API from iOS — 1 operation(s) for backgroundassetversionappstorereleases.
  name: iOS BackgroundAssetVersionAppStoreReleases API
  phrasing_intents:
  - id: backgroundAssetVersionAppStoreReleases_getInstance
    intent: Get a background asset App Store release
    question: Where can I look up an App Store release of a background asset version?
  phrasing_ops: 1
  slug: ios-backgroundassetversionappstorereleases-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The BackgroundAssetVersionExternalBetaReleases API from iOS — 1 operation(s) for backgroundassetversionexternalbetareleases.
  name: iOS BackgroundAssetVersionExternalBetaReleases API
  phrasing_intents:
  - id: backgroundAssetVersionExternalBetaReleases_getInstance
    intent: Get an external beta release of a background asset
    question: Is a background asset version released to external TestFlight testers?
  phrasing_ops: 1
  slug: ios-backgroundassetversionexternalbetareleases-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The BackgroundAssetVersionInternalBetaReleases API from iOS — 1 operation(s) for backgroundassetversioninternalbetareleases.
  name: iOS BackgroundAssetVersionInternalBetaReleases API
  phrasing_intents:
  - id: backgroundAssetVersionInternalBetaReleases_getInstance
    intent: Get a background asset internal beta release
    question: Is a background asset version released to internal TestFlight testers?
  phrasing_ops: 1
  slug: ios-backgroundassetversioninternalbetareleases-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The BackgroundAssetVersions API from iOS — 4 operation(s) for backgroundassetversions.
  name: iOS BackgroundAssetVersions API
  phrasing_intents:
  - id: backgroundAssetVersions_createInstance
    intent: Create a background asset version
    question: How do I create a new version of a background asset for my app?
  - id: backgroundAssetVersions_getInstance
    intent: Get a background asset version
    question: What state is my background asset version in?
  - id: backgroundAssetVersions_backgroundAssetUploadFiles_getToManyRelationship
    intent: List IDs of a version's upload files
    question: Can I get just the upload file IDs for a background asset version?
  - id: backgroundAssetVersions_backgroundAssetUploadFiles_getToManyRelated
    intent: List upload files of a background asset version
    question: What files were uploaded for a background asset version and are they processed?
  phrasing_ops: 4
  slug: ios-backgroundassetversions-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The BetaAppClipInvocationLocalizations API from iOS — 2 operation(s) for betaappclipinvocationlocalizations.
  name: iOS BetaAppClipInvocationLocalizations API
  phrasing_intents:
  - id: betaAppClipInvocationLocalizations_createInstance
    intent: Add a localized title for a TestFlight App Clip invocation
    question: How do I give testers a translated title for an App Clip invocation in TestFlight?
  - id: betaAppClipInvocationLocalizations_updateInstance
    intent: Update a TestFlight App Clip invocation localization
    question: How do I change the title testers see for an App Clip invocation?
  - id: betaAppClipInvocationLocalizations_deleteInstance
    intent: Delete a TestFlight App Clip invocation localization
    question: Can I remove a language from a TestFlight App Clip invocation?
  phrasing_ops: 3
  slug: ios-betaappclipinvocationlocalizations-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The BetaAppClipInvocations API from iOS — 2 operation(s) for betaappclipinvocations.
  name: iOS BetaAppClipInvocations API
  phrasing_intents:
  - id: betaAppClipInvocations_createInstance
    intent: Add a TestFlight App Clip invocation
    question: How do I give TestFlight testers a URL to launch my App Clip?
  - id: betaAppClipInvocations_getInstance
    intent: Get a TestFlight App Clip invocation
    question: Which URL does a beta App Clip invocation open for testers?
  - id: betaAppClipInvocations_updateInstance
    intent: Update a TestFlight App Clip invocation
    question: Can I change the URL on an existing beta App Clip invocation?
  - id: betaAppClipInvocations_deleteInstance
    intent: Delete a TestFlight App Clip invocation
    question: Can I remove an App Clip test URL testers should no longer use?
  phrasing_ops: 4
  slug: ios-betaappclipinvocations-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The BetaAppLocalizations API from iOS — 4 operation(s) for betaapplocalizations.
  name: iOS BetaAppLocalizations API
  phrasing_intents:
  - id: betaAppLocalizations_getCollection
    intent: List TestFlight app localizations
    question: What TestFlight descriptions and feedback emails have I set per language?
  - id: betaAppLocalizations_createInstance
    intent: Add TestFlight test information in a language
    question: How do I add a German description for testers in TestFlight?
  - id: betaAppLocalizations_getInstance
    intent: Get a TestFlight app localization
    question: What does a specific TestFlight localization say to testers?
  - id: betaAppLocalizations_updateInstance
    intent: Update a TestFlight app localization
    question: How do I change what testers see in the TestFlight app description?
  - id: betaAppLocalizations_deleteInstance
    intent: Delete a TestFlight app localization
    question: Can I remove a language from my TestFlight test information?
  - id: betaAppLocalizations_app_getToOneRelationship
    intent: Get the app ID of a TestFlight localization
    question: Which app ID does a beta app localization belong to?
  - id: betaAppLocalizations_app_getToOneRelated
    intent: Get the app behind a TestFlight localization
    question: What app name and bundle ID does a TestFlight localization belong to?
  phrasing_ops: 7
  slug: ios-betaapplocalizations-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The BetaAppReviewDetails API from iOS — 4 operation(s) for betaappreviewdetails.
  name: iOS BetaAppReviewDetails API
  phrasing_intents:
  - id: betaAppReviewDetails_getCollection
    intent: List beta app review details for an app
    question: Where do I find the TestFlight beta review details on file for my app?
  - id: betaAppReviewDetails_getInstance
    intent: Get a beta app review detail
    question: Can I look up a beta app review detail record by ID?
  - id: betaAppReviewDetails_updateInstance
    intent: Update beta app review details
    question: How do I change the review contact information for TestFlight beta review?
  - id: betaAppReviewDetails_app_getToOneRelationship
    intent: Get the app ID of a beta review detail
    question: Which app ID is a beta app review detail linked to?
  - id: betaAppReviewDetails_app_getToOneRelated
    intent: Get the app of a beta review detail
    question: Which app do these beta review details belong to?
  phrasing_ops: 5
  slug: ios-betaappreviewdetails-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The BetaAppReviewSubmissions API from iOS — 4 operation(s) for betaappreviewsubmissions.
  name: iOS BetaAppReviewSubmissions API
  phrasing_intents:
  - id: betaAppReviewSubmissions_getCollection
    intent: List beta app review submissions for a build
    question: Has my build been submitted for TestFlight beta review?
  - id: betaAppReviewSubmissions_createInstance
    intent: Submit a build for beta app review
    question: How do I send a build to Apple for TestFlight external beta review?
  - id: betaAppReviewSubmissions_getInstance
    intent: Get a beta app review submission
    question: What's the review state of a specific beta review submission?
  - id: betaAppReviewSubmissions_build_getToOneRelationship
    intent: Get the build ID of a beta review submission
    question: Can I get just the build ID for a beta review submission?
  - id: betaAppReviewSubmissions_build_getToOneRelated
    intent: Get the build in a beta review submission
    question: Which build version was sent to beta review in a submission?
  phrasing_ops: 5
  slug: ios-betaappreviewsubmissions-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The BetaBuildLocalizations API from iOS — 4 operation(s) for betabuildlocalizations.
  name: iOS BetaBuildLocalizations API
  phrasing_intents:
  - id: betaBuildLocalizations_getCollection
    intent: List beta build localizations
    question: What localized 'What to Test' notes exist for my TestFlight builds?
  - id: betaBuildLocalizations_createInstance
    intent: Add localized test notes to a build
    question: How do I add 'What to Test' notes in another language for a TestFlight build?
  - id: betaBuildLocalizations_getInstance
    intent: Get a beta build localization
    question: What do one localization's TestFlight test notes say?
  - id: betaBuildLocalizations_updateInstance
    intent: Update localized test notes for a build
    question: Can I edit the What to Test text after uploading a build?
  - id: betaBuildLocalizations_deleteInstance
    intent: Delete a beta build localization
    question: How do I remove one language's test notes from a build?
  - id: betaBuildLocalizations_build_getToOneRelationship
    intent: Get the build ID of a beta build localization
    question: Can I get just the build ID a beta localization belongs to?
  - id: betaBuildLocalizations_build_getToOneRelated
    intent: Get the build for a beta build localization
    question: Which build do these localized test notes describe?
  phrasing_ops: 7
  slug: ios-betabuildlocalizations-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The BetaCrashLogs API from iOS — 1 operation(s) for betacrashlogs.
  name: iOS BetaCrashLogs API
  phrasing_intents:
  - id: betaCrashLogs_getInstance
    intent: Get a TestFlight crash log
    question: Can I download the crash log a TestFlight tester submitted?
  phrasing_ops: 1
  slug: ios-betacrashlogs-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The BetaFeedbackCrashSubmissions API from iOS — 3 operation(s) for betafeedbackcrashsubmissions.
  name: iOS BetaFeedbackCrashSubmissions API
  phrasing_intents:
  - id: betaFeedbackCrashSubmissions_getInstance
    intent: Get a TestFlight crash feedback submission
    question: What did a TestFlight tester report when their app crashed?
  - id: betaFeedbackCrashSubmissions_deleteInstance
    intent: Delete a TestFlight crash feedback submission
    question: How do I delete a crash feedback submission from TestFlight?
  - id: betaFeedbackCrashSubmissions_crashLog_getToOneRelationship
    intent: Get the crash log ID for a crash submission
    question: Which crash log ID is attached to a TestFlight crash feedback submission?
  - id: betaFeedbackCrashSubmissions_crashLog_getToOneRelated
    intent: Download the crash log from tester feedback
    question: Where can I read the actual crash log text a tester sent with their feedback?
  phrasing_ops: 4
  slug: ios-betafeedbackcrashsubmissions-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The BetaFeedbackScreenshotSubmissions API from iOS — 1 operation(s) for betafeedbackscreenshotsubmissions.
  name: iOS BetaFeedbackScreenshotSubmissions API
  phrasing_intents:
  - id: betaFeedbackScreenshotSubmissions_getInstance
    intent: Get a beta screenshot feedback submission
    question: What did a TestFlight tester say in their screenshot feedback?
  - id: betaFeedbackScreenshotSubmissions_deleteInstance
    intent: Delete a beta screenshot feedback submission
    question: How do I delete a tester's screenshot feedback?
  phrasing_ops: 2
  slug: ios-betafeedbackscreenshotsubmissions-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The BetaGroups API from iOS — 14 operation(s) for betagroups.
  name: iOS BetaGroups API
  phrasing_intents:
  - id: betaGroups_getCollection
    intent: List TestFlight beta groups
    question: Which TestFlight beta groups do I have across my apps?
  - id: betaGroups_createInstance
    intent: Create a TestFlight beta group
    question: How do I set up a new TestFlight tester group for my app?
  - id: betaGroups_getInstance
    intent: Get a beta group's details
    question: What settings does a specific TestFlight beta group have?
  - id: betaGroups_updateInstance
    intent: Update a beta group's settings
    question: Can I rename a beta group or change its public link limit?
  - id: betaGroups_deleteInstance
    intent: Delete a beta group
    question: How do I remove a TestFlight beta group I no longer use?
  - id: betaGroups_app_getToOneRelationship
    intent: Get the app ID linked to a beta group
    question: Which app ID is a beta group linked to, without the full app record?
  - id: betaGroups_app_getToOneRelated
    intent: Get the app a beta group belongs to
    question: What app does this TestFlight beta group test?
  - id: betaGroups_betaRecruitmentCriteria_getToOneRelationship
    intent: Get the recruitment criteria ID of a beta group
    question: Does a beta group have recruitment criteria attached, by ID only?
  phrasing_ops: 21
  slug: ios-betagroups-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The BetaLicenseAgreements API from iOS — 4 operation(s) for betalicenseagreements.
  name: iOS BetaLicenseAgreements API
  phrasing_intents:
  - id: betaLicenseAgreements_getCollection
    intent: List TestFlight beta license agreements
    question: Where can I see the beta license agreements for my TestFlight apps?
  - id: betaLicenseAgreements_getInstance
    intent: Get a beta license agreement
    question: Can I read the text of one TestFlight license agreement?
  - id: betaLicenseAgreements_updateInstance
    intent: Update a beta license agreement
    question: How do I change the license text testers agree to in TestFlight?
  - id: betaLicenseAgreements_app_getToOneRelationship
    intent: Get the app ID of a beta license agreement
    question: Which app ID does a beta license agreement apply to?
  - id: betaLicenseAgreements_app_getToOneRelated
    intent: Get the app of a beta license agreement
    question: What app is this TestFlight license agreement for?
  phrasing_ops: 5
  slug: ios-betalicenseagreements-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The BetaRecruitmentCriteria API from iOS — 2 operation(s) for betarecruitmentcriteria.
  name: iOS BetaRecruitmentCriteria API
  phrasing_intents:
  - id: betaRecruitmentCriteria_createInstance
    intent: Set beta recruitment criteria
    question: How do I limit which devices can join my public TestFlight link?
  - id: betaRecruitmentCriteria_updateInstance
    intent: Update beta recruitment criteria
    question: How do I change the device requirements for beta testers?
  - id: betaRecruitmentCriteria_deleteInstance
    intent: Remove beta recruitment criteria
    question: How do I remove recruitment criteria from a beta group?
  phrasing_ops: 3
  slug: ios-betarecruitmentcriteria-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The BetaRecruitmentCriterionOptions API from iOS — 1 operation(s) for betarecruitmentcriterionoptions.
  name: iOS BetaRecruitmentCriterionOptions API
  phrasing_intents:
  - id: betaRecruitmentCriterionOptions_getCollection
    intent: List TestFlight tester recruitment criteria options
    question: What device and OS criteria can I use to recruit TestFlight testers from a public link?
  phrasing_ops: 1
  slug: ios-betarecruitmentcriterionoptions-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The BetaTesterInvitations API from iOS — 1 operation(s) for betatesterinvitations.
  name: iOS BetaTesterInvitations API
  phrasing_intents:
  - id: betaTesterInvitations_createInstance
    intent: Send a TestFlight invitation to a tester
    question: A beta tester never got their TestFlight email; can I send them the invitation again?
  phrasing_ops: 1
  slug: ios-betatesterinvitations-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The BuildBetaDetails API from iOS — 4 operation(s) for buildbetadetails.
  name: iOS BuildBetaDetails API
  phrasing_intents:
  - id: buildBetaDetails_getCollection
    intent: List TestFlight beta details for builds
    question: Which of my builds have auto-notify turned on for TestFlight testers?
  - id: buildBetaDetails_getInstance
    intent: Get a build's TestFlight beta details
    question: What is the internal and external TestFlight state of a build's beta detail?
  - id: buildBetaDetails_updateInstance
    intent: Update a build's TestFlight beta settings
    question: How do I stop TestFlight from automatically notifying testers about a build?
  - id: buildBetaDetails_build_getToOneRelationship
    intent: Get the build ID behind a beta detail
    question: Which build ID is a beta detail record attached to?
  - id: buildBetaDetails_build_getToOneRelated
    intent: Get the build behind a beta detail
    question: Which build, with its version and expiration date, does a beta detail describe?
  phrasing_ops: 5
  slug: ios-buildbetadetails-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The BuildBetaNotifications API from iOS — 1 operation(s) for buildbetanotifications.
  name: iOS BuildBetaNotifications API
  phrasing_intents:
  - id: buildBetaNotifications_createInstance
    intent: Notify testers about a build
    question: Can I send TestFlight testers a notification that a new build is ready?
  phrasing_ops: 1
  slug: ios-buildbetanotifications-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The BuildBundles API from iOS — 8 operation(s) for buildbundles.
  name: iOS BuildBundles API
  phrasing_intents:
  - id: buildBundles_appClipDomainCacheStatus_getToOneRelationship
    intent: Get the App Clip domain cache status ID
    question: Which App Clip domain cache status record ID belongs to a build bundle?
  - id: buildBundles_appClipDomainCacheStatus_getToOneRelated
    intent: Check App Clip domain cache status
    question: Has Apple's CDN cached the associated domains for my App Clip yet?
  - id: buildBundles_appClipDomainDebugStatus_getToOneRelationship
    intent: Get the App Clip domain debug status ID
    question: Which App Clip domain debug status record ID is on a build bundle?
  - id: buildBundles_appClipDomainDebugStatus_getToOneRelated
    intent: Check App Clip domain debug status
    question: Why is my App Clip's associated domain failing in developer mode testing?
  - id: buildBundles_betaAppClipInvocations_getToManyRelationship
    intent: List beta App Clip invocation IDs
    question: Which TestFlight App Clip invocation IDs are set on a build bundle?
  - id: buildBundles_betaAppClipInvocations_getToManyRelated
    intent: List beta App Clip invocations for testers
    question: What invocation URLs can TestFlight testers use to launch my App Clip?
  - id: buildBundles_buildBundleFileSizes_getToManyRelationship
    intent: List file size record IDs for a build bundle
    question: Which file size record IDs are attached to a build bundle?
  - id: buildBundles_buildBundleFileSizes_getToManyRelated
    intent: Get download and install sizes per device
    question: How big is my app to download and install on each device model?
  phrasing_ops: 8
  slug: ios-buildbundles-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The Builds API from iOS — 25 operation(s) for builds.
  name: iOS Builds API
  phrasing_intents:
  - id: builds_getCollection
    intent: List builds uploaded to App Store Connect
    question: How do I list all the builds I've uploaded to App Store Connect?
  - id: builds_getInstance
    intent: Get one build's details
    question: What are the details of a single build, like its version and processing state?
  - id: builds_updateInstance
    intent: Update a build's settings
    question: How do I change attributes on a build, such as marking it expired or setting its encryption flag?
  - id: builds_app_getToOneRelationship
    intent: Get the app ID a build belongs to
    question: Which app ID does a given build belong to, without loading the whole app record?
  - id: builds_app_getToOneRelated
    intent: Get the full app record for a build
    question: What app is this build for, with its name and bundle ID?
  - id: builds_appEncryptionDeclaration_getToOneRelationship
    intent: Get the encryption declaration ID for a build
    question: Which export-compliance encryption declaration ID is attached to my build?
  - id: builds_appEncryptionDeclaration_updateToOneRelationship
    intent: Attach an encryption declaration to a build
    question: How do I assign an existing export-compliance encryption declaration to a build?
  - id: builds_appEncryptionDeclaration_getToOneRelated
    intent: Get a build's full encryption declaration
    question: What does the encryption declaration on my build actually say about exempt or proprietary crypto?
  phrasing_ops: 30
  slug: ios-builds-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The BuildUploadFiles API from iOS — 2 operation(s) for builduploadfiles.
  name: iOS BuildUploadFiles API
  phrasing_intents:
  - id: buildUploadFiles_createInstance
    intent: Reserve a build upload file
    question: How do I reserve a file upload for a new build?
  - id: buildUploadFiles_getInstance
    intent: Get a build upload file
    question: Can I check a build upload file by ID?
  - id: buildUploadFiles_updateInstance
    intent: Update a build upload file
    question: Can I update a build upload file after sending its parts?
  phrasing_ops: 3
  slug: ios-builduploadfiles-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The BuildUploads API from iOS — 4 operation(s) for builduploads.
  name: iOS BuildUploads API
  phrasing_intents:
  - id: buildUploads_createInstance
    intent: Start a build upload
    question: How do I start uploading a new build to App Store Connect through the API?
  - id: buildUploads_getInstance
    intent: Check a build upload's status
    question: What is the state of a build upload I started?
  - id: buildUploads_deleteInstance
    intent: Cancel and delete a build upload
    question: How do I cancel a build upload that's stuck or wrong?
  - id: buildUploads_buildUploadFiles_getToManyRelationship
    intent: List file IDs in a build upload
    question: Which file IDs belong to a build upload?
  - id: buildUploads_buildUploadFiles_getToManyRelated
    intent: List files and upload operations in a build upload
    question: What files are part of a build upload, with their sizes and upload instructions?
  phrasing_ops: 5
  slug: ios-builduploads-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The BundleIdCapabilities API from iOS — 2 operation(s) for bundleidcapabilities.
  name: iOS BundleIdCapabilities API
  phrasing_intents:
  - id: bundleIdCapabilities_createInstance
    intent: Enable a capability on a bundle ID
    question: How do I turn on push notifications or iCloud for my app's bundle ID?
  - id: bundleIdCapabilities_updateInstance
    intent: Change a bundle ID capability's settings
    question: Can I change the settings of a capability that's already enabled?
  - id: bundleIdCapabilities_deleteInstance
    intent: Disable a capability on a bundle ID
    question: How do I turn off a capability like Sign in with Apple for a bundle ID?
  phrasing_ops: 3
  slug: ios-bundleidcapabilities-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The BundleIds API from iOS — 8 operation(s) for bundleids.
  name: iOS BundleIds API
  phrasing_intents:
  - id: bundleIds_getCollection
    intent: List bundle IDs
    question: Which bundle IDs are registered on my developer account?
  - id: bundleIds_createInstance
    intent: Register a bundle ID
    question: How do I register a new bundle ID for my app?
  - id: bundleIds_getInstance
    intent: Get a bundle ID
    question: What details are stored for a single bundle ID?
  - id: bundleIds_updateInstance
    intent: Update a bundle ID
    question: How do I rename an existing bundle ID?
  - id: bundleIds_deleteInstance
    intent: Delete a bundle ID
    question: How do I delete a bundle ID I no longer use?
  - id: bundleIds_app_getToOneRelationship
    intent: Get the app ID linked to a bundle ID
    question: How do I find just the app ID that uses a bundle ID?
  - id: bundleIds_app_getToOneRelated
    intent: Get the app for a bundle ID
    question: Which app is using a given bundle ID?
  - id: bundleIds_bundleIdCapabilities_getToManyRelationship
    intent: List capability IDs of a bundle ID
    question: How do I get only the capability IDs enabled on a bundle ID?
  phrasing_ops: 11
  slug: ios-bundleids-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The Certificates API from iOS — 4 operation(s) for certificates.
  name: iOS Certificates API
  phrasing_intents:
  - id: certificates_getCollection
    intent: List signing certificates
    question: Which signing certificates exist on my developer account?
  - id: certificates_createInstance
    intent: Create a signing certificate
    question: How do I create a new signing certificate from a CSR?
  - id: certificates_getInstance
    intent: Get a signing certificate
    question: What details and expiration are stored for one certificate?
  - id: certificates_updateInstance
    intent: Update a signing certificate
    question: How do I change attributes of an existing certificate?
  - id: certificates_deleteInstance
    intent: Revoke a signing certificate
    question: How do I revoke a certificate I no longer need?
  - id: certificates_passTypeId_getToOneRelationship
    intent: Get a certificate's pass type ID linkage
    question: How do I get just the pass type ID linked to a certificate?
  - id: certificates_passTypeId_getToOneRelated
    intent: Get a certificate's pass type
    question: What are the full details of the pass type a certificate signs?
  phrasing_ops: 7
  slug: ios-certificates-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The CiArtifacts API from iOS — 1 operation(s) for ciartifacts.
  name: iOS CiArtifacts API
  phrasing_intents:
  - id: ciArtifacts_getInstance
    intent: Get an Xcode Cloud build artifact
    question: How do I download an archive or log produced by an Xcode Cloud build?
  phrasing_ops: 1
  slug: ios-ciartifacts-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The CiBuildActions API from iOS — 9 operation(s) for cibuildactions.
  name: iOS CiBuildActions API
  phrasing_intents:
  - id: ciBuildActions_getInstance
    intent: Get an Xcode Cloud build action
    question: How do I look up a single Xcode Cloud build action?
  - id: ciBuildActions_artifacts_getToManyRelationship
    intent: List artifact IDs of a build action
    question: Which artifact IDs did an Xcode Cloud build action produce?
  - id: ciBuildActions_artifacts_getToManyRelated
    intent: List artifacts produced by a build action
    question: What artifacts did my Xcode Cloud build action produce, with details?
  - id: ciBuildActions_buildRun_getToOneRelationship
    intent: Get the build run ID of a build action
    question: Which build run ID does this build action belong to?
  - id: ciBuildActions_buildRun_getToOneRelated
    intent: Get the build run a build action belongs to
    question: Which Xcode Cloud build run did this action run in?
  - id: ciBuildActions_issues_getToManyRelationship
    intent: List issue IDs of a build action
    question: Which issue IDs were reported by an Xcode Cloud build action?
  - id: ciBuildActions_issues_getToManyRelated
    intent: List issues reported by a build action
    question: What errors and warnings did my Xcode Cloud build action report?
  - id: ciBuildActions_testResults_getToManyRelationship
    intent: List test result IDs of a build action
    question: Which test result IDs belong to an Xcode Cloud build action?
  phrasing_ops: 9
  slug: ios-cibuildactions-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The CiBuildRuns API from iOS — 6 operation(s) for cibuildruns.
  name: iOS CiBuildRuns API
  phrasing_intents:
  - id: ciBuildRuns_createInstance
    intent: Start an Xcode Cloud build
    question: How do I trigger a new Xcode Cloud build from the API?
  - id: ciBuildRuns_getInstance
    intent: Get an Xcode Cloud build run
    question: What is the status of a particular Xcode Cloud build run?
  - id: ciBuildRuns_actions_getToManyRelationship
    intent: List IDs of a build run's actions
    question: Can I get just the action IDs for an Xcode Cloud build run?
  - id: ciBuildRuns_actions_getToManyRelated
    intent: List the actions in a build run
    question: What steps (build, test, analyze, archive) ran in my Xcode Cloud build?
  - id: ciBuildRuns_builds_getToManyRelationship
    intent: List IDs of builds from a build run
    question: Can I fetch only the build IDs a CI run produced?
  - id: ciBuildRuns_builds_getToManyRelated
    intent: List builds produced by a build run
    question: What app builds did an Xcode Cloud run upload?
  phrasing_ops: 6
  slug: ios-cibuildruns-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The CiIssues API from iOS — 1 operation(s) for ciissues.
  name: iOS CiIssues API
  phrasing_intents:
  - id: ciIssues_getInstance
    intent: Get an Xcode Cloud build issue
    question: What error or warning did an Xcode Cloud build action report?
  phrasing_ops: 1
  slug: ios-ciissues-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The CiMacOsVersions API from iOS — 4 operation(s) for cimacosversions.
  name: iOS CiMacOsVersions API
  phrasing_intents:
  - id: ciMacOsVersions_getCollection
    intent: List macOS versions available in Xcode Cloud
    question: Which macOS versions can my Xcode Cloud builds run on?
  - id: ciMacOsVersions_getInstance
    intent: Get an Xcode Cloud macOS version
    question: What are the details of one Xcode Cloud macOS version?
  - id: ciMacOsVersions_xcodeVersions_getToManyRelationship
    intent: List Xcode version IDs for a macOS version
    question: Which Xcode version IDs are supported on a given Xcode Cloud macOS?
  - id: ciMacOsVersions_xcodeVersions_getToManyRelated
    intent: List Xcode versions for a macOS version
    question: What Xcode releases can I use with this Xcode Cloud macOS version?
  phrasing_ops: 4
  slug: ios-cimacosversions-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The CiProducts API from iOS — 12 operation(s) for ciproducts.
  name: iOS CiProducts API
  phrasing_intents:
  - id: ciProducts_getCollection
    intent: List Xcode Cloud products
    question: Which of my apps and frameworks are set up in Xcode Cloud?
  - id: ciProducts_getInstance
    intent: Get an Xcode Cloud product
    question: Can I look up one Xcode Cloud product by its ID?
  - id: ciProducts_deleteInstance
    intent: Remove a product from Xcode Cloud
    question: How do I stop using Xcode Cloud for an app and delete its product?
  - id: ciProducts_additionalRepositories_getToManyRelationship
    intent: List IDs of a product's additional repos
    question: Can I get just the IDs of the extra repositories an Xcode Cloud product uses?
  - id: ciProducts_additionalRepositories_getToManyRelated
    intent: List a product's additional repositories
    question: What secondary repositories does my Xcode Cloud product pull from?
  - id: ciProducts_app_getToOneRelationship
    intent: Get the app ID behind an Xcode Cloud product
    question: Which app ID is an Xcode Cloud product tied to?
  - id: ciProducts_app_getToOneRelated
    intent: Get the app for an Xcode Cloud product
    question: What app does this Xcode Cloud product build?
  - id: ciProducts_buildRuns_getToManyRelationship
    intent: List IDs of a product's build runs
    question: Can I fetch only the build run IDs for an Xcode Cloud product?
  phrasing_ops: 13
  slug: ios-ciproducts-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The CiTestResults API from iOS — 1 operation(s) for citestresults.
  name: iOS CiTestResults API
  phrasing_intents:
  - id: ciTestResults_getInstance
    intent: Get an Xcode Cloud test result
    question: Can I look up one Xcode Cloud test result by ID?
  phrasing_ops: 1
  slug: ios-citestresults-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The CiWorkflows API from iOS — 6 operation(s) for ciworkflows.
  name: iOS CiWorkflows API
  phrasing_intents:
  - id: ciWorkflows_createInstance
    intent: Create an Xcode Cloud workflow
    question: How do I create a new Xcode Cloud workflow for my product?
  - id: ciWorkflows_getInstance
    intent: Get an Xcode Cloud workflow
    question: What triggers and actions are configured on one of my Xcode Cloud workflows?
  - id: ciWorkflows_updateInstance
    intent: Update an Xcode Cloud workflow
    question: How can I disable an Xcode Cloud workflow without deleting it?
  - id: ciWorkflows_deleteInstance
    intent: Delete an Xcode Cloud workflow
    question: Can I delete an Xcode Cloud workflow I no longer use?
  - id: ciWorkflows_buildRuns_getToManyRelationship
    intent: List build run IDs for a workflow
    question: Which build run IDs has my Xcode Cloud workflow produced?
  - id: ciWorkflows_buildRuns_getToManyRelated
    intent: List a workflow's build runs
    question: What were the results of the recent Xcode Cloud runs for this workflow?
  - id: ciWorkflows_repository_getToOneRelationship
    intent: Get the repository ID for a workflow
    question: Which repository ID is my Xcode Cloud workflow connected to?
  - id: ciWorkflows_repository_getToOneRelated
    intent: Get the repository a workflow builds
    question: What Git repository and URL does this Xcode Cloud workflow build from?
  phrasing_ops: 8
  slug: ios-ciworkflows-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The CiXcodeVersions API from iOS — 4 operation(s) for cixcodeversions.
  name: iOS CiXcodeVersions API
  phrasing_intents:
  - id: ciXcodeVersions_getCollection
    intent: List Xcode versions available in Xcode Cloud
    question: Which Xcode versions can my Xcode Cloud workflows build with?
  - id: ciXcodeVersions_getInstance
    intent: Get an Xcode Cloud Xcode version
    question: What test destinations does a specific Xcode version support in Xcode Cloud?
  - id: ciXcodeVersions_macOsVersions_getToManyRelationship
    intent: List macOS version IDs for an Xcode version
    question: Which macOS version IDs pair with an Xcode version in Xcode Cloud?
  - id: ciXcodeVersions_macOsVersions_getToManyRelated
    intent: List macOS versions compatible with an Xcode version
    question: Which macOS versions can run a particular Xcode version in Xcode Cloud?
  phrasing_ops: 4
  slug: ios-cixcodeversions-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The CustomerReviewResponses API from iOS — 2 operation(s) for customerreviewresponses.
  name: iOS CustomerReviewResponses API
  phrasing_intents:
  - id: customerReviewResponses_createInstance
    intent: Reply to a customer review
    question: How do I respond publicly to a customer's App Store review?
  - id: customerReviewResponses_getInstance
    intent: Get a customer review response
    question: Has my reply to a review been published yet?
  - id: customerReviewResponses_deleteInstance
    intent: Delete a customer review response
    question: Can I take down a reply I posted to a customer review?
  phrasing_ops: 3
  slug: ios-customerreviewresponses-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The CustomerReviews API from iOS — 3 operation(s) for customerreviews.
  name: iOS CustomerReviews API
  phrasing_intents:
  - id: customerReviews_getInstance
    intent: Get a customer review
    question: Can I read a single App Store customer review by ID?
  - id: customerReviews_response_getToOneRelationship
    intent: Get the response ID for a review
    question: Has a customer review been responded to, and what is the response ID?
  - id: customerReviews_response_getToOneRelated
    intent: Get my response to a customer review
    question: What did we reply to this customer review?
  phrasing_ops: 3
  slug: ios-customerreviews-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The Devices API from iOS — 2 operation(s) for devices.
  name: iOS Devices API
  phrasing_intents:
  - id: devices_getCollection
    intent: List registered devices
    question: Which test devices are registered on my developer account?
  - id: devices_createInstance
    intent: Register a device
    question: How do I register a new test device for development?
  - id: devices_getInstance
    intent: Get a registered device
    question: What details are stored for one registered device?
  - id: devices_updateInstance
    intent: Rename or disable a device
    question: How do I rename a registered device or disable it?
  phrasing_ops: 4
  slug: ios-devices-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The DiagnosticSignatures API from iOS — 1 operation(s) for diagnosticsignatures.
  name: iOS DiagnosticSignatures API
  phrasing_intents:
  - id: diagnosticSignatures_logs_getToManyRelated
    intent: Get logs for a diagnostic signature
    question: Where can I see the call stacks behind a hang or disk-write diagnostic?
  phrasing_ops: 1
  slug: ios-diagnosticsignatures-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The EndAppAvailabilityPreOrders API from iOS — 1 operation(s) for endappavailabilitypreorders.
  name: iOS EndAppAvailabilityPreOrders API
  phrasing_intents:
  - id: endAppAvailabilityPreOrders_createInstance
    intent: End pre-orders for an app
    question: Is there a way to end pre-orders for my app in some territories?
  phrasing_ops: 1
  slug: ios-endappavailabilitypreorders-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The EndUserLicenseAgreements API from iOS — 4 operation(s) for enduserlicenseagreements.
  name: iOS EndUserLicenseAgreements API
  phrasing_intents:
  - id: endUserLicenseAgreements_createInstance
    intent: Add a custom EULA to an app
    question: How do I replace Apple's standard license agreement with my own EULA?
  - id: endUserLicenseAgreements_getInstance
    intent: Get a custom EULA
    question: What license agreement text does my app currently use?
  - id: endUserLicenseAgreements_updateInstance
    intent: Update a custom EULA
    question: Can I edit the wording of my custom license agreement?
  - id: endUserLicenseAgreements_deleteInstance
    intent: Delete a custom EULA
    question: Can I drop my custom license agreement and go back to the standard one?
  - id: endUserLicenseAgreements_territories_getToManyRelationship
    intent: List territory IDs covered by a custom EULA
    question: Which territory IDs does a custom license agreement apply to?
  - id: endUserLicenseAgreements_territories_getToManyRelated
    intent: List territories covered by a custom EULA
    question: In which countries do customers see my custom license agreement?
  phrasing_ops: 6
  slug: ios-enduserlicenseagreements-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The FinanceReports API from iOS — 1 operation(s) for financereports.
  name: iOS FinanceReports API
  phrasing_intents:
  - id: financeReports_getCollection
    intent: Download a financial report
    question: How do I download my monthly App Store financial report?
  phrasing_ops: 1
  slug: ios-financereports-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The GameCenterAchievementImages API from iOS — 4 operation(s) for gamecenterachievementimages.
  name: iOS GameCenterAchievementImages API
  phrasing_intents:
  - id: gameCenterAchievementImages_createInstance
    intent: Reserve a Game Center achievement image (v1)
    question: How do I start uploading an achievement image with the original v1 endpoint?
  - id: gameCenterAchievementImages_getInstance
    intent: Get a Game Center achievement image (v1)
    question: Where can I check a v1 achievement image's upload state?
  - id: gameCenterAchievementImages_updateInstance
    intent: Commit a Game Center achievement image upload (v1)
    question: How do I mark a v1 achievement image upload as complete?
  - id: gameCenterAchievementImages_deleteInstance
    intent: Delete a Game Center achievement image (v1)
    question: Can I delete achievement artwork that was uploaded through the v1 API?
  - id: gameCenterAchievementImagesV2_createInstance
    intent: Reserve a Game Center achievement image (v2)
    question: How do I upload achievement artwork using the newer v2 endpoint?
  - id: gameCenterAchievementImagesV2_getInstance
    intent: Get a Game Center achievement image (v2)
    question: What is the processing state of an achievement image created with v2?
  - id: gameCenterAchievementImagesV2_updateInstance
    intent: Commit a Game Center achievement image upload (v2)
    question: How do I finish a v2 achievement image upload once the parts are sent?
  - id: gameCenterAchievementImagesV2_deleteInstance
    intent: Delete a Game Center achievement image (v2)
    question: Can I delete achievement artwork created with the v2 endpoint?
  phrasing_ops: 8
  slug: ios-gamecenterachievementimages-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The GameCenterAchievementLocalizations API from iOS — 10 operation(s) for gamecenterachievementlocalizations.
  name: iOS GameCenterAchievementLocalizations API
  phrasing_intents:
  - id: gameCenterAchievementLocalizationsV2_createInstance
    intent: Add a language to a Game Center achievement (V2)
    question: How do I add a French name and description to a Game Center achievement using the V2 localizations endpoint?
  - id: gameCenterAchievementLocalizationsV2_getInstance
    intent: Get a Game Center achievement localization (V2)
    question: What localized title and descriptions does a V2 achievement localization hold?
  - id: gameCenterAchievementLocalizationsV2_updateInstance
    intent: Update a Game Center achievement localization (V2)
    question: Can I fix a typo in an achievement's localized description using the V2 resource?
  - id: gameCenterAchievementLocalizationsV2_deleteInstance
    intent: Delete a Game Center achievement localization (V2)
    question: Can I drop one language from an achievement using the V2 localizations resource?
  - id: gameCenterAchievementLocalizations_createInstance
    intent: Add a language to a Game Center achievement (v1)
    question: How do I localize a Game Center achievement with the original v1 localizations endpoint?
  - id: gameCenterAchievementLocalizations_getInstance
    intent: Get a Game Center achievement localization (v1)
    question: What does a legacy v1 achievement localization record contain?
  - id: gameCenterAchievementLocalizations_updateInstance
    intent: Update a Game Center achievement localization (v1)
    question: Can I edit achievement text through the legacy v1 localization resource?
  - id: gameCenterAchievementLocalizations_deleteInstance
    intent: Delete a Game Center achievement localization (v1)
    question: Can I remove an achievement language using the original v1 endpoint?
  phrasing_ops: 14
  slug: ios-gamecenterachievementlocalizations-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The GameCenterAchievementReleases API from iOS — 2 operation(s) for gamecenterachievementreleases.
  name: iOS GameCenterAchievementReleases API
  phrasing_intents:
  - id: gameCenterAchievementReleases_createInstance
    intent: Release a Game Center achievement to live
    question: How do I push a new Game Center achievement live to players?
  - id: gameCenterAchievementReleases_getInstance
    intent: Get a Game Center achievement release
    question: Has a given achievement release gone live yet?
  - id: gameCenterAchievementReleases_deleteInstance
    intent: Delete a Game Center achievement release
    question: Can I pull an achievement back out of a pending release?
  phrasing_ops: 3
  slug: ios-gamecenterachievementreleases-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The GameCenterAchievements API from iOS — 14 operation(s) for gamecenterachievements.
  name: iOS GameCenterAchievements API
  phrasing_intents:
  - id: gameCenterAchievementsV2_createInstance
    intent: Create an achievement (v2)
    question: How do I create a Game Center achievement with the v2 API?
  - id: gameCenterAchievementsV2_getInstance
    intent: Get an achievement (v2)
    question: What details does the v2 API return for one achievement?
  - id: gameCenterAchievementsV2_updateInstance
    intent: Update an achievement (v2)
    question: How do I edit an existing achievement through v2?
  - id: gameCenterAchievementsV2_deleteInstance
    intent: Delete an achievement (v2)
    question: How do I delete an achievement using the v2 API?
  - id: gameCenterAchievements_createInstance
    intent: Create an achievement (v1)
    question: How do I create an achievement with the legacy v1 Game Center API?
  - id: gameCenterAchievements_getInstance
    intent: Get an achievement (v1)
    question: What does the legacy v1 endpoint return for one achievement?
  - id: gameCenterAchievements_updateInstance
    intent: Update an achievement (v1)
    question: How do I edit an achievement through the v1 API?
  - id: gameCenterAchievements_deleteInstance
    intent: Delete an achievement (v1)
    question: How do I delete an achievement using the legacy v1 API?
  phrasing_ops: 19
  slug: ios-gamecenterachievements-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The GameCenterAchievementVersions API from iOS — 4 operation(s) for gamecenterachievementversions.
  name: iOS GameCenterAchievementVersions API
  phrasing_intents:
  - id: gameCenterAchievementVersionsV2_createInstance
    intent: Create a Game Center achievement version
    question: How do I create a new version of a Game Center achievement?
  - id: gameCenterAchievementVersionsV2_getInstance
    intent: Get a Game Center achievement version
    question: Can I look up a Game Center achievement version by ID?
  - id: gameCenterAchievementVersionsV2_localizations_getToManyRelationship
    intent: List localization IDs of an achievement version
    question: Which localization IDs belong to a Game Center achievement version?
  - id: gameCenterAchievementVersionsV2_localizations_getToManyRelated
    intent: List localizations of an achievement version
    question: Which languages is my achievement version localized into?
  phrasing_ops: 4
  slug: ios-gamecenterachievementversions-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The GameCenterActivities API from iOS — 8 operation(s) for gamecenteractivities.
  name: iOS GameCenterActivities API
  phrasing_intents:
  - id: gameCenterActivities_createInstance
    intent: Create a Game Center activity
    question: How do I set up a new Game Center activity for my game?
  - id: gameCenterActivities_getInstance
    intent: Get a Game Center activity
    question: What are the settings of one Game Center activity?
  - id: gameCenterActivities_updateInstance
    intent: Update a Game Center activity
    question: How do I change the settings on an existing Game Center activity?
  - id: gameCenterActivities_deleteInstance
    intent: Delete a Game Center activity
    question: How do I permanently remove a Game Center activity I no longer use?
  - id: gameCenterActivities_achievements_createToManyRelationship
    intent: Link achievements to an activity
    question: How do I attach existing achievements to a Game Center activity?
  - id: gameCenterActivities_achievements_deleteToManyRelationship
    intent: Unlink achievements from an activity
    question: How do I detach achievements from a Game Center activity without deleting them?
  - id: gameCenterActivities_achievementsV2_createToManyRelationship
    intent: Link V2 achievements to an activity
    question: How do I attach the newer V2 achievements to a Game Center activity?
  - id: gameCenterActivities_achievementsV2_deleteToManyRelationship
    intent: Unlink V2 achievements from an activity
    question: How do I detach V2 achievements from a Game Center activity?
  phrasing_ops: 14
  slug: ios-gamecenteractivities-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The GameCenterActivityImages API from iOS — 2 operation(s) for gamecenteractivityimages.
  name: iOS GameCenterActivityImages API
  phrasing_intents:
  - id: gameCenterActivityImages_createInstance
    intent: Reserve a Game Center activity image upload
    question: How do I upload artwork for a Game Center activity?
  - id: gameCenterActivityImages_getInstance
    intent: Get a Game Center activity image
    question: Has my activity image finished processing?
  - id: gameCenterActivityImages_updateInstance
    intent: Commit or update an activity image upload
    question: How do I confirm an activity image upload is complete?
  - id: gameCenterActivityImages_deleteInstance
    intent: Delete a Game Center activity image
    question: How do I remove an image from a Game Center activity?
  phrasing_ops: 4
  slug: ios-gamecenteractivityimages-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The GameCenterActivityLocalizations API from iOS — 4 operation(s) for gamecenteractivitylocalizations.
  name: iOS GameCenterActivityLocalizations API
  phrasing_intents:
  - id: gameCenterActivityLocalizations_createInstance
    intent: Add a language to a Game Center activity
    question: How do I translate a Game Center activity's name and description into another language?
  - id: gameCenterActivityLocalizations_getInstance
    intent: Get a Game Center activity localization
    question: What name and description did I set for an activity in a particular language?
  - id: gameCenterActivityLocalizations_updateInstance
    intent: Update a Game Center activity localization
    question: Where do I fix a typo in a translated Game Center activity description?
  - id: gameCenterActivityLocalizations_deleteInstance
    intent: Delete a Game Center activity localization
    question: How do I remove a language from a Game Center activity?
  - id: gameCenterActivityLocalizations_image_getToOneRelationship
    intent: Get the image ID of an activity localization
    question: Which image ID is attached to a Game Center activity localization?
  - id: gameCenterActivityLocalizations_image_getToOneRelated
    intent: Get the artwork for an activity localization
    question: What artwork is shown for a Game Center activity in a given language, and has it finished uploading?
  phrasing_ops: 6
  slug: ios-gamecenteractivitylocalizations-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The GameCenterActivityVersionReleases API from iOS — 2 operation(s) for gamecenteractivityversionreleases.
  name: iOS GameCenterActivityVersionReleases API
  phrasing_intents:
  - id: gameCenterActivityVersionReleases_createInstance
    intent: Release a Game Center activity version
    question: How do I make a new version of a Game Center activity live?
  - id: gameCenterActivityVersionReleases_getInstance
    intent: Get a Game Center activity version release
    question: Which activity version does a given release record point to?
  - id: gameCenterActivityVersionReleases_deleteInstance
    intent: Delete a Game Center activity version release
    question: How do I delete a release record for a Game Center activity version?
  phrasing_ops: 3
  slug: ios-gamecenteractivityversionreleases-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The GameCenterActivityVersions API from iOS — 6 operation(s) for gamecenteractivityversions.
  name: iOS GameCenterActivityVersions API
  phrasing_intents:
  - id: gameCenterActivityVersions_createInstance
    intent: Create a Game Center activity version
    question: How do I start a new version of a Game Center activity?
  - id: gameCenterActivityVersions_getInstance
    intent: Get a Game Center activity version
    question: What state is a given Game Center activity version in?
  - id: gameCenterActivityVersions_updateInstance
    intent: Update a Game Center activity version
    question: Can I change the fallback URL on an activity version?
  - id: gameCenterActivityVersions_defaultImage_getToOneRelationship
    intent: Get the default image ID of an activity version
    question: Which default image ID is attached to my activity version?
  - id: gameCenterActivityVersions_defaultImage_getToOneRelated
    intent: Get the default image of an activity version
    question: What default image will players see for this Game Center activity?
  - id: gameCenterActivityVersions_localizations_getToManyRelationship
    intent: List localization IDs for an activity version
    question: Which localization IDs exist on my activity version?
  - id: gameCenterActivityVersions_localizations_getToManyRelated
    intent: List an activity version's localizations
    question: What languages and names has my Game Center activity version been translated into?
  phrasing_ops: 7
  slug: ios-gamecenteractivityversions-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The GameCenterAppVersions API from iOS — 6 operation(s) for gamecenterappversions.
  name: iOS GameCenterAppVersions API
  phrasing_intents:
  - id: gameCenterAppVersions_createInstance
    intent: Enable Game Center for an app version
    question: How do I turn on Game Center for a new version of my game?
  - id: gameCenterAppVersions_getInstance
    intent: Get a Game Center app version
    question: Is Game Center enabled on a given Game Center app version record?
  - id: gameCenterAppVersions_updateInstance
    intent: Update a Game Center app version
    question: Can I switch Game Center off for an existing app version?
  - id: gameCenterAppVersions_appStoreVersion_getToOneRelationship
    intent: Get the App Store version ID for a Game Center version
    question: Which App Store version ID is a Game Center app version linked to?
  - id: gameCenterAppVersions_appStoreVersion_getToOneRelated
    intent: Get the App Store version for a Game Center version
    question: Which App Store release, with its version string and state, does this Game Center app version belong to?
  - id: gameCenterAppVersions_compatibilityVersions_getToManyRelationship
    intent: List compatible Game Center version IDs
    question: Which compatibility version IDs are linked to a Game Center app version?
  - id: gameCenterAppVersions_compatibilityVersions_createToManyRelationship
    intent: Mark Game Center versions as compatible
    question: How do I let players on an older version of my game share leaderboards with the new one?
  - id: gameCenterAppVersions_compatibilityVersions_deleteToManyRelationship
    intent: Remove Game Center version compatibility
    question: Can I stop an old game version from sharing Game Center data with the current one?
  phrasing_ops: 9
  slug: ios-gamecenterappversions-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The GameCenterChallengeImages API from iOS — 2 operation(s) for gamecenterchallengeimages.
  name: iOS GameCenterChallengeImages API
  phrasing_intents:
  - id: gameCenterChallengeImages_createInstance
    intent: Reserve a Game Center challenge image
    question: Can I add artwork to a Game Center challenge?
  - id: gameCenterChallengeImages_getInstance
    intent: Get a Game Center challenge image
    question: Has my Game Center challenge image finished processing?
  - id: gameCenterChallengeImages_updateInstance
    intent: Commit a Game Center challenge image upload
    question: How do I confirm a challenge image upload is complete?
  - id: gameCenterChallengeImages_deleteInstance
    intent: Delete a Game Center challenge image
    question: Can I remove the artwork from a Game Center challenge?
  phrasing_ops: 4
  slug: ios-gamecenterchallengeimages-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The GameCenterChallengeLocalizations API from iOS — 4 operation(s) for gamecenterchallengelocalizations.
  name: iOS GameCenterChallengeLocalizations API
  phrasing_intents:
  - id: gameCenterChallengeLocalizations_createInstance
    intent: Localize a Game Center challenge
    question: How do I translate a Game Center challenge's name into another language?
  - id: gameCenterChallengeLocalizations_getInstance
    intent: Get a challenge localization
    question: What name and description does one challenge localization show?
  - id: gameCenterChallengeLocalizations_updateInstance
    intent: Update a challenge localization
    question: How can I fix the wording of a translated Game Center challenge?
  - id: gameCenterChallengeLocalizations_deleteInstance
    intent: Delete a challenge localization
    question: Can I remove a language from a Game Center challenge?
  - id: gameCenterChallengeLocalizations_image_getToOneRelationship
    intent: Get the image ID of a challenge localization
    question: Which image ID is attached to a challenge localization?
  - id: gameCenterChallengeLocalizations_image_getToOneRelated
    intent: Get the image of a challenge localization
    question: What image do players see for a challenge in a given language?
  phrasing_ops: 6
  slug: ios-gamecenterchallengelocalizations-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The GameCenterChallenges API from iOS — 6 operation(s) for gamecenterchallenges.
  name: iOS GameCenterChallenges API
  phrasing_intents:
  - id: gameCenterChallenges_createInstance
    intent: Create a Game Center challenge
    question: How do I add a challenge players can send to friends in my game?
  - id: gameCenterChallenges_getInstance
    intent: Get a Game Center challenge
    question: What are the settings of one of my Game Center challenges?
  - id: gameCenterChallenges_updateInstance
    intent: Update a Game Center challenge
    question: Can I rename a challenge or change whether it's repeatable?
  - id: gameCenterChallenges_deleteInstance
    intent: Delete a Game Center challenge
    question: How do I remove a challenge from my game?
  - id: gameCenterChallenges_leaderboard_updateToOneRelationship
    intent: Link a challenge to a v1 leaderboard
    question: How do I point a challenge at a v1 leaderboard?
  - id: gameCenterChallenges_leaderboardV2_updateToOneRelationship
    intent: Link a challenge to a v2 leaderboard
    question: How do I attach a challenge to a leaderboard created with the v2 API?
  - id: gameCenterChallenges_versions_getToManyRelationship
    intent: List version IDs of a challenge
    question: Can I get just the version IDs for a Game Center challenge?
  - id: gameCenterChallenges_versions_getToManyRelated
    intent: List versions of a challenge
    question: What versions of a challenge exist and what state are they in?
  phrasing_ops: 8
  slug: ios-gamecenterchallenges-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The GameCenterChallengeVersionReleases API from iOS — 2 operation(s) for gamecenterchallengeversionreleases.
  name: iOS GameCenterChallengeVersionReleases API
  phrasing_intents:
  - id: gameCenterChallengeVersionReleases_createInstance
    intent: Release a Game Center challenge version
    question: How do I release a new version of a Game Center challenge to players?
  - id: gameCenterChallengeVersionReleases_getInstance
    intent: Get a challenge version release
    question: Which challenge version did a given release make live?
  - id: gameCenterChallengeVersionReleases_deleteInstance
    intent: Delete a challenge version release
    question: Can I undo a Game Center challenge version release?
  phrasing_ops: 3
  slug: ios-gamecenterchallengeversionreleases-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The GameCenterChallengeVersions API from iOS — 6 operation(s) for gamecenterchallengeversions.
  name: iOS GameCenterChallengeVersions API
  phrasing_intents:
  - id: gameCenterChallengeVersions_createInstance
    intent: Create a Game Center challenge version
    question: How do I start a new version of a Game Center challenge?
  - id: gameCenterChallengeVersions_getInstance
    intent: Get a Game Center challenge version
    question: What state is a particular Game Center challenge version in?
  - id: gameCenterChallengeVersions_defaultImage_getToOneRelationship
    intent: Get the default image ID of a challenge version
    question: Which image ID is the default artwork for a challenge version?
  - id: gameCenterChallengeVersions_defaultImage_getToOneRelated
    intent: Get a challenge version's default artwork
    question: What does the default artwork for my Game Center challenge look like?
  - id: gameCenterChallengeVersions_localizations_getToManyRelationship
    intent: List localization IDs of a challenge version
    question: Which localization IDs belong to a challenge version?
  - id: gameCenterChallengeVersions_localizations_getToManyRelated
    intent: List a challenge version's localized text
    question: What names and descriptions does my challenge show players in each language?
  phrasing_ops: 6
  slug: ios-gamecenterchallengeversions-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The GameCenterDetails API from iOS — 35 operation(s) for gamecenterdetails.
  name: iOS GameCenterDetails API
  phrasing_intents:
  - id: gameCenterDetails_createInstance
    intent: Set up Game Center for an app
    question: How do I turn on Game Center for an app through App Store Connect?
  - id: gameCenterDetails_getInstance
    intent: Get an app's Game Center configuration
    question: Can I look up a single Game Center detail record by its ID?
  - id: gameCenterDetails_updateInstance
    intent: Update an app's Game Center configuration
    question: Can I change settings on an existing Game Center detail record?
  - id: gameCenterDetails_achievementReleases_getToManyRelationship
    intent: List IDs of a Game Center's achievement releases
    question: Is there a lightweight way to get just the IDs of achievement releases linked to a Game Center detail?
  - id: gameCenterDetails_achievementReleases_getToManyRelated
    intent: List a Game Center's achievement releases
    question: Which achievement releases are live for my game's Game Center?
  - id: gameCenterDetails_activityReleases_getToManyRelationship
    intent: List IDs of a Game Center's activity releases
    question: How can I get only the activity release IDs tied to a Game Center detail?
  - id: gameCenterDetails_activityReleases_getToManyRelated
    intent: List a Game Center's activity releases
    question: What activity releases has my game published through Game Center?
  - id: gameCenterDetails_challengeReleases_getToManyRelationship
    intent: List IDs of a Game Center's challenge releases
    question: Can I fetch only the challenge release IDs linked to a Game Center detail?
  phrasing_ops: 42
  slug: ios-gamecenterdetails-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The GameCenterEnabledVersions API from iOS — 2 operation(s) for gamecenterenabledversions.
  name: iOS GameCenterEnabledVersions API
  phrasing_intents:
  - id: gameCenterEnabledVersions_compatibleVersions_getToManyRelationship
    intent: List compatible version IDs
    question: Which compatible version IDs are linked to my Game Center enabled version?
  - id: gameCenterEnabledVersions_compatibleVersions_createToManyRelationship
    intent: Add compatible Game Center versions
    question: How do I mark another app version as Game Center compatible with this one?
  - id: gameCenterEnabledVersions_compatibleVersions_replaceToManyRelationship
    intent: Replace compatible Game Center versions
    question: How do I overwrite the whole compatibility list for a Game Center enabled version?
  - id: gameCenterEnabledVersions_compatibleVersions_deleteToManyRelationship
    intent: Remove compatible Game Center versions
    question: Can I remove a single version from a Game Center compatibility list?
  - id: gameCenterEnabledVersions_compatibleVersions_getToManyRelated
    intent: List compatible Game Center versions
    question: What app versions can play together with this Game Center enabled version?
  phrasing_ops: 5
  slug: ios-gamecenterenabledversions-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The GameCenterGroups API from iOS — 20 operation(s) for gamecentergroups.
  name: iOS GameCenterGroups API
  phrasing_intents:
  - id: gameCenterGroups_getCollection
    intent: List Game Center groups
    question: Which Game Center groups do I have set up in App Store Connect?
  - id: gameCenterGroups_createInstance
    intent: Create a Game Center group
    question: How do I create a Game Center group so several games can share leaderboards and achievements?
  - id: gameCenterGroups_getInstance
    intent: Get a Game Center group
    question: What does a single Game Center group look like, including its reference name?
  - id: gameCenterGroups_updateInstance
    intent: Update a Game Center group
    question: Can I rename a Game Center group after creating it?
  - id: gameCenterGroups_deleteInstance
    intent: Delete a Game Center group
    question: Can I delete a Game Center group I no longer need?
  - id: gameCenterGroups_gameCenterAchievements_getToManyRelationship
    intent: List achievement IDs linked to a group
    question: Which achievement IDs are linked to my Game Center group?
  - id: gameCenterGroups_gameCenterAchievements_replaceToManyRelationship
    intent: Replace a group's achievements
    question: How do I reorder or swap the achievements assigned to a Game Center group?
  - id: gameCenterGroups_gameCenterAchievements_getToManyRelated
    intent: List a group's achievements
    question: What achievements are in my Game Center group, with their names and details?
  phrasing_ops: 29
  slug: ios-gamecentergroups-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The GameCenterLeaderboardEntrySubmissions API from iOS — 1 operation(s) for gamecenterleaderboardentrysubmissions.
  name: iOS GameCenterLeaderboardEntrySubmissions API
  phrasing_intents:
  - id: gameCenterLeaderboardEntrySubmissions_createInstance
    intent: Submit a score to a Game Center leaderboard
    question: How do I post a player's score to a Game Center leaderboard from my server?
  phrasing_ops: 1
  slug: ios-gamecenterleaderboardentrysubmissions-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The GameCenterLeaderboardImages API from iOS — 4 operation(s) for gamecenterleaderboardimages.
  name: iOS GameCenterLeaderboardImages API
  phrasing_intents:
  - id: gameCenterLeaderboardImages_createInstance
    intent: Reserve a leaderboard image (v1)
    question: How do I upload artwork for a leaderboard with the legacy v1 API?
  - id: gameCenterLeaderboardImages_getInstance
    intent: Get a leaderboard image (v1)
    question: What is the upload state of a leaderboard image on v1?
  - id: gameCenterLeaderboardImages_updateInstance
    intent: Commit a leaderboard image (v1)
    question: How do I mark a leaderboard image upload as complete on v1?
  - id: gameCenterLeaderboardImages_deleteInstance
    intent: Delete a leaderboard image (v1)
    question: How do I remove a leaderboard image using v1?
  - id: gameCenterLeaderboardImagesV2_createInstance
    intent: Reserve a leaderboard image (v2)
    question: How do I upload leaderboard artwork with the newer v2 API?
  - id: gameCenterLeaderboardImagesV2_getInstance
    intent: Get a leaderboard image (v2)
    question: What is the upload state of a leaderboard image on v2?
  - id: gameCenterLeaderboardImagesV2_updateInstance
    intent: Commit a leaderboard image (v2)
    question: How do I mark a leaderboard image upload as complete on v2?
  - id: gameCenterLeaderboardImagesV2_deleteInstance
    intent: Delete a leaderboard image (v2)
    question: How do I remove a leaderboard image using v2?
  phrasing_ops: 8
  slug: ios-gamecenterleaderboardimages-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The GameCenterLeaderboardLocalizations API from iOS — 8 operation(s) for gamecenterleaderboardlocalizations.
  name: iOS GameCenterLeaderboardLocalizations API
  phrasing_intents:
  - id: gameCenterLeaderboardLocalizations_createInstance
    intent: Add a leaderboard localization (v1)
    question: How do I add a translated name for a leaderboard using the original v1 endpoint?
  - id: gameCenterLeaderboardLocalizations_getInstance
    intent: Get a leaderboard localization (v1)
    question: What does a v1 leaderboard localization contain for one language?
  - id: gameCenterLeaderboardLocalizations_updateInstance
    intent: Update a leaderboard localization (v1)
    question: How do I fix the translated name on a v1 leaderboard localization?
  - id: gameCenterLeaderboardLocalizations_deleteInstance
    intent: Delete a leaderboard localization (v1)
    question: How do I remove a language from a leaderboard via the v1 localization endpoint?
  - id: gameCenterLeaderboardLocalizationsV2_createInstance
    intent: Add a leaderboard localization (v2)
    question: What's the V2 way to add a translated leaderboard name?
  - id: gameCenterLeaderboardLocalizationsV2_getInstance
    intent: Get a leaderboard localization (v2)
    question: What does a V2 leaderboard localization look like for one language?
  - id: gameCenterLeaderboardLocalizationsV2_updateInstance
    intent: Update a leaderboard localization (v2)
    question: Which v2 call edits a translated leaderboard name or description?
  - id: gameCenterLeaderboardLocalizationsV2_deleteInstance
    intent: Delete a leaderboard localization (v2)
    question: Which v2 call removes a language from a leaderboard?
  phrasing_ops: 12
  slug: ios-gamecenterleaderboardlocalizations-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The GameCenterLeaderboardReleases API from iOS — 2 operation(s) for gamecenterleaderboardreleases.
  name: iOS GameCenterLeaderboardReleases API
  phrasing_intents:
  - id: gameCenterLeaderboardReleases_createInstance
    intent: Release a Game Center leaderboard to live
    question: How do I push a Game Center leaderboard live in my production game?
  - id: gameCenterLeaderboardReleases_getInstance
    intent: Get a Game Center leaderboard release
    question: Is my Game Center leaderboard live for players?
  - id: gameCenterLeaderboardReleases_deleteInstance
    intent: Pull a leaderboard release from live
    question: Can I take a Game Center leaderboard back out of the live game?
  phrasing_ops: 3
  slug: ios-gamecenterleaderboardreleases-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The GameCenterLeaderboards API from iOS — 16 operation(s) for gamecenterleaderboards.
  name: iOS GameCenterLeaderboards API
  phrasing_intents:
  - id: gameCenterLeaderboards_createInstance
    intent: Create a Game Center leaderboard
    question: How do I add a new leaderboard to my game in Game Center?
  - id: gameCenterLeaderboards_getInstance
    intent: Get a Game Center leaderboard
    question: What are the settings of one of my Game Center leaderboards?
  - id: gameCenterLeaderboards_updateInstance
    intent: Update a Game Center leaderboard
    question: Can I change a leaderboard's score format or sort order after creating it?
  - id: gameCenterLeaderboards_deleteInstance
    intent: Delete a Game Center leaderboard
    question: How do I delete a leaderboard I created with the v1 API?
  - id: gameCenterLeaderboardsV2_createInstance
    intent: Create a leaderboard with the v2 API
    question: How do I create a leaderboard with the newer v2 Game Center endpoint?
  - id: gameCenterLeaderboardsV2_getInstance
    intent: Get a leaderboard from the v2 API
    question: Can I fetch a leaderboard through the v2 Game Center API?
  - id: gameCenterLeaderboardsV2_updateInstance
    intent: Update a v2 leaderboard
    question: Can I edit a leaderboard through the v2 Game Center API?
  - id: gameCenterLeaderboardsV2_deleteInstance
    intent: Delete a v2 leaderboard
    question: How do I delete a leaderboard that was created with the v2 API?
  phrasing_ops: 21
  slug: ios-gamecenterleaderboards-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The GameCenterLeaderboardSetImages API from iOS — 4 operation(s) for gamecenterleaderboardsetimages.
  name: iOS GameCenterLeaderboardSetImages API
  phrasing_intents:
  - id: gameCenterLeaderboardSetImages_createInstance
    intent: Create a leaderboard set image (legacy v1)
    question: Can I still upload a leaderboard set image through the legacy v1 endpoint?
  - id: gameCenterLeaderboardSetImages_getInstance
    intent: Get a leaderboard set image (legacy v1)
    question: Is fetching a leaderboard set image still possible through the legacy v1 endpoint?
  - id: gameCenterLeaderboardSetImages_updateInstance
    intent: Update a leaderboard set image (legacy v1)
    question: Is editing leaderboard set artwork still possible on the older v1 API?
  - id: gameCenterLeaderboardSetImages_deleteInstance
    intent: Delete a leaderboard set image (legacy v1)
    question: Can I delete a leaderboard set image using the legacy v1 endpoint?
  - id: gameCenterLeaderboardSetImagesV2_createInstance
    intent: Add an image to a Game Center leaderboard set
    question: How do I add an image to a Game Center leaderboard set?
  - id: gameCenterLeaderboardSetImagesV2_getInstance
    intent: Get a Game Center leaderboard set image
    question: Can I look up a Game Center leaderboard set image by ID?
  - id: gameCenterLeaderboardSetImagesV2_updateInstance
    intent: Update a Game Center leaderboard set image
    question: What's the way to update an existing Game Center leaderboard set image?
  - id: gameCenterLeaderboardSetImagesV2_deleteInstance
    intent: Remove a Game Center leaderboard set image
    question: How do I remove an image from a Game Center leaderboard set?
  phrasing_ops: 8
  slug: ios-gamecenterleaderboardsetimages-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The GameCenterLeaderboardSetLocalizations API from iOS — 8 operation(s) for gamecenterleaderboardsetlocalizations.
  name: iOS GameCenterLeaderboardSetLocalizations API
  phrasing_intents:
  - id: gameCenterLeaderboardSetLocalizations_createInstance
    intent: Localize a leaderboard set (v1)
    question: How do I add a translated name for a Game Center leaderboard set using the original v1 endpoint?
  - id: gameCenterLeaderboardSetLocalizations_getInstance
    intent: Get a leaderboard set localization (v1)
    question: Where can I read one v1 leaderboard set localization and its locale?
  - id: gameCenterLeaderboardSetLocalizations_updateInstance
    intent: Update a leaderboard set localization (v1)
    question: How can I fix a typo in a leaderboard set's translated name via v1?
  - id: gameCenterLeaderboardSetLocalizations_deleteInstance
    intent: Delete a leaderboard set localization (v1)
    question: Can I remove a language from a leaderboard set through the v1 API?
  - id: gameCenterLeaderboardSetLocalizationsV2_createInstance
    intent: Localize a leaderboard set (v2)
    question: What's the newer v2 way to add a language to a Game Center leaderboard set?
  - id: gameCenterLeaderboardSetLocalizationsV2_getInstance
    intent: Get a leaderboard set localization (v2)
    question: How do I fetch one leaderboard set localization from the v2 API?
  - id: gameCenterLeaderboardSetLocalizationsV2_updateInstance
    intent: Update a leaderboard set localization (v2)
    question: Can I rename a leaderboard set in one language through the v2 API?
  - id: gameCenterLeaderboardSetLocalizationsV2_deleteInstance
    intent: Delete a leaderboard set localization (v2)
    question: Can I delete a leaderboard set language using the v2 endpoint?
  phrasing_ops: 12
  slug: ios-gamecenterleaderboardsetlocalizations-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The GameCenterLeaderboardSetMemberLocalizations API from iOS — 6 operation(s) for gamecenterleaderboardsetmemberlocalizations.
  name: iOS GameCenterLeaderboardSetMemberLocalizations API
  phrasing_intents:
  - id: gameCenterLeaderboardSetMemberLocalizations_getCollection
    intent: List localizations of a leaderboard in a set
    question: How do I see the localized names a leaderboard uses inside a particular leaderboard set?
  - id: gameCenterLeaderboardSetMemberLocalizations_createInstance
    intent: Localize a leaderboard within a set
    question: Can I give a leaderboard a different localized name when it appears in a set?
  - id: gameCenterLeaderboardSetMemberLocalizations_updateInstance
    intent: Update a leaderboard set member localization
    question: Can I rename a leaderboard's localized title inside a set?
  - id: gameCenterLeaderboardSetMemberLocalizations_deleteInstance
    intent: Delete a leaderboard set member localization
    question: How do I remove a set-specific localization from a leaderboard?
  - id: gameCenterLeaderboardSetMemberLocalizations_gameCenterLeaderboard_getToOneRelationship
    intent: Get the leaderboard ID of a member localization
    question: Which leaderboard ID does a set member localization belong to?
  - id: gameCenterLeaderboardSetMemberLocalizations_gameCenterLeaderboard_getToOneRelated
    intent: Get the leaderboard of a member localization
    question: What leaderboard is this set member localization for?
  - id: gameCenterLeaderboardSetMemberLocalizations_gameCenterLeaderboardSet_getToOneRelationship
    intent: Get the set ID of a member localization
    question: Which leaderboard set ID is a member localization attached to?
  - id: gameCenterLeaderboardSetMemberLocalizations_gameCenterLeaderboardSet_getToOneRelated
    intent: Get the set of a member localization
    question: Which leaderboard set does this member localization appear in?
  phrasing_ops: 8
  slug: ios-gamecenterleaderboardsetmemberlocalizations-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The GameCenterLeaderboardSetReleases API from iOS — 2 operation(s) for gamecenterleaderboardsetreleases.
  name: iOS GameCenterLeaderboardSetReleases API
  phrasing_intents:
  - id: gameCenterLeaderboardSetReleases_createInstance
    intent: Release a leaderboard set
    question: How do I make a leaderboard set live for a Game Center detail?
  - id: gameCenterLeaderboardSetReleases_getInstance
    intent: Get a leaderboard set release
    question: Is a given leaderboard set release live?
  - id: gameCenterLeaderboardSetReleases_deleteInstance
    intent: Delete a leaderboard set release
    question: How do I pull a leaderboard set release?
  phrasing_ops: 3
  slug: ios-gamecenterleaderboardsetreleases-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The GameCenterLeaderboardSets API from iOS — 16 operation(s) for gamecenterleaderboardsets.
  name: iOS GameCenterLeaderboardSets API
  phrasing_intents:
  - id: gameCenterLeaderboardSetsV2_createInstance
    intent: Create a leaderboard set (v2)
    question: How do I group several Game Center leaderboards into a set using the v2 API?
  - id: gameCenterLeaderboardSetsV2_getInstance
    intent: Get a leaderboard set (v2)
    question: What details does the v2 API return for a single leaderboard set?
  - id: gameCenterLeaderboardSetsV2_updateInstance
    intent: Update a leaderboard set (v2)
    question: How do I rename or edit an existing leaderboard set via v2?
  - id: gameCenterLeaderboardSetsV2_deleteInstance
    intent: Delete a leaderboard set (v2)
    question: How do I remove a leaderboard set with the v2 API?
  - id: gameCenterLeaderboardSets_createInstance
    intent: Create a leaderboard set (v1)
    question: How do I create a leaderboard set with the original v1 Game Center API?
  - id: gameCenterLeaderboardSets_getInstance
    intent: Get a leaderboard set (v1)
    question: What does the legacy v1 endpoint return for one leaderboard set?
  - id: gameCenterLeaderboardSets_updateInstance
    intent: Update a leaderboard set (v1)
    question: How do I edit a leaderboard set's attributes through the v1 API?
  - id: gameCenterLeaderboardSets_deleteInstance
    intent: Delete a leaderboard set (v1)
    question: How do I delete a leaderboard set using the legacy v1 API?
  phrasing_ops: 27
  slug: ios-gamecenterleaderboardsets-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The GameCenterLeaderboardSetVersions API from iOS — 4 operation(s) for gamecenterleaderboardsetversions.
  name: iOS GameCenterLeaderboardSetVersions API
  phrasing_intents:
  - id: gameCenterLeaderboardSetVersionsV2_createInstance
    intent: Create a leaderboard set version
    question: How do I create a new version of a Game Center leaderboard set?
  - id: gameCenterLeaderboardSetVersionsV2_getInstance
    intent: Get a leaderboard set version
    question: What state is a particular leaderboard set version in?
  - id: gameCenterLeaderboardSetVersionsV2_localizations_getToManyRelationship
    intent: List IDs of a set version's localizations
    question: Can I get just the localization IDs for a leaderboard set version?
  - id: gameCenterLeaderboardSetVersionsV2_localizations_getToManyRelated
    intent: List a leaderboard set version's localizations
    question: Which languages is my leaderboard set version localized into?
  phrasing_ops: 4
  slug: ios-gamecenterleaderboardsetversions-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The GameCenterLeaderboardVersions API from iOS — 4 operation(s) for gamecenterleaderboardversions.
  name: iOS GameCenterLeaderboardVersions API
  phrasing_intents:
  - id: gameCenterLeaderboardVersionsV2_createInstance
    intent: Create a Game Center leaderboard version
    question: How do I create a new version of a Game Center leaderboard so I can change it?
  - id: gameCenterLeaderboardVersionsV2_getInstance
    intent: Get a Game Center leaderboard version
    question: What state is a leaderboard version in, live or still being prepared?
  - id: gameCenterLeaderboardVersionsV2_localizations_getToManyRelationship
    intent: List localization IDs for a leaderboard version
    question: Which localization IDs are attached to a leaderboard version?
  - id: gameCenterLeaderboardVersionsV2_localizations_getToManyRelated
    intent: List localizations of a leaderboard version
    question: What names and score formats does my leaderboard show in each language?
  phrasing_ops: 4
  slug: ios-gamecenterleaderboardversions-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The GameCenterMatchmakingQueues API from iOS — 7 operation(s) for gamecentermatchmakingqueues.
  name: iOS GameCenterMatchmakingQueues API
  phrasing_intents:
  - id: gameCenterMatchmakingQueues_getCollection
    intent: List matchmaking queues
    question: What Game Center matchmaking queues do I have?
  - id: gameCenterMatchmakingQueues_createInstance
    intent: Create a matchmaking queue
    question: How do I create a new matchmaking queue for my game?
  - id: gameCenterMatchmakingQueues_getInstance
    intent: Get a matchmaking queue
    question: Can I look up one matchmaking queue by ID?
  - id: gameCenterMatchmakingQueues_updateInstance
    intent: Update a matchmaking queue
    question: Can I change the rule set or settings of an existing matchmaking queue?
  - id: gameCenterMatchmakingQueues_deleteInstance
    intent: Delete a matchmaking queue
    question: How do I remove a matchmaking queue I no longer use?
  - id: gameCenterMatchmakingQueues_experimentMatchmakingQueueSizes_getMetrics
    intent: Get experiment queue size metrics
    question: How big is the experiment queue for my matchmaking test over time?
  - id: gameCenterMatchmakingQueues_experimentMatchmakingRequests_getMetrics
    intent: Get experiment matchmaking request metrics
    question: How many matchmaking requests went through my experiment rule set?
  - id: gameCenterMatchmakingQueues_matchmakingQueueSizes_getMetrics
    intent: Get matchmaking queue size metrics
    question: How many players are waiting in my matchmaking queue over time?
  phrasing_ops: 10
  slug: ios-gamecentermatchmakingqueues-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The GameCenterMatchmakingRules API from iOS — 5 operation(s) for gamecentermatchmakingrules.
  name: iOS GameCenterMatchmakingRules API
  phrasing_intents:
  - id: gameCenterMatchmakingRules_createInstance
    intent: Create a matchmaking rule
    question: How do I add a matchmaking rule to a Game Center rule set?
  - id: gameCenterMatchmakingRules_updateInstance
    intent: Update a matchmaking rule
    question: How do I change a matchmaking rule's expression or weight?
  - id: gameCenterMatchmakingRules_deleteInstance
    intent: Delete a matchmaking rule
    question: How do I remove a matchmaking rule?
  - id: gameCenterMatchmakingRules_matchmakingBooleanRuleResults_getMetrics
    intent: Get boolean rule result metrics
    question: How often does my boolean matchmaking rule evaluate true versus false?
  - id: gameCenterMatchmakingRules_matchmakingNumberRuleResults_getMetrics
    intent: Get number rule result metrics
    question: What values does my numeric matchmaking rule produce over time?
  - id: gameCenterMatchmakingRules_matchmakingRuleErrors_getMetrics
    intent: Get matchmaking rule error metrics
    question: Is my matchmaking rule throwing errors, and how often?
  phrasing_ops: 6
  slug: ios-gamecentermatchmakingrules-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The GameCenterMatchmakingRuleSets API from iOS — 8 operation(s) for gamecentermatchmakingrulesets.
  name: iOS GameCenterMatchmakingRuleSets API
  phrasing_intents:
  - id: gameCenterMatchmakingRuleSets_getCollection
    intent: List Game Center matchmaking rule sets
    question: What matchmaking rule sets have I defined in Game Center?
  - id: gameCenterMatchmakingRuleSets_createInstance
    intent: Create a matchmaking rule set
    question: How do I set up rule-based matchmaking for my game?
  - id: gameCenterMatchmakingRuleSets_getInstance
    intent: Get a matchmaking rule set
    question: What are the settings of one matchmaking rule set?
  - id: gameCenterMatchmakingRuleSets_updateInstance
    intent: Update a matchmaking rule set
    question: Can I change the player limits on an existing rule set?
  - id: gameCenterMatchmakingRuleSets_deleteInstance
    intent: Delete a matchmaking rule set
    question: How do I delete a matchmaking rule set I no longer need?
  - id: gameCenterMatchmakingRuleSets_matchmakingQueues_getToManyRelationship
    intent: List queue IDs using a rule set
    question: Can I get just the IDs of queues using a matchmaking rule set?
  - id: gameCenterMatchmakingRuleSets_matchmakingQueues_getToManyRelated
    intent: List matchmaking queues using a rule set
    question: Which matchmaking queues are driven by a given rule set?
  - id: gameCenterMatchmakingRuleSets_rules_getToManyRelationship
    intent: List rule IDs in a rule set
    question: Can I get just the rule IDs inside a matchmaking rule set?
  phrasing_ops: 11
  slug: ios-gamecentermatchmakingrulesets-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The GameCenterMatchmakingRuleSetTests API from iOS — 1 operation(s) for gamecentermatchmakingrulesettests.
  name: iOS GameCenterMatchmakingRuleSetTests API
  phrasing_intents:
  - id: gameCenterMatchmakingRuleSetTests_createInstance
    intent: Test a Game Center matchmaking rule set
    question: What would my matchmaking rules do with a set of sample player requests before I go live?
  phrasing_ops: 1
  slug: ios-gamecentermatchmakingrulesettests-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The GameCenterMatchmakingTeams API from iOS — 2 operation(s) for gamecentermatchmakingteams.
  name: iOS GameCenterMatchmakingTeams API
  phrasing_intents:
  - id: gameCenterMatchmakingTeams_createInstance
    intent: Create a Game Center matchmaking team
    question: How do I add a team to Game Center matchmaking?
  - id: gameCenterMatchmakingTeams_updateInstance
    intent: Update a Game Center matchmaking team
    question: Can I edit a Game Center matchmaking team?
  - id: gameCenterMatchmakingTeams_deleteInstance
    intent: Delete a Game Center matchmaking team
    question: Can I delete a Game Center matchmaking team?
  phrasing_ops: 3
  slug: ios-gamecentermatchmakingteams-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The GameCenterPlayerAchievementSubmissions API from iOS — 1 operation(s) for gamecenterplayerachievementsubmissions.
  name: iOS GameCenterPlayerAchievementSubmissions API
  phrasing_intents:
  - id: gameCenterPlayerAchievementSubmissions_createInstance
    intent: Submit a player's achievement progress
    question: Can I report a player's Game Center achievement progress from my server?
  phrasing_ops: 1
  slug: ios-gamecenterplayerachievementsubmissions-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The InAppPurchaseAppStoreReviewScreenshots API from iOS — 2 operation(s) for inapppurchaseappstorereviewscreenshots.
  name: iOS InAppPurchaseAppStoreReviewScreenshots API
  phrasing_intents:
  - id: inAppPurchaseAppStoreReviewScreenshots_createInstance
    intent: Reserve a review screenshot for an in-app purchase
    question: How do I add the review screenshot App Review needs for an in-app purchase?
  - id: inAppPurchaseAppStoreReviewScreenshots_getInstance
    intent: Get an in-app purchase review screenshot
    question: What's the upload state of my in-app purchase review screenshot?
  - id: inAppPurchaseAppStoreReviewScreenshots_updateInstance
    intent: Commit an in-app purchase review screenshot upload
    question: After uploading the image parts, what marks an in-app purchase review screenshot as uploaded?
  - id: inAppPurchaseAppStoreReviewScreenshots_deleteInstance
    intent: Delete an in-app purchase review screenshot
    question: How do I remove the wrong review screenshot from an in-app purchase?
  phrasing_ops: 4
  slug: ios-inapppurchaseappstorereviewscreenshots-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The InAppPurchaseAvailabilities API from iOS — 4 operation(s) for inapppurchaseavailabilities.
  name: iOS InAppPurchaseAvailabilities API
  phrasing_intents:
  - id: inAppPurchaseAvailabilities_createInstance
    intent: Set where an in-app purchase is available
    question: How do I choose which countries an in-app purchase is sold in?
  - id: inAppPurchaseAvailabilities_getInstance
    intent: Get an in-app purchase's availability
    question: Is my in-app purchase set to be available in new territories automatically?
  - id: inAppPurchaseAvailabilities_availableTerritories_getToManyRelationship
    intent: List territory IDs for an IAP availability
    question: Which territory codes is my in-app purchase available in?
  - id: inAppPurchaseAvailabilities_availableTerritories_getToManyRelated
    intent: List territories where an IAP is sold
    question: In which countries, with their currencies, can customers buy my in-app purchase?
  phrasing_ops: 4
  slug: ios-inapppurchaseavailabilities-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The InAppPurchaseContents API from iOS — 1 operation(s) for inapppurchasecontents.
  name: iOS InAppPurchaseContents API
  phrasing_intents:
  - id: inAppPurchaseContents_getInstance
    intent: Get hosted content for an in-app purchase
    question: What Apple-hosted content package is attached to my in-app purchase?
  phrasing_ops: 1
  slug: ios-inapppurchasecontents-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The InAppPurchaseImages API from iOS — 2 operation(s) for inapppurchaseimages.
  name: iOS InAppPurchaseImages API
  phrasing_intents:
  - id: inAppPurchaseImages_createInstance
    intent: Reserve an in-app purchase image upload
    question: How do I upload promotional artwork for an in-app purchase?
  - id: inAppPurchaseImages_getInstance
    intent: Get an in-app purchase image
    question: Has the promotional image for my in-app purchase been approved?
  - id: inAppPurchaseImages_updateInstance
    intent: Commit an in-app purchase image upload
    question: How do I finalize an in-app purchase image after uploading the file?
  - id: inAppPurchaseImages_deleteInstance
    intent: Delete an in-app purchase image
    question: Can I remove the promotional artwork from an in-app purchase?
  phrasing_ops: 4
  slug: ios-inapppurchaseimages-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The InAppPurchaseLocalizations API from iOS — 2 operation(s) for inapppurchaselocalizations.
  name: iOS InAppPurchaseLocalizations API
  phrasing_intents:
  - id: inAppPurchaseLocalizations_createInstance
    intent: Add an in-app purchase localization
    question: How do I add a display name and description for an in-app purchase in another language?
  - id: inAppPurchaseLocalizations_getInstance
    intent: Get an in-app purchase localization
    question: What localized name and description does an in-app purchase have in one locale?
  - id: inAppPurchaseLocalizations_updateInstance
    intent: Update an in-app purchase localization
    question: How do I change the localized description of an in-app purchase?
  - id: inAppPurchaseLocalizations_deleteInstance
    intent: Delete an in-app purchase localization
    question: How do I remove a language from an in-app purchase?
  phrasing_ops: 4
  slug: ios-inapppurchaselocalizations-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The InAppPurchaseOfferCodeCustomCodes API from iOS — 2 operation(s) for inapppurchaseoffercodecustomcodes.
  name: iOS InAppPurchaseOfferCodeCustomCodes API
  phrasing_intents:
  - id: inAppPurchaseOfferCodeCustomCodes_createInstance
    intent: Create a custom in-app purchase offer code
    question: How do I create a memorable promo code for an in-app purchase offer?
  - id: inAppPurchaseOfferCodeCustomCodes_getInstance
    intent: Get a custom in-app purchase offer code
    question: How many redemptions does a custom in-app purchase code allow?
  - id: inAppPurchaseOfferCodeCustomCodes_updateInstance
    intent: Update a custom in-app purchase offer code
    question: Can I deactivate a custom in-app purchase promo code?
  phrasing_ops: 3
  slug: ios-inapppurchaseoffercodecustomcodes-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The InAppPurchaseOfferCodeOneTimeUseCodes API from iOS — 3 operation(s) for inapppurchaseoffercodeonetimeusecodes.
  name: iOS InAppPurchaseOfferCodeOneTimeUseCodes API
  phrasing_intents:
  - id: inAppPurchaseOfferCodeOneTimeUseCodes_createInstance
    intent: Generate one-time use offer codes
    question: Can I generate a batch of one-time use offer codes for an in-app purchase?
  - id: inAppPurchaseOfferCodeOneTimeUseCodes_getInstance
    intent: Get a batch of one-time use offer codes
    question: Can I look up a one-time use code batch by ID?
  - id: inAppPurchaseOfferCodeOneTimeUseCodes_updateInstance
    intent: Update a batch of one-time use offer codes
    question: Can I change a batch of one-time use offer codes after creating it?
  - id: inAppPurchaseOfferCodeOneTimeUseCodes_values_getToOneRelated
    intent: Get the code values in a one-time use batch
    question: How do I get the actual one-time use code values to hand out?
  phrasing_ops: 4
  slug: ios-inapppurchaseoffercodeonetimeusecodes-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The InAppPurchaseOfferCodes API from iOS — 8 operation(s) for inapppurchaseoffercodes.
  name: iOS InAppPurchaseOfferCodes API
  phrasing_intents:
  - id: inAppPurchaseOfferCodes_createInstance
    intent: Create an offer code for an in-app purchase
    question: How do I create a promotional offer code campaign for an in-app purchase?
  - id: inAppPurchaseOfferCodes_getInstance
    intent: Get an in-app purchase offer code
    question: What are the settings of one in-app purchase offer code, like eligibility and status?
  - id: inAppPurchaseOfferCodes_updateInstance
    intent: Update an in-app purchase offer code
    question: How do I turn off or change an existing in-app purchase offer code?
  - id: inAppPurchaseOfferCodes_customCodes_getToManyRelationship
    intent: List custom code IDs for an offer code
    question: Which custom code IDs belong to an in-app purchase offer code?
  - id: inAppPurchaseOfferCodes_customCodes_getToManyRelated
    intent: List custom codes for an in-app purchase offer
    question: What custom, human-readable codes have I created for an in-app purchase offer, and how many redemptions does each allow?
  - id: inAppPurchaseOfferCodes_oneTimeUseCodes_getToManyRelationship
    intent: List one-time-use code batch IDs for an offer
    question: Which one-time-use code batch IDs exist for an in-app purchase offer?
  - id: inAppPurchaseOfferCodes_oneTimeUseCodes_getToManyRelated
    intent: List one-time-use code batches for an offer
    question: What batches of single-use redemption codes have been generated for an in-app purchase offer?
  - id: inAppPurchaseOfferCodes_prices_getToManyRelationship
    intent: List price IDs for an in-app purchase offer code
    question: Which price record IDs are attached to an in-app purchase offer code?
  phrasing_ops: 9
  slug: ios-inapppurchaseoffercodes-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The InAppPurchasePricePoints API from iOS — 2 operation(s) for inapppurchasepricepoints.
  name: iOS InAppPurchasePricePoints API
  phrasing_intents:
  - id: inAppPurchasePricePoints_equalizations_getToManyRelationship
    intent: List equalization IDs of a price point
    question: Which equalized price point IDs match an in-app purchase price point?
  - id: inAppPurchasePricePoints_equalizations_getToManyRelated
    intent: List equalized prices for a price point
    question: What's the equivalent price in other territories for an in-app purchase price point?
  phrasing_ops: 2
  slug: ios-inapppurchasepricepoints-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The InAppPurchasePriceSchedules API from iOS — 8 operation(s) for inapppurchasepriceschedules.
  name: iOS InAppPurchasePriceSchedules API
  phrasing_intents:
  - id: inAppPurchasePriceSchedules_createInstance
    intent: Set an in-app purchase's price schedule
    question: How do I price a consumable in-app purchase and schedule a future change?
  - id: inAppPurchasePriceSchedules_getInstance
    intent: Get an in-app purchase's price schedule
    question: What price schedule is applied to one of my in-app purchases?
  - id: inAppPurchasePriceSchedules_automaticPrices_getToManyRelationship
    intent: List automatic IAP price IDs in a schedule
    question: Which auto-equalized price IDs belong to an in-app purchase price schedule?
  - id: inAppPurchasePriceSchedules_automaticPrices_getToManyRelated
    intent: List automatically equalized in-app purchase prices
    question: What did my in-app purchase get priced at automatically in each storefront?
  - id: inAppPurchasePriceSchedules_baseTerritory_getToOneRelationship
    intent: Get the base territory ID of an IAP price schedule
    question: Which territory ID anchors an in-app purchase's price schedule?
  - id: inAppPurchasePriceSchedules_baseTerritory_getToOneRelated
    intent: Get the base territory of an IAP price schedule
    question: Which country and currency is my in-app purchase priced from?
  - id: inAppPurchasePriceSchedules_manualPrices_getToManyRelationship
    intent: List manual IAP price IDs in a schedule
    question: Which manually set price IDs are in an in-app purchase price schedule?
  - id: inAppPurchasePriceSchedules_manualPrices_getToManyRelated
    intent: List manually set in-app purchase prices
    question: Which territories have a price I set by hand for this in-app purchase?
  phrasing_ops: 8
  slug: ios-inapppurchasepriceschedules-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The InAppPurchases API from iOS — 21 operation(s) for inapppurchases.
  name: iOS InAppPurchases API
  phrasing_intents:
  - id: inAppPurchases_getInstance
    intent: Get an in-app purchase (legacy v1)
    question: Can I still fetch an in-app purchase through the older v1 endpoint?
  - id: inAppPurchasesV2_createInstance
    intent: Create an in-app purchase
    question: How do I set up a new in-app purchase for my app in App Store Connect?
  - id: inAppPurchasesV2_getInstance
    intent: Get an in-app purchase
    question: Where can I look up the current details of one in-app purchase?
  - id: inAppPurchasesV2_updateInstance
    intent: Update an in-app purchase
    question: How do I change the settings of an existing in-app purchase?
  - id: inAppPurchasesV2_deleteInstance
    intent: Delete an in-app purchase
    question: Can I remove an in-app purchase I no longer want to sell?
  - id: inAppPurchasesV2_appStoreReviewScreenshot_getToOneRelationship
    intent: Get the review screenshot ID of an in-app purchase
    question: Which review screenshot ID is linked to my in-app purchase?
  - id: inAppPurchasesV2_appStoreReviewScreenshot_getToOneRelated
    intent: Get an in-app purchase's review screenshot
    question: Where do I see the screenshot I submitted for App Store review of an in-app purchase?
  - id: inAppPurchasesV2_content_getToOneRelationship
    intent: Get the hosted content ID of an in-app purchase
    question: Which hosted content ID belongs to my in-app purchase?
  phrasing_ops: 23
  slug: ios-inapppurchases-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The InAppPurchaseSubmissions API from iOS — 1 operation(s) for inapppurchasesubmissions.
  name: iOS InAppPurchaseSubmissions API
  phrasing_intents:
  - id: inAppPurchaseSubmissions_createInstance
    intent: Submit an in-app purchase for review
    question: How do I submit an in-app purchase for App Review?
  phrasing_ops: 1
  slug: ios-inapppurchasesubmissions-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The MarketplaceSearchDetails API from iOS — 2 operation(s) for marketplacesearchdetails.
  name: iOS MarketplaceSearchDetails API
  phrasing_intents:
  - id: marketplaceSearchDetails_createInstance
    intent: Set an app's alternative marketplace catalog URL
    question: How do I register a catalog URL for my app in alternative marketplace search?
  - id: marketplaceSearchDetails_updateInstance
    intent: Change an app's marketplace catalog URL
    question: Can I change the catalog URL used for alternative marketplace search?
  - id: marketplaceSearchDetails_deleteInstance
    intent: Remove an app's marketplace search detail
    question: Can I remove my app's catalog URL from alternative marketplace search?
  phrasing_ops: 3
  slug: ios-marketplacesearchdetails-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The MarketplaceWebhooks API from iOS — 2 operation(s) for marketplacewebhooks.
  name: iOS MarketplaceWebhooks API
  phrasing_intents:
  - id: marketplaceWebhooks_getCollection
    intent: List marketplace webhooks
    question: Which alternative marketplace webhooks have I registered?
  - id: marketplaceWebhooks_createInstance
    intent: Register a marketplace webhook
    question: How do I get notified when my alternative marketplace receives events?
  - id: marketplaceWebhooks_updateInstance
    intent: Update a marketplace webhook
    question: Can I change the URL or secret of an existing marketplace webhook?
  - id: marketplaceWebhooks_deleteInstance
    intent: Delete a marketplace webhook
    question: How do I stop receiving marketplace webhook events?
  phrasing_ops: 4
  slug: ios-marketplacewebhooks-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The Metrics API from iOS — 15 operation(s) for metrics.
  name: iOS Metrics API
  phrasing_intents:
  - id: apps_betaTesterUsages_getMetrics
    intent: Get beta tester usage metrics for an app
    question: How actively are TestFlight testers using my app?
  - id: betaGroups_betaTesterUsages_getMetrics
    intent: Get tester usage metrics for a beta group
    question: How engaged are the testers in one of my TestFlight beta groups?
  - id: betaGroups_publicLinkUsages_getMetrics
    intent: Get public link usage for a beta group
    question: How many people joined my beta through the TestFlight public link?
  - id: betaTesters_betaTesterUsages_getMetrics
    intent: Get usage metrics for one beta tester
    question: How much is a specific TestFlight tester using my app?
  - id: builds_betaBuildUsages_getMetrics
    intent: Get beta usage metrics for a build
    question: How are testers using a particular TestFlight build?
  - id: gameCenterDetails_classicMatchmakingRequests_getMetrics
    intent: Get classic matchmaking request metrics
    question: How many classic Game Center matchmaking requests is my game handling?
  - id: gameCenterDetails_ruleBasedMatchmakingRequests_getMetrics
    intent: Get rule-based matchmaking request metrics
    question: How many rule-based matchmaking requests are coming through my Game Center detail?
  - id: gameCenterMatchmakingQueues_experimentMatchmakingQueueSizes_getMetrics
    intent: Get experiment queue size metrics
    question: How large is the experimental matchmaking queue over time?
  phrasing_ops: 15
  slug: ios-metrics-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The Nominations API from iOS — 2 operation(s) for nominations.
  name: iOS Nominations API
  phrasing_intents:
  - id: nominations_getCollection
    intent: List my featuring nominations
    question: Which App Store featuring nominations have I drafted or submitted?
  - id: nominations_createInstance
    intent: Nominate an app for App Store featuring
    question: How do I nominate my app or launch for featuring on the App Store?
  - id: nominations_getInstance
    intent: Get a featuring nomination
    question: What did I write in a specific featuring nomination?
  - id: nominations_updateInstance
    intent: Update a featuring nomination
    question: Can I edit the description or publish date of an existing nomination?
  - id: nominations_deleteInstance
    intent: Delete a featuring nomination
    question: Can I delete a nomination I no longer want to send?
  phrasing_ops: 5
  slug: ios-nominations-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The PassTypeIds API from iOS — 4 operation(s) for passtypeids.
  name: iOS PassTypeIds API
  phrasing_intents:
  - id: passTypeIds_getCollection
    intent: List Wallet pass type IDs
    question: How do I list the Wallet pass type IDs registered to my developer account?
  - id: passTypeIds_createInstance
    intent: Register a Wallet pass type ID
    question: How do I register a new pass type ID for Apple Wallet passes?
  - id: passTypeIds_getInstance
    intent: Get a Wallet pass type ID
    question: Where can I look up one pass type ID's details?
  - id: passTypeIds_updateInstance
    intent: Update a Wallet pass type ID
    question: Can I change the details of an existing pass type ID?
  - id: passTypeIds_deleteInstance
    intent: Delete a Wallet pass type ID
    question: Can I delete a pass type ID I no longer use?
  - id: passTypeIds_certificates_getToManyRelationship
    intent: List certificate IDs of a pass type ID
    question: Which certificate IDs are tied to a pass type ID?
  - id: passTypeIds_certificates_getToManyRelated
    intent: List certificates for a pass type ID
    question: What signing certificates exist for my Wallet pass type ID?
  phrasing_ops: 7
  slug: ios-passtypeids-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The PreReleaseVersions API from iOS — 6 operation(s) for prereleaseversions.
  name: iOS PreReleaseVersions API
  phrasing_intents:
  - id: preReleaseVersions_getCollection
    intent: List TestFlight pre-release versions
    question: How do I list the TestFlight pre-release versions for my app?
  - id: preReleaseVersions_getInstance
    intent: Get a TestFlight pre-release version
    question: Can I look up one pre-release version by ID?
  - id: preReleaseVersions_app_getToOneRelationship
    intent: Get the app ID of a pre-release version
    question: Which app ID does a pre-release version belong to?
  - id: preReleaseVersions_app_getToOneRelated
    intent: Get the app of a pre-release version
    question: Which app is this pre-release version for?
  - id: preReleaseVersions_builds_getToManyRelationship
    intent: List build IDs of a pre-release version
    question: Which build IDs are under a pre-release version?
  - id: preReleaseVersions_builds_getToManyRelated
    intent: List builds of a pre-release version
    question: What builds have been uploaded for this pre-release version?
  phrasing_ops: 6
  slug: ios-prereleaseversions-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The Profiles API from iOS — 8 operation(s) for profiles.
  name: iOS Profiles API
  phrasing_intents:
  - id: profiles_getCollection
    intent: List provisioning profiles
    question: What provisioning profiles do I have in my developer account?
  - id: profiles_createInstance
    intent: Create a provisioning profile
    question: How do I generate a new development provisioning profile through the API?
  - id: profiles_getInstance
    intent: Get a provisioning profile
    question: How do I download the contents of a specific provisioning profile?
  - id: profiles_deleteInstance
    intent: Delete a provisioning profile
    question: Can I delete an old provisioning profile I no longer use?
  - id: profiles_bundleId_getToOneRelationship
    intent: Get the bundle ID reference of a profile
    question: Which bundle ID record ID is a provisioning profile tied to?
  - id: profiles_bundleId_getToOneRelated
    intent: Get the app identifier a profile is for
    question: What app identifier string and platform does a provisioning profile cover?
  - id: profiles_certificates_getToManyRelationship
    intent: List certificate IDs in a profile
    question: Which certificate IDs are included in a provisioning profile?
  - id: profiles_certificates_getToManyRelated
    intent: List the signing certificates in a profile
    question: Which signing certificates can sign builds with this provisioning profile?
  phrasing_ops: 10
  slug: ios-profiles-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The PromotedPurchases API from iOS — 2 operation(s) for promotedpurchases.
  name: iOS PromotedPurchases API
  phrasing_intents:
  - id: promotedPurchases_createInstance
    intent: Promote an in-app purchase on the App Store
    question: How do I promote an in-app purchase or subscription on my product page?
  - id: promotedPurchases_getInstance
    intent: Get a promoted purchase
    question: Is a promoted purchase approved and visible to customers?
  - id: promotedPurchases_updateInstance
    intent: Update a promoted purchase
    question: Can I hide a promoted purchase from all users without deleting it?
  - id: promotedPurchases_deleteInstance
    intent: Stop promoting an in-app purchase
    question: Can I stop promoting an in-app purchase on my product page?
  phrasing_ops: 4
  slug: ios-promotedpurchases-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The ReviewSubmissionItems API from iOS — 2 operation(s) for reviewsubmissionitems.
  name: iOS ReviewSubmissionItems API
  phrasing_intents:
  - id: reviewSubmissionItems_createInstance
    intent: Add an item to an App Review submission
    question: How do I add an app version or in-app event to a review submission?
  - id: reviewSubmissionItems_updateInstance
    intent: Update a review submission item
    question: Can I mark a review submission item as resolved or removed?
  - id: reviewSubmissionItems_deleteInstance
    intent: Remove an item from a review submission
    question: Can I pull an item out of a review submission before it is sent?
  phrasing_ops: 3
  slug: ios-reviewsubmissionitems-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The ReviewSubmissions API from iOS — 4 operation(s) for reviewsubmissions.
  name: iOS ReviewSubmissions API
  phrasing_intents:
  - id: reviewSubmissions_getCollection
    intent: List an app's App Review submissions
    question: Which submissions to App Review exist for my app?
  - id: reviewSubmissions_createInstance
    intent: Start a new App Review submission
    question: How do I start a submission to send my app to App Review?
  - id: reviewSubmissions_getInstance
    intent: Get an App Review submission
    question: What state is a specific review submission in right now?
  - id: reviewSubmissions_updateInstance
    intent: Submit or cancel an App Review submission
    question: How do I actually submit a prepared review submission to App Review?
  - id: reviewSubmissions_items_getToManyRelationship
    intent: List item IDs in a review submission
    question: Can I get only the IDs of the items inside a review submission?
  - id: reviewSubmissions_items_getToManyRelated
    intent: List the items in a review submission
    question: What versions, events or product pages are included in my review submission?
  phrasing_ops: 6
  slug: ios-reviewsubmissions-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The RoutingAppCoverages API from iOS — 2 operation(s) for routingappcoverages.
  name: iOS RoutingAppCoverages API
  phrasing_intents:
  - id: routingAppCoverages_createInstance
    intent: Upload a routing app coverage file
    question: How do I register the geographic coverage file for my routing app?
  - id: routingAppCoverages_getInstance
    intent: Get a routing app coverage file
    question: Has my routing app coverage file finished processing?
  - id: routingAppCoverages_updateInstance
    intent: Commit a routing app coverage upload
    question: How do I mark my routing coverage upload as complete?
  - id: routingAppCoverages_deleteInstance
    intent: Delete a routing app coverage file
    question: How do I remove a routing app coverage file from a version?
  phrasing_ops: 4
  slug: ios-routingappcoverages-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The SalesReports API from iOS — 1 operation(s) for salesreports.
  name: iOS SalesReports API
  phrasing_intents:
  - id: salesReports_getCollection
    intent: Download a sales and trends report
    question: How do I download my App Store sales and trends report?
  phrasing_ops: 1
  slug: ios-salesreports-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The SandboxTesters API from iOS — 2 operation(s) for sandboxtesters.
  name: iOS SandboxTesters API
  phrasing_intents:
  - id: sandboxTestersV2_getCollection
    intent: List sandbox testers
    question: Which sandbox Apple Accounts do I have for testing purchases?
  - id: sandboxTestersV2_updateInstance
    intent: Update a sandbox tester
    question: Can I change a sandbox tester's storefront territory?
  phrasing_ops: 2
  slug: ios-sandboxtesters-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The SandboxTestersClearPurchaseHistoryRequest API from iOS — 1 operation(s) for sandboxtestersclearpurchasehistoryrequest.
  name: iOS SandboxTestersClearPurchaseHistoryRequest API
  phrasing_intents:
  - id: sandboxTestersClearPurchaseHistoryRequestV2_createInstance
    intent: Clear purchase history for sandbox testers
    question: How do I reset a sandbox tester's purchase history so I can buy again?
  phrasing_ops: 1
  slug: ios-sandboxtestersclearpurchasehistoryrequest-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The ScmGitReferences API from iOS — 1 operation(s) for scmgitreferences.
  name: iOS ScmGitReferences API
  phrasing_intents:
  - id: scmGitReferences_getInstance
    intent: Get an Xcode Cloud git reference
    question: What branch or tag does an Xcode Cloud git reference point to?
  phrasing_ops: 1
  slug: ios-scmgitreferences-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The ScmProviders API from iOS — 4 operation(s) for scmproviders.
  name: iOS ScmProviders API
  phrasing_intents:
  - id: scmProviders_getCollection
    intent: List connected source control providers
    question: Which source code hosts has Xcode Cloud been connected to?
  - id: scmProviders_getInstance
    intent: Get a source control provider
    question: What type and URL does a connected SCM provider have?
  - id: scmProviders_repositories_getToManyRelationship
    intent: List repository IDs for an SCM provider
    question: Which repository IDs does Xcode Cloud see under one SCM provider?
  - id: scmProviders_repositories_getToManyRelated
    intent: List repositories for an SCM provider
    question: What Git repositories, with owner and clone URLs, are available through this SCM connection?
  phrasing_ops: 4
  slug: ios-scmproviders-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The ScmPullRequests API from iOS — 1 operation(s) for scmpullrequests.
  name: iOS ScmPullRequests API
  phrasing_intents:
  - id: scmPullRequests_getInstance
    intent: Get a pull request seen by Xcode Cloud
    question: Can I look up a pull request that Xcode Cloud built?
  phrasing_ops: 1
  slug: ios-scmpullrequests-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The ScmRepositories API from iOS — 6 operation(s) for scmrepositories.
  name: iOS ScmRepositories API
  phrasing_intents:
  - id: scmRepositories_getCollection
    intent: List Xcode Cloud source repositories
    question: Which Git repositories are connected to Xcode Cloud?
  - id: scmRepositories_getInstance
    intent: Get an Xcode Cloud repository
    question: What are the URLs and owner of a connected repository?
  - id: scmRepositories_gitReferences_getToManyRelationship
    intent: List Git reference IDs of a repository
    question: Can I get just the branch and tag reference IDs for a repository?
  - id: scmRepositories_gitReferences_getToManyRelated
    intent: List branches and tags of a repository
    question: What branches and tags does Xcode Cloud see in my repo?
  - id: scmRepositories_pullRequests_getToManyRelationship
    intent: List pull request IDs of a repository
    question: Can I get just the pull request IDs Xcode Cloud tracks for a repo?
  - id: scmRepositories_pullRequests_getToManyRelated
    intent: List pull requests of a repository
    question: What open pull requests does Xcode Cloud see for my repository?
  phrasing_ops: 6
  slug: ios-scmrepositories-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The SubscriptionAppStoreReviewScreenshots API from iOS — 2 operation(s) for subscriptionappstorereviewscreenshots.
  name: iOS SubscriptionAppStoreReviewScreenshots API
  phrasing_intents:
  - id: subscriptionAppStoreReviewScreenshots_createInstance
    intent: Reserve a review screenshot for a subscription
    question: How do I add the review screenshot App Review needs for an auto-renewable subscription?
  - id: subscriptionAppStoreReviewScreenshots_getInstance
    intent: Get a subscription review screenshot
    question: What's the upload state of my subscription's review screenshot?
  - id: subscriptionAppStoreReviewScreenshots_updateInstance
    intent: Commit a subscription review screenshot upload
    question: After uploading the image parts, what marks a subscription review screenshot as uploaded?
  - id: subscriptionAppStoreReviewScreenshots_deleteInstance
    intent: Delete a subscription review screenshot
    question: How do I remove the wrong review screenshot from a subscription?
  phrasing_ops: 4
  slug: ios-subscriptionappstorereviewscreenshots-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The SubscriptionAvailabilities API from iOS — 4 operation(s) for subscriptionavailabilities.
  name: iOS SubscriptionAvailabilities API
  phrasing_intents:
  - id: subscriptionAvailabilities_createInstance
    intent: Set where a subscription is available
    question: How do I choose which countries an auto-renewable subscription is sold in?
  - id: subscriptionAvailabilities_getInstance
    intent: Get a subscription's availability
    question: Is my subscription set to be offered in new territories automatically?
  - id: subscriptionAvailabilities_availableTerritories_getToManyRelationship
    intent: List territory IDs for a subscription
    question: Which territory codes is my subscription available in?
  - id: subscriptionAvailabilities_availableTerritories_getToManyRelated
    intent: List territories where a subscription is sold
    question: In which countries, with their currencies, can people subscribe?
  phrasing_ops: 4
  slug: ios-subscriptionavailabilities-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The SubscriptionGracePeriods API from iOS — 1 operation(s) for subscriptiongraceperiods.
  name: iOS SubscriptionGracePeriods API
  phrasing_intents:
  - id: subscriptionGracePeriods_getInstance
    intent: Get billing grace period settings
    question: Is Billing Grace Period turned on for my subscriptions?
  - id: subscriptionGracePeriods_updateInstance
    intent: Change billing grace period settings
    question: How do I enable Billing Grace Period for my app's subscriptions?
  phrasing_ops: 2
  slug: ios-subscriptiongraceperiods-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The SubscriptionGroupLocalizations API from iOS — 2 operation(s) for subscriptiongrouplocalizations.
  name: iOS SubscriptionGroupLocalizations API
  phrasing_intents:
  - id: subscriptionGroupLocalizations_createInstance
    intent: Add a subscription group display name in a language
    question: How do I localize the name of my subscription group for Japanese users?
  - id: subscriptionGroupLocalizations_getInstance
    intent: Get a subscription group localization
    question: What name does my subscription group show in a given language?
  - id: subscriptionGroupLocalizations_updateInstance
    intent: Update a subscription group localization
    question: How do I rename my subscription group in one language?
  - id: subscriptionGroupLocalizations_deleteInstance
    intent: Delete a subscription group localization
    question: Can I remove a language from my subscription group?
  phrasing_ops: 4
  slug: ios-subscriptiongrouplocalizations-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The SubscriptionGroupSubmissions API from iOS — 1 operation(s) for subscriptiongroupsubmissions.
  name: iOS SubscriptionGroupSubmissions API
  phrasing_intents:
  - id: subscriptionGroupSubmissions_createInstance
    intent: Submit a subscription group for review
    question: How do I send a subscription group to App Review?
  phrasing_ops: 1
  slug: ios-subscriptiongroupsubmissions-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The SubscriptionImages API from iOS — 2 operation(s) for subscriptionimages.
  name: iOS SubscriptionImages API
  phrasing_intents:
  - id: subscriptionImages_createInstance
    intent: Reserve a subscription image
    question: How do I upload a promotional image for a subscription?
  - id: subscriptionImages_getInstance
    intent: Get a subscription image
    question: What is the upload state of a subscription image?
  - id: subscriptionImages_updateInstance
    intent: Commit a subscription image
    question: How do I mark a subscription image upload as complete?
  - id: subscriptionImages_deleteInstance
    intent: Delete a subscription image
    question: How do I remove a subscription's promotional image?
  phrasing_ops: 4
  slug: ios-subscriptionimages-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The SubscriptionIntroductoryOffers API from iOS — 2 operation(s) for subscriptionintroductoryoffers.
  name: iOS SubscriptionIntroductoryOffers API
  phrasing_intents:
  - id: subscriptionIntroductoryOffers_createInstance
    intent: Create a subscription introductory offer
    question: How do I give new subscribers a free trial for the first week?
  - id: subscriptionIntroductoryOffers_updateInstance
    intent: Update a subscription introductory offer
    question: Can I change the end date of an existing introductory offer?
  - id: subscriptionIntroductoryOffers_deleteInstance
    intent: Delete a subscription introductory offer
    question: Can I end a free trial offer for new subscribers early?
  phrasing_ops: 3
  slug: ios-subscriptionintroductoryoffers-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The SubscriptionLocalizations API from iOS — 2 operation(s) for subscriptionlocalizations.
  name: iOS SubscriptionLocalizations API
  phrasing_intents:
  - id: subscriptionLocalizations_createInstance
    intent: Add a subscription localization
    question: How do I add a localized name and description for a subscription?
  - id: subscriptionLocalizations_getInstance
    intent: Get a subscription localization
    question: Can I look up one subscription localization?
  - id: subscriptionLocalizations_updateInstance
    intent: Update a subscription localization
    question: How do I edit the localized text of a subscription?
  - id: subscriptionLocalizations_deleteInstance
    intent: Delete a subscription localization
    question: Can I delete a subscription localization for a language I no longer support?
  phrasing_ops: 4
  slug: ios-subscriptionlocalizations-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The SubscriptionOfferCodeCustomCodes API from iOS — 2 operation(s) for subscriptionoffercodecustomcodes.
  name: iOS SubscriptionOfferCodeCustomCodes API
  phrasing_intents:
  - id: subscriptionOfferCodeCustomCodes_createInstance
    intent: Create a custom subscription offer code
    question: How do I create a memorable custom code, like SUMMER25, for a subscription offer?
  - id: subscriptionOfferCodeCustomCodes_getInstance
    intent: Get a custom subscription offer code
    question: What is the code text, quantity and expiration of a custom subscription offer code?
  - id: subscriptionOfferCodeCustomCodes_updateInstance
    intent: Deactivate a custom subscription offer code
    question: How do I switch off a custom subscription offer code early?
  phrasing_ops: 3
  slug: ios-subscriptionoffercodecustomcodes-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The SubscriptionOfferCodeOneTimeUseCodes API from iOS — 3 operation(s) for subscriptionoffercodeonetimeusecodes.
  name: iOS SubscriptionOfferCodeOneTimeUseCodes API
  phrasing_intents:
  - id: subscriptionOfferCodeOneTimeUseCodes_createInstance
    intent: Generate one-time-use subscription offer codes
    question: How do I generate a batch of single-use codes for a subscription offer?
  - id: subscriptionOfferCodeOneTimeUseCodes_getInstance
    intent: Get a batch of one-time-use offer codes
    question: How many codes are in a one-time-use batch and when do they expire?
  - id: subscriptionOfferCodeOneTimeUseCodes_updateInstance
    intent: Update a one-time-use code batch
    question: Can I deactivate a batch of one-time-use subscription codes?
  - id: subscriptionOfferCodeOneTimeUseCodes_values_getToOneRelated
    intent: Download the one-time-use code values
    question: Where do I get the actual code strings to hand out to customers?
  phrasing_ops: 4
  slug: ios-subscriptionoffercodeonetimeusecodes-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The SubscriptionOfferCodes API from iOS — 8 operation(s) for subscriptionoffercodes.
  name: iOS SubscriptionOfferCodes API
  phrasing_intents:
  - id: subscriptionOfferCodes_createInstance
    intent: Create a subscription offer code campaign
    question: How do I create an offer code campaign for an auto-renewable subscription?
  - id: subscriptionOfferCodes_getInstance
    intent: Get a subscription offer code
    question: What are the eligibility and duration settings of one of my offer codes?
  - id: subscriptionOfferCodes_updateInstance
    intent: Update a subscription offer code
    question: Can I turn off an active subscription offer code?
  - id: subscriptionOfferCodes_customCodes_getToManyRelationship
    intent: List custom code IDs for an offer
    question: Which custom code IDs belong to my subscription offer?
  - id: subscriptionOfferCodes_customCodes_getToManyRelated
    intent: List an offer's custom codes
    question: What custom codes like SUMMER2026 exist for my subscription offer?
  - id: subscriptionOfferCodes_oneTimeUseCodes_getToManyRelationship
    intent: List one-time code batch IDs for an offer
    question: Which one-time-use code batch IDs are attached to my offer?
  - id: subscriptionOfferCodes_oneTimeUseCodes_getToManyRelated
    intent: List an offer's one-time-use code batches
    question: How many one-time-use code batches have I generated for an offer, and when do they expire?
  - id: subscriptionOfferCodes_prices_getToManyRelationship
    intent: List price IDs for an offer code
    question: Which price IDs are set on my subscription offer code?
  phrasing_ops: 9
  slug: ios-subscriptionoffercodes-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The SubscriptionPricePoints API from iOS — 3 operation(s) for subscriptionpricepoints.
  name: iOS SubscriptionPricePoints API
  phrasing_intents:
  - id: subscriptionPricePoints_getInstance
    intent: Get a subscription price point
    question: What customer price and proceeds does a subscription price point give me?
  - id: subscriptionPricePoints_equalizations_getToManyRelationship
    intent: List equalized price point IDs
    question: Which equalized price point IDs match my subscription price in other countries?
  - id: subscriptionPricePoints_equalizations_getToManyRelated
    intent: List equivalent prices in other territories
    question: What would my subscription price be in other countries if equalized?
  phrasing_ops: 3
  slug: ios-subscriptionpricepoints-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The SubscriptionPrices API from iOS — 2 operation(s) for subscriptionprices.
  name: iOS SubscriptionPrices API
  phrasing_intents:
  - id: subscriptionPrices_createInstance
    intent: Set a subscription price
    question: How do I set the price of an auto-renewable subscription in a territory?
  - id: subscriptionPrices_deleteInstance
    intent: Delete a subscription price
    question: How do I remove a scheduled subscription price?
  phrasing_ops: 2
  slug: ios-subscriptionprices-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The SubscriptionPromotionalOffers API from iOS — 4 operation(s) for subscriptionpromotionaloffers.
  name: iOS SubscriptionPromotionalOffers API
  phrasing_intents:
  - id: subscriptionPromotionalOffers_createInstance
    intent: Create a subscription promotional offer
    question: How do I create a promotional offer for an auto-renewable subscription?
  - id: subscriptionPromotionalOffers_getInstance
    intent: Get a subscription promotional offer
    question: Can I look up a single promotional offer by ID?
  - id: subscriptionPromotionalOffers_updateInstance
    intent: Update a promotional offer's prices
    question: Can I change the prices of an existing promotional offer?
  - id: subscriptionPromotionalOffers_deleteInstance
    intent: Delete a subscription promotional offer
    question: How do I remove a promotional offer from a subscription?
  - id: subscriptionPromotionalOffers_prices_getToManyRelationship
    intent: List IDs of a promo offer's prices
    question: Can I get just the price IDs attached to a promotional offer?
  - id: subscriptionPromotionalOffers_prices_getToManyRelated
    intent: List a promo offer's prices by territory
    question: What does my promotional offer cost in each country?
  phrasing_ops: 6
  slug: ios-subscriptionpromotionaloffers-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The Subscriptions API from iOS — 24 operation(s) for subscriptions.
  name: iOS Subscriptions API
  phrasing_intents:
  - id: subscriptions_createInstance
    intent: Create an auto-renewable subscription
    question: How do I add a new auto-renewable subscription product to my app in App Store Connect?
  - id: subscriptions_getInstance
    intent: Get a subscription's details
    question: What are the current settings of one of my auto-renewable subscriptions?
  - id: subscriptions_updateInstance
    intent: Update a subscription
    question: How do I change the name or duration of an existing subscription product?
  - id: subscriptions_deleteInstance
    intent: Delete a subscription
    question: Can I remove a subscription product that I no longer want to offer?
  - id: subscriptions_appStoreReviewScreenshot_getToOneRelationship
    intent: Get the review screenshot ID linked to a subscription
    question: Which review screenshot ID is attached to my subscription?
  - id: subscriptions_appStoreReviewScreenshot_getToOneRelated
    intent: Get the App Review screenshot for a subscription
    question: How do I see the screenshot I uploaded for App Review on a subscription?
  - id: subscriptions_images_getToManyRelationship
    intent: List image IDs linked to a subscription
    question: Which promotional image IDs are linked to my subscription?
  - id: subscriptions_images_getToManyRelated
    intent: List a subscription's promotional images
    question: How do I see all the promotional images uploaded for a subscription?
  phrasing_ops: 28
  slug: ios-subscriptions-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The SubscriptionSubmissions API from iOS — 1 operation(s) for subscriptionsubmissions.
  name: iOS SubscriptionSubmissions API
  phrasing_intents:
  - id: subscriptionSubmissions_createInstance
    intent: Submit a subscription for App Review
    question: What call sends an auto-renewable subscription to App Review?
  phrasing_ops: 1
  slug: ios-subscriptionsubmissions-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The Territories API from iOS — 1 operation(s) for territories.
  name: iOS Territories API
  phrasing_intents:
  - id: territories_getCollection
    intent: List App Store territories
    question: Which countries and regions does the App Store operate in?
  phrasing_ops: 1
  slug: ios-territories-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The TerritoryAvailabilities API from iOS — 1 operation(s) for territoryavailabilities.
  name: iOS TerritoryAvailabilities API
  phrasing_intents:
  - id: territoryAvailabilities_updateInstance
    intent: Change an app's availability in a territory
    question: How do I make my app available or unavailable in one specific country?
  phrasing_ops: 1
  slug: ios-territoryavailabilities-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The UserInvitations API from iOS — 4 operation(s) for userinvitations.
  name: iOS UserInvitations API
  phrasing_intents:
  - id: userInvitations_getCollection
    intent: List pending team invitations
    question: Who have I invited to my App Store Connect team that hasn't accepted yet?
  - id: userInvitations_createInstance
    intent: Invite a user to the team
    question: How do I invite a new developer to my team with specific roles?
  - id: userInvitations_getInstance
    intent: Get a team invitation
    question: When does a specific pending invitation expire?
  - id: userInvitations_deleteInstance
    intent: Cancel a team invitation
    question: Can I revoke an invitation I sent to the wrong person?
  - id: userInvitations_visibleApps_getToManyRelationship
    intent: List app IDs visible to an invited user
    question: Which app IDs will an invited user be able to see?
  - id: userInvitations_visibleApps_getToManyRelated
    intent: List apps an invited user will have access to
    question: Which apps, by name and bundle ID, will this invitee be able to access?
  phrasing_ops: 6
  slug: ios-userinvitations-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The Users API from iOS — 4 operation(s) for users.
  name: iOS Users API
  phrasing_intents:
  - id: users_getCollection
    intent: List team users
    question: Who are the users on my App Store Connect team?
  - id: users_getInstance
    intent: Get a team user
    question: What roles and details does a specific team user have?
  - id: users_updateInstance
    intent: Update a team user
    question: How do I change a team member's roles?
  - id: users_deleteInstance
    intent: Remove a user from the team
    question: How do I remove someone from my App Store Connect team?
  - id: users_visibleApps_getToManyRelationship
    intent: List app IDs a user can see
    question: How do I get just the IDs of apps a user has access to?
  - id: users_visibleApps_createToManyRelationship
    intent: Grant a user access to apps
    question: How do I give a team member access to more apps?
  - id: users_visibleApps_replaceToManyRelationship
    intent: Replace the apps a user can see
    question: How do I set exactly which apps a user can access?
  - id: users_visibleApps_deleteToManyRelationship
    intent: Revoke a user's access to apps
    question: How do I stop a team member from seeing certain apps?
  phrasing_ops: 9
  slug: ios-users-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The WebhookPings API from iOS — 1 operation(s) for webhookpings.
  name: iOS WebhookPings API
  phrasing_intents:
  - id: webhookPings_createInstance
    intent: Send a test ping to a webhook
    question: Is there a way to send a test ping to my App Store Connect webhook?
  phrasing_ops: 1
  slug: ios-webhookpings-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The Webhooks API from iOS — 4 operation(s) for webhooks.
  name: iOS Webhooks API
  phrasing_intents:
  - id: webhooks_createInstance
    intent: Create an App Store Connect webhook
    question: How do I register a webhook so App Store Connect notifies my server about events?
  - id: webhooks_getInstance
    intent: Get a webhook's configuration
    question: What URL and event types is one of my webhooks set up for?
  - id: webhooks_updateInstance
    intent: Update a webhook
    question: Can I change a webhook's URL, secret or event types?
  - id: webhooks_deleteInstance
    intent: Delete a webhook
    question: How do I stop App Store Connect from sending events to a webhook permanently?
  - id: webhooks_deliveries_getToManyRelationship
    intent: List delivery IDs for a webhook
    question: Which delivery attempt IDs have been recorded for a webhook?
  - id: webhooks_deliveries_getToManyRelated
    intent: Review a webhook's delivery history
    question: Which webhook notifications failed to reach my server?
  phrasing_ops: 6
  slug: ios-webhooks-api
- baseURL: https://api.appstoreconnect.apple.com
  baseurl_source: declared
  description: The WinBackOffers API from iOS — 4 operation(s) for winbackoffers.
  name: iOS WinBackOffers API
  phrasing_intents:
  - id: winBackOffers_createInstance
    intent: Create a win-back offer
    question: How do I create a win-back offer to bring lapsed subscribers back?
  - id: winBackOffers_getInstance
    intent: Get a win-back offer
    question: What eligibility rules and dates does one of my win-back offers have?
  - id: winBackOffers_updateInstance
    intent: Update a win-back offer
    question: Can I change the end date or priority of a win-back offer?
  - id: winBackOffers_deleteInstance
    intent: Delete a win-back offer
    question: Can I delete a win-back offer I set up by mistake?
  - id: winBackOffers_prices_getToManyRelationship
    intent: List price IDs for a win-back offer
    question: Which price IDs are attached to my win-back offer?
  - id: winBackOffers_prices_getToManyRelated
    intent: List a win-back offer's prices by territory
    question: What does my win-back offer cost in each country?
  phrasing_ops: 6
  slug: ios-winbackoffers-api
- baseURL: https://api.storekit.itunes.apple.com
  baseurl_source: declared
  description: The Analytics Reports API from iOS — 3 operation(s) for analytics reports.
  name: iOS Analytics Reports API
  phrasing_intents:
  - id: analyticsReports_getInstance
    intent: Get an analytics report
    question: What category and name does an App Store analytics report have?
  - id: analyticsReports_instances_getToManyRelationship
    intent: List IDs of an analytics report's instances
    question: Can I get just the instance IDs for an analytics report?
  - id: analyticsReports_instances_getToManyRelated
    intent: List instances of an analytics report
    question: Which daily, weekly or monthly instances of an analytics report are available?
  phrasing_ops: 3
  slug: ios-analytics-reports-api
- baseURL: https://api.storekit.itunes.apple.com
  baseurl_source: declared
  description: The App Categories API from iOS — 6 operation(s) for app categories.
  name: iOS App Categories API
  phrasing_intents:
  - id: appCategories_getCollection
    intent: List App Store categories
    question: What categories can I put my app in on the App Store?
  - id: appCategories_getInstance
    intent: Get an App Store category
    question: What platforms does a specific App Store category support?
  - id: appCategories_parent_getToOneRelationship
    intent: Get the parent category ID
    question: Can I get just the parent category ID of a subcategory?
  - id: appCategories_parent_getToOneRelated
    intent: Get a category's parent category
    question: What top-level category does a subcategory like Puzzle sit under?
  - id: appCategories_subcategories_getToManyRelationship
    intent: List subcategory IDs of a category
    question: Can I get just the subcategory IDs of a category?
  - id: appCategories_subcategories_getToManyRelated
    intent: List a category's subcategories
    question: What subcategories exist under a top-level App Store category?
  phrasing_ops: 6
  slug: ios-app-categories-api
- baseURL: https://api.storekit.itunes.apple.com
  baseurl_source: declared
  description: The App Events API from iOS — 4 operation(s) for app events.
  name: iOS App Events API
  phrasing_intents:
  - id: appEvents_createInstance
    intent: Create an in-app event
    question: How do I create an in-app event to feature on the App Store?
  - id: appEvents_getInstance
    intent: Get an in-app event
    question: What are the dates, badge and status of one in-app event?
  - id: appEvents_updateInstance
    intent: Update an in-app event
    question: How do I change the schedule or badge of an existing in-app event?
  - id: appEvents_deleteInstance
    intent: Delete an in-app event
    question: How do I delete an in-app event I don't want to run?
  - id: appEvents_localizations_getToManyRelationship
    intent: List localization IDs for an in-app event
    question: Which localization IDs exist for an in-app event?
  - id: appEvents_localizations_getToManyRelated
    intent: List an in-app event's localized text and media
    question: What names and descriptions have I written for an in-app event in each language?
  phrasing_ops: 6
  slug: ios-app-events-api
- baseURL: https://api.storekit.itunes.apple.com
  baseurl_source: declared
  description: The App Previews API from iOS — 2 operation(s) for app previews.
  name: iOS App Previews API
  phrasing_intents:
  - id: appPreviews_createInstance
    intent: Upload an app preview video
    question: How do I upload an app preview video to App Store Connect?
  - id: appPreviews_getInstance
    intent: Get an app preview
    question: Can I check an app preview by ID?
  - id: appPreviews_updateInstance
    intent: Update an app preview
    question: What's the way to update an existing app preview?
  - id: appPreviews_deleteInstance
    intent: Delete an app preview
    question: Can I delete an app preview video?
  phrasing_ops: 4
  slug: ios-app-previews-api
- baseURL: https://api.storekit.itunes.apple.com
  baseurl_source: declared
  description: The Beta Testers API from iOS — 9 operation(s) for beta testers.
  name: iOS Beta Testers API
  phrasing_intents:
  - id: betaTesters_getCollection
    intent: List TestFlight beta testers
    question: Who are all the TestFlight beta testers on my account?
  - id: betaTesters_createInstance
    intent: Invite a new TestFlight beta tester
    question: How do I add a new external tester to TestFlight?
  - id: betaTesters_getInstance
    intent: Get a beta tester's details
    question: What name, email and invite type does a specific beta tester have?
  - id: betaTesters_deleteInstance
    intent: Remove a beta tester from TestFlight
    question: How do I completely remove someone from TestFlight testing?
  - id: betaTesters_apps_getToManyRelationship
    intent: List app IDs a beta tester can test
    question: Which app IDs is a beta tester linked to?
  - id: betaTesters_apps_deleteToManyRelationship
    intent: Remove a beta tester's access to apps
    question: How do I stop a tester from testing one of my apps without deleting them?
  - id: betaTesters_apps_getToManyRelated
    intent: List the apps a beta tester can test
    question: Which of my apps can a particular beta tester try out?
  - id: betaTesters_betaGroups_getToManyRelationship
    intent: List beta group IDs a tester belongs to
    question: Which beta group IDs is a tester a member of?
  phrasing_ops: 16
  slug: ios-beta-testers-api
- baseURL: https://api.storekit.itunes.apple.com
  baseurl_source: declared
  description: The Merchant IDs API from iOS — 4 operation(s) for merchant ids.
  name: iOS Merchant IDs API
  phrasing_intents:
  - id: merchantIds_getCollection
    intent: List Apple Pay merchant IDs
    question: What Apple Pay merchant identifiers are registered on my account?
  - id: merchantIds_createInstance
    intent: Register an Apple Pay merchant ID
    question: How do I register a new merchant identifier for Apple Pay?
  - id: merchantIds_getInstance
    intent: Get an Apple Pay merchant ID
    question: What name and identifier does a particular merchant ID have?
  - id: merchantIds_updateInstance
    intent: Rename an Apple Pay merchant ID
    question: How do I change the description of an existing merchant ID?
  - id: merchantIds_deleteInstance
    intent: Delete an Apple Pay merchant ID
    question: Can I delete a merchant identifier I no longer process payments with?
  - id: merchantIds_certificates_getToManyRelationship
    intent: List certificate IDs for a merchant ID
    question: Which certificate IDs are linked to my merchant ID?
  - id: merchantIds_certificates_getToManyRelated
    intent: List Apple Pay certificates for a merchant ID
    question: Which payment processing certificates belong to my merchant ID?
  phrasing_ops: 7
  slug: ios-merchant-ids-api
- baseURL: https://api.storekit.itunes.apple.com
  baseurl_source: declared
  description: The Subscription groups API from iOS — 6 operation(s) for subscription groups.
  name: iOS Subscription groups API
  phrasing_intents:
  - id: subscriptionGroups_createInstance
    intent: Create a subscription group
    question: How do I create a new subscription group for my auto-renewable subscriptions?
  - id: subscriptionGroups_getInstance
    intent: Get a subscription group
    question: What's the reference name of one subscription group?
  - id: subscriptionGroups_updateInstance
    intent: Rename or update a subscription group
    question: How do I rename a subscription group's reference name?
  - id: subscriptionGroups_deleteInstance
    intent: Delete a subscription group
    question: How do I delete a subscription group I never used?
  - id: subscriptionGroups_subscriptionGroupLocalizations_getToManyRelationship
    intent: List localization IDs for a subscription group
    question: Which localization IDs are attached to a subscription group?
  - id: subscriptionGroups_subscriptionGroupLocalizations_getToManyRelated
    intent: List a subscription group's localized names
    question: What display names and custom app names have I set for a subscription group in each language?
  - id: subscriptionGroups_subscriptions_getToManyRelationship
    intent: List subscription IDs in a group
    question: Which subscription IDs are in a given subscription group?
  - id: subscriptionGroups_subscriptions_getToManyRelated
    intent: List the subscriptions in a group
    question: What subscriptions, with their durations and states, are in one of my subscription groups?
  phrasing_ops: 8
  slug: ios-subscription-groups-api
- baseURL: https://api.storekit.itunes.apple.com
  baseurl_source: declared
  description: The Webhook Deliveries API from iOS — 1 operation(s) for webhook deliveries.
  name: iOS Webhook Deliveries API
  phrasing_intents:
  - id: webhookDeliveries_createInstance
    intent: Redeliver a webhook event
    question: How do I resend a webhook delivery that failed?
  phrasing_ops: 1
  slug: ios-webhook-deliveries-api
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
artifact_total: 605
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
- group: company
  title: ''
  type: Website
  url: https://www.apple.com/
- group: other
  href: https://artifacts.apis.io/ios/capabilities/ios-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/ios-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/ios/overview
- group: agent
  href: https://artifacts.apis.io/ios/agentic-access/ios-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ios-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/ios/security/ios-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/ios-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/ios/security/ios-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ios-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/ios/authentication/ios-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ios-authentication.yml
- group: design
  href: https://artifacts.apis.io/ios/arazzo/ios-create-app-store-version-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/ios-create-app-store-version-workflow.yml
- group: design
  href: https://artifacts.apis.io/ios/arazzo/ios-create-beta-group-assign-build-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/ios-create-beta-group-assign-build-workflow.yml
- group: design
  href: https://artifacts.apis.io/ios/arazzo/ios-create-in-app-purchase-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/ios-create-in-app-purchase-workflow.yml
- group: design
  href: https://artifacts.apis.io/ios/arazzo/ios-create-signing-certificate-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/ios-create-signing-certificate-workflow.yml
- group: design
  href: https://artifacts.apis.io/ios/arazzo/ios-create-subscription-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/ios-create-subscription-workflow.yml
- group: design
  href: https://artifacts.apis.io/ios/arazzo/ios-enable-bundle-id-capability-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/ios-enable-bundle-id-capability-workflow.yml
- group: design
  href: https://artifacts.apis.io/ios/arazzo/ios-invite-beta-tester-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/ios-invite-beta-tester-workflow.yml
- group: design
  href: https://artifacts.apis.io/ios/arazzo/ios-notify-testers-new-build-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/ios-notify-testers-new-build-workflow.yml
- group: design
  href: https://artifacts.apis.io/ios/arazzo/ios-register-provisioning-profile-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/ios-register-provisioning-profile-workflow.yml
- group: design
  href: https://artifacts.apis.io/ios/arazzo/ios-respond-to-customer-review-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/ios-respond-to-customer-review-workflow.yml
- group: design
  href: https://artifacts.apis.io/ios/arazzo/ios-submit-build-for-beta-review-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/ios-submit-build-for-beta-review-workflow.yml
- group: design
  href: https://artifacts.apis.io/ios/arazzo/ios-submit-version-for-review-workflow.yml
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
- has_sources: false
  method: generated
  name: Ios Finops
  primary_unit: ''
  service_category: ''
  slug: ios-finops
  template: true
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
overview: 'iOS publishes 199 API contracts indexed on the [APIs.io](https://apis.io/) network, including App Store Server Notifications, AccessibilityDeclarations API, Actors API, and 196 more. Tagged areas include iOS, Apple, Mobile, App Store, and Push Notifications.


  The iOS catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  iOS''s developer surface includes authentication, developer portal, documentation, API reference, signup flow, pricing, engineering blog, and 39 more developer resources.'
plans:
- name: Ios Plans Pricing
  plan_count: 5
  slug: ios-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 7
  name: Ios Rate Limits
  slug: ios-rate-limits
rules:
- authorship: unmarked
  effective_rule_count: 48
  extends:
  - spectral:oas
  name: iOS — app store connect rules
  rule_count: 7
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 3
  slug: app-store-connect-rules
- authorship: generated
  effective_rule_count: 28
  extends:
  - spectral:asyncapi
  name: iOS — asyncapi rules
  rule_count: 1
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 1
  slug: ios-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: iOS — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: ios-jsonschema-spectral-rules
score:
  band: strong
  composite: 59.1
  coverage:
    artifact_dirs: 24
    catalog_earned: 55.0
    catalog_earned_first_party: 0.0
    catalog_gap: 60.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 52.6
    contract_governance: 27.3
    contract_quality: 60.4
    developer_ergonomics: 78.6
    discoverability: 57.1
    operational_transparency: 55.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 59.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 192
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/ios/ios-2026-06-20T183533.png
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
- Subscription
- Authentication
- Developer Platform
website: https://www.apple.com/
---
