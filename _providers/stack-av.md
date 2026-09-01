---
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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://stackav.com/
- group: company
  title: ''
  type: About
  url: https://stackav.com/about
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/stackav-oss
- group: commercial
  title: ''
  type: TermsOfService
  url: https://stackav.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://stackav.com/privacy
- group: company
  title: ''
  type: Careers
  url: https://stackav.com/join
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/stackav/
- group: build
  title: ''
  type: Packages
  url: packages/stack-av-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/stack-av-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stack-av-domain-security.yml
coverage:
  checked: '2026-08-29'
  detail: Stack AV sells an autonomous freight service, not software — its stackav.com Next.js site is six marketing pages (home, about, safety, join, terms, privacy) with no developer section, and while the company does run a real open-source org at github.com/stackav-oss shipping ML libraries (dltype, conch-triton-kernels), none of them is an API client and no API host exists to call.
  evidence:
  - status: 404
    url: https://stackav.com/developers
  - status: 404
    url: https://stackav.com/openapi.json
  - status: 404
    url: https://stackav.com/.well-known/api-catalog
  - status: 0
    url: https://api.stackav.com/
  - status: 200
    url: https://github.com/stackav-oss
  reason: no-developer-program
  state: none
created: '2026-08-29'
description: Stack AV is a Pittsburgh, Pennsylvania autonomous-vehicle company founded in 2023 by Bryan Salesky (CEO), Peter Rander (President) and Brett Browning (CTO) — the leadership team behind Argo AI — and backed by SoftBank Group. The company develops AI-driven autonomy software and hardware for Class 8 commercial freight trucking, targeting driver shortages, vehicle uptime, safety, operating cost and emissions, and in May 2026 unveiled its first autonomous truck built in collaboration with PACCAR and Peterbilt Motors. Stack AV runs a public open-source engineering organization at github.com/stackav-oss (dltype, conch Triton kernels, clockwork, scene-tokens, push-guard, ai-workloads). It publishes no public developer program, API reference, or machine-readable API contract as of August 2026 — the product is an autonomous freight service, not a developer platform.
image: https://stackav.com/Stack_Primary_Stacked_Blue_RGB_.jpg
layout: provider
modified: '2026-08-29'
name: Stack AV
nav: Providers
network: true
overview: Stack AV is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Autonomous Vehicles, Transportation, Trucking, and Freight.
random_paper: 17
score:
  band: minimal
  composite: 10.3
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 10.3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Stack Av Domain Security
  slug: stack-av-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: stack-av
tags:
- Company
- Autonomous Vehicles
- Transportation
- Trucking
- Freight
- Logistics
- Artificial Intelligence
- Robotics
- Machine-Learning
- Open-Source
website: https://stackav.com/
---
