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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.4
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 12
  human_in_the_loop: 1
  name: Android Agentic Access
  operation_count: 21
  slug: android-agentic-access
  summary_line: 21 operations · 12 acting · 1 human-in-the-loop
api_count: 24
apis:
- description: Core Android framework APIs for building Android applications.
  name: Android Platform APIs
  slug: android-platform-apis
- description: APIs for integrating Google services into Android apps.
  name: Google Play Services APIs
  slug: google-play-services-apis
- description: Firebase SDKs and APIs for Android app development.
  name: Firebase Android APIs
  slug: firebase-android-apis
- description: Add maps, location, and geospatial data to Android applications.
  name: Google Maps Android API
  slug: google-maps-android-api
- description: Suite of libraries to help developers follow best practices.
  name: Android Jetpack APIs
  slug: android-jetpack-apis
- description: Programmatically manage app releases and track analytics.
  name: Google Play Console API
  slug: google-play-console-api
- description: Implement in-app purchases and subscriptions.
  name: Google Play Billing API
  slug: google-play-billing-api
- description: Native Development Kit for implementing parts of Android apps in C and C++ for performance-critical code.
  name: Android NDK APIs
  slug: android-ndk-apis
- description: On-device machine learning APIs for text recognition, face detection, barcode scanning, image labeling, and more.
  name: Google ML Kit Android APIs
  slug: google-ml-kit-android-apis
- description: Health data platform providing a single consolidated interface for accessing user health and fitness data across apps.
  name: Android Health Connect API
  slug: android-health-connect-api
- description: Jetpack library for camera app development with consistent behavior across Android devices.
  name: Android CameraX API
  slug: android-camerax-api
- description: APIs for building applications for Wear OS smartwatches and wearable devices.
  name: Wear OS APIs
  slug: wear-os-apis
- description: APIs for building apps for Android Auto and Android Automotive OS in-vehicle experiences.
  name: Android for Cars APIs
  slug: android-for-cars-apis
- description: Monetize Android apps with in-app advertising including banner, interstitial, native, and rewarded ad formats.
  name: Google AdMob Android API
  slug: google-admob-android-api
- description: Framework APIs for building accessible applications and custom accessibility services.
  name: Android Accessibility APIs
  slug: android-accessibility-apis
- description: APIs and tools for building apps optimized for the television experience using Compose for TV and Leanback.
  name: Android TV APIs
  slug: android-tv-apis
- description: Verify that interactions and server requests come from genuine apps on genuine Android devices.
  name: Google Play Integrity API
  slug: google-play-integrity-api
- description: Unified API for managing user credentials including passkeys, passwords, and federated sign-in.
  name: Android Credential Manager API
  slug: android-credential-manager-api
- description: On-device generative AI powered by Gemini Nano for summarization, proofreading, rewriting, and image description without network connectivity.
  name: Gemini Nano On-Device AI API
  slug: gemini-nano-on-device-ai-api
- description: Cloud-based Gemini API for integrating generative AI capabilities into Android applications.
  name: Gemini Developer API for Android
  slug: gemini-developer-api-for-android
- description: Refund orders placed through Google Play for in-app products and subscriptions.
  name: Android Orders API
  slug: android-orders-api
- description: Manage in-app product and subscription purchases, including verification, acknowledgment, and consumption of purchase tokens.
  name: Android Purchases API
  slug: android-purchases-api
- description: Retrieve user reviews from the Google Play Store and post developer replies to those reviews.
  name: Android Reviews API
  slug: android-reviews-api
- description: Create, manage, and query subscription products and their base plans, offers, and purchase entitlements.
  name: Android Subscriptions API
  slug: android-subscriptions-api
arazzos:
- description: Find a subscription in the catalog, read its current configuration, patch it with a field mask, and verify the change.
  name: Android Audit and Update a Subscription Product
  slug: android-audit-update-subscription-workflow
- description: Cancel a subscriber's auto-renewal from your own support tooling while leaving their paid access intact until expiry.
  name: Android Cancel a Subscription Purchase
  slug: android-cancel-subscription-purchase-workflow
- description: Read a subscriber's current expiry time and push it forward as a goodwill credit or service-outage make-good.
  name: Android Defer a Subscription Renewal
  slug: android-defer-subscription-renewal-workflow
