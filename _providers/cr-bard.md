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
  scored_at: '2026-09-07'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cr-bard-domain-security.yml
- group: auth
  title: ''
  type: Security
  url: security/cr-bard-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cr-bard-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/cr-bard-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/cr-bard-trust-center.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cr-bard-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.bd.com/en-us
- group: other
  title: ''
  type: ParentCompany
  url: https://www.bd.com/en-us/about-bd/our-company
- group: company
  title: ''
  type: Careers
  url: https://jobs.bd.com/en/bd-interventional
- group: operate
  title: ''
  type: PressReleases
  url: https://investors.bd.com/news-events/press-releases/detail/352/bd-completes-bard-acquisition-creating-new-global-health-care-leader
- group: operate
  title: ''
  type: Support
  url: https://www.bd.com/en-us/support/contact-us
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bd1/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bd.com/en-us/about-bd/policies/privacy-policy-statement
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bd.com/en-us/about-bd/policies/terms-of-use
coverage:
  checked: '2026-09-07'
  detail: C. R. Bard ceased to exist as an operating company when BD completed its acquisition on 2017-12-29; the legacy crbard.com domain still resolves but returns a hard 404 from an Azure Application Gateway at the root and at every path probed, and no successor developer surface exists under the BD Bard brand.
  evidence:
  - status: 404
    url: https://www.crbard.com/
  - status: 404
    url: https://www.bd.com/en-us/products-and-solutions/products/product-brands/bard
  - status: 502
    url: https://api.bd.com/openapi.json
  - status: 404
    url: https://www.bd.com/.well-known/security.txt
  reason: defunct
  state: none
created: '2024-01-01'
description: C. R. Bard, Inc. was an American multinational developer, manufacturer, and marketer of medical technologies in the fields of vascular, urology, oncology, and surgical specialties. Bard was founded in 1907 by Charles Russell Bard and was acquired by Becton, Dickinson and Company (BD) in December 2017 for approximately $24 billion. Bard's product lines now operate as part of BD's Interventional segment under the BD Bard brand. No public API or developer portal is published; integrations with hospital and provider systems are arranged through BD enterprise channels.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cr-bard.png
layout: provider
modified: '2026-09-07'
name: C. R. Bard
nav: Providers
network: true
overview: 'C. R. Bard is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include BD, Becton Dickinson, Interventional, Medical Devices, and Medical Technology.


  C. R. Bard''s developer surface includes support and 13 more developer resources.'
press:
- date: '2026-05-25'
  title: 5 takeaways from Becton Dickinson's $24B acquisition of ...
  url: https://medcitynews.com/2017/04/5-takeaways-becton-dickinsons-24b-acquisition-c-r-bard/
- date: '2026-05-25'
  title: C. R. Bard, Inc. to Acquire Medivance for $250 Million
  url: https://www.biospace.com/c-r-bard-inc-to-acquire-medivance-for-250-million
- date: '2026-05-25'
  title: Boston Scientific Buys C.R. Bard's Electrophysiology ...
  url: https://www.mddionline.com/business/boston-scientific-buys-c-r-bard-s-electrophysiology-business
- date: '2026-05-25'
  title: BD Completes Bard Acquisition, Creating New Global ...
  url: https://www.prnewswire.com/news-releases/bd-completes-bard-acquisition-creating-new-global-health-care-leader-300576098.html
- date: '2026-05-25'
  title: BD accelerates offerings with Bard
  url: https://www.hmenews.com/article/bd-accelerates-offerings-bard
random_paper: 16
score:
  band: emerging
  composite: 17.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 14.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 3.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.20.0
  scored_at: '2026-09-07'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/cr-bard/refs/heads/main/screenshots/cr-bard-2026-06-20T175204.png
security:
- kind: domain-security
  name: Cr Bard Domain Security
  slug: cr-bard-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Cr Bard Vulnerability Disclosure
  slug: cr-bard-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Cr Bard Trust Center
  slug: cr-bard-trust-center
  summary_line: ISO/IEC 27001:2022, SOC 2+, UL CAP (UL Cybersecurity Assurance Program)
slug: cr-bard
tags:
- BD
- Becton Dickinson
- Interventional
- Medical Devices
- Medical Technology
- Oncology
- Surgery
- Urology
- Vascular
- Fortune 1000
website: https://www.bd.com/en-us
---
