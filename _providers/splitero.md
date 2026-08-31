---
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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/splitero-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.splitero.com/
- group: company
  title: ''
  type: Blog
  url: https://www.splitero.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.splitero.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.splitero.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.splitero.com/terms-of-use
- group: start
  title: ''
  type: Login
  url: https://my.splitero.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SpliteroInc
- group: agent
  title: ''
  type: WellKnown
  url: well-known/splitero-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/splitero-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/splitero-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/splitero-rate-limits.yml
coverage:
  checked: '2026-08-29'
  detail: Splitero sells a consumer home equity investment through an authenticated web application at my.splitero.com; api.splitero.com, developers.splitero.com and docs.splitero.com do not resolve in DNS, and the only machine-readable document anywhere on the estate is the JWKS of its Stytch login tenant.
  evidence:
  - status: 403
    url: https://www.splitero.com/openapi.json
  - status: 404
    url: https://www.splitero.com/.well-known/api-catalog
  - status: 404
    url: https://www.splitero.com/.well-known/agent-card.json
  - status: 404
    url: https://www.splitero.com/llms.txt
  - status: 200
    url: https://my.splitero.com/openapi.json
  - status: 200
    url: https://auth.splitero.com/.well-known/jwks.json
  - status: 400
    url: https://auth.splitero.com/.well-known/openid-configuration
  reason: no-developer-program
  state: none
created: '2026-08-29'
description: 'Splitero is a San Diego, California fintech founded in 2021 by Michael Gifford and David Zvaifler that originates Home Equity Investments (HEIs) — a lump sum of cash, up to $500,000, paid to a homeowner today in exchange for a share of the home''s future value, with no monthly payments, no income requirement, credit scores accepted from 500, and terms of up to 30 years. The company operates a consumer application and servicing portal at my.splitero.com, funds its originations through institutional capital commitments (including a $350M facility led by Blue Owl Capital), and has expanded into a licensed residential brokerage, Splitero Homes. Splitero is an end-user consumer finance product: it publishes no developer portal, no public API, no SDKs and no machine-readable contract of any kind.'
image: https://www.splitero.com/apple-touch-icon.png
layout: provider
modified: '2026-08-29'
name: Splitero
nav: Providers
network: true
overview: 'Splitero is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial-Services, Fintech, Real-Estate, and Home Equity.


  Splitero''s developer surface includes engineering blog, support, and 10 more developer resources.'
plans:
- name: Splitero Plans Pricing
  plan_count: 0
  slug: splitero-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Splitero Rate Limits
  slug: splitero-rate-limits
score:
  band: emerging
  composite: 12.3
  coverage:
    artifact_dirs: 6
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 12.3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Splitero Domain Security
  slug: splitero-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: splitero
tags:
- Company
- Financial-Services
- Fintech
- Real-Estate
- Home Equity
- Lending
- Mortgage
- Consumer Finance
website: https://www.splitero.com/
---