- description: Verify a consumable in-app purchase, acknowledge it, then consume it so the user can buy the item again.
  name: Android Grant and Consume a Consumable Purchase
  slug: android-grant-consumable-purchase-workflow
- description: Create a subscription product with its base plan and listing, then attach an introductory offer and verify it landed.
  name: Android Launch a Subscription Product with an Introductory Offer
  slug: android-launch-subscription-product-workflow
- description: Poll the voided purchases feed for refunds and chargebacks, then re-verify each token so revoked entitlements can be clawed back.
  name: Android Reconcile Voided Purchases
  slug: android-reconcile-voided-purchases-workflow
- description: Resolve a purchase token to its Google Play order id, refund that order, and optionally revoke the entitlement.
  name: Android Refund a Play Order
  slug: android-refund-order-workflow
- description: Pre-flight a subscription product's base plans and offers, then delete it if it was never published, or archive it if it was.
  name: Android Retire an Unpublished Subscription Product
  slug: android-retire-subscription-product-workflow
- description: Page the Play Store review feed, read a single review in full, and post or update the developer reply.
  name: Android Triage and Reply to App Reviews
  slug: android-review-triage-reply-workflow
- description: Immediately terminate a subscriber's access and issue a refund, with a pre-flight read and a post-revoke state confirmation.
  name: Android Revoke and Refund a Subscription Purchase
  slug: android-revoke-subscription-purchase-workflow
- description: Validate a Google Play in-app product purchase token and acknowledge it before the three-day auto-refund window closes.
  name: Android Verify and Acknowledge an In-App Product Purchase
  slug: android-verify-acknowledge-product-purchase-workflow
- description: Validate a new subscription purchase with the Subscriptions v2 API and acknowledge it before the three-day auto-refund window closes.
  name: Android Verify and Acknowledge a Subscription Purchase
  slug: android-verify-acknowledge-subscription-purchase-workflow
artifact_total: 241
collections:
- collection_type: postman
  name: Google Play Developer Orders API
  slug: postman-android-orders-api
- collection_type: postman
  name: Google Play Developer Orders Purchases API
  slug: postman-android-purchases-api
- collection_type: postman
  name: Google Play Developer Orders Reviews API
  slug: postman-android-reviews-api
- collection_type: postman
  name: Google Play Developer Orders Subscriptions API
  slug: postman-android-subscriptions-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Play Developer Orders API
  slug: open-android-orders-api
- collection_type: open
  name: Google Play Developer Orders Purchases API
  slug: open-android-purchases-api
- collection_type: open
  name: Google Play Developer Orders Subscriptions API
  slug: open-android-subscriptions-api
- collection_type: open
  name: Google Play Developer API
  slug: open-google-play-developer-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/android/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/android-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/android-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/android-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/android-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/android-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/android-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/android-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/android-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/android-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/android-google-play-developer-api-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/android-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/android-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/android-lifecycle.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/android-vulnerability-disclosure.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/android-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/android-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/android-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/android-cli.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/android-data-model.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/android_by_google
- group: start
  title: ''
  type: Portal
  url: https://developer.android.com
- group: company
  title: ''
  type: Blog
  url: https://android-developers.googleblog.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/android
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/android
- group: other
  title: ''
  type: X
  url: https://twitter.com/AndroidDev
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/androiddevelopers
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.android.com/get-started/overview
- group: learn
  title: ''
  type: Training
  url: https://developer.android.com/courses
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://developer.android.com/about/versions
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/android/skills
- group: design
  title: ''
  type: Arazzo
  url: arazzo/android-audit-update-subscription-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/android-cancel-subscription-purchase-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/android-defer-subscription-renewal-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/android-grant-consumable-purchase-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/android-launch-subscription-product-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/android-reconcile-voided-purchases-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/android-refund-order-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/android-retire-subscription-product-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/android-review-triage-reply-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/android-revoke-subscription-purchase-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/android-verify-acknowledge-product-purchase-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/android-verify-acknowledge-subscription-purchase-workflow.yml
created: '2024-01-01'
description: Collection of APIs and services available in the Android ecosystem.
examples:
- key_count: 6
  name: Android Acknowledgepurchaseproduct Example
  slug: android-acknowledgepurchaseproduct-example
- key_count: 6
  name: Android Acknowledgepurchasesubscription Example
  slug: android-acknowledgepurchasesubscription-example
