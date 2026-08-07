---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 26
  human_in_the_loop: 1
  name: 7Digital Agentic Access
  operation_count: 107
  slug: 7digital-agentic-access
  summary_line: 107 operations · 26 acting · 1 human-in-the-loop
api_count: 23
apis:
- description: Browse, search, chart, and resolve 7digital artists and their releases.
  name: 7digital Artists API
  slug: 7digital-artists-api
- description: Manage purchase baskets, apply vouchers, and complete PayPal checkout.
  name: 7digital Basket API
  slug: 7digital-basket-api
- description: Resolve catalogue entities (artist, release) from 7digital web URLs.
  name: 7digital Catalogue API
  slug: 7digital-catalogue-api
- description: Bulk media transfer for content delivery / catalogue ingestion partners.
  name: 7digital Content Delivery API
  slug: 7digital-content-delivery-api
- description: Download a previously purchased track or release (ZIP or single-file).
  name: 7digital Download Purchases API
  slug: 7digital-download-purchases-api
- description: List 7digital editorial features, banners, and curated content slots.
  name: 7digital Editorial API
  slug: 7digital-editorial-api
- description: Lean-back, ruleset-governed (DMCA, GVL) radio listening sessions.
  name: 7digital Interactive Radio API
  slug: 7digital-interactive-radio-api
- description: Resolve an end-user's country from an IP address.
  name: 7digital IpLookup API
  slug: 7digital-iplookup-api
- description: Stream / preview / subscription play reporting required for licensor royalty calculations.
  name: 7digital Logging API
  slug: 7digital-logging-api
- description: Authorise, list, and inspect devices registered for offline subscription playback.
  name: 7digital Offline Devices API
  slug: 7digital-offline-devices-api
- description: Payment metadata — supported card types and voucher details.
  name: 7digital Payment API
  slug: 7digital-payment-api
- description: Partner-level playlist management — create, list, update and add tracks.
  name: 7digital Playlists API
  slug: 7digital-playlists-api
- description: Browse, search, recommend, and chart 7digital releases (albums, singles, EPs).
  name: 7digital Releases API
  slug: 7digital-releases-api
- description: Log sales, log refunds, and manage a user's locker of purchased content.
  name: 7digital Sales API
  slug: 7digital-sales-api
- description: HLS and HTTP Progressive streaming for previews, catalogue, locker and subscriber playback.
  name: 7digital Streaming API
  slug: 7digital-streaming-api
- description: Notify the platform of subscription state — required for royalty + entitlement.
  name: 7digital Subscriptions API
  slug: 7digital-subscriptions-api
- description: List the curated tag vocabulary used across the 7digital catalogue.
  name: 7digital Tags API
  slug: 7digital-tags-api
- description: List supported countries / sales territories.
  name: 7digital Territories API
  slug: 7digital-territories-api
- description: Search, chart, and look up 7digital track metadata.
  name: 7digital Tracks API
  slug: 7digital-tracks-api
- description: Localised translation bundles for the 7digital catalogue.
  name: 7digital Translations API
  slug: 7digital-translations-api
- description: Per-user account operations — locker, purchases, payment cards, subscriptions, signup.
  name: 7digital User API
  slug: 7digital-user-api
- description: Create and manage user accounts on the partner's behalf.
  name: 7digital User Management API
  slug: 7digital-user-management-api
- description: Partner-scoped user directory operations — find and update users.
  name: 7digital Users API
  slug: 7digital-users-api
artifact_total: 286
collections:
- collection_type: postman
  name: 7digital Artists API
  slug: postman-7digital-artists-api
- collection_type: postman
  name: 7digital Artists Basket API
  slug: postman-7digital-basket-api
- collection_type: postman
  name: 7digital Artists Catalogue API
  slug: postman-7digital-catalogue-api
- collection_type: postman
  name: 7digital Artists Content Delivery API
  slug: postman-7digital-content-delivery-api
- collection_type: postman
  name: 7digital Artists Download Purchases API
  slug: postman-7digital-download-purchases-api
- collection_type: postman
  name: 7digital Artists Editorial API
  slug: postman-7digital-editorial-api
- collection_type: postman
  name: 7digital Artists Interactive Radio API
  slug: postman-7digital-interactive-radio-api
