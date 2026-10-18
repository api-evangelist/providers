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
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/crmbonus/refs/heads/main/hosts/crmbonus-hosts.yml
  title: ''
  type: Hosts
  url: hosts/crmbonus-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/crmbonus/refs/heads/main/vendors/crmbonus-vendors.yml
  title: ''
  type: Vendors
  url: vendors/crmbonus-vendors.yml
- group: company
  title: ''
  type: Blog
  url: https://www.crmbonus.com.br/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/crmbonus/refs/heads/main/security/crmbonus-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crmbonus-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.crmbonus.com.br
coverage:
  checked: '2026-10-11'
  detail: The website provides only static HTML with no machine‑readable API specification.
  evidence:
  - status: 200
    url: https://www.crmbonus.com.br
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-11'
description: Crmbônus is a Brazilian SaaS company offering a suite of tools for retail businesses to attract, convert, and retain customers through loyalty programs, cashback, conversational commerce, and retail media solutions. Their platform integrates with WhatsApp, e‑commerce, and ERP systems, providing analytics, campaigns, and member management to boost sales and customer engagement across multiple channels.
image: https://cdn.prod.website-files.com/646b6f3bf6907682fc10812f/681ba9a856b8e9d70c5e8948_WhatsApp%20Image%202025-05-07%20at%2015.40.53.webp
layout: provider
modified: '2026-10-11'
name: Crmbônus
nav: Providers
network: true
overview: 'Crmbônus is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Software-as-a-Service, Retail, Loyalty, and Marketing.


  Crmbônus'' developer surface includes engineering blog and 4 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 3.9
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Crmbonus Domain Security
  slug: crmbonus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: crmbonus
tags:
- Company
- Software-as-a-Service
- Retail
- Loyalty
- Marketing
website: https://www.crmbonus.com.br
---
