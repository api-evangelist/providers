---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: partial
    protected_resource_metadata: documented
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 43.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 46
  human_in_the_loop: 4
  name: Arkova Ai Agentic Access
  operation_count: 91
  slug: arkova-ai-agentic-access
  summary_line: 91 operations · 46 acting · 4 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.arkova.ai/api/v1
  baseurl_source: declared
  description: Tenant-scoped agent lifecycle and ComputeID passport admission
  name: Arkova Agents API
  slug: arkova-ai-agents-api
- baseURL: https://api.arkova.ai/api/v1
  baseurl_source: declared
  description: AI-powered extraction, search, and fraud detection (requires Supabase JWT)
  name: Arkova AI Intelligence API
  slug: arkova-ai-ai-intelligence-api
- baseURL: https://api.arkova.ai/api/v1
  baseurl_source: declared
  description: Bitcoin anchoring for credential integrity
  name: Arkova Anchoring API
  slug: arkova-ai-anchoring-api
- baseURL: https://api.arkova.ai/api/v1
  baseurl_source: declared
  description: Attestation claims (create, verify, revoke)
  name: Arkova Attestations API
  slug: arkova-ai-attestations-api
- baseURL: https://api.arkova.ai/api/v1
  baseurl_source: declared
  description: Regulatory lookups, CLE verification, compliance checks
  name: Arkova Compliance API
  slug: arkova-ai-compliance-api
- baseURL: https://api.arkova.ai/api/v1
  baseurl_source: declared
  description: Nested personal and organization record folders
  name: Arkova Folders API
  slug: arkova-ai-folders-api
- baseURL: https://api.arkova.ai/api/v1
  baseurl_source: declared
  description: Third-party connector metadata endpoints (Google Drive, DocuSign) — session-authenticated, not reachable with an API key
  name: Arkova Integrations API
  slug: arkova-ai-integrations-api
- baseURL: https://api.arkova.ai/api/v1
  baseurl_source: declared
  description: Async batch job polling
  name: Arkova Jobs API
  slug: arkova-ai-jobs-api
- baseURL: https://api.arkova.ai/api/v1
  baseurl_source: declared
  description: API key lifecycle management (requires Supabase JWT)
  name: Arkova Key Management API
  slug: arkova-ai-key-management-api
- baseURL: https://api.arkova.ai/api/v1
  baseurl_source: declared
  description: Sub-organization management over an organization API key (orgs:manage)
  name: Arkova Organizations API
  slug: arkova-ai-organizations-api
- baseURL: https://api.arkova.ai/api/v1
  baseurl_source: declared
  description: Anonymous public search across organizations, members, records and imported public records
  name: Arkova Search API
  slug: arkova-ai-search-api
- baseURL: https://api.arkova.ai/api/v1
  baseurl_source: declared
  description: API usage and quota monitoring
  name: Arkova Usage API
  slug: arkova-ai-usage-api
- baseURL: https://api.arkova.ai/api/v1
  baseurl_source: declared
  description: Credential verification endpoints
  name: Arkova Verification API
  slug: arkova-ai-verification-api
- baseURL: https://api.arkova.ai/api/v1
  baseurl_source: declared
  description: Webhook management, testing, and delivery logs
  name: Arkova Webhooks API
  slug: arkova-ai-webhooks-api
artifact_total: 31
asyncapis:
- description: ''
  name: Arkova Ai Webhooks
  slug: arkova-ai-webhooks
common:
- group: auth
  href: https://artifacts.apis.io/arkova-ai/well-known/arkova-ai-modelcontextprotocol-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/arkova-ai-modelcontextprotocol-security.txt
- group: agent
  href: https://artifacts.apis.io/arkova-ai/agentic-access/arkova-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/arkova-ai-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/arkova-ai/plans/arkova-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/arkova-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/arkova-ai/rules/arkova-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/arkova-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/arkova-ai/json-ld/arkova-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/arkova-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/arkova-ai/vocabulary/arkova-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/arkova-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/arkova-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/arkova-ai/asyncapi/arkova-ai-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/arkova-ai-webhooks.yml
- group: design
  href: https://artifacts.apis.io/arkova-ai/data-model/arkova-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/arkova-ai-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://arkova.ai/
- group: auth
  href: https://artifacts.apis.io/arkova-ai/security/arkova-ai-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/arkova-ai-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/arkova-ai/errors/arkova-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/arkova-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/arkova-ai/conformance/arkova-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/arkova-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/arkova-ai/llms/arkova-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/arkova-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/arkova-ai/mcp/arkova-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/arkova-ai-mcp.yml
