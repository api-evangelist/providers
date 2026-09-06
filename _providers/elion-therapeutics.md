---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/elion-therapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://eliontx.com/
- group: other
  title: ''
  type: Company
  url: https://forgeglobal.com/elion-therapeutics_stock/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/elion-therapeutics-llms.txt
coverage:
  checked: '2026-08-12'
  detail: Elion Therapeutics is a clinical-stage antifungal drug developer whose only web property is a WordPress marketing site — the origin answers HTTP 404 to every /.well-known/ path and to /llms.txt, and there is no developer portal, GitHub organization, or API of any kind to profile.
  evidence:
  - status: 404
    url: https://eliontx.com/.well-known/api-catalog
  - status: 404
    url: https://eliontx.com/llms.txt
  - status: 200
    url: https://eliontx.com/robots.txt
  - status: 404
    url: https://github.com/eliontx
  reason: not-a-software-company
  state: none
created: '2026-08-12'
description: 'Elion Therapeutics is a privately held, clinical-stage biotechnology company developing treatments for life-threatening invasive fungal infections (IFIs). Formerly known as Sfunga Therapeutics, the company was founded on the belief that mechanistic insight into natural products enables targeted optimization of them. Its lead candidate, SF001, is a next-generation polyene antifungal — a rationally designed analog of amphotericin B intended to retain broad fungicidal activity while mitigating the systemic toxicity that limits the parent molecule. SF001 received FDA Qualified Infectious Disease Product (QIDP) and Fast Track designations in 2023 and has advanced from a first-in-human single-ascending-dose study into multiple-ascending-dose evaluation. Elion closed an $81 million Series B in June 2024 led by Deerfield Management and the AMR Action Fund, with participation from Illinois Ventures. Elion is a therapeutics developer, not a software vendor: it publishes no developer
  program, public API, or machine-readable API contract, and this profile records that absence rather than any API surface.'
layout: provider
modified: '2026-08-12'
name: Elion Therapeutics
nav: Providers
network: true
overview: Elion Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Therapeutics, and Life Sciences.
random_paper: 8
score:
  band: minimal
  composite: 3.7
  coverage:
    artifact_dirs: 3
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.7
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 3.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: domain-security
  name: Elion Therapeutics Domain Security
  slug: elion-therapeutics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: elion-therapeutics
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Therapeutics
- Life Sciences
- Anti-Infectives
- Drug Development
- Clinical Stage
- Healthcare
website: https://eliontx.com/
---
