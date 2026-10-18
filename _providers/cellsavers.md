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
api_count: 1
apis:
- description: API documentation hosted at api-docs.puls.com, but no machine-readable spec was found.
  name: Cellsavers API
  slug: cellsavers-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cellsavers/refs/heads/main/vendors/cellsavers-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cellsavers-vendors.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cellsavers/refs/heads/main/llms/cellsavers-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cellsavers-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cellsavers/refs/heads/main/hosts/cellsavers-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cellsavers-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://puls.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://puls.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://puls.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://puls.com/press
- group: start
  title: ''
  type: Login
  url: https://puls.com/re/login
- group: company
  title: ''
  type: Blog
  url: https://blog.puls.com
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.puls.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cellsavers/refs/heads/main/security/cellsavers-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cellsavers-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://puls.com
coverage:
  checked: '2026-10-07'
  detail: API docs at https://api-docs.puls.com/ provide no OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract.
  evidence:
  - status: 200
    url: https://api-docs.puls.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-07'
description: Cellsavers provides home care and repair services, offering TV mounting, appliance repair, handyman services, iPhone repair, smart home installation, garage door repair, and plumbing. The company serves millions of households, emphasizing vetted technicians and a comprehensive service platform.
image: https://d7gh5vrfihrl.cloudfront.net/website/banners/home-page/1200.png
layout: provider
modified: '2026-10-07'
name: Cellsavers
nav: Providers
network: true
overview: 'Cellsavers is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Home Care, Repair, Handyman, and Smart Home.


  Cellsavers'' developer surface includes pricing, engineering blog, documentation, and 9 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 17.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
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
  name: Cellsavers Domain Security
  slug: cellsavers-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: cellsavers
tags:
- Company
- Home Care
- Repair
- Handyman
- Smart Home
- Services
website: https://puls.com
---
