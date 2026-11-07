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
    protected_resource_metadata: documented
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 4.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/broen-tech/well-known/broen-tech-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/broen-tech-security.txt
- group: agent
  href: https://artifacts.apis.io/broen-tech/well-known/broen-tech-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/broen-tech-well-known.yml
- group: other
  href: https://artifacts.apis.io/broen-tech/hosts/broen-tech-hosts.yml
  title: ''
  type: Hosts
  url: hosts/broen-tech-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://broen.tech/terms
- group: auth
  title: ''
  type: Security
  url: https://broen.tech/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://broen.tech/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://broen.tech/news
- group: start
  title: ''
  type: Login
  url: https://broen.tech/signin
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Stiander
- group: company
  title: ''
  type: Blog
  url: https://broen.tech/blog
- group: auth
  href: https://artifacts.apis.io/broen-tech/security/broen-tech-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/broen-tech-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/broen-tech/security/broen-tech-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/broen-tech-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://broen.tech/
coverage:
  checked: '2026-11-03'
  detail: The site provides no developer program or API documentation.
  evidence:
  - status: 200
    url: https://broen.tech/
  reason: no-developer-program
  state: none
created: '2026-11-03'
description: Broentech builds AI products — ASMI, a design-time builder for conversational avatars — and ships production software for clients from Horten, Norway. The company focuses on AI-driven solutions, ESG compliance automation, and consulting services, delivering end‑to‑end software engineering for enterprises.
image: https://broen.tech/images/og-default.png
layout: provider
modified: '2026-11-03'
name: Broentech
nav: Providers
network: true
overview: 'Broentech is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Software, Consulting, ESG, and Norway.


  Broentech''s developer surface includes engineering blog and 12 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 49.1
    operational_transparency: 7.9
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Broen Tech Domain Security
  slug: broen-tech-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Broen Tech Vulnerability Disclosure
  slug: broen-tech-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: broen-tech
tags:
- Artificial Intelligence
- Software
- Consulting
- ESG
- Norway
- Company
website: https://broen.tech/
---
