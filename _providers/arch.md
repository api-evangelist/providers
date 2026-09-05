---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
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
  score: 26.1
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Arch Agentic Access
  operation_count: 52
  slug: arch-agentic-access
  summary_line: 52 operations · 19 acting
api_count: 1
apis:
- baseURL: https://arch.co/client-api/v0
  baseurl_source: declared
  description: The Accounts API from Arch — 2 operation(s) for accounts.
  name: Arch Accounts API
  slug: arch-accounts-api
- baseURL: https://arch.co/client-api/v0
  baseurl_source: declared
  description: Interact with Arch objects representing financial updates
  name: Arch Activities API
  slug: arch-activities-api
- baseURL: https://arch.co/client-api/v0
  baseurl_source: declared
  description: The Addepar API from Arch — 1 operation(s) for addepar.
  name: Arch Addepar API
  slug: arch-addepar-api
- baseURL: https://arch.co/client-api/v0
  baseurl_source: declared
  description: The Authentication API from Arch — 1 operation(s) for authentication.
  name: Arch Authentication API
  slug: arch-authentication-api
- baseURL: https://arch.co/client-api/v0
  baseurl_source: declared
  description: Read and write data relating to money inflow / outflow
  name: Arch Cash Flows API
  slug: arch-cash-flows-api
- baseURL: https://arch.co/client-api/v0
  baseurl_source: declared
  description: Reference info about firms.
  name: Arch Firms API
  slug: arch-firms-api
- baseURL: https://arch.co/client-api/v0
  baseurl_source: declared
  description: Read holding data and push new investments.
  name: Arch Holdings API
  slug: arch-holdings-api
- baseURL: https://arch.co/client-api/v0
  baseurl_source: declared
  description: Read from and create new investing entities
  name: Arch Investing Entities API
  slug: arch-investing-entities-api
- baseURL: https://arch.co/client-api/v0
  baseurl_source: declared
  description: Read from and create new issuing entities
  name: Arch Issuing Entities API
  slug: arch-issuing-entities-api
- baseURL: https://arch.co/client-api/v0
  baseurl_source: declared
  description: Fetch data relating to the underling investments made by your own investments
  name: Arch Lookthroughs API
  slug: arch-lookthroughs-api
- baseURL: https://arch.co/client-api/v0
  baseurl_source: declared
  description: Get data on individual investment offering opportunities offered by your holdings
  name: Arch Offerings API
  slug: arch-offerings-api
- baseURL: https://arch.co/client-api/v0
  baseurl_source: declared
  description: The Tasks API from Arch — 6 operation(s) for tasks.
  name: Arch Tasks API
  slug: arch-tasks-api
- baseURL: https://arch.co/client-api/v0
  baseurl_source: declared
  description: The Tax Documents API from Arch — 4 operation(s) for tax documents.
  name: Arch Tax Documents API
  slug: arch-tax-documents-api
- baseURL: https://arch.co/client-api/v0
  baseurl_source: declared
  description: The User Roles API from Arch — 1 operation(s) for user roles.
  name: Arch User Roles API
  slug: arch-user-roles-api
- baseURL: https://arch.co/client-api/v0
  baseurl_source: declared
  description: The Users API from Arch — 2 operation(s) for users.
  name: Arch Users API
  slug: arch-users-api
artifact_total: 36
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Arch Client Accounts API
  slug: open-arch-accounts-api
- collection_type: open
  name: Arch Client Accounts Activities API
  slug: open-arch-activities-api
- collection_type: open
  name: Arch Client Accounts Addepar API
  slug: open-arch-addepar-api
- collection_type: open
  name: Arch Client Accounts Authentication API
  slug: open-arch-authentication-api
- collection_type: open
  name: Arch Client Accounts Cash Flows API
  slug: open-arch-cash-flows-api
- collection_type: open
  name: Arch Client Accounts Firms API
  slug: open-arch-firms-api
- collection_type: open
  name: Arch Client Accounts Holdings API
  slug: open-arch-holdings-api
- collection_type: open
  name: Arch Client Accounts Investing Entities API
  slug: open-arch-investing-entities-api
- collection_type: open
  name: Arch Client Accounts Issuing Entities API
  slug: open-arch-issuing-entities-api
- collection_type: open
  name: Arch Client Accounts Lookthroughs API
  slug: open-arch-lookthroughs-api
- collection_type: open
  name: Arch Client Accounts Offerings API
  slug: open-arch-offerings-api
- collection_type: open
  name: Arch Client Accounts Tasks API
  slug: open-arch-tasks-api
- collection_type: open
  name: Arch Client Accounts Tax Documents API
  slug: open-arch-tax-documents-api
- collection_type: open
  name: Arch Client Accounts User Roles API
  slug: open-arch-user-roles-api
- collection_type: open
  name: Arch Client Accounts Users API
  slug: open-arch-users-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/arch-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/arch-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/arch-authentication.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/arch-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/arch-conformance.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/arch-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/arch-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/arch-client-api-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/arch-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://archlabs.com
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
- group: operate
  title: ''
  type: Support
  url: https://archlabs.com/contact.html
- group: start
  title: ''
  type: SignUp
  url: https://archlabs.com/portal
- group: start
  title: ''
  type: Login
  url: https://archlabs.com/portal/home
- group: commercial
  title: ''
  type: TermsOfService
  url: https://arch.co/legal.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://arch.co/legal.html#privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://arch.co/legal.html#gdpr-compliance-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://arch-group.gitlab.io/status-page/
created: '2026-07-17'
description: Arch (Arch Labs, Inc.) is the digital administration platform for private markets and alternative investments. It aggregates statements, capital calls, tax documents, and data from hundreds of funds and sources into one secure portal, then uses automation and AI to extract data, summarize documents, surface insights, and coordinate workflows for limited partners, advisors, accountants, family offices, and fund service providers. The Arch Client API is a JSON HTTP REST API that lets customers programmatically access holdings, cash flows, investing/issuing entities, activities, tasks, files, and tax documents on the platform, authenticating with client-credential JWT bearer tokens. Founded in 2018, Arch is backed by Oak HC/FT, Menlo Ventures, Craft Ventures, Uncork Capital, Citi Ventures, and others.
image: https://archlabs.com/images/arch-logo.svg
layout: provider
modified: '2026-07-18'
name: Arch
nav: Providers
network: true
overview: 'Arch publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Activities API, Addepar API, and 12 more. Tagged areas include Company, Private Markets, Alternative Investments, Fintech, and Wealth Management.


  Arch''s developer surface includes authentication, documentation, API reference, getting-started guide, support, signup flow, and 16 more developer resources.'
random_paper: 15
rate_limits:
- limit_count: 0
  name: Arch Rate Limits
  slug: arch-rate-limits
score:
  band: developing
  composite: 43.6
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 4.5
    contract_quality: 48.4
    developer_ergonomics: 56.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 15.8
  previous_composite: 43.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/arch/refs/heads/main/screenshots/arch-2026-07-25T201014.png
security:
- kind: authentication
  name: Arch Authentication
  slug: arch-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Arch Domain Security
  slug: arch-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Arch Trust Center
  slug: arch-trust-center
  summary_line: trust center published
slug: arch
tags:
- Company
- Private Markets
- Alternative Investments
- Fintech
- Wealth Management
- Investment Administration
- Portfolio-Management
- Documents
website: https://archlabs.com
---
