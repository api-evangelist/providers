---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 46.7
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 25
  human_in_the_loop: 2
  name: Placementapi Com Agentic Access
  operation_count: 49
  slug: placementapi-com-agentic-access
  summary_line: 49 operations · 25 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.placementapi.com
  baseurl_source: declared
  description: Balance, spend limits, keys, briefs and automation.
  name: placementapi-com Account API
  slug: placementapi-com-account-api
- baseURL: https://api.placementapi.com
  baseurl_source: declared
  description: Search inventory, inspect a publisher, read market context.
  name: placementapi-com Catalogue API
  slug: placementapi-com-catalogue-api
- baseURL: https://api.placementapi.com
  baseurl_source: declared
  description: Card checkout for a basket, with or without an account.
  name: placementapi-com Checkout API
  slug: placementapi-com-checkout-api
- baseURL: https://api.placementapi.com
  baseurl_source: declared
  description: Read-only comparison of a basket captured elsewhere (Perch). No ordering, no writes.
  name: placementapi-com Comparison API
  slug: placementapi-com-comparison-api
- baseURL: https://api.placementapi.com
  baseurl_source: declared
  description: Articles for placements where the buyer supplies or commissions copy.
  name: placementapi-com Content API
  slug: placementapi-com-content-api
- baseURL: https://api.placementapi.com
  baseurl_source: declared
  description: Service banner, health and field semantics.
  name: placementapi-com Meta API
  slug: placementapi-com-meta-api
- baseURL: https://api.placementapi.com
  baseurl_source: declared
  description: Place, list, cancel and follow orders. Requires the `order` scope to spend.
  name: placementapi-com Orders API
  slug: placementapi-com-orders-api
- baseURL: https://api.placementapi.com
  baseurl_source: declared
  description: Briefs in, costed and held baskets out.
  name: placementapi-com Planning API
  slug: placementapi-com-planning-api
- baseURL: https://api.placementapi.com
  baseurl_source: declared
  description: Target profiles, gap maps and keyword winners (DataForSEO-backed).
  name: placementapi-com Research API
  slug: placementapi-com-research-api
- baseURL: https://api.placementapi.com
  baseurl_source: declared
  description: A customer's own retained Search Console rows. Read-only, never shared.
  name: placementapi-com Search Console API
  slug: placementapi-com-search-console-api
artifact_total: 27
common:
- group: agent
  href: https://artifacts.apis.io/placementapi-com/agentic-access/placementapi-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/placementapi-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/placementapi-com/rate-limits/placementapi-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/placementapi-com-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/placementapi-com/rules/placementapi-com-rules.yml
  title: ''
  type: Spectral
  url: rules/placementapi-com-rules.yml
- group: design
  href: https://artifacts.apis.io/placementapi-com/json-ld/placementapi-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/placementapi-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/placementapi-com/vocabulary/placementapi-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/placementapi-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/placementapi-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/placementapi-com/data-model/placementapi-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/placementapi-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/placementapi-com/conventions/placementapi-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/placementapi-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/placementapi-com/conventions/placementapi-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/placementapi-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/placementapi-com/authentication/placementapi-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/placementapi-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/placementapi-com/scopes/placementapi-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/placementapi-com-scopes.yml
- group: design
  href: https://artifacts.apis.io/placementapi-com/errors/placementapi-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/placementapi-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/placementapi-com/conformance/placementapi-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/placementapi-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/placementapi-com/llms/placementapi-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/placementapi-com-llms.txt
- group: other
  href: https://artifacts.apis.io/placementapi-com/hosts/placementapi-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/placementapi-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/placementapi-com/vendors/placementapi-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/placementapi-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/placementapi-com/packages/placementapi-com-packages.yml
  title: ''
  type: SDKs
  url: packages/placementapi-com-packages.yml
- group: build
  href: https://artifacts.apis.io/placementapi-com/packages/placementapi-com-packages.yml
  title: ''
  type: Packages
  url: packages/placementapi-com-packages.yml
- group: auth
  href: https://artifacts.apis.io/placementapi-com/security/placementapi-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/placementapi-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://placementapi.com/
- group: docs
  title: ''
  type: APIReference
  url: https://placementapi.com/openapi.json
- group: commercial
  title: ''
  type: Pricing
  url: https://placementapi.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://placementapi.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://placementapi.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://placementapi.com/signup
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://placementapi.com/openapi.json
  - status: null
    url: https://api.placementapi.com/openapi.json
  - status: 200
    url: https://placementapi.com/mcp
  - status: 200
    url: https://api.placementapi.com/mcp
  - status: 200
    url: https://placementapi.com/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: Placement API aggregates backlink placement inventory from multiple suppliers into a normalized catalogue, deduplicated by domain, and lets software purchase from it programmatically. It offers AI agents the ability to buy backlinks across 10 suppliers, with deduplication, verified metrics, and real turnaround times. Prices are expressed in prepaid credits (1 credit = 1 US cent). The service provides endpoints for quoting, ordering, content handling, and post‑placement outcome tracking, all via a RESTful API documented with OpenAPI. The company behind the service is Future Bets, Inc., operating under the brand Placement API.
image: https://placementapi.com/opengraph-image?2bee39213984a5f6
json_schemas:
- name: Brief
  property_count: 26
  slug: placementapi-com-brief
- name: Offer
  property_count: 25
  slug: placementapi-com-offer
- name: Order
  property_count: 27
  slug: placementapi-com-order
- name: QuoteLine
  property_count: 34
  slug: placementapi-com-quote-line
- name: Quote
  property_count: 21
  slug: placementapi-com-quote
- name: Site
  property_count: 15
  slug: placementapi-com-site
jsonld:
- class_count: 37
  name: Placementapi Com Context
  property_count: 237
  slug: placementapi-com-context
layout: provider
modified: '2026-10-30'
name: placementapi-com
nav: Providers
network: true
overview: 'placementapi-com publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Catalogue API, Checkout API, and 7 more. Tagged areas include Company, AI, SEO, Marketing, and Backlinks.


  The placementapi-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  placementapi-com''s developer surface includes authentication, API reference, pricing, signup flow, and 21 more developer resources.'
plans:
- name: Placementapi Com Plans Pricing
  plan_count: 0
  slug: placementapi-com-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 2
  name: Placementapi Com Rate Limits
  slug: placementapi-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: placementapi-com API Rules
  rule_count: 18
  severity_counts:
    error: 11
    hint: 0
    info: 3
    warn: 4
  slug: placementapi-com-rules
scopes:
- name: Placementapi Com Scopes
  scope_count: 2
  slug: placementapi-com-scopes
  summary_line: 2 scopes
score:
  band: developing
  composite: 52.3
  coverage:
    artifact_dirs: 29
    catalog_earned: 84.9
    catalog_earned_first_party: 0.0
    catalog_gap: 30.1
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 79.1
    contract_quality: 63.2
    developer_ergonomics: 32.6
    discoverability: 66.1
    operational_transparency: 18.9
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Placementapi Com Authentication
  slug: placementapi-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Placementapi Com Domain Security
  slug: placementapi-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: catalogue
  slug: placementapi-com-catalogue
- name: content
  slug: placementapi-com-content
- name: orders
  slug: placementapi-com-orders
slug: placementapi-com
tags:
- Company
- AI
- SEO
- Marketing
- Backlinks
- Automation
- Technology
website: https://placementapi.com/
---
