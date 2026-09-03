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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nsknox-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nsknox.net/
- group: other
  title: ''
  type: Technology
  url: https://nsknox.net/technology/
- group: operate
  title: ''
  type: Support
  url: https://nsknox.net/support/
- group: company
  title: ''
  type: Blog
  url: https://nsknox.net/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://nsknox.net/feed/
- group: company
  title: ''
  type: News
  url: https://nsknox.net/news/
- group: start
  title: ''
  type: Login
  url: https://nsknox.net/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nsknox.net/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nsknox.net/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nsKnox
- group: company
  title: ''
  type: Partners
  url: https://nsknox.net/partners/
- group: company
  title: ''
  type: About
  url: https://nsknox.net/about/
- group: company
  title: ''
  type: Careers
  url: https://nsknox.net/career/
- group: operate
  title: ''
  type: ContactSales
  url: https://nsknox.net/contact-us/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/nsKnoxTech
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/7972484/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nsknox-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/nsknox-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/nsknox-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nsknox-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nsknox-conformance.yml
- group: agent
  title: ''
  type: WellKnownProbe
  url: well-known/nsknox-well-known.yml
coverage:
  checked: '2026-08-26'
  detail: nsKnox markets "a full ERP API integration" for SAP and Oracle and an API interface into the PaymentKnox platform, but ships no developer portal — https://nsknox.net/docs/ answers 403 Forbidden, the site's own Yoast page sitemap lists 79 public pages and not one is a reference or spec, and every path on the PaymentKnox API host pknox.nsknox.net (read from the customer portals' own Content-Security-Policy connect-src) is intercepted by a BIG-IP WAF, so the contract is reachable only by an onboarded tenant.
  evidence:
  - status: 403
    url: https://nsknox.net/docs/
  - status: 404
    url: https://nsknox.net/openapi.json
  - status: 200
    url: https://pknox.nsknox.net/swagger.json
  - status: 404
    url: https://verify.nsknox.net/.well-known/agent-card.json
  reason: customer-only-docs
  state: gated
created: '2026-08-26'
description: nsKnox is an Israeli fintech-security company that protects business-to-business payments against fraud and misdirection for corporations and banks. Founded and led by Alon Cohen, the founder and former CEO of CyberArk, nsKnox built its platform on a patented Cooperative Cyber Security (CCS) architecture in which payment and bank-account data is shredded and distributed across multiple independent "Knoxer" systems so that no single breach reveals anything. Its PaymentKnox product line covers outgoing payments (accounts payable), incoming payments (accounts receivable), Bank Account Certificates, Master Data Guard, Payment Check, and an Adaptive Payment Security service that validates payee bank accounts worldwide using Quick Check in-network lookups and Knox Verify out-of-network mini-transactions against the banking system. Customers connect through a hosted portal, scheduled file transfer, or a direct ERP API integration with systems such as SAP and Oracle. nsKnox publishes
  no public developer portal, API reference, or machine-readable specification; the API surface is documented to onboarded customers only.
image: https://nsknox.net/wp-content/uploads/2021/04/nsknox-newlogo-dark-1.png
layout: provider
modified: '2026-08-26'
name: nsKnox
nav: Providers
network: true
overview: 'nsKnox is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, Payment Fraud, Financial-Services, Banking, and Security.


  nsKnox''s developer surface includes support, engineering blog, product news, and 20 more developer resources.'
plans:
- name: Nsknox Plans Pricing
  plan_count: 0
  slug: nsknox-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Nsknox Rate Limits
  slug: nsknox-rate-limits
score:
  band: emerging
  composite: 13.4
  coverage:
    artifact_dirs: 10
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 13.4
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 24.1
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nsknox/refs/heads/main/screenshots/nsknox-2026-09-02T150808.png
security:
- kind: domain-security
  name: Nsknox Domain Security
  slug: nsknox-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nsknox
tags:
- Payments
- Payment Fraud
- Financial-Services
- Banking
- Security
- Fraud Prevention
- Bank Account Validation
- Accounts Payable
- Accounts Receivable
- Fintech
- Compliance
- Israel
website: https://nsknox.net/
---
