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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API reference page is gated (403 Forbidden) and does not expose a machine-readable contract.
  name: Sofortfax API
  slug: sofortfax-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/sofortfax-de/llms/sofortfax-de-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sofortfax-de-llms.txt
- group: commercial
  href: https://artifacts.apis.io/sofortfax-de/plans/sofortfax-de-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sofortfax-de-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/sofortfax-de/authentication/sofortfax-de-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sofortfax-de-authentication.yml
- group: design
  href: https://artifacts.apis.io/sofortfax-de/errors/sofortfax-de-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/sofortfax-de-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/sofortfax-de/well-known/sofortfax-de-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sofortfax-de-well-known.yml
- group: other
  href: https://artifacts.apis.io/sofortfax-de/hosts/sofortfax-de-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sofortfax-de-hosts.yml
- group: company
  title: ''
  type: Blog
  url: https://sofortfax.de/blog/
- group: company
  title: ''
  type: Website
  url: https://sofortfax.de/
- group: auth
  href: https://artifacts.apis.io/sofortfax-de/security/sofortfax-de-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sofortfax-de-domain-security.yml
coverage:
  checked: '2026-10-29'
  detail: API reference page https://sofortfax.de/api/ returns 403 Forbidden, indicating access requires login.
  evidence:
  - status: 403
    url: https://sofortfax.de/api/
  reason: partner-login
  state: gated
created: '2026-10-29'
description: 'sofortfax-de is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full‑pipeline profiling. During the identity investigation, no public website, documentation, or API endpoints were found that reliably identify the company''s services or domain ownership. The domain sofortfax.de currently serves unrelated content and does not reference the company, so the website pointer has been removed. This entry records the limited publicly available information about the provider.'
image: https://via.placeholder.com/150
layout: provider
modified: '2026-10-29'
name: sofortfax-de
nav: Providers
network: true
overview: 'sofortfax-de is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Germany, Fax, and Telecommunications.


  sofortfax-de''s developer surface includes authentication, engineering blog, and 7 more developer resources.'
plans:
- name: Sofortfax De Plans Pricing
  plan_count: 6
  slug: sofortfax-de-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Sofortfax De Rate Limits
  slug: sofortfax-de-rate-limits
scopes:
- name: Sofortfax De Scopes
  scope_count: 0
  slug: sofortfax-de-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 15.1
  coverage:
    artifact_dirs: 20
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.1
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 13.1
    discoverability: 55.4
    operational_transparency: 0.0
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
  previous_composite: 16.2
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 24.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/sofortfax-de/sofortfax-de-2026-11-03T143446.png
security:
- kind: authentication
  name: Sofortfax De Authentication
  slug: sofortfax-de-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Sofortfax De Domain Security
  slug: sofortfax-de-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sofortfax-de
tags:
- Company
- Germany
- Fax
- Telecommunications
website: https://sofortfax.de/
---
