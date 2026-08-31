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
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/masergy-domain-security.yml
created: '2026-07-17'
description: Masergy Communications was a managed networking and security provider offering software-defined networking (SD-WAN), secure networking (SASE), managed security services, and unified communications as a service (UCaaS/CCaaS) to enterprises over a global software-defined platform. Masergy was acquired by Comcast Business in October 2021 and folded into Comcast Business; the masergy.com web properties now redirect to business.comcast.com/masergy/. Added to the API Evangelist network as a portfolio company of lightspeed-venture-partners. Enrichment found no live standalone developer portal or API surface (api.masergy.com returns HTTP 502; developer/docs subdomains do not resolve), so this profile documents identity and the probed domain-security posture only.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/masergy.png
layout: provider
modified: '2026-07-20'
name: Masergy
nav: Providers
network: true
overview: Masergy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Networking, SD-WAN, SASE, and Managed Security.
random_paper: 4
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 1
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
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 5.0
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Masergy Domain Security
  slug: masergy-domain-security
  summary_line: TLSv1.2 · DMARC
slug: masergy
tags:
- Company
- Networking
- SD-WAN
- SASE
- Managed Security
- Unified Communications
- Cloud Networking
- Enterprise
---
