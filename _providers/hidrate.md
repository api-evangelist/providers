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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
  score: 20.3
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://hidratespark.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hidratespark.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hidratespark.com/policies/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://hidratespark.com/pages/contact-hidrate-spark
- group: agent
  title: ''
  type: WellKnown
  url: well-known/hidrate-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hidrate-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hidrate-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hidrate-domain-security.yml
created: '2026-07-17'
description: HidrateSpark is the world's smartest water bottle brand, tracking daily water intake with a Bluetooth-connected sensor puck that glows to remind you to drink and syncs to the HidrateSpark hydration app, Fitbit, and Apple Watch. The company (originally Hidrate, Inc., a Techstars-backed startup) sells its smart bottles and accessories through a Shopify-hosted direct-to-consumer storefront at hidratespark.com. It does not publish a first-party developer or product API; the only machine-facing surface is the Shopify platform layer — OIDC/OAuth customer accounts and the Universal Commerce Protocol (UCP) agent-commerce endpoints that let buyer-approved AI shopping agents browse and check out.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hidrate.png
layout: provider
mcp_servers:
- description: ''
  name: HidrateSpark UCP commerce MCP (Shopify platform)
  slug: hidratespark-ucp-commerce-mcp-shopify-platform
modified: '2026-07-19'
name: Hidrate
nav: Providers
network: true
overview: 'Hidrate is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Smart Water Bottle, Hydration, Consumer Hardware, and Wearables.


  Hidrate''s developer surface includes support and 7 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 11.9
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.9
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 25.0
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hidrate/refs/heads/main/screenshots/hidrate-2026-08-07T170124.png
security:
- kind: domain-security
  name: Hidrate Domain Security
  slug: hidrate-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hidrate
tags:
- Company
- Smart Water Bottle
- Hydration
- Consumer Hardware
- Wearables
- Health and Fitness
- Bluetooth
- IoT
- E-Commerce
- Shopify
website: https://hidratespark.com/
---
