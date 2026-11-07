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
artifact_total: 5
common:
- group: other
  href: https://artifacts.apis.io/bnetd-ci/hosts/bnetd-ci-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bnetd-ci-hosts.yml
- group: auth
  href: https://artifacts.apis.io/bnetd-ci/security/bnetd-ci-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bnetd-ci-domain-security.yml
coverage:
  checked: '2026-10-29'
  detail: No API documentation or machine‑readable contract was found after probing known hosts and attempting to locate a website.
  evidence:
  - status: 200
    url: https://bnetd.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: No public description is available for Bureau National d'Etudes Techniques et de Developpement (BNETD). The company appears in the API Evangelist harvest backlog as a stub with limited publicly available information. Attempts to locate an official website or detailed corporate information were unsuccessful; the domain https://bnetd.com redirects to a GoDaddy for‑sale page, and other plausible domains do not resolve. No GitHub organization, documentation site, or other authoritative source was found. Consequently, the available public data consists only of the company name and its inclusion in the harvest list.
layout: provider
modified: '2026-10-29'
name: Bureau National d'Etudes Techniques et de Developpement (BNETD)
nav: Providers
network: true
overview: Bureau National d'Etudes Techniques et de Developpement (BNETD) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Research, Development, France, and Technology.
plans:
- name: Bnetd Ci Plans Pricing
  plan_count: 0
  slug: bnetd-ci-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Bnetd Ci Rate Limits
  slug: bnetd-ci-rate-limits
scopes:
- name: Bnetd Ci Scopes
  scope_count: 0
  slug: bnetd-ci-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 4.6
  coverage:
    artifact_dirs: 19
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 4.6
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bnetd Ci Authentication
  slug: bnetd-ci-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Bnetd Ci Domain Security
  slug: bnetd-ci-domain-security
  summary_line: DMARC
slug: bnetd-ci
tags:
- Company
- Research
- Development
- France
- Technology
- Engineering
---