- key_count: 6
  name: Android Createsubscription Example
  slug: android-createsubscription-example
- key_count: 6
  name: Android Createsubscriptionoffer Example
  slug: android-createsubscriptionoffer-example
- key_count: 6
  name: Android Deferpurchasesubscription Example
  slug: android-deferpurchasesubscription-example
- key_count: 6
  name: Android Getpurchaseproduct Example
  slug: android-getpurchaseproduct-example
- key_count: 6
  name: Android Getpurchasesubscription Example
  slug: android-getpurchasesubscription-example
- key_count: 6
  name: Android Getreview Example
  slug: android-getreview-example
- key_count: 6
  name: Android Getsubscription Example
  slug: android-getsubscription-example
- key_count: 6
  name: Android Getsubscriptionpurchasev2 Example
  slug: android-getsubscriptionpurchasev2-example
- key_count: 6
  name: Android Listreviews Example
  slug: android-listreviews-example
- key_count: 6
  name: Android Listsubscriptionoffers Example
  slug: android-listsubscriptionoffers-example
- key_count: 6
  name: Android Listsubscriptions Example
  slug: android-listsubscriptions-example
- key_count: 6
  name: Android Listvoidedpurchases Example
  slug: android-listvoidedpurchases-example
- key_count: 6
  name: Android Replytoreview Example
  slug: android-replytoreview-example
- key_count: 6
  name: Android Updatesubscription Example
  slug: android-updatesubscription-example
- key_count: 6
  name: Google Play Developer Base Plan Example
  slug: google-play-developer-base-plan-example
- key_count: 0
  name: Google Play Developer Comment Example
  slug: google-play-developer-comment-example
- key_count: 1
  name: Google Play Developer Developer Comment Example
  slug: google-play-developer-developer-comment-example
- key_count: 11
  name: Google Play Developer Device Metadata Example
  slug: google-play-developer-device-metadata-example
- key_count: 1
  name: Google Play Developer Error Example
  slug: google-play-developer-error-example
- key_count: 4
  name: Google Play Developer Introductory Price Info Example
  slug: google-play-developer-introductory-price-info-example
- key_count: 2
  name: Google Play Developer List Subscription Offers Response Example
  slug: google-play-developer-list-subscription-offers-response-example
- key_count: 2
  name: Google Play Developer List Subscriptions Response Example
  slug: google-play-developer-list-subscriptions-response-example
- key_count: 3
  name: Google Play Developer Money Example
  slug: google-play-developer-money-example
- key_count: 3
  name: Google Play Developer Page Info Example
  slug: google-play-developer-page-info-example
- key_count: 15
  name: Google Play Developer Product Purchase Example
  slug: google-play-developer-product-purchase-example
- key_count: 1
  name: Google Play Developer Product Purchases Acknowledge Request Example
  slug: google-play-developer-product-purchases-acknowledge-request-example
- key_count: 3
  name: Google Play Developer Review Example
  slug: google-play-developer-review-example
- key_count: 1
  name: Google Play Developer Reviews List Response Example
  slug: google-play-developer-reviews-list-response-example
- key_count: 1
  name: Google Play Developer Reviews Reply Request Example
  slug: google-play-developer-reviews-reply-request-example
- key_count: 1
  name: Google Play Developer Reviews Reply Response Example
  slug: google-play-developer-reviews-reply-response-example
- key_count: 2
  name: Google Play Developer Subscription Deferral Info Example
  slug: google-play-developer-subscription-deferral-info-example
- key_count: 5
  name: Google Play Developer Subscription Example
  slug: google-play-developer-subscription-example
- key_count: 4
  name: Google Play Developer Subscription Listing Example
  slug: google-play-developer-subscription-listing-example
- key_count: 9
  name: Google Play Developer Subscription Offer Example
  slug: google-play-developer-subscription-offer-example
- key_count: 3
  name: Google Play Developer Subscription Offer Phase Example
  slug: google-play-developer-subscription-offer-phase-example
- key_count: 20
  name: Google Play Developer Subscription Purchase Example
  slug: google-play-developer-subscription-purchase-example
- key_count: 5
  name: Google Play Developer Subscription Purchase Line Item Example
  slug: google-play-developer-subscription-purchase-line-item-example
