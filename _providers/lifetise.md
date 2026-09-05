---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.1
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lifetise-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.coadjute.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/lifetise-authentication.yml
- group: other
  title: ''
  type: OpenIDConnectDiscovery
  url: https://auth.coadjute.com/.well-known/openid-configuration
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/lifetise-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/lifetise-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lifetise-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.coadjute.com/our-technology
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lifetise-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lifetise-llms.txt
- group: operate
  title: ''
  type: StatusPage
  url: https://status.coadjute.com
- group: operate
  title: ''
  type: SLA
  url: https://www.coadjute.com/incident-severity-levels-and-slas
- group: operate
  title: ''
  type: Support
  url: https://www.coadjute.com/help-centre
- group: start
  title: ''
  type: Login
  url: https://app.coadjute.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.coadjute.com/coadjute-partner-terms-of-service
- group: other
  title: ''
  type: AcceptableUsePolicy
  url: https://www.coadjute.com/coadjute-network-acceptable-use-policy
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.coadjute.com/privacy-statement
- group: commercial
  title: ''
  type: Pricing
  url: https://www.coadjute.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.coadjute.com/resources
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/coadjute
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/coadjute/
- group: operate
  title: ''
  type: Contact
  url: https://www.coadjute.com/contact-us
created: '2026-07-26'
description: 'Coadjute Ltd is a London-based property technology company that operates a shared network for the UK residential property market, connecting estate agents, conveyancers, mortgage brokers, lenders and consumers through the CRM and case-management systems they already use rather than through any multiple listing service — the UK has no MLS and no RESO adoption. Built on R3 Corda distributed ledger technology and now positioned as a fully managed AML and compliance platform for UK property, Coadjute sits in the middle of the transaction as connective infrastructure: property packs, material information, shareable AML checks and status data moving between parties. Its API posture is partner-only and not publicly reachable. Coadjute''s own Partner Terms of Service govern "the Coadjute Applet, APIs, Connector, Sandbox, DLT Application" under an Order Form and Subscription Term, and its Network Acceptable Use Policy names a "Partner Cloud API" and an "End User App Plugin" — but the
  developer portal that once published an API catalogue at developer.coadjute.com returns HTTP 502 as of 2026-07-26, api.coadjute.com answers only with authenticated JSON error envelopes, and no OpenAPI, Postman collection, SDK or public reference could be retrieved. The only publicly fetchable machine-readable contract is the Auth0-backed OpenID Connect discovery document at auth.coadjute.com. Coadjute publishes no open data; the open property-data layer in its home market belongs to HM Land Registry and Ordnance Survey, not to Coadjute.'
image: https://www.coadjute.com/hubfs/Logo.svg
layout: provider
modified: '2026-07-26'
name: Coadjute
nav: Providers
network: true
overview: 'Coadjute is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Real-Estate, United Kingdom, PropTech, Property Transactions, and Conveyancing.


  Coadjute''s developer surface includes authentication, support, pricing, engineering blog, and 18 more developer resources.'
random_paper: 13
scopes:
- name: Lifetise Scopes
  scope_count: 14
  slug: lifetise-scopes
  summary_line: 14 scopes · authorizationCode/clientCredentials/deviceCode/implicit
score:
  band: emerging
  composite: 23.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 46.1
    commercial_clarity: 46.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 23.3
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lifetise/refs/heads/main/screenshots/lifetise-2026-08-07T171648.png
security:
- kind: authentication
  name: Lifetise Authentication
  slug: lifetise-authentication
  summary_line: oauth2/openIdConnect/apiKey · 3 schemes
- kind: domain-security
  name: Lifetise Domain Security
  slug: lifetise-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lifetise
tags:
- Real-Estate
- United Kingdom
- PropTech
- Property Transactions
- Conveyancing
- AML
- Compliance
- Distributed Ledger
- Estate Agents
- Mortgage
website: https://www.coadjute.com/
---
