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
  url: security/discgenics-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/discgenics-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.discgenics.com/
- group: company
  title: ''
  type: About
  url: https://www.discgenics.com/about-us
- group: company
  title: ''
  type: Blog
  url: https://www.discgenics.com/ceos-blog
- group: company
  title: ''
  type: News
  url: https://www.discgenics.com/news
- group: operate
  title: ''
  type: Contact
  url: https://www.discgenics.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.discgenics.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.discgenics.com/privacy-policy
- group: company
  title: ''
  type: Investors
  url: https://www.discgenics.com/investors-and-media
- group: company
  title: ''
  type: Careers
  url: https://www.discgenics.com/about-us#careers
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/discgenics/
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/DiscGenics
- group: start
  title: ''
  type: ClinicalTrials
  url: https://clinicaltrials.gov/search?spons=DiscGenics
- group: start
  title: ''
  type: PatientTrialSite
  url: https://www.dddtrial.com/
coverage:
  checked: '2026-08-12'
  detail: DiscGenics is a late-stage clinical biopharmaceutical company whose product is an injectable allogeneic cell therapy (IDCT/rebonuputemcel), not software — its entire web presence is a bilingual Squarespace marketing site whose 139-URL sitemap contains only company, science, pipeline, patient and news pages, with no developer, API or documentation section, and no public GitHub organization.
  evidence:
  - status: 404
    url: https://www.discgenics.com/openapi.json
  - status: 404
    url: https://www.discgenics.com/docs
  - status: 404
    url: https://www.discgenics.com/.well-known/agent-card.json
  - status: 404
    url: https://www.dddtrial.com/.well-known/agent-card.json
  - status: 200
    url: https://www.discgenics.com/sitemap.xml
  - status: 200
    url: https://api.github.com/search/users?q=discgenics
  reason: not-a-software-company
  state: none
created: '2026-08-12'
description: 'DiscGenics is a privately held, late-stage clinical biopharmaceutical company headquartered in Salt Lake City, Utah, developing allogeneic, cell-based regenerative biologic therapies for degenerative diseases of the spine. Its lead candidate, IDCT (rebonuputemcel), is a single-injection allogeneic discogenic progenitor cell therapy for symptomatic mild-to-moderate lumbar degenerative disc disease, manufactured under cGMP from donated adult human intervertebral disc tissue and granted FDA Regenerative Medicine Advanced Therapy (RMAT) and Fast Track designations. The company is running a US Phase III program (the PIVOT and CONFIRM studies) alongside a clinical study in Japan. DiscGenics is a therapeutics developer, not a software vendor: it publishes no developer portal, API, SDK or machine-readable specification of any kind.'
image: http://static1.squarespace.com/static/59d2b1d812abd948b8707a48/t/59e93fb88a02c760fefcc86b/1774284572317/Discgenics-Logo-White.png?format=1500w
layout: provider
modified: '2026-08-12'
name: DiscGenics
nav: Providers
network: true
overview: 'DiscGenics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Biopharmaceutical, Regenerative Medicine, and Cell Therapy.


  DiscGenics'' developer surface includes engineering blog, product news, and 13 more developer resources.'
random_paper: 2
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
screenshot: https://raw.githubusercontent.com/api-evangelist/discgenics/refs/heads/main/screenshots/discgenics-2026-09-02T145244.png
security:
- kind: domain-security
  name: Discgenics Domain Security
  slug: discgenics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: discgenics
tags:
- Company
- Biotechnology
- Biopharmaceutical
- Regenerative Medicine
- Cell Therapy
- Healthcare
- Life Sciences
- Clinical Trials
- Spine
- Utah
website: https://www.discgenics.com/
---
