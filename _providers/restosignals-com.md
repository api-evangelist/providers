---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 38.3
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 16
  human_in_the_loop: 2
  name: Restosignals Com Agentic Access
  operation_count: 31
  slug: restosignals-com-agentic-access
  summary_line: 31 operations · 16 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.restosignals.com
  baseurl_source: declared
  description: The Account API from restosignals-com — 1 operation(s) for account.
  name: restosignals-com Account API
  slug: restosignals-com-account-api
- baseURL: https://api.restosignals.com
  baseurl_source: declared
  description: The Auth API from restosignals-com — 7 operation(s) for auth.
  name: restosignals-com Auth API
  slug: restosignals-com-auth-api
- baseURL: https://api.restosignals.com
  baseurl_source: declared
  description: The Billing API from restosignals-com — 2 operation(s) for billing.
  name: restosignals-com Billing API
  slug: restosignals-com-billing-api
- baseURL: https://api.restosignals.com
  baseurl_source: declared
  description: The Config API from restosignals-com — 1 operation(s) for config.
  name: restosignals-com Config API
  slug: restosignals-com-config-api
- baseURL: https://api.restosignals.com
  baseurl_source: declared
  description: The export API from restosignals-com — 1 operation(s) for export.
  name: restosignals-com Export API
  slug: restosignals-com-export-api
- baseURL: https://api.restosignals.com
  baseurl_source: declared
  description: The Health API from restosignals-com — 1 operation(s) for health.
  name: restosignals-com Health API
  slug: restosignals-com-health-api
- baseURL: https://api.restosignals.com
  baseurl_source: declared
  description: The Keys API from restosignals-com — 2 operation(s) for keys.
  name: restosignals-com Keys API
  slug: restosignals-com-keys-api
- baseURL: https://api.restosignals.com
  baseurl_source: declared
  description: The Mcp API from restosignals-com — 1 operation(s) for mcp.
  name: restosignals-com MCP API
  slug: restosignals-com-mcp-api
- baseURL: https://api.restosignals.com
  baseurl_source: declared
  description: The Me API from restosignals-com — 1 operation(s) for me.
  name: restosignals-com Me API
  slug: restosignals-com-me-api
- baseURL: https://api.restosignals.com
  baseurl_source: declared
  description: The openings API from restosignals-com — 5 operation(s) for openings.
  name: restosignals-com Openings API
  slug: restosignals-com-openings-api
- baseURL: https://api.restosignals.com
  baseurl_source: declared
  description: The Register API from restosignals-com — 1 operation(s) for register.
  name: restosignals-com Register API
  slug: restosignals-com-register-api
- baseURL: https://api.restosignals.com
  baseurl_source: declared
  description: The signals API from restosignals-com — 1 operation(s) for signals.
  name: restosignals-com Signals API
  slug: restosignals-com-signals-api
- baseURL: https://api.restosignals.com
  baseurl_source: declared
  description: The Usage API from restosignals-com — 1 operation(s) for usage.
  name: restosignals-com Usage API
  slug: restosignals-com-usage-api
- baseURL: https://api.restosignals.com
  baseurl_source: declared
  description: The Webhooks API from restosignals-com — 4 operation(s) for webhooks.
  name: restosignals-com Webhooks API
  slug: restosignals-com-webhooks-api
artifact_total: 26
common:
- group: agent
  href: https://artifacts.apis.io/restosignals-com/agentic-access/restosignals-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/restosignals-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/restosignals-com/plans/restosignals-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/restosignals-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/restosignals-com/rules/restosignals-com-rules.yml
  title: ''
  type: Spectral
  url: rules/restosignals-com-rules.yml
- group: design
  href: https://artifacts.apis.io/restosignals-com/json-ld/restosignals-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/restosignals-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/restosignals-com/vocabulary/restosignals-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/restosignals-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/restosignals-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/restosignals-com/data-model/restosignals-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/restosignals-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/restosignals-com/authentication/restosignals-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/restosignals-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/restosignals-com/errors/restosignals-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/restosignals-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/restosignals-com/conformance/restosignals-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/restosignals-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/restosignals-com/llms/restosignals-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/restosignals-com-llms.txt
- group: build
  href: https://artifacts.apis.io/restosignals-com/mcp/restosignals-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/restosignals-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/restosignals-com/mcp/restosignals-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/restosignals-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/restosignals-com/well-known/restosignals-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/restosignals-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/restosignals-com/hosts/restosignals-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/restosignals-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/restosignals-com/vendors/restosignals-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/restosignals-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/restosignals-com/security/restosignals-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/restosignals-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://restosignals.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://restosignals.com/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://restosignals.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://restosignals.com/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://restosignals.com/docs/
- group: operate
  title: ''
  type: Support
  url: https://restosignals.com/contact
- group: company
  title: ''
  type: Blog
  url: https://restosignals.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://restosignals.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://restosignals.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://restosignals.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://restosignals.com/privacy
created: '2026-10-31'
description: RestoSignals provides pre‑opening restaurant leads by aggregating public government data such as liquor licenses, permits and business filings across multiple US states. The service fuses these signals into a single scored venue, delivering clean JSON that can be integrated into CRMs or other workflows. Users can query the REST API to retrieve openings, filter by state, score thresholds, and limit results. Pricing includes a free tier with 100 trial leads and paid plans for unlimited access. The platform also offers a developer portal with documentation, API reference, and support resources.
image: https://restosignals.com/og-restosignals.png
jsonld:
- class_count: 2
  name: Restosignals Com Context
  property_count: 6
  slug: restosignals-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.restosignals.com.
  name: restosignals-com MCP Server
  slug: restosignals-com-mcp-yml
modified: '2026-10-31'
name: restosignals-com
nav: Providers
network: true
overview: 'restosignals-com publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Auth API, Billing API, and 11 more. Tagged areas include Restaurant, Data, API, MCP, and Lead Generation.


  The restosignals-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  restosignals-com''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 21 more developer resources.'
plans:
- name: Restosignals Com Plans Pricing
  plan_count: 2
  slug: restosignals-com-plans-pricing
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: restosignals-com API Rules
  rule_count: 11
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 0
  slug: restosignals-com-rules
scopes:
- name: Restosignals Com Scopes
  scope_count: 0
  slug: restosignals-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 52.9
  coverage:
    artifact_dirs: 23
    catalog_earned: 67.2
    catalog_earned_first_party: 0.0
    catalog_gap: 47.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.7
    contract_governance: 70.9
    contract_quality: 38.4
    developer_ergonomics: 63.6
    discoverability: 65.0
    operational_transparency: 0.0
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
  name: Restosignals Com Authentication
  slug: restosignals-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Restosignals Com Domain Security
  slug: restosignals-com-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 4
skills:
- name: coverage
  slug: coverage
- name: new-openings
  slug: new-openings
- name: venue-signals
  slug: venue-signals
- name: watch-area
  slug: watch-area
slug: restosignals-com
tags:
- Restaurant
- Data
- API
- MCP
- Lead Generation
website: https://restosignals.com/
---
