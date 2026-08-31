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
api_count: 1
apis:
- description: Generate merchant-specific and one-time use credit card numbers that link back to your bank
  name: Privacy.com
  slug: privacycom
artifact_total: 3
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/privacy-com-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/privacy-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://privacy.com/developer/docs
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: company
  title: ''
  type: Blog
  url: https://privacy.com/blog
created: '2026-05-28'
description: Generate merchant-specific and one-time use credit card numbers that link back to your bank
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/privacy-com.png
layout: provider
modified: '2026-05-28'
name: Privacy.com
nav: Providers
network: true
overview: 'Privacy.com publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Security and Public APIs.


  Privacy.com''s developer surface includes engineering blog and 4 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 8.7
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
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.7
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/privacy-com/refs/heads/main/screenshots/privacy-com-2026-06-20T192119.png
security:
- kind: domain-security
  name: Privacy Com Domain Security
  slug: privacy-com-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Privacy Com Trust Center
  slug: privacy-com-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS
slug: privacy-com
tags:
- Security
- Public APIs
website: https://privacy.com/developer/docs
---
