---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 20.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: The production 4.screen API. Automakers and mobility service providers integrate it into infotainment and navigation systems to render 4.screen content in the vehicle, and the 4.screen customer portal
  name: 4.screen Mobility Experience Cloud API
  slug: mobility-experience-cloud
artifact_total: 7
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/4screen-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/4screen-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://4screen.com/
- group: docs
  title: ''
  type: Documentation
  url: https://4screen.com/faqs/
- group: operate
  title: ''
  type: Support
  url: https://4screen.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://4screen.com/news/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/4screen
- group: start
  title: ''
  type: SignUp
  url: https://portal.4screen.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://4screen.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://4screen.com/advertising-conditions-europe/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/4screen/
- group: other
  title: ''
  type: CaseStudies
  url: https://4screen.com/case-studies/
- group: auth
  title: ''
  type: Authentication
  url: authentication/4screen-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/4screen-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/4screen-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/4screen-security.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/4screen-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/4screen-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/4screen-conventions.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/4screen-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/4screen-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/4screen-rate-limits.yml
- group: auth
  title: ''
  type: Security
  url: security/4screen-vulnerability-disclosure.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/4screen-problem-types.yml
coverage:
  checked: '2026-09-05'
  detail: 4.screen's API is real and central to the product — its own FAQ says automakers "can implement the 4screen API into their infotainment systems ... easily within days" — but api.4screen.com answers HTTP 401 AUTHENTICATION_FAILED on every path including /openapi.json, /v3/api-docs and /graphql, docs.4screen.com and developer.4screen.com do not resolve in DNS, and both the OEM page and the advertiser page replace a reference with a "Book an OEM Partnership Meeting" form. The only machine-readable contract 4.screen publishes anonymously is its Keycloak OIDC/OAuth discovery document.
  evidence:
  - status: 401
    url: https://api.4screen.com/v3/api-docs
  - status: 401
    url: https://api.4screen.com/openapi.json
  - status: 401
    url: https://api.4screen.com/graphql
  - status: 200
    url: https://4screen.com/4-automotives/
  - status: 200
    url: https://api.4screen.com/auth/realms/fourscreen/.well-known/openid-configuration
  reason: sales-gate
  state: gated
created: '2026-09-05'
description: '4.screen GmbH (Munich, Germany) operates the Driver Interaction Platform — a two-sided in-car marketplace connecting businesses with drivers in real time through the vehicle''s built-in navigation and infotainment screen. Its Mobility Experience Cloud (MXC) connects by API to automaker vehicle backends, and brands buy four placement formats through it: Branded Pins (a logo on the in-car map at a business location), Sponsored Search (paid ranking in in-car navigation results), Recommendations (context-aware offers driven by vehicle signals) and Detail Screen (an interactive promotion with engagement tracking). OEM partners include Audi, Volkswagen, Skoda, Nissan, Hyundai, Kia and the Stellantis brands; advertisers include McDonald''s, Shell, KFC, Waitrose, Kaufland and Coop. The API is real and central to the product, but entirely gated: api.4screen.com answers HTTP 401 on every path, and there is no public developer portal, reference or specification.'
image: https://4screen.com/wp-content/uploads/2024/06/4screen_logo.svg
layout: provider
modified: '2026-09-05'
name: 4.screen
nav: Providers
network: true
overview: '4.screen publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, AdTech, Automotive, and Mobility.


  4.screen''s developer surface includes documentation, support, engineering blog, signup flow, authentication, and 19 more developer resources.'
plans:
- name: 4Screen Plans Pricing
  plan_count: 0
  slug: 4screen-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: 4Screen Rate Limits
  slug: 4screen-rate-limits
scopes:
- name: 4Screen Scopes
  scope_count: 0
  slug: 4screen-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 20.7
  coverage:
    artifact_dirs: 13
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 13.2
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: authentication
  name: 4Screen Authentication
  slug: 4screen-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: 4Screen Domain Security
  slug: 4screen-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: 4Screen Vulnerability Disclosure
  slug: 4screen-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: 4screen
tags:
- Company
- Advertising
- AdTech
- Automotive
- Mobility
- Connected Vehicle
- In-Car Commerce
- Location
- Navigation
- Marketing
- Germany
website: https://4screen.com/
---
