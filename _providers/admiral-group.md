---
access_model:
  confidence: high
  label: No public API - partner-gated
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - probe
  - documentation
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.7
  scored_at: '2026-08-12'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/admiral-group-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.admiralgroup.co.uk/
- group: company
  title: ''
  type: Website
  url: https://www.admiral.com/
- group: company
  title: ''
  type: Website
  url: https://www.confused.com/
- group: company
  title: ''
  type: Website
  url: https://www.veygo.com/
- group: company
  title: ''
  type: Website
  url: https://www.admiralpioneer.com/
- group: company
  title: ''
  type: About
  url: https://www.admiral.com/about-us
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.admiralgroup.co.uk/investors
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/admiral-group-plc
- group: other
  title: ''
  type: Sitemap
  url: https://www.admiral.com/sitemap.xml
- group: other
  title: ''
  type: Robots
  url: https://www.admiral.com/robots.txt
- group: operate
  title: ''
  type: Support
  url: https://www.admiral.com/contact-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.admiral.com/help-support-hub
- group: company
  title: ''
  type: Blog
  url: https://www.admiral.com/magazine
- group: company
  title: ''
  type: Press
  url: https://www.admiral.com/press-office
- group: start
  title: ''
  type: Login
  url: https://www.admiral.com/myaccount
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.admiral.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.admiral.com/your-privacy-and-security
- group: other
  title: ''
  type: Cookies
  url: https://www.admiral.com/cookie-policy
- group: other
  title: ''
  type: Accessibility
  url: https://www.admiral.com/accessibility
- group: company
  title: ''
  type: Careers
  url: https://admiraljobs.co.uk
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/admiral-group-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/admiral-group-well-known.yml
- group: auth
  title: ''
  type: Security
  url: https://www.confused.com/privacy-and-security/security/security-disclosure-policy
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/admiral-group-vulnerability-disclosure.yml
- group: build
  title: ''
  type: Packages
  url: packages/admiral-group-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/admiral-group-llms.txt
created: '2026-07-25'
description: 'Admiral Group plc is a FTSE 100 personal-lines insurance group headquartered in Cardiff, Wales, and listed on the London Stock Exchange since 2004. Its home market is the United Kingdom, where it is one of the largest motor insurers, trading through the Admiral, Bell, Diamond, elephant.co.uk and Veygo brands and underwriting through EUI Limited and Admiral Insurance Company Limited. Beyond UK motor it writes household, travel and pet insurance (expanded by the 2024 acquisition of RSA''s UK home and pet book, including the MORE THAN brand), runs the Admiral Money consumer lending arm, owns the Confused.com price comparison site, and operates internationally as ConTe.it in Italy, L''olivier in France and Admiral Seguros in Spain. Its Admiral Pioneer venture arm builds new businesses including Veygo, Admiral Business and the API-first embedded insurance venture Connect by Admiral, and in 2026 it agreed to acquire the commercial fleet insurtech Flock. Admiral''s API posture is
  honestly recorded here as closed: it is a direct-to-consumer and price-comparison distributor, not a broker-channel or platform carrier. No developer, developers, docs or api subdomain resolves on admiralgroup.co.uk; the corporate site is bot-blocked to automated probes; admiral.com publishes 837 sitemap URLs with no developer, API, partner or integration page; and the only API hosts that resolve (api.admiral.com, api.veygo.com) are undocumented private mobile and web backends that return 502 and 403 respectively. No public self-serve API, no OpenAPI, no Postman collection, no GraphQL surface, no webhook or event catalog, and no ACORD, AL3 or NGDS reference was found. Distribution integration runs through price-comparison-website connections and partner agreements, not through a published developer program.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: Admiral Group
nav: Providers
network: true
overview: 'Admiral Group is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, United Kingdom, Property and Casualty, Motor Insurance, and Home Insurance.


  Admiral Group''s developer surface includes support, engineering blog, and 25 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 18.4
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 18.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 30.3
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/admiral-group/refs/heads/main/screenshots/admiral-group-2026-07-25T181651.png
security:
- kind: domain-security
  name: Admiral Group Domain Security
  slug: admiral-group-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Admiral Group Vulnerability Disclosure
  slug: admiral-group-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: admiral-group
tags:
- Insurance
- United Kingdom
- Property and Casualty
- Motor Insurance
- Home Insurance
- Pet Insurance
- Travel Insurance
- Carrier
- Personal Lines
- Price Comparison
- Embedded Insurance
- Consumer Lending
- Underwriting
- Claims
- Company
website: https://www.admiralgroup.co.uk/
---
