---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.6
  scored_at: '2026-11-06'
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
artifact_total: 23
collections:
- collection_type: open
  name: PropertyMe
  slug: open-propertyme
common:
- group: commercial
  href: https://artifacts.apis.io/propertyme/plans/propertyme-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/propertyme-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/propertyme/capabilities/propertyme-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/propertyme-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/propertyme/agentic-access/propertyme-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/propertyme-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/propertyme/security/propertyme-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/propertyme-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/propertyme/authentication/propertyme-authentication.yml
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
  href: https://artifacts.apis.io/propertyme/authentication/propertyme-openid-configuration.json
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
  href: https://artifacts.apis.io/propertyme/well-known/propertyme-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/propertyme-well-known.yml
- group: auth
  href: https://artifacts.apis.io/propertyme/scopes/propertyme-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/propertyme-scopes.yml
- group: design
  href: https://artifacts.apis.io/propertyme/conformance/propertyme-conformance.yml
  title: ''
  type: Conformance
  url: conformance/propertyme-conformance.yml
- group: design
  href: https://artifacts.apis.io/propertyme/errors/propertyme-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/propertyme-problem-types.yml
- group: design
  href: https://artifacts.apis.io/propertyme/lifecycle/propertyme-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/propertyme-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/propertyme/conventions/propertyme-conventions.yml
  title: ''
  type: Conventions
  url: conventions/propertyme-conventions.yml
- group: design
  href: https://artifacts.apis.io/propertyme/data-model/propertyme-data-model.yml
  title: ''
  type: DataModel
  url: data-model/propertyme-data-model.yml
- group: agent
  href: https://artifacts.apis.io/propertyme/mcp/propertyme-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/propertyme-mcp.yml
- group: build
  href: https://artifacts.apis.io/propertyme/mcp/propertyme-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/propertyme-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/propertyme/llms/propertyme-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/propertyme-llms.txt
- group: other
  href: https://artifacts.apis.io/propertyme/overlays/propertyme-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/propertyme-openapi-overlay.yaml
- group: build
  href: https://artifacts.apis.io/propertyme/packages/propertyme-packages.yml
  title: ''
  type: Packages
  url: packages/propertyme-packages.yml
- group: agent
  href: https://artifacts.apis.io/propertyme/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/propertyme/arazzo/propertyme-connect-and-sync.yml
  title: ''
  type: Arazzo
  url: arazzo/propertyme-connect-and-sync.yml
- group: design
  href: https://artifacts.apis.io/propertyme/arazzo/propertyme-maintenance-job.yml
  title: ''
  type: Arazzo
  url: arazzo/propertyme-maintenance-job.yml
- group: design
  href: https://artifacts.apis.io/propertyme/arazzo/propertyme-inspection-cycle.yml
  title: ''
  type: Arazzo
  url: arazzo/propertyme-inspection-cycle.yml
created: '2026-07-26'
description: PropertyMe is an Australian cloud property management and trust accounting platform for residential real estate agencies, founded in 2013 and operated by MePay Holdings Pty Ltd (AFCA member ID 81095, AFS licence no. 528836), with roughly 1.7 million properties under management across Australia and New Zealand. In the Australian property value chain it sits on the PROPERTY MANAGEMENT rail rather than the listing or settlement rails — it does not operate a portal like REA Group's realestate.com.au or Domain, and it is not a PEXA conveyancing participant; it is the system of record for the rental portfolio, holding lots, tenancies, owners, tenants, suppliers, trust transactions, inspections, maintenance jobs and documents, plus its own MePay payments product and the Grow CRM and AiMe assistant products. Its API posture is unusually honest for this sector — the machine-readable contract is genuinely open while the credentials are not. A Swagger 2.0 document describing 75 paths,
  86 operations and 296 definitions is served anonymously with no login at https://app.propertyme.com/api/openapi.json, rendered by a public Swagger UI at https://app.propertyme.com/api/swagger-ui/, and the OpenID Connect discovery document at https://login.propertyme.com is also served anonymously and advertises the full scope list. But no self-serve developer signup, app registration route or public client-credential issuance path exists anywhere on propertyme.com.au, app.propertyme.com or any developer/developers/docs/api subdomain (none of which resolve); a developer must approach PropertyMe to be issued an OAuth client_id and client_secret, and every call is additionally scoped to one customer's portfolio that the agency itself connects and can disconnect. RESO is absent — PropertyMe does not appear in the RESO certification directory, there is no OData service, no $metadata document and no Universal Property Identifier, which is the expected Australian answer because RESO is a North
  American NAR/MLS construct with no Australian counterpart. PropertyMe publishes no open data.
finops:
- has_sources: true
  method: derived
  name: Propertyme Finops
  primary_unit: 100 properties
  service_category: ''
  slug: propertyme-finops
  template: false
image: https://www.propertyme.com.au/wp-content/themes/PropertyMe/assets/dist/favicons/android-icon-192x192.png
layout: provider
modified: '2026-07-26'
name: PropertyMe
nav: Providers
network: true
overview: 'PropertyMe publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Connection API, Scope: Activities API, Scope: Bills API, and 3 more. Tagged areas include Real Estate, Australia, Property Management, Rentals, and PropTech.


  The PropertyMe catalog on APIs.io includes 1 Spectral governance ruleset.


  PropertyMe''s developer surface includes authentication, documentation, API reference, signup flow, pricing, support, engineering blog, and 35 more developer resources.'
plans:
- name: Propertyme Plans Pricing
  plan_count: 12
  slug: propertyme-plans-pricing
- name: Propertyme Price Estimates
  plan_count: 0
  slug: propertyme-price-estimates
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 96
  extends:
  - spectral:oas
  name: PropertyMe API Rules
  rule_count: 55
  severity_counts:
    error: 49
    hint: 0
    info: 1
    warn: 5
  slug: propertyme-rules
scopes:
- name: Propertyme Scopes
  scope_count: 20
  slug: propertyme-scopes
  summary_line: 20 scopes · authorizationCode/clientCredentials/deviceCode/ciba
score:
  band: developing
  composite: 52.2
  coverage:
    artifact_dirs: 29
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.3
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 54.3
    developer_ergonomics: 37.5
    discoverability: 73.2
    operational_transparency: 28.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    - new-zealand
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 50.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 31.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/propertyme/propertyme-2026-07-27T125353.png
security:
- kind: authentication
  name: Propertyme Authentication
  slug: propertyme-authentication
  summary_line: openIdConnect/oauth2/http · 2 schemes
- kind: domain-security
  name: Propertyme Domain Security
  slug: propertyme-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 5
skills:
- name: Connect a PropertyMe portfolio and keep it in sync
  slug: propertyme-connect-and-sync-portfolio
- name: Schedule, conduct and close a PropertyMe inspection
  slug: propertyme-inspection-lifecycle
- name: Run a PropertyMe maintenance job end to end
  slug: propertyme-maintenance-job-lifecycle
- name: Post a supplier bill to the PropertyMe trust ledger
  slug: propertyme-post-supplier-bill
- name: Review PropertyMe tenancies and arrears
  slug: propertyme-tenancy-arrears-review
slug: propertyme
tags:
- Real Estate
- Australia
- Property Management
- Rentals
- PropTech
- Tenancy
- Trust Accounting
- Inspection
- Maintenance
- Documents
- Payments
- New Zealand
website: https://www.propertyme.com.au/
---
