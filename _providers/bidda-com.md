---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: flavored
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.5
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Bidda provides compliance intelligence APIs as described in the developer portal.
  name: Bidda API
  slug: bidda-api
- description: 'Bidda API as documented publicly: 10 operations. Contract generated from the documentation by API Evangelist (2026-11-02); not the provider''s own document.'
  name: Bidda API
  slug: bidda-com-api
artifact_total: 14
common:
- group: commercial
  href: https://artifacts.apis.io/bidda-com/plans/bidda-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bidda-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/bidda-com/rules/bidda-com-rules.yml
  title: ''
  type: Spectral
  url: rules/bidda-com-rules.yml
- group: design
  href: https://artifacts.apis.io/bidda-com/json-ld/bidda-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bidda-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/bidda-com/vocabulary/bidda-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bidda-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/bidda-com/data-model/bidda-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bidda-com-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://bidda.com/compliance
- group: design
  href: https://artifacts.apis.io/bidda-com/conformance/bidda-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bidda-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bidda-com/llms/bidda-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bidda-com-llms.txt
- group: other
  href: https://artifacts.apis.io/bidda-com/a2a/bidda-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/bidda-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/bidda-com/mcp/bidda-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bidda-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/bidda-com/well-known/bidda-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bidda-com-security.txt
- group: agent
  href: https://artifacts.apis.io/bidda-com/well-known/bidda-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bidda-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/bidda-com/hosts/bidda-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bidda-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/bidda-com/vendors/bidda-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bidda-com-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://bidda.com/security
- group: start
  title: ''
  type: Sandbox
  url: https://bidda.com/playground
- group: company
  title: ''
  type: Newsroom
  url: https://bidda.com/intelligence/category/media
- group: operate
  title: ''
  type: ChangeLog
  url: https://bidda.com/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://bidda.com/insights/enterprise-ai-governance-onboarding
- group: auth
  href: https://artifacts.apis.io/bidda-com/security/bidda-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/bidda-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/bidda-com/security/bidda-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bidda-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/bidda-com/security/bidda-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bidda-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bidda.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://bidda.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://bidda.com/developers
- group: commercial
  title: ''
  type: Pricing
  url: https://bidda.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://bidda.com/status
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bidda.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bidda.com/privacy
- group: other
  title: ''
  type: AcceptableUsePolicy
  url: https://bidda.com/aup
coverage:
  checked: '2026-11-02'
  detail: Developer portal provides HTML documentation but no machine‑readable OpenAPI, GraphQL, AsyncAPI, gRPC or WSDL contracts were found.
  evidence:
  - status: timeout
    url: https://api.bidda.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Bidda provides compliance intelligence by aggregating primary source regulations, offering a signed record of each rule, its version, and verification timestamps. With over 10,000 regulations, it helps compliance teams and AI systems ensure they rely on accurate, up-to-date legal data, enhancing risk management and audit readiness.
image: https://bidda.com/assets/bidda-logo.png
json_schemas:
- name: GetApiV1RegistryHealthJsonResponse
  property_count: 7
  slug: bidda-com-get-api-v1-registry-health-json-response
- name: PostMcpRequest
  property_count: 1
  slug: bidda-com-post-mcp-request
- name: PostMcpResponse
  property_count: 3
  slug: bidda-com-post-mcp-response
- name: PostScanRequest
  property_count: 3
  slug: bidda-com-post-scan-request
- name: PostScanResponse
  property_count: 4
  slug: bidda-com-post-scan-response
jsonld:
- class_count: 5
  name: Bidda Com Context
  property_count: 18
  slug: bidda-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at bidda.com.
  name: Bidda MCP Server
  slug: bidda-com-mcp-yml
modified: '2026-11-02'
name: Bidda
nav: Providers
network: true
overview: 'Bidda is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Compliance, Regulations, Artificial Intelligence, and Data.


  The Bidda catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Bidda''s developer surface includes sandbox, changelog, getting-started guide, documentation, pricing, and 25 more developer resources.'
plans:
- name: Bidda Com Plans Pricing
  plan_count: 3
  slug: bidda-com-plans-pricing
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 85
  extends:
  - spectral:oas
  name: Bidda API Rules
  rule_count: 44
  severity_counts:
    error: 42
    hint: 0
    info: 1
    warn: 1
  slug: bidda-com-rules
score:
  band: thin
  composite: 33.9
  coverage:
    artifact_dirs: 17
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 59.2
    contract_governance: 22.0
    contract_quality: 24.7
    developer_ergonomics: 19.0
    discoverability: 57.5
    operational_transparency: 21.1
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bidda Com Domain Security
  slug: bidda-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bidda Com Vulnerability Disclosure
  slug: bidda-com-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Bidda Com Trust Center
  slug: bidda-com-trust-center
  summary_line: SOC 2, HIPAA, FedRAMP, GDPR
slug: bidda-com
tags:
- Company
- Compliance
- Regulations
- Artificial Intelligence
- Data
website: https://bidda.com/
---
