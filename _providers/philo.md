---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
  score: 0.0
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.philo.com/
- group: company
  title: ''
  type: About
  url: https://www.philo.com/about
- group: operate
  title: ''
  type: Support
  url: https://help.philo.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.philo.com/
- group: company
  title: ''
  type: Blog
  url: https://www.philo.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.philo.com/go/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.philo.com/login/subscribe
- group: start
  title: ''
  type: Login
  url: https://www.philo.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.philo.com/about/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.philo.com/about/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PhiloInc
- group: operate
  title: ''
  type: StatusPage
  url: https://status.philo.com/
- group: auth
  title: ''
  type: Security
  url: https://www.philo.com/.well-known/security.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/philo-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/philo-well-known.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/philo-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/philo-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/philo-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/philo-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/philo-llms.txt
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/philo_stock/
coverage:
  checked: '2026-08-05'
  detail: Philo ships only a consumer streaming product — there is no developer.philo.com or api.philo.com (neither hostname resolves), and the one API-shaped surface, the Apollo GraphQL endpoint its own apps call at www.philo.com/graphql, answers 200 but rejects introspection with "GraphQL introspection has been disabled".
  evidence:
  - status: 200
    url: https://www.philo.com/graphql
  - status: 404
    url: https://www.philo.com/openapi.json
  - status: 404
    url: https://www.philo.com/.well-known/api-catalog
  - status: 200
    url: https://www.philo.com/.well-known/security.txt
  reason: no-developer-program
  state: none
created: '2026-08-05'
description: 'Philo is a US live-television streaming service founded at Harvard in 2010 as Tivli, renamed in 2013 after television inventor Philo T. Farnsworth, and launched to the public in 2017. Headquartered at 225 Green Street in San Francisco, it delivers 70+ entertainment and lifestyle channels, 75,000+ on-demand titles, 120+ free ad-supported channels, and unlimited one-year DVR from $25/month across web, iOS, Android, Roku, Fire TV, Apple TV and Chromecast, with TV Everywhere sign-in to partner network apps. Philo publishes no public developer program: its product GraphQL endpoint at www.philo.com/graphql is live but has introspection disabled, and the only machine-readable documents it serves are IAB Tech Lab advertising-transparency files (ads.txt, app-ads.txt, sellers.json), an RFC 9116 security.txt, and an Instatus status page with a JSON API.'
image: https://prod-s.cdn-cf.philo.com/storage/images/maestro/web/philo-opengraph.png
layout: provider
modified: '2026-08-05'
name: Philo
nav: Providers
network: true
overview: 'Philo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Streaming, Television, Video, and Media.


  Philo''s developer surface includes support, engineering blog, pricing, signup flow, and 17 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 18.6
  coverage:
    artifact_dirs: 7
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 7.9
  previous_composite: 18.6
  provenance:
    conformance: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Philo Domain Security
  slug: philo-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Philo Vulnerability Disclosure
  slug: philo-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: philo
tags:
- Company
- Streaming
- Television
- Video
- Media
- Entertainment
- Live TV
- Advertising
- Consumer
website: https://www.philo.com/
---
