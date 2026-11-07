---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 1
  name: Geotab Agentic Access
  operation_count: 5
  slug: geotab-agentic-access
  summary_line: 5 operations · 4 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: The MyGeotab API provides JSON-RPC 2.0 access to all fleet telematics data including vehicle location, trip history, driver behavior, fault codes, fuel usage, HOS/ELD compliance records, and sensor da
  name: MyGeotab API
  slug: mygeotab-api
- description: The MyAdmin API provides reseller and partner access to Geotab's administrative platform for managing databases, device provisioning, orders, billing, and account management. Access requires a MyAdmin
  name: MyAdmin API
  slug: myadmin-api
- baseURL: https://my.geotab.com/apiv1
  baseurl_source: declared
  description: The Authentication API from Geotab — 3 operation(s) for authentication.
  name: Geotab Authentication API
  slug: geotab-authentication-api
- baseURL: https://my.geotab.com/apiv1
  baseurl_source: declared
  description: The Invalid Records API from Geotab — 1 operation(s) for invalid records.
  name: Geotab Invalid Records API
  slug: geotab-invalid-records-api
- baseURL: https://my.geotab.com/apiv1
  baseurl_source: declared
  description: The Records API from Geotab — 1 operation(s) for records.
  name: Geotab Records API
  slug: geotab-records-api
artifact_total: 21
collections:
- collection_type: open
  name: Data Intake Gateway Authentication API
  slug: open-geotab-authentication-api
- collection_type: open
  name: Data Intake Gateway Authentication Invalid Records API
  slug: open-geotab-invalid-records-api
- collection_type: open
  name: Data Intake Gateway Authentication Records API
  slug: open-geotab-records-api
common:
- group: other
  href: https://artifacts.apis.io/geotab/capabilities/geotab-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/geotab-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/geotab/agentic-access/geotab-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/geotab-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/geotab/security/geotab-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/geotab-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/geotab/security/geotab-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/geotab-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/geotab/authentication/geotab-authentication.yml
  title: ''
  type: Authentication
  url: authentication/geotab-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.geotab.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.geotab.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Geotab
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/geotab
- group: other
  title: ''
  type: X
  url: https://x.com/geotab
- group: company
  title: ''
  type: Blog
  url: https://www.geotab.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.geotab.com/software-packages/
- group: commercial
  href: https://artifacts.apis.io/geotab/plans/geotab-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/geotab-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/geotab/rate-limits/geotab-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/geotab-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/geotab/finops/geotab-finops.yml
  title: ''
  type: FinOps
  url: finops/geotab-finops.yml
- group: design
  href: https://artifacts.apis.io/geotab/vocabulary/geotab-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/geotab-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/geotab/json-ld/geotab-context.jsonld
  title: ''
  type: JSONLDContext
  url: json-ld/geotab-context.jsonld
created: 2026-06-12
description: Geotab is a fleet telematics platform providing the MyGeotab SDK and REST API for vehicle tracking, driver behavior monitoring, fuel management, ELD compliance, and route optimization. The MyGeotab API uses JSON-RPC 2.0 over HTTPS with session-token authentication, exposing a single versioned endpoint at /apiv1 that supports Get, Add, Set, and Remove operations across all fleet entities including devices, trips, fault data, and status data. The MyAdmin API provides reseller and partner access to manage databases, orders, and provisioning. Native SDK clients are available for JavaScript, .NET, Java, and Python, and the full SDK and sample code are published on GitHub.
examples:
- key_count: 4
  name: Geotab Dig Authenticate Example
  slug: geotab-dig-authenticate-example
- key_count: 4
  name: Geotab Dig Records Example
  slug: geotab-dig-records-example
finops:
- has_sources: true
  method: generated
  name: Geotab Finops
  primary_unit: Vehicle/Month
  service_category: ''
  slug: geotab-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/geotab.png
json_schemas:
- name: GpsRecord
  property_count: 16
  slug: geotab-gps-record
- name: StatusRecord
  property_count: 5
  slug: geotab-status-record
jsonld:
- class_count: 0
  name: Geotab Context
  property_count: 47
  slug: geotab-context
layout: provider
modified: 2026-06-12
name: Geotab
nav: Providers
network: true
overview: 'Geotab publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authentication API, Invalid Records API, Records API, and 2 more. Tagged areas include Fleet Management, Telematics, Vehicle Tracking, ELD Compliance, and Driver Behavior.


  The Geotab catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Geotab''s developer surface includes authentication, documentation, engineering blog, pricing, and 13 more developer resources.'
plans:
- name: Geotab Plans Pricing
  plan_count: 2
  slug: geotab-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Geotab Rate Limits
  slug: geotab-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Geotab — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: geotab-jsonschema-spectral-rules
score:
  band: thin
  composite: 36.9
  coverage:
    artifact_dirs: 20
    catalog_earned: 66.8
    catalog_earned_first_party: 0.0
    catalog_gap: 48.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    contract_governance: 23.5
    contract_quality: 57.8
    developer_ergonomics: 31.0
    discoverability: 66.1
    operational_transparency: 13.2
  previous_composite: 36.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/geotab/geotab-2026-06-20T181804.png
security:
- kind: authentication
  name: Geotab Authentication
  slug: geotab-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Geotab Domain Security
  slug: geotab-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Geotab Vulnerability Disclosure
  slug: geotab-vulnerability-disclosure
  summary_line: no policy recorded
slug: geotab
tags:
- Fleet Management
- Telematics
- Vehicle Tracking
- ELD Compliance
- Driver Behavior
- Fuel Monitoring
- Route Optimization
- GPS Tracking
- IoT
website: https://www.geotab.com/
---
