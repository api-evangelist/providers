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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.9
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 38
  human_in_the_loop: 0
  name: Propertyme Agentic Access
  operation_count: 86
  slug: propertyme-agentic-access
  summary_line: 86 operations · 38 acting
api_count: 1
apis:
- baseURL: https://app.propertyme.com/api
  baseurl_source: declared
  description: The Connection API from PropertyMe — 1 operation(s) for connection.
  name: PropertyMe Connection API
  slug: propertyme-connection-api
- baseURL: https://app.propertyme.com/api
  baseurl_source: declared
  description: 'The Scope: Activities API from PropertyMe — 43 operation(s) for scope: activities.'
  name: 'PropertyMe Scope: Activities API'
  slug: propertyme-scope-activities-api
- baseURL: https://app.propertyme.com/api
  baseurl_source: declared
  description: 'The Scope: Bills API from PropertyMe — 2 operation(s) for scope: bills.'
  name: 'PropertyMe Scope: Bills API'
  slug: propertyme-scope-bills-api
- baseURL: https://app.propertyme.com/api
  baseurl_source: declared
  description: 'The Scope: Contacts API from PropertyMe — 11 operation(s) for scope: contacts.'
  name: 'PropertyMe Scope: Contacts API'
  slug: propertyme-scope-contacts-api
- baseURL: https://app.propertyme.com/api
  baseurl_source: declared
  description: 'The Scope: Messages API from PropertyMe — 1 operation(s) for scope: messages.'
  name: 'PropertyMe Scope: Messages API'
  slug: propertyme-scope-messages-api
- baseURL: https://app.propertyme.com/api
  baseurl_source: declared
  description: 'The Scope: Properties API from PropertyMe — 17 operation(s) for scope: properties.'
  name: 'PropertyMe Scope: Properties API'
  slug: propertyme-scope-properties-api
arazzos:
- description: 'PropertyMe publishes no webhooks, so an integration keeps a portfolio current by polling the six change-since collections with an int64 Timestamp cursor. This workflow seeds the mirror from Timestamp '
  name: Connect a PropertyMe portfolio and run a change-since sync
  slug: propertyme-connect-and-sync
- description: The routine and entry/exit inspection lifecycle. Requires activity:read for the reads and activity:write for every transition. The permitted transition graph is not published, so each step reads curre
  name: Schedule, conduct, report and close a PropertyMe inspection
  slug: propertyme-inspection-cycle
- description: The maintenance work-order flow, using the v2 job-task shape for create and read and the shared v1 sub-resources for quotations, transitions and attachments. Requires activity:read and activity:write,
  name: Raise, quote, approve and complete a PropertyMe maintenance job
  slug: propertyme-maintenance-job
artifact_total: 14
collections:
- collection_type: open
  name: PropertyMe
  slug: open-propertyme
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/propertyme-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/propertyme-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/propertyme-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/propertyme-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.propertyme.com.au/
- group: company
  title: ''
  type: About
  url: https://www.propertyme.com.au/about
- group: docs
  title: ''
  type: Documentation
  url: https://app.propertyme.com/api/swagger-ui/
- group: docs
  title: ''
  type: APIReference
  url: https://app.propertyme.com/api/swagger-ui/
- group: docs
  title: ''
  type: OpenAPI
  url: https://app.propertyme.com/api/openapi.json
- group: other
  title: ''
  type: OpenIDConnect
  url: authentication/propertyme-openid-configuration.json
- group: start
  title: ''
  type: SignUp
  url: https://www.propertyme.com.au/request-a-demo
- group: commercial
  title: ''
  type: Pricing
  url: https://www.propertyme.com.au/pricing
- group: auth
  title: ''
  type: Security
  url: https://www.propertyme.com.au/security
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.propertyme.com.au/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.propertyme.com.au/privacy
- group: operate
  title: ''
  type: Support
  url: https://support.propertyme.com/hc/en-us
- group: operate
  title: ''
  type: StatusPage
  url: https://status.propertyme.com/
- group: company
  title: ''
  type: Blog
  url: https://www.propertyme.com.au/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.propertyme.com.au/feed
