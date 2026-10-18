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
- description: Briq provides AI-driven orchestration APIs for construction workflows, referenced in their Guides section.
  name: Briq API
  slug: briq-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/briq/refs/heads/main/llms/briq-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/briq-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/briq/refs/heads/main/hosts/briq-hosts.yml
  title: ''
  type: Hosts
  url: hosts/briq-hosts.yml
- group: auth
  title: ''
  type: Security
  url: https://briq.ai/security
- group: commercial
  title: ''
  type: Pricing
  url: https://briq.ai/home/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://briq.ai/guides/
- group: start
  title: ''
  type: GettingStarted
  url: https://briq.ai/acu/object/vendor-onboarding-w9
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/briq/refs/heads/main/security/briq-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/briq-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://briq.ai
coverage:
  checked: '2026-10-06'
  detail: Guides page loads content via JavaScript, no machine‑readable API spec discovered.
  evidence:
  - status: 200
    url: https://briq.ai/guides/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-06'
description: Briq provides AI-driven orchestration solutions for the construction industry, enabling companies to automate workflows, optimize resource allocation, and integrate data across projects. Their platform leverages machine learning to improve decision‑making and operational efficiency in construction management.
image: https://briq.ai/images/briq-logo-white.png
layout: provider
modified: '2026-10-06'
name: Briq
nav: Providers
network: true
overview: 'Briq is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Construction, Artificial Intelligence, Automation, Platform, and Software-as-a-Service.


  Briq''s developer surface includes pricing, documentation, getting-started guide, and 5 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 12.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 64.3
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Briq Domain Security
  slug: briq-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: briq
tags:
- Construction
- Artificial Intelligence
- Automation
- Platform
- Software-as-a-Service
website: https://briq.ai
---
