---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.2
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Provider-published Model Context Protocol server ("governance-hub") distributed as the npm package @credoai/governance-hub-mcp and run over stdio via npx. Grounds the Credo AI Claude Code Agent Skills
  name: Credo AI Governance Intelligence Pro MCP Server
  slug: credo-ai-governance-intelligence-pro-mcp-server
- baseURL: https://api.credo.ai/api/v2/{tenant}
  baseurl_source: declared
  description: The alerts API from Credo AI — 4 operation(s) for alerts.
  name: Credo AI Alerts API
  slug: credo-ai-alerts-api
- baseURL: https://api.credo.ai/api/v2/{tenant}
  baseurl_source: declared
  description: The Audit Logs API from Credo AI — 4 operation(s) for audit logs.
  name: Credo AI Audit Logs API
  slug: credo-ai-audit-logs-api
- baseURL: https://api.credo.ai/api/v2/{tenant}
  baseurl_source: declared
  description: The comment_threads API from Credo AI — 4 operation(s) for comment_threads.
  name: Credo AI Comment Threads API
  slug: credo-ai-comment-threads-api
- baseURL: https://api.credo.ai/api/v2/{tenant}
  baseurl_source: declared
  description: The entities API from Credo AI — 1 operation(s) for entities.
  name: Credo AI Entities API
  slug: credo-ai-entities-api
- baseURL: https://api.credo.ai/api/v2/{tenant}
  baseurl_source: declared
  description: The entity_control_assignments API from Credo AI — 1 operation(s) for entity_control_assignments.
  name: Credo AI Entity Control Assignments API
  slug: credo-ai-entity-control-assignments-api
- baseURL: https://api.credo.ai/api/v2/{tenant}
  baseurl_source: declared
  description: The entity_controls API from Credo AI — 7 operation(s) for entity_controls.
  name: Credo AI Entity Controls API
  slug: credo-ai-entity-controls-api
- baseURL: https://api.credo.ai/api/v2/{tenant}
  baseurl_source: declared
  description: The entity_evidences API from Credo AI — 1 operation(s) for entity_evidences.
  name: Credo AI Entity Evidences API
  slug: credo-ai-entity-evidences-api
- baseURL: https://api.credo.ai/api/v2/{tenant}
  baseurl_source: declared
  description: The entity_policy_packs API from Credo AI — 2 operation(s) for entity_policy_packs.
  name: Credo AI Entity Policy Packs API
  slug: credo-ai-entity-policy-packs-api
- baseURL: https://api.credo.ai/api/v2/{tenant}
  baseurl_source: declared
  description: The entity_risk_scenario_controls API from Credo AI — 3 operation(s) for entity_risk_scenario_controls.
  name: Credo AI Entity Risk Scenario Controls API
  slug: credo-ai-entity-risk-scenario-controls-api
- baseURL: https://api.credo.ai/api/v2/{tenant}
  baseurl_source: declared
  description: The entity_risk_scenarios API from Credo AI — 2 operation(s) for entity_risk_scenarios.
  name: Credo AI Entity Risk Scenarios API
  slug: credo-ai-entity-risk-scenarios-api
- baseURL: https://api.credo.ai/api/v2/{tenant}
  baseurl_source: declared
  description: The entity_section_assignments API from Credo AI — 1 operation(s) for entity_section_assignments.
  name: Credo AI Entity Section Assignments API
  slug: credo-ai-entity-section-assignments-api
- baseURL: https://api.credo.ai/api/v2/{tenant}
  baseurl_source: declared
  description: The entity_types API from Credo AI — 1 operation(s) for entity_types.
  name: Credo AI Entity Types API
  slug: credo-ai-entity-types-api
- baseURL: https://api.credo.ai/api/v2/{tenant}
  baseurl_source: declared
  description: Operations related to custom fields management
  name: Credo AI Fields API
  slug: credo-ai-fields-api
- baseURL: https://api.credo.ai/api/v2/{tenant}
  baseurl_source: declared
  description: The integrations API from Credo AI — 4 operation(s) for integrations.
  name: Credo AI Integrations API
  slug: credo-ai-integrations-api
- baseURL: https://api.credo.ai/api/v2/{tenant}
  baseurl_source: declared
  description: Operations related to models and model versions
  name: Credo AI Models API
  slug: credo-ai-models-api
