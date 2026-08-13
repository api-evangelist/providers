---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
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
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 88
  human_in_the_loop: 0
  name: Mediamath Agentic Access
  operation_count: 207
  slug: mediamath-agentic-access
  summary_line: 207 operations · 88 acting
api_count: 41
apis:
- description: API for leveraging PMP Direct and Exchange supply sources, enabling programmatic access to private marketplace deals and exchange inventory within the MediaMath Platform.
  name: MediaMath Marketplaces API V2.0
  slug: mediamath-marketplaces-api-v20
- description: API for applying custom bidding algorithms within the MediaMath platform brain, including Campaign Settings configuration and Custom Bid Router for external algorithm invocation during bid opportuniti
  name: MediaMath Bring Your Own Algorithm (BYOA) API
  slug: mediamath-bring-your-own-algorithm-byoa-api
- description: API for ingesting audience event data into the MediaMath Platform via real-time server-side pixel events and batch event uploads. Supports UUID, mobile advertising IDs, and CTV device IDs for cross-de
  name: MediaMath Audience Onboarding API
  slug: mediamath-audience-onboarding-api
- description: API for syncing audience segment data through server-to-server data distribution, supporting UUID-to-segment mappings, SFTP file transfer, and processing log access with Basic Authentication.
  name: MediaMath Server-to-Server Data Distribution API
  slug: mediamath-server-to-server-data-distribution-api
- description: Ad Servers
  name: MediaMath Ad Servers API
  slug: mediamath-ad-servers-api
- description: Advertisers
  name: MediaMath Advertisers API
  slug: mediamath-advertisers-api
- description: Agencies
  name: MediaMath Agencies API
  slug: mediamath-agencies-api
- description: Atomic Creatives
  name: MediaMath Atomic Creatives API
  slug: mediamath-atomic-creatives-api
- description: Audience Vendors
  name: MediaMath Audience Vendors API
  slug: mediamath-audience-vendors-api
- description: Campaign Plans
  name: MediaMath Campaign Plans API
  slug: mediamath-campaign-plans-api
- description: Campaigns
  name: MediaMath Campaigns API
  slug: mediamath-campaigns-api
- description: Campaigns Budget Flights
  name: MediaMath Campaigns Budget Flights API
  slug: mediamath-campaigns-budget-flights-api
- description: Concepts
  name: MediaMath Concepts API
  slug: mediamath-concepts-api
- description: Contracts
  name: MediaMath Contracts API
  slug: mediamath-contracts-api
- description: Creatives
  name: MediaMath Creatives API
  slug: mediamath-creatives-api
- description: Currency Rates
  name: MediaMath Currency Rates API
  slug: mediamath-currency-rates-api
- description: The Datasets API from MediaMath — 10 operation(s) for datasets.
  name: MediaMath Datasets API
  slug: mediamath-datasets-api
- description: Enterprise Controls
  name: MediaMath Enterprise Controls API
  slug: mediamath-enterprise-controls-api
- description: General
  name: MediaMath General API
  slug: mediamath-general-api
- description: Marketplaces
  name: MediaMath Marketplaces API
  slug: mediamath-marketplaces-api
- description: The New Strategy Groups API from MediaMath — 3 operation(s) for new strategy groups.
  name: MediaMath New Strategy Groups API
  slug: mediamath-new-strategy-groups-api
- description: New Strategy Plans
  name: MediaMath New Strategy Plans API
  slug: mediamath-new-strategy-plans-api
- description: Organizations
  name: MediaMath Organizations API
  slug: mediamath-organizations-api
- description: Pixel Bundles
  name: MediaMath Pixel Bundles API
  slug: mediamath-pixel-bundles-api
- description: Pixel Providers
  name: MediaMath Pixel Providers API
  slug: mediamath-pixel-providers-api
- description: Segment Groups
  name: MediaMath Segment Groups API
  slug: mediamath-segment-groups-api
- description: Site Lists
  name: MediaMath Site Lists API
  slug: mediamath-site-lists-api
- description: Strategies
  name: MediaMath Strategies API
  slug: mediamath-strategies-api
- description: Strategy Parameters
  name: MediaMath Strategy Parameters API
  slug: mediamath-strategy-parameters-api
- description: Strategy Templates
  name: MediaMath Strategy Templates API
  slug: mediamath-strategy-templates-api
- description: Supply Sources
  name: MediaMath Supply Sources API
  slug: mediamath-supply-sources-api
- description: Targeting
  name: MediaMath Targeting API
  slug: mediamath-targeting-api
- description: TargetingAttachments
  name: MediaMath Targeting Attachments API
  slug: mediamath-targeting-attachments-api
- description: Targeting Segment Objectives
  name: MediaMath Targeting Segment Objectives API
  slug: mediamath-targeting-segment-objectives-api
- description: Targeting Segments
  name: MediaMath Targeting Segments API
  slug: mediamath-targeting-segments-api
