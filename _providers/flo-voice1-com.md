---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 4
asyncapis:
- description: ''
  name: Flo Voice1 Com Webhooks
  slug: flo-voice1-com-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/flo-voice1-com/plans/flo-voice1-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/flo-voice1-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/flo-voice1-com/asyncapi/flo-voice1-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/flo-voice1-com-webhooks.yml
- group: operate
  href: https://artifacts.apis.io/flo-voice1-com/changelog/flo-voice1-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/flo-voice1-com-changelog.yml
- group: auth
  href: https://artifacts.apis.io/flo-voice1-com/security/flo-voice1-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/flo-voice1-com-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/flo-voice1-com/conformance/flo-voice1-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/flo-voice1-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/flo-voice1-com/llms/flo-voice1-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/flo-voice1-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/flo-voice1-com/well-known/flo-voice1-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/flo-voice1-com-security.txt
- group: agent
  href: https://artifacts.apis.io/flo-voice1-com/well-known/flo-voice1-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/flo-voice1-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/flo-voice1-com/hosts/flo-voice1-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/flo-voice1-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/flo-voice1-com/vendors/flo-voice1-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/flo-voice1-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/flo-voice1-com/packages/flo-voice1-com-packages.yml
  title: ''
  type: SDKs
  url: packages/flo-voice1-com-packages.yml
- group: build
  href: https://artifacts.apis.io/flo-voice1-com/packages/flo-voice1-com-packages.yml
  title: ''
  type: Packages
  url: packages/flo-voice1-com-packages.yml
- group: start
  title: ''
  type: Login
  url: https://flo-voice1.com/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://flo-voice1.com/changelog
- group: auth
  href: https://artifacts.apis.io/flo-voice1-com/security/flo-voice1-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/flo-voice1-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/flo-voice1-com/security/flo-voice1-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/flo-voice1-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://flo-voice1.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://flo-voice1.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://flo-voice1.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://flo-voice1.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://flo-voice1.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://flo-voice1.com/contact
coverage:
  checked: '2026-10-30'
  detail: API documentation page https://flo-voice1.com/api-access redirects to a login form, preventing public access to the API spec.
  evidence:
  - status: 200
    url: https://flo-voice1.com/api-access
  reason: auth-required
  state: gated
created: '2026-10-30'
description: FloVoice SRL provides a service to rent real UK mobile phone numbers for SMS verification and messaging. Users can obtain numbers for WhatsApp, Telegram, Google, Discord, Instagram, X, PayPal and more, receiving verification codes instantly without using personal numbers. The platform offers a public API and npm SDK for automation, with pricing per code and subscription options. It includes a Telegram bot, a web portal, and a status page, aiming to simplify phone verification for AI agents and developers.
image: https://flo-voice1.com/logo.png
layout: provider
modified: '2026-10-30'
name: flo-voice1-com
nav: Providers
network: true
overview: 'flo-voice1-com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, SMS, Verification, United Kingdom, and Telecommunications.


  The flo-voice1-com catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  flo-voice1-com''s developer surface includes changelog, pricing, engineering blog, support, and 18 more developer resources.'
plans:
- name: Flo Voice1 Com Plans Pricing
  plan_count: 2
  slug: flo-voice1-com-plans-pricing
random_paper: 17
score:
  band: thin
  composite: 32.0
  coverage:
    artifact_dirs: 15
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.7
  facets:
    access_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 39.0
    developer_ergonomics: 10.7
    discoverability: 55.4
    operational_transparency: 26.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 38.7
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 22.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/flo-voice1-com/flo-voice1-com-2026-11-03T132149.png
security:
- kind: domain-security
  name: Flo Voice1 Com Domain Security
  slug: flo-voice1-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Flo Voice1 Com Vulnerability Disclosure
  slug: flo-voice1-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: flo-voice1-com
tags:
- Company
- SMS
- Verification
- United Kingdom
- Telecommunications
website: https://flo-voice1.com/
---
