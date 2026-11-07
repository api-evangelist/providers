---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 52.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 45
  human_in_the_loop: 0
  name: Lawvu Agentic Access
  operation_count: 105
  slug: lawvu-agentic-access
  summary_line: 105 operations · 45 acting
api_count: 2
apis:
- baseURL: https://api.lawvu.com
  baseurl_source: declared
  description: The Contracts API from LawVu — 12 operation(s) for contracts.
  name: LawVu Contracts API
  slug: lawvu-contracts-api
- baseURL: https://api.lawvu.com
  baseurl_source: declared
  description: The Fields API from LawVu — 5 operation(s) for fields.
  name: LawVu Fields API
  slug: lawvu-fields-api
- baseURL: https://api.lawvu.com
  baseurl_source: declared
  description: The Files API from LawVu — 9 operation(s) for files.
  name: LawVu Files API
  slug: lawvu-files-api
- baseURL: https://api.lawvu.com
  baseurl_source: declared
  description: The Invoices API from LawVu — 3 operation(s) for invoices.
  name: LawVu Invoices API
  slug: lawvu-invoices-api
- baseURL: https://api.lawvu.com
  baseurl_source: declared
  description: The Matters API from LawVu — 11 operation(s) for matters.
  name: LawVu Matters API
  slug: lawvu-matters-api
- baseURL: https://api.lawvu.com
  baseurl_source: declared
  description: The Teams API from LawVu — 1 operation(s) for teams.
  name: LawVu Teams API
  slug: lawvu-teams-api
- baseURL: https://api.lawvu.com
  baseurl_source: declared
  description: The Users API from LawVu — 2 operation(s) for users.
  name: LawVu Users API
  slug: lawvu-users-api
artifact_total: 47
asyncapis:
- description: ''
  name: Lawvu Webhooks
  slug: lawvu-webhooks
collections:
- collection_type: open
  name: LawVu Account Auth API
  slug: open-lawvu-auth-api
- collection_type: open
  name: LawVu Account Auth ContractFiles API
  slug: open-lawvu-contractfiles-api
- collection_type: open
  name: LawVu Account Auth ContractKeyDate API
  slug: open-lawvu-contractkeydate-api
- collection_type: open
  name: LawVu Account Auth Contracts API
  slug: open-lawvu-contracts-api
- collection_type: open
  name: LawVu Account Auth ContractStatusMessage API
  slug: open-lawvu-contractstatusmessage-api
- collection_type: open
  name: LawVu Account Auth ContractTemplates API
  slug: open-lawvu-contracttemplates-api
- collection_type: open
  name: LawVu Account Auth ContractUser API
  slug: open-lawvu-contractuser-api
- collection_type: open
  name: LawVu Account Auth Emails API
  slug: open-lawvu-emails-api
- collection_type: open
  name: LawVu Account Auth Features API
  slug: open-lawvu-features-api
- collection_type: open
  name: LawVu Account Auth Fields API
  slug: open-lawvu-fields-api
- collection_type: open
  name: LawVu Account Auth Files API
  slug: open-lawvu-files-api
- collection_type: open
  name: LawVu Account Auth Folders API
  slug: open-lawvu-folders-api
- collection_type: open
  name: LawVu Account Auth Invoices API
  slug: open-lawvu-invoices-api
- collection_type: open
  name: LawVu Account Auth LookupFields API
  slug: open-lawvu-lookupfields-api
- collection_type: open
  name: LawVu Account Auth MatterCategories API
  slug: open-lawvu-mattercategories-api
- collection_type: open
  name: LawVu Account Auth MatterFiles API
  slug: open-lawvu-matterfiles-api
- collection_type: open
  name: LawVu Account Auth Matters API
  slug: open-lawvu-matters-api
- collection_type: open
  name: LawVu Account Auth MattersInvoices API
  slug: open-lawvu-mattersinvoices-api
