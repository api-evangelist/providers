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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: API for soil carbon measurement and reporting
  name: Chrysalabs API
  slug: chrysalabs-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/chrysalabs/refs/heads/main/llms/chrysalabs-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/chrysalabs-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/chrysalabs/refs/heads/main/well-known/chrysalabs-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/chrysalabs-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/chrysalabs/refs/heads/main/hosts/chrysalabs-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chrysalabs-hosts.yml
- group: start
  title: ''
  type: SignUp
  url: https://www.chrysalabs.com/register-webinar/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.chrysalabs.com/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.chrysalabs.com/pricing_request_carbonlabs/
- group: company
  title: ''
  type: Newsroom
  url: https://www.chrysalabs.com/insightlabs/news/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ChrysaLabs
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chrysalabs/refs/heads/main/security/chrysalabs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chrysalabs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.chrysalabs.com
coverage:
  checked: '2026-10-08'
  detail: OpenAPI spec endpoints on api.chrysalabs.com return 404, indicating no machine‑readable contract.
  evidence:
  - status: 404
    url: https://api.chrysalabs.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-08'
description: Chrysalabs provides reliable soil carbon measurement, verification, and reporting (MRV) solutions for bankable carbon assets. Their platform uses proximal sensing technology to deliver high‑integrity data, helping project developers and financiers turn complex soil carbon projects into market‑ready assets with transparency and scientific rigor.
image: https://www.chrysalabs.com/wp-content/uploads/2023/04/Contact.jpg
layout: provider
modified: '2026-10-08'
name: Chrysalabs
nav: Providers
network: true
overview: 'Chrysalabs is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Soil Carbon, MRV, Climate Tech, and Sustainability.


  Chrysalabs'' developer surface includes signup flow, pricing, and 8 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 14.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 66.1
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Chrysalabs Domain Security
  slug: chrysalabs-domain-security
  summary_line: TLSv1.3 · DMARC
slug: chrysalabs
tags:
- Company
- Soil Carbon
- MRV
- Climate Tech
- Sustainability
website: https://www.chrysalabs.com
---
