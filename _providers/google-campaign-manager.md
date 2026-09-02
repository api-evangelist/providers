---
access_model:
  confidence: high
  label: Contact sales · Campaign Manager 360 contract required
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.1
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Google Campaign Manager Agentic Access
  operation_count: 23
  slug: google-campaign-manager-agentic-access
  summary_line: 23 operations · 15 acting
api_count: 1
apis:
- description: Data Transfer v2.0 provides raw, event-level reporting data from Campaign Manager 360 beyond what is available through standard reporting. Data is delivered to Google Cloud Storage as CSV files for ad
  name: Campaign Manager 360 Data Transfer v2.0
  slug: campaign-manager-360-data-transfer-v20
- description: Manage ad configurations within campaigns. Ads define the creative content, delivery schedules, targeting rules, and placement assignments that determine how and where advertising is served to users.
  name: Google Campaign Manager Ads API
  slug: google-campaign-manager-ads-api
- description: Manage advertising campaigns. Campaigns serve as top-level organizational containers that group ads, placements, and creatives under a single advertiser with shared start and end dates, budgets, and t
  name: Google Campaign Manager Campaigns API
  slug: google-campaign-manager-campaigns-api
- description: Manage placements representing ad inventory on publisher sites. Placements define the size, format, pricing, and site location where ads can be served, and generate the ad tags that publishers install
  name: Google Campaign Manager Placements API
  slug: google-campaign-manager-placements-api
- description: Create, configure, and run reports to analyze campaign performance. Reports support multiple types including standard, reach, path to conversion, cross-dimension reach, floodlight, and cross-media rea
  name: Google Campaign Manager Reports API
  slug: google-campaign-manager-reports-api
artifact_total: 230
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Campaign Manager Campaign Manager 360 Ads API
  slug: open-google-campaign-manager-ads-api
- collection_type: open
  name: Google Campaign Manager Campaign Manager 360 Ads Campaigns API
  slug: open-google-campaign-manager-campaigns-api
- collection_type: open
  name: Google Campaign Manager Campaign Manager 360 Ads Placements API
  slug: open-google-campaign-manager-placements-api
- collection_type: open
  name: Google Campaign Manager Campaign Manager 360 Ads Reports API
  slug: open-google-campaign-manager-reports-api
- collection_type: open
  name: Google Campaign Manager Campaign Manager 360 API
  slug: open-google-campaign-manager
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/google-campaign-manager-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-campaign-manager-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-campaign-manager-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-campaign-manager-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-campaign-manager-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-campaign-manager-scopes.yml
- group: other
  title: ''
  type: Discovery
  url: discovery/google-campaign-manager-dfareporting-v5-discovery.json
- group: build
  title: ''
  type: Packages
  url: packages/google-campaign-manager-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/google-campaign-manager-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/google-campaign-manager-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/google-campaign-manager-security.txt
- group: auth
  title: ''
  type: Security
  url: security/google-campaign-manager-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/google-campaign-manager-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/google-campaign-manager-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/google-campaign-manager-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/google-campaign-manager-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/google-campaign-manager-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/google-campaign-manager-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/google-campaign-manager-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/google-campaign-manager-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/google-campaign-manager-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/google-campaign-manager-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/google-campaign-manager-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/google-campaign-manager-finops.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/google-campaign-manager-jsonschema-spectral-rules.yml
- group: build
  title: ''
  type: PostmanCollection
  url: collections/google-campaign-manager.postman_collection.json
- group: build
  title: ''
  type: OpenCollection
  url: collections/google-campaign-manager.opencollection.json
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.google.com/doubleclick-advertisers
- group: docs
  title: ''
  type: Documentation
  url: https://developers.google.com/doubleclick-advertisers
- group: docs
  title: ''
  type: APIReference
  url: https://developers.google.com/doubleclick-advertisers/rest
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/doubleclick-advertisers/getting_started
- group: operate
  title: ''
  type: Support
  url: https://developers.google.com/doubleclick-advertisers/get-support
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.google.com/campaignmanager
- group: operate
  title: ''
  type: Forum
  url: https://groups.google.com/g/dfa-api
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://developers.google.com/doubleclick-advertisers/rel_notes
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googleads
- group: commercial
  title: ''
  type: Pricing
  url: https://marketingplatform.google.com/about/campaign-manager-360/
