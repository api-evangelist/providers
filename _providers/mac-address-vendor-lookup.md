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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: Retrieve vendor details and other information regarding a given MAC address or an OUI
  name: MAC address vendor lookup
  slug: mac-address-vendor-lookup
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mac-address-vendor-lookup-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://macaddress.io/api
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Retrieve vendor details and other information regarding a given MAC address or an OUI
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mac-address-vendor-lookup.png
layout: provider
modified: '2026-05-28'
name: MAC address vendor lookup
nav: Providers
network: true
overview: MAC address vendor lookup publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Development and Public APIs.
random_paper: 32
score:
  band: minimal
  composite: 5.7
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.7
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mac-address-vendor-lookup/refs/heads/main/screenshots/mac-address-vendor-lookup-2026-06-20T184823.png
security:
- kind: domain-security
  name: Mac Address Vendor Lookup Domain Security
  slug: mac-address-vendor-lookup-domain-security
  summary_line: TLSv1.3 · DMARC
slug: mac-address-vendor-lookup
tags:
- Development
- Public APIs
website: https://macaddress.io/api
---