- collection_type: postman
  name: 7digital Artists IpLookup API
  slug: postman-7digital-iplookup-api
- collection_type: postman
  name: 7digital Artists Logging API
  slug: postman-7digital-logging-api
- collection_type: postman
  name: 7digital Artists Offline Devices API
  slug: postman-7digital-offline-devices-api
- collection_type: postman
  name: 7digital Artists Payment API
  slug: postman-7digital-payment-api
- collection_type: postman
  name: 7digital Artists Playlists API
  slug: postman-7digital-playlists-api
- collection_type: postman
  name: 7digital Artists Releases API
  slug: postman-7digital-releases-api
- collection_type: postman
  name: 7digital Artists Sales API
  slug: postman-7digital-sales-api
- collection_type: postman
  name: 7digital Artists Streaming API
  slug: postman-7digital-streaming-api
- collection_type: postman
  name: 7digital Artists Subscriptions API
  slug: postman-7digital-subscriptions-api
- collection_type: postman
  name: 7digital Artists Tags API
  slug: postman-7digital-tags-api
- collection_type: postman
  name: 7digital Artists Territories API
  slug: postman-7digital-territories-api
- collection_type: postman
  name: 7digital Artists Tracks API
  slug: postman-7digital-tracks-api
- collection_type: postman
  name: 7digital Artists Translations API
  slug: postman-7digital-translations-api
- collection_type: postman
  name: 7digital Artists User API
  slug: postman-7digital-user-api
- collection_type: postman
  name: 7digital Artists User Management API
  slug: postman-7digital-user-management-api
- collection_type: postman
  name: 7digital Artists Users API
  slug: postman-7digital-users-api
- collection_type: open
  name: 7digital API
  slug: open-7digital-api
- collection_type: open
  name: 7digital / MassiveMusic Streaming Platform API
  slug: open-7digital-streaming-platform
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/7digital/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/7digital-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/7digital-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/7digital-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://uk.7digital.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.massivemusic.com
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.massivemusic.com/docs/guides-introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.massivemusic.com/reference
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.massivemusic.com/changelog
- group: operate
  title: ''
  type: FAQ
  url: https://docs.massivemusic.com/docs/faq
- group: operate
  title: ''
  type: Support
  url: https://docs.massivemusic.com/docs/support
- group: operate
  title: ''
  type: StatusPage
  url: https://docs.massivemusic.com/docs/health-dashboards
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.massivemusic.com/docs/sla
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/7digital
- group: build
  title: Node.js Client
  type: GitHubRepository
  url: https://github.com/7digital/7digital-api
- group: build
  title: Python Client
  type: GitHubRepository
  url: https://github.com/7digital/python-7digital-api
- group: build
  title: .NET Wrapper
  type: GitHubRepository
  url: https://github.com/7digital/SevenDigital.Api.Wrapper
- group: build
  title: ''
  type: PostmanCollection
  url: https://www.postman.com/speeding-water-232919/7digital-client-test-suite/overview
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: design
  title: ''
  type: SpectralRules
  url: rules/7digital-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/7digital-vocabulary.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/7digital-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/7digital-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/7digital-finops.yml
created: '2026-05-28'
description: 7digital (now operating as MassiveMusic following a corporate pivot toward Songtradr-affiliated business music services) is a B2B music platform that licenses a 100M+ track music catalogue and provides the streaming, download-delivery, royalty-reporting, and content-ingestion infrastructure that powers music services for fitness apps, social-media platforms, background-music providers, interactive-radio products, music stores, and subscription streaming services. The API surface is split into a classic REST API (v1.2) and a modern MassiveMusic Streaming Platform API, both signed with OAuth 1.0 and gated behind a commercial agreement.
examples:
- key_count: 2
  name: Api Artist Details Response Example
  slug: api-artist-details-response-example
- key_count: 6
  name: Api Artist Example
  slug: api-artist-example
- key_count: 5
  name: Api Artist List Response Example
  slug: api-artist-list-response-example
- key_count: 4
  name: Api Basket Example
  slug: api-basket-example
- key_count: 4
  name: Api Basket Item Example
  slug: api-basket-item-example