- collection_type: open
  name: LawVu Account Auth MatterStatusMessage API
  slug: open-lawvu-matterstatusmessage-api
- collection_type: open
  name: LawVu Account Auth MatterTasks API
  slug: open-lawvu-mattertasks-api
- collection_type: open
  name: LawVu Account Auth MatterTaskTemplates API
  slug: open-lawvu-mattertasktemplates-api
- collection_type: open
  name: LawVu Account Auth Organisations API
  slug: open-lawvu-organisations-api
- collection_type: open
  name: LawVu Account Auth Recents API
  slug: open-lawvu-recents-api
- collection_type: open
  name: LawVu Account Auth Teams API
  slug: open-lawvu-teams-api
- collection_type: open
  name: LawVu Account Auth Users API
  slug: open-lawvu-users-api
- collection_type: open
  name: LawVu Account Auth WebhookSubscriptions API
  slug: open-lawvu-webhooksubscriptions-api
common:
- group: commercial
  href: https://artifacts.apis.io/lawvu/plans/lawvu-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/lawvu-plans-pricing.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/lawvu/overview
- group: other
  href: https://artifacts.apis.io/lawvu/capabilities/lawvu-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/lawvu-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/lawvu/overlays/lawvu-account-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/lawvu-account-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://lawvu.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.lawvu.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.lawvu.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.lawvu.com/new-api/lawvuapi.openapi
- group: start
  title: ''
  type: GettingStarted
  url: https://api-docs.lawvu.com/docs
- group: start
  title: ''
  type: SignUp
  url: https://developer.lawvu.com/the-lawvu-api/
- group: start
  title: ''
  type: Login
  url: https://go.lawvu.com/
- group: operate
  title: ''
  type: Support
  url: https://help.lawvu.com/en/
- group: company
  title: ''
  type: Blog
  url: https://lawvu.com/articles/
- group: commercial
  title: ''
  type: Pricing
  url: https://lawvu.com/plans/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lawvu.com/website-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lawvu.com/trust-center/privacy/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LawVu
- group: auth
  href: https://artifacts.apis.io/lawvu/authentication/lawvu-authentication.yml
  title: ''
  type: Authentication
  url: authentication/lawvu-authentication.yml
- group: design
  href: https://artifacts.apis.io/lawvu/conventions/lawvu-conventions.yml
  title: ''
  type: Conventions
  url: conventions/lawvu-conventions.yml
- group: design
  href: https://artifacts.apis.io/lawvu/errors/lawvu-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/lawvu-problem-types.yml
- group: design
  href: https://artifacts.apis.io/lawvu/lifecycle/lawvu-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/lawvu-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://lawvu.com/lawvu-system-status/
- group: operate
  title: ''
  type: Deprecation
  url: https://api-docs.lawvu.com/docs/v2-endpoints-faq
- group: operate
  href: https://artifacts.apis.io/lawvu/changelog/lawvu-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/lawvu-changelog.yml
- group: design
  href: https://artifacts.apis.io/lawvu/asyncapi/lawvu-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/lawvu-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/lawvu/mcp/lawvu-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/lawvu-mcp.yml
- group: agent
  href: https://artifacts.apis.io/lawvu/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  href: https://artifacts.apis.io/lawvu/sandbox/lawvu-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/lawvu-sandbox.yml
- group: build
  href: https://artifacts.apis.io/lawvu/packages/lawvu-packages.yml
  title: ''
  type: Packages
  url: packages/lawvu-packages.yml
- group: design
  href: https://artifacts.apis.io/lawvu/data-model/lawvu-data-model.yml
  title: ''
  type: DataModel
  url: data-model/lawvu-data-model.yml
- group: design
  href: https://artifacts.apis.io/lawvu/conformance/lawvu-conformance.yml
  title: ''
  type: Conformance
  url: conformance/lawvu-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://lawvu.com/trust-center/
- group: auth
  href: https://artifacts.apis.io/lawvu/security/lawvu-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/lawvu-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://lawvu.com/.well-known/security.txt
