---
agent_readiness:
  band: agent-ready
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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.5
  scored_at: '2026-09-02'
api_count: 3
apis:
- description: The Public API of the Digital Enterprise Suite — 129 operations across 30 resource groups covering modeling places and their content, model promotion change requests, execution environments and deploy
  name: Trisotech Digital Enterprise Suite Public API
  slug: public-api
- description: 'Every service published to the Trisotech Service Library gets its own REST endpoint and its own generated OpenAPI document, built from that service''s inputs, outputs and characteristics. The endpoint '
  name: Trisotech Automation (Service Execution) API
  slug: automation-api
- description: 'A read-only SPARQL 1.1 endpoint over the Digital Enterprise Graph, the RDF projection of every model in a modeling place. One graph exists per place, named http://trisotech.com/graph/1.0/graph#<place '
  name: Trisotech Digital Enterprise Graph SPARQL API
  slug: graph-sparql
artifact_total: 12
asyncapis:
- description: ''
  name: Trisotech Events
  slug: trisotech-events
common:
- group: company
  title: ''
  type: Website
  url: https://www.trisotech.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://cloud.trisotech.com/help/des/system-integration/system-integration.html
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.trisotech.com/help/
- group: docs
  title: ''
  type: APIReference
  url: https://cloud.trisotech.com/help/des/system-integration/rest-api-documentation.html
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.trisotech.com/help/des/system-integration/rest-api.html
- group: operate
  title: ''
  type: Support
  url: https://www.trisotech.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://www.trisotech.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.trisotech.com/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Trisotech
- group: commercial
  title: ''
  type: Pricing
  url: https://www.trisotech.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.trisotech.com/trials/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.trisotech.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.trisotech.com/privacy-statement/
- group: operate
  title: ''
  type: StatusPage
  url: https://www.trisotech.com/status/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.trisotech.com/release-notes/
- group: auth
  title: ''
  type: Security
  url: https://www.trisotech.com/security/
- group: auth
  title: ''
  type: Compliance
  url: conformance/trisotech-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/trisotech-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/trisotech-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trisotech-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/trisotech-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/trisotech-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/trisotech-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/trisotech-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/trisotech-rate-limits.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/trisotech-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/trisotech-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/trisotech-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/trisotech-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/trisotech-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/trisotech-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/trisotech-mcp.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/trisotech-events.yml
- group: design
  title: ''
  type: Components
  url: components/trisotech-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/trisotech-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/trisotech-llms.txt
created: '2026-09-02'
description: 'Trisotech is a Montreal, Canada software company, founded in 1996, that builds the Digital Enterprise Suite — a standards-anchored low-code platform for modelling and automating business processes, cases and decisions. Its modelers implement the OMG trio of BPMN 2.0, CMMN 1.1 and DMN with FEEL, and its Digital Automation Suite executes those same models as live services. Trisotech''s founder chairs OMG work on those standards, and the product line reflects it: services publish themselves as OpenAPI, as containers, as CDS Hooks discovery endpoints and SMART on FHIR applications for healthcare, and as Model Context Protocol servers for AI agents. The platform is sold into healthcare, finance and the public sector, and the machine-readable surface is a 129-operation OAuth 2 Public API for repository, deployment, identity and administration work, plus a per-service Automation API and a SPARQL endpoint over the Digital Enterprise Graph.'
image: https://www.trisotech.com/wp-content/themes/trisotech/images/logo-trisotech-brand.png
layout: provider
mcp_servers:
- description: ''
  name: Trisotech Service Library MCP Server
  slug: trisotech-service-library-mcp-server
modified: '2026-09-02'
name: Trisotech
nav: Providers
network: true
overview: 'Trisotech publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Business Process Management, Decision Management, Workflow Automation, Low Code, and BPMN.


  The Trisotech catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Trisotech''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 30 more developer resources.'
plans:
- name: Trisotech Plans Pricing
  plan_count: 0
  slug: trisotech-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Trisotech Rate Limits
  slug: trisotech-rate-limits
scopes:
- name: Trisotech Scopes
  scope_count: 20
  slug: trisotech-scopes
  summary_line: 20 scopes
score:
  band: strong
  composite: 62.3
  coverage:
    artifact_dirs: 19
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 66.1
    discoverability: 74.1
    governance: 18.2
    operational_transparency: 55.3
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 83.8
  schema_version: 0.18.0
  scored_at: '2026-09-02'
security:
- kind: authentication
  name: Trisotech Authentication
  slug: trisotech-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Trisotech Domain Security
  slug: trisotech-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Trisotech Vulnerability Disclosure
  slug: trisotech-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Trisotech Trust Center
  slug: trisotech-trust-center
  summary_line: SOC 2 Type II, ISO/IEC 27001:2013, SOC 3
slug: trisotech
tags:
- Business Process Management
- Decision Management
- Workflow Automation
- Low Code
- BPMN
- DMN
- CMMN
- Healthcare
- FHIR
- Clinical Decision Support
- Standards
- AI Agents
- Model Context Protocol
- Enterprise Architecture
website: https://www.trisotech.com/
---
