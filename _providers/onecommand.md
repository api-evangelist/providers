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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/onecommand-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.onecommand.com/
coverage:
  checked: '2026-08-13'
  detail: OneCommand was absorbed into Affinitiv in the 2016 four-way merger and its own web presence is now dead — onecommand.com and portal.onecommand.com still resolve to Cloudflare but the origin behind them answers HTTP 522 on every path, highergear.com refuses connections, karmotive.com does not resolve at all, and onecommand.net and trafficaccelerator.com serve parked "/lander" holding pages.
  evidence:
  - status: 522
    url: https://www.onecommand.com/
  - status: 522
    url: https://portal.onecommand.com/.well-known/security.txt
  - status: 522
    url: https://www.onecommand.com/openapi.json
  - status: 200
    url: https://onecommand.net/
  - status: 404
    url: https://www.affinitiv.com/developers
  reason: defunct
  state: none
created: '2026-07-17'
description: OneCommand was a cloud-based customer marketing and loyalty-automation platform built for automotive dealerships, headquartered in Mason, Ohio. It helped dealers drive service and sales traffic, increase owner retention, and lower marketing costs through data-driven, multichannel outreach across voice, text, email, and direct mail. Its product family included the OneCommand loyalty-automation platform, the Higher Gear CRM, and the TrafficAccelerator service. OneCommand was absorbed into Affinitiv in September 2016, one of four automotive-marketing firms (with TimeHighway.com, Peak Performance and DPS) merged to form that company. The brand is now defunct as an operating surface — onecommand.com and portal.onecommand.com are still fronted by Cloudflare but the origin no longer answers (HTTP 522 on every path probed 2026-08-13), highergear.com no longer connects, and onecommand.net and trafficaccelerator.com resolve to parked landing pages. OneCommand never published a public
  developer API, developer portal, SDKs, or API documentation, and the acquirer's site (affinitiv.com) publishes none either.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/onecommand.png
layout: provider
modified: '2026-08-13'
name: OneCommand
nav: Providers
network: true
overview: OneCommand is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Automotive, Marketing, Customer Loyalty, and Marketing Automation.
random_paper: 7
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.0
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
security:
- kind: domain-security
  name: Onecommand Domain Security
  slug: onecommand-domain-security
  summary_line: TLSv1.3 · DMARC
slug: onecommand
tags:
- Company
- Automotive
- Marketing
- Customer Loyalty
- Marketing Automation
- CRM
- Dealership
website: http://www.onecommand.com/
---
