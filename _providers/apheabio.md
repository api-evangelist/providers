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
  href: https://raw.githubusercontent.com/api-evangelist/apheabio/refs/heads/main/hosts/apheabio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apheabio-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/apheabio/refs/heads/main/vendors/apheabio-vendors.yml
  title: ''
  type: Vendors
  url: vendors/apheabio-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.aphea.bio/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apheabio/refs/heads/main/security/apheabio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apheabio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aphea.bio
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aphea.bio/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aphea.bio/terms-and-conditions
- group: company
  title: ''
  type: AboutUs
  url: https://www.aphea.bio/company/about-us
- group: other
  title: ''
  type: Products
  url: https://www.aphea.bio/products
- group: other
  title: ''
  type: Technology
  url: https://www.aphea.bio/technology
- group: company
  title: ''
  type: Careers
  url: https://www.aphea.bio/company/careers
- group: other
  title: ''
  type: Sustainability
  url: https://www.aphea.bio/company/sustainability
coverage:
  checked: 2026-09-25
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract found at api.aphea.bio.
  evidence:
  - status: no-response
    url: https://api.aphea.bio/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-25'
description: Apheabio (Aphea.Bio) develops innovative biocontrol and biostimulant products for sustainable agriculture. Leveraging its APEXbio™ R&D platform, the company creates microbial‑based solutions that integrate with conventional and organic crop protection, aiming to improve yields, resilience, and environmental outcomes across the agricultural sector.
layout: provider
modified: '2026-09-25'
name: Apheabio
nav: Providers
network: true
overview: Apheabio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agriculture, Biotechnology, Sustainability, and Biostimulants.
random_paper: 11
score:
  band: minimal
  composite: 8.6
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.4
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Apheabio Domain Security
  slug: apheabio-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: apheabio
tags:
- Company
- Agriculture
- Biotechnology
- Sustainability
- Biostimulants
website: https://www.aphea.bio
---
