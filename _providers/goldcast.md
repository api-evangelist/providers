---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 22.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Public facing API for managing virtual events.
  name: Goldcast External API
  slug: goldcast-external-api
artifact_total: 5
asyncapis:
- description: ''
  name: Goldcast Webhooks
  slug: goldcast-webhooks
common:
- group: auth
  href: https://artifacts.apis.io/goldcast/well-known/goldcast-goldcast-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/goldcast-goldcast-security.txt
- group: agent
  href: https://artifacts.apis.io/goldcast/well-known/goldcast-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/goldcast-well-known.yml
- group: commercial
  href: https://artifacts.apis.io/goldcast/plans/goldcast-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/goldcast-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/goldcast/asyncapi/goldcast-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/goldcast-webhooks.yml
- group: auth
  href: https://artifacts.apis.io/goldcast/authentication/goldcast-authentication.yml
  title: ''
  type: Authentication
  url: authentication/goldcast-authentication.yml
- group: design
  href: https://artifacts.apis.io/goldcast/conformance/goldcast-conformance.yml
  title: ''
  type: Conformance
  url: conformance/goldcast-conformance.yml
- group: other
  href: https://artifacts.apis.io/goldcast/hosts/goldcast-hosts.yml
  title: ''
  type: Hosts
  url: hosts/goldcast-hosts.yml
- group: other
  href: https://artifacts.apis.io/goldcast/vendors/goldcast-vendors.yml
  title: ''
  type: Vendors
  url: vendors/goldcast-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://www.goldcast.io/integrations/webhooks
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.goldcast.io/trust
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.goldcast.io/trust/terms
- group: operate
  title: ''
  type: Support
  url: https://help.goldcast.io
- group: operate
  title: ''
  type: StatusPage
  url: https://goldcast.statuspage.io
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.goldcast.io/trust/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.goldcast.io/press
- group: start
  title: ''
  type: Login
  url: https://dashboard.goldcast.io/login
- group: start
  title: ''
  type: GettingStarted
  url: https://help.goldcast.io/en_US/QA-event-setup/24684404619035-de-indexing-your-goldcast-pages-from-google-search-results
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/goldcast
- group: auth
  href: https://artifacts.apis.io/goldcast/security/goldcast-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/goldcast-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.goldcast.io/
- group: docs
  title: ''
  type: Documentation
  url: https://www.goldcast.io/platform
- group: commercial
  title: ''
  type: Pricing
  url: https://www.goldcast.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.goldcast.io/blog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.goldcast.io/mcp
created: '2026-10-29'
description: Goldcast is an AI‑first video content platform that enables B2B companies to create, host, and manage webinars, virtual events, and on‑demand video experiences. Leveraging AI, Goldcast offers tools for content repurposing, automated highlights, analytics, and integration with marketing workflows, helping businesses engage audiences at scale.
image: https://www.goldcast.io/images/og-images/homepage.png
layout: provider
modified: '2026-10-29'
name: Goldcast
nav: Providers
network: true
overview: 'Goldcast is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Video, Artificial Intelligence, Webinars, and Event.


  The Goldcast catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Goldcast''s developer surface includes authentication, support, getting-started guide, documentation, pricing, engineering blog, and 18 more developer resources.'
plans:
- name: Goldcast Plans Pricing
  plan_count: 1
  slug: goldcast-plans-pricing
random_paper: 9
score:
  band: thin
  composite: 38.5
  coverage:
    artifact_dirs: 13
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.9
  facets:
    access_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 39.0
    developer_ergonomics: 31.0
    discoverability: 67.0
    operational_transparency: 25.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 50.4
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/goldcast/goldcast-2026-11-03T132916.png
security:
- kind: authentication
  name: Goldcast Authentication
  slug: goldcast-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Goldcast Domain Security
  slug: goldcast-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: goldcast
tags:
- Company
- Video
- Artificial Intelligence
- Webinars
- Event
- B2B
website: https://www.goldcast.io/
---
