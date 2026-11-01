---
agent_readiness:
  band: agent-native
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
    error_semantics: documented
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 55.7
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 118
  human_in_the_loop: 8
  name: Luckpanda App Agentic Access
  operation_count: 210
  slug: luckpanda-app-agentic-access
  summary_line: 210 operations · 118 acting · 8 human-in-the-loop
api_count: 1
apis:
- baseURL: https://luckpanda.app/api/v1
  baseurl_source: declared
  description: Two-step sign-in policy, resets and recovery decisions (enrolment itself is session-bound at /mfa), and the accountant's client list (D122)
  name: LuckPanda Access API
  slug: luckpanda-app-access-api
- baseURL: https://luckpanda.app/api/v1
  baseurl_source: declared
  description: People only (a signed-in session); a key cannot manage keys
  name: LuckPanda API keys API
  slug: luckpanda-app-api-keys-api
- baseURL: https://luckpanda.app/api/v1
  baseurl_source: declared
  description: The Approvals API from LuckPanda — 1 operation(s) for approvals.
  name: LuckPanda Approvals API
  slug: luckpanda-app-approvals-api
- baseURL: https://luckpanda.app/api/v1
  baseurl_source: declared
  description: Statement import, the review queue, bank rules, reconciliation, deposits, transfers and registers (Books phase 2)
  name: LuckPanda Banking API
  slug: luckpanda-app-banking-api
- baseURL: https://luckpanda.app/api/v1
  baseurl_source: declared
  description: Periods, year-end close, tie-outs, exceptions and the audit trail (Books phase 1)
  name: LuckPanda Books API
  slug: luckpanda-app-books-api
- baseURL: https://luckpanda.app/api/v1
  baseurl_source: declared
  description: Support tickets (D147). The rest of the chatbot module has REST routes whose bodies are its tool inputs in architecture/mcp/chatbot.json.
  name: LuckPanda Chatbot API
  slug: luckpanda-app-chatbot-api
- baseURL: https://luckpanda.app/api/v1
  baseurl_source: declared
  description: The Connectors API from LuckPanda — 1 operation(s) for connectors.
  name: LuckPanda Connectors API
  slug: luckpanda-app-connectors-api
- baseURL: https://luckpanda.app/api/v1
  baseurl_source: declared
  description: The Context API from LuckPanda — 2 operation(s) for context.
  name: LuckPanda Context API
  slug: luckpanda-app-context-api
- baseURL: https://luckpanda.app/api/v1
  baseurl_source: declared
  description: The Documents API from LuckPanda — 14 operation(s) for documents.
  name: LuckPanda Documents API
  slug: luckpanda-app-documents-api
- baseURL: https://luckpanda.app/api/v1
  baseurl_source: declared
  description: The Guest Access Grants API from LuckPanda — 1 operation(s) for guest access grants.
  name: LuckPanda Guest Access Grants API
  slug: luckpanda-app-guest-access-grants-api
- baseURL: https://luckpanda.app/api/v1
  baseurl_source: declared
  description: One call from your billing code
  name: LuckPanda Invoices API
  slug: luckpanda-app-invoices-api
- baseURL: https://luckpanda.app/api/v1
  baseurl_source: declared
  description: The Members API from LuckPanda — 1 operation(s) for members.
  name: LuckPanda Members API
  slug: luckpanda-app-members-api
- baseURL: https://luckpanda.app/api/v1
  baseurl_source: declared
  description: The Parties API from LuckPanda — 4 operation(s) for parties.
  name: LuckPanda Parties API
  slug: luckpanda-app-parties-api
- baseURL: https://luckpanda.app/api/v1
  baseurl_source: declared
  description: The Payments API from LuckPanda — 6 operation(s) for payments.
  name: LuckPanda Payments API
  slug: luckpanda-app-payments-api
- baseURL: https://luckpanda.app/api/v1
  baseurl_source: declared
  description: UK, US federal and Canada (outside Québec) payroll; journal import elsewhere. Never holds or moves money (D109).
  name: LuckPanda Payroll API
  slug: luckpanda-app-payroll-api
