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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/renew-financial-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://renewfinancial.com/
- group: company
  title: ''
  type: About
  url: https://renewfinancial.com/about
- group: company
  title: ''
  type: Blog
  url: https://renewfinancial.com/resources/blog
- group: operate
  title: ''
  type: Support
  url: https://renewfinancial.com/service-and-support-pace-financing-customers
- group: operate
  title: ''
  type: HelpCenter
  url: https://renewfinancial.com/resources/pace-faqs
- group: start
  title: ''
  type: SignUp
  url: https://applycontractors.renewfinancial.com
- group: start
  title: ''
  type: Login
  url: https://contractors.renewfinancial.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://renewfinancial.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://renewfinancial.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/renewfinancial
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/renewable-funding-llc
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/renewfinancial
- group: company
  title: ''
  type: Careers
  url: https://renewfinancial.com/careers
- group: other
  title: ''
  type: Licensing
  url: https://renewfinancial.com/lending-licenses
- group: company
  title: ''
  type: Investors
  url: https://renewfinancial.com/about/investors
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/renew-financial_stock/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/renew-financial-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/renew-financial-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/renew-financial-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/renew-financial-rate-limits.yml
coverage:
  checked: '2026-08-26'
  detail: api.renewfinancial.com is a live AWS API Gateway custom domain backing Renew Financial's contractor platform, but it answers every anonymous path with HTTP 403 {"message":"Forbidden"}, and the only door to it is the login form at contractors.renewfinancial.com — an SPA that returns a 200 HTML shell for every URL and exposes no spec, no docs and no developer sign-up.
  evidence:
  - status: 403
    url: https://api.renewfinancial.com/openapi.json
  - status: 403
    url: https://api.renewfinancial.com/
  - status: 200
    url: https://contractors.renewfinancial.com/login
  - status: 404
    url: https://renewfinancial.com/.well-known/api-catalog
  - status: 404
    url: https://renewfinancial.com/llms.txt
  reason: partner-login
  state: gated
created: '2026-08-26'
description: Renew Financial (Renew Financial Group LLC) is a specialty consumer finance company founded in 2008 and headquartered in Oakland, California that pioneered and administers Property Assessed Clean Energy (PACE) financing for residential energy efficiency, renewable energy, water efficiency and resiliency home improvements. It administers the CaliforniaFIRST program in California and RenewPACE in Florida, funding solar, HVAC, roofing, windows, landscaping, hurricane and seismic projects through a voluntary property tax assessment repaid over terms up to 30 years. The company is licensed by the California Department of Financial Protection and Innovation as a PACE Program Administrator (#60DBO-90653) and carries NMLS ID 1788120. Renew Financial runs a contractor technology platform and an online homeowner application, but publishes no public developer program, API documentation, SDK or machine-readable API contract.
image: https://renewfinancial.com/wp-content/uploads/2023/07/home-image-share.png
layout: provider
modified: '2026-08-26'
name: Renew Financial
nav: Providers
network: true
overview: 'Renew Financial is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial-Services, Lending, Consumer Finance, and PACE Financing.


  Renew Financial''s developer surface includes engineering blog, support, signup flow, and 18 more developer resources.'
plans:
- name: Renew Financial Plans Pricing
  plan_count: 0
  slug: renew-financial-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Renew Financial Rate Limits
  slug: renew-financial-rate-limits
score:
  band: emerging
  composite: 13.5
  coverage:
    artifact_dirs: 7
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 13.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 18.9
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
security:
- kind: domain-security
  name: Renew Financial Domain Security
  slug: renew-financial-domain-security
  summary_line: TLSv1.3 · DMARC
slug: renew-financial
tags:
- Company
- Financial-Services
- Lending
- Consumer Finance
- PACE Financing
- Home Improvement
- Clean Energy
- Energy Efficiency
- Solar
- Real-Estate
website: https://renewfinancial.com/
---
