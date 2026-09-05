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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.9
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/valon-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/valon-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://valon.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://gestaltd.ai
- group: docs
  title: ''
  type: Documentation
  url: https://gestaltd.ai
- group: docs
  title: ''
  type: APIReference
  url: https://gestaltd.ai/reference/http-api
- group: start
  title: ''
  type: GettingStarted
  url: https://gestaltd.ai/getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/valon-technologies
- group: company
  title: ''
  type: Blog
  url: https://valon.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://help.valon.com/hc/en-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://valon.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://valon.com/privacy-policy
- group: build
  title: ''
  type: Packages
  url: packages/valon-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/valon-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/valon-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/valon-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/valon-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/valon-conformance.yml
- group: build
  title: ''
  type: CLI
  url: cli/valon-cli.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/valon-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/valon-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/valon-llms.txt
- group: other
  title: ''
  type: Protobuf
  url: grpc/valon-grpc.yml
- group: auth
  title: ''
  type: Compliance
  url: https://valon.com/security/
created: '2026-07-17'
description: Valon is a technology-first residential mortgage servicing platform founded in 2019 and headquartered in New York. Built on its own servicing system of record, Valon gives homeowners a modern app for payments, escrow, insurance, and mortgage assistance while offering lending (HELOC/HELOAN, refinance, purchase) and insurance products. Backed by Andreessen Horowitz and Westcap, Valon raised a $100M Series C in October 2024 and was approved as a Ginnie Mae issuer in December 2024. Its engineering arm, Valon Technologies, also publishes Gestalt (gestaltd.ai) — an Apache-2.0, self-hostable platform for managing agentic tools and services that unifies REST/OpenAPI, GraphQL, MCP, and executable code behind one operation model with an HTTP API, CLI, SDKs, and an MCP endpoint.
image: https://valon.com/wp-content/uploads/2023/03/brandmark-light-1.svg
layout: provider
mcp_servers:
- description: ''
  name: Gestalt MCP Server (self-hosted)
  slug: gestalt-mcp-server-self-hosted
modified: '2026-07-21'
name: Valon
nav: Providers
network: true
overview: 'Valon is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Mortgages, Loan Servicing, Lending, and Fintech.


  Valon''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, CLI, and 17 more developer resources.'
random_paper: 19
score:
  band: developing
  composite: 41.7
  coverage:
    artifact_dirs: 14
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 26.7
    developer_ergonomics: 71.4
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 21.1
  previous_composite: 41.7
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 45.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/valon/refs/heads/main/screenshots/valon-2026-09-02T165329.png
security:
- kind: authentication
  name: Valon Authentication
  slug: valon-authentication
  summary_line: http-bearer/session-cookie · 2 schemes
- kind: domain-security
  name: Valon Domain Security
  slug: valon-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Valon Trust Center
  slug: valon-trust-center
  summary_line: SOC 2
slug: valon
tags:
- Company
- Mortgages
- Loan Servicing
- Lending
- Fintech
- Real-Estate
- Insurance
- Agentic Tools
- MCP
- Open-Source
website: https://valon.com
---
