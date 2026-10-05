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
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: Agentic AI platform API (no public machine‑readable contract discovered)
  name: Auquan API
  slug: auquan-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aoquan/refs/heads/main/vendors/aoquan-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aoquan-vendors.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aoquan/refs/heads/main/llms/aoquan-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aoquan-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aoquan/refs/heads/main/hosts/aoquan-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aoquan-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aoquan/refs/heads/main/security/aoquan-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aoquan-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://equityzen.com/company/aoquan
coverage:
  checked: 2026-09-25
  detail: The provider’s website is a static marketing site with no public API documentation or machine‑readable contract.
  evidence:
  - status: 200
    url: https://www.auquan.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-25'
description: Auquan (formerly Aoquan) provides agentic AI solutions for institutional finance, automating data collection, analysis, and reporting workflows. Their platform enables finance professionals to reduce manual effort, accelerate decision‑making, and focus on strategic insights across credit, sustainability, and investor relations. The company offers a suite of AI‑driven tools, a sandbox environment, and integrations that streamline complex financial processes.
layout: provider
modified: '2026-09-25'
name: Aoquan
nav: Providers
network: true
overview: Aoquan publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Artificial Intelligence, Automation, and Institutional.
random_paper: 7
score:
  band: minimal
  composite: 4.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 60.7
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: venue_as_website
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aoquan Domain Security
  slug: aoquan-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: aoquan
tags:
- Company
- Finance
- Artificial Intelligence
- Automation
- Institutional
website: https://equityzen.com/company/aoquan
---
