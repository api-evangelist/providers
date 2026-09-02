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
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Provide access to BinaryEdge 40fy scanning platform
  name: BinaryEdge
  slug: binaryedge
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/binaryedge-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/binaryedge-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://docs.binaryedge.io/api-v2.html
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Provide access to BinaryEdge 40fy scanning platform
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/binaryedge.png
layout: provider
modified: '2026-05-28'
name: BinaryEdge
nav: Providers
network: true
overview: BinaryEdge publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Security and Public APIs.
random_paper: 0
score:
  band: minimal
  composite: 5.7
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
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.7
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/binaryedge/refs/heads/main/screenshots/binaryedge-2026-06-20T173243.png
security:
- kind: domain-security
  name: Binaryedge Domain Security
  slug: binaryedge-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Binaryedge Vulnerability Disclosure
  slug: binaryedge-vulnerability-disclosure
  summary_line: disclosure policy published
slug: binaryedge
tags:
- Security
- Public APIs
website: https://docs.binaryedge.io/api-v2.html
---
