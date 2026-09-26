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
    agent_skills: derived
    agentic_access: derived
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.7
  scored_at: '2026-09-25'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Startree Agentic Access
  operation_count: 1
  slug: startree-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- baseURL: https://broker.pinot.celpxu.cp.s7e.startree.cloud
  baseurl_source: declared
  description: The Query API API from StarTree — 1 operation(s) for query api.
  name: StarTree Query API
  slug: startree-query-api-api
artifact_total: 8
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: StarTree Cloud Query Query API API
  slug: open-startree-query-api-api
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/startree/refs/heads/main/overlays/startree-query-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/startree-query-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.startree.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.startree.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.startree.ai/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.startree.ai/getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.startree.ai/
- group: company
  title: ''
  type: Blog
  url: https://startree.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/startreedata
- group: commercial
  title: ''
  type: Pricing
  url: https://startree.ai/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://startree.ai/trial/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://startree.ai/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://startree.ai/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://startree.statuspage.io
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/startree/refs/heads/main/llms/startree-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/startree-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/startree/refs/heads/main/packages/startree-packages.yml
  title: ''
  type: Packages
  url: packages/startree-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/startree/refs/heads/main/packages/startree-packages.yml
  title: ''
  type: SDKs
  url: packages/startree-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/startree/refs/heads/main/mcp/startree-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/startree-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/startree/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/startree/refs/heads/main/conventions/startree-conventions.yml
  title: ''
  type: Conventions
  url: conventions/startree-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/startree/refs/heads/main/lifecycle/startree-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/startree-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/startree/refs/heads/main/changelog/startree-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/startree-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/startree/refs/heads/main/conformance/startree-conformance.yml
  title: ''
  type: Conformance
  url: conformance/startree-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://startree.ai/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/startree/refs/heads/main/agentic-access/startree-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/startree-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/startree/refs/heads/main/security/startree-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/startree-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://startree.ai/responsible-disclosure/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/startree/refs/heads/main/security/startree-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/startree-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/startree/refs/heads/main/authentication/startree-authentication.yml
  title: ''
  type: Authentication
  url: authentication/startree-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://startree.ai/
created: '2026-07-17'
description: StarTree is a real-time analytics platform built on Apache Pinot, the open-source OLAP database for user-facing and agent-facing analytics. StarTree Cloud is the fully managed, enterprise-grade service — sub-second queries at high concurrency, streaming and batch ingestion up to millions of events per second, scalable upserts, in-place queries on Apache Iceberg tables, and ThirdEye anomaly detection. It ships enterprise security (RBAC, SSO, encryption, SOC 2 / ISO 27001 / HIPAA) with SaaS, BYOC, and BYOK deployment options, and exposes Controller, Broker, and Query REST APIs plus an official MCP server for agents.
image: https://startree.ai/favicon.ico
layout: provider
mcp_servers:
- description: Official StarTree MCP server for Apache Pinot. Lets an agent list tables, segments, and schema info and execute read-only SQL queries against a Pinot / StarTree Cloud cluster.
  name: StarTree MCP Server
  slug: startree-mcp-server
modified: '2026-09-16'
name: StarTree
nav: Providers
network: true
overview: 'StarTree publishes 1 API on the [APIs.io](https://apis.io/) network: Query API. Tagged areas include Company, Data, Analytics, Real-Time Analytics, and OLAP.


  StarTree''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 22 more developer resources.'
random_paper: 16
score:
  band: developing
  composite: 49.8
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.2
  facets:
    access_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 47.8
    developer_ergonomics: 49.4
    discoverability: 71.7
    operational_transparency: 44.7
  previous_composite: 48.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/startree/refs/heads/main/screenshots/startree-2026-08-17T082113.png
security:
- kind: authentication
  name: Startree Authentication
  slug: startree-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Startree Domain Security
  slug: startree-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Startree Vulnerability Disclosure
  slug: startree-vulnerability-disclosure
  summary_line: disclosure policy published
slug: startree
tags:
- Company
- Data
- Analytics
- Real-Time Analytics
- OLAP
- Apache Pinot
- Streaming
- Database
website: https://startree.ai/
---
