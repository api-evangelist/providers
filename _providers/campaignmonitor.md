---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
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
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.2
  scored_at: '2026-11-06'
api_count: 3
apis:
- description: REST API for managing email campaigns, subscriber lists, transactional emails, segments, journeys, templates, and campaign performance analytics.
  name: Campaign Monitor API
  slug: campaign-monitor-api
- description: Legacy ASP.NET SOAP web service still served at api.createsend.com/api/api.asmx, the same host as the REST v3.3 API. Its WSDL (targetNamespace http://api.createsend.com/api/) declares 50 SOAP operatio
  name: Campaign Monitor SOAP API (legacy createsend)
  slug: createsend-soap-api
- baseURL: https://api.createsend.com
  baseurl_source: declared
  description: 'Campaign Monitor API as documented publicly: 6 operations. Contract generated from the documentation by API Evangelist (2026-10-21); not the provider''s own document.'
  name: Campaign Monitor API
  slug: campaignmonitor-api
artifact_total: 19
asyncapis:
- description: ''
  name: Campaignmonitor Webhooks
  slug: campaignmonitor-webhooks
common:
- group: design
  href: https://artifacts.apis.io/campaignmonitor/rules/campaignmonitor-rules.yml
  title: ''
  type: Spectral
  url: rules/campaignmonitor-rules.yml
- group: design
  href: https://artifacts.apis.io/campaignmonitor/json-ld/campaignmonitor-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/campaignmonitor-context.jsonld
- group: design
  href: https://artifacts.apis.io/campaignmonitor/vocabulary/campaignmonitor-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/campaignmonitor-vocabulary.yml
- group: operate
  href: https://artifacts.apis.io/campaignmonitor/lifecycle/campaignmonitor-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/campaignmonitor-lifecycle.yml
- group: other
  href: https://artifacts.apis.io/campaignmonitor/hosts/campaignmonitor-hosts.yml
  title: ''
  type: Hosts
  url: hosts/campaignmonitor-hosts.yml
- group: build
  href: https://artifacts.apis.io/campaignmonitor/integrations/campaignmonitor-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/campaignmonitor-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/campaignmonitor/vendors/campaignmonitor-vendors.yml
  title: ''
  type: Vendors
  url: vendors/campaignmonitor-vendors.yml
- group: auth
  href: https://artifacts.apis.io/campaignmonitor/security/campaignmonitor-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/campaignmonitor-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/campaignmonitor/security/campaignmonitor-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/campaignmonitor-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/campaignmonitor/security/campaignmonitor-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/campaignmonitor-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.campaignmonitor.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.campaignmonitor.com/api/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/campaignmonitor
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/campaign-monitor
- group: company
  title: ''
  type: Blog
  url: https://www.campaignmonitor.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.campaignmonitor.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.campaignmonitor.com/
- group: other
  title: ''
  type: X
  url: https://x.com/campaignmonitor
- group: commercial
  href: https://artifacts.apis.io/campaignmonitor/plans/campaignmonitor-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/campaignmonitor-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/campaignmonitor/rate-limits/campaignmonitor-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/campaignmonitor-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/campaignmonitor/finops/campaignmonitor-finops.yml
  title: ''
  type: FinOps
  url: finops/campaignmonitor-finops.yml
- group: company
  href: https://artifacts.apis.io/campaignmonitor/blogs/blogs.json
  title: ''
  type: BlogPosts
  url: blogs/blogs.json
- group: design
  href: https://artifacts.apis.io/campaignmonitor/json-ld/campaignmonitor-context.jsonld
  title: ''
  type: JSONLDContext
  url: json-ld/campaignmonitor-context.jsonld
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.campaignmonitor.com/api/
- group: docs
  title: ''
  type: APIReference
  url: https://www.campaignmonitor.com/api/v3-3/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.campaignmonitor.com/api/v3-3/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://help.campaignmonitor.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.campaignmonitor.com/signup/
- group: start
  title: ''
  type: Login
  url: https://login.createsend.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.campaignmonitor.com/policies/#terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.campaignmonitor.com/policies/#privacy-policy
- group: build
  href: https://artifacts.apis.io/campaignmonitor/packages/campaignmonitor-packages.yml
  title: ''
  type: Packages
  url: packages/campaignmonitor-packages.yml
- group: build
  href: https://artifacts.apis.io/campaignmonitor/packages/campaignmonitor-packages.yml
  title: ''
  type: SDKs
  url: packages/campaignmonitor-packages.yml
- group: agent
  href: https://artifacts.apis.io/campaignmonitor/well-known/campaignmonitor-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/campaignmonitor-well-known.yml
- group: auth
  href: https://artifacts.apis.io/campaignmonitor/well-known/campaignmonitor-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/campaignmonitor-security.txt
- group: auth
  href: https://artifacts.apis.io/campaignmonitor/security/campaignmonitor-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/campaignmonitor-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/campaignmonitor/conformance/campaignmonitor-conformance.yml
  title: ''
  type: Compliance
  url: conformance/campaignmonitor-conformance.yml
- group: design
  href: https://artifacts.apis.io/campaignmonitor/conformance/campaignmonitor-conformance.yml
  title: ''
  type: Conformance
  url: conformance/campaignmonitor-conformance.yml
- group: auth
  href: https://artifacts.apis.io/campaignmonitor/authentication/campaignmonitor-authentication.yml
  title: ''
  type: Authentication
  url: authentication/campaignmonitor-authentication.yml
- group: auth
  href: https://artifacts.apis.io/campaignmonitor/scopes/campaignmonitor-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/campaignmonitor-scopes.yml
- group: design
  href: https://artifacts.apis.io/campaignmonitor/conventions/campaignmonitor-conventions.yml
  title: ''
  type: Conventions
  url: conventions/campaignmonitor-conventions.yml
- group: design
  href: https://artifacts.apis.io/campaignmonitor/errors/campaignmonitor-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/campaignmonitor-error-codes.yml
- group: design
  href: https://artifacts.apis.io/campaignmonitor/lifecycle/campaignmonitor-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/campaignmonitor-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/campaignmonitor/changelog/campaignmonitor-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/campaignmonitor-changelog.yml
- group: design
  href: https://artifacts.apis.io/campaignmonitor/data-model/campaignmonitor-data-model.yml
  title: ''
  type: DataModel
  url: data-model/campaignmonitor-data-model.yml
- group: design
  href: https://artifacts.apis.io/campaignmonitor/asyncapi/campaignmonitor-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/campaignmonitor-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/campaignmonitor/mcp/campaignmonitor-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/campaignmonitor-mcp.yml
created: '2026-06-13'
description: Campaign Monitor, a Marigold brand, is an email marketing platform for marketers and agencies. Its REST API — served under the original createsend name at api.createsend.com/api/v3.3 — manages clients, subscriber lists, subscribers and custom fields, segments, campaigns, HTML templates, automated journeys, authenticated sending domains and transactional email, and returns per-recipient reporting for opens, clicks, bounces, unsubscribes and spam complaints. Authentication is OAuth 2.0 with twelve coarse permissions, or an API key over HTTP Basic. Per-list webhooks push Subscribe, Update and Deactivate events. Campaign Monitor publishes no OpenAPI, no AsyncAPI and no MCP server; the contract is HTML reference documentation plus seven official client libraries.
finops:
- has_sources: true
  method: derived
  name: Campaignmonitor Finops
  primary_unit: subscription
  service_category: ''
  slug: campaignmonitor-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/campaignmonitor.png
json_schemas:
- name: GetApiApiidClientsJsonResponse
  property_count: 2
  slug: campaignmonitor-get-api-apiid-clients-json-response
- name: GetApiV32ClientsXmlResponse
  property_count: 2
  slug: campaignmonitor-get-api-v32-clients-xml-response
- name: PostApiV32ClientsJsonRequest
  property_count: 5
  slug: campaignmonitor-post-api-v32-clients-json-request
- name: PostApiV32ClientsXmlRequest
  property_count: 5
  slug: campaignmonitor-post-api-v32-clients-xml-request
- name: PostDeactivateRequest
  property_count: 2
  slug: campaignmonitor-post-deactivate-request
jsonld:
- class_count: 18
  name: Campaignmonitor Context
  property_count: 1
  slug: campaignmonitor-context
layout: provider
modified: '2026-10-21'
name: Campaign Monitor
nav: Providers
network: true
overview: 'Campaign Monitor is listed with 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Email Marketing, Campaigns, Subscribers, Transactional Email, and Segments.


  The Campaign Monitor catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Campaign Monitor''s developer surface includes documentation, engineering blog, pricing, API reference, getting-started guide, support, signup flow, and 40 more developer resources.'
plans:
- name: Campaignmonitor Plans Pricing
  plan_count: 5
  slug: campaignmonitor-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 1
  name: Campaignmonitor Rate Limits
  slug: campaignmonitor-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Campaign Monitor API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: campaignmonitor-rules
scopes:
- name: Campaignmonitor Scopes
  scope_count: 12
  slug: campaignmonitor-scopes
  summary_line: 12 scopes
score:
  band: strong
  composite: 65.3
  coverage:
    artifact_dirs: 31
    catalog_earned: 85.8
    catalog_earned_first_party: 20.0
    catalog_gap: 29.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 100.0
    contract_governance: 35.6
    contract_quality: 31.8
    developer_ergonomics: 60.7
    discoverability: 71.4
    operational_transparency: 84.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 66.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 44.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/campaignmonitor/campaignmonitor-2026-06-20T173912.png
security:
- kind: authentication
  name: Campaignmonitor Authentication
  slug: campaignmonitor-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Campaignmonitor Domain Security
  slug: campaignmonitor-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Campaignmonitor Vulnerability Disclosure
  slug: campaignmonitor-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
- kind: trust-center
  name: Campaignmonitor Trust Center
  slug: campaignmonitor-trust-center
  summary_line: SOC 2, GDPR
slug: campaignmonitor
tags:
- Email Marketing
- Campaigns
- Subscribers
- Transactional Email
- Segments
- Newsletters
- Automation
- Marketing Automation
- Webhook
- Email Deliverability
- Marketing
website: https://www.campaignmonitor.com/
---
