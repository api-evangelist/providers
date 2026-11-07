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
api_count: 1
apis:
- description: API documentation and developer guides for CSIDIA's AI automation platform.
  name: CSIDIA API
  slug: csidia-api
artifact_total: 2
common:
- group: design
  href: https://artifacts.apis.io/csidia-com/conformance/csidia-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/csidia-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/csidia-com/llms/csidia-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/csidia-com-llms.txt
- group: other
  href: https://artifacts.apis.io/csidia-com/hosts/csidia-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/csidia-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/csidia-com/vendors/csidia-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/csidia-com-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://csidia.com/privacy/
- group: docs
  title: ''
  type: Documentation
  url: https://csidia.com/en/guides/
- group: auth
  href: https://artifacts.apis.io/csidia-com/security/csidia-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/csidia-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://csidia.com/
coverage:
  checked: '2026-11-04'
  detail: Documentation pages exist but no OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found.
  evidence:
  - status: 200
    url: https://csidia.com/en/guides/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: CSIDIA S.r.l. provides AI‑driven automation platforms that turn enterprise data into actionable decisions and actions. Based in Vignola, Italy, the company builds data and AI platforms designed for European compliance, offering tools for operational AI, governance, and integration across business processes.
image: https://csidia.com/og.png
layout: provider
modified: '2026-11-04'
name: CSIDIA S.r.l.
nav: Providers
network: true
overview: 'CSIDIA S.r.l. is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Automation, Data, and Europe.


  CSIDIA S.r.l.''s developer surface includes documentation and 7 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 11.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 57.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - italy
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Csidia Com Domain Security
  slug: csidia-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: csidia-com
tags:
- Company
- Artificial Intelligence
- Automation
- Data
- Europe
website: https://csidia.com/
---