- key_count: 11
  name: Google Play Developer Subscription Purchase V2 Example
  slug: google-play-developer-subscription-purchase-v2-example
- key_count: 1
  name: Google Play Developer Subscription Purchases Acknowledge Request Example
  slug: google-play-developer-subscription-purchases-acknowledge-request-example
- key_count: 0
  name: Google Play Developer Subscription Purchases Defer Request Example
  slug: google-play-developer-subscription-purchases-defer-request-example
- key_count: 1
  name: Google Play Developer Subscription Purchases Defer Response Example
  slug: google-play-developer-subscription-purchases-defer-response-example
- key_count: 3
  name: Google Play Developer Subscription Tax And Compliance Settings Example
  slug: google-play-developer-subscription-tax-and-compliance-settings-example
- key_count: 2
  name: Google Play Developer Timestamp Example
  slug: google-play-developer-timestamp-example
- key_count: 2
  name: Google Play Developer Token Pagination Example
  slug: google-play-developer-token-pagination-example
- key_count: 10
  name: Google Play Developer User Comment Example
  slug: google-play-developer-user-comment-example
- key_count: 8
  name: Google Play Developer Voided Purchase Example
  slug: google-play-developer-voided-purchase-example
- key_count: 1
  name: Google Play Developer Voided Purchases List Response Example
  slug: google-play-developer-voided-purchases-list-response-example
features:
- description: Modern declarative UI toolkit for building native Android interfaces with less code and powerful tools.
  name: Jetpack Compose
- description: Design system providing components, layouts, and guidelines for building consistent Android user experiences.
  name: Material Design
- description: Run machine learning models locally on devices with ML Kit and Gemini Nano for privacy-preserving AI features.
  name: On-Device AI
- description: Unified health data platform allowing apps to share and access user health and fitness data with user consent.
  name: Health Connect
- description: Build apps that work seamlessly across phones, tablets, wearables, TVs, and cars with adaptive layouts.
  name: Multi-Device Experiences
- description: Protect apps with Play Integrity API, Credential Manager for passkeys, and built-in security best practices.
  name: App Security
finops:
- name: Android Finops
  service_category: Mobile Development Platform
  slug: android-finops
image: https://www.android.com/static/images/logos/android-logo.png
integrations:
- description: Integrate cloud backend services including authentication, real-time database, cloud messaging, and analytics.
  name: Firebase
- description: Add interactive maps, location services, and geospatial data to Android applications.
  name: Google Maps
- description: Access Google platform capabilities including authentication, location, and Google Drive APIs.
  name: Google Play Services
- description: Deploy custom machine learning models on Android devices for real-time inference with hardware acceleration.
  name: TensorFlow Lite
json_schemas:
- name: Android Application
  property_count: 15
  slug: android-app
- name: BasePlan
  property_count: 6
  slug: android-baseplan
- name: Comment
  property_count: 2
  slug: android-comment
- name: DeveloperComment
  property_count: 2
  slug: android-developercomment
- name: DeviceMetadata
  property_count: 11
  slug: android-devicemetadata
- name: Error
  property_count: 1
  slug: android-error
- name: IntroductoryPriceInfo
  property_count: 4
  slug: android-introductorypriceinfo
- name: ListSubscriptionOffersResponse
  property_count: 2
  slug: android-listsubscriptionoffersresponse
- name: ListSubscriptionsResponse
  property_count: 2
  slug: android-listsubscriptionsresponse
- name: Money
  property_count: 3
  slug: android-money
- name: PageInfo
  property_count: 3
  slug: android-pageinfo
- name: ProductPurchase
  property_count: 15
  slug: android-productpurchase
- name: ProductPurchasesAcknowledgeRequest
  property_count: 1
  slug: android-productpurchasesacknowledgerequest
- name: Review
  property_count: 3
  slug: android-review
- name: ReviewsListResponse
  property_count: 3
  slug: android-reviewslistresponse
- name: ReviewsReplyRequest
  property_count: 1
  slug: android-reviewsreplyrequest
- name: ReviewsReplyResponse
  property_count: 1
  slug: android-reviewsreplyresponse
- name: Subscription
  property_count: 6
  slug: android-subscription
- name: SubscriptionDeferralInfo
  property_count: 2
  slug: android-subscriptiondeferralinfo