- group: start
  title: ''
  type: SignUp
  url: https://marketingplatform.google.com/about/campaign-manager-360/
- group: start
  title: ''
  type: Console
  url: https://console.cloud.google.com/apis/library/dfareporting.googleapis.com
- group: start
  title: ''
  type: Portal
  url: https://developers.google.com/
- group: auth
  title: ''
  type: Authentication
  url: https://developers.google.com/identity/protocols/oauth2
- group: company
  title: ''
  type: Blog
  url: https://blog.google/products/marketingplatform/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://policies.google.com/terms
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/googleads/googleads-dfa-reporting-samples
- group: design
  title: ''
  type: JSONLD
  url: json-ld/google-campaign-manager-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/google-campaign-manager-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/google-campaign-manager-vocabulary.yaml
created: '2024-01-01'
description: Campaign Manager 360 is Google's ad-serving, trafficking and measurement platform for advertisers and agencies. Its API — service name dfareporting — lets developers programmatically manage advertisers, campaigns, ads, creatives, placements, floodlight conversion tags and remarketing lists, generate publisher ad tags, and define, run and download standard, reach, path-to-conversion, floodlight and cross-media reach reports. Access is OAuth 2.0 only and every path is scoped to a Campaign Manager 360 user profile. The current version is v5; v4 has been fully sunset. Google publishes a Discovery Document rather than an OpenAPI, plus Data Transfer v2.0 for bulk event-level delivery to Cloud Storage.
examples:
- key_count: 3
  name: Google Campaign Manager Activities Example
  slug: google-campaign-manager-activities-example
- key_count: 2
  name: Google Campaign Manager Ad Blocking Configuration Example
  slug: google-campaign-manager-ad-blocking-configuration-example
- key_count: 16
  name: Google Campaign Manager Ad Example
  slug: google-campaign-manager-ad-example
- key_count: 3
  name: Google Campaign Manager Ads List Response Example
  slug: google-campaign-manager-ads-list-response-example
- key_count: 3
  name: Google Campaign Manager Audience Segment Example
  slug: google-campaign-manager-audience-segment-example
- key_count: 3
  name: Google Campaign Manager Audience Segment Group Example
  slug: google-campaign-manager-audience-segment-group-example
- key_count: 6
  name: Google Campaign Manager Browser Example
  slug: google-campaign-manager-browser-example
- key_count: 19
  name: Google Campaign Manager Campaign Example
  slug: google-campaign-manager-campaign-example
- key_count: 3
  name: Google Campaign Manager Campaigns List Response Example
  slug: google-campaign-manager-campaigns-list-response-example
- key_count: 9
  name: Google Campaign Manager City Example
  slug: google-campaign-manager-city-example
- key_count: 4
  name: Google Campaign Manager Click Through Url Example
  slug: google-campaign-manager-click-through-url-example
- key_count: 2
  name: Google Campaign Manager Click Through Url Suffix Properties Example
  slug: google-campaign-manager-click-through-url-suffix-properties-example
- key_count: 3
  name: Google Campaign Manager Connection Type Example
  slug: google-campaign-manager-connection-type-example
- key_count: 1
  name: Google Campaign Manager Conversion Domain Override Example
  slug: google-campaign-manager-conversion-domain-override-example
- key_count: 5
  name: Google Campaign Manager Country Example
  slug: google-campaign-manager-country-example
- key_count: 7
  name: Google Campaign Manager Creative Assignment Example
  slug: google-campaign-manager-creative-assignment-example
- key_count: 4
  name: Google Campaign Manager Creative Optimization Configuration Example
  slug: google-campaign-manager-creative-optimization-configuration-example
- key_count: 4
  name: Google Campaign Manager Creative Rotation Example
  slug: google-campaign-manager-creative-rotation-example
- key_count: 2
  name: Google Campaign Manager Custom Rich Media Events Example
  slug: google-campaign-manager-custom-rich-media-events-example
- key_count: 4
  name: Google Campaign Manager Date Range Example
  slug: google-campaign-manager-date-range-example
- key_count: 3
  name: Google Campaign Manager Day Part Targeting Example
  slug: google-campaign-manager-day-part-targeting-example
