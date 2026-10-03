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
api_count: 1
apis:
- description: API for Argámedtech medical technology platform
  name: Argámedtech API
  slug: arg-medtech-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/argamedtech/refs/heads/main/llms/argamedtech-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/argamedtech-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/argamedtech/refs/heads/main/hosts/argamedtech-hosts.yml
  title: ''
  type: Hosts
  url: hosts/argamedtech-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://argamedtech.com/news
- group: operate
  title: ''
  type: ChangeLog
  url: https://argamedtech.com/whats-new
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/argamedtech/refs/heads/main/security/argamedtech-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/argamedtech-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://argamedtech.com
- group: docs
  title: ''
  type: Documentation
  url: https://argamedtech.com/technology
- group: operate
  title: ''
  type: Support
  url: https://argamedtech.com/contact
- group: company
  title: ''
  type: About
  url: https://argamedtech.com/team
coverage:
  checked: 2026-09-26
  detail: Technology page renders HTML and no machine‑readable OpenAPI spec was found despite probing common spec URLs.
  evidence:
  - status: 200
    url: https://argamedtech.com/technology
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-26'
description: Argámedtech is a medical technology company developing next‑generation non‑thermal cardiac ablation systems using Pulsed Field Ablation (PFA) technology. The firm focuses on improving safety and efficacy of atrial fibrillation treatments, offering a versatile catheter‑based solution. Their platform integrates advanced energy delivery and proprietary software to enhance procedural outcomes for physicians and patients worldwide.
image: https://img1.wsimg.com/isteam/ip/786408e0-1890-4c49-9bbf-d7a2008aa099/blob-9bae762.png
layout: provider
modified: '2026-09-26'
name: Argámedtech
nav: Providers
network: true
overview: 'Argámedtech publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, MedTech, Cardiology, Healthcare, and Innovation.


  Argámedtech''s developer surface includes changelog, documentation, support, and 6 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 10.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 66.1
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Argamedtech Domain Security
  slug: argamedtech-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: argamedtech
tags:
- Company
- MedTech
- Cardiology
- Healthcare
- Innovation
website: https://argamedtech.com
---
