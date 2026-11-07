---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 27.5
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Managed Cybersecurity Platform API documentation
  name: CYBRET MCP
  slug: cybret-mcp
- description: 'CYBRET API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: CYBRET API
  slug: cybret-ai-api
artifact_total: 9
common:
- group: design
  href: https://artifacts.apis.io/cybret-ai/rules/cybret-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/cybret-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/cybret-ai/json-ld/cybret-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cybret-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/cybret-ai/vocabulary/cybret-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cybret-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/cybret-ai/data-model/cybret-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cybret-ai-data-model.yml
- group: auth
  href: https://artifacts.apis.io/cybret-ai/security/cybret-ai-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/cybret-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/cybret-ai/authentication/cybret-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cybret-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/cybret-ai/conformance/cybret-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cybret-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cybret-ai/llms/cybret-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cybret-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/cybret-ai/mcp/cybret-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cybret-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/cybret-ai/well-known/cybret-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cybret-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/cybret-ai/hosts/cybret-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cybret-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/cybret-ai/vendors/cybret-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cybret-ai-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.cybret.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cybret.ai/terms
- group: operate
  title: ''
  type: Support
  url: https://www.cybret.ai/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cybret.ai/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://www.cybret.ai/docs/mcp
- group: auth
  href: https://artifacts.apis.io/cybret-ai/security/cybret-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cybret-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/cybret-ai/security/cybret-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cybret-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cybret.ai/
coverage:
  checked: '2026-11-04'
  detail: Documentation pages are rendered via JavaScript and no machine‑readable spec was found.
  evidence:
  - status: 200
    url: https://www.cybret.ai/docs/mcp
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-04'
description: CYBRET provides continuous black, grey, and white‑box penetration testing services, delivering authorized target coverage, exploit evidence, and remediation guidance. Their platform secures applications, APIs, and infrastructure, emphasizing comprehensive risk reduction and compliance support for modern enterprises.
image: https://www.cybret.ai/og-default.jpg
json_schemas:
- name: PostAccessApiV1TokensResponse
  property_count: 1
  slug: cybret-ai-post-access-api-v1-tokens-response
jsonld:
- class_count: 1
  name: Cybret Ai Context
  property_count: 1
  slug: cybret-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.cybret.ai requiring OAuth.
  name: CYBRET MCP Server
  slug: cybret-ai-mcp-yml
modified: '2026-11-04'
name: CYBRET
nav: Providers
network: true
overview: 'CYBRET is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Security, Penetration Testing, API Security, Software-as-a-Service, and Compliance.


  The CYBRET catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  CYBRET''s developer surface includes authentication, support, documentation, and 17 more developer resources.'
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 72
  extends:
  - spectral:oas
  name: CYBRET API Rules
  rule_count: 31
  severity_counts:
    error: 29
    hint: 0
    info: 1
    warn: 1
  slug: cybret-ai-rules
score:
  band: thin
  composite: 29.8
  coverage:
    artifact_dirs: 17
    catalog_earned: 48.2
    catalog_earned_first_party: 0.0
    catalog_gap: 66.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 28.9
    contract_governance: 35.6
    contract_quality: 17.6
    developer_ergonomics: 26.2
    discoverability: 56.7
    operational_transparency: 10.5
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Cybret Ai Authentication
  slug: cybret-ai-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Cybret Ai Domain Security
  slug: cybret-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cybret Ai Vulnerability Disclosure
  slug: cybret-ai-vulnerability-disclosure
  summary_line: no policy recorded
slug: cybret-ai
tags:
- Security
- Penetration Testing
- API Security
- Software-as-a-Service
- Compliance
website: https://cybret.ai/
---
