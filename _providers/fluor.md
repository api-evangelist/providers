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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
  score: 10.8
  scored_at: '2026-09-10'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.fluor.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fluor
- group: company
  title: ''
  type: Blog
  url: https://newsroom.fluor.com/rss/pressrelease.aspx
- group: operate
  title: ''
  type: Support
  url: https://www.fluor.com/contact-us/general
- group: start
  title: ''
  type: Login
  url: https://www.fluor.com/client-login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fluor.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fluor.com/privacy-policy
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fluor-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/fluor-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fluor-llms.txt
coverage:
  checked: '2026-09-10'
  detail: Fluor sells engineering, procurement and construction services, not software — the fluor.com sitemap's 1,201 URLs contain no developer, API or documentation page, api/developer/developers/docs/apis.fluor.com all resolve NXDOMAIN, and the only machine-readable document served anywhere on the estate is an RFC 8414 OAuth metadata file belonging to the Eightfold recruiting platform running under careers.fluor.com.
  evidence:
  - status: 200
    url: https://www.fluor.com/sitemap.xml
  - status: 404
    url: https://www.fluor.com/llms.txt
  - status: 404
    url: https://www.fluor.com/openapi.json
  - status: 404
    url: https://www.fluor.com/.well-known/api-catalog
  - status: 200
    url: https://careers.fluor.com/.well-known/oauth-authorization-server
  reason: not-a-software-company
  state: none
created: '2026-03-21'
description: 'Fluor Corporation (NYSE: FLR) is a Fortune 500 engineering, procurement, construction and maintenance company headquartered in Irving, Texas. Fluor designs and builds capital projects and provides project-management services for energy, chemicals, life sciences, mining and metals, advanced technologies, infrastructure and government clients worldwide, and licenses its own process technologies such as Econamine FG Plus and Fluor Solvent. Fluor sells engineering and construction services rather than software: it operates no developer program, publishes no API reference, and serves no machine-readable API contract. Its business-to-business integration with suppliers runs inside SAP Ariba and Workday, whose contracts belong to those vendors. This is an independent API Evangelist profile of Fluor''s public surface.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fluor.png
layout: provider
modified: '2026-09-10'
name: Fluor
nav: Providers
network: true
overview: 'Fluor is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fortune 500, Engineering, Construction, Procurement, and Project Management.


  Fluor''s developer surface includes engineering blog, support, and 8 more developer resources.'
press:
- date: '2026-05-25'
  title: Business Incubation – Accelerating Emerging Technologies
  url: https://www.fluor.com/services-and-expertise/innovation-and-expertise/business-incubation/
- date: '2026-05-25'
  title: Fluor Uses IBM Watson to Deliver Predictive Analytics ...
  url: https://www.prnewswire.com/news-releases/fluor-uses-ibm-watson-to-deliver-predictive-analytics-capability-for-megaprojects-300711688.html
- date: '2026-05-25'
  title: 'Fluor Corporation (FLR): This Industrial Stock Is Already ...'
  url: https://finance.yahoo.com/news/fluor-corporation-flr-industrial-stock-114846750.html
- date: '2026-05-25'
  title: Quarterly Results - Fluor Corporation - Financials
  url: https://fluorenterprisesinc2023rbcr.q4web.com/financials/quarterly-results/default.aspx
- date: '2026-05-25'
  title: Fluor Selected for Expansion of Large-Scale Biologics ...
  url: https://www.sttinfo.fi/tiedote/69952904/fluor-selected-for-expansion-of-large-scale-biologics-manufacturing-facility-in-scandinavia?publisherId=58763726
random_paper: 6
score:
  band: emerging
  composite: 13.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 10.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 3.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 27.0
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/fluor/refs/heads/main/screenshots/fluor-2026-06-20T181338.png
security:
- kind: domain-security
  name: Fluor Domain Security
  slug: fluor-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Fluor Vulnerability Disclosure
  slug: fluor-vulnerability-disclosure
  summary_line: Hackerone
slug: fluor
tags:
- Fortune 500
- Engineering
- Construction
- Procurement
- Project Management
- Energy
- Infrastructure
- Mining
website: https://www.fluor.com
---
