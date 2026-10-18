---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.8
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Openweb Agentic Access
  operation_count: 24
  slug: openweb-agentic-access
  summary_line: 24 operations · 10 acting
api_count: 9
apis:
- description: 'JWT-authenticated REST API for publishers on the OpenWeb platform: request an API token, export comments/users/ranks (v2 and v4), retrieve top comments and trending articles, manage SSO users (registe'
  name: OpenWeb Publisher API
  slug: openweb-publisher-api
- baseURL: https://api.openweb.com
  baseurl_source: declared
  description: The Export API from OpenWeb — 8 operation(s) for export.
  name: OpenWeb Export API
  slug: openweb-export-api
- baseURL: https://api.openweb.com
  baseurl_source: declared
  description: Top Comments
  name: OpenWeb top comments API
  slug: openweb-top-comments-api
- baseURL: https://api.openweb.com
  baseurl_source: declared
  description: Trending Articles
  name: OpenWeb trending articles API
  slug: openweb-trending-articles-api
- baseURL: https://api.openweb.com
  baseurl_source: declared
  description: SEO related to an article
  name: OpenWeb Article API
  slug: openweb-article-api
- baseURL: https://api.openweb.com
  baseurl_source: declared
  description: SEO related to a comment
  name: OpenWeb Comment API
  slug: openweb-comment-api
- baseURL: https://api.openweb.com
  baseurl_source: declared
  description: SEO related to a live blog
  name: OpenWeb live blog API
  slug: openweb-live-blog-api
- baseURL: https://api.openweb.com
  baseurl_source: declared
  description: Moderation Policy
  name: OpenWeb moderation policy API
  slug: openweb-moderation-policy-api
- baseURL: https://api.openweb.com
  baseurl_source: declared
  description: SEO related to scores and reviews
  name: OpenWeb score and reviews API
  slug: openweb-score-and-reviews-api
- baseURL: https://api.openweb.com
  baseurl_source: declared
  description: SSO-related calls
  name: OpenWeb SSO API
  slug: openweb-sso-api
- baseURL: https://api.openweb.com
  baseurl_source: declared
  description: Authorization token
  name: OpenWeb Token API
  slug: openweb-token-api
artifact_total: 18
asyncapis:
- description: ''
  name: Openweb Notifications Webhooks
  slug: openweb-notifications-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/openweb/refs/heads/main/agentic-access/openweb-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/openweb-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/openweb/refs/heads/main/rules/openweb-rules.yml
  title: ''
  type: Spectral
  url: rules/openweb-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/openweb/refs/heads/main/json-ld/openweb-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/openweb-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/openweb/refs/heads/main/vocabulary/openweb-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/openweb-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/openweb/refs/heads/main/data-model/openweb-data-model.yml
  title: ''
  type: DataModel
  url: data-model/openweb-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/openweb/refs/heads/main/security/openweb-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/openweb-trust-center.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/openweb/refs/heads/main/lifecycle/openweb-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/openweb-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/openweb/refs/heads/main/errors/openweb-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/openweb-problem-types.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/openweb/refs/heads/main/hosts/openweb-hosts.yml
  title: ''
  type: Hosts
  url: hosts/openweb-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/openweb/refs/heads/main/vendors/openweb-vendors.yml
  title: ''
  type: Vendors
  url: vendors/openweb-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.openweb.com/de/privacy/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.openweb.com/feed/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/openweb/refs/heads/main/security/openweb-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/openweb-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.openweb.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.openweb.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.openweb.com/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://developers.openweb.com/reference/post_v1-publisher-auth
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.openweb.com/docs/getting-started
- group: company
  title: ''
  type: Blog
  url: https://www.openweb.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/spotim
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.openweb.com/terms-of-service
- group: operate
  title: ''
  type: StatusPage
  url: https://status.openweb.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://updates.openweb.com
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.openweb.com
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/openweb/refs/heads/main/packages/openweb-packages.yml
  title: ''
  type: Packages
  url: packages/openweb-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/openweb/refs/heads/main/packages/openweb-packages.yml
  title: ''
  type: SDKs
  url: packages/openweb-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/openweb/refs/heads/main/authentication/openweb-authentication.yml
  title: ''
  type: Authentication
  url: authentication/openweb-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/openweb/refs/heads/main/conventions/openweb-conventions.yml
  title: ''
  type: Conventions
  url: conventions/openweb-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/openweb/refs/heads/main/conformance/openweb-conformance.yml
  title: ''
  type: Conformance
  url: conformance/openweb-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.openweb.com
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/openweb/refs/heads/main/lifecycle/openweb-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/openweb-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/openweb/refs/heads/main/changelog/openweb-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/openweb-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/openweb/refs/heads/main/asyncapi/openweb-notifications-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/openweb-notifications-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/openweb/refs/heads/main/components/openweb-components.yml
  title: ''
  type: Components
  url: components/openweb-components.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/openweb/refs/heads/main/mcp/openweb-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/openweb-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/openweb/refs/heads/main/well-known/openweb-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/openweb-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/openweb/refs/heads/main/llms/openweb-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/openweb-llms.txt
created: '2026-07-17'
description: OpenWeb (formerly Spot.IM) is a community and audience-engagement platform for publishers, delivering OpenWebOS — a unified, end-to-end suite for building community, harnessing first-party data, and driving sustainable revenue. Its developer platform exposes a JWT-authenticated Publisher API (comment export, top comments, trending articles, SSO user management, moderation policy, and SEO markup services) at api.openweb.com, a notification webhook surface, and web, Android, iOS, and React Native SDKs for embedding Conversation, Reactions, Community Spotlight, Live Blog, and Standalone Ad experiences. Backed by Insight Partners.
image: https://www.openweb.com/wp-content/uploads/2025/09/favicon-32x32-1.png
jsonld:
- class_count: 5
  name: Openweb Context
  property_count: 7
  slug: openweb-context
layout: provider
modified: '2026-10-06'
name: OpenWeb
nav: Providers
network: true
overview: 'OpenWeb publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Export API, top comments API, trending articles API, and 8 more. Tagged areas include Company, Consumer, Community, Comments, and Audience Engagement.


  The OpenWeb catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  OpenWeb''s developer surface includes documentation, API reference, getting-started guide, engineering blog, changelog, authentication, and 31 more developer resources.'
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: OpenWeb API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: openweb-rules
score:
  band: developing
  composite: 44.4
  coverage:
    artifact_dirs: 25
    catalog_earned: 53.8
    catalog_earned_first_party: 0.0
    catalog_gap: 61.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 9.7
  facets:
    access_clarity: 21.1
    contract_governance: 35.6
    contract_quality: 55.0
    developer_ergonomics: 40.5
    discoverability: 78.6
    operational_transparency: 42.1
  previous_composite: 34.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 10
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/openweb/refs/heads/main/screenshots/openweb-2026-08-07T190658.png
security:
- kind: authentication
  name: Openweb Authentication
  slug: openweb-authentication
  summary_line: http/jwt/sso · 4 schemes
- kind: domain-security
  name: Openweb Domain Security
  slug: openweb-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Openweb Trust Center
  slug: openweb-trust-center
  summary_line: SOC 2 Type II
slug: openweb
tags:
- Company
- Consumer
- Community
- Comments
- Audience Engagement
- Publishing
- Media
- Moderation
- Identity
- SSO
- Webhook
website: https://www.openweb.com/
---
