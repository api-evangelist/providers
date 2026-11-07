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
    agent_skills: unknown
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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Konnectify offers a RESTful API for managing integrations, agents, and workflows. Documentation is available at the developer portal.
  name: Konnectify API
  slug: konnectify-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/konnectify/plans/konnectify-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/konnectify-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/konnectify/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/konnectify/authentication/konnectify-authentication.yml
  title: ''
  type: Authentication
  url: authentication/konnectify-authentication.yml
- group: agent
  href: https://artifacts.apis.io/konnectify/llms/konnectify-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/konnectify-llms.txt
- group: other
  href: https://artifacts.apis.io/konnectify/hosts/konnectify-hosts.yml
  title: ''
  type: Hosts
  url: hosts/konnectify-hosts.yml
- group: other
  href: https://artifacts.apis.io/konnectify/vendors/konnectify-vendors.yml
  title: ''
  type: Vendors
  url: vendors/konnectify-vendors.yml
- group: auth
  href: https://artifacts.apis.io/konnectify/security/konnectify-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/konnectify-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://konnectify.co/
- group: start
  title: ''
  type: GettingStarted
  url: https://konnectify.co/sign-up
- group: docs
  title: ''
  type: Documentation
  url: https://konnectify.co/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://konnectify.co/integrations
- group: operate
  title: ''
  type: Support
  url: https://support.konnectify.co/support/home
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.konnectify.co/
- group: commercial
  title: ''
  type: Pricing
  url: https://konnectify.co/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://konnectify.co/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://konnectify.co/terms-of-use
- group: start
  title: ''
  type: SignUp
  url: https://konnectify.co/sign-up
- group: start
  title: ''
  type: Login
  url: https://konnectify.co/login
created: '2026-10-20'
description: Konnectify provides an AI‑powered integration platform that enables businesses to connect SaaS applications, automate workflows, and embed AI agents directly into their products. The service offers a visual workflow builder, pre‑built connectors for popular tools like Salesforce, HubSpot, and ChatGPT, and a robust API for custom integrations. Konnectify emphasizes security with a dedicated Trust Center, transparent pricing, and extensive documentation to help developers get started quickly.
layout: provider
modified: '2026-10-20'
name: Konnectify
nav: Providers
network: true
overview: 'Konnectify is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Integration Platform, Artificial Intelligence, Automation, Software-as-a-Service, and Low-Code.


  Konnectify''s developer surface includes authentication, getting-started guide, documentation, support, pricing, signup flow, and 12 more developer resources.'
plans:
- name: Konnectify Plans Pricing
  plan_count: 5
  slug: konnectify-plans-pricing
random_paper: 2
score:
  band: emerging
  composite: 25.1
  coverage:
    artifact_dirs: 11
    catalog_earned: 42.0
    catalog_earned_first_party: 12.0
    catalog_gap: 73.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.8
  facets:
    access_clarity: 57.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 36.2
    discoverability: 60.7
    operational_transparency: 0.0
  previous_composite: 34.9
  provenance:
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/konnectify/konnectify-2026-11-03T134512.png
security:
- kind: authentication
  name: Konnectify Authentication
  slug: konnectify-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Konnectify Domain Security
  slug: konnectify-domain-security
  summary_line: TLSv1.3 · DMARC
slug: konnectify
tags:
- Integration Platform
- Artificial Intelligence
- Automation
- Software-as-a-Service
- Low-Code
website: https://konnectify.co/
---
