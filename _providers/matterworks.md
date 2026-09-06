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
    dynamic_client_registration: true
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
  score: 15.1
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/matterworks-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/matterworks-well-known.yml
- group: company
  title: ''
  type: Website
  url: https://www.matterworks.ai/
- group: other
  title: ''
  type: Platform
  url: https://www.matterworks.ai/platform
- group: company
  title: ''
  type: Blog
  url: https://www.matterworks.ai/insights
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/matterworksbio
- group: start
  title: ''
  type: SignUp
  url: https://app.matterworks.ai/sign-up
- group: operate
  title: ''
  type: Support
  url: https://www.matterworks.ai/#contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.matterworks.ai/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.matterworks.ai/terms-of-use
created: '2026-07-17'
description: Matterworks is a Boston-based life-sciences AI company building foundation models for biochemical omics. Its Large Spectral Model is trained on billions of small-molecule, lipid, peptide, and protein mass-spectrometry spectra across millions of biological contexts, and its Pyxis platform turns raw omics data into quantitative, untargeted biochemical annotations and predictions used for asset and target discovery, mode-of-action elucidation, and life-science R&D pipeline decisions. Matterworks positions biochemical omics as explaining orders of magnitude more biological variation than sequence data alone. The product is accessed through the Pyxis web application (app.matterworks.ai, Auth0 sign-in); no public developer API, OpenAPI, SDK, or documentation surface is published at this time.
image: https://avatars.githubusercontent.com/u/66066030?v=4
layout: provider
modified: '2026-07-20'
name: Matterworks
nav: Providers
network: true
overview: 'Matterworks is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Metabolomics, Omics, and Life Sciences.


  Matterworks'' developer surface includes engineering blog, signup flow, support, and 7 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 11.5
  coverage:
    artifact_dirs: 4
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
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 11.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 25.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/matterworks/refs/heads/main/screenshots/matterworks-2026-07-25T230432.png
security:
- kind: domain-security
  name: Matterworks Domain Security
  slug: matterworks-domain-security
  summary_line: TLSv1.3 · HSTS
slug: matterworks
tags:
- Company
- Artificial Intelligence
- Metabolomics
- Omics
- Life Sciences
- Biotechnology
- Mass Spectrometry
- Foundation Models
website: https://www.matterworks.ai/
---
