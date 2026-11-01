---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: unknown
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 52.9
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Digiparser Agentic Access
  operation_count: 3
  slug: digiparser-agentic-access
  summary_line: 3 operations · 2 acting
api_count: 1
apis:
- baseURL: https://api.digiparser.com
  baseurl_source: declared
  description: Upload documents for extraction.
  name: DigiParser Document processing API
  slug: digiparser-document-processing-api
- baseURL: https://api.digiparser.com
  baseurl_source: declared
  description: OAuth-protected tools for AI agents.
  name: DigiParser MCP API
  slug: digiparser-mcp-api
- baseURL: https://api.digiparser.com
  baseurl_source: declared
  description: Discover the parsers available to an API key.
  name: DigiParser Parsers API
  slug: digiparser-parsers-api
artifact_total: 15
common:
- group: agent
  href: https://artifacts.apis.io/digiparser/agentic-access/digiparser-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/digiparser-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/digiparser/plans/digiparser-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/digiparser-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/digiparser/rules/digiparser-rules.yml
  title: ''
  type: Spectral
  url: rules/digiparser-rules.yml
- group: design
  href: https://artifacts.apis.io/digiparser/json-ld/digiparser-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/digiparser-context.jsonld
- group: design
  href: https://artifacts.apis.io/digiparser/vocabulary/digiparser-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/digiparser-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/digiparser/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/digiparser/data-model/digiparser-data-model.yml
  title: ''
  type: DataModel
  url: data-model/digiparser-data-model.yml
- group: operate
  href: https://artifacts.apis.io/digiparser/changelog/digiparser-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/digiparser-changelog.yml
- group: auth
  href: https://artifacts.apis.io/digiparser/authentication/digiparser-authentication.yml
  title: ''
  type: Authentication
  url: authentication/digiparser-authentication.yml
- group: design
  href: https://artifacts.apis.io/digiparser/errors/digiparser-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/digiparser-problem-types.yml
- group: design
  href: https://artifacts.apis.io/digiparser/conformance/digiparser-conformance.yml
  title: ''
  type: Conformance
  url: conformance/digiparser-conformance.yml
- group: agent
  href: https://artifacts.apis.io/digiparser/llms/digiparser-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/digiparser-llms.txt
- group: other
  href: https://artifacts.apis.io/digiparser/a2a/digiparser-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/digiparser-a2a.yml
- group: agent
  href: https://artifacts.apis.io/digiparser/mcp/digiparser-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/digiparser-mcp.yml
- group: agent
  href: https://artifacts.apis.io/digiparser/well-known/digiparser-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/digiparser-well-known.yml
- group: other
  href: https://artifacts.apis.io/digiparser/hosts/digiparser-hosts.yml
  title: ''
  type: Hosts
  url: hosts/digiparser-hosts.yml
- group: other
  href: https://artifacts.apis.io/digiparser/vendors/digiparser-vendors.yml
  title: ''
  type: Vendors
  url: vendors/digiparser-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://www.digiparser.com/integrations/webhooks
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mintlify
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.digiparser.com/docs/changelog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.digiparser.com</code
- group: auth
  href: https://artifacts.apis.io/digiparser/security/digiparser-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/digiparser-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.digiparser.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.digiparser.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.digiparser.com/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://www.digiparser.com/docs/guides/quick-start
- group: operate
  title: ''
  type: Support
  url: https://www.digiparser.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.digiparser.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.digiparser.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.digiparser.com/schedule-demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.digiparser.com/docs/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.digiparser.com/docs/legal/privacy-policy
created: '2026-10-30'
description: DigiParser provides AI‑powered document parsing and data extraction services for invoices, receipts, contracts, bank statements, and more. Its cloud‑based platform lets developers integrate OCR, classification, and custom field extraction via a RESTful API, supporting multiple regions with dedicated endpoints. The service offers robust rate limits, webhook notifications, and an MCP server for AI agents, enabling automated workflows across finance, logistics, and insurance sectors.
image: https://www.digiparser.com/favicon.ico
json_schemas:
- name: JsonRpcRequest
  property_count: 4
  slug: digiparser-json-rpc-request
jsonld:
- class_count: 2
  name: Digiparser Context
  property_count: 8
  slug: digiparser-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.digiparser.com requiring OAuth.
  name: DigiParser MCP Server
  slug: digiparser-mcp-yml
modified: '2026-10-30'
name: DigiParser
nav: Providers
network: true
overview: 'DigiParser publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Document processing API, MCP API, and Parsers API. Tagged areas include Company, Document-Processing, API, Automation, and Data-Extraction.


  The DigiParser catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  DigiParser''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 25 more developer resources.'
plans:
- name: Digiparser Plans Pricing
  plan_count: 3
  slug: digiparser-plans-pricing
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: DigiParser API Rules
  rule_count: 16
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 1
  slug: digiparser-rules
scopes:
- name: Digiparser Scopes
  scope_count: 0
  slug: digiparser-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 62.4
  coverage:
    artifact_dirs: 27
    catalog_earned: 78.9
    catalog_earned_first_party: 0.0
    catalog_gap: 36.1
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 79.1
    contract_quality: 51.1
    developer_ergonomics: 63.6
    discoverability: 65.0
    operational_transparency: 28.9
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Digiparser Authentication
  slug: digiparser-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Digiparser Domain Security
  slug: digiparser-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: call-mcp-tool
  slug: call-mcp-tool
- name: list-parsers
  slug: list-parsers
- name: upload-files
  slug: upload-files
slug: digiparser
tags:
- Company
- Document-Processing
- API
- Automation
- Data-Extraction
- AI
website: https://www.digiparser.com/
---
