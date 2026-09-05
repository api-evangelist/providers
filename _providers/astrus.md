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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/astrus-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.astrus.ai/
- group: company
  title: ''
  type: Blog
  url: https://medium.com/@B83MOON
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.astrus.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.astrus.ai/privacy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/astrus-ai
- group: company
  title: ''
  type: Careers
  url: https://www.astrus.ai/careers
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/astrus-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/astrus-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/astrus-rate-limits.yml
coverage:
  checked: '2026-08-10'
  detail: Astrus ships its analog-layout tool only as a private authenticated web app at app.astrus.ai (an S3/CloudFront SPA behind an AWS Cognito login whose robots.txt disallows everything); the public site is a five-page Framer marketing site whose own sitemap lists only /, /careers, /404, /privacy and /terms, and which never uses the word API.
  evidence:
  - status: 200
    url: https://www.astrus.ai/sitemap.xml
  - status: 404
    url: https://www.astrus.ai/openapi.json
  - status: 404
    url: https://www.astrus.ai/.well-known/agent-card.json
  - status: 404
    url: https://www.astrus.ai/docs
  - status: 200
    url: https://app.astrus.ai/robots.txt
  - status: 302
    url: https://acg-eda-tool.auth.us-east-2.amazoncognito.com/oauth2/authorize
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: Astrus is an AI-powered microchip design company automating the physical layout of analog circuits. Founded in 2022 by Brad Moon (CEO) and Zeyi Wang (CTO) and based in Toronto and Waterloo, Canada, Astrus applies deep reinforcement learning — inspired by AlphaGo-style self-play — to generate thousands of manufacturable analog chip layouts in seconds, targeting high-speed SERDES interconnects used in data-center GPUs. The platform lets circuit designers submit a schematic and receive optimized layouts in minutes rather than the weeks of manual transistor-by-transistor placement that analog EDA traditionally requires. Astrus raised $8M in seed funding led by Khosla Ventures with participation from Pradeep Sindhu, 1517 Fund, Drive Capital and Alumni Ventures. This profile was surfaced as a Khosla Ventures portfolio company; Astrus publishes no public developer API, SDK, or documentation surface at this time.
image: https://framerusercontent.com/assets/zV3g2D3ZQFZKjSTe4Mzzhce8G9A.png
layout: provider
modified: '2026-08-10'
name: Astrus
nav: Providers
network: true
overview: 'Astrus is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Semiconductors, Chip Design, and Electronic Design Automation.


  Astrus'' developer surface includes engineering blog and 9 more developer resources.'
plans:
- name: Astrus Plans Pricing
  plan_count: 0
  slug: astrus-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Astrus Rate Limits
  slug: astrus-rate-limits
score:
  band: minimal
  composite: 9.7
  coverage:
    artifact_dirs: 7
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
  previous_composite: 9.7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/astrus/refs/heads/main/screenshots/astrus-2026-07-25T201511.png
security:
- kind: domain-security
  name: Astrus Domain Security
  slug: astrus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: astrus
tags:
- Company
- Artificial Intelligence
- Semiconductors
- Chip Design
- Electronic Design Automation
- Analog Circuits
- Machine-Learning
- Reinforcement Learning
website: https://www.astrus.ai/
---
