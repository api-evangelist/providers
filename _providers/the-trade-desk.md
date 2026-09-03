---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.5
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: The Trade Desk Agentic Access
  operation_count: 12
  slug: the-trade-desk-agentic-access
  summary_line: 12 operations · 12 acting
api_count: 2
apis:
- description: The Trade Desk Platform API provides REST and GraphQL interfaces for programmatically managing all aspects of programmatic advertising campaigns. Key resources include advertisers, campaigns, ad group
  name: The Trade Desk Platform API
  slug: the-trade-desk-platform-api
- description: The Trade Desk Real-Time Conversions API (formerly the Real-Time Conversion Events API) allows advertisers to send conversion events server-side in real time, enabling more accurate attribution, cross
  name: The Trade Desk Real-Time Conversions API
  slug: the-trade-desk-real-time-conversions-api
- description: The Trade Desk Reporting API provides programmatic access to campaign performance data including impressions, clicks, conversions, spend, win rates, viewability, effective CPM, completion rates, and 2
  name: The Trade Desk Reporting API
  slug: the-trade-desk-reporting-api
- baseURL: https://api.thetradedesk.com/v3
  baseurl_source: declared
  description: The Advertiser API from The Trade Desk — 1 operation(s) for advertiser.
  name: The Trade Desk Advertiser API
  slug: the-trade-desk-advertiser-api
- baseURL: https://api.thetradedesk.com/v3
  baseurl_source: declared
  description: The DeletionOptOut API from The Trade Desk — 3 operation(s) for deletionoptout.
  name: The Trade Desk DeletionOptOut API
  slug: the-trade-desk-deletionoptout-api
- baseURL: https://api.thetradedesk.com/v3
  baseurl_source: declared
  description: The OfflineConversion API from The Trade Desk — 1 operation(s) for offlineconversion.
  name: The Trade Desk OfflineConversion API
  slug: the-trade-desk-offlineconversion-api
- baseURL: https://api.thetradedesk.com/v3
  baseurl_source: declared
  description: The ThirdParty API from The Trade Desk — 1 operation(s) for thirdparty.
  name: The Trade Desk ThirdParty API
  slug: the-trade-desk-thirdparty-api
artifact_total: 57
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: TTD Data Advertiser API
  slug: open-the-trade-desk-advertiser-api
- collection_type: open
  name: TTD Data Advertiser DeletionOptOut API
  slug: open-the-trade-desk-deletionoptout-api
- collection_type: open
  name: TTD Data Advertiser OfflineConversion API
  slug: open-the-trade-desk-offlineconversion-api
- collection_type: open
  name: TTD Data Advertiser ThirdParty API
  slug: open-the-trade-desk-thirdparty-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/the-trade-desk-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/the-trade-desk-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://partner.thetradedesk.com/v3/portal/api/overview
- group: company
  title: ''
  type: Website
  url: https://www.thetradedesk.com
- group: other
  title: ''
  type: EnterpriseAPIs
  url: https://www.thetradedesk.com/us/our-platform/enterprise-apis
- group: start
  title: ''
  type: GettingStarted
  url: https://partner.thetradedesk.com/v3/portal/api/doc/ApiPlatformGetStarted
- group: auth
  title: ''
  type: Authentication
  url: https://partner.thetradedesk.com/v3/portal/api/area/Authentication
- group: operate
  title: ''
  type: RateLimits
  url: https://partner.thetradedesk.com/v3/portal/api/doc/RateLimits
- group: other
  title: ''
  type: AdditionalFees
  url: https://partner.thetradedesk.com/v3/portal/api/area/Additional%20Fees
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.thetradedesk.com/general/privacy
- group: company
  title: ''
  type: Blog
  url: https://www.thetradedesk.com/us/blog
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/the-trade-desk
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/thetradedesk
- group: other
  title: ''
  type: X
  url: https://twitter.com/TheTradeDesk
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/the-trade-desk/refs/heads/main/plans/plans.md
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/the-trade-desk/refs/heads/main/rate-limits/rate-limits.md
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/the-trade-desk/refs/heads/main/finops/finops.md
created: '2026-06-13'
description: The Trade Desk is a global programmatic advertising platform and demand-side platform (DSP) that enables advertisers, agencies, and media buyers to plan, manage, and optimize digital advertising campaigns across connected TV, display, video, audio, native, and mobile channels. The platform provides REST and GraphQL APIs for managing advertisers, campaigns, ad groups, creatives, targeting, bidding strategies, audience data segments, and campaign performance reporting at scale.
examples:
- key_count: 7
  name: Datasubjectrequestadvertiserdata
  slug: DataSubjectRequestAdvertiserData
- key_count: 7
  name: Datasubjectrequestmerchantdata
  slug: DataSubjectRequestMerchantData
- key_count: 7
  name: Datasubjectrequestthirdpartydata
  slug: DataSubjectRequestThirdPartyData
- key_count: 7
  name: Ingestadvertiserdata
  slug: IngestAdvertiserData
- key_count: 7
  name: Ingestofflineconversiondata
  slug: IngestOfflineConversionData
- key_count: 7
  name: Ingestthirdpartydata
  slug: IngestThirdPartyData
