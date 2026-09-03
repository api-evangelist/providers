---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.3
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: 'REST/JSON API for managing NS1 (IBM NS1 Connect) authoritative DNS: zones, records, answers and filter chains, monitoring jobs, notification lists, data sources and feeds, account/team/user/API-key ma'
  name: NS1 Connect API
  slug: ns1-connect-api
artifact_total: 3
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/ibm/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ns1-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ns1.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.ibm.com/apis/catalog/ns1--ibm-ns1-connect-api/Introduction
- group: docs
  title: ''
  type: Documentation
  url: https://www.ibm.com/docs/en/ns1-connect
- group: docs
  title: ''
  type: APIReference
  url: https://developer.ibm.com/apis/catalog/ns1--ibm-ns1-connect-api/Introduction
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ns1
- group: auth
  title: ''
  type: Authentication
  url: authentication/ns1-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ns1-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ns1-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ns1-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/ns1-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/ns1-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/ns1-cli.yml
- group: other
  title: ''
  type: Protobuf
  url: grpc/ns1-bulkbeacon.proto
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ns1-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ns1-llms.txt
created: '2026-07-17'
description: NS1 (now IBM NS1 Connect) is a managed authoritative DNS, traffic management, and DDI platform. Its data-driven DNS steers traffic with real-time telemetry (Pulsar RUM), health-check monitoring, filter-chain traffic-steering policies, GeoDNS, and dedicated DNS. Everything is programmable through the NS1 REST API at api.nsone.net/v1, authenticated with an X-NSONE-Key API key, and supported by first-party SDKs (Python, Go, JavaScript, PHP), an Ansible module set, a Terraform provider, and a command-line interface. NS1 was acquired by IBM in 2022 and is delivered as IBM NS1 Connect; the api.nsone.net API host and v1 contract remain unchanged.
image: https://github.com/ns1.png
layout: provider
modified: '2026-07-20'
name: NS1
nav: Providers
network: true
overview: 'NS1 publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Networking, DNS, Managed DNS, and Traffic Management.


  NS1''s developer surface includes documentation, API reference, authentication, CLI, and 13 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 25.1
  coverage:
    artifact_dirs: 11
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 26.7
    developer_ergonomics: 52.4
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 25.1
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ns1/refs/heads/main/screenshots/ns1-2026-08-07T185658.png
security:
- kind: authentication
  name: Ns1 Authentication
  slug: ns1-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Ns1 Domain Security
  slug: ns1-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: ns1
tags:
- Company
- Networking
- DNS
- Managed DNS
- Traffic Management
- DDI
- Infrastructure
website: https://ns1.com/
---
