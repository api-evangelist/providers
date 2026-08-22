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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.7
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 22
  human_in_the_loop: 3
  name: Snappt Agentic Access
  operation_count: 48
  slug: snappt-agentic-access
  summary_line: 48 operations · 22 acting · 3 human-in-the-loop
api_count: 7
apis:
- description: The Account API from Snappt — 1 operation(s) for account.
  name: Snappt Account API
  slug: snappt-account-api
- description: The Applicant Sessions API from Snappt — 8 operation(s) for applicant sessions.
  name: Snappt Applicant Sessions API
  slug: snappt-applicant-sessions-api
- description: The Applicants API from Snappt — 7 operation(s) for applicants.
  name: Snappt Applicants API
  slug: snappt-applicants-api
- description: The ID Verification API from Snappt — 8 operation(s) for id verification.
  name: Snappt ID Verification API
  slug: snappt-id-verification-api
- description: The Internal IDV API from Snappt — 1 operation(s) for internal idv.
  name: Snappt Internal IDV API
  slug: snappt-internal-idv-api
- description: The Properties API from Snappt — 8 operation(s) for properties.
  name: Snappt Properties API
  slug: snappt-properties-api
- description: The Webhooks API from Snappt — 3 operation(s) for webhooks.
  name: Snappt Webhooks API
  slug: snappt-webhooks-api
artifact_total: 21
asyncapis:
- description: ''
  name: Snappt Enterprise Api Webhooks
  slug: snappt-enterprise-api-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Snappt Account API
  slug: open-snappt-account-api
- collection_type: open
  name: Snappt Applicant Sessions API
  slug: open-snappt-applicant-sessions-api
- collection_type: open
  name: Snappt Applicants API
  slug: open-snappt-applicants-api
- collection_type: open
  name: Snappt ID Verification API
  slug: open-snappt-id-verification-api
- collection_type: open
  name: Snappt Internal IDV API
  slug: open-snappt-internal-idv-api
- collection_type: open
  name: Snappt Properties API
  slug: open-snappt-properties-api
- collection_type: open
  name: Snappt Webhooks API
  slug: open-snappt-webhooks-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/snappt-mcp.yml
- group: company
  title: ''
  type: Website
  url: https://snappt.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://snappt-enterprise-api.readme.io/
- group: docs
  title: ''
  type: Documentation
  url: https://snappt-enterprise-api.readme.io/docs/getting-started-fraud-detection
- group: docs
  title: ''
  type: APIReference
  url: https://snappt-enterprise-api.readme.io/reference/get_account
- group: start
  title: ''
  type: GettingStarted
  url: https://snappt-enterprise-api.readme.io/docs/getting-started-fraud-detection
- group: operate
  title: ''
  type: Support
  url: https://snappt.com/contact-support/
- group: company
  title: ''
  type: Blog
  url: https://snappt.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Snappt
- group: commercial
  title: ''
  type: Pricing
  url: https://snappt.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://client.snappt.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://snappt.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://snappt.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.snappt.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/snappt-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://snappt.com/security/
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/snappt-lifecycle.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/snappt-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/snappt-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/snappt-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/snappt-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/snappt-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/snappt-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/snappt-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/snappt-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/snappt-packages.yml
- group: design
  title: ''
  type: Components
  url: components/snappt-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/snappt-sandbox.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/snappt-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/snappt-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/snappt-llms.txt
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/snappt-enterprise-api-webhooks.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/snappt-enterprise-api-overlay.yaml
created: '2026-08-05'
description: Snappt is a Los Angeles-based applicant-screening and document-fraud-detection company serving the multifamily rental and property-management industry. Its Applicant Trust Platform combines proprietary AI document forensics with human review to detect edited pay stubs and bank statements, verify applicant income from traditional and connected payroll sources, verify identity with biometric and document checks, and confirm rental payment history. Snappt exposes this to property-management systems and partners through the Snappt Enterprise API — a partner API-key-authenticated REST API covering properties, applicant sessions, document upload, fraud and income reports, ID-verification sessions and outbound webhooks — plus an embeddable browser SDK that launches the applicant verification flow as a modal inside a partner's own leasing flow.
image: https://snappt.com/wp-content/uploads/2023/05/snappt-sharing-fallback.png
layout: provider
mcp_servers:
- description: ''
  name: snappt-mcp.yml
  slug: snappt-mcpyml
modified: '2026-08-05'
name: Snappt
nav: Providers
network: true
overview: 'Snappt publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Account API, Applicant Sessions API, Applicants API, and 4 more. Tagged areas include Company, fraud-detection, document-verification, identity-verification, and income-verification.


  The Snappt catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Snappt''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 27 more developer resources.'
random_paper: 11
score:
  band: strong
  composite: 54.6
  delta: -5.1
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 30.3
    contract_quality: 59.7
    developer_ergonomics: 54.2
    discoverability: 92.6
    governance: 30.3
    operational_transparency: 50.0
  previous_composite: 59.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/snappt/refs/heads/main/screenshots/snappt-2026-08-17T081942.png
security:
- kind: authentication
  name: Snappt Authentication
  slug: snappt-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Snappt Domain Security
  slug: snappt-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Snappt Trust Center
  slug: snappt-trust-center
  summary_line: SOC 2 Type II
slug: snappt
tags:
- Company
- fraud-detection
- document-verification
- identity-verification
- income-verification
- property-management
- multifamily
- real-estate
- proptech
- tenant-screening
- rental-applications
- webhooks
website: https://snappt.com/
---
