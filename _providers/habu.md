---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 38.9
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: The Habu Clean Room API — published by LiveRamp as "External APIs for Customer Integration" and still served from Habu's own api.habu.com host — lets customers set up and manage clean rooms, provision
  name: Habu Clean Room API
  slug: habu-clean-room-api
artifact_total: 9
collections:
- collection_type: open
  name: External APIs for Customer Integration
  slug: open-habu-clean-room-api
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.liveramp.com/clean-room-api
- group: docs
  title: ''
  type: APIReference
  url: https://developers.liveramp.com/clean-room-api/reference/clean-room-api-endpoints
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.liveramp.com/clean-room-api/reference/python-tutorial-for-creating-and-running-questions
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/liveramp
- group: commercial
  title: ''
  type: TermsOfService
  url: https://liveramp.com/liveramp-terms-of-service/
- group: start
  title: ''
  type: Login
  url: https://console.habu.com/login
- group: operate
  title: ''
  type: StatusPage
  url: https://status.liveramp.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/habu-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/habu-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/habu-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/habu-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/habu-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/habu-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/habu-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/habu-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/habu-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/habu-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/habu-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/habu-clean-room-api-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/habu-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/habu-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://habu.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.liveramp.com/clean-room-api
- group: company
  title: ''
  type: Blog
  url: https://liveramp.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://liveramp.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://liveramp.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://liveramp.com/privacy
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.liveramp.com/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.liveramp.com/
- group: auth
  title: ''
  type: Security
  url: https://liveramp.com/security/bug-bounty
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/habu-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/habu-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/habu-trust-center.yml
created: '2026-07-17'
description: 'Habu was a data clean room and data collaboration company, founded in 2017 and headquartered in San Francisco, that let brands, publishers, and media platforms run privacy-safe joins and analytics on each other''s first-party data without moving or exposing raw records. In January 2024 Habu was acquired by LiveRamp, and the product now ships as LiveRamp Clean Room within the LiveRamp data collaboration network. The habu.com marketing domain 301-redirects to liveramp.com and the old docs.habu.com / developer.habu.com hosts no longer resolve, but the product API itself is still very much alive on Habu''s own infrastructure: api.habu.com/v1 answers today, and LiveRamp publishes its full 151-operation OpenAPI 3.0.0 contract — titled "External APIs for Customer Integration", contact platform_admin@habu.com — under developers.liveramp.com. The console is still Habu-branded at console.habu.com. This profile originated as a portfolio-lead stub (backed by Norwest Venture Partners and
  Wing Venture Capital) and is enriched here from that live, publicly documented surface plus the security and compliance posture inherited by LiveRamp.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/habu.png
layout: provider
modified: '2026-08-12'
name: Habu
nav: Providers
network: true
overview: 'Habu publishes 1 API on the [APIs.io](https://apis.io/) network: Clean Room API. Tagged areas include Company, Data Clean Room, Data Collaboration, Advertising, and Privacy.


  Habu''s developer surface includes API reference, getting-started guide, changelog, authentication, documentation, engineering blog, pricing, and 27 more developer resources.'
plans:
- name: Habu Plans Pricing
  plan_count: 0
  slug: habu-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 3
  name: Habu Rate Limits
  slug: habu-rate-limits
scopes:
- name: Habu Scopes
  scope_count: 0
  slug: habu-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 48.8
  delta: -11.4
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 16.7
    contract_quality: 56.6
    developer_ergonomics: 16.1
    discoverability: 87.0
    governance: 16.7
    operational_transparency: 76.3
  previous_composite: 60.2
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/habu/refs/heads/main/screenshots/habu-2026-07-25T220519.png
security:
- kind: authentication
  name: Habu Authentication
  slug: habu-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Habu Domain Security
  slug: habu-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Habu Vulnerability Disclosure
  slug: habu-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Habu Trust Center
  slug: habu-trust-center
  summary_line: SOC 2 Type 2, ISO 27001, GDPR, CCPA, SOX
slug: habu
tags:
- Company
- Data Clean Room
- Data Collaboration
- Advertising
- Privacy
- Identity
- Marketing
- Analytics
website: https://habu.com
---
