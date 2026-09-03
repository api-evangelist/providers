---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/abpro-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://abpro.co/
- group: company
  title: ''
  type: About
  url: https://abpro.co/about-us/
- group: other
  title: ''
  type: Technology
  url: https://abpro.co/technology/
- group: other
  title: ''
  type: Pipeline
  url: https://abpro.co/pipeline/
- group: company
  title: ''
  type: News
  url: https://abpro.co/news/
- group: company
  title: ''
  type: Careers
  url: https://abpro.co/careers/
- group: operate
  title: ''
  type: Contact
  url: https://abpro.co/contact/
- group: company
  title: ''
  type: InvestorRelations
  url: https://investor.abpro.co/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://abpro.co/privacy-policy/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/abpro_stock/
coverage:
  checked: '2026-08-06'
  detail: Abpro is a clinical-stage antibody-therapeutics developer whose product is a drug pipeline rather than software, and its entire published surface is the 33-page corporate WordPress site listed in sitemap_index.xml — every developer path (/developers, /docs, /api, /graphql, /openapi.json) 404s and there is no github.com/abpro organization.
  evidence:
  - status: 404
    url: https://abpro.co/openapi.json
  - status: 404
    url: https://abpro.co/graphql
  - status: 404
    url: https://abpro.co/developers
  - status: 404
    url: https://abpro.co/.well-known/agent-card.json
  - status: 404
    url: https://abpro.co/.well-known/agent.json
  - status: 404
    url: https://abpro.co/llms.txt
  - status: 404
    url: https://api.github.com/orgs/abpro
  - status: 403
    url: https://investor.abpro.co/
  - status: 200
    url: https://abpro.co/sitemap_index.xml
  reason: not-a-software-company
  state: none
created: '2026-08-06'
description: 'Abpro Holdings, Inc. is a clinical-stage biotechnology company headquartered in the Boston area (Woburn / Burlington, Massachusetts) that develops next-generation multispecific antibody therapeutics for oncology and ophthalmology. Its DiversImmune antibody-discovery platform and MultiMab multispecific-engineering platform are used to build bispecific and tetravalent T-cell-engager constructs, led by ABP-102/CT-P72, a tetravalent bispecific HER2 x CD3 T-cell engager partnered with Celltrion, alongside the ABP-110, ABP-150 and ABP-201 programs. Abpro is a drug developer rather than a software company: its public web surface is a corporate and investor-relations site, and it publishes no developer program, public API, SDK, webhook surface, or machine-readable specification of any kind.'
image: https://abpro.co/wp-content/uploads/2023/05/Abpro_logo_with_trademark-transparent.png
layout: provider
modified: '2026-08-06'
name: Abpro
nav: Providers
network: true
overview: 'Abpro is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Antibody Therapeutics, and Oncology.


  Abpro''s developer surface includes product news and 10 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 6.2
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/abpro/refs/heads/main/screenshots/abpro-2026-08-07T160745.png
security:
- kind: domain-security
  name: Abpro Domain Security
  slug: abpro-domain-security
  summary_line: TLSv1.3
slug: abpro
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Antibody Therapeutics
- Oncology
- Life Sciences
- Drug Discovery
- Clinical Stage
website: https://abpro.co/
---
