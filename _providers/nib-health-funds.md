---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 15.3
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: 'The Auth0-backed OpenID Connect tenant behind nib member sign-in, issuer https://id.nib.com.au/. It is the only nib API surface with anonymously readable, machine-readable metadata: the OIDC discovery'
  name: nib Identity (OpenID Connect)
  slug: identity
artifact_total: 5
common:
- group: auth
  title: ''
  type: Authentication
  url: authentication/nib-health-funds-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/nib-health-funds-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/nib-health-funds-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/nib-health-funds-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.nib.com.au/.well-known/security.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/nib-health-funds-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/nib-health-funds-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nib-health-funds-llms.txt
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nib.com.au/docs/online-terms
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/nib-health-funds-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nib-health-funds-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nib.com.au/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nib-health-funds
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nib-health
- group: company
  title: ''
  type: Blog
  url: https://www.nib.com.au/the-checkup
- group: company
  title: ''
  type: Press
  url: https://www.nib.com.au/media
- group: start
  title: ''
  type: Login
  url: https://my.nib.com.au/login
- group: start
  title: ''
  type: PartnerPortal
  url: https://www.nib.com.au/providers/hcp-portal/user/login
- group: other
  title: ''
  type: Providers
  url: https://www.nib.com.au/providers
- group: operate
  title: ''
  type: Support
  url: https://www.nib.com.au/help
- group: operate
  title: ''
  type: Contact
  url: https://www.nib.com.au/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nib.com.au/legal/privacy-policy
- group: other
  title: ''
  type: OpenIDConnectDiscovery
  url: https://id.nib.com.au/.well-known/openid-configuration
created: '2026-07-25'
description: 'nib holdings limited (ASX:NHF), trading as nib, is an Australian private health insurer headquartered in Newcastle, New South Wales, and one of the country''s largest health funds alongside Medibank, Bupa and HCF. Its lines of business span Australian residents health insurance, New Zealand health insurance through nib nz insurance limited, international workers and overseas student health cover (OSHC), travel insurance, and nib Thrive, its National Disability Insurance Scheme plan-management arm. As a private health insurer it is regulated by APRA and the Private Health Insurance Act rather than by an open-data mandate — Australia''s Consumer Data Right was designated to extend to general insurance and then deferred, and it never reached private health insurance at all, so there is no regulatory forcing function pushing nib toward public APIs. Its API posture reflects that exactly: nib publishes no public, self-serve developer portal and no downloadable OpenAPI definitions.
  Probes of developer.nib.com.au, developers.nib.com.au, docs.nib.com.au and api.nib.com.au do not resolve, and /developers, /api, /developer, /partners and /integrations on nib.com.au all return 404. A real AWS API Gateway host, api-gateway.nib.com.au, is referenced by nib''s own web front-end Content-Security-Policy and answers anonymously with HTTP 403 {"message":"Forbidden"}, confirming a first-party, credential-gated gateway with no public documentation. Healthcare provider integration runs through the login-walled nib HCP portal and through third-party claiming terminals — HICAPS and HealthPoint — plus Honeysuckle Health for medical network and MediGap registration, not through an nib-published API. Member identity is an Auth0-backed OpenID Connect tenant at id.nib.com.au whose discovery document is publicly readable, as is an RFC 9116 security.txt at www.nib.com.au naming security@nib.com.au. nib also publishes three first-party npm scopes (@nib, @nib-styles, @nib-components) across
  four public GitHub organisations, but they carry frontend and DevOps tooling rather than any API client library. nib is recorded here as an honest partner-gated stub.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: nib
nav: Providers
network: true
overview: 'nib publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Australia, Health Insurance, Carrier, and Claims.


  nib''s developer surface includes authentication, engineering blog, support, and 20 more developer resources.'
random_paper: 19
scopes:
- name: Nib Health Funds Scopes
  scope_count: 14
  slug: nib-health-funds-scopes
  summary_line: 14 scopes · authorizationCode/clientCredentials/implicit/deviceCode
score:
  band: thin
  composite: 29.1
  delta: -2.6
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 17.4
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 15.8
  previous_composite: 31.7
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 72.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Nib Health Funds Authentication
  slug: nib-health-funds-authentication
  summary_line: oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Nib Health Funds Domain Security
  slug: nib-health-funds-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Nib Health Funds Vulnerability Disclosure
  slug: nib-health-funds-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: nib-health-funds
tags:
- Insurance
- Australia
- Health Insurance
- Carrier
- Claims
- Private Health Insurance
- Travel Insurance
- New Zealand
- NDIS
- Partner Gated
website: https://www.nib.com.au/
---
