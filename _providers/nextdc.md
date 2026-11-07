---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 22
  human_in_the_loop: 0
  name: Nextdc Agentic Access
  operation_count: 43
  slug: nextdc-agentic-access
  summary_line: 43 operations · 22 acting
api_count: 1
apis:
- baseURL: https://sandbox-api.axonvx.com/api/biz2
  baseurl_source: declared
  description: The comments API from NEXTDC — 1 operation(s) for comments.
  name: NEXTDC Comments API
  slug: nextdc-comments-api
- baseURL: https://sandbox-api.axonvx.com/api/biz2
  baseurl_source: declared
  description: The discount API from NEXTDC — 2 operation(s) for discount.
  name: NEXTDC Discount API
  slug: nextdc-discount-api
- baseURL: https://sandbox-api.axonvx.com/api/biz2
  baseurl_source: declared
  description: The discounts API from NEXTDC — 1 operation(s) for discounts.
  name: NEXTDC Discounts API
  slug: nextdc-discounts-api
- baseURL: https://sandbox-api.axonvx.com/api/biz2
  baseurl_source: declared
  description: The limitations API from NEXTDC — 1 operation(s) for limitations.
  name: NEXTDC Limitations API
  slug: nextdc-limitations-api
- baseURL: https://sandbox-api.axonvx.com/api/biz2
  baseurl_source: declared
  description: The locations API from NEXTDC — 3 operation(s) for locations.
  name: NEXTDC Locations API
  slug: nextdc-locations-api
- baseURL: https://sandbox-api.axonvx.com/api/biz2
  baseurl_source: declared
  description: The pricepoints API from NEXTDC — 1 operation(s) for pricepoints.
  name: NEXTDC Pricepoints API
  slug: nextdc-pricepoints-api
- baseURL: https://sandbox-api.axonvx.com/api/biz2
  baseurl_source: declared
  description: The quote API from NEXTDC — 9 operation(s) for quote.
  name: NEXTDC Quote API
  slug: nextdc-quote-api
- baseURL: https://sandbox-api.axonvx.com/api/biz2
  baseurl_source: declared
  description: The quotes API from NEXTDC — 1 operation(s) for quotes.
  name: NEXTDC Quotes API
  slug: nextdc-quotes-api
- baseURL: https://sandbox-api.axonvx.com/api/biz2
  baseurl_source: declared
  description: The resource API from NEXTDC — 7 operation(s) for resource.
  name: NEXTDC Resource API
  slug: nextdc-resource-api
- baseURL: https://sandbox-api.axonvx.com/api/biz2
  baseurl_source: declared
  description: The resources API from NEXTDC — 2 operation(s) for resources.
  name: NEXTDC Resources API
  slug: nextdc-resources-api
- baseURL: https://sandbox-api.axonvx.com/api/biz2
  baseurl_source: declared
  description: The service API from NEXTDC — 6 operation(s) for service.
  name: NEXTDC Service API
  slug: nextdc-service-api
- baseURL: https://sandbox-api.axonvx.com/api/biz2
  baseurl_source: declared
  description: The services API from NEXTDC — 2 operation(s) for services.
  name: NEXTDC Services API
  slug: nextdc-services-api
- baseURL: https://sandbox-api.axonvx.com/api/biz2
  baseurl_source: declared
  description: The task API from NEXTDC — 1 operation(s) for task.
  name: NEXTDC Task API
  slug: nextdc-task-api
- baseURL: https://sandbox-api.axonvx.com/api/biz2
  baseurl_source: declared
  description: The tasks API from NEXTDC — 1 operation(s) for tasks.
  name: NEXTDC Tasks API
  slug: nextdc-tasks-api
artifact_total: 26
common:
- group: agent
  href: https://artifacts.apis.io/nextdc/agentic-access/nextdc-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/nextdc-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/nextdc/rules/nextdc-rules.yml
  title: ''
  type: Spectral
  url: rules/nextdc-rules.yml
- group: design
  href: https://artifacts.apis.io/nextdc/vocabulary/nextdc-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/nextdc-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/nextdc/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/nextdc/data-model/nextdc-data-model.yml
  title: ''
  type: DataModel
  url: data-model/nextdc-data-model.yml
- group: design
  href: https://artifacts.apis.io/nextdc/conventions/nextdc-conventions.yml
  title: ''
  type: Conventions
  url: conventions/nextdc-conventions.yml
- group: start
  href: https://artifacts.apis.io/nextdc/sandbox/nextdc-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/nextdc-sandbox.yml