- key_count: 2
  name: Google Campaign Manager Default Click Through Event Tag Properties Example
  slug: google-campaign-manager-default-click-through-event-tag-properties-example
- key_count: 3
  name: Google Campaign Manager Delivery Schedule Example
  slug: google-campaign-manager-delivery-schedule-example
- key_count: 6
  name: Google Campaign Manager Dimension Value Example
  slug: google-campaign-manager-dimension-value-example
- key_count: 1
  name: Google Campaign Manager Error Example
  slug: google-campaign-manager-error-example
- key_count: 2
  name: Google Campaign Manager Event Tag Override Example
  slug: google-campaign-manager-event-tag-override-example
- key_count: 9
  name: Google Campaign Manager File Example
  slug: google-campaign-manager-file-example
- key_count: 2
  name: Google Campaign Manager Frequency Cap Example
  slug: google-campaign-manager-frequency-cap-example
- key_count: 6
  name: Google Campaign Manager Geo Targeting Example
  slug: google-campaign-manager-geo-targeting-example
- key_count: 1
  name: Google Campaign Manager Last Modified Info Example
  slug: google-campaign-manager-last-modified-info-example
- key_count: 2
  name: Google Campaign Manager Lookback Configuration Example
  slug: google-campaign-manager-lookback-configuration-example
- key_count: 3
  name: Google Campaign Manager Measurement Partner Link Example
  slug: google-campaign-manager-measurement-partner-link-example
- key_count: 4
  name: Google Campaign Manager Measurement Partner Wrapping Data Example
  slug: google-campaign-manager-measurement-partner-wrapping-data-example
- key_count: 7
  name: Google Campaign Manager Metro Example
  slug: google-campaign-manager-metro-example
- key_count: 5
  name: Google Campaign Manager Mobile Carrier Example
  slug: google-campaign-manager-mobile-carrier-example
- key_count: 5
  name: Google Campaign Manager Operating System Example
  slug: google-campaign-manager-operating-system-example
- key_count: 5
  name: Google Campaign Manager Operating System Version Example
  slug: google-campaign-manager-operating-system-version-example
- key_count: 2
  name: Google Campaign Manager Optimization Activity Example
  slug: google-campaign-manager-optimization-activity-example
- key_count: 3
  name: Google Campaign Manager Placement Assignment Example
  slug: google-campaign-manager-placement-assignment-example
- key_count: 28
  name: Google Campaign Manager Placement Example
  slug: google-campaign-manager-placement-example
- key_count: 2
  name: Google Campaign Manager Placement Tag Example
  slug: google-campaign-manager-placement-tag-example
- key_count: 2
  name: Google Campaign Manager Placements Generate Tags Response Example
  slug: google-campaign-manager-placements-generate-tags-response-example
- key_count: 3
  name: Google Campaign Manager Placements List Response Example
  slug: google-campaign-manager-placements-list-response-example
- key_count: 3
  name: Google Campaign Manager Platform Example
  slug: google-campaign-manager-platform-example
- key_count: 5
  name: Google Campaign Manager Postal Code Example
  slug: google-campaign-manager-postal-code-example
- key_count: 6
  name: Google Campaign Manager Pricing Schedule Example
  slug: google-campaign-manager-pricing-schedule-example
- key_count: 5
  name: Google Campaign Manager Pricing Schedule Pricing Period Example
  slug: google-campaign-manager-pricing-schedule-pricing-period-example
- key_count: 2
  name: Google Campaign Manager Recipient Example
  slug: google-campaign-manager-recipient-example
- key_count: 6
  name: Google Campaign Manager Region Example
  slug: google-campaign-manager-region-example
- key_count: 3
  name: Google Campaign Manager Report Criteria Example
  slug: google-campaign-manager-report-criteria-example
- key_count: 6
  name: Google Campaign Manager Report Cross Dimension Reach Criteria Example
  slug: google-campaign-manager-report-cross-dimension-reach-criteria-example
- key_count: 2
  name: Google Campaign Manager Report Cross Media Reach Criteria Example
  slug: google-campaign-manager-report-cross-media-reach-criteria-example
