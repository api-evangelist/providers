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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-08-10'
api_count: 0
artifact_total: 4
common:
- group: agent
  title: ''
  type: WellKnown
  url: well-known/hcf-well-known.yml
- group: other
  title: ''
  type: OpenIDConfiguration
  url: well-known/hcf-openid-configuration.json
- group: auth
  title: ''
  type: OAuthAuthorizationServer
  url: well-known/hcf-oauth-authorization-server.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/hcf-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/hcf-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hcf-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hcf-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/hcf-trust-center.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hcf-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.hcf.com.au/
- group: company
  title: ''
  type: About
  url: https://www.hcf.com.au/about-us
- group: operate
  title: ''
  type: ContactUs
  url: https://www.hcf.com.au/contact-us
- group: operate
  title: ''
  type: Support
  url: https://www.hcf.com.au/about-hcf/help-hub
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.hcf.com.au/about-hcf/help-hub
- group: other
  title: ''
  type: CustomerService
  url: https://www.hcf.com.au/about-us/about-HCF/customer-service
- group: other
  title: ''
  type: Feedback
  url: https://www.hcf.com.au/complaints-feedback
- group: start
  title: ''
  type: ProviderPortal
  url: https://www.hcf.com.au/provider-portals/
- group: auth
  title: ''
  type: InformationSecurity
  url: https://www.hcf.com.au/about-us/about-HCF/information-security
- group: build
  title: ''
  type: CodeOfConduct
  url: https://www.hcf.com.au/about-us/about-HCF/governance-and-structure/policies/code-of-conduct
- group: other
  title: ''
  type: Sustainability
  url: https://www.hcf.com.au/about-hcf/group-sustainability-statement
- group: company
  title: ''
  type: Careers
  url: https://www.hcf.com.au/about-us/careers
- group: other
  title: ''
  type: Forms
  url: https://www.hcf.com.au/forms-and-brochures
- group: company
  title: ''
  type: LinkedIn
  url: https://au.linkedin.com/company/hcf
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/hcfau
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/hcfaustralia/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hcf.com.au/about-us/about-HCF/governance-and-structure/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hcf.com.au/about-us/about-HCF/governance-and-structure/policies/terms-and-conditions
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.hcf.com.au/about-hcf/privacy-information-trust-centre
- group: company
  title: ''
  type: Blog
  url: https://www.hcf.com.au/health-agenda
- group: company
  title: ''
  type: PressRoom
  url: https://www.hcf.com.au/about-us/media-centre
- group: other
  title: ''
  type: AnnualReport
  url: https://www.hcf.com.au/about-us/about-HCF/governance-and-structure/annual-report
- group: start
  title: ''
  type: Login
  url: https://www.hcf.com.au/member-login
- group: other
  title: ''
  type: OpenIDConfiguration
  url: https://id.hcf.com.au/.well-known/openid-configuration
created: '2026-07-25'
description: 'HCF — The Hospitals Contribution Fund of Australia Limited (ABN 68 000 026 746, AFSL 241 414), founded in 1932 and headquartered in Sydney — is Australia''s largest not-for-profit health fund, covering over 2 million members. It underwrites private health insurance (hospital, extras and ambulance cover) and Overseas Visitors Health Cover, and distributes life and Recover Cover products (life protect, income protect, critical illness), travel, pet, home, car and landlord insurance, plus the Flip accidental-injury brand, alongside its own HCF dental and eyecare centres and the HCF Research Foundation. As a carrier in Australian private health insurance, HCF publishes NO public, self-serve developer API and no developer portal: probes of developer.hcf.com.au, developers.hcf.com.au and docs.hcf.com.au do not resolve, and /developers, /developer, /api-docs, /partners and /integrations on www.hcf.com.au all return 404. Member and provider integration runs through channels HCF does
  not itself expose as an API — point-of-service extras claiming over third-party HICAPS VX, HICAPS Trinity and CommBank Smart Health terminals, Medicare Benefit Statements for medical gap claims, the My Membership app and online member services behind an Okta-backed sign-in at id.hcf.com.au, and four login-gated ASP.NET provider portals (hospital, medical, dental and ancillary) at www.hcf.com.au/provider-portals which are web applications rather than machine interfaces. The only machine-readable surface HCF answers on is that Okta tenant''s OIDC and RFC 8414 discovery metadata, captured in this record. No ACORD reference of any kind appears on the site, which is consistent with private health insurance sitting outside the general-insurance ACORD/AL3 world, and Australia''s Consumer Data Right — designated for general insurance and then deferred — never reached health insurance at all. The record here is deliberately an honest stub: this is a partner-gated, no-public-API carrier.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: HCF
nav: Providers
network: true
overview: 'HCF is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Australia, Health Insurance, Life Insurance, and Travel Insurance.


  HCF''s developer surface includes authentication, support, YouTube channel, engineering blog, and 29 more developer resources.'
random_paper: 73
scopes:
- name: Hcf Scopes
  scope_count: 83
  slug: hcf-scopes
  summary_line: 83 scopes · authorizationCode/clientCredentials
score:
  band: emerging
  composite: 27.9
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 0.0
    developer_ergonomics: 17.4
    discoverability: 68.5
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 27.9
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 71.2
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: authentication
  name: Hcf Authentication
  slug: hcf-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Hcf Domain Security
  slug: hcf-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Hcf Trust Center
  slug: hcf-trust-center
  summary_line: trust center published
slug: hcf
tags:
- Insurance
- Australia
- Health Insurance
- Life Insurance
- Travel Insurance
- Pet Insurance
- Carrier
- Not-for-Profit
- Claims
- Member Services
- Partner Gated
- No Public API
website: https://www.hcf.com.au/
---
