---
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Crossover provides a developer portal with API reference pages, but no machine‑readable OpenAPI/GraphQL/AsyncAPI contract was found.
  name: Crossover API
  slug: crossover-api
artifact_total: 3
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/crossover/refs/heads/main/well-known/crossover-clarity-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/crossover-clarity-security.txt
- group: auth
  title: ''
  type: Security
  url: https://clarity.com/vdp
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/crossover/refs/heads/main/well-known/crossover-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/crossover-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/crossover/refs/heads/main/well-known/crossover-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/crossover-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/crossover/refs/heads/main/hosts/crossover-hosts.yml
  title: ''
  type: Hosts
  url: hosts/crossover-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/crossover/refs/heads/main/vendors/crossover-vendors.yml
  title: ''
  type: Vendors
  url: vendors/crossover-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.crossover.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/crossover/refs/heads/main/security/crossover-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/crossover-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/crossover/refs/heads/main/security/crossover-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crossover-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://crossoverhealth.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.crossover.com/about
- group: docs
  title: ''
  type: Documentation
  url: https://www.crossover.com/help
- group: docs
  title: ''
  type: APIReference
  url: https://www.crossover.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://www.crossover.com/selection-process
- group: operate
  title: ''
  type: Support
  url: https://www.crossover.com/help
- group: company
  title: ''
  type: Blog
  url: https://www.crossover.com/resources
- group: commercial
  title: ''
  type: Pricing
  url: https://www.crossover.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.crossover.com/hire
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.crossover.com/website-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.crossover.com/privacy-policy
coverage:
  checked: '2026-10-11'
  detail: 'API reference page https://www.crossover.com/api returns HTML with no machine‑readable spec, and attempts to fetch OpenAPI endpoints returned 404. '
  evidence:
  - status: 200
    url: https://www.crossover.com/api
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-11'
description: Crossover is a global recruitment platform that connects top 1% talent with AI‑first remote full‑time job opportunities. It offers a sophisticated matching system, productivity monitoring tools like WorkSmart, and serves over 70 leading tech companies. The service includes hiring solutions for enterprises and career resources for job seekers, positioning Crossover as a leading marketplace for remote work.
layout: provider
modified: '2026-10-11'
name: Crossover
nav: Providers
network: true
overview: 'Crossover is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Recruiting, Remote Work, Artificial Intelligence, and TalentMarketplace.


  Crossover''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 13 more developer resources.'
random_paper: 8
score:
  band: thin
  composite: 27.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 53.6
    operational_transparency: 26.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Crossover Domain Security
  slug: crossover-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Crossover Vulnerability Disclosure
  slug: crossover-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: crossover
tags:
- Company
- Recruiting
- Remote Work
- Artificial Intelligence
- TalentMarketplace
website: https://crossoverhealth.com
---
