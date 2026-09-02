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
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.2
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The Assignments API from Sana — 1 operation(s) for assignments.
  name: Sana Assignments API
  slug: sana-assignments-api
- description: The Authentication API from Sana — 2 operation(s) for authentication.
  name: Sana Authentication API
  slug: sana-authentication-api
- description: The Courses API from Sana — 6 operation(s) for courses.
  name: Sana Courses API
  slug: sana-courses-api
- description: The Groups API from Sana — 4 operation(s) for groups.
  name: Sana Groups API
  slug: sana-groups-api
- description: The Paths API from Sana — 2 operation(s) for paths.
  name: Sana Paths API
  slug: sana-paths-api
- description: The Programs API from Sana — 3 operation(s) for programs.
  name: Sana Programs API
  slug: sana-programs-api
- description: The Reporting API from Sana — 5 operation(s) for reporting.
  name: Sana Reporting API
  slug: sana-reporting-api
- description: The Teamspaces API from Sana — 3 operation(s) for teamspaces.
  name: Sana Teamspaces API
  slug: sana-teamspaces-api
- description: The Users API from Sana — 8 operation(s) for users.
  name: Sana Users API
  slug: sana-users-api
- description: The xAPI API from Sana — 1 operation(s) for xapi.
  name: Sana xAPI API
  slug: sana-xapi-api
artifact_total: 27
asyncapis:
- description: ''
  name: Sana Events Webhooks
  slug: sana-events-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Sana Assignments API
  slug: open-sana-assignments-api
- collection_type: open
  name: Sana Assignments Authentication API
  slug: open-sana-authentication-api
- collection_type: open
  name: Sana Assignments Courses API
  slug: open-sana-courses-api
- collection_type: open
  name: Sana Assignments Groups API
  slug: open-sana-groups-api
- collection_type: open
  name: Sana Assignments Paths API
  slug: open-sana-paths-api
- collection_type: open
  name: Sana Assignments Programs API
  slug: open-sana-programs-api
- collection_type: open
  name: Sana Assignments Reporting API
  slug: open-sana-reporting-api
- collection_type: open
  name: Sana Assignments Teamspaces API
  slug: open-sana-teamspaces-api
- collection_type: open
  name: Sana Assignments Users API
  slug: open-sana-users-api
- collection_type: open
  name: Sana Assignments xAPI API
  slug: open-sana-xapi-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/sana-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/sana-openapi-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sana-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sanalabs.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.sana.ai/api-docs/
- group: docs
  title: ''
  type: Documentation
  url: https://help.sana.ai/en/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.sana.ai/api-docs/
- group: operate
  title: ''
  type: Support
  url: https://support.sana.ai/en/
- group: commercial
  title: ''
  type: Pricing
  url: https://sana.ai/pricing
- group: start
  title: ''
  type: Login
  url: https://app.sana.ai
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sana.ai
- group: auth
  title: ''
  type: TrustCenter
  url: https://app.eu.vanta.com/sanalabs/trust/5awpv6z2jqb96ybu60v6ir
- group: auth
  title: ''
  type: Compliance
  url: https://app.eu.vanta.com/sanalabs/trust/5awpv6z2jqb96ybu60v6ir
- group: auth
  title: ''
  type: Authentication
  url: authentication/sana-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/sana-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sana-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sana-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sana-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/sana-events-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sana-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sana-llms.txt
- group: design
  title: ''
  type: DataModel
  url: data-model/sana-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Sana is an enterprise AI platform, now part of Workday, offering two products: Sana, an AI knowledge and agent workspace that automates tasks, answers questions, and generates documents across a company''s connected applications; and Sana Learn, an AI-native learning platform combining LMS, LXP, authoring, and virtual classroom capabilities. Sana exposes a secure REST API (users, groups, programs, assignments, courses, paths, teamspaces, reporting and Insights, and xAPI statements), served per tenant at https://<domain>.sana.ai and authenticated with OAuth 2.0 client credentials using read/write scopes. It also provides SCIM 2.0 user provisioning, SAML/OIDC single sign-on, and real-time xAPI webhook events. Sana is ISO 27001, SOC 2, and GDPR compliant and runs on Google Cloud. Originally surfaced as a portfolio company of NEA.'
image: https://www.sanalabs.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Sana MCP Server
  slug: sana-mcp-server
modified: '2026-07-21'
name: Sana
nav: Providers
network: true
overview: 'Sana publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Assignments API, Authentication API, Courses API, and 7 more. Tagged areas include Company, Enterprise AI, Artificial Intelligence, Learning Management, and LMS.


  The Sana catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Sana''s developer surface includes documentation, API reference, support, pricing, authentication, and 18 more developer resources.'
random_paper: 20
scopes:
- name: Sana Scopes
  scope_count: 2
  slug: sana-scopes
  summary_line: 2 scopes · clientCredentials
score:
  band: developing
  composite: 41.8
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 18.2
    contract_quality: 61.2
    developer_ergonomics: 44.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 23.7
  previous_composite: 42.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 50.0
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sana/refs/heads/main/screenshots/sana-2026-08-17T081718.png
security:
- kind: authentication
  name: Sana Authentication
  slug: sana-authentication
  summary_line: oauth2/http · 4 schemes
- kind: domain-security
  name: Sana Domain Security
  slug: sana-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Sana Trust Center
  slug: sana-trust-center
  summary_line: ISO 27001, SOC 2, GDPR
slug: sana
tags:
- Company
- Enterprise AI
- Artificial Intelligence
- Learning Management
- LMS
- Knowledge-Management
- Agents
- SCIM
- xAPI
- REST API
website: https://www.sanalabs.com
---
