---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.0
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Konfetti Agentic Access
  operation_count: 21
  slug: konfetti-agentic-access
  summary_line: 21 operations · 9 acting
api_count: 5
apis:
- baseURL: https://api.gokonfetti.com/v1
  baseurl_source: declared
  description: Authenticated customer profile and registration.
  name: konfetti Account API
  slug: konfetti-account-api
- baseURL: https://api.gokonfetti.com/v1
  baseurl_source: declared
  description: OAuth 2.0 token issuance.
  name: konfetti Auth API
  slug: konfetti-auth-api
- baseURL: https://api.gokonfetti.com/v1
  baseurl_source: declared
  description: Public read access to experiences and categories.
  name: konfetti Catalog API
  slug: konfetti-catalog-api
- baseURL: https://api.gokonfetti.com/v1
  baseurl_source: declared
  description: Cart validation, coupons and orders.
  name: konfetti Checkout API
  slug: konfetti-checkout-api
- baseURL: https://api.gokonfetti.com/v1
  baseurl_source: declared
  description: Lead-capture endpoints for date and private-event requests.
  name: konfetti Requests API
  slug: konfetti-requests-api
artifact_total: 24
collections:
- collection_type: open
  name: konfetti Store account API
  slug: open-konfetti-account-api
- collection_type: open
  name: konfetti Store account auth API
  slug: open-konfetti-auth-api
- collection_type: open
  name: konfetti Store account catalog API
  slug: open-konfetti-catalog-api
- collection_type: open
  name: konfetti Store account checkout API
  slug: open-konfetti-checkout-api
- collection_type: open
  name: konfetti Store account requests API
  slug: open-konfetti-requests-api
common:
- group: commercial
  href: https://artifacts.apis.io/konfetti/plans/konfetti-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/konfetti-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/konfetti/well-known/konfetti-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/konfetti-api-security.txt
- group: docs
  title: ''
  type: Documentation
  url: https://help.gokonfetti.com/
- group: agent
  href: https://artifacts.apis.io/konfetti/agentic-access/konfetti-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/konfetti-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/konfetti/rules/konfetti-rules.yml
  title: ''
  type: Spectral
  url: rules/konfetti-rules.yml
- group: design
  href: https://artifacts.apis.io/konfetti/json-ld/konfetti-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/konfetti-context.jsonld
- group: design
  href: https://artifacts.apis.io/konfetti/vocabulary/konfetti-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/konfetti-vocabulary.yml
- group: operate
  href: https://artifacts.apis.io/konfetti/lifecycle/konfetti-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/konfetti-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/konfetti/well-known/konfetti-join-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/konfetti-join-security.txt
- group: other
  href: https://artifacts.apis.io/konfetti/hosts/konfetti-hosts.yml
  title: ''
  type: Hosts
  url: hosts/konfetti-hosts.yml
- group: other
  href: https://artifacts.apis.io/konfetti/vendors/konfetti-vendors.yml
  title: ''
  type: Vendors
  url: vendors/konfetti-vendors.yml
- group: agent
  href: https://artifacts.apis.io/konfetti/skills/konfetti-search-experiences.md
  title: ''
  type: AgentSkill
  url: skills/konfetti-search-experiences.md
- group: agent
  href: https://artifacts.apis.io/konfetti/mcp/konfetti-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/konfetti-mcp.yml
- group: other
  href: https://artifacts.apis.io/konfetti/overlays/konfetti-store-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/konfetti-store-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/konfetti/security/konfetti-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/konfetti-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gokonfetti.com
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.gokonfetti.com
- group: operate
  title: ''
  type: Support
  url: https://help.gokonfetti.com
- group: operate
  title: ''
  type: FAQ
  url: https://gokonfetti.com/de-de/faq/
- group: company
  title: ''
  type: Blog
  url: https://gokonfetti.com/de-de/magazine/
- group: start
  title: ''
  type: SignUp
  url: https://gokonfetti.com/de-de/partner/
- group: start
  title: ''
  type: Login
  url: https://backoffice.gokonfetti.com/#/sign-in
- group: start
  title: ''
  type: Portal
  url: https://backoffice.gokonfetti.com
- group: commercial
  title: ''
  type: Pricing
  url: https://gokonfetti.com/de-de/partner/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gokonfetti.com/de-de/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gokonfetti.com/de-de/privacy-policy/
- group: other
  title: ''
  type: CookiePolicy
  url: https://www.iubenda.com/privacy-policy/79545710/cookie-policy
- group: other
  title: ''
  type: Accessibility
  url: https://gokonfetti.com/de-de/b2c/accessibility-declaration/
