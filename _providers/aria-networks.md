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
  band: agent-aware
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
    error_semantics: documented
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
  score: 5.4
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: The Aria API is the REST control surface for the Aria Networks Deep Networking platform. Its unauthenticated root index at https://api.arianetworks.com/ advertises version 1.0.0 and sixteen resource g
  name: Aria API
  slug: aria-api
artifact_total: 3
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/juniper-networks/
- group: company
  title: ''
  type: Website
  url: https://arianetworks.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.arianetworks.com/
- group: start
  title: ''
  type: Login
  url: https://app.arianetworks.com/login
- group: company
  title: ''
  type: Blog
  url: https://arianetworks.com/news
- group: commercial
  title: ''
  type: TermsOfService
  url: https://arianetworks.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://arianetworks.com/privacy
- group: commercial
  title: ''
  type: LicenseAgreement
  url: https://arianetworks.com/eula
- group: operate
  title: ''
  type: Support
  url: mailto:sales@arianetworks.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aria-networks-inc
- group: company
  title: ''
  type: Twitter
  url: https://x.com/AriaNetworks
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aria-networks-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aria-networks-llms.txt
coverage:
  checked: '2026-08-06'
  detail: Aria Networks runs a live REST API at api.arianetworks.com whose unauthenticated root index advertises sixteen /v1 resource groups, but its Mintlify documentation site 302-redirects every single path — including /llms.txt and /docs.json — to /login, and the doc_url that every API error response points at (https://api.arianetworks.com/reference) returns 404, so no reference or spec is reachable without a customer account.
  evidence:
  - status: 302
    url: https://docs.arianetworks.com/
  - status: 200
    url: https://api.arianetworks.com/
  - status: 404
    url: https://api.arianetworks.com/reference
  - status: 401
    url: https://api.arianetworks.com/v1/fabrics
  - status: 404
    url: https://arianetworks.com/llms.txt
  reason: customer-only-docs
  state: gated
created: '2026-08-06'
description: Aria Networks, Inc. is a Palo Alto, California networking company founded in 2025 by Mansour Karam (founder and former CEO of Apstra, acquired by Juniper Networks in 2020) that builds "Deep Networking" — an AI-native networking system for AI factories and GPU data centers. The platform pairs purpose-built 800GbE and 1.6Tbps Ethernet switches on Broadcom Tomahawk 5 and Tomahawk 6 silicon running a hardened SONiC network OS with microsecond-resolution telemetry agents on switch ASICs, switch-OS kernels, transceivers, server NICs and GPU clusters, plus a reasoning layer that detects, root-causes and resolves fabric issues. Aria measures itself on Model FLOPS Utilization (MFU) and token efficiency rather than traditional network metrics. The company disclosed $125M in funding from Sutter Hill Ventures, Atreides Management, Valor Equity Partners and Eclipse Ventures in April 2026. A production REST API is live at api.arianetworks.com (Aria API 1.0.0), but its reference documentation
  and machine-readable specification sit behind a customer login.
image: https://arianetworks.com/og/aria_opengraph.png
layout: provider
modified: '2026-08-06'
name: Aria Networks
nav: Providers
network: true
overview: 'Aria Networks publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Networking, Data-Center, Artificial Intelligence, and Infrastructure.


  Aria Networks'' developer surface includes documentation, engineering blog, support, and 10 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 18.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 18.4
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
security:
- kind: authentication
  name: Aria Networks Authentication
  slug: aria-networks-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Aria Networks Domain Security
  slug: aria-networks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aria-networks
tags:
- Company
- Networking
- Data-Center
- Artificial Intelligence
- Infrastructure
- Telemetry
- Observability
- Ethernet
- Hardware
website: https://arianetworks.com/
---
