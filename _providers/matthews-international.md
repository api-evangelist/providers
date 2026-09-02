---
access_model:
  confidence: high
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.matw.com
- group: company
  title: ''
  type: About
  url: https://www.matw.com/about
- group: company
  title: ''
  type: Blog
  url: https://www.matw.com/news-media
- group: operate
  title: ''
  type: ContactUs
  url: https://www.matw.com/contact
- group: company
  title: ''
  type: Careers
  url: https://www.matw.com/careers
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.matw.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.matw.com/terms-conditions
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/matthews-international
- group: auth
  title: ''
  type: DomainSecurity
  url: security/matthews-international-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/matthews-international-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/matthews-international-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/matthews-international-llms.txt
coverage:
  checked: '2026-08-13'
  detail: Matthews International is a 175-year-old manufacturer of memorial products, cremation equipment and industrial marking systems with no developer program of any kind — the api.matw.com and developer.matw.com hosts this profile carried were scaffold values that are both NXDOMAIN, matw.com serves no robots.txt and a 368-URL sitemap with not one developer, API or documentation page, and the only integration surface it markets is the MPERIA controller's on-premises XML / command-line protocol over Ethernet or RS-232, documented in equipment datasheets rather than a public reference.
  evidence:
  - status: 0
    url: https://developer.matw.com/
  - status: 0
    url: https://api.matw.com/
  - status: 404
    url: https://www.matw.com/openapi.json
  - status: 404
    url: https://www.matw.com/llms.txt
  - status: 404
    url: https://www.matw.com/.well-known/api-catalog
  - status: 404
    url: https://www.matw.com/.well-known/agent-card.json
  - status: 404
    url: https://matthewsmarking.com/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/matthewsintl
  - status: 200
    url: https://www.matw.com/sitemap.xml
  reason: no-developer-program
  state: none
created: '2026-04-19'
description: 'Matthews International Corporation (NASDAQ: MATW) is a Pittsburgh, Pennsylvania diversified manufacturer founded in 1850 and reporting in three segments. Memorialization covers bronze and granite memorials, caskets, cremation-related products and cremation and incineration equipment for the cemetery and funeral home industries, sold through Matthews Aurora Funeral Solutions and Matthews Environmental Solutions. Industrial Technologies covers product identification — the Matthews Marking Systems marking and coding business and its MPERIA controller platform — plus the design, manufacture and service of custom energy storage solutions including dry-battery-electrode coating and converting lines. Brand Solutions is now a 40% ownership interest in Propelis Group, the entity formed on 1 May 2025 when Matthews contributed the majority of its SGK brand business; the company sold its warehouse automation business (Matthews Automation Solutions — Pyramid, Compass and Lightning Pick)
  to Duravant on 31 December 2025. Matthews is a manufacturer rather than a software vendor: it operates no public developer program and publishes no API documentation, SDK, package, CLI, MCP server, agent card or machine-readable specification. The MPERIA controller sold with its marking and coding equipment markets a "common API" for ERP, WMS, MES and PLC integration, but that is an on-premises XML or command-line protocol carried over Ethernet or RS-232 and documented only in sales collateral — not a public web API.'
finops:
- name: Matthews International Finops
  service_category: Industrial / B2B Solutions
  slug: matthews-international-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/matthews-international.png
layout: provider
modified: '2026-08-13'
name: Matthews International
nav: Providers
network: true
overview: 'Matthews International is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Memorialization, Branding, Industrial, Manufacturing, and Marking and Coding.


  Matthews International''s developer surface includes engineering blog and 11 more developer resources.'
plans:
- name: Matthews International Plans Pricing
  plan_count: 1
  slug: matthews-international-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 1
  name: Matthews International Rate Limits
  slug: matthews-international-rate-limits
score:
  band: emerging
  composite: 18.9
  coverage:
    artifact_dirs: 8
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 18.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 18.9
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/matthews-international/refs/heads/main/screenshots/matthews-international-2026-06-20T185042.png
security:
- kind: domain-security
  name: Matthews International Domain Security
  slug: matthews-international-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: matthews-international
tags:
- Memorialization
- Branding
- Industrial
- Manufacturing
- Marking and Coding
- Energy Storage
- Funeral Services
- Company
website: https://www.matw.com
---
