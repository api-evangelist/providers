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
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.3
  scored_at: '2026-10-31'
api_count: 1
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
artifact_total: 29
collections:
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
  href: https://artifacts.apis.io/opaque/mcp/opaque-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/opaque-mcp.yml
- group: auth
  href: https://artifacts.apis.io/opaque/security/opaque-domain-security.yml
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
  href: https://artifacts.apis.io/opaque/changelog/opaque-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/opaque-changelog.yml
- group: auth
  href: https://artifacts.apis.io/opaque/authentication/opaque-authentication.yml
  title: ''
  type: Authentication
  url: authentication/opaque-authentication.yml
- group: design
  href: https://artifacts.apis.io/opaque/conventions/opaque-conventions.yml
  title: ''
  type: Conventions
  url: conventions/opaque-conventions.yml
- group: design
  href: https://artifacts.apis.io/opaque/errors/opaque-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/opaque-problem-types.yml
- group: design
  href: https://artifacts.apis.io/opaque/lifecycle/opaque-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/opaque-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/opaque/conformance/opaque-conformance.yml
  title: ''
  type: Conformance
  url: conformance/opaque-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.opaque.co/resources/articles/the-opaque-platform-is-now-soc-2-certified
- group: design
  href: https://artifacts.apis.io/opaque/data-model/opaque-data-model.yml
  title: ''
  type: DataModel
  url: data-model/opaque-data-model.yml
- group: other
  href: https://artifacts.apis.io/opaque/overlays/opaque-platform-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/opaque-platform-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/opaque/llms/opaque-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/opaque-llms.txt
- group: build
  href: https://artifacts.apis.io/opaque/packages/opaque-packages.yml
  title: ''
  type: Packages
  url: packages/opaque-packages.yml
- group: agent
  href: https://artifacts.apis.io/opaque/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  href: https://artifacts.apis.io/opaque/sandbox/opaque-sandbox.yml
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
overview: 'OPAQUE publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Asset Configs API, Auth API, Datasets API, and 8 more. Tagged areas include Confidential Computing, Confidential AI, AI Governance, Privacy, and Trusted Execution Environment.


  OPAQUE''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, authentication, and 19 more developer resources.'
random_paper: 3
score:
  band: developing
  composite: 43.4
  coverage:
    artifact_dirs: 22
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 43.0
    developer_ergonomics: 66.1
    discoverability: 66.1
    operational_transparency: 21.1
  previous_composite: 43.4
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/opaque/opaque-2026-08-07T190445.png
security:
- kind: authentication
  name: Opaque Authentication
  slug: opaque-authentication
  summary_line: apiKey/http · 4 schemes
- kind: domain-security
  name: Opaque Domain Security
  slug: opaque-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 5
skills:
- name: Authenticate against the OPAQUE Platform REST API
  slug: opaque-authenticate
- name: Build, approve and launch an agentic workflow
  slug: opaque-launch-agentic-workflow
- name: Manage workspaces, members and reusable integrations
  slug: opaque-manage-workspaces-and-integrations
- name: Onboard a dataset and share it into a workspace
  slug: opaque-onboard-and-share-data
- name: Run a confidential analytics job and collect its results
  slug: opaque-run-analytics-job
slug: opaque
tags:
- Confidential Computing
- Confidential AI
- AI Governance
- Privacy
- Trusted Execution Environment
- Attestation
- Agentic Workflows
- RAG
- Enterprise AI
- secure-analytics
- Data Clean Room
- MCP
website: https://www.opaque.co/
---
