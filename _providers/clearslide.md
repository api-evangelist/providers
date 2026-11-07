---
access_model:
  confidence: high
  label: Paid · Requires approval
  onboarding: approval
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 30.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Clearslide Agentic Access
  operation_count: 9
  slug: clearslide-agentic-access
  summary_line: 9 operations · 4 acting
api_count: 2
apis:
- baseURL: https://platform.clearslide.com
  baseurl_source: declared
  description: The Insights API from ClearSlide — 1 operation(s) for insights.
  name: ClearSlide Insights API
  slug: clearslide-insights-api
- baseURL: https://platform.clearslide.com
  baseurl_source: declared
  description: The Links API from ClearSlide — 1 operation(s) for links.
  name: ClearSlide Links API
  slug: clearslide-links-api
- baseURL: https://platform.clearslide.com
  baseurl_source: declared
  description: The Meetings API from ClearSlide — 2 operation(s) for meetings.
  name: ClearSlide Meetings API
  slug: clearslide-meetings-api
- baseURL: https://platform.clearslide.com
  baseurl_source: declared
  description: The Presentations API from ClearSlide — 1 operation(s) for presentations.
  name: ClearSlide Presentations API
  slug: clearslide-presentations-api
- baseURL: https://platform.clearslide.com
  baseurl_source: declared
  description: The Upload API from ClearSlide — 2 operation(s) for upload.
  name: ClearSlide Upload API
  slug: clearslide-upload-api
- baseURL: https://platform.clearslide.com
  baseurl_source: declared
  description: The Users API from ClearSlide — 1 operation(s) for users.
  name: ClearSlide Users API
  slug: clearslide-users-api
- description: ClearSlide's SCIM 2.0 (RFC 7644) user and group provisioning API, for automating directory sync from an identity provider. Serves /scim/ServiceProviderConfigs, /scim/Schemas (core User and Group), ful
  name: ClearSlide SCIM API
  slug: clearslide-scim-api
artifact_total: 24
collections:
- collection_type: open
  name: ClearSlide Platform Insights API
  slug: open-clearslide-insights-api
- collection_type: open
  name: ClearSlide Platform Insights Links API
  slug: open-clearslide-links-api
- collection_type: open
  name: ClearSlide Platform Insights Meetings API
  slug: open-clearslide-meetings-api
- collection_type: open
  name: ClearSlide Platform Insights Presentations API
  slug: open-clearslide-presentations-api
- collection_type: open
  name: ClearSlide Platform Insights Upload API
  slug: open-clearslide-upload-api
- collection_type: open
  name: ClearSlide Platform Insights Users API
  slug: open-clearslide-users-api
common:
- group: design
  href: https://artifacts.apis.io/clearslide/data-model/clearslide-data-model.yml
  title: ''
  type: DataModel
  url: data-model/clearslide-data-model.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.showpad.com/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.showpad.com/blog
- group: agent
  href: https://artifacts.apis.io/clearslide/agentic-access/clearslide-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/clearslide-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/clearslide/rules/clearslide-rules.yml
  title: ''
  type: Spectral
  url: rules/clearslide-rules.yml
- group: design
  href: https://artifacts.apis.io/clearslide/vocabulary/clearslide-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/clearslide-vocabulary.yml
- group: auth
  title: ''
  type: Security
  url: https://www.showpad.com/security
- group: other
  href: https://artifacts.apis.io/clearslide/a2a/clearslide-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/clearslide-a2a.yml
- group: other
  href: https://artifacts.apis.io/clearslide/hosts/clearslide-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clearslide-hosts.yml
- group: other
  href: https://artifacts.apis.io/clearslide/vendors/clearslide-vendors.yml
  title: ''
  type: Vendors
  url: vendors/clearslide-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: http://status.clearslide.com/
- group: company
  title: ''
  type: Newsroom
  url: https://www.showpad.com/press
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/showpad/
- group: company
  title: ''
  type: Website
  url: https://www.clearslide.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.clearslide.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.clearslide.com/docs/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://developer.clearslide.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.clearslide.com/docs/getting-started-1
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.clearslide.com/changelog
- group: operate
  title: ''
  type: Support
  url: https://developer.clearslide.com/discuss
- group: start
  title: ''
  type: Login
  url: https://www.clearslide.com/auth/login
- group: agent
  href: https://artifacts.apis.io/clearslide/llms/clearslide-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/clearslide-llms.txt
- group: docs
  href: https://artifacts.apis.io/clearslide/openapi/_original/clearslide-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/clearslide-openapi.yml
- group: other
  href: https://artifacts.apis.io/clearslide/overlays/clearslide-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/clearslide-openapi-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/clearslide/authentication/clearslide-authentication.yml
  title: ''
  type: Authentication
  url: authentication/clearslide-authentication.yml
