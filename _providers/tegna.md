---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Tegna Agentic Access
  operation_count: 15
  slug: tegna-agentic-access
  summary_line: 15 operations · 4 acting
api_count: 7
apis:
- description: The Audiences API from TEGNA — 2 operation(s) for audiences.
  name: TEGNA Audiences API
  slug: tegna-audiences-api
- description: The Campaigns API from TEGNA — 2 operation(s) for campaigns.
  name: TEGNA Campaigns API
  slug: tegna-campaigns-api
- description: The Creatives API from TEGNA — 1 operation(s) for creatives.
  name: TEGNA Creatives API
  slug: tegna-creatives-api
- description: The Inventory API from TEGNA — 1 operation(s) for inventory.
  name: TEGNA Inventory API
  slug: tegna-inventory-api
- description: The Markets API from TEGNA — 1 operation(s) for markets.
  name: TEGNA Markets API
  slug: tegna-markets-api
- description: The OTT Campaigns API from TEGNA — 2 operation(s) for ott campaigns.
  name: TEGNA OTT Campaigns API
  slug: tegna-ott-campaigns-api
- description: The Reporting API from TEGNA — 1 operation(s) for reporting.
  name: TEGNA Reporting API
  slug: tegna-reporting-api
artifact_total: 22
collections:
- collection_type: open
  name: TEGNA AudienceOne API
  slug: open-tegna-audience-one
- collection_type: open
  name: TEGNA Premion OTT Advertising API
  slug: open-tegna-premion
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tegna-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tegna-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tegna-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.tegna.com
- group: company
  title: ''
  type: Website
  url: https://www.nexstar.tv/
- group: other
  title: ''
  type: Advertising
  url: https://www.tegna.com/advertise/
- group: docs
  title: ''
  type: Documentation
  url: https://www.tegna.com/advertise/solutions/digital/
- group: docs
  title: ''
  type: Documentation
  url: https://www.tegna.com/advertise/solutions/broadcast/
- group: docs
  title: ''
  type: Documentation
  url: https://www.tegna.com/advertise/solutions/streaming/
- group: company
  title: ''
  type: Website
  url: https://premion.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tegna
- group: company
  title: ''
  type: Blog
  url: https://www.tegna.com/feed/
created: '2026-03-24'
description: TEGNA Inc. is an American broadcast, digital media, and marketing services company headquartered in Tysons, Virginia, operating as a subsidiary of Nexstar Media Group following FCC approval of the $6.2 billion acquisition in March 2026. TEGNA operates 64 full-power broadcast television stations across 51 U.S. markets, reaching approximately 39 percent of all television households. TEGNA offers digital marketing solutions including AudienceOne first-party data targeting, OTT/CTV advertising through its Premion platform, and the TEGNA Marketing Solutions full-service agency. The company provides advertising APIs and programmatic integrations for digital, broadcast, streaming, and connected TV advertising campaigns.
examples:
- key_count: 2
  name: Tegna Get Campaign Performance Example
  slug: tegna-get-campaign-performance-example
- key_count: 2
  name: Tegna List Campaigns Example
  slug: tegna-list-campaigns-example
finops:
- name: Tegna Finops
  service_category: Media / Advertising
  slug: tegna-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tegna.png
json_schemas:
- name: TEGNA Advertising Campaign
  property_count: 10
  slug: tegna-campaign
json_structures:
- name: Tegna Campaign Structure
  property_count: 0
  slug: tegna-campaign-structure
jsonld:
- class_count: 37
  name: Tegna Context
  property_count: 0
  slug: tegna-context
layout: provider
modified: '2026-05-19'
name: TEGNA
nav: Providers
network: true
overview: 'TEGNA publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Audiences API, Campaigns API, Creatives API, and 4 more. Tagged areas include Broadcasting, Media, Television, Digital Advertising, and OTT.


  The TEGNA catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  TEGNA''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Tegna Plans Pricing
  plan_count: 1
  slug: tegna-plans-pricing
press:
- date: '2026-05-25'
  title: Nexstar Media Group's proposed acquisition of Tegna Inc. ...
  url: https://www.facebook.com/12NewsNow/posts/nexstar-media-groups-proposed-acquisition-of-tegna-inc-was-announced-in-august-2/1411894880980522/
- date: '2026-05-25'
  title: 'Ask ChatGPT: Why Should I Advertise with TEGNA?'
  url: https://www.tegna.com/advertise/ask-chatgpt-why-should-i-advertise-with-tegna/
- date: '2026-05-25'
  title: How Local Stations Are Leveraging AI To Increase ...
  url: https://tvnewscheck.com/ai/article/how-local-stations-are-leveraging-ai-to-increase-revenue-and-improve-efficiencies/
- date: '2026-05-25'
  title: Big Tent AI Comments to OMB
  url: https://publicknowledge.org/policy/big-tent-ai-comments-to-omb/
- date: '2026-05-25'
  title: Nexstar Media Group, Inc. Enters into Definitive Agreement ...
  url: https://www.nexstar.tv/nexstar-media-group-inc-enters-into-definitive-agreement-to-acquire-tegna-inc-for-6-2-billion-in-accretive-transaction/
random_paper: 47
rate_limits:
- limit_count: 1
  name: Tegna Rate Limits
  slug: tegna-rate-limits
rules:
- name: TEGNA API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: tegna-jsonschema-spectral-rules
- name: TEGNA API Rules
  rule_count: 10
  severity_counts:
    error: 3
    hint: 1
    info: 0
    warn: 6
  slug: tegna-rules
score:
  band: developing
  composite: 44.8
  delta: -4.1
  facets:
    commercial_clarity: 28.9
    contract_quality: 70.1
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 48.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tegna/refs/heads/main/screenshots/tegna-2026-06-20T195014.png
security:
- kind: authentication
  name: Tegna Authentication
  slug: tegna-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Tegna Domain Security
  slug: tegna-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tegna
tags:
- Broadcasting
- Media
- Television
- Digital Advertising
- OTT
- CTV
- Fortune 500
website: https://www.tegna.com
---
