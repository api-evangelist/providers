---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
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
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 29.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 97
  human_in_the_loop: 12
  name: Easee Agentic Access
  operation_count: 175
  slug: easee-agentic-access
  summary_line: 175 operations · 97 acting · 12 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.easee.com
  baseurl_source: declared
  description: Sign in, refresh tokens and manage the logged-in account.
  name: Easee Account API
  slug: easee-account-api
- baseURL: https://api.easee.com
  baseurl_source: declared
  description: Start charging on a charger.
  name: Easee Authorize Charging API
  slug: easee-authorizecharging-api
- baseURL: https://api.easee.com
  baseurl_source: declared
  description: Latest, ongoing and historical charging sessions for a charger.
  name: Easee Charge Session API
  slug: easee-charge-session-api
- baseURL: https://api.easee.com
  baseurl_source: declared
  description: Read, configure and control chargers.
  name: Easee Charger API
  slug: easee-charger-api
- baseURL: https://api.easee.com
  baseurl_source: declared
  description: Configure Cloud OCPP settings and custom endpoints for operators.
  name: Easee Cloud OCPP API
  slug: easee-cloud-ocpp-api
- baseURL: https://api.easee.com
  baseurl_source: declared
  description: Charge at the same times every day.
  name: Easee Daily schedule API
  slug: easee-daily-schedule-api
- baseURL: https://api.easee.com
  baseurl_source: declared
  description: Start charging after a delay.
  name: Easee Delayed schedule API
  slug: easee-delayed-schedule-api
- baseURL: https://api.easee.com
  baseurl_source: declared
  description: Operators manage direct OCPP connections on their chargers and sites.
  name: Easee Direct OCPP - For Operators API
  slug: easee-direct-ocpp-for-operators-api
- baseURL: https://api.easee.com
  baseurl_source: declared
  description: Users manage direct OCPP on their own chargers.
  name: Easee Direct OCPP - For Users API
  slug: easee-direct-ocpp-for-users-api
- baseURL: https://api.easee.com
  baseurl_source: declared
  description: Manage Easee keys linked to an account.
  name: Easee Easee Keys API
  slug: easee-easeekeys-api
- baseURL: https://api.easee.com
  baseurl_source: declared
  description: Lifetime energy measurements for chargers, hourly to yearly.
  name: Easee Energy Reporting API
  slug: easee-energy-reporting-api
- baseURL: https://api.easee.com
  baseurl_source: declared
  description: Read and manage equalizers.
  name: Easee Equalizer API
  slug: easee-equalizer-api
- baseURL: https://api.easee.com
  baseurl_source: declared
  description: Observations reported by devices.
  name: Easee Observations API
  slug: easee-observations-api
- baseURL: https://api.easee.com
  baseurl_source: declared
  description: Reference data such as countries and currencies.
  name: Easee Resources API
  slug: easee-resources-api
- baseURL: https://api.easee.com
  baseurl_source: declared
  description: Read and manage sites.
  name: Easee Site API
  slug: easee-site-api
- baseURL: https://api.easee.com
  baseurl_source: declared
  description: Energy usage, cost and sessions for a site.
  name: Easee Site Charge Session API
  slug: easee-site-charge-session-api
- baseURL: https://api.easee.com
  baseurl_source: declared
  description: Read the active scheduling state of a charger.
  name: Easee State API
  slug: easee-state-api
- baseURL: https://api.easee.com
  baseurl_source: declared
  description: Charge at set times for each day of the week.
  name: Easee Weekly schedule API
  slug: easee-weekly-schedule-api
artifact_total: 88
common:
- group: auth
  href: https://artifacts.apis.io/easee/well-known/easee-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/easee-status-security.txt
- group: agent
  href: https://artifacts.apis.io/easee/agentic-access/easee-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/easee-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/easee/rules/easee-rules.yml
  title: ''
  type: Spectral
  url: rules/easee-rules.yml
- group: design
  href: https://artifacts.apis.io/easee/json-ld/easee-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/easee-context.jsonld
- group: design
  href: https://artifacts.apis.io/easee/vocabulary/easee-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/easee-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/easee/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/easee/data-model/easee-data-model.yml
  title: ''
  type: DataModel
  url: data-model/easee-data-model.yml
- group: auth
  href: https://artifacts.apis.io/easee/authentication/easee-authentication.yml
  title: ''
  type: Authentication
  url: authentication/easee-authentication.yml
