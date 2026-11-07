---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 52.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 36
  human_in_the_loop: 0
  name: Clarifeye Agentic Access
  operation_count: 62
  slug: clarifeye-agentic-access
  summary_line: 62 operations · 36 acting
api_count: 1
apis:
- baseURL: https://eu.app.clarifeye.ai/api/v1
  baseurl_source: declared
  description: Manage AI agent configurations
  name: Clarifeye Agent Settings API
  slug: clarifeye-agent-settings-api
- baseURL: https://eu.app.clarifeye.ai/api/v1
  baseurl_source: declared
  description: Create and interact with AI-powered conversations
  name: Clarifeye Conversations API
  slug: clarifeye-conversations-api
- baseURL: https://eu.app.clarifeye.ai/api/v1
  baseurl_source: declared
  description: Manage documents within a project
  name: Clarifeye Documents API
  slug: clarifeye-documents-api
- baseURL: https://eu.app.clarifeye.ai/api/v1
  baseurl_source: declared
  description: Manage extraction flows (auto-sync DAGs) — list, run, inspect statistics, update, and publish
  name: Clarifeye Extraction Flows API
  slug: clarifeye-extraction-flows-api
- baseURL: https://eu.app.clarifeye.ai/api/v1
  baseurl_source: declared
  description: Submit feedback on conversation messages
  name: Clarifeye Feedback API
  slug: clarifeye-feedback-api
- baseURL: https://eu.app.clarifeye.ai/api/v1
  baseurl_source: declared
  description: Assign and review structured interview conversations
  name: Clarifeye Interviews API
  slug: clarifeye-interviews-api
- baseURL: https://eu.app.clarifeye.ai/api/v1
  baseurl_source: declared
  description: Manage project invitations
  name: Clarifeye Invitations API
  slug: clarifeye-invitations-api
- baseURL: https://eu.app.clarifeye.ai/api/v1
  baseurl_source: declared
  description: Manage project-scoped notifications for users
  name: Clarifeye Notifications API
  slug: clarifeye-notifications-api
- baseURL: https://eu.app.clarifeye.ai/api/v1
  baseurl_source: declared
  description: Inspect pipeline runs queued by extraction flows or other pipeline triggers — list runs and fetch the details/status of a single run
  name: Clarifeye Pipeline Runs API
  slug: clarifeye-pipeline-runs-api
- baseURL: https://eu.app.clarifeye.ai/api/v1
  baseurl_source: declared
  description: Perform CRUD operations on warehouse tables
  name: Clarifeye Tables API
  slug: clarifeye-tables-api
- baseURL: https://eu.app.clarifeye.ai/api/v1
  baseurl_source: declared
  description: Execute configured AI tools with custom parameters
  name: Clarifeye Tools API
  slug: clarifeye-tools-api
- baseURL: https://eu.app.clarifeye.ai/api/v1
  baseurl_source: declared
  description: Manage users within a project
  name: Clarifeye Users API
  slug: clarifeye-users-api
- baseURL: https://eu.app.clarifeye.ai/api/v1
  baseurl_source: declared
  description: 'Knowledge-store artifact catalog — list artifacts, create/edit custom artifacts, manage scope membership, read and publish versions, configure the cohesion guide, and export/import the whole catalog. '
  name: Clarifeye Artifacts API
  slug: clarifeye-artifacts-api
- baseURL: https://eu.app.clarifeye.ai/api/v1
  baseurl_source: declared
  description: Restrict a downstream pipeline branch to chunks carrying specific tags. Update auto-creates a new version when the filter changes.
  name: Clarifeye Chunk Tag Filter Extractors API
  slug: clarifeye-chunk-tag-filter-extractors-api
- baseURL: https://eu.app.clarifeye.ai/api/v1
  baseurl_source: declared
  description: The Chunks API from Clarifeye — 1 operation(s) for chunks.
  name: Clarifeye Chunks API
  slug: clarifeye-chunks-api
- baseURL: https://eu.app.clarifeye.ai/api/v1
  baseurl_source: declared
  description: Segment parsed documents into chunks for downstream processing. Update auto-creates a new `ChunksExtractorVersion` when version-bearing fields change.
  name: Clarifeye Chunks Extractors API
  slug: clarifeye-chunks-extractors-api
