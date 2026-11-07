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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/drgsystem-de/hosts/drgsystem-de-hosts.yml
  title: ''
  type: Hosts
  url: hosts/drgsystem-de-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.drgsystem.de/news
- group: auth
  href: https://artifacts.apis.io/drgsystem-de/security/drgsystem-de-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/drgsystem-de-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://drgsystem.de/
coverage:
  checked: '2026-11-06'
  detail: MCP endpoint requires POST, which is disallowed, preventing contract discovery
  evidence:
  - status: 405
    url: https://drgsystem.de/mcp
  reason: auth-required
  state: gated
created: '2026-11-05'
description: DRG System Deutschland provides an online catalogue of medical classification systems including ICD-10-GM, OPS, DRG, ZE, PEPP, DKR, ATC and related coding guidelines. The platform offers searchable access to all years from 2010 to 2027, with comparison tools, news updates, and a coding trainer to assist healthcare professionals in accurate billing and documentation.
image: https://www.drgsystem.de/opengraph-image-s7q7cj?c27aeabcd91b6252
layout: provider
modified: '2026-11-05'
name: DRG System Deutschland
nav: Providers
network: true
overview: DRG System Deutschland is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Medical Coding, Catalog, Germany, and DRG.
random_paper: 16
score:
  band: minimal
  composite: 3.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Drgsystem De Domain Security
  slug: drgsystem-de-domain-security
  summary_line: TLSv1.3 · DMARC
slug: drgsystem-de
tags:
- Healthcare
- Medical Coding
- Catalog
- Germany
- DRG
website: https://drgsystem.de/
---
