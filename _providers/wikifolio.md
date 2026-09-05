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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wikifolio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.wikifolio.com
- group: company
  title: ''
  type: Blog
  url: https://www.wikifolio.com/en/int/blog
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.wikifolio.com/en/int/faq
- group: start
  title: ''
  type: GettingStarted
  url: https://www.wikifolio.com/en/int/how-to-invest/how-it-works
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.wikifolio.com/en/int/legal/gtc
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.wikifolio.com/en/int/legal/disclaimer
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wikifolio-llms.txt
created: '2026-07-17'
description: wikifolio (wikifolio Financial Technologies AG) is a European social- and copy-trading platform that lets everyday investors follow, compare, and invest in the strategies of experienced traders. Traders build virtual portfolios ("wikifolios") that are published transparently; in Germany, Austria, and Switzerland the best-performing wikifolios can be securitized as exchange-listed wikifolio certificates that investors buy through their bank or broker. The platform surfaces thousands of trading ideas with published rules, fees, and live performance tracking. wikifolio was surfaced as a portfolio company of Speedinvest and is profiled in the API Evangelist network; it does not appear to publish a public developer API at this time.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wikifolio.png
layout: provider
modified: '2026-07-21'
name: Wikifolio
nav: Providers
network: true
overview: 'Wikifolio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Social Trading, Copy Trading, and Investing.


  Wikifolio''s developer surface includes engineering blog, getting-started guide, and 6 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 12.0
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 23.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wikifolio/refs/heads/main/screenshots/wikifolio-2026-09-02T170744.png
security:
- kind: domain-security
  name: Wikifolio Domain Security
  slug: wikifolio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wikifolio
tags:
- Company
- Fintech
- Social Trading
- Copy Trading
- Investing
- Wealth Management
- Certificates
- Europe
website: https://www.wikifolio.com
---
