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
- description: Real-time insurance data and predictive AI via the Fenris MCP platform. Provides prefill, scoring, and data enrichment APIs.
  name: Fenris MCP API
  slug: fenris-mcp-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/fenrisd/refs/heads/main/llms/fenrisd-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fenrisd-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/fenrisd/refs/heads/main/hosts/fenrisd-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fenrisd-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/fenrisd/refs/heads/main/vendors/fenrisd-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fenrisd-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fenrisd.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fenrisd.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://fenrisd.com/category/news/
- group: company
  title: ''
  type: Blog
  url: https://fenrisd.com/category/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.fenrisd.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fenrisd/refs/heads/main/security/fenrisd-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fenrisd-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fenrisd.com/
coverage:
  checked: '2026-10-16'
  detail: Documentation is publicly available at the developer portal but no machine‑readable OpenAPI or other contract was found.
  evidence:
  - status: 200
    url: https://dev.fenrisd.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-16'
description: Fenris provides real-time insurance data and predictive AI solutions that power quoting, risk assessment, and personalized customer experiences. Their MCP platform offers prefill, predictive scoring, and data enrichment across auto, property, and commercial insurance, serving millions of transactions annually. The service integrates via RESTful APIs, delivering sub‑second response times, SOC 2 compliance, and enterprise‑grade security.
image: https://fenrisd.com/wp-content/uploads/2026/08/Embed_Fenris_Logo.png
layout: provider
modified: '2026-10-16'
name: Fenris MCP Server
nav: Providers
network: true
overview: 'Fenris MCP Server is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurance, Data, and Artificial Intelligence.


  Fenris MCP Server''s developer surface includes engineering blog, documentation, and 8 more developer resources.'
random_paper: 21
score:
  band: emerging
  composite: 11.5
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
    developer_ergonomics: 11.9
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 11.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Fenrisd Domain Security
  slug: fenrisd-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fenrisd
tags:
- Company
- Insurance
- Data
- Artificial Intelligence
website: https://fenrisd.com/
---
