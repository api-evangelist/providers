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
    consent_identity: true
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
  score: 2.7
  scored_at: '2026-08-17'
api_count: 2
apis:
- description: 'JSON:API-compliant REST API for NETSCOUT Arbor Sightline (formerly SP/Peakflow), fully discoverable from the root URL /api/sp/. Exposes network traffic data, DDoS alerts, managed objects, mitigations '
  name: Arbor Sightline SP REST API
  slug: arbor-sightline-sp-rest-api
- description: REST API for NETSCOUT Arbor Edge Defense Manager (EDM) covering device management, alert and threat viewing (DDoS alerts, threats), traffic analysis, Contextual Threat Intelligence (CTI) data/config a
  name: Arbor Edge Defense Manager (EDM) API
  slug: arbor-edge-defense-manager-edm-api
artifact_total: 5
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/arbor/edm-api-docs/issues
- group: auth
  title: ''
  type: TrustCenter
  url: security/arbor-networks-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.netscout.com/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/arbor-networks-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.netscout.com/data-privacy-and-trust-center
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/arbor-networks-security.txt
- group: company
  title: ''
  type: Website
  url: https://www.netscout.com/arbor
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.netscout.com/arbor
- group: docs
  title: ''
  type: Documentation
  url: https://arbor.github.io/sp-rest-api-cookbook/
- group: docs
  title: ''
  type: APIReference
  url: https://arbor.github.io/sp-rest-api-cookbook/sp-rest-api-tutorial.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/arbor
- group: build
  title: ''
  type: Packages
  url: packages/arbor-networks-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/arbor-networks-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/arbor-networks-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/arbor-networks-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/arbor-networks-well-known.yml
created: '2026-07-17'
description: Arbor Networks is the DDoS protection and network-visibility division of NETSCOUT (Arbor Networks was acquired by NETSCOUT in 2015). Drawing on more than 25 years of experience and visibility into roughly 800 Tbps of global internet traffic across 550+ service-provider and enterprise customers, Arbor builds products that detect and mitigate distributed denial-of-service (DDoS) attacks and provide network traffic analytics. Its portfolio includes Arbor Sightline (formerly Peakflow SP) for service-provider-scale monitoring, analytics and mitigation orchestration; Arbor Edge Defense (AED) as an inline stateless perimeter appliance; the Arbor Threat Mitigation System (TMS); Arbor Cloud managed scrubbing (16 global scrubbing centers, 15+ Tbps); and Arbor Spectrum/Insight for advanced threat analytics. Arbor exposes programmatic control primarily through the Sightline "SP REST API" (a JSON:API-compliant interface rooted at /api/sp/ on the appliance) and the Edge Defense Manager (EDM)
  API, with first-party client tooling published on GitHub and PyPI.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/arbor-networks.png
layout: provider
modified: '2026-07-18'
name: Arbor Networks
nav: Providers
network: true
overview: 'Arbor Networks publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, DDoS Protection, Network Security, Cybersecurity, and Threat Mitigation.


  Arbor Networks'' developer surface includes documentation, API reference, and 14 more developer resources.'
random_paper: 131
score:
  band: emerging
  composite: 19.6
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 0.0
    developer_ergonomics: 30.4
    discoverability: 68.5
    governance: 12.5
    operational_transparency: 15.8
  previous_composite: 19.6
  provenance:
    conformance: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/arbor-networks/refs/heads/main/screenshots/arbor-networks-2026-07-25T201002.png
security:
- kind: domain-security
  name: Arbor Networks Domain Security
  slug: arbor-networks-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Arbor Networks Vulnerability Disclosure
  slug: arbor-networks-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Arbor Networks Trust Center
  slug: arbor-networks-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, PCI DSS, GDPR
slug: arbor-networks
tags:
- Company
- DDoS Protection
- Network Security
- Cybersecurity
- Threat Mitigation
- Network Visibility
- DDoS
- Security
website: https://www.netscout.com/arbor
---
