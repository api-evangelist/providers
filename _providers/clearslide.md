---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 29.7
  scored_at: '2026-09-19'
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
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.clearslide.com/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.clearslide.com/legal/privacy/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/clearslide/refs/heads/main/llms/clearslide-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/clearslide-llms.txt
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/clearslide/refs/heads/main/openapi/_original/clearslide-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/clearslide-openapi.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/clearslide/refs/heads/main/overlays/clearslide-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/clearslide-openapi-overlay.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clearslide/refs/heads/main/authentication/clearslide-authentication.yml
  title: ''
  type: Authentication
  url: authentication/clearslide-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clearslide/refs/heads/main/scopes/clearslide-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/clearslide-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clearslide/refs/heads/main/conventions/clearslide-conventions.yml
  title: ''
  type: Conventions
  url: conventions/clearslide-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clearslide/refs/heads/main/lifecycle/clearslide-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/clearslide-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clearslide/refs/heads/main/conformance/clearslide-conformance.yml
  title: ''
  type: Conformance
  url: conformance/clearslide-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.clearslide.com/about/security/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clearslide/refs/heads/main/security/clearslide-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/clearslide-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.clearslide.com/about/security/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clearslide/refs/heads/main/security/clearslide-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clearslide-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/clearslide/refs/heads/main/well-known/clearslide-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/clearslide-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/clearslide/refs/heads/main/mcp/clearslide-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/clearslide-mcp.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clearslide/refs/heads/main/data-model/clearslide-data-model.yml
  title: ''
  type: DataModel
  url: data-model/clearslide-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/clearslide/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/clearslide/refs/heads/main/openapi/_original/clearslide-platform-api-swagger.json
  title: ''
  type: OpenAPI
  url: openapi/_original/clearslide-platform-api-swagger.json
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/clearslide/refs/heads/main/overlays/clearslide-platform-api-swagger-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/clearslide-platform-api-swagger-overlay.yaml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/clearslide/refs/heads/main/packages/clearslide-packages.yml
  title: ''
  type: Packages
  url: packages/clearslide-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clearslide/refs/heads/main/errors/clearslide-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/clearslide-problem-types.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/clearslide/refs/heads/main/rate-limits/clearslide-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/clearslide-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/clearslide/refs/heads/main/plans/clearslide-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/clearslide-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clearslide/refs/heads/main/components/clearslide-components.yml
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
- group: start
  title: ''
  type: SignUp
  url: https://www.clearslide.com/freetrial
- group: company
  title: ''
  type: Blog
  url: https://www.clearslide.com/blog/
created: '2026-07-17'
description: ClearSlide is a sales engagement platform, now part of Bigtincan, that unifies content management, communications (email, web conferencing, screen share), and real-time engagement analytics so sales teams can make every buyer interaction count. Its public Platform API lets customers and partners programmatically list presentations, create trackable links, retrieve engagement insights, manage users (including SCIM provisioning), upload content to Amazon S3, and reserve and manage scheduled meetings. The API uses OAuth 2.0 and is documented on a public ReadMe developer portal at developer.clearslide.com. ClearSlide was originally an a16z-backed company and is profiled here in the API Evangelist network.
image: https://www.clearslide.com/wp-content/themes/clearslide/images/logo.svg
layout: provider
modified: '2026-08-13'
name: ClearSlide
nav: Providers
network: true
overview: 'ClearSlide publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Insights API, Links API, Meetings API, and 3 more. Tagged areas include Company, Sales Engagement, Sales Enablement, Content Management, and Presentations.


  ClearSlide''s developer surface includes documentation, API reference, getting-started guide, changelog, support, authentication, pricing, and 31 more developer resources.'
plans:
- name: Clearslide Plans Pricing
  plan_count: 2
  slug: clearslide-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Clearslide Rate Limits
  slug: clearslide-rate-limits
scopes:
- name: Clearslide Scopes
  scope_count: 2
  slug: clearslide-scopes
  summary_line: 2 scopes · authorizationCode/refreshToken
score:
  band: developing
  composite: 47.0
  coverage:
    artifact_dirs: 27
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 73.7
    contract_governance: 18.2
    contract_quality: 51.7
    developer_ergonomics: 37.5
    discoverability: 75.9
    operational_transparency: 21.1
  previous_composite: 47.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-19'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/clearslide/refs/heads/main/screenshots/clearslide-2026-07-25T205547.png
security:
- kind: authentication
  name: Clearslide Authentication
  slug: clearslide-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Clearslide Domain Security
  slug: clearslide-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Clearslide Vulnerability Disclosure
  slug: clearslide-vulnerability-disclosure
  summary_line: contact published
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
