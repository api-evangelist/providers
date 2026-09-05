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
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/prysm-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.prysm.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.prysm.com/resources/index.html
- group: operate
  title: ''
  type: Support
  url: https://www.prysm.com/support/index.html
- group: operate
  title: ''
  type: StatusPage
  url: https://www.prysm.com/support/status.html
- group: company
  title: ''
  type: Blog
  url: https://blog.prysm.com/en-us.html
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.prysm.com/en-us/rss.xml
- group: company
  title: ''
  type: Newsroom
  url: https://www.prysm.com/newsroom/index.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.prysm.com/legal/terms-and-conditions/index.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.prysm.com/legal/privacy-policy.html
- group: start
  title: ''
  type: SignUp
  url: https://www.prysm.com/trial-request/index.html
- group: company
  title: ''
  type: Partners
  url: https://www.prysm.com/partners/partner-program/index.html
- group: operate
  title: ''
  type: Contact
  url: https://www.prysm.com/contact/index.html
- group: company
  title: ''
  type: About
  url: https://www.prysm.com/company/index.html
- group: company
  title: ''
  type: Careers
  url: https://www.prysm.com/company/careers/index.html
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://forgeglobal.com/prysm_stock/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/prysm-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/prysm-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/prysm-plans-pricing.yml
coverage:
  checked: '2026-08-26'
  detail: Prysm ships an end-user product only — LPD 6K displays plus the Prysm Application Suite desktop, web and iPhone clients — and www.prysm.com is a static HTTrack mirror (captured 2025-10-28) of the former prysmsystems.com HubSpot site with no developer, docs or API entry anywhere in its navigation; the 2017 "Prysm API" early-preview announcement never produced a public reference, and developer/docs/api.prysm.com do not resolve in DNS.
  evidence:
  - status: 200
    url: https://www.prysm.com/
  - status: 200
    url: https://www.prysm.com/support/index.html
  - status: 404
    url: https://www.prysm.com/openapi.json
  - status: 404
    url: https://www.prysm.com/.well-known/api-catalog
  - status: 404
    url: https://www.prysm.com/.well-known/agent-card.json
  - status: 200
    url: https://blog.prysm.com/newsroom/news/prysm-api-creates-customized-collaboration-experiences/
  - status: 0
    url: https://support.prysm.com/
  reason: no-developer-program
  state: none
created: '2026-08-26'
description: Prysm — legally Motherson Prysm, Inc. — builds large-format interactive display hardware and the Prysm Application Suite, a cloud-hosted visual collaboration and digital-workplace platform. Founded in 2005 in Silicon Valley as Spudnik by Amit Jain and Roger Hajjar, the company invented and patented Laser Phosphor Display (LPD) technology, shipped today as the bezel-free LPD 6K Series single-panel display (up to 225 inches) alongside an 85-inch LCD room solution. In 2014 Prysm merged with Anacore to add a multi-source interactive canvas, producing a platform that combines digital whiteboarding, on-screen annotation, co-browsing, device sharing and Teams/Zoom/Webex launching across web, desktop and iPhone clients for customer experience centers, executive boardrooms and huddle rooms. Prysm became part of the Motherson Group in 2025. Prysm announced an early preview of a "Prysm API" for custom applications on its digital workplace platform in June 2017, but publishes no developer
  portal, API reference, or machine-readable specification today.
image: https://www.prysm.com/hubfs/Prysym_Favicon.png
layout: provider
modified: '2026-08-26'
name: Prysm
nav: Providers
network: true
overview: 'Prysm is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Collaboration, Visual Collaboration, Digital Workplace, and Displays.


  Prysm''s developer surface includes documentation, support, engineering blog, signup flow, and 15 more developer resources.'
plans:
- name: Prysm Plans Pricing
  plan_count: 0
  slug: prysm-plans-pricing
random_paper: 4
score:
  band: emerging
  composite: 18.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 18.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/prysm/refs/heads/main/screenshots/prysm-2026-09-02T152256.png
security:
- kind: domain-security
  name: Prysm Domain Security
  slug: prysm-domain-security
  summary_line: TLSv1.3 · DMARC
slug: prysm
tags:
- Company
- Collaboration
- Visual Collaboration
- Digital Workplace
- Displays
- Display Technology
- Hardware
- Meetings
- Whiteboarding
- Enterprise Software
- Unified Communications
website: https://www.prysm.com/
---
