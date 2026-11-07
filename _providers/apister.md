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
- group: design
  href: https://artifacts.apis.io/apister/conformance/apister-conformance.yml
  title: ''
  type: Conformance
  url: conformance/apister-conformance.yml
- group: other
  href: https://artifacts.apis.io/apister/hosts/apister-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apister-hosts.yml
- group: other
  href: https://artifacts.apis.io/apister/vendors/apister-vendors.yml
  title: ''
  type: Vendors
  url: vendors/apister-vendors.yml
- group: auth
  href: https://artifacts.apis.io/apister/security/apister-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apister-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apister.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.apister.io/
- group: docs
  title: ''
  type: Documentation
  url: https://www.apister.io/docs?section=introduction
- group: docs
  title: ''
  type: APIReference
  url: https://www.apister.io/docs?section=start-building
- group: start
  title: ''
  type: GettingStarted
  url: https://www.apister.io/docs?section=start-building
- group: operate
  title: ''
  type: Support
  url: https://www.apister.io/contact
- group: company
  title: ''
  type: Blog
  url: https://www.apister.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.apister.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.apister.io/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apister.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.apister.io/privacy-policy
coverage:
  checked: '2026-10-19'
  detail: No OpenAPI/AsyncAPI/GraphQL spec found at api.apister.io endpoints (all returned 404).
  evidence:
  - status: 404
    url: https://api.apister.io/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-19'
description: Apister is a no‑code API builder platform that enables users to create, deploy, and manage APIs without writing code. It offers a visual flow editor, multi‑database support, AI integration with OpenAI and Anthropic, and extensive tooling for building complex API logic through drag‑and‑drop components. Apister aims to streamline workflow automation for developers and non‑technical teams alike, providing features such as authentication, rate‑limiting, and real‑time testing, all accessible via a web‑based interface.
image: https://www.apister.io/open-graph-image.png
layout: provider
modified: '2026-10-19'
name: Apister
nav: Providers
network: true
overview: 'Apister is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, No-Code, API Builder, Automation, and Integration.


  Apister''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 8 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 15.9
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.6
  facets:
    access_clarity: 22.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 22.6
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 25.5
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/apister/apister-2026-11-03T121005.png
security:
- kind: domain-security
  name: Apister Domain Security
  slug: apister-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: apister
tags:
- Company
- No-Code
- API Builder
- Automation
- Integration
website: https://apister.io/
---
