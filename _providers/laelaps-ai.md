---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/laelaps-ai/refs/heads/main/security/laelaps-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/laelaps-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://laelaps.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://laelaps.ai/legal.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://laelaps.ai/privacy.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LaelapsAI
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/laelaps-ai/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/laelaps-ai/refs/heads/main/llms/laelaps-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/laelaps-ai-llms.txt
created: '2026-07-17'
description: Laelaps AI builds field intelligence for critical assets. Its system, LEA, combines autonomous embodied agents (AI-powered robots for site perimeter coverage), video monitoring agents that work on existing camera infrastructure, and fixed and mobile sensing systems under a control center layer that fuses their data into actionable intelligence for human operators; the company says one operator can then protect and operate multiple sites 24/7. Target sites include military bases, power grids, data centers, factories and hospitals, and the control layer supports encrypted, air-gapped on-premises hosting. Founded in 2025 by Dr. Sophia Belser (CEO), Dr. Mania Stamatopoulou (CRO) and Rokas Bendikas (CTO), Laelaps AI is based in Switzerland and operates across Europe; its site lists Speedinvest, Expeditions Fund, Florent Venture Partners, Fund F, ESA BIC and NVIDIA Inception as backers. It publishes a corporate website and an llms.txt but no public developer surface - no documentation,
  API reference, SDKs or machine-readable API artifacts.
image: https://laelaps.ai/favicon.svg
layout: provider
modified: '2026-10-06'
name: Laelaps AI
nav: Providers
network: true
overview: Laelaps AI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Robotics, Autonomous Systems, and Security.
random_paper: 17
score:
  band: minimal
  composite: 9.7
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 55.4
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 9.7
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/laelaps-ai/refs/heads/main/screenshots/laelaps-ai-2026-07-25T224425.png
security:
- kind: domain-security
  name: Laelaps Ai Domain Security
  slug: laelaps-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: laelaps-ai
tags:
- Company
- Artificial Intelligence
- Robotics
- Autonomous Systems
- Security
- Surveillance
- Computer Vision
- Defense
- Physical Security
website: https://laelaps.ai/
---
