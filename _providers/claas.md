---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 5.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: CLAAS connect APIs enable your application to be connected to the global machine and agricultural management portal CLAAS connect. These interfaces ensure secure and scalable interoperability of fleet
  name: CLAAS Connect API
  slug: claas-connect-api
artifact_total: 4
common:
- group: auth
  href: https://artifacts.apis.io/claas/scopes/claas-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/claas-scopes.yml
- group: auth
  href: https://artifacts.apis.io/claas/well-known/claas-developer-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/claas-developer-security.txt
- group: auth
  href: https://artifacts.apis.io/claas/well-known/claas-dealer-locator-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/claas-dealer-locator-security.txt
- group: agent
  href: https://artifacts.apis.io/claas/well-known/claas-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/claas-well-known.yml
- group: other
  href: https://artifacts.apis.io/claas/hosts/claas-hosts.yml
  title: ''
  type: Hosts
  url: hosts/claas-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.claas.com/en-us/about-claas/legal/legal-notice
- group: start
  title: ''
  type: Sandbox
  url: https://support.claas.com/console
- group: auth
  href: https://artifacts.apis.io/claas/security/claas-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/claas-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://claas.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.claas.com/en-gb/about-claas/partners/claas-api-partner-portal
- group: docs
  title: ''
  type: Documentation
  url: https://www.claas.com/en-gb/about-claas/partners/claas-api-partner-portal
- group: start
  title: ''
  type: GettingStarted
  url: https://www.claas.com/en-gb/about-claas/partners/claas-api-partner-portal
- group: operate
  title: ''
  type: Support
  url: https://www.claas.com/en-us/services
coverage:
  checked: '2026-10-28'
  detail: The CLAAS API Partner Portal provides marketing information but does not expose any machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications.
  evidence:
  - status: 200
    url: https://api.claas.com/openapi.json
  - status: 200
    url: https://api.claas.com/asyncapi.yaml
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: CLAAS is a German manufacturer of agricultural machinery, producing a wide range of tractors, combine harvesters, forage harvesters, balers, and other equipment for modern farming. The company focuses on innovative technology, precision farming solutions, and global service networks to support farmers worldwide.
image: https://www.claas.com/caas/v1/media/1432092/data/c6df1da409d0c037d17f96f407f13809/1138847-coa-27.jpg
layout: provider
modified: '2026-10-28'
name: CLAAS
nav: Providers
network: true
overview: 'CLAAS is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Agriculture, Machinery, Manufacturing, Germany, and Farming.


  CLAAS''s developer surface includes sandbox, documentation, getting-started guide, support, and 9 more developer resources.'
random_paper: 12
scopes:
- name: Claas Scopes
  scope_count: 2
  slug: claas-scopes
  summary_line: 2 scopes
score:
  band: emerging
  composite: 12.8
  coverage:
    artifact_dirs: 19
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.6
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 57.1
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 18.4
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/claas/claas-2026-11-03T124254.png
security:
- kind: authentication
  name: Claas Authentication
  slug: claas-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Claas Domain Security
  slug: claas-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: claas
tags:
- Agriculture
- Machinery
- Manufacturing
- Germany
- Farming
website: https://claas.com/
---
