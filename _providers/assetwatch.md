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
api_count: 1
apis:
- description: AssetWatch provides an API for asset condition monitoring and predictive maintenance data.
  name: AssetWatch API
  slug: assetwatch-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/assetwatch/refs/heads/main/llms/assetwatch-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/assetwatch-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/assetwatch/refs/heads/main/hosts/assetwatch-hosts.yml
  title: ''
  type: Hosts
  url: hosts/assetwatch-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/assetwatch/refs/heads/main/vendors/assetwatch-vendors.yml
  title: ''
  type: Vendors
  url: vendors/assetwatch-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.assetwatch.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.assetwatch.com/msa/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.assetwatch.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.assetwatch.com/news
- group: start
  title: ''
  type: GettingStarted
  url: https://www.assetwatch.com/get-started
- group: company
  title: ''
  type: Blog
  url: https://www.assetwatch.com/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/assetwatch/refs/heads/main/security/assetwatch-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/assetwatch-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.assetwatch.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://api.assetwatch.com/mcp
  - status: 403
    url: https://forgeglobal.com/assetwatch_stock/
  reason: no-developer-program
  state: none
created: '2026-09-26'
description: AssetWatch provides advanced asset condition monitoring and predictive maintenance solutions for industrial plants. Their platform combines vibration analysis, oil analysis, AI-driven insights, and human expertise to help organizations reduce unplanned downtime, improve reliability, and optimize maintenance strategies across various industries such as chemicals, food & beverage, metals, mining, and more.
image: https://cdn.prod.website-files.com/63218ae5858431d054be1093/63d2d51d19229c2fc32a7d1b_opengraph-assetwatch.jpg
layout: provider
modified: '2026-09-26'
name: AssetWatch
nav: Providers
network: true
overview: 'AssetWatch publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Asset Management, Predictive Maintenance, Industrial IoT, and Monitoring.


  AssetWatch''s developer surface includes getting-started guide, engineering blog, and 9 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 15.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Assetwatch Domain Security
  slug: assetwatch-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: assetwatch
tags:
- Company
- Asset Management
- Predictive Maintenance
- Industrial IoT
- Monitoring
website: https://www.assetwatch.com/
---
