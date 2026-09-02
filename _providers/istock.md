---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
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
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Istock Agentic Access
  operation_count: 12
  slug: istock-agentic-access
  summary_line: 12 operations · 3 acting
api_count: 1
apis:
- description: Reference data
  name: iStock Countries API
  slug: istock-countries-api
- description: License and download assets
  name: iStock Downloads API
  slug: istock-downloads-api
- description: Image metadata retrieval
  name: iStock Images API
  slug: istock-images-api
- description: OAuth 2.0 token acquisition
  name: iStock OAuth API
  slug: istock-oauth-api
- description: Search creative and editorial assets
  name: iStock Search API
  slug: istock-search-api
- description: Video metadata retrieval
  name: iStock Videos API
  slug: istock-videos-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: iStock API (Getty Images Platform) Countries API
  slug: open-istock-countries-api
- collection_type: open
  name: iStock API (Getty Images Platform) Countries Downloads API
  slug: open-istock-downloads-api
- collection_type: open
  name: iStock API (Getty Platform) Countries Images API
  slug: open-istock-images-api
- collection_type: open
  name: iStock API (Getty Images Platform) Countries OAuth API
  slug: open-istock-oauth-api
- collection_type: open
  name: iStock API (Getty Images Platform) Countries Search API
  slug: open-istock-search-api
- collection_type: open
  name: iStock API (Getty Images Platform) Countries Videos API
  slug: open-istock-videos-api
- collection_type: open
  name: iStock API (Getty Images Platform)
  slug: open-istock
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/istock-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/istock-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/istock-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/istock-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/istockphoto
- group: company
  title: ''
  type: Website
  url: https://www.istockphoto.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.gettyimages.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/istock-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/istock-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/istock-finops.yml
created: '2026-05-08'
description: iStock is Getty Images' royalty-free stock media brand for affordable, subscription-based image, video, illustration, and audio licensing. iStock shares Getty's underlying API platform; partner API access is gated and tied to a commercial licensing agreement.
finops:
- name: Istock Finops
  service_category: Stock Media
  slug: istock-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/istock.png
layout: provider
modified: '2026-05-08'
name: iStock
nav: Providers
network: true
overview: 'iStock publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Countries API, Downloads API, Images API, and 3 more. Tagged areas include Stock Media, Image, Video, Illustrations, and Royalty-Free.


  iStock''s developer surface includes authentication and 9 more developer resources.'
plans:
- name: Istock Plans Pricing
  plan_count: 3
  slug: istock-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 1
  name: Istock Rate Limits
  slug: istock-rate-limits
score:
  band: thin
  composite: 29.8
  coverage:
    artifact_dirs: 9
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 51.5
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 29.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/istock/refs/heads/main/screenshots/istock-2026-06-20T183628.png
security:
- kind: authentication
  name: Istock Authentication
  slug: istock-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Istock Domain Security
  slug: istock-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Istock Vulnerability Disclosure
  slug: istock-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: istock
tags:
- Stock Media
- Image
- Video
- Illustrations
- Royalty-Free
- Getty
website: https://www.istockphoto.com/
---