- description: Timezones
  name: MediaMath Timezones API
  slug: mediamath-timezones-api
- description: User Permissions
  name: MediaMath User Permissions API
  slug: mediamath-user-permissions-api
- description: Users
  name: MediaMath Users API
  slug: mediamath-users-api
- description: Vendor Contracts
  name: MediaMath Vendor Contracts API
  slug: mediamath-vendor-contracts-api
- description: Vendors
  name: MediaMath Vendors API
  slug: mediamath-vendors-api
- description: Verticals
  name: MediaMath Verticals API
  slug: mediamath-verticals-api
artifact_total: 378
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mediamath-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mediamath-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mediamath-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/mediamath-scopes.yml
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/mediamath/refs/heads/main/plans/mediamath-plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/mediamath/refs/heads/main/rate-limits/mediamath-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/mediamath/refs/heads/main/finops/mediamath-finops.yml
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.mediamath.com/
- group: auth
  title: ''
  type: Authentication
  url: https://apidocs.mediamath.com/guides
- group: company
  title: ''
  type: Blog
  url: https://devblog.mediamath.com/
- group: operate
  title: ''
  type: Support
  url: https://support.infillion.com/s/submit-a-case
- group: start
  title: ''
  type: Login
  url: https://platform.mediamath.com/
- group: learn
  title: ''
  type: Academy
  url: https://academy.mediamath.com/
created: '2026-06-13'
description: MediaMath (by Infillion) is a programmatic advertising DSP with REST APIs for managing campaigns, targeting, bidding strategies, creative trafficking, audience segments, and performance analytics. The platform provides an API-first composable architecture supporting campaign management, reporting, audience onboarding, marketplaces access, and custom bidding algorithms.
examples:
- key_count: 6
  name: Reporting Post All Dimensions And Metrics Request
  slug: reporting-post-all-dimensions-and-metrics-request
- key_count: 2
  name: Reporting Post All Dimensions And Metrics Response 200
  slug: reporting-post-all-dimensions-and-metrics-response-200
- key_count: 6
  name: Reporting Post Brain Feature Summary Request
  slug: reporting-post-brain-feature-summary-request
- key_count: 2
  name: Reporting Post Brain Feature Summary Response 200
  slug: reporting-post-brain-feature-summary-response-200
- key_count: 6
  name: Reporting Post Brain Feature Value Request
  slug: reporting-post-brain-feature-value-request
- key_count: 2
  name: Reporting Post Brain Feature Value Response 200
  slug: reporting-post-brain-feature-value-response-200
- key_count: 6
  name: Reporting Post Day Part Request
  slug: reporting-post-day-part-request
- key_count: 2
  name: Reporting Post Day Part Response 200
  slug: reporting-post-day-part-response-200
- key_count: 6
  name: Reporting Post Deals Request
  slug: reporting-post-deals-request
- key_count: 2
  name: Reporting Post Deals Response 200
  slug: reporting-post-deals-response-200
- key_count: 6
  name: Reporting Post Performance Hourly Request
  slug: reporting-post-performance-hourly-request
- key_count: 2
  name: Reporting Post Performance Hourly Response 200
  slug: reporting-post-performance-hourly-response-200
- key_count: 6
  name: Reporting Post Performance Request
  slug: reporting-post-performance-request
- key_count: 2
  name: Reporting Post Performance Response 200
  slug: reporting-post-performance-response-200
- key_count: 6
  name: Reporting Post Pixel Loads Request
  slug: reporting-post-pixel-loads-request
- key_count: 2
  name: Reporting Post Pixel Loads Response 200
  slug: reporting-post-pixel-loads-response-200
- key_count: 6
  name: Reporting Post Reach Frequency Request
  slug: reporting-post-reach-frequency-request
- key_count: 2
  name: Reporting Post Reach Frequency Response 200
  slug: reporting-post-reach-frequency-response-200
- key_count: 6
  name: Reporting Post Win Loss Request
  slug: reporting-post-win-loss-request
- key_count: 2
  name: Reporting Post Win Loss Response 200
  slug: reporting-post-win-loss-response-200
finops:
- name: Mediamath Finops
  service_category: ''
  slug: mediamath-finops
graphqls:
- description: MediaMath (now Infillion) is a programmatic advertising platform. Their TerminalOne API covers marketer management, campaigns, strategies, supply sources, audience segments, deals, and performance dat
  name: MediaMath GraphQL API
  slug: mediamath-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mediamath.png
json_schemas:
- name: ad_server_collection
  property_count: 2
  slug: campaigns-ad_server_collection
- name: ad_server_collection_full
  property_count: 2
  slug: campaigns-ad_server_collection_full
- name: ad_server_full
  property_count: 0
  slug: campaigns-ad_server_full
- name: advertiser
  property_count: 20
  slug: campaigns-advertiser_base
- name: advertiser_collection
  property_count: 2
  slug: campaigns-advertiser_collection
- name: advertiser_collection_full
  property_count: 2
  slug: campaigns-advertiser_collection_full
