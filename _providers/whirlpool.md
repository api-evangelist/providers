---
access_model:
  confidence: medium
  label: Enterprise · Requires approval
  onboarding: approval
  pricing: enterprise
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 3
apis:
- description: The Whirlpool connected appliances cloud API enables control and monitoring of Whirlpool, Maytag, KitchenAid, and Consul smart appliances including washers, dryers, ovens, refrigerators, and air condi
  name: Whirlpool Connected Appliances API
  slug: connected-appliances
- description: Whirlpool smart appliances integrate with Amazon Alexa to enable voice control of washers, dryers, ovens, and refrigerators across the Whirlpool brand portfolio. Users can start/pause laundry, check c
  name: Whirlpool Alexa Voice Control
  slug: amazon-alexa-integration
- description: Whirlpool was the first appliance company to integrate Amazon Dash Replenishment Service. Whirlpool smart washers monitor laundry detergent levels and automatically reorder supplies via Amazon when ru
  name: Whirlpool Amazon Dash Replenishment
  slug: amazon-dash-replenishment
artifact_total: 11
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/whirlpool-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/whirlpool-corporation
- group: company
  title: ''
  type: Website
  url: https://www.whirlpool.com
- group: company
  title: ''
  type: Website
  url: https://www.whirlpoolcorp.com
- group: other
  title: ''
  type: Smart Appliances
  url: https://www.whirlpool.com/smart-appliances.html
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer-latam.whirlpool.com
- group: other
  title: ''
  type: Wikipedia
  url: https://en.wikipedia.org/wiki/Whirlpool_Corporation
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/whirlpool/refs/heads/main/vocabulary/whirlpool-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/whirlpool/refs/heads/main/json-ld/whirlpool-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/whirlpool/refs/heads/main/json-schema/whirlpool-appliance-schema.json
- group: company
  title: ''
  type: Blog
  url: https://www.whirlpoolcorp.com/latest-news.html
created: '2026-03-21'
description: Whirlpool Corporation is the world's only major U.S.-based manufacturer of kitchen and laundry appliances, with approximately $16 billion in annual net sales and 41,000 employees globally. Its brand portfolio includes Whirlpool, KitchenAid, JennAir, Maytag, Amana, Brastemp, Consul, and InSinkErator. Whirlpool offers connected smart appliances integrating with Amazon Alexa, Amazon Dash Replenishment, Google Assistant, and Matter for smart home automation, and provides a cloud-connected appliance API used by the Whirlpool mobile app and third-party integrations.
finops:
- name: Whirlpool Finops
  service_category: Connected Appliances
  slug: whirlpool-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/whirlpool.png
json_schemas:
- name: Whirlpool Connected Appliance
  property_count: 15
  slug: whirlpool-appliance
json_structures:
- name: Whirlpool Appliance Structure
  property_count: 0
  slug: whirlpool-appliance-structure
jsonld:
- class_count: 44
  name: Whirlpool Context
  property_count: 0
  slug: whirlpool-context
layout: provider
modified: '2026-05-03'
name: Whirlpool Corporation
nav: Providers
network: true
overview: 'Whirlpool Corporation publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Appliances, Smart Home, IoT, Connected Devices, and Fortune 500.


  The Whirlpool Corporation catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Whirlpool Corporation''s developer surface includes engineering blog and 10 more developer resources.'
plans:
- name: Whirlpool Plans Pricing
  plan_count: 1
  slug: whirlpool-plans-pricing
press:
- date: '2026-05-25'
  title: Whirlpool Corporation Migrates SAP Systems to ...
  url: https://www.googlecloudpresscorner.com/2021-06-03-Whirlpool-Corporation-Migrates-SAP-Systems-to-Google-Cloud-for-Sustainable-Growth
- date: '2026-05-25'
  title: Whirlpool Corporation recently held its first ATLAS Data & ...
  url: https://www.instagram.com/p/CyBOb8SO0ic/
- date: '2026-05-25'
  title: Smart Appliances
  url: https://www.whirlpool.com/smart-appliances.html
- date: '2026-05-25'
  title: 'Whirlpool CEO: AI is making kitchens and appliances smarter'
  url: https://fortune.com/videos/watch/Whirlpool-CEO-AI-is-making-kitchens-and-appliances-smarter-/7c21f374-e607-4cb5-845d-f4674a9d6e52
- date: '2026-05-25'
  title: Whirlpool Announces Strategic Recapitalization to ...
  url: https://www.prnewswire.com/news-releases/whirlpool-announces-strategic-recapitalization-to-accelerate-deleveraging-and-strategic-growth-302694986.html
random_paper: 98
rate_limits:
- limit_count: 1
  name: Whirlpool Rate Limits
  slug: whirlpool-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Whirlpool Corporation API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: whirlpool-jsonschema-spectral-rules
score:
  band: emerging
  composite: 17.1
  delta: -6.4
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 25.0
    contract_quality: 11.3
    developer_ergonomics: 7.1
    discoverability: 64.8
    governance: 25.0
    operational_transparency: 5.3
  previous_composite: 23.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/whirlpool/refs/heads/main/screenshots/whirlpool-2026-06-20T201441.png
security:
- kind: domain-security
  name: Whirlpool Domain Security
  slug: whirlpool-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: whirlpool
tags:
- Appliances
- Smart Home
- IoT
- Connected Devices
- Fortune 500
- Consumer Electronics
website: https://www.whirlpool.com
---
