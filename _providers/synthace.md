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
  url: security/synthace-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.synthace.com/
- group: company
  title: ''
  type: Blog
  url: https://www.synthace.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.synthace.com/blog/rss.xml
- group: company
  title: ''
  type: About
  url: https://www.synthace.com/about
- group: operate
  title: ''
  type: ContactUs
  url: https://www.synthace.com/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.synthace.com/privacy-notice
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Synthace
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/synthace
- group: company
  title: ''
  type: Twitter
  url: https://x.com/synthace
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@synthace
- group: company
  title: ''
  type: Partners
  url: https://www.synthace.com/about/partners
- group: company
  title: ''
  type: News
  url: https://www.synthace.com/news-room
- group: build
  title: ''
  type: Packages
  url: packages/synthace-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/synthace-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/synthace-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/synthace-llms.txt
coverage:
  checked: '2026-08-29'
  detail: Synthace ships no developer surface at all - its Antha platform at antha.com is a tenant-only single-page app whose entire /api/* namespace answers every unauthenticated request with a blanket JSON 401, and the docs.synthace.com hostname resolves to a Google Workspace Drive sign-in for @synthace.com staff rather than to a public reference.
  evidence:
  - status: 401
    url: https://antha.com/api/v1
  - status: 401
    url: https://antha.com/api/openapi.json
  - status: 302
    url: http://docs.synthace.com/
  - status: 404
    url: https://www.synthace.com/openapi.json
  - status: 404
    url: https://www.synthace.com/llms.txt
  - status: 404
    url: https://www.synthace.com/.well-known/agent-card.json
  reason: customer-only-docs
  state: gated
created: '2026-08-29'
description: Synthace is a London-headquartered life-science software company (offices in London, Boston and San Diego) behind Antha, a cloud digital-experiment platform for R&D teams. The platform lets biologists design multifactorial Design of Experiments (DOE) and Quality by Design (QbD) studies, simulate them ahead of time, compile them into machine-executable protocols that run on third-party lab automation hardware (Tecan, Formulatrix, SPT Labtech and others), and capture the resulting experimental data and metadata in a single structured, AI-ready record. Synthace is delivered as an authenticated tenant application at antha.com rather than as a developer product - as of 2026-08-29 the company publishes no developer portal, no API reference, no SDKs and no machine-readable contract on any public host, and the platform's own /api/* surface answers every unauthenticated request with a blanket JSON 401.
image: https://www.synthace.com/hubfs/nb-icons/synthace-logo.svg
layout: provider
modified: '2026-08-29'
name: Synthace
nav: Providers
network: true
overview: 'Synthace is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Life Sciences, Biotechnology, Laboratory Automation, Design of Experiments, and Research and Development.


  Synthace''s developer surface includes engineering blog, YouTube channel, product news, and 14 more developer resources.'
plans:
- name: Synthace Plans Pricing
  plan_count: 0
  slug: synthace-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Synthace Rate Limits
  slug: synthace-rate-limits
score:
  band: minimal
  composite: 7.0
  coverage:
    artifact_dirs: 8
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 7.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/synthace/refs/heads/main/screenshots/synthace-2026-09-02T161629.png
security:
- kind: domain-security
  name: Synthace Domain Security
  slug: synthace-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: synthace
tags:
- Life Sciences
- Biotechnology
- Laboratory Automation
- Design of Experiments
- Research and Development
- Scientific Data
- Cloud Platform
- Company
website: https://www.synthace.com/
---
