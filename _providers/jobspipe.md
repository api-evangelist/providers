---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: self
    auth_clarity: served
    consent_identity: true
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 80.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Jobspipe Agentic Access
  operation_count: 33
  slug: jobspipe-agentic-access
  summary_line: 33 operations · 11 acting
api_count: 3
apis:
- baseURL: https://api.jobspipe.dev
  baseurl_source: declared
  description: The Account API from JobsPipe — 1 operation(s) for account.
  name: JobsPipe Account API
  slug: jobspipe-account-api
- baseURL: https://api.jobspipe.dev
  baseurl_source: declared
  description: The Billing API from JobsPipe — 1 operation(s) for billing.
  name: JobsPipe Billing API
  slug: jobspipe-billing-api
- baseURL: https://api.jobspipe.dev
  baseurl_source: declared
  description: The Companies API from JobsPipe — 3 operation(s) for companies.
  name: JobsPipe Companies API
  slug: jobspipe-companies-api
- baseURL: https://api.jobspipe.dev
  baseurl_source: declared
  description: The Jobs API from JobsPipe — 2 operation(s) for jobs.
  name: JobsPipe Jobs API
  slug: jobspipe-jobs-api
- baseURL: https://api.jobspipe.dev
  baseurl_source: declared
  description: The JobsPipe API API from JobsPipe — 0 operation(s) for jobspipe api.
  name: JobsPipe JobsPipe API
  slug: jobspipe-jobspipe-api-api
- baseURL: https://api.jobspipe.dev
  baseurl_source: declared
  description: The Labour Market Insights API from JobsPipe — 10 operation(s) for labour market insights.
  name: JobsPipe Labour Market Insights API
  slug: jobspipe-labour-market-insights-api
- baseURL: https://api.jobspipe.dev
  baseurl_source: declared
  description: The Monitors API from JobsPipe — 4 operation(s) for monitors.
  name: JobsPipe Monitors API
  slug: jobspipe-monitors-api
- baseURL: https://api.jobspipe.dev
  baseurl_source: declared
  description: The Sandbox API from JobsPipe — 4 operation(s) for sandbox.
  name: JobsPipe Sandbox API
  slug: jobspipe-sandbox-api
- baseURL: https://api.jobspipe.dev
  baseurl_source: declared
  description: The Stack API from JobsPipe — 1 operation(s) for stack.
  name: JobsPipe Stack API
  slug: jobspipe-stack-api
- baseURL: https://api.jobspipe.dev
  baseurl_source: declared
  description: The Technologies API from JobsPipe — 3 operation(s) for technologies.
  name: JobsPipe Technologies API
  slug: jobspipe-technologies-api
- baseURL: https://api.jobspipe.dev
  baseurl_source: declared
  description: Find work emails, personal emails and phone numbers for people.
  name: JobsPipe Contacts API
  slug: jobspipe-contacts-api
- baseURL: https://api.jobspipe.dev
  baseurl_source: declared
  description: US WARN Act layoff and closure notices, with the company each names.
  name: JobsPipe Layoffs API
  slug: jobspipe-layoffs-api
- baseURL: https://api.jobspipe.dev
  baseurl_source: declared
  description: Read a board or search a source live, without waiting for a crawl.
  name: JobsPipe Live API
  slug: jobspipe-live-api
artifact_total: 35
asyncapis:
- description: ''
  name: Jobspipe Webhooks
  slug: jobspipe-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/jobspipe/finops/jobspipe-finops.yml
  title: ''
  type: FinOps
  url: finops/jobspipe-finops.yml
- group: operate
  href: https://artifacts.apis.io/jobspipe/changelog/jobspipe-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/jobspipe-changelog.yml
- group: start
  href: https://artifacts.apis.io/jobspipe/sandbox/jobspipe-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/jobspipe-sandbox.yml
- group: build
  href: https://artifacts.apis.io/jobspipe/integrations/jobspipe-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/jobspipe-integration-edges.yml
- group: docs
  title: ''
  type: OpenAPI
  url: https://jobspipe.dev/openapi.json
- group: design
  title: ''
  type: Spectral
  url: https://jobspipe.dev/governance/spectral.yaml
- group: design
  title: ''
  type: Vocabulary
  url: https://jobspipe.dev/governance/vocabulary.yaml
- group: design
  title: ''
  type: Conformance
  url: https://jobspipe.dev/governance/conformance.yaml
- group: other
  title: ''
  type: Overlay
  url: https://jobspipe.dev/governance/overlay.json