- key_count: 4
  name: Google Campaign Manager Report Delivery Example
  slug: google-campaign-manager-report-delivery-example
- key_count: 11
  name: Google Campaign Manager Report Example
  slug: google-campaign-manager-report-example
- key_count: 4
  name: Google Campaign Manager Report Floodlight Criteria Example
  slug: google-campaign-manager-report-floodlight-criteria-example
- key_count: 4
  name: Google Campaign Manager Report Path To Conversion Criteria Example
  slug: google-campaign-manager-report-path-to-conversion-criteria-example
- key_count: 5
  name: Google Campaign Manager Report Reach Criteria Example
  slug: google-campaign-manager-report-reach-criteria-example
- key_count: 7
  name: Google Campaign Manager Report Schedule Example
  slug: google-campaign-manager-report-schedule-example
- key_count: 4
  name: Google Campaign Manager Reports List Response Example
  slug: google-campaign-manager-reports-list-response-example
- key_count: 5
  name: Google Campaign Manager Size Example
  slug: google-campaign-manager-size-example
- key_count: 3
  name: Google Campaign Manager Sorted Dimension Example
  slug: google-campaign-manager-sorted-dimension-example
- key_count: 4
  name: Google Campaign Manager Tag Setting Example
  slug: google-campaign-manager-tag-setting-example
- key_count: 6
  name: Google Campaign Manager Technology Targeting Example
  slug: google-campaign-manager-technology-targeting-example
- key_count: 7
  name: Google Campaign Manager Video Settings Example
  slug: google-campaign-manager-video-settings-example
features:
- description: Create, update, and manage advertising campaigns from inception through completion with full programmatic control.
  name: Campaign Lifecycle Management
- description: Automate the placement and scheduling of ads across publisher sites with targeting and delivery rules.
  name: Ad Trafficking
- description: Generate standard, reach, path-to-conversion, cross-dimension, floodlight, and cross-media reach reports.
  name: Multi-Format Reporting
- description: Automatically generate ad tags for publishers to install on their pages.
  name: Placement Tag Generation
- description: Configure geo-targeting, technology targeting, day-part targeting, and audience segment rules.
  name: Audience Targeting
- description: Track and attribute conversions using Floodlight tags for cross-channel measurement.
  name: Floodlight Conversion Tracking
finops:
- name: Google Campaign Manager Finops
  service_category: API
  slug: google-campaign-manager-finops
image: https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png
integrations:
- description: Combine Campaign Manager 360 data with Google Analytics for unified web analytics and attribution.
  name: Google Analytics
- description: Coordinate campaign management between Campaign Manager 360 and Google Ads platforms.
  name: Google Ads
- description: Integrate with DV360 for programmatic buying and campaign execution.
  name: Display & Video 360
- description: Export raw event-level data via Data Transfer for advanced analysis in BigQuery or other tools.
  name: Google Cloud Storage
- description: Automate Campaign Manager operations using Google Apps Script advanced service.
  name: Google Apps Script
json_schemas:
- name: Activities
  property_count: 3
  slug: google-campaign-manager-activities
- name: AdBlockingConfiguration
  property_count: 2
  slug: google-campaign-manager-ad-blocking-configuration
- name: Ad
  property_count: 16
  slug: google-campaign-manager-ad
- name: AdsListResponse
  property_count: 3
  slug: google-campaign-manager-ads-list-response
- name: AudienceSegmentGroup
  property_count: 3
  slug: google-campaign-manager-audience-segment-group
- name: AudienceSegment
  property_count: 3
  slug: google-campaign-manager-audience-segment
- name: Browser
  property_count: 6
  slug: google-campaign-manager-browser
- name: Campaign
  property_count: 19
  slug: google-campaign-manager-campaign
- name: CampaignsListResponse
  property_count: 3
  slug: google-campaign-manager-campaigns-list-response
- name: City
  property_count: 9
  slug: google-campaign-manager-city
- name: ClickThroughUrl
  property_count: 4
  slug: google-campaign-manager-click-through-url
- name: ClickThroughUrlSuffixProperties
  property_count: 2
  slug: google-campaign-manager-click-through-url-suffix-properties
- name: ConnectionType
  property_count: 3
  slug: google-campaign-manager-connection-type
