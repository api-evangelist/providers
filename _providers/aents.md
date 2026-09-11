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
  scored_at: '2026-09-10'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aents-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aents.co/
- group: company
  title: ''
  type: About
  url: https://aents.co/about/
- group: commercial
  title: ''
  type: Pricing
  url: https://aents.co/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aents.co/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aents.co/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://aents.co/posts/
- group: company
  title: ''
  type: BlogRSS
  url: https://aents.co/posts/index.xml
- group: operate
  title: ''
  type: FAQ
  url: https://aents.co/faq/
- group: operate
  title: ''
  type: Contact
  url: https://aents.co/get-started/
- group: other
  title: ''
  type: CaseStudies
  url: https://aents.co/customers/
- group: operate
  title: ''
  type: PressReleases
  url: https://aents.co/press/
- group: company
  title: ''
  type: Newsletter
  url: https://aents.co/newsletter/
- group: start
  title: ''
  type: Login
  url: https://www.aentscope.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AENTS
- group: commercial
  title: ''
  type: Plans
  url: plans/aents-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/aents-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aents-llms.txt
coverage:
  checked: '2026-09-10'
  detail: 'AENTS sells AENTSCOPE as a tenant SaaS and an ESG consulting engagement, and its integration story runs INWARD — the platform consumes the KEPCO (한국전력) and Allbaro (올바로) APIs and customer ERP systems to collect activity data — so the company publishes no API of its own: /openapi.json, /swagger.json, /graphql, /llms.txt, /apis.json and every /.well-known/ path return the site''s own 404 page on both aents.co and www.aentscope.com, the only docs host (docs.aentscope.com, a GitBook space that historically served company PDFs) answers HTTP 401 on every path including a negative control, and the company GitHub org github.com/AENTS holds one public repository which is a front-end hiring assignment, not API code.'
  evidence:
  - status: 404
    url: https://aents.co/openapi.json
  - status: 404
    url: https://www.aentscope.com/openapi.json
  - status: 404
    url: https://aents.co/.well-known/api-catalog
  - status: 404
    url: https://aents.co/.well-known/agent-card.json
  - status: 401
    url: https://docs.aentscope.com/
  - status: 200
    url: https://api.github.com/orgs/AENTS/repos
  reason: no-developer-program
  state: none
created: '2026-09-10'
description: 'AENTS (엔츠) is a Seoul, South Korea climate-technology company founded in 2021 by CEO Gwangbeen Park and CTO Chongsoo Jung. Its product is AENTSCOPE (엔스코프), an enterprise carbon-management and carbon-accounting SaaS platform — described by the company as the first of its kind in Korea, launched in early 2022 — that lets a corporation build a greenhouse-gas inventory, automate Scope 1, 2 and 3 emissions calculation, run third-party verification, and produce disclosure reports aligned to KSSB, IFRS S2, CSRD, GRI, ISSB and CDP, alongside product carbon footprint (PCF/LCA), CBAM, climate physical-risk analysis and a supplier portal for Scope 3 value-chain data. AENTS pairs the platform with a climate-expert ESG consulting practice, and publishes a Korean-language blog, newsletter and a free corporate emissions calculator. Named customers include JYP, Nongshim, Woosung and Hansalim. The company raised a Series A led by Envisioning Partners in February 2023 and is also a Mashup Ventures
  portfolio company. AENTSCOPE is an API CONSUMER rather than an API producer: the company markets automated data collection through connections to external systems — the Korea Electric Power Corporation (한국전력/KEPCO) API, the Allbaro (올바로) national waste-management API, and customer ERP systems including SAP and Douzone — but publishes no public API, developer portal, OpenAPI, SDK or webhook surface of its own.'
image: https://aents.co/og-default.png
layout: provider
modified: '2026-09-10'
name: AENTS
nav: Providers
network: true
overview: 'AENTS is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Climate Tech, Carbon Accounting, Carbon Management, and ESG.


  AENTS''s developer surface includes pricing, engineering blog, FAQ, and 15 more developer resources.'
plans:
- name: Aents Plans Pricing
  plan_count: 0
  slug: aents-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Aents Rate Limits
  slug: aents-rate-limits
score:
  band: emerging
  composite: 13.4
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 18.9
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aents Domain Security
  slug: aents-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aents
tags:
- Company
- Climate Tech
- Carbon Accounting
- Carbon Management
- ESG
- Sustainability
- Greenhouse Gas
- Net Zero
- Emissions Reporting
- SaaS
- South Korea
website: https://aents.co/
---