- group: agent
  title: ''
  type: AgenticAccess
  url: https://jobspipe.dev/governance/agentic-access.json
- group: other
  title: ''
  type: Governance
  url: https://jobspipe.dev/governance
- group: operate
  title: ''
  type: Deprecation
  url: https://jobspipe.dev/trust/compliance#api-versioning-and-deprecation
- group: operate
  title: ''
  type: SupportLifetime
  url: https://jobspipe.dev/trust/compliance#support-lifetime
- group: design
  title: ''
  type: Idempotency
  url: https://docs.jobspipe.dev/api-reference/errors
- group: design
  title: ''
  type: ErrorCatalog
  url: https://docs.jobspipe.dev/api-reference/errors
- group: design
  title: ''
  type: Pagination
  url: https://docs.jobspipe.dev/api-reference/pagination
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.jobspipe.dev/usage/rate-limits
- group: design
  title: ''
  type: Webhooks
  url: https://docs.jobspipe.dev/api-reference/webhooks
- group: design
  title: ''
  type: DataModel
  url: https://docs.jobspipe.dev/api-reference/job-schema
- group: auth
  title: ''
  type: Authentication
  url: https://docs.jobspipe.dev/authentication
- group: auth
  title: ''
  type: OAuthScopes
  url: https://api.jobspipe.dev/.well-known/oauth-protected-resource
- group: design
  title: ''
  type: ProtectedResourceMetadata
  url: https://api.jobspipe.dev/.well-known/oauth-protected-resource
- group: design
  title: ''
  type: AuthorizationServerMetadata
  url: https://api.jobspipe.dev/.well-known/oauth-authorization-server
- group: other
  title: ''
  type: OpenIDConfiguration
  url: https://jobspipe.dev/.well-known/openid-configuration
- group: other
  title: ''
  type: APICatalog
  url: https://jobspipe.dev/.well-known/api-catalog
- group: agent
  title: ''
  type: WellKnown
  url: https://jobspipe.dev/.well-known/api-catalog
- group: auth
  title: ''
  type: SecurityTxt
  url: https://jobspipe.dev/.well-known/security.txt
- group: other
  title: ''
  type: HTTPMessageSignatures
  url: https://jobspipe.dev/.well-known/http-message-signatures-directory
- group: other
  title: ''
  type: ContentSignal
  url: https://jobspipe.dev/robots.txt
- group: agent
  title: ''
  type: AgenticCommerce
  url: https://jobspipe.dev/.well-known/ucp.json
- group: agent
  title: ''
  type: MCPServer
  url: https://mcp.jobspipe.dev/mcp
- group: agent
  title: ''
  type: MCPServerCard
  url: https://jobspipe.dev/.well-known/mcp/server-card.json
- group: other
  title: ''
  type: AgentCard
  url: https://jobspipe.dev/.well-known/agent-card.json
- group: agent
  title: ''
  type: AgentSkill
  url: https://jobspipe.dev/.well-known/agent-skills/index.json
- group: agent
  title: ''
  type: LLMsTxt
  url: https://jobspipe.dev/llms.txt
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.jobspipe.dev/quickstart
- group: docs
  title: ''
  type: APIReference
  url: https://docs.jobspipe.dev/api-reference/jobs-search
- group: build
  title: ''
  type: SDK
  url: https://pypi.org/project/jobspipe/
- group: build
  title: ''
  type: SDK
  url: https://pkg.go.dev/github.com/jobspipe/jobspipe-go
- group: build
  title: ''
  type: CLI
  url: https://www.npmjs.com/package/jobspipe-cli
- group: build
  title: ''
  type: Examples
  url: https://github.com/jobspipe/job-board-starter
- group: commercial
  title: ''
  type: Pricing
  url: https://jobspipe.dev/pricing
- group: operate
  title: ''
  type: Support
  url: https://jobspipe.dev/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://jobspipe.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://jobspipe.dev/privacy
- group: other
  title: ''
  type: AcceptableUse
  url: https://jobspipe.dev/acceptable-use
- group: auth
  title: ''
  type: Compliance
  url: https://jobspipe.dev/trust/compliance
- group: commercial
  title: ''
  type: DataProcessingAgreement
  url: https://jobspipe.dev/dpa
- group: other
  title: ''
  type: Subprocessors
  url: https://jobspipe.dev/dpa#sub-processors
