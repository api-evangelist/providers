---
access_model:
  confidence: medium
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
  band: agent-aware
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.3
  scored_at: '2026-09-07'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Edmunds Agentic Access
  operation_count: 5
  slug: edmunds-agentic-access
  summary_line: 5 operations
api_count: 1
apis:
- description: The Edmunds Dealership API is a tool that provides real-time access to data on cars for sale at dealerships across the country. By connecting to the API, users can search for specific makes and models
  name: Edmunds Dealership API
  slug: edmunds
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
  description: The only machine-readable contract Edmunds serves. An OpenAPI 3.0.1 document published at https://api.edmunds.com/openapi.yaml and pointed at by Edmunds' own OpenAI plugin manifest at /.well-known/ai-
  name: Edmunds Cars API
  slug: edmunds-cars-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Edmunds Vehicle API
  slug: open-edmunds-vehicle-api
- collection_type: open
  name: Edmunds Vehicle API
  slug: open-edmunds
common:
- group: company
  title: ''
  type: Website
  url: https://www.edmunds.com/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/edmunds-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/edmunds-domain-security.yml
- group: auth
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
  title: ''
  type: Packages
  url: packages/edmunds-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/edmunds-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/edmunds-well-known.yml
- group: build
  title: ''
  type: OpenAIPluginManifest
  url: well-known/edmunds-ai-plugin.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/edmunds-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/edmunds-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/edmunds-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/edmunds-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/edmunds-lifecycle.yml
- group: agent
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
- name: Edmunds Finops
  service_category: API
  slug: edmunds-finops
image: https://kinlane-productions2.s3.amazonaws.com/apis-json-icons/edmunds-developer-network-welcome-to-the-edmunds-api-edmunds-developer-portal.png
layout: provider
mcp_servers:
- description: ''
  name: Edmunds MCP Server
  slug: edmunds-mcp-server
modified: '2026-09-06'
name: Edmunds
nav: Providers
network: true
overview: 'Edmunds publishes 2 APIs on the [APIs.io](https://apis.io/) network: Vehicle API and Cars API. Tagged areas include Automobiles, Cars, Vehicles, Vehicle Data, and Dealerships.


  Edmunds'' developer surface includes authentication, developer portal, documentation, FAQ, engineering blog, API reference, support, and 19 more developer resources.'
plans:
- name: Edmunds Plans Pricing
  plan_count: 0
  slug: edmunds-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Edmunds Rate Limits
  slug: edmunds-rate-limits
score:
  band: thin
  composite: 29.5
  coverage:
    artifact_dirs: 21
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 4.5
    contract_quality: 22.1
    developer_ergonomics: 54.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 29.5
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
  schema_version: 0.20.0
  scored_at: '2026-09-07'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://raw.githubusercontent.com/api-evangelist/edmunds/refs/heads/main/screenshots/edmunds-2026-06-20T180456.png
security:
- kind: authentication
  name: Edmunds Authentication
  slug: edmunds-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Edmunds Domain Security
  slug: edmunds-domain-security
  summary_line: TLSv1.3 · DMARC
slug: edmunds
tags:
- Automobiles
- Cars
- Vehicles
- Vehicle Data
- Dealerships
- Reviews
- Pricing
- Automotive
website: https://www.edmunds.com/
---
