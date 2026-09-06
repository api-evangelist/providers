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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vumedi-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/vumedi-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vumedi-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.vumedi.com/
- group: company
  title: ''
  type: About
  url: https://www.vumedi.com/public/pages/about/
- group: start
  title: ''
  type: SignUp
  url: https://www.vumedi.com/accounts/register/
- group: start
  title: ''
  type: Login
  url: https://www.vumedi.com/accounts/login/
- group: operate
  title: ''
  type: Support
  url: https://www.vumedi.com/public/pages/contact/
- group: operate
  title: ''
  type: FAQ
  url: https://www.vumedi.com/public/pages/faq/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.vumedi.com/public/pages/tos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vumedi.com/public/pages/privacy/
- group: company
  title: ''
  type: Partners
  url: https://www.vumedi.com/public/pages/partnering/
- group: company
  title: ''
  type: Careers
  url: https://www.vumedi.com/public/pages/jobs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/VuMedi
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vumedi-inc
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/vumedi
- group: other
  title: ''
  type: iOSApp
  url: https://apps.apple.com/us/app/vumedi/id1074275721
- group: other
  title: ''
  type: StockProfile
  url: https://forgeglobal.com/vumedi_stock/
created: '2026-08-02'
description: VuMedi (Vumedi, Inc.) operates a video education platform for physicians and other healthcare professionals. Founded in 2008 and headquartered in Oakland, California, with offices in Saint Louis Park, Minnesota and Zagreb, Croatia, the platform aggregates a library of long-form educational videos, webinars, conference coverage and case discussions contributed by key opinion leaders and academic medical centers across more than twenty-five clinical specialties. Physicians use it to watch surgical technique videos, follow live and on-demand webinars, discuss cases with peers and presenters, and stay current on clinical evidence. The company monetizes through industry partnerships with pharmaceutical and medical-device brands rather than a subscription paywall. As of August 2026 VuMedi publishes no public developer program, API documentation, machine-readable API contract, SDKs or MCP server; its public surface is the consumer web application, an iOS app, and a set of static marketing
  and policy pages.
image: https://static.vumedi.com/gfx/favicons/android-icon-192x192.png
layout: provider
modified: '2026-08-02'
name: VuMedi
nav: Providers
network: true
overview: 'VuMedi is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Medical Education, Continuing Medical Education, and Video.


  VuMedi''s developer surface includes signup flow, support, FAQ, and 15 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 16.8
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 16.8
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: tags
    regime: Health
    regime_id: health
    score: 23.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vumedi/refs/heads/main/screenshots/vumedi-2026-09-02T170332.png
security:
- kind: domain-security
  name: Vumedi Domain Security
  slug: vumedi-domain-security
  summary_line: TLSv1.2 · DMARC
slug: vumedi
tags:
- Company
- Healthcare
- Medical Education
- Continuing Medical Education
- Video
- Physicians
- Life Sciences
- Content Platform
website: https://www.vumedi.com/
---
