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
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Genlogs Agentic Access
  operation_count: 28
  slug: genlogs-agentic-access
  summary_line: 28 operations · 16 acting
api_count: 1
apis:
- baseURL: https://api.genlogs.io
  baseurl_source: declared
  description: The Alerts API from GenLogs — 2 operation(s) for alerts.
  name: GenLogs Alerts API
  slug: genlogs-alerts-api
- baseURL: https://api.genlogs.io
  baseurl_source: declared
  description: Access-token creation and refresh
  name: GenLogs Auth API
  slug: genlogs-auth-api
- baseURL: https://api.genlogs.io
  baseurl_source: declared
  description: The Carrier API from GenLogs — 3 operation(s) for carrier.
  name: GenLogs Carrier API
  slug: genlogs-carrier-api
- baseURL: https://api.genlogs.io
  baseurl_source: declared
  description: Carrier verification and vetting rules
  name: GenLogs Carrier Vetting API
  slug: genlogs-carrier-vetting-api
- baseURL: https://api.genlogs.io
  baseurl_source: declared
  description: The Compliance Rules API from GenLogs — 3 operation(s) for compliance rules.
  name: GenLogs Compliance Rules API
  slug: genlogs-compliance-rules-api
- baseURL: https://api.genlogs.io
  baseurl_source: declared
  description: The Facilities API from GenLogs — 2 operation(s) for facilities.
  name: GenLogs Facilities API
  slug: genlogs-facilities-api
- baseURL: https://api.genlogs.io
  baseurl_source: declared
  description: The Mismatch alerts API from GenLogs — 2 operation(s) for mismatch alerts.
  name: GenLogs Mismatch alerts API
  slug: genlogs-mismatch-alerts-api
- baseURL: https://api.genlogs.io
  baseurl_source: declared
  description: The Onboarded Carriers API from GenLogs — 3 operation(s) for onboarded carriers.
  name: GenLogs Onboarded Carriers API
  slug: genlogs-onboarded-carriers-api
- baseURL: https://api.genlogs.io
  baseurl_source: declared
  description: The Shipper API from GenLogs — 1 operation(s) for shipper.
  name: GenLogs Shipper API
  slug: genlogs-shipper-api
- baseURL: https://api.genlogs.io
  baseurl_source: declared
  description: The Webhook Alerts API from GenLogs — 3 operation(s) for webhook alerts.
  name: GenLogs Webhook Alerts API
  slug: genlogs-webhook-alerts-api
artifact_total: 29
asyncapis:
- description: GenLogs delivers alert.matches_found webhook notifications when detection alerts (license plate, VIN, USDOT, etc.) match roadside sensor observations. Payloads are signed with an HMAC-SHA512 signature
  name: GenLogs Alert Webhooks
  slug: genlogs-alerts-asyncapi
- description: ''
  name: Genlogs Webhooks
  slug: genlogs-webhooks
collections:
- collection_type: open
  name: GenLogs Alerts API
  slug: open-genlogs-alerts-api
- collection_type: open
  name: GenLogs Alerts auth API
  slug: open-genlogs-auth-api
- collection_type: open
  name: GenLogs Alerts Carrier API
  slug: open-genlogs-carrier-api
- collection_type: open
  name: GenLogs Alerts carrier-vetting API
  slug: open-genlogs-carrier-vetting-api
- collection_type: open
  name: GenLogs Alerts Compliance Rules API
  slug: open-genlogs-compliance-rules-api
- collection_type: open
  name: GenLogs Alerts Facilities API
  slug: open-genlogs-facilities-api
- collection_type: open
  name: GenLogs Alerts Mismatch alerts API
  slug: open-genlogs-mismatch-alerts-api
- collection_type: open
  name: GenLogs Alerts Onboarded Carriers API
  slug: open-genlogs-onboarded-carriers-api
- collection_type: open
  name: GenLogs Alerts Shipper API
  slug: open-genlogs-shipper-api
- collection_type: open
  name: GenLogs Alerts Webhook Alerts API
  slug: open-genlogs-webhook-alerts-api
common:
- group: other
  href: https://artifacts.apis.io/genlogs/capabilities/genlogs-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/genlogs-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/genlogs/mcp/genlogs-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/genlogs-mcp.yml
