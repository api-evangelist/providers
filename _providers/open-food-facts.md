---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.0
  scored_at: '2026-09-17'
agentic_access:
- acting_count: 48
  human_in_the_loop: 0
  name: Open Food Facts Agentic Access
  operation_count: 136
  slug: open-food-facts-agentic-access
  summary_line: 136 operations · 48 acting
api_count: 1
apis:
- baseURL: https://world.openfoodfacts.org
  baseurl_source: declared
  description: 'The Open Food Facts read/write HTTP API, version 2 — product lookup by barcode, faceted and full-text search, image upload and product edit. Published by the project as an OpenAPI 3.1 document in the '
  name: Open Food Facts API v2
  slug: open-food-facts-api-v2
- baseURL: https://world.openfoodfacts.org
  baseurl_source: declared
  description: 'Version 3 of the Open Food Facts HTTP API — the current recommended version, with standardized response envelopes, the v3.3 image structure and taxonomy-suggestion endpoints. Published by the project '
  name: Open Food Facts API v3
  slug: open-food-facts-api-v3
- baseURL: https://prices.openfoodfacts.org
  baseurl_source: declared
  description: Open Prices is Open Food Facts' open crowdsourced database of product prices. Its REST API covers prices, proofs, locations, products, users and stats, and serves its own OpenAPI 3.0.3 document from t
  name: Open Prices API
  slug: open-food-facts-open-prices
- baseURL: https://search.openfoodfacts.org
  baseurl_source: declared
  description: Search-a-licious is the pluggable search service Open Food Facts runs over the product collection. It exposes search, facet and chart endpoints and serves its own OpenAPI 3.1 document from the live ho
  name: Search-a-licious API
  slug: open-food-facts-search-a-licious
- baseURL: https://api.folksonomy.openfoodfacts.org
  baseurl_source: declared
  description: The Folksonomy Engine lets contributors attach free property/value pairs to Open Food Facts products. It serves its own OpenAPI 3.1 document and uses an OAuth2 password flow against the Open Food Fact
  name: Folksonomy Engine API
  slug: open-food-facts-folksonomy
- baseURL: https://facets-kp.openfoodfacts.org
  baseurl_source: declared
  description: 'Serves knowledge panels for an Open Food Facts facet — category, label, brand and similar — so client applications can render the same explanatory panels the website shows. Serves its own OpenAPI 3.1 '
  name: Facets Knowledge Panels API
  slug: open-food-facts-facets-knowledge-panels
- baseURL: https://nutripatrol.openfoodfacts.org
  baseurl_source: declared
  description: NutriPatrol is the Open Food Facts moderation backend — it takes tickets and flags on products and images and exposes them to the moderation front end. Serves its own OpenAPI 3.1 document from the liv
  name: NutriPatrol API
  slug: open-food-facts-nutripatrol
- baseURL: https://world.openfoodfacts.org
  baseurl_source: declared
  description: The Cgi API from Open Food Facts — 1 operation(s) for cgi.
  name: Open Food Facts Cgi API
  slug: open-food-facts-cgi-api
- baseURL: https://world.openfoodfacts.org
  baseurl_source: declared
  description: The Product API from Open Food Facts — 3 operation(s) for product.
  name: Open Food Facts Product API
  slug: open-food-facts-product-api
- baseURL: https://world.openfoodfacts.org
  baseurl_source: declared
  description: The Search API from Open Food Facts — 1 operation(s) for search.
  name: Open Food Facts Search API
  slug: open-food-facts-search-api
- baseURL: https://world.openfoodfacts.org
  baseurl_source: declared
  description: The Taxonomy API from Open Food Facts — 1 operation(s) for taxonomy.
  name: Open Food Facts Taxonomy API
  slug: open-food-facts-taxonomy-api
- baseURL: https://world.openfoodfacts.org
  baseurl_source: declared
  description: The Taxonomy Suggestions API from Open Food Facts — 1 operation(s) for taxonomy suggestions.
  name: Open Food Facts Taxonomy Suggestions API
  slug: open-food-facts-taxonomy-suggestions-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Open Food Facts Cgi API
  slug: open-open-food-facts-cgi-api
- collection_type: open
  name: Open Food Facts Cgi Product API
  slug: open-open-food-facts-product-api
- collection_type: open
  name: Open Food Facts Cgi Search API
  slug: open-open-food-facts-search-api
- collection_type: open
  name: Open Food Facts Cgi Taxonomy API
  slug: open-open-food-facts-taxonomy-api
- collection_type: open
  name: Open Food Facts Cgi Taxonomy Suggestions API
  slug: open-open-food-facts-taxonomy-suggestions-api
- collection_type: open
  name: Open Food Facts API
  slug: open-open-food-facts
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/open-food-facts/refs/heads/main/scopes/open-food-facts-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/open-food-facts-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://world.openfoodfacts.org/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://openfoodfacts.github.io/openfoodfacts-server/api/
- group: docs
  title: ''
  type: Documentation
  url: https://openfoodfacts.github.io/openfoodfacts-server/
- group: docs
  title: ''
  type: APIReference
  url: https://openfoodfacts.github.io/openfoodfacts-server/api/ref-v2/
- group: start
  title: ''
  type: GettingStarted
  url: https://openfoodfacts.github.io/openfoodfacts-server/api/tutorial-off-api/
- group: operate
  title: ''
  type: Support
  url: https://forum.openfoodfacts.org/
- group: operate
  title: ''
  type: Roadmap
  url: https://wiki.openfoodfacts.org/Roadmap
- group: start
  title: ''
  type: SignUp
  url: https://world.openfoodfacts.org/cgi/user.pl
