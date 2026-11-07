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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/brixastudio-com/llms/brixastudio-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/brixastudio-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/brixastudio-com/well-known/brixastudio-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/brixastudio-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/brixastudio-com/hosts/brixastudio-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brixastudio-com-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://brixastudio.com/media/ejemplos/marca.jpg
- group: auth
  href: https://artifacts.apis.io/brixastudio-com/security/brixastudio-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brixastudio-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://brixastudio.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://brixastudio.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://brixastudio.com/terms
coverage:
  checked: '2026-11-03'
  detail: Provider's website offers no machine‑readable API specification and documentation pages are absent.
  evidence:
  - status: 200
    url: https://brixastudio.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: Brixa Studio provides an AI‑powered design automation platform that transforms designs from tools like Claude, Figma, and Canva into layered templates. Users can generate on‑brand graphics, social posts, data slides, and LinkedIn carousels at scale, with a web‑based application that supports multiple languages and integrates with AI assistants for endless publishing.
image: https://brixastudio.com/media/poster-16x9.jpg
layout: provider
modified: '2026-11-03'
name: Brixa Studio
nav: Providers
network: true
overview: Brixa Studio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Design, Artificial Intelligence, Automation, Templates, and Web App.
random_paper: 2
score:
  band: minimal
  composite: 6.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 49.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Brixastudio Com Domain Security
  slug: brixastudio-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: brixastudio-com
tags:
- Design
- Artificial Intelligence
- Automation
- Templates
- Web App
website: https://brixastudio.com/
---