- name: advertiser_create
  property_count: 0
  slug: campaigns-advertiser_create
- name: advertiser_response
  property_count: 2
  slug: campaigns-advertiser_response
- name: advertiser_response_base
  property_count: 0
  slug: campaigns-advertiser_response_base
- name: advertiser_response_extended
  property_count: 2
  slug: campaigns-advertiser_response_extended
- name: advertiser_update
  property_count: 0
  slug: campaigns-advertiser_update
- name: agency
  property_count: 9
  slug: campaigns-agency_base
- name: agency_collection
  property_count: 2
  slug: campaigns-agency_collection
- name: agency_collection_full
  property_count: 2
  slug: campaigns-agency_collection_full
- name: agency_create
  property_count: 0
  slug: campaigns-agency_create
- name: agency_response
  property_count: 2
  slug: campaigns-agency_response
- name: agency_response_base
  property_count: 0
  slug: campaigns-agency_response_base
- name: agency_response_extended
  property_count: 2
  slug: campaigns-agency_response_extended
- name: agency_update
  property_count: 0
  slug: campaigns-agency_update
- name: atomic_creative_create
  property_count: 40
  slug: campaigns-atomic_creative_create
- name: atomic_creative_healthcheck_response
  property_count: 14
  slug: campaigns-atomic_creative_healthcheck_response
- name: atomic_creative_response
  property_count: 50
  slug: campaigns-atomic_creative_response
- name: atomic_creative_response_extended
  property_count: 56
  slug: campaigns-atomic_creative_response_extended
- name: atomic_creative_update
  property_count: 28
  slug: campaigns-atomic_creative_update
- name: atomic_creative_vendor
  property_count: 1
  slug: campaigns-atomic_creative_vendor
- name: attachment_base
  property_count: 10
  slug: campaigns-attachment_base
- name: attachment_create
  property_count: 5
  slug: campaigns-attachment_create
- name: attachment_update
  property_count: 6
  slug: campaigns-attachment_update
- name: audience_segment_short
  property_count: 7
  slug: campaigns-audience_segment_short
- name: audience_segments_group
  property_count: 2
  slug: campaigns-audience_segments_group
- name: audience_target
  property_count: 2
  slug: campaigns-audience_target
- name: audience_vendor
  property_count: 12
  slug: campaigns-audience_vendor
- name: budget_flight_collection
  property_count: 2
  slug: campaigns-budget_flight_collection
- name: budget_flight_collection_full
  property_count: 2
  slug: campaigns-budget_flight_collection_full
- name: budget_flight_full
  property_count: 13
  slug: campaigns-budget_flight_full
- name: bulk errors
  property_count: 0
  slug: campaigns-bulk_errors
- name: campaign_ad_server
  property_count: 5
  slug: campaigns-campaign_ad_server
- name: campaign_attribution
  property_count: 8
  slug: campaigns-campaign_attribution
- name: campaign_base
  property_count: 18
  slug: campaigns-campaign_base
- name: campaign_budget
  property_count: 7
  slug: campaigns-campaign_budget
- name: campaign_budget_flights
  property_count: 6
  slug: campaigns-campaign_budget_flights
- name: campaign_budget_flights_create
  property_count: 4
  slug: campaigns-campaign_budget_flights_create
- name: campaign_bulk
  property_count: 0
  slug: campaigns-campaign_bulk
- name: campaign_collection
  property_count: 2
  slug: campaigns-campaign_collection
- name: campaign_collection_full
  property_count: 2
  slug: campaigns-campaign_collection_full
- name: campaign_create
  property_count: 0
  slug: campaigns-campaign_create
- name: campaign_custom_brain_selection
  property_count: 16
  slug: campaigns-campaign_custom_brain_selection
- name: campaign_dba_collection
  property_count: 2
  slug: campaigns-campaign_dba_collection
- name: campaign_dba_collection_full
  property_count: 2
  slug: campaigns-campaign_dba_collection_full
- name: campaign_duration
  property_count: 2
  slug: campaigns-campaign_duration
- name: campaign_frequency
  property_count: 5
  slug: campaigns-campaign_frequency
- name: campaign_response
  property_count: 2
  slug: campaigns-campaign_full-2
- name: campaign_full
  property_count: 0
  slug: campaigns-campaign_full
- name: campaign_response_extended
  property_count: 2
  slug: campaigns-campaign_full_extended-2
- name: campaign_full_extended
  property_count: 0
  slug: campaigns-campaign_full_extended
- name: campaign_full_with_inherited
  property_count: 0
  slug: campaigns-campaign_full_with_inherited
- name: campaign_goals
  property_count: 4
  slug: campaigns-campaign_goals
- name: campaign_goals_create
  property_count: 0
  slug: campaigns-campaign_goals_create
- name: campaign_identity
  property_count: 3
  slug: campaigns-campaign_identity
- name: campaign_inventory
  property_count: 7
  slug: campaigns-campaign_inventory
