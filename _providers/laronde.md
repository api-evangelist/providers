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
  url: security/laronde-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sail.bio/
- group: company
  title: ''
  type: About
  url: https://www.sail.bio/about-us/
- group: company
  title: ''
  type: News
  url: https://www.sail.bio/news/
- group: company
  title: ''
  type: Blog
  url: https://www.sail.bio/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.sail.bio/feed/
- group: company
  title: ''
  type: Careers
  url: https://www.sail.bio/careers/
- group: operate
  title: ''
  type: Contact
  url: https://www.sail.bio/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sail.bio/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sail.bio/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sail-biomedicines
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/SailBiomeds
- group: company
  title: ''
  type: Investor
  url: https://www.flagshippioneering.com/companies/sail-biomedicines
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/laronde_stock/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/laronde-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/laronde-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/laronde-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/laronde-rate-limits.yml
coverage:
  checked: '2026-08-23'
  detail: Sail Biomedicines (the company behind this profile's legacy `laronde` slug, formed when Flagship Pioneering merged Laronde and Senda Biosciences in October 2023) is a preclinical biopharmaceutical company whose product is an in vivo CAR-T drug pipeline, not software — www.sail.bio is a 14-page WordPress marketing site on WP Engine that returns an honest 404 for every OpenAPI, GraphQL, llms.txt and /.well-known/ path, api./docs./developer./data./mcp. and every other developer subdomain are NXDOMAIN, and no package exists on npm, PyPI, RubyGems or crates.io; the site's only machine-readable surface is the stock WordPress core REST API at /wp-json/, which is the CMS, not a published API.
  evidence:
  - status: 200
    url: https://www.sail.bio/
  - status: 404
    url: https://www.sail.bio/openapi.json
  - status: 404
    url: https://www.sail.bio/graphql
  - status: 404
    url: https://www.sail.bio/llms.txt
  - status: 404
    url: https://www.sail.bio/.well-known/security.txt
  - status: 404
    url: https://www.sail.bio/.well-known/agent-card.json
  - status: 200
    url: https://www.sail.bio/wp-json/
  - status: 404
    url: https://pypi.org/pypi/sailbio/json
  reason: not-a-software-company
  state: none
created: '2026-08-23'
description: 'Sail Biomedicines is a Cambridge, Massachusetts preclinical biotechnology company created in October 2023 by Flagship Pioneering through the merger of Laronde and Senda Biosciences, and it is the company this profile''s legacy `laronde` slug refers to. Sail combines Laronde''s Endless RNA (eRNA) platform — synthetic circular RNA engineered to be translated persistently inside the body — with Senda''s programmable lipid and natural nanoparticle delivery chemistry, and layers generative AI on the combined dataset to design what the company calls fully programmable medicines. Its lead effort is in vivo CAR-T for autoimmune disease: instructing a patient''s own T cells to reprogram themselves inside the body rather than extracting, engineering and reinfusing them, an approach Sail markets as "immune reset". In July 2026 Johnson & Johnson committed $785 million up front (including a $465 million equity investment) plus up to $140 million in milestones and took an exclusive option
  to acquire the company for a further $2.58 billion. Sail sells therapeutics, not software: it publishes no API, no SDK, no machine-readable specification and no developer documentation, and it operates no public source-code organization.'
image: https://www.sail.bio/wp-content/uploads/2024/05/sail-logo-primary-dark.svg
layout: provider
modified: '2026-08-23'
name: Sail Biomedicines
nav: Providers
network: true
overview: 'Sail Biomedicines is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, RNA, and Circular RNA.


  Sail Biomedicines'' developer surface includes product news, engineering blog, and 16 more developer resources.'
plans:
- name: Laronde Plans Pricing
  plan_count: 0
  slug: laronde-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Laronde Rate Limits
  slug: laronde-rate-limits
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 8
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/laronde/refs/heads/main/screenshots/laronde-2026-09-02T150209.png
security:
- kind: domain-security
  name: Laronde Domain Security
  slug: laronde-domain-security
  summary_line: TLSv1.3 · DMARC
slug: laronde
tags:
- Company
- Biotechnology
- Pharmaceuticals
- RNA
- Circular RNA
- Cell Therapy
- Cart
- Nanoparticles
- Drug Discovery
- Immunology
- Autoimmune Disease
- Life Sciences
- Artificial Intelligence
- Preclinical
website: https://www.sail.bio/
---