- baseURL: https://api.credo.ai/api/v2/{tenant}
  baseurl_source: declared
  description: Utility endpoints including tenant information and evidence types
  name: Credo AI Other API
  slug: credo-ai-other-api
- baseURL: https://api.credo.ai/api/v2/{tenant}
  baseurl_source: declared
  description: Endpoints for policy controls management
  name: Credo AI Policy Controls API
  slug: credo-ai-policy-controls-api
- baseURL: https://api.credo.ai/api/v2/{tenant}
  baseurl_source: declared
  description: Endpoints for policy packs management
  name: Credo AI Policy Packs API
  slug: credo-ai-policy-packs-api
- baseURL: https://api.credo.ai/api/v2/{tenant}
  baseurl_source: declared
  description: Operations related to questionnaires and their versions
  name: Credo AI Questionnaires API
  slug: credo-ai-questionnaires-api
- baseURL: https://api.credo.ai/api/v2/{tenant}
  baseurl_source: declared
  description: Endpoints for management of risk classifications, risk types, and risk scenarios
  name: Credo AI Risks API
  slug: credo-ai-risks-api
- baseURL: https://api.credo.ai/api/v2/{tenant}
  baseurl_source: declared
  description: The Shadow AI API from Credo AI — 6 operation(s) for shadow ai.
  name: Credo AI Shadow AI API
  slug: credo-ai-shadow-ai-api
- baseURL: https://api.credo.ai/api/v2/{tenant}
  baseurl_source: declared
  description: The sources API from Credo AI — 3 operation(s) for sources.
  name: Credo AI Sources API
  slug: credo-ai-sources-api
- baseURL: https://api.credo.ai/api/v2/{tenant}
  baseurl_source: declared
  description: Operations related to task management
  name: Credo AI Tasks API
  slug: credo-ai-tasks-api
- baseURL: https://api.credo.ai/api/v2/{tenant}
  baseurl_source: declared
  description: Operations related to team management and memberships
  name: Credo AI Teams API
  slug: credo-ai-teams-api
- baseURL: https://api.credo.ai/api/v2/{tenant}
  baseurl_source: declared
  description: Endpoints for managing triggers and actions
  name: Credo AI Triggers And Actions API
  slug: credo-ai-triggers-and-actions-api
- baseURL: https://api.credo.ai/api/v2/{tenant}
  baseurl_source: declared
  description: The use_case API from Credo AI — 1 operation(s) for use_case.
  name: Credo AI Use Case API
  slug: credo-ai-use-case-api
- baseURL: https://api.credo.ai/api/v2/{tenant}
  baseurl_source: declared
  description: Operations related to controls for a specific use case
  name: Credo AI Use Case Controls API
  slug: credo-ai-use-case-controls-api
- baseURL: https://api.credo.ai/api/v2/{tenant}
  baseurl_source: declared
  description: Operations related to use case custom fields
  name: Credo AI Use Case Custom Fields API
  slug: credo-ai-use-case-custom-fields-api
- baseURL: https://api.credo.ai/api/v2/{tenant}
  baseurl_source: declared
  description: Operations related to policy packs for a specific use case
  name: Credo AI Use Case Policy Packs API
  slug: credo-ai-use-case-policy-packs-api
- baseURL: https://api.credo.ai/api/v2/{tenant}
  baseurl_source: declared
  description: Operations related to questionnaires, questionnaire sections, and questionnaire evidence for a specific use case
  name: Credo AI Use Case Questionnaires API
  slug: credo-ai-use-case-questionnaires-api
- baseURL: https://api.credo.ai/api/v2/{tenant}
  baseurl_source: declared
  description: Operations related to reports for a specific use case, including creation, retrieval, and management of attestation requests
  name: Credo AI Use Case Reports API
  slug: credo-ai-use-case-reports-api
- baseURL: https://api.credo.ai/api/v2/{tenant}
  baseurl_source: declared
  description: Operations related to use case reviews, review actions, tasks and attestations
  name: Credo AI Use Case Reviews API
  slug: credo-ai-use-case-reviews-api
