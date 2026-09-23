---
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
  score: 15.1
  scored_at: '2026-09-23'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/lseg/refs/heads/main/well-known/lseg-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/lseg-well-known.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lseg/refs/heads/main/conventions/lseg-conventions.yml
  title: ''
  type: Conventions
  url: conventions/lseg-conventions.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/lseg/refs/heads/main/sandbox/lseg-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/lseg-sandbox.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.lseg.com/en/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://support.lseg.com/s/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lseg.com/en/policies/privacy-statement
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.lseg.com/en
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.lseg.com/en/api-catalog/app-studio/app-studio-web-sdk/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://developers.lseg.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LSEG
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/lseg/refs/heads/main/security/lseg-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lseg-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.lseg.com/
coverage:
  checked: 2026-09-21
  detail: Developer portal pages are rendered via JavaScript and provide no machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://developers.lseg.com/en
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-21'
description: LSEG (London Stock Exchange Group) is a leading global financial markets infrastructure and data provider, offering a broad range of services including data & analytics, FTSE Russell indices, trading venues, FX, post‑trade solutions and risk intelligence. It serves customers worldwide, enabling sustainable growth and stability through trusted data and innovative technology platforms.
image: https://www.lseg.com/content/dam/lseg/en_us/images/logos/thumbnail/lseg-default-social-image.jpg.transform/rect-768/q90/image.jpg
layout: provider
modified: '2026-09-21'
name: LSEG
nav: Providers
network: true
overview: 'LSEG is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Data, Infrastructure, and Markets.


  LSEG''s developer surface includes sandbox, support, getting-started guide, documentation, and 8 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 18.5
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 50.0
    operational_transparency: 5.3
  previous_composite: 18.5
  provenance:
    mcp: derived
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Lseg Domain Security
  slug: lseg-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: lseg
tags:
- Company
- Finance
- Data
- Infrastructure
- Markets
website: https://www.lseg.com/
---