- group: auth
  href: https://artifacts.apis.io/lawvu/security/lawvu-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/lawvu-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/lawvu/security/lawvu-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lawvu-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/lawvu/well-known/lawvu-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/lawvu-well-known.yml
- group: auth
  href: https://artifacts.apis.io/lawvu/well-known/lawvu-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/lawvu-security.txt
- group: agent
  href: https://artifacts.apis.io/lawvu/llms/lawvu-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lawvu-llms.txt
- group: agent
  href: https://artifacts.apis.io/lawvu/agentic-access/lawvu-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/lawvu-agentic-access.yml
created: '2026-07-17'
description: LawVu is a New Zealand-founded legal technology company whose LegalOS is a connected workspace for corporate in-house legal teams, bringing matter management, contract lifecycle management, legal request intake, spend management and e-billing, document management, reporting and embedded AI into a single platform. LawVu publishes a public REST developer platform — a v2 API covering matters, contracts, fields and files, and a set of legacy v1 product APIs covering accounts, users, organisations, email threads, invoices and webhook subscriptions — secured with OAuth 2.0 authorization code, documented with OpenAPI 3.0.1, returning RFC 9457 problem details, and filtered and paged with a subset of OData. It also ships a first-party MCP server for connecting AI assistants to the LegalOS, a Microsoft Power Platform connector, and a Workato connector. LawVu is backed by Insight Partners.
finops:
- has_sources: true
  method: derived
  name: Lawvu Finops
  primary_unit: ''
  service_category: ''
  slug: lawvu-finops
  template: true
image: https://lawvu.com/wp-content/uploads/2023/09/cropped-fav-icon-192x192.png
layout: provider
mcp_servers:
- description: Remote MCP server at lawvu.com.
  name: LawVu MCP Server
  slug: lawvu-mcp-yml
modified: '2026-07-19'
name: LawVu
nav: Providers
network: true
overview: 'LawVu publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Contracts API, Fields API, Files API, and 4 more. Tagged areas include Company, Legal, Legal Tech, Legal Operations, and Contract Lifecycle Management.


  The LawVu catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  LawVu''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, engineering blog, pricing, and 33 more developer resources.'
plans:
- name: Lawvu Plans Pricing
  plan_count: 3
  slug: lawvu-plans-pricing
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 102
  extends:
  - spectral:oas
  name: LawVu API Rules
  rule_count: 61
  severity_counts:
    error: 49
    hint: 0
    info: 6
    warn: 6
  slug: lawvu-rules
score:
  band: exemplar
  composite: 68.3
  coverage:
    artifact_dirs: 29
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.2
  facets:
    access_clarity: 92.1
    contract_governance: 31.8
    contract_quality: 60.9
    developer_ergonomics: 55.4
    discoverability: 75.0
    operational_transparency: 55.3
  previous_composite: 68.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 15.8
      total: 38
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/lawvu/lawvu-2026-07-25T224645.png
security:
- kind: authentication
  name: Lawvu Authentication
  slug: lawvu-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Lawvu Domain Security
  slug: lawvu-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Lawvu Vulnerability Disclosure
  slug: lawvu-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Lawvu Trust Center
  slug: lawvu-trust-center
  summary_line: ISO 27001, SOC 1, SOC 2
skill_count: 4
skills:
- name: Move a LawVu contract through its lifecycle
  slug: lawvu-contract-lifecycle
- name: Create and track a LawVu matter
  slug: lawvu-create-and-track-matter
- name: Manage LawVu custom fields and their options
  slug: lawvu-manage-fields-and-options
- name: Subscribe to LawVu events
  slug: lawvu-subscribe-to-events
slug: lawvu
tags:
- Company
- Legal
- Legal Tech
- Legal Operations
- Contract Lifecycle Management
- Matter Management
- Document Management
- Spend Management
- Software-as-a-Service
- Workflows
website: https://lawvu.com/
---