- name: campaign_pacing
  property_count: 10
  slug: campaigns-campaign_pacing
- name: campaign_plan
  property_count: 0
  slug: campaigns-campaign_plan
- name: campaign_plan_common
  property_count: 5
  slug: campaigns-campaign_plan_common
- name: campaign_plan_create
  property_count: 4
  slug: campaigns-campaign_plan_create
- name: campaign_plan_update
  property_count: 1
  slug: campaigns-campaign_plan_update
- name: campaign_site_list
  property_count: 15
  slug: campaigns-campaign_site_list
- name: campaign_update
  property_count: 0
  slug: campaigns-campaign_update
- name: campaign_viewability
  property_count: 3
  slug: campaigns-campaign_viewability
- name: campaign_with
  property_count: 2
  slug: campaigns-campaign_with
- name: concept_common
  property_count: 3
  slug: campaigns-concept_common
- name: concept_create
  property_count: 1
  slug: campaigns-concept_create
- name: concept_full
  property_count: 0
  slug: campaigns-concept_response
- name: concept_update
  property_count: 1
  slug: campaigns-concept_update
- name: concept
  property_count: 3
  slug: campaigns-concepts_collection_short
- name: contextual_segment_collection
  property_count: 2
  slug: campaigns-contextual_segment_collection
- name: contextual_segment_collection_full
  property_count: 2
  slug: campaigns-contextual_segment_collection_full
- name: contextual_segment_full
  property_count: 0
  slug: campaigns-contextual_segment_full
- name: contextual_segment_short
  property_count: 7
  slug: campaigns-contextual_segment_short
- name: contract_base
  property_count: 81
  slug: campaigns-contract_base
- name: contract_base_response
  property_count: 0
  slug: campaigns-contract_base_response
- name: contract_collection
  property_count: 2
  slug: campaigns-contract_collection
- name: contract_collection_full
  property_count: 2
  slug: campaigns-contract_collection_full
- name: control_boolean
  property_count: 2
  slug: campaigns-control_boolean
- name: control_decimal
  property_count: 2
  slug: campaigns-control_decimal
- name: control_decimal_array
  property_count: 2
  slug: campaigns-control_decimal_array
- name: control_integer
  property_count: 2
  slug: campaigns-control_integer
- name: control_integer_array
  property_count: 2
  slug: campaigns-control_integer_array
- name: control_string
  property_count: 2
  slug: campaigns-control_string
- name: control_string_array
  property_count: 2
  slug: campaigns-control_string_array
- name: cpm
  property_count: 2
  slug: campaigns-cpm
- name: creative
  property_count: 4
  slug: campaigns-creative_base
- name: creative_response
  property_count: 2
  slug: campaigns-creative_response
- name: currency_rate_collection
  property_count: 2
  slug: campaigns-currency_rate_collection
- name: currency_rate_collection_full
  property_count: 2
  slug: campaigns-currency_rate_collection_full
- name: currency_rate_full
  property_count: 0
  slug: campaigns-currency_rate_full
- name: day_part
  property_count: 4
  slug: campaigns-day_part
- name: dba
  property_count: 0
  slug: campaigns-dba
- name: ''
  property_count: 1
  slug: campaigns-deal
- name: ''
  property_count: 1
  slug: campaigns-deal_group
- name: domain_restriction
  property_count: 2
  slug: campaigns-domain_restriction
- name: duration_base
  property_count: 2
  slug: campaigns-duration_base
- name: enterprise_control
  property_count: 0
  slug: campaigns-enterprise_control
- name: entity_group
  property_count: 8
  slug: campaigns-entity_group
- name: entity_group_advertiser
  property_count: 0
  slug: campaigns-entity_group_advertiser
- name: entity_group_agency
  property_count: 0
  slug: campaigns-entity_group_agency
- name: entity_group_entity
  property_count: 2
  slug: campaigns-entity_group_entity
- name: entity_group_list_item
  property_count: 7
  slug: campaigns-entity_group_list_item
- name: error response
  property_count: 2
  slug: campaigns-error_response
- name: exchange_seat
  property_count: 7
  slug: campaigns-exchange_seat
- name: exchange_seat_extended
  property_count: 1
  slug: campaigns-exchange_seat_extended
- name: forecast
  property_count: 2
  slug: campaigns-forecast
- name: forecast_request
  property_count: 2
  slug: campaigns-forecast_request
- name: frequency_base
  property_count: 3
  slug: campaigns-frequency_base
- name: healthcheck_result
  property_count: 2
  slug: campaigns-healthcheck_result
- name: inventory_base
  property_count: 0
  slug: campaigns-inventory_base
- name: pagination metadata
  property_count: 6
  slug: campaigns-list_metadata
- name: ''
  property_count: 13
  slug: campaigns-location_response
- name: marketplace_create
  property_count: 0
  slug: campaigns-marketplace_create
- name: marketplace_full
  property_count: 23
  slug: campaigns-marketplace_full