- group: other
  href: https://artifacts.apis.io/genlogs/overlays/genlogs-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/genlogs-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.genlogs.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.genlogs.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.genlogs.io
- group: docs
  title: ''
  type: APIReference
  url: https://docs.genlogs.io/genlogs-api-docs
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.genlogs.io/getting-started
- group: operate
  title: ''
  type: Support
  url: https://help.genlogs.io/en/
- group: company
  title: ''
  type: Blog
  url: https://genlogs.substack.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/genlogs
- group: operate
  title: ''
  type: StatusPage
  url: https://status.genlogs.io
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.genlogs.io/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://brokers.genlogs.io
- group: agent
  href: https://artifacts.apis.io/genlogs/llms/genlogs-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/genlogs-llms.txt
- group: build
  href: https://artifacts.apis.io/genlogs/packages/genlogs-packages.yml
  title: ''
  type: Packages
  url: packages/genlogs-packages.yml
- group: auth
  href: https://artifacts.apis.io/genlogs/authentication/genlogs-authentication.yml
  title: ''
  type: Authentication
  url: authentication/genlogs-authentication.yml
- group: agent
  href: https://artifacts.apis.io/genlogs/agentic-access/genlogs-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/genlogs-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/genlogs/security/genlogs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/genlogs-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/genlogs/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'GenLogs is a truck intelligence platform that provides ground-truth data on every motor carrier in America from a nationwide network of proprietary roadside sensors, satellites, and millions of data sources - 4.2 billion commercial-vehicle images with 16 million added daily, covering 97% of active motor carriers. The GenLogs API (https://api.genlogs.io) turns that sensor network into freight intelligence: source and score carriers by lane, verify a carrier was recently sighted along an origin/destination, pull carrier and FMCSA profiles, run carrier-vetting rules, discover shippers by lane and shipper facilities with GeoJSON network maps, manage onboarded-carrier contacts, track mismatch observations, and receive HMAC-SHA512-signed alert webhooks. It serves brokers and shippers, insurance underwriting and claims, law enforcement asset recovery, and carriers. Auth uses an x-api-key plus a short-lived Access-Token, with named per-endpoint permissions.'
image: https://static1.squarespace.com/static/6389ebe42811fa07a7c17692/t/67362a2579a24b6b8c42992c/1731602981116/GenLogs+logo+black.png?format=1500w
json_schemas:
- name: GenLogs alert.matches_found webhook payload
  property_count: 7
  slug: genlogs-alert-matches-found.schema
layout: provider
modified: '2026-07-19'
name: GenLogs
nav: Providers
network: true
overview: 'GenLogs publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Alerts API, Auth API, Carrier API, and 7 more. Tagged areas include Company, Logistics, Freight, Trucking, and Supply Chain.


  The GenLogs catalog on APIs.io includes 2 event-driven AsyncAPI specifications and 1 Spectral governance ruleset.


  GenLogs'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, and 14 more developer resources.'
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 106
  extends:
  - spectral:oas
  name: GenLogs API Rules
  rule_count: 65
  severity_counts:
    error: 54
    hint: 0
    info: 7
    warn: 4
  slug: genlogs-rules
score:
  band: developing
  composite: 45.5
  coverage:
    artifact_dirs: 24
    catalog_earned: 46.9
    catalog_earned_first_party: 0.0
    catalog_gap: 68.1
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.4
  facets:
    access_clarity: 17.1
    contract_governance: 18.2
    contract_quality: 71.3
    developer_ergonomics: 58.9
    discoverability: 73.2
    operational_transparency: 26.3
  previous_composite: 44.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 10
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 18.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/genlogs/genlogs-2026-07-25T215622.png
security:
- kind: authentication
  name: Genlogs Authentication
  slug: genlogs-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Genlogs Domain Security
  slug: genlogs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: Configure and test alert webhooks
  slug: genlogs-alert-webhooks
- name: Source and verify carriers on a lane
  slug: genlogs-source-carriers-by-lane
slug: genlogs
tags:
- Company
- Logistics
- Freight
- Trucking
- Supply Chain
- Carrier Intelligence
- Fleet Management
- Transportation
- Insurance
- Fraud Prevention
- Webhook
- Geospatial
website: https://www.genlogs.io
---
