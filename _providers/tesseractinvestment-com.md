---
access_model:
  confidence: low
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 6
common:
- group: other
  href: https://artifacts.apis.io/tesseractinvestment-com/hosts/tesseractinvestment-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tesseractinvestment-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/tesseractinvestment-com/security/tesseractinvestment-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tesseractinvestment-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tesseractinvestment.com/
coverage:
  checked: '2026-10-29'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract files were discoverable despite probing known hosts.
  evidence:
  - status: host-unresolved
    url: https://api.tesseractinvestment.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: 'Tesseract is a company surfaced via the API Evangelist harvest backlog (source: vc-portfolio; backed by sapphire-ventures) and added to the network as a stub for full-pipeline profiling.'
jsonld:
- class_count: 40
  name: Tesseractinvestment Com Context
  property_count: 37
  slug: tesseractinvestment-com-context
layout: provider
modified: '2026-10-29'
name: Tesseract
nav: Providers
network: true
overview: 'Tesseract is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  The Tesseract catalog on APIs.io includes 1 JSON-LD context.'
plans:
- name: Tesseractinvestment Com Plans Pricing
  plan_count: 0
  slug: tesseractinvestment-com-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Tesseractinvestment Com Rate Limits
  slug: tesseractinvestment-com-rate-limits
scopes:
- name: Tesseractinvestment Com Scopes
  scope_count: 0
  slug: tesseractinvestment-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 7.7
  coverage:
    artifact_dirs: 26
    catalog_earned: 26.0
    catalog_earned_first_party: 0.0
    catalog_gap: 89.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 14.7
    developer_ergonomics: 0.0
    discoverability: 26.8
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 7.7
  provenance:
    conformance: derived
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: authentication
  name: Tesseractinvestment Com Authentication
  slug: tesseractinvestment-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Tesseractinvestment Com Domain Security
  slug: tesseractinvestment-com-domain-security
  summary_line: DMARC
slug: tesseractinvestment-com
tags:
- Company
website: https://tesseractinvestment.com/
---
