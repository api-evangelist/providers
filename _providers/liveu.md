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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/liveu-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.liveu.tv/security
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/liveu-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.liveu.tv/security
- group: auth
  title: ''
  type: DomainSecurity
  url: security/liveu-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.liveu.tv/
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.liveu.tv/hc/en-us
- group: operate
  title: ''
  type: Support
  url: https://support.liveu.tv/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.liveu.tv/resources/blog
- group: other
  title: ''
  type: Products
  url: https://www.liveu.tv/products
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.liveu.tv/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.liveu.tv/terms-of-use
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/liveu-llms.txt
created: '2026-07-17'
description: LiveU is a provider of cloud-based, IP-bonded live video contribution, production, and distribution technology for broadcasters, sports, news, public safety, and enterprise. Its portfolio spans field encoders (the LU-series and the Q Era LU900Q), the LiveU Central cloud management platform, LiveU Studio and Nexus production tools, the LiveU Matrix distribution grid, DataBridge and LU-LINK connectivity, and the LiveU Solo streaming line. LiveU pioneered bonded-cellular transmission that aggregates multiple LTE/5G, Wi-Fi, and satellite links into a single reliable, low-latency video feed. This profile was surfaced as a venture-capital portfolio company and enriched by the API Evangelist pipeline; LiveU publishes marketing, support, and training surfaces but no public developer portal, OpenAPI, or open API documentation was found - the LiveU Central API is available to customers behind authentication.
image: https://www.liveu.tv/wp-content/uploads/2021/09/liveu-logo.png
layout: provider
modified: '2026-07-20'
name: Liveu
nav: Providers
network: true
overview: 'Liveu is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Live Video, Video Streaming, Broadcast, and Bonded Cellular.


  Liveu''s developer surface includes support, engineering blog, and 11 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 15.9
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 15.9
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/liveu/refs/heads/main/screenshots/liveu-2026-07-25T225402.png
security:
- kind: domain-security
  name: Liveu Domain Security
  slug: liveu-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Liveu Vulnerability Disclosure
  slug: liveu-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Liveu Trust Center
  slug: liveu-trust-center
  summary_line: SOC 2 Type 2, ISO 27001
slug: liveu
tags:
- Company
- Live Video
- Video Streaming
- Broadcast
- Bonded Cellular
- Video Contribution
- Media and Entertainment
- Sports Production
- Public Safety
- 5G
website: https://www.liveu.tv/
---
