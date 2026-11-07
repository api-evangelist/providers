---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: verified
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
  score: 30.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Trueproxies Agentic Access
  operation_count: 21
  slug: trueproxies-agentic-access
  summary_line: 21 operations · 7 acting
api_count: 1
apis:
- baseURL: https://api.trueproxies.com
  baseurl_source: declared
  description: The Analytics API from TrueProxies — 1 operation(s) for analytics.
  name: TrueProxies Analytics API
  slug: trueproxies-analytics-api
- baseURL: https://api.trueproxies.com
  baseurl_source: declared
  description: The Catalog API from TrueProxies — 2 operation(s) for catalog.
  name: TrueProxies Catalog API
  slug: trueproxies-catalog-api
- baseURL: https://api.trueproxies.com
  baseurl_source: declared
  description: The Invoices API from TrueProxies — 4 operation(s) for invoices.
  name: TrueProxies Invoices API
  slug: trueproxies-invoices-api
- baseURL: https://api.trueproxies.com
  baseurl_source: declared
  description: The Me API from TrueProxies — 1 operation(s) for me.
  name: TrueProxies Me API
  slug: trueproxies-me-api
- baseURL: https://api.trueproxies.com
  baseurl_source: declared
  description: The Services API from TrueProxies — 11 operation(s) for services.
  name: TrueProxies Services API
  slug: trueproxies-services-api
artifact_total: 24
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://trueproxies.com/feed.xml
- group: other
  href: https://artifacts.apis.io/trueproxies/capabilities/trueproxies-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/trueproxies-capability-edges.yml
- group: auth
  title: ''
  type: Security
  url: https://dashboard.trueproxies.com/.well-known/security.txt
- group: auth
  href: https://artifacts.apis.io/trueproxies/security/trueproxies-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/trueproxies-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/trueproxies/agentic-access/trueproxies-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/trueproxies-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/trueproxies/rate-limits/trueproxies-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/trueproxies-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/trueproxies/plans/trueproxies-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/trueproxies-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/trueproxies/rules/trueproxies-rules.yml
  title: ''
  type: Spectral
  url: rules/trueproxies-rules.yml
- group: design
  href: https://artifacts.apis.io/trueproxies/json-ld/trueproxies-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/trueproxies-context.jsonld
- group: design
  href: https://artifacts.apis.io/trueproxies/vocabulary/trueproxies-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/trueproxies-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/trueproxies/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/trueproxies/data-model/trueproxies-data-model.yml
  title: ''
  type: DataModel
  url: data-model/trueproxies-data-model.yml
- group: design
  href: https://artifacts.apis.io/trueproxies/conventions/trueproxies-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/trueproxies-conventions.yml
- group: design
  href: https://artifacts.apis.io/trueproxies/conventions/trueproxies-conventions.yml
  title: ''
  type: Conventions
  url: conventions/trueproxies-conventions.yml
- group: design
  href: https://artifacts.apis.io/trueproxies/errors/trueproxies-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/trueproxies-problem-types.yml
- group: design
  href: https://artifacts.apis.io/trueproxies/conformance/trueproxies-conformance.yml
  title: ''
  type: Conformance
  url: conformance/trueproxies-conformance.yml
- group: other
  href: https://artifacts.apis.io/trueproxies/overlays/trueproxies-customer-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/trueproxies-customer-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/trueproxies/llms/trueproxies-website-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/trueproxies-website-llms.txt
- group: agent
  href: https://artifacts.apis.io/trueproxies/llms/trueproxies-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/trueproxies-llms.txt
- group: auth
  href: https://artifacts.apis.io/trueproxies/well-known/trueproxies-dashboard-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/trueproxies-dashboard-security.txt
- group: agent
  href: https://artifacts.apis.io/trueproxies/well-known/trueproxies-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/trueproxies-well-known.yml
- group: other
  href: https://artifacts.apis.io/trueproxies/hosts/trueproxies-hosts.yml
  title: ''
  type: Hosts
  url: hosts/trueproxies-hosts.yml
- group: other
  href: https://artifacts.apis.io/trueproxies/vendors/trueproxies-vendors.yml
  title: ''
  type: Vendors
  url: vendors/trueproxies-vendors.yml
- group: auth
  href: https://artifacts.apis.io/trueproxies/security/trueproxies-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/trueproxies-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/trueproxies/authentication/trueproxies-authentication.yml
  title: ''
  type: Authentication
  url: authentication/trueproxies-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://trueproxies.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.trueproxies.com/overview/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.trueproxies.com/getting-started/quickstart/
