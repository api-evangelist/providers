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
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: GraphQL based NFT API
  name: icy.tools
  slug: icytools
artifact_total: 5
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/icy-tools-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/icy-tools-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/icy-tools-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://developers.icy.tools/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: GraphQL based NFT API
graphqls:
- description: ''
  name: icy.tools GraphQL API
  slug: icy-tools-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/icy-tools.png
layout: provider
modified: '2026-05-28'
name: icy.tools
nav: Providers
network: true
overview: icy.tools publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cryptocurrency and Public APIs.
random_paper: 7
score:
  band: minimal
  composite: 7.3
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/icy-tools/refs/heads/main/screenshots/icy-tools-2026-06-20T183202.png
security:
- kind: domain-security
  name: Icy Tools Domain Security
  slug: icy-tools-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Icy Tools Vulnerability Disclosure
  slug: icy-tools-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Icy Tools Trust Center
  slug: icy-tools-trust-center
  summary_line: SOC 2, ISO 27001
slug: icy-tools
tags:
- Cryptocurrency
- Public APIs
website: https://developers.icy.tools/
---
