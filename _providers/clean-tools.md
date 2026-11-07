---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 25.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 40
  human_in_the_loop: 2
  name: Clean Tools Agentic Access
  operation_count: 42
  slug: clean-tools-agentic-access
  summary_line: 42 operations · 40 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.clean.tools
  baseurl_source: declared
  description: Color conversion, palettes, and accessibility — deterministic.
  name: Clean.tools Color API
  slug: clean-tools-color-api
- baseURL: https://api.clean.tools
  baseurl_source: declared
  description: Structured-data conversion and validation — deterministic.
  name: Clean.tools Data API
  slug: clean-tools-data-api
- baseURL: https://api.clean.tools
  baseurl_source: declared
  description: Cron, RRULE, timezone, and timestamp tools — deterministic.
  name: Clean.tools Datetime API
  slug: clean-tools-datetime-api
- baseURL: https://api.clean.tools
  baseurl_source: declared
  description: Hashing, encoding, JWT, regex, and ID tools.
  name: Clean.tools Developer API
  slug: clean-tools-developer-api
- baseURL: https://api.clean.tools
  baseurl_source: declared
  description: Loan, interest, and percentage math — deterministic.
  name: Clean.tools Finance API
  slug: clean-tools-finance-api
- baseURL: https://api.clean.tools
  baseurl_source: declared
  description: Cryptographically random generators (NOT deterministic).
  name: Clean.tools Random API
  slug: clean-tools-random-api
- baseURL: https://api.clean.tools
  baseurl_source: declared
  description: Text analysis and transformation — deterministic.
  name: Clean.tools Text API
  slug: clean-tools-text-api
artifact_total: 13
common:
- group: agent
  href: https://artifacts.apis.io/clean-tools/agentic-access/clean-tools-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/clean-tools-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/clean-tools/rules/clean-tools-rules.yml
  title: ''
  type: Spectral
  url: rules/clean-tools-rules.yml
- group: design
  href: https://artifacts.apis.io/clean-tools/json-ld/clean-tools-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/clean-tools-context.jsonld
- group: design
  href: https://artifacts.apis.io/clean-tools/vocabulary/clean-tools-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/clean-tools-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/clean-tools/data-model/clean-tools-data-model.yml
  title: ''
  type: DataModel
  url: data-model/clean-tools-data-model.yml
- group: auth
  title: ''
  type: Security
  url: https://clean.tools/privacy/
- group: design
  href: https://artifacts.apis.io/clean-tools/errors/clean-tools-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/clean-tools-problem-types.yml
- group: design
  href: https://artifacts.apis.io/clean-tools/conformance/clean-tools-conformance.yml
  title: ''
  type: Conformance
  url: conformance/clean-tools-conformance.yml
- group: agent
  href: https://artifacts.apis.io/clean-tools/llms/clean-tools-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/clean-tools-llms.txt
- group: agent
  href: https://artifacts.apis.io/clean-tools/mcp/clean-tools-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/clean-tools-mcp.yml
- group: auth
  href: https://artifacts.apis.io/clean-tools/well-known/clean-tools-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/clean-tools-security.txt
- group: agent
  href: https://artifacts.apis.io/clean-tools/well-known/clean-tools-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/clean-tools-well-known.yml
- group: other
  href: https://artifacts.apis.io/clean-tools/hosts/clean-tools-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clean-tools-hosts.yml
- group: other
  href: https://artifacts.apis.io/clean-tools/vendors/clean-tools-vendors.yml
  title: ''
  type: Vendors
  url: vendors/clean-tools-vendors.yml
- group: build
  href: https://artifacts.apis.io/clean-tools/packages/clean-tools-packages.yml
  title: ''
  type: SDKs
  url: packages/clean-tools-packages.yml
- group: build
  href: https://artifacts.apis.io/clean-tools/packages/clean-tools-packages.yml
  title: ''
  type: Packages
  url: packages/clean-tools-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://clean.tools/changelog/
- group: auth
  href: https://artifacts.apis.io/clean-tools/security/clean-tools-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/clean-tools-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/clean-tools/security/clean-tools-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clean-tools-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://clean.tools/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://clean.tools/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://clean.tools/developers/
- group: docs
  title: ''
  type: APIReference
  url: https://clean.tools/developers/
- group: start
  title: ''
  type: GettingStarted
  url: https://clean.tools/developers/
- group: operate
  title: ''
  type: Support
  url: mailto:support@clean.tools
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://clean.tools/privacy/
created: '2026-11-03'
description: Clean.tools offers private, browser‑based tools that run entirely on your device. It provides fast image resizing, file conversion, text utilities, finance calculators, time tools, and fun utilities without any uploads, accounts, or tracking. The service emphasizes privacy, running all processing locally in the browser, and aims to give users a secure, ad‑free experience.
image: https://clean.tools/assets/images/og-image.png
jsonld:
- class_count: 2
  name: Clean Tools Context
  property_count: 3
  slug: clean-tools-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.clean.tools.
  name: Clean.tools MCP Server
  slug: clean-tools-mcp-yml
modified: '2026-11-03'
name: Clean.tools
nav: Providers
network: true
overview: 'Clean.tools publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Color API, Data API, Datetime API, and 4 more. Tagged areas include Browser, Privacy, Tools, Image, and Conversion.


  The Clean.tools catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Clean.tools'' developer surface includes changelog, documentation, API reference, getting-started guide, support, and 21 more developer resources.'
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 91
  extends:
  - spectral:oas
  name: Clean.tools API Rules
  rule_count: 50
  severity_counts:
    error: 48
    hint: 0
    info: 1
    warn: 1
  slug: clean-tools-rules
score:
  band: thin
  composite: 31.9
  coverage:
    artifact_dirs: 18
    catalog_earned: 47.8
    catalog_earned_first_party: 0.0
    catalog_gap: 67.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 5.3
    contract_governance: 22.0
    contract_quality: 52.9
    developer_ergonomics: 31.0
    discoverability: 65.0
    operational_transparency: 13.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Clean Tools Domain Security
  slug: clean-tools-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Clean Tools Vulnerability Disclosure
  slug: clean-tools-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: clean-tools
tags:
- Browser
- Privacy
- Tools
- Image
- Conversion
website: https://clean.tools/
---