- group: commercial
  title: ''
  type: Pricing
  url: https://trueproxies.com/pricing/
- group: operate
  title: ''
  type: Support
  url: https://docs.trueproxies.com/support/
- group: operate
  title: ''
  type: Contact
  url: https://trueproxies.com/contact/
- group: operate
  title: ''
  type: FAQ
  url: https://trueproxies.com/faq/
- group: company
  title: ''
  type: Blog
  url: https://trueproxies.com/blog/
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.trueproxies.com/signup
- group: start
  title: ''
  type: Login
  url: https://dashboard.trueproxies.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://trueproxies.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://trueproxies.com/privacy/
- group: other
  title: ''
  type: RefundPolicy
  url: https://trueproxies.com/refund-policy/
- group: other
  title: ''
  type: AcceptableUsePolicy
  url: https://trueproxies.com/acceptable-use/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/trueproxies
- group: other
  title: ''
  type: X
  url: https://x.com/trueproxiesltd
created: '2026-09-23'
description: 'TrueProxies, LLC (USA) sells residential and datacenter proxies (HTTP/HTTPS/SOCKS5) for developers and data teams, priced per hour, per GB or per day: unlimited-bandwidth Residential IPv4 at a chosen speed tier, GB-based Residential IPv4 with country, city, region and ASN targeting, and Datacenter IPv6. Beyond the proxy gateways it publishes the TrueProxies Customer API (OpenAPI 3.1 at api.trueproxies.com/v1/openapi.json), a scoped-Bearer-key REST API for managing existing proxy services, whitelists, credentials, usage analytics and invoices, with technical docs at docs.trueproxies.com.'
finops:
- has_sources: true
  method: derived
  name: Trueproxies Finops
  primary_unit: subscription
  service_category: ''
  slug: trueproxies-finops
  template: false
json_schemas:
- name: EndpointRequest
  property_count: 12
  slug: trueproxies-endpoint-request
- name: Invoice
  property_count: 20
  slug: trueproxies-invoice
- name: LiveMetrics
  property_count: 12
  slug: trueproxies-live-metrics
- name: Me
  property_count: 12
  slug: trueproxies-me
- name: Service
  property_count: 27
  slug: trueproxies-service
- name: Usage
  property_count: 16
  slug: trueproxies-usage
jsonld:
- class_count: 36
  name: Trueproxies Context
  property_count: 160
  slug: trueproxies-context
layout: provider
modified: '2026-10-06'
name: TrueProxies
nav: Providers
network: true
overview: 'TrueProxies publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Analytics API, Catalog API, Invoices API, and 2 more. Tagged areas include Proxies, Residential Proxies, Datacenter Proxies, Web Scraping, and Networking.


  The TrueProxies catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  TrueProxies'' developer surface includes authentication, documentation, getting-started guide, pricing, support, FAQ, engineering blog, and 34 more developer resources.'
plans:
- name: Trueproxies Plans Pricing
  plan_count: 4
  slug: trueproxies-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 2
  name: Trueproxies Rate Limits
  slug: trueproxies-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: TrueProxies API Rules
  rule_count: 16
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 4
  slug: trueproxies-rules
score:
  band: developing
  composite: 48.0
  coverage:
    artifact_dirs: 29
    catalog_earned: 83.8
    catalog_earned_first_party: 20.0
    catalog_gap: 31.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.6
  facets:
    access_clarity: 61.8
    contract_governance: 22.0
    contract_quality: 64.1
    developer_ergonomics: 28.0
    discoverability: 69.6
    operational_transparency: 26.3
  previous_composite: 56.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/trueproxies/trueproxies-2026-10-11T131220.png
security:
- kind: authentication
  name: Trueproxies Authentication
  slug: trueproxies-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Trueproxies Domain Security
  slug: trueproxies-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Trueproxies Vulnerability Disclosure
  slug: trueproxies-vulnerability-disclosure
  summary_line: contact published
skill_count: 4
skills:
- name: buy-and-pay-invoice
  slug: trueproxies-buy-and-pay-invoice
- name: diagnose-proxy-service
  slug: trueproxies-diagnose-proxy-service
- name: manage-ip-whitelist
  slug: trueproxies-manage-ip-whitelist
- name: rotate-proxy-password
  slug: trueproxies-rotate-proxy-password
slug: trueproxies
tags:
- Proxies
- Residential Proxies
- Datacenter Proxies
- Web Scraping
- Networking
- IPv6
- SOCKS5
- Data Collection
website: https://trueproxies.com/
---
