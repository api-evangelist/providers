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
    agent_card: conformant
    agent_skills: unknown
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 9.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for AstraNL coordination platform.
  name: AstraNL API
  slug: astranl-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/astranl-com/plans/astranl-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/astranl-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/astranl-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://astranl.com/spec/
- group: design
  href: https://artifacts.apis.io/astranl-com/conformance/astranl-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/astranl-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/astranl-com/llms/astranl-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/astranl-com-llms.txt
- group: other
  href: https://artifacts.apis.io/astranl-com/a2a/astranl-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/astranl-com-a2a.yml
- group: auth
  href: https://artifacts.apis.io/astranl-com/well-known/astranl-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/astranl-com-security.txt
- group: agent
  href: https://artifacts.apis.io/astranl-com/well-known/astranl-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/astranl-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/astranl-com/hosts/astranl-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/astranl-com-hosts.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://astranl.com/uk/pricing/
- group: auth
  href: https://artifacts.apis.io/astranl-com/security/astranl-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/astranl-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/astranl-com/security/astranl-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/astranl-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://astranl.com/
- group: docs
  title: ''
  type: Documentation
  url: https://astranl.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://astranl.com/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://astranl.com/welcome/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://astranl.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://astranl.com/privacy
created: '2026-10-29'
description: AstraNL is a Dutch‑based coordination platform that lets users describe tasks, collect a 1 % coordination fee, and never holds funds. It offers a simple web interface for submitting requests, integrates with Stripe for payments, and provides an OpenAPI specification at https://astranl.com/openapi.json for programmatic access.
image: https://astranl.com/og-image.png
layout: provider
modified: '2026-10-29'
name: astranl-com
nav: Providers
network: true
overview: 'astranl-com publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Coordination, Payments, Platform, and NL.


  astranl-com''s developer surface includes pricing, documentation, API reference, getting-started guide, and 14 more developer resources.'
plans:
- name: Astranl Com Plans Pricing
  plan_count: 3
  slug: astranl-com-plans-pricing
random_paper: 17
score:
  band: emerging
  composite: 22.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.2
  facets:
    access_clarity: 47.4
    contract_governance: 4.5
    contract_quality: 6.0
    developer_ergonomics: 20.7
    discoverability: 73.2
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - netherlands
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 30.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 41
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/astranl-com/astranl-com-2026-11-03T121225.png
security:
- kind: authentication
  name: Astranl Com Authentication
  slug: astranl-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Astranl Com Domain Security
  slug: astranl-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Astranl Com Vulnerability Disclosure
  slug: astranl-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: astranl-com
tags:
- Company
- Coordination
- Payments
- Platform
- NL
website: https://astranl.com/
---
