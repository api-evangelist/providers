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
  band: agent-aware
  dimensions:
    agent_card: flavored
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
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 10.1
  scored_at: '2026-09-16'
api_count: 1
apis:
- description: Internet censorship measurements, incidents, and ISP-level blocking data across 126 countries
  name: Voidly
  slug: voidly
artifact_total: 3
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/voidly/refs/heads/main/a2a/voidly-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/voidly-a2a.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/voidly/refs/heads/main/security/voidly-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/voidly-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/voidly/refs/heads/main/security/voidly-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/voidly-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://voidly.ai/api-docs
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: operate
  title: ''
  type: Support
  url: mailto:support@voidly.ai
created: '2026-05-28'
description: Internet censorship measurements, incidents, and ISP-level blocking data across 126 countries
layout: provider
modified: '2026-05-28'
name: Voidly
nav: Providers
network: true
overview: 'Voidly publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data and Public APIs.


  Voidly''s developer surface includes support and 5 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 8.3
  coverage:
    artifact_dirs: 4
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
    developer_ergonomics: 14.3
    discoverability: 53.7
    operational_transparency: 0.0
  previous_composite: 8.3
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 22.2
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/voidly/refs/heads/main/screenshots/voidly-2026-06-20T201129.png
security:
- kind: domain-security
  name: Voidly Domain Security
  slug: voidly-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Voidly Vulnerability Disclosure
  slug: voidly-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: voidly
tags:
- Open Data
- Public APIs
website: https://voidly.ai/api-docs
---
