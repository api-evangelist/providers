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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.1
  scored_at: '2026-09-23'
api_count: 1
apis:
- description: A live, anonymously reachable Model Context Protocol endpoint served from the atma.io marketing site (Avery Dennison's connected product cloud and Digital Product Passport brand). It is the Wix-platfo
  name: atma.io Site MCP
  slug: atma-io-site-mcp
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.averydennison.com
- group: start
  title: ''
  type: Portal
  url: https://developer.averydennison.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/averydennison
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/avery-dennison/
- group: company
  title: ''
  type: Blog
  url: https://www.averydennison.com/en/home/news/company-blog.html
- group: operate
  title: ''
  type: PressReleases
  url: https://www.averydennison.com/en/home/news/press-releases.html
- group: operate
  title: ''
  type: Support
  url: https://www.averydennison.com/en/home/contact-us.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.averydennison.com/en/home/legal-and-privacy-notices.html
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/avery-dennison/refs/heads/main/security/avery-dennison-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/avery-dennison-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/avery-dennison/refs/heads/main/well-known/avery-dennison-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/avery-dennison-well-known.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/avery-dennison/refs/heads/main/conformance/avery-dennison-conformance.yml
  title: ''
  type: Conformance
  url: conformance/avery-dennison-conformance.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/avery-dennison/refs/heads/main/plans/avery-dennison-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/avery-dennison-plans-pricing.yml
coverage:
  checked: '2026-09-18'
  detail: The developer portal developer.averydennison.com 302s every path to an Okta sign-in (averydennison.okta.com), and the atma.io API reference docs.atma.io 302s to an Auth0 login at login.atma.io with audience https://open.atma.io, an API gateway that serves no anonymous document — the only public machine-readable surfaces are the identity provider's OIDC discovery and a Wix-platform llms.txt/MCP on the marketing site.
  evidence:
  - status: 302
    url: https://developer.averydennison.com/developers/
  - status: 302
    url: https://docs.atma.io/
  - status: 404
    url: https://open.atma.io/openapi.json
  - status: 200
    url: https://www.averydennison.com/en/home.html
  reason: partner-login
  state: gated
created: '2026-01-01'
description: Avery Dennison is a global materials science and manufacturing company specializing in the design and manufacture of labeling and functional materials, packaging, and intelligent labels. Its RFID and digital-identification business runs atma.io, a connected product cloud that assigns digital IDs to physical items and underpins its Digital Product Passport offering; the atma.io API is gated behind an OAuth 2.0 login and no public contract is published.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/avery-dennison.png
layout: provider
mcp_servers:
- description: ''
  name: atma.io (Wix Site MCP)
  slug: atmaio-wix-site-mcp
modified: '2026-09-18'
name: Avery Dennison
nav: Providers
network: true
overview: 'Avery Dennison publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Fortune 500, IoT, RFID, Labels, and Supply Chain.


  Avery Dennison''s developer surface includes developer portal, engineering blog, support, and 9 more developer resources.'
plans:
- name: Avery Dennison Plans Pricing
  plan_count: 0
  slug: avery-dennison-plans-pricing
press:
- date: ''
  title: Avery Dennison Announces Strategic $75 Million ...
  url: https://www.businesswire.com/news/home/20260427581185/en/Avery-Dennison-Announces-Strategic-%2475-Million-Investment-in-Wiliot-to-Scale-Physical-AI
- date: ''
  title: 'From problem solving to capability building: How AI is ...'
  url: https://www.averydennison.com/en/home/news/leadership-perspectives/nick-colisto/from-problem-solving-capability-building-ai.html
- date: ''
  title: Avery Dennison
  url: https://www.facebook.com/AveryDennisonCorporation/posts/we-are-pleased-to-announce-that-avery-dennison-has-made-a-significant-strategic-/1432150978954408/
- date: ''
  title: Avery Dennison adopts enterprise automation
  url: https://www.tcs.com/what-we-do/industries/manufacturing/case-study/intelligent-enterprise-robotic-process-automation
- date: ''
  title: Avery Dennison's atma.io adds new ChatGPT and AI ...
  url: https://rfid.averydennison.com/en/home/news-insights/press-releases/avery-dennisons-atma-io-adds-new-chatgpt-and-ai-features-to-help-manage-billion-of-items-across-its-connected-product-cloud.html
random_paper: 6
rate_limits:
- limit_count: 0
  name: Avery Dennison Rate Limits
  slug: avery-dennison-rate-limits
score:
  band: emerging
  composite: 17.9
  coverage:
    artifact_dirs: 13
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 75.9
    operational_transparency: 2.6
  previous_composite: 17.9
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/avery-dennison/refs/heads/main/screenshots/avery-dennison-2026-07-25T202123.png
security:
- kind: authentication
  name: Avery Dennison Authentication
  slug: avery-dennison-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Avery Dennison Domain Security
  slug: avery-dennison-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: avery-dennison
tags:
- Fortune 500
- IoT
- RFID
- Labels
- Supply Chain
- Manufacturing
- Digital Product Passport
website: https://www.averydennison.com
---
