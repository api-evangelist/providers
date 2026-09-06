---
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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.2
  scored_at: '2026-09-05'
api_count: 2
apis:
- description: 'The core Ximalaya Open Platform HTTP+JSON API on api.ximalaya.com: free on-demand content (albums, tracks, categories, tags), paid on-demand content metadata, content search with hot/suggest words, re'
  name: Ximalaya Open Platform API
  slug: ximalaya-open-platform-api
- description: 'The paid-content and distribution HTTP+JSON API on mpay.ximalaya.com: product/price lookup (get_price_info, get_gradient_activity_price_info), album and track distribution (distribute, v2/distribute, '
  name: Ximalaya Paid Content & Distribution API
  slug: ximalaya-open-pay-distribution-api
artifact_total: 8
asyncapis:
- description: ''
  name: Ximalaya Callbacks Webhooks
  slug: ximalaya-callbacks-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ximalaya-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ximalaya.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://open.ximalaya.com/
- group: docs
  title: ''
  type: Documentation
  url: https://open.ximalaya.com/doc/api
- group: docs
  title: ''
  type: APIReference
  url: https://open.ximalaya.com/doc/api
- group: start
  title: ''
  type: GettingStarted
  url: https://open.ximalaya.com/doc/quickStart
- group: start
  title: ''
  type: SignUp
  url: https://open.ximalaya.com/developer/app
- group: commercial
  title: ''
  type: TermsOfService
  url: https://open.ximalaya.com/doc/detailQuickStart?categoryId=18&articleId=35
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://open.ximalaya.com/doc/detailQuickStart?categoryId=18&articleId=78
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/XimalayaCloud
- group: start
  title: ''
  type: Sandbox
  url: sandbox/ximalaya-sandbox.yml
- group: start
  title: ''
  type: Console
  url: https://open.ximalaya.com/doc/tool
- group: auth
  title: ''
  type: Authentication
  url: authentication/ximalaya-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/ximalaya-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ximalaya-error-codes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ximalaya-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ximalaya-plans-pricing.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ximalaya-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ximalaya-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ximalaya-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ximalaya-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/ximalaya-callbacks-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/ximalaya-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/ximalaya-packages.yml
- group: design
  title: ''
  type: Components
  url: components/ximalaya-components.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ximalaya-llms.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/ximalaya-mcp.yml
created: '2026-09-04'
description: Ximalaya (喜马拉雅) is China's largest online audio and podcast platform, distributing audiobooks, radio dramas, children's content, courses, news and live broadcast radio. Its developer surface is the Ximalaya Open Platform (open.ximalaya.com), a partner-oriented program that lets mobile apps, smart speakers, in-car head units, H5 sub-sites and WeChat mini-programs embed Ximalaya audio. The platform publishes a documented HTTP+JSON API across two hosts — api.ximalaya.com for content, search, recommendation, OAuth2 accounts, user data and analytics callbacks, and mpay.ximalaya.com for paid-content distribution, pricing and orders — secured by an app_key plus an HMAC-SHA1/MD5 request signature, with OAuth 2.0 access tokens for user-private data.
image: https://s1.xmcdn.com/yx/open-website/last/build/favicon.ico
layout: provider
modified: '2026-09-04'
name: Ximalaya
nav: Providers
network: true
overview: 'Ximalaya publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Audio, Podcasts, Audiobooks, and Media.


  The Ximalaya catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Ximalaya''s developer surface includes documentation, API reference, getting-started guide, signup flow, sandbox, developer console, authentication, and 20 more developer resources.'
plans:
- name: Ximalaya Plans Pricing
  plan_count: 0
  slug: ximalaya-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 3
  name: Ximalaya Rate Limits
  slug: ximalaya-rate-limits
scopes:
- name: Ximalaya Scopes
  scope_count: 0
  slug: ximalaya-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 28.7
  coverage:
    artifact_dirs: 17
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -16.2
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 42.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 44.9
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: falling
security:
- kind: authentication
  name: Ximalaya Authentication
  slug: ximalaya-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Ximalaya Domain Security
  slug: ximalaya-domain-security
  summary_line: TLSv1.2 · DNSSEC
slug: ximalaya
tags:
- Company
- Audio
- Podcasts
- Audiobooks
- Media
- Content Distribution
- Streaming
- China
- Entertainment
website: https://www.ximalaya.com/
---
