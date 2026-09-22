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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-09-21'
api_count: 1
apis:
- description: Programmatic access to Inoreader feed data and user actions.
  name: Inoreader API
  slug: inoreader-api
artifact_total: 4
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/inoreader/refs/heads/main/rate-limits/inoreader-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/inoreader-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/inoreader/refs/heads/main/plans/inoreader-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/inoreader-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/inoreader/refs/heads/main/changelog/inoreader-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/inoreader-changelog.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/inoreader/refs/heads/main/mcp/inoreader-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/inoreader-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/inoreader/refs/heads/main/packages/inoreader-packages.yml
  title: ''
  type: SDKs
  url: packages/inoreader-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/inoreader/refs/heads/main/packages/inoreader-packages.yml
  title: ''
  type: Packages
  url: packages/inoreader-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.inoreader.com/
- group: other
  title: ''
  type: Leadership
  url: https://www.inoreader.com/discover/topic/business/management
- group: other
  title: ''
  type: x-coverage
  url: ''
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/inoreader/refs/heads/main/security/inoreader-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/inoreader-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://inoreader.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.inoreader.com/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://www.inoreader.com/developers/
- group: docs
  title: ''
  type: APIReference
  url: https://www.inoreader.com/developers/api-endpoint
- group: start
  title: ''
  type: GettingStarted
  url: https://www.inoreader.com/developers/register-app
- group: operate
  title: ''
  type: Support
  url: https://www.inoreader.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.inoreader.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.inoreader.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.inoreader.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.inoreader.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.inoreader.com/privacy_policy
created: '2026-09-21'
description: Inoreader provides a powerful RSS feed reader and content aggregation platform that lets users subscribe to, organize, and share web content. It offers features such as automated tagging, rules for filtering, offline access, and collaborative sharing for teams. The service includes a developer API that enables programmatic access to feed data, article content, and user actions, supporting integration with third‑party applications and custom workflows.
image: https://www.inoreader.com/images/landing/v4/og-images/og-image-default.png
layout: provider
modified: '2026-09-21'
name: Inoreader
nav: Providers
network: true
overview: 'Inoreader publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, RSS, Content Aggregation, and Productivity.


  Inoreader''s developer surface includes changelog, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 13 more developer resources.'
plans:
- name: Inoreader Plans Pricing
  plan_count: 3
  slug: inoreader-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 2
  name: Inoreader Rate Limits
  slug: inoreader-rate-limits
score:
  band: thin
  composite: 37.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 47.0
    catalog_earned_first_party: 20.0
    catalog_gap: 68.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 52.4
    discoverability: 50.0
    operational_transparency: 52.6
  provenance:
    mcp: unknown
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Inoreader Domain Security
  slug: inoreader-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: inoreader
tags:
- Company
- RSS
- Content Aggregation
- Productivity
website: https://inoreader.com/
---
