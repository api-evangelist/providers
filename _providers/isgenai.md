---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 41.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Isgenai Agentic Access
  operation_count: 7
  slug: isgenai-agentic-access
  summary_line: 7 operations · 5 acting
api_count: 1
apis:
- baseURL: https://isgenai.com
  baseurl_source: declared
  description: AI-origin evidence checks
  name: isGenAI Checks API
  slug: isgenai-checks-api
- baseURL: https://isgenai.com
  baseurl_source: declared
  description: 'Read and validate the C2PA manifest of one uploaded file. Signature validity (cryptographic_validation) and signer trust (trust_validation) are separate results; a missing manifest is not evidence of '
  name: isGenAI Content Credentials API
  slug: isgenai-content-credentials-api
- baseURL: https://isgenai.com
  baseurl_source: declared
  description: Service liveness
  name: isGenAI Health API
  slug: isgenai-health-api
- baseURL: https://isgenai.com
  baseurl_source: declared
  description: 'Public, no-auth remote Model Context Protocol server over Streamable HTTP (JSON-RPC 2.0, stateless, JSON responses rather than SSE). Tools: check_text, check_url, check_image, extract_saved_prompt and'
  name: isGenAI MCP API
  slug: isgenai-mcp-api
- baseURL: https://isgenai.com
  baseurl_source: declared
  description: Read supported saved image prompts or request optional reconstruction when available
  name: isGenAI Prompts API
  slug: isgenai-prompts-api
artifact_total: 25
common:
- group: agent
  href: https://artifacts.apis.io/isgenai/agentic-access/isgenai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/isgenai-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/isgenai/rules/isgenai-rules.yml
  title: ''
  type: Spectral
  url: rules/isgenai-rules.yml
- group: design
  href: https://artifacts.apis.io/isgenai/json-ld/isgenai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/isgenai-context.jsonld
- group: design
  href: https://artifacts.apis.io/isgenai/vocabulary/isgenai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/isgenai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/isgenai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/isgenai/data-model/isgenai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/isgenai-data-model.yml
- group: auth
  href: https://artifacts.apis.io/isgenai/security/isgenai-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/isgenai-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/isgenai/errors/isgenai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/isgenai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/isgenai/conformance/isgenai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/isgenai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/isgenai/llms/isgenai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/isgenai-llms.txt
- group: build
  href: https://artifacts.apis.io/isgenai/mcp/isgenai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/isgenai-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/isgenai/mcp/isgenai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/isgenai-mcp.yml
- group: auth
  href: https://artifacts.apis.io/isgenai/well-known/isgenai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/isgenai-security.txt
- group: agent
  href: https://artifacts.apis.io/isgenai/well-known/isgenai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/isgenai-well-known.yml
- group: other
  href: https://artifacts.apis.io/isgenai/hosts/isgenai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/isgenai-hosts.yml
- group: other
  href: https://artifacts.apis.io/isgenai/vendors/isgenai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/isgenai-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://isgenai.com/changelog
- group: auth
  href: https://artifacts.apis.io/isgenai/security/isgenai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/isgenai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/isgenai/security/isgenai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/isgenai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://isgenai.com
- group: docs
  title: ''
  type: Documentation
  url: https://isgenai.com/api
- group: start
  title: ''
  type: DeveloperPortal
  url: https://isgenai.com/developers
- group: docs
  title: ''
  type: APIReference
  url: https://isgenai.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://isgenai.com/api.md
- group: operate
  title: ''
  type: Support
  url: https://isgenai.com/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://isgenai.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://isgenai.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://isgenai.com/terms
created: '2026-11-02'
description: isGenAI provides a free AI detection service for images, text, code and links. It analyses uploaded files or URLs and returns evidence such as Content Credentials (C2PA), AI labels, saved prompts, and AI‑use statements. The service is private by default, requires no API key or account, and offers a public HTTP API that returns JSON with detection results, supporting formats PNG, JPG, WEBP, AVIF, TIFF and up to 16 000 characters of text. The platform also supplies tools for image metadata, prompt extraction, and workflow inspection, all accessible via a web interface.
image: https://isgenai.com/icon-512.png
json_schemas:
- name: C2paInspectionResponse
  property_count: 7
  slug: isgenai-c2pa-inspection-response
- name: CheckResponse
  property_count: 18
  slug: isgenai-check-response
- name: JsonCheckInput
  property_count: 10
  slug: isgenai-json-check-input
- name: JsonPromptInput
  property_count: 6
  slug: isgenai-json-prompt-input
- name: MultipartCheckInput
  property_count: 9
  slug: isgenai-multipart-check-input
- name: MultipartPromptInput
  property_count: 2
  slug: isgenai-multipart-prompt-input
jsonld:
- class_count: 41
  name: Isgenai Context
  property_count: 129
  slug: isgenai-context
layout: provider
mcp_servers:
- description: Remote MCP server at isgenai.com.
  name: isGenAI MCP Server
  slug: isgenai-mcp-yml
modified: '2026-11-02'
name: isGenAI
nav: Providers
network: true
overview: 'isGenAI publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Checks API, Content Credentials API, Health API, and 2 more. Tagged areas include Artificial Intelligence, Detector, Image, Text, and Code.


  The isGenAI catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  isGenAI''s developer surface includes changelog, documentation, API reference, getting-started guide, support, pricing, and 22 more developer resources.'
random_paper: 16
rate_limits:
- limit_count: 0
  name: Isgenai Rate Limits
  slug: isgenai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 94
  extends:
  - spectral:oas
  name: isGenAI API Rules
  rule_count: 53
  severity_counts:
    error: 46
    hint: 0
    info: 4
    warn: 3
  slug: isgenai-rules
scopes:
- name: Isgenai Scopes
  scope_count: 0
  slug: isgenai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 37.8
  coverage:
    artifact_dirs: 29
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 15.8
    contract_governance: 22.0
    contract_quality: 62.1
    developer_ergonomics: 27.9
    discoverability: 65.0
    operational_transparency: 18.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Isgenai Authentication
  slug: isgenai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Isgenai Domain Security
  slug: isgenai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
- kind: vulnerability-disclosure
  name: Isgenai Vulnerability Disclosure
  slug: isgenai-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 5
skills:
- name: check-image
  slug: isgenai-check-image
- name: check-text
  slug: isgenai-check-text
- name: check-url
  slug: isgenai-check-url
- name: extract-saved-prompt
  slug: isgenai-extract-saved-prompt
- name: read-content-credentials
  slug: isgenai-read-content-credentials
slug: isgenai
tags:
- Artificial Intelligence
- Detector
- Image
- Text
- Code
- Free
- Privacy
website: https://isgenai.com
---