- group: operate
  title: ''
  type: IncidentNotification
  url: https://jobspipe.dev/dpa#breach-notification
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://jobspipe.dev/trust/privacy-compliance
- group: other
  title: ''
  type: DataResidency
  url: https://jobspipe.dev/trust/compliance#data-residency
- group: commercial
  title: ''
  type: GlobalPrivacyControl
  url: https://jobspipe.dev/.well-known/gpc.json
- group: design
  title: ''
  type: AccessibilityConformance
  url: https://jobspipe.dev/trust/compliance#accessibility
- group: other
  title: ''
  type: AgeAssurance
  url: https://jobspipe.dev/privacy#children
- group: other
  title: ''
  type: NoticeAndAction
  url: https://jobspipe.dev/trust/abuse
- group: other
  title: ''
  type: ExitAssistance
  url: https://jobspipe.dev/trust/compliance#switching-and-exit
- group: other
  title: ''
  type: SBOM
  url: https://jobspipe.dev/sbom.json
- group: other
  href: https://artifacts.apis.io/jobspipe/capabilities/jobspipe-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/jobspipe-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/jobspipe/agentic-access/jobspipe-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/jobspipe-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/jobspipe/rate-limits/jobspipe-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/jobspipe-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/jobspipe/plans/jobspipe-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/jobspipe-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/jobspipe/rules/jobspipe-rules.yml
  title: ''
  type: Spectral
  url: rules/jobspipe-rules.yml
- group: design
  href: https://artifacts.apis.io/jobspipe/json-ld/jobspipe-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/jobspipe-context.jsonld
- group: design
  href: https://artifacts.apis.io/jobspipe/vocabulary/jobspipe-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/jobspipe-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/jobspipe/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/jobspipe/asyncapi/jobspipe-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/jobspipe-webhooks.yml
- group: design
  href: https://artifacts.apis.io/jobspipe/data-model/jobspipe-data-model.yml
  title: ''
  type: DataModel
  url: data-model/jobspipe-data-model.yml
- group: design
  href: https://artifacts.apis.io/jobspipe/conventions/jobspipe-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/jobspipe-conventions.yml
- group: design
  href: https://artifacts.apis.io/jobspipe/conventions/jobspipe-conventions.yml
  title: ''
  type: Conventions
  url: conventions/jobspipe-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://jobspipe.dev/trust
- group: auth
  title: ''
  type: Security
  url: https://jobspipe.dev/trust/security
- group: auth
  href: https://artifacts.apis.io/jobspipe/authentication/jobspipe-authentication.yml
  title: ''
  type: Authentication
  url: authentication/jobspipe-authentication.yml
- group: design
  href: https://artifacts.apis.io/jobspipe/errors/jobspipe-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/jobspipe-problem-types.yml
- group: design
  href: https://artifacts.apis.io/jobspipe/conformance/jobspipe-conformance.yml
  title: ''
  type: Conformance
  url: conformance/jobspipe-conformance.yml
- group: agent
  href: https://artifacts.apis.io/jobspipe/llms/jobspipe-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/jobspipe-llms.txt
- group: other
  href: https://artifacts.apis.io/jobspipe/a2a/jobspipe-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/jobspipe-a2a.yml
- group: agent
  href: https://artifacts.apis.io/jobspipe/mcp/jobspipe-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/jobspipe-mcp.yml
- group: auth
  href: https://artifacts.apis.io/jobspipe/well-known/jobspipe-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/jobspipe-security.txt
- group: agent
  href: https://artifacts.apis.io/jobspipe/well-known/jobspipe-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/jobspipe-well-known.yml
- group: other
  href: https://artifacts.apis.io/jobspipe/hosts/jobspipe-hosts.yml
  title: ''
  type: Hosts
  url: hosts/jobspipe-hosts.yml
- group: build
  href: https://artifacts.apis.io/jobspipe/packages/jobspipe-packages.yml
  title: ''
  type: SDKs
  url: packages/jobspipe-packages.yml
- group: build
  href: https://artifacts.apis.io/jobspipe/packages/jobspipe-packages.yml
  title: ''
  type: Packages
  url: packages/jobspipe-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.jobspipe.dev
- group: start
  title: ''
  type: Sandbox
  url: https://jobspipe.dev/sandbox
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jobspipe
- group: start
  title: ''
  type: DeveloperPortal
  url: https://jobspipe.dev/developers
- group: operate
  title: ''
  type: ChangeLog
  url: https://jobspipe.dev/changelog
