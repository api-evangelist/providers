---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
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
  score: 27.9
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 22
  human_in_the_loop: 3
  name: Snappt Agentic Access
  operation_count: 48
  slug: snappt-agentic-access
  summary_line: 48 operations · 22 acting · 3 human-in-the-loop
api_count: 1
apis:
- baseURL: https://enterprise-api.snappt.com
  baseurl_source: declared
  description: The Account API from Snappt — 1 operation(s) for account.
  name: Snappt Account API
  slug: snappt-account-api
- baseURL: https://enterprise-api.snappt.com
  baseurl_source: declared
  description: The Applicant Sessions API from Snappt — 8 operation(s) for applicant sessions.
  name: Snappt Applicant Sessions API
  slug: snappt-applicant-sessions-api
- baseURL: https://enterprise-api.snappt.com
  baseurl_source: declared
  description: The Applicants API from Snappt — 7 operation(s) for applicants.
  name: Snappt Applicants API
  slug: snappt-applicants-api
- baseURL: https://enterprise-api.snappt.com
  baseurl_source: declared
  description: The ID Verification API from Snappt — 8 operation(s) for id verification.
  name: Snappt ID Verification API
  slug: snappt-id-verification-api
- baseURL: https://enterprise-api.snappt.com
  baseurl_source: declared
  description: The Internal IDV API from Snappt — 1 operation(s) for internal idv.
  name: Snappt Internal IDV API
  slug: snappt-internal-idv-api
- baseURL: https://enterprise-api.snappt.com
  baseurl_source: declared
  description: The Properties API from Snappt — 8 operation(s) for properties.
  name: Snappt Properties API
  slug: snappt-properties-api
- baseURL: https://enterprise-api.snappt.com
  baseurl_source: declared
  description: The Webhooks API from Snappt — 3 operation(s) for webhooks.
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
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/snappt-capability-edges.yml
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
  name: Snappt MCP Server
  slug: snappt-mcp-server
modified: '2026-08-05'
name: Snappt
nav: Providers
network: true
overview: 'Snappt publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Account API, Applicant Sessions API, Applicants API, and 4 more. Tagged areas include Company, Fraud Detection, Document Verification, Identity Verification, and Income Verification.


  The Snappt catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Snappt''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 28 more developer resources.'
random_paper: 11
score:
  band: developing
  composite: 50.9
  coverage:
    artifact_dirs: 23
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 57.3
    developer_ergonomics: 54.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 50.0
  previous_composite: 50.9
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
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
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
- Fraud Detection
- Document Verification
- Identity Verification
- Income Verification
- Property Management
- Multifamily
- Real-Estate
- PropTech
- Tenant Screening
- Rental Applications
- Webhook
website: https://snappt.com/
---
