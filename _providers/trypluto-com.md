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
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/trypluto-com/hosts/trypluto-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/trypluto-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/trypluto-com/vendors/trypluto-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/trypluto-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/trypluto-com/security/trypluto-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/trypluto-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://trypluto.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://trypluto.com/
  reason: no-developer-program
  state: none
created: '2026-10-24'
description: Pluto Health provides a clinical intelligence platform that unifies fragmented health data into a single source of truth, enabling care teams to close gaps, surface unmet needs, and deliver measurable outcomes. The platform offers in‑home phlebotomy, at‑home diagnostics, asynchronous clinician chats, and longitudinal follow‑up, serving health systems, providers, and patients across the United States.
image: https://pub-bb2e103a32db4e198524a2e9ed8f35b4.r2.dev/33c41e82-abb8-4669-9499-a8582a8f35ed/id-preview-95f3ae57--679efd5b-c14f-400d-81cb-01f63dcdf14e.lovable.app-1776992589521.png
layout: provider
modified: '2026-10-24'
name: Pluto
nav: Providers
network: true
overview: Pluto is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health Tech, Clinical Intelligence, Data Integration, and Patient Care.
random_paper: 7
score:
  band: minimal
  composite: 3.7
  coverage:
    artifact_dirs: 8
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
    discoverability: 48.2
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 3.7
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
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/trypluto-com/trypluto-com-2026-11-03T145155.png
security:
- kind: domain-security
  name: Trypluto Com Domain Security
  slug: trypluto-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: trypluto-com
tags:
- Company
- Health Tech
- Clinical Intelligence
- Data Integration
- Patient Care
website: https://trypluto.com/
---
