---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
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
    error_semantics: false
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
  score: 17.6
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sentry-insurance-group-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sentryinsurance
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sentry
- group: company
  title: ''
  type: Website
  url: https://www.sentry.com
- group: company
  title: ''
  type: AboutUs
  url: https://www.sentry.com/about-us
- group: operate
  title: ''
  type: Support
  url: https://www.sentry.com/contact-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.sentry.com/what-we-offer/resources/articles/faqs
- group: company
  title: ''
  type: Blog
  url: https://www.sentry.com/about-us/company-news-and-events
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sentry.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sentry.com/terms-and-conditions
- group: start
  title: ''
  type: Login
  url: https://insight.sentry.com/login
- group: company
  title: ''
  type: Careers
  url: https://www.sentry.com/careers
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sentry-insurance-group-well-known.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/sentry-insurance-group-openid-configuration.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/sentry-insurance-group-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/sentry-insurance-group-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sentry-insurance-group-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sentry-insurance-group-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/sentry-insurance-group-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/sentry-insurance-group-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sentry-insurance-group-rate-limits.yml
coverage:
  checked: '2026-08-29'
  detail: 'Sentry Insurance ships insurance, not software: its 1,000+ URL sitemap.xml contains no /api, /developer or /docs path, its GitHub org holds 15 repositories that are all forks of third-party tooling, and the only machine-readable documents it serves anywhere are the OpenID Connect discovery files for the Okta tenant that logs customers into insight.sentry.com.'
  evidence:
  - status: 404
    url: https://www.sentry.com/developers
  - status: 404
    url: https://www.sentry.com/api
  - status: 404
    url: https://www.sentry.com/openapi.json
  - status: 404
    url: https://www.sentry.com/.well-known/api-catalog
  - status: 404
    url: https://www.dairylandinsurance.com/openapi.json
  - status: 200
    url: https://account.sentry.com/oauth2/default/.well-known/openid-configuration
  reason: no-developer-program
  state: none
created: '2026-03-24'
description: Sentry Insurance is a US mutual insurance holding company headquartered in Stevens Point, Wisconsin, writing commercial property and casualty insurance, workers' compensation, business auto and trucking coverage, group life and health, annuities and 401(k) retirement plans for businesses and individuals. Its personal-lines brand is Dairyland, acquired in 1966, which writes non-standard auto and motorcycle policies, and the group agreed to acquire The General from American Family Insurance. Sentry holds an AM Best Financial Strength Rating of A+ (Superior) and also operates SentryWorld, a golf and event venue. Sentry Insurance publishes no public API, developer portal or machine-readable product contract; business is transacted through appointed independent agents and authenticated customer portals. Not to be confused with Sentry (Functional Software, Inc.) at sentry.io, the unrelated application error-monitoring company.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sentry-insurance-group.png
layout: provider
modified: '2026-08-29'
name: Sentry Insurance
nav: Providers
network: true
overview: 'Sentry Insurance is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fortune 1000, Insurance, Property and Casualty Insurance, Commercial Insurance, and Workers Compensation.


  Sentry Insurance''s developer surface includes support, engineering blog, authentication, and 18 more developer resources.'
plans:
- name: Sentry Insurance Group Plans Pricing
  plan_count: 0
  slug: sentry-insurance-group-plans-pricing
press:
- date: '2026-05-25'
  title: Sentry Lloyds of TX 'AApi' Financial Strength Rating Affirmed
  url: https://www.spglobal.com/ratings/en/regulatory/article/-/view/type/HTML/id/133737
- date: '2026-05-25'
  title: APCIA Announces 2024 Class of Emerging Leaders
  url: https://www.publicnow.com/view/659C381469DE64D5A91998C958D93C8DB8C58B01
- date: '2026-05-25'
  title: David Shah-Pettyjohn, AINS - Claims Representative at ...
  url: https://www.linkedin.com/in/david-pettyjohn
- date: '2026-05-25'
  title: Affirms Ratings of Sentry Ins Group Members - Best's News
  url: https://news.ambest.com/newscontent.aspx?altsrc=149&refnum=233871
- date: '2026-05-25'
  title: Dairyland Privacy Policy
  url: https://www.dairylandinsurance.com/privacy
random_paper: 3
rate_limits:
- limit_count: 0
  name: Sentry Insurance Group Rate Limits
  slug: sentry-insurance-group-rate-limits
scopes:
- name: Sentry Insurance Group Scopes
  scope_count: 0
  slug: sentry-insurance-group-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 23.0
  coverage:
    artifact_dirs: 14
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 23.0
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 63.6
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
security:
- kind: authentication
  name: Sentry Insurance Group Authentication
  slug: sentry-insurance-group-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Sentry Insurance Group Domain Security
  slug: sentry-insurance-group-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sentry-insurance-group
tags:
- Fortune 1000
- Insurance
- Property and Casualty Insurance
- Commercial Insurance
- Workers Compensation
- Auto Insurance
- Retirement
- Annuities
- Mutual Insurance
- Financial-Services
- Trucking
- Wisconsin
- United States
website: https://www.sentry.com
---
