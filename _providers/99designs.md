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
  band: agent-aware
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
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: 99Designs Agentic Access
  operation_count: 8
  slug: 99designs-agentic-access
  summary_line: 8 operations · 3 acting
api_count: 1
apis:
- baseURL: https://api.99designs.com/resources/v1
  baseurl_source: declared
  description: Collect design briefs.
  name: 99designs Briefs API
  slug: 99designs-briefs-api
- baseURL: https://api.99designs.com/resources/v1
  baseurl_source: declared
  description: Generate partner coupon tokens.
  name: 99designs Coupons API
  slug: 99designs-coupons-api
- baseURL: https://api.99designs.com/resources/v1
  baseurl_source: declared
  description: Search and retrieve designers, reviews, and portfolios.
  name: 99designs Designers API
  slug: 99designs-designers-api
- baseURL: https://api.99designs.com/resources/v1
  baseurl_source: declared
  description: List the 99designs products a partner has available for sale, with prices and the brief schema each product version requires.
  name: 99designs Products API
  slug: 99designs-products-api
- baseURL: https://api.99designs.com/resources/v1
  baseurl_source: declared
  description: Place orders against 99designs products.
  name: 99designs Orders API
  slug: 99designs-orders-api
artifact_total: 21
collections:
- collection_type: open
  name: 99designs Briefs API
  slug: open-99designs-briefs-api
- collection_type: open
  name: 99designs Coupons API
  slug: open-99designs-coupons-api
- collection_type: open
  name: 99designs Briefs Designers API
  slug: open-99designs-designers-api
- collection_type: open
  name: 99designs Briefs Orders API
  slug: open-99designs-orders-api
- collection_type: open
  name: 99designs Products API
  slug: open-99designs-products-api
common:
- group: company
  title: ''
  type: Blog
  url: https://99designs.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://99designs.com/blog/feed/
- group: other
  href: https://artifacts.apis.io/99designs/capabilities/99designs-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/99designs-capability-edges.yml
- group: docs
  href: https://artifacts.apis.io/99designs/openapi/_original/99designs-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/99designs-openapi.yml
- group: other
  href: https://artifacts.apis.io/99designs/overlays/99designs-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/99designs-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/99designs/authentication/99designs-authentication.yml
  title: ''
  type: Authentication
  url: authentication/99designs-authentication.yml
- group: design
  href: https://artifacts.apis.io/99designs/conventions/99designs-conventions.yml
  title: ''
  type: Conventions
  url: conventions/99designs-conventions.yml
- group: design
  href: https://artifacts.apis.io/99designs/errors/99designs-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/99designs-problem-types.yml
- group: design
  href: https://artifacts.apis.io/99designs/data-model/99designs-data-model.yml
  title: ''
  type: DataModel
  url: data-model/99designs-data-model.yml
- group: design
  href: https://artifacts.apis.io/99designs/conformance/99designs-conformance.yml
  title: ''
  type: Conformance
  url: conformance/99designs-conformance.yml
- group: design
  href: https://artifacts.apis.io/99designs/lifecycle/99designs-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/99designs-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/99designs/mcp/99designs-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/99designs-mcp.yml
- group: build
  href: https://artifacts.apis.io/99designs/packages/99designs-packages.yml
  title: ''
  type: Packages
  url: packages/99designs-packages.yml
- group: commercial
  href: https://artifacts.apis.io/99designs/plans/99designs-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/99designs-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/99designs/rate-limits/99designs-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/99designs-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/99designs/llms/99designs-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/99designs-llms.txt
- group: agent
  href: https://artifacts.apis.io/99designs/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/99designs/agentic-access/99designs-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/99designs-agentic-access.yml
- group: agent
  href: https://artifacts.apis.io/99designs/well-known/99designs-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/99designs-well-known.yml
- group: auth
  href: https://artifacts.apis.io/99designs/well-known/99designs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/99designs-security.txt
- group: auth
  href: https://artifacts.apis.io/99designs/security/99designs-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/99designs-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://99designs.com/.well-known/security.txt
- group: auth
  href: https://artifacts.apis.io/99designs/security/99designs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/99designs-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://99designs.com/api
- group: docs
  title: ''
  type: Documentation
  url: https://api.99designs.com/resources/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://api.99designs.com/resources/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://api.99designs.com/resources/docs/#getting-started
- group: start
  title: ''
  type: SignUp
  url: https://99designs.com/api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/99designs
- group: commercial
  title: ''
  type: Pricing
  url: https://99designs.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://99designs.com/blog
- group: operate
  title: ''
  type: Support
  url: https://support.99designs.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://99designs.com/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://99designs.com/legal/privacy
- group: company
  title: ''
  type: Website
  url: https://www.99designs.com
created: '2026-07-17'
description: '99designs by Vista is a global creative marketplace connecting clients with a worldwide network of freelance designers for logos, brand identity, web and packaging design, illustration, and more, using both a design-contest model and one-to-one projects. Its partner API (base https://api.99designs.com/resources/v1) lets platforms embed a fully-managed creative marketplace: search and match designers, retrieve designer profiles, reviews and portfolios, collect design briefs, list the products a partner has available for sale, place orders against those product versions, and generate partner coupons. Authentication uses a pair of API key headers (Api-Key-Id and Api-Key-Secret) issued to partners on request — access is sales-gated rather than self-serve, and no API plans or pricing are published. Founded in 2008 as a SitePoint spin-off and acquired by Cimpress/Vista in 2020.'
finops:
- has_sources: true
  method: derived
  name: 99Designs Finops
  primary_unit: contest package
  service_category: ''
  slug: 99designs-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/99designs.png
layout: provider
modified: '2026-10-06'
name: 99designs
nav: Providers
network: true
overview: '99designs publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Briefs API, Coupons API, Designers API, and 2 more. Tagged areas include Company, Media, Design, Marketplace, and Creative.


  The 99designs catalog on APIs.io includes 1 Spectral governance ruleset.


  99designs'' developer surface includes engineering blog, authentication, documentation, API reference, getting-started guide, signup flow, pricing, and 28 more developer resources.'
plans:
- name: 99Designs Plans Pricing
  plan_count: 5
  slug: 99designs-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 1
  name: 99Designs Rate Limits
  slug: 99designs-rate-limits
rules:
- authorship: generated
  effective_rule_count: 100
  extends:
  - spectral:oas
  name: 99designs API Rules
  rule_count: 59
  severity_counts:
    error: 57
    hint: 0
    info: 1
    warn: 1
  slug: 99designs-rules
score:
  band: strong
  composite: 57.5
  coverage:
    artifact_dirs: 28
    catalog_earned: 64.5
    catalog_earned_first_party: 20.0
    catalog_gap: 50.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.4
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 56.2
    developer_ergonomics: 58.9
    discoverability: 73.2
    operational_transparency: 28.9
  previous_composite: 56.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/99designs/99designs-2026-07-25T181252.png
security:
- kind: authentication
  name: 99Designs Authentication
  slug: 99designs-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: 99Designs Domain Security
  slug: 99designs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: 99Designs Vulnerability Disclosure
  slug: 99designs-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 3
skills:
- name: Find and evaluate a 99designs designer
  slug: 99designs-find-and-book-designer
- name: List partner products and order the right one
  slug: 99designs-list-products-and-order
- name: Submit a brief and place a 99designs order
  slug: 99designs-submit-brief-and-order
slug: 99designs
tags:
- Company
- Media
- Design
- Marketplace
- Creative
- Freelance
- Graphic Design
- Branding
website: https://www.99designs.com
---
