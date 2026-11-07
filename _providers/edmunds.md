---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - finops
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Edmunds Agentic Access
  operation_count: 5
  slug: edmunds-agentic-access
  summary_line: 5 operations
api_count: 2
apis:
- description: The Edmunds Dealership API is a tool that provides real-time access to data on cars for sale at dealerships across the country. By connecting to the API, users can search for specific makes and models
  name: Edmunds Dealership API
  slug: edmunds-dealership-api
- description: 'Edmunds API is a robust software interface that provides access to a vast database of automotive information and data. With this API, users can access details on car specifications, pricing, reviews, '
  name: Edmunds API
  slug: edmunds
- baseURL: https://api.edmunds.com
  baseurl_source: declared
  description: The Vehicle API from Edmunds — 5 operation(s) for vehicle.
  name: Edmunds Vehicle API
  slug: edmunds-vehicle-api
- baseURL: https://api.edmunds.com
  baseurl_source: declared
  description: The Aiplugin API from Edmunds — 2 operation(s) for aiplugin.
  name: Edmunds Aiplugin API
  slug: edmunds-aiplugin-api
artifact_total: 16
collections:
- collection_type: open
  name: Edmunds Vehicle API
  slug: open-edmunds-vehicle-api
- collection_type: open
  name: Edmunds Vehicle API
  slug: open-edmunds
common:
- group: commercial
  href: https://artifacts.apis.io/edmunds/plans/edmunds-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/edmunds-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/edmunds/rate-limits/edmunds-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/edmunds-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/edmunds/finops/edmunds-finops.yml
  title: ''
  type: FinOps
  url: finops/edmunds-finops.yml
- group: other
  href: https://artifacts.apis.io/edmunds/overlays/edmunds-cars-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/edmunds-cars-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/edmunds/mcp/edmunds-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/edmunds-mcp.yml
- group: company
  title: ''
  type: Website
  url: https://www.edmunds.com/
- group: agent
  href: https://artifacts.apis.io/edmunds/agentic-access/edmunds-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/edmunds-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/edmunds/security/edmunds-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/edmunds-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/edmunds/authentication/edmunds-authentication.yml
  title: ''
  type: Authentication
  url: authentication/edmunds-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/edmunds
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/edmunds-com
- group: start
  title: ''
  type: Portal
  url: https://developer.edmunds.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.edmunds.com/terms_of_service.html
- group: docs
  title: ''
  type: Documentation
  url: https://developer.edmunds.com/api_branding_guide.html
- group: operate
  title: ''
  type: FAQ
  url: https://developer.edmunds.com/faq.html
- group: operate
  title: ''
  type: Contact
  url: https://developer.edmunds.com/contact_us.html
- group: build
  title: ''
  type: SDKs
  url: https://developer.edmunds.com/api-documentation/overview/#sec-9
- group: build
  href: https://artifacts.apis.io/edmunds/packages/edmunds-packages.yml
  title: ''
  type: Packages
  url: packages/edmunds-packages.yml
- group: build
  href: https://artifacts.apis.io/edmunds/packages/edmunds-packages.yml
  title: ''
  type: SDKs
  url: packages/edmunds-packages.yml
- group: agent
  href: https://artifacts.apis.io/edmunds/well-known/edmunds-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/edmunds-well-known.yml
- group: build
  href: https://artifacts.apis.io/edmunds/well-known/edmunds-ai-plugin.json
  title: ''
  type: OpenAIPluginManifest
  url: well-known/edmunds-ai-plugin.json
- group: agent
  href: https://artifacts.apis.io/edmunds/llms/edmunds-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/edmunds-llms.txt
- group: design
  href: https://artifacts.apis.io/edmunds/conventions/edmunds-conventions.yml
  title: ''
  type: Conventions
  url: conventions/edmunds-conventions.yml
- group: design
  href: https://artifacts.apis.io/edmunds/conformance/edmunds-conformance.yml
  title: ''
  type: Conformance
  url: conformance/edmunds-conformance.yml
- group: design
  href: https://artifacts.apis.io/edmunds/lifecycle/edmunds-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/edmunds-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/edmunds/lifecycle/edmunds-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/edmunds-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/edmunds/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Blog
  url: https://technology.edmunds.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.edmunds.com/api-documentation/overview/
- group: operate
  title: ''
  type: Support
  url: https://developer.edmunds.com/contact_us.html
- group: docs
  title: ''
  type: Documentation
  url: https://developer.edmunds.com/special_requirements.html
created: '2024-07-11T00:00:00.000Z'
description: Edmunds is a popular automotive resource website that provides consumers with valuable information and tools to help them make informed decisions about buying and selling cars. They offer expert reviews, comparison tools, price guides, and a variety of resources to help users research and find the perfect vehicle for their needs.
finops:
- has_sources: false
  method: generated
  name: Edmunds Finops
  primary_unit: request
  service_category: API
  slug: edmunds-finops
  template: true
image: https://kinlane-productions2.s3.amazonaws.com/apis-json-icons/edmunds-developer-network-welcome-to-the-edmunds-api-edmunds-developer-portal.png
layout: provider
mcp_servers:
- description: MCP server; 2 tools listed. A candidate, not confirmed as published by the provider.
  name: Edmunds MCP Server
  slug: edmunds-mcp-yml
modified: '2026-09-06'
name: Edmunds
nav: Providers
network: true
overview: 'Edmunds publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Vehicle API, Aiplugin API, and 2 more. Tagged areas include Automobiles, Cars, Vehicles, Vehicle Data, and Dealership.


  The Edmunds catalog on APIs.io includes 1 Spectral governance ruleset.


  Edmunds'' developer surface includes authentication, developer portal, documentation, FAQ, engineering blog, API reference, support, and 24 more developer resources.'
plans:
- name: Edmunds Plans Pricing
  plan_count: 0
  slug: edmunds-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Edmunds Rate Limits
  slug: edmunds-rate-limits
rules:
- authorship: generated
  effective_rule_count: 92
  extends:
  - spectral:oas
  name: Edmunds API Rules
  rule_count: 51
  severity_counts:
    error: 47
    hint: 0
    info: 3
    warn: 1
  slug: edmunds-rules
score:
  band: thin
  composite: 30.2
  coverage:
    artifact_dirs: 25
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.4
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 22.1
    developer_ergonomics: 54.2
    discoverability: 73.2
    operational_transparency: 10.5
  previous_composite: 29.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/edmunds/edmunds-2026-06-20T180456.png
security:
- kind: authentication
  name: Edmunds Authentication
  slug: edmunds-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Edmunds Domain Security
  slug: edmunds-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 2
skills:
- name: edmunds-find-local-inventory
  slug: edmunds-find-local-inventory
- name: edmunds-vehicle-expert-review
  slug: edmunds-vehicle-expert-review
slug: edmunds
tags:
- Automobiles
- Cars
- Vehicles
- Vehicle Data
- Dealership
- Reviews
- Pricing
- Automotive
website: https://www.edmunds.com/
---
