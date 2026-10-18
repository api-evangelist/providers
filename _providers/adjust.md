---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.0
  scored_at: '2026-10-17'
api_count: 6
apis:
- description: Adjust mobile measurement and fraud prevention API documentation
  name: Adjust API
  slug: adjust-api-2
- baseURL: https://api.adjust.com
  baseurl_source: declared
  description: The Cost API from Adjust — 1 operation(s) for cost.
  name: Adjust Cost API
  slug: adjust-cost-api
- baseURL: https://api.adjust.com
  baseurl_source: declared
  description: The Dashboard API from Adjust — 2 operation(s) for dashboard.
  name: Adjust Dashboard API
  slug: adjust-dashboard-api
- baseURL: https://api.adjust.com
  baseurl_source: declared
  description: The Device Service API from Adjust — 3 operation(s) for device service.
  name: Adjust Device Service API
  slug: adjust-device-service-api
- baseURL: https://api.adjust.com
  baseurl_source: declared
  description: The Public API from Adjust — 1 operation(s) for public.
  name: Adjust Public API
  slug: adjust-public-api
- baseURL: https://api.adjust.com
  baseurl_source: declared
  description: The Reports Service API from Adjust — 1 operation(s) for reports service.
  name: Adjust Reports Service API
  slug: adjust-reports-service-api
artifact_total: 16
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/adjust/refs/heads/main/rate-limits/adjust-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/adjust-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adjust/refs/heads/main/rules/adjust-rules.yml
  title: ''
  type: Spectral
  url: rules/adjust-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adjust/refs/heads/main/json-ld/adjust-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/adjust-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adjust/refs/heads/main/vocabulary/adjust-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/adjust-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adjust/refs/heads/main/data-model/adjust-data-model.yml
  title: ''
  type: DataModel
  url: data-model/adjust-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adjust/refs/heads/main/conformance/adjust-conformance.yml
  title: ''
  type: Conformance
  url: conformance/adjust-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/adjust/refs/heads/main/llms/adjust-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/adjust-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/adjust/refs/heads/main/well-known/adjust-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/adjust-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/adjust/refs/heads/main/well-known/adjust-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/adjust-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adjust/refs/heads/main/hosts/adjust-hosts.yml
  title: ''
  type: Hosts
  url: hosts/adjust-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adjust/refs/heads/main/vendors/adjust-vendors.yml
  title: ''
  type: Vendors
  url: vendors/adjust-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/adjust/refs/heads/main/packages/adjust-packages.yml
  title: ''
  type: SDKs
  url: packages/adjust-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/adjust/refs/heads/main/packages/adjust-packages.yml
  title: ''
  type: Packages
  url: packages/adjust-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://help.adjust.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.adjust.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.adjust.com/en/sdk/android/setup
- group: docs
  title: ''
  type: Documentation
  url: https://dev.adjust.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/adjust
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/adjust/refs/heads/main/security/adjust-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adjust-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.adjust.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.adjust.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.adjust.com/blog/
- group: auth
  title: ''
  type: Security
  url: https://www.adjust.com/security/
- group: operate
  title: ''
  type: Contact
  url: https://www.adjust.com/company/contact-us/
coverage:
  checked: '2026-10-13'
  detail: Developer portal provides HTML documentation but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found.
  evidence:
  - status: 200
    url: https://dev.adjust.com/en/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-13'
description: Adjust provides a mobile measurement and fraud prevention platform that helps app developers and marketers track user acquisition, engagement, and revenue across mobile, web, CTV, and console. Their solutions include analytics, automation, deep linking, AI-driven insights, and robust security to prevent ad fraud. Adjust serves enterprises worldwide, offering customizable dashboards, real-time data, and integration with major ad networks and SDKs.
image: https://a.storyblok.com/f/47007/2501x1314/884dd286a6/meta-adjuststandard.png/m/1200x630/filters:quality(70)
json_schemas:
- name: GetDeviceServiceApiV1InspectDeviceResponse
  property_count: 9
  slug: adjust-get-device-service-api-v1-inspect-device-response
- name: GetDeviceServiceApiV2InspectDeviceResponse
  property_count: 13
  slug: adjust-get-device-service-api-v2-inspect-device-response
- name: GetPublicV2PartnersResponse
  property_count: 1
  slug: adjust-get-public-v2-partners-response
- name: GetReportsServiceReportsserviceidResponse
  property_count: 1
  slug: adjust-get-reports-service-reportsserviceid-response
- name: PostDashboardApiTrackersLinktokenBlacklistResponse
  property_count: 18
  slug: adjust-post-dashboard-api-trackers-linktoken-blacklist-response
- name: PostDashboardApiTrackersResponse
  property_count: 18
  slug: adjust-post-dashboard-api-trackers-response
jsonld:
- class_count: 6
  name: Adjust Context
  property_count: 34
  slug: adjust-context
layout: provider
modified: '2026-10-13'
name: Adjust
nav: Providers
network: true
overview: 'Adjust is listed with 6 APIs on the [APIs.io](https://apis.io/) network, including Cost API, Dashboard API, Device Service API, and 3 more. Tagged areas include Measurements, Analytics, Attribution, Deep Linking, and Fraud Prevention.


  The Adjust catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Adjust''s developer surface includes support, getting-started guide, documentation, pricing, engineering blog, and 19 more developer resources.'
random_paper: 13
rate_limits:
- limit_count: 2
  name: Adjust Rate Limits
  slug: adjust-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Adjust API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: adjust-rules
score:
  band: thin
  composite: 30.8
  coverage:
    artifact_dirs: 17
    catalog_earned: 68.8
    catalog_earned_first_party: 8.0
    catalog_gap: 46.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 25.9
    developer_ergonomics: 35.7
    discoverability: 69.6
    operational_transparency: 52.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Adjust Domain Security
  slug: adjust-domain-security
  summary_line: TLSv1.3 · DMARC
slug: adjust
tags:
- Measurements
- Analytics
- Attribution
- Deep Linking
- Fraud Prevention
- Mobile Marketing
- AI Solutions
- Gaming
website: https://www.adjust.com
---
