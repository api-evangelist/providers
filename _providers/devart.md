---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Developer API for Devart services as described in the documentation.
  name: Devart API
  slug: devart-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/devart/llms/devart-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/devart-llms.txt
- group: agent
  href: https://artifacts.apis.io/devart/well-known/devart-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/devart-well-known.yml
- group: other
  href: https://artifacts.apis.io/devart/hosts/devart-hosts.yml
  title: ''
  type: Hosts
  url: hosts/devart-hosts.yml
- group: other
  href: https://artifacts.apis.io/devart/vendors/devart-vendors.yml
  title: ''
  type: Vendors
  url: vendors/devart-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.devart.com/using-website/terms-of-use.html
- group: operate
  title: ''
  type: Support
  url: https://support.devart.com/portal/en/community
- group: operate
  title: ''
  type: StatusPage
  url: https://status.devart.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.devart.com/using-website/privacy-policy.html
- group: company
  title: ''
  type: Blog
  url: https://blog.devart.com/
- group: auth
  href: https://artifacts.apis.io/devart/security/devart-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/devart-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.devart.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.devart.com/
coverage:
  checked: '2026-10-20'
  detail: Docs site returns a JavaScript shell, preventing machine‑readable extraction of an OpenAPI spec.
  evidence:
  - status: 200
    url: https://devart.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-20'
description: Devart provides a comprehensive suite of database management software and developer tools, including data connectivity solutions, IDE extensions, and productivity utilities. Their products span SQL Server, MySQL, Oracle, PostgreSQL, and cloud services, helping enterprises streamline complex data tasks, improve workflow efficiency, and ensure reliable data integration across diverse environments.
image: https://cdn0.devart.com/images/og/devart-1200-630.png
layout: provider
modified: '2026-10-20'
name: Devart
nav: Providers
network: true
overview: 'Devart is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Database, Developer Tools, Data Connectivity, and Software.


  Devart''s developer surface includes support, engineering blog, documentation, and 9 more developer resources.'
random_paper: 22
score:
  band: emerging
  composite: 16.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 57.1
    operational_transparency: 15.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Devart Domain Security
  slug: devart-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: devart
tags:
- Company
- Database
- Developer Tools
- Data Connectivity
- Software
website: https://www.devart.com/
---
