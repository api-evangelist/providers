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
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
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
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 60.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Debounce Agentic Access
  operation_count: 7
  slug: debounce-agentic-access
  summary_line: 7 operations
api_count: 3
apis:
- description: 'Free company logo lookup service positioned as a drop-in replacement for the deprecated Clearbit Logo API. A GET against logo.debounce.com with a company domain returns a high-quality PNG logo served '
  name: DeBounce Logo API
  slug: debounce-logo-api
- baseURL: https://api.debounce.io
  baseurl_source: declared
  description: The Account Management API from DeBounce — 1 operation(s) for account management.
  name: DeBounce Account Management API
  phrasing_intents:
  - id: getBalance
    intent: Check remaining validation credits
    question: How many DeBounce credits do I have left on my account?
  phrasing_ops: 1
  slug: debounce-account-management-api
- baseURL: https://api.debounce.io
  baseurl_source: declared
  description: The DeBounce Disposable Email Detector API API from DeBounce — 1 operation(s) for debounce disposable email detector api.
  name: DeBounce Disposable Email Detector API
  phrasing_intents:
  - id: checkDisposableEmail
    intent: Check if an email or domain is disposable
    question: Is there a free way to tell if a signup email is a throwaway address?
  phrasing_ops: 1
  slug: debounce-debounce-disposable-email-detector-api-api
- baseURL: https://api.debounce.io
  baseurl_source: declared
  description: The DeBounce Email Validation API API from DeBounce — 1 operation(s) for debounce email validation api.
  name: DeBounce Email Validation API
  phrasing_intents:
  - id: validateEmail
    intent: Validate a single email address
    question: How do I verify that one email address is deliverable before I send to it?
  phrasing_ops: 1
  slug: debounce-debounce-email-validation-api-api
- baseURL: https://api.debounce.io
  baseurl_source: declared
  description: The Reverse API from DeBounce — 1 operation(s) for reverse.
  name: DeBounce Reverse API
  phrasing_intents:
  - id: reverseEmailLookup
    intent: Look up data associated with an email
    question: Can I find out who is behind an email address?
  phrasing_ops: 1
  slug: debounce-reverse-api
- baseURL: https://api.debounce.io
  baseurl_source: declared
  description: The Status API from DeBounce — 1 operation(s) for status.
  name: DeBounce Status API
  phrasing_intents:
  - id: checkBulkStatus
    intent: Check the status of a bulk validation list
    question: Has my uploaded email list finished validating yet?
  phrasing_ops: 1
  slug: debounce-status-api
- baseURL: https://api.debounce.io
  baseurl_source: declared
  description: The Upload API from DeBounce — 1 operation(s) for upload.
  name: DeBounce Upload API
  phrasing_intents:
  - id: uploadBulkList
    intent: Start bulk validation of an email list
    question: How do I validate a whole CSV of email addresses at once?
  phrasing_ops: 1
  slug: debounce-upload-api
- baseURL: https://api.debounce.io
  baseurl_source: declared
  description: The Usage API from DeBounce — 1 operation(s) for usage.
  name: DeBounce Usage API
  phrasing_intents:
  - id: getUsage
    intent: Get validation usage for a date range
    question: How many email validations did I use last month?
  phrasing_ops: 1
  slug: debounce-usage-api
artifact_total: 31
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
- group: other
  href: https://artifacts.apis.io/debounce/capabilities/debounce-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/debounce-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/debounce/overlays/debounce-validation-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/debounce-validation-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/debounce/overlays/debounce-bulk-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/debounce-bulk-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/debounce/overlays/debounce-data-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/debounce-data-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/debounce/overlays/debounce-account-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/debounce-account-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/debounce/overlays/debounce-disposable-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/debounce-disposable-api-overlay.yaml
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
  href: https://artifacts.apis.io/debounce/a2a/debounce-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/debounce-a2a.yml
- group: agent
  href: https://artifacts.apis.io/debounce/mcp/debounce-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/debounce-mcp.yml
- group: build
  href: https://artifacts.apis.io/debounce/mcp/debounce-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/debounce-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/debounce/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/debounce/llms/debounce-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/debounce-llms.txt
