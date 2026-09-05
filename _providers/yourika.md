---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://yourika.ai/'', ''status'': 301, ''note'': ''declared website redirects to https://www.yourikalabs.com/ — a different registrable domain (yourika.ai -> yourikalabs.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.6
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://yourika.ai/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/yourika-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/yourika-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/yourika-domain-security.yml
- group: operate
  title: ''
  type: Support
  url: mailto:info@yourika.ai
created: '2026-07-17'
description: YOURIKA (YOURIKA Labs) is a Kitchener-Waterloo, Canada AI platform and venture studio that creates and scales purpose-built, verticalized AI ventures in partnership with industry experts, prioritizing accuracy, trust, and measurable outcomes over technology-first approaches. Its ventures include smart'n, a nurse-first intelligence and learning platform that helps nurses learn, grow, and make more informed decisions throughout their careers, and Retain / Workforce Intelligence for senior and long-term care, which helps operators identify, hire, and retain caregivers while reducing turnover. yourikaLABS also offers AI advisory services connecting businesses with experts to build data-driven strategies and roadmaps. YOURIKA is backed by Amazon, Techstars (Amazon Alexa Accelerator), and the University of Waterloo. The company exposes no bespoke public developer API; its marketing site is built on Wix and advertises a Wix Site MCP endpoint plus an llms.txt for agentic access.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/yourika.png
layout: provider
mcp_servers:
- description: ''
  name: YOURIKA Labs Wix Site MCP
  slug: yourika-labs-wix-site-mcp
modified: '2026-07-21'
name: YOURIKA
nav: Providers
network: true
overview: 'YOURIKA is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Machine-Learning, Healthcare, and Nursing.


  YOURIKA''s developer surface includes support and 4 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/yourika/refs/heads/main/screenshots/yourika-2026-09-02T171335.png
security:
- kind: domain-security
  name: Yourika Domain Security
  slug: yourika-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: yourika
tags:
- Company
- Artificial Intelligence
- Machine-Learning
- Healthcare
- Nursing
- Workforce
- Long-Term Care
- Venture Studio
- Education
website: https://yourika.ai/
---
