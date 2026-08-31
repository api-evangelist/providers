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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mutual-of-america-life-insurance-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/mutual-of-america-life-insurance-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mutual-of-america-life-insurance-authentication.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/mutual-of-america-life-insurance-openid-configuration.json
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/mutual-of-america-life-insurance-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mutual-of-america-life-insurance-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mutual-of-america-life-insurance-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/mutual-of-america-life-insurance-plans-pricing.yml
- group: company
  title: ''
  type: Website
  url: https://www.mutualofamerica.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mutualofamerica
- group: operate
  title: ''
  type: Support
  url: https://www.mutualofamerica.com/customer-support
- group: company
  title: ''
  type: Blog
  url: https://www.mutualofamerica.com/insights-and-tools/learning-center/articles
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mutualofamerica.com/legal-information
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mutualofamerica.com/Privacy-Page
- group: start
  title: ''
  type: Login
  url: https://login.mutualofamerica.com
coverage:
  checked: '2026-08-28'
  detail: 'Mutual of America ships software only as an end-user product — a plan administration portal, online enrollment and a mobile app — and publishes no developer program: no developer/api/docs subdomain resolves, the 255-URL sitemap contains no developer or API page, and the only integration it markets (Payroll Integration, "Premier" and "Standard") is described in prose as a payroll file transfer with no published file layout, standard, or endpoint.'
  evidence:
  - status: 404
    url: https://www.mutualofamerica.com/openapi.json
  - status: 404
    url: https://www.mutualofamerica.com/llms.txt
  - status: 200
    url: https://www.mutualofamerica.com/employers/services/payroll-integration
  - status: 404
    url: https://api.github.com/orgs/mutualofamerica
  - status: 200
    url: https://login.mutualofamerica.com/.well-known/openid-configuration
  reason: no-developer-program
  state: none
created: '2026-03-24'
description: Mutual of America Life Insurance Company is a mutual life insurance and retirement services provider headquartered in New York City, offering employer-sponsored retirement plans — 401(k), 403(b), 401(a) and 457 deferred compensation — alongside individual retirement products including Traditional, Roth, Rollover, Managed, Self-Select and Inherited IRAs, flexible premium annuities and interest-account and investment options. It serves nonprofit, business, governmental and tribal employers and their employees through a plan administration portal, payroll integration services, online enrollment and salary deferral, and automatic enrollment. Mutual of America publishes no public developer program, API reference or machine-readable API contract; the only machine-readable discovery documents it serves are the OpenID Connect and OAuth 2.0 authorization-server metadata on its customer identity host, login.mutualofamerica.com.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mutual-of-america-life-insurance.png
layout: provider
modified: '2026-08-28'
name: Mutual of America Life Insurance Company
nav: Providers
network: true
overview: 'Mutual of America Life Insurance Company is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Life Insurance, Retirement, Financial-Services, and Pensions.


  Mutual of America Life Insurance Company''s developer surface includes authentication, support, engineering blog, and 12 more developer resources.'
plans:
- name: Mutual Of America Life Insurance Plans Pricing
  plan_count: 0
  slug: mutual-of-america-life-insurance-plans-pricing
press:
- date: '2026-05-25'
  title: Mutual of America Financial Group - Overview, News & ...
  url: https://www.zoominfo.com/c/mutual-of-america-life-insurance-co/71911491
- date: '2026-05-25'
  title: Virtual Assistant Important Information
  url: https://www.mutualofamerica.com/virtual-assistant-important-information
- date: '2026-05-25'
  title: 'Economic & Market Perspective: Year-End 2025 and 2026 ...'
  url: https://www.mutualofamerica.com/insights-and-tools/learning-center/emp/economic--market-perspective-january-2026
- date: '2026-05-25'
  title: Mutual of America Financial Group Names Christine ...
  url: https://www.prnewswire.com/news-releases/mutual-of-america-financial-group-names-christine-janofsky-as-executive-vice-president-chief-financial-officer-302459614.html
- date: '2026-05-25'
  title: What are some key issues investors should keep an eye on ...
  url: https://www.facebook.com/MutualofAmerica/posts/what-are-some-key-issues-investors-should-keep-an-eye-on-in-2026-joe-gaffoglio-p/866224722689607/
random_paper: 13
rate_limits:
- limit_count: 0
  name: Mutual Of America Life Insurance Rate Limits
  slug: mutual-of-america-life-insurance-rate-limits
scopes:
- name: Mutual Of America Life Insurance Scopes
  scope_count: 0
  slug: mutual-of-america-life-insurance-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 22.0
  coverage:
    artifact_dirs: 13
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
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  previous_composite: 22.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 63.6
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Mutual Of America Life Insurance Authentication
  slug: mutual-of-america-life-insurance-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Mutual Of America Life Insurance Domain Security
  slug: mutual-of-america-life-insurance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mutual-of-america-life-insurance
tags:
- Insurance
- Life Insurance
- Retirement
- Financial-Services
- Pensions
- Annuities
- Wealth Management
- Identity
website: https://www.mutualofamerica.com
---
