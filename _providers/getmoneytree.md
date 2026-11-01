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
  href: https://artifacts.apis.io/getmoneytree/llms/getmoneytree-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/getmoneytree-llms.txt
- group: auth
  href: https://artifacts.apis.io/getmoneytree/well-known/getmoneytree-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/getmoneytree-help-security.txt
- group: agent
  href: https://artifacts.apis.io/getmoneytree/well-known/getmoneytree-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/getmoneytree-well-known.yml
- group: other
  href: https://artifacts.apis.io/getmoneytree/hosts/getmoneytree-hosts.yml
  title: ''
  type: Hosts
  url: hosts/getmoneytree-hosts.yml
- group: other
  href: https://artifacts.apis.io/getmoneytree/vendors/getmoneytree-vendors.yml
  title: ''
  type: Vendors
  url: vendors/getmoneytree-vendors.yml
- group: build
  href: https://artifacts.apis.io/getmoneytree/packages/getmoneytree-packages.yml
  title: ''
  type: SDKs
  url: packages/getmoneytree-packages.yml
- group: build
  href: https://artifacts.apis.io/getmoneytree/packages/getmoneytree-packages.yml
  title: ''
  type: Packages
  url: packages/getmoneytree-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://help.getmoneytree.com/ja/
- group: auth
  title: ''
  type: Security
  url: https://getmoneytree.com/jp-blogs/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://getmoneytree.com/privacy-first/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://getmoneytree.com/jp/app/plans-and-pricing
- group: company
  title: ''
  type: Newsroom
  url: https://getmoneytree.com/press
- group: other
  title: ''
  type: Leadership
  url: https://getmoneytree.com/moneytree-business-blog-tag-jps/management
- group: company
  title: ''
  type: Blog
  url: https://getmoneytree.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://help.getmoneytree.com/
- group: auth
  href: https://artifacts.apis.io/getmoneytree/security/getmoneytree-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/getmoneytree-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://getmoneytree.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://app.getmoneytree.com/mcp
  - status: 403
    url: https://dashboard.getmoneytree.com/mcp
  - status: 200
    url: https://getmoneytree.com/
  reason: no-developer-program
  state: none
created: '2026-10-20'
description: 'MoneyTree is a company surfaced via the API Evangelist harvest backlog (source: g2-catalog) and added to the network as a stub for full-pipeline profiling.'
image: https://cdn.prod.website-files.com/60794987246a1d5f3d6bfde6/622e970cb6948c01bf0cc74b_202203_WebsiteOGP_MoneytreeCompany%402x.png
layout: provider
modified: '2026-10-20'
name: MoneyTree
nav: Providers
network: true
overview: 'MoneyTree is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  MoneyTree''s developer surface includes support, pricing, engineering blog, documentation, and 13 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 12.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 17.0
    catalog_earned_first_party: 0.0
    catalog_gap: 98.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 33.9
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Getmoneytree Domain Security
  slug: getmoneytree-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: getmoneytree
tags:
- Company
website: https://getmoneytree.com/
---