- baseURL: https://eu.app.clarifeye.ai/api/v1
  baseurl_source: declared
  description: The Connectors API from Clarifeye — 3 operation(s) for connectors.
  name: Clarifeye Connectors API
  slug: clarifeye-connectors-api
- baseURL: https://eu.app.clarifeye.ai/api/v1
  baseurl_source: declared
  description: Reference/example files attached to a design template.
  name: Clarifeye Design System Templates API
  slug: clarifeye-design-system-templates-api
- baseURL: https://eu.app.clarifeye.ai/api/v1
  baseurl_source: declared
  description: Restrict a downstream pipeline branch to documents matching a filter. Update auto-creates a new version when the filter changes.
  name: Clarifeye Document Filter Extractors API
  slug: clarifeye-document-filter-extractors-api
- baseURL: https://eu.app.clarifeye.ai/api/v1
  baseurl_source: declared
  description: Apply a flat set of metadata tags to each document. Update auto-creates a new version when version-bearing fields change.
  name: Clarifeye Document Tag Extractors API
  slug: clarifeye-document-tag-extractors-api
- baseURL: https://eu.app.clarifeye.ai/api/v1
  baseurl_source: declared
  description: The External MCP API from Clarifeye — 9 operation(s) for external mcp.
  name: Clarifeye External MCP API
  slug: clarifeye-external-mcp-api
- baseURL: https://eu.app.clarifeye.ai/api/v1
  baseurl_source: declared
  description: Hold objects imported from an external system (rather than extracted by an LLM). Useful for hydrating the warehouse with data produced outside the platform.
  name: Clarifeye Imported Object Extractors API
  slug: clarifeye-imported-object-extractors-api
- baseURL: https://eu.app.clarifeye.ai/api/v1
  baseurl_source: declared
  description: Meetings Clara attends as a bot (Recall.ai) — live transcript, live insights, recording, and calendar scheduling (CLA-1843). Store admins only.
  name: Clarifeye Meetings API
  slug: clarifeye-meetings-api
- baseURL: https://eu.app.clarifeye.ai/api/v1
  baseurl_source: declared
  description: Run LLM-based alerts over already-extracted object rows. Update auto-creates a new version when version-bearing fields change.
  name: Clarifeye Object Alerts Extractors API
  slug: clarifeye-object-alerts-extractors-api
- baseURL: https://eu.app.clarifeye.ai/api/v1
  baseurl_source: declared
  description: Extract structured data (instances of a Pydantic model) from chunks or blocks of documents. Update auto-creates a new `ObjectExtractorVersion` when version-bearing fields change.
  name: Clarifeye Object Extractors API
  slug: clarifeye-object-extractors-api
- baseURL: https://eu.app.clarifeye.ai/api/v1
  baseurl_source: declared
  description: Superuser management of org-scoped provisioning API keys. Minting and revoking are superuser-only; org admins can list/retrieve/reveal their own org's keys.
  name: Clarifeye Organization API Keys API
  slug: clarifeye-organization-api-keys-api
- baseURL: https://eu.app.clarifeye.ai/api/v1
  baseurl_source: declared
  description: Convert source documents to text blocks via the parsing pipeline. Update auto-creates a new `ParsingExtractorVersion` when version-bearing fields change.
  name: Clarifeye Parsing Extractors API
  slug: clarifeye-parsing-extractors-api
- baseURL: https://eu.app.clarifeye.ai/api/v1
  baseurl_source: declared
  description: The Projects API from Clarifeye — 10 operation(s) for projects.
  name: Clarifeye Projects API
  slug: clarifeye-projects-api
- baseURL: https://eu.app.clarifeye.ai/api/v1
  baseurl_source: declared
  description: The Service Accounts API from Clarifeye — 5 operation(s) for service accounts.
  name: Clarifeye Service Accounts API
  slug: clarifeye-service-accounts-api
- baseURL: https://eu.app.clarifeye.ai/api/v1
  baseurl_source: declared
  description: Run LLM-based alerts over already-extracted tag rows. Update auto-creates a new version when version-bearing fields change.
  name: Clarifeye Tag Alerts Extractors API
  slug: clarifeye-tag-alerts-extractors-api
