---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API to connect to the Meadow platform
  name: Meadow API
  slug: meadow-api
artifact_total: 4
common:
- group: operate
  href: https://artifacts.apis.io/getmeadow-com/rate-limits/getmeadow-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/getmeadow-com-rate-limits.yml
- group: operate
  href: https://artifacts.apis.io/getmeadow-com/changelog/getmeadow-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/getmeadow-com-changelog.yml
- group: auth
  href: https://artifacts.apis.io/getmeadow-com/authentication/getmeadow-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/getmeadow-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/getmeadow-com/conformance/getmeadow-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/getmeadow-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/getmeadow-com/llms/getmeadow-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/getmeadow-com-llms.txt
- group: other
  href: https://artifacts.apis.io/getmeadow-com/a2a/getmeadow-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/getmeadow-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/getmeadow-com/well-known/getmeadow-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/getmeadow-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/getmeadow-com/hosts/getmeadow-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/getmeadow-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/getmeadow-com/vendors/getmeadow-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/getmeadow-com-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/meadow
- group: operate
  title: ''
  type: ChangeLog
  url: https://api-docs.getmeadow.com/changelog
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.getmeadow.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.getmeadow.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/getmeadow-com/security/getmeadow-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/getmeadow-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://getmeadow.com
- group: commercial
  title: ''
  type: Pricing
  url: https://getmeadow.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://getmeadow.com/blog
- group: company
  title: ''
  type: About
  url: https://getmeadow.com/about
- group: commercial
  title: ''
  type: TermsOfService
  url: https://getmeadow.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://getmeadow.com/legal/privacy-policy
created: '2026-10-29'
description: Meadow provides a comprehensive cannabis point‑of‑sale (POS) and e‑commerce platform for dispensaries across the United States. Founded in 2014, Meadow offers integrated inventory management, compliance reporting, delivery logistics, and retail analytics, helping cannabis retailers streamline operations and scale across multiple states. The platform supports integrations with major partners and delivers a unified dashboard for sales, compliance, and customer engagement.
image: https://images.ctfassets.net/6kwu1u6s8j23/KQ4SXA1l85wsCNt4aA1Pp/328c29905e8489630079ab5ad8db6555/index.png?fm=jpg
layout: provider
modified: '2026-10-29'
name: Meadow
nav: Providers
network: true
overview: 'Meadow is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cannabis, Point-of-Sale, E-Commerce, and Software-as-a-Service.


  Meadow''s developer surface includes changelog, authentication, documentation, API reference, pricing, engineering blog, and 14 more developer resources.'
random_paper: 1
rate_limits:
- limit_count: 2
  name: Getmeadow Com Rate Limits
  slug: getmeadow-com-rate-limits
score:
  band: emerging
  composite: 20.2
  coverage:
    artifact_dirs: 17
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.1
  facets:
    access_clarity: 15.8
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 73.2
    operational_transparency: 31.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 27.3
  provenance:
    conformance: derived
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/getmeadow-com/getmeadow-com-2026-11-03T132731.png
security:
- kind: authentication
  name: Getmeadow Com Authentication
  slug: getmeadow-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Getmeadow Com Domain Security
  slug: getmeadow-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: getmeadow-com
tags:
- Company
- Cannabis
- Point-of-Sale
- E-Commerce
- Software-as-a-Service
website: https://getmeadow.com
---
