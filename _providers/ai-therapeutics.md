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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-09-21'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://orphai-therapeutics.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AI-Therapeutics
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ai-therapeutics/refs/heads/main/security/ai-therapeutics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ai-therapeutics-domain-security.yml
coverage:
  checked: '2026-09-13'
  detail: AI Therapeutics is a clinical-stage biopharmaceutical company (now Orphai Therapeutics, a Quince Therapeutics subsidiary) whose product is an inhaled rapamycin drug candidate, not software — its only live host, orphai-therapeutics.com, is a one-page WordPress corporate site that 404s every /.well-known/, OpenAPI and llms.txt path, and its GitHub organization has zero public repositories.
  evidence:
  - status: 404
    url: https://orphai-therapeutics.com/.well-known/agent-card.json
  - status: 404
    url: https://orphai-therapeutics.com/openapi.json
  - status: 404
    url: https://orphai-therapeutics.com/llms.txt
  - status: 200
    url: https://api.github.com/users/AI-Therapeutics/repos
  reason: not-a-software-company
  state: none
created: '2026-09-13'
description: 'AI Therapeutics (now Orphai Therapeutics) is a clinical-stage biopharmaceutical company founded in Guilford, Connecticut by Jonathan Rothberg as LAM Therapeutics, renamed AI Therapeutics, and renamed again to OrphAI Therapeutics in September 2023. It built an internal deep-learning platform that synthesized public and proprietary drug and disease data to match existing chemical entities to new indications, and used it to advance a rare-disease and pulmonary pipeline — LAM-001, an inhaled formulation of sirolimus (rapamycin) targeting mTOR-driven pulmonary disease, plus the earlier PIKfyve inhibitor programs LAM-002 and LAM-003. Quince Therapeutics (Nasdaq: QNCX) acquired Orphai in May 2026 and now runs it as a subsidiary. The AI platform is an internal drug-discovery tool, not a product: the company operates no developer program, publishes no API, SDK or machine-readable contract, and its public web presence is a single-page corporate site.'
image: https://orphai-therapeutics.com/wp-content/uploads/2026/07/orphai-logo-new.png
layout: provider
modified: '2026-09-13'
name: AI Therapeutics
nav: Providers
network: true
overview: AI Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Life Sciences, and Drug Discovery.
random_paper: 4
score:
  band: minimal
  composite: 3.7
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 2.6
  previous_composite: 3.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ai Therapeutics Domain Security
  slug: ai-therapeutics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ai-therapeutics
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Life Sciences
- Drug Discovery
- Artificial Intelligence
- Clinical Trials
- Rare Disease
website: https://orphai-therapeutics.com/
---
