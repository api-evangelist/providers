---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: full
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 54.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Edgrapi Agentic Access
  operation_count: 33
  slug: edgrapi-agentic-access
  summary_line: 33 operations · 4 acting
api_count: 1
apis:
- description: The activist API from Paper and Beyond — 1 operation(s) for activist.
  name: Paper and Beyond Activist API
  slug: edgrapi-activist-api
- description: 8-K material events with parsed item codes.
  name: Paper and Beyond Events API
  slug: edgrapi-events-api
- description: Filing history & 10-K/10-Q sections.
  name: Paper and Beyond Filings API
  slug: edgrapi-filings-api
- description: Financial statements & ratios.
  name: Paper and Beyond Fundamentals API
  slug: edgrapi-fundamentals-api
- description: 'US government data beyond the SEC: federal contract opportunities and more.'
  name: Paper and Beyond Government API
  slug: edgrapi-government-api
- description: The holdings API from Paper and Beyond — 1 operation(s) for holdings.
  name: Paper and Beyond Holdings API
  slug: edgrapi-holdings-api
- description: Parsed Form 4 insider trades and the market-wide buy feed.
  name: Paper and Beyond Insider API
  slug: edgrapi-insider-api
- description: Health & discovery.
  name: Paper and Beyond Meta API
  slug: edgrapi-meta-api
- description: The reference API from Paper and Beyond — 2 operation(s) for reference.
  name: Paper and Beyond Reference API
  slug: edgrapi-reference-api
- description: The search API from Paper and Beyond — 1 operation(s) for search.
  name: Paper and Beyond Search API
  slug: edgrapi-search-api
- description: Get a signed POST the moment a watched company files.
  name: Paper and Beyond Webhooks API
  slug: edgrapi-webhooks-api
- description: The xbrl API from Paper and Beyond — 2 operation(s) for xbrl.
  name: Paper and Beyond Xbrl API
  slug: edgrapi-xbrl-api
artifact_total: 24
common:
- group: other
  href: https://artifacts.apis.io/edgrapi/capabilities/edgrapi-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/edgrapi-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/edgrapi/agentic-access/edgrapi-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/edgrapi-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/edgrapi/rate-limits/edgrapi-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/edgrapi-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/edgrapi/plans/edgrapi-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/edgrapi-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/edgrapi/rules/edgrapi-rules.yml
  title: ''
  type: Spectral
  url: rules/edgrapi-rules.yml
- group: design
  href: https://artifacts.apis.io/edgrapi/json-ld/edgrapi-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/edgrapi-context.jsonld
- group: design
  href: https://artifacts.apis.io/edgrapi/vocabulary/edgrapi-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/edgrapi-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/edgrapi/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/edgrapi/data-model/edgrapi-data-model.yml
  title: ''
  type: DataModel
  url: data-model/edgrapi-data-model.yml
- group: auth
  title: ''
  type: Security
  url: https://edgrapi.com/contact
- group: auth
  href: https://artifacts.apis.io/edgrapi/authentication/edgrapi-authentication.yml
  title: ''
  type: Authentication
  url: authentication/edgrapi-authentication.yml
- group: design
  href: https://artifacts.apis.io/edgrapi/errors/edgrapi-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/edgrapi-problem-types.yml
- group: design
  href: https://artifacts.apis.io/edgrapi/conformance/edgrapi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/edgrapi-conformance.yml
- group: agent
  href: https://artifacts.apis.io/edgrapi/llms/edgrapi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/edgrapi-llms.txt
- group: build
  href: https://artifacts.apis.io/edgrapi/mcp/edgrapi-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/edgrapi-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/edgrapi/mcp/edgrapi-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/edgrapi-mcp.yml
- group: auth
  href: https://artifacts.apis.io/edgrapi/well-known/edgrapi-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/edgrapi-security.txt
- group: auth
  href: https://artifacts.apis.io/edgrapi/well-known/edgrapi-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/edgrapi-api-security.txt