- key_count: 3
  name: Api Card Registration Example
  slug: api-card-registration-example
- key_count: 5
  name: Api Card Registration Request Example
  slug: api-card-registration-request-example
- key_count: 3
  name: Api Country Example
  slug: api-country-example
- key_count: 6
  name: Api Editorial Item Example
  slug: api-editorial-item-example
- key_count: 2
  name: Api Editorial List Response Example
  slug: api-editorial-list-response-example
- key_count: 2
  name: Api Editorial Response Example
  slug: api-editorial-response-example
- key_count: 6
  name: Api Locker Example
  slug: api-locker-example
- key_count: 6
  name: Api Payment Card Example
  slug: api-payment-card-example
- key_count: 3
  name: Api Price Example
  slug: api-price-example
- key_count: 5
  name: Api Purchase Example
  slug: api-purchase-example
- key_count: 2
  name: Api Release Details Response Example
  slug: api-release-details-response-example
- key_count: 12
  name: Api Release Example
  slug: api-release-example
- key_count: 5
  name: Api Release List Response Example
  slug: api-release-list-response-example
- key_count: 5
  name: Api Subscription Status Example
  slug: api-subscription-status-example
- key_count: 3
  name: Api Tag Example
  slug: api-tag-example
- key_count: 2
  name: Api Tag List Response Example
  slug: api-tag-list-response-example
- key_count: 2
  name: Api Track Details Response Example
  slug: api-track-details-response-example
- key_count: 11
  name: Api Track Example
  slug: api-track-example
- key_count: 5
  name: Api Track List Response Example
  slug: api-track-list-response-example
- key_count: 7
  name: Api User Example
  slug: api-user-example
- key_count: 5
  name: Api User Signup Request Example
  slug: api-user-signup-request-example
- key_count: 4
  name: Api User Update Request Example
  slug: api-user-update-request-example
- key_count: 5
  name: Api Voucher Example
  slug: api-voucher-example
- key_count: 1
  name: Streaming Platform Add Tracks Request Example
  slug: streaming-platform-add-tracks-request-example
- key_count: 5
  name: Streaming Platform Artist Example
  slug: streaming-platform-artist-example
- key_count: 5
  name: Streaming Platform Artist List Response Example
  slug: streaming-platform-artist-list-response-example
- key_count: 2
  name: Streaming Platform Batch Release Request Example
  slug: streaming-platform-batch-release-request-example
- key_count: 3
  name: Streaming Platform Batch Release Response Example
  slug: streaming-platform-batch-release-response-example
- key_count: 2
  name: Streaming Platform Batch Track Request Example
  slug: streaming-platform-batch-track-request-example
- key_count: 3
  name: Streaming Platform Batch Track Response Example
  slug: streaming-platform-batch-track-response-example
- key_count: 4
  name: Streaming Platform Create Playlist Request Example
  slug: streaming-platform-create-playlist-request-example
- key_count: 4
  name: Streaming Platform Create Radio Session Request Example
  slug: streaming-platform-create-radio-session-request-example
- key_count: 5
  name: Streaming Platform Create Subscription Request Example
  slug: streaming-platform-create-subscription-request-example
- key_count: 5
  name: Streaming Platform Create User Request Example
  slug: streaming-platform-create-user-request-example
- key_count: 5
  name: Streaming Platform Credit Item Request Example
  slug: streaming-platform-credit-item-request-example
- key_count: 5
  name: Streaming Platform Device Authorisation Example
  slug: streaming-platform-device-authorisation-example
- key_count: 3
  name: Streaming Platform Device Authorisation Request Example
  slug: streaming-platform-device-authorisation-request-example
- key_count: 2
  name: Streaming Platform Download Url Example
  slug: streaming-platform-download-url-example
- key_count: 6
  name: Streaming Platform Locker Example
  slug: streaming-platform-locker-example
- key_count: 1
  name: Streaming Platform Playback Event Batch Example
  slug: streaming-platform-playback-event-batch-example
- key_count: 4
  name: Streaming Platform Playback Event Example
  slug: streaming-platform-playback-event-example
- key_count: 9
  name: Streaming Platform Playlist Example
  slug: streaming-platform-playlist-example
