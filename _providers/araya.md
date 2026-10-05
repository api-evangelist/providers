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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/araya/refs/heads/main/hosts/araya-hosts.yml
  title: ''
  type: Hosts
  url: hosts/araya-hosts.yml
- group: auth
  title: ''
  type: Security
  url: https://www.araya.org/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.araya.org/privacy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.araya.org/publications_category_en/news/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/araya/refs/heads/main/security/araya-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/araya-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.araya.org/en/
- group: docs
  title: ''
  type: Documentation
  url: https://www.araya.org/en/about/company/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.araya.org/en/about/
- group: operate
  title: ''
  type: Contact
  url: https://www.araya.org/en/contact/
coverage:
  checked: 2026-09-25
  detail: The provider's website offers HTML documentation but no machine‑readable OpenAPI, AsyncAPI, GraphQL or other contract was found.
  evidence:
  - status: 200
    url: https://www.araya.org/en/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-25'
description: Araya is a Japanese AI and neurotechnology company focused on integrating cutting‑edge artificial intelligence and brain‑machine interface research into business and daily life. The company offers custom AI development, edge AI consulting, advanced research support for large language models, and neurotech solutions aimed at improving industry processes and human‑machine interaction. Its mission is to create an overwhelmingly interesting future for workers, researchers, and society by bridging scientific innovation with practical applications.
image: https://www.araya.org/wp-content/uploads/2021/04/arayatw.png
layout: provider
modified: '2026-09-25'
name: Araya
nav: Providers
network: true
overview: 'Araya is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Neurotechnology, Japan, Business, and Innovation.


  Araya''s developer surface includes documentation, getting-started guide, and 7 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 11.8
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 50.0
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - japan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Araya Domain Security
  slug: araya-domain-security
  summary_line: TLSv1.3 · DMARC
slug: araya
tags:
- Artificial Intelligence
- Neurotechnology
- Japan
- Business
- Innovation
website: https://www.araya.org/en/
---
