---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: self
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 40.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 17
  human_in_the_loop: 1
  name: Ace Bl Tech Agentic Access
  operation_count: 38
  slug: ace-bl-tech-agentic-access
  summary_line: 38 operations · 17 acting · 1 human-in-the-loop
api_count: 2
apis:
- baseURL: https://ace-bl.tech
  baseurl_source: declared
  description: The Agent API from Ace AI Assistant — 13 operation(s) for agent.
  name: Ace AI Assistant Agent API
  slug: ace-bl-tech-agent-api
- baseURL: https://tryacee.com
  baseurl_source: declared
  description: The Apps API from Ace AI Assistant — 4 operation(s) for apps.
  name: Ace AI Assistant Apps API
  slug: ace-bl-tech-apps-api
- baseURL: https://tryacee.com
  baseurl_source: declared
  description: The Catalog API from Ace AI Assistant — 1 operation(s) for catalog.
  name: Ace AI Assistant Catalog API
  slug: ace-bl-tech-catalog-api
- baseURL: https://tryacee.com
  baseurl_source: declared
  description: The Connections API from Ace AI Assistant — 2 operation(s) for connections.
  name: Ace AI Assistant Connections API
  slug: ace-bl-tech-connections-api
- baseURL: https://tryacee.com
  baseurl_source: declared
  description: The Custom Connectors API from Ace AI Assistant — 2 operation(s) for custom connectors.
  name: Ace AI Assistant Custom Connectors API
  slug: ace-bl-tech-custom-connectors-api
- baseURL: https://tryacee.com
  baseurl_source: declared
  description: The Events API from Ace AI Assistant — 1 operation(s) for events.
  name: Ace AI Assistant Events API
  slug: ace-bl-tech-events-api
- baseURL: https://ace-bl.tech
  baseurl_source: declared
  description: The Mcp API from Ace AI Assistant — 1 operation(s) for mcp.
  name: Ace AI Assistant MCP API
  slug: ace-bl-tech-mcp-api
- baseURL: https://tryacee.com
  baseurl_source: declared
  description: The Me API from Ace AI Assistant — 1 operation(s) for me.
  name: Ace AI Assistant Me API
  slug: ace-bl-tech-me-api
- baseURL: https://tryacee.com
  baseurl_source: declared
  description: The Runs API from Ace AI Assistant — 1 operation(s) for runs.
  name: Ace AI Assistant Runs API
  slug: ace-bl-tech-runs-api
- baseURL: https://tryacee.com
  baseurl_source: declared
  description: The Tools API from Ace AI Assistant — 4 operation(s) for tools.
  name: Ace AI Assistant Tools API
  slug: ace-bl-tech-tools-api
- baseURL: https://tryacee.com
  baseurl_source: declared
  description: The Triggers API from Ace AI Assistant — 3 operation(s) for triggers.
  name: Ace AI Assistant Triggers API
  slug: ace-bl-tech-triggers-api
artifact_total: 22
common:
- group: agent
  href: https://artifacts.apis.io/ace-bl-tech/agentic-access/ace-bl-tech-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ace-bl-tech-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/ace-bl-tech/plans/ace-bl-tech-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ace-bl-tech-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/ace-bl-tech/rules/ace-bl-tech-rules.yml
  title: ''
  type: Spectral
  url: rules/ace-bl-tech-rules.yml
- group: design
  href: https://artifacts.apis.io/ace-bl-tech/json-ld/ace-bl-tech-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ace-bl-tech-context.jsonld
- group: design
  href: https://artifacts.apis.io/ace-bl-tech/vocabulary/ace-bl-tech-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ace-bl-tech-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/ace-bl-tech/data-model/ace-bl-tech-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ace-bl-tech-data-model.yml
- group: design
  href: https://artifacts.apis.io/ace-bl-tech/conventions/ace-bl-tech-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/ace-bl-tech-conventions.yml
- group: design
  href: https://artifacts.apis.io/ace-bl-tech/conventions/ace-bl-tech-conventions.yml
  title: ''
  type: Conventions
  url: conventions/ace-bl-tech-conventions.yml
- group: design
  href: https://artifacts.apis.io/ace-bl-tech/errors/ace-bl-tech-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ace-bl-tech-problem-types.yml
- group: design
  href: https://artifacts.apis.io/ace-bl-tech/conformance/ace-bl-tech-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ace-bl-tech-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ace-bl-tech/llms/ace-bl-tech-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ace-bl-tech-llms.txt
