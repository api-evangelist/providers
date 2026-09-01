---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 62.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Debounce Agentic Access
  operation_count: 7
  slug: debounce-agentic-access
  summary_line: 7 operations
api_count: 3
apis:
- description: Real-time single email address validation. Returns a deliverability result (Safe to Send, Risky, Invalid, Unknown), a result code, role-account and free-provider flags, a did-you-mean typo suggestion,
  name: DeBounce Validation API
  slug: debounce-validation-api
- description: Asynchronous bulk email list validation on bulk.debounce.io. Submit the URL of a hosted CSV or TXT list for processing, receive a list_id, then poll the status endpoint for the processing percentage a
  name: DeBounce Bulk API
  slug: debounce-bulk-api
- description: Reverse email lookup / data append. Returns additional contact data associated with an email address. The same enrichment engine is reachable from the single-validation endpoint via the append and pho
  name: DeBounce Data API
  slug: debounce-data-api
- description: Account operations. Returns the remaining credit balance on the account and a dated API usage history for a requested start/end window, so consumers can monitor consumption and top up before hitting t
  name: DeBounce Account API
  slug: debounce-account-api
- description: Free, unauthenticated disposable email detector on disposable.debounce.io. A single GET with an email address or domain returns whether it belongs to a known disposable or temporary email provider, ch
  name: DeBounce Disposable Detector API
  slug: debounce-disposable-api
- description: 'Free company logo lookup service positioned as a drop-in replacement for the deprecated Clearbit Logo API. A GET against logo.debounce.com with a company domain returns a high-quality PNG logo served '
  name: DeBounce Logo API
  slug: debounce-logo-api
artifact_total: 28
collections:
- collection_type: postman
  name: DeBounce Email Validation Account API
  slug: postman-debounce-account-api
- collection_type: postman
  name: DeBounce Email Validation Account Bulk API
  slug: postman-debounce-bulk-api
- collection_type: postman
  name: DeBounce Email Validation Account Data API
  slug: postman-debounce-data-api
- collection_type: postman
  name: DeBounce Email Account Validation API
  slug: postman-debounce-validation-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: DeBounce Email Validation API — Account
  slug: open-debounce-account-api
- collection_type: open
  name: DeBounce Bulk Email Validation API
  slug: open-debounce-bulk-api
- collection_type: open
  name: DeBounce Email Validation API — Data Enrichment
  slug: open-debounce-data-api
- collection_type: open
  name: DeBounce Disposable Email Detector API
  slug: open-debounce-disposable-api
- collection_type: open
  name: DeBounce Email Validation API — Single Validation
  slug: open-debounce-validation-api
common:
- group: company
  title: ''
  type: Website
  url: https://debounce.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.debounce.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.debounce.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.debounce.com/api-reference/endpoint/single-validation
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.debounce.com/
- group: operate
  title: ''
  type: Support
  url: https://help.debounce.com/
- group: company
  title: ''
  type: Blog
  url: https://debounce.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://debounce.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.debounce.com/register
- group: start
  title: ''
  type: Login
  url: https://app.debounce.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://debounce.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://debounce.com/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://debounce.com/gdpr/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.debounce.com/
- group: operate
  title: ''
  type: Roadmap
  url: https://feedback.debounce.com/roadmap
- group: operate
  title: ''
  type: ChangeLog
  url: https://feedback.debounce.com/changelog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/debounceio
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/debounceio
- group: other
  title: ''
  type: X
  url: https://x.com/debounceio
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/debounce/overview
- group: other
  title: ''
  type: AgentCard
  url: a2a/debounce-a2a.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/debounce-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/debounce-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/debounce-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/debounce-well-known.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/debounce-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/debounce-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/debounce-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/debounce-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/debounce-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/debounce-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/debounce-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/debounce-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/debounce-components.yml
- group: build
  title: ''
  type: Packages
  url: packages/debounce-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/debounce-changelog.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/debounce-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/debounce-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/debounce-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/debounce-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/debounce-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/debounce-context.jsonld
- group: company
  title: ''
  type: BlogPosts
  url: blogs/blogs.json
created: '2026-06-12'
description: DeBounce is an email validation and verification REST API that helps developers ensure the deliverability and quality of email addresses at scale. The API supports real-time single email validation, asynchronous bulk list processing, and data enrichment via reverse email lookup. It detects disposable addresses, role-based emails, catch-all domains, syntax errors, and performs MX record and SMTP-level mailbox verification. DeBounce offers pay-as-you-go credit-based pricing with no monthly subscription required, full API access at every tier, and credits that never expire. The surface is split across four hosts — api.debounce.io for validation, enrichment and account operations, bulk.debounce.io for asynchronous list jobs, disposable.debounce.io for the free disposable detector, and logo.debounce.com for the free company logo lookup — and DeBounce publishes OpenAPI 3.1.0, llms.txt, an A2A agent card, an agent skill and a remote MCP server from its developer portal.
examples:
- key_count: 9
  name: Debounce Single Validation Example
  slug: debounce-single-validation-example
finops:
- name: Debounce Finops
  service_category: ''
  slug: debounce-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/debounce.png
json_schemas:
- name: DeBounce Validation Result
  property_count: 3
  slug: debounce-validation-result
jsonld:
- class_count: 14
  name: Debounce Context
  property_count: 32
  slug: debounce-context
layout: provider
mcp_servers:
- description: DeBounce serves two Model Context Protocol endpoints from its own hosts. The developer-portal server is anonymous and answers tools/list live — its three tools are documentation-retrieval tools, not e
  name: DeBounce MCP Server
  slug: debounce-mcp-server
modified: '2026-08-14'
name: DeBounce
nav: Providers
network: true
overview: 'DeBounce publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Validation API, Bulk API, Data API, and 2 more. Tagged areas include Email Validation, Email Verification, Deliverability, Disposable Email Detection, and MX Records.


  The DeBounce catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  DeBounce''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 37 more developer resources.'
plans:
- name: Debounce Plans Pricing
  plan_count: 9
  slug: debounce-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 4
  name: Debounce Rate Limits
  slug: debounce-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: DeBounce API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: debounce-jsonschema-spectral-rules
scopes:
- name: Debounce Scopes
  scope_count: 1
  slug: debounce-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: exemplar
  composite: 69.9
  coverage:
    artifact_dirs: 31
    catalog_gap: 22.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 43.2
    contract_quality: 68.8
    developer_ergonomics: 69.0
    discoverability: 81.5
    governance: 43.2
    operational_transparency: 55.3
  previous_composite: 69.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 5
    mcp: first-party
    skills: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/debounce/refs/heads/main/screenshots/debounce-2026-06-20T175751.png
security:
- kind: authentication
  name: Debounce Authentication
  slug: debounce-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Debounce Domain Security
  slug: debounce-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: debounce
tags:
- Email Validation
- Email Verification
- Deliverability
- Disposable Email Detection
- MX Records
- Bulk Email Validation
- Data Enrichment
- Syntax Validation
- Reverse Email Lookup
- Logo API
website: https://debounce.com/
---
