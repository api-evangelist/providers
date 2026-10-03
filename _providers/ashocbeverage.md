---
agent_readiness:
  band: agent-aware
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
    mcp_server: platform
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.7
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: API documented on the Drink Accelerator site, but no owned machine‑readable contract could be verified.
  name: Ashocbeverage API
  slug: ashocbeverage-api
artifact_total: 3
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ashocbeverage/refs/heads/main/llms/ashocbeverage-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ashocbeverage-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ashocbeverage/refs/heads/main/mcp/ashocbeverage-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/ashocbeverage-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ashocbeverage/refs/heads/main/well-known/ashocbeverage-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ashocbeverage-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ashocbeverage/refs/heads/main/hosts/ashocbeverage-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ashocbeverage-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ashocbeverage/refs/heads/main/vendors/ashocbeverage-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ashocbeverage-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.drinkaccelerator.com/blogs/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ashocbeverage/refs/heads/main/security/ashocbeverage-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ashocbeverage-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.drinkaccelerator.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.drinkaccelerator.com/pages/about-us
- group: company
  title: ''
  type: Blog
  url: https://www.drinkaccelerator.com/pages/newsletter
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.drinkaccelerator.com/pages/privacy-policy_
created: '2026-09-26'
description: Ashocbeverage is a modern energy drink brand offering a range of performance‑focused beverages such as SHOC Accelerator, SHOC Frozen Ice, and SHOC Fruit Punch. The brand is marketed through the Drink Accelerator online store, featuring product pages, a blog, and a privacy policy. It targets active consumers seeking natural caffeine blends and is distributed via major retailers.
image: https://www.drinkaccelerator.com/assets/logo.png
layout: provider
mcp_servers:
- description: ''
  name: Ashocbeverage MCP Server
  slug: ashocbeverage-mcp-server
modified: '2026-09-26'
name: Ashocbeverage
nav: Providers
network: true
overview: 'Ashocbeverage publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy Drink, Beverages, Health, and Lifestyle.


  Ashocbeverage''s developer surface includes documentation, engineering blog, and 9 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 10.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 68.3
    operational_transparency: 0.0
  provenance:
    mcp: platform-generated
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ashocbeverage Domain Security
  slug: ashocbeverage-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ashocbeverage
tags:
- Company
- Energy Drink
- Beverages
- Health
- Lifestyle
website: https://www.drinkaccelerator.com
---