- name: SubscriptionListing
  property_count: 4
  slug: android-subscriptionlisting
- name: SubscriptionOffer
  property_count: 9
  slug: android-subscriptionoffer
- name: SubscriptionOfferPhase
  property_count: 3
  slug: android-subscriptionofferphase
- name: SubscriptionPurchase
  property_count: 21
  slug: android-subscriptionpurchase
- name: SubscriptionPurchaseLineItem
  property_count: 5
  slug: android-subscriptionpurchaselineitem
- name: SubscriptionPurchasesAcknowledgeRequest
  property_count: 1
  slug: android-subscriptionpurchasesacknowledgerequest
- name: SubscriptionPurchasesDeferRequest
  property_count: 1
  slug: android-subscriptionpurchasesdeferrequest
- name: SubscriptionPurchasesDeferResponse
  property_count: 1
  slug: android-subscriptionpurchasesdeferresponse
- name: SubscriptionPurchaseV2
  property_count: 11
  slug: android-subscriptionpurchasev2
- name: SubscriptionTaxAndComplianceSettings
  property_count: 3
  slug: android-subscriptiontaxandcompliancesettings
- name: Timestamp
  property_count: 2
  slug: android-timestamp
- name: TokenPagination
  property_count: 2
  slug: android-tokenpagination
- name: UserComment
  property_count: 12
  slug: android-usercomment
- name: VoidedPurchase
  property_count: 8
  slug: android-voidedpurchase
- name: VoidedPurchasesListResponse
  property_count: 3
  slug: android-voidedpurchaseslistresponse
- name: BasePlan
  property_count: 6
  slug: google-play-developer-base-plan
- name: Comment
  property_count: 0
  slug: google-play-developer-comment
- name: DeveloperComment
  property_count: 1
  slug: google-play-developer-developer-comment
- name: DeviceMetadata
  property_count: 11
  slug: google-play-developer-device-metadata
- name: Error
  property_count: 1
  slug: google-play-developer-error
- name: IntroductoryPriceInfo
  property_count: 4
  slug: google-play-developer-introductory-price-info
- name: ListSubscriptionOffersResponse
  property_count: 2
  slug: google-play-developer-list-subscription-offers-response
- name: ListSubscriptionsResponse
  property_count: 2
  slug: google-play-developer-list-subscriptions-response
- name: Money
  property_count: 3
  slug: google-play-developer-money
- name: PageInfo
  property_count: 3
  slug: google-play-developer-page-info
- name: ProductPurchase
  property_count: 15
  slug: google-play-developer-product-purchase
- name: ProductPurchasesAcknowledgeRequest
  property_count: 1
  slug: google-play-developer-product-purchases-acknowledge-request
- name: Review
  property_count: 3
  slug: google-play-developer-review
- name: ReviewsListResponse
  property_count: 1
  slug: google-play-developer-reviews-list-response
- name: ReviewsReplyRequest
  property_count: 1
  slug: google-play-developer-reviews-reply-request
- name: ReviewsReplyResponse
  property_count: 1
  slug: google-play-developer-reviews-reply-response
- name: SubscriptionDeferralInfo
  property_count: 2
  slug: google-play-developer-subscription-deferral-info
- name: SubscriptionListing
  property_count: 4
  slug: google-play-developer-subscription-listing
- name: SubscriptionOfferPhase
  property_count: 3
  slug: google-play-developer-subscription-offer-phase
- name: SubscriptionOffer
  property_count: 9
  slug: google-play-developer-subscription-offer
- name: SubscriptionPurchaseLineItem
  property_count: 5
  slug: google-play-developer-subscription-purchase-line-item
- name: SubscriptionPurchase
  property_count: 20
  slug: google-play-developer-subscription-purchase
- name: SubscriptionPurchaseV2
  property_count: 11
  slug: google-play-developer-subscription-purchase-v2
- name: SubscriptionPurchasesAcknowledgeRequest
  property_count: 1
  slug: google-play-developer-subscription-purchases-acknowledge-request
- name: SubscriptionPurchasesDeferRequest
  property_count: 0
  slug: google-play-developer-subscription-purchases-defer-request
- name: SubscriptionPurchasesDeferResponse
  property_count: 1
  slug: google-play-developer-subscription-purchases-defer-response
- name: Subscription
  property_count: 5
  slug: google-play-developer-subscription
