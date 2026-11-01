---
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
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/apiway/plans/apiway-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/apiway-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/apiway/changelog/apiway-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/apiway-changelog.yml
- group: auth
  href: https://artifacts.apis.io/apiway/authentication/apiway-authentication.yml
  title: ''
  type: Authentication
  url: authentication/apiway-authentication.yml
- group: agent
  href: https://artifacts.apis.io/apiway/llms/apiway-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/apiway-llms.txt
- group: agent
  href: https://artifacts.apis.io/apiway/well-known/apiway-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/apiway-well-known.yml
- group: other
  href: https://artifacts.apis.io/apiway/hosts/apiway-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apiway-hosts.yml
- group: other
  href: https://artifacts.apis.io/apiway/vendors/apiway-vendors.yml
  title: ''
  type: Vendors
  url: vendors/apiway-vendors.yml
- group: auth
  href: https://artifacts.apis.io/apiway/security/apiway-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apiway-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apiway.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apiway.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://apiway.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://apiway.ai/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://apiway.ai/docs#getting-started
- group: operate
  title: ''
  type: Support
  url: https://apiway.ai/contact
- group: company
  title: ''
  type: Blog
  url: https://apiway.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://apiway.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://apiway.ai/login?mode=register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://apiway.ai/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://apiway.ai/legal/privacy-policy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/apiway/workspace
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://apiway.ai/api/mcp
  - status: 200
    url: https://apiway.ai/
  reason: partner-login
  state: gated
created: '2026-10-20'
description: Apiway provides an all‑in‑one AI‑powered workspace that enables businesses to build, automate, and scale applications without code. Users can create AI‑driven apps, automate lead capture, generate marketing content, design visuals, and manage workflows all within a unified platform. The service integrates with popular tools like Google Sheets, Telegram, and Stripe, offering templates for email marketing, social media, e‑commerce, and more. Apiway aims to accelerate digital transformation by letting teams prototype and launch AI‑enhanced solutions quickly, with a focus on ease of use and collaborative editing.
image: https://apiway.ai/opengraph-image?ee7c37b661a27a0e
layout: provider
modified: '2026-10-20'
name: Apiway
nav: Providers
network: true
overview: 'Apiway is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Workspace, Automation, and No-code.


  Apiway''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 13 more developer resources.'
plans:
- name: Apiway Plans Pricing
  plan_count: 7
  slug: apiway-plans-pricing
random_paper: 3
score:
  band: thin
  composite: 35.0
  coverage:
    artifact_dirs: 11
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 61.9
    discoverability: 48.2
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Apiway Authentication
  slug: apiway-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Apiway Domain Security
  slug: apiway-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: apiway
tags:
- Company
- AI
- Workspace
- Automation
- No-code
website: https://apiway.ai/
---