- baseURL: https://eu.app.clarifeye.ai/api/v1
  baseurl_source: declared
  description: Apply hierarchical metadata tags to chunks or documents using an LLM. Update auto-creates a new `TagExtractorVersion` when version-bearing fields change.
  name: Clarifeye Tag Extractors API
  slug: clarifeye-tag-extractors-api
- baseURL: https://eu.app.clarifeye.ai/api/v1
  baseurl_source: declared
  description: 'Pre-create and de-provision org users via an org-scoped API key (`Authorization: Bearer <key>`). The organization is resolved from the key.'
  name: Clarifeye User Provisioning API
  slug: clarifeye-user-provisioning-api
artifact_total: 57
collections:
- collection_type: open
  name: Clarifeye Platform Agent Settings API
  slug: open-clarifeye-agent-settings-api
- collection_type: open
  name: Clarifeye Platform Agent Settings Conversations API
  slug: open-clarifeye-conversations-api
- collection_type: open
  name: Clarifeye Platform Agent Settings Documents API
  slug: open-clarifeye-documents-api
- collection_type: open
  name: Clarifeye Platform Agent Settings Extraction Flows API
  slug: open-clarifeye-extraction-flows-api
- collection_type: open
  name: Clarifeye Platform Agent Settings Feedback API
  slug: open-clarifeye-feedback-api
- collection_type: open
  name: Clarifeye Platform Agent Settings Interviews API
  slug: open-clarifeye-interviews-api
- collection_type: open
  name: Clarifeye Platform Agent Settings Invitations API
  slug: open-clarifeye-invitations-api
- collection_type: open
  name: Clarifeye Platform Agent Settings Notifications API
  slug: open-clarifeye-notifications-api
- collection_type: open
  name: Clarifeye Platform Agent Settings Pipeline Runs API
  slug: open-clarifeye-pipeline-runs-api
- collection_type: open
  name: Clarifeye Platform Agent Settings Signals API
  slug: open-clarifeye-signals-api
- collection_type: open
  name: Clarifeye Platform Agent Settings Tables API
  slug: open-clarifeye-tables-api
- collection_type: open
  name: Clarifeye Platform Agent Settings Tools API
  slug: open-clarifeye-tools-api
- collection_type: open
  name: Clarifeye Platform Agent Settings Users API
  slug: open-clarifeye-users-api
common:
- group: commercial
  href: https://artifacts.apis.io/clarifeye/plans/clarifeye-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/clarifeye-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/clarifeye/capabilities/clarifeye-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/clarifeye-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/clarifeye/overlays/clarifeye-backoffice-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/clarifeye-backoffice-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.clarifeye.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.clarifeye.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.clarifeye.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.clarifeye.ai/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.clarifeye.ai/guides/quickstart
- group: start
  title: ''
  type: Quickstart
  url: https://docs.clarifeye.ai/guides/quickstart
- group: company
  title: ''
  type: Blog
  url: https://www.clarifeye.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://www.clarifeye.ai/contact-us
- group: commercial
  title: ''
  type: Pricing
  url: https://www.clarifeye.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://us.app.clarifeye.ai/
- group: start
  title: ''
  type: Login
  url: https://us.app.clarifeye.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.clarifeye.ai/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.clarifeye.ai/legal/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/clarifeyeai/
- group: auth
  title: ''
  type: Compliance
  url: https://www.clarifeye.ai/technology
- group: agent
  href: https://artifacts.apis.io/clarifeye/mcp/clarifeye-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/clarifeye-mcp.yml
- group: agent
  href: https://artifacts.apis.io/clarifeye/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/clarifeye/authentication/clarifeye-authentication.yml
  title: ''
  type: Authentication
  url: authentication/clarifeye-authentication.yml
- group: auth
  href: https://artifacts.apis.io/clarifeye/scopes/clarifeye-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/clarifeye-scopes.yml
- group: agent
  href: https://artifacts.apis.io/clarifeye/well-known/clarifeye-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/clarifeye-well-known.yml
- group: design
  href: https://artifacts.apis.io/clarifeye/errors/clarifeye-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/clarifeye-problem-types.yml
- group: design
  href: https://artifacts.apis.io/clarifeye/conventions/clarifeye-conventions.yml
  title: ''
  type: Conventions
  url: conventions/clarifeye-conventions.yml
