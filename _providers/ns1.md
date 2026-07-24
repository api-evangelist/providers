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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.1
  score: 21.2
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: 'REST/JSON API for managing NS1 (IBM NS1 Connect) authoritative DNS: zones, records, answers and filter chains, monitoring jobs, notification lists, data sources and feeds, account/team/user/API-key ma'
  name: NS1 Connect API
  slug: ns1-connect-api
artifact_total: 3
common:
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


  NS1''s developer surface includes documentation, API reference, authentication, CLI, and 12 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 19.5
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 47.8
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 19.5
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
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
- API
- Infrastructure
website: https://ns1.com/
---
