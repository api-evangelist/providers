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
- description: API for First Bite platform
  name: First Bite API
  slug: first-bite-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/first-bite/refs/heads/main/llms/first-bite-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/first-bite-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/first-bite/refs/heads/main/hosts/first-bite-hosts.yml
  title: ''
  type: Hosts
  url: hosts/first-bite-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/first-bite/refs/heads/main/vendors/first-bite-vendors.yml
  title: ''
  type: Vendors
  url: vendors/first-bite-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/first-bite/refs/heads/main/security/first-bite-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/first-bite-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.firstbite.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.firstbite.io/
- group: docs
  title: ''
  type: Documentation
  url: https://help.firstbite.io/
- group: docs
  title: ''
  type: APIReference
  url: https://help.firstbite.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.firstbite.io/request-a-demo
- group: operate
  title: ''
  type: Support
  url: https://help.firstbite.io/
- group: company
  title: ''
  type: Blog
  url: https://www.firstbite.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.firstbite.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.firstbite.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://app.firstbite.io/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://app.firstbite.io/privacy-policy
coverage:
  detail: Help center pages are rendered via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://help.firstbite.io/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-12'
description: First Bite provides a foodservice sales platform that unifies prospecting, CRM, operator data, contact info, and rebates & rewards. It offers direct operator data and attribution tools for foodservice businesses, enabling them to supercharge sales, manage customer relationships, and access comprehensive data across operators. The platform includes features such as product CRM, operator data, contact management, prospecting tools, and activation resources, catering to B2B foodservice companies seeking integrated sales solutions.
image: https://cdn.prod.website-files.com/6834cdd1f95654c0496ce53f/683dc01f20765a5c603c09bd_Open%20Graph.jpg
layout: provider
modified: '2026-10-12'
name: First Bite
nav: Providers
network: true
overview: 'First Bite is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food Service, SalesPlatform, CRM, and Data.


  First Bite''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 8 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 24.2
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
    developer_ergonomics: 45.2
    discoverability: 64.3
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
  name: First Bite Domain Security
  slug: first-bite-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: first-bite
tags:
- Company
- Food Service
- SalesPlatform
- CRM
- Data
website: https://www.firstbite.io/
---
