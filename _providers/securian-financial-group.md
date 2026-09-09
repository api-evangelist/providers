---
access_model:
  confidence: high
  label: Partner/sales-gated — API access is arranged through a sales or partner agreement
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://www.securian.com/employers/flexible-administration/strategic-partnerships/securian-platform-connect.html
  - https://www.securian.com/financial-institutions/products-solutions/embedded-technology-solutions.html
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
  scored_at: '2026-09-08'
api_count: 0
artifact_total: 5
common:
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.securian.com/legal-information.html
- group: auth
  title: ''
  type: DomainSecurity
  url: security/securian-financial-group-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/securian-financial
- group: company
  title: ''
  type: Website
  url: https://www.securian.com/
- group: company
  title: ''
  type: Blog
  url: https://www.securian.com/about-us/newsroom/news-releases.html
- group: operate
  title: ''
  type: Support
  url: https://www.securian.com/contact-us.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.securian.com/privacy-notices.html
- group: agent
  title: ''
  type: WellKnown
  url: well-known/securian-financial-group-well-known.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: https://sso.securian.com/.well-known/openid-configuration
- group: auth
  title: ''
  type: Authentication
  url: authentication/securian-financial-group-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/securian-financial-group-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/securian-financial-group-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/securian-financial-group-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/securian-financial-group-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/securian-financial-group-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/securian-financial-group-llms.txt
created: '2026-04-07'
description: Securian Financial Group is a Minnesota-based mutual holding company providing life insurance, annuities, retirement plan solutions, investment management, group and workplace benefits, and credit-union and bank insurance programs to individuals, employers and financial institutions. Securian runs production API infrastructure — a Kong gateway at api.securian.com and AWS API Gateway hosts at api.connect.securian.com and api.lifebenefits.com — and markets API integrations through Securian Platform Connect (group benefits, aligned to LIMRA LDEx EOIS and BEM) and FlexTech (embedded payment protection for digital lenders), but publishes no developer portal, no API contract and no SDK. Its only anonymously readable machine-readable document is the OpenID Connect / OAuth 2.0 discovery metadata served by its PingFederate authorization server at sso.securian.com.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/securian-financial-group.png
layout: provider
modified: '2026-09-06'
name: Securian Financial Group
nav: Providers
network: true
overview: 'Securian Financial Group is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fortune 1000, Financial Services, Insurance, Life Insurance, and Annuities.


  Securian Financial Group''s developer surface includes engineering blog, support, authentication, and 13 more developer resources.'
plans:
- name: Securian Financial Group Plans Pricing
  plan_count: 0
  slug: securian-financial-group-plans-pricing
press:
- date: '2026-05-25'
  title: Artificial Intelligence
  url: https://www.securian.com/about-us/sustainability/inspiring-trust/artificial-intelligence.html
- date: '2026-05-25'
  title: Securian Financial Launches Industry-First AI-Enabled ...
  url: https://www.businesswire.com/news/home/20260203881829/en/Securian-Financial-Launches-Industry-First-AI-Enabled-Instant-Decision-and-Payment-Capabilities-for-Supplemental-Health-Insurance-Claims
- date: '2026-05-25'
  title: Securian Financial and Reclaim Health Now Paying Auto- ...
  url: https://www.securian.com/about-us/newsroom/news-releases/securian-financial-reclaim-health-paying-auto-substantiated-claims.html
- date: '2026-05-25'
  title: Digital Capabilities
  url: https://www.securian.com/employers/employee-engagement/digital-capabilities.html
- date: '2026-05-25'
  title: Securian Financial Group
  url: https://www.cuinsight.com/companies/securian-financial-group/
random_paper: 2
rate_limits:
- limit_count: 0
  name: Securian Financial Group Rate Limits
  slug: securian-financial-group-rate-limits
scopes:
- name: Securian Financial Group Scopes
  scope_count: 0
  slug: securian-financial-group-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 19.2
  coverage:
    artifact_dirs: 14
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 19.2
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 63.6
  schema_version: 0.20.0
  scored_at: '2026-09-08'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Securian Financial Group Authentication
  slug: securian-financial-group-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Securian Financial Group Domain Security
  slug: securian-financial-group-domain-security
  summary_line: TLSv1.3 · DMARC
slug: securian-financial-group
tags:
- Fortune 1000
- Financial Services
- Insurance
- Life Insurance
- Annuities
- Retirement
- Group Benefits
- Employee Benefits
website: https://www.securian.com/
---
