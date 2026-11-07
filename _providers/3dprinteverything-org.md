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
api_count: 1
apis:
- description: 3D Print Everything provides an API for ordering and managing 3D prints.
  name: 3D Print Everything API
  slug: 3d-print-everything-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/3dprinteverything-org/llms/3dprinteverything-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/3dprinteverything-org-llms.txt
- group: other
  href: https://artifacts.apis.io/3dprinteverything-org/hosts/3dprinteverything-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/3dprinteverything-org-hosts.yml
- group: other
  href: https://artifacts.apis.io/3dprinteverything-org/vendors/3dprinteverything-org-vendors.yml
  title: ''
  type: Vendors
  url: vendors/3dprinteverything-org-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://3dprinteverything.org/staff/login
- group: auth
  href: https://artifacts.apis.io/3dprinteverything-org/security/3dprinteverything-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/3dprinteverything-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://3dprinteverything.org/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://3dprinteverything.org/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://3dprinteverything.org/privacy
coverage:
  checked: '2026-10-31'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found on the provider's hosts.
  evidence:
  - status: 404
    url: https://3dprinteverything.org/openapi.json
  - status: 0
    url: https://api.3dprinteverything.org/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: 3D Print Everything is an industrial 3D printing service based in Frisco, TX, offering B2B rapid prototyping, low‑volume production, and replacement parts. Founded in 2016 by Michael Lynn, the company grew from a single bedroom printer to a fleet of Bambu Lab machines, serving engineers and manufacturers across Dallas‑Fort Worth with a range of materials including PLA, PETG, ASA, nylon, and resin.
image: https://3dprinteverything.org/brand/og-default.jpg
layout: provider
modified: '2026-10-31'
name: 3D Print Everything
nav: Providers
network: true
overview: 3D Print Everything is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include 3D Printing, Manufacturing, B2B Services, Rapid Prototyping, and Dallas-Fort Worth.
random_paper: 14
score:
  band: minimal
  composite: 8.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.0
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 12.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: 3Dprinteverything Org Domain Security
  slug: 3dprinteverything-org-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: 3dprinteverything-org
tags:
- 3D Printing
- Manufacturing
- B2B Services
- Rapid Prototyping
- Dallas-Fort Worth
website: https://3dprinteverything.org/
---
