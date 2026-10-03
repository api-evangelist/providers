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
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aras/refs/heads/main/llms/aras-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aras-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aras/refs/heads/main/hosts/aras-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aras-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aras/refs/heads/main/vendors/aras-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aras-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://aras.com/en/trust-center
- group: operate
  title: ''
  type: Support
  url: https://community.aras.com/category/help-center
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aras.com/en/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://aras.com/en/news
- group: start
  title: ''
  type: GettingStarted
  url: https://community.aras.com/category/engage/discussions/getting-started
- group: company
  title: ''
  type: Blog
  url: https://aras.com/en/blog
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aras.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aras/refs/heads/main/security/aras-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aras-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aras.com
coverage:
  checked: 2026-09-25
  detail: Documentation pages exist but no machine‑readable OpenAPI/AsyncAPI/GraphQL spec was found.
  evidence:
  - status: 200
    url: https://docs.aras.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-25'
description: Aras provides open and adaptable Product Lifecycle Management (PLM) and digital thread solutions. Their platform supports low‑code development, AI‑ready digital thread, and extensive integration capabilities for MCAD, ECAD, ERP, and more, serving industries such as aerospace, automotive, and medical devices. Aras Innovator is offered as a SaaS platform with subscription and upgrade options, and the company is recognized as a leader in the Gartner Magic Quadrant for PLM software.
layout: provider
modified: '2026-09-25'
name: Aras
nav: Providers
network: true
overview: 'Aras is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include PLM, Digital Thread, Low-Code Development, PLM Software, and Cloud Platform.


  Aras'' developer surface includes support, getting-started guide, engineering blog, documentation, and 8 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 14.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 18.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aras Domain Security
  slug: aras-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: aras
tags:
- PLM
- Digital Thread
- Low-Code Development
- PLM Software
- Cloud Platform
- AI-Ready
- Industry Solutions
website: https://aras.com
---
