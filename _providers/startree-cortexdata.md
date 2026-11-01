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
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://broker.pinot.celpxu.cp.s7e.startree.cloud
  baseurl_source: declared
  description: The Query API API from StarTree (Cortexdata) — 1 operation(s) for query api.
  name: StarTree (Cortexdata) Query API
  slug: startree-cortexdata-query-api-api
artifact_total: 9
collections:
- collection_type: open
  name: StarTree Cloud Query Query API API
  slug: open-startree-cortexdata-query-api-api
common:
- group: commercial
  href: https://artifacts.apis.io/startree-cortexdata/plans/startree-cortexdata-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/startree-cortexdata-plans-pricing.yml
- group: company
  title: ''
  type: Blog
  url: https://startree.ai/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://startree.ai/feed/
- group: other
  href: https://artifacts.apis.io/startree-cortexdata/overlays/startree-cortexdata-query-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/startree-cortexdata-query-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/startree-cortexdata/authentication/startree-cortexdata-authentication.yml
  title: ''
  type: Authentication
  url: authentication/startree-cortexdata-authentication.yml
- group: auth
  href: https://artifacts.apis.io/startree-cortexdata/security/startree-cortexdata-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/startree-cortexdata-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://startree.ai/responsible-disclosure/
- group: auth
  href: https://artifacts.apis.io/startree-cortexdata/security/startree-cortexdata-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/startree-cortexdata-domain-security.yml
- group: build
  href: https://artifacts.apis.io/startree-cortexdata/packages/startree-cortexdata-packages.yml
  title: ''
  type: Packages
  url: packages/startree-cortexdata-packages.yml
- group: build
  href: https://artifacts.apis.io/startree-cortexdata/packages/startree-cortexdata-packages.yml
  title: ''
  type: SDKs
  url: packages/startree-cortexdata-packages.yml
- group: agent
  href: https://artifacts.apis.io/startree-cortexdata/mcp/startree-cortexdata-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/startree-cortexdata-mcp.yml
- group: agent
  href: https://artifacts.apis.io/startree-cortexdata/llms/startree-cortexdata-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/startree-cortexdata-llms.txt
- group: design
  href: https://artifacts.apis.io/startree-cortexdata/conformance/startree-cortexdata-conformance.yml
  title: ''
  type: Conformance
  url: conformance/startree-cortexdata-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.startree.ai/products/startree-cloud/
- group: design
  href: https://artifacts.apis.io/startree-cortexdata/lifecycle/startree-cortexdata-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/startree-cortexdata-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/startree-cortexdata/changelog/startree-cortexdata-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/startree-cortexdata-changelog.yml
- group: design
  href: https://artifacts.apis.io/startree-cortexdata/conventions/startree-cortexdata-conventions.yml
  title: ''
  type: Conventions
  url: conventions/startree-cortexdata-conventions.yml
- group: agent
  href: https://artifacts.apis.io/startree-cortexdata/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
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
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/startreedata
- group: operate
  title: ''
  type: Support
  url: https://support.startree.ai/
- group: company
  title: ''
  type: Blog
  url: https://startree.ai/resources/
- group: commercial
  title: ''
  type: Pricing
  url: https://startree.ai/pricing/
- group: start
  title: ''
  type: Login
  url: https://startree.cloud/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://startree.ai/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://startree.ai/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://www.startree.ai/
created: '2026-07-17'
description: StarTree is a real-time analytics company founded by the creators of Apache Pinot. Its managed StarTree Cloud platform ingests streaming and batch data (Kafka, Confluent, S3, GCS, Iceberg and more), models it, and serves sub-second, high-concurrency SQL analytics for customer-facing, agent-facing, and operational use cases via a console, client libraries, and REST APIs. StarTree Cloud runs as SaaS, BYOC, or BYOK, adds indexing, tiered storage, RBAC/SSO, and SOC 2 + ISO 27001 security, and includes the ThirdEye anomaly detection product. Authenticated with a console-issued Bearer JWT.
finops:
- has_sources: true
  method: derived
  name: Startree Cortexdata Finops
  primary_unit: production vcpu hour
  service_category: ''
  slug: startree-cortexdata-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/startree-cortexdata.png
layout: provider
mcp_servers:
- description: Open-source Model Context Protocol server for Apache Pinot / StarTree Cloud, maintained in the StarTree (startreedata) GitHub org. Lets Claude and other MCP-compatible clients query a Pinot cluster ov
  name: StarTree (Cortexdata) MCP Server
  slug: mcp-pinot
modified: '2026-10-06'
name: StarTree (Cortexdata)
nav: Providers
network: true
overview: 'StarTree (Cortexdata) publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Query API. Tagged areas include Company, AI Infrastructure, Real-Time Analytics, Apache Pinot, and OLAP.


  StarTree (Cortexdata)''s developer surface includes engineering blog, authentication, changelog, documentation, API reference, support, pricing, and 22 more developer resources.'
plans:
- name: Startree Cortexdata Plans Pricing
  plan_count: 3
  slug: startree-cortexdata-plans-pricing
random_paper: 22
score:
  band: strong
  composite: 57.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 7.9
  facets:
    access_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 47.8
    developer_ergonomics: 54.2
    discoverability: 65.0
    operational_transparency: 31.6
  previous_composite: 49.1
  provenance:
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
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/startree-cortexdata/startree-cortexdata-2026-08-17T082112.png
security:
- kind: authentication
  name: Startree Cortexdata Authentication
  slug: startree-cortexdata-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Startree Cortexdata Domain Security
  slug: startree-cortexdata-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Startree Cortexdata Vulnerability Disclosure
  slug: startree-cortexdata-vulnerability-disclosure
  summary_line: no policy recorded
skill_count: 1
skills:
- name: Run a SQL query on StarTree Cloud
  slug: startree-cortexdata-run-query
slug: startree-cortexdata
tags:
- Company
- AI Infrastructure
- Real-Time Analytics
- Apache Pinot
- OLAP
- Analytics
- Streaming Data
- Database
website: https://www.startree.ai/
---
