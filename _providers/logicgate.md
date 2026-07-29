---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 51.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 24
  human_in_the_loop: 0
  name: Logicgate Agentic Access
  operation_count: 43
  slug: logicgate-agentic-access
  summary_line: 43 operations · 24 acting
api_count: 11
apis:
- description: An Access Audit captures information about access related events such as logins and logouts associated with a user.
  name: LogicGate Access Audit API
  slug: logicgate-access-audit-api
- description: An [Application](https://help.logicgate.com/hc/en-us/articles/4402674055572-Create-a-new-Application) is a collection of Workflows, Steps, and logic that collectively solve a business use case
  name: LogicGate Application API
  slug: logicgate-application-api
- description: 'Getting Started: How to create an [API Access Token](https://www.logicgate.com/developer/risk-cloud-api-authentication/) to begin integrating with the Risk Cloud API'
  name: LogicGate Authentication API
  slug: logicgate-authentication-api
- description: A [Conditional Edge Path](https://help.logicgate.com/hc/en-us/articles/4402683114004-Work-with-Paths#conditional-edge-paths) defines an alternative route that a Record might need to follow if specific
  name: LogicGate Edge Path API
  slug: logicgate-edge-path-api
- description: A [Field](https://help.logicgate.com/hc/en-us/articles/4402674064020-Create-Fields) is used to capture information from and display information to users in a Workflow
  name: LogicGate Field API
  slug: logicgate-field-api
- description: API endpoints for determining the next path(s) in a workflow, including routing and step information.
  name: LogicGate Next Path API
  slug: logicgate-next-path-api
- description: A [Record](https://help.logicgate.com/hc/en-us/articles/4402683104020-Complete-a-Record) is a form that can capture information, store cataloged data, and link to other Records as it moves through eac
  name: LogicGate Record API
  slug: logicgate-record-api
- description: 'A [Redirect Path](https://help.logicgate.com/hc/en-us/articles/4402683115156-Selected-Redirects) gives end users access to Redirect a Record to any Step in the Workflow other than the Default Path or '
  name: LogicGate Redirect Path API
  slug: logicgate-redirect-path-api
- description: A [Step](https://help.logicgate.com/hc/en-us/articles/4402674059668-Create-a-Step) lives in a Workflow and is configured with a set of Sections, Subsections and Fields to create a form
  name: LogicGate Step API
  slug: logicgate-step-api
- description: A [Workflow](https://help.logicgate.com/hc/en-us/articles/4402683108756-Create-a-new-Workflow) is a combination of Steps, Paths, Fields, and routing logic that combine to form a system in an Applicati
  name: LogicGate Workflow API
  slug: logicgate-workflow-api
- description: A [Workflow Map](https://help.logicgate.com/hc/en-us/articles/4402683117588) represents a relationship between two Workflows
  name: LogicGate Workflow Map API
  slug: logicgate-workflow-map-api
artifact_total: 17
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.logicgate.com/developer/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.logicgate.com/v2/index.html
- group: docs
  title: ''
  type: APIReference
  url: https://docs.logicgate.com/v2/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://www.logicgate.com/developer/risk-cloud-api-getting-started/
- group: operate
  title: ''
  type: Support
  url: https://help.logicgate.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LogicGateTech
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/logicgate-postman/logicgate-risk-cloud-api/overview
- group: commercial
  title: ''
  type: Pricing
  url: https://www.logicgate.com/pricing/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.logicgate.com/privacy-policy/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/logicgate-risk-cloud-openapi-original.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/logicgate-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/logicgate-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/logicgate-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/logicgate-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/logicgate-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/logicgate-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/logicgate-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.logicgate.com/
- group: other
  title: ''
  type: Overlay
  url: overlays/logicgate-risk-cloud-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/logicgate-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/logicgate-llms.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/logicgate-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/logicgate-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/logicgate-security.txt
- group: auth
  title: ''
  type: TrustCenter
  url: security/logicgate-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/logicgate-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.logicgate.com/vulnerability-disclosure
- group: auth
  title: ''
  type: DomainSecurity
  url: security/logicgate-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://logicgate.com/
created: '2026-07-17'
description: LogicGate is the maker of Risk Cloud, a no-code governance, risk, and compliance (GRC) platform that lets teams design, automate, and connect their risk and compliance programs. The Risk Cloud API v2 is an API-first, RESTful interface for managing the building blocks of a Risk Cloud environment - Applications, Workflows, Workflow Maps, Steps, Paths (edge/next/redirect), Fields, Records, and Access Audits - so organizations can integrate, automate, and build custom workflows against their risk data. Authentication is an HTTP bearer "API Token" minted via HTTP basic against the token endpoint, and API access requires the paid API Access add-on. The v2 OpenAPI 3.1 specification is published on GitHub as the single source of truth, alongside a Postman collection and interactive documentation.
image: https://www.logicgate.com/wp-content/uploads/img-grid-01.png
layout: provider
mcp_servers:
- description: ''
  name: logicgate-mcp.yml
  slug: logicgate-mcpyml
modified: '2026-07-20'
name: LogicGate
nav: Providers
network: true
overview: 'LogicGate publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Access Audit API, Application API, Authentication API, and 8 more. Tagged areas include Company, GRC, Governance Risk and Compliance, Risk Management, and Compliance.


  LogicGate''s developer surface includes documentation, API reference, getting-started guide, support, pricing, authentication, changelog, and 23 more developer resources.'
random_paper: 19
score:
  band: developing
  composite: 49.6
  delta: -1.3
  facets:
    commercial_clarity: 36.8
    contract_quality: 63.6
    developer_ergonomics: 58.2
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 31.6
  previous_composite: 50.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/logicgate/refs/heads/main/screenshots/logicgate-2026-07-25T225458.png
security:
- kind: authentication
  name: Logicgate Authentication
  slug: logicgate-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Logicgate Domain Security
  slug: logicgate-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Logicgate Vulnerability Disclosure
  slug: logicgate-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Logicgate Trust Center
  slug: logicgate-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, FedRAMP, GDPR
slug: logicgate
tags:
- Company
- GRC
- Governance Risk and Compliance
- Risk Management
- Compliance
- Workflow Automation
- Audit
- No-Code
website: https://logicgate.com/
---