- name: ConversionDomainOverride
  property_count: 1
  slug: google-campaign-manager-conversion-domain-override
- name: Country
  property_count: 5
  slug: google-campaign-manager-country
- name: CreativeAssignment
  property_count: 7
  slug: google-campaign-manager-creative-assignment
- name: CreativeOptimizationConfiguration
  property_count: 4
  slug: google-campaign-manager-creative-optimization-configuration
- name: CreativeRotation
  property_count: 4
  slug: google-campaign-manager-creative-rotation
- name: CustomRichMediaEvents
  property_count: 2
  slug: google-campaign-manager-custom-rich-media-events
- name: DateRange
  property_count: 4
  slug: google-campaign-manager-date-range
- name: DayPartTargeting
  property_count: 3
  slug: google-campaign-manager-day-part-targeting
- name: DefaultClickThroughEventTagProperties
  property_count: 2
  slug: google-campaign-manager-default-click-through-event-tag-properties
- name: DeliverySchedule
  property_count: 3
  slug: google-campaign-manager-delivery-schedule
- name: DimensionValue
  property_count: 6
  slug: google-campaign-manager-dimension-value
- name: Error
  property_count: 1
  slug: google-campaign-manager-error
- name: EventTagOverride
  property_count: 2
  slug: google-campaign-manager-event-tag-override
- name: File
  property_count: 9
  slug: google-campaign-manager-file
- name: FrequencyCap
  property_count: 2
  slug: google-campaign-manager-frequency-cap
- name: GeoTargeting
  property_count: 6
  slug: google-campaign-manager-geo-targeting
- name: LastModifiedInfo
  property_count: 1
  slug: google-campaign-manager-last-modified-info
- name: LookbackConfiguration
  property_count: 2
  slug: google-campaign-manager-lookback-configuration
- name: MeasurementPartnerLink
  property_count: 3
  slug: google-campaign-manager-measurement-partner-link
- name: MeasurementPartnerWrappingData
  property_count: 4
  slug: google-campaign-manager-measurement-partner-wrapping-data
- name: Metro
  property_count: 7
  slug: google-campaign-manager-metro
- name: MobileCarrier
  property_count: 5
  slug: google-campaign-manager-mobile-carrier
- name: OperatingSystem
  property_count: 5
  slug: google-campaign-manager-operating-system
- name: OperatingSystemVersion
  property_count: 5
  slug: google-campaign-manager-operating-system-version
- name: OptimizationActivity
  property_count: 2
  slug: google-campaign-manager-optimization-activity
- name: PlacementAssignment
  property_count: 3
  slug: google-campaign-manager-placement-assignment
- name: Placement
  property_count: 28
  slug: google-campaign-manager-placement
- name: PlacementTag
  property_count: 2
  slug: google-campaign-manager-placement-tag
- name: PlacementsGenerateTagsResponse
  property_count: 2
  slug: google-campaign-manager-placements-generate-tags-response
- name: PlacementsListResponse
  property_count: 3
  slug: google-campaign-manager-placements-list-response
- name: Platform
  property_count: 3
  slug: google-campaign-manager-platform
- name: PostalCode
  property_count: 5
  slug: google-campaign-manager-postal-code
- name: PricingSchedulePricingPeriod
  property_count: 5
  slug: google-campaign-manager-pricing-schedule-pricing-period
- name: PricingSchedule
  property_count: 6
  slug: google-campaign-manager-pricing-schedule
- name: Recipient
  property_count: 2
  slug: google-campaign-manager-recipient
- name: Region
  property_count: 6
  slug: google-campaign-manager-region
- name: ReportCriteria
  property_count: 3
  slug: google-campaign-manager-report-criteria
- name: ReportCrossDimensionReachCriteria
  property_count: 6
  slug: google-campaign-manager-report-cross-dimension-reach-criteria
- name: ReportCrossMediaReachCriteria
  property_count: 2
  slug: google-campaign-manager-report-cross-media-reach-criteria
- name: ReportDelivery
  property_count: 4
  slug: google-campaign-manager-report-delivery
- name: ReportFloodlightCriteria
  property_count: 4
  slug: google-campaign-manager-report-floodlight-criteria
