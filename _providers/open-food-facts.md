---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
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
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 46
  human_in_the_loop: 0
  name: Open Food Facts Agentic Access
  operation_count: 136
  slug: open-food-facts-agentic-access
  summary_line: 136 operations · 46 acting
api_count: 8
apis:
- baseURL: https://world.openfoodfacts.org
  baseurl_source: spec
  description: The Cgi API from Open Food Facts — 1 operation(s) for cgi.
  name: Open Food Facts Cgi API
  slug: open-food-facts-cgi-api
- baseURL: https://world.openfoodfacts.org
  baseurl_source: spec
  description: The Product API from Open Food Facts — 3 operation(s) for product.
  name: Open Food Facts Product API
  slug: open-food-facts-product-api
- baseURL: https://world.openfoodfacts.net
  baseurl_source: spec
  description: The Search API from Open Food Facts — 1 operation(s) for search.
  name: Open Food Facts Search API
  slug: open-food-facts-search-api
- baseURL: https://world.openfoodfacts.org
  baseurl_source: spec
  description: The Taxonomy API from Open Food Facts — 1 operation(s) for taxonomy.
  name: Open Food Facts Taxonomy API
  slug: open-food-facts-taxonomy-api
- baseURL: https://world.openfoodfacts.org
  baseurl_source: spec
  description: The Taxonomy Suggestions API from Open Food Facts — 1 operation(s) for taxonomy suggestions.
  name: Open Food Facts Taxonomy Suggestions API
  slug: open-food-facts-taxonomy-suggestions-api
- baseURL: https://api.folksonomy.openfoodfacts.org
  baseurl_source: declared
  description: The Admin - Property Management API from Open Food Facts — 3 operation(s) for admin - property management.
  name: Open Food Facts Admin - Property Management API
  slug: open-food-facts-admin-property-management-api
- baseURL: https://api.folksonomy.openfoodfacts.org
  baseurl_source: declared
  description: The Admin - Value Management API from Open Food Facts — 2 operation(s) for admin - value management.
  name: Open Food Facts Admin - Value Management API
  slug: open-food-facts-admin-value-management-api
- baseURL: https://world.openfoodfacts.net
  baseurl_source: declared
  description: The auth API from Open Food Facts — 2 operation(s) for auth.
  name: Open Food Facts Auth API
  slug: open-food-facts-auth-api
- baseURL: https://world.openfoodfacts.net
  baseurl_source: declared
  description: Endpoints for user authentication and session management.
  name: Open Food Facts Authentication API
  slug: open-food-facts-authentication-api
- baseURL: https://world.openfoodfacts.net
  baseurl_source: declared
  description: The Autocomplete API from Open Food Facts — 1 operation(s) for autocomplete.
  name: Open Food Facts Autocomplete API
  slug: open-food-facts-autocomplete-api
- baseURL: https://world.openfoodfacts.net
  baseurl_source: declared
  description: The badges API from Open Food Facts — 3 operation(s) for badges.
  name: Open Food Facts Badges API
  slug: open-food-facts-badges-api
- baseURL: https://world.openfoodfacts.net
  baseurl_source: declared
  description: The challenges API from Open Food Facts — 2 operation(s) for challenges.
  name: Open Food Facts Challenges API
  slug: open-food-facts-challenges-api
- baseURL: https://world.openfoodfacts.net
  baseurl_source: declared
  description: The Document API from Open Food Facts — 1 operation(s) for document.
  name: Open Food Facts Document API
  slug: open-food-facts-document-api
- baseURL: https://world.openfoodfacts.net
  baseurl_source: declared
  description: The Flags API from Open Food Facts — 3 operation(s) for flags.
  name: Open Food Facts Flags API
  slug: open-food-facts-flags-api
- baseURL: https://world.openfoodfacts.net
  baseurl_source: declared
  description: The Health API from Open Food Facts — 1 operation(s) for health.
  name: Open Food Facts Health API
  slug: open-food-facts-health-api
- baseURL: https://world.openfoodfacts.net
  baseurl_source: declared
  description: Endpoints for uploading, cropping, rotating, and managing product images.
  name: Open Food Facts Images API
  slug: open-food-facts-images-api
- baseURL: https://api.folksonomy.openfoodfacts.org
  baseurl_source: declared
  description: Browse available keys and their possible values
  name: Open Food Facts Keys & Values API
  slug: open-food-facts-keys-values-api
- baseURL: https://world.openfoodfacts.net
  baseurl_source: declared
  description: Return different knowledge panels based on the facet provided.
  name: Open Food Facts Knowledge Panel API
  slug: open-food-facts-knowledge-panel-api
