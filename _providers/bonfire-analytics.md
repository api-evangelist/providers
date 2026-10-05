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
  href: https://raw.githubusercontent.com/api-evangelist/bonfire-analytics/refs/heads/main/llms/bonfire-analytics-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bonfire-analytics-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bonfire-analytics/refs/heads/main/hosts/bonfire-analytics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bonfire-analytics-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bonfire-analytics/refs/heads/main/vendors/bonfire-analytics-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bonfire-analytics-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bonfireanalytics.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bonfireanalytics.com/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.bonfireanalytics.com/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bonfire-analytics/refs/heads/main/security/bonfire-analytics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bonfire-analytics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bonfireanalytics.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-developer-program
  state: none
created: '2026-10-02'
description: Bonfire Analytics provides sales intelligence solutions for the healthcare sector, helping commercial leaders and business development teams identify target markets, optimize referral pathways, and evaluate market share. Their platform offers deep provider and organization insights, market segmentation, and referral intelligence to drive growth and improve outreach strategies across the health ecosystem.
image: https://cdn.prod.website-files.com/68afcc1247d4ac2e7cc42fb7/68c298a3cb47ae57b0977688_Open%20Graph%20%5BHome%20Page%5D.webp
layout: provider
modified: '2026-10-02'
name: Bonfire Analytics
nav: Providers
network: true
overview: 'Bonfire Analytics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Sales Intelligence, B2B, Data Analytics, and Company.


  Bonfire Analytics'' developer surface includes engineering blog and 7 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 10.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 55.4
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bonfire Analytics Domain Security
  slug: bonfire-analytics-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bonfire-analytics
tags:
- Healthcare
- Sales Intelligence
- B2B
- Data Analytics
- Company
website: https://www.bonfireanalytics.com/
---
