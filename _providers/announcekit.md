---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.8
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The AnnounceKit API provides GraphQL and REST endpoints for programmatically creating and updating posts, syncing user data, managing widgets, and automating product changelog workflows. Supports 11 w
  name: AnnounceKit API
  slug: announcekit-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/announcekit-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/announcekit-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/announcekit
- group: company
  title: ''
  type: Website
  url: https://announcekit.app/
- group: docs
  title: ''
  type: Documentation
  url: https://announcekit.app/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://announcekit.app/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://changelog.announcekit.app/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/announcekitapp
- group: build
  title: ''
  type: Examples
  url: https://announcekit.app/examples
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://announcekit.app/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://announcekit.app/terms
- group: company
  title: ''
  type: Blog
  url: http://announcekit.app/blog/
created: '2026-03-29'
description: AnnounceKit is a product communication platform providing changelog management, in-app notification widgets, feature request boards, roadmaps, and NPS surveys. It enables product teams to communicate updates to users via 10+ widget display modes, email digests, Slack, webhooks, and RSS, with GraphQL and REST APIs for programmatic integration.
finops:
- name: Announcekit Finops
  service_category: API
  slug: announcekit-finops
graphqls:
- description: The AnnounceKit API provides GraphQL and REST endpoints for programmatically creating and updating posts, syncing user data, managing widgets, and automating product changelog workflows. Supports 11 w
  name: AnnounceKit GraphQL API
  slug: announcekit-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/announcekit.png
layout: provider
modified: '2026-04-19'
name: AnnounceKit
nav: Providers
network: true
overview: 'AnnounceKit publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Changelog, Feature Requests, NPS, Notification, and Product Communication.


  AnnounceKit''s developer surface includes documentation, pricing, changelog, code examples, engineering blog, and 7 more developer resources.'
plans:
- name: Announcekit Plans Pricing
  plan_count: 3
  slug: announcekit-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Announcekit Rate Limits
  slug: announcekit-rate-limits
score:
  band: emerging
  composite: 25.7
  coverage:
    artifact_dirs: 7
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 55.3
    commercial_clarity: 55.3
    contract_governance: 0.0
    contract_quality: 6.7
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 25.7
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/announcekit/refs/heads/main/screenshots/announcekit-2026-06-20T172011.png
security:
- kind: domain-security
  name: Announcekit Domain Security
  slug: announcekit-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: trust-center
  name: Announcekit Trust Center
  slug: announcekit-trust-center
  summary_line: SOC 2, GDPR
slug: announcekit
tags:
- Changelog
- Feature Requests
- NPS
- Notification
- Product Communication
- Roadmaps
- Software-as-a-Service
- Widgets
website: https://announcekit.app/
---