graphqls:
- description: The Trade Desk is a demand-side platform for programmatic advertising. Their API covers campaign management, ad groups, targeting segments, creatives, deal management, and reporting across display, vi
  name: The Trade Desk GraphQL API
  slug: the-trade-desk-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/the-trade-desk.png
json_schemas:
- name: AdvertiserData
  property_count: 6
  slug: AdvertiserData
- name: AdvertiserDataItem
  property_count: 15
  slug: AdvertiserDataItem
- name: AdvertiserDataRequest
  property_count: 5
  slug: AdvertiserDataRequest
- name: AdvertiserDataResponseErrorCode
  property_count: 0
  slug: AdvertiserDataResponseErrorCode
- name: AdvertiserDataServerResponse
  property_count: 1
  slug: AdvertiserDataServerResponse
- name: AdvertiserDataServerResponseLine
  property_count: 5
  slug: AdvertiserDataServerResponseLine
- name: AdvertiserDsrFailedLine
  property_count: 6
  slug: AdvertiserDsrFailedLine
- name: AdvertiserDsrRequest
  property_count: 5
  slug: AdvertiserDsrRequest
- name: AdvertiserDsrResponse
  property_count: 1
  slug: AdvertiserDsrResponse
- name: DataOrigin
  property_count: 2
  slug: DataOrigin
- name: DataOriginType
  property_count: 0
  slug: DataOriginType
- name: DsrErrorCode
  property_count: 0
  slug: DsrErrorCode
- name: MerchantDsrFailedLine
  property_count: 5
  slug: MerchantDsrFailedLine
- name: MerchantDsrRequest
  property_count: 4
  slug: MerchantDsrRequest
- name: MerchantDsrResponse
  property_count: 1
  slug: MerchantDsrResponse
- name: OfflineConversionDataItem
  property_count: 34
  slug: OfflineConversionDataItem
- name: OfflineConversionDataRequest
  property_count: 5
  slug: OfflineConversionDataRequest
- name: OfflineConversionDataResponseErrorCode
  property_count: 0
  slug: OfflineConversionDataResponseErrorCode
- name: OfflineConversionDataServerResponse
  property_count: 1
  slug: OfflineConversionDataServerResponse
- name: OfflineConversionDataServerResponseLine
  property_count: 9
  slug: OfflineConversionDataServerResponseLine
- name: PartnerDsrDataItem
  property_count: 13
  slug: PartnerDsrDataItem
- name: PartnerDsrRequestType
  property_count: 0
  slug: PartnerDsrRequestType
- name: RealTimeConversionEventLineItem
  property_count: 5
  slug: RealTimeConversionEventLineItem
- name: RealTimeConversionEventsPrivacySetting
  property_count: 3
  slug: RealTimeConversionEventsPrivacySetting
- name: StringStringValueTuple
  property_count: 2
  slug: StringStringValueTuple
- name: ThirdPartyData
  property_count: 3
  slug: ThirdPartyData
- name: ThirdPartyDataItem
  property_count: 16
  slug: ThirdPartyDataItem
- name: ThirdPartyDataRequest
  property_count: 5
  slug: ThirdPartyDataRequest
- name: ThirdPartyDataResponseErrorCode
  property_count: 0
  slug: ThirdPartyDataResponseErrorCode
- name: ThirdPartyDataServerResponse
  property_count: 1
  slug: ThirdPartyDataServerResponse
- name: ThirdPartyDataServerResponseLine
  property_count: 6
  slug: ThirdPartyDataServerResponseLine
- name: ThirdPartyDsrFailedLine
  property_count: 5
  slug: ThirdPartyDsrFailedLine
- name: ThirdPartyDsrRequest
  property_count: 5
  slug: ThirdPartyDsrRequest
- name: ThirdPartyDsrResponse
  property_count: 1
  slug: ThirdPartyDsrResponse
jsonld:
- class_count: 9
  name: context Context
  property_count: 12
  slug: context
layout: provider
modified: '2026-06-13'
name: The Trade Desk
nav: Providers
network: true
overview: 'The Trade Desk publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Advertiser API, DeletionOptOut API, OfflineConversion API, and 1 more. Tagged areas include Advertising, Programmatic Advertising, DSP, Demand-Side Platform, and Campaign Management.


  The The Trade Desk catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  The Trade Desk''s developer surface includes developer portal, getting-started guide, authentication, engineering blog, and 13 more developer resources.'
random_paper: 18
rules:
- effective_rule_count: 5
  extends: []
  name: The Trade Desk API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: the-trade-desk-jsonschema-spectral-rules
score:
  band: thin
  composite: 34.6
  coverage:
    artifact_dirs: 15
    catalog_gap: 63.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 9.8
    contract_quality: 56.6
    developer_ergonomics: 50.0
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 2.6
  previous_composite: 34.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/the-trade-desk/refs/heads/main/screenshots/the-trade-desk-2026-06-20T195241.png
security:
- kind: domain-security
  name: The Trade Desk Domain Security
  slug: the-trade-desk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: the-trade-desk
tags:
- Advertising
- Programmatic Advertising
- DSP
- Demand-Side Platform
- Campaign Management
- Connected TV
- Digital Advertising
- Marketing
- AdTech
website: https://www.thetradedesk.com
---
