---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
- description: OwlRelay provides an email-to-HTTP service with webhook integration, allowing developers to trigger webhooks via generated email addresses.
  name: OwlRelay API
  slug: owlrelay-api
artifact_total: 2
common:
- group: design
  href: https://artifacts.apis.io/owlrelay/conformance/owlrelay-conformance.yml
  title: ''
  type: Conformance
  url: conformance/owlrelay-conformance.yml
- group: auth
  href: https://artifacts.apis.io/owlrelay/well-known/owlrelay-bsky-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/owlrelay-bsky-security.txt
- group: agent
  href: https://artifacts.apis.io/owlrelay/well-known/owlrelay-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/owlrelay-well-known.yml
- group: other
  href: https://artifacts.apis.io/owlrelay/hosts/owlrelay-hosts.yml
  title: ''
  type: Hosts
  url: hosts/owlrelay-hosts.yml
- group: other
  href: https://artifacts.apis.io/owlrelay/vendors/owlrelay-vendors.yml
  title: ''
  type: Vendors
  url: vendors/owlrelay-vendors.yml
- group: auth
  href: https://artifacts.apis.io/owlrelay/security/owlrelay-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/owlrelay-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://owlrelay.email/
- group: docs
  title: ''
  type: Documentation
  url: https://owlrelay.email/
- group: commercial
  title: ''
  type: Pricing
  url: https://owlrelay.email/#pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://owlrelay.email/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://owlrelay.email/privacy
- group: operate
  title: ''
  type: Community
  url: https://github.com/papra-hq/owlrelay
- group: operate
  title: ''
  type: Community
  url: https://discord.gg/8UPjzsrBNF
- group: operate
  title: ''
  type: Community
  url: https://bsky.app/profile/owlrelay.email
coverage:
  checked: '2026-10-27'
  detail: Documentation site is a JavaScript-rendered SPA, no machine‑readable OpenAPI spec found.
  evidence:
  - status: 200
    url: https://owlrelay.email/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-27'
description: OwlRelay provides an open-source solution that converts incoming emails into HTTP requests, enabling developers to trigger webhooks and integrate email-driven workflows. Users can create unique email addresses that forward messages, including attachments, to specified endpoints, facilitating automation with services like Zapier, n8n, and custom APIs. The platform offers a self-hosted option and a hosted SaaS, focusing on simplicity, privacy, and extensibility for developers building email-triggered integrations.
image: https://owlrelay.email/og-image.png
layout: provider
modified: '2026-10-27'
name: OwlRelay
nav: Providers
network: true
overview: 'OwlRelay is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Email, Webhook, Open Source, and Automation.


  OwlRelay''s developer surface includes documentation, pricing, and 12 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 13.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.2
  facets:
    access_clarity: 15.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.1
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 19.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/owlrelay/owlrelay-2026-11-03T140824.png
security:
- kind: domain-security
  name: Owlrelay Domain Security
  slug: owlrelay-domain-security
  summary_line: TLSv1.3 · DMARC
slug: owlrelay
tags:
- Company
- Email
- Webhook
- Open Source
- Automation
website: https://owlrelay.email/
---
