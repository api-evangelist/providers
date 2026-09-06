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
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stoik-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.stoik.com/en-us
- group: docs
  title: ''
  type: Documentation
  url: https://docs.stoik.io/readme.md
- group: operate
  title: ''
  type: HelpCenter
  url: https://docs.stoik.io/
- group: company
  title: ''
  type: Blog
  url: https://www.stoik.com/en-us/resources
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/stoikio
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.stoik.io/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/stoik-changelog.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.stoik.com/en-us/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.stoik.com/privacy
- group: start
  title: ''
  type: Login
  url: https://app.stoik.io/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/stoik-llms.txt
created: '2026-07-17'
description: Stoïk is a European cyber-insurtech, founded in 2021 and headquartered in Paris, that pairs cyber insurance with active security prevention for small and mid-market businesses (up to roughly €1B revenue). Insurance coverage of up to €10M is backed by Tokio Marine HCC, Swiss Re and Axeria IARD and sold 100% online through a broker platform used by 1,500+ partner brokers across France, Germany, Spain, Austria, Belgium and the Netherlands. Beyond insurance, Stoïk ships a free risk-monitoring suite — Stoïk Protect (external scan, phishing simulation, Active Directory and cloud scanning, leaked-credential monitoring), Managed Detection & Response (MDR), and managed email security — plus 24/7 incident response. Stoïk is a portfolio company of Andreessen Horowitz (a16z) and Anthemis. No public developer API is published today; the developer-adjacent surface is a GitBook help center (docs.stoik.io, with an llms.txt index and a dated changelog), the insured/broker platform at app.stoik.io,
  and the GitHub org github.com/stoikio.
image: https://uploads-ssl.webflow.com/60be2330f31e471e6ee67e0c/627e251a82a788379f0f1e77_Name%20-%20Dark.jpg
layout: provider
modified: '2026-07-21'
name: Stoik
nav: Providers
network: true
overview: 'Stoik is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cyber Insurance, Cybersecurity, Insurtech, and Managed Detection and Response.


  Stoik''s developer surface includes documentation, engineering blog, changelog, and 9 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 16.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 18.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 16.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 21.2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stoik/refs/heads/main/screenshots/stoik-2026-09-02T160916.png
security:
- kind: domain-security
  name: Stoik Domain Security
  slug: stoik-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: stoik
tags:
- Company
- Cyber Insurance
- Cybersecurity
- Insurtech
- Managed Detection and Response
- Email Security
- Phishing Simulation
- Vulnerability Scanning
- Incident Response
- Europe
website: https://www.stoik.com/en-us
---