- key_count: 5
  name: Streaming Platform Playlist List Response Example
  slug: streaming-platform-playlist-list-response-example
- key_count: 6
  name: Streaming Platform Playlist Track Input Example
  slug: streaming-platform-playlist-track-input-example
- key_count: 5
  name: Streaming Platform Radio Session Example
  slug: streaming-platform-radio-session-example
- key_count: 3
  name: Streaming Platform Radio Track Example
  slug: streaming-platform-radio-track-example
- key_count: 3
  name: Streaming Platform Refund Request Example
  slug: streaming-platform-refund-request-example
- key_count: 10
  name: Streaming Platform Release Example
  slug: streaming-platform-release-example
- key_count: 5
  name: Streaming Platform Release List Response Example
  slug: streaming-platform-release-list-response-example
- key_count: 1
  name: Streaming Platform Stream Log Batch Example
  slug: streaming-platform-stream-log-batch-example
- key_count: 6
  name: Streaming Platform Stream Log Example
  slug: streaming-platform-stream-log-example
- key_count: 6
  name: Streaming Platform Subscription Example
  slug: streaming-platform-subscription-example
- key_count: 10
  name: Streaming Platform Track Example
  slug: streaming-platform-track-example
- key_count: 5
  name: Streaming Platform Track List Response Example
  slug: streaming-platform-track-list-response-example
- key_count: 3
  name: Streaming Platform Update Playlist Request Example
  slug: streaming-platform-update-playlist-request-example
- key_count: 3
  name: Streaming Platform Usage Type Example
  slug: streaming-platform-usage-type-example
- key_count: 2
  name: Streaming Platform Usage Type List Response Example
  slug: streaming-platform-usage-type-list-response-example
- key_count: 6
  name: Streaming Platform User Example
  slug: streaming-platform-user-example
features:
- description: Direct licences with major and independent labels. Standard + Enhanced metadata. Pre-cleared Songtradr catalogue (representated catalogue) for synced uses.
  name: 100M+ Track Licensed Catalogue
- description: Free-text search across artists, releases, and tracks; popularity- weighted ranking; alphabetical browse; batch lookup of releases / tracks in a single request.
  name: Catalogue Search + Browse
- description: Preview clips, catalogue streaming, locker streaming, subscription streaming (online + offline), in HLS or HTTP Progressive variants.
  name: HLS and HTTP Progressive Streaming
- description: DMCA and GVL-compliant lean-back radio sessions. Skip-budget and ruleset enforcement on every Get-Next-Track call. Playback events influence subsequent track selection.
  name: Interactive Radio
- description: Subscriber playback gated on a valid subscription record; clientId parameter enforces single-device concurrency.
  name: Subscription Streaming with Device Concurrency
- description: Per-device offline authorisation, encrypted on-device caching, deferred play-event reporting when connectivity is restored.
  name: Offline Mode for Subscriptions
- description: Three logging endpoints (catalogue / preview / subscriber) plus S3-bucket bulk loggers feed Client Usage Reports and Label Reports.
  name: Royalty + Usage Reporting
- description: Log sales in the originating currency, attach purchased content to the user locker, and remove refunds from the sales report.
  name: Sales Credit + Refund Tracking
- description: DDEX ERN message ingestion via SFTP and bulk media transfer for downloading an entire licensed catalogue at 50 req/sec.
  name: Content Delivery (DDEX + SFTP + Media Transfer)
- description: Partner-scoped playlists with optional user association, public / private visibility, descriptions, and per-track source / audioUrl metadata.
  name: Playlist Management API
- description: OAuth 1.0 user accounts with signup, authenticate, and details endpoints. 2-legged (partner) and 3-legged (user-context) flows.
  name: User Account + Authentication
- description: ISO 3166-1 alpha-2 territory codes, IP-to-country resolution for geo-restriction, per-territory pricing in local currency.
  name: Multi-Territory + Multi-Currency
- description: Pre-launch Compliance Testing with Client Success validates that stream logs are correctly attributed to the right usage type before royalty reporting goes live.
  name: Compliance Testing
finops:
- name: 7Digital Finops
  service_category: Music Licensing + Streaming Infrastructure
  slug: 7digital-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/7digital.png
