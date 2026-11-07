---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Microsoft Yammer Agentic Access
  operation_count: 33
  slug: microsoft-yammer-agentic-access
  summary_line: 33 operations · 12 acting
api_count: 1
apis:
- description: 'The Yammer REST API (now Viva Engage) provides access to enterprise social networking features including messages, groups, users, and networks. Developers can post messages, manage group memberships, '
  name: Yammer REST API
  slug: rest-api
- baseURL: https://www.yammer.com/api/v1/
  baseurl_source: declared
  description: The Files API from Microsoft Yammer — 1 operation(s) for files.
  name: Microsoft Yammer Files API
  slug: microsoft-yammer-files-api
- baseURL: https://www.yammer.com/api/v1/
  baseurl_source: declared
  description: The Groups API from Microsoft Yammer — 2 operation(s) for groups.
  name: Microsoft Yammer Groups API
  slug: microsoft-yammer-groups-api
- baseURL: https://www.yammer.com/api/v1/
  baseurl_source: declared
  description: The Messages API from Microsoft Yammer — 12 operation(s) for messages.
  name: Microsoft Yammer Messages API
  slug: microsoft-yammer-messages-api
- baseURL: https://www.yammer.com/api/v1/
  baseurl_source: declared
  description: The Networks API from Microsoft Yammer — 1 operation(s) for networks.
  name: Microsoft Yammer Networks API
  slug: microsoft-yammer-networks-api
- baseURL: https://www.yammer.com/api/v1/
  baseurl_source: declared
  description: The Search API from Microsoft Yammer — 1 operation(s) for search.
  name: Microsoft Yammer Search API
  slug: microsoft-yammer-search-api
- baseURL: https://www.yammer.com/api/v1/
  baseurl_source: declared
  description: The Subscriptions API from Microsoft Yammer — 2 operation(s) for subscriptions.
  name: Microsoft Yammer Subscriptions API
  slug: microsoft-yammer-subscriptions-api
- baseURL: https://www.yammer.com/api/v1/
  baseurl_source: declared
  description: The Threads API from Microsoft Yammer — 1 operation(s) for threads.
  name: Microsoft Yammer Threads API
  slug: microsoft-yammer-threads-api
- baseURL: https://www.yammer.com/api/v1/
  baseurl_source: declared
  description: The Topics API from Microsoft Yammer — 1 operation(s) for topics.
  name: Microsoft Yammer Topics API
  slug: microsoft-yammer-topics-api
- baseURL: https://www.yammer.com/api/v1/
  baseurl_source: declared
  description: The Users API from Microsoft Yammer — 5 operation(s) for users.
  name: Microsoft Yammer Users API
  slug: microsoft-yammer-users-api
artifact_total: 30
collections:
- collection_type: open
  name: Viva Engage (Yammer) Legacy REST Files API
  slug: open-microsoft-yammer-files-api
- collection_type: open
  name: Viva Engage (Yammer) Legacy REST Files Groups API
  slug: open-microsoft-yammer-groups-api
- collection_type: open
  name: Viva Engage (Yammer) Legacy REST Files Messages API
  slug: open-microsoft-yammer-messages-api
- collection_type: open
  name: Viva Engage (Yammer) Legacy REST Files Networks API
  slug: open-microsoft-yammer-networks-api
- collection_type: open
  name: Viva Engage (Yammer) Legacy REST Files Search API
  slug: open-microsoft-yammer-search-api
- collection_type: open
  name: Viva Engage (Yammer) Legacy REST Files Subscriptions API
  slug: open-microsoft-yammer-subscriptions-api
- collection_type: open
  name: Viva Engage (Yammer) Legacy REST Files Threads API
  slug: open-microsoft-yammer-threads-api
- collection_type: open
  name: Viva Engage (Yammer) Legacy REST Files Topics API
  slug: open-microsoft-yammer-topics-api
- collection_type: open
  name: Viva Engage (Yammer) Legacy REST Files Users API
  slug: open-microsoft-yammer-users-api
- collection_type: open
  name: Viva Engage (Yammer) Legacy REST API
  slug: open-microsoft-yammer
common:
- group: other
  title: ''
  type: Leadership
  url: https://news.microsoft.com/leadership
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.microsoft.com/en-us/changelog
- group: company
  title: ''
  type: Blog
  url: https://techcommunity.microsoft.com/category/azure/blog/analyticsonazure
- group: design
  href: https://artifacts.apis.io/microsoft-yammer/rules/microsoft-yammer-rules.yml
  title: ''
  type: Spectral
  url: rules/microsoft-yammer-rules.yml
- group: design
  href: https://artifacts.apis.io/microsoft-yammer/vocabulary/microsoft-yammer-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/microsoft-yammer-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/microsoft-yammer/conventions/microsoft-yammer-conventions.yml
  title: ''
  type: Conventions
  url: conventions/microsoft-yammer-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.microsoft.com/en-us/trust-center
- group: operate
  title: ''
  type: Deprecation
  url: https://learn.microsoft.com/en-us/rest/api/yammer/getting-started
