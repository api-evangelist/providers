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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/boyd-gaming-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/boyd-gaming
- group: company
  title: ''
  type: Website
  url: https://www.boydgaming.com
- group: other
  title: ''
  type: LoyaltyProgram
  url: https://rewards.boydgaming.com
- group: other
  title: ''
  type: SportsBetting
  url: https://sports.boydgaming.com
- group: company
  title: ''
  type: InvestorRelations
  url: https://investors.boydgaming.com
- group: company
  title: ''
  type: Careers
  url: https://careers.boydgaming.com
- group: other
  title: ''
  type: Suppliers
  url: https://boydgaming.supplier.bid
- group: other
  title: ''
  type: Media
  url: https://media.boydgaming.com
- group: auth
  title: ''
  type: Security
  url: https://www.boydgaming.com/security-policy
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/boyd-gaming-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/boyd-gaming-llms.txt
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.boydgaming.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.boydgaming.com/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://www.boydgaming.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.boydgaming.com/company/news
coverage:
  checked: '2026-09-04'
  detail: Boyd Gaming is a casino operator whose software ships only as end-user apps (Boyd Rewards, Boyd Sports, Stardust Social Casino) - no api./developer./developers. subdomain resolves, the 368-URL corporate sitemap contains no API, developer or integration page, and every OpenAPI/GraphQL/MCP/agent-card probe across nine Boyd hosts either 404d or returned an HTML catch-all shell.
  evidence:
  - status: 200
    url: https://www.boydgaming.com/sitemap.xml
  - status: 404
    url: https://rewards.boydgaming.com/openapi.json
  - status: 404
    url: https://www.stardustsocialcasino.com/.well-known/agent-card.json
  - status: 403
    url: https://www.boydgaming.com/.well-known/security.txt
  reason: no-developer-program
  state: none
created: '2026-03-23'
description: Boyd Gaming is a multi-jurisdictional casino entertainment company that owns and operates 28+ gaming properties across 10 U.S. states. The company offers casino gaming, hotel accommodations, dining, entertainment, and sports betting through its Boyd Sports platform. Boyd Rewards is the company's loyalty program spanning all properties, accessible via web portal and mobile app.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/boyd-gaming.png
layout: provider
modified: '2026-09-04'
name: Boyd Gaming
nav: Providers
network: true
overview: 'Boyd Gaming is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Gaming, Casinos, Hospitality, Sports Betting, and Loyalty Programs.


  Boyd Gaming''s developer surface includes support, engineering blog, and 14 more developer resources.'
press:
- date: '2026-05-25'
  title: Hotels, Casinos, & Shows | Boyd
  url: https://www.boydgaming.com/
- date: '2026-05-25'
  title: Matthew Boyd Stats, Height, Weight, Position, Rookie ...
  url: https://www.baseball-reference.com/players/b/boydma01.shtml
- date: '2026-05-25'
  title: Boyd Gaming
  url: https://en.wikipedia.org/wiki/Boyd_Gaming
- date: '2026-05-25'
  title: City of Boyd | Boyd TX
  url: https://www.cityofboyd.com/
- date: '2026-05-25'
  title: Home - Boyd | Trusted Innovation
  url: https://www.boydcorp.com/
random_paper: 10
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/boyd-gaming/refs/heads/main/screenshots/boyd-gaming-2026-06-20T173622.png
security:
- kind: domain-security
  name: Boyd Gaming Domain Security
  slug: boyd-gaming-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Boyd Gaming Vulnerability Disclosure
  slug: boyd-gaming-vulnerability-disclosure
  summary_line: Bugcrowd · contact published
slug: boyd-gaming
tags:
- Gaming
- Casinos
- Hospitality
- Sports Betting
- Loyalty Programs
- Fortune 1000
website: https://www.boydgaming.com
---