- group: auth
  href: https://artifacts.apis.io/jobspipe/security/jobspipe-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/jobspipe-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/jobspipe/security/jobspipe-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/jobspipe-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/jobspipe/security/jobspipe-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/jobspipe-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://jobspipe.dev
- group: docs
  title: ''
  type: Documentation
  url: https://docs.jobspipe.dev
- group: docs
  title: ''
  type: APIReference
  url: https://api.jobspipe.dev/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://jobspipe.dev/jobs-api.md
- group: operate
  title: ''
  type: Support
  url: https://jobspipe.dev/contact.md
- group: company
  title: ''
  type: Blog
  url: https://jobspipe.dev/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://jobspipe.dev/pricing.md
- group: start
  title: ''
  type: SignUp
  url: https://jobspipe.dev/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://jobspipe.dev/terms.md
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://jobspipe.dev/privacy.md
created: '2026-10-02'
description: JobsPipe provides a universal jobs API and hiring-signal platform that aggregates and normalizes job postings from over 30 applicant tracking systems and job boards, including LinkedIn, Indeed, Workday, Greenhouse, Lever, and Ashby. It offers real-time webhooks, AI-parsed salary ranges, and historical data, enabling AI agents and developers to integrate comprehensive job market data into their applications.
finops:
- has_sources: true
  method: derived
  name: Jobspipe Finops
  primary_unit: credits
  service_category: ''
  slug: jobspipe-finops
  template: false
image: https://jobspipe.dev/opengraph-image?b21373484c707b8f
json_schemas:
- name: AgenticSearchResponse
  property_count: 2
  slug: jobspipe-agentic-search-response
- name: CompanyObject
  property_count: 11
  slug: jobspipe-company-object
- name: CompanySearchRequest
  property_count: 18
  slug: jobspipe-company-search-request
- name: JobSearchRequest
  property_count: 57
  slug: jobspipe-job-search-request
- name: JobSearchResponse
  property_count: 2
  slug: jobspipe-job-search-response
- name: TechnologyDetailResponse
  property_count: 12
  slug: jobspipe-technology-detail-response
jsonld:
- class_count: 33
  name: Jobspipe Context
  property_count: 238
  slug: jobspipe-context
layout: provider
mcp_servers:
- description: ''
  name: JobsPipe MCP Server
  slug: mcp
- description: Remote MCP server at jobspipe.dev.
  name: JobsPipe MCP Server
  slug: jobspipe-mcp-yml
modified: '2026-10-02'
name: JobsPipe
nav: Providers
network: true
overview: 'JobsPipe publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Billing API, Companies API, and 10 more. Tagged areas include Company, Job, Data, Hiring, and JobsAPI.


  The JobsPipe catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  JobsPipe''s developer surface includes changelog, sandbox, authentication, getting-started guide, API reference, SDKs, CLI, and 94 more developer resources.'
plans:
- name: Jobspipe Plans Pricing
  plan_count: 3
  slug: jobspipe-plans-pricing
- name: Jobspipe Price Estimates
  plan_count: 0
  slug: jobspipe-price-estimates
random_paper: 20
rate_limits:
- limit_count: 7
  name: Jobspipe Rate Limits
  slug: jobspipe-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: JobsPipe API Rules
  rule_count: 16
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 2
  slug: jobspipe-rules
score:
  band: exemplar
  composite: 84.9
  coverage:
    artifact_dirs: 33
    catalog_earned: 96.1
    catalog_earned_first_party: 24.0
    catalog_gap: 18.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -15.1
  facets:
    access_clarity: 73.7
    contract_governance: 32.2
    contract_quality: 77.9
    developer_ergonomics: 53.3
    discoverability: 90.0
    operational_transparency: 63.2
  previous_composite: 100.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 17.4
      total: 23
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 79.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 100.0
screenshot: https://apis.io/screenshots/jobspipe/jobspipe-2026-10-11T105939.png
security:
- kind: authentication
  name: Jobspipe Authentication
  slug: jobspipe-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Jobspipe Domain Security
  slug: jobspipe-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Jobspipe Vulnerability Disclosure
  slug: jobspipe-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Jobspipe Trust Center
  slug: jobspipe-trust-center
  summary_line: GDPR
skill_count: 2
skills:
- name: jobspipe-companies-tech-stack
  slug: jobspipe-companies-tech-stack
- name: jobspipe-labour-market-insights
  slug: jobspipe-labour-market-insights
slug: jobspipe
tags:
- Company
- Job
- Data
- Hiring
- JobsAPI
website: https://jobspipe.dev
---
