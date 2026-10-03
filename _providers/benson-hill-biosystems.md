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
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: API documentation hosted at Confluence Genetics website, but no machine-readable contract found.
  name: Confluence Genetics API
  slug: confluence-genetics-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/benson-hill-biosystems/refs/heads/main/hosts/benson-hill-biosystems-hosts.yml
  title: ''
  type: Hosts
  url: hosts/benson-hill-biosystems-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/benson-hill-biosystems/refs/heads/main/vendors/benson-hill-biosystems-vendors.yml
  title: ''
  type: Vendors
  url: vendors/benson-hill-biosystems-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/benson-hill-biosystems/refs/heads/main/security/benson-hill-biosystems-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/benson-hill-biosystems-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://confluence.ag/
- group: operate
  title: ''
  type: Support
  url: https://confluence.ag/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://confluence.ag/legal/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://confluence.ag/legal/privacy-policy/
coverage:
  checked: '2026-09-27'
  detail: Documentation is provided as HTML pages without an OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://confluence.ag/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-27'
description: Benson Hill Biosystems, a leader in agricultural genomics and digital breeding, develops advanced seed traits to improve crop yields, nutrition, and sustainability. Leveraging proprietary genetics platforms and data-driven breeding, the company serves global food, feed, and fuel markets, delivering high-protein soybeans, low-oligosaccharide varieties, and other innovative crops. Their mission focuses on better feed, better food, and better fuel through science and technology.
image: https://confluence.ag/wp-content/uploads/2025/08/08262025-Confluence-Turkey-Release-Image-scaled.jpg
layout: provider
modified: '2026-09-27'
name: Benson Hill Biosystems
nav: Providers
network: true
overview: 'Benson Hill Biosystems publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agriculture, Genomics, SeedTechnology, and Food Security.


  Benson Hill Biosystems'' developer surface includes support and 6 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 10.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Benson Hill Biosystems Domain Security
  slug: benson-hill-biosystems-domain-security
  summary_line: TLSv1.3 · DMARC
slug: benson-hill-biosystems
tags:
- Company
- Agriculture
- Genomics
- SeedTechnology
- Food Security
website: https://confluence.ag/
---