- baseURL: https://luckpanda.app/api/v1
  baseurl_source: declared
  description: Free allowance and trial, connected apps (OAuth for /mcp), AI policy and kill switch, proposals, change feed, personal keys
  name: LuckPanda Platform API
  slug: luckpanda-app-platform-api
- baseURL: https://luckpanda.app/api/v1
  baseurl_source: declared
  description: The Security API from LuckPanda — 1 operation(s) for security.
  name: LuckPanda Security API
  slug: luckpanda-app-security-api
- baseURL: https://luckpanda.app/api/v1
  baseurl_source: declared
  description: The Tasks API from LuckPanda — 1 operation(s) for tasks.
  name: LuckPanda Tasks API
  slug: luckpanda-app-tasks-api
- baseURL: https://luckpanda.app/api/v1
  baseurl_source: declared
  description: The Teams API from LuckPanda — 1 operation(s) for teams.
  name: LuckPanda Teams API
  slug: luckpanda-app-teams-api
- baseURL: https://luckpanda.app/api/v1
  baseurl_source: declared
  description: The Webhooks API from LuckPanda — 8 operation(s) for webhooks.
  name: LuckPanda Webhooks API
  slug: luckpanda-app-webhooks-api
- baseURL: https://luckpanda.app/api/v1
  baseurl_source: declared
  description: The Workspace API from LuckPanda — 2 operation(s) for workspace.
  name: LuckPanda Workspace API
  slug: luckpanda-app-workspace-api
artifact_total: 38
common:
- group: other
  href: https://artifacts.apis.io/luckpanda-app/capabilities/luckpanda-app-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/luckpanda-app-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/luckpanda-app/overlays/luckpanda-app-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/luckpanda-app-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/luckpanda-app/agentic-access/luckpanda-app-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/luckpanda-app-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/luckpanda-app/plans/luckpanda-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/luckpanda-app-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/luckpanda-app/rules/luckpanda-app-rules.yml
  title: ''
  type: Spectral
  url: rules/luckpanda-app-rules.yml
- group: design
  href: https://artifacts.apis.io/luckpanda-app/json-ld/luckpanda-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/luckpanda-app-context.jsonld
- group: design
  href: https://artifacts.apis.io/luckpanda-app/vocabulary/luckpanda-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/luckpanda-app-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/luckpanda-app/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/luckpanda-app/data-model/luckpanda-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/luckpanda-app-data-model.yml
- group: operate
  href: https://artifacts.apis.io/luckpanda-app/changelog/luckpanda-app-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/luckpanda-app-changelog.yml
- group: design
  href: https://artifacts.apis.io/luckpanda-app/conventions/luckpanda-app-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/luckpanda-app-conventions.yml
- group: design
  href: https://artifacts.apis.io/luckpanda-app/conventions/luckpanda-app-conventions.yml
  title: ''
  type: Conventions
  url: conventions/luckpanda-app-conventions.yml
- group: auth
  href: https://artifacts.apis.io/luckpanda-app/authentication/luckpanda-app-authentication.yml
  title: ''
  type: Authentication
  url: authentication/luckpanda-app-authentication.yml
- group: design
  href: https://artifacts.apis.io/luckpanda-app/lifecycle/luckpanda-app-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/luckpanda-app-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/luckpanda-app/errors/luckpanda-app-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/luckpanda-app-problem-types.yml
- group: design
  href: https://artifacts.apis.io/luckpanda-app/conformance/luckpanda-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/luckpanda-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/luckpanda-app/llms/luckpanda-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/luckpanda-app-llms.txt
- group: build
  href: https://artifacts.apis.io/luckpanda-app/mcp/luckpanda-app-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/luckpanda-app-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/luckpanda-app/mcp/luckpanda-app-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/luckpanda-app-mcp.yml
