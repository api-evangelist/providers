---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    mcp_server: documented
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
  score: 5.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: The LocalImpact API provides programmatic access to locations, reviews, contacts, and webhooks.
  name: LocalImpact API
  slug: localimpact-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/localimpact/plans/localimpact-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/localimpact-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/localimpact/conventions/localimpact-conventions.yml
  title: ''
  type: Conventions
  url: conventions/localimpact-conventions.yml
- group: auth
  href: https://artifacts.apis.io/localimpact/authentication/localimpact-authentication.yml
  title: ''
  type: Authentication
  url: authentication/localimpact-authentication.yml
- group: design
  href: https://artifacts.apis.io/localimpact/conformance/localimpact-conformance.yml
  title: ''
  type: Conformance
  url: conformance/localimpact-conformance.yml
- group: other
  href: https://artifacts.apis.io/localimpact/hosts/localimpact-hosts.yml
  title: ''
  type: Hosts
  url: hosts/localimpact-hosts.yml
- group: other
  href: https://artifacts.apis.io/localimpact/vendors/localimpact-vendors.yml
  title: ''
  type: Vendors
  url: vendors/localimpact-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://localimpact.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://localimpact.com/privacy
- group: start
  title: ''
  type: Login
  url: https://app.localimpact.com/login
- group: start
  title: ''
  type: GettingStarted
  url: https://localimpact.com/api#/#getting-started
- group: auth
  href: https://artifacts.apis.io/localimpact/security/localimpact-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/localimpact-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://localimpact.com/
- group: docs
  title: ''
  type: Documentation
  url: https://localimpact.com/api
- group: commercial
  title: ''
  type: Pricing
  url: https://localimpact.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://localimpact.com/blog
- group: operate
  title: ''
  type: HelpCenter
  url: https://localimpact.com/help
- group: operate
  title: ''
  type: Contact
  url: https://localimpact.com/contact
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://localimpact.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: LocalImpact provides review management software for local businesses, agencies, and multi‑location brands. It helps collect more 5‑star reviews, showcase them where customers decide, and build trust without bloated enterprise pricing. Founded by Vitaly, the platform offers review collection, AI‑driven replies, social sharing, and agency workflows, focusing on usability, affordability, and real results.
image: https://localimpact.com/assets/site/images/LocalImpact-dashboard@2x.webp
layout: provider
modified: '2026-11-03'
name: LocalImpact
nav: Providers
network: true
overview: 'LocalImpact is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Review, Software-as-a-Service, Local Business, Reputation, and Software.


  LocalImpact''s developer surface includes authentication, getting-started guide, documentation, pricing, engineering blog, and 12 more developer resources.'
plans:
- name: Localimpact Plans Pricing
  plan_count: 3
  slug: localimpact-plans-pricing
random_paper: 9
score:
  band: emerging
  composite: 24.0
  coverage:
    artifact_dirs: 11
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Localimpact Authentication
  slug: localimpact-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Localimpact Domain Security
  slug: localimpact-domain-security
  summary_line: TLSv1.3 · DMARC
slug: localimpact
tags:
- Review
- Software-as-a-Service
- Local Business
- Reputation
- Software
website: https://localimpact.com/
---
