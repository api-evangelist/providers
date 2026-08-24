---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
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
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.9
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 4
  human_in_the_loop: 1
  name: Geotab Agentic Access
  operation_count: 5
  slug: geotab-agentic-access
  summary_line: 5 operations · 4 acting · 1 human-in-the-loop
api_count: 5
apis:
- description: The MyGeotab API provides JSON-RPC 2.0 access to all fleet telematics data including vehicle location, trip history, driver behavior, fault codes, fuel usage, HOS/ELD compliance records, and sensor da
  name: MyGeotab API
  slug: mygeotab-api
- description: The MyAdmin API provides reseller and partner access to Geotab's administrative platform for managing databases, device provisioning, orders, billing, and account management. Access requires a MyAdmin
  name: MyAdmin API
  slug: myadmin-api
- description: The Authentication API from Geotab — 3 operation(s) for authentication.
  name: Geotab Authentication API
  slug: geotab-authentication-api
- description: The Invalid Records API from Geotab — 1 operation(s) for invalid records.
  name: Geotab Invalid Records API
  slug: geotab-invalid-records-api
- description: The Records API from Geotab — 1 operation(s) for records.
  name: Geotab Records API
  slug: geotab-records-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/geotab-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/geotab-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/geotab-domain-security.yml
- group: auth
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
  title: ''
  type: Plans
  url: plans/geotab-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/geotab-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/geotab-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/geotab-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/geotab-context.jsonld
- group: company
  title: ''
  type: Blog
  url: blogs/blogs.json
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
- name: Geotab Finops
  service_category: ''
  slug: geotab-finops
graphqls:
- description: Geotab is a fleet management and connected vehicle platform. The API covers device management, vehicle tracking, trips, exceptions, diagnostics, engine data, driver behavior, hours of service complian
  name: Geotab GraphQL API
  slug: geotab-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/geotab.png
json_schemas:
- name: GpsRecord
  property_count: 0
  slug: geotab-gps-record
- name: StatusRecord
  property_count: 0
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
overview: 'Geotab publishes 3 APIs on the [APIs.io](https://apis.io/) network: Authentication API, Invalid Records API, and Records API. Tagged areas include Fleet Management, Telematics, Vehicle Tracking, ELD Compliance, and Driver Behavior.


  The Geotab catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Geotab''s developer surface includes authentication, documentation, engineering blog, pricing, and 13 more developer resources.'
plans:
- name: Geotab Plans Pricing
  plan_count: 2
  slug: geotab-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Geotab Rate Limits
  slug: geotab-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Geotab API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: geotab-jsonschema-spectral-rules
score:
  band: thin
  composite: 39.1
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 25.0
    contract_quality: 62.6
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 25.0
    operational_transparency: 2.6
  previous_composite: 39.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/geotab/refs/heads/main/screenshots/geotab-2026-06-20T181804.png
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
  summary_line: disclosure policy published
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
