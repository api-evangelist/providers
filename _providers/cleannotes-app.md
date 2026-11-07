---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API documentation for Clean Notes project management SaaS.
  name: Clean Notes API
  slug: clean-notes-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/cleannotes-app/plans/cleannotes-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cleannotes-app-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/cleannotes-app/conformance/cleannotes-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cleannotes-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cleannotes-app/well-known/cleannotes-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cleannotes-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/cleannotes-app/hosts/cleannotes-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cleannotes-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/cleannotes-app/vendors/cleannotes-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cleannotes-app-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cleannotes.app/terms
- group: operate
  title: ''
  type: Support
  url: https://cleannotes.app/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cleannotes.app/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://cleannotes.app/en/guides
- group: auth
  href: https://artifacts.apis.io/cleannotes-app/security/cleannotes-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cleannotes-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cleannotes.app/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://cleannotes.app/mcp
  - status: 200
    url: https://cleannotes.app/
  reason: partner-login
  state: gated
created: '2026-11-03'
description: Clean Notes is a project management SaaS for small teams, offering real‑time notes, tasks, and AI‑assisted features powered by Claude and ChatGPT. Users pay only for the projects they create, while invited collaborators use the platform for free. The service includes free, Pro, and Scale plans, with pricing in Brazilian Real.
image: https://cleannotes.app/favicon-96x96.png
layout: provider
modified: '2026-11-03'
name: Clean Notes
nav: Providers
network: true
overview: 'Clean Notes is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Project Management, Software-as-a-Service, Artificial Intelligence, Small Teams, and Collaboration.


  Clean Notes'' developer surface includes support, documentation, and 9 more developer resources.'
plans:
- name: Cleannotes App Plans Pricing
  plan_count: 3
  slug: cleannotes-app-plans-pricing
random_paper: 18
score:
  band: emerging
  composite: 15.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cleannotes App Domain Security
  slug: cleannotes-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cleannotes-app
tags:
- Project Management
- Software-as-a-Service
- Artificial Intelligence
- Small Teams
- Collaboration
website: https://cleannotes.app/
---
