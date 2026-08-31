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
api_count: 2
apis:
- description: Tenant-scoped REST API for retrieving events, alerts, incidents, audit logs, network and application telemetry, and for managing policies, IoCs, and configuration on the Netskope platform. Authenticat
  name: Netskope REST API v2
  slug: rest-api-v2
- description: SCIM 2.0 provisioning API for users and groups, enabling identity providers and IGA platforms to synchronize directory state into Netskope using a dedicated SCIM token issued from the Security Cloud P
  name: Netskope SCIM API
  slug: scim-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/netskope-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/netskope-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/netskopeoss
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/netskope
- group: company
  title: ''
  type: Website
  url: https://www.netskope.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.netskope.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.netskope.com/request-pricing
- group: start
  title: ''
  type: Signup
  url: https://www.netskope.com/request-demo
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.netskope.com/llms.txt
created: '2026-05-11'
description: Netskope is a security service edge (SSE) and SASE platform delivering cloud-native Secure Web Gateway, CASB, Zero Trust Network Access, data loss prevention, and threat protection from its NewEdge global network. The Netskope REST API v2 provides tenant-level programmatic access to events, alerts, incidents, policies, IoCs, SCIM provisioning, and configuration so SOC and platform teams can automate SOAR, SIEM, and IGA workflows using service-account bearer tokens in the Netskope-Api-Token header.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/netskope.png
layout: provider
modified: '2026-05-11'
name: Netskope
nav: Providers
network: true
overview: 'Netskope publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Security, SASE, SSE, CASB, and Zero Trust.


  Netskope''s developer surface includes documentation, pricing, signup flow, and 6 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 12.5
  coverage:
    artifact_dirs: 4
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 12.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/netskope/refs/heads/main/screenshots/netskope-2026-06-20T190208.png
security:
- kind: domain-security
  name: Netskope Domain Security
  slug: netskope-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Netskope Vulnerability Disclosure
  slug: netskope-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: netskope
tags:
- Security
- SASE
- SSE
- CASB
- Zero Trust
- SWG
- DLP
- Cloud Security
website: https://www.netskope.com/
---
