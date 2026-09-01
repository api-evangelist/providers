---
access_model:
  confidence: medium
  label: Partner Only
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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.0
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/securian-financial-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/securian-financial-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/securian-financial-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/securian-financial-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/securian-financial-rate-limits.yml
- group: company
  title: ''
  type: Website
  url: https://www.securian.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/securian-financial
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
  type: TermsOfService
  url: https://www.securian.com/legal-information.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.securian.com/privacy-notices.html
coverage:
  checked: '2026-08-28'
  detail: Securian runs a Kong gateway at api.securian.com that answers every request with "no Route matched with those values", and both integration products - FlexTech embedded protection and Securian Platform Connect - route to a sales contact form instead of any developer signup, reference or spec.
  evidence:
  - status: 404
    url: https://api.securian.com/openapi.json
  - status: 200
    url: https://www.securian.com/financial-institutions/products-solutions/embedded-technology-solutions.html
  - status: 0
    url: https://developer.securian.com/
  reason: sales-gate
  state: gated
created: '2026-03-21'
description: 'Securian Financial Group is a Saint Paul, Minnesota-based mutual holding company offering life insurance, annuities, institutional retirement solutions, trust services, investment management and group workplace benefits to individuals, employers, financial institutions and institutional clients across the United States and Canada. Its operating companies include Minnesota Life Insurance Company, Securian Life Insurance Company, Securian Asset Management and Securian Canada. Securian does not run a public developer program: its integration surfaces are partner-facing and sales-gated. Securian Platform Connect exchanges benefits data with employer benefits-administration platforms using LIMRA LDEx standards (Evidence of Insurability and Benefits Enrollment Management) plus SSO, API notifications and file feeds, and FlexTech - launched March 2026 with Walnut - embeds payment protection into digital lending journeys through API-based integration. Neither publishes a machine-readable
  contract, developer portal or self-service onboarding.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/securian-financial.png
layout: provider
modified: '2026-08-28'
name: Securian Financial
nav: Providers
network: true
overview: 'Securian Financial is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fortune 1000, Insurance, Life Insurance, Financial-Services, and Retirement.


  Securian Financial''s developer surface includes engineering blog, support, and 9 more developer resources.'
plans:
- name: Securian Financial Plans Pricing
  plan_count: 0
  slug: securian-financial-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Securian Financial Rate Limits
  slug: securian-financial-rate-limits
score:
  band: emerging
  composite: 11.6
  coverage:
    artifact_dirs: 11
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  previous_composite: 11.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 28.8
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Securian Financial Domain Security
  slug: securian-financial-domain-security
  summary_line: TLSv1.3 · DMARC
slug: securian-financial
tags:
- Fortune 1000
- Insurance
- Life Insurance
- Financial-Services
- Retirement
- Employee Benefits
- Annuities
- Asset Management
- Embedded Insurance
website: https://www.securian.com/
---
