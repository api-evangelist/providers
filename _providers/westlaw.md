---
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-09-25'
api_count: 1
apis:
- description: Developer portal for Westlaw APIs and integration resources.
  name: Westlaw API
  slug: westlaw-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/westlaw/refs/heads/main/hosts/westlaw-hosts.yml
  title: ''
  type: Hosts
  url: hosts/westlaw-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/westlaw/refs/heads/main/vendors/westlaw-vendors.yml
  title: ''
  type: Vendors
  url: vendors/westlaw-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.thomsonreuters.com/en/terms-of-use.html
- group: operate
  title: ''
  type: Support
  url: https://legal.thomsonreuters.com/en/support
- group: build
  title: ''
  type: SDKs
  url: https://legal.thomsonreuters.com/en/products/practical-law/government/libraries
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.thomsonreuters.com/en/privacy-statement
- group: commercial
  title: ''
  type: Pricing
  url: https://legal.thomsonreuters.com/en/westlaw/plans-and-pricing
- group: company
  title: ''
  type: Newsroom
  url: https://legal.thomsonreuters.com/en/insights/reports/2025-state-of-corporate-law-department-report/media
- group: start
  title: ''
  type: Login
  url: https://community.thomsonreuters.com/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://legal.thomsonreuters.com/en/products/highq/whats-new
- group: company
  title: ''
  type: Blog
  url: https://legal.thomsonreuters.com/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://legal.thomsonreuters.com/en/insights/white-papers/building-digital-trust-into-your-onboarding-tech-stack
- group: docs
  title: ''
  type: Documentation
  url: https://developers.thomsonreuters.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/westlaw/refs/heads/main/security/westlaw-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/westlaw-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://legal.thomsonreuters.com/en/westlaw
coverage:
  checked: 2026-09-23
  detail: Developer portal renders JavaScript and provides no machine‑readable OpenAPI, GraphQL, AsyncAPI, or WSDL specifications.
  evidence:
  - status: 200
    url: https://developers.thomsonreuters.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-23'
description: Westlaw, a Thomson Reuters legal research platform, provides AI‑enhanced tools, extensive case law, statutes, and practical guidance for law firms, businesses, and government agencies. Leveraging over 175 years of legal expertise, Westlaw delivers trusted research, drafting assistance, and compliance solutions across a wide range of practice areas.
image: https://legal.thomsonreuters.com/content/dam/ue/en-us/images/og-image/243454.png.transform/rect-768/q90/image.png
layout: provider
modified: '2026-09-23'
name: Westlaw
nav: Providers
network: true
overview: 'Westlaw publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Legal Tech, Research, Artificial Intelligence, Thomson Reuters, and Westlaw.


  Westlaw''s developer surface includes support, pricing, changelog, engineering blog, getting-started guide, documentation, and 9 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 23.6
  coverage:
    artifact_dirs: 5
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.5
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 58.9
    operational_transparency: 15.8
  previous_composite: 24.1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Westlaw Domain Security
  slug: westlaw-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: westlaw
tags:
- Legal Tech
- Research
- Artificial Intelligence
- Thomson Reuters
- Westlaw
website: https://legal.thomsonreuters.com/en/westlaw
---
