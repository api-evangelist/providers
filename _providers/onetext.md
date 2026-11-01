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
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 13.9
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/onetext/plans/onetext-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/onetext-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/onetext/changelog/onetext-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/onetext-changelog.yml
- group: auth
  href: https://artifacts.apis.io/onetext/authentication/onetext-authentication.yml
  title: ''
  type: Authentication
  url: authentication/onetext-authentication.yml
- group: agent
  href: https://artifacts.apis.io/onetext/llms/onetext-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/onetext-llms.txt
- group: auth
  href: https://artifacts.apis.io/onetext/well-known/onetext-calendly-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/onetext-calendly-security.txt
- group: agent
  href: https://artifacts.apis.io/onetext/well-known/onetext-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/onetext-well-known.yml
- group: other
  href: https://artifacts.apis.io/onetext/hosts/onetext-hosts.yml
  title: ''
  type: Hosts
  url: hosts/onetext-hosts.yml
- group: other
  href: https://artifacts.apis.io/onetext/vendors/onetext-vendors.yml
  title: ''
  type: Vendors
  url: vendors/onetext-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://home.onetext.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://home.onetext.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://home.onetext.com/pricing
- group: start
  title: ''
  type: Login
  url: https://onetext.com/login
- group: company
  title: ''
  type: Blog
  url: https://home.onetext.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.onetext.com/articles/1859988467-onboarding
- group: docs
  title: ''
  type: Documentation
  url: https://docs.onetext.com/
- group: auth
  href: https://artifacts.apis.io/onetext/security/onetext-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/onetext-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://home.onetext.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: null
    url: https://api.onetext.com/api/mcp
  - status: null
    url: https://onetext.com/api/mcp
  - status: 403
    url: https://docs.onetext.com/mcp
  - status: 200
    url: https://home.onetext.com/
  reason: no-developer-program
  state: none
created: '2026-10-25'
description: OneText provides a text‑to‑buy platform that enables ecommerce merchants to send SMS campaigns where shoppers can reply and complete purchases directly in the conversation. The service includes AI smart replies, payment processing via PayPal, Stripe, Maverick or Authorize.net, and integrates with Shopify, WooCommerce and Salesforce Commerce Cloud.
image: https://cdn.prod.website-files.com/65494a7bcadbde828287c9e0/65498dcde4a775933ae41ee3_OG%20Image%20compress.jpg
layout: provider
modified: '2026-10-25'
name: OneText
nav: Providers
network: true
overview: 'OneText is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Text to Buy, Ecommerce, SMS Marketing, Conversational Sales, and AI Smart Replies.


  OneText''s developer surface includes changelog, authentication, pricing, engineering blog, getting-started guide, documentation, and 11 more developer resources.'
plans:
- name: Onetext Plans Pricing
  plan_count: 1
  slug: onetext-plans-pricing
random_paper: 7
score:
  band: thin
  composite: 28.3
  coverage:
    artifact_dirs: 11
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 48.2
    operational_transparency: 26.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 17.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Onetext Authentication
  slug: onetext-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Onetext Domain Security
  slug: onetext-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: onetext
tags:
- Text to Buy
- Ecommerce
- SMS Marketing
- Conversational Sales
- AI Smart Replies
- Payments
- Cart Recovery
website: https://home.onetext.com/
---
