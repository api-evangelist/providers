---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bluebirds-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bluebirds.com
coverage:
  checked: '2026-08-13'
  detail: Salesforce completed its acquisition of Bluebirds and every path on bluebirds.com — including /openapi.json, /llms.txt, /pricing and every /.well-known/ path — now answers a blanket HTTP 301 to Salesforce's AI prospecting agent page from an AWS redirect service, while the former app host app.bluebirds.com resolves but resets the TLS handshake.
  evidence:
  - status: 301
    url: https://bluebirds.com/openapi.json
  - status: 301
    url: https://bluebirds.com/.well-known/agent-card.json
  - status: 301
    url: https://bluebirds.com/pricing
  - status: 0
    url: https://app.bluebirds.com/
  reason: defunct
  state: none
created: '2026-07-17'
description: 'Bluebirds was an AI-powered outbound sales and go-to-market (GTM) prospecting platform, founded in 2022 by Rohan Punamia (CEO) and Kunal Punera (CTO). The product helped sales teams create, test, and scale AI-driven prospecting triggers, combining LinkedIn signals with first-party CRM data and de-anonymized web traffic so representatives could target and personalize outreach in a unified workflow. Bluebirds was seed-funded by Lightspeed Venture Partners (invested 2023). Salesforce announced a definitive agreement to acquire Bluebirds in August 2025 and folded the prospecting agent into Sales Cloud and Agentforce, with integration expected complete by the end of Salesforce fiscal Q3 2026. The absorption is now complete: as of August 2026 every path on bluebirds.com — including /pricing, /docs and every /.well-known/ path — answers HTTP 301 to Salesforce''s AI prospecting agent page from an AWS redirect service, api./docs./developer./status./trust subdomains do not resolve, and
  the former application host app.bluebirds.com resolves but resets the TLS handshake. Bluebirds therefore exposes no public developer or API surface of its own; the prospecting capability is now reached through Salesforce, and this profile is identity-only.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bluebirds.png
layout: provider
modified: '2026-08-13'
name: Bluebirds
nav: Providers
network: true
overview: Bluebirds is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sales, Go-To-Market, Prospecting, and Sales Intelligence.
plans:
- name: Bluebirds Plans Pricing
  plan_count: 0
  slug: bluebirds-plans-pricing
random_paper: 11
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 4
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
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bluebirds/refs/heads/main/screenshots/bluebirds-2026-07-25T203443.png
security:
- kind: domain-security
  name: Bluebirds Domain Security
  slug: bluebirds-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bluebirds
tags:
- Company
- Sales
- Go-To-Market
- Prospecting
- Sales Intelligence
- Outbound Sales
- Artificial Intelligence
- Software-as-a-Service
- Lead Generation
website: https://bluebirds.com
---