integrations:
- description: Documented integration steps for Warner Music Group catalogue + reporting.
  name: Warner Music Group
- description: Security due diligence + integration steps for Universal Music Group.
  name: Universal Music Group
- description: ERN 3.8 message components for catalogue ingestion via SFTP.
  name: DDEX
- description: PayPal Express Checkout integration for basket purchase completion.
  name: PayPal
- description: S3-bucket bulk loggers for stream / preview / subscription logs and bulk batch submission.
  name: AWS S3
- description: Access to the Songtradr pre-cleared catalogue (the represented catalogue) via the same API surface.
  name: Songtradr
- description: Public Postman workspace with example requests covering authentication and core operations.
  name: Postman
json_schemas:
- name: ArtistDetailsResponse
  property_count: 2
  slug: api-artist-details-response
- name: ArtistListResponse
  property_count: 5
  slug: api-artist-list-response
- name: Artist
  property_count: 6
  slug: api-artist
- name: BasketItem
  property_count: 4
  slug: api-basket-item
- name: Basket
  property_count: 4
  slug: api-basket
- name: CardRegistrationRequest
  property_count: 5
  slug: api-card-registration-request
- name: CardRegistration
  property_count: 3
  slug: api-card-registration
- name: Country
  property_count: 3
  slug: api-country
- name: EditorialItem
  property_count: 6
  slug: api-editorial-item
- name: EditorialListResponse
  property_count: 2
  slug: api-editorial-list-response
- name: EditorialResponse
  property_count: 2
  slug: api-editorial-response
- name: Locker
  property_count: 6
  slug: api-locker
- name: PaymentCard
  property_count: 6
  slug: api-payment-card
- name: Price
  property_count: 3
  slug: api-price
- name: Purchase
  property_count: 5
  slug: api-purchase
- name: ReleaseDetailsResponse
  property_count: 2
  slug: api-release-details-response
- name: ReleaseListResponse
  property_count: 5
  slug: api-release-list-response
- name: Release
  property_count: 12
  slug: api-release
- name: SubscriptionStatus
  property_count: 5
  slug: api-subscription-status
- name: TagListResponse
  property_count: 2
  slug: api-tag-list-response
- name: Tag
  property_count: 3
  slug: api-tag
- name: TrackDetailsResponse
  property_count: 2
  slug: api-track-details-response
- name: TrackListResponse
  property_count: 5
  slug: api-track-list-response
- name: Track
  property_count: 11
  slug: api-track
- name: User
  property_count: 7
  slug: api-user
- name: UserSignupRequest
  property_count: 5
  slug: api-user-signup-request
- name: UserUpdateRequest
  property_count: 4
  slug: api-user-update-request
- name: Voucher
  property_count: 5
  slug: api-voucher
- name: AddTracksRequest
  property_count: 1
  slug: streaming-platform-add-tracks-request
- name: ArtistListResponse
  property_count: 5
  slug: streaming-platform-artist-list-response
- name: Artist
  property_count: 5
  slug: streaming-platform-artist
- name: BatchReleaseRequest
  property_count: 2
  slug: streaming-platform-batch-release-request
- name: BatchReleaseResponse
  property_count: 3
  slug: streaming-platform-batch-release-response
- name: BatchTrackRequest
  property_count: 2
  slug: streaming-platform-batch-track-request
- name: BatchTrackResponse
  property_count: 3
  slug: streaming-platform-batch-track-response
- name: CreatePlaylistRequest
  property_count: 4
  slug: streaming-platform-create-playlist-request
- name: CreateRadioSessionRequest
  property_count: 4
  slug: streaming-platform-create-radio-session-request
- name: CreateSubscriptionRequest
  property_count: 5
  slug: streaming-platform-create-subscription-request
- name: CreateUserRequest
  property_count: 5
  slug: streaming-platform-create-user-request
- name: CreditItemRequest
  property_count: 5
  slug: streaming-platform-credit-item-request
- name: DeviceAuthorisationRequest
  property_count: 3
  slug: streaming-platform-device-authorisation-request
- name: DeviceAuthorisation
  property_count: 5
  slug: streaming-platform-device-authorisation
- name: DownloadUrl
  property_count: 2
  slug: streaming-platform-download-url