- group: auth
  href: https://artifacts.apis.io/arkova-ai/well-known/arkova-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/arkova-ai-security.txt
- group: agent
  href: https://artifacts.apis.io/arkova-ai/well-known/arkova-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/arkova-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/arkova-ai/hosts/arkova-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arkova-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/arkova-ai/vendors/arkova-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arkova-ai-vendors.yml
- group: auth
  href: https://artifacts.apis.io/arkova-ai/authentication/arkova-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/arkova-ai-authentication.yml
- group: auth
  href: https://artifacts.apis.io/arkova-ai/security/arkova-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/arkova-ai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/arkova-ai/security/arkova-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/arkova-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/arkova-ai/security/arkova-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arkova-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arkova.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://arkova.ai/docs/v2-migration
- group: docs
  title: ''
  type: APIReference
  url: https://app.arkova.ai/api/docs/spec.json
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.arkova.ai
- group: start
  title: ''
  type: GettingStarted
  url: https://arkova.ai/verification-guide
- group: operate
  title: ''
  type: Support
  url: https://arkova.ai/contact
- group: company
  title: ''
  type: Blog
  url: https://arkova.ai/newsletter
- group: commercial
  title: ''
  type: Pricing
  url: https://arkova.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://arkova.ai/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://arkova.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://arkova.ai/privacy
created: '2026-11-01'
description: Arkova is the trust layer for humans and AI agents. It turns documents into checkable records by computing a SHA-256 fingerprint, publishing a verification record, and linking the record to a public-network receipt without retaining the original document. Teams that own audits get records they can check without trusting Arkova; software and AI agents get the same records through an MCP server, a REST API and SDKs. Direct uploads stay on the user's device; selected connected-source documents are fingerprinted in server memory and discarded. Arkova is live and offers a free tier for developers.
image: https://arkova.ai/og-image.png
json_schemas:
- name: AgentLogAnchorReceiptWithStatements
  property_count: 30
  slug: arkova-ai-agent-log-anchor-receipt-with-statements
- name: ApiKeyMasked
  property_count: 16
  slug: arkova-ai-api-key-masked
- name: Attestation
  property_count: 25
  slug: arkova-ai-attestation
- name: ExtractionResponse
  property_count: 17
  slug: arkova-ai-extraction-response
- name: PublicSearchResponse
  property_count: 5
  slug: arkova-ai-public-search-response
- name: VerificationResult
  property_count: 29
  slug: arkova-ai-verification-result
jsonld:
- class_count: 63
  name: Arkova Ai Context
  property_count: 255
  slug: arkova-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at edge.arkova.ai requiring an API key.
  name: Arkova MCP Server
  slug: arkova-ai-mcp-yml
modified: '2026-11-01'
name: Arkova
nav: Providers
network: true
overview: 'Arkova publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agents API, AI Intelligence API, Anchoring API, and 11 more. Tagged areas include Artificial Intelligence, Trust, Auditing, Verification, and Records.


  The Arkova catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Arkova''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 27 more developer resources.'
plans:
- name: Arkova Ai Plans Pricing
  plan_count: 1
  slug: arkova-ai-plans-pricing
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 109
  extends:
  - spectral:oas
  name: Arkova API Rules
  rule_count: 68
  severity_counts:
    error: 49
    hint: 0
    info: 4
    warn: 15
  slug: arkova-ai-rules
score:
  band: developing
  composite: 50.0
  coverage:
    artifact_dirs: 24
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.7
  facets:
    access_clarity: 55.3
    contract_governance: 22.0
    contract_quality: 69.8
    developer_ergonomics: 41.0
    discoverability: 65.0
    operational_transparency: 18.4
  previous_composite: 60.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Arkova Ai Authentication
  slug: arkova-ai-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Arkova Ai Domain Security
  slug: arkova-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Arkova Ai Vulnerability Disclosure
  slug: arkova-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Arkova Ai Trust Center
  slug: arkova-ai-trust-center
  summary_line: SOC 2, ISO 27001, CSA STAR
skill_count: 1
skills:
- name: agent-management
  slug: arkova-ai-agent-management
slug: arkova-ai
tags:
- Artificial Intelligence
- Trust
- Auditing
- Verification
- Records
- Agents
website: https://arkova.ai/
---