- group: commercial
  title: ''
  type: TermsOfService
  url: https://world.openfoodfacts.org/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://world.openfoodfacts.org/privacy
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/open-food-facts/refs/heads/main/agentic-access/open-food-facts-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/open-food-facts-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/open-food-facts/refs/heads/main/security/open-food-facts-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/open-food-facts-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/open-food-facts/refs/heads/main/security/open-food-facts-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/open-food-facts-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/open-food-facts/refs/heads/main/security/open-food-facts-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/open-food-facts-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/openfoodfacts
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/open-food-facts
- group: company
  title: ''
  type: Blog
  url: https://blog.openfoodfacts.org/en/feed/
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/open-food-facts/refs/heads/main/packages/open-food-facts-packages.yml
  title: ''
  type: Packages
  url: packages/open-food-facts-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/open-food-facts/refs/heads/main/packages/open-food-facts-packages.yml
  title: ''
  type: SDKs
  url: packages/open-food-facts-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/open-food-facts/refs/heads/main/components/open-food-facts-components.yml
  title: ''
  type: Components
  url: components/open-food-facts-components.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/open-food-facts/refs/heads/main/well-known/open-food-facts-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/open-food-facts-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/open-food-facts/refs/heads/main/well-known/open-food-facts-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/open-food-facts-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/open-food-facts/refs/heads/main/authentication/open-food-facts-authentication.yml
  title: ''
  type: Authentication
  url: authentication/open-food-facts-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/open-food-facts/refs/heads/main/errors/open-food-facts-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/open-food-facts-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/open-food-facts/refs/heads/main/conventions/open-food-facts-conventions.yml
  title: ''
  type: Conventions
  url: conventions/open-food-facts-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/open-food-facts/refs/heads/main/conformance/open-food-facts-conformance.yml
  title: ''
  type: Conformance
  url: conformance/open-food-facts-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/open-food-facts/refs/heads/main/lifecycle/open-food-facts-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/open-food-facts-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.openfoodfacts.org/
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/open-food-facts/refs/heads/main/lifecycle/open-food-facts-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/open-food-facts-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/open-food-facts/refs/heads/main/changelog/open-food-facts-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/open-food-facts-changelog.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/open-food-facts/refs/heads/main/rate-limits/open-food-facts-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/open-food-facts-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/open-food-facts/refs/heads/main/plans/open-food-facts-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/open-food-facts-plans-pricing.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/open-food-facts/refs/heads/main/sandbox/open-food-facts-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/open-food-facts-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/open-food-facts/refs/heads/main/vocabulary/open-food-facts-taxonomies.yml
  title: ''
  type: Vocabulary
  url: vocabulary/open-food-facts-taxonomies.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/open-food-facts/refs/heads/main/data-model/open-food-facts-data-model.yml
  title: ''
  type: DataModel
  url: data-model/open-food-facts-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/open-food-facts/refs/heads/main/llms/open-food-facts-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/open-food-facts-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/open-food-facts/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/open-food-facts/refs/heads/main/finops/open-food-facts-finops.yml
  title: ''
  type: FinOps
  url: finops/open-food-facts-finops.yml
created: '2025-03-01'
description: Open Food Facts is a collaborative, free and open database of food products from around the world, built by everyone for everyone. Anyone can scan a barcode and contribute product data, and the whole database is published under the Open Database License so it can be re-used for any purpose. The project publishes a documented public HTTP API for reading and writing product data, plus a family of companion services — Open Prices, Search-a-licious full-text search, the Folksonomy engine, facet knowledge panels and the NutriPatrol moderation API — alongside official SDKs in Python, JavaScript, Dart, Ruby, PHP and Go.
finops:
- name: Open Food Facts Finops
  service_category: API
  slug: open-food-facts-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/open-food-facts.png
layout: provider
modified: '2026-09-17'
name: Open Food Facts
nav: Providers
network: true
overview: 'Open Food Facts publishes 12 APIs on the [APIs.io](https://apis.io/) network, including API v2, API v3, Open Prices API, and 9 more. Tagged areas include Food, Nutrition, Open Data, Product Data, and Barcodes.


  Open Food Facts'' developer surface includes documentation, API reference, getting-started guide, support, signup flow, engineering blog, authentication, and 32 more developer resources.'
plans:
- name: Open Food Facts Plans Pricing
  plan_count: 0
  slug: open-food-facts-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 3
  name: Open Food Facts Rate Limits
  slug: open-food-facts-rate-limits
scopes:
- name: Open Food Facts Scopes
  scope_count: 0
  slug: open-food-facts-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 67.3
  coverage:
    artifact_dirs: 27
    catalog_earned: 57.0
    catalog_earned_first_party: 17.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 49.2
  facets:
    access_clarity: 42.1
    contract_governance: 19.7
    contract_quality: 50.6
    developer_ergonomics: 73.2
    discoverability: 68.5
    operational_transparency: 89.5
  previous_composite: 18.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 87.5
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 75.9
  schema_version: 0.22.0
  scored_at: '2026-09-17'
  trend: rising
  upsert:
    applies: true
    score: 33.3
screenshot: https://raw.githubusercontent.com/api-evangelist/open-food-facts/refs/heads/main/screenshots/open-food-facts-2026-06-20T190753.png
security:
- kind: authentication
  name: Open Food Facts Authentication
  slug: open-food-facts-authentication
  summary_line: apiKey/http/oauth2 · 4 schemes
- kind: domain-security
  name: Open Food Facts Domain Security
  slug: open-food-facts-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Open Food Facts Vulnerability Disclosure
  slug: open-food-facts-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: open-food-facts
tags:
- Food
- Nutrition
- Open Data
- Product Data
- Barcodes
- Taxonomy
- Prices
- Search
website: https://world.openfoodfacts.org/
---
