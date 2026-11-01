---
agent_readiness:
  band: agent-aware
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/tasq/llms/tasq-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tasq-llms.txt
- group: other
  href: https://artifacts.apis.io/tasq/hosts/tasq-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tasq-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tasq.ai/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tasq.ai/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://www.tasq.ai/blog/
- group: auth
  href: https://artifacts.apis.io/tasq/security/tasq-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tasq-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tasq.ai/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://console.tasq.ai/mcp
  - status: 200
    url: https://tasq.ai/
  reason: no-developer-program
  state: none
created: '2026-10-21'
description: Tasq.ai provides a data processing and management layer for AI that offers annotation, evaluation, and validation services across text, video, audio, and images. It serves AI teams that need trusted model training data and production‑grade output verification for use cases such as physical AI, advertising, commerce, and defense. The platform routes decisions to models, a 100M+ contributor network, or verified domain experts based on confidence levels, delivering a neutral trust layer for production AI.
image: https://www.tasq.ai/wp-content/uploads/2026/10/tasq_hero_desktop_poster.jpg
layout: provider
modified: '2026-10-21'
name: Tasq.ai
nav: Providers
network: true
overview: 'Tasq.ai is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Annotation, Evaluation, Validation, AI Infrastructure, and Production AI.


  Tasq.ai''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 9.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Tasq Domain Security
  slug: tasq-domain-security
  summary_line: TLSv1.3 · DMARC
slug: tasq
tags:
- Annotation
- Evaluation
- Validation
- AI Infrastructure
- Production AI
website: https://tasq.ai/
---