- group: company
  title: ''
  type: Partners
  url: https://www.propertyme.com.au/partner-directory
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PropertyMe
- group: build
  title: ''
  type: SampleCode
  url: https://github.com/PropertyMe/HelloPropertyMe.NET
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/propertyme
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UC99HN1NFPAYyXvyKyRhHkJQ
- group: operate
  title: ''
  type: Contact
  url: https://www.propertyme.com.au/contact
- group: agent
  title: ''
  type: WellKnown
  url: well-known/propertyme-well-known.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/propertyme-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/propertyme-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/propertyme-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/propertyme-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/propertyme-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/propertyme-data-model.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/propertyme-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/propertyme-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/propertyme-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/propertyme-openapi-overlay.yaml
- group: build
  title: ''
  type: Packages
  url: packages/propertyme-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/propertyme-connect-and-sync.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/propertyme-maintenance-job.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/propertyme-inspection-cycle.yml
created: '2026-07-26'
description: PropertyMe is an Australian cloud property management and trust accounting platform for residential real estate agencies, founded in 2013 and operated by MePay Holdings Pty Ltd (AFCA member ID 81095, AFS licence no. 528836), with roughly 1.7 million properties under management across Australia and New Zealand. In the Australian property value chain it sits on the PROPERTY MANAGEMENT rail rather than the listing or settlement rails — it does not operate a portal like REA Group's realestate.com.au or Domain, and it is not a PEXA conveyancing participant; it is the system of record for the rental portfolio, holding lots, tenancies, owners, tenants, suppliers, trust transactions, inspections, maintenance jobs and documents, plus its own MePay payments product and the Grow CRM and AiMe assistant products. Its API posture is unusually honest for this sector — the machine-readable contract is genuinely open while the credentials are not. A Swagger 2.0 document describing 75 paths,
  86 operations and 296 definitions is served anonymously with no login at https://app.propertyme.com/api/openapi.json, rendered by a public Swagger UI at https://app.propertyme.com/api/swagger-ui/, and the OpenID Connect discovery document at https://login.propertyme.com is also served anonymously and advertises the full scope list. But no self-serve developer signup, app registration route or public client-credential issuance path exists anywhere on propertyme.com.au, app.propertyme.com or any developer/developers/docs/api subdomain (none of which resolve); a developer must approach PropertyMe to be issued an OAuth client_id and client_secret, and every call is additionally scoped to one customer's portfolio that the agency itself connects and can disconnect. RESO is absent — PropertyMe does not appear in the RESO certification directory, there is no OData service, no $metadata document and no Universal Property Identifier, which is the expected Australian answer because RESO is a North
  American NAR/MLS construct with no Australian counterpart. PropertyMe publishes no open data.
image: https://www.propertyme.com.au/wp-content/themes/PropertyMe/assets/dist/favicons/android-icon-192x192.png
layout: provider
modified: '2026-07-26'
name: PropertyMe
nav: Providers
network: true
overview: 'PropertyMe publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Connection API, Scope: Activities API, Scope: Bills API, and 3 more. Tagged areas include Real-Estate, Australia, Property Management, Rentals, and PropTech.


  PropertyMe''s developer surface includes authentication, documentation, API reference, signup flow, pricing, support, engineering blog, and 34 more developer resources.'
random_paper: 19
scopes:
- name: Propertyme Scopes
  scope_count: 20
  slug: propertyme-scopes
  summary_line: 20 scopes · authorizationCode/clientCredentials/deviceCode/ciba
score:
  band: developing
  composite: 45.2
  coverage:
    artifact_dirs: 21
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 54.3
    developer_ergonomics: 37.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 28.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 45.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 54.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/propertyme/refs/heads/main/screenshots/propertyme-2026-07-27T125353.png
security:
- kind: authentication
  name: Propertyme Authentication
  slug: propertyme-authentication
  summary_line: openIdConnect/oauth2/http · 2 schemes
- kind: domain-security
  name: Propertyme Domain Security
  slug: propertyme-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: propertyme
tags:
- Real-Estate
- Australia
- Property Management
- Rentals
- PropTech
- Tenancy
- Trust Accounting
- Inspections
- Maintenance
- Documents
- Payments
- New Zealand
website: https://www.propertyme.com.au/
---