- group: commercial
  title: ''
  type: LegalNotice
  url: https://gokonfetti.com/de-de/impressum/
- group: company
  title: ''
  type: Press
  url: https://konfetti.notion.site/Pressebereich-konfetti-8ba576a989014ac9a6976509ab633332
- group: company
  title: ''
  type: Partners
  url: https://konfetti.notion.site/Werde-Kooperationspartner-9ab08775d1e14e329786dfc7ab5ed7b7
- group: company
  title: ''
  type: Jobs
  url: https://join.com/companies/gokonfetti
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/72680824/
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/gokonfetti/
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/gokonfetti/
- group: other
  title: ''
  type: Pinterest
  url: https://de.pinterest.com/gokonfetti/
- group: other
  title: ''
  type: Email
  url: mailto:hallo@gokonfetti.com
- group: design
  href: https://artifacts.apis.io/konfetti/components/konfetti-components.yml
  title: ''
  type: Components
  url: components/konfetti-components.yml
- group: design
  href: https://artifacts.apis.io/konfetti/conformance/konfetti-conformance.yml
  title: ''
  type: Conformance
  url: conformance/konfetti-conformance.yml
- group: design
  href: https://artifacts.apis.io/konfetti/lifecycle/konfetti-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/konfetti-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/konfetti/well-known/konfetti-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/konfetti-well-known.yml
created: '2026-07-17'
description: 'konfetti (Konfetti GmbH, Berlin) operates a marketplace for bookable experiences — cooking classes, pottery and ceramics workshops, cocktail courses, tastings, boat tours, creative and craft workshops, DIY kits and team events — across Germany and Austria, with more than 7,600 bookable experience listings and coverage in Berlin, Munich, Cologne, Hamburg, Frankfurt, Stuttgart, Dusseldorf, Leipzig, Dresden, Hannover, Nuremberg, Muenster, Heidelberg and Vienna. Alongside the consumer storefront, konfetti sells an all-in-one booking-management product to its partner hosts: a back-office at backoffice.gokonfetti.com for managing experiences, dates, tickets, gift cards, invoicing and payouts, plus an embeddable booking solution and a set of embeddable widgets that partners place on their own websites and social channels. konfetti is backed by Speedinvest. It publishes no public developer portal or API reference; the JSON API behind the storefront at api.gokonfetti.com is documented
  here observationally by API Evangelist.'
image: https://gokonfetti.com/_nuxt3-static/logos/kft-short-logo-white-bg.webp
json_schemas:
- name: CategoryPage
  property_count: 0
  slug: konfetti-category-page
- name: Category
  property_count: 7
  slug: konfetti-category
- name: Event
  property_count: 41
  slug: konfetti-event
- name: ListMeta
  property_count: 3
  slug: konfetti-list-meta
jsonld:
- class_count: 10
  name: Konfetti Context
  property_count: 73
  slug: konfetti-context
layout: provider
modified: '2026-07-19'
name: konfetti
nav: Providers
network: true
overview: 'konfetti is listed with 5 APIs on the [APIs.io](https://apis.io/) network, including Account API, Auth API, Catalog API, and 2 more. Tagged areas include Company, Marketplace, Experience, Booking, and Event.


  The konfetti catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  konfetti''s developer surface includes documentation, support, FAQ, engineering blog, signup flow, developer portal, pricing, and 34 more developer resources.'
plans:
- name: Konfetti Plans Pricing
  plan_count: 3
  slug: konfetti-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Konfetti Rate Limits
  slug: konfetti-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: konfetti API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: konfetti-rules
scopes:
- name: Konfetti Scopes
  scope_count: 0
  slug: konfetti-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 44.0
  coverage:
    artifact_dirs: 31
    catalog_earned: 77.8
    catalog_earned_first_party: 12.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 26.5
    developer_ergonomics: 39.9
    discoverability: 73.2
    operational_transparency: 18.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 44.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 31.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/konfetti/konfetti-2026-07-25T224149.png
security:
- kind: authentication
  name: Konfetti Authentication
  slug: konfetti-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Konfetti Domain Security
  slug: konfetti-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 2
skills:
- name: konfetti-search-experiences
  slug: konfetti-search-experiences
- name: konfetti-supplier-catalog
  slug: konfetti-supplier-catalog
slug: konfetti
tags:
- Company
- Marketplace
- Experience
- Booking
- Event
- Workshops
- Ticketing
- Gift Cards
- Travel And Leisure
- Germany
- Commerce
website: https://gokonfetti.com
---
