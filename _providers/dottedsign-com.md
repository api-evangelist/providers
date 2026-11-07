---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 43.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 36
  human_in_the_loop: 0
  name: Dottedsign Com Agentic Access
  operation_count: 58
  slug: dottedsign-com-agentic-access
  summary_line: 58 operations · 36 acting
api_count: 7
apis:
- baseURL: https://api.dottedsign.com
  baseurl_source: declared
  description: The Download API from DottedSign — 4 operation(s) for download.
  name: DottedSign Download API
  slug: dottedsign-com-download-api
- baseURL: https://api.dottedsign.com
  baseurl_source: declared
  description: The General API from DottedSign — 18 operation(s) for general.
  name: DottedSign General API
  slug: dottedsign-com-general-api
- baseURL: https://api.dottedsign.com
  baseurl_source: declared
  description: The Management API from DottedSign — 13 operation(s) for management.
  name: DottedSign Management API
  slug: dottedsign-com-management-api
- baseURL: https://api.dottedsign.com
  baseurl_source: declared
  description: The Seal API from DottedSign — 2 operation(s) for seal.
  name: DottedSign Seal API
  slug: dottedsign-com-seal-api
- baseURL: https://api.dottedsign.com
  baseurl_source: declared
  description: The Signature API from DottedSign — 2 operation(s) for signature.
  name: DottedSign Signature API
  slug: dottedsign-com-signature-api
- baseURL: https://api.dottedsign.com
  baseurl_source: declared
  description: The Signing API from DottedSign — 8 operation(s) for signing.
  name: DottedSign Signing API
  slug: dottedsign-com-signing-api
- baseURL: https://api.dottedsign.com
  baseurl_source: declared
  description: The SignTask API from DottedSign — 1 operation(s) for signtask.
  name: DottedSign Sign Task API
  slug: dottedsign-com-signtask-api
artifact_total: 55
asyncapis:
- description: ''
  name: Dottedsign Com Webhooks
  slug: dottedsign-com-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/dottedsign-com/agentic-access/dottedsign-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dottedsign-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/dottedsign-com/rate-limits/dottedsign-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/dottedsign-com-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/dottedsign-com/rules/dottedsign-com-rules.yml
  title: ''
  type: Spectral
  url: rules/dottedsign-com-rules.yml
- group: design
  href: https://artifacts.apis.io/dottedsign-com/json-ld/dottedsign-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dottedsign-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/dottedsign-com/vocabulary/dottedsign-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dottedsign-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/dottedsign-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/dottedsign-com/asyncapi/dottedsign-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/dottedsign-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/dottedsign-com/data-model/dottedsign-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dottedsign-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/dottedsign-com/changelog/dottedsign-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/dottedsign-com-changelog.yml
- group: auth
  href: https://artifacts.apis.io/dottedsign-com/authentication/dottedsign-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dottedsign-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/dottedsign-com/errors/dottedsign-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dottedsign-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/dottedsign-com/conformance/dottedsign-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dottedsign-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dottedsign-com/llms/dottedsign-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dottedsign-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/dottedsign-com/mcp/dottedsign-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dottedsign-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/dottedsign-com/well-known/dottedsign-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dottedsign-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/dottedsign-com/hosts/dottedsign-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dottedsign-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dottedsign-com/vendors/dottedsign-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dottedsign-com-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.dottedsign.com/trust/ccpa/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dottedsign.com/terms_of_service/
- group: operate
  title: ''
  type: Support
  url: https://support.dottedsign.com/hc/en-us
- group: auth
  title: ''
  type: Security
  url: https://www.dottedsign.com/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dottedsign.com/privacy_policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.dottedsign.com/en/pricing/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.dottedsign.com/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://developer.dottedsign.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.dottedsign.com/docs/01-welcome-dottedsign-api-01-get-started
- group: docs
  title: ''
  type: Documentation
  url: https://developer.dottedsign.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.dottedsign.com`
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DottedSign
- group: auth
  href: https://artifacts.apis.io/dottedsign-com/security/dottedsign-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dottedsign-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dottedsign.com/
created: '2026-11-05'
description: DottedSign provides an eSignature solution for seamless workflows, allowing users to create, collect, and manage electronic signatures online. The platform ensures signatures are secure, legally binding, and compliant with international standards, supporting web, iOS, Android, Windows, and macOS applications.
image: https://www.dottedsign.com/static/social/share.png
json_schemas:
- name: CredentialRequest
  property_count: 8
  slug: dottedsign-com-credential-request
- name: CredentialToken
  property_count: 6
  slug: dottedsign-com-credential-token
- name: FileMissionData
  property_count: 1
  slug: dottedsign-com-file-mission-data
- name: FileMissionRequestCreate
  property_count: 1
  slug: dottedsign-com-file-mission-request-create
- name: FileMissionRequestRenew
  property_count: 2
  slug: dottedsign-com-file-mission-request-renew
- name: GroupData
  property_count: 1
  slug: dottedsign-com-group-data
