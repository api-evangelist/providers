---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
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
    agent_skills: derived
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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 16.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for Scout reservation automation
  name: Scout API
  slug: scout-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/dinewithscout-com/plans/dinewithscout-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dinewithscout-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/dinewithscout-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/dinewithscout-com/authentication/dinewithscout-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dinewithscout-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/dinewithscout-com/conformance/dinewithscout-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dinewithscout-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dinewithscout-com/llms/dinewithscout-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dinewithscout-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/dinewithscout-com/well-known/dinewithscout-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dinewithscout-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/dinewithscout-com/hosts/dinewithscout-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dinewithscout-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dinewithscout.com/terms
- group: operate
  title: ''
  type: Support
  url: https://dinewithscout.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dinewithscout.com/privacy
- group: start
  title: ''
  type: Login
  url: https://dinewithscout.com/api/auth/login
- group: auth
  href: https://artifacts.apis.io/dinewithscout-com/security/dinewithscout-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dinewithscout-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dinewithscout.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dinewithscout.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://dinewithscout.com/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://dinewithscout.com/developers
created: '2026-11-05'
description: Scout (dinewithscout.com) offers a service that monitors restaurant reservation platforms such as Resy and automatically books hard-to-get tables on behalf of users. The platform provides a web interface and mobile app where users set their dining preferences, limits, and payment details. Scout then watches for openings and either auto‑books or sends alerts so users can secure reservations at popular venues. It targets diners seeking convenient, automated reservation handling and integrates with major reservation services.
image: https://dinewithscout.com/icons/og-image.png?v=scout-plans-1
layout: provider
modified: '2026-11-05'
name: Scout
nav: Providers
network: true
overview: 'Scout is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Restaurant, Reservations, Automation, Software-as-a-Service, and Consumer.


  Scout''s developer surface includes authentication, support, documentation, getting-started guide, and 12 more developer resources.'
plans:
- name: Dinewithscout Com Plans Pricing
  plan_count: 2
  slug: dinewithscout-com-plans-pricing
random_paper: 6
score:
  band: thin
  composite: 28.6
  coverage:
    artifact_dirs: 12
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 55.3
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 49.4
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Dinewithscout Com Authentication
  slug: dinewithscout-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Dinewithscout Com Domain Security
  slug: dinewithscout-com-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: capabilities
  slug: dinewithscout-com-capabilities-skill
slug: dinewithscout-com
tags:
- Restaurant
- Reservations
- Automation
- Software-as-a-Service
- Consumer
website: https://dinewithscout.com/
---
