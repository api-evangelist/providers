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
  scored_at: '2026-09-21'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aitrics/refs/heads/main/security/aitrics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aitrics-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aitrics/refs/heads/main/llms/aitrics-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aitrics-llms.txt
- group: company
  title: ''
  type: Website
  url: https://aitrics.com
coverage:
  checked: 2026-09-21
  detail: The provider's website is a static Korean site with no public API documentation or machine‑readable spec.
  evidence:
  - status: 200
    url: https://aitrics.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-21'
description: Aitrics is a Korean AI-driven healthcare technology company that provides innovative workflow solutions for medical staff. Their platform analyzes real‑time EMR data with artificial intelligence to predict patient condition deterioration, offering products such as AITRICS‑VC, Business Service, and Virtual Doctor. The company aims to save lives and empower future healthcare through intelligent, all‑in‑one solutions, with certifications in Malaysia and Indonesia.
layout: provider
modified: '2026-09-21'
name: Aitrics
nav: Providers
network: true
overview: Aitrics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Healthcare, South Korea, and AI-Healthcare.
random_paper: 3
score:
  band: minimal
  composite: 2.9
  coverage:
    artifact_dirs: 4
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
    discoverability: 46.3
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aitrics Domain Security
  slug: aitrics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aitrics
tags:
- Company
- Artificial Intelligence
- Healthcare
- South Korea
- AI-Healthcare
website: https://aitrics.com
---
