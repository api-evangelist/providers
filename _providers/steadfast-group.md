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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Steadfast Group Agentic Access
  operation_count: 2
  slug: steadfast-group-agentic-access
  summary_line: 2 operations
api_count: 1
apis:
- description: Steadfast Group's Okta-hosted OpenID Connect provider, issuer https://idp.steadfast.com.au. It fronts the credentialed broker portal used by the Steadfast Network's 414 brokerages and, by inference fr
  name: Steadfast Identity (OpenID Connect)
  slug: identity
- baseURL: https://floodrisktracker.steadfast.com.au
  baseurl_source: declared
  description: Australian address resolution against G-NAF identifiers.
  name: Steadfast Group Address API
  slug: steadfast-group-address-api
- baseURL: https://floodrisktracker.steadfast.com.au
  baseurl_source: declared
  description: Natural-catastrophe flood risk layers for a resolved address.
  name: Steadfast Group Risk API
  slug: steadfast-group-risk-api
artifact_total: 8
collections:
- collection_type: open
  name: Steadfast Flood Risk Tracker API
  slug: open-steadfast-group-flood-risk-tracker
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/steadfast-group-flood-risk-tracker-overlay.yaml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/steadfast-group-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/steadfast-group-flood-risk-lookup.md
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/steadfast-group-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/steadfast-group-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.steadfast.com.au/
- group: company
  title: ''
  type: About
  url: https://www.steadfast.com.au/about-us/
- group: other
  title: ''
  type: BoardAndManagement
  url: https://www.steadfast.com.au/about-us/board-and-management/
- group: company
  title: ''
  type: InvestorRelations
  url: https://investor.steadfast.com.au/investor-centre/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/steadfast-group-limited/
- group: company
  title: ''
  type: Blog
  url: https://www.steadfast.com.au/well-covered/
- group: operate
  title: ''
  type: Contact
  url: https://www.steadfast.com.au/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.steadfast.com.au/privacy-policy/
- group: commercial
  title: ''
  type: Legal
  url: https://www.steadfast.com.au/legal/
- group: build
  title: ''
  type: CodeOfPractice
  url: https://www.steadfast.com.au/codes-of-practice/
- group: start
  title: ''
  type: PartnerPortal
  url: https://broker.steadfast.com.au/
- group: company
  title: ''
  type: Website
  url: https://steadfastagencies.com.au/
- group: company
  title: ''
  type: Website
  url: https://www.steadfastlife.com.au/
- group: company
  title: ''
  type: Website
  url: https://www.steadfastnz.nz/
- group: company
  title: ''
  type: Website
  url: https://www.steadfast.com.sg/
- group: build
  title: ''
  type: Tool
  url: https://floodrisktracker.steadfast.com.au/
- group: operate
  title: ''
  type: Support
  url: https://www.steadfast.com.au/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.steadfast.com.au/legal/
- group: company
  title: ''
  type: Careers
  url: https://www.steadfast.com.au/about-us/careers/
- group: other
  title: ''
  type: FindABroker
  url: https://www.steadfast.com.au/find-an-insurance-broker
- group: agent
  title: ''
  type: WellKnown
  url: well-known/steadfast-group-well-known.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/steadfast-group-openid-configuration.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/steadfast-group-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/steadfast-group-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/steadfast-group-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/steadfast-group-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/steadfast-group-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/steadfast-group-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/steadfast-group-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/steadfast-group-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/steadfast-group-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-25'
description: 'Steadfast Group Limited (ASX:SDF) is the largest general insurance broker network and the largest group of insurance underwriting agencies in Australasia, headquartered in Sydney, Australia. It is a broker-intermediary rather than a risk carrier: the Steadfast Network comprises 414 independent brokerages placing approximately $12.7 billion in gross written premium, alongside 31 underwriting agencies writing roughly 100 products across business pack, liability, professional indemnity, cyber, construction, marine, aviation, farm, strata, motor and home and contents lines, plus complementary businesses covering premium funding (IQumulate), life insurance, workplace risk, legal and compliance. Its trading technology is the Steadfast Client Trading Platform (SCTP), launched in 2009, which lets network brokers send one question set to a panel of insurers for instant comparative quotes and which transacted over $1.5 billion in GWP in CY25 across 9 insurer lines and 23 connected partners;
  SCTP and the INSIGHT policy management platform are being consolidated into a broader "Steadfast Apps" broking platform. API posture, recorded honestly - Steadfast Group publishes NO developer portal, NO API documentation and NO specification of any kind, and a full crawl of all 311 pages in the public sitemap returned zero references to a developer portal, REST API, OpenAPI or Swagger. Two genuinely machine-readable surfaces nonetheless exist and neither is announced anywhere. The consumer Flood Risk Tracker is backed by a public, anonymous, undocumented JSON API that resolves Australian addresses against the national G-NAF dataset and returns Swiss Re river-flood and storm-surge risk layers, returning RFC 9457 problem details and advertising api-supported-versions 1.0; the OpenAPI in this record was derived from the tool''s own client JavaScript and from live probes. Separately, idp.steadfast.com.au is an Okta-hosted OpenID Connect provider publishing a complete anonymous discovery document
  with PKCE S256 and DPoP, though client registration is commercially gated. The commercial surfaces remain closed: broker.steadfast.com.au is a credentialed broker login wall, and api.steadfast.com.au and api-sf.steadfast.com.au are live but undocumented hosts returning HTTP 403 at the root. Insurer and partner connectivity into SCTP is arranged commercially, not through self-serve onboarding. The company''s most notable standards signal is governance rather than implementation: founder, Managing Director and CEO Robert B. Kelly AM is Chair of the ACORD Board in New York, though no ACORD, AL3, ACORD XML or NGDS implementation detail is published anywhere on the public site. Australia has the legal machinery for open insurance but no live obligation - the Consumer Data Right was designated to extend to general insurance and then deferred, so no regulatory forcing function pushes a broker network of this scale toward a public API.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: Steadfast Group
nav: Providers
network: true
overview: 'Steadfast Group publishes 2 APIs on the [APIs.io](https://apis.io/) network: Address API and Risk API. Tagged areas include Insurance, Australia, Brokers, Insurance Broker Network, and General Insurance.


  Steadfast Group''s developer surface includes engineering blog, legal docs, tooling, support, authentication, and 32 more developer resources.'
random_paper: 7
scopes:
- name: Steadfast Group Scopes
  scope_count: 7
  slug: steadfast-group-scopes
  summary_line: 7 scopes · authorizationCode/implicit/deviceCode/password
score:
  band: thin
  composite: 32.6
  coverage:
    artifact_dirs: 20
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 63.0
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 57.1
    commercial_clarity: 57.1
    contract_governance: 4.5
    contract_quality: 16.5
    developer_ergonomics: 20.8
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 32.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 63.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/steadfast-group/refs/heads/main/screenshots/steadfast-group-2026-09-02T160824.png
security:
- kind: authentication
  name: Steadfast Group Authentication
  slug: steadfast-group-authentication
  summary_line: none/openIdConnect/oauth2 · 2 schemes
- kind: domain-security
  name: Steadfast Group Domain Security
  slug: steadfast-group-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: steadfast-group
tags:
- Insurance
- Australia
- Brokers
- Insurance Broker Network
- General Insurance
- Property and Casualty
- Underwriting Agency
- Agency Management
- ACORD
- Partner Gated
- New Zealand
website: https://www.steadfast.com.au/
---