- baseURL: https://api.credo.ai/api/v2/{tenant}
  baseurl_source: declared
  description: Operations related to risk scenarios for a specific use case
  name: Credo AI Use Case Risk Scenarios API
  slug: credo-ai-use-case-risk-scenarios-api
- baseURL: https://api.credo.ai/api/v2/{tenant}
  baseurl_source: declared
  description: The use_case_scheduled_reviews API from Credo AI — 2 operation(s) for use_case_scheduled_reviews.
  name: Credo AI Use Case Scheduled Reviews API
  slug: credo-ai-use-case-scheduled-reviews-api
- baseURL: https://api.credo.ai/api/v2/{tenant}
  baseurl_source: declared
  description: Operations related to use cases
  name: Credo AI Use Cases API
  slug: credo-ai-use-cases-api
- baseURL: https://api.credo.ai/api/v2/{tenant}
  baseurl_source: declared
  description: Endpoints related to user preferences and settings
  name: Credo AI User API
  slug: credo-ai-user-api
- baseURL: https://api.credo.ai/api/v2/{tenant}
  baseurl_source: declared
  description: Endpoints for user management, roles, and profiles
  name: Credo AI Users API
  slug: credo-ai-users-api
- baseURL: https://api.credo.ai/api/v2/{tenant}
  baseurl_source: declared
  description: Operations related to vendors and their questionnaires
  name: Credo AI Vendors API
  slug: credo-ai-vendors-api
- baseURL: https://api.credo.ai/api/v2/{tenant}
  baseurl_source: declared
  description: The workflow_stages API from Credo AI — 2 operation(s) for workflow_stages.
  name: Credo AI Workflow Stages API
  slug: credo-ai-workflow-stages-api
- baseURL: npx -y @credoai/governance-hub-mcp
  baseurl_source: declared
  description: The relationship_types API from Credo AI — 2 operation(s) for relationship_types.
  name: Credo AI Relationship Types API
  slug: credo-ai-relationship-types-api
artifact_total: 62
collections:
- collection_type: open
  name: Credo AI API
  slug: open-credo-ai-audit-logs-shadow-ai
- collection_type: open
  name: Credo AI server API
  slug: open-credo-ai-governance-platform-swagger
common:
- group: other
  href: https://artifacts.apis.io/credo-ai/capabilities/credo-ai-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/credo-ai-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/credo-ai/overlays/credo-ai-governance-platform-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/credo-ai-governance-platform-overlay.yaml
- group: other
  href: https://artifacts.apis.io/credo-ai/overlays/credo-ai-audit-logs-shadow-ai-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/credo-ai-audit-logs-shadow-ai-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/credo-ai/security/credo-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/credo-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.credo.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.sdk.credo.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sdk.credo.ai/docs/intro/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.sdk.credo.ai/docs/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.sdk.credo.ai/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://www.credo.ai/contact
- group: company
  title: ''
  type: Blog
  url: https://www.credo.ai/resources
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/credo-ai
- group: start
  title: ''
  type: SignUp
  url: https://www.credo.ai/get-started
- group: start
  title: ''
  type: Login
  url: https://app.credo.ai/
- group: commercial
  href: https://artifacts.apis.io/credo-ai/plans/credo-ai-plans-pricing.yml
  title: ''
  type: Pricing
  url: plans/credo-ai-plans-pricing.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.credo.ai/legal/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.credo.ai/legal/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://www.credo.ai/legal/vulnerability-disclosure-policy
- group: auth
  href: https://artifacts.apis.io/credo-ai/security/credo-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/credo-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/credo-ai/security/credo-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/credo-ai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/credo-ai/conformance/credo-ai-conformance.yml
  title: ''
  type: Compliance
  url: conformance/credo-ai-conformance.yml
- group: design
  href: https://artifacts.apis.io/credo-ai/conformance/credo-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/credo-ai-conformance.yml
- group: build
  href: https://artifacts.apis.io/credo-ai/packages/credo-ai-packages.yml
  title: ''
  type: Packages
  url: packages/credo-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/credo-ai/packages/credo-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/credo-ai-packages.yml
- group: agent
  href: https://artifacts.apis.io/credo-ai/llms/credo-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/credo-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/credo-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/credo-ai/lifecycle/credo-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/credo-ai-lifecycle.yml
