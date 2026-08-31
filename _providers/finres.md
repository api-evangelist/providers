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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/finres-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.finres.org/
- group: company
  title: ''
  type: About
  url: https://www.finres.org/about
- group: company
  title: ''
  type: Blog
  url: https://www.finres.org/posts
- group: operate
  title: ''
  type: Support
  url: https://www.finres.org/contact
- group: start
  title: ''
  type: SignUp
  url: https://www.finres.org/inscription
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/finres-llms.txt
created: '2026-07-17'
description: Finres (finres SAS) is a French climate-risk analytics company building a decision platform for agriculture. It translates climate hazards into economic consequences for farms, agricultural value chains and territories, combining agronomic, pedological, climate and market data with AI models that are peer-reviewed and validated against published research. Two productized offerings sit on top of the platform - a farm-level economic and climate viability diagnostic (DPEC, currently in beta, seeded from a grower's TelePAC parcel file and reference datasets such as Agreste, IPPAP and RICA) and bespoke territorial or sector studies. Finres was founded by Florent Baarsch, previously with the World Bank, the United Nations and climate research institutes, and its customers include the French government, the World Bank, the Green Climate Fund, IFAD and the FAO. The company markets high-resolution data delivery into customer decision systems, but as of this enrichment pass publishes
  no public developer portal, API reference, machine-readable specification or SDK - access is arranged through a sales demo.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/finres.png
layout: provider
modified: '2026-07-20'
name: Finres
nav: Providers
network: true
overview: 'Finres is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Climate, Agriculture, AgTech, and Climate Risk.


  Finres'' developer surface includes engineering blog, support, signup flow, and 4 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 9.8
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.8
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/finres/refs/heads/main/screenshots/finres-2026-07-25T214543.png
security:
- kind: domain-security
  name: Finres Domain Security
  slug: finres-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: finres
tags:
- Company
- Climate
- Agriculture
- AgTech
- Climate Risk
- Analytics
- Data
- Sustainability
- France
- Artificial Intelligence
website: https://www.finres.org/
---
