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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 27.2
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Resent email API with REST, SMTP relay, SDKs, and signed webhooks. Idempotent sends, delivery events, and 300 free emails a day.
  name: Resent Email API
  slug: email-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/resent-one/plans/resent-one-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/resent-one-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/resent-one/llms/resent-one-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/resent-one-llms.txt
- group: agent
  href: https://artifacts.apis.io/resent-one/well-known/resent-one-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/resent-one-well-known.yml
- group: other
  href: https://artifacts.apis.io/resent-one/hosts/resent-one-hosts.yml
  title: ''
  type: Hosts
  url: hosts/resent-one-hosts.yml
- group: other
  href: https://artifacts.apis.io/resent-one/vendors/resent-one-vendors.yml
  title: ''
  type: Vendors
  url: vendors/resent-one-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://resent.one/company/leadership/
- group: auth
  href: https://artifacts.apis.io/resent-one/security/resent-one-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/resent-one-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://resent.one/
- group: company
  title: ''
  type: Blog
  url: https://resent.one/blog/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://resent.one/features/email-api/
- group: docs
  title: ''
  type: Documentation
  url: https://resent.one/features/email-api/
- group: commercial
  title: ''
  type: Pricing
  url: https://resent.one/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://resent.one/account/register/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://resent.one/legal-notice/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://resent.one/legal/privacypolicy/
- group: operate
  title: ''
  type: Support
  url: https://resent.one/contact/
- group: operate
  title: ''
  type: StatusPage
  url: https://resent.one/contact/
- group: operate
  title: ''
  type: ChangeLog
  url: https://resent.one/releases/
coverage:
  checked: '2026-10-31'
  detail: No public OpenAPI or other machine-readable spec found despite API documentation page.
  evidence:
  - status: 200
    url: https://api.resent.one/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: Email and SMS for developers and enterprise SaaS. Send campaigns and transactional mail, automate journeys, and track delivery from one workspace. Start free with Resent. Resent email API with REST, SMTP relay, SDKs, and signed webhooks. Idempotent sends, delivery events, and 300 free emails a day. Start free—no card.
image: https://resent.one/api/branding/logo?v=1784710648835
layout: provider
modified: '2026-10-31'
name: resent-one
nav: Providers
network: true
overview: 'resent-one is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Email, SMS, Messaging, and SaaS.


  resent-one''s developer surface includes engineering blog, documentation, pricing, signup flow, support, changelog, and 12 more developer resources.'
plans:
- name: Resent One Plans Pricing
  plan_count: 5
  slug: resent-one-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Resent One Rate Limits
  slug: resent-one-rate-limits
scopes:
- name: Resent One Scopes
  scope_count: 0
  slug: resent-one-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 32.3
  coverage:
    artifact_dirs: 21
    catalog_earned: 47.8
    catalog_earned_first_party: 0.0
    catalog_gap: 67.2
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 67.9
    operational_transparency: 31.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 30.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Resent One Authentication
  slug: resent-one-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Resent One Domain Security
  slug: resent-one-domain-security
  summary_line: TLSv1.3 · DMARC
slug: resent-one
tags:
- Company
- Email
- SMS
- Messaging
- SaaS
website: https://resent.one/
---
