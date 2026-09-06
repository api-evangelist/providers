---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
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
  score: 2.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Public, unauthenticated Atlassian Statuspage v2 JSON API served on DolarApp's own status host. Exposes overall status, the ten monitored components (sign up, sign in, website, and card payments / bank
  name: DolarApp Status API
  slug: dolarapp-status-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dolarapp-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.arqfinance.com/
- group: company
  title: ''
  type: Blog
  url: https://www.arqfinance.com/en-MX/blog
- group: operate
  title: ''
  type: Support
  url: https://help.arqfinance.com/en
- group: operate
  title: ''
  type: HelpCenter
  url: https://help-business.arqfinance.com/en
- group: start
  title: ''
  type: SignUp
  url: https://business.arqfinance.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://business.arqfinance.com/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.arqfinance.com/en-MX/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.arqfinance.com/en-MX/legal/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dolarapp
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dolarapp.com/
- group: auth
  title: ''
  type: Security
  url: https://www.arqfinance.com/en-MX/responsible-disclosure-policy
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/dolarapp-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dolarapp-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dolarapp-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/dolarapp-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/dolarapp-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dolarapp-rate-limits.yml
coverage:
  checked: '2026-08-12'
  detail: DolarApp (rebranded ARQ) runs api.dolarapp.com purely as the backend for its own mobile and business apps — it answers every anonymous request, including /openapi.json and /.well-known/*, with HTTP 403 — and the crawlable site map carries no /developers, /docs or /api path in any of its twelve locales, so there is no public developer program to profile.
  evidence:
  - status: 403
    url: https://api.dolarapp.com/openapi.json
  - status: 200
    url: https://www.arqfinance.com/sitemap-0.xml
  - status: 0
    url: https://docs.arqfinance.com/
  - status: 404
    url: https://www.dolarapp.com/llms.txt
  - status: 404
    url: https://www.arqfinance.com/.well-known/agent-card.json
  reason: no-developer-program
  state: none
created: '2026-08-12'
description: DolarApp — rebranded to ARQ in March 2026 — is a Latin American cross-border fintech founded in Mexico in 2022 by former Revolut operators Fernando Terres, Zach Garman and Alvaro Correa. It gives consumers and businesses in Mexico, Argentina, Colombia and Brazil digital dollar (USDc) and euro (EURc) accounts, US ACH/wire receiving details, international cards accepted in 180+ countries, interbank-rate FX conversion, bulk supplier and contractor payouts, corporate cards with spend controls, and investment and credit products. It reports roughly two million users and is backed by Sequoia Capital, Founders Fund, Brevan Howard Digital, Y Combinator and Kaszek. DolarApp/ARQ runs a private API host at api.dolarapp.com for its own mobile and web applications but publishes no public developer program, documentation or machine-readable specification.
image: https://www.arqfinance.com/og-image-en.png
layout: provider
modified: '2026-08-12'
name: DolarApp
nav: Providers
network: true
overview: 'DolarApp publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Payments, Cross-Border Payments, and Banking.


  DolarApp''s developer surface includes engineering blog, support, signup flow, and 15 more developer resources.'
plans:
- name: Dolarapp Plans Pricing
  plan_count: 0
  slug: dolarapp-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Dolarapp Rate Limits
  slug: dolarapp-rate-limits
score:
  band: emerging
  composite: 17.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 28.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 17.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 31.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dolarapp/refs/heads/main/screenshots/dolarapp-2026-09-02T145251.png
security:
- kind: domain-security
  name: Dolarapp Domain Security
  slug: dolarapp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Dolarapp Vulnerability Disclosure
  slug: dolarapp-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: dolarapp
tags:
- Company
- Fintech
- Payments
- Cross-Border Payments
- Banking
- Digital Dollars
- Stablecoins
- Foreign Exchange
- Corporate Cards
- Latin America
website: https://www.arqfinance.com/
---