- name: ReportPathToConversionCriteria
  property_count: 4
  slug: google-campaign-manager-report-path-to-conversion-criteria
- name: ReportReachCriteria
  property_count: 5
  slug: google-campaign-manager-report-reach-criteria
- name: ReportSchedule
  property_count: 7
  slug: google-campaign-manager-report-schedule
- name: Report
  property_count: 11
  slug: google-campaign-manager-report
- name: ReportsListResponse
  property_count: 4
  slug: google-campaign-manager-reports-list-response
- name: Size
  property_count: 5
  slug: google-campaign-manager-size
- name: SortedDimension
  property_count: 3
  slug: google-campaign-manager-sorted-dimension
- name: TagSetting
  property_count: 4
  slug: google-campaign-manager-tag-setting
- name: TechnologyTargeting
  property_count: 6
  slug: google-campaign-manager-technology-targeting
- name: VideoSettings
  property_count: 7
  slug: google-campaign-manager-video-settings
json_structures:
- name: Google Campaign Manager Activities Structure
  property_count: 3
  slug: google-campaign-manager-activities-structure
- name: Google Campaign Manager Ad Blocking Configuration Structure
  property_count: 2
  slug: google-campaign-manager-ad-blocking-configuration-structure
- name: Google Campaign Manager Ad Structure
  property_count: 16
  slug: google-campaign-manager-ad-structure
- name: Google Campaign Manager Ads List Response Structure
  property_count: 3
  slug: google-campaign-manager-ads-list-response-structure
- name: Google Campaign Manager Audience Segment Group Structure
  property_count: 3
  slug: google-campaign-manager-audience-segment-group-structure
- name: Google Campaign Manager Audience Segment Structure
  property_count: 3
  slug: google-campaign-manager-audience-segment-structure
- name: Google Campaign Manager Browser Structure
  property_count: 6
  slug: google-campaign-manager-browser-structure
- name: Google Campaign Manager Campaign Structure
  property_count: 19
  slug: google-campaign-manager-campaign-structure
- name: Google Campaign Manager Campaigns List Response Structure
  property_count: 3
  slug: google-campaign-manager-campaigns-list-response-structure
- name: Google Campaign Manager City Structure
  property_count: 9
  slug: google-campaign-manager-city-structure
- name: Google Campaign Manager Click Through Url Structure
  property_count: 4
  slug: google-campaign-manager-click-through-url-structure
- name: Google Campaign Manager Click Through Url Suffix Properties Structure
  property_count: 2
  slug: google-campaign-manager-click-through-url-suffix-properties-structure
- name: Google Campaign Manager Connection Type Structure
  property_count: 3
  slug: google-campaign-manager-connection-type-structure
- name: Google Campaign Manager Conversion Domain Override Structure
  property_count: 1
  slug: google-campaign-manager-conversion-domain-override-structure
- name: Google Campaign Manager Country Structure
  property_count: 5
  slug: google-campaign-manager-country-structure
- name: Google Campaign Manager Creative Assignment Structure
  property_count: 7
  slug: google-campaign-manager-creative-assignment-structure
- name: Google Campaign Manager Creative Optimization Configuration Structure
  property_count: 4
  slug: google-campaign-manager-creative-optimization-configuration-structure
- name: Google Campaign Manager Creative Rotation Structure
  property_count: 4
  slug: google-campaign-manager-creative-rotation-structure
- name: Google Campaign Manager Custom Rich Media Events Structure
  property_count: 2
  slug: google-campaign-manager-custom-rich-media-events-structure
- name: Google Campaign Manager Date Range Structure
  property_count: 4
  slug: google-campaign-manager-date-range-structure
- name: Google Campaign Manager Day Part Targeting Structure
  property_count: 3
  slug: google-campaign-manager-day-part-targeting-structure
- name: Google Campaign Manager Default Click Through Event Tag Properties Structure
  property_count: 2
  slug: google-campaign-manager-default-click-through-event-tag-properties-structure
- name: Google Campaign Manager Delivery Schedule Structure
  property_count: 3
  slug: google-campaign-manager-delivery-schedule-structure
- name: Google Campaign Manager Dimension Value Structure
  property_count: 6
  slug: google-campaign-manager-dimension-value-structure
