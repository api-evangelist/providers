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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kyrok-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kyrok.com/en
- group: auth
  title: ''
  type: TrustCenter
  url: security/kyrok-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.kyrok.com/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kyrok-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kyrok-llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kyrok
- group: company
  title: ''
  type: Blog
  url: https://kyrok.com/en/press
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kyrok.com/en/legal/privacy
- group: other
  title: ''
  type: Imprint
  url: https://kyrok.com/en/legal/imprint
- group: operate
  title: ''
  type: Support
  url: mailto:support@kyrok.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kyrok
created: '2026-07-17'
description: Kyrok GmbH is a Berlin-based software company building an AI operating system for mid-sized pharmaceutical and chemical manufacturers in Europe. The platform layers over a company's existing ERP (SAP S/4HANA, SAP R/3, Microsoft Dynamics 365, Infor, Applus) and connects the systems supply chain teams currently hold together by hand into intelligent operations across customer service, production planning, material planning and procurement. Kyrok positions itself on an "AI assists, people decide" model, running on European infrastructure in Frankfurt am Main, GDPR-compliant, with ISO 27001 and ISO 42001 certifications in progress. The company announced a EUR 3.1M round in June 2026 and names AnalytiChem and Konapharma as customers. Kyrok connects to ERP systems via API but publishes no public developer API, API reference, or SDKs as of this enrichment pass.
image: https://kyrok.com/og/home-en.jpg
layout: provider
modified: '2026-07-19'
name: Kyrok
nav: Providers
network: true
overview: 'Kyrok is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Supply Chain, Artificial Intelligence, ERP, and Pharmaceuticals.


  Kyrok''s developer surface includes engineering blog, support, and 10 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 12.8
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 12.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kyrok/refs/heads/main/screenshots/kyrok-2026-07-25T224350.png
security:
- kind: domain-security
  name: Kyrok Domain Security
  slug: kyrok-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Kyrok Trust Center
  slug: kyrok-trust-center
  summary_line: trust center published
slug: kyrok
tags:
- Company
- Supply Chain
- Artificial Intelligence
- ERP
- Pharmaceuticals
- Chemicals
- Manufacturing
- Enterprise Software
- Germany
website: https://kyrok.com/en
---
