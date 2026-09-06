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
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/researchgate-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.researchgate.net
created: '2026-07-17'
description: ResearchGate is a professional network and social platform for scientists and researchers, founded in 2008 in Berlin, Germany. Members use it to share and discover research publications, connect and collaborate with colleagues, ask and answer questions, and track the reach and citations of their work. The platform hosts tens of millions of researcher profiles and a large corpus of full-text papers, and is operated by ResearchGate GmbH. It exposes no publicly documented developer API surface; this profile was surfaced via the dragoneer portfolio and enriched by the API Evangelist pipeline.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/researchgate.png
layout: provider
modified: '2026-07-20'
name: ResearchGate
nav: Providers
network: true
overview: ResearchGate is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer Internet, Research, Academic, and Social Network.
random_paper: 2
score:
  band: minimal
  composite: 2.5
  coverage:
    artifact_dirs: 1
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 2.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 11.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: domain-security
  name: Researchgate Domain Security
  slug: researchgate-domain-security
  summary_line: TLSv1.3 · DMARC
slug: researchgate
tags:
- Company
- Consumer Internet
- Research
- Academic
- Social Network
- Publishing
- Science
website: https://www.researchgate.net
---