- name: marketplace_full_response
  property_count: 0
  slug: campaigns-marketplace_full_response
- name: marketplace_update
  property_count: 0
  slug: campaigns-marketplace_update
- name: new_strategy_group_base
  property_count: 7
  slug: campaigns-new_strategy_group_base
- name: new_strategy_group_collection
  property_count: 2
  slug: campaigns-new_strategy_group_collection
- name: new_strategy_group_collection_full
  property_count: 2
  slug: campaigns-new_strategy_group_collection_full
- name: new_strategy_group_create
  property_count: 0
  slug: campaigns-new_strategy_group_create
- name: new_strategy_group_full
  property_count: 0
  slug: campaigns-new_strategy_group_full
- name: new_strategy_group_list_item
  property_count: 6
  slug: campaigns-new_strategy_group_list_item
- name: new_strategy_group_response
  property_count: 2
  slug: campaigns-new_strategy_group_response
- name: new_strategy_group_strategy_embed
  property_count: 3
  slug: campaigns-new_strategy_group_strategy_embed
- name: new_strategy_group_update
  property_count: 0
  slug: campaigns-new_strategy_group_update
- name: new_strategy_plan_collection_full
  property_count: 2
  slug: campaigns-new_strategy_plan_collection_full
- name: new_strategy_plan_collection_full_extended
  property_count: 2
  slug: campaigns-new_strategy_plan_collection_full_extended
- name: new_strategy_plan_full
  property_count: 0
  slug: campaigns-new_strategy_plan_full
- name: new_strategy_plan_full_extended
  property_count: 0
  slug: campaigns-new_strategy_plan_full_extended
- name: new_strategy_plan_full_response
  property_count: 0
  slug: campaigns-new_strategy_plan_full_response
- name: new_strategy_plan_full_response_extended
  property_count: 0
  slug: campaigns-new_strategy_plan_full_response_extended
- name: new_strategy_plan_response
  property_count: 2
  slug: campaigns-new_strategy_plan_response
- name: new_strategy_plan_response_extended
  property_count: 2
  slug: campaigns-new_strategy_plan_response_extended
- name: organization_base
  property_count: 40
  slug: campaigns-organization_base
- name: organization_collection
  property_count: 2
  slug: campaigns-organization_collection
- name: organization_create
  property_count: 0
  slug: campaigns-organization_create
- name: organization_response
  property_count: 2
  slug: campaigns-organization_response
- name: organization_update
  property_count: 0
  slug: campaigns-organization_update
- name: path_audience_segment
  property_count: 17
  slug: campaigns-path_audience_segment
- name: path_audience_segments_full
  property_count: 2
  slug: campaigns-path_audience_segments_collection_full
- name: permission
  property_count: 6
  slug: campaigns-permission
- name: permission_advertiser
  property_count: 0
  slug: campaigns-permission_advertiser
- name: permission_agency
  property_count: 0
  slug: campaigns-permission_agency
- name: permission_campaign
  property_count: 0
  slug: campaigns-permission_campaign
- name: permission_campaign_with_user
  property_count: 0
  slug: campaigns-permission_campaign_with_user
- name: permission_flags
  property_count: 5
  slug: campaigns-permission_flags
- name: permission_list
  property_count: 5
  slug: campaigns-permission_list
- name: permission_organization
  property_count: 0
  slug: campaigns-permission_organization
- name: permission_strategy
  property_count: 0
  slug: campaigns-permission_strategy
- name: permission_strategy_with_user
  property_count: 0
  slug: campaigns-permission_strategy_with_user
- name: permission_user_output
  property_count: 35
  slug: campaigns-permission_user_output
- name: permission_v2_advertiser
  property_count: 0
  slug: campaigns-permission_v2_advertiser
- name: permission_v2_agency
  property_count: 0
  slug: campaigns-permission_v2_agency
- name: permission_v2_flags
  property_count: 12
  slug: campaigns-permission_v2_flags
- name: permission_v2_object
  property_count: 2
  slug: campaigns-permission_v2_object
- name: permission_v2_organization
  property_count: 0
  slug: campaigns-permission_v2_organization
- name: pixel_bundle_base
  property_count: 24
  slug: campaigns-pixel_bundle_base
- name: pixel_bundle_collection
  property_count: 2
  slug: campaigns-pixel_bundle_collection
- name: pixel_bundle_collection_full
  property_count: 2
  slug: campaigns-pixel_bundle_collection_full
- name: pixel_bundle_create
  property_count: 3
  slug: campaigns-pixel_bundle_create
- name: pixel_bundle
  property_count: 0
  slug: campaigns-pixel_bundle_response
- name: pixel_providers_response
  property_count: 2
  slug: campaigns-pixel_providers_response
- name: pixel_providers_full_response
  property_count: 2
  slug: campaigns-pixel_providers_response_full
- name: roles
  property_count: 0
  slug: campaigns-roles
