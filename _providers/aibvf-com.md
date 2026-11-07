---
access_model:
  confidence: low
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/aibvf-com/hosts/aibvf-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aibvf-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/aibvf-com/vendors/aibvf-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aibvf-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/aibvf-com/security/aibvf-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aibvf-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aibvf.com/
coverage:
  checked: '2026-11-01'
  detail: No OpenAPI/AsyncAPI/GraphQL spec found; only HTML pages returned.
  evidence:
  - status: 200
    url: https://www.aibvf.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: AI BVF provides an open AI Business Value Framework that lets users describe AI initiatives and receive an Accelerate, Fix, or Stop verdict. The platform offers a start page, assessment tools, and documentation for integrating the framework via an MCP server. It emphasizes no account required for initial assessments and open-source MIT‑licensed code.
layout: provider
modified: '2026-11-01'
name: AI BVF
nav: Providers
network: true
overview: AI BVF is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Business, Framework, Assessment, and Open Source.
random_paper: 20
score:
  band: minimal
  composite: 3.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  previous_composite: 3.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aibvf Com Domain Security
  slug: aibvf-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: aibvf-com
tags:
- Artificial Intelligence
- Business
- Framework
- Assessment
- Open Source
- Company
website: https://aibvf.com/
---
