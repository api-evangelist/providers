---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
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
    mcp_server: documented
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
  score: 21.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for BotPhone AI receptionist services
  name: BotPhone API
  slug: botphone-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/botphone-tel/plans/botphone-tel-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/botphone-tel-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/botphone-tel/conventions/botphone-tel-conventions.yml
  title: ''
  type: Conventions
  url: conventions/botphone-tel-conventions.yml
- group: auth
  href: https://artifacts.apis.io/botphone-tel/authentication/botphone-tel-authentication.yml
  title: ''
  type: Authentication
  url: authentication/botphone-tel-authentication.yml
- group: design
  href: https://artifacts.apis.io/botphone-tel/conformance/botphone-tel-conformance.yml
  title: ''
  type: Conformance
  url: conformance/botphone-tel-conformance.yml
- group: agent
  href: https://artifacts.apis.io/botphone-tel/llms/botphone-tel-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/botphone-tel-llms.txt
- group: agent
  href: https://artifacts.apis.io/botphone-tel/well-known/botphone-tel-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/botphone-tel-well-known.yml
- group: other
  href: https://artifacts.apis.io/botphone-tel/hosts/botphone-tel-hosts.yml
  title: ''
  type: Hosts
  url: hosts/botphone-tel-hosts.yml
- group: other
  href: https://artifacts.apis.io/botphone-tel/vendors/botphone-tel-vendors.yml
  title: ''
  type: Vendors
  url: vendors/botphone-tel-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.botphone.tel/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.botphone.tel/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.botphone.tel/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://www.botphone.tel/guides
- group: auth
  href: https://artifacts.apis.io/botphone-tel/security/botphone-tel-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/botphone-tel-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://botphone.tel/
coverage:
  checked: '2026-11-02'
  detail: Documentation pages are rendered via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://www.botphone.tel/guides
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-02'
description: BotPhone builds and manages AI receptionists that answer every call 24/7, screen spam, qualify leads, and book appointments for small and mid-sized businesses. Their service is fully managed and live in days, starting from $100 per month, providing an automated front‑line for customer interaction.
image: https://www.botphone.tel/images/botphone-opengraph.png
layout: provider
modified: '2026-11-02'
name: BotPhone
nav: Providers
network: true
overview: 'BotPhone is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Telephony, Receptionist, Software-as-a-Service, and BotPhone.


  BotPhone''s developer surface includes authentication, pricing, documentation, and 11 more developer resources.'
plans:
- name: Botphone Tel Plans Pricing
  plan_count: 2
  slug: botphone-tel-plans-pricing
random_paper: 9
score:
  band: emerging
  composite: 19.2
  coverage:
    artifact_dirs: 13
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Botphone Tel Authentication
  slug: botphone-tel-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Botphone Tel Domain Security
  slug: botphone-tel-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: botphone-tel
tags:
- Artificial Intelligence
- Telephony
- Receptionist
- Software-as-a-Service
- BotPhone
website: https://botphone.tel/
---
