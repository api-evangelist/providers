---
agent_readiness:
  band: agent-native
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
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.1
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 182
  human_in_the_loop: 32
  name: Axonflow Agentic Access
  operation_count: 369
  slug: axonflow-agentic-access
  summary_line: 369 operations · 182 acting · 32 human-in-the-loop
api_count: 8
apis:
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: Agent configuration management (MAP 0.8). **Enterprise only** — the `/api/v1/agents` route family is registered only in Enterprise builds with a database connection; Community returns 404.
  name: AxonFlow Agents API
  slug: axonflow-agents-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: FEAT Assessment lifecycle
  name: AxonFlow Assessments API
  slug: axonflow-assessments-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: Audit log search and retrieval
  name: AxonFlow Audit API
  slug: axonflow-audit-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: Non-repudiation verification of the signed decision chain (#2722). Read-only endpoints that re-verify per-record Ed25519 signatures and the prev_hash linkage of a tenant's decision records, and publis
  name: AxonFlow Audit Verification API
  slug: axonflow-audit-verification-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: Import and export policies
  name: AxonFlow Bulk Operations API
  slug: axonflow-bulk-operations-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: Emergency circuit breaker for AI operations (EU AI Act Article 14). Instantly halt AI operations with two-person deactivation requirement.
  name: AxonFlow Circuit Breaker API
  slug: axonflow-circuit-breaker-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: Self-registration on the hosted Community SaaS deployment (`DEPLOYMENT_MODE=community-saas` only).
  name: AxonFlow Community SaaS API
  slug: axonflow-community-saas-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: The Compliance API from AxonFlow — 3 operation(s) for compliance.
  name: AxonFlow Compliance API
  slug: axonflow-compliance-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: Connector marketplace
  name: AxonFlow Connectors API
  slug: axonflow-connectors-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: Budget management and LLM usage tracking for cost optimization. Supports budgets at organization, team, agent, workflow, and user scopes. Provides usage summaries, breakdowns, and pre-request budget c
  name: AxonFlow Cost Controls API
  slug: axonflow-cost-controls-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: The Cost Management API from AxonFlow — 2 operation(s) for cost management.
  name: AxonFlow Cost Management API
  slug: axonflow-cost-management-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: Decision & Execution Replay API for debugging, auditing, and compliance. Captures every step of workflow execution with full input/output snapshots and policy decisions.
  name: AxonFlow Decision & Execution Replay API
  slug: axonflow-decision-execution-replay-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: 'Synchronous policy decision endpoint (ADR-056). Called by an infrastructure gateway acting as a Policy Enforcement Point (PEP); AxonFlow returns a verdict (`allow` or `deny`) and the PEP enforces it. '
  name: AxonFlow Decision Mode API
  slug: axonflow-decision-mode-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: Decision explainability (ADR-043) and session-scoped policy overrides (ADR-044). List recent governance decisions, explain a specific decision, and create/list/revoke time-boxed policy overrides.
  name: AxonFlow Decisions & Overrides API
  slug: axonflow-decisions-overrides-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: Legacy policy management on `/api/v1/policies`. Reads, tests and simulation are served; writes answer `409 LEGACY_POLICY_WRITE_FROZEN` in v11 (see the `LegacyPolicyWriteFrozen` response) - author poli
  name: AxonFlow Dynamic Policies API
  slug: axonflow-dynamic-policies-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: EU AI Act compliance endpoints for technical documentation export, conformity assessments (Article 43), and accuracy/bias tracking (Article 15). Enterprise feature for EU regulatory compliance.
  name: AxonFlow EU AI Act API
  slug: axonflow-eu-ai-act-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: EU AI Act compliance module (conformity assessments, accuracy monitoring, evidence exports). Served by the orchestrator and PROXIED through the agent (`/api/v1/euaiact/*`) per the single-entry-point a
  name: AxonFlow EU AI Act (Proxied) API
  slug: axonflow-eu-ai-act-proxied-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: The Evidence Export API from AxonFlow — 2 operation(s) for evidence export.
  name: AxonFlow Evidence Export API
  slug: axonflow-evidence-export-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: Pre-check and audit for SDK-managed LLM calls
  name: AxonFlow Gateway Mode API
  slug: axonflow-gateway-mode-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: Service health and readiness checks
  name: AxonFlow Health API
  slug: axonflow-health-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: Human-in-the-Loop decision queue (EU AI Act Article 14). Route high-risk AI decisions for human review before execution.
  name: AxonFlow HITL API
  slug: axonflow-hitl-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: Emergency system disable mechanism
  name: AxonFlow Kill Switch API
  slug: axonflow-kill-switch-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: LLM provider management
  name: AxonFlow LLM Providers API
  slug: axonflow-llm-providers-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: The MAP API from AxonFlow — 1 operation(s) for map.
  name: AxonFlow MAP API
  slug: axonflow-map-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: Model Context Protocol data connector operations
  name: AxonFlow MCP Connectors API
  slug: axonflow-mcp-connectors-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: Streamable-HTTP MCP server (spec 2025-06-18) exposing AxonFlow governance as MCP tools (check_policy, check_output, audit_tool_call, list_policies, get_policy_stats, explain_decision + Pro tools). Con
  name: AxonFlow MCP Server API
  slug: axonflow-mcp-server-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: Multimodal image governance for LLM requests. Analyzes images for PII (via OCR), content safety, face/biometric detection, and document classification. Community tier provides fail-open governance wit
  name: AxonFlow Media Governance API
  slug: axonflow-media-governance-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: Performance monitoring and observability
  name: AxonFlow Metrics API
  slug: axonflow-metrics-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: LLM-powered task decomposition and execution
  name: AxonFlow Multi-Agent Planning API
  slug: axonflow-multi-agent-planning-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: OJK AI Governance + UU PDP compliance for Indonesian financial services. Audit export, retention/readiness checks, UU PDP Art. 46 breach-notification lifecycle, and a compliance dashboard. **Enterpris
  name: AxonFlow OJK Compliance API
  slug: axonflow-ojk-compliance-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: 'OpenAI-compatible gateway endpoint (Issue #2351). Accepts standard OpenAI Chat Completions requests, runs AxonFlow policy checks, forwards to the upstream provider, records audit, and returns an OpenA'
  name: AxonFlow OpenAI Compatible API
  slug: axonflow-openai-compatible-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: OpenTelemetry OTLP/HTTP ingest for Claude Code (cowork) telemetry (#2832). **Enterprise only** — community builds mount the routes but return 501. Org/tenant identity always comes from the authenticat
  name: AxonFlow OTLP Ingest API
  slug: axonflow-otlp-ingest-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: Dynamic policy CRUD operations (Orchestrator)
  name: AxonFlow Policies API
  slug: axonflow-policies-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: The Policy Simulation API from AxonFlow — 3 operation(s) for policy simulation.
  name: AxonFlow Policy Simulation API
  slug: axonflow-policy-simulation-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: Main request processing pipeline
  name: AxonFlow Processing API
  slug: axonflow-processing-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: Full request interception and processing
  name: AxonFlow Proxy Mode API
  slug: axonflow-proxy-mode-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: RBI FREE-AI Framework compliance for Indian banking institutions. Enterprise feature providing AI System Registry, Model Validation, Incident Management, Kill Switch, Board Reporting, and Audit Export
  name: AxonFlow RBI Compliance API
  slug: axonflow-rbi-compliance-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: AI System Registry management
  name: AxonFlow Registry API
  slug: axonflow-registry-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: SEBI AI/ML Guidelines compliance and DPDP Act 2023 audit exports. Enterprise feature for Indian financial services compliance.
  name: AxonFlow SEBI Compliance API
  slug: axonflow-sebi-compliance-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: Policy simulation, impact reports, and conflict detection. **Evaluation tier and above.**
  name: AxonFlow Simulation API
  slug: axonflow-simulation-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: DEPRECATED spelling of System Policies, served at `/api/v1/static-policies`. Every operation is the same handler as its `/api/v1/system-policies` counterpart and returns the same status code and body.
  name: AxonFlow Static Policies API
  slug: axonflow-static-policies-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: System policy management (ADR-019), served at `/api/v1/system-policies`. Pattern-based enforcement rules for SQL injection detection, PII detection and similar checks, resolved across the system, orga
  name: AxonFlow System Policies API
  slug: axonflow-system-policies-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: Policy templates for quick policy creation
  name: AxonFlow Templates API
  slug: axonflow-templates-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: Tenant policy CRUD via the ADR-024 `/api/v1/tenant-policies` surface (Orchestrator, proxied by the Agent). On create, update and import it accepts only policies whose category starts with `dynamic-` o
  name: AxonFlow Tenant Policies API
  slug: axonflow-tenant-policies-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: Policy testing and validation
  name: AxonFlow Testing API
  slug: axonflow-testing-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: 'The ADR-065 typed policy authoring surface, available on EVERY edition (#3907). It is the write path a deployment without the Enterprise customer portal uses, and the portal is one client of the same '
  name: AxonFlow Typed Policy Authoring API
  slug: axonflow-typed-policy-authoring-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: 'Unified execution tracking and real-time streaming for MAP plans and WCP workflows. SSE streaming provides real-time status updates. Community: 5 concurrent connections per tenant. Enterprise: Unlimit'
  name: AxonFlow Unified Executions API
  slug: axonflow-unified-executions-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: 'US federal banking and Farm Credit examination evidence (ADR-063). One read: the examination-readiness summary. The evidence itself is produced by the compliance report facade with `regulator=usbankin'
  name: AxonFlow US Banking Compliance API
  slug: axonflow-us-banking-compliance-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: 'NAIC AI Systems Evaluation Tool exhibit evidence for US insurers, with the NYDFS Circular Letter No. 7 and Colorado Regulation 10-1-1 annexes. Read-only: these routes report AI system surfaces, human '
  name: AxonFlow US Insurance Compliance API
  slug: axonflow-us-insurance-compliance-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: 'SEC adviser and FINRA broker-dealer examination evidence (ADR-064). One read: the examination-readiness summary. The evidence itself is produced by the compliance report facade with `regulator=ussecur'
  name: AxonFlow US Securities Compliance API
  slug: axonflow-us-securities-compliance-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: Webhook subscription management for real-time event notifications. Subscribe to events like policy violations, workflow completions, budget alerts, etc.
  name: AxonFlow Webhooks API
  slug: axonflow-webhooks-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: 'Governance gates for external orchestrators (LangChain, LangGraph, CrewAI). "LangChain runs the workflow. AxonFlow decides when it''s allowed to move forward." Features: - Register workflows from exter'
  name: AxonFlow Workflow Control Plane API
  slug: axonflow-workflow-control-plane-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: Workflow execution engine
  name: AxonFlow Workflows API
  slug: axonflow-workflows-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: The Auth ZEN API from AxonFlow — 1 operation(s) for auth zen.
  name: AxonFlow Auth ZEN API
  slug: axonflow-auth-zen-api
artifact_total: 87
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/axonflow/refs/heads/main/well-known/axonflow-getaxonflow-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/axonflow-getaxonflow-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/axonflow/refs/heads/main/agentic-access/axonflow-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/axonflow-agentic-access.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/axonflow/refs/heads/main/rate-limits/axonflow-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/axonflow-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/axonflow/refs/heads/main/plans/axonflow-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/axonflow-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/axonflow/refs/heads/main/rules/axonflow-rules.yml
  title: ''
  type: Spectral
  url: rules/axonflow-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/axonflow/refs/heads/main/rules/axonflow-axonflow-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/axonflow-axonflow-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/axonflow/refs/heads/main/json-ld/axonflow-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/axonflow-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/axonflow/refs/heads/main/vocabulary/axonflow-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/axonflow-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/axonflow/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/axonflow/refs/heads/main/data-model/axonflow-data-model.yml
  title: ''
  type: DataModel
  url: data-model/axonflow-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/axonflow/refs/heads/main/changelog/axonflow-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/axonflow-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/axonflow/refs/heads/main/conventions/axonflow-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/axonflow-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/axonflow/refs/heads/main/conventions/axonflow-conventions.yml
  title: ''
  type: Conventions
  url: conventions/axonflow-conventions.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/axonflow/refs/heads/main/sandbox/axonflow-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/axonflow-sandbox.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/axonflow/refs/heads/main/lifecycle/axonflow-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/axonflow-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/axonflow/refs/heads/main/lifecycle/axonflow-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/axonflow-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/axonflow/refs/heads/main/errors/axonflow-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/axonflow-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/axonflow/refs/heads/main/errors/axonflow-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/axonflow-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/axonflow/refs/heads/main/conformance/axonflow-conformance.yml
  title: ''
  type: Conformance
  url: conformance/axonflow-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/axonflow/refs/heads/main/overlays/axonflow-agent-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/axonflow-agent-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/axonflow/refs/heads/main/llms/axonflow-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/axonflow-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/axonflow/refs/heads/main/mcp/axonflow-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/axonflow-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/axonflow/refs/heads/main/mcp/axonflow-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/axonflow-mcp.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/axonflow/refs/heads/main/well-known/axonflow-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/axonflow-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/axonflow/refs/heads/main/well-known/axonflow-docs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/axonflow-docs-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/axonflow/refs/heads/main/well-known/axonflow-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/axonflow-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/axonflow/refs/heads/main/hosts/axonflow-hosts.yml
  title: ''
  type: Hosts
  url: hosts/axonflow-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/axonflow/refs/heads/main/vendors/axonflow-vendors.yml
  title: ''
  type: Vendors
  url: vendors/axonflow-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/axonflow/refs/heads/main/packages/axonflow-packages.yml
  title: ''
  type: Packages
  url: packages/axonflow-packages.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.getaxonflow.com/docs/orchestration/api-reference/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/axonflow/refs/heads/main/security/axonflow-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/axonflow-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/axonflow/refs/heads/main/authentication/axonflow-authentication.yml
  title: ''
  type: Authentication
  url: authentication/axonflow-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://docs.getaxonflow.com
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.getaxonflow.com/docs/getting-started/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.getaxonflow.com/docs/orchestration/api-reference/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.getaxonflow.com/docs/releases/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getaxonflow
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/getaxonflow/axonflow
- group: build
  title: ''
  type: SDKs
  url: https://getaxonflow.com/sdks/
- group: commercial
  title: ''
  type: Pricing
  url: https://getaxonflow.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://getaxonflow.com/blog/
- group: start
  title: ''
  type: Login
  url: https://app.getaxonflow.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://getaxonflow.com/trust/
- group: company
  title: ''
  type: About
  url: https://getaxonflow.com/about/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://getaxonflow.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://getaxonflow.com/privacy/
- group: design
  title: ''
  type: SpectralRules
  url: https://github.com/getaxonflow/axonflow/blob/220ffccc4ee5776e04b72fded5a91cc76b3c3332/.spectral.yaml
created: '2026-10-09'
description: 'AxonFlow is a runtime governance platform for AI agents. It gives every agent a mandate, limits and a paper trail: deterministic policies evaluated before an agent acts, human approvals, PII redaction, AI usage budgets, tamper-evident audit logs and decision records exportable for frameworks such as the EU AI Act, RBI, SEBI and MAS FEAT. It ships an open-source Community Edition on GitHub, an Evaluation licence and a paid production program, runs in the customer''s own environment, and integrates via Python, TypeScript, Go, Java and Rust SDKs and plugins for LangChain, LangGraph, CrewAI, LiteLLM, n8n, Claude Code, Cursor and others, plus an optional Fraud & Risk Add-on for payment agents.'
image: https://docs.getaxonflow.com/img/axonflow-social-card.png
json_schemas:
- name: AISystemRegistry
  property_count: 24
  slug: axonflow-aisystem-registry
- name: ApplyTemplateRequest
  property_count: 5
  slug: axonflow-apply-template-request
- name: ApprovalResponse
  property_count: 15
  slug: axonflow-approval-response
- name: AuditActionReport
  property_count: 10
  slug: axonflow-audit-action-report
- name: AuditLogEntry
  property_count: 30
  slug: axonflow-audit-log-entry
- name: ClientResponse
  property_count: 18
  slug: axonflow-client-response
- name: CreatePolicyRequest
  property_count: 10
  slug: axonflow-create-policy-request
- name: CreateRegistryRequest
  property_count: 12
  slug: axonflow-create-registry-request
- name: DecideRequest
  property_count: 8
  slug: axonflow-decide-request
- name: DecideResponse
  property_count: 17
  slug: axonflow-decide-response
- name: FEATAssessment
  property_count: 30
  slug: axonflow-featassessment
- name: ImpactReportResponse
  property_count: 11
  slug: axonflow-impact-report-response
- name: KillSwitch
  property_count: 17
  slug: axonflow-kill-switch
- name: MCPCheckInputResponse
  property_count: 20
  slug: axonflow-mcpcheck-input-response
- name: MCPCheckOutputResponse
  property_count: 13
  slug: axonflow-mcpcheck-output-response
- name: OJKAuditExportResponse
  property_count: 12
  slug: axonflow-ojkaudit-export-response
- name: PolicyEvaluationResult
  property_count: 14
  slug: axonflow-policy-evaluation-result
- name: PreCheckResponse
  property_count: 14
  slug: axonflow-pre-check-response
- name: SimulatePoliciesResponse
  property_count: 10
  slug: axonflow-simulate-policies-response
- name: StepGateResponse
  property_count: 16
  slug: axonflow-step-gate-response
- name: TestPolicyResponse
  property_count: 5
  slug: axonflow-test-policy-response
- name: UpdateAssessmentRequest
  property_count: 11
  slug: axonflow-update-assessment-request
- name: UpdatePolicyRequest
  property_count: 9
  slug: axonflow-update-policy-request
- name: UpdateRegistryRequest
  property_count: 12
  slug: axonflow-update-registry-request
jsonld:
- class_count: 120
  name: Axonflow Context
  property_count: 405
  slug: axonflow-context
layout: provider
mcp_servers:
- description: Built-in MCP server of the self-hosted AxonFlow agent (gateway). It is served by every AxonFlow deployment at /api/v1/mcp-server as a single Streamable-HTTP JSON-RPC 2.0 endpoint (initialize, tools/li
  name: AxonFlow MCP Server
  slug: axonflow-mcp-server
modified: '2026-10-09'
name: AxonFlow
nav: Providers
network: true
overview: 'AxonFlow publishes 54 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agents API, Assessments API, Audit API, and 51 more. Tagged areas include Company, AI Governance, AI Agents, Policy Enforcement, and Audit Logging.


  The AxonFlow catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  AxonFlow''s developer surface includes changelog, sandbox, authentication, getting-started guide, API reference, pricing, engineering blog, and 40 more developer resources.'
plans:
- name: Axonflow Plans Pricing
  plan_count: 8
  slug: axonflow-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 4
  name: Axonflow Rate Limits
  slug: axonflow-rate-limits
rules:
- authorship: provider
  effective_rule_count: 41
  extends:
  - spectral:oas
  name: AxonFlow — axonflow rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: axonflow-axonflow-spectral-rules
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: AxonFlow API Rules
  rule_count: 14
  severity_counts:
    error: 8
    hint: 0
    info: 3
    warn: 3
  slug: axonflow-rules
score:
  band: exemplar
  composite: 69.9
  coverage:
    artifact_dirs: 29
    catalog_earned: 84.8
    catalog_earned_first_party: 24.0
    catalog_gap: 30.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.4
  facets:
    access_clarity: 84.2
    contract_governance: 35.6
    contract_quality: 63.4
    developer_ergonomics: 68.5
    discoverability: 71.7
    operational_transparency: 60.5
  previous_composite: 71.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 54
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://raw.githubusercontent.com/api-evangelist/axonflow/refs/heads/main/screenshots/axonflow-2026-10-11T101252.png
security:
- kind: authentication
  name: Axonflow Authentication
  slug: axonflow-authentication
  summary_line: apiKey/http · 6 schemes
- kind: domain-security
  name: Axonflow Domain Security
  slug: axonflow-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: axonflow
tags:
- Company
- AI Governance
- AI Agents
- Policy Enforcement
- Audit Logging
- Compliance
- MCP
- Open Source
website: https://docs.getaxonflow.com
---
