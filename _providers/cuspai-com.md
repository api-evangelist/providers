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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/cuspai-com/hosts/cuspai-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cuspai-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/cuspai-com/security/cuspai-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cuspai-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cuspai.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: null
    url: https://www.cuspai.com
  reason: no-developer-program
  state: none
created: '2026-10-22'
description: Cuspai is a technology company focused on providing advanced AI-driven solutions for data analytics and automation. Founded with backing from Northzone, the company aims to empower enterprises with intelligent platforms that streamline workflows, enhance decision-making, and drive operational efficiency across various industries. Their offerings include cloud-based services, APIs, and developer tools designed to integrate seamlessly into existing tech stacks.
layout: provider
modified: '2026-10-22'
name: Cuspai
nav: Providers
network: true
overview: Cuspai is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Data-Analytics, Automation, and Cloud.
random_paper: 1
score:
  band: minimal
  composite: 3.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cuspai Com Domain Security
  slug: cuspai-com-domain-security
  summary_line: DNSSEC · DMARC
slug: cuspai-com
tags:
- Company
- AI
- Data-Analytics
- Automation
- Cloud
website: https://www.cuspai.com
---
