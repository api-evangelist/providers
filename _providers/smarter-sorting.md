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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.5
  scored_at: '2026-09-04'
api_count: 2
apis:
- baseURL: https://api.smartersorting.com
  baseurl_source: declared
  description: The Api(.*) API from Smarter Sorting — 1 operation(s) for api(.*).
  name: Smarter Sorting Api(.*) API
  slug: smarter-sorting-api-api
- baseURL: https://api.smartersorting.com
  baseurl_source: declared
  description: The Assets(.*) API from Smarter Sorting — 1 operation(s) for assets(.*).
  name: Smarter Sorting Assets(.*) API
  slug: smarter-sorting-assets-api
- baseURL: https://api.smartersorting.com
  baseurl_source: declared
  description: The Docs(.*) API from Smarter Sorting — 2 operation(s) for docs(.*).
  name: Smarter Sorting Docs(.*) API
  slug: smarter-sorting-docs-api
- baseURL: https://api.smartersorting.com
  baseurl_source: declared
  description: The products API from Smarter Sorting — 4 operation(s) for products.
  name: Smarter Sorting Products API
  slug: smarter-sorting-products-api
artifact_total: 11
asyncapis:
- description: ''
  name: Smarter Sorting Event Surface
  slug: smarter-sorting-event-surface
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/smarter-sorting-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/smarter-sorting-customer-classification-v1-overlay.yaml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/smarter-sorting-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/smarter-sorting-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/smarter-sorting-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.smartersorting.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.smartersorting.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://api.smartersorting.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.smartersorting.com/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://api.smartersorting.com/docs#setup
- group: operate
  title: ''
  type: Support
  url: https://support.smartersorting.com/s/
- group: company
  title: ''
  type: Blog
  url: https://www.smartersorting.com/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.smartersorting.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.smartersorting.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.smartersorting.com/legal/privacy-policy
- group: design
  title: ''
  type: Conformance
  url: conformance/smarter-sorting-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/smarter-sorting-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/smarter-sorting-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: security/smarter-sorting-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/smarter-sorting-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/smarter-sorting-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/smarter-sorting-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/smarter-sorting-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-28'
description: Smarter Sorting (which rebranded as SmarterX in 2023 and now operates as part of Syndigo) is an Austin, Texas product-intelligence and regulatory-classification company serving retailers, consumer-goods brands and the logistics industry. Its Smarter-1 platform takes a customer's product catalog — at minimum a UPC and a product name — and returns machine-generated regulatory classifications covering hazardous-waste handling (RCRA waste codes and state waste codes), transport of dangerous goods (DOT, IATA and IMDG hazard classes, UN numbers, packing groups and proper shipping names), NFPA 704 fire-diamond ratings, lithium-battery attributes and UN 38.3 documentation, so that a retailer can decide whether an item may be sold, shipped, donated, recycled, reclaimed or must be disposed of as regulated waste. The company publishes a public Customer Classification API (OpenAPI 3.1.0) alongside its Back of Store Solution (BOSS) platform, a developer portal, a staging environment and
  a public status page.
image: https://portal.smartersorting.com/assets/imgs/logo-ss-color.svg
layout: provider
modified: '2026-08-28'
name: Smarter Sorting
nav: Providers
network: true
overview: 'Smarter Sorting publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Api(.*) API, Assets(.*) API, Docs(.*) API, and 1 more. Tagged areas include Company, Product Data, Regulatory Compliance, Hazardous Waste, and Retail.


  The Smarter Sorting catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Smarter Sorting''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, and 18 more developer resources.'
plans:
- name: Smarter Sorting Plans Pricing
  plan_count: 0
  slug: smarter-sorting-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Smarter Sorting Rate Limits
  slug: smarter-sorting-rate-limits
score:
  band: developing
  composite: 45.4
  coverage:
    artifact_dirs: 22
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 4.5
    contract_quality: 56.2
    developer_ergonomics: 66.1
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 26.3
  previous_composite: 45.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/smarter-sorting/refs/heads/main/screenshots/smarter-sorting-2026-09-02T155912.png
security:
- kind: authentication
  name: Smarter Sorting Authentication
  slug: smarter-sorting-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Smarter Sorting Domain Security
  slug: smarter-sorting-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Smarter Sorting Vulnerability Disclosure
  slug: smarter-sorting-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Smarter Sorting Trust Center
  slug: smarter-sorting-trust-center
  summary_line: SOC 2 Type II
slug: smarter-sorting
tags:
- Company
- Product Data
- Regulatory Compliance
- Hazardous Waste
- Retail
- Consumer Goods
- Supply Chain
- Sustainability
- Dangerous Goods
- Product Classification
website: https://www.smartersorting.com/
---