- group: agent
  href: https://artifacts.apis.io/luckpanda-app/well-known/luckpanda-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/luckpanda-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/luckpanda-app/hosts/luckpanda-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/luckpanda-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/luckpanda-app/vendors/luckpanda-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/luckpanda-app-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://luckpanda.app/chatbot/security
- group: other
  title: ''
  type: Leadership
  url: https://luckpanda.app/modules/workspace/team
- group: docs
  title: ''
  type: Documentation
  url: https://luckpanda.app/chatbot/guides
- group: start
  title: ''
  type: DeveloperPortal
  url: https://luckpanda.app/modules/workspace/developers
- group: operate
  title: ''
  type: ChangeLog
  url: https://luckpanda.app/changelog
- group: start
  title: ''
  type: Login
  url: https://luckpanda.app/signin
- group: start
  title: ''
  type: GettingStarted
  url: https://luckpanda.app/chatbot/tools/chatbot-setup
- group: docs
  title: ''
  type: APIReference
  url: https://luckpanda.app/llms.txt
- group: auth
  href: https://artifacts.apis.io/luckpanda-app/security/luckpanda-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/luckpanda-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://luckpanda.app
- group: company
  title: ''
  type: Blog
  url: https://luckpanda.app/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://luckpanda.app/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://luckpanda.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://luckpanda.app/privacy
created: '2026-10-28'
description: LuckPanda provides a unified workspace for sales, CRM, purchasing, inventory, finance and compliance, enabling small businesses to manage invoicing, inventory, accounts and regulatory requirements across borders. The platform offers modular tools, a free starter plan, API and MCP keys for developers, and is built by Vynara.
image: https://luckpanda.app/icon-512.png
json_schemas:
- name: ApiKeyInput
  property_count: 4
  slug: luckpanda-app-api-key-input
- name: CreateInvoiceRequest
  property_count: 0
  slug: luckpanda-app-create-invoice-request
- name: Document
  property_count: 11
  slug: luckpanda-app-document
- name: InvoiceResult
  property_count: 8
  slug: luckpanda-app-invoice-result
- name: RecordPaymentReceipt
  property_count: 0
  slug: luckpanda-app-record-payment-receipt
- name: WebhookDelivery
  property_count: 11
  slug: luckpanda-app-webhook-delivery
jsonld:
- class_count: 21
  name: Luckpanda App Context
  property_count: 104
  slug: luckpanda-app-context
layout: provider
mcp_servers:
- description: Remote MCP server at luckpanda.app.
  name: LuckPanda MCP Server
  slug: luckpanda-app-mcp-yml
modified: '2026-10-28'
name: LuckPanda
nav: Providers
network: true
overview: 'LuckPanda publishes 21 API contracts indexed on the [APIs.io](https://apis.io/) network, including Access API, API keys API, Approvals API, and 18 more. Tagged areas include Company, Business Management, CRM, Accounting, and Inventory.


  The LuckPanda catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  LuckPanda''s developer surface includes changelog, authentication, documentation, getting-started guide, API reference, engineering blog, pricing, and 29 more developer resources.'
plans:
- name: Luckpanda App Plans Pricing
  plan_count: 10
  slug: luckpanda-app-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Luckpanda App Rate Limits
  slug: luckpanda-app-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: LuckPanda API Rules
  rule_count: 11
  severity_counts:
    error: 6
    hint: 0
    info: 2
    warn: 3
  slug: luckpanda-app-rules
score:
  band: strong
  composite: 55.8
  coverage:
    artifact_dirs: 27
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 58.6
    developer_ergonomics: 58.8
    discoverability: 66.7
    operational_transparency: 26.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 21
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Luckpanda App Authentication
  slug: luckpanda-app-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Luckpanda App Domain Security
  slug: luckpanda-app-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 3
skills:
- name: create-invoice
  slug: luckpanda-app-create-invoice
- name: get-document
  slug: luckpanda-app-get-document
- name: issue-document
  slug: luckpanda-app-issue-document
slug: luckpanda-app
tags:
- Company
- Business Management
- CRM
- Accounting
- Inventory
website: https://luckpanda.app
---
