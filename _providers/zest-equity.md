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
  name: Zest Equity Agentic Access
  operation_count: 23
  slug: zest-equity-agentic-access
  summary_line: 23 operations · 7 acting
api_count: 1
apis:
- baseURL: https://public-api.zestequity.com
  baseurl_source: declared
  description: OAuth 2.0 JWT-Bearer assertion grant. Exchange a partner-signed JWT for a short-lived bearer access token, then send that token in the Authorization header on every partner API call.
  name: Zest Equity Authentication API
  slug: zest-equity-authentication-api
- baseURL: https://public-api.zestequity.com
  baseurl_source: declared
  description: Read-only access to the spaas-contract registry (templates, catalogs, primitives, samples) used to validate SPV-request `attributes`.
  name: Zest Equity Contracts API
  slug: zest-equity-contracts-api
- baseURL: https://public-api.zestequity.com
  baseurl_source: declared
  description: Bulk-create investor records with partial-success semantics. Each row carries its own status / error envelope so a single bad row never fails the batch.
  name: Zest Equity Investors API
  slug: zest-equity-investors-api
- baseURL: https://public-api.zestequity.com
  baseurl_source: declared
  description: Submit SPV creation requests, inspect their lifecycle, and cancel pending ones. SPV requests are reviewed by Zest admins and produce SPV materialisation on approval.
  name: Zest Equity SPV Requests API
  slug: zest-equity-spv-requests-api
- baseURL: https://public-api.zestequity.com
  baseurl_source: declared
  description: Upload signed subscription forms (PDF or image) for partner-managed subscriptions. Files are streamed to private storage and referenced on the Bid.
  name: Zest Equity Subscription Forms API
  slug: zest-equity-subscription-forms-api
- baseURL: https://public-api.zestequity.com
  baseurl_source: declared
  description: 'Upload wire-transfer receipts plus funding metadata. Strict order: a signed form must already be on record before fundings can be uploaded.'
  name: Zest Equity Subscription Fundings API
  slug: zest-equity-subscription-fundings-api
- baseURL: https://public-api.zestequity.com
  baseurl_source: declared
  description: Create one or more subscriptions for a single SPV.
  name: Zest Equity Subscriptions API
  slug: zest-equity-subscriptions-api
- baseURL: https://public-api.zestequity.com
  baseurl_source: declared
  description: Service health and OpenAPI introspection endpoints.
  name: Zest Equity System API
  slug: zest-equity-system-api
arazzos:
- description: Mint an access token then submit and read back a contract-validated SPV creation request.
  name: Zest — authenticate and create an SPV request
  slug: zest-equity-create-spv-request
- description: Bulk-create investors, subscribe one to an SPV, then upload the signed form and funding receipt in strict order.
  name: Zest — onboard investors and record a subscription
  slug: zest-equity-onboard-and-subscribe
artifact_total: 23
asyncapis:
- description: ''
  name: Zest Equity Webhooks
  slug: zest-equity-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Zest equity public api Authentication API
  slug: open-zest-equity-authentication-api
- collection_type: open
  name: Zest equity public api Authentication Contracts API
  slug: open-zest-equity-contracts-api
- collection_type: open
  name: Zest equity public api Authentication Investors API
  slug: open-zest-equity-investors-api
- collection_type: open
  name: Zest equity public api Authentication SPV Requests API
  slug: open-zest-equity-spv-requests-api
- collection_type: open
  name: Zest equity public api Authentication Subscription Forms API
  slug: open-zest-equity-subscription-forms-api
- collection_type: open
  name: Zest equity public api Authentication Subscription Fundings API
  slug: open-zest-equity-subscription-fundings-api
- collection_type: open
  name: Zest equity public api Authentication Subscriptions API
  slug: open-zest-equity-subscriptions-api
- collection_type: open
  name: Zest equity public api Authentication System API
  slug: open-zest-equity-system-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zest-equity-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zest-equity-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zest-equity-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/zest-equity-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/zest-equity-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/zest-equity-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/zest-equity-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/zest-equity-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/zest-equity-webhooks.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/zest-equity-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zest-equity-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/zest-equity-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/zest-equity-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://zestequity.com
- group: design
  title: ''
  type: DataModel
  url: data-model/zest-equity-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/zest-equity-sandbox.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/zest-equity-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/zest-equity-create-spv-request.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/zest-equity-onboard-and-subscribe.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.zestequity.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.zestequity.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.zestequity.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.zestequity.com/quickstart
- group: company
  title: ''
  type: Blog
  url: https://www.zestequity.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://app.zestequity.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://app.zestequity.com/sign-in
- group: operate
  title: ''
  type: Support
  url: https://www.zestequity.com/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zestequity
- group: company
  title: ''
  type: Website
  url: https://zestequity.com
created: '2026-07-17'
description: 'Zest Equity is the digital infrastructure for private-market transactions — built in MENA, used worldwide. Its SPV-as-a-Service platform lets partners create DIFC-regulated Special Purpose Vehicles, run FSRA-regulated escrow and deal-arranging, bulk-onboard investors, and process subscriptions. The Zest Public API exposes this workflow programmatically: OAuth 2.0 JWT-Bearer (RFC 7523, EdDSA) authentication, idempotent write endpoints, a versioned contract-template engine, and a nine-event HMAC-signed webhook surface — so fund managers, family offices, VCs, and PE firms can embed SPV setup, fund administration, and regulatory compliance directly inside their own product.'
image: https://cdn.prod.website-files.com/699db6380f5e26c60d1ebda3/6a31ad4a4c9ad7f045465700_favicon%20light.png
layout: provider
modified: '2026-07-21'
name: Zest Equity
nav: Providers
network: true
overview: 'Zest Equity publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Contracts API, Investors API, and 5 more. Tagged areas include Company, Fintech, Private Markets, SPV, and Investments.


  The Zest Equity catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Zest Equity''s developer surface includes authentication, changelog, sandbox, documentation, API reference, getting-started guide, engineering blog, and 23 more developer resources.'
random_paper: 17
score:
  band: developing
  composite: 48.1
  coverage:
    artifact_dirs: 21
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 61.4
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 48.1
  provenance:
    agentic_access: derived
    conformance: first-party
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
screenshot: https://raw.githubusercontent.com/api-evangelist/zest-equity/refs/heads/main/screenshots/zest-equity-2026-08-17T083105.png
security:
- kind: authentication
  name: Zest Equity Authentication
  slug: zest-equity-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Zest Equity Domain Security
  slug: zest-equity-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: zest-equity
tags:
- Company
- Fintech
- Private Markets
- SPV
- Investments
- Escrow
- Fund Administration
- MENA
- Webhook
- Regulated
website: https://zestequity.com
---
