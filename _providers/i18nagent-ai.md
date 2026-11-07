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
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.2
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: The i18n Agent Translation API provides AI‑powered localization across 45 languages, supporting JSON, YAML, XML, CSV, Markdown and other formats. It offers real‑time streaming, credit‑based pay‑as‑you
  name: i18n Agent Translation API
  slug: translation-api
- description: 'i18nagent-ai API as documented publicly: 15 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: i18nagent-ai API
  slug: i18nagent-ai-api
artifact_total: 9
common:
- group: design
  href: https://artifacts.apis.io/i18nagent-ai/rules/i18nagent-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/i18nagent-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/i18nagent-ai/vocabulary/i18nagent-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/i18nagent-ai-vocabulary.yml
- group: build
  href: https://artifacts.apis.io/i18nagent-ai/cli/i18nagent-ai-cli.yml
  title: ''
  type: CLI
  url: cli/i18nagent-ai-cli.yml
- group: design
  href: https://artifacts.apis.io/i18nagent-ai/conventions/i18nagent-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/i18nagent-ai-conventions.yml
- group: auth
  href: https://artifacts.apis.io/i18nagent-ai/authentication/i18nagent-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/i18nagent-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/i18nagent-ai/errors/i18nagent-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/i18nagent-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/i18nagent-ai/conformance/i18nagent-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/i18nagent-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/i18nagent-ai/llms/i18nagent-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/i18nagent-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/i18nagent-ai/mcp/i18nagent-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/i18nagent-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/i18nagent-ai/well-known/i18nagent-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/i18nagent-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/i18nagent-ai/hosts/i18nagent-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/i18nagent-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/i18nagent-ai/vendors/i18nagent-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/i18nagent-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/i18nagent-ai/packages/i18nagent-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/i18nagent-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/i18nagent-ai/packages/i18nagent-ai-packages.yml
  title: ''
  type: Packages
  url: packages/i18nagent-ai-packages.yml
- group: start
  title: ''
  type: Login
  url: https://auth.i18nagent.ai/auth/sign-in
- group: auth
  href: https://artifacts.apis.io/i18nagent-ai/security/i18nagent-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/i18nagent-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://i18nagent.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.i18nagent.ai/en
- group: docs
  title: ''
  type: APIReference
  url: https://api.i18nagent.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.i18nagent.ai/en
- group: start
  title: ''
  type: GettingStarted
  url: https://i18nagent.ai/en/quote
- group: company
  title: ''
  type: Blog
  url: https://i18nagent.ai/en/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://i18nagent.ai/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://i18nagent.ai/en/privacy
coverage:
  checked: '2026-10-31'
  detail: Documentation is publicly readable but no OpenAPI, AsyncAPI, GraphQL, or other machine‑readable spec is published.
  evidence:
  - status: 200
    url: https://docs.i18nagent.ai/en
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: i18n Agent provides an AI‑powered internationalization platform that translates JSON, YAML, XML, CSV, Markdown and other developer‑centric file formats into 45 languages with cultural adaptation. It offers a credit‑based pay‑as‑you‑go model, real‑time streaming translations, secure API‑key authentication, and MCP integration for IDEs such as VS Code, Claude Code and Cursor. The service targets developers building multilingual applications, enabling fast, high‑quality localization without agency costs.
image: https://i18nagent.ai/images/facebook-og.png
layout: provider
mcp_servers:
- description: Remote MCP server at api.i18nagent.ai.
  name: i18nagent-ai MCP Server
  slug: i18nagent-ai-mcp-yml
modified: '2026-10-30'
name: i18nagent-ai
nav: Providers
network: true
overview: 'i18nagent-ai is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Localization, Translation, and Developer Tools.


  The i18nagent-ai catalog on APIs.io includes 1 Spectral governance ruleset.


  i18nagent-ai''s developer surface includes CLI, authentication, documentation, API reference, getting-started guide, engineering blog, and 18 more developer resources.'
plans:
- name: I18Nagent Ai Plans Pricing
  plan_count: 0
  slug: i18nagent-ai-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: I18Nagent Ai Rate Limits
  slug: i18nagent-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: i18nagent-ai API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: i18nagent-ai-rules
scopes:
- name: I18Nagent Ai Scopes
  scope_count: 0
  slug: i18nagent-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 25.6
  coverage:
    artifact_dirs: 26
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.0
  facets:
    access_clarity: 17.1
    contract_governance: 22.0
    contract_quality: 10.5
    developer_ergonomics: 46.4
    discoverability: 56.7
    operational_transparency: 0.0
  previous_composite: 33.6
  provenance:
    conformance: derived
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
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/i18nagent-ai/i18nagent-ai-2026-11-03T133557.png
security:
- kind: authentication
  name: I18Nagent Ai Authentication
  slug: i18nagent-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: I18Nagent Ai Domain Security
  slug: i18nagent-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: i18nagent-ai
tags:
- Company
- Artificial Intelligence
- Localization
- Translation
- Developer Tools
- Software-as-a-Service
website: https://i18nagent.ai/
---
