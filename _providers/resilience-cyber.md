---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: The only publicly documented, machine-readable surface Resilience operates. portal.cyberresilience.com — the gated client and broker application — redirects through /v2/api/auth/login to an Auth0 tena
  name: Resilience Identity (Auth0 Authorization Server)
  slug: resilience-identity-auth0-authorization-server
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/resilience-cyber-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cyberresilience.com/
- group: company
  title: ''
  type: Blog
  url: https://cyberresilience.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://cyberresilience.com/?feed=rss2
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.cyberresilience.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/resilience-cyber-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.cyberresilience.com/
- group: start
  title: ''
  type: SignUp
  url: https://portal.cyberresilience.com/
- group: auth
  title: ''
  type: Authentication
  url: https://auth.cyberresilience.com/.well-known/openid-configuration
- group: auth
  title: ''
  type: Authentication
  url: authentication/resilience-cyber-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/resilience-cyber-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/resilience-cyber-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/resilience-cyber-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/resilience-cyber-llms.txt
- group: operate
  title: ''
  type: Support
  url: https://cyberresilience.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cyberresilience.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cyberresilience.com/privacy-policy/
- group: start
  title: ''
  type: Demo
  url: https://cyberresilience.com/request-demo
- group: company
  title: ''
  type: Press
  url: https://cyberresilience.com/newsroom/press-releases/
- group: other
  title: ''
  type: CaseStudies
  url: https://cyberresilience.com/resources/case-studies/
- group: other
  title: ''
  type: Research
  url: https://cyberresilience.com/resources/industry-reports/
- group: company
  title: ''
  type: About
  url: https://cyberresilience.com/about-us/
- group: other
  title: ''
  type: Leadership
  url: https://cyberresilience.com/leadership/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/resilience-cyber/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/ResilienceSays
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@Cyber.Resilience
- group: operate
  title: ''
  type: ContactForm
  url: https://cyberresilience.com/contact-us/
- group: company
  title: ''
  type: Careers
  url: https://job-boards.greenhouse.io/resilience
- group: company
  title: ''
  type: Partners
  url: https://cyberresilience.com/brokers/
created: '2026-07-25'
description: 'Resilience is a United States cyber-risk company that underwrites cyber insurance and technology errors-and-omissions coverage while running the security analytics and claims service around it. Founded in 2016 by operators out of US military and intelligence backgrounds and headquartered in San Francisco, it distributes through brokers rather than direct-to-consumer, and positions itself as a specialty cyber carrier whose underwriting is fed by its own risk model — the Threatonomics Risk Graph — plus a 24/7 in-house Risk Operations Center and claims/incident-response team. Product lines are cyber insurance, technology E&O, claims and incident response, security investment prioritization, and multi-entity/portfolio risk, sold in the US and in UK, Canadian, German, French, Italian and Spanish locales. Its API posture is partner-gated and honest to record as such: there is no developer portal, no public API reference, no downloadable OpenAPI, and no public Postman collection anywhere
  on cyberresilience.com. The only machine-facing surface is portal.cyberresilience.com, a client and broker application that 302-redirects to an Auth0 tenant at auth.cyberresilience.com requesting an access token for the private audience https://api.prod.resilienceinsurance.app — an internal product API, not a published one. No ACORD, AL3, ACORD XML, NGDS, IVANS, Applied Epic or Vertafore reference appears anywhere on the public site, which is itself a finding for a US specialty carrier: this is a direct-underwriting, broker-relationship distribution model rather than an agency-download one.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: Resilience
nav: Providers
network: true
overview: 'Resilience publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, United States, Cyber Insurance, Property and Casualty, and Insurtech.


  Resilience''s developer surface includes engineering blog, signup flow, authentication, support, YouTube channel, and 24 more developer resources.'
random_paper: 20
scopes:
- name: Resilience Cyber Scopes
  scope_count: 14
  slug: resilience-cyber-scopes
  summary_line: 14 scopes · authorizationCode/clientCredentials
score:
  band: thin
  composite: 30.8
  delta: -1.6
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 17.4
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 32.4
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 71.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Resilience Cyber Authentication
  slug: resilience-cyber-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Resilience Cyber Domain Security
  slug: resilience-cyber-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Resilience Cyber Trust Center
  slug: resilience-cyber-trust-center
  summary_line: trust center published
slug: resilience-cyber
tags:
- Insurance
- United States
- Cyber Insurance
- Property and Casualty
- Insurtech
- Underwriting
- Claims
- Risk Data
- Technology Errors and Omissions
- Broker
- Specialty Insurance
website: https://cyberresilience.com/
---
