---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
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
    auth_clarity: bearer
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 9.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: REST API for managing prints, printers, and filaments.
  name: 3D Print Log API
  slug: 3d-print-log-api
artifact_total: 3
common:
- group: design
  href: https://artifacts.apis.io/3dprintlog-com/conventions/3dprintlog-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/3dprintlog-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/3dprintlog-com/authentication/3dprintlog-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/3dprintlog-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/3dprintlog-com/conformance/3dprintlog-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/3dprintlog-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/3dprintlog-com/llms/3dprintlog-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/3dprintlog-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/3dprintlog-com/well-known/3dprintlog-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/3dprintlog-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/3dprintlog-com/hosts/3dprintlog-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/3dprintlog-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.3dprintlog.com/docs/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.3dprintlog.com/docs/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.3dprintlog.com/docs/release-notes
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.3dprintlog.com</code
- group: auth
  href: https://artifacts.apis.io/3dprintlog-com/security/3dprintlog-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/3dprintlog-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://3dprintlog.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.3dprintlog.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.3dprintlog.com/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://www.3dprintlog.com/docs/api
- group: commercial
  title: ''
  type: Pricing
  url: https://www.3dprintlog.com/docs/pro-subscription
- group: operate
  title: ''
  type: Support
  url: https://www.3dprintlog.com/docs/contact
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://3dprintlog.com/openapi.json
  - status: null
    url: https://www.3dprintlog.com/openapi.json
  - status: null
    url: https://api.3dprintlog.com/swagger/v1/swagger.json
  - status: 401
    url: https://api.3dprintlog.com/mcp
  - status: 200
    url: https://3dprintlog.com/
  reason: partner-login
  state: gated
created: '2026-10-31'
description: 3D Print Log is a free web application with an Android companion that lets users track every 3D print they make. It records print settings, filament usage, photos, and outcomes, aggregating data from slicers like Cura, PrusaSlicer, OrcaSlicer, and OctoPrint. Users can view analytics, manage material inventories, and share prints, while developers can access a REST API for integration.
image: https://www.3dprintlog.com/assets/Homepage_PrinterList_ddc38eb8db62.webp
layout: provider
modified: '2026-10-31'
name: 3D Print Log
nav: Providers
network: true
overview: '3D Print Log is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include 3D Printing, Software-as-a-Service, Analytics, Inventory, and Community.


  3D Print Log''s developer surface includes authentication, changelog, documentation, getting-started guide, API reference, pricing, support, and 10 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 18.8
  coverage:
    artifact_dirs: 11
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.1
  facets:
    access_clarity: 15.8
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 66.1
    operational_transparency: 7.9
  previous_composite: 27.9
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: 3Dprintlog Com Authentication
  slug: 3dprintlog-com-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: 3Dprintlog Com Domain Security
  slug: 3dprintlog-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: 3dprintlog-com
tags:
- 3D Printing
- Software-as-a-Service
- Analytics
- Inventory
- Community
website: https://3dprintlog.com/
---
