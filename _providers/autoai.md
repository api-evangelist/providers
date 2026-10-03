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
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/autoai/refs/heads/main/well-known/autoai-clarity-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/autoai-clarity-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/autoai/refs/heads/main/well-known/autoai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/autoai-well-known.yml
- group: auth
  title: ''
  type: Security
  url: https://clarity.com/vdp
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/autoai/refs/heads/main/llms/autoai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/autoai-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/autoai/refs/heads/main/hosts/autoai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/autoai-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/autoai/refs/heads/main/security/autoai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/autoai-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/autoai/refs/heads/main/security/autoai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/autoai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.autoai.com/
coverage:
  checked: 2026-09-26
  detail: The provider's site https://autoai.inc returns a JavaScript shell with no machine‑readable documentation.
  evidence:
  - status: 200
    url: https://autoai.inc
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-26'
description: Autoai is an emerging technology company focused on delivering AI-driven solutions for enterprise automation, data analytics, and intelligent decision-making. Founded in 2022, Autoai provides a suite of APIs that enable developers to integrate machine learning models, workflow automation, and predictive analytics into their applications, aiming to accelerate digital transformation across industries.
image: https://www.autoai.inc/og-share.png
layout: provider
modified: '2026-09-26'
name: Autoai
nav: Providers
network: true
overview: Autoai is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Automation, Data Analytics, Enterprise, and Machine Learning.
random_paper: 5
score:
  band: minimal
  composite: 6.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 55.4
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Autoai Domain Security
  slug: autoai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Autoai Vulnerability Disclosure
  slug: autoai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: autoai
tags:
- Artificial Intelligence
- Automation
- Data Analytics
- Enterprise
- Machine Learning
- Company
website: https://www.autoai.com/
---