- group: design
  href: https://artifacts.apis.io/microsoft-yammer/lifecycle/microsoft-yammer-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/microsoft-yammer-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/microsoft-yammer/conformance/microsoft-yammer-conformance.yml
  title: ''
  type: Conformance
  url: conformance/microsoft-yammer-conformance.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-yammer/llms/microsoft-yammer-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/microsoft-yammer-llms.txt
- group: auth
  href: https://artifacts.apis.io/microsoft-yammer/well-known/microsoft-yammer-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/microsoft-yammer-security.txt
- group: agent
  href: https://artifacts.apis.io/microsoft-yammer/well-known/microsoft-yammer-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/microsoft-yammer-well-known.yml
- group: other
  href: https://artifacts.apis.io/microsoft-yammer/hosts/microsoft-yammer-hosts.yml
  title: ''
  type: Hosts
  url: hosts/microsoft-yammer-hosts.yml
- group: other
  href: https://artifacts.apis.io/microsoft-yammer/vendors/microsoft-yammer-vendors.yml
  title: ''
  type: Vendors
  url: vendors/microsoft-yammer-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.microsoft.com/security
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/rest/api/yammer/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/rest/api/yammer/
- group: docs
  title: ''
  type: APIReference
  url: https://learn.microsoft.com/en-us/rest/api/yammer/yammer-core-apis
- group: auth
  href: https://artifacts.apis.io/microsoft-yammer/security/microsoft-yammer-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/microsoft-yammer-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-yammer/security/microsoft-yammer-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-yammer-vulnerability-disclosure.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-yammer/plans/microsoft-yammer-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/microsoft-yammer-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/microsoft-yammer/rate-limits/microsoft-yammer-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/microsoft-yammer-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-yammer/finops/microsoft-yammer-finops.yml
  title: ''
  type: FinOps
  url: finops/microsoft-yammer-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/
- group: agent
  href: https://artifacts.apis.io/microsoft-yammer/agentic-access/microsoft-yammer-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-yammer-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-yammer/security/microsoft-yammer-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microsoft-yammer-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-yammer/authentication/microsoft-yammer-authentication.yml
  title: ''
  type: Authentication
  url: authentication/microsoft-yammer-authentication.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-yammer/scopes/microsoft-yammer-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-yammer-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/yammer
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/yammer-inc
- group: start
  title: ''
  type: Portal
  url: https://engage.cloud.microsoft/
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/rest/api/yammer/oauth-2
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/
created: '2024-01-01'
description: APIs for Yammer (now Viva Engage) enterprise social networking platform providing access to messages, groups, users, and networks.
finops:
- has_sources: false
  method: generated
  name: Microsoft Yammer Finops
  primary_unit: request
  service_category: API
  slug: microsoft-yammer-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-yammer.png
layout: provider
modified: '2026-04-28'
name: Microsoft Yammer
nav: Providers
network: true
overview: 'Microsoft Yammer publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Files API, Groups API, Messages API, and 7 more. Tagged areas include Enterprise Social, Microsoft, Social Network, Viva Engage, and Yammer.


  The Microsoft Yammer catalog on APIs.io includes 1 Spectral governance ruleset.


  Microsoft Yammer''s developer surface includes changelog, engineering blog, getting-started guide, documentation, API reference, authentication, developer portal, and 29 more developer resources.'
plans:
- name: Microsoft Yammer Plans Pricing
  plan_count: 3
  slug: microsoft-yammer-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 4
  name: Microsoft Yammer Rate Limits
  slug: microsoft-yammer-rate-limits
rules:
- authorship: generated
  effective_rule_count: 93
  extends:
  - spectral:oas
  name: Microsoft Yammer API Rules
  rule_count: 52
  severity_counts:
    error: 50
    hint: 0
    info: 1
    warn: 1
  slug: microsoft-yammer-rules
scopes:
- name: Microsoft Yammer Scopes
  scope_count: 2
  slug: microsoft-yammer-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 53.5
  coverage:
    artifact_dirs: 25
    catalog_earned: 52.8
    catalog_earned_first_party: 12.0
    catalog_gap: 62.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 18.5
  facets:
    access_clarity: 44.7
    contract_governance: 22.0
    contract_quality: 44.9
    developer_ergonomics: 57.1
    discoverability: 66.1
    operational_transparency: 68.4
  previous_composite: 35.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/microsoft-yammer/microsoft-yammer-2026-06-20T185547.png
security:
- kind: authentication
  name: Microsoft Yammer Authentication
  slug: microsoft-yammer-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Yammer Domain Security
  slug: microsoft-yammer-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Yammer Vulnerability Disclosure
  slug: microsoft-yammer-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Microsoft Yammer Trust Center
  slug: microsoft-yammer-trust-center
  summary_line: GDPR
slug: microsoft-yammer
tags:
- Enterprise Social
- Microsoft
- Social Network
- Viva Engage
- Yammer
website: https://www.microsoft.com/
---
