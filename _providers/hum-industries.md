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
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hum-industries-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://humindustries.com
- group: start
  title: ''
  type: SignUp
  url: https://humindustries.com
created: '2026-07-17'
description: HUM Industries is a consumer hardware company building a wearable AI assistant designed to enhance social presence. The device records conversations locally, maintains a rolling buffer of recent audio, and surfaces contextual information such as names, personal details, and commitments back to the wearer through subtle audio cues. The company frames the product as giving people "the freedom to forget" by offloading memory to the device so they can stay present in the moment. At the time of profiling the product is pre-launch, offered through a preorder waitlist, with no public API, developer portal, or third-party integration surface. Backed by a16z; added to the API Evangelist network as a portfolio lead.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hum-industries.png
layout: provider
modified: '2026-07-19'
name: HUM Industries
nav: Providers
network: true
overview: 'HUM Industries is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Wearables, Artificial Intelligence, Consumer Hardware, and Voice.


  HUM Industries'' developer surface includes signup flow and 2 more developer resources.'
random_paper: 3
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
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hum-industries/refs/heads/main/screenshots/hum-industries-2026-07-25T221641.png
security:
- kind: domain-security
  name: Hum Industries Domain Security
  slug: hum-industries-domain-security
  summary_line: TLSv1.3 · HSTS
slug: hum-industries
tags:
- Company
- Wearables
- Artificial Intelligence
- Consumer Hardware
- Voice
- Memory
- AI Assistant
website: https://humindustries.com
---