- group: design
  href: https://artifacts.apis.io/easee/errors/easee-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/easee-problem-types.yml
- group: design
  href: https://artifacts.apis.io/easee/conformance/easee-conformance.yml
  title: ''
  type: Conformance
  url: conformance/easee-conformance.yml
- group: agent
  href: https://artifacts.apis.io/easee/llms/easee-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/easee-llms.txt
- group: agent
  href: https://artifacts.apis.io/easee/well-known/easee-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/easee-well-known.yml
- group: other
  href: https://artifacts.apis.io/easee/hosts/easee-hosts.yml
  title: ''
  type: Hosts
  url: hosts/easee-hosts.yml
- group: other
  href: https://artifacts.apis.io/easee/vendors/easee-vendors.yml
  title: ''
  type: Vendors
  url: vendors/easee-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://easee.com/en/terms/
- group: operate
  title: ''
  type: Support
  url: https://support.easee.com/hc/en-gb
- group: operate
  title: ''
  type: StatusPage
  url: https://status.easee.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://easee.com/en/privacy/
- group: company
  title: ''
  type: Newsroom
  url: https://easee.com/sv/om-oss/press/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.easee.com/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.easee.com/docs/onboarding-introduction
- group: docs
  title: ''
  type: Documentation
  url: https://developer.easee.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.easee.com/reference/open-api-specification.md
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/easee
- group: auth
  href: https://artifacts.apis.io/easee/security/easee-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/easee-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://easee.com/
created: '2026-10-27'
description: Easee provides smart electric vehicle (EV) charging solutions, offering Wi‑Fi‑enabled, app‑controlled home and commercial chargers that optimize charging speed, energy usage, and integration with renewable sources. Their platform includes a cloud‑based dashboard for monitoring, scheduling, and firmware updates, as well as APIs for third‑party integration, enabling developers to retrieve charger status, control charging sessions, and manage user access across multiple locations.
image: https://easee.com/wp-content/uploads/2026/03/mnmt_15_plugged-e1773234476872.webp
json_schemas:
- name: Access_Control_API_Login
  property_count: 2
  slug: easee-access-control-api-login
- name: Access_Control_API_PartnerDetailedDTO
  property_count: 29
  slug: easee-access-control-api-partner-detailed-dto
- name: Access_Control_API_ProductPinDTO
  property_count: 2
  slug: easee-access-control-api-product-pin-dto
- name: Access_Control_API_ProfileDTO
  property_count: 14
  slug: easee-access-control-api-profile-dto
- name: Access_Control_API_RefreshTokenDTO
  property_count: 1
  slug: easee-access-control-api-refresh-token-dto
- name: Access_Control_API_SiteDTO
  property_count: 15
  slug: easee-access-control-api-site-dto
- name: Access_Control_API_UserToken
  property_count: 5
  slug: easee-access-control-api-user-token
- name: Current_Device_State_API_MultiObservationResponse
  property_count: 1
  slug: easee-current-device-state-api-multi-observation-response
- name: Easee.ChargeAuthorization.ExternalWebApi_EaseeKeyDTO
  property_count: 2
  slug: easee-easee-charge-authorization-external-web-api-easee-key-dto
- name: Easee.ChargeSessionTracking.WebApi_ChargeSessionDTO
  property_count: 18
  slug: easee-easee-charge-session-tracking-web-api-charge-session-dto
- name: Easee.ChargeSessionTracking.WebApi_ChargingSessionDetailDTO
  property_count: 5
  slug: easee-easee-charge-session-tracking-web-api-charging-session-detail-dto
- name: Easee.ChargeSessionTracking.WebApi_DailySummaryDTO
  property_count: 7
  slug: easee-easee-charge-session-tracking-web-api-daily-summary-dto
- name: Easee.ChargeSessionTracking.WebApi_MonthlySummaryDTO
  property_count: 6
  slug: easee-easee-charge-session-tracking-web-api-monthly-summary-dto
- name: Easee.ChargeSessionTracking.WebApi_UsageStatisticsDTO
  property_count: 17
  slug: easee-easee-charge-session-tracking-web-api-usage-statistics-dto
- name: Easee.ChargeSessionTracking.WebApi_WeeklySummaryDTO
  property_count: 7
  slug: easee-easee-charge-session-tracking-web-api-weekly-summary-dto
