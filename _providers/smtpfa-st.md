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
  band: agent-ready
  band_gated_from: agent-native
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
    mcp_server: documented
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
  score: 39.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: SMTPfast API provides email sending, domain management, webhooks and analytics.
  name: SMTPfast API
  slug: smtpfast-api
artifact_total: 5
asyncapis:
- description: ''
  name: Smtpfa St Webhooks
  slug: smtpfa-st-webhooks
common:
- group: start
  title: ''
  type: GettingStarted
  url: https://smtpfa.st/blog/getting-started
- group: commercial
  href: https://artifacts.apis.io/smtpfa-st/plans/smtpfa-st-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/smtpfa-st-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/smtpfa-st/asyncapi/smtpfa-st-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/smtpfa-st-webhooks.yml
- group: auth
  href: https://artifacts.apis.io/smtpfa-st/authentication/smtpfa-st-authentication.yml
  title: ''
  type: Authentication
  url: authentication/smtpfa-st-authentication.yml
- group: design
  href: https://artifacts.apis.io/smtpfa-st/conformance/smtpfa-st-conformance.yml
  title: ''
  type: Conformance
  url: conformance/smtpfa-st-conformance.yml
- group: agent
  href: https://artifacts.apis.io/smtpfa-st/llms/smtpfa-st-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/smtpfa-st-llms.txt
- group: agent
  href: https://artifacts.apis.io/smtpfa-st/well-known/smtpfa-st-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/smtpfa-st-well-known.yml
- group: other
  href: https://artifacts.apis.io/smtpfa-st/hosts/smtpfa-st-hosts.yml
  title: ''
  type: Hosts
  url: hosts/smtpfa-st-hosts.yml
- group: other
  href: https://artifacts.apis.io/smtpfa-st/vendors/smtpfa-st-vendors.yml
  title: ''
  type: Vendors
  url: vendors/smtpfa-st-vendors.yml
- group: build
  href: https://artifacts.apis.io/smtpfa-st/packages/smtpfa-st-packages.yml
  title: ''
  type: Packages
  url: packages/smtpfa-st-packages.yml
- group: start
  title: ''
  type: SignUp
  url: https://smtpfa.st/register
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@smtpfast/sdk
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/smtpfast
- group: operate
  title: ''
  type: ChangeLog
  url: https://smtpfa.st/changelog
- group: auth
  href: https://artifacts.apis.io/smtpfa-st/security/smtpfa-st-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/smtpfa-st-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://smtpfa.st/
- group: docs
  title: ''
  type: Documentation
  url: https://smtpfa.st/docs
- group: docs
  title: ''
  type: APIReference
  url: https://smtpfa.st/api/v1/openapi.json
- group: commercial
  title: ''
  type: Pricing
  url: https://smtpfa.st/pricing
- group: company
  title: ''
  type: Blog
  url: https://smtpfa.st/blog
- group: operate
  title: ''
  type: Support
  url: https://smtpfa.st/status
- group: commercial
  title: ''
  type: TermsOfService
  url: https://smtpfa.st/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://smtpfa.st/privacy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/smtpfast/workspace
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://smtpfa.st/api/mcp
  - status: 200
    url: https://smtpfa.st/
  reason: partner-login
  state: gated
created: '2026-10-31'
description: SMTPfast provides a developer-friendly email API that offers full visibility into the email delivery pipeline, including sending, tracking opens, bounces, and webhook events. It features a free tier with 3,000 emails per month, detailed analytics, and tools for SPF, DKIM, and DMARC checking. The service emphasizes transparency and real‑time tracing of each email, catering to developers who need reliable transactional email capabilities.
image: https://smtpfa.st/api/og?title=SMTPfast+-+Email+API+for+Developers&description=Built+on+AWS+SES+with+webhooks%2C+analytics%2C+and+developer-friendly+pricing.&section=Email+API
layout: provider
modified: '2026-10-31'
name: smtpfa-st
nav: Providers
network: true
overview: 'smtpfa-st is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Email, Transactional, and Developers.


  The smtpfa-st catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  smtpfa-st''s developer surface includes getting-started guide, authentication, signup flow, changelog, documentation, API reference, pricing, and 17 more developer resources.'
plans:
- name: Smtpfa St Plans Pricing
  plan_count: 4
  slug: smtpfa-st-plans-pricing
random_paper: 15
score:
  band: thin
  composite: 37.9
  coverage:
    artifact_dirs: 16
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.3
  facets:
    access_clarity: 53.9
    contract_governance: 4.5
    contract_quality: 39.0
    developer_ergonomics: 39.3
    discoverability: 57.1
    operational_transparency: 18.4
  previous_composite: 49.2
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
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/smtpfa-st/smtpfa-st-2026-11-03T143401.png
security:
- kind: authentication
  name: Smtpfa St Authentication
  slug: smtpfa-st-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Smtpfa St Domain Security
  slug: smtpfa-st-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: smtpfa-st
tags:
- Company
- Email
- Transactional
- Developers
website: https://smtpfa.st/
---
