---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 2.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Per-customer JSON REST API over each Uptycs stack covering alerts and alert rules, events and event rules, assets and asset groups/tags, ad-hoc and saved SQL (osquery) queries, threat indicators/sourc
  name: Uptycs Platform API
  slug: uptycs-platform-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://uptycs.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.uptycs.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.uptycs.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.uptycs.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://support.uptycs.com/portal/en/home
- group: company
  title: ''
  type: Blog
  url: https://www.uptycs.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Uptycs
- group: auth
  title: ''
  type: Security
  url: https://www.uptycs.com/about/security
- group: auth
  title: ''
  type: Compliance
  url: https://www.uptycs.com/about/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/uptycs-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/uptycs-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/uptycs-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/uptycs-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/uptycs-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/uptycs-conventions.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/uptycs-llms.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/uptycs-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/uptycs-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/uptycs-well-known.yml
created: '2026-07-17'
description: Uptycs is a unified cloud-native application protection platform (CNAPP) and extended detection and response (XDR) company. Built on osquery — which its founders helped commercialize at scale — the Uptycs platform streams structured telemetry from endpoints, cloud workloads, containers, and Kubernetes into a SQL-queryable security data lake, powering CSPM, CWPP, CIEM, vulnerability management, compliance, threat hunting, and detection and response from a single console. Each customer runs on a dedicated stack ({stack}.uptycs.io) whose JSON REST API covers alerts, events, assets, ad-hoc SQL queries, threat intelligence, lookup tables, and users. Uptycs is backed by investors including Norwest Venture Partners and Sapphire Ventures and maintains active SOC 2 Type II compliance.
image: https://www.uptycs.com/hubfs/About%20Us%20Page%20SPI-2.png
layout: provider
modified: '2026-07-21'
name: Uptycs
nav: Providers
network: true
overview: 'Uptycs publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Security, Cybersecurity, CNAPP, XDR, and Cloud Security.


  Uptycs'' developer surface includes pricing, support, engineering blog, authentication, and 15 more developer resources.'
random_paper: 8
score:
  band: thin
  composite: 26.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 13.2
  previous_composite: 26.7
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/uptycs/refs/heads/main/screenshots/uptycs-2026-09-02T165149.png
security:
- kind: authentication
  name: Uptycs Authentication
  slug: uptycs-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Uptycs Domain Security
  slug: uptycs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Uptycs Vulnerability Disclosure
  slug: uptycs-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Uptycs Trust Center
  slug: uptycs-trust-center
  summary_line: SOC 2 Type II
slug: uptycs
tags:
- Security
- Cybersecurity
- CNAPP
- XDR
- Cloud Security
- Endpoint Security
- Kubernetes Security
- osquery
- Threat Detection
- Compliance
website: https://uptycs.com
---
