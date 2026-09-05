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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.8
  scored_at: '2026-09-04'
api_count: 5
apis:
- baseURL: https://api.gokonfetti.com/v1
  baseurl_source: declared
  description: Authenticated customer profile and registration.
  name: konfetti account API
  slug: konfetti-account-api
- baseURL: https://api.gokonfetti.com/v1
  baseurl_source: declared
  description: OAuth 2.0 token issuance.
  name: konfetti auth API
  slug: konfetti-auth-api
- baseURL: https://api.gokonfetti.com/v1
  baseurl_source: declared
  description: Public read access to experiences and categories.
  name: konfetti catalog API
  slug: konfetti-catalog-api
- baseURL: https://api.gokonfetti.com/v1
  baseurl_source: declared
  description: Cart validation, coupons and orders.
  name: konfetti checkout API
  slug: konfetti-checkout-api
- baseURL: https://api.gokonfetti.com/v1
  baseurl_source: declared
  description: Lead-capture endpoints for date and private-event requests.
  name: konfetti requests API
  slug: konfetti-requests-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
- group: agent
  title: ''
  type: AgentSkill
  url: skills/konfetti-search-experiences.md
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/konfetti-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/konfetti-store-overlay.yaml
- group: auth
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
  title: ''
  type: Components
  url: components/konfetti-components.yml
- group: build
  title: ''
  type: Packages
  url: packages/konfetti-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/konfetti-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/konfetti-lifecycle.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/konfetti-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/konfetti-llms.txt
created: '2026-07-17'
description: 'konfetti (Konfetti GmbH, Berlin) operates a marketplace for bookable experiences — cooking classes, pottery and ceramics workshops, cocktail courses, tastings, boat tours, creative and craft workshops, DIY kits and team events — across Germany and Austria, with more than 7,600 bookable experience listings and coverage in Berlin, Munich, Cologne, Hamburg, Frankfurt, Stuttgart, Dusseldorf, Leipzig, Dresden, Hannover, Nuremberg, Muenster, Heidelberg and Vienna. Alongside the consumer storefront, konfetti sells an all-in-one booking-management product to its partner hosts: a back-office at backoffice.gokonfetti.com for managing experiences, dates, tickets, gift cards, invoicing and payouts, plus an embeddable booking solution and a set of embeddable widgets that partners place on their own websites and social channels. konfetti is backed by Speedinvest. It publishes no public developer portal or API reference; the JSON API behind the storefront at api.gokonfetti.com is documented
  here observationally by API Evangelist.'
image: https://gokonfetti.com/_nuxt3-static/logos/kft-short-logo-white-bg.webp
layout: provider
modified: '2026-07-19'
name: konfetti
nav: Providers
network: true
overview: 'konfetti publishes 5 APIs on the [APIs.io](https://apis.io/) network, including account API, auth API, catalog API, and 2 more. Tagged areas include Company, Marketplace, Experience, Booking, and Event.


  konfetti''s developer surface includes support, FAQ, engineering blog, signup flow, developer portal, pricing, and 26 more developer resources.'
random_paper: 7
score:
  band: thin
  composite: 27.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 12.9
    developer_ergonomics: 30.4
    discoverability: 74.1
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 27.2
  provenance:
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
    score: 39.1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/konfetti/refs/heads/main/screenshots/konfetti-2026-07-25T224149.png
security:
- kind: authentication
  name: Konfetti Authentication
  slug: konfetti-authentication
  summary_line: none/http/oauth2 · 3 schemes
- kind: domain-security
  name: Konfetti Domain Security
  slug: konfetti-domain-security
  summary_line: TLSv1.3 · DMARC
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
