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
- group: company
  title: ''
  type: Website
  url: https://iliadbio.com/
- group: company
  title: ''
  type: About
  url: https://iliadbio.com/company/overview.html
- group: company
  title: ''
  type: News
  url: https://iliadbio.com/company/news.html
- group: company
  title: ''
  type: Investors
  url: https://iliadbio.com/company/for-investors.html
- group: company
  title: ''
  type: Careers
  url: https://iliadbio.com/careers.html
- group: operate
  title: ''
  type: ContactUs
  url: https://iliadbio.com/contact-us.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://iliadbio.com/privacy-policy.html
- group: auth
  title: ''
  type: DomainSecurity
  url: security/iliad-biotechnologies-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/iliad-biotechnologies-llms.txt
- group: other
  title: ''
  type: Team
  url: https://iliadbio.com/team/executive-board.html
- group: other
  title: ''
  type: Product
  url: https://iliadbio.com/our_science/bpze1_vaccine.html
- group: other
  title: ''
  type: Pipeline
  url: https://iliadbio.com/opportunity/pipeline.html
- group: other
  title: ''
  type: Publications
  url: https://iliadbio.com/our_science/publications.html
coverage:
  checked: '2026-08-22'
  detail: ILiAD Biotechnologies is a clinical-stage vaccine developer whose product is BPZE1, a live attenuated intranasal pertussis vaccine in human trials — not software — and iliadbio.com is an 88-page static HTML site of science, patent PDFs and press releases where /openapi.json, /graphql, /api-docs, /llms.txt and every /.well-known/ path return a real 404, and api./docs./developer.iliadbio.com do not resolve in DNS.
  evidence:
  - status: 404
    url: https://iliadbio.com/openapi.json
  - status: 404
    url: https://iliadbio.com/graphql
  - status: 404
    url: https://iliadbio.com/.well-known/agent-card.json
  - status: 404
    url: https://iliadbio.com/llms.txt
  - status: 404
    url: https://iliadbiotech.com/.well-known/security.txt
  reason: not-a-software-company
  state: none
created: '2026-08-22'
description: 'ILiAD Biotechnologies, Inc. is a privately held, clinical-stage biotechnology company headquartered in Weston, Florida, developing BPZE1 — a live attenuated intranasal vaccine candidate designed to prevent Bordetella pertussis (whooping cough) colonization and transmission — alongside its B-Tech vector platform, which the company is exploring for infectious, allergic, autoimmune and neurodegenerative disease. The BPZE1 technology originated at Institut Pasteur de Lille and is exclusively licensed to ILiAD, which announced a $115M Series B in February 2026 and received a UK MHRA Innovation Passport designation in December 2024. ILiAD publishes a static corporate and scientific website only: as of 2026-08-22 it operates no public API, developer portal, SDK, machine-readable specification, or any other programmable surface.'
image: https://iliadbio.com/images/logo1.png
layout: provider
modified: '2026-08-22'
name: ILiAD Biotechnologies
nav: Providers
network: true
overview: 'ILiAD Biotechnologies is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Vaccines, Life Sciences, and Pharmaceuticals.


  ILiAD Biotechnologies'' developer surface includes product news and 12 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 6.2
  coverage:
    artifact_dirs: 4
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
screenshot: https://raw.githubusercontent.com/api-evangelist/iliad-biotechnologies/refs/heads/main/screenshots/iliad-biotechnologies-2026-09-02T145833.png
security:
- kind: domain-security
  name: Iliad Biotechnologies Domain Security
  slug: iliad-biotechnologies-domain-security
  summary_line: TLSv1.2 · DMARC
slug: iliad-biotechnologies
tags:
- Company
- Biotechnology
- Vaccines
- Life Sciences
- Pharmaceuticals
- Health
- Immunology
- Infectious Disease
- Clinical Trials
website: https://iliadbio.com/
---
