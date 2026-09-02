---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
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
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/fizz-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://fizzsocial.notion.site/Fizz-Vulnerability-Disclosure-Policy-b32371f595344efb8cacfea9160bed73
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fizz-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/fizz-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/fizz-security.txt
- group: company
  title: ''
  type: Website
  url: https://fizz.social
- group: company
  title: ''
  type: Blog
  url: https://fizz.social/blog
- group: operate
  title: ''
  type: Support
  url: https://fizz.social/FAQ
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fizz.social/Guidelines-and-Policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fizz.social/Guidelines-and-Policies/privacy-policy
- group: company
  title: ''
  type: Press
  url: https://fizz.social/Press
created: '2026-07-17'
description: Fizz is a social platform built for college campuses, connecting students within their own school communities across 700+ campuses in the United States. Founded by Stanford students, Fizz gives verified students an anonymous, hyper-local feed to find their community and join the conversation, buy and sell through Fizz Marketplace, and engage under community values of being supportive, curious, honest, and brave. The platform is backed by Lightspeed Venture Partners and NEA. Fizz is a consumer mobile social app and does not publish a public developer API, SDKs, or API documentation; this API Evangelist profile captures its public web, legal, and security surface for network discovery and monitoring.
image: https://fizz.social/favicon.ico
layout: provider
modified: '2026-07-19'
name: Fizz
nav: Providers
network: true
overview: 'Fizz is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Social, Social Networking, Community, and Campus.


  Fizz''s developer surface includes engineering blog, support, and 9 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 13.4
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 13.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 37.0
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fizz/refs/heads/main/screenshots/fizz-2026-07-25T214655.png
security:
- kind: domain-security
  name: Fizz Domain Security
  slug: fizz-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Fizz Vulnerability Disclosure
  slug: fizz-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: fizz
tags:
- Company
- Social
- Social Networking
- Community
- Campus
- Higher Education
- Students
- Consumer
- Mobile
- Marketplace
website: https://fizz.social
---