- group: commercial
  href: https://artifacts.apis.io/credo-ai/plans/credo-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/credo-ai-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/credo-ai/rate-limits/credo-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/credo-ai-rate-limits.yml
created: '2026-08-11'
description: Credo AI is an enterprise AI governance, risk, and compliance platform used to discover, register, risk-classify, and continuously govern every AI model, application, agent, and third-party AI vendor an organization runs. The platform pairs an AI Registry (use cases, models, vendors, agents, shadow-AI discovery) with a policy engine that turns regulatory frameworks — the EU AI Act, NIST AI RMF, ISO/IEC 42001, NYC Local Law 144, Colorado SB21-169, OMB M-25 — into machine-enforced policy packs, controls, questionnaires, risk scenarios, and audit-ready evidence artifacts. Programmatic access is delivered through a multi-tenant JSON:API REST surface at api.credo.ai (300 operations across use cases, models, vendors, questionnaires, policy packs, policy controls, risks, tasks, teams, users, triggers, and Shadow AI), a first-party Python SDK (pycredoai) and TypeScript SDK (@credo-ai/sdk), and a published Claude Code plugin marketplace of eleven AI-governance Agent Skills backed by
  a gated Governance Intelligence Pro MCP server.
finops:
- has_sources: true
  method: derived
  name: Credo Ai Finops
  primary_unit: ''
  service_category: ''
  slug: credo-ai-finops
  template: true
image: https://cdn.prod.website-files.com/649d808ba8385965c74d94df/6a27d15ec3da571348386f01_OPENGRAPGH-light.png
layout: provider
mcp_servers:
- description: Local (stdio) MCP server; 5 tools listed.
  name: Credo AI MCP Server
  slug: governance-hub
modified: '2026-08-11'
name: Credo AI
nav: Providers
network: true
overview: 'Credo AI publishes 41 API contracts indexed on the [APIs.io](https://apis.io/) network, including Alerts API, Audit Logs API, Comment Threads API, and 38 more. Tagged areas include Company, AI Governance, ai-risk-management, Responsible AI, and Compliance.


  Credo AI''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, pricing, and 22 more developer resources.'
plans:
- name: Credo Ai Plans Pricing
  plan_count: 0
  slug: credo-ai-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Credo Ai Rate Limits
  slug: credo-ai-rate-limits
score:
  band: developing
  composite: 52.1
  coverage:
    artifact_dirs: 23
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.5
  facets:
    access_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 47.7
    developer_ergonomics: 71.4
    discoverability: 65.0
    operational_transparency: 15.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 52.6
  provenance:
    conformance: first-party
    contracts:
      callable: 2.6
      derived: 0
      marker_coverage: 0.0
      total: 77
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/credo-ai/credo-ai-2026-08-17T080838.png
security:
- kind: authentication
  name: Credo Ai Authentication
  slug: credo-ai-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Credo Ai Domain Security
  slug: credo-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Credo Ai Vulnerability Disclosure
  slug: credo-ai-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Credo Ai Trust Center
  slug: credo-ai-trust-center
  summary_line: SOC 2 Type II
skill_count: 11
skills:
- name: aigov-audit-viz
  slug: credo-ai-aigov-audit-viz
- name: aigov-audit
  slug: credo-ai-aigov-audit
- name: aigov-evidence
  slug: credo-ai-aigov-evidence
- name: aigov-intake
  slug: credo-ai-aigov-intake
- name: aigov-maturity-viz
  slug: credo-ai-aigov-maturity-viz
- name: aigov-maturity
  slug: credo-ai-aigov-maturity
- name: aigov-onboarding
  slug: credo-ai-aigov-onboarding
- name: aigov-plan-viz
  slug: credo-ai-aigov-plan-viz
- name: aigov-plan
  slug: credo-ai-aigov-plan
- name: aigov-registry
  slug: credo-ai-aigov-registry
- name: aigov-share
  slug: credo-ai-aigov-share
slug: credo-ai
tags:
- Company
- AI Governance
- ai-risk-management
- Responsible AI
- Compliance
- RegTech
- Model Registry
- Vendor Risk
- EU AI Act
- NIST AI RMF
- ISO 42001
- Shadow AI
- Agent Governance
- Audit
- JSON:API
- Agent Skills
website: https://www.credo.ai/
---
