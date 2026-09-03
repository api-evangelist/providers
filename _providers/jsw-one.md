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
  url: security/jsw-one-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.jswonemsme.com/
- group: company
  title: ''
  type: About
  url: https://www.jswonemsme.com/about-us
- group: operate
  title: ''
  type: Support
  url: https://www.jswonemsme.com/help-support
- group: company
  title: ''
  type: Blog
  url: https://www.jswonemsme.com/blogs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/JSWOne
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.jswonemsme.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.jswonemsme.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://www.jswonemsme.com/login
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/jsw-one-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/jsw-one-homes-llms.txt
coverage:
  checked: '2026-08-23'
  detail: JSW One is a B2B materials marketplace with no developer program of any kind - the api., developer., docs. and apis. subdomains of jswonemsme.com do not resolve in DNS, /openapi.json, /swagger.json, /graphql, /api-docs and every /.well-known/ path return a hard 404 on www.jswonemsme.com and www.jswonehomes.com, the 830-URL sitemap contains no developer or reference section, and the company's own GitHub org (github.com/JSWOne, 10 public repos) ships CI actions and internal automation but no SDK, spec or client library.
  evidence:
  - status: 404
    url: https://www.jswonemsme.com/openapi.json
  - status: 404
    url: https://www.jswonemsme.com/.well-known/agent-card.json
  - status: 200
    url: https://www.jswonemsme.com/sitemap.xml
  - status: 200
    url: https://www.jswonemsme.com/llms.txt
  - status: 200
    url: https://github.com/JSWOne
  reason: no-developer-program
  state: none
created: '2026-08-23'
description: 'JSW One Platforms is the digital B2B arm of India''s JSW Group, operating a full-stack e-commerce and services platform for the country''s manufacturing and construction MSMEs. It runs four connected businesses on one technology stack: JSW One Commerce (jswonemsme.com), a multi-brand marketplace for TMT bars, mild/hot-rolled/cold-rolled and structural steel, coated steel, wire rods, cement and bitumen sourced from certified mills; JSW One Homes (jswonehomes.com), a turnkey home-construction service with digital project tracking across fifteen Indian cities; JSW One Finance, the NBFC arm providing digital credit lines, channel financing and invoice factoring to MSMEs and retailers; and private brands JSW One TMT and One Helix. The platform reported FY25 gross merchandise value of INR 12,567 crore across more than 84,000 registered MSMEs, and raised INR 575 crore in a 2025 round led by the State Bank of India. JSW One publishes no public developer program, API reference or machine-readable
  contract; its customer-facing surfaces are the web marketplace and the JSW One MSME mobile apps. It does publish a maintained llms.txt on both of its consumer properties, plus an explicit AI/LLM bot-access policy on JSW One Homes.'
image: https://internal-assets.jswonemsme.com/JSW_One_Logo_footer_3f248bc727/JSW_One_Logo_footer_3f248bc727.svg
layout: provider
modified: '2026-08-23'
name: JSW One
nav: Providers
network: true
overview: 'JSW One is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, B2B Commerce, Marketplace, Construction, and Steel.


  JSW One''s developer surface includes support, engineering blog, and 9 more developer resources.'
plans:
- name: Jsw One Plans Pricing
  plan_count: 0
  slug: jsw-one-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Jsw One Rate Limits
  slug: jsw-one-rate-limits
score:
  band: emerging
  composite: 13.0
  coverage:
    artifact_dirs: 7
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
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 13.0
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jsw-one/refs/heads/main/screenshots/jsw-one-2026-09-02T150003.png
security:
- kind: domain-security
  name: Jsw One Domain Security
  slug: jsw-one-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: jsw-one
tags:
- Company
- B2B Commerce
- Marketplace
- Construction
- Steel
- Building Materials
- Manufacturing
- Supply Chain
- Embedded Finance
- MSME
- India
- E-Commerce
website: https://www.jswonemsme.com/
---
