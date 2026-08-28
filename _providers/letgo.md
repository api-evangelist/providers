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
    well_known_catalog: true
  schema_version: 0.2
  score: 2.9
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 1
common:
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/letgo-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/letgo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.letgo.com/
created: '2026-07-17'
description: letgo is a mobile-first classifieds and secondhand marketplace where individuals list, browse, and negotiate on used goods — vehicles, electronics, furniture, and household items — with chat-based buyer/seller messaging and location-based discovery. Launched in 2015 and backed by Naspers/OLX, letgo grew into one of the largest peer-to-peer resale apps in the United States before combining its US operation with OfferUp in 2020. The letgo brand and letgo.com continue to operate as a regional classifieds marketplace; the live site currently serves a Turkish-language catalog (category browsing, search, and an otoplus vehicles section per its robots.txt). letgo publishes no public developer program, API documentation, or SDKs. The application-internal API under /api/ is explicitly disallowed in robots.txt, and the entire site sits behind an Akamai bot-mitigation challenge, so no developer surface could be verified.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/letgo.png
layout: provider
modified: '2026-07-19'
name: LetGo
nav: Providers
network: true
overview: LetGo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Classifieds, Marketplace, Secondhand, and Peer to Peer Commerce.
random_paper: 14
score:
  band: minimal
  composite: 6.9
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.9
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: domain-security
  name: Letgo Domain Security
  slug: letgo-domain-security
  summary_line: TLSv1.3 · DMARC
slug: letgo
tags:
- Company
- Classifieds
- Marketplace
- Secondhand
- Peer to Peer Commerce
- Mobile Commerce
- Consumer
website: https://www.letgo.com/
---
