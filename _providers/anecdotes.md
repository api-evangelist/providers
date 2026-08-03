---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.5
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 49
  human_in_the_loop: 10
  name: Anecdotes Agentic Access
  operation_count: 114
  slug: anecdotes-agentic-access
  summary_line: 114 operations · 49 acting · 10 human-in-the-loop
api_count: 3
apis:
- description: 'The Anecdotes API provides programmatic access to the Anecdotes GRC platform: frameworks, requirements, controls, custom fields, risks, findings, policies, analysis rules and evidence. Authentication '
  name: Anecdotes GRC API
  slug: anecdotes-grc-api
- description: A three-tier API over the Anecdotes Trust Center. Public endpoints require no authentication and return Cloud Service Offering metadata, the status-page rollup, the Recommended Secure Configuration in
  name: Anecdotes FedRAMP 20x Trust Center API
  slug: anecdotes-fedramp-20x-api
- description: 'A hosted Model Context Protocol proxy that exposes Anecdotes GRC domains - risk, control, evidence, policy, framework, uar, analysis, comments, requirement and semantic search - to any MCP-capable AI '
  name: Anecdotes MCP Proxy
  slug: anecdotes-mcp-proxy
artifact_total: 12
asyncapis:
- description: ''
  name: Anecdotes Playbooks Webhooks
  slug: anecdotes-playbooks-webhooks
collections:
- collection_type: postman
  name: FedRAMP 20x API
  slug: postman-anecdotes-fedramp-20x
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
  name: anecdotes-mcp.yml
  slug: anecdotes-mcpyml
modified: '2026-07-31'
name: anecdotes
nav: Providers
network: true
overview: 'anecdotes publishes 2 APIs on the [APIs.io](https://apis.io/) network: GRC API and FedRAMP 20x Trust Center API. Tagged areas include Company, Compliance, Governance, Risk, and Security.


  The anecdotes catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  anecdotes'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 29 more developer resources.'
random_paper: 0
rate_limits:
- limit_count: 1
  name: Anecdotes Rate Limits
  slug: anecdotes-rate-limits
score:
  band: strong
  composite: 65.1
  facets:
    commercial_clarity: 60.5
    contract_quality: 73.5
    developer_ergonomics: 64.7
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 76.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
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
