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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API referenced on developer portal but no machine‑readable spec found.
  name: Cannon VoIP API
  slug: cannon-voip-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/cannonvoip-com/plans/cannonvoip-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cannonvoip-com-plans-pricing.yml
- group: auth
  title: ''
  type: Security
  url: https://cannonvoip.com/post/security-compliance#report
- group: design
  href: https://artifacts.apis.io/cannonvoip-com/conformance/cannonvoip-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cannonvoip-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cannonvoip-com/llms/cannonvoip-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cannonvoip-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/cannonvoip-com/well-known/cannonvoip-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cannonvoip-com-security.txt
- group: agent
  href: https://artifacts.apis.io/cannonvoip-com/well-known/cannonvoip-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cannonvoip-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/cannonvoip-com/hosts/cannonvoip-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cannonvoip-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/cannonvoip-com/vendors/cannonvoip-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cannonvoip-com-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://cannonvoip.com/trust
- group: operate
  title: ''
  type: Support
  url: https://cannonvoip.com/help/desk-phone-wifi
- group: company
  title: ''
  type: Newsroom
  url: https://cannonvoip.com/press
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.cannonvoip.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CannonVoIP
- group: auth
  href: https://artifacts.apis.io/cannonvoip-com/security/cannonvoip-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cannonvoip-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/cannonvoip-com/security/cannonvoip-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cannonvoip-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cannonvoip.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://cannonvoip.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://cannonvoip.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://cannonvoip.com/learn
- group: operate
  title: ''
  type: FAQ
  url: https://cannonvoip.com/faq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cannonvoip.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cannonvoip.com/privacy-and-security
- group: operate
  title: ''
  type: StatusPage
  url: https://app.cannonvoip.com/status
coverage:
  checked: '2026-11-04'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract found on any discovered host.
  evidence:
  - status: 200
    url: https://portal.cannonvoip.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: Cannon VoIP provides a cloud‑based business phone system with no contracts, pricing at $34 per extension per month, AI receptionist, eFax, SMS and integrations. Based in Fort Worth, Texas, serving US businesses since 2019.
image: https://cannonvoip.com/assets/og-image.png
layout: provider
modified: '2026-11-04'
name: Cannon VoIP
nav: Providers
network: true
overview: 'Cannon VoIP is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include VoIP, Business Communications, Cloud Phone System, US, and Software-as-a-Service.


  Cannon VoIP''s developer surface includes support, pricing, engineering blog, documentation, FAQ, and 18 more developer resources.'
plans:
- name: Cannonvoip Com Plans Pricing
  plan_count: 6
  slug: cannonvoip-com-plans-pricing
random_paper: 7
score:
  band: emerging
  composite: 24.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 51.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 13.1
    discoverability: 58.0
    operational_transparency: 15.8
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cannonvoip Com Domain Security
  slug: cannonvoip-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Cannonvoip Com Vulnerability Disclosure
  slug: cannonvoip-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: cannonvoip-com
tags:
- VoIP
- Business Communications
- Cloud Phone System
- US
- Software-as-a-Service
website: https://cannonvoip.com/
---
