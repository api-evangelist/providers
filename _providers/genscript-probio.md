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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/genscript-probio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.probiocdmo.com/
- group: company
  title: ''
  type: About
  url: https://www.probiocdmo.com/about-us.html
- group: operate
  title: ''
  type: Support
  url: https://www.probiocdmo.com/online_request/general
- group: start
  title: ''
  type: SignUp
  url: https://www.probiocdmo.com/customer/signup
- group: start
  title: ''
  type: Login
  url: https://www.probiocdmo.com/customer/login
- group: company
  title: ''
  type: Blog
  url: https://www.probiocdmo.com/special/news
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.probiocdmo.com/standard_t_c.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.probiocdmo.com/privacy_policy.html
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/genscript-probio-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/genscript-probio-plans-pricing.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.probiocdmo.com/information-security.html
- group: auth
  title: ''
  type: Compliance
  url: security/genscript-probio-trust-center.yml
coverage:
  checked: '2026-08-21'
  detail: GenScript ProBio is a biologics and cell & gene therapy contract manufacturer whose product is laboratory and cGMP manufacturing services, not software — its 213-URL sitemap contains no developer, API, or integration page, api./developer./docs. subdomains do not resolve, no GitHub organization exists, and the only account surface is a quote-request form and a customer login.
  evidence:
  - status: 404
    url: https://www.probiocdmo.com/openapi.json
  - status: 404
    url: https://www.probiocdmo.com/llms.txt
  - status: 403
    url: https://www.probiocdmo.com/.well-known/agent-card.json
  - status: 200
    url: https://www.probiocdmo.com/sitemap.xml
  - status: 404
    url: https://api.github.com/orgs/genscript-probio
  reason: not-a-software-company
  state: none
created: '2026-08-21'
description: 'GenScript ProBio (ProBio) is the biologics and cell & gene therapy contract development and manufacturing organization (CDMO) segment of GenScript Biotech Corporation (HKEX 1548), operating from sites in the United States, the Netherlands, South Korea, Hong Kong, Shanghai, Nanjing and Zhenjiang. It provides end-to-end drug-discovery-to-commercialization services covering antibody and ADC discovery, antibody engineering and humanization, developability assessment, cell line development, bioanalytical and bioassay services, process development, and cGMP clinical and commercial manufacturing of recombinant proteins, plasmid DNA, lentiviral and AAV viral vectors, mRNA and cell therapies, having supported more than 150 IND approvals since 2017. ProBio is a laboratory and manufacturing services business rather than a software vendor: it publishes no developer portal, no API reference and no machine-readable contract, and customer engagement runs through a quote request form and an
  authenticated customer account area.'
image: https://www.probiocdmo.com/gsfiles/j/img/logo.png
layout: provider
modified: '2026-08-21'
name: Genscript Probio
nav: Providers
network: true
overview: 'Genscript Probio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Life Sciences, Pharmaceuticals, and Contract Manufacturing.


  Genscript Probio''s developer surface includes support, signup flow, engineering blog, and 10 more developer resources.'
plans:
- name: Genscript Probio Plans Pricing
  plan_count: 0
  slug: genscript-probio-plans-pricing
random_paper: 12
score:
  band: emerging
  composite: 17.9
  coverage:
    artifact_dirs: 6
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 17.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 23.8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/genscript-probio/refs/heads/main/screenshots/genscript-probio-2026-09-02T145557.png
security:
- kind: domain-security
  name: Genscript Probio Domain Security
  slug: genscript-probio-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Genscript Probio Trust Center
  slug: genscript-probio-trust-center
  summary_line: trust center published
slug: genscript-probio
tags:
- Company
- Biotechnology
- Life Sciences
- Pharmaceuticals
- Contract Manufacturing
- CDMO
- Cell and Gene Therapy
- Biologics
- Manufacturing
website: https://www.probiocdmo.com/
---