- group: agent
  href: https://artifacts.apis.io/ace-bl-tech/mcp/ace-bl-tech-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/ace-bl-tech-mcp.yml
- group: auth
  href: https://artifacts.apis.io/ace-bl-tech/well-known/ace-bl-tech-tryacee-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ace-bl-tech-tryacee-security.txt
- group: auth
  href: https://artifacts.apis.io/ace-bl-tech/well-known/ace-bl-tech-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ace-bl-tech-security.txt
- group: agent
  href: https://artifacts.apis.io/ace-bl-tech/well-known/ace-bl-tech-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ace-bl-tech-well-known.yml
- group: other
  href: https://artifacts.apis.io/ace-bl-tech/hosts/ace-bl-tech-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ace-bl-tech-hosts.yml
- group: other
  href: https://artifacts.apis.io/ace-bl-tech/vendors/ace-bl-tech-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ace-bl-tech-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tryacee.com/terms
- group: auth
  title: ''
  type: Security
  url: https://tryacee.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tryacee.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://tryacee.com/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://tryacee.com/security/release-notes
- group: auth
  href: https://artifacts.apis.io/ace-bl-tech/authentication/ace-bl-tech-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ace-bl-tech-authentication.yml
- group: auth
  href: https://artifacts.apis.io/ace-bl-tech/security/ace-bl-tech-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/ace-bl-tech-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/ace-bl-tech/security/ace-bl-tech-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ace-bl-tech-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ace-bl.tech/
- group: docs
  title: ''
  type: Documentation
  url: https://tryacee.com/developers
- group: start
  title: ''
  type: DeveloperPortal
  url: https://tryacee.com/
- group: operate
  title: ''
  type: Support
  url: https://tryacee.com/support
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://ace-bl.tech/openapi.json
  - status: null
    url: https://ace-bl.tech/mcp
  - status: null
    url: https://tryacee.com/openapi.json
  - status: 401
    url: https://tryacee.com/mcp
  - status: 200
    url: https://ace-bl.tech/
  reason: partner-login
  state: gated
created: '2026-10-31'
description: Ace AI Assistant provides an AI‑powered personal assistant for macOS, Windows, iPhone, and iPad. It captures screen content, transcribes speech, generates notes, flashcards, and helps draft documents across popular apps. Users can access the service via desktop apps, a web portal, and mobile apps, with flexible credit‑based pricing plans. The platform emphasizes privacy, offering optional integration with existing AI subscriptions like Claude, ChatGPT, or Grok.
image: https://tryacee.com/ace-home/og/og-dark-blue-1200x630.jpg
json_schemas:
- name: App
  property_count: 8
  slug: ace-bl-tech-app
- name: Run
  property_count: 6
  slug: ace-bl-tech-run
- name: Tool
  property_count: 7
  slug: ace-bl-tech-tool
jsonld:
- class_count: 3
  name: Ace Bl Tech Context
  property_count: 17
  slug: ace-bl-tech-context
layout: provider
mcp_servers:
- description: Remote MCP server at ace-bl.tech.
  name: Ace AI Assistant MCP Server
  slug: ace-bl-tech-mcp-yml
modified: '2026-10-31'
name: Ace AI Assistant
nav: Providers
network: true
overview: 'Ace AI Assistant publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent API, Apps API, Catalog API, and 8 more. Tagged areas include Artificial Intelligence, Productivity, Assistant, macOS, and Windows.


  The Ace AI Assistant catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Ace AI Assistant''s developer surface includes pricing, changelog, authentication, documentation, support, and 24 more developer resources.'
plans:
- name: Ace Bl Tech Plans Pricing
  plan_count: 9
  slug: ace-bl-tech-plans-pricing
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Ace AI Assistant API Rules
  rule_count: 11
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 2
  slug: ace-bl-tech-rules
score:
  band: developing
  composite: 40.9
  coverage:
    artifact_dirs: 21
    catalog_earned: 71.8
    catalog_earned_first_party: 12.0
    catalog_gap: 43.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.8
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 57.5
    developer_ergonomics: 23.8
    discoverability: 65.0
    operational_transparency: 13.2
  previous_composite: 48.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Ace Bl Tech Authentication
  slug: ace-bl-tech-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Ace Bl Tech Domain Security
  slug: ace-bl-tech-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Ace Bl Tech Vulnerability Disclosure
  slug: ace-bl-tech-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ace-bl-tech
tags:
- Artificial Intelligence
- Productivity
- Assistant
- macOS
- Windows
- iOS
website: https://ace-bl.tech/
---
