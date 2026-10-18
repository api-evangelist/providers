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
artifact_total: 1
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dreams-technology/refs/heads/main/security/dreams-technology-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dreams-technology-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/dreams-technology/refs/heads/main/llms/dreams-technology-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dreams-technology-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/dreams-technology/refs/heads/main/hosts/dreams-technology-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dreams-technology-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/dreams-technology/refs/heads/main/vendors/dreams-technology-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dreams-technology-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dreamstechnologies.com/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://dreamstechnologies.com/blog/
- group: company
  title: ''
  type: Website
  url: https://dreamstechnologies.com/
coverage:
  checked: '2026-10-15'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract discovered on the provider’s site.
  evidence:
  - status: 200
    url: https://dreamstechnologies.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-15'
description: Dreams Technologies is a custom software development company operating in the UK and India, offering AI development, mobile app, SaaS platform, cloud & DevOps, digital transformation, and MVP services. They serve enterprise and startup clients across multiple regions, with a portfolio of products such as SmartHR, Doccure, Kanakku, TruelySell, DreamsPOS, and DreamsSchool. The company emphasizes end‑to‑end engineering, product development, and modernization for businesses.
image: https://dreamstechnologies.com/wp-content/uploads/2026/07/og-default.png
layout: provider
modified: '2026-10-15'
name: Dreams Technology
nav: Providers
network: true
overview: 'Dreams Technology is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Software, Artificial Intelligence, Cloud, Development, and Services.


  Dreams Technology''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 7.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 55.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dreams Technology Domain Security
  slug: dreams-technology-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dreams-technology
tags:
- Software
- Artificial Intelligence
- Cloud
- Development
- Services
website: https://dreamstechnologies.com/
---
