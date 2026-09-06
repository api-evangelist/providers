---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
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
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.2
  scored_at: '2026-09-05'
api_count: 2
apis:
- description: 'Connect a worker''s accounts and retrieve normalized income, employment, transactions, activity, assets, banking info, documents, and vehicle data across 70+ gig-economy, tax, payroll, and wallet data '
  name: Rollee User API
  slug: rollee-user-api
- description: Company-side (employer / fleet) API to manage companies and company accounts and retrieve employees, absences, employment, income, activity, banking info, documents, trips, vehicles, and wallet data f
  name: Rollee Company API
  slug: rollee-company-api
artifact_total: 7
asyncapis:
- description: ''
  name: Rollee Webhooks
  slug: rollee-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/rollee-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rollee-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.getrollee.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.getrollee.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.getrollee.com/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://developers.getrollee.com/reference/getting-started-with-your-api
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.getrollee.com/docs/getting-started
- group: company
  title: ''
  type: Blog
  url: https://www.getrollee.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.getrollee.com/contact-us
- group: start
  title: ''
  type: SignUp
  url: https://www.getrollee.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.getrollee.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getrollee.com/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rollee
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.getrollee.com/changelog
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rollee-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/rollee-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rollee-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/rollee-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/rollee-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rollee-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/rollee-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.getrollee.com/security
- group: start
  title: ''
  type: Sandbox
  url: sandbox/rollee-sandbox.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/rollee-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/rollee-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/rollee-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/rollee-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/rollee-packages.yml
- group: design
  title: ''
  type: Components
  url: components/rollee-components.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Rollee is an Open Finance / employment-data platform that lets fintechs, lenders, and HR platforms verify the income, employment, and work history of both salaried and self-employed workers in real time. Through a single API and the embeddable Rollee Connect flow, Rollee aggregates data from 70+ sources — gig-economy platforms (Uber, Bolt, Deliveroo, Just Eat, Stuart, and more), government tax portals, payroll systems, and digital wallets — and normalizes it into a common "Rollee Standard" schema covering income, transactions, employment, activity, assets, banking info, documents, and vehicles. It powers consumer lending, vehicle financing, tenant and income verification, earned-wage access, and recruitment / work-history checks. The platform is ISO 27001 certified and GDPR-compliant, and is backed by Seedcamp and Speedinvest.
image: https://www.getrollee.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Rollee MCP Server
  slug: rollee-mcp-server
modified: '2026-07-21'
name: Rollee
nav: Providers
network: true
overview: 'Rollee publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Open Finance, Income Verification, Employment Verification, and Payroll Data.


  The Rollee catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Rollee''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, changelog, and 23 more developer resources.'
random_paper: 13
score:
  band: developing
  composite: 46.5
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 57.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 15.8
  previous_composite: 46.5
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 45.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rollee/refs/heads/main/screenshots/rollee-2026-08-17T081628.png
security:
- kind: authentication
  name: Rollee Authentication
  slug: rollee-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Rollee Domain Security
  slug: rollee-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Rollee Trust Center
  slug: rollee-trust-center
  summary_line: ISO 27001, GDPR
slug: rollee
tags:
- Company
- Open Finance
- Income Verification
- Employment Verification
- Payroll Data
- Gig Economy
- Alternative Data
- Underwriting
- Lending
- Fintech
website: https://www.getrollee.com
---
