---
agent_readiness:
  band: agent-aware
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.7
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Domyn API documentation is hosted at docs.igenius.ai, but the site renders only a JavaScript shell and does not expose a machine‑readable OpenAPI spec.
  name: Domyn API
  slug: domyn-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/domyn/llms/domyn-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/domyn-llms.txt
- group: agent
  href: https://artifacts.apis.io/domyn/well-known/domyn-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/domyn-well-known.yml
- group: other
  href: https://artifacts.apis.io/domyn/hosts/domyn-hosts.yml
  title: ''
  type: Hosts
  url: hosts/domyn-hosts.yml
- group: other
  href: https://artifacts.apis.io/domyn/vendors/domyn-vendors.yml
  title: ''
  type: Vendors
  url: vendors/domyn-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.domyn.com/legal/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.domyn.com/news
- group: other
  title: ''
  type: Leadership
  url: https://www.domyn.com/team
- group: company
  title: ''
  type: Blog
  url: https://www.domyn.com/blog
- group: auth
  href: https://artifacts.apis.io/domyn/security/domyn-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/domyn-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.domyn.com/
coverage:
  checked: '2026-10-23'
  detail: Documentation at https://docs.igenius.ai renders only a JavaScript shell, preventing retrieval of a machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://docs.igenius.ai/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-23'
description: Domyn provides a composite AI platform enabling enterprises to design, deploy, and orchestrate AI agents tailored to regulated and mission‑critical use cases. The platform offers centralized management, customizable language models, governance tools, and secure deployment options, targeting industries such as finance, healthcare, and manufacturing. Domyn’s solutions aim to enhance decision‑making, automate complex workflows, and ensure compliance while delivering scalable AI capabilities across the enterprise.
image: https://cdn.prod.website-files.com/682dcb35e7fd7a313cae803a/6838358a5f5a5ed1b8f33aab_og-image.png
layout: provider
modified: '2026-10-23'
name: Domyn
nav: Providers
network: true
overview: 'Domyn is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Enterprise, Platform, Automation, and Regulated Industries.


  Domyn''s developer surface includes engineering blog and 9 more developer resources.'
random_paper: 23
score:
  band: minimal
  composite: 7.8
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
    developer_ergonomics: 2.4
    discoverability: 60.7
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Domyn Domain Security
  slug: domyn-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: domyn
tags:
- Artificial Intelligence
- Enterprise
- Platform
- Automation
- Regulated Industries
website: https://www.domyn.com/
---
