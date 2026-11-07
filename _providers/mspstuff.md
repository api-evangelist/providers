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
- description: API for AutomatedMSP platform providing read‑only access to MSP data and automation endpoints.
  name: AutomatedMSP API
  slug: automatedmsp-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/mspstuff/plans/mspstuff-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mspstuff-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.mspstuff.io/security
- group: agent
  href: https://artifacts.apis.io/mspstuff/llms/mspstuff-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mspstuff-llms.txt
- group: auth
  href: https://artifacts.apis.io/mspstuff/well-known/mspstuff-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/mspstuff-security.txt
- group: auth
  href: https://artifacts.apis.io/mspstuff/well-known/mspstuff-mspstuff-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/mspstuff-mspstuff-security.txt
- group: agent
  href: https://artifacts.apis.io/mspstuff/well-known/mspstuff-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mspstuff-well-known.yml
- group: other
  href: https://artifacts.apis.io/mspstuff/hosts/mspstuff-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mspstuff-hosts.yml
- group: other
  href: https://artifacts.apis.io/mspstuff/vendors/mspstuff-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mspstuff-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mspstuff.io/terms
- group: operate
  title: ''
  type: Support
  url: https://www.mspstuff.io/support
- group: auth
  title: ''
  type: Security
  url: https://www.mspstuff.io/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mspstuff.io/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.mspstuff.io/pricing
- group: auth
  href: https://artifacts.apis.io/mspstuff/security/mspstuff-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/mspstuff-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/mspstuff/security/mspstuff-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/mspstuff-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/mspstuff/security/mspstuff-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mspstuff-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mspstuff.io/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://www.mspstuff.io/mcp
  - status: 200
    url: https://mspstuff.io/
  reason: partner-login
  state: gated
created: '2026-10-18'
description: AutomatedMSP, operating under the brand MSPStuff, provides an AI‑powered platform that connects to Managed Service Provider (MSP) stacks including PSA, RMM, Microsoft 365, backup, network and billing systems. The service offers read‑only access with traceable answers via Switchboard or supported AI clients, enabling automation, insight and streamlined operations for MSPs.
image: https://www.mspstuff.io/og-default.png
layout: provider
modified: '2026-10-18'
name: AutomatedMSP,
nav: Providers
network: true
overview: 'AutomatedMSP, is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, MSP, Artificial Intelligence, Automation, and Software-as-a-Service.


  AutomatedMSP,''s developer surface includes support, pricing, and 15 more developer resources.'
plans:
- name: Mspstuff Plans Pricing
  plan_count: 4
  slug: mspstuff-plans-pricing
random_paper: 0
score:
  band: emerging
  composite: 19.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.0
  facets:
    access_clarity: 59.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 64.3
    operational_transparency: 5.3
  previous_composite: 25.7
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
screenshot: https://apis.io/screenshots/mspstuff/mspstuff-2026-11-03T135905.png
security:
- kind: domain-security
  name: Mspstuff Domain Security
  slug: mspstuff-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Mspstuff Vulnerability Disclosure
  slug: mspstuff-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Mspstuff Trust Center
  slug: mspstuff-trust-center
  summary_line: SOC 2, HIPAA
slug: mspstuff
tags:
- Company
- MSP
- Artificial Intelligence
- Automation
- Software-as-a-Service
website: https://mspstuff.io/
---
