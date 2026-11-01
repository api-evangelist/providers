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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/to-increase/llms/to-increase-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/to-increase-llms.txt
- group: other
  href: https://artifacts.apis.io/to-increase/hosts/to-increase-hosts.yml
  title: ''
  type: Hosts
  url: hosts/to-increase-hosts.yml
- group: other
  href: https://artifacts.apis.io/to-increase/vendors/to-increase-vendors.yml
  title: ''
  type: Vendors
  url: vendors/to-increase-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://staedean.com/trust-center
- group: operate
  title: ''
  type: Support
  url: https://support.to-increase.com/ticsm
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://staedean.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://staedean.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://staedean.com/news
- group: company
  title: ''
  type: Blog
  url: https://staedean.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.staedean.com/docs/optional-setup-for-customer-policy
- group: docs
  title: ''
  type: Documentation
  url: https://docs.to-increase.com/
- group: auth
  href: https://artifacts.apis.io/to-increase/security/to-increase-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/to-increase-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://staedean.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://to-increase.com/mcp
  - status: 401
    url: https://support.to-increase.com/api/mcp
  - status: 200
    url: https://to-increase.com/
  reason: no-developer-program
  state: none
created: '2026-10-21'
description: STAEDEAN provides Dynamics 365 ERP solutions tailored for equipment rental, manufacturing, and life sciences sectors. The company offers comprehensive software suites covering equipment rental management, life sciences compliance, manufacturing operations, data management, and extensive resources such as blogs, case studies, and webinars. Their platform includes pricing information, support plans, documentation, and a trust center, reflecting a robust enterprise resource planning ecosystem.
image: https://staedean.com/hubfs/General/Logos/Staedean-logo-320x80.png
layout: provider
modified: '2026-10-21'
name: STAEDEAN
nav: Providers
network: true
overview: 'STAEDEAN is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, ERP, Equipment Rental, Manufacturing, and Life Sciences.


  STAEDEAN''s developer surface includes support, pricing, engineering blog, getting-started guide, documentation, and 8 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 16.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 11.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: To Increase Domain Security
  slug: to-increase-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: to-increase
tags:
- Company
- ERP
- Equipment Rental
- Manufacturing
- Life Sciences
website: https://staedean.com/
---
