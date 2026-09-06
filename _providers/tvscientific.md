---
access_model:
  confidence: medium
  label: Gated
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://api.tvscientific.app/v1/
  - https://www.tvscientific.com/ctv-demo
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: The REST API behind the tvScientific Campaign Management UI, named by tvScientific's own status page as the "Campaign Management API" component running at api.tvscientific.app. Two major versions serv
  name: tvScientific Campaign Management API
  slug: tvscientific-campaign-management-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://tvscientific.com
- group: company
  title: ''
  type: Blog
  url: https://www.tvscientific.com/insight
- group: start
  title: ''
  type: GettingStarted
  url: https://www.tvscientific.com/academy
- group: operate
  title: ''
  type: Support
  url: https://www.tvscientific.com/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.tvscientific.com/
- group: start
  title: ''
  type: Login
  url: https://tvscientific.app
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tvScientific
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tvscientific.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tvscientific-lifecycle.yml
- group: design
  title: ''
  type: Components
  url: components/tvscientific-components.yml
- group: build
  title: ''
  type: Packages
  url: packages/tvscientific-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/tvscientific-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tvscientific-llms.txt
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tvscientific.com/platform-master-agreement-demand
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tvscientific.com/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.tvscientific.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/tvscientific-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tvscientific-domain-security.yml
created: '2026-07-17'
description: 'tvScientific is a connected-TV (CTV) advertising platform for performance marketers, pairing premium streaming-TV inventory with AI-powered bidding and optimization and outcome-based measurement so brands can run television campaigns against measurable goals like sales, app installs, and site traffic. It positions itself on "premium inventory, AI-powered optimization, and radical transparency," and offers a self-serve buying platform plus an academy and reporting resources for advertisers and agencies. Originally surfaced as a portfolio company of Norwest Venture Partners, it now brands itself "tvScientific by Pinterest" after Pinterest completed its acquisition of the company in February 2026. tvScientific runs a real Campaign Management REST API at api.tvscientific.app — named as a component on its own status page — whose v1 and v2 version roots publicly enumerate 50 resource collections covering campaigns, line items, creatives, audiences, targeting, bid strategies, billing
  and accounts. It publishes no developer program around it: no portal, no API reference, no OpenAPI or GraphQL contract, no SDK, no CLI, and no MCP or agent surface. Every collection but one is credentialed, both documentation hosts sit behind a customer login, and the machine-readable operational signal is limited to an Atlassian Statuspage API and a first-party Google Tag Manager measurement pixel.'
image: https://www.tvscientific.com/hubfs/Opengraph.jpg
layout: provider
modified: '2026-08-12'
name: Tvscientific
nav: Providers
network: true
overview: 'Tvscientific publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, Connected TV, CTV, and Streaming.


  Tvscientific''s developer surface includes engineering blog, getting-started guide, support, and 15 more developer resources.'
plans:
- name: Tvscientific Plans Pricing
  plan_count: 0
  slug: tvscientific-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Tvscientific Rate Limits
  slug: tvscientific-rate-limits
score:
  band: emerging
  composite: 22.1
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 22.1
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tvscientific/refs/heads/main/screenshots/tvscientific-2026-09-02T164602.png
security:
- kind: authentication
  name: Tvscientific Authentication
  slug: tvscientific-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Tvscientific Domain Security
  slug: tvscientific-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Tvscientific Trust Center
  slug: tvscientific-trust-center
  summary_line: trust center published
slug: tvscientific
tags:
- Company
- Advertising
- Connected TV
- CTV
- Streaming
- Performance Marketing
- AdTech
- Measurements
- Campaign Management
- Real-Time Bidding
- Attribution
website: https://tvscientific.com
---
