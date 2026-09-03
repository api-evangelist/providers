---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
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
  score: 5.4
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: Versioned REST API behind Realisti.co, the virtual-tour and property-imaging platform Casavo operates as Casavo Virtual Tools. Casavo's own help centre documented it as the integration path for estate
  name: Casavo Virtual Tools (Realisti.co) API
  slug: virtual-tools
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://casavo.com/
- group: start
  title: ''
  type: SignUp
  url: https://my.casavo.com/
- group: start
  title: ''
  type: Login
  url: https://editor.realisti.co/login/
- group: operate
  title: ''
  type: Support
  url: https://casavo.com/en/contact/
- group: company
  title: ''
  type: Blog
  url: https://blog.casavo.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/casavo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://casavo.com/en/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://casavo.com/pdf/privacy-policy-en.pdf
- group: operate
  title: ''
  type: StatusPage
  url: https://uptime.casavo.com/
- group: company
  title: ''
  type: Careers
  url: https://casavo.com/en/careers/
- group: other
  title: ''
  type: Engineering
  url: https://casavo.com/en/engineering/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/casavo-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/casavo-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/casavo-domain-security.yml
coverage:
  checked: '2026-08-09'
  detail: Casavo's Virtual Tools (Realisti.co) REST API is live and its v4 collection index is served anonymously, but the API reference Casavo published to integrators (editor.realisti.co/api/v4/docs/) now 404s, the whole HubSpot help centre that pointed at it 404s, every resource collection answers 401, and API use is a per-account plan entitlement (plan.can_api_use_api_key) reachable only through a login-gated Freshdesk support portal.
  evidence:
  - status: 200
    url: https://editor.realisti.co/api/v4/
  - status: 404
    url: https://editor.realisti.co/api/v4/docs/
  - status: 401
    url: https://editor.realisti.co/api/v4/house/
  - status: 404
    url: https://help.casavo.com/documentazione-api
  - status: 302
    url: https://support.casavo.com/
  reason: customer-only-docs
  state: gated
created: '2026-08-09'
description: 'Casavo Management S.p.A. is an Italian proptech company founded in Milan in 2017 by Giorgio Tinacci that operates a digital residential real estate platform across Italy, Spain, France and Portugal. It began as an iBuyer — instantly valuing, buying, renovating and reselling homes — and has since shifted to a marketplace and brokerage model that connects sellers, buyers and partner estate agents, wrapping the transaction in mortgage brokerage, document management and renovation services. Casavo''s developer-facing surface is not its consumer marketplace but the virtual-tour platform it acquired, Realisti.co (marketed as Casavo Virtual Tools): a versioned REST API at editor.realisti.co that lets partner agencies and property-management software create virtual tours, retrieve tour URLs, and activate or deactivate a tour at the end of a mandate. The company also runs a public GitHub organization of DevOps tooling, Helm charts, Terraform modules and the Habitat design system, and
  an engineering blog.'
image: https://casavo-wine.imgix.net/images/seo/casavo-og-image.png
layout: provider
modified: '2026-08-09'
name: Casavo
nav: Providers
network: true
overview: 'Casavo publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Real-Estate, PropTech, Marketplace, and Virtual Tours.


  Casavo''s developer surface includes signup flow, support, engineering blog, and 11 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 22.8
  coverage:
    artifact_dirs: 12
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 22.8
  provenance:
    conformance: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/casavo/refs/heads/main/screenshots/casavo-2026-09-02T145020.png
security:
- kind: authentication
  name: Casavo Authentication
  slug: casavo-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Casavo Domain Security
  slug: casavo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: casavo
tags:
- Company
- Real-Estate
- PropTech
- Marketplace
- Virtual Tours
- Property Listings
- Italy
- Spain
- France
- Mortgages
website: https://casavo.com/
---