- baseURL: https://world.openfoodfacts.org
  baseurl_source: declared
  description: Endpoints for retrieving knowledge panels for tags and categories.
  name: Open Food Facts Knowledge Panels API
  slug: open-food-facts-knowledge-panels-api
- baseURL: https://world.openfoodfacts.net
  baseurl_source: declared
  description: The locations API from Open Food Facts — 7 operation(s) for locations.
  name: Open Food Facts Locations API
  slug: open-food-facts-locations-api
- baseURL: https://world.openfoodfacts.net
  baseurl_source: declared
  description: The Metrics API from Open Food Facts — 1 operation(s) for metrics.
  name: Open Food Facts Metrics API
  slug: open-food-facts-metrics-api
- baseURL: https://world.openfoodfacts.net
  baseurl_source: declared
  description: The moderation API from Open Food Facts — 4 operation(s) for moderation.
  name: Open Food Facts Moderation API
  slug: open-food-facts-moderation-api
- baseURL: https://world.openfoodfacts.net
  baseurl_source: declared
  description: Endpoints for retrieving nutrition-related data and facts.
  name: Open Food Facts Nutrients API
  slug: open-food-facts-nutrients-api
- baseURL: https://world.openfoodfacts.net
  baseurl_source: declared
  description: The Nutripatrol API from Open Food Facts — 1 operation(s) for nutripatrol.
  name: Open Food Facts Nutripatrol API
  slug: open-food-facts-nutripatrol-api
- baseURL: https://world.openfoodfacts.net
  baseurl_source: declared
  description: Endpoints for optical character recognition on product labels.
  name: Open Food Facts OCR API
  slug: open-food-facts-ocr-api
- baseURL: https://world.openfoodfacts.net
  baseurl_source: declared
  description: The Off Test API from Open Food Facts — 1 operation(s) for off test.
  name: Open Food Facts Off Test API
  slug: open-food-facts-off-test-api
- baseURL: https://world.openfoodfacts.net
  baseurl_source: declared
  description: The Open Food Facts Knowledge Panels API API from Open Food Facts — 1 operation(s) for open food facts knowledge panels api.
  name: Open Food Facts Open Food Facts Knowledge Panels API
  slug: open-food-facts-open-food-facts-knowledge-panels-api-api
- baseURL: https://world.openfoodfacts.net
  baseurl_source: declared
  description: Endpoints for personalized search and recommendations.
  name: Open Food Facts Personal Search API
  slug: open-food-facts-personal-search-api
- baseURL: https://world.openfoodfacts.net
  baseurl_source: declared
  description: The price-tags API from Open Food Facts — 2 operation(s) for price-tags.
  name: Open Food Facts Price Tags API
  slug: open-food-facts-price-tags-api
- baseURL: https://world.openfoodfacts.net
  baseurl_source: declared
  description: The prices API from Open Food Facts — 4 operation(s) for prices.
  name: Open Food Facts Prices API
  slug: open-food-facts-prices-api
- baseURL: https://world.openfoodfacts.org
  baseurl_source: declared
  description: Endpoints for retrieving product attribute groups and user preference importance values.
  name: Open Food Facts Product Attributes API
  slug: open-food-facts-product-attributes-api
- baseURL: https://api.folksonomy.openfoodfacts.org
  baseurl_source: declared
  description: CRUD operations for product tags and properties
  name: Open Food Facts Product Tags API
  slug: open-food-facts-product-tags-api
- baseURL: https://world.openfoodfacts.net
  baseurl_source: declared
  description: Endpoints for managing product data and information.
  name: Open Food Facts Products API
  slug: open-food-facts-products-api
- baseURL: https://world.openfoodfacts.net
  baseurl_source: declared
  description: The proofs API from Open Food Facts — 9 operation(s) for proofs.
  name: Open Food Facts Proofs API
  slug: open-food-facts-proofs-api
- baseURL: https://world.openfoodfacts.net
  baseurl_source: declared
  description: The receipt-items API from Open Food Facts — 2 operation(s) for receipt-items.
  name: Open Food Facts Receipt Items API
  slug: open-food-facts-receipt-items-api
- baseURL: https://world.openfoodfacts.net
  baseurl_source: declared
  description: Render html based on knowledge panels.
  name: Open Food Facts Render to HTML API
  slug: open-food-facts-render-to-html-api
- baseURL: https://world.openfoodfacts.net
  baseurl_source: declared
  description: The Robots.txt API from Open Food Facts — 1 operation(s) for robots.txt.
  name: Open Food Facts Robots.txt API
  slug: open-food-facts-robots-txt-api
- baseURL: https://world.openfoodfacts.net
  baseurl_source: declared
  description: The Schema API from Open Food Facts — 1 operation(s) for schema.
  name: Open Food Facts Schema API
  slug: open-food-facts-schema-api
