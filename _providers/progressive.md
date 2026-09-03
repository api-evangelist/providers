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
    agentic_commerce: false
    auth_clarity: bearer
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Progressive Agentic Access
  operation_count: 7
  slug: progressive-agentic-access
  summary_line: 7 operations · 2 acting
api_count: 2
apis:
- baseURL: https://api.progressive.com
  baseurl_source: declared
  description: Generate and manage certificates of insurance.
  name: Progressive Certificates API
  slug: progressive-certificates-api
- baseURL: https://api.progressive.com
  baseurl_source: declared
  description: Manage driver profiles for quoting.
  name: Progressive Drivers API
  slug: progressive-drivers-api
- baseURL: https://api.progressive.com
  baseurl_source: declared
  description: Retrieve policy information for certificate generation.
  name: Progressive Policies API
  slug: progressive-policies-api
- baseURL: https://api.progressive.com
  baseurl_source: declared
  description: Create and retrieve auto insurance quotes.
  name: Progressive Quotes API
  slug: progressive-quotes-api
- baseURL: https://api.progressive.com
  baseurl_source: declared
  description: Manage vehicle information for quoting.
  name: Progressive Vehicles API
  slug: progressive-vehicles-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Progressive Auto Quote API
  slug: open-progressive-auto-quote-api
- collection_type: open
  name: Progressive Certificate of Insurance API
  slug: open-progressive-certificate-of-insurance-api
- collection_type: open
  name: Progressive Auto Quote Certificates API
  slug: open-progressive-certificates-api
- collection_type: open
  name: Progressive Auto Quote Certificates Drivers API
  slug: open-progressive-drivers-api
- collection_type: open
  name: Progressive Auto Quote Certificates Policies API
  slug: open-progressive-policies-api
- collection_type: open
  name: Progressive Auto Quote Certificates Quotes API
  slug: open-progressive-quotes-api
- collection_type: open
  name: Progressive Auto Quote Certificates Vehicles API
  slug: open-progressive-vehicles-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/progressive-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/progressive-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/progressive-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/progressive-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/the-progressive-corporation
- group: start
  title: ''
  type: Portal
  url: https://developer.progressive.com/s/
- group: company
  title: ''
  type: Website
  url: https://www.progressive.com/
created: '2026-03-21'
description: The Progressive Corporation is one of the largest providers of car insurance in the United States, also offering personal and commercial auto, home, renters, boat, motorcycle, and other insurance products. Progressive operates a developer portal at developer.progressive.com offering APIs for auto insurance quoting, certificate of insurance generation, and agent portal integrations.
finops:
- name: Progressive Finops
  service_category: Insurance
  slug: progressive-finops
graphqls:
- description: Progressive Insurance is one of the largest auto insurers in the United States, offering personal and commercial auto, home, renters, motorcycle, boat, RV, and other insurance products. Progressive op
  name: Progressive Insurance GraphQL Schema
  slug: progressive-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/progressive.png
layout: provider
modified: '2026-05-19'
name: Progressive
nav: Providers
network: true
overview: 'Progressive publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Certificates API, Drivers API, Policies API, and 2 more. Tagged areas include Auto Insurance, Commercial Insurance, Embedded Insurance, Insurance, and Quoting.


  Progressive''s developer surface includes authentication, developer portal, and 5 more developer resources.'
plans:
- name: Progressive Plans Pricing
  plan_count: 1
  slug: progressive-plans-pricing
press:
- date: '2026-05-25'
  title: Progressive CEO Tricia Griffith Prioritizes AI for Strategic ...
  url: https://www.linkedin.com/posts/ron-arnold-40723644_progressive-investors-hear-about-ai-strategies-activity-7440542524496228352-TMwt
- date: '2026-05-25'
  title: Progressive Insurance® Imagines a World Where Animals ...
  url: https://progressive.mediaroom.com/news-releases/?item=122548
- date: '2026-05-25'
  title: Artificial Intelligence at Progressive Insurance - Two Use ...
  url: https://emerj.com/artificial-intelligence-at-progressive-insurance/
- date: '2026-05-25'
  title: 'How Progressive is thinking about AI. #progressive ...'
  url: https://www.instagram.com/reel/DXIYDGDDamB/
- date: '2026-05-25'
  title: Progressive Insurance tests limits of AI-generated ads
  url: https://www.thedrum.com/news/progressive-insurance-tests-limits-ai-generated-ads-and-learns-when-pull-back
random_paper: 12
rate_limits:
- limit_count: 1
  name: Progressive Rate Limits
  slug: progressive-rate-limits
score:
  band: thin
  composite: 28.3
  coverage:
    artifact_dirs: 14
    catalog_gap: 71.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 53.0
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 28.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 18.2
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/progressive/refs/heads/main/screenshots/progressive-2026-06-20T192149.png
security:
- kind: authentication
  name: Progressive Authentication
  slug: progressive-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Progressive Domain Security
  slug: progressive-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: progressive
tags:
- Auto Insurance
- Commercial Insurance
- Embedded Insurance
- Insurance
- Quoting
- Fortune 500
website: https://www.progressive.com/
---
