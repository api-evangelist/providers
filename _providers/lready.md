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
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/lready-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/lready-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lready-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://life360.com
created: '2026-07-17'
description: Lready, Inc. was the original 2007 incorporated name of Life360 — the family safety and location-sharing company that rebranded to Life360, Inc. in October 2011. Life360 operates a consumer mobile platform (iOS and Android) for real-time family location sharing, driving safety, crash detection, roadside and emergency response, and is publicly traded. This profile resolves the "Lready" venture-portfolio lead to its operating entity, Life360, and captures the security posture the company exposes at its production domain. Life360 does not publish a public first-party developer API program or OpenAPI, so no API-surface artifacts are derived here.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lready.png
layout: provider
modified: '2026-07-20'
name: Lready
nav: Providers
network: true
overview: Lready is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Location Sharing, Family Safety, Mobile App, and Consumer.
random_paper: 11
score:
  band: minimal
  composite: 6.4
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
    operational_transparency: 10.5
  previous_composite: 6.4
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lready/refs/heads/main/screenshots/lready-2026-07-25T225631.png
security:
- kind: domain-security
  name: Lready Domain Security
  slug: lready-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Lready Vulnerability Disclosure
  slug: lready-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: lready
tags:
- Company
- Location Sharing
- Family Safety
- Mobile App
- Consumer
- Safety
- Location
website: https://life360.com
---