- name: Locker
  property_count: 6
  slug: streaming-platform-locker
- name: PlaybackEventBatch
  property_count: 1
  slug: streaming-platform-playback-event-batch
- name: PlaybackEvent
  property_count: 4
  slug: streaming-platform-playback-event
- name: PlaylistListResponse
  property_count: 5
  slug: streaming-platform-playlist-list-response
- name: Playlist
  property_count: 9
  slug: streaming-platform-playlist
- name: PlaylistTrackInput
  property_count: 6
  slug: streaming-platform-playlist-track-input
- name: PlaylistTrack
  property_count: 0
  slug: streaming-platform-playlist-track
- name: RadioSession
  property_count: 5
  slug: streaming-platform-radio-session
- name: RadioTrack
  property_count: 3
  slug: streaming-platform-radio-track
- name: RefundRequest
  property_count: 3
  slug: streaming-platform-refund-request
- name: ReleaseListResponse
  property_count: 5
  slug: streaming-platform-release-list-response
- name: Release
  property_count: 10
  slug: streaming-platform-release
- name: StreamLogBatch
  property_count: 1
  slug: streaming-platform-stream-log-batch
- name: StreamLog
  property_count: 6
  slug: streaming-platform-stream-log
- name: Subscription
  property_count: 6
  slug: streaming-platform-subscription
- name: TrackListResponse
  property_count: 5
  slug: streaming-platform-track-list-response
- name: Track
  property_count: 10
  slug: streaming-platform-track
- name: UpdatePlaylistRequest
  property_count: 3
  slug: streaming-platform-update-playlist-request
- name: UsageTypeListResponse
  property_count: 2
  slug: streaming-platform-usage-type-list-response
- name: UsageType
  property_count: 3
  slug: streaming-platform-usage-type
- name: User
  property_count: 6
  slug: streaming-platform-user
json_structures:
- name: Api Artist Details Response Structure
  property_count: 2
  slug: api-artist-details-response-structure
- name: Api Artist List Response Structure
  property_count: 5
  slug: api-artist-list-response-structure
- name: Api Artist Structure
  property_count: 6
  slug: api-artist-structure
- name: Api Basket Item Structure
  property_count: 4
  slug: api-basket-item-structure
- name: Api Basket Structure
  property_count: 4
  slug: api-basket-structure
- name: Api Card Registration Request Structure
  property_count: 5
  slug: api-card-registration-request-structure
- name: Api Card Registration Structure
  property_count: 3
  slug: api-card-registration-structure
- name: Api Country Structure
  property_count: 3
  slug: api-country-structure
- name: Api Editorial Item Structure
  property_count: 6
  slug: api-editorial-item-structure
- name: Api Editorial List Response Structure
  property_count: 2
  slug: api-editorial-list-response-structure
- name: Api Editorial Response Structure
  property_count: 2
  slug: api-editorial-response-structure
- name: Api Locker Structure
  property_count: 6
  slug: api-locker-structure
- name: Api Payment Card Structure
  property_count: 6
  slug: api-payment-card-structure
- name: Api Price Structure
  property_count: 3
  slug: api-price-structure
- name: Api Purchase Structure
  property_count: 5
  slug: api-purchase-structure
- name: Api Release Details Response Structure
  property_count: 2
  slug: api-release-details-response-structure
- name: Api Release List Response Structure
  property_count: 5
  slug: api-release-list-response-structure
- name: Api Release Structure
  property_count: 12
  slug: api-release-structure
- name: Api Subscription Status Structure
  property_count: 5
  slug: api-subscription-status-structure
- name: Api Tag List Response Structure
  property_count: 2
  slug: api-tag-list-response-structure
- name: Api Tag Structure
  property_count: 3
  slug: api-tag-structure
- name: Api Track Details Response Structure
  property_count: 2
  slug: api-track-details-response-structure
- name: Api Track List Response Structure
  property_count: 5
  slug: api-track-list-response-structure
- name: Api Track Structure
  property_count: 11
  slug: api-track-structure
- name: Api User Signup Request Structure
  property_count: 5
  slug: api-user-signup-request-structure
- name: Api User Structure
  property_count: 7
  slug: api-user-structure
