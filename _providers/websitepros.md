---
access_model:
  confidence: high
  label: Request Access
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://api-docs.intl.web.com/
  - https://nts.developer.azure-api.net
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.9
  scored_at: '2026-11-06'
api_count: 5
apis:
- baseURL: https://api.nts.web.com
  baseurl_source: declared
  description: Domain-name availability and suggestion.
  name: WebsitePros Domains API
  slug: websitepros-domains-api
- baseURL: https://api.nts.web.com
  baseurl_source: declared
  description: Gateway and service liveness.
  name: WebsitePros Health API
  slug: websitepros-health-api
- baseURL: https://api.nts.web.com
  baseurl_source: declared
  description: Create, read, update and delete sales orders in the Web.com International pipeline.
  name: WebsitePros Sales Orders API
  slug: websitepros-sales-orders-api
- baseURL: https://api.nts.web.com
  baseurl_source: declared
  description: Provision products and services against a customer and account.
  name: WebsitePros Service Orders API
  slug: websitepros-service-orders-api
- baseURL: https://api.nts.web.com
  baseurl_source: declared
  description: Generate a single-sign-on URL for a customer owned by your tenant.
  name: WebsitePros SSO API
  slug: websitepros-sso-api
artifact_total: 12
common:
- group: auth
  href: https://artifacts.apis.io/websitepros/security/websitepros-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/websitepros-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.web.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://nts.developer.azure-api.net
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.intl.web.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.intl.web.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://api-docs.intl.web.com/#getting-started
- group: start
  title: ''
  type: SignUp
  url: https://nts.developer.azure-api.net/signup
- group: build
  title: ''
  type: Postman
  url: https://api-docs.intl.web.com/
- group: build
  href: https://artifacts.apis.io/websitepros/collections/websitepros-international-platform.postman_collection.json
  title: ''
  type: PostmanCollection
  url: collections/websitepros-international-platform.postman_collection.json
- group: auth
  href: https://artifacts.apis.io/websitepros/authentication/websitepros-authentication.yml
  title: ''
  type: Authentication
  url: authentication/websitepros-authentication.yml
- group: design
  href: https://artifacts.apis.io/websitepros/conventions/websitepros-conventions.yml
  title: ''
  type: Conventions
  url: conventions/websitepros-conventions.yml
- group: design
  href: https://artifacts.apis.io/websitepros/errors/websitepros-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/websitepros-problem-types.yml
- group: design
  href: https://artifacts.apis.io/websitepros/lifecycle/websitepros-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/websitepros-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/websitepros/conformance/websitepros-conformance.yml
  title: ''
  type: Conformance
  url: conformance/websitepros-conformance.yml
- group: design
  href: https://artifacts.apis.io/websitepros/data-model/websitepros-data-model.yml
  title: ''
  type: DataModel
  url: data-model/websitepros-data-model.yml
- group: start
  href: https://artifacts.apis.io/websitepros/sandbox/websitepros-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/websitepros-sandbox.yml
- group: commercial
  href: https://artifacts.apis.io/websitepros/plans/websitepros-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/websitepros-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/websitepros/rate-limits/websitepros-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/websitepros-rate-limits.yml
- group: build
  href: https://artifacts.apis.io/websitepros/packages/websitepros-packages.yml
  title: ''
  type: Packages
  url: packages/websitepros-packages.yml
- group: agent
  href: https://artifacts.apis.io/websitepros/mcp/websitepros-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/websitepros-mcp.yml
- group: agent
  href: https://artifacts.apis.io/websitepros/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/websitepros/llms/websitepros-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/websitepros-llms.txt
- group: other
  href: https://artifacts.apis.io/websitepros/overlays/websitepros-international-platform-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/websitepros-international-platform-overlay.yaml
created: '2026-07-17'
description: 'WebsitePros, now operating as Web.com, is an American company that provides website building, web hosting, domain registration, e-commerce, and online marketing services primarily to small and medium-sized businesses. Website Pros, Inc. merged with Web.com in 2007 and adopted the Web.com name, and the business is now part of Newfold Digital, formed in 2021 from Endurance Web Presence and Web.com Group. It offers do-it-yourself and do-it-for-you website builders, managed WordPress hosting, professional email, SEO and digital marketing tools, and is headquartered in Jacksonville, Florida. Behind the retail brand it runs a real partner-facing B2B API — the Web.com International ("NTS") Platform API, fronted by Azure API Management at api.nts.web.com and documented publicly at api-docs.intl.web.com — through which approved resellers and sales partners create and manage sales orders, provision service orders, check domain availability and mint customer single-sign-on URLs. Access
  is not self-service: registration is reviewed and approved by the Web.com International team, separately for the production and development environments.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/websitepros.png
layout: provider
modified: '2026-08-13'
name: WebsitePros
nav: Providers
network: true
overview: 'WebsitePros is listed with 5 APIs on the [APIs.io](https://apis.io/) network, including Domains API, Health API, Sales Orders API, and 2 more. Tagged areas include Company, Website Builder, Web Hosting, Domains, and Small Business.


  The WebsitePros catalog on APIs.io includes 1 Spectral governance ruleset.


  WebsitePros'' developer surface includes documentation, API reference, getting-started guide, signup flow, authentication, sandbox, and 17 more developer resources.'
plans:
- name: Websitepros Plans Pricing
  plan_count: 0
  slug: websitepros-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Websitepros Rate Limits
  slug: websitepros-rate-limits
rules:
- authorship: generated
  effective_rule_count: 109
  extends:
  - spectral:oas
  name: WebsitePros API Rules
  rule_count: 68
  severity_counts:
    error: 66
    hint: 0
    info: 1
    warn: 1
  slug: websitepros-rules
score:
  band: thin
  composite: 27.0
  coverage:
    artifact_dirs: 23
    catalog_earned: 44.5
    catalog_earned_first_party: 0.0
    catalog_gap: 70.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    contract_governance: 18.2
    contract_quality: 15.9
    developer_ergonomics: 57.7
    discoverability: 71.4
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 27.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 6
      marker_coverage: 100.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/websitepros/websitepros-2026-09-02T170535.png
security:
- kind: authentication
  name: Websitepros Authentication
  slug: websitepros-authentication
  summary_line: apiKey/http/oauth2 · 5 schemes
- kind: domain-security
  name: Websitepros Domain Security
  slug: websitepros-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: websitepros-domain-availability
  slug: websitepros-domain-availability
- name: websitepros-sales-order-lifecycle
  slug: websitepros-sales-order-lifecycle
slug: websitepros
tags:
- Company
- Website Builder
- Web Hosting
- Domains
- Small Business
- Digital Marketing
- E-Commerce
- Reseller
- Sales Orders
- Provisioning
- SSO
- Azure API Management
website: https://www.web.com/
---
