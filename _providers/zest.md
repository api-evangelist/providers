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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.4
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Zest Agentic Access
  operation_count: 23
  slug: zest-agentic-access
  summary_line: 23 operations · 7 acting
api_count: 1
apis:
- baseURL: https://public-api.zestequity.com
  baseurl_source: declared
  description: OAuth 2.0 JWT-Bearer assertion grant. Exchange a partner-signed JWT for a short-lived bearer access token, then send that token in the Authorization header on every partner API call.
  name: Zest Authentication API
  slug: zest-authentication-api
- baseURL: https://public-api.zestequity.com
  baseurl_source: declared
  description: Read-only access to the spaas-contract registry (templates, catalogs, primitives, samples) used to validate SPV-request `attributes`.
  name: Zest Contracts API
  slug: zest-contracts-api
- baseURL: https://public-api.zestequity.com
  baseurl_source: declared
  description: Bulk-create investor records with partial-success semantics. Each row carries its own status / error envelope so a single bad row never fails the batch.
  name: Zest Investors API
  slug: zest-investors-api
- baseURL: https://public-api.zestequity.com
  baseurl_source: declared
  description: Submit SPV creation requests, inspect their lifecycle, and cancel pending ones. SPV requests are reviewed by Zest admins and produce SPV materialisation on approval.
  name: Zest SPV Requests API
  slug: zest-spv-requests-api
- baseURL: https://public-api.zestequity.com
  baseurl_source: declared
  description: Upload signed subscription forms (PDF or image) for partner-managed subscriptions. Files are streamed to private storage and referenced on the Bid.
  name: Zest Subscription Forms API
  slug: zest-subscription-forms-api
- baseURL: https://public-api.zestequity.com
  baseurl_source: declared
  description: 'Upload wire-transfer receipts plus funding metadata. Strict order: a signed form must already be on record before fundings can be uploaded.'
  name: Zest Subscription Fundings API
  slug: zest-subscription-fundings-api
- baseURL: https://public-api.zestequity.com
  baseurl_source: declared
  description: Create one or more subscriptions for a single SPV.
  name: Zest Subscriptions API
  slug: zest-subscriptions-api
- baseURL: https://public-api.zestequity.com
  baseurl_source: declared
  description: Service health and OpenAPI introspection endpoints.
  name: Zest System API
  slug: zest-system-api
artifact_total: 21
asyncapis:
- description: ''
  name: Zest Webhooks
  slug: zest-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Zest equity public api Authentication API
  slug: open-zest-authentication-api
- collection_type: open
  name: Zest equity public api Authentication Contracts API
  slug: open-zest-contracts-api
- collection_type: open
  name: Zest equity public api Authentication Investors API
  slug: open-zest-investors-api
- collection_type: open
  name: Zest equity public api Authentication SPV Requests API
  slug: open-zest-spv-requests-api
- collection_type: open
  name: Zest equity public api Authentication Subscription Forms API
  slug: open-zest-subscription-forms-api
- collection_type: open
  name: Zest equity public api Authentication Subscription Fundings API
  slug: open-zest-subscription-fundings-api
- collection_type: open
  name: Zest equity public api Authentication Subscriptions API
  slug: open-zest-subscriptions-api
- collection_type: open
  name: Zest equity public api Authentication System API
  slug: open-zest-system-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/zest-openapi-overlay.yaml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.zestequity.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.zestequity.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.zestequity.com/api-reference/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.zestequity.com/quickstart
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zest-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/zest-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/zest-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/zest-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/zest-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/zest-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/zest-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/zest-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/zest-webhooks.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/zest-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zest-agentic-access.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/zest-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/zest-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zest-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zestequity
- group: company
  title: ''
  type: Blog
  url: https://www.zestequity.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.zestequity.com/contact
- group: start
  title: ''
  type: SignUp
  url: https://app.zestequity.com/sign-in
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://app.zestequity.com/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://zestequity.com
created: '2026-07-17'
description: 'Zest Equity is a DIFC/ADGM-based provider of digital infrastructure for private-market transactions across the Middle East and North Africa. Its SPV-as-a-Service (SPaaS) platform lets partners create Cayman/DIFC Special Purpose Vehicles, run FSRA-regulated escrow, and arrange private capital deals. The Zest Public API gives partners programmatic access to the core workflow: OAuth 2.0 JWT-Bearer authentication, contract-validated SPV creation requests, bulk investor onboarding, subscription processing (signed forms + funding receipts), and nine HMAC-SHA256-signed webhook lifecycle events, with Idempotency-Key support on write endpoints and a uniform error envelope.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zest.png
layout: provider
modified: '2026-07-21'
name: Zest
nav: Providers
network: true
overview: 'Zest publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Contracts API, Investors API, and 5 more. Tagged areas include Company, SPV, Private Markets, Fintech, and Equity.


  The Zest catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Zest''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, sandbox, engineering blog, and 19 more developer resources.'
random_paper: 13
score:
  band: developing
  composite: 44.9
  coverage:
    artifact_dirs: 21
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 4.5
    contract_quality: 61.4
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 26.3
  previous_composite: 44.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zest/refs/heads/main/screenshots/zest-2026-08-17T083101.png
security:
- kind: authentication
  name: Zest Authentication
  slug: zest-authentication
  summary_line: http/oauth2 · 1 scheme
- kind: domain-security
  name: Zest Domain Security
  slug: zest-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: zest
tags:
- Company
- SPV
- Private Markets
- Fintech
- Equity
- Investors
- Escrow
- SPaaS
- MENA
website: https://zestequity.com
---
