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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.6
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/gannett-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.usatodayco.com/responsible-disclosure-program/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gannett-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/gannett-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/gannett-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gannett-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/gannett-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/gannett-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/gannett-rate-limits.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gannett
- group: company
  title: ''
  type: Website
  url: https://www.usatodayco.com
- group: other
  title: ''
  type: USATodayNetwork
  url: https://www.usatoday.com
- group: other
  title: ''
  type: LocaliQ
  url: https://localiq.com
- group: company
  title: ''
  type: Blog
  url: https://localiq.com/blog/
- group: start
  title: ''
  type: Login
  url: https://localiq.com/login/
- group: other
  title: ''
  type: Brands
  url: https://www.usatodayco.com/brands/
- group: company
  title: ''
  type: News
  url: https://www.usatodayco.com/media-room/
- group: company
  title: ''
  type: Careers
  url: https://www.usatodayco.com/careers/
- group: company
  title: ''
  type: InvestorRelations
  url: https://investors.usatodayco.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.usatodayco.com/privacy-statement/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.usatodayco.com/terms-and-conditions/
- group: operate
  title: ''
  type: Contact
  url: https://www.usatodayco.com/contact/
coverage:
  checked: '2026-08-13'
  detail: Gannett runs no developer program at all — developer.gannett.com 301s to the www.usatodayco.com corporate homepage and developer.usatoday.com 301s to the www.usatoday.com consumer news site, api.usatoday.com returns 404, and /openapi.json, /swagger.json, /api-docs and /.well-known/agent-card.json miss on every Gannett, USA TODAY and LocaliQ host; the only machine-readable documents it serves are a security.txt, a Global Privacy Control signal and a WordPress-generated llms.txt on the LocaliQ blog.
  evidence:
  - status: 200
    url: https://developer.gannett.com/
  - status: 200
    url: https://developer.usatoday.com/
  - status: 404
    url: https://api.usatoday.com/
  - status: 403
    url: https://www.usatodayco.com/openapi.json
  - status: 404
    url: https://localiq.com/openapi.json
  - status: 200
    url: https://www.usatoday.com/.well-known/security.txt
  reason: no-developer-program
  state: none
created: '2026-05-04'
description: 'Gannett Co., Inc. is a diversified media and digital marketing solutions company and the publisher of USA TODAY and a network of more than 200 local daily newspapers across the United States. It now presents its corporate identity as USA TODAY Co. — www.gannett.com 301-redirects its corporate pages to www.usatodayco.com, and investors.gannett.com resolves to investors.usatodayco.com. Through the USA TODAY Network and LocaliQ, its digital marketing services arm for small and medium-sized businesses, Gannett delivers news, audience and advertising technology. Gannett publishes no developer portal, no API reference and no machine-readable API contract: developer.gannett.com and developer.usatoday.com both redirect to consumer sites, and no OpenAPI, AsyncAPI, GraphQL, MCP or A2A surface is served on any of its hosts. What it does publish machine-readably is a publisher-side control surface — an RFC 9116 security.txt, a Global Privacy Control signal, an llms.txt on localiq.com,
  and a 958-line robots.txt that denies the major AI crawlers site-wide while re-allowing a commercial subset of shopping, money and sponsor-content paths.'
image: https://www.gannett.com/favicon.ico
layout: provider
modified: '2026-08-13'
name: Gannett
nav: Providers
network: true
overview: 'Gannett is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Media, News, Publishing, Journalism, and Digital Marketing.


  Gannett''s developer surface includes engineering blog, product news, and 20 more developer resources.'
plans:
- name: Gannett Plans Pricing
  plan_count: 0
  slug: gannett-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Gannett Rate Limits
  slug: gannett-rate-limits
score:
  band: emerging
  composite: 16.4
  delta: -0.6
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 17.0
  provenance:
    conformance: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gannett/refs/heads/main/screenshots/gannett-2026-06-20T181644.png
security:
- kind: domain-security
  name: Gannett Domain Security
  slug: gannett-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Gannett Vulnerability Disclosure
  slug: gannett-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: gannett
tags:
- Media
- News
- Publishing
- Journalism
- Digital Marketing
- Advertising
- Local Marketing
- Content
website: https://www.usatodayco.com
---
