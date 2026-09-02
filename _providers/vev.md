---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
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
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The Vev REST API (api.vev.design) for API-key introspection and platform integration, authenticated with an x-vev-key header. Complemented by a publish webhook and a React component SDK/CLI toolchain.
  name: Vev API
  slug: vev-api
artifact_total: 5
asyncapis:
- description: ''
  name: Vev Webhooks
  slug: vev-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.vev.design/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.vev.design/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.vev.design/api/auth
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.vev.design/cli/getting-started
- group: auth
  title: ''
  type: Authentication
  url: authentication/vev-authentication.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/vev-webhooks.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vev-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/vev-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/vev-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/vev-cli.yml
- group: design
  title: ''
  type: Components
  url: components/vev-components.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/vev-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/vev-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/vev-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.vev.design/security/responsible-disclosure-policy/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vev-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.vev.design/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.vev.design/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vev-design
- group: operate
  title: ''
  type: Support
  url: https://help.vev.design/
- group: company
  title: ''
  type: Blog
  url: https://www.vev.design/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.vev.design/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://editor.vev.design/signup
- group: start
  title: ''
  type: Login
  url: https://editor.vev.design/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.vev.design/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vev.design/privacy-policy/
- group: company
  title: ''
  type: Website
  url: https://www.vev.design/
created: '2026-07-17'
description: 'Vev is a no-code web design and publishing platform for enterprise teams, letting designers and marketers build interactive content, landing pages, and high-performing marketing materials in a visual Design Editor (trusted by brands like Experian and Pfizer). Its developer surface extends the platform with code: a REST API at api.vev.design authenticated with an x-vev-key API key, a publish webhook that delivers server-rendered HTML/CSS/JS to your own host on every publish, a React component SDK (@vev/react + registerVevComponent) for building custom drag-and-drop widgets, a CLI (@vev/cli) for local development and deployment, and CMS integration via client-side or server-side (Mustache) rendering.'
image: https://cdn.vev.design/cdn-cgi/image/f=auto,q=82,h=628,w=1200,fit=crop/private/FExxUXqHHsQUqBgoOFYgE0rdnoq2/image/W78KT_O5Pd_2k5o5u.png
layout: provider
modified: '2026-07-21'
name: Vev
nav: Providers
network: true
overview: 'Vev publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Design Tech, No-Code, Web Design, and CMS.


  The Vev catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Vev''s developer surface includes documentation, API reference, getting-started guide, authentication, CLI, support, engineering blog, and 20 more developer resources.'
random_paper: 1
score:
  band: developing
  composite: 40.9
  coverage:
    artifact_dirs: 10
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.3
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 0.0
    contract_quality: 41.6
    developer_ergonomics: 52.4
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 41.2
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vev/refs/heads/main/screenshots/vev-2026-08-17T082739.png
security:
- kind: authentication
  name: Vev Authentication
  slug: vev-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Vev Domain Security
  slug: vev-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Vev Vulnerability Disclosure
  slug: vev-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: vev
tags:
- Company
- Design Tech
- No-Code
- Web Design
- CMS
- Website Builder
- Webhook
- React Components
- Developer Tools
website: https://www.vev.design/
---