- group: agent
  href: https://artifacts.apis.io/debounce/well-known/debounce-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/debounce-well-known.yml
- group: agent
  href: https://artifacts.apis.io/debounce/agentic-access/debounce-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/debounce-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/debounce/authentication/debounce-authentication.yml
  title: ''
  type: Authentication
  url: authentication/debounce-authentication.yml
- group: auth
  href: https://artifacts.apis.io/debounce/scopes/debounce-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/debounce-scopes.yml
- group: design
  href: https://artifacts.apis.io/debounce/conventions/debounce-conventions.yml
  title: ''
  type: Conventions
  url: conventions/debounce-conventions.yml
- group: design
  href: https://artifacts.apis.io/debounce/errors/debounce-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/debounce-problem-types.yml
- group: design
  href: https://artifacts.apis.io/debounce/lifecycle/debounce-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/debounce-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/debounce/conformance/debounce-conformance.yml
  title: ''
  type: Conformance
  url: conformance/debounce-conformance.yml
- group: design
  href: https://artifacts.apis.io/debounce/data-model/debounce-data-model.yml
  title: ''
  type: DataModel
  url: data-model/debounce-data-model.yml
- group: design
  href: https://artifacts.apis.io/debounce/components/debounce-components.yml
  title: ''
  type: Components
  url: components/debounce-components.yml
- group: build
  href: https://artifacts.apis.io/debounce/packages/debounce-packages.yml
  title: ''
  type: Packages
  url: packages/debounce-packages.yml
- group: operate
  href: https://artifacts.apis.io/debounce/changelog/debounce-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/debounce-changelog.yml
- group: auth
  href: https://artifacts.apis.io/debounce/security/debounce-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/debounce-domain-security.yml
- group: commercial
  href: https://artifacts.apis.io/debounce/plans/debounce-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/debounce-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/debounce/rate-limits/debounce-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/debounce-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/debounce/finops/debounce-finops.yml
  title: ''
  type: FinOps
  url: finops/debounce-finops.yml
- group: design
  href: https://artifacts.apis.io/debounce/vocabulary/debounce-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/debounce-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/debounce/json-ld/debounce-context.jsonld
  title: ''
  type: JSONLDContext
  url: json-ld/debounce-context.jsonld
- group: company
  href: https://artifacts.apis.io/debounce/blogs/blogs.json
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
- has_sources: true
  method: derived
  name: Debounce Finops
  primary_unit: check/credit
  service_category: ''
  slug: debounce-finops
  template: false
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
  slug: debounce-mcp-yml
modified: '2026-09-16'
name: DeBounce
nav: Providers
network: true
overview: 'DeBounce publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account Management API, Disposable Email Detector API, Email Validation API, and 5 more. Tagged areas include Email Verification, Deliverability, Disposable Email Detection, MX Records, and Bulk Email Validation.


  The DeBounce catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  DeBounce''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 43 more developer resources.'
plans:
- name: Debounce Plans Pricing
  plan_count: 1
  slug: debounce-plans-pricing
- name: Debounce Price Estimates
  plan_count: 0
  slug: debounce-price-estimates
random_paper: 21
rate_limits:
- limit_count: 4
  name: Debounce Rate Limits
  slug: debounce-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: DeBounce — jsonschema rules
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
  composite: 68.3
  coverage:
    artifact_dirs: 36
    catalog_earned: 81.8
    catalog_earned_first_party: 20.0
    catalog_gap: 33.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 81.6
    contract_governance: 41.7
    contract_quality: 53.8
    developer_ergonomics: 68.6
    discoverability: 80.0
    operational_transparency: 63.2
  previous_composite: 68.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 39.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/debounce/debounce-2026-06-20T175751.png
security:
- kind: authentication
  name: Debounce Authentication
  slug: debounce-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Debounce Domain Security
  slug: debounce-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: De Bounce
  slug: debounce-de-bounce
slug: debounce
tags:
- Email Verification
- Deliverability
- Disposable Email Detection
- MX Records
- Bulk Email Validation
- Data Enrichment
- Syntax Validation
- Reverse Email Lookup
- Logo API
- A2A
website: https://debounce.com/
---