- name: Api User Update Request Structure
  property_count: 4
  slug: api-user-update-request-structure
- name: Api Voucher Structure
  property_count: 5
  slug: api-voucher-structure
- name: Streaming Platform Add Tracks Request Structure
  property_count: 1
  slug: streaming-platform-add-tracks-request-structure
- name: Streaming Platform Artist List Response Structure
  property_count: 5
  slug: streaming-platform-artist-list-response-structure
- name: Streaming Platform Artist Structure
  property_count: 5
  slug: streaming-platform-artist-structure
- name: Streaming Platform Batch Release Request Structure
  property_count: 2
  slug: streaming-platform-batch-release-request-structure
- name: Streaming Platform Batch Release Response Structure
  property_count: 3
  slug: streaming-platform-batch-release-response-structure
- name: Streaming Platform Batch Track Request Structure
  property_count: 2
  slug: streaming-platform-batch-track-request-structure
- name: Streaming Platform Batch Track Response Structure
  property_count: 3
  slug: streaming-platform-batch-track-response-structure
- name: Streaming Platform Create Playlist Request Structure
  property_count: 4
  slug: streaming-platform-create-playlist-request-structure
- name: Streaming Platform Create Radio Session Request Structure
  property_count: 4
  slug: streaming-platform-create-radio-session-request-structure
- name: Streaming Platform Create Subscription Request Structure
  property_count: 5
  slug: streaming-platform-create-subscription-request-structure
- name: Streaming Platform Create User Request Structure
  property_count: 5
  slug: streaming-platform-create-user-request-structure
- name: Streaming Platform Credit Item Request Structure
  property_count: 5
  slug: streaming-platform-credit-item-request-structure
- name: Streaming Platform Device Authorisation Request Structure
  property_count: 3
  slug: streaming-platform-device-authorisation-request-structure
- name: Streaming Platform Device Authorisation Structure
  property_count: 5
  slug: streaming-platform-device-authorisation-structure
- name: Streaming Platform Download Url Structure
  property_count: 2
  slug: streaming-platform-download-url-structure
- name: Streaming Platform Locker Structure
  property_count: 6
  slug: streaming-platform-locker-structure
- name: Streaming Platform Playback Event Batch Structure
  property_count: 1
  slug: streaming-platform-playback-event-batch-structure
- name: Streaming Platform Playback Event Structure
  property_count: 4
  slug: streaming-platform-playback-event-structure
- name: Streaming Platform Playlist List Response Structure
  property_count: 5
  slug: streaming-platform-playlist-list-response-structure
- name: Streaming Platform Playlist Structure
  property_count: 9
  slug: streaming-platform-playlist-structure
- name: Streaming Platform Playlist Track Input Structure
  property_count: 6
  slug: streaming-platform-playlist-track-input-structure
- name: Streaming Platform Playlist Track Structure
  property_count: 0
  slug: streaming-platform-playlist-track-structure
- name: Streaming Platform Radio Session Structure
  property_count: 5
  slug: streaming-platform-radio-session-structure
- name: Streaming Platform Radio Track Structure
  property_count: 3
  slug: streaming-platform-radio-track-structure
- name: Streaming Platform Refund Request Structure
  property_count: 3
  slug: streaming-platform-refund-request-structure
- name: Streaming Platform Release List Response Structure
  property_count: 5
  slug: streaming-platform-release-list-response-structure
- name: Streaming Platform Release Structure
  property_count: 10
  slug: streaming-platform-release-structure
- name: Streaming Platform Stream Log Batch Structure
  property_count: 1
  slug: streaming-platform-stream-log-batch-structure
- name: Streaming Platform Stream Log Structure
  property_count: 6
  slug: streaming-platform-stream-log-structure
- name: Streaming Platform Subscription Structure
  property_count: 6
  slug: streaming-platform-subscription-structure
- name: Streaming Platform Track List Response Structure
  property_count: 5
  slug: streaming-platform-track-list-response-structure
- name: Streaming Platform Track Structure
  property_count: 10
  slug: streaming-platform-track-structure
- name: Streaming Platform Update Playlist Request Structure
  property_count: 3
  slug: streaming-platform-update-playlist-request-structure
