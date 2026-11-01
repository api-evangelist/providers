---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.6
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 37
  human_in_the_loop: 9
  name: Secure Flows Com Agentic Access
  operation_count: 65
  slug: secure-flows-com-agentic-access
  summary_line: 65 operations · 37 acting · 9 human-in-the-loop
api_count: 4
apis:
- baseURL: https://www.secure-flows.com/api/v1
  baseurl_source: declared
  description: The ai-optional API from secure-flows-com — 3 operation(s) for ai-optional.
  name: secure-flows-com AI Optional API
  slug: secure-flows-com-ai-optional-api
- baseURL: https://www.secure-flows.com/api/v1
  baseurl_source: declared
  description: Public read-only documentation lookup (no tokens)
  name: secure-flows-com AI Safe API
  slug: secure-flows-com-ai-safe-api
- baseURL: https://www.secure-flows.com/api/v1
  baseurl_source: declared
  description: Registered applications and redirect allowlists (ADMIN/OWNER)
  name: secure-flows-com Applications API
  slug: secure-flows-com-applications-api
- baseURL: https://www.secure-flows.com/api/v1
  baseurl_source: declared
  description: Workspace audit trail and HTTP API access log (ADMIN/OWNER read)
  name: secure-flows-com Audit API
  slug: secure-flows-com-audit-api
- baseURL: https://www.secure-flows.com/api/v1
  baseurl_source: declared
  description: Browser entry (Flutter); not a JSON API
  name: secure-flows-com Hosted UI API
  slug: secure-flows-com-hosted-ui-api
- baseURL: https://www.secure-flows.com/api/v1
  baseurl_source: declared
  description: Human chat surface (SSE); prefer docs search for agents
  name: secure-flows-com Human Only API
  slug: secure-flows-com-human-only-api
- baseURL: https://www.secure-flows.com/api/v1
  baseurl_source: declared
  description: Workspace user directory (ADMIN/OWNER)
  name: secure-flows-com Users API
  slug: secure-flows-com-users-api
artifact_total: 30
common:
- group: agent
  href: https://artifacts.apis.io/secure-flows-com/agentic-access/secure-flows-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/secure-flows-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/secure-flows-com/rules/secure-flows-com-rules.yml
  title: ''
  type: Spectral
  url: rules/secure-flows-com-rules.yml
- group: design
  href: https://artifacts.apis.io/secure-flows-com/json-ld/secure-flows-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/secure-flows-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/secure-flows-com/vocabulary/secure-flows-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/secure-flows-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/secure-flows-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/secure-flows-com/data-model/secure-flows-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/secure-flows-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/secure-flows-com/authentication/secure-flows-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/secure-flows-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/secure-flows-com/errors/secure-flows-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/secure-flows-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/secure-flows-com/conformance/secure-flows-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/secure-flows-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/secure-flows-com/llms/secure-flows-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/secure-flows-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/secure-flows-com/mcp/secure-flows-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/secure-flows-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/secure-flows-com/hosts/secure-flows-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/secure-flows-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/secure-flows-com/vendors/secure-flows-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/secure-flows-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/secure-flows-com/security/secure-flows-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/secure-flows-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://secure-flows.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.secure-flows.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://www.secure-flows.com/docs/openapi/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.secure-flows.com/docs/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://www.secure-flows.com/docs/contact/
- group: company
  title: ''
  type: Blog
  url: https://www.secure-flows.com/docs/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.secure-flows.com/docs/workspace-management/billing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.secure-flows.com/docs/legal/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.secure-flows.com/docs/legal/privacy-policy/
created: '2026-10-30'
description: Secure Flows provides encrypted storage, tenant isolation, hosted login, and session management for no‑code applications, enabling developers to add secure user data handling without building authentication or encryption themselves. The platform offers APIs for data storage, user management, and integration with AI assistants, emphasizing privacy, compliance, and easy integration.
image: https://www.secure-flows.com/favicon.png
json_schemas:
- name: AssistantChatRequest
  property_count: 1
  slug: secure-flows-com-assistant-chat-request
- name: ClientAppRequest
  property_count: 5
  slug: secure-flows-com-client-app-request
- name: ClientAppResponse
  property_count: 7
  slug: secure-flows-com-client-app-response
- name: CreateSessionResponse
  property_count: 1
  slug: secure-flows-com-create-session-response
- name: DocSearchResponse
  property_count: 4
  slug: secure-flows-com-doc-search-response
- name: GetSessionValueResponse
  property_count: 2
  slug: secure-flows-com-get-session-value-response
- name: SessionIdentityView
  property_count: 2
  slug: secure-flows-com-session-identity-view
- name: SessionRenewResponse
  property_count: 2
  slug: secure-flows-com-session-renew-response
- name: SessionRequest
  property_count: 3
  slug: secure-flows-com-session-request
- name: SetSessionValueRequest
  property_count: 0
  slug: secure-flows-com-set-session-value-request
- name: UserDto
  property_count: 8
  slug: secure-flows-com-user-dto
- name: WorkspaceBillingResponse
  property_count: 17
  slug: secure-flows-com-workspace-billing-response
- name: WorkspaceCreateRequest
  property_count: 5
  slug: secure-flows-com-workspace-create-request
jsonld:
- class_count: 56
  name: Secure Flows Com Context
  property_count: 118
  slug: secure-flows-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at www.secure-flows.com.
  name: secure-flows-com MCP Server
  slug: secure-flows-com-mcp-yml
modified: '2026-10-30'
name: secure-flows-com
nav: Providers
network: true
overview: 'secure-flows-com publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including AI Optional API, AI Safe API, Applications API, and 4 more. Tagged areas include Company, Security, Data-Encryption, No-code, and Authentication.


  The secure-flows-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  secure-flows-com''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 16 more developer resources.'
plans:
- name: Secure Flows Com Plans Pricing
  plan_count: 0
  slug: secure-flows-com-plans-pricing
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: secure-flows-com API Rules
  rule_count: 14
  severity_counts:
    error: 7
    hint: 0
    info: 4
    warn: 3
  slug: secure-flows-com-rules
score:
  band: developing
  composite: 42.9
  coverage:
    artifact_dirs: 21
    catalog_earned: 65.8
    catalog_earned_first_party: 0.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 59.0
    developer_ergonomics: 54.0
    discoverability: 70.0
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
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
  name: Secure Flows Com Authentication
  slug: secure-flows-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Secure Flows Com Domain Security
  slug: secure-flows-com-domain-security
  summary_line: TLSv1.3
skill_count: 3
skills:
- name: secure-flows-com-auth
  slug: secure-flows-com-auth
- name: secure-flows-com-docs
  slug: secure-flows-com-docs
- name: secure-flows-com-user
  slug: secure-flows-com-user
slug: secure-flows-com
tags:
- Company
- Security
- Data-Encryption
- No-code
- Authentication
website: https://secure-flows.com/
---
