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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kromatid-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kromatid.com/
- group: company
  title: ''
  type: Blog
  url: https://kromatid.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://kromatid.com/blog/rss.xml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kromatid.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://kromatid.com/contact-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kromatid
- group: start
  title: ''
  type: CustomerPortal
  url: https://my.kromatid.com/user/login
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kromatid
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@kromatideducation
- group: company
  title: ''
  type: Careers
  url: https://kromatid.com/careers
- group: commercial
  title: ''
  type: Plans
  url: plans/kromatid-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kromatid-llms.txt
coverage:
  checked: '2026-08-23'
  detail: KromaTiD sells wet-lab dGH reagent kits and single-cell cytogenomics lab services to cell and gene therapy developers, not software — its HubSpot marketing site has no developer section and its only login is a Drupal/Cognidox customer document portal at my.kromatid.com, so every contract-discovery path on both hosts 404s.
  evidence:
  - status: 404
    url: https://kromatid.com/openapi.json
  - status: 404
    url: https://kromatid.com/.well-known/agent-card.json
  - status: 404
    url: https://my.kromatid.com/jsonapi
  - status: 200
    url: https://api.github.com/orgs/kromatid/repos
  - status: 200
    url: https://kromatid.com/
  reason: not-a-software-company
  state: none
created: '2026-08-23'
description: KromaTiD (KROMASURE) is a Boulder, Colorado single-cell analysis life-science tools and services company founded in 2016, built around its proprietary directional Genomic Hybridization (dGH) platform. dGH probes only the parental strand of DNA, which lets it resolve orientation-specific structural variation — inversions, translocations, insertions and other complex rearrangements — cell by cell, at resolutions that next-generation sequencing and conventional FISH cannot reach. The company sells the KROMASURE platform and the dGH in-Site, dGH SCREEN, kBand and PinPoint product lines as kits and as lab services, aimed at cell and gene therapy developers who need insertional-mutagenesis risk assessment, genotoxicity profiling, edit optimization, starting-material and donor qualification, cell-line characterization and batch-release testing for CMC and FDA IND submissions. Its work has also been used by NASA for spaceflight radiation research. KromaTiD publishes no developer program,
  no API documentation and no machine-readable API contract; its only authenticated surface is a Cognidox-backed customer document portal at my.kromatid.com.
image: https://kromatid.com/hs-fs/hubfs/logos/kromatid-logo-master.png
layout: provider
modified: '2026-08-23'
name: KromaTiD
nav: Providers
network: true
overview: 'KromaTiD is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Genomics, Biotechnology, Life Sciences, and Cell and Gene Therapy.


  KromaTiD''s developer surface includes engineering blog, support, YouTube channel, and 10 more developer resources.'
plans:
- name: Kromatid Plans Pricing
  plan_count: 0
  slug: kromatid-plans-pricing
random_paper: 19
score:
  band: minimal
  composite: 7.9
  coverage:
    artifact_dirs: 6
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 7.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kromatid/refs/heads/main/screenshots/kromatid-2026-09-02T150148.png
security:
- kind: domain-security
  name: Kromatid Domain Security
  slug: kromatid-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: kromatid
tags:
- Company
- Genomics
- Biotechnology
- Life Sciences
- Cell and Gene Therapy
- Cytogenetics
- Laboratory Services
- Healthcare
- Research
website: https://kromatid.com/
---
