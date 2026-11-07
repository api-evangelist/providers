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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: flavored
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 38.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Desaira Com Agentic Access
  operation_count: 15
  slug: desaira-com-agentic-access
  summary_line: 15 operations · 1 acting
api_count: 1
apis:
- baseURL: https://desaira.com/api/v1
  baseurl_source: declared
  description: AI agent identity / registration
  name: DesAira Agents API
  slug: desaira-com-agents-api
- baseURL: https://desaira.com/api/v1
  baseurl_source: declared
  description: Hashtag and search endpoints
  name: DesAira Tags API
  slug: desaira-com-tags-api
- baseURL: https://desaira.com/api/v1
  baseurl_source: declared
  description: Creator profile endpoints
  name: DesAira Users API
  slug: desaira-com-users-api
- baseURL: https://desaira.com/api/v1
  baseurl_source: declared
  description: Video content endpoints
  name: DesAira Videos API
  slug: desaira-com-videos-api
artifact_total: 15
common:
- group: agent
  href: https://artifacts.apis.io/desaira-com/agentic-access/desaira-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/desaira-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/desaira-com/rules/desaira-com-rules.yml
  title: ''
  type: Spectral
  url: rules/desaira-com-rules.yml
- group: design
  href: https://artifacts.apis.io/desaira-com/json-ld/desaira-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/desaira-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/desaira-com/vocabulary/desaira-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/desaira-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/desaira-com/data-model/desaira-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/desaira-com-data-model.yml
- group: auth
  title: ''
  type: Security
  url: https://desaira.com/guidelines
- group: design
  href: https://artifacts.apis.io/desaira-com/errors/desaira-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/desaira-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/desaira-com/conformance/desaira-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/desaira-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/desaira-com/llms/desaira-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/desaira-com-llms.txt
- group: other
  href: https://artifacts.apis.io/desaira-com/a2a/desaira-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/desaira-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/desaira-com/mcp/desaira-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/desaira-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/desaira-com/well-known/desaira-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/desaira-com-security.txt
- group: agent
  href: https://artifacts.apis.io/desaira-com/well-known/desaira-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/desaira-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/desaira-com/hosts/desaira-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/desaira-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/desaira-com/vendors/desaira-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/desaira-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/desaira-com/authentication/desaira-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/desaira-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/desaira-com/security/desaira-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/desaira-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/desaira-com/security/desaira-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/desaira-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://desaira.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://desaira.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://desaira.com/terms
- group: operate
  title: ''
  type: Support
  url: https://desaira.com/contact
created: '2026-11-05'
description: DesAira is an AI-driven adult content platform offering AI-generated porn, AI girlfriends, and explicit AI sex videos. The service provides free browsing of AI porn, hentai, and anime-style NSFW content without paywalls or apps, positioning itself as a cutting-edge AI entertainment site.
image: https://cdn.desaira.com/branding/og.jpg?v=1788027420
json_schemas:
- name: Comment
  property_count: 12
  slug: desaira-com-comment
- name: Tag
  property_count: 4
  slug: desaira-com-tag
- name: User
  property_count: 8
  slug: desaira-com-user
- name: Video
  property_count: 18
  slug: desaira-com-video
jsonld:
- class_count: 4
  name: Desaira Com Context
  property_count: 36
  slug: desaira-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at desaira.com.
  name: DesAira MCP Server
  slug: desaira-com-mcp-yml
modified: '2026-11-05'
name: DesAira
nav: Providers
network: true
overview: 'DesAira publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agents API, Tags API, Users API, and 1 more. Tagged areas include Adult, Artificial Intelligence, Pornography, Video, and Platform.


  The DesAira catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  DesAira''s developer surface includes authentication, support, and 20 more developer resources.'
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 97
  extends:
  - spectral:oas
  name: DesAira API Rules
  rule_count: 56
  severity_counts:
    error: 54
    hint: 0
    info: 1
    warn: 1
  slug: desaira-com-rules
score:
  band: thin
  composite: 34.2
  coverage:
    artifact_dirs: 19
    catalog_earned: 59.8
    catalog_earned_first_party: 0.0
    catalog_gap: 55.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 56.6
    developer_ergonomics: 16.7
    discoverability: 65.0
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
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
  name: Desaira Com Authentication
  slug: desaira-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Desaira Com Domain Security
  slug: desaira-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Desaira Com Vulnerability Disclosure
  slug: desaira-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: desaira-com
tags:
- Adult
- Artificial Intelligence
- Pornography
- Video
- Platform
website: https://desaira.com/
---
