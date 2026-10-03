---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 4.5
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/asleep/refs/heads/main/llms/asleep-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/asleep-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/asleep/refs/heads/main/well-known/asleep-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/asleep-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/asleep/refs/heads/main/hosts/asleep-hosts.yml
  title: ''
  type: Hosts
  url: hosts/asleep-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/asleep/refs/heads/main/vendors/asleep-vendors.yml
  title: ''
  type: Vendors
  url: vendors/asleep-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://asleepcompany.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://asleepcompany.com/policies/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://asleepcompany.com/blogs/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/asleep/refs/heads/main/security/asleep-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/asleep-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://asleepcompany.com
created: '2026-09-26'
description: Asleep is a company identified in the API Evangelist harvest backlog. It appears to be a consumer sleep‑related brand offering products such as eyemasks and pillows via an e‑commerce site. No public API documentation or developer portal could be located despite searching the company’s website and related domains. The profile therefore reflects a lack of discoverable API resources.
layout: provider
modified: '2026-09-26'
name: Asleep
nav: Providers
network: true
overview: Asleep is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sleep, E-Commerce, Consumer Goods, and Retail.
random_paper: 18
score:
  band: minimal
  composite: 9.3
  coverage:
    artifact_dirs: 6
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
    discoverability: 53.6
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
  name: Asleep Domain Security
  slug: asleep-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: asleep
tags:
- Company
- Sleep
- E-Commerce
- Consumer Goods
- Retail
website: https://asleepcompany.com
---
