---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.5
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: 'A live, production API gateway at api.canadalife.com serving Canada Life''s partner, distributor and MGA integrations. It is fully gated: every business path probed (including /v1, /docs, /health, /ope'
  name: Canada Life Partner API Gateway
  slug: canada-life-partner-api-gateway
- description: The retail customer portal at my.canadalife.com is hosted on Salesforce Experience Cloud and publishes a complete OpenID Connect discovery document anonymously — authorization, token, userinfo, intros
  name: Canada Life Customer Portal Identity (my.canadalife.com)
  slug: canada-life-customer-portal-identity-mycanadalifecom
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.canadalife.com/
- group: company
  title: ''
  type: About
  url: https://www.canadalife.com/about-us.html
- group: other
  title: ''
  type: SignIn
  url: https://www.canadalife.com/sign-in.html
- group: start
  title: ''
  type: PartnerPortal
  url: https://advisor.canadalife.com/login
- group: start
  title: ''
  type: CustomerPortal
  url: https://my.canadalife.com/
- group: operate
  title: ''
  type: Support
  url: https://www.canadalife.com/support.html
- group: operate
  title: ''
  type: ContactUs
  url: https://www.canadalife.com/contact-us.html
- group: company
  title: ''
  type: Blog
  url: https://www.canadalife.com/blog.html
- group: company
  title: ''
  type: News
  url: https://www.canadalife.com/about-us/news-highlights/news.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.canadalife.com/privacy.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.canadalife.com/terms-of-use.html
- group: auth
  title: ''
  type: Security
  url: https://www.canadalife.com/internet-security.html
- group: other
  title: ''
  type: Standards
  url: https://www.cliedis.ca/who-we-are/members
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/canada-life
- group: auth
  title: ''
  type: Authentication
  url: authentication/canada-life-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/canada-life-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/canada-life-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/canada-life-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/canada-life-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/canada-life-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/canada-life-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/canada-life-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/canada-life-llms.txt
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-07-25'
description: 'The Canada Life Assurance Company is one of Canada''s largest life and health insurers, formed from the 2020 amalgamation of Great-West Life, London Life and Canada Life under Winnipeg-based parent Great-West Lifeco. From its home market of Canada it underwrites individual life insurance, critical illness and disability coverage, individual and group health and dental benefits, group retirement and savings, segregated funds and annuities, distributed through an advisor and managing-general-agent channel rather than direct-to-developer. Canada Life publishes no public, self-serve developer portal and no downloadable API specifications. Its integration surface is entirely partner-gated: a live OAuth2-protected API gateway at api.canadalife.com that returns 403 on every path and exposes only OpenID discovery and JWKS anonymously, a Liferay "Digital Agent" advisor login wall at advisor.canadalife.com, a Salesforce-hosted customer portal at my.canadalife.com that publishes its own
  OpenID Connect discovery document with 36 platform scopes, and — the real machine-to-machine channel for this market — ACORD XML for Life data exchange with distributors through its carrier membership in CLIEDIS, the Canadian Life Insurance EDI Standards body. A former Apigee developer portal at developers.canadalife.com survives only as a dangling DNS CNAME pointing at prod-canadalife-portal.apigee.net, which no longer resolves.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: Canada Life
nav: Providers
network: true
overview: 'Canada Life publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Canada, Life Insurance, Health Insurance, and Employee Benefits.


  Canada Life''s developer surface includes support, engineering blog, product news, authentication, and 20 more developer resources.'
random_paper: 11
scopes:
- name: Canada Life Scopes
  scope_count: 36
  slug: canada-life-scopes
  summary_line: 36 scopes · clientCredentials/authorizationCode
score:
  band: emerging
  composite: 26.0
  coverage:
    artifact_dirs: 10
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 26.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 72.7
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/canada-life/refs/heads/main/screenshots/canada-life-2026-07-25T204322.png
security:
- kind: authentication
  name: Canada Life Authentication
  slug: canada-life-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Canada Life Domain Security
  slug: canada-life-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Canada Life Vulnerability Disclosure
  slug: canada-life-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: canada-life
tags:
- Insurance
- Canada
- Life Insurance
- Health Insurance
- Employee Benefits
- Group Retirement
- Carrier
- ACORD
- Partner Gated
- No Public API
website: https://www.canadalife.com/
---
