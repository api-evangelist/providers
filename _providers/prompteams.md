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
- description: Prompteams API documentation is hosted on ReadMe but no machine‑readable contract was found for this provider.
  name: Prompteams API
  slug: prompteams-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/prompteams/well-known/prompteams-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/prompteams-well-known.yml
- group: other
  href: https://artifacts.apis.io/prompteams/hosts/prompteams-hosts.yml
  title: ''
  type: Hosts
  url: hosts/prompteams-hosts.yml
- group: other
  href: https://artifacts.apis.io/prompteams/vendors/prompteams-vendors.yml
  title: ''
  type: Vendors
  url: vendors/prompteams-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://www.prompteams.com/api/auth/login
- group: auth
  href: https://artifacts.apis.io/prompteams/security/prompteams-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/prompteams-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://prompteams.com/
- group: docs
  title: ''
  type: Documentation
  url: https://reineed-doc.readme.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.prompteams.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.prompteams.com/blog
coverage:
  checked: '2026-10-18'
  detail: Documentation is on a ReadMe site that only lists a Reineed OpenAPI spec, not a Prompteams contract.
  evidence:
  - status: 200
    url: https://reineed-doc.readme.io/openapi/6501c8c913c97b0074750b3e
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-18'
description: Prompteams provides an AI prompt management platform that enables teams to version, test, and collaborate on large language model prompts. It offers features such as prompt versioning, automated testing suites, real‑time API endpoints for prompts, and CI/CD pipeline integration. Users can manage prompt repositories, run unlimited test cases, and monitor prompt performance, all through a web interface and API. The platform aims to streamline prompt engineering workflows for enterprises and developers, improving reliability and reducing hallucinations in AI applications.
image: https://www.prompteams.com/favicon.jpg
layout: provider
modified: '2026-10-18'
name: Prompteams
nav: Providers
network: true
overview: 'Prompteams is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Prompt Management, Collaboration, Version Control, and Testing.


  Prompteams'' developer surface includes documentation, pricing, engineering blog, and 6 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 7.8
  coverage:
    artifact_dirs: 11
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.4
  facets:
    access_clarity: 11.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 12.2
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
screenshot: https://apis.io/screenshots/prompteams/prompteams-2026-11-03T141551.png
security:
- kind: domain-security
  name: Prompteams Domain Security
  slug: prompteams-domain-security
  summary_line: TLSv1.3 · HSTS
slug: prompteams
tags:
- Artificial Intelligence
- Prompt Management
- Collaboration
- Version Control
- Testing
- Company
website: https://prompteams.com/
---
