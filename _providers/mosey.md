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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.6
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 29
  human_in_the_loop: 0
  name: Mosey Agentic Access
  operation_count: 52
  slug: mosey-agentic-access
  summary_line: 52 operations · 29 acting
api_count: 3
apis:
- baseURL: https://api.mosey.com
  baseurl_source: declared
  description: The Accounts API from Mosey — 7 operation(s) for accounts.
  name: Mosey Accounts API
  slug: mosey-accounts-api
- baseURL: https://api.mosey.com
  baseurl_source: declared
  description: The Agency Accounts API from Mosey — 2 operation(s) for agency accounts.
  name: Mosey Agency Accounts API
  slug: mosey-agency-accounts-api
- baseURL: https://api.mosey.com
  baseurl_source: declared
  description: The Auth API from Mosey — 2 operation(s) for auth.
  name: Mosey Auth API
  slug: mosey-auth-api
- baseURL: https://api.mosey.com
  baseurl_source: declared
  description: The Documents API from Mosey — 1 operation(s) for documents.
  name: Mosey Documents API
  slug: mosey-documents-api
- baseURL: https://api.mosey.com
  baseurl_source: declared
  description: The Handbook API from Mosey — 3 operation(s) for handbook.
  name: Mosey Handbook API
  slug: mosey-handbook-api
- baseURL: https://api.mosey.com
  baseurl_source: declared
  description: The Legal Entity API from Mosey — 2 operation(s) for legal entity.
  name: Mosey Legal Entity API
  slug: mosey-legal-entity-api
- baseURL: https://api.mosey.com
  baseurl_source: declared
  description: The Locations API from Mosey — 7 operation(s) for locations.
  name: Mosey Locations API
  slug: mosey-locations-api
- baseURL: https://api.mosey.com
  baseurl_source: declared
  description: The Logins API from Mosey — 4 operation(s) for logins.
  name: Mosey Logins API
  slug: mosey-logins-api
- baseURL: https://api.mosey.com
  baseurl_source: declared
  description: The Mail API from Mosey — 2 operation(s) for mail.
  name: Mosey Mail API
  slug: mosey-mail-api
- baseURL: https://api.mosey.com
  baseurl_source: declared
  description: The Regions API from Mosey — 2 operation(s) for regions.
  name: Mosey Regions API
  slug: mosey-regions-api
- baseURL: https://api.mosey.com
  baseurl_source: declared
  description: The Signup API from Mosey — 3 operation(s) for signup.
  name: Mosey Signup API
  slug: mosey-signup-api
- baseURL: https://api.mosey.com
  baseurl_source: declared
  description: The Tasks API from Mosey — 9 operation(s) for tasks.
  name: Mosey Tasks API
  slug: mosey-tasks-api
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Mosey Accounts API
  slug: open-mosey-accounts-api
- collection_type: open
  name: Mosey Accounts Agency Accounts API
  slug: open-mosey-agency-accounts-api
- collection_type: open
  name: Mosey Accounts Auth API
  slug: open-mosey-auth-api
- collection_type: open
  name: Mosey Accounts Documents API
  slug: open-mosey-documents-api
- collection_type: open
  name: Mosey Accounts Handbook API
  slug: open-mosey-handbook-api
- collection_type: open
  name: Mosey Accounts Legal Entity API
  slug: open-mosey-legal-entity-api
- collection_type: open
  name: Mosey Accounts Locations API
  slug: open-mosey-locations-api
- collection_type: open
  name: Mosey Accounts Logins API
  slug: open-mosey-logins-api
- collection_type: open
  name: Mosey Accounts Mail API
  slug: open-mosey-mail-api
- collection_type: open
  name: Mosey Accounts Regions API
  slug: open-mosey-regions-api
- collection_type: open
  name: Mosey Accounts Signup API
  slug: open-mosey-signup-api
- collection_type: open
  name: Mosey Accounts Tasks API
  slug: open-mosey-tasks-api
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/gusto/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mosey-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.mosey.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mosey.com/api-reference/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.mosey.com/api-reference/introduction
- group: company
  title: ''
  type: Blog
  url: https://mosey.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://mosey.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.mosey.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.mosey.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mosey.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mosey.com/privacy-policy/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mosey-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/mosey-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mosey-agentic-access.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/mosey-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/mosey-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/mosey-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mosey-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mosey-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mosey-conventions.yml
- group: design
  title: ''
  type: Components
  url: components/mosey-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/mosey-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Mosey is a business compliance platform that helps multi-state companies open and manage state and local tax, HR, payroll, insurance, and registration accounts. The Mosey API is a composable set of OpenAPI 3.1 endpoints that let software platforms embed state compliance into their own products: sign up or authenticate a legal entity, register the states it operates in, generate and resolve compliance tasks, receive physical mail, and securely manage state-agency logins via short-lived hosted sessions. Authentication is OAuth2 (password grant). Mosey partnered with Gusto, Stripe, and Sequoia Consulting Group and was subsequently acquired by Gusto. This profile was surfaced as a Canaan Partners portfolio company and enriched by the API Evangelist pipeline from Mosey''s public OpenAPI and developer documentation.'
image: https://mosey.com/favicon.ico
layout: provider
modified: '2026-07-20'
name: Mosey
nav: Providers
network: true
overview: 'Mosey publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Agency Accounts API, Auth API, and 9 more. Tagged areas include Company, Compliance, Regulatory Technology, State Compliance, and Tax.


  Mosey''s developer surface includes documentation, API reference, engineering blog, pricing, signup flow, authentication, and 17 more developer resources.'
random_paper: 11
score:
  band: thin
  composite: 36.8
  coverage:
    artifact_dirs: 18
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 4.5
    contract_quality: 48.1
    developer_ergonomics: 42.3
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 36.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mosey/refs/heads/main/screenshots/mosey-2026-08-07T184318.png
security:
- kind: authentication
  name: Mosey Authentication
  slug: mosey-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Mosey Domain Security
  slug: mosey-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mosey
tags:
- Company
- Compliance
- Regulatory Technology
- State Compliance
- Tax
- Payroll
- HR
- Business Operations
website: https://docs.mosey.com
---
