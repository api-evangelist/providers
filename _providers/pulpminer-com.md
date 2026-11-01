---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 46.3
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Access your saved JSON APIs
  name: Pulpminer API
  slug: pulpminer-api
- baseURL: https://api.pulpminer.com
  baseurl_source: declared
  description: 'pulpminer-com API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: pulpminer-com API
  slug: pulpminer-com-api
artifact_total: 7
common:
- group: design
  href: https://artifacts.apis.io/pulpminer-com/rules/pulpminer-com-rules.yml
  title: ''
  type: Spectral
  url: rules/pulpminer-com-rules.yml
- group: design
  href: https://artifacts.apis.io/pulpminer-com/vocabulary/pulpminer-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/pulpminer-com-vocabulary.yml
- group: auth
  href: https://artifacts.apis.io/pulpminer-com/authentication/pulpminer-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/pulpminer-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/pulpminer-com/errors/pulpminer-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/pulpminer-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/pulpminer-com/conformance/pulpminer-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pulpminer-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/pulpminer-com/llms/pulpminer-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/pulpminer-com-llms.txt
- group: other
  href: https://artifacts.apis.io/pulpminer-com/a2a/pulpminer-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/pulpminer-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/pulpminer-com/mcp/pulpminer-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/pulpminer-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/pulpminer-com/well-known/pulpminer-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/pulpminer-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/pulpminer-com/hosts/pulpminer-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pulpminer-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/pulpminer-com/vendors/pulpminer-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pulpminer-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/pulpminer-com/packages/pulpminer-com-packages.yml
  title: ''
  type: SDKs
  url: packages/pulpminer-com-packages.yml
- group: build
  href: https://artifacts.apis.io/pulpminer-com/packages/pulpminer-com-packages.yml
  title: ''
  type: Packages
  url: packages/pulpminer-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pulpminer.com/terms-and-conditions
- group: start
  title: ''
  type: Sandbox
  url: https://www.pulpminer.com/playground
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pulpminer.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://accounts.pulpminer.com/sign-in
- group: company
  title: ''
  type: Blog
  url: https://www.pulpminer.com/blog
- group: auth
  href: https://artifacts.apis.io/pulpminer-com/security/pulpminer-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pulpminer-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pulpminer.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pulpminer.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.pulpminer.com/api-reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.pulpminer.com/quickstart.md
- group: operate
  title: ''
  type: Support
  url: mailto:hello@pulpminer.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.pulpminer.com/#pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.pulpminer.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.pulpminer.com/
coverage:
  checked: '2026-10-31'
  detail: Documentation pages describe API endpoints but no OpenAPI/AsyncAPI/GraphQL spec is provided.
  evidence:
  - status: 200
    url: https://docs.pulpminer.com/api-reference/endpoints/external-api.md
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: Turn Any webpage into a clean, structured realtime JSON API in seconds with PulpMiner. No scraping code required—just enter a URL and your desired JSON format. Get real-time, AI-powered APIs with flexible pricing and instant setup.
image: https://res.cloudinary.com/dkn197fqs/image/upload/q_auto,f_auto,w/400/v1746916904/logo_1_yzn1z4.png
layout: provider
mcp_servers:
- description: Remote MCP server at docs.pulpminer.com.
  name: pulpminer-com MCP Server
  slug: pulpminer-com-mcp-yml
modified: '2026-10-31'
name: pulpminer-com
nav: Providers
network: true
overview: 'pulpminer-com is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include API, Web Scraping, Realtime, JSON, and Low-code.


  The pulpminer-com catalog on APIs.io includes 1 Spectral governance ruleset.


  pulpminer-com''s developer surface includes authentication, sandbox, engineering blog, documentation, API reference, getting-started guide, support, and 20 more developer resources.'
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: pulpminer-com API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: pulpminer-com-rules
scopes:
- name: Pulpminer Com Scopes
  scope_count: 0
  slug: pulpminer-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 54.1
  coverage:
    artifact_dirs: 21
    catalog_earned: 57.7
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 79.1
    contract_quality: 39.8
    developer_ergonomics: 71.4
    discoverability: 65.0
    operational_transparency: 15.8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Pulpminer Com Authentication
  slug: pulpminer-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Pulpminer Com Domain Security
  slug: pulpminer-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: pulpminer-com
tags:
- API
- Web Scraping
- Realtime
- JSON
- Low-code
website: https://pulpminer.com/
---
