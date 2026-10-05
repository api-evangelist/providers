---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 68.0
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Jobspipe Agentic Access
  operation_count: 33
  slug: jobspipe-agentic-access
  summary_line: 33 operations · 11 acting
api_count: 1
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
artifact_total: 27
asyncapis:
- description: ''
  name: Jobspipe Webhooks
  slug: jobspipe-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/jobspipe/refs/heads/main/agentic-access/jobspipe-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/jobspipe-agentic-access.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/jobspipe/refs/heads/main/rate-limits/jobspipe-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/jobspipe-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/jobspipe/refs/heads/main/plans/jobspipe-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/jobspipe-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/jobspipe/refs/heads/main/rules/jobspipe-rules.yml
  title: ''
  type: Spectral
  url: rules/jobspipe-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/jobspipe/refs/heads/main/json-ld/jobspipe-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/jobspipe-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/jobspipe/refs/heads/main/vocabulary/jobspipe-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/jobspipe-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/jobspipe/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/jobspipe/refs/heads/main/asyncapi/jobspipe-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/jobspipe-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/jobspipe/refs/heads/main/data-model/jobspipe-data-model.yml
  title: ''
  type: DataModel
  url: data-model/jobspipe-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/jobspipe/refs/heads/main/conventions/jobspipe-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/jobspipe-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/jobspipe/refs/heads/main/conventions/jobspipe-conventions.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/jobspipe/refs/heads/main/authentication/jobspipe-authentication.yml
  title: ''
  type: Authentication
  url: authentication/jobspipe-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/jobspipe/refs/heads/main/errors/jobspipe-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/jobspipe-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/jobspipe/refs/heads/main/conformance/jobspipe-conformance.yml
  title: ''
  type: Conformance
  url: conformance/jobspipe-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/jobspipe/refs/heads/main/llms/jobspipe-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/jobspipe-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/jobspipe/refs/heads/main/a2a/jobspipe-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/jobspipe-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/jobspipe/refs/heads/main/mcp/jobspipe-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/jobspipe-mcp.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/jobspipe/refs/heads/main/well-known/jobspipe-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/jobspipe-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/jobspipe/refs/heads/main/well-known/jobspipe-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/jobspipe-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/jobspipe/refs/heads/main/hosts/jobspipe-hosts.yml
  title: ''
  type: Hosts
  url: hosts/jobspipe-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/jobspipe/refs/heads/main/packages/jobspipe-packages.yml
  title: ''
  type: SDKs
  url: packages/jobspipe-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/jobspipe/refs/heads/main/packages/jobspipe-packages.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/jobspipe/refs/heads/main/security/jobspipe-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/jobspipe-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/jobspipe/refs/heads/main/security/jobspipe-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/jobspipe-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/jobspipe/refs/heads/main/security/jobspipe-domain-security.yml
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
- description: Remote MCP server at jobspipe.dev requiring an API key.
  name: JobsPipe MCP Server
  slug: jobspipe-mcp-yml
modified: '2026-10-02'
name: JobsPipe
nav: Providers
network: true
overview: 'JobsPipe publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Account API, Billing API, Companies API, and 7 more. Tagged areas include Company, Job, Data, and Hiring.


  The JobsPipe catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  JobsPipe''s developer surface includes authentication, sandbox, changelog, documentation, API reference, getting-started guide, support, and 35 more developer resources.'
plans:
- name: Jobspipe Plans Pricing
  plan_count: 6
  slug: jobspipe-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 3
  name: Jobspipe Rate Limits
  slug: jobspipe-rate-limits
rules:
- effective_rule_count: 57
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
  composite: 73.9
  coverage:
    artifact_dirs: 25
    catalog_earned: 81.8
    catalog_earned_first_party: 24.0
    catalog_gap: 33.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 92.1
    contract_governance: 22.0
    contract_quality: 72.0
    developer_ergonomics: 73.2
    discoverability: 66.7
    operational_transparency: 86.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Jobspipe Authentication
  slug: jobspipe-authentication
  summary_line: 2 schemes
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
slug: jobspipe
tags:
- Company
- Job
- Data
- Hiring
website: https://jobspipe.dev
---
