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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/earlens-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/earlens-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.earlens.com/
- group: company
  title: ''
  type: About
  url: https://www.earlens.com/about
- group: operate
  title: ''
  type: Support
  url: https://www.earlens.com/support
- group: company
  title: ''
  type: Blog
  url: https://www.earlens.com/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/earlens
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.earlens.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.earlens.com/privacy-policy
- group: operate
  title: ''
  type: FAQ
  url: https://www.earlens.com/patient-faq
- group: operate
  title: ''
  type: ContactUs
  url: https://www.earlens.com/contact-us
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/earlens_stock/
created: '2026-08-04'
description: Earlens Corporation is a privately held medical technology company in Menlo Park, California that makes the Earlens Contact Hearing Solution, a non-surgical, custom-fit direct-drive hearing device. Instead of amplifying sound through a speaker, a custom lens rests on the eardrum and is driven by light from an ear-tip, vibrating the eardrum directly to reproduce a broader frequency range than conventional hearing aids. Founded by Dr. Rodney Perkins, the company holds more than 180 patents, received FDA clearance for its second-generation system in 2019, and was named to TIME's Best Inventions of 2020. Earlens is sold through audiology and ENT providers and publishes a consumer and provider marketing site, patient support documents, and a news section. As of this profiling pass it publishes no public developer portal, API documentation, SDK, or machine-readable API contract.
image: https://www.earlens.com/images/Logo-Earlens-r-Mar19_cmyk_cmyk.jpg
layout: provider
modified: '2026-08-04'
name: EarLens
nav: Providers
network: true
overview: 'EarLens is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Hearing, Hearing Aids, Audiology, and Medical Devices.


  EarLens'' developer surface includes support, engineering blog, FAQ, and 9 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 10.8
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 10.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/earlens/refs/heads/main/screenshots/earlens-2026-08-07T164624.png
security:
- kind: domain-security
  name: Earlens Domain Security
  slug: earlens-domain-security
  summary_line: TLSv1.3 · DMARC
slug: earlens
tags:
- Company
- Hearing
- Hearing Aids
- Audiology
- Medical Devices
- Medical Technology
- Health
- Consumer Health
website: https://www.earlens.com/
---
