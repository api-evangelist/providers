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
    agent_skills: derived
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 16.4
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: 'Karat''s GraphQL API for managing technical-interview hiring workflows: query candidacies, roles, groups and users; invite candidates into assessments; and bulk-update candidacy dispositions. Hosted pe'
  name: Karat GraphQL API
  slug: karat-graphql-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://karat.com
- group: docs
  title: ''
  type: Documentation
  url: https://karat.slab.com/posts/karat-api-documentation-dezzam7y
- group: docs
  title: ''
  type: APIReference
  url: https://karat.slab.com/posts/karat-api-overview-6l4gprc3
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/karat/api-sdk#installation
- group: docs
  title: ''
  type: GraphQL
  url: https://github.com/karat/api-docs
- group: build
  title: ''
  type: Postman
  url: https://github.com/karat/api-docs/tree/main/Postman
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/karat
- group: company
  title: ''
  type: Blog
  url: https://karat.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://karat.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://karat.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://karat.com/privacy/
- group: auth
  title: ''
  type: Compliance
  url: https://karat.com/customer-faq/
- group: build
  title: ''
  type: SDKs
  url: packages/karat-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/karat-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/karat-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/karat-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/karat-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/karat-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/karat-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/karat-sandbox.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/karat-well-known.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/karat-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/karat-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/karat-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/karat-llms.txt
- group: docs
  title: ''
  type: GraphQLOperations
  url: graphql/karat-operations.graphql
created: '2026-07-17'
description: Karat Inc. is a Seattle-based technical interviewing platform that conducts standardized software engineering interviews for enterprise hiring teams through its community of trained Interview Engineers. Karat exposes a GraphQL API, hosted per-customer at https://{subdomain}.karat.io/api/v1/graphql, that lets talent and ATS systems programmatically manage roles and groups, look up users, invite candidates into assessments, retrieve candidacy statuses, code-challenge and interview results, and bulk-update candidacy dispositions. The API uses Bearer token authentication, Relay-style cursor pagination, and ships an example Python SDK and a Postman collection. Karat is SOC 2 Type II certified and certified under the EU-US, UK-US and Swiss-US Data Privacy Frameworks.
image: https://karat.com/wp-content/themes/karat/assets/img/png/logo.png
layout: provider
mcp_servers:
- description: ''
  name: Karat MCP Server
  slug: karat-mcp-server
modified: '2026-07-19'
name: Karat
nav: Providers
network: true
overview: 'Karat publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Technical Interviewing, Hiring, Recruiting, and Talent Assessment.


  Karat''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, sandbox, and 20 more developer resources.'
random_paper: 6
score:
  band: thin
  composite: 34.8
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 31.9
    developer_ergonomics: 51.8
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 34.8
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/karat/refs/heads/main/screenshots/karat-2026-07-25T223504.png
security:
- kind: authentication
  name: Karat Authentication
  slug: karat-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Karat Domain Security
  slug: karat-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Karat Trust Center
  slug: karat-trust-center
  summary_line: SOC 2 Type II, EU-US Data Privacy Framework, UK-US Data Privacy Framework, Swiss-US Data Privacy Framework
slug: karat
tags:
- Company
- Technical Interviewing
- Hiring
- Recruiting
- Talent Assessment
- Engineering
- GraphQL
website: https://karat.com
---
