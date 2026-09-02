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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.3
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The Accounts API from Arch Labs — 2 operation(s) for accounts.
  name: Arch Labs Accounts API
  slug: arch-labs-accounts-api
- description: Interact with Arch objects representing financial updates
  name: Arch Labs Activities API
  slug: arch-labs-activities-api
- description: The Addepar API from Arch Labs — 1 operation(s) for addepar.
  name: Arch Labs Addepar API
  slug: arch-labs-addepar-api
- description: The Authentication API from Arch Labs — 1 operation(s) for authentication.
  name: Arch Labs Authentication API
  slug: arch-labs-authentication-api
- description: Read and write data relating to money inflow / outflow
  name: Arch Labs Cash Flows API
  slug: arch-labs-cash-flows-api
- description: Reference info about firms.
  name: Arch Labs Firms API
  slug: arch-labs-firms-api
- description: Read holding data and push new investments.
  name: Arch Labs Holdings API
  slug: arch-labs-holdings-api
- description: Read from and create new investing entities
  name: Arch Labs Investing Entities API
  slug: arch-labs-investing-entities-api
- description: Read from and create new issuing entities
  name: Arch Labs Issuing Entities API
  slug: arch-labs-issuing-entities-api
- description: Fetch data relating to the underling investments made by your own investments
  name: Arch Labs Lookthroughs API
  slug: arch-labs-lookthroughs-api
- description: Get data on individual investment offering opportunities offered by your holdings
  name: Arch Labs Offerings API
  slug: arch-labs-offerings-api
- description: The Tasks API from Arch Labs — 6 operation(s) for tasks.
  name: Arch Labs Tasks API
  slug: arch-labs-tasks-api
- description: The Tax Documents API from Arch Labs — 4 operation(s) for tax documents.
  name: Arch Labs Tax Documents API
  slug: arch-labs-tax-documents-api
- description: The User Roles API from Arch Labs — 1 operation(s) for user roles.
  name: Arch Labs User Roles API
  slug: arch-labs-user-roles-api
- description: The Users API from Arch Labs — 2 operation(s) for users.
  name: Arch Labs Users API
  slug: arch-labs-users-api
artifact_total: 36
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Arch Client Accounts API
  slug: open-arch-labs-accounts-api
- collection_type: open
  name: Arch Client Accounts Activities API
  slug: open-arch-labs-activities-api
- collection_type: open
  name: Arch Client Accounts Addepar API
  slug: open-arch-labs-addepar-api
- collection_type: open
  name: Arch Client Accounts Authentication API
  slug: open-arch-labs-authentication-api
- collection_type: open
  name: Arch Client Accounts Cash Flows API
  slug: open-arch-labs-cash-flows-api
- collection_type: open
  name: Arch Client Accounts Firms API
  slug: open-arch-labs-firms-api
- collection_type: open
  name: Arch Client Accounts Holdings API
  slug: open-arch-labs-holdings-api
- collection_type: open
  name: Arch Client Accounts Investing Entities API
  slug: open-arch-labs-investing-entities-api
- collection_type: open
  name: Arch Client Accounts Issuing Entities API
  slug: open-arch-labs-issuing-entities-api
- collection_type: open
  name: Arch Client Accounts Lookthroughs API
  slug: open-arch-labs-lookthroughs-api
- collection_type: open
  name: Arch Client Accounts Offerings API
  slug: open-arch-labs-offerings-api
- collection_type: open
  name: Arch Client Accounts Tasks API
  slug: open-arch-labs-tasks-api
- collection_type: open
  name: Arch Client Accounts Tax Documents API
  slug: open-arch-labs-tax-documents-api
- collection_type: open
  name: Arch Client Accounts User Roles API
  slug: open-arch-labs-user-roles-api
- collection_type: open
  name: Arch Client Accounts Users API
  slug: open-arch-labs-users-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/arch-labs-capability-edges.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/arch-labs-collect-tax-documents.md
- group: agent
  title: ''
  type: MCPServer
  url: mcp/arch-labs-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/arch-labs-client-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://arch.co
- group: start
  title: ''
  type: DeveloperPortal
  url: https://arch.co/client-api/api-docs/
- group: docs
  title: ''
  type: Documentation
  url: https://arch.co/client-api/api-docs/
- group: docs
  title: ''
  type: APIReference
  url: https://arch.co/client-api/api-docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://arch.co/client-api/api-docs/
- group: auth
  title: ''
  type: Authentication
  url: authentication/arch-labs-authentication.yml
- group: operate
  title: ''
  type: Support
  url: https://arch.co/contact.html
- group: start
  title: ''
  type: SignUp
  url: https://arch.co/portal
- group: start
  title: ''
  type: Login
  url: https://arch.co/portal
- group: commercial
  title: ''
  type: TermsOfService
  url: https://arch.co/legal.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://arch.co/legal.html#privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://arch-group.gitlab.io/status-page/
- group: auth
  title: ''
  type: Security
  url: https://arch.co/vulnerabilitydisclosure.html
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/arch-labs-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.arch.co/
- group: auth
  title: ''
  type: Compliance
  url: https://arch.co/security.html
- group: auth
  title: ''
  type: DomainSecurity
  url: security/arch-labs-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/arch-labs-conformance.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/archsoftware/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/gotk1s
created: '2026-07-17'
description: Arch (Arch Labs, Inc.) is a private-markets infrastructure platform that centralizes the administration of alternative investments for individual investors, wealth managers, family offices, institutional allocators, CPAs, fund managers and their advisors. Acting as a "portal of portals," Arch collects and classifies investment correspondence, parses account statements and cash flows, automates capital-call and distribution workflows, tracks tax-document deadlines, and produces standardized portfolio views and AI-generated manager-update summaries across private credit, real estate, venture capital, hedge funds and private equity. Its Client API exposes holdings, investing/issuing entities, activities, cash flows, tasks, tax documents, user roles and Addepar exports, and it integrates with Addepar, Salesforce and Bipsync. Backed by Craft Ventures, Menlo Ventures, Oak HC/FT and others.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/arch-labs.png
layout: provider
mcp_servers:
- description: ''
  name: Arch Labs MCP Server
  slug: arch-labs-mcp-server
modified: '2026-07-18'
name: Arch Labs
nav: Providers
network: true
overview: 'Arch Labs publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Activities API, Addepar API, and 12 more. Tagged areas include Company, Fintech, Alternative Investments, Private Markets, and Wealth Management.


  Arch Labs'' developer surface includes documentation, API reference, getting-started guide, authentication, support, signup flow, and 18 more developer resources.'
random_paper: 16
score:
  band: developing
  composite: 45.8
  coverage:
    artifact_dirs: 16
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 46.1
    commercial_clarity: 46.1
    contract_governance: 18.2
    contract_quality: 48.4
    developer_ergonomics: 56.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 45.8
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/arch-labs/refs/heads/main/screenshots/arch-labs-2026-07-25T201015.png
security:
- kind: authentication
  name: Arch Labs Authentication
  slug: arch-labs-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Arch Labs Domain Security
  slug: arch-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Arch Labs Vulnerability Disclosure
  slug: arch-labs-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Arch Labs Trust Center
  slug: arch-labs-trust-center
  summary_line: SOC 2
slug: arch-labs
tags:
- Company
- Fintech
- Alternative Investments
- Private Markets
- Wealth Management
- Investment Management
- Financial-Services
- Data Aggregation
website: https://arch.co
---
