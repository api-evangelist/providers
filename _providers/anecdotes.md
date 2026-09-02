---
agent_readiness:
  band: agent-ready
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
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.7
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 49
  human_in_the_loop: 10
  name: Anecdotes Agentic Access
  operation_count: 114
  slug: anecdotes-agentic-access
  summary_line: 114 operations · 49 acting · 10 human-in-the-loop
api_count: 3
apis:
- description: 'A hosted Model Context Protocol proxy that exposes Anecdotes GRC domains - risk, control, evidence, policy, framework, uar, analysis, comments, requirement and semantic search - to any MCP-capable AI '
  name: Anecdotes MCP Proxy
  slug: anecdotes-mcp-proxy
- description: '**Analysis rules** evaluate evidence table rows for **gaps or warnings**; configure query, scoping, and alert levels, and read **execution results** per instance. [Analysis rules (product)](https://he'
  name: anecdotes Analysis Rules API
  slug: anecdotes-analysis-rules-api
- description: API key to JWT exchange and token management.
  name: anecdotes Authorization API
  slug: anecdotes-authorization-api
- description: Create one or more **custom controls** in a framework.
  name: anecdotes Create Controls API
  slug: anecdotes-create-controls-api
- description: 'Create custom **Evidence Collections**, **attach** JSON/CSV files to a collection, and upload **manual** evidence of any type. Customer-pushed evidence can also carry **IPE** (Information Produced by '
  name: anecdotes Create Evidence API
  slug: anecdotes-create-evidence-api
- description: '**Custom fields** extend platform resources (including **requirements**) with your own **dropdown**, **multi-select**, or **free-text** values. These endpoints manage the field **definitions** — creat'
  name: anecdotes Custom Fields API
  slug: anecdotes-custom-fields-api
- description: Download **raw** evidence payloads, processed **evidence tables**, combined full-or-raw streams, and latest binary payloads.
  name: anecdotes Download Evidence API
  slug: anecdotes-download-evidence-api
- description: '**Findings** record compliance gaps and issues, including links to controls, evidence, and policies.'
  name: anecdotes Findings API
  slug: anecdotes-findings-api
- description: 'A **framework** in anecdotes is a compliance program built from a formally written standard or regulation (e.g. ISO/IEC 27001, SOC 2, HIPAA, CSA STAR). It is organized into **control categories** and '
  name: anecdotes Framework API
  slug: anecdotes-framework-api
- description: Authorization package, KSI and evidence endpoints. Require an approved FedRAMP user JWT.
  name: anecdotes Gated API
  slug: anecdotes-gated-api
- description: '**Policy Manager** allows you to create, edit, and manage policies for your organization. List customer-owned policies, library templates, policy versions, and configure approval cycles.'
  name: anecdotes Policy Manager API
  slug: anecdotes-policy-manager-api
- description: Public Trust Center information. No authentication required.
  name: anecdotes Public API
  slug: anecdotes-public-api
- description: List all controls or fetch by framework or id.
  name: anecdotes Read Controls API
  slug: anecdotes-read-controls-api
- description: List and retrieve **evidence definitions**, **instance metadata**, and multi-instance **run history**.
  name: anecdotes Read Evidence Metadata API
  slug: anecdotes-read-evidence-metadata-api
- description: '**Requirements** tie **controls** to expected **evidence** and framework scoping. These endpoints cover listing customer requirements, simple **create / read / update / delete** for a single requireme'
  name: anecdotes Requirements API
  slug: anecdotes-requirements-api
- description: '**Risks** live in **risk registers** in Risk Manager: inherent/residual dimensions, treatment, custom fields, and links to evidence. **API:** create, list (full), get, update. [Risk Manager](https://h'
  name: anecdotes Risk API
  slug: anecdotes-risk-api
- description: 'Exchange your **API key** for a **short-lived JWT** (1 hour). Send the JWT as `Authorization: Bearer <token>` on all subsequent requests.'
  name: anecdotes Token API
  slug: anecdotes-token-api
- description: Update or delete a **custom control**'s name, description, category, and implementation.
  name: anecdotes Update Control Metadata API
  slug: anecdotes-update-control-metadata-api
artifact_total: 30
asyncapis:
- description: ''
  name: Anecdotes Playbooks Webhooks
  slug: anecdotes-playbooks-webhooks
