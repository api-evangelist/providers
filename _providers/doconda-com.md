---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 65.9
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 30
  human_in_the_loop: 4
  name: Doconda Com Agentic Access
  operation_count: 49
  slug: doconda-com-agentic-access
  summary_line: 49 operations · 30 acting · 4 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.eu.doconda.com/v1
  baseurl_source: declared
  description: Used by the Doconda dashboard with a signed-in user. Not available with API keys.
  name: doconda-com Dashboard API
  slug: doconda-com-dashboard-api
- baseURL: https://api.eu.doconda.com/v1
  baseurl_source: declared
  description: Create and edit documents.
  name: doconda-com Documents API
  slug: doconda-com-documents-api
- baseURL: https://api.eu.doconda.com/v1
  baseurl_source: declared
  description: Calls your backend makes for the editor plugin.
  name: doconda-com Editor API
  slug: doconda-com-editor-api
- baseURL: https://api.eu.doconda.com/v1
  baseurl_source: declared
  description: 'Your own files: convert them, or use them as a source or to edit.'
  name: doconda-com Files API
  slug: doconda-com-files-api
- baseURL: https://api.eu.doconda.com/v1
  baseurl_source: declared
  description: Be notified when a document is ready.
  name: doconda-com Webhooks API
  slug: doconda-com-webhooks-api
artifact_total: 14
common:
- group: agent
  href: https://artifacts.apis.io/doconda-com/agentic-access/doconda-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/doconda-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/doconda-com/rate-limits/doconda-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/doconda-com-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/doconda-com/rules/doconda-com-rules.yml
  title: ''
  type: Spectral
  url: rules/doconda-com-rules.yml
- group: design
  href: https://artifacts.apis.io/doconda-com/json-ld/doconda-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/doconda-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/doconda-com/vocabulary/doconda-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/doconda-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/doconda-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/doconda-com/data-model/doconda-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/doconda-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/doconda-com/conventions/doconda-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/doconda-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/doconda-com/conventions/doconda-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/doconda-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/doconda-com/authentication/doconda-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/doconda-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/doconda-com/lifecycle/doconda-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/doconda-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/doconda-com/errors/doconda-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/doconda-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/doconda-com/conformance/doconda-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/doconda-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/doconda-com/llms/doconda-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/doconda-com-llms.txt
- group: other
  href: https://artifacts.apis.io/doconda-com/a2a/doconda-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/doconda-com-a2a.yml
- group: build
  href: https://artifacts.apis.io/doconda-com/mcp/doconda-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/doconda-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/doconda-com/mcp/doconda-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/doconda-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/doconda-com/well-known/doconda-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/doconda-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/doconda-com/hosts/doconda-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/doconda-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/doconda-com/vendors/doconda-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/doconda-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/doconda-com/packages/doconda-com-packages.yml
  title: ''
  type: Packages
  url: packages/doconda-com-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://doconda.com/status
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@doconda/sdk
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.doconda.com/changelog
- group: auth
  href: https://artifacts.apis.io/doconda-com/security/doconda-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/doconda-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://doconda.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.doconda.com/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.doconda.com/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.doconda.com/quickstart
- group: operate
  title: ''
  type: Support
  url: https://doconda.com/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/B-C-Software
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.doconda.com/guides/account
- group: start
  title: ''
  type: SignUp
  url: https://doconda.com/app/login?mode=signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://doconda.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://doconda.com/privacy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://docs.doconda.com/openapi.json
  - status: null
    url: https://docs.doconda.com/mcp
  - status: 401
    url: https://doconda.com/mcp
  - status: 401
    url: https://api.eu.doconda.com/mcp
  - status: 200
    url: https://doconda.com/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: Doconda provides an API that generates, converts, and edits Word, PowerPoint, Excel, and PDF documents. Users can create documents from a single sentence or Markdown, convert between formats, and edit existing files via simple API calls. The service offers a free tier of up to 1,000 conversions per month and tiered pricing for higher volumes. It is hosted in the European Union, supports OAuth2 bearer token authentication, and includes webhook notifications for background processing.
image: https://doconda.com/og-en.png
jsonld:
- class_count: 65
  name: Doconda Com Context
  property_count: 120
  slug: doconda-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at docs.doconda.com.
  name: doconda-com MCP Server
  slug: doconda-com-mcp-yml
modified: '2026-10-30'
name: doconda-com
nav: Providers
network: true
overview: 'doconda-com publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Dashboard API, Documents API, Editor API, and 2 more. Tagged areas include Document Generation, API, Conversion, Automation, and AI.


  The doconda-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  doconda-com''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, support, pricing, and 28 more developer resources.'
random_paper: 12
rate_limits:
- limit_count: 1
  name: Doconda Com Rate Limits
  slug: doconda-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: doconda-com API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: doconda-com-rules
scopes:
- name: Doconda Com Scopes
  scope_count: 0
  slug: doconda-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 58.9
  coverage:
    artifact_dirs: 26
    catalog_earned: 75.9
    catalog_earned_first_party: 0.0
    catalog_gap: 39.1
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 79.1
    contract_quality: 49.8
    developer_ergonomics: 58.8
    discoverability: 65.0
    operational_transparency: 55.8
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
  name: Doconda Com Authentication
  slug: doconda-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Doconda Com Domain Security
  slug: doconda-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: doconda-create-document
  slug: doconda-com-create-document
slug: doconda-com
tags:
- Document Generation
- API
- Conversion
- Automation
- AI
website: https://doconda.com/
---