- name: Google Campaign Manager Error Structure
  property_count: 1
  slug: google-campaign-manager-error-structure
- name: Google Campaign Manager Event Tag Override Structure
  property_count: 2
  slug: google-campaign-manager-event-tag-override-structure
- name: Google Campaign Manager File Structure
  property_count: 9
  slug: google-campaign-manager-file-structure
- name: Google Campaign Manager Frequency Cap Structure
  property_count: 2
  slug: google-campaign-manager-frequency-cap-structure
- name: Google Campaign Manager Geo Targeting Structure
  property_count: 6
  slug: google-campaign-manager-geo-targeting-structure
- name: Google Campaign Manager Last Modified Info Structure
  property_count: 1
  slug: google-campaign-manager-last-modified-info-structure
- name: Google Campaign Manager Lookback Configuration Structure
  property_count: 2
  slug: google-campaign-manager-lookback-configuration-structure
- name: Google Campaign Manager Measurement Partner Link Structure
  property_count: 3
  slug: google-campaign-manager-measurement-partner-link-structure
- name: Google Campaign Manager Measurement Partner Wrapping Data Structure
  property_count: 4
  slug: google-campaign-manager-measurement-partner-wrapping-data-structure
- name: Google Campaign Manager Metro Structure
  property_count: 7
  slug: google-campaign-manager-metro-structure
- name: Google Campaign Manager Mobile Carrier Structure
  property_count: 5
  slug: google-campaign-manager-mobile-carrier-structure
- name: Google Campaign Manager Operating System Structure
  property_count: 5
  slug: google-campaign-manager-operating-system-structure
- name: Google Campaign Manager Operating System Version Structure
  property_count: 5
  slug: google-campaign-manager-operating-system-version-structure
- name: Google Campaign Manager Optimization Activity Structure
  property_count: 2
  slug: google-campaign-manager-optimization-activity-structure
- name: Google Campaign Manager Placement Assignment Structure
  property_count: 3
  slug: google-campaign-manager-placement-assignment-structure
- name: Google Campaign Manager Placement Structure
  property_count: 28
  slug: google-campaign-manager-placement-structure
- name: Google Campaign Manager Placement Tag Structure
  property_count: 2
  slug: google-campaign-manager-placement-tag-structure
- name: Google Campaign Manager Placements Generate Tags Response Structure
  property_count: 2
  slug: google-campaign-manager-placements-generate-tags-response-structure
- name: Google Campaign Manager Placements List Response Structure
  property_count: 3
  slug: google-campaign-manager-placements-list-response-structure
- name: Google Campaign Manager Platform Structure
  property_count: 3
  slug: google-campaign-manager-platform-structure
- name: Google Campaign Manager Postal Code Structure
  property_count: 5
  slug: google-campaign-manager-postal-code-structure
- name: Google Campaign Manager Pricing Schedule Pricing Period Structure
  property_count: 5
  slug: google-campaign-manager-pricing-schedule-pricing-period-structure
- name: Google Campaign Manager Pricing Schedule Structure
  property_count: 6
  slug: google-campaign-manager-pricing-schedule-structure
- name: Google Campaign Manager Recipient Structure
  property_count: 2
  slug: google-campaign-manager-recipient-structure
- name: Google Campaign Manager Region Structure
  property_count: 6
  slug: google-campaign-manager-region-structure
- name: Google Campaign Manager Report Criteria Structure
  property_count: 3
  slug: google-campaign-manager-report-criteria-structure
- name: Google Campaign Manager Report Cross Dimension Reach Criteria Structure
  property_count: 6
  slug: google-campaign-manager-report-cross-dimension-reach-criteria-structure
- name: Google Campaign Manager Report Cross Media Reach Criteria Structure
  property_count: 2
  slug: google-campaign-manager-report-cross-media-reach-criteria-structure
- name: Google Campaign Manager Report Delivery Structure
  property_count: 4
  slug: google-campaign-manager-report-delivery-structure
- name: Google Campaign Manager Report Floodlight Criteria Structure
  property_count: 4
  slug: google-campaign-manager-report-floodlight-criteria-structure
- name: Google Campaign Manager Report Path To Conversion Criteria Structure
  property_count: 4
  slug: google-campaign-manager-report-path-to-conversion-criteria-structure
