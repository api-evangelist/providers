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
  url: security/continuum-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gocontinuum.ai/
- group: company
  title: ''
  type: About
  url: https://gocontinuum.ai/about
- group: company
  title: ''
  type: Blog
  url: https://resources.gocontinuum.ai/
- group: start
  title: ''
  type: SignUp
  url: https://gocontinuum.ai/get-started
- group: operate
  title: ''
  type: Support
  url: https://gocontinuum.ai/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gocontinuum.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gocontinuum.ai/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.gocontinuum.ai/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.gocontinuum.ai/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/continuum-llms.txt
created: '2026-07-17'
description: 'Continuum (gocontinuum.ai) is an AI-powered platform that automates B2B returns, warranties, and repairs for distributors and manufacturers. It handles the post-sales workflow end to end through four solution hubs: a Customer Hub with self-service warranty and return portals, a Warehouse Hub for one-click receiving, inspection and dispute processing, a Vendor & Finance Hub for automated vendor engagement and accounts-receivable management, and a Manufacturer Warranty Hub for warranty claim automation. The company reports outcomes such as a 70% reduction in returns labor cost, a 30% increase in profitability, and an 8% reduction in customer churn. Continuum integrates with major distribution ERP systems (Infor, NetSuite, Epicor, Oracle, Acumatica). Based in Chicago, it is seed-funded and backed by Cowboy Ventures. Continuum is SOC 2 audited and publishes a public trust center. No public developer API or documentation is available at this time.'
image: https://gocontinuum.ai/hubfs/cont-blog-four-hubs.png
layout: provider
modified: '2026-07-18'
name: Continuum
nav: Providers
network: true
overview: 'Continuum is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Returns, Warranty, Reverse Logistics, and Supply Chain.


  Continuum''s developer surface includes engineering blog, signup flow, support, and 8 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 14.0
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 14.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/continuum/refs/heads/main/screenshots/continuum-2026-07-25T210334.png
security:
- kind: domain-security
  name: Continuum Domain Security
  slug: continuum-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Continuum Trust Center
  slug: continuum-trust-center
  summary_line: SOC 2
slug: continuum
tags:
- Company
- Returns
- Warranty
- Reverse Logistics
- Supply Chain
- Post-Sales
- Distribution
- Manufacturing
- ERP Integration
- Artificial Intelligence
website: https://gocontinuum.ai/
---
