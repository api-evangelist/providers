---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 39.0
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 55
  human_in_the_loop: 2
  name: Unqork Agentic Access
  operation_count: 93
  slug: unqork-agentic-access
  summary_line: 93 operations · 55 acting · 2 human-in-the-loop
api_count: 1
apis:
- description: 'An application is the parent of a group of one or more elements. An application can be of either ''Module'' (type is `form` in DB) or ''Workflow'' type. ''Module'' type application cannot have workflow but '
  name: Unqork Applications API
  slug: unqork-applications-api
- description: The Authentication API from Unqork — 1 operation(s) for authentication.
  name: Unqork Authentication API
  slug: unqork-authentication-api
- description: The Credentials API from Unqork — 3 operation(s) for credentials.
  name: Unqork Credentials API
  slug: unqork-credentials-api
- description: The Data Collections API from Unqork — 2 operation(s) for data collections.
  name: Unqork Data Collections API
  slug: unqork-data-collections-api
- description: The Data Model Records API from Unqork — 1 operation(s) for data model records.
  name: Unqork Data Model Records API
  slug: unqork-data-model-records-api
- description: The Global Variables API from Unqork — 2 operation(s) for global variables.
  name: Unqork Global Variables API
  slug: unqork-global-variables-api
- description: The following endpoints are available to "Administrator" users only.
  name: Unqork Groups API
  slug: unqork-groups-api
- description: The Logs API from Unqork — 1 operation(s) for logs.
  name: Unqork Logs API
  slug: unqork-logs-api
- description: The Modules API from Unqork — 5 operation(s) for modules.
  name: Unqork Modules API
  slug: unqork-modules-api
- description: The following endpoints are available to "Administrator" users and users with the "Promote" permission for the resource.
  name: Unqork Promotions API
  slug: unqork-promotions-api
- description: The Query API from Unqork — 1 operation(s) for query.
  name: Unqork Query API
  slug: unqork-query-api
- description: The Revisions API from Unqork — 4 operation(s) for revisions.
  name: Unqork Revisions API
  slug: unqork-revisions-api
- description: The Search Configs API from Unqork — 1 operation(s) for search configs.
  name: Unqork Search Configs API
  slug: unqork-search-configs-api
- description: The Submissions API from Unqork — 8 operation(s) for submissions.
  name: Unqork Submissions API
  slug: unqork-submissions-api
- description: 'The following endpoints are available to "Administrator" users only. Transforms should expect the following input data structure: ***NJK (in):***<br/> Input includes only the `data.rawData` part of th'
  name: Unqork Transforms API
  slug: unqork-transforms-api
- description: The following endpoints are available to "Administrator" users only.
  name: Unqork Users API
  slug: unqork-users-api
- description: The Workflow API from Unqork — 10 operation(s) for workflow.
  name: Unqork Workflow API
  slug: unqork-workflow-api
artifact_total: 27
asyncapis:
- description: ''
  name: Unqork Webhooks
  slug: unqork-webhooks
collections:
- collection_type: open
  name: Unqork Customer API
  slug: open-unqork-customer-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/unqork-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/unqork-customer-api-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/unqork-mcp.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/unqork-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/unqork-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://unqork.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.unqork.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.unqork.io/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.unqork.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.unqork.io/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://community.unqork.com/
- group: company
  title: ''
  type: Blog
  url: https://unqork.com/resource-center/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/unqork-external
- group: start
  title: ''
  type: SignUp
  url: https://community.unqork.com/member/register
- group: commercial
  title: ''
  type: Pricing
  url: https://unqork.com/pricing-meeting-request/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://unqork.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://unqork.com/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.unqork.com/
- group: auth
  title: ''
  type: Security
  url: https://unqork.com/security/
- group: auth
  title: ''
  type: Compliance
  url: https://unqork.com/security-compliance/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.unqork.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.unqork.io/docs/unqork-release-notes
- group: learn
  title: ''
  type: Training
  url: https://academy.unqork.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/unqork-llms.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/unqork-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/unqork-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/unqork-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/unqork-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/unqork-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/unqork-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/unqork-components.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/unqork-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-31'
description: Unqork is an enterprise application development platform — a no-code / "codeless" platform-as-a-service used by banks, insurers, healthcare organizations and government agencies to build and operate complex, regulated business applications without hand-written application code. Creators assemble applications from modules, workflows, components and data models in the Unqork Designer, and the platform exposes a REST Customer API (documented as OpenAPI 3.0.3 at developers.unqork.io) that lets external systems manage submissions, modules, applications, workflows, users, groups, promotions, transforms, global variables and API access credentials in an Unqork environment. The API is served per-tenant at https://{subdomain}.unqork.io/api/1.0, secured with OAuth 2.0 client-credentials and password grants issued through API Access Management, and the platform ships on a quarterly GA release cadence with weekly patch releases.
image: https://developers.unqork.io/unqork-logo.png
layout: provider
mcp_servers:
- description: ''
  name: Unqork MCP Server
  slug: unqork-mcp-server
modified: '2026-07-31'
name: Unqork
nav: Providers
network: true
overview: 'Unqork publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Applications API, Authentication API, Credentials API, and 14 more. Tagged areas include Company, No-Code, Low-Code, Application Development, and Enterprise Software.


  The Unqork catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Unqork''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, pricing, and 26 more developer resources.'
random_paper: 0
rate_limits:
- limit_count: 2
  name: Unqork Rate Limits
  slug: unqork-rate-limits
scopes:
- name: Unqork Scopes
  scope_count: 1
  slug: unqork-scopes
  summary_line: 1 scope · clientCredentials/password
score:
  band: strong
  composite: 55.2
  coverage:
    artifact_dirs: 25
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 56.4
    developer_ergonomics: 63.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 63.2
  previous_composite: 55.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 68.2
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/unqork/refs/heads/main/screenshots/unqork-2026-08-17T082627.png
security:
- kind: authentication
  name: Unqork Authentication
  slug: unqork-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Unqork Domain Security
  slug: unqork-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Unqork Vulnerability Disclosure
  slug: unqork-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Unqork Trust Center
  slug: unqork-trust-center
  summary_line: SOC 2 Type II, ISO/IEC 27001:2013, HIPAA, FedRAMP, GDPR
slug: unqork
tags:
- Company
- No-Code
- Low-Code
- Application Development
- Enterprise Software
- Platform-as-a-Service
- Workflows
- Financial-Services
- Insurance
- Government
- Application Modernization
website: https://unqork.com/
---
