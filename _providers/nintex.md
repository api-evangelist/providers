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
- description: Developer portal for Nintex API Design Management Platform
  name: Nintex API
  slug: nintex-api
artifact_total: 2
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/nintex/refs/heads/main/changelog/nintex-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/nintex-changelog.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/nintex/refs/heads/main/llms/nintex-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/nintex-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/nintex/refs/heads/main/hosts/nintex-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nintex-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/nintex/refs/heads/main/vendors/nintex-vendors.yml
  title: ''
  type: Vendors
  url: vendors/nintex-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://community.nintex.com/site/terms
- group: operate
  title: ''
  type: Support
  url: https://help.nintex.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.nintex.com/
- group: auth
  title: ''
  type: Security
  url: https://www.nintex.com/security/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.nintex.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.nintex.com/platforms/whats-new/
- group: company
  title: ''
  type: Blog
  url: https://www.nintex.com/Blog
- group: start
  title: ''
  type: GettingStarted
  url: https://www.nintex.com/blog/getting-started-nintex-ce-platform/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.nintex.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/nintex/refs/heads/main/security/nintex-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nintex-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nintex.com
coverage:
  checked: '2026-10-13'
  detail: Developer portal renders via JavaScript and provides no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://developer.nintex.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-13'
description: Nintex provides a low-code workflow automation platform enabling businesses to design, execute, and optimize processes across cloud, on-premises, and major SaaS ecosystems. Its solutions include workflow automation, document generation, e‑signatures, and robotic process automation, helping organizations accelerate digital transformation.
image: https://www.nintex.com/wp-content/uploads/2024/11/HP-Primary-Hero-01-1.jpg
layout: provider
modified: '2026-10-13'
name: Nintex
nav: Providers
network: true
overview: 'Nintex is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Automation, Low-code, Workflows, and Document Generation.


  Nintex''s developer surface includes changelog, support, engineering blog, getting-started guide, documentation, and 10 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 20.8
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
    developer_ergonomics: 38.1
    discoverability: 64.3
    operational_transparency: 42.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Nintex Domain Security
  slug: nintex-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nintex
tags:
- Company
- Automation
- Low-code
- Workflows
- Document Generation
website: https://www.nintex.com
---
