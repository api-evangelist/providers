---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cava-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://cava.com/.well-known/security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cava-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cava.com/
- group: other
  title: ''
  type: Locations
  url: https://cava.com/locations
- group: operate
  title: ''
  type: Support
  url: https://support.cava.com/
- group: start
  title: ''
  type: SignUp
  url: https://cava.com/rewards
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cava.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cava.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://cava.com/news
- group: company
  title: ''
  type: News
  url: https://cava.com/news
- group: company
  title: ''
  type: Investors
  url: https://investor.cava.com/overview/default.aspx
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cavagrill
- group: company
  title: ''
  type: Careers
  url: https://cava.com/careers
- group: other
  title: ''
  type: Sustainability
  url: https://cava.com/sustainability
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cava-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cava-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/cava-security.txt
created: '2026-08-02'
description: 'CAVA Group, Inc. (NYSE: CAVA) is a Washington, D.C.-headquartered Mediterranean fast-casual restaurant company that operates the CAVA brand, serving customizable bowls, pitas, salads and sides built on house-made dips, spreads and dressings. Alongside its restaurants CAVA runs a consumer packaged goods line sold in grocery stores, a digital ordering and delivery channel, a catering business at catering.cava.com, and the CAVA Rewards loyalty program delivered through its iOS and Android apps. The company listed on the New York Stock Exchange in June 2023 and reports an in-house technology program — CavaCore, its data platform, and CAVA Current, a restaurant operating system. CAVA publishes no public developer program, API documentation, or machine-readable API contract; its public machine-readable surface is limited to an RFC 9116 security.txt and a published llms.txt.'
image: https://cava.com/favicon.ico
layout: provider
modified: '2026-08-02'
name: CAVA
nav: Providers
network: true
overview: 'CAVA is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Restaurant, Food and Beverage, Fast Casual, and Hospitality.


  CAVA''s developer surface includes support, signup flow, engineering blog, product news, and 14 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 15.0
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 15.0
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cava/refs/heads/main/screenshots/cava-2026-08-07T163134.png
security:
- kind: domain-security
  name: Cava Domain Security
  slug: cava-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Cava Vulnerability Disclosure
  slug: cava-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: cava
tags:
- Company
- Restaurant
- Food and Beverage
- Fast Casual
- Hospitality
- Consumer
- Loyalty
- Catering
- Retail
- Mediterranean
website: https://cava.com/
---
