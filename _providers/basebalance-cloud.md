---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/basebalance-cloud/vendors/basebalance-cloud-vendors.yml
  title: ''
  type: Vendors
  url: vendors/basebalance-cloud-vendors.yml
- group: other
  href: https://artifacts.apis.io/basebalance-cloud/hosts/basebalance-cloud-hosts.yml
  title: ''
  type: Hosts
  url: hosts/basebalance-cloud-hosts.yml
- group: company
  title: ''
  type: Website
  url: https://basebalance.cloud/
- group: auth
  href: https://artifacts.apis.io/basebalance-cloud/security/basebalance-cloud-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/basebalance-cloud-domain-security.yml
coverage:
  checked: '2026-11-02'
  detail: No public API documentation or machine-readable contract was found on the provider's hosts.
  evidence:
  - status: 0
    url: https://api.basebalance.cloud/openapi.json
  reason: no-developer-program
  state: none
created: '2026-11-02'
description: 'basebalance-cloud is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
image: https://blackhorizons.es/assets/og-image.jpg
layout: provider
modified: '2026-11-02'
name: basebalance-cloud
nav: Providers
network: true
overview: basebalance-cloud is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 21
score:
  band: minimal
  composite: 1.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 17.0
    catalog_earned_first_party: 0.0
    catalog_gap: 98.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 30.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Basebalance Cloud Domain Security
  slug: basebalance-cloud-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: basebalance-cloud
tags:
- Company
website: https://basebalance.cloud/
---
