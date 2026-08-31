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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qsic-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.getqsic.com/
- group: company
  title: ''
  type: About
  url: https://www.getqsic.com/about-us
- group: company
  title: ''
  type: Blog
  url: https://www.getqsic.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.getqsic.com/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.getqsic.com/faqs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.getqsic.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getqsic.com/privacy-policy-26
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getqsic
- group: operate
  title: ''
  type: StatusPage
  url: https://status.getqsic.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.getqsic.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/qsic-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/qsic-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/qsic-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/qsic-rate-limits.yml
coverage:
  checked: '2026-08-26'
  detail: 'Qsic sells a managed in-store audio and retail media service, not a developer product: the Webflow marketing site has no developer, docs or API route (/developers, /docs and /api all 404), no docs or developer subdomain resolves, and the one live API host, api.getqsic.com, is the product''s own undocumented backend that answers anonymous requests with a bare JSON error envelope.'
  evidence:
  - status: 404
    url: https://www.getqsic.com/developers
  - status: 404
    url: https://www.getqsic.com/docs
  - status: 404
    url: https://api.getqsic.com/openapi.json
  - status: 200
    url: https://api.getqsic.com/health
  - status: 404
    url: https://www.getqsic.com/llms.txt
  - status: 404
    url: https://www.getqsic.com/.well-known/agent-card.json
  reason: no-developer-program
  state: none
created: '2026-08-26'
description: Qsic (styled QSIC) is an Australian-founded, AI-driven in-store audio and retail media platform, headquartered in Melbourne with a North American office in Dallas, Texas. The platform blends curated music, targeted audio advertising and store-level intelligence, deploying either over a retailer's existing speaker infrastructure or over premium smart speakers, and adapting playback to ambient conditions, dayparts and shopper behaviour. Qsic sells three connected products — In-Store Audio, Ads and Intelligence — and positions the combination as a way to turn physical stores into measurable retail media networks with store-level performance reporting and demand-side platform integration. Publicly reported deployments include 7-Eleven ("Gulp Radio"), Dollar General, Coles Liquor and Mecca. Qsic runs a live JSON API host at api.getqsic.com and a Vanta-hosted trust center, but publishes no public developer portal, API reference or machine-readable specification as of this profile.
image: https://cdn.prod.website-files.com/67dd6fe7bd7e331b5970b9a2/67e163850b12009683e71450_Webclip.png
layout: provider
modified: '2026-08-26'
name: Qsic
nav: Providers
network: true
overview: 'Qsic is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail Media, In-Store Audio, Advertising, and Audio.


  Qsic''s developer surface includes engineering blog, support, and 13 more developer resources.'
plans:
- name: Qsic Plans Pricing
  plan_count: 0
  slug: qsic-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Qsic Rate Limits
  slug: qsic-rate-limits
score:
  band: emerging
  composite: 11.0
  coverage:
    artifact_dirs: 8
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
    operational_transparency: 2.6
  previous_composite: 11.0
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Qsic Domain Security
  slug: qsic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Qsic Trust Center
  slug: qsic-trust-center
  summary_line: trust center published
slug: qsic
tags:
- Company
- Retail Media
- In-Store Audio
- Advertising
- Audio
- Retail
- Music
- Media
- Marketing
- Advertising Technology
website: https://www.getqsic.com/
---
