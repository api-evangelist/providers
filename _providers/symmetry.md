---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 38.8
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 3
asyncapis:
- description: ''
  name: Symmetry Webhooks
  slug: symmetry-webhooks
common:
- group: design
  href: https://artifacts.apis.io/symmetry/asyncapi/symmetry-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/symmetry-webhooks.yml
- group: design
  href: https://artifacts.apis.io/symmetry/conventions/symmetry-conventions.yml
  title: ''
  type: Conventions
  url: conventions/symmetry-conventions.yml
- group: auth
  href: https://artifacts.apis.io/symmetry/authentication/symmetry-authentication.yml
  title: ''
  type: Authentication
  url: authentication/symmetry-authentication.yml
- group: agent
  href: https://artifacts.apis.io/symmetry/llms/symmetry-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/symmetry-llms.txt
- group: auth
  href: https://artifacts.apis.io/symmetry/well-known/symmetry-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/symmetry-status-security.txt
- group: agent
  href: https://artifacts.apis.io/symmetry/well-known/symmetry-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/symmetry-well-known.yml
- group: other
  href: https://artifacts.apis.io/symmetry/hosts/symmetry-hosts.yml
  title: ''
  type: Hosts
  url: hosts/symmetry-hosts.yml
- group: other
  href: https://artifacts.apis.io/symmetry/vendors/symmetry-vendors.yml
  title: ''
  type: Vendors
  url: vendors/symmetry-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.symmetry.com/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://status.symmetry.com
- group: auth
  title: ''
  type: Security
  url: https://www.symmetry.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.symmetry.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.symmetry.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.symmetry.com/press
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.symmetry.com/ste/quickstarts/hosted-api-quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://docs.symmetry.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api.symmetry.com/i9/docs
- group: auth
  href: https://artifacts.apis.io/symmetry/security/symmetry-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/symmetry-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://symmetry.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: null
    url: https://docs.symmetry.com/mcp
  - status: 403
    url: https://api.symmetry.com/mcp
  - status: 403
    url: https://symmetry.com/mcp
  - status: 200
    url: https://symmetry.com/
  reason: no-developer-program
  state: none
created: '2026-10-21'
description: Symmetry provides payroll tax compliance software that enables employers, payroll providers, and platforms to calculate and file employee and employer taxes. Its products include a tax engine, payroll forms automation, I‑9 verification, payroll point location‑based tax rates, and minimum‑wage data for the United States and Canada. The company targets payroll providers, vertical payroll platforms, EOR and PEO services, recruiting and staffing firms, and large employers seeking automated, compliant payroll tax solutions.
image: https://www.symmetry.com/symmetry-link-preview.png
layout: provider
modified: '2026-10-21'
name: Symmetry
nav: Providers
network: true
overview: 'Symmetry is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Payroll Tax Compliance, Payroll Platforms, EOR, PEO, and Recruiting.


  The Symmetry catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Symmetry''s developer surface includes authentication, pricing, getting-started guide, documentation, API reference, and 14 more developer resources.'
random_paper: 18
score:
  band: thin
  composite: 33.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 39.0
    developer_ergonomics: 40.5
    discoverability: 50.0
    operational_transparency: 34.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Symmetry Authentication
  slug: symmetry-authentication
  summary_line: 5 schemes
- kind: domain-security
  name: Symmetry Domain Security
  slug: symmetry-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: symmetry
tags:
- Payroll Tax Compliance
- Payroll Platforms
- EOR
- PEO
- Recruiting
- Staffing
- Large Employers
- Tax APIs
website: https://symmetry.com/
---
