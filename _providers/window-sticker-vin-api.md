---
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: na
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 32.1
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Window Sticker Vin Api Agentic Access
  operation_count: 4
  slug: window-sticker-vin-api-agentic-access
  summary_line: 4 operations
api_count: 1
apis:
- baseURL: https://windowsticker.org
  baseurl_source: spec
  description: The Sticker API from Window Sticker VIN API — 1 operation(s) for sticker.
  name: Window Sticker VIN API Sticker API
  slug: window-sticker-vin-api-sticker-api
- baseURL: https://windowsticker.org
  baseurl_source: spec
  description: The Vin API from Window Sticker VIN API — 1 operation(s) for vin.
  name: Window Sticker VIN API Vin API
  slug: window-sticker-vin-api-vin-api
artifact_total: 11
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/window-sticker-vin-api/refs/heads/main/agentic-access/window-sticker-vin-api-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/window-sticker-vin-api-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/window-sticker-vin-api/refs/heads/main/rules/window-sticker-vin-api-rules.yml
  title: ''
  type: Spectral
  url: rules/window-sticker-vin-api-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/window-sticker-vin-api/refs/heads/main/json-ld/window-sticker-vin-api-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/window-sticker-vin-api-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/window-sticker-vin-api/refs/heads/main/vocabulary/window-sticker-vin-api-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/window-sticker-vin-api-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/window-sticker-vin-api/refs/heads/main/llms/window-sticker-vin-api-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/window-sticker-vin-api-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/window-sticker-vin-api/refs/heads/main/mcp/window-sticker-vin-api-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/window-sticker-vin-api-mcp.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/window-sticker-vin-api/refs/heads/main/hosts/window-sticker-vin-api-hosts.yml
  title: ''
  type: Hosts
  url: hosts/window-sticker-vin-api-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/window-sticker-vin-api/refs/heads/main/vendors/window-sticker-vin-api-vendors.yml
  title: ''
  type: Vendors
  url: vendors/window-sticker-vin-api-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://windowsticker.org/terms
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/window-sticker-vin-api/refs/heads/main/overlays/window-sticker-vin-api-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/window-sticker-vin-api-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://windowsticker.org/
- group: docs
  title: ''
  type: Documentation
  url: https://windowsticker.org/api-docs
- group: docs
  title: ''
  type: APIReference
  url: https://windowsticker.org/api-docs
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://windowsticker.org/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://windowsticker.org/status
- group: agent
  title: ''
  type: LLMsTxt
  url: https://windowsticker.org/llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/window-sticker-vin-api/refs/heads/main/well-known/window-sticker-vin-api-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/window-sticker-vin-api-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/window-sticker-vin-api/refs/heads/main/authentication/window-sticker-vin-api-authentication.yml
  title: ''
  type: Authentication
  url: authentication/window-sticker-vin-api-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/window-sticker-vin-api/refs/heads/main/conventions/window-sticker-vin-api-conventions.yml
  title: ''
  type: Conventions
  url: conventions/window-sticker-vin-api-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/window-sticker-vin-api/refs/heads/main/lifecycle/window-sticker-vin-api-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/window-sticker-vin-api-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/window-sticker-vin-api/refs/heads/main/conformance/window-sticker-vin-api-conformance.yml
  title: ''
  type: Conformance
  url: conformance/window-sticker-vin-api-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/window-sticker-vin-api/refs/heads/main/security/window-sticker-vin-api-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/window-sticker-vin-api-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/window-sticker-vin-api/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/window-sticker-vin-api/refs/heads/main/rate-limits/window-sticker-vin-api-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/window-sticker-vin-api-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/window-sticker-vin-api/refs/heads/main/plans/window-sticker-vin-api-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/window-sticker-vin-api-plans-pricing.yml
created: '2026-09-19'
description: A free, keyless VIN-lookup service that returns the original factory window sticker (Monroney label) PDF plus an NHTSA vPIC specification decode for any 17-character US VIN. Serves decoded vehicle specs, EPA fuel economy, crash ratings, and recalls over an open, CORS-enabled JSON API with no registration, no API key and no paid tiers. Factory PDFs are available for 16 makes (Ford, GM, Stellantis, Subaru, Kia, Hyundai, Genesis and more); every other make still returns a full specification decode.
image: https://windowsticker.org/og.png
json_schemas:
- name: VinResponse
  property_count: 5
  slug: window-sticker-vin-api-vin-response
jsonld:
- class_count: 1
  name: Window Sticker Vin Api Context
  property_count: 5
  slug: window-sticker-vin-api-context
layout: provider
mcp_servers:
- description: ''
  name: Window Sticker VIN API MCP Server
  slug: window-sticker-vin-api-mcp-server
modified: '2026-09-20'
name: Window Sticker VIN API
nav: Providers
network: true
overview: 'Window Sticker VIN API publishes 2 APIs on the [APIs.io](https://apis.io/) network: Sticker API and Vin API. Tagged areas include Automotive, Vehicle Data, VIN Decoding, Monroney, and Window sticker.


  The Window Sticker VIN API catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Window Sticker VIN API''s developer surface includes documentation, API reference, authentication, and 22 more developer resources.'
plans:
- name: Window Sticker Vin Api Plans Pricing
  plan_count: 0
  slug: window-sticker-vin-api-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Window Sticker Vin Api Rate Limits
  slug: window-sticker-vin-api-rate-limits
rules:
- effective_rule_count: 53
  extends:
  - spectral:oas
  name: Window Sticker VIN API API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: window-sticker-vin-api-rules
score:
  band: thin
  composite: 35.5
  coverage:
    artifact_dirs: 25
    catalog_earned: 45.2
    catalog_earned_first_party: 0.0
    catalog_gap: 69.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 7.5
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 50.5
    developer_ergonomics: 30.4
    discoverability: 61.7
    operational_transparency: 15.8
  previous_composite: 28.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 24.5
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: authentication
  name: Window Sticker Vin Api Authentication
  slug: window-sticker-vin-api-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Window Sticker Vin Api Domain Security
  slug: window-sticker-vin-api-domain-security
  summary_line: TLSv1.3 · HSTS
slug: window-sticker-vin-api
tags:
- Automotive
- Vehicle Data
- VIN Decoding
- Monroney
- Window sticker
- Government open data
- Auto Retail
- Dealer tooling
website: https://windowsticker.org/
---
