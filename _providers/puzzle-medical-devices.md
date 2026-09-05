---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
  - security
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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.0
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: An anonymous Model Context Protocol endpoint served from www.puzzlemed.com and advertised by the company's own /llms.txt. It is the Wix platform Site Visitor Assistant, provisioned by the website host
  name: Puzzle Medical Devices Site MCP
  slug: puzzle-medical-devices-site-mcp
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/puzzle-medical-devices-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.puzzlemed.com/
- group: company
  title: ''
  type: Blog
  url: https://www.puzzlemed.com/news
- group: company
  title: ''
  type: BlogRSS
  url: https://www.puzzlemed.com/blog-feed.xml
- group: operate
  title: ''
  type: Support
  url: https://www.puzzlemed.com/contact
- group: other
  title: ''
  type: Team
  url: https://www.puzzlemed.com/team
- group: company
  title: ''
  type: Careers
  url: https://www.puzzlemed.com/joinus
- group: company
  title: ''
  type: LinkedIn
  url: https://ca.linkedin.com/company/puzzlemedicaldevices
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.nasdaqprivatemarket.com/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/puzzle-medical-devices-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/puzzle-medical-devices-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/puzzle-medical-devices-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/puzzle-medical-devices-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/puzzle-medical-devices-rate-limits.yml
created: '2026-08-26'
description: Puzzle Medical Devices Inc. is a Montreal, Quebec based clinical-stage medical device company founded in 2018 by Jade Doucet-Martineau, Gabriel Georges and Francois Trudeau. It develops ModulHeart, a modular percutaneous mechanical circulatory support pump for patients with advanced heart failure, anchored in the descending aorta to reduce cardiac afterload and improve renal perfusion. ModulHeart holds FDA Breakthrough Device Designation and has completed a first-in-human study. The company is a hardware manufacturer, not a software vendor - it publishes no developer program, API reference, SDK or machine-readable contract. Its only agent-reachable surface is a Model Context Protocol endpoint provisioned automatically by Wix, its website host, which serves public site content rather than any product capability.
image: https://static.wixstatic.com/media/fa79dc_887c5a16307349cbb8a24d8c75802651~mv2.jpg/v1/fill/w_2500,h_3333,al_c/fa79dc_887c5a16307349cbb8a24d8c75802651~mv2.jpg
layout: provider
mcp_servers:
- description: A live, anonymous Model Context Protocol endpoint served from Puzzle Medical Devices' own host (www.puzzlemed.com). It is the Wix platform "Site Visitor Assistant" MCP, provisioned automatically by th
  name: Puzzle Medical Devices Site MCP
  slug: puzzle-medical-devices-site-mcp
modified: '2026-08-26'
name: Puzzle Medical Devices
nav: Providers
network: true
overview: 'Puzzle Medical Devices publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Healthcare, Cardiology, and Heart Failure.


  Puzzle Medical Devices'' developer surface includes engineering blog, support, and 12 more developer resources.'
plans:
- name: Puzzle Medical Devices Plans Pricing
  plan_count: 0
  slug: puzzle-medical-devices-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Puzzle Medical Devices Rate Limits
  slug: puzzle-medical-devices-rate-limits
score:
  band: minimal
  composite: 10.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 10.5
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 13.8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/puzzle-medical-devices/refs/heads/main/screenshots/puzzle-medical-devices-2026-09-02T152349.png
security:
- kind: domain-security
  name: Puzzle Medical Devices Domain Security
  slug: puzzle-medical-devices-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: puzzle-medical-devices
tags:
- Company
- Medical Devices
- Healthcare
- Cardiology
- Heart Failure
- Mechanical Circulatory Support
- Medical Technology
- Clinical Stage
- Canada
- Hardware
website: https://www.puzzlemed.com/
---