- baseURL: https://world.openfoodfacts.net
  baseurl_source: declared
  description: The Search A Licious API API from Open Food Facts — 1 operation(s) for search a licious api.
  name: Open Food Facts Search A Licious API
  slug: open-food-facts-search-a-licious-api-api
- baseURL: https://world.openfoodfacts.net
  baseurl_source: declared
  description: The Stats API from Open Food Facts — 1 operation(s) for stats.
  name: Open Food Facts Stats API
  slug: open-food-facts-stats-api
- baseURL: https://world.openfoodfacts.net
  baseurl_source: declared
  description: The Status API from Open Food Facts — 1 operation(s) for status.
  name: Open Food Facts Status API
  slug: open-food-facts-status-api
- baseURL: https://world.openfoodfacts.net
  baseurl_source: declared
  description: Endpoints for getting suggestions to aid in product editing.
  name: Open Food Facts Suggestions API
  slug: open-food-facts-suggestions-api
- baseURL: https://api.folksonomy.openfoodfacts.org
  baseurl_source: declared
  description: System health and general API information
  name: Open Food Facts System API
  slug: open-food-facts-system-api
- baseURL: https://world.openfoodfacts.net
  baseurl_source: declared
  description: The Tickets API from Open Food Facts — 3 operation(s) for tickets.
  name: Open Food Facts Tickets API
  slug: open-food-facts-tickets-api
- baseURL: https://api.folksonomy.openfoodfacts.org
  baseurl_source: declared
  description: The User API from Open Food Facts — 1 operation(s) for user.
  name: Open Food Facts User API
  slug: open-food-facts-user-api
- baseURL: https://world.openfoodfacts.net
  baseurl_source: declared
  description: The users API from Open Food Facts — 3 operation(s) for users.
  name: Open Food Facts Users API
  slug: open-food-facts-users-api
artifact_total: 64
collections:
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
- group: other
  href: https://artifacts.apis.io/open-food-facts/capabilities/open-food-facts-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/open-food-facts-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/open-food-facts/overlays/open-food-facts-api-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/open-food-facts-api-v2-overlay.yaml
- group: other
  href: https://artifacts.apis.io/open-food-facts/overlays/open-food-facts-api-v3-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/open-food-facts-api-v3-overlay.yaml
- group: other
  href: https://artifacts.apis.io/open-food-facts/overlays/open-food-facts-open-prices-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/open-food-facts-open-prices-overlay.yaml
- group: other
  href: https://artifacts.apis.io/open-food-facts/overlays/open-food-facts-search-a-licious-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/open-food-facts-search-a-licious-overlay.yaml
- group: other
  href: https://artifacts.apis.io/open-food-facts/overlays/open-food-facts-folksonomy-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/open-food-facts-folksonomy-overlay.yaml
- group: other
  href: https://artifacts.apis.io/open-food-facts/overlays/open-food-facts-facets-knowledge-panels-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/open-food-facts-facets-knowledge-panels-overlay.yaml
- group: other
  href: https://artifacts.apis.io/open-food-facts/overlays/open-food-facts-nutripatrol-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/open-food-facts-nutripatrol-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/open-food-facts/scopes/open-food-facts-scopes.yml
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
  href: https://artifacts.apis.io/open-food-facts/agentic-access/open-food-facts-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/open-food-facts-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/open-food-facts/security/open-food-facts-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/open-food-facts-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/open-food-facts/security/open-food-facts-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/open-food-facts-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/open-food-facts/security/open-food-facts-domain-security.yml
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
  href: https://artifacts.apis.io/open-food-facts/packages/open-food-facts-packages.yml
  title: ''
  type: Packages
  url: packages/open-food-facts-packages.yml
- group: build
  href: https://artifacts.apis.io/open-food-facts/packages/open-food-facts-packages.yml
  title: ''
  type: SDKs
  url: packages/open-food-facts-packages.yml
- group: design
  href: https://artifacts.apis.io/open-food-facts/components/open-food-facts-components.yml
  title: ''
  type: Components
  url: components/open-food-facts-components.yml
- group: agent
  href: https://artifacts.apis.io/open-food-facts/well-known/open-food-facts-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/open-food-facts-well-known.yml
- group: auth
  href: https://artifacts.apis.io/open-food-facts/well-known/open-food-facts-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/open-food-facts-security.txt
- group: auth
  href: https://artifacts.apis.io/open-food-facts/authentication/open-food-facts-authentication.yml
  title: ''
  type: Authentication
  url: authentication/open-food-facts-authentication.yml
- group: design
  href: https://artifacts.apis.io/open-food-facts/errors/open-food-facts-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/open-food-facts-problem-types.yml
- group: design
  href: https://artifacts.apis.io/open-food-facts/conventions/open-food-facts-conventions.yml
  title: ''
  type: Conventions
  url: conventions/open-food-facts-conventions.yml
