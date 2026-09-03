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
api_count: 1
apis:
- description: Lumin Digital's platform API and SDK surface, used by financial institutions and by ecosystem partners to integrate third-party products into the digital banking experience and to move data between th
  name: Lumin Digital Platform APIs
  slug: lumin-digital-platform
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://lumindigital.com/
- group: operate
  title: ''
  type: Support
  url: https://clients.lumindigital.com/
- group: company
  title: ''
  type: Blog
  url: https://lumindigital.com/insights/
- group: company
  title: ''
  type: BlogRSS
  url: https://lumindigital.com/feed/
- group: company
  title: ''
  type: News
  url: https://lumindigital.com/news/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lumindigital
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lumindigital.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lumindigital.com/privacy-policy/
- group: other
  title: ''
  type: AcceptableUsePolicy
  url: https://lumindigital.com/aup/
- group: other
  title: ''
  type: Accessibility
  url: https://lumindigital.com/accessibility/
- group: start
  title: ''
  type: Login
  url: https://clients.lumindigital.com/login
- group: auth
  title: ''
  type: Security
  url: https://lumindigital.com/security/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.lumindigital.com/
- group: auth
  title: ''
  type: Compliance
  url: conformance/lumin-digital-conformance.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lumin-digital-conformance.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/lumin-digital-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/lumin-digital-well-known.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/lumin-digital-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lumin-digital-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/lumin-digital-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/lumin-digital-cli.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lumin-digital-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lumin-digital-conventions.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/lumin-digital-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lumin-digital-rate-limits.yml
- group: design
  title: ''
  type: Components
  url: components/lumin-digital-components.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lumin-digital-llms.txt
coverage:
  checked: '2026-08-25'
  detail: Lumin Digital markets platform APIs, an SDK and a developer portal on lumindigital.com, but every developer path resolves into the client portal at clients.lumindigital.com, which 302s to /login?ReturnUrl= for /docs and for every other path including /.well-known/*, and the 31-page public sitemap contains no developer, API-reference or spec page at all.
  evidence:
  - status: 302
    url: https://clients.lumindigital.com/docs
  - status: 200
    url: https://lumindigital.com/page-sitemap.xml
  - status: 404
    url: https://api.demo.lumindigital.com/openapi.json
  - status: 200
    url: https://lumindigital.com/.well-known/security.txt
  reason: partner-login
  state: gated
created: '2026-08-25'
description: 'Lumin Digital is a cloud-native digital banking platform for credit unions and community banks, founded in 2016 by Jeff Chambers and headquartered in San Ramon, California. The platform is built on a single-tenant, microservices architecture and sits on top of an institution''s existing core banking processor, delivering retail banking, commercial banking, digital account opening, user engagement, risk management, digital marketing and data analytics as modules. Its extensibility layer is API- and SDK-based: Lumin publishes a client SDK and a partner API programme that connects the platform to a stated 200+ third-party fintech solutions, and a developer portal used by financial institutions and integration partners to move data into and out of digital banking. The API reference, SDK downloads and developer portal are reachable only through the authenticated client portal at clients.lumindigital.com, so no machine-readable contract is published publicly.'
image: https://lumindigital.com/wp-content/uploads/2024/07/logo-lumin-rev.svg
layout: provider
modified: '2026-08-25'
name: Lumin Digital
nav: Providers
network: true
overview: 'Lumin Digital publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Digital Banking, Banking, Credit Unions, Financial-Services, and Fintech.


  Lumin Digital''s developer surface includes support, engineering blog, product news, CLI, and 23 more developer resources.'
plans:
- name: Lumin Digital Plans Pricing
  plan_count: 0
  slug: lumin-digital-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Lumin Digital Rate Limits
  slug: lumin-digital-rate-limits
score:
  band: emerging
  composite: 18.9
  coverage:
    artifact_dirs: 14
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 18.2
    operational_transparency: 13.2
  previous_composite: 18.9
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 31.6
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lumin-digital/refs/heads/main/screenshots/lumin-digital-2026-09-02T150347.png
security:
- kind: domain-security
  name: Lumin Digital Domain Security
  slug: lumin-digital-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Lumin Digital Vulnerability Disclosure
  slug: lumin-digital-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Lumin Digital Trust Center
  slug: lumin-digital-trust-center
  summary_line: trust center published
slug: lumin-digital
tags:
- Digital Banking
- Banking
- Credit Unions
- Financial-Services
- Fintech
- Core Banking
- Digital Account Opening
- Payments
- Commercial Banking
- Software-as-a-Service
website: https://lumindigital.com/
---
