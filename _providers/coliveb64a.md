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
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/coliveb64a/refs/heads/main/llms/coliveb64a-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/coliveb64a-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/coliveb64a/refs/heads/main/hosts/coliveb64a-hosts.yml
  title: ''
  type: Hosts
  url: hosts/coliveb64a-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.colive.com/terms-and-conditions
- group: auth
  title: ''
  type: Security
  url: https://www.colive.com/blog/category/colive-6s/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.colive.com/privacypolicy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.colive.com/gurukool-pg-for-students/docs/PriceSheet.pdf
- group: start
  title: ''
  type: Login
  url: https://www.colive.com/login
- group: company
  title: ''
  type: Blog
  url: https://www.colive.com/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/coliveb64a/refs/heads/main/security/coliveb64a-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coliveb64a-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.colive.com
coverage:
  checked: '2026-10-09'
  detail: No API documentation or machine‑readable contract was found on any owned host.
  evidence:
  - status: 404
    url: https://api.colive.com/openapi.json
  - status: 302
    url: https://www.colive.com/openapi.json
  reason: not-a-software-company
  state: none
created: '2026-10-09'
description: 'Coliveb64a is a proptech company operating a co‑living platform in India. It provides smart, furnished, managed flexible homes for professionals and students, offering a property‑management suite, AI‑enabled rental engine, and community services. The company claims over 1 million users, 400 000 units, and aims to reshape urban living with its 6S principles: Style, Safety, Smart, Service, Savings, and Social.'
image: https://www.colive.com/assets/images/icons/favicon.png
layout: provider
modified: '2026-10-09'
name: Coliveb64a
nav: Providers
network: true
overview: 'Coliveb64a is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include PropTech, CoLiving, Real Estate, India, and Platform.


  Coliveb64a''s developer surface includes pricing, engineering blog, and 8 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 16.1
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 55.4
    operational_transparency: 10.5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Coliveb64A Domain Security
  slug: coliveb64a-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: coliveb64a
tags:
- PropTech
- CoLiving
- Real Estate
- India
- Platform
website: https://www.colive.com
---