- name: search_result
  property_count: 3
  slug: campaigns-search_result
- name: segment_group_create
  property_count: 5
  slug: campaigns-segment_group_create
- name: segment_group_update
  property_count: 5
  slug: campaigns-segment_group_update
- name: settings_organization
  property_count: 2
  slug: campaigns-settings_organization
- name: settings_organization_update
  property_count: 1
  slug: campaigns-settings_organization_update
- name: sidekick_usage_log_base
  property_count: 26
  slug: campaigns-sidekick_usage_log_base
- name: sidekick_usage_log_create
  property_count: 22
  slug: campaigns-sidekick_usage_log_create
- name: single_metadata
  property_count: 1
  slug: campaigns-single_metadata
- name: site_list
  property_count: 2
  slug: campaigns-site_list
- name: site_list_assignment_collection
  property_count: 2
  slug: campaigns-site_list_assignment_collection
- name: site_list_assignment_collection_full
  property_count: 2
  slug: campaigns-site_list_assignment_collection_full
- name: site_list_assignment_full
  property_count: 0
  slug: campaigns-site_list_assignment_full
- name: site_list_collection
  property_count: 2
  slug: campaigns-site_list_collection
- name: site_list_collection_full
  property_count: 2
  slug: campaigns-site_list_collection_full
- name: site_list_extended
  property_count: 10
  slug: campaigns-site_list_extended
- name: site_list_full
  property_count: 0
  slug: campaigns-site_list_full
- name: strategy_response
  property_count: 2
  slug: campaigns-strategy
- name: strategy_audience_segment
  property_count: 2
  slug: campaigns-strategy_audience_segment
- name: ''
  property_count: 10
  slug: campaigns-strategy_audience_segment_extended
- name: strategy_base
  property_count: 0
  slug: campaigns-strategy_base
- name: strategy_budget
  property_count: 3
  slug: campaigns-strategy_budget
- name: strategy_campaign_info
  property_count: 9
  slug: campaigns-strategy_campaign_info
- name: strategy_collection
  property_count: 2
  slug: campaigns-strategy_collection
- name: strategy_collection_full
  property_count: 2
  slug: campaigns-strategy_collection_full
- name: strategy_collection_full_extended
  property_count: 2
  slug: campaigns-strategy_collection_full_extended
- name: strategy_concept_collection
  property_count: 2
  slug: campaigns-strategy_concept_collection
- name: strategy_concept_collection_full
  property_count: 2
  slug: campaigns-strategy_concept_collection_full
- name: strategy_concept_full
  property_count: 0
  slug: campaigns-strategy_concept_full
- name: strategy_concepts
  property_count: 2
  slug: campaigns-strategy_concepts
- name: strategy_concepts_extended
  property_count: 2
  slug: campaigns-strategy_concepts_extended
- name: strategy_contextual_segment
  property_count: 2
  slug: campaigns-strategy_contextual_segment
- name: ''
  property_count: 11
  slug: campaigns-strategy_contextual_segment_extended
- name: strategy_create_request
  property_count: 0
  slug: campaigns-strategy_create_request
- name: strategy_day_part_collection
  property_count: 2
  slug: campaigns-strategy_day_part_collection
- name: strategy_day_part_collection_full
  property_count: 2
  slug: campaigns-strategy_day_part_collection_full
- name: strategy_day_part_full
  property_count: 0
  slug: campaigns-strategy_day_part_full
- name: strategy_deal_collection
  property_count: 2
  slug: campaigns-strategy_deal_collection
- name: strategy_deal_collection_full
  property_count: 2
  slug: campaigns-strategy_deal_collection_full
- name: strategy_deal_full
  property_count: 0
  slug: campaigns-strategy_deal_full
- name: strategy_details
  property_count: 15
  slug: campaigns-strategy_details
- name: strategy_duration
  property_count: 4
  slug: campaigns-strategy_duration
- name: strategy_extended_response
  property_count: 2
  slug: campaigns-strategy_extended
- name: strategy_forecast_query
  property_count: 5
  slug: campaigns-strategy_forecast_query
- name: strategy_frequency
  property_count: 4
  slug: campaigns-strategy_frequency
- name: strategy_full
  property_count: 0
  slug: campaigns-strategy_full
- name: strategy_full_extended
  property_count: 0
  slug: campaigns-strategy_full_extended
- name: strategy_full_response
  property_count: 0
  slug: campaigns-strategy_full_response
- name: ''
  property_count: 2
  slug: campaigns-strategy_geofence
- name: ''
  property_count: 2
  slug: campaigns-strategy_geofence_extended
- name: strategy_goals
  property_count: 11
  slug: campaigns-strategy_goals
- name: strategy_group_collection
  property_count: 2
  slug: campaigns-strategy_group_collection
- name: strategy_group_collection_full
  property_count: 2
  slug: campaigns-strategy_group_collection_full
- name: strategy_group_collection_full_extended
  property_count: 2
  slug: campaigns-strategy_group_collection_full_extended