collections:
- collection_type: postman
  name: FedRAMP 20x API
  slug: postman-anecdotes-fedramp-20x
- collection_type: open
  name: Anecdotes FedRAMP 20x Trust Center API
  slug: open-anecdotes-fedramp-20x
- collection_type: open
  name: Anecdotes API
  slug: open-anecdotes-grc-openapi-original
- collection_type: open
  name: Anecdotes API
  slug: open-anecdotes-grc
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/anecdotes-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.anecdotes.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.anecdotes.ai/technical-setup/api
- group: docs
  title: ''
  type: Documentation
  url: https://help.anecdotes.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://help.anecdotes.ai/api/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://help.anecdotes.ai/technical-setup/api/using-the-anecdotes-api
- group: operate
  title: ''
  type: Support
  url: https://help.anecdotes.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.anecdotes.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/anecdotes-ai
- group: commercial
  title: ''
  type: Pricing
  url: https://www.anecdotes.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.anecdotes.ai/get-started
- group: start
  title: ''
  type: Login
  url: https://platform.anecdotes.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.anecdotes.ai/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.anecdotes.ai/privacy-policy
- group: build
  title: ''
  type: Postman
  url: postman/anecdotes-fedramp-20x.postman_collection.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/anecdotes-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/anecdotes-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/anecdotes-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/anecdotes-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/anecdotes-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/anecdotes-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/anecdotes-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/anecdotes-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.anecdotes.ai/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/anecdotes-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/anecdotes-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/anecdotes-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.anecdotes.ai/trust
- group: auth
  title: ''
  type: TrustCenter
  url: security/anecdotes-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/anecdotes-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/anecdotes-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.anecdotes.ai/trust
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/anecdotes-playbooks-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/anecdotes-grc-overlay.yaml
- group: build
  title: ''
  type: Examples
  url: examples/anecdotes-examples.yml
created: '2026-07-31'
description: anecdotes is an enterprise Governance, Risk and Compliance (GRC) platform, founded in 2020 and headquartered in Tel Aviv, that pairs a GRC data engine with AI agents to replace point-in-time audit cycles with continuous, evidence-backed compliance. Its Compliance OS collects evidence automatically from 230+ pre-built plugins into 1,000+ predefined artifacts, maps that evidence across 60+ frameworks at once, and drives core applications for controls, requirements, risk, policy management, findings and user access review. Developers reach the platform through a documented REST API at api.anecdotes.ai (API key exchanged for a short-lived JWT), a hosted MCP Proxy at mcp.anecdotes.ai that exposes GRC domains as agent tools, a FedRAMP 20x Trust Center API with genuinely public endpoints, SAML SSO and SCIM provisioning, and outbound event webhooks driven by Playbooks.
image: https://kinlane-productions2.s3.amazonaws.com/api-evangelist-site/companies/anecdotes.jpg
layout: provider
mcp_servers:
- description: ''
  name: anecdotes MCP Server
  slug: anecdotes-mcp-server
modified: '2026-07-31'
name: anecdotes
nav: Providers
network: true
overview: 'anecdotes publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Analysis Rules API, Authorization API, Create Controls API, and 14 more. Tagged areas include Company, Compliance, Governance, Risk, and Security.


  The anecdotes catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  anecdotes'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 29 more developer resources.'
random_paper: 5
rate_limits:
- limit_count: 1
  name: Anecdotes Rate Limits
  slug: anecdotes-rate-limits
score:
  band: strong
  composite: 63.8
  coverage:
    artifact_dirs: 23
    catalog_gap: 67.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 70.4
    developer_ergonomics: 70.8
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 73.7
  previous_composite: 64.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/anecdotes/refs/heads/main/screenshots/anecdotes-2026-08-07T161404.png
security:
- kind: authentication
  name: Anecdotes Authentication
  slug: anecdotes-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Anecdotes Domain Security
  slug: anecdotes-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Anecdotes Vulnerability Disclosure
  slug: anecdotes-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Anecdotes Trust Center
  slug: anecdotes-trust-center
  summary_line: SOC 1, SOC 2, ISO 27001, ISO 27701, ISO 27032, ISO 42001, GDPR
slug: anecdotes
tags:
- Company
- Compliance
- Governance
- Risk
- Security
- GRC
- Audit
- Evidence
- Continuous Compliance
- FedRAMP
- Artificial Intelligence
- Agents
website: https://www.anecdotes.ai/
---
