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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/circular-genomics-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/circular-genomics-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.circulargenomics.com/
- group: company
  title: ''
  type: About
  url: https://www.circulargenomics.com/about
- group: other
  title: ''
  type: Products
  url: https://www.circulargenomics.com/products
- group: company
  title: ''
  type: Blog
  url: https://www.circulargenomics.com/news
- group: operate
  title: ''
  type: Contact
  url: https://www.circulargenomics.com/contact
- group: company
  title: ''
  type: Partners
  url: https://www.circulargenomics.com/partnerships
- group: other
  title: ''
  type: Publications
  url: https://www.circulargenomics.com/publications-resources
- group: company
  title: ''
  type: Careers
  url: https://www.circulargenomics.com/careers
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.circulargenomics.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.circulargenomics.com/privacy
- group: other
  title: ''
  type: CookiePolicy
  url: https://www.circulargenomics.com/cookie-policy
- group: start
  title: ''
  type: ProviderPortal
  url: https://mindlight.circulargenomics.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/circulargenomics
- group: company
  title: ''
  type: Twitter
  url: https://x.com/CircGenomics
- group: company
  title: ''
  type: Crunchbase
  url: https://www.crunchbase.com/organization/circular-genomics
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/circular-genomics_stock/
coverage:
  checked: '2026-08-09'
  detail: 'Circular Genomics ships clinical circRNA assays, not software — its only logged-in surface, the MindLight provider portal at mindlight.circulargenomics.com, is a white-labeled CrelioHealth LIS (the response carries `server: Crelio`) for test ordering by licensed clinicians, and every spec, /.well-known/ and developer path probed on both company hosts returned 404.'
  evidence:
  - status: 404
    url: https://www.circulargenomics.com/openapi.json
  - status: 404
    url: https://www.circulargenomics.com/developers
  - status: 404
    url: https://mindlight.circulargenomics.com/openapi.json
  - status: 404
    url: https://mindlight.circulargenomics.com/.well-known/agent-card.json
  - status: 200
    url: https://www.circulargenomics.com/sitemap.xml
  - status: 200
    url: https://api.github.com/users/circular-genomics/repos
  reason: no-developer-program
  state: none
created: '2026-08-09'
description: 'Circular Genomics is a San Diego, California precision-neurology diagnostics company that uses brain-derived circular RNA (circRNA) as a class of stable, blood-based biomarkers for psychiatric and neurological disease. Spun out of the University of New Mexico in 2021 and now resident at Lilly Gateway Labs in San Diego, the company builds CircPath, a proprietary molecular-intelligence platform that discovers, validates and translates circRNA signals into biological insight, and productizes it as research and clinical assays: Discover 1600+ (whole-transcriptome circRNA sequencing across 1,600+ brain-derived circRNAs with pathway-level analysis), AD Predict and AD Detect for Alzheimer''s disease, and MindLight, an SSRI antidepressant response test for major depressive disorder. Test ordering and results delivery for licensed healthcare providers run through a login-gated provider portal at mindlight.circulargenomics.com, which is a white-labeled CrelioHealth laboratory information
  system rather than a first-party developer surface. Circular Genomics publishes no public API, SDK, webhook or developer documentation of any kind.'
image: https://cdn.prod.website-files.com/69f294bcc4f8261224416905/6a5e4d5072472bd95c583d2f_Circular%20Genomics%20Monogram%401x.png
layout: provider
modified: '2026-08-09'
name: Circular Genomics
nav: Providers
network: true
overview: 'Circular Genomics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Diagnostics, Genomics, and Precision Medicine.


  Circular Genomics'' developer surface includes engineering blog and 17 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/circular-genomics/refs/heads/main/screenshots/circular-genomics-2026-09-02T145040.png
security:
- kind: domain-security
  name: Circular Genomics Domain Security
  slug: circular-genomics-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: circular-genomics
tags:
- Company
- Biotechnology
- Diagnostics
- Genomics
- Precision Medicine
- Neurology
- Life Sciences
- Health
- Clinical Laboratory
- Biomarkers
website: https://www.circulargenomics.com/
---
