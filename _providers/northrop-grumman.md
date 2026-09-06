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
  url: security/northrop-grumman-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/northrop-grumman-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.northropgrumman.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NorthropGrumman
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/northrop-grumman-corporation
- group: company
  title: ''
  type: Blog
  url: https://news.northropgrumman.com/
- group: operate
  title: ''
  type: Support
  url: https://www.northropgrumman.com/who-we-are/contact-us-northrop-grumman
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.northropgrumman.com/who-we-are/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.northropgrumman.com/who-we-are/privacy-policy
- group: company
  title: ''
  type: Careers
  url: https://www.northropgrumman.com/careers
- group: other
  title: ''
  type: Suppliers
  url: https://www.northropgrumman.com/suppliers
- group: company
  title: ''
  type: Investors
  url: https://investor.northropgrumman.com/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCiTTe3mBodoZVGVhQDpEFjg
- group: company
  title: ''
  type: X (Twitter)
  url: https://twitter.com/northropgrumman
coverage:
  checked: '2026-08-28'
  detail: 'Northrop Grumman ships mission software but runs no developer program of any kind: developer.northropgrumman.com and api.northropgrumman.com do not resolve, every /.well-known/, /openapi.json and /llms.txt path on www.northropgrumman.com returns a clean 404, and the only external integration surfaces — the OASIS supplier tools on myngc.com — are ADFS-authenticated web portals with no documented API behind them.'
  evidence:
  - status: 404
    url: https://www.northropgrumman.com/openapi.json
  - status: 404
    url: https://www.northropgrumman.com/.well-known/api-catalog
  - status: 404
    url: https://www.northropgrumman.com/.well-known/agent-card.json
  - status: 404
    url: https://www.northropgrumman.com/llms.txt
  - status: 0
    url: https://developer.northropgrumman.com/
  - status: 307
    url: https://oasis-dashboard.amer.myngc.com/
  reason: no-developer-program
  state: none
created: '2026-03-21'
description: 'Northrop Grumman Corporation is a US global aerospace, defense and security company headquartered in Falls Church, Virginia, organized into four segments: Aeronautics Systems, Defense Systems, Mission Systems and Space Systems. It builds autonomous aircraft, strategic bombers and long-range strike weapons, missile defense and integrated battle command systems, radar and electronic warfare sensors, cyber and command-and-control mission software, solid rocket motors, and space vehicles and launch systems for US Department of Defense, intelligence-community, NASA and allied customers. It publishes no public developer program, API portal or machine-readable API contract; its external integration surfaces are the ADFS-authenticated OASIS supplier tools on myngc.com, available only to registered suppliers under contract.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/northrop-grumman.png
layout: provider
modified: '2026-08-28'
name: Northrop Grumman
nav: Providers
network: true
overview: 'Northrop Grumman is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Aerospace, Autonomous Systems, Command and Control, Cybersecurity, and Defense.


  Northrop Grumman''s developer surface includes engineering blog, support, YouTube channel, and 11 more developer resources.'
press:
- date: '2026-05-25'
  title: Northrop Grumman Expanding Its Use of NVIDIA AI ...
  url: https://news.northropgrumman.com/digital-transformation/northrop-grumman-expanding-its-use-of-nvidia-ai-technology-to-advance-solutions-for-space
- date: '2026-05-25'
  title: Northrop Grumman Accelerates Innovation with AI ...
  url: https://www.linkedin.com/posts/travisgarriss_deploying-an-ai-factory-for-regulated-industries-activity-7424914206048731136-0XYR
- date: '2026-05-25'
  title: Artificial Intelligence and Machine Learning
  url: https://www.northropgrumman.com/what-we-do/mission-solutions/artificial-intelligence-and-machine-learning
- date: '2026-05-25'
  title: Artificial Intelligence Applications at Northrop Grumman
  url: https://emerj.com/artificial-intelligence-applications-at-northrop-grumman-an-overview/
- date: '2026-05-25'
  title: Artificial Intelligence
  url: https://news.northropgrumman.com/artificial-intelligence
random_paper: 16
score:
  band: emerging
  composite: 12.3
  coverage:
    artifact_dirs: 9
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
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 12.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 25.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: domain-security
  name: Northrop Grumman Domain Security
  slug: northrop-grumman-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: northrop-grumman
tags:
- Aerospace
- Autonomous Systems
- Command and Control
- Cybersecurity
- Defense
- Fortune 100
- Fortune 500
- Government
- Manufacturing
- Mission Systems
- Space
website: https://www.northropgrumman.com/
---
