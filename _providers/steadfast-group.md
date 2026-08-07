---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 42.1
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Steadfast Group Agentic Access
  operation_count: 2
  slug: steadfast-group-agentic-access
  summary_line: 2 operations
api_count: 2
apis:
- description: The public, anonymous, read-only JSON API behind Steadfast Group's consumer Flood Risk Tracker tool. Two GET operations resolve a free-text Australian street address against the national G-NAF address
  name: Steadfast Flood Risk Tracker API
  slug: flood-risk-tracker
- description: Steadfast Group's Okta-hosted OpenID Connect provider, issuer https://idp.steadfast.com.au. It fronts the credentialed broker portal used by the Steadfast Network's 414 brokerages and, by inference fr
  name: Steadfast Identity (OpenID Connect)
  slug: identity
artifact_total: 7
common:
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
mcp_servers:
- description: ''
  name: Candidate MCP tools derived from the OpenAPI (no Steadfast MCP server exists)
  slug: candidate-mcp-tools-derived-from-the-openapi-no-steadfast-mcp-server-exists
modified: '2026-07-25'
name: Steadfast Group
nav: Providers
network: true
overview: 'Steadfast Group publishes 1 API on the [APIs.io](https://apis.io/) network: Steadfast Flood Risk Tracker API. Tagged areas include Insurance, Australia, Broker, Insurance Broker Network, and General Insurance.


  Steadfast Group''s developer surface includes engineering blog, legal docs, tooling, support, authentication, and 29 more developer resources.'
random_paper: 92
scopes:
- name: Steadfast Group Scopes
  scope_count: 7
  slug: steadfast-group-scopes
  summary_line: 7 scopes · authorizationCode/implicit/deviceCode/password
score:
  band: thin
  composite: 38.3
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 62.8
    developer_ergonomics: 19.0
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 38.3
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
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 63.6
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
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
- Broker
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