- group: agent
  href: https://artifacts.apis.io/edgrapi/well-known/edgrapi-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/edgrapi-well-known.yml
- group: other
  href: https://artifacts.apis.io/edgrapi/hosts/edgrapi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/edgrapi-hosts.yml
- group: other
  href: https://artifacts.apis.io/edgrapi/vendors/edgrapi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/edgrapi-vendors.yml
- group: build
  href: https://artifacts.apis.io/edgrapi/packages/edgrapi-packages.yml
  title: ''
  type: SDKs
  url: packages/edgrapi-packages.yml
- group: build
  href: https://artifacts.apis.io/edgrapi/packages/edgrapi-packages.yml
  title: ''
  type: Packages
  url: packages/edgrapi-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://edgrapi.com/status
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.edgrapi.com</code
- group: auth
  href: https://artifacts.apis.io/edgrapi/security/edgrapi-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/edgrapi-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/edgrapi/security/edgrapi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/edgrapi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://edgrapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://edgrapi.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://edgrapi.com/swagger
- group: start
  title: ''
  type: GettingStarted
  url: https://edgrapi.com/docs
- group: operate
  title: ''
  type: Support
  url: https://edgrapi.com/contact
- group: company
  title: ''
  type: Blog
  url: https://edgrapi.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://edgrapi.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://edgrapi.com/app
- group: commercial
  title: ''
  type: TermsOfService
  url: https://edgrapi.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://edgrapi.com/privacy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/edgrapi/workspace
created: '2026-10-16'
description: Paper and Beyond provides a US Government Data API for developers and AI agents, aggregating data from SAM.gov contracts, USAspending awards, Grants.gov, Congress trades, and SEC EDGAR into a single JSON schema. The service offers a hosted MCP server with a free tier, no credit card required, and supports REST access. It targets AI agents and developers needing comprehensive federal data via a unified API.
finops:
- has_sources: true
  method: derived
  name: Edgrapi Finops
  primary_unit: subscription
  service_category: ''
  slug: edgrapi-finops
  template: false
image: https://edgrapi.com/static/og-edgrapi.png
jsonld:
- class_count: 2
  name: Edgrapi Context
  property_count: 6
  slug: edgrapi-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.edgrapi.com requiring an API key.
  name: Paper and Beyond MCP Server
  slug: edgrapi-mcp-yml
modified: '2026-10-16'
name: Paper and Beyond
nav: Providers
network: true
overview: 'Paper and Beyond publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including Activist API, Events API, Filings API, and 9 more. Tagged areas include Company, Data, Government, and Artificial Intelligence.


  The Paper and Beyond catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Paper and Beyond''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 31 more developer resources.'
plans:
- name: Edgrapi Plans Pricing
  plan_count: 8
  slug: edgrapi-plans-pricing
- name: Edgrapi Price Estimates
  plan_count: 0
  slug: edgrapi-price-estimates
random_paper: 12
rate_limits:
- limit_count: 1
  name: Edgrapi Rate Limits
  slug: edgrapi-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Paper and Beyond API Rules
  rule_count: 14
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 2
  slug: edgrapi-rules
score:
  band: developing
  composite: 46.9
  coverage:
    artifact_dirs: 27
    catalog_earned: 60.8
    catalog_earned_first_party: 20.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.7
  facets:
    access_clarity: 61.8
    contract_governance: 22.0
    contract_quality: 45.8
    developer_ergonomics: 45.8
    discoverability: 58.3
    operational_transparency: 34.2
  previous_composite: 58.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/edgrapi/edgrapi-2026-11-03T131314.png
security:
- kind: authentication
  name: Edgrapi Authentication
  slug: edgrapi-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Edgrapi Domain Security
  slug: edgrapi-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Edgrapi Vulnerability Disclosure
  slug: edgrapi-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: edgrapi-webhook-create-test-delete
  slug: edgrapi-webhook-create-test-delete
slug: edgrapi
tags:
- Company
- Data
- Government
- Artificial Intelligence
website: https://edgrapi.com/
---
