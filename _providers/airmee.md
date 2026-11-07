---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 35.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.airmee.com/integration
  baseurl_source: declared
  description: The Collection Point Deliveries API from Airmee — 3 operation(s) for collection point deliveries.
  name: Airmee Collection Point Deliveries API
  slug: airmee-collection-point-deliveries-api
- baseURL: https://api.airmee.com/integration
  baseurl_source: declared
  description: The Home Deliveries API from Airmee — 6 operation(s) for home deliveries.
  name: Airmee Home Deliveries API
  slug: airmee-home-deliveries-api
- baseURL: https://api.airmee.com/integration
  baseurl_source: declared
  description: The Parcel Locker Deliveries API from Airmee — 3 operation(s) for parcel locker deliveries.
  name: Airmee Parcel Locker Deliveries API
  slug: airmee-parcel-locker-deliveries-api
- baseURL: https://api.airmee.com/integration
  baseurl_source: declared
  description: The Returns API from Airmee — 2 operation(s) for returns.
  name: Airmee Returns API
  slug: airmee-returns-api
artifact_total: 12
common:
- group: other
  href: https://artifacts.apis.io/airmee/capabilities/airmee-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/airmee-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://airmee.com/
- group: docs
  title: ''
  type: Documentation
  url: http://integration.docs.airmee.com.s3-website-eu-west-1.amazonaws.com/
- group: docs
  title: ''
  type: APIReference
  url: http://integration.docs.airmee.com.s3-website-eu-west-1.amazonaws.com/
- group: operate
  title: ''
  type: Support
  url: https://airmee.com/en/support/
- group: operate
  title: ''
  type: Contact
  url: https://airmee.com/en/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://airmee.com/en/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://airmee.com/en/news/
- group: company
  title: ''
  type: Careers
  url: https://careers.airmee.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://se.linkedin.com/company/airmee
- group: build
  title: ''
  type: SourceCode
  url: https://bitbucket.org/airmeedevs/
- group: auth
  href: https://artifacts.apis.io/airmee/authentication/airmee-authentication.yml
  title: ''
  type: Authentication
  url: authentication/airmee-authentication.yml
- group: design
  href: https://artifacts.apis.io/airmee/conventions/airmee-conventions.yml
  title: ''
  type: Conventions
  url: conventions/airmee-conventions.yml
- group: design
  href: https://artifacts.apis.io/airmee/errors/airmee-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/airmee-problem-types.yml
- group: design
  href: https://artifacts.apis.io/airmee/data-model/airmee-data-model.yml
  title: ''
  type: DataModel
  url: data-model/airmee-data-model.yml
- group: design
  href: https://artifacts.apis.io/airmee/lifecycle/airmee-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/airmee-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/airmee/conformance/airmee-conformance.yml
  title: ''
  type: Conformance
  url: conformance/airmee-conformance.yml
- group: build
  href: https://artifacts.apis.io/airmee/packages/airmee-packages.yml
  title: ''
  type: Packages
  url: packages/airmee-packages.yml
- group: build
  href: https://artifacts.apis.io/airmee/packages/airmee-packages.yml
  title: ''
  type: SDKs
  url: packages/airmee-packages.yml
- group: commercial
  href: https://artifacts.apis.io/airmee/plans/airmee-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/airmee-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/airmee/rate-limits/airmee-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/airmee-rate-limits.yml
- group: start
  href: https://artifacts.apis.io/airmee/sandbox/airmee-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/airmee-sandbox.yml
- group: other
  href: https://artifacts.apis.io/airmee/overlays/airmee-integration-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/airmee-integration-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/airmee/mcp/airmee-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/airmee-mcp.yml
- group: agent
  href: https://artifacts.apis.io/airmee/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/airmee/llms/airmee-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/airmee-llms.txt
- group: agent
  href: https://artifacts.apis.io/airmee/well-known/airmee-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/airmee-well-known.yml
- group: auth
  href: https://artifacts.apis.io/airmee/security/airmee-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/airmee-domain-security.yml
- group: other
  href: https://artifacts.apis.io/airmee/regulatory/airmee-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/airmee-regulatory-posture.yml
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://airmee.com/en/privacy-policy/
- group: operate
  title: ''
  type: IncidentNotification
  url: https://airmee.com/en/privacy-policy/
created: '2026-09-19'
description: Airmee is a Stockholm-based last-mile delivery company (founded 2018 by Julian Lee and Adrian Prelipcean) that runs same-day and next-day home delivery, outdoor parcel-locker delivery and label-less returns for e-commerce retailers across Sweden — Amazon, Apotea, Adlibris, Acne Studios, Sellpy and Meds among them — on a proprietary Smart Logistics Platform that route-optimises deliveries in real time and reports 99%+ fossil-free transport. Retailers and transport-administration (TA) systems integrate through the Airmee Integration API on api.airmee.com, a JWT-authenticated REST surface that quotes delivery intervals for a zip code at checkout, checks service-area availability and parcel size thresholds, lists nearby collection points and parcel lockers, books home / locker / collection-point deliveries and returns, and cancels a booking before pickup. A first-party PHP SDK and Magento 2 module are on Packagist, and partner-built WooCommerce and Shopify connectors exist.
image: https://airmee.com/assets/og-image.png
layout: provider
mcp_servers:
- description: MCP server requiring an API key; 12 tools listed. A candidate, not confirmed as published by the provider.
  name: Airmee MCP Server
  slug: airmee-mcp-yml
modified: '2026-09-19'
name: Airmee
nav: Providers
network: true
overview: 'Airmee publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Collection Point Deliveries API, Home Deliveries API, Parcel Locker Deliveries API, and 1 more. Tagged areas include Logistics, Last Mile Delivery, Shipping, Parcel Delivery, and Parcel Lockers.


  The Airmee catalog on APIs.io includes 1 Spectral governance ruleset.


  Airmee''s developer surface includes documentation, API reference, support, engineering blog, authentication, sandbox, and 25 more developer resources.'
plans:
- name: Airmee Plans Pricing
  plan_count: 0
  slug: airmee-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Airmee Rate Limits
  slug: airmee-rate-limits
rules:
- authorship: generated
  effective_rule_count: 107
  extends:
  - spectral:oas
  name: Airmee API Rules
  rule_count: 66
  severity_counts:
    error: 64
    hint: 0
    info: 1
    warn: 1
  slug: airmee-rules
score:
  band: thin
  composite: 35.1
  coverage:
    artifact_dirs: 25
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    contract_governance: 13.6
    contract_quality: 52.7
    developer_ergonomics: 51.8
    discoverability: 73.2
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - sweden
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - nordics
  previous_composite: 35.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 24.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/airmee/airmee-2026-10-11T093428.png
security:
- kind: authentication
  name: Airmee Authentication
  slug: airmee-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Airmee Domain Security
  slug: airmee-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 2
skills:
- name: Book an Airmee home delivery
  slug: airmee-book-a-home-delivery
- name: Offer Airmee locker or collection-point delivery
  slug: airmee-offer-locker-and-collection-point-delivery
slug: airmee
tags:
- Logistics
- Last Mile Delivery
- Shipping
- Parcel Delivery
- Parcel Lockers
- Returns
- E-Commerce
- Same-Day Delivery
- Sweden
- Carrier
website: https://airmee.com/
---