- group: operate
  href: https://artifacts.apis.io/nextdc/lifecycle/nextdc-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/nextdc-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/nextdc/lifecycle/nextdc-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/nextdc-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/nextdc/errors/nextdc-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/nextdc-error-codes.yml
- group: design
  href: https://artifacts.apis.io/nextdc/errors/nextdc-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/nextdc-problem-types.yml
- group: design
  href: https://artifacts.apis.io/nextdc/conformance/nextdc-conformance.yml
  title: ''
  type: Conformance
  url: conformance/nextdc-conformance.yml
- group: other
  href: https://artifacts.apis.io/nextdc/overlays/nextdc-axon-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/nextdc-axon-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/nextdc/well-known/nextdc-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/nextdc-well-known.yml
- group: other
  href: https://artifacts.apis.io/nextdc/hosts/nextdc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nextdc-hosts.yml
- group: build
  href: https://artifacts.apis.io/nextdc/integrations/nextdc-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/nextdc-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/nextdc/vendors/nextdc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/nextdc-vendors.yml
- group: auth
  href: https://artifacts.apis.io/nextdc/authentication/nextdc-authentication.yml
  title: ''
  type: Authentication
  url: authentication/nextdc-authentication.yml
- group: auth
  href: https://artifacts.apis.io/nextdc/security/nextdc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nextdc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nextdc.com/
- group: company
  title: ''
  type: Blog
  url: https://www.nextdc.com/resources?type=insights
- group: company
  title: ''
  type: Newsroom
  url: https://www.nextdc.com/resources?type=news
- group: operate
  title: ''
  type: Support
  url: https://www.nextdc.com/customer-support
- group: operate
  title: ''
  type: Contact
  url: https://www.nextdc.com/contact
- group: company
  title: ''
  type: About
  url: https://www.nextdc.com/about-us
- group: auth
  title: ''
  type: Compliance
  url: https://www.nextdc.com/about-us/certifications
- group: start
  title: ''
  type: Login
  url: https://www.onedc.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nextdc.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nextdc.com/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nextdc/
created: '2026-10-22'
description: 'NEXTDC is an Australian data centre operator providing AI-ready colocation, connectivity and hybrid cloud infrastructure across Australia-wide data centres, and expanding into Southeast Asia with its KL1 Kuala Lumpur facility. Customers manage their services through the ONEDC self-service customer portal. No public developer API, API documentation or developer portal was found on nextdc.com during this identity pass (source: australia-apidays-2026 harvest).'
image: https://www.nextdc.com/hubfs/nextDCLogo.svg
json_schemas:
- name: Azure Provider Schema
  property_count: 2
  slug: nextdc-axon-azure-provider
- name: Oob Provider Schema
  property_count: 1
  slug: nextdc-axon-oob-provider
layout: provider
modified: '2026-10-22'
name: NEXTDC
nav: Providers
network: true
overview: 'NEXTDC publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including Comments API, Discount API, Discounts API, and 11 more. Tagged areas include Company, Data Center, Colocation, Cloud Infrastructure, and Connectivity.


  The NEXTDC catalog on APIs.io includes 1 Spectral governance ruleset.


  NEXTDC''s developer surface includes sandbox, authentication, engineering blog, support, and 26 more developer resources.'
plans:
- name: Nextdc Plans Pricing
  plan_count: 0
  slug: nextdc-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 0
  name: Nextdc Rate Limits
  slug: nextdc-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: NEXTDC API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: nextdc-rules
score:
  band: thin
  composite: 36.8
  coverage:
    artifact_dirs: 26
    catalog_earned: 51.8
    catalog_earned_first_party: 0.0
    catalog_gap: 63.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.9
  facets:
    access_clarity: 21.1
    contract_governance: 35.6
    contract_quality: 50.5
    developer_ergonomics: 38.7
    discoverability: 67.0
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 43.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/nextdc/nextdc-2026-11-03T140205.png
security:
- kind: authentication
  name: Nextdc Authentication
  slug: nextdc-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Nextdc Domain Security
  slug: nextdc-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 4
skills:
- name: nextdc-allocate-a-port
  slug: nextdc-allocate-a-port
- name: nextdc-approve-an-incoming-connection
  slug: nextdc-approve-an-incoming-connection
- name: nextdc-create-a-virtual-connection
  slug: nextdc-create-a-virtual-connection
- name: nextdc-quote-a-connection
  slug: nextdc-quote-a-connection
slug: nextdc
tags:
- Company
- Data Center
- Colocation
- Cloud Infrastructure
- Connectivity
- Artificial Intelligence
- Australia
website: https://www.nextdc.com/
---
