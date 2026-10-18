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
  href: https://raw.githubusercontent.com/api-evangelist/chromaway/refs/heads/main/security/chromaway-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/chromaway-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chromaway/refs/heads/main/well-known/chromaway-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/chromaway-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/chromaway/refs/heads/main/well-known/chromaway-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/chromaway-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/chromaway/refs/heads/main/hosts/chromaway-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chromaway-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://chromaway.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://chromaway.com/news
- group: other
  title: ''
  type: Leadership
  url: https://chromaway.com/team
- group: company
  title: ''
  type: Blog
  url: https://blog.chromaway.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://blog.chromaway.com/tag/getting-started/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chromaway/refs/heads/main/security/chromaway-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/chromaway-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chromaway/refs/heads/main/security/chromaway-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chromaway-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chromaway.com/
coverage:
  checked: '2026-10-08'
  detail: The company provides blockchain infrastructure but does not expose a public developer API or documentation.
  evidence:
  - status: 200
    url: https://chromaway.com/
  reason: not-a-software-company
  state: none
created: '2026-10-08'
description: ChromaWay is a blockchain pioneer and venture builder founded in 2012, known for creating the relational blockchain platform Chromia. The company offers blockchain infrastructure, verifiable AI pipelines, and professional services, partnering with enterprises and governments to build decentralized applications and digital assets. It focuses on innovation, consulting, and development across sectors such as finance, supply chain, and public services.
image: https://www.chromaway.com/assets/images/seo/og-cover.png
layout: provider
modified: '2026-10-08'
name: ChromaWay
nav: Providers
network: true
overview: 'ChromaWay is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Blockchain, Web3, Platform, Consulting, and Ventures.


  ChromaWay''s developer surface includes engineering blog, getting-started guide, and 10 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 11.4
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 51.8
    operational_transparency: 10.5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Chromaway Domain Security
  slug: chromaway-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Chromaway Vulnerability Disclosure
  slug: chromaway-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: chromaway
tags:
- Blockchain
- Web3
- Platform
- Consulting
- Ventures
- Artificial Intelligence
website: https://chromaway.com/
---
