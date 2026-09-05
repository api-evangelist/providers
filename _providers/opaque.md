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
  - sandbox
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.4
  scored_at: '2026-09-04'
api_count: 2
apis:
- baseURL: https://api.<your-subdomain>/v2.5
  baseurl_source: declared
  description: Asset Configurations
  name: OPAQUE Asset Configs API
  slug: opaque-asset-configs-api
- baseURL: https://api.<your-subdomain>/v2.5
  baseurl_source: declared
  description: Authentication
  name: OPAQUE Auth API
  slug: opaque-auth-api
- baseURL: https://api.<your-subdomain>/v2.5
  baseurl_source: declared
  description: Data & Datum
  name: OPAQUE Datasets API
  slug: opaque-datasets-api
- baseURL: https://api.<your-subdomain>/v2.5
  baseurl_source: declared
  description: Jobs
  name: OPAQUE Jobs API
  slug: opaque-jobs-api
- baseURL: https://api.<your-subdomain>/v2.5
  baseurl_source: declared
  description: The organizations API from OPAQUE — 4 operation(s) for organizations.
  name: OPAQUE Organizations API
  slug: opaque-organizations-api
- baseURL: https://api.<your-subdomain>/v2.5
  baseurl_source: declared
  description: The pinned-queries API from OPAQUE — 3 operation(s) for pinned-queries.
  name: OPAQUE Pinned Queries API
  slug: opaque-pinned-queries-api
- baseURL: https://api.<your-subdomain>/v2.5
  baseurl_source: declared
  description: The predefined-query-templates API from OPAQUE — 3 operation(s) for predefined-query-templates.
  name: OPAQUE Predefined Query Templates API
  slug: opaque-predefined-query-templates-api
- baseURL: https://api.<your-subdomain>/v2.5
  baseurl_source: declared
  description: Users
  name: OPAQUE Users API
  slug: opaque-users-api
- baseURL: https://api.<your-subdomain>/v2.5
  baseurl_source: declared
  description: The versioning API from OPAQUE — 1 operation(s) for versioning.
  name: OPAQUE Versioning API
  slug: opaque-versioning-api
- baseURL: https://api.<your-subdomain>/v2.5
  baseurl_source: declared
  description: The workflows API from OPAQUE — 9 operation(s) for workflows.
  name: OPAQUE Workflows API
  slug: opaque-workflows-api
- baseURL: https://api.<your-subdomain>/v2.5
  baseurl_source: declared
  description: Workspaces
  name: OPAQUE Workspaces API
  slug: opaque-workspaces-api
artifact_total: 25
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Opaque UI Asset Configs API
  slug: open-opaque-asset-configs-api
- collection_type: open
  name: Opaque UI Auth API
  slug: open-opaque-auth-api
- collection_type: open
  name: Opaque UI Datasets API
  slug: open-opaque-datasets-api
- collection_type: open
  name: Opaque UI Jobs API
  slug: open-opaque-jobs-api
- collection_type: open
  name: Opaque UI Organizations API
  slug: open-opaque-organizations-api
- collection_type: open
  name: Opaque UI Pinned Queries API
  slug: open-opaque-pinned-queries-api
- collection_type: open
  name: Opaque UI Predefined Query Templates API
  slug: open-opaque-predefined-query-templates-api
- collection_type: open
  name: Opaque UI Users API
  slug: open-opaque-users-api
- collection_type: open
  name: Opaque UI Versioning API
  slug: open-opaque-versioning-api
- collection_type: open
  name: Opaque UI Workflows API
  slug: open-opaque-workflows-api
- collection_type: open
  name: Opaque UI Workspaces API
  slug: open-opaque-workspaces-api
common:
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/opaque-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/opaque-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.opaque.co/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.opaque.co/en/latest/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.opaque.co/en/latest/public_guide/developers/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.opaque.co/en/latest/api_reference/rest_api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.opaque.co/en/latest/public_guide/users/get_started/
- group: operate
  title: ''
  type: Support
  url: https://docs.opaque.co/en/latest/support/
- group: company
  title: ''
  type: Blog
  url: https://www.opaque.co/resources
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/opaque-systems
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.opaque.co/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.opaque.co/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.opaque.co/en/latest/release_notes/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/opaque-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/opaque-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/opaque-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/opaque-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/opaque-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/opaque-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.opaque.co/resources/articles/the-opaque-platform-is-now-soc-2-certified
- group: design
  title: ''
  type: DataModel
  url: data-model/opaque-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/opaque-platform-api-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/opaque-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/opaque-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/opaque-sandbox.yml
created: '2026-08-04'
description: 'OPAQUE Systems, Inc. is a confidential-AI platform company that lets enterprises run AI and analytics on their most sensitive data without exposing it. The OPAQUE Confidential AI Platform executes agentic workflows, retrieval-augmented generation, and analytics jobs inside hardware trusted execution environments (TEEs), with attested TLS between components, signed attestation reports, and tamper-evident audit logs so every run can be independently verified. It is deployed in a hybrid architecture: an OPAQUE-hosted control plane manages users, workspaces, job metadata, notifications, audit logging, and key management, while the data plane, client/API pod, and encrypted storage all run inside the customer''s own cloud environment. The platform exposes a documented REST API (workspaces, datasets, jobs, workflows, asset configs, users, organizations) described by an OpenAPI 3.0.3 specification, plus a Python SDK for invoking deployed workflows. It is used in insurance, financial
  services, and high-tech for confidential RAG, secure multi-party analytics, and governed agent execution.'
image: https://cdn.prod.website-files.com/66d977be14c1ef2f8e88c93c/68cb38f2400045b985a92458_Opaque%20Logo.svg
layout: provider
modified: '2026-08-04'
name: OPAQUE
nav: Providers
network: true
overview: 'OPAQUE publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Asset Configs API, Auth API, Datasets API, and 8 more. Tagged areas include Confidential Computing, confidential-ai, AI Governance, Data Privacy, and Trusted Execution Environment.


  OPAQUE''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, authentication, and 19 more developer resources.'
random_paper: 0
score:
  band: developing
  composite: 42.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 47.8
    developer_ergonomics: 66.1
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 42.4
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/opaque/refs/heads/main/screenshots/opaque-2026-08-07T190445.png
security:
- kind: authentication
  name: Opaque Authentication
  slug: opaque-authentication
  summary_line: apiKey/http · 4 schemes
- kind: domain-security
  name: Opaque Domain Security
  slug: opaque-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: opaque
tags:
- Confidential Computing
- confidential-ai
- AI Governance
- Data Privacy
- Trusted Execution Environment
- Attestation
- Agentic Workflows
- Retrieval Augmented Generation
- Enterprise AI
- secure-analytics
- Data Clean Room
- MCP
website: https://www.opaque.co/
---