- name: strategy_group_full
  property_count: 0
  slug: campaigns-strategy_group_full
- name: strategy_group_full_extended
  property_count: 0
  slug: campaigns-strategy_group_full_extended
- name: strategy_healthcheck
  property_count: 8
  slug: campaigns-strategy_healthcheck
- name: strategy_inventory
  property_count: 10
  slug: campaigns-strategy_inventory
- name: strategy_inventory_extended
  property_count: 9
  slug: campaigns-strategy_inventory_extended
- name: strategy_ip_address_collection
  property_count: 2
  slug: campaigns-strategy_ip_address_collection
- name: strategy_ip_address_collection_full
  property_count: 2
  slug: campaigns-strategy_ip_address_collection_full
- name: strategy_ip_address_full
  property_count: 0
  slug: campaigns-strategy_ip_address_full
- name: ''
  property_count: 3
  slug: campaigns-strategy_location
- name: ''
  property_count: 6
  slug: campaigns-strategy_location_extended
- name: ''
  property_count: 2
  slug: campaigns-strategy_my_data
- name: ''
  property_count: 2
  slug: campaigns-strategy_my_data_extended
- name: strategy_pacing
  property_count: 10
  slug: campaigns-strategy_pacing
- name: strategy_plan_budget
  property_count: 2
  slug: campaigns-strategy_plan_budget
- name: strategy_plan_creatives
  property_count: 3
  slug: campaigns-strategy_plan_creatives
- name: strategy_plan_details
  property_count: 3
  slug: campaigns-strategy_plan_details
- name: strategy_plan_duration
  property_count: 4
  slug: campaigns-strategy_plan_duration
- name: strategy_plan_frequency
  property_count: 4
  slug: campaigns-strategy_plan_frequency
- name: strategy_plan_goals
  property_count: 10
  slug: campaigns-strategy_plan_goals
- name: strategy_plan_inventory
  property_count: 8
  slug: campaigns-strategy_plan_inventory
- name: strategy_plan_target_full
  property_count: 0
  slug: campaigns-strategy_plan_target_full
- name: strategy_plan_target_value_collection
  property_count: 2
  slug: campaigns-strategy_plan_target_value_collection
- name: strategy_plan_target_value_collection_full
  property_count: 2
  slug: campaigns-strategy_plan_target_value_collection_full
- name: strategy_plan_target_value_full
  property_count: 0
  slug: campaigns-strategy_plan_target_value_full
- name: strategy_plan_targeting
  property_count: 0
  slug: campaigns-strategy_plan_targeting
- name: strategy_plan_targeting_extended
  property_count: 0
  slug: campaigns-strategy_plan_targeting_extended
- name: strategy_postal_code_collection
  property_count: 2
  slug: campaigns-strategy_postal_code_collection
- name: strategy_postal_code_collection_full
  property_count: 2
  slug: campaigns-strategy_postal_code_collection_full
- name: strategy_postal_code_full
  property_count: 0
  slug: campaigns-strategy_postal_code_full
- name: strategy_segment_group
  property_count: 2
  slug: campaigns-strategy_segment_group
- name: strategy_segment_group_exclude
  property_count: 1
  slug: campaigns-strategy_segment_group_exclude
- name: strategy_segment_group_exclude_extended
  property_count: 1
  slug: campaigns-strategy_segment_group_exclude_extended
- name: strategy_segment_group_extended
  property_count: 2
  slug: campaigns-strategy_segment_group_extended
- name: strategy_target_full
  property_count: 0
  slug: campaigns-strategy_target_full
- name: strategy_target_value_collection
  property_count: 2
  slug: campaigns-strategy_target_value_collection
- name: strategy_target_value_collection_full
  property_count: 2
  slug: campaigns-strategy_target_value_collection_full
- name: strategy_target_value_full
  property_count: 0
  slug: campaigns-strategy_target_value_full
- name: strategy_targeting
  property_count: 0
  slug: campaigns-strategy_targeting
- name: strategy_targeting_expression
  property_count: 1
  slug: campaigns-strategy_targeting_expression
- name: strategy_targeting_extended
  property_count: 0
  slug: campaigns-strategy_targeting_extended
- name: strategy_targeting_request
  property_count: 1
  slug: campaigns-strategy_targeting_request
- name: strategy_targeting_request_for_bulk
  property_count: 1
  slug: campaigns-strategy_targeting_request_for_bulk
- name: ''
  property_count: 3
  slug: campaigns-strategy_technology
- name: ''
  property_count: 4
  slug: campaigns-strategy_technology_extended
- name: strategy template response
  property_count: 10
  slug: campaigns-strategy_template_response
- name: ''
  property_count: 1
  slug: campaigns-supply_source
- name: ''
  property_count: 3
  slug: campaigns-supply_source_extended
- name: supply_source_response
  property_count: 0
  slug: campaigns-supply_source_response
