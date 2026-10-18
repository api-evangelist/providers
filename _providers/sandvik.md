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
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sandvik/refs/heads/main/well-known/sandvik-home-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/sandvik-home-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sandvik/refs/heads/main/security/sandvik-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/sandvik-vulnerability-disclosure.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/sandvik/refs/heads/main/llms/sandvik-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sandvik-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sandvik/refs/heads/main/well-known/sandvik-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/sandvik-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/sandvik/refs/heads/main/well-known/sandvik-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sandvik-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sandvik/refs/heads/main/hosts/sandvik-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sandvik-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sandvik/refs/heads/main/vendors/sandvik-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sandvik-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.home.sandvik/en/news-and-media/news/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sandvik/refs/heads/main/security/sandvik-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/sandvik-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sandvik/refs/heads/main/security/sandvik-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sandvik-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://home.sandvik/
coverage:
  checked: '2026-10-15'
  detail: No OpenAPI or other machine‑readable contract was found at the API host.
  evidence:
  - status: 0
    url: https://api.home.sandvik/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-14'
description: Sandvik is a global engineering group that provides equipment, tools and services for the mining, construction, and manufacturing industries. With a focus on innovation, sustainability and digitalization, Sandvik delivers solutions that improve productivity, safety and environmental performance across the entire value chain. The company operates in more than 150 countries, serving customers in mining, rock processing, metal cutting, tooling and additive manufacturing, while investing heavily in research and development to drive future technologies.
image: https://www.home.sandvik/cdn-cgi/image/w=1200,h=630,quality=90,fit=cover,format=avif/contentassets/8ab126e3464d4aaf8a2246d00c89b4fe/sandvik_og.jpg?v=1789038534
layout: provider
modified: '2026-10-14'
name: Sandvik
nav: Providers
network: true
overview: Sandvik is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Manufacturing, Mining, Infrastructure, Engineering, and Sustainability.
random_paper: 4
score:
  band: minimal
  composite: 6.6
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 10.5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Sandvik Domain Security
  slug: sandvik-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sandvik Vulnerability Disclosure
  slug: sandvik-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: sandvik
tags:
- Manufacturing
- Mining
- Infrastructure
- Engineering
- Sustainability
- Digitalization
website: https://home.sandvik/
---
