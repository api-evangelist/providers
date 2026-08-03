---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 16.2
  scored_at: '2026-08-03'
api_count: 3
apis:
- description: TAL's partner-facing OpenID Connect identity tenant (Okta org talpartner-au.okta.com), and the only machine-readable API contract TAL serves anonymously. Full OIDC discovery and RFC 8414 authorization
  name: TAL Partner Identity
  slug: tal-partner-identity
- description: The integration estate behind TAL's group insurance business with superannuation funds — underwriting in/out (uwin, uwout), claims in/out (claimsin, claimsout), a common service, a delivery service an
  name: TAL Group Life B2B (glsb2b)
  slug: tal-group-life-b2b-glsb2b
- description: A live production GraphQL endpoint serving TAL's Underwriting Rules Engine. It answers anonymous POSTs and reports a query root type of CaseQuery with no mutation or subscription type, but field-level
  name: TAL Underwriting Rules Engine (URE) GraphQL
  slug: tal-underwriting-rules-engine-ure-graphql
artifact_total: 6
common:
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tal-australia-well-known.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: https://login.talpartner.tal.com.au/.well-known/openid-configuration
- group: auth
  title: ''
  type: Authentication
  url: authentication/tal-australia-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/tal-australia-scopes.yml
- group: docs
  title: ''
  type: GraphQL
  url: graphql/tal-australia-ure-graphql.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tal-australia-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tal-australia-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tal-australia-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tal-australia-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/tal-australia-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tal-australia-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tal-australia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.tal.com.au/
- group: company
  title: ''
  type: About
  url: https://www.tal.com.au/about-us
- group: start
  title: ''
  type: PartnerPortal
  url: https://adviser.tal.com.au/
- group: start
  title: ''
  type: PartnerPortal
  url: https://www.grouphq.tal.com.au/
- group: operate
  title: ''
  type: Support
  url: https://www.tal.com.au/contact-us
- group: operate
  title: ''
  type: FAQ
  url: https://www.tal.com.au/tools-and-faqs/insurance-faqs
- group: start
  title: ''
  type: Login
  url: https://mytal.tal.com.au/login
- group: company
  title: ''
  type: Blog
  url: https://www.tal.com.au/slice-of-life-blog
- group: company
  title: ''
  type: Press
  url: https://www.tal.com.au/about-us/media-centre
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tal.com.au/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://www.tal.com.au/security
- group: other
  title: ''
  type: Complaints
  url: https://www.tal.com.au/contact-us/complaint-handling-process
- group: company
  title: ''
  type: Careers
  url: https://www.tal.com.au/about-us/careers
- group: other
  title: ''
  type: Sitemap
  url: https://www.tal.com.au/sitemap.xml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tal-australia
created: '2026-07-25'
description: 'TAL is Australia''s largest life insurer by inforce risk-only premium (NMG Consulting, 2023), owned by Japan''s Dai-ichi Life Group and underwriting through TAL Life Limited (ABN 70 050 109 450, AFSL 237848). Operating in the Australian market for roughly 150 years, TAL writes life cover, income protection, total and permanent disability and critical illness, and reports paying $4.7 billion in benefits to 57,000 customers and their families in its most recent year. It distributes through three channels — financial advisers via the login-gated TAL Adviser Centre, group insurance inside superannuation funds, and direct/embedded offers including backd by TAL, a payroll-embedded product built with Sydney insurtech Cover Genius. TAL is not API-less, it is API-private: certificate transparency and live probing surface a real partner API estate — an OpenID Connect partner identity tenant, a bearer-protected Group Life B2B integration estate (glsb2b), per-distributor API hosts including
  one named for the Iress adviser software, and a production Underwriting Rules Engine GraphQL endpoint — none of which is documented, registrable or self-serve. There is no developer portal, no public API reference, no downloadable OpenAPI, and no published ACORD or AL3 position. Australia''s Consumer Data Right was designated to extend to insurance but was deferred, so no open-insurance mandate forces a public surface here.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: TAL
nav: Providers
network: true
overview: 'TAL publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Australia, Life Insurance, Income Protection, and Group Insurance.


  TAL''s developer surface includes authentication, support, FAQ, engineering blog, and 23 more developer resources.'
random_paper: 2
scopes:
- name: Tal Australia Scopes
  scope_count: 7
  slug: tal-australia-scopes
  summary_line: 7 scopes · authorizationCode/deviceCode
score:
  band: emerging
  composite: 25.0
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 0.0
    developer_ergonomics: 17.4
    discoverability: 92.6
    governance: 3.1
    operational_transparency: 10.5
  previous_composite: 25.0
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 57.6
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Tal Australia Authentication
  slug: tal-australia-authentication
  summary_line: openIdConnect/oauth2/http · 5 schemes
- kind: domain-security
  name: Tal Australia Domain Security
  slug: tal-australia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tal-australia
tags:
- Insurance
- Australia
- Life Insurance
- Income Protection
- Group Insurance
- Superannuation
- Underwriting
- Claims
- Carrier
- Embedded Insurance
- Partner Gated
- No Public API
- OpenID Connect
- GraphQL
- Identity
website: https://www.tal.com.au/
---