- name: SubscriptionTaxAndComplianceSettings
  property_count: 3
  slug: google-play-developer-subscription-tax-and-compliance-settings
- name: Timestamp
  property_count: 2
  slug: google-play-developer-timestamp
- name: TokenPagination
  property_count: 2
  slug: google-play-developer-token-pagination
- name: UserComment
  property_count: 10
  slug: google-play-developer-user-comment
- name: VoidedPurchase
  property_count: 8
  slug: google-play-developer-voided-purchase
- name: VoidedPurchasesListResponse
  property_count: 1
  slug: google-play-developer-voided-purchases-list-response
json_structures:
- name: Android Structure
  property_count: 0
  slug: android-structure
- name: Google Play Developer Base Plan Structure
  property_count: 6
  slug: google-play-developer-base-plan-structure
- name: Google Play Developer Comment Structure
  property_count: 0
  slug: google-play-developer-comment-structure
- name: Google Play Developer Developer Comment Structure
  property_count: 1
  slug: google-play-developer-developer-comment-structure
- name: Google Play Developer Device Metadata Structure
  property_count: 11
  slug: google-play-developer-device-metadata-structure
- name: Google Play Developer Error Structure
  property_count: 1
  slug: google-play-developer-error-structure
- name: Google Play Developer Introductory Price Info Structure
  property_count: 4
  slug: google-play-developer-introductory-price-info-structure
- name: Google Play Developer List Subscription Offers Response Structure
  property_count: 2
  slug: google-play-developer-list-subscription-offers-response-structure
- name: Google Play Developer List Subscriptions Response Structure
  property_count: 2
  slug: google-play-developer-list-subscriptions-response-structure
- name: Google Play Developer Money Structure
  property_count: 3
  slug: google-play-developer-money-structure
- name: Google Play Developer Page Info Structure
  property_count: 3
  slug: google-play-developer-page-info-structure
- name: Google Play Developer Product Purchase Structure
  property_count: 15
  slug: google-play-developer-product-purchase-structure
- name: Google Play Developer Product Purchases Acknowledge Request Structure
  property_count: 1
  slug: google-play-developer-product-purchases-acknowledge-request-structure
- name: Google Play Developer Review Structure
  property_count: 3
  slug: google-play-developer-review-structure
- name: Google Play Developer Reviews List Response Structure
  property_count: 1
  slug: google-play-developer-reviews-list-response-structure
- name: Google Play Developer Reviews Reply Request Structure
  property_count: 1
  slug: google-play-developer-reviews-reply-request-structure
- name: Google Play Developer Reviews Reply Response Structure
  property_count: 1
  slug: google-play-developer-reviews-reply-response-structure
- name: Google Play Developer Subscription Deferral Info Structure
  property_count: 2
  slug: google-play-developer-subscription-deferral-info-structure
- name: Google Play Developer Subscription Listing Structure
  property_count: 4
  slug: google-play-developer-subscription-listing-structure
- name: Google Play Developer Subscription Offer Phase Structure
  property_count: 3
  slug: google-play-developer-subscription-offer-phase-structure
- name: Google Play Developer Subscription Offer Structure
  property_count: 9
  slug: google-play-developer-subscription-offer-structure
- name: Google Play Developer Subscription Purchase Line Item Structure
  property_count: 5
  slug: google-play-developer-subscription-purchase-line-item-structure
- name: Google Play Developer Subscription Purchase Structure
  property_count: 20
  slug: google-play-developer-subscription-purchase-structure
- name: Google Play Developer Subscription Purchase V2 Structure
  property_count: 11
  slug: google-play-developer-subscription-purchase-v2-structure
- name: Google Play Developer Subscription Purchases Acknowledge Request Structure
  property_count: 1
  slug: google-play-developer-subscription-purchases-acknowledge-request-structure
- name: Google Play Developer Subscription Purchases Defer Request Structure
  property_count: 0
  slug: google-play-developer-subscription-purchases-defer-request-structure
- name: Google Play Developer Subscription Purchases Defer Response Structure
  property_count: 1
  slug: google-play-developer-subscription-purchases-defer-response-structure
- name: Google Play Developer Subscription Structure
  property_count: 5
  slug: google-play-developer-subscription-structure
