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
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cerebriai/refs/heads/main/llms/cerebriai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cerebriai-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cerebriai/refs/heads/main/hosts/cerebriai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cerebriai-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cerebriai/refs/heads/main/vendors/cerebriai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cerebriai-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://www.cerebriai.com/team/mike-daly
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cerebriai/refs/heads/main/security/cerebriai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cerebriai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cerebriai.com
- group: start
  title: ''
  type: GettingStarted
  url: https://www.cerebriai.com/how-ai-works
- group: operate
  title: ''
  type: Support
  url: https://www.cerebriai.com/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cerebriai.com/privacy-policy
coverage:
  checked: '2026-10-08'
  detail: The main website renders content via JavaScript, preventing automated extraction of machine‑readable API specifications.
  evidence:
  - status: 200
    url: https://www.cerebriai.com/how-ai-works
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-07'
description: Cerebriai provides a trusted digital workforce powered by AI for travel & expense (T&E) management and procurement. Their platform offers AI agents that automate expense reporting, hotel sourcing, and custom AI solutions for enterprises, delivering frictionless T&E processes, data-driven decision making, and scalable digital employees. The company focuses on integrating AI into business workflows to improve efficiency and reduce manual effort across procurement and travel operations.
layout: provider
modified: '2026-10-07'
name: Cerebriai
nav: Providers
network: true
overview: 'Cerebriai is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Travel, Expenses, and Procurement.


  Cerebriai''s developer surface includes getting-started guide, support, and 7 more developer resources.'
random_paper: 10
score:
  band: minimal
  composite: 9.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 53.6
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cerebriai Domain Security
  slug: cerebriai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: cerebriai
tags:
- Company
- Artificial Intelligence
- Travel
- Expenses
- Procurement
- Automation
website: https://www.cerebriai.com
---