- group: design
  href: https://artifacts.apis.io/clarifeye/lifecycle/clarifeye-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/clarifeye-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/clarifeye/conformance/clarifeye-conformance.yml
  title: ''
  type: Conformance
  url: conformance/clarifeye-conformance.yml
- group: design
  href: https://artifacts.apis.io/clarifeye/data-model/clarifeye-data-model.yml
  title: ''
  type: DataModel
  url: data-model/clarifeye-data-model.yml
- group: agent
  href: https://artifacts.apis.io/clarifeye/llms/clarifeye-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/clarifeye-llms.txt
- group: auth
  href: https://artifacts.apis.io/clarifeye/security/clarifeye-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clarifeye-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/clarifeye/agentic-access/clarifeye-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/clarifeye-agentic-access.yml
created: '2026-07-17'
description: Clarifeye is an AI-native knowledge infrastructure platform that captures the undocumented knowledge locked in people's heads. Its AI interviewer, Clara, runs document-aware interviews with subject-matter experts, surfaces contradictions, and structures the results into versioned, reusable knowledge artifacts — briefs, playbooks, mental maps, and ontologies. That captured knowledge is exposed to AI clients such as Claude, ChatGPT, and Microsoft Copilot through a hosted Model Context Protocol (MCP) server and a REST API, so agents answer grounded in an organization's own logic with references back to source. Clarifeye targets regulated industries where undocumented processes create key-person risk, offers EU and US data localization with PII redaction at ingestion, and is SOC 2 Type II certified. Backed by EQT Ventures.
finops:
- has_sources: true
  method: derived
  name: Clarifeye Finops
  primary_unit: platform fee
  service_category: ''
  slug: clarifeye-finops
  template: false
image: https://www.clarifeye.ai/_astro/og-default.BHhQt8Bo.png
layout: provider
mcp_servers:
- description: Clarifeye publishes a hosted, per-knowledge-store MCP server that exposes an organization's captured knowledge (briefs, playbooks, mental maps, tags, objects) to AI clients (Claude, ChatGPT, Microsoft
  name: Clarifeye MCP Server
  slug: clarifeye
modified: '2026-07-18'
name: Clarifeye
nav: Providers
network: true
overview: 'Clarifeye publishes 32 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent Settings API, Conversations API, Documents API, and 29 more. Tagged areas include Company, Artificial Intelligence, Knowledge Management, MCP, and Document Intelligence.


  The Clarifeye catalog on APIs.io includes 1 Spectral governance ruleset.


  Clarifeye''s developer surface includes documentation, API reference, getting-started guide, quickstart, engineering blog, support, pricing, and 24 more developer resources.'
plans:
- name: Clarifeye Plans Pricing
  plan_count: 5
  slug: clarifeye-plans-pricing
- name: Clarifeye Price Estimates
  plan_count: 0
  slug: clarifeye-price-estimates
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 103
  extends:
  - spectral:oas
  name: Clarifeye API Rules
  rule_count: 62
  severity_counts:
    error: 45
    hint: 0
    info: 6
    warn: 11
  slug: clarifeye-rules
scopes:
- name: Clarifeye Scopes
  scope_count: 3
  slug: clarifeye-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: strong
  composite: 60.7
  coverage:
    artifact_dirs: 26
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.0
  facets:
    access_clarity: 78.9
    contract_governance: 31.8
    contract_quality: 57.3
    developer_ergonomics: 58.9
    discoverability: 75.0
    operational_transparency: 0.0
  previous_composite: 59.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 68.1
      total: 47
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 50.0
screenshot: https://apis.io/screenshots/clarifeye/clarifeye-2026-07-25T205502.png
security:
- kind: authentication
  name: Clarifeye Authentication
  slug: clarifeye-authentication
  summary_line: apiKey/http/oauth2 · 2 schemes
- kind: domain-security
  name: Clarifeye Domain Security
  slug: clarifeye-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: Ingest and manage knowledge-store documents
  slug: clarifeye-manage-documents
- name: Discover and run a knowledge-store tool
  slug: clarifeye-run-tool
- name: Submit and triage knowledge signals
  slug: clarifeye-signals-loop
slug: clarifeye
tags:
- Company
- Artificial Intelligence
- Knowledge Management
- MCP
- Document Intelligence
- Agents
- Enterprise AI
- Retrieval
website: https://www.clarifeye.ai/
---
