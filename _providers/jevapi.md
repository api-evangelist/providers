---
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.4
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Jev API provides fast decision-making via the Jev model hosted on BeatAPI. It returns choices, scores, and probabilities via POST /v1/systemone.
  name: Jev API
  slug: jev-api
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/jevapi/authentication/jevapi-authentication.yml
  title: ''
  type: Authentication
  url: authentication/jevapi-authentication.yml
- group: design
  href: https://artifacts.apis.io/jevapi/errors/jevapi-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/jevapi-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/jevapi/llms/jevapi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/jevapi-llms.txt
- group: other
  href: https://artifacts.apis.io/jevapi/hosts/jevapi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/jevapi-hosts.yml
- group: other
  href: https://artifacts.apis.io/jevapi/vendors/jevapi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/jevapi-vendors.yml
- group: auth
  href: https://artifacts.apis.io/jevapi/security/jevapi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/jevapi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://jevapi.io
- group: docs
  title: ''
  type: Documentation
  url: https://jevapi.io/jev-api/
- group: docs
  title: ''
  type: APIReference
  url: https://jevapi.io/jev-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://jevapi.io/what-is-jev/
- group: operate
  title: ''
  type: Support
  url: https://jevapi.io/privacy/
- group: company
  title: ''
  type: Blog
  url: https://jevapi.io/blog/jev-use-cases/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://jevapi.io/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://jevapi.io/terms/
coverage:
  checked: '2026-10-30'
  detail: The Jev API documentation is a JavaScript‑rendered SPA, so no machine‑readable contract could be fetched.
  evidence:
  - status: 200
    url: https://beatapi.io/jev-api
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-30'
description: JevAPI is an independent developer guide and resource for the Jev decision model, offering fast, typed decisions for software. The site explains Jev through documented request shapes, decision patterns, and production safeguards, helping developers evaluate whether the model fits their software before building on it. Maintained by the BeatAPI team, it provides API guides, tutorials, comparisons with LLMs, and links to the official Jev API hosted on BeatAPI.
image: https://jevapi.io/og-image.png
layout: provider
modified: '2026-10-30'
name: JevAPI
nav: Providers
network: true
overview: 'JevAPI is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, API, DecisionModel, Software, and DeveloperGuide.


  JevAPI''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, and 8 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 21.0
  coverage:
    artifact_dirs: 11
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 47.6
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Jevapi Authentication
  slug: jevapi-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Jevapi Domain Security
  slug: jevapi-domain-security
  summary_line: TLSv1.3 · HSTS
slug: jevapi
tags:
- Company
- API
- DecisionModel
- Software
- DeveloperGuide
website: https://jevapi.io
---