- name: Easee.ChargeSessionTracking.WebApi_YearlySummaryDTO
  property_count: 5
  slug: easee-easee-charge-session-tracking-web-api-yearly-summary-dto
- name: Easee_Cloud_API_AggregatedLifetimeEnergy
  property_count: 6
  slug: easee-easee-cloud-api-aggregated-lifetime-energy
- name: Easee_Cloud_API_BasicSiteDTO
  property_count: 7
  slug: easee-easee-cloud-api-basic-site-dto
- name: Easee_Cloud_API_ChargerConfigurationDTO
  property_count: 25
  slug: easee-easee-cloud-api-charger-configuration-dto
- name: Easee_Cloud_API_ChargerDTO
  property_count: 8
  slug: easee-easee-cloud-api-charger-dto
- name: Easee_Cloud_API_ChargerDTO2
  property_count: 10
  slug: easee-easee-cloud-api-charger-dto2
- name: Easee_Cloud_API_ChargerSettingDTO
  property_count: 17
  slug: easee-easee-cloud-api-charger-setting-dto
- name: Easee_Cloud_API_CircuitDTO2
  property_count: 11
  slug: easee-easee-cloud-api-circuit-dto2
- name: Easee_Cloud_API_CircuitSettingsDTO
  property_count: 11
  slug: easee-easee-cloud-api-circuit-settings-dto
- name: Easee_Cloud_API_CommandDto
  property_count: 3
  slug: easee-easee-cloud-api-command-dto
- name: Easee_Cloud_API_CountryDTO2
  property_count: 3
  slug: easee-easee-cloud-api-country-dto2
- name: Easee_Cloud_API_Currency
  property_count: 3
  slug: easee-easee-cloud-api-currency
- name: Easee_Cloud_API_DetailedEqualizerDTO
  property_count: 5
  slug: easee-easee-cloud-api-detailed-equalizer-dto
- name: Easee_Cloud_API_EqualizerConfigurationDTO
  property_count: 12
  slug: easee-easee-cloud-api-equalizer-configuration-dto
- name: Easee_Cloud_API_EqualizerDTO2
  property_count: 4
  slug: easee-easee-cloud-api-equalizer-dto2
- name: Easee_Cloud_API_GetAllMeasurementsResponse
  property_count: 1
  slug: easee-easee-cloud-api-get-all-measurements-response
- name: Easee_Cloud_API_LifetimeEnergyMeasurementSettingsRequest
  property_count: 2
  slug: easee-easee-cloud-api-lifetime-energy-measurement-settings-request
- name: Easee_Cloud_API_MeterSettingsDTO
  property_count: 2
  slug: easee-easee-cloud-api-meter-settings-dto
- name: Easee_Cloud_API_ObservationPropertyDTO
  property_count: 3
  slug: easee-easee-cloud-api-observation-property-dto
- name: Easee_Cloud_API_SiteCostDTO
  property_count: 4
  slug: easee-easee-cloud-api-site-cost-dto
- name: Easee_Cloud_API_SiteDTO
  property_count: 34
  slug: easee-easee-cloud-api-site-dto
- name: Easee_Cloud_API_SiteDTO2
  property_count: 31
  slug: easee-easee-cloud-api-site-dto2
- name: Easee_Cloud_Ocpp_Api_SaveOcppConfigRequest
  property_count: 9
  slug: easee-easee-cloud-ocpp-api-save-ocpp-config-request
- name: Easee_Cloud_Ocpp_Api_SetCustomEndpointRequest
  property_count: 1
  slug: easee-easee-cloud-ocpp-api-set-custom-endpoint-request
- name: Easee_Command_API_Command
  property_count: 14
  slug: easee-easee-command-api-command
- name: Easee_OCPP_Configuration_API_ApplyOcppForChargerRequest
  property_count: 1
  slug: easee-easee-ocpp-configuration-api-apply-ocpp-for-charger-request
- name: Easee_OCPP_Configuration_API_ApplyOcppForSiteResult
  property_count: 1
  slug: easee-easee-ocpp-configuration-api-apply-ocpp-for-site-result
- name: Easee_OCPP_Configuration_API_ApplyOcppForUserChargerRequest
  property_count: 1
  slug: easee-easee-ocpp-configuration-api-apply-ocpp-for-user-charger-request
- name: Easee_OCPP_Configuration_API_ConnectionDetailsDto
  property_count: 4
  slug: easee-easee-ocpp-configuration-api-connection-details-dto