- name: target_base
  property_count: 9
  slug: campaigns-target_base
- name: target_create
  property_count: 0
  slug: campaigns-target_create
- name: target_dimension_exclude
  property_count: 3
  slug: campaigns-target_dimension_exclude
- name: target_dimension_include
  property_count: 3
  slug: campaigns-target_dimension_include
- name: target_update
  property_count: 10
  slug: campaigns-target_update
- name: target_value_full
  property_count: 0
  slug: campaigns-target_value_full
- name: targeting_base
  property_count: 6
  slug: campaigns-targeting_base
- name: targeting_friendly_name
  property_count: 7
  slug: campaigns-targeting_friendly_name
- name: targeting_ip_addresses
  property_count: 2
  slug: campaigns-targeting_ip_addresses
- name: targeting_ip_addresses_response
  property_count: 2
  slug: campaigns-targeting_ip_addresses_response
- name: targeting_postal_codes
  property_count: 2
  slug: campaigns-targeting_postal_codes
- name: targeting_postal_codes_response
  property_count: 2
  slug: campaigns-targeting_postal_codes_response
- name: targeting_recency_element_request
  property_count: 3
  slug: campaigns-targeting_recency_element_request
- name: targeting_recency_element_response
  property_count: 3
  slug: campaigns-targeting_recency_element_response
- name: targeting_segment_collection
  property_count: 2
  slug: campaigns-targeting_segment_collection
- name: targeting_segment_collection_full
  property_count: 2
  slug: campaigns-targeting_segment_collection_full
- name: targeting_segment_full
  property_count: 0
  slug: campaigns-targeting_segment_full
- name: targeting_segment_objective_response
  property_count: 0
  slug: campaigns-targeting_segment_objective_response
- name: timezone_collection
  property_count: 2
  slug: campaigns-timezone_collection
- name: timezone_collection_full
  property_count: 2
  slug: campaigns-timezone_collection_full
- name: timezone_full
  property_count: 0
  slug: campaigns-timezone_full
- name: user
  property_count: 4
  slug: campaigns-user_base
- name: user_create
  property_count: 0
  slug: campaigns-user_create
- name: user permission
  property_count: 5
  slug: campaigns-user_permission
- name: user_permission_update
  property_count: 1
  slug: campaigns-user_permission_update
- name: user permissions
  property_count: 3
  slug: campaigns-user_permissions
- name: user_permissions_response
  property_count: 2
  slug: campaigns-user_permissions_response
- name: user_response
  property_count: 2
  slug: campaigns-user_response
- name: user_settings_response
  property_count: 3
  slug: campaigns-user_settings_response
- name: user_settings_update_request
  property_count: 1
  slug: campaigns-user_settings_update_request
- name: user_update
  property_count: 0
  slug: campaigns-user_update
- name: vendor
  property_count: 22
  slug: campaigns-vendor_base
- name: vendor_collection
  property_count: 2
  slug: campaigns-vendor_collection
- name: vendor_collection_full
  property_count: 2
  slug: campaigns-vendor_collection_full
- name: vendor_contract
  property_count: 0
  slug: campaigns-vendor_contract
- name: vendor_contract_base
  property_count: 4
  slug: campaigns-vendor_contract_base
- name: Error
  property_count: 3
  slug: reporting-Error
- name: Streaming Response
  property_count: 0
  slug: reporting-StreamingResponse
layout: provider
modified: '2026-06-13'
name: MediaMath
nav: Providers
network: true
overview: 'MediaMath publishes 37 APIs on the [APIs.io](https://apis.io/) network, including Ad Servers API, Advertisers API, Agencies API, and 34 more. Tagged areas include Programmatic Advertising, DSP, Demand-Side Platform, Campaign Management, and Ad Tech.


  The MediaMath catalog on APIs.io includes 1 Spectral governance ruleset.


  MediaMath''s developer surface includes authentication, documentation, engineering blog, support, academy / training, and 8 more developer resources.'
plans:
- name: Mediamath Plans
  plan_count: 2
  slug: mediamath-plans
random_paper: 98
rate_limits:
- limit_count: 7
  name: Mediamath Rate Limits
  slug: mediamath-rate-limits
rules:
- name: MediaMath API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: mediamath-jsonschema-spectral-rules
scopes:
- name: Mediamath Scopes
  scope_count: 2
  slug: mediamath-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 47.5
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 63.8
    developer_ergonomics: 26.1
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 31.6
  previous_composite: 47.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 37
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mediamath/refs/heads/main/screenshots/mediamath-2026-06-20T185115.png
security:
- kind: authentication
  name: Mediamath Authentication
  slug: mediamath-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Mediamath Domain Security
  slug: mediamath-domain-security
  summary_line: TLSv1.3 · DMARC
slug: mediamath
tags:
- Programmatic Advertising
- DSP
- Demand-Side Platform
- Campaign Management
- Ad Tech
- Bidding
- Audience Segments
- Creative Management
- Reporting
- Analytics
---
