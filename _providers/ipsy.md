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
- group: company
  title: ''
  type: Website
  url: https://www.ipsy.com
- group: company
  title: ''
  type: Blog
  url: https://www.ipsy.com/blog
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.ipsy.com/hc/en-us
- group: start
  title: ''
  type: SignUp
  url: https://www.ipsy.com/signup
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ipsy.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ipsy.com/terms
- group: auth
  title: ''
  type: Security
  url: https://www.ipsy.com/vulnerability-disclosure
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ipsy-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ipsy-domain-security.yml
created: '2026-07-17'
description: IPSY is a personalized beauty subscription company founded in 2011 by Michelle Phan, Marcelo Camberos, and Jennifer Goldfarb. Members take a detailed beauty quiz and receive monthly curated "Glam Bag" drops of deluxe samples and full-size makeup, skincare, hair, and fragrance products across tiers (Original, Boxycharm, and Ultimate). IPSY operates as a direct-to-consumer commerce and membership platform under the BFA Industries umbrella; it exposes no public developer API, running on internal GraphQL and REST services with Auth0-based consumer identity. This API Evangelist profile tracks IPSY's public web, security, and identity surface rather than a documented developer program.
image: https://cdn-cf.ipsy.com/contentAsset/image/3dec557d-7a11-45be-ae7a-1dd0b41b3918/fileAsset?byInode=1
layout: provider
modified: '2026-07-19'
name: Ipsy
nav: Providers
network: true
overview: 'Ipsy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Beauty, Cosmetics, Subscription, and E-Commerce.


  Ipsy''s developer surface includes engineering blog, signup flow, and 7 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 6.0
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.0
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ipsy/refs/heads/main/screenshots/ipsy-2026-07-25T222847.png
security:
- kind: domain-security
  name: Ipsy Domain Security
  slug: ipsy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ipsy Vulnerability Disclosure
  slug: ipsy-vulnerability-disclosure
  summary_line: contact published
slug: ipsy
tags:
- Company
- Beauty
- Cosmetics
- Subscription
- E-Commerce
- Direct to Consumer
- Personalization
- Membership
website: https://www.ipsy.com
---
