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
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 53.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 58
  human_in_the_loop: 0
  name: Good Grants Agentic Access
  operation_count: 103
  slug: good-grants-agentic-access
  summary_line: 103 operations · 58 acting
api_count: 1
apis:
- baseURL: https://api.us.cr4ce.com
  baseurl_source: declared
  description: 'Use this operation to retrieve information about your organisation account. The account resource provides metadata about the tenant associated with your API key. Note: Account information is read-only'
  name: GOOD Grants Account API
  slug: good-grants-account-api
- baseURL: https://api.us.cr4ce.com
  baseurl_source: declared
  description: Use these operations to manage individual review and evaluation activities. Action tasks represent specific actions that reviewers or administrators need to complete during the evaluation process. Tas
  name: GOOD Grants Action tasks API
  slug: good-grants-action-tasks-api
- baseURL: https://api.us.cr4ce.com
  baseurl_source: declared
  description: Use these operations to manage individual payments made against grant allocations. Allocation payments represent installments or disbursements of awarded funds. Payments track scheduling, status (pend
  name: GOOD Grants Allocation payments API
  slug: good-grants-allocation-payments-api
- baseURL: https://api.us.cr4ce.com
  baseurl_source: declared
  description: Use these operations to manage grant allocations awarded to applications. An allocation represents the award of funds from a budget (fund) to an application or applicant. Allocations track the total g
  name: GOOD Grants Allocations API
  slug: good-grants-allocations-api
- baseURL: https://api.us.cr4ce.com
  baseurl_source: declared
  description: Use these operations to manage grant applications submitted to your funding programs. Applications are the core entity that flows through the entire lifecycle from submission to review to grant award.
  name: GOOD Grants Applications API
  slug: good-grants-applications-api
- baseURL: https://api.us.cr4ce.com
  baseurl_source: declared
  description: 'Use these operations to perform granular updates on applications without replacing the entire resource. These endpoints enable real-time updates to specific application properties such as: title, cate'
  name: GOOD Grants Applications (realtime) API
  slug: good-grants-applications-realtime-api
- baseURL: https://api.us.cr4ce.com
  baseurl_source: declared
  description: Use these operations to manage review assignments for evaluating grant applications. Assignments connect reviewers (or roles) with applications and scoring rubrics to facilitate the evaluation process
  name: GOOD Grants Assignments API
  slug: good-grants-assignments-api
- baseURL: https://api.us.cr4ce.com
  baseurl_source: declared
  description: Use these operations to manage files uploaded to applications through attachment tabs. Attachments are distinct from field-based file uploads and allow for supplementary materials such as letters of s
  name: GOOD Grants Attachments API
  slug: good-grants-attachments-api
- baseURL: https://api.us.cr4ce.com
  baseurl_source: declared
  description: Use these operations to manage funding categories or program areas. Categories organise applications into logical groups and can be hierarchical with parent-child relationships. Each category can have
  name: GOOD Grants Categories API
  slug: good-grants-categories-api
- baseURL: https://api.us.cr4ce.com
  baseurl_source: declared
  description: Use these operations to manage geographic or organisational divisions within your grant programs. Chapters enable you to run regional funding programs, manage local grants, or organise by funding prio
  name: GOOD Grants Chapters API
  slug: good-grants-chapters-api
- baseURL: https://api.us.cr4ce.com
  baseurl_source: declared
  description: Use these operations to manage additional people associated with applications beyond the primary applicant. Contributors represent project team members, fiscal sponsors, or partners on a grant proposa
  name: GOOD Grants Contributors API
  slug: good-grants-contributors-api
- baseURL: https://api.us.cr4ce.com
  baseurl_source: declared
  description: Use these operations to generate and retrieve PDF documents and data exports. Documents can be created based on application data, grantee data, compliance reports, or other program information. Docume
  name: GOOD Grants Documents API
  slug: good-grants-documents-api
- baseURL: https://api.us.cr4ce.com
  baseurl_source: declared
  description: Use these operations to manage custom form fields used to collect data throughout your grant programs. Fields can be attached to applications, users, contributors, attachments, and other resources. Su
  name: GOOD Grants Fields API
  slug: good-grants-fields-api
- baseURL: https://api.us.cr4ce.com
  baseurl_source: declared
  description: Use these operations to retrieve information about uploaded files. Files provide metadata and download links for documents uploaded throughout the system. Access files using their secure token identif
  name: GOOD Grants Files API
  slug: good-grants-files-api
- baseURL: https://api.us.cr4ce.com
  baseurl_source: declared
  description: Use these operations to retrieve application form structures and configurations. Forms define the data collection structure for grant applications within categories. Each form contains custom fields o
  name: GOOD Grants Forms API
  slug: good-grants-forms-api
- baseURL: https://api.us.cr4ce.com
  baseurl_source: declared
  description: Use these operations to manage budget sources for allocations and grants. Funds represent pools of money available for distribution, such as "Innovation Fund 2026" or "Community Development Budget". E
  name: GOOD Grants Funds API
  slug: good-grants-funds-api
- baseURL: https://api.us.cr4ce.com
  baseurl_source: declared
  description: Use these operations to manage grant reports and post-award compliance documentation. Grant reports track progress reporting requirements and outcomes for awarded grants. Reports capture applicant inf
  name: GOOD Grants Grant reports API
  slug: good-grants-grant-reports-api
- baseURL: https://api.us.cr4ce.com
  baseurl_source: declared
  description: Use these operations to retrieve custom grant lifecycle statuses. Grant statuses provide additional status tracking beyond standard application review statuses. These are used to track stages like "El
  name: GOOD Grants Grant statuses API
  slug: good-grants-grant-statuses-api
- baseURL: https://api.us.cr4ce.com
  baseurl_source: declared
  description: Use these operations to retrieve ranking results and scores for applications. The leaderboard shows how applications rank based on score sets, with support for filtering by category, chapter, and tags
  name: GOOD Grants Leaderboard API
  slug: good-grants-leaderboard-api
- baseURL: https://api.us.cr4ce.com
  baseurl_source: declared
  description: Use these operations to retrieve round information for your grant programs. Rounds represent phases within a funding cycle, such as application rounds, review rounds, or decision rounds. Each round ha
  name: GOOD Grants Rounds API
  slug: good-grants-rounds-api
- baseURL: https://api.us.cr4ce.com
  baseurl_source: declared
  description: Use these operations to retrieve scoring rubrics and evaluation criteria. Score sets define the questions, scoring scales, and calculation methods used to evaluate grant applications. Score sets can o
  name: GOOD Grants Score sets API
  slug: good-grants-score-sets-api
- baseURL: https://api.us.cr4ce.com
  baseurl_source: declared
  description: Use these operations to retrieve information about funding cycles (seasons). A season represents a time-bound grant program instance, such as "2026 Community Grants" or "Q1 2026 Innovation Fund". Seas
  name: GOOD Grants Seasons API
  slug: good-grants-seasons-api
- baseURL: https://api.us.cr4ce.com
  baseurl_source: declared
  description: Use these operations to manage the tabs that divide a form into sections. Each tab groups what the form collects at that point, such as the application details, custom fields, attachments, contributor
  name: GOOD Grants Tabs API
  slug: good-grants-tabs-api
- baseURL: https://api.us.cr4ce.com
  baseurl_source: declared
  description: 'Use these operations to retrieve tax configurations for financial transactions. Tax settings define how taxes are calculated and applied to orders and payments. Note: Tax configurations are read-only '
  name: GOOD Grants Taxes API
  slug: good-grants-taxes-api
- baseURL: https://api.us.cr4ce.com
  baseurl_source: declared
  description: Use these operations to manage user accounts in your grant-making organisation. Users represent people who interact with your programs, including applicants, reviewers, administrators, and other roles
  name: GOOD Grants Users API
  slug: good-grants-users-api
- baseURL: https://api.us.cr4ce.com
  baseurl_source: declared
  description: 'Use these operations to manage webhook subscriptions for real-time event notifications. Webhooks notify your external systems when events occur in Good Grants, such as application submissions, status '
  name: GOOD Grants Webhooks API
  slug: good-grants-webhooks-api
artifact_total: 48
asyncapis:
- description: ''
  name: Good Grants Webhooks
  slug: good-grants-webhooks
common:
- group: operate
  href: https://artifacts.apis.io/good-grants/rate-limits/good-grants-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/good-grants-rate-limits.yml
- group: auth
  href: https://artifacts.apis.io/good-grants/well-known/good-grants-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/good-grants-status-security.txt
- group: other
  href: https://artifacts.apis.io/good-grants/capabilities/good-grants-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/good-grants-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/good-grants/agentic-access/good-grants-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/good-grants-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/good-grants/plans/good-grants-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/good-grants-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/good-grants/rules/good-grants-rules.yml
  title: ''
  type: Spectral
  url: rules/good-grants-rules.yml
- group: design
  href: https://artifacts.apis.io/good-grants/json-ld/good-grants-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/good-grants-context.jsonld
- group: design
  href: https://artifacts.apis.io/good-grants/vocabulary/good-grants-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/good-grants-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/good-grants/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/good-grants/asyncapi/good-grants-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/good-grants-webhooks.yml
- group: design
  href: https://artifacts.apis.io/good-grants/data-model/good-grants-data-model.yml
  title: ''
  type: DataModel
  url: data-model/good-grants-data-model.yml
- group: operate
  href: https://artifacts.apis.io/good-grants/changelog/good-grants-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/good-grants-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://goodgrants.com/features/security/
- group: auth
  href: https://artifacts.apis.io/good-grants/authentication/good-grants-authentication.yml
  title: ''
  type: Authentication
  url: authentication/good-grants-authentication.yml
- group: design
  href: https://artifacts.apis.io/good-grants/errors/good-grants-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/good-grants-problem-types.yml
- group: design
  href: https://artifacts.apis.io/good-grants/conformance/good-grants-conformance.yml
  title: ''
  type: Conformance
  url: conformance/good-grants-conformance.yml
- group: agent
  href: https://artifacts.apis.io/good-grants/llms/good-grants-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/good-grants-llms.txt
- group: other
  href: https://artifacts.apis.io/good-grants/a2a/good-grants-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/good-grants-a2a.yml
- group: build
  href: https://artifacts.apis.io/good-grants/mcp/good-grants-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/good-grants-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/good-grants/mcp/good-grants-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/good-grants-mcp.yml
- group: agent
  href: https://artifacts.apis.io/good-grants/well-known/good-grants-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/good-grants-well-known.yml
- group: other
  href: https://artifacts.apis.io/good-grants/hosts/good-grants-hosts.yml
  title: ''
  type: Hosts
  url: hosts/good-grants-hosts.yml
- group: other
  href: https://artifacts.apis.io/good-grants/vendors/good-grants-vendors.yml
  title: ''
  type: Vendors
  url: vendors/good-grants-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://goodgrants.com/tos/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.goodgrants.com/
- group: auth
  title: ''
  type: Security
  url: https://goodgrants.com/features/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.goodgrants.com/privacy-policy
- group: other
  title: ''
  type: Leadership
  url: https://goodgrants.com/team/nick/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.goodgrants.com/docs/additional/changelog
- group: auth
  href: https://artifacts.apis.io/good-grants/security/good-grants-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/good-grants-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/good-grants/security/good-grants-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/good-grants-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://goodgrants.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.goodgrants.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.goodgrants.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.goodgrants.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://goodgrants.com/contact/
- group: commercial
  title: ''
  type: Pricing
  url: https://goodgrants.com/pricing/
created: '2026-10-28'
description: Good Grants provides grantmakers with affordable, comprehensive software to manage the entire grantmaking lifecycle—from pre‑award planning through post‑award reporting. The platform is 100 % remote, bootstrapped, and operates without outside funding, allowing the team to focus on continuous product innovation and high‑quality service. Good Grants emphasizes values such as improvement, environmental responsibility, integrity, good design, and community, and participates in the Pledge 1% movement, contributing a portion of equity, profit, product, or time each year. Their solution supports multiple languages, currencies, and data residency options, catering to international grantmakers seeking a reliable, scalable SaaS tool.
image: https://goodgrants.com/wp-content/uploads/2023/05/Good-Grants-logo-500px.png
json_schemas:
- name: Allocation
  property_count: 11
  slug: good-grants-allocation
- name: Assignment
  property_count: 16
  slug: good-grants-assignment
- name: Attachment
  property_count: 8
  slug: good-grants-attachment
- name: Category
  property_count: 21
  slug: good-grants-category
- name: Field
  property_count: 32
  slug: good-grants-field
- name: GetAccountResponse
  property_count: 2
  slug: good-grants-get-account-response
- name: GetAssignmentResponse
  property_count: 6
  slug: good-grants-get-assignment-response
- name: GetDocumentResponse
  property_count: 6
  slug: good-grants-get-document-response
- name: Tab
  property_count: 17
  slug: good-grants-tab
jsonld:
- class_count: 33
  name: Good Grants Context
  property_count: 171
  slug: good-grants-context
layout: provider
mcp_servers:
- description: Remote MCP server at docs.goodgrants.com.
  name: GOOD Grants MCP Server
  slug: good-grants-mcp-yml
modified: '2026-10-28'
name: GOOD Grants
nav: Providers
network: true
overview: 'GOOD Grants publishes 26 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Action tasks API, Allocation payments API, and 23 more. Tagged areas include Company, Grants, Software-as-a-Service, Non-Profit, and Funding.


  The GOOD Grants catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  GOOD Grants'' developer surface includes changelog, authentication, documentation, API reference, getting-started guide, support, pricing, and 30 more developer resources.'
plans:
- name: Good Grants Plans Pricing
  plan_count: 36
  slug: good-grants-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 1
  name: Good Grants Rate Limits
  slug: good-grants-rate-limits
rules:
- authorship: generated
  effective_rule_count: 98
  extends:
  - spectral:oas
  name: GOOD Grants API Rules
  rule_count: 57
  severity_counts:
    error: 49
    hint: 0
    info: 1
    warn: 7
  slug: good-grants-rules
scopes:
- name: Good Grants Scopes
  scope_count: 0
  slug: good-grants-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 58.7
  coverage:
    artifact_dirs: 34
    catalog_earned: 82.8
    catalog_earned_first_party: 20.0
    catalog_gap: 32.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.1
  facets:
    access_clarity: 59.2
    contract_governance: 22.0
    contract_quality: 73.8
    developer_ergonomics: 35.0
    discoverability: 75.8
    operational_transparency: 50.0
  previous_composite: 69.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 96.4
      derived: 1
      marker_coverage: 3.6
      total: 28
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/good-grants/good-grants-2026-11-03T132926.png
security:
- kind: authentication
  name: Good Grants Authentication
  slug: good-grants-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Good Grants Domain Security
  slug: good-grants-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Good Grants Trust Center
  slug: good-grants-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
skill_count: 2
skills:
- name: get-account
  slug: good-grants-get-account
- name: goodgrants
  slug: good-grants-goodgrants
slug: good-grants
tags:
- Company
- Grants
- Software-as-a-Service
- Non-Profit
- Funding
website: https://goodgrants.com/
---
