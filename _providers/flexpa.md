---
access_model:
  confidence: high
  label: Paid (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 55.0
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Flexpa Agentic Access
  operation_count: 15
  slug: flexpa-agentic-access
  summary_line: 15 operations · 2 acting
api_count: 4
apis:
- description: The Access Tokens API from Flexpa — 1 operation(s) for access tokens.
  name: Flexpa Access Tokens API
  slug: flexpa-access-tokens-api
- description: The Claims Data API from Flexpa — 5 operation(s) for claims data.
  name: Flexpa Claims Data API
  slug: flexpa-claims-data-api
- description: The FHIR API from Flexpa — 8 operation(s) for fhir.
  name: Flexpa FHIR API
  slug: flexpa-fhir-api
- description: The Link API from Flexpa — 1 operation(s) for link.
  name: Flexpa Link API
  slug: flexpa-link-api
artifact_total: 20
asyncapis:
- description: ''
  name: Flexpa Webhooks
  slug: flexpa-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Flexpa Access Tokens API
  slug: open-flexpa-access-tokens-api
- collection_type: open
  name: Flexpa Access Tokens Claims Data API
  slug: open-flexpa-claims-data-api
- collection_type: open
  name: Flexpa Access Tokens FHIR API
  slug: open-flexpa-fhir-api
- collection_type: open
  name: Flexpa Access Tokens Link API
  slug: open-flexpa-link-api
- collection_type: open
  name: Flexpa API
  slug: open-flexpa
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/flexpa-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flexpa-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/flexpa-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/flexpa
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/flexpa
- group: company
  title: ''
  type: Website
  url: https://www.flexpa.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.flexpa.com/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/flexpa-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/flexpa-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/flexpa-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.flexpa.com/blog
- group: agent
  title: ''
  type: WellKnown
  url: well-known/flexpa-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/flexpa-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/flexpa-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/flexpa-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/flexpa-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/flexpa-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/flexpa-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/flexpa-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/flexpa-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://flexpastatus.com
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/flexpa-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/flexpa-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://security.flexpa.com
- group: auth
  title: ''
  type: TrustCenter
  url: security/flexpa-trust-center.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/flexpa-scopes.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/flexpa-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/flexpa-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/flexpa-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/flexpa-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.flexpa.com
- group: docs
  title: ''
  type: APIReference
  url: https://www.flexpa.com/docs/records
- group: start
  title: ''
  type: GettingStarted
  url: https://www.flexpa.com/docs/guides/quickstart
- group: operate
  title: ''
  type: Support
  url: https://www.flexpa.com/docs/support
- group: commercial
  title: ''
  type: Pricing
  url: https://www.flexpa.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.flexpa.com/demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.flexpa.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.flexpa.com/privacy
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/flexpa
created: '2026-06-21'
description: Flexpa is a patient-access platform that lets applications connect a patient to their health insurance plan and retrieve claims and clinical data as normalized FHIR R4 resources. Patients authorize access through Flexpa Link / OAuth 2.0 PKCE, and applications read ExplanationOfBenefit, Coverage, Patient, and other resources from a single FHIR API at https://api.flexpa.com.
finops:
- name: Flexpa Finops
  service_category: Healthcare
  slug: flexpa-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/flexpa.png
layout: provider
mcp_servers:
- description: ''
  name: flexpa-mcp.yml
  slug: flexpa-mcpyml
modified: '2026-08-14'
name: Flexpa
nav: Providers
network: true
overview: 'Flexpa publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Access Tokens API, Claims Data API, FHIR API, and 1 more. Tagged areas include Healthcare, FHIR, Patient Access, Claims Data, and Health Insurance.


  The Flexpa catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Flexpa''s developer surface includes authentication, documentation, engineering blog, changelog, sandbox, API reference, getting-started guide, and 33 more developer resources.'
plans:
- name: Flexpa Plans Pricing
  plan_count: 5
  slug: flexpa-plans-pricing
random_paper: 44
rate_limits:
- limit_count: 6
  name: Flexpa Rate Limits
  slug: flexpa-rate-limits
scopes:
- name: Flexpa Scopes
  scope_count: 0
  slug: flexpa-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 72.4
  delta: 37.9
  facets:
    commercial_clarity: 100.0
    contract_quality: 62.9
    developer_ergonomics: 80.4
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 76.3
  previous_composite: 34.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 66.3
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/flexpa/refs/heads/main/screenshots/flexpa-2026-07-25T214752.png
security:
- kind: authentication
  name: Flexpa Authentication
  slug: flexpa-authentication
  summary_line: oauth2/http/apiKey · 3 schemes
- kind: domain-security
  name: Flexpa Domain Security
  slug: flexpa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Flexpa Trust Center
  slug: flexpa-trust-center
  summary_line: SOC 2 (published as "SOC II"), HIPAA, CARIN Alliance Code of Conduct
slug: flexpa
tags:
- Healthcare
- FHIR
- Patient Access
- Claims Data
- Health Insurance
website: https://www.flexpa.com
---