- name: Google Campaign Manager Report Reach Criteria Structure
  property_count: 5
  slug: google-campaign-manager-report-reach-criteria-structure
- name: Google Campaign Manager Report Schedule Structure
  property_count: 7
  slug: google-campaign-manager-report-schedule-structure
- name: Google Campaign Manager Report Structure
  property_count: 11
  slug: google-campaign-manager-report-structure
- name: Google Campaign Manager Reports List Response Structure
  property_count: 4
  slug: google-campaign-manager-reports-list-response-structure
- name: Google Campaign Manager Size Structure
  property_count: 5
  slug: google-campaign-manager-size-structure
- name: Google Campaign Manager Sorted Dimension Structure
  property_count: 3
  slug: google-campaign-manager-sorted-dimension-structure
- name: Google Campaign Manager Tag Setting Structure
  property_count: 4
  slug: google-campaign-manager-tag-setting-structure
- name: Google Campaign Manager Technology Targeting Structure
  property_count: 6
  slug: google-campaign-manager-technology-targeting-structure
- name: Google Campaign Manager Video Settings Structure
  property_count: 7
  slug: google-campaign-manager-video-settings-structure
jsonld:
- class_count: 0
  name: Google Campaign Manager Context
  property_count: 0
  slug: google-campaign-manager-context
layout: provider
mcp_servers:
- description: CANDIDATE tool surface derived from the Campaign Manager 360 OpenAPI operations in this repo. Google publishes NO Model Context Protocol server for Campaign Manager 360. Nothing below is deployed by t
  name: Google Campaign Manager MCP Server
  slug: google-campaign-manager-mcp-server
modified: '2026-08-13'
name: Google Campaign Manager
nav: Providers
network: true
overview: 'Google Campaign Manager publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Ads API, Campaigns API, Placements API, and 1 more. Tagged areas include Advertising, Analytics, Campaign Management, Digital Marketing, and Reporting.


  The Google Campaign Manager catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Google Campaign Manager''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, support, release notes, and 43 more developer resources.'
plans:
- name: Google Campaign Manager Plans Pricing
  plan_count: 0
  slug: google-campaign-manager-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 3
  name: Google Campaign Manager Rate Limits
  slug: google-campaign-manager-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Google Campaign Manager API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-campaign-manager-jsonschema-spectral-rules
- effective_rule_count: 59
  extends:
  - spectral:oas
  name: Google Campaign Manager API Rules
  rule_count: 18
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 9
  slug: google-campaign-manager-spectral-rules
scopes:
- name: Google Campaign Manager Scopes
  scope_count: 3
  slug: google-campaign-manager-scopes
  summary_line: 3 scopes
score:
  band: strong
  composite: 63.9
  coverage:
    artifact_dirs: 31
    catalog_gap: 46.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 33.3
    contract_quality: 69.9
    developer_ergonomics: 74.4
    discoverability: 61.1
    governance: 33.3
    operational_transparency: 84.2
  previous_composite: 63.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-campaign-manager/refs/heads/main/screenshots/google-campaign-manager-2026-06-20T182032.png
security:
- kind: authentication
  name: Google Campaign Manager Authentication
  slug: google-campaign-manager-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Campaign Manager Domain Security
  slug: google-campaign-manager-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Campaign Manager Vulnerability Disclosure
  slug: google-campaign-manager-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-campaign-manager
tags:
- Advertising
- Analytics
- Campaign Management
- Digital Marketing
- Reporting
- Ad Serving
- Ad Trafficking
- Attribution
- Conversion Tracking
- Marketing
- Media Buying
- Google Marketing Platform
use_cases:
- description: Automate the creation and configuration of advertising campaigns, ads, and placements across publisher inventory.
  name: Programmatic Campaign Setup
- description: Generate and schedule reports to analyze campaign performance, reach, and conversion data.
  name: Performance Reporting
- description: Use path-to-conversion and cross-media reach reports to understand multi-channel advertising impact.
  name: Cross-Channel Attribution
- description: Streamline trafficking workflows including placement creation, tag generation, and creative assignment.
  name: Ad Operations Automation
website: https://developers.google.com/doubleclick-advertisers
---