- group: design
  href: https://artifacts.apis.io/open-food-facts/conformance/open-food-facts-conformance.yml
  title: ''
  type: Conformance
  url: conformance/open-food-facts-conformance.yml
- group: design
  href: https://artifacts.apis.io/open-food-facts/lifecycle/open-food-facts-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/open-food-facts-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.openfoodfacts.org/
- group: operate
  href: https://artifacts.apis.io/open-food-facts/lifecycle/open-food-facts-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/open-food-facts-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/open-food-facts/changelog/open-food-facts-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/open-food-facts-changelog.yml
- group: operate
  href: https://artifacts.apis.io/open-food-facts/rate-limits/open-food-facts-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/open-food-facts-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/open-food-facts/plans/open-food-facts-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/open-food-facts-plans-pricing.yml
- group: start
  href: https://artifacts.apis.io/open-food-facts/sandbox/open-food-facts-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/open-food-facts-sandbox.yml
- group: design
  href: https://artifacts.apis.io/open-food-facts/vocabulary/open-food-facts-taxonomies.yml
  title: ''
  type: Vocabulary
  url: vocabulary/open-food-facts-taxonomies.yml
- group: design
  href: https://artifacts.apis.io/open-food-facts/data-model/open-food-facts-data-model.yml
  title: ''
  type: DataModel
  url: data-model/open-food-facts-data-model.yml
- group: agent
  href: https://artifacts.apis.io/open-food-facts/llms/open-food-facts-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/open-food-facts-llms.txt
- group: agent
  href: https://artifacts.apis.io/open-food-facts/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/open-food-facts/finops/open-food-facts-finops.yml
  title: ''
  type: FinOps
  url: finops/open-food-facts-finops.yml
- group: design
  title: ''
  type: SpectralRules
  url: https://github.com/openfoodfacts/robotoff/blob/4019f07251fb12191c445c852009cd8135b848de/.spectral.yml
created: '2025-03-01'
description: Open Food Facts is a collaborative, free and open database of food products from around the world, built by everyone for everyone. Anyone can scan a barcode and contribute product data, and the whole database is published under the Open Database License so it can be re-used for any purpose. The project publishes a documented public HTTP API for reading and writing product data, plus a family of companion services — Open Prices, Search-a-licious full-text search, the Folksonomy engine, facet knowledge panels and the NutriPatrol moderation API — alongside official SDKs in Python, JavaScript, Dart, Ruby, PHP and Go.
finops:
- has_sources: true
  method: derived
  name: Open Food Facts Finops
  primary_unit: ''
  service_category: ''
  slug: open-food-facts-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/open-food-facts.png
layout: provider
modified: '2026-09-17'
name: Open Food Facts
nav: Providers
network: true
overview: 'Open Food Facts publishes 46 API contracts indexed on the [APIs.io](https://apis.io/) network, including Cgi API, Product API, Search API, and 43 more. Tagged areas include Food, Nutrition, Open Data, Product Data, and Barcodes.


  The Open Food Facts catalog on APIs.io includes 1 Spectral governance ruleset.


  Open Food Facts'' developer surface includes documentation, API reference, getting-started guide, support, signup flow, engineering blog, authentication, and 41 more developer resources.'
plans:
- name: Open Food Facts Plans Pricing
  plan_count: 0
  slug: open-food-facts-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 3
  name: Open Food Facts Rate Limits
  slug: open-food-facts-rate-limits
rules:
- authorship: provider
  effective_rule_count: 47
  extends:
  - spectral:oas
  name: Open Food Facts — robotoff rules
  rule_count: 6
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 3
  slug: open-food-facts-robotoff-spectral-rules
scopes:
- name: Open Food Facts Scopes
  scope_count: 0
  slug: open-food-facts-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 65.1
  coverage:
    artifact_dirs: 32
    catalog_earned: 67.0
    catalog_earned_first_party: 32.0
    catalog_gap: 48.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 34.2
    contract_governance: 65.2
    contract_quality: 47.8
    developer_ergonomics: 73.2
    discoverability: 62.5
    operational_transparency: 84.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 64.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 30.4
      derived: 0
      marker_coverage: 58.7
      total: 46
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 40.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 33.3
screenshot: https://apis.io/screenshots/open-food-facts/open-food-facts-2026-06-20T190753.png
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
skill_count: 3
skills:
- name: open-food-facts-contribute-product-edit
  slug: open-food-facts-contribute-product-edit
- name: open-food-facts-lookup-product-by-barcode
  slug: open-food-facts-lookup-product-by-barcode
- name: open-food-facts-search-products
  slug: open-food-facts-search-products
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
- Food and Beverage
website: https://world.openfoodfacts.org/
---
