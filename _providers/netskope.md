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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.4
  scored_at: '2026-10-17'
api_count: 4
apis:
- description: Tenant-scoped REST API for retrieving events, alerts, incidents, audit logs, network and application telemetry, and for managing policies, IoCs, and configuration on the Netskope platform. Authenticat
  name: Netskope REST API v2
  slug: rest-api-v2
- description: SCIM 2.0 provisioning API for users and groups, enabling identity providers and IGA platforms to synchronize directory state into Netskope using a dedicated SCIM token issued from the Security Cloud P
  name: Netskope SCIM API
  slug: scim-api
- baseURL: https://{tenant}.goskope.com/api/v2
  baseurl_source: declared
  description: The Deviceclassification API from Netskope — 1 operation(s) for deviceclassification.
  name: Netskope Deviceclassification API
  slug: netskope-deviceclassification-api
- baseURL: https://{tenant}.goskope.com/api/v2
  baseurl_source: declared
  description: The Scale API from Netskope — 2 operation(s) for scale.
  name: Netskope Scale API
  slug: netskope-scale-api
artifact_total: 8
asyncapis:
- description: ''
  name: Netskope Webhooks
  slug: netskope-webhooks
common:
- group: company
  title: ''
  type: Blog
  url: https://www.netskope.com/company/newsroom
- group: company
  title: ''
  type: BlogRSS
  url: https://www.netskope.com/feed
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/netskope/refs/heads/main/security/netskope-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/netskope-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/netskope/refs/heads/main/security/netskope-domain-security.yml
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
modified: '2026-10-06'
name: Netskope
nav: Providers
network: true
overview: 'Netskope is listed with 4 APIs on the [APIs.io](https://apis.io/) network, including Deviceclassification API, Scale API, and 2 more. Tagged areas include Security, SASE, SSE, CASB, and Zero Trust.


  The Netskope catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Netskope''s developer surface includes engineering blog, documentation, pricing, signup flow, and 7 more developer resources.'
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: Netskope API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: netskope-rules
score:
  band: emerging
  composite: 21.0
  coverage:
    artifact_dirs: 17
    catalog_earned: 44.5
    catalog_earned_first_party: 0.0
    catalog_gap: 70.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -27.4
  facets:
    access_clarity: 13.2
    contract_governance: 31.8
    contract_quality: 17.3
    developer_ergonomics: 11.9
    discoverability: 78.6
    operational_transparency: 2.6
  previous_composite: 48.4
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: falling
  upsert:
    applies: true
    score: 0.0
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
