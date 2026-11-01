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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/thesparkle-ai/hosts/thesparkle-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/thesparkle-ai-hosts.yml
- group: auth
  href: https://artifacts.apis.io/thesparkle-ai/security/thesparkle-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/thesparkle-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://thesparkle.ai
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://thesparkle.ai
  reason: no-developer-program
  state: none
created: '2026-10-25'
description: TAAI Labs, Inc, operating under the brand Sparkle, provides an AI‑first Secure Software Development Lifecycle (SDLC) platform that integrates security policies, threat modeling, and code analysis to prevent vulnerabilities from design through deployment. The solution offers real‑time risk mitigation, automated policy enforcement, and a living security brain that connects architecture, cloud context, and code repositories, helping organizations build secure AI‑driven products faster.
layout: provider
modified: '2026-10-25'
name: TAAI Labs, Inc
nav: Providers
network: true
overview: TAAI Labs, Inc is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Security, SDLC, and Platform.
random_paper: 2
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
    mcp: derived
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
  name: Thesparkle Ai Domain Security
  slug: thesparkle-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: thesparkle-ai
tags:
- Company
- AI
- Security
- SDLC
- Platform
website: https://thesparkle.ai
---