- name: Google Play Developer Subscription Tax And Compliance Settings Structure
  property_count: 3
  slug: google-play-developer-subscription-tax-and-compliance-settings-structure
- name: Google Play Developer Timestamp Structure
  property_count: 2
  slug: google-play-developer-timestamp-structure
- name: Google Play Developer Token Pagination Structure
  property_count: 2
  slug: google-play-developer-token-pagination-structure
- name: Google Play Developer User Comment Structure
  property_count: 10
  slug: google-play-developer-user-comment-structure
- name: Google Play Developer Voided Purchase Structure
  property_count: 8
  slug: google-play-developer-voided-purchase-structure
- name: Google Play Developer Voided Purchases List Response Structure
  property_count: 1
  slug: google-play-developer-voided-purchases-list-response-structure
jsonld:
- class_count: 0
  name: Android Context
  property_count: 19
  slug: android-context
- class_count: 0
  name: Google Play Developer Context
  property_count: 0
  slug: google-play-developer-context
layout: provider
mcp_servers:
- description: ''
  name: Android MCP Server
  slug: android-mcp-server
modified: '2026-06-20'
name: Android
nav: Providers
network: true
overview: 'Android publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Orders API, Purchases API, Reviews API, and 1 more. Tagged areas include Artificial Intelligence, Android, Automotive, Google, and Machine-Learning.


  The Android catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  Android''s developer surface includes authentication, sandbox, changelog, CLI, developer portal, engineering blog, Stack Overflow tag, and 36 more developer resources.'
plans:
- name: Android Plans Pricing
  plan_count: 6
  slug: android-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 10
  name: Android Rate Limits
  slug: android-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Android API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: android-jsonschema-spectral-rules
- effective_rule_count: 58
  extends:
  - spectral:oas
  name: Android API Rules
  rule_count: 17
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 8
  slug: android-spectral-rules
scopes:
- name: Android Scopes
  scope_count: 1
  slug: android-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 49.8
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 30.3
    contract_quality: 72.5
    developer_ergonomics: 61.9
    discoverability: 90.7
    governance: 30.3
    operational_transparency: 26.3
  previous_composite: 49.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/android/refs/heads/main/screenshots/android-2026-06-20T171952.png
security:
- kind: authentication
  name: Android Authentication
  slug: android-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Android Domain Security
  slug: android-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Android Vulnerability Disclosure
  slug: android-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 18
skills:
- name: adaptive
  slug: adaptive
- name: agp-9-upgrade
  slug: agp-9-upgrade
- name: android-cli
  slug: android-cli
- name: appfunctions
  slug: appfunctions
- name: camera1-to-camerax
  slug: camera1-to-camerax
- name: display-glasses-with-jetpack-compose-glimmer
  slug: display-glasses-with-jetpack-compose-glimmer
- name: edge-to-edge
  slug: edge-to-edge
- name: engage-sdk-integration
  slug: engage-sdk-integration
- name: jetpack-compose-m3
  slug: jetpack-compose-m3
- name: migrate-xml-views-to-jetpack-compose
  slug: migrate-xml-views-to-jetpack-compose
- name: navigation-3
  slug: navigation-3
- name: perfetto-sql
  slug: perfetto-sql
- name: perfetto-trace-analysis
  slug: perfetto-trace-analysis
- name: play-billing-library-version-upgrade
  slug: play-billing-library-version-upgrade
- name: r8-analyzer
  slug: r8-analyzer
- name: styles
  slug: styles
- name: testing-setup
  slug: testing-setup
- name: verified-email
  slug: verified-email
slug: android
tags:
- Artificial Intelligence
- Android
- Automotive
- Google
- Machine-Learning
- Mobile Development
- SDK
- TV
- Wearables
use_cases:
- description: Build native Android applications for phones and tablets using Kotlin, Jetpack, and Material Design.
  name: Mobile App Development
- description: Create watch face designs and health-focused apps for Wear OS smartwatches and fitness devices.
  name: Wearable Apps
- description: Build media, messaging, and navigation apps for Android Auto and Android Automotive OS.
  name: In-Vehicle Experiences
- description: Develop media streaming and entertainment apps optimized for the large-screen TV experience.
  name: TV Entertainment
- description: Implement subscriptions, in-app purchases, and advertising revenue using Google Play Billing and AdMob.
  name: In-App Monetization
website: https://developer.android.com
---
