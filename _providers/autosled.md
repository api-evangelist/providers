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
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/autosled/refs/heads/main/llms/autosled-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/autosled-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/autosled/refs/heads/main/hosts/autosled-hosts.yml
  title: ''
  type: Hosts
  url: hosts/autosled-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://autosled.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://autosled.com/category/autosled-blog/news/
- group: company
  title: ''
  type: Blog
  url: https://autosled.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/autosled
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/autosled/refs/heads/main/security/autosled-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/autosled-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://autosled.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-developer-program
  state: none
created: '2026-09-26'
description: Autosled is a marketplace for vehicle shippers and transporters, providing a modern digital platform to manage shipments, payments, and logistics. It connects carriers with customers, offering tools for tracking, quoting, and optimizing transport processes across the United States.
image: https://autosled.com/wp-content/uploads/2021/11/cropped-Untitled-design-83-1-e1603983203766-1.png
layout: provider
modified: '2026-09-26'
name: Autosled
nav: Providers
network: true
overview: 'Autosled is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Logistics, Transportation, Marketplace, and Shipping.


  Autosled''s developer surface includes engineering blog and 7 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 8.1
  coverage:
    artifact_dirs: 7
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
    discoverability: 57.1
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Autosled Domain Security
  slug: autosled-domain-security
  summary_line: TLSv1.3 · DMARC
slug: autosled
tags:
- Company
- Logistics
- Transportation
- Marketplace
- Shipping
website: https://autosled.com/
---
