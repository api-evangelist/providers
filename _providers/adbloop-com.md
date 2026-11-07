---
access_model:
  confidence: medium
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 24.7
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/adbloop-com/plans/adbloop-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/adbloop-com-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/adbloop-com/authentication/adbloop-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/adbloop-com-authentication.yml
- group: agent
  href: https://artifacts.apis.io/adbloop-com/llms/adbloop-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/adbloop-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/adbloop-com/well-known/adbloop-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/adbloop-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/adbloop-com/hosts/adbloop-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/adbloop-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/adbloop-com/vendors/adbloop-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/adbloop-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://adbloop.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://adbloop.com/privacy-policy/
- group: docs
  title: ''
  type: Documentation
  url: https://adbloop.com/guides/
- group: start
  title: ''
  type: GettingStarted
  url: https://adbloop.com/meta-ads-mcp-setup/
- group: auth
  href: https://artifacts.apis.io/adbloop-com/security/adbloop-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adbloop-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adbloop.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://adbloop.com/#pricing
- group: operate
  title: ''
  type: Contact
  url: https://adbloop.com/#contact
- group: start
  title: ''
  type: SignUp
  url: https://app.adbloop.com/signup
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://mcp.adbloop.com/mcp
  - status: 200
    url: https://adbloop.com/
  reason: partner-login
  state: gated
created: '2026-10-31'
description: Adbloop is a Meta Verified technology provider that enables users to bulk‑create Facebook and Instagram advertising campaigns directly from Google Sheets, a web dashboard, or AI assistants like Claude and ChatGPT. Offering over 150 campaign templates, the platform automates ad creation, dynamic creative testing, and management in under two minutes per campaign, all for a flat $19 per month. The service targets marketers and agencies seeking rapid, scalable Meta ad deployment without the complexity of traditional Ads Manager.
image: https://adbloop.com/og-image.png
layout: provider
modified: '2026-10-31'
name: Adbloop
nav: Providers
network: true
overview: 'Adbloop is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Advertising, Marketing, Automation, Artificial Intelligence, and Software-as-a-Service.


  Adbloop''s developer surface includes authentication, documentation, getting-started guide, pricing, signup flow, and 10 more developer resources.'
plans:
- name: Adbloop Com Plans Pricing
  plan_count: 4
  slug: adbloop-com-plans-pricing
random_paper: 21
score:
  band: emerging
  composite: 20.0
  coverage:
    artifact_dirs: 10
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.2
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 22.6
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 27.2
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Adbloop Com Authentication
  slug: adbloop-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Adbloop Com Domain Security
  slug: adbloop-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: adbloop-com
tags:
- Advertising
- Marketing
- Automation
- Artificial Intelligence
- Software-as-a-Service
- Company
website: https://adbloop.com/
---