- name: Easee_OCPP_Configuration_API_EmptyResponse
  property_count: 0
  slug: easee-easee-ocpp-configuration-api-empty-response
- name: Easee_OCPP_Configuration_API_OperatorConnectionDetailsDto
  property_count: 5
  slug: easee-easee-ocpp-configuration-api-operator-connection-details-dto
- name: Easee_OCPP_Configuration_API_PostChargerConnectionDetailsRequest
  property_count: 4
  slug: easee-easee-ocpp-configuration-api-post-charger-connection-details-request
- name: Easee_OCPP_Configuration_API_PostOperatorConnectionDetailsRequest
  property_count: 4
  slug: easee-easee-ocpp-configuration-api-post-operator-connection-details-request
- name: Easee_OCPP_Configuration_API_PostUserChargerConnectionDetailsRequest
  property_count: 4
  slug: easee-easee-ocpp-configuration-api-post-user-charger-connection-details-request
- name: Easee_OCPP_Configuration_API_PostUserChargerConnectionDetailsResponse
  property_count: 1
  slug: easee-easee-ocpp-configuration-api-post-user-charger-connection-details-response
- name: Scheduled_charging_CreateDailyScheduleRequest
  property_count: 3
  slug: easee-scheduled-charging-create-daily-schedule-request
- name: Scheduled_charging_CreateDailyScheduleResponse
  property_count: 3
  slug: easee-scheduled-charging-create-daily-schedule-response
- name: Scheduled_charging_CreateDelayedScheduleRequest
  property_count: 4
  slug: easee-scheduled-charging-create-delayed-schedule-request
- name: Scheduled_charging_CreateDelayedScheduleResponse
  property_count: 4
  slug: easee-scheduled-charging-create-delayed-schedule-response
- name: Scheduled_charging_CreateWeeklyScheduleRequest
  property_count: 3
  slug: easee-scheduled-charging-create-weekly-schedule-request
- name: Scheduled_charging_CreateWeeklyScheduleResponse
  property_count: 3
  slug: easee-scheduled-charging-create-weekly-schedule-response
- name: Scheduled_charging_GetDailyScheduleResponse
  property_count: 3
  slug: easee-scheduled-charging-get-daily-schedule-response
- name: Scheduled_charging_GetDelayedScheduleResponse
  property_count: 4
  slug: easee-scheduled-charging-get-delayed-schedule-response
- name: Scheduled_charging_GetScheduleStateResponse
  property_count: 6
  slug: easee-scheduled-charging-get-schedule-state-response
- name: Scheduled_charging_GetWeeklyScheduleResponse
  property_count: 3
  slug: easee-scheduled-charging-get-weekly-schedule-response
jsonld:
- class_count: 120
  name: Easee Context
  property_count: 260
  slug: easee-context
layout: provider
modified: '2026-10-27'
name: Easee
nav: Providers
network: true
overview: 'Easee publishes 18 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Authorize Charging API, Charge Session API, and 15 more. Tagged areas include Company, EV Charging, Smart Home, IoT, and Energy.


  The Easee catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Easee''s developer surface includes authentication, support, changelog, getting-started guide, documentation, API reference, and 20 more developer resources.'
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 95
  extends:
  - spectral:oas
  name: Easee API Rules
  rule_count: 54
  severity_counts:
    error: 40
    hint: 0
    info: 2
    warn: 12
  slug: easee-rules
score:
  band: thin
  composite: 38.4
  coverage:
    artifact_dirs: 21
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.5
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 69.5
    developer_ergonomics: 30.4
    discoverability: 65.2
    operational_transparency: 28.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 43.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 18
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 17.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/easee/easee-2026-11-03T131425.png
security:
- kind: authentication
  name: Easee Authentication
  slug: easee-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Easee Domain Security
  slug: easee-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
skill_count: 5
skills:
- name: easee-apply-ocpp-connection-to-charger
  slug: easee-apply-ocpp-connection-to-charger
- name: easee-get-charger-info
  slug: easee-get-charger-info
- name: easee-get-site-chargers
  slug: easee-get-site-chargers
- name: easee-manage-charger-favorites
  slug: easee-manage-charger-favorites
- name: easee-manage-direct-ocpp-connection
  slug: easee-manage-direct-ocpp-connection
slug: easee
tags:
- Company
- EV Charging
- Smart Home
- IoT
- Energy
website: https://easee.com/
---
