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
  href: https://artifacts.apis.io/aggors-com/llms/aggors-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aggors-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/aggors-com/well-known/aggors-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aggors-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/aggors-com/hosts/aggors-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aggors-com-hosts.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://aggors.com/developer
- group: auth
  href: https://artifacts.apis.io/aggors-com/security/aggors-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aggors-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aggors.com/
- group: docs
  title: ''
  type: Documentation
  url: https://aggors.com/developer/docs
- group: docs
  title: ''
  type: APIReference
  url: https://aggors.com/merchant-evidence-api
- group: start
  title: ''
  type: GettingStarted
  url: https://aggors.com/guides
- group: operate
  title: ''
  type: Support
  url: https://aggors.com/support
- group: operate
  title: ''
  type: Contact
  url: https://aggors.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aggors.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aggors.com/terms
coverage:
  checked: '2026-11-01'
  detail: Documentation page https://aggors.com/merchant-evidence-api provides description but no machine‑readable OpenAPI/AsyncAPI/GraphQL spec.
  evidence:
  - status: 200
    url: https://aggors.com/merchant-evidence-api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Aggors is an individual‑operated company building tools that let people and software inspect observable merchant evidence. It provides a merchant evidence API, guides, methodology, and support, emphasizing transparency of sources, measurements, and policy decisions. The service is not a marketplace, credit bureau, or safety certification.
image: https://aggors.com/assets/social-card.png
layout: provider
modified: '2026-11-01'
name: Aggors
nav: Providers
network: true
overview: 'Aggors is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, MerchantEvidence, Transparency, and Tools.


  Aggors'' developer surface includes documentation, API reference, getting-started guide, support, and 9 more developer resources.'
random_paper: 23
score:
  band: minimal
  composite: 10.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.9
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 39.3
    operational_transparency: 0.0
  previous_composite: 18.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aggors Com Domain Security
  slug: aggors-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: aggors-com
tags:
- Company
- MerchantEvidence
- Transparency
- Tools
website: https://aggors.com/
---
