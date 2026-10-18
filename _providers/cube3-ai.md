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
  href: https://raw.githubusercontent.com/api-evangelist/cube3-ai/refs/heads/main/llms/cube3-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cube3-ai-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cube3-ai/refs/heads/main/hosts/cube3-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cube3-ai-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cube3.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cube3.ai/privacy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cube3-ai/refs/heads/main/security/cube3-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cube3-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cube3.ai/
coverage:
  checked: '2026-10-11'
  detail: All attempts to fetch OpenAPI specs from https://api.cube3.ai returned HTTP 403, providing no machine‑readable contract.
  evidence:
  - status: 403
    url: https://api.cube3.ai/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-11'
description: Cube3.ai provides an agentic AI platform for financial crime prevention, offering real‑time detection and mitigation of fraud, scams, and cyber threats for large institutions such as banks, fintechs, crypto exchanges, and public sector agencies. Leveraging autonomous AI agents, the service monitors transactions, identifies malicious patterns, and blocks threats before loss occurs, delivering a proactive defense against AI‑powered criminal operations.
image: https://www.cube3.ai/og-image.png
layout: provider
modified: '2026-10-11'
name: Cube3.ai
nav: Providers
network: true
overview: Cube3.ai is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, FinancialCrime, FraudPrevention, and CyberSecurity.
random_paper: 9
score:
  band: minimal
  composite: 9.4
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
    developer_ergonomics: 0.0
    discoverability: 55.4
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cube3 Ai Domain Security
  slug: cube3-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cube3-ai
tags:
- Company
- Artificial Intelligence
- FinancialCrime
- FraudPrevention
- CyberSecurity
website: https://www.cube3.ai/
---