- name: Streaming Platform Usage Type List Response Structure
  property_count: 2
  slug: streaming-platform-usage-type-list-response-structure
- name: Streaming Platform Usage Type Structure
  property_count: 3
  slug: streaming-platform-usage-type-structure
- name: Streaming Platform User Structure
  property_count: 6
  slug: streaming-platform-user-structure
jsonld:
- class_count: 28
  name: 7Digital Api Context
  property_count: 69
  slug: 7digital-api-context
- class_count: 35
  name: 7Digital Streaming Platform Context
  property_count: 75
  slug: 7digital-streaming-platform-context
layout: provider
modified: '2026-05-28'
name: 7digital
nav: Providers
network: true
overview: '7digital publishes 23 APIs on the [APIs.io](https://apis.io/) network, including Artists API, Basket API, Catalogue API, and 20 more. Tagged areas include Music, Streaming, Licensing, Catalogue, and B2B.


  The 7digital catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  7digital''s developer surface includes authentication, documentation, getting-started guide, API reference, changelog, FAQ, support, and 17 more developer resources.'
plans:
- name: 7Digital Plans Pricing
  plan_count: 1
  slug: 7digital-plans-pricing
random_paper: 111
rate_limits:
- limit_count: 7
  name: 7Digital Rate Limits
  slug: 7digital-rate-limits
rules:
- name: 7digital API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: 7digital-jsonschema-spectral-rules
- name: 7digital API Rules
  rule_count: 36
  severity_counts:
    error: 17
    hint: 0
    info: 4
    warn: 15
  slug: 7digital-rules
score:
  band: developing
  composite: 48.8
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 28.0
    developer_ergonomics: 45.7
    discoverability: 75.9
    governance: 68.8
    operational_transparency: 68.4
  previous_composite: 48.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 23
      marker_coverage: 100.0
      total: 23
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/7digital/refs/heads/main/screenshots/7digital-2026-06-20T162807.png
security:
- kind: authentication
  name: 7Digital Authentication
  slug: 7digital-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: 7Digital Domain Security
  slug: 7digital-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: 7digital
solutions:
- description: End-to-end recipe for a lean-back retail / hospitality music product.
  name: Background Music Service
- description: End-to-end recipe for a catalogue ingestion + delivery pipeline.
  name: Content Delivery Service
- description: End-to-end recipe for a track / release download storefront.
  name: Download Service
- description: End-to-end recipe for a fitness app with curated music streams.
  name: Fitness Service
- description: End-to-end recipe for a DMCA / GVL-compliant radio station.
  name: Interactive Radio Streaming Service
- description: End-to-end recipe for short-form music with MassiveMusic-managed content delivery.
  name: Social Media Service (Managed)
- description: End-to-end recipe for short-form music with partner-managed content delivery.
  name: Social Media Service (Self-Managed)
- description: End-to-end recipe for a non-subscription catalogue streaming service.
  name: Streaming Service
- description: End-to-end recipe for a subscription-based streaming service with offline mode.
  name: Subscription Streaming Service
tags:
- Music
- Streaming
- Licensing
- Catalogue
- B2B
- Royalty Reporting
- Public APIs
use_cases:
- description: Build a full subscription streaming service on top of licensed catalogue + HLS streaming + subscriber logging.
  name: Music Streaming Service
- description: Stream catalogue tracks to workout sessions, report plays for licensor royalty.
  name: Fitness App with Curated Music
- description: Either MassiveMusic-managed content delivery or self-managed delivery for short-form video music.
  name: Social Media Music
- description: Lean-back music for retail, hospitality, or workplace using catalogue + ruleset-compliant playback.
  name: Background Music Service
- description: Launch a DMCA / GVL-compliant lean-back radio station with skip budgets and playback-event-driven track selection.
  name: Interactive Radio Product
- description: Sell tracks and releases via basket + payment-card + PayPal flows; deliver downloads from the user locker.
  name: Digital Music Storefront
- description: Operate a fully white-labelled subscription music service with offline mode and per-territory licensing.
  name: White-Label Subscription Service
- description: Ingest catalogue via DDEX + SFTP and bulk-download licensed media for upstream distribution.
  name: Content Delivery / Aggregator
website: https://uk.7digital.com
---
