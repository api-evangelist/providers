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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.3
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Open Insurance Agentic Access
  operation_count: 1
  slug: open-insurance-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: Open's browser JavaScript library for embedding insurance into a partner's web app. Documented methods are opensdk.quote.load, opensdk.quote.prepare, opensdk.quote.portal, opensdk.quote.status, opensd
  name: Open.js Embedded Insurance SDK
  slug: open-js-embedded-insurance-sdk
- baseURL: https://api.beopen.com
  baseurl_source: declared
  description: The Policy API from Open — 1 operation(s) for policy.
  name: Open Policy API
  slug: open-insurance-policy-api
artifact_total: 6
collections:
- collection_type: open
  name: Open Insurance API
  slug: open-open-insurance-certificate-of-currency
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/open-insurance-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/open-insurance-certificate-of-currency-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/open-insurance-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/open-insurance-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.beopen.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.beopen.com/docs/welcome
- group: docs
  title: ''
  type: APIReference
  url: https://developers.beopen.com/reference
- group: auth
  title: ''
  type: Authentication
  url: https://developers.beopen.com/docs/keys
- group: design
  title: ''
  type: ErrorCodes
  url: https://developers.beopen.com/docs/errors
- group: operate
  title: ''
  type: Status
  url: https://developers.beopen.com/docs/check-service-status
- group: agent
  title: ''
  type: LLMsTxt
  url: https://developers.beopen.com/llms.txt
- group: start
  title: ''
  type: Portal
  url: https://insurance.beopen.com/
- group: operate
  title: ''
  type: Contact
  url: https://www.beopen.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.beopen.com/terms/australia
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/beopen
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.beopen.com/docs/welcome
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.beopen.com/docs/using-openjs
- group: operate
  title: ''
  type: Support
  url: https://www.beopen.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.beopen.com/research
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.beopen.com/terms/australia
- group: start
  title: ''
  type: Login
  url: https://insurance.beopen.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://developers.beopen.com/docs/check-service-status
- group: auth
  title: ''
  type: Compliance
  url: https://www.beopen.com/terms/australia
- group: auth
  title: ''
  type: Authentication
  url: authentication/open-insurance-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/open-insurance-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/open-insurance-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/open-insurance-decline-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/open-insurance-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/open-insurance-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/open-insurance-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/open-insurance-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/open-insurance-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/open-insurance-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/open-insurance-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/open-insurance-well-known.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/open-insurance-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/open-insurance-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/open-insurance-llms.txt
created: '2026-07-25'
description: Open Insurance Pty Limited (ABN 23 166 949 444, AFSL 451712), trading as Open, is an Australian insurtech and underwriting agency that packages car, home and contents, landlord and travel cover as an embedded product other brands can sell. Open is not a carrier — it holds a binding authority from the insurer, acts as the insurer's agent to issue, vary, renew and cancel policies and to handle claims, and appoints partner brands as authorised representatives. Huddle Insurance is a business name of Open, and partner programs include Bupa and the SuperSaveClub marketplace; the business also operates in the United Kingdom and New Zealand from its Australian home market. Its API posture is real but narrow and partner-gated. Open runs a public, unauthenticated ReadMe developer hub at developers.beopen.com covering the Open.js browser SDK, the Open.Widget embed and a URL-handover redirect, plus exactly one documented server-side REST operation — POST /v1/policy/coc, Retrieve a Certificate
  of Currency — for which a real OpenAPI 3.0.3 definition is published. Quote is only prepared and polled through the SDK; bind, issue, policy servicing and claims all happen inside Open's hosted (optionally white-labelled) journey rather than over an API, and there is no public FNOL, webhook, GraphQL or Postman surface. API keys and secrets are issued by Open at partner account creation — there is no self-serve signup — and no ACORD, AL3 or NGDS reference appears anywhere on the site or in the documentation.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: Open
nav: Providers
network: true
overview: 'Open publishes 1 API on the [APIs.io](https://apis.io/) network: Policy API. Tagged areas include Insurance, Australia, Insurtech, Embedded Insurance, and Property and Casualty.


  Open''s developer surface includes documentation, API reference, authentication, status page, developer portal, getting-started guide, support, and 32 more developer resources.'
random_paper: 19
score:
  band: developing
  composite: 44.0
  coverage:
    artifact_dirs: 21
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 45.6
    developer_ergonomics: 53.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 44.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 45.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/open-insurance/refs/heads/main/screenshots/open-insurance-2026-08-07T190517.png
security:
- kind: authentication
  name: Open Insurance Authentication
  slug: open-insurance-authentication
  summary_line: apiKey/jwt-bearer (deprecated) · 5 schemes
- kind: domain-security
  name: Open Insurance Domain Security
  slug: open-insurance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: open-insurance
tags:
- Insurance
- Australia
- Insurtech
- Embedded Insurance
- Property and Casualty
- Travel Insurance
- Underwriting
- Policy Administration
- White Label
- Quotes
website: https://www.beopen.com/
---
