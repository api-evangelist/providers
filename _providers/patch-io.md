---
access_model:
  confidence: medium
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    agent_skills: false
    agentic_access: derived
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.3
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Patch Io Agentic Access
  operation_count: 12
  slug: patch-io-agentic-access
  summary_line: 12 operations · 7 acting
api_count: 2
apis:
- baseURL: https://api.patch.io/
  baseurl_source: declared
  description: Manage individual line items inside a multi-line carbon credit order.
  name: Patch Order Line Items API
  slug: patch-io-order-line-items-api
- baseURL: https://api.patch.io/
  baseurl_source: declared
  description: Place, retrieve, place, and cancel carbon credit and removal orders.
  name: Patch Orders API
  slug: patch-io-orders-api
- baseURL: https://api.patch.io/
  baseurl_source: declared
  description: Browse and retrieve verified carbon projects across removal and avoidance categories.
  name: Patch Projects API
  slug: patch-io-projects-api
- baseURL: https://api.patch.io/
  baseurl_source: declared
  description: List the technology and parent technology types backing Patch's carbon project taxonomy.
  name: Patch Technology Types API
  slug: patch-io-technology-types-api
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Patch Carbon API
  slug: open-patch-io-carbon-api
- collection_type: open
  name: Patch Carbon Order Line Items API
  slug: open-patch-io-order-line-items-api
- collection_type: open
  name: Patch Carbon Order Line Items Orders API
  slug: open-patch-io-orders-api
- collection_type: open
  name: Patch Carbon Order Line Items Projects API
  slug: open-patch-io-projects-api
- collection_type: open
  name: Patch Carbon Order Line Items Technology Types API
  slug: open-patch-io-technology-types-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/patch-io-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/patch-io-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/patch-io-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/patch-io-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.patch.io/
- group: other
  title: ''
  type: Platform
  url: https://www.patch.io/platform
- group: other
  title: ''
  type: HowItWorks
  url: https://www.patch.io/how-it-works
- group: docs
  title: ''
  type: Documentation
  url: https://docs.patch.io/
- group: docs
  title: ''
  type: SwaggerUI
  url: https://api.patch.io/api-docs/index.html
- group: build
  title: ''
  type: GitHub
  url: https://github.com/patch-technology
- group: company
  title: ''
  type: Blog
  url: https://www.patch.io/blog
- group: build
  title: ''
  type: ClimateNeutral
  url: https://www.patch.io/climate-neutral
- group: company
  title: ''
  type: Careers
  url: https://www.patch.io/careers
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/patch-technology/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/patch-technology
- group: commercial
  title: ''
  type: Pricing
  url: https://www.patch.io/how-it-works
- group: operate
  title: ''
  type: StatusPage
  url: https://status.patch.io
- group: other
  title: ''
  type: X
  url: https://x.com/usepatch
- group: commercial
  title: ''
  type: Plans
  url: plans/patch-io-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/patch-io-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/patch-io-finops.yml
created: '2026-05-23'
description: Patch is an API-first climate platform that helps companies procure carbon credits and removals, run climate strategy programs, and embed climate action into their own products. The core Patch API exposes carbon projects, estimates, and orders so developers can build offset purchase flows directly into checkouts, accounting systems, and ESG products. Patch also runs Radius (network-based impact acceleration), Offtake (climate tech funding and long-term credit access), and an RFP tool for carbon credit procurement. Official SDKs are available for Node.js, Python, Ruby, and other languages, and the API is documented with an OpenAPI 3 spec and Swagger UI.
examples:
- key_count: 2
  name: Patch Io Create Order Example
  slug: patch-io-create-order-example
- key_count: 2
  name: Patch Io Place Order Example
  slug: patch-io-place-order-example
- key_count: 2
  name: Patch Io Retrieve Projects Example
  slug: patch-io-retrieve-projects-example
finops:
- name: Patch Io Finops
  service_category: API
  slug: patch-io-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/patch-io.png
json_schemas:
- name: Patch Order
  property_count: 13
  slug: patch-io-order
- name: Patch Project
  property_count: 18
  slug: patch-io-project
- name: Patch Technology Type
  property_count: 3
  slug: patch-io-technology-type
json_structures:
- name: Patch Io Order Structure
  property_count: 9
  slug: patch-io-order-structure
- name: Patch Io Project Structure
  property_count: 7
  slug: patch-io-project-structure
jsonld:
- class_count: 17
  name: Patch Io Context
  property_count: 10
  slug: patch-io-context
layout: provider
modified: '2026-08-08'
name: Patch
nav: Providers
network: true
overview: 'Patch publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Order Line Items API, Orders API, Projects API, and 1 more. Tagged areas include Climate, Carbon Credits, Carbon Removal, Offsets, and API-First.


  The Patch catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Patch''s developer surface includes authentication, documentation, GitHub presence, engineering blog, pricing, and 16 more developer resources.'
plans:
- name: Patch Io Plans Pricing
  plan_count: 1
  slug: patch-io-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 2
  name: Patch Io Rate Limits
  slug: patch-io-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Patch API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: patch-io-jsonschema-spectral-rules
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: Patch API Rules
  rule_count: 10
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 5
  slug: patch-io-rules
score:
  band: developing
  composite: 45.5
  coverage:
    artifact_dirs: 16
    catalog_earned: 86.5
    catalog_earned_first_party: 0.0
    catalog_gap: 28.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 28.8
    contract_quality: 69.4
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 28.8
    operational_transparency: 39.5
  previous_composite: 45.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/patch-io/refs/heads/main/screenshots/patch-io-2026-06-20T191438.png
security:
- kind: authentication
  name: Patch Io Authentication
  slug: patch-io-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Patch Io Domain Security
  slug: patch-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Patch Io Vulnerability Disclosure
  slug: patch-io-vulnerability-disclosure
  summary_line: disclosure policy published
slug: patch-io
tags:
- Climate
- Carbon Credits
- Carbon Removal
- Offsets
- API-First
- Embedded Climate
- Marketplace
- Sustainability
- OpenAPI
- SDK
website: https://www.patch.io/
---