- name: GroupID
  property_count: 1
  slug: dottedsign-com-group-id
- name: GroupRequest
  property_count: 4
  slug: dottedsign-com-group-request
- name: MemberID
  property_count: 1
  slug: dottedsign-com-member-id
- name: MemberRequest
  property_count: 3
  slug: dottedsign-com-member-request
- name: PublicFormID
  property_count: 1
  slug: dottedsign-com-public-form-id
- name: PublicFormList
  property_count: 1
  slug: dottedsign-com-public-form-list
- name: PublicFormRequestCreate
  property_count: 7
  slug: dottedsign-com-public-form-request-create
- name: PublicFormRequestID
  property_count: 1
  slug: dottedsign-com-public-form-request-id
- name: PublicFormRequestUpdate
  property_count: 7
  slug: dottedsign-com-public-form-request-update
- name: PublicFormRequestUpdateStatus
  property_count: 2
  slug: dottedsign-com-public-form-request-update-status
- name: SealID
  property_count: 1
  slug: dottedsign-com-seal-id
- name: SealList
  property_count: 1
  slug: dottedsign-com-seal-list
- name: SignTaskList
  property_count: 1
  slug: dottedsign-com-sign-task-list
- name: SignTaskRequestCreate
  property_count: 10
  slug: dottedsign-com-sign-task-request-create
- name: SignTaskRequestDecline
  property_count: 5
  slug: dottedsign-com-sign-task-request-decline
- name: SignTaskRequestQuickCreate
  property_count: 6
  slug: dottedsign-com-sign-task-request-quick-create
- name: SignTaskRequestReview
  property_count: 5
  slug: dottedsign-com-sign-task-request-review
- name: SignTaskRequestSign
  property_count: 4
  slug: dottedsign-com-sign-task-request-sign
- name: SignTaskRequestUpdate
  property_count: 9
  slug: dottedsign-com-sign-task-request-update
- name: SignatureID
  property_count: 1
  slug: dottedsign-com-signature-id
- name: SignatureList
  property_count: 1
  slug: dottedsign-com-signature-list
- name: SignatureRequestCreate
  property_count: 3
  slug: dottedsign-com-signature-request-create
- name: SignatureRequestID
  property_count: 1
  slug: dottedsign-com-signature-request-id
- name: TemplateID
  property_count: 1
  slug: dottedsign-com-template-id
- name: TemplateList
  property_count: 1
  slug: dottedsign-com-template-list
- name: TemplateRequestCreate
  property_count: 8
  slug: dottedsign-com-template-request-create
- name: TemplateRequestDuplicate
  property_count: 2
  slug: dottedsign-com-template-request-duplicate
- name: TemplateRequestID
  property_count: 1
  slug: dottedsign-com-template-request-id
- name: TemplateRequestUpdate
  property_count: 8
  slug: dottedsign-com-template-request-update
jsonld:
- class_count: 120
  name: Dottedsign Com Context
  property_count: 284
  slug: dottedsign-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at developer.dottedsign.com.
  name: DottedSign MCP Server
  slug: dottedsign-com-mcp-yml
modified: '2026-11-05'
name: DottedSign
nav: Providers
network: true
overview: 'DottedSign publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Download API, General API, Management API, and 4 more. Tagged areas include Company, E-Signature, Workflows, Software-as-a-Service, and Document Management.


  The DottedSign catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  DottedSign''s developer surface includes changelog, authentication, support, pricing, API reference, getting-started guide, documentation, and 24 more developer resources.'
random_paper: 1
rate_limits:
- limit_count: 1
  name: Dottedsign Com Rate Limits
  slug: dottedsign-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 92
  extends:
  - spectral:oas
  name: DottedSign API Rules
  rule_count: 51
  severity_counts:
    error: 41
    hint: 0
    info: 2
    warn: 8
  slug: dottedsign-com-rules
score:
  band: strong
  composite: 57.4
  coverage:
    artifact_dirs: 24
    catalog_earned: 73.8
    catalog_earned_first_party: 8.0
    catalog_gap: 41.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 39.5
    contract_governance: 22.0
    contract_quality: 74.1
    developer_ergonomics: 56.5
    discoverability: 70.0
    operational_transparency: 60.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 7
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Dottedsign Com Authentication
  slug: dottedsign-com-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Dottedsign Com Domain Security
  slug: dottedsign-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 5
skills:
- name: dottedsign-com-archive-sign-task
  slug: dottedsign-com-archive-sign-task
- name: dottedsign-com-create-and-start-sign-task
  slug: dottedsign-com-create-and-start-sign-task
- name: dottedsign-com-manage-signatures
  slug: dottedsign-com-manage-signatures
- name: dottedsign-com-seal-management
  slug: dottedsign-com-seal-management
- name: dottedsign-com-sign-task
  slug: dottedsign-com-sign-task
slug: dottedsign-com
tags:
- Company
- E-Signature
- Workflows
- Software-as-a-Service
- Document Management
website: https://dottedsign.com/
---
