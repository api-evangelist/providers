---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 3
asyncapis:
- description: ''
  name: Cheddar Up Webhooks
  slug: cheddar-up-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://cheddarup.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.cheddarup.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cheddarup.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.cheddarup.com/javascript-sdk/component-use/checkout
- group: start
  title: ''
  type: GettingStarted
  url: https://www.cheddarup.com/how-does-cheddar-up-work/
- group: operate
  title: ''
  type: Support
  url: https://support.cheddarup.com/
- group: company
  title: ''
  type: Blog
  url: https://www.cheddarup.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cheddarup.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://my.cheddarup.com/signup
- group: start
  title: ''
  type: Login
  url: https://my.cheddarup.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cheddarup.com/termsofuse/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cheddarup.com/privacypolicy/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cheddar-up-llms.txt
- group: design
  title: ''
  type: Components
  url: components/cheddar-up-components.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cheddar-up-authentication.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/cheddar-up-webhooks.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cheddar-up-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cheddar-up-domain-security.yml
created: '2026-07-17'
description: Cheddar Up is an all-in-one online platform that helps groups and communities collect payments and forms in one place. Purpose-built for PTAs/PTOs, booster clubs, youth sports teams, nonprofits, schools, clubs, HOAs, churches, and other volunteer-led organizations, it lets organizers collect dues, registrations, donations, event fees, fundraisers, and group gifts without any technical setup. It combines online payments (credit card, e-check, Apple Pay, Google Pay, and Link), custom forms, waivers, sign-ups, recurring payments, itemized storefronts, automated tracking and reporting, and multi-manager team administration. For technical users, Cheddar Up exposes an embeddable JavaScript SDK (a guest-facing Checkout component instantiated via CheddarUpWidgetFactory), API keys on the Team plan, and a native webhooks integration for syncing collection and payment events to external apps.
image: https://www.cheddarup.com/wp-content/uploads/2021/10/CUp_Logo_2c.svg
layout: provider
modified: '2026-07-18'
name: Cheddar Up
nav: Providers
network: true
overview: 'Cheddar Up is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Group Payments, Fundraising, and Non-Profit.


  The Cheddar Up catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Cheddar Up''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 11 more developer resources.'
random_paper: 2
score:
  band: thin
  composite: 37.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 41.6
    developer_ergonomics: 57.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 37.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 31.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cheddar-up/refs/heads/main/screenshots/cheddar-up-2026-07-25T205201.png
security:
- kind: authentication
  name: Cheddar Up Authentication
  slug: cheddar-up-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Cheddar Up Domain Security
  slug: cheddar-up-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cheddar-up
tags:
- Company
- Payments
- Group Payments
- Fundraising
- Non-Profit
- Schools
- Forms
- Fintech
- Payment Collection
website: https://cheddarup.com
---
