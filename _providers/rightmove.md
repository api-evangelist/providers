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
  - rate-limits
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
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.1
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Rightmove Agentic Access
  operation_count: 4
  slug: rightmove-agentic-access
  summary_line: 4 operations · 2 acting
api_count: 1
apis:
- description: The Real Time Data Feed (RTDF) is Rightmove's incremental HTTPS/JSON interface for UK sales, lettings and overseas sales listings, used by estate agency CRM and feed provider software rather than by e
  name: Rightmove Real Time Data Feed API
  slug: rightmove-real-time-data-feed-api
- baseURL: https://api-services.rightmove.co.uk
  baseurl_source: declared
  description: Create, Updated, Remove and Retrieve properties
  name: Rightmove Property API
  slug: rightmove-property-api
artifact_total: 11
collections:
- collection_type: open
  name: Commercial Listings API
  slug: open-rightmove-commercial-listings
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://www.rightmove.co.uk/news/feed/
- group: other
  href: https://artifacts.apis.io/rightmove/capabilities/rightmove-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/rightmove-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/rightmove/mcp/rightmove-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/rightmove-mcp.yml
- group: agent
  href: https://artifacts.apis.io/rightmove/agentic-access/rightmove-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/rightmove-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/rightmove/security/rightmove-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rightmove-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/rightmove/scopes/rightmove-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/rightmove-scopes.yml
- group: auth
  href: https://artifacts.apis.io/rightmove/authentication/rightmove-authentication.yml
  title: ''
  type: Authentication
  url: authentication/rightmove-authentication.yml
- group: design
  href: https://artifacts.apis.io/rightmove/conventions/rightmove-conventions.yml
  title: ''
  type: Conventions
  url: conventions/rightmove-conventions.yml
- group: design
  href: https://artifacts.apis.io/rightmove/conventions/rightmove-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/rightmove-conventions.yml
- group: design
  href: https://artifacts.apis.io/rightmove/errors/rightmove-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/rightmove-problem-types.yml
- group: operate
  href: https://artifacts.apis.io/rightmove/rate-limits/rightmove-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/rightmove-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/rightmove/lifecycle/rightmove-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/rightmove-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/rightmove/changelog/rightmove-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/rightmove-changelog.yml
- group: design
  href: https://artifacts.apis.io/rightmove/data-model/rightmove-data-model.yml
  title: ''
  type: DataModel
  url: data-model/rightmove-data-model.yml
- group: design
  href: https://artifacts.apis.io/rightmove/conformance/rightmove-conformance.yml
  title: ''
  type: Conformance
  url: conformance/rightmove-conformance.yml
- group: start
  href: https://artifacts.apis.io/rightmove/sandbox/rightmove-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/rightmove-sandbox.yml
- group: build
  href: https://artifacts.apis.io/rightmove/packages/rightmove-packages.yml
  title: ''
  type: Packages
  url: packages/rightmove-packages.yml
- group: agent
  href: https://artifacts.apis.io/rightmove/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/rightmove/llms/rightmove-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/rightmove-llms.txt
- group: other
  href: https://artifacts.apis.io/rightmove/overlays/rightmove-commercial-listings-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/rightmove-commercial-listings-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.rightmove.co.uk/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-docs.rightmove.co.uk/
- group: docs
  title: ''
  type: Documentation
  url: https://www.rightmove.co.uk/adf.html
- group: docs
  title: ''
  type: Specification
  url: https://media.rightmove.co.uk/ps/pdf/guides/ADF_V4n_specification.pdf
- group: commercial
  title: ''
  type: License
  url: https://media.rightmove.co.uk/ps/pdf/guides/adf/RTDF_EULA.pdf
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rightmove.co.uk/c/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rightmove.co.uk/c/privacy-policy/
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.rightmove.co.uk/apis
- group: start
  title: ''
  type: GettingStarted
  url: https://api-docs.rightmove.co.uk/get-started
- group: start
  title: ''
  type: SignUp
  url: https://api-docs.rightmove.co.uk/accounts/create
- group: start
  title: ''
  type: Onboarding
  url: https://media.rightmove.co.uk/ps/pdf/guides/adf/Provider_Contact_Form.pdf
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rightmove
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rightmove
- group: company
  title: ''
  type: InvestorRelations
  url: https://plc.rightmove.co.uk/
- group: company
  title: ''
  type: Blog
  url: https://www.rightmove.co.uk/news/
- group: operate
  title: ''
  type: Support
  url: mailto:adfsupport@rightmove.co.uk
created: '2026-07-26'
description: Rightmove is the United Kingdom's largest residential property portal, operated by Rightmove Group Limited (Milton Keynes) and listed on the London Stock Exchange as Rightmove plc. It aggregates for-sale, to-let, new-homes, commercial and overseas listings supplied by member estate agents, letting agents and new-homes developers, and monetises the audience by charging those agents for advertising rather than by licensing data. The UK has no MLS, so Rightmove sits at the demand end of the value chain and its inbound feeds — not any cooperative database — are the machine-readable surface. Its API posture is publish-in, not read-out - the documented APIs let an agent's CRM or feed provider push listings into Rightmove, and there is no public API for reading listings, sold prices or valuations. A public Apigee developer portal at api-docs.rightmove.co.uk ("Rightmove APIs - Early adopters") anonymously serves a real OpenAPI 3.0.1 contract for the Commercial Listings API, and www.rightmove.co.uk/adf.html
  publishes the Real Time Data Feed specification, but working credentials for every environment are issued case by case by the Rightmove Data Feed Team and use is governed by a binding End User Licence Agreement. No RESO Web API or Data Dictionary certification, OData `$metadata` document or Universal Property Identifier appears anywhere in Rightmove's surface - RESO is a North American, NAR-driven standard with no UK counterpart, and Rightmove uses its own proprietary ADF/RTDF schema instead.
image: https://media.rightmove.co.uk/assets/shared-assets/favicons/light/favicon.ico
layout: provider
modified: '2026-10-06'
name: Rightmove
nav: Providers
network: true
overview: 'Rightmove publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Property API, and 1 more. Tagged areas include Real Estate, United Kingdom, Property Listings, Property Portal, and PropTech.


  Rightmove''s developer surface includes authentication, changelog, sandbox, documentation, API reference, getting-started guide, signup flow, and 29 more developer resources.'
random_paper: 21
rate_limits:
- limit_count: 0
  name: Rightmove Rate Limits
  slug: rightmove-rate-limits
scopes:
- name: Rightmove Scopes
  scope_count: 1
  slug: rightmove-scopes
  summary_line: 1 scope · implicit
score:
  band: developing
  composite: 44.0
  coverage:
    artifact_dirs: 24
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 44.7
    developer_ergonomics: 66.1
    discoverability: 66.1
    operational_transparency: 21.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 44.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/rightmove/rightmove-2026-08-17T081601.png
security:
- kind: authentication
  name: Rightmove Authentication
  slug: rightmove-authentication
  summary_line: oauth2/mutualTLS · 2 schemes
- kind: domain-security
  name: Rightmove Domain Security
  slug: rightmove-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 3
skills:
- name: Publish or update a commercial property listing
  slug: rightmove-publish-commercial-listing
- name: Reconcile a branch's commercial listings
  slug: rightmove-reconcile-branch-listings
- name: Withdraw or remove a commercial listing
  slug: rightmove-withdraw-commercial-listing
slug: rightmove
tags:
- Real Estate
- United Kingdom
- Property Listings
- Property Portal
- PropTech
- Rentals
- Commercial Real Estate
- Data Feed
website: https://www.rightmove.co.uk/
---
