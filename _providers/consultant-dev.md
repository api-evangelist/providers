---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
api_count: 1
apis:
- description: API for Consultant platform, documented at the MCP docs page.
  name: Consultant API
  slug: consultant-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/consultant-dev/plans/consultant-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/consultant-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/consultant-dev/conventions/consultant-dev-conventions.yml
  title: ''
  type: Conventions
  url: conventions/consultant-dev-conventions.yml
- group: auth
  href: https://artifacts.apis.io/consultant-dev/security/consultant-dev-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/consultant-dev-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/consultant-dev/authentication/consultant-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/consultant-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/consultant-dev/conformance/consultant-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/consultant-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/consultant-dev/llms/consultant-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/consultant-dev-llms.txt
- group: auth
  href: https://artifacts.apis.io/consultant-dev/well-known/consultant-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/consultant-dev-security.txt
- group: agent
  href: https://artifacts.apis.io/consultant-dev/well-known/consultant-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/consultant-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/consultant-dev/hosts/consultant-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/consultant-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/consultant-dev/vendors/consultant-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/consultant-dev-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://consultant.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://consultant.dev/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://consultant.dev/pricing
- group: start
  title: ''
  type: Login
  url: https://consultant.dev/sign-in
- group: company
  title: ''
  type: Blog
  url: https://consultant.dev/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://consultant.dev/mcp/docs
- group: auth
  href: https://artifacts.apis.io/consultant-dev/security/consultant-dev-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/consultant-dev-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/consultant-dev/security/consultant-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/consultant-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://consultant.dev/
coverage:
  checked: 2026-11-04"}<|end|><|start|>assistant<|channel|>final<|message|>{
  detail: Documentation page https://consultant.dev/mcp/docs returns HTML but provides no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL specifications.
  evidence:
  - status: 200
    url: https://consultant.dev/mcp/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: Consultant is a global platform that matches consulting assignments with qualified consultants and provides CV matching services. The service enables businesses to post consulting projects, while consultants can create profiles, showcase expertise, and receive relevant assignment opportunities. The site offers information about its mission, how it works, and contact options for both clients and consultants.
image: https://consultant.dev/og-image.png?v=nordic-blue
layout: provider
modified: '2026-11-04'
name: Consultant
nav: Providers
network: true
overview: 'Consultant is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include CV Matching, Contract Assignments, Rate Calculator, Income & Tax Tools, and Pension Planner.


  Consultant''s developer surface includes authentication, pricing, engineering blog, getting-started guide, and 15 more developer resources.'
plans:
- name: Consultant Dev Plans Pricing
  plan_count: 4
  slug: consultant-dev-plans-pricing
random_paper: 23
score:
  band: thin
  composite: 32.1
  coverage:
    artifact_dirs: 11
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 57.1
    operational_transparency: 10.5
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Consultant Dev Authentication
  slug: consultant-dev-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Consultant Dev Domain Security
  slug: consultant-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Consultant Dev Vulnerability Disclosure
  slug: consultant-dev-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: consultant-dev
tags:
- CV Matching
- Contract Assignments
- Rate Calculator
- Income & Tax Tools
- Pension Planner
website: https://consultant.dev/
---
