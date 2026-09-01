---
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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ossia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ossia.com/
- group: company
  title: ''
  type: About
  url: https://www.ossia.com/about
- group: other
  title: ''
  type: Company
  url: https://www.ossia.com/about/ossia-the-company/
- group: other
  title: ''
  type: Team
  url: https://www.ossia.com/about/team
- group: company
  title: ''
  type: Careers
  url: https://www.ossia.com/about/careers
- group: operate
  title: ''
  type: Contact
  url: https://www.ossia.com/contact
- group: other
  title: ''
  type: Products
  url: https://www.ossia.com/cota
- group: other
  title: ''
  type: Licensing
  url: https://www.ossia.com/licensing
- group: company
  title: ''
  type: Partners
  url: https://www.ossia.com/partners
- group: company
  title: ''
  type: Blog
  url: https://www.ossia.com/blog
- group: company
  title: ''
  type: BlogFeeds
  url: https://www.ossia.com/blog/rss.xml
- group: company
  title: ''
  type: Press
  url: https://www.ossia.com/press
- group: company
  title: ''
  type: News
  url: https://www.ossia.com/news
- group: company
  title: ''
  type: NewsFeeds
  url: https://www.ossia.com/news/rss.xml
- group: learn
  title: ''
  type: Video
  url: https://www.ossia.com/video-blog
- group: other
  title: ''
  type: Research
  url: https://www.ossia.com/rf-wireless-power
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ossia.com/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ossia-inc-/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/ossiainc
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/OssiaInc/
- group: commercial
  title: ''
  type: Plans
  url: plans/ossia-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ossia-llms.txt
- group: company
  title: ''
  type: Partners
  url: https://www.ossia.com/motherson-ossia
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/ossia_stock/
coverage:
  checked: '2026-08-26'
  detail: Ossia licenses RF wireless-power IP and ships Cota transmitter/receiver silicon and reference design kits to authorized licensees — the "software components" in a Cota dev kit are device firmware, not a network service — so there is nothing to expose as an API; www.ossia.com is a 641-URL HubSpot marketing site with no /developers, /api or /docs path, no api./docs./developer./portal. subdomain resolving in DNS at all, and the company's own GitHub org (CotaByOssia, blog ossia.com) has zero public repositories.
  evidence:
  - status: 404
    url: https://www.ossia.com/developers
  - status: 404
    url: https://www.ossia.com/openapi.json
  - status: 404
    url: https://www.ossia.com/llms.txt
  - status: 404
    url: https://www.ossia.com/.well-known/agent-card.json
  - status: 404
    url: https://www.ossia.com/.well-known/security.txt
  - status: 0
    url: https://api.ossia.com/openapi.json
  - status: 200
    url: https://www.ossia.com/licensing
  reason: not-a-software-company
  state: none
created: '2026-08-26'
description: 'Ossia, Inc. is a Redmond, Washington wireless power technology company founded by physicist Hatem Zeine (incorporated as Omnilectric in 2008, operating as Ossia from 2013) and the inventor of Cota Real Wireless Power — a patented RF smart-antenna system that delivers targeted energy over the air to multiple moving devices at a distance, without pads, plugs, cables or line of sight. A Cota receiver emits a beacon and the Cota transmitter returns a focused 2.4 GHz or 5.8 GHz power signal along the same path, which is how the system tracks and powers devices in motion. Ossia does not manufacture products for sale: it licenses the Cota technology to manufacturers, brands and OEMs, ships Cota developer and reference design kits (receiver chip, sample hardware, software components, test instructions) to authorized licensees, and works through joint ventures and development partners such as Motherson Ossia. The company holds 180+ US and international patents, is FCC certified under
  Parts 15 and 18, and carries regulatory approval in the US, UK and 45+ other countries. Ossia publishes no public API, developer portal, SDK or machine-readable contract of any kind — the developer surface it does have is hardware and firmware delivered under license.'
image: https://www.ossia.com/hubfs/OssiaWebFeature-1.png
layout: provider
modified: '2026-08-26'
name: Ossia
nav: Providers
network: true
overview: 'Ossia is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Wireless Power, Wireless Charging, RF Energy, and Power over Air.


  Ossia''s developer surface includes engineering blog, product news, and 23 more developer resources.'
plans:
- name: Ossia Plans Pricing
  plan_count: 0
  slug: ossia-plans-pricing
random_paper: 18
score:
  band: minimal
  composite: 6.7
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 13.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Ossia Domain Security
  slug: ossia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ossia
tags:
- Company
- Wireless Power
- Wireless Charging
- RF Energy
- Power over Air
- Hardware
- Semiconductors
- Internet of Things
- IoT Sensors
- Consumer Electronics
- Automotive
- Technology Licensing
- Deep Tech
- Washington
website: https://www.ossia.com/
---