- group: auth
  href: https://artifacts.apis.io/clearslide/scopes/clearslide-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/clearslide-scopes.yml
- group: design
  href: https://artifacts.apis.io/clearslide/conventions/clearslide-conventions.yml
  title: ''
  type: Conventions
  url: conventions/clearslide-conventions.yml
- group: design
  href: https://artifacts.apis.io/clearslide/lifecycle/clearslide-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/clearslide-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/clearslide/conformance/clearslide-conformance.yml
  title: ''
  type: Conformance
  url: conformance/clearslide-conformance.yml
- group: auth
  href: https://artifacts.apis.io/clearslide/security/clearslide-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/clearslide-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/clearslide/security/clearslide-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clearslide-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/clearslide/well-known/clearslide-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/clearslide-well-known.yml
- group: agent
  href: https://artifacts.apis.io/clearslide/mcp/clearslide-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/clearslide-mcp.yml
- group: agent
  href: https://artifacts.apis.io/clearslide/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  href: https://artifacts.apis.io/clearslide/openapi/_original/clearslide-platform-api-swagger.json
  title: ''
  type: OpenAPI
  url: openapi/_original/clearslide-platform-api-swagger.json
- group: other
  href: https://artifacts.apis.io/clearslide/overlays/clearslide-platform-api-swagger-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/clearslide-platform-api-swagger-overlay.yaml
- group: operate
  href: https://artifacts.apis.io/clearslide/rate-limits/clearslide-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/clearslide-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/clearslide/plans/clearslide-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/clearslide-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/clearslide/components/clearslide-components.yml
  title: ''
  type: Components
  url: components/clearslide-components.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ClearSlide
- group: commercial
  title: ''
  type: Pricing
  url: https://www.clearslide.com/pricing/
created: '2026-07-17'
description: ClearSlide is a sales engagement platform, now part of Bigtincan, that unifies content management, communications (email, web conferencing, screen share), and real-time engagement analytics so sales teams can make every buyer interaction count. Its public Platform API lets customers and partners programmatically list presentations, create trackable links, retrieve engagement insights, manage users (including SCIM provisioning), upload content to Amazon S3, and reserve and manage scheduled meetings. The API uses OAuth 2.0 and is documented on a public ReadMe developer portal at developer.clearslide.com. ClearSlide was originally an a16z-backed company and is profiled here in the API Evangelist network.
finops:
- has_sources: true
  method: derived
  name: Clearslide Finops
  primary_unit: ''
  service_category: ''
  slug: clearslide-finops
  template: true
image: https://www.clearslide.com/wp-content/themes/clearslide/images/logo.svg
layout: provider
modified: '2026-08-13'
name: ClearSlide
nav: Providers
network: true
overview: 'ClearSlide publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Insights API, Links API, Meetings API, and 4 more. Tagged areas include Company, Sales Engagement, Sales Enablement, Content Management, and Presentations.


  The ClearSlide catalog on APIs.io includes 1 Spectral governance ruleset.


  ClearSlide''s developer surface includes engineering blog, documentation, API reference, getting-started guide, changelog, support, authentication, and 34 more developer resources.'
plans:
- name: Clearslide Plans Pricing
  plan_count: 2
  slug: clearslide-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Clearslide Rate Limits
  slug: clearslide-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: ClearSlide API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: clearslide-rules
scopes:
- name: Clearslide Scopes
  scope_count: 2
  slug: clearslide-scopes
  summary_line: 2 scopes · authorizationCode/refreshToken
score:
  band: developing
  composite: 51.4
  coverage:
    artifact_dirs: 35
    catalog_earned: 50.8
    catalog_earned_first_party: 8.0
    catalog_gap: 64.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.2
  facets:
    access_clarity: 48.7
    contract_governance: 35.6
    contract_quality: 46.5
    developer_ergonomics: 58.9
    discoverability: 74.1
    operational_transparency: 31.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 49.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/clearslide/clearslide-2026-07-25T205547.png
security:
- kind: authentication
  name: Clearslide Authentication
  slug: clearslide-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Clearslide Domain Security
  slug: clearslide-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Clearslide Vulnerability Disclosure
  slug: clearslide-vulnerability-disclosure
  summary_line: contact published
skill_count: 2
skills:
- name: share-and-track
  slug: clearslide-share-and-track
- name: upload-content
  slug: clearslide-upload-content
slug: clearslide
tags:
- Company
- Sales Engagement
- Sales Enablement
- Content Management
- Presentations
- Analytics
- Meetings
- CRM
- Authentication
- SCIM
website: https://www.clearslide.com/
---
